from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Contoh data foto + pesan
    photos = [
        {
            "img": "img/foto1.jpg",
            "message": "Selamat ulang tahun, Mylove ❤️. Hari ini adalah Honey pe hari spesial. Setiap hari kita bersyukur karena boleh bakudapa deng Honey. Semoga kedepannya, setiap mimpi yang Honey ingin capai bisa tercapai, semoga Honey selalu dipenuhi dengan semangat untuk terus melangkah meski banyak rintangan."
        },
        {
            "img": "img/foto2.jpg",
            "message": "Kita tau belakangan ini Honey pasti merasa banyak beban. Mulai dari mo cari pekerjaan, menghadapi situasi keluarga yang beking saki hati, berjuang di tengah kondisi ekonomi yang sulit. Tapi kita suka Honey tau bahwa: Honey nda pernah sendiri. Ada Kita di sini for Honey, mo dengar Honey pe cerita, mo dukung setiap Honey pe usaha, deng mo genggam Honey pe tangan saat Honey merasa rapuh."
        },
        {
            "video": "vidio/vidio1.mp4",
            "message": "Honey, kita percaya dengan Honey pe kemampuan. Honey ada potensi besar yang mungkin kadang Honey sendiri lupa. Jangan pernah ragu deng Honey pe diri sendiri. Dunia ini luas, kesempatan banyak, dan kita yakin Tuhan sedang menyiapkan jalan terbaik for Honey. Semoga Honey pe doa-doa segera dijawab."
        },
        {
            "img": "img/foto3.jpg",
            "message": "Tentang pekerjaan, jangan pernah kehilangan harapan neh honey. Kita yakin akan ada kesempatan yang besar for honey. Jangan tako gagal, karena setiap kegagalan adalah batu loncatan menuju sesuatu yang lebih baik. Honey hanya butuh sedikit waktu, dan kita percaya momen itu akan segera datang."
        },
        {
            "img": "img/foto4.jpg",
            "message": "Kita, sayang pa Honey apapun Honey pe kondisi, bagaimanapun itu. karena kita sayang pa honey tanpa syarat. Maaf kalau kita banyak kurang, nda sama dengan Honey pe mantan mantan sebelumnya yang lebih baik dari kita."
        },
        {
            "video": "vidio/vidio2.mp4",
            "message": "Setiap hari kita belajar banyak : tentang sabar, tentang bertahan, dan tentang berjuang. karena cuman Honey yang ingin kita ajak banyak hal bersama-sama. cuman Honey yang kita mau nda ada yang lain."
        },
        {
            "video": "vidio/vidio3.mp4",
            "message": "Kita mau torang 2 basama-sama trus, melangkah bersama-sama. Susah senang tong dua hadapi sama-sama. Kita tau perjalanan kedepan pasti nda akan pernah mudah, tapi kita yaking torang dua boleh mo lalui selama torang dua saling menopang. Kita mau selalu ada di sisi pa Honey, sampai kapanpun itu."
        },
        {
            "img": "img/foto5.jpg",
            "message": "Pa Honey pe ulang tahun ini, kita berdoa semoga Honey selalu sehat, dijauhkan dari rasa putus asa, dan selalu diberikan kekuatan hati. Semoga setiap Honey pe langkahmu dipenuhi berkat, setiap Honey pe keputusan dilancarkan, dan setiap Honey pe mimpi semakin dekat menjadi nyata."
        },
        {
            "img": "img/foto6.jpg",
            "message": "Ingat, Mylove… Honey nda perlu merubah apapun untuk jadi berharga. Honey so berharga apa adanya. Kita mencintai semua hal tetang Honey: Honey pe senyum, Honey pe cerita, bahkan waktu Honey manangis. Kita ingin jadi orang yang selalu berdiri disamping pa Honey apapun yang terjadi."
        },
        {
            "video": "vidio/vidio4.mp4",
            "message": "Semoga tahun ini jadi awal yang indah for Honey. Semoga Honey menemukan kedamaian, kebahagiaan, dan keberanian untuk terus mengejar mimpi. Kita akan selalu mendukung Honey, dari hal-hal kecil sampai yang besar sekalipun."
        },
        {
            "img": "img/foto7.jpg",
            "message": "Dan terakhir, terima kasih sudah menjadi bagian dari kita pe hidop. Honey adalah hadiah terindah yang pernah kita dapa. Kita bangga pa Honey, Kita bersyukur memiliki pa Honey, dan kita mencintai Honey lebih dari yang bisa Kita ungkapkan dengan kata-kata. ❤️"
        }
    ]
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)
