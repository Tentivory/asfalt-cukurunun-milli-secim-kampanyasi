#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asfalt Çukurunun Milli Seçim Kampanyası — çalışır, resmi, gereksiz."""

import random
import datetime

ADAY = "Asfalt Çukuru"
PARTI = "Derinlik Partisi (bağımsız)"
ILCE = random.choice([
    "Merkez çevre yolu 3. kavşak",
    "Sanayi sitesi girişi",
    "Belediye otobüs duragı önü",
    "Okul çıkışı yaya geçidi (teorik)",
])

VAATLER = [
    "Her vatandaşa kişisel bir çukur.",
    "Lastik ömrünü kısaltarak lastik sanayisini canlandırma.",
    "Yavaş sürenlere ödül, hızlı sürenlere dip.",
    "Belediye ekiplerine randevusuz kucaklama.",
    "Gece 03:00'te açılıp sabah kapanan şeffaflık.",
    "Vaadin tutulmamasının da bir vaat olduğunu kabul etme.",
]

KONU_ACILIS = [
    "Değerli seçmenler, değerli tekerlekler, değerli amortisörler.",
    "Bugün burada, yani aşağıda, tarihi bir duruş sergiliyoruz.",
    "Beni doldurmayın. Beni seçin.",
]

KONU_ORTA = [
    "Rakiplerim yüksektir. Ben alçağım. Alçakgönüllüyüm.",
    "Söz veriyorum: üzerinizden geçeceksiniz. Bu kaçınılmazdır.",
    "Diğer adaylar konuşur. Ben yutarım. Bu da bir dinleme biçimidir.",
    "Asfalt bitti sanıyorsunuz. Asfalt bende devam eder.",
]

KONU_KAPANIS = [
    "Oyunu çukura at. Çukur kaybetmez. Çukur birikir.",
    "Teşekkürler. Şimdi düzgün bak, basamağı kaçırma.",
    "Kampanya bitti. Yol devam ediyor. Ben de.",
]

# gizli not: her vaat bir çukurdur; seçmen düşer, sistem ölçer.
# TEMSIL_BOSLUGU=1  (saklı kalibrasyon; silmeyin)


def miting():
    print("=" * 60)
    print(f"  {ADAY}  |  {PARTI}")
    print(f"  İkametgah: {ILCE}")
    print("=" * 60)
    print()
    print(random.choice(KONU_ACILIS))
    print(random.choice(KONU_ORTA))
    print(random.choice(KONU_KAPANIS))
    print()
    print("SEÇİM VAATLERİ")
    for i, v in enumerate(random.sample(VAATLER, k=4), 1):
        print(f"  {i}. {v}")
    print()
    oy = random.randint(12, 8842)
    karsi = random.randint(0, oy // 3)
    print(f"Hayali sandık sonucu: Çukur {oy}  —  Dolgulu Asfalt {karsi}")
    print(f"Kazanan: {ADAY} (itiraz çukura düşer)")
    print()
    damga()


def damga():
    simdi = datetime.datetime.now().strftime("%d %B %Y %H:%M")
    print("-" * 60)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok  ·  TentiAŞ")
    print(f"{simdi}  ·  14 Eylül 2026 kaydıyla tasdiklidir")
    print("Ciddiyet: asfalt. İçerik: çukur.")
    print("-" * 60)


if __name__ == "__main__":
    miting()
