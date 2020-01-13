Om een brede waaier aan oefeningen te kunnen oplossen, heb ik geprobeerd om het
concept van een *oplossing* zo algemeen mogelijk op te vatten. Een oplossing
(`Solution`) bevat een of meerdere stappen (`Step`s) in het attribuut `steps`.
Losstaand van hoe de oplossing is bereikt, bevat een `Solution` ook de uitkomst
van de oplossing in het attribuut `value`.

Een `Step` bestaat dan weer uit een of meerdere verklaringen (`Explanation`s).
Meer bepaald kan een `Step` vier mogelijke `Explanation`s bevatten: het doel
(`purpose`), de uitvoering (`execution`), het resultaat (`result`) en een
controle (`check`) van de stap.

Een `Explanation` kan een uitgebreide tekstuele beschrijving (`description`),
een korte tekstuele beschrijving (`short`) en een illustratie (`illustration`)
bevatten.

Het meest interessante onderdeel van een `Explanation` is haar `illustration`.
Dat attribuut is van het abstracte type `Illustration`. De package
`stembox.illustrs` bevat implementaties van deze abstracte klasse.

# Wat zijn `Illustration`s?

Het idee achter de `Illustration`-klasse is om puur tekstuele (*verbose*)
uitleg visueel te kunnen verduidelijken. Dat kan met een tekening zijn, maar
ook bijvoorbeeld met een vergelijking.

## `Illustration`s verduidelijken met `label`s en `mark`s

Soms is het nuttig dat er in de illustratie zelf ook nog eens dingen staan
aangeduid. Op een grafiek zouden we bijvoorbeeld met een pijltje het nulpunt
kunnen aanduiden, of in een vergelijking zouden we kunnen aanduiden welke
termen *geschrapt* mogen worden.

Hiervoor dienen de attributen `label` en `mark` van de klasse `Illustration`.
Met `label` kunnen we een korte tekstuele uitleg toevoegen aan de illustratie,
zoals bij het aanduiden van een nulpunt op een grafiek.
Het attribuut `mark` daarentegen is een globale categorie waarmee we kunnen
aangeven dat bepaalde illustraties bij elkaar horen, net als termen die kunnen
geschrapt worden in een vergelijking.

Merk op dat een `Illustration` kan bestaan uit meerdere `Illustration`s (zie de
klasse `ListIllustration`), net als dat een vergelijking bestaat uit meerdere
symbolen. De attributen `label` en `mark` zijn dan ook vooral interessant voor
`Illustration`s die onderdeel zijn van een andere `Illustration`.

## De methodes van een `Illustration`

Illustraties van een uitleg kunnen erg verschillen, gaande van een grafiek tot
een vergelijking tot een combinatie van beide. Om geen beperkingen op te leggen
aan illustraties, bestaat een `Illustration` uit algemene Python-objecten die
kunnen opgevraagd en ingesteld worden met de methodes `get_at_path` en
`set_at_path`, respectievelijk.
