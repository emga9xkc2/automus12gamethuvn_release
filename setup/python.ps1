
function DownloadFile($url, $targetFile)
{
   [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
   $uri = New-Object "System.Uri" "$url"

   $request = [System.Net.HttpWebRequest]::Create($uri)

   $request.set_Timeout(15000) #15 second timeout

   $response = $request.GetResponse()

   $totalLength = [System.Math]::Floor($response.get_ContentLength()/1024)

   $responseStream = $response.GetResponseStream()

   $targetStream = New-Object -TypeName System.IO.FileStream -ArgumentList $targetFile, Create

   $buffer = new-object byte[] 10KB

   $count = $responseStream.Read($buffer,0,$buffer.length)

   $downloadedBytes = $count

   while ($count -gt 0)

   {

       $targetStream.Write($buffer, 0, $count)

       $count = $responseStream.Read($buffer,0,$buffer.length)

       $downloadedBytes = $downloadedBytes + $count

       Write-Progress -activity "Downloading file '$($url.split('/') | Select -Last 1)'" -status "Downloaded ($([System.Math]::Floor($downloadedBytes/1024))K of $($totalLength)K): " -PercentComplete ((([System.Math]::Floor($downloadedBytes/1024)) / $totalLength)  * 100)

   }

   Write-Progress -activity "Finished downloading file '$($url.split('/') | Select -Last 1)'"

   $targetStream.Flush()

   $targetStream.Close()

   $targetStream.Dispose()

   $responseStream.Dispose()

}

# This is the link to download Python 3.6.7 from Python.org
# See https://www.python.org/downloads/
$pythonUrl = "https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe"



# Installation Directory
# Some packages look for Python here
$targetDir = "$Env:USERPROFILE\AppData\Roaming\Python399\"




# create the download directory and get the exe file
$pythonNameLoc = $targetDir + "python399.exe"

$pythonExePathCaiTay = "$Env:USERPROFILE\AppData\Local\Programs\Python\Python39\python.exe"

$pythonExePath = $targetDir + "python399.exe"

Write-Output "Check file $pythonExePath and $pythonExePathCaiTay"

if (-not(Test-Path -Path $pythonExePath -PathType Leaf) -and -not(Test-Path -Path $pythonExePathCaiTay -PathType Leaf)) {

Write-Output "Check file $pythonNameLoc"

if (-not(Test-Path -Path $pythonNameLoc -PathType Leaf)) { 
    
    Write-Output "Create directory $targetDir"
    New-Item -ItemType directory -Path $targetDir -Force | Out-Null


    Write-Output "Download file $pythonUrl"    
    downloadFile $pythonUrl $pythonNameLoc
}


# These are the silent arguments for the install of python
# See https://docs.python.org/3/using/windows.html
$Arguments = @()
$Arguments += "/i"
$Arguments += 'InstallAllUsers="1"'
$Arguments += 'TargetDir="' + $targetDir + '"'
$Arguments += 'DefaultAllUsersTargetDir="' + $targetDir + '"'
$Arguments += 'AssociateFiles="1"'
$Arguments += 'PrependPath="1"'
$Arguments += 'Include_doc="1"'
$Arguments += 'Include_debug="1"'
$Arguments += 'Include_dev="1"'
$Arguments += 'Include_exe="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'InstallLauncherAllUsers="1"'
$Arguments += 'Include_lib="1"'
$Arguments += 'Include_pip="1"'
$Arguments += 'Include_symbols="1"'
$Arguments += 'Include_tcltk="1"'
$Arguments += 'Include_test="1"'
$Arguments += 'Include_tools="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += 'Include_launcher="1"'
$Arguments += "/passive"

Write-Output "Install Python"

Start-Sleep -Seconds 1000
Start-Process $pythonNameLoc -ArgumentList $Arguments -Wait

}else{
    Write-Output "Setup python ok"
}

Write-Output "Done"
Start-Sleep -Seconds 1000