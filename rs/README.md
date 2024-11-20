# Dobrodošli na Srpski SNSWiki!

## Kako sajt funkcioniše / Kako doprineti

Sam <a href="https://sns.graphite.in.rs/">sajt SNSWiki</a> vuče podatke (stranice) odavde. Da bi stvorili stranicu morate da napravite folder koji odgovara stranici koju pokušavate da napravite, ime foldera je ujedno i naslov stranice. Struktura foldera je definisana [ovde](#struktura).

#### Kako zapravo napraviti novu stranicu

Kako sam ja zamislio da se koristi ovaj sajt je:

- Napišete članak u [editoru](#editor), da bi mogli uživo da pratite šta radite
- Kad završite ovde pravite novi fajl (na dugme "add file") i samo prebacite tekst iz wiki editora u GitHub editor.

Ali sam shvatio da većina ljudi koja verovatno želi da uredi nešto nije upoznata sa GitHub interfejsom i ne zna kako se dodaju fajlovi, folderi i slično.

##### 1. GitHub nalog

Nažalost GitHub zahteva da imate nalog da bi ste pravili izmene na repozitorijumima. To znači da morate napraviti GitHub nalog da bi doprineli SNSWiki.


## Generalna pravila uređivanja

- Držite se pouzdanih izvora, tabloide koji su privržni vlasti treba ređe koristiti.

- Za diskusiju oko neke specifične stranice koristite "discussions" tab, a ako želite da predložite nešto u vezi samog sajta (formatiranje, layout) koristite "issues" tab.

- Ostanite civilizovani, botovanje i vandalizam nisu dozvoljeni.

- Ton svih stranica sme da bude malo sarkastičan ali mora ostati objektivan, nalik Rational wiki.

- Svaka velika tvrdnja na stranici mora biti podržana sa odgovarajućim [izvorom](#izvori).

## `rs-meta.json` fajl

Ovaj fajl sadrži generalne meta-podatke za srpsku stranu sajta. Osim stranica (`pages` niz koji **ne treba dirati ručno**) koje sam repozitorijum prati i dodaje, takođe postoji i `featured` koji sadrži stranice koje se nalaze u "sidebar"-u sajta.

## Struktura jedne stranice <a name="struktura"></a>

Folder stranice treba da sadrži `.html` fajl sa istim imenom (ali malim slovima) i može sadržati `Images` folder koji sadrži sve slike koje ta stranica koristi.

Taj folder takođe može sadržati `link.cfg` fajl koji u sebi sadrži samo naziv te stranice na drugom jeziku. Ovo povezuje srpsku i englesku stranu sajta.

Sve u ovoj strukturi je **case-sensitive**, `Images` počinje velikim slovom, `.html` fajl je uvek sve malim slovima i `link.cfg` je takođe malim slovima. Samo ime foldera je naslov stranice koji se prikazuje na sajtu pa velika i mala slova trebaju da budu adekvatna.

#### Primer strukture jedne stranice:

```
📂 Covid Protesti 2020
┣ 📄 covid protesti 2020.html
┣ 📂 Images
┃  ┣ 🖼️ Protest_ispred_skupstine.png
┃  ┣ 🖼️ Policija_bije_gradjane.png
┃  ┗ 🖼️ Protest_2.png
┗ 📄 link.cfg
```

Ovde bi `covid protesti 2020.html` bila stranica koja se pojavljuje na sajtu pod imenom "Covid Protesti 2020", a u `link.cfg` bi pisalo ime te stranice na engleskoj strani wiki.

U suštini, jedino što je potrebno da sajt funkcioniše je sam folder i `.html` fajl unutar njega.

## Uputstvo za korišćenje editora<a name="editor"></a>

Pošto se stranice na ovom sajtu kreiraju i uređuju ovde, na GitHub-u, a GitHub nema opciju za preview toga što ste napisali, na sajtu se nalazi "on-site editor" u kom možete kucati i čuvati vaše nedovršene članke.

Editor ima par korisnih alatki, i sve opcije običnog text editora (undo, redo, itd.).

On može da čuva **maksimalno deset "draft"-ova** i svaki mora imati **različito ime**. 

**Dugme za brisanje drafta nema prompt da potvrdite brisanje, jednom kad kliknete malu kantu za smeće, draft je trajno obrisan.**

Preview dugme će zatvoriti text editor i pokazati vam kako bi vaša stranica izgledala da je uživo na sajtu.

Nažalost editor nema pristup slikama u `Images` folderu.

## Formatiranje

Jezik koji koristi ovaj wiki je, kao i sve ostalo, napravljen namenski od strane mene. On je zapravo samo našminkani HTML i koristi tagove za sve elemente i formatiranje. Svi custom tagovi imaju prefiks `w`.

Kao brzi 

### Osnovno formatiranje

Osnovno formatiranje kao što su *italic*, **bold** i slično se vrši kroz obični HTML. Dobra referenca za HTML je [W3Schools](https://www.w3schools.com/tags/).

Po potrebi moguće je koristiti HTML za bukvalno bilo šta na stranicama, ali to je malo naprednije i nije pokriveno ovim uputstvom.

### Naslovi  

Naslovi se označavaju sa tagovima `<w-h1>` do `<w-h3>`, gde je 1 najveći a 3 najmanji "header" tag. Koriste se tako što ubacujete tekst koji treba da bude naslov među tagove.

#### Primer:

`<w-h1>Ovo je najveći naslov</w-h1>`

### Slike

Slike se u stranicu ubacuju kroz `<w-image>` tag. Koristi se tako što u tag ubacite URL slike koju želite da prikažete. Opciono možete dodati tekst ispod slike tako što ćete ga ubaciti pored teksta, odvojeno s karakterom `|`.

U slučaju da se slika koju želite da iskoristite nalazi u `Images` folderu vaše stranice, možete samo navesti ime fajla te slike umesto URL-a.

#### Primeri:

Bez teksta:

`<w-image>https://example.com/</w-image>`

Sa tekstom:

`<w-image>https://example.com/|Ovo je neka slika</w-image>`

Slika u `Images` folderu:

`<w-image>Protest2.png|Slika protesta</w-image>`

### Linkovi

Linkovi se u stranice dodaju kroz `<w-a>` tag, on može da se koristi i za unutrašnje linkove (prema ostatku wikije) ili za spoljašnje linkove (koji vode ka drugim sajtovima). Tekst koji se pojavljuje umesto samog linka treba odvojiti s karakterom `|`.

Spoljašni linkovi koji vode ka wikipediji se vode kao unutrašnji, i nemaju ikonicu koju spoljašnji linkovi nose.

#### Primeri:

Spoljašnji: `<w-a>https://example.com/|primer spoljašnjeg linka</w-a>`

  
Unutrašnji: `<w-a>Aleksandar Vučić|primer unutrašnjeg linka</w-a>`

### Izvori <a name="izvori"></a>

Takozvani "inline" izvori se na ovoj wikiji dodaju sa tagom `<w-ref>`. Svaki izvor može imati ime, i tako se može iskoristiti opet. **Obavezno je dodati `<w-reflist>` tag na kraju stranice da bi se stvorio odvojen deo sa svim izvorima.**
  
Dobri izvori su: Knjige, novinski članci, informacije s nekog zvaničnog sajta, kratki isečci iz videa itd.

Izvor (po mogućnosti) treba da sadrži:

- Ime i prezime autora

- Godinu objavljivanja

- Ime materijala (naslov članka, naslov videa, ime knjige)

- URL do materijala

- Naglasiti ako je materijal preuzet iz arhiva (npr. Internet Archive/Wayback Machine)

#### Primer:

`<w-ref name="izbori 2012"><w-a>https://www.vreme.com/projekat/izbori-2012-rezultati-i-postizborna-trgovina/|"Izbori 2012: Rezultati i postizborna trgovina"</w-a>. <i>Vreme</i>. 10. Maj 2012. Arhivirano 30. Juna 2022.</w-ref>.`

Ako bi hteli opet da stavimo isti ovaj izvor sa istim brojem u jednom članku, samo bi napisali:

`<w-ref name="izbori 2012"></w-ref>`

`name` atribut **NIJE** obavezan, samo se koristi za ponovno korišćenje istog izvora.

Na kraju stranice stavljamo 

`<w-reflist></w-reflist>`

za listu svih izvora navedenih u tekstu.

### Anotacije

Anotacije (en. annotations) predstavljaju stilizovani tekst koji je "aligned" na sredini stranice. Koriste se za neke napomene, dodatne informacije ili upozorenja vezana za stranicu.

Oni se ubacuju u stranicu sa `<w-annotation>` tagom i imaju tri vrste: `none`, `warn` i `danger`. Ove vrste se određuju `type` atributom, a "default" je none.

`none` je običan *italic* tekst na sredini stranice. Inače obeležava neke dodatne informacije za čitaoca, kao na primer ako postoji drugi članak sa sličnim imenom.

`warn` ima žutu marginu i obaveštava o nekim važnim ali ne i nužno hitnim stvarima. Na Wikipediji on bi se koristio da se označi kad je neki članak "outdated" ili ako nema dovoljno izvora.

`danger` ima crvenu marginu i obaveštava o stvarima koje hitno moraju da se promene na stranici. Na Wikipediji on bi se koristio da obavesti druge urednike da je članak neadekvatan za sajt i da ga treba obrisati.

#### Primer:

`<w-annotation> Ovo je članak o Covid protestima 2020. godine, za ekološke proteste sličnog imena, pogledajte <w-a>Ekološki protesti 2020</w-a></w-annotation>`

`<w-annotation type="warn">Ovaj članak nema dovoljno izvora. Treba dodati još.</w-annotation>`

### Infoboksovi

Infoboks (en. infobox) je element koji sadrži neke generalne informacije o stranici na kojoj se nalazi. Evo primera sa wikipedije:

![Primer](../images/oreo-primer.png)

Na mom sajtu se infoboksevi dodaju u sledećoj formi:

```
<w-infobox title="COVID Protesti 2020">
[Infoboks elementi]
</w-infobox>
```

**Infoboks elementi**, koji imaju prefiks `wi-`, su sledeći:

`<wi-section>` je naslov odeljka u infoboksu. Koristi se isto kao tagovi za naslov samo što nema više veličina. Default boja pozadine naslova je plava.

`<wi-image>` je puna slika u infoboksu. Koristi se kao obični tag za [slike].

`<wi-row>` koji predstavlja obični red u infoboksu sa levom i desnom vrednošću. Leva i desna strana su odvojene karakterom `|`. I leva i desna strana mogu da sadrže linkove i liste. 

Nasuprot, da bi stavili SLIKU na levu ili desnu stranu morate koristiti element `<wic-image>`. Koristi se isto kao drugi elementi za slike ali ne može da ima tekst ispod.

`<wi-vs>` je element koji služi za prikazivanje dve suprotstavljene strane. Primer sa wikipedije je ispod.

On u sebi mora da sadrži bar 2 `<wvs-side>` dela, koji predstavljaju suprotstavljene strane, i te strane moraju sadržati svoje partije koje su predstavljene `<wvs-p>` elementom.

Same partije mogu biti običan tekst, linkovi ili liste. Ako je partija lista u `<wvs-p>` element je moguće staviti dva opciona atributa, `list` i `collapsed`.

`list` označava boldovani naslov liste, a `collapsed` označava da li je ta lista "kolapsovana" (sakrivena).

#### Primer: