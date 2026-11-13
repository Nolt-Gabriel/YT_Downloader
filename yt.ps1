
param(
    [string]$link,
    [string]$opcao
)

$pastamusic = Join-Path $env:USERPROFILE "Music\yt-dlp"
$pastavideo = Join-Path $env:USERPROFILE "Videos\yt-dlp"

New-Item -ItemType Directory -Force -Path $pastamusic | Out-Null
New-Item -ItemType Directory -Force -Path $pastavideo | Out-Null

$pastaTools = Join-Path $PSScriptRoot "tools"

$ytDlp = Join-Path $pastaTools "yt-dlp.exe"

$env:PATH = "$pastaTools;$env:PATH"

Write-Output "INICIANDO"

switch ($opcao) {

    "1" {
        Write-Output "BAIXANDO_AUDIO"
        Write-Output "PASTA_DESTINO|$pastamusic"

        & $ytDlp `
            --newline `
            --progress `
            --progress-template "download:PROGRESSO|%(progress._percent_str)s|%(progress._speed_str)s|%(progress._downloaded_bytes_str)s|%(progress._total_bytes_str)s|%(progress._eta_str)s" `
            -P $pastamusic `
            -x `
            --audio-format mp3 `
            $link
    }

    "2" {
        Write-Output "BAIXANDO_VIDEO"
        Write-Output "PASTA_DESTINO|$pastavideo"

        & $ytDlp `
            --newline `
            --progress `
            --progress-template "download:PROGRESSO|%(progress._percent_str)s|%(progress._speed_str)s|%(progress._downloaded_bytes_str)s|%(progress._total_bytes_str)s|%(progress._eta_str)s" `
            -P $pastavideo `
            -f "bv*+ba/b" `
            --merge-output-format mp4 `
            $link
    }

    default {
        Write-Output "OPCAO_INVALIDA"
        exit 1
    }
}

$codigo = $LASTEXITCODE

if ($codigo -eq 0) {
    Write-Output "DOWNLOAD_CONCLUIDO"
    exit 0
}
else {
    Write-Output "DOWNLOAD_ERRO"
    exit $codigo
}
