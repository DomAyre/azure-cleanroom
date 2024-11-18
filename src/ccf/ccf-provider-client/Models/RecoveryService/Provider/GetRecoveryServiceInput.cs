﻿// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

using System.Text.Json.Nodes;

namespace Controllers;

public class GetRecoveryServiceInput
{
    public string InfraType { get; set; } = default!;

    public JsonObject? ProviderConfig { get; set; }
}