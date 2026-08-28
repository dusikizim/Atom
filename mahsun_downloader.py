import re
import sys
import time
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, Error as PlaywrightError

AD_PATTERNS = [
    "bsky.app", "bluesky", "twitter.com", "x.com", "telegram.org",
    "doubleclick", "googlesyndication", "analytics", "gtag",
    "adcash", "popads", "propeller", "adnxs", "histats"
]

def check_active_domain(context):
    test_urls = [
        "https://mahsun-amp.click/",
        "https://mahsunsports.xyz/",
        "https://mahsunsports46.xyz/",
    ]

    print("\n🔍 Mahsun Sports domain kontrolü yapılıyor...\n")
    page = context.new_page()
    page.on("popup", lambda popup: popup.close())

    for url in test_urls:
        try:
            print(f"   Deniyor → {url}", end=" ")
            response = page.goto(url, timeout=8000, wait_until="domcontentloaded")
            if response and response.ok:
                print("✅ BULUNDU!")
                page.close()
                return url.rstrip("/")
            else:
                print(f"❌ HTTP {response.status if response else 'Yok'}")
        except Exception as e:
            print(f"❌ {str(e)[:40]}")

    page.close()
    return "https://mahsun-amp.click"


def main():
    with sync_playwright() as p:
        print("🚀 Mahsun Sports M3U8 İndirici Başlatılıyor...\n")
        
        browser_args = [
            '--autoplay-policy=no-user-gesture-required',
            '--disable-blink-features=AutomationControlled',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--disable-infobars',
            '--window-size=1366,768',
        ]
        
        browser = p.chromium.launch(headless=True, args=browser_args)
        
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            ignore_https_errors=True,
            viewport={'width': 1366, 'height': 768},
            locale='tr-TR',
            timezone_id='Europe/Istanbul',
            extra_http_headers={
                'Referer': 'https://mahsun-amp.click/',
                'Origin': 'https://mahsun-amp.click'
            }
        )

        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """)

        domain = check_active_domain(context)
        print(f"\n📡 Kullanılan Domain: {domain}\n")

        channels = {
            "androstreamlivebs1": ("BeIN Sports 1", "BeinSports"),
            "androstreamlivebs2": ("BeIN Sports 2", "BeinSports"),
            "androstreamlivebs3": ("BeIN Sports 3", "BeinSports"),
            "androstreamlivebs4": ("BeIN Sports 4", "BeinSports"),
            "androstreamlivebs5": ("BeIN Sports 5", "BeinSports"),
            "androstreamlivebsm1": ("BeIN Sports Max 1", "BeinSports"),
            "androstreamlivebsm2": ("BeIN Sports Max 2", "BeinSports"),
            "androstreamlivebsh": ("BeIN Sports Haber", "BeinSports"),
            "androstreamlivess1": ("S Sport 1", "S Sports"),
            "androstreamlivess2": ("S Sport 2", "S Sports"),
            "androstreamlivessplus1": ("S Sport Plus", "S Sports"),
            "androstreamlivets": ("Tivibu Spor", "Tivibu"),
            "androstreamlivets1": ("Tivibu Spor 1", "Tivibu"),
            "androstreamlivets2": ("Tivibu Spor 2", "Tivibu"),
            "androstreamlivets3": ("Tivibu Spor 3", "Tivibu"),
            "androstreamlivets4": ("Tivibu Spor 4", "Tivibu"),
            "androstreamlivesm1": ("Spor Smart 1", "Smart Sports"),
            "androstreamlivesm2": ("Spor Smart 2", "Smart Sports"),
            "androstreamlivees1": ("Euro Sport 1", "Eurosport"),
            "androstreamlivees2": ("Euro Sport 2", "Eurosport"),
            "androstreamliveidm": ("Idman TV", "Azerbaycan"),
            "androstreamlivecbcs": ("CBC Sport", "Azerbaycan"),
            "androstreamlivetrt1": ("TRT 1", "TRT"),
            "androstreamlivetrts": ("TRT Spor", "TRT"),
            "androstreamlivetrtsy": ("TRT Spor Yildiz", "TRT"),
            "androstreamliveatv": ("ATV", "Ulusal"),
            "androstreamliveas": ("A Spor", "Ulusal"),
            "androstreamlivea2": ("A2", "Ulusal"),
            "androstreamliveht": ("HT Spor", "Ulusal"),
            "androstreamlivenba": ("NBA TV", "NBA"),
            "androstreamlivetv8": ("TV 8", "Ulusal"),
            "androstreamlivetv85": ("TV 8.5", "Ulusal"),
            "androstreamlivetb": ("tabii Spor", "tabii"),
            "androstreamlivetb1": ("tabii Spor 1", "tabii"),
            "androstreamlivetb2": ("tabii Spor 2", "tabii"),
            "androstreamlivetb3": ("tabii Spor 3", "tabii"),
            "androstreamliveexn": ("Exxen TV", "Exxen"),
            "androstreamliveexn1": ("Exxen Sports 1", "Exxen"),
            "androstreamliveexn2": ("Exxen Sports 2", "Exxen"),
            "androstreamliveexn3": ("Exxen Sports 3", "Exxen"),
            "androstreamliveexn4": ("Exxen Sports 4", "Exxen"),
        }

        channel_results = {}
        output_filename = "kanallar7.m3u8"
        active_cdn_host = "andro.evrenesoglu57.click"  # Bilinen temel CDN

        for i, (channel_id, (channel_name, category)) in enumerate(channels.items(), 1):
            page = None
            try:
                            if skip_btn.is_visible():
                                skip_btn.click(timeout=300)
                        except:
                            pass

                        page.wait_for_timeout(400)

                    chosen_m3u8 = None
                    if captured_urls:
                        chosen_m3u8 = captured_urls[-1]
                        parsed = urlparse(chosen_m3u8)
                        if parsed.netloc:
                            active_cdn_host = parsed.netloc

                    # Otomatik tamamlama
                    if not chosen_m3u8 and active_cdn_host:
                        if channel_id == "androstreamlivebs1":
                            chosen_m3u8 = f"https://{active_cdn_host}/checklist/batutest.m3u8"
                        else:
                            chosen_m3u8 = f"https://{active_cdn_host}/checklist/{channel_id}.m3u8"
                        print(f"-> ⚡ OK (Oto-Çözüldü: {chosen_m3u8})")
                    elif chosen_m3u8:
                        print(f"-> ✅ OK ({chosen_m3u8})")
                    else:
                        print("-> ❌ Link bulunamadı")

                    if chosen_m3u8:
                        channel_results[channel_id] = (channel_name, category, chosen_m3u8)

                except Exception as e:
                    print(f"-> ❌ Hata: {str(e)[:50]}")
                finally:
                    page.remove_listener("request", handle_request)
                    page.close()

            except Exception as e:
                print(f"-> ❌ Genel hata: {e}")
                if page:
                    page.close()
                continue

        browser.close()

        # BeIN Sports 1 kontrolü (Garantör)
        if "androstreamlivebs1" not in channel_results:
            bs1_url = f"https://{active_cdn_host}/checklist/batutest.m3u8"
            channel_results["androstreamlivebs1"] = ("BeIN Sports 1", "BeinSports", bs1_url)
            print(f"\n💎 BeIN Sports 1 Garantör ile eklendi → {bs1_url}")

        # Playlist oluşturma
        m3u_content = []
        for ch_id, (ch_name, ch_cat) in channels.items():
            if ch_id in channel_results:
                _, _, stream_url = channel_results[ch_id]
                m3u_content.append(f'#EXTINF:-1 tvg-name="{ch_name}" group-title="{ch_cat}",{ch_name}')
                m3u_content.append(stream_url)

        if m3u_content:
            header = f"""#EXTM3U
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
#EXTVLCOPT:http-referrer=https://mahsun-amp.click/
#EXT-X-USER-AGENT:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
#EXT-X-REFERER:https://mahsun-amp.click/"""

            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(header + "\n\n")
                f.write("\n".join(m3u_content))
            
            print(f"\n🎉 Tamamlandı! {len(channel_results)}/{len(channels)} kanal kaydedildi → {output_filename}")
        else:
            print("\n❌ Hiçbir kanal için m3u8 linki yakalanamadı.")

if __name__ == "__main__":
    main()
