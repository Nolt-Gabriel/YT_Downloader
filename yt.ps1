
param(
    [string]$link,
    [string]$opcao
)

Write-Output "Iniciando download..."

$pastamusic = "C:\Users\Nicholas Gabriel\Music"
$pastavideo = "C:\Users\Nicholas Gabriel\Videos\yt-dlp"
# Verifica qual opcao foi escolhida
switch ($opcao) {

    "1" {
        Write-Output "Baixando somente o audio..."

        yt-dlp -P $pastamusic -x --audio-format mp3 $link
    }

    "2" {
        Write-Output "Baixando somente o video..."

        yt-dlp -P $pastavideo -f "bv*+ba/b" --merge-output-format mp4 $link
    }

    default {
        Write-Output "Opcao invalida!"
        exit 1
    }
}

if ($LASTEXITCODE -eq 0) {
    Write-Output "Download concluido!"
}
else {
    Write-Output "Erro durante o download!"
    exit 1
}
