#!/usr/bin/env python3
"""Standalone import script for GA132 — GA132 - Die Evolution vom Gesichtspunkte des Wahrhaftigen"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA132 - Die Evolution vom Gesichtspunkte des Wahrhaftigen"""
GA_NUMBER = "GA132"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG Berlin, 31. Oktober 1911",
    "paragraphs": [
      "Wenn wir in den Betrachtungen, welche wir im vorigen Jahre in unse­ren Zweigabenden gepflogen haben, fortfahren wollen, so ist es not­wendig, daß wir uns noch einige andere Begriffe, Vorstellungen, Anschauungen aneignen, als die sind, von denen bisher gesprochen worden ist. Wir wissen, daß wir gar nicht auskommen konnten mit dem, was wir über die Evangelien und sonstige geistige Dokumente der Menschheit zu sagen haben, wenn wir nicht vorausgesetzt hätten jene Entwickelung unseres ganzen Weltsystems, die wir da bezeichnen als die Verkörperungen unseres Planeten selber durch das Saturndasein, durch das Sonnendasein, das Mondendasein, bis herauf zum gegenwär­tigen Erdendasein.",
      "Wer sich zurückerinnert, wie oft an diese Grundvor­stellungen angeknüpft werden mußte, der weiß, wie notwendig für alle okkulte Betrachtung der Menschheitsentwickelung diese Grundvorstel­lungen eben sind. Wenn Sie nun die Angaben sich einmal ansehen, welche zum Beispiel in der «Geheimwissenschaft im Umriß» gegeben sind über die Saturn-, Sonnen- und Mondentwickelung bis zur Erdentwickelung herein, so werden Sie sich gestehen, daß es sich dabei - und selbst, wenn es noch viel ausführlicher wäre, könnte es nicht anders sein - nur um eine Skizze handeln kann, nur um Angaben, die von einer ge­wissen Seite, von einem gewissen Gesichtspunkte aus, gemacht werden können.",
      "Denn wie das Erdendasein eine unendliche Fülle von Einzel­heiten bietet, so ist es ganz selbstverständlich, daß wir auch für das Saturn-, Sonnen- und Monddasein eine unendliche Reihe von Einzel­heiten zu verzeichnen haben, und daß immer nur eine ganz grobe Kohlezeichnung, eine Art Umriß, gegeben werden kann. Für uns ist aber eine Charakteristik der Evolution noch von einer anderen Seite aus notwendig.",
      "Wenn wir uns fragen: Woher stammen alle die Angaben, die da gemacht worden sind? - so wissen wir, daß sie von den sogenannten Eintragungen in die Akasha-Chronik stammen. Wir wissen, daß das, was einmal geschehen ist oder vorgeht im Verlaufe der Weltentwicke­lung, gewissermaßen zu lesen ist wie durch eine Eintragung in eine",
      "feine geistige Substanz, in die Akasha-Substanz. Von allem, was sich abgespielt hat, gibt es eine solche Eintragung, aus welcher entnommen werden kann, wie die Dinge einmal waren. Nun werden wir natürlich annehmen können, daß, ebenso wie dem gewöhnlichen Blick, der irgend etwas von unserer physischen Welt überblickt, die Dinge, die in der Nähe sind, in ihren Einzelheiten mehr oder weniger klar und deut­lich, und je weiter sie entfernt sind, mehr oder weniger unklar erschei­nen, so werden auch die Dinge, die zeitlich in unserer Nähe sind, die der Erden- oder der Mondentwickelung angehören, sich genauer ange­ben lassen; wogegen die Dinge, die zeitlich weiter entfernt sind, un­deutlichere Umrisse bekommen, so zum Beispiel, wenn wir in das Saturn- oder Sonnendasein hellseherisch zurückblicken.",
      "Warum tun wir das überhaupt, daß wir einen gewissen Wert darauf legen, so weit hinter uns liegende Zeiträume zu verfolgen? Es könnte ja jemand sagen: Wozu bringen diese Anthroposophen allerlei so uralte Dinge heute noch zur Sprache? Man braucht sich doch in der Welt nicht um diese uralten Dinge zu kümmern, denn man hat doch genügend zu tun mit dem, was gegenwärtig vorgeht!",
      "Es wäre sehr unrichtig, so zu sprechen. Denn, was einmal vorgegan­gen ist, das vollzieht sich heute noch fortwährend. Was in der Saturn­zeit sich abgespielt hat, das ist nicht bloß dazumal gewesen, sondern das geht heute noch vor, nur wird es überdeckt, unsichtbar gemacht durch das, was heute äußerlich um den Menschen auf dem physischen Plan ist. Und recht, recht stark unsichtbar wird gerade das alte Saturn­dasein gemacht, das vor so langer Zeit sich abgespielt hat. Aber es geht den Menschen noch etwas an, heute noch, das alte Saturndasein. Und um uns eine Vorstellung zu machen, wie es uns angeht, wollen wir uns folgendes vor die Seele stellen.",
      "Wir wissen, daß der innerste Kern unseres Wesens uns entgegentritt als das, was wir unser «Ich» nennen. Dieses Ich, der innerste Kern unseres Wesens, ist wahrhaftig für den heutigen Menschen eine recht übersinnliche, eine recht unwägbare Wesenheit. Wie unwägbar sie ist, kann schon daraus geschlossen werden, daß es heute Seelenlehren gibt, die sogenannten offiziellen Psychologien, die überhaupt keine Ahnung mehr davon haben, daß auf ein solches Ich hinzudeuten ist.",
      "Ich habe schon öfter darauf aufmerksam gemacht, daß sich nach und nach im 19. Jahrhundert in der deutschen Psychologie der schöne Ausdruck herausgebildet hat «Seelenlehre ohne Seele». Namentlich war tonangebend für diese «Seelenlehre ohne Seele» - obwohl das Wort nicht von ihr geprägt worden ist - die heute weltberühmte Schule Wundts' die ja nicht bloß in den deutschen Landen ausschlag­gebend ist, sondern die überall, wo von Psychologie geredet wird, mit großen Ehren genannt wird. «Seelenlehre ohne Seele» könnte man so ausdrücken: sie lehre, ohne auf ein selbständiges Seelenwesen Rück­sicht zu nehmen, daß sich alle Eigenschaften der Seele erst sammeln in einer Art von Brennpunkt, sich versammeln im Ich. Man kann sich einen größeren Unsinn gar nicht denken, dennoch steht die heutige Psychologie ganz unter dem Eindruck dieses Unsinns. Und diese «Seelenlehre ohne Seele» ist heute in der ganzen Welt berühmt. Künf­tige Kulturgeschichtsschreiber werden viel zu tun haben, wenn sie es unseren Nachkommen plausibel machen wollen, wie so etwas möglich war, daß im 19. Jahrhundert und weit ins 20. hinein so etwas als die größte Leistung auf psychologischem Gebiete angeschlagen worden ist. Das alles soll nur gesagt werden, um anzudeuten, wie unklar sich gerade die offizielle Psychologie über das ist, was wir als den Mittel­punkt des menschlichen Wesens bezeichnen.",
      "Wenn man das Ich klar erfassen und so vor sich hinstellen könnte wie den äußeren physischen Leib, und wenn man die Umgebung, von der das Ich so abhängt, wie der physische Leib von dem abhängt, was von außen durch die Augen gesehen, durch die Sinne sonst wahr­genommen werden kann, wenn man ebenso die Umgebung des Ich suchen könnte, wie man im physischen Reich die Umgebung in den Wolken, Bergen und so weiter hat, oder wie zum Beispiel der physische Leib abhängt von seinen Nahrungsmitteln, so käme man zu einer Weltcharakteristik, zu einem Weltentableau, heute noch, in dem, gleichsam imprägniert, unsere sonstige Umgebung enthalten ist, un­sichtbar drinnensteckt, und das gleich ist dem Weltentableau des alten Saturn. Das heißt, wer das Ich in seiner Welt kennenlernen will, der muß sich eine solche Welt vor Augen stellen können, wie der alte Saturn war. Diese Welt ist verdeckt, ist eine übersinnliche Welt für",
      "den Menschen. Der Mensch könnte sie auch in dem heutigen Grade sei­ner Entwickelung durchaus nicht ertragen. Sie ist ihm durch den Hüter der Schwelle zugedeckt, damit sie vor ihm verborgen bleibe, und es gehört ein gewisser Grad spiritueller Entwickelung dazu, um einen solchen Anblick aushalten zu können.",
      "Es ist ja in der Tat ein Anblick, an den man sich erst gewöhnen muß. Sie müssen sich vor allen Dingen von alledem eine Vorstellung ma­chen, was notwendig ist, um überhaupt dahin zu kommen, ein solches Weltentableau als etwas Wirkliches noch empfinden zu können.",
      "Alles, was Sie mit den Sinnen wahrnehmen können, müßten Sie sich wegden­ken, müßten sich auch fortdenken Ihre Innenwelt, insofern dieselbe aus den gewöhnlichen Gemütsbewegungen besteht. Der Mensch müßte sich weiter wegdenken von dem, was in der Welt ist, auch alles, was er an Vorstellungen in sich hat.",
      "Also von der Außenwelt müßten Sie alles wegnehmen, was Sinne wahrnehmen können, und vom Inneren alles, was Gemütsbewegungen, Vorstellungen sind. Und wenn Sie jetzt von jener Seelenverfassung sich einen Begriff machen wollen, in die der Mensch kommen muß, wenn er den Gedanken real faßt: Alles das wäre weggeschafft, aber der Mensch wäre noch da -, dann kann man nicht anders sagen als, der Mensch muß lernen, Schauder, Furcht emp­finden zu können vor der unendlichen Leere, die sich da auftut um uns herum.",
      "Man muß gleichsam seine Umgebung empfinden können wie ganz und gar gesättigt, tingiert mit dem, was uns von allen Seiten Schauder, Furcht erregt, und muß zu gleicher Zeit in der Lage sein, diese Furcht durch innere Festigkeit und Sicherheit seines Wesens über­winden zu können. Ohne diese zwei Gemütsstimmungeu, Schauder und Furcht vor der unendlichen Leere des Daseins und der Überwin­dung dieser Furcht, kann man überhaupt gar keine Ahnung empfin­den von dem, was unserem Weltendasein als das alte Saturndasein zugrunde liegt.",
      "Beide Empfindungen, wie sie jetzt charakterisiert worden sind, kul­tivieren ja die Menschen wenig bei sich selber. Daher findet man sogar in der Literatur wenig Beschreibungen von diesem Zustand. Es kennen diesen Zustand natürlich die, welche durch hellseherische Kräfte den Dingen auf den Grund zu gehen versuchen im Laufe der Zeit. Aber in",
      "der äußeren Literatur, der geschriebenen oder gedruckten, finden sich nur wenig Angaben darüber, daß Menschen so etwas empfunden ha­ben wie das Schaudern vor der unendlichen Leere oder gar die Über­windung dieses Schauderns. Um eine Art äußeren Einblick in die Sache zu haben, versuchte ich ein wenig nachzugehen in der jüngeren Literatur, wo so etwas auftreten könnte wie dieses Schaudern vor der unermeßlichen Leere in einem Menschen.",
      "Die Philosophen sind ja ge­wöhnlich ungeheuer klug, reden in ihren Begriffen abgeklärt und ver­meiden es, von den großen, imponierenden Eindrücken zu sprechen. Dort findet man nicht so leicht etwas darüber.",
      "Nun will ich nicht davon sprechen, wo ich überall nichts gefunden habe. Aber einmal habe ich doch einen kleinen Anklang an diese Empfindungen gefun­den, und zwar in dem Tagebuch des Hegelianers Karl Rosenkranz, wo er manchmal intime Gefühle schildert, wie er sie gehabt hat beim Durchleben der Hegelschen Philosophie.",
      "Ich habe auf eine merkwür­dige Stelle stoßen können, die bei ihm so herauskommt wie eine un­schuldige Stelle, die er in sein Tagebuch fixierte. Karl Rosenkranz macht sich klar, daß die Hegelsche Philosophie ausgeht von dem «reinen Sein».",
      "Von diesem « reinen Sein» Hegels ist viel geschwatzt worden in der philosophischen Literatur des 19. Jahrhunderts, aber man muß sagen, es ist wenig verstanden worden. Man möchte fast sa­gen, in der Philosophie der zweiten Hälfte des 19.",
      "Jahrhunderts - das kann man natürlich nur im intimsten Kreise sagen! - versteht man von dem «reinen Sein» Hegels soviel wie der Ochs vom Sonntag, wenn er die ganze Woche hindurch Gras gefressen hat. Es ist ein durchgesiebter Begriff, dieses «reine Sein» Hegels - nicht das Seiende, sondern das Sein -, es ist ein Begriff, der wahrhaftig noch nicht das ist, was ich jetzt charakterisiert habe als die schauervolle, Furcht einflößende Leere, aber es ist der ganze Raum im Hegelschen Sein tingiert mit der Eigenschaft, die nichts hat, was vom Menschen erlebt werden kann:",
      "die Unendlichkeit, mit Sein erfüllt. Und Karl Rosenkranz empfindet es einmal wie ein schauervolles Durchschütteltsein von einer Kälte, die mit nichts tingiert ist als mit dem Sein.",
      "Um zu begreifen, was der Welt zugrunde liegt, genügt es nicht, daß man in Begriffen darüber redet, sich Begriffe, Ideen davon macht;",
      "sondern es ist viel notwendiger, daß man sich eine Vorstellung hervor­rufen kann von dem Empfinden, das entsteht gegenüber der unend­lichen Leere des alten Saturndaseins. Das Gemüt ergreift dann, wenn es nur eine Ahnung davon erhält, das Gefühl des Schauderns. Wenn man hellseherisch aufsteigen will, damit man dann zum Schauen dieses Saturnzustandes kommt, muß man sich in der Weise vorbereiten, in­dem man sich in der Tat ein Gefühl erwirbt, das in gewisser Beziehung ausgeht von dem jedem Menschen mehr oder weniger bekannten Ge­fühl des Schwindelns auf hohem Berge, wenn der Mensch über einem Abgrunde steht und keinen sicheren Boden unter den Füßen zu haben glaubt; ein Gefühl, daß er an keinem Orte verbleiben könnte, so daß er sich übergeben wollte an Mächte, an Kräfte, über die er keine Macht mehr hat. Das ist aber erst das Elementare dieses zu ahnenden Gefüh­les. Denn man verliert nicht nur den Boden unter den Füßen, sondern auch das, was Augen sehen, Ohren hören, Hände greifen können, über­haupt das, was in der räumlichen Umgebung ist; und es kann nicht anders sein, als daß man jeden Gedanken verliert, daß man in eine Art von Dämmerung oder Schlafzustand verfällt, in dem man auch zu keiner Erkenntnis kommen kann. Oder aber man lebt sich hinein in jene Empfindung, und dann gibt es nichts anderes, als daß man zu jenem Schauerzustande kommt, und oft ist es eine Art von Schwindel-zustand, der nicht besiegt werden kann.",
      "Nun gibt es zwei Möglichkeiten für den heutigen Menschen. Die eine sichere Möglichkeit ist die, daß jemand die Evangelien verstanden hat, das Mysterium von Golgatha verstanden hat. Wer sie wirklich in ihrer vollen Tiefe verstanden hat - natürlich nicht so, wie die moder­nen Theologen heute darüber reden, sondern so, daß er daraus heraus-gesogen hat das Tiefste, was der Mensch daraus innerlich erfahren kann -, der nimmt etwas mit in jene Leere hinein, das sich wie von einem Punkte aus vergrößert und die Leere ausfüllt mit etwas, was mutähnlich ist, was ein Gefühl von Mut, von Geborgensein ist durch das Vereintsein mit jener Wesenheit, die auf Golgatha das Opfer voll­bracht hat. Der andere Weg ist der, daß wir ohne die Evangelien ein­dringen in die geistigen Welten, daß wir durch wahre, echte Theoso­phie in die geistigen Welten eindringen. Das kann auch geschehen. Sie",
      "wissen, daß wir zunächst immer betonen: wir gehen nicht von den Evangelien aus, wenn wir das Mysterium von Golgatha betrachten, sondern wir kämen dazu auch, wenn es gar keine Evangelien gäbe. Das hat, bevor das Mysterium von Golgatha geschehen ist, nicht sein können; das ist aber heute der Fall, weil etwas in die Welt gekommen ist durch das Mysterium von Golgatha, wodurch der Mensch die gei­stige Welt unmittelbar aus den Impressionen heraus selber begreifen kann.",
      "Das ist das, was wir das Walten des Heiligen Geistes in der Welt nennen können, das Walten der Weltgedanken in der Welt. Wenn wir eines oder das andere mitnehmen, können wir uns nicht verlieren und können nicht sozusagen abstürzen in den unendlichen Abgrund, wenn wir der schauervollen Leere zunächst gegenüberstehen.",
      "Wenn wir uns nun dieser schauervollen Leere nähern mit den anderen Vorbereitun­gen, welche uns durch die verschiedenen Mittel gegeben sind, wie es zum Beispiel in «Wie erlangt man Erkenntnisse der höheren Welten?» ausgeführt ist und in dem, was sich weiter darauf aufbaut, und ein­dringen in eine Welt, die herausgeboren ist aus dem, was unser Gemüt erschüttern, was unsere Vorstellungen erfassen kann, wenn wir uns einleben in diese Welt, dann lernen wir, indem wir uns sozusagen einstellen auf das Saturndasein, zunächst Wesenheiten kennen - jetzt aber nicht etwas, was ähnlich schaut dem Tierreich, Pflanzenreich oder Mineralreich, sondern Wesenheiten; es ist ja eine Welt, in der keine Wolken sind, auch kein Licht ist, in der es auch ganz tonlos ist -, aber wir lernen kennen Wesenheiten, und zwar jene Wesenheiten lernen wir kennen, die in unserer Terminologie genannt werden die Geister des Willens oder die Throne. Diese Geister des Willens lernen wir gerade so kennen, daß es wie eine richtige Gegenständlichkeit für uns wird, man könnte sagen: ein wogendes Meer des Mutes.",
      "Was sich der Mensch zunächst nur vorstellen kann, das wird hell­seherisch Gegenwart. Denken Sie sich getaucht in das Meer, aber jetzt getaucht als geistiges Wesen, welches sich eins fühlt mit der Christus­-Wesenheit, getragen von der Christus-Wesenheit, schwimmend, aber jetzt nicht in einem Meere von Wasser, sondern in einem den unend­lichen Raum erfüllenden Meere von - es gibt keine andere Bezeich­nung dafür - flutendem Mute, flutender Energie! Das ist nicht etwa",
      "bloß ein gleichgültiges, undifferenziertes Meer, sondern alle Möglich­keiten und Unterschiedlichkeiten dessen, was man bezeichnen kann mit dem Gefühl des Mutes, tritt uns da entgegen. Wir lernen kennen Wesenheiten, die zwar aus Mut bestehen, die wir aber, wenn sie auch nur aus Mut bestehen, sehr wohl als konkrete Wesenheiten treffen. Es erscheint natürlich ganz sonderbar, wenn man sagt, man treffe Wesen­heiten, die ebenso real sind wie der Mensch aus Fleisch, und die nicht aus Fleisch, sondern aus Mut bestehen. Aber es ist so. Als solche Wesen­heiten treffen wir die Geister des Willens, und zunächst bezeichnen wir nur das als Saturndasein, was die Geister des Willens, die aus Mut bestehen, darstellen, nichts sonst. Das ist zunächst Saturn. Das ist eine Welt, von der wir nicht sagen könnten, sie sei eine Welt, die kugelför­mig, sechseckig oder viereckig ist. Alle diese Bestimmungen des Rau­mes passen nicht darauf, denn es gibt dort nicht die Möglichkeit, ein Ende zu finden. Wenn wir noch einmal das Bild vom Schwimmen ge­brauchen wollen, so können wir sagen: es ist nicht ein Meer, wo man an eine Oberfläche kommen würde, sondern nach allen Seiten findet man immer Geister des Mutes oder des Willens.",
      "Ich werde in späteren Vorträgen charakterisieren, wie man nicht gleich auf einmal zu dieser Sache kommt, ich will jetzt nur dieselbe Ordnung einhalten wie früher: Saturn, Sonne, Mond, denn es ist viel besser, wenn man die umgekehrte Richtung einhält: von der Erde zum Saturn. Jetzt charakterisiere ich umgekehrt, das macht aber nichts.",
      "Wenn man sich bis zu diesem Anschauen erhoben hat, tritt eines ein, was für den ungeheuer schwer ist, sich vorzustellen, der sich nicht be­müht, langsam und allmählich zu solchen Vorstellungen zu kommen. Denn es hört etwas auf, was mit dem gewöhnlichen menschlichen Vor­stellen so verquickt ist wie nur irgend etwas: der Raum hört auf! Es hat keinen Sinn mehr, zu sagen, man schwimme oben oder unten, vorn oder hinten, rechts oder links. Es ist überall gleich in dieser Be­ziehung. Aber das Wichtige ist: wenn man in die ersten Zeiten des Saturndaseins kommt, so hört auch die Zeit auf! Es gibt kein Früher oder Später mehr. Das ist natürlich für den Menschen heute sehr schwer vorzustellen, weil sein Vorstellen selbst in der Zeit verfließt:",
      "ein Gedanke ist vor oder nach dem anderen. Daß die Zeit aufhört, das",
      "ist nun wieder nur durch ein Gefühl zu charakterisieren. Dieses Gefühl ist wahrhaftig nicht angenehm. - Denken Sie sich einmal Ihre Vorstel­lungen erstarrt, indem alles, woran Sie sich erinnern können und was Sie sich vornehmen, wie zu einem starren Stabe erstarrt, so daß Sie sich festgehalten fühlen in Ihrem Vorstellen und sich nicht mehr rühren können. Dann werden Sie nicht mehr sagen können, Sie haben etwas, was Sie früher erlebt haben, «früher» erlebt. Sie sind angebun­den daran, es ist da, aber es ist erstarrt. Die Zeit hört auf, eine Bedeu­tung zu haben. Sie ist überhaupt nicht mehr da. Deshalb ist es auch ziemlich unsinnig, wenn man fragt: Du schilderst da das Saturndasein, das Sonnendasein und so weiter, sage doch, was vor dem Saturndasein war! «Vorher» hat da keinen Sinn mehr, weil die Zeit aufhört, so daß man auch aufhören muß mit allen Zeitbestimmungen. Es ist wirklich beim alten Saturndasein - in einem sehr vergleichsweisen Sinn kann man das sagen - die Welt wie mit Brettern verschlagen, indem man mit dem Gedanken stillestehen muß. Mit dem Hellsehen auch. Die gewöhnlichen Gedanken muß man schon lange zurücklassen, die gehen nicht bis dahin. Bildlich, vergleichsweise ausgedrückt, müßten Sie sich sagen, das Ihr Gehirn einfriert. Und indem Sie diese Starrheit gewahr werden, würden Sie ungefähr eine Vorstellung haben von dem Be­wußtsein, das sich nicht mehr in der Zeit abschließt.",
      "Nun wird man, wenn man so weit gekommen ist, eine merkwürdige Abwechselung in dem ganzen Bilde gewahr. Es zeigt sich jetzt, daß aus der Starrheit, der Zeitlosigkeit, durch welche dieses unendliche  Meer des Mutes mit seinen Wesenheiten, die wir die Geister des Willens nen­nen, charakterisiert ist, Wesen anderer Hierarchien wie durchschlagen, wie hineinspielen. Erst in dem Moment, wo man dieses Nichtmehrvorhandensein der Zeit spürt, merkt man es, daß da andere Wesen hineinspielen. Man merkt nämlich ein unbestimmtes Erleben, von dem man nicht sagen kann, daß man es selbst erlebt, sondern daß es da ist, kann man nur sagen, daß es in dem ganzen unendlichen Meere des Mutes drinnen ist. Man merkt etwas wie ein durch dieses Feld gehendes Aufblitzen, wie ein Hellerwerden, aber nicht eigentliche Blitze, sondern mehr ein Aufglimmen; aber ein Aufglimmen, das nicht den Eindruck macht des aufglimmenden Lichtes, sondern - man muß ja bei diesen",
      "Dingen zu mancherlei greifen - wenn Sie es sich begreiflich machen wollen, so denken Sie sich folgendes. Sie treten einem Menschen gegen­über, der Ihnen etwas sagt, und Sie bekommen das Gefühl: Wie ist doch der klug! - und indem er weiterredet, steigert sich dieses Gefühl, und Sie empfinden: Der ist weise, hat Unendliches erlebt, daß er so weise Dinge sagen kann! - und diese Persönlichkeit wirkt außerdem so, daß Sie förmlich etwas wie einen Zauberhauch von ihr ausgehen fühlen. Denken Sie sich diesen Zauberhauch hoch gesteigert und in diesen hinein Wolken, die darinnen nicht aufblitzen, sondern glimmen. Wenn Sie das alles zusammennehmen, haben Sie eine Vorstellung davon, daß hineinspielen in die Hierarchie der Geister des Willens Wesenheiten, welche ganz Weisheit sind, aber eine solche Weisheit, die da hineinspielt strahlend, die nicht bloß Weisheit ist, sondern hinstrahlende Weisheit ist. Kurz, Sie bekommen hellseherisch wahrneh­mend die Vorstellung von dem, was die Cherubim sind. Die Cherubim spielen da hinein.",
      "Jetzt denken Sie sich gar nichts um sich als das, was ich eben be­schrieben habe. Ich sagte vorhin, indem ich darauf einen gewissen Wert legte: Man kann nicht sagen, man habe es um sich -, sondern man kann nur sagen, es ist eben da -, wie ich es jetzt beschrieben habe. Man muß sich da hineindenken. Und über die Vorstellung, daß etwa das eine da aufblitzt, sagte ich, es ist nicht ein Blitzen, sondern ein Glimmen, weil alles gleichzeitig ist. Es ist eben nicht etwa, daß eines entsteht und vergeht, sondern alles ist gleichzeitig. Aber man bekommt jetzt ein Gefühl von einer Beziehung dieser Geister des Willens und der Cherubim. Man bekommt das Gefühl, daß die ein Verhältnis zu­einander gewinnen. Dieses Bewußtsein erlangt man. Und zwar erlangt man das Bewußtsein, daß die Geister des Willens oder die Throne ihre eigene Wesenheit den Cherubim opfern. Das ist die letzte Vorstellung, zu der man überhaupt kommt, wenn man sich, rückwärtsgehend, dem Saturn nähert: die opfernden Geister des Willens, die ihre Opfer hin­auflenken zu den Cherubim. Da ist die Welt mit Brettern verschlagen. Und indem man erleben kann dieses Opfern der Geister des Willens gegenüber den Cherubim, preßt sich etwas los aus unserem Wesen. Das kann man jetzt nur mit dem Worte sagen: Durch das Opfer, das die",
      "Geister des Willens den Cherubim bringen, wird die Zeit geboren. - Aber die Zeit ist jetzt nicht jene abstrakte Zeit, von der wir gewöhn­lich sprechen, sondern sie ist selbständige Wesenheit. Jetzt kann man anfangen zu reden von etwas, was beginnt. Die Zeit beginnt mit dem, was da zunächst als Zeitwesenheiten geboren wird, die nichts sind als lauter Zeit. Es werden Wesenheiten geboren, die nur aus Zeit beste­hen; das sind die Geister der Persönlichkeit, die wir dann als Archai in der Hierarchie der geistigen Wesenheiten kennenlernen. Im Saturndasein sind sie nur Zeit. Bei uns haben wir sie auch beschrieben als Zeitgeister, als Geister, welche die Zeit regeln. Aber die da geboren werden als Geister, sind wirklich Wesenheiten, die überhaupt nur aus Zeit bestehen.",
      "Das ist etwas außerordentlich Wichtiges: teilzunehmen an diesem Opfer der Geister des Willens gegenüber den Cherubim und an der Geburt der Zeit. Denn erst jetzt, indem die Zeit geboren wird, tritt etwas anderes auf, was uns jetzt überhaupt erst möglich macht, von dem Saturnzustande als von etwas zu sprechen, was sozusagen einige Ähnlichkeit hat mit dem, was uns umgibt. Gleichsam der Opferrauch der Throne, der die Zeit gebiert, ist das, was wir die Wärme des Saturn nennen. Daher sagte ich früher immer, der Saturn ist im Wärmezustand, indem ich beschrieb, was da ist. Gegenüber all den Elementen, die wir gegenwärtig um uns haben, können wir bei dem alten Saturn-zustand nur sprechen als von einem Wärmezustand. Aber diese Wärme entsteht als Opferwärme, welche die Geister des Willens darbringen den Cherubim. Nun gibt uns das zugleich eine Anleitung, wie wir in Wahrheit über das Feuer denken sollen. Wo wir Feuer sehen, wo wir Wärme empfinden, sollten wir nicht so materialistisch denken, wie es dem heutigen Menschen natürlich und gewöhnlich ist, sondern wo wir Wärme auftreten sehen und fühlen, da ist das noch unsichtbar vor­handen, was dem Leben geistig zugrunde liegend ist: das Opfer von den Geistern des Willens gegenüber den Cherubim. Dadurch gewinnt die Welt erst ihre Wahrheit, daß wir wissen, daß hinter jeder Wärmeentwickelung ein Opfer ist.",
      "In der «Geheimwissenschaft» ist, um die Menschen draußen nicht gar zu sehr vor den Kopf zu stoßen, zunächst mehr der äußere Zustand",
      "des alten Saturn geschildert. Es sind ja schon genug dadurch vor den Kopf gestoßen, und die Menschen, die nur im heutigen wissen­schaftlichen Sinne denken können, sehen das Buch als reinen Unsinn an. Aber nun denken Sie sich, was es hieße, wenn man gar sagen würde: Der alte Saturn hat in seiner innersten Wesenheit, in dem, was ihm zugrunde liegt, das, daß die Wesenheiten, welche den Geistern des Willens angehören, den Cherubim opferten; daß in dem Opferrauch die Zeit geboren wird als das Opfer, welches sie den Cherubim brin­gen; daß daraus die Archai, die Zeitgeister, hervorgegangen sind und daß die äußere Wärme nur eine Maja ist gegenüber dem Opfer der Geister des Willens. Aber es ist so: Die äußere Wärme ist nur eine Maja, und wollen wir in Wahrheit sprechen, so müssen wir sagen:",
      "Überall, wo Wärme ist, haben wir in Wahrheit Opfer, Opfer der Throne gegenüber den Cherubim!",
      "Und nun ist eine gute Imagination dies: Es wird in «Wie erlangt man Erkenntnisse der höheren Welten?» sehr häufig davon gespro­chen, und auch sonst ist es gesagt worden, daß die zweite Stufe der rosenkreuzerischen Einweihung die Bildung von Imaginationen ist. Diese Imaginationen muß sich der Anthroposoph bilden aus den rich­tigen Vorstellungen gegenüber der Welt. So kann er sich, was wir heute besprochen haben, umgewandelt denken in eine phantasieartige Imagi­nation: die Throne, die Geister des Willens, kniend in voller Hinge­bung vor den Cherubim, aber so, daß die Hingebung nicht hervorgeht aus der Empfindung der Kleinheit, sondern aus dem Bewußtsein, daß man etwas hat, was man opfern kann! Die Throne in dieser Opfer­willigkeit, der die Stärke, der Mut zugrunde liegt, wie kniend vor den Cherubim und das Opfer zu ihnen hinaufschickend, und dieses Opfer schicken sie hinauf wie brodelnde Wärme, so daß der Opferrauch hinaufgeht zu den geflügelten Cherubim! So könnte das Bild sein. Und von diesem Opfer ausgehend - als wenn wir in die Luft hinein das Wort sprechen könnten und dies die Zeit wäre, was aber Wesen­heiten sind -, von dem ganzen Vorgange ausgehend: die Geister der Zeit, die Archai! Dieses Hinaussenden der Archai, das gibt ein gran­dioses, mächtiges Bild. Und dieses Bild, vor unsere Seele hingestellt, ist außerordentlich impressionierend für gewisse Imaginationen, die",
      "uns dann immer weiter und weiter auf dem Gebiete des okkulten Er­kennens bringen können.",
      "Das ist es ja überhaupt, was wir erreichen müssen: umzuwandeln die Vorstellungen, die wir bekommen, in Imaginationen, in Bilder. Wenn die Bilder auch von uns ungeschickt gemacht sind, wenn sie auch anthropomorphistisch sind, wenn sie auch ausschauen wie geflügelte Engel und so weiter, darauf kommt es nicht an. Das andere wird uns zuletzt schon gegeben, und was sie nicht haben sollen, fällt schon ab. Wenn wir uns diesen Bildern hingeben, dringen wir in das imaginative Vorstellen ein.",
      "Wenn Sie das nehmen, was ich jetzt versuchte zu charakterisieren, so werden Sie sehen, daß die Seele bald zu allerlei Bildern Zuflucht nehmen muß, die abliegen von den Verstandesbegriffen. Die Verstan­desbegriffe verdanken erst viel Späterem ihr Dasein, so daß wir solche Dinge zunächst nicht verstandesmäßig nehmen dürfen.",
      "Und Sie müs­sen es begreifen, was gemeint ist, wenn manche Geister so etwas schil­dern, und anders schildern als die Verstandesmenschen. Aber die Ver­standesmenschen können dann solche Geister auch nie verstehen.",
      "Wer sich davon unterrichten will, dem will ich eine Anleitung dafür geben. Nehmen Sie aus der Reclamschen Universal-Bibliothek das Buch, das ein gutes ist: den sogenannten «alten Schwegler>, den früher die Stu­denten gern benutzten vor dem Examen, der aber jetzt nicht mehr ver­wendbar ist, seitdem die Seele abgesetzt ist; wenn er auch durch einen Bearbeiter verschlimmbessert worden ist, so ist er doch nicht ganz entstellt worden.",
      "Also Sie können des alten Schweglers «Geschichte der Philosophie» nehmen, und Sie werden ein gutes Buch haben. Wenn Sie da nachlesen über die Hegelsche Philosophie, so finden Sie alles ausgezeichnet geschildert.",
      "Aber nun lesen Sie darin das kurze Kapitel gerade über Jakob Böhme, und versuchen Sie sich eine rechte Vorstel­lung davon zu machen, wie hilflos ein solcher Mensch, der eine Ver­standesphilosophie schreibt, gegenüber einem Geist wie Jakob Böhme ist! Paracelsus hat er, Gott sei Dank, ganz ausgelassen, denn da würde er ganz schlimme Sätze hingeschrieben haben.",
      "Aber lesen Sie, was dort über Jakob Böhme geschrieben ist. Da kommt Schwegler an einen Geist, dem naiv aufgegangen ist - jetzt nicht das Saturnbild, sondern",
      "die Wiederholung des Saturnbildes, denn das hat sich ja in der Erd­periode wiederholt; das kann er nicht anders, als mit Worten und Be­griffen schildern, an die der Verstand nicht heran kann. Da hört für den Verstandesmenschen jedes Begreifen auf. Nicht, als ob man nicht etwa die Dinge begreifen könnte, aber man kann sie nicht begreifen, wenn man auf dem Standpunkte des trockenen Philosophenverstandes bleiben will.",
      "Sie sehen, das ist gerade das Wichtige, daß wir uns erheben zu dem, wozu der gewöhnliche Intellekt nicht ausreicht. Wenn auch der ge­wöhnliche Verstand so etwas Ausgezeichnetes liefert wie die «Ge­schichte der Philosophie» von Schwegler - denn ich habe es absichtlich ein «gutes» Buch genannt -, so ist es doch ein Beispiel dafür, wie ein ausgezeichneter Verstand vollständig stillesteht vor einem Geist wie Jakob Böhme.",
      "So haben wir heute versucht, an der Hand der Betrachtung des alten Saturn, sozusagen mehr innerlich in diese alte planetarische Verkör­perung unserer Erde einzudringen. Wir werden es demnächst so ma­chen mit dem Sonnen- und Mondendasein und werden dabei sehen, wie wir auch dort zu Begriffen kommen, die uns vielleicht nicht weni­ger grandios vorkommen, als wenn wir uns zurückahnen zu dem alten Saturnzustand und in der Ahnung in uns auftreten die vor den Che­rubim opfernden Throne, welche die Wesen der Zeit schaffen als Re­sultate des Opfers. Denn die Zeit ist ein Ergebnis des Opfers, und sie entsteht zunächst als lebendige Zeit, als ein Geschöpf des Opfers. Dann werden wir sehen, wie alle diese Dinge auf der Sonne umgeän­dert werden und wie uns andere grandiose Vorgänge des Weltendaseins entgegentreten werden, wenn wir vom Saturn zur Sonne und dann zum Mondendasein übergehen werden."
    ],
    "sentences": [
      [
        "Wenn wir in den Betrachtungen, welche wir im vorigen Jahre in unse­ren Zweigabenden gepflogen haben, fortfahren wollen, so ist es not­wendig, daß wir uns noch einige andere Begriffe, Vorstellungen, Anschauungen aneignen, als die sind, von denen bisher gesprochen worden ist.",
        "Wir wissen, daß wir gar nicht auskommen konnten mit dem, was wir über die Evangelien und sonstige geistige Dokumente der Menschheit zu sagen haben, wenn wir nicht vorausgesetzt hätten jene Entwickelung unseres ganzen Weltsystems, die wir da bezeichnen als die Verkörperungen unseres Planeten selber durch das Saturndasein, durch das Sonnendasein, das Mondendasein, bis herauf zum gegenwär­tigen Erdendasein."
      ],
      [
        "Wer sich zurückerinnert, wie oft an diese Grundvor­stellungen angeknüpft werden mußte, der weiß, wie notwendig für alle okkulte Betrachtung der Menschheitsentwickelung diese Grundvorstel­lungen eben sind.",
        "Wenn Sie nun die Angaben sich einmal ansehen, welche zum Beispiel in der «Geheimwissenschaft im Umriß» gegeben sind über die Saturn-, Sonnen- und Mondentwickelung bis zur Erdentwickelung herein, so werden Sie sich gestehen, daß es sich dabei - und selbst, wenn es noch viel ausführlicher wäre, könnte es nicht anders sein - nur um eine Skizze handeln kann, nur um Angaben, die von einer ge­wissen Seite, von einem gewissen Gesichtspunkte aus, gemacht werden können."
      ],
      [
        "Denn wie das Erdendasein eine unendliche Fülle von Einzel­heiten bietet, so ist es ganz selbstverständlich, daß wir auch für das Saturn-, Sonnen- und Monddasein eine unendliche Reihe von Einzel­heiten zu verzeichnen haben, und daß immer nur eine ganz grobe Kohlezeichnung, eine Art Umriß, gegeben werden kann.",
        "Für uns ist aber eine Charakteristik der Evolution noch von einer anderen Seite aus notwendig."
      ],
      [
        "Wenn wir uns fragen: Woher stammen alle die Angaben, die da gemacht worden sind? - so wissen wir, daß sie von den sogenannten Eintragungen in die Akasha-Chronik stammen.",
        "Wir wissen, daß das, was einmal geschehen ist oder vorgeht im Verlaufe der Weltentwicke­lung, gewissermaßen zu lesen ist wie durch eine Eintragung in eine"
      ],
      [
        "feine geistige Substanz, in die Akasha-Substanz.",
        "Von allem, was sich abgespielt hat, gibt es eine solche Eintragung, aus welcher entnommen werden kann, wie die Dinge einmal waren.",
        "Nun werden wir natürlich annehmen können, daß, ebenso wie dem gewöhnlichen Blick, der irgend etwas von unserer physischen Welt überblickt, die Dinge, die in der Nähe sind, in ihren Einzelheiten mehr oder weniger klar und deut­lich, und je weiter sie entfernt sind, mehr oder weniger unklar erschei­nen, so werden auch die Dinge, die zeitlich in unserer Nähe sind, die der Erden- oder der Mondentwickelung angehören, sich genauer ange­ben lassen; wogegen die Dinge, die zeitlich weiter entfernt sind, un­deutlichere Umrisse bekommen, so zum Beispiel, wenn wir in das Saturn- oder Sonnendasein hellseherisch zurückblicken."
      ],
      [
        "Warum tun wir das überhaupt, daß wir einen gewissen Wert darauf legen, so weit hinter uns liegende Zeiträume zu verfolgen?",
        "Es könnte ja jemand sagen: Wozu bringen diese Anthroposophen allerlei so uralte Dinge heute noch zur Sprache?",
        "Man braucht sich doch in der Welt nicht um diese uralten Dinge zu kümmern, denn man hat doch genügend zu tun mit dem, was gegenwärtig vorgeht!"
      ],
      [
        "Es wäre sehr unrichtig, so zu sprechen.",
        "Denn, was einmal vorgegan­gen ist, das vollzieht sich heute noch fortwährend.",
        "Was in der Saturn­zeit sich abgespielt hat, das ist nicht bloß dazumal gewesen, sondern das geht heute noch vor, nur wird es überdeckt, unsichtbar gemacht durch das, was heute äußerlich um den Menschen auf dem physischen Plan ist.",
        "Und recht, recht stark unsichtbar wird gerade das alte Saturn­dasein gemacht, das vor so langer Zeit sich abgespielt hat.",
        "Aber es geht den Menschen noch etwas an, heute noch, das alte Saturndasein.",
        "Und um uns eine Vorstellung zu machen, wie es uns angeht, wollen wir uns folgendes vor die Seele stellen."
      ],
      [
        "Wir wissen, daß der innerste Kern unseres Wesens uns entgegentritt als das, was wir unser «Ich» nennen.",
        "Dieses Ich, der innerste Kern unseres Wesens, ist wahrhaftig für den heutigen Menschen eine recht übersinnliche, eine recht unwägbare Wesenheit.",
        "Wie unwägbar sie ist, kann schon daraus geschlossen werden, daß es heute Seelenlehren gibt, die sogenannten offiziellen Psychologien, die überhaupt keine Ahnung mehr davon haben, daß auf ein solches Ich hinzudeuten ist."
      ],
      [
        "Ich habe schon öfter darauf aufmerksam gemacht, daß sich nach und nach im 19.",
        "Jahrhundert in der deutschen Psychologie der schöne Ausdruck herausgebildet hat «Seelenlehre ohne Seele».",
        "Namentlich war tonangebend für diese «Seelenlehre ohne Seele» - obwohl das Wort nicht von ihr geprägt worden ist - die heute weltberühmte Schule Wundts' die ja nicht bloß in den deutschen Landen ausschlag­gebend ist, sondern die überall, wo von Psychologie geredet wird, mit großen Ehren genannt wird.",
        "«Seelenlehre ohne Seele» könnte man so ausdrücken: sie lehre, ohne auf ein selbständiges Seelenwesen Rück­sicht zu nehmen, daß sich alle Eigenschaften der Seele erst sammeln in einer Art von Brennpunkt, sich versammeln im Ich.",
        "Man kann sich einen größeren Unsinn gar nicht denken, dennoch steht die heutige Psychologie ganz unter dem Eindruck dieses Unsinns.",
        "Und diese «Seelenlehre ohne Seele» ist heute in der ganzen Welt berühmt.",
        "Künf­tige Kulturgeschichtsschreiber werden viel zu tun haben, wenn sie es unseren Nachkommen plausibel machen wollen, wie so etwas möglich war, daß im 19.",
        "Jahrhundert und weit ins 20. hinein so etwas als die größte Leistung auf psychologischem Gebiete angeschlagen worden ist.",
        "Das alles soll nur gesagt werden, um anzudeuten, wie unklar sich gerade die offizielle Psychologie über das ist, was wir als den Mittel­punkt des menschlichen Wesens bezeichnen."
      ],
      [
        "Wenn man das Ich klar erfassen und so vor sich hinstellen könnte wie den äußeren physischen Leib, und wenn man die Umgebung, von der das Ich so abhängt, wie der physische Leib von dem abhängt, was von außen durch die Augen gesehen, durch die Sinne sonst wahr­genommen werden kann, wenn man ebenso die Umgebung des Ich suchen könnte, wie man im physischen Reich die Umgebung in den Wolken, Bergen und so weiter hat, oder wie zum Beispiel der physische Leib abhängt von seinen Nahrungsmitteln, so käme man zu einer Weltcharakteristik, zu einem Weltentableau, heute noch, in dem, gleichsam imprägniert, unsere sonstige Umgebung enthalten ist, un­sichtbar drinnensteckt, und das gleich ist dem Weltentableau des alten Saturn.",
        "Das heißt, wer das Ich in seiner Welt kennenlernen will, der muß sich eine solche Welt vor Augen stellen können, wie der alte Saturn war.",
        "Diese Welt ist verdeckt, ist eine übersinnliche Welt für"
      ],
      [
        "den Menschen.",
        "Der Mensch könnte sie auch in dem heutigen Grade sei­ner Entwickelung durchaus nicht ertragen.",
        "Sie ist ihm durch den Hüter der Schwelle zugedeckt, damit sie vor ihm verborgen bleibe, und es gehört ein gewisser Grad spiritueller Entwickelung dazu, um einen solchen Anblick aushalten zu können."
      ],
      [
        "Es ist ja in der Tat ein Anblick, an den man sich erst gewöhnen muß.",
        "Sie müssen sich vor allen Dingen von alledem eine Vorstellung ma­chen, was notwendig ist, um überhaupt dahin zu kommen, ein solches Weltentableau als etwas Wirkliches noch empfinden zu können."
      ],
      [
        "Alles, was Sie mit den Sinnen wahrnehmen können, müßten Sie sich wegden­ken, müßten sich auch fortdenken Ihre Innenwelt, insofern dieselbe aus den gewöhnlichen Gemütsbewegungen besteht.",
        "Der Mensch müßte sich weiter wegdenken von dem, was in der Welt ist, auch alles, was er an Vorstellungen in sich hat."
      ],
      [
        "Also von der Außenwelt müßten Sie alles wegnehmen, was Sinne wahrnehmen können, und vom Inneren alles, was Gemütsbewegungen, Vorstellungen sind.",
        "Und wenn Sie jetzt von jener Seelenverfassung sich einen Begriff machen wollen, in die der Mensch kommen muß, wenn er den Gedanken real faßt: Alles das wäre weggeschafft, aber der Mensch wäre noch da -, dann kann man nicht anders sagen als, der Mensch muß lernen, Schauder, Furcht emp­finden zu können vor der unendlichen Leere, die sich da auftut um uns herum."
      ],
      [
        "Man muß gleichsam seine Umgebung empfinden können wie ganz und gar gesättigt, tingiert mit dem, was uns von allen Seiten Schauder, Furcht erregt, und muß zu gleicher Zeit in der Lage sein, diese Furcht durch innere Festigkeit und Sicherheit seines Wesens über­winden zu können.",
        "Ohne diese zwei Gemütsstimmungeu, Schauder und Furcht vor der unendlichen Leere des Daseins und der Überwin­dung dieser Furcht, kann man überhaupt gar keine Ahnung empfin­den von dem, was unserem Weltendasein als das alte Saturndasein zugrunde liegt."
      ],
      [
        "Beide Empfindungen, wie sie jetzt charakterisiert worden sind, kul­tivieren ja die Menschen wenig bei sich selber.",
        "Daher findet man sogar in der Literatur wenig Beschreibungen von diesem Zustand.",
        "Es kennen diesen Zustand natürlich die, welche durch hellseherische Kräfte den Dingen auf den Grund zu gehen versuchen im Laufe der Zeit.",
        "Aber in"
      ],
      [
        "der äußeren Literatur, der geschriebenen oder gedruckten, finden sich nur wenig Angaben darüber, daß Menschen so etwas empfunden ha­ben wie das Schaudern vor der unendlichen Leere oder gar die Über­windung dieses Schauderns.",
        "Um eine Art äußeren Einblick in die Sache zu haben, versuchte ich ein wenig nachzugehen in der jüngeren Literatur, wo so etwas auftreten könnte wie dieses Schaudern vor der unermeßlichen Leere in einem Menschen."
      ],
      [
        "Die Philosophen sind ja ge­wöhnlich ungeheuer klug, reden in ihren Begriffen abgeklärt und ver­meiden es, von den großen, imponierenden Eindrücken zu sprechen.",
        "Dort findet man nicht so leicht etwas darüber."
      ],
      [
        "Nun will ich nicht davon sprechen, wo ich überall nichts gefunden habe.",
        "Aber einmal habe ich doch einen kleinen Anklang an diese Empfindungen gefun­den, und zwar in dem Tagebuch des Hegelianers Karl Rosenkranz, wo er manchmal intime Gefühle schildert, wie er sie gehabt hat beim Durchleben der Hegelschen Philosophie."
      ],
      [
        "Ich habe auf eine merkwür­dige Stelle stoßen können, die bei ihm so herauskommt wie eine un­schuldige Stelle, die er in sein Tagebuch fixierte.",
        "Karl Rosenkranz macht sich klar, daß die Hegelsche Philosophie ausgeht von dem «reinen Sein»."
      ],
      [
        "Von diesem « reinen Sein» Hegels ist viel geschwatzt worden in der philosophischen Literatur des 19.",
        "Jahrhunderts, aber man muß sagen, es ist wenig verstanden worden.",
        "Man möchte fast sa­gen, in der Philosophie der zweiten Hälfte des 19."
      ],
      [
        "Jahrhunderts - das kann man natürlich nur im intimsten Kreise sagen! - versteht man von dem «reinen Sein» Hegels soviel wie der Ochs vom Sonntag, wenn er die ganze Woche hindurch Gras gefressen hat.",
        "Es ist ein durchgesiebter Begriff, dieses «reine Sein» Hegels - nicht das Seiende, sondern das Sein -, es ist ein Begriff, der wahrhaftig noch nicht das ist, was ich jetzt charakterisiert habe als die schauervolle, Furcht einflößende Leere, aber es ist der ganze Raum im Hegelschen Sein tingiert mit der Eigenschaft, die nichts hat, was vom Menschen erlebt werden kann:"
      ],
      [
        "die Unendlichkeit, mit Sein erfüllt.",
        "Und Karl Rosenkranz empfindet es einmal wie ein schauervolles Durchschütteltsein von einer Kälte, die mit nichts tingiert ist als mit dem Sein."
      ],
      [
        "Um zu begreifen, was der Welt zugrunde liegt, genügt es nicht, daß man in Begriffen darüber redet, sich Begriffe, Ideen davon macht;"
      ],
      [
        "sondern es ist viel notwendiger, daß man sich eine Vorstellung hervor­rufen kann von dem Empfinden, das entsteht gegenüber der unend­lichen Leere des alten Saturndaseins.",
        "Das Gemüt ergreift dann, wenn es nur eine Ahnung davon erhält, das Gefühl des Schauderns.",
        "Wenn man hellseherisch aufsteigen will, damit man dann zum Schauen dieses Saturnzustandes kommt, muß man sich in der Weise vorbereiten, in­dem man sich in der Tat ein Gefühl erwirbt, das in gewisser Beziehung ausgeht von dem jedem Menschen mehr oder weniger bekannten Ge­fühl des Schwindelns auf hohem Berge, wenn der Mensch über einem Abgrunde steht und keinen sicheren Boden unter den Füßen zu haben glaubt; ein Gefühl, daß er an keinem Orte verbleiben könnte, so daß er sich übergeben wollte an Mächte, an Kräfte, über die er keine Macht mehr hat.",
        "Das ist aber erst das Elementare dieses zu ahnenden Gefüh­les.",
        "Denn man verliert nicht nur den Boden unter den Füßen, sondern auch das, was Augen sehen, Ohren hören, Hände greifen können, über­haupt das, was in der räumlichen Umgebung ist; und es kann nicht anders sein, als daß man jeden Gedanken verliert, daß man in eine Art von Dämmerung oder Schlafzustand verfällt, in dem man auch zu keiner Erkenntnis kommen kann.",
        "Oder aber man lebt sich hinein in jene Empfindung, und dann gibt es nichts anderes, als daß man zu jenem Schauerzustande kommt, und oft ist es eine Art von Schwindel-zustand, der nicht besiegt werden kann."
      ],
      [
        "Nun gibt es zwei Möglichkeiten für den heutigen Menschen.",
        "Die eine sichere Möglichkeit ist die, daß jemand die Evangelien verstanden hat, das Mysterium von Golgatha verstanden hat.",
        "Wer sie wirklich in ihrer vollen Tiefe verstanden hat - natürlich nicht so, wie die moder­nen Theologen heute darüber reden, sondern so, daß er daraus heraus-gesogen hat das Tiefste, was der Mensch daraus innerlich erfahren kann -, der nimmt etwas mit in jene Leere hinein, das sich wie von einem Punkte aus vergrößert und die Leere ausfüllt mit etwas, was mutähnlich ist, was ein Gefühl von Mut, von Geborgensein ist durch das Vereintsein mit jener Wesenheit, die auf Golgatha das Opfer voll­bracht hat.",
        "Der andere Weg ist der, daß wir ohne die Evangelien ein­dringen in die geistigen Welten, daß wir durch wahre, echte Theoso­phie in die geistigen Welten eindringen.",
        "Das kann auch geschehen."
      ],
      [
        "wissen, daß wir zunächst immer betonen: wir gehen nicht von den Evangelien aus, wenn wir das Mysterium von Golgatha betrachten, sondern wir kämen dazu auch, wenn es gar keine Evangelien gäbe.",
        "Das hat, bevor das Mysterium von Golgatha geschehen ist, nicht sein können; das ist aber heute der Fall, weil etwas in die Welt gekommen ist durch das Mysterium von Golgatha, wodurch der Mensch die gei­stige Welt unmittelbar aus den Impressionen heraus selber begreifen kann."
      ],
      [
        "Das ist das, was wir das Walten des Heiligen Geistes in der Welt nennen können, das Walten der Weltgedanken in der Welt.",
        "Wenn wir eines oder das andere mitnehmen, können wir uns nicht verlieren und können nicht sozusagen abstürzen in den unendlichen Abgrund, wenn wir der schauervollen Leere zunächst gegenüberstehen."
      ],
      [
        "Wenn wir uns nun dieser schauervollen Leere nähern mit den anderen Vorbereitun­gen, welche uns durch die verschiedenen Mittel gegeben sind, wie es zum Beispiel in «Wie erlangt man Erkenntnisse der höheren Welten?» ausgeführt ist und in dem, was sich weiter darauf aufbaut, und ein­dringen in eine Welt, die herausgeboren ist aus dem, was unser Gemüt erschüttern, was unsere Vorstellungen erfassen kann, wenn wir uns einleben in diese Welt, dann lernen wir, indem wir uns sozusagen einstellen auf das Saturndasein, zunächst Wesenheiten kennen - jetzt aber nicht etwas, was ähnlich schaut dem Tierreich, Pflanzenreich oder Mineralreich, sondern Wesenheiten; es ist ja eine Welt, in der keine Wolken sind, auch kein Licht ist, in der es auch ganz tonlos ist -, aber wir lernen kennen Wesenheiten, und zwar jene Wesenheiten lernen wir kennen, die in unserer Terminologie genannt werden die Geister des Willens oder die Throne.",
        "Diese Geister des Willens lernen wir gerade so kennen, daß es wie eine richtige Gegenständlichkeit für uns wird, man könnte sagen: ein wogendes Meer des Mutes."
      ],
      [
        "Was sich der Mensch zunächst nur vorstellen kann, das wird hell­seherisch Gegenwart.",
        "Denken Sie sich getaucht in das Meer, aber jetzt getaucht als geistiges Wesen, welches sich eins fühlt mit der Christus­-Wesenheit, getragen von der Christus-Wesenheit, schwimmend, aber jetzt nicht in einem Meere von Wasser, sondern in einem den unend­lichen Raum erfüllenden Meere von - es gibt keine andere Bezeich­nung dafür - flutendem Mute, flutender Energie!",
        "Das ist nicht etwa"
      ],
      [
        "bloß ein gleichgültiges, undifferenziertes Meer, sondern alle Möglich­keiten und Unterschiedlichkeiten dessen, was man bezeichnen kann mit dem Gefühl des Mutes, tritt uns da entgegen.",
        "Wir lernen kennen Wesenheiten, die zwar aus Mut bestehen, die wir aber, wenn sie auch nur aus Mut bestehen, sehr wohl als konkrete Wesenheiten treffen.",
        "Es erscheint natürlich ganz sonderbar, wenn man sagt, man treffe Wesen­heiten, die ebenso real sind wie der Mensch aus Fleisch, und die nicht aus Fleisch, sondern aus Mut bestehen.",
        "Aber es ist so.",
        "Als solche Wesen­heiten treffen wir die Geister des Willens, und zunächst bezeichnen wir nur das als Saturndasein, was die Geister des Willens, die aus Mut bestehen, darstellen, nichts sonst.",
        "Das ist zunächst Saturn.",
        "Das ist eine Welt, von der wir nicht sagen könnten, sie sei eine Welt, die kugelför­mig, sechseckig oder viereckig ist.",
        "Alle diese Bestimmungen des Rau­mes passen nicht darauf, denn es gibt dort nicht die Möglichkeit, ein Ende zu finden.",
        "Wenn wir noch einmal das Bild vom Schwimmen ge­brauchen wollen, so können wir sagen: es ist nicht ein Meer, wo man an eine Oberfläche kommen würde, sondern nach allen Seiten findet man immer Geister des Mutes oder des Willens."
      ],
      [
        "Ich werde in späteren Vorträgen charakterisieren, wie man nicht gleich auf einmal zu dieser Sache kommt, ich will jetzt nur dieselbe Ordnung einhalten wie früher: Saturn, Sonne, Mond, denn es ist viel besser, wenn man die umgekehrte Richtung einhält: von der Erde zum Saturn.",
        "Jetzt charakterisiere ich umgekehrt, das macht aber nichts."
      ],
      [
        "Wenn man sich bis zu diesem Anschauen erhoben hat, tritt eines ein, was für den ungeheuer schwer ist, sich vorzustellen, der sich nicht be­müht, langsam und allmählich zu solchen Vorstellungen zu kommen.",
        "Denn es hört etwas auf, was mit dem gewöhnlichen menschlichen Vor­stellen so verquickt ist wie nur irgend etwas: der Raum hört auf!",
        "Es hat keinen Sinn mehr, zu sagen, man schwimme oben oder unten, vorn oder hinten, rechts oder links.",
        "Es ist überall gleich in dieser Be­ziehung.",
        "Aber das Wichtige ist: wenn man in die ersten Zeiten des Saturndaseins kommt, so hört auch die Zeit auf!",
        "Es gibt kein Früher oder Später mehr.",
        "Das ist natürlich für den Menschen heute sehr schwer vorzustellen, weil sein Vorstellen selbst in der Zeit verfließt:"
      ],
      [
        "ein Gedanke ist vor oder nach dem anderen.",
        "Daß die Zeit aufhört, das"
      ],
      [
        "ist nun wieder nur durch ein Gefühl zu charakterisieren.",
        "Dieses Gefühl ist wahrhaftig nicht angenehm. - Denken Sie sich einmal Ihre Vorstel­lungen erstarrt, indem alles, woran Sie sich erinnern können und was Sie sich vornehmen, wie zu einem starren Stabe erstarrt, so daß Sie sich festgehalten fühlen in Ihrem Vorstellen und sich nicht mehr rühren können.",
        "Dann werden Sie nicht mehr sagen können, Sie haben etwas, was Sie früher erlebt haben, «früher» erlebt.",
        "Sie sind angebun­den daran, es ist da, aber es ist erstarrt.",
        "Die Zeit hört auf, eine Bedeu­tung zu haben.",
        "Sie ist überhaupt nicht mehr da.",
        "Deshalb ist es auch ziemlich unsinnig, wenn man fragt: Du schilderst da das Saturndasein, das Sonnendasein und so weiter, sage doch, was vor dem Saturndasein war!",
        "«Vorher» hat da keinen Sinn mehr, weil die Zeit aufhört, so daß man auch aufhören muß mit allen Zeitbestimmungen.",
        "Es ist wirklich beim alten Saturndasein - in einem sehr vergleichsweisen Sinn kann man das sagen - die Welt wie mit Brettern verschlagen, indem man mit dem Gedanken stillestehen muß.",
        "Mit dem Hellsehen auch.",
        "Die gewöhnlichen Gedanken muß man schon lange zurücklassen, die gehen nicht bis dahin.",
        "Bildlich, vergleichsweise ausgedrückt, müßten Sie sich sagen, das Ihr Gehirn einfriert.",
        "Und indem Sie diese Starrheit gewahr werden, würden Sie ungefähr eine Vorstellung haben von dem Be­wußtsein, das sich nicht mehr in der Zeit abschließt."
      ],
      [
        "Nun wird man, wenn man so weit gekommen ist, eine merkwürdige Abwechselung in dem ganzen Bilde gewahr.",
        "Es zeigt sich jetzt, daß aus der Starrheit, der Zeitlosigkeit, durch welche dieses unendliche Meer des Mutes mit seinen Wesenheiten, die wir die Geister des Willens nen­nen, charakterisiert ist, Wesen anderer Hierarchien wie durchschlagen, wie hineinspielen.",
        "Erst in dem Moment, wo man dieses Nichtmehrvorhandensein der Zeit spürt, merkt man es, daß da andere Wesen hineinspielen.",
        "Man merkt nämlich ein unbestimmtes Erleben, von dem man nicht sagen kann, daß man es selbst erlebt, sondern daß es da ist, kann man nur sagen, daß es in dem ganzen unendlichen Meere des Mutes drinnen ist.",
        "Man merkt etwas wie ein durch dieses Feld gehendes Aufblitzen, wie ein Hellerwerden, aber nicht eigentliche Blitze, sondern mehr ein Aufglimmen; aber ein Aufglimmen, das nicht den Eindruck macht des aufglimmenden Lichtes, sondern - man muß ja bei diesen"
      ],
      [
        "Dingen zu mancherlei greifen - wenn Sie es sich begreiflich machen wollen, so denken Sie sich folgendes.",
        "Sie treten einem Menschen gegen­über, der Ihnen etwas sagt, und Sie bekommen das Gefühl: Wie ist doch der klug! - und indem er weiterredet, steigert sich dieses Gefühl, und Sie empfinden: Der ist weise, hat Unendliches erlebt, daß er so weise Dinge sagen kann! - und diese Persönlichkeit wirkt außerdem so, daß Sie förmlich etwas wie einen Zauberhauch von ihr ausgehen fühlen.",
        "Denken Sie sich diesen Zauberhauch hoch gesteigert und in diesen hinein Wolken, die darinnen nicht aufblitzen, sondern glimmen.",
        "Wenn Sie das alles zusammennehmen, haben Sie eine Vorstellung davon, daß hineinspielen in die Hierarchie der Geister des Willens Wesenheiten, welche ganz Weisheit sind, aber eine solche Weisheit, die da hineinspielt strahlend, die nicht bloß Weisheit ist, sondern hinstrahlende Weisheit ist.",
        "Kurz, Sie bekommen hellseherisch wahrneh­mend die Vorstellung von dem, was die Cherubim sind.",
        "Die Cherubim spielen da hinein."
      ],
      [
        "Jetzt denken Sie sich gar nichts um sich als das, was ich eben be­schrieben habe.",
        "Ich sagte vorhin, indem ich darauf einen gewissen Wert legte: Man kann nicht sagen, man habe es um sich -, sondern man kann nur sagen, es ist eben da -, wie ich es jetzt beschrieben habe.",
        "Man muß sich da hineindenken.",
        "Und über die Vorstellung, daß etwa das eine da aufblitzt, sagte ich, es ist nicht ein Blitzen, sondern ein Glimmen, weil alles gleichzeitig ist.",
        "Es ist eben nicht etwa, daß eines entsteht und vergeht, sondern alles ist gleichzeitig.",
        "Aber man bekommt jetzt ein Gefühl von einer Beziehung dieser Geister des Willens und der Cherubim.",
        "Man bekommt das Gefühl, daß die ein Verhältnis zu­einander gewinnen.",
        "Dieses Bewußtsein erlangt man.",
        "Und zwar erlangt man das Bewußtsein, daß die Geister des Willens oder die Throne ihre eigene Wesenheit den Cherubim opfern.",
        "Das ist die letzte Vorstellung, zu der man überhaupt kommt, wenn man sich, rückwärtsgehend, dem Saturn nähert: die opfernden Geister des Willens, die ihre Opfer hin­auflenken zu den Cherubim.",
        "Da ist die Welt mit Brettern verschlagen.",
        "Und indem man erleben kann dieses Opfern der Geister des Willens gegenüber den Cherubim, preßt sich etwas los aus unserem Wesen.",
        "Das kann man jetzt nur mit dem Worte sagen: Durch das Opfer, das die"
      ],
      [
        "Geister des Willens den Cherubim bringen, wird die Zeit geboren. - Aber die Zeit ist jetzt nicht jene abstrakte Zeit, von der wir gewöhn­lich sprechen, sondern sie ist selbständige Wesenheit.",
        "Jetzt kann man anfangen zu reden von etwas, was beginnt.",
        "Die Zeit beginnt mit dem, was da zunächst als Zeitwesenheiten geboren wird, die nichts sind als lauter Zeit.",
        "Es werden Wesenheiten geboren, die nur aus Zeit beste­hen; das sind die Geister der Persönlichkeit, die wir dann als Archai in der Hierarchie der geistigen Wesenheiten kennenlernen.",
        "Im Saturndasein sind sie nur Zeit.",
        "Bei uns haben wir sie auch beschrieben als Zeitgeister, als Geister, welche die Zeit regeln.",
        "Aber die da geboren werden als Geister, sind wirklich Wesenheiten, die überhaupt nur aus Zeit bestehen."
      ],
      [
        "Das ist etwas außerordentlich Wichtiges: teilzunehmen an diesem Opfer der Geister des Willens gegenüber den Cherubim und an der Geburt der Zeit.",
        "Denn erst jetzt, indem die Zeit geboren wird, tritt etwas anderes auf, was uns jetzt überhaupt erst möglich macht, von dem Saturnzustande als von etwas zu sprechen, was sozusagen einige Ähnlichkeit hat mit dem, was uns umgibt.",
        "Gleichsam der Opferrauch der Throne, der die Zeit gebiert, ist das, was wir die Wärme des Saturn nennen.",
        "Daher sagte ich früher immer, der Saturn ist im Wärmezustand, indem ich beschrieb, was da ist.",
        "Gegenüber all den Elementen, die wir gegenwärtig um uns haben, können wir bei dem alten Saturn-zustand nur sprechen als von einem Wärmezustand.",
        "Aber diese Wärme entsteht als Opferwärme, welche die Geister des Willens darbringen den Cherubim.",
        "Nun gibt uns das zugleich eine Anleitung, wie wir in Wahrheit über das Feuer denken sollen.",
        "Wo wir Feuer sehen, wo wir Wärme empfinden, sollten wir nicht so materialistisch denken, wie es dem heutigen Menschen natürlich und gewöhnlich ist, sondern wo wir Wärme auftreten sehen und fühlen, da ist das noch unsichtbar vor­handen, was dem Leben geistig zugrunde liegend ist: das Opfer von den Geistern des Willens gegenüber den Cherubim.",
        "Dadurch gewinnt die Welt erst ihre Wahrheit, daß wir wissen, daß hinter jeder Wärmeentwickelung ein Opfer ist."
      ],
      [
        "In der «Geheimwissenschaft» ist, um die Menschen draußen nicht gar zu sehr vor den Kopf zu stoßen, zunächst mehr der äußere Zustand"
      ],
      [
        "des alten Saturn geschildert.",
        "Es sind ja schon genug dadurch vor den Kopf gestoßen, und die Menschen, die nur im heutigen wissen­schaftlichen Sinne denken können, sehen das Buch als reinen Unsinn an.",
        "Aber nun denken Sie sich, was es hieße, wenn man gar sagen würde: Der alte Saturn hat in seiner innersten Wesenheit, in dem, was ihm zugrunde liegt, das, daß die Wesenheiten, welche den Geistern des Willens angehören, den Cherubim opferten; daß in dem Opferrauch die Zeit geboren wird als das Opfer, welches sie den Cherubim brin­gen; daß daraus die Archai, die Zeitgeister, hervorgegangen sind und daß die äußere Wärme nur eine Maja ist gegenüber dem Opfer der Geister des Willens.",
        "Aber es ist so: Die äußere Wärme ist nur eine Maja, und wollen wir in Wahrheit sprechen, so müssen wir sagen:"
      ],
      [
        "Überall, wo Wärme ist, haben wir in Wahrheit Opfer, Opfer der Throne gegenüber den Cherubim!"
      ],
      [
        "Und nun ist eine gute Imagination dies: Es wird in «Wie erlangt man Erkenntnisse der höheren Welten?» sehr häufig davon gespro­chen, und auch sonst ist es gesagt worden, daß die zweite Stufe der rosenkreuzerischen Einweihung die Bildung von Imaginationen ist.",
        "Diese Imaginationen muß sich der Anthroposoph bilden aus den rich­tigen Vorstellungen gegenüber der Welt.",
        "So kann er sich, was wir heute besprochen haben, umgewandelt denken in eine phantasieartige Imagi­nation: die Throne, die Geister des Willens, kniend in voller Hinge­bung vor den Cherubim, aber so, daß die Hingebung nicht hervorgeht aus der Empfindung der Kleinheit, sondern aus dem Bewußtsein, daß man etwas hat, was man opfern kann!",
        "Die Throne in dieser Opfer­willigkeit, der die Stärke, der Mut zugrunde liegt, wie kniend vor den Cherubim und das Opfer zu ihnen hinaufschickend, und dieses Opfer schicken sie hinauf wie brodelnde Wärme, so daß der Opferrauch hinaufgeht zu den geflügelten Cherubim!",
        "So könnte das Bild sein.",
        "Und von diesem Opfer ausgehend - als wenn wir in die Luft hinein das Wort sprechen könnten und dies die Zeit wäre, was aber Wesen­heiten sind -, von dem ganzen Vorgange ausgehend: die Geister der Zeit, die Archai!",
        "Dieses Hinaussenden der Archai, das gibt ein gran­dioses, mächtiges Bild.",
        "Und dieses Bild, vor unsere Seele hingestellt, ist außerordentlich impressionierend für gewisse Imaginationen, die"
      ],
      [
        "uns dann immer weiter und weiter auf dem Gebiete des okkulten Er­kennens bringen können."
      ],
      [
        "Das ist es ja überhaupt, was wir erreichen müssen: umzuwandeln die Vorstellungen, die wir bekommen, in Imaginationen, in Bilder.",
        "Wenn die Bilder auch von uns ungeschickt gemacht sind, wenn sie auch anthropomorphistisch sind, wenn sie auch ausschauen wie geflügelte Engel und so weiter, darauf kommt es nicht an.",
        "Das andere wird uns zuletzt schon gegeben, und was sie nicht haben sollen, fällt schon ab.",
        "Wenn wir uns diesen Bildern hingeben, dringen wir in das imaginative Vorstellen ein."
      ],
      [
        "Wenn Sie das nehmen, was ich jetzt versuchte zu charakterisieren, so werden Sie sehen, daß die Seele bald zu allerlei Bildern Zuflucht nehmen muß, die abliegen von den Verstandesbegriffen.",
        "Die Verstan­desbegriffe verdanken erst viel Späterem ihr Dasein, so daß wir solche Dinge zunächst nicht verstandesmäßig nehmen dürfen."
      ],
      [
        "Und Sie müs­sen es begreifen, was gemeint ist, wenn manche Geister so etwas schil­dern, und anders schildern als die Verstandesmenschen.",
        "Aber die Ver­standesmenschen können dann solche Geister auch nie verstehen."
      ],
      [
        "Wer sich davon unterrichten will, dem will ich eine Anleitung dafür geben.",
        "Nehmen Sie aus der Reclamschen Universal-Bibliothek das Buch, das ein gutes ist: den sogenannten «alten Schwegler>, den früher die Stu­denten gern benutzten vor dem Examen, der aber jetzt nicht mehr ver­wendbar ist, seitdem die Seele abgesetzt ist; wenn er auch durch einen Bearbeiter verschlimmbessert worden ist, so ist er doch nicht ganz entstellt worden."
      ],
      [
        "Also Sie können des alten Schweglers «Geschichte der Philosophie» nehmen, und Sie werden ein gutes Buch haben.",
        "Wenn Sie da nachlesen über die Hegelsche Philosophie, so finden Sie alles ausgezeichnet geschildert."
      ],
      [
        "Aber nun lesen Sie darin das kurze Kapitel gerade über Jakob Böhme, und versuchen Sie sich eine rechte Vorstel­lung davon zu machen, wie hilflos ein solcher Mensch, der eine Ver­standesphilosophie schreibt, gegenüber einem Geist wie Jakob Böhme ist!",
        "Paracelsus hat er, Gott sei Dank, ganz ausgelassen, denn da würde er ganz schlimme Sätze hingeschrieben haben."
      ],
      [
        "Aber lesen Sie, was dort über Jakob Böhme geschrieben ist.",
        "Da kommt Schwegler an einen Geist, dem naiv aufgegangen ist - jetzt nicht das Saturnbild, sondern"
      ],
      [
        "die Wiederholung des Saturnbildes, denn das hat sich ja in der Erd­periode wiederholt; das kann er nicht anders, als mit Worten und Be­griffen schildern, an die der Verstand nicht heran kann.",
        "Da hört für den Verstandesmenschen jedes Begreifen auf.",
        "Nicht, als ob man nicht etwa die Dinge begreifen könnte, aber man kann sie nicht begreifen, wenn man auf dem Standpunkte des trockenen Philosophenverstandes bleiben will."
      ],
      [
        "Sie sehen, das ist gerade das Wichtige, daß wir uns erheben zu dem, wozu der gewöhnliche Intellekt nicht ausreicht.",
        "Wenn auch der ge­wöhnliche Verstand so etwas Ausgezeichnetes liefert wie die «Ge­schichte der Philosophie» von Schwegler - denn ich habe es absichtlich ein «gutes» Buch genannt -, so ist es doch ein Beispiel dafür, wie ein ausgezeichneter Verstand vollständig stillesteht vor einem Geist wie Jakob Böhme."
      ],
      [
        "So haben wir heute versucht, an der Hand der Betrachtung des alten Saturn, sozusagen mehr innerlich in diese alte planetarische Verkör­perung unserer Erde einzudringen.",
        "Wir werden es demnächst so ma­chen mit dem Sonnen- und Mondendasein und werden dabei sehen, wie wir auch dort zu Begriffen kommen, die uns vielleicht nicht weni­ger grandios vorkommen, als wenn wir uns zurückahnen zu dem alten Saturnzustand und in der Ahnung in uns auftreten die vor den Che­rubim opfernden Throne, welche die Wesen der Zeit schaffen als Re­sultate des Opfers.",
        "Denn die Zeit ist ein Ergebnis des Opfers, und sie entsteht zunächst als lebendige Zeit, als ein Geschöpf des Opfers.",
        "Dann werden wir sehen, wie alle diese Dinge auf der Sonne umgeän­dert werden und wie uns andere grandiose Vorgänge des Weltendaseins entgegentreten werden, wenn wir vom Saturn zur Sonne und dann zum Mondendasein übergehen werden."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG Berlin, 7. November 1911",
    "paragraphs": [
      "Aus unseren letzten Auseinandersetzungen werden Sie entnommen haben, daß die Beschreibung jener früheren Zustände unserer Ent­wickelung, die noch vor der Entstehung unserer Erde selbst liegen, außerordentlich schwierig ist. Denn wir haben gesehen, daß wir uns die Begriffe und Ideen erst heranbilden müssen, durch die wir zu sol­chen fremdartigen, fernen Zuständen unserer Weltentwickelung kom­men können.",
      "Ich habe schon darauf aufmerksam gemacht, daß eine solche Beschreibung, wie sie in meiner «Geheimwissenschaft im Um­riß» von der alten Saturnzeit und auch von den folgenden planeta­rischen Verkörperungen unserer Erde gegeben wird, nicht nur keine erschöpfende ist, sondern sich in gewissem Sinne damit begnügen muß - damit die Öffentlichkeit, der auch dieses Buch übergeben wer­den sollte, nicht zu stark schockiert wird -, dasjenige, worauf es eigent­lich ankommt, in Bilder zu kleiden, die von Naheliegendem und auch von Gewohntem hergenommen sind. Man gibt damit natürlich nicht eine unrichtige Beschreibung, aber in gewissem Sinne doch eine solche, die sehr bildhaft in Maja, in die Illusion getaucht ist, und man muß sich erst durch die Illusion hindurcharbeiten, um immer mehr und mehr in die Wahrheit der Sache eindringen zu können.",
      "So ist zum Bei­spiel die alte Saturnzeit so beschrieben - wie es innerhalb gewisser Grenzen durchaus richtig ist -, daß gesagt wird, der alte Saturn sei ein Himmelskörper gewesen, der im wesentlichen nicht aus den Bestand­teilen bestanden hat, die wir als Erde, Wasser oder Luft kennen, son­dern nur aus Wärme. Und wenn von «Raum» gesprochen wird, so ist das nur eine bildhafte Beschreibung, denn wir haben das letzte Mal gesehen, daß es auf dem alten Saturn nicht einmal eine «Zeit» gegeben hat.",
      "Wenn wir also von Raum sprechen, so ist das auch ein Bildhaftes. Raum gab es auf dem alten Saturn auch nicht in unserem Sinne; und die Zeit entsteht erst auf dem Saturn. Wir sind durchaus, wenn wir uns auf den alten Saturn zurückversetzen, in dem Be-reich der raumlosen Ewigkeit.",
      "Wenn also etwas gesagt wird, was",
      "uns ein Bild geben kann, so müssen wir uns klar sein, daß es ein Bild ist.",
      "Wenn wir den Raum des alten Saturn betreten hätten, so würden wir nicht einmal eine so feine Substanz gefunden haben, die wir als «Gas» hätten bezeichnen können, sondern nur Wärme und Kälte. In Wirklichkeit ist es so, daß man von dem Kommen aus einem Raumteil in einen anderen nicht sprechen kann, sondern daß man nur die Emp­findung von dem Ablauf von wärmeren und kälteren Zuständen ge­brauchen könnte, so daß also auch der Hellseher, wenn er sich in die alte Saturnzeit zurückversetzt, den Eindruck empfängt eines auf und ab flutenden raumlosen Wärmezustandes.",
      "Aber das ist nur der äußere Schleier des Saturnzustandes Denn diese Wärme oder dieses Feuer, wie man im Okkultismus sagt, hat sich uns ja enthüllt in seinen gei­stigen Untergründen; und wir haben gesehen, daß geistige Taten, gei­stige Verrichtungen in Wahrheit das waren, was auf dem alten Saturn wirklich vorhanden war. Und wir haben uns ein Bild gemacht von dem, was da an geistigen Taten auf dem Saturn vorhanden war.",
      "Wir haben gesagt, daß die Geister des Willens oder die Throne Opfertaten verrichtet haben, so daß, wenn wir zurückschauen auf das, was kon­kret auf dem Saturn geschah, wir die Cherubim haben und die von den Thronen fließenden Opfer. Opfer fließen von den Thronen zu den Cherubim, und diese Taten des Opfers sind es, die, gleichsam von außen angeschaut, als Wärme erscheinen.",
      "Wärmezustände sind der äußere physische Ausdruck, überhaupt der äußere sinnliche Ausdruck für Opfer. Und in der ganzen Welt, wo wir Wärme wahrnehmen, ist Wärme der äußere Ausdruck für das, was hinter der Wärme ist.",
      "Wärmezustände sind die Opfertaten von Wesenheiten. Wenn wir daher die Wärme in Wahrheit charakterisieren wollen, werden wir sagen mussen: Die Weltenwärme ist die Offenbarung des Welten-opfers oder der Weltenopfertaten.",
      "Dann haben wir gesehen, daß aus dieser Tat des Opfers, das die Throne gegenüber den Cherubim darbringen, gleichsam herausgeboren wird - aber ich habe schon darauf aufmerksam gemacht, daß es wie­der ein modernes Wort ist, das nicht recht paßt -, das, was wir die «Zeit» nennen. Aber die Zeit ist damals noch nicht jenes Abstraktum,",
      "als welches sie heute der Mensch wahrnimmt, sondern eine Summe von geistigen Wesenheiten: das sind die Geister der Persönlichkeit, die wir dann auch kennengelernt haben als die Zeitgeister. Die Zeitgeister sind die wirkliche alte Zeit, und sie sind die Kinder der Throne mit den Cherubim.",
      "Aber die Verhältnisse, durch welche die Wesen des Zeitlichen auf dem alten Saturn entstehen, sind Opfer. Wenn gesagt wird: Der alte Saturn besteht in Wärme -, so müssen wir uns, um ein eigentliches Verständnis dafür zu gewinnen, was dahinter liegt, nicht bloß äußere physische Begriffe aneignen - denn «Warme» ist ein phy­sischer Begriff -, sondern Begriffe, die wir nur aus dem Seelenleben selber gewinnen können, aus dem moralischen, weisheitsvollen Seelenleben.",
      "Niemand kann wissen, was Wärme ist, der nicht in der Lage ist, sich eine Vorstellung zu machen von dem, was heißt, opferfähige Hingabe dessen, was man besitzt, was man hat, ja nicht nur opferfähige Hingabe dessen, was man hat, sondern dessen, was man selber ist. Die Hinopferung des eigenen Wesens, das Sich-Ent­äußern des eigenen Wesens seelisch gefaßt, so daß man es sich zugleich so denkt, daß man bereit ist, sein Bestes hinzugeben zum Heile der Welt; nicht für sich sein Bestes behalten, sondern es gern hinopfern zu wollen auf dem Altar des Weltalls: das als einen lebendigen Begriff gefaßt, als unsere Seele durchdringend, führt allmählich zum Ver­ständnisse dessen, was hinter der Erscheinung der Wärme ist.",
      "Man vergegenwärtige sich einmal, was im modernen Leben auch heute mit dem Begriff des Opfers verknüpft ist: man kann sich nicht recht den­ken, daß der, welcher mit Verständnis opfert, dies jemals tut gegen seinen Willen. Wenn jemand opfert gegen seinen Willen, so müßte er dazu aus irgendeinem Grunde gezwungen sein; es müßte ein Zwang walten.",
      "Dann aber würden wir es nicht mit dem zu tun haben, was hier gemeint ist. Hier ist aber gemeint, was als Opfer selbstverständ­lich fließt aus dem Wesen, das opfert. Und wenn jemand etwas opfert, nicht weil er aus irgendeinem äußeren Grunde dazu gedrängt wird, auch nicht, weil er hofft, etwas zu erringen, sondern weil er sich aus seinem Inneren heraus gedrängt fühlt zu opfern, dann ist es undenk­bar, daß er etwas anderes empfindet als innere Wärmeseligkeit.",
      "Füh­len wir uns durchglutet mit innerer Wärmeseligkeit, dann haben wir",
      "schon das ausgesprochen, was wir nicht anders bezeichnen können als:",
      "der Opfernde fühlt sich durchwärmt, durchglutet mit der Seligkeit. Da haben wir die Möglichkeit, selbst zu empfinden, wie die Opferglut uns in der äußeren Weltenwärme entgegentreten kann. Nur der ver­steht wirklich, was Wärme ist, der den Gedanken fassen kann: Wenn Wärme in der Welt auftritt, liegt zugrunde in irgendeiner Weise ein Seelisch-Geistiges, das hinter der Wärme ist und das die Wärme be­wirkt durch die Seligkeit des Opfers. Wer so die Wärme empfinden kann, der kommt allmählich zu der Realität, welche sich hinter der Wärmeerscheinung, hinter der Wärmeillusion verbirgt.",
      "Wenn wir nun weiterdringen wollen von dem alten Saturndasein zum alten Sonnendasein, so müssen wir uns erst wieder einen Begriff zurechtlegen, durch den wir von der Substanz der alten Sonne, nicht der jetzigen Sonne, eine Vorstellung bilden können. Denn, was wir in der «Geheimwissenschaft» lesen: «Die alte Sonne hat die Wärme heraufgebildet, indem sie hinzugefügt hat zu der Wärme Luft und Licht», das ist wieder nur durch eine äußere Erscheinung dargestellt. Wie wir hinter der Wärme suchen müssen die Opferglut der Geister des Willens, so müssen wir hinter der Luft und dem Licht etwas Mora­lisches suchen, wenn wir Luft und Licht, die auf der Sonne zu der Wärme hinzukommen, verstehen wollen. Nun können wir nur eine Empfindung davon bekommen, was die Substanz der alten Sonne war, wenn wir uns an etwas halten, was wir in uns selbst geistig-seelisch erleben können.",
      "Da gibt es ein Erlebnis, das wir in folgender Weise als ein Seelen-erlebnis beschreiben können. Denken wir uns, daß irgendein Mensch sehen würde eine richtige, echte Opfertat, oder daß er sich vorstellen würde, wie wir es das letzte Mal bei der Betrachtung des alten Saturn-daseins als Opfertat der Throne geschildert haben, die Throne hinauf­sendend ihre Opfer zu den Cherubim, so daß der Mensch angeregt würde durch das Bild des beseligenden Opfers, das er anschaut und das die Seele lebendig machen würde. Was würde unsere Seele fühlen entweder durch den Anblick des opfernden Wesens selbst oder durch das Bild, das wir in unserer Seele recht lebendig machen? - Ein solcher Mensch würde, wenn er lebendige Gefühle hat, wenn er nicht mehr",
      "oder weniger gefühllos der Opferseligkeit gegenüberstehen würde, eine tiefgehende Seligkeit empfinden müssen beim Anblick des Opferbildes; er würde in seiner Seele empfinden müssen: das ist die schönste Tat, das schönste Erlebnis, das überhaupt aus unserer Seele hervorgerufen werden kann, Opferseligkeit anzuschauen! Das ist aber auch eine solche Empfindung: man müßte ein Stück Holz sein, wenn nicht da in der Seele der Trieb entstehen würde, mit höchster Ehrfurcht anzu­schauen, was Opferseligkeit ist, wenn man nicht davon lernen könnte die Stimmung der völligen Hingabe. Opfertat ist aktive, in Aktivität sich umsetzende Hingebung. Die Anschauung von dem aktiven, dem tätigen Hingeben kann die Stimmung des Hingegebenseins, des Sich­Verlierens, des Sich-Vergessens in der Anschauung hervorrufen. Den­ken wir uns diese Stimmung des selbstlosen Sich-Verlierens in der An­schauung ganz in der Seele ausgegossen, dann haben wir mit dieser Stimmung dasjenige, was insofern uns näher kommen soll für unser Verständnis, als wir ohne eine solche Stimmung, wenigstens ohne eine Ahnung und einen Anklang an eine solche Stimmung, in Wahrheit niemals zu dem kommen könnten, was die höhere Erkenntnis gibt.",
      "Wer niemals solche Stimmung des Hingegebenseins haben kann, der kann nicht zu höheren Erkenntnissen kommen. Denn, was wäre das Gegenteil dieser Stimmung? Es wäre der Eigenwille, Geltendma­chung des Eigenwillens. Das sind überhaupt wie zwei Pole des Weltgeschehens: hingegebene Verlorenheit an das, was man anschaut, und eigenwillige Geltendmachung dessen, was in einem ist. Das sind zwei große Gegensätze. Für ein Sich-Durchdringen mit Weisheit ist Eigenwille tötend. Im gewöhnlichen Leben kennt man Eigenwillen nur als Vorurteil, und Vorurteile zerstören immer höhere Einsicht.",
      "Was hier als Hingegebensein gemeint ist, muß man sich aber gestei­gert denken, denn nur durch dies gesteigerte Hingegebensein kann der Mensch sich zu höheren Welten hinaufarbeiten. Da muß er jenes Sich-Verlieren wenigstens als Stimmung erleben können. Daher muß es immer wieder und wieder betont werden, daß wir nie zu einer höheren Erkenntnis kommen, wenn wir so arbeiten wie die gewöhnliche Wis­senschaft oder das alltägliche Denken. Seien wir uns klar: wie die gewöhnliche Wissenschaft und das alltägliche Denken arbeiten, so arbeiten",
      "sie aus dem gewöhnlichen Willen des Menschen heraus durch alles dasjenige, was den Eigenwillen geschaffen hat: durch die vererb­ten oder anerzogenen Empfindungen und Gefühle. Darüber kann man sich sehr täuschen.",
      "Es kommen zum Beispiel Leute und sagen: Da soll man aufnehmen irgendeine Wissenschaft, wie sie geboten wird in der Geisteswissenschaft, aber ich will nichts aufnehmen, als was dem ent­spricht, was ich mir schon denken kann, ich will nichts ungeprüft aufnehmen! - Gewiß, ungeprüft soll man nichts aufnehmen. Aber da­mit kommt man auch keinen Schritt weiter, daß man nur Geprüftes aufnimmt.",
      "Und der, welcher Hellseher werden will, wird nie sagen, daß er nur das aufnehmen will, was er vorher geprüft hat, sondern er muß vollständig frei werden von allem Eigensüchtigen und muß alles erwarten von dem, was aus der Welt an ihn herantritt, und was man nicht anders bezeichnen kann als mit dem Worte «Gnade». Er erwar­tet alles von der Gnade, die erleuchtet.",
      "Denn wie erwirbt man hell­seherische Erkenntnisse? Nur dadurch, daß man alles ausschalten kann, was man jemals gelernt hat. Gewöhnlich denkt der Mensch: Ich habe mein eigenes Urteil. Er müßte sich aber sagen: Das besteht nur daraus, daß du auffrischst, was deine Vorfahren gedacht haben, oder was deine Triebe anregen und so weiter.",
      "Denn davon ist nie die Rede, daß dies der Menschen eigene Urteile sind; und die ihre eigenen Urteile am meisten geltend machen, wissen gar nicht, wie sie am Gängelbande ihrer Vorurteile geführt werden. Das muß alles fort, wenn man zu höheren Erkenntnissen kommen will.",
      "Leer muß die Seele werden und ruhig warten können auf das, was sich aus der raum- und zeitfreien, ding- und tatsachenfreien, verborgenen, geheimen Welt an die Seele heranbegeben kann. Und nie müssen wir glauben, daß wir an uns heranreißen können, was hellseherische Erkenntnis ist, sondern nur, daß wir eine Stimmung schaffen, durch die wir entgegennehmen, was sich uns darbietet als Offenbarung oder Erleuchtung.",
      "So daß wir nie anders als von der Gnade, die an uns herantritt und uns etwas gibt, das erwarten können, was an uns herantreten soll.",
      "Wie also offenbart sich eine solche Erkenntnis? Wie offenbart sich das, was da herantritt, wenn wir uns genügend vorbereitet haben? Es offenbart sich als die Stimmung des Begnadetwerdens durch die uns",
      "entgegenkommende Gabe aus der geistigen Welt. Wenn wir das, was an uns herantritt, um uns gnadenvoll entgegenzukommen und in uns die Erkenntnis einzugießen, bezeichnen wollten, so könnten wir nur den Ausdruck gebrauchen: es ist das, was uns da entgegentritt, ein Gnadewirkendes, ein Schenkendes, ein Gebendes.",
      "Fassen wir die Natur eines Wesens, dessen Hauptcharakterzug in dem bestehen würde, was ich jetzt eben mit diesen Worten bezeichnet habe: es ist ein Schenken-des, ein Gebendes, ein Darbietendes; ein solches Wesen, mit dem Hauptcharakterzug des Gnade-um-sich-Streuens, des Gnade-von-sich-Ausgießens - fassen wir es so, daß es, um in diese Möglichkeit des Gnadegebens zu kommen, brauchte den Anblick des Opfers der Throne an die Cherubim! Denken wir uns einmal, es würde hinzutre­ten zu dem, was da geschieht, wenn die Throne den Cherubim opfern, ein Wesen, welches durch diesen Anblick veranlaßt würde zu einem Schenkenden, zu einem seine Gaben in Gnade um sich Ergießenden zu werden!",
      "Stellen wir uns das ganz genau vor. Denken wir uns, wir würden eine Rose anschauen und entzückt werden davon, also das Gefühl eines Beseligenden empfinden über das, was wir «schön» nen­nen! Denken wir, ein anderes Wesen würde durch den Anblick dessen, was beschrieben ist als das Opfer der Throne an die Cherubim, ver­anlaßt werden, alles, was es hat, um sich herum zu schenken, schen­kend in die Welt zu ergießen: dann würden wir damit diejenigen We­senheiten beschrieben haben, von denen in der «Geheimwissenschaft» die Rede ist als den Geistern der Weisheit, die auf der Sonne hinzu­treten zu denjenigen Wesenheiten, die wir schon auf dem Saturn kennengelernt haben.",
      "Würden wir also die Frage aufwerfen: Welches ist der Charakter der Geister, die auf der Sonne auftraten und zu den Saturngeistern hinzutraten? - so müßten wir antworten: Diese Geister haben als ihren Hauptcharakterzug die schenkende, gnadewirkende, gebende Tugend. - Und wollten wir ein Beiwort haben, so müßten wir sagen: Sie sind die Geister der Weisheit, die großen Schenkenden, die großen Gebenden des Weltalls! - Wie wir von den Thronen gesagt haben: Die großen Opferer -, so müßten wir von den Geistern der Weisheit sagen: Die großen Gebenden, die ihre Gabe so Hingebenden, daß dieselbe von ihnen aus das Weltall durchwebt und durchlebt, indem",
      "sie einströmt in das Weltall und in dasselbe erst Ordnung hinein­schafft.",
      "Das ist die Wirkung der Geister der Weisheit auf der Sonne. Das tun sie: schenken ihr eigenes Wesen an ihre Umgebung. Und was ist das, was sich dem äußeren Anblick darbietet, wenn man so hinblickt und wie eine höhere Sinnesempfindung wahrnehmen will, was da auf der Sonne geschieht?",
      "Wenn man es ansieht, ist es so, wie es beschrieben ist in der «Ge­heimwissenschaft»: Die Sonne besteht außer aus Wärme auch noch aus Luft und Licht. Aber wenn man das sagt: Die Sonne besteht außer aus Wärme auch noch aus Luft und Licht -, dann ist es so, wie wenn jemand sagte: In der Ferne sehe ich eine graue Wolke -, und würde er als Maler den Eindruck, den er hat, hinmalen, so würde er eine solche graue Wolke malen, wenn er aber näher hinzuginge, würde er vielleicht statt der grauen Wolke einen Mückenschwarm vor sich haben.",
      "In Wirklichkeit ist dann das, was er für eine graue Wolke hielt, eine Summe von lauter lebendigen Wesen. In ähnlicher Weise stehen wir von ferne dem alten Sonnendasein gegenüber: Indem wir es von ferne anschauen, erscheint es als die Illusion eines Luft- und Lichtkörpers, wenn wir es aber näher betrachten, haben wir nicht mehr einen Luft- und Lichtkörper, sondern da erscheint es als die große schenkende Tugend der Geister der Weisheit!",
      "Und niemand lernt die Luft richtig kennen, der sie nur ihren äußeren physischen Eigenschaften nach be­schreibt. Das ist nur Maja oder Illusion, das ist nur die äußere Offen­barung. Denn überall wo Luft ist in der Welt, sind die Taten der Gei­ster der Weisheit dahinter.",
      "Webende, wirkende Luft heißt Offen­barung der schenkenden Tugend des Makrokosmos. Und nur der sieht die Luft richtig an, der sich sagt: Ich nehme hier Luft wahr, in Wahrheit aber wird da geschenkt von den Geistern der Weisheit an die Umgebung, wird etwas ausgestrahlt an die Umgebung.",
      "Jetzt wissen wir, was es eigentlich ist, was wir von der alten Sonne beschrieben haben, indem wir sagten, sie besteht aus Luft. Wir wissen jetzt, daß es Schenken ist: daß die Geister der Weisheit ihr eigenes Wesen ausfließen lassen und daß es äußerlich als Luft erscheint. Aber eine merkwürdige Sache trat nuii ein, die sich dem Hellseher darbietet.",
      "Wir müssen uns klarmachen, wie wir von dieser schenkenden Tugend eine noch genauere Vorstellung bekommen können aus unserem Seelen­leben heraus. Vergegenwärtigen wir uns dazu jenes Gefühl, das wir selbst haben können, wenn es uns gelingt, aus der eben geschilderten Stimmung von Hingabe uns zu durchdringen mit einer Erkenntnis, mit einer Idee. Von einer solchen Idee haben wir dann immer eine be­stimmte Empfindung. Die beste Empfindung einer solchen Idee hat man noch, wenn man das Künstlerische ins Auge faßt, wo die Idee den Drang hat, zum Beispiel Farbe oder Form irgendwie zu bemei­stern, also in der Welt auszuströmen, so daß sie ein selbständiges Da­sein der Welt geschenkt hat. Das Wesen einer solchen schenkenden Fähigkeit ist damit zu charakterisieren, daß man sagt: Produktivität, Schöpferisches ist damit verbunden, denn dieses Schenken ist selbst schöpferisch. Wer eine Idee hat, von der er empfindet, daß sie der Welt zum Heile gereichen kann und die sich darstellt in Kunstwerken und so weiter, der hat von dieser Produktivität der schenkenden Tu­gend einen richtigen Begriff, das ist es, was als Luft die Sonne durchwebt. Wenn wir uns denken die schaffende Idee im Kopfe des Künst­lers, wie sie sich einfügt in den Stoff - von allem anderen abgesehen -, dann ist dies das geistige Wesen der Luft. Wo Luft ist, haben wir es mit so etwas zu tun. Aber dadurch, daß diese lebendige Produktivität auf der Sonne da war, stellte sich die folgende Tatsache heraus.",
      "Halten wir fest, daß auf dem alten Saturn schon die Geister der Zeit geboren waren, daß also auf der Sonne «Zeit» schon sein konnte, denn diese ist herübergekommen von dem Saturn. Also es gibt jene Möglichkeit auf der alten Sonne, die es auf dem alten Saturn noch nicht gegeben hätte, daß ein solches Schenken eintrat. Denn denken Sie einmal, was es wäre mit einem Schenken, wenn es keine Zeit gäbe: da könnte man nicht schenken; denn Schenken besteht im Geben und im Entgegennehmen. Ohne das zweite ist das Schenken gar nicht zu denken. Also es muß das Schenken aus zwei Akten bestehen: aus Geben und Nehmen, sonst hat das Schenken keinen Zweck. Auf der Sonne stehen sich aber Geben und Nehmen ganz sonderbar gegenüber, so nämlich, daß, weil nun schon die Zeit da ist, die Gabe, die dar­gereicht wird auf der alten Sonne an die Umgebung, in der Zeit aufbewahrt",
      "wird, gleichsam bewahrt wird in der Zeit, so daß die Geister der Weisheit ihr Geschenktes ausgießen, dann bleibt es. Aber nun muß etwas eintreten, was das nimmt. Das arbeitet im Verhältnis zu den Gei­stern der Weisheit in einem späteren Augenblick. So daß die Geister der Weisheit im früheren Augenblicke geben, und das, was notwendig damit verbunden sein muß als Nehmen, tritt im späteren Augen­blicke ein.",
      "Davon können wir nur eine richtige Vorstellung bekommen, wenn wir wieder das eigene Seelenerleben zugrunde legen. Stellen Sie sich vor, Sie bemühen sich, irgend etwas zu verstehen, oder irgendeinen Gedanken zu bilden.",
      "Jetzt haben Sie diesen Gedanken gebildet. Mor­gen besinnen Sie sich, machen rein Ihren Geist, damit alles, was Sie gestern an Gedanken gebildet haben, zurückkommen kann in Ihren Geist. Dann ist das, was gestern gebildet worden ist, von Ihnen heute aufgenommen.",
      "So ist es auf der alten Sonne, indem das, was früher geschenkt wird, bewahrt bleibt für einen späteren Augenblick und später entgegengenommen wird. Was ist denn dann dieses Entgegen­nehmen? Es ist eine Tat, ein Geschehen, das sich nur dadurch von dem anderen Geschehen unterscheidet, daß es später ist.",
      "Das Geben kommt den Geistern der Weisheit zu. Wer nimmt denn nun? Damit jemand nehmen kann, muß erst jemand da sein. In derselben Art wie gleich­sam durch einen Geburtsakt, nämlich aus den Opfern der Throne an die Cherubim, die Geister der Zeit auf dem Saturn entstehen, so ent­stehen durch Schenken an die Welt von seiten der Geister der Weisheit auf der Sonne diejenigen Geister, die wir die Erzengel nennen: Ar­changeloi.",
      "Und sie sind auf der alten Sonne die Nehmenden. Aber sie nehmen auf eine ganz besondere Weise, so nämlich, daß sie, was sie als Gabe erhalten von den Geistern der Weisheit, nicht für sich behalten, sondern es zurückstrahlen, wie der Spiegel Ihr Bild zurückstrahlt.",
      "So haben die Erzengel auf der Sonne die Aufgabe, dasjenige, was in einem früheren Zeitpunkt geschenkt worden ist, in einem späteren Zeit­punkte aufzufangen, so daß es in einem späteren Zeitpunkte noch da ist und widergestrahlt wird durch die Erzengel. Wir haben also auf der Sonne ein älteres Geben und ein späteres Nehmen, aber dieses Nehmen als Widerstrahlung einer früheren Zeit.",
      "Sie könnten sich denken, daß die Erde nicht so wäre, wie sie jetzt ist, sondern daß folgendes eintreten würde: daß in dem jetzigen Zeit­punkt widerstrahlen könnte, was in einem früheren Zeitpunkt gesche­hen ist. Nun wissen wir aber, daß so etwas wirklich geschieht.",
      "Wir leben jetzt im fünften nachatlantischen Kulturzeitraum; da strahlen wider die Ereignisse des dritten nachatlantischen Kulturzeitraumes, der alten ägyptisch-chaldäischen Zeit. Was früher da war, wird auf­gefangen und strahlt jetzt zurück.",
      "Alles, was früher da war, wieder­holt sich. So haben wir uns gegenüber den Geistern der Weisheit, die in den älteren Sonnenzeiten die Gebenden, Schenkenden sind, in den Erzengeln die Aufnehmenden zu denken.",
      "Dadurch wird etwas ganz Besonderes hervorgerufen, was Sie sich nur richtig vorstellen können, wenn Sie sich denken das Bild einer innerlich geschlossenen Kugel, wo vom Mittelpunkte etwas ausgestrahlt wird, was geschenkt wird; das strahlt bis zur Peripherie hin und strahlt von dort zurück zum Mittel­punkte. Wir haben uns also von einem Zentrum ausgehend zu denken das, was von den Geistern der Weisheit kommt: das wird ausgestrahlt nach allen Seiten, wird aufgefangen von den Erzengeln und zurück­gestrahlt.",
      "Was da zurückstrahlt in den Raum hinein, ist das Geschenk der Geister der Weisheit. Und was da die Ausstrahlung der Geister der Weisheit zurückleitet, das ist das Licht, und damit sind die Erz­engel zugleich die Schöpfer des Lichtes.",
      "Licht ist ebensowenig das, als was es uns in der äußeren Illusion erscheint, sondern wo Licht auftritt, haben wir die zurückgestrahlten Gaben der Geister der Weisheit. Und die Wesen, die wir überall hinter dem Licht vermuten müssen, das sind die Erzengel.",
      "Daher müssen wir sagen: Trifft uns ein Licht, so stecken dahinter die Archangeloi; daß sie uns aber Licht zuströmen können, das kommt nur davon her, daß sie zurückstrahlen, was ihnen entgegenstrahlt, nämlich die schenkende Tugend der Geister der Weisheit.",
      "So bekommen wir ein Bild der alten Sonne. Wir denken uns einen Zentralsitz, wo vereinigt ist das, was vom alten Saturn herübergekom­men ist: die Opfertaten der Throne gegenüber den Cherubim, im Anblick dieser Opfertaten versunken die Geister der Weisheit. Durch den Anblick dieser Opfertaten werden sie veranlaßt, von sich auszustrahlen,",
      "was ihr eigenes Wesen ist: strömende, flutende Weisheit als schenkende Tugend. Das aber wird, weil es zeitdurchstrahlt ist, aus­gesandt und wieder zurückgesandt, so daß wir einen Globus, einen durch die zurückstrahlende Tugend innerlich erleuchteten Globus haben. Denn wir müssen uns die alte Sonne nicht nach außen, sondern nach innen leuchtend denken. Damit ist ein Neues geschaffen, das wir fo]gendermaßen beschreiben können. Denken wir uns diese Geister der Weisheit, sitzend im Mittelpunkte der Sonne, im Anblick der opfernden Throne versunken und ausstrahlend, was ihr eigenes Wesen ist, wegen des Anblickes der opfernden Throne, und zurück erhalten sie ihr ausstrahlendes Wesen, indem es ihnen von der Ober­fläche zurückstrahlt, so daß sie es als Licht wieder zurückbekommen. Alles ist durchleuchtet. Aber was bekommen sie zurück? Ihr eigenes Wesen wurde, indem sie es hingegeben haben, zum Geschenk an den Makrokosmos, da war es ihr Inneres. Jetzt strahlt es zurück: ihr eige­nes Wesen tritt ihnen von außen entgegen. Sie sehen ihr eigenes Inneres in die Welt verteilt und widergestrahlt von außen als Licht, als die Widerspiegelung ihres eigenen Wesens.",
      "Inneres und Äußeres sind die zwei Gegensätze, die uns jetzt ent­gegentreten. Das Frühere und Spätere verwandelt sich und wird so, daß es sich verwandelt in Inneres und Äußeres. Der «Raum» ist gebo­ren! Durch die schenkende Tugend der Geister der Weisheit entsteht der Raum auf der alten Sonne. Vorher kann «Raum» nur eine bild­liche Bedeutung haben. Jetzt haben wir den Raum, aber zunächst nur in zwei Dimensionen: noch nicht oben und unten, noch nicht rechts und links, sondern nur Außeres und Inneres. - In Wirklichkeit treten diese beiden Gegensätze schon am Ende des alten Saturn auf, aber sie wiederholen sich als raumschaffend auf der alten Sonne. Und wenn wir jetzt von all diesen Vorgängen wieder eine Vorstellung gewinnen wollen in der Weise, wie wir es das letzte Mal getan haben, wo das Bild der opfernden Throne vor unsere Seele trat, die Zeitgeister gebä­rend, so werden wir nicht hinmalen einen Körper, der aus Licht be­steht, denn Licht ist nur im Widerstrahlen im Inneren vorhanden. Sondern eine Kugel als inneren Raum haben wir uns zu denken, in dem Mittelpunkt zunächst sich wiederholend das Bild des Saturn: die",
      "Throne als Geister wie kniend vor den Cherubim, den geflügelten Wesen, opfernd ihr eigenes Wesen; und hinzukommend die Geister der Weisheit, in dem Anblick des Opfers versinkend. Und nun kann man als Anblick haben, daß die Glut, die im Opfer liegt, sich verwandelt so, daß sie sinnenfällig vorzustellen ist als Opferrauch, als Luft, die aufsteigt von der Opfertat als Opferrauch.",
      "Und wir bekommen ein vollständiges Bild, wenn wir uns vorstellen: Die opfernden Throne kniend vor den Cherubim, und zu dem Opfer hinzukommend wie im Reigen die Geister der Weisheit, hingegeben in ihrer Stimmung dem, was sie erblicken im Mittelpunkte der Sonne an dem Opfer der Throne; dadurch in ihrer Stimmung erwachsend zu dem Bilde des Opferrau­ches, der sich verbreitet nach allen Seiten, der ausströmt, sich am Ende ballt und aus seinen Wolken herausschafft die Gestalten der Erzengel, die zurückstrahlen von der Peripherie den Opferrauch als Licht, das Innere der Sonne durchleuchtend, das Geschenk der Geister der Weis­heit zurückgebend und die Sphäre der Sonne in dieser Weise schaffend. Sie besteht schenkend aus Glut und Opferrauch.",
      "An der äußeren Peripherie sitzen die Erzengel, die Schöpfer des Lichtes, die das, was zuerst auf der Sonne da ist, später abbilden; dann aber kommt es zu­rück als Licht. Was bewahren also die Erzengel? Sie bewahren das Frühere.",
      "Die Gaben, die sie nehmen, strahlen sie zurück. Was im An­fange war, strahlen sie dar in einer späteren Zeit. Und indem sie es zurückstrahlen, sind sie die Engel des Anfanges, weil sie das in späte­ren Zeiten wirksam machen, was früher war.",
      "Archangeloi, Boten des Anfanges sind sie!",
      "Es ist ganz wunderbar, wenn aus der wirklichen okkulten Erkennt­nis heraus ein solches Wort wieder auftaucht und wir uns dann über­legen, wie dieses Wort aus uralten Traditionen - auf dem Wege über die Schule Dionysius des Areopagiten, der ein Schüler des Paulus war - uns überkommt. Es ist wunderbar zu sehen, daß dieses Wort so geprägt ist, daß, wenn wir es unabhängig von dem, was da steht, wie­der entwickeln, das entsteht, was da war. Und wir fühlen uns dann verbunden mit den alten heiligen Schulen der Weiheweisheit, der Weihewissenschaft, so daß wir gleichsam fühlen, wie wenn dieses Alte in uns einströmen würde, indem wir es verständnisvoll ergreifen,",
      "nachdem wir uns selbst die Möglichkeit geschaffen haben, es unab­hängig von dem Alten aufzunehmen. Wer nur ein wenig fühlen kann das Stimmen der alten Ausdrücke, die uns überliefert sind, ohne daß wir auf diese Ausdrücke Rücksicht nehmen, der fühlt sich hinein­gestellt in das Walten der Zeitengeister durch den Menschen hindurch. Es ist etwas Wunderbares verbunden mit der ganzen menschlichen Evolution, was da herauskommt; es ist ein Sicher-Fühlen bei diesen Dingen.",
      "Das Andenken an die Urbeginne bewahren die Erzengel. Was aber auf irgendeinem Planeten vorhanden war, das wiederholt sich in einer späteren Zeit, nur daß das Spätere immer anderes noch hinzufügt, so daß uns das Wesen der Sonne wieder entgegentritt in dem, was uns auf unserer Erde entgegentritt.",
      "Die ganze Vorstellung, die ganze Empfindung, die wir uns hier aneignen konnten, die uns ein Bild gibt von den opfernden Thronen, von den opferempfangenden Cherubim, von der Glut, die aus dem Opfer ausströmt, von dem Opferrauch, der sich luftartig verbreitet, von dem Licht, das zurückgestrahlt wird von den Erzengeln, die das bewahren, was in den Anfängen geschehen ist, für die späteren Zeiten:",
      "diese Empfindung ist etwas, was in uns hervorrufen kann ein richtiges Verständnis alles dessen, was zusammenhängt mit den Schöpfungen einer solchen Empfindung, mit Opfern, die aus einer solchen Empfin­dung hervorgehen.",
      "So haben wir an diesem Milieu, das ich eben als Seelenmilieu ge­schildert habe, mehr geistig aufgefaßt, was wir früher an einem mehr physischen Bilde gewonnen haben. Und wir werden nun sehen, daß aus diesem Milieu geboren wird, was auf der Erde als Christus-Wesen­heit aufgetreten ist; und wir werden nur verstehen, was auf die Erde durch die Christus-Wesenheit gebracht wird, wenn wir uns aneignen den Begriff der schenkenden Tugend, der gnadewirkenden Tugend in ihrer Zurückstrahlung in dem Lichte des Weltenalls in der inneren Substanz des Sonnenmäßigen, die durchdrungen und durchleuchtet ist von diesem Licht. Wenn wir dies zum Bilde erheben, was wir eben beschrieben haben, und in eine Imagination umwandeln und uns den­ken, daß von alledem, was von diesem Wesen mitgebracht wird auf",
      "die Erde, sich etwas auf der Erde auslebt, dann werden wir das eigent­liche geistige Wesen des Christus-Impulses daraus noch wieder tiefer beschreiben können. Wir werden dann verstehen, welche dunkle Ah­nung in der Menschenseele leben kann, wenn diese Menschenseele gegenüber irgendeiner Darstellung empfindet, daß das, was eben be­schrieben worden ist, in einer gewissen Weise wieder lebendig werden kann auf der Erde.",
      "Denken wir uns einmal, es könnte das, was eben von der Sonne beschrieben worden ist, in eines Wesens Seele ganz und gar sich kon­zentrieren, könnte sich zusammendrehen und mitgenommen werden, um später wieder zu erscheinen. Und es würde wieder erscheinen und so wirken, daß es aus dem, was aus der uralten Opfertat und dem Opferrauch, der lichtschaffenden Zeit und der schenkenden Tugend geschaffen ist, den Extrakt überbringen und ihn widerspiegeln würde aus dem Weltall der Lichtesherrlichkeit.",
      "Denken wir das alles in einer Seele konzentriert, es gebend dem Erdendasein, um sich versammelt die, welche jetzt als Erdenwesen berufen sein sollen, dies wieder zu­rückzustrahlen, dies zu bewahren für den Rest des Erdendaseins: In der Mitte der aus dem Opfer heraus und durch das Opfer Schenkende, um ihn herum die, welche es empfangen sollen; damit verbunden zu­gleich das, was das Opfer ist, und alles, was damit zusammenhängt, gleichsam übersetzt in irdisches Dasein. Und andrerseits die Möglich­keit, dieses Opfer zu zerstören, so daß alles, was dem Menschenwesen gegeben werden kann, wenn es auf die Gnadewirkung trifft, ebensogut angenommen wie zurückgewiesen werden kann.",
      "Denken wir uns das alles in eine Intuition verkörpert, dann kann man eine solche Empfin­dung haben gegenüber dem «Abendmahl» des Lionardo da Vinci: die ganze Sonne mit den Opferwesen, mit den Wesen der schenkenden Tugend, mit den Wesen der Wärmeseligkeit, der Lichtesherrlichkeit seelisch gefaßt - zurückgestrahlt von denen, die erkoren sind, zu be­wahren aus den früheren Zeiten in die späteren Zeiten; für die Erde hergerichtet dadurch, daß es auch zurückgewiesen werden kann in dem Verräter.",
      "Das Wesen der Erde, insofern das Wesen der Sonne auf der Erde wiedererscheint, man kann es so empfinden. Und wenn dies nicht in",
      "äußerlicher intellektueller Weise, sondern in wahrhaft künstlerischer Weise gefühlt wird, dann hat man etwas von dem empfunden, was die eigentlich treibende Kraft in einem so großen Kunstwerke ist, das gleichsam den Extrakt des Erdendaseins wiedergibt. Und wenn wir das nächste Mal sehen werden, wie herauswächst aus dem Sonnenmilieu der Christus, dann werden wir noch besser das verstehen, was schon öfter gesagt ist: Wenn ein Geist aus dem Mars herunterkäme auf die Erde und alles sehen würde, was er nicht verstehen würde, dann würde er vielleicht kein Stück der Erde begreifen, aber er würde die eigentliche Erdenmission verstehen, wenn er das «Abendmahl» von Lionardo da Vinci auf sich wirken lassen könnte.",
      "Da würde ein solcher Marsbewohner sehen können, wie das Sonnendasein hinein­geheimnißt sein muß in das Erdendasein, und alles, wovon man ihm sagen würde, daß es die Erde bedeutet, würde ihm dadurch klar wer­den. Daß die Erde etwas bedeutet, das würde er verstehen, und er würde wissen, um was es sich auf der Erde handelt.",
      "Er würde sich sagen: Da mag auf der Erde vorgehen, was sonst nur einen Teil für die Erde bedeutet; aber konnte diese Tat wirklich dargestellt werden, die Tat, die mir hier entgegenstrahlt aus den Farben? Wenn ich die Mittel-gestalt mit den umgebenden zusammenhalte, dann fühle ich, was die Geister der Weisheit empfunden haben auf der Sonne, was uns hier wieder entgegentönt in dem Wort: «Dies tut zu meinem Angedenken!» Die Bewahrung des Früheren in dem Späteren: dieses Wort wird uns erst verständlich, wenn wir es begreifen aus dem ganzen Weltenzusammenhange heraus, den wir jetzt kennengelernt haben.",
      "Das nächste Mal wird es unsere Aufgabe sein, das Christus-Wesen aus dem geistigen Wesen der Sonne heraus zu begreifen, um dann überzugehen zu dem geistigen Wesen des Mondes."
    ],
    "sentences": [
      [
        "Aus unseren letzten Auseinandersetzungen werden Sie entnommen haben, daß die Beschreibung jener früheren Zustände unserer Ent­wickelung, die noch vor der Entstehung unserer Erde selbst liegen, außerordentlich schwierig ist.",
        "Denn wir haben gesehen, daß wir uns die Begriffe und Ideen erst heranbilden müssen, durch die wir zu sol­chen fremdartigen, fernen Zuständen unserer Weltentwickelung kom­men können."
      ],
      [
        "Ich habe schon darauf aufmerksam gemacht, daß eine solche Beschreibung, wie sie in meiner «Geheimwissenschaft im Um­riß» von der alten Saturnzeit und auch von den folgenden planeta­rischen Verkörperungen unserer Erde gegeben wird, nicht nur keine erschöpfende ist, sondern sich in gewissem Sinne damit begnügen muß - damit die Öffentlichkeit, der auch dieses Buch übergeben wer­den sollte, nicht zu stark schockiert wird -, dasjenige, worauf es eigent­lich ankommt, in Bilder zu kleiden, die von Naheliegendem und auch von Gewohntem hergenommen sind.",
        "Man gibt damit natürlich nicht eine unrichtige Beschreibung, aber in gewissem Sinne doch eine solche, die sehr bildhaft in Maja, in die Illusion getaucht ist, und man muß sich erst durch die Illusion hindurcharbeiten, um immer mehr und mehr in die Wahrheit der Sache eindringen zu können."
      ],
      [
        "So ist zum Bei­spiel die alte Saturnzeit so beschrieben - wie es innerhalb gewisser Grenzen durchaus richtig ist -, daß gesagt wird, der alte Saturn sei ein Himmelskörper gewesen, der im wesentlichen nicht aus den Bestand­teilen bestanden hat, die wir als Erde, Wasser oder Luft kennen, son­dern nur aus Wärme.",
        "Und wenn von «Raum» gesprochen wird, so ist das nur eine bildhafte Beschreibung, denn wir haben das letzte Mal gesehen, daß es auf dem alten Saturn nicht einmal eine «Zeit» gegeben hat."
      ],
      [
        "Wenn wir also von Raum sprechen, so ist das auch ein Bildhaftes.",
        "Raum gab es auf dem alten Saturn auch nicht in unserem Sinne; und die Zeit entsteht erst auf dem Saturn.",
        "Wir sind durchaus, wenn wir uns auf den alten Saturn zurückversetzen, in dem Be-reich der raumlosen Ewigkeit."
      ],
      [
        "Wenn also etwas gesagt wird, was"
      ],
      [
        "uns ein Bild geben kann, so müssen wir uns klar sein, daß es ein Bild ist."
      ],
      [
        "Wenn wir den Raum des alten Saturn betreten hätten, so würden wir nicht einmal eine so feine Substanz gefunden haben, die wir als «Gas» hätten bezeichnen können, sondern nur Wärme und Kälte.",
        "In Wirklichkeit ist es so, daß man von dem Kommen aus einem Raumteil in einen anderen nicht sprechen kann, sondern daß man nur die Emp­findung von dem Ablauf von wärmeren und kälteren Zuständen ge­brauchen könnte, so daß also auch der Hellseher, wenn er sich in die alte Saturnzeit zurückversetzt, den Eindruck empfängt eines auf und ab flutenden raumlosen Wärmezustandes."
      ],
      [
        "Aber das ist nur der äußere Schleier des Saturnzustandes Denn diese Wärme oder dieses Feuer, wie man im Okkultismus sagt, hat sich uns ja enthüllt in seinen gei­stigen Untergründen; und wir haben gesehen, daß geistige Taten, gei­stige Verrichtungen in Wahrheit das waren, was auf dem alten Saturn wirklich vorhanden war.",
        "Und wir haben uns ein Bild gemacht von dem, was da an geistigen Taten auf dem Saturn vorhanden war."
      ],
      [
        "Wir haben gesagt, daß die Geister des Willens oder die Throne Opfertaten verrichtet haben, so daß, wenn wir zurückschauen auf das, was kon­kret auf dem Saturn geschah, wir die Cherubim haben und die von den Thronen fließenden Opfer.",
        "Opfer fließen von den Thronen zu den Cherubim, und diese Taten des Opfers sind es, die, gleichsam von außen angeschaut, als Wärme erscheinen."
      ],
      [
        "Wärmezustände sind der äußere physische Ausdruck, überhaupt der äußere sinnliche Ausdruck für Opfer.",
        "Und in der ganzen Welt, wo wir Wärme wahrnehmen, ist Wärme der äußere Ausdruck für das, was hinter der Wärme ist."
      ],
      [
        "Wärmezustände sind die Opfertaten von Wesenheiten.",
        "Wenn wir daher die Wärme in Wahrheit charakterisieren wollen, werden wir sagen mussen: Die Weltenwärme ist die Offenbarung des Welten-opfers oder der Weltenopfertaten."
      ],
      [
        "Dann haben wir gesehen, daß aus dieser Tat des Opfers, das die Throne gegenüber den Cherubim darbringen, gleichsam herausgeboren wird - aber ich habe schon darauf aufmerksam gemacht, daß es wie­der ein modernes Wort ist, das nicht recht paßt -, das, was wir die «Zeit» nennen.",
        "Aber die Zeit ist damals noch nicht jenes Abstraktum,"
      ],
      [
        "als welches sie heute der Mensch wahrnimmt, sondern eine Summe von geistigen Wesenheiten: das sind die Geister der Persönlichkeit, die wir dann auch kennengelernt haben als die Zeitgeister.",
        "Die Zeitgeister sind die wirkliche alte Zeit, und sie sind die Kinder der Throne mit den Cherubim."
      ],
      [
        "Aber die Verhältnisse, durch welche die Wesen des Zeitlichen auf dem alten Saturn entstehen, sind Opfer.",
        "Wenn gesagt wird: Der alte Saturn besteht in Wärme -, so müssen wir uns, um ein eigentliches Verständnis dafür zu gewinnen, was dahinter liegt, nicht bloß äußere physische Begriffe aneignen - denn «Warme» ist ein phy­sischer Begriff -, sondern Begriffe, die wir nur aus dem Seelenleben selber gewinnen können, aus dem moralischen, weisheitsvollen Seelenleben."
      ],
      [
        "Niemand kann wissen, was Wärme ist, der nicht in der Lage ist, sich eine Vorstellung zu machen von dem, was heißt, opferfähige Hingabe dessen, was man besitzt, was man hat, ja nicht nur opferfähige Hingabe dessen, was man hat, sondern dessen, was man selber ist.",
        "Die Hinopferung des eigenen Wesens, das Sich-Ent­äußern des eigenen Wesens seelisch gefaßt, so daß man es sich zugleich so denkt, daß man bereit ist, sein Bestes hinzugeben zum Heile der Welt; nicht für sich sein Bestes behalten, sondern es gern hinopfern zu wollen auf dem Altar des Weltalls: das als einen lebendigen Begriff gefaßt, als unsere Seele durchdringend, führt allmählich zum Ver­ständnisse dessen, was hinter der Erscheinung der Wärme ist."
      ],
      [
        "Man vergegenwärtige sich einmal, was im modernen Leben auch heute mit dem Begriff des Opfers verknüpft ist: man kann sich nicht recht den­ken, daß der, welcher mit Verständnis opfert, dies jemals tut gegen seinen Willen.",
        "Wenn jemand opfert gegen seinen Willen, so müßte er dazu aus irgendeinem Grunde gezwungen sein; es müßte ein Zwang walten."
      ],
      [
        "Dann aber würden wir es nicht mit dem zu tun haben, was hier gemeint ist.",
        "Hier ist aber gemeint, was als Opfer selbstverständ­lich fließt aus dem Wesen, das opfert.",
        "Und wenn jemand etwas opfert, nicht weil er aus irgendeinem äußeren Grunde dazu gedrängt wird, auch nicht, weil er hofft, etwas zu erringen, sondern weil er sich aus seinem Inneren heraus gedrängt fühlt zu opfern, dann ist es undenk­bar, daß er etwas anderes empfindet als innere Wärmeseligkeit."
      ],
      [
        "Füh­len wir uns durchglutet mit innerer Wärmeseligkeit, dann haben wir"
      ],
      [
        "schon das ausgesprochen, was wir nicht anders bezeichnen können als:"
      ],
      [
        "der Opfernde fühlt sich durchwärmt, durchglutet mit der Seligkeit.",
        "Da haben wir die Möglichkeit, selbst zu empfinden, wie die Opferglut uns in der äußeren Weltenwärme entgegentreten kann.",
        "Nur der ver­steht wirklich, was Wärme ist, der den Gedanken fassen kann: Wenn Wärme in der Welt auftritt, liegt zugrunde in irgendeiner Weise ein Seelisch-Geistiges, das hinter der Wärme ist und das die Wärme be­wirkt durch die Seligkeit des Opfers.",
        "Wer so die Wärme empfinden kann, der kommt allmählich zu der Realität, welche sich hinter der Wärmeerscheinung, hinter der Wärmeillusion verbirgt."
      ],
      [
        "Wenn wir nun weiterdringen wollen von dem alten Saturndasein zum alten Sonnendasein, so müssen wir uns erst wieder einen Begriff zurechtlegen, durch den wir von der Substanz der alten Sonne, nicht der jetzigen Sonne, eine Vorstellung bilden können.",
        "Denn, was wir in der «Geheimwissenschaft» lesen: «Die alte Sonne hat die Wärme heraufgebildet, indem sie hinzugefügt hat zu der Wärme Luft und Licht», das ist wieder nur durch eine äußere Erscheinung dargestellt.",
        "Wie wir hinter der Wärme suchen müssen die Opferglut der Geister des Willens, so müssen wir hinter der Luft und dem Licht etwas Mora­lisches suchen, wenn wir Luft und Licht, die auf der Sonne zu der Wärme hinzukommen, verstehen wollen.",
        "Nun können wir nur eine Empfindung davon bekommen, was die Substanz der alten Sonne war, wenn wir uns an etwas halten, was wir in uns selbst geistig-seelisch erleben können."
      ],
      [
        "Da gibt es ein Erlebnis, das wir in folgender Weise als ein Seelen-erlebnis beschreiben können.",
        "Denken wir uns, daß irgendein Mensch sehen würde eine richtige, echte Opfertat, oder daß er sich vorstellen würde, wie wir es das letzte Mal bei der Betrachtung des alten Saturn-daseins als Opfertat der Throne geschildert haben, die Throne hinauf­sendend ihre Opfer zu den Cherubim, so daß der Mensch angeregt würde durch das Bild des beseligenden Opfers, das er anschaut und das die Seele lebendig machen würde.",
        "Was würde unsere Seele fühlen entweder durch den Anblick des opfernden Wesens selbst oder durch das Bild, das wir in unserer Seele recht lebendig machen? - Ein solcher Mensch würde, wenn er lebendige Gefühle hat, wenn er nicht mehr"
      ],
      [
        "oder weniger gefühllos der Opferseligkeit gegenüberstehen würde, eine tiefgehende Seligkeit empfinden müssen beim Anblick des Opferbildes; er würde in seiner Seele empfinden müssen: das ist die schönste Tat, das schönste Erlebnis, das überhaupt aus unserer Seele hervorgerufen werden kann, Opferseligkeit anzuschauen!",
        "Das ist aber auch eine solche Empfindung: man müßte ein Stück Holz sein, wenn nicht da in der Seele der Trieb entstehen würde, mit höchster Ehrfurcht anzu­schauen, was Opferseligkeit ist, wenn man nicht davon lernen könnte die Stimmung der völligen Hingabe.",
        "Opfertat ist aktive, in Aktivität sich umsetzende Hingebung.",
        "Die Anschauung von dem aktiven, dem tätigen Hingeben kann die Stimmung des Hingegebenseins, des Sich­Verlierens, des Sich-Vergessens in der Anschauung hervorrufen.",
        "Den­ken wir uns diese Stimmung des selbstlosen Sich-Verlierens in der An­schauung ganz in der Seele ausgegossen, dann haben wir mit dieser Stimmung dasjenige, was insofern uns näher kommen soll für unser Verständnis, als wir ohne eine solche Stimmung, wenigstens ohne eine Ahnung und einen Anklang an eine solche Stimmung, in Wahrheit niemals zu dem kommen könnten, was die höhere Erkenntnis gibt."
      ],
      [
        "Wer niemals solche Stimmung des Hingegebenseins haben kann, der kann nicht zu höheren Erkenntnissen kommen.",
        "Denn, was wäre das Gegenteil dieser Stimmung?",
        "Es wäre der Eigenwille, Geltendma­chung des Eigenwillens.",
        "Das sind überhaupt wie zwei Pole des Weltgeschehens: hingegebene Verlorenheit an das, was man anschaut, und eigenwillige Geltendmachung dessen, was in einem ist.",
        "Das sind zwei große Gegensätze.",
        "Für ein Sich-Durchdringen mit Weisheit ist Eigenwille tötend.",
        "Im gewöhnlichen Leben kennt man Eigenwillen nur als Vorurteil, und Vorurteile zerstören immer höhere Einsicht."
      ],
      [
        "Was hier als Hingegebensein gemeint ist, muß man sich aber gestei­gert denken, denn nur durch dies gesteigerte Hingegebensein kann der Mensch sich zu höheren Welten hinaufarbeiten.",
        "Da muß er jenes Sich-Verlieren wenigstens als Stimmung erleben können.",
        "Daher muß es immer wieder und wieder betont werden, daß wir nie zu einer höheren Erkenntnis kommen, wenn wir so arbeiten wie die gewöhnliche Wis­senschaft oder das alltägliche Denken.",
        "Seien wir uns klar: wie die gewöhnliche Wissenschaft und das alltägliche Denken arbeiten, so arbeiten"
      ],
      [
        "sie aus dem gewöhnlichen Willen des Menschen heraus durch alles dasjenige, was den Eigenwillen geschaffen hat: durch die vererb­ten oder anerzogenen Empfindungen und Gefühle.",
        "Darüber kann man sich sehr täuschen."
      ],
      [
        "Es kommen zum Beispiel Leute und sagen: Da soll man aufnehmen irgendeine Wissenschaft, wie sie geboten wird in der Geisteswissenschaft, aber ich will nichts aufnehmen, als was dem ent­spricht, was ich mir schon denken kann, ich will nichts ungeprüft aufnehmen! - Gewiß, ungeprüft soll man nichts aufnehmen.",
        "Aber da­mit kommt man auch keinen Schritt weiter, daß man nur Geprüftes aufnimmt."
      ],
      [
        "Und der, welcher Hellseher werden will, wird nie sagen, daß er nur das aufnehmen will, was er vorher geprüft hat, sondern er muß vollständig frei werden von allem Eigensüchtigen und muß alles erwarten von dem, was aus der Welt an ihn herantritt, und was man nicht anders bezeichnen kann als mit dem Worte «Gnade».",
        "Er erwar­tet alles von der Gnade, die erleuchtet."
      ],
      [
        "Denn wie erwirbt man hell­seherische Erkenntnisse?",
        "Nur dadurch, daß man alles ausschalten kann, was man jemals gelernt hat.",
        "Gewöhnlich denkt der Mensch: Ich habe mein eigenes Urteil.",
        "Er müßte sich aber sagen: Das besteht nur daraus, daß du auffrischst, was deine Vorfahren gedacht haben, oder was deine Triebe anregen und so weiter."
      ],
      [
        "Denn davon ist nie die Rede, daß dies der Menschen eigene Urteile sind; und die ihre eigenen Urteile am meisten geltend machen, wissen gar nicht, wie sie am Gängelbande ihrer Vorurteile geführt werden.",
        "Das muß alles fort, wenn man zu höheren Erkenntnissen kommen will."
      ],
      [
        "Leer muß die Seele werden und ruhig warten können auf das, was sich aus der raum- und zeitfreien, ding- und tatsachenfreien, verborgenen, geheimen Welt an die Seele heranbegeben kann.",
        "Und nie müssen wir glauben, daß wir an uns heranreißen können, was hellseherische Erkenntnis ist, sondern nur, daß wir eine Stimmung schaffen, durch die wir entgegennehmen, was sich uns darbietet als Offenbarung oder Erleuchtung."
      ],
      [
        "So daß wir nie anders als von der Gnade, die an uns herantritt und uns etwas gibt, das erwarten können, was an uns herantreten soll."
      ],
      [
        "Wie also offenbart sich eine solche Erkenntnis?",
        "Wie offenbart sich das, was da herantritt, wenn wir uns genügend vorbereitet haben?",
        "Es offenbart sich als die Stimmung des Begnadetwerdens durch die uns"
      ],
      [
        "entgegenkommende Gabe aus der geistigen Welt.",
        "Wenn wir das, was an uns herantritt, um uns gnadenvoll entgegenzukommen und in uns die Erkenntnis einzugießen, bezeichnen wollten, so könnten wir nur den Ausdruck gebrauchen: es ist das, was uns da entgegentritt, ein Gnadewirkendes, ein Schenkendes, ein Gebendes."
      ],
      [
        "Fassen wir die Natur eines Wesens, dessen Hauptcharakterzug in dem bestehen würde, was ich jetzt eben mit diesen Worten bezeichnet habe: es ist ein Schenken-des, ein Gebendes, ein Darbietendes; ein solches Wesen, mit dem Hauptcharakterzug des Gnade-um-sich-Streuens, des Gnade-von-sich-Ausgießens - fassen wir es so, daß es, um in diese Möglichkeit des Gnadegebens zu kommen, brauchte den Anblick des Opfers der Throne an die Cherubim!",
        "Denken wir uns einmal, es würde hinzutre­ten zu dem, was da geschieht, wenn die Throne den Cherubim opfern, ein Wesen, welches durch diesen Anblick veranlaßt würde zu einem Schenkenden, zu einem seine Gaben in Gnade um sich Ergießenden zu werden!"
      ],
      [
        "Stellen wir uns das ganz genau vor.",
        "Denken wir uns, wir würden eine Rose anschauen und entzückt werden davon, also das Gefühl eines Beseligenden empfinden über das, was wir «schön» nen­nen!",
        "Denken wir, ein anderes Wesen würde durch den Anblick dessen, was beschrieben ist als das Opfer der Throne an die Cherubim, ver­anlaßt werden, alles, was es hat, um sich herum zu schenken, schen­kend in die Welt zu ergießen: dann würden wir damit diejenigen We­senheiten beschrieben haben, von denen in der «Geheimwissenschaft» die Rede ist als den Geistern der Weisheit, die auf der Sonne hinzu­treten zu denjenigen Wesenheiten, die wir schon auf dem Saturn kennengelernt haben."
      ],
      [
        "Würden wir also die Frage aufwerfen: Welches ist der Charakter der Geister, die auf der Sonne auftraten und zu den Saturngeistern hinzutraten? - so müßten wir antworten: Diese Geister haben als ihren Hauptcharakterzug die schenkende, gnadewirkende, gebende Tugend. - Und wollten wir ein Beiwort haben, so müßten wir sagen: Sie sind die Geister der Weisheit, die großen Schenkenden, die großen Gebenden des Weltalls! - Wie wir von den Thronen gesagt haben: Die großen Opferer -, so müßten wir von den Geistern der Weisheit sagen: Die großen Gebenden, die ihre Gabe so Hingebenden, daß dieselbe von ihnen aus das Weltall durchwebt und durchlebt, indem"
      ],
      [
        "sie einströmt in das Weltall und in dasselbe erst Ordnung hinein­schafft."
      ],
      [
        "Das ist die Wirkung der Geister der Weisheit auf der Sonne.",
        "Das tun sie: schenken ihr eigenes Wesen an ihre Umgebung.",
        "Und was ist das, was sich dem äußeren Anblick darbietet, wenn man so hinblickt und wie eine höhere Sinnesempfindung wahrnehmen will, was da auf der Sonne geschieht?"
      ],
      [
        "Wenn man es ansieht, ist es so, wie es beschrieben ist in der «Ge­heimwissenschaft»: Die Sonne besteht außer aus Wärme auch noch aus Luft und Licht.",
        "Aber wenn man das sagt: Die Sonne besteht außer aus Wärme auch noch aus Luft und Licht -, dann ist es so, wie wenn jemand sagte: In der Ferne sehe ich eine graue Wolke -, und würde er als Maler den Eindruck, den er hat, hinmalen, so würde er eine solche graue Wolke malen, wenn er aber näher hinzuginge, würde er vielleicht statt der grauen Wolke einen Mückenschwarm vor sich haben."
      ],
      [
        "In Wirklichkeit ist dann das, was er für eine graue Wolke hielt, eine Summe von lauter lebendigen Wesen.",
        "In ähnlicher Weise stehen wir von ferne dem alten Sonnendasein gegenüber: Indem wir es von ferne anschauen, erscheint es als die Illusion eines Luft- und Lichtkörpers, wenn wir es aber näher betrachten, haben wir nicht mehr einen Luft- und Lichtkörper, sondern da erscheint es als die große schenkende Tugend der Geister der Weisheit!"
      ],
      [
        "Und niemand lernt die Luft richtig kennen, der sie nur ihren äußeren physischen Eigenschaften nach be­schreibt.",
        "Das ist nur Maja oder Illusion, das ist nur die äußere Offen­barung.",
        "Denn überall wo Luft ist in der Welt, sind die Taten der Gei­ster der Weisheit dahinter."
      ],
      [
        "Webende, wirkende Luft heißt Offen­barung der schenkenden Tugend des Makrokosmos.",
        "Und nur der sieht die Luft richtig an, der sich sagt: Ich nehme hier Luft wahr, in Wahrheit aber wird da geschenkt von den Geistern der Weisheit an die Umgebung, wird etwas ausgestrahlt an die Umgebung."
      ],
      [
        "Jetzt wissen wir, was es eigentlich ist, was wir von der alten Sonne beschrieben haben, indem wir sagten, sie besteht aus Luft.",
        "Wir wissen jetzt, daß es Schenken ist: daß die Geister der Weisheit ihr eigenes Wesen ausfließen lassen und daß es äußerlich als Luft erscheint.",
        "Aber eine merkwürdige Sache trat nuii ein, die sich dem Hellseher darbietet."
      ],
      [
        "Wir müssen uns klarmachen, wie wir von dieser schenkenden Tugend eine noch genauere Vorstellung bekommen können aus unserem Seelen­leben heraus.",
        "Vergegenwärtigen wir uns dazu jenes Gefühl, das wir selbst haben können, wenn es uns gelingt, aus der eben geschilderten Stimmung von Hingabe uns zu durchdringen mit einer Erkenntnis, mit einer Idee.",
        "Von einer solchen Idee haben wir dann immer eine be­stimmte Empfindung.",
        "Die beste Empfindung einer solchen Idee hat man noch, wenn man das Künstlerische ins Auge faßt, wo die Idee den Drang hat, zum Beispiel Farbe oder Form irgendwie zu bemei­stern, also in der Welt auszuströmen, so daß sie ein selbständiges Da­sein der Welt geschenkt hat.",
        "Das Wesen einer solchen schenkenden Fähigkeit ist damit zu charakterisieren, daß man sagt: Produktivität, Schöpferisches ist damit verbunden, denn dieses Schenken ist selbst schöpferisch.",
        "Wer eine Idee hat, von der er empfindet, daß sie der Welt zum Heile gereichen kann und die sich darstellt in Kunstwerken und so weiter, der hat von dieser Produktivität der schenkenden Tu­gend einen richtigen Begriff, das ist es, was als Luft die Sonne durchwebt.",
        "Wenn wir uns denken die schaffende Idee im Kopfe des Künst­lers, wie sie sich einfügt in den Stoff - von allem anderen abgesehen -, dann ist dies das geistige Wesen der Luft.",
        "Wo Luft ist, haben wir es mit so etwas zu tun.",
        "Aber dadurch, daß diese lebendige Produktivität auf der Sonne da war, stellte sich die folgende Tatsache heraus."
      ],
      [
        "Halten wir fest, daß auf dem alten Saturn schon die Geister der Zeit geboren waren, daß also auf der Sonne «Zeit» schon sein konnte, denn diese ist herübergekommen von dem Saturn.",
        "Also es gibt jene Möglichkeit auf der alten Sonne, die es auf dem alten Saturn noch nicht gegeben hätte, daß ein solches Schenken eintrat.",
        "Denn denken Sie einmal, was es wäre mit einem Schenken, wenn es keine Zeit gäbe: da könnte man nicht schenken; denn Schenken besteht im Geben und im Entgegennehmen.",
        "Ohne das zweite ist das Schenken gar nicht zu denken.",
        "Also es muß das Schenken aus zwei Akten bestehen: aus Geben und Nehmen, sonst hat das Schenken keinen Zweck.",
        "Auf der Sonne stehen sich aber Geben und Nehmen ganz sonderbar gegenüber, so nämlich, daß, weil nun schon die Zeit da ist, die Gabe, die dar­gereicht wird auf der alten Sonne an die Umgebung, in der Zeit aufbewahrt"
      ],
      [
        "wird, gleichsam bewahrt wird in der Zeit, so daß die Geister der Weisheit ihr Geschenktes ausgießen, dann bleibt es.",
        "Aber nun muß etwas eintreten, was das nimmt.",
        "Das arbeitet im Verhältnis zu den Gei­stern der Weisheit in einem späteren Augenblick.",
        "So daß die Geister der Weisheit im früheren Augenblicke geben, und das, was notwendig damit verbunden sein muß als Nehmen, tritt im späteren Augen­blicke ein."
      ],
      [
        "Davon können wir nur eine richtige Vorstellung bekommen, wenn wir wieder das eigene Seelenerleben zugrunde legen.",
        "Stellen Sie sich vor, Sie bemühen sich, irgend etwas zu verstehen, oder irgendeinen Gedanken zu bilden."
      ],
      [
        "Jetzt haben Sie diesen Gedanken gebildet.",
        "Mor­gen besinnen Sie sich, machen rein Ihren Geist, damit alles, was Sie gestern an Gedanken gebildet haben, zurückkommen kann in Ihren Geist.",
        "Dann ist das, was gestern gebildet worden ist, von Ihnen heute aufgenommen."
      ],
      [
        "So ist es auf der alten Sonne, indem das, was früher geschenkt wird, bewahrt bleibt für einen späteren Augenblick und später entgegengenommen wird.",
        "Was ist denn dann dieses Entgegen­nehmen?",
        "Es ist eine Tat, ein Geschehen, das sich nur dadurch von dem anderen Geschehen unterscheidet, daß es später ist."
      ],
      [
        "Das Geben kommt den Geistern der Weisheit zu.",
        "Wer nimmt denn nun?",
        "Damit jemand nehmen kann, muß erst jemand da sein.",
        "In derselben Art wie gleich­sam durch einen Geburtsakt, nämlich aus den Opfern der Throne an die Cherubim, die Geister der Zeit auf dem Saturn entstehen, so ent­stehen durch Schenken an die Welt von seiten der Geister der Weisheit auf der Sonne diejenigen Geister, die wir die Erzengel nennen: Ar­changeloi."
      ],
      [
        "Und sie sind auf der alten Sonne die Nehmenden.",
        "Aber sie nehmen auf eine ganz besondere Weise, so nämlich, daß sie, was sie als Gabe erhalten von den Geistern der Weisheit, nicht für sich behalten, sondern es zurückstrahlen, wie der Spiegel Ihr Bild zurückstrahlt."
      ],
      [
        "So haben die Erzengel auf der Sonne die Aufgabe, dasjenige, was in einem früheren Zeitpunkt geschenkt worden ist, in einem späteren Zeit­punkte aufzufangen, so daß es in einem späteren Zeitpunkte noch da ist und widergestrahlt wird durch die Erzengel.",
        "Wir haben also auf der Sonne ein älteres Geben und ein späteres Nehmen, aber dieses Nehmen als Widerstrahlung einer früheren Zeit."
      ],
      [
        "Sie könnten sich denken, daß die Erde nicht so wäre, wie sie jetzt ist, sondern daß folgendes eintreten würde: daß in dem jetzigen Zeit­punkt widerstrahlen könnte, was in einem früheren Zeitpunkt gesche­hen ist.",
        "Nun wissen wir aber, daß so etwas wirklich geschieht."
      ],
      [
        "Wir leben jetzt im fünften nachatlantischen Kulturzeitraum; da strahlen wider die Ereignisse des dritten nachatlantischen Kulturzeitraumes, der alten ägyptisch-chaldäischen Zeit.",
        "Was früher da war, wird auf­gefangen und strahlt jetzt zurück."
      ],
      [
        "Alles, was früher da war, wieder­holt sich.",
        "So haben wir uns gegenüber den Geistern der Weisheit, die in den älteren Sonnenzeiten die Gebenden, Schenkenden sind, in den Erzengeln die Aufnehmenden zu denken."
      ],
      [
        "Dadurch wird etwas ganz Besonderes hervorgerufen, was Sie sich nur richtig vorstellen können, wenn Sie sich denken das Bild einer innerlich geschlossenen Kugel, wo vom Mittelpunkte etwas ausgestrahlt wird, was geschenkt wird; das strahlt bis zur Peripherie hin und strahlt von dort zurück zum Mittel­punkte.",
        "Wir haben uns also von einem Zentrum ausgehend zu denken das, was von den Geistern der Weisheit kommt: das wird ausgestrahlt nach allen Seiten, wird aufgefangen von den Erzengeln und zurück­gestrahlt."
      ],
      [
        "Was da zurückstrahlt in den Raum hinein, ist das Geschenk der Geister der Weisheit.",
        "Und was da die Ausstrahlung der Geister der Weisheit zurückleitet, das ist das Licht, und damit sind die Erz­engel zugleich die Schöpfer des Lichtes."
      ],
      [
        "Licht ist ebensowenig das, als was es uns in der äußeren Illusion erscheint, sondern wo Licht auftritt, haben wir die zurückgestrahlten Gaben der Geister der Weisheit.",
        "Und die Wesen, die wir überall hinter dem Licht vermuten müssen, das sind die Erzengel."
      ],
      [
        "Daher müssen wir sagen: Trifft uns ein Licht, so stecken dahinter die Archangeloi; daß sie uns aber Licht zuströmen können, das kommt nur davon her, daß sie zurückstrahlen, was ihnen entgegenstrahlt, nämlich die schenkende Tugend der Geister der Weisheit."
      ],
      [
        "So bekommen wir ein Bild der alten Sonne.",
        "Wir denken uns einen Zentralsitz, wo vereinigt ist das, was vom alten Saturn herübergekom­men ist: die Opfertaten der Throne gegenüber den Cherubim, im Anblick dieser Opfertaten versunken die Geister der Weisheit.",
        "Durch den Anblick dieser Opfertaten werden sie veranlaßt, von sich auszustrahlen,"
      ],
      [
        "was ihr eigenes Wesen ist: strömende, flutende Weisheit als schenkende Tugend.",
        "Das aber wird, weil es zeitdurchstrahlt ist, aus­gesandt und wieder zurückgesandt, so daß wir einen Globus, einen durch die zurückstrahlende Tugend innerlich erleuchteten Globus haben.",
        "Denn wir müssen uns die alte Sonne nicht nach außen, sondern nach innen leuchtend denken.",
        "Damit ist ein Neues geschaffen, das wir fo]gendermaßen beschreiben können.",
        "Denken wir uns diese Geister der Weisheit, sitzend im Mittelpunkte der Sonne, im Anblick der opfernden Throne versunken und ausstrahlend, was ihr eigenes Wesen ist, wegen des Anblickes der opfernden Throne, und zurück erhalten sie ihr ausstrahlendes Wesen, indem es ihnen von der Ober­fläche zurückstrahlt, so daß sie es als Licht wieder zurückbekommen.",
        "Alles ist durchleuchtet.",
        "Aber was bekommen sie zurück?",
        "Ihr eigenes Wesen wurde, indem sie es hingegeben haben, zum Geschenk an den Makrokosmos, da war es ihr Inneres.",
        "Jetzt strahlt es zurück: ihr eige­nes Wesen tritt ihnen von außen entgegen.",
        "Sie sehen ihr eigenes Inneres in die Welt verteilt und widergestrahlt von außen als Licht, als die Widerspiegelung ihres eigenen Wesens."
      ],
      [
        "Inneres und Äußeres sind die zwei Gegensätze, die uns jetzt ent­gegentreten.",
        "Das Frühere und Spätere verwandelt sich und wird so, daß es sich verwandelt in Inneres und Äußeres.",
        "Der «Raum» ist gebo­ren!",
        "Durch die schenkende Tugend der Geister der Weisheit entsteht der Raum auf der alten Sonne.",
        "Vorher kann «Raum» nur eine bild­liche Bedeutung haben.",
        "Jetzt haben wir den Raum, aber zunächst nur in zwei Dimensionen: noch nicht oben und unten, noch nicht rechts und links, sondern nur Außeres und Inneres. - In Wirklichkeit treten diese beiden Gegensätze schon am Ende des alten Saturn auf, aber sie wiederholen sich als raumschaffend auf der alten Sonne.",
        "Und wenn wir jetzt von all diesen Vorgängen wieder eine Vorstellung gewinnen wollen in der Weise, wie wir es das letzte Mal getan haben, wo das Bild der opfernden Throne vor unsere Seele trat, die Zeitgeister gebä­rend, so werden wir nicht hinmalen einen Körper, der aus Licht be­steht, denn Licht ist nur im Widerstrahlen im Inneren vorhanden.",
        "Sondern eine Kugel als inneren Raum haben wir uns zu denken, in dem Mittelpunkt zunächst sich wiederholend das Bild des Saturn: die"
      ],
      [
        "Throne als Geister wie kniend vor den Cherubim, den geflügelten Wesen, opfernd ihr eigenes Wesen; und hinzukommend die Geister der Weisheit, in dem Anblick des Opfers versinkend.",
        "Und nun kann man als Anblick haben, daß die Glut, die im Opfer liegt, sich verwandelt so, daß sie sinnenfällig vorzustellen ist als Opferrauch, als Luft, die aufsteigt von der Opfertat als Opferrauch."
      ],
      [
        "Und wir bekommen ein vollständiges Bild, wenn wir uns vorstellen: Die opfernden Throne kniend vor den Cherubim, und zu dem Opfer hinzukommend wie im Reigen die Geister der Weisheit, hingegeben in ihrer Stimmung dem, was sie erblicken im Mittelpunkte der Sonne an dem Opfer der Throne; dadurch in ihrer Stimmung erwachsend zu dem Bilde des Opferrau­ches, der sich verbreitet nach allen Seiten, der ausströmt, sich am Ende ballt und aus seinen Wolken herausschafft die Gestalten der Erzengel, die zurückstrahlen von der Peripherie den Opferrauch als Licht, das Innere der Sonne durchleuchtend, das Geschenk der Geister der Weis­heit zurückgebend und die Sphäre der Sonne in dieser Weise schaffend.",
        "Sie besteht schenkend aus Glut und Opferrauch."
      ],
      [
        "An der äußeren Peripherie sitzen die Erzengel, die Schöpfer des Lichtes, die das, was zuerst auf der Sonne da ist, später abbilden; dann aber kommt es zu­rück als Licht.",
        "Was bewahren also die Erzengel?",
        "Sie bewahren das Frühere."
      ],
      [
        "Die Gaben, die sie nehmen, strahlen sie zurück.",
        "Was im An­fange war, strahlen sie dar in einer späteren Zeit.",
        "Und indem sie es zurückstrahlen, sind sie die Engel des Anfanges, weil sie das in späte­ren Zeiten wirksam machen, was früher war."
      ],
      [
        "Archangeloi, Boten des Anfanges sind sie!"
      ],
      [
        "Es ist ganz wunderbar, wenn aus der wirklichen okkulten Erkennt­nis heraus ein solches Wort wieder auftaucht und wir uns dann über­legen, wie dieses Wort aus uralten Traditionen - auf dem Wege über die Schule Dionysius des Areopagiten, der ein Schüler des Paulus war - uns überkommt.",
        "Es ist wunderbar zu sehen, daß dieses Wort so geprägt ist, daß, wenn wir es unabhängig von dem, was da steht, wie­der entwickeln, das entsteht, was da war.",
        "Und wir fühlen uns dann verbunden mit den alten heiligen Schulen der Weiheweisheit, der Weihewissenschaft, so daß wir gleichsam fühlen, wie wenn dieses Alte in uns einströmen würde, indem wir es verständnisvoll ergreifen,"
      ],
      [
        "nachdem wir uns selbst die Möglichkeit geschaffen haben, es unab­hängig von dem Alten aufzunehmen.",
        "Wer nur ein wenig fühlen kann das Stimmen der alten Ausdrücke, die uns überliefert sind, ohne daß wir auf diese Ausdrücke Rücksicht nehmen, der fühlt sich hinein­gestellt in das Walten der Zeitengeister durch den Menschen hindurch.",
        "Es ist etwas Wunderbares verbunden mit der ganzen menschlichen Evolution, was da herauskommt; es ist ein Sicher-Fühlen bei diesen Dingen."
      ],
      [
        "Das Andenken an die Urbeginne bewahren die Erzengel.",
        "Was aber auf irgendeinem Planeten vorhanden war, das wiederholt sich in einer späteren Zeit, nur daß das Spätere immer anderes noch hinzufügt, so daß uns das Wesen der Sonne wieder entgegentritt in dem, was uns auf unserer Erde entgegentritt."
      ],
      [
        "Die ganze Vorstellung, die ganze Empfindung, die wir uns hier aneignen konnten, die uns ein Bild gibt von den opfernden Thronen, von den opferempfangenden Cherubim, von der Glut, die aus dem Opfer ausströmt, von dem Opferrauch, der sich luftartig verbreitet, von dem Licht, das zurückgestrahlt wird von den Erzengeln, die das bewahren, was in den Anfängen geschehen ist, für die späteren Zeiten:"
      ],
      [
        "diese Empfindung ist etwas, was in uns hervorrufen kann ein richtiges Verständnis alles dessen, was zusammenhängt mit den Schöpfungen einer solchen Empfindung, mit Opfern, die aus einer solchen Empfin­dung hervorgehen."
      ],
      [
        "So haben wir an diesem Milieu, das ich eben als Seelenmilieu ge­schildert habe, mehr geistig aufgefaßt, was wir früher an einem mehr physischen Bilde gewonnen haben.",
        "Und wir werden nun sehen, daß aus diesem Milieu geboren wird, was auf der Erde als Christus-Wesen­heit aufgetreten ist; und wir werden nur verstehen, was auf die Erde durch die Christus-Wesenheit gebracht wird, wenn wir uns aneignen den Begriff der schenkenden Tugend, der gnadewirkenden Tugend in ihrer Zurückstrahlung in dem Lichte des Weltenalls in der inneren Substanz des Sonnenmäßigen, die durchdrungen und durchleuchtet ist von diesem Licht.",
        "Wenn wir dies zum Bilde erheben, was wir eben beschrieben haben, und in eine Imagination umwandeln und uns den­ken, daß von alledem, was von diesem Wesen mitgebracht wird auf"
      ],
      [
        "die Erde, sich etwas auf der Erde auslebt, dann werden wir das eigent­liche geistige Wesen des Christus-Impulses daraus noch wieder tiefer beschreiben können.",
        "Wir werden dann verstehen, welche dunkle Ah­nung in der Menschenseele leben kann, wenn diese Menschenseele gegenüber irgendeiner Darstellung empfindet, daß das, was eben be­schrieben worden ist, in einer gewissen Weise wieder lebendig werden kann auf der Erde."
      ],
      [
        "Denken wir uns einmal, es könnte das, was eben von der Sonne beschrieben worden ist, in eines Wesens Seele ganz und gar sich kon­zentrieren, könnte sich zusammendrehen und mitgenommen werden, um später wieder zu erscheinen.",
        "Und es würde wieder erscheinen und so wirken, daß es aus dem, was aus der uralten Opfertat und dem Opferrauch, der lichtschaffenden Zeit und der schenkenden Tugend geschaffen ist, den Extrakt überbringen und ihn widerspiegeln würde aus dem Weltall der Lichtesherrlichkeit."
      ],
      [
        "Denken wir das alles in einer Seele konzentriert, es gebend dem Erdendasein, um sich versammelt die, welche jetzt als Erdenwesen berufen sein sollen, dies wieder zu­rückzustrahlen, dies zu bewahren für den Rest des Erdendaseins: In der Mitte der aus dem Opfer heraus und durch das Opfer Schenkende, um ihn herum die, welche es empfangen sollen; damit verbunden zu­gleich das, was das Opfer ist, und alles, was damit zusammenhängt, gleichsam übersetzt in irdisches Dasein.",
        "Und andrerseits die Möglich­keit, dieses Opfer zu zerstören, so daß alles, was dem Menschenwesen gegeben werden kann, wenn es auf die Gnadewirkung trifft, ebensogut angenommen wie zurückgewiesen werden kann."
      ],
      [
        "Denken wir uns das alles in eine Intuition verkörpert, dann kann man eine solche Empfin­dung haben gegenüber dem «Abendmahl» des Lionardo da Vinci: die ganze Sonne mit den Opferwesen, mit den Wesen der schenkenden Tugend, mit den Wesen der Wärmeseligkeit, der Lichtesherrlichkeit seelisch gefaßt - zurückgestrahlt von denen, die erkoren sind, zu be­wahren aus den früheren Zeiten in die späteren Zeiten; für die Erde hergerichtet dadurch, daß es auch zurückgewiesen werden kann in dem Verräter."
      ],
      [
        "Das Wesen der Erde, insofern das Wesen der Sonne auf der Erde wiedererscheint, man kann es so empfinden.",
        "Und wenn dies nicht in"
      ],
      [
        "äußerlicher intellektueller Weise, sondern in wahrhaft künstlerischer Weise gefühlt wird, dann hat man etwas von dem empfunden, was die eigentlich treibende Kraft in einem so großen Kunstwerke ist, das gleichsam den Extrakt des Erdendaseins wiedergibt.",
        "Und wenn wir das nächste Mal sehen werden, wie herauswächst aus dem Sonnenmilieu der Christus, dann werden wir noch besser das verstehen, was schon öfter gesagt ist: Wenn ein Geist aus dem Mars herunterkäme auf die Erde und alles sehen würde, was er nicht verstehen würde, dann würde er vielleicht kein Stück der Erde begreifen, aber er würde die eigentliche Erdenmission verstehen, wenn er das «Abendmahl» von Lionardo da Vinci auf sich wirken lassen könnte."
      ],
      [
        "Da würde ein solcher Marsbewohner sehen können, wie das Sonnendasein hinein­geheimnißt sein muß in das Erdendasein, und alles, wovon man ihm sagen würde, daß es die Erde bedeutet, würde ihm dadurch klar wer­den.",
        "Daß die Erde etwas bedeutet, das würde er verstehen, und er würde wissen, um was es sich auf der Erde handelt."
      ],
      [
        "Er würde sich sagen: Da mag auf der Erde vorgehen, was sonst nur einen Teil für die Erde bedeutet; aber konnte diese Tat wirklich dargestellt werden, die Tat, die mir hier entgegenstrahlt aus den Farben?",
        "Wenn ich die Mittel-gestalt mit den umgebenden zusammenhalte, dann fühle ich, was die Geister der Weisheit empfunden haben auf der Sonne, was uns hier wieder entgegentönt in dem Wort: «Dies tut zu meinem Angedenken!» Die Bewahrung des Früheren in dem Späteren: dieses Wort wird uns erst verständlich, wenn wir es begreifen aus dem ganzen Weltenzusammenhange heraus, den wir jetzt kennengelernt haben."
      ],
      [
        "Das nächste Mal wird es unsere Aufgabe sein, das Christus-Wesen aus dem geistigen Wesen der Sonne heraus zu begreifen, um dann überzugehen zu dem geistigen Wesen des Mondes."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG Berlin, 14. November 1911",
    "paragraphs": [
      "In unseren beiden letzten Betrachtungen hier haben wir versucht, den Hinweis darauf zu erbringen, wie hinter allem Materiell-Stofflichen unserer Welterscheinungen Geistiges zu suchen ist. Wir haben versucht, zunächst das Geistige, das sich hinter den Wärmeerscheinungen, dann hinter den Erscheinungen der strömenden Luft findet, zu charakteri­sieren.",
      "Wir mußten, da wir ja, um solche Charakteristiken geben zu können, in sehr frühe, urferne Vergangenheiten unserer Entwickelung zurückzugreifen hatten, wir mußten bei unserer Schilderung jener gei­stigen Verhältnisse, die dem Materiellen zugrunde liegen, in unser eige­nes Seelenleben blicken. Denn es ist selbstverständlich notwendig, daß man irgendwoher die Vorstellungen nimmt, mit denen man etwas charakterisiert.",
      "Worte allein tun es nicht, sondern wir müssen ganz bestimmte Vorstellungen haben. Wir haben gesehen, daß die geistigen Verhältnisse, auf die wir uns dabei beziehen müssen, zum Teil so ferne liegend alledem sind, was der Mensch gegenwärtig erlebt, wovon der Mensch gegenwärtig wissen kann, daß wir selbst in unserem Seelenleben, in unserem eigenen Geistesleben an seltene Zustände, an gar nicht allgemeine Verhältnisse appellieren mußten.",
      "Wir haben gesehen, daß wir das tiefste Wesen aller Wärme- und Feuerverhältnisse ganz weit abseits von dem suchen mußten, was äußerlich physikalisch Feuer oder Wärme ist. Gewiß muß es dem Menschen der Gegenwart recht grotesk erscheinen, wenn als das Wesen aller Feuer- und Wärmever­hältnisse das Opfer erkannt worden ist, das Opfer ganz bestimmter Wesenheiten, die wir auf dem alten Saturnzustand der Erde angetrof­fen haben, der Throne, die ihr Opfer den Cherubim damals darbrach­ten.",
      "Und in Wahrheit, müßten wir sagen, besteht ein solches Opfer, wie es damals seinen Ausgangspunkt genommen hat in der Weltentwickelung, in allem, was uns äußerlich, in Maja oder Illusion, in den Wärme- oder Feuerverhältnissen erscheint.",
      "Ebenso haben wir das letzte Mal erkannt, daß hinter allem, was wir nennen können strömende Luft oder strömende Gase, etwas sehr, sehr",
      "Fernes liegt, dasjenige, was wir «schenkende Tugend» genannt haben, das hingebungsvolle Ausgießen des eigenen Wesens geistiger Wesen­heiten. Das liegt in jedem Windhauch, in aller strömenden Luft. Was also äußerlich physisch wahrgenommen wird, ist wirklich nur eine Illusion, eine Maja; und wir haben erst die richtige Vorstellung, wenn wir von der Maja vorschreiten zu dem Geistigen, zu dem Spirituellen. Im Wahrhaftigen der Welt ist Feuer oder Wärme oder Luft ebenso vorhanden, wie ein Spiegelbild im Verhältnis zum Menschen, der sich im Spiegel sieht, vorhanden ist. Denn wie ein Spiegelbild im Grunde genommen eine Illusion im Verhältnis zum Menschen ist, so sind Feuer oder Wärme oder Luft Illusionen, und die Wahrheiten dahinter ver­halten sich in Wirklichkeit so wie der wahrhaftige Mensch zu seinem Spiegelbilde. Nicht Feuer oder Luft haben wir zu suchen in der Welt des Wahrhaftigen, sondern Opfer und schenkende Tugend.",
      "Dabei sind wir aufgestiegen, indem wir zu dem Opfer sozusagen hinzutreten sahen die schenkende Tugend, von dem alten Saturnleben zu dem alten Sonnenleben. Innerhalb des letzteren, das heißt der zwei­ten kosmischen Verkörperung unserer Erde, finden wir etwas, was uns wieder einen Schritt näher führen wird den wahrhaftigen Verhält­nissen unserer Entwickelung. Und wir müssen heute wieder einen Be­griff einführen, der der Welt des Wahrhaftigen angehört gegenüber der Welt der Illusion. Bevor wir also zu den eigentlichen Verhältnis­sen der Entwickelung übergehen, wollen wir uns einen bestimmten Be­griff aneignen. Wir gehen dabei von folgendem aus.",
      "Wenn der Mensch im äußeren Leben irgend etwas tut, irgend etwas vollzieht, so liegt dem in der Regel sein Willensimpuls zugrunde. Was der Mensch tut, sei es nun eine Handbewegung oder sei es die größte Tat, überall liegt der Willensimpuls zugrunde. Von diesem geht dann alles übrige aus, was zu einer Tat, zu einer Verrichtung des Men­schen führt. Der Mensch wird nun zunächst sagen: zu einer starken, kräftigen Tat, die, sagen wir, viel Heil und Segen bringen soll, gehöre ein starker Willensimpuls, und zu einer weniger bedeutsamen Tat ge­höre ein schwacher Willensimpuls. Und im allgemeinen wird der Mensch zu der Annahme geneigt sein, daß von der Stärke des Willens-impulses die Größe der Tat abhängt.",
      "Nun ist das aber nur bis zu einem gewissen Grade richtig, daß wir, wenn wir unseren Willen verstärken, Großes in der Welt erreichen. Von einem gewissen Punkt an ist das nämlich nicht mehr der Fall. Gewisse Taten, die der Mensch tun kann, Taten, die sich vor allen Dingen auf die geistige Welt beziehen, hängen nun nicht ab von der Verstärkung unserer Willensimpulse, sonderbarerweise. Gewiß, in der physischen Welt, in der wir zunächst leben, wird die Größe der Tat abhängen von der Größe des Willensimpulses, denn wir müssen uns stärker anstrengen, wenn wir mehr erreichen wollen. Aber in der gei­stigen Welt ist das gar nicht so, sondern da tritt das Gegenteil von dem ein. Da ist es so, daß zu den größten Taten, zu den größten Wir­kungen, können wir besser noch sagen, nicht eine Verstärkung des positiven Willensimpulses notwendig ist, sondern vielmehr eine ge­wisse Resignation, ein Verzicht. Wir können da schon von den klein­sten, rein geistigen Tatsachen ausgehen. Wir erreichen eine gewisse geistige Wirkung nicht dadurch, daß wir möglichst unsere Begehrlich­keit in Szene setzen, oder möglichst geschäftig sind, sondern in der geistigen Welt erreichen wir gewisse Wirkungen dadurch, daß wir un­sere Wünsche und Begierden bezähmen und auf deren Befriedigung verzichten.",
      "Nehmen wir einmal an, ein Mensch habe es darauf abgesehen, durch innere geistige Wirkungen etwas in der Welt zu erreichen. Dann muß er sich dazu dadurch vorbereiten, daß er vor allen Dingen seine Wünsche, seine Begierden unterdrücken lernt. Und während man in der Welt des Physischen kräftiger wird, sagen wir, wenn man gut ißt, wenn man sich gut ernährt und dadurch mehr Kräfte hat, wird man -es ist das jetzt nur eine Schilderung, kein Rat! - in der geistigen Welt Bedeutsames in einer gewissen Weise gerade dann erreichen, wenn man fastet oder in einer anderen Weise etwas tut, um die Wünsche und Begierden zu unterdrücken, zu bezähmen. Und zu den größten gei­stigen Wirkungen, zu den magischen Wirkungen gehört immer eine solche Vorbereitung, die zusammenhängt mit Verzicht auf Wünsche, Begierden, Willensimpulse, die in uns auftreten. Je weniger wir «wol­len», je mehr wir uns sagen: Wir lassen das Leben an uns vorüber-strömen und begehren nicht dies und begehren nicht jenes, sondern",
      "nehmen die Dinge, wie sie uns Karma zuwirft -, je mehr wir so Karma und seine Wirkungen hinnehmen und ruhig uns verhalten in einem Verzicht in bezug auf alles, was wir sonst im Leben ergreifen wollen für dieses Leben, desto kräftiger werden wir in bezug auf Gedankenwirkungen.",
      "Bei einem Menschen, der ein sehr begierdenvoller Mensch ist, der es vor allen Dingen liebt, recht gut zu essen und zu trinken und auch sonst begierdenvoll ist, bei dem wird sich herausstellen, wenn er zum Beispiel Lehrer oder Erzieher ist, daß seine Worte, die er an seine Zöglinge richtet, nicht viel erreichen, das geht bei den Zöglingen zum einen Ohr hinein, zum anderen heraus. Er wird dann der Meinung sein, daß dies die Schuld der Zöglinge wäre. Das ist aber nicht immer der Fall. Der Mensch, der ein höheres Leben angefangen hat, der mäßig lebt, der nur soviel ißt, als nötig ist, um das Leben zu unterhal­ten, der vorzugsweise darauf bedacht ist, die Dinge, die das Schicksal gibt, hinzunehmen, der wird allmählich merken, daß seine Worte eine große Kraft haben; ja, sein Blick kann dann schon eine große Kraft haben, und es braucht nicht einmal zum Blick zu kommen, er braucht nur neben dem Zögling zu sein, braucht nur einen aufmunternden Gedanken zu haben, den er gar nicht äußert: das wird auf den Zögling übergehen. Das alles hängt ab von dem Grade des Verzichtes, der Resignation gegenüber dem, was der Mensch sonst verlangt.",
      "Nun ist für geistige Betätigungen, um geistige Wirkungen in den höheren Welten zu erzielen, der richtige Weg der, welcher durch den Verzicht geht. In dieser Beziehung bestehen viele Täuschungen, und Täuschungen führen nicht deshalb, weil sie auch im Äußeren so ähn­lich aussehen, zu den richtigen Wirkungen. Sie alle kennen das, was man im gewöhnlichen Leben die Askese, die Selbstpeinigung nennt. Diese Selbstpeinigung kann in vielen Fällen geradezu eine Wollust sein, die der Betreffende aus der Begierde heraus wählt, zum Beispiel, um viel zu erreichen, oder sei es auch aus einem anderen Begierdequell, um Wollust zu wollen. Dann wirkt die Askese nichts; denn sie hat nur dann eine Bedeutung, wenn sie als Begleiterscheinung des schon im Geistigen wurzelnden Verzichts auftritt. Diesen Begriff wollen wir uns eben aneignen: den Begriff des schöpferischen Verzichtes, der",
      "schöpferischen Resignation. Es ist ungeheuer wichtig, daß wir diesen Verzicht, diese schöpferische Resignation, die wir ja in der Seele erle­ben können, wieder als eine dem alltäglichen Leben fernliegende Vor­stellung aufnehmen: dann werden wir einen Schritt tiefer in die Menschheitsevolution hineingeführt werden. Denn so etwas geschieht im Verlaufe der Evolution, zum Beispiel beim Herübergang der Ent­wickelung von den Sonnenverhältnissen zu den Mondverhältnissen. So etwas wie Resignieren geschieht im Bereiche der Wesenheiten der höheren Welten, von denen wir ja wissen, daß sie mit dem Fortgang der Erdentwickelung zusammenhängen. Und zwar wollen wir da noch einmal die alte Sonnenentwickelung ins Auge fassen. Aber machen wir zunächst noch auf etwas aufmerksam, was wir schon wissen, was uns aber bis jetzt noch in mancher Hinsicht rätselhaft erscheinen kann.",
      "Wir haben wiederholt aufmerksam gemacht auf solche Vorgänge in der Entwickelung, die wir zurückzuführen haben auf Wesenheiten, die im Laufe der Entwickelung zurückgeblieben sind. So wissen wir, daß eingreifen in unsere Erdenmenschheit die luziferischen Wesen­heiten. Wir haben wiederholt darauf aufmerksam machen müssen, daß diese luziferischen Wesenheiten deshalb in unseren astralischen Leib während der Erdentwickelung eingreifen, weil sie die Entwickelungs­stufe, die sie während der alten Mondenentwickelung hätten erreichen können, nicht erreicht haben. Wir haben oftmals den trivialen Ver­gleich gebraucht, daß nicht nur in unseren Schulen die Schüler sitzen-bleiben, sondern daß auch die Weltenwesen in der großen kosmischen Evolution sitzenbleiben auf ihren Entwickelungsstufen und später eingreifen in die Entwickelungsstufen von Wesenheiten und dann ähn­liches bewirken wie die luziferischen Wesenheiten, die auf dem alten Monde zurückgeblieben sind.",
      "Demgegenüber könnte man nun sehr leicht den Gedanken aufwer­fen: Eigentlich sind diese Wesenheiten fehlerhafte Wesenheiten, Schädlinge der Weltentwickelung; denn warum sind sie sitzengeblie­ben? Das ist der eine Gedanke, der uns kommen kann. Aber der an­dere Gedanke, den wir auch fassen können, ist der: daß der Mensch nie zu seiner Freiheit, zur selbsteigenen Entschließfähigkeit gekommen wäre, wenn die luziferischen Wesenheiten nicht auf dem Monde zurückgeblieben",
      "wären. So daß der Mensch den luziferischen Wesenhei­ten auf der einen Seite im Üblen das verdankt, daß er Begierden, Triebe, Leidenschaften in seinem Astralleib hat, die ihn fortwährend von einer gewissen Höhe herabdrängen, ihn nach niederen Regionen seines Seins hinziehen. Andererseits aber, wenn dies nicht der Fall wäre, daß der Mensch böse werden kann, daß er abirren kann von dem Guten durch die Kraft der luziferischen Wesenheiten in seinem Astralleib, könnte er auch nicht frei handeln, könnte er nicht das haben, was wir Freiheit des Willens, Willkür nennen. Wir müssen also sagen, auch unsere Freiheit verdanken wir den luziferischen Wesen. Daraus geht also schon hervor, daß die einseitige Auffassung, als ob die luziferischen Wesenheiten nur den Menschen herabbrächten, nicht zutrifft, sondern daß der Mensch ihr Zurückbleiben als etwas Gutes ansehen muß, als etwas, ohne das er gar nicht hätte seine Menschen­würde im wahren Sinne des Wortes erringen können.",
      "Nun liegt alledem, was wir für die luziferischen und ahrimanischen Wesenheiten ein solches Zurückbleiben nennen, etwas viel Tieferes zugrunde, was uns zwar schon auf dem alten Saturn entgegentritt, aber dort so schwer erkennbar, daß wir kaum in irgendeiner Sprache Worte finden könnten, um das, was da zugrunde liegt auf dem alten Saturn, zu charakterisieren. Wenn wir dagegen zum alten Sonnen-dasein vorschreiten, können wir es ganz deutlich charakterisieren, wenn wir den heute zuerst beschriebenen Begriff der Resignation, des Verzichts ins Auge fassen. Denn allem solchen Zurückbleiben von Wesenheiten, allem solchen Hereinwirken durch das Zurückbleiben liegt zugrunde Resignation oder Verzicht höherer Wesenheiten. So können wir sehen, daß folgendes auf der Sonne auftritt. Wir haben gesagt, daß die Throne, die Geister des Willens, Opfer darbringen den Cherubim. Diese Opfer bringen sie - wie wir das letzte Mal gesehen haben - nicht nur während der Saturnzeit dar, sondern sie setzen sie fort während der Sonnenzeit. So daß wir auch da im Bilde bekommen haben: die Throne, die Geister des Willens, opfernd den Cherubim. Und in der Opferung liegt das eigentliche Wesen aller in der Welt existierenden Wärme- oder Feuerverhältnisse. Während der Sonnen-zeit können wir nun deutlich das Folgende bemerken, wenn wir in der",
      "Akasha-Chronik zurückschauen. Die Throne opfern, verbleiben bei ihrer Opfertätigkeit; so daß wir die opfernden Throne haben, haben auch eine Anzahl von Cherubim, zu denen wir das Opfer aufsteigen sehen, indem sie das, was aus dem Opfer fließt, die Wärme, in sich aufnehmen. Aber eine Anzahl von Cherubim vollzieht etwas anderes:",
      "sie verzichten auf das Opfer, nehmen nicht an die Opferung. Daher müssen wir das Bild, das wir das letzte Mal vor unsere Seele treten ließen, noch etwas ergänzen.",
      "Wir haben in diesem Bilde die opfernden Throne und die das Opfer annehmenden Cherubim, wir haben aber auch solche Cherubim, die das Opfer nicht annehmen, sondern wieder zurückgeben, was als Opfer zu ihnen dringt. Das ist außerordentlich interessant in der Akasha-Chronik zu verfolgen.",
      "Denn dadurch, daß nun sozusagen die schenkende Tugend der Geister der Weisheit einfließt in die Opfer-wärme, dadurch sehen wir wie aufsteigend Opferrauch während der alten Sonne, von dem wir gesagt haben, daß er dann durch die Erz­engel in Form von Licht zurückgeworfen wird von dem äußersten Um­fange der Sonne. Aber nun sehen wir, wie wenn innerhalb des alten Sonnenraumes noch etwas ganz anderes vorhanden wäre: Opferrauch, der aber jetzt nicht bloß durch die Erzengel im Licht zurückgeworfen wird, sondern der von den Cherubim nicht angenommen wird, so daß er wie zurückfließt, sich zurückstaut, so daß wir dauernd Opferwolken im Raume haben: Opfer, das aufsteigt, Opfer, das absteigt, Opfer, das angenommen wird, Opfer, auf das ver­zichtet wird.",
      "Dieses Sich-Begegnen der eigentlichen spirituellen Wolkengebilde im alten Sonnenraum finden wir gleichsam zwischen dem, was wir das letzte Mal das Äußere und das Innere genannt haben, bis die Trennung geschieht, so daß wir in der Mitte haben die opfernden Throne, dann die Cherubim in der Höhe, die das Opfer annehmen, dann solche Cherubim, die das Opfer nicht annehmen, son­dern es zurückstauen. Durch dieses Zurückstauen entsteht gleichsam eine Ringwolke, und ganz außen haben wir die zurückgeworfenen Lichtmassen.",
      "Stellen Sie sich dieses Bild ganz lebendig vor: daß wir also diesen alten Sonnenraum haben, diese alte Sonnenmasse, gleichsam eine kosmische",
      "Kugel, außerhalb welcher nichts vorzustellen ist, so daß wir nur den Raum uns zu denken haben bis zu den Erzengeln hin. Stellen wir uns weiter vor, daß wir in der Mitte diese Ringbildung aus den sich begegnenden angenommenen und zurückgewiesenen Opfern haben. Aus diesen angenommenen und zurückgewiesenen Opfern ent­steht innerhalb der alten Sonne etwas, was wir nennen können eine Verdoppelung der ganzen Sonnensubstanz, ein Auseinandergehen. Mit einer äußeren Figur zu vergleichen ist die Sonne in dieser alten Zeit nur, wenn wir sie vergleichen mit unserer jetzigen Saturngestalt: der Kugel, die von Ringen umgeben ist, indem diese sich stauenden Opfer-massen nach einwärts werfen, was in der Mitte ist, und das, was außen ist, wird wie eine Ringinasse außen angeordnet. So haben wir die Sonnensubstanz eigentlich in zwei Teile getrennt durch die Kraft der sich stauenden Opfergewalten. Was wird nun dadurch bewirkt, daß auf der Seite gewisser Cherubim ein solcher Verzicht auf das Opfer eintritt?",
      "Es ist ein außerordentlich schwieriges Kapitel, dem wir uns da nähern, und Sie werden nur in langsamem Meditieren erfassen können, was in den Begriffen liegt, die jetzt auseinandergesetzt werden. Nur wenn man lange über die Begriffe, die gegeben werden, nachdenkt, wird man herausfinden, welche Realitäten diesen Begriffen zugrunde liegen. Die Resignation, von der wir gesprochen haben, müssen wir in Verbindung bringen mit etwas, dessen Entstehung wir auf den alten Saturn verlegt haben: mit der Entstehung der Zeit. Wir haben gesehen, daß mit den Geistern der Zeit, den Archai, die Zeit eigentlich erst auf dem alten Saturn entsteht, und daß es keinen Sinn hat, vor dem alten Saturn von einer «Zeit» zu sprechen. Nun liegt zwar eine Wieder­holung darin, aber wir können doch sagen: die Zeit dauert fort. «Dauern» ist schon ein Begriff, der die Zeit in sich enthält. Wenn also gesagt wird, «die Zeit dauert fort», so bedeutet das: Wenn wir in der Akasha-Chronik Saturn und Sonne betrachten, so finden wir auf dem Saturn die Entstehung der Zeit, und auf der Sonne, daß die Zeit auch vorhanden ist. Wenn nun alle Verhältnisse so fortgingen, wie wir sie in den beiden letzten Betrachtungen charakterisiert haben in bezug auf Saturn und Sonne, so würde die Zeit ein Element bilden für alles",
      "Geschehen in der Evolution. Wir könnten uns die Zeit von keinem Geschehen in der Evolution wegdenken. Wir haben ja gesehen, daß die Geister der Zeit entstanden sind auf dem alten Saturn, und daß die Zeit allem eingepflanzt ist. Und alles, was wir in Bildern, in Imagi­nationen bisher über die Evolution gedacht haben, müssen wir uns mit der Zeit in Verbindung denken. Es war also nur geschehen, was wir angeführt haben: Opferung und schenkende Tugend. Das wäre alles der Zeit unterworfen gewesen. Nichts wäre nicht der Zeit unterworfen gewesen. Das heißt, es würde alles dem Entstehen und Vergehen, was ja der Zeit angehört, unterworfen sein.",
      "Diejenigen Cherubim nun, welche verzichtet haben auf das Opfer, auf das, was gleichsam im Opferrauch liegt, sie haben darauf verzich­tet aus dem Grunde, weil sie sich damit den Eigenschaften dieses Opferrauches entziehen. Und zu diesen Eigenschaften gehört vor allem die Zeit und damit Entstehen und Vergehen.",
      "In dem ganzen Ver­zicht der Cherubim auf das Opfer liegt daher ein den Zeitverhältnis­sen Entwachsen der Cherubim. Sie gehen über die Zeit hinaus, entzie­hen sich dem Unterworfensein unter die Zeit. Damit treffen sich gleichsam die Verhältnisse während der alten Sonnenentwickelung so, daß gewisse Verhältnisse, die in der geraden Linie vom Saturn aus weiter fortgehen, als Opferung und schenkende Tugend der Zeit un­terworfen bleiben, während die anderen Verhältnisse, die von den Cherubim dadurch eingeleitet wurden, daß diese Cherubim auf das Opfer verzichteten, sich der Zeit entreißen und die Ewigkeit, die Dauer, das Nichtunterworfensein dem Entstehen und Vergehen wäh­len.",
      "Das ist etwas höchst Merkwürdiges: wir kommen da während der alten Sonnenentwickelung zu einer Trennung in Zeit und Ewig­keit. Es ist durch die Resignation der Cherubim während der Sonnen-entwickelung die Ewigkeit errungen worden als eine Eigenschaft ge­wisser Verhältnisse, die während der Sonnenentwickelung eintraten.",
      "Sahen wir also, indem wir in unsere eigene Seele blickten, gewisse Wir­kungen aus dieser Seele dadurch erwachsen, daß der Mensch Verzicht und Resignation in der Seele sich aneignet, so sehen wir, wenn wir zunächst nur von der alten Sonne sprechen, daß von gewissen göttlich-geistigen Wesenheiten Unsterblichkeit, Ewigkeit dadurch errungen ist,",
      "daß sie resignierten auf das Opfer und auf das, was aus der schenken­den Tugend und aus den sie verbreitenden Gaben kommen konnte. Sahen wir auf dem Saturn die Zeit entstehen, so sehen wir gewisse Verhältnisse sich der Zeit entreißen während der Sonnenentwickelung. Ich habe allerdings gesagt - ich bitte, das wohl zu beachten -, es be­reitet sich dies schon vor während der Saturnzeit, so daß die Ewigkeit nicht erst beginnt während der Sonnenzeit. Aber klar und deutlich zu sehen, so daß man es aussprechen kann in Begriffen, ist es erst wäh­rend der Sonnenzeit. Es ist auf dem Saturn so schwach erkennbar, dieses Abtrennen der Ewigkeit von der Zeit, daß unsere Begriffe und Worte sich nicht als scharf genug erweisen, um so etwas schon für den alten Saturn und seine Entwickelung zu charakterisieren.",
      "So haben wir die Bedeutung der Resignation kennengelernt, den Verzicht der Götter während der alten Sonnenzeit und die Erringung der Unsterblichkeit. Was war nun die weitere Folge davon?",
      "Aus der «Geheimwissenschaft im Umriß», die in gewisser Beziehung noch in Maja bleiben muß, wissen wir, daß auf die Sonnenentwicke­lung die Mondentwickelung folgte, daß am Ende der Sonnenzeit alle Verhältnisse in eine gewisse Dämmerung, in ein gewisses kosmisches Chaos eintauchten und wieder als Mond auftauchten. So haben wir denn wieder auftauchen zu sehen die Opferung als Wärme. Also, was auch auf der Sonne blieb als Wärme, das sehen wir auch auf dem Monde als Wärme auftauchen. Was schenkende Tugend ist, sehen wir als Gas, als Luft auftauchen. Aber auch die Resignation dauert fort, der Verzicht auf die Opferung. Was wir «Resignation» nannten, ist in all diesem drinnen, was auf dem alten Monde vorgeht. Es ist wirklich so: was wir als Resignation erleben können, müssen wir uns ebenso in allem auf dem alten Monde denken, von der Sonne herübergekom­men, wie wir uns etwas anderes denken, was in der äußeren Welt vor­handen ist. Was Opfer war, erscheint als Wärme in der Maja; was schenkende Tugend war, erscheint in der Maja als Gas oder Luft. Was nun Resignation ist, das erscheint in der äußeren Maja als Flüssigkeit, als Wasser. Wasser ist Maja, und es wäre nicht da in der Welt, wenn nicht geistig zugrunde läge Verzicht oder Resignation. Überall, wo Wasser ist in der Welt, ist Götterverzicht! Ebenso wahr wie Wärme",
      "eine Illusion ist, und wie dahinter das Opfer ist, wie Gas oder Luft eine Illusion ist, und dahinter die schenkende Tugend ist, so ist das Wasser als Substanz, als äußere Wirklichkeit nur eine sinnliche Illu­sion, ein Spiegelbild, und was im Wahrhaftigen davon existiert, ist Resignation irgendwelcher Wesenheiten für das, was sie von anderen Wesenheiten erhalten. Man möchte sagen, es kann nur Wasser in der Welt rieseln, wenn zugrunde liegt Resignation. Nun wissen wir, daß, während die Sonne zum Monde fortschritt, die Luftverhältnisse sich verdichteten zu den Wasserverhältnissen, Wasser entsteht erst auf dem Monde, auf der Sonne gab es noch kein Wasser. Was wir während der alten Sonnenentwickelung als sich ballende Wolkenmassen sehen, das gerinnt, indem es sich ineinanderdrängt zu einem Dichteren, zum Wasser, das auf dem Monde auftritt, zum Mondenmeere.",
      "Wenn wir dies ins Auge fassen, wird es uns immerhin möglich sein, eine Frage, die aufgeworfen werden kann, zu begreifen. Aus der Resignation wird Wasser; Wasser ist eigentlich in Wahrheit Resi­gnation. Wir bekommen also einen geistigen Begriff ganz sonderbarer Art für das, was das Wasser eigentlich ist. Aber wir können die Frage aufwerfen: Es ist doch ein gewisser Unterschied zwischen dem Zu­stande, der eingetreten wäre, wenn die Cherubim nicht resigniert hät­ten, und zwischen dem Zustande, der nun dadurch eingetreten ist, daß sie resigniert haben? Drückt sich dieser Unterschied in irgendeiner Weise aus? - Ja, das tut er. Er drückt sich nämlich dadurch aus, daß nunmehr während der Sonnenverhältnisse deutlich die Folgen jener Resignation auftreten. Wenn nämlich diese Resignation nicht einge­treten wäre, wenn die betreffenden verzichtenden Cherubim das ihnen gebrachte Opfer angenommen hätten, so hätten sie - jetzt bildlich ge­sprochen - den Opferrauch in ihrer eigenen Substanz drinnen gehabt; was sie selber getan hätten, das hätte sich in dem Opferrauch zum Ausdruck gebracht. Nehmen wir an, diese Cherubim hätten dieses oder jenes vollzogen. Dann wäre es erschienen, äußerlich ausgedrückt, durch die sich verändernden Wolken der Luft, das heißt, in der äuße­ren Gestalt der Luft würde sich ausgedrückt haben, was die nicht resignierenden Cherubim mit der Opfersubstanz gemacht hätten. Nun aber haben sie dieselbe zurückgewiesen und sind dadurch aus der",
      "Sterblichkeit in die Unsterblichkeit, aus der Vergänglichkeit in die Dauer übergegangen. Aber die Opfersubstanz ist zunächst da, sie ist sozusagen entlassen aus den Kräften, die sie sonst aufgenommen hät­ten, und braucht jetzt nicht zu folgen den Antrieben, den Impulsen der Cherubim, denn diese haben sie entlassen, haben sie zurückgewie­sen.",
      "Was geschieht nun mit dieser Opfersubstanz? - Es geschieht das, daß andere Wesen sich ihrer bemächtigen, die dadurch, daß sie jetzt diese Opfersubstanz nicht in den Cherubim haben, von den Cherubim unabhängig werden, selbständige Wesen werden, die neben den Cheru­bim da sind, während sie sonst dirigiert werden von der Opfersub­stanz in den Cherubim drinnen, wenn diese die Opfersubstanz auf­genommen haben. Darauf beruht die Möglichkeit, daß das Gegenteil von Resignation eintritt: daß Wesenheiten die ausgeflossene Opfer-substanz an sich heranziehen und in ihr handeln.",
      "Und das sind die Wesenheiten, die zurückbleiben, so daß das Zurückbleiben eine Folge der Resignation der Cherubim ist. Die Cherubim liefern durch das, worauf sie resignieren, den zurückbleibenden Wesenheiten selbst erst die Möglichkeit zum Zurückbleiben.",
      "Dadurch, daß ein Opfer abgewie­sen wird, können andere Wesenheiten, die nicht resignieren, die den Wünschen und Begierden sich hingeben und ihre Wünsche zum Aus­druck bringen, sich des Gegenstandes des Opfers, der Opfersubstanz, bemächtigen und sind damit in der Möglichkeit, als selbständige We­senheiten neben die Opfernden hinzutreten.",
      "So ist mit dem Hinübergehen der Entwickelung von der Sonne zum Mond, mit dem Unsterblichwerden der Cherubim die Möglichkeit gegeben, daß andere Wesenheiten sich abtrennen in eigener Substan­tialität von der fortlaufenden Entwickelung der Cherubim, überhaupt der unsterblichen Wesenheiten. Wir sehen also, indem wir jetzt den tieferen Grund des Zurückbleibens kennenlernen, daß eigentlich die Urschuld, wenn wir von einer solchen Urschuld sprechen wollen, an diesem Zurückbleiben gar nicht diejenigen haben, welche zurück­geblieben sind. Das ist das Wichtige, daß wir das auffassen. Hätten die Cherubim die Opfer angenommen, so hätten die luziferischen Wesenheiten nicht zurückbleiben können, denn sie hätten keine Gele­genheit gehabt, sich in dieser Substanz zu verkörpern. Damit die",
      "Möglichkeit vorhanden war, daß Wesenheiten in dieser Weise selb­ständig werden, trat vorher der Verzicht ein. Es ist also in der Welt-entwickelung so, daß die Götter sich ihre Gegner selbst hervorgerufen haben. Hätten Götter nicht verzichtet, so hätten sich Wesenheiten nicht widersetzen können. Oder wenn wir trivial sprechen wollen, können wir sagen, die Götter hätten gleichsam vorausgesehen: Wenn wir nur so fortschaffen, wie wir es getan haben vom Saturn zur Sonne herüber, so werden niemals freie, aus ihrer Willkür heraus handelnde Wesenheiten entstehen. Es muß, damit solche Wesenheiten entstehen können, die Möglichkeit gegeben sein, daß uns Gegner im Weltenall erstehen, daß wir Widerstände finden in dem, was der Zeit unterwor­fen ist. Würden wir nur selbst alles anordnen, so würden wir einen solchen Widerstand nicht finden können. Wir könnten es uns sehr leicht machen, dadurch daß wir alles Opfer annähmen, dann würde alle Evolution uns unterworfen sein. Das werden wir aber nicht ma­chen; wir wollen Wesenheiten, die sich widersetzen können. Daher nehmen wir das Opfer nicht an, so daß jene Wesenheiten durch unsere Resignation und dadurch, daß sie das Opfer nehmen, unsere Gegner werden!",
      "So sehen wir, daß wir nicht bei den sogenannten bösen Wesenheiten den Grund des Bösen zu suchen haben, sondern bei den guten Wesen­heiten, die erst durch ihre Resignation bewirkt haben, daß durch die Wesenheiten, welche das Böse in die Welt bringen konnten, das Böse entstanden ist. Nun könnte jemand sehr leicht einwenden - und ich bitte, diesen Gedanken recht genau auf Ihre Seele wirken zu lassen -:",
      "Ich habe bisher eine bessere Meinung von den Göttern gehabt! Ich habe bisher die Meinung von den Göttern gehabt, daß sie das, was menschliche Freiheit in Szene setzen sollte, auch bewirken könnten, ohne die Möglichkeit des Bösen zu schaffen. Wie kommt es, daß alle diese guten Götter so etwas wie die menschliche Freiheit nicht ohne das Böse in die Welt bringen konnten? - Ich möchte dabei erinnern an jenen spanischen König, der die Welt so furchtbar kompliziert gefun­den hat und der deshalb einmal gesagt hat: wenn Gott es ihm über­lassen hätte, die Welt zu schaffen, so würde er sie einfacher gemacht haben. - Der Mensch mag in seiner Schwäche denken, daß die Welt",
      "einfacher gemacht werden könnte; aber die Götter wissen es besser, und sie haben es daher dem Menschen nicht überlassen, die Welt zu schaffen.",
      "Wir könnten vom Gesichtspunkt der Erkenntniswissenschaft aus diese Verhältnisse auch noch genauer charakterisieren. Nehmen wir an, es sollte irgend etwas gestützt werden, und man sagt jemandem, das könnte man so stützen, daß man eine Säule aufrichtet und die Sache draufrichtet.",
      "Da könnte der Betreffende dann sagen: Eigentlich müßte es auch anders zu machen sein! - Ja, warum sollte es nicht auch anders zu machen sein? Oder es könnte jemand sagen, wenn man bei einem Bau ein Dreieck braucht: Warum sollte dieses Dreieck nur drei Ecken haben?",
      "Ein Gott könnte vielleicht ein Dreieck so machen, daß es nicht drei Ecken habe! - Aber so viel Sinn es hat, daß ein Dreieck nicht drei Ecken haben soll, so viel Sinn hätte es, daß die Götter die Freiheit hätten schaffen sollen ohne die Möglichkeit des Bösen und des Leides. Wie zum Dreieck drei Ecken gehören, so gehört zur Freiheit die Möglichkeit des Bösen durch die Resignation geistiger Wesenhei­ten.",
      "Das alles gehört zur Resignation der Götter, die dadurch die Evo­lution geschaffen haben aus dem Unsterblichen heraus, nachdem sie durch den Verzicht auf das Opfer den Grad zur Unsterblichkeit ge­nommen hatten, um das Böse wieder zurückzuführen zum Guten. Die Götter haben nicht vermieden das Böse, was allein die Möglichkeit der Freiheit geben konnte.",
      "Hätten die Götter das Böse vermieden, so wäre die Welt arm, wäre nicht mannigfaltig. Die Götter mußten das Böse um der Freiheit willen in die Welt kommen lassen, und sie mußten da­für für sich die Macht erringen, das Böse wieder in das Gute zurück­zuführen.",
      "Diese Macht ist etwas, was als Wirkung nur aus dem Ver­zicht, aus der Resignation kommen kann.",
      "Religionen sind immer dazu da, um sozusagen in Bildern, in Imagi­nationen auf die großen Weltengeheimnisse hinzuweisen. Wir haben heute auf uralte Entwickelungsphasen hingewiesen, und indem wir dem Begriff des Opfers und der schenkenden Tugend hinzufügten den Begriff der Resignation, haben wir dadurch wieder einen Schritt in das Wahrhaftige gegenüber der Maja und Illusion hinein gemacht. Solche Begriffe wurden den Menschen in den Religionen gegeben. Und",
      "es gibt etwas innerhalb der biblischen Religion, wodurch sich der Mensch aneignen kann den Begriff der Resignation, des Zurückwei­sens des Opfers. Das ist die Erzählung von dem opfernden Abraham, der seinen eigenen Sohn dem Gotte darbringen soll, und von dem Ver­zicht dieses Gottes auf das Opfer des Patriarchen. Wenn wir diesen Begriff des Verzichtes in unsere Seele aufnehmen, dann können solche Anschauungen in uns hineinkommen, wie wir sie schon geäußert haben. Einmal habe ich gesagt: Nehmen wir an, das Opfer des Abraham wäre angenommen und Isaak geopfert worden. Da von ihm das ganze alt­hebräische Volk abstammt, so hätte der Gott durch die Annahme des Opfers dieses ganze Volk von der Erde genommen. Alles, was von Abraham abstammte, schenkte der Gott durch den Verzicht einer Sphäre, die außerhalb seiner ist. Hätte er das Opfer angenommen, so hätte er damit die ganze Sphäre, die sich innerhalb des althebräischen Volkes abspielte, in sich aufgenommen, denn der geopferte Isaak wäre dann bei Gott gewesen. So aber hat er darauf verzichtet und damit diese ganze Evolutionslinie der Erde überlassen.",
      "Also die Begriffe der Resignation, des Opfers, können uns aufgehen bei dem bedeutungsvollen Bilde der Opferung des alten Patriarchen. Aber noch an einer anderen Stelle unserer irdischen Geschichte können wir dieses Resignieren höherer Wesenheiten finden, und auch da dür­fen wir wieder hinweisen auf etwas, worauf wir schon das letzte Mal hingewiesen haben: auf das Bild von Lionardo da Vinci, auf das «Abendmahl». Stellt es doch die Szene vor, wo wir gleichsam den Sinn der Erde vor uns haben, den Christus. Erinnern wir uns, indem wir den ganzen Sinn des Bildes durchdringen wollen, an jene Worte, die wir auch im Evangelium finden: «Könnte ich nicht ein ganzes Heer von Engeln herbeirufen, wenn ich entgehen wollte dem Opfertode?» Was in diesem Moment der Christus annehmen könnte, was ihm selbst­verständlich eine leichte Möglichkeit wäre, das wird in Resignation, in Verzicht zurückgewiesen. Und der größte Verzicht des Christus Jesus tritt uns da entgegen, wo er durch seinen Verzicht sich den Gegner selber in seine Sphäre kommen läßt: den Judas. Wenn wir in dem Christus Jesus dasjenige sehen, was wir in ihm sehen können, so müssen wir in ihm ein Abbild derjenigen Wesenheiten sehen, die wir",
      "jetzt eben auf einer gewissen Entwickelungsstufe kennengelernt haben, derjenigen, die auf das Opfer verzichten mußten, derjenigen, deren Natur Resignation ist. - Der Christus resigniert auf das, was gesche­hen würde, wenn er nicht den Judas als seinen Gegner auftreten lassen würde, wie die Götter einst während der Sonnenzeit selber durch Resignation ihre Gegner hervorgerufen haben. So sehen wir diesen Vorgang wiederholt im Bilde auf der Erde: der Christus unter den Zwölfen, den Verräter in der Mitte, den Judas, so wie die Gegner der kosmischen Mächte auftraten.",
      "Damit das in die Entwickelung eintre­ten kann, was der Menschheit unendlich wert ist, muß sich der Chri­stus selbst seinem Gegner entgegenstellen. Weil wir an einen solchen kosmischen Augenblick erinnert werden beim Anblick des Abend­mahles, wenn wir uns die Worte vorhalten: «Wer mit mir den Bissen in die Schüssel tauchen wird, der wird mich verraten», weil wir da im irdischen Abbilde sehen den Gegner der Götter selbst den Göttern gegenübergestellt, deshalb macht dieses Bild einen so gewaltigen Ein­druck.",
      "Deshalb durfte ich oft sagen: Alles, was ein Marsbewohner sehen würde, wenn er heruntersteigen könnte auf die Erde, würde er vielleicht mehr oder weniger interessant finden, wenn er es auch nicht recht verstehen würde. Beim Anblick aber jenes Bildes von Lionardo da Vinci würde er aus einer Stelle des Kosmischen, die mit dem Mars ebenso zusammenhängt wie mit der Erde, etwas kennenlernen, woraus er den Sinn der Erde erkennen würde.",
      "Was da im irdischen Bilde ab­gebildet ist, das hat für den ganzen Kosmos eine Bedeutung: das Sich-Entgegenstellen gewisser Mächte den unsterblichen göttlichen Mäch­ten. Und indem inmitten seiner Apostel der Christus erscheint, der auf der Erde den Tod überwindet, also den Triumph der Unsterblichkeit zeigt, muß auf jenen bedeutungsvollen universellen Moment hinge­wiesen werden, der da eintrat, als sich überhaupt Götter absonderten vom zeitlichen Sein und den Sieg über die Zeit errangen, das heißt, un­sterblich wurden.",
      "Das kann unser Herz fühlen, wenn wir das «Abend­mahl» von Lionardo da Vinci anschauen.",
      "Sagen Sie nicht, daß der, welcher mit einem naiven Gemüte das «Abendmahl» anschaut, dies alles doch nicht weiß, was wir heute ge­sagt haben. Er braucht es nicht zu wissen. Denn darin besteht das geheimnisvolle",
      "Tiefe der Menschenseele, daß man gar nicht mit dem Verstande zu wissen braucht, was die Menschenseele fühlt. Weiß die Blume die Gesetze, nach denen sie wächst? Nein, aber sie wächst darum doch. Was braucht die Blume die Gesetze, was die Menschen-seele einen Verstand, um zu fühlen das ganz unermeßlich Große, das vorhanden ist, wenn vor dem Auge sich ausbreitet ein Gott und sein Gegner, wenn das Höchste, das ausgedrückt werden kann, der Gegen­satz von Unsterblichem und Vergänglichem, vor uns steht? Das braucht man nicht zu wissen, das geht mit magischer Kraft in die Seele über, wenn der Mensch vor diesem Bilde steht, das als Spiegel des Weltensinnes uns da hingemalt ist. Und der Künstler brauchte auch nicht in demselben Sinne ein Okkultist zu sein, um es hinzumalen. Aber in der Seele des Lionardo da Vinci waren die Kräfte, die gerade dieses Höchste, Bedeutungsvollste zum Ausdruck bringen konnten. Deshalb wirken die großen Kunstwerke so ungeheuer, weil sie tief ver­bunden sind mit dem Sinn der Weltenordnung. In früheren Zeiten waren die Künstler verbunden mit dem Sinn der Weltenordnung in dumpfem Bewußtsein, ohne daß sie es wußten. Aber die Kunst würde ersterben, würde keine Fortsetzung erhalten, wenn nicht in Zukunft die Geisteswissenschaft als Wissen von diesen Dingen der Kunst eine neue Grundlage gäbe.",
      "Die unterbewußte Kunst hat ihre Vergangenheit und mit ihrer Ver­gangenheit ein Ende erreicht. Die Kunst, welche sich von der Geistes­wissenschaft inspirieren läßt, steht im Beginn, im Ausgange. Das ist die Kunst der Zukunft. So wahr es ist, daß der alte Künstler nicht zu wissen brauchte, was den Kunstwerken zugrunde liegt, so wahr ist es, daß es der zukünftige Künstler wissen muß, aber mit jenen Kräften, die wieder eine Art des Unendlichen darstellen, die wieder etwas aus dem Vollinhaltlichen der Seele darstellen. Denn der hat nicht die Geisteswissenschaft, der sie wieder zu einer Verstandeswissenschaft macht, sondern der hat sie, der bei jedem Begriff, den wir ent­wickeln - Opfer, schenkende Tugend, Resignation -, der bei jedem Worte etwas empfinden kann, was das Wort, was die Idee selbst zer­sprengen will, was höchstens in die Vieldeutigkeit der Bilder aus­fließen kann.",
      "Schemen wird man hinstellen können, wenn man glaubt, die Ent­wickelung der Welt vollziehe sich in abstrakten Begriffen. Es geht schon nicht mehr gut mit Schemen, wenn man lebendige Begriffe, wie Opferung, schenkende Tugend und Resignation hinstellen will; da müssen wir schon solche Bilder vor uns hinmalen, wie wir sie die letzten Male beschrieben haben: die opfernden Throne, die ihr Opfer hinaufsenden zu den Cherubim, der sich verbreitende Opferrauch, die das Licht zurückwerfenden Erzengel und so weiter. Und wenn wir das nächste Mal zum Mondendasein übergehen, werden wir sehen, wie das Bild reicher wird, wie tatsächlich etwas wird hinzutreten müssen wie die Verflüssigung der sich stauenden Wolkenmassen, die rieseln als Regenmassen, und das Dazutreten der zuckenden Blitze der Seraphim. Da müssen wir zu reicheren Vorstellungen übergehen, gegenüber denen man sagen wird: Die Zukunft der Menschheit wird schon die Möglich­keit finden, auch das künstlerische Material, die künstlerischen Mittel herbeizuschaffen, um für die äußere Welt zum Ausdruck zu bringen, was sonst nur in der Akasha-Chronik zu lesen sein kann."
    ],
    "sentences": [
      [
        "In unseren beiden letzten Betrachtungen hier haben wir versucht, den Hinweis darauf zu erbringen, wie hinter allem Materiell-Stofflichen unserer Welterscheinungen Geistiges zu suchen ist.",
        "Wir haben versucht, zunächst das Geistige, das sich hinter den Wärmeerscheinungen, dann hinter den Erscheinungen der strömenden Luft findet, zu charakteri­sieren."
      ],
      [
        "Wir mußten, da wir ja, um solche Charakteristiken geben zu können, in sehr frühe, urferne Vergangenheiten unserer Entwickelung zurückzugreifen hatten, wir mußten bei unserer Schilderung jener gei­stigen Verhältnisse, die dem Materiellen zugrunde liegen, in unser eige­nes Seelenleben blicken.",
        "Denn es ist selbstverständlich notwendig, daß man irgendwoher die Vorstellungen nimmt, mit denen man etwas charakterisiert."
      ],
      [
        "Worte allein tun es nicht, sondern wir müssen ganz bestimmte Vorstellungen haben.",
        "Wir haben gesehen, daß die geistigen Verhältnisse, auf die wir uns dabei beziehen müssen, zum Teil so ferne liegend alledem sind, was der Mensch gegenwärtig erlebt, wovon der Mensch gegenwärtig wissen kann, daß wir selbst in unserem Seelenleben, in unserem eigenen Geistesleben an seltene Zustände, an gar nicht allgemeine Verhältnisse appellieren mußten."
      ],
      [
        "Wir haben gesehen, daß wir das tiefste Wesen aller Wärme- und Feuerverhältnisse ganz weit abseits von dem suchen mußten, was äußerlich physikalisch Feuer oder Wärme ist.",
        "Gewiß muß es dem Menschen der Gegenwart recht grotesk erscheinen, wenn als das Wesen aller Feuer- und Wärmever­hältnisse das Opfer erkannt worden ist, das Opfer ganz bestimmter Wesenheiten, die wir auf dem alten Saturnzustand der Erde angetrof­fen haben, der Throne, die ihr Opfer den Cherubim damals darbrach­ten."
      ],
      [
        "Und in Wahrheit, müßten wir sagen, besteht ein solches Opfer, wie es damals seinen Ausgangspunkt genommen hat in der Weltentwickelung, in allem, was uns äußerlich, in Maja oder Illusion, in den Wärme- oder Feuerverhältnissen erscheint."
      ],
      [
        "Ebenso haben wir das letzte Mal erkannt, daß hinter allem, was wir nennen können strömende Luft oder strömende Gase, etwas sehr, sehr"
      ],
      [
        "Fernes liegt, dasjenige, was wir «schenkende Tugend» genannt haben, das hingebungsvolle Ausgießen des eigenen Wesens geistiger Wesen­heiten.",
        "Das liegt in jedem Windhauch, in aller strömenden Luft.",
        "Was also äußerlich physisch wahrgenommen wird, ist wirklich nur eine Illusion, eine Maja; und wir haben erst die richtige Vorstellung, wenn wir von der Maja vorschreiten zu dem Geistigen, zu dem Spirituellen.",
        "Im Wahrhaftigen der Welt ist Feuer oder Wärme oder Luft ebenso vorhanden, wie ein Spiegelbild im Verhältnis zum Menschen, der sich im Spiegel sieht, vorhanden ist.",
        "Denn wie ein Spiegelbild im Grunde genommen eine Illusion im Verhältnis zum Menschen ist, so sind Feuer oder Wärme oder Luft Illusionen, und die Wahrheiten dahinter ver­halten sich in Wirklichkeit so wie der wahrhaftige Mensch zu seinem Spiegelbilde.",
        "Nicht Feuer oder Luft haben wir zu suchen in der Welt des Wahrhaftigen, sondern Opfer und schenkende Tugend."
      ],
      [
        "Dabei sind wir aufgestiegen, indem wir zu dem Opfer sozusagen hinzutreten sahen die schenkende Tugend, von dem alten Saturnleben zu dem alten Sonnenleben.",
        "Innerhalb des letzteren, das heißt der zwei­ten kosmischen Verkörperung unserer Erde, finden wir etwas, was uns wieder einen Schritt näher führen wird den wahrhaftigen Verhält­nissen unserer Entwickelung.",
        "Und wir müssen heute wieder einen Be­griff einführen, der der Welt des Wahrhaftigen angehört gegenüber der Welt der Illusion.",
        "Bevor wir also zu den eigentlichen Verhältnis­sen der Entwickelung übergehen, wollen wir uns einen bestimmten Be­griff aneignen.",
        "Wir gehen dabei von folgendem aus."
      ],
      [
        "Wenn der Mensch im äußeren Leben irgend etwas tut, irgend etwas vollzieht, so liegt dem in der Regel sein Willensimpuls zugrunde.",
        "Was der Mensch tut, sei es nun eine Handbewegung oder sei es die größte Tat, überall liegt der Willensimpuls zugrunde.",
        "Von diesem geht dann alles übrige aus, was zu einer Tat, zu einer Verrichtung des Men­schen führt.",
        "Der Mensch wird nun zunächst sagen: zu einer starken, kräftigen Tat, die, sagen wir, viel Heil und Segen bringen soll, gehöre ein starker Willensimpuls, und zu einer weniger bedeutsamen Tat ge­höre ein schwacher Willensimpuls.",
        "Und im allgemeinen wird der Mensch zu der Annahme geneigt sein, daß von der Stärke des Willens-impulses die Größe der Tat abhängt."
      ],
      [
        "Nun ist das aber nur bis zu einem gewissen Grade richtig, daß wir, wenn wir unseren Willen verstärken, Großes in der Welt erreichen.",
        "Von einem gewissen Punkt an ist das nämlich nicht mehr der Fall.",
        "Gewisse Taten, die der Mensch tun kann, Taten, die sich vor allen Dingen auf die geistige Welt beziehen, hängen nun nicht ab von der Verstärkung unserer Willensimpulse, sonderbarerweise.",
        "Gewiß, in der physischen Welt, in der wir zunächst leben, wird die Größe der Tat abhängen von der Größe des Willensimpulses, denn wir müssen uns stärker anstrengen, wenn wir mehr erreichen wollen.",
        "Aber in der gei­stigen Welt ist das gar nicht so, sondern da tritt das Gegenteil von dem ein.",
        "Da ist es so, daß zu den größten Taten, zu den größten Wir­kungen, können wir besser noch sagen, nicht eine Verstärkung des positiven Willensimpulses notwendig ist, sondern vielmehr eine ge­wisse Resignation, ein Verzicht.",
        "Wir können da schon von den klein­sten, rein geistigen Tatsachen ausgehen.",
        "Wir erreichen eine gewisse geistige Wirkung nicht dadurch, daß wir möglichst unsere Begehrlich­keit in Szene setzen, oder möglichst geschäftig sind, sondern in der geistigen Welt erreichen wir gewisse Wirkungen dadurch, daß wir un­sere Wünsche und Begierden bezähmen und auf deren Befriedigung verzichten."
      ],
      [
        "Nehmen wir einmal an, ein Mensch habe es darauf abgesehen, durch innere geistige Wirkungen etwas in der Welt zu erreichen.",
        "Dann muß er sich dazu dadurch vorbereiten, daß er vor allen Dingen seine Wünsche, seine Begierden unterdrücken lernt.",
        "Und während man in der Welt des Physischen kräftiger wird, sagen wir, wenn man gut ißt, wenn man sich gut ernährt und dadurch mehr Kräfte hat, wird man -es ist das jetzt nur eine Schilderung, kein Rat! - in der geistigen Welt Bedeutsames in einer gewissen Weise gerade dann erreichen, wenn man fastet oder in einer anderen Weise etwas tut, um die Wünsche und Begierden zu unterdrücken, zu bezähmen.",
        "Und zu den größten gei­stigen Wirkungen, zu den magischen Wirkungen gehört immer eine solche Vorbereitung, die zusammenhängt mit Verzicht auf Wünsche, Begierden, Willensimpulse, die in uns auftreten.",
        "Je weniger wir «wol­len», je mehr wir uns sagen: Wir lassen das Leben an uns vorüber-strömen und begehren nicht dies und begehren nicht jenes, sondern"
      ],
      [
        "nehmen die Dinge, wie sie uns Karma zuwirft -, je mehr wir so Karma und seine Wirkungen hinnehmen und ruhig uns verhalten in einem Verzicht in bezug auf alles, was wir sonst im Leben ergreifen wollen für dieses Leben, desto kräftiger werden wir in bezug auf Gedankenwirkungen."
      ],
      [
        "Bei einem Menschen, der ein sehr begierdenvoller Mensch ist, der es vor allen Dingen liebt, recht gut zu essen und zu trinken und auch sonst begierdenvoll ist, bei dem wird sich herausstellen, wenn er zum Beispiel Lehrer oder Erzieher ist, daß seine Worte, die er an seine Zöglinge richtet, nicht viel erreichen, das geht bei den Zöglingen zum einen Ohr hinein, zum anderen heraus.",
        "Er wird dann der Meinung sein, daß dies die Schuld der Zöglinge wäre.",
        "Das ist aber nicht immer der Fall.",
        "Der Mensch, der ein höheres Leben angefangen hat, der mäßig lebt, der nur soviel ißt, als nötig ist, um das Leben zu unterhal­ten, der vorzugsweise darauf bedacht ist, die Dinge, die das Schicksal gibt, hinzunehmen, der wird allmählich merken, daß seine Worte eine große Kraft haben; ja, sein Blick kann dann schon eine große Kraft haben, und es braucht nicht einmal zum Blick zu kommen, er braucht nur neben dem Zögling zu sein, braucht nur einen aufmunternden Gedanken zu haben, den er gar nicht äußert: das wird auf den Zögling übergehen.",
        "Das alles hängt ab von dem Grade des Verzichtes, der Resignation gegenüber dem, was der Mensch sonst verlangt."
      ],
      [
        "Nun ist für geistige Betätigungen, um geistige Wirkungen in den höheren Welten zu erzielen, der richtige Weg der, welcher durch den Verzicht geht.",
        "In dieser Beziehung bestehen viele Täuschungen, und Täuschungen führen nicht deshalb, weil sie auch im Äußeren so ähn­lich aussehen, zu den richtigen Wirkungen.",
        "Sie alle kennen das, was man im gewöhnlichen Leben die Askese, die Selbstpeinigung nennt.",
        "Diese Selbstpeinigung kann in vielen Fällen geradezu eine Wollust sein, die der Betreffende aus der Begierde heraus wählt, zum Beispiel, um viel zu erreichen, oder sei es auch aus einem anderen Begierdequell, um Wollust zu wollen.",
        "Dann wirkt die Askese nichts; denn sie hat nur dann eine Bedeutung, wenn sie als Begleiterscheinung des schon im Geistigen wurzelnden Verzichts auftritt.",
        "Diesen Begriff wollen wir uns eben aneignen: den Begriff des schöpferischen Verzichtes, der"
      ],
      [
        "schöpferischen Resignation.",
        "Es ist ungeheuer wichtig, daß wir diesen Verzicht, diese schöpferische Resignation, die wir ja in der Seele erle­ben können, wieder als eine dem alltäglichen Leben fernliegende Vor­stellung aufnehmen: dann werden wir einen Schritt tiefer in die Menschheitsevolution hineingeführt werden.",
        "Denn so etwas geschieht im Verlaufe der Evolution, zum Beispiel beim Herübergang der Ent­wickelung von den Sonnenverhältnissen zu den Mondverhältnissen.",
        "So etwas wie Resignieren geschieht im Bereiche der Wesenheiten der höheren Welten, von denen wir ja wissen, daß sie mit dem Fortgang der Erdentwickelung zusammenhängen.",
        "Und zwar wollen wir da noch einmal die alte Sonnenentwickelung ins Auge fassen.",
        "Aber machen wir zunächst noch auf etwas aufmerksam, was wir schon wissen, was uns aber bis jetzt noch in mancher Hinsicht rätselhaft erscheinen kann."
      ],
      [
        "Wir haben wiederholt aufmerksam gemacht auf solche Vorgänge in der Entwickelung, die wir zurückzuführen haben auf Wesenheiten, die im Laufe der Entwickelung zurückgeblieben sind.",
        "So wissen wir, daß eingreifen in unsere Erdenmenschheit die luziferischen Wesen­heiten.",
        "Wir haben wiederholt darauf aufmerksam machen müssen, daß diese luziferischen Wesenheiten deshalb in unseren astralischen Leib während der Erdentwickelung eingreifen, weil sie die Entwickelungs­stufe, die sie während der alten Mondenentwickelung hätten erreichen können, nicht erreicht haben.",
        "Wir haben oftmals den trivialen Ver­gleich gebraucht, daß nicht nur in unseren Schulen die Schüler sitzen-bleiben, sondern daß auch die Weltenwesen in der großen kosmischen Evolution sitzenbleiben auf ihren Entwickelungsstufen und später eingreifen in die Entwickelungsstufen von Wesenheiten und dann ähn­liches bewirken wie die luziferischen Wesenheiten, die auf dem alten Monde zurückgeblieben sind."
      ],
      [
        "Demgegenüber könnte man nun sehr leicht den Gedanken aufwer­fen: Eigentlich sind diese Wesenheiten fehlerhafte Wesenheiten, Schädlinge der Weltentwickelung; denn warum sind sie sitzengeblie­ben?",
        "Das ist der eine Gedanke, der uns kommen kann.",
        "Aber der an­dere Gedanke, den wir auch fassen können, ist der: daß der Mensch nie zu seiner Freiheit, zur selbsteigenen Entschließfähigkeit gekommen wäre, wenn die luziferischen Wesenheiten nicht auf dem Monde zurückgeblieben"
      ],
      [
        "wären.",
        "So daß der Mensch den luziferischen Wesenhei­ten auf der einen Seite im Üblen das verdankt, daß er Begierden, Triebe, Leidenschaften in seinem Astralleib hat, die ihn fortwährend von einer gewissen Höhe herabdrängen, ihn nach niederen Regionen seines Seins hinziehen.",
        "Andererseits aber, wenn dies nicht der Fall wäre, daß der Mensch böse werden kann, daß er abirren kann von dem Guten durch die Kraft der luziferischen Wesenheiten in seinem Astralleib, könnte er auch nicht frei handeln, könnte er nicht das haben, was wir Freiheit des Willens, Willkür nennen.",
        "Wir müssen also sagen, auch unsere Freiheit verdanken wir den luziferischen Wesen.",
        "Daraus geht also schon hervor, daß die einseitige Auffassung, als ob die luziferischen Wesenheiten nur den Menschen herabbrächten, nicht zutrifft, sondern daß der Mensch ihr Zurückbleiben als etwas Gutes ansehen muß, als etwas, ohne das er gar nicht hätte seine Menschen­würde im wahren Sinne des Wortes erringen können."
      ],
      [
        "Nun liegt alledem, was wir für die luziferischen und ahrimanischen Wesenheiten ein solches Zurückbleiben nennen, etwas viel Tieferes zugrunde, was uns zwar schon auf dem alten Saturn entgegentritt, aber dort so schwer erkennbar, daß wir kaum in irgendeiner Sprache Worte finden könnten, um das, was da zugrunde liegt auf dem alten Saturn, zu charakterisieren.",
        "Wenn wir dagegen zum alten Sonnen-dasein vorschreiten, können wir es ganz deutlich charakterisieren, wenn wir den heute zuerst beschriebenen Begriff der Resignation, des Verzichts ins Auge fassen.",
        "Denn allem solchen Zurückbleiben von Wesenheiten, allem solchen Hereinwirken durch das Zurückbleiben liegt zugrunde Resignation oder Verzicht höherer Wesenheiten.",
        "So können wir sehen, daß folgendes auf der Sonne auftritt.",
        "Wir haben gesagt, daß die Throne, die Geister des Willens, Opfer darbringen den Cherubim.",
        "Diese Opfer bringen sie - wie wir das letzte Mal gesehen haben - nicht nur während der Saturnzeit dar, sondern sie setzen sie fort während der Sonnenzeit.",
        "So daß wir auch da im Bilde bekommen haben: die Throne, die Geister des Willens, opfernd den Cherubim.",
        "Und in der Opferung liegt das eigentliche Wesen aller in der Welt existierenden Wärme- oder Feuerverhältnisse.",
        "Während der Sonnen-zeit können wir nun deutlich das Folgende bemerken, wenn wir in der"
      ],
      [
        "Akasha-Chronik zurückschauen.",
        "Die Throne opfern, verbleiben bei ihrer Opfertätigkeit; so daß wir die opfernden Throne haben, haben auch eine Anzahl von Cherubim, zu denen wir das Opfer aufsteigen sehen, indem sie das, was aus dem Opfer fließt, die Wärme, in sich aufnehmen.",
        "Aber eine Anzahl von Cherubim vollzieht etwas anderes:"
      ],
      [
        "sie verzichten auf das Opfer, nehmen nicht an die Opferung.",
        "Daher müssen wir das Bild, das wir das letzte Mal vor unsere Seele treten ließen, noch etwas ergänzen."
      ],
      [
        "Wir haben in diesem Bilde die opfernden Throne und die das Opfer annehmenden Cherubim, wir haben aber auch solche Cherubim, die das Opfer nicht annehmen, sondern wieder zurückgeben, was als Opfer zu ihnen dringt.",
        "Das ist außerordentlich interessant in der Akasha-Chronik zu verfolgen."
      ],
      [
        "Denn dadurch, daß nun sozusagen die schenkende Tugend der Geister der Weisheit einfließt in die Opfer-wärme, dadurch sehen wir wie aufsteigend Opferrauch während der alten Sonne, von dem wir gesagt haben, daß er dann durch die Erz­engel in Form von Licht zurückgeworfen wird von dem äußersten Um­fange der Sonne.",
        "Aber nun sehen wir, wie wenn innerhalb des alten Sonnenraumes noch etwas ganz anderes vorhanden wäre: Opferrauch, der aber jetzt nicht bloß durch die Erzengel im Licht zurückgeworfen wird, sondern der von den Cherubim nicht angenommen wird, so daß er wie zurückfließt, sich zurückstaut, so daß wir dauernd Opferwolken im Raume haben: Opfer, das aufsteigt, Opfer, das absteigt, Opfer, das angenommen wird, Opfer, auf das ver­zichtet wird."
      ],
      [
        "Dieses Sich-Begegnen der eigentlichen spirituellen Wolkengebilde im alten Sonnenraum finden wir gleichsam zwischen dem, was wir das letzte Mal das Äußere und das Innere genannt haben, bis die Trennung geschieht, so daß wir in der Mitte haben die opfernden Throne, dann die Cherubim in der Höhe, die das Opfer annehmen, dann solche Cherubim, die das Opfer nicht annehmen, son­dern es zurückstauen.",
        "Durch dieses Zurückstauen entsteht gleichsam eine Ringwolke, und ganz außen haben wir die zurückgeworfenen Lichtmassen."
      ],
      [
        "Stellen Sie sich dieses Bild ganz lebendig vor: daß wir also diesen alten Sonnenraum haben, diese alte Sonnenmasse, gleichsam eine kosmische"
      ],
      [
        "Kugel, außerhalb welcher nichts vorzustellen ist, so daß wir nur den Raum uns zu denken haben bis zu den Erzengeln hin.",
        "Stellen wir uns weiter vor, daß wir in der Mitte diese Ringbildung aus den sich begegnenden angenommenen und zurückgewiesenen Opfern haben.",
        "Aus diesen angenommenen und zurückgewiesenen Opfern ent­steht innerhalb der alten Sonne etwas, was wir nennen können eine Verdoppelung der ganzen Sonnensubstanz, ein Auseinandergehen.",
        "Mit einer äußeren Figur zu vergleichen ist die Sonne in dieser alten Zeit nur, wenn wir sie vergleichen mit unserer jetzigen Saturngestalt: der Kugel, die von Ringen umgeben ist, indem diese sich stauenden Opfer-massen nach einwärts werfen, was in der Mitte ist, und das, was außen ist, wird wie eine Ringinasse außen angeordnet.",
        "So haben wir die Sonnensubstanz eigentlich in zwei Teile getrennt durch die Kraft der sich stauenden Opfergewalten.",
        "Was wird nun dadurch bewirkt, daß auf der Seite gewisser Cherubim ein solcher Verzicht auf das Opfer eintritt?"
      ],
      [
        "Es ist ein außerordentlich schwieriges Kapitel, dem wir uns da nähern, und Sie werden nur in langsamem Meditieren erfassen können, was in den Begriffen liegt, die jetzt auseinandergesetzt werden.",
        "Nur wenn man lange über die Begriffe, die gegeben werden, nachdenkt, wird man herausfinden, welche Realitäten diesen Begriffen zugrunde liegen.",
        "Die Resignation, von der wir gesprochen haben, müssen wir in Verbindung bringen mit etwas, dessen Entstehung wir auf den alten Saturn verlegt haben: mit der Entstehung der Zeit.",
        "Wir haben gesehen, daß mit den Geistern der Zeit, den Archai, die Zeit eigentlich erst auf dem alten Saturn entsteht, und daß es keinen Sinn hat, vor dem alten Saturn von einer «Zeit» zu sprechen.",
        "Nun liegt zwar eine Wieder­holung darin, aber wir können doch sagen: die Zeit dauert fort.",
        "«Dauern» ist schon ein Begriff, der die Zeit in sich enthält.",
        "Wenn also gesagt wird, «die Zeit dauert fort», so bedeutet das: Wenn wir in der Akasha-Chronik Saturn und Sonne betrachten, so finden wir auf dem Saturn die Entstehung der Zeit, und auf der Sonne, daß die Zeit auch vorhanden ist.",
        "Wenn nun alle Verhältnisse so fortgingen, wie wir sie in den beiden letzten Betrachtungen charakterisiert haben in bezug auf Saturn und Sonne, so würde die Zeit ein Element bilden für alles"
      ],
      [
        "Geschehen in der Evolution.",
        "Wir könnten uns die Zeit von keinem Geschehen in der Evolution wegdenken.",
        "Wir haben ja gesehen, daß die Geister der Zeit entstanden sind auf dem alten Saturn, und daß die Zeit allem eingepflanzt ist.",
        "Und alles, was wir in Bildern, in Imagi­nationen bisher über die Evolution gedacht haben, müssen wir uns mit der Zeit in Verbindung denken.",
        "Es war also nur geschehen, was wir angeführt haben: Opferung und schenkende Tugend.",
        "Das wäre alles der Zeit unterworfen gewesen.",
        "Nichts wäre nicht der Zeit unterworfen gewesen.",
        "Das heißt, es würde alles dem Entstehen und Vergehen, was ja der Zeit angehört, unterworfen sein."
      ],
      [
        "Diejenigen Cherubim nun, welche verzichtet haben auf das Opfer, auf das, was gleichsam im Opferrauch liegt, sie haben darauf verzich­tet aus dem Grunde, weil sie sich damit den Eigenschaften dieses Opferrauches entziehen.",
        "Und zu diesen Eigenschaften gehört vor allem die Zeit und damit Entstehen und Vergehen."
      ],
      [
        "In dem ganzen Ver­zicht der Cherubim auf das Opfer liegt daher ein den Zeitverhältnis­sen Entwachsen der Cherubim.",
        "Sie gehen über die Zeit hinaus, entzie­hen sich dem Unterworfensein unter die Zeit.",
        "Damit treffen sich gleichsam die Verhältnisse während der alten Sonnenentwickelung so, daß gewisse Verhältnisse, die in der geraden Linie vom Saturn aus weiter fortgehen, als Opferung und schenkende Tugend der Zeit un­terworfen bleiben, während die anderen Verhältnisse, die von den Cherubim dadurch eingeleitet wurden, daß diese Cherubim auf das Opfer verzichteten, sich der Zeit entreißen und die Ewigkeit, die Dauer, das Nichtunterworfensein dem Entstehen und Vergehen wäh­len."
      ],
      [
        "Das ist etwas höchst Merkwürdiges: wir kommen da während der alten Sonnenentwickelung zu einer Trennung in Zeit und Ewig­keit.",
        "Es ist durch die Resignation der Cherubim während der Sonnen-entwickelung die Ewigkeit errungen worden als eine Eigenschaft ge­wisser Verhältnisse, die während der Sonnenentwickelung eintraten."
      ],
      [
        "Sahen wir also, indem wir in unsere eigene Seele blickten, gewisse Wir­kungen aus dieser Seele dadurch erwachsen, daß der Mensch Verzicht und Resignation in der Seele sich aneignet, so sehen wir, wenn wir zunächst nur von der alten Sonne sprechen, daß von gewissen göttlich-geistigen Wesenheiten Unsterblichkeit, Ewigkeit dadurch errungen ist,"
      ],
      [
        "daß sie resignierten auf das Opfer und auf das, was aus der schenken­den Tugend und aus den sie verbreitenden Gaben kommen konnte.",
        "Sahen wir auf dem Saturn die Zeit entstehen, so sehen wir gewisse Verhältnisse sich der Zeit entreißen während der Sonnenentwickelung.",
        "Ich habe allerdings gesagt - ich bitte, das wohl zu beachten -, es be­reitet sich dies schon vor während der Saturnzeit, so daß die Ewigkeit nicht erst beginnt während der Sonnenzeit.",
        "Aber klar und deutlich zu sehen, so daß man es aussprechen kann in Begriffen, ist es erst wäh­rend der Sonnenzeit.",
        "Es ist auf dem Saturn so schwach erkennbar, dieses Abtrennen der Ewigkeit von der Zeit, daß unsere Begriffe und Worte sich nicht als scharf genug erweisen, um so etwas schon für den alten Saturn und seine Entwickelung zu charakterisieren."
      ],
      [
        "So haben wir die Bedeutung der Resignation kennengelernt, den Verzicht der Götter während der alten Sonnenzeit und die Erringung der Unsterblichkeit.",
        "Was war nun die weitere Folge davon?"
      ],
      [
        "Aus der «Geheimwissenschaft im Umriß», die in gewisser Beziehung noch in Maja bleiben muß, wissen wir, daß auf die Sonnenentwicke­lung die Mondentwickelung folgte, daß am Ende der Sonnenzeit alle Verhältnisse in eine gewisse Dämmerung, in ein gewisses kosmisches Chaos eintauchten und wieder als Mond auftauchten.",
        "So haben wir denn wieder auftauchen zu sehen die Opferung als Wärme.",
        "Also, was auch auf der Sonne blieb als Wärme, das sehen wir auch auf dem Monde als Wärme auftauchen.",
        "Was schenkende Tugend ist, sehen wir als Gas, als Luft auftauchen.",
        "Aber auch die Resignation dauert fort, der Verzicht auf die Opferung.",
        "Was wir «Resignation» nannten, ist in all diesem drinnen, was auf dem alten Monde vorgeht.",
        "Es ist wirklich so: was wir als Resignation erleben können, müssen wir uns ebenso in allem auf dem alten Monde denken, von der Sonne herübergekom­men, wie wir uns etwas anderes denken, was in der äußeren Welt vor­handen ist.",
        "Was Opfer war, erscheint als Wärme in der Maja; was schenkende Tugend war, erscheint in der Maja als Gas oder Luft.",
        "Was nun Resignation ist, das erscheint in der äußeren Maja als Flüssigkeit, als Wasser.",
        "Wasser ist Maja, und es wäre nicht da in der Welt, wenn nicht geistig zugrunde läge Verzicht oder Resignation.",
        "Überall, wo Wasser ist in der Welt, ist Götterverzicht!",
        "Ebenso wahr wie Wärme"
      ],
      [
        "eine Illusion ist, und wie dahinter das Opfer ist, wie Gas oder Luft eine Illusion ist, und dahinter die schenkende Tugend ist, so ist das Wasser als Substanz, als äußere Wirklichkeit nur eine sinnliche Illu­sion, ein Spiegelbild, und was im Wahrhaftigen davon existiert, ist Resignation irgendwelcher Wesenheiten für das, was sie von anderen Wesenheiten erhalten.",
        "Man möchte sagen, es kann nur Wasser in der Welt rieseln, wenn zugrunde liegt Resignation.",
        "Nun wissen wir, daß, während die Sonne zum Monde fortschritt, die Luftverhältnisse sich verdichteten zu den Wasserverhältnissen, Wasser entsteht erst auf dem Monde, auf der Sonne gab es noch kein Wasser.",
        "Was wir während der alten Sonnenentwickelung als sich ballende Wolkenmassen sehen, das gerinnt, indem es sich ineinanderdrängt zu einem Dichteren, zum Wasser, das auf dem Monde auftritt, zum Mondenmeere."
      ],
      [
        "Wenn wir dies ins Auge fassen, wird es uns immerhin möglich sein, eine Frage, die aufgeworfen werden kann, zu begreifen.",
        "Aus der Resignation wird Wasser; Wasser ist eigentlich in Wahrheit Resi­gnation.",
        "Wir bekommen also einen geistigen Begriff ganz sonderbarer Art für das, was das Wasser eigentlich ist.",
        "Aber wir können die Frage aufwerfen: Es ist doch ein gewisser Unterschied zwischen dem Zu­stande, der eingetreten wäre, wenn die Cherubim nicht resigniert hät­ten, und zwischen dem Zustande, der nun dadurch eingetreten ist, daß sie resigniert haben?",
        "Drückt sich dieser Unterschied in irgendeiner Weise aus? - Ja, das tut er.",
        "Er drückt sich nämlich dadurch aus, daß nunmehr während der Sonnenverhältnisse deutlich die Folgen jener Resignation auftreten.",
        "Wenn nämlich diese Resignation nicht einge­treten wäre, wenn die betreffenden verzichtenden Cherubim das ihnen gebrachte Opfer angenommen hätten, so hätten sie - jetzt bildlich ge­sprochen - den Opferrauch in ihrer eigenen Substanz drinnen gehabt; was sie selber getan hätten, das hätte sich in dem Opferrauch zum Ausdruck gebracht.",
        "Nehmen wir an, diese Cherubim hätten dieses oder jenes vollzogen.",
        "Dann wäre es erschienen, äußerlich ausgedrückt, durch die sich verändernden Wolken der Luft, das heißt, in der äuße­ren Gestalt der Luft würde sich ausgedrückt haben, was die nicht resignierenden Cherubim mit der Opfersubstanz gemacht hätten.",
        "Nun aber haben sie dieselbe zurückgewiesen und sind dadurch aus der"
      ],
      [
        "Sterblichkeit in die Unsterblichkeit, aus der Vergänglichkeit in die Dauer übergegangen.",
        "Aber die Opfersubstanz ist zunächst da, sie ist sozusagen entlassen aus den Kräften, die sie sonst aufgenommen hät­ten, und braucht jetzt nicht zu folgen den Antrieben, den Impulsen der Cherubim, denn diese haben sie entlassen, haben sie zurückgewie­sen."
      ],
      [
        "Was geschieht nun mit dieser Opfersubstanz? - Es geschieht das, daß andere Wesen sich ihrer bemächtigen, die dadurch, daß sie jetzt diese Opfersubstanz nicht in den Cherubim haben, von den Cherubim unabhängig werden, selbständige Wesen werden, die neben den Cheru­bim da sind, während sie sonst dirigiert werden von der Opfersub­stanz in den Cherubim drinnen, wenn diese die Opfersubstanz auf­genommen haben.",
        "Darauf beruht die Möglichkeit, daß das Gegenteil von Resignation eintritt: daß Wesenheiten die ausgeflossene Opfer-substanz an sich heranziehen und in ihr handeln."
      ],
      [
        "Und das sind die Wesenheiten, die zurückbleiben, so daß das Zurückbleiben eine Folge der Resignation der Cherubim ist.",
        "Die Cherubim liefern durch das, worauf sie resignieren, den zurückbleibenden Wesenheiten selbst erst die Möglichkeit zum Zurückbleiben."
      ],
      [
        "Dadurch, daß ein Opfer abgewie­sen wird, können andere Wesenheiten, die nicht resignieren, die den Wünschen und Begierden sich hingeben und ihre Wünsche zum Aus­druck bringen, sich des Gegenstandes des Opfers, der Opfersubstanz, bemächtigen und sind damit in der Möglichkeit, als selbständige We­senheiten neben die Opfernden hinzutreten."
      ],
      [
        "So ist mit dem Hinübergehen der Entwickelung von der Sonne zum Mond, mit dem Unsterblichwerden der Cherubim die Möglichkeit gegeben, daß andere Wesenheiten sich abtrennen in eigener Substan­tialität von der fortlaufenden Entwickelung der Cherubim, überhaupt der unsterblichen Wesenheiten.",
        "Wir sehen also, indem wir jetzt den tieferen Grund des Zurückbleibens kennenlernen, daß eigentlich die Urschuld, wenn wir von einer solchen Urschuld sprechen wollen, an diesem Zurückbleiben gar nicht diejenigen haben, welche zurück­geblieben sind.",
        "Das ist das Wichtige, daß wir das auffassen.",
        "Hätten die Cherubim die Opfer angenommen, so hätten die luziferischen Wesenheiten nicht zurückbleiben können, denn sie hätten keine Gele­genheit gehabt, sich in dieser Substanz zu verkörpern.",
        "Damit die"
      ],
      [
        "Möglichkeit vorhanden war, daß Wesenheiten in dieser Weise selb­ständig werden, trat vorher der Verzicht ein.",
        "Es ist also in der Welt-entwickelung so, daß die Götter sich ihre Gegner selbst hervorgerufen haben.",
        "Hätten Götter nicht verzichtet, so hätten sich Wesenheiten nicht widersetzen können.",
        "Oder wenn wir trivial sprechen wollen, können wir sagen, die Götter hätten gleichsam vorausgesehen: Wenn wir nur so fortschaffen, wie wir es getan haben vom Saturn zur Sonne herüber, so werden niemals freie, aus ihrer Willkür heraus handelnde Wesenheiten entstehen.",
        "Es muß, damit solche Wesenheiten entstehen können, die Möglichkeit gegeben sein, daß uns Gegner im Weltenall erstehen, daß wir Widerstände finden in dem, was der Zeit unterwor­fen ist.",
        "Würden wir nur selbst alles anordnen, so würden wir einen solchen Widerstand nicht finden können.",
        "Wir könnten es uns sehr leicht machen, dadurch daß wir alles Opfer annähmen, dann würde alle Evolution uns unterworfen sein.",
        "Das werden wir aber nicht ma­chen; wir wollen Wesenheiten, die sich widersetzen können.",
        "Daher nehmen wir das Opfer nicht an, so daß jene Wesenheiten durch unsere Resignation und dadurch, daß sie das Opfer nehmen, unsere Gegner werden!"
      ],
      [
        "So sehen wir, daß wir nicht bei den sogenannten bösen Wesenheiten den Grund des Bösen zu suchen haben, sondern bei den guten Wesen­heiten, die erst durch ihre Resignation bewirkt haben, daß durch die Wesenheiten, welche das Böse in die Welt bringen konnten, das Böse entstanden ist.",
        "Nun könnte jemand sehr leicht einwenden - und ich bitte, diesen Gedanken recht genau auf Ihre Seele wirken zu lassen -:"
      ],
      [
        "Ich habe bisher eine bessere Meinung von den Göttern gehabt!",
        "Ich habe bisher die Meinung von den Göttern gehabt, daß sie das, was menschliche Freiheit in Szene setzen sollte, auch bewirken könnten, ohne die Möglichkeit des Bösen zu schaffen.",
        "Wie kommt es, daß alle diese guten Götter so etwas wie die menschliche Freiheit nicht ohne das Böse in die Welt bringen konnten? - Ich möchte dabei erinnern an jenen spanischen König, der die Welt so furchtbar kompliziert gefun­den hat und der deshalb einmal gesagt hat: wenn Gott es ihm über­lassen hätte, die Welt zu schaffen, so würde er sie einfacher gemacht haben. - Der Mensch mag in seiner Schwäche denken, daß die Welt"
      ],
      [
        "einfacher gemacht werden könnte; aber die Götter wissen es besser, und sie haben es daher dem Menschen nicht überlassen, die Welt zu schaffen."
      ],
      [
        "Wir könnten vom Gesichtspunkt der Erkenntniswissenschaft aus diese Verhältnisse auch noch genauer charakterisieren.",
        "Nehmen wir an, es sollte irgend etwas gestützt werden, und man sagt jemandem, das könnte man so stützen, daß man eine Säule aufrichtet und die Sache draufrichtet."
      ],
      [
        "Da könnte der Betreffende dann sagen: Eigentlich müßte es auch anders zu machen sein! - Ja, warum sollte es nicht auch anders zu machen sein?",
        "Oder es könnte jemand sagen, wenn man bei einem Bau ein Dreieck braucht: Warum sollte dieses Dreieck nur drei Ecken haben?"
      ],
      [
        "Ein Gott könnte vielleicht ein Dreieck so machen, daß es nicht drei Ecken habe! - Aber so viel Sinn es hat, daß ein Dreieck nicht drei Ecken haben soll, so viel Sinn hätte es, daß die Götter die Freiheit hätten schaffen sollen ohne die Möglichkeit des Bösen und des Leides.",
        "Wie zum Dreieck drei Ecken gehören, so gehört zur Freiheit die Möglichkeit des Bösen durch die Resignation geistiger Wesenhei­ten."
      ],
      [
        "Das alles gehört zur Resignation der Götter, die dadurch die Evo­lution geschaffen haben aus dem Unsterblichen heraus, nachdem sie durch den Verzicht auf das Opfer den Grad zur Unsterblichkeit ge­nommen hatten, um das Böse wieder zurückzuführen zum Guten.",
        "Die Götter haben nicht vermieden das Böse, was allein die Möglichkeit der Freiheit geben konnte."
      ],
      [
        "Hätten die Götter das Böse vermieden, so wäre die Welt arm, wäre nicht mannigfaltig.",
        "Die Götter mußten das Böse um der Freiheit willen in die Welt kommen lassen, und sie mußten da­für für sich die Macht erringen, das Böse wieder in das Gute zurück­zuführen."
      ],
      [
        "Diese Macht ist etwas, was als Wirkung nur aus dem Ver­zicht, aus der Resignation kommen kann."
      ],
      [
        "Religionen sind immer dazu da, um sozusagen in Bildern, in Imagi­nationen auf die großen Weltengeheimnisse hinzuweisen.",
        "Wir haben heute auf uralte Entwickelungsphasen hingewiesen, und indem wir dem Begriff des Opfers und der schenkenden Tugend hinzufügten den Begriff der Resignation, haben wir dadurch wieder einen Schritt in das Wahrhaftige gegenüber der Maja und Illusion hinein gemacht.",
        "Solche Begriffe wurden den Menschen in den Religionen gegeben."
      ],
      [
        "es gibt etwas innerhalb der biblischen Religion, wodurch sich der Mensch aneignen kann den Begriff der Resignation, des Zurückwei­sens des Opfers.",
        "Das ist die Erzählung von dem opfernden Abraham, der seinen eigenen Sohn dem Gotte darbringen soll, und von dem Ver­zicht dieses Gottes auf das Opfer des Patriarchen.",
        "Wenn wir diesen Begriff des Verzichtes in unsere Seele aufnehmen, dann können solche Anschauungen in uns hineinkommen, wie wir sie schon geäußert haben.",
        "Einmal habe ich gesagt: Nehmen wir an, das Opfer des Abraham wäre angenommen und Isaak geopfert worden.",
        "Da von ihm das ganze alt­hebräische Volk abstammt, so hätte der Gott durch die Annahme des Opfers dieses ganze Volk von der Erde genommen.",
        "Alles, was von Abraham abstammte, schenkte der Gott durch den Verzicht einer Sphäre, die außerhalb seiner ist.",
        "Hätte er das Opfer angenommen, so hätte er damit die ganze Sphäre, die sich innerhalb des althebräischen Volkes abspielte, in sich aufgenommen, denn der geopferte Isaak wäre dann bei Gott gewesen.",
        "So aber hat er darauf verzichtet und damit diese ganze Evolutionslinie der Erde überlassen."
      ],
      [
        "Also die Begriffe der Resignation, des Opfers, können uns aufgehen bei dem bedeutungsvollen Bilde der Opferung des alten Patriarchen.",
        "Aber noch an einer anderen Stelle unserer irdischen Geschichte können wir dieses Resignieren höherer Wesenheiten finden, und auch da dür­fen wir wieder hinweisen auf etwas, worauf wir schon das letzte Mal hingewiesen haben: auf das Bild von Lionardo da Vinci, auf das «Abendmahl».",
        "Stellt es doch die Szene vor, wo wir gleichsam den Sinn der Erde vor uns haben, den Christus.",
        "Erinnern wir uns, indem wir den ganzen Sinn des Bildes durchdringen wollen, an jene Worte, die wir auch im Evangelium finden: «Könnte ich nicht ein ganzes Heer von Engeln herbeirufen, wenn ich entgehen wollte dem Opfertode?» Was in diesem Moment der Christus annehmen könnte, was ihm selbst­verständlich eine leichte Möglichkeit wäre, das wird in Resignation, in Verzicht zurückgewiesen.",
        "Und der größte Verzicht des Christus Jesus tritt uns da entgegen, wo er durch seinen Verzicht sich den Gegner selber in seine Sphäre kommen läßt: den Judas.",
        "Wenn wir in dem Christus Jesus dasjenige sehen, was wir in ihm sehen können, so müssen wir in ihm ein Abbild derjenigen Wesenheiten sehen, die wir"
      ],
      [
        "jetzt eben auf einer gewissen Entwickelungsstufe kennengelernt haben, derjenigen, die auf das Opfer verzichten mußten, derjenigen, deren Natur Resignation ist. - Der Christus resigniert auf das, was gesche­hen würde, wenn er nicht den Judas als seinen Gegner auftreten lassen würde, wie die Götter einst während der Sonnenzeit selber durch Resignation ihre Gegner hervorgerufen haben.",
        "So sehen wir diesen Vorgang wiederholt im Bilde auf der Erde: der Christus unter den Zwölfen, den Verräter in der Mitte, den Judas, so wie die Gegner der kosmischen Mächte auftraten."
      ],
      [
        "Damit das in die Entwickelung eintre­ten kann, was der Menschheit unendlich wert ist, muß sich der Chri­stus selbst seinem Gegner entgegenstellen.",
        "Weil wir an einen solchen kosmischen Augenblick erinnert werden beim Anblick des Abend­mahles, wenn wir uns die Worte vorhalten: «Wer mit mir den Bissen in die Schüssel tauchen wird, der wird mich verraten», weil wir da im irdischen Abbilde sehen den Gegner der Götter selbst den Göttern gegenübergestellt, deshalb macht dieses Bild einen so gewaltigen Ein­druck."
      ],
      [
        "Deshalb durfte ich oft sagen: Alles, was ein Marsbewohner sehen würde, wenn er heruntersteigen könnte auf die Erde, würde er vielleicht mehr oder weniger interessant finden, wenn er es auch nicht recht verstehen würde.",
        "Beim Anblick aber jenes Bildes von Lionardo da Vinci würde er aus einer Stelle des Kosmischen, die mit dem Mars ebenso zusammenhängt wie mit der Erde, etwas kennenlernen, woraus er den Sinn der Erde erkennen würde."
      ],
      [
        "Was da im irdischen Bilde ab­gebildet ist, das hat für den ganzen Kosmos eine Bedeutung: das Sich-Entgegenstellen gewisser Mächte den unsterblichen göttlichen Mäch­ten.",
        "Und indem inmitten seiner Apostel der Christus erscheint, der auf der Erde den Tod überwindet, also den Triumph der Unsterblichkeit zeigt, muß auf jenen bedeutungsvollen universellen Moment hinge­wiesen werden, der da eintrat, als sich überhaupt Götter absonderten vom zeitlichen Sein und den Sieg über die Zeit errangen, das heißt, un­sterblich wurden."
      ],
      [
        "Das kann unser Herz fühlen, wenn wir das «Abend­mahl» von Lionardo da Vinci anschauen."
      ],
      [
        "Sagen Sie nicht, daß der, welcher mit einem naiven Gemüte das «Abendmahl» anschaut, dies alles doch nicht weiß, was wir heute ge­sagt haben.",
        "Er braucht es nicht zu wissen.",
        "Denn darin besteht das geheimnisvolle"
      ],
      [
        "Tiefe der Menschenseele, daß man gar nicht mit dem Verstande zu wissen braucht, was die Menschenseele fühlt.",
        "Weiß die Blume die Gesetze, nach denen sie wächst?",
        "Nein, aber sie wächst darum doch.",
        "Was braucht die Blume die Gesetze, was die Menschen-seele einen Verstand, um zu fühlen das ganz unermeßlich Große, das vorhanden ist, wenn vor dem Auge sich ausbreitet ein Gott und sein Gegner, wenn das Höchste, das ausgedrückt werden kann, der Gegen­satz von Unsterblichem und Vergänglichem, vor uns steht?",
        "Das braucht man nicht zu wissen, das geht mit magischer Kraft in die Seele über, wenn der Mensch vor diesem Bilde steht, das als Spiegel des Weltensinnes uns da hingemalt ist.",
        "Und der Künstler brauchte auch nicht in demselben Sinne ein Okkultist zu sein, um es hinzumalen.",
        "Aber in der Seele des Lionardo da Vinci waren die Kräfte, die gerade dieses Höchste, Bedeutungsvollste zum Ausdruck bringen konnten.",
        "Deshalb wirken die großen Kunstwerke so ungeheuer, weil sie tief ver­bunden sind mit dem Sinn der Weltenordnung.",
        "In früheren Zeiten waren die Künstler verbunden mit dem Sinn der Weltenordnung in dumpfem Bewußtsein, ohne daß sie es wußten.",
        "Aber die Kunst würde ersterben, würde keine Fortsetzung erhalten, wenn nicht in Zukunft die Geisteswissenschaft als Wissen von diesen Dingen der Kunst eine neue Grundlage gäbe."
      ],
      [
        "Die unterbewußte Kunst hat ihre Vergangenheit und mit ihrer Ver­gangenheit ein Ende erreicht.",
        "Die Kunst, welche sich von der Geistes­wissenschaft inspirieren läßt, steht im Beginn, im Ausgange.",
        "Das ist die Kunst der Zukunft.",
        "So wahr es ist, daß der alte Künstler nicht zu wissen brauchte, was den Kunstwerken zugrunde liegt, so wahr ist es, daß es der zukünftige Künstler wissen muß, aber mit jenen Kräften, die wieder eine Art des Unendlichen darstellen, die wieder etwas aus dem Vollinhaltlichen der Seele darstellen.",
        "Denn der hat nicht die Geisteswissenschaft, der sie wieder zu einer Verstandeswissenschaft macht, sondern der hat sie, der bei jedem Begriff, den wir ent­wickeln - Opfer, schenkende Tugend, Resignation -, der bei jedem Worte etwas empfinden kann, was das Wort, was die Idee selbst zer­sprengen will, was höchstens in die Vieldeutigkeit der Bilder aus­fließen kann."
      ],
      [
        "Schemen wird man hinstellen können, wenn man glaubt, die Ent­wickelung der Welt vollziehe sich in abstrakten Begriffen.",
        "Es geht schon nicht mehr gut mit Schemen, wenn man lebendige Begriffe, wie Opferung, schenkende Tugend und Resignation hinstellen will; da müssen wir schon solche Bilder vor uns hinmalen, wie wir sie die letzten Male beschrieben haben: die opfernden Throne, die ihr Opfer hinaufsenden zu den Cherubim, der sich verbreitende Opferrauch, die das Licht zurückwerfenden Erzengel und so weiter.",
        "Und wenn wir das nächste Mal zum Mondendasein übergehen, werden wir sehen, wie das Bild reicher wird, wie tatsächlich etwas wird hinzutreten müssen wie die Verflüssigung der sich stauenden Wolkenmassen, die rieseln als Regenmassen, und das Dazutreten der zuckenden Blitze der Seraphim.",
        "Da müssen wir zu reicheren Vorstellungen übergehen, gegenüber denen man sagen wird: Die Zukunft der Menschheit wird schon die Möglich­keit finden, auch das künstlerische Material, die künstlerischen Mittel herbeizuschaffen, um für die äußere Welt zum Ausdruck zu bringen, was sonst nur in der Akasha-Chronik zu lesen sein kann."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG Berlin, 21. November 1911",
    "paragraphs": [
      "Ein schwieriges Kapitel unserer Weltanschauung haben wir nun so weit gebracht, daß wir hinter den Erscheinungen der äußeren Sinnes-welt zum Teil erblicken gelernt haben Geistiges. Von solchen Erschei­nungen, die zunächst äußerlich wenig davon verraten, daß Geistiges in der eigentümlichen Form, wie wir dieses Geistige in unserem eigenen Seelenleben erfahren, dahintersteht, von solchen Erscheinungen haben wir erkannt, daß dennoch geistige Betätigungen, geistige Qualitäten und Eigenschaften dahinterstehen. Was uns so zum Beispiel im ge­wöhnlichen Leben als wärmehafte Eigenschaft erscheint, als Wärme oder Feuer, das erkannten wir als den Ausdruck des Opfers. In dem, was als Luft uns entgegentritt und wieder zunächst so wenig verrät, wenigstens für unsere Begriffe, daß es geistig ist, darin erkannten wir dasjenige, was wir die schenkende Tugend besonderer Weltenwesen nannten. Und im Wasser haben wir das erkannt, was Resignation, Verzicht genannt werden kann.",
      "Jn früheren Weltanschauungen - darauf sei nur nebenbei aufmerk­sam gemacht - hat man natürlich schon eher in dem äußeren Stoff­lichen das Geistige geahnt und erkannt, wofür ein Beweis sein kann, daß man besonders fluchtige Stoffe mit dem Worte «Spiritus » be­zeichnet hat, das wir heute in eigenschaftlicher Bedeutung anwenden auf das Geistige, indem wir sagen «spirituell»; und in der äußeren Welt kann es ja vorkommen, daß die Menschen dieses «spirituell» noch so wenig auf das Geistige beziehen, auf das Übersinnliche, daß einmal, wie einzelnen von Ihnen bekannt sein wird, als an einen Münchener Spiritistenverein ein Brief adressiert worden ist und man nicht wußte, was das ist, ein Spiritistenverein, man diesen Brief dem Vorsitzenden des Zentralverbandes der Spirituosenhändler aushändigte.",
      "Indem wir nun heute jenen bedeutungsvollen Übergang betrachten wollen, der sich in der Evolution des Erdenplaneten vollzogen hat von der alten Sonne zum alten Mond herüber, werden wir eine andere Art der Entwickelung des Geistigen ins Auge fassen müssen. Wir werden",
      "aber ausgehen müssen von dem, was uns das letzte Mal entgegen­getreten ist als der Verzicht. Da haben wir gesehen, daß dieser Ver­zicht im wesentlichen darin besteht, daß geistig hochstehende Wesen­heiten verzichteten auf die Entgegennahme des Opfers, was ja, wie wir erkannt haben, im wesentlichen das Opfer des Willens oder der Willenssubstanz ist. Wenn wir uns dies so vorstellen, daß gewisse Wesenheiten das opfern wollen, was ihre Willenssubstanz ist, und ihnen durch den Verzicht höherer Wesenheiten sozusagen verweigert wird die Entgegennahme dieses Willens, dann werden wir uns leicht zu dem Begriff erheben können, daß dann jene Willenssubstanz, welche die betreffenden Wesenheiten eigentlich höheren geistigen We­senheiten opfern wollten, zurückbleiben muß in den betreffenden Wesenheiten, welche opfern wollen und nicht opfern können. So sind uns damit ohne weiteres im Weltenzusammenhange gegeben Wesen­heiten, welche bereit sind, ihr Opfer darzubringen, also in einer ge­wissen Weise bereit sind, das, was in ihrem Inneren ruht, inbrünstig hinzugeben, aber es nicht können und daher in sich behalten müssen. Oder anders ausgedrückt bedeutet es, daß diese Wesenheiten eine ge­wisse Verbindung mit höheren Wesenheiten, die sich ihnen ergeben hätte, wenn sie hätten opfern dürfen, durch die Zurückweisung des Opfers nicht haben können.",
      "In weltgeschichtlich symbolischer Weise tritt uns das entgegen, was wir dabei ins Auge fassen sollen - aber es ist dort verschärft - in dem Kain, der dem Abel gegenübersteht. Auch Kain will sein Opfer hinauf-senden zu seinem Gott. Sein Opfer aber ist nicht wohlgestaltet, und der Gott nimmt es nicht auf. Das Opfer Abels nimmt er auf. Was wir dabei ins Auge fassen wollen, ist das innere Erlebnis, das dabei zu­stande kommen kann, daß Kain sein Opfer zurückgewiesen findet. Wenn wir uns zu der Höhe der Auffassung erheben wollen, die dabei in Betracht kommt, so müssen wir uns klarmachen, daß wir bei den Regionen, von denen wir hier sprechen, Begriffe, die bloß eine Bedeu­tung in unserem gewöhnlichen Leben haben, hineinschleppen in die höheren Regionen. Es wäre falsch, wenn man davon sprechen würde, daß durch eine Schuld oder ein Unrecht die Zurückweisung des Opfers zustande käme. Von Schuld oder Sühne, wie wir sie in unserem",
      "jetzigen gewöhnlichen Leben kennen, darf in diesen Regionen noch nicht die Rede sein. Wir müssen diese Wesenheiten vielmehr so be­trachten, daß es von seiten der höheren Wesenheiten, welche das Opfer zurückwiesen, ein Verzicht, eine Resignation ist.",
      "In dem, was wir vor acht Tagen als Seelenstimmung charakterisierten, liegt nichts, was Schuld oder Unterlassung ist, sondern es liegt darin alles Große und Bedeutungsvolle, was in einem Verzicht, in einer Resignation lie­gen kann. Das bleibt aber dabei doch bestehen, daß die anderen We­senheiten, welche das Opfer haben bringen wollen, in sich eine Stim­mung erzeugen müssen, von der wir fühlen können, daß damit etwas beginnt wie eine, wenn auch außerordentlich leise Gegnerschaft gegen jene Wesen, welche die Opfer zurückweisen.",
      "Deshalb ist dies in bezug auf Kain, wo es in einer späteren Zeit uns vorgeführt wird, in ver­schärftem Maße dargestellt. Wir werden daher nicht dieselbe Stim­mung, die wir bei Kain finden, bei denjenigen Wesenheiten antreffen, die sich von der Sonne zum Mond herüberentwickeln; wir werden diese Stimmung bei ihnen in einem anderen Maße antreffen.",
      "Und wir lernen die Stimmung, die sich da geltend macht, nur kennen, wenn wir, wie wir es in den letzten Vorträgen getan haben, wieder in unsere eigene Seele blicken und uns fragen, wo wir in der eigenen Seele eine solche Stimmung finden können, die uns andeuten kann, wie die Stim­mung ist, die sich entwickeln müßte in den Individualitäten, deren Opfergaben zurückgewiesen worden sind.",
      "Diese Stimmung in uns - und wir kommen da immer näher und näher dem irdischen Menschenleben -, die jede Seele schon kennt in ihrer Unbestimmtheit und zugleich in ihrer quälenden Weise in der Art, die wir voll rechnen können zu dem, was am nächsten Don­nerstage im öffentlichen Vortrage «Die verborgenen Tiefen des Seelen­lebens» zu besprechen sein wird, diese Stimmung, die jede Seele kennt als waltend in den verborgenen Tiefen des Seelenlebens, sie dringt zu­weilen herauf an die Oberfläche unseres Seelenlebens; dann ist sie vielleicht am wenigsten quälend. Aber wir Menschen gehen mit dieser Stimmung oftmals herum, ohne daß wir uns derselben in unserein Oberbewußtsein recht klar bewußt sind, und wir haben sie doch in uns. Man möchte an das Dichterwort erinnern, um so recht das Quälerische,",
      "das mit der Nuance des Schmerzes Verbundene daran hervor­zuheben: «Nur wer die Sehnsucht kennt, weiß, was ich leide.» Ge­meint ist die Sehnsucht als Seelenstimmung, Sehnsucht, wie sie lebt in den Seelen der Menschen.",
      "Um uns hineinzuversetzen in das, was geistig in der Entwickelungs-phase des alten Saturn und der Sonne vorging, war notwendig, daß wir zu besonderen Seelenzuständen unseren Blick erhoben, die sozu­sagen erst eintreten, wenn die menschliche Seele strebend wird, wenn sie sich hinauforganisiert zu einem höheren Streben. Das haben wir gesehen, als wir versuchten, uns die Natur des Opfers aus unserem eigenen Seelenleben heraus klarzumachen, versuchten, uns klarzuma­chen, was der Mensch erlangt als Weisheit, die wir hineinträufeln sehen und die entsteht aus dem, was man nennen könnte: Bereitschaft zu geben, bereit sein dazu, sich selber sozusagen hinzugeben. Indem wir so zu mehr irdischen Verhältnissen heraufkommen, die sich aus früheren entwickelt haben, treffen wir eine Seelenstimmung, die ähn­lich ist manchem, was der Mensch heute noch erleben kann. Nur müs­sen wir uns klar sein, daß alles Leben unserer Seele, insofern unsere Seele in den Erdenleib eingefügt ist, eine obere Schicht legt über ein verborgenes Seelenleben, das unten in den Tiefen abläuft. Wer sollte denn nicht wissen, daß es ein solches verborgenes Seelenleben gibt? Das Leben belehrt uns hinlänglich darüber, daß es ein solches gibt.",
      "Nehmen wir nun einmal an, um uns etwas von diesem verborgenen Seelenleben klarzumachen, ein Kind habe vielleicht in seinem sieben-ten oder achten Jahre oder in einer anderen Lebenszeit dieses oder jenes erfahren; es habe zum Beispiel erfahren, wofür Kinder sehr häu­Fig ganz besonders empfänglich sind, Ungerechtigkeit - Ungerechtig­keit, indem es beschuldigt wurde, dies oder jenes getan zu haben, was es in Wahrheit nicht getan hat, aber die Bequemlichkeit der Umge­bung des Kindes habe, um wenigstens mit der Sache fertigzuwerden, das Kind beschuldigt, dies oder jenes getan zu haben. Kinder haben ein ganz besonders reges Empfinden dafür, wenn ihnen in dieser Weise eine Ungerechtigkeit zugefügt wird. Aber, wie das Leben nun ist, nachdem sich dieses Erlebnis tief eingefressen hat in das kindliche Le­ben, legt das spätere Leben die anderen Schichten des Seelendaseins",
      "darüber, und das Kind hat für alles, was das Alltagsleben betrifft, ein Vergessen. Es könnte nun auch sein, daß eine solche Sache niemals wie­der auftauchen würde. Aber nehmen wir jetzt an: im fünfzehnten, sechzehnten Jahre erfährt das Kind, sagen wir in der Schule, eine neue Ungerechtigkeit.",
      "Und jetzt wird das wirksam, was sonst tief un­ten in der wogenden Seele ruht. Das Kind braucht es gar nicht einmal zu wissen, kann sich ganz andere Vorstellungen und Begriffe bilden, als zu wissen, daß heraufwirkt eine Reminiszenz dessen, was es in früheren Jahren erlebt hat.",
      "Wäre das aber, was früher vorgegangen ist, nicht geschehen, so würde es, wenn zum Beispiel das Kind ein Junge ist, nach Hause gehen, ein bißchen weinen, vielleicht auch ein bißchen schimpfen, es würde aber darüber hinweggehen. So aber ist jenes frühere Ereignis geschehen - und ich betone ausdrücklich, daß das Kind nicht zu wissen braucht, was da vorgekommen ist -, und das wirkt, wirkt unter der Oberfläche des Seelenlebens, wie unter dem glatt ausschauenden Meeresspiegel die Wogen aufgerührt werden kön­nen.",
      "Und aus dem, was sonst vielleicht ein Weinen, ein Klagen oder ein Schimpfen geworden wäre, wird nun ein Schülerselbstmord! So spielen die verborgenen Tiefen des Seelenlebens herauf aus den Unter­gründen.",
      "Und die wichtigste Kraft, die da unten waltet, die bei jeder Seele waltet und zuweilen heraufdringt in ihrer ureigenen Gestalt, aber am bedeutsamsten ist, wenn sie so heraufdringt, daß sich der Mensch ihrer nicht bewußt ist, das ist die Sehnsucht. Wir kennen auch die Namen, welche diese Kraft für die äußere Welt hat, die aber doch nur metaphorische, unbestimmte Namen sind, weil sie Beziehungen ausdrücken, die kompliziert sind und so überhaupt nicht ins Bewußt­sein heraufkommen.",
      "Nehmen Sie eine Erscheinung, die Sie alle kennen - der Stadt-mensch vielleicht weniger, aber er hat sie doch bei anderen erfahren -, eine Erscheinung, die man mit «Heimweh» bezeichnet. Wenn Sie nachgehen würden, was das Heimweh in Wirklichkeit ist, so würden Sie sehen, daß es im Grunde genommen bei jedem Menschen ein an­deres ist. Bald ist es so, bald so. Bald sehnt sich der Betreffende nach den traulichen Erzählungen, die er im Elternhause gehört hat; er weiß nicht, daß er sich nach Hause sehnt, was in ihm lebt, ist ein unbestimmter",
      "Drang, ein unbestimmtes Wollen. Ein anderer sehnt sich nach seinen Bergen oder nach dem Fluß, an dem er so oft gespielt hat, wenn vor ihm Wogen spielten. Was da wirkt, dessen ist sich der Mensch oft wenig bewußt, aber wir fassen alle diese verschiedenen Eigenschaften zusammen unter dem «Heimweh», etwas ausdrückend, was unter tausendfältiger Verschiedenheit spielen kann, und was doch am besten getroffen ist, wenn wir sie als eine Art Sehnsucht kenn­zeichnen. Aber was ist diese Sehnsucht? Wir haben es eben ausgespro­chen, daß sie eine Art von Wille ist, und überall, wo wir die Sehn­sucht prüfen, können wir sehen, daß es eine Art von Wille ist. Aber was für ein Wille? Es ist ein Wille, der so, wie er zunächst ist, nicht befriedigt werden kann, denn wird er befriedigt, so hört die Sehnsucht auf. Ein sich nicht ausleben könnender Wille ist es, was wir als Sehn­sucht bezeichnen.",
      "So etwas müssen wir als Stimmung bei denjenigen Wesenheiten be­zeichnen, deren Opfer zurückgewiesen worden ist. Was wir in den Tiefen unseres Seelenlebens wahrnehmen können, das ist uns geblieben als ein Erbstück von jenen alten Zeiten, von denen wir jetzt sprechen. Wie wir anderes als Erbstücke der alten Entwickelungsstadien haben, so sind uns geblieben von der Entwickelungsphase, von der wir hier sprechen, alle Arten von Sehnsucht, von nicht zu befriedigendem Wil­len, von zurückgehaltenem Willen. So haben wir uns auch zu denken, daß durch das Zurückweisen des Opfers während dieser Ent­wickelungsphase Wesen entstehen, die wir nennen können: Wesen mit zurückgehaltenem Willen. Dadurch, daß sie diesen zurückgehaltenen Willen in sich haben mußten, waren sie in einer ganz besonderen Lage. Und man muß sich wieder in eigene Seelenzustände versetzen - denn die Gedanken erreichen kaum diese Zustände -, wenn man diese Dinge nachfühlen, nachempfinden will.",
      "Das Wesen, das seinen Willen hinopfern kann, geht auf in gewisser Beziehung in dem anderen Wesen. Auch das kann man fühlen im Menschenleben, wie man lebt und webt in einem Wesen, dem man Opfer bringt, wie man sich befriedigt und glücklich fühlt, wenn man dem Wesen gegenüberstehen kann, dem man Opfer bringt. Und weil wir hier sprechen von der Opferung an höhere Wesen, an umfassendere,",
      "universelle Wesenheiten, zu denen hinaufzuschauen die opfern­den Wesen als ihre höchste Seligkeit empfinden müssen, so kann, was da zurückbleibt als zurückgehaltene Willenssehnsucht, nimmermehr dasselbe sein an innerer Stimmung, an innerem Seelengehalt als das, was sie erleben dürften, wenn sie opfern dürften. Denn wenn sie opfern dürften, wäre das Opfer bei den anderen Wesen. Wir dürfen gleichsam den Vergleich gebrauchen: wenn die Erde und die anderen Planeten der Sonne opfern dürften, dann wären sie bei der Sonne. Wenn sie nicht der Sonne opfern dürften, wenn sie zurückhalten müßten, was sie sonst opfern könnten, dann sind sie in sich selber zurückgedrängt.",
      "Wenn wir das fassen, was jetzt eben mit einem Worte ausgesprochen ist, dann merken wir, daß da etwas ins Weltall hineinkommt. Fassen Sie es klar, daß es nicht anders ausgesprochen werden kann: die We­sen, die einem anderen Wesen opfern, das in ihnen allen lebt, sie sind jetzt, wenn das Opfer nicht angenommen wird, darauf angewiesen, es selbst in sich zu tragen. Spüren Sie nicht, daß da etwas hereinblitzt, was man Egoität nennt, was als Egoität in allen Formen heraus­kommt? In dieser Weise ins Auge gefaßt, muß man fühlen, was - spä­ter sozusagen in die Entwickelung hineingegossen - als ein Erbstück nachlebt in den Wesen. Als die Sehnsucht sehen wir den Egoismus aufblitzen in der schwächsten Gestalt, aber wir sehen ihn sich hinein-schleichen in die Weltentwickelung. Und so sehen wir, wie die Wesen, die sich sich selbst, ihrer Egoität, hingeben werden, in einer gewissen Beziehung verdammt werden zur Einseitigkeit, zum bloßen Leben nur in sich selber, wenn nicht etwas anderes eintreten würde.",
      "Stellen wir uns einmal ein Wesen vor, das opfern darf: das lebt in dem anderen Wesen, und es lebt immer in dem anderen. Ein Wesen, das nicht opfern darf, kann nur in sich selber leben. Dadurch ist es ausgeschlossen von dem, was es in den anderen und in diesem Falle in den höheren Wesen erleben dürfte. Die Evolution würde schon in diesem Falle die entsprechenden Wesen in die Einseitigkeit hineinver­dammen und -verbannen, wenn nicht etwas einträte, was da in die Entwickelung hineinfällt und was die Einseitigkeit hinwegbewegen will. Das ist das Eintreten neuer Wesenheiten, welche die Einseitigkeit hintanhalten. Wie auf dem Saturn Willenswesen, wie auf der Sonne",
      "Weisheitswesen, so sehen wir auf dem Monde die Geister der Bewegung auftreten, wobei wir aber nicht räumliche Bewegung uns vorzustellen haben, sondern wobei wir «Bewegung» so fassen müssen, daß sie einen mehr gedanklichen Charakter trägt. Jeder kennt den Ausdruck «Denkbewegung», obwohl das nur der Ablauf der Flüssigkeit der eige­nen Gedanken ist; aber daraus schon werden Sie sehen, daß, wenn wir uns einen umfassenderen Begriff der Bewegung aneignen wollen, wir zur Erklärung der Bewegung zu etwas anderem als der bloßen Ortsbewegung, die nur eine einzelne Gattung der gesamten Bewegung darstellt, greifen müssen. Wenn viele Menschen einem höheren Wesen hingegeben sind, das sich gleichsam in ihnen allen ausdrückt, das von ihnen allen Opfer entgegennimmt, so leben diese Vielen mit dem Einen und sind darin befriedigt. Wenn aber die Opfer zurückgewiesen wer­den, so leben die Vielen in sich selber und können nicht befriedigt werden. Da treten die Geister der Bewegung ein und führen gleich­sam die Wesen, welche sonst nur auf sich angewiesen wären, zu allen anderen Wesenheiten in einer gewissen Weise hin, bringen sie zu den anderen in eine Beziehung. Die Geister der Bewegung sind zunächst nicht nur als ortsverändernde Wesen zu denken, sondern sie sind solche Wesen, die etwas hervorbringen, wodurch ein Wesen in immer neue Beziehungen zu anderen Wesen tritt.",
      "Man kann sich eine Vorstellung machen von dem, was jetzt damit auf dieser Stufe im Kosmos erlangt ist, wenn man wieder auf eine ent­sprechende Seelenstimmung reflektiert. Wer weiß nicht, was Sehnsucht ist, was ein ganz Reguläres ist, wenn ein Seelenzustand naht, wenn er bleibt, wenn er gar keine Veränderung erleben darf? Wer weiß nicht, wie quälend es wird und den Menschen in einen Zustand bannt, der ihm unerträglich wird, der dann bei den flachköpfigen Menschen zu dem wird, was man «Langeweile» nennt? Aber von dieser Langeweile, die man gewöhnlich nur den flachköpfigen Menschen zuschreiben kann, gibt es alle möglichen Zwischenstufen bis zu denen, welche den großen, edlen Naturen eigen sind, in denen das lebt, was ihre eigene Natur als Sehnsucht ausbrütet, und was nicht befriedigt werden kann in der Welt. Und wodurch wird die Sehnsucht mehr befriedigt als durch Veränderung? Der Beweis dafür ist, daß diese Menschen die",
      "Beziehungen suchen zu immer neuen und neuen Wesenheiten. Die Qual der Sehnsucht wird oft überwunden durch das, was veränderte Beziehungen sind zu immer neuen Wesenheiten.",
      "Da sehen wir, als die Erde ihre Mondenphase durchmacht, wie die Geister der Bewegung in das Leben der sich sehnenden Wesen, die sonst veröden würden - und Langeweile ist auch eine Art von Ver­ödung -, die Veränderung, die Bewegung hineinbringen, die Beziehung zu immer neuen und neuen Wesenheiten oder zu immer neuen und neuen Zuständen. Die räumliche, örtliche Bewegung ist nur eine Gat­tung dieser umfassenderen Bewegung, von der wir jetzt gesprochen haben. Eine Bewegung haben wir, wenn wir in der Lage sind, am Mor­gen einen bestimmten Gedankeninhalt in der Seele zu haben, diesen aber nicht zu behalten brauchen, sondern zu anderem übergehen kön­nen. Da überwinden wir die Einseitigkeit in der Sehnsucht durch die Mannigfaltigkeit, durch die Veränderung und die Bewegung des Erleb­ten. Im Raume draußen haben wir nur eine besondere Art dieser Ver­änderung.",
      "Denken wir uns dazu einen Planeten, der einer Sonne gegenüber­steht. Würde er immer in derselben Stellung gegenüber der Sonne sein, würde er sich nicht bewegen, so würde er bei jener Einseitigkeit blei­ben, die sich nur ergeben kann, indem er eben nur immer die eine Seite der Sonne zuwendet. Da kommen die Geister der Bewegung, führen den Planeten herum, um Veränderung hineinzubringen in seinen Zu­stand. Ortsveränderung ist nur eine Art der Veränderung überhaupt. Und indem die Geister der Bewegung die Ortsveränderung hineinbrin­gen in den Kosmos, bringen sie nur ein Spezifikum hinein in das, was die Bewegung im allgemeinen ist.",
      "Dadurch aber, daß die Geister der Bewegung in das Weltall, wie wir es bisher kennengelernt haben, die Bewegung und die Veränderung hineinbringen, muß noch etwas anderes hineinkommen. Wir haben gesehen, daß in dieser Evolution, in der ganzen kosmischen Mannig­faltigkeit, die sich da heraufentwickelt als die Geister der Bewegung, Geister der Persönlichkeit, Geister der Weisheit, des Willens und so weiter, auch dasjenige lebt, was wir genannt haben «schenkende Tugend», was als Weisheit ausgestrahlt wird und als Geistiges der",
      "Luft, der Gasströmung zugrunde liegt. Das fließt nun mit dem in Sehnsucht umgestalteten Willen zusammen und wird in diesen Wesen­heiten das, was der Mensch nun kennt - noch nicht als Gedanken, sondern als Bild. Am besten vergegenwärtigen wir uns das an dem Bilde, das der Mensch hat, wenn er träumt. Das flüssige Bild des Traumes kann eine Vorstellung hervorrufen von dem, was bei einem Wesen geschieht, in dem der Wille der Sehnsucht lebt und von den Geistern der Bewegung in eine Beziehung zu anderen Wesen geführt wird. Und indem es zu dem anderen Wesen gebracht wird, kann es ja nicht ganz sich hingeben, da die eigene Egoität in ihm lebt. Aber es kann das flüchtige Bild des anderen aufnehmen, das lebt wie ein Traumbild in ihm. Daher das, was wir nennen können das «Aufstei­gen der Bilder der anderen Welt». Das Aufsteigen des Bilderbewußt­seins sehen wir während dieser Phase der Entwickelung heraufkom­men. Und indem wir Menschen selber noch ohne unser heutiges Erden-Ich-Bewußtsein diese Phase der Entwickelung durchgemacht haben, müssen wir uns vorstellen, daß wir während dieser Entwickelungs-phase dasjenige, was wir durch unser Ich erlangen, noch nicht haben, daß wir da wesen und weben im Weltall, indem in uns etwas lebt, was wir uns heute nur vergegenwärtigen können, wenn wir die Sehnsucht kennen.",
      "Wir könnten in einer gewissen Weise, wenn wir nicht solche Lei­denszustände ins Auge fassen, wie es die irdischen sind, uns vorstellen, daß sie gar nicht sein könnten, wenn wir folgendes bedenken. In ge­wisser Weise kommt Leid, Schmerz, in seiner seelischen Gestalt natür­lich, in der damaligen Zeit auch in unsere Wesenheiten und in die Wesenheiten anderer Wesen hinein, die mit unserer Evolution verbun­den sind. Und erfüllt wird durch die Tätigkeit der Geister der Bewe­gung das sonst leerbleibende Innere, das von Sehnsucht leidende Innere mit dem Balsam, der in Form des Bilderbewußtseins hinein sich ergießt in diese Wesenheiten. Sonst wären diese Wesenheiten leer in ihrer Seele, leer von jeglichem anderen, was nicht Sehnsucht zu nennen Ware. Aber hinein träufelt der Balsam der Bilder, welche die Öde und Leerheit mit Mannigfaltigkeit ausfüllen und die Wesen so hinwegführen über das Verbannt- und Verdammtsein.",
      "Wenn wir solche Worte ernst nehmen, haben wir zu gleicher Zeit das, was geistig zugrunde liegt dem, was sich während der Mond­phase unserer Erde entwickelt hat, und was wir jetzt, weil sich da übergelagert hat die Erdenphase unseres Wesens, in den tiefen Unter­gründen unseres Bewußtseins haben. Aber wir haben es - und in einer populären Weise soll das übermorgen im öffentlichen Vortrage gezeigt werden - so in den Untergründen unserer Seele, daß es, wie das, was unten wirbelt unter der Oberfläche des Meeres und nach oben Wellen treibt, sich abspielen kann, ohne daß man weiß, was die Gründe dessen sind, was dann ins Bewußtsein eintritt. Unter der Oberfläche unseres gewöhnlichen Ich-Bewußtseins haben wir ein solches Seelenleben, das da heraufspielen kann. Und was sagt dieses Seelenleben dem Men­schen, wenn es heraufspielt? Wenn wir ins Auge fassen den kosmischen Untergrund dieses unterbewußten Seelenlebens, so können wir sagen:",
      "Das Seelenleben, das wir so heraufkommen spüren aus seelischen Un­tergründen, ist ein Heraufschlagen dessen, was sich da aus der Monden­phase der Entwickelung hineinbewegt hat in das, was während der Erdenphase selbst in uns hineingekommen ist. Und wenn wir so recht ins Auge fassen, was während der Erdennatur in uns hineingekommen ist, dann haben wir so richtig einen Grund dessen, was von dem alten Monde geistig herübergeführt hat zum Erdendasein.",
      "Fassen Sie ins Auge, daß es, wie wir es charakterisiert haben, not­wendig war, daß immer Bilder auftauchen mußten, die eine Öde zu befriedigen hatten. Dann kommt Ihnen ein Begriff von einem schwe­ren Gewicht, von einer großen Bedeutung: die sehnende Menschen-seele in ihrer sehnsuchtvollen Leerheit, die diese Sehnsucht befriedigt oder harmonisiert erhält durch das Hereinspielen von Bildern, die wieder nur an die Stelle von anderen Bildern treten können. Und wenn die Bilder da sind und eine Weile dagewesen sind, dann dämmert sie wieder auf aus den Untergründen, die alte Sehnsucht, und nach neuen Bildern führen sie die Geister der Bewegung. Und sind die neuen Bilder wieder eine Weile dagewesen, so schlägt die Sehnsucht wieder an nach neuen Bildern. Und das gewichtige Wort müssen wir aussprechen in bezug auf solches Seelenleben: Wenn die Sehnsucht nur befriedigt wird durch Bilder, welche den Bildern nachjagen, so ist das",
      "die fortfließende Unendlichkeit ohne Ende. Da hinein kann nur das kommen, was kommen muß, wenn an die Stelle der in die Unendlich­keit fortfließenden Bilder etwas tritt, was die Unendlichkeit erlösen kann durch etwas anderes als bloß durch Bilder, nämlich durch Reali­täten. Das heißt mit anderen Worten: diejenige planetarische Verkör­perung unserer Erde, in der wir durchgemacht haben, daß die Bilder herbeigeführt werden durch die Tätigkeit der Geister der Bewegung, sie muß abgelöst werden von derjenigen planetarischen Phase der Erdenverkörperungen, welche wir die Phase der Erlösung nennen müs­sen. Und wir werden noch sehen, daß die Erde der «Planet der Erlö­sung» zu nennen ist, wie wir die vorherige Verkörperung der Erde, das Mondendasein, den «Planeten der Sehnsucht» nennen können, der zwar zu stillenden Sehnsucht, die aber in eine nie endende Unendlich­keit ausläuft. Und während wir leben im Erdenbewußtsein - das uns, wie wir gesehen haben, durch das Mysterium von Golgatha die Er­lösung bringt -, steigt herauf während dieses Lebens aus den Unter­gründen unserer Seele das, was fortwährend nach Erlösung verlangt. Es ist, wie wenn wir oben die Wellen des gewöhnlichen Bewußtseins hätten, und unten in den Tiefen des Meeres des Seelenlebens lebt der Untergrund unserer Seele als Sehnsucht, als etwas, was da immer herauf will nach dem Vollbringer des Opfers, zu dem universellen Wesen, das auf einmal die Begierde befriedigt, nicht in der unend­lichen Aufeinanderfolge der Bilder.",
      "Der Erdenmensch fühlt schon diese Stimmungen - und sie sind die allerallerbesten, wenn er sie eben fühlt. Und diejenigen Erdenmen­schen, die in unserer Zeit ganz gemäß unserem besonderen Zeitalter diese Sehnsucht fühlen, sie sind im Grunde die, welche zu unserer gei­steswissenschaftlichen Bewegung kommen. Da lernen die Menschen erkennen im Leben draußen alles, was sie in den Einzelheiten befrie­digt für ihr gewöhnliches, oberes Bewußtsein; aber da schlägt dann herauf aus dem Unterbewußtsein das, was in seinen Einzelheiten nie befriedigt werden kann, was nach dem zentralen Grunde des Lebens verlangt. Und dieser zentrale Grund kann nur dadurch gegeben wer­den, daß wir eine universelle Wissenschaft haben, die sich nicht mit den Einzelheiten, sondern mit der Gesamtheit des Lebens beschäftigt.",
      "Dem, was aus dem Unterbewußtsein spielt und herauf will, muß im Sinne unserer heutigen Zeit entgegenkommen die Beschäftigung mit dem universellen Dasein, das in der Welt lebt, denn sonst spielt aus den Untergründen der Seele herauf das, was sich sehnt nach etwas, das es nie erreichen kann.",
      "In diesem Sinne ist die Geisteswissenschaft ein Entgegenkommen jenen Sehnsuchten, die in den Untergründen der Seele leben. Und weil alles, was später in der Welt geschieht, seine Vorspiele hat, brauchten wir uns nicht zu verwundern über einen Menschen, der etwa im heu­tigen Zeitalter durch die spirituelle Wissenschaft nach Befriedigung für die Macht der Sehnsucht in seiner Seele verlangen würde, wenn ihm zunächst gar nicht bewußte Seelenkräfte, die wie Sehnsuchten sind, ihn verzehren würden, da er in einem früheren Zeitalter lebte, in dem es diese spirituelle Weisheit nicht gegeben hat und er sie des­halb noch nicht haben konnte. So ist es, wie wenn er sich verzehren würde nach ihr, ein immerwährendes Verlangen haben würde nach ihr und das Leben nicht begreifen könnte - gerade weil er ein hervor-ragend großer Geist ist -, während heute hereinträufeln könnte in seine Seele etwas, was die Sehnsucht nach Bildern, welche nur die Öde übertönen können, stillen würde; ja, während er sich sehnt nach Auf­hören dieses Bilderjagens und sich um so mehr danach sehnen würde, je mächtiger dieses Bilderjagen wäre! Und kann uns, so wie es jetzt ausgesprochen ist, die Stimme dieses Menschen nicht erscheinen als eine Außerung eines Geistes, der in einer Zeit lebt, in welcher er diese spiri­tuelle Weisheit, die sich hineingießt wie Balsam in die Sehnsucht der Seele, noch nicht haben kann, wenn wir hören, wie er einem anderen schreibt:",
      "«Wer wollte auf dieser Welt glücklich sein. Pfui, schäme dich, möcht' ich fast sagen, wenn du es willst! Welch eine Kurzsichtigkeit, o du edler Mensch, gehört dazu, hier, wo alles mit dem Tode endigt, nach etwas zu streben. Wir begegnen uns, drei Frühlinge lieben wir uns: und eine Ewigkeit fliehen wir wieder auseinander. Und was ist des Strebens würdig, wenn es die Liebe nicht ist! Ach, es muß noch etwas anderes geben als Liebe, Glück, Ruhm und x, y, z, wovon unsre Seelen nichts träumen.",
      "Es kann kein böser Geist sein, der an der Spitze der Welt steht; es ist ein bloß unbegriffener! Lächeln wir nicht auch, wenn die Kinder weinen? Denke nur, diese unendliche Fortdauer! Myriaden von Zeit­räumen, jedweder ein Leben, und für jedweden eine Erscheinung wie diese Welt! Wie doch das kleine Sternchen heißen mag, das man auf dem Sirius, wenn der Himmel klar ist, sieht? Und dieses ganze unge­heure Firmament nur ein Stäubchen gegen die Unendlichkeit! 0 Rühle, sage mir, ist dies ein Traum? Zwischen je zwei Lindenblättern, wenn wir abends auf dem Rücken liegen, eine Aussicht, an Ahndungen rei­cher, als Gedanken fassen, und Worte sagen können. Komm, laß uns etwas Gutes tun und dabei sterben! Einen der Millionen Tode, die wir schon gestorben sind und noch sterben werden. Es ist, als ob wir aus einem Zimmer in das andere gehen. Sieh, die Welt kommt mir vor wie eingeschachtelt, das kleine ist dem großen ähnlich!» Aus einem Briefe Heinrich von Kleists aus dem Jahre 1806.",
      "So drängt die Sehnsucht, die er in solche Worte fassen konnte, einen Geist, der noch nicht eine Befriedigung dieser Sehnsucht finden konnte durch das, was, wenn sie nur mit einigem Verständnis an die Geistes­wissenschaft herantritt, die moderne Seele finden kann. Denn dieser Geist ist der, welcher jetzt vor hundert Jahren seinem Leben ein Ende machte, indem er zuerst seine Freundin Henriette Vogel und dann sich selbst erschoß, und der in jenem einsamen Grabe am Wannsee ruht, das sich vor hundert Jahren über seine Hülle geschlossen hat.",
      "Es ist eine sonderbare Fügung, man möchte sagen des Karma, daß wir uber die Stimmung, die uns am allerbesten das charakterisieren kann, was wir zu fassen versuchen, wenn wir sprechen von dem Zu­sammenwirken der zurückgehaltenen Willensopfer in der Sehnsucht, der Befriedigung dieser Sehnsucht, die allein kommen konnte von den Geistern der Bewegung, und dem Drange nach einer endgültigen Be­friedigung, wie sie nur kommen konnte auf dem Planeten der Erlö­sung - es ist ein sonderbarer karmischer Zusammenschluß, daß wir nach unserem ganz gewöhnlichen Programm gerade an einem Tage hier darüber sprechen mußten, der uns erinnern kann, wie ein Geist die unbestimmte Sehnsucht in den allerhöchsten Worten zum Aus­druck bringen konnte und sie endlich umgegossen hat in die allertragischste",
      "Tat, welche die Sehnsucht verkörpern konnte. Und wie könn­ten wir verkennen, daß dieser Geist in seiner Ganzheit, wie er vor uns steht, eigentlich eine lebendige Verkörperung dessen ist, was unten in der Seele lebt, was wir zurückführen müssen auf ein Anderes noch als auf das Erdendasein, wenn wir es erkennen wollen? Hat uns Heinrich von Kleist nicht am bedeutsamsten geschildert, was in einem Menschen leben kann - wie Sie gleich auf den ersten Seiten von «Die geistige Führung des Menschen und der Menschheit» geschildert fin­den - von dem, was über ihn selbst hinausgeht, ihn treibt, und was er erst später einsehen kann, wenn er nicht vorher seinen Lebensfaden unterbricht?",
      "Denken wir an seine «Penthesilea»: Wie viel mehr ist in Penthesilea, als sie mit ihrem Erdenbewußtsein umspannen kann! Wir könnten sie gar nicht beschreiben, wenn wir nicht annehmen würden, ihre Seele sei unendlich viel weiter als die enge kleine Seele, die sie - wenn sie auch eine große ist - mit ihrem Erdenbewußtsein umspannt. Daher muß eine Situation hineinspielen, die künstlich den ganzen Vorgang in das Drama hineinbringt. Ja, es muß sogar verhindert werden, daß der ganze Vorgang, wie Kleist sie an Achill heranführt, mit dem Ober-bewußtsein zu überschauen wäre, sonst würden wir die ganze Tragik nicht erleben können. Daher ist es «ihr» Achill. Es muß das, was im Oberbewußtsein lebt, in das Nichtbewußte hineingetaucht werden.",
      "Und wie spielt wieder dieses Unterbewußte hinein in eine Hand­lung wie zum Beispiel «das Käthchen von Heilbronn», besonders in der merkwürdigen Beziehung zwischen dem Käthchen und dem Wetter vom Strahl, die sich nicht abspielt im Oberbewußtsein, sondern in den tieferen Schichten der Seele, wo die Kräfte sind, von denen der Mensch nichts weiß, die von einem zum anderen gehen. Wenn wir das vor uns haben, spüren wir das Geistige, das in den Gravitations- und Attrak­tionskräften der Welt liegt. Fühlen Sie das, was in den Kräften der Welt liegt, zum Beispiel in der Szene, wo Käthchen ihrem Angebeteten gegenübersteht, wo wir sehen, was in dem Unterbewußtsein lebt und wie es verwandt ist dem, was draußen in der Welt lebt, und was man mit dem nüchternen trockenen Worte «Anziehungskräfte - und so weiter - der Planeten» belegt? Doch hineintauchen in dieses Unterbewußtsein",
      "konnte auch ein durchdringender und strebender Geist vor hundert Jahren noch nicht. Heute muß es geschehen.",
      "Und in ganz anderer Weise steht daher heute die Tragik eines «Prin­zen von Homburg» vor uns. Ich möchte wissen, wie die Abstraktlinge, die alles, was der Mensch vollbringt, nur ableiten wollen aus dem Ver­stande, eine Figur erklären wollen, wie es der Prinz von Homburg ist, der alle seine großen Taten in einer Art Traumzustand ausführt, auch die, welche zuletzt zum Siege führt. Und klar weist Kleist darauf hin, daß er aus seinem Oberbewußtsein heraus gar nicht den Sieg erlangen könnte, daß er auch nach seinem Oberbewußtsein nicht einmal ein ganz besonders großer Mensch ist, denn er wimmert bei jedem Tun. Und als durch einen besonderen Willensimpuls das, was in den Tiefen der Seele lebt, heraufgeholt wird, erst da ermannt er sich.",
      "Was als ein Erbstück dem Menschen aus dem Mondenbewußtsein geblieben ist, das ist etwas, was nicht heraufgebracht werden muß durch die abstrakte Wissenschaft, sondern von der vielseitigen und subtilen und allseitig an die geistigen Konturen angreifenden Wissen­schaft: das ist die Geisteswissenschaft. Das Größte bindet sich an das Mittlere und bindet sich an das Gewöhnliche.",
      "So sehen wir ein, daß die Geisteswissenschaft uns zeigt, wie die Zu­stände, welche wir heute in der Seele erleben, sich heranbilden im Kosmos, im Weltall. Wir sehen aber auch ein, wie das, was wir in der Seele erleben, uns einzig und allein einen Begriff verschaffen kann von dem, was geistig in den Untergründen der Dinge ist. Wir sehen aber auch, wie unsere Zeit herankommen mußte, um das zu befriedigen, was ersehnt worden ist in der Zeit, die der unsrigen vorangegangen ist, wie die Menschen begehrt haben nach dem, was unsere Zeit erst geben kann. Und eine Art der Verehrung für solche Menschen, die sich nicht zurechtfinden konnten in der Vorzeit gegenüber dem, was ihr Herz begehrte und was die Welt ihnen nicht geben konnte, eine gewisse Ver­ehrung für solche Menschen kann auch darin bestehen, daß wir uns erinnern, wie alles menschliche Leben zusammengehört und wie der heutige Mensch sein Leben widmen kann jenen geistigen Bewegungen, welche die Menschen - das zeigen uns ihre Schicksale - lange schon gebraucht hätten.",
      "So darf gewissermaßen auf die Geisteswissenschaft als eine Brin­gerin der Erlösung der Menschensehnsucht hingewiesen werden an einem Tage, der als der Jahrhunderttag des tragischen Todes eines dieser sehnsüchtigen Menschen sehr wohl daran erinnern kann, wie das, was die Geisteswissenschaft geben kann, von den Menschen stür­misch, aber auch wehmütig seit langen Zeiten schon verlangt worden ist. Das ist ein Gedanke, den wir fassen können, und der vielleicht auch theosophisch ist, an dem Jahrhunderttage des Todes eines der größten deutschen Dichter."
    ],
    "sentences": [
      [
        "Ein schwieriges Kapitel unserer Weltanschauung haben wir nun so weit gebracht, daß wir hinter den Erscheinungen der äußeren Sinnes-welt zum Teil erblicken gelernt haben Geistiges.",
        "Von solchen Erschei­nungen, die zunächst äußerlich wenig davon verraten, daß Geistiges in der eigentümlichen Form, wie wir dieses Geistige in unserem eigenen Seelenleben erfahren, dahintersteht, von solchen Erscheinungen haben wir erkannt, daß dennoch geistige Betätigungen, geistige Qualitäten und Eigenschaften dahinterstehen.",
        "Was uns so zum Beispiel im ge­wöhnlichen Leben als wärmehafte Eigenschaft erscheint, als Wärme oder Feuer, das erkannten wir als den Ausdruck des Opfers.",
        "In dem, was als Luft uns entgegentritt und wieder zunächst so wenig verrät, wenigstens für unsere Begriffe, daß es geistig ist, darin erkannten wir dasjenige, was wir die schenkende Tugend besonderer Weltenwesen nannten.",
        "Und im Wasser haben wir das erkannt, was Resignation, Verzicht genannt werden kann."
      ],
      [
        "Jn früheren Weltanschauungen - darauf sei nur nebenbei aufmerk­sam gemacht - hat man natürlich schon eher in dem äußeren Stoff­lichen das Geistige geahnt und erkannt, wofür ein Beweis sein kann, daß man besonders fluchtige Stoffe mit dem Worte «Spiritus » be­zeichnet hat, das wir heute in eigenschaftlicher Bedeutung anwenden auf das Geistige, indem wir sagen «spirituell»; und in der äußeren Welt kann es ja vorkommen, daß die Menschen dieses «spirituell» noch so wenig auf das Geistige beziehen, auf das Übersinnliche, daß einmal, wie einzelnen von Ihnen bekannt sein wird, als an einen Münchener Spiritistenverein ein Brief adressiert worden ist und man nicht wußte, was das ist, ein Spiritistenverein, man diesen Brief dem Vorsitzenden des Zentralverbandes der Spirituosenhändler aushändigte."
      ],
      [
        "Indem wir nun heute jenen bedeutungsvollen Übergang betrachten wollen, der sich in der Evolution des Erdenplaneten vollzogen hat von der alten Sonne zum alten Mond herüber, werden wir eine andere Art der Entwickelung des Geistigen ins Auge fassen müssen.",
        "Wir werden"
      ],
      [
        "aber ausgehen müssen von dem, was uns das letzte Mal entgegen­getreten ist als der Verzicht.",
        "Da haben wir gesehen, daß dieser Ver­zicht im wesentlichen darin besteht, daß geistig hochstehende Wesen­heiten verzichteten auf die Entgegennahme des Opfers, was ja, wie wir erkannt haben, im wesentlichen das Opfer des Willens oder der Willenssubstanz ist.",
        "Wenn wir uns dies so vorstellen, daß gewisse Wesenheiten das opfern wollen, was ihre Willenssubstanz ist, und ihnen durch den Verzicht höherer Wesenheiten sozusagen verweigert wird die Entgegennahme dieses Willens, dann werden wir uns leicht zu dem Begriff erheben können, daß dann jene Willenssubstanz, welche die betreffenden Wesenheiten eigentlich höheren geistigen We­senheiten opfern wollten, zurückbleiben muß in den betreffenden Wesenheiten, welche opfern wollen und nicht opfern können.",
        "So sind uns damit ohne weiteres im Weltenzusammenhange gegeben Wesen­heiten, welche bereit sind, ihr Opfer darzubringen, also in einer ge­wissen Weise bereit sind, das, was in ihrem Inneren ruht, inbrünstig hinzugeben, aber es nicht können und daher in sich behalten müssen.",
        "Oder anders ausgedrückt bedeutet es, daß diese Wesenheiten eine ge­wisse Verbindung mit höheren Wesenheiten, die sich ihnen ergeben hätte, wenn sie hätten opfern dürfen, durch die Zurückweisung des Opfers nicht haben können."
      ],
      [
        "In weltgeschichtlich symbolischer Weise tritt uns das entgegen, was wir dabei ins Auge fassen sollen - aber es ist dort verschärft - in dem Kain, der dem Abel gegenübersteht.",
        "Auch Kain will sein Opfer hinauf-senden zu seinem Gott.",
        "Sein Opfer aber ist nicht wohlgestaltet, und der Gott nimmt es nicht auf.",
        "Das Opfer Abels nimmt er auf.",
        "Was wir dabei ins Auge fassen wollen, ist das innere Erlebnis, das dabei zu­stande kommen kann, daß Kain sein Opfer zurückgewiesen findet.",
        "Wenn wir uns zu der Höhe der Auffassung erheben wollen, die dabei in Betracht kommt, so müssen wir uns klarmachen, daß wir bei den Regionen, von denen wir hier sprechen, Begriffe, die bloß eine Bedeu­tung in unserem gewöhnlichen Leben haben, hineinschleppen in die höheren Regionen.",
        "Es wäre falsch, wenn man davon sprechen würde, daß durch eine Schuld oder ein Unrecht die Zurückweisung des Opfers zustande käme.",
        "Von Schuld oder Sühne, wie wir sie in unserem"
      ],
      [
        "jetzigen gewöhnlichen Leben kennen, darf in diesen Regionen noch nicht die Rede sein.",
        "Wir müssen diese Wesenheiten vielmehr so be­trachten, daß es von seiten der höheren Wesenheiten, welche das Opfer zurückwiesen, ein Verzicht, eine Resignation ist."
      ],
      [
        "In dem, was wir vor acht Tagen als Seelenstimmung charakterisierten, liegt nichts, was Schuld oder Unterlassung ist, sondern es liegt darin alles Große und Bedeutungsvolle, was in einem Verzicht, in einer Resignation lie­gen kann.",
        "Das bleibt aber dabei doch bestehen, daß die anderen We­senheiten, welche das Opfer haben bringen wollen, in sich eine Stim­mung erzeugen müssen, von der wir fühlen können, daß damit etwas beginnt wie eine, wenn auch außerordentlich leise Gegnerschaft gegen jene Wesen, welche die Opfer zurückweisen."
      ],
      [
        "Deshalb ist dies in bezug auf Kain, wo es in einer späteren Zeit uns vorgeführt wird, in ver­schärftem Maße dargestellt.",
        "Wir werden daher nicht dieselbe Stim­mung, die wir bei Kain finden, bei denjenigen Wesenheiten antreffen, die sich von der Sonne zum Mond herüberentwickeln; wir werden diese Stimmung bei ihnen in einem anderen Maße antreffen."
      ],
      [
        "Und wir lernen die Stimmung, die sich da geltend macht, nur kennen, wenn wir, wie wir es in den letzten Vorträgen getan haben, wieder in unsere eigene Seele blicken und uns fragen, wo wir in der eigenen Seele eine solche Stimmung finden können, die uns andeuten kann, wie die Stim­mung ist, die sich entwickeln müßte in den Individualitäten, deren Opfergaben zurückgewiesen worden sind."
      ],
      [
        "Diese Stimmung in uns - und wir kommen da immer näher und näher dem irdischen Menschenleben -, die jede Seele schon kennt in ihrer Unbestimmtheit und zugleich in ihrer quälenden Weise in der Art, die wir voll rechnen können zu dem, was am nächsten Don­nerstage im öffentlichen Vortrage «Die verborgenen Tiefen des Seelen­lebens» zu besprechen sein wird, diese Stimmung, die jede Seele kennt als waltend in den verborgenen Tiefen des Seelenlebens, sie dringt zu­weilen herauf an die Oberfläche unseres Seelenlebens; dann ist sie vielleicht am wenigsten quälend.",
        "Aber wir Menschen gehen mit dieser Stimmung oftmals herum, ohne daß wir uns derselben in unserein Oberbewußtsein recht klar bewußt sind, und wir haben sie doch in uns.",
        "Man möchte an das Dichterwort erinnern, um so recht das Quälerische,"
      ],
      [
        "das mit der Nuance des Schmerzes Verbundene daran hervor­zuheben: «Nur wer die Sehnsucht kennt, weiß, was ich leide.» Ge­meint ist die Sehnsucht als Seelenstimmung, Sehnsucht, wie sie lebt in den Seelen der Menschen."
      ],
      [
        "Um uns hineinzuversetzen in das, was geistig in der Entwickelungs-phase des alten Saturn und der Sonne vorging, war notwendig, daß wir zu besonderen Seelenzuständen unseren Blick erhoben, die sozu­sagen erst eintreten, wenn die menschliche Seele strebend wird, wenn sie sich hinauforganisiert zu einem höheren Streben.",
        "Das haben wir gesehen, als wir versuchten, uns die Natur des Opfers aus unserem eigenen Seelenleben heraus klarzumachen, versuchten, uns klarzuma­chen, was der Mensch erlangt als Weisheit, die wir hineinträufeln sehen und die entsteht aus dem, was man nennen könnte: Bereitschaft zu geben, bereit sein dazu, sich selber sozusagen hinzugeben.",
        "Indem wir so zu mehr irdischen Verhältnissen heraufkommen, die sich aus früheren entwickelt haben, treffen wir eine Seelenstimmung, die ähn­lich ist manchem, was der Mensch heute noch erleben kann.",
        "Nur müs­sen wir uns klar sein, daß alles Leben unserer Seele, insofern unsere Seele in den Erdenleib eingefügt ist, eine obere Schicht legt über ein verborgenes Seelenleben, das unten in den Tiefen abläuft.",
        "Wer sollte denn nicht wissen, daß es ein solches verborgenes Seelenleben gibt?",
        "Das Leben belehrt uns hinlänglich darüber, daß es ein solches gibt."
      ],
      [
        "Nehmen wir nun einmal an, um uns etwas von diesem verborgenen Seelenleben klarzumachen, ein Kind habe vielleicht in seinem sieben-ten oder achten Jahre oder in einer anderen Lebenszeit dieses oder jenes erfahren; es habe zum Beispiel erfahren, wofür Kinder sehr häu­Fig ganz besonders empfänglich sind, Ungerechtigkeit - Ungerechtig­keit, indem es beschuldigt wurde, dies oder jenes getan zu haben, was es in Wahrheit nicht getan hat, aber die Bequemlichkeit der Umge­bung des Kindes habe, um wenigstens mit der Sache fertigzuwerden, das Kind beschuldigt, dies oder jenes getan zu haben.",
        "Kinder haben ein ganz besonders reges Empfinden dafür, wenn ihnen in dieser Weise eine Ungerechtigkeit zugefügt wird.",
        "Aber, wie das Leben nun ist, nachdem sich dieses Erlebnis tief eingefressen hat in das kindliche Le­ben, legt das spätere Leben die anderen Schichten des Seelendaseins"
      ],
      [
        "darüber, und das Kind hat für alles, was das Alltagsleben betrifft, ein Vergessen.",
        "Es könnte nun auch sein, daß eine solche Sache niemals wie­der auftauchen würde.",
        "Aber nehmen wir jetzt an: im fünfzehnten, sechzehnten Jahre erfährt das Kind, sagen wir in der Schule, eine neue Ungerechtigkeit."
      ],
      [
        "Und jetzt wird das wirksam, was sonst tief un­ten in der wogenden Seele ruht.",
        "Das Kind braucht es gar nicht einmal zu wissen, kann sich ganz andere Vorstellungen und Begriffe bilden, als zu wissen, daß heraufwirkt eine Reminiszenz dessen, was es in früheren Jahren erlebt hat."
      ],
      [
        "Wäre das aber, was früher vorgegangen ist, nicht geschehen, so würde es, wenn zum Beispiel das Kind ein Junge ist, nach Hause gehen, ein bißchen weinen, vielleicht auch ein bißchen schimpfen, es würde aber darüber hinweggehen.",
        "So aber ist jenes frühere Ereignis geschehen - und ich betone ausdrücklich, daß das Kind nicht zu wissen braucht, was da vorgekommen ist -, und das wirkt, wirkt unter der Oberfläche des Seelenlebens, wie unter dem glatt ausschauenden Meeresspiegel die Wogen aufgerührt werden kön­nen."
      ],
      [
        "Und aus dem, was sonst vielleicht ein Weinen, ein Klagen oder ein Schimpfen geworden wäre, wird nun ein Schülerselbstmord!",
        "So spielen die verborgenen Tiefen des Seelenlebens herauf aus den Unter­gründen."
      ],
      [
        "Und die wichtigste Kraft, die da unten waltet, die bei jeder Seele waltet und zuweilen heraufdringt in ihrer ureigenen Gestalt, aber am bedeutsamsten ist, wenn sie so heraufdringt, daß sich der Mensch ihrer nicht bewußt ist, das ist die Sehnsucht.",
        "Wir kennen auch die Namen, welche diese Kraft für die äußere Welt hat, die aber doch nur metaphorische, unbestimmte Namen sind, weil sie Beziehungen ausdrücken, die kompliziert sind und so überhaupt nicht ins Bewußt­sein heraufkommen."
      ],
      [
        "Nehmen Sie eine Erscheinung, die Sie alle kennen - der Stadt-mensch vielleicht weniger, aber er hat sie doch bei anderen erfahren -, eine Erscheinung, die man mit «Heimweh» bezeichnet.",
        "Wenn Sie nachgehen würden, was das Heimweh in Wirklichkeit ist, so würden Sie sehen, daß es im Grunde genommen bei jedem Menschen ein an­deres ist.",
        "Bald ist es so, bald so.",
        "Bald sehnt sich der Betreffende nach den traulichen Erzählungen, die er im Elternhause gehört hat; er weiß nicht, daß er sich nach Hause sehnt, was in ihm lebt, ist ein unbestimmter"
      ],
      [
        "Drang, ein unbestimmtes Wollen.",
        "Ein anderer sehnt sich nach seinen Bergen oder nach dem Fluß, an dem er so oft gespielt hat, wenn vor ihm Wogen spielten.",
        "Was da wirkt, dessen ist sich der Mensch oft wenig bewußt, aber wir fassen alle diese verschiedenen Eigenschaften zusammen unter dem «Heimweh», etwas ausdrückend, was unter tausendfältiger Verschiedenheit spielen kann, und was doch am besten getroffen ist, wenn wir sie als eine Art Sehnsucht kenn­zeichnen.",
        "Aber was ist diese Sehnsucht?",
        "Wir haben es eben ausgespro­chen, daß sie eine Art von Wille ist, und überall, wo wir die Sehn­sucht prüfen, können wir sehen, daß es eine Art von Wille ist.",
        "Aber was für ein Wille?",
        "Es ist ein Wille, der so, wie er zunächst ist, nicht befriedigt werden kann, denn wird er befriedigt, so hört die Sehnsucht auf.",
        "Ein sich nicht ausleben könnender Wille ist es, was wir als Sehn­sucht bezeichnen."
      ],
      [
        "So etwas müssen wir als Stimmung bei denjenigen Wesenheiten be­zeichnen, deren Opfer zurückgewiesen worden ist.",
        "Was wir in den Tiefen unseres Seelenlebens wahrnehmen können, das ist uns geblieben als ein Erbstück von jenen alten Zeiten, von denen wir jetzt sprechen.",
        "Wie wir anderes als Erbstücke der alten Entwickelungsstadien haben, so sind uns geblieben von der Entwickelungsphase, von der wir hier sprechen, alle Arten von Sehnsucht, von nicht zu befriedigendem Wil­len, von zurückgehaltenem Willen.",
        "So haben wir uns auch zu denken, daß durch das Zurückweisen des Opfers während dieser Ent­wickelungsphase Wesen entstehen, die wir nennen können: Wesen mit zurückgehaltenem Willen.",
        "Dadurch, daß sie diesen zurückgehaltenen Willen in sich haben mußten, waren sie in einer ganz besonderen Lage.",
        "Und man muß sich wieder in eigene Seelenzustände versetzen - denn die Gedanken erreichen kaum diese Zustände -, wenn man diese Dinge nachfühlen, nachempfinden will."
      ],
      [
        "Das Wesen, das seinen Willen hinopfern kann, geht auf in gewisser Beziehung in dem anderen Wesen.",
        "Auch das kann man fühlen im Menschenleben, wie man lebt und webt in einem Wesen, dem man Opfer bringt, wie man sich befriedigt und glücklich fühlt, wenn man dem Wesen gegenüberstehen kann, dem man Opfer bringt.",
        "Und weil wir hier sprechen von der Opferung an höhere Wesen, an umfassendere,"
      ],
      [
        "universelle Wesenheiten, zu denen hinaufzuschauen die opfern­den Wesen als ihre höchste Seligkeit empfinden müssen, so kann, was da zurückbleibt als zurückgehaltene Willenssehnsucht, nimmermehr dasselbe sein an innerer Stimmung, an innerem Seelengehalt als das, was sie erleben dürften, wenn sie opfern dürften.",
        "Denn wenn sie opfern dürften, wäre das Opfer bei den anderen Wesen.",
        "Wir dürfen gleichsam den Vergleich gebrauchen: wenn die Erde und die anderen Planeten der Sonne opfern dürften, dann wären sie bei der Sonne.",
        "Wenn sie nicht der Sonne opfern dürften, wenn sie zurückhalten müßten, was sie sonst opfern könnten, dann sind sie in sich selber zurückgedrängt."
      ],
      [
        "Wenn wir das fassen, was jetzt eben mit einem Worte ausgesprochen ist, dann merken wir, daß da etwas ins Weltall hineinkommt.",
        "Fassen Sie es klar, daß es nicht anders ausgesprochen werden kann: die We­sen, die einem anderen Wesen opfern, das in ihnen allen lebt, sie sind jetzt, wenn das Opfer nicht angenommen wird, darauf angewiesen, es selbst in sich zu tragen.",
        "Spüren Sie nicht, daß da etwas hereinblitzt, was man Egoität nennt, was als Egoität in allen Formen heraus­kommt?",
        "In dieser Weise ins Auge gefaßt, muß man fühlen, was - spä­ter sozusagen in die Entwickelung hineingegossen - als ein Erbstück nachlebt in den Wesen.",
        "Als die Sehnsucht sehen wir den Egoismus aufblitzen in der schwächsten Gestalt, aber wir sehen ihn sich hinein-schleichen in die Weltentwickelung.",
        "Und so sehen wir, wie die Wesen, die sich sich selbst, ihrer Egoität, hingeben werden, in einer gewissen Beziehung verdammt werden zur Einseitigkeit, zum bloßen Leben nur in sich selber, wenn nicht etwas anderes eintreten würde."
      ],
      [
        "Stellen wir uns einmal ein Wesen vor, das opfern darf: das lebt in dem anderen Wesen, und es lebt immer in dem anderen.",
        "Ein Wesen, das nicht opfern darf, kann nur in sich selber leben.",
        "Dadurch ist es ausgeschlossen von dem, was es in den anderen und in diesem Falle in den höheren Wesen erleben dürfte.",
        "Die Evolution würde schon in diesem Falle die entsprechenden Wesen in die Einseitigkeit hineinver­dammen und -verbannen, wenn nicht etwas einträte, was da in die Entwickelung hineinfällt und was die Einseitigkeit hinwegbewegen will.",
        "Das ist das Eintreten neuer Wesenheiten, welche die Einseitigkeit hintanhalten.",
        "Wie auf dem Saturn Willenswesen, wie auf der Sonne"
      ],
      [
        "Weisheitswesen, so sehen wir auf dem Monde die Geister der Bewegung auftreten, wobei wir aber nicht räumliche Bewegung uns vorzustellen haben, sondern wobei wir «Bewegung» so fassen müssen, daß sie einen mehr gedanklichen Charakter trägt.",
        "Jeder kennt den Ausdruck «Denkbewegung», obwohl das nur der Ablauf der Flüssigkeit der eige­nen Gedanken ist; aber daraus schon werden Sie sehen, daß, wenn wir uns einen umfassenderen Begriff der Bewegung aneignen wollen, wir zur Erklärung der Bewegung zu etwas anderem als der bloßen Ortsbewegung, die nur eine einzelne Gattung der gesamten Bewegung darstellt, greifen müssen.",
        "Wenn viele Menschen einem höheren Wesen hingegeben sind, das sich gleichsam in ihnen allen ausdrückt, das von ihnen allen Opfer entgegennimmt, so leben diese Vielen mit dem Einen und sind darin befriedigt.",
        "Wenn aber die Opfer zurückgewiesen wer­den, so leben die Vielen in sich selber und können nicht befriedigt werden.",
        "Da treten die Geister der Bewegung ein und führen gleich­sam die Wesen, welche sonst nur auf sich angewiesen wären, zu allen anderen Wesenheiten in einer gewissen Weise hin, bringen sie zu den anderen in eine Beziehung.",
        "Die Geister der Bewegung sind zunächst nicht nur als ortsverändernde Wesen zu denken, sondern sie sind solche Wesen, die etwas hervorbringen, wodurch ein Wesen in immer neue Beziehungen zu anderen Wesen tritt."
      ],
      [
        "Man kann sich eine Vorstellung machen von dem, was jetzt damit auf dieser Stufe im Kosmos erlangt ist, wenn man wieder auf eine ent­sprechende Seelenstimmung reflektiert.",
        "Wer weiß nicht, was Sehnsucht ist, was ein ganz Reguläres ist, wenn ein Seelenzustand naht, wenn er bleibt, wenn er gar keine Veränderung erleben darf?",
        "Wer weiß nicht, wie quälend es wird und den Menschen in einen Zustand bannt, der ihm unerträglich wird, der dann bei den flachköpfigen Menschen zu dem wird, was man «Langeweile» nennt?",
        "Aber von dieser Langeweile, die man gewöhnlich nur den flachköpfigen Menschen zuschreiben kann, gibt es alle möglichen Zwischenstufen bis zu denen, welche den großen, edlen Naturen eigen sind, in denen das lebt, was ihre eigene Natur als Sehnsucht ausbrütet, und was nicht befriedigt werden kann in der Welt.",
        "Und wodurch wird die Sehnsucht mehr befriedigt als durch Veränderung?",
        "Der Beweis dafür ist, daß diese Menschen die"
      ],
      [
        "Beziehungen suchen zu immer neuen und neuen Wesenheiten.",
        "Die Qual der Sehnsucht wird oft überwunden durch das, was veränderte Beziehungen sind zu immer neuen Wesenheiten."
      ],
      [
        "Da sehen wir, als die Erde ihre Mondenphase durchmacht, wie die Geister der Bewegung in das Leben der sich sehnenden Wesen, die sonst veröden würden - und Langeweile ist auch eine Art von Ver­ödung -, die Veränderung, die Bewegung hineinbringen, die Beziehung zu immer neuen und neuen Wesenheiten oder zu immer neuen und neuen Zuständen.",
        "Die räumliche, örtliche Bewegung ist nur eine Gat­tung dieser umfassenderen Bewegung, von der wir jetzt gesprochen haben.",
        "Eine Bewegung haben wir, wenn wir in der Lage sind, am Mor­gen einen bestimmten Gedankeninhalt in der Seele zu haben, diesen aber nicht zu behalten brauchen, sondern zu anderem übergehen kön­nen.",
        "Da überwinden wir die Einseitigkeit in der Sehnsucht durch die Mannigfaltigkeit, durch die Veränderung und die Bewegung des Erleb­ten.",
        "Im Raume draußen haben wir nur eine besondere Art dieser Ver­änderung."
      ],
      [
        "Denken wir uns dazu einen Planeten, der einer Sonne gegenüber­steht.",
        "Würde er immer in derselben Stellung gegenüber der Sonne sein, würde er sich nicht bewegen, so würde er bei jener Einseitigkeit blei­ben, die sich nur ergeben kann, indem er eben nur immer die eine Seite der Sonne zuwendet.",
        "Da kommen die Geister der Bewegung, führen den Planeten herum, um Veränderung hineinzubringen in seinen Zu­stand.",
        "Ortsveränderung ist nur eine Art der Veränderung überhaupt.",
        "Und indem die Geister der Bewegung die Ortsveränderung hineinbrin­gen in den Kosmos, bringen sie nur ein Spezifikum hinein in das, was die Bewegung im allgemeinen ist."
      ],
      [
        "Dadurch aber, daß die Geister der Bewegung in das Weltall, wie wir es bisher kennengelernt haben, die Bewegung und die Veränderung hineinbringen, muß noch etwas anderes hineinkommen.",
        "Wir haben gesehen, daß in dieser Evolution, in der ganzen kosmischen Mannig­faltigkeit, die sich da heraufentwickelt als die Geister der Bewegung, Geister der Persönlichkeit, Geister der Weisheit, des Willens und so weiter, auch dasjenige lebt, was wir genannt haben «schenkende Tugend», was als Weisheit ausgestrahlt wird und als Geistiges der"
      ],
      [
        "Luft, der Gasströmung zugrunde liegt.",
        "Das fließt nun mit dem in Sehnsucht umgestalteten Willen zusammen und wird in diesen Wesen­heiten das, was der Mensch nun kennt - noch nicht als Gedanken, sondern als Bild.",
        "Am besten vergegenwärtigen wir uns das an dem Bilde, das der Mensch hat, wenn er träumt.",
        "Das flüssige Bild des Traumes kann eine Vorstellung hervorrufen von dem, was bei einem Wesen geschieht, in dem der Wille der Sehnsucht lebt und von den Geistern der Bewegung in eine Beziehung zu anderen Wesen geführt wird.",
        "Und indem es zu dem anderen Wesen gebracht wird, kann es ja nicht ganz sich hingeben, da die eigene Egoität in ihm lebt.",
        "Aber es kann das flüchtige Bild des anderen aufnehmen, das lebt wie ein Traumbild in ihm.",
        "Daher das, was wir nennen können das «Aufstei­gen der Bilder der anderen Welt».",
        "Das Aufsteigen des Bilderbewußt­seins sehen wir während dieser Phase der Entwickelung heraufkom­men.",
        "Und indem wir Menschen selber noch ohne unser heutiges Erden-Ich-Bewußtsein diese Phase der Entwickelung durchgemacht haben, müssen wir uns vorstellen, daß wir während dieser Entwickelungs-phase dasjenige, was wir durch unser Ich erlangen, noch nicht haben, daß wir da wesen und weben im Weltall, indem in uns etwas lebt, was wir uns heute nur vergegenwärtigen können, wenn wir die Sehnsucht kennen."
      ],
      [
        "Wir könnten in einer gewissen Weise, wenn wir nicht solche Lei­denszustände ins Auge fassen, wie es die irdischen sind, uns vorstellen, daß sie gar nicht sein könnten, wenn wir folgendes bedenken.",
        "In ge­wisser Weise kommt Leid, Schmerz, in seiner seelischen Gestalt natür­lich, in der damaligen Zeit auch in unsere Wesenheiten und in die Wesenheiten anderer Wesen hinein, die mit unserer Evolution verbun­den sind.",
        "Und erfüllt wird durch die Tätigkeit der Geister der Bewe­gung das sonst leerbleibende Innere, das von Sehnsucht leidende Innere mit dem Balsam, der in Form des Bilderbewußtseins hinein sich ergießt in diese Wesenheiten.",
        "Sonst wären diese Wesenheiten leer in ihrer Seele, leer von jeglichem anderen, was nicht Sehnsucht zu nennen Ware.",
        "Aber hinein träufelt der Balsam der Bilder, welche die Öde und Leerheit mit Mannigfaltigkeit ausfüllen und die Wesen so hinwegführen über das Verbannt- und Verdammtsein."
      ],
      [
        "Wenn wir solche Worte ernst nehmen, haben wir zu gleicher Zeit das, was geistig zugrunde liegt dem, was sich während der Mond­phase unserer Erde entwickelt hat, und was wir jetzt, weil sich da übergelagert hat die Erdenphase unseres Wesens, in den tiefen Unter­gründen unseres Bewußtseins haben.",
        "Aber wir haben es - und in einer populären Weise soll das übermorgen im öffentlichen Vortrage gezeigt werden - so in den Untergründen unserer Seele, daß es, wie das, was unten wirbelt unter der Oberfläche des Meeres und nach oben Wellen treibt, sich abspielen kann, ohne daß man weiß, was die Gründe dessen sind, was dann ins Bewußtsein eintritt.",
        "Unter der Oberfläche unseres gewöhnlichen Ich-Bewußtseins haben wir ein solches Seelenleben, das da heraufspielen kann.",
        "Und was sagt dieses Seelenleben dem Men­schen, wenn es heraufspielt?",
        "Wenn wir ins Auge fassen den kosmischen Untergrund dieses unterbewußten Seelenlebens, so können wir sagen:"
      ],
      [
        "Das Seelenleben, das wir so heraufkommen spüren aus seelischen Un­tergründen, ist ein Heraufschlagen dessen, was sich da aus der Monden­phase der Entwickelung hineinbewegt hat in das, was während der Erdenphase selbst in uns hineingekommen ist.",
        "Und wenn wir so recht ins Auge fassen, was während der Erdennatur in uns hineingekommen ist, dann haben wir so richtig einen Grund dessen, was von dem alten Monde geistig herübergeführt hat zum Erdendasein."
      ],
      [
        "Fassen Sie ins Auge, daß es, wie wir es charakterisiert haben, not­wendig war, daß immer Bilder auftauchen mußten, die eine Öde zu befriedigen hatten.",
        "Dann kommt Ihnen ein Begriff von einem schwe­ren Gewicht, von einer großen Bedeutung: die sehnende Menschen-seele in ihrer sehnsuchtvollen Leerheit, die diese Sehnsucht befriedigt oder harmonisiert erhält durch das Hereinspielen von Bildern, die wieder nur an die Stelle von anderen Bildern treten können.",
        "Und wenn die Bilder da sind und eine Weile dagewesen sind, dann dämmert sie wieder auf aus den Untergründen, die alte Sehnsucht, und nach neuen Bildern führen sie die Geister der Bewegung.",
        "Und sind die neuen Bilder wieder eine Weile dagewesen, so schlägt die Sehnsucht wieder an nach neuen Bildern.",
        "Und das gewichtige Wort müssen wir aussprechen in bezug auf solches Seelenleben: Wenn die Sehnsucht nur befriedigt wird durch Bilder, welche den Bildern nachjagen, so ist das"
      ],
      [
        "die fortfließende Unendlichkeit ohne Ende.",
        "Da hinein kann nur das kommen, was kommen muß, wenn an die Stelle der in die Unendlich­keit fortfließenden Bilder etwas tritt, was die Unendlichkeit erlösen kann durch etwas anderes als bloß durch Bilder, nämlich durch Reali­täten.",
        "Das heißt mit anderen Worten: diejenige planetarische Verkör­perung unserer Erde, in der wir durchgemacht haben, daß die Bilder herbeigeführt werden durch die Tätigkeit der Geister der Bewegung, sie muß abgelöst werden von derjenigen planetarischen Phase der Erdenverkörperungen, welche wir die Phase der Erlösung nennen müs­sen.",
        "Und wir werden noch sehen, daß die Erde der «Planet der Erlö­sung» zu nennen ist, wie wir die vorherige Verkörperung der Erde, das Mondendasein, den «Planeten der Sehnsucht» nennen können, der zwar zu stillenden Sehnsucht, die aber in eine nie endende Unendlich­keit ausläuft.",
        "Und während wir leben im Erdenbewußtsein - das uns, wie wir gesehen haben, durch das Mysterium von Golgatha die Er­lösung bringt -, steigt herauf während dieses Lebens aus den Unter­gründen unserer Seele das, was fortwährend nach Erlösung verlangt.",
        "Es ist, wie wenn wir oben die Wellen des gewöhnlichen Bewußtseins hätten, und unten in den Tiefen des Meeres des Seelenlebens lebt der Untergrund unserer Seele als Sehnsucht, als etwas, was da immer herauf will nach dem Vollbringer des Opfers, zu dem universellen Wesen, das auf einmal die Begierde befriedigt, nicht in der unend­lichen Aufeinanderfolge der Bilder."
      ],
      [
        "Der Erdenmensch fühlt schon diese Stimmungen - und sie sind die allerallerbesten, wenn er sie eben fühlt.",
        "Und diejenigen Erdenmen­schen, die in unserer Zeit ganz gemäß unserem besonderen Zeitalter diese Sehnsucht fühlen, sie sind im Grunde die, welche zu unserer gei­steswissenschaftlichen Bewegung kommen.",
        "Da lernen die Menschen erkennen im Leben draußen alles, was sie in den Einzelheiten befrie­digt für ihr gewöhnliches, oberes Bewußtsein; aber da schlägt dann herauf aus dem Unterbewußtsein das, was in seinen Einzelheiten nie befriedigt werden kann, was nach dem zentralen Grunde des Lebens verlangt.",
        "Und dieser zentrale Grund kann nur dadurch gegeben wer­den, daß wir eine universelle Wissenschaft haben, die sich nicht mit den Einzelheiten, sondern mit der Gesamtheit des Lebens beschäftigt."
      ],
      [
        "Dem, was aus dem Unterbewußtsein spielt und herauf will, muß im Sinne unserer heutigen Zeit entgegenkommen die Beschäftigung mit dem universellen Dasein, das in der Welt lebt, denn sonst spielt aus den Untergründen der Seele herauf das, was sich sehnt nach etwas, das es nie erreichen kann."
      ],
      [
        "In diesem Sinne ist die Geisteswissenschaft ein Entgegenkommen jenen Sehnsuchten, die in den Untergründen der Seele leben.",
        "Und weil alles, was später in der Welt geschieht, seine Vorspiele hat, brauchten wir uns nicht zu verwundern über einen Menschen, der etwa im heu­tigen Zeitalter durch die spirituelle Wissenschaft nach Befriedigung für die Macht der Sehnsucht in seiner Seele verlangen würde, wenn ihm zunächst gar nicht bewußte Seelenkräfte, die wie Sehnsuchten sind, ihn verzehren würden, da er in einem früheren Zeitalter lebte, in dem es diese spirituelle Weisheit nicht gegeben hat und er sie des­halb noch nicht haben konnte.",
        "So ist es, wie wenn er sich verzehren würde nach ihr, ein immerwährendes Verlangen haben würde nach ihr und das Leben nicht begreifen könnte - gerade weil er ein hervor-ragend großer Geist ist -, während heute hereinträufeln könnte in seine Seele etwas, was die Sehnsucht nach Bildern, welche nur die Öde übertönen können, stillen würde; ja, während er sich sehnt nach Auf­hören dieses Bilderjagens und sich um so mehr danach sehnen würde, je mächtiger dieses Bilderjagen wäre!",
        "Und kann uns, so wie es jetzt ausgesprochen ist, die Stimme dieses Menschen nicht erscheinen als eine Außerung eines Geistes, der in einer Zeit lebt, in welcher er diese spiri­tuelle Weisheit, die sich hineingießt wie Balsam in die Sehnsucht der Seele, noch nicht haben kann, wenn wir hören, wie er einem anderen schreibt:"
      ],
      [
        "«Wer wollte auf dieser Welt glücklich sein.",
        "Pfui, schäme dich, möcht' ich fast sagen, wenn du es willst!",
        "Welch eine Kurzsichtigkeit, o du edler Mensch, gehört dazu, hier, wo alles mit dem Tode endigt, nach etwas zu streben.",
        "Wir begegnen uns, drei Frühlinge lieben wir uns: und eine Ewigkeit fliehen wir wieder auseinander.",
        "Und was ist des Strebens würdig, wenn es die Liebe nicht ist!",
        "Ach, es muß noch etwas anderes geben als Liebe, Glück, Ruhm und x, y, z, wovon unsre Seelen nichts träumen."
      ],
      [
        "Es kann kein böser Geist sein, der an der Spitze der Welt steht; es ist ein bloß unbegriffener!",
        "Lächeln wir nicht auch, wenn die Kinder weinen?",
        "Denke nur, diese unendliche Fortdauer!",
        "Myriaden von Zeit­räumen, jedweder ein Leben, und für jedweden eine Erscheinung wie diese Welt!",
        "Wie doch das kleine Sternchen heißen mag, das man auf dem Sirius, wenn der Himmel klar ist, sieht?",
        "Und dieses ganze unge­heure Firmament nur ein Stäubchen gegen die Unendlichkeit! 0 Rühle, sage mir, ist dies ein Traum?",
        "Zwischen je zwei Lindenblättern, wenn wir abends auf dem Rücken liegen, eine Aussicht, an Ahndungen rei­cher, als Gedanken fassen, und Worte sagen können.",
        "Komm, laß uns etwas Gutes tun und dabei sterben!",
        "Einen der Millionen Tode, die wir schon gestorben sind und noch sterben werden.",
        "Es ist, als ob wir aus einem Zimmer in das andere gehen.",
        "Sieh, die Welt kommt mir vor wie eingeschachtelt, das kleine ist dem großen ähnlich!» Aus einem Briefe Heinrich von Kleists aus dem Jahre 1806."
      ],
      [
        "So drängt die Sehnsucht, die er in solche Worte fassen konnte, einen Geist, der noch nicht eine Befriedigung dieser Sehnsucht finden konnte durch das, was, wenn sie nur mit einigem Verständnis an die Geistes­wissenschaft herantritt, die moderne Seele finden kann.",
        "Denn dieser Geist ist der, welcher jetzt vor hundert Jahren seinem Leben ein Ende machte, indem er zuerst seine Freundin Henriette Vogel und dann sich selbst erschoß, und der in jenem einsamen Grabe am Wannsee ruht, das sich vor hundert Jahren über seine Hülle geschlossen hat."
      ],
      [
        "Es ist eine sonderbare Fügung, man möchte sagen des Karma, daß wir uber die Stimmung, die uns am allerbesten das charakterisieren kann, was wir zu fassen versuchen, wenn wir sprechen von dem Zu­sammenwirken der zurückgehaltenen Willensopfer in der Sehnsucht, der Befriedigung dieser Sehnsucht, die allein kommen konnte von den Geistern der Bewegung, und dem Drange nach einer endgültigen Be­friedigung, wie sie nur kommen konnte auf dem Planeten der Erlö­sung - es ist ein sonderbarer karmischer Zusammenschluß, daß wir nach unserem ganz gewöhnlichen Programm gerade an einem Tage hier darüber sprechen mußten, der uns erinnern kann, wie ein Geist die unbestimmte Sehnsucht in den allerhöchsten Worten zum Aus­druck bringen konnte und sie endlich umgegossen hat in die allertragischste"
      ],
      [
        "Tat, welche die Sehnsucht verkörpern konnte.",
        "Und wie könn­ten wir verkennen, daß dieser Geist in seiner Ganzheit, wie er vor uns steht, eigentlich eine lebendige Verkörperung dessen ist, was unten in der Seele lebt, was wir zurückführen müssen auf ein Anderes noch als auf das Erdendasein, wenn wir es erkennen wollen?",
        "Hat uns Heinrich von Kleist nicht am bedeutsamsten geschildert, was in einem Menschen leben kann - wie Sie gleich auf den ersten Seiten von «Die geistige Führung des Menschen und der Menschheit» geschildert fin­den - von dem, was über ihn selbst hinausgeht, ihn treibt, und was er erst später einsehen kann, wenn er nicht vorher seinen Lebensfaden unterbricht?"
      ],
      [
        "Denken wir an seine «Penthesilea»: Wie viel mehr ist in Penthesilea, als sie mit ihrem Erdenbewußtsein umspannen kann!",
        "Wir könnten sie gar nicht beschreiben, wenn wir nicht annehmen würden, ihre Seele sei unendlich viel weiter als die enge kleine Seele, die sie - wenn sie auch eine große ist - mit ihrem Erdenbewußtsein umspannt.",
        "Daher muß eine Situation hineinspielen, die künstlich den ganzen Vorgang in das Drama hineinbringt.",
        "Ja, es muß sogar verhindert werden, daß der ganze Vorgang, wie Kleist sie an Achill heranführt, mit dem Ober-bewußtsein zu überschauen wäre, sonst würden wir die ganze Tragik nicht erleben können.",
        "Daher ist es «ihr» Achill.",
        "Es muß das, was im Oberbewußtsein lebt, in das Nichtbewußte hineingetaucht werden."
      ],
      [
        "Und wie spielt wieder dieses Unterbewußte hinein in eine Hand­lung wie zum Beispiel «das Käthchen von Heilbronn», besonders in der merkwürdigen Beziehung zwischen dem Käthchen und dem Wetter vom Strahl, die sich nicht abspielt im Oberbewußtsein, sondern in den tieferen Schichten der Seele, wo die Kräfte sind, von denen der Mensch nichts weiß, die von einem zum anderen gehen.",
        "Wenn wir das vor uns haben, spüren wir das Geistige, das in den Gravitations- und Attrak­tionskräften der Welt liegt.",
        "Fühlen Sie das, was in den Kräften der Welt liegt, zum Beispiel in der Szene, wo Käthchen ihrem Angebeteten gegenübersteht, wo wir sehen, was in dem Unterbewußtsein lebt und wie es verwandt ist dem, was draußen in der Welt lebt, und was man mit dem nüchternen trockenen Worte «Anziehungskräfte - und so weiter - der Planeten» belegt?",
        "Doch hineintauchen in dieses Unterbewußtsein"
      ],
      [
        "konnte auch ein durchdringender und strebender Geist vor hundert Jahren noch nicht.",
        "Heute muß es geschehen."
      ],
      [
        "Und in ganz anderer Weise steht daher heute die Tragik eines «Prin­zen von Homburg» vor uns.",
        "Ich möchte wissen, wie die Abstraktlinge, die alles, was der Mensch vollbringt, nur ableiten wollen aus dem Ver­stande, eine Figur erklären wollen, wie es der Prinz von Homburg ist, der alle seine großen Taten in einer Art Traumzustand ausführt, auch die, welche zuletzt zum Siege führt.",
        "Und klar weist Kleist darauf hin, daß er aus seinem Oberbewußtsein heraus gar nicht den Sieg erlangen könnte, daß er auch nach seinem Oberbewußtsein nicht einmal ein ganz besonders großer Mensch ist, denn er wimmert bei jedem Tun.",
        "Und als durch einen besonderen Willensimpuls das, was in den Tiefen der Seele lebt, heraufgeholt wird, erst da ermannt er sich."
      ],
      [
        "Was als ein Erbstück dem Menschen aus dem Mondenbewußtsein geblieben ist, das ist etwas, was nicht heraufgebracht werden muß durch die abstrakte Wissenschaft, sondern von der vielseitigen und subtilen und allseitig an die geistigen Konturen angreifenden Wissen­schaft: das ist die Geisteswissenschaft.",
        "Das Größte bindet sich an das Mittlere und bindet sich an das Gewöhnliche."
      ],
      [
        "So sehen wir ein, daß die Geisteswissenschaft uns zeigt, wie die Zu­stände, welche wir heute in der Seele erleben, sich heranbilden im Kosmos, im Weltall.",
        "Wir sehen aber auch ein, wie das, was wir in der Seele erleben, uns einzig und allein einen Begriff verschaffen kann von dem, was geistig in den Untergründen der Dinge ist.",
        "Wir sehen aber auch, wie unsere Zeit herankommen mußte, um das zu befriedigen, was ersehnt worden ist in der Zeit, die der unsrigen vorangegangen ist, wie die Menschen begehrt haben nach dem, was unsere Zeit erst geben kann.",
        "Und eine Art der Verehrung für solche Menschen, die sich nicht zurechtfinden konnten in der Vorzeit gegenüber dem, was ihr Herz begehrte und was die Welt ihnen nicht geben konnte, eine gewisse Ver­ehrung für solche Menschen kann auch darin bestehen, daß wir uns erinnern, wie alles menschliche Leben zusammengehört und wie der heutige Mensch sein Leben widmen kann jenen geistigen Bewegungen, welche die Menschen - das zeigen uns ihre Schicksale - lange schon gebraucht hätten."
      ],
      [
        "So darf gewissermaßen auf die Geisteswissenschaft als eine Brin­gerin der Erlösung der Menschensehnsucht hingewiesen werden an einem Tage, der als der Jahrhunderttag des tragischen Todes eines dieser sehnsüchtigen Menschen sehr wohl daran erinnern kann, wie das, was die Geisteswissenschaft geben kann, von den Menschen stür­misch, aber auch wehmütig seit langen Zeiten schon verlangt worden ist.",
        "Das ist ein Gedanke, den wir fassen können, und der vielleicht auch theosophisch ist, an dem Jahrhunderttage des Todes eines der größten deutschen Dichter."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG Berlin, 5. Dezember 1911",
    "paragraphs": [
      "So haben wir uns denn in einer Reihe von Betrachtungen vor die Seele geführt, wie hinter alledem, was wir die Maja oder die große Illusion nennen, das Geistige steht. Wir wollen noch einmal uns die Frage stellen: In welcher Art hat sich uns denn gezeigt, daß hinter allem, was wir zunächst für unsere Sinne und für unsere sonstige an unseren Leib gebundene Weltenauffassung um uns herum haben, das Geistige zunächst von uns erkannt worden ist?",
      "Wir haben es dadurch charakterisiert, dieses Geistige, daß wir im Laufe der letzten Betrachtungen genötigt waren, gleichsam vor unse­rem Blick hinwegzuschaffen die nächsten äußeren Welterscheinungen und durchzudringen bis zu solchen Eigenschaften des Wirklichen, wie die waren, die wir bezeichneten als Opferwilligkeit, schenkende Tu­gend oder Verzicht, also lauter Eigenschaften, die wir nur kennenler­nen können, wenn wir in unsere eigene Seele blicken, die wir sinnvoll zunächst nur unserer eigenen Seele beilegen können. Wenn wir nun demjenigen, was wir als das Wirkliche, wir könnten auch sagen, als das Wahrhaftige hinter der Welt der Illusion zu denken haben, in sei­ner Wahrheit solche Eigenschaften beilegen müssen, wie die eben ge­nannten, so müssen wir sagen: In dieser Welt des wahrhaftigen Da­seins, in dieser Welt des Wirklichen lebt dasjenige, was wir seinen Eigenschaften nach im Grunde genommen nur vergleichen können mit Eigenschaften, die wir zunächst an unserer eigenen Seele wahrnehmen. Wenn wir zum Beispiel das, was sich äußerlich ausdrückt im Scheine der Wärme, zu charakterisieren haben in bezug auf seine Wahrheit als Opferdienst, als strömendes Opfer in der Welt, so heißt das eben, daß wir das Element der Wärme zurückgeführt haben auf ein Spirituelles, auf ein Geistiges, gleichsam also hinweggeschafft haben, was der äußere Schleier des Daseins ist, und das aufgezeigt haben, was in der Außenwelt gleich ist demjenigen, was wir als unser eigenes Spirituelles erkennen.",
      "Bevor wir nun in den Betrachtungen weitergehen, ist uns eine an­dere Idee notwendig. Das ist die: Verfliegt denn nun wirklich alles,",
      "was wir innerhalb der Welt der Maja oder der großen Illusion haben, in eine Art von Nichtigkeit? Ist wirklich in all dieser uns umgebenden Sinnenwelt und der Welt unserer äußeren Auffassung gar nichts, was sich sozusagen darstellt als das Wahrhaftige oder als ein Wahr­haftiges?",
      "Es wäre ja gewiß ein guter Vergleich, wenn man sagen würde: die Welt der Wahrheit, die Welt der Wirklichkeit sei zunächst verborgen, wie die inneren Kräfte eines Teiches oder selbst des Ozeans in der Wassermasse verborgen sind; und die Welt der Maja könnten wir ver­gleichen mit dem Wellenkräuselspiel, das sich an der Oberfläche ab­spielt. Der Vergleich wäre gut, aber er zeigt uns gerade, daß doch un­ten etwas im Ozean ist von dem, was das Wellenkräuselspiel oben be­wirkt als das Substantielle des Wassers und auch das Konfigurelle der Kraft. So ist es gleichgültig, ob wir diesen oder einen anderen Ver­gleich wählen. Wir können wohl die Frage aufwerfen: Gibt es nicht auch im weiten Reiche unserer Maja oder Illusion etwas, was «wirk­lich» ist?",
      "Wir wollen es heute ebenso machen, wie wir es bei den letzten Be­trachtungen gemacht haben. Wir werden uns dem, was wir uns vor die Seele führen wollen, langsam nähern, indem wir ausgehen von inneren Erlebnissen unserer Seele. Und zwar, weil wir uns durch das Saturn-, Sonnen- und Mondendasein spirituell vorwärtsbewegt haben und jetzt zum Erdendasein heranrücken, wollen wir von noch naheliegenderen, man möchte sagen, gewöhnlicheren Seelenerlebnissen ausgehen, als wir es das letzte Mal taten. Das letzte Mal gingen wir aus von den verborge­nen Tiefen des Seelenlebens, von dem, was heraufragt aus dem, was wir in der Geisteswissenschaft kennengelernt haben als unseren astra­lischen Leib. Da haben wir heraufragen gefühlt die Sehnsucht, und wir haben gesehen, wie zunächst die Sehnsucht arbeitet in dem Wesen des Menschen, und wie sie es ist, die eigentlich das Seelenleben dahin führt, Befriedigung nur in dem Entgegenkommen jener Bilderwelt zu finden, die wir als die innere Bewegung dieses Seelenlebens haben auf­fassen können. Und dadurch haben wir den Weg gefunden von der mikrokosmischen Seele bis zu jenem Weltenschaffen, das wir zuge­schrieben haben den Geistern der Bewegung.",
      "Heute wollen wir noch von einem nähergehenden Erlebnis der Seele ausgehen, und zwar von einem Erlebnis, auf das schon aufmerksam gemacht worden ist im alten Griechenland, das aber in seiner Wahr­heit noch heute ein tief bedeutsames ist, und das angedeutet wird durch die Worte: Alle Philosophie, also alles Streben nach einem gewissen menschlichen Wissen gehe aus von dem Staunen. - Das ist in der Tat richtig. Wer nur ein wenig reflektiert und achtgibt auf den ganzen Vorgang im Erleben seiner Seele, wie er sich nähert irgendeinem Wis­sen, der wird schon an sich selbst erfahren können, daß ein gesunder Weg zum Wissen immer seinen Ausgangspunkt findet von dem Staunen, von der Verwunderung über irgend etwas.",
      "Dieses Staunen, diese Verwunde­rung, von der jeder Wissensprozeß auszugehen hat, gehört geradezu zu jenen seelischen Erlebnissen, die wir bezeichnen müssen als diejenigen, welche in alles Nüchterne Hoheit und Leben hineinbringen. Denn, was wäre irgendein Wissen, das in unserer Seele Platz greift, das nicht ausginge von dem Staunen?",
      "Es wäre wahrhaftig ein Wissen, das ganz einge­taucht sein müßte in Nüchternheit, in Pedanterie. Allein jener Prozeß, der sich abspielt in der Seele, der von der Verwunderung hinführt zu der Beseligung, die wir empfangen von den gelösten Rätseln, und der sich zuerst über der Verwunderung erhoben hat, macht das Hoheits­volle und das innerlich Lebendige des Wissensprozesses aus.",
      "Man sollte eigentlich fühlen das Trockene und Vertrocknende eines Wissens, das nicht von diesen beiden Gemütsbewegungen sozusagen eingesäumt ist. Eingerahmt von Staunen und von Beseligung über das gelöste Rätsel ist das gesunde Wissen.",
      "Alles andere Wissen kann von außen ange­eignet sein, kann von dem Menschen aus diesem oder jenem Grund herangebracht sein. Aber ein Wissen, das nicht eingerahmt ist von diesen beiden Gemütsbewegungen, ist nicht wirklich im Ernste aus der Menschenseele entsprungen.",
      "Alles Aroma des Wissens, das die Atmosphäre des Lebendigen im Wissen bildet, geht aus von diesen zwei Dingen, von Staunen und Beseligung über das erfüllte Staunen.",
      "Was für einen Ursprung hat aber das Staunen selbst? Warum tritt Staunen - also Verwunderung über irgendein Außeres - in unserer Seele auf? Es tritt Staunen, Verwunderung aus dem Grunde auf, weil wir uns zunächst irgendeinem Wesen oder einem Ding oder einer Tatsache",
      "gegenüber, die vor uns auftritt, fremd angemutet fühlen. Die Fremdheit ist das erste Element, das zur Verwunderung, zum Staunen führt. Aber nicht allem Fremden gegenüber empfinden wir das Stau­nen, die Verwunderung, sondern nur einem solchen Fremden gegen­über, mit dem wir uns doch in einer gewissen Weise verwandt fühlen, so verwandt fühlen, daß wir uns sagen: Es ist etwas in dem Ding oder Wesen, das jetzt noch nicht in mir ist, das aber in mich übergehen kann. - Also zugleich verwandt und fremd fühlen wir uns einer Sache gegenüber, die wir durch Verwunderung, durch ein Staunen zunächst erfassen.",
      "Mit dem Worte «Verwunderung» hängt dann auch das Wort «Wun­der» zusammen, das wir eine:n Ereignis beilegen, zu dem der Mensch zunächst in seiner Erkenntnis keine verwandtschaftliche Beziehung finden kann. Aber das kann ja nur an ihm liegen, oder braucht wenig­stens nur an ihm zu liegen.",
      "Und er würde sich gar nicht selbst in ab­lehnender Weise zu dem verhalten, was er als «Wunder» bezeichnet, wenn er nicht in einer gewissen Weise doch Anspruch darauf machen würde, daß es sich ihm erschließt, also in einer gewissen Weise doch verwandt mit ihm sein sollte. Denn warum leugnen die Menschen, die von materialistischen oder rein verstandesmäßigen Begriffen ausgehen, zum Beispiel dasjenige, was andere anerkennen als Wunder, wenn sie nicht direkte Beweise dafür haben, daß eine Lüge, eine Unwahrheit vorliegt?",
      "Das müssen heute selbst schon Philosophen zugeben, daß man aus den Erscheinungen der Welt, welche dem Menschen vorliegen, niemals beweisen könne, dad zum Beispiel der in dem Jesus von Nazareth inkarnierte Christus nicht auferstanden sei. Man kann Gründe dagegen anführen.",
      "Aber wie sind diese Gründe? Sie sind lo­gisch nicht haltbar! Das geben heute schon aufgeklärte Philosophen zu. Denn die Gründe, welche von materialistischer Seite beigebracht werden, zum Beispiel daß alle Menschen, welche diese Leute bisher ge­sehen haben, zunächst nicht so auferstehen wie der Christus, diese Gründe stehen auf derselben Höhe wie der, daß jemand bisher nur Fische gesehen hat und aus der Beschaffenheit der Fische nun nachwei­sen will, daß es keine Vögel gibt.",
      "Man kann nie aus der einen Klasse von Wesenheiten in logisch berechtigter Weise ableiten, daß andere",
      "Wesen nicht existieren. Ebensowenig kann man aus den Erfahrungen, welche man über die Menschen des physischen Planes machen kann, etwas ableiten - was als Wunder zunächst bezeichnet wird - über die Ereignisse von Golgatha. Wenn Sie aber einem Menschen etwas mit­teilen, was er als Wunder bezeichnen müßte, wenn die Sache auch wahr wäre, und er sagt: Ich kann sie nicht verstehen -, so widerspricht er damit nicht dem, was wir über den Begriff der Verwunderung ge­sagt haben; denn er zeigt in seinem Verhalten ganz klar, daß dieser Ausgangspunkt alles Wissens für ihn auch begründet ist. Er verlangt nämlich, daß das, was ihm mitgeteilt wird, ein ihm Verwandtes habe. Er will, daß es in einer gewissen Weise sein Eigentum werden kann im Geistigen, und da er glaubt, daß er das nicht haben könne, daß es nicht mit ihm verwandt ist, so lehnt er es ab. Selbst wenn wir bis zum Wun­derbegriff selbst herangehen, würden wir sehen, daß Verwundern oder Erstaunen, von dem schon im Sinne des alten Griechentums alle Philo­sophie ausgegangen ist, darauf beruht, daß sich der Mensch gegenüber befindet einem Fremden, es aber doch als ein Verwandtes anerkennen muß. Versuchen wir nun eine Verbindungsbrücke zu schaffen zwi­schen diesen Begriffen und dem, was wir das letzte Mal vor unsere Seele geführt haben.",
      "Wir haben das letzte Mal gezeigt, wie ein gewisser Fortschritt in der Evolution dadurch herbeigeführt wird, daß Wesen bereit sind zu opfern, Opfer darzubringen, daß aber diese Opfer verweigert, zurück­gewiesen werden, und wir haben in den zurückgewiesenen Opfern eine der Haupttatsachen erkannt, welche während der alten Monden­entwickelung gespielt haben. Es gehört zu dem Wesentlichsten der alten Mondenentwickelung, daß damals von gewissen Wesen an höhere Wesenheiten Opfer dargebracht werden sollten, auf welche diese höheren Wesenheiten verzichteten, so daß also gleichsam der Opferrauch der alten Mondwesen hinaufdrang zu den höheren Wesen­heiten, aber von ihnen nicht angenommen wurde und zurückgeleitet wurde als Substanz in die Wesenheiten, welche das Opfer darbringen wollten. Und wir haben gesehen, daß ein großer Teil der Eigentümlich­keit der Wesen des alten Mondes darin bestand, daß sie dasjenige in sich zurückgestoßen fühlen, was sie von sich selbst hinaufsenden wollten",
      "zu höheren Wesenheiten als Opfersubstanz. Ja, wir haben gesehen, daß das, was da hinauf wollte zu den höheren Wesenheiten und nicht konnte, eben zurückblieb in den betreffenden Wesenheiten, und sich dadurch in diesen Wesenheiten des zurückgewiesenen Opfers als die Kraft der Sehnsucht herausgebildet hatte. Und wir haben noch immer in alledem, was wir in unserer eigenen Seele als Sehnsucht empfinden, eine Erbschaft jener alten Mondenvorgänge, die darin bestehen, daß Wesen damals ihr Opfer nicht angenommen fanden. Der ganze Charakter der alten Mondenentwickelung, spirituell erfaßt, die ganze geistige Atmosphäre des alten Mondes läßt sich in vieler Beziehung so charakterisieren, daß Wesen auf dem alten Monde sind, die ihre Opfer darbringen wollen, aber finden, daß diese Opfer, weil die höheren Wesenheiten in bezug auf sie resignieren, nicht angenommen werden. Das ist der eigenartige Grundzug in der spirituellen alten Monden­atmosphäre: das zurückgewiesene Opfer. Und das zurückgewiesene Opfer des Kain, in dem symbolisch einer der Ausgangspunkte un­serer Erdenmenschheitsevolution angezeigt ist, erscheint uns wie eine Art Wiederholung des Grundzuges der alten Mondenentwicke­lung, der sich da abspielt in der Seele des Kain, der sein Opfer nicht angenommen sieht. Das ist etwas, was uns wie versinnbildlichen kann ein Leid, einen Schmerz, welche die Sehnsucht gebären, wie es bei den Wesen des alten Mondendaseins der Fall war.",
      "Wir haben nun das letzte Mal schon gesehen, daß zwischen diesen nicht angenommenen Opfern und zwischen der Sehnsucht, die da­durch in den Wesenheiten entstanden ist, daß das Opfer nicht ange­nommen worden ist, gewissermaßen ein Ausgleich geschaffen wurde, indem auf dem alten Monde die Geister der Bewegung auftraten. Dadurch wurde wenigstens die Möglichkeit geschaffen, daß die Sehn­sucht, die entstanden war bei den Wesen des zurückgewiesenen Opfers, in einer gewissen Art befriedigt werden konnte. Stellen Sie sich das recht lebendig vor, Sie haben höhere Wesenheiten, denen geopfert wer­den soll, aber die Opfersubstanzen werden zurückgewiesen. Sehnsucht entsteht dadurch in diesen Wesen, welche opfern wollten, und die nun fühlen: Hätte ich mein Opfer jenen höheren Wesen darbringen kön­nen, so würde das Beste meines eigenen Wesens bei diesen Wesen leben,",
      "ich selber würde in diesen höheren Wesenheiten leben, so aber bin ich ausgeschlossen von diesen Wesenheiten, so stehe ich hier, und diese hö­heren Wesenheiten stehen dort! - Die Geister der Bewegung aber - wir können das fast wörtlich verstehen - bringen diese Wesenheiten, in denen durch das zurückgewiesene Opfer aufglimmt die Sehnsucht nach den höheren Wesenheiten, in solche Lagen, daß sie sich von den ver­schiedensten Seiten nähern können den höheren Wesenheiten. So daß das, was in ihnen ruht als nicht darzubringendes Opfer, wenigstens durch die Fülle der Eindrücke, die empfangen werden von den höhe­ren Wesen, welche gleichsam umkreist werden von den Wesen des zu­rückgewiesenen Opfers, ausgeglichen werden kann; ausgeglichen, was durch das Zurückweisen des Opfers nicht befriedigt wird, indem in der Position dieser Wesen zu den höheren Wesenheiten eine Beziehung entsteht, wie sie durch ein dargebrachtes Opfer ausgedrückt werden kann.",
      "Wir machen uns völlig verständlich, was damit gemeint ist, wenn wir uns denken, symbolisch zusammengefaßt, die höheren Wesenheiten als Sonne, und dann in einer einzigen Position, als einen Planeten, nie­drigere Wesenheiten zusammengefaßt. Nehmen wir nun an, die Wesen des niederen Planeten wollten dem höheren Planeten, also der Sonne, ihre Opfer darbringen. Aber die Sonneweist sie zurück, und dieOpfer­substanzen müssen bleiben bei den Wesenheiten des nicht angenom­menen Opfers, dabei fühlen sich diese Wesen voll von Sehnsucht in ihrer Einsamkeit, in ihrer Abgeschlossenheit. Nun bringen die Geister der Bewegung sie in den Umkreis der höheren Wesenheiten; dadurch ist es ihnen erst möglich, an die Stelle des unmittelbaren Hinauf­fließens ihrer Opfersubstanz, diese Opfersubstanz selbst in Bewegung zu bringen und sie dadurch in eine Beziehung zu bringen zu den We­sen höherer Art. Es ist das geradezu so, als wenn ein Mensch nicht in der Lage ist, durch eine einmalige große Befriedigung mit sich zurecht­zukommen und dann eine Reihe Teilbefriedigungen erlebt: so daß also sein ganzes Gemüt in Bewegung kommt, wenn er so eine Reihe Teil­befriedigungen erlebt. Das haben wir das letzte Mal genauer beschrie­ben. Wir haben gesehen, wie durch die Eindrücke, die nun von außen kommen, weil sich das Wesen nicht innerlich in der Opferung mit den",
      "höheren Wesenheiten vereinigt fühlt, ein Ersatz entsteht; das konnte uns zeigen, wie solche Wesen dennoch zu einer gewissen Befriedigung kommen.",
      "Nun aber kann doch nicht geleugnet werden, daß das, was hätte geopfert werden sollen, in anderer Weise bei den höheren Wesen fort­bestehen würde als bei den niederen Wesen. Denn die eigentlichen Da­seinsbedingungen dessen, was hätte geopfert werden sollen, liegen bei den höheren Wesen. Bei den niederen Wesen müssen also andere Da­seinsbedingungen dafür eintreten. - Wiederum können wir uns dazu bildlich vorstellen: Wenn von einem Planeten die ganze Substanz, die er enthält, in die Sonne fließen könnte und die Sonne sie nicht zurück­weisen würde, so würden die Wesen dieses Planeten in der Sonne an­dere Daseinsbedingungen finden als sonst, wenn die Sonne sie zurück-weist, außerhalb der Sonne im Planeten. Kurz: Eine Entfremdung dessen, was wir den «Inhalt des Opfers» nennen müssen, tritt ein, eine Entfremdung dieser Opfersubstanz von ihrem Ursprung.",
      "Fassen Sie nun diesen Gedanken, daß Wesenheiten etwas in sich behalten müssen, was sie gern als Opfer darbringen würden, und wo­von sie das Gefühl und die Empfindung haben, daß es erst dann seinen rechten Sinn fände, wenn es als Opfer dargebracht werden könnte. Vergegenwärtigen Sie sich die Empfindungen solcher Wesenheiten, dann werden Sie das haben, was man nennen kann: Abgeschlossenheit eines gewissen Teiles der Weltenwesenheit gegenüber seinem eigent­lichen Sinn und gegenüber seinem eigentlichen großen Weltenzweck. Es haben Wesen etwas in sich, was eigentlich - wenn wir bildlich spre­chen dürften - an einem anderen Orte als bei ihnen selber seinen Sinn hätte. Die Folge davon ist, daß diese Deplacierung - wenn wir wieder bildlich sprechen - des zurückgewiesenen Opferrauches, der zurück­gewiesenen Opfersubstanz, ein Ausgeschlossenwerden zunächst dieser Opfersubstanz von dem übrigen Weltenprozeß bewirkt.",
      "Wenn Sie diesen Gedanken nicht mit Ihrem Verstande - denn der geht nicht auf solche Dinge -, sondern wenn Sie mit Ihrem Gefühl das fassen, was damit ausgesprochen ist, so werden Sie die Empfindung haben: Es ist etwas wie ein Herausreißen aus dem allgemeinen Welten-prozeß. Für die Wesen, die das Opfer zurückgewiesen haben, ist es nur",
      "etwas, was sie von sich abgestoßen haben. Für die anderen Wesen, in denen die Opfersubstanz geblieben ist, ist es etwas, dem der Charakter der Fremdheit seines eigenen Ursprunges aufgedrückt wird. Wir haben also dadurch Wesen, denen in ihrer Substantialität die Fremdheit von seinem Ursprunge aufgedrückt ist. Es ist, wenn man sich gefühlsmäßig diese Dinge vor die Seele malt, etwas, dem die Fremdheit seines Ur­sprunges innewohnt: Das ist der Tod! Und nichts anderes ist der Tod im Weltenall als das, was notwendig eintritt mit der zurückgewiesenen Opfersubstanz bei den Wesen, die eben diese Opfersubstanz behalten müssen. So kommen wir von der Resignation, von dem Verzicht, den wir gefunden haben auf der dritten Stufe der Evolution, gegenüber dem, worauf von den höheren Wesen verzichtet worden ist, zum Tod. Und der Tod in seiner wahren Bedeutung ist nichts anderes als die Eigenschaft von Wesensinhalten, die nicht an ihrem wahren Orte sind, die ausgeschlossen von ihrem wahren Orte sind.",
      "Auch wenn der Tod im konkreten Leben beim Menschen eintritt, liegt dasselbe zugrunde. Denn wenn wir uns den Leichnam besehen, der in der Welt der Maja zurückbleibt, so ist in ihm nichts anderes ent­halten als eine Substantialität, die mit dem Moment des Todes aus­geschlossen ist von Ich, Astralleib und Ätherleib, die entfremdet ist demjenigen, innerhalb dessen sie nur einen eigentlichen Sinn hat. Denn des Menschen physischer Leib hat keinen Sinn ohne Atherleib, Astral­leib und Ich, ist sinnlos, ist in diesem Moment von seinem Sinn aus­geschlossen. Was wir nicht mehr durchschauen können, wenn ein Mensch stirbt, das stellt sich uns eben dar im Makrokosmos. Dadurch, daß die Weltenwesen höherer Sphären zurückweisen, was ihnen als Opfer dargebracht werden soll, verfällt diese zurückgewiesene Opfer-substanz in den Wesenheiten, denen sie zurückgewiesen worden ist, dem Tode, denn der Tod ist Ausgeschlossenwerden irgendeiner Wel­tensubstanz, irgendeiner Weltenwesenheit von seinem eigentlichen Sinn.",
      "Damit aber sind wir eingetreten in eine spirituelle Charakteristik desjenigen, was wir das vierte Element im Weltall nennen. Wenn uns das Feuer reinster Opfersinn war - und überall, wo uns Feuer oder Wärme entgegentritt, liegt spirituell dahinter Opferung -, wenn wir",
      "hinter allem, was als Luft ausgebreitet ist um unsere Erde herum, schenkende oder spendende Tugend, hinströmende Tugend in Wahr­heit fanden, wenn wir charakterisieren konnten das fließende Wasser, also Flüßigkeit als Element, als spirituelle Resignation oder Verzicht, so müssen wir das Element der Erde, das allein der Träger des Todes werden kann - denn der Tod würde nicht da sein, wenn das Element der Erde nicht da wäre -, als dasjenige charakterisieren, was abgespal­ten worden ist von seinem Sinn durch den Verzicht. Jetzt haben Sie förmlich konkret irgend etwas, wo sich aus Flüssigem Festes bildet. Denn das spiegelt in einer gewissen Weise auch einen spirituellen Pro­zeß. Stellen wir uns vor, es gliedert sich ein in die Wassermasse eines Teiches Eis, das Wasser also wird fest. In Wahrheit liegt da nichts an­deres zugrunde, als daß dasjenige, was das Wasser zu Eis werden läßt, es abschnürt von dem Sinn des Wassers. Da haben Sie das Spirituelle des Festwerdens, das Spirituelle des Erdewerdens. Denn in bezug auf die Charakteristik der vier Elemente ist das Eis ebenfalls «Erde» und nur das Flüssige «Wasser». Und das, worin der Tod sich darstellt, sich auslebt, das ist das Element der Erde.",
      "Wir sind ausgegangen davon, daß wir die Frage aufgeworfen haben, ob es innerhalb unserer Welt der Illusion, der Maja, gar nichts Wahr­haftiges gibt, ob es dort gar nichts von dem gibt, was sozusagen einer Wirklichkeit entspricht? Nehmen Sie einmal jetzt recht genau den Be­griff, den wir eben vor unsere Seele hingestellt haben. Ich habe Ihnen von Anfang an gesagt: die Begriffe dieser unserer Betrachtungen sind einigermaßen kompliziert. Es wird also notwendig sein, daß wir sie nicht nur verstandesmäßig aufnehmen, sondern darüber meditieren, dann werden sie uns erst ganz klar werden. Aber nehmen wir jetzt diesen Begriff vom Tode beziehungsweise vom Erdigen; er zeigt uns ein ganz merkwürdiges Gesicht. Während wir bei allen anderen Be­griffen uns sagen konnten: In bezug auf das, was da in der Welt der Maja um uns herum ist, liegt eigentlich gar nichts Wahrhaftiges vor, sondern das Wahrhaftige ist ein ihm zugrunde liegendes Spirituelles -, haben wir jetzt etwas herausbekommen, wo dasjenige, was wir inner­halb der Maja haben, eigentlich gerade deshalb, weil es getrennt ist von seinem Sinn, weil es im Spirituellen sein sollte, sich als das Tote",
      "charakterisiert. Es ist damit in die Maja hinein etwas abgeschnürt, was eigentlich nicht in der Maja sein sollte. Überall im ganzen weiten Reiche der Maja oder der großen Illusion haben wir eben lauter Täu­schungen, lauter Illusionen vor uns. Aber wir bekommen etwas in die Maja hinein, was dadurch einem Wahrhaftigen entspricht, daß es ab­geschnürt wird von seinem eigentlichen Sinn im Spirituellen, und in dem Augenblick, wo es hereinkommt, tritt an es die Vernichtung, der Tod heran. Das sagt uns aber nichts Geringeres als die große okkulte Wahrheit: Innerhalb der Welt der Maja ist das einzige, das sich in seiner Wirklichkeit zeigt, der Tod! - Alle anderen Erscheinungen müs­sen wir zurückverfolgen auf ihr Wirkliches, alle anderen Erscheinun­gen, die in der Maja auftreten, haben hinter sich das Wahrhaftige:",
      "Nur der Tod ist innerhalb der Maja das Wahrhaftige, denn er besteht darin, daß von dem Wahrhaftigen etwas abgeschnürt und herein­genommen ist in die Maja. Daher ist der Tod innerhalb der Maja das einzig Wahrhaftige.",
      "Und wenn wir jetzt von dem, man möchte sagen, in der allgemeinen Maja sich Ausbreitenden übergehen zu den großen Prinzipien der Welt, dann stellt sich für die okkulte Wissenschaft eine sehr wichtige und wesentliche Konsequenz dieses Satzes dar, daß innerhalb unserer Welt der Maja nur der Tod eigentlich das Wahrhaftige ist. Wir kön­nen uns dem, was ich hier sagen will, noch von einer anderen Seite nähern. Wir können zunächst die Wesenheiten der anderen Reiche be­trachten, die um uns herum sind. Wir können fragen: Sterben zum Beispiel Mineralien? - Für den Okkultisten hat es keinen Sinn zu sa­gen: Mineralien sterben. - Das wäre ungefähr ebensoviel, als wenn man sagen würde, der Fingernagel, den wir uns abschneiden, sei ge­storben. Der Fingernagel ist eben nicht irgend etwas, was als Totalität Anspruch hat auf Dasein, sondern er ist etwas an uns, und wenn wir ihn abschneiden, so haben wir ihn von uns getrennt und ihm das mit uns zusammenhängende Leben entrissen. Er stirbt im Grunde genom­men erst dann, wenn wir selber sterben. Also in demselben Sinne, sagt die okkulte Wissenschaft, sterben die Mineralien nicht. Denn die Mine­ralien sind nur Glieder an einem großen Organismus, wie der Finger­nagel an unserem Organismus ein Glied ist; und wenn ein Mineral",
      "scheinbar zugrunde geht, so ist es nur losgerissen von diesem großen Organismus, wie das Stück Fingernagel losgerissen ist von unserem Organismus, wenn wir es abschneiden. Die Zerstörung des Minerals ist kein Tod, denn das Mineral lebt nicht in sich selber, sondern in dem großen Organismus, von dem es ein Glied ist. - Wenn Sie sich erinnern an den Vortrag über das Wesen der Pflanzen, so werden Sie wissen, daß gesagt worden ist: Die Pflanze ist als solche auch nicht selbständig, sondern sie ist ein Glied, nun nicht wie das Mineral an einem großen Organismus, sondern an dem ganzen Erdenorganismus; und es hat für eine okkulte Betrachtung keinen Sinn, von einzelnen Pflanzenorganismen zu sprechen, sondern man muß sprechen von dem Erdenorganismus, an dem die Pflanzen überall Teile sind.",
      "Und wenn wir sie zu ihrem «Tode» bringen, dann ist es so, wie wenn wir uns einen Fingernagel abschneiden. Wir können nicht sagen, der Finger­nagel ist gestorben. Ebensowenig können wir dies von den Pflanzen sagen, denn sie gehören einem großen Organismus an, der identisch ist mit der ganzen Erde und der ein Organismus ist, der im Frühling ein­schläft, die Pflanzen als seine Organe der Sonne entgegensendet und sie im Herbst wieder in sich aufnimmt, wenn er die Samen der Pflan­zen in sich aufnimmt.",
      "Es hat keinen Sinn, die Pflanzen für sich allein zu betrachten, denn der Erdenorganismus stirbt nicht ab, wenn die ein­zelnen Pflanzen an ihm verwelken, ebenso wie wir, wenn wir graue Haare bekommen, auch nicht sterben, wenn wir die grauen Haare nicht wieder auf naturgemäße Weise in schwarze färben können. Nur sind wir da in einer anderen Lage als die Pflanzen.",
      "Aber die Erde ist da in einer solchen Lage, die sich vergleichen ließe mit dem Menschen, wenn er graue Haare wieder in schwarze zurückverwandeln könnte. Also die Erde stirbt nicht, sondern was sich da zeigt im Welken der Pflanzen, ist ein Prozeß, der sich an der Oberfläche abspielt.",
      "So kön­nen wir niemals sagen, daß die Pflanzen in Wahrheit sterben. Aber auch von den Tieren können wir zunächst nicht sagen, daß sie wie wir sterben. Denn das einzelne Tier ist in Wahrheit auch nicht vorhanden, es ist nur die Gruppenseele vorhanden, die im Übersinnlichen ist.",
      "Was das Tier im Wahrhaftigen ist, das ist nur auf dem Astralplan vorhan­den als die Gruppenseele, und das einzelne Tier ist aus der Gruppenseele",
      "heraus verdichtet. Und wenn es stirbt, so ist es ein abgelegtes Glied der Gruppenseele, und diese ersetzt es durch ein anderes.",
      "Was wir also als den Tod im Mineral-, Pflanzen- und Tierreich an­treffen, das ist nur scheinbar, ist nur innerhalb der Maja Tod. In Wahrheit stirbt wirklich nur der Mensch, der es mit seiner Individuali­tät so weit bringt, daß er hinunterkommt zu seinem physischen Leibe, in dem er während des Erdendaseins real werden muß. In Wahrheit hat von «Tod» zu sprechen nur einen Sinn für das Erdendasein des Menschen.",
      "Wenn wir dies ins Auge fassen, müssen wir sagen: Nur der Mensch kann eigentlich den Tod wirklich erleben. - Beim Menschen ist also das, was wir durch die okkulte Forschung kennenlernen, ein wirkliches Überwinden des Todes, ein wirkliches Besiegen des Todes. Denn bei anderen Wesen ist der Tod nur scheinbar, ist er nicht in Realität vor­handen.",
      "Wenn wir höher hinaufkommen würden, von dem Menschen wieder zu den Wesenheiten der höheren Hierarchien, so würden wir ebenso finden, daß diese den Tod nach Menschenart nicht kennen; so daß es im Grunde genommen nur bei jenen Wesenheiten einen realen Tod, das heißt, einen Tod auf dem physischen Plan gibt, die sich auch etwas zu holen haben auf dem physischen Plan. Der Mensch aber hat sich auf dem physischen Plan sein Ich-Bewußtsein zu holen.",
      "Das könnte er ohne den Tod nicht finden. Weder bei den Wesenheiten, die unter dem Menschen stehen, noch bei den Wesenheiten, die höher ste­hen als der Mensch, hat es einen Sinn, von wahrhaftem Tod zu spre­chen.",
      "Dann aber wird es begreiflich erscheinen, daß wir für jene We­senheit, die wir die Christus -Wesenheit nennen, gar keine Möglichkeit haben, ihre bedeutendste Erdentat auszulöschen. Denn wir haben ja gesehen, daß bei dieser Christus-Wesenheit das Mysterium von Gol­gatha als das Wesentlichste in Betracht kommt: die Besiegung des Todes durch das Leben.",
      "Wo aber kann diese Besiegung des Todes nur vor sich gehen? Kann sie vor sich gehen in den höheren Welten? Nein! Denn schon bei den niederen Wesen, die wir angeführt haben, im Mineral-, Pflanzen- und Tierreich, kann von Tod nicht gesprochen werden, weil sie eigentlich ihr wahres Wesen in den höheren, über­sinnlichen Welten haben.",
      "Und wir werden im Laufe der Winterbetrachtungen",
      "noch weiter ausführen, daß auch bei den höheren We­senheiten nicht von Tod gesprochen werden kann, sondern nur von Verwandlungen, von Metamorphosen, von Umgestaltung. Von einem Einschnitt in das Leben, den wir als «Tod» bezeichnen, kann nur beim Menschen gesprochen werden. Und der Mensch kann diesen Tod nur erleben auf dem physischen Plan. Wäre der Mensch niemals auf den physischen Plan gekommen, so würde er nichts wissen vom Tod, denn kein Wesen, das den physischen Plan nicht betreten hat, weiß etwas vom Tod. Es gibt in den anderen Welten nicht das, was man «Tod» nennen kann, sondern nur Verwandlungen, Metamorphosen. Sollte der Christus durch den Tod gehen, so mußte er auf den physischen Plan heruntersteigen! Denn nur dort konnte er den Tod erleben.",
      "So sehen wir, daß auch im geschichtlichen Werden des Menschen in einer merkwürdigen Weise das Wahrhaftige der höheren Welten hereinspielt in die Maja. Während wir für alle anderen geschichtlichen Ereignisse mit unserem Denken nur dann zurechtkommen, wenn wir sagen: Hier auf dem physischen Plan ist das geschichtliche Ereignis, aber die Ursache dafür liegt oben in der geistigen Welt, zu der müssen wir gehen -, können wir von dem Ereignis von Golgatha nicht sagen:",
      "Dieses Ereignis ist hier unten auf dem physischen Plan, und etwas Entsprechendes liegt in der höheren Welt. - Gewiß, der Christus selbst gehört den höheren Welten an und stieg herunter auf den physischen Plan. Aber ein Urbild, wie wir es für alle anderen geschichtlichen Ereignisse suchen müssen, gibt es nicht für das, was sich auf Golgatha vollzogen hat. Das hat sich nur auf dem physischen Plan abgespielt! -Unter den vielen Beweisen, die aus der okkulten Wissenschaft für diese Tatsache gegeben werden könnten, ist zum Beispiel dieses, daß das Ereignis von Damaskus sich, wie wir dies schon öfter dargestellt ha­ben, im Laufe der nächsten drei Jahrtausende für eine genügend große Anzahl von Menschen erneuern wird. Das heißt, es werden sich bei den Menschen solche Fähigkeiten entwickeln, daß sie den Christus auf dem astralischen Plan als Äthergestalt wahrnehmen werden, wie es bei Paulus vor Damaskus der Fall war. Dieses Ereignis des Wahrnehmens des Christus durch nach und nach bei den Menschen im Laufe der nächsten drei Jahrtausende sich entwickelnde höhere Fähigkeiten",
      "macht seinen Anfang in unserem 20. Jahrhundert. Von da ab kommen diese Fähigkeiten allmählich heraus und werden in den nächsten drei Jahrtausenden bei einer genügend großen Anzahl von Menschen sich ausbilden. Das heißt, eine genügend große Anzahl von Menschen wird wissen durch den Hineinblick in die höheren Welten, daß der Christus eine Realität ist, daß er lebt, sie werden ihn kennenlernen, wie er jetzt lebt. Und sie werden nicht nur die Art kennenlernen, wie er jetzt lebt, sondern sie werden sich genau wie Paulus die Überzeugung verschaf­fen, daß er gestorben und auferstanden ist. Aber die Grundlage dazu kann nicht gelegt werden in den höheren Welten, die muß auf dem physischen Plan gelegt werden.",
      "Wenn also heute schon jemand dazu kommt, diese Dinge zu ver­stehen und zu begreifen, wie die Entwickelung des Christus selber vor­wärtsgeht und damit die Entwickelung gewisser menschlicher Fähig­keiten, wenn es jemand begreift, dadurch begreift, daß er die Geistes­wissenschaft heute versteht, so hindert nichts daran, daß er, wenn er durch die Pforte des Todes gegangen ist, an diesem Ereignis teilnimmt, wenn es wirklich als ein erstes Hereinleuchten des Christus in die Welt des Menschen sich darstellt. Derjenige also, der heute im physischen Leibe sich auf dieses Ereignis vorbereitet, kann es auch erleben in dem Leben zwischen dem Tode und einer neuen Geburt.",
      "Diejenigen Men­schen aber, die sich nicht darauf vorbereiten, die sich in dieser Inkar-nation kein Verständnis dafür erwerben, sie können in dem Leben, das sich an dieses anschließt zwischen dem Tode und einer neuen Geburt, nichts wissen von dem, was in bezug auf den Christus von unserem Jahrhunderte ab durch die nächsten drei Jahrtausende geschieht. Sie müssen warten, bis sie wieder inkarniert sind und weiter sich die Vor­bereitung dazu auf der Erde schaffen.",
      "Das also, was als die Ursache aller folgenden Christus-Entwickelung auf der Erde sich abspielen mußte, der Tod auf Golgatha, das kann auch nur innerhalb des phy­sischen Leibes begriffen werden. Das ist unter allen Tatsachen, die uns wichtig sind für das höhere Leben, das einzige, was nur innerhalb des physischen Leibes begriffen werden kann.",
      "Dann wird es weiter ver­arbeitet, wird es weiter ausgebildet in den höheren Welten. Aber be­griffen müssen wir es zunächst haben innerhalb des physischen Leibes.",
      "Gerade wie das Mysterium von Golgatha niemals sich hätte in den höheren Welten abspielen können, wie es auch kein Urbild hat in den höheren Welten, sondern ein Ereignis ist, das, weil es den Tod in sich schließt, abgeschlossen ist innerhalb des physischen Planes, so muß das Verständnis dafür auf dem physischen Plan erworben werden. Ja, es gehört sogar geradezu zu den Aufgaben des Menschen auf der Erde, in irgendeiner seiner Inkarnationen sich dieses Verständnis zu erwerben.",
      "Wir müssen also sagen, damit haben wir auch im Großen etwas ge­funden, was sozusagen auf dem physischen Plan uns ein unmittelbar Reales, ein unmittelbar Wahrhaftiges zeigt. Was also ist denn real auf dem physischen Plan? Real auf dem physischen Plan, so daß wir dabei stehenbleiben können und sagen: Hier haben wir etwas Wahres! - ist der Tod in der Menschenwelt, nicht in den anderen Reichen der Natur. Und bei den geschichtlichen Ereignissen, die im Laufe der Erden-entwickelung geschehen, müssen wir, wenn wir diese geschichtlichen Ereignisse kennenlernen wollen, von jedem solchen geschichtlichen Ereignis zu einem geistigen Urbild gehen - nur nicht bei dem Myste­rium von Golgatha! In diesem haben wir etwas, was so, wie es ist, unmittelbar in die Welt des Wahrhaftigen hineingehört.",
      "Nun ist es außerordentlich interessant, daß sich gewissermaßen auch die andere Seite des eben Auseinandergesetzten zeigt. Es ist wirklich außerordentlich bedeutsam, zu sehen, wie dieses Ereignis von Golgatha heute als ein reales Ereignis abgeleugnet wird, wie die Leute, wenn wir von äußerer Historie reden, sagen, es läßt sich im Zusammenhange der historischen Tatsachen nicht beweisen. Es gibt nun unter den histo­rischen Tatsachen, die wesentlich sind, auch kaum eine, die sich so schlecht durch äußere realistische Gründe beweisen läßt wie das My­sterium von Golgatha. Denken Sie, wie leicht es im Verhältnis dazu ist, in bezug auf die Existenz eines Sokrates oder Plato oder irgend­eines griechischen Helden, insofern sie bedeutend sind für den Fort­schritt der Menschheit in der äußeren Welt, mit historischen Gründen zu arbeiten; und wie die Menschen bis zu einem gewissen Grade mit vollem Recht kommen und sagen: Keine Historie darf behaupten, daß ein Jesus von Nazareth gelebt habe! - Äußere historische Widergründe",
      "gibt es da nicht. Wie man andere historische Tatsachen behandelt, so läßt sich diese nicht behandeln.",
      "Es ist höchst merkwürdig: diese auf dem äußeren physischen Plan ge­scheheneTatsache hat dies eine gemeinschaftlich mit allen übersinnlichen Tatsachen, die lassen sich auch nicht beweisen. Und es sind so ziemlich dieselben Leute, welche die übersinnliche Welt leugnen und denen die Möglichkeit fehlt, dieses Ereignis, das gar kein übersinnliches ist, zu erfassen.",
      "Man kann es in bezug auf seine Wirkungen darstellen. Aber da machen sich die Leute den Gedanken, daß solche Wirkungen auch eintreten könnten, ohne daß das reale Ereignis in der Geschichte auf­getreten wäre, und erklären sie dann als Folge soziologischer Verhält­nisse.",
      "Für den jedoch, der den inneren Gang des Weltenwerdens kennt, ist die Idee, daß Wirkungen wie die des Christentums ohne eine da­hinterstehende Macht geschehen könnten, ebenso gescheit, wie wenn man sagte, daß auf einem Felde Kohlköpfe wachsen können, ohne daß vorher Samen ausgestreut wird. Ja, wir können noch weitergehen und sagen, daß für die, welche an der letzten Ausgestaltung der Evan­gelien beteiligt waren, keine Möglichkeit vorhanden war, das histo­rische Ereignis des Mysteriums von Golgatha als historisches Ereignis mit historischen Gründen nachzuweisen, denn es ging wirklich ziem­lich spurlos für alle äußere Beobachtung vorüber!",
      "Wissen Sie, wie die, welche an der späteren Ausgestaltung der Evangelien beteiligt waren, sich selber von diesen Ereignissen überzeugt haben - mit Ausnahme des Schreibers des Johannes-Evangeliums, der ja der unmittelbare Zeit­genosse dieser Ereignisse war? Sie haben sich überzeugt zunächst nicht aus historischen Urkunden, denn sie haben ja auch nichts anderes ge­habt als mündliche Mitteilungen und die Mysterienbücher - wie diese Verhältnisse dargestellt sind in dem «Christentum als mystische Tat­sache» -, aber von dem wirklichen Dasein des Christus Jesus haben sie sich überzeugt aus der Sternkonstellation, indem sie noch große Ken­ner waren des Zusammenhanges des Makrokosmos mit dem Mikrokos­mos.",
      "Sie haben eine Kenntnis davon gehabt, die man sich heute auch schon beschaffen kann, indem man die Sternkonstellation für den be­treffenden Punkt der Weltgeschichte berechnet und sagt: Wenn die Sternkonstellation so und so ist, so muß Der auf der Erde gelebt haben,",
      "welcher als der Christus bezeichnet wird. - So haben sich die Schreiber des Matthäus-, Markus- und Lukas-Evangeliums von dem ge­schichtlichen Geschehen überzeugt. Denn den Inhalt haben sie auf hellseherischem Wege gewonnen, aber die Überzeugung haben sie sich verschafft auf eine Weise, wie man sich durch die Konstellationen des Makrokosmos eine Überzeugung davon verschafft, daß auf der Erde dieses oder jenes vor sich gehen kann. Daher kann ihnen auch nur Glauben beibringen der, welcher so etwas weiß. Beweisen die Unrich­tigkeit dessen, was da vorgebracht wird gegen die Historizität der Evangelien, ist eine vergebliche Aufgabe. Wir müssen uns vielmehr als Anthroposophen klar sein, daß wir uns auf einen ganz anderen Boden stellen müssen: auf den Boden desjenigen, was wir uns nur durch eine Einsicht in die okkulte Wissenschaft verschaffen können.",
      "Ich möchte gerade auch hier dieser Erscheinung gegenüber auf etwas hinweisen, wodurch ich schon an einem anderen Orte zu begründen versuchte, wie man mit richtigen Einwänden, das heißt mit Einwän-den, die an sich richtig sind, die Wirklichkeiten nicht treffen kann, von denen die Geisteswissenschaft redet, so daß die Menschen noch so viel Richtiges sagen können, was nach ihrem Wissen richtig ist, es widerlegt die Geisteswissenschaft nicht. Ich habe in dem Vortrag:",
      "«Wie begründet man Theosophie?», ein Gleichnis gebraucht und habe gesagt: Ein kleiner Junge mußte in einem Dorfe immer die Semmeln holen zum Frühstück seiner Familie. Man bekam nun in jenem Orte für zwei Kreuzer eine Semmel, und er bekam immer zehn Kreuzer mit. Nun brachte er - und es sei hierbei bemerkt, daß er kein großer Arithmetikus war - die Anzahl der Semmeln vom Greisler nach Hause und kümmerte sich nicht weiter darum. Nun wurde aber in die Familie ein Pflegesohn aufgenommen, der jetzt anstelle des anderen zum Greisler nach Semmeln geschickt wurde. Da der nun ein guter Arithmetikus war, so sagte er sich: Du gehst Semmeln holen, zehn Kreuzer hast du mitbekommen, für zwei Kreuzer gibt es eine Semmel, zehn durch zwei geteilt gibt fünf: also wirst du fünf Semmeln nach Hause bringen. Er ging fort, aber er brachte sechs Semmeln nach Hause. Da sagte er sich: Das ist falsch, so viel kannst du nicht be­kommen, und da deine Rechnung richtig ist, so wirst du morgen schon",
      "fünf Semmeln nach Hause bringen. - Am nächsten Tage bekam er wieder zehn Kreuzer mit und brachte wieder sechs Semmeln nach Hause. Die Rechnung war richtig, nur stimmte sie nicht mit der Wirk­lichkeit, denn in der Wirklichkeit war es anders. In der Wirklichkeit war es nämlich an jenem Orte üblich, daß jemand, der für zehn Kreu­zer Semmeln kaufte, auf fünf eine drauf bekam, also statt fünf sechs. Der Einwand des Knaben war also richtig - nur stimmte er nicht mit der Wirklichkeit.",
      "So können die scharfsinnigst ausgedachten Einwände gegen die Geisteswissenschaft alle stimmen, brauchen aber nichts zu tun zu haben mit der Realität, denn die Realität kann auf ganz anderen Untergründen fußen. Es ist dieses angeführte Beispiel ganz praktisch, um sich klarzumachen, auch erkenntnistheoretisch, was in der Berech­nung richtig ist, und was in dem Wahrhaftigen richtig ist.",
      "Damit haben wir in unseren Bemühungen, die Welt der Maja zu­rückzuführen auf das Wahrhaftige - wobei sich uns gezeigt hat, daß alles Feuer Opfer ist, alles Luftartige strömende, spendende oder schenkende Tugend, und alles Flüssige Verzichtleistung, Resignation -, heute zu diesen drei Wahrheiten diejenige hinzugefügt, daß das wahre Wesen der Erde oder des Festen der Tod ist, das Abgeschnürtsein von seinem Weltensinn bei irgendeiner Substantialität. Dadurch aber, daß diese Abgeschnürtheit eintritt, tritt der Tod selber als ein Wahrhaf­tiges herein in die Welt der Maja oder der Illusion. Die Götter selbst könnten den Tod nicht einmal kennenlernen, wenn sie nicht in irgend­einer Weise herunterstiegen in die physische Welt, um den Tod in der physischen Welt, in der Welt der Maja oder der Illusion, zu begreifen.",
      "Das ist es, was wir heute hinzufügen wollen zu den Begriffen, die wir schon aufgenommen haben. Noch einmal sei es bemerkt, daß wir zur Klarheit über diese Begriffe, die uns aber notwendig sein werden zu einem gründlichen Eingehen auf so mancherlei im Markus-Evan­gelium, nur kommen können durch sorgfältige Meditation, und indem wir es öfter und öfter vor die Seele ziehen lassen. Denn das Markus-Evangelium ist nur zu begreifen, wenn man die allerbedeutsamsten Weltbegriffe dem zugrunde legt."
    ],
    "sentences": [
      [
        "So haben wir uns denn in einer Reihe von Betrachtungen vor die Seele geführt, wie hinter alledem, was wir die Maja oder die große Illusion nennen, das Geistige steht.",
        "Wir wollen noch einmal uns die Frage stellen: In welcher Art hat sich uns denn gezeigt, daß hinter allem, was wir zunächst für unsere Sinne und für unsere sonstige an unseren Leib gebundene Weltenauffassung um uns herum haben, das Geistige zunächst von uns erkannt worden ist?"
      ],
      [
        "Wir haben es dadurch charakterisiert, dieses Geistige, daß wir im Laufe der letzten Betrachtungen genötigt waren, gleichsam vor unse­rem Blick hinwegzuschaffen die nächsten äußeren Welterscheinungen und durchzudringen bis zu solchen Eigenschaften des Wirklichen, wie die waren, die wir bezeichneten als Opferwilligkeit, schenkende Tu­gend oder Verzicht, also lauter Eigenschaften, die wir nur kennenler­nen können, wenn wir in unsere eigene Seele blicken, die wir sinnvoll zunächst nur unserer eigenen Seele beilegen können.",
        "Wenn wir nun demjenigen, was wir als das Wirkliche, wir könnten auch sagen, als das Wahrhaftige hinter der Welt der Illusion zu denken haben, in sei­ner Wahrheit solche Eigenschaften beilegen müssen, wie die eben ge­nannten, so müssen wir sagen: In dieser Welt des wahrhaftigen Da­seins, in dieser Welt des Wirklichen lebt dasjenige, was wir seinen Eigenschaften nach im Grunde genommen nur vergleichen können mit Eigenschaften, die wir zunächst an unserer eigenen Seele wahrnehmen.",
        "Wenn wir zum Beispiel das, was sich äußerlich ausdrückt im Scheine der Wärme, zu charakterisieren haben in bezug auf seine Wahrheit als Opferdienst, als strömendes Opfer in der Welt, so heißt das eben, daß wir das Element der Wärme zurückgeführt haben auf ein Spirituelles, auf ein Geistiges, gleichsam also hinweggeschafft haben, was der äußere Schleier des Daseins ist, und das aufgezeigt haben, was in der Außenwelt gleich ist demjenigen, was wir als unser eigenes Spirituelles erkennen."
      ],
      [
        "Bevor wir nun in den Betrachtungen weitergehen, ist uns eine an­dere Idee notwendig.",
        "Das ist die: Verfliegt denn nun wirklich alles,"
      ],
      [
        "was wir innerhalb der Welt der Maja oder der großen Illusion haben, in eine Art von Nichtigkeit?",
        "Ist wirklich in all dieser uns umgebenden Sinnenwelt und der Welt unserer äußeren Auffassung gar nichts, was sich sozusagen darstellt als das Wahrhaftige oder als ein Wahr­haftiges?"
      ],
      [
        "Es wäre ja gewiß ein guter Vergleich, wenn man sagen würde: die Welt der Wahrheit, die Welt der Wirklichkeit sei zunächst verborgen, wie die inneren Kräfte eines Teiches oder selbst des Ozeans in der Wassermasse verborgen sind; und die Welt der Maja könnten wir ver­gleichen mit dem Wellenkräuselspiel, das sich an der Oberfläche ab­spielt.",
        "Der Vergleich wäre gut, aber er zeigt uns gerade, daß doch un­ten etwas im Ozean ist von dem, was das Wellenkräuselspiel oben be­wirkt als das Substantielle des Wassers und auch das Konfigurelle der Kraft.",
        "So ist es gleichgültig, ob wir diesen oder einen anderen Ver­gleich wählen.",
        "Wir können wohl die Frage aufwerfen: Gibt es nicht auch im weiten Reiche unserer Maja oder Illusion etwas, was «wirk­lich» ist?"
      ],
      [
        "Wir wollen es heute ebenso machen, wie wir es bei den letzten Be­trachtungen gemacht haben.",
        "Wir werden uns dem, was wir uns vor die Seele führen wollen, langsam nähern, indem wir ausgehen von inneren Erlebnissen unserer Seele.",
        "Und zwar, weil wir uns durch das Saturn-, Sonnen- und Mondendasein spirituell vorwärtsbewegt haben und jetzt zum Erdendasein heranrücken, wollen wir von noch naheliegenderen, man möchte sagen, gewöhnlicheren Seelenerlebnissen ausgehen, als wir es das letzte Mal taten.",
        "Das letzte Mal gingen wir aus von den verborge­nen Tiefen des Seelenlebens, von dem, was heraufragt aus dem, was wir in der Geisteswissenschaft kennengelernt haben als unseren astra­lischen Leib.",
        "Da haben wir heraufragen gefühlt die Sehnsucht, und wir haben gesehen, wie zunächst die Sehnsucht arbeitet in dem Wesen des Menschen, und wie sie es ist, die eigentlich das Seelenleben dahin führt, Befriedigung nur in dem Entgegenkommen jener Bilderwelt zu finden, die wir als die innere Bewegung dieses Seelenlebens haben auf­fassen können.",
        "Und dadurch haben wir den Weg gefunden von der mikrokosmischen Seele bis zu jenem Weltenschaffen, das wir zuge­schrieben haben den Geistern der Bewegung."
      ],
      [
        "Heute wollen wir noch von einem nähergehenden Erlebnis der Seele ausgehen, und zwar von einem Erlebnis, auf das schon aufmerksam gemacht worden ist im alten Griechenland, das aber in seiner Wahr­heit noch heute ein tief bedeutsames ist, und das angedeutet wird durch die Worte: Alle Philosophie, also alles Streben nach einem gewissen menschlichen Wissen gehe aus von dem Staunen. - Das ist in der Tat richtig.",
        "Wer nur ein wenig reflektiert und achtgibt auf den ganzen Vorgang im Erleben seiner Seele, wie er sich nähert irgendeinem Wis­sen, der wird schon an sich selbst erfahren können, daß ein gesunder Weg zum Wissen immer seinen Ausgangspunkt findet von dem Staunen, von der Verwunderung über irgend etwas."
      ],
      [
        "Dieses Staunen, diese Verwunde­rung, von der jeder Wissensprozeß auszugehen hat, gehört geradezu zu jenen seelischen Erlebnissen, die wir bezeichnen müssen als diejenigen, welche in alles Nüchterne Hoheit und Leben hineinbringen.",
        "Denn, was wäre irgendein Wissen, das in unserer Seele Platz greift, das nicht ausginge von dem Staunen?"
      ],
      [
        "Es wäre wahrhaftig ein Wissen, das ganz einge­taucht sein müßte in Nüchternheit, in Pedanterie.",
        "Allein jener Prozeß, der sich abspielt in der Seele, der von der Verwunderung hinführt zu der Beseligung, die wir empfangen von den gelösten Rätseln, und der sich zuerst über der Verwunderung erhoben hat, macht das Hoheits­volle und das innerlich Lebendige des Wissensprozesses aus."
      ],
      [
        "Man sollte eigentlich fühlen das Trockene und Vertrocknende eines Wissens, das nicht von diesen beiden Gemütsbewegungen sozusagen eingesäumt ist.",
        "Eingerahmt von Staunen und von Beseligung über das gelöste Rätsel ist das gesunde Wissen."
      ],
      [
        "Alles andere Wissen kann von außen ange­eignet sein, kann von dem Menschen aus diesem oder jenem Grund herangebracht sein.",
        "Aber ein Wissen, das nicht eingerahmt ist von diesen beiden Gemütsbewegungen, ist nicht wirklich im Ernste aus der Menschenseele entsprungen."
      ],
      [
        "Alles Aroma des Wissens, das die Atmosphäre des Lebendigen im Wissen bildet, geht aus von diesen zwei Dingen, von Staunen und Beseligung über das erfüllte Staunen."
      ],
      [
        "Was für einen Ursprung hat aber das Staunen selbst?",
        "Warum tritt Staunen - also Verwunderung über irgendein Außeres - in unserer Seele auf?",
        "Es tritt Staunen, Verwunderung aus dem Grunde auf, weil wir uns zunächst irgendeinem Wesen oder einem Ding oder einer Tatsache"
      ],
      [
        "gegenüber, die vor uns auftritt, fremd angemutet fühlen.",
        "Die Fremdheit ist das erste Element, das zur Verwunderung, zum Staunen führt.",
        "Aber nicht allem Fremden gegenüber empfinden wir das Stau­nen, die Verwunderung, sondern nur einem solchen Fremden gegen­über, mit dem wir uns doch in einer gewissen Weise verwandt fühlen, so verwandt fühlen, daß wir uns sagen: Es ist etwas in dem Ding oder Wesen, das jetzt noch nicht in mir ist, das aber in mich übergehen kann. - Also zugleich verwandt und fremd fühlen wir uns einer Sache gegenüber, die wir durch Verwunderung, durch ein Staunen zunächst erfassen."
      ],
      [
        "Mit dem Worte «Verwunderung» hängt dann auch das Wort «Wun­der» zusammen, das wir eine:n Ereignis beilegen, zu dem der Mensch zunächst in seiner Erkenntnis keine verwandtschaftliche Beziehung finden kann.",
        "Aber das kann ja nur an ihm liegen, oder braucht wenig­stens nur an ihm zu liegen."
      ],
      [
        "Und er würde sich gar nicht selbst in ab­lehnender Weise zu dem verhalten, was er als «Wunder» bezeichnet, wenn er nicht in einer gewissen Weise doch Anspruch darauf machen würde, daß es sich ihm erschließt, also in einer gewissen Weise doch verwandt mit ihm sein sollte.",
        "Denn warum leugnen die Menschen, die von materialistischen oder rein verstandesmäßigen Begriffen ausgehen, zum Beispiel dasjenige, was andere anerkennen als Wunder, wenn sie nicht direkte Beweise dafür haben, daß eine Lüge, eine Unwahrheit vorliegt?"
      ],
      [
        "Das müssen heute selbst schon Philosophen zugeben, daß man aus den Erscheinungen der Welt, welche dem Menschen vorliegen, niemals beweisen könne, dad zum Beispiel der in dem Jesus von Nazareth inkarnierte Christus nicht auferstanden sei.",
        "Man kann Gründe dagegen anführen."
      ],
      [
        "Aber wie sind diese Gründe?",
        "Sie sind lo­gisch nicht haltbar!",
        "Das geben heute schon aufgeklärte Philosophen zu.",
        "Denn die Gründe, welche von materialistischer Seite beigebracht werden, zum Beispiel daß alle Menschen, welche diese Leute bisher ge­sehen haben, zunächst nicht so auferstehen wie der Christus, diese Gründe stehen auf derselben Höhe wie der, daß jemand bisher nur Fische gesehen hat und aus der Beschaffenheit der Fische nun nachwei­sen will, daß es keine Vögel gibt."
      ],
      [
        "Man kann nie aus der einen Klasse von Wesenheiten in logisch berechtigter Weise ableiten, daß andere"
      ],
      [
        "Wesen nicht existieren.",
        "Ebensowenig kann man aus den Erfahrungen, welche man über die Menschen des physischen Planes machen kann, etwas ableiten - was als Wunder zunächst bezeichnet wird - über die Ereignisse von Golgatha.",
        "Wenn Sie aber einem Menschen etwas mit­teilen, was er als Wunder bezeichnen müßte, wenn die Sache auch wahr wäre, und er sagt: Ich kann sie nicht verstehen -, so widerspricht er damit nicht dem, was wir über den Begriff der Verwunderung ge­sagt haben; denn er zeigt in seinem Verhalten ganz klar, daß dieser Ausgangspunkt alles Wissens für ihn auch begründet ist.",
        "Er verlangt nämlich, daß das, was ihm mitgeteilt wird, ein ihm Verwandtes habe.",
        "Er will, daß es in einer gewissen Weise sein Eigentum werden kann im Geistigen, und da er glaubt, daß er das nicht haben könne, daß es nicht mit ihm verwandt ist, so lehnt er es ab.",
        "Selbst wenn wir bis zum Wun­derbegriff selbst herangehen, würden wir sehen, daß Verwundern oder Erstaunen, von dem schon im Sinne des alten Griechentums alle Philo­sophie ausgegangen ist, darauf beruht, daß sich der Mensch gegenüber befindet einem Fremden, es aber doch als ein Verwandtes anerkennen muß.",
        "Versuchen wir nun eine Verbindungsbrücke zu schaffen zwi­schen diesen Begriffen und dem, was wir das letzte Mal vor unsere Seele geführt haben."
      ],
      [
        "Wir haben das letzte Mal gezeigt, wie ein gewisser Fortschritt in der Evolution dadurch herbeigeführt wird, daß Wesen bereit sind zu opfern, Opfer darzubringen, daß aber diese Opfer verweigert, zurück­gewiesen werden, und wir haben in den zurückgewiesenen Opfern eine der Haupttatsachen erkannt, welche während der alten Monden­entwickelung gespielt haben.",
        "Es gehört zu dem Wesentlichsten der alten Mondenentwickelung, daß damals von gewissen Wesen an höhere Wesenheiten Opfer dargebracht werden sollten, auf welche diese höheren Wesenheiten verzichteten, so daß also gleichsam der Opferrauch der alten Mondwesen hinaufdrang zu den höheren Wesen­heiten, aber von ihnen nicht angenommen wurde und zurückgeleitet wurde als Substanz in die Wesenheiten, welche das Opfer darbringen wollten.",
        "Und wir haben gesehen, daß ein großer Teil der Eigentümlich­keit der Wesen des alten Mondes darin bestand, daß sie dasjenige in sich zurückgestoßen fühlen, was sie von sich selbst hinaufsenden wollten"
      ],
      [
        "zu höheren Wesenheiten als Opfersubstanz.",
        "Ja, wir haben gesehen, daß das, was da hinauf wollte zu den höheren Wesenheiten und nicht konnte, eben zurückblieb in den betreffenden Wesenheiten, und sich dadurch in diesen Wesenheiten des zurückgewiesenen Opfers als die Kraft der Sehnsucht herausgebildet hatte.",
        "Und wir haben noch immer in alledem, was wir in unserer eigenen Seele als Sehnsucht empfinden, eine Erbschaft jener alten Mondenvorgänge, die darin bestehen, daß Wesen damals ihr Opfer nicht angenommen fanden.",
        "Der ganze Charakter der alten Mondenentwickelung, spirituell erfaßt, die ganze geistige Atmosphäre des alten Mondes läßt sich in vieler Beziehung so charakterisieren, daß Wesen auf dem alten Monde sind, die ihre Opfer darbringen wollen, aber finden, daß diese Opfer, weil die höheren Wesenheiten in bezug auf sie resignieren, nicht angenommen werden.",
        "Das ist der eigenartige Grundzug in der spirituellen alten Monden­atmosphäre: das zurückgewiesene Opfer.",
        "Und das zurückgewiesene Opfer des Kain, in dem symbolisch einer der Ausgangspunkte un­serer Erdenmenschheitsevolution angezeigt ist, erscheint uns wie eine Art Wiederholung des Grundzuges der alten Mondenentwicke­lung, der sich da abspielt in der Seele des Kain, der sein Opfer nicht angenommen sieht.",
        "Das ist etwas, was uns wie versinnbildlichen kann ein Leid, einen Schmerz, welche die Sehnsucht gebären, wie es bei den Wesen des alten Mondendaseins der Fall war."
      ],
      [
        "Wir haben nun das letzte Mal schon gesehen, daß zwischen diesen nicht angenommenen Opfern und zwischen der Sehnsucht, die da­durch in den Wesenheiten entstanden ist, daß das Opfer nicht ange­nommen worden ist, gewissermaßen ein Ausgleich geschaffen wurde, indem auf dem alten Monde die Geister der Bewegung auftraten.",
        "Dadurch wurde wenigstens die Möglichkeit geschaffen, daß die Sehn­sucht, die entstanden war bei den Wesen des zurückgewiesenen Opfers, in einer gewissen Art befriedigt werden konnte.",
        "Stellen Sie sich das recht lebendig vor, Sie haben höhere Wesenheiten, denen geopfert wer­den soll, aber die Opfersubstanzen werden zurückgewiesen.",
        "Sehnsucht entsteht dadurch in diesen Wesen, welche opfern wollten, und die nun fühlen: Hätte ich mein Opfer jenen höheren Wesen darbringen kön­nen, so würde das Beste meines eigenen Wesens bei diesen Wesen leben,"
      ],
      [
        "ich selber würde in diesen höheren Wesenheiten leben, so aber bin ich ausgeschlossen von diesen Wesenheiten, so stehe ich hier, und diese hö­heren Wesenheiten stehen dort! - Die Geister der Bewegung aber - wir können das fast wörtlich verstehen - bringen diese Wesenheiten, in denen durch das zurückgewiesene Opfer aufglimmt die Sehnsucht nach den höheren Wesenheiten, in solche Lagen, daß sie sich von den ver­schiedensten Seiten nähern können den höheren Wesenheiten.",
        "So daß das, was in ihnen ruht als nicht darzubringendes Opfer, wenigstens durch die Fülle der Eindrücke, die empfangen werden von den höhe­ren Wesen, welche gleichsam umkreist werden von den Wesen des zu­rückgewiesenen Opfers, ausgeglichen werden kann; ausgeglichen, was durch das Zurückweisen des Opfers nicht befriedigt wird, indem in der Position dieser Wesen zu den höheren Wesenheiten eine Beziehung entsteht, wie sie durch ein dargebrachtes Opfer ausgedrückt werden kann."
      ],
      [
        "Wir machen uns völlig verständlich, was damit gemeint ist, wenn wir uns denken, symbolisch zusammengefaßt, die höheren Wesenheiten als Sonne, und dann in einer einzigen Position, als einen Planeten, nie­drigere Wesenheiten zusammengefaßt.",
        "Nehmen wir nun an, die Wesen des niederen Planeten wollten dem höheren Planeten, also der Sonne, ihre Opfer darbringen.",
        "Aber die Sonneweist sie zurück, und dieOpfer­substanzen müssen bleiben bei den Wesenheiten des nicht angenom­menen Opfers, dabei fühlen sich diese Wesen voll von Sehnsucht in ihrer Einsamkeit, in ihrer Abgeschlossenheit.",
        "Nun bringen die Geister der Bewegung sie in den Umkreis der höheren Wesenheiten; dadurch ist es ihnen erst möglich, an die Stelle des unmittelbaren Hinauf­fließens ihrer Opfersubstanz, diese Opfersubstanz selbst in Bewegung zu bringen und sie dadurch in eine Beziehung zu bringen zu den We­sen höherer Art.",
        "Es ist das geradezu so, als wenn ein Mensch nicht in der Lage ist, durch eine einmalige große Befriedigung mit sich zurecht­zukommen und dann eine Reihe Teilbefriedigungen erlebt: so daß also sein ganzes Gemüt in Bewegung kommt, wenn er so eine Reihe Teil­befriedigungen erlebt.",
        "Das haben wir das letzte Mal genauer beschrie­ben.",
        "Wir haben gesehen, wie durch die Eindrücke, die nun von außen kommen, weil sich das Wesen nicht innerlich in der Opferung mit den"
      ],
      [
        "höheren Wesenheiten vereinigt fühlt, ein Ersatz entsteht; das konnte uns zeigen, wie solche Wesen dennoch zu einer gewissen Befriedigung kommen."
      ],
      [
        "Nun aber kann doch nicht geleugnet werden, daß das, was hätte geopfert werden sollen, in anderer Weise bei den höheren Wesen fort­bestehen würde als bei den niederen Wesen.",
        "Denn die eigentlichen Da­seinsbedingungen dessen, was hätte geopfert werden sollen, liegen bei den höheren Wesen.",
        "Bei den niederen Wesen müssen also andere Da­seinsbedingungen dafür eintreten. - Wiederum können wir uns dazu bildlich vorstellen: Wenn von einem Planeten die ganze Substanz, die er enthält, in die Sonne fließen könnte und die Sonne sie nicht zurück­weisen würde, so würden die Wesen dieses Planeten in der Sonne an­dere Daseinsbedingungen finden als sonst, wenn die Sonne sie zurück-weist, außerhalb der Sonne im Planeten.",
        "Kurz: Eine Entfremdung dessen, was wir den «Inhalt des Opfers» nennen müssen, tritt ein, eine Entfremdung dieser Opfersubstanz von ihrem Ursprung."
      ],
      [
        "Fassen Sie nun diesen Gedanken, daß Wesenheiten etwas in sich behalten müssen, was sie gern als Opfer darbringen würden, und wo­von sie das Gefühl und die Empfindung haben, daß es erst dann seinen rechten Sinn fände, wenn es als Opfer dargebracht werden könnte.",
        "Vergegenwärtigen Sie sich die Empfindungen solcher Wesenheiten, dann werden Sie das haben, was man nennen kann: Abgeschlossenheit eines gewissen Teiles der Weltenwesenheit gegenüber seinem eigent­lichen Sinn und gegenüber seinem eigentlichen großen Weltenzweck.",
        "Es haben Wesen etwas in sich, was eigentlich - wenn wir bildlich spre­chen dürften - an einem anderen Orte als bei ihnen selber seinen Sinn hätte.",
        "Die Folge davon ist, daß diese Deplacierung - wenn wir wieder bildlich sprechen - des zurückgewiesenen Opferrauches, der zurück­gewiesenen Opfersubstanz, ein Ausgeschlossenwerden zunächst dieser Opfersubstanz von dem übrigen Weltenprozeß bewirkt."
      ],
      [
        "Wenn Sie diesen Gedanken nicht mit Ihrem Verstande - denn der geht nicht auf solche Dinge -, sondern wenn Sie mit Ihrem Gefühl das fassen, was damit ausgesprochen ist, so werden Sie die Empfindung haben: Es ist etwas wie ein Herausreißen aus dem allgemeinen Welten-prozeß.",
        "Für die Wesen, die das Opfer zurückgewiesen haben, ist es nur"
      ],
      [
        "etwas, was sie von sich abgestoßen haben.",
        "Für die anderen Wesen, in denen die Opfersubstanz geblieben ist, ist es etwas, dem der Charakter der Fremdheit seines eigenen Ursprunges aufgedrückt wird.",
        "Wir haben also dadurch Wesen, denen in ihrer Substantialität die Fremdheit von seinem Ursprunge aufgedrückt ist.",
        "Es ist, wenn man sich gefühlsmäßig diese Dinge vor die Seele malt, etwas, dem die Fremdheit seines Ur­sprunges innewohnt: Das ist der Tod!",
        "Und nichts anderes ist der Tod im Weltenall als das, was notwendig eintritt mit der zurückgewiesenen Opfersubstanz bei den Wesen, die eben diese Opfersubstanz behalten müssen.",
        "So kommen wir von der Resignation, von dem Verzicht, den wir gefunden haben auf der dritten Stufe der Evolution, gegenüber dem, worauf von den höheren Wesen verzichtet worden ist, zum Tod.",
        "Und der Tod in seiner wahren Bedeutung ist nichts anderes als die Eigenschaft von Wesensinhalten, die nicht an ihrem wahren Orte sind, die ausgeschlossen von ihrem wahren Orte sind."
      ],
      [
        "Auch wenn der Tod im konkreten Leben beim Menschen eintritt, liegt dasselbe zugrunde.",
        "Denn wenn wir uns den Leichnam besehen, der in der Welt der Maja zurückbleibt, so ist in ihm nichts anderes ent­halten als eine Substantialität, die mit dem Moment des Todes aus­geschlossen ist von Ich, Astralleib und Ätherleib, die entfremdet ist demjenigen, innerhalb dessen sie nur einen eigentlichen Sinn hat.",
        "Denn des Menschen physischer Leib hat keinen Sinn ohne Atherleib, Astral­leib und Ich, ist sinnlos, ist in diesem Moment von seinem Sinn aus­geschlossen.",
        "Was wir nicht mehr durchschauen können, wenn ein Mensch stirbt, das stellt sich uns eben dar im Makrokosmos.",
        "Dadurch, daß die Weltenwesen höherer Sphären zurückweisen, was ihnen als Opfer dargebracht werden soll, verfällt diese zurückgewiesene Opfer-substanz in den Wesenheiten, denen sie zurückgewiesen worden ist, dem Tode, denn der Tod ist Ausgeschlossenwerden irgendeiner Wel­tensubstanz, irgendeiner Weltenwesenheit von seinem eigentlichen Sinn."
      ],
      [
        "Damit aber sind wir eingetreten in eine spirituelle Charakteristik desjenigen, was wir das vierte Element im Weltall nennen.",
        "Wenn uns das Feuer reinster Opfersinn war - und überall, wo uns Feuer oder Wärme entgegentritt, liegt spirituell dahinter Opferung -, wenn wir"
      ],
      [
        "hinter allem, was als Luft ausgebreitet ist um unsere Erde herum, schenkende oder spendende Tugend, hinströmende Tugend in Wahr­heit fanden, wenn wir charakterisieren konnten das fließende Wasser, also Flüßigkeit als Element, als spirituelle Resignation oder Verzicht, so müssen wir das Element der Erde, das allein der Träger des Todes werden kann - denn der Tod würde nicht da sein, wenn das Element der Erde nicht da wäre -, als dasjenige charakterisieren, was abgespal­ten worden ist von seinem Sinn durch den Verzicht.",
        "Jetzt haben Sie förmlich konkret irgend etwas, wo sich aus Flüssigem Festes bildet.",
        "Denn das spiegelt in einer gewissen Weise auch einen spirituellen Pro­zeß.",
        "Stellen wir uns vor, es gliedert sich ein in die Wassermasse eines Teiches Eis, das Wasser also wird fest.",
        "In Wahrheit liegt da nichts an­deres zugrunde, als daß dasjenige, was das Wasser zu Eis werden läßt, es abschnürt von dem Sinn des Wassers.",
        "Da haben Sie das Spirituelle des Festwerdens, das Spirituelle des Erdewerdens.",
        "Denn in bezug auf die Charakteristik der vier Elemente ist das Eis ebenfalls «Erde» und nur das Flüssige «Wasser».",
        "Und das, worin der Tod sich darstellt, sich auslebt, das ist das Element der Erde."
      ],
      [
        "Wir sind ausgegangen davon, daß wir die Frage aufgeworfen haben, ob es innerhalb unserer Welt der Illusion, der Maja, gar nichts Wahr­haftiges gibt, ob es dort gar nichts von dem gibt, was sozusagen einer Wirklichkeit entspricht?",
        "Nehmen Sie einmal jetzt recht genau den Be­griff, den wir eben vor unsere Seele hingestellt haben.",
        "Ich habe Ihnen von Anfang an gesagt: die Begriffe dieser unserer Betrachtungen sind einigermaßen kompliziert.",
        "Es wird also notwendig sein, daß wir sie nicht nur verstandesmäßig aufnehmen, sondern darüber meditieren, dann werden sie uns erst ganz klar werden.",
        "Aber nehmen wir jetzt diesen Begriff vom Tode beziehungsweise vom Erdigen; er zeigt uns ein ganz merkwürdiges Gesicht.",
        "Während wir bei allen anderen Be­griffen uns sagen konnten: In bezug auf das, was da in der Welt der Maja um uns herum ist, liegt eigentlich gar nichts Wahrhaftiges vor, sondern das Wahrhaftige ist ein ihm zugrunde liegendes Spirituelles -, haben wir jetzt etwas herausbekommen, wo dasjenige, was wir inner­halb der Maja haben, eigentlich gerade deshalb, weil es getrennt ist von seinem Sinn, weil es im Spirituellen sein sollte, sich als das Tote"
      ],
      [
        "charakterisiert.",
        "Es ist damit in die Maja hinein etwas abgeschnürt, was eigentlich nicht in der Maja sein sollte.",
        "Überall im ganzen weiten Reiche der Maja oder der großen Illusion haben wir eben lauter Täu­schungen, lauter Illusionen vor uns.",
        "Aber wir bekommen etwas in die Maja hinein, was dadurch einem Wahrhaftigen entspricht, daß es ab­geschnürt wird von seinem eigentlichen Sinn im Spirituellen, und in dem Augenblick, wo es hereinkommt, tritt an es die Vernichtung, der Tod heran.",
        "Das sagt uns aber nichts Geringeres als die große okkulte Wahrheit: Innerhalb der Welt der Maja ist das einzige, das sich in seiner Wirklichkeit zeigt, der Tod! - Alle anderen Erscheinungen müs­sen wir zurückverfolgen auf ihr Wirkliches, alle anderen Erscheinun­gen, die in der Maja auftreten, haben hinter sich das Wahrhaftige:"
      ],
      [
        "Nur der Tod ist innerhalb der Maja das Wahrhaftige, denn er besteht darin, daß von dem Wahrhaftigen etwas abgeschnürt und herein­genommen ist in die Maja.",
        "Daher ist der Tod innerhalb der Maja das einzig Wahrhaftige."
      ],
      [
        "Und wenn wir jetzt von dem, man möchte sagen, in der allgemeinen Maja sich Ausbreitenden übergehen zu den großen Prinzipien der Welt, dann stellt sich für die okkulte Wissenschaft eine sehr wichtige und wesentliche Konsequenz dieses Satzes dar, daß innerhalb unserer Welt der Maja nur der Tod eigentlich das Wahrhaftige ist.",
        "Wir kön­nen uns dem, was ich hier sagen will, noch von einer anderen Seite nähern.",
        "Wir können zunächst die Wesenheiten der anderen Reiche be­trachten, die um uns herum sind.",
        "Wir können fragen: Sterben zum Beispiel Mineralien? - Für den Okkultisten hat es keinen Sinn zu sa­gen: Mineralien sterben. - Das wäre ungefähr ebensoviel, als wenn man sagen würde, der Fingernagel, den wir uns abschneiden, sei ge­storben.",
        "Der Fingernagel ist eben nicht irgend etwas, was als Totalität Anspruch hat auf Dasein, sondern er ist etwas an uns, und wenn wir ihn abschneiden, so haben wir ihn von uns getrennt und ihm das mit uns zusammenhängende Leben entrissen.",
        "Er stirbt im Grunde genom­men erst dann, wenn wir selber sterben.",
        "Also in demselben Sinne, sagt die okkulte Wissenschaft, sterben die Mineralien nicht.",
        "Denn die Mine­ralien sind nur Glieder an einem großen Organismus, wie der Finger­nagel an unserem Organismus ein Glied ist; und wenn ein Mineral"
      ],
      [
        "scheinbar zugrunde geht, so ist es nur losgerissen von diesem großen Organismus, wie das Stück Fingernagel losgerissen ist von unserem Organismus, wenn wir es abschneiden.",
        "Die Zerstörung des Minerals ist kein Tod, denn das Mineral lebt nicht in sich selber, sondern in dem großen Organismus, von dem es ein Glied ist. - Wenn Sie sich erinnern an den Vortrag über das Wesen der Pflanzen, so werden Sie wissen, daß gesagt worden ist: Die Pflanze ist als solche auch nicht selbständig, sondern sie ist ein Glied, nun nicht wie das Mineral an einem großen Organismus, sondern an dem ganzen Erdenorganismus; und es hat für eine okkulte Betrachtung keinen Sinn, von einzelnen Pflanzenorganismen zu sprechen, sondern man muß sprechen von dem Erdenorganismus, an dem die Pflanzen überall Teile sind."
      ],
      [
        "Und wenn wir sie zu ihrem «Tode» bringen, dann ist es so, wie wenn wir uns einen Fingernagel abschneiden.",
        "Wir können nicht sagen, der Finger­nagel ist gestorben.",
        "Ebensowenig können wir dies von den Pflanzen sagen, denn sie gehören einem großen Organismus an, der identisch ist mit der ganzen Erde und der ein Organismus ist, der im Frühling ein­schläft, die Pflanzen als seine Organe der Sonne entgegensendet und sie im Herbst wieder in sich aufnimmt, wenn er die Samen der Pflan­zen in sich aufnimmt."
      ],
      [
        "Es hat keinen Sinn, die Pflanzen für sich allein zu betrachten, denn der Erdenorganismus stirbt nicht ab, wenn die ein­zelnen Pflanzen an ihm verwelken, ebenso wie wir, wenn wir graue Haare bekommen, auch nicht sterben, wenn wir die grauen Haare nicht wieder auf naturgemäße Weise in schwarze färben können.",
        "Nur sind wir da in einer anderen Lage als die Pflanzen."
      ],
      [
        "Aber die Erde ist da in einer solchen Lage, die sich vergleichen ließe mit dem Menschen, wenn er graue Haare wieder in schwarze zurückverwandeln könnte.",
        "Also die Erde stirbt nicht, sondern was sich da zeigt im Welken der Pflanzen, ist ein Prozeß, der sich an der Oberfläche abspielt."
      ],
      [
        "So kön­nen wir niemals sagen, daß die Pflanzen in Wahrheit sterben.",
        "Aber auch von den Tieren können wir zunächst nicht sagen, daß sie wie wir sterben.",
        "Denn das einzelne Tier ist in Wahrheit auch nicht vorhanden, es ist nur die Gruppenseele vorhanden, die im Übersinnlichen ist."
      ],
      [
        "Was das Tier im Wahrhaftigen ist, das ist nur auf dem Astralplan vorhan­den als die Gruppenseele, und das einzelne Tier ist aus der Gruppenseele"
      ],
      [
        "heraus verdichtet.",
        "Und wenn es stirbt, so ist es ein abgelegtes Glied der Gruppenseele, und diese ersetzt es durch ein anderes."
      ],
      [
        "Was wir also als den Tod im Mineral-, Pflanzen- und Tierreich an­treffen, das ist nur scheinbar, ist nur innerhalb der Maja Tod.",
        "In Wahrheit stirbt wirklich nur der Mensch, der es mit seiner Individuali­tät so weit bringt, daß er hinunterkommt zu seinem physischen Leibe, in dem er während des Erdendaseins real werden muß.",
        "In Wahrheit hat von «Tod» zu sprechen nur einen Sinn für das Erdendasein des Menschen."
      ],
      [
        "Wenn wir dies ins Auge fassen, müssen wir sagen: Nur der Mensch kann eigentlich den Tod wirklich erleben. - Beim Menschen ist also das, was wir durch die okkulte Forschung kennenlernen, ein wirkliches Überwinden des Todes, ein wirkliches Besiegen des Todes.",
        "Denn bei anderen Wesen ist der Tod nur scheinbar, ist er nicht in Realität vor­handen."
      ],
      [
        "Wenn wir höher hinaufkommen würden, von dem Menschen wieder zu den Wesenheiten der höheren Hierarchien, so würden wir ebenso finden, daß diese den Tod nach Menschenart nicht kennen; so daß es im Grunde genommen nur bei jenen Wesenheiten einen realen Tod, das heißt, einen Tod auf dem physischen Plan gibt, die sich auch etwas zu holen haben auf dem physischen Plan.",
        "Der Mensch aber hat sich auf dem physischen Plan sein Ich-Bewußtsein zu holen."
      ],
      [
        "Das könnte er ohne den Tod nicht finden.",
        "Weder bei den Wesenheiten, die unter dem Menschen stehen, noch bei den Wesenheiten, die höher ste­hen als der Mensch, hat es einen Sinn, von wahrhaftem Tod zu spre­chen."
      ],
      [
        "Dann aber wird es begreiflich erscheinen, daß wir für jene We­senheit, die wir die Christus -Wesenheit nennen, gar keine Möglichkeit haben, ihre bedeutendste Erdentat auszulöschen.",
        "Denn wir haben ja gesehen, daß bei dieser Christus-Wesenheit das Mysterium von Gol­gatha als das Wesentlichste in Betracht kommt: die Besiegung des Todes durch das Leben."
      ],
      [
        "Wo aber kann diese Besiegung des Todes nur vor sich gehen?",
        "Kann sie vor sich gehen in den höheren Welten?",
        "Nein!",
        "Denn schon bei den niederen Wesen, die wir angeführt haben, im Mineral-, Pflanzen- und Tierreich, kann von Tod nicht gesprochen werden, weil sie eigentlich ihr wahres Wesen in den höheren, über­sinnlichen Welten haben."
      ],
      [
        "Und wir werden im Laufe der Winterbetrachtungen"
      ],
      [
        "noch weiter ausführen, daß auch bei den höheren We­senheiten nicht von Tod gesprochen werden kann, sondern nur von Verwandlungen, von Metamorphosen, von Umgestaltung.",
        "Von einem Einschnitt in das Leben, den wir als «Tod» bezeichnen, kann nur beim Menschen gesprochen werden.",
        "Und der Mensch kann diesen Tod nur erleben auf dem physischen Plan.",
        "Wäre der Mensch niemals auf den physischen Plan gekommen, so würde er nichts wissen vom Tod, denn kein Wesen, das den physischen Plan nicht betreten hat, weiß etwas vom Tod.",
        "Es gibt in den anderen Welten nicht das, was man «Tod» nennen kann, sondern nur Verwandlungen, Metamorphosen.",
        "Sollte der Christus durch den Tod gehen, so mußte er auf den physischen Plan heruntersteigen!",
        "Denn nur dort konnte er den Tod erleben."
      ],
      [
        "So sehen wir, daß auch im geschichtlichen Werden des Menschen in einer merkwürdigen Weise das Wahrhaftige der höheren Welten hereinspielt in die Maja.",
        "Während wir für alle anderen geschichtlichen Ereignisse mit unserem Denken nur dann zurechtkommen, wenn wir sagen: Hier auf dem physischen Plan ist das geschichtliche Ereignis, aber die Ursache dafür liegt oben in der geistigen Welt, zu der müssen wir gehen -, können wir von dem Ereignis von Golgatha nicht sagen:"
      ],
      [
        "Dieses Ereignis ist hier unten auf dem physischen Plan, und etwas Entsprechendes liegt in der höheren Welt. - Gewiß, der Christus selbst gehört den höheren Welten an und stieg herunter auf den physischen Plan.",
        "Aber ein Urbild, wie wir es für alle anderen geschichtlichen Ereignisse suchen müssen, gibt es nicht für das, was sich auf Golgatha vollzogen hat.",
        "Das hat sich nur auf dem physischen Plan abgespielt! -Unter den vielen Beweisen, die aus der okkulten Wissenschaft für diese Tatsache gegeben werden könnten, ist zum Beispiel dieses, daß das Ereignis von Damaskus sich, wie wir dies schon öfter dargestellt ha­ben, im Laufe der nächsten drei Jahrtausende für eine genügend große Anzahl von Menschen erneuern wird.",
        "Das heißt, es werden sich bei den Menschen solche Fähigkeiten entwickeln, daß sie den Christus auf dem astralischen Plan als Äthergestalt wahrnehmen werden, wie es bei Paulus vor Damaskus der Fall war.",
        "Dieses Ereignis des Wahrnehmens des Christus durch nach und nach bei den Menschen im Laufe der nächsten drei Jahrtausende sich entwickelnde höhere Fähigkeiten"
      ],
      [
        "macht seinen Anfang in unserem 20.",
        "Jahrhundert.",
        "Von da ab kommen diese Fähigkeiten allmählich heraus und werden in den nächsten drei Jahrtausenden bei einer genügend großen Anzahl von Menschen sich ausbilden.",
        "Das heißt, eine genügend große Anzahl von Menschen wird wissen durch den Hineinblick in die höheren Welten, daß der Christus eine Realität ist, daß er lebt, sie werden ihn kennenlernen, wie er jetzt lebt.",
        "Und sie werden nicht nur die Art kennenlernen, wie er jetzt lebt, sondern sie werden sich genau wie Paulus die Überzeugung verschaf­fen, daß er gestorben und auferstanden ist.",
        "Aber die Grundlage dazu kann nicht gelegt werden in den höheren Welten, die muß auf dem physischen Plan gelegt werden."
      ],
      [
        "Wenn also heute schon jemand dazu kommt, diese Dinge zu ver­stehen und zu begreifen, wie die Entwickelung des Christus selber vor­wärtsgeht und damit die Entwickelung gewisser menschlicher Fähig­keiten, wenn es jemand begreift, dadurch begreift, daß er die Geistes­wissenschaft heute versteht, so hindert nichts daran, daß er, wenn er durch die Pforte des Todes gegangen ist, an diesem Ereignis teilnimmt, wenn es wirklich als ein erstes Hereinleuchten des Christus in die Welt des Menschen sich darstellt.",
        "Derjenige also, der heute im physischen Leibe sich auf dieses Ereignis vorbereitet, kann es auch erleben in dem Leben zwischen dem Tode und einer neuen Geburt."
      ],
      [
        "Diejenigen Men­schen aber, die sich nicht darauf vorbereiten, die sich in dieser Inkar-nation kein Verständnis dafür erwerben, sie können in dem Leben, das sich an dieses anschließt zwischen dem Tode und einer neuen Geburt, nichts wissen von dem, was in bezug auf den Christus von unserem Jahrhunderte ab durch die nächsten drei Jahrtausende geschieht.",
        "Sie müssen warten, bis sie wieder inkarniert sind und weiter sich die Vor­bereitung dazu auf der Erde schaffen."
      ],
      [
        "Das also, was als die Ursache aller folgenden Christus-Entwickelung auf der Erde sich abspielen mußte, der Tod auf Golgatha, das kann auch nur innerhalb des phy­sischen Leibes begriffen werden.",
        "Das ist unter allen Tatsachen, die uns wichtig sind für das höhere Leben, das einzige, was nur innerhalb des physischen Leibes begriffen werden kann."
      ],
      [
        "Dann wird es weiter ver­arbeitet, wird es weiter ausgebildet in den höheren Welten.",
        "Aber be­griffen müssen wir es zunächst haben innerhalb des physischen Leibes."
      ],
      [
        "Gerade wie das Mysterium von Golgatha niemals sich hätte in den höheren Welten abspielen können, wie es auch kein Urbild hat in den höheren Welten, sondern ein Ereignis ist, das, weil es den Tod in sich schließt, abgeschlossen ist innerhalb des physischen Planes, so muß das Verständnis dafür auf dem physischen Plan erworben werden.",
        "Ja, es gehört sogar geradezu zu den Aufgaben des Menschen auf der Erde, in irgendeiner seiner Inkarnationen sich dieses Verständnis zu erwerben."
      ],
      [
        "Wir müssen also sagen, damit haben wir auch im Großen etwas ge­funden, was sozusagen auf dem physischen Plan uns ein unmittelbar Reales, ein unmittelbar Wahrhaftiges zeigt.",
        "Was also ist denn real auf dem physischen Plan?",
        "Real auf dem physischen Plan, so daß wir dabei stehenbleiben können und sagen: Hier haben wir etwas Wahres! - ist der Tod in der Menschenwelt, nicht in den anderen Reichen der Natur.",
        "Und bei den geschichtlichen Ereignissen, die im Laufe der Erden-entwickelung geschehen, müssen wir, wenn wir diese geschichtlichen Ereignisse kennenlernen wollen, von jedem solchen geschichtlichen Ereignis zu einem geistigen Urbild gehen - nur nicht bei dem Myste­rium von Golgatha!",
        "In diesem haben wir etwas, was so, wie es ist, unmittelbar in die Welt des Wahrhaftigen hineingehört."
      ],
      [
        "Nun ist es außerordentlich interessant, daß sich gewissermaßen auch die andere Seite des eben Auseinandergesetzten zeigt.",
        "Es ist wirklich außerordentlich bedeutsam, zu sehen, wie dieses Ereignis von Golgatha heute als ein reales Ereignis abgeleugnet wird, wie die Leute, wenn wir von äußerer Historie reden, sagen, es läßt sich im Zusammenhange der historischen Tatsachen nicht beweisen.",
        "Es gibt nun unter den histo­rischen Tatsachen, die wesentlich sind, auch kaum eine, die sich so schlecht durch äußere realistische Gründe beweisen läßt wie das My­sterium von Golgatha.",
        "Denken Sie, wie leicht es im Verhältnis dazu ist, in bezug auf die Existenz eines Sokrates oder Plato oder irgend­eines griechischen Helden, insofern sie bedeutend sind für den Fort­schritt der Menschheit in der äußeren Welt, mit historischen Gründen zu arbeiten; und wie die Menschen bis zu einem gewissen Grade mit vollem Recht kommen und sagen: Keine Historie darf behaupten, daß ein Jesus von Nazareth gelebt habe! - Äußere historische Widergründe"
      ],
      [
        "gibt es da nicht.",
        "Wie man andere historische Tatsachen behandelt, so läßt sich diese nicht behandeln."
      ],
      [
        "Es ist höchst merkwürdig: diese auf dem äußeren physischen Plan ge­scheheneTatsache hat dies eine gemeinschaftlich mit allen übersinnlichen Tatsachen, die lassen sich auch nicht beweisen.",
        "Und es sind so ziemlich dieselben Leute, welche die übersinnliche Welt leugnen und denen die Möglichkeit fehlt, dieses Ereignis, das gar kein übersinnliches ist, zu erfassen."
      ],
      [
        "Man kann es in bezug auf seine Wirkungen darstellen.",
        "Aber da machen sich die Leute den Gedanken, daß solche Wirkungen auch eintreten könnten, ohne daß das reale Ereignis in der Geschichte auf­getreten wäre, und erklären sie dann als Folge soziologischer Verhält­nisse."
      ],
      [
        "Für den jedoch, der den inneren Gang des Weltenwerdens kennt, ist die Idee, daß Wirkungen wie die des Christentums ohne eine da­hinterstehende Macht geschehen könnten, ebenso gescheit, wie wenn man sagte, daß auf einem Felde Kohlköpfe wachsen können, ohne daß vorher Samen ausgestreut wird.",
        "Ja, wir können noch weitergehen und sagen, daß für die, welche an der letzten Ausgestaltung der Evan­gelien beteiligt waren, keine Möglichkeit vorhanden war, das histo­rische Ereignis des Mysteriums von Golgatha als historisches Ereignis mit historischen Gründen nachzuweisen, denn es ging wirklich ziem­lich spurlos für alle äußere Beobachtung vorüber!"
      ],
      [
        "Wissen Sie, wie die, welche an der späteren Ausgestaltung der Evangelien beteiligt waren, sich selber von diesen Ereignissen überzeugt haben - mit Ausnahme des Schreibers des Johannes-Evangeliums, der ja der unmittelbare Zeit­genosse dieser Ereignisse war?",
        "Sie haben sich überzeugt zunächst nicht aus historischen Urkunden, denn sie haben ja auch nichts anderes ge­habt als mündliche Mitteilungen und die Mysterienbücher - wie diese Verhältnisse dargestellt sind in dem «Christentum als mystische Tat­sache» -, aber von dem wirklichen Dasein des Christus Jesus haben sie sich überzeugt aus der Sternkonstellation, indem sie noch große Ken­ner waren des Zusammenhanges des Makrokosmos mit dem Mikrokos­mos."
      ],
      [
        "Sie haben eine Kenntnis davon gehabt, die man sich heute auch schon beschaffen kann, indem man die Sternkonstellation für den be­treffenden Punkt der Weltgeschichte berechnet und sagt: Wenn die Sternkonstellation so und so ist, so muß Der auf der Erde gelebt haben,"
      ],
      [
        "welcher als der Christus bezeichnet wird. - So haben sich die Schreiber des Matthäus-, Markus- und Lukas-Evangeliums von dem ge­schichtlichen Geschehen überzeugt.",
        "Denn den Inhalt haben sie auf hellseherischem Wege gewonnen, aber die Überzeugung haben sie sich verschafft auf eine Weise, wie man sich durch die Konstellationen des Makrokosmos eine Überzeugung davon verschafft, daß auf der Erde dieses oder jenes vor sich gehen kann.",
        "Daher kann ihnen auch nur Glauben beibringen der, welcher so etwas weiß.",
        "Beweisen die Unrich­tigkeit dessen, was da vorgebracht wird gegen die Historizität der Evangelien, ist eine vergebliche Aufgabe.",
        "Wir müssen uns vielmehr als Anthroposophen klar sein, daß wir uns auf einen ganz anderen Boden stellen müssen: auf den Boden desjenigen, was wir uns nur durch eine Einsicht in die okkulte Wissenschaft verschaffen können."
      ],
      [
        "Ich möchte gerade auch hier dieser Erscheinung gegenüber auf etwas hinweisen, wodurch ich schon an einem anderen Orte zu begründen versuchte, wie man mit richtigen Einwänden, das heißt mit Einwän-den, die an sich richtig sind, die Wirklichkeiten nicht treffen kann, von denen die Geisteswissenschaft redet, so daß die Menschen noch so viel Richtiges sagen können, was nach ihrem Wissen richtig ist, es widerlegt die Geisteswissenschaft nicht.",
        "Ich habe in dem Vortrag:"
      ],
      [
        "«Wie begründet man Theosophie?», ein Gleichnis gebraucht und habe gesagt: Ein kleiner Junge mußte in einem Dorfe immer die Semmeln holen zum Frühstück seiner Familie.",
        "Man bekam nun in jenem Orte für zwei Kreuzer eine Semmel, und er bekam immer zehn Kreuzer mit.",
        "Nun brachte er - und es sei hierbei bemerkt, daß er kein großer Arithmetikus war - die Anzahl der Semmeln vom Greisler nach Hause und kümmerte sich nicht weiter darum.",
        "Nun wurde aber in die Familie ein Pflegesohn aufgenommen, der jetzt anstelle des anderen zum Greisler nach Semmeln geschickt wurde.",
        "Da der nun ein guter Arithmetikus war, so sagte er sich: Du gehst Semmeln holen, zehn Kreuzer hast du mitbekommen, für zwei Kreuzer gibt es eine Semmel, zehn durch zwei geteilt gibt fünf: also wirst du fünf Semmeln nach Hause bringen.",
        "Er ging fort, aber er brachte sechs Semmeln nach Hause.",
        "Da sagte er sich: Das ist falsch, so viel kannst du nicht be­kommen, und da deine Rechnung richtig ist, so wirst du morgen schon"
      ],
      [
        "fünf Semmeln nach Hause bringen. - Am nächsten Tage bekam er wieder zehn Kreuzer mit und brachte wieder sechs Semmeln nach Hause.",
        "Die Rechnung war richtig, nur stimmte sie nicht mit der Wirk­lichkeit, denn in der Wirklichkeit war es anders.",
        "In der Wirklichkeit war es nämlich an jenem Orte üblich, daß jemand, der für zehn Kreu­zer Semmeln kaufte, auf fünf eine drauf bekam, also statt fünf sechs.",
        "Der Einwand des Knaben war also richtig - nur stimmte er nicht mit der Wirklichkeit."
      ],
      [
        "So können die scharfsinnigst ausgedachten Einwände gegen die Geisteswissenschaft alle stimmen, brauchen aber nichts zu tun zu haben mit der Realität, denn die Realität kann auf ganz anderen Untergründen fußen.",
        "Es ist dieses angeführte Beispiel ganz praktisch, um sich klarzumachen, auch erkenntnistheoretisch, was in der Berech­nung richtig ist, und was in dem Wahrhaftigen richtig ist."
      ],
      [
        "Damit haben wir in unseren Bemühungen, die Welt der Maja zu­rückzuführen auf das Wahrhaftige - wobei sich uns gezeigt hat, daß alles Feuer Opfer ist, alles Luftartige strömende, spendende oder schenkende Tugend, und alles Flüssige Verzichtleistung, Resignation -, heute zu diesen drei Wahrheiten diejenige hinzugefügt, daß das wahre Wesen der Erde oder des Festen der Tod ist, das Abgeschnürtsein von seinem Weltensinn bei irgendeiner Substantialität.",
        "Dadurch aber, daß diese Abgeschnürtheit eintritt, tritt der Tod selber als ein Wahrhaf­tiges herein in die Welt der Maja oder der Illusion.",
        "Die Götter selbst könnten den Tod nicht einmal kennenlernen, wenn sie nicht in irgend­einer Weise herunterstiegen in die physische Welt, um den Tod in der physischen Welt, in der Welt der Maja oder der Illusion, zu begreifen."
      ],
      [
        "Das ist es, was wir heute hinzufügen wollen zu den Begriffen, die wir schon aufgenommen haben.",
        "Noch einmal sei es bemerkt, daß wir zur Klarheit über diese Begriffe, die uns aber notwendig sein werden zu einem gründlichen Eingehen auf so mancherlei im Markus-Evan­gelium, nur kommen können durch sorgfältige Meditation, und indem wir es öfter und öfter vor die Seele ziehen lassen.",
        "Denn das Markus-Evangelium ist nur zu begreifen, wenn man die allerbedeutsamsten Weltbegriffe dem zugrunde legt."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Die in den Vorträgen genannten geschriebenen Werke von Rudolf Steiner sind alle innerhalb der Gesamtausgabe erschienen. Siehe die Ubersicht am Schluß des Bandes.",
      "9    Betrachtungen, welche wir im vorigen Jahre... gepflo gen haben: Bezieht",
      "sich hauptsächlich auf die zehn Vorträge in Berlin «Exkurse in das Gebiet",
      "des Markus-Evangeliums» vom 17. Oktober 1910 bis 10. Juni1911; Gesamt­",
      "ausgabe Dornach 1963, Bibl.-Nr. 124.",
      "11    ,Seelenlehre ohne Seele': Dieser Ausdruck wurde geprägt von Friedrich",
      "Albert Lange. Siehe «Geschichte des Materialismus» 2 Bde, Univ. Bibl. Leip­",
      "zig 0. J.; 3. Abschnitt des 2. Bandes, S.474.",
      "Wundtsche Schule: Wilhelm Wundt, 1832-1920, Arzt, Philosoph und Psy­chologe. Gründete das erste Institut für experimentelle Psychologie in Leipzig.",
      "12    Sie ist ihm durch den Hüter der Schwelle zugedeckt: Siehe dazu die Aus-",
      "führungen Rudolf Steiners in «Wie erlangt man Erkenntnisse der höheren",
      "Welten?», Gesamtausgabe 1961, Bibl.-Nr. 10.",
      "13          Karl Rosenkranz, 1805-1879, Philosoph. Siehe »Aus einem Tagebuch»,",
      "Leipzig 1854, S.24 f., wo es heißt: «Die zerschmetterndste Vorstellung, die",
      "ich kaum auszudenken wage und kaum auszudrücken vermag, ist die, daß",
      "überhaupt etwas ist. Es gähnt mich aus diesem Gedanken der absolute, der",
      "gestaltenleere Abgrund der Welt an. Es wispert mir zu, wie der Verrat des",
      "Gottes. Es ergreift mich ein Bangen, wie in meiner Kindheit, wenn ich die",
      "Offenbarung Johannis las und Himmel und Erde darin zusammenbrachen... »",
      "Georg Wilhelm Friedrich Hegel, 1770-1831.",
      "21    Albert Schwegler, 1819-1857, Philosoph und Altphilologe. «Geschichte der",
      "Philosophie im Umriß», Stuttgart 1848, neue Ausgabe, durchgesehen und",
      "ergänzt von J. Stern, Univ.-Bibl. Leipzig o. J.",
      "Jakob Böhme, 1575-1624.",
      "Paracelsus, Theophrastus von Hohenheim, 1493-1541.",
      "35          Dion ysius der Areopagite, gehörte zum Areopaggericht in Athen und wurde",
      "vom Apostel Paulus für das Christentum gewonnen (Apostelgesch. 17, 34.)",
      "37    «Abendmahl» des Lionardo da Vinci: In dem Refektorium von Santa Maria",
      "delle Grazie in Mailand.",
      "38    «Dies tut zu meinem Angedenken!»: Luk. 22, 19.",
      "53    auf das «Abendmahl»: siehe Hinweis zu Seite 37.",
      "jene Worte, die wir auch im Evangelium finden: Math. 26, 53.",
      "54    wenn wzr uns die Worte vorhalten: Joh. 13, 26; Math. 26, 23.",
      "59    im öffentlichen Vortrage: Am 23. November 1911 in Berlin »Die verborge­nen Tiefen des Seelenlebens», abgedruckt in «Menschengeschichte im Lichte der Geistesforschung», Gesamtausgabe Dornach 1962, Bibl.-Nr. 61.",
      "60    ,Nur wer die Sehnsucht kennt...': Mignon in Goethes «Wilhelm Meister».",
      "70 ff. Heinrich von Kleist, (1777-1811). Das Zitat ist aus einem Brief vom",
      "31. August 1806; Kleists sämtl. Werke, hg. von Erich Schmidt, Bd. V, Leipzig und Wien 1905, S.326 f. - «Penthesilea», ein Trauerspiel, Tübingen 1808; »Das Käthchen von Heilbronn oder die Feuerprobe», ein großes historisches Ritterschauspiel, Berlin 1810; «Prinz Friedrich von Homburg», ein Schau­spiel, hg. von Ludwig Tieck, Berlin 1821.",
      "85    Vortrag über das Wesen der Pflanzen: Am 8. Dezember 1910 in Berlin «Der Geist im Pflanzenreich», abgedruckt in »Antworten der Geisteswissenschaft auf die großen Fragen des Daseins», Gesamtausgabe 1959, Bibl.-Nr. 60.",
      "87    Ereignis von Damaskus: Apostelgesch. 9.",
      "91    in dem Vortrag «Wie begründet man Theosophie»: Gehalten am 29. Novem­ber 1911 in Stuttgart. Von diesem Vortrag ist nur eine ungenügende Nach-schrift vorhanden; er ist nicht gedruckt.",
      "92    zu einem gründlichen Eingehen auf so mancherlei im Markus-Evangelium:",
      "Diese Vorträge wurden nicht in Berlin, sondern in Basel vom 15. bis 24. Sep­tember 1912 gehalten. Siehe »Das Markus-Evangelium», Gesamtausgabe Dornach 1960, Bibl.-Nr. 139."
    ],
    "sentences": [
      [
        "Die in den Vorträgen genannten geschriebenen Werke von Rudolf Steiner sind alle innerhalb der Gesamtausgabe erschienen.",
        "Siehe die Ubersicht am Schluß des Bandes."
      ],
      [
        "9 Betrachtungen, welche wir im vorigen Jahre... gepflo gen haben: Bezieht"
      ],
      [
        "sich hauptsächlich auf die zehn Vorträge in Berlin «Exkurse in das Gebiet"
      ],
      [
        "des Markus-Evangeliums» vom 17.",
        "Oktober 1910 bis 10.",
        "Juni1911; Gesamt­"
      ],
      [
        "ausgabe Dornach 1963, Bibl.-Nr. 124."
      ],
      [
        "11 ,Seelenlehre ohne Seele': Dieser Ausdruck wurde geprägt von Friedrich"
      ],
      [
        "Albert Lange.",
        "Siehe «Geschichte des Materialismus» 2 Bde, Univ.",
        "Bibl.",
        "Leip­"
      ],
      [
        "zig 0.",
        "J.; 3.",
        "Abschnitt des 2.",
        "Bandes, S.474."
      ],
      [
        "Wundtsche Schule: Wilhelm Wundt, 1832-1920, Arzt, Philosoph und Psy­chologe.",
        "Gründete das erste Institut für experimentelle Psychologie in Leipzig."
      ],
      [
        "12 Sie ist ihm durch den Hüter der Schwelle zugedeckt: Siehe dazu die Aus-"
      ],
      [
        "führungen Rudolf Steiners in «Wie erlangt man Erkenntnisse der höheren"
      ],
      [
        "Welten?», Gesamtausgabe 1961, Bibl.-Nr. 10."
      ],
      [
        "13 Karl Rosenkranz, 1805-1879, Philosoph.",
        "Siehe »Aus einem Tagebuch»,"
      ],
      [
        "Leipzig 1854, S.24 f., wo es heißt: «Die zerschmetterndste Vorstellung, die"
      ],
      [
        "ich kaum auszudenken wage und kaum auszudrücken vermag, ist die, daß"
      ],
      [
        "überhaupt etwas ist.",
        "Es gähnt mich aus diesem Gedanken der absolute, der"
      ],
      [
        "gestaltenleere Abgrund der Welt an.",
        "Es wispert mir zu, wie der Verrat des"
      ],
      [
        "Gottes.",
        "Es ergreift mich ein Bangen, wie in meiner Kindheit, wenn ich die"
      ],
      [
        "Offenbarung Johannis las und Himmel und Erde darin zusammenbrachen... »"
      ],
      [
        "Georg Wilhelm Friedrich Hegel, 1770-1831."
      ],
      [
        "21 Albert Schwegler, 1819-1857, Philosoph und Altphilologe.",
        "«Geschichte der"
      ],
      [
        "Philosophie im Umriß», Stuttgart 1848, neue Ausgabe, durchgesehen und"
      ],
      [
        "ergänzt von J.",
        "Stern, Univ.-Bibl.",
        "Leipzig o."
      ],
      [
        "Jakob Böhme, 1575-1624."
      ],
      [
        "Paracelsus, Theophrastus von Hohenheim, 1493-1541."
      ],
      [
        "35 Dion ysius der Areopagite, gehörte zum Areopaggericht in Athen und wurde"
      ],
      [
        "vom Apostel Paulus für das Christentum gewonnen (Apostelgesch. 17, 34.)"
      ],
      [
        "37 «Abendmahl» des Lionardo da Vinci: In dem Refektorium von Santa Maria"
      ],
      [
        "delle Grazie in Mailand."
      ],
      [
        "38 «Dies tut zu meinem Angedenken!»: Luk. 22, 19."
      ],
      [
        "53 auf das «Abendmahl»: siehe Hinweis zu Seite 37."
      ],
      [
        "jene Worte, die wir auch im Evangelium finden: Math. 26, 53."
      ],
      [
        "54 wenn wzr uns die Worte vorhalten: Joh. 13, 26; Math. 26, 23."
      ],
      [
        "59 im öffentlichen Vortrage: Am 23.",
        "November 1911 in Berlin »Die verborge­nen Tiefen des Seelenlebens», abgedruckt in «Menschengeschichte im Lichte der Geistesforschung», Gesamtausgabe Dornach 1962, Bibl.-Nr. 61."
      ],
      [
        "60 ,Nur wer die Sehnsucht kennt...': Mignon in Goethes «Wilhelm Meister»."
      ],
      [
        "70 ff.",
        "Heinrich von Kleist, (1777-1811).",
        "Das Zitat ist aus einem Brief vom"
      ],
      [
        "August 1806; Kleists sämtl.",
        "Werke, hg. von Erich Schmidt, Bd.",
        "V, Leipzig und Wien 1905, S.326 f. - «Penthesilea», ein Trauerspiel, Tübingen 1808; »Das Käthchen von Heilbronn oder die Feuerprobe», ein großes historisches Ritterschauspiel, Berlin 1810; «Prinz Friedrich von Homburg», ein Schau­spiel, hg. von Ludwig Tieck, Berlin 1821."
      ],
      [
        "85 Vortrag über das Wesen der Pflanzen: Am 8.",
        "Dezember 1910 in Berlin «Der Geist im Pflanzenreich», abgedruckt in »Antworten der Geisteswissenschaft auf die großen Fragen des Daseins», Gesamtausgabe 1959, Bibl.-Nr. 60."
      ],
      [
        "87 Ereignis von Damaskus: Apostelgesch. 9."
      ],
      [
        "91 in dem Vortrag «Wie begründet man Theosophie»: Gehalten am 29.",
        "Novem­ber 1911 in Stuttgart.",
        "Von diesem Vortrag ist nur eine ungenügende Nach-schrift vorhanden; er ist nicht gedruckt."
      ],
      [
        "92 zu einem gründlichen Eingehen auf so mancherlei im Markus-Evangelium:"
      ],
      [
        "Diese Vorträge wurden nicht in Berlin, sondern in Basel vom 15. bis 24.",
        "Sep­tember 1912 gehalten.",
        "Siehe »Das Markus-Evangelium», Gesamtausgabe Dornach 1960, Bibl.-Nr. 139."
      ]
    ]
  }
]

# === SQL GENERATION ===
def generate_sql():
    """Generate SQL using PL/pgSQL DO block."""
    sql_lines = []
    sql_lines.append("-- Auto-generated import for " + GA_NUMBER)
    sql_lines.append("BEGIN;")
    sql_lines.append("")
    sql_lines.append("DO $$")
    sql_lines.append("DECLARE")
    sql_lines.append("    v_book_id INT;")
    sql_lines.append("    v_lecture_id INT;")
    sql_lines.append("    v_para_id INT;")
    sql_lines.append("BEGIN")
    sql_lines.append("    -- Create or get book")
    te = BOOK_TITLE.replace("'", "''")
    sql_lines.append("    v_book_id := (SELECT id FROM books WHERE ga_number = '%s');" % GA_NUMBER)
    sql_lines.append("    IF v_book_id IS NULL THEN")
    sql_lines.append("        INSERT INTO books (ga_number, title_de, pdf_filename)")
    sql_lines.append("        VALUES ('%s', '%s', '%s.epub')" % (GA_NUMBER, te, GA_NUMBER))
    sql_lines.append("        RETURNING id INTO v_book_id;")
    sql_lines.append("    ELSE")
    sql_lines.append("        UPDATE books SET title_de = '%s' WHERE id = v_book_id;" % te)
    sql_lines.append("    END IF;")
    sql_lines.append("")
    sql_lines.append("    -- Delete old data (cascades to paragraphs/sentences)")
    sql_lines.append("    DELETE FROM lectures WHERE book_id = v_book_id;")
    sql_lines.append("")

    for ch in CHAPTERS:
        te = ch["title_de"].replace("'", "''")
        sql_lines.append("    -- Chapter %d: %s" % (ch["order"], te))
        sql_lines.append("    INSERT INTO lectures (book_id, title_de, order_index, level)")
        sql_lines.append("    VALUES (v_book_id, '%s', %d, 'lecture')" % (te, ch["order"]))
        sql_lines.append("    RETURNING id INTO v_lecture_id;")
        sql_lines.append("")

        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else []
            if not sentences:
                continue

            sql_lines.append("    INSERT INTO paragraphs (lecture_id, order_index)")
            sql_lines.append("    VALUES (v_lecture_id, %d)" % pi)
            sql_lines.append("    RETURNING id INTO v_para_id;")
            sql_lines.append("")

            for si, sent in enumerate(sentences, 1):
                se = sent.replace("'", "''")
                sql_lines.append("    INSERT INTO sentences (paragraph_id, order_index, text_de)")
                sql_lines.append("    VALUES (v_para_id, %d, '%s');" % (si, se))
                sql_lines.append("")

    sql_lines.append("END $$;")
    sql_lines.append("COMMIT;")
    sql_lines.append("")

    return "\n".join(sql_lines)


def import_to_db():
    """Run the SQL import via docker exec psql."""
    print("Generating SQL for %s..." % GA_NUMBER)
    sql = generate_sql()
    sql_path = "/tmp/%s_import.sql" % GA_NUMBER
    Path(sql_path).write_text(sql, encoding='utf-8')
    ln = len(sql.split('\n'))
    sk = len(sql) / 1024
    print("  SQL written: %s (%d lines, %d KB)" % (sql_path, ln, sk))

    result = subprocess.run(
        ["docker", "cp", sql_path, "%s:/tmp/%s_import.sql" % (DOCKER_CONTAINER, GA_NUMBER)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  FAILED COPY: %s" % result.stderr)
        return False

    print("  Importing into Docker PostgreSQL...")
    with open(sql_path, 'r') as f:
        proc = subprocess.Popen(
            ["docker", "exec", "-i", DOCKER_CONTAINER, "psql", "-U", DB_USER, "-d", DB_NAME],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=sql)

    if proc.returncode != 0:
        sl = stderr.strip().split('\n')
        print("  psql error (exit=%d):" % proc.returncode)
        for line in sl[-5:]:
            print("     %s" % line)
        return False
    else:
        print("  IMPORTED %s successfully!" % GA_NUMBER)
        if stdout.strip():
            for line in stdout.strip().split('\n')[-3:]:
                print("     %s" % line)
        return True


if __name__ == "__main__":
    print()
    print("=" * 60)
    print("Importing %s: %s" % (GA_NUMBER, BOOK_TITLE))
    print("=" * 60)

    tp = sum(len(c["paragraphs"]) for c in CHAPTERS)
    ts = sum(sum(len(s) for s in c["sentences"]) for c in CHAPTERS)
    print("  %d chapters, %d paragraphs, %d sentences" % (len(CHAPTERS), tp, ts))

    success = import_to_db()
    sys.exit(0 if success else 1)
