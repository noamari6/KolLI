# KolLi – בוט טלגרם שמדבר בקול שאתה בוחר 🎙️

## 🎯 מה זה?
אתה שולח לבוט הקלטת קול של מישהו → ואז כל טקסט שתשלח לו – הוא יקריא בקול הזה!

---

## 📦 מה יש בפרויקט:
- `bot.py` – הקוד הראשי של הבוט
- `config.py` – טוען את הטוקן מתוך משתנה סביבה
- `.env` – קובץ מקומי עם הטוקן (לא לעלות לגיטהאב!)
- `.gitignore` – מונע חשיפה של `.env` וקבצים זמניים
- `requirements.txt` – תלויות
- תיקיות `voices/` ו־`outputs/` – הקלטות ופלטים

---

## ⚙️ איך מריצים מקומית?

1. התקן ספריות:
```bash
pip install -r requirements.txt
```

2. צור קובץ `.env` עם הטוקן:
```
TELEGRAM_TOKEN=הטוקן_שלך_מ־BotFather
```

3. הרץ את הבוט:
```bash
python bot.py
```

---

## ☁️ איך מעלים ל־Render?

1. כנס ל־https://render.com
2. לחץ על **"New" → "Web Service"**
3. בחר את הריפו שלך (KolLi)
4. בהגדרות:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
5. בלשונית **Environment** תוסיף משתנה:
   - KEY: `TELEGRAM_TOKEN`
   - VALUE: (הטוקן שלך)

6. לחץ Deploy ותן לו לעבוד!

---

## 📢 ואז מה?

- תיכנס לבוט שלך בטלגרם
- תשלח לו הקלטה (voice)
- תשלח טקסט
- תקבל הקראה (בשלב הבא נוסיף את הקול המותאם)

---

👑 בהצלחה!
