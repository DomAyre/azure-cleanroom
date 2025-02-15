﻿// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

using System.Net.Http.Headers;
using System.Security.Cryptography;
using System.Security.Cryptography.Cose;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace CoseUtils;

public static class Cose
{
    public static byte[] Sign(CoseSignRequest request)
    {
        var cert = X509Certificate2.CreateFromPem(request.Certificate, request.PrivateKey);
        var privateKey = ECDsa.Create();
        privateKey.ImportFromPem(request.PrivateKey);

        CoseHeaderMap protectedHeaders = request.ProtectedHeaders != null ?
            AddHeaders(request.ProtectedHeaders) : new();
        CoseHeaderMap unprotectedHeaders = request.UnprotectedHeaders != null ?
            AddHeaders(request.UnprotectedHeaders) : new();

        try
        {
            var algorithm = (Algorithms)Enum.Parse(typeof(Algorithms), request.Algorithm);
            protectedHeaders.Add(CoseHeaderLabel.Algorithm, (int)algorithm);
            protectedHeaders.Add(CoseHeaderLabel.KeyIdentifier, FingerprintCertificate(cert));
        }
        catch (ArgumentException)
        {
            throw new Exception(
                $"{request.Algorithm} is not supported, supported algorithms " +
                $"are: ES256, ES384, ES512 and EdDSA.");
        }

        var signer = new CoseSigner(
            privateKey,
            HashAlgorithmName.SHA384,
            protectedHeaders,
            unprotectedHeaders);

        var payload = request.Payload ?? string.Empty;

        var message = CoseSign1Message.SignEmbedded(Encoding.ASCII.GetBytes(payload), signer);
        return message;
    }

    public static bool Verify(CoseSign1Message message, string pemCert)
    {
        var cert = X509Certificate2.CreateFromPem(pemCert);
        ECDsa? publicKey = cert.GetECDsaPublicKey();
        if (publicKey == null)
        {
            throw new Exception("Certificate does not contain ECDsa public key.");
        }

        bool result = message.VerifyEmbedded(publicKey);
        return result;
    }

    public static Task<byte[]> CreateGovCoseSign1Message(
        string certificate,
        string privateKey,
        GovMessageType messageType,
        string? payload,
        string? proposalId = null)
    {
        var createdAt = ((DateTimeOffset)DateTime.UtcNow).ToUnixTimeSeconds().ToString();
        Dictionary<string, string> protectedHeaders = new()
        {
            { "ccf.gov.msg.type", messageType.Value },
            { "ccf.gov.msg.created_at", createdAt }
        };

        if (!string.IsNullOrEmpty(proposalId))
        {
            protectedHeaders["ccf.gov.msg.proposal_id"] = proposalId;
        }

        var result = Sign(new CoseSignRequest
        {
            Algorithm = "ES384",
            Certificate = certificate,
            PrivateKey = privateKey,
            ProtectedHeaders = protectedHeaders,
            Payload = payload
        });

        return Task.FromResult(result);
    }

    public static Task<byte[]> CreateRecoveryCoseSign1Message(
        string certificate,
        string privateKey,
        RecoveryMessageType messageType,
        string? payload)
    {
        var createdAt = ((DateTimeOffset)DateTime.UtcNow).ToUnixTimeSeconds().ToString();
        Dictionary<string, string> protectedHeaders = new()
        {
            { "ccf.recovery.msg.type", messageType.Value },
            { "ccf.recovery.msg.created_at", createdAt }
        };

        var result = Sign(new CoseSignRequest
        {
            Algorithm = "ES384",
            Certificate = certificate,
            PrivateKey = privateKey,
            ProtectedHeaders = protectedHeaders,
            Payload = payload
        });

        return Task.FromResult(result);
    }

    public static HttpRequestMessage CreateHttpRequestMessage(string path, byte[] content)
    {
        HttpRequestMessage request = new(HttpMethod.Post, path);
        request.Content = new ByteArrayContent(content);
        request.Content.Headers.ContentType =
            new MediaTypeWithQualityHeaderValue("application/cose");
        return request;
    }

    private static CoseHeaderMap AddHeaders(Dictionary<string, string> headers)
    {
        CoseHeaderMap headersMap = new();

        foreach (var header in headers)
        {
            int parsedValue;
            if (int.TryParse(header.Value, out parsedValue))
            {
                headersMap.Add(new CoseHeaderLabel(header.Key), parsedValue);
            }
            else
            {
                headersMap.Add(new CoseHeaderLabel(header.Key), header.Value);
            }
        }

        return headersMap;
    }

    private static byte[] FingerprintCertificate(X509Certificate2 cert)
    {
        using (var sha256 = SHA256.Create())
        {
            var hash = sha256.ComputeHash(cert.RawData);
            var convertedHash = BitConverter.ToString(hash).Replace("-", string.Empty);
            return Encoding.ASCII.GetBytes(convertedHash.ToLower());
        }
    }
}
