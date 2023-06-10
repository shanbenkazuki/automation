import sqlite3

from datetime import datetime

# SQLiteデータベースに接続
conn = sqlite3.connect('moba_database.sqlite3')
cursor = conn.cursor()

# mlbbのデータを保存するテーブルを作成
cursor.execute('''
  CREATE TABLE IF NOT EXISTS unite_pokemon_info (
    name TEXT UNIQUE,
    name_en TEXT UNIQUE,
    style TEXT,
    article_url TEXT,
    image_url TEXT,
    created_at TEXT,
    updated_at TEXT
  )
''')

pokemon_urls = {
  "Tsareena": {"name": "アマージョ", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/tsareena", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Tsareena.png"},
  "Lucario": {"name": "ルカリオ", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/lucario", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/lucario.png"},
  "Aegislash": {"name": "ギルガルド", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/aegislash", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Aegislash.png"},
  "Hoopa": {"name": "フーパ", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/supporter/hoopa", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Hoopa.png"},
  "Pikachu": {"name": "ピカチュウ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/pikachu", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Pikachu.png"},
  "Ninetales": {"name": "キュウコン", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/ninetales", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Ninetales.png"},
  "Blissey": {"name": "ハピナス", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/supporter/blissey", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Blissey.png"},
  "Trevenant": {"name": "オーロット", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/trevenant", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Trevenant.png"},
  "Greedent": {"name": "ヨクバリス", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/greedent", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Greedent.png"},
  "Venusaur": {"name": "フシギバナ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/venusaur", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Venusaur.png"},
  "Blastoise": {"name": "カメックス", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/blastoise", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Blastoise.png"},
  "Wigglytuff": {"name": "プクリン", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/supporter/wigglytuff", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Wigglytuff.png"},
  "Machamp": {"name": "カイリキー", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/machamp", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Machamp.png"},
  "Slowbro": {"name": "ヤドラン", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/slowbro", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Slowbro.png"},
  "Garchomp": {"name": "ガブリアス", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/garchomp", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Garchomp.png"},
  "MrMime": {"name": "バリヤード", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/supporter/mr-mime", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/MrMime.png"},
  "Snorlax": {"name": "カビゴン", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/snorlax", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Snorlax.png"},
  "Gardevoir": {"name": "サーナイト", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/gardevoir", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Gardevoir.png"},
  "Charizard": {"name": "リザードン", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/charizard", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Charizard.png"},
  "Gengar": {"name": "ゲンガー", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/speedster/gengar", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Gengar.png"},
  "Talonflame": {"name": "ファイアロー", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/speedster/talonflame", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Talonflame.png"},
  "Cinderace": {"name": "エースバーン", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/cinderace", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Cinderace.png"},
  "Crustle": {"name": "イワパレス", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/defender/crustle", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Crustle.png"},
  "Zeraora": {"name": "ゼラオラ", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/speedster/zeraora", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Zeraora.png"},
  "Azumarill": {"name": "マリルリ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/azumarill", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Azumarill.png"},
  "Mamoswine": {"name": "マンムー", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/defender/mamoswine", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Mamoswine.png"},
  "Cramorant": {"name": "ウッウ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/attacker/cramorant", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Cramorant.png"},
  "Dragonite": {"name": "カイリュー", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/all-rounder/dragonite", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Dragonite.png"},
  "Absol": {"name": "アブソル", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/speedster/absol", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Absol.png"},
  "Greninja": {"name": "ゲッコウガ", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/greninja", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Greninja.png"},
  "Espeon": {"name": "エーフィ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/espeon", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Espeon.png"},
  "Sylveon": {"name": "ニンフィア", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/sylveon", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Sylveon.png"},
  "Decidueye": {"name": "ジュナイパー", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/decidueye", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Decidueye.png"},
  "Eldegoss": {"name": "ワタシラガ", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/supporter/eldegoss", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Eldegoss.png"},
  "Duraludon": {"name": "ジュラルドン", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/duraludon", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Duraludon.png"},
  "Delphox": {"name": "マフォクシー", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/delphox", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Delphox.png"},
  "Glaceon": {"name": "グレイシア", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/attacker/glaceon", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/07/Glaceon.png"},
  "Umbreon": {"name": "ブラッキー", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/defender/umbreon", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Umberon.png"},
  "Zacian": {"name": "ザシアン", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/zacian", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Zacian.png"},
  "Lapras": {"name": "ラプラス", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/defender/lapras", "image_url": "https://shanbenzzz.com/wp-content/uploads/2022/06/Lapras.png"},
  "Chandelure": {"name": "シャンデラ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/attacker/chandelure", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Chandelure.png"},
  "Clefable": {"name": "ピクシー", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/supporter/clefable", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Clefable.png"},
  "Comfey": {"name": "キュワワー", "style": "supporter", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/supporter/comfey", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Comfey.png"},
  "Mew": {"name": "ミュウ", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/attacker/mew", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Mew.png"},
  "Sableye": {"name": "ヤミラミ", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/supporter/sableye", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Sableye.png"},
  "Zoroark": {"name": "ゾロアーク", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/speedster/zoroark", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Zoroark.png"},
  "Dragapult": {"name": "ドラパルト", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/attacker/dragapult", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Dragapult.png"},
  "Scizor": {"name": "ハッサム", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/scizor", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Scizor.png"},
  "Tyranitar": {"name": "バンギラス", "style": "all-rounder", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/tyranitar", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Tyranitar.png"},
  "Goodra": {"name": "ヌメルゴン", "style": "defender", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/defender/goodra", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Goodra.png"},
  "Buzzwole": {"name": "マッシブーン", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/buzzwole", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Buzzwole.png"},
  "Urshifu": {"name": "ウーラオス", "style": "attacker", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/all-rounder/urshifu", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Urshifu.png"},
  "Dodrio": {"name": "ドードリオ", "style": "speedster", "article_url": "https://shanbenzzz.com/pokemon-unite/pokemon/style/speedster/dodrio", "image_url": "https://shanbenzzz.com/wp-content/uploads/2023/06/Dodrio.png"}
}

# データを追加
for pokemon, data in pokemon_urls.items():
  name_en = pokemon
  name = data['name']
  style = data['style']
  article_url = data['article_url']
  image_url = data['image_url']
  created_at = datetime.now().strftime('%Y-%m-%d')
  updated_at = datetime.now().strftime('%Y-%m-%d')

  # SQLクエリを実行してデータを追加
  try:
    cursor.execute(
      '''
      INSERT INTO unite_pokemon_info (name, name_en, style, article_url, image_url, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?)
      ''',
      (name, name_en, style, article_url, image_url, created_at, updated_at)
    )
  except sqlite3.IntegrityError:
    print(f"Duplicate entry: {name_en}")

# 変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()