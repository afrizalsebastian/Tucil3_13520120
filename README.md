# Tucil3-STIMA

## 15-Puzzle Solver
> Menggunakan Branch and Bound Method

## Deskripsi Singkat Program
Directory Project memiliki 4 Folder, yaitu bin, docs, src, dan test.<br>
1. Folder bin menyimpan run.bat
2. Folder bin menyimpan laporan
3. Folder src menyimpan source code
4. Folder test menyimpan test case

**Source Code**
<br>

Program Memiliki 3 file utama yaitu Puzzle.py, PriorityQueue.py, dan Main.py<br>
Pada Puzzle.py disimpan kelas Puzzle yang memilii atribut puzzle, depth, cost, lastMove, dan TotalMove. lastMove digunakan untuk melihat gerakan yang dilakukan sebelum mencapai state sekarang dan TotalMove digunakan untuk menampung semua gerakan yang telah dilakukan hingga mencapai state sekarang.
<br>
Pada PriorityQueue.py terdapat kelas PriorityQueue dengan atribut buffer dan func. Func digunakan untuk melakukan pengurutan saat enqueue dari yang terkecil.
<br>
Pada Main.py program utama berada. Alur program adalah menerima terlebih dahulu puzzle dari user baik dari konsole atau file. Puzzle tersebut akan dilakukan pengecekan dengan Kurang(i) + X. Jika Puzzle dapat diselesaikan Kelas PriorityQueue diinisialisasi dan Kelas Puzzle diinisialisai dengan Puzzle masukan user. Puzzle dienqueue ke priorityqueue. Akan dilakukan Loop hingga PriorityQueue Kosong atau sampai ke Goal State. Jika Sampai ke Goal State makan Puzzle yang memiliki Goal State akan diambil TotalMove dan TotalMove Tersebut akan digunakan oleh initialPuzzle untuk melakukan pencetakan di layar.
## Requirement
1. Mempunyai Python 3

## Menjalankan Project

Pergi ke directory src pada Project ini di Command Line
```
 ..\Tucil3-STIMA\src>
```
Ketik pada Command Line :
```bash
py Main.py
```
atau <br>
Run **run.bat** pada bin Folder<br>
### Input
**Ubah Tile kosong pada Puzzle menjadi '-'**<br><br>
Jika Program dijalankan menggunakan input dari konsole <br>
**EXAMPLE** <br>
1 2 3 4 <br>
5 6 7 8 <br>
9 10 11 12 <br>
13 14 15 - <br>
Setiap baris diakhiri dengan enter<br>

Jika Program dijalankan menggunakan File <br>
**Simpan File pada test Folder**<br>
Struktur pada File sama dengan yang diatas

## Conctact
[Afrizal Sebastian <br> 13520120](https://github.com/afrizalsebastian)
