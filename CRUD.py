import cx_Oracle
import os
import datetime
cx_Oracle.init_oracle_client(lib_dir=r"C:\\Users\\User\\Desktop\\Uczelnia\\Semestr IV\\Bazy danych\\CWP\\3\\4\\instantclient_19_11")

dsn = cx_Oracle.makedsn("127.0.0.1", 1521, service_name="XE")
baza = cx_Oracle.connect(user="uczelnia", password='Kacper', dsn=dsn, encoding="UTF-8")

kursor = baza.cursor()
#zmienna=True

while True:
  os.system("cls")
  print("Na jakiej tabeli chcesz operowac?")
  print("1.Studenci")
  print("2.Pracownicy")
  print("3.Przedmioty")
  print("4.Grupy zajeciowe")
  print("5.Zajecia")
  print("6.Oceny")
  print("7.Wyjscie")
  wybor1=int(input())
  if wybor1==1:
      while True:
          os.system("cls")
          print("Co chcesz zrobic?")
          print("1.Dodanie nowego rekordu")
          print("2.Usuniecie rekordu")
          print("3.Modyfikacja rekordu")
          print("4.Wyswietlenie rekordow")
          print("5.Wyswietl oceny studentow[CTE]")
          print("6.Wyjscie do menu glownego")
          wybor=int(input())
          if wybor==1:
            os.system("cls")
            print("Dodanie nowego rekordu do tablicy studenci")
            insert = "INSERT INTO studenci (NR_albumu, imie,nazwisko,GR_zajeciowa) VALUES (:i, :im, :na,:gr)"
            print("Podaj dane nowego rekordu")
            nr=input("Numer albumu: ")
            imie=input("imie: ")
            nazwisko=input("nazwisko: ")
            gr=input("Grupa zajeciowa: ")
            val = [nr, imie, nazwisko, gr]
            kursor.execute(insert, val)
            baza.commit()
            print(kursor.rowcount, " rekordow zostalo dodanych!")
            input()
          elif wybor==2:
            os.system("cls")
            print("Usuniecie rekordu")
            print("Podaj numer albumu studenta, ktorego chcesz usunac:")
            nr=input()
            delete = "DELETE FROM studenci WHERE nr_albumu = :i"
            kursor.execute(delete, [nr])
            baza.commit()
            print(kursor.rowcount, " rekordow usunieto!")
            input()
          elif wybor==3:
            os.system("cls")
            print("Zmiana grupy zajeciowej studenta")
            print("Podaj numer albumu studenta, ktorego grupe zajeciowa chcesz zmienic: ")
            nr=input()
            print("Podaj nowa grupe zajeciowa")
            nowa_gr=input()
            update = "UPDATE studenci SET gr_zajeciowa = :nowe WHERE  nr_albumu= :n"
            kursor.execute(update,[nowa_gr,nr])
            baza.commit()
            print(kursor.rowcount, " rekordow zostalo zmodyfikowanych!")
            input()
          elif wybor==4:
            os.system("cls")
            print("Rekordy z tablicy studenci[numer_albumu_studenta, imie, nazwisko]")
            read = "SELECT nr_albumu, imie, nazwisko FROM studenci order by nazwisko"
            kursor.execute(read)
            koniec = kursor.fetchall()
            for a in koniec:
              print(a)
            input()
          elif wybor==5:
            os.system("cls")
            print("Nazwiska studentow i ich ocen:")
            read = '''with cte1 as (select nazwisko, nr_albumu from studenci), cte2 as (select ocena, nr_albumu_studenta, id_przedmiotu from oceny),
                    cte3 as (select id_przedmiotu, nazwa_przedmiotu from przedmioty)
                    select nazwisko, ocena, nazwa_przedmiotu from 
                    cte1 inner join cte2 on cte1.nr_albumu=cte2.nr_albumu_studenta
                    inner join cte3 on cte3.id_przedmiotu=cte2.id_przedmiotu
                    order by nazwisko'''
            kursor.execute(read)
            koniec = kursor.fetchall()
            for a in koniec:
              print(a)
            input()
          elif wybor==6:
            break
          else:
            os.system("cls")
            print("Zly wybor!")
            input()#czas przestoju dopoki uzytkownik wcisnie enter
  elif wybor1==2:
      while True:
          os.system("cls")
          print("Co chcesz zrobic?")
          print("1.Dodanie nowego rekordu")
          print("2.Usuniecie rekordu")
          print("3.Wyswietlenie rekordow")
          print("4.Wyjscie do menu glownego")
          wybor=int(input())
          if wybor==1:
            os.system("cls")
            print("Dodanie nowego rekordu do tablicy pracownicy")
            insert = "INSERT INTO pracownicy (ID_pracownika, imie,nazwisko) VALUES (:i, :im, :n)"
            print("Podaj dane nowego rekordu")
            id=input("ID: ")
            imie=input("imie: ")
            nazwisko=input("nazwisko: ")
            val = [id, imie,nazwisko]
            kursor.execute(insert, val)
            baza.commit()
            print(kursor.rowcount, " rekordow zostalo dodanych!")
            input()
          elif wybor==2: 
            os.system("cls")
            print("Usuniecie rekordu")
            print("Podaj id pracownika, ktorego chcesz usunac:")
            id=input()
            delete = "DELETE FROM pracownicy WHERE id_pracownika = :i"
            kursor.execute(delete,[id])
            baza.commit()
            print(kursor.rowcount, " rekordow usunieto!")
            input()
          elif wybor==3:
            os.system("cls")
            print("Rekordy z tablicy pracownicy")
            read = "SELECT * FROM pracownicy order by nazwisko"
            kursor.execute(read)
            koniec = kursor.fetchall()
            for a in koniec:
              print(a)
            input()
          elif wybor==4:
            os.system("cls")
            break;
          else:
            os.system("cls")
            print("Zly wybor!")
            input()#czas przestoju dopoki uzytkownik wcisnie enter
  elif wybor1==3:
      while True:
          os.system("cls")
          print("Co chcesz zrobic?")
          print("1.Dodanie nowego rekordu")
          print("2.Usuniecie rekordu")
          print("3.Wyswietlenie rekordow")
          print("4.Wyjscie do menu glownego")
          wybor=int(input())
          if wybor==1:
            os.system("cls")
            print("Dodanie nowego rekordu do tablicy przedmioty")
            insert = "INSERT INTO przedmioty (ID_przedmiotu, Nazwa_przedmiotu) VALUES (:i, :n)"
            print("Podaj dane nowego rekordu")
            id=input("ID: ")
            nazwa=input("Nazwa przedmiotu: ")
            val = [id, nazwa]
            kursor.execute(insert, val)
            baza.commit()
            print(kursor.rowcount, " rekordow zostalo dodanych!")
            input()
          elif wybor==2:
            os.system("cls")
            print("Usuniecie rekordu")
            print("Podaj id przedmiotu, ktorego chcesz usunac:")
            id=input()
            delete = "DELETE FROM przedmioty WHERE id_przedmiotu = :i"
            kursor.execute(delete,[id])
            baza.commit()
            print(kursor.rowcount, " rekordow usunieto!")
            input()
          elif wybor==3:
            os.system("cls")
            print("Rekordy z tablicy przedmioty")
            read = "SELECT * FROM przedmioty order by nazwa_przedmiotu"
            kursor.execute(read)
            koniec = kursor.fetchall()
            for a in koniec:
              print(a)
            input()
          elif wybor==4:
            os.system("cls")
            break
          else:
            os.system("cls")
            print("Zly wybor!")
            input()#czas przestoju dopoki uzytkownik wcisnie enter
  elif wybor1==4:
      while True:
          os.system("cls")
          print("Co chcesz zrobic?")
          print("1.Dodanie nowego rekordu")
          print("2.Usuniecie rekordu")
          print("3.Wyswietlenie rekordow")
          print("4.Wyjscie do menu glownego")
          wybor=int(input())
          if wybor==1:
            os.system("cls")
            print("Dodanie nowego rekordu do tablicy grupyzajeciowe")
            insert = "INSERT INTO grupyzajeciowe (numer_grupy) VALUES (:n)"
            print("Podaj dane nowego rekordu")
            nr=input("Numer grupy: ")
            val = [nr]
            kursor.execute(insert, val)
            baza.commit()
            print(kursor.rowcount, " rekordow zostalo dodanych!")
            input()
          elif wybor==2:
            os.system("cls")
            print("Usuniecie rekordu")
            print("Podaj numer grupy, ktora chcesz usunac:")
            nr=input()
            delete = "DELETE FROM grupyzajeciowe WHERE numer_grupy = :n"
            kursor.execute(delete,[nr])
            baza.commit()
            print(kursor.rowcount, " rekordow usunieto!")
            input()
          elif wybor==3:
            os.system("cls")
            print("Rekordy z tablicy grupyzajeciowe")
            read = "SELECT * FROM grupyzajeciowe"
            kursor.execute(read)
            koniec = kursor.fetchall()
            for a in koniec:
              print(a[0])
            input()
          elif wybor==4:
            os.system("cls")
            break
          else:
            os.system("cls")
            print("Zly wybor!")
            input()#czas przestoju dopoki uzytkownik wcisnie enter
  elif wybor1==5:
        while True:
            os.system("cls")
            print("Co chcesz zrobic?")
            print("1.Dodanie nowego rekordu")
            print("2.Usuniecie rekordu")
            print("3.Modyfikacja rekord")
            print("4.Wyswietlenie rekordow")
            print("5.Wyjscie do menu glownego")
            wybor=int(input())
            if wybor==1:
                os.system("cls")
                print("Dodanie nowego rekordu do tablicy zajecia")
                insert = "insert into ZAJECIA (Przedmiot, prowadzacy,id_zajec,data,grupa_zajeciowa) values(:prze,:pro,:id, TO_DATE(:de, 'MM/DD/YYYY HH24:MI:SS'), :gr)"
                print("Podaj dane nowego rekordu")
                przedmiot=input("Przedmiot: ")
                prowadzacy=input("prowadzacy: ")
                id=input("Id zajec: ")
                dat = input("Data MM/DD/YYY HH24:MI:SS: ")
                Gr=input("Grupa zajeciowa: ")
                val = [przedmiot,prowadzacy,id,dat,Gr]
                kursor.execute(insert, val)
                baza.commit()
                print(kursor.rowcount, " rekordow zostalo dodanych!")
                input()
            elif wybor==2:
                os.system("cls")
                print("Usuniecie rekordu")
                print("Podaj id zajec, ktore chcesz usunac:")
                id=input()
                delete = "DELETE FROM zajecia WHERE id_zajec = :id"
                kursor.execute(delete,[id])
                baza.commit()
                print(kursor.rowcount, " rekordow usunieto!")
                input()
            elif wybor==3:
                os.system("cls")
                print("Zmiana grupy, ktora ma zajecia")
                print("Podaj id zajec dla ktorego chcesz zmienic grupe: ")
                id=input()
                print("Podaj akutalna grupe zajeciowa: ") 
                nowa=input()
                update = "UPDATE zajecia SET grupa_zajeciowa = :n WHERE  id_zajec= :id"
                kursor.execute(update,[nowa,id])
                baza.commit()
                print(kursor.rowcount, " rekordow zostalo zmodyfikowanych!")
                input()
            elif wybor==4:
                os.system("cls")
                print("Rekordy z tablicy zajecia")
                read = "SELECT * FROM zajecia order by data"
                kursor.execute(read)
                koniec = kursor.fetchall()
                for a in koniec:
                  print(a)
                input()
            elif wybor==5:
                os.system("cls")
                break
            else:
                os.system("cls")
                print("Zly wybor!")
                input()#czas przestoju dopoki uzytkownik wcisnie enter
  elif wybor1==6:
            while True:
              os.system("cls")
              print("Co chcesz zrobic?")
              print("1.Dodanie nowego rekordu")
              print("2.Usuniecie rekordu")
              print("3.Modyfikacja rekordu")
              print("4.Wyswietlenie rekordow")
              print("5.Wyjscie do menu glownego")
              wybor=int(input())
              if wybor==1:
                os.system("cls")
                print("Dodanie nowego rekordu do tablicy oceny")
                insert = "INSERT INTO oceny (ocena, nr_albumu_studenta,id_prowadzacego,id_oceny,id_przedmiotu) VALUES (:o, :n, :idpro,:ido,:idp)"
                print("Podaj dane nowego rekordu")
                ocena=input("Ocena: ")
                nr=input("Numer albumu studenta: ")
                id_p=input("Id prowadzacego: ")
                id_o=input("Id oceny: ") 
                id_pr=input("Id przedmiotu: ")
                val = [ocena,nr,id_p,id_o,id_pr]
                kursor.execute(insert, val)
                baza.commit()
                print(kursor.rowcount, " rekordow zostalo dodanych!")
                input()
              elif wybor==2:
                os.system("cls")
                print("Usuniecie rekordu")
                print("Podaj id oceny, ktora chcesz usunac:")
                id=input()
                delete = "DELETE FROM oceny WHERE id_oceny = :id"
                kursor.execute(delete,[id])
                baza.commit()
                print(kursor.rowcount, " rekordow usunieto!")
                input()
              elif wybor==3:
                os.system("cls")
                print("Zmiana oceny")
                print("Podaj id oceny, ktora chcesz zmienic: ")
                id=input()
                print("Nowa ocena: ") 
                nowa=input()
                update = "UPDATE oceny SET ocena = :n WHERE  id_oceny= :id"
                kursor.execute(update,[nowa,id])
                baza.commit()
                print(kursor.rowcount, " rekordow zostalo zmodyfikowanych!")
                input()
              elif wybor==4:
                os.system("cls")
                print("Rekordy z tablicy oceny[id_oceny,id_oceny, nr_albumu_studenta, id_prowadzacego, id_przedmiotu] ")
                read = "SELECT id_oceny, nr_albumu_studenta, id_prowadzacego, id_przedmiotu, ocena FROM oceny order by ocena"
                kursor.execute(read)
                koniec = kursor.fetchall()
                for a in koniec:
                  print(a)
                input()
              elif wybor==5:
                os.system("cls")
                break
              else:
                os.system("cls")
                print("Zly wybor!")
                input()#czas przestoju dopoki uzytkownik wcisnie enter  
  elif wybor1==7:
        break
  else:
        os.system("cls")
        print("Zly wybor!")
        input()#czas przestoju dopoki uzytkownik wcisnie enter 
