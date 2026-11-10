# Cyber-Cop / Corporation — Atlas 40

**[Русский](#по-русски) | [English](#english)**

## По-русски

Автономный интерактивный атлас неофициальной модификации игры **Cyber-Cop / Corporation** для Sega Mega Drive / Genesis, включающий **32 карты** двух кампаний: Original и Amiga Mission Disk.

Атлас поддерживает русский и английский языки, выбор клеток, описание предметов и противников, изображения панелей, подсказки по кодам и уровню доступа, а также переключение кампаний с сохранением положения просмотра. Все изображения уже встроены в HTML. Никаких серверных приложений или домашних IP-адресов не требуется.

**Сайт после публикации:** https://valetos2.github.io/cyber-cop-atlas/

**[Полный архив с PNG, JSON и CSV](https://valetos2.github.io/cyber-cop-atlas/downloads/Cyber-Cop_Atlas40_full.zip)** (ссылка заработает после первой публикации).

### Один раз настроить публикацию

1. Открыть **Settings → Pages → Build and deployment** и выбрать **Source: GitHub Actions**.
2. В корне репозитория выбрать **Add file → Upload files**, перетащить исходный архив Atlas 40, назвать его **точно** `Cyber-Cop_Atlas40_full.zip` (без `(1)`), затем нажать **Commit changes** в `main`.
3. На вкладке **Actions** запустится **Publish Atlas 40 to GitHub Pages**. После успешного завершения сайт откроется по адресу выше.

**Ничего распаковывать вручную и загружать 984 PNG по одному не нужно.** Workflow проверит ZIP, подготовит `index.html`, обе языковые страницы, данные карт и полный ZIP для скачивания, после чего опубликует сайт. Следующие обновления потребуют только заменить тот же ZIP одним коммитом (при обновлении через веб-интерфейс можно удалить старый ZIP и загрузить новый).

На момент подготовки этот репозиторий содержит скрипты публикации; **без загруженного ZIP сайт ещё не опубликован**.

Исходники генератора Atlas 40 находятся в основном [репозитории модификации](https://github.com/Valetos2/Cyber-Cop-Genesis-mod/tree/main/atlas39). Этот репозиторий предназначен только для **распространения готового атласа**.

Оригинальные игровые изображения и звук принадлежат их правообладателям. Атлас — независимый фанатский проект, не связанный с первоначальными разработчиками и издателями.

## English

A standalone bilingual, interactive **32-map** atlas for the unofficial Sega Genesis / Mega Drive *Cyber-Cop / Corporation* improvement project, covering both the original campaign and the Amiga Mission Disk adaptation.

Once deployed, open https://valetos2.github.io/cyber-cop-atlas/ for the interactive atlas. Download the complete offline ZIP from [the download link](https://valetos2.github.io/cyber-cop-atlas/downloads/Cyber-Cop_Atlas40_full.zip).

To deploy: enable **Settings → Pages → Source: GitHub Actions**, then upload the original Atlas 40 ZIP to the repository root under the exact name `Cyber-Cop_Atlas40_full.zip`. Commit it to `main`; the workflow will unpack and publish the complete site automatically. No external dependencies are required for the finished viewer.

This is an unofficial fan atlas. Rights to the original game assets remain with their respective holders.
