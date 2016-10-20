# HttpCovertChannels

Исследования скрытых каналов в протоколе HTTP и веб-приложениях.
Результаты исследований вошли в рейтинг [Top 10 Web Hacking Techniques of 2014](https://www.whitehatsec.com/blog/top-10-web-hacking-techniques-of-2014/).

## Статьи

1. [Hooked Browser Network with BeEF and Google Drive](http://blog.beefproject.com/2016/01/hooked-browser-network-with-beef-and.html).
2. [Исследование возможности управления веб-браузерами на основе фрэймворка BeEF и облачного сервиса Google Drive](papers/pdm523.pdf).
 Д.Н. Колегов, О.В. Брославский, Н.Е. Олексов. ПДМ, 2015, № 4, 72–76.
3. [Скрытые каналы по времени на основе заголовков кэширования протокола HTTP](papers/pdm506.pdf).
Д.Н. Колегов, О.В. Брославский, Н.Е. Олексов.ПДМ, 2015, № 2, 71–85.
4. [Исследование скрытых каналов по времени на основе заголовков кэширования протокола HTTP в WEB API](papers/bit2.pdf).
Д.Н. Колегов, О.В. Брославский, Н.Е. Олексов. Безопасность информационных технологий. 2015. №4, декабрь. С. 13 – 18.

## Прототипы

### Фрэймворк BeEF
В качестве прототипа реализованы расширения и модули для [BeEF](https://github.com/beefproject/beef).

Расширения:
* [s2c-dns-tunnel](beef/extensions/s2c_dns_tunnel)
* [etag tunnel](beef/extensions/etag)

Модули:
* [s2c-dns-tunnel](beef/modules/s2c_dns_tunnel)
* [etag-client](beef/modules/etag_client)

### BeEF-Drive
[BeEF-Drive](https://github.com/tsu-iscd/beef-drive) - специльная версия BeEF, в которой потоки управления зараженными браузерами (зомби) реализуются через файловую систему Google Drive.

## Слайды выступлений на конференциях
1. [Hooked Browser Network with BeEF and Google Drive](http://www.slideshare.net/dnkolegov/zn27112015). Zero Nights 2015.
2. [Covert Timing Channels using HTTP Cache Headers](http://www.slideshare.net/dnkolegov/15112014-41633305). Zero Nights 2014.
3. [Covert Timing Channels based on HTTP Cache Headers](http://www.slideshare.net/dnkolegov/wh102014). Top 10 Web Hacking Techniques of 2014.

## Видео
1. [BeEF Hooked-Browser with Google Drive](https://www.youtube.com/watch?v=_RfBUEcvynM).
2. [ETag Tunnel: Server-to-Client](https://www.youtube.com/watch?v=W2qWA7XUzGQ).

## Авторы
* Denis Kolegov
* Oleg Broslavsky
* Nikita Oleksov
