![](_page_0_Picture_0.jpeg)

# OBJEKTORIENTIERTE SYSTEME INITIALISIERUNG VON OBJEKTEN IN C++

PROF. DR. JÖRG NITZSCHE HOCHSCHULE ESSLINGEN [JOERG.NITZSCHE@HS-ESSLINGEN.DE](mailto:Joerg.Nitzsche@hs-Esslingen.de)

![](_page_1_Picture_0.jpeg)

#### LERNZIEL

- Initialisierung von Objekten durch Konstruktoren vornehmen können
- Verschiedene Konstruktortypen unterscheiden und verwenden können
- Destruktoren korrekt einsetzen können

![](_page_2_Picture_0.jpeg)

## "Initialisierung" von Objekten

- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

![](_page_3_Picture_1.jpeg)

- Deklaration
	- Eine Variable wird eingeführt und der Typ der Variable bestimmt, z.B.:
		- int a; // wie in C
- Initialisierung
	- Einer Variable wird bei der Deklaration gleich ein Wert zugeordnet, z.B.:
		- int a = 8; // wie in C
		- int a {8};
		- int a {};
		- auto a = 8;
		- auto a {8};
- Zuweisung
	- Einer Variablen wird NACH der Deklaration ein Wert zugewiesen / der Wert einer Variablen wird geändert, z.B.:
		- a = 9; // wie in C

#### "INITIALISIERUNG" VON KLASSENELEMENTEN

![](_page_4_Picture_1.jpeg)

```
#include <iostream>
    class Fraction {
        int _numerator, _denominator;
    public:
        void init(int n, int d){
             _numerator = n;
             _denominator = d;
        }
        void print(){
             std::cout << "Bruch: " << _numerator << "/" << _denominator << std::endl;
        }
    };
    int main(){
        Fraction f;
        f.init(0,1);
        f.print();
        return 0;
    }
                                                                                  Ausgabe
                                                                                Bruch = 0/1
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
```
![](_page_5_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

#### INITIALISIERUNG VON OBJEKTEN

- Ein Objekt wird bei seiner Erzeugung normalerweise nicht initialisiert. Um eine automatische Initialisierung zu bewirken, stehen spezielle Methoden sogenannte **Konstruktoren** zur Verfügung.
- Konstruktoren sind Methoden ohne Rückgabetyp. Der Methodenname eines Konstruktors ist identisch mit dem Namen der Klasse.
- Konstruktoren können nicht explizit aufgerufen werden, sondern der Kompiler benutzt die Konstruktoren, wenn Objekte zu 'konstruieren' sind (Definition, new, ...).
- Der Kompiler stellt Konstruktoren zur Verfügung. Bei der Deklaration einer Klasse kann der Programmierer diese mit eigenen Konstruktoren redefinieren.

#### STANDARDKONSTRUKTOR DES KOMPILERS

- Der Standardkonstruktor hat keine Parameter.
- Der vom Kompiler zur Verfügung gestellte Standardkonstruktor initialisiert die Datenelemente mit zufälligen Werten (also quasi gar nicht).
- Er heißt auch Defaultkonstruktor, weil er in Fällen 'per default' benutzt wird, wenn es keine Möglichkeit gibt, den Aufruf eines anderen Konstruktors zu veranlassen.

#### VERWENDUNG EINES OBJEKTS "OHNE INITIALISIERUNG"

![](_page_8_Picture_1.jpeg)

Bruch = -20543360/32767

public:

}

int main() {

};

}

#include <iostream> using namespace std;

#include <iostream> class Fraction {

void print(){

Fraction f; f.print(); return 0;

int \_numerator, \_denominator;

### SELBSTDEFINIERTER STANDARDKONSTRUKTOR

![](_page_9_Picture_1.jpeg)

```
#include <iostream>
    using namespace std;
    class Fraction {
         int _numerator, _denominator;
    public:
         Fraction() {
             _numerator = 0;
             _denominator = 1;
         }
         void print(){
             cout << "Bruch: " << _numerator
                   << "/" << _denominator << endl;
         }
    };
    int main()
    {
         Fraction f;
         f.print();
         return 0;
    }
                                       Ausgabe
                                      Bruch = 0/1
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
```
 Auch ein selbstdefiniertre Standardkonstruktor hat keine Parameter. Der hier gezeigte Standardkonstruktor initialisiert die Attribute \_numerator und \_denominator mit den Werten 0 und 1

![](_page_10_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor

## Konstruktoren mit Parametern

- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

#### KONSTRUKTOREN MIT PARAMETERN

- Wie eine Methode können Konstruktoren **Parameter** haben, um die Objekte mit individuellen Werten zu initialisieren.
- Bei bestimmten Parameterprofilen haben die Konstruktoren mit Parametern eigene Namen:
	- **Kopierkonstruktor**
		- (1 Parameter vom Typ der eigenen Klasse)
	- **Konvertierkonstruktor**
		- (1 Parameter von einem anderen Typ)
- Bei den Konstruktoren mit Parametern gelten auch die Regeln für Defaultwerte und für das Overloading.

### ÜBERLADEN VON KONSTRUKTOREN

![](_page_12_Picture_1.jpeg)

```
#include <iostream>
    using namespace std;
    class Fraction {
         int _numerator, _denominator;
    public:
        Fraction() {
             _numerator = 0;
             _denominator = 1;
        }
        Fraction(int n) {
             _numerator = n;
             _denominator = 1;
        }
        Fraction(int n, int d) {
             _numerator = n;
             _denominator = d;
        }
                                                                     void print() {
                                                                         cout << "Bruch = " << _numerator
                                                                              << "/" << _denominator << endl;
                                                                     }
                                                                };
                                                                int main() {
                                                                     Fraction f_1, f_2(12), f_3(7, -24);
                                                                     f_1.print();
                                                                     f_2.print();
                                                                     f_3.print();
                                                                     return 0;
                                                                }
                                                                                       Ausgabe
                                                                                     Bruch = 0/1
                                                                                    Bruch = 12/1
                                                                                    Bruch = 7/-24
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
                                                            19
                                                            20
                                                            21
                                                            22
                                                            23
                                                            24
                                                            25
                                                            26
                                                            27
                                                            28
                                                            29
                                                            30
```
#### KONSTRUKTOR MIT DEFAULTWERTEN

![](_page_13_Picture_1.jpeg)

```
#include <iostream>
    using namespace std;
    class Fraction {
        int _numerator, _denominator;
    public:
        Fraction(int n = 0, int d = 1) {
             _numerator = n;
             _denominator = d;
        }
        void print() {
             cout << "Bruch = " << _numerator
                  << "/" << _denominator << endl;
        }
    };
                                                                int main()
                                                                {
                                                                    Fraction f_1, f_2(12), f_3(7, -24);
                                                                    f_1.print();
                                                                    f_2.print();
                                                                    f_3.print();
                                                                    return 0;
                                                                }
                                                                                      Ausgabe
                                                                                    Bruch = 0/1
                                                                                    Bruch = 12/1
                                                                                   Bruch = 7/-24
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
                                                           16
                                                           17
                                                           18
                                                           19
                                                           20
                                                           21
                                                           22
                                                           23
```
![](_page_14_Picture_0.jpeg)

![](_page_14_Picture_1.jpeg)

# FRAGEN?

![](_page_14_Picture_4.jpeg)

![](_page_15_Picture_1.jpeg)

![](_page_15_Picture_2.jpeg)

![](_page_15_Picture_3.jpeg)

![](_page_15_Picture_5.jpeg)

![](_page_16_Picture_0.jpeg)

int \_numerator, \_denominator;

\_numerator = 0; \_denominator = 1;

\_numerator = n; \_denominator = 1;

Fraction(int n, int d) { \_numerator = n; \_denominator = d;

#include <iostream> using namespace std; class Fraction {

Fraction() {

Fraction(int n) {

public:

}

}

}

}

![](_page_16_Picture_1.jpeg)

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
```
# Welche Aussagen stimmen:

- Der erste Konstruktor ist der Standardkonstruktor
- Der zweite Konstruktor ist ein parametrisierter Konstruktor
- Der dritte Konstruktor ist ein Konvertierkonstruktor

![](_page_17_Picture_0.jpeg)

int \_numerator, \_denominator;

\_numerator = 0; \_denominator = 1;

\_numerator = n;

![](_page_17_Picture_1.jpeg)

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
```
public:

}

```
_denominator = 1;
    }
    Fraction(int n, int d) {
        _numerator = n;
        _denominator = d;
    }
}
```
#include <iostream> using namespace std; class Fraction {

Fraction() {

Fraction(int n) {

- Welche Aussagen stimmen:
	- Der erste Konstruktor ist der Standardkonstruktor
	- Der zweite Konstruktor ist ein parametrisierter Konstruktor
	- Der dritte Konstruktor ist ein Konvertierkonstruktor

![](_page_18_Picture_0.jpeg)

<< "/" << \_denominator << endl;

```
#include <iostream>
    using namespace std;
    class Fraction {
         int _numerator, _denominator;
    public:
         Fraction(int n, int d) {
             _numerator = n;
             _denominator = d;
         }
         void print() {
             cout << "Bruch = " << _numerator
         }
    };
    int main()
    {
         Fraction f_1, f_2(7, -24);
         f_1.print();
         f_2.print();
         return 0;
    }
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
```
- Was ist das Ergebnis?
	- Bruch = 2456/98302 Bruch = 7/-24
	- error

![](_page_19_Picture_0.jpeg)

int \_numerator, \_denominator;

cout << "Bruch = " << \_numerator

<< "/" << \_denominator << endl;

Fraction(int n, int d) { \_numerator = n; \_denominator = d;

Fraction f\_1, f\_2(7, -24);

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```
© HS Esslingen Objektorientierte Systeme 1 20
```
f\_1.print(); f\_2.print(); return 0;

#include <iostream> using namespace std; class Fraction {

void print() {

public:

}

}

int main()

};

{

}

# Was ist das Ergebnis?

- Bruch = 2456/98302
	- Bruch = 7/-24
- error

### Compiler-Ausgabe

![](_page_20_Picture_0.jpeg)

### ERLÄUTERUNG ZU FRAGE 2

- Wird ein eigener Konstruktor definiert, so wird der Standardkonstruktor verdeckt.
- Soll er wieder verfügbar gemacht werden, so kann er
	- explizit implementiert werden, z.B.: Fraction(){}
	- Sichtbar gemacht werden, z.B: Fraction() = default

![](_page_21_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern

## Initialisierungsliste

- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

![](_page_22_Picture_1.jpeg)

- Beim Aufruf des Konstruktors wird zunächst, noch vor Betreten des Blocks, Speicherplatz für die Elemente (im Beispiel \_numerator und \_denominator) beschafft.
- Dann wird im zweiten Schritt der Programmcode innerhalb der geschweiften Klammern ausgeführt und die Parameter werden zugewiesen.

#### INITIALISIERUNG SCHRITTE – ERSTER SCHRITT

![](_page_23_Picture_1.jpeg)

![](_page_23_Figure_2.jpeg)

#### INITIALISIERUNG SCHRITTE – ZWEITER SCHRITT

![](_page_24_Picture_1.jpeg)

![](_page_24_Figure_2.jpeg)

![](_page_25_Picture_1.jpeg)

- Es gibt eine Möglichkeit, beide Vorgänge in *einem* Schritt zusammenzufassen, der deshalb besonders bei größeren oder vielen Objekten Laufzeitvorteile bringt.
- Der Weg führt über eine *Element-Initialisierungsliste* (englisch *member initializer list*), die noch vor dem Block angegeben und abgearbeitet wird

#### INITIALISIERUNG IN EINEM SCHRITT MIT INITIALISIERUNGSLISTE

![](_page_26_Picture_1.jpeg)

![](_page_26_Figure_2.jpeg)

© HS Esslingen Objektorientierte Systeme 1 27

### BLOCK UND INITIALISIERUNGSLISTE

![](_page_27_Picture_1.jpeg)

Beide Ansätze können auch gemischt werden

| 1<br>2                               | #include<br><iostream><br/>using<br/>namespace<br/>std;</iostream>                                    |
|--------------------------------------|-------------------------------------------------------------------------------------------------------|
| 3<br>4<br>5<br>6<br>7                | class<br>Fraction<br>{<br>int<br>_numerator,<br>_denominator;                                         |
| 8<br>9<br>10<br>11<br>12<br>13<br>14 | public:<br>Fraction(int<br>n,<br>int<br>d)<br>: _numerator{n}<br>{<br>_denominator<br>= n;<br>}<br>}; |

ANWENDUNGSFÄLLE FÜR DIE INITIALISIERUNGSLISTE

![](_page_28_Picture_1.jpeg)

- Die Verwendung der Initialisierungsliste ist nicht nur effizienter, sondern es gibt auch Anwendungsfälle für die man die Initialisierungsliste verwenden muss, z.B.:
	- Delegation
	- Aufruf anderer Konstruktoren (siehe Kapitel Vererbung)

![](_page_29_Picture_0.jpeg)

![](_page_29_Picture_1.jpeg)

# FRAGEN?

![](_page_29_Picture_4.jpeg)

![](_page_30_Picture_1.jpeg)

![](_page_30_Picture_2.jpeg)

![](_page_30_Picture_3.jpeg)

![](_page_30_Picture_5.jpeg)

![](_page_31_Picture_0.jpeg)

Welcher Code führt zu angegebener Ausgabe:

```
#include<iostream>
   using namespace std;
   // Auswahl an Klassenimplementierungen siehe nächste Folie
   int main(){
       Class object_1;
       Class object_2(2,84);
       object_1.print();
       object_2.print();
       return 0;
   }
1
```
Ausgabe 1 42 2 84

![](_page_32_Figure_0.jpeg)

![](_page_33_Figure_0.jpeg)

![](_page_34_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste

## Kopierkonstruktor

- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

#### KONSTRUKTOREN MIT PARAMETERN

- Wie eine Methode können Konstruktoren **Parameter** haben, um die Objekte mit individuellen Werten zu initialisieren.
- Bei bestimmten Parameterprofilen haben die Konstruktoren mit Parametern eigene Namen:
	- **Kopierkonstruktor**
		- (1 Parameter vom Typ der eigenen Klasse)
	- **Konvertierkonstruktor**
		- (1 Parameter von einem anderen Typ)
- Bei den Konstruktoren mit Parametern gelten auch die Regeln für Defaultwerte und für das Overloading.

### KOPIERKONSTRUKTOR

- Ein **Standard-**
	- **Kopierkonstruktor** ist für jede Klasse automatisch definiert. Man kann jedoch auch einen Kopierkonstruktor selbst definieren
- Der **Standard-Kopierkonstruktor** kopiert **elementweise**, macht also genau das, was der selbstdefinierte Kopierkonstruktor im Beispiel rechts auch macht.

```
#include <iostream>
    using namespace std;
    class Fraction {
         int _numerator, _denominator;
    public:
         Fraction(int n = 0, int d = 1) {
             _numerator = n;
             _denominator = d;
         }
         Fraction(const Fraction& f) {
             _numerator = f._numerator;
             _denominator = f._denominator;
         }
    };
    int main()
    {
         Fraction f_1;
         Fraction f_2(f_1);
         return 0;
    }
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
```
KOPIERKONSTRUKTOR BEI FUNKTIONSAUFRUF

```
 Funktionsdeklaration mit call-by-value:
  int fkt_cbv(Fraction f){
    return f.get_numerator()*f.get_denominator();
  }
```
- Zur Herstellung einer **lokalen Kopie** (also zum Initialisieren des Parameters **o** auf dem Stack) wird der **Kopierkonstruktor** aufgerufen.
- Der **Kopierkonstruktor** wird bei jedem Aufruf dieser Funktion verwendet.

![](_page_38_Picture_1.jpeg)

 Zur Vermeidung der Kopie eines aktuellen Parameters kann in C++ ein Referenzparameter benutzt werden (**call-by-reference**):

```
int fkt_cbr(Fraction& f){
  return f.get_numerator()*f.get_denominator();
}
```
![](_page_39_Picture_1.jpeg)

![](_page_39_Picture_2.jpeg)

![](_page_39_Picture_3.jpeg)

![](_page_39_Picture_5.jpeg)

![](_page_40_Picture_0.jpeg)

![](_page_40_Picture_1.jpeg)

 Zur Herstellung einer **lokalen Kopie** (also zum Initialisieren des Parameters **f** auf dem Stack) wird der **Kopierkonstruktor** aufgerufen.

```
int fkt_cbv(Fraction f){
  return f.get_numerator()*f.get_denominator();
}
```
 Was würde passieren, wenn im Kopierkonstruktur auch cbv gemacht würde?

```
Fraction(const Fraction f){
    _numerator = f.get_numerator();
    _denominator = f.get_denominator();
}
```
### SELBSTDEFINIERTER KOPIERKONSTRUKTOR

- Wann braucht man einen eigenen Kopierkonstruktor? Häufig dann, wenn dynamische Elemente im Spiel sind (Zeiger)!
- Der Standard-Kopierkonstruktor kopiert nur den/die Pointer, z.B. nur den Anker einer verketteten Liste.
- Man spricht von einer flachen Kopie.
- Will man jedoch die komplette Struktur kopieren, z.B. die ganze verkettete Liste, dann spricht man von einer tiefen Kopie.
- Für eine tiefe Kopie benötigt man einen selbstdefinierten Kopierkonstruktor.

### FLACHE KOPIE VS. TIEFE KOPIE

![](_page_42_Figure_2.jpeg)

![](_page_43_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor

## Konvertierkonstruktor

- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

### KONVERTIERKONSTRUKTOR

![](_page_44_Picture_1.jpeg)

 Ein Konvertierkonstruktor ist ein Konstruktor mit einem Parameter, der nicht ein Objekt der Klasse ist.

```
class Fraction
  {
       int _numerator, _denominator;
  public:
       Fraction(int n) {
            _numerator = n;
            _denominator = 1;
       }
1
2
3
4
5
6
7
8
9
                                            10
                                            12
                                            13
                                            14
                                            15
                                            16
                                            17
                                            18
```

```
Fraction(char n) {
    _numerator = int(n);
    _denominator = 1;
}
Fraction(string f) {
 // string in der Form
 // "int/int" }
    ...
```
![](_page_45_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor

# Konstruktoraufruf

- Destruktoren
- Standardmethoden und –operatoren

```
Fraction fraction_1(70, 90);
// Objektdefinition = Konstruktoraufruf (Argumenteliste)
Fraction fraction_2 = {70, 90};
// Alternative mit Initialisierungsliste {}
Fraction fraction_3 {70, 90};
// mit Initialisierungsliste {} ohne =
Fraction fraction_4 {};
// wie {0, 0}
```
![](_page_47_Picture_1.jpeg)

 Folgende Schreibweisen zum Aufruf des Konvertierkonstruktors sind möglich:

```
int i = 5;
Fraction f(i);
Fraction f = i;
Fraction f = (Fraction) i;
Fraction f = Fraction (i);
Fraction f = static_cast<Fraction>(i);
```
#### KONVERTIERUNG VON EINER KLASSE IN EINE ANDERE

![](_page_48_Picture_1.jpeg)

```
class Quotient {
       double result;
   public:
       Quotient (Fraction& f) {
            result = f.get_numerator()/
                     f.get_denominator();
       }
       void print() {
            cout << result << endl;
       }
   };
   int main()
   {
       Fraction f(12, 3);
       f.print();
       Quotient q(f);
       q.print();
       return 0;
   }
1
```
 Der Konvertierkonstruktor kann auch für die Konvertierung einer eigenen Klasse in eine andere genutzt werden: Fraction f(12,3); Quotient q(f); Ausgabe

![](_page_49_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf

## Destruktoren

Standardmethoden und –operatoren

#### DESTRUKTOREN

- Ein **Destruktor** ist das Gegenstück zum Konstruktor.
- Er hat **keine Parameter** und kann **nicht überladen** werden.
- Er wird **automatisch aufgerufen**, wenn der Gültigkeitsbereich eines Objektes verlassen wird, oder **delete** aufgerufen wird.
- Name: **~Fraction();**
- Es gibt einen **Standarddestruktor** des Compilers; er gibt nur den Speicher frei.
- Mit einem **eigens geschriebenen Destruktor** kann man Aktionen veranlassen, die mit dem zu 'destruierenden' Objekt zusammenhängen (Speicher löschen, Datei freigeben, 'tiefe' Struktur löschen).

![](_page_51_Picture_1.jpeg)

![](_page_51_Picture_2.jpeg)

![](_page_51_Picture_3.jpeg)

![](_page_51_Picture_5.jpeg)

![](_page_52_Picture_0.jpeg)

![](_page_52_Picture_1.jpeg)

```
#include <iostream>
    class Example
    {
    public:
          Example(int i = 0) // Konstruktor
             : _number{i}
         {
             std::cout << "Objekt " << _number
                        << " wird erzeugt.\n";
         }
         ~ Example()
         { // Destruktor
             std::cout << "Objekt " << _number
                        << " wird zerstört.\n";
         }
    private:
         int _number;
    };
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
```

```
// globale Variable, durch Vorgabewert 
// mit 0 initialisiert
Example a_global_example;
int main()
{
    std::cout << "main wird begonnen\n";
    Example an_example(1);
    {
        std::cout << " neuer Block\n ";
        Example an_example(2);
        std::cout << " Block wird
                        verlassen\n ";
    }
    std::cout << "main wird 
                  verlassen\n";
}
```
![](_page_53_Picture_0.jpeg)

![](_page_53_Picture_1.jpeg)

```
#include <iostream>
class Example
{
public:
     Example(int i = 0) // Konstruktor
         : _number{i}
    {
         std::cout << "Objekt " << _number
                    << " wird erzeugt.\n";
    }
    ~ Example()
    { // Destruktor
         std::cout << "Objekt " << _number
                    << " wird zerstört.\n";
    }
private:
    int _number;
};
                                                       // globale Variable, durch Vorgabewert 
                                                       // mit 0 initialisiert
                                                       Example a_global_example;
                                                       int main()
                                                       {
                                                           std::cout << "main wird begonnen\n";
                                                           Example an_example(1);
                                                           {
                                                                std::cout << " neuer Block\n ";
                                                                Example an_example(2);
                                                                std::cout << " Block wird
                                                                                 verlassen\n ";
                                                           }
                                                           std::cout << "main wird 
                                                                           verlassen\n";
                                                       }
                                                  19
                                                  20
                                                  21
                                                  22
                                                  23
                                                  24
                                                  25
                                                  26
                                                  27
                                                  28
                                                  29
                                                  30
                                                  31
                                                  32
                                                  33
                                                  34
                                                                                                       Ausgabe
                                                                                                  Objekt 0 wird erzeugt.
                                                                                                  main wird begonnen
                                                                                                  Objekt 1 wird erzeugt.
                                                                                                  neuer Block
                                                                                                  Objekt 2 wird erzeugt.
                                                                                                  Block wird verlassen
                                                                                                  Objekt 2 wird zerstört.
                                                                                                  main wird verlassen
                                                                                                  Objekt 1 wird zerstört.
                                                                                                  Objekt 0 wird zerstört.
```
![](_page_54_Picture_0.jpeg)

- "Initialisierung" von Objekten
- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

![](_page_55_Picture_0.jpeg)

STANDARDMETHODEN UND -OPERATOREN

- Standardkonstruktor **Fraction();**
- Defaultkopierkonstruktor **Fraction (const Fraction & f);**
- Defaultdestruktor
	- **~Fraction();**
- Defaultzuweisungsoperator **Fraction f\_1(1,2), f\_2; f\_2 = f\_1;**

#### KONSTRUKTOR UND MEHR VORGEBEN ODER VERBIETEN

![](_page_56_Picture_1.jpeg)

- Der Compiler erzeugt automatisch einen Konstruktor ohne Parameter, einen Kopierkonstruktor, einen Destruktor und einen Zuweisungsoperator, falls eine Klasse diese nicht zur Verfügung stellt.
- Um dem Programmierer mehr Kontrolle darüber zu erlauben, sind die syntaktischen Konstruktionen = default und = delete eingeführt worden. Das folgende Beispiel zeigt den Einsatz

```
class X
{
public:
    X() = default; // Compiler-generierten Konstruktor erlauben, obwohl es schon X(int) gibt.
    X(int i);
    X(const X &) = delete; // Kopieren verbieten
};
```
![](_page_57_Picture_0.jpeg)

![](_page_57_Picture_1.jpeg)

# FRAGEN?

![](_page_57_Picture_4.jpeg)

![](_page_58_Picture_0.jpeg)

# KLEINE ÜBUNG

#### AUFGABE

© HS Esslingen Implementieren Sie ein "dynamisches Array", das integer -Werte speichern kann. Neue Werte sollen durch die Methode push\_back (int) hinten im array eingefügt werden können. Durch die Methode at() sollen die Werte an der entsprechenden Position ausgelesen werden können. Die methode size() gibt die Größe des Arrays zurück. Durch das vorgegebene Hauptprogramm soll die Ausgabe (rechts) erzeugt werden.

![](_page_59_Picture_3.jpeg)

![](_page_60_Picture_0.jpeg)

# LABORAUFGABEN

![](_page_61_Picture_0.jpeg)

### AUFGABE 6

#### Themen: Initialisierung von Objekten, Konstruktoren, Destruktoren

### Ihre Aufgabe:

Schreiben Sie eine Klasse 'Student' mit den Attributen '\_name' und '\_first\_name' vom Typ String. Schützen Sie die Attribute gegen Zugriff von außen. Die folgenden Methoden implementieren sie außerhalb der Klasse: Die Klasse soll einen parametrisierten Konstruktor haben, der Name und Vorname entgegennimmt und die beiden Attribute '\_name' und '\_first\_name' entsprechend belegt. Verwenden Sie hierzu keine Initialisierungsliste. Schreiben sie get-Methoden für beide Attribute und einen Destruktor. Schreiben Sie zwei print-Methoden, beide ohne Rückgabewert. Eine der beiden Methoden nimmt eine boolsche Variable entgegen, mit der gesteuert werden kann, ob am Ende der Zeile ein Zeilenumbruch erfolgen soll oder nicht. In der anderen Methode erfolgt immer ein Zeilenumbruch.

#### AUFGABE 6 (2)

Schreiben Sie eine Klasse 'Employee', ebenfalls mit den Attributen '\_name' und '\_first\_name' vom Typ String. Schützen Sie auch diese Attribute gegen einen Zugriff von außen. Die folgenden Methoden implementieren sie innerhalb der Klasse: Die Klasse soll einen parametrisierten Konstruktor haben, der Name und Vorname entgegennimmt und die beiden Attribute '\_name' und '\_first\_name' entsprechend belegt. Verwenden Sie hierzu die Initialisierungsliste. Die Klasse soll einen Standardkonstruktor haben, die den Konstruktoraufruf an den parametrisierten Konstruktor delegiert. Nutzen Sie auch hier die Initialisierungsliste und setzen sie die Werte 'Mustermann' für Name und 'Erika' für Vorname. Schreiben Sie zusätzlich einen Konvertierkonstruktor, der einen Studenten entgegennimmt und die enthaltenen Daten zur Initialisierung von Name und Vorname verwendet. Schreiben sie einen Destruktor. Schreiben Sie auch für diese Klasse zwei print-Methoden, ebenfalls beide ohne Rückgabewert. Eine der beiden Methoden nimmt eine boolsche Variable entgegen, mit der gesteuert werden kann, ob am Ende der Zeile ein Zeilenumbruch erfolgen soll oder nicht. In der anderen Methode erfolgt immer ein Zeilenumbruch.

Die Methoden der beiden Klassen sollen jeweils eine Ausgabe enthalten, die zur Ausgabe der vorgegebenen main-Methode passt. Die Ausgabe ist unten angegeben.

![](_page_63_Picture_0.jpeg)

#### AUFGABE 6 (3)

Parametrisierter Konstruktor Student: Max Mustermann Konvertierungskonstruktor Employee: Max Mustermann Parametrisierter Konstruktor Employee: Erika Mustermann Standardkonstruktor Employee: Erika Mustermann print() ohne Parameter; Student: Max Mustermann print() mit Parameter; Student: Max Mustermann print() ohne Parameter; Mitarbeiter: Max Mustermann print() ohne Parameter; Mitarbeiter: Erika Mustermann Block wird betreten Parametrisierter Konstruktor Student: Markus Mustermann print() mit Parameter; Student: Markus Mustermann Block wurde verlassen Destruktor Student: Markus Mustermann Destruktor Employee: Erika Mustermann Destruktor Employee: Max Mustermann Destruktor Student: Max Mustermann

![](_page_64_Picture_0.jpeg)

# ZUSAMMENFASSUNG & AUSBLICK

![](_page_65_Picture_0.jpeg)

#### ZUSAMMENFASSUNG

- Standardkonstruktor
- Konstruktoren mit Parametern
- Initialisierungsliste
- Kopierkonstruktor
- Konvertierkonstruktor
- Konstruktoraufruf
- Destruktoren
- Standardmethoden und –operatoren

WAS KOMMT NÄCHSTE WOCHE?

- Weitere Klassenelemente
- Beziehungen zwischen Objekten

![](_page_66_Picture_3.jpeg)

![](_page_67_Picture_0.jpeg)

![](_page_67_Picture_1.jpeg)

# DANKE

![](_page_67_Picture_4.jpeg)