function Create-Storage-Resources {
    param(
        [string]$resourceGroup,

        [string[]]$storageAccountNames,

        [string]$objectId,

        [switch]$enableHns,

        [switch]$allowSharedKeyAccess,

        [string]$kind = "StorageV2"
    )

    foreach ($storageAccountName in $storageAccountNames) {
        Write-Host "Creating storage account $storageAccountName in resource group $resourceGroup"
        $result = (az storage account create `
                --name $storageAccountName `
                --resource-group $resourceGroup `
                --min-tls-version TLS1_2 `
                --allow-shared-key-access $allowSharedKeyAccess `
                --kind $kind `
                --enable-hierarchical-namespace $enableHns)
        CheckLastExitCode
        $storageAccountResult = $result | ConvertFrom-Json

        Write-Host "Assigning 'Storage Blob Data Contributor' permissions to logged in user"
        az role assignment create --role "Storage Blob Data Contributor" --scope $storageAccountResult.id --assignee-object-id $objectId --assignee-principal-type $(Get-Assignee-Principal-Type)
        $storageAccountResult

        if ($env:GITHUB_ACTIONS -eq "true") {
            $sleepTime = 90
            Write-Host "Waiting for $sleepTime seconds for permissions to get applied"
            Start-Sleep -Seconds $sleepTime
        }
    }
}

function Get-Assignee-Principal-Type {
    if ($env:GITHUB_ACTIONS -eq "true") {
        return "ServicePrincipal"
    }
    else {
        return "User"
    }
}
