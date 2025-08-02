const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/', (req, res) => {
  res.json({ message: "Belirobux API aktif" });
});

app.get('/harga', (req, res) => {
  const jumlah = parseInt(req.query.jumlah);
  if (isNaN(jumlah) || jumlah <= 0) {
    return res.status(400).json({ error: "Jumlah tidak valid" });
  }

  // Hitung harga: 1 Robux = 140, biaya admin 3000
  const hargaRobux = jumlah * 140;
  const biayaAdmin = 3000;
  const total = hargaRobux + biayaAdmin;

  // Roblox ambil 30%, jadi harus buat gamepass senilai:
  const gamepass = Math.ceil(total / 0.7);

  res.json({
    jumlah,
    harga: total,
    biaya_admin: biayaAdmin,
    harus_buat_gamepass: gamepass
  });
});

const port = process.env.PORT || 10000;
app.listen(port, () => {
  console.log(`Server jalan di port ${port}`);
});
