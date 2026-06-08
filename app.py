import streamlit as st

st.set_page_config(
    page_title="matematika geometri",
    page_icon="🏆"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("baim.png")
        
    st.title("bangun datar")
    
    pilihan = st.selectbox(
        "pilihan bangun datar",
        ["persegi", "persegi panjang", "lingkaran"]
    )
    
    st.caption("dibuat dengan 🔥 oleh **Ibrahim Cesa Chandra**")

match pilihan:
    case "persegi":
        st.title("persegi")
        st.markdown("menghitung luas dan keliling `persegi`")
        
        sisi = st.number_input("masukkan sisi")
        
        if st.button("hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            
            st.snow()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("luas", value=f"{luas:.2f}F", border=True)
            with col2:
                st.metric("keliling", value=f"{keliling:.2f}F", border=True)
                
    case "persegi panjang":
        st.title("persegi panjang")
        st.markdown("menghitung luas dan keliling `persegi panjang`")
        
        panjang = st.number_input("masukkan panjang")
        lebar = st.number_input("masukkan lebar")
        
        if st.button("hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            
            st.balloons()
            
            st.success(f"luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            
    case "lingkaran":
        st.title("lingkaran")
        st.markdown("menghitung luas dan keliling `lingkaran`")
        
        jari_jari = st.number_input("masukkan jari jari")
        
        if st.button("hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            
            st.balloons()
            
            st.success(f"luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            
    case _:
        st.error("terjadi kesalahan")