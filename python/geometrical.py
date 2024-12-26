# Python Trial for Geometrical Surface and Around Formulas
import math

def rectangular() :
    print("Menghitung Luas dan Keliling Segiempat")

    # Data untuk dimasukkan pada Rumus Segiempat
    length = float(input("Enter Rectangular Length = "))
    width = float(input("Enter Rectangular Width = "))

    # Rumus Luas dan Keliling Segiempat
    rect_surface_area = length*width
    rect_around_area = 2*(length+width)

    choose = input("\nHitung Luas atau Keliling? >> ").title()
    while True :
        if choose == "Luas" :
            print(f"\nLuas Segiempat = {rect_surface_area}")
            break
        elif choose == "Keliling" :
            print(f"\nKeliling Segiempat = {rect_around_area}")
            break
        else :
            print("\nPilihan hanya Luas atau Keliling!")
            break

    print("\n")


def triangular() :
    print("Menghitung Luas dan Keliling Segitiga")

    # Triangular Modelling for being counted
    triangle_model = ["Right Triangle", "Isosceles Triangle", "Equilateral Triangle", "Scalene Triangle"]

    for idx, model in enumerate(triangle_model, 1) :
        # {idx} = i / index, {model} = data dalam triangle_model, enumerate = perngulangan untuk output list >> run to understand this
        print(f"{idx}. {model}")

    print()

    # Data untuk dimasukkan dalam segitiga
    base_tri = float(input("Enter Triangular Base = "))
    height_tri = float(input("Enter Triangular Height = "))

    # Segitiga mana yang akan dieksekusi >>
    triangle_choose = int(input("\nPilih nomor segitiga yang ingin dihitung = "))
    print()

    # Rumus Luas Segitiga
    tri_surface_area = (base_tri*height_tri)/2
    # RUmus Keliling Segitiga Siku-Siku
    sisi_miring_siku = math.sqrt(base_tri**2 + height_tri**2)
    around_area_siku = str(base_tri + height_tri + sisi_miring_siku)
    # Rumus Keliling Segitiga Sama Sisi
    sisi_sisi = (2 * height_tri) / math.sqrt(3)
    around_area_sisi = str(3 * sisi_sisi)
    # Rumus Keliling Segitiga Sama kaki
    sisi_miring_kaki = math.sqrt((base_tri/2)**2 + height_tri**2)
    around_area_kaki = str(base_tri + height_tri + sisi_miring_kaki)

    match triangle_choose :

        # Segitiga Siku-Siku
        case 1 :
            # print(triangle_model[0])
            print(triangle_model[triangle_choose - 1])
            # print(triangle_choose - 1, triangle_model[])
            choose = input("Hitung Luas atau Keliling? >> ").title()
            if choose == "Luas" :
                # Hitung Luas dulu
                print(f"\nLuas Segitiga Siku-Siku = {tri_surface_area}") # mengubah tipe data float >> int = {int(tri_surface)area)}
            elif choose == "Keliling" :
                # Hitung Keliling nya
                print(f"\nKeliling Segitiga Siku-Siku = {around_area_siku}") # berlaku pada print(f"output {var}")
            else :
                print("\nPilihan hanya Luas atau Keliling!\n")

        # Segitiga Sama Sisi
        case 2 :
            print(triangle_model[triangle_choose - 1])
            choose = input("Hitung Luas atau Keliling? >> ").title()
            if choose == "Luas" :
                # Hitung Luas dulu
                print(f"\nLuas Segitiga Sama Sisi = {tri_surface_area}")
            elif choose == "Keliling" :
                # Hitung Keliling nya
                print(f"\nKeliling Segitiga Sama Sisi = {around_area_sisi}")
            else :
                print("\nPilihan hanya Luas atau Keliling!\n")

        # Segitiga Sama Kaki
        case 3 :
            print(triangle_model[triangle_choose - 1])
            choose = input("Hitung Luas atau Keliling? >> ").title()
            if choose == "Luas"  :
                # Hitung Luas nya
                print(f"\nLuas Segitiga Sama Kaki = {tri_surface_area}")
            elif choose == "Keliling" :
                # Hitung Keliling
                print(f"\nKeliling Segitiga Sama Kaki = {around_area_kaki}")
            else :
                print("\nPilihan hanya Luas atau Keliling!\n")

        # Segitiga Sembarang
        case 4 :
            print(triangle_model[triangle_choose - 1])
            choose = input("Hitung Luas atau Keliling? >> ").title()
            if choose == "Luas"  :
                # Hitung Luas nya
                print(f"\nLuas Segitiga Sembarang = {tri_surface_area}")
            elif choose == "Keliling" :
                # Hitung Keliling >> Segitiga Sembarang harus diketahui sisinya, karena sisi segitiga sembarang ya sembarangan :V
                print("\nKeliling Segitiga Sembarang hanya dapat dicari jika diketahui panjang tiap sisinya.")
                a_sem = int(input("Masukkan panjang sisi a = "))
                b_sem = int(input("Masukkan panjang sisi b = "))
                c_sem = int(input("Masukkan panjang sisi c = "))

                around_area_sembarang = a_sem + b_sem + c_sem
                print(f"\nKeliling Segitiga Sembarang = {around_area_sembarang}")
            else :
                print("\nPilihan hanya Luas atau Keliling!\n")

        case _ :
            print("Pilihan hanya yang terdapat pada List Segitiga berikut !!")

            # # Add New Triangular Type into Triangular Modeelling
            # add_triangle = input("Ataukah Anda ingin menambahkan jenis segitiga lagi? (y/n) >> ").lower().strip()
            # if add_triangle == "y" :
            #     new_triangle = input("Masukkan nama Segitiga Anda = ").strip()
            #     if new_triangle :
            #         triangle_model.append(new_triangle)
            #         print(f"{new_triangle} has been added to Triangular Types")
            #     else :
            #         print("Nama segitiga tidak boleh kosong!")
            # else :
            #     print("Anda tidak jadi menambahkan segitiga V:<")

    print("\n")

    # Previous Feature :

    # # Segitiga Siku-Siku
    # if triangle_choose == 1 :
    #     print(triangle_model[0])
    #     # print(triangle_model[triangle_choose - 1])
    #     choose = input("Hitung Luas atau Keliling? >> ").title()
    #     if choose == "Luas" :
    #         # Hitung Luas dulu
    #         print(f"\nLuas Segitiga Siku-Siku = {tri_surface_area}") # mengubah tipe data float >> int = {int(tri_surface)area)}
    #     elif choose == "Keliling" :
    #         # Hitung Keliling nya
    #         print(f"\nKeliling Segitiga Siku-Siku = {around_area_siku}") # berlaku pada print(f"output {var}")
    #     else :
    #         print("\nPilihan hanya Luas atau Keliling!\n")
    # # Segitiga Sama Sisi
    # elif triangle_choose == 2 :
    #     print(triangle_model[1])
    #     # print(triangle_model[triangle_choose - 1])
    #     choose = input("Hitung Luas atau Keliling? >> ").title()
    #     if choose == "Luas" :
    #         # Hitung Luas dulu
    #         print(f"\nLuas Segitiga Sama Sisi = {tri_surface_area}")
    #     elif choose == "Keliling" :
    #         # Hitung Keliling nya
    #         print(f"\nKeliling Segitiga Sama Sisi = {around_area_sisi}")
    #     else :
    #         print("\nPilihan hanya Luas atau Keliling!\n")
    # # Segitiga Sama Kaki
    # elif triangle_choose == 3 :
    #     print(triangle_model[2])
    #     # print(triangle_model[triangle_choose - 1])
    #     choose = input("Hitung Luas atau Keliling? >> ").title()
    #     if choose == "Luas"  :
    #         # Hitung Luas nya
    #         print(f"\nLuas Segitiga Sama Kaki = {tri_surface_area}")
    #     elif choose == "Keliling" :
    #         # Hitung Keliling
    #         print(f"\nKeliling Segitiga Sama Kaki = {around_area_kaki}")
    #     else :
    #         print("\nPilihan hanya Luas atau Keliling!\n")
    # # Segitiga Sembarang
    # elif triangle_choose == 4 :
    #     print(triangle_model[3])
    #     # print(triangle_model[triangle_choose - 1])
    #     choose = input("Hitung Luas atau Keliling? >> ").title()
    #     if choose == "Luas"  :
    #         # Hitung Luas nya
    #         print(f"\nLuas Segitiga Sembarang = {tri_surface_area}")
    #     elif choose == "Keliling" :
    #         # Hitung Keliling >> Segitiga Sembarang harus diketahui sisinya, karena sisi segitiga sembarang ya sembarangan :V
    #         print("\nKeliling Segitiga Sembarang hanya dapat dicari jika diketahui panjang tiap sisinya.")
    #         a_sem = int(input("Masukkan panjang sisi a = "))
    #         b_sem = int(input("Masukkan panjang sisi b = "))
    #         c_sem = int(input("Masukkan panjang sisi c = "))
    #         around_area_sembarang = a_sem + b_sem + c_sem
    #         print(f"\nKeliling Segitiga Sembarang = {around_area_sembarang}")
    #     else :
    #         print("\nPilihan hanya Luas atau Keliling!\n")
    # else :
    #     print("Pilihan hanya yang terdapat pada List Segitiga berikut !!")


def kite() :
    print("Menghitung Luas dan Keliling Layang-Layang")

    # Data untuk dimasukkan pada Rumus Layang-Layang
    diag_1 = float(input("Masukkan panjang diagonal 1 = "))
    diag_2 = float(input("Masukkan panjang diagonal 2 = "))
    side_kite = float(input("Masukkan panjang sisi layang-layang = "))

    # Rumus Luas dan Keliling Layang-Layang
    kite_surface_area = 0.5 * diag_1 * diag_2
    kite_around_area = 4 * side_kite

    choose = input("\nHitung Luas atau Keliling? >> ").title()
    if choose == "Luas" :
        print(f"\nLuas Layang-Layang = {kite_surface_area}")
    elif choose == "Keliling" :
        print(f"\nKeliling Layang-Layang = {kite_around_area}")
    else :
        print("\nPilihan hanya Luas atau Keliling!")

    print("\n")


def trapezoid() :
    print("Menghitung Luas dan Keliling Trapesium")

    # Data untuk dimasukkan pada Rumus Trapesium
    a_trap = float(input("Masukkan nilai a = "))
    b_trap = float(input("Masukkan nilai b = "))
    height_trap = float(input("Masukkan tinggi trapesium = "))

    # Rumus Luas Trapesium
    trapezoid_surface_area = ((a+b)*t)/2

    choose = input("\nHitung Luas atau Keliling? >> ").title()
    while True :
        if choose == "Luas" :
            print(f"\nLuas Trapesium = {rect_surface_area}")
            break
        elif choose == "Keliling" :
            print("\nTrapesium membutuhkan data panjang dari sisi miring untuk menghitung kelilingnya")
            c_trap = int(input("Masukkan nilai c = "))
            d_trap = int(input("Masukkan nilai d = "))

            trapezoid_around_area = a_trap + b_trap + c_trap + d_trap
            print(f"\nKeliling Trapesium = {trapezoid_around_area}")
            break
        else :
            print("\nPilihan hanya Luas atau Keliling!")
            break

    print("\n")


# def exit_program() :



    # print("\n")


# Tampilan Program pada Terminal
def menu_app() :
    print()
    print("----------SHAPE MENU----------")
    print("[1] Rectangular")
    print("[2] Triangular")
    print("[3] Kite Shape")
    print("[4] Trapezoid")
    print("[5] Exit Programm")
    print()

    menu = input("--- CHOOSE SHAPE >> ").strip()
    print()

    if menu == "1" :
        rectangular()
    elif menu == "2" :
        triangular()
    elif menu == "3" :
        kite()
    elif menu == "4" :
        trapezoid()
    elif menu == "5" :
        exit_program()
    else :
        print("Please choose only those progamm !!")


# Greeting Application
print("Program Perhitungan Rumus Luas dan Keliling Bangun Datar")
print()


# Run Program and Loop
while True :
    jawab = str(input("Apakah Anda bersedia untuk mencoba program ini? (y/n/break) >> ")).lower().strip()

    if jawab == "y" :
        while True :
            menu_app()
            ulang = str(input("Jalankan ulang program ini? ('y' for repeating, enter any key to finish this program) >> ")).lower().strip()
            print()
            if ulang != "y" :
                print("Terima kasih sudah berpartisipasi dalam program ini :D")
                break
        break
    elif jawab == "n" :
        print("Apakah kamu ngga mau nyoba program ini? Siapa tau kamu butuh lo :D\n")
    else :
        print("OK, Aku tunggu kamu di project ku selanjutnya yaa... :)")
        break
