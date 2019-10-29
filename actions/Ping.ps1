param(
	[parameter( ValueFromRemainingArguments = $true )]
	[string[]]$hostnames = $Env:ComputerName,
	[switch]$V,
	[switch]$h
)

if ( $h ) {
	Write-Host
	Write-Host "Ping.ps1,  Version 2.00"
	Write-Host "Ping any number of hosts and return false if any of the pings failed"
	Write-Host
	Write-Host "Usage:   " -NoNewline
	Write-Host "./Ping.ps1  [ hostname  [ hostname  [ ... ] ] ] -V" -ForegroundColor White
	Write-Host
	Write-Host "Where:   " -NoNewline
	Write-Host "hostname    " -ForegroundColor White -NoNewline
	Write-Host "is a host or list of hosts to be pinged"
	Write-Host "                     (default: local computer)"
	Write-Host "         -V          " -ForegroundColor White -NoNewline
	Write-Host "shows each host's name, IP address and result"
	Write-Host
	Write-Host "Note:    Return code is 0 if pings to all hosts were successful,"
	Write-Host "         1 if any ping failed or if help was requested."
	Write-Host
	Write-Host "Written by Rob van der Woude"
	Write-Host "http://www.robvanderwoude.com"
	Exit 1
}

function Ping-Host {
	param(
		[parameter( Mandatory = $true )]
		[string]$hostname
	)
	
	[boolean]$rc = $true
	
	try {
		$ping = ( New-Object Net.NetworkInformation.Ping ).SendPingAsync( $hostname )
		while ( -not ( $ping.IsCompleted ) ) {
			Start-Sleep -Seconds 1
		}
		if ( $V ) {
			Write-Host $hostname -NoNewline
			if ( $ping.Status -eq "RanToCompletion" ) { 
				Write-Host "`t" -NoNewline
				Write-Host $ping.Result.Address.IPAddressToString -NoNewline
				Write-Host "`t" -NoNewline
				Write-Host $ping.Result.Status
			} else {
				Write-Host "`tN/A`tFailed"
			}
		}
		if ( $ping.Result.Status -ne "Success" ) {
			$rc = $false
		}
	}
	catch {
		if ( $V ) {
			Write-Host $hostname -NoNewline
			Write-Host "`tN/A`tFailed"
			$rc = $false
		}
	}
	return $rc 
}

$result = 0
foreach ( $hostname in $hostnames ) {
	if ( -not ( Ping-Host $hostname ) ) {
		$result = 1
	}
}

Exit $result
