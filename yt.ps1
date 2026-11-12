
param(
    [string]$link,
    [string]$opcao
)

$pastamusic = "C:\Users\Nicholas Gabriel\Music\yt-dlp"
$pastavideo = "C:\Users\Nicholas Gabriel\Videos\yt-dlp"

Write-Output "INICIANDO"

switch ($opcao) {

    "1" {
        Write-Output "BAIXANDO_AUDIO"

        & yt-dlp `
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

        & yt-dlp `
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
