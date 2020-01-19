Om een brede waaier aan oefeningen te kunnen oplossen, heb ik geprobeerd om het
concept van een *oplossing* zo algemeen mogelijk op te vatten. Een oplossing
(`Solution`) heeft twee attributen: `steps` en `value`. Het attribuut `steps` 
bevat de stappen (`Step`s) van de oplossing. Het attribuut `value` is de 
uitkomst van de oplossing.

# Solvers

Een *solver* is een functie die een `Solution` teruggeeft. Om een solver 
gemakkelijk te onderscheiden van andere functies, begint de naam van een solver 
altijd met `solve_*`, bijvoorbeeld `solve_find_grade()`. In principe kan je een 
solver ook gebruiken als *gewone* functie, door van het teruggegeven 
`Solution`-object enkel het attribuut `value` te gebruiken. In het geval van de 
solver `solve_find_grade()`, bijvoorbeeld, zal het attribuut `value` de waarde
van de graad bevatten.

# De stappen van een `Solution`

Een `Solution` heeft naast een attribuut `value` ook een attribuut `steps`. Dat
attribuut bevat een lijst met stappen (`Step`-objecten) die leiden tot de
oplossing. Een `Step` bestaat dan weer uit **vier verklaringen**
(`Explanation`s) die verduidelijken wat er in de stap gebeurt:

1. het doel (`purpose`);
2. de uitvoering (`execution`);
3. het resultaat (`result`);
4. een controle (`check`).

Die `Explanation`-objecten zijn de *bouwblokken* van de
stap-per-stap-oplossingen in STEMbox. Je kan ze zien als een soort mini-lessen
in de stijl van *Hoe Zit Het?*.

# De `description` van een `Explanation`

Het belangrijkste attribuut van een `Explanation` is zijn `description`. Je kan
het vergelijken met het Markdown-bestand dat je zou schrijven voor een les van
*Hoe Zit Het?*. Om de uitleg duidelijker te maken, kan je in de tekst van
`description` ook illustraties gebruiken. Dat doe je op een gelijkaardige
manier als hoe je in Markdown afbeeldingen kan toevoegen (zie ook
[hier](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images)):

```md
Hieronder staat een mooie afbeelding:

![hier schrijf je de alt text](https://image.insider.com/59ae8e6c2488496fc3605a0f "En hier de title text")
```

In STEMbox gebruiken we geen urls om naar illustraties te verwijzen, maar
verwijzen we vanuit het `description`-Attribuut van een `Explanation` naar het
`illustration`-attribuut van diezelfde `Explanation`. Dat doen we met een
syntax die gebaseerd is op [JSONPath](https://jsonpath.com/).

Het resultaat van het oplossen van een vergelijking zou bijvoorbeeld de
volgende `Explanation` kunnen bevatten:

```
{
   description: "We vinden dat ![onbekende]($.lhs) gelijk is aan ![oplossing]($.rhs).",
   
   illustration: {
     lhs: {
       sign: "+", 
       symbol: "x"
     },
     rhs: {
       sign: "-",
       absvalue: "3"
     },
   },
   
   short: "$"
}
```

In het `description`-attribuut zie je `$.lhs` en `$.rhs` staan. Die verwijzen
naar het `illustration`-attribuut.  `$.lhs`, bijvoorbeeld, moet je
interpreteren als: "plaats hier het attribuut `lhs` van het object in het
`illustration`-attribuut. De attributen van een
[`Illustration`](src/stembox/elements/illustr.py) zijn zelf ook
`Illustration`s, dus `$.lhs` is ook een `Illustration`.

Uiteindelijk kan bovenstaande `Explanation` bijvoorbeeld omgezet worden naar de
onderstaande markdown:

```
We vinden dat $x$ gelijk is aan $-3$.
```

Merk op dat een `Illustration` kan bestaan uit meerdere `Illustration`s (zie de
klasse `ListIllustration`), net als dat een vergelijking bestaat uit meerdere
symbolen. De attributen `label` en `mark` zijn dan ook vooral interessant voor
`Illustration`s die onderdeel zijn van een andere `Illustration`.

# Van `Illustration` naar illustratie

Een `Illustration` is slechts een abstracte voorstelling van een illustratie in
de vorm van een Python-object. Uiteindelijk moet deze nog omgezet worden naar
een echte illustratie. Dat is de taak van **renderers**. De renderers zijn
verzameld in het [`stembox.io`](src/stembox/io) package, meer bepaald in de modules die
eindigen op `*out.py`. De naam van de module vertelt het formaat naar waar
`Solution`s - en dus `Illustration`s - zullen worden omgezet. Het bestand
[`mdout.py`](src/stembox/io/mdout.py), bijvoorbeeld, bevat renderers die
`Sollution`-objecten kunnen omzetten naar Mardown-bestanden.

## `Illustration`s zelf verduidelijken met `label`s en `mark`s

Soms is het nuttig dat er in de illustratie zelf ook nog eens dingen staan
aangeduid. Op een grafiek zouden we bijvoorbeeld met een pijltje het nulpunt
kunnen aanduiden, of in een vergelijking zouden we kunnen aanduiden welke
termen *geschrapt* mogen worden.

Hiervoor dienen de attributen `label` en `mark` van de klasse `Illustration`.
Met `label` kunnen we een korte tekstuele uitleg toevoegen aan de illustratie,
zoals bij het aanduiden van een nulpunt op een grafiek.
Het attribuut `mark` daarentegen is een globale categorie waarmee we kunnen
aangeven dat bepaalde illustraties bij elkaar horen, bijvoorbeeld termen die kunnen
geschrapt worden in een vergelijking.
