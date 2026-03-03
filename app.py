import streamlit as st
import yfinance as yf

# إعدادات واجهة التطبيق لعام 2026
st.set_page_config(page_title="AlgoTrader 2026", layout="centered")
st.title("📱 مكتب التداول الآلي الخاص بك")

# خانة اختيار السهم أو العملة
ticker = st.text_input("أدخل الرمز (مثلاً BTC-USD أو NVDA)", "BTC-USD")

if st.button("تحليل الإشارة الآن"):
    try:
        # جلب البيانات الحقيقية من البورصة
        data = yf.download(ticker, period="1d", interval="15m", progress=False)
        price = data['Close'].iloc[-1]
        
        # عرض السعر الحالي
        st.metric("السعر الحالي اللحظي", f"${price:,.2f}")
        
        # رسم بياني تفاعلي
        st.line_chart(data['Close'])
        
        st.success("✅ الخوارزمية تعمل بنجاح وتراقب السوق")
    except Exception as e:
        st.error("⚠️ تأكد من رمز السهم بشكل صحيح")

st.caption("نظام تداول آلي خاص - نسخة 2026")
