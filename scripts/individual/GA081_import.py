#!/usr/bin/env python3
"""Standalone import script for GA081 — GA081 - Erneuerungs-Impulse für Kultur und Wissenschaft"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA081 - Erneuerungs-Impulse für Kultur und Wissenschaft"""
GA_NUMBER = "GA081"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG ANTHROPOSOPHIE UND NATURWISSENSCHAFT Berlin, 6. März 1922",
    "paragraphs": [
      "Sehr verehrte Anwesende! Es war der Wunsch des Ko- mitees für diese Hochschulwoche, daß ich an jedem Tage durch einige Ausführungen einleite, was im Laufe des Tages wissenschaftlich zur Verhandlung kommen soll.",
      "Es ist das ja wohl so eingerichtet worden aus der An- schauung heraus, daß durch Anthroposophie die ein- zelnen Wissenschafts- und Lebenszweige eine gewisse Befruchtung erfahren sollen; und nur in diesem Sinne, als einleitende Bemerkungen zu den Verhandlungen des Tages, bitte ich Sie diese ersten Vorträge aufzufassen. Was mich immer am meisten gewundert hat bei der Entgegennahme der anthroposophischen Forschungs- methode, das ist der Widerstand, der insbesondere von philosophisch-naturwissenschaftlicher Seite - ich sage nicht: rein von naturwissenschaftlicher Seite - der An- throposophie entgegengebracht wird, und zwar aus dem Grunde, weil man glaubt, daß Anthroposophie in einer unberechtigten oppositionellen Weise den Methoden der Naturwissenschaft gegenüberstehe, welche sich in so fruchtbarer Art im Laufe der letzten Jahrhunderte, ins- besondere des 19.",
      "Jahrhunderts herausgebildet haben. Und mir scheint, daß unter all den Dingen, die in bezug auf Anthroposophie von unserer Zeitgenossenschaft am allerschwersten eingesehen werden, das ist, daß An- 13 throposophie gerade gegenüber der Naturwissenschaft nichts anderes will, als die Methoden, die in der Natur- wissenschaft sich so fruchtbar erwiesen haben, in ent- sprechender Weise weiterzubilden.",
      "Allerdings muß man unter der Idee der Weiterbildung etwas anderes noch verstehen können, wenn man von dieser Seite her zum Begreifen des Anthroposophischen kommen will, als das, was man gewöhnlich heute eine Weiterbildung von theoretischen Anschauungen nennt. Eine Weiterbildung der theoretischen Anschauungen ist heute den meisten Menschen dieses: daß die besondere Art der Gedankenverknüpfung - insbesondere, wenn ich mich so ausdrücken darf, das Feld der Gedanken - dieselbe bleibt, auch wenn man die betreffenden Gedan- kensysteme auf andere Gebiete der Welterscheinungen ausdehnt.",
      "So zum Beispiel: Man kommt, wenn man sich naturwissenschaftlich betätigt, gegenüber der leblosen, der anorganischen Natur in die Notwendigkeit, gewisse Gedankenverknüpfungen, ein gewisses Feld von Gedan- ken, das heißt eine Summe von miteinander verbunde- nen Gedanken zugrundezulegen, um gewissermaßen eine Theorie der unorganischen, der leblosen Naturerschei- nungen zu bekommen. Dieses System von Gedanken will man dann so, wie es ist, weiter ausdehnen, wenn man ein anderes Gebiet der Welt, also zum Beispiel das Gebiet der organischen Naturerscheinungen, zu begrei- fen bestrebt ist.",
      "Man will also mit derjenigen kausalen Orientierung, die sich so fruchtbar erweist im unorga- nischen Gebiet, einfach hinübergehen in das Gebiet der Lebewesen und diese mit denselben Begriffen durch- tränken und erklären, also gewissermaßen begrifflich das Gebiet der Lebewesen ebenso zu einem Wirkungssystem von unorganischen Kausalitäten machen, wie man ja 14 genötigt ist, es gegenüber der leblosen, der unorganischen Natur zu tun. Also was man sich angeeignet hat als Gedankensystem aus der leblosen Natur, das trägt man einfach hinüber in die organische Natur.",
      "Und das ist das, was man heute gewöhnlich unter «Erweiterung» von Gedanken und Theorien versteht. Damit steht allerdings dann im vollen Gegensatz, was Anthroposophie unter einer solchen Erweiterung von Gedanken verstehen muß.",
      "Sie muß den Begriff eines gewissen selbständigen Wachsens, eines Sichmetamor- phosierens der Idee vollziehen, wenn von einem Gebiete der Welterscheinungen zu einem anderen übergegangen wird, so daß man nicht bloß das, was man an den leb- losen Naturerscheinungen gelernt hat, ich möchte sa- gen «logisch übertragen» kann auf die belebten Natur- erscheinungen. So wie vergleichsweise in der Lebewelt die Dinge selber sich sehr verändern, wenn sie wachsen, wenn sie Metamorphosen durchmachen, und wie sie dann oftmals in der Gestaltung, die sie angenommen haben, gar nicht wiederzuerkennen sind, so müssen auch die Gedanken andere Gestaltungen annehmen, wenn sie in ein anderes Gebiet kommen.",
      "Was aber über alle Ge- biete hin dasselbe bleibt und was dann der ganzen wis- senschaftlichen Weltauffassung methodisch einen moni- stischen Charakter gibt, das ist die Art und Weise, wie man sich innerlich stellt zu dem, was man «wissen- schaftliche Gewißheit» nennen kann, was die Grundlage gibt zur wissenschaftlichen Überzeugung. Wer zu prü- fen vermag, warum man nicht mit den Begriffen, die man in der leblosen Natur schon einmal gewohnt ist anzu- wenden, zu einer Befriedigung des menschlichen Kau- salitätsbedürfnisses kommt - wenn ich mich des Du Bois-Reymondschen Ausdruckes bedienen darf -, wer 15 das wirklich innerlich kennenlernt, der kann es dann hinüberführen in die Art und Weise, wie man durch ganz andere Begriffe, die aber doch nur Metamorphosen gegenüber den früheren Begriffen sind, überzeugt wird in der Welt des Lebendigen.",
      "Diese Art, wie sich der Mensch da innerhalb des Wissenschaftsgetriebes stellt, ist durchaus monistisch durch die ganze wissenschaft- liche Weltanschauung hindurch. Das ist etwas, was gewöhnlich mißverstanden wird und was dazu führt, daß man der anthroposophisch-wissenschaftlichen Welt- anschauung nicht einen monistischen, sondern einen dualistischen Charakter beilegen will.",
      "Das zweite, was sehr häufig zu Mißverständnissen führt, ist der Phänomenalismus, dem sich Anthroposo- phie gerade mit Bezug auf Naturwissenschaft hingeben muß. Wir haben ja gerade in dem für so vieles fruchtbar- sten Zeitalter naturwissenschaftlicher Entwicklung, etwa in der Zeit, in welcher der bedeutende Naturforscher Virchow seine Rede gehalten hat über die Ablösung der philosophischen Weltanschauung durch die naturwis- senschaftliche, erfahren, wie alles, was damals mit einer gewissen historischen Berechtigung an fruchtbaren Be- griffen über das Anorganische gewonnen worden ist, dazu geführt hat, einen gewissen Rationalismus in der Naturwissenschaft zu begründen.",
      "Und das Zeitalter, das auf der einen Seite streng auf Empirismus gegenüber der äußeren Tatsachenwelt hinarbeitete, das erging sich doch in einem sehr weittragenden Rationalismus, wenn es dazu kam, die empirisch erkundeten Naturtatsachen zu erklären. Demgegenüber steht nun die Anthroposophie auf dem Standpunkte, der sich ergibt - wenigstens für mich sich ergeben hat, wenn ich diese persönliche Bemerkung 16 machen darf - aus der Goetheschen Naturauffassung heraus.",
      "Anthroposophie steht auf dem Boden einer phä- nomenologischen Naturauffassung. In einer gewissen Weise hat diese Phänomenologie in der neueren Zeit wieder Ernst Mach begründet, und so wie er sie begrün- det, scheint sie durchaus wiederum fruchtbare Ge- sichtspunkte zu enthalten, wenn man ihre Grenzen ein- hält.",
      "Es handelt sich bei Goethe einfach um das, was in seinen Worten liegt: Die Erscheinungswelt selbst ist schon genügend Theorie, man braucht nicht erst zu künst- lichen Theorien fortzuschreiten. Die Bläue des Himmels ist ein Phänomen, innerhalb dessen man stehenbleiben und sich nicht herbeilassen soll, nun in rationalistischer Weise durch bloße Gedanken hinter den Erscheinungen zunächst hypothetische, angenommene Erklärungsgründe zu suchen.",
      "Goethe kam ja auf diesem Wege zur Statu- ierung dessen, was er «Urphänomen» nannte. Wenn auch, wie es ja selbstverständlich ist, im Laufe des für die Naturwissenschaft so fruchtbaren 19. Jahrhunderts vieles von dem überholt worden ist, was Goethe in der Naturwissenschaft wollte, so kann man doch sagen: Das Methodische, die Denkweise selbst, die Goethe in die Naturwissenschaft hineingetragen hat, ist heute nicht nur noch nicht überholt, sondern sie scheint mir überhaupt noch nicht gründlich genug verstanden zu sein.",
      "Ich weiß sehr gut, wie im 19. Jahrhundert manches - man möchte sagen fast alles - von den Einzelheiten Goethescher Darstellungen über naturwissenschaftliche Dinge überholt worden ist. Dennoch möchte ich auch heute noch den Satz aufrecht erhalten, den ich in den 80er Jahren des vorigen Jahrhunderts in bezug auf die Goethesche Naturanschauung ausgesprochen habe: daß 17 Goethe der Kopernikus und Kepler ist für die organi- sche Naturwissenschaft.",
      "Ich will diesen Satz aus dem Grunde auch heute noch aufrecht erhalten, weil ich glaube, daß folgendes durchaus gerechtfertigt ist. Wodurch kommen wir denn schließlich zu einer wirklichen Naturanschauung auf dem Gebiete, auf dem gerade das 19.",
      "Jahrhundert so viel geleistet hat? Ich kann das, was ich meine, nicht anders begrenzen als durch diese historische Kategorie. Das, worin das 19. Jahr- hundert in der Naturwissenschaft so viel geleistet hat, führt zuletzt fast überall zurück auf die Anwendung der mathematischen Methoden; denn auch da, wo man nicht rein mathematisch vorgeht, sondern nach anderen Kau- salitätsprinzipien denkt, wo man Theorien ausgebildet hat, lag ja durchaus auch die mathematische Denkweise zugrunde.",
      "Bezeichnend dafür ist etwa das Folgende: Wir haben gesehen, wie im Laufe des 19. Jahrhunderts gewisse Partien der Naturwissenschaft durchaus in einer gewis- sen rationalistischen Weise dadurch begründet werden sollten, daß man Mathematik in sie einführte.",
      "Bekannt ist der Kantsche Satz, daß eigentlich in jeder Wissenschaft nur so viel wirkliche Gewißheit sei, wie Mathematik in ihr zu finden sei. - Nun kann man selbstverständlich Mathematik nicht überall hintragen. Die Kausalitätser- klärungen gehen weiter als die Möglichkeit mathemati- scher Begriffsbildungen.",
      "Aber das, was man so unter- nommen hat an Kausalitätserklärungen, das wurde doch weitgehend nach dem Muster mathematischer Begriffs- bildungen unternommen. Und als sich dann Ernst Mach daranmachte, von seinem mehr phänomenologischen Standpunkte aus dieses Begriffssystem zu überschauen, mußte er auch auf den Begriff der Kausalität zurück- 18 blicken, wie er sich in der Naturwissenschaft im Laufe des 19.",
      "Jahrhunderts ausgebildet hat, und er wollte zu einem gewissen Inhalt für diesen Kausalitätsbegriff kom- men. Zuletzt sagte er sich: Wenn ich eine Wirkung mit einer Ursache zusammendenke, so ist doch eigentlich nichts anderes darin enthalten als ein mathematischer Funktionsbegriff; zum Beispiel wenn ich sage: x ist gleich y, wobei ich unter x die Ursachen zusammenfasse und unter y die Wirkung, habe ich das Ganze auf diejenigen Begriffe zurückgeführt, die ich in der Mathematik habe, wenn ich den Funktionsbegriff bilde.",
      "Also man kann auch aus der Geschichte der Wissenschaften sehen, wie man den Mathematikbegriff in das ganze Gebiet der Naturwissenschaft hineingetragen hat. Nun wird Goethe - und zwar mit einem gewissen Recht gewöhnlich als ein Nicht-Mathematiker angese- hen; er hat sich ja selbst als einen solchen bezeichnet.",
      "Aber wenn man so einfach Goethe als einen Nicht- Mathematiker hinstellt, so führt das auch wieder zu Mißverständnissen - in dem Sinne etwa, daß Goethe nicht viel im einzelnen mathematisch habe leisten kön- nen, daß er nicht besonders geschickt gewesen sei, auch schon zu seiner Zeit durchaus bestehende mathemati- sche Exempel zu lösen. Das muß natürlich durchaus zugegeben werden.",
      "Ich glaube auch nicht, daß Goethe bei seinem ganzen Wesen sonderlich viel Geduld gehabt hätte, sich auf die Lösung einzelner mathematischer Exempel einzulassen, wenn es mehr ins Algebraische hineingegangen wäre. Das muß schon zugegeben wer- den.",
      "Aber Goethe war in gewissem Sinne, so paradox es klingt, mehr ein mathematischer Kopf als mancher Ma- thematiker; denn er hatte eine feine Einsicht in die Natur des Mathematisierens, in die Natur des Bildens von 19 mathematischen Begriffen, und er schätzte diese Art und Weise zu denken, die ganz in dem inneren Seelenprozeß auch mit dem Inhalt der Vorstellung bleibt, wenn sie Begriffe bildet. Man überschaut im Mathematischen, wenn man Be- griffe bildet, innerlich vollständig alles.",
      "Nehmen Sie als ein einfaches Beispiel in der euklidischen Geometrie den gewöhnlichen Beweis dafür, daß die drei Winkel eines Dreiecks zusammen 180 Grad betragen, wo man oben durch die Spitze des Dreiecks eine Parallele zur Grund- linie zieht, die dort auf diese Weise entstandenen Winkel betrachtet, die als Wechselwinkel gleich sind den beiden anderen Winkeln des Dreiecks - der dazwischen liegende bleibt sich ja gleich -, und wo man dann sehen kann, wie diese drei Winkel dort an der Spitze zusammen 180 Grad betragen, also in ihrer Summe den drei Winkeln des Dreiecks gleich sind. - Wenn man das überschaut, hat man einen mathematischen Beweis, aber man hat zu gleicher Zeit etwas, wobei man gar nicht abhängig ist von einer äußeren Anschauung, sondern durchaus die Dinge in innerlichem Konstruieren überschauen kann. Hat man dann ein äußeres Dreieck, so findet man, daß durch die äußeren Tatsachen verifiziert wird, was man vorher innerlich überschaut hat.",
      "Das ist in der ganzen Mathematik so. Es bleibt alles so, daß man nicht an die Sinnesanschauung heranzugehen braucht, um zu dem zu kommen, was man «Beweis» nennt, daß aber alles, was man innerlich gefunden hat, auch äußerlich Stück für Stück verifiziert werden kann.",
      "Diese besondere Art des Mathematischen ist es ja, welche Goethe gerade als die eminent wissenschaftliche ansah, und insofern war er wirklich ein guter mathema- tischer Kopf. Das liegt zum Beispiel auch der Führung 20 jenes berühmten Gespräches zugrunde, das Goethe und Schiller einmal in der Blütezeit ihrer Freundschaft ge- führt haben über die Methode der naturwissenschaft- lichen Betrachtung.",
      "Sie waren beide bei einem Vortrage, den der Naturforscher Batsch in der Naturforschenden Gesellschaft in Jena gehalten hatte, und als sie fortgin- gen, sagte ja Schiller zu Goethe über das, was sie dort gehört hatten, das sei eine zerstückelte Art, die Naturer- scheinungen zu betrachten, damit komme man zu nichts Ganzem. - Man kann sich denken, daß Batsch einfach die einzelnen Naturobjekte nebeneinander hingeordnet und es unterlassen hatte, wie es ja auch durchaus einem Naturforscher der damaligen Zeit geziemte, irgendetwas vorzuführen, was zu einer Gesamtanschauung in der Natur führen konnte. Schiller empfand dies unbefrie- digend und sprach sich darüber bei Goethe aus.",
      "Und Goethe sagte, er verstehe es, eine gewisse Einheit, eine gewisse Ganzheit in eine solche Naturbetrachtung hin- einzubringen. Und er fing an, mit wenigen Strichen - er erzählt es ja selbst - die «Urpflanze» aufzuzeichnen, wie sie zu denken ist, wie sie innerlich angeschaut werden kann, nicht, wie sie in dieser oder jener Pflanze zu Tage tritt, sondern wie sie innerlich angeschaut werden kann mit Wurzel, Stengel, Blättern, Blüte, Frucht.",
      "Ich habe in meinen Einleitungen zu den «Naturwis- senschaftlichen Schriften» Goethes in den 80er Jahren des vorigen Jahrhunderts versucht, das Bild, das damals Goethe auf das Papier vor Schiller hingeworfen hat, nachzuzeichnen. - Schiller sah sich das an und sagte dann aus seiner Denkweise heraus: Das ist keine Erfah- rung, das ist eine Idee. - Schiller hatte eben gemeint: wenn man so etwas aufzeichnet, so hat man das aus sich heraus gesponnen; das ist als Idee, als Gedanke ganz gut, 21 hat aber in der Wirklichkeit im Grunde genommen keine Quelle. Goethe verstand diese Denkweise eigentlich gar nicht, und zuletzt endete das Gespräch damit, daß Goethe erwiderte, gewissermaßen das Gespräch zusammenfas- send: Wenn das so ist, dann sehe ich meine Ideen mit Augen.",
      "Was meinte denn Goethe damit? Er meinte - er hat es nicht so ausgesprochen, aber er meinte es: Wenn ich ein Dreieck hinzeichne, so hat es von selbst eine Winkel- summe von 180 Grad; und wenn ich noch so viele Dreiecke anschaue, das, was ich an diesem einen Dreieck innerlich konstruiert habe, das paßt auf alle Dreiecke; ich habe also etwas aus dem Innern heraus gewonnen, das nun in vollem Umfang auf das Erfahrene paßt.",
      "So wollte Goethe auch eine «Urpflanze» - gewissermaßen gemäß dem «Urdreieck» - zeichnen, und einen solchen Cha- rakter sollte diese Urpflanze haben, daß man diesen bei jeder einzelnen Pflanze finden könne. Und so, wie die Winkelsumme jedes Dreiecks, wenn man das Urdreieck hat, 180 Grad beträgt, so sollte auch dieses ideelle Gebilde, die Urpflanze, in jeder einzelnen Pflanze wiedergefunden werden, wenn man die ganze Pflanzenreihe durchgeht.",
      "In diesem Sinne wollte Goethe die ganze Wissen- schaft gestalten. Im wesentlichen wollte er - er kam ja damit nicht weiter - die Wissenschaft des Organischen so gestalten und eine solche Denkweise einführen, wie sie sich für die Wissenschaft des Unorganischen als fruchtbar erwiesen hat.",
      "Man sieht das ganz besonders klar, wenn Goethe von Italien aus schreibt, wie er die Idee der Urpflanze immer weiter ausgebildet hat. Da sagt er ungefähr: Da, unter den Pflanzen in Süditalien und Sizilien in der Mannigfaltigkeit der Pflanzenwelt ist mir die Urpflanze ganz besonders aufgegangen, und es 22 muß sich doch ein Gebilde finden lassen, das die Mög- lichkeit aller wirklichen Pflanzen in sich hat, ein Gebil- de, das sich nach verschiedenen Seiten hin variieren kann; es nimmt dann diese oder jene, langgestreckte oder andere Blattform an, bildet bald die Blüte, bald die Frucht mehr aus und so weiter so wie ein Dreieck stumpfwinklig oder spitzwinklig sein kann.",
      "Ein Gebilde wollte Goethe finden, nach dessen Muster alle Pflanzen gebildet sind. Es ist ganz falsch, wenn dann später Schieiden meinte, Goethe habe mit der Urpflanze eine tatsächliche Pflanze gemeint. Das ist nicht so so wie auch der Mathemati- ker, der vom Dreieck spricht, nicht irgendein bestimm- tes Dreieck im Auge hat -, sondern Goethe meinte ein Gebilde, das innerlich erzeugt wird, das sich aber in der Außenwelt überall verifiziert findet.",
      "So war Goethe im Grunde genommen ein durchaus mathematischer Kopf, viel mathematischer als etwa die, die die Astronomie ausbilden. Und das ist das Wesent- liche. Das veranlaßte Goethe auch, in diesem Gespräch mit Schiller zu sagen: Dann sehe ich meine Ideen mit Augen. - Er sah sie mit Augen, weil er sie überall in den Phänomenen verfolgen konnte.",
      "Er begriff gar nicht, daß etwas nur eine «Idee» sein sollte, weil er sich im vollen Einklang fand mit der Erfahrung, wenn er Ideen bildete; geradeso, wie der Mathematiker sich im Einklang fühlt mit der Erfahrung, wenn er mathematische Ideen bildet. Das aber führte Goethe, ich möchte sagen, durch eine innere Konsequenz dazu, zur bloßen Phänomenologie zu kommen, das heißt, nichts hinter den Erscheinun- gen als solchen zu suchen, vor allen Dingen nicht eine rationalistische Atomwelt zu konstruieren.",
      "Nun, damit betritt man ein Gebiet, auf dem sich viele ich kann aber doch nur sagen - auf Mißverständnissen 23 beruhende Kämpfe gegenüber mancher naturwissen- schaftlich-philosophischen Anschauung entwickelten. Es handelt sich zunächst einfach darum, das, was sich den Sinnen in der äußeren Welt darbietet, was also in der Beobachtung und im Experiment gegeben ist, rein als Phänomen zu betrachten.",
      "Goethe und mit ihm die ganze naturwissenschaftliche Phänomenologie beschränkt sich darauf, nicht gleich von irgendeinem sinnlichen Phäno- men zu einem dahinterstehenden Atomgeschehen zu gehen, sondern zunächst das sinnliche Phänomen und das einzelne Element der sinnlichen Tatsachen rein ins Auge zu fassen, sie also nicht auf ein Dahinterliegendes zu beziehen, sondern auf andere Elemente in der sinn- lichen Erscheinungswelt, und den Zusammenhang in der sinnlichen Erscheinungswelt aufzusuchen. Man kann sehr leicht - ich verstehe vollständig, wo- her die entsprechenden Mißverständnisse kommen - eine solche Phänomenologie sogar trostlos finden.",
      "Man könnte zum Beispiel sagen: Wenn man sich nun bloß beschränken will auf das Beschreiben der gegenseitigen Beziehungen der sinnlichen Phänomene und dann diejenigen Phäno- mene aufsucht, die am einfachsten sind, in denen sich möglichst überschaubares Geschehen abspielt - und die Goethe «Urphänomene» nennt -, so kommt man bei einem solchen Vorgehen nicht zu einer Anschauung über jene unendlich fruchtbaren Dinge, die zum Beispiel die moderne Chemie geliefert hat. Wie, so könnte man fragen, kann man denn eigentlich gegenüber den Atom- gewichtsverhältnissen auskommen, ohne eine Anschau- ung über eine atomistische Welt?",
      "Nun, in einem solchen Falle möchte man aber doch die Gegenfrage stellen: Wenn man sich nun wirklich besinnt auf das, was da vorliegt, hat man es denn da zu tun mit einer Notwen- 24 digkeit, vom Phänomen abzugehen? Man hat es gar nicht damit zu tun.",
      "Man hat es auch bei den Atomgewichts- verhältnissen mit Phänomenen zu tun, nämlich mit Ge- wichtsverhältnissen. Aber man könnte auch fragen: Führt es denn weiter, wenn man nun diese durch Zahlen aus- drückbaren Atomgewichtsverhältnisse dadurch zu er- klären versucht, daß man gewisse Molekularstrukturen aus den Atomgewichten auf rein denkerische, rationa- listische Weise bildet?",
      "Man kann eben auch diese Fra- ge aufwerfen. Kurz, worum es sich handelt, wenn die Goethesche Denkweise ausgebildet wird, das ist: ste- henzubleiben innerhalb der Phänomene selbst. Ich möchte dafür einen trivialen Vergleich gebrauchen.",
      "Nehmen wir an, jemand bekommt ein aufgeschriebe- nes Wort vor sein Auge. Was wird er tun? Nun, wenn er nie lesen gelernt hat, wird er davor stehen wie vor etwas Unerklärbarem. Hat er aber lesen gelernt, so wird er unbewußt die einzelnen Formen zusammenfügen; er wird den Wortsinn in der Seele erleben.",
      "Aber er wird ganz gewiß nicht von den Formen aus, zum Beispiel beim W, etwas zu erklären versuchen, indem er den Ausgang nähme von dem nach aufwärts gehenden Strich, dann überginge zu dem nach abwärts gehenden, um dadurch auf etwas diesem Buchstaben Zugrundeliegendes zu kommen. Nein, er wird lesen und nicht durch Unter- legungen erklären wollen.",
      "So möchte auch die Phäno- menologie «lesen». Sie möchte innerhalb des Zusammen- hanges der Phänomene stehenbleiben und lesen lernen, und nicht, wenn ich einen Komplex von Phänomenen habe, von ihm aus zurückgehen auf Atomstrukturen.",
      "Es handelt sich also darum, das Feld des Phänomena- len hinzunehmen und in seiner eigenen inneren Bedeu- tung lesen zu lernen. Dadurch wird man dann zu einer 25 Naturwissenschaft kommen, welche in ihren Inhalten nichts Rationalistisches, hinter den Phänomenen Kon- struiertes hat, sondern welche einfach in der Art und Weise, wie sie die Phänomene überschaut, gewisse ge- setzmäßige Strukturen findet.",
      "Überall wird dieser Na- turwissenschaft eingegliedert sein die Summe der Phä- nomene selbst. Man wird auf eine bestimmte Art über die Natur reden. In dieser Art zu reden werden die Natur- gesetze enthalten sein, aber überall werden m den Aus- drucksformen schon die Phänomene selber liegen.",
      "Man wird also das bekommen, was ich nennen möchte: eine den Erscheinungen immanente Naturwissenschaft. Nach einer solchen strebte Goethe. Die Art und Weise, wie er das betrieb, muß unter den Fortschritten der neueren Zeit verändert werden, aber es ist doch so, daß das Grundprinzip festgehalten werden kann.",
      "Und wenn dieses Grundprinzip festgehalten wird, stellt sich für die menschliche Auffassungsweise der Natur ganz von selbst etwas heraus, das ich in der folgenden Weise charakte- risieren möchte. Es ist ja ganz selbstverständlich, daß wir als gegen- wärtige Menschheit unsere naturwissenschaftlichen Be- griffe zunächst an der unorganischen Natur gebildet haben.",
      "Das ist dadurch veranlaßt gewesen, daß die un- organischen Naturerscheinungen verhältnismäßig ein- fach sind; das war aber auch veranlaßt dadurch, daß ja, wenn man ins organische Reich hinaufsteigt, durchaus auch die im Leblosen wirkenden Agenzien fortdauern. Wenn man vom Mineralreich zum Pflanzenreich her- aufsteigt, dann ist es ja nicht so, daß etwa die leblose Wirkungsweise bei der Pflanze aufhörte; sie wird nur eingefaßt in ein höheres Prinzip, aber sie dauert in der Pflanze fort.",
      "Wir tun recht, wenn wir die physischen und 26 chemischen Prozesse in den Pflanzenorganismus hinein weiterverfolgen, und zwar nach denselben Gesichts- punkten, nach denen wir gewohnt sind, sie in der un- organischen Natur zu verfolgen. Wir müssen dann nur auch die Fähigkeit haben, in unseren Begriffssystemen überzugehen zu veränderten, zu metamorphosierten Be- griffen.",
      "Wir müssen schon verfolgen, wie das Unorgani- sche auch verwendet wird in der Pflanze und wie die- selben Prozesse, die sich in der leblosen Natur finden, auch in die Pflanze hineingehen. Aber dadurch wird die Versuchung hervorgerufen, daß man wissenschaftlich nur das verfolgt, was sich aus der mineralischen Welt hereinerstreckt in Pflanze und Tier und dabei einfach unberücksichtigt läßt, was dann in den höheren Reichen dazu auftritt.",
      "Diese Versuchung wurde durch einen be- sonderen Umstand gerade im Laufe des 19. Jahrhunderts noch außerordentlich größer. Das ist in folgender Weise geschehen. Wenn man die leblose Natur betrachtet, fühlt man sich gewissermaßen innerlich tief befriedigt, weil man die Erscheinungen mit mathematischen Gedanken ver- folgen kann.",
      "Und es ist sehr begreiflich, daß Du Bois- Reymond in einer so wortreichen und glänzenden Weise m seiner Rede «Über die Grenzen des Naturerkennens» die Laplacesche Weltanschauung, die er die «astronomi- sche Auffassung» des ganzen natürlichen Weltendaseins nennt, gefeiert hat, möchte ich sagen. Nach dieser astro- nomischen Auffassung wird ja nicht nur der Sternen- himmel so angesehen, daß man seine einzelnen Phäno- mene mit mathematischen Gedanken zusammenfaßt und sie dann als ein Ganzes, soweit es geht, konstruiert, sondern man versucht, auch damit unterzutauchen in die Konstitution der Materie.",
      "Man versucht im Molekül ein 27 kleines Weltsystem zu konstruieren, wo sich die Atome so bewegen und zueinander stehen wie die Sterne im Weltgebäude. Man konstruiert sich so im Kleinen kleinste Weltsysteme und hat die Befriedigung, daß man so im Kleinen dieselben Gesetzmäßigkeiten findet wie im Großen.",
      "So hat man in den einzelnen Atomen und Mo- lekülen ein System sich bewegender Körper, wie man draußen im Weltgebäude das System der Fixsterne und Planeten hat. Das ist charakteristisch für die Art, wie man vor allem im 19.",
      "Jahrhundert gestrebt hat und wo- durch, wie Du Bois-Reymond sagte, das Kausalitäts- bedürfnis des Menschen sich befriedigt fühlt. Es ist das einfach entstanden aus dem Drang heraus, das mathe- matisch Fruchtbare in alle Naturerscheinungen hinein- zutragen.",
      "Daraus entstand nun eben die Versuchung, bei diesem Mathematischen in der Betrachtung der Natur- erscheinungen stehenzubleiben. Es wird keinem einfallen, auch einem Anthroposo- phen nicht, wenn er nicht laienhaft über diese Dinge spricht, bestreiten zu wollen, daß dies alles seine Berech- tigung hat, namentlich dann, wenn man innerhalb der Phänomene stehen bleibt und sich bemüht, die Einzel- heiten, zum Beispiel der Astronomie, in diesem Sinne aufzufassen.",
      "Keinem wird es einfallen, dagegen einen Kampf zu führen. Aber im Laufe des 19. Jahrhunderts trat das ein, daß man bei dem, was die Welt darbietet, alles das übersah, was qualitativ ist, und nur das sah, was ja da ist und in allem Qualitativen drinnen ist: das, was durch die Mathematik zu erfassen ist.",
      "Da muß man unterscheiden: Man kann durchaus zugeben, daß diese mechanistische Welterklärung voll berechtigt ist; es ist gar nichts dagegen einzuwenden. Aber etwas anderes ist es, ob man sie auf bestimmten Gebieten als vollberech- 28 tigt erklärt oder ob man sie nun als das einzige mögliche Begriffssystem hingestellt will und mit diesem Begriffs- system schon alles in der Welt für erklärt halten will.",
      "Hier liegt der Differenzpunkt. Es wird durch den Anthroposophen nicht im geringsten das bestritten, was seine Berechtigung hat. Die Anthroposophie kämpft nämlich gar nicht gegen die anderen, und es ist interes- sant, bei Diskussionen zu verfolgen, wie Anthroposophie eigentlich alles innerhalb der berechtigten Grenzen zu- gibt.",
      "Es fällt den Anthroposophen gar nicht ein, das, was durch die Naturwissenschaft geltend gemacht wird, ir- gendwie zu bestreiten. Sondern es handelt sich darum, ob es berechtigt ist, das ganze Gebiet der Phänomene mit der mathematisch-kausalen Denkweise zu umfassen, oder ob es berechtigt ist, aus der Summe der Erscheinungen dasjenige herauszunehmen, was mathematisch-kausal eine reine Abstraktion ist, und es hinzustellen als einen «er- dachten» Welteninhalt, wie es zum Beispiel der frühere Atomismus getan hat.",
      "Heute ist der Atomismus bis zu einem gewissen Grade schon phänomenologisch ge- worden, und bis zu diesem Grade geht Anthroposophie ganz gewiß mit. Aber es handelt sich darum, daß heute eben noch etwas hereinspukt von dem im 19.",
      "Jahrhundert so ungoetheschen Atomismus, der sich nicht beschränkte auf die Phänomene, sondern der ein reines Begriffssystem hinter den Phänomenen konstruierte. Und wenn man sich nicht klar darüber ist, daß man es doch nur mit einem Begriffssystem zu tun hat, das die Welt hinter den Erscheinungen sucht, sondern sich der Anschauung hin- gibt, man habe mit diesem Begriffssystem ein Reales ergriffen, so wird man durch dieses Begriffssystem ge- wissermaßen festgenagelt.",
      "Denn es ist die Eigentümlich- keit solcher Begriffssysteme, daß sie den Menschen 29 festnageln. Er wird durch sie zum Dogmatiker, und dann sagt er: Da gibt es Leute, die wollen das Organische mit ganz anderen Begriffen erklären, die sie von ganz woanders her haben, aber das gibt es nicht; wir haben solche Begriffssysteme ausgebildet, die die Welt hinter den Erscheinungen umfassen, und die ist die einzige Welt und die muß auch das einzig Wirksame in bezug auf das Organische sein. - Aber auf diese Weise wird in die Betrachtung des Organischen das hineingetragen, was man für die Erscheinungen der unorganischen Na- tur ausgebildet hat; man sieht das Organische als auf dieselbe Art gebildet an wie die unorganische Natur.",
      "Hier muß Klarheit geschaffen werden. Ohne diese Klarheit kann man niemals eine wirkliche Diskussions- grundlage schaffen. Anthroposophie will durchaus nicht in dilettantischer Weise gegen berechtigte Methoden sündigen; sie will nicht sündigen gegen das Berechtigte des Atomismus, sondern sie will die Bahn frei haben für das Bilden von Gedankensystemen, wie sie früher für das Anorganische gebildet wurden und jetzt für andere Gebiete der Natur gebildet werden müssen.",
      "Das wird geschehen, wenn man sich sagt: In den Phänomenen will ich nur «lesen»; das heißt, das, was ich zuletzt über den Inhalt der Naturgesetze bekomme, liegt innerhalb der Phänomene selber - geradeso wie beim Lesen eines Wortes der Sinn in den Buchstaben selber hegt. Wenn ich recht liebevoll innerhalb der Phänomene stehenblei- be und nicht darauf aus bin, die Wirklichkeit irgendwie mit einem hypothetischen Gedankensystem zu durch- setzen, dann werde ich in meinem wissenschaftlichen Sinne frei bleiben für eine Weiterentwicklung der Begrif- fe.",
      "Und dieses Freibleiben ist das, was wir ausbilden müssen. 30 Wir dürfen uns nicht durch ein Begriffssystem, das wir für ein bestimmtes Naturgebiet vollberechtigt ausge- bildet haben, festnageln lassen, es auf andere Gebiete anzuwenden. Bilden wir eine bloße Phänomenologie aus, was selbstverständlich nur dadurch geschehen kann, daß man die geschauten oder durch das Experiment dargestellten Phänomene mit Gedanken durchsetzt und verbindet und so zu Naturgesetzen kommt, bleibt man also innerhalb der Phänomene stehen, so bekommt man ein ganz anderes Verhältnis zum Gedanken selbst; dann bekommt man ein Erlebnis davon, wie in den Phäno- menen selbst schon die Naturgesetze vorhanden sind, die dann in unseren Gedanken auftreten.",
      "Geben wir uns so diesen Gedanken hm, dann haben wir gar keine Berechtigung mehr, sofern wir innerhalb der Natur- erscheinungen stehenbleiben, von einem Gegensatz zwi- schen dem subjektiven Gedanken und dem objektiven Naturgesetz zu sprechen. Wir tauchen einfach in die Phänomene unter und haben dann in den Inhalten der Naturgesetze einen Gedankeninhalt gegeben, den uns die Dinge selber geben.",
      "Deshalb sagte Goethe ganz naiv: Dann sehe ich meine Ideen - die eigentlich Naturgesetze waren in der Natur mit Augen. Wenn man sich in dieser Weise zu den Phänomenen der unorganischen Natur stellt, dann ist es möglich, dies in die Organik hinüberzutragen, auch im wissenschaft- lichen Sinne.",
      "Wenn man dann sieht, daß ein Pferd braun oder ein Schimmel weiß ist, wird man das nicht auf unorganische Farben zurückführen, sondern es nur auf etwas beziehen, was als ein geistig-seelisch Lebendiges in einem Organismus selber lebt. Man wird verstehen ler- nen aus der erkrafteten inneren Organisation heraus, daß sich das Tier wie auch die Pflanze selbst die Farbe gibt. 31 Selbstverständlich muß man dabei alle Einzelheiten, zum Beispiel das Funktionieren des Stoffwechsels, innerlich durchschauen.",
      "Aber man trägt dann nicht in die Organik das herauf, was man in der Unorganik gefunden hat. Man nagelt sich nicht fest auf ein bestimmtes Gedan- kensystem, und man wird nicht dieselbe Gesinnung, die man auf einem Gebiete gehabt hat, in die anderen Gebiete herauftragen.",
      "Man bleibt ein «mathematischer Kopf», mehr als die, welche die Begriffe nicht metamorphosie- ren wollen ins Qualitative hinein. So kommt man dazu, für die höheren Gebiete des Naturdaseins das innere Anschauen ebenso gelten zu lassen, wie man das innere Anschauen gelten läßt für leblose mathematische Gebilde.",
      "Das ist das, was ich hier nur kurz skizzieren kann, was aber, wenn es weiter ausgebildet wird, zeigt, daß die wissenschaftliche Seite der Anthroposophie durchaus das kann, was Goethe nannte: Rechenschaft ablegen vor jedem, auch vor dem strengsten Mathematiker. Denn das wollte Goethe mit der Ausbildung seiner Idee von der Urpflanze, zu der er gekommen ist, und mit der Idee des Urtieres, wozu er nicht gekommen ist.",
      "Und das will Anthroposophie: Hervorgehen lassen aus der Goethe- schen Weltanschauung das, was diese in bezug auf die Erscheinungen der Natur konnte und vom Erfassen des Lebendigen in der Imagination aufsteigen zu dem Typus der Pflanze und zu dem Typus des Tieres. Ich habe schon in den 80er Jahren des vorigen Jahrhunderts ge- zeigt, daß wir für die organische Natur die aus dem Unorganischen genommenen Begriffe metamorphosie- ren müssen.",
      "Davon werde ich in den nächsten Tagen noch weiter zu sprechen haben. Dadurch kommt man aber dazu, in der Organik dasjenige zu sehen, was das eigentliche Wirkungsprinzip, Gestaltungsprinzip ist. Und 32 da möchte ich an den Schluß dieser Betrachtungen etwas hinstellen, was in den nächsten Tagen noch weitere Be- trachtung erfahren wird, und was zeigen soll, wie diese materialistische Phase naturwissenschaftlicher Entwick- lung von der Anthroposophie nicht unterschätzt wird.",
      "Die Anthroposophie muß in dieser materialistischen Phase der Naturwissenschaft ein wichtiges Übergangs- prinzip sehen, eine Erziehungsmethode, damit man ein- mal gelernt hat, sich rein der äußeren Sinnes-Empirie hinzugeben. Das war außerordentlich erzieherisch für die Entwicklung der Menschheit, und nur wenn man diese Erziehung genossen hat, kann man auch dazu kommen, gewisse Dinge mit voller Klarheit zu über- sehen.",
      "Denn wer nun, ausgerüstet mit solchem Wissen- schaftssinn die äußere materielle Welt betrachtet, der schaut, wie sich diese materielle Welt innerlich im Menschen «spiegelt», wenn ich mich dieses Ausdrucks bedienen darf. Die Welt, wie wir sie im Innern erleben, ist mehr oder weniger eine Abstraktion, ein von Empfindungen und Willensimpulsen durchzogenes inneres Bild dessen, was die äußere materielle Welt ist; so daß wir, wenn wir vom Verfolgen der materiellen Außenwelt zum Geistig-See- lischen übergehen, zu einem bloß Bildhaften kommen.",
      "Halten wir das ganz streng fest: außen die Summe der materiellen Erscheinungen, die wir im phänomenologi- schen Sinne anschauen im Innern das Seelisch-Geistige, mit einem gewissen abstrakten Charakter, mit einem Bildcharakter. Tritt man aber mit anthroposophischer Anschauung in die Betrachtung dessen ein, was der äußeren materiellen Welt geistig zugrunde liegt, in den Geist, der da wirkt in den Bewegungen der Sterne, in dem Werden der Mineralien, der Pflanzen und der Tiere, 33 tritt man ein in das Geistige des Werdens der Außenwelt, lernt man diese durch Imagination, Inspiration und In- tuition kennen, dann gibt uns auch das ein inneres Spiegelbild des Menschen.",
      "Aber was ist dieses innere Spiegelbild des Menschen? Das sind unsere materiellen Organe. Sie antworten mir jetzt auf das, was ich vorher kennengelernt habe als die Natur der Sonne, als die Natur des Mondes, der Mineralien, der Pflanzen, der Tiere und so weiter; darauf antworten mir die inneren Organe.",
      "Ich lerne das Eigene des menschlichen Orga- nismus nur kennen, wenn ich das Äußere der Welt kennenlerne. Die materielle Welt außen spiegelt sich innen geistig-seelisch; die geistig-seelische Welt außen spiegelt sich innen in den Formen von Lunge, Leber, Herz und so weiter.",
      "Die inneren Organe sind, wenn man sie anschaut, so in einem Verhältnis zur geistigen Außenwelt, wie unsere Gedanken und Empfindungen zur materiellen Außenwelt in einem Verhältnis sind. Das zeigt uns, wie die Anthroposophie durchaus nicht in einem schwärmerischen Sinne den Materialis- mus ablehnen will.",
      "Sehen Sie sich den ganzen Umfang der Naturwissenschaft an: Tausende werden unbefriedigt sein über das, was da aus der Naturwissenschaft mit den gewöhnlichen Methoden gewonnen wird. Die Anthro- posophie wird durch ihre Methoden gerade über das Materielle der Welt eine Anschauung gewinnen, die nicht unbefriedigt lassen wird.",
      "Sie anerkennt das Materielle in der eigenen inneren Organisation und in dem Phäno- menologischen der Umwelt; aber sie muß zu gleicher Zeit erkennen, daß diese innere Organisation ein Ergebnis, eine Konsequenz von kosmischem Geistig-Seelischen ist. Sie will daher auch das ergänzen, was in der Astro- nomie, in der Astrophysik, Physik oder Chemie nur 34 mathematisch geleistet wird.",
      "Das wird sie in einer orga- nischen Kosmologie und so weiter erkunden und da- durch auch zu einem Verständnis des materiellen Men- schen vordringen. Darin liegen dann die Grundlagen für dasjenige, was Anthroposophie für die Medizin, die Biologie und so weiter geben will.",
      "So glaube ich durch diese Andeutungen, die ich jetzt nur ganz skizzenhaft geben konnte, darauf hingedeutet zu haben, wie Anthroposophie, wenn man sie richtig erfaßt, nicht so angesehen werden kann, als ob sie von sich aus sich in einen Kampf stellen wolle gegen die gegenwärtige Wissenschaft; sondern die Dinge liegen so, daß die gegenwärtigen Vertreter der Wissenschaft noch nicht die Brücke zur Anthroposophie geschlagen haben, um zu sehen, wie die Anthroposophie streng wissenschaftlich auch gegenüber den Naturerscheinun- gen sein will. 35"
    ],
    "sentences": [
      [
        "Sehr verehrte Anwesende!",
        "Es war der Wunsch des Ko- mitees für diese Hochschulwoche, daß ich an jedem Tage durch einige Ausführungen einleite, was im Laufe des Tages wissenschaftlich zur Verhandlung kommen soll."
      ],
      [
        "Es ist das ja wohl so eingerichtet worden aus der An- schauung heraus, daß durch Anthroposophie die ein- zelnen Wissenschafts- und Lebenszweige eine gewisse Befruchtung erfahren sollen; und nur in diesem Sinne, als einleitende Bemerkungen zu den Verhandlungen des Tages, bitte ich Sie diese ersten Vorträge aufzufassen.",
        "Was mich immer am meisten gewundert hat bei der Entgegennahme der anthroposophischen Forschungs- methode, das ist der Widerstand, der insbesondere von philosophisch-naturwissenschaftlicher Seite - ich sage nicht: rein von naturwissenschaftlicher Seite - der An- throposophie entgegengebracht wird, und zwar aus dem Grunde, weil man glaubt, daß Anthroposophie in einer unberechtigten oppositionellen Weise den Methoden der Naturwissenschaft gegenüberstehe, welche sich in so fruchtbarer Art im Laufe der letzten Jahrhunderte, ins- besondere des 19."
      ],
      [
        "Jahrhunderts herausgebildet haben.",
        "Und mir scheint, daß unter all den Dingen, die in bezug auf Anthroposophie von unserer Zeitgenossenschaft am allerschwersten eingesehen werden, das ist, daß An- 13 throposophie gerade gegenüber der Naturwissenschaft nichts anderes will, als die Methoden, die in der Natur- wissenschaft sich so fruchtbar erwiesen haben, in ent- sprechender Weise weiterzubilden."
      ],
      [
        "Allerdings muß man unter der Idee der Weiterbildung etwas anderes noch verstehen können, wenn man von dieser Seite her zum Begreifen des Anthroposophischen kommen will, als das, was man gewöhnlich heute eine Weiterbildung von theoretischen Anschauungen nennt.",
        "Eine Weiterbildung der theoretischen Anschauungen ist heute den meisten Menschen dieses: daß die besondere Art der Gedankenverknüpfung - insbesondere, wenn ich mich so ausdrücken darf, das Feld der Gedanken - dieselbe bleibt, auch wenn man die betreffenden Gedan- kensysteme auf andere Gebiete der Welterscheinungen ausdehnt."
      ],
      [
        "So zum Beispiel: Man kommt, wenn man sich naturwissenschaftlich betätigt, gegenüber der leblosen, der anorganischen Natur in die Notwendigkeit, gewisse Gedankenverknüpfungen, ein gewisses Feld von Gedan- ken, das heißt eine Summe von miteinander verbunde- nen Gedanken zugrundezulegen, um gewissermaßen eine Theorie der unorganischen, der leblosen Naturerschei- nungen zu bekommen.",
        "Dieses System von Gedanken will man dann so, wie es ist, weiter ausdehnen, wenn man ein anderes Gebiet der Welt, also zum Beispiel das Gebiet der organischen Naturerscheinungen, zu begrei- fen bestrebt ist."
      ],
      [
        "Man will also mit derjenigen kausalen Orientierung, die sich so fruchtbar erweist im unorga- nischen Gebiet, einfach hinübergehen in das Gebiet der Lebewesen und diese mit denselben Begriffen durch- tränken und erklären, also gewissermaßen begrifflich das Gebiet der Lebewesen ebenso zu einem Wirkungssystem von unorganischen Kausalitäten machen, wie man ja 14 genötigt ist, es gegenüber der leblosen, der unorganischen Natur zu tun.",
        "Also was man sich angeeignet hat als Gedankensystem aus der leblosen Natur, das trägt man einfach hinüber in die organische Natur."
      ],
      [
        "Und das ist das, was man heute gewöhnlich unter «Erweiterung» von Gedanken und Theorien versteht.",
        "Damit steht allerdings dann im vollen Gegensatz, was Anthroposophie unter einer solchen Erweiterung von Gedanken verstehen muß."
      ],
      [
        "Sie muß den Begriff eines gewissen selbständigen Wachsens, eines Sichmetamor- phosierens der Idee vollziehen, wenn von einem Gebiete der Welterscheinungen zu einem anderen übergegangen wird, so daß man nicht bloß das, was man an den leb- losen Naturerscheinungen gelernt hat, ich möchte sa- gen «logisch übertragen» kann auf die belebten Natur- erscheinungen.",
        "So wie vergleichsweise in der Lebewelt die Dinge selber sich sehr verändern, wenn sie wachsen, wenn sie Metamorphosen durchmachen, und wie sie dann oftmals in der Gestaltung, die sie angenommen haben, gar nicht wiederzuerkennen sind, so müssen auch die Gedanken andere Gestaltungen annehmen, wenn sie in ein anderes Gebiet kommen."
      ],
      [
        "Was aber über alle Ge- biete hin dasselbe bleibt und was dann der ganzen wis- senschaftlichen Weltauffassung methodisch einen moni- stischen Charakter gibt, das ist die Art und Weise, wie man sich innerlich stellt zu dem, was man «wissen- schaftliche Gewißheit» nennen kann, was die Grundlage gibt zur wissenschaftlichen Überzeugung.",
        "Wer zu prü- fen vermag, warum man nicht mit den Begriffen, die man in der leblosen Natur schon einmal gewohnt ist anzu- wenden, zu einer Befriedigung des menschlichen Kau- salitätsbedürfnisses kommt - wenn ich mich des Du Bois-Reymondschen Ausdruckes bedienen darf -, wer 15 das wirklich innerlich kennenlernt, der kann es dann hinüberführen in die Art und Weise, wie man durch ganz andere Begriffe, die aber doch nur Metamorphosen gegenüber den früheren Begriffen sind, überzeugt wird in der Welt des Lebendigen."
      ],
      [
        "Diese Art, wie sich der Mensch da innerhalb des Wissenschaftsgetriebes stellt, ist durchaus monistisch durch die ganze wissenschaft- liche Weltanschauung hindurch.",
        "Das ist etwas, was gewöhnlich mißverstanden wird und was dazu führt, daß man der anthroposophisch-wissenschaftlichen Welt- anschauung nicht einen monistischen, sondern einen dualistischen Charakter beilegen will."
      ],
      [
        "Das zweite, was sehr häufig zu Mißverständnissen führt, ist der Phänomenalismus, dem sich Anthroposo- phie gerade mit Bezug auf Naturwissenschaft hingeben muß.",
        "Wir haben ja gerade in dem für so vieles fruchtbar- sten Zeitalter naturwissenschaftlicher Entwicklung, etwa in der Zeit, in welcher der bedeutende Naturforscher Virchow seine Rede gehalten hat über die Ablösung der philosophischen Weltanschauung durch die naturwis- senschaftliche, erfahren, wie alles, was damals mit einer gewissen historischen Berechtigung an fruchtbaren Be- griffen über das Anorganische gewonnen worden ist, dazu geführt hat, einen gewissen Rationalismus in der Naturwissenschaft zu begründen."
      ],
      [
        "Und das Zeitalter, das auf der einen Seite streng auf Empirismus gegenüber der äußeren Tatsachenwelt hinarbeitete, das erging sich doch in einem sehr weittragenden Rationalismus, wenn es dazu kam, die empirisch erkundeten Naturtatsachen zu erklären.",
        "Demgegenüber steht nun die Anthroposophie auf dem Standpunkte, der sich ergibt - wenigstens für mich sich ergeben hat, wenn ich diese persönliche Bemerkung 16 machen darf - aus der Goetheschen Naturauffassung heraus."
      ],
      [
        "Anthroposophie steht auf dem Boden einer phä- nomenologischen Naturauffassung.",
        "In einer gewissen Weise hat diese Phänomenologie in der neueren Zeit wieder Ernst Mach begründet, und so wie er sie begrün- det, scheint sie durchaus wiederum fruchtbare Ge- sichtspunkte zu enthalten, wenn man ihre Grenzen ein- hält."
      ],
      [
        "Es handelt sich bei Goethe einfach um das, was in seinen Worten liegt: Die Erscheinungswelt selbst ist schon genügend Theorie, man braucht nicht erst zu künst- lichen Theorien fortzuschreiten.",
        "Die Bläue des Himmels ist ein Phänomen, innerhalb dessen man stehenbleiben und sich nicht herbeilassen soll, nun in rationalistischer Weise durch bloße Gedanken hinter den Erscheinungen zunächst hypothetische, angenommene Erklärungsgründe zu suchen."
      ],
      [
        "Goethe kam ja auf diesem Wege zur Statu- ierung dessen, was er «Urphänomen» nannte.",
        "Wenn auch, wie es ja selbstverständlich ist, im Laufe des für die Naturwissenschaft so fruchtbaren 19.",
        "Jahrhunderts vieles von dem überholt worden ist, was Goethe in der Naturwissenschaft wollte, so kann man doch sagen: Das Methodische, die Denkweise selbst, die Goethe in die Naturwissenschaft hineingetragen hat, ist heute nicht nur noch nicht überholt, sondern sie scheint mir überhaupt noch nicht gründlich genug verstanden zu sein."
      ],
      [
        "Ich weiß sehr gut, wie im 19.",
        "Jahrhundert manches - man möchte sagen fast alles - von den Einzelheiten Goethescher Darstellungen über naturwissenschaftliche Dinge überholt worden ist.",
        "Dennoch möchte ich auch heute noch den Satz aufrecht erhalten, den ich in den 80er Jahren des vorigen Jahrhunderts in bezug auf die Goethesche Naturanschauung ausgesprochen habe: daß 17 Goethe der Kopernikus und Kepler ist für die organi- sche Naturwissenschaft."
      ],
      [
        "Ich will diesen Satz aus dem Grunde auch heute noch aufrecht erhalten, weil ich glaube, daß folgendes durchaus gerechtfertigt ist.",
        "Wodurch kommen wir denn schließlich zu einer wirklichen Naturanschauung auf dem Gebiete, auf dem gerade das 19."
      ],
      [
        "Jahrhundert so viel geleistet hat?",
        "Ich kann das, was ich meine, nicht anders begrenzen als durch diese historische Kategorie.",
        "Das, worin das 19.",
        "Jahr- hundert in der Naturwissenschaft so viel geleistet hat, führt zuletzt fast überall zurück auf die Anwendung der mathematischen Methoden; denn auch da, wo man nicht rein mathematisch vorgeht, sondern nach anderen Kau- salitätsprinzipien denkt, wo man Theorien ausgebildet hat, lag ja durchaus auch die mathematische Denkweise zugrunde."
      ],
      [
        "Bezeichnend dafür ist etwa das Folgende: Wir haben gesehen, wie im Laufe des 19.",
        "Jahrhunderts gewisse Partien der Naturwissenschaft durchaus in einer gewis- sen rationalistischen Weise dadurch begründet werden sollten, daß man Mathematik in sie einführte."
      ],
      [
        "Bekannt ist der Kantsche Satz, daß eigentlich in jeder Wissenschaft nur so viel wirkliche Gewißheit sei, wie Mathematik in ihr zu finden sei. - Nun kann man selbstverständlich Mathematik nicht überall hintragen.",
        "Die Kausalitätser- klärungen gehen weiter als die Möglichkeit mathemati- scher Begriffsbildungen."
      ],
      [
        "Aber das, was man so unter- nommen hat an Kausalitätserklärungen, das wurde doch weitgehend nach dem Muster mathematischer Begriffs- bildungen unternommen.",
        "Und als sich dann Ernst Mach daranmachte, von seinem mehr phänomenologischen Standpunkte aus dieses Begriffssystem zu überschauen, mußte er auch auf den Begriff der Kausalität zurück- 18 blicken, wie er sich in der Naturwissenschaft im Laufe des 19."
      ],
      [
        "Jahrhunderts ausgebildet hat, und er wollte zu einem gewissen Inhalt für diesen Kausalitätsbegriff kom- men.",
        "Zuletzt sagte er sich: Wenn ich eine Wirkung mit einer Ursache zusammendenke, so ist doch eigentlich nichts anderes darin enthalten als ein mathematischer Funktionsbegriff; zum Beispiel wenn ich sage: x ist gleich y, wobei ich unter x die Ursachen zusammenfasse und unter y die Wirkung, habe ich das Ganze auf diejenigen Begriffe zurückgeführt, die ich in der Mathematik habe, wenn ich den Funktionsbegriff bilde."
      ],
      [
        "Also man kann auch aus der Geschichte der Wissenschaften sehen, wie man den Mathematikbegriff in das ganze Gebiet der Naturwissenschaft hineingetragen hat.",
        "Nun wird Goethe - und zwar mit einem gewissen Recht gewöhnlich als ein Nicht-Mathematiker angese- hen; er hat sich ja selbst als einen solchen bezeichnet."
      ],
      [
        "Aber wenn man so einfach Goethe als einen Nicht- Mathematiker hinstellt, so führt das auch wieder zu Mißverständnissen - in dem Sinne etwa, daß Goethe nicht viel im einzelnen mathematisch habe leisten kön- nen, daß er nicht besonders geschickt gewesen sei, auch schon zu seiner Zeit durchaus bestehende mathemati- sche Exempel zu lösen.",
        "Das muß natürlich durchaus zugegeben werden."
      ],
      [
        "Ich glaube auch nicht, daß Goethe bei seinem ganzen Wesen sonderlich viel Geduld gehabt hätte, sich auf die Lösung einzelner mathematischer Exempel einzulassen, wenn es mehr ins Algebraische hineingegangen wäre.",
        "Das muß schon zugegeben wer- den."
      ],
      [
        "Aber Goethe war in gewissem Sinne, so paradox es klingt, mehr ein mathematischer Kopf als mancher Ma- thematiker; denn er hatte eine feine Einsicht in die Natur des Mathematisierens, in die Natur des Bildens von 19 mathematischen Begriffen, und er schätzte diese Art und Weise zu denken, die ganz in dem inneren Seelenprozeß auch mit dem Inhalt der Vorstellung bleibt, wenn sie Begriffe bildet.",
        "Man überschaut im Mathematischen, wenn man Be- griffe bildet, innerlich vollständig alles."
      ],
      [
        "Nehmen Sie als ein einfaches Beispiel in der euklidischen Geometrie den gewöhnlichen Beweis dafür, daß die drei Winkel eines Dreiecks zusammen 180 Grad betragen, wo man oben durch die Spitze des Dreiecks eine Parallele zur Grund- linie zieht, die dort auf diese Weise entstandenen Winkel betrachtet, die als Wechselwinkel gleich sind den beiden anderen Winkeln des Dreiecks - der dazwischen liegende bleibt sich ja gleich -, und wo man dann sehen kann, wie diese drei Winkel dort an der Spitze zusammen 180 Grad betragen, also in ihrer Summe den drei Winkeln des Dreiecks gleich sind. - Wenn man das überschaut, hat man einen mathematischen Beweis, aber man hat zu gleicher Zeit etwas, wobei man gar nicht abhängig ist von einer äußeren Anschauung, sondern durchaus die Dinge in innerlichem Konstruieren überschauen kann.",
        "Hat man dann ein äußeres Dreieck, so findet man, daß durch die äußeren Tatsachen verifiziert wird, was man vorher innerlich überschaut hat."
      ],
      [
        "Das ist in der ganzen Mathematik so.",
        "Es bleibt alles so, daß man nicht an die Sinnesanschauung heranzugehen braucht, um zu dem zu kommen, was man «Beweis» nennt, daß aber alles, was man innerlich gefunden hat, auch äußerlich Stück für Stück verifiziert werden kann."
      ],
      [
        "Diese besondere Art des Mathematischen ist es ja, welche Goethe gerade als die eminent wissenschaftliche ansah, und insofern war er wirklich ein guter mathema- tischer Kopf.",
        "Das liegt zum Beispiel auch der Führung 20 jenes berühmten Gespräches zugrunde, das Goethe und Schiller einmal in der Blütezeit ihrer Freundschaft ge- führt haben über die Methode der naturwissenschaft- lichen Betrachtung."
      ],
      [
        "Sie waren beide bei einem Vortrage, den der Naturforscher Batsch in der Naturforschenden Gesellschaft in Jena gehalten hatte, und als sie fortgin- gen, sagte ja Schiller zu Goethe über das, was sie dort gehört hatten, das sei eine zerstückelte Art, die Naturer- scheinungen zu betrachten, damit komme man zu nichts Ganzem. - Man kann sich denken, daß Batsch einfach die einzelnen Naturobjekte nebeneinander hingeordnet und es unterlassen hatte, wie es ja auch durchaus einem Naturforscher der damaligen Zeit geziemte, irgendetwas vorzuführen, was zu einer Gesamtanschauung in der Natur führen konnte.",
        "Schiller empfand dies unbefrie- digend und sprach sich darüber bei Goethe aus."
      ],
      [
        "Und Goethe sagte, er verstehe es, eine gewisse Einheit, eine gewisse Ganzheit in eine solche Naturbetrachtung hin- einzubringen.",
        "Und er fing an, mit wenigen Strichen - er erzählt es ja selbst - die «Urpflanze» aufzuzeichnen, wie sie zu denken ist, wie sie innerlich angeschaut werden kann, nicht, wie sie in dieser oder jener Pflanze zu Tage tritt, sondern wie sie innerlich angeschaut werden kann mit Wurzel, Stengel, Blättern, Blüte, Frucht."
      ],
      [
        "Ich habe in meinen Einleitungen zu den «Naturwis- senschaftlichen Schriften» Goethes in den 80er Jahren des vorigen Jahrhunderts versucht, das Bild, das damals Goethe auf das Papier vor Schiller hingeworfen hat, nachzuzeichnen. - Schiller sah sich das an und sagte dann aus seiner Denkweise heraus: Das ist keine Erfah- rung, das ist eine Idee. - Schiller hatte eben gemeint: wenn man so etwas aufzeichnet, so hat man das aus sich heraus gesponnen; das ist als Idee, als Gedanke ganz gut, 21 hat aber in der Wirklichkeit im Grunde genommen keine Quelle.",
        "Goethe verstand diese Denkweise eigentlich gar nicht, und zuletzt endete das Gespräch damit, daß Goethe erwiderte, gewissermaßen das Gespräch zusammenfas- send: Wenn das so ist, dann sehe ich meine Ideen mit Augen."
      ],
      [
        "Was meinte denn Goethe damit?",
        "Er meinte - er hat es nicht so ausgesprochen, aber er meinte es: Wenn ich ein Dreieck hinzeichne, so hat es von selbst eine Winkel- summe von 180 Grad; und wenn ich noch so viele Dreiecke anschaue, das, was ich an diesem einen Dreieck innerlich konstruiert habe, das paßt auf alle Dreiecke; ich habe also etwas aus dem Innern heraus gewonnen, das nun in vollem Umfang auf das Erfahrene paßt."
      ],
      [
        "So wollte Goethe auch eine «Urpflanze» - gewissermaßen gemäß dem «Urdreieck» - zeichnen, und einen solchen Cha- rakter sollte diese Urpflanze haben, daß man diesen bei jeder einzelnen Pflanze finden könne.",
        "Und so, wie die Winkelsumme jedes Dreiecks, wenn man das Urdreieck hat, 180 Grad beträgt, so sollte auch dieses ideelle Gebilde, die Urpflanze, in jeder einzelnen Pflanze wiedergefunden werden, wenn man die ganze Pflanzenreihe durchgeht."
      ],
      [
        "In diesem Sinne wollte Goethe die ganze Wissen- schaft gestalten.",
        "Im wesentlichen wollte er - er kam ja damit nicht weiter - die Wissenschaft des Organischen so gestalten und eine solche Denkweise einführen, wie sie sich für die Wissenschaft des Unorganischen als fruchtbar erwiesen hat."
      ],
      [
        "Man sieht das ganz besonders klar, wenn Goethe von Italien aus schreibt, wie er die Idee der Urpflanze immer weiter ausgebildet hat.",
        "Da sagt er ungefähr: Da, unter den Pflanzen in Süditalien und Sizilien in der Mannigfaltigkeit der Pflanzenwelt ist mir die Urpflanze ganz besonders aufgegangen, und es 22 muß sich doch ein Gebilde finden lassen, das die Mög- lichkeit aller wirklichen Pflanzen in sich hat, ein Gebil- de, das sich nach verschiedenen Seiten hin variieren kann; es nimmt dann diese oder jene, langgestreckte oder andere Blattform an, bildet bald die Blüte, bald die Frucht mehr aus und so weiter so wie ein Dreieck stumpfwinklig oder spitzwinklig sein kann."
      ],
      [
        "Ein Gebilde wollte Goethe finden, nach dessen Muster alle Pflanzen gebildet sind.",
        "Es ist ganz falsch, wenn dann später Schieiden meinte, Goethe habe mit der Urpflanze eine tatsächliche Pflanze gemeint.",
        "Das ist nicht so so wie auch der Mathemati- ker, der vom Dreieck spricht, nicht irgendein bestimm- tes Dreieck im Auge hat -, sondern Goethe meinte ein Gebilde, das innerlich erzeugt wird, das sich aber in der Außenwelt überall verifiziert findet."
      ],
      [
        "So war Goethe im Grunde genommen ein durchaus mathematischer Kopf, viel mathematischer als etwa die, die die Astronomie ausbilden.",
        "Und das ist das Wesent- liche.",
        "Das veranlaßte Goethe auch, in diesem Gespräch mit Schiller zu sagen: Dann sehe ich meine Ideen mit Augen. - Er sah sie mit Augen, weil er sie überall in den Phänomenen verfolgen konnte."
      ],
      [
        "Er begriff gar nicht, daß etwas nur eine «Idee» sein sollte, weil er sich im vollen Einklang fand mit der Erfahrung, wenn er Ideen bildete; geradeso, wie der Mathematiker sich im Einklang fühlt mit der Erfahrung, wenn er mathematische Ideen bildet.",
        "Das aber führte Goethe, ich möchte sagen, durch eine innere Konsequenz dazu, zur bloßen Phänomenologie zu kommen, das heißt, nichts hinter den Erscheinun- gen als solchen zu suchen, vor allen Dingen nicht eine rationalistische Atomwelt zu konstruieren."
      ],
      [
        "Nun, damit betritt man ein Gebiet, auf dem sich viele ich kann aber doch nur sagen - auf Mißverständnissen 23 beruhende Kämpfe gegenüber mancher naturwissen- schaftlich-philosophischen Anschauung entwickelten.",
        "Es handelt sich zunächst einfach darum, das, was sich den Sinnen in der äußeren Welt darbietet, was also in der Beobachtung und im Experiment gegeben ist, rein als Phänomen zu betrachten."
      ],
      [
        "Goethe und mit ihm die ganze naturwissenschaftliche Phänomenologie beschränkt sich darauf, nicht gleich von irgendeinem sinnlichen Phäno- men zu einem dahinterstehenden Atomgeschehen zu gehen, sondern zunächst das sinnliche Phänomen und das einzelne Element der sinnlichen Tatsachen rein ins Auge zu fassen, sie also nicht auf ein Dahinterliegendes zu beziehen, sondern auf andere Elemente in der sinn- lichen Erscheinungswelt, und den Zusammenhang in der sinnlichen Erscheinungswelt aufzusuchen.",
        "Man kann sehr leicht - ich verstehe vollständig, wo- her die entsprechenden Mißverständnisse kommen - eine solche Phänomenologie sogar trostlos finden."
      ],
      [
        "Man könnte zum Beispiel sagen: Wenn man sich nun bloß beschränken will auf das Beschreiben der gegenseitigen Beziehungen der sinnlichen Phänomene und dann diejenigen Phäno- mene aufsucht, die am einfachsten sind, in denen sich möglichst überschaubares Geschehen abspielt - und die Goethe «Urphänomene» nennt -, so kommt man bei einem solchen Vorgehen nicht zu einer Anschauung über jene unendlich fruchtbaren Dinge, die zum Beispiel die moderne Chemie geliefert hat.",
        "Wie, so könnte man fragen, kann man denn eigentlich gegenüber den Atom- gewichtsverhältnissen auskommen, ohne eine Anschau- ung über eine atomistische Welt?"
      ],
      [
        "Nun, in einem solchen Falle möchte man aber doch die Gegenfrage stellen: Wenn man sich nun wirklich besinnt auf das, was da vorliegt, hat man es denn da zu tun mit einer Notwen- 24 digkeit, vom Phänomen abzugehen?",
        "Man hat es gar nicht damit zu tun."
      ],
      [
        "Man hat es auch bei den Atomgewichts- verhältnissen mit Phänomenen zu tun, nämlich mit Ge- wichtsverhältnissen.",
        "Aber man könnte auch fragen: Führt es denn weiter, wenn man nun diese durch Zahlen aus- drückbaren Atomgewichtsverhältnisse dadurch zu er- klären versucht, daß man gewisse Molekularstrukturen aus den Atomgewichten auf rein denkerische, rationa- listische Weise bildet?"
      ],
      [
        "Man kann eben auch diese Fra- ge aufwerfen.",
        "Kurz, worum es sich handelt, wenn die Goethesche Denkweise ausgebildet wird, das ist: ste- henzubleiben innerhalb der Phänomene selbst.",
        "Ich möchte dafür einen trivialen Vergleich gebrauchen."
      ],
      [
        "Nehmen wir an, jemand bekommt ein aufgeschriebe- nes Wort vor sein Auge.",
        "Was wird er tun?",
        "Nun, wenn er nie lesen gelernt hat, wird er davor stehen wie vor etwas Unerklärbarem.",
        "Hat er aber lesen gelernt, so wird er unbewußt die einzelnen Formen zusammenfügen; er wird den Wortsinn in der Seele erleben."
      ],
      [
        "Aber er wird ganz gewiß nicht von den Formen aus, zum Beispiel beim W, etwas zu erklären versuchen, indem er den Ausgang nähme von dem nach aufwärts gehenden Strich, dann überginge zu dem nach abwärts gehenden, um dadurch auf etwas diesem Buchstaben Zugrundeliegendes zu kommen.",
        "Nein, er wird lesen und nicht durch Unter- legungen erklären wollen."
      ],
      [
        "So möchte auch die Phäno- menologie «lesen».",
        "Sie möchte innerhalb des Zusammen- hanges der Phänomene stehenbleiben und lesen lernen, und nicht, wenn ich einen Komplex von Phänomenen habe, von ihm aus zurückgehen auf Atomstrukturen."
      ],
      [
        "Es handelt sich also darum, das Feld des Phänomena- len hinzunehmen und in seiner eigenen inneren Bedeu- tung lesen zu lernen.",
        "Dadurch wird man dann zu einer 25 Naturwissenschaft kommen, welche in ihren Inhalten nichts Rationalistisches, hinter den Phänomenen Kon- struiertes hat, sondern welche einfach in der Art und Weise, wie sie die Phänomene überschaut, gewisse ge- setzmäßige Strukturen findet."
      ],
      [
        "Überall wird dieser Na- turwissenschaft eingegliedert sein die Summe der Phä- nomene selbst.",
        "Man wird auf eine bestimmte Art über die Natur reden.",
        "In dieser Art zu reden werden die Natur- gesetze enthalten sein, aber überall werden m den Aus- drucksformen schon die Phänomene selber liegen."
      ],
      [
        "Man wird also das bekommen, was ich nennen möchte: eine den Erscheinungen immanente Naturwissenschaft.",
        "Nach einer solchen strebte Goethe.",
        "Die Art und Weise, wie er das betrieb, muß unter den Fortschritten der neueren Zeit verändert werden, aber es ist doch so, daß das Grundprinzip festgehalten werden kann."
      ],
      [
        "Und wenn dieses Grundprinzip festgehalten wird, stellt sich für die menschliche Auffassungsweise der Natur ganz von selbst etwas heraus, das ich in der folgenden Weise charakte- risieren möchte.",
        "Es ist ja ganz selbstverständlich, daß wir als gegen- wärtige Menschheit unsere naturwissenschaftlichen Be- griffe zunächst an der unorganischen Natur gebildet haben."
      ],
      [
        "Das ist dadurch veranlaßt gewesen, daß die un- organischen Naturerscheinungen verhältnismäßig ein- fach sind; das war aber auch veranlaßt dadurch, daß ja, wenn man ins organische Reich hinaufsteigt, durchaus auch die im Leblosen wirkenden Agenzien fortdauern.",
        "Wenn man vom Mineralreich zum Pflanzenreich her- aufsteigt, dann ist es ja nicht so, daß etwa die leblose Wirkungsweise bei der Pflanze aufhörte; sie wird nur eingefaßt in ein höheres Prinzip, aber sie dauert in der Pflanze fort."
      ],
      [
        "Wir tun recht, wenn wir die physischen und 26 chemischen Prozesse in den Pflanzenorganismus hinein weiterverfolgen, und zwar nach denselben Gesichts- punkten, nach denen wir gewohnt sind, sie in der un- organischen Natur zu verfolgen.",
        "Wir müssen dann nur auch die Fähigkeit haben, in unseren Begriffssystemen überzugehen zu veränderten, zu metamorphosierten Be- griffen."
      ],
      [
        "Wir müssen schon verfolgen, wie das Unorgani- sche auch verwendet wird in der Pflanze und wie die- selben Prozesse, die sich in der leblosen Natur finden, auch in die Pflanze hineingehen.",
        "Aber dadurch wird die Versuchung hervorgerufen, daß man wissenschaftlich nur das verfolgt, was sich aus der mineralischen Welt hereinerstreckt in Pflanze und Tier und dabei einfach unberücksichtigt läßt, was dann in den höheren Reichen dazu auftritt."
      ],
      [
        "Diese Versuchung wurde durch einen be- sonderen Umstand gerade im Laufe des 19.",
        "Jahrhunderts noch außerordentlich größer.",
        "Das ist in folgender Weise geschehen.",
        "Wenn man die leblose Natur betrachtet, fühlt man sich gewissermaßen innerlich tief befriedigt, weil man die Erscheinungen mit mathematischen Gedanken ver- folgen kann."
      ],
      [
        "Und es ist sehr begreiflich, daß Du Bois- Reymond in einer so wortreichen und glänzenden Weise m seiner Rede «Über die Grenzen des Naturerkennens» die Laplacesche Weltanschauung, die er die «astronomi- sche Auffassung» des ganzen natürlichen Weltendaseins nennt, gefeiert hat, möchte ich sagen.",
        "Nach dieser astro- nomischen Auffassung wird ja nicht nur der Sternen- himmel so angesehen, daß man seine einzelnen Phäno- mene mit mathematischen Gedanken zusammenfaßt und sie dann als ein Ganzes, soweit es geht, konstruiert, sondern man versucht, auch damit unterzutauchen in die Konstitution der Materie."
      ],
      [
        "Man versucht im Molekül ein 27 kleines Weltsystem zu konstruieren, wo sich die Atome so bewegen und zueinander stehen wie die Sterne im Weltgebäude.",
        "Man konstruiert sich so im Kleinen kleinste Weltsysteme und hat die Befriedigung, daß man so im Kleinen dieselben Gesetzmäßigkeiten findet wie im Großen."
      ],
      [
        "So hat man in den einzelnen Atomen und Mo- lekülen ein System sich bewegender Körper, wie man draußen im Weltgebäude das System der Fixsterne und Planeten hat.",
        "Das ist charakteristisch für die Art, wie man vor allem im 19."
      ],
      [
        "Jahrhundert gestrebt hat und wo- durch, wie Du Bois-Reymond sagte, das Kausalitäts- bedürfnis des Menschen sich befriedigt fühlt.",
        "Es ist das einfach entstanden aus dem Drang heraus, das mathe- matisch Fruchtbare in alle Naturerscheinungen hinein- zutragen."
      ],
      [
        "Daraus entstand nun eben die Versuchung, bei diesem Mathematischen in der Betrachtung der Natur- erscheinungen stehenzubleiben.",
        "Es wird keinem einfallen, auch einem Anthroposo- phen nicht, wenn er nicht laienhaft über diese Dinge spricht, bestreiten zu wollen, daß dies alles seine Berech- tigung hat, namentlich dann, wenn man innerhalb der Phänomene stehen bleibt und sich bemüht, die Einzel- heiten, zum Beispiel der Astronomie, in diesem Sinne aufzufassen."
      ],
      [
        "Keinem wird es einfallen, dagegen einen Kampf zu führen.",
        "Aber im Laufe des 19.",
        "Jahrhunderts trat das ein, daß man bei dem, was die Welt darbietet, alles das übersah, was qualitativ ist, und nur das sah, was ja da ist und in allem Qualitativen drinnen ist: das, was durch die Mathematik zu erfassen ist."
      ],
      [
        "Da muß man unterscheiden: Man kann durchaus zugeben, daß diese mechanistische Welterklärung voll berechtigt ist; es ist gar nichts dagegen einzuwenden.",
        "Aber etwas anderes ist es, ob man sie auf bestimmten Gebieten als vollberech- 28 tigt erklärt oder ob man sie nun als das einzige mögliche Begriffssystem hingestellt will und mit diesem Begriffs- system schon alles in der Welt für erklärt halten will."
      ],
      [
        "Hier liegt der Differenzpunkt.",
        "Es wird durch den Anthroposophen nicht im geringsten das bestritten, was seine Berechtigung hat.",
        "Die Anthroposophie kämpft nämlich gar nicht gegen die anderen, und es ist interes- sant, bei Diskussionen zu verfolgen, wie Anthroposophie eigentlich alles innerhalb der berechtigten Grenzen zu- gibt."
      ],
      [
        "Es fällt den Anthroposophen gar nicht ein, das, was durch die Naturwissenschaft geltend gemacht wird, ir- gendwie zu bestreiten.",
        "Sondern es handelt sich darum, ob es berechtigt ist, das ganze Gebiet der Phänomene mit der mathematisch-kausalen Denkweise zu umfassen, oder ob es berechtigt ist, aus der Summe der Erscheinungen dasjenige herauszunehmen, was mathematisch-kausal eine reine Abstraktion ist, und es hinzustellen als einen «er- dachten» Welteninhalt, wie es zum Beispiel der frühere Atomismus getan hat."
      ],
      [
        "Heute ist der Atomismus bis zu einem gewissen Grade schon phänomenologisch ge- worden, und bis zu diesem Grade geht Anthroposophie ganz gewiß mit.",
        "Aber es handelt sich darum, daß heute eben noch etwas hereinspukt von dem im 19."
      ],
      [
        "Jahrhundert so ungoetheschen Atomismus, der sich nicht beschränkte auf die Phänomene, sondern der ein reines Begriffssystem hinter den Phänomenen konstruierte.",
        "Und wenn man sich nicht klar darüber ist, daß man es doch nur mit einem Begriffssystem zu tun hat, das die Welt hinter den Erscheinungen sucht, sondern sich der Anschauung hin- gibt, man habe mit diesem Begriffssystem ein Reales ergriffen, so wird man durch dieses Begriffssystem ge- wissermaßen festgenagelt."
      ],
      [
        "Denn es ist die Eigentümlich- keit solcher Begriffssysteme, daß sie den Menschen 29 festnageln.",
        "Er wird durch sie zum Dogmatiker, und dann sagt er: Da gibt es Leute, die wollen das Organische mit ganz anderen Begriffen erklären, die sie von ganz woanders her haben, aber das gibt es nicht; wir haben solche Begriffssysteme ausgebildet, die die Welt hinter den Erscheinungen umfassen, und die ist die einzige Welt und die muß auch das einzig Wirksame in bezug auf das Organische sein. - Aber auf diese Weise wird in die Betrachtung des Organischen das hineingetragen, was man für die Erscheinungen der unorganischen Na- tur ausgebildet hat; man sieht das Organische als auf dieselbe Art gebildet an wie die unorganische Natur."
      ],
      [
        "Hier muß Klarheit geschaffen werden.",
        "Ohne diese Klarheit kann man niemals eine wirkliche Diskussions- grundlage schaffen.",
        "Anthroposophie will durchaus nicht in dilettantischer Weise gegen berechtigte Methoden sündigen; sie will nicht sündigen gegen das Berechtigte des Atomismus, sondern sie will die Bahn frei haben für das Bilden von Gedankensystemen, wie sie früher für das Anorganische gebildet wurden und jetzt für andere Gebiete der Natur gebildet werden müssen."
      ],
      [
        "Das wird geschehen, wenn man sich sagt: In den Phänomenen will ich nur «lesen»; das heißt, das, was ich zuletzt über den Inhalt der Naturgesetze bekomme, liegt innerhalb der Phänomene selber - geradeso wie beim Lesen eines Wortes der Sinn in den Buchstaben selber hegt.",
        "Wenn ich recht liebevoll innerhalb der Phänomene stehenblei- be und nicht darauf aus bin, die Wirklichkeit irgendwie mit einem hypothetischen Gedankensystem zu durch- setzen, dann werde ich in meinem wissenschaftlichen Sinne frei bleiben für eine Weiterentwicklung der Begrif- fe."
      ],
      [
        "Und dieses Freibleiben ist das, was wir ausbilden müssen. 30 Wir dürfen uns nicht durch ein Begriffssystem, das wir für ein bestimmtes Naturgebiet vollberechtigt ausge- bildet haben, festnageln lassen, es auf andere Gebiete anzuwenden.",
        "Bilden wir eine bloße Phänomenologie aus, was selbstverständlich nur dadurch geschehen kann, daß man die geschauten oder durch das Experiment dargestellten Phänomene mit Gedanken durchsetzt und verbindet und so zu Naturgesetzen kommt, bleibt man also innerhalb der Phänomene stehen, so bekommt man ein ganz anderes Verhältnis zum Gedanken selbst; dann bekommt man ein Erlebnis davon, wie in den Phäno- menen selbst schon die Naturgesetze vorhanden sind, die dann in unseren Gedanken auftreten."
      ],
      [
        "Geben wir uns so diesen Gedanken hm, dann haben wir gar keine Berechtigung mehr, sofern wir innerhalb der Natur- erscheinungen stehenbleiben, von einem Gegensatz zwi- schen dem subjektiven Gedanken und dem objektiven Naturgesetz zu sprechen.",
        "Wir tauchen einfach in die Phänomene unter und haben dann in den Inhalten der Naturgesetze einen Gedankeninhalt gegeben, den uns die Dinge selber geben."
      ],
      [
        "Deshalb sagte Goethe ganz naiv: Dann sehe ich meine Ideen - die eigentlich Naturgesetze waren in der Natur mit Augen.",
        "Wenn man sich in dieser Weise zu den Phänomenen der unorganischen Natur stellt, dann ist es möglich, dies in die Organik hinüberzutragen, auch im wissenschaft- lichen Sinne."
      ],
      [
        "Wenn man dann sieht, daß ein Pferd braun oder ein Schimmel weiß ist, wird man das nicht auf unorganische Farben zurückführen, sondern es nur auf etwas beziehen, was als ein geistig-seelisch Lebendiges in einem Organismus selber lebt.",
        "Man wird verstehen ler- nen aus der erkrafteten inneren Organisation heraus, daß sich das Tier wie auch die Pflanze selbst die Farbe gibt. 31 Selbstverständlich muß man dabei alle Einzelheiten, zum Beispiel das Funktionieren des Stoffwechsels, innerlich durchschauen."
      ],
      [
        "Aber man trägt dann nicht in die Organik das herauf, was man in der Unorganik gefunden hat.",
        "Man nagelt sich nicht fest auf ein bestimmtes Gedan- kensystem, und man wird nicht dieselbe Gesinnung, die man auf einem Gebiete gehabt hat, in die anderen Gebiete herauftragen."
      ],
      [
        "Man bleibt ein «mathematischer Kopf», mehr als die, welche die Begriffe nicht metamorphosie- ren wollen ins Qualitative hinein.",
        "So kommt man dazu, für die höheren Gebiete des Naturdaseins das innere Anschauen ebenso gelten zu lassen, wie man das innere Anschauen gelten läßt für leblose mathematische Gebilde."
      ],
      [
        "Das ist das, was ich hier nur kurz skizzieren kann, was aber, wenn es weiter ausgebildet wird, zeigt, daß die wissenschaftliche Seite der Anthroposophie durchaus das kann, was Goethe nannte: Rechenschaft ablegen vor jedem, auch vor dem strengsten Mathematiker.",
        "Denn das wollte Goethe mit der Ausbildung seiner Idee von der Urpflanze, zu der er gekommen ist, und mit der Idee des Urtieres, wozu er nicht gekommen ist."
      ],
      [
        "Und das will Anthroposophie: Hervorgehen lassen aus der Goethe- schen Weltanschauung das, was diese in bezug auf die Erscheinungen der Natur konnte und vom Erfassen des Lebendigen in der Imagination aufsteigen zu dem Typus der Pflanze und zu dem Typus des Tieres.",
        "Ich habe schon in den 80er Jahren des vorigen Jahrhunderts ge- zeigt, daß wir für die organische Natur die aus dem Unorganischen genommenen Begriffe metamorphosie- ren müssen."
      ],
      [
        "Davon werde ich in den nächsten Tagen noch weiter zu sprechen haben.",
        "Dadurch kommt man aber dazu, in der Organik dasjenige zu sehen, was das eigentliche Wirkungsprinzip, Gestaltungsprinzip ist.",
        "Und 32 da möchte ich an den Schluß dieser Betrachtungen etwas hinstellen, was in den nächsten Tagen noch weitere Be- trachtung erfahren wird, und was zeigen soll, wie diese materialistische Phase naturwissenschaftlicher Entwick- lung von der Anthroposophie nicht unterschätzt wird."
      ],
      [
        "Die Anthroposophie muß in dieser materialistischen Phase der Naturwissenschaft ein wichtiges Übergangs- prinzip sehen, eine Erziehungsmethode, damit man ein- mal gelernt hat, sich rein der äußeren Sinnes-Empirie hinzugeben.",
        "Das war außerordentlich erzieherisch für die Entwicklung der Menschheit, und nur wenn man diese Erziehung genossen hat, kann man auch dazu kommen, gewisse Dinge mit voller Klarheit zu über- sehen."
      ],
      [
        "Denn wer nun, ausgerüstet mit solchem Wissen- schaftssinn die äußere materielle Welt betrachtet, der schaut, wie sich diese materielle Welt innerlich im Menschen «spiegelt», wenn ich mich dieses Ausdrucks bedienen darf.",
        "Die Welt, wie wir sie im Innern erleben, ist mehr oder weniger eine Abstraktion, ein von Empfindungen und Willensimpulsen durchzogenes inneres Bild dessen, was die äußere materielle Welt ist; so daß wir, wenn wir vom Verfolgen der materiellen Außenwelt zum Geistig-See- lischen übergehen, zu einem bloß Bildhaften kommen."
      ],
      [
        "Halten wir das ganz streng fest: außen die Summe der materiellen Erscheinungen, die wir im phänomenologi- schen Sinne anschauen im Innern das Seelisch-Geistige, mit einem gewissen abstrakten Charakter, mit einem Bildcharakter.",
        "Tritt man aber mit anthroposophischer Anschauung in die Betrachtung dessen ein, was der äußeren materiellen Welt geistig zugrunde liegt, in den Geist, der da wirkt in den Bewegungen der Sterne, in dem Werden der Mineralien, der Pflanzen und der Tiere, 33 tritt man ein in das Geistige des Werdens der Außenwelt, lernt man diese durch Imagination, Inspiration und In- tuition kennen, dann gibt uns auch das ein inneres Spiegelbild des Menschen."
      ],
      [
        "Aber was ist dieses innere Spiegelbild des Menschen?",
        "Das sind unsere materiellen Organe.",
        "Sie antworten mir jetzt auf das, was ich vorher kennengelernt habe als die Natur der Sonne, als die Natur des Mondes, der Mineralien, der Pflanzen, der Tiere und so weiter; darauf antworten mir die inneren Organe."
      ],
      [
        "Ich lerne das Eigene des menschlichen Orga- nismus nur kennen, wenn ich das Äußere der Welt kennenlerne.",
        "Die materielle Welt außen spiegelt sich innen geistig-seelisch; die geistig-seelische Welt außen spiegelt sich innen in den Formen von Lunge, Leber, Herz und so weiter."
      ],
      [
        "Die inneren Organe sind, wenn man sie anschaut, so in einem Verhältnis zur geistigen Außenwelt, wie unsere Gedanken und Empfindungen zur materiellen Außenwelt in einem Verhältnis sind.",
        "Das zeigt uns, wie die Anthroposophie durchaus nicht in einem schwärmerischen Sinne den Materialis- mus ablehnen will."
      ],
      [
        "Sehen Sie sich den ganzen Umfang der Naturwissenschaft an: Tausende werden unbefriedigt sein über das, was da aus der Naturwissenschaft mit den gewöhnlichen Methoden gewonnen wird.",
        "Die Anthro- posophie wird durch ihre Methoden gerade über das Materielle der Welt eine Anschauung gewinnen, die nicht unbefriedigt lassen wird."
      ],
      [
        "Sie anerkennt das Materielle in der eigenen inneren Organisation und in dem Phäno- menologischen der Umwelt; aber sie muß zu gleicher Zeit erkennen, daß diese innere Organisation ein Ergebnis, eine Konsequenz von kosmischem Geistig-Seelischen ist.",
        "Sie will daher auch das ergänzen, was in der Astro- nomie, in der Astrophysik, Physik oder Chemie nur 34 mathematisch geleistet wird."
      ],
      [
        "Das wird sie in einer orga- nischen Kosmologie und so weiter erkunden und da- durch auch zu einem Verständnis des materiellen Men- schen vordringen.",
        "Darin liegen dann die Grundlagen für dasjenige, was Anthroposophie für die Medizin, die Biologie und so weiter geben will."
      ],
      [
        "So glaube ich durch diese Andeutungen, die ich jetzt nur ganz skizzenhaft geben konnte, darauf hingedeutet zu haben, wie Anthroposophie, wenn man sie richtig erfaßt, nicht so angesehen werden kann, als ob sie von sich aus sich in einen Kampf stellen wolle gegen die gegenwärtige Wissenschaft; sondern die Dinge liegen so, daß die gegenwärtigen Vertreter der Wissenschaft noch nicht die Brücke zur Anthroposophie geschlagen haben, um zu sehen, wie die Anthroposophie streng wissenschaftlich auch gegenüber den Naturerscheinun- gen sein will. 35"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG DIE MENSCHLICHE UND DIE TIERISCHE ORGANISATION Berlin, 6. März 1922",
    "paragraphs": [
      "Sehr verehrte Anwesende! Bei diesem Vortrage bitte ich Sie zu berücksichtigen, daß ich bis gestern Abend anneh- men mußte, daß ich diesen Vortrag heute von Dr. Kolisko hören würde, und ihn nicht selber halten würde.",
      "Es war daher in dieser kurzen Zeit nicht möglich, das, was ich zu sagen haben werde, irgendwie zurechtzulegen, und ich kann auch nur hoffen, im großen und ganzen un- gefähr dasjenige in den Einzelheiten zu treffen, was Dr. Koslisko heute zu Ihnen hat sagen wollen.",
      "Wenn von anthroposophischen Gesichtspunkten aus über das Verhältnis der tierischen Welt zur menschli- chen Welt gesprochen wird, so darf besonders darauf aufmerksam gemacht werden, wie die gegenwärtigen an- throposophischen Ideen geschichtlich doch zusammen- hängen mit demjenigen, was sich aus der Goetheschen Weltanschauung - ich habe das jetzt hier schon zweimal gesagt - ergibt. Und für das Thema, das jetzt in Frage steht, kommt insbesondere eine der allerersten Leistun- gen Goethes auf naturwissenschaftlichem Gebiete in Betracht, nämlich seine Abhandlung, die den Titel trägt: «Dem Menschen wie den Tieren ist ein Zwischenkiefer- knochen in der obern Kinnlade zuzuschreiben».",
      "Man muß nun alle die Verhältnisse sich vor Augen führen, 36 aus denen heraus Goethe dazu gekommen ist, diese Abhandlung aufgrund eingehender anatomischer und physiologischer Studien, auch aufgrund von Ansätzen zu embryologischen Studien, die er gemacht hat, zu schreiben. In der Zeit, als Goethe sich, schon als junger Student und später als der Freund der ja in einer gewissen Weise von ihm abhängigen Jenaischen Universitätsinstitute, in diejenigen Probleme hineinlebte, in die er durch alles das hineingestellt war, und namentlich in das Problem, welches der eigentliche Unterschied des Menschen gegenüber dem Tiere sei, da sah er überall um sich herum, wie man bemüht war, irgendetwas in der Gestaltung, in der Morphologie des Menschen und der Tiere zu finden, das auf einen strengen Unterschied hinwies zwischen dem Menschen, der gewissermaßen die Krone der Schöpfung sein soll, und der Tierwelt.",
      "Und an dem Umstände, daß sich der sogenannte Zwischenkieferknochen, der sonst bei den Tieren über- all von den anderen Kieferknochen deutlich abgetrennt ist, sich ja beim Menschen nicht als abgesonderter Knochen findet, an diesem Umstände glaubte man, gerade in einem Teil der Kopfesbildung einen solchen durchgreifenden Unterschied zwischen Mensch und Tier zu finden. Goethe ging das nicht ein.",
      "Er war der Ansicht, da Mensch und Tier m bezug auf ihre ganze Organisation analog gebildet sind, so dürfe in einer solchen Einzelheit sich nicht eine Differenzierung zei- gen. Und da allerdings der Zwischenkieferknochen beim erwachsenen Menschen mit den anderen Kiefer- knochen verwachsen ist, so suchte Goethe zu zeigen, wie das eben nur auf einer späteren Verwachsung beruht, und daß der Mensch in seinen embryonalen 37 Verhältnissen den oberen Zwischenkieferknochen auch hat, wie die Tiere.",
      "Man muß nur einmal verfolgen, mit welchem En- thusiasmus Goethe darauf hinweist, daß es ihm gelungen ist zu zeigen, wie der Mensch tatsächlich den Zwi- schenkieferknochen mit den Tieren gemeinsam hat, um eben aus dem großen und ganzen heraus zu zeigen, daß aus dem Bau, aus der Morphologie des Menschen und der Tiere ein so durchgreifender Unterschied zwischen beiden im einzelnen nicht zu finden sei. Also von einer solchen Abgrenzung des Menschen von den Tieren in der Weise, wie es im 18.",
      "Jahrhundert überall sich fand, kann für Goethe nicht die Rede sein - kann auch für die Anthroposophie nicht die Rede sein. Was schon Goethe annahm, ist dies: Indem die tierische Organisation zur menschlichen heraufsteigt, werden die einzelnen, schon im Tiere liegenden Organformen umgebildet und dann gewissermaßen durch ihre Umbildung in die Möglichkeit versetzt, nun Platz zu haben für das, was sich vom Innern des Menschen her, aus dem ganzen Menschen heraus in der also umgebildeten tierischen Organisation offenbaren kann.",
      "Nur an eine Metamorphose der tie- rischen Organisation ins Menschliche herauf dachte Goethe, nicht an eine selbständig abgegliederte mensch- liche Morphologie. Dies, möchte ich sagen, muß man als Grundlage voraussetzen, wenn nun auch im anthroposophischen Sinne aufgesucht wird die Differenzierung zwischen dem tierischen und dem menschlichen Organismus.",
      "Wenn die Organisation selbst, in ihren Formen, nur auf einer Metamorphose des Tierischen und des Menschlichen beruht, dann muß man, wenn man die Differenzie- rung aufsuchen will, vor allem darauf sehen, wie das 38 Leben beim Menschen und wie es beim Tiere verläuft, man muß gewissermaßen darauf sehen, wie aus dem Menschlichen heraus das Funktionieren mit den Orga- nen sich gestaltet, und wie aus dem Tierischen heraus das Funktionieren mit den Organen sich gestaltet. Kurz, man muß den Unterschied mehr auf einem biologischen, als auf einem morphologischen Gebiete suchen.",
      "Nun kann man von einer gewissen Seite her der Auffassung von einem biologischen Unterschied ganz besonders die Wege bereiten, indem man von demjeni- gen ausgeht, was einem als die Grundlage des tierischen Funktionierens erscheinen muß, und das ist sowohl bei den Menschen wie bei den Tieren das, was mit den Sinnesorganen zusammenhängt. Die Sinnesorgane oder besser gesagt, die Funktionen der Sinnesorgane, leben ja mehr oder weniger in allem, was sich im tierischen und menschlichen Organismus abspielt.",
      "Wir müssen schon bei den niederen Tieren annehmen, daß sich bei den einfachen Ernährungsprozessen, in den reinen Stoff- wechselvorgängen, ein gewisses Funktionieren primi- tiver Sinne abspielt, daß also, sagen wir, Geschmacks- erlebnisse zum Beispiel parallel gehen dem, was mehr oder weniger rein chemisch der Stoffwechsel ist. Diese Dinge differenzieren sich immer mehr und mehr, je weiter man in der Tierreihe heraufkommt, bis zum Menschen hin.",
      "Aber wir werden durchaus nirgends, wenn wir unbefangen auf die tierische Organisation eingehen, etwas finden, worinnen nicht ein Sinnesleben vorhanden ist. Gewiß, man kann sagen: Was hat schließlich dieses Sinnesleben zum Beispiel mit der Lymphebildung oder mit der Blutbildung und so weiter zu tun?",
      "Nun ist man heute auch schon in der nicht von An- throposophie beeinflußten Wissenschaft dazu gekom- 39 men, von unterbewußten Vorgängen der menschlichen Psyche zu sprechen, und es wird deshalb, auch wenn es der Kürze der Zeit halber nur angedeutet werden kann, nicht als etwas ganz Unberechtigtes erscheinen, wenn ich sage: Was sich in Mund und Gaumen als das Ge- schmackserlebnis abspielt, was als das Geschmackserleb- nis auftritt unter dem Wirken und der Funktion zum Beispiel des Ptyalins, des Pepsins und so weiter, wie sollte das nicht auch ins Unbewußte hineinspielen? Warum sollte - ich sage es als eine Art von Postulat - das Ge- schmackserlebnis sich nicht fortsetzen durch den ganzen Organismus, und warum sollten nicht unbewußt Ge- schmackserlebnisse parallel gehen der Lymphe- und Blutbildung und allen Organprozessen?",
      "Wir werden da- her die menschliche und die tierische Organisation von ihrer biologischen Seite her sehr wohl verfolgen können, wenn wir einmal das Sinnesleben betrachten. Dieses Sinnesleben verläuft nun - wie ich für einige von Ihnen seit Jahren angedeutet habe, wie es zum Teil durchaus schon eine Sache der äußeren Wissenschaft ist - nicht nur in den gewöhnlich angeführten fünf Sinnen, sondern in einer deutlich unterscheidbaren Anzahl von zwölf menschlichen Sinnen.",
      "Dabei muß man aber bloß vom Menschen sprechen. Für den, der einsehen will, daß es ebenso berechtigt ist, von zwölf Sinnen zu sprechen, wie von fünf oder sechs vom Sehen, Hören, Riechen, Schmecken, Fühlen oder Tasten -, für den ist es berechtigt, davon zu sprechen, daß wir zum Beispiel einen Gleich- gewichtssinn haben, der uns innerlich erkennen läßt, ob wir auf beiden Füßen stehen oder nur auf einem, ob wir mit unsern Armen die eine oder die andere Bewegung ausführen und so weiter.",
      "Indem wir uns als Mensch in die Welt hineinstellen, sind wir in einer Gleichge- 40 wichtslage. Diese Gleichgewichtslage nehmen wir also, wenn auch viel dumpfer, sinnlich wahr, wie wir dasjenige sinnlich wahrnehmen, was im Sehvorgang sich abspielt; so daß wir von einem Gleichgewichtssinn sprechen kön- nen, wie wir von einem Sehsinn sprechen können.",
      "Wir müssen uns nur darüber klar sein: Wenn wir von diesem Gleichgewichtssinn sprechen, so wenden wir uns mehr der eigenen Organisation zu; wir schauen gewissermaßen nach innen, während wir mit den Augen nach außen schauen. Aber es hegt diesem Erleben im Gleichge- wichtssinn durchaus eine sinnliche Funktion zugrunde.",
      "Ebenso können wir nach einer anderen Seite hin die Anzahl der Sinne ergänzen. Wenn wir bloß hören, so ist das Funktionieren des menschlichen Organismus etwas wesentlich anderes, als wenn wir zwar durch das Ohr direkt hören, aber dann auf das eingehen, was indirekt in der Sprache uns wahrnehmbar wird.",
      "Wenn wir mit in- nerem Verständnis die Worte, die Sätze des anderen verfolgen, haben wir es nicht bloß zu tun mit einem Urteilen, sondern dem Urteilsprozeß geht auch da vor- aus ein Wahrnehmungsprozeß, ein Sinnesprozeß; also wir müssen davon sprechen, daß wir einen Sprachsinn - oder eigentlich einen Sprachesinn, einen Wortesinn - haben, wie wir einen Gehörsinn haben. Mit anderen Worten: Wir müssen, wenn wir die Worte mehr anato- misch-physiologisch betrachten, innerhalb der mensch- lichen Organisation eine spezielle [Sinnes] organisation voraussetzen, welche dem Anhören des Gesprochenen ebenso entspricht, wie die Gehörorganisation dem An- hören der unartikulierten Töne.",
      "Und wir müssen eine Spezialorganisation voraussetzen für den Sprachsinn, die ganz ähnlich ist einer sonstigen Sinnesorganisation, zum Beispiel der Sehorganisation oder der Hörorganisation. 41 Wir dürfen auch, wenn wir unbefangen zu Werke gehen, nicht sagen: Wir lernen erkennen, daß ein anderer Mensch vor uns steht, wenn wir sehen, daß an dieser äußeren Raumesform etwas wie eine Nase ist, wie zwei Augen und so weiter, und nun durch Analogie schließen, daß darin ein Mensch steckt, weil wir sehen, daß in uns selber ein Mensch steckt, der sich äußerlich offenbart durch Nase, Augen und so weiter. Ein solcher unbewuß- ter Schluß liegt in Wirklichkeit nicht zugrunde, aber es liegt ein unmittelbares Eingehen auf den anderen Men- schen zugrunde, dem etwas Spezielles in der Organisa- tion des Menschen entsprechen muß, das nur zu paral- lelisieren ist mit einer Sinnesorganisation, so daß wir auch von einem Ichsinn sprechen können.",
      "Wenn wir in dieser Weise das Funktionieren des Menschen ganz un- befangen durchschauen, müssen wir mit derselben Be- rechtigung, mit der wir von einer Gehör-, Geschmack- und so weiter -Organisation sprechen, auch sprechen von einer Wahrnehmungsorganisation für Worte, von einer Wahrnehmungsorganisation für Gedanken, von einer Wahrnehmungsorganisation für das Ich - nicht für das eigene Ich, denn das beruht auf etwas ganz anderem. Und wir müssen weiter sprechen von einem Bewe- gungssinn, denn ob wir uns bewegen oder ob wir in Ruhe sind, das ist etwas ganz anderes.",
      "Ebenso müssen wir dann sprechen von einem Lebenssinn - die ge- wöhnliche Wissenschaft spricht zum Teil schon davon. Wenn wir so die Zahl der Sinnesorganisationen fest- stellen, kommen wir auf zwölf menschliche Sinne.",
      "Von diesen sind eine Anzahl allerdings innere Sinne; denn wir nehmen den inneren Organismus - wie wir uns fühlen und wie es uns geht im Gleichgewichtssinn, im Bewe- gungssinn und so weiter - ebenfalls wahr. Aber qualitativ 42 ist das Erlebnis beim Wahrnehmen der inneren Organi- sation durchaus das gleiche wie beim Seh-, Hör- oder Geschmackvorgang.",
      "Es handelt sich nur darum, die Dinge im richtigen Zusammenhang zu sehen. Wenn man in dieser Weise in bezug auf den Men- schen von einer vollständigen Sinnesphysiologie ausgeht, werden gewisse biologische Erscheinungen auf der einen Seite im Reiche des Menschen, auf der anderen Seite im Reiche der Tiere von einer ganz besonderen Bedeutung [sichtbar], von einer Bedeutung, die bestehen kann, auch wenn man alles dasjenige restlos zugibt, was von neueren Naturforschern, selbst von Haeckel, vorgebracht worden ist für den morphologischen und auch physiologischen Zusammenhang der menschlichen Organisation mit der tierischen.",
      "Hier walten ja allerdings die unmöglich- sten Mißverständnisse. Man glaubt zum Beispiel, die Anthroposophie müsse sich in Gegensatz stellen zum Haeckelismus, einfach aus dem Grunde, weil sie von der bloßen Betrachtung der Sinneswahrnehmungen zur em- pirischen Betrachtung des Geistigen aufsteigt; man glaubt, Anthroposophie müsse aus diesen Untergründen heraus etwas am Haeckelismus verändern.",
      "Nein! - Was am Haeckelismus verändert werden muß, das muß aus na- turwissenschaftlicher Methodik heraus verändert wer- den, da braucht Anthroposophie nicht mitzureden, da kann man auch als Naturforscher mit Haeckel disku- tieren. Was Anthroposophie zu sagen hat, das liegt auf einem ganz anderen Gebiete.",
      "Mit Recht kann betont werden: Zählt man die Knochen der höheren Tiere, so unter- scheidet sich die Anzahl der Knochen nicht von der beim Menschen. Und ebenso ist es mit den Muskeln. So kommen wir nicht zu einer Differenzierung der mensch- 43 liehen und der tierischen Organisation.",
      "Aber wenn wir biologisch vorgehen, kommen wir zu einer wirklichen Differenzierung. Wir kommen dann dazu, einen beson- deren Wert darauf zu legen, daß sich im wesentlichen die menschliche Organisation in einer anderen Art in den Kosmos hineinstellt als die tierische.",
      "Wenn wir gerade die höheren Tiere betrachten, müssen wir sagen: Ein Wesentliches bei ihnen ist es, daß die Achse ihres Rückgrats parallel zur Erdoberfläche geht, während im Gegensatz dazu beim Menschen im Verlaufe seines Le- bens die horizontale Lage der Rückgratachse in eine vertikale verwandelt wird, so daß also eine wichtige Lebensfunktion beim Menschen darin besteht, sich auf- zurichten. - Ich weiß, es kann nun natürlich eingewen- det werden: Es gibt doch aber auch Tiere mit mehr oder weniger aufrechter, vertikaler Rückgratachse. - Darauf kommt es aber nicht an, wie es sich gegenüber einer äußeren Morphologie ausnimmt, sondern darauf, wie die ganze Organisation veranlagt ist. Wir werden auch sehen, wie bei gewissen Tieren, Vogelarten oder auch Säuge- tierarten, bei denen mehr oder weniger die Rückgratachse in eine vertikale Lage gebracht werden kann, gerade gegenüber ihrer ganzen Veranlagung eine Art Degene- rierung auftritt, während es beim Menschen schon in der Veranlagung liegt, daß die Rückgratachse eine Vertikal- lage hat.",
      "Als ich dies einmal vor vielen Jahren bei einem Vor- trage in München sagte, kam ein naturwissenschaftlich gebildeter Mann zu mir, den ich natürlich ganz gut verstehen konnte, und sagte: Wenn wir schlafen, haben wir aber doch auch die Rückgratachse horizontal. - Darauf aber kommt es nicht an, sagte ich ihm, sondern darauf, wie im Verhältnis zu der Lage, sagen wir, der 44 Bein- oder Fußknochen zum ganzen übrigen Körperbau die Rückgratachse im ganzen kosmischen Zusammenhang des Menschen gestellt ist, und wie sich das beim Men- schen oder beim Tier auswirkt. Der Mensch hat zwar beim Schlafen sein Rückgrat horizontal, aber diese hori- zontale Lage ist äußerlich; innerlich dynamisch ist der Mensch so organisiert, daß er sich in seinen Gleich- gewichtszustand bringen kann, wo die Rückgratachse vertikal ist.",
      "Und wenn sich Tiere in einen solchen Gleichgewichtszustand bringen, so degenerieren sie in gewisser Beziehung, oder sie bringen es dahin, gewisse menschenähnliche Funktionen zu entwickeln und da- durch auch das zu beweisen, was ich nun ausführen will. Wir können sagen: Indem der Mensch rein funktio- neil aus der gesamten Dynamik seines Wesens heraus im Laufe seiner ersten Lebensjahre seine Rückgratachse vertikal gestaltet, bringt er sich im Kosmos in eine andere Gleichgewichtslage als das Tier.",
      "Aber jedes Wesen ist ja aus dem Gesamtkosmos heraus gebildet; man könnte auch sagen, es paßt sich ihm an - ich will jetzt darauf nicht weiter eingehen. Wenn wir die Gestaltung der einzelnen Knochen, zum Beispiel der Rippen- oder Kopfknochen und so weiter verfolgen, dann werden wir auch morphologisch die Möglichkeit gewinnen, in den Formen der Rippen- oder der Kopfknochen eines Menschen oder eines Hundes die Anpassung zu finden an die Vertikallage oder Horizontallage des Rückgrats.",
      "Indem sich der Mensch in die vertikale Lage hineinfin- det, lebt er gegenüber dem Tier, das auf seinen vier Bei- nen steht, in einer ganz anderen Gleichgewichtslage; er lebt in einem ganz anderen kosmischen Zusammenhang. Nun versuchen wir, das Problem von einer anderen Seite her anzufassen und uns klarzumachen, was eigent- 45 lich im Menschen beim Sinnesvorgang und was in An- lehnung an den Sinnesvorgang bei ihm vorgeht.",
      "Ich werde dabei wegen der Kürze der Zeit genötigt sein, nur andeutend zu sprechen, aber es könnte das auch in eine ganz exakte biologisch-physiologische Terminologie um- gesetzt werden. Nehmen wir den Sehvorgang.",
      "Wir können ihn gliedern in das, was spezifische Funktion des Sehorgans ist, und in das, was sich dann abspielt in der weiteren Fortsetzung in das Physische hinein, ich möchte sagen, in Analogie dazu, daß der Sehnerv vom Auge ausgeht und sich dann im Innern der Nervenorganisation verliert. Wir können also unterscheiden: einmal den Sehvorgang selbst, und dann alles, was sich daranschließt im Gesamterleben.",
      "In dem unmittelbar präsenten Sehvorgang ist noch das Vorstellungsmäßige immanent; indem wir irgend etwas anschauen, trennen wir noch nicht das Vorstellungs- mäßige von dem Sehvorgang. Wenden wir das Auge ab von dem, was wir anschauen, so behalten wir einen vor- stellungsmäßigen Rest zurück, der deutlich seine Ver- wandtschaft mit dem beim Sehvorgang Wahrgenomme- nen zeigt.",
      "Wer das richtig analysieren kann, sieht, wie verschieden gerade das ist, was sich als Vorstellungsrest ergibt aus dem Sehvorgang, gegenüber dem, was sich ergibt aus einem Hörvorgang. Wir haben also in uns das Erlebnis des Sehvorganges, ich möchte sagen, in dua- listischer Weise: zuerst mehr hingewendet zu dem, was die eigentliche Sinneswahrnehmung ist, und dann hin- gewendet zu dem, was uns als vorstellungsmäßiger Rest, als mehr oder weniger ausgestaltete Erinnerung bleibt.",
      "Nun nehmen Sie einmal alles das, was im Menschen lebt an innerem Vorstellungsmäßigen, das sich anlehnt an die fünf Sinne. Das meiste im menschlichen Seelen- 46 leben lehnt sich ja an an die Sehvorgänge; nur ein Neuntel etwa von dem, was durch die Sehvorgänge gegeben ist, ist durch die Hörvorgänge gegeben.",
      "Und wenn wir das innere Seelenleben betrachten, so ist dadurch noch we- niger gegeben als durch die Seh- und Hörvorgänge und so weiter. Wir wissen, daß dabei das Vorstellungmäßige, das ja zur bleibenden Erinnerung führt, auch eine Rolle spielt, aber eine wesentlich geringere als beim Seh- und Hörvorgang.",
      "Nun können wir die Frage aufwerfen: Gibt es für die mehr verborgenen Sinne, zum Beispiel für den Gleich- gewichtssinn oder für den Bewegungssinn auch diese Dualität, wie wir sie finden beim Sehsinn in dem Wahr- nehmungsmäßigen und dem Vorstellungsmäßigen? Bei einer wirklich unbefangenen Physiologie und Psycho- logie gibt es dies auch zum Beispiel für den Gleich- gewichtssinn, nur wird gewöhnlich der Zusammenhang nicht bemerkt.",
      "In dem Vortrage, den ich eben gehalten habe, habe ich von dem Mathematischen gesprochen, von dem Sichzurechtfinden in den Raumesverhältnissen, wo das Mathematische geometrisch angewandt wird. Wir konstruieren uns Raumesverhältnisse.",
      "Was ist das eigentlich, was wir da tun? Es ist in bezug auf den ganzen Menschen genau dasselbe wie das, was wir tun, wenn wir beim Sehvorgang die Wahrnehmung deutlich absondern von dem Vorstellungsmäßigen, indem wir die Vorstellung innerlich behalten. [Wir nehmen eine Farbe nicht nur äußerlich wahr], sondern wir erleben das Qualitative der Farbe, des Farbtones, und es lebt sogar das Gefühl, das ich als Gefühl habe bei einer warmen oder kalten Farbe, im Innern fort.",
      "Wir können uns nun folgendes sagen: Ich will einmal in einer umfassenden Seelenschau alle diejenigen Vor- 47 Stellungen überschauen, die ich im Leben dadurch ge- wonnen habe, daß ich durch meine Augen sehen kann. Wir würden ein inneres visuelles System in der Seele bekommen.",
      "Wir würden, ohne daß wir jetzt äußere Sehvorgänge haben, innerlich aufsteigen haben eine Art Nachkonstruktion der Sehvorgänge. Und wenn Sie dies in ebensolcher Weise in bezug auf den Gleichgewichts- sinn berücksichtigen, dann kommen Sie darauf, daß Sie durch alles das, was Sie durch den Gleichgewichtssinn im eigenen Organismus erleben, etwas im Innern herauf- steigen haben, das dem Geometrischen in der äußeren Welt [entspricht].* Mathematik oder Mechanik haben wir nicht [aus der äußeren Erfahrung] gewonnen.",
      "Ma- thematische und mechanische [Gesetze] sind durch inne- res [Konstruieren gewonnen]. Wenn Sie sich mechani- sche [Gesetze] vergegenwärtigen, so haben Sie sie [ge- wonnen] durch das Vorstellungsmäßige Ihres Gleichge- wichtssinnes.",
      "Der ganze Mensch wird da zum Sinnesorgan und er bildet dabei [innerlich] gleichsam den anderen Pol [zu dem Wahrgenommenen] aus. Wir bilden zum Beispiel die Mathematik aus und glauben, wir haben in ihr eine reine a-priori-Wissenschaft.",
      "Aber die Mathematik ist keine reine a-priori-Wissenschaft. Wir merken nur nicht, daß wir dasjenige, was wir im Gleichgewichtssinn erle- ben, ebenso [in mathematisch-geometrische Vorstellun- gen] umsetzen, wie die Sehwahrnehmung sich in die Sehvorstellungen umsetzt.",
      "Ohne daß wir die Brücke *Die nachfolgenden Ausführungen sind vom Stenographen nur lük- kenhaft festgehalten. Die vom Herausgeber vorgenommenen not- wendigen Ergänzungen - gekennzeichnet durch eckige Klammern - stützen sich im wesentlichen auf folgende Vorträge Rudolf Steiners: 16.",
      "März 1921, in GA 324; 29. September, 1. und 3. Oktober 1920, in GA 322. 48 bemerken, wird das [durch den Gleichgewichtssinn Wahrgenommene] zu Mathematik oder zu Mechanik. Wenn Sie das bedenken, werden Sie den innigen Zu- sammenhang des menschlichen Gesamtorganismus mit seiner Gleichgewichtslage im Kosmos verstehen.",
      "Dann werden Sie sich sagen: Beim Tier, das auf seinen vier Bei- nen steht und dem durch seine Gleichgewichtslage auch der Inhalt seines Gleichgewichtssinnes gegeben ist, muß ja das Erleben des Gleichgewichts sich in einer ganz ande- ren Weise innerlich spiegeln als beim Menschen im Ma- thematischen. Wir finden das Mathematische einfach als ein Ergebnis unseres Hineingestelltseins in denKosmos.",
      "Wir reden von drei Dimensionen, weil wir nach drei Dimensionen in den Kosmos hineingestellt sind. Aber die vertikale Dimension haben wir uns selbst erst im Laufe unseres Lebens errungen. Wir haben uns in die vertikale Dimension erst hineingestellt.",
      "Was wir so in frühester Kindheit erleben, das spiegelt sich uns später in der Mathematik; es geht das nur nicht so schnell wie beim Sehvorgang. Die Spiegelung des Gleichgewicht- Erlebens geht im Laufe des Lebens vor sich.",
      "Wir haben in der Kindheit sehr stark das Erleben des Gleichge- wichtssinnes, wenn wir vom Kriechen übergehen zum Gehen und Stehen. Das spiegelt sich uns im späteren Lebensalter und wird als Mathematik und Mechanik sichtbar.",
      "Wir halten oft die Mathematik für etwas aus uns selbst Gesponnenes. Das ist sie nicht. Sie geht aus der Wahrnehmung des eigenen Organismus hervor. Warum sind denn gewisse Gedanken beim Menschen so, daß er sie auf den Kosmos beziehen kann, daß er sich aus den Gedanken ein ganzes Gedankengebäude bilden kann?",
      "Das ist nur das Ergebnis dessen, wie der Mensch im Kosmos drinnensteht. Und wenn wir nun die Gleich- 49 gewichtslage, in der sich das Tier befindet [in seinem Verhältnis zum Kosmos], vergleichen mit der Gleich- gewichtslage des Menschen, so können wir sagen: Wir haben beim Tier das Gebundensein an die Erdenorgani- sation und wir haben beim Menschen das Aufgerich- tetsein, das Herausgehobensein aus der Erdenorgani- sation.",
      "Was wir als selbständige Gedanken aussprechen, rührt davon her, daß wir uns für unsere menschliche Organisation auch eine selbständige Gleichgewichtslage erringen. Es ist also der Akt des Sichhineinstellens in den Kosmos nicht etwas, was aus dem Organismus selbst hervorgeht und sich auch beim Tier findet, sondern etwas, was in diesen menschlichen Organismus selbst sich hineinbildet und was erst im Laufe der [ersten] Leben[sjahre] errungen wird, bis in die Organe hinein.",
      "Dadurch kommen wir zu jener Polarität des Menschen [gegenüber dem Tier], daß auf der einen Seite der Mensch aufrechtsteht und einen aufrechten Gang hat, und daß dieser ganzen kosmischen Position, in der der Mensch lebt, nun eben alles das angepaßt wird, was sich im einzelnen bei Mensch und Tier nicht unterscheidet. Und auf der anderen Seite erscheint im Seelischen dasjenige als Gedanken, was jetzt über das sinnlich Angeschaute, über das mit den fünf Sinnen Wahrgenommene hinaus- geht, was sich davon losmacht.",
      "So wie sich der Mensch durch seine Stellung zum Kosmos losmacht von der Erde, ebenso machen sich die Gedanken des Menschen los von ihrer Gebundenheit an die Sinneswelt, sie werden in einer gewissen Beziehung frei. Wir müssen - für die Anthroposophie ist das wieder- um eine Sicherheit, hier möchte ich es zunächst mehr als Postulat hinstellen - wir müssen darin, daß der Mensch 50 diese durch die aufrechte Stellung seiner Rückgratachse bedingte Gleichgewichtslage hat, etwas sehen, was den Menschen trennt von dem Tiere; und auf der anderen Seite müssen wir die besondere Form der Vorstellungs- welt, der Gedanken, als das spezifisch Menschliche an- sehen.",
      "Aber gerade der, der solche Dinge vom anthro- posophischen Standpunkte aus durchschaut das wird mehr oder weniger noch zur Sprache kommen kön- nen -, der sieht, wie der Mensch durch die besondere Ausbildung seines Gleichgewichtssinnes und seines Be- wegungssinnes auch mehr zu einem freien Gedankensy- stem kommt, als das [bei dem Erleben durch] Augen und Ohren der Fall ist, und der wird auch einsehen, daß der Mensch nun dafür auch eine innere Organisation haben muß. Der Mensch hat einfach eine Organisation in sich, die beim Tier noch nicht zu finden ist - das kann durchaus auch einmal materiell nachgewiesen werden -, die einfach derjenigen Form der Gedanken dient, die sich losgeris- sen hat von der [Gebundenheit an die Erde] wie beim Tier, und die durch die besondere Gleichgewichtslage beim Menschen bedingt ist.",
      "Wir können also sagen: Indem der Mensch sich aufrichtet, schafft er sich ein Organ für die abstrakten Gedanken. Und so haben wir beim Menschen die durch seine aufrechte Lage bedingte Organisation, die zunächst nichts anderes zeigt, als daß die Organe, die beim Tier auch da sind, eine andere Lage haben; aber durch diese aufrechte Lage wird in der Nerven- und Blutorganisation bewirkt, daß unter dem Einfluß dieser anderen Gleichgewichtslage im Menschen etwas auftritt, was das Tier nicht haben kann.",
      "Da finden wir das, was den Menschen biologisch vom Tier unterscheidet. Wir finden diesen Zusammen- hang wirklich in der physischen Organisation des Men- 51 sehen und nicht in einem bloßen Dynamismus. Das ist von fundamentaler Bedeutung.",
      "Stellen Sie sich nur ein- mal die Umbildung der Organisation vor, die geschieht durch die Veränderung der Gleichgewichtslage, wie sie beim Tier ist, in die Gleichgewichtslage des Menschen, was sich da ändert zum Beispiel in bezug auf die Ober- und Unterschenkel, die Hände und so weiter. [Stellen Sie sich einmal vor, was es bedeutet], daß der Mensch ein Zweihänder ist und kein Vierfüßler. Der Mensch ist zwar mit denselben Formen ausgestattet wie das Tier, aber er hat sie in einer anderen Lage und dadurch in veränderten, metamorphosierten Formen.",
      "Das wird auch einmal anatomisch nachgewiesen werden können, wenn die notwendigen Werkzeuge und Experimentiermetho- den ausgebildet sein werden. Wir suchen nach solchen Werkzeugen und Experimentiermethoden in unseren Instituten in Stuttgart.",
      "Man muß allerdings, um diese Methoden auch äußerlich empirisch zu finden, zuerst durch imaginatives Anschauen darauf gekommen sein, [wo die Unterschiede hegen]. Daher ist die Anthroposo- phie in bezug auf [die Erforschung] der feineren Gebiete der Menschen-, Tier- und Pflanzenformen der Wissen- schaft durchaus nicht unnütz, denn die Wissenschaft kann die Dinge nicht durch Imagination finden.",
      "Sind sie aber gefunden, dann können sie auch [durch die Wis- senschaft] verifiziert werden. Wenn man darauf schaut, wie eine andere Gleichge- wichtslage die Organe umbildet, so findet man auch, daß bestimmte Organe so umgeändert werden, daß sie zum menschlichen Sprachorgan werden, daß der Organismus sprachschöpferisch wird.",
      "Damit haben Sie nun eine Einsicht gewonnen in die besondere Organisation des Menschen, die einfach da- 52 durch entsteht, daß er ein aufrechtgehendes Wesen ist, was sogar bis ins Materielle hinein Folgen hat. Auch in bezug auf den physiologischen Sprachorganismus haben Sie etwas gegeben auch wo man einen äußeren mor- phologischen Unterschied zwischen Mensch und Tier nicht festsetzen kann -, was doch eine Differenzierung zwischen Mensch und Tier in biologischer Beziehung zeigt.",
      "Dies sind einige Anregungen, die den Weg angeben können, wie das, was in einer äußeren, laienhaften Weise gesucht wird, auch auf einem wirklich wissenschaftli- chen Wege untersucht werden kann. Ich konnte das, was ich sagen wollte, hier nur skizzieren.",
      "Aber denken Sie sich [diese Gedanken] weiter fortgesetzt, so ergibt sich für die Wissenschaft tatsächlich ein Weg, um die Unter- schiede zwischen der tierischen und der menschlichen Organisation in biologischer Beziehung zu [erforschen]. 53"
    ],
    "sentences": [
      [
        "Sehr verehrte Anwesende!",
        "Bei diesem Vortrage bitte ich Sie zu berücksichtigen, daß ich bis gestern Abend anneh- men mußte, daß ich diesen Vortrag heute von Dr.",
        "Kolisko hören würde, und ihn nicht selber halten würde."
      ],
      [
        "Es war daher in dieser kurzen Zeit nicht möglich, das, was ich zu sagen haben werde, irgendwie zurechtzulegen, und ich kann auch nur hoffen, im großen und ganzen un- gefähr dasjenige in den Einzelheiten zu treffen, was Dr.",
        "Koslisko heute zu Ihnen hat sagen wollen."
      ],
      [
        "Wenn von anthroposophischen Gesichtspunkten aus über das Verhältnis der tierischen Welt zur menschli- chen Welt gesprochen wird, so darf besonders darauf aufmerksam gemacht werden, wie die gegenwärtigen an- throposophischen Ideen geschichtlich doch zusammen- hängen mit demjenigen, was sich aus der Goetheschen Weltanschauung - ich habe das jetzt hier schon zweimal gesagt - ergibt.",
        "Und für das Thema, das jetzt in Frage steht, kommt insbesondere eine der allerersten Leistun- gen Goethes auf naturwissenschaftlichem Gebiete in Betracht, nämlich seine Abhandlung, die den Titel trägt: «Dem Menschen wie den Tieren ist ein Zwischenkiefer- knochen in der obern Kinnlade zuzuschreiben»."
      ],
      [
        "Man muß nun alle die Verhältnisse sich vor Augen führen, 36 aus denen heraus Goethe dazu gekommen ist, diese Abhandlung aufgrund eingehender anatomischer und physiologischer Studien, auch aufgrund von Ansätzen zu embryologischen Studien, die er gemacht hat, zu schreiben.",
        "In der Zeit, als Goethe sich, schon als junger Student und später als der Freund der ja in einer gewissen Weise von ihm abhängigen Jenaischen Universitätsinstitute, in diejenigen Probleme hineinlebte, in die er durch alles das hineingestellt war, und namentlich in das Problem, welches der eigentliche Unterschied des Menschen gegenüber dem Tiere sei, da sah er überall um sich herum, wie man bemüht war, irgendetwas in der Gestaltung, in der Morphologie des Menschen und der Tiere zu finden, das auf einen strengen Unterschied hinwies zwischen dem Menschen, der gewissermaßen die Krone der Schöpfung sein soll, und der Tierwelt."
      ],
      [
        "Und an dem Umstände, daß sich der sogenannte Zwischenkieferknochen, der sonst bei den Tieren über- all von den anderen Kieferknochen deutlich abgetrennt ist, sich ja beim Menschen nicht als abgesonderter Knochen findet, an diesem Umstände glaubte man, gerade in einem Teil der Kopfesbildung einen solchen durchgreifenden Unterschied zwischen Mensch und Tier zu finden.",
        "Goethe ging das nicht ein."
      ],
      [
        "Er war der Ansicht, da Mensch und Tier m bezug auf ihre ganze Organisation analog gebildet sind, so dürfe in einer solchen Einzelheit sich nicht eine Differenzierung zei- gen.",
        "Und da allerdings der Zwischenkieferknochen beim erwachsenen Menschen mit den anderen Kiefer- knochen verwachsen ist, so suchte Goethe zu zeigen, wie das eben nur auf einer späteren Verwachsung beruht, und daß der Mensch in seinen embryonalen 37 Verhältnissen den oberen Zwischenkieferknochen auch hat, wie die Tiere."
      ],
      [
        "Man muß nur einmal verfolgen, mit welchem En- thusiasmus Goethe darauf hinweist, daß es ihm gelungen ist zu zeigen, wie der Mensch tatsächlich den Zwi- schenkieferknochen mit den Tieren gemeinsam hat, um eben aus dem großen und ganzen heraus zu zeigen, daß aus dem Bau, aus der Morphologie des Menschen und der Tiere ein so durchgreifender Unterschied zwischen beiden im einzelnen nicht zu finden sei.",
        "Also von einer solchen Abgrenzung des Menschen von den Tieren in der Weise, wie es im 18."
      ],
      [
        "Jahrhundert überall sich fand, kann für Goethe nicht die Rede sein - kann auch für die Anthroposophie nicht die Rede sein.",
        "Was schon Goethe annahm, ist dies: Indem die tierische Organisation zur menschlichen heraufsteigt, werden die einzelnen, schon im Tiere liegenden Organformen umgebildet und dann gewissermaßen durch ihre Umbildung in die Möglichkeit versetzt, nun Platz zu haben für das, was sich vom Innern des Menschen her, aus dem ganzen Menschen heraus in der also umgebildeten tierischen Organisation offenbaren kann."
      ],
      [
        "Nur an eine Metamorphose der tie- rischen Organisation ins Menschliche herauf dachte Goethe, nicht an eine selbständig abgegliederte mensch- liche Morphologie.",
        "Dies, möchte ich sagen, muß man als Grundlage voraussetzen, wenn nun auch im anthroposophischen Sinne aufgesucht wird die Differenzierung zwischen dem tierischen und dem menschlichen Organismus."
      ],
      [
        "Wenn die Organisation selbst, in ihren Formen, nur auf einer Metamorphose des Tierischen und des Menschlichen beruht, dann muß man, wenn man die Differenzie- rung aufsuchen will, vor allem darauf sehen, wie das 38 Leben beim Menschen und wie es beim Tiere verläuft, man muß gewissermaßen darauf sehen, wie aus dem Menschlichen heraus das Funktionieren mit den Orga- nen sich gestaltet, und wie aus dem Tierischen heraus das Funktionieren mit den Organen sich gestaltet.",
        "Kurz, man muß den Unterschied mehr auf einem biologischen, als auf einem morphologischen Gebiete suchen."
      ],
      [
        "Nun kann man von einer gewissen Seite her der Auffassung von einem biologischen Unterschied ganz besonders die Wege bereiten, indem man von demjeni- gen ausgeht, was einem als die Grundlage des tierischen Funktionierens erscheinen muß, und das ist sowohl bei den Menschen wie bei den Tieren das, was mit den Sinnesorganen zusammenhängt.",
        "Die Sinnesorgane oder besser gesagt, die Funktionen der Sinnesorgane, leben ja mehr oder weniger in allem, was sich im tierischen und menschlichen Organismus abspielt."
      ],
      [
        "Wir müssen schon bei den niederen Tieren annehmen, daß sich bei den einfachen Ernährungsprozessen, in den reinen Stoff- wechselvorgängen, ein gewisses Funktionieren primi- tiver Sinne abspielt, daß also, sagen wir, Geschmacks- erlebnisse zum Beispiel parallel gehen dem, was mehr oder weniger rein chemisch der Stoffwechsel ist.",
        "Diese Dinge differenzieren sich immer mehr und mehr, je weiter man in der Tierreihe heraufkommt, bis zum Menschen hin."
      ],
      [
        "Aber wir werden durchaus nirgends, wenn wir unbefangen auf die tierische Organisation eingehen, etwas finden, worinnen nicht ein Sinnesleben vorhanden ist.",
        "Gewiß, man kann sagen: Was hat schließlich dieses Sinnesleben zum Beispiel mit der Lymphebildung oder mit der Blutbildung und so weiter zu tun?"
      ],
      [
        "Nun ist man heute auch schon in der nicht von An- throposophie beeinflußten Wissenschaft dazu gekom- 39 men, von unterbewußten Vorgängen der menschlichen Psyche zu sprechen, und es wird deshalb, auch wenn es der Kürze der Zeit halber nur angedeutet werden kann, nicht als etwas ganz Unberechtigtes erscheinen, wenn ich sage: Was sich in Mund und Gaumen als das Ge- schmackserlebnis abspielt, was als das Geschmackserleb- nis auftritt unter dem Wirken und der Funktion zum Beispiel des Ptyalins, des Pepsins und so weiter, wie sollte das nicht auch ins Unbewußte hineinspielen?",
        "Warum sollte - ich sage es als eine Art von Postulat - das Ge- schmackserlebnis sich nicht fortsetzen durch den ganzen Organismus, und warum sollten nicht unbewußt Ge- schmackserlebnisse parallel gehen der Lymphe- und Blutbildung und allen Organprozessen?"
      ],
      [
        "Wir werden da- her die menschliche und die tierische Organisation von ihrer biologischen Seite her sehr wohl verfolgen können, wenn wir einmal das Sinnesleben betrachten.",
        "Dieses Sinnesleben verläuft nun - wie ich für einige von Ihnen seit Jahren angedeutet habe, wie es zum Teil durchaus schon eine Sache der äußeren Wissenschaft ist - nicht nur in den gewöhnlich angeführten fünf Sinnen, sondern in einer deutlich unterscheidbaren Anzahl von zwölf menschlichen Sinnen."
      ],
      [
        "Dabei muß man aber bloß vom Menschen sprechen.",
        "Für den, der einsehen will, daß es ebenso berechtigt ist, von zwölf Sinnen zu sprechen, wie von fünf oder sechs vom Sehen, Hören, Riechen, Schmecken, Fühlen oder Tasten -, für den ist es berechtigt, davon zu sprechen, daß wir zum Beispiel einen Gleich- gewichtssinn haben, der uns innerlich erkennen läßt, ob wir auf beiden Füßen stehen oder nur auf einem, ob wir mit unsern Armen die eine oder die andere Bewegung ausführen und so weiter."
      ],
      [
        "Indem wir uns als Mensch in die Welt hineinstellen, sind wir in einer Gleichge- 40 wichtslage.",
        "Diese Gleichgewichtslage nehmen wir also, wenn auch viel dumpfer, sinnlich wahr, wie wir dasjenige sinnlich wahrnehmen, was im Sehvorgang sich abspielt; so daß wir von einem Gleichgewichtssinn sprechen kön- nen, wie wir von einem Sehsinn sprechen können."
      ],
      [
        "Wir müssen uns nur darüber klar sein: Wenn wir von diesem Gleichgewichtssinn sprechen, so wenden wir uns mehr der eigenen Organisation zu; wir schauen gewissermaßen nach innen, während wir mit den Augen nach außen schauen.",
        "Aber es hegt diesem Erleben im Gleichge- wichtssinn durchaus eine sinnliche Funktion zugrunde."
      ],
      [
        "Ebenso können wir nach einer anderen Seite hin die Anzahl der Sinne ergänzen.",
        "Wenn wir bloß hören, so ist das Funktionieren des menschlichen Organismus etwas wesentlich anderes, als wenn wir zwar durch das Ohr direkt hören, aber dann auf das eingehen, was indirekt in der Sprache uns wahrnehmbar wird."
      ],
      [
        "Wenn wir mit in- nerem Verständnis die Worte, die Sätze des anderen verfolgen, haben wir es nicht bloß zu tun mit einem Urteilen, sondern dem Urteilsprozeß geht auch da vor- aus ein Wahrnehmungsprozeß, ein Sinnesprozeß; also wir müssen davon sprechen, daß wir einen Sprachsinn - oder eigentlich einen Sprachesinn, einen Wortesinn - haben, wie wir einen Gehörsinn haben.",
        "Mit anderen Worten: Wir müssen, wenn wir die Worte mehr anato- misch-physiologisch betrachten, innerhalb der mensch- lichen Organisation eine spezielle [Sinnes] organisation voraussetzen, welche dem Anhören des Gesprochenen ebenso entspricht, wie die Gehörorganisation dem An- hören der unartikulierten Töne."
      ],
      [
        "Und wir müssen eine Spezialorganisation voraussetzen für den Sprachsinn, die ganz ähnlich ist einer sonstigen Sinnesorganisation, zum Beispiel der Sehorganisation oder der Hörorganisation. 41 Wir dürfen auch, wenn wir unbefangen zu Werke gehen, nicht sagen: Wir lernen erkennen, daß ein anderer Mensch vor uns steht, wenn wir sehen, daß an dieser äußeren Raumesform etwas wie eine Nase ist, wie zwei Augen und so weiter, und nun durch Analogie schließen, daß darin ein Mensch steckt, weil wir sehen, daß in uns selber ein Mensch steckt, der sich äußerlich offenbart durch Nase, Augen und so weiter.",
        "Ein solcher unbewuß- ter Schluß liegt in Wirklichkeit nicht zugrunde, aber es liegt ein unmittelbares Eingehen auf den anderen Men- schen zugrunde, dem etwas Spezielles in der Organisa- tion des Menschen entsprechen muß, das nur zu paral- lelisieren ist mit einer Sinnesorganisation, so daß wir auch von einem Ichsinn sprechen können."
      ],
      [
        "Wenn wir in dieser Weise das Funktionieren des Menschen ganz un- befangen durchschauen, müssen wir mit derselben Be- rechtigung, mit der wir von einer Gehör-, Geschmack- und so weiter -Organisation sprechen, auch sprechen von einer Wahrnehmungsorganisation für Worte, von einer Wahrnehmungsorganisation für Gedanken, von einer Wahrnehmungsorganisation für das Ich - nicht für das eigene Ich, denn das beruht auf etwas ganz anderem.",
        "Und wir müssen weiter sprechen von einem Bewe- gungssinn, denn ob wir uns bewegen oder ob wir in Ruhe sind, das ist etwas ganz anderes."
      ],
      [
        "Ebenso müssen wir dann sprechen von einem Lebenssinn - die ge- wöhnliche Wissenschaft spricht zum Teil schon davon.",
        "Wenn wir so die Zahl der Sinnesorganisationen fest- stellen, kommen wir auf zwölf menschliche Sinne."
      ],
      [
        "Von diesen sind eine Anzahl allerdings innere Sinne; denn wir nehmen den inneren Organismus - wie wir uns fühlen und wie es uns geht im Gleichgewichtssinn, im Bewe- gungssinn und so weiter - ebenfalls wahr.",
        "Aber qualitativ 42 ist das Erlebnis beim Wahrnehmen der inneren Organi- sation durchaus das gleiche wie beim Seh-, Hör- oder Geschmackvorgang."
      ],
      [
        "Es handelt sich nur darum, die Dinge im richtigen Zusammenhang zu sehen.",
        "Wenn man in dieser Weise in bezug auf den Men- schen von einer vollständigen Sinnesphysiologie ausgeht, werden gewisse biologische Erscheinungen auf der einen Seite im Reiche des Menschen, auf der anderen Seite im Reiche der Tiere von einer ganz besonderen Bedeutung [sichtbar], von einer Bedeutung, die bestehen kann, auch wenn man alles dasjenige restlos zugibt, was von neueren Naturforschern, selbst von Haeckel, vorgebracht worden ist für den morphologischen und auch physiologischen Zusammenhang der menschlichen Organisation mit der tierischen."
      ],
      [
        "Hier walten ja allerdings die unmöglich- sten Mißverständnisse.",
        "Man glaubt zum Beispiel, die Anthroposophie müsse sich in Gegensatz stellen zum Haeckelismus, einfach aus dem Grunde, weil sie von der bloßen Betrachtung der Sinneswahrnehmungen zur em- pirischen Betrachtung des Geistigen aufsteigt; man glaubt, Anthroposophie müsse aus diesen Untergründen heraus etwas am Haeckelismus verändern."
      ],
      [
        "Nein! - Was am Haeckelismus verändert werden muß, das muß aus na- turwissenschaftlicher Methodik heraus verändert wer- den, da braucht Anthroposophie nicht mitzureden, da kann man auch als Naturforscher mit Haeckel disku- tieren.",
        "Was Anthroposophie zu sagen hat, das liegt auf einem ganz anderen Gebiete."
      ],
      [
        "Mit Recht kann betont werden: Zählt man die Knochen der höheren Tiere, so unter- scheidet sich die Anzahl der Knochen nicht von der beim Menschen.",
        "Und ebenso ist es mit den Muskeln.",
        "So kommen wir nicht zu einer Differenzierung der mensch- 43 liehen und der tierischen Organisation."
      ],
      [
        "Aber wenn wir biologisch vorgehen, kommen wir zu einer wirklichen Differenzierung.",
        "Wir kommen dann dazu, einen beson- deren Wert darauf zu legen, daß sich im wesentlichen die menschliche Organisation in einer anderen Art in den Kosmos hineinstellt als die tierische."
      ],
      [
        "Wenn wir gerade die höheren Tiere betrachten, müssen wir sagen: Ein Wesentliches bei ihnen ist es, daß die Achse ihres Rückgrats parallel zur Erdoberfläche geht, während im Gegensatz dazu beim Menschen im Verlaufe seines Le- bens die horizontale Lage der Rückgratachse in eine vertikale verwandelt wird, so daß also eine wichtige Lebensfunktion beim Menschen darin besteht, sich auf- zurichten. - Ich weiß, es kann nun natürlich eingewen- det werden: Es gibt doch aber auch Tiere mit mehr oder weniger aufrechter, vertikaler Rückgratachse. - Darauf kommt es aber nicht an, wie es sich gegenüber einer äußeren Morphologie ausnimmt, sondern darauf, wie die ganze Organisation veranlagt ist.",
        "Wir werden auch sehen, wie bei gewissen Tieren, Vogelarten oder auch Säuge- tierarten, bei denen mehr oder weniger die Rückgratachse in eine vertikale Lage gebracht werden kann, gerade gegenüber ihrer ganzen Veranlagung eine Art Degene- rierung auftritt, während es beim Menschen schon in der Veranlagung liegt, daß die Rückgratachse eine Vertikal- lage hat."
      ],
      [
        "Als ich dies einmal vor vielen Jahren bei einem Vor- trage in München sagte, kam ein naturwissenschaftlich gebildeter Mann zu mir, den ich natürlich ganz gut verstehen konnte, und sagte: Wenn wir schlafen, haben wir aber doch auch die Rückgratachse horizontal. - Darauf aber kommt es nicht an, sagte ich ihm, sondern darauf, wie im Verhältnis zu der Lage, sagen wir, der 44 Bein- oder Fußknochen zum ganzen übrigen Körperbau die Rückgratachse im ganzen kosmischen Zusammenhang des Menschen gestellt ist, und wie sich das beim Men- schen oder beim Tier auswirkt.",
        "Der Mensch hat zwar beim Schlafen sein Rückgrat horizontal, aber diese hori- zontale Lage ist äußerlich; innerlich dynamisch ist der Mensch so organisiert, daß er sich in seinen Gleich- gewichtszustand bringen kann, wo die Rückgratachse vertikal ist."
      ],
      [
        "Und wenn sich Tiere in einen solchen Gleichgewichtszustand bringen, so degenerieren sie in gewisser Beziehung, oder sie bringen es dahin, gewisse menschenähnliche Funktionen zu entwickeln und da- durch auch das zu beweisen, was ich nun ausführen will.",
        "Wir können sagen: Indem der Mensch rein funktio- neil aus der gesamten Dynamik seines Wesens heraus im Laufe seiner ersten Lebensjahre seine Rückgratachse vertikal gestaltet, bringt er sich im Kosmos in eine andere Gleichgewichtslage als das Tier."
      ],
      [
        "Aber jedes Wesen ist ja aus dem Gesamtkosmos heraus gebildet; man könnte auch sagen, es paßt sich ihm an - ich will jetzt darauf nicht weiter eingehen.",
        "Wenn wir die Gestaltung der einzelnen Knochen, zum Beispiel der Rippen- oder Kopfknochen und so weiter verfolgen, dann werden wir auch morphologisch die Möglichkeit gewinnen, in den Formen der Rippen- oder der Kopfknochen eines Menschen oder eines Hundes die Anpassung zu finden an die Vertikallage oder Horizontallage des Rückgrats."
      ],
      [
        "Indem sich der Mensch in die vertikale Lage hineinfin- det, lebt er gegenüber dem Tier, das auf seinen vier Bei- nen steht, in einer ganz anderen Gleichgewichtslage; er lebt in einem ganz anderen kosmischen Zusammenhang.",
        "Nun versuchen wir, das Problem von einer anderen Seite her anzufassen und uns klarzumachen, was eigent- 45 lich im Menschen beim Sinnesvorgang und was in An- lehnung an den Sinnesvorgang bei ihm vorgeht."
      ],
      [
        "Ich werde dabei wegen der Kürze der Zeit genötigt sein, nur andeutend zu sprechen, aber es könnte das auch in eine ganz exakte biologisch-physiologische Terminologie um- gesetzt werden.",
        "Nehmen wir den Sehvorgang."
      ],
      [
        "Wir können ihn gliedern in das, was spezifische Funktion des Sehorgans ist, und in das, was sich dann abspielt in der weiteren Fortsetzung in das Physische hinein, ich möchte sagen, in Analogie dazu, daß der Sehnerv vom Auge ausgeht und sich dann im Innern der Nervenorganisation verliert.",
        "Wir können also unterscheiden: einmal den Sehvorgang selbst, und dann alles, was sich daranschließt im Gesamterleben."
      ],
      [
        "In dem unmittelbar präsenten Sehvorgang ist noch das Vorstellungsmäßige immanent; indem wir irgend etwas anschauen, trennen wir noch nicht das Vorstellungs- mäßige von dem Sehvorgang.",
        "Wenden wir das Auge ab von dem, was wir anschauen, so behalten wir einen vor- stellungsmäßigen Rest zurück, der deutlich seine Ver- wandtschaft mit dem beim Sehvorgang Wahrgenomme- nen zeigt."
      ],
      [
        "Wer das richtig analysieren kann, sieht, wie verschieden gerade das ist, was sich als Vorstellungsrest ergibt aus dem Sehvorgang, gegenüber dem, was sich ergibt aus einem Hörvorgang.",
        "Wir haben also in uns das Erlebnis des Sehvorganges, ich möchte sagen, in dua- listischer Weise: zuerst mehr hingewendet zu dem, was die eigentliche Sinneswahrnehmung ist, und dann hin- gewendet zu dem, was uns als vorstellungsmäßiger Rest, als mehr oder weniger ausgestaltete Erinnerung bleibt."
      ],
      [
        "Nun nehmen Sie einmal alles das, was im Menschen lebt an innerem Vorstellungsmäßigen, das sich anlehnt an die fünf Sinne.",
        "Das meiste im menschlichen Seelen- 46 leben lehnt sich ja an an die Sehvorgänge; nur ein Neuntel etwa von dem, was durch die Sehvorgänge gegeben ist, ist durch die Hörvorgänge gegeben."
      ],
      [
        "Und wenn wir das innere Seelenleben betrachten, so ist dadurch noch we- niger gegeben als durch die Seh- und Hörvorgänge und so weiter.",
        "Wir wissen, daß dabei das Vorstellungmäßige, das ja zur bleibenden Erinnerung führt, auch eine Rolle spielt, aber eine wesentlich geringere als beim Seh- und Hörvorgang."
      ],
      [
        "Nun können wir die Frage aufwerfen: Gibt es für die mehr verborgenen Sinne, zum Beispiel für den Gleich- gewichtssinn oder für den Bewegungssinn auch diese Dualität, wie wir sie finden beim Sehsinn in dem Wahr- nehmungsmäßigen und dem Vorstellungsmäßigen?",
        "Bei einer wirklich unbefangenen Physiologie und Psycho- logie gibt es dies auch zum Beispiel für den Gleich- gewichtssinn, nur wird gewöhnlich der Zusammenhang nicht bemerkt."
      ],
      [
        "In dem Vortrage, den ich eben gehalten habe, habe ich von dem Mathematischen gesprochen, von dem Sichzurechtfinden in den Raumesverhältnissen, wo das Mathematische geometrisch angewandt wird.",
        "Wir konstruieren uns Raumesverhältnisse."
      ],
      [
        "Was ist das eigentlich, was wir da tun?",
        "Es ist in bezug auf den ganzen Menschen genau dasselbe wie das, was wir tun, wenn wir beim Sehvorgang die Wahrnehmung deutlich absondern von dem Vorstellungsmäßigen, indem wir die Vorstellung innerlich behalten. [Wir nehmen eine Farbe nicht nur äußerlich wahr], sondern wir erleben das Qualitative der Farbe, des Farbtones, und es lebt sogar das Gefühl, das ich als Gefühl habe bei einer warmen oder kalten Farbe, im Innern fort."
      ],
      [
        "Wir können uns nun folgendes sagen: Ich will einmal in einer umfassenden Seelenschau alle diejenigen Vor- 47 Stellungen überschauen, die ich im Leben dadurch ge- wonnen habe, daß ich durch meine Augen sehen kann.",
        "Wir würden ein inneres visuelles System in der Seele bekommen."
      ],
      [
        "Wir würden, ohne daß wir jetzt äußere Sehvorgänge haben, innerlich aufsteigen haben eine Art Nachkonstruktion der Sehvorgänge.",
        "Und wenn Sie dies in ebensolcher Weise in bezug auf den Gleichgewichts- sinn berücksichtigen, dann kommen Sie darauf, daß Sie durch alles das, was Sie durch den Gleichgewichtssinn im eigenen Organismus erleben, etwas im Innern herauf- steigen haben, das dem Geometrischen in der äußeren Welt [entspricht].* Mathematik oder Mechanik haben wir nicht [aus der äußeren Erfahrung] gewonnen."
      ],
      [
        "Ma- thematische und mechanische [Gesetze] sind durch inne- res [Konstruieren gewonnen].",
        "Wenn Sie sich mechani- sche [Gesetze] vergegenwärtigen, so haben Sie sie [ge- wonnen] durch das Vorstellungsmäßige Ihres Gleichge- wichtssinnes."
      ],
      [
        "Der ganze Mensch wird da zum Sinnesorgan und er bildet dabei [innerlich] gleichsam den anderen Pol [zu dem Wahrgenommenen] aus.",
        "Wir bilden zum Beispiel die Mathematik aus und glauben, wir haben in ihr eine reine a-priori-Wissenschaft."
      ],
      [
        "Aber die Mathematik ist keine reine a-priori-Wissenschaft.",
        "Wir merken nur nicht, daß wir dasjenige, was wir im Gleichgewichtssinn erle- ben, ebenso [in mathematisch-geometrische Vorstellun- gen] umsetzen, wie die Sehwahrnehmung sich in die Sehvorstellungen umsetzt."
      ],
      [
        "Ohne daß wir die Brücke *Die nachfolgenden Ausführungen sind vom Stenographen nur lük- kenhaft festgehalten.",
        "Die vom Herausgeber vorgenommenen not- wendigen Ergänzungen - gekennzeichnet durch eckige Klammern - stützen sich im wesentlichen auf folgende Vorträge Rudolf Steiners: 16."
      ],
      [
        "März 1921, in GA 324; 29.",
        "September, 1. und 3.",
        "Oktober 1920, in GA 322. 48 bemerken, wird das [durch den Gleichgewichtssinn Wahrgenommene] zu Mathematik oder zu Mechanik.",
        "Wenn Sie das bedenken, werden Sie den innigen Zu- sammenhang des menschlichen Gesamtorganismus mit seiner Gleichgewichtslage im Kosmos verstehen."
      ],
      [
        "Dann werden Sie sich sagen: Beim Tier, das auf seinen vier Bei- nen steht und dem durch seine Gleichgewichtslage auch der Inhalt seines Gleichgewichtssinnes gegeben ist, muß ja das Erleben des Gleichgewichts sich in einer ganz ande- ren Weise innerlich spiegeln als beim Menschen im Ma- thematischen.",
        "Wir finden das Mathematische einfach als ein Ergebnis unseres Hineingestelltseins in denKosmos."
      ],
      [
        "Wir reden von drei Dimensionen, weil wir nach drei Dimensionen in den Kosmos hineingestellt sind.",
        "Aber die vertikale Dimension haben wir uns selbst erst im Laufe unseres Lebens errungen.",
        "Wir haben uns in die vertikale Dimension erst hineingestellt."
      ],
      [
        "Was wir so in frühester Kindheit erleben, das spiegelt sich uns später in der Mathematik; es geht das nur nicht so schnell wie beim Sehvorgang.",
        "Die Spiegelung des Gleichgewicht- Erlebens geht im Laufe des Lebens vor sich."
      ],
      [
        "Wir haben in der Kindheit sehr stark das Erleben des Gleichge- wichtssinnes, wenn wir vom Kriechen übergehen zum Gehen und Stehen.",
        "Das spiegelt sich uns im späteren Lebensalter und wird als Mathematik und Mechanik sichtbar."
      ],
      [
        "Wir halten oft die Mathematik für etwas aus uns selbst Gesponnenes.",
        "Das ist sie nicht.",
        "Sie geht aus der Wahrnehmung des eigenen Organismus hervor.",
        "Warum sind denn gewisse Gedanken beim Menschen so, daß er sie auf den Kosmos beziehen kann, daß er sich aus den Gedanken ein ganzes Gedankengebäude bilden kann?"
      ],
      [
        "Das ist nur das Ergebnis dessen, wie der Mensch im Kosmos drinnensteht.",
        "Und wenn wir nun die Gleich- 49 gewichtslage, in der sich das Tier befindet [in seinem Verhältnis zum Kosmos], vergleichen mit der Gleich- gewichtslage des Menschen, so können wir sagen: Wir haben beim Tier das Gebundensein an die Erdenorgani- sation und wir haben beim Menschen das Aufgerich- tetsein, das Herausgehobensein aus der Erdenorgani- sation."
      ],
      [
        "Was wir als selbständige Gedanken aussprechen, rührt davon her, daß wir uns für unsere menschliche Organisation auch eine selbständige Gleichgewichtslage erringen.",
        "Es ist also der Akt des Sichhineinstellens in den Kosmos nicht etwas, was aus dem Organismus selbst hervorgeht und sich auch beim Tier findet, sondern etwas, was in diesen menschlichen Organismus selbst sich hineinbildet und was erst im Laufe der [ersten] Leben[sjahre] errungen wird, bis in die Organe hinein."
      ],
      [
        "Dadurch kommen wir zu jener Polarität des Menschen [gegenüber dem Tier], daß auf der einen Seite der Mensch aufrechtsteht und einen aufrechten Gang hat, und daß dieser ganzen kosmischen Position, in der der Mensch lebt, nun eben alles das angepaßt wird, was sich im einzelnen bei Mensch und Tier nicht unterscheidet.",
        "Und auf der anderen Seite erscheint im Seelischen dasjenige als Gedanken, was jetzt über das sinnlich Angeschaute, über das mit den fünf Sinnen Wahrgenommene hinaus- geht, was sich davon losmacht."
      ],
      [
        "So wie sich der Mensch durch seine Stellung zum Kosmos losmacht von der Erde, ebenso machen sich die Gedanken des Menschen los von ihrer Gebundenheit an die Sinneswelt, sie werden in einer gewissen Beziehung frei.",
        "Wir müssen - für die Anthroposophie ist das wieder- um eine Sicherheit, hier möchte ich es zunächst mehr als Postulat hinstellen - wir müssen darin, daß der Mensch 50 diese durch die aufrechte Stellung seiner Rückgratachse bedingte Gleichgewichtslage hat, etwas sehen, was den Menschen trennt von dem Tiere; und auf der anderen Seite müssen wir die besondere Form der Vorstellungs- welt, der Gedanken, als das spezifisch Menschliche an- sehen."
      ],
      [
        "Aber gerade der, der solche Dinge vom anthro- posophischen Standpunkte aus durchschaut das wird mehr oder weniger noch zur Sprache kommen kön- nen -, der sieht, wie der Mensch durch die besondere Ausbildung seines Gleichgewichtssinnes und seines Be- wegungssinnes auch mehr zu einem freien Gedankensy- stem kommt, als das [bei dem Erleben durch] Augen und Ohren der Fall ist, und der wird auch einsehen, daß der Mensch nun dafür auch eine innere Organisation haben muß.",
        "Der Mensch hat einfach eine Organisation in sich, die beim Tier noch nicht zu finden ist - das kann durchaus auch einmal materiell nachgewiesen werden -, die einfach derjenigen Form der Gedanken dient, die sich losgeris- sen hat von der [Gebundenheit an die Erde] wie beim Tier, und die durch die besondere Gleichgewichtslage beim Menschen bedingt ist."
      ],
      [
        "Wir können also sagen: Indem der Mensch sich aufrichtet, schafft er sich ein Organ für die abstrakten Gedanken.",
        "Und so haben wir beim Menschen die durch seine aufrechte Lage bedingte Organisation, die zunächst nichts anderes zeigt, als daß die Organe, die beim Tier auch da sind, eine andere Lage haben; aber durch diese aufrechte Lage wird in der Nerven- und Blutorganisation bewirkt, daß unter dem Einfluß dieser anderen Gleichgewichtslage im Menschen etwas auftritt, was das Tier nicht haben kann."
      ],
      [
        "Da finden wir das, was den Menschen biologisch vom Tier unterscheidet.",
        "Wir finden diesen Zusammen- hang wirklich in der physischen Organisation des Men- 51 sehen und nicht in einem bloßen Dynamismus.",
        "Das ist von fundamentaler Bedeutung."
      ],
      [
        "Stellen Sie sich nur ein- mal die Umbildung der Organisation vor, die geschieht durch die Veränderung der Gleichgewichtslage, wie sie beim Tier ist, in die Gleichgewichtslage des Menschen, was sich da ändert zum Beispiel in bezug auf die Ober- und Unterschenkel, die Hände und so weiter. [Stellen Sie sich einmal vor, was es bedeutet], daß der Mensch ein Zweihänder ist und kein Vierfüßler.",
        "Der Mensch ist zwar mit denselben Formen ausgestattet wie das Tier, aber er hat sie in einer anderen Lage und dadurch in veränderten, metamorphosierten Formen."
      ],
      [
        "Das wird auch einmal anatomisch nachgewiesen werden können, wenn die notwendigen Werkzeuge und Experimentiermetho- den ausgebildet sein werden.",
        "Wir suchen nach solchen Werkzeugen und Experimentiermethoden in unseren Instituten in Stuttgart."
      ],
      [
        "Man muß allerdings, um diese Methoden auch äußerlich empirisch zu finden, zuerst durch imaginatives Anschauen darauf gekommen sein, [wo die Unterschiede hegen].",
        "Daher ist die Anthroposo- phie in bezug auf [die Erforschung] der feineren Gebiete der Menschen-, Tier- und Pflanzenformen der Wissen- schaft durchaus nicht unnütz, denn die Wissenschaft kann die Dinge nicht durch Imagination finden."
      ],
      [
        "Sind sie aber gefunden, dann können sie auch [durch die Wis- senschaft] verifiziert werden.",
        "Wenn man darauf schaut, wie eine andere Gleichge- wichtslage die Organe umbildet, so findet man auch, daß bestimmte Organe so umgeändert werden, daß sie zum menschlichen Sprachorgan werden, daß der Organismus sprachschöpferisch wird."
      ],
      [
        "Damit haben Sie nun eine Einsicht gewonnen in die besondere Organisation des Menschen, die einfach da- 52 durch entsteht, daß er ein aufrechtgehendes Wesen ist, was sogar bis ins Materielle hinein Folgen hat.",
        "Auch in bezug auf den physiologischen Sprachorganismus haben Sie etwas gegeben auch wo man einen äußeren mor- phologischen Unterschied zwischen Mensch und Tier nicht festsetzen kann -, was doch eine Differenzierung zwischen Mensch und Tier in biologischer Beziehung zeigt."
      ],
      [
        "Dies sind einige Anregungen, die den Weg angeben können, wie das, was in einer äußeren, laienhaften Weise gesucht wird, auch auf einem wirklich wissenschaftli- chen Wege untersucht werden kann.",
        "Ich konnte das, was ich sagen wollte, hier nur skizzieren."
      ],
      [
        "Aber denken Sie sich [diese Gedanken] weiter fortgesetzt, so ergibt sich für die Wissenschaft tatsächlich ein Weg, um die Unter- schiede zwischen der tierischen und der menschlichen Organisation in biologischer Beziehung zu [erforschen]. 53"
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG ANTHROPOSOPHIE UND PHILOSOPHIE Berlin, 7. März 1922",
    "paragraphs": [
      "Meine sehr verehrten Anwesenden! Es ist immer schwer, wenn man mit einem ernsten wissenschaftlichen Gewis- sen den überkommenen Ausdruck «Logos» in irgendei- ne der neueren Sprachen übersetzen will. Wir sagen ja, wenn wir «Logos» übersetzen, gewöhnlich «Wort», wie das für die Bibel üblich ist.",
      "Wir denken aber, wenn wir zum Beispiel die «Logik» im Sinne haben, nicht so sehr an das «Wort», sondern wir denken dann an den «Ge- danken», wie er in den menschlichen Individuen wirkt und seine Gesetzmäßigkeiten hat. Doch wenn -wir von «Philologie» reden, so haben wir wiederum das Bewußt- sein: Wir entwickeln eine Wissenschaft, die sich auf das Wort bezieht.",
      "Ich möchte sagen: Gerade heute ist das, was nach neuerem Sprachgebrauch in dem Wort «Logos» enthalten ist, im Grunde genommen in allem Philoso- phischen drinnen. Und wenn wir von «Philosophie» sprechen, dann können wir in dem, was wir dabei nicht so sehr definieren als erleben, gar wohl empfinden, wie ein Abglanz dieses unbestimmten Erlebnisses gegenüber dem Logos in all dem enthalten ist, was wir bei «Philo- sophie» fühlen.",
      "Philosophie deutet ja dem Wortlaute nach - was aber zweifellos damals, als Philosophie entstand, etwas mehr als nur Wortlaut war -, deutet ja auf ein ganz bestimm- tes inneres Erlebnis des Menschen; das Wort Philo- 54 sophie deutet darauf, daß der Mensch an dem, was dem Logos verwandt ist, «Sophia», ein bestimmtes, man möchte sagen, wenn auch nicht ein persönliches, so doch ein allgemein menschliches Interesse hat. Es deutet das Wort Philosophie weniger unmittelbar auf den Besitz eines Wissenschaftlichen hin, als auf ein inneres Verhalten des Menschen zu dem weisheitsvollen Inhalt des Wis- senschaftlichen.",
      "Da unser Gefühl gegenüber der Philo- sophie heute nicht mehr so ganz sicher ist wie in den Zeiten, als Philosophie auf der einen Seite fast zusam- menfiel mit, ich will nicht sagen mit Wissenschaft, aber mit wissenschaftlichem Streben, und auf der anderen Seite etwas war, was auf ein inneres menschliches Ver- halten hindeutete, haben wir heute ein außerordentlich unbestimmtes Erlebnis, wenn wir von Philosophie spre- chen oder uns in Philosophie betätigen. Dieses unbe- stimmte Erlebnis ist aber außerordentlich schwer aus den Tiefen des Bewußtseins heraufzuheben, wenn man das auf eine bloß dialektische oder auch äußerlich defi- nierende Weise versucht, und nicht einzugehen versucht auf das, was gegenüber der Philosophie menschliches Erleben im Laufe der geschichtlichen Entwicklung war.",
      "Zu einer solchen Betrachtung fordert ja die Gegenwart ganz besonders heraus. Blicken wir als mitteleuropäische Menschen um eini- ge Jahrzehnte zurück, so war eigentlich das Hineinleben in die Philosophie für den Menschen, der ein solches Einleben suchte, gerade in Mitteleuropa noch etwas an- deres, als es heute im zweiten Jahrzehnt des 20.",
      "Jahrhun- derts ist, wo wir ja im Grunde genommen nicht nur äußerlich physisch, sondern gerade geistig wirklich so viel durchlebt haben, wie früher - man darf das ruhig aussprechen - in Jahrhunderten erlebt worden ist. Und 55 wenn man zurückblickt auf die Erlebnisse, die ein - wenn ich mich des pedantisch-philiströsen Ausdruckes bedienen darf - Philosophie-Beflissener so in den 50er, 60er, 70er Jahren des 19.",
      "Jahrhunderts, vielleicht auch noch später, als Mitteleuropäer haben konnte, so sind es im wesentlichen diese: Man blickte zurück auf die Blüte- zeit deutscher philosophischer Entwicklung, man blickte zurück auf die große Philosophenzeit Fichtes, Schellings, Hegels; man hatte um sich eine gebildete und gelehrte Welt, welche diese Philosophenzeit als etwas durchaus Abgetanes betrachtete und welche in der heraufkom- menden naturwissenschaftlichen Weltanschauung dasje- nige sah, was an die Stelle früherer philosophischer Be- trachtungen treten sollte. Man bewunderte die Größe der Gedankenerhebung, wie sie bei einem Schelling hervortrat, man bewunderte die Energie und die Kraft Fichtescher Gedankenentwicklung, man hatte vielleicht auch ein Gefühl für das rein Umfassende, Scharfsinnige Hegeischen Denkens, aber man betrachtete mehr oder weniger dieses klassische Zeitalter deutscher Philosophie doch als etwas Überwundenes.",
      "Und daneben gab es dann die Bestrebung, aus der Naturwissenschaft heraus etwas zu entwickeln, was eine allgemeine Weltanschauung werden sollte, von den Be- strebungen der «Kraft- und Stoff-Menschen» bis zu den- jenigen, die vorsichtiger aus naturwissenschaftlichen Begriffen heraus zu einer philosophischen Weltanschau- ung kommen wollten, die aber die ehemalige idealisti- sche Philosophie eben ablehnten. Es gab alle Nuancen von Denken und Forschen auf diesem Gebiete.",
      "Und dann gab es eine dritte Sorte von Denkern auf diesem Gebiete, die konnten nicht mitgehen mit dem bloßen naturwissenschaftlichen Begründen einer Welt- 56 anschauung, aber sie konnten auf der anderen Seite auch wieder nicht hineintauchen in das real Gedankliche, wie es etwa bei Hegel gegeben ist. Für diese entstand die große Frage: Wie kann sich der Mensch mit seinem Denken, das er als etwas ausbildet, das nur in ihm selber liegt, in ein Verhältnis zur Objektivität, zur Außenwelt setzen?",
      "Es waren die Erkenntnistheoretiker der ver- schiedenen Nuancen, welche in dem Ruf «zurück zu Kant» übereinstimmten, aber diesen Weg zu Kant in der verschiedensten Weise einschlugen; es waren scharfsin- nige Denker wie etwa Liebmann, Volkelt und so weiter, die aber im Grunde genommen doch innerhalb des Er- kenntnistheoretischen blieben und nicht über die Frage hinauskamen: Wie soll der Mensch mit dem, was er gedanklich, vorstellungsgemäß in sich trägt, die Brücke schlagen zu einer transsubjektiven, außerhalb des Men- schen bestehenden Realität? Was ich Ihnen hier als eine Situation schildere, die der Philosophie-Beflissene etwa im letzten Drittel des 19.",
      "Jahrhunderts vorfand, hat zu keinerlei Art von Lösung geführt. Das war gewissermaßen die Mitte eines Dramas oder irgendeines in der Zeit verlaufenden Kunstwerkes, zu dem kein Ende hinzugefunden worden ist.",
      "Es liefen diese Bestrebungen mehr oder weniger ins Unbestimmte aus. Sie liefen aus in eine große Anzahl von Fragen, und überall fehlte im Grunde genommen der Mut, gegenüber diesen Fragen auch nur das Streben nach Lösungsversu- chen zu entwickeln.",
      "Heute nimmt sich die Situation in der ganzen philo- sophischen Welt so aus, daß man sie gar nicht mehr so schildern kann, wie ich jetzt eben die Situation vom letzten Drittel des 19. Jahrhunderts dargestellt habe, wenn man die Wirklichkeit treffen will.",
      "Heute sind vor 57 unserem Blick philosophische Gesichtspunkte aufge- taucht, welche, ich möchte sagen, aus ganz anderen Untergründen emporgestiegen sind, und die notwendig machen, daß wir heute die philosophische Situation in einer ganz anderen Weise charakterisieren. Heute tritt, wenn wir die philosophische Situation charakterisieren wollen, scharf vor unser Seelenauge dasjenige, wofür ja unser Blick im zweiten Jahrzehnt des 20.",
      "Jahrhunderts so sehr geschärft werden konnte, nämlich die vonein- ander so stark differierenden philosophischen Weltan- schauungen des Westens, der europäischen Mitte und des europäischen Ostens. Heute steht in einer anderen Weise als noch vor kurzer Zeit vor unserem gefühlsmä- ßigen Erleben des Philosophischen das, was sich etwa aussprechen kann in den drei Namen: Herbert Spencer - Hegel - Wladimir Solowjew.",
      "Indem wir diese drei Per- sönlichkeiten vor uns hinstellen, haben wir in ihnen die Repräsentanten dessen, was heute die philosophische Situation charakterisieren kann. Innerlich war das ge- wissermaßen schon immer oder seit langer Zeit der Fall, aber es tritt erst heute die philosophische Situation so charakteristisch vor unser Seelenauge.",
      "Sehen wir uns einmal den Westen an: Herbert Spen- cer. Ich müßte natürlich, wenn ich vollständig sein wollte, den ganzen Hergang der philosophischen Entwicklung schildern, wie er von Bacon, Locke über Mill zu Spencer geführt hat; doch das kann heute nicht meine Aufgabe sein.",
      "In Herbert Spencer tritt uns eine Persönlichkeit entgegen, welche Philosophie begründen will, aber Phi- losophie begründen will rein aus Begriffssystemen her- aus, die an der Naturwissenschaft gewonnen sind. Wir finden in Spencer eine Persönlichkeit, die zu dem Na- turwissenschaftlichen restlos Ja sagt, und die aus diesem 58 Jasagen heraus die Konsequenz zieht: Also muß alles philosophische Denken über die Welt aus diesem Na- turwissenschaftlichen gewonnen werden.",
      "So sehen wir, wie Spencer sucht, in der Naturwissenschaft gewisse Vorgänge in Begriffe zu fassen, zum Beispiel wie ein fortwährendes Sichzusammenziehen und Sichausbreiten der Stoffe stattfindet, ein Differenzieren und Konsoli- dieren. Er beobachtet das zum Beispiel an der Pflanze, die in den Blättern sich ausbreitet und sich im Keime zusammenzieht, und er versucht, solche Begriffe dann m klare naturwissenschaftliche Formen zu bringen und damit eine Weltanschauung aufzubauen.",
      "Und er versucht sogar, die menschliche Gesellschaft selber, den sozialen Organismus, nur so zu denken, daß dieses Denken eine Analogie bietet zu dem natürlichen Organismus. Da kommt er aber sogleich in die Enge.",
      "Der natürliche Organismus des Menschen ist gebunden an den Zusam- menfluß alles dessen, wodurch dieser Organismus mit der Außenwelt in ein Verhältnis tritt, durch Wahrneh- mungen, durch Vorstellungen und so weiter. Der einzelne natürliche Organismus ist gebunden an das, was sich unter dem Einfluß des Sensoriums entwickeln kann.",
      "In dem gesellschaftlichen Organismus findet Herbert Spencer ein solches Sensorium nicht, kein irgendwie zentral zusammenlaufendes Nervensystem. Dennoch konstruiert er einen solchen gesellschaftlichen Organis- mus und findet darin gewissermaßen die Krönung seines philosophischen Gebäudes, das ganz auf Naturwissen- schaft aufgebaut ist.",
      "Was liegt damit eigentlich in diesem Westen vor? Da liegt vor, daß dort gerade der naturwissenschaftliche Gedanke in seiner vollen, seiner berechtigten Einseitig- keit sich entwickelt hat. Da liegt vor, daß aus den ur- 59 sprünglichen Völkeranlagen heraus feinste Beobach- tungsgabe und Experimentiertalent sich entwickelt ha- ben.",
      "Da liegt vor, daß ein Interesse vorhanden ist, die Welt des äußerlich Sinnlich-Wirklichen in den kleinsten Einzelheiten zu beobachten, ohne dabei etwa ungedul- dig zu werden und aufsteigen zu wollen zu irgendwelchen zusammenfassenden Begriffen. Da liegt aber auch vor ein Hang, mit der Wissenschaft stehenzubleiben innerhalb dieser äußeren sinnlichen Tatsachenwelt.",
      "Da liegt das vor, was ich nennen möchte: eine Art Furcht davor, von der Sinneswelt irgendwie zu einem Zusammenfassenden aufzusteigen. Da aber der Mensch doch nicht anders kann, als zu leben in etwas, was auch über die Sinneswelt hinausgeht, was dem Menschen nicht einfach durch die Sinne gegeben wird, so tritt hier im Westen die Er- scheinung hervor, daß die gesamte geistige Welt restlos übergeben sein soll dem individuellen Glauben des ein- zelnen, und daß dieser Glaube frei von allem wissen- schaftlichen Einfluß sich entwickeln soll.",
      "Was Inhalt des Religiösen ist, das will sich der Mensch nicht antasten lassen von dem, was er wissenschaftlich erkundet. So sehen wir, daß bei Herbert Spencer, der in seiner Art ganz konsequent die naturwissenschaftliche Denkweise heraufführt bis in die Soziologie hinein, streng [getrennt] vorhanden ist, auf der einen Seite die Wissenschaft, die ganz naturwissenschaftlich verlaufen soll, und auf der anderen Seite für den Menschen ein geistiger Inhalt, mit dem Wissenschaft sich nichts zu schaffen machen soll.",
      "Gehen wir nun von Herbert Spencer zu dem, was uns bei Hegel entgegentritt. Es verschlägt nichts, daß Hegel, der dem ersten Drittel des 19. Jahrhunderts angehörte, im zweiten Drittel für das mitteleuropäische Philoso- phieren mehr oder weniger als überwunden galt, denn 60 was für Mitteleuropa charakteristisch ist, das ist doch am bedeutsamsten gerade bei Hegel zum Vorschein gekom- men.",
      "Sehen wir uns Hegel an: Schon in seiner, ich möchte sagen, gefühlsmäßigen Veranlagung liegt eine gewisse Abneigung gegen diese universalistische naturwissen- schaftliche Art, mit der Weltanschauung so zu verfah- ren, wie sie im Westen ausgestaltet wird durch Herbert Spencer, aber sich selbstverständlich vorbereitet hat durch dessen Vorgänger, sowohl die Naturforscher wie auch die Philosophen. Wir sehen bei Hegel, wie er zum Bei- spiel Newton nicht leiden kann, wie ihm die besondere Art, das Weltall nur mechanistisch zu denken, unsym- pathisch ist, wie er Newton ablehnt nicht etwa bloß in bezug auf die Farbenlehre, sondern auch als Interpreten des Kosmos.",
      "Hegel gibt sich Mühe, zu den Keplerschen Formeln über die Planetenbewegungen zurückzukeh- ren; er analysiert die Keplerschen Formeln über die Planetenbewegungen und findet für sich, daß Newton eigentlich gar nichts hinzugefügt hat, sondern daß in den Keplerschen Formeln schon das ganze Gravitationsge- setz drinnenliegt. Und das übernimmt er aus dem Grunde, weil er aus dem, was bei Kepler mehr aus geistigem Erleben kommt, ein wissenschaftliches Denken hervor- gehen sieht, das umfassend ist und das das äußere Natur- wissenschaftliche vom Geiste aus begreiflich zu machen versucht.",
      "Kepler ist für Hegel einfach die Persönlichkeit, die imstande ist, in den Geist auch mit dem Denken einzudringen und eine Brücke zu schlagen zwischen dem, was wissenschaftlich erkannt wird, und dem, was nach der Meinung des Westens bloß geglaubt werden soll, der also imstande ist, die Wissenschaft heraufzutra- gen in das Gebiet, das für den Westen vermeintliches Gebiet des Glaubens ist. 61 Aus diesem Grunde lehnt Hegel, ganz im Einklang mit Goethe, die Newtonsche Farbenlehre streng ab. Überall sehen wir in der Hegeischen Anlage eine Art Antipathie gegen das, was bei Newton aus dessen An- lagen heraus ganz natürlich ist.",
      "Dafür ist bei Hegel ein entschiedenes Talent vorhanden, ganz in dem Gedank- lichen selber zu leben. Für Hegel war das einfach selbst- verständlich, was Goethe gegenüber Schiller sagte: «Ich sehe meine Ideen mit Augen».",
      "Das ist scheinbar eine Naivität, allein, solche Naivitäten nehmen sich oftmals, richtig betrachtet, als die tiefste philosophische Weisheit aus. Hegel würde einfach nicht verstanden haben, -wie man behaupten könne, die Idee des Dreiecks sei nicht zu fassen, denn Hegels Leben verlief eigentlich ganz - wenn ich mich so ausdrücken darf auf dem Plan des Gedan- kens.",
      "Für ihn war auch eine höhere Offenbarungswelt, eine Welt höherer Geistigkeit dadurch vorhanden, daß sie gewissermaßen ihre Schattenbilder auf eine Fläche wirft, die von Gedanken ausgefüllt ist. Von oben her wirft die geistige Welt ihre Schattenbilder auf die Fläche der menschlichen Seele, auf der der menschliche Gedan- ke sich entwickelt.",
      "Dadurch kommt für Hegel der Begriff des höheren Geistigen zustande, daß es auf der Fläche der Seele sich abschattet als Gedanken. Hegel ist dazu veranlagt, diese Gedanken voll als Geistiges zu erleben, und er erlebt auch das natürliche Geschehen nicht in seiner elementaren Gegenwart, sondern sieht es in den Gedankenbildern, die es auf die Fläche der Seele gewor- fen hat.",
      "So wird es in Hegels Philosophie zur Unmöglich- keit, in jener äußerlichen Weise Wissen und Glauben voneinander zu trennen, wie es dem Westen ganz natürlich ist. Für Hegel wird zur Lebensaufgabe die 62 Vereinigung der geistigen Welt, die der Westen einfach aus seinen Anlagen heraus in das bloße Glaubensgebiet verweisen will, mit der sinnlich-physischen Welt, zu einer solchen Welt, von der man wissen kann.",
      "Hier ist nicht mehr Wissen auf der einen Seite, Glauben auf der anderen Seite; hier ist der Menschenseele das große, bedeutsame Problem gestellt: Wie findet man im in- neren Erleben selbst die Brücke zwischen Glauben und Wissen, zwischen Geist und Natur? Aber es war gewissermaßen das Tragische in Hegel, daß er das, was er in so grandioser Weise als ein Problem aufzuwerfen verstand, eigentlich nur sah sozusagen in bezug auf die Fläche des Gedankens, daß er zwar die innere Kraft, die innere Lebendigkeit des Gedankens zu erleben verstand, aber vom Inhalte des Gedankens nichts Lebendiges erfassen konnte.",
      "Nehmen Sie die Hegeische Logik: Wiederum zurückgehen will er zum alten Begriff des Logos! Er fühlt: Wenn wir überhaupt einen realen Begriff vom Logos haben wollen, dann muß der Logos etwas sein, was nicht bloß als ein Gedachtes, sondern als ein real Wirkendes die Welt durchflutet und durchlebt.",
      "Für ihn ist der Logos nicht nur abstrakt- logischer Inhalt, sondern für ihn wird er realer Welt- inhalt. Sehen wir uns seine «Logik» an, den einen der drei Teile von Hegels Philosophie: Sie enthält nur abstrakte Begriffe!",
      "Und so steht, so furchtbar ergreifend für den, der mit seinem ganzen Menschen auf die Hegeische Philosophie einzugehen weiß, auf der einen Seite Hegels so grundrichtige Empfindung: Durch das, was in dem Logos erfaßt werden kann, muß eingedrun- gen werden in das schöpferische Prinzip der Welt. Der Logos muß sein «Gott vor der Erschaffung der Welt» - ein Hegelscher Ausdruck! 63 Dies auf der einen Seite.",
      "Und wie wird auf der ande- ren Seite dieser Logos von Hegel selbst entwickelt? Er beginnt beim «Sein», kommt zu dem «Nichts», zu dem «Werden», zu dem «Dasein». Er kommt zu der Kausali- tät, dem Zweck, zu der Teleologie.",
      "Man sehe sich die ganzen Begriffe in der Hegeischen Logik an und frage sich: Ist das dasjenige, was «vor dem Beginn der Schöp- fung als der Inhalt des Göttlichen» da sein konnte? Es ist abstrakte Logik, Forderung des Schöpferischen, der Logos als Postulat, aber als rein menschliches Gedan- kenpostulat!",
      "Man empfinde diese Tragik, die darin liegt! Und man empfinde dann weiter die Tragik, die darin liegt, daß die Hegeische Philosophie als überwunden galt! Sie enthält aber Momente, aus denen in der Tat neues Leben sprießen kann.",
      "Sie enthält Keime. Hegel hat sein Heil gesehen in dem: Sein - Nichts - Werden - Dasein. Wenn aber heute die Leute Hegel zugeführt bekommen, dann sagen sie: Das ist eine alte Schwarte, darauf brauchen wir uns nicht einzulassen. - Wenn man es aber unternimmt, sich durch einen inneren Seelen- prozeß darauf einzulassen, den Begriff innerlich zu er- leben, wie ihn Hegel zu erleben suchte, dann schwinden alle Begriffe von Empirie und Rationalismus, dann wird der Gedanke erfahren und das Erfahrene unmittelbar gedacht.",
      "Da wird der Gedanke zum Erlebnis und das Erlebnis zum reinen Gedanken. Wer das mitmacht, der empfindet das Bestreben, den Gedanken aus der Ab- straktheit zu erlösen, und die Hegeische Logik als den Keim dazu, daß aus dem Gedanken etwas ganz anderes werden kann, wenn er sich lebendig ausgestaltet.",
      "Mir erscheint oft Hegels Logik als der Keim einer Pflanze, dem man kaum ansieht, was er werden kann, der aber doch die mannigfaltigsten Anlagen in sich trägt. Und mir 64 scheint, wenn dieser Keim wächst, wenn ihn der Mensch liebevoll pflegt und in den seelischen Boden einsetzt durch anthroposophische Forschung, dann entsteht ge- rade das, daß der Gedanke nicht nur gedacht, sondern als Realität erlebt werden kann.",
      "Da haben wir das Mittel- europäische. Gehen wir nun zum Osten, so haben wir in Wladimir Solowjew einen Mann vor uns, der wie kein anderer Philosoph dazu berufen ist, immer mehr nun auch ein Inhalt unseres eigenen philosophischen Strebens zu werden, der uns so wichtig werden muß, indem wir seine besondere Charaktereigentümlichkeit auf uns wirken lassen.",
      "Wir sehen in Solowjew zugleich den Repräsen- tanten dessen, was europäisch-östliche Denkweise ist, die aber nicht die orientalisch-asiatische ist. Solowieff hat ja alles Europäische aufgenommen, er hat es nur in seiner besonderen östlichen Art entwickelt.",
      "Aber was sehen wir da sich entwickeln in bezug auf menschliches wissenschaftliches Streben? Da sehen wir, wie eigentlich gerade jene Denkweise, auf die der Westen bei Herbert Spencer das meiste gibt, etwas ist, auf das Solowjew im Grunde genommen hinunterschaut, an dem er höchstens die Wahrheiten und Erkenntnisse, die er sucht, sozusa- gen illustriert.",
      "Dagegen ist das, was er auseinandersetzt, ein volles Erleben in der Geistigkeit selbst. Es tritt bei ihm nicht mit dem vollen Bewußtsein hervor; es tritt mehr atavistisch, unbewußt hervor, aber es ist ein Erle- ben in der Geistigkeit selbst.",
      "Es ist der mehr oder weniger traumhafte Versuch, wissentlich das zu erleben, was der Westen - wiederum ganz bewußt in das Gebiet des Glaubens versetzt. Und so finden wir im Osten eine Auseinandersetzung mit dem, was in unbestimmter Weise erlebt werden kann, was sich etwa ausnimmt wie ein 65 einseitiges Erleben dessen, zu dem Hegel als der Geistig- keit der Welt von dem natürlichen Dasein aus die Brücke hinüberschlagen wollte.",
      "Vertieft sich heute jemand, der aus mitteleuropä- ischer Geistesbildung hervorgegangen ist, in Solowjew, so hat er zunächst ein außerordentlich unbehagliches Gefühl. Er empfindet etwas, was ihn erinnert an man- ches nebelhaft Mystische, an Überhitztes im menschlichen Seelenleben, das nicht zu solchen Begriffen kommt, die sich äußerlich durch irgend etwas restlos belegen lassen, sondern die nur innerlich erlebt werden können.",
      "Er empfindet das vollständig Unbestimmte des mystischen Erlebens, aber er findet auch, daß Solowjew sich durch- aus derjenigen Begriffsformen und Ausdrucksmittel be- dient, die wir kennen, Hegelscher, Humescher, Millscher, sogar solcher, die spencerisch sind - aber nur als Illu- stration. So kann man durchaus sagen, daß er nicht im Nebulosen stehenbleibt, sondern daß er durch die Art, wie er das Religiöse als Wissenschaft behandelt, wie er es in allem sucht und als Philosophie entfaltet, durchaus an den philosophischen Begriffsentwicklungen des Westens gemessen und kritisiert werden kann.",
      "So sehen wir uns heute vor der Situation: Im Westen das Bestreben, aus der Naturwissenschaft heraus eine Weltanschauung zu gewinnen, das Naturwissenschaft- liche auf die eine Seite zu stellen, das Geistige auf die andere Seite, und in der Mitte zu ringen mit dem Pro- blem, die Brücke zwischen beiden zu schlagen und das in den unbestimmten Ausdrücken, die Hegel gebraucht hat: «Die Natur ist der Geist in seinem Anderssein», «Der Geist ist der Begriff, wenn er wieder zu sich zu- rückgekehrt ist». In allen diesen stammelnden Ausdrük- ken liegt die Tragik, daß Hegel nur an der Pflege des 66 abstrakten Gedankens das erleben konnte, nach dem er eigentlich strebte.",
      "Und dann sehen wir im Osten, bei Solowjew, etwa die Art noch bewahrt, wie wohl die Kirchenväter in bezug auf Philosophie geredet haben mochten vor dem Konzil zu Nicäa. Er versetzt uns vollständig zurück in die drei ersten nachchristlichen Jahrhunderte des Abendlandes.",
      "So haben wir im Osten ein Erleben der geistigen Welt, das sich noch nicht auf- schwingen kann zu selbsteigenen begrifflichen Formu- lierungen, das die westlichen Formulierungen, die west- lichen Begriffe gebraucht, um sich auszusprechen, und dem daher die Formulierungen etwas Unbestimmtes, sogar etwas Aufgedrängtes, Fremdes bleiben. So sehen wir also, wie in dreifacher Art das philo- sophische Weltbild sich entfaltet hat.",
      "Und indem wir verfolgen, wie diese dreifache Art eines philosophi- schen Weltbildes aus den Charakteren und Anlagen der Menschheit des Westens, der Mitte und des Ostens her- vorgeht, können wir sehen, daß es uns heute obliegen muß da doch Wissenschaft als etwas Einheitliches sich über die ganze Menschheit ausbreiten muß -, etwas zu finden, was sich erheben kann über diese verschiedenen philosophischen Aspekte, die im Grunde genommen doch noch aus denjenigen Elementen hervorgehen, wo die Philosophie noch eine menschlich-persönliche An- gelegenheit war. Wir sehen heute: Auf verschiedene Art lieben der Westen, die Mitte von Europa und der Osten die Weisheit.",
      "Wir begreifen, daß in älteren Zeiten die Philosophie noch da sein konnte als eine innere Seelen- verfassung. Jetzt aber, in der neueren Zeit, wo sich die Menschen so stark differenziert haben, kommt diese Art, die Weisheit zu lieben, in mannigfaltigen Weisen zum Ausdruck.",
      "Und vielleicht können wir gerade daran er- 67 kennen, was wir selber zu tun haben, insbesondere, was wir in der Mitte zu tun haben, wo ja das Problem am tragischsten und intensivsten aufgeworfen ist, wenn dies auch heute noch nicht in der gleichen Art vor allen philosophischen Gemütern steht. Wenn ich das bildlich zusammenfassen soll, was ich ausgeführt habe, so möchte ich sagen: In Solowjew spricht philosophisch gesehen der alte Priester, der in höheren Welten lebte und eine Art innerer Fähigkeiten zu ent- wickeln hatte, in diesen höheren Welten zu leben; prie- sterliche Sprache, nur ins Philosophische umgesetzt, fühlt man überall bei Solowjew.",
      "Im Westen, bei Herbert Spencer, spricht der Weltmann, der sich in die Lebens- praxis hineinschicken will, der - wie es ja aus der darwi- nistischen Theorie hervorgehen kann - die Wissenschaft so ausbilden will, daß sie die praktische Lebensgrund- lage ergeben kann. In der Mitte haben wir weder den Weltmann noch den Priester; Fichte, Schelling, Hegel, sie sind keine priesterlichen Naturen wie etwa Solowjew.",
      "In der Mitte haben wir den Lehrer, den Volkspädagogen, und zwar auch da, wo die deutsche Philosophie etwa hervorgegangen ist aus der religiösen Vertiefung; da ist der Pastor wiederum zum Lehrer geworden. Das Lehr- hafte haftet auch der Hegeischen Philosophie an.",
      "Und wir sehen in der neuesten Zeit - etwa bei Oswald Külpe -, wie die Sache so geworden ist, daß nun die Philosophie, als man sie eigentlich schon verloren hatte, nichts mehr ist als eine Zusammenfassung dessen, was die einzelnen Wissenschaften geben. Man fragt bei der unorganischen Naturwissenschaft: was kommen da für Begriffe hervor?, man fragt bei der organischen Natur- wissenschaft: was kommen da für Begriffe hervor?, bei der Geschichte, bei der Religionswissenschaft ebenso, 68 und so weiter.",
      "Man sammelt diese Begriffe und bildet damit äußerlich abstrakt eine Einheit. Ich möchte sagen, was Gegenstand der Lehre in den einzelnen Wissen- schaften ist, soll eine Gesamtlehre bilden. Das ist es, wozu im Grunde genommen die Wissenschaft in der Mitte nach der ganzen Veranlagung der Menschen gelan- gen mußte.",
      "Blicken wir zurück auf das, was da geworden ist, so sehen wir: Bei Herbert Spencer der unbedingte Glaube an die Naturwissenschaft, der Glaube, festhalten zu müssen an dem, was Beobachtung, Experiment und der reflektierende Verstand, der sich über Beobachtung und Experiment hermacht, erleben können; und man täuscht sich darüber hinweg, welcher Widerspruch darin liegt, wenn man die so gewonnenen Begriffe hinauftragen will bis in den sozialen Organismus, und obwohl dieser das allerwichtigste Charakteristikon des natürlichen Orga- nismus, das Sensorium, nicht hat - ihn dennoch erfassen will mit denselben Begriffen, die im natürlichen Dasein sich ergeben. Wir sehen die Hinneigung zu dem Natur- wissenschaftlichen so stark, daß Charaktere möglich geworden sind, die - wie Newton - einseitig festhalten an dem Mechanistischen und ihre Seelenbedürfnisse ab- seits davon befriedigen.",
      "Newton hat ja bekanntlich in ganz einseitig mystischer Weise die Apokalypse zu er- klären versucht; also neben seiner wissenschaftlichen Weltauffassung hatte er seine eigenen mystischen Be- dürfnisse. Sehen wir uns zum Beispiel an, was da als Naturwis- senschaft aufgetreten und nach und nach im Laufe des 19.",
      "Jahrhunderts unbewußt in der europäischen Mitte übernommen worden ist; denn man hat in der europä- ischen Mitte die Wissenschaft einfach nach dem Muster 69 dessen ausgebildet, was westliches naturwissenschaft- liches Denken war. Man merkte das nicht, aber man bildete dennoch alles Weltanschauungsdenken nach dem Muster des Westens aus.",
      "Wie wild wurden die Leute, wenn irgend jemand einmal versuchte, die Goethesche Denkweise in der Physik gegenüber der Newtonschen in Schutz zu nehmen! - Und wie verlief die Entwicklung in der Biologie? Goethe hat eine Organik begründet, zu der ein Einleben in Begriffe in mathematischer Art notwen- dig ist.",
      "Die Zeit drängt, eine Biologie zu gewinnen, die dem modernen Denken angemessener ist als das, was aus alten Zeiten heraufgekommen ist. Aber der weitere Fort- schritt im 19. Jahrhundert hat einmal für Mitteleuropa nicht die Goethesche Biologie angenommen, sondern die des Darwinismus, der von Begriffen durchsetzt ist, die gegenüber den Goetheschen sich so ausnehmen wie die Begriffe des 16.",
      "Jahrhunderts gegenüber denen des 18. Jahrhunderts. Einzig und allein in Mitteleuropa hatten sich einmal die Begriffe fortgebildet; im Westen ist man bei denjenigen Begriffen geblieben, die ausreichten für das Naturbegreifen.",
      "So kommt es, daß gewisse Begriffe im Westen einfach nicht vorhanden sind und daß sie, als man in Mitteleuropa das westliche Denken übernommen hat, einfach verlorengingen. Zum Beispiel der Gedanke, der lebendige Gedanke, der Begriff des Erfassens einer Wirklichkeit, abgesondert von einem Empirischen, wie er bei Hegel zum Vorschein gekommen ist, ist einfach in Mitteleuropa heute nicht vorhanden; er ging deshalb verloren, weil das mitteleuropäische Denken vom west- lichen Denken überflutet worden ist.",
      "So haben wir in Mitteleuropa die Aufgabe, hinzu- schauen auf das, was naturwissenschaftliche Denkweise sein kann. Dem Anthroposophen wird es übel genom- 70 men, wenn er diese naturwissenschaftliche Denkweise mit ebensolcher Liebe pflegt wie der Naturforscher sel- ber.",
      "Nichts, gar nichts soll gegen die naturwissenschaft- liche Denkweise von mir gesagt werden; es ist nur ein Mißverständnis, wenn man dies glaubt. Aber ich muß naturwissenschaftliche Denkweise eben in ihrer Reinheit sehen und dann auch versuchen, sie in ihrer Reinheit zu charakterisieren.",
      "Und da stellen sich für den, der unbe- fangen der naturwissenschaftlichen Denkweise gegen- übersteht, die Dinge, die diese selbst darstellt - so wie etwa die westlichen Forscher sie dargestellt haben, wie es Haeckel in einer genialen Weise getan hat -, da stellen sich diese Ergebnisse westlicher Forschungsart, wenn man sie so läßt und nicht philosophisch umdeutet, nicht als Lösungen, nicht als Antworten dar, sondern sie stellen sich überall als Fragen dar. Die ganze Naturwissenschaft wird nach und nach für den Unbefangenen nicht zu einer Antwort auf Fragen, sondern sie wird zur großen Wel- tenfrage selbst.",
      "Überall empfindet man: Was gerade in der schönsten Weise durch diese Naturwissenschaft er- forscht wird - meinetwillen bis zur Atomtheorie, die ich auch nicht negiere, sondern nur an ihren richtigen Platz stellen will , das alles wird zu Fragen, und aus dem Westen spricht eine große Fragestellung zu uns. Woher rührt diese Fragestellung?",
      "Wenn wir den Blick in die Außenwelt lenken und uns bloß der Wahrnehmung des Gegebenen zuwenden, so haben wir darin keine volle Wirklichkeit. Wir werden als Menschen hineingeboren in die Welt, sind so konstitu- iert, wie wir es schon einmal sind, nehmen einen Teil der Wirklichkeit für unsere Anschauung in unser eigenes Innere herein, schauen dann die Außenwelt, das Sinnlich- Gegebene an - und es fehlt uns in unserer Anschauung 71 derjenige Teil der Wirklichkeit, der in uns lebt, den wir nur durch menschliches Ringen verbinden können mit der ändern halben Wirklichkeit, die uns von außen ent- gegenschaut.",
      "Blicken wir nach dem Westen, so sehen wir dort die halbe Wirklichkeit mit besonderer Hingebung erforscht; aber sie liefert nur eine Summe von Fragen, weil sie halbe Wirklichkeit ist. So tritt uns auf der einen Seite die eine Hälfte der Wirklichkeit, das Gegebene entgegen; schaut man es richtig an, so wird es zur Frage.",
      "In Mitteleuropa empfand man das Fragenhafte, das die westliche Denkweise geben kann, und man versuchte durchzustoßen bis zum Gedanken. Das ist die Hegeische Philosophie. Im Osten empfand man das, was über dem Gedanken lebt, was zum Gedanken hinunterwirkt; aber man kam nicht dazu, es selbst so weit zum Leben zu erwecken, daß sozusagen das Fleisch auch ein Knochensystem er- hielt.",
      "Solowjew war fähig, in seiner Philosophie Fleisch, Muskeln, auch Blut zu entwickeln - aber das Knochen- gerüst fehlt. Und daher nahm er die Hegeischen Begriffe, die Humeschen und andere und bildete damit dem, was er zu sagen hatte, ein fremdes Knochensystem ein.",
      "Erst wenn man in der Lage ist, nicht mehr ein fremdes Kno- chensystem zu gebrauchen, dann verwandelt sich das, was im Geistigen erlebt werden kann. So aber, wie es etwa bei Solowjew auftritt, führt es ein schattenhaftes Dasein, weil es sich nicht zum Knochensystem durchbil- den und dadurch anschaulich werden kann.",
      "Wenn man dabei nicht stehenbleiben will, sich nur äußerlich ein Knochensystem zu entwickeln, sondern in der Geistig- keit lebt und sich vorbereitet durch starke geistige Ar- beit, dann entwickelt man für das geistige Erleben selbst das innere Knochensystem, man entwickelt die Begriffe, 72 die man dazu braucht. Dazu sollen jene Übungen sein, die zum Beispiel in meinen Schriften «Geheimwissen- schaft», «Wie erlangt man Erkenntnisse der höheren Welten?» und anderen gegeben sind.",
      "Da entwickelt man das, was nun wirklich zu einem inneren Begriffsorga- nismus werden kann. Das ist dann die andere Seite der Wirklichkeit, und diese Seite der Wirklichkeit hat ihre Keime in der östlichen Philosophie Solowjews.",
      "In Mitteleuropa gab es immer nur das große Problem: zwischen Natur und Geist die Brücke zu schlagen. Es ist für uns zu gleicher Zeit ein bedeutsames historisches Problem geworden: die Brücke zu schlagen zwischen West und Ost, und diese Aufgabe muß heute vor uns stehen in der Philosophie.",
      "Diese Aufgabe führt aber zugleich hinein in die Anthroposophie. Wird die An- throposophie innerlich fähig, sich selber in dem Gedan- kenerleben lebendige Gestalt zu geben, dann darf sie auch auf der anderen Seite ganz materialistisch die natürliche Wirklichkeit erleben, wie man sie im Westen erlebt; denn dann wird nicht durch abstrakte Begriffe, sondern im lebendigen Wissenschaftsringen die Brücke gebaut zwischen dem bloßen Glauben und dem Wissen, zwischen dem Erkennen und der subjektiven Gewißheit.",
      "Dann wird aus der Philosophie eine wirkliche Anthro- posophie entwickelt, und die Philosophie kann jederzeit von dieser lebendigen Wissenschaft befruchtet werden. Das wird die Hegeische Philosophie erst wieder zum Leben erwecken können, wenn ihr durch das anthro- posophische Erleben Lebensblut geistiger Art zugeführt wird.",
      "Dann wird nicht mehr eine Logik dastehen, die so abstrakt ist, daß sie nicht der «Geist jenseits der Natur» sein kann, wie Hegel wollte, sondern daß sie das wirklich sein kann, indem dann nicht der abstrakte, 73 sondern der lebendige Geist von der Philosophie erfaßt wird. Das gab der Anthroposophie zunächst die Aufgabe, zu untersuchen: Wie muß gemäß unserem heutigen Standpunkte, der nun wiederum Jahrzehnte hinter He- gel liegt, die Brücke geschlagen werden zwischen dem, was wir Wahrheit nennen auf der einen Seite, die die volle Wirklichkeit umfassen muß, und dem, was wir Wissenschaft nennen auf der anderen Seite, die nun auch die volle Wirklichkeit umfassen muß.",
      "Kurz, es mußte das Problem gestellt werden - und das ist das wichtigste aus der Anthroposophie hervorgehende philosophische Problem: Welches ist die Beziehung zwischen Wahrheit und Wissenschaft? Dieses Problem möchte ich in der Einleitung heute an die Spitze derjenigen Betrachtung gestellt haben, von der ich glaube, daß sie nun folgen wird. 74"
    ],
    "sentences": [
      [
        "Meine sehr verehrten Anwesenden!",
        "Es ist immer schwer, wenn man mit einem ernsten wissenschaftlichen Gewis- sen den überkommenen Ausdruck «Logos» in irgendei- ne der neueren Sprachen übersetzen will.",
        "Wir sagen ja, wenn wir «Logos» übersetzen, gewöhnlich «Wort», wie das für die Bibel üblich ist."
      ],
      [
        "Wir denken aber, wenn wir zum Beispiel die «Logik» im Sinne haben, nicht so sehr an das «Wort», sondern wir denken dann an den «Ge- danken», wie er in den menschlichen Individuen wirkt und seine Gesetzmäßigkeiten hat.",
        "Doch wenn -wir von «Philologie» reden, so haben wir wiederum das Bewußt- sein: Wir entwickeln eine Wissenschaft, die sich auf das Wort bezieht."
      ],
      [
        "Ich möchte sagen: Gerade heute ist das, was nach neuerem Sprachgebrauch in dem Wort «Logos» enthalten ist, im Grunde genommen in allem Philoso- phischen drinnen.",
        "Und wenn wir von «Philosophie» sprechen, dann können wir in dem, was wir dabei nicht so sehr definieren als erleben, gar wohl empfinden, wie ein Abglanz dieses unbestimmten Erlebnisses gegenüber dem Logos in all dem enthalten ist, was wir bei «Philo- sophie» fühlen."
      ],
      [
        "Philosophie deutet ja dem Wortlaute nach - was aber zweifellos damals, als Philosophie entstand, etwas mehr als nur Wortlaut war -, deutet ja auf ein ganz bestimm- tes inneres Erlebnis des Menschen; das Wort Philo- 54 sophie deutet darauf, daß der Mensch an dem, was dem Logos verwandt ist, «Sophia», ein bestimmtes, man möchte sagen, wenn auch nicht ein persönliches, so doch ein allgemein menschliches Interesse hat.",
        "Es deutet das Wort Philosophie weniger unmittelbar auf den Besitz eines Wissenschaftlichen hin, als auf ein inneres Verhalten des Menschen zu dem weisheitsvollen Inhalt des Wis- senschaftlichen."
      ],
      [
        "Da unser Gefühl gegenüber der Philo- sophie heute nicht mehr so ganz sicher ist wie in den Zeiten, als Philosophie auf der einen Seite fast zusam- menfiel mit, ich will nicht sagen mit Wissenschaft, aber mit wissenschaftlichem Streben, und auf der anderen Seite etwas war, was auf ein inneres menschliches Ver- halten hindeutete, haben wir heute ein außerordentlich unbestimmtes Erlebnis, wenn wir von Philosophie spre- chen oder uns in Philosophie betätigen.",
        "Dieses unbe- stimmte Erlebnis ist aber außerordentlich schwer aus den Tiefen des Bewußtseins heraufzuheben, wenn man das auf eine bloß dialektische oder auch äußerlich defi- nierende Weise versucht, und nicht einzugehen versucht auf das, was gegenüber der Philosophie menschliches Erleben im Laufe der geschichtlichen Entwicklung war."
      ],
      [
        "Zu einer solchen Betrachtung fordert ja die Gegenwart ganz besonders heraus.",
        "Blicken wir als mitteleuropäische Menschen um eini- ge Jahrzehnte zurück, so war eigentlich das Hineinleben in die Philosophie für den Menschen, der ein solches Einleben suchte, gerade in Mitteleuropa noch etwas an- deres, als es heute im zweiten Jahrzehnt des 20."
      ],
      [
        "Jahrhun- derts ist, wo wir ja im Grunde genommen nicht nur äußerlich physisch, sondern gerade geistig wirklich so viel durchlebt haben, wie früher - man darf das ruhig aussprechen - in Jahrhunderten erlebt worden ist.",
        "Und 55 wenn man zurückblickt auf die Erlebnisse, die ein - wenn ich mich des pedantisch-philiströsen Ausdruckes bedienen darf - Philosophie-Beflissener so in den 50er, 60er, 70er Jahren des 19."
      ],
      [
        "Jahrhunderts, vielleicht auch noch später, als Mitteleuropäer haben konnte, so sind es im wesentlichen diese: Man blickte zurück auf die Blüte- zeit deutscher philosophischer Entwicklung, man blickte zurück auf die große Philosophenzeit Fichtes, Schellings, Hegels; man hatte um sich eine gebildete und gelehrte Welt, welche diese Philosophenzeit als etwas durchaus Abgetanes betrachtete und welche in der heraufkom- menden naturwissenschaftlichen Weltanschauung dasje- nige sah, was an die Stelle früherer philosophischer Be- trachtungen treten sollte.",
        "Man bewunderte die Größe der Gedankenerhebung, wie sie bei einem Schelling hervortrat, man bewunderte die Energie und die Kraft Fichtescher Gedankenentwicklung, man hatte vielleicht auch ein Gefühl für das rein Umfassende, Scharfsinnige Hegeischen Denkens, aber man betrachtete mehr oder weniger dieses klassische Zeitalter deutscher Philosophie doch als etwas Überwundenes."
      ],
      [
        "Und daneben gab es dann die Bestrebung, aus der Naturwissenschaft heraus etwas zu entwickeln, was eine allgemeine Weltanschauung werden sollte, von den Be- strebungen der «Kraft- und Stoff-Menschen» bis zu den- jenigen, die vorsichtiger aus naturwissenschaftlichen Begriffen heraus zu einer philosophischen Weltanschau- ung kommen wollten, die aber die ehemalige idealisti- sche Philosophie eben ablehnten.",
        "Es gab alle Nuancen von Denken und Forschen auf diesem Gebiete."
      ],
      [
        "Und dann gab es eine dritte Sorte von Denkern auf diesem Gebiete, die konnten nicht mitgehen mit dem bloßen naturwissenschaftlichen Begründen einer Welt- 56 anschauung, aber sie konnten auf der anderen Seite auch wieder nicht hineintauchen in das real Gedankliche, wie es etwa bei Hegel gegeben ist.",
        "Für diese entstand die große Frage: Wie kann sich der Mensch mit seinem Denken, das er als etwas ausbildet, das nur in ihm selber liegt, in ein Verhältnis zur Objektivität, zur Außenwelt setzen?"
      ],
      [
        "Es waren die Erkenntnistheoretiker der ver- schiedenen Nuancen, welche in dem Ruf «zurück zu Kant» übereinstimmten, aber diesen Weg zu Kant in der verschiedensten Weise einschlugen; es waren scharfsin- nige Denker wie etwa Liebmann, Volkelt und so weiter, die aber im Grunde genommen doch innerhalb des Er- kenntnistheoretischen blieben und nicht über die Frage hinauskamen: Wie soll der Mensch mit dem, was er gedanklich, vorstellungsgemäß in sich trägt, die Brücke schlagen zu einer transsubjektiven, außerhalb des Men- schen bestehenden Realität?",
        "Was ich Ihnen hier als eine Situation schildere, die der Philosophie-Beflissene etwa im letzten Drittel des 19."
      ],
      [
        "Jahrhunderts vorfand, hat zu keinerlei Art von Lösung geführt.",
        "Das war gewissermaßen die Mitte eines Dramas oder irgendeines in der Zeit verlaufenden Kunstwerkes, zu dem kein Ende hinzugefunden worden ist."
      ],
      [
        "Es liefen diese Bestrebungen mehr oder weniger ins Unbestimmte aus.",
        "Sie liefen aus in eine große Anzahl von Fragen, und überall fehlte im Grunde genommen der Mut, gegenüber diesen Fragen auch nur das Streben nach Lösungsversu- chen zu entwickeln."
      ],
      [
        "Heute nimmt sich die Situation in der ganzen philo- sophischen Welt so aus, daß man sie gar nicht mehr so schildern kann, wie ich jetzt eben die Situation vom letzten Drittel des 19.",
        "Jahrhunderts dargestellt habe, wenn man die Wirklichkeit treffen will."
      ],
      [
        "Heute sind vor 57 unserem Blick philosophische Gesichtspunkte aufge- taucht, welche, ich möchte sagen, aus ganz anderen Untergründen emporgestiegen sind, und die notwendig machen, daß wir heute die philosophische Situation in einer ganz anderen Weise charakterisieren.",
        "Heute tritt, wenn wir die philosophische Situation charakterisieren wollen, scharf vor unser Seelenauge dasjenige, wofür ja unser Blick im zweiten Jahrzehnt des 20."
      ],
      [
        "Jahrhunderts so sehr geschärft werden konnte, nämlich die vonein- ander so stark differierenden philosophischen Weltan- schauungen des Westens, der europäischen Mitte und des europäischen Ostens.",
        "Heute steht in einer anderen Weise als noch vor kurzer Zeit vor unserem gefühlsmä- ßigen Erleben des Philosophischen das, was sich etwa aussprechen kann in den drei Namen: Herbert Spencer - Hegel - Wladimir Solowjew."
      ],
      [
        "Indem wir diese drei Per- sönlichkeiten vor uns hinstellen, haben wir in ihnen die Repräsentanten dessen, was heute die philosophische Situation charakterisieren kann.",
        "Innerlich war das ge- wissermaßen schon immer oder seit langer Zeit der Fall, aber es tritt erst heute die philosophische Situation so charakteristisch vor unser Seelenauge."
      ],
      [
        "Sehen wir uns einmal den Westen an: Herbert Spen- cer.",
        "Ich müßte natürlich, wenn ich vollständig sein wollte, den ganzen Hergang der philosophischen Entwicklung schildern, wie er von Bacon, Locke über Mill zu Spencer geführt hat; doch das kann heute nicht meine Aufgabe sein."
      ],
      [
        "In Herbert Spencer tritt uns eine Persönlichkeit entgegen, welche Philosophie begründen will, aber Phi- losophie begründen will rein aus Begriffssystemen her- aus, die an der Naturwissenschaft gewonnen sind.",
        "Wir finden in Spencer eine Persönlichkeit, die zu dem Na- turwissenschaftlichen restlos Ja sagt, und die aus diesem 58 Jasagen heraus die Konsequenz zieht: Also muß alles philosophische Denken über die Welt aus diesem Na- turwissenschaftlichen gewonnen werden."
      ],
      [
        "So sehen wir, wie Spencer sucht, in der Naturwissenschaft gewisse Vorgänge in Begriffe zu fassen, zum Beispiel wie ein fortwährendes Sichzusammenziehen und Sichausbreiten der Stoffe stattfindet, ein Differenzieren und Konsoli- dieren.",
        "Er beobachtet das zum Beispiel an der Pflanze, die in den Blättern sich ausbreitet und sich im Keime zusammenzieht, und er versucht, solche Begriffe dann m klare naturwissenschaftliche Formen zu bringen und damit eine Weltanschauung aufzubauen."
      ],
      [
        "Und er versucht sogar, die menschliche Gesellschaft selber, den sozialen Organismus, nur so zu denken, daß dieses Denken eine Analogie bietet zu dem natürlichen Organismus.",
        "Da kommt er aber sogleich in die Enge."
      ],
      [
        "Der natürliche Organismus des Menschen ist gebunden an den Zusam- menfluß alles dessen, wodurch dieser Organismus mit der Außenwelt in ein Verhältnis tritt, durch Wahrneh- mungen, durch Vorstellungen und so weiter.",
        "Der einzelne natürliche Organismus ist gebunden an das, was sich unter dem Einfluß des Sensoriums entwickeln kann."
      ],
      [
        "In dem gesellschaftlichen Organismus findet Herbert Spencer ein solches Sensorium nicht, kein irgendwie zentral zusammenlaufendes Nervensystem.",
        "Dennoch konstruiert er einen solchen gesellschaftlichen Organis- mus und findet darin gewissermaßen die Krönung seines philosophischen Gebäudes, das ganz auf Naturwissen- schaft aufgebaut ist."
      ],
      [
        "Was liegt damit eigentlich in diesem Westen vor?",
        "Da liegt vor, daß dort gerade der naturwissenschaftliche Gedanke in seiner vollen, seiner berechtigten Einseitig- keit sich entwickelt hat.",
        "Da liegt vor, daß aus den ur- 59 sprünglichen Völkeranlagen heraus feinste Beobach- tungsgabe und Experimentiertalent sich entwickelt ha- ben."
      ],
      [
        "Da liegt vor, daß ein Interesse vorhanden ist, die Welt des äußerlich Sinnlich-Wirklichen in den kleinsten Einzelheiten zu beobachten, ohne dabei etwa ungedul- dig zu werden und aufsteigen zu wollen zu irgendwelchen zusammenfassenden Begriffen.",
        "Da liegt aber auch vor ein Hang, mit der Wissenschaft stehenzubleiben innerhalb dieser äußeren sinnlichen Tatsachenwelt."
      ],
      [
        "Da liegt das vor, was ich nennen möchte: eine Art Furcht davor, von der Sinneswelt irgendwie zu einem Zusammenfassenden aufzusteigen.",
        "Da aber der Mensch doch nicht anders kann, als zu leben in etwas, was auch über die Sinneswelt hinausgeht, was dem Menschen nicht einfach durch die Sinne gegeben wird, so tritt hier im Westen die Er- scheinung hervor, daß die gesamte geistige Welt restlos übergeben sein soll dem individuellen Glauben des ein- zelnen, und daß dieser Glaube frei von allem wissen- schaftlichen Einfluß sich entwickeln soll."
      ],
      [
        "Was Inhalt des Religiösen ist, das will sich der Mensch nicht antasten lassen von dem, was er wissenschaftlich erkundet.",
        "So sehen wir, daß bei Herbert Spencer, der in seiner Art ganz konsequent die naturwissenschaftliche Denkweise heraufführt bis in die Soziologie hinein, streng [getrennt] vorhanden ist, auf der einen Seite die Wissenschaft, die ganz naturwissenschaftlich verlaufen soll, und auf der anderen Seite für den Menschen ein geistiger Inhalt, mit dem Wissenschaft sich nichts zu schaffen machen soll."
      ],
      [
        "Gehen wir nun von Herbert Spencer zu dem, was uns bei Hegel entgegentritt.",
        "Es verschlägt nichts, daß Hegel, der dem ersten Drittel des 19.",
        "Jahrhunderts angehörte, im zweiten Drittel für das mitteleuropäische Philoso- phieren mehr oder weniger als überwunden galt, denn 60 was für Mitteleuropa charakteristisch ist, das ist doch am bedeutsamsten gerade bei Hegel zum Vorschein gekom- men."
      ],
      [
        "Sehen wir uns Hegel an: Schon in seiner, ich möchte sagen, gefühlsmäßigen Veranlagung liegt eine gewisse Abneigung gegen diese universalistische naturwissen- schaftliche Art, mit der Weltanschauung so zu verfah- ren, wie sie im Westen ausgestaltet wird durch Herbert Spencer, aber sich selbstverständlich vorbereitet hat durch dessen Vorgänger, sowohl die Naturforscher wie auch die Philosophen.",
        "Wir sehen bei Hegel, wie er zum Bei- spiel Newton nicht leiden kann, wie ihm die besondere Art, das Weltall nur mechanistisch zu denken, unsym- pathisch ist, wie er Newton ablehnt nicht etwa bloß in bezug auf die Farbenlehre, sondern auch als Interpreten des Kosmos."
      ],
      [
        "Hegel gibt sich Mühe, zu den Keplerschen Formeln über die Planetenbewegungen zurückzukeh- ren; er analysiert die Keplerschen Formeln über die Planetenbewegungen und findet für sich, daß Newton eigentlich gar nichts hinzugefügt hat, sondern daß in den Keplerschen Formeln schon das ganze Gravitationsge- setz drinnenliegt.",
        "Und das übernimmt er aus dem Grunde, weil er aus dem, was bei Kepler mehr aus geistigem Erleben kommt, ein wissenschaftliches Denken hervor- gehen sieht, das umfassend ist und das das äußere Natur- wissenschaftliche vom Geiste aus begreiflich zu machen versucht."
      ],
      [
        "Kepler ist für Hegel einfach die Persönlichkeit, die imstande ist, in den Geist auch mit dem Denken einzudringen und eine Brücke zu schlagen zwischen dem, was wissenschaftlich erkannt wird, und dem, was nach der Meinung des Westens bloß geglaubt werden soll, der also imstande ist, die Wissenschaft heraufzutra- gen in das Gebiet, das für den Westen vermeintliches Gebiet des Glaubens ist. 61 Aus diesem Grunde lehnt Hegel, ganz im Einklang mit Goethe, die Newtonsche Farbenlehre streng ab.",
        "Überall sehen wir in der Hegeischen Anlage eine Art Antipathie gegen das, was bei Newton aus dessen An- lagen heraus ganz natürlich ist."
      ],
      [
        "Dafür ist bei Hegel ein entschiedenes Talent vorhanden, ganz in dem Gedank- lichen selber zu leben.",
        "Für Hegel war das einfach selbst- verständlich, was Goethe gegenüber Schiller sagte: «Ich sehe meine Ideen mit Augen»."
      ],
      [
        "Das ist scheinbar eine Naivität, allein, solche Naivitäten nehmen sich oftmals, richtig betrachtet, als die tiefste philosophische Weisheit aus.",
        "Hegel würde einfach nicht verstanden haben, -wie man behaupten könne, die Idee des Dreiecks sei nicht zu fassen, denn Hegels Leben verlief eigentlich ganz - wenn ich mich so ausdrücken darf auf dem Plan des Gedan- kens."
      ],
      [
        "Für ihn war auch eine höhere Offenbarungswelt, eine Welt höherer Geistigkeit dadurch vorhanden, daß sie gewissermaßen ihre Schattenbilder auf eine Fläche wirft, die von Gedanken ausgefüllt ist.",
        "Von oben her wirft die geistige Welt ihre Schattenbilder auf die Fläche der menschlichen Seele, auf der der menschliche Gedan- ke sich entwickelt."
      ],
      [
        "Dadurch kommt für Hegel der Begriff des höheren Geistigen zustande, daß es auf der Fläche der Seele sich abschattet als Gedanken.",
        "Hegel ist dazu veranlagt, diese Gedanken voll als Geistiges zu erleben, und er erlebt auch das natürliche Geschehen nicht in seiner elementaren Gegenwart, sondern sieht es in den Gedankenbildern, die es auf die Fläche der Seele gewor- fen hat."
      ],
      [
        "So wird es in Hegels Philosophie zur Unmöglich- keit, in jener äußerlichen Weise Wissen und Glauben voneinander zu trennen, wie es dem Westen ganz natürlich ist.",
        "Für Hegel wird zur Lebensaufgabe die 62 Vereinigung der geistigen Welt, die der Westen einfach aus seinen Anlagen heraus in das bloße Glaubensgebiet verweisen will, mit der sinnlich-physischen Welt, zu einer solchen Welt, von der man wissen kann."
      ],
      [
        "Hier ist nicht mehr Wissen auf der einen Seite, Glauben auf der anderen Seite; hier ist der Menschenseele das große, bedeutsame Problem gestellt: Wie findet man im in- neren Erleben selbst die Brücke zwischen Glauben und Wissen, zwischen Geist und Natur?",
        "Aber es war gewissermaßen das Tragische in Hegel, daß er das, was er in so grandioser Weise als ein Problem aufzuwerfen verstand, eigentlich nur sah sozusagen in bezug auf die Fläche des Gedankens, daß er zwar die innere Kraft, die innere Lebendigkeit des Gedankens zu erleben verstand, aber vom Inhalte des Gedankens nichts Lebendiges erfassen konnte."
      ],
      [
        "Nehmen Sie die Hegeische Logik: Wiederum zurückgehen will er zum alten Begriff des Logos!",
        "Er fühlt: Wenn wir überhaupt einen realen Begriff vom Logos haben wollen, dann muß der Logos etwas sein, was nicht bloß als ein Gedachtes, sondern als ein real Wirkendes die Welt durchflutet und durchlebt."
      ],
      [
        "Für ihn ist der Logos nicht nur abstrakt- logischer Inhalt, sondern für ihn wird er realer Welt- inhalt.",
        "Sehen wir uns seine «Logik» an, den einen der drei Teile von Hegels Philosophie: Sie enthält nur abstrakte Begriffe!"
      ],
      [
        "Und so steht, so furchtbar ergreifend für den, der mit seinem ganzen Menschen auf die Hegeische Philosophie einzugehen weiß, auf der einen Seite Hegels so grundrichtige Empfindung: Durch das, was in dem Logos erfaßt werden kann, muß eingedrun- gen werden in das schöpferische Prinzip der Welt.",
        "Der Logos muß sein «Gott vor der Erschaffung der Welt» - ein Hegelscher Ausdruck! 63 Dies auf der einen Seite."
      ],
      [
        "Und wie wird auf der ande- ren Seite dieser Logos von Hegel selbst entwickelt?",
        "Er beginnt beim «Sein», kommt zu dem «Nichts», zu dem «Werden», zu dem «Dasein».",
        "Er kommt zu der Kausali- tät, dem Zweck, zu der Teleologie."
      ],
      [
        "Man sehe sich die ganzen Begriffe in der Hegeischen Logik an und frage sich: Ist das dasjenige, was «vor dem Beginn der Schöp- fung als der Inhalt des Göttlichen» da sein konnte?",
        "Es ist abstrakte Logik, Forderung des Schöpferischen, der Logos als Postulat, aber als rein menschliches Gedan- kenpostulat!"
      ],
      [
        "Man empfinde diese Tragik, die darin liegt!",
        "Und man empfinde dann weiter die Tragik, die darin liegt, daß die Hegeische Philosophie als überwunden galt!",
        "Sie enthält aber Momente, aus denen in der Tat neues Leben sprießen kann."
      ],
      [
        "Sie enthält Keime.",
        "Hegel hat sein Heil gesehen in dem: Sein - Nichts - Werden - Dasein.",
        "Wenn aber heute die Leute Hegel zugeführt bekommen, dann sagen sie: Das ist eine alte Schwarte, darauf brauchen wir uns nicht einzulassen. - Wenn man es aber unternimmt, sich durch einen inneren Seelen- prozeß darauf einzulassen, den Begriff innerlich zu er- leben, wie ihn Hegel zu erleben suchte, dann schwinden alle Begriffe von Empirie und Rationalismus, dann wird der Gedanke erfahren und das Erfahrene unmittelbar gedacht."
      ],
      [
        "Da wird der Gedanke zum Erlebnis und das Erlebnis zum reinen Gedanken.",
        "Wer das mitmacht, der empfindet das Bestreben, den Gedanken aus der Ab- straktheit zu erlösen, und die Hegeische Logik als den Keim dazu, daß aus dem Gedanken etwas ganz anderes werden kann, wenn er sich lebendig ausgestaltet."
      ],
      [
        "Mir erscheint oft Hegels Logik als der Keim einer Pflanze, dem man kaum ansieht, was er werden kann, der aber doch die mannigfaltigsten Anlagen in sich trägt.",
        "Und mir 64 scheint, wenn dieser Keim wächst, wenn ihn der Mensch liebevoll pflegt und in den seelischen Boden einsetzt durch anthroposophische Forschung, dann entsteht ge- rade das, daß der Gedanke nicht nur gedacht, sondern als Realität erlebt werden kann."
      ],
      [
        "Da haben wir das Mittel- europäische.",
        "Gehen wir nun zum Osten, so haben wir in Wladimir Solowjew einen Mann vor uns, der wie kein anderer Philosoph dazu berufen ist, immer mehr nun auch ein Inhalt unseres eigenen philosophischen Strebens zu werden, der uns so wichtig werden muß, indem wir seine besondere Charaktereigentümlichkeit auf uns wirken lassen."
      ],
      [
        "Wir sehen in Solowjew zugleich den Repräsen- tanten dessen, was europäisch-östliche Denkweise ist, die aber nicht die orientalisch-asiatische ist.",
        "Solowieff hat ja alles Europäische aufgenommen, er hat es nur in seiner besonderen östlichen Art entwickelt."
      ],
      [
        "Aber was sehen wir da sich entwickeln in bezug auf menschliches wissenschaftliches Streben?",
        "Da sehen wir, wie eigentlich gerade jene Denkweise, auf die der Westen bei Herbert Spencer das meiste gibt, etwas ist, auf das Solowjew im Grunde genommen hinunterschaut, an dem er höchstens die Wahrheiten und Erkenntnisse, die er sucht, sozusa- gen illustriert."
      ],
      [
        "Dagegen ist das, was er auseinandersetzt, ein volles Erleben in der Geistigkeit selbst.",
        "Es tritt bei ihm nicht mit dem vollen Bewußtsein hervor; es tritt mehr atavistisch, unbewußt hervor, aber es ist ein Erle- ben in der Geistigkeit selbst."
      ],
      [
        "Es ist der mehr oder weniger traumhafte Versuch, wissentlich das zu erleben, was der Westen - wiederum ganz bewußt in das Gebiet des Glaubens versetzt.",
        "Und so finden wir im Osten eine Auseinandersetzung mit dem, was in unbestimmter Weise erlebt werden kann, was sich etwa ausnimmt wie ein 65 einseitiges Erleben dessen, zu dem Hegel als der Geistig- keit der Welt von dem natürlichen Dasein aus die Brücke hinüberschlagen wollte."
      ],
      [
        "Vertieft sich heute jemand, der aus mitteleuropä- ischer Geistesbildung hervorgegangen ist, in Solowjew, so hat er zunächst ein außerordentlich unbehagliches Gefühl.",
        "Er empfindet etwas, was ihn erinnert an man- ches nebelhaft Mystische, an Überhitztes im menschlichen Seelenleben, das nicht zu solchen Begriffen kommt, die sich äußerlich durch irgend etwas restlos belegen lassen, sondern die nur innerlich erlebt werden können."
      ],
      [
        "Er empfindet das vollständig Unbestimmte des mystischen Erlebens, aber er findet auch, daß Solowjew sich durch- aus derjenigen Begriffsformen und Ausdrucksmittel be- dient, die wir kennen, Hegelscher, Humescher, Millscher, sogar solcher, die spencerisch sind - aber nur als Illu- stration.",
        "So kann man durchaus sagen, daß er nicht im Nebulosen stehenbleibt, sondern daß er durch die Art, wie er das Religiöse als Wissenschaft behandelt, wie er es in allem sucht und als Philosophie entfaltet, durchaus an den philosophischen Begriffsentwicklungen des Westens gemessen und kritisiert werden kann."
      ],
      [
        "So sehen wir uns heute vor der Situation: Im Westen das Bestreben, aus der Naturwissenschaft heraus eine Weltanschauung zu gewinnen, das Naturwissenschaft- liche auf die eine Seite zu stellen, das Geistige auf die andere Seite, und in der Mitte zu ringen mit dem Pro- blem, die Brücke zwischen beiden zu schlagen und das in den unbestimmten Ausdrücken, die Hegel gebraucht hat: «Die Natur ist der Geist in seinem Anderssein», «Der Geist ist der Begriff, wenn er wieder zu sich zu- rückgekehrt ist».",
        "In allen diesen stammelnden Ausdrük- ken liegt die Tragik, daß Hegel nur an der Pflege des 66 abstrakten Gedankens das erleben konnte, nach dem er eigentlich strebte."
      ],
      [
        "Und dann sehen wir im Osten, bei Solowjew, etwa die Art noch bewahrt, wie wohl die Kirchenväter in bezug auf Philosophie geredet haben mochten vor dem Konzil zu Nicäa.",
        "Er versetzt uns vollständig zurück in die drei ersten nachchristlichen Jahrhunderte des Abendlandes."
      ],
      [
        "So haben wir im Osten ein Erleben der geistigen Welt, das sich noch nicht auf- schwingen kann zu selbsteigenen begrifflichen Formu- lierungen, das die westlichen Formulierungen, die west- lichen Begriffe gebraucht, um sich auszusprechen, und dem daher die Formulierungen etwas Unbestimmtes, sogar etwas Aufgedrängtes, Fremdes bleiben.",
        "So sehen wir also, wie in dreifacher Art das philo- sophische Weltbild sich entfaltet hat."
      ],
      [
        "Und indem wir verfolgen, wie diese dreifache Art eines philosophi- schen Weltbildes aus den Charakteren und Anlagen der Menschheit des Westens, der Mitte und des Ostens her- vorgeht, können wir sehen, daß es uns heute obliegen muß da doch Wissenschaft als etwas Einheitliches sich über die ganze Menschheit ausbreiten muß -, etwas zu finden, was sich erheben kann über diese verschiedenen philosophischen Aspekte, die im Grunde genommen doch noch aus denjenigen Elementen hervorgehen, wo die Philosophie noch eine menschlich-persönliche An- gelegenheit war.",
        "Wir sehen heute: Auf verschiedene Art lieben der Westen, die Mitte von Europa und der Osten die Weisheit."
      ],
      [
        "Wir begreifen, daß in älteren Zeiten die Philosophie noch da sein konnte als eine innere Seelen- verfassung.",
        "Jetzt aber, in der neueren Zeit, wo sich die Menschen so stark differenziert haben, kommt diese Art, die Weisheit zu lieben, in mannigfaltigen Weisen zum Ausdruck."
      ],
      [
        "Und vielleicht können wir gerade daran er- 67 kennen, was wir selber zu tun haben, insbesondere, was wir in der Mitte zu tun haben, wo ja das Problem am tragischsten und intensivsten aufgeworfen ist, wenn dies auch heute noch nicht in der gleichen Art vor allen philosophischen Gemütern steht.",
        "Wenn ich das bildlich zusammenfassen soll, was ich ausgeführt habe, so möchte ich sagen: In Solowjew spricht philosophisch gesehen der alte Priester, der in höheren Welten lebte und eine Art innerer Fähigkeiten zu ent- wickeln hatte, in diesen höheren Welten zu leben; prie- sterliche Sprache, nur ins Philosophische umgesetzt, fühlt man überall bei Solowjew."
      ],
      [
        "Im Westen, bei Herbert Spencer, spricht der Weltmann, der sich in die Lebens- praxis hineinschicken will, der - wie es ja aus der darwi- nistischen Theorie hervorgehen kann - die Wissenschaft so ausbilden will, daß sie die praktische Lebensgrund- lage ergeben kann.",
        "In der Mitte haben wir weder den Weltmann noch den Priester; Fichte, Schelling, Hegel, sie sind keine priesterlichen Naturen wie etwa Solowjew."
      ],
      [
        "In der Mitte haben wir den Lehrer, den Volkspädagogen, und zwar auch da, wo die deutsche Philosophie etwa hervorgegangen ist aus der religiösen Vertiefung; da ist der Pastor wiederum zum Lehrer geworden.",
        "Das Lehr- hafte haftet auch der Hegeischen Philosophie an."
      ],
      [
        "Und wir sehen in der neuesten Zeit - etwa bei Oswald Külpe -, wie die Sache so geworden ist, daß nun die Philosophie, als man sie eigentlich schon verloren hatte, nichts mehr ist als eine Zusammenfassung dessen, was die einzelnen Wissenschaften geben.",
        "Man fragt bei der unorganischen Naturwissenschaft: was kommen da für Begriffe hervor?, man fragt bei der organischen Natur- wissenschaft: was kommen da für Begriffe hervor?, bei der Geschichte, bei der Religionswissenschaft ebenso, 68 und so weiter."
      ],
      [
        "Man sammelt diese Begriffe und bildet damit äußerlich abstrakt eine Einheit.",
        "Ich möchte sagen, was Gegenstand der Lehre in den einzelnen Wissen- schaften ist, soll eine Gesamtlehre bilden.",
        "Das ist es, wozu im Grunde genommen die Wissenschaft in der Mitte nach der ganzen Veranlagung der Menschen gelan- gen mußte."
      ],
      [
        "Blicken wir zurück auf das, was da geworden ist, so sehen wir: Bei Herbert Spencer der unbedingte Glaube an die Naturwissenschaft, der Glaube, festhalten zu müssen an dem, was Beobachtung, Experiment und der reflektierende Verstand, der sich über Beobachtung und Experiment hermacht, erleben können; und man täuscht sich darüber hinweg, welcher Widerspruch darin liegt, wenn man die so gewonnenen Begriffe hinauftragen will bis in den sozialen Organismus, und obwohl dieser das allerwichtigste Charakteristikon des natürlichen Orga- nismus, das Sensorium, nicht hat - ihn dennoch erfassen will mit denselben Begriffen, die im natürlichen Dasein sich ergeben.",
        "Wir sehen die Hinneigung zu dem Natur- wissenschaftlichen so stark, daß Charaktere möglich geworden sind, die - wie Newton - einseitig festhalten an dem Mechanistischen und ihre Seelenbedürfnisse ab- seits davon befriedigen."
      ],
      [
        "Newton hat ja bekanntlich in ganz einseitig mystischer Weise die Apokalypse zu er- klären versucht; also neben seiner wissenschaftlichen Weltauffassung hatte er seine eigenen mystischen Be- dürfnisse.",
        "Sehen wir uns zum Beispiel an, was da als Naturwis- senschaft aufgetreten und nach und nach im Laufe des 19."
      ],
      [
        "Jahrhunderts unbewußt in der europäischen Mitte übernommen worden ist; denn man hat in der europä- ischen Mitte die Wissenschaft einfach nach dem Muster 69 dessen ausgebildet, was westliches naturwissenschaft- liches Denken war.",
        "Man merkte das nicht, aber man bildete dennoch alles Weltanschauungsdenken nach dem Muster des Westens aus."
      ],
      [
        "Wie wild wurden die Leute, wenn irgend jemand einmal versuchte, die Goethesche Denkweise in der Physik gegenüber der Newtonschen in Schutz zu nehmen! - Und wie verlief die Entwicklung in der Biologie?",
        "Goethe hat eine Organik begründet, zu der ein Einleben in Begriffe in mathematischer Art notwen- dig ist."
      ],
      [
        "Die Zeit drängt, eine Biologie zu gewinnen, die dem modernen Denken angemessener ist als das, was aus alten Zeiten heraufgekommen ist.",
        "Aber der weitere Fort- schritt im 19.",
        "Jahrhundert hat einmal für Mitteleuropa nicht die Goethesche Biologie angenommen, sondern die des Darwinismus, der von Begriffen durchsetzt ist, die gegenüber den Goetheschen sich so ausnehmen wie die Begriffe des 16."
      ],
      [
        "Jahrhunderts gegenüber denen des 18.",
        "Jahrhunderts.",
        "Einzig und allein in Mitteleuropa hatten sich einmal die Begriffe fortgebildet; im Westen ist man bei denjenigen Begriffen geblieben, die ausreichten für das Naturbegreifen."
      ],
      [
        "So kommt es, daß gewisse Begriffe im Westen einfach nicht vorhanden sind und daß sie, als man in Mitteleuropa das westliche Denken übernommen hat, einfach verlorengingen.",
        "Zum Beispiel der Gedanke, der lebendige Gedanke, der Begriff des Erfassens einer Wirklichkeit, abgesondert von einem Empirischen, wie er bei Hegel zum Vorschein gekommen ist, ist einfach in Mitteleuropa heute nicht vorhanden; er ging deshalb verloren, weil das mitteleuropäische Denken vom west- lichen Denken überflutet worden ist."
      ],
      [
        "So haben wir in Mitteleuropa die Aufgabe, hinzu- schauen auf das, was naturwissenschaftliche Denkweise sein kann.",
        "Dem Anthroposophen wird es übel genom- 70 men, wenn er diese naturwissenschaftliche Denkweise mit ebensolcher Liebe pflegt wie der Naturforscher sel- ber."
      ],
      [
        "Nichts, gar nichts soll gegen die naturwissenschaft- liche Denkweise von mir gesagt werden; es ist nur ein Mißverständnis, wenn man dies glaubt.",
        "Aber ich muß naturwissenschaftliche Denkweise eben in ihrer Reinheit sehen und dann auch versuchen, sie in ihrer Reinheit zu charakterisieren."
      ],
      [
        "Und da stellen sich für den, der unbe- fangen der naturwissenschaftlichen Denkweise gegen- übersteht, die Dinge, die diese selbst darstellt - so wie etwa die westlichen Forscher sie dargestellt haben, wie es Haeckel in einer genialen Weise getan hat -, da stellen sich diese Ergebnisse westlicher Forschungsart, wenn man sie so läßt und nicht philosophisch umdeutet, nicht als Lösungen, nicht als Antworten dar, sondern sie stellen sich überall als Fragen dar.",
        "Die ganze Naturwissenschaft wird nach und nach für den Unbefangenen nicht zu einer Antwort auf Fragen, sondern sie wird zur großen Wel- tenfrage selbst."
      ],
      [
        "Überall empfindet man: Was gerade in der schönsten Weise durch diese Naturwissenschaft er- forscht wird - meinetwillen bis zur Atomtheorie, die ich auch nicht negiere, sondern nur an ihren richtigen Platz stellen will , das alles wird zu Fragen, und aus dem Westen spricht eine große Fragestellung zu uns.",
        "Woher rührt diese Fragestellung?"
      ],
      [
        "Wenn wir den Blick in die Außenwelt lenken und uns bloß der Wahrnehmung des Gegebenen zuwenden, so haben wir darin keine volle Wirklichkeit.",
        "Wir werden als Menschen hineingeboren in die Welt, sind so konstitu- iert, wie wir es schon einmal sind, nehmen einen Teil der Wirklichkeit für unsere Anschauung in unser eigenes Innere herein, schauen dann die Außenwelt, das Sinnlich- Gegebene an - und es fehlt uns in unserer Anschauung 71 derjenige Teil der Wirklichkeit, der in uns lebt, den wir nur durch menschliches Ringen verbinden können mit der ändern halben Wirklichkeit, die uns von außen ent- gegenschaut."
      ],
      [
        "Blicken wir nach dem Westen, so sehen wir dort die halbe Wirklichkeit mit besonderer Hingebung erforscht; aber sie liefert nur eine Summe von Fragen, weil sie halbe Wirklichkeit ist.",
        "So tritt uns auf der einen Seite die eine Hälfte der Wirklichkeit, das Gegebene entgegen; schaut man es richtig an, so wird es zur Frage."
      ],
      [
        "In Mitteleuropa empfand man das Fragenhafte, das die westliche Denkweise geben kann, und man versuchte durchzustoßen bis zum Gedanken.",
        "Das ist die Hegeische Philosophie.",
        "Im Osten empfand man das, was über dem Gedanken lebt, was zum Gedanken hinunterwirkt; aber man kam nicht dazu, es selbst so weit zum Leben zu erwecken, daß sozusagen das Fleisch auch ein Knochensystem er- hielt."
      ],
      [
        "Solowjew war fähig, in seiner Philosophie Fleisch, Muskeln, auch Blut zu entwickeln - aber das Knochen- gerüst fehlt.",
        "Und daher nahm er die Hegeischen Begriffe, die Humeschen und andere und bildete damit dem, was er zu sagen hatte, ein fremdes Knochensystem ein."
      ],
      [
        "Erst wenn man in der Lage ist, nicht mehr ein fremdes Kno- chensystem zu gebrauchen, dann verwandelt sich das, was im Geistigen erlebt werden kann.",
        "So aber, wie es etwa bei Solowjew auftritt, führt es ein schattenhaftes Dasein, weil es sich nicht zum Knochensystem durchbil- den und dadurch anschaulich werden kann."
      ],
      [
        "Wenn man dabei nicht stehenbleiben will, sich nur äußerlich ein Knochensystem zu entwickeln, sondern in der Geistig- keit lebt und sich vorbereitet durch starke geistige Ar- beit, dann entwickelt man für das geistige Erleben selbst das innere Knochensystem, man entwickelt die Begriffe, 72 die man dazu braucht.",
        "Dazu sollen jene Übungen sein, die zum Beispiel in meinen Schriften «Geheimwissen- schaft», «Wie erlangt man Erkenntnisse der höheren Welten?» und anderen gegeben sind."
      ],
      [
        "Da entwickelt man das, was nun wirklich zu einem inneren Begriffsorga- nismus werden kann.",
        "Das ist dann die andere Seite der Wirklichkeit, und diese Seite der Wirklichkeit hat ihre Keime in der östlichen Philosophie Solowjews."
      ],
      [
        "In Mitteleuropa gab es immer nur das große Problem: zwischen Natur und Geist die Brücke zu schlagen.",
        "Es ist für uns zu gleicher Zeit ein bedeutsames historisches Problem geworden: die Brücke zu schlagen zwischen West und Ost, und diese Aufgabe muß heute vor uns stehen in der Philosophie."
      ],
      [
        "Diese Aufgabe führt aber zugleich hinein in die Anthroposophie.",
        "Wird die An- throposophie innerlich fähig, sich selber in dem Gedan- kenerleben lebendige Gestalt zu geben, dann darf sie auch auf der anderen Seite ganz materialistisch die natürliche Wirklichkeit erleben, wie man sie im Westen erlebt; denn dann wird nicht durch abstrakte Begriffe, sondern im lebendigen Wissenschaftsringen die Brücke gebaut zwischen dem bloßen Glauben und dem Wissen, zwischen dem Erkennen und der subjektiven Gewißheit."
      ],
      [
        "Dann wird aus der Philosophie eine wirkliche Anthro- posophie entwickelt, und die Philosophie kann jederzeit von dieser lebendigen Wissenschaft befruchtet werden.",
        "Das wird die Hegeische Philosophie erst wieder zum Leben erwecken können, wenn ihr durch das anthro- posophische Erleben Lebensblut geistiger Art zugeführt wird."
      ],
      [
        "Dann wird nicht mehr eine Logik dastehen, die so abstrakt ist, daß sie nicht der «Geist jenseits der Natur» sein kann, wie Hegel wollte, sondern daß sie das wirklich sein kann, indem dann nicht der abstrakte, 73 sondern der lebendige Geist von der Philosophie erfaßt wird.",
        "Das gab der Anthroposophie zunächst die Aufgabe, zu untersuchen: Wie muß gemäß unserem heutigen Standpunkte, der nun wiederum Jahrzehnte hinter He- gel liegt, die Brücke geschlagen werden zwischen dem, was wir Wahrheit nennen auf der einen Seite, die die volle Wirklichkeit umfassen muß, und dem, was wir Wissenschaft nennen auf der anderen Seite, die nun auch die volle Wirklichkeit umfassen muß."
      ],
      [
        "Kurz, es mußte das Problem gestellt werden - und das ist das wichtigste aus der Anthroposophie hervorgehende philosophische Problem: Welches ist die Beziehung zwischen Wahrheit und Wissenschaft?",
        "Dieses Problem möchte ich in der Einleitung heute an die Spitze derjenigen Betrachtung gestellt haben, von der ich glaube, daß sie nun folgen wird. 74"
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG ANTHROPOSOPHIE UND ERZIEHUNGSWISSENSCHAFT Berlin, 8. März 1922",
    "paragraphs": [
      "Meine sehr verehrten Anwesenden! Es wird anthroposo- phischer Weltanschauung in begreiflicher Weise immer der Vorwurf gemacht, daß sie ihre Ideen, ihre Ergebnisse verkündet auf der Grundlage von Forschungen, zu de- nen die Fähigkeiten im Menschen erst herangebildet werden müssen, daß also Forschungsergebnisse der An- throposophie nicht von vornherein von jedem nachge- prüft werden können, und daß sie dennoch diese An- schauungen vor den hierauf unvorbereiteten Menschen verkünde.",
      "Doch gerade dieser Vorwurf, so scheinbar berechtigt er ist, gehört zu den aller unberechtigsten, welche der anthroposophischen Bewegung gemacht werden können. Denn es handelt sich bei ihr nicht darum, jeden einzel- nen sofort dazu anzuleiten, ein Forscher im übersinnli- chen Gebiet zu werden, sondern es handelt sich bei ihr darum, ihre Forschungsergebnisse auf eine Weise dar- zulegen, die von jedem einzelnen Menschen nachgeprüft werden kann, einfach durch den gewöhnlichen gesunden Menschenverstand und die gewöhnliche gesunde Logik.",
      "Dies macht allerdings nicht unnötig, daß danach gestrebt wird, wenigstens die ersten Schritte zu übersinnlicher Forschung zu machen, und dafür gibt es ja Anleitungen in den verschiedenen Schriften, die auch hier schon ge- 75 nannt worden sind. Jeder kann also bis zu einem gewis- sen Grade ein anthroposophischer Forscher werden - einfach aus den Zivilisationsbedingungen der Gegenwart heraus -, aber zum Prüfen der Ergebnisse anthroposo- phischer Forschung ist dies nicht nötig, denn diese Prüfung kann einfach aus dem gesunden Menschenver- stand heraus erfolgen.",
      "Und eines der Gebiete, auf denen diese Prüfung wirklich praktisch erfolgen kann, ist das pädagogische Gebiet. Sehr verehrte Anwesende! Anthroposophische Welt- anschauung mußte lange rein in dem Sinne wirken, die dem Menschen nahegehenden Ideen über das Übersinn- liche vorzubringen, bevor es ihr aus den Kulturbedin- gungen der Gegenwart heraus möglich war, in das praktische Leben, wozu sie sich so besonders veranlagt fühlt, wirklich einzugreifen.",
      "Dies wurde nun auf einem eingeschränkten Gebiete - und auch da wieder nur in einem sehr geringen Maße möglich, als Emil Molt in Stuttgart die Waldorfschule begründete, deren Leitung mir obliegt. Zwar war schon früher, wie das kleine Schriftchen «Die Erziehung des Kindes vom Gesichts- punkte der Geisteswissenschaft» zeigt, der Versuch un- ternommen worden, aus anthroposophischen Unter- gründen heraus bestimmte Erziehungsprinzipien zu vertreten.",
      "Allein erst durch die Gründung der Waldorf- schule ist es möglich geworden, diese Dinge in die Le- benspraxis einzuführen, und seit jener Zeit ist es auch möglich, die pädagogisch-didaktische Seite der Anthro- posophie im einzelnen durchzuführen. Es wird mir na- türlich nicht möglich sein, hier in diesem einleitenden Vortrag mehr als einige Andeutungen zu geben, allein ich denke, daß durch die anderen Vorträge des heutigen Tages das Angedeutete weiter ausgeführt werden kann. 76 Was durch anthroposophische Ideen aufgenommen wird, wenn man sie einfach mit dem gesunden Men- schenverstand für sich selber verifiziert, ist nicht bloß eine theoretische Anschauung, das sind nicht bloß Ideen abstrakter Art, die man nun haben kann, um irgend-welche Erkenntnisbedürfnisse in theoretischer Weise zu befriedigen.",
      "Sondern das, was in den Ideen zum Ausdruck kommt, die aus anthroposophischen Quellen geschöpft sind, das ist wirkliche menschliche Kraft, das ist etwas, was übergeht in den ganzen Menschen, was die Liebe intensiver macht, was in die Tatkraft des Menschen sich umsetzen kann. Während die Ideen und Gedanken der üblichen Wissenschaft- lichkeit, die sich nur auf die Sinneswelt beziehen, gerade darin ihr Eigentümliches haben, daß sie sich in den Dienst theoretischer und auch wiederum nur für die Sinneswelt in Betracht kommender praktischer Interessen stellen, ist es das Charakteristische derjenigen Ideen, in welche anthroposophische Forschungsergebnisse hin- eingelegt sind, daß sie auf den ganzen Menschen, auf seine Erkraftung, auf seine - wenn ich es so ausdrücken darf Lebensgeschicklichkeit, auf sein Lebensverständnis wirken, und zwar auf jenes Lebensverständnis, das ihm möglich macht, durch seinen Willen bei den verschie- densten Gelegenheiten des Lebens wirklich einzugrei- fen.",
      "Und wenn man an irgendeinem Ende einfach dieses Leben anfaßt und es befruchtet durch anthroposophi- sche Ideen, so kann man sehen, wie das Handeln des Menschen, wenn es sich dirigieren läßt von diesen Ideen, dann größere Kraft, größere Eindringlichkeit und so weiter erhält. Das ist etwas, was sich insbeson- dere auf pädagogisch-didaktischem Gebiete bewähren muß. 77 Wir hatten ja, als die Waldorfschule begründet wor- den ist, nicht Gelegenheit, die äußeren Bedingungen für die Erziehung und den Unterricht der uns übergebenen Kinder auszuwählen.",
      "Es wird in der Gegenwart vielfach geltend gemacht, wenn ein befriedigender Unterricht, eine befriedigende Erziehung Zustandekommen soll, dann müsse der oder jener Ort für die Schule, für das Erzie- hungsinstitut oder dergleichen ausgesucht werden. Ge- wiß, für alle diese Behauptungen spricht außerordentlich vieles, und sie bewähren sich ja auch in der Praxis bis zu einem gewissen Grade.",
      "Aber wir hatten das alles nicht. Zunächst mußten wir den Versuch aus den gegebenen Bedingungen heraus mit den Kindern der Stuttgarter Waldorf-Astoria-Zigaretten-Fabrik beginnen. Wir hatten also ein ganz bestimmtes Kindermaterial zunächst, wir mußten in einem Hause, das selbstverständlich sehr wenig dazu geeignet war - es war ein früheres Wirtshaus -, mit unserem Unterricht und unserer Erziehung beginnen.",
      "Wir konnten uns also auf nichts verlassen als auf das, was rein aus geistigen Untergründen heraus für die pädago- gischen und didaktischen Gesichtspunkte selbst begon- nen werden kann. Und da muß immer wieder betont werden: Weil Anthroposophie nicht eine abstrakte Kopf-Erkenntnis - wenn ich den Ausdruck gebrauchen darf - anstrebt, sondern eine Einsicht in die Welt und ihre Geheimnisse, die den ganzen Menschen ergreift, so kann sie gerade dadurch zu einer Menschenerkenntnis, zu einem Men- schenverständnis führen, wie man es sonst nicht auf irgendeinem theoretischen Gebiete erreichen kann.",
      "Und letzten Endes beruht ja alle Erziehung, aller Unterricht auf jenem Menschenverständnis, das sich bewährt in dem Verhältnis des Lehrenden, des Erziehenden zum 78 werdenden, heranwachsenden Menschen, zum Kinde. Daher ist unsere Waldorf-Pädagogik aufgebaut auf einer intimen Erkenntnis des werdenden Menschen, des Kin- des.",
      "Ich brauche nur eine Einzelheit anzudeuten, an der ersichtlich werden kann, wie sich wirkliche Einsicht in den ganzen Menschen in der Praxis bewähren muß. Wir haben ja heute auch eine Psychologie, die mehr oder weniger von der anerkannten Wissenschaft gelten gelassen wird.",
      "Aber diese Psychologie theoretisiert her- um an mancherlei Fragen, die eben immer einen unbe- friedigenden Rest lassen müssen. Sie legt sich zum Bei- spiel die Frage vor: Welches Verhältnis besteht zwischen dem Geistig-Seelischen und dem Leiblich-Physischen des Menschen? - und sie hat alle möglichen Theorien darüber ausgebildet.",
      "Wir haben da drei Typen von Theorien: Die eine sucht von dem Geistig-Seelischen auszugehen, dieses zunächst in irgendeiner Weise zu definieren, sich einen abstrakten Begriff davon zu ma- chen und dann zu untersuchen, inwiefern das Geistig- Seelische auf das Physisch-Leibliche wirken kann. Eine andere, mehr materialistisch gefärbte Theorie geht davon aus, daß das Leiblich-Physische die Grundlage sei, und daß dieses Leiblich-Physische dann das Geistig-Seeli- sche nur als eine Funktion hervorbringe.",
      "Eine dritte Theorie ist die des psycho-physischen Parallelismus, die davon ausgeht, in gleicher Weise nebeneinander gelten zu lassen das Geistig-Seelische und das Leiblich-Physische und nur zu verfolgen, wie die Funktionen des einen parallel neben denen des ändern verlaufen, ohne daß man auf ein inneres Wechselverhältnis zwischen beiden eingeht. Das alles sind psychologische Spekulationen.",
      "Sie werden erst in dem Augenblick zu Angelegenhei- ten der Lebenspraxis, wo man durch diese Psychologie, 79 durch diese Seelenerkenntnis, zu pädagogisch-didak- tischen Triebkräften kommt. Man kann sagen: Auf diesem Gebiet ist einfach unse- re Anschauung des Geistig-Seelischen des Menschen noch nicht denjenigen Prinzipien nachgekommen, die wir gewohnt sind, in der Naturwissenschaft wie selbstver- ständlich zu verfolgen.",
      "In der Naturwissenschaft ver- folgen wir, wenn zum Beispiel irgendwo Wärme auftritt, ohne daß zunächst auf die gewöhnliche Art Wärme zugeführt worden ist, wie diese Wärme in einem anderen Zustande, also als sogenannte latente Wärme vorhanden war und wie sie sich aus diesem latenten Zustande ent- wickelt hat, und nun als Wärme offenbar wird. Solche Prinzipien, wie sie in der Naturwissenschaft gang und gäbe sind, müssen - selbstverständlich in der entspre- chenden Weise metamorphosiert - auch aufgenommen werden in die Betrachtung des Vollmenschlichen des Menschen, welches das Geistig-Seelische in sich schließt.",
      "Und man kommt zu einer solchen Anschauungs- weise, die sich vor der Naturwissenschaft voll recht- fertigen läßt - wenn das auch heute noch nicht eingese- hen wird -, wenn man etwa seinen Blick hinwendet auf die erste bedeutungsvolle Umwandlung, die mit der ganzen menschlichen Organisation vor sich geht mit dem Zahnwechsel um das siebente Lebensjahr herum. Man beobachtet solche Umwandlungen des Menschen in der Regel recht äußerlich.",
      "Allein, der Zahnwechsel ist etwas, was in das ganze menschliche Leben tief eingreift. Wer sein Anschauungsvermögen dafür schult, der lernt erkennen, wie mit dem Eintritt des Zahnwechsels das ganze seelische Leben des Kindes ein anderes wird.",
      "Er lernt erkennen, wie das Kind vorher im vollsten Sinne des Wortes eigentlich nicht «in sich» lebte, sondern ganz 80 mit seinem Seelenleben in seiner Umgebung aufging. Er lernt erkennen, wie das Wesentlichste der Triebkräfte im kindlichen Organismus vor dem Zahnwechsel die Nachahmung ist.",
      "Durch Nachahmung lernt das Kind seine Bewegungen. Man kann durch eine unbefangene Beobachtung ge- nau feststellen, wie die Bewegungen von Vater und Mutter oder von der anderen Umgebung des Kindes hineingehen in den kindlichen Organismus selbst.",
      "Man kann verfol- gen, wie unter gesunden Verhältnissen die Sprache gelernt wird unter dem Einfluß der Nachahmung. Man kann sehen, wie das Kind im vollsten Sinne des Wortes mit seinem ganzen Wesen an seine Umgebung hingegeben ist.",
      "Das aber wird völlig anders im Verlaufe des Zahn- wechsels. Da sehen wir, wie sich im Kinde Kräfte ausbil- den, die bewirken, daß das Kind nun selbständig Vor- stellungen hervorbringen kann. Diese Fähigkeit zu selbständigen Vorstellungen, die das Innere des Kindes bis zu einem gewissen Grade von der Umwelt befreien, ist vor dem siebenten Lebensjahr gar nicht vorhanden.",
      "Mit dem Zahnwechsel erlangt das Kind eine gewisse Innerlichkeit und es wird dann nach und nach auch für Abstraktes zugänglich. Nun ist aber durch die kindliche Natur wiederum bedingt, daß alles, was innerlich m den das Kind umge- benden Menschen lebt, von dem Kind aufgenommen wird.",
      "Daher muß es in der zweiten Lebensepoche; die mit dem Zahnwechsel beginnt und bis zur Geschlechts- reife geht, so angesehen werden, daß es alles, was sich in ihm nun innerlich ausbildet, in Anpassung an die menschliche Umgebung ausbildet. Nicht das, was die Menschen seiner Umgebung tun, denn das wird nach- geahmt, sondern das, was in diesen Menschen lebt, also 81 was zum Ausdruck kommt durch das Wort, durch die Gesinnung, durch die Gedankenrichtung, das überträgt sich auf das Kind und zwar jetzt nicht durch Nachah- mung, sondern durch eine Kraft, die aufzunehmen das Kind ebenso veranlagt ist wie in ihm die Wachstums- und Ernährungskräfte veranlagt sind: die Kraft der Au- torität.",
      "Man wird wohl nicht mißverstehen, was ich hier mit der Kraft der Autorität meine, denn derjenige, der «Die Philosophie der Freiheit» geschrieben hat, will hier nur darauf hinweisen, wie das Autoritätsprinzip für eine bestimmte Lebensphase des Menschen in Betracht kommt. Es soll also nicht die gesamte Erziehung abge- stellt werden auf das, was man heute vielfach als das Autoritätsprinzip bezeichnet.",
      "Wenn man nun auf solche Beobachtungen den entsprechenden Wert legt, dann dif- ferenzieren sich die Dinge immer deutlicher und man erwirbt sich immer mehr die Fähigkeit, die Metamor- phosen im Menschen nicht nur von Jahr zu Jahr, sondern von Monat zu Monat beobachten zu können. Was aber ist es denn, was da zwischen Zahnwechsel und Ge- schlechtsreife im Kinde zutage tritt?",
      "Wenn man sich einen Blick aneignet für das, was da tatsächlich vorliegt, dann findet man, daß zwischen dem siebten und vierzehnten Jahr - das sind natürlich nur approximative Zahlen - beim Kind innerlich seelisch das zum Ausdruck kommt, was vorher verborgen in ihm als Kraft wirkte. Dieses steckte unten in der Leiblichkeit und bewirkte die Ausgestaltung des menschlichen Or- ganismus, wirkte auch in der Umbildung des Gehirns in den ersten Lebensjahren und in der Zubereitung der Sprachorgane, wirkte also in allem, was das Kind über- haupt in seinem Körperlichen ausbildete.",
      "Und so kann man sagen: So wie zum Beispiel die Wärme in einem 82 Körper verborgen sein und dann durch gewisse Umstän- de frei werden kann, so wird das Geistig-Seelische, das in den ersten sieben Lebensjahren latent im Physisch- Organischen wirkt, was in jeder einzelnen Bewegung, in jedem körperlichen Vorgang zum Ausdruck kommt, erst später frei. Nach dem siebten Lebensjahr wird das Körperliche mehr sich selbst überlassen; es zieht sich das Geistig-Seelische allerdings nicht vollständig aus dem Körperlichen heraus, aber doch in einem hohen Maße.",
      "Der Zahnwechsel ist dann eine Art Schlußpunkt der ersten Entwicklungsphase, in der das Geistig-Seelische des Menschen noch deckungsgleich war mit dem Phy- sisch-Leiblichen. Sie sehen, daß man durch eine solche Betrachtungs- weise in die Lage kommt, nun eine wirkliche Beziehung zu erkennen zwischen dem Geistig-Seelischen und dem Physisch-Leiblichen.",
      "Man theoretisiert nicht mehr nur herum über die Frage, wie denn die beiden aufeinander wirken und so weiter. Man sieht einfach das Geistig- Seelische während der einen Lebensepoche ganz im Körperlichen drin - man hat es in der kindlichen Ent- wicklung anschaulich vor sich -, und man sieht es später, nach seiner Befreiung, in seiner eigenen Gestalt.",
      "Man vergleicht also nicht erst, was man zuvor in abstrakte Begriffe gefaßt hat, sondern man verfolgt die Wirksam- keit des Geistig-Seelischen im Körperlichen in den ver- schiedenen Lebensepochen. Das heißt aber, daß das, was m der Naturwissenschaft als das den äußeren Sinnen Zugängliche erforscht wird, herausgehoben wird m das geistige Gebiet.",
      "Würde man viel mehr auf die Einzel- heiten dessen, was Anthroposophie will, eingehen und nicht bei oberflächlichen Definitionen stehenbleiben, so würde man schon sehen, welch eine treue Fortsetzerin 83 der so berechtigten naturwissenschaftlichen Denkweise die geisteswissenschaftlich-anthroposophische Weltan- schauung eigentlich ist. Dann aber, wenn man sich in dieser Weise bis herein in die Begriffs- und Ideenwelt Menschenerkenntnis erwirbt, dann löst sich der Vorwurf von der Lebensfremdheit der Ideenwelt von selber auf.",
      "Sehr verehrte Anwesende! Anthroposophie will am wenigsten auf pädagogischem Gebiete irgendwie oppo- sitionell sein zu dem, was an Großem und Bedeutsamem im Laufe besonders des 19. Jahrhunderts durch die großen Pädagogen der Menschheit an pädagogischen Prinzipien gegeben worden ist.",
      "Anthroposophie erkennt völlig an, daß große, bedeutungsvolle Erziehungsprinzipien da sind und sie steht nicht zurück vor irgend jemandem in der Anerkennung der großen Pädagogen. Allein, dennoch muß man sagen: Bei allen großen Erziehungsprinzipien, die da sind, herrscht heute vielfach eine gewisse Unbe- friedigung gegenüber der Erziehungspraxis, und Erzie- hungsmethoden der verschiedensten Art treten auf zum Zeugnis dafür, daß es so ist.",
      "Warum ist das so? Es ist dies oft lediglich eine Folge des Intellektualis- mus in unserem Zeitalter. Dieser Intellektualismus be- wirkt ja mehr als man gewöhnlich glaubt eine gewisse Lebensfeindlichkeit, namentlich für die sozialen Gebiete des Daseins.",
      "Er erzeugt in bezug auf das Ideenhafte eigentlich nur das Abstrakte. Das Abstrakte aber hat keine Lebenskraft in sich; es ist in gewisser Beziehung der Leichnam des Geistigen und wird auch als solcher erlebt.",
      "Und hat man die schönsten Grundsätze, für die man geradezu in Begeisterung erglühen kann - solange diese Grundsätze abstrakt bleiben, können sie im Leben nicht einen irgendwie günstigen Einfluß gewinnen. Erst wenn diese Grundsätze durchzogen werden von wirk- 84 licher Geistigkeit, von lebendiger Geistigkeit, die sich mit dem Wesen des Menschen verbindet, können diese Grundsätze praktisch werden.",
      "Und so möchte Anthro- posophie nicht neue Erziehungsgrundsätze wiederum in abstrakter Art aufstellen; sie will nur eine Anleitung sein für die pädagogischen und didaktischen Geschicklich- keiten, für die Handhabung der Erziehungskunst und der Unterrichtskunst, und sie möchte gerade das geben, was auch die schönsten Erziehungsgrundsätze nicht ge- ben können: geistige Untergründe für die praktische Handhabung, für die innere Befähigung des Lehrers, in der Schule und in der Erziehung zu wirken. Daher ist ja auch die Waldorfschule nicht so einge- richtet, daß - wie leider oft geglaubt wird - durch sie Weltanschauung, wie wir sie vor Erwachsenen vortragen, in die Kinder hineingepfropft werden sollte.",
      "Wir haben daher ganz besonders zu betonen, daß sogar der Reli- gionsunterricht für die katholischen Kinder den katho- lischen Pfarrern, und für die evangelischen Kinder den evangelischen Pfarrern überlassen wird. Wir haben nur einen freien Religionsunterricht eingerichtet für dieje- nigen Kinder, die Dissidentenkinder sind, und die, wenn dieser Unterricht nicht eingerichtet worden wäre, gar keinen Religionsunterricht hätten.",
      "Gerade dadurch konn- te wieder etwas zur Belebung des religiösen Gefühles geleistet werden; denn gerade diejenigen Eltern, die sonst ihre Kinder dem Religionsunterricht ganz entzogen hät- ten, schicken ihre Kinder jetzt in diesen Religionsunter- richt, in welchem wir uns Mühe geben, nicht etwa An- throposophie vorzutragen, sondern das auszugestalten, was für das kindliche Alter in dieser Beziehung ausge- staltet werden muß. Also nicht darum handelt es sich, Anthroposophie in das kindliche Gemüt hineinzutragen, 85 sondern darum, daß die Lehrerschaft durch Anthro- posophie dazu kommt, die pädagogisch-didaktischen Handlungsweisen so einzurichten, daß sie nun wirklich wahrer Menschenerziehung entsprechen.",
      "Hieraus folgt, daß zunächst einfach durch die prakti- sche Handhabung eine solche Erziehung und ein solcher Unterricht Zustandekommen, die nicht bloß auf das Kind sehen, sondern die auf den ganzen Menschen sehen. Denn es wäre höchst töricht, etwa die Füße oder Hände eines Kindes, wie sie im kindlichen Alter sind, als etwas Fertiges zu betrachten und sie etwa zu nötigen, so zu bleiben, wie sie im kindlichen Alter sind.",
      "Es ist selbst- verständlich, daß wir im kindlichen Alter den kindlichen Organismus als etwas Werdendes betrachten, das später im Leben anders zu sein hat. Aber in bezug auf das Geistig-Seelische tun wir im Leben nicht immer das Gleiche.",
      "Wir sehen oftmals sogar, daß dem Kinde starre Begriffe beigebracht werden und das Kind häufig schon im kindlichen Alter etwas in seine Seele hereinbekommt, was scharfe Konturen hat. Das ist falsch! Es muß sich darum handeln, daß wir alles, was wir dem kindlichen Organismus einverleiben wollen, so an ihn heranbringen, daß es wachsen, daß es sich nach und nach umwandeln kann; so daß der Mensch später, im dreißigsten Jahre zum Beispiel, nicht nur eine Erinnerung an das hat, was er im kindlichen Alter aufgenommen hat, sondern daß er das damals Aufgenommene so umgestaltet hat, wie er auch seine Glieder umgestaltet hat.",
      "Wir müssen dem Kinde in allem, was wir ihm geistig-seelisch geben, auch etwas geben, was Wachstumskräfte, was Umwandlungs- kräfte in sich hat; das heißt, wir müssen den Unterricht lebendiger und immer lebendiger machen. Gewiß, das kann als abstraktes Prinzip ausgespro- chen werden; aber praktisch erreicht kann es nur wer- den, wenn eine wirklich intime Menschenerkenntnis vorhanden ist.",
      "Eine solche intime Menschenerkenntnis macht es möglich, daß man einfach von der kindlichen Natur selbst alles abliest, was man gewöhnlich unter Lehrplan und unter Lernziel versteht. Daher herrscht in der Waldorfschule ein solcher Lehrplan und sind solche Lernziele in Aussicht genommen, die aus einer wirk- lichen Menschenkenntnis heraus von Monat zu Monat aus der Entwicklung der kindlichen Natur selbst abge- lesen werden.",
      "Es ist der Versuch gemacht worden, wirk- lich alles in lebendigem Sinne zu gestalten. Ich will nur eines erwähnen. Es ist ja heute in ver- schiedener Beziehung auch im heutigen öffentlichen Unterricht manches besser geworden.",
      "Allein, Sie wissen alle, daß während des ganzen Schuljahres das Kind ei- gentlich mehr als es einem gewöhnlich bewußt wird, unter dem System leidet, das die Fortschritte des Kindes beurteilt. Da gibt es auf der einen Seite die kindlichen Leistungen, auf der anderen Seite die Beurteilungen dieser Leistungen durch den Lehrer; die werden so ausgedrückt: «befriedigend», «fast befriedigend», «fast kaum befrie- digend», «minder befriedigend» und so weiter.",
      "Ich muß Ihnen offen gestehen: Ich war eigentlich nie fähig, einen Unterschied einzusehen zwischen «fast befriedigend», «fast nicht befriedigend» und dergleichen. Bei uns in der Waldorfschule handelt es sich darum, daß aus der Ge- samtheit der Fortschritte heraus am Ende des Schuljah- res dem Kinde eine Art Zeugnis übergeben wird, in dem der Lehrer individuell das Kind charakterisiert, indem er einfach das, was er an dem Kinde erlebt hat, auf ein Stück Papier schreibt.",
      "Das Kind sieht so eine Art Spiegelbild seiner selbst, und die Praxis hat gezeigt, daß es dieses 87 Spiegelbild - worauf nicht «befriedigend», «minder be- friedigend» und so weiter für die einzelnen Gegenstände steht - mit einer gewissen inneren Befriedigung und Freude aufnimmt, selbst wenn darin Tadel stehen. Und dann bekommt das Kind eine Art Kraftspruch mit, der gerade aus seiner Natur geholt ist, den es sich dann aneignet, und der ihm ein Leitspruch für das nächste Jahr sein kann. - So kann man, wenn man die Liebe dazu hat, auf das Lebendige einzugehen, den Unterricht selbst unter ungünstigen Verhältnissen lebendig gestalten.",
      "Dadurch aber kommen wir auch dazu, etwas zu überwinden, was in unserem Zeitalter gerade in der Pädagogik und Didaktik überwunden werden muß. Man wird ja heute in der äußeren Geschichtsschreibung we- nig Anhaltspunkte dafür finden, wie sich die Seelenver- fassungen der Menschen in den einzelnen Entwicklungs- epochen der Menschheit geändert haben.",
      "Wer aber Un- befangenheit genug hat, wird schon verstehen können, wie das, was man als geistige Äußerungen zum Beispiel des 10., 11., 12. Jahrhunderts sich vor die Seele stellen kann, einen ganz anderen Charakter trägt als das, was etwa seit der Mitte des 15.",
      "Jahrhunderts die Seelenverfas- sung der zivilisierten Menschheit geworden ist. Ja, bis zum 20. Jahrhundert herauf hat sich der Intellektualis- mus m der Menschheit bis zu einem Kulminationspunkt entwickelt.",
      "Dieser Intellektualismus hat aber die Eigen- tümlichkeit, daß er - geradeso wie das Nachahmungs- prinzip oder das Autoritätsprinzip erst in einem be- stimmten Lebensalter des Menschen aus einem laten- ten in einen freien Zustand versetzt wird, und das ist beim Intellektualismus in einem verhältnismäßig späten Lebensalter der Fall. Wir sehen, wie der Mensch eigent- lich erst, wenn er die Geschlechtsreife überwunden hat, eigentlich sogar noch später, aus seiner elementaren Na- tur heraus geeignet wird, zum Intellektualistischen fort- zuschreiten.",
      "Vorher wirkt das Intellektualistische auf seine Seelentätigkeit durchaus ablähmend, abtötend. Daher können wir sagen: Wir leben in einem Zeital- ter, das eigentlich nur für den erwachsenen Menschen da ist, das als den wichtigsten Kulturimpuls etwas hat, was erst im erwachsenen Menschen voll zum Ausdruck kommen sollte.",
      "Das aber hat zur Folge, daß wir heute mit dem, was in bezug auf die ganze Kultur für die erwachsenen Menschen gerade tonangebend ist, eigent- lich das Kind und selbst den jungen Menschen nicht mehr verstehen! Das ist das wichtigste, was in unserer Zivilisation zu berücksichtigen ist.",
      "Wir müssen uns darüber klar sein, daß wir gerade durch diejenigen Kräfte, durch die wir unsere Wissenschaften und unsere Technik zu so großen Trium- phen und so großer Blüte gebracht haben, uns die Mög- lichkeit nehmen, das Kind voll zu verstehen und auf die volle Menschennatur des Kindes einzugehen. Es bedarf eben wieder eigener Mittel, um die Brücke zu dem jungen Menschen und dem Kinde herüber zu schlagen.",
      "Das, was jetzt in mannigfacher Gestalt als Jugendbewegung auftritt man mag sich dazu verhalten, wie man will -, hat seine tiefste Berechtigung; sie ist nichts anderes als der Schrei der Jugend: Ihr Erwachsenen habt eine Zivilisation, die wir einfach nicht verstehen, wenn wir uns unserer elemen- tarsten Natur hingeben! - Aber diese Brücke vom Er- wachsenen zur Kindeswelt muß wieder gefunden werden, und dazu möchte Anthroposophie das ihrige beitragen. Und wenn man dann vom allgemeinen Kulturstand- punkt zum einzelnen heruntersteigt, wird man wieder finden, wie dieser Erziehungsplan, der abgelesen ist vom 89 Wesen des Kindes selbst, uns erkennen läßt, was man im Erziehungsplan für die einzelnen Lebensphasen der Kindheit entwickeln muß.",
      "Schreiben und Lesen waren in früheren Zeitaltern etwas ganz anderes, als sie es heute sind. Nehmen Sie unsere heutigen Buchstaben: sie sind etwas ganz Abstraktes, Lebensfremdes im Verhältnis zum eigentlichen Leben.",
      "Gehen wir zu früheren Zeiten zurück: Wir finden in der Bilderschrift etwas, was sich unmittelbar an das Leben anlehnt. Wir machen uns heute oft gar keine Gedanken darüber, wie innig mit dem Leben [diese Bilderschrift] verbunden war, und wie heute dem Leben so fremd ist: Lesen und Schreiben.",
      "Ja, wir stehen in einer Zivilisation drinnen, der es natürlich ist, daß das Lebensfremdeste zu Zwecken der Zivilisa- tion ausgebildet wird. Wer heute mit unbefangenem Sinn zum Beispiel einen Stenographen oder einen alten Menschen an der Schreibmaschine sitzen sieht, der weiß, daß mit einer solchen Betätigung gerade das menschlich Fremdeste in die Zivilisation eingezogen ist.",
      "Sehr verehr- te Anwesende, man wird nicht kulturfeindlich oder zum Reaktionär, wenn man dies ausspricht. Es wird auch nichts gesagt gegenüber dem, was mit diesen Mitteln in die neuere Zeit eingezogen ist; sie mußten da sein.",
      "Aber es müssen auch die Gegenkräfte entwickelt werden, die das wieder heilen, was, wenn es einzig und allein wirk- sam gelassen wird, nur zu einem gewissen Niedergang der Kultur, zu einer Dekadenz führen könnte. Und das wichtigste Moment, was in dieser Beziehung als Heil- mittel eingeführt werden kann, liegt in der Erziehung, im Unterricht, der aber stets erzieherisch gestaltet wer- den muß.",
      "Wenn wir das Kind m die Volksschule hereinbekom- men, ist es ja so, daß sein Intellekt zunächst noch 90 schlummert. Die Fähigkeit zu abstraktem Denken, die erst von anderem belebt werden muß, diese Fähigkeit tritt erst später auf.",
      "Daher können wir mit den abstrak- ten Schreibe- und Leseformen an das Kind, wenn es in die Schule kommt, noch nicht herankommen. Da können wir nur das nehmen, womit wir lebendig an das Kind herankommen können, denn im Kinde selbst wirkt ja ein künstlerisches seelisches Prinzip, das vollkommener und großartiger ist als jede andere Kunst.",
      "Das wirkt auf unbewußte Art. Diese müssen wir fortsetzen und müs- sen versuchen, für das kindliche Alter besondere Formen zu erfinden, wodurch das Kind auf künstlerische Art in das Schreiben, das heißt in die Betätigung seines gesamten Menschen hereinkommt und dann zum Lesen übergeht.",
      "Man muß in bezug auf die Pädagogik, wenn die Kinder heute im achten oder neunten Jahre noch nicht lesen oder schreiben können, den Mut haben, sagen zu kön- nen: Gott sei Dank, daß die Kinder in diesen Jahren noch nicht lesen oder schreiben können! - denn es kommt nicht darauf an, daß der Mensch dieses oder jenes [früh] lernt, sondern daß er es im richtigen Lebensalter und auf eine richtige Art lernt. So ist in der Waldorfschule der Unterricht auf künst- lerische Gestaltung hin eingerichtet.",
      "Aus pädagogisch- künstlerischen Prinzipien heraus wird zunächst vorge- gangen und erst allmählich zum Intellektuahstischen übergeleitet. Wir tragen auch dem Rechnung, daß das Musikalische möglichst früh im Unterricht auftritt, weil es zur Willensbildung des Menschen in Beziehung steht.",
      "Wir tragen dem dadurch Rechnung, daß wir zu dem gewöhnlichen Turnunterricht den Eurythmie-Unterricht, das beseelte Turnen, m den Unterricht eingefügt haben. Es muß noch metamorphosiert werden, muß ins Päd- 91 agogisch-Didaktische umgesetzt werden, dann aber fin- det man, daß durch diese Bewegungskunst, die das wahrzunehmen hat, was Geist und Seele des Menschen ist, etwas vermittelt wird, was sinnvoll ist.",
      "Man findet, daß das Kind sich während der schulpflichtigen Erziehung in diese Bewegungskunst so hineinfindet, wie es sich als ganz kleines Kind eben in die Sprache hineinfindet, mit innerem Wohlgefallen und mit innerer Selbstverständ- lichkeit. Dieses Herausarbeiten aus dem Künstlerischen führt dann auch dahin, daß man das Kind von sehr früh an mit Farben hantieren läßt.",
      "Wenn das auch zuweilen unbequem ist, und -wenn dann auch schärfere Reinlich- keitsgrundsätze als sonst dabei eingreifen müssen, so wird sich doch herausstellen, daß man dadurch das Kind tiefer in das Leben einführt als sonst. Man bringt es dazu, daß es einen Sinn bekommt für das Leben, daß es nicht am Leben vorbeigeht, sondern daß es mit der äußeren Welt lebt, daß es empfänglich wird für alles Schöne, für alles, was ihm sinnvoll in Natur und Menschenleben entgegentritt.",
      "Und dies ist wichtiger als die Übertragung einzelner Einzelheiten aus diesem oder jenem Gebiete auf das Kind. Zu alle dem aber, was ich hier nur in seinen Richt- linien andeuten kann, kommt das, was aus anthroposo- phischen Untergründen heraus in die Gesinnung des Lehrers einfließt, was der Lehrer einfach durch sein ganzes Wesen mitbringt an pädagogisch-didaktischen Imponderabilien, wenn er die Tür des Schulzimmers hinter sich schließt nach der Klasse zu, wenn er vor die Kinder tritt.",
      "Wer mit lebendigem Sinn - nicht mit ab- strakten Ideen - anschaut, wie das Kind nachahmend sich anpaßt an die Umgebung, der weiß, was in diesem Kinde als Geistig-Seelisches wirkt. Er lernt das Kind 92 kennen und bekommt dadurch die Voraussetzungen, es in ganz anderer Weise zu beurteilen, als man es gewöhn- lich tut.",
      "Ich will dafür nur ein Beispiel anführen. Man lernt ja so manches, wenn man in diesem Sinne das Leben ansieht. Zu mir kam einmal ein Elternpaar und sagte, der junge Sohn, der bisher ganz brav und ordentlich gewesen sei, habe jetzt plötzlich gestohlen.",
      "Ich fragte: «Wie alt ist das Kind?» -, die Eltern antwor- teten: «Fünf Jahre». Ich sagte: «Dann muß man erst untersuchen, was das Kind eigentlich getan hat, denn vielleicht hat es gar nicht gestohlen.» - Was hatte es denn getan?",
      "Es hatte einiges Geld aus der Schublade genom- men, aus der die Mutter jeden Morgen Geld nahm, wenn sie einkaufen wollte. Für dieses Geld hatte sich der Knabe einige Naschereien gekauft, die er nicht einmal für sich selbst verwendet hat, sondern die er anderen Kindern gegeben hat.",
      "In diesem Fall muß man sagen: Da ist gar keine Rede von Stehlen; das Kind hat einfach gesehen, was die Mutter jeden Morgen getan hat, und es fühlte sich befugt, dies selbst auch zu machen. Das Kind ist ein Nachahmer.",
      "Jenes Verhältnis des Kindes zu den Normen der Erwachsenen, die ihren Ausdruck finden in «gut» und «böse», tritt ja erst ein, wenn der Zahnwechsel überwunden ist. Wir müssen deshalb eine ganz andere Beurteilungsmöglichkeit gewinnen und wissen lernen: alles, was wir in der Umgebung des Kindes tun, muß so eingerichtet werden, daß das Kind es nachahmen kann, es nachahmen kann bis in die Imponderabilien der Ge- danken hinein.",
      "Da erweist sich eben die Realität der Gedanken. Nicht bloß das, was wir tun, sondern auch die Art und Weise unserer Gedanken ist maßgebend dafür. Wir sollen uns in der Umgebung des Kindes nicht jedem Gedanken hingeben, denn er wirkt auf das Kind. 93 Also bis auf die Imponderabilien hin müssen die Gedan- ken berücksichtigt werden.",
      "Schaut man darauf hin, wie das Kind bis zum sieben- ten Jahre mit seiner Umgebung lebt, dann hat man dann einen Abdruck dafür, was das Kind war, bevor der Mensch in die physisch-sinnliche Welt heruntersteigt. Bis dahin - das zeigt anthroposophische Forschung - ist der Mensch ganz umgeben von einer geistig-seelischen Welt, die so mit ihm zusammenhängt im Universum, wie hier in der physischen Welt sein Leib mit dieser.",
      "Und wir kommen dazu, in dem kindlichen Leben bis zum siebenten Jahre eine rechte Fortsetzung des Lebens vor der Geburt oder vor der Konzeption zu sehen. Das aber muß sich verwandeln in pädagogisch-didaktische Emp- findung, so daß der Lehrer so vor dem Kinde steht, daß er sich sagt: Mir ist aus übersinnlichen Welten etwas übergeben, das ich enträtseln muß, dem ich die Lebens- bahn ebnen muß.",
      "Unterricht und Erziehung wird so wirklich ein Op- ferdienst gegenüber der ganzen Welt. Es wird über Un- terricht und Erziehung etwas ausgegossen von jener Gesinnung, die eine Kraft ist, und ohne die wirklicher Unterricht und wirkliche Erziehung nichts sein können.",
      "Diese Gesinnung, die sich nicht aus äußerlich ange- nommener, sondern aus innerlich erarbeiteter anthropo- sophischer Weltanschauung ergibt, sie ist gerade das Allerwichtigste im pädagogisch-didaktischen Wirken. Man steht dann mit religiöser scheuer Ehrfurcht vor dem, was der kindliche Leib in sich birgt; man schaut hin, wie ein aus den ewigen Weltengründen Erstandenes nach und nach sich offenbart in den kindlichen Bewe- gungen, Gesten und so weiter, und man weiß, daß man ein Lebensrätsel in praktischer Art zu lösen hat.",
      "Die 94 ganze Erziehungs- und Unterrichtsgesinnung wird da- durch überhaupt erst in die richtigen Wege geleitet. Diese Atmosphäre, die sich ausbreitet bei allen Hand- lungen, die im schulgemäßen Leben getan werden müs- sen, ist das, was Anthroposophie vor allem hinein haben möchte in das Unterrichts- und Erziehungswesen, und von dem sie alle Einzelheiten beherrscht haben möchte.",
      "Aber um sie beherrschen zu können, ist nötig, daß man mit wirklicher innerer Anschauung dazu komme, in der kleinsten Lebensregung des Kindes zu sehen, wie der Geist fortwirkt bis in die Fingerspitzen hinein. Der Lehrer wird sich dazu eine innere Gesamtanschauung aneignen, so daß er aus einer Fähigkeit, die wiederum zum Instinkt werden muß, seiner Klasse gegenübertritt mit der Ge- sinnung und der Geschicklichkeit, die gerade aus dieser innerlichen Verarbeitung der anthroposophischen Welt- anschauung kommen.",
      "Das sind einige Andeutungen, die ich geben konnte; sie werden in den folgenden Vorträgen weiter ausgeführt werden können. Diese Andeutungen sollten zeigen, daß die Anthroposophie nicht radikal sein will gegen das Große, was auf pädagogischem Gebiete geleistet worden ist, sondern daß sie sein will eine Helferin für das Große, sonst nur abstrakt Bleibende, so daß es in der Lebens- praxis lebendig durchgeführt werden kann, damit die Erziehungskunst ein wirklicher Impuls, ein wirksamer Faktor in unserem sozialen Leben werden kann! 95"
    ],
    "sentences": [
      [
        "Meine sehr verehrten Anwesenden!",
        "Es wird anthroposo- phischer Weltanschauung in begreiflicher Weise immer der Vorwurf gemacht, daß sie ihre Ideen, ihre Ergebnisse verkündet auf der Grundlage von Forschungen, zu de- nen die Fähigkeiten im Menschen erst herangebildet werden müssen, daß also Forschungsergebnisse der An- throposophie nicht von vornherein von jedem nachge- prüft werden können, und daß sie dennoch diese An- schauungen vor den hierauf unvorbereiteten Menschen verkünde."
      ],
      [
        "Doch gerade dieser Vorwurf, so scheinbar berechtigt er ist, gehört zu den aller unberechtigsten, welche der anthroposophischen Bewegung gemacht werden können.",
        "Denn es handelt sich bei ihr nicht darum, jeden einzel- nen sofort dazu anzuleiten, ein Forscher im übersinnli- chen Gebiet zu werden, sondern es handelt sich bei ihr darum, ihre Forschungsergebnisse auf eine Weise dar- zulegen, die von jedem einzelnen Menschen nachgeprüft werden kann, einfach durch den gewöhnlichen gesunden Menschenverstand und die gewöhnliche gesunde Logik."
      ],
      [
        "Dies macht allerdings nicht unnötig, daß danach gestrebt wird, wenigstens die ersten Schritte zu übersinnlicher Forschung zu machen, und dafür gibt es ja Anleitungen in den verschiedenen Schriften, die auch hier schon ge- 75 nannt worden sind.",
        "Jeder kann also bis zu einem gewis- sen Grade ein anthroposophischer Forscher werden - einfach aus den Zivilisationsbedingungen der Gegenwart heraus -, aber zum Prüfen der Ergebnisse anthroposo- phischer Forschung ist dies nicht nötig, denn diese Prüfung kann einfach aus dem gesunden Menschenver- stand heraus erfolgen."
      ],
      [
        "Und eines der Gebiete, auf denen diese Prüfung wirklich praktisch erfolgen kann, ist das pädagogische Gebiet.",
        "Sehr verehrte Anwesende!",
        "Anthroposophische Welt- anschauung mußte lange rein in dem Sinne wirken, die dem Menschen nahegehenden Ideen über das Übersinn- liche vorzubringen, bevor es ihr aus den Kulturbedin- gungen der Gegenwart heraus möglich war, in das praktische Leben, wozu sie sich so besonders veranlagt fühlt, wirklich einzugreifen."
      ],
      [
        "Dies wurde nun auf einem eingeschränkten Gebiete - und auch da wieder nur in einem sehr geringen Maße möglich, als Emil Molt in Stuttgart die Waldorfschule begründete, deren Leitung mir obliegt.",
        "Zwar war schon früher, wie das kleine Schriftchen «Die Erziehung des Kindes vom Gesichts- punkte der Geisteswissenschaft» zeigt, der Versuch un- ternommen worden, aus anthroposophischen Unter- gründen heraus bestimmte Erziehungsprinzipien zu vertreten."
      ],
      [
        "Allein erst durch die Gründung der Waldorf- schule ist es möglich geworden, diese Dinge in die Le- benspraxis einzuführen, und seit jener Zeit ist es auch möglich, die pädagogisch-didaktische Seite der Anthro- posophie im einzelnen durchzuführen.",
        "Es wird mir na- türlich nicht möglich sein, hier in diesem einleitenden Vortrag mehr als einige Andeutungen zu geben, allein ich denke, daß durch die anderen Vorträge des heutigen Tages das Angedeutete weiter ausgeführt werden kann. 76 Was durch anthroposophische Ideen aufgenommen wird, wenn man sie einfach mit dem gesunden Men- schenverstand für sich selber verifiziert, ist nicht bloß eine theoretische Anschauung, das sind nicht bloß Ideen abstrakter Art, die man nun haben kann, um irgend-welche Erkenntnisbedürfnisse in theoretischer Weise zu befriedigen."
      ],
      [
        "Sondern das, was in den Ideen zum Ausdruck kommt, die aus anthroposophischen Quellen geschöpft sind, das ist wirkliche menschliche Kraft, das ist etwas, was übergeht in den ganzen Menschen, was die Liebe intensiver macht, was in die Tatkraft des Menschen sich umsetzen kann.",
        "Während die Ideen und Gedanken der üblichen Wissenschaft- lichkeit, die sich nur auf die Sinneswelt beziehen, gerade darin ihr Eigentümliches haben, daß sie sich in den Dienst theoretischer und auch wiederum nur für die Sinneswelt in Betracht kommender praktischer Interessen stellen, ist es das Charakteristische derjenigen Ideen, in welche anthroposophische Forschungsergebnisse hin- eingelegt sind, daß sie auf den ganzen Menschen, auf seine Erkraftung, auf seine - wenn ich es so ausdrücken darf Lebensgeschicklichkeit, auf sein Lebensverständnis wirken, und zwar auf jenes Lebensverständnis, das ihm möglich macht, durch seinen Willen bei den verschie- densten Gelegenheiten des Lebens wirklich einzugrei- fen."
      ],
      [
        "Und wenn man an irgendeinem Ende einfach dieses Leben anfaßt und es befruchtet durch anthroposophi- sche Ideen, so kann man sehen, wie das Handeln des Menschen, wenn es sich dirigieren läßt von diesen Ideen, dann größere Kraft, größere Eindringlichkeit und so weiter erhält.",
        "Das ist etwas, was sich insbeson- dere auf pädagogisch-didaktischem Gebiete bewähren muß. 77 Wir hatten ja, als die Waldorfschule begründet wor- den ist, nicht Gelegenheit, die äußeren Bedingungen für die Erziehung und den Unterricht der uns übergebenen Kinder auszuwählen."
      ],
      [
        "Es wird in der Gegenwart vielfach geltend gemacht, wenn ein befriedigender Unterricht, eine befriedigende Erziehung Zustandekommen soll, dann müsse der oder jener Ort für die Schule, für das Erzie- hungsinstitut oder dergleichen ausgesucht werden.",
        "Ge- wiß, für alle diese Behauptungen spricht außerordentlich vieles, und sie bewähren sich ja auch in der Praxis bis zu einem gewissen Grade."
      ],
      [
        "Aber wir hatten das alles nicht.",
        "Zunächst mußten wir den Versuch aus den gegebenen Bedingungen heraus mit den Kindern der Stuttgarter Waldorf-Astoria-Zigaretten-Fabrik beginnen.",
        "Wir hatten also ein ganz bestimmtes Kindermaterial zunächst, wir mußten in einem Hause, das selbstverständlich sehr wenig dazu geeignet war - es war ein früheres Wirtshaus -, mit unserem Unterricht und unserer Erziehung beginnen."
      ],
      [
        "Wir konnten uns also auf nichts verlassen als auf das, was rein aus geistigen Untergründen heraus für die pädago- gischen und didaktischen Gesichtspunkte selbst begon- nen werden kann.",
        "Und da muß immer wieder betont werden: Weil Anthroposophie nicht eine abstrakte Kopf-Erkenntnis - wenn ich den Ausdruck gebrauchen darf - anstrebt, sondern eine Einsicht in die Welt und ihre Geheimnisse, die den ganzen Menschen ergreift, so kann sie gerade dadurch zu einer Menschenerkenntnis, zu einem Men- schenverständnis führen, wie man es sonst nicht auf irgendeinem theoretischen Gebiete erreichen kann."
      ],
      [
        "Und letzten Endes beruht ja alle Erziehung, aller Unterricht auf jenem Menschenverständnis, das sich bewährt in dem Verhältnis des Lehrenden, des Erziehenden zum 78 werdenden, heranwachsenden Menschen, zum Kinde.",
        "Daher ist unsere Waldorf-Pädagogik aufgebaut auf einer intimen Erkenntnis des werdenden Menschen, des Kin- des."
      ],
      [
        "Ich brauche nur eine Einzelheit anzudeuten, an der ersichtlich werden kann, wie sich wirkliche Einsicht in den ganzen Menschen in der Praxis bewähren muß.",
        "Wir haben ja heute auch eine Psychologie, die mehr oder weniger von der anerkannten Wissenschaft gelten gelassen wird."
      ],
      [
        "Aber diese Psychologie theoretisiert her- um an mancherlei Fragen, die eben immer einen unbe- friedigenden Rest lassen müssen.",
        "Sie legt sich zum Bei- spiel die Frage vor: Welches Verhältnis besteht zwischen dem Geistig-Seelischen und dem Leiblich-Physischen des Menschen? - und sie hat alle möglichen Theorien darüber ausgebildet."
      ],
      [
        "Wir haben da drei Typen von Theorien: Die eine sucht von dem Geistig-Seelischen auszugehen, dieses zunächst in irgendeiner Weise zu definieren, sich einen abstrakten Begriff davon zu ma- chen und dann zu untersuchen, inwiefern das Geistig- Seelische auf das Physisch-Leibliche wirken kann.",
        "Eine andere, mehr materialistisch gefärbte Theorie geht davon aus, daß das Leiblich-Physische die Grundlage sei, und daß dieses Leiblich-Physische dann das Geistig-Seeli- sche nur als eine Funktion hervorbringe."
      ],
      [
        "Eine dritte Theorie ist die des psycho-physischen Parallelismus, die davon ausgeht, in gleicher Weise nebeneinander gelten zu lassen das Geistig-Seelische und das Leiblich-Physische und nur zu verfolgen, wie die Funktionen des einen parallel neben denen des ändern verlaufen, ohne daß man auf ein inneres Wechselverhältnis zwischen beiden eingeht.",
        "Das alles sind psychologische Spekulationen."
      ],
      [
        "Sie werden erst in dem Augenblick zu Angelegenhei- ten der Lebenspraxis, wo man durch diese Psychologie, 79 durch diese Seelenerkenntnis, zu pädagogisch-didak- tischen Triebkräften kommt.",
        "Man kann sagen: Auf diesem Gebiet ist einfach unse- re Anschauung des Geistig-Seelischen des Menschen noch nicht denjenigen Prinzipien nachgekommen, die wir gewohnt sind, in der Naturwissenschaft wie selbstver- ständlich zu verfolgen."
      ],
      [
        "In der Naturwissenschaft ver- folgen wir, wenn zum Beispiel irgendwo Wärme auftritt, ohne daß zunächst auf die gewöhnliche Art Wärme zugeführt worden ist, wie diese Wärme in einem anderen Zustande, also als sogenannte latente Wärme vorhanden war und wie sie sich aus diesem latenten Zustande ent- wickelt hat, und nun als Wärme offenbar wird.",
        "Solche Prinzipien, wie sie in der Naturwissenschaft gang und gäbe sind, müssen - selbstverständlich in der entspre- chenden Weise metamorphosiert - auch aufgenommen werden in die Betrachtung des Vollmenschlichen des Menschen, welches das Geistig-Seelische in sich schließt."
      ],
      [
        "Und man kommt zu einer solchen Anschauungs- weise, die sich vor der Naturwissenschaft voll recht- fertigen läßt - wenn das auch heute noch nicht eingese- hen wird -, wenn man etwa seinen Blick hinwendet auf die erste bedeutungsvolle Umwandlung, die mit der ganzen menschlichen Organisation vor sich geht mit dem Zahnwechsel um das siebente Lebensjahr herum.",
        "Man beobachtet solche Umwandlungen des Menschen in der Regel recht äußerlich."
      ],
      [
        "Allein, der Zahnwechsel ist etwas, was in das ganze menschliche Leben tief eingreift.",
        "Wer sein Anschauungsvermögen dafür schult, der lernt erkennen, wie mit dem Eintritt des Zahnwechsels das ganze seelische Leben des Kindes ein anderes wird."
      ],
      [
        "Er lernt erkennen, wie das Kind vorher im vollsten Sinne des Wortes eigentlich nicht «in sich» lebte, sondern ganz 80 mit seinem Seelenleben in seiner Umgebung aufging.",
        "Er lernt erkennen, wie das Wesentlichste der Triebkräfte im kindlichen Organismus vor dem Zahnwechsel die Nachahmung ist."
      ],
      [
        "Durch Nachahmung lernt das Kind seine Bewegungen.",
        "Man kann durch eine unbefangene Beobachtung ge- nau feststellen, wie die Bewegungen von Vater und Mutter oder von der anderen Umgebung des Kindes hineingehen in den kindlichen Organismus selbst."
      ],
      [
        "Man kann verfol- gen, wie unter gesunden Verhältnissen die Sprache gelernt wird unter dem Einfluß der Nachahmung.",
        "Man kann sehen, wie das Kind im vollsten Sinne des Wortes mit seinem ganzen Wesen an seine Umgebung hingegeben ist."
      ],
      [
        "Das aber wird völlig anders im Verlaufe des Zahn- wechsels.",
        "Da sehen wir, wie sich im Kinde Kräfte ausbil- den, die bewirken, daß das Kind nun selbständig Vor- stellungen hervorbringen kann.",
        "Diese Fähigkeit zu selbständigen Vorstellungen, die das Innere des Kindes bis zu einem gewissen Grade von der Umwelt befreien, ist vor dem siebenten Lebensjahr gar nicht vorhanden."
      ],
      [
        "Mit dem Zahnwechsel erlangt das Kind eine gewisse Innerlichkeit und es wird dann nach und nach auch für Abstraktes zugänglich.",
        "Nun ist aber durch die kindliche Natur wiederum bedingt, daß alles, was innerlich m den das Kind umge- benden Menschen lebt, von dem Kind aufgenommen wird."
      ],
      [
        "Daher muß es in der zweiten Lebensepoche; die mit dem Zahnwechsel beginnt und bis zur Geschlechts- reife geht, so angesehen werden, daß es alles, was sich in ihm nun innerlich ausbildet, in Anpassung an die menschliche Umgebung ausbildet.",
        "Nicht das, was die Menschen seiner Umgebung tun, denn das wird nach- geahmt, sondern das, was in diesen Menschen lebt, also 81 was zum Ausdruck kommt durch das Wort, durch die Gesinnung, durch die Gedankenrichtung, das überträgt sich auf das Kind und zwar jetzt nicht durch Nachah- mung, sondern durch eine Kraft, die aufzunehmen das Kind ebenso veranlagt ist wie in ihm die Wachstums- und Ernährungskräfte veranlagt sind: die Kraft der Au- torität."
      ],
      [
        "Man wird wohl nicht mißverstehen, was ich hier mit der Kraft der Autorität meine, denn derjenige, der «Die Philosophie der Freiheit» geschrieben hat, will hier nur darauf hinweisen, wie das Autoritätsprinzip für eine bestimmte Lebensphase des Menschen in Betracht kommt.",
        "Es soll also nicht die gesamte Erziehung abge- stellt werden auf das, was man heute vielfach als das Autoritätsprinzip bezeichnet."
      ],
      [
        "Wenn man nun auf solche Beobachtungen den entsprechenden Wert legt, dann dif- ferenzieren sich die Dinge immer deutlicher und man erwirbt sich immer mehr die Fähigkeit, die Metamor- phosen im Menschen nicht nur von Jahr zu Jahr, sondern von Monat zu Monat beobachten zu können.",
        "Was aber ist es denn, was da zwischen Zahnwechsel und Ge- schlechtsreife im Kinde zutage tritt?"
      ],
      [
        "Wenn man sich einen Blick aneignet für das, was da tatsächlich vorliegt, dann findet man, daß zwischen dem siebten und vierzehnten Jahr - das sind natürlich nur approximative Zahlen - beim Kind innerlich seelisch das zum Ausdruck kommt, was vorher verborgen in ihm als Kraft wirkte.",
        "Dieses steckte unten in der Leiblichkeit und bewirkte die Ausgestaltung des menschlichen Or- ganismus, wirkte auch in der Umbildung des Gehirns in den ersten Lebensjahren und in der Zubereitung der Sprachorgane, wirkte also in allem, was das Kind über- haupt in seinem Körperlichen ausbildete."
      ],
      [
        "Und so kann man sagen: So wie zum Beispiel die Wärme in einem 82 Körper verborgen sein und dann durch gewisse Umstän- de frei werden kann, so wird das Geistig-Seelische, das in den ersten sieben Lebensjahren latent im Physisch- Organischen wirkt, was in jeder einzelnen Bewegung, in jedem körperlichen Vorgang zum Ausdruck kommt, erst später frei.",
        "Nach dem siebten Lebensjahr wird das Körperliche mehr sich selbst überlassen; es zieht sich das Geistig-Seelische allerdings nicht vollständig aus dem Körperlichen heraus, aber doch in einem hohen Maße."
      ],
      [
        "Der Zahnwechsel ist dann eine Art Schlußpunkt der ersten Entwicklungsphase, in der das Geistig-Seelische des Menschen noch deckungsgleich war mit dem Phy- sisch-Leiblichen.",
        "Sie sehen, daß man durch eine solche Betrachtungs- weise in die Lage kommt, nun eine wirkliche Beziehung zu erkennen zwischen dem Geistig-Seelischen und dem Physisch-Leiblichen."
      ],
      [
        "Man theoretisiert nicht mehr nur herum über die Frage, wie denn die beiden aufeinander wirken und so weiter.",
        "Man sieht einfach das Geistig- Seelische während der einen Lebensepoche ganz im Körperlichen drin - man hat es in der kindlichen Ent- wicklung anschaulich vor sich -, und man sieht es später, nach seiner Befreiung, in seiner eigenen Gestalt."
      ],
      [
        "Man vergleicht also nicht erst, was man zuvor in abstrakte Begriffe gefaßt hat, sondern man verfolgt die Wirksam- keit des Geistig-Seelischen im Körperlichen in den ver- schiedenen Lebensepochen.",
        "Das heißt aber, daß das, was m der Naturwissenschaft als das den äußeren Sinnen Zugängliche erforscht wird, herausgehoben wird m das geistige Gebiet."
      ],
      [
        "Würde man viel mehr auf die Einzel- heiten dessen, was Anthroposophie will, eingehen und nicht bei oberflächlichen Definitionen stehenbleiben, so würde man schon sehen, welch eine treue Fortsetzerin 83 der so berechtigten naturwissenschaftlichen Denkweise die geisteswissenschaftlich-anthroposophische Weltan- schauung eigentlich ist.",
        "Dann aber, wenn man sich in dieser Weise bis herein in die Begriffs- und Ideenwelt Menschenerkenntnis erwirbt, dann löst sich der Vorwurf von der Lebensfremdheit der Ideenwelt von selber auf."
      ],
      [
        "Sehr verehrte Anwesende!",
        "Anthroposophie will am wenigsten auf pädagogischem Gebiete irgendwie oppo- sitionell sein zu dem, was an Großem und Bedeutsamem im Laufe besonders des 19.",
        "Jahrhunderts durch die großen Pädagogen der Menschheit an pädagogischen Prinzipien gegeben worden ist."
      ],
      [
        "Anthroposophie erkennt völlig an, daß große, bedeutungsvolle Erziehungsprinzipien da sind und sie steht nicht zurück vor irgend jemandem in der Anerkennung der großen Pädagogen.",
        "Allein, dennoch muß man sagen: Bei allen großen Erziehungsprinzipien, die da sind, herrscht heute vielfach eine gewisse Unbe- friedigung gegenüber der Erziehungspraxis, und Erzie- hungsmethoden der verschiedensten Art treten auf zum Zeugnis dafür, daß es so ist."
      ],
      [
        "Warum ist das so?",
        "Es ist dies oft lediglich eine Folge des Intellektualis- mus in unserem Zeitalter.",
        "Dieser Intellektualismus be- wirkt ja mehr als man gewöhnlich glaubt eine gewisse Lebensfeindlichkeit, namentlich für die sozialen Gebiete des Daseins."
      ],
      [
        "Er erzeugt in bezug auf das Ideenhafte eigentlich nur das Abstrakte.",
        "Das Abstrakte aber hat keine Lebenskraft in sich; es ist in gewisser Beziehung der Leichnam des Geistigen und wird auch als solcher erlebt."
      ],
      [
        "Und hat man die schönsten Grundsätze, für die man geradezu in Begeisterung erglühen kann - solange diese Grundsätze abstrakt bleiben, können sie im Leben nicht einen irgendwie günstigen Einfluß gewinnen.",
        "Erst wenn diese Grundsätze durchzogen werden von wirk- 84 licher Geistigkeit, von lebendiger Geistigkeit, die sich mit dem Wesen des Menschen verbindet, können diese Grundsätze praktisch werden."
      ],
      [
        "Und so möchte Anthro- posophie nicht neue Erziehungsgrundsätze wiederum in abstrakter Art aufstellen; sie will nur eine Anleitung sein für die pädagogischen und didaktischen Geschicklich- keiten, für die Handhabung der Erziehungskunst und der Unterrichtskunst, und sie möchte gerade das geben, was auch die schönsten Erziehungsgrundsätze nicht ge- ben können: geistige Untergründe für die praktische Handhabung, für die innere Befähigung des Lehrers, in der Schule und in der Erziehung zu wirken.",
        "Daher ist ja auch die Waldorfschule nicht so einge- richtet, daß - wie leider oft geglaubt wird - durch sie Weltanschauung, wie wir sie vor Erwachsenen vortragen, in die Kinder hineingepfropft werden sollte."
      ],
      [
        "Wir haben daher ganz besonders zu betonen, daß sogar der Reli- gionsunterricht für die katholischen Kinder den katho- lischen Pfarrern, und für die evangelischen Kinder den evangelischen Pfarrern überlassen wird.",
        "Wir haben nur einen freien Religionsunterricht eingerichtet für dieje- nigen Kinder, die Dissidentenkinder sind, und die, wenn dieser Unterricht nicht eingerichtet worden wäre, gar keinen Religionsunterricht hätten."
      ],
      [
        "Gerade dadurch konn- te wieder etwas zur Belebung des religiösen Gefühles geleistet werden; denn gerade diejenigen Eltern, die sonst ihre Kinder dem Religionsunterricht ganz entzogen hät- ten, schicken ihre Kinder jetzt in diesen Religionsunter- richt, in welchem wir uns Mühe geben, nicht etwa An- throposophie vorzutragen, sondern das auszugestalten, was für das kindliche Alter in dieser Beziehung ausge- staltet werden muß.",
        "Also nicht darum handelt es sich, Anthroposophie in das kindliche Gemüt hineinzutragen, 85 sondern darum, daß die Lehrerschaft durch Anthro- posophie dazu kommt, die pädagogisch-didaktischen Handlungsweisen so einzurichten, daß sie nun wirklich wahrer Menschenerziehung entsprechen."
      ],
      [
        "Hieraus folgt, daß zunächst einfach durch die prakti- sche Handhabung eine solche Erziehung und ein solcher Unterricht Zustandekommen, die nicht bloß auf das Kind sehen, sondern die auf den ganzen Menschen sehen.",
        "Denn es wäre höchst töricht, etwa die Füße oder Hände eines Kindes, wie sie im kindlichen Alter sind, als etwas Fertiges zu betrachten und sie etwa zu nötigen, so zu bleiben, wie sie im kindlichen Alter sind."
      ],
      [
        "Es ist selbst- verständlich, daß wir im kindlichen Alter den kindlichen Organismus als etwas Werdendes betrachten, das später im Leben anders zu sein hat.",
        "Aber in bezug auf das Geistig-Seelische tun wir im Leben nicht immer das Gleiche."
      ],
      [
        "Wir sehen oftmals sogar, daß dem Kinde starre Begriffe beigebracht werden und das Kind häufig schon im kindlichen Alter etwas in seine Seele hereinbekommt, was scharfe Konturen hat.",
        "Das ist falsch!",
        "Es muß sich darum handeln, daß wir alles, was wir dem kindlichen Organismus einverleiben wollen, so an ihn heranbringen, daß es wachsen, daß es sich nach und nach umwandeln kann; so daß der Mensch später, im dreißigsten Jahre zum Beispiel, nicht nur eine Erinnerung an das hat, was er im kindlichen Alter aufgenommen hat, sondern daß er das damals Aufgenommene so umgestaltet hat, wie er auch seine Glieder umgestaltet hat."
      ],
      [
        "Wir müssen dem Kinde in allem, was wir ihm geistig-seelisch geben, auch etwas geben, was Wachstumskräfte, was Umwandlungs- kräfte in sich hat; das heißt, wir müssen den Unterricht lebendiger und immer lebendiger machen.",
        "Gewiß, das kann als abstraktes Prinzip ausgespro- chen werden; aber praktisch erreicht kann es nur wer- den, wenn eine wirklich intime Menschenerkenntnis vorhanden ist."
      ],
      [
        "Eine solche intime Menschenerkenntnis macht es möglich, daß man einfach von der kindlichen Natur selbst alles abliest, was man gewöhnlich unter Lehrplan und unter Lernziel versteht.",
        "Daher herrscht in der Waldorfschule ein solcher Lehrplan und sind solche Lernziele in Aussicht genommen, die aus einer wirk- lichen Menschenkenntnis heraus von Monat zu Monat aus der Entwicklung der kindlichen Natur selbst abge- lesen werden."
      ],
      [
        "Es ist der Versuch gemacht worden, wirk- lich alles in lebendigem Sinne zu gestalten.",
        "Ich will nur eines erwähnen.",
        "Es ist ja heute in ver- schiedener Beziehung auch im heutigen öffentlichen Unterricht manches besser geworden."
      ],
      [
        "Allein, Sie wissen alle, daß während des ganzen Schuljahres das Kind ei- gentlich mehr als es einem gewöhnlich bewußt wird, unter dem System leidet, das die Fortschritte des Kindes beurteilt.",
        "Da gibt es auf der einen Seite die kindlichen Leistungen, auf der anderen Seite die Beurteilungen dieser Leistungen durch den Lehrer; die werden so ausgedrückt: «befriedigend», «fast befriedigend», «fast kaum befrie- digend», «minder befriedigend» und so weiter."
      ],
      [
        "Ich muß Ihnen offen gestehen: Ich war eigentlich nie fähig, einen Unterschied einzusehen zwischen «fast befriedigend», «fast nicht befriedigend» und dergleichen.",
        "Bei uns in der Waldorfschule handelt es sich darum, daß aus der Ge- samtheit der Fortschritte heraus am Ende des Schuljah- res dem Kinde eine Art Zeugnis übergeben wird, in dem der Lehrer individuell das Kind charakterisiert, indem er einfach das, was er an dem Kinde erlebt hat, auf ein Stück Papier schreibt."
      ],
      [
        "Das Kind sieht so eine Art Spiegelbild seiner selbst, und die Praxis hat gezeigt, daß es dieses 87 Spiegelbild - worauf nicht «befriedigend», «minder be- friedigend» und so weiter für die einzelnen Gegenstände steht - mit einer gewissen inneren Befriedigung und Freude aufnimmt, selbst wenn darin Tadel stehen.",
        "Und dann bekommt das Kind eine Art Kraftspruch mit, der gerade aus seiner Natur geholt ist, den es sich dann aneignet, und der ihm ein Leitspruch für das nächste Jahr sein kann. - So kann man, wenn man die Liebe dazu hat, auf das Lebendige einzugehen, den Unterricht selbst unter ungünstigen Verhältnissen lebendig gestalten."
      ],
      [
        "Dadurch aber kommen wir auch dazu, etwas zu überwinden, was in unserem Zeitalter gerade in der Pädagogik und Didaktik überwunden werden muß.",
        "Man wird ja heute in der äußeren Geschichtsschreibung we- nig Anhaltspunkte dafür finden, wie sich die Seelenver- fassungen der Menschen in den einzelnen Entwicklungs- epochen der Menschheit geändert haben."
      ],
      [
        "Wer aber Un- befangenheit genug hat, wird schon verstehen können, wie das, was man als geistige Äußerungen zum Beispiel des 10., 11., 12.",
        "Jahrhunderts sich vor die Seele stellen kann, einen ganz anderen Charakter trägt als das, was etwa seit der Mitte des 15."
      ],
      [
        "Jahrhunderts die Seelenverfas- sung der zivilisierten Menschheit geworden ist.",
        "Ja, bis zum 20.",
        "Jahrhundert herauf hat sich der Intellektualis- mus m der Menschheit bis zu einem Kulminationspunkt entwickelt."
      ],
      [
        "Dieser Intellektualismus hat aber die Eigen- tümlichkeit, daß er - geradeso wie das Nachahmungs- prinzip oder das Autoritätsprinzip erst in einem be- stimmten Lebensalter des Menschen aus einem laten- ten in einen freien Zustand versetzt wird, und das ist beim Intellektualismus in einem verhältnismäßig späten Lebensalter der Fall.",
        "Wir sehen, wie der Mensch eigent- lich erst, wenn er die Geschlechtsreife überwunden hat, eigentlich sogar noch später, aus seiner elementaren Na- tur heraus geeignet wird, zum Intellektualistischen fort- zuschreiten."
      ],
      [
        "Vorher wirkt das Intellektualistische auf seine Seelentätigkeit durchaus ablähmend, abtötend.",
        "Daher können wir sagen: Wir leben in einem Zeital- ter, das eigentlich nur für den erwachsenen Menschen da ist, das als den wichtigsten Kulturimpuls etwas hat, was erst im erwachsenen Menschen voll zum Ausdruck kommen sollte."
      ],
      [
        "Das aber hat zur Folge, daß wir heute mit dem, was in bezug auf die ganze Kultur für die erwachsenen Menschen gerade tonangebend ist, eigent- lich das Kind und selbst den jungen Menschen nicht mehr verstehen!",
        "Das ist das wichtigste, was in unserer Zivilisation zu berücksichtigen ist."
      ],
      [
        "Wir müssen uns darüber klar sein, daß wir gerade durch diejenigen Kräfte, durch die wir unsere Wissenschaften und unsere Technik zu so großen Trium- phen und so großer Blüte gebracht haben, uns die Mög- lichkeit nehmen, das Kind voll zu verstehen und auf die volle Menschennatur des Kindes einzugehen.",
        "Es bedarf eben wieder eigener Mittel, um die Brücke zu dem jungen Menschen und dem Kinde herüber zu schlagen."
      ],
      [
        "Das, was jetzt in mannigfacher Gestalt als Jugendbewegung auftritt man mag sich dazu verhalten, wie man will -, hat seine tiefste Berechtigung; sie ist nichts anderes als der Schrei der Jugend: Ihr Erwachsenen habt eine Zivilisation, die wir einfach nicht verstehen, wenn wir uns unserer elemen- tarsten Natur hingeben! - Aber diese Brücke vom Er- wachsenen zur Kindeswelt muß wieder gefunden werden, und dazu möchte Anthroposophie das ihrige beitragen.",
        "Und wenn man dann vom allgemeinen Kulturstand- punkt zum einzelnen heruntersteigt, wird man wieder finden, wie dieser Erziehungsplan, der abgelesen ist vom 89 Wesen des Kindes selbst, uns erkennen läßt, was man im Erziehungsplan für die einzelnen Lebensphasen der Kindheit entwickeln muß."
      ],
      [
        "Schreiben und Lesen waren in früheren Zeitaltern etwas ganz anderes, als sie es heute sind.",
        "Nehmen Sie unsere heutigen Buchstaben: sie sind etwas ganz Abstraktes, Lebensfremdes im Verhältnis zum eigentlichen Leben."
      ],
      [
        "Gehen wir zu früheren Zeiten zurück: Wir finden in der Bilderschrift etwas, was sich unmittelbar an das Leben anlehnt.",
        "Wir machen uns heute oft gar keine Gedanken darüber, wie innig mit dem Leben [diese Bilderschrift] verbunden war, und wie heute dem Leben so fremd ist: Lesen und Schreiben."
      ],
      [
        "Ja, wir stehen in einer Zivilisation drinnen, der es natürlich ist, daß das Lebensfremdeste zu Zwecken der Zivilisa- tion ausgebildet wird.",
        "Wer heute mit unbefangenem Sinn zum Beispiel einen Stenographen oder einen alten Menschen an der Schreibmaschine sitzen sieht, der weiß, daß mit einer solchen Betätigung gerade das menschlich Fremdeste in die Zivilisation eingezogen ist."
      ],
      [
        "Sehr verehr- te Anwesende, man wird nicht kulturfeindlich oder zum Reaktionär, wenn man dies ausspricht.",
        "Es wird auch nichts gesagt gegenüber dem, was mit diesen Mitteln in die neuere Zeit eingezogen ist; sie mußten da sein."
      ],
      [
        "Aber es müssen auch die Gegenkräfte entwickelt werden, die das wieder heilen, was, wenn es einzig und allein wirk- sam gelassen wird, nur zu einem gewissen Niedergang der Kultur, zu einer Dekadenz führen könnte.",
        "Und das wichtigste Moment, was in dieser Beziehung als Heil- mittel eingeführt werden kann, liegt in der Erziehung, im Unterricht, der aber stets erzieherisch gestaltet wer- den muß."
      ],
      [
        "Wenn wir das Kind m die Volksschule hereinbekom- men, ist es ja so, daß sein Intellekt zunächst noch 90 schlummert.",
        "Die Fähigkeit zu abstraktem Denken, die erst von anderem belebt werden muß, diese Fähigkeit tritt erst später auf."
      ],
      [
        "Daher können wir mit den abstrak- ten Schreibe- und Leseformen an das Kind, wenn es in die Schule kommt, noch nicht herankommen.",
        "Da können wir nur das nehmen, womit wir lebendig an das Kind herankommen können, denn im Kinde selbst wirkt ja ein künstlerisches seelisches Prinzip, das vollkommener und großartiger ist als jede andere Kunst."
      ],
      [
        "Das wirkt auf unbewußte Art.",
        "Diese müssen wir fortsetzen und müs- sen versuchen, für das kindliche Alter besondere Formen zu erfinden, wodurch das Kind auf künstlerische Art in das Schreiben, das heißt in die Betätigung seines gesamten Menschen hereinkommt und dann zum Lesen übergeht."
      ],
      [
        "Man muß in bezug auf die Pädagogik, wenn die Kinder heute im achten oder neunten Jahre noch nicht lesen oder schreiben können, den Mut haben, sagen zu kön- nen: Gott sei Dank, daß die Kinder in diesen Jahren noch nicht lesen oder schreiben können! - denn es kommt nicht darauf an, daß der Mensch dieses oder jenes [früh] lernt, sondern daß er es im richtigen Lebensalter und auf eine richtige Art lernt.",
        "So ist in der Waldorfschule der Unterricht auf künst- lerische Gestaltung hin eingerichtet."
      ],
      [
        "Aus pädagogisch- künstlerischen Prinzipien heraus wird zunächst vorge- gangen und erst allmählich zum Intellektuahstischen übergeleitet.",
        "Wir tragen auch dem Rechnung, daß das Musikalische möglichst früh im Unterricht auftritt, weil es zur Willensbildung des Menschen in Beziehung steht."
      ],
      [
        "Wir tragen dem dadurch Rechnung, daß wir zu dem gewöhnlichen Turnunterricht den Eurythmie-Unterricht, das beseelte Turnen, m den Unterricht eingefügt haben.",
        "Es muß noch metamorphosiert werden, muß ins Päd- 91 agogisch-Didaktische umgesetzt werden, dann aber fin- det man, daß durch diese Bewegungskunst, die das wahrzunehmen hat, was Geist und Seele des Menschen ist, etwas vermittelt wird, was sinnvoll ist."
      ],
      [
        "Man findet, daß das Kind sich während der schulpflichtigen Erziehung in diese Bewegungskunst so hineinfindet, wie es sich als ganz kleines Kind eben in die Sprache hineinfindet, mit innerem Wohlgefallen und mit innerer Selbstverständ- lichkeit.",
        "Dieses Herausarbeiten aus dem Künstlerischen führt dann auch dahin, daß man das Kind von sehr früh an mit Farben hantieren läßt."
      ],
      [
        "Wenn das auch zuweilen unbequem ist, und -wenn dann auch schärfere Reinlich- keitsgrundsätze als sonst dabei eingreifen müssen, so wird sich doch herausstellen, daß man dadurch das Kind tiefer in das Leben einführt als sonst.",
        "Man bringt es dazu, daß es einen Sinn bekommt für das Leben, daß es nicht am Leben vorbeigeht, sondern daß es mit der äußeren Welt lebt, daß es empfänglich wird für alles Schöne, für alles, was ihm sinnvoll in Natur und Menschenleben entgegentritt."
      ],
      [
        "Und dies ist wichtiger als die Übertragung einzelner Einzelheiten aus diesem oder jenem Gebiete auf das Kind.",
        "Zu alle dem aber, was ich hier nur in seinen Richt- linien andeuten kann, kommt das, was aus anthroposo- phischen Untergründen heraus in die Gesinnung des Lehrers einfließt, was der Lehrer einfach durch sein ganzes Wesen mitbringt an pädagogisch-didaktischen Imponderabilien, wenn er die Tür des Schulzimmers hinter sich schließt nach der Klasse zu, wenn er vor die Kinder tritt."
      ],
      [
        "Wer mit lebendigem Sinn - nicht mit ab- strakten Ideen - anschaut, wie das Kind nachahmend sich anpaßt an die Umgebung, der weiß, was in diesem Kinde als Geistig-Seelisches wirkt.",
        "Er lernt das Kind 92 kennen und bekommt dadurch die Voraussetzungen, es in ganz anderer Weise zu beurteilen, als man es gewöhn- lich tut."
      ],
      [
        "Ich will dafür nur ein Beispiel anführen.",
        "Man lernt ja so manches, wenn man in diesem Sinne das Leben ansieht.",
        "Zu mir kam einmal ein Elternpaar und sagte, der junge Sohn, der bisher ganz brav und ordentlich gewesen sei, habe jetzt plötzlich gestohlen."
      ],
      [
        "Ich fragte: «Wie alt ist das Kind?» -, die Eltern antwor- teten: «Fünf Jahre».",
        "Ich sagte: «Dann muß man erst untersuchen, was das Kind eigentlich getan hat, denn vielleicht hat es gar nicht gestohlen.» - Was hatte es denn getan?"
      ],
      [
        "Es hatte einiges Geld aus der Schublade genom- men, aus der die Mutter jeden Morgen Geld nahm, wenn sie einkaufen wollte.",
        "Für dieses Geld hatte sich der Knabe einige Naschereien gekauft, die er nicht einmal für sich selbst verwendet hat, sondern die er anderen Kindern gegeben hat."
      ],
      [
        "In diesem Fall muß man sagen: Da ist gar keine Rede von Stehlen; das Kind hat einfach gesehen, was die Mutter jeden Morgen getan hat, und es fühlte sich befugt, dies selbst auch zu machen.",
        "Das Kind ist ein Nachahmer."
      ],
      [
        "Jenes Verhältnis des Kindes zu den Normen der Erwachsenen, die ihren Ausdruck finden in «gut» und «böse», tritt ja erst ein, wenn der Zahnwechsel überwunden ist.",
        "Wir müssen deshalb eine ganz andere Beurteilungsmöglichkeit gewinnen und wissen lernen: alles, was wir in der Umgebung des Kindes tun, muß so eingerichtet werden, daß das Kind es nachahmen kann, es nachahmen kann bis in die Imponderabilien der Ge- danken hinein."
      ],
      [
        "Da erweist sich eben die Realität der Gedanken.",
        "Nicht bloß das, was wir tun, sondern auch die Art und Weise unserer Gedanken ist maßgebend dafür.",
        "Wir sollen uns in der Umgebung des Kindes nicht jedem Gedanken hingeben, denn er wirkt auf das Kind. 93 Also bis auf die Imponderabilien hin müssen die Gedan- ken berücksichtigt werden."
      ],
      [
        "Schaut man darauf hin, wie das Kind bis zum sieben- ten Jahre mit seiner Umgebung lebt, dann hat man dann einen Abdruck dafür, was das Kind war, bevor der Mensch in die physisch-sinnliche Welt heruntersteigt.",
        "Bis dahin - das zeigt anthroposophische Forschung - ist der Mensch ganz umgeben von einer geistig-seelischen Welt, die so mit ihm zusammenhängt im Universum, wie hier in der physischen Welt sein Leib mit dieser."
      ],
      [
        "Und wir kommen dazu, in dem kindlichen Leben bis zum siebenten Jahre eine rechte Fortsetzung des Lebens vor der Geburt oder vor der Konzeption zu sehen.",
        "Das aber muß sich verwandeln in pädagogisch-didaktische Emp- findung, so daß der Lehrer so vor dem Kinde steht, daß er sich sagt: Mir ist aus übersinnlichen Welten etwas übergeben, das ich enträtseln muß, dem ich die Lebens- bahn ebnen muß."
      ],
      [
        "Unterricht und Erziehung wird so wirklich ein Op- ferdienst gegenüber der ganzen Welt.",
        "Es wird über Un- terricht und Erziehung etwas ausgegossen von jener Gesinnung, die eine Kraft ist, und ohne die wirklicher Unterricht und wirkliche Erziehung nichts sein können."
      ],
      [
        "Diese Gesinnung, die sich nicht aus äußerlich ange- nommener, sondern aus innerlich erarbeiteter anthropo- sophischer Weltanschauung ergibt, sie ist gerade das Allerwichtigste im pädagogisch-didaktischen Wirken.",
        "Man steht dann mit religiöser scheuer Ehrfurcht vor dem, was der kindliche Leib in sich birgt; man schaut hin, wie ein aus den ewigen Weltengründen Erstandenes nach und nach sich offenbart in den kindlichen Bewe- gungen, Gesten und so weiter, und man weiß, daß man ein Lebensrätsel in praktischer Art zu lösen hat."
      ],
      [
        "Die 94 ganze Erziehungs- und Unterrichtsgesinnung wird da- durch überhaupt erst in die richtigen Wege geleitet.",
        "Diese Atmosphäre, die sich ausbreitet bei allen Hand- lungen, die im schulgemäßen Leben getan werden müs- sen, ist das, was Anthroposophie vor allem hinein haben möchte in das Unterrichts- und Erziehungswesen, und von dem sie alle Einzelheiten beherrscht haben möchte."
      ],
      [
        "Aber um sie beherrschen zu können, ist nötig, daß man mit wirklicher innerer Anschauung dazu komme, in der kleinsten Lebensregung des Kindes zu sehen, wie der Geist fortwirkt bis in die Fingerspitzen hinein.",
        "Der Lehrer wird sich dazu eine innere Gesamtanschauung aneignen, so daß er aus einer Fähigkeit, die wiederum zum Instinkt werden muß, seiner Klasse gegenübertritt mit der Ge- sinnung und der Geschicklichkeit, die gerade aus dieser innerlichen Verarbeitung der anthroposophischen Welt- anschauung kommen."
      ],
      [
        "Das sind einige Andeutungen, die ich geben konnte; sie werden in den folgenden Vorträgen weiter ausgeführt werden können.",
        "Diese Andeutungen sollten zeigen, daß die Anthroposophie nicht radikal sein will gegen das Große, was auf pädagogischem Gebiete geleistet worden ist, sondern daß sie sein will eine Helferin für das Große, sonst nur abstrakt Bleibende, so daß es in der Lebens- praxis lebendig durchgeführt werden kann, damit die Erziehungskunst ein wirklicher Impuls, ein wirksamer Faktor in unserem sozialen Leben werden kann! 95"
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG ANTHROPOSOPHIE UND SOZIALWISSENSCHAFT Berlin, 9. März 1922",
    "paragraphs": [
      "Meine sehr verehrten Anwesenden! Noch mehr als bei den übrigen einleitenden Worten, die ich zu diesen Ta- gesunternehmungen vorauszusprechen habe, wird es heute der Fall sein, daß ich mich auf Andeutungen zu beschränken habe, da ja das Wesentliche, was zu sagen ist, in den folgenden Vorträgen über Einzelheiten des Wirtschaftslebens gerade für das heute in Betracht kommende Gebiet wird liegen müssen.",
      "Man kann heute wohl nicht über Sozialwissenschaft sprechen, wenn man nur von einem theoretischen Stand- punkte ausgeht. Man kann heute - und ich meine damit die unmittelbare Gegenwart, den gegenwärtigen Au- genblick - über solche Fragen nur sprechen, wenn man im Hintergrunde hat die trostlose Lage des Wirtschafts- lebens in der gegenwärtigen zivilisierten Welt.",
      "In diese trostlose Lage fiel in einer gewissen Weise auch noch dasjenige hinein, was ich nach der vorläufigen Beendigung der furchtbaren Weltkriegskatastrophe darzustellen ver- suchte in meinen «Kernpunkten der sozialen Frage». Ich ging dazumal aus von jener Beobachtung des sozialwirtschaftlichen Lebens, die sich eigentlich im ge- genwärtigen Zeitpunkt der Weltentwicklung jedem auf- drängen sollte.",
      "Es ist die, daß das Wirtschaftsleben der Gegenwart innig verquickt ist mit dem, was sich inner- 96 halb des ganzen Umfanges der sozialen Frage bewegt. Ja, die meisten Menschen in der Gegenwart werden wohl kaum empfinden, daß die soziale Frage getrennt werden könne von der wirtschaftlichen Frage.",
      "Und dennoch ging gerade mein Buch «Die Kernpunkte der sozialen Frage» darauf aus, dadurch Klarheit zu schaffen in bezug auf das hier in Betracht kommende Gebiet, daß dar- auf hingewiesen wurde, wie das Wirtschaftsleben inner- halb des sozialen Organismus seine eigene selbständige Stellung erhalten müsse, jene selbständige Stellung, durch welche innerhalb desselben die Tatsachen und Ein- richtungen lediglich nach wirtschaftlichen Grundsätzen, wirtschaftlichen Gesichtspunkten und Impulsen ihre Gestaltung bekommen. Insofern enthält eigentlich mein Buch - ich sage es hier m ganz unumwundener Weise, weil gerade darauf außerordentlich viel ankommt - einen inneren Widerspruch.",
      "Allein, dieses Buch wollte nicht ein theoretisches Buch der Sozialwissenschaft sein. Die- ses Buch wollte Anregungen geben vor allen Dingen den Lebenspraktikern; dieses Buch wollte aus dem heraus geschrieben sein, was man in jahrzehntelanger Beobach- tung des europäischen Wirtschaftslebens sich aneignen konnte.",
      "Und indem so dieses Buch anstrebte, durch und durch realistisch zu sein, unmittelbar eine Anregung für praktisches Handeln zu sein - und zwar für praktisches Handeln im Augenblick -, mußte es ja einen Wider- spruch enthalten. Dieser Widerspruch ist nämlich kein anderer als der, der unser ganzes soziales Leben durch- zieht, und der darin besteht, daß dieses soziale Leben im Laufe der neueren Zeit durcheinander, chaotisch das gebracht hat, was nur dann lebensfähig ist, wenn es sich aus seinen eigenen Bedingungen in jedem seiner einzel- nen Glieder entwickelt. 97 Ich mußte sprechen von einer Dreigliederung des sozialen Organismus, die dazu führen würde, daß das Wirtschaftsleben in völlig freier Weise, relativ abgeson- dert sich organisiert von dem Rechts- und Staatsleben und von dem geistigen Leben, daß also dieses Wirt- schaftsleben von denjenigen, die in ihm drinnen stehen, die aus seinen eigenen Impulsen heraus handeln können, gestaltet wird.",
      "Nun aber leben wir ja zunächst in einer Zeit, in welcher ein solcher Zustand nicht da ist, in welcher das Wirtschaftsleben absolut drinnen steht in der übrigen Struktur des sozialen Organismus. Wir leben in einer Zeit, in welcher der Widerspruch eine Realität ist.",
      "Daher konnte eine Schrift, die aus der Realität heraus geschrieben sein wollte und für die Realität Anregungen bieten wollte, nur etwas Widerspruchsvolles wiederum bringen; sie konnte nur darauf ausgehen, aus dem Wi- dersprechenden heraus zunächst zur Klarheit, zur Klä- rung der Verhältnisse aufzurufen. Ich bin deshalb heute in einer ganz besonderen Lage, indem ich diese Einleitung spreche, weil in bezug auf dasjenige, was auf anthroposophischem Boden, mit an- throposophischen Denkmethoden gefunden worden ist, aber gefunden worden ist aufgrund durchaus realisti- scher, jahrzehntelanger Beobachtung der europäischen Wirtschaftsverhältnisse - weil das doch in den weitesten Kreisen zunächst in der ärgsten Weise mißverstanden worden ist.",
      "Ich kann nur sagen: Ich begreife vollständig diese Mißverständnisse, die diesen zugrunde liegenden Absichten entgegengebracht worden sind; diese Mißver- ständnisse sind eben auch ein Zeitphänomen. Allein, ich muß auf der anderen Seite der Anschauung sein, daß in der Überwindung dieser Mißverständnisse dasjenige liegt, was wir zunächst auf soziologischem, auf sozialem Ge- 98 biete anzustreben haben, und gerade dazu möchte ich einiges Orientierende sagen.",
      "Als mein Buch «Die Kernpunkte der sozialen Frage» zuerst veröffentlicht wurde, fiel es in eine Zeit mittel- europäischer Entwicklung, die unmittelbar gefolgt war der furchtbaren Kriegskatastrophe. Es war eine Zeit, die dem Versailler Vertrag vorangegangen war; es war eine Zeit, in welcher die Valutaverhältnisse der mitteleuro- päischen und der osteuropäischen Staaten noch wesent- lich andere waren.",
      "Nicht aus irgendeinem Wolkenkuk- kucksheim heraus waren die Impulse gemeint, die damals in meinen «Kernpunkten» niedergeschrieben wurden, sondern sie waren aus der unmittelbaren Weltsituation der damaligen Zeit heraus so gedacht, daß ich glauben durfte, wenn eine größere Anzahl von Menschen sich fände, welche auf Grundlage dieser Anregungen Weite- res suchte, dann würde man - namentlich von Mitteleu- ropa aus - einen Impuls auch in die wirtschaftliche Entwicklung hineinwerfen können, der zu einer Art von Aufstieg führen könnte in dem ja damals deutlich ver- nehmbaren und bis heute andauernden Abfall des Wirt- schaftslebens und des sozialen Lebens überhaupt. Man konnte damals sich sagen, wenn man aus den sehr komplizierten Verhältnissen der Weltsituation heraus dachte: Vielleicht bleibt kein Stein stehen, so wie er hineingebaut ist in das Ideengebäude der «Kernpunkte der sozialen Frage» -; aber diese Ideen waren überall herausgedacht aus demjenigen, was war.",
      "Doch man könnte sie angreifen, und es wäre vielleicht etwas ganz anderes herausgekommen, als man zunächst schriftlich fixieren konnte. Denn nicht darauf kam es an, Ideen in utopistischer Weise hinzustellen, die ein Bild etwa eines sozialen Zukunftsorganismus entwerfen wollten; son- 99 dern darauf kam es an, Menschen zu finden, welche verstanden: Hier hegen reale, unmittelbar im Leben vorhandene Probleme vor; wir müssen uns aus unserer Sachkenntnis heraus mit diesen Problemen befassen und müssen sehen, ob wir, indem wir uns mit diesen Pro- blemen befassen, dann immer weiteres und weiteres Verständnis finden.",
      "Nun ist im Grunde genommen etwas ganz anderes eingetreten. Es haben sich auf der einen Seite wohl Theoretiker gefunden, welche über das, was in meinem Buche steht, allerlei Diskussionen gepflogen haben, welche an das dort Ausgesprochene allerlei Forderungen geknüpft haben.",
      "Es hat auch Theoretiker gegeben, die in vollständig mißverstehender Art das, was gesagt war, in utopistischem Sinne umdeuteten und immer wieder fragten: Wie wird sich dieses, wie wird sich jenes ge- stalten?, - was man ja eigentlich hätte abwarten müssen. Es hat sich sogar die merkwürdige Tatsache herausge- stellt, die für mich ganz überraschend war, daß gerade die wirtschaftlichen Praktiker, die in irgendeinem Ge- biete des Wirtschaftslebens mit ihrer Routine ganz gut drinnenstanden, die sich in diesem oder jenem Ge- schäftszweige auskannten und es abgelehnt hätten, sich in ihrem Geschäftszweige etwas hereinreden zu lassen von dem, der nicht gerade in diesem Geschäftszweig versiert war , daß diese Praktiker diskutierten über die Kernpunkte der sozialen Frage und sich durch das, was von ihnen als Folgerung gezogen wurde, gerade als die abstraktesten Theoretiker erwiesen.",
      "Es zeigte sich, daß man im Wirtschaftsleben ganz gut ein routinierter Prak- tiker sein konnte - im alten Sinne; unter den neuen Verhältnissen kannten sie sich nicht mehr aus -, daß aber diese Praktiker absolut nicht in der Lage waren, das, was 100 hier angeschlagen war in bezug auf die Probleme auch des Wirtschaftslebens, anders als gerade von dem Ge- sichtspunkte der abstraktesten Theorien aus zu diskutie- ren; so daß man da gerade in Verzweiflung kommen konnte, wenn man Praktikern gegenüberstand und sich mit ihnen eine Diskussion entwickelte, wo sie durchaus nicht auf etwas Konkretes eingingen, sondern nur das völlig triviale Allgemeine über die soziale Frage und namentlich über den wirtschaftlichen Teil der sozialen Frage wiederholten, wenn man sich mit ihnen irgendwie darüber aussprach. Das andere, was einem da entgegentreten konnte, war, daß zunächst ja diejenigen, die nun so die ganz handfesten Praktiker sind, es überhaupt ablehnten, sich in solcher Weise über die mögliche Gestaltung der wirtschaftlichen Probleme zu unterhalten.",
      "Das Weitere war, daß ja einiges Interesse zum Beispiel in sozialistischen Kreisen erweckt werden konnte, daß man aber gerade dort die Erfahrung machen konnte, daß das, was gewollt war, am allerwenigsten von dieser Seite verstanden wurde, und daß alles nur danach beurteilt wurde, ob es sich in die alten Parteischablonen einfüge oder nicht. Und so verging jene Zeit, aus der heraus diese Anregungen ge- dacht waren.",
      "Es kam das ganze furchtbare Valuta-Elend, das aber in einer ganz anderen Weise eigentlich zu be- urteilen ist, als man es heute gewöhnlich beurteilt. Als zuerst mein «Aufruf an das deutsche Volk und an die Kulturwelt» und dann die «Kernpunkte der so- zialen Frage» erschienen waren, da zeigte sich sogleich, wie einzelne Persönlichkeiten, die es ja in ihrer Art mit einer Gesundung des mitteleuropäischen Wirtschaftsle- bens ganz ehrlich meinten, sagten: Ja, solche Vorschläge - sie nannten das Vorschläge - sind ja ganz schön, aber 101 es sollte zunächst einmal gesagt werden, wie wir zu einer Aufbesserung der Valuta kommen.",
      "Das wurde in Zeiten gesagt, als das Valuta-Elend gegenüber den heu- tigen Verhältnissen noch das reine Paradies war. Nun zeigt sich in solchen Forderungen, wie man überall nur an den äußeren Symptomen herumpfuschen will.",
      "Es zeigt sich wenig Verständnis dafür, daß ja in den Valuta- verhältnissen nur die an die Oberfläche schlagenden ungesunden Wirtschaftsverhältnisse sich symptomatisch anzeigen, daß man mit einer solchen Symptomenkur überhaupt das Übel gar nicht anpackt, und daß es sich darum handelt, viel tiefer und tiefer in die sozialwirt- schaftlichen Zustände der Gegenwart hineinzugehen, wenn man in irgendeiner Weise dazu kommen will, die Probleme realistisch zu besprechen, für die die Andeu- tung gegeben werden sollte in den «Kernpunkten der sozialen Frage». Und so ist es denn gekommen, daß das, was ich wiederholt am Schlüsse von Vorträgen, die ich im Anschlüsse an die «Kernpunkte» hielt, damals gerufen habe: man solle sich besinnen, ehe es zu spät ist -, daß dieses «Zu spät!» in einem hohen Grade heute eingetreten ist, daß wir gar nicht mehr in der Lage sind, in dem ursprünglichen Sinne, der die «Kernpunkte» durchpulst, die Sache anzufassen; denn mittlerweile ist das Chaos des Wirtschaftslebens so hereingebrochen, daß wiederum ganz andere Ergänzungen notwendig wären zu dem, was dazumal nicht bloß ausgesprochen werden sollte, sondern ausgesprochen werden mußte, meiner Über- zeugung nach.",
      "Und man wird wohl doch kaum vor- übergehen können an einer Charakteristik unseres Zeit- alters im allgemeinen, wenn man das besprechen will, was heute auch dem Wirtschaftsleben am allerschäd- lichsten ist. 102 Als ich gestern ein Zeitungsblatt in die Hand nahm, da trat mir - und es können einem heute ja die wichtig- sten Symptome gewissermaßen aus einzelnen Sätzen, die heute unsere Zeitgenossen aussprechen, überall entge- gentreten -, es trat mir ein Artikel entgegen: «Verschie- bung der Demission des Lloyd George bis nach der Konferenz von Genua». Damit war wieder einmal die heutige Tagessituation ausgesprochen, indem alles, was heute den Tag charakterisiert, «wartet».",
      "«Wir wollen warten» - das ist eigentlich heute überall das Prinzip; warten, bis irgend etwas geschieht, von dem man nicht sagen kann, was es eigentlich sein wird. Was da gesche- hen soll, weiß man nicht, aber man wartet, bis es ge- schehen ist!",
      "Das ist das, was heute den Leuten tief in den Seelen sitzt, auf allen Gebieten. Und nun möchte ich etwas scheinbar aber nur scheinbar - recht Abstraktes vorbringen; aber auch das ist durchaus in realistischem Sinne gemeint, denn es weist hin auf die unter uns wirksamen Kräfte, durch die wir eigentlich im Laufe der Menschheitsentwicklung allmählich dazu gekommen sind, dieses so aussichtsvolle Prinzip «wir wollen war- ten» überall geltend zu machen.",
      "Wenn wir in ältere Kulturentwicklungen zurückblik- ken, so finden wir gerade bei diesen älteren Kulturen, daß ein eigentliches wissenschaftliches Denken, auch in dem Sinne, wie es in den alten Zeiten vorhanden war - Sie wissen das ja aus dem Vortrage, den ich hier zuletzt in der Philharmonie gehalten habe -, nicht rein «wissen- schaftlich» zu nennen ist. Sieht man aber auf das, was an Stelle des heutigen wissenschaftlichen Denkens stand, so kann man wissen, daß aus jenem Denken zunächst nicht unmittelbar das wirtschaftliche Leben hervorgegangen ist.",
      "Das wirtschaftliche Leben hat sich zunächst mehr 103 oder weniger unabhängig von dem menschlichen Ge- danken, wie instinktiv - um nicht zu sagen automatisch - im Wechselverkehr der Menschheit entwickelt. Was man im wirtschaftlichen Leben hat tun wollen, hat sich einfach aus der Lebenspraxis heraus entwickelt.",
      "Man hat instinktiv gehandelt, hat ja wohl auch den Bereich des Handels erweitert über dieses oder jenes Gebiet, aber alles ist eben mehr oder weniger instinktiv geschehen. Man mag nun das eine oder andere einwenden vom Gesichtspunkte der heutigen Auffassungen von Men- schenfreiheit, Menschenwürde und so weiter gegen die wirtschaftlichen Zustände älterer Zeiten; allem, man wird gut tun, auch auf der anderen Seite zu sehen, wie ganz merkwürdige Symptome in der Menschheitsentwicklung, die auch heute noch lehrreich sein können, sich zum Beispiel zeigen in der Art und Weise, wie Arbeitnehmer und Arbeitgeber - wenn wir diese modernen Ausdrücke auf alte Zeiten anwenden wollten - im Verhältnis zuein- ander lebten im alten Griechentum, im alten Ägypter- tum, bis nach Asien hinüber.",
      "Diese Dinge nehmen sich gegenüber den heutigen Empfindungen so aus, daß sie eben die schärfste Kritik selbstverständlich herausfor- dern; allein, jede solche Kritik ist eben unhistorisch, und man muß sagen: Es waren eben diejenigen Verhältnisse in den entsprechenden Zeitepochen da, die sich aus dem damaligen Empfinden jener Menschheit ergaben. Das ist das eine, was man ins Auge fassen muß.",
      "Das andere ist die Tatsache, die zusammenhängt mit jenem Umschwung in der Menschheitsentwicklung, auf den ich schon öfters hindeuten mußte, der etwa im 15. Jahrhundert liegt, und durch den die Seelenverfassung der zivilisierten Menschheit eine ganz andere geworden ist.",
      "Ich sagte schon: Die äußere Geschichte weist wenig 104 darauf hin, wie damals die Gesamtlebensauffassung der menschlichen Seele eine andere geworden ist. Und wenn wir uns dann fragen: Wie steht diese menschliche Ent- wicklung zum Wirtschaftsleben? - dann bekommen wir die Antwort: Die Zeit der instinktiven Führung des Wirtschaftslebens, die so war, wie ich sie eben charakte- risiert habe, diese Zeit reichte noch herein bis in die Epoche dieses Umschwunges.",
      "Mit diesem Umschwünge kam dann herauf in die Seelenverfassung der Menschheit der Intellektualismus, der Drang, mit reiner Verstan- deslogik die Welt zu begreifen. Dieser Drang, der einfach ein tiefes Bedürfnis der menschlichen Seelenverfassung wurde, er bewährte sich ja in so glänzender Art gerade auf naturwissenschaftlichem Gebiete und auf jenem Gebiete, das aus der Naturwissenschaft in so glänzender Weise sich herausgebildet hat: auf dem Gebiete der Technik, wo er die außerordentlichsten, nicht genug anzuerkennenden Triumphe gefeiert hat.",
      "Aber dieser Intellektualismus - und das werden doch verschiedene Auseinandersetzungen gezeigt haben, die hier auch wäh- rend dieses Kursus schon gepflogen worden sind - hat sich völlig unfähig gezeigt, die Erscheinungen des Menschenlebens und Menschenwesens selbst, auch in sozialer Beziehung, zu ergreifen. Man kann mit diesem Intellektualismus, mit dieser intellektualistischen Orien- tierung der Seele in grandioser Weise die äußere sinnli- che Natur auf ihre Gesetzmäßigkeiten zurückführen.",
      "Man kann aber nicht mit diesem Intellektualismus diese sich ineinander verschlingenden und während des Ver- schlingens sich organisierenden und während des Orga- nisierens sich seelisch auslebenden und geistig sich durchdringenden Verhältnisse des sozialen Lebens er- greifen. Ich möchte sagen: Das Netzwerk intellektuali- 105 stischer Ideen ist einfach zu weitmaschig für das, was im sozialen Leben vorliegt.",
      "Aber wissenschaftlich zu denken - das hat die Menschheit gelernt an diesem Intellektua- lismus. In ihn ist ja zuletzt alles einbezogen worden, bis in die Theologie hinein. Der Intellektualismus beherrscht, wenn wir auch beobachten und experimentieren, doch unsere ganze wissenschaftliche Denkweise, und wir haben es zuletzt dahin gebracht, das, was nicht in die Bahnen des Intellektualismus hineingebracht wird, ein- fach als nicht wissenschaftlich anzusehen.",
      "In diese Zeit des Intellektualismus fiel nun hinein der Übergang von dem rein instinktiven zu demjenigen Wirtschaftsleben, das angefacht werden soll mit mensch- lichen Gedanken. Wir dürfen sagen: In der Zeit, wo man noch nicht intellektualistisch über die Welt gedacht hat, wurde das Wirtschaftsleben instinktiv geführt.",
      "Als aber die Zeit heraufkam, die immer mehr und mehr nach Weltwirtschaft und Weltverkehr hintendierte, wurde der Mensch aus dieser Tendenz nach Weltverkehr und Weltwirtschaft dazu angehalten, auch das Wirtschaftsle- ben nun mit Gedanken zu durchdringen. Diese Gedan- ken aber wurden allein aus dem Intellektualismus heraus genommen.",
      "Dadurch zeigte sich in allem, was als wirt- schaftswissenschaftliche Gedanken heraufgezogen ist - im Merkantilismus, im Physiokratismus, in den natio- nalökonomischen Ideen eines Adam Smith, wie in allem, was dann später hervorgetreten ist bis zu Karl Marx -, daß auf der einen Seite das Wirtschaftsleben forderte, daß nicht mehr bloß instinktiv gewirtschaftet würde, sondern daß es mit Gedanken erfaßt werde, daß aber auf der anderen Seite, da die Gedanken nur hergenommen werden konnten aus dem Intellektualismus, damit alle wirtschaftlichen Anschauungen durch und durch einseitig 106 wurden, so daß aus diesen wirtschaftlichen Anschauun- gen niemals eigentlich etwas hervorging, was man fort- wirken gesehen hätte in der wirtschaftlichen Praxis. Auf der einen Seite waren die Wirtschaftstheoretiker, die aus intellektualistischen Sätzen Axiome bildeten - wie zum Beispiel Ricardo, Adam Smith oder John Stuart Mill -, und die auf solchen Axiomen Systeme aufbauten, womit sie eine ganz in sich verlaufende Geistesart bildeten; auf der anderen Seite war die wirtschaftliche Praxis, die eigentlich einer Durchdringung mit dem Geist bedurft hätte, die diese Durchdringung geradezu forderte, aber keinen Anschluß fand, die im alten Instinktleben fort- wirkte und daher in das vollständige Chaos verfiel.",
      "So waren diese zwei Strömungen in der neueren Zeit immer mehr gang und gäbe geworden: auf der einen Seite die Wirtschaftstheoretiker - ohne Einfluß auf die wirtschaftliche Praxis; auf der anderen Seite die Prakti- ker, welche die alte, zur Routine gewordene Praxis fort- setzten, und damit das Wirtschaftsleben der zivilisierten Welt in das Chaos hineinwarfen. - Man muß selbstver- ständlich solche Dinge in einer etwas radikalen Weise aussprechen, denn nur dadurch wird wirklich auf das hingedeutet, was ist, was wirksam ist und was als Problem aufgefaßt werden muß. Wenn man nun, ich möchte sagen, eine Art Ver- bindung, eine Art Synthese zwischen wirtschaftlichem Denken - das aber von der Praxis allmählich ganz ausge- rottet worden ist - und dieser wirtschaftlichen Praxis sucht, so findet man diese Verbindung höchstens in einem.",
      "In der neuesten Zeit bildete sich nämlich heraus eine Art von wirtschaftlichem Realismus, eine Art wirt- schaftlich-wissenschaftlicher Realismus, der da sagt, man könne überhaupt nicht so allgemein zu Gesetzen des 107 Wirtschaftslebens kommen, sondern man müsse die Tat- sachen der Wirtschaft betrachten, wie sie sich bei ein- zelnen Nationen oder Menschengruppen abspielen, und nur wenn man in dieser Weise rein äußerlich betrachtet, was geschehen ist, könne man einige Richtlinien für das wirtschaftliche Handeln finden. Was aus diesen Unter- gründen heraus entstanden ist, das ist das, was dann als die sogenannte sozialpolitische, als die wirtschaftli- che Gesetzgebung aufgetreten ist.",
      "Das heißt, man hat allmählich geglaubt, herausgefunden zu haben, daß man zwar durch die Betrachtung der tatsächlichen wirt- schaftlichen Verhältnisse im Zusammenhange mit den sie durchsetzenden sozialen Verhältnissen gewisse Richt- linien bekommen könne, die man dann in der wirtschaft- lichen Gesetzgebung zum Ausdruck brachte; man hat also auf dem Umwege durch den Staat versucht, einiges von dem zu verwirklichen, was aus den Beobachtungen hervorgegangen ist, aber dadurch hat man in Wirklichkeit selbst zugegeben, daß aus diesen Beobachtungen wirk- liche wissenschaftliche Wirtschaftsgesetze gar nicht hervorgehen können. Ja, in dieser Situation steht man eigentlich im Grunde genommen heute noch drinnen.",
      "Und gerade, wenn man in der Lage ist, einschneiden- de Erfahrungen zu machen und, ich möchte sagen, so- ziale Urphänomene in der richtigen Weise zu werten, dann sieht man, wie man in dieser Situation drinnen steht. Sie wissen ja alle, daß in das in ein so furchtbares Chaos hineingehende Zivilisationsleben in einem gewis- sen Zeitpunkte die sogenannten «Vierzehn Punkte» Woodrow Wilsons fielen.",
      "Was waren diese Vierzehn Punkte denn eigentlich? Sie waren im Grunde genommen nichts anderes als die abstrakten Prinzipien eines welt- 108 fremden Mannes, die abstrakten Prinzipien eines Men- schen, der von der Wirklichkeit wenig wußte, wie sich dann in Versailles, wo er in der Wirklichkeit eine her- vorragende Rolle hätte spielen können, gezeigt hat.",
      "Ein wirklichkeitsfremder Mann wollte aus dem Intellektua- lismus heraus der Welt zeigen, wie sie sich organisieren sollte. Man muß nur erlebt haben, mit welcher Begei- sterung die zivilisierte Menschheit an diesen Vierzehn Punkten hing, allerdings mit Ausnahme eines großen Teiles der mitteleuropäischen Bevölkerung, für die es aber leider auch einen, wenn auch kurzen Zeitraum gab, in dem sie auf diese Vierzehn Punkte hereinfiel.",
      "Im Jahre 1917 versuchte ich demgegenüber, einzelnen Persönlichkeiten Mitteleuropas, die sich dafür interes- sierten, denen aber nicht nachgelaufen wurde, sondern die entweder herankamen oder herangebracht wurden, zu zeigen, wie abstrakt, wie wirklichkeitsfremd dasjeni- ge ist, was da in die soziale Gestaltung der Welt herein will, wie sozusagen alles das, was an schlechten Erzie- hungsgrundsätzen m der modernen Zivilisation waltet, kondensiert in diesem Weltschulmeister Woodrow Wil- son sich darstellte, und wie die abstrakten Grundsätze dieser - im schlechten Sinne - Weltschulmeisterei von den Leuten mit Begeisterung aufgenommen wurden. Dazumal versuchte ich zu zeigen, daß eine Gesundung dieser Verhältnisse nur eintreten könne, wenn man ge- genüber allen solchen abstrakten Einstellungen sich auf den Boden stellt, der die Gedanken nicht ausschließt, der aber gerade die Gedanken so hervorbringt, daß sie aus der Wirklichkeit, aus der Realität herauswachsen.",
      "Dann darf man sich aber nicht irgend etwas Utopistisches ausdenken - ich möchte sagen, die Woodrow Wilson- schen Grundsätze waren der verdichtetste Utopismus, 109 waren der Utopismus in der dritten Potenz schon -, sondern dann muß man sich klar sein, daß man aus den realen Bedingungen der gegenwärtigen Menschheit selbst suchen muß, wie Impulse zu finden sind. Daher verzich- tete ich bei dem, was ich auseinanderzusetzen hatte, auf jede utopistische Theorie, verzichtete darauf, überhaupt zu sagen, wie sich etwa Kapital, wie sich Arbeit und dergleichen gestalten sollten; ich gab höchstens einige Beispiele dafür, wie man sich denken könne, daß sie sich aus den gegenwärtigen Verhältnissen heraus in eine nächste Zukunft hinein gestalten könnten.",
      "Das aber war alles nur zur Illustration dessen gesagt, was sie werden sollten; denn ebenso gut wie ich da über die Wandlung der Kapitalkräfte in meinen «Kernpunkten» gesprochen habe, ebenso gut könnte diese Wandlung auch in einer modifizierten Weise sich vollziehen. Nicht darauf kam es mir an, ein abstraktes Zukunftsbild hinzustellen, sondern zu sagen, aus welchen Untergründen heraus, auf reale Art, man nun - nicht zu einer theoretisch ausge- dachten, sondern zu einer wirklichen Lösung der soge- nannten sozialen Frage kommen könnte.",
      "Es handelte sich nicht darum, zu sagen: Dies oder jenes ist die Lösung der sozialen Frage. Um eine solche Lösung zu versu- chen, dazu habe ich nun wirklich zu viele Erfahrungen gemacht. Ich war schon in den 80er Jahren des vori- gen Jahrhunderts in dem gemütlichen Wien fast jeden Nachmittag nach zwei Uhr eine Stunde zusammen mit allen möglichen gescheiten Leuten.",
      "Da ist im Verlaufe einer Stunde die soziale Frage jeden Nachmittag mehr- mals gelöst worden! Und derjenige, der unbefangen ge- nug in die Verhältnisse der Gegenwart hineinsieht, weiß schon ganz gut, daß Lösungen, die heute oftmals in dicken Büchern auftreten, auch nicht viel mehr wert 110 sind, als die, welche damals in Wien mit einigen Bleistift- strichen und vielen fanatischen Worten über einer wei- ßen Tischplatte verhandelt worden sind.",
      "Darum konnte es sich also nicht handeln, und das war das ärgste Miß- verständnis, das mir entgegengebracht wurde, daß es sich um so etwas handeln sollte. Was ich zeigen wollte, war: Die Lösung des sozialen Problems kann nur auf reale Weise selbst erfolgen; diese Lösung kann überhaupt nicht durch Diskussionen, son- dern nur durch Geschehen, durch Tätigkeit erfolgen.",
      "Zu dieser Tätigkeit müssen aber erst die Bedingungen hin- gestellt werden, und auf diese Bedingungen versuchte ich in meinen «Kernpunkten» und in anderen Auseinan- dersetzungen zu verweisen. Ich versuchte zu zeigen, daß wir in unserem sozialen Organismus einmal solche Ein- richtungen brauchen, die es ermöglichen, daß ein Gei- stesleben aus seinen eigenen Bedingungen heraus sich entwickeln kann, wo also nur die Bedingungen des Geisteslebens selbst wirken; daß wir sodann ein zweites Glied brauchen, wo nur die rechtlich-staatlichen Impul- se wirken, und außerdem ein drittes Glied, wo nur dieje- nigen Impulse wirken, die aus der Warenproduktion und der Warenkonsumtion hervorgehen, und die zu- letzt, wenn sie sich aus einem assoziativen Wirtschafts- system entwickeln, gipfeln müssen in einer gesunden Preisbildung.",
      "Damit sollten nicht etwa die alten Stände wieder ins Dasein zurückgerufen werden. Nicht die Menschen sollten sich gliedern in einen Lehrstand, einen Wehrstand und einen Nährstand; sondern der Mensch der neueren Zeit ist bis zur Individualität vorgeschritten, und er wird nicht in abstrakter Weise eingegliedert sein in einen bestimmten Stand.",
      "Aber was draußen als Ein- richtungen vorhanden ist, das tendiert einfach aus den 111 Kräften, die im geschichtlichen Werden vorhanden sind, dazu, daß abgesondert aus den eigenen Bedingungen heraus verhandelt wird, etwas getan wird für das Gei- stesleben, für das Rechts- oder Staatsleben und für das Wirtschaftsleben. Dann erst, wenn die Bedingungen dazu geschaffen sind, daß zum Beispiel der Wirtschafter rein aus wirtschaftlichen Impulsen heraus das gestalten kann, was etwa die gegenwärtigen Marktverhältnisse modifi- zieren soll, oder was die gegenwärtigen Kapitalverhält- nisse modifizieren soll, erst wenn solche Möglichkeiten geschaffen sind, entwickelt sich unter den Menschen dasjenige, was eine reale Lösung - die aber in fortwäh- rendem Werden ist - der sozialen Frage genannt werden kann.",
      "Also es geht mir nicht darum, die soziale Frage zu lösen, weil ich der Meinung sein mußte, daß überhaupt diese Lösung nie in einem einzelnen Moment als etwas Abgeschlossenes gegeben werden kann, weil das soziale Problem, nachdem es einmal heraufgekommen ist, in fortwährendem Fluß ist. Der soziale Organismus ist etwas, was jung wird, altert, und dem immer neue Impulse eingeflößt werden müssen, von dem aber nie gesagt werden kann: so und so ist seine Gestalt.",
      "Wenn der soziale Organismus nicht so ist, daß die Menschen in einem, alle Interessen zusammenmischenden Parlament zusammensitzen, wo dann wirtschaftlich Interessierte über Fragen des Geisteslebens, staatliche Interessen über wirtschaftliche Fragen und so weiter entscheiden, sondern wenn in einem gesunden sozialen Organismus die ein- zelnen Gebiete aus ihren eigenen Bedingungen heraus betrachtet werden, dann wird einmal das Staatsleben auf eine reale demokratische Grundlage gestellt werden können; dann wird das, was zu sagen ist, nicht von einem 112 Menschen in einem solchen einzigen Parlament gesagt werden, sondern es wird hervorgehen aus den fortdau- ernden kontinuierlichen Verhandlungen unter den ein- zelnen Gliedern des sozialen Organismus. In diesem Sinne war also mein Buch eine Mahnung dazu, endlich aufzuhören mit dem unfruchtbaren Reden über die soziale Frage und sich auf einen Boden zu stellen, von dem aus man jeden Tag die Lösung der sozialen Probleme in die Hand nehmen kann.",
      "Es war ein Ruf, der an die Verstehenden ging, um wirklich das, was immer nur im Abstrakten gedacht war, überzuführen in das durchdachte Handeln. Dazu sollten zum Beispiel im wirtschaftlichen Leben die Assoziationen dienen.",
      "Solche Assoziationen sind grundverschieden von dem, was in der neueren Zeit an Vergesellschaftungen zustande ge- kommen ist, und können jeden Tag aus den wirtschaft- lichen Untergründen gebildet werden. Bei ihnen handelt es sich darum, daß nun wirklich diejenigen Menschen, die im Behandeln von Warenproduktion, von Waren- zirkulation und im Konsumieren von Waren verbunden sind - was jeder Mensch ist -, sich zu Assoziationen zusammenschließen, so daß daraus vor allem die gesun- de Preisbildung hervorgeht.",
      "Es ist ein langer Weg von dem, was aus Sach- und Fachkenntnis heraus die in den Assoziationen verbundenen Menschen werden zu leisten haben, bis zu dem, was nicht durch eine Gesetzgebung, auch nicht als Resultat von Diskussionen, sondern als Resultat der Erfahrung sich ergibt als die gesunde Preis- bildung. Doch vor allem hatten Menschen das Bedürf- nis, die Grundzüge dessen, was damals gewollt wurde und was ich jetzt m diesen einleitenden Worten vor Sie hinzustellen versuchte, zu diskutieren; denn die Welt war so eingeschult in abstraktes Denken, daß man auch 113 diese Anregung nur vom Gesichtspunkte des abstrakten Denkens nahm, und daß man sich mit dem, was ich nur als Illustration gegeben habe, vor allem so hilft, daß man stundenlang diskutiert, während es sich darum handeln sollte, wirklich einzusehen, wie jeden Tag die Gliederung des sozialen Organismus in Angriff genommen werden kann in der Weise, wie es in den «Kernpunkten» ange- deutet ist.",
      "So handelt es sich heute nicht darum, theoretische Lösungen der sozialen Frage zu suchen, sondern die Bedingungen aufzusuchen, unter denen die Menschen sozial leben werden. Und sie werden sozial leben, wenn der soziale Organismus nach seinen drei Gliedern hin arbeitet, wie ja der natürliche Organismus auch unter dem Einfluß seiner relativen Dreigliederung gerade zur Einheit hin arbeitet.",
      "Sehen Sie, man muß heute erst einmal sagen, wie solche Dinge gemeint sind. Und wenn man sie aus- spricht, wird immer noch gefordert, daß nun die Worte, deren man sich schon einmal bedienen muß, so genom- men werden sollen, wie man sie nimmt nach der intellek- tualistischen Bedeutung, die man ihnen heute beilegt.",
      "Man übersetzt sofort in seinen Intellektualismus das, was ganz ausdrücklich nicht in Intellektualismus einge- taucht ist. Daher ist über Kapital, über die Naturgrund- lagen der Produktion, über die Arbeit in meinem Buche so gesprochen, daß die Ideen einfach für das Leben gedacht sind.",
      "Wenn wir abstrakt verhandeln, können wir lange definieren, und das ist ja auch geschehen. Der eine sagt mit demselben Recht: Kapital ist kristallisierte Ar- beit, ist Arbeit, die aufgespeichert ist -, wie der andere mit demselben Recht sagt: Kapital ist ersparte Arbeit.",
      "Und so kann man es mit allen volkswirtschaftlichen 114 Begriffen machen, wenn man innerhalb des Intellektua- lismus stehen bleibt. Aber das alles sind nicht Dinge, mit denen man es nur theoretisch zu tun haben kann, sondern die man lebendig in ihrer Gestaltung erfassen muß.",
      "Und wer sich wie die Praktiker, die viel auf ihre Praxis und Routine sich zugute tun, der Abstraktheit in diesen Dingen befleißigt, der kann folgendes machen, was ich durch einen Vergleich verdeutlichen will. Ich sehe den Ernst Müller.",
      "Er ist klein, hat durchaus kindliche Züge und kindliche Eigenschaften. Ich sehe diesen Ernst Müller nach zwanzig Jahren wieder und sage: Das ist nicht der Ernst Müller, denn der ist klein, hat kindliche Eigenschaften und eine ganz andere Phy- siognomie. -Ja, wenn ich mir damals meinen Begriff von dem Ernst Müller gebildet habe und ihn nun nach zwanzig Jahren zur Deckung bringen will mit dem, was mir jetzt als reale Wesenheit entgegentritt, so mache ich einen furchtbaren Fehler.",
      "Doch so wenig es die Menschen glauben mögen: es ist so, wenn sie heute wirtschaftlich denken. Sie machen sich Gedanken und Begriffe über Kapital und Arbeit und so weiter, und sie meinen, diese Begriffe müßten immer Geltung haben.",
      "Aber da braucht man nicht zwanzig Jahre zu warten, braucht man nur von einem Arbeitgeber zum ändern zu gehen, aus einem Lande ins andere und entdeckt dann, daß der Begriff, den man sich an der einen Stelle gebildet hat, eben an der anderen Stelle gar nicht mehr gilt, wenn er sich nicht von selbst umgewandelt hat - wie der Ernst Müller. Man erkennt nicht, was da ist, wenn man nicht bewegliche Begriffe hat, die voll im Leben drinnen stehen.",
      "Das ist das, was möglich machte, daß gerade auf anthroposophischem Boden in unserer heutigen Zeit der Not auch wirtschaftliche Einrichtungen ihren Ausdruck 115 finden, weil Anthroposophie es ihrer Natur nach gegen- über dem beweglichen Geiste mit beweglichen Ideen zu tun haben muß, weil man an ihr lernen kann, wie man seine Ideen mit Wachstumskraft, mit innerer Beweg- lichkeit ausstatten muß und dann mit solchen Ideen - so wenig es die heutigen Praktiker glauben mögen - auch in die andersgeartete Wirklichkeit eintauchen kann, die sich abspielt als soziales Leben von Mensch zu Mensch, von Volk zu Volk durch die ganze, nunmehr notwendig gewordene und so künstlich beeinträchtigte Weltwirt- schaft hindurch. Und so darf wohl gesagt werden: Nicht eine Äußerlichkeit ist es, daß gerade auf anthroposophi- schem Boden auch der Versuch gemacht wurde, zu nicht sozialen Ideen, sondern zu sozialen Impulsen zu kommen.",
      "Ich erinnere mich noch an die Zeit, in der über diese Dinge viel diskutiert worden ist. Ich habe immer sagen müssen: Ich meine soziale Impulse! - Das hat die Leute furchtbar geärgert. Denn selbstverständlich hätte ich sagen sollen: soziale Ideen oder soziale Gedanken; denn die Leute hatten für solche Dinge nur Gedanken im Kopfe.",
      "Daß ich von Impulsen sprach, ärgerte sie furchtbar; denn sie merkten nicht, daß ich «Impulse» brauchte aus dem Grunde, weil ich Realitäten meinte und nicht ab- strakte Ideen. Ausdrücken muß man sich selbstverständ- lich in abstrakten Ideen.",
      "So muß heute wieder begriffen werden, daß ein neues Verständnis gesucht werden muß für das, was man das soziale Problem nennt. Wir leben heute unter anderen Verhältnissen als im Jahre 1919. Die Zeit ist insbesondere auf dem Wirtschaftsgebiete außerordentlich schnellebig.",
      "Notwendig ist es, daß selbst solche Ideen, die schon für die damalige Zeit beweglich gehalten worden sind, wei- ter in Fluß gehalten werden, und daß man bei seinen 116 Beobachtungen auf dem Standpunkte des Geistesgegen- wärtigen steht. Wer die Verhältnisse des Wirtschaftslebens real ins Auge zu fassen vermag, der weiß, daß sie sich seit der Abfassung der «Kernpunkte» wesentlich geändert haben, und daß man nicht wieder bloß so deduzieren kann wie damals.",
      "Aber man wird dort [in den «Kern- punkten»] wenigstens einen Versuch finden, diese Me- thode des sozialen Denkens in einer realistischen Weise zu suchen, gerade vielleicht deshalb, weil dieser Versuch entsprossen ist einem Boden, wo Realitäten immer ge- sucht wurden, wo man nicht in Schwärmerei oder in falsche Mystik hineinfallen will - weil dieser Versuch erwachsen ist auf dem nach Exaktheit ringenden Boden der anthroposophischen Weltanschauung. 117"
    ],
    "sentences": [
      [
        "Meine sehr verehrten Anwesenden!",
        "Noch mehr als bei den übrigen einleitenden Worten, die ich zu diesen Ta- gesunternehmungen vorauszusprechen habe, wird es heute der Fall sein, daß ich mich auf Andeutungen zu beschränken habe, da ja das Wesentliche, was zu sagen ist, in den folgenden Vorträgen über Einzelheiten des Wirtschaftslebens gerade für das heute in Betracht kommende Gebiet wird liegen müssen."
      ],
      [
        "Man kann heute wohl nicht über Sozialwissenschaft sprechen, wenn man nur von einem theoretischen Stand- punkte ausgeht.",
        "Man kann heute - und ich meine damit die unmittelbare Gegenwart, den gegenwärtigen Au- genblick - über solche Fragen nur sprechen, wenn man im Hintergrunde hat die trostlose Lage des Wirtschafts- lebens in der gegenwärtigen zivilisierten Welt."
      ],
      [
        "In diese trostlose Lage fiel in einer gewissen Weise auch noch dasjenige hinein, was ich nach der vorläufigen Beendigung der furchtbaren Weltkriegskatastrophe darzustellen ver- suchte in meinen «Kernpunkten der sozialen Frage».",
        "Ich ging dazumal aus von jener Beobachtung des sozialwirtschaftlichen Lebens, die sich eigentlich im ge- genwärtigen Zeitpunkt der Weltentwicklung jedem auf- drängen sollte."
      ],
      [
        "Es ist die, daß das Wirtschaftsleben der Gegenwart innig verquickt ist mit dem, was sich inner- 96 halb des ganzen Umfanges der sozialen Frage bewegt.",
        "Ja, die meisten Menschen in der Gegenwart werden wohl kaum empfinden, daß die soziale Frage getrennt werden könne von der wirtschaftlichen Frage."
      ],
      [
        "Und dennoch ging gerade mein Buch «Die Kernpunkte der sozialen Frage» darauf aus, dadurch Klarheit zu schaffen in bezug auf das hier in Betracht kommende Gebiet, daß dar- auf hingewiesen wurde, wie das Wirtschaftsleben inner- halb des sozialen Organismus seine eigene selbständige Stellung erhalten müsse, jene selbständige Stellung, durch welche innerhalb desselben die Tatsachen und Ein- richtungen lediglich nach wirtschaftlichen Grundsätzen, wirtschaftlichen Gesichtspunkten und Impulsen ihre Gestaltung bekommen.",
        "Insofern enthält eigentlich mein Buch - ich sage es hier m ganz unumwundener Weise, weil gerade darauf außerordentlich viel ankommt - einen inneren Widerspruch."
      ],
      [
        "Allein, dieses Buch wollte nicht ein theoretisches Buch der Sozialwissenschaft sein.",
        "Die- ses Buch wollte Anregungen geben vor allen Dingen den Lebenspraktikern; dieses Buch wollte aus dem heraus geschrieben sein, was man in jahrzehntelanger Beobach- tung des europäischen Wirtschaftslebens sich aneignen konnte."
      ],
      [
        "Und indem so dieses Buch anstrebte, durch und durch realistisch zu sein, unmittelbar eine Anregung für praktisches Handeln zu sein - und zwar für praktisches Handeln im Augenblick -, mußte es ja einen Wider- spruch enthalten.",
        "Dieser Widerspruch ist nämlich kein anderer als der, der unser ganzes soziales Leben durch- zieht, und der darin besteht, daß dieses soziale Leben im Laufe der neueren Zeit durcheinander, chaotisch das gebracht hat, was nur dann lebensfähig ist, wenn es sich aus seinen eigenen Bedingungen in jedem seiner einzel- nen Glieder entwickelt. 97 Ich mußte sprechen von einer Dreigliederung des sozialen Organismus, die dazu führen würde, daß das Wirtschaftsleben in völlig freier Weise, relativ abgeson- dert sich organisiert von dem Rechts- und Staatsleben und von dem geistigen Leben, daß also dieses Wirt- schaftsleben von denjenigen, die in ihm drinnen stehen, die aus seinen eigenen Impulsen heraus handeln können, gestaltet wird."
      ],
      [
        "Nun aber leben wir ja zunächst in einer Zeit, in welcher ein solcher Zustand nicht da ist, in welcher das Wirtschaftsleben absolut drinnen steht in der übrigen Struktur des sozialen Organismus.",
        "Wir leben in einer Zeit, in welcher der Widerspruch eine Realität ist."
      ],
      [
        "Daher konnte eine Schrift, die aus der Realität heraus geschrieben sein wollte und für die Realität Anregungen bieten wollte, nur etwas Widerspruchsvolles wiederum bringen; sie konnte nur darauf ausgehen, aus dem Wi- dersprechenden heraus zunächst zur Klarheit, zur Klä- rung der Verhältnisse aufzurufen.",
        "Ich bin deshalb heute in einer ganz besonderen Lage, indem ich diese Einleitung spreche, weil in bezug auf dasjenige, was auf anthroposophischem Boden, mit an- throposophischen Denkmethoden gefunden worden ist, aber gefunden worden ist aufgrund durchaus realisti- scher, jahrzehntelanger Beobachtung der europäischen Wirtschaftsverhältnisse - weil das doch in den weitesten Kreisen zunächst in der ärgsten Weise mißverstanden worden ist."
      ],
      [
        "Ich kann nur sagen: Ich begreife vollständig diese Mißverständnisse, die diesen zugrunde liegenden Absichten entgegengebracht worden sind; diese Mißver- ständnisse sind eben auch ein Zeitphänomen.",
        "Allein, ich muß auf der anderen Seite der Anschauung sein, daß in der Überwindung dieser Mißverständnisse dasjenige liegt, was wir zunächst auf soziologischem, auf sozialem Ge- 98 biete anzustreben haben, und gerade dazu möchte ich einiges Orientierende sagen."
      ],
      [
        "Als mein Buch «Die Kernpunkte der sozialen Frage» zuerst veröffentlicht wurde, fiel es in eine Zeit mittel- europäischer Entwicklung, die unmittelbar gefolgt war der furchtbaren Kriegskatastrophe.",
        "Es war eine Zeit, die dem Versailler Vertrag vorangegangen war; es war eine Zeit, in welcher die Valutaverhältnisse der mitteleuro- päischen und der osteuropäischen Staaten noch wesent- lich andere waren."
      ],
      [
        "Nicht aus irgendeinem Wolkenkuk- kucksheim heraus waren die Impulse gemeint, die damals in meinen «Kernpunkten» niedergeschrieben wurden, sondern sie waren aus der unmittelbaren Weltsituation der damaligen Zeit heraus so gedacht, daß ich glauben durfte, wenn eine größere Anzahl von Menschen sich fände, welche auf Grundlage dieser Anregungen Weite- res suchte, dann würde man - namentlich von Mitteleu- ropa aus - einen Impuls auch in die wirtschaftliche Entwicklung hineinwerfen können, der zu einer Art von Aufstieg führen könnte in dem ja damals deutlich ver- nehmbaren und bis heute andauernden Abfall des Wirt- schaftslebens und des sozialen Lebens überhaupt.",
        "Man konnte damals sich sagen, wenn man aus den sehr komplizierten Verhältnissen der Weltsituation heraus dachte: Vielleicht bleibt kein Stein stehen, so wie er hineingebaut ist in das Ideengebäude der «Kernpunkte der sozialen Frage» -; aber diese Ideen waren überall herausgedacht aus demjenigen, was war."
      ],
      [
        "Doch man könnte sie angreifen, und es wäre vielleicht etwas ganz anderes herausgekommen, als man zunächst schriftlich fixieren konnte.",
        "Denn nicht darauf kam es an, Ideen in utopistischer Weise hinzustellen, die ein Bild etwa eines sozialen Zukunftsorganismus entwerfen wollten; son- 99 dern darauf kam es an, Menschen zu finden, welche verstanden: Hier hegen reale, unmittelbar im Leben vorhandene Probleme vor; wir müssen uns aus unserer Sachkenntnis heraus mit diesen Problemen befassen und müssen sehen, ob wir, indem wir uns mit diesen Pro- blemen befassen, dann immer weiteres und weiteres Verständnis finden."
      ],
      [
        "Nun ist im Grunde genommen etwas ganz anderes eingetreten.",
        "Es haben sich auf der einen Seite wohl Theoretiker gefunden, welche über das, was in meinem Buche steht, allerlei Diskussionen gepflogen haben, welche an das dort Ausgesprochene allerlei Forderungen geknüpft haben."
      ],
      [
        "Es hat auch Theoretiker gegeben, die in vollständig mißverstehender Art das, was gesagt war, in utopistischem Sinne umdeuteten und immer wieder fragten: Wie wird sich dieses, wie wird sich jenes ge- stalten?, - was man ja eigentlich hätte abwarten müssen.",
        "Es hat sich sogar die merkwürdige Tatsache herausge- stellt, die für mich ganz überraschend war, daß gerade die wirtschaftlichen Praktiker, die in irgendeinem Ge- biete des Wirtschaftslebens mit ihrer Routine ganz gut drinnenstanden, die sich in diesem oder jenem Ge- schäftszweige auskannten und es abgelehnt hätten, sich in ihrem Geschäftszweige etwas hereinreden zu lassen von dem, der nicht gerade in diesem Geschäftszweig versiert war , daß diese Praktiker diskutierten über die Kernpunkte der sozialen Frage und sich durch das, was von ihnen als Folgerung gezogen wurde, gerade als die abstraktesten Theoretiker erwiesen."
      ],
      [
        "Es zeigte sich, daß man im Wirtschaftsleben ganz gut ein routinierter Prak- tiker sein konnte - im alten Sinne; unter den neuen Verhältnissen kannten sie sich nicht mehr aus -, daß aber diese Praktiker absolut nicht in der Lage waren, das, was 100 hier angeschlagen war in bezug auf die Probleme auch des Wirtschaftslebens, anders als gerade von dem Ge- sichtspunkte der abstraktesten Theorien aus zu diskutie- ren; so daß man da gerade in Verzweiflung kommen konnte, wenn man Praktikern gegenüberstand und sich mit ihnen eine Diskussion entwickelte, wo sie durchaus nicht auf etwas Konkretes eingingen, sondern nur das völlig triviale Allgemeine über die soziale Frage und namentlich über den wirtschaftlichen Teil der sozialen Frage wiederholten, wenn man sich mit ihnen irgendwie darüber aussprach.",
        "Das andere, was einem da entgegentreten konnte, war, daß zunächst ja diejenigen, die nun so die ganz handfesten Praktiker sind, es überhaupt ablehnten, sich in solcher Weise über die mögliche Gestaltung der wirtschaftlichen Probleme zu unterhalten."
      ],
      [
        "Das Weitere war, daß ja einiges Interesse zum Beispiel in sozialistischen Kreisen erweckt werden konnte, daß man aber gerade dort die Erfahrung machen konnte, daß das, was gewollt war, am allerwenigsten von dieser Seite verstanden wurde, und daß alles nur danach beurteilt wurde, ob es sich in die alten Parteischablonen einfüge oder nicht.",
        "Und so verging jene Zeit, aus der heraus diese Anregungen ge- dacht waren."
      ],
      [
        "Es kam das ganze furchtbare Valuta-Elend, das aber in einer ganz anderen Weise eigentlich zu be- urteilen ist, als man es heute gewöhnlich beurteilt.",
        "Als zuerst mein «Aufruf an das deutsche Volk und an die Kulturwelt» und dann die «Kernpunkte der so- zialen Frage» erschienen waren, da zeigte sich sogleich, wie einzelne Persönlichkeiten, die es ja in ihrer Art mit einer Gesundung des mitteleuropäischen Wirtschaftsle- bens ganz ehrlich meinten, sagten: Ja, solche Vorschläge - sie nannten das Vorschläge - sind ja ganz schön, aber 101 es sollte zunächst einmal gesagt werden, wie wir zu einer Aufbesserung der Valuta kommen."
      ],
      [
        "Das wurde in Zeiten gesagt, als das Valuta-Elend gegenüber den heu- tigen Verhältnissen noch das reine Paradies war.",
        "Nun zeigt sich in solchen Forderungen, wie man überall nur an den äußeren Symptomen herumpfuschen will."
      ],
      [
        "Es zeigt sich wenig Verständnis dafür, daß ja in den Valuta- verhältnissen nur die an die Oberfläche schlagenden ungesunden Wirtschaftsverhältnisse sich symptomatisch anzeigen, daß man mit einer solchen Symptomenkur überhaupt das Übel gar nicht anpackt, und daß es sich darum handelt, viel tiefer und tiefer in die sozialwirt- schaftlichen Zustände der Gegenwart hineinzugehen, wenn man in irgendeiner Weise dazu kommen will, die Probleme realistisch zu besprechen, für die die Andeu- tung gegeben werden sollte in den «Kernpunkten der sozialen Frage».",
        "Und so ist es denn gekommen, daß das, was ich wiederholt am Schlüsse von Vorträgen, die ich im Anschlüsse an die «Kernpunkte» hielt, damals gerufen habe: man solle sich besinnen, ehe es zu spät ist -, daß dieses «Zu spät!» in einem hohen Grade heute eingetreten ist, daß wir gar nicht mehr in der Lage sind, in dem ursprünglichen Sinne, der die «Kernpunkte» durchpulst, die Sache anzufassen; denn mittlerweile ist das Chaos des Wirtschaftslebens so hereingebrochen, daß wiederum ganz andere Ergänzungen notwendig wären zu dem, was dazumal nicht bloß ausgesprochen werden sollte, sondern ausgesprochen werden mußte, meiner Über- zeugung nach."
      ],
      [
        "Und man wird wohl doch kaum vor- übergehen können an einer Charakteristik unseres Zeit- alters im allgemeinen, wenn man das besprechen will, was heute auch dem Wirtschaftsleben am allerschäd- lichsten ist. 102 Als ich gestern ein Zeitungsblatt in die Hand nahm, da trat mir - und es können einem heute ja die wichtig- sten Symptome gewissermaßen aus einzelnen Sätzen, die heute unsere Zeitgenossen aussprechen, überall entge- gentreten -, es trat mir ein Artikel entgegen: «Verschie- bung der Demission des Lloyd George bis nach der Konferenz von Genua».",
        "Damit war wieder einmal die heutige Tagessituation ausgesprochen, indem alles, was heute den Tag charakterisiert, «wartet»."
      ],
      [
        "«Wir wollen warten» - das ist eigentlich heute überall das Prinzip; warten, bis irgend etwas geschieht, von dem man nicht sagen kann, was es eigentlich sein wird.",
        "Was da gesche- hen soll, weiß man nicht, aber man wartet, bis es ge- schehen ist!"
      ],
      [
        "Das ist das, was heute den Leuten tief in den Seelen sitzt, auf allen Gebieten.",
        "Und nun möchte ich etwas scheinbar aber nur scheinbar - recht Abstraktes vorbringen; aber auch das ist durchaus in realistischem Sinne gemeint, denn es weist hin auf die unter uns wirksamen Kräfte, durch die wir eigentlich im Laufe der Menschheitsentwicklung allmählich dazu gekommen sind, dieses so aussichtsvolle Prinzip «wir wollen war- ten» überall geltend zu machen."
      ],
      [
        "Wenn wir in ältere Kulturentwicklungen zurückblik- ken, so finden wir gerade bei diesen älteren Kulturen, daß ein eigentliches wissenschaftliches Denken, auch in dem Sinne, wie es in den alten Zeiten vorhanden war - Sie wissen das ja aus dem Vortrage, den ich hier zuletzt in der Philharmonie gehalten habe -, nicht rein «wissen- schaftlich» zu nennen ist.",
        "Sieht man aber auf das, was an Stelle des heutigen wissenschaftlichen Denkens stand, so kann man wissen, daß aus jenem Denken zunächst nicht unmittelbar das wirtschaftliche Leben hervorgegangen ist."
      ],
      [
        "Das wirtschaftliche Leben hat sich zunächst mehr 103 oder weniger unabhängig von dem menschlichen Ge- danken, wie instinktiv - um nicht zu sagen automatisch - im Wechselverkehr der Menschheit entwickelt.",
        "Was man im wirtschaftlichen Leben hat tun wollen, hat sich einfach aus der Lebenspraxis heraus entwickelt."
      ],
      [
        "Man hat instinktiv gehandelt, hat ja wohl auch den Bereich des Handels erweitert über dieses oder jenes Gebiet, aber alles ist eben mehr oder weniger instinktiv geschehen.",
        "Man mag nun das eine oder andere einwenden vom Gesichtspunkte der heutigen Auffassungen von Men- schenfreiheit, Menschenwürde und so weiter gegen die wirtschaftlichen Zustände älterer Zeiten; allem, man wird gut tun, auch auf der anderen Seite zu sehen, wie ganz merkwürdige Symptome in der Menschheitsentwicklung, die auch heute noch lehrreich sein können, sich zum Beispiel zeigen in der Art und Weise, wie Arbeitnehmer und Arbeitgeber - wenn wir diese modernen Ausdrücke auf alte Zeiten anwenden wollten - im Verhältnis zuein- ander lebten im alten Griechentum, im alten Ägypter- tum, bis nach Asien hinüber."
      ],
      [
        "Diese Dinge nehmen sich gegenüber den heutigen Empfindungen so aus, daß sie eben die schärfste Kritik selbstverständlich herausfor- dern; allein, jede solche Kritik ist eben unhistorisch, und man muß sagen: Es waren eben diejenigen Verhältnisse in den entsprechenden Zeitepochen da, die sich aus dem damaligen Empfinden jener Menschheit ergaben.",
        "Das ist das eine, was man ins Auge fassen muß."
      ],
      [
        "Das andere ist die Tatsache, die zusammenhängt mit jenem Umschwung in der Menschheitsentwicklung, auf den ich schon öfters hindeuten mußte, der etwa im 15.",
        "Jahrhundert liegt, und durch den die Seelenverfassung der zivilisierten Menschheit eine ganz andere geworden ist."
      ],
      [
        "Ich sagte schon: Die äußere Geschichte weist wenig 104 darauf hin, wie damals die Gesamtlebensauffassung der menschlichen Seele eine andere geworden ist.",
        "Und wenn wir uns dann fragen: Wie steht diese menschliche Ent- wicklung zum Wirtschaftsleben? - dann bekommen wir die Antwort: Die Zeit der instinktiven Führung des Wirtschaftslebens, die so war, wie ich sie eben charakte- risiert habe, diese Zeit reichte noch herein bis in die Epoche dieses Umschwunges."
      ],
      [
        "Mit diesem Umschwünge kam dann herauf in die Seelenverfassung der Menschheit der Intellektualismus, der Drang, mit reiner Verstan- deslogik die Welt zu begreifen.",
        "Dieser Drang, der einfach ein tiefes Bedürfnis der menschlichen Seelenverfassung wurde, er bewährte sich ja in so glänzender Art gerade auf naturwissenschaftlichem Gebiete und auf jenem Gebiete, das aus der Naturwissenschaft in so glänzender Weise sich herausgebildet hat: auf dem Gebiete der Technik, wo er die außerordentlichsten, nicht genug anzuerkennenden Triumphe gefeiert hat."
      ],
      [
        "Aber dieser Intellektualismus - und das werden doch verschiedene Auseinandersetzungen gezeigt haben, die hier auch wäh- rend dieses Kursus schon gepflogen worden sind - hat sich völlig unfähig gezeigt, die Erscheinungen des Menschenlebens und Menschenwesens selbst, auch in sozialer Beziehung, zu ergreifen.",
        "Man kann mit diesem Intellektualismus, mit dieser intellektualistischen Orien- tierung der Seele in grandioser Weise die äußere sinnli- che Natur auf ihre Gesetzmäßigkeiten zurückführen."
      ],
      [
        "Man kann aber nicht mit diesem Intellektualismus diese sich ineinander verschlingenden und während des Ver- schlingens sich organisierenden und während des Orga- nisierens sich seelisch auslebenden und geistig sich durchdringenden Verhältnisse des sozialen Lebens er- greifen.",
        "Ich möchte sagen: Das Netzwerk intellektuali- 105 stischer Ideen ist einfach zu weitmaschig für das, was im sozialen Leben vorliegt."
      ],
      [
        "Aber wissenschaftlich zu denken - das hat die Menschheit gelernt an diesem Intellektua- lismus.",
        "In ihn ist ja zuletzt alles einbezogen worden, bis in die Theologie hinein.",
        "Der Intellektualismus beherrscht, wenn wir auch beobachten und experimentieren, doch unsere ganze wissenschaftliche Denkweise, und wir haben es zuletzt dahin gebracht, das, was nicht in die Bahnen des Intellektualismus hineingebracht wird, ein- fach als nicht wissenschaftlich anzusehen."
      ],
      [
        "In diese Zeit des Intellektualismus fiel nun hinein der Übergang von dem rein instinktiven zu demjenigen Wirtschaftsleben, das angefacht werden soll mit mensch- lichen Gedanken.",
        "Wir dürfen sagen: In der Zeit, wo man noch nicht intellektualistisch über die Welt gedacht hat, wurde das Wirtschaftsleben instinktiv geführt."
      ],
      [
        "Als aber die Zeit heraufkam, die immer mehr und mehr nach Weltwirtschaft und Weltverkehr hintendierte, wurde der Mensch aus dieser Tendenz nach Weltverkehr und Weltwirtschaft dazu angehalten, auch das Wirtschaftsle- ben nun mit Gedanken zu durchdringen.",
        "Diese Gedan- ken aber wurden allein aus dem Intellektualismus heraus genommen."
      ],
      [
        "Dadurch zeigte sich in allem, was als wirt- schaftswissenschaftliche Gedanken heraufgezogen ist - im Merkantilismus, im Physiokratismus, in den natio- nalökonomischen Ideen eines Adam Smith, wie in allem, was dann später hervorgetreten ist bis zu Karl Marx -, daß auf der einen Seite das Wirtschaftsleben forderte, daß nicht mehr bloß instinktiv gewirtschaftet würde, sondern daß es mit Gedanken erfaßt werde, daß aber auf der anderen Seite, da die Gedanken nur hergenommen werden konnten aus dem Intellektualismus, damit alle wirtschaftlichen Anschauungen durch und durch einseitig 106 wurden, so daß aus diesen wirtschaftlichen Anschauun- gen niemals eigentlich etwas hervorging, was man fort- wirken gesehen hätte in der wirtschaftlichen Praxis.",
        "Auf der einen Seite waren die Wirtschaftstheoretiker, die aus intellektualistischen Sätzen Axiome bildeten - wie zum Beispiel Ricardo, Adam Smith oder John Stuart Mill -, und die auf solchen Axiomen Systeme aufbauten, womit sie eine ganz in sich verlaufende Geistesart bildeten; auf der anderen Seite war die wirtschaftliche Praxis, die eigentlich einer Durchdringung mit dem Geist bedurft hätte, die diese Durchdringung geradezu forderte, aber keinen Anschluß fand, die im alten Instinktleben fort- wirkte und daher in das vollständige Chaos verfiel."
      ],
      [
        "So waren diese zwei Strömungen in der neueren Zeit immer mehr gang und gäbe geworden: auf der einen Seite die Wirtschaftstheoretiker - ohne Einfluß auf die wirtschaftliche Praxis; auf der anderen Seite die Prakti- ker, welche die alte, zur Routine gewordene Praxis fort- setzten, und damit das Wirtschaftsleben der zivilisierten Welt in das Chaos hineinwarfen. - Man muß selbstver- ständlich solche Dinge in einer etwas radikalen Weise aussprechen, denn nur dadurch wird wirklich auf das hingedeutet, was ist, was wirksam ist und was als Problem aufgefaßt werden muß.",
        "Wenn man nun, ich möchte sagen, eine Art Ver- bindung, eine Art Synthese zwischen wirtschaftlichem Denken - das aber von der Praxis allmählich ganz ausge- rottet worden ist - und dieser wirtschaftlichen Praxis sucht, so findet man diese Verbindung höchstens in einem."
      ],
      [
        "In der neuesten Zeit bildete sich nämlich heraus eine Art von wirtschaftlichem Realismus, eine Art wirt- schaftlich-wissenschaftlicher Realismus, der da sagt, man könne überhaupt nicht so allgemein zu Gesetzen des 107 Wirtschaftslebens kommen, sondern man müsse die Tat- sachen der Wirtschaft betrachten, wie sie sich bei ein- zelnen Nationen oder Menschengruppen abspielen, und nur wenn man in dieser Weise rein äußerlich betrachtet, was geschehen ist, könne man einige Richtlinien für das wirtschaftliche Handeln finden.",
        "Was aus diesen Unter- gründen heraus entstanden ist, das ist das, was dann als die sogenannte sozialpolitische, als die wirtschaftli- che Gesetzgebung aufgetreten ist."
      ],
      [
        "Das heißt, man hat allmählich geglaubt, herausgefunden zu haben, daß man zwar durch die Betrachtung der tatsächlichen wirt- schaftlichen Verhältnisse im Zusammenhange mit den sie durchsetzenden sozialen Verhältnissen gewisse Richt- linien bekommen könne, die man dann in der wirtschaft- lichen Gesetzgebung zum Ausdruck brachte; man hat also auf dem Umwege durch den Staat versucht, einiges von dem zu verwirklichen, was aus den Beobachtungen hervorgegangen ist, aber dadurch hat man in Wirklichkeit selbst zugegeben, daß aus diesen Beobachtungen wirk- liche wissenschaftliche Wirtschaftsgesetze gar nicht hervorgehen können.",
        "Ja, in dieser Situation steht man eigentlich im Grunde genommen heute noch drinnen."
      ],
      [
        "Und gerade, wenn man in der Lage ist, einschneiden- de Erfahrungen zu machen und, ich möchte sagen, so- ziale Urphänomene in der richtigen Weise zu werten, dann sieht man, wie man in dieser Situation drinnen steht.",
        "Sie wissen ja alle, daß in das in ein so furchtbares Chaos hineingehende Zivilisationsleben in einem gewis- sen Zeitpunkte die sogenannten «Vierzehn Punkte» Woodrow Wilsons fielen."
      ],
      [
        "Was waren diese Vierzehn Punkte denn eigentlich?",
        "Sie waren im Grunde genommen nichts anderes als die abstrakten Prinzipien eines welt- 108 fremden Mannes, die abstrakten Prinzipien eines Men- schen, der von der Wirklichkeit wenig wußte, wie sich dann in Versailles, wo er in der Wirklichkeit eine her- vorragende Rolle hätte spielen können, gezeigt hat."
      ],
      [
        "Ein wirklichkeitsfremder Mann wollte aus dem Intellektua- lismus heraus der Welt zeigen, wie sie sich organisieren sollte.",
        "Man muß nur erlebt haben, mit welcher Begei- sterung die zivilisierte Menschheit an diesen Vierzehn Punkten hing, allerdings mit Ausnahme eines großen Teiles der mitteleuropäischen Bevölkerung, für die es aber leider auch einen, wenn auch kurzen Zeitraum gab, in dem sie auf diese Vierzehn Punkte hereinfiel."
      ],
      [
        "Im Jahre 1917 versuchte ich demgegenüber, einzelnen Persönlichkeiten Mitteleuropas, die sich dafür interes- sierten, denen aber nicht nachgelaufen wurde, sondern die entweder herankamen oder herangebracht wurden, zu zeigen, wie abstrakt, wie wirklichkeitsfremd dasjeni- ge ist, was da in die soziale Gestaltung der Welt herein will, wie sozusagen alles das, was an schlechten Erzie- hungsgrundsätzen m der modernen Zivilisation waltet, kondensiert in diesem Weltschulmeister Woodrow Wil- son sich darstellte, und wie die abstrakten Grundsätze dieser - im schlechten Sinne - Weltschulmeisterei von den Leuten mit Begeisterung aufgenommen wurden.",
        "Dazumal versuchte ich zu zeigen, daß eine Gesundung dieser Verhältnisse nur eintreten könne, wenn man ge- genüber allen solchen abstrakten Einstellungen sich auf den Boden stellt, der die Gedanken nicht ausschließt, der aber gerade die Gedanken so hervorbringt, daß sie aus der Wirklichkeit, aus der Realität herauswachsen."
      ],
      [
        "Dann darf man sich aber nicht irgend etwas Utopistisches ausdenken - ich möchte sagen, die Woodrow Wilson- schen Grundsätze waren der verdichtetste Utopismus, 109 waren der Utopismus in der dritten Potenz schon -, sondern dann muß man sich klar sein, daß man aus den realen Bedingungen der gegenwärtigen Menschheit selbst suchen muß, wie Impulse zu finden sind.",
        "Daher verzich- tete ich bei dem, was ich auseinanderzusetzen hatte, auf jede utopistische Theorie, verzichtete darauf, überhaupt zu sagen, wie sich etwa Kapital, wie sich Arbeit und dergleichen gestalten sollten; ich gab höchstens einige Beispiele dafür, wie man sich denken könne, daß sie sich aus den gegenwärtigen Verhältnissen heraus in eine nächste Zukunft hinein gestalten könnten."
      ],
      [
        "Das aber war alles nur zur Illustration dessen gesagt, was sie werden sollten; denn ebenso gut wie ich da über die Wandlung der Kapitalkräfte in meinen «Kernpunkten» gesprochen habe, ebenso gut könnte diese Wandlung auch in einer modifizierten Weise sich vollziehen.",
        "Nicht darauf kam es mir an, ein abstraktes Zukunftsbild hinzustellen, sondern zu sagen, aus welchen Untergründen heraus, auf reale Art, man nun - nicht zu einer theoretisch ausge- dachten, sondern zu einer wirklichen Lösung der soge- nannten sozialen Frage kommen könnte."
      ],
      [
        "Es handelte sich nicht darum, zu sagen: Dies oder jenes ist die Lösung der sozialen Frage.",
        "Um eine solche Lösung zu versu- chen, dazu habe ich nun wirklich zu viele Erfahrungen gemacht.",
        "Ich war schon in den 80er Jahren des vori- gen Jahrhunderts in dem gemütlichen Wien fast jeden Nachmittag nach zwei Uhr eine Stunde zusammen mit allen möglichen gescheiten Leuten."
      ],
      [
        "Da ist im Verlaufe einer Stunde die soziale Frage jeden Nachmittag mehr- mals gelöst worden!",
        "Und derjenige, der unbefangen ge- nug in die Verhältnisse der Gegenwart hineinsieht, weiß schon ganz gut, daß Lösungen, die heute oftmals in dicken Büchern auftreten, auch nicht viel mehr wert 110 sind, als die, welche damals in Wien mit einigen Bleistift- strichen und vielen fanatischen Worten über einer wei- ßen Tischplatte verhandelt worden sind."
      ],
      [
        "Darum konnte es sich also nicht handeln, und das war das ärgste Miß- verständnis, das mir entgegengebracht wurde, daß es sich um so etwas handeln sollte.",
        "Was ich zeigen wollte, war: Die Lösung des sozialen Problems kann nur auf reale Weise selbst erfolgen; diese Lösung kann überhaupt nicht durch Diskussionen, son- dern nur durch Geschehen, durch Tätigkeit erfolgen."
      ],
      [
        "Zu dieser Tätigkeit müssen aber erst die Bedingungen hin- gestellt werden, und auf diese Bedingungen versuchte ich in meinen «Kernpunkten» und in anderen Auseinan- dersetzungen zu verweisen.",
        "Ich versuchte zu zeigen, daß wir in unserem sozialen Organismus einmal solche Ein- richtungen brauchen, die es ermöglichen, daß ein Gei- stesleben aus seinen eigenen Bedingungen heraus sich entwickeln kann, wo also nur die Bedingungen des Geisteslebens selbst wirken; daß wir sodann ein zweites Glied brauchen, wo nur die rechtlich-staatlichen Impul- se wirken, und außerdem ein drittes Glied, wo nur dieje- nigen Impulse wirken, die aus der Warenproduktion und der Warenkonsumtion hervorgehen, und die zu- letzt, wenn sie sich aus einem assoziativen Wirtschafts- system entwickeln, gipfeln müssen in einer gesunden Preisbildung."
      ],
      [
        "Damit sollten nicht etwa die alten Stände wieder ins Dasein zurückgerufen werden.",
        "Nicht die Menschen sollten sich gliedern in einen Lehrstand, einen Wehrstand und einen Nährstand; sondern der Mensch der neueren Zeit ist bis zur Individualität vorgeschritten, und er wird nicht in abstrakter Weise eingegliedert sein in einen bestimmten Stand."
      ],
      [
        "Aber was draußen als Ein- richtungen vorhanden ist, das tendiert einfach aus den 111 Kräften, die im geschichtlichen Werden vorhanden sind, dazu, daß abgesondert aus den eigenen Bedingungen heraus verhandelt wird, etwas getan wird für das Gei- stesleben, für das Rechts- oder Staatsleben und für das Wirtschaftsleben.",
        "Dann erst, wenn die Bedingungen dazu geschaffen sind, daß zum Beispiel der Wirtschafter rein aus wirtschaftlichen Impulsen heraus das gestalten kann, was etwa die gegenwärtigen Marktverhältnisse modifi- zieren soll, oder was die gegenwärtigen Kapitalverhält- nisse modifizieren soll, erst wenn solche Möglichkeiten geschaffen sind, entwickelt sich unter den Menschen dasjenige, was eine reale Lösung - die aber in fortwäh- rendem Werden ist - der sozialen Frage genannt werden kann."
      ],
      [
        "Also es geht mir nicht darum, die soziale Frage zu lösen, weil ich der Meinung sein mußte, daß überhaupt diese Lösung nie in einem einzelnen Moment als etwas Abgeschlossenes gegeben werden kann, weil das soziale Problem, nachdem es einmal heraufgekommen ist, in fortwährendem Fluß ist.",
        "Der soziale Organismus ist etwas, was jung wird, altert, und dem immer neue Impulse eingeflößt werden müssen, von dem aber nie gesagt werden kann: so und so ist seine Gestalt."
      ],
      [
        "Wenn der soziale Organismus nicht so ist, daß die Menschen in einem, alle Interessen zusammenmischenden Parlament zusammensitzen, wo dann wirtschaftlich Interessierte über Fragen des Geisteslebens, staatliche Interessen über wirtschaftliche Fragen und so weiter entscheiden, sondern wenn in einem gesunden sozialen Organismus die ein- zelnen Gebiete aus ihren eigenen Bedingungen heraus betrachtet werden, dann wird einmal das Staatsleben auf eine reale demokratische Grundlage gestellt werden können; dann wird das, was zu sagen ist, nicht von einem 112 Menschen in einem solchen einzigen Parlament gesagt werden, sondern es wird hervorgehen aus den fortdau- ernden kontinuierlichen Verhandlungen unter den ein- zelnen Gliedern des sozialen Organismus.",
        "In diesem Sinne war also mein Buch eine Mahnung dazu, endlich aufzuhören mit dem unfruchtbaren Reden über die soziale Frage und sich auf einen Boden zu stellen, von dem aus man jeden Tag die Lösung der sozialen Probleme in die Hand nehmen kann."
      ],
      [
        "Es war ein Ruf, der an die Verstehenden ging, um wirklich das, was immer nur im Abstrakten gedacht war, überzuführen in das durchdachte Handeln.",
        "Dazu sollten zum Beispiel im wirtschaftlichen Leben die Assoziationen dienen."
      ],
      [
        "Solche Assoziationen sind grundverschieden von dem, was in der neueren Zeit an Vergesellschaftungen zustande ge- kommen ist, und können jeden Tag aus den wirtschaft- lichen Untergründen gebildet werden.",
        "Bei ihnen handelt es sich darum, daß nun wirklich diejenigen Menschen, die im Behandeln von Warenproduktion, von Waren- zirkulation und im Konsumieren von Waren verbunden sind - was jeder Mensch ist -, sich zu Assoziationen zusammenschließen, so daß daraus vor allem die gesun- de Preisbildung hervorgeht."
      ],
      [
        "Es ist ein langer Weg von dem, was aus Sach- und Fachkenntnis heraus die in den Assoziationen verbundenen Menschen werden zu leisten haben, bis zu dem, was nicht durch eine Gesetzgebung, auch nicht als Resultat von Diskussionen, sondern als Resultat der Erfahrung sich ergibt als die gesunde Preis- bildung.",
        "Doch vor allem hatten Menschen das Bedürf- nis, die Grundzüge dessen, was damals gewollt wurde und was ich jetzt m diesen einleitenden Worten vor Sie hinzustellen versuchte, zu diskutieren; denn die Welt war so eingeschult in abstraktes Denken, daß man auch 113 diese Anregung nur vom Gesichtspunkte des abstrakten Denkens nahm, und daß man sich mit dem, was ich nur als Illustration gegeben habe, vor allem so hilft, daß man stundenlang diskutiert, während es sich darum handeln sollte, wirklich einzusehen, wie jeden Tag die Gliederung des sozialen Organismus in Angriff genommen werden kann in der Weise, wie es in den «Kernpunkten» ange- deutet ist."
      ],
      [
        "So handelt es sich heute nicht darum, theoretische Lösungen der sozialen Frage zu suchen, sondern die Bedingungen aufzusuchen, unter denen die Menschen sozial leben werden.",
        "Und sie werden sozial leben, wenn der soziale Organismus nach seinen drei Gliedern hin arbeitet, wie ja der natürliche Organismus auch unter dem Einfluß seiner relativen Dreigliederung gerade zur Einheit hin arbeitet."
      ],
      [
        "Sehen Sie, man muß heute erst einmal sagen, wie solche Dinge gemeint sind.",
        "Und wenn man sie aus- spricht, wird immer noch gefordert, daß nun die Worte, deren man sich schon einmal bedienen muß, so genom- men werden sollen, wie man sie nimmt nach der intellek- tualistischen Bedeutung, die man ihnen heute beilegt."
      ],
      [
        "Man übersetzt sofort in seinen Intellektualismus das, was ganz ausdrücklich nicht in Intellektualismus einge- taucht ist.",
        "Daher ist über Kapital, über die Naturgrund- lagen der Produktion, über die Arbeit in meinem Buche so gesprochen, daß die Ideen einfach für das Leben gedacht sind."
      ],
      [
        "Wenn wir abstrakt verhandeln, können wir lange definieren, und das ist ja auch geschehen.",
        "Der eine sagt mit demselben Recht: Kapital ist kristallisierte Ar- beit, ist Arbeit, die aufgespeichert ist -, wie der andere mit demselben Recht sagt: Kapital ist ersparte Arbeit."
      ],
      [
        "Und so kann man es mit allen volkswirtschaftlichen 114 Begriffen machen, wenn man innerhalb des Intellektua- lismus stehen bleibt.",
        "Aber das alles sind nicht Dinge, mit denen man es nur theoretisch zu tun haben kann, sondern die man lebendig in ihrer Gestaltung erfassen muß."
      ],
      [
        "Und wer sich wie die Praktiker, die viel auf ihre Praxis und Routine sich zugute tun, der Abstraktheit in diesen Dingen befleißigt, der kann folgendes machen, was ich durch einen Vergleich verdeutlichen will.",
        "Ich sehe den Ernst Müller."
      ],
      [
        "Er ist klein, hat durchaus kindliche Züge und kindliche Eigenschaften.",
        "Ich sehe diesen Ernst Müller nach zwanzig Jahren wieder und sage: Das ist nicht der Ernst Müller, denn der ist klein, hat kindliche Eigenschaften und eine ganz andere Phy- siognomie. -Ja, wenn ich mir damals meinen Begriff von dem Ernst Müller gebildet habe und ihn nun nach zwanzig Jahren zur Deckung bringen will mit dem, was mir jetzt als reale Wesenheit entgegentritt, so mache ich einen furchtbaren Fehler."
      ],
      [
        "Doch so wenig es die Menschen glauben mögen: es ist so, wenn sie heute wirtschaftlich denken.",
        "Sie machen sich Gedanken und Begriffe über Kapital und Arbeit und so weiter, und sie meinen, diese Begriffe müßten immer Geltung haben."
      ],
      [
        "Aber da braucht man nicht zwanzig Jahre zu warten, braucht man nur von einem Arbeitgeber zum ändern zu gehen, aus einem Lande ins andere und entdeckt dann, daß der Begriff, den man sich an der einen Stelle gebildet hat, eben an der anderen Stelle gar nicht mehr gilt, wenn er sich nicht von selbst umgewandelt hat - wie der Ernst Müller.",
        "Man erkennt nicht, was da ist, wenn man nicht bewegliche Begriffe hat, die voll im Leben drinnen stehen."
      ],
      [
        "Das ist das, was möglich machte, daß gerade auf anthroposophischem Boden in unserer heutigen Zeit der Not auch wirtschaftliche Einrichtungen ihren Ausdruck 115 finden, weil Anthroposophie es ihrer Natur nach gegen- über dem beweglichen Geiste mit beweglichen Ideen zu tun haben muß, weil man an ihr lernen kann, wie man seine Ideen mit Wachstumskraft, mit innerer Beweg- lichkeit ausstatten muß und dann mit solchen Ideen - so wenig es die heutigen Praktiker glauben mögen - auch in die andersgeartete Wirklichkeit eintauchen kann, die sich abspielt als soziales Leben von Mensch zu Mensch, von Volk zu Volk durch die ganze, nunmehr notwendig gewordene und so künstlich beeinträchtigte Weltwirt- schaft hindurch.",
        "Und so darf wohl gesagt werden: Nicht eine Äußerlichkeit ist es, daß gerade auf anthroposophi- schem Boden auch der Versuch gemacht wurde, zu nicht sozialen Ideen, sondern zu sozialen Impulsen zu kommen."
      ],
      [
        "Ich erinnere mich noch an die Zeit, in der über diese Dinge viel diskutiert worden ist.",
        "Ich habe immer sagen müssen: Ich meine soziale Impulse! - Das hat die Leute furchtbar geärgert.",
        "Denn selbstverständlich hätte ich sagen sollen: soziale Ideen oder soziale Gedanken; denn die Leute hatten für solche Dinge nur Gedanken im Kopfe."
      ],
      [
        "Daß ich von Impulsen sprach, ärgerte sie furchtbar; denn sie merkten nicht, daß ich «Impulse» brauchte aus dem Grunde, weil ich Realitäten meinte und nicht ab- strakte Ideen.",
        "Ausdrücken muß man sich selbstverständ- lich in abstrakten Ideen."
      ],
      [
        "So muß heute wieder begriffen werden, daß ein neues Verständnis gesucht werden muß für das, was man das soziale Problem nennt.",
        "Wir leben heute unter anderen Verhältnissen als im Jahre 1919.",
        "Die Zeit ist insbesondere auf dem Wirtschaftsgebiete außerordentlich schnellebig."
      ],
      [
        "Notwendig ist es, daß selbst solche Ideen, die schon für die damalige Zeit beweglich gehalten worden sind, wei- ter in Fluß gehalten werden, und daß man bei seinen 116 Beobachtungen auf dem Standpunkte des Geistesgegen- wärtigen steht.",
        "Wer die Verhältnisse des Wirtschaftslebens real ins Auge zu fassen vermag, der weiß, daß sie sich seit der Abfassung der «Kernpunkte» wesentlich geändert haben, und daß man nicht wieder bloß so deduzieren kann wie damals."
      ],
      [
        "Aber man wird dort [in den «Kern- punkten»] wenigstens einen Versuch finden, diese Me- thode des sozialen Denkens in einer realistischen Weise zu suchen, gerade vielleicht deshalb, weil dieser Versuch entsprossen ist einem Boden, wo Realitäten immer ge- sucht wurden, wo man nicht in Schwärmerei oder in falsche Mystik hineinfallen will - weil dieser Versuch erwachsen ist auf dem nach Exaktheit ringenden Boden der anthroposophischen Weltanschauung. 117"
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SECHSTER VORTRAG ANTHROPOSOPHIE UND THEOLOGIE Berlin, 10. März 1922",
    "paragraphs": [
      "Meine sehr verehrten Anwesenden! Ich bin genötigt, auszugehen von einer Zeitschriftennotiz, die mir eben überreicht worden ist, einer Notiz m der «Christlichen Welt», von der ich - weil ich sie vorher nicht kannte - selbstverständlich nicht dachte, bei meinen heutigen ein- leitenden Worten auszugehen.",
      "In dieser Zeitungsnotiz steht: «Vom 5. bis 12. März findet in Berlin ein anthro- posophischer Hochschulkurs statt. ... Der Tag der Theologen ist Freitag, der 10. - Diese Veranstaltung am Freitag ist nun eine unzweideutige Herausforderung Steiners und seiner Anhänger an die Theologen» und so weiter.",
      "Nun, meine sehr verehrten Anwesenden, diese heuti- ge Veranstaltung mag alles andere sein; das, was sie jedenfalls nicht ist und wodurch sie, wenn es der Glaube wäre, im allertiefsten Sinne mißverstanden würde, das ist eine Herausforderung an die Theologen. Ich selber bin an dieser Veranstaltung niemals in irgendeiner anderen Weise beteiligt gewesen, als daß ich gefragt worden bin, ob ich durch Vorträge und einleitende Betrachtungen mitwirken wolle an diesem Hochschulkurse, dessen Initiative nicht von mir ausgegangen ist.",
      "Ich bin am wenigsten beteiligt an der heutigen Veranstaltung, das heißt, an der Einfügung dieses Programmpunktes in den Hochschulkurs, und ich würde niemals daran gedacht 118 haben, daß dasjenige, was heute hier verhandelt werden soll, aufgefaßt werden könnte als eine «unzweideutige Herausforderung an die heutigen Theologen». Daher gestatten Sie auch, meine sehr verehrten An- wesenden, damit nicht wieder oder neuerdings alle mög- lichen Mißverständnisse sich an das knüpfen, was ich hier als ganz wenige einleitende Worte zu sagen haben werde, daß ich mich heute wirklich beschränke auf das Thema: Das Verhältnis der Anthroposophie zur Theo- logie, und daß ich mit Rücksicht darauf, daß nicht neue Mißverständnisse entstehen, auf einiges verzichte von dem, was von mir hier vorgebracht würde, weil ich sonst neuerdings sehen müßte, wie das verkannt wird, was von mir gewollt wird.",
      "Sehr verehrte Anwesende, es war niemals mein Be- streben - verzeihen Sie, wenn ich durch diese an mich ergangene Herausforderung gezwungen bin, heute ganz kurz in der Einleitung einzelne persönliche Bemerkun- gen zu machen -, es war eigentlich niemals meine Ab- sicht, irgendwie die Theologie herauszufordern, und von ihrem Ausgangspunkt an hat Anthroposophie, insofern sie ein Arbeitsgebiet darstellt, an dem ich selbst beteiligt bin, niemals irgendwie gesucht, sich innerhalb ihrer Arbeit mit der heutigen Theologie als solcher auseinanderzu- setzen. Das ist, insofern es geschehen ist, und es ist ja wirklich von mir so wenig wie möglich geschehen, le- diglich dadurch geschehen, daß Angriffe gegen die An- throposophie von theologischer Seite her allerdings sehr viele erfolgt sind, und daß man sich - nicht so sehr ich als andere - manchmal zur Wehr setzt.",
      "Denn Anthroposo- phie wollte als Arbeitsgebiet durchaus, ich möchte sagen, der Theologie gegenüber neutral bleiben, sie will arbei- ten aus dem gegenwärtigen Wissenschaftsgeist heraus. 119 Man hatte am Ende des vorigen Jahrhunderts eine gewisse wissenschaftliche Richtung, gewisse wissen- schaftliche Methoden, eine gewisse wissenschaftliche Gesinnung vor sich, eine Gesinnung und Methode, welche aus Gründen, über die ich schon gesprochen habe, und über die wegen der Kürze der Zeit nicht ausführlich gesprochen werden kann, eine Methode und Gesinnung, die man aus der ganzen geschichtlichen Entwicklung der neueren Zeit insbesondere anwendete auf die naturwis- senschaftliche Forschung, und durch die man innerhalb der naturwissenschaftlichen Forschung die größtmög- lichsten Triumphe - ich meine das nicht in einem trivialen, sondern in einem tieferen Sinne - für Menschenfortschritt und Menschenwohl errungen hat. Der naturwissen- schaftlichen Forschung stand in dieser Zeit die Philoso- phie, ich möchte sagen etwas ratlos gegenüber.",
      "Die Philosophie mußte sich auseinandersetzen mit denjenigen Methoden, welche vor allen Dingen auf die Naturwis- senschaft angewendet worden sind, und welche in der Philosophie, in der man es doch mit einem ganz anderen Tatsachengebiet zu tun hat, nicht anwendbar waren. Man war sich, ich möchte sagen theoretisch und er- kenntnistheoretisch nicht immer darüber klar, in wel- chem Sinne man mit den naturwissenschaftlichen Me- thoden in der Philosophie arbeiten sollte.",
      "Man ist dann in der experimentellen Psychologie auf ein gewisses Gebiet verfallen, wo es mehr oder weniger scheinbar oder auch mehr oder weniger richtig geht, aber die Un- sicherheit ist im Grunde genommen doch auch da vor- handen. Demgegenüber erarbeitete sich Anthroposophie aus den verschiedensten Untergründen heraus ihre eigene Arbeitsmethode.",
      "Sie will auf der einen Seite demjenigen Rechnung tragen, was gerade mit der besonderen Aus- 120 bildung der neueren Denk- und Forschungsmethoden in der Naturwissenschaft zu erreichen ist, auf der anderen Seite den menschlichen Bedürfnissen nach einer geistigen Welt und ihrer Erkenntnis. Man stand auf der einen Seite vor der Tatsache, die naturwissenschaftlichen Methoden voll anzuerkennen, und in bezug auf die Behandlung des naturwissenschaftlichen GeBietes - ich haBe das schon ausgesprochen - Bin ich heute selBst noch so Haeckel- ianer, wie ich es in den 90er Jahren des vorigen Jahrhun- derts gewesen Bin; nicht in dem Sinne, als oB die natur- wissenschaftlichen Methoden nicht weitergeBildet wer- den müßten und als oB nicht gerade von Seiten der Naturwissenschaft manches gegen das, was Haeckel ge- schrieben hat, eingewendet werden müßte, aBer da kommt man auf ein ganz anderes DiskussionsgeBiet, ich meine in der Behandlung der rein natürlichen Welt Bin ich heute genauso Haeckelianer wie damals.",
      "Es handelt sich mehr darum, was man an der naturwissenschaftlichen Betrachtungsart erlebt, namentlich dadurch, daß man sich erzieht in naturwissenschaftlicher Exaktheit, in na- turwissenschaftlicher Gesinnung, also um das, was man dadurch ausBilden kann an Ideen und Begriffen, die man einfach Braucht, wenn man naturwissenschaftlich arBei- ten will. Denn eines BleiBt für alle WeltBetrachtung - ich kann wegen der Kürze der Zeit jetzt den Beweis dafür nicht erBringen - eine Wahrheit: Wenn für die äußere SinnesBeoBachtung der Satz gilt: Es ist nichts im Ver- stande, was nicht vorher in den Sinnen ist , so gilt ganz gewiß auf der anderen Seite der LeiBnizsche Satz: «außer der Verstand selber».",
      "Im ErleBen des Verstandes, das heißt in dem Sich- Bewegen der Seele in den Verstandes-Kategorien, in dem ErleBen der Ideen, mit denen man die Naturobjekte, die 121 Naturtatsachen untersucht und die man zuletzt zur For- mulierung der Naturgesetze braucht, in dem Erleben dieser Ideenwelt liegt etwas, was durchaus über das Erleben von bloß Sinnlichem hinausgeht, so daß man, wenn man als naturwissenschaftlicher Forscher der Na- turwissenschaft gegenübersteht, sich sagen muß, wenn man unbefangen genug dazu ist: Alles das, was im Ver- stande ist, muß aus den Sinnen heraus geschöpft werden, nur der Verstand selbst kann nicht aus den Sinnen heraus geschöpft werden. Hat man aber einmal lebensvoll dies begriffen, dann gibt es auch kein Hindernis dafür, nun zu betrachten, was innerlich gewissermaßen angeschaut wird in der Verfolgung, die Verstandes-Kategorien weiterzubilden durch einen innerlichen seelisch-geistigen Prozeß, durch einen solchen Prozeß, der innerlich etwas ganz ähnliches ist wie äußere Wachstumsprozesse bei der Pflanze und beim Tier.",
      "Man bleibt durchaus mit seiner Gesinnung gerade dem natürlichen Werden treu, wenn man zugibt, daß aus dem Keim, den man in innerlicher Anschauung vor sich hat, man die Wahrheit gewinnt, daß der Verstand selbst nicht aus der Sinneswelt geschöpft werden kann. Man bleibt dem treu, was man erlernt hat an dem na- türlichen Dasein, wenn man den Versuch macht, den menschlichen Verstand selbst als einen Keim zu be- trachten, der innerlich wachsen kann; und wenn man diesen Versuch wirklich unternimmt, dann ist das übrige eine unmittelbare Folge dessen, was ich m diesen Tagen hier und an anderen Orten geschildert habe von dem Wachsen des menschlichen Intellekts in Imagination, Inspiration und Intuition.",
      "Das ist lediglich eine Sache des weiteren Fortschrittes der inneren menschlichen Entwicklung. Dadurch ergibt sich aber eine wirkliche 122 Anschauung der geistigen Welt. Diese Anschauung der geistigen Welt versucht man in der Anthroposophie, so gut es geht, nach dem heutigen Sprachgebrauch in Worte zu kleiden.",
      "Man ist natürlich oftmals genötigt, das, was man schaut - ich gebe es ohne weiteres zu -, in ungenü- gender Weise in Worte zu kleiden, aus dem einfachen Grunde, weil unsere Sprache, wie alle modernen Spra- chen, im Laufe der letzten Jahrhunderte angepaßt wurde dem äußeren materiellen Weltanschauen und wir heute einfach die Empfindungen, die wir bei den Worten haben, schon mehr oder weniger an dieser Weltanschauung orientiert haben. Daher ringt man immer mit den Worten, wenn man in die Notwendigkeit versetzt ist, dasjenige, was durch Imagination, Inspiration, Intuition angeschaut wurde, in Worte einzukleiden, es namentlich so in Worte einzu- kleiden, daß es nun wirklich nachgeprüft werden kann durch den gewöhnlichen gesunden Menschenverstand, denn dies muß wiederum ein Ziel anthroposophischer Forschung sein.",
      "So war Anthroposophie einfach ein Arbeitsgebiet, und als solches Arbeitsgebiet wird sie im strengsten Sinne des Wortes von mir aufgefaßt. Diejenigen Men- schen, die es war zunächst ein sehr kleiner Kreis - ein Bedürfnis hatten, etwas zu hören über das, was durch eine solche Forschungsmethode aus der übersinnlichen Welt erkundet werden kann, denen wurde das gesagt und gezeigt, was auf diese Weise gefunden werden kann.",
      "Niemand wurde irgendwie herangezwungen an diese Bewegung durch etwas anderes als durch seinen eigenen freien Willen, daran teilzunehmen. Was darüber gesagt wird, daß irgendwie suggestive Mittel oder dergleichen angewendet werden, das ist bei den einen eine bewußte, 123 bei den ändern eine unbewußte Verleumdung dessen, was in der anthroposophischen Bewegung eigentlich gewollt wird.",
      "Und es gilt, daß der, welcher mit seinem gesunden Menschenverstand dasjenige nachdenkt, was durch Imagination, Inspiration und Intuition erforscht wird, im höheren Sinne gerade ein freierer Mensch wird, als es die Menschen in der Gegenwart sind. Diese Men- schen der Gegenwart laufen zum Beispiel ihren Par- teiströmungen nach, lassen sich alles Mögliche suggerie- ren.",
      "Von diesen inneren seelischen Abhängigkeiten gerade muß Anthroposophie die Menschen befreien, weil sie darauf Anspruch macht, daß jeder, der sich in sie einle- ben will, nicht bloß in dem gewöhnlichen, mehr passiven Denken verharrt, sondern das Denken innerlich beweg- lich macht, es erkraftet, und durch dieses innerlich er- kraftete Denken wird man gerade ein freier Mensch. Aus Gründen, auf die ich heute nicht eingehen will, kam es, daß von den wissenschaftlich orientierten Men- schen, auf die eigentlich bei der Anthroposophie gerade gerechnet war, anfangs nur sehr wenige an die Anthro- posophie herankamen.",
      "Heute haben wir damit einen gewissen Anfang gemacht. Denjenigen Menschen, welche zuerst in die anthroposophische Bewegung hineinkamen es waren mehr oder weniger naive Gemüter mit star- ken seelischen Bedürfnissen -, denen wurde niemals etwas anderes gesagt als das, was in gewissenhafter Weise innerhalb der anthroposophischen Forschung gefunden werden konnte.",
      "Und ich freute mich immer, wenn mir Dinge gesagt wurden, wie zum Beispiel von einer heute auch hier anwesenden, sehr verehrten Persönlichkeit: Es ist eigentlich merkwürdig, daß Sie überhaupt einen größeren Zuhörerkreis bekommen, denn Sie vermeiden es eigentlich in der Art zu sprechen, was man sonst 124 populär, allgemein verständlich nennt. Sie sprechen so, daß die Menschen eigentlich immer eine innere Arbeit verrichten müssen beim Zuhören, und das wollen doch heute die Leute nicht, so daß man sich eigentlich wundern muß, daß Sie einen größeren Zuhörerkreis finden. - So ähnlich klangen die Worte, die mir eine heute auch hier sitzende Persönlichkeit vor Jahren sagte, nachdem sie damals eine Reihe von Vorträgen angehört hatte.",
      "Nach Popularität bin ich wahrlich niemals gegangen, indem ich Anthroposophie habe vor der Welt zur Geltung bringen wollen. Nun war es das Eigentümliche, daß zu uns Menschen aus allen Lebenskreisen und auch aus allen Bekenntnis- kreisen gekommen sind.",
      "Und insofern Anthroposophie auf diese Weise einfach durch ihre Arbeit in ein gewisses Verhältnis kam zur religiösen Strömung der Gegenwart, kam sie eigentlich zunächst niemals in irgendeinen Kon- flikt mit den religiösen Bedürfnissen derjenigen Men- schen, die zu ihr kamen: Leute - wie gesagt - aller Lebenskreise. Ich bin zum Beispiel von Katholiken, die sich in unserer Mitte befinden, oftmals gefragt worden, ob es in bezug auf praktische religiöse Übung möglich sei, Katholik zu bleiben, wenn man an der anthroposo- phischen Bewegung teilnimmt.",
      "Gerade bei Katholiken mußte ich sagen: Selbstver- ständlich ist es auch möglich, daß man als ganz guter Katholik teilnimmt an dem, was Anthroposophie bietet, denn Anthroposophie ist dazu da, nicht in der Beschrän- kung auf ein bestimmtes Bekenntnis über die übersinn- liche Welt zu reden, sondern einfach auf Grundlage dessen, was in der übersinnlichen Welt erforscht werden kann. So würde es mir am meisten entsprechen, dasjenige, was da aus der übersinnlichen Welt herauskommt, ein- 125 fach zu den Menschen zu sagen und gar nicht teilzu- nehmen an irgendeiner Polemik.",
      "Denn der, der ehrlich dasjenige sagt, was er erschaut, weiß ja, wodurch Pole- miken entstehen und wie unfruchtbar sie eigentlich sind. Mein ursprüngliches Bestreben war einfach, schlicht und ehrlich dasjenige zu sagen, was durch Anthroposophie gefunden werden kann, und keine Rücksicht zu nehmen auf die Polemiken.",
      "Solche Dinge gehen ja aber im Leben nicht immer so ab. Doch innerhalb der anthroposophi- schen Bewegung fanden sich eben die Menschen aller Glaubenskreise zusammen, auch Katholiken, und so mußte ich sagen: Auch der Katholik kann selbstver- ständlich an der anthroposophischen Bewegung teil- nehmen, er wird nur in einem einzigen Punkte in Kon- flikt kommen mit der praktischen Ausübung der Religion, und das ist die Ohrenbeichte.",
      "Nicht aus dem Grunde, weil sie Ohrenbeichte ist, denn das könnte als eine bloße Gewissenssache betrachtet werden. Ich habe genug pro- testantische Geistliche gefunden, die geradezu gelechzt haben nach einer Art von Ohrenbeichte, um in eine Art intimeres Verhältnis zur Gemeinde zu kommen.",
      "Darüber kann man verschiedene Ansichten haben. Aber hier handelt es sich darum, daß die katholische Kirche dem- jenigen das Altarsakrament verweigert, der nicht vor- her die Ohrenbeichte abgelegt hat. Und wegen dieser Verhinderung, praktisch teilzunehmen an dem wichtig- sten Sakrament der katholischen Kirche, ist es für den Katholiken außerordentlich schwierig, dann diejenigen Überzeugungen, die er aus der übersinnlichen Welt be- kommt, zu vereinigen mit diesem Verhalten, das ein unfreies ist, und das er durch die römisch-katholische Kirchenverfassung dennoch befolgen muß.",
      "Die Ohren- beichte, so wie sie gehandhabt wird, reißt - nicht we- 126 gen der Anthroposophie, sondern wegen der römisch- katholischen Kirchenverfassung - den Katholiken her- aus aus dem freien Verfolgen der übersinnlichen Welt. Das würde der Katholik vermeiden können, wenn er die Ohrenbeichte vermeiden könnte.",
      "Er kann sie nicht vermeiden, weil er sonst des Abendmahles nicht teilhaf- tig werden könnte. Hier liegt die Schwierigkeit, in die der Katholik kommt. Aber dennoch haben sich viele Katholiken gefunden, die innerhalb der anthroposophi- schen Bewegung die Bedürfnisse ihrer Seele zu befriedigen versuchen.",
      "Sehr verehrte Anwesende, es war natürlich, daß Menschen aller Bekenntnisse an die Anthroposophie herankamen, es war natürlich, daß einfach aus unserer Zeit heraus ein starkes Bedürfnis danach entstand, inner- halb der Anthroposophischen Gesellschaft über das zu reden, was das Christentum betrifft. Nun möchte ich darüber das Folgende sagen: Gerade so wie alle anderen Objekte der Forschung, insofern in diesen Objekten zusammenfließen Übersinnliches und Sinnliches in die- ser Welt, gerade so betrachtet Anthroposophie zunächst den Inhalt der Christologie; und ebenso versucht sie mit Hilfe ihrer übersinnlichen Forschung über den Inhalt der Christologie dasjenige zu erforschen und zu geben, was eben mit ihren Methoden erlangt werden kann.",
      "Nun ist es schwer, in ein paar Worten etwas zu sagen, was die Stellung der Anthroposophie zur Christologie charak- terisieren kann, aber ich möchte das Folgende bemerken. Wir sehen den Menschen zunächst hier im Erdenleben zwischen Geburt und Tod so, daß er mit seinem seeli- schen und geistigen Leben in dem physischen Leibe sein Dasein hat, daß er an seinen physischen Leib gebunden ist in bezug auf das Anschauen und auf die Verarbeitung 127 dessen, was m seiner Umgebung ist, auch m bezug auf seine Arbeit selbst, in bezug auf sein Willensleben und überhaupt in bezug auf die Art, wie er sich in diese sinnlich-physische Welt hineinstellt.",
      "Wenn nun der Mensch den Blick zurücklenkt, den er, aufwachend, selbstverständlich in seine Umgebung wendet, so be- kommt er zunächst Anschauungen einfach durch die Sinne seines Leibes, durch den Verstand, der die Erfah- rungen dieser Sinne und die Anschauungen über das, was in seiner physischen Umgebung ist, kombiniert. Da aber der Verstand, der Intellekt sein Urgeistiges, sein selbsteigenes Geistiges in sich trägt, so kann der Mensch - wenn er nur genügend sich auf sich selbst besinnt, wenn er nur ein wenig wegblickt von der Umge- bung und in sich selbst blickt -, nicht ableugnen, daß er durch seine eigene Tätigkeit zu einer Zusammenfassung kommt, die zuletzt in einer Vorstellung gipfelt, die nur einen geistigen Inhalt hat, und dieser geistige Inhalt ist - wenn ich mich so ausdrücken darf - die göttliche Vater- Vorstellung.",
      "Hier muß anthroposophische Forschung mit ihren Mitteln eingreifen. Ich kann das nur kurz charakterisieren; sie macht ja den ganzen Erkenntnisar- beitsprozeß des Menschen allmählich durchsichtig - das wird ja auch aus den Vorträgen dieses Kurses hervorge- hen.",
      "Sie will ja auch auf dasjenige hinweisen, was durch den Menschen geschieht, wenn er den Blick zurückzu- wenden versucht von der äußeren Welt, um gewisser- maßen das anzuschauen, was er selbst getan hat und sich zu fragen: Was hast du da eigentlich getan? Was berechtigt dich denn überhaupt, die äußere Welt [zu einer Vorstel- lung] zusammenzufassen?",
      "Und indem er dieses Erlebnis genügend weit verfolgt, kommt der Mensch wenn ich wieder das Wort gebrauchen darf - zum göttlichen 128 Vater-Erlebnis. Und wer dieses Kommen zum göttli- chen Vater-Erlebnis anthroposophisch durchschaut, der kommt zu einem ganz bestimmten Urteil.",
      "Ich bitte, dieses Urteil, das eine Tatsache ist, die ich radikal aus- sprechen muß, nicht mißzuverstehen. Man kommt zu dem Urteil, daß einfach der vollge- sunde Mensch - derjenige Mensch, der in seinem phy- sischen Leibe voll gesund ist - zu diesem göttlichen Vater-Erlebnis kommt -, das heißt, daß derjenige, der zu diesem göttlichen Vater-Erlebnis nicht kommt, irgend- wo etwas von Degenerationserscheinungen, wenn auch noch so verborgener Art, in sich trägt.",
      "Mit anderen Worten, man kommt durch anthroposophische For- schung darauf, zu sagen: Nicht zum göttlichen Vater- Erlebnis zu kommen, bedeutet beim Menschen eine Krankheit. Das ist natürlich radikal gesprochen, weil die Krankheit eben durchaus nicht mit den gewöhn- lichen physischen Mitteln gesehen werden kann, weil sie - wenn ich so sagen darf -, in den Feinheiten der menschlichen Organisation liegt.",
      "Aber tatsächlich er- gibt sich für den, der anthroposophisch forschen kann: Atheismus ist Krankheit. Was ich gestern gesagt habe über das Ausbilden des Urteils, das richtig oder falsch, gesund oder krank sein kann, das setzt hier ganz besonders ein.",
      "Wenn der Mensch diesen Weg allein verfolgt, kommt er zunächst nur zu dem göttlichen Vater-Erlebnis. Wenn er aber dann den Weg weiter verfolgt, wenn er gewahr wird, welcher Mangel in seiner Seele lebt, wenn er nur zu diesem Vater-Erlebnis kommt, wenn er gewahr wird, daß im Grunde genommen einfach in der Beschränkung der modernen Menschheit auf den Intellektualismus auch eine Art Beschränkung auf dieses göttliche Vater-Erlebnis 129 liegt, dann muß der Mensch darauf kommen, weiterzu- dringen von diesem göttlichen Vater-Erlebnis aus.",
      "Hier können uns äußere Beobachtungen sehr gut unterstützen. Es ist eine merkwürdige Tatsache, daß gerade in westlichen Ländern, wo die naturwissenschaftliche Ge- sinnung gewissermaßen bis zum Maximum ihrer Inten- sität gekommen ist, und wo man diese naturwissen- schaftliche Gesinnung nicht hineinreden lassen will in das Gebiet des Übersinnlichen, das der Religion bewahrt bleiben soll, daß gerade in diesen religiösen Bewegungen der westlichen Länder dasjenige, was der Geist des Alten Testamentes ist, besonders erfolgreich auch in unserer neueren Zeit wiederum eingegriffen hat.",
      "Und wir sehen den Westen, wenn er auch äußerlich das Christentum annimmt und predigt, dieses durchaus im Geiste des Alten Testamentes tun; wir sehen ihn in einem gewissen Sinne den Christus umprägen in den Vatergott und nicht wahrnehmen die Differenz zwischen dem Vatergott und dem Christus. Im Osten dagegen, wo für das Menschengemüt die Trennung zwischen der Religion und der Wissenschaft nicht so vorhanden ist wie im Westen, im Osten, wo diese Brücke für die Menschenseele mehr oder weniger als elementares inneres Seelenerlebnis vorhanden ist - wir finden es zum Beispiel noch in den Ausführungen des großen Philosophen Wladimir Solowjew -, dort se- hen wir, wie das Christus-Erlebnis als ein selbständiges Erlebnis unmittelbar vorhanden ist neben dem Vater- Erlebnis.",
      "Und auf diese Art kommt man dazu, sich zu sagen: Zwar kann der vollständig gesunde Mensch nicht Atheist sein, wenn er das, was ihm die äußere Welt gibt, zusam- menfaßt in der Spitze der Gottes-Vorstellung, der er 130 einen geistigen Inhalt geben muß; er bleibt aber zunächst bei der Vater-Vorstellung. Man kommt mit dieser Vater- Vorstellung aber nicht hinaus über die Zusammenfassung der äußeren Naturereignisse, sie versagt sofort, wenn man damit nun die eigene menschliche Entwicklung verfolgen will; man steht dann gewissermaßen verlassen da.",
      "Vertieft man sich in diese menschliche innere Ent- wicklung von diesem Punkt aus, an dem man ange- kommen ist, wenn man die äußere Welt in seine Seele aufgenommen hat - verfolgt man die innere Entwicklung, dann wird man, wenn man sie nur unbefangen verfolgt, zu dem Christus-Erlebnis kommen, das zunächst als ein unbestimmtes inneres Erlebnis da ist. Dieses Erlebnis aber verfolgt wieder erkennend Anthroposophie.",
      "Der Mensch kommt, einfach durch ehrliches Anschauen der Menschheitsentwicklung auf der Erde dazu, das Myste- rium von Golgatha, das historische Mysterium von Golgatha, nun selber ins Auge zu fassen. Er kommt dazu durch das innerliche Ausbilden geistiger Organe, [sie führen ihn zu] Imagination, Inspiration und Intuition.",
      "Wenn man mit Hilfe dieser Forschungsmittel den Weg verfolgt, den die Menschheitsentwicklung vom Altertum bis zum Mysterium von Golgatha genommen hat, so findet man, daß gerade in den Religionsvorstellungen überall - und nicht nur in der alttestamentlichen Re- ligionsvorstellung, sondern in allen Religionsvorstel- lungen - lebte eine Hinneigung zu dem kommenden Christus-Geist. Dann kann man einfach durch Anschauung erkennen lernen, wie dieser Christus-Geist in der Zeit vor dem Mysterium von Golgatha nicht mit der Erde vereinigt war.",
      "Verfolgen wir alles, was in den Mysterien gesucht worden ist, was in den populären [vorchristlichen] Reli- 131 gionen war, so sehen wir, wie die Vorstellungen, die sie sich von den Göttern machten, überall zuletzt doch zusammenschmolzen zu dem, was die Christus-Vorstel- lung ist. Wir sehen, wie sich die Gemüter der Menschen über die Erde hinaus zu dem Überirdischen erhoben, wenn sie zu ihren Göttern ihre Seelen wandten.",
      "Und wir sehen, wie im Ausgangspunkte der irdischen Mensch- heitsentwicklung einfach durch die menschliche Orga- nisation dem Menschen mehr gegeben war als das, was er durch seine Sinne und durch seinen Verstand in der Umgebung seines Erdendaseins wahrnehmen konnte. Es kam in die menschliche Seele das hinein - am stärksten in uralten Zeiten, dann immer weniger und weniger -, was ich instinktives Schauen nennen möchte, traumartiges Schauen, Anschauen einer geistigen - nichtirdischen - Welt, der der Mensch sich angehörig fühlte.",
      "In dem Augenblicke, wo der Mensch durch die Mysterien oder durch die populären Religionen dazu gebracht worden ist, hinauf gehoben zu werden mit seiner Seele zu dem, was er als Außerirdisches schauen konnte und mit dem er sich selbst einig wußte in seinem tiefstinneren Wesen, in diesem Augenblicke hatte der Mensch erlebt im Innern seine Wiedergeburt. Nun, meine sehr verehrten Anwesenden, wenn wir vom anthroposophischen Gesichtspunkt die Mensch- heitsentwicklung bis zum Mysterium von Golgatha ver- folgen, zeigt sich, daß gerade diese Fähigkeiten, die da im Inneren des Menschen saßen, eigentlich immer geringer und geringer wurden und nicht mehr da waren in dem Augenblick, wo das Mysterium von Golgatha auf der Erde eintrat.",
      "Gewiß, Reste blieben immer da, weil die Entwicklung nicht so sprunghaft vor sich geht. Einzelne Menschen bewahrten sich, wenn auch vielleicht ein un- 132 genaues Schauen, so aber doch ein instinktives Bewußt- sein von dem, was einmal geschaut worden ist; das kann man verfolgen bis in die Kunst hinein.",
      "Dann kam auf die Erde das Mysterium von Golgatha. Und in dem My- sterium von Golgatha sieht Anthroposophie eben das Einströmen desjenigen Geistes, der vorher nur im Au- ßerirdischen gesucht werden konnte, in einen Men- schenleib: das Einströmen des Christus in den Men- schenleib des Jesus.",
      "Wie das im einzelnen vorgestellt werden kann, darüber kann man nur mit denjenigen diskutieren, die sich positiv auf die Forschung auf die- sem Gebiete einlassen. Da zeigt Anthroposophie, wie von jener Zeit an, von dem Mysterium von Golgatha an, eine andere Zeit auf der Erde eingetreten ist, die Zeit, von der alle alten religiösen Bekenntnisse [gesprochen haben].",
      "Und der Christus, der durch das Mysterium von Golgatha gegangen ist, der Christus, den Paulus geschaut hat auf dem Wege nach Damaskus, der Christus ist dann innerhalb der Erde bei der Menschheit geblieben. Das wollen die Worte sagen: Ich bin bei Euch alle Tage bis an das Ende der Welt. - Er lebt unter uns, er kann wieder- gefunden werden.",
      "Das Paulus-Ereignis kann mit gewis- ser Vorbereitung immer wieder und wieder erneuert werden. Dann aber, wenn in dieser Weise der Weg zu dem Christus gesucht wird, erlebt der Mensch, indem er auf seine eigene innere Entwicklung schaut, eben den seit dem Mysterium von Golgatha auf der Erde wandelnden Christus durch Anschauung; dann findet er in innerlichem Erleben den Christus so, wie er durch Erleben der äuße- ren Welt, wenn er nicht krankhaft atheistisch ist, den Vatergott findet.",
      "So kann ich nur ganz flüchtig, skizzenhaft andeuten, wie Anthroposophie durch wirkliche Forschung zu 133 dem Christus-Ereignis als zu einer objektiven Tatsache kommt. In allen möglichen Einzelheiten versucht An- throposophie das Christus-Ereignis hinzustellen als die wichtigste Tatsache des Erdenlebens der Menschheit, als dasjenige, was objektiv geschehen ist.",
      "Daher ist auch der ganze Geist, in dem das Christus-Ereignis in der An- throposophie dargestellt wird, so, daß dieses Ereignis einfach als Tatsache hingenommen werden kann. Und wir hatten gerade innerhalb der anthroposophischen Bewegung erlebt, daß zum Beispiel Bekenner des Juden- tums im echtesten, wahrsten und ehrlichsten Sinne sich fanden zur Anerkennung des Mysteriums von Golgatha.",
      "Damit aber, meine sehr verehrten Anwesenden, ist viel- leicht gerade durch die anthroposophische Bewegung schon das vorausgenommen, was überhaupt in der zu- künftigen Entwicklung der Menschheit eintreten muß: daß, indem man unmittelbar hinweist auf das, was ge- schaut werden kann im Mysterium von Golgatha, der Weg zum Christentum wiedergefunden werden kann. Es ist durchaus die Frage, ob es nicht doch eine tiefe Bedeutung hat, was in dem Buche von Friedrich Nietz- sches Freund Overbeck enthalten ist, daß ja die moderne Theologie gar nicht mehr christlich sei.",
      "Würde darin einige Berechtigung liegen, so dürfte man vielleicht doch mit einem gewissen Recht sagen: Anthroposophie ist geeignet, in lebendiger Weise den Menschen hinzufüh- ren zu dem Christus-Erlebnis. Sie stellt die Zeit, in welcher das Christus-Ereignis stattgefunden hat, so dar, daß von den alten instinktiven Anschauungen bei einzel- nen Menschen noch so viel vorhanden war, daß der geistige Untergrund, ich möchte sagen, die geistige Substanzialität des Mysteriums von Golgatha geschaut und in den ersten christlichen Jahrhunderten anerkannt 134 werden konnte.",
      "Wir sehen dann, wie das immer weniger und weniger wird, wir sehen es völlig verglimmen bei einer solchen Erscheinung wie Scotus Erigena, wir sehen immer mehr und mehr sich ausbilden die mittelalterliche Theologie, wo man versuchte, sich auseinanderzusetzen mit dem, was die moderne Menschheit ausbilden mußte, mit dem Intellekt, der, wenn er unmittelbar sich selbst überlassen ist und sich innerlich nicht weiter entwickelt, nicht herankommen kann an die übersinnlichen Welten. Sie spaltete dasjenige, was in die Menschenseele hinein- kommen wollte, gewissermaßen auf in das, was der Mensch durch den Intellekt erkennen kann, und in das Unerkennbare, zu dem der Mensch nicht selbst gelangen kann, sondern nur durch eine Offenbarung.",
      "Aus diesen Untergründen heraus kann man die ganze mittelalterliche Theologie begreifen, besonders die tho- mistische Theologie, die von dem Katholizismus als die allein maßgebende erachtet wurde. Davon wird heute manches gesagt werden können.",
      "Worum es der Anthro- posophie zu tun war und ist, das ist nichts anderes, als in einfacher und schlichter Weise auszusprechen, was für die geistige Anschauung da ist. Und wie Anthroposophie zu dem Satz kommt, der Atheismus ist eigentlich verborgene Krankheit, so kommt sie zu dem zweiten Satze: Den Christus nicht zu finden, zu dem Christus keine Beziehung zu finden, ist für den Menschen ein Schicksal, ein Schicksalsunglück!",
      "Atheis- mus ist eine Krankheit, den Christus nicht zu finden ist ein Schicksalsunglück; denn man kann ihn finden im innerlichen Erleben. Dann aber stellt er sich dar als diejenige Wesenheit, die durch das Mysterium von Golgatha gegangen ist.",
      "Man kann durch innerliches Er- leben allein zu dem Christus kommen, man braucht 135 nicht anthroposophische Forschung, um ein religiöser Mensch im christlichen Sinne zu sein. Dann aber, wenn man zu dem Christus kommt, dann wird man ein Glied der geistigen Welt und man kann wirklich von einer Auferstehung der menschlichen Wesenheit in der geisti- gen Welt sprechen, von einer Erweiterung des Seelen- wesens in dem Erleben der geistigen Welt, und man kann davon sprechen, daß derjenige Mensch, der den Christus nicht findet, in einer gewissen Weise in bezug auf seine Weltanschauung beschränkt ist.",
      "Atheismus ist eine Krankheit! Nicht zum Christus kommen ist ein Schicksal, nicht zum Geiste kommen ist eine seelische Beschränktheit! Nun, meine sehr verehrten Anwesenden, Anthropo- sophie hat es aus solchen Untergründen heraus im Grunde genommen nur mit Religion zu tun, [nicht mit Theolo- gie], und mit Religion nur insofern, als die Menschen, die religiöse Bedürfnisse haben und diese in den gegenwär- tigen Bekenntnissen nicht befriedigen können, an die Anthroposophie herankommen.",
      "Anthroposophie will nur das tun, was innerhalb der heutigen Zeitbedürfnisse notwendig ist, und was die anderen nicht tun. Welche Gesinnung dem zugrunde liegt ich muß das immer wieder charakterisieren -, können Sie aus folgendem entnehmen.",
      "Schon vor vielen Jahren hielt ich einmal in einer süddeutschen Stadt - damals war sie eine deutsche Stadt, heute ist sie es nicht mehr - einen Vortrag über «Bibel und Weisheit». Bei diesem Vortrag waren auch zwei katholische Priester anwesend.",
      "Nach dem Vortrag ka- men die beiden zu mir und sagten: Wir haben eigentlich gar nichts in Ihrem Vortrage gefunden, was vom katho- lischen Standpunkte aus angefochten werden könnte. 136 Ich sagte: Wenn ich nur immer so glücklich sein könn- te! - Darauf sagten die beiden: Ja, aber eines ist uns aufgefallen; es ist nicht, was Sie sagen, sondern es ist die Art und Weise, wie Sie es vorbringen, und da müssen wir sagen: Sie reden zu Menschen, die in einer gewissen Beziehung vorbereitet sind. Sie reden zu einer Art von Gemeinde, welche eine bestimmte Bildung hat; wir aber reden für alle Menschen. - Ich sagte: Hochwürden, es kommt nicht darauf an, daß wir das nach unserem subjektiven Empfinden entscheiden, sondern darauf, daß wir uns als Menschen einleben mit unserer Arbeit in die Zeitenentwicklung, daß wir uns nicht einbilden, wir reden für alle Menschen, sondern daß wir uns eine sol- che Frage beantworten nach dem, was objektiv in der Menschheitsentwicklung lebt.",
      "So, wie ich mir einbilden kann, ich rede für alle Menschen und mich darin sehr irren kann -, so könnten Sie sich das einbilden. Für den Enthusiasmus ist es sehr gut, wenn man diese Einbildung hat. Aber fragen wir einmal: Kommen noch alle Men- schen, die heute ein Bedürfnis haben, über den Christus etwas zu hören, zu Ihnen in die Kirche? - Da konnten die beiden nicht Ja sagen, denn natürlich wußten Sie, daß eine Menge Menschen, die auch den Weg zum Christus suchten, nicht zu ihnen in die Kirche kamen.",
      "Da sagte ich: Sehen Sie, für die, die nicht zu Ihnen kommen, und doch den Weg zum Christus suchen, für diese rede ich. - Das heißt, sich seine Aufgaben aus der Zeitentwicklung heraus stellen, und nicht sich einbilden, man rede für alle Menschen, sondern sich zu fragen: Sind Gemüter da, die in einer besonderen Art dieses oder jenes entgegenneh- men wollen? Mit einer anderen Gesinnung wandte sich Anthropo- sophie auch niemals an irgendein religiöses Bekenntnis. 137 Wenn wir auch in der Waldorfschule dazu gelangt sind, gerade die Praxis unseres Unterrichtes aus der Anthropo- sophie heraus zu gestalten, so haben wir doch ganz davon abgesehen, aus der Waldorfschule eine solche Schule zu machen, durch die die Anthroposophie in die Gemüter der Kinder hineingepfropft würde.",
      "Mit Bezug auf den Religionsunterricht lassen wir die katholischen Kinder unterrichten von einem katholischen Pfarrer und die evangelischen von einem evangelischen Pfarrer. Nur für die Dissidentenkinder ist eine Art freier Religionsunter- richt eingerichtet worden, aber durchaus in christlichem Sinn.",
      "Da bringen wir aber nicht abstrakte Anthro-posophie vor auch keine konkrete Anthroposophie,wie sie an die Erwachsenen herangebracht werden kann -, sondern da versuchen wir mit aller Mühe, dasjenige an die Kinder heranzubringen, was ihrer realen Entwicklungsstufe entspricht; das muß aber alles nach Inhalt und Methode erst gesucht und gefunden werden. Durch den von uns eingerichteten freien Religionsunterricht haben wir er- reicht, daß nun auch diejenigen Kinder, die sonst gar keinen Religionsunterricht hätten, wieder an das Chri- stentum herangebracht werden, und sie kommen in Scharen, um an dieser Art des christlichen Religionsun- terrichtes teilzunehmen.",
      "Aber niemals haben wir eine irgendwie religiös geartete Propaganda getrieben inner- halb der anthroposophischen Bewegung und am wenig- sten wurde von der Anthroposophie aus irgend etwas un- ternommen gegen die einzelnen theologischen Systeme. Denn, was in dieser Beziehung der Anthroposophie allein obliegen kann, das ist, die einzelnen theologischen Systeme in ihrer Differenzierung begreiflich zu machen, und nicht, sie zu bekämpfen.",
      "Darin habe ich immer meine Aufgabe gesehen, wenn ich vor den Menschen 138 gesprochen habe, die zur Anthroposophie gekommen sind: begreiflich zu machen, warum der Katholizismus Katholizismus, der Protestantismus Protestantismus, das Judentum Judentum und der Buddhismus Buddhismus geworden ist, und wie in ihnen allen - ich glaube, das ist eine christliche Vorstellung - dasjenige Wesen lebt, das durch sein Schicksal der wirkliche Christ in seiner Seele zu erleben in der Lage ist. So hätte also gar nicht, wenn nicht von anderer Seite die Angriffe gekommen wären, ein Streit zu entstehen brauchen zwischen der Anthroposophie und der Theo- logie, und auch heute spreche ich diese Worte nur, weil das gewünscht wurde von denjenigen, die diesen heuti- gen Theologentag veranstalten.",
      "Was sich aber Anthro- posophie allein zur Aufgabe macht, ist die Verkündi- gung von anthroposophischen Forschungsergebnissen über die übersinnliche Welt. Deshalb war ich auch im- mer zurückhaltend besonders gegenüber den von theo- logischer Seite herrührenden Angriffen.",
      "Denn Anthropo- sophie will nicht als Kämpfer auf den Plan treten, son- dern sie will die von der Zeit geforderten berechtigten menschlichen Seelenbedürfnisse befriedigen. Und alle, die in diesem Sinne mit der Anthroposophie zusammen- wirken wollen zur Befriedigung dieser berechtigten, aus den Untergründen der Seele an die Oberfläche drängen- den menschlichen Seelenbedürfnisse, alle, die in diesem Sinne mit ihr arbeiten wollen, sind ihr willkommen! 139"
    ],
    "sentences": [
      [
        "Meine sehr verehrten Anwesenden!",
        "Ich bin genötigt, auszugehen von einer Zeitschriftennotiz, die mir eben überreicht worden ist, einer Notiz m der «Christlichen Welt», von der ich - weil ich sie vorher nicht kannte - selbstverständlich nicht dachte, bei meinen heutigen ein- leitenden Worten auszugehen."
      ],
      [
        "In dieser Zeitungsnotiz steht: «Vom 5. bis 12.",
        "März findet in Berlin ein anthro- posophischer Hochschulkurs statt. ...",
        "Der Tag der Theologen ist Freitag, der 10. - Diese Veranstaltung am Freitag ist nun eine unzweideutige Herausforderung Steiners und seiner Anhänger an die Theologen» und so weiter."
      ],
      [
        "Nun, meine sehr verehrten Anwesenden, diese heuti- ge Veranstaltung mag alles andere sein; das, was sie jedenfalls nicht ist und wodurch sie, wenn es der Glaube wäre, im allertiefsten Sinne mißverstanden würde, das ist eine Herausforderung an die Theologen.",
        "Ich selber bin an dieser Veranstaltung niemals in irgendeiner anderen Weise beteiligt gewesen, als daß ich gefragt worden bin, ob ich durch Vorträge und einleitende Betrachtungen mitwirken wolle an diesem Hochschulkurse, dessen Initiative nicht von mir ausgegangen ist."
      ],
      [
        "Ich bin am wenigsten beteiligt an der heutigen Veranstaltung, das heißt, an der Einfügung dieses Programmpunktes in den Hochschulkurs, und ich würde niemals daran gedacht 118 haben, daß dasjenige, was heute hier verhandelt werden soll, aufgefaßt werden könnte als eine «unzweideutige Herausforderung an die heutigen Theologen».",
        "Daher gestatten Sie auch, meine sehr verehrten An- wesenden, damit nicht wieder oder neuerdings alle mög- lichen Mißverständnisse sich an das knüpfen, was ich hier als ganz wenige einleitende Worte zu sagen haben werde, daß ich mich heute wirklich beschränke auf das Thema: Das Verhältnis der Anthroposophie zur Theo- logie, und daß ich mit Rücksicht darauf, daß nicht neue Mißverständnisse entstehen, auf einiges verzichte von dem, was von mir hier vorgebracht würde, weil ich sonst neuerdings sehen müßte, wie das verkannt wird, was von mir gewollt wird."
      ],
      [
        "Sehr verehrte Anwesende, es war niemals mein Be- streben - verzeihen Sie, wenn ich durch diese an mich ergangene Herausforderung gezwungen bin, heute ganz kurz in der Einleitung einzelne persönliche Bemerkun- gen zu machen -, es war eigentlich niemals meine Ab- sicht, irgendwie die Theologie herauszufordern, und von ihrem Ausgangspunkt an hat Anthroposophie, insofern sie ein Arbeitsgebiet darstellt, an dem ich selbst beteiligt bin, niemals irgendwie gesucht, sich innerhalb ihrer Arbeit mit der heutigen Theologie als solcher auseinanderzu- setzen.",
        "Das ist, insofern es geschehen ist, und es ist ja wirklich von mir so wenig wie möglich geschehen, le- diglich dadurch geschehen, daß Angriffe gegen die An- throposophie von theologischer Seite her allerdings sehr viele erfolgt sind, und daß man sich - nicht so sehr ich als andere - manchmal zur Wehr setzt."
      ],
      [
        "Denn Anthroposo- phie wollte als Arbeitsgebiet durchaus, ich möchte sagen, der Theologie gegenüber neutral bleiben, sie will arbei- ten aus dem gegenwärtigen Wissenschaftsgeist heraus. 119 Man hatte am Ende des vorigen Jahrhunderts eine gewisse wissenschaftliche Richtung, gewisse wissen- schaftliche Methoden, eine gewisse wissenschaftliche Gesinnung vor sich, eine Gesinnung und Methode, welche aus Gründen, über die ich schon gesprochen habe, und über die wegen der Kürze der Zeit nicht ausführlich gesprochen werden kann, eine Methode und Gesinnung, die man aus der ganzen geschichtlichen Entwicklung der neueren Zeit insbesondere anwendete auf die naturwis- senschaftliche Forschung, und durch die man innerhalb der naturwissenschaftlichen Forschung die größtmög- lichsten Triumphe - ich meine das nicht in einem trivialen, sondern in einem tieferen Sinne - für Menschenfortschritt und Menschenwohl errungen hat.",
        "Der naturwissen- schaftlichen Forschung stand in dieser Zeit die Philoso- phie, ich möchte sagen etwas ratlos gegenüber."
      ],
      [
        "Die Philosophie mußte sich auseinandersetzen mit denjenigen Methoden, welche vor allen Dingen auf die Naturwis- senschaft angewendet worden sind, und welche in der Philosophie, in der man es doch mit einem ganz anderen Tatsachengebiet zu tun hat, nicht anwendbar waren.",
        "Man war sich, ich möchte sagen theoretisch und er- kenntnistheoretisch nicht immer darüber klar, in wel- chem Sinne man mit den naturwissenschaftlichen Me- thoden in der Philosophie arbeiten sollte."
      ],
      [
        "Man ist dann in der experimentellen Psychologie auf ein gewisses Gebiet verfallen, wo es mehr oder weniger scheinbar oder auch mehr oder weniger richtig geht, aber die Un- sicherheit ist im Grunde genommen doch auch da vor- handen.",
        "Demgegenüber erarbeitete sich Anthroposophie aus den verschiedensten Untergründen heraus ihre eigene Arbeitsmethode."
      ],
      [
        "Sie will auf der einen Seite demjenigen Rechnung tragen, was gerade mit der besonderen Aus- 120 bildung der neueren Denk- und Forschungsmethoden in der Naturwissenschaft zu erreichen ist, auf der anderen Seite den menschlichen Bedürfnissen nach einer geistigen Welt und ihrer Erkenntnis.",
        "Man stand auf der einen Seite vor der Tatsache, die naturwissenschaftlichen Methoden voll anzuerkennen, und in bezug auf die Behandlung des naturwissenschaftlichen GeBietes - ich haBe das schon ausgesprochen - Bin ich heute selBst noch so Haeckel- ianer, wie ich es in den 90er Jahren des vorigen Jahrhun- derts gewesen Bin; nicht in dem Sinne, als oB die natur- wissenschaftlichen Methoden nicht weitergeBildet wer- den müßten und als oB nicht gerade von Seiten der Naturwissenschaft manches gegen das, was Haeckel ge- schrieben hat, eingewendet werden müßte, aBer da kommt man auf ein ganz anderes DiskussionsgeBiet, ich meine in der Behandlung der rein natürlichen Welt Bin ich heute genauso Haeckelianer wie damals."
      ],
      [
        "Es handelt sich mehr darum, was man an der naturwissenschaftlichen Betrachtungsart erlebt, namentlich dadurch, daß man sich erzieht in naturwissenschaftlicher Exaktheit, in na- turwissenschaftlicher Gesinnung, also um das, was man dadurch ausBilden kann an Ideen und Begriffen, die man einfach Braucht, wenn man naturwissenschaftlich arBei- ten will.",
        "Denn eines BleiBt für alle WeltBetrachtung - ich kann wegen der Kürze der Zeit jetzt den Beweis dafür nicht erBringen - eine Wahrheit: Wenn für die äußere SinnesBeoBachtung der Satz gilt: Es ist nichts im Ver- stande, was nicht vorher in den Sinnen ist , so gilt ganz gewiß auf der anderen Seite der LeiBnizsche Satz: «außer der Verstand selber»."
      ],
      [
        "Im ErleBen des Verstandes, das heißt in dem Sich- Bewegen der Seele in den Verstandes-Kategorien, in dem ErleBen der Ideen, mit denen man die Naturobjekte, die 121 Naturtatsachen untersucht und die man zuletzt zur For- mulierung der Naturgesetze braucht, in dem Erleben dieser Ideenwelt liegt etwas, was durchaus über das Erleben von bloß Sinnlichem hinausgeht, so daß man, wenn man als naturwissenschaftlicher Forscher der Na- turwissenschaft gegenübersteht, sich sagen muß, wenn man unbefangen genug dazu ist: Alles das, was im Ver- stande ist, muß aus den Sinnen heraus geschöpft werden, nur der Verstand selbst kann nicht aus den Sinnen heraus geschöpft werden.",
        "Hat man aber einmal lebensvoll dies begriffen, dann gibt es auch kein Hindernis dafür, nun zu betrachten, was innerlich gewissermaßen angeschaut wird in der Verfolgung, die Verstandes-Kategorien weiterzubilden durch einen innerlichen seelisch-geistigen Prozeß, durch einen solchen Prozeß, der innerlich etwas ganz ähnliches ist wie äußere Wachstumsprozesse bei der Pflanze und beim Tier."
      ],
      [
        "Man bleibt durchaus mit seiner Gesinnung gerade dem natürlichen Werden treu, wenn man zugibt, daß aus dem Keim, den man in innerlicher Anschauung vor sich hat, man die Wahrheit gewinnt, daß der Verstand selbst nicht aus der Sinneswelt geschöpft werden kann.",
        "Man bleibt dem treu, was man erlernt hat an dem na- türlichen Dasein, wenn man den Versuch macht, den menschlichen Verstand selbst als einen Keim zu be- trachten, der innerlich wachsen kann; und wenn man diesen Versuch wirklich unternimmt, dann ist das übrige eine unmittelbare Folge dessen, was ich m diesen Tagen hier und an anderen Orten geschildert habe von dem Wachsen des menschlichen Intellekts in Imagination, Inspiration und Intuition."
      ],
      [
        "Das ist lediglich eine Sache des weiteren Fortschrittes der inneren menschlichen Entwicklung.",
        "Dadurch ergibt sich aber eine wirkliche 122 Anschauung der geistigen Welt.",
        "Diese Anschauung der geistigen Welt versucht man in der Anthroposophie, so gut es geht, nach dem heutigen Sprachgebrauch in Worte zu kleiden."
      ],
      [
        "Man ist natürlich oftmals genötigt, das, was man schaut - ich gebe es ohne weiteres zu -, in ungenü- gender Weise in Worte zu kleiden, aus dem einfachen Grunde, weil unsere Sprache, wie alle modernen Spra- chen, im Laufe der letzten Jahrhunderte angepaßt wurde dem äußeren materiellen Weltanschauen und wir heute einfach die Empfindungen, die wir bei den Worten haben, schon mehr oder weniger an dieser Weltanschauung orientiert haben.",
        "Daher ringt man immer mit den Worten, wenn man in die Notwendigkeit versetzt ist, dasjenige, was durch Imagination, Inspiration, Intuition angeschaut wurde, in Worte einzukleiden, es namentlich so in Worte einzu- kleiden, daß es nun wirklich nachgeprüft werden kann durch den gewöhnlichen gesunden Menschenverstand, denn dies muß wiederum ein Ziel anthroposophischer Forschung sein."
      ],
      [
        "So war Anthroposophie einfach ein Arbeitsgebiet, und als solches Arbeitsgebiet wird sie im strengsten Sinne des Wortes von mir aufgefaßt.",
        "Diejenigen Men- schen, die es war zunächst ein sehr kleiner Kreis - ein Bedürfnis hatten, etwas zu hören über das, was durch eine solche Forschungsmethode aus der übersinnlichen Welt erkundet werden kann, denen wurde das gesagt und gezeigt, was auf diese Weise gefunden werden kann."
      ],
      [
        "Niemand wurde irgendwie herangezwungen an diese Bewegung durch etwas anderes als durch seinen eigenen freien Willen, daran teilzunehmen.",
        "Was darüber gesagt wird, daß irgendwie suggestive Mittel oder dergleichen angewendet werden, das ist bei den einen eine bewußte, 123 bei den ändern eine unbewußte Verleumdung dessen, was in der anthroposophischen Bewegung eigentlich gewollt wird."
      ],
      [
        "Und es gilt, daß der, welcher mit seinem gesunden Menschenverstand dasjenige nachdenkt, was durch Imagination, Inspiration und Intuition erforscht wird, im höheren Sinne gerade ein freierer Mensch wird, als es die Menschen in der Gegenwart sind.",
        "Diese Men- schen der Gegenwart laufen zum Beispiel ihren Par- teiströmungen nach, lassen sich alles Mögliche suggerie- ren."
      ],
      [
        "Von diesen inneren seelischen Abhängigkeiten gerade muß Anthroposophie die Menschen befreien, weil sie darauf Anspruch macht, daß jeder, der sich in sie einle- ben will, nicht bloß in dem gewöhnlichen, mehr passiven Denken verharrt, sondern das Denken innerlich beweg- lich macht, es erkraftet, und durch dieses innerlich er- kraftete Denken wird man gerade ein freier Mensch.",
        "Aus Gründen, auf die ich heute nicht eingehen will, kam es, daß von den wissenschaftlich orientierten Men- schen, auf die eigentlich bei der Anthroposophie gerade gerechnet war, anfangs nur sehr wenige an die Anthro- posophie herankamen."
      ],
      [
        "Heute haben wir damit einen gewissen Anfang gemacht.",
        "Denjenigen Menschen, welche zuerst in die anthroposophische Bewegung hineinkamen es waren mehr oder weniger naive Gemüter mit star- ken seelischen Bedürfnissen -, denen wurde niemals etwas anderes gesagt als das, was in gewissenhafter Weise innerhalb der anthroposophischen Forschung gefunden werden konnte."
      ],
      [
        "Und ich freute mich immer, wenn mir Dinge gesagt wurden, wie zum Beispiel von einer heute auch hier anwesenden, sehr verehrten Persönlichkeit: Es ist eigentlich merkwürdig, daß Sie überhaupt einen größeren Zuhörerkreis bekommen, denn Sie vermeiden es eigentlich in der Art zu sprechen, was man sonst 124 populär, allgemein verständlich nennt.",
        "Sie sprechen so, daß die Menschen eigentlich immer eine innere Arbeit verrichten müssen beim Zuhören, und das wollen doch heute die Leute nicht, so daß man sich eigentlich wundern muß, daß Sie einen größeren Zuhörerkreis finden. - So ähnlich klangen die Worte, die mir eine heute auch hier sitzende Persönlichkeit vor Jahren sagte, nachdem sie damals eine Reihe von Vorträgen angehört hatte."
      ],
      [
        "Nach Popularität bin ich wahrlich niemals gegangen, indem ich Anthroposophie habe vor der Welt zur Geltung bringen wollen.",
        "Nun war es das Eigentümliche, daß zu uns Menschen aus allen Lebenskreisen und auch aus allen Bekenntnis- kreisen gekommen sind."
      ],
      [
        "Und insofern Anthroposophie auf diese Weise einfach durch ihre Arbeit in ein gewisses Verhältnis kam zur religiösen Strömung der Gegenwart, kam sie eigentlich zunächst niemals in irgendeinen Kon- flikt mit den religiösen Bedürfnissen derjenigen Men- schen, die zu ihr kamen: Leute - wie gesagt - aller Lebenskreise.",
        "Ich bin zum Beispiel von Katholiken, die sich in unserer Mitte befinden, oftmals gefragt worden, ob es in bezug auf praktische religiöse Übung möglich sei, Katholik zu bleiben, wenn man an der anthroposo- phischen Bewegung teilnimmt."
      ],
      [
        "Gerade bei Katholiken mußte ich sagen: Selbstver- ständlich ist es auch möglich, daß man als ganz guter Katholik teilnimmt an dem, was Anthroposophie bietet, denn Anthroposophie ist dazu da, nicht in der Beschrän- kung auf ein bestimmtes Bekenntnis über die übersinn- liche Welt zu reden, sondern einfach auf Grundlage dessen, was in der übersinnlichen Welt erforscht werden kann.",
        "So würde es mir am meisten entsprechen, dasjenige, was da aus der übersinnlichen Welt herauskommt, ein- 125 fach zu den Menschen zu sagen und gar nicht teilzu- nehmen an irgendeiner Polemik."
      ],
      [
        "Denn der, der ehrlich dasjenige sagt, was er erschaut, weiß ja, wodurch Pole- miken entstehen und wie unfruchtbar sie eigentlich sind.",
        "Mein ursprüngliches Bestreben war einfach, schlicht und ehrlich dasjenige zu sagen, was durch Anthroposophie gefunden werden kann, und keine Rücksicht zu nehmen auf die Polemiken."
      ],
      [
        "Solche Dinge gehen ja aber im Leben nicht immer so ab.",
        "Doch innerhalb der anthroposophi- schen Bewegung fanden sich eben die Menschen aller Glaubenskreise zusammen, auch Katholiken, und so mußte ich sagen: Auch der Katholik kann selbstver- ständlich an der anthroposophischen Bewegung teil- nehmen, er wird nur in einem einzigen Punkte in Kon- flikt kommen mit der praktischen Ausübung der Religion, und das ist die Ohrenbeichte."
      ],
      [
        "Nicht aus dem Grunde, weil sie Ohrenbeichte ist, denn das könnte als eine bloße Gewissenssache betrachtet werden.",
        "Ich habe genug pro- testantische Geistliche gefunden, die geradezu gelechzt haben nach einer Art von Ohrenbeichte, um in eine Art intimeres Verhältnis zur Gemeinde zu kommen."
      ],
      [
        "Darüber kann man verschiedene Ansichten haben.",
        "Aber hier handelt es sich darum, daß die katholische Kirche dem- jenigen das Altarsakrament verweigert, der nicht vor- her die Ohrenbeichte abgelegt hat.",
        "Und wegen dieser Verhinderung, praktisch teilzunehmen an dem wichtig- sten Sakrament der katholischen Kirche, ist es für den Katholiken außerordentlich schwierig, dann diejenigen Überzeugungen, die er aus der übersinnlichen Welt be- kommt, zu vereinigen mit diesem Verhalten, das ein unfreies ist, und das er durch die römisch-katholische Kirchenverfassung dennoch befolgen muß."
      ],
      [
        "Die Ohren- beichte, so wie sie gehandhabt wird, reißt - nicht we- 126 gen der Anthroposophie, sondern wegen der römisch- katholischen Kirchenverfassung - den Katholiken her- aus aus dem freien Verfolgen der übersinnlichen Welt.",
        "Das würde der Katholik vermeiden können, wenn er die Ohrenbeichte vermeiden könnte."
      ],
      [
        "Er kann sie nicht vermeiden, weil er sonst des Abendmahles nicht teilhaf- tig werden könnte.",
        "Hier liegt die Schwierigkeit, in die der Katholik kommt.",
        "Aber dennoch haben sich viele Katholiken gefunden, die innerhalb der anthroposophi- schen Bewegung die Bedürfnisse ihrer Seele zu befriedigen versuchen."
      ],
      [
        "Sehr verehrte Anwesende, es war natürlich, daß Menschen aller Bekenntnisse an die Anthroposophie herankamen, es war natürlich, daß einfach aus unserer Zeit heraus ein starkes Bedürfnis danach entstand, inner- halb der Anthroposophischen Gesellschaft über das zu reden, was das Christentum betrifft.",
        "Nun möchte ich darüber das Folgende sagen: Gerade so wie alle anderen Objekte der Forschung, insofern in diesen Objekten zusammenfließen Übersinnliches und Sinnliches in die- ser Welt, gerade so betrachtet Anthroposophie zunächst den Inhalt der Christologie; und ebenso versucht sie mit Hilfe ihrer übersinnlichen Forschung über den Inhalt der Christologie dasjenige zu erforschen und zu geben, was eben mit ihren Methoden erlangt werden kann."
      ],
      [
        "Nun ist es schwer, in ein paar Worten etwas zu sagen, was die Stellung der Anthroposophie zur Christologie charak- terisieren kann, aber ich möchte das Folgende bemerken.",
        "Wir sehen den Menschen zunächst hier im Erdenleben zwischen Geburt und Tod so, daß er mit seinem seeli- schen und geistigen Leben in dem physischen Leibe sein Dasein hat, daß er an seinen physischen Leib gebunden ist in bezug auf das Anschauen und auf die Verarbeitung 127 dessen, was m seiner Umgebung ist, auch m bezug auf seine Arbeit selbst, in bezug auf sein Willensleben und überhaupt in bezug auf die Art, wie er sich in diese sinnlich-physische Welt hineinstellt."
      ],
      [
        "Wenn nun der Mensch den Blick zurücklenkt, den er, aufwachend, selbstverständlich in seine Umgebung wendet, so be- kommt er zunächst Anschauungen einfach durch die Sinne seines Leibes, durch den Verstand, der die Erfah- rungen dieser Sinne und die Anschauungen über das, was in seiner physischen Umgebung ist, kombiniert.",
        "Da aber der Verstand, der Intellekt sein Urgeistiges, sein selbsteigenes Geistiges in sich trägt, so kann der Mensch - wenn er nur genügend sich auf sich selbst besinnt, wenn er nur ein wenig wegblickt von der Umge- bung und in sich selbst blickt -, nicht ableugnen, daß er durch seine eigene Tätigkeit zu einer Zusammenfassung kommt, die zuletzt in einer Vorstellung gipfelt, die nur einen geistigen Inhalt hat, und dieser geistige Inhalt ist - wenn ich mich so ausdrücken darf - die göttliche Vater- Vorstellung."
      ],
      [
        "Hier muß anthroposophische Forschung mit ihren Mitteln eingreifen.",
        "Ich kann das nur kurz charakterisieren; sie macht ja den ganzen Erkenntnisar- beitsprozeß des Menschen allmählich durchsichtig - das wird ja auch aus den Vorträgen dieses Kurses hervorge- hen."
      ],
      [
        "Sie will ja auch auf dasjenige hinweisen, was durch den Menschen geschieht, wenn er den Blick zurückzu- wenden versucht von der äußeren Welt, um gewisser- maßen das anzuschauen, was er selbst getan hat und sich zu fragen: Was hast du da eigentlich getan?",
        "Was berechtigt dich denn überhaupt, die äußere Welt [zu einer Vorstel- lung] zusammenzufassen?"
      ],
      [
        "Und indem er dieses Erlebnis genügend weit verfolgt, kommt der Mensch wenn ich wieder das Wort gebrauchen darf - zum göttlichen 128 Vater-Erlebnis.",
        "Und wer dieses Kommen zum göttli- chen Vater-Erlebnis anthroposophisch durchschaut, der kommt zu einem ganz bestimmten Urteil."
      ],
      [
        "Ich bitte, dieses Urteil, das eine Tatsache ist, die ich radikal aus- sprechen muß, nicht mißzuverstehen.",
        "Man kommt zu dem Urteil, daß einfach der vollge- sunde Mensch - derjenige Mensch, der in seinem phy- sischen Leibe voll gesund ist - zu diesem göttlichen Vater-Erlebnis kommt -, das heißt, daß derjenige, der zu diesem göttlichen Vater-Erlebnis nicht kommt, irgend- wo etwas von Degenerationserscheinungen, wenn auch noch so verborgener Art, in sich trägt."
      ],
      [
        "Mit anderen Worten, man kommt durch anthroposophische For- schung darauf, zu sagen: Nicht zum göttlichen Vater- Erlebnis zu kommen, bedeutet beim Menschen eine Krankheit.",
        "Das ist natürlich radikal gesprochen, weil die Krankheit eben durchaus nicht mit den gewöhn- lichen physischen Mitteln gesehen werden kann, weil sie - wenn ich so sagen darf -, in den Feinheiten der menschlichen Organisation liegt."
      ],
      [
        "Aber tatsächlich er- gibt sich für den, der anthroposophisch forschen kann: Atheismus ist Krankheit.",
        "Was ich gestern gesagt habe über das Ausbilden des Urteils, das richtig oder falsch, gesund oder krank sein kann, das setzt hier ganz besonders ein."
      ],
      [
        "Wenn der Mensch diesen Weg allein verfolgt, kommt er zunächst nur zu dem göttlichen Vater-Erlebnis.",
        "Wenn er aber dann den Weg weiter verfolgt, wenn er gewahr wird, welcher Mangel in seiner Seele lebt, wenn er nur zu diesem Vater-Erlebnis kommt, wenn er gewahr wird, daß im Grunde genommen einfach in der Beschränkung der modernen Menschheit auf den Intellektualismus auch eine Art Beschränkung auf dieses göttliche Vater-Erlebnis 129 liegt, dann muß der Mensch darauf kommen, weiterzu- dringen von diesem göttlichen Vater-Erlebnis aus."
      ],
      [
        "Hier können uns äußere Beobachtungen sehr gut unterstützen.",
        "Es ist eine merkwürdige Tatsache, daß gerade in westlichen Ländern, wo die naturwissenschaftliche Ge- sinnung gewissermaßen bis zum Maximum ihrer Inten- sität gekommen ist, und wo man diese naturwissen- schaftliche Gesinnung nicht hineinreden lassen will in das Gebiet des Übersinnlichen, das der Religion bewahrt bleiben soll, daß gerade in diesen religiösen Bewegungen der westlichen Länder dasjenige, was der Geist des Alten Testamentes ist, besonders erfolgreich auch in unserer neueren Zeit wiederum eingegriffen hat."
      ],
      [
        "Und wir sehen den Westen, wenn er auch äußerlich das Christentum annimmt und predigt, dieses durchaus im Geiste des Alten Testamentes tun; wir sehen ihn in einem gewissen Sinne den Christus umprägen in den Vatergott und nicht wahrnehmen die Differenz zwischen dem Vatergott und dem Christus.",
        "Im Osten dagegen, wo für das Menschengemüt die Trennung zwischen der Religion und der Wissenschaft nicht so vorhanden ist wie im Westen, im Osten, wo diese Brücke für die Menschenseele mehr oder weniger als elementares inneres Seelenerlebnis vorhanden ist - wir finden es zum Beispiel noch in den Ausführungen des großen Philosophen Wladimir Solowjew -, dort se- hen wir, wie das Christus-Erlebnis als ein selbständiges Erlebnis unmittelbar vorhanden ist neben dem Vater- Erlebnis."
      ],
      [
        "Und auf diese Art kommt man dazu, sich zu sagen: Zwar kann der vollständig gesunde Mensch nicht Atheist sein, wenn er das, was ihm die äußere Welt gibt, zusam- menfaßt in der Spitze der Gottes-Vorstellung, der er 130 einen geistigen Inhalt geben muß; er bleibt aber zunächst bei der Vater-Vorstellung.",
        "Man kommt mit dieser Vater- Vorstellung aber nicht hinaus über die Zusammenfassung der äußeren Naturereignisse, sie versagt sofort, wenn man damit nun die eigene menschliche Entwicklung verfolgen will; man steht dann gewissermaßen verlassen da."
      ],
      [
        "Vertieft man sich in diese menschliche innere Ent- wicklung von diesem Punkt aus, an dem man ange- kommen ist, wenn man die äußere Welt in seine Seele aufgenommen hat - verfolgt man die innere Entwicklung, dann wird man, wenn man sie nur unbefangen verfolgt, zu dem Christus-Erlebnis kommen, das zunächst als ein unbestimmtes inneres Erlebnis da ist.",
        "Dieses Erlebnis aber verfolgt wieder erkennend Anthroposophie."
      ],
      [
        "Der Mensch kommt, einfach durch ehrliches Anschauen der Menschheitsentwicklung auf der Erde dazu, das Myste- rium von Golgatha, das historische Mysterium von Golgatha, nun selber ins Auge zu fassen.",
        "Er kommt dazu durch das innerliche Ausbilden geistiger Organe, [sie führen ihn zu] Imagination, Inspiration und Intuition."
      ],
      [
        "Wenn man mit Hilfe dieser Forschungsmittel den Weg verfolgt, den die Menschheitsentwicklung vom Altertum bis zum Mysterium von Golgatha genommen hat, so findet man, daß gerade in den Religionsvorstellungen überall - und nicht nur in der alttestamentlichen Re- ligionsvorstellung, sondern in allen Religionsvorstel- lungen - lebte eine Hinneigung zu dem kommenden Christus-Geist.",
        "Dann kann man einfach durch Anschauung erkennen lernen, wie dieser Christus-Geist in der Zeit vor dem Mysterium von Golgatha nicht mit der Erde vereinigt war."
      ],
      [
        "Verfolgen wir alles, was in den Mysterien gesucht worden ist, was in den populären [vorchristlichen] Reli- 131 gionen war, so sehen wir, wie die Vorstellungen, die sie sich von den Göttern machten, überall zuletzt doch zusammenschmolzen zu dem, was die Christus-Vorstel- lung ist.",
        "Wir sehen, wie sich die Gemüter der Menschen über die Erde hinaus zu dem Überirdischen erhoben, wenn sie zu ihren Göttern ihre Seelen wandten."
      ],
      [
        "Und wir sehen, wie im Ausgangspunkte der irdischen Mensch- heitsentwicklung einfach durch die menschliche Orga- nisation dem Menschen mehr gegeben war als das, was er durch seine Sinne und durch seinen Verstand in der Umgebung seines Erdendaseins wahrnehmen konnte.",
        "Es kam in die menschliche Seele das hinein - am stärksten in uralten Zeiten, dann immer weniger und weniger -, was ich instinktives Schauen nennen möchte, traumartiges Schauen, Anschauen einer geistigen - nichtirdischen - Welt, der der Mensch sich angehörig fühlte."
      ],
      [
        "In dem Augenblicke, wo der Mensch durch die Mysterien oder durch die populären Religionen dazu gebracht worden ist, hinauf gehoben zu werden mit seiner Seele zu dem, was er als Außerirdisches schauen konnte und mit dem er sich selbst einig wußte in seinem tiefstinneren Wesen, in diesem Augenblicke hatte der Mensch erlebt im Innern seine Wiedergeburt.",
        "Nun, meine sehr verehrten Anwesenden, wenn wir vom anthroposophischen Gesichtspunkt die Mensch- heitsentwicklung bis zum Mysterium von Golgatha ver- folgen, zeigt sich, daß gerade diese Fähigkeiten, die da im Inneren des Menschen saßen, eigentlich immer geringer und geringer wurden und nicht mehr da waren in dem Augenblick, wo das Mysterium von Golgatha auf der Erde eintrat."
      ],
      [
        "Gewiß, Reste blieben immer da, weil die Entwicklung nicht so sprunghaft vor sich geht.",
        "Einzelne Menschen bewahrten sich, wenn auch vielleicht ein un- 132 genaues Schauen, so aber doch ein instinktives Bewußt- sein von dem, was einmal geschaut worden ist; das kann man verfolgen bis in die Kunst hinein."
      ],
      [
        "Dann kam auf die Erde das Mysterium von Golgatha.",
        "Und in dem My- sterium von Golgatha sieht Anthroposophie eben das Einströmen desjenigen Geistes, der vorher nur im Au- ßerirdischen gesucht werden konnte, in einen Men- schenleib: das Einströmen des Christus in den Men- schenleib des Jesus."
      ],
      [
        "Wie das im einzelnen vorgestellt werden kann, darüber kann man nur mit denjenigen diskutieren, die sich positiv auf die Forschung auf die- sem Gebiete einlassen.",
        "Da zeigt Anthroposophie, wie von jener Zeit an, von dem Mysterium von Golgatha an, eine andere Zeit auf der Erde eingetreten ist, die Zeit, von der alle alten religiösen Bekenntnisse [gesprochen haben]."
      ],
      [
        "Und der Christus, der durch das Mysterium von Golgatha gegangen ist, der Christus, den Paulus geschaut hat auf dem Wege nach Damaskus, der Christus ist dann innerhalb der Erde bei der Menschheit geblieben.",
        "Das wollen die Worte sagen: Ich bin bei Euch alle Tage bis an das Ende der Welt. - Er lebt unter uns, er kann wieder- gefunden werden."
      ],
      [
        "Das Paulus-Ereignis kann mit gewis- ser Vorbereitung immer wieder und wieder erneuert werden.",
        "Dann aber, wenn in dieser Weise der Weg zu dem Christus gesucht wird, erlebt der Mensch, indem er auf seine eigene innere Entwicklung schaut, eben den seit dem Mysterium von Golgatha auf der Erde wandelnden Christus durch Anschauung; dann findet er in innerlichem Erleben den Christus so, wie er durch Erleben der äuße- ren Welt, wenn er nicht krankhaft atheistisch ist, den Vatergott findet."
      ],
      [
        "So kann ich nur ganz flüchtig, skizzenhaft andeuten, wie Anthroposophie durch wirkliche Forschung zu 133 dem Christus-Ereignis als zu einer objektiven Tatsache kommt.",
        "In allen möglichen Einzelheiten versucht An- throposophie das Christus-Ereignis hinzustellen als die wichtigste Tatsache des Erdenlebens der Menschheit, als dasjenige, was objektiv geschehen ist."
      ],
      [
        "Daher ist auch der ganze Geist, in dem das Christus-Ereignis in der An- throposophie dargestellt wird, so, daß dieses Ereignis einfach als Tatsache hingenommen werden kann.",
        "Und wir hatten gerade innerhalb der anthroposophischen Bewegung erlebt, daß zum Beispiel Bekenner des Juden- tums im echtesten, wahrsten und ehrlichsten Sinne sich fanden zur Anerkennung des Mysteriums von Golgatha."
      ],
      [
        "Damit aber, meine sehr verehrten Anwesenden, ist viel- leicht gerade durch die anthroposophische Bewegung schon das vorausgenommen, was überhaupt in der zu- künftigen Entwicklung der Menschheit eintreten muß: daß, indem man unmittelbar hinweist auf das, was ge- schaut werden kann im Mysterium von Golgatha, der Weg zum Christentum wiedergefunden werden kann.",
        "Es ist durchaus die Frage, ob es nicht doch eine tiefe Bedeutung hat, was in dem Buche von Friedrich Nietz- sches Freund Overbeck enthalten ist, daß ja die moderne Theologie gar nicht mehr christlich sei."
      ],
      [
        "Würde darin einige Berechtigung liegen, so dürfte man vielleicht doch mit einem gewissen Recht sagen: Anthroposophie ist geeignet, in lebendiger Weise den Menschen hinzufüh- ren zu dem Christus-Erlebnis.",
        "Sie stellt die Zeit, in welcher das Christus-Ereignis stattgefunden hat, so dar, daß von den alten instinktiven Anschauungen bei einzel- nen Menschen noch so viel vorhanden war, daß der geistige Untergrund, ich möchte sagen, die geistige Substanzialität des Mysteriums von Golgatha geschaut und in den ersten christlichen Jahrhunderten anerkannt 134 werden konnte."
      ],
      [
        "Wir sehen dann, wie das immer weniger und weniger wird, wir sehen es völlig verglimmen bei einer solchen Erscheinung wie Scotus Erigena, wir sehen immer mehr und mehr sich ausbilden die mittelalterliche Theologie, wo man versuchte, sich auseinanderzusetzen mit dem, was die moderne Menschheit ausbilden mußte, mit dem Intellekt, der, wenn er unmittelbar sich selbst überlassen ist und sich innerlich nicht weiter entwickelt, nicht herankommen kann an die übersinnlichen Welten.",
        "Sie spaltete dasjenige, was in die Menschenseele hinein- kommen wollte, gewissermaßen auf in das, was der Mensch durch den Intellekt erkennen kann, und in das Unerkennbare, zu dem der Mensch nicht selbst gelangen kann, sondern nur durch eine Offenbarung."
      ],
      [
        "Aus diesen Untergründen heraus kann man die ganze mittelalterliche Theologie begreifen, besonders die tho- mistische Theologie, die von dem Katholizismus als die allein maßgebende erachtet wurde.",
        "Davon wird heute manches gesagt werden können."
      ],
      [
        "Worum es der Anthro- posophie zu tun war und ist, das ist nichts anderes, als in einfacher und schlichter Weise auszusprechen, was für die geistige Anschauung da ist.",
        "Und wie Anthroposophie zu dem Satz kommt, der Atheismus ist eigentlich verborgene Krankheit, so kommt sie zu dem zweiten Satze: Den Christus nicht zu finden, zu dem Christus keine Beziehung zu finden, ist für den Menschen ein Schicksal, ein Schicksalsunglück!"
      ],
      [
        "Atheis- mus ist eine Krankheit, den Christus nicht zu finden ist ein Schicksalsunglück; denn man kann ihn finden im innerlichen Erleben.",
        "Dann aber stellt er sich dar als diejenige Wesenheit, die durch das Mysterium von Golgatha gegangen ist."
      ],
      [
        "Man kann durch innerliches Er- leben allein zu dem Christus kommen, man braucht 135 nicht anthroposophische Forschung, um ein religiöser Mensch im christlichen Sinne zu sein.",
        "Dann aber, wenn man zu dem Christus kommt, dann wird man ein Glied der geistigen Welt und man kann wirklich von einer Auferstehung der menschlichen Wesenheit in der geisti- gen Welt sprechen, von einer Erweiterung des Seelen- wesens in dem Erleben der geistigen Welt, und man kann davon sprechen, daß derjenige Mensch, der den Christus nicht findet, in einer gewissen Weise in bezug auf seine Weltanschauung beschränkt ist."
      ],
      [
        "Atheismus ist eine Krankheit!",
        "Nicht zum Christus kommen ist ein Schicksal, nicht zum Geiste kommen ist eine seelische Beschränktheit!",
        "Nun, meine sehr verehrten Anwesenden, Anthropo- sophie hat es aus solchen Untergründen heraus im Grunde genommen nur mit Religion zu tun, [nicht mit Theolo- gie], und mit Religion nur insofern, als die Menschen, die religiöse Bedürfnisse haben und diese in den gegenwär- tigen Bekenntnissen nicht befriedigen können, an die Anthroposophie herankommen."
      ],
      [
        "Anthroposophie will nur das tun, was innerhalb der heutigen Zeitbedürfnisse notwendig ist, und was die anderen nicht tun.",
        "Welche Gesinnung dem zugrunde liegt ich muß das immer wieder charakterisieren -, können Sie aus folgendem entnehmen."
      ],
      [
        "Schon vor vielen Jahren hielt ich einmal in einer süddeutschen Stadt - damals war sie eine deutsche Stadt, heute ist sie es nicht mehr - einen Vortrag über «Bibel und Weisheit».",
        "Bei diesem Vortrag waren auch zwei katholische Priester anwesend."
      ],
      [
        "Nach dem Vortrag ka- men die beiden zu mir und sagten: Wir haben eigentlich gar nichts in Ihrem Vortrage gefunden, was vom katho- lischen Standpunkte aus angefochten werden könnte. 136 Ich sagte: Wenn ich nur immer so glücklich sein könn- te! - Darauf sagten die beiden: Ja, aber eines ist uns aufgefallen; es ist nicht, was Sie sagen, sondern es ist die Art und Weise, wie Sie es vorbringen, und da müssen wir sagen: Sie reden zu Menschen, die in einer gewissen Beziehung vorbereitet sind.",
        "Sie reden zu einer Art von Gemeinde, welche eine bestimmte Bildung hat; wir aber reden für alle Menschen. - Ich sagte: Hochwürden, es kommt nicht darauf an, daß wir das nach unserem subjektiven Empfinden entscheiden, sondern darauf, daß wir uns als Menschen einleben mit unserer Arbeit in die Zeitenentwicklung, daß wir uns nicht einbilden, wir reden für alle Menschen, sondern daß wir uns eine sol- che Frage beantworten nach dem, was objektiv in der Menschheitsentwicklung lebt."
      ],
      [
        "So, wie ich mir einbilden kann, ich rede für alle Menschen und mich darin sehr irren kann -, so könnten Sie sich das einbilden.",
        "Für den Enthusiasmus ist es sehr gut, wenn man diese Einbildung hat.",
        "Aber fragen wir einmal: Kommen noch alle Men- schen, die heute ein Bedürfnis haben, über den Christus etwas zu hören, zu Ihnen in die Kirche? - Da konnten die beiden nicht Ja sagen, denn natürlich wußten Sie, daß eine Menge Menschen, die auch den Weg zum Christus suchten, nicht zu ihnen in die Kirche kamen."
      ],
      [
        "Da sagte ich: Sehen Sie, für die, die nicht zu Ihnen kommen, und doch den Weg zum Christus suchen, für diese rede ich. - Das heißt, sich seine Aufgaben aus der Zeitentwicklung heraus stellen, und nicht sich einbilden, man rede für alle Menschen, sondern sich zu fragen: Sind Gemüter da, die in einer besonderen Art dieses oder jenes entgegenneh- men wollen?",
        "Mit einer anderen Gesinnung wandte sich Anthropo- sophie auch niemals an irgendein religiöses Bekenntnis. 137 Wenn wir auch in der Waldorfschule dazu gelangt sind, gerade die Praxis unseres Unterrichtes aus der Anthropo- sophie heraus zu gestalten, so haben wir doch ganz davon abgesehen, aus der Waldorfschule eine solche Schule zu machen, durch die die Anthroposophie in die Gemüter der Kinder hineingepfropft würde."
      ],
      [
        "Mit Bezug auf den Religionsunterricht lassen wir die katholischen Kinder unterrichten von einem katholischen Pfarrer und die evangelischen von einem evangelischen Pfarrer.",
        "Nur für die Dissidentenkinder ist eine Art freier Religionsunter- richt eingerichtet worden, aber durchaus in christlichem Sinn."
      ],
      [
        "Da bringen wir aber nicht abstrakte Anthro-posophie vor auch keine konkrete Anthroposophie,wie sie an die Erwachsenen herangebracht werden kann -, sondern da versuchen wir mit aller Mühe, dasjenige an die Kinder heranzubringen, was ihrer realen Entwicklungsstufe entspricht; das muß aber alles nach Inhalt und Methode erst gesucht und gefunden werden.",
        "Durch den von uns eingerichteten freien Religionsunterricht haben wir er- reicht, daß nun auch diejenigen Kinder, die sonst gar keinen Religionsunterricht hätten, wieder an das Chri- stentum herangebracht werden, und sie kommen in Scharen, um an dieser Art des christlichen Religionsun- terrichtes teilzunehmen."
      ],
      [
        "Aber niemals haben wir eine irgendwie religiös geartete Propaganda getrieben inner- halb der anthroposophischen Bewegung und am wenig- sten wurde von der Anthroposophie aus irgend etwas un- ternommen gegen die einzelnen theologischen Systeme.",
        "Denn, was in dieser Beziehung der Anthroposophie allein obliegen kann, das ist, die einzelnen theologischen Systeme in ihrer Differenzierung begreiflich zu machen, und nicht, sie zu bekämpfen."
      ],
      [
        "Darin habe ich immer meine Aufgabe gesehen, wenn ich vor den Menschen 138 gesprochen habe, die zur Anthroposophie gekommen sind: begreiflich zu machen, warum der Katholizismus Katholizismus, der Protestantismus Protestantismus, das Judentum Judentum und der Buddhismus Buddhismus geworden ist, und wie in ihnen allen - ich glaube, das ist eine christliche Vorstellung - dasjenige Wesen lebt, das durch sein Schicksal der wirkliche Christ in seiner Seele zu erleben in der Lage ist.",
        "So hätte also gar nicht, wenn nicht von anderer Seite die Angriffe gekommen wären, ein Streit zu entstehen brauchen zwischen der Anthroposophie und der Theo- logie, und auch heute spreche ich diese Worte nur, weil das gewünscht wurde von denjenigen, die diesen heuti- gen Theologentag veranstalten."
      ],
      [
        "Was sich aber Anthro- posophie allein zur Aufgabe macht, ist die Verkündi- gung von anthroposophischen Forschungsergebnissen über die übersinnliche Welt.",
        "Deshalb war ich auch im- mer zurückhaltend besonders gegenüber den von theo- logischer Seite herrührenden Angriffen."
      ],
      [
        "Denn Anthropo- sophie will nicht als Kämpfer auf den Plan treten, son- dern sie will die von der Zeit geforderten berechtigten menschlichen Seelenbedürfnisse befriedigen.",
        "Und alle, die in diesem Sinne mit der Anthroposophie zusammen- wirken wollen zur Befriedigung dieser berechtigten, aus den Untergründen der Seele an die Oberfläche drängen- den menschlichen Seelenbedürfnisse, alle, die in diesem Sinne mit ihr arbeiten wollen, sind ihr willkommen! 139"
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SIEBENTER VORTRAG ANTHROPOSOPHIE UND SPRACHWISSENSCHAFT Berlin, 11. März 1922",
    "paragraphs": [
      "Sehr verehrte Anwesende! Die Veranstalter dieses Hochschulkurses haben gewünscht, daß ich an jedem Morgen durch einige Ausführungen die Betrachtungen des Tages einleite, und so muß es denn wohl auch sein, daß ich die heutige Tagesarbeit in einer gewissen aphori- stischen Weise durch eine Besprechung eröffne.",
      "Ich bin mir bewußt, daß dies gerade am heutigen Tage nicht ganz leicht ist. Bei einem kurzen Kurse, den ich einmal vor einem kleineren Kreise in Stuttgart über diejenigen Dinge hielt, die heute zur Sprache gebracht werden sol- len, war es mir ganz besonders klar geworden, wie man wirklich viel Zeit braucht, um diejenigen umstrittenen Dinge zu besprechen, die heute besprochen werden sol- len.",
      "So möchte ich denn nur einiges über den Geist der Betrachtung vorausschicken, der durch Anthroposophie gefordert ist in bezug auf die Anschauung der mensch- lichen Sprache. Wenn von der Sprache die Rede ist, und wenn man sich das Ziel setzt, die Sprache wissenschaftlich zu be- handeln, so muß man sich darüber klar sein, daß man es gegenüber der Sprache als Objekt einer wissenschaft- lichen Behandlung nicht so leicht hat wie zum Beispiel gegenüber der außer dem Menschen gelegenen Natur oder auch gegenüber der physischen Natur des Men- 140 sehen.",
      "In diesen Fällen hat man nämlich wenigstens ein für die Wahrnehmung klar umrissenes Objekt. Gewiß, man kann dann noch darüber diskutieren, inwiefern dem Objekt eine Wahrnehmung zugrundeliegt, oder inwiefern es bloß als Wirkung einer unbekannten Ursache vom menschlichen Erkenntnisvermögen erfaßt wird.",
      "Aber das sind dann Diskussionen, die rein innerhalb des Gedank- lichen verlaufen. Was der wissenschaftlichen Betrach- tung als Objekt vorliegt, ist ein abgeschlossener Gegen- stand, der eben gegeben ist.",
      "Das ist beim Sprachlichen durchaus nicht der Fall. Beim Sprachlichen liegt ein großer Teil dessen, was sich entfaltet, indem der Mensch spricht, schon in den unbe- wußten Regionen des menschlichen Seelenlebens.",
      "Es schlägt schon etwas herauf aus diesen unbewußten Re- gionen, und was da heraufschlägt, das wird dann verbun- den mit bewußten Elementen, die gewissermaßen wie die Oberwellen sich hinbewegen auf einem unbewußten oder unterbewußten Strom. Und das, was augenblicklich im Bewußtsein präsent ist, was gegenwärtig ist während wir sprechen, das ist eigentlich nur teilweise das für die Sprache im Wesentlichen in Betracht kommende Objekt, der eigentliche Gegenstand.",
      "Man kann, auch wenn man innerhalb der gegenwärtigen Sprachgewohnheiten des Menschenwesens stehen bleibt, sich schon eine gewisse Möglichkeit aneignen, die Sprache als Objekt in das Bewußtsein hereinzubringen, auch während man spricht. Ich möchte Ihnen dafür in bescheidener Weise ein Bei- spiel anführen, das dieses vielleicht veranschaulichen kann.",
      "Ich habe zu Weihnachten in Dornach am Goethe- anum einen Vortragszyklus zu halten gehabt über päd- agogisch-didaktische Gegenstände. Dieser Vortragszy- klus war zunächst dadurch veranlaßt, daß eine Reihe 141 englischer Lehrer und Lehrerinnen diesen Vortrags- zyklus, zu dem sie kommen wollten, verlangten.",
      "Als aber bekannt wurde, daß dieser Kursus stattfinden sollte, fanden sich dann aus allen Ländern des Westens und Mitteleuropas, namentlich aus der Schweiz auch, Leute zusammen, die nun ebenfalls diesen Vortragszyklus hören wollten. Weil nun dieser Kursus nicht in dem weit über 900 Personen fassenden großen Saal des Goetheanum gehalten werden konnte, sondern nur in einem kleinen Saal stattfinden konnte, war ich genötigt, die Vorträge jeweilig zweimal hintereinander zu halten.",
      "Nun glaubte ich schon von vornherein, daß es in einem gewissen Grade notwendig sei, die englisch sprechenden Menschen abzusondern von denjenigen, die anderen Nationalitäten angehören - nicht etwa aus politischen Gründen; der Vortragskursus - das bemerke ich ausdrücklich - war durchaus auch für die Engländer deutsch gesprochen; denn wenn die Leute etwas über Anthroposophie hören wollen, wo es auch immer ist, wird von mir immer deutsch zu ihnen gesprochen. Ich denke, das ist auch etwas, wodurch man seine «Deutschheit» dokumentie- ren kann, und wodurch dem deutschen Wesen und der deutschen Sprache gedient werden kann.",
      "Nun hatte ich in einem dieser Vorträge die ethische, die sittliche Erziehung zu erörtern. Ich versuchte im Laufe des Vortrages darzustellen, wie das Kind hinzu- führen ist zu denjenigen Stufen des inneren Erlebens, die eine gewisse ethisch-sittliche Verfassung in dem Kinde herbeiführen können. - Wenn ich heute wieder vor Persönlichkeiten sprechen würde, die in derselben Weise zuhören, wie manche gestern zugehört haben, so würde man wieder das, was ich aus unmittelbarem Erlebnis heraus spreche, konstruiert nennen können, wie das ge- 142 stern gegenüber dem geschehen ist, was ich über die Trinität gesagt habe.",
      "Allein, Dr. Rittelmeyer hat ja dar- auf so deutlich geantwortet mit dem Vergleich zwischen dem Kopf und dem Buch, wie ich es aus begreiflichen Gründen nicht habe tun wollen. Ich mußte also in diesem Vortrage über ethisch- sittliche Erziehung zeigen, wie das Kind geführt werden muß, damit bei ihm in der richtigen Weise entfacht werden: Dankbarkeitsgefühle, Interesse an der Welt, Liebe zu der Welt und zum eigenen Handeln und Tun; und ich mußte dann zeigen, wie durch Liebe zum eige- nen Handeln und Tun heranentwickelt wird das, was im Menschen als Pflicht gefühlt wird.",
      "Nun war es notwendig, diese Dreiheit aus dem unmittelbaren Leben heraus mit diesen drei Worten - wir reden ja heute von der Sprache - zu bezeichnen. Ich kam also von den ersten beiden Stufen - Dankbarkeit und Liebe - zu der dritten Stufe: Pflicht.",
      "Aber trotzdem ich den Vortrag zweimal zu halten hatte, einmal von 10 bis 11 Uhr für die englischen Zu- hörer, das zweite Mal von 11 bis 12 Uhr für die anderen Nationalitäten, die im wesentlichen in ihrer Gemüts- stimmung das Mitteleuropäische hatten, mußte ich nun tatsächlich diesen Vortrag, der eigentlich einfach ein Parallelvortrag sein sollte, an diesem Tage ganz anders für die Engländer halten als für die Deutschen, weil ich mich hineinzuleben versuchte in die Stimmung der Zu- hörer. Etwas ähnliches war zwar auch für die anderen Tage notwendig, aber an diesem Tage war es ganz be- sonders notwendig.",
      "Warum war das so? Ja, während ich in der Stunde von 11 bis 12 über Pflicht sprach vor Leuten, die durchaus aus dem Empfinden heraus zuhörten, aus dem die deutsche Sprache gebildet worden ist, hatte ich in der 143 ersten Stunde von 10 bis 11 vor Leuten zu sprechen, welche das, was ich über den Pflicht-Impuls zu sagen hatte, aus dem heraus empfanden, zu dem sie «duty» sagen.",
      "Nun ist es etwas ganz anderes, was jemand in der Seele hat, wenn er das Wort «Pflicht» ausspricht, oder wenn er das Wort «duty» ausspricht, und ich mußte einfach in den Vortrag von 11 bis 12 Uhr einfließen lassen diejenige Nuance des Erlebens, die sich ergibt, wenn man zu den Menschen von «Pflicht» spricht. Denn sagt man «Pflicht», so schlägt man mit diesem Worte einen Impuls an, der aus dem Gemütsleben kommt, der unmittelbar das Erleben hinüberführt zu etwas, das - wenn ich es als Verbum aussprechen will - mit «pflegen» zu tun hat, mit dem Hinausfließen des Gefühls von dem Tätigsein zu dem, worauf sich die Tätigkeit bezieht.",
      "Das liegt m dem Impulse, den man mit dem Worte «Pflicht» bezeichnet. Etwas ganz anderes lebt in der Seele, wenn man diesen Impuls mit dem Worte «duty» bezeichnet; denn ebenso, wie das Wort «Pflicht» auf das Gemüt hindeutet, so deutet das Wort «duty» auf den Intellekt, auf den Geist, auf das, was einen innerlich dirigiert, so wie einen der Gedanke dirigiert, wenn man zum Handeln übergeht.",
      "Man kann sagen: «Pflicht» wird erfüllt aus innerer Liebe und Hingebung, «duty» wird erfüllt aus dem Grunde, weil man, wenn man seine Menschenwürde fühlt, sich sagen muß: Du mußt einem dich durchdrin- genden Gesetz gehorchen, mußt dich hingeben einem Gesetz, das du intellektuell erfassest. Das ist nur annä- hernd charakterisiert.",
      "Aber ich will damit zum Ausdruck bringen, wie die innerlichen Erlebniskomplexe ganz an- dere sind bei dem einen und bei dem anderen Worte, trotzdem im Lexikon für das deutsche Wort «Pflicht» das englische Wort «duty» steht. Das aber überträgt sich 144 auf den ganzen Volksgeist, auf die ganze Volksseele, und in der Sprache haben Sie eine Nuance der ganzen Volksseele.",
      "Sie werden sehen, daß es in der Seele des Mitteleuropäers in dieser Beziehung ganz anders aussieht als in der Seele anderer Nationalitäten, und daß sich das Seelenleben ganz anders in der Sprache auslebt beim Mitteleuropäer als beim Engländer. Wer nun keinen Sinn dafür hat, daß das, was Sie aus den unterbewußten Tiefen der Seele m die Sprache hin- einnehmen, schon eine ganze Stufe tiefer liegt als das, was im Bewußtsein erlebt wird, der hat eigentlich nicht wirklich ein sauberes Objekt für die [wissenschaftliche Betrachtung der] Sprache.",
      "Man muß sich darüber klar sein: Bei der Naturbetrachtung sind die Objekte da, oder man stellt sie etwa durch äußere Hantierungen sich sauber her, wobei man aber wiederum die Objekte außerhalb von sich selbst hat und deshalb durchaus verfolgen kann. Betrachtet man die Sprache, so ist es notwendig, daß man zuerst einen Bewußtseinsprozeß durchmacht, um darauf zu kommen, was eigentlich das wirkliche Objekt ist, das man zu betrachten hat.",
      "So darf man, wenn es sich um die Sprache handelt, nicht bloß das betrachten, was im menschlichen Bewußtsein lebt, sondern man muß bei der Betrachtung der Sprache das ganze Lebendige im Auge haben, das sich im Sprechen und in der Sprache auslebt. Diese Vorbereitung für die wissenschaftliche Sprach- betrachtung wird im Grunde genommen ja sehr wenig gemacht.",
      "Würde sie gemacht, so würde man, wenn man, sagen wir Sprachgeschichte oder vergleichende Sprach- wissenschaft treibt, das tiefe Bedürfnis haben, überall erst den Gegenstand irgendeiner Sprache, den inneren unbewußten Inhalt, diese unterbewußte Substanz, die 145 im Sprechen nur zum Teil bewußt zum Ausdruck kommt, ins Auge zu fassen. Nun kommt dazu noch etwas anderes, nämlich daß bei den verschiedenen Stufen der Menschheitsentwick- lung dieser Grad der Bewußtheit, der mit der Sprache verbunden ist, eben ein ganz verschiedener war.",
      "Ein ganz anderer war er zum Beispiel in den Zeiten, in welchen die Quelle der Sanskritsprache liegt; ein anderer war er in der Zeit, in der die griechische Sprache gebildet worden ist, ein anderer ist er bei uns hier in Deutschland - aber hier werden die Nuancen immer kleiner und kleiner und unbemerkbarer - und ein anderer ist er zum Beispiel in England. Es sind schon große Verschieden- heiten im inneren Erleben bei der Handhabung der englischen Sprache durch einen Engländer oder durch einen Amerikaner, wenn ich nur die groben Unterschie- de hier ins Auge fasse.",
      "Wer aber auf das Dialekt-Studium eingehen kann, wer also zum Beispiel darauf eingeht, was die verschiedenen Dialekte der deutschen Sprache den Menschen erleben lassen, wenn sie gehandhabt wer- den, der merkt auch daran, was da alles an komplizierten Seelenimpulsen hineinläuft in das, was dann in der Sprache, im Sprachorganismus zum Ausdruck kommt. Es ist zum Beispiel durchaus nicht etwa grundlos, daß die Griechischsprechenden, wenn sie «Sprache» sagten, und wenn sie «Vernunft» sagten, im wesentlichen dasselbe empfanden und beides in einem Worte zusammenfaßten, weil das Erleben innerhalb des Wortes und das Erleben innerhalb des Gedankens, innerhalb der Vorstellung, bei der griechischen Handhabung der Sprache noch bis zu einem gewissen Grade unterschiedlos zusammenflössen, während unsere heutige Zeitepoche Unterschiedlichkeiten in dieser Beziehung zeigt.",
      "Der Grieche fühlte durchaus, 146 wenn er sprach, wie im Worte selbst hinrollte der Ge- danke. Für ihn war der Gedanke die «Seele» und das Wort, das hinströmte, war der «Leib», das äußere Kleid, sagen wir, der in den Gedanken hinströmenden Wort- seele.",
      "Wir fühlen heute, wenn wir uns den Prozeß klar zum Bewußtsein bringen, etwa so, wie wenn wir auf der einen Seite das Wort aussprechen würden - das Wort strömt dahin, indem wir es aussprechen -, und auf der anderen Seite der Gedanke gewissermaßen oben auf dem Strom der Worte schwimmt; er ist aber schon wieder deutlich unterscheidbar von dem Strom der Worte. Gehen wir zum Beispiel ins Sanskrit zurück, dann ist es nötig, erst wirkliche psychologische Prozesse durch- zumachen, psychische Vorgänge zu erleben, damit wir in die Lage kommen, wirklich innerlich dasjenige zu haben, was in der Zeit, da die Sanskritsprache ihre Quelle hatte, bei einem Worte erlebt wurde.",
      "Wir dürfen das Sanskrit durchaus nicht etwa mit denselben Gefühlen gegenüber dem Sprechen, gegenüber der Sprache betrachten, wie wir eine heutige Sprache betrachten. Nehmen wir zum Beispiel ein sehr bekanntes Wort: «manas».",
      "Sie werden, wenn Sie ein Lexikon aufschlagen, für «manas» die mannigfaltigsten Worte finden: Geist, Verstand, Gemüt, manchmal auch Zorn, Zornmütigkeit und so weiter. Im Grunde genommen kommt man durch solche Übersetzungen dem inneren Worterlebnis, das einmal da war und das in älteren Zeiten für die Menschen sehr deutlich innerlich erlebbar war, nicht nahe.",
      "Inner- halb derjenigen Zeitepoche, wo das Sanskrit in seiner vollen Lebendigkeit lebte, war überhaupt die mensch- liche Seelenverfassung noch anders als sie heute ist, und zwar wesentlich anders. Wir müssen uns darüber klar sein, daß in der Menschheitsentwicklung schon so etwas 147 vorhanden ist wie eine tiefgehende Umwandlung der Seelenverfassung des Menschen.",
      "Ich habe jene eine große Umwandlung hier wiederholt charakterisiert, die etwa in die Mitte des 15. Jahrhunderts gesetzt werden darf. Aber es gibt, indem man in der Menschheitsentwicklung her- aufsteigt, immer wieder solche Epochengrenzen, und nur wenn man in der Geschichte auch das innere seelische Leben des Menschen wirklich verfolgen kann, kommt man darauf, was da eigentlich vorhanden war, und woran das Spracherleben teilgenommen hat.",
      "Es war in der Zeit, in der so etwas wie das Wort «manas» noch lebendig innerlich ergriffen worden ist, durchaus etwas vorhanden, was ich nennen möchte das Erleben der Lautbedeutung. In einer ungeheuer intensiven Weise empfand man das, was innerlich erlebt wurde bei den Lauten, die wir heute als m, als a, als n und als s bezeichnen.",
      "Das Seelenleben ging noch bis zu einem hohen Grade wenn auch traumhaft, aber doch im Traume bewußt - mit dem mit, was innerlich im Orga- nismus lebte, während die Vokale und die Konsonanten ausgesprochen wurden. Wer dann mit einer solchen wissenschaftlichen Ausrüstung verfolgt, wie die Sprache im Menschen lebt, der findet, daß alles, was konsonan- tisch ist, darauf beruht, daß der Mensch sich mit seinem eigenen Wesen in äußere Vorgänge, in Dinghaftes, hin- einversetzt, und das innere Leben der Dinge mit sei- nen eigenen inneren, aber zurückgehaltenen Gebärden nachahmen will.",
      "Konsonanten sind zurückgehaltene Gebärden, nicht sichtbar werdende Gebärden, die aber in ihrem Inhalt durchaus dasjenige erfassen, was äußer- lich im Rollen des Donners, im Zucken des Blitzes, im Hinrollen des Windes und so weiter erlebt werden kann. Ein inneres Sichhineinversetzen in die äußeren Dinge ist 148 vorhanden, indem der Konsonant erlebt wird.",
      "Man will eigentlich, wenn ich mich so ausdrücken darf, durch Gebärden nachahmen, was äußerlich lebt und webt; man hält die Gebärde zurück, sie verwandelt sich im Innern und kommt in dieser Verwandlung im Konsonanten zum Vorschein. Dagegen lebt im Menschen, indem er sich der äuße- ren Natur entgegenstellt, eine Summe von Sympathien und Antipathien.",
      "Diese Sympathien und Antipathien, die ein inneres Erleben darstellen, gebären aus sich her- aus den gesamten Vokalismus; so daß der Mensch, indem er in der Sprache lebt, so lebt, daß er im konsonantischen Wesen die äußere Welt nachbildet, aber metamorpho- siert, daß er dagegen im Vokalischen sein eigenes inneres Verhältnis zur äußeren Welt darstellt. - Das ist etwas, was, wenn man auf die konkrete Tatsache des Sprach- erlebens eingeht, auch mit dem heutigen Seelenleben durchaus erfaßt, durchschaut werden kann. Es handelt sich bei dem, was als Imagination geschildert wird, nicht um irgendwelche Phantasien, sondern darum, daß zum Beispiel dieser innere Prozeß des Spracherlebens wirklich erschaut werden kann.",
      "Nun war aber in den älteren Zeiten, in denen das Sanskrit seine Quelle hat, noch etwas in der Menschen- seele lebendig wie eine traumhafte Imagination. Nicht ein solches scharf konturiertes Vorstellen, wie wir es heute haben, war damals dem Menschen eigen, sondern ein Leben in Bildern, in Imaginationen - allerdings nicht solche Imaginationen, wie wir sie heute in der Anthro- posophie meinen, die vollbewußt sind wie unsere scharf konturierten Begriffe, sondern traumhaft instinktive Imaginationen waren da.",
      "Aber diese traumhaften Ima- ginationen wirkten als Kraft. Gehen wir zurück bis zu 149 dem angedeuteten Zeiträume, so kann man sagen: Diese Imaginationen lebten als lebendige Kraft in dem Men- schen; er verspürte sie, wie er Hunger und Durst ver- spürte, nur in einem leiseren Sinne.",
      "Man malte innerlich in einer Art, die natürlich nicht ein Malen im heutigen Sinne ist, die sich aber so auslebte, daß man das Vokalische innerlich aufträgt, wie wir die Farben auf eine Fläche auftragen, und daß man dann ins Konsonantische mit diesem Vokalisieren sich hineinlebt, so wie wenn man, indem man die Farben nebeneinander setzt, die Grenzen und die Konturen hervorbringt. Es ist ein innerliches Nacherleben eines Imaginierens, das aber ein objektives Nacherleben der äußeren Natur darstellt.",
      "Es ist ein Er- leben der traumhaften Imaginationen. Man gibt sich diesen Imaginationen hin und stülpt die innerlich wirk- samen Imaginationen durch die Sprachorgane aus dem Organismus in die Worte. Nur auf diese Weise stellt man sich den innerlichen Vorgang des Spracherlebens so vor, wie er einmal in der Menschheitsentwicklung gelebt hat.",
      "Wenn man dann Ernst macht mit einer solchen Betrachtung, zum Beispiel mit dem Erleben des Lautes, den wir heute m nennen, so merkt man beim Erleben dieses Lautes, daß er einmal an der Grenze dessen stand, was Konsonant und Vokal ist. So wie wenn wir heute ein Bild malen und dann die Farben, die nun zu ihren inneren Grenzen ihre äußeren Grenzen haben, nicht weiter fortsetzen in die Fläche hinein, so wurde etwas ausgesprochen bei dem Worte «manas».",
      "Und beim a wurde etwas gefühlt wie mensch- liche Innerlichkeit. Und wenn ich das ganze Wort manas so umschreiben wollte, müßte ich sagen: In jenen alten Zeiten lebten die Menschen mit ihren traumhaften Ima- ginationen in der Sprache, so wie wir bewußt die Sprache 150 erleben.",
      "Wir leben heute mit Bezug auf die Sprache nicht mehr in Traumvorstellungen, sondern unser Bewußtsein liegt über der Sprache. Die alten traumhaften Imagina- tionen flössen fortwährend in die Sprache. Und so fühlte, wer das Wort «manas» aussprach, sich wie in einer Art von Schale drinnen; er fühlte seinen physischen Men- schenleib, namentlich insofern dieser flüssig-wässerig ist, wie in einer Art von Schale, und den übrigen Leib wie getragen von einer Art Luftkörper.",
      "Das alles wurde traumhaft erlebt, wenn in alten Zeiten das Wort «manas» ausgesprochen wurde. Man fühlte nicht so, wie wir uns heute im Seelenleben fühlen, sondern man fühlte sich als Träger des Seelenlebens - und das Seelenhafte selber erlebte man wie aus den außerirdischen und außer- menschlichen Kräften der Schale gegeben.",
      "Diese Empfindung muß man erst rege machen, wenn man einen älteren Wortinhalt verstehen will. Und man muß wissen, daß, wenn wir heute unser Ich empfinden, das innere Seelenerlebnis ein ganz anderes ist, als das war, was etwa bei dem Wort «ego» erlebt worden ist oder was von den Menschen früherer Zeiten bei dem Wort «aham» der Sanskritsprache erlebt worden ist.",
      "Wir erleben heute unser Ich als etwas, was ganz und gar wie in einem Punkte zusammengezogen ist, in einem Punkte, auf den wir als den Mittelpunkt unseres Innenwesens alle unsere Seelenkräfte beziehen. Diese Empfindung lag nicht den älteren Offenbarun- gen des Ich-Begriffes zugrunde.",
      "In diesen älteren Zeiten fühlte man auch das Ich noch als etwas, was getragen worden ist; man fühlte sich nicht im Ich drinnen. Man fühlte auch das Ich gewissermaßen wie auf den Wogen des seelischen Lebens wie etwas Selbständiges schwim- mend.",
      "Was man aber so fühlte, deutete man in dem 151 Lautzusammenhang nicht an; so daß eigentlich das, was in dem Sanskritwort «aham» liegt, etwas ist, was um das Ich herum ist, was das Ich trägt. Und während wir das Ich innerlich als einen Willensimpuls haben - denn so wird es heute wirklich erlebt -, der innerlich unser Wesen durchstrahlt, sagen wir als ein Mittelpunkt innerhalb einer Wärmequelle, die die Wärmestrahlen - um einen Vergleich zu gebrauchen - nach allen Seiten hinstrahlt, so fühlte der Grieche oder sogar noch der Lateiner das Ich wie eine Kugel von Wasser, und diese Wasserkugel ganz durchdrungen von Luft.",
      "Es ist etwas anderes, zu erleben die sich in einer Wasserkugel ausbreitende Luft, oder zu erleben das innerliche Strahlen eines Wärmemittelpunk- tes und Wärme nach allen Seiten der Kugel hinstrahlen, die dann - wenn wir den Vergleich ganz genau gebrauchen - als eine Luftkugel erfaßt werden muß. - Das alles sind Symbole. Aber die Worte der Sprache sind ja in diesem Sinne auch Symbole, und wer das Recht bestreitet, daß man die Worte als Symbole bezeichnet, der wird über- haupt nicht in eine solche Betrachtung einrücken können.",
      "So ist es notwendig, wenn man Sprachwissenschaft treiben will, daß man sich erst hineinlebt in das, was eigentlich Gegenstand der Sprachwissenschaft werden muß. Und da findet man eben, daß in älteren Zeiten die Sprache durchaus einen ganz anderen Charakter hatte als den, der etwa in den heutigen Zivilisationssprachen liegt; und man findet weiter, daß das Körperliche, das Leibli- che einen viel größeren Anteil hatte am Zustandekommen des Lautlichen, am Zustandekommen der Konfiguration eines Wortes.",
      "Der Mensch gab viel mehr sein Inneres [in die Sprache]. Daher auch haben Sie in dem Worte «manas» das m im Anfang, weil es den Menschen in sich abschließt, konturiert. 152 Wenn man Bezeichnungen in der Sanskritsprache vor sich hat, merkt man sehr bald, daß man darin das Erleben des Konsonantischen und des Vokalischen hat, man merkt, wie in der Tat ein innerliches Einleben in die äußeren Vorgänge und äußeren Dinghaftigkeiten da ist, und wie dadurch, daß im Konsonantischen nachgeahmt wird, im Vokalischen Sympathien und Antipathien empfunden werden, der Wortprozeß und der Sprach- prozeß Zustandekommen.",
      "Das ist in den alten Zeiten in einer viel körperlicheren Schattierung zustandegekom- men. Es war ein viel volleres Erleben in dem älteren Spracherleben. Das kann man heute noch erleben. Wenn Sie heute einen das Sanskrit oder überhaupt eine orienta- lische Zivilisationssprache sprechenden Menschen hö- ren, so hören Sie, wie das, was er ertönen läßt, aus seinem ganzen Menschen heraus, einschließlich aus der Leib- lichkeit, ertönt, und wie die Sprache musikalischen Charakter annimmt, weil sie aus einem solchen inneren Erleben kommt wie das Musikalische.",
      "Denn erst in einer späteren Phase der Menschheitsentwicklung hat sich in der Sprache das Musikalische abgetrennt von dem Logischen, also von dem Seelenleben m bloßen Vor- stellungen. Das kann man wiederum auch heute noch merken.",
      "Wenn Sie zum Beispiel vergleichen das innere Erleben in der deutschen und in der englischen Sprache, so ist es so, daß bei der englischen Sprache der Prozeß des In-ab- strakten-Vorstellungen-Lebens weiter fortgeschritten ist. Wenn wir heute in der deutschen Sprache leben wollen, müssen wir uns ja in diejenigen Formen der Sprache hineinleben, welche mit dem Neuhochdeutschen her- aufgekommen sind.",
      "Die Dialekte lassen unsere Seele durchaus noch untertauchen in ein viel intensiveres vitales 153 Erleben. Das eigentliche geistige Erleben der Sprache ist erst im Hochdeutschen möglich. Daher ist auch eine solche Gestalt wie Hegel, die ganz aus diesem Geiste herausgeboren ist, daß die Vorstellung gesondert für sich ist und doch wieder ganz gebunden an ein besonderes Element der Sprache erlebt wird, aus diesen Vorausset- zungen zustandegekommen und Hegel läßt sich deshalb in Wirklichkeit nicht in eine westliche Sprache überset- zen.",
      "Denn da erlebt man das Sprachliche noch unmit- telbar. Wenn Sie nach dem Westen gehen, merken Sie überall in dem Erleben, das die Seele entfaltet, wenn sie dem Sprachgebrauch hingegeben ist: Es erlebt zwar die Seele intensiv, es wird aber überall das Sprachliche herausge- worfen aus dem unmittelbaren Seelenerleben; es fließt der Strom der Sprache dahin, und fortwährend wird gewissermaßen aus dem fließenden Wasser etwas her- ausgebildet wie Eisschollen, die wie ein fester Inhalt auf den Wogen dahinrollen - zum Beispiel im Englischen.",
      "Wenn wir dagegen das Hochdeutsche sprechen, können wir merken, wie man in dem Strom der Sprache ebenfalls ein Flüssiges hat, aber es sind noch nicht Eisblöcke darin, die schon herausgefallen wären aus dem Sprach- lichen, das verbunden ist mit dem Geistig-Seelischen des Menschen. Kommt man nach Osten, so findet man diesen Pro- zeß auf einer noch weiter rückwärts liegenden Stufe.",
      "Da sieht man nun nicht Eisschollen, die herausgeworfen werden aus dem Strom der Sprache, und die nicht etwa fest verbunden mit ihm sind; da wird auch nicht wie im Hochdeutschen die vollständige Adäquatheit des Ge- dankens mit dem Wort erlebt, sondern es wird das Wort so erlebt, daß man es in seinem Organismus behält, 154 während wiederum der Gedanke etwas ist, dem die Worte entfließen, und dem man nachläuft, der eigentlich vor einem einhergeht. Das sind die Dinge, die man durchmachen muß, wenn man das Sprachliche wirklich erfassen will.",
      "Und man kann das nicht durchmachen, wenn man nicht we- nigstens bis zu einem gewissen Grade diejenige An- schauung aufnimmt, die Goethe für die Betrachtung der lebendigen Pflanzenwelt ausgebildet hat, und die, wenn sie in innerlichem Erleben und innerlichem Üben konse- quent verfolgt wird, zu dem imaginativen Vorstellen führt, das in der Anthroposophie gemeint ist. Über- haupt, wer die Sprache betrachten will, muß sie so be- trachten, daß er die innerliche Metamorphose des Sprach- organisierens erlebt, erlebt in ihrer Konkretheit; denn dann erst hat er das vor sich, was eigentlich der Sprach- prozeß ist.",
      "Solange man sich nicht aufschwingen kann zu einer solchen innerlichen Betrachtung der Sprache, so- lange betrachtet man eben die Sprache äußerlich, und man kann nicht bis zu dem eigentlichen lebendigen Objekt der Sprache vordringen. Daher ist alles mögliche an Sprachtheorien heraufgekommen.",
      "Das Denken über die Sprache ist ja in vieler Beziehung zu einem Denken über den Ursprung der Sprache geworden; eine ganze Anzahl von Theorien ist da heraufgekommen. Wilhelm Wundt hat sie in seiner Sprachtheorie aufgezählt und kritisch zerpflückt.",
      "Es ist damit ja so, wie man es heute auf vielen Gebie- ten erlebt, und wie man es gestern beobachten konnte. Wenn nämlich die Träger irgendeiner wissenschaftlichen Richtung sich heute zum vollen Nachdenken erheben und das betrachten, was ihnen die Wissenschaft, die sie vertreten, heute darbietet, dann fangen sie an vom 155 «Untergang» zu reden.",
      "Das ist eigentlich nicht das, was Ihnen die Anthroposophie sagen will. Im Grunde ge- nommen ist ja zum Beispiel gestern von der Anthropo- sophie aus sehr wenig von Untergang geredet worden; sehr wohl aber ist von denen, die heute in der Theologie drinnenstehen, von dem von ihnen erlebten Untergang gesprochen worden.",
      "Ähnlich spricht man auch, wenn man über die Spra- che philosophiert, von den untergehenden Theorien, zum Beispiel von der «Erfindungstheorie». Wundt zählt die verschiedenen Theorien auf. Nach der Erfindungstheo- rie ist die Sprache so entstanden, daß die Menschen gewissermaßen festgesetzt haben die Bezeichnungen für die Dinge; aber das findet der heutige Mensch nicht mehr angemessen, denn, so meint er, wie sollten die Stummen die Sprachformen haben festsetzen können, wenn auch noch so primitive?",
      "Als zweite zählt Wundt die «Wundertheorie» auf, die darauf ausgeht, daß die Sprache dem Menschen in einem gewissen Entwick- lungsstadium als ein Geschenk des Schöpfers gegeben worden ist. Aber das hat ja gestern schon Dr.",
      "Geyer ausgeführt, daß es heute für einen halbwegs anständigen Wissenschafter das nicht mehr gibt, an Wunder zu glauben; das ist verboten, und damit ist auch die Wun- dertheorie nicht mehr möglich. Dann wird als weitere die «Nachahmungstheorie» aufgezählt, die schon Ele- mente enthält, die eine partielle Berechtigung haben, weil das konsonantische Element der Sprache auf einem viel innerlicheren Prozeß beruht, als man sich gewöhn- lich vorstellt.",
      "Dann wird die «Naturlauttheorie» ange- führt; sie besagt, daß aus innerlichem Erleben heraus der Mensch in bezug auf die Sprache anstrebte, daß sich die Worte in lautlicher Beziehung decken sollten mit dem, 156 was man draußen in der Natur wahrnimmt und mit Sympathie oder Antipathie verfolgt. Diese Theorien könnten auch anders definiert werden.",
      "Aber es ist heute ja möglich, daß auch auf dem Boden derjenigen, die diese Theorien kritisieren, gezeigt wird, wie diese Theorien alle nicht das eigentliche Objekt der Sprache erfassen können. Sehr verehrte Anwesende, die Sache ist eben durch- aus so, daß Anthroposophie - auch wenn die Leute sagen, sie brauchten nicht auf sie zu warten - dennoch in einer gewissen Beziehung zeigen kann, was sie an Fruchtbarem zu geben in der Lage ist, wodurch - selbst auf solchem Gebiete, wie es die Sprachwissenschaft ist erst die sauberen, die reinlichen Objekte zu finden sind, an denen dann die Betrachtung angestellt werden kann.",
      "Man kann ja selbstverständlich über alles mögliche reden, auch über die Sprache, selbst wenn man sie als ein wirklich sauberes Objekt noch gar nicht hat. Aber Anthropo- sophie trägt eben in sich jenen tieferen Charakter der Wissenschaftlichkeit, der darauf ausgeht, zuerst ein- mal sich klar zu werden, welche Art von Wirklichkeit auf einem bestimmten Gebiete gefunden werden kann, so daß dann der Zusammenhang dessen, was wir als Wahrheit, als Erkenntnis von diesen Gebieten durch- dringen, mit diesem Wirklichkeitsgebiete auch tatsäch- lich innerlich erlebt werden kann.",
      "Und wenn, wie es gestern hier geschehen ist, dann mit Bezug auf das, was in so ehrlicher Arbeit, die nicht leichter ist als die in anderen Wissenschaften, gesagt wird, diese Anthroposo- phie stecke ihre Nase in alles mögliche hinein, so muß erwidert werden: Gewiß, es hat sich gezeigt, daß diese Anthroposophie im Laufe ihrer Entwicklung ihre Nase auch in alles hineinstecken mußte. Wenn es aber nicht 157 bei der Oberflächlichkeit bleibt, dieses Apercu zu prä- gen: «Die Anthroposophie steckt ihre Nase in alles mögliche hinein» -, sondern wenn man dazu fortschrei- ten möchte, dasjenige einmal wirklich ins Auge zu fassen und es ernsthaft zu studieren, was dabei herauskommt, wenn die Anthroposophie ihre Nase in alles steckt, dann erst, wenn man zu dieser zweiten Stufe des Verhältnisses zur Anthroposophie übergeht, wird sich zeigen, wie fruchtbar die Anthroposophie ist, und inwiefern sie ihre Berechtigung hat gegenüber dem ersten Urteil, das doch nur aus einer oberflächlichen Betrachtung hervorgeht! 158"
    ],
    "sentences": [
      [
        "Sehr verehrte Anwesende!",
        "Die Veranstalter dieses Hochschulkurses haben gewünscht, daß ich an jedem Morgen durch einige Ausführungen die Betrachtungen des Tages einleite, und so muß es denn wohl auch sein, daß ich die heutige Tagesarbeit in einer gewissen aphori- stischen Weise durch eine Besprechung eröffne."
      ],
      [
        "Ich bin mir bewußt, daß dies gerade am heutigen Tage nicht ganz leicht ist.",
        "Bei einem kurzen Kurse, den ich einmal vor einem kleineren Kreise in Stuttgart über diejenigen Dinge hielt, die heute zur Sprache gebracht werden sol- len, war es mir ganz besonders klar geworden, wie man wirklich viel Zeit braucht, um diejenigen umstrittenen Dinge zu besprechen, die heute besprochen werden sol- len."
      ],
      [
        "So möchte ich denn nur einiges über den Geist der Betrachtung vorausschicken, der durch Anthroposophie gefordert ist in bezug auf die Anschauung der mensch- lichen Sprache.",
        "Wenn von der Sprache die Rede ist, und wenn man sich das Ziel setzt, die Sprache wissenschaftlich zu be- handeln, so muß man sich darüber klar sein, daß man es gegenüber der Sprache als Objekt einer wissenschaft- lichen Behandlung nicht so leicht hat wie zum Beispiel gegenüber der außer dem Menschen gelegenen Natur oder auch gegenüber der physischen Natur des Men- 140 sehen."
      ],
      [
        "In diesen Fällen hat man nämlich wenigstens ein für die Wahrnehmung klar umrissenes Objekt.",
        "Gewiß, man kann dann noch darüber diskutieren, inwiefern dem Objekt eine Wahrnehmung zugrundeliegt, oder inwiefern es bloß als Wirkung einer unbekannten Ursache vom menschlichen Erkenntnisvermögen erfaßt wird."
      ],
      [
        "Aber das sind dann Diskussionen, die rein innerhalb des Gedank- lichen verlaufen.",
        "Was der wissenschaftlichen Betrach- tung als Objekt vorliegt, ist ein abgeschlossener Gegen- stand, der eben gegeben ist."
      ],
      [
        "Das ist beim Sprachlichen durchaus nicht der Fall.",
        "Beim Sprachlichen liegt ein großer Teil dessen, was sich entfaltet, indem der Mensch spricht, schon in den unbe- wußten Regionen des menschlichen Seelenlebens."
      ],
      [
        "Es schlägt schon etwas herauf aus diesen unbewußten Re- gionen, und was da heraufschlägt, das wird dann verbun- den mit bewußten Elementen, die gewissermaßen wie die Oberwellen sich hinbewegen auf einem unbewußten oder unterbewußten Strom.",
        "Und das, was augenblicklich im Bewußtsein präsent ist, was gegenwärtig ist während wir sprechen, das ist eigentlich nur teilweise das für die Sprache im Wesentlichen in Betracht kommende Objekt, der eigentliche Gegenstand."
      ],
      [
        "Man kann, auch wenn man innerhalb der gegenwärtigen Sprachgewohnheiten des Menschenwesens stehen bleibt, sich schon eine gewisse Möglichkeit aneignen, die Sprache als Objekt in das Bewußtsein hereinzubringen, auch während man spricht.",
        "Ich möchte Ihnen dafür in bescheidener Weise ein Bei- spiel anführen, das dieses vielleicht veranschaulichen kann."
      ],
      [
        "Ich habe zu Weihnachten in Dornach am Goethe- anum einen Vortragszyklus zu halten gehabt über päd- agogisch-didaktische Gegenstände.",
        "Dieser Vortragszy- klus war zunächst dadurch veranlaßt, daß eine Reihe 141 englischer Lehrer und Lehrerinnen diesen Vortrags- zyklus, zu dem sie kommen wollten, verlangten."
      ],
      [
        "Als aber bekannt wurde, daß dieser Kursus stattfinden sollte, fanden sich dann aus allen Ländern des Westens und Mitteleuropas, namentlich aus der Schweiz auch, Leute zusammen, die nun ebenfalls diesen Vortragszyklus hören wollten.",
        "Weil nun dieser Kursus nicht in dem weit über 900 Personen fassenden großen Saal des Goetheanum gehalten werden konnte, sondern nur in einem kleinen Saal stattfinden konnte, war ich genötigt, die Vorträge jeweilig zweimal hintereinander zu halten."
      ],
      [
        "Nun glaubte ich schon von vornherein, daß es in einem gewissen Grade notwendig sei, die englisch sprechenden Menschen abzusondern von denjenigen, die anderen Nationalitäten angehören - nicht etwa aus politischen Gründen; der Vortragskursus - das bemerke ich ausdrücklich - war durchaus auch für die Engländer deutsch gesprochen; denn wenn die Leute etwas über Anthroposophie hören wollen, wo es auch immer ist, wird von mir immer deutsch zu ihnen gesprochen.",
        "Ich denke, das ist auch etwas, wodurch man seine «Deutschheit» dokumentie- ren kann, und wodurch dem deutschen Wesen und der deutschen Sprache gedient werden kann."
      ],
      [
        "Nun hatte ich in einem dieser Vorträge die ethische, die sittliche Erziehung zu erörtern.",
        "Ich versuchte im Laufe des Vortrages darzustellen, wie das Kind hinzu- führen ist zu denjenigen Stufen des inneren Erlebens, die eine gewisse ethisch-sittliche Verfassung in dem Kinde herbeiführen können. - Wenn ich heute wieder vor Persönlichkeiten sprechen würde, die in derselben Weise zuhören, wie manche gestern zugehört haben, so würde man wieder das, was ich aus unmittelbarem Erlebnis heraus spreche, konstruiert nennen können, wie das ge- 142 stern gegenüber dem geschehen ist, was ich über die Trinität gesagt habe."
      ],
      [
        "Allein, Dr.",
        "Rittelmeyer hat ja dar- auf so deutlich geantwortet mit dem Vergleich zwischen dem Kopf und dem Buch, wie ich es aus begreiflichen Gründen nicht habe tun wollen.",
        "Ich mußte also in diesem Vortrage über ethisch- sittliche Erziehung zeigen, wie das Kind geführt werden muß, damit bei ihm in der richtigen Weise entfacht werden: Dankbarkeitsgefühle, Interesse an der Welt, Liebe zu der Welt und zum eigenen Handeln und Tun; und ich mußte dann zeigen, wie durch Liebe zum eige- nen Handeln und Tun heranentwickelt wird das, was im Menschen als Pflicht gefühlt wird."
      ],
      [
        "Nun war es notwendig, diese Dreiheit aus dem unmittelbaren Leben heraus mit diesen drei Worten - wir reden ja heute von der Sprache - zu bezeichnen.",
        "Ich kam also von den ersten beiden Stufen - Dankbarkeit und Liebe - zu der dritten Stufe: Pflicht."
      ],
      [
        "Aber trotzdem ich den Vortrag zweimal zu halten hatte, einmal von 10 bis 11 Uhr für die englischen Zu- hörer, das zweite Mal von 11 bis 12 Uhr für die anderen Nationalitäten, die im wesentlichen in ihrer Gemüts- stimmung das Mitteleuropäische hatten, mußte ich nun tatsächlich diesen Vortrag, der eigentlich einfach ein Parallelvortrag sein sollte, an diesem Tage ganz anders für die Engländer halten als für die Deutschen, weil ich mich hineinzuleben versuchte in die Stimmung der Zu- hörer.",
        "Etwas ähnliches war zwar auch für die anderen Tage notwendig, aber an diesem Tage war es ganz be- sonders notwendig."
      ],
      [
        "Warum war das so?",
        "Ja, während ich in der Stunde von 11 bis 12 über Pflicht sprach vor Leuten, die durchaus aus dem Empfinden heraus zuhörten, aus dem die deutsche Sprache gebildet worden ist, hatte ich in der 143 ersten Stunde von 10 bis 11 vor Leuten zu sprechen, welche das, was ich über den Pflicht-Impuls zu sagen hatte, aus dem heraus empfanden, zu dem sie «duty» sagen."
      ],
      [
        "Nun ist es etwas ganz anderes, was jemand in der Seele hat, wenn er das Wort «Pflicht» ausspricht, oder wenn er das Wort «duty» ausspricht, und ich mußte einfach in den Vortrag von 11 bis 12 Uhr einfließen lassen diejenige Nuance des Erlebens, die sich ergibt, wenn man zu den Menschen von «Pflicht» spricht.",
        "Denn sagt man «Pflicht», so schlägt man mit diesem Worte einen Impuls an, der aus dem Gemütsleben kommt, der unmittelbar das Erleben hinüberführt zu etwas, das - wenn ich es als Verbum aussprechen will - mit «pflegen» zu tun hat, mit dem Hinausfließen des Gefühls von dem Tätigsein zu dem, worauf sich die Tätigkeit bezieht."
      ],
      [
        "Das liegt m dem Impulse, den man mit dem Worte «Pflicht» bezeichnet.",
        "Etwas ganz anderes lebt in der Seele, wenn man diesen Impuls mit dem Worte «duty» bezeichnet; denn ebenso, wie das Wort «Pflicht» auf das Gemüt hindeutet, so deutet das Wort «duty» auf den Intellekt, auf den Geist, auf das, was einen innerlich dirigiert, so wie einen der Gedanke dirigiert, wenn man zum Handeln übergeht."
      ],
      [
        "Man kann sagen: «Pflicht» wird erfüllt aus innerer Liebe und Hingebung, «duty» wird erfüllt aus dem Grunde, weil man, wenn man seine Menschenwürde fühlt, sich sagen muß: Du mußt einem dich durchdrin- genden Gesetz gehorchen, mußt dich hingeben einem Gesetz, das du intellektuell erfassest.",
        "Das ist nur annä- hernd charakterisiert."
      ],
      [
        "Aber ich will damit zum Ausdruck bringen, wie die innerlichen Erlebniskomplexe ganz an- dere sind bei dem einen und bei dem anderen Worte, trotzdem im Lexikon für das deutsche Wort «Pflicht» das englische Wort «duty» steht.",
        "Das aber überträgt sich 144 auf den ganzen Volksgeist, auf die ganze Volksseele, und in der Sprache haben Sie eine Nuance der ganzen Volksseele."
      ],
      [
        "Sie werden sehen, daß es in der Seele des Mitteleuropäers in dieser Beziehung ganz anders aussieht als in der Seele anderer Nationalitäten, und daß sich das Seelenleben ganz anders in der Sprache auslebt beim Mitteleuropäer als beim Engländer.",
        "Wer nun keinen Sinn dafür hat, daß das, was Sie aus den unterbewußten Tiefen der Seele m die Sprache hin- einnehmen, schon eine ganze Stufe tiefer liegt als das, was im Bewußtsein erlebt wird, der hat eigentlich nicht wirklich ein sauberes Objekt für die [wissenschaftliche Betrachtung der] Sprache."
      ],
      [
        "Man muß sich darüber klar sein: Bei der Naturbetrachtung sind die Objekte da, oder man stellt sie etwa durch äußere Hantierungen sich sauber her, wobei man aber wiederum die Objekte außerhalb von sich selbst hat und deshalb durchaus verfolgen kann.",
        "Betrachtet man die Sprache, so ist es notwendig, daß man zuerst einen Bewußtseinsprozeß durchmacht, um darauf zu kommen, was eigentlich das wirkliche Objekt ist, das man zu betrachten hat."
      ],
      [
        "So darf man, wenn es sich um die Sprache handelt, nicht bloß das betrachten, was im menschlichen Bewußtsein lebt, sondern man muß bei der Betrachtung der Sprache das ganze Lebendige im Auge haben, das sich im Sprechen und in der Sprache auslebt.",
        "Diese Vorbereitung für die wissenschaftliche Sprach- betrachtung wird im Grunde genommen ja sehr wenig gemacht."
      ],
      [
        "Würde sie gemacht, so würde man, wenn man, sagen wir Sprachgeschichte oder vergleichende Sprach- wissenschaft treibt, das tiefe Bedürfnis haben, überall erst den Gegenstand irgendeiner Sprache, den inneren unbewußten Inhalt, diese unterbewußte Substanz, die 145 im Sprechen nur zum Teil bewußt zum Ausdruck kommt, ins Auge zu fassen.",
        "Nun kommt dazu noch etwas anderes, nämlich daß bei den verschiedenen Stufen der Menschheitsentwick- lung dieser Grad der Bewußtheit, der mit der Sprache verbunden ist, eben ein ganz verschiedener war."
      ],
      [
        "Ein ganz anderer war er zum Beispiel in den Zeiten, in welchen die Quelle der Sanskritsprache liegt; ein anderer war er in der Zeit, in der die griechische Sprache gebildet worden ist, ein anderer ist er bei uns hier in Deutschland - aber hier werden die Nuancen immer kleiner und kleiner und unbemerkbarer - und ein anderer ist er zum Beispiel in England.",
        "Es sind schon große Verschieden- heiten im inneren Erleben bei der Handhabung der englischen Sprache durch einen Engländer oder durch einen Amerikaner, wenn ich nur die groben Unterschie- de hier ins Auge fasse."
      ],
      [
        "Wer aber auf das Dialekt-Studium eingehen kann, wer also zum Beispiel darauf eingeht, was die verschiedenen Dialekte der deutschen Sprache den Menschen erleben lassen, wenn sie gehandhabt wer- den, der merkt auch daran, was da alles an komplizierten Seelenimpulsen hineinläuft in das, was dann in der Sprache, im Sprachorganismus zum Ausdruck kommt.",
        "Es ist zum Beispiel durchaus nicht etwa grundlos, daß die Griechischsprechenden, wenn sie «Sprache» sagten, und wenn sie «Vernunft» sagten, im wesentlichen dasselbe empfanden und beides in einem Worte zusammenfaßten, weil das Erleben innerhalb des Wortes und das Erleben innerhalb des Gedankens, innerhalb der Vorstellung, bei der griechischen Handhabung der Sprache noch bis zu einem gewissen Grade unterschiedlos zusammenflössen, während unsere heutige Zeitepoche Unterschiedlichkeiten in dieser Beziehung zeigt."
      ],
      [
        "Der Grieche fühlte durchaus, 146 wenn er sprach, wie im Worte selbst hinrollte der Ge- danke.",
        "Für ihn war der Gedanke die «Seele» und das Wort, das hinströmte, war der «Leib», das äußere Kleid, sagen wir, der in den Gedanken hinströmenden Wort- seele."
      ],
      [
        "Wir fühlen heute, wenn wir uns den Prozeß klar zum Bewußtsein bringen, etwa so, wie wenn wir auf der einen Seite das Wort aussprechen würden - das Wort strömt dahin, indem wir es aussprechen -, und auf der anderen Seite der Gedanke gewissermaßen oben auf dem Strom der Worte schwimmt; er ist aber schon wieder deutlich unterscheidbar von dem Strom der Worte.",
        "Gehen wir zum Beispiel ins Sanskrit zurück, dann ist es nötig, erst wirkliche psychologische Prozesse durch- zumachen, psychische Vorgänge zu erleben, damit wir in die Lage kommen, wirklich innerlich dasjenige zu haben, was in der Zeit, da die Sanskritsprache ihre Quelle hatte, bei einem Worte erlebt wurde."
      ],
      [
        "Wir dürfen das Sanskrit durchaus nicht etwa mit denselben Gefühlen gegenüber dem Sprechen, gegenüber der Sprache betrachten, wie wir eine heutige Sprache betrachten.",
        "Nehmen wir zum Beispiel ein sehr bekanntes Wort: «manas»."
      ],
      [
        "Sie werden, wenn Sie ein Lexikon aufschlagen, für «manas» die mannigfaltigsten Worte finden: Geist, Verstand, Gemüt, manchmal auch Zorn, Zornmütigkeit und so weiter.",
        "Im Grunde genommen kommt man durch solche Übersetzungen dem inneren Worterlebnis, das einmal da war und das in älteren Zeiten für die Menschen sehr deutlich innerlich erlebbar war, nicht nahe."
      ],
      [
        "Inner- halb derjenigen Zeitepoche, wo das Sanskrit in seiner vollen Lebendigkeit lebte, war überhaupt die mensch- liche Seelenverfassung noch anders als sie heute ist, und zwar wesentlich anders.",
        "Wir müssen uns darüber klar sein, daß in der Menschheitsentwicklung schon so etwas 147 vorhanden ist wie eine tiefgehende Umwandlung der Seelenverfassung des Menschen."
      ],
      [
        "Ich habe jene eine große Umwandlung hier wiederholt charakterisiert, die etwa in die Mitte des 15.",
        "Jahrhunderts gesetzt werden darf.",
        "Aber es gibt, indem man in der Menschheitsentwicklung her- aufsteigt, immer wieder solche Epochengrenzen, und nur wenn man in der Geschichte auch das innere seelische Leben des Menschen wirklich verfolgen kann, kommt man darauf, was da eigentlich vorhanden war, und woran das Spracherleben teilgenommen hat."
      ],
      [
        "Es war in der Zeit, in der so etwas wie das Wort «manas» noch lebendig innerlich ergriffen worden ist, durchaus etwas vorhanden, was ich nennen möchte das Erleben der Lautbedeutung.",
        "In einer ungeheuer intensiven Weise empfand man das, was innerlich erlebt wurde bei den Lauten, die wir heute als m, als a, als n und als s bezeichnen."
      ],
      [
        "Das Seelenleben ging noch bis zu einem hohen Grade wenn auch traumhaft, aber doch im Traume bewußt - mit dem mit, was innerlich im Orga- nismus lebte, während die Vokale und die Konsonanten ausgesprochen wurden.",
        "Wer dann mit einer solchen wissenschaftlichen Ausrüstung verfolgt, wie die Sprache im Menschen lebt, der findet, daß alles, was konsonan- tisch ist, darauf beruht, daß der Mensch sich mit seinem eigenen Wesen in äußere Vorgänge, in Dinghaftes, hin- einversetzt, und das innere Leben der Dinge mit sei- nen eigenen inneren, aber zurückgehaltenen Gebärden nachahmen will."
      ],
      [
        "Konsonanten sind zurückgehaltene Gebärden, nicht sichtbar werdende Gebärden, die aber in ihrem Inhalt durchaus dasjenige erfassen, was äußer- lich im Rollen des Donners, im Zucken des Blitzes, im Hinrollen des Windes und so weiter erlebt werden kann.",
        "Ein inneres Sichhineinversetzen in die äußeren Dinge ist 148 vorhanden, indem der Konsonant erlebt wird."
      ],
      [
        "Man will eigentlich, wenn ich mich so ausdrücken darf, durch Gebärden nachahmen, was äußerlich lebt und webt; man hält die Gebärde zurück, sie verwandelt sich im Innern und kommt in dieser Verwandlung im Konsonanten zum Vorschein.",
        "Dagegen lebt im Menschen, indem er sich der äuße- ren Natur entgegenstellt, eine Summe von Sympathien und Antipathien."
      ],
      [
        "Diese Sympathien und Antipathien, die ein inneres Erleben darstellen, gebären aus sich her- aus den gesamten Vokalismus; so daß der Mensch, indem er in der Sprache lebt, so lebt, daß er im konsonantischen Wesen die äußere Welt nachbildet, aber metamorpho- siert, daß er dagegen im Vokalischen sein eigenes inneres Verhältnis zur äußeren Welt darstellt. - Das ist etwas, was, wenn man auf die konkrete Tatsache des Sprach- erlebens eingeht, auch mit dem heutigen Seelenleben durchaus erfaßt, durchschaut werden kann.",
        "Es handelt sich bei dem, was als Imagination geschildert wird, nicht um irgendwelche Phantasien, sondern darum, daß zum Beispiel dieser innere Prozeß des Spracherlebens wirklich erschaut werden kann."
      ],
      [
        "Nun war aber in den älteren Zeiten, in denen das Sanskrit seine Quelle hat, noch etwas in der Menschen- seele lebendig wie eine traumhafte Imagination.",
        "Nicht ein solches scharf konturiertes Vorstellen, wie wir es heute haben, war damals dem Menschen eigen, sondern ein Leben in Bildern, in Imaginationen - allerdings nicht solche Imaginationen, wie wir sie heute in der Anthro- posophie meinen, die vollbewußt sind wie unsere scharf konturierten Begriffe, sondern traumhaft instinktive Imaginationen waren da."
      ],
      [
        "Aber diese traumhaften Ima- ginationen wirkten als Kraft.",
        "Gehen wir zurück bis zu 149 dem angedeuteten Zeiträume, so kann man sagen: Diese Imaginationen lebten als lebendige Kraft in dem Men- schen; er verspürte sie, wie er Hunger und Durst ver- spürte, nur in einem leiseren Sinne."
      ],
      [
        "Man malte innerlich in einer Art, die natürlich nicht ein Malen im heutigen Sinne ist, die sich aber so auslebte, daß man das Vokalische innerlich aufträgt, wie wir die Farben auf eine Fläche auftragen, und daß man dann ins Konsonantische mit diesem Vokalisieren sich hineinlebt, so wie wenn man, indem man die Farben nebeneinander setzt, die Grenzen und die Konturen hervorbringt.",
        "Es ist ein innerliches Nacherleben eines Imaginierens, das aber ein objektives Nacherleben der äußeren Natur darstellt."
      ],
      [
        "Es ist ein Er- leben der traumhaften Imaginationen.",
        "Man gibt sich diesen Imaginationen hin und stülpt die innerlich wirk- samen Imaginationen durch die Sprachorgane aus dem Organismus in die Worte.",
        "Nur auf diese Weise stellt man sich den innerlichen Vorgang des Spracherlebens so vor, wie er einmal in der Menschheitsentwicklung gelebt hat."
      ],
      [
        "Wenn man dann Ernst macht mit einer solchen Betrachtung, zum Beispiel mit dem Erleben des Lautes, den wir heute m nennen, so merkt man beim Erleben dieses Lautes, daß er einmal an der Grenze dessen stand, was Konsonant und Vokal ist.",
        "So wie wenn wir heute ein Bild malen und dann die Farben, die nun zu ihren inneren Grenzen ihre äußeren Grenzen haben, nicht weiter fortsetzen in die Fläche hinein, so wurde etwas ausgesprochen bei dem Worte «manas»."
      ],
      [
        "Und beim a wurde etwas gefühlt wie mensch- liche Innerlichkeit.",
        "Und wenn ich das ganze Wort manas so umschreiben wollte, müßte ich sagen: In jenen alten Zeiten lebten die Menschen mit ihren traumhaften Ima- ginationen in der Sprache, so wie wir bewußt die Sprache 150 erleben."
      ],
      [
        "Wir leben heute mit Bezug auf die Sprache nicht mehr in Traumvorstellungen, sondern unser Bewußtsein liegt über der Sprache.",
        "Die alten traumhaften Imagina- tionen flössen fortwährend in die Sprache.",
        "Und so fühlte, wer das Wort «manas» aussprach, sich wie in einer Art von Schale drinnen; er fühlte seinen physischen Men- schenleib, namentlich insofern dieser flüssig-wässerig ist, wie in einer Art von Schale, und den übrigen Leib wie getragen von einer Art Luftkörper."
      ],
      [
        "Das alles wurde traumhaft erlebt, wenn in alten Zeiten das Wort «manas» ausgesprochen wurde.",
        "Man fühlte nicht so, wie wir uns heute im Seelenleben fühlen, sondern man fühlte sich als Träger des Seelenlebens - und das Seelenhafte selber erlebte man wie aus den außerirdischen und außer- menschlichen Kräften der Schale gegeben."
      ],
      [
        "Diese Empfindung muß man erst rege machen, wenn man einen älteren Wortinhalt verstehen will.",
        "Und man muß wissen, daß, wenn wir heute unser Ich empfinden, das innere Seelenerlebnis ein ganz anderes ist, als das war, was etwa bei dem Wort «ego» erlebt worden ist oder was von den Menschen früherer Zeiten bei dem Wort «aham» der Sanskritsprache erlebt worden ist."
      ],
      [
        "Wir erleben heute unser Ich als etwas, was ganz und gar wie in einem Punkte zusammengezogen ist, in einem Punkte, auf den wir als den Mittelpunkt unseres Innenwesens alle unsere Seelenkräfte beziehen.",
        "Diese Empfindung lag nicht den älteren Offenbarun- gen des Ich-Begriffes zugrunde."
      ],
      [
        "In diesen älteren Zeiten fühlte man auch das Ich noch als etwas, was getragen worden ist; man fühlte sich nicht im Ich drinnen.",
        "Man fühlte auch das Ich gewissermaßen wie auf den Wogen des seelischen Lebens wie etwas Selbständiges schwim- mend."
      ],
      [
        "Was man aber so fühlte, deutete man in dem 151 Lautzusammenhang nicht an; so daß eigentlich das, was in dem Sanskritwort «aham» liegt, etwas ist, was um das Ich herum ist, was das Ich trägt.",
        "Und während wir das Ich innerlich als einen Willensimpuls haben - denn so wird es heute wirklich erlebt -, der innerlich unser Wesen durchstrahlt, sagen wir als ein Mittelpunkt innerhalb einer Wärmequelle, die die Wärmestrahlen - um einen Vergleich zu gebrauchen - nach allen Seiten hinstrahlt, so fühlte der Grieche oder sogar noch der Lateiner das Ich wie eine Kugel von Wasser, und diese Wasserkugel ganz durchdrungen von Luft."
      ],
      [
        "Es ist etwas anderes, zu erleben die sich in einer Wasserkugel ausbreitende Luft, oder zu erleben das innerliche Strahlen eines Wärmemittelpunk- tes und Wärme nach allen Seiten der Kugel hinstrahlen, die dann - wenn wir den Vergleich ganz genau gebrauchen - als eine Luftkugel erfaßt werden muß. - Das alles sind Symbole.",
        "Aber die Worte der Sprache sind ja in diesem Sinne auch Symbole, und wer das Recht bestreitet, daß man die Worte als Symbole bezeichnet, der wird über- haupt nicht in eine solche Betrachtung einrücken können."
      ],
      [
        "So ist es notwendig, wenn man Sprachwissenschaft treiben will, daß man sich erst hineinlebt in das, was eigentlich Gegenstand der Sprachwissenschaft werden muß.",
        "Und da findet man eben, daß in älteren Zeiten die Sprache durchaus einen ganz anderen Charakter hatte als den, der etwa in den heutigen Zivilisationssprachen liegt; und man findet weiter, daß das Körperliche, das Leibli- che einen viel größeren Anteil hatte am Zustandekommen des Lautlichen, am Zustandekommen der Konfiguration eines Wortes."
      ],
      [
        "Der Mensch gab viel mehr sein Inneres [in die Sprache].",
        "Daher auch haben Sie in dem Worte «manas» das m im Anfang, weil es den Menschen in sich abschließt, konturiert. 152 Wenn man Bezeichnungen in der Sanskritsprache vor sich hat, merkt man sehr bald, daß man darin das Erleben des Konsonantischen und des Vokalischen hat, man merkt, wie in der Tat ein innerliches Einleben in die äußeren Vorgänge und äußeren Dinghaftigkeiten da ist, und wie dadurch, daß im Konsonantischen nachgeahmt wird, im Vokalischen Sympathien und Antipathien empfunden werden, der Wortprozeß und der Sprach- prozeß Zustandekommen."
      ],
      [
        "Das ist in den alten Zeiten in einer viel körperlicheren Schattierung zustandegekom- men.",
        "Es war ein viel volleres Erleben in dem älteren Spracherleben.",
        "Das kann man heute noch erleben.",
        "Wenn Sie heute einen das Sanskrit oder überhaupt eine orienta- lische Zivilisationssprache sprechenden Menschen hö- ren, so hören Sie, wie das, was er ertönen läßt, aus seinem ganzen Menschen heraus, einschließlich aus der Leib- lichkeit, ertönt, und wie die Sprache musikalischen Charakter annimmt, weil sie aus einem solchen inneren Erleben kommt wie das Musikalische."
      ],
      [
        "Denn erst in einer späteren Phase der Menschheitsentwicklung hat sich in der Sprache das Musikalische abgetrennt von dem Logischen, also von dem Seelenleben m bloßen Vor- stellungen.",
        "Das kann man wiederum auch heute noch merken."
      ],
      [
        "Wenn Sie zum Beispiel vergleichen das innere Erleben in der deutschen und in der englischen Sprache, so ist es so, daß bei der englischen Sprache der Prozeß des In-ab- strakten-Vorstellungen-Lebens weiter fortgeschritten ist.",
        "Wenn wir heute in der deutschen Sprache leben wollen, müssen wir uns ja in diejenigen Formen der Sprache hineinleben, welche mit dem Neuhochdeutschen her- aufgekommen sind."
      ],
      [
        "Die Dialekte lassen unsere Seele durchaus noch untertauchen in ein viel intensiveres vitales 153 Erleben.",
        "Das eigentliche geistige Erleben der Sprache ist erst im Hochdeutschen möglich.",
        "Daher ist auch eine solche Gestalt wie Hegel, die ganz aus diesem Geiste herausgeboren ist, daß die Vorstellung gesondert für sich ist und doch wieder ganz gebunden an ein besonderes Element der Sprache erlebt wird, aus diesen Vorausset- zungen zustandegekommen und Hegel läßt sich deshalb in Wirklichkeit nicht in eine westliche Sprache überset- zen."
      ],
      [
        "Denn da erlebt man das Sprachliche noch unmit- telbar.",
        "Wenn Sie nach dem Westen gehen, merken Sie überall in dem Erleben, das die Seele entfaltet, wenn sie dem Sprachgebrauch hingegeben ist: Es erlebt zwar die Seele intensiv, es wird aber überall das Sprachliche herausge- worfen aus dem unmittelbaren Seelenerleben; es fließt der Strom der Sprache dahin, und fortwährend wird gewissermaßen aus dem fließenden Wasser etwas her- ausgebildet wie Eisschollen, die wie ein fester Inhalt auf den Wogen dahinrollen - zum Beispiel im Englischen."
      ],
      [
        "Wenn wir dagegen das Hochdeutsche sprechen, können wir merken, wie man in dem Strom der Sprache ebenfalls ein Flüssiges hat, aber es sind noch nicht Eisblöcke darin, die schon herausgefallen wären aus dem Sprach- lichen, das verbunden ist mit dem Geistig-Seelischen des Menschen.",
        "Kommt man nach Osten, so findet man diesen Pro- zeß auf einer noch weiter rückwärts liegenden Stufe."
      ],
      [
        "Da sieht man nun nicht Eisschollen, die herausgeworfen werden aus dem Strom der Sprache, und die nicht etwa fest verbunden mit ihm sind; da wird auch nicht wie im Hochdeutschen die vollständige Adäquatheit des Ge- dankens mit dem Wort erlebt, sondern es wird das Wort so erlebt, daß man es in seinem Organismus behält, 154 während wiederum der Gedanke etwas ist, dem die Worte entfließen, und dem man nachläuft, der eigentlich vor einem einhergeht.",
        "Das sind die Dinge, die man durchmachen muß, wenn man das Sprachliche wirklich erfassen will."
      ],
      [
        "Und man kann das nicht durchmachen, wenn man nicht we- nigstens bis zu einem gewissen Grade diejenige An- schauung aufnimmt, die Goethe für die Betrachtung der lebendigen Pflanzenwelt ausgebildet hat, und die, wenn sie in innerlichem Erleben und innerlichem Üben konse- quent verfolgt wird, zu dem imaginativen Vorstellen führt, das in der Anthroposophie gemeint ist.",
        "Über- haupt, wer die Sprache betrachten will, muß sie so be- trachten, daß er die innerliche Metamorphose des Sprach- organisierens erlebt, erlebt in ihrer Konkretheit; denn dann erst hat er das vor sich, was eigentlich der Sprach- prozeß ist."
      ],
      [
        "Solange man sich nicht aufschwingen kann zu einer solchen innerlichen Betrachtung der Sprache, so- lange betrachtet man eben die Sprache äußerlich, und man kann nicht bis zu dem eigentlichen lebendigen Objekt der Sprache vordringen.",
        "Daher ist alles mögliche an Sprachtheorien heraufgekommen."
      ],
      [
        "Das Denken über die Sprache ist ja in vieler Beziehung zu einem Denken über den Ursprung der Sprache geworden; eine ganze Anzahl von Theorien ist da heraufgekommen.",
        "Wilhelm Wundt hat sie in seiner Sprachtheorie aufgezählt und kritisch zerpflückt."
      ],
      [
        "Es ist damit ja so, wie man es heute auf vielen Gebie- ten erlebt, und wie man es gestern beobachten konnte.",
        "Wenn nämlich die Träger irgendeiner wissenschaftlichen Richtung sich heute zum vollen Nachdenken erheben und das betrachten, was ihnen die Wissenschaft, die sie vertreten, heute darbietet, dann fangen sie an vom 155 «Untergang» zu reden."
      ],
      [
        "Das ist eigentlich nicht das, was Ihnen die Anthroposophie sagen will.",
        "Im Grunde ge- nommen ist ja zum Beispiel gestern von der Anthropo- sophie aus sehr wenig von Untergang geredet worden; sehr wohl aber ist von denen, die heute in der Theologie drinnenstehen, von dem von ihnen erlebten Untergang gesprochen worden."
      ],
      [
        "Ähnlich spricht man auch, wenn man über die Spra- che philosophiert, von den untergehenden Theorien, zum Beispiel von der «Erfindungstheorie».",
        "Wundt zählt die verschiedenen Theorien auf.",
        "Nach der Erfindungstheo- rie ist die Sprache so entstanden, daß die Menschen gewissermaßen festgesetzt haben die Bezeichnungen für die Dinge; aber das findet der heutige Mensch nicht mehr angemessen, denn, so meint er, wie sollten die Stummen die Sprachformen haben festsetzen können, wenn auch noch so primitive?"
      ],
      [
        "Als zweite zählt Wundt die «Wundertheorie» auf, die darauf ausgeht, daß die Sprache dem Menschen in einem gewissen Entwick- lungsstadium als ein Geschenk des Schöpfers gegeben worden ist.",
        "Aber das hat ja gestern schon Dr."
      ],
      [
        "Geyer ausgeführt, daß es heute für einen halbwegs anständigen Wissenschafter das nicht mehr gibt, an Wunder zu glauben; das ist verboten, und damit ist auch die Wun- dertheorie nicht mehr möglich.",
        "Dann wird als weitere die «Nachahmungstheorie» aufgezählt, die schon Ele- mente enthält, die eine partielle Berechtigung haben, weil das konsonantische Element der Sprache auf einem viel innerlicheren Prozeß beruht, als man sich gewöhn- lich vorstellt."
      ],
      [
        "Dann wird die «Naturlauttheorie» ange- führt; sie besagt, daß aus innerlichem Erleben heraus der Mensch in bezug auf die Sprache anstrebte, daß sich die Worte in lautlicher Beziehung decken sollten mit dem, 156 was man draußen in der Natur wahrnimmt und mit Sympathie oder Antipathie verfolgt.",
        "Diese Theorien könnten auch anders definiert werden."
      ],
      [
        "Aber es ist heute ja möglich, daß auch auf dem Boden derjenigen, die diese Theorien kritisieren, gezeigt wird, wie diese Theorien alle nicht das eigentliche Objekt der Sprache erfassen können.",
        "Sehr verehrte Anwesende, die Sache ist eben durch- aus so, daß Anthroposophie - auch wenn die Leute sagen, sie brauchten nicht auf sie zu warten - dennoch in einer gewissen Beziehung zeigen kann, was sie an Fruchtbarem zu geben in der Lage ist, wodurch - selbst auf solchem Gebiete, wie es die Sprachwissenschaft ist erst die sauberen, die reinlichen Objekte zu finden sind, an denen dann die Betrachtung angestellt werden kann."
      ],
      [
        "Man kann ja selbstverständlich über alles mögliche reden, auch über die Sprache, selbst wenn man sie als ein wirklich sauberes Objekt noch gar nicht hat.",
        "Aber Anthropo- sophie trägt eben in sich jenen tieferen Charakter der Wissenschaftlichkeit, der darauf ausgeht, zuerst ein- mal sich klar zu werden, welche Art von Wirklichkeit auf einem bestimmten Gebiete gefunden werden kann, so daß dann der Zusammenhang dessen, was wir als Wahrheit, als Erkenntnis von diesen Gebieten durch- dringen, mit diesem Wirklichkeitsgebiete auch tatsäch- lich innerlich erlebt werden kann."
      ],
      [
        "Und wenn, wie es gestern hier geschehen ist, dann mit Bezug auf das, was in so ehrlicher Arbeit, die nicht leichter ist als die in anderen Wissenschaften, gesagt wird, diese Anthroposo- phie stecke ihre Nase in alles mögliche hinein, so muß erwidert werden: Gewiß, es hat sich gezeigt, daß diese Anthroposophie im Laufe ihrer Entwicklung ihre Nase auch in alles hineinstecken mußte.",
        "Wenn es aber nicht 157 bei der Oberflächlichkeit bleibt, dieses Apercu zu prä- gen: «Die Anthroposophie steckt ihre Nase in alles mögliche hinein» -, sondern wenn man dazu fortschrei- ten möchte, dasjenige einmal wirklich ins Auge zu fassen und es ernsthaft zu studieren, was dabei herauskommt, wenn die Anthroposophie ihre Nase in alles steckt, dann erst, wenn man zu dieser zweiten Stufe des Verhältnisses zur Anthroposophie übergeht, wird sich zeigen, wie fruchtbar die Anthroposophie ist, und inwiefern sie ihre Berechtigung hat gegenüber dem ersten Urteil, das doch nur aus einer oberflächlichen Betrachtung hervorgeht! 158"
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "BERICHT über den anthroposophischen Hochschulkurs in Berlin Aus dem Mitgliedervortrag in Dornach, 18. März 1922",
    "paragraphs": [
      "Meine lieben Freunde! Gestatten Sie, daß ich heute eini- ges über den Verlauf des Berliner Hochschulkurses sage. Der Berliner Hochschulkurs hatte sein Programm in einer besonderen Weise angeordnet. Es sollten darge- stellt werden die Beziehungen gewisser Lebens- und Wissenschaftszweige in der Gegenwart zur anthroposo- phischen Weltanschauung.",
      "Der einzelne Tag sollte im- mer einem besonderen Wissenschafts- oder Lebenszwei- ge in der Hauptsache gewidmet sein. Und die Woche war so eingeteilt, daß begonnen wurde mit dem Sonntag, der der anorganischen Naturwissenschaft gewidmet sein sollte.",
      "Der Montag sollte dann gewidmet sein der organi- schen Naturwissenschaft und der Medizin, der Dienstag der Philosophie, der Mittwoch der Erziehungswissen- schaft, der Donnerstag der Volkswirtschaft und der Freitag der Theologie. Der Sonnabend sollte der Sprach- wissenschaft gewidmet sein, und dann sollte am Sonntag das Ganze durch die Eurythmievorstellung im Deut- schen Theater einen gewissen Abschluß erlangen.",
      "Es war das Programm so gedacht, daß jeder Tag mit einem kurzen Vortrag von mir beginnen sollte. Nur der erste Sonntag konnte nicht so beginnen, da ich damals noch nicht in Berlin sein konnte. So mußte ich am Montag in meinen einführenden Worten sowohl die anorganische wie die organische Naturwissenschaft zu- 159 sammenfassen.",
      "Dann sollte der Tag also einen einheitli- chen Charakter tragen. Es fanden anschließend an meine Einführungsworte dann zwei weitere Vorträge am Vor- mittag statt. Dann fand eine halbstündige Imbißpause statt, zu der man aber - das war schon angekündigt - in den Räumen der Singakademie keinen Imbiß bekam.",
      "Und von l bis 2 Uhr sollte dann eine Diskussion stattfin- den. Daran sollte sich dann der letzte Vortrag des Vor- mittags anschließen von 2 bis 3 Uhr. Es war ein etwas anstrengendes Programm. Am Abend schlössen sich daran Vorträge, die zum Teil m der Philharmonie von mir gehalten wurden, zum Teil von anderen in den Räumen der Berliner Universität; jeden Abend einen Vortrag und bei den ändern Vorträgen, außer meinem, war immer noch nach diesen Vorträgen abends auch eine Art von Aussprache.",
      "Es waren die Tage also außeror- dentlich reichlich besetzt. Nun, die ganze Gliederung des Programmes darf tatsächlich interessant genannt werden, namentlich durch die Formulierungen, welche die einzelnen Tagespro- gramme erfahren hatten.",
      "Gewissermaßen hatte jeder Tag einen Gesamttitel, und die Formulierungen dieser Ge- samttitel für die Tage sind nun wirklich interessant, denn sie verraten so manches Bedeutungsvolle: Jeder einzelne Tag hatte nämlich in seiner Formulierung etwas Positi- ves, nur der Freitag nicht, der der Theologie gewidmet war. Das ist schon bedeutsam, nicht so sehr aus dem Zeitbewußtsein heraus, sondern aus der Art und Weise, wie man sich zu der Entwicklung des Anthroposophi- schen auf Seiten derjenigen stellte, die das Programm formuliert haben.",
      "Man fühlte sich einfach gedrängt, die anderen Tagesprogramme in positivem Sinne zu for- mulieren, und wir brauchen uns nur diese Formulierun- 160 gen anzuschauen, um das Bedeutungsvolle herauszu- finden. Sonntag, den 5.",
      "März: «Von lebensfeindlicher Me- chanistik zu wahrer Phänomenologie». Es wird also die Hoffnung ausgesprochen in der Formulierung des Pro- grammes, daß man durch Anthroposophie dazu kommen wird, eine Phänomenologie als Grundlage der Natur- wissenschaft, der anorganischen Naturwissenschaft zu finden.",
      "Noch positiver ist dann das Programm vom Montag zusammengefaßt: «Wege anthroposophischer Menschen- erkenntnis in Biologie und Medizin», und ebenso positiv das Programm vom Dienstag über Philosophie: «Die Begründung der Anthroposophie aus dem philosophi- schen Bewußtsem der Gegenwart.» Ebenso positiv das Programm vom Mittwoch: «Von modernen pädagogischen Forderungen zu ihrer Ver- wirklichung durch Anthroposophie» - also auch hier der Gedanke: Es bestehen solche pädagogischen Forderun- gen in der Gegenwart, die durch Anthroposophie ver- wirklicht werden können. Der Donnerstag, der der Sozialwissenschaft gewid- met war, hatte ja sogar einen sehr verheißungsvollen Titel in der Gesamtformulierung des Programmes, ob- wohl das, was dann gehalten worden ist, weniger verhei- ßungsvoll war.",
      "Der Donnerstag trug sogar den außeror- dentlich verheißungsvollen Titel, der sehr positiv klingt: «Nationalökonomische Ausblicke». Der Sonnabend, der der Sprachwissenschaft gewid- met war, trug den Titel: «Von der toten Sprachwissen- schaft zur lebendigen Sprachwissenschaft».",
      "Sie sehen also, überall liegt diesen Titelformulierun- gen zugrunde: Man will hinweisen auf den Weg, der aus 161 dem Gegenwärtigen hineinführt in die anthroposophi- sche Gestaltung des betreffenden geistigen Weges. Man hat eine Vorstellung davon, wie die einzelnen Diszipli- nen ihren Ausgangspunkt nehmen von den gegebenen wissenschaftlichen Formulierungen der Gegenwart und hineinlaufen in gewisse andere Erkenntnisse, welche durch Anthroposophie gegeben werden sollen; überall also absolut konkretes Vorstellen über mögliche Wege.",
      "Nur - wie gesagt - der Donnerstag trägt den außer- ordentlich verheißungsvollen Titel: «Ausblicke», sogar «Nationalökonomische Ausblicke», was eine abstrakte Formulierung ist, was aber in der Abstraktheit gerade hinweist darauf, daß man - ich möchte sagen nicht gehen, sondern springen möchte. Wenn wir dann den Freitag uns ansehen in der all- gemeinen Formulierung des Tagesprogrammes, so lautet dieses so: «Der Untergang der Religion in der gegen- wärtigen Theologie und die Neubegründung durch An- throposophie».",
      "Also hier wird zuerst ganz negativ formuliert: Der Untergang der Religion in der gegen- wärtigen Theologie und die Neubegründung durch An- throposophie. - Es wird also nur hingewiesen, auch noch in negativer Weise, daß es etwas gibt wie Anthro- posophie, und daß dadurch Theologie und Religion eine Erneuerung erfahren können. Es wird in diesem Titel nicht in so konkreter Weise gezeigt, wie der Weg aus den gegenwärtigen Wirrnissen heraus in die anthroposophi- sche Gestaltung hineinführen kann.",
      "Wenn Sie nun das zum Beispiel mit der Formulierung am Sonntag vergleichen: «Von lebensfeindlicher Mecha- nistik zu wahrer Phänomenologie», so haben Sie hier sogar schon in dem Worte «Phänomenologie» eine ganz konkrete Bezeichnung für das, was werden soll. Ebenso 162 haben Sie in dem Worte: «Menschenerkenntnis» vom Montag auf etwas durchaus Konkretes hingewiesen.",
      "Bei der Philosophie haben Sie auf das philosophische Be- wußtsein in der Gegenwart, also auch auf etwas Konkretes hingewiesen, bei der Erziehungswissenschaft auf die pädagogischen Forderungen der Gegenwart, und bei der Sprachwissenschaft wird gesagt: «Von der toten Sprachwissenschaft zur lebendigen Sprachwissenschaft», also auch eine ms Konkrete gehende Formulierung. Nun, es ist das außerordentlich bezeichnend, daß dieser Hochschulkursus, der im wesentlichen sowohl innerlich wie äußerlich in der Freitags-Veranstaltung gegipfelt hat, und der im Grunde genommen - insbeson- dere die Empfindung konnte das ergeben - einen theo- logischen Charakter hatte, daß dieser Hochschulkurs, der ja auch sonst außerordentlich gut besucht war, am Freitag, am theologischen Tag, einen solchen Besuch hatte, daß es «brechend voll», übervoll war, und es ist außerordentlich bezeichnend, daß dieser Kursus gerade in der Tagesformulierung für das theologische Programm etwas Negatives hatte.",
      "Natürlich gingen diese Formulie- rungen aus dem hervor, was eben einmal vorliegt, und man versuchte in einer durchaus ehrlichen und aufrich- tigen Weise, diese Formulierungen so zu geben, wie sie eben auf der einen Seite aus dem Bewußtsein der Ge- genwart hervorgehen können, und auf der ändern Seite aus einer Vorstellung darüber, was aus diesem Bewußt- sein der Gegenwart durch Anthroposophie werden kann. Gehen wir dann die einzelnen Tage durch, so treffen wir natürlich auf Dinge, die uns zum größten Teil be- kannt sind.",
      "Sonntag: Von lebensfeindlicher Mechanistik zu wahrer Phänomenologie. Da handelt es sich also darum, daß darauf hingewiesen wird, wie alles Spekulieren 163 über Atomistik, über eine mechanistische Auffassung der leblosen Natur überwunden werden soll, und wie man zu einem reinen Betrachten dessen, was in den Phäno- menen, in den Erscheinungen vorliegt, kommen soll, wie diese Erscheinungen selber für sich sprechen sollen, wie sie selber ihre Theorie liefern sollen.",
      "Also es ist in dieser Formulierung zum Ausdrucke gebracht, daß man Goetheanismus treiben will in der Naturwissenschaft. Es ist dann in der organischen Naturwissenschaft zum Ausdrucke gebracht, daß man den gesamten Um- fang der organischen Naturwissenschaft auf Menschen- erkenntnis bauen müsse, daß man also notwendig hat, nicht so zerstückelt die Natur in ihren Reichen zu be- trachten, wie man das gegenwärtig tut, sondern daß man vor allen Dingen darauf auszugehen hätte, den Menschen kennenzulernen, und daß man vom Menschen aus die anderen Reiche der Natur zu erforschen hätte.",
      "Was dann die Philosophie betrifft, so handelte es sich am Dienstag darum zu zeigen, wie das philosophische Bewußtsein an einer Art von Ende angekommen ist. Es ist interessant, diese Formulierung im Zusammenhang zu denken zum Beispiel mit dem Hegeltum.",
      "Hegel hat ja bereits in seiner Philosophie im Beginne des 19. Jahr- hunderts gesagt, daß alle Philosophie der Gegenwart ein Ende sei, und daß man im Grunde genommen in der Philosophie nur auf den Hergang zurückblicken kann, daß aber eine Weiterentwicklung nicht möglich sei.",
      "Nun sollte eben an diesem Dienstag gezeigt werden, wie aus dem Ende der Philosophie ein Anfang, ein neuer Anfang hervorgehen kann, wenn man diesen Anfang in anthro- posophischem Sinne gestaltet. In der Erziehungswissenschaft wollte man darauf hindeuten, daß eigentlich alle wirklich denkenden Men- 164 sehen der Gegenwart gewisse pädagogische Forderun- gen aufstellen, die aber nicht zu erfüllen sind mit dem, was man gegenwärtig an Pädagogik entwickelt, daß also diese Forderungen, die im Grunde genommen alle den- kenden Menschen aufstellen, nur zu erfüllen sind durch Anthroposophie.",
      "In der Sprachwissenschaft sollte gezeigt werden, wie die Sprache selber als lebendiger Organismus im Zusam- menhange mit dem Menschen erfaßt werden soll, nicht bloß aus den toten Urkunden heraus, wie das bei der gegenwärtigen Sprachwissenschaft der Fall ist. Von der Sozialwissenschaft ist ja nur zu sagen, daß in einer außerordentlich lichtvollen Weise Emil Leinhas aus seinen tüchtigen Kenntnissen heraus über das Geld- problem der Gegenwart ganz Bedeutendes gesagt hat; aber es läßt sich ja über das Geldproblem der Gegenwart, wie Sie wohl selbst manchmal fühlen werden, nicht ge- rade außerordentlich viel Positives sagen.",
      "Das werden Sie schon hier in der Schweiz fühlen, in dem beinahe höchstvalutigen Lande; daß sich aber nicht viel Positives über das Geldproblem sagen läßt, wenn Sie über die Grenze hinüberkommen, das werden Sie ja glauben. Also das ist schon so, daß da nicht sehr viel Positives gesagt werden konnte.",
      "Solches Positive haben dann auch die nächsten beiden Vorträge nicht gebracht, und es hat ja gerade dieser nationalökonomische Tag gezeigt, wie im Grunde genommen die Pflege des Nationalökonomi- schen innerhalb unserer anthroposophischen Bewegung etwas ist, was eigentlich durch und durch versagt. Denn wir haben im Grunde genommen es nicht dazu bringen können, trotzdem immer wieder und wiederum die Notwendigkeit gerade auf diesem Gebiete betont wurde, daß in der Wirtschaftswissenschaft von Seiten derjeni- 165 gen, die im Wirtschaftsleben selber drinnenstehen, auch wirklich Zukunftssicheres vorgebracht worden wäre, namentlich solches nicht, das den so außerordentlich schwierigen Anforderungen der Gegenwart genügen würde.",
      "Und so war für diesen Tag der Titel «National- ökonomische Ausblicke» im Grunde genommen etwas wie ein tanzendes Versprechen; aber was dann der Tag gebracht hat, das war ein mehr oder weniger hinkendes Nachbewegen zu diesem tanzenden Versprechen. Was nun die Theologie betrifft: Ebenso interessant, wie die allgemeine Formulierung des Tagesprogrammes war, ebenso interessant waren auch die drei Titel der Vorträge, die auf meine einführenden Vorträge folgten.",
      "Der erste Titel, der Titel des Vortrages von Lizentiat Bock hieß: «Der Untergang der Religion im Psycholo- gismus», der Titel des Vortrages von Dr. Rittelmeyer hieß: «Der Untergang der Theologie im Irrationalis- mus», und der dritte Vortrag, gehalten von Dr.",
      "Geyer, hieß: «Der Untergang der Theologie im Historismus». Wir haben also dreifach den Untergang der Theologie beziehungsweise der Religion in diesen Tagen geschil- dert bekommen. Es hatte ja in einem gewissen Sinne die Lage der Zeit es von selbst ergeben, daß Theologen sprachen, die aus ihren besonderen Denk- und Empfindungserlebnissen heraus darlegten, wie sie innerhalb ihrer Theologie heute an einen toten Punkt kommen.",
      "Es war im Grunde ge- nommen überall die Tendenz vorhanden bei den Theo- logen, zu zeigen, wie sie innerhalb dessen, was ihnen die Theologie darbietet in der Gegenwart, an einen toten Punkt kommen. Und wenn man sich dann besinnt, was in positiver Weise vorgebracht worden ist, so könnte man zusam- 166 menfassend das, was an diesem Freitag gesagt worden ist, so formulieren: Die theologische Betrachtung der Religion - so meinte wohl Lizentiat Bock - kommt dazu, nur auf das seelische Erlebnis zu sehen, das man als religiöses Erlebnis, vielleicht als Gotteserlebnis bezeich- nen kann.",
      "Man findet, daß der Mensch unter den ver- schiedenen inneren Erlebnissen der Seele auch das reli- giöse Erlebnis hat, das Erlebnis, das in gewisser Beziehung hinweist auf ein Göttliches, daß man aber, wenn man unbefangen ist, sagen muß: Ja, da hat man eben nur ein subjektives Erlebnis. Man hat etwas rein Psychologisches.",
      "Man kann durchaus keine Gewähr finden dafür, daß diesem Erlebnis auch irgendetwas in der objektiven Welt entspricht. Es ist in der modernen Theologie das sub- jektive Gotteserlebnis nicht so, daß es zu einer wirklichen Annahme des Gottes führen kann, geschweige denn zu einer Anschauung über das Wesen des Göttlichen in der Welt.",
      "Es erstickt gewissermaßen das religiöse Element in dem Bewußtsein des Menschen in der psychologischen Tatsache: Ja, wir bedürfen eines religiösen Leben; aber es ist nichts da, was die Gewißheit liefern kann, daß diesem Bedürfnis auch irgendwie Befriedigung geschaffen wer- de. Die psychologische Tatsache ist da, daß der Mensch Religion braucht, aber die Gegenwart weiß dieser Reli- gion keinen Inhalt zu geben. - Das wäre etwa das Ergebnis des ersten Vortrages von Lizentiat Bock.",
      "Rittelmeyer stellte dann dar, wie die Theologie überdrüssig geworden ist des Rationalismus, wie sie dazu gekommen ist, nicht mehr das Wesen des Göttlichen in der Welt der Gedanken formulieren zu wollen, daß sie nicht mehr sagen wolle, das oder jenes sei Inhalt des Göttlichen, das die Welt durchwebt und durchlebt. Der Gedanke sollte ausgeschaltet werden aus dem Theologi- 167 sehen.",
      "Das Rationelle, das aus der Vernunft Stammende, sollte wegkommen, und das Irrationale, das, was den Gedanken ausschließt, das sollte Inhalt der Theologie werden. So daß man also eigentlich zu nichts anderem kommt in der Theologie, als zu den alleräußersten Ab- straktionen.",
      "Man getraut sich nicht zu sagen: Die Got- teswesenheit kann man durch diesen oder jenen Gedanken erfassen. Man getraut sich nur zu sagen: Die Gotteswe- senheit ist das Unbedingte, das Absolute. Einen ganz unbestimmten Begriff pfählt man hin, das Irrationale, etwas, was keine Vernunft erfassen kann.",
      "Nicht wahr, auf jedem anderen Gebiete des Lebens wäre es sonderbar, wenn man so negativ charakterisierte. Wenn zum Beispiel jemand fragt: Wer ist der Vorstand des Goetheanums? , und man antworten würde: Der Vorstand ist derjenige, der Vorstand von keiner anderen Institution ist -, dann würde man keine Auskunft dar- über bekommen, wer nun eigentlich der Vorstand des Goetheanums ist.",
      "So bekommt man natürlich auch keine Auskunft über das Göttliche, wenn man sagt: Die Ratio des göttlichen Wesens besteht darin, daß der Gott das Irrationale ist, dasjenige, was keine Vernunft erfassen kann. - Es ist alles nur Negation. Daran knüpfte dann Rittelmeyer einiges, was diese gegenwärtigen Irrationali- sten zu sagen haben, so zum Beispiel, wie der Mensch sich innerlich verhält, wenn er zu diesem nur auf irratio- nale Weise zu erfassenden Gott sich erheben will.",
      "Wie erlebt er das, dieses Erheben? Er erlebt es schweigend. Das ist nicht etwa das Schweigen des mystischen Erlebens, das sehr positiv sein kann, sondern das ist das Nichtssagen, das Aufhören, auch innerlich in Gedanken zu sich selber zu sprechen.",
      "Es wurde dann noch des weiteren ausgeführt, wie dieses Schweigen im Kultus Platz greift. Es ist aus 168 der absoluten Ohnmacht heraus, irgendwie überhaupt etwas zu formulieren, daß man die Zuflucht zu dem Schweigen nimmt.",
      "Dann war es ja interessant, wie zwei Herren spra- chen, ein Privatdozent und ein Pfarrer, die nun diesen Irrationalismus ihrerseits verteidigten, um besonders zu zeigen, daß der Irrationalismus wirklich etwas Herr- schendes in der Gegenwart ist. Da mußte man zum Beispiel von dem Privatdozenten hören: Ja, das wäre ganz richtig; es wäre zum Beispiel Unsinn zu sagen, aus der Natur könne man weniger den Gott finden als aus dem Geiste.",
      "Die Natur stehe nicht ferner dem Gotte als der Geist. Geisteserkenntnis liefere nicht mehr als Na- turerkenntnis für den Gott, denn der Gott sei eben das Unbedingte, das überall durchbricht. - Dies wurde sehr häufig wiederholt, daß der Gott das Unbedingte sei, das überall durchbricht.",
      "«Theologie!» - der Faust würde nicht nur einmal, sondern dreimal «leider» gesagt haben! Der Faust müßte umgedichtet werden: «Habe nun, ach! Philosophie, Juri- sterei, Medizin und leider, leider, leider auch Theologie studiert ...» -, wenn man so etwas immer wieder hören muß: Der Gott ist das Unbedingte, das überall durch- bricht.",
      "Da stellt man sich also das Überall vor und dann bricht's durch, bricht heraus - aber eben das Unbestimmte bricht überall durch! Nun, der letzte Vortrag war dann der von Dr. Geyer. Der behandelte den Untergang der Theologie im Histo- rismus.",
      "Geyer suchte zu zeigen, wie die Theologie all- mählich dazu gekommen ist, nichts mehr selber Schöp- ferisches zu haben, sondern nur zu betrachten, was schon gewesen ist, also immer die Geschichte zu studieren, was schon gewesen ist, um dadurch zu einem Inhalt zu 169 kommen. Das aber führt natürlich dazu, daß man höch- stens sagen kann: In der Vergangenheit haben die Men- schen ein religiöses Bewußtsein gehabt, aber heute haben sie nur noch die Möglichkeit, diese verschiedenen Stufen des religiösen Bewußtseins in der Vergangenheit zu be- trachten, und irgend etwas, was sie noch behalten wol- len, sich zu wählen. - Nur, zum Unglück, indem sie dann die Wahl treffen, bleibt ihnen nichts übrig von all dem, was ihnen von den verschiedenen Epochen der Vergangenheit da serviert wird.",
      "Ich selber habe dieses Tagesprogramm dadurch ein- geleitet, daß ich bemerkt habe, daß Anthroposophie durchaus nicht religionsbildend auftreten will, daß sie eine Erkenntnis übersinnlicher Welten sein will, und wenn Theologie eben von ihr befruchtet werden will, so mag sie das tun. Anthroposophie wird natürlich sagen, was über die übersinnlichen Welten zu sagen ist, und sie kann ihrerseits warten, was die Theologen für sich aus dieser Anthroposophie brauchen können.",
      "Es ist für denjenigen, der die Gesamtsituation der Gegenwart zu überschauen vermag, gerade an diesem Tage ein, aber natürlich aus den Verhältnissen hervorge- hender Mangel sehr stark hervorgetreten. Wenn ein vollständiges Erschöpfen des Tagesthemas hätte erfolgen können, so wie das bei den anderen Tagesthemen ja versucht worden ist - und mit Ausnahme der Sozialwis- senschaft bis zu einem gewissen Grade auch erreicht wurde -, dann hätte natürlich auch noch ein katholischer Theologe sprechen müssen.",
      "Denn alle diese Vorträge, die gehalten worden sind, sind lediglich aus dem protestan- tischen Bewußtsein heraus gesprochen worden. Ein ka- tholischer Theologe wäre ja in einer ganz anderen Lage gewesen als diese drei protestantischen Theologen.",
      "Ein 170 katholischer Theologe hat nicht nur eine historisch überbrachte, sondern eine historisch überbrachte und ewig gültige Theologie, eine Theologie, die in der Ge- genwart unbedingt so lebendig erfaßt werden muß, wie sie erfaßt worden ist, sagen wir im 3., 2. Jahrhunderte der christlichen Zeitrechung.",
      "Gewiß, die Konzilien und im 19. Jahrhundert dann der unfehlbar gewordene Papst haben ja manches hinzugefügt. Das sind aber einzelne Dogmen, das sind Hinzufügungen. Aber das ganze Wesen der katholischen Theologie ist etwas, was erstens von der Zeitentwicklung nicht abhängt, und was in sich durch seine eigene Erkenntnisart einen perennierenden, einen immerwährenden Charakter tragen soll.",
      "Es würde, wenn ein mehr fortschrittlicher Mann über katholische Theo- logie gesprochen haben würde, vielleicht das Ringen eines solchen katholischen Denkers wie dem Kardinal Newman eine außerordentlich interessante Auseinan- dersetzung haben erfahren können. Wenn ein weniger fortgeschrittener katholischer Theologe gesprochen hät- te, würde er eben das Wesen der ewigen Heilslehre, al- so eine katholische Theologie dargestellt haben.",
      "Dann würden Fragen von ungeheurer Bedeutung aufgetaucht sein, zum Beispiel jene Frage: Was ist nun eigentlich in der katholischen Theologie für den heutigen Menschen gegeben? In der katholischen Theologie ist ja ohne Zweifel, so wie sie heute auftritt, für das Gegenwartsbewußtsein nichts Lebendes.",
      "Aber sie war einmal etwas Lebendes. Ihr Inhalt beruht ja durchaus auf dem Ereignis alter geisteswissenschaftlicher, wenn auch atavistischer Er- kenntnisse. Was in der katholischen Theologie ent- halten ist, sagen wir über das Faktum der Schöpfung, über die Erlösung, über den Inhalt der Trinität, über alle 171 diese Dinge, das sind ja reale Begriffe, das ist etwas, was Inhalt hat; nur ein Inhalt, den das moderne Bewußtsein nicht mehr erfassen kann, sondern ihn in abstrakte, un- verständliche Dogmatik kleidet, oder auch gar nicht kleidet, sondern als unverständliche, trockene Dogmatik hinnimmt.",
      "Es war ja insbesondere die Entwicklung der katholi- schen Theologie im 19. Jahrhundert so, daß nicht mehr erkannt wurde, was in den Dogmeninhalten enthalten ist. Dafür lag gerade bei diesem Hochschulkurs in Berlin ein interessantes Erlebnis vor.",
      "Ich hatte am Freitag in meiner Einleitung aus dem unmittelbaren Erleben heraus folgendes gesagt, was Sie ja schon kennen, ich hatte gesagt: Wer das erlebt, was in unserer Naturumgebung ist und in dem, was an diese Naturumgebung sich anschließt, kommt, wenn er nicht irgendwie innerlich verkrüppelt ist, zum Bewußtsein des Vater-Gottes. Derjenige, der dann während seines Lebens das Ungenügende des Vatergott-Erlebnisses erkennt und eine Art innerer Wiedergeburt erlebt, der kommt zu dem Erleben des Gott-Sohnes, des Sohnes Gottes.",
      "Und auf dieselbe Weise kommt man dann durch ein Weiter- schreiten zu dem Geist-Erlebnis. Da dachte nun ein protestantischer Privatdozent, Lizentiat Tillich: Aha, da ist ja die Trinität, die muß man konstruieren , und er nannte das eine Konstruktion: Er merkte also gar nichts davon, daß da Erlebnisse zugrunde liegen.",
      "Das war ihm ganz fremd. Nun, so fremd sind auch jene Erlebnisse dem modernen Bewußtsein des 19. Jahrhunderts geworden, die den katholischen Dogmen zugrunde liegen. Diese katholischen Dogmen gehen natürlich ur- sprünglich zurück auf geistige Realitäten, aber man ver- 172 steht nichts mehr davon.",
      "Es sind leere Begriffe gewor- den. Nun sollte man aber im 19. Jahrhundert wenigstens wiederum dazu kommen, ein wenig äußerlich beleben zu können, was in der katholischen Theologie lebt. Sie wissen ja wohl, daß dieser Drang, wenigstens ein bißchen wieder verstehen zu können, was in der katholischen Theologie lebt, ganz besonders unter dem Pontifikat Leos XIII. aufgekommen ist.",
      "Daher dazumal die katho- lische Verordnung, die römische Verordnung für alle katholischen Theologen, zurückzukehren zum Studium der Thomistischen Philosophie, der Philosophie des Thomas von Aquino, weil die ganze spätere Philosophie nicht mehr brauchbar ist, um so etwas zu erfassen, wie es in den katholischen Dogmen liegt. Alle auf die Thomi- stik folgende Philosophie ist eigentlich nur brauchbar, um das natürliche Dasein zu verstehen, um der Natur- wissenschaft eine Grundlage zu geben, nicht aber um die geistigen Tatsachen zu verstehen, von denen man aller- dings auch auf katholischer Seite nichts weiß, aber die doch in den katholischen Dogmen in einer Zeit formu- liert worden sind, als man noch von diesen geistigen Tatsachen wußte.",
      "Um diese geistigen Tatsachen zu ver- stehen, dazu taugt alle spätere nach-thomistische Philo- sophie nichts mehr. Als man daher das Bedürfnis emp- fand, wiederum etwas von dem zu verstehen, was in den katholischen Dogmen liegt, forderte man die Erneuerung des Studiums der Thomistik, was ja heute das eigentliche philosophische Bestreben innerhalb des römischen Ka- tholizismus ist.",
      "Dem liegen durchaus historische Reali- täten zugrunde. Und wenn man vergleicht, was eigentlich notwendig ist, um wiederum ins Geistige hineinzukom- men, so sieht man schon ein, daß natürlich auch die Thomistik nicht genügt, um wieder zu beleben, was in 173 den alten, in Rom erstarrten Dogmen enthalten ist.",
      "Man muß da zu einer ganz anderen Betrachtung kommen. Bitte, erinnern Sie sich nur an die für einen gegenwär- tigen Literatur-Historiker so gänzlich verdrehte An- schauung, die ich hier, bevor ich von Dornach abgereist bin, in den letzten Vorträgen vorgebracht habe, wo ich mit Hinweggehen über alles, was Raum und Zeit ist, Ihnen dargestellt habe, wie Hamlet ein Schüler von Faust ist, wie Hamlet zehn Jahre lang zu Füßen des Faust gesessen hat; in jenen zehn Jahren, wo Faust seine Schüler an der Nase herumführte, und wie Hamlet einer von denen war, die damals grade und krumm und kreuz und quer an der Nase herumgeführt worden sind.",
      "Solche Zusammenhänge sind natürlich einem gegenwärtigen Literatur-Historiker ein Greuel. Aber man kann ja heute fast nichts Erhebliches sagen auf geistigem Gebiete, was den offiziellen Vertretern der Wissenschaft nicht ein Greuel wäre.",
      "Es ist heute ja geradezu das Stigma der wirklichen Wahrheit, daß sie den öffentlichen Vertretern der Wissenschaft ein Greuel ist. Nun, wenn Sie das schon für ein so profanes Gebiet nehmen, dann werden Sie sehen, was wirklich notwen- dig ist, um wiederum zu jener Beweglichkeit des Geistes zu kommen, die eine Grundlage liefern kann für das Erfassen dessen, was in den Dogmen bewahrt ist.",
      "Wie man zurückgehen muß zu einer ganz anderen Seelenver- fassung, um in die Art hineinzukommen, wie man in solchen Dogmen lebte, das zeigt ja gerade der Entwick- lungsgang des Kardinals Newman. Es ist ja vielleicht heute in Berlin selbstverständlich, daß man bei einem solchen Hochschulkurs nur von protestantischem Standpunkte aus redet und den katho- lischen Standpunkt unberücksichtigt läßt.",
      "Aber ein Bild 174 dessen, was da eigentlich heute waltet, bekommt man natürlich nicht, wenn man nicht auch den katholischen Standpunkt irgendwie zu erörtern in der Lage ist, ins- besondere heute nicht, wo wir wieder notwendig haben, mit unserem Blicke über die ganze Welt hinzuschauen. Sehen Sie, darüber müssen wir ja heute hinauskom- men, nur Kirchturms-Wissenschaft, Kirchturms-Weltanschauung zu reden. - Kirchturms-Pohtik kennen Sie, aber es gibt auch etwas wie Kirchturms-Weltanschauung.",
      "Sie tritt einem stark entgegen, wenn man so etwas sieht wie zum Beispiel an dem Freitag Abend, wo der Dr. Theberat über das Thema vorgetragen hat: «Atomi- stische und wirklichkeitsgemäße Betrachtung chemischer Prozesse».",
      "Das heißt, Dr. Theberat, der ja nun in unse- rem Forschungsinstitut in Stuttgart angestellt ist, ver- suchte zu zeigen, wie Atomistik verlassen werden muß und wie man eben die Phänomenologie auch in die Chemie hineintragen muß.",
      "Da trat dann in der Debatte Dr. Kurt Grelling auf. Ich will jetzt nicht über Dr. Kurt Grelling sprechen, der ja so ungefähr nach dem Rezepte auftritt: Ja, da wird in der Anthroposophie allerlei gesagt, aber das ist mir alles noch nicht wahrscheinlich.",
      "Sicher aber ist doch, daß 2 + 2 = 4 ist, und man muß sich doch an das halten, was sicher ist: 2 + 2 = 4; das ist sicher. - Das hat er ja schon im vorigen Sommer im Stuttgarter Kursus geltend gemacht und hat dann sogar zwei Uni- versitätslehrer zu Hilfe gezogen, um dieses, daß 2 + 2 = 4 ist, an einem besonderen Abend geltend zu machen. Dem konnte man natürlich nicht widersprechen.",
      "Ich meine, ich will damit nur symbolisch andeuten, was er sagte, denn 2 + 2 ist ja wirklich 4. Ich konnte nicht widersprechen. Ich konnte nicht einmal widersprechen, als er am letzten Freitag, ganz aus dem Zusammenhang 175 herausgerissen, sagte, ich hätte in Stuttgart ja zugegeben, daß 2 + 2 = 4 ist.",
      "Gewiß, ich kann das nicht in Abrede stellen. Ich meine jetzt nicht gerade 2 + 2 = 4, sondern Dinge, die im ganzen Zusammenhang ebenso wertvoll sind, die er damals vorgebracht hat. Er sagte dann: Ja, über die Frage, die da vorgebracht wurde, über Phäno- menologie, kann nicht vom Standpunkte der Naturwis- senschaft entschieden werden, sondern nur vom Stand- punkte der Philosophie aus.",
      "Nun, ich will nicht sagen, daß das gerade bloß «Göt- tingisch» ist, aber mindestens ist es heute nicht irgendwie weltmännisch wissenschaftlich gedacht, denn mit einem solchen Satze, daß etwas nicht naturwissenschaftlich, sondern nur philosophisch entschieden werden könne, würde man zum Beispiel in England überhaupt keinen Sinn verbinden können, weil dieser Unterschied etwas ist, was eben Kirchturms-Weltanschauung ist. Diese Formulierung, die kennt man nur innerhalb gewisser mitteleuropäischer Kreise.",
      "Jedenfalls ist es schon so, daß wir heute, wenn von solchen Fragen die Rede ist, einen weiteren Gesichts- kreis brauchen. Man kann zum Beispiel unmöglich im- mer weiter von Mitte, West und Ost sprechen.",
      "In den Formulierungen des Programms zum Wiener Kongreß ist ja fortwährend von West und Ost und Mitte die Rede, was ich nicht tadle. Ich finde es ja recht großgeistig, wenn von West und Ost und Mitte die Rede ist - aber ich meine, man muß dann auch seine Begriffe etwas erwei- tern; sie müssen dann wirklich auch diese Gebiete um- spannen.",
      "Man kann natürlich nicht von einem einge- schränkten Standpunkte aus die Welt umfassen. So fehlte natürlich [in Berlin bei den Vorträgen über Religion und Theologie] etwas, zum Beispiel in bezug 176 auf die westliche Entwicklung des religiösen Lebens, weil man das Katholische ganz ausgelassen hat, denn dieses westliche religiöse Leben hat gar nichts in sich von dem, was man berührt, wenn man bloß von der evan- gelischen Theologie spricht.",
      "Man kam auch gar nicht darauf zu reden, wie etwa der Puritanismus in England oder die Hochkirche in England oder dergleichen sich entwickelt haben. Also das alles bringe ich nicht als eine Kritik vor, denn selbstverständlich waren die Dinge, die vorgebracht worden sind, ausgezeichnet.",
      "Aber ich möchte doch im engeren anthroposophischen Kreise über das sprechen, was in Anknüpfung an die ganzen Vorgänge eben hätte gesagt werden müssen. Und da würde man eben gezeigt haben müssen, wie das gegenwärtige Denken eben gar nicht in der Lage ist, an das heranzukommen, was einmal Quell für den theologischen Inhalt war.",
      "Aber es war so, daß in Berlin keine Brücke zu sehen war zwischen dem, was moderne evangelische Theologie ist, und dem, was nun aus Anthroposophie kommen soll zur Belebung des religiösen Bewußtseins. Es waren immer nur Hinweise, daß das von der Anthroposophie kommen soll; aber wie es sich gestalten soll, davon war eigentlich im Grunde genommen nicht die Rede.",
      "Das sind Dinge, die Ihnen vielleicht ein Bild geben werden von jenem Ringen auf anthroposophischem Bo- den, das sich gerade in Berlin jetzt in der schönsten Weise zum Ausdruck gebracht hat. Es zeigte sich ja gerade in Berlin auch an der Teilnahme der verschiedenen Kreise - die Vorträge waren außerordentlich stark besucht, auch die Vormittagsvorträge -, daß durchaus etwas in der anthroposophischen Bewegung lebt, was stark und in- tensiv an das Gegenwartsbewußtsein heranschlägt. 177 Und es wurde von unserer Seite aus ja auch manch- mal nicht gespart in der Schärfe der Ausdrücke, die charakteristisch sein sollten für das, was ist.",
      "Ich erinnere mich zum Beispiel mit einer gewissen inneren Freude daran, wie am Sonnabend dann Dr. Schubert sprach, der innerhalb des Rahmens «Anthroposophie und Sprach- wissenschaft» auch seinerseits zeigen wollte, wie die Sprachwissenschaft im politischen Leben der Völker und Rassen eine Rolle spielte, und wie er dann in der Debatte temperamentvoll darauf hinweisen wollte, was heute die Sprachwissenschaft ist, und was sie werden muß durch die Anthroposophie.",
      "Es war temperamentvoll, als er dann sagte: Ja, er sei doch in Berlin gewesen, er habe bei den verschiedensten Lehrern Sprachwissenschaft studiert, und dann kam er an die Anthroposophie, um diese Sprachwissenschaft zu beleben; und da ging ihm erst ein Licht auf, da fand er, was die gegenwärtige Sprachwis- senschaft eigentlich ist: ein Misthaufen. - Und da schlug er auf den Tisch. Also es war nicht gespart worden an temperamentvollen Ausdrücken, um die Gegenwart zu charakterisieren.",
      "Die Gegner haben ja auch nicht gerade - ja, temperamentvoll kann ich eigentlich nicht sagen nun, so sage ich gar nichts! Die Abendveranstaltungen waren dann so, daß man versuchte, ein Bild von den anthroposophischen Inhalten zu geben.",
      "Es war namentlich diesmal sehr bedeutungs- voll, daß sowohl von Dr. Stein wie von Dr. Schwebsch, zwei Lehrern der Waldorfschule, anschauliche Bilder des pädagogischen Wirkens in der Waldorfschule gegeben wurden.",
      "Ich möchte sagen, so zwischen den Zeilen konnte man ja manches Merkwürdige erleben. Der ganze Kursus schloß dann am Sonntag. Ich hatte dann nachher am Sonntag noch den Schluß-Abendvortrag 178 zu halten, und die Vormittagsveranstaltungen schlössen mit einer vor einem vollbesetzten Hause gehaltenen Eurythmievorstellung im Deutschen Theater, die einen außerordentlich starken Erfolg hatte.",
      "Ich brauche wohl kaum zu sagen, daß, wenn Ihnen irgendwelche Zeitungsblätter in die Hand kommen soll- ten, Sie das Gegenteil von dem lesen werden, was da gewesen ist. Aber ein Herr, der zum Beispiel einen Artikel in einem Berliner Blatte geschrieben hat, den manche für einen Artikel pro Anthroposophie ansehen ich will mich darüber nicht äußern! -, der hat dann bei einem ändern großen Blatte angefragt, ob er nun auch einen Artikel über diesen Hochschulkurs schreiben darf.",
      "Man fragte: Pro oder Kontra? Da sagte er, weil er mein- te, daß sein Artikel Pro ist: Pro. Da sagte man: Nein, wir nehmen nur Kontra. - Also man kümmert sich nicht darum, was irgend jemand schreibt, sondern man kauft nur Kontra!",
      "Also Sie werden natürlich keine Vorstellung bekommen von dem, was da gewesen ist, wenn Sie andere Berichte bekommen von außen her. Schade ist es, daß außer dieser im Deutschen Theater erfolgten Eurythmie-Vorstellung nicht auch noch - außer den kurzen Eurythmie-Vorstellungen am Don- nerstag und Sonntag mehr Eurythmie gepflegt worden ist, denn es hätte vielleicht das nach dem Muster des Stuttgarter anthroposophischen Kongresses dazu führen können, daß unter der Last dieser vollbesetzten Tage die verehrten Anwesenden doch nicht gar so schwer zu tragen gehabt hätten.",
      "Denn ich kann mir schon vorstel- len, daß es recht hart war! Nehmen Sie zum Beispiel irgendeinen der Tage, so einen Durchschnittstag, wo nicht außerdem noch Sitzungen für eine Anzahl von Leuten gehalten worden sind, da hat derjenige, der alles 179 mitgemacht hat, fünf Vorträge und eine Diskussion ge- hört.",
      "Das ist für einen heutigen Menschen etwas viel, an einem Tage fünf Vorträge und eine Diskussion. Es waren eigentlich sogar zwei Diskussionen an einem normalen Tage. Also man hatte Gelegenheit, von 9 Uhr bis 3 Uhr und dann wiederum von 8 Uhr bis etwa 10 1/2 Uhr abends in einem fort in solchen Gedanken zu leben.",
      "Dem wäre natürlich viel besser gedient gewesen, wenn zwischen- durch, wie es in Stuttgart der Fall war, launige Euryth- mievorführungen hätten stattfinden können. - Nun, im Ganzen ist das Ergebnis ein außerordentlich Bedeut- sames. 180 ANHANG Zwei Briefe des Berliner Zweigleiters und Organisators des Hoch- schulkurses Rudolf Meyer an Rudolf Steiner Berlin S. O. 36, Cottbuser Ufer 25 26.",
      "August 1921 Hochverehrter Herr Dr. Steiner, darf ich im Namen der Berliner Bewegung die Bitte aussprechen, daß Sie im Anschluß an den von der Konzertdirektion Wolff veranstalteten Vortrag einen oder zwei öffentliche Vorträge halten, die von uns veranstaltet würden?",
      "Ich glaube, daß durch zwei oder drei große öffentliche Vorträge von Ihnen der Boden für den im nächsten Frühjahr von uns geplanten anthroposophi- schen Hochschulkurs gut vorbereitet wird. - Herr Raether [*], der wie ich Ihnen in diesem Frühjahr in Dornach mitteilte, damals 25 000 M stiftete für eine große eurythmische Vorstellung in Berlin, hat durch sein neuerliches Eintreten für die Verwirkli- chung des Hochschulkurses diesen eigentlich erst ermöglicht. Er wünscht so wie ich u. alle anderen Freunde, die mit der Seele bei der Bewegung sind, daß dieser Hochschulkursus eine großzügige Veranstaltung wird.",
      "Wir glauben, daß 2 oder mehrere große öffentliche Vorträge von Ihnen jetzt im September das Interesse der Berliner Öffentlichkeit in so weitem Maße erregen würden, daß wir auf eine unseren Plänen entsprechende starke Beteiligung im nächsten März beim Hochschulkurs rechnen können. Mit den herzlichsten Grüßen an Sie u. die verehrte Frau Doktor Ihr unwandelbar ergebener Rudolf Meyer [* Hans Raether, Lebensdaten unbekannt, zu dieser Zeit Vorstandsmitglied des Rudolf Steiner-Zweiges in Berlin.] 187 Berlin, Sonntag, den 6.",
      "November 1921 Hochverehrter Herr Dr. Steiner, Die Schwierigkeiten, für den Hochschulkursus im nächsten Frühjahr geeignete Räume zu erhalten, waren zeitweise so stark, daß es manchmal aussah, als würden die Verhältnisse uns zwingen, den Kursus zu vertagen.",
      "Nun stellt sich die Möglichkeit heraus, vom 1. - 15. März 22 die Berliner Singakademie zu erhalten. Der eigentliche Hochschulkursus könnte hier sehr gut stattfinden, wenn wir die Singakademie auch nicht für die Abende erhalten können, sondern für die Zeit von 9-3.",
      "Für die Abendveranstaltungen finden wir andere geeignete Räume. Uns scheint es, daß es besser ist, den Kursus im März 22, wenn auch an 2 Stellen, stattfinden zu lassen, als erst im Jahre 1923 an einer. Da der Berliner Hochschulkurs von anfang an so gedacht war, daß Sie ihm durch Ihre Vortragstätigkeit u. sonstige Mitwirkung das Schwergewicht u. die Durchschlagskraft geben, so hängt die Möglichkeit, den Kursus in der Zeit vom 1. - 15.",
      "März 22 stattfinden zu lassen, hauptsächlich davon ab, ob Ihre Disposi- tionen Ihnen erlauben, während dieser Zeit in Berlin zu sein. Darf ich bitten, mir ganz kurz mitzuteilen, ob es Ihnen möglich sein wird, vom 1. - 15.",
      "März 22 in Berlin tätig zu sein, damit wir dann sofort die Singakademie und die anderen Räume mieten. Ein adressierter Briefumschlag liegt bei. Herzliche Grüße von unseren Freunden u. mir an Sie u. Frau Dr.",
      "Ihr stets aufrichtig verbundener Rudolf Meyer 188"
    ],
    "sentences": [
      [
        "Meine lieben Freunde!",
        "Gestatten Sie, daß ich heute eini- ges über den Verlauf des Berliner Hochschulkurses sage.",
        "Der Berliner Hochschulkurs hatte sein Programm in einer besonderen Weise angeordnet.",
        "Es sollten darge- stellt werden die Beziehungen gewisser Lebens- und Wissenschaftszweige in der Gegenwart zur anthroposo- phischen Weltanschauung."
      ],
      [
        "Der einzelne Tag sollte im- mer einem besonderen Wissenschafts- oder Lebenszwei- ge in der Hauptsache gewidmet sein.",
        "Und die Woche war so eingeteilt, daß begonnen wurde mit dem Sonntag, der der anorganischen Naturwissenschaft gewidmet sein sollte."
      ],
      [
        "Der Montag sollte dann gewidmet sein der organi- schen Naturwissenschaft und der Medizin, der Dienstag der Philosophie, der Mittwoch der Erziehungswissen- schaft, der Donnerstag der Volkswirtschaft und der Freitag der Theologie.",
        "Der Sonnabend sollte der Sprach- wissenschaft gewidmet sein, und dann sollte am Sonntag das Ganze durch die Eurythmievorstellung im Deut- schen Theater einen gewissen Abschluß erlangen."
      ],
      [
        "Es war das Programm so gedacht, daß jeder Tag mit einem kurzen Vortrag von mir beginnen sollte.",
        "Nur der erste Sonntag konnte nicht so beginnen, da ich damals noch nicht in Berlin sein konnte.",
        "So mußte ich am Montag in meinen einführenden Worten sowohl die anorganische wie die organische Naturwissenschaft zu- 159 sammenfassen."
      ],
      [
        "Dann sollte der Tag also einen einheitli- chen Charakter tragen.",
        "Es fanden anschließend an meine Einführungsworte dann zwei weitere Vorträge am Vor- mittag statt.",
        "Dann fand eine halbstündige Imbißpause statt, zu der man aber - das war schon angekündigt - in den Räumen der Singakademie keinen Imbiß bekam."
      ],
      [
        "Und von l bis 2 Uhr sollte dann eine Diskussion stattfin- den.",
        "Daran sollte sich dann der letzte Vortrag des Vor- mittags anschließen von 2 bis 3 Uhr.",
        "Es war ein etwas anstrengendes Programm.",
        "Am Abend schlössen sich daran Vorträge, die zum Teil m der Philharmonie von mir gehalten wurden, zum Teil von anderen in den Räumen der Berliner Universität; jeden Abend einen Vortrag und bei den ändern Vorträgen, außer meinem, war immer noch nach diesen Vorträgen abends auch eine Art von Aussprache."
      ],
      [
        "Es waren die Tage also außeror- dentlich reichlich besetzt.",
        "Nun, die ganze Gliederung des Programmes darf tatsächlich interessant genannt werden, namentlich durch die Formulierungen, welche die einzelnen Tagespro- gramme erfahren hatten."
      ],
      [
        "Gewissermaßen hatte jeder Tag einen Gesamttitel, und die Formulierungen dieser Ge- samttitel für die Tage sind nun wirklich interessant, denn sie verraten so manches Bedeutungsvolle: Jeder einzelne Tag hatte nämlich in seiner Formulierung etwas Positi- ves, nur der Freitag nicht, der der Theologie gewidmet war.",
        "Das ist schon bedeutsam, nicht so sehr aus dem Zeitbewußtsein heraus, sondern aus der Art und Weise, wie man sich zu der Entwicklung des Anthroposophi- schen auf Seiten derjenigen stellte, die das Programm formuliert haben."
      ],
      [
        "Man fühlte sich einfach gedrängt, die anderen Tagesprogramme in positivem Sinne zu for- mulieren, und wir brauchen uns nur diese Formulierun- 160 gen anzuschauen, um das Bedeutungsvolle herauszu- finden.",
        "Sonntag, den 5."
      ],
      [
        "März: «Von lebensfeindlicher Me- chanistik zu wahrer Phänomenologie».",
        "Es wird also die Hoffnung ausgesprochen in der Formulierung des Pro- grammes, daß man durch Anthroposophie dazu kommen wird, eine Phänomenologie als Grundlage der Natur- wissenschaft, der anorganischen Naturwissenschaft zu finden."
      ],
      [
        "Noch positiver ist dann das Programm vom Montag zusammengefaßt: «Wege anthroposophischer Menschen- erkenntnis in Biologie und Medizin», und ebenso positiv das Programm vom Dienstag über Philosophie: «Die Begründung der Anthroposophie aus dem philosophi- schen Bewußtsem der Gegenwart.» Ebenso positiv das Programm vom Mittwoch: «Von modernen pädagogischen Forderungen zu ihrer Ver- wirklichung durch Anthroposophie» - also auch hier der Gedanke: Es bestehen solche pädagogischen Forderun- gen in der Gegenwart, die durch Anthroposophie ver- wirklicht werden können.",
        "Der Donnerstag, der der Sozialwissenschaft gewid- met war, hatte ja sogar einen sehr verheißungsvollen Titel in der Gesamtformulierung des Programmes, ob- wohl das, was dann gehalten worden ist, weniger verhei- ßungsvoll war."
      ],
      [
        "Der Donnerstag trug sogar den außeror- dentlich verheißungsvollen Titel, der sehr positiv klingt: «Nationalökonomische Ausblicke».",
        "Der Sonnabend, der der Sprachwissenschaft gewid- met war, trug den Titel: «Von der toten Sprachwissen- schaft zur lebendigen Sprachwissenschaft»."
      ],
      [
        "Sie sehen also, überall liegt diesen Titelformulierun- gen zugrunde: Man will hinweisen auf den Weg, der aus 161 dem Gegenwärtigen hineinführt in die anthroposophi- sche Gestaltung des betreffenden geistigen Weges.",
        "Man hat eine Vorstellung davon, wie die einzelnen Diszipli- nen ihren Ausgangspunkt nehmen von den gegebenen wissenschaftlichen Formulierungen der Gegenwart und hineinlaufen in gewisse andere Erkenntnisse, welche durch Anthroposophie gegeben werden sollen; überall also absolut konkretes Vorstellen über mögliche Wege."
      ],
      [
        "Nur - wie gesagt - der Donnerstag trägt den außer- ordentlich verheißungsvollen Titel: «Ausblicke», sogar «Nationalökonomische Ausblicke», was eine abstrakte Formulierung ist, was aber in der Abstraktheit gerade hinweist darauf, daß man - ich möchte sagen nicht gehen, sondern springen möchte.",
        "Wenn wir dann den Freitag uns ansehen in der all- gemeinen Formulierung des Tagesprogrammes, so lautet dieses so: «Der Untergang der Religion in der gegen- wärtigen Theologie und die Neubegründung durch An- throposophie»."
      ],
      [
        "Also hier wird zuerst ganz negativ formuliert: Der Untergang der Religion in der gegen- wärtigen Theologie und die Neubegründung durch An- throposophie. - Es wird also nur hingewiesen, auch noch in negativer Weise, daß es etwas gibt wie Anthro- posophie, und daß dadurch Theologie und Religion eine Erneuerung erfahren können.",
        "Es wird in diesem Titel nicht in so konkreter Weise gezeigt, wie der Weg aus den gegenwärtigen Wirrnissen heraus in die anthroposophi- sche Gestaltung hineinführen kann."
      ],
      [
        "Wenn Sie nun das zum Beispiel mit der Formulierung am Sonntag vergleichen: «Von lebensfeindlicher Mecha- nistik zu wahrer Phänomenologie», so haben Sie hier sogar schon in dem Worte «Phänomenologie» eine ganz konkrete Bezeichnung für das, was werden soll.",
        "Ebenso 162 haben Sie in dem Worte: «Menschenerkenntnis» vom Montag auf etwas durchaus Konkretes hingewiesen."
      ],
      [
        "Bei der Philosophie haben Sie auf das philosophische Be- wußtsein in der Gegenwart, also auch auf etwas Konkretes hingewiesen, bei der Erziehungswissenschaft auf die pädagogischen Forderungen der Gegenwart, und bei der Sprachwissenschaft wird gesagt: «Von der toten Sprachwissenschaft zur lebendigen Sprachwissenschaft», also auch eine ms Konkrete gehende Formulierung.",
        "Nun, es ist das außerordentlich bezeichnend, daß dieser Hochschulkursus, der im wesentlichen sowohl innerlich wie äußerlich in der Freitags-Veranstaltung gegipfelt hat, und der im Grunde genommen - insbeson- dere die Empfindung konnte das ergeben - einen theo- logischen Charakter hatte, daß dieser Hochschulkurs, der ja auch sonst außerordentlich gut besucht war, am Freitag, am theologischen Tag, einen solchen Besuch hatte, daß es «brechend voll», übervoll war, und es ist außerordentlich bezeichnend, daß dieser Kursus gerade in der Tagesformulierung für das theologische Programm etwas Negatives hatte."
      ],
      [
        "Natürlich gingen diese Formulie- rungen aus dem hervor, was eben einmal vorliegt, und man versuchte in einer durchaus ehrlichen und aufrich- tigen Weise, diese Formulierungen so zu geben, wie sie eben auf der einen Seite aus dem Bewußtsein der Ge- genwart hervorgehen können, und auf der ändern Seite aus einer Vorstellung darüber, was aus diesem Bewußt- sein der Gegenwart durch Anthroposophie werden kann.",
        "Gehen wir dann die einzelnen Tage durch, so treffen wir natürlich auf Dinge, die uns zum größten Teil be- kannt sind."
      ],
      [
        "Sonntag: Von lebensfeindlicher Mechanistik zu wahrer Phänomenologie.",
        "Da handelt es sich also darum, daß darauf hingewiesen wird, wie alles Spekulieren 163 über Atomistik, über eine mechanistische Auffassung der leblosen Natur überwunden werden soll, und wie man zu einem reinen Betrachten dessen, was in den Phäno- menen, in den Erscheinungen vorliegt, kommen soll, wie diese Erscheinungen selber für sich sprechen sollen, wie sie selber ihre Theorie liefern sollen."
      ],
      [
        "Also es ist in dieser Formulierung zum Ausdrucke gebracht, daß man Goetheanismus treiben will in der Naturwissenschaft.",
        "Es ist dann in der organischen Naturwissenschaft zum Ausdrucke gebracht, daß man den gesamten Um- fang der organischen Naturwissenschaft auf Menschen- erkenntnis bauen müsse, daß man also notwendig hat, nicht so zerstückelt die Natur in ihren Reichen zu be- trachten, wie man das gegenwärtig tut, sondern daß man vor allen Dingen darauf auszugehen hätte, den Menschen kennenzulernen, und daß man vom Menschen aus die anderen Reiche der Natur zu erforschen hätte."
      ],
      [
        "Was dann die Philosophie betrifft, so handelte es sich am Dienstag darum zu zeigen, wie das philosophische Bewußtsein an einer Art von Ende angekommen ist.",
        "Es ist interessant, diese Formulierung im Zusammenhang zu denken zum Beispiel mit dem Hegeltum."
      ],
      [
        "Hegel hat ja bereits in seiner Philosophie im Beginne des 19.",
        "Jahr- hunderts gesagt, daß alle Philosophie der Gegenwart ein Ende sei, und daß man im Grunde genommen in der Philosophie nur auf den Hergang zurückblicken kann, daß aber eine Weiterentwicklung nicht möglich sei."
      ],
      [
        "Nun sollte eben an diesem Dienstag gezeigt werden, wie aus dem Ende der Philosophie ein Anfang, ein neuer Anfang hervorgehen kann, wenn man diesen Anfang in anthro- posophischem Sinne gestaltet.",
        "In der Erziehungswissenschaft wollte man darauf hindeuten, daß eigentlich alle wirklich denkenden Men- 164 sehen der Gegenwart gewisse pädagogische Forderun- gen aufstellen, die aber nicht zu erfüllen sind mit dem, was man gegenwärtig an Pädagogik entwickelt, daß also diese Forderungen, die im Grunde genommen alle den- kenden Menschen aufstellen, nur zu erfüllen sind durch Anthroposophie."
      ],
      [
        "In der Sprachwissenschaft sollte gezeigt werden, wie die Sprache selber als lebendiger Organismus im Zusam- menhange mit dem Menschen erfaßt werden soll, nicht bloß aus den toten Urkunden heraus, wie das bei der gegenwärtigen Sprachwissenschaft der Fall ist.",
        "Von der Sozialwissenschaft ist ja nur zu sagen, daß in einer außerordentlich lichtvollen Weise Emil Leinhas aus seinen tüchtigen Kenntnissen heraus über das Geld- problem der Gegenwart ganz Bedeutendes gesagt hat; aber es läßt sich ja über das Geldproblem der Gegenwart, wie Sie wohl selbst manchmal fühlen werden, nicht ge- rade außerordentlich viel Positives sagen."
      ],
      [
        "Das werden Sie schon hier in der Schweiz fühlen, in dem beinahe höchstvalutigen Lande; daß sich aber nicht viel Positives über das Geldproblem sagen läßt, wenn Sie über die Grenze hinüberkommen, das werden Sie ja glauben.",
        "Also das ist schon so, daß da nicht sehr viel Positives gesagt werden konnte."
      ],
      [
        "Solches Positive haben dann auch die nächsten beiden Vorträge nicht gebracht, und es hat ja gerade dieser nationalökonomische Tag gezeigt, wie im Grunde genommen die Pflege des Nationalökonomi- schen innerhalb unserer anthroposophischen Bewegung etwas ist, was eigentlich durch und durch versagt.",
        "Denn wir haben im Grunde genommen es nicht dazu bringen können, trotzdem immer wieder und wiederum die Notwendigkeit gerade auf diesem Gebiete betont wurde, daß in der Wirtschaftswissenschaft von Seiten derjeni- 165 gen, die im Wirtschaftsleben selber drinnenstehen, auch wirklich Zukunftssicheres vorgebracht worden wäre, namentlich solches nicht, das den so außerordentlich schwierigen Anforderungen der Gegenwart genügen würde."
      ],
      [
        "Und so war für diesen Tag der Titel «National- ökonomische Ausblicke» im Grunde genommen etwas wie ein tanzendes Versprechen; aber was dann der Tag gebracht hat, das war ein mehr oder weniger hinkendes Nachbewegen zu diesem tanzenden Versprechen.",
        "Was nun die Theologie betrifft: Ebenso interessant, wie die allgemeine Formulierung des Tagesprogrammes war, ebenso interessant waren auch die drei Titel der Vorträge, die auf meine einführenden Vorträge folgten."
      ],
      [
        "Der erste Titel, der Titel des Vortrages von Lizentiat Bock hieß: «Der Untergang der Religion im Psycholo- gismus», der Titel des Vortrages von Dr.",
        "Rittelmeyer hieß: «Der Untergang der Theologie im Irrationalis- mus», und der dritte Vortrag, gehalten von Dr."
      ],
      [
        "Geyer, hieß: «Der Untergang der Theologie im Historismus».",
        "Wir haben also dreifach den Untergang der Theologie beziehungsweise der Religion in diesen Tagen geschil- dert bekommen.",
        "Es hatte ja in einem gewissen Sinne die Lage der Zeit es von selbst ergeben, daß Theologen sprachen, die aus ihren besonderen Denk- und Empfindungserlebnissen heraus darlegten, wie sie innerhalb ihrer Theologie heute an einen toten Punkt kommen."
      ],
      [
        "Es war im Grunde ge- nommen überall die Tendenz vorhanden bei den Theo- logen, zu zeigen, wie sie innerhalb dessen, was ihnen die Theologie darbietet in der Gegenwart, an einen toten Punkt kommen.",
        "Und wenn man sich dann besinnt, was in positiver Weise vorgebracht worden ist, so könnte man zusam- 166 menfassend das, was an diesem Freitag gesagt worden ist, so formulieren: Die theologische Betrachtung der Religion - so meinte wohl Lizentiat Bock - kommt dazu, nur auf das seelische Erlebnis zu sehen, das man als religiöses Erlebnis, vielleicht als Gotteserlebnis bezeich- nen kann."
      ],
      [
        "Man findet, daß der Mensch unter den ver- schiedenen inneren Erlebnissen der Seele auch das reli- giöse Erlebnis hat, das Erlebnis, das in gewisser Beziehung hinweist auf ein Göttliches, daß man aber, wenn man unbefangen ist, sagen muß: Ja, da hat man eben nur ein subjektives Erlebnis.",
        "Man hat etwas rein Psychologisches."
      ],
      [
        "Man kann durchaus keine Gewähr finden dafür, daß diesem Erlebnis auch irgendetwas in der objektiven Welt entspricht.",
        "Es ist in der modernen Theologie das sub- jektive Gotteserlebnis nicht so, daß es zu einer wirklichen Annahme des Gottes führen kann, geschweige denn zu einer Anschauung über das Wesen des Göttlichen in der Welt."
      ],
      [
        "Es erstickt gewissermaßen das religiöse Element in dem Bewußtsein des Menschen in der psychologischen Tatsache: Ja, wir bedürfen eines religiösen Leben; aber es ist nichts da, was die Gewißheit liefern kann, daß diesem Bedürfnis auch irgendwie Befriedigung geschaffen wer- de.",
        "Die psychologische Tatsache ist da, daß der Mensch Religion braucht, aber die Gegenwart weiß dieser Reli- gion keinen Inhalt zu geben. - Das wäre etwa das Ergebnis des ersten Vortrages von Lizentiat Bock."
      ],
      [
        "Rittelmeyer stellte dann dar, wie die Theologie überdrüssig geworden ist des Rationalismus, wie sie dazu gekommen ist, nicht mehr das Wesen des Göttlichen in der Welt der Gedanken formulieren zu wollen, daß sie nicht mehr sagen wolle, das oder jenes sei Inhalt des Göttlichen, das die Welt durchwebt und durchlebt.",
        "Der Gedanke sollte ausgeschaltet werden aus dem Theologi- 167 sehen."
      ],
      [
        "Das Rationelle, das aus der Vernunft Stammende, sollte wegkommen, und das Irrationale, das, was den Gedanken ausschließt, das sollte Inhalt der Theologie werden.",
        "So daß man also eigentlich zu nichts anderem kommt in der Theologie, als zu den alleräußersten Ab- straktionen."
      ],
      [
        "Man getraut sich nicht zu sagen: Die Got- teswesenheit kann man durch diesen oder jenen Gedanken erfassen.",
        "Man getraut sich nur zu sagen: Die Gotteswe- senheit ist das Unbedingte, das Absolute.",
        "Einen ganz unbestimmten Begriff pfählt man hin, das Irrationale, etwas, was keine Vernunft erfassen kann."
      ],
      [
        "Nicht wahr, auf jedem anderen Gebiete des Lebens wäre es sonderbar, wenn man so negativ charakterisierte.",
        "Wenn zum Beispiel jemand fragt: Wer ist der Vorstand des Goetheanums? , und man antworten würde: Der Vorstand ist derjenige, der Vorstand von keiner anderen Institution ist -, dann würde man keine Auskunft dar- über bekommen, wer nun eigentlich der Vorstand des Goetheanums ist."
      ],
      [
        "So bekommt man natürlich auch keine Auskunft über das Göttliche, wenn man sagt: Die Ratio des göttlichen Wesens besteht darin, daß der Gott das Irrationale ist, dasjenige, was keine Vernunft erfassen kann. - Es ist alles nur Negation.",
        "Daran knüpfte dann Rittelmeyer einiges, was diese gegenwärtigen Irrationali- sten zu sagen haben, so zum Beispiel, wie der Mensch sich innerlich verhält, wenn er zu diesem nur auf irratio- nale Weise zu erfassenden Gott sich erheben will."
      ],
      [
        "Wie erlebt er das, dieses Erheben?",
        "Er erlebt es schweigend.",
        "Das ist nicht etwa das Schweigen des mystischen Erlebens, das sehr positiv sein kann, sondern das ist das Nichtssagen, das Aufhören, auch innerlich in Gedanken zu sich selber zu sprechen."
      ],
      [
        "Es wurde dann noch des weiteren ausgeführt, wie dieses Schweigen im Kultus Platz greift.",
        "Es ist aus 168 der absoluten Ohnmacht heraus, irgendwie überhaupt etwas zu formulieren, daß man die Zuflucht zu dem Schweigen nimmt."
      ],
      [
        "Dann war es ja interessant, wie zwei Herren spra- chen, ein Privatdozent und ein Pfarrer, die nun diesen Irrationalismus ihrerseits verteidigten, um besonders zu zeigen, daß der Irrationalismus wirklich etwas Herr- schendes in der Gegenwart ist.",
        "Da mußte man zum Beispiel von dem Privatdozenten hören: Ja, das wäre ganz richtig; es wäre zum Beispiel Unsinn zu sagen, aus der Natur könne man weniger den Gott finden als aus dem Geiste."
      ],
      [
        "Die Natur stehe nicht ferner dem Gotte als der Geist.",
        "Geisteserkenntnis liefere nicht mehr als Na- turerkenntnis für den Gott, denn der Gott sei eben das Unbedingte, das überall durchbricht. - Dies wurde sehr häufig wiederholt, daß der Gott das Unbedingte sei, das überall durchbricht."
      ],
      [
        "«Theologie!» - der Faust würde nicht nur einmal, sondern dreimal «leider» gesagt haben!",
        "Der Faust müßte umgedichtet werden: «Habe nun, ach!",
        "Philosophie, Juri- sterei, Medizin und leider, leider, leider auch Theologie studiert ...» -, wenn man so etwas immer wieder hören muß: Der Gott ist das Unbedingte, das überall durch- bricht."
      ],
      [
        "Da stellt man sich also das Überall vor und dann bricht's durch, bricht heraus - aber eben das Unbestimmte bricht überall durch!",
        "Nun, der letzte Vortrag war dann der von Dr.",
        "Geyer.",
        "Der behandelte den Untergang der Theologie im Histo- rismus."
      ],
      [
        "Geyer suchte zu zeigen, wie die Theologie all- mählich dazu gekommen ist, nichts mehr selber Schöp- ferisches zu haben, sondern nur zu betrachten, was schon gewesen ist, also immer die Geschichte zu studieren, was schon gewesen ist, um dadurch zu einem Inhalt zu 169 kommen.",
        "Das aber führt natürlich dazu, daß man höch- stens sagen kann: In der Vergangenheit haben die Men- schen ein religiöses Bewußtsein gehabt, aber heute haben sie nur noch die Möglichkeit, diese verschiedenen Stufen des religiösen Bewußtseins in der Vergangenheit zu be- trachten, und irgend etwas, was sie noch behalten wol- len, sich zu wählen. - Nur, zum Unglück, indem sie dann die Wahl treffen, bleibt ihnen nichts übrig von all dem, was ihnen von den verschiedenen Epochen der Vergangenheit da serviert wird."
      ],
      [
        "Ich selber habe dieses Tagesprogramm dadurch ein- geleitet, daß ich bemerkt habe, daß Anthroposophie durchaus nicht religionsbildend auftreten will, daß sie eine Erkenntnis übersinnlicher Welten sein will, und wenn Theologie eben von ihr befruchtet werden will, so mag sie das tun.",
        "Anthroposophie wird natürlich sagen, was über die übersinnlichen Welten zu sagen ist, und sie kann ihrerseits warten, was die Theologen für sich aus dieser Anthroposophie brauchen können."
      ],
      [
        "Es ist für denjenigen, der die Gesamtsituation der Gegenwart zu überschauen vermag, gerade an diesem Tage ein, aber natürlich aus den Verhältnissen hervorge- hender Mangel sehr stark hervorgetreten.",
        "Wenn ein vollständiges Erschöpfen des Tagesthemas hätte erfolgen können, so wie das bei den anderen Tagesthemen ja versucht worden ist - und mit Ausnahme der Sozialwis- senschaft bis zu einem gewissen Grade auch erreicht wurde -, dann hätte natürlich auch noch ein katholischer Theologe sprechen müssen."
      ],
      [
        "Denn alle diese Vorträge, die gehalten worden sind, sind lediglich aus dem protestan- tischen Bewußtsein heraus gesprochen worden.",
        "Ein ka- tholischer Theologe wäre ja in einer ganz anderen Lage gewesen als diese drei protestantischen Theologen."
      ],
      [
        "Ein 170 katholischer Theologe hat nicht nur eine historisch überbrachte, sondern eine historisch überbrachte und ewig gültige Theologie, eine Theologie, die in der Ge- genwart unbedingt so lebendig erfaßt werden muß, wie sie erfaßt worden ist, sagen wir im 3., 2.",
        "Jahrhunderte der christlichen Zeitrechung."
      ],
      [
        "Gewiß, die Konzilien und im 19.",
        "Jahrhundert dann der unfehlbar gewordene Papst haben ja manches hinzugefügt.",
        "Das sind aber einzelne Dogmen, das sind Hinzufügungen.",
        "Aber das ganze Wesen der katholischen Theologie ist etwas, was erstens von der Zeitentwicklung nicht abhängt, und was in sich durch seine eigene Erkenntnisart einen perennierenden, einen immerwährenden Charakter tragen soll."
      ],
      [
        "Es würde, wenn ein mehr fortschrittlicher Mann über katholische Theo- logie gesprochen haben würde, vielleicht das Ringen eines solchen katholischen Denkers wie dem Kardinal Newman eine außerordentlich interessante Auseinan- dersetzung haben erfahren können.",
        "Wenn ein weniger fortgeschrittener katholischer Theologe gesprochen hät- te, würde er eben das Wesen der ewigen Heilslehre, al- so eine katholische Theologie dargestellt haben."
      ],
      [
        "Dann würden Fragen von ungeheurer Bedeutung aufgetaucht sein, zum Beispiel jene Frage: Was ist nun eigentlich in der katholischen Theologie für den heutigen Menschen gegeben?",
        "In der katholischen Theologie ist ja ohne Zweifel, so wie sie heute auftritt, für das Gegenwartsbewußtsein nichts Lebendes."
      ],
      [
        "Aber sie war einmal etwas Lebendes.",
        "Ihr Inhalt beruht ja durchaus auf dem Ereignis alter geisteswissenschaftlicher, wenn auch atavistischer Er- kenntnisse.",
        "Was in der katholischen Theologie ent- halten ist, sagen wir über das Faktum der Schöpfung, über die Erlösung, über den Inhalt der Trinität, über alle 171 diese Dinge, das sind ja reale Begriffe, das ist etwas, was Inhalt hat; nur ein Inhalt, den das moderne Bewußtsein nicht mehr erfassen kann, sondern ihn in abstrakte, un- verständliche Dogmatik kleidet, oder auch gar nicht kleidet, sondern als unverständliche, trockene Dogmatik hinnimmt."
      ],
      [
        "Es war ja insbesondere die Entwicklung der katholi- schen Theologie im 19.",
        "Jahrhundert so, daß nicht mehr erkannt wurde, was in den Dogmeninhalten enthalten ist.",
        "Dafür lag gerade bei diesem Hochschulkurs in Berlin ein interessantes Erlebnis vor."
      ],
      [
        "Ich hatte am Freitag in meiner Einleitung aus dem unmittelbaren Erleben heraus folgendes gesagt, was Sie ja schon kennen, ich hatte gesagt: Wer das erlebt, was in unserer Naturumgebung ist und in dem, was an diese Naturumgebung sich anschließt, kommt, wenn er nicht irgendwie innerlich verkrüppelt ist, zum Bewußtsein des Vater-Gottes.",
        "Derjenige, der dann während seines Lebens das Ungenügende des Vatergott-Erlebnisses erkennt und eine Art innerer Wiedergeburt erlebt, der kommt zu dem Erleben des Gott-Sohnes, des Sohnes Gottes."
      ],
      [
        "Und auf dieselbe Weise kommt man dann durch ein Weiter- schreiten zu dem Geist-Erlebnis.",
        "Da dachte nun ein protestantischer Privatdozent, Lizentiat Tillich: Aha, da ist ja die Trinität, die muß man konstruieren , und er nannte das eine Konstruktion: Er merkte also gar nichts davon, daß da Erlebnisse zugrunde liegen."
      ],
      [
        "Das war ihm ganz fremd.",
        "Nun, so fremd sind auch jene Erlebnisse dem modernen Bewußtsein des 19.",
        "Jahrhunderts geworden, die den katholischen Dogmen zugrunde liegen.",
        "Diese katholischen Dogmen gehen natürlich ur- sprünglich zurück auf geistige Realitäten, aber man ver- 172 steht nichts mehr davon."
      ],
      [
        "Es sind leere Begriffe gewor- den.",
        "Nun sollte man aber im 19.",
        "Jahrhundert wenigstens wiederum dazu kommen, ein wenig äußerlich beleben zu können, was in der katholischen Theologie lebt.",
        "Sie wissen ja wohl, daß dieser Drang, wenigstens ein bißchen wieder verstehen zu können, was in der katholischen Theologie lebt, ganz besonders unter dem Pontifikat Leos XIII. aufgekommen ist."
      ],
      [
        "Daher dazumal die katho- lische Verordnung, die römische Verordnung für alle katholischen Theologen, zurückzukehren zum Studium der Thomistischen Philosophie, der Philosophie des Thomas von Aquino, weil die ganze spätere Philosophie nicht mehr brauchbar ist, um so etwas zu erfassen, wie es in den katholischen Dogmen liegt.",
        "Alle auf die Thomi- stik folgende Philosophie ist eigentlich nur brauchbar, um das natürliche Dasein zu verstehen, um der Natur- wissenschaft eine Grundlage zu geben, nicht aber um die geistigen Tatsachen zu verstehen, von denen man aller- dings auch auf katholischer Seite nichts weiß, aber die doch in den katholischen Dogmen in einer Zeit formu- liert worden sind, als man noch von diesen geistigen Tatsachen wußte."
      ],
      [
        "Um diese geistigen Tatsachen zu ver- stehen, dazu taugt alle spätere nach-thomistische Philo- sophie nichts mehr.",
        "Als man daher das Bedürfnis emp- fand, wiederum etwas von dem zu verstehen, was in den katholischen Dogmen liegt, forderte man die Erneuerung des Studiums der Thomistik, was ja heute das eigentliche philosophische Bestreben innerhalb des römischen Ka- tholizismus ist."
      ],
      [
        "Dem liegen durchaus historische Reali- täten zugrunde.",
        "Und wenn man vergleicht, was eigentlich notwendig ist, um wiederum ins Geistige hineinzukom- men, so sieht man schon ein, daß natürlich auch die Thomistik nicht genügt, um wieder zu beleben, was in 173 den alten, in Rom erstarrten Dogmen enthalten ist."
      ],
      [
        "Man muß da zu einer ganz anderen Betrachtung kommen.",
        "Bitte, erinnern Sie sich nur an die für einen gegenwär- tigen Literatur-Historiker so gänzlich verdrehte An- schauung, die ich hier, bevor ich von Dornach abgereist bin, in den letzten Vorträgen vorgebracht habe, wo ich mit Hinweggehen über alles, was Raum und Zeit ist, Ihnen dargestellt habe, wie Hamlet ein Schüler von Faust ist, wie Hamlet zehn Jahre lang zu Füßen des Faust gesessen hat; in jenen zehn Jahren, wo Faust seine Schüler an der Nase herumführte, und wie Hamlet einer von denen war, die damals grade und krumm und kreuz und quer an der Nase herumgeführt worden sind."
      ],
      [
        "Solche Zusammenhänge sind natürlich einem gegenwärtigen Literatur-Historiker ein Greuel.",
        "Aber man kann ja heute fast nichts Erhebliches sagen auf geistigem Gebiete, was den offiziellen Vertretern der Wissenschaft nicht ein Greuel wäre."
      ],
      [
        "Es ist heute ja geradezu das Stigma der wirklichen Wahrheit, daß sie den öffentlichen Vertretern der Wissenschaft ein Greuel ist.",
        "Nun, wenn Sie das schon für ein so profanes Gebiet nehmen, dann werden Sie sehen, was wirklich notwen- dig ist, um wiederum zu jener Beweglichkeit des Geistes zu kommen, die eine Grundlage liefern kann für das Erfassen dessen, was in den Dogmen bewahrt ist."
      ],
      [
        "Wie man zurückgehen muß zu einer ganz anderen Seelenver- fassung, um in die Art hineinzukommen, wie man in solchen Dogmen lebte, das zeigt ja gerade der Entwick- lungsgang des Kardinals Newman.",
        "Es ist ja vielleicht heute in Berlin selbstverständlich, daß man bei einem solchen Hochschulkurs nur von protestantischem Standpunkte aus redet und den katho- lischen Standpunkt unberücksichtigt läßt."
      ],
      [
        "Aber ein Bild 174 dessen, was da eigentlich heute waltet, bekommt man natürlich nicht, wenn man nicht auch den katholischen Standpunkt irgendwie zu erörtern in der Lage ist, ins- besondere heute nicht, wo wir wieder notwendig haben, mit unserem Blicke über die ganze Welt hinzuschauen.",
        "Sehen Sie, darüber müssen wir ja heute hinauskom- men, nur Kirchturms-Wissenschaft, Kirchturms-Weltanschauung zu reden. - Kirchturms-Pohtik kennen Sie, aber es gibt auch etwas wie Kirchturms-Weltanschauung."
      ],
      [
        "Sie tritt einem stark entgegen, wenn man so etwas sieht wie zum Beispiel an dem Freitag Abend, wo der Dr.",
        "Theberat über das Thema vorgetragen hat: «Atomi- stische und wirklichkeitsgemäße Betrachtung chemischer Prozesse»."
      ],
      [
        "Das heißt, Dr.",
        "Theberat, der ja nun in unse- rem Forschungsinstitut in Stuttgart angestellt ist, ver- suchte zu zeigen, wie Atomistik verlassen werden muß und wie man eben die Phänomenologie auch in die Chemie hineintragen muß."
      ],
      [
        "Da trat dann in der Debatte Dr.",
        "Kurt Grelling auf.",
        "Ich will jetzt nicht über Dr.",
        "Kurt Grelling sprechen, der ja so ungefähr nach dem Rezepte auftritt: Ja, da wird in der Anthroposophie allerlei gesagt, aber das ist mir alles noch nicht wahrscheinlich."
      ],
      [
        "Sicher aber ist doch, daß 2 + 2 = 4 ist, und man muß sich doch an das halten, was sicher ist: 2 + 2 = 4; das ist sicher. - Das hat er ja schon im vorigen Sommer im Stuttgarter Kursus geltend gemacht und hat dann sogar zwei Uni- versitätslehrer zu Hilfe gezogen, um dieses, daß 2 + 2 = 4 ist, an einem besonderen Abend geltend zu machen.",
        "Dem konnte man natürlich nicht widersprechen."
      ],
      [
        "Ich meine, ich will damit nur symbolisch andeuten, was er sagte, denn 2 + 2 ist ja wirklich 4.",
        "Ich konnte nicht widersprechen.",
        "Ich konnte nicht einmal widersprechen, als er am letzten Freitag, ganz aus dem Zusammenhang 175 herausgerissen, sagte, ich hätte in Stuttgart ja zugegeben, daß 2 + 2 = 4 ist."
      ],
      [
        "Gewiß, ich kann das nicht in Abrede stellen.",
        "Ich meine jetzt nicht gerade 2 + 2 = 4, sondern Dinge, die im ganzen Zusammenhang ebenso wertvoll sind, die er damals vorgebracht hat.",
        "Er sagte dann: Ja, über die Frage, die da vorgebracht wurde, über Phäno- menologie, kann nicht vom Standpunkte der Naturwis- senschaft entschieden werden, sondern nur vom Stand- punkte der Philosophie aus."
      ],
      [
        "Nun, ich will nicht sagen, daß das gerade bloß «Göt- tingisch» ist, aber mindestens ist es heute nicht irgendwie weltmännisch wissenschaftlich gedacht, denn mit einem solchen Satze, daß etwas nicht naturwissenschaftlich, sondern nur philosophisch entschieden werden könne, würde man zum Beispiel in England überhaupt keinen Sinn verbinden können, weil dieser Unterschied etwas ist, was eben Kirchturms-Weltanschauung ist.",
        "Diese Formulierung, die kennt man nur innerhalb gewisser mitteleuropäischer Kreise."
      ],
      [
        "Jedenfalls ist es schon so, daß wir heute, wenn von solchen Fragen die Rede ist, einen weiteren Gesichts- kreis brauchen.",
        "Man kann zum Beispiel unmöglich im- mer weiter von Mitte, West und Ost sprechen."
      ],
      [
        "In den Formulierungen des Programms zum Wiener Kongreß ist ja fortwährend von West und Ost und Mitte die Rede, was ich nicht tadle.",
        "Ich finde es ja recht großgeistig, wenn von West und Ost und Mitte die Rede ist - aber ich meine, man muß dann auch seine Begriffe etwas erwei- tern; sie müssen dann wirklich auch diese Gebiete um- spannen."
      ],
      [
        "Man kann natürlich nicht von einem einge- schränkten Standpunkte aus die Welt umfassen.",
        "So fehlte natürlich [in Berlin bei den Vorträgen über Religion und Theologie] etwas, zum Beispiel in bezug 176 auf die westliche Entwicklung des religiösen Lebens, weil man das Katholische ganz ausgelassen hat, denn dieses westliche religiöse Leben hat gar nichts in sich von dem, was man berührt, wenn man bloß von der evan- gelischen Theologie spricht."
      ],
      [
        "Man kam auch gar nicht darauf zu reden, wie etwa der Puritanismus in England oder die Hochkirche in England oder dergleichen sich entwickelt haben.",
        "Also das alles bringe ich nicht als eine Kritik vor, denn selbstverständlich waren die Dinge, die vorgebracht worden sind, ausgezeichnet."
      ],
      [
        "Aber ich möchte doch im engeren anthroposophischen Kreise über das sprechen, was in Anknüpfung an die ganzen Vorgänge eben hätte gesagt werden müssen.",
        "Und da würde man eben gezeigt haben müssen, wie das gegenwärtige Denken eben gar nicht in der Lage ist, an das heranzukommen, was einmal Quell für den theologischen Inhalt war."
      ],
      [
        "Aber es war so, daß in Berlin keine Brücke zu sehen war zwischen dem, was moderne evangelische Theologie ist, und dem, was nun aus Anthroposophie kommen soll zur Belebung des religiösen Bewußtseins.",
        "Es waren immer nur Hinweise, daß das von der Anthroposophie kommen soll; aber wie es sich gestalten soll, davon war eigentlich im Grunde genommen nicht die Rede."
      ],
      [
        "Das sind Dinge, die Ihnen vielleicht ein Bild geben werden von jenem Ringen auf anthroposophischem Bo- den, das sich gerade in Berlin jetzt in der schönsten Weise zum Ausdruck gebracht hat.",
        "Es zeigte sich ja gerade in Berlin auch an der Teilnahme der verschiedenen Kreise - die Vorträge waren außerordentlich stark besucht, auch die Vormittagsvorträge -, daß durchaus etwas in der anthroposophischen Bewegung lebt, was stark und in- tensiv an das Gegenwartsbewußtsein heranschlägt. 177 Und es wurde von unserer Seite aus ja auch manch- mal nicht gespart in der Schärfe der Ausdrücke, die charakteristisch sein sollten für das, was ist."
      ],
      [
        "Ich erinnere mich zum Beispiel mit einer gewissen inneren Freude daran, wie am Sonnabend dann Dr.",
        "Schubert sprach, der innerhalb des Rahmens «Anthroposophie und Sprach- wissenschaft» auch seinerseits zeigen wollte, wie die Sprachwissenschaft im politischen Leben der Völker und Rassen eine Rolle spielte, und wie er dann in der Debatte temperamentvoll darauf hinweisen wollte, was heute die Sprachwissenschaft ist, und was sie werden muß durch die Anthroposophie."
      ],
      [
        "Es war temperamentvoll, als er dann sagte: Ja, er sei doch in Berlin gewesen, er habe bei den verschiedensten Lehrern Sprachwissenschaft studiert, und dann kam er an die Anthroposophie, um diese Sprachwissenschaft zu beleben; und da ging ihm erst ein Licht auf, da fand er, was die gegenwärtige Sprachwis- senschaft eigentlich ist: ein Misthaufen. - Und da schlug er auf den Tisch.",
        "Also es war nicht gespart worden an temperamentvollen Ausdrücken, um die Gegenwart zu charakterisieren."
      ],
      [
        "Die Gegner haben ja auch nicht gerade - ja, temperamentvoll kann ich eigentlich nicht sagen nun, so sage ich gar nichts!",
        "Die Abendveranstaltungen waren dann so, daß man versuchte, ein Bild von den anthroposophischen Inhalten zu geben."
      ],
      [
        "Es war namentlich diesmal sehr bedeutungs- voll, daß sowohl von Dr.",
        "Stein wie von Dr.",
        "Schwebsch, zwei Lehrern der Waldorfschule, anschauliche Bilder des pädagogischen Wirkens in der Waldorfschule gegeben wurden."
      ],
      [
        "Ich möchte sagen, so zwischen den Zeilen konnte man ja manches Merkwürdige erleben.",
        "Der ganze Kursus schloß dann am Sonntag.",
        "Ich hatte dann nachher am Sonntag noch den Schluß-Abendvortrag 178 zu halten, und die Vormittagsveranstaltungen schlössen mit einer vor einem vollbesetzten Hause gehaltenen Eurythmievorstellung im Deutschen Theater, die einen außerordentlich starken Erfolg hatte."
      ],
      [
        "Ich brauche wohl kaum zu sagen, daß, wenn Ihnen irgendwelche Zeitungsblätter in die Hand kommen soll- ten, Sie das Gegenteil von dem lesen werden, was da gewesen ist.",
        "Aber ein Herr, der zum Beispiel einen Artikel in einem Berliner Blatte geschrieben hat, den manche für einen Artikel pro Anthroposophie ansehen ich will mich darüber nicht äußern! -, der hat dann bei einem ändern großen Blatte angefragt, ob er nun auch einen Artikel über diesen Hochschulkurs schreiben darf."
      ],
      [
        "Man fragte: Pro oder Kontra?",
        "Da sagte er, weil er mein- te, daß sein Artikel Pro ist: Pro.",
        "Da sagte man: Nein, wir nehmen nur Kontra. - Also man kümmert sich nicht darum, was irgend jemand schreibt, sondern man kauft nur Kontra!"
      ],
      [
        "Also Sie werden natürlich keine Vorstellung bekommen von dem, was da gewesen ist, wenn Sie andere Berichte bekommen von außen her.",
        "Schade ist es, daß außer dieser im Deutschen Theater erfolgten Eurythmie-Vorstellung nicht auch noch - außer den kurzen Eurythmie-Vorstellungen am Don- nerstag und Sonntag mehr Eurythmie gepflegt worden ist, denn es hätte vielleicht das nach dem Muster des Stuttgarter anthroposophischen Kongresses dazu führen können, daß unter der Last dieser vollbesetzten Tage die verehrten Anwesenden doch nicht gar so schwer zu tragen gehabt hätten."
      ],
      [
        "Denn ich kann mir schon vorstel- len, daß es recht hart war!",
        "Nehmen Sie zum Beispiel irgendeinen der Tage, so einen Durchschnittstag, wo nicht außerdem noch Sitzungen für eine Anzahl von Leuten gehalten worden sind, da hat derjenige, der alles 179 mitgemacht hat, fünf Vorträge und eine Diskussion ge- hört."
      ],
      [
        "Das ist für einen heutigen Menschen etwas viel, an einem Tage fünf Vorträge und eine Diskussion.",
        "Es waren eigentlich sogar zwei Diskussionen an einem normalen Tage.",
        "Also man hatte Gelegenheit, von 9 Uhr bis 3 Uhr und dann wiederum von 8 Uhr bis etwa 10 1/2 Uhr abends in einem fort in solchen Gedanken zu leben."
      ],
      [
        "Dem wäre natürlich viel besser gedient gewesen, wenn zwischen- durch, wie es in Stuttgart der Fall war, launige Euryth- mievorführungen hätten stattfinden können. - Nun, im Ganzen ist das Ergebnis ein außerordentlich Bedeut- sames. 180 ANHANG Zwei Briefe des Berliner Zweigleiters und Organisators des Hoch- schulkurses Rudolf Meyer an Rudolf Steiner Berlin S.",
        "O. 36, Cottbuser Ufer 25 26."
      ],
      [
        "August 1921 Hochverehrter Herr Dr.",
        "Steiner, darf ich im Namen der Berliner Bewegung die Bitte aussprechen, daß Sie im Anschluß an den von der Konzertdirektion Wolff veranstalteten Vortrag einen oder zwei öffentliche Vorträge halten, die von uns veranstaltet würden?"
      ],
      [
        "Ich glaube, daß durch zwei oder drei große öffentliche Vorträge von Ihnen der Boden für den im nächsten Frühjahr von uns geplanten anthroposophi- schen Hochschulkurs gut vorbereitet wird. - Herr Raether [*], der wie ich Ihnen in diesem Frühjahr in Dornach mitteilte, damals 25 000 M stiftete für eine große eurythmische Vorstellung in Berlin, hat durch sein neuerliches Eintreten für die Verwirkli- chung des Hochschulkurses diesen eigentlich erst ermöglicht.",
        "Er wünscht so wie ich u. alle anderen Freunde, die mit der Seele bei der Bewegung sind, daß dieser Hochschulkursus eine großzügige Veranstaltung wird."
      ],
      [
        "Wir glauben, daß 2 oder mehrere große öffentliche Vorträge von Ihnen jetzt im September das Interesse der Berliner Öffentlichkeit in so weitem Maße erregen würden, daß wir auf eine unseren Plänen entsprechende starke Beteiligung im nächsten März beim Hochschulkurs rechnen können.",
        "Mit den herzlichsten Grüßen an Sie u. die verehrte Frau Doktor Ihr unwandelbar ergebener Rudolf Meyer [* Hans Raether, Lebensdaten unbekannt, zu dieser Zeit Vorstandsmitglied des Rudolf Steiner-Zweiges in Berlin.] 187 Berlin, Sonntag, den 6."
      ],
      [
        "November 1921 Hochverehrter Herr Dr.",
        "Steiner, Die Schwierigkeiten, für den Hochschulkursus im nächsten Frühjahr geeignete Räume zu erhalten, waren zeitweise so stark, daß es manchmal aussah, als würden die Verhältnisse uns zwingen, den Kursus zu vertagen."
      ],
      [
        "Nun stellt sich die Möglichkeit heraus, vom 1. - 15.",
        "März 22 die Berliner Singakademie zu erhalten.",
        "Der eigentliche Hochschulkursus könnte hier sehr gut stattfinden, wenn wir die Singakademie auch nicht für die Abende erhalten können, sondern für die Zeit von 9-3."
      ],
      [
        "Für die Abendveranstaltungen finden wir andere geeignete Räume.",
        "Uns scheint es, daß es besser ist, den Kursus im März 22, wenn auch an 2 Stellen, stattfinden zu lassen, als erst im Jahre 1923 an einer.",
        "Da der Berliner Hochschulkurs von anfang an so gedacht war, daß Sie ihm durch Ihre Vortragstätigkeit u. sonstige Mitwirkung das Schwergewicht u. die Durchschlagskraft geben, so hängt die Möglichkeit, den Kursus in der Zeit vom 1. - 15."
      ],
      [
        "März 22 stattfinden zu lassen, hauptsächlich davon ab, ob Ihre Disposi- tionen Ihnen erlauben, während dieser Zeit in Berlin zu sein.",
        "Darf ich bitten, mir ganz kurz mitzuteilen, ob es Ihnen möglich sein wird, vom 1. - 15."
      ],
      [
        "März 22 in Berlin tätig zu sein, damit wir dann sofort die Singakademie und die anderen Räume mieten.",
        "Ein adressierter Briefumschlag liegt bei.",
        "Herzliche Grüße von unseren Freunden u. mir an Sie u.",
        "Frau Dr."
      ],
      [
        "Ihr stets aufrichtig verbundener Rudolf Meyer 188"
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "PRESSESTIMMEN",
    "paragraphs": [
      "Auszug aus dem Bericht «Der Anthroposophische Hochschulkurs in Berlin» von Ernst Uehli, erschienen in der Zeitschrift «Dreigliederung des sozialen Organismus», Stuttgart, 3. Jg., Nrn. 38 - 40 vom 23., 30.",
      "März und 6. April 1922. «Was die ganze Veranstaltung auszeichnete, war, daß sie von einer lebendig schwingenden Geistigkeit durchdrungen war, die ganz allgemein empfunden wurde und sich in der Frequenz der Einzelvorträge äußerte.",
      "Es war eine Resonanz vorhanden, der sich auch der Skeptiker auf die Dauer nicht entziehen konnte. Daß diese in dem kühlen Großstadtmilieu Berlins sich so stark zur Geltung bringen konnte, darf als ein Zeugnis gelten für die lebendige Kraft, welche von der anthroposophischen Geisteswis- senschaft ausgeht, denn für den genauer Beobachtenden war es klar, daß in dieser Veranstaltung nicht nur ein geistig, sondern auch ein sozial verbindendes Element zur Auswirkung gelangte.",
      "Die Vorträge in der Singakademie begannen morgens um 9 Uhr und dauerten fortlaufend mit kurzer Pause bis nachmittags 3 Uhr. Sie waren so angeordnet, daß jeweilen ein Tag einer bestimmten Wissenschaft gewidmet war.",
      "Rudolf Steiner hielt für jede der behandelten Wissenschaften den einleitenden Vor- trag. Vor dem letzten Vortrag wurde eine Diskussionsstunde eingeschaltet. Leider hatte diese Anordnung den entschiedenen Nachteil, daß die Diskussion nicht genügend fruchtbar gemacht werden konnte, da die Vortragenden meist nicht genügend Zeit hatten, auf Fragen und Einwände mit der nötigen Gründlichkeit zu antworten.",
      "Man konnte angesichts der Gesamtanordnung einige Besorgnis haben für den Besuch des letzten Vortrages. Diese Besorgnis erwies sich jedoch als unbegründet, denn es zeigte sich in der Regel eine Geschlossenheit des Besuches bis zum Schluß der sechsstündigen Tagesveranstaltung.",
      "Und diese Tatsache scheint mir für die geistige Wertung dieses Kurses von besonderer Bedeutung zu sein. [...] Dr. Steiner eröffnete jeden Tag, der einer besonderen Wis- senschaft gewidmet war, mit einem einleitenden Vortrag für die betreffende Wissenschaft.",
      "Man kann in einem einstündigen 189 Vortrage nichts Erschöpfendes sagen über das betreffende Fach- gebiet. Was Dr. Steiner in diesen sieben einleitenden Vorträgen für sieben fachwissenschaftliche Gebiete gab, trug den Charakter des Fresko.",
      "Sie waren großartige Skizzen, aber Skizzen von durchleuchteter Klarheit, von einer ganz sicheren Linienführung, so daß gerade durch eine solche Darstellung die betreffende Wissenschaft im Bilde so erschien, wie sie von anthroposophischer Geisteswissenschaft für die Zukunft gemeint ist. Ebenso wie in der Skizze eines Künstlers sich für den künstlerisch Schauenden das ganze Gemälde offenbart, das erst ausgeführt werden soll, so waren diese Einleitungsvorträge wissenschaftlich-künstleri- sche Skizzen für dasjenige, was für jedes einzelne dieser Wissen- schaftsgebiete als Zukunftsaufgabe zur Ausgestaltung kommen muß, wenn Wissenschaft nicht immer mehr in ein riesiges atomistisches Trümmerfeld zerfallen soll. [...] Gegenüber der tiefen Wirkung, die Rudolf Steiner mit seinen Vorträgen über Anthroposophie wie über Fachwissenschaften im besonderen, vornehmlich in gebildeten, namentlich in Akade- mikerkreisen erzielt hat, was in Berlin ganz offensichtlich der Fall war, ist in der Presse geltend gemacht worden, sie beruhe auf Suggestion.",
      "Wer auch nur ein wenig die menschlich-geistigen Zusammenhänge kennt, der weiß, daß es sich hierbei um Totengräber-Urteile handelt. Von solcher Seite mag auch gegen den vorliegenden Bericht gesagt werden, er sei lediglich subjektiv und persönlich.",
      "Gerade darauf kommt es mir an, meine per- sönlichen Erlebnisse mitzuteilen, und wenn eine gewisse Sorte von Journalisten in den Spalten ihrer Blätter den Großstadtschmutz als ihre persönlichen Erlebnisse über anthroposophische Ver- anstaltungen ablädt, so nehme ich mir das Recht, meine Erleb- nisse dagegenzustellen. Mir trat aus den Vorträgen Rudolf Steiners als tiefstes Erlebnis etwas entgegen, das ich als bezeichnen möchte, als objektive Liebe in dem Sinne, weil ihr ganzer Inhalt sich in einer für alle Menschen gültigen Erkenntnisform gibt.",
      "Hierin erblicke ich den tiefsten Grund der Erfolge Dr. Steiners. Die fachwissenschaftlichen Vorträge der übrigen Redner, die sich an die einleitenden Vorträge Dr. Steiners anschlössen, haben im großen und ganzen ein schönes in sich abgeschlossenes Bild dessen, was Anthroposophie gegenwärtig zur Befruchtung der Wissenschaften beizutragen vermag, gegeben.",
      "Daß man sich 190 hierin noch im Anfang befindet, das wissen die wissenschaftlichen Vertreter der Anthroposophie selbst am allerbesten. Das Ent- scheidende Hegt darin, daß bereits eine stattliche und immer mehr wachsende Zahl von Wissenschaftlern aller Zweige den Mut gefunden hat, die Konsequenzen aus dem wissenschaftlichen Betrieb der Gegenwart zu ziehen und den Anfang zu machen.",
      "Diese Tatsache ist es neben dem eigentlichen Inhalt der Vorträge, welche in Berlin auf viele der besten unter den Zuhörern einen ganz offensichtlichen Eindruck machen konnte. [...] Es lebte in diesen Vorträgen dasjenige, was ein neutraler Diskussionsredner als ein von ihm erlebtes Phänomen hervorhob, es lebte Enthusiasmus in ihnen. Man spürte den gemeinsamen Untergrund, die anthroposophische Geisteswissenschaft, deren Lebensquell in besonders intimer Weise zu vernehmen war an dem pädagogischen Tag, der nach meinem Empfinden einen Höhepunkt dieser Hochschulwoche bildete.",
      "Was hier vertreten wurde als die pädagogischen Methoden der Waldorfschule, wozu der Schlußvortrag des sprachwissenschaftlichen Tages mitgerechnet werden muß, welcher in die Waldorfschulpädagogik einmündete mitsamt der feinsinnigen treffenden Kritik der Experimentalpäd- agogik, das stimmte zu einem schönen Gesamteindruck dessen zusammen, was die Freie Waldorfschule an Bedeutung für das gegenwärtige Zivilisationsleben sich errungen hat. [...] Es sprachen [...] eine ganze Reihe Lehrer der Waldorfschule. Stein gab mit seinem Vortrag ein Bild, wie eine Erzie- hungspsychologie beschaffen sein müsse.",
      "Aber er gab mehr als ein Bild. Im vollen Erleben stehend, stellte er ein an der Wal- dorfschule geübtes Erziehungsideal hin, das den Lehrer als einen der Kinderseele dienenden Menschen zeigt. Fräulein Dr. von Heydebrand sprach gegen Experimentalpädagogik.",
      "Aber man empfand, hier spricht eine Persönlichkeit mit feinstem Verständnis auch für die pädagogischen Irrungen. Sie meisterte ihren Stoff nicht bloß durch Wissen, sondern durch einen überlegenen Humor, durch ein liebevolles Ruhen in ihm.",
      "Ihre Kritik hatte zugleich etwas Menschlich-Versöhnendes. Man empfand, daß man einer im besten Sinne des Wortes kultivierten Seele gegenüberstand. Schwebschs sprühender Vortrag über das Künstlerische in der Pädagogik gab eine Anschauung davon, was Pädagogik sein kann, wenn sie nicht Vorschrift, sondern in jedem Augenblick persönlichste Schöpfung ist und eben dadurch erst 191 wirkenden moralischen Wert für das Kind schafft.",
      "Von innerer Gediegenheit und feinstem persönlichen Empfinden durchleuchtet war der Vortrag Dr. Hahns, der vieles über den Sprachunterricht in der Waldorfschule vermittelte. Man erhielt durch diese Persönlichkeit eine Empfindung für das geistig-soziale Element der Sprache.",
      "Schubert sprach über das Wort. Er gab kulturgeschichtliche Ausblicke über die moralische Anwendung des Wortes. Er hämmerte, formte Sätze, die ganze Apercus enthielten und oft von fesselnder Originalität waren.",
      "Er suchte das Wissensmaterial künstlerisch umzubilden. [...] Der theologische Tag erfreute sich in besonderem Maße eines ausgesprochenen offiziellen Interesses. Das Tagesprogramm, welches den Untergang der Religion in der gegenwärtigen Theologie und die Neubegründung durch Anthroposophie vorsah, war von theologischer Seite als eine Herausforderung seitens der Anthroposophie statt als eine wissenschaftliche Auseinanderset- zung mit der gegenwärtigen Lage in der Theologie aufgefaßt worden.",
      "Steiner sah sich daher veranlaßt, zu erklären, daß er sich seinerseits zu nichts anderem veranlaßt sehen könne, als die ihm gestellte Aufgabe zu erfüllen, das Verhältnis der An- throposophie zur Theolgie darzulegen. In den drei nachfolgenden kritischen Vorträgen wurde allerdings in objektiver Weise die schwere Krisis des religiösen Lebens von drei verschiedenen Gesichtspunkten festgestellt, eine Feststellung, die in der Dis- kussion als zutreffend zugegeben werden mußte.",
      "Und so hatte man das Gefühl, an einem Leichenbegängnis der Theologie teil- genommen zu haben (die schwarzen Röcke der zahlreich er- schienenen Pfarrer erhöhten nur diesen Eindruck). Die Diskus- sion nahm einen völlig unfruchtbaren Verlauf, sie nahm sogar von Seite der Opposition einen peinlich berührenden polemischen Charakter an.",
      "Während von der theologischen Opposition auf die in ihrem Lager vorhandene Frömmigkeit hingewiesen wurde, brachte es fast gleichzeitig ein Theologe fertig, Dr. Steiner eine bewußte Irreführung des Publikums durch seine Vorträge vor- zuwerfen.",
      "Aber auch dieses schlug zum Besten aus. Hatte man durch die Vorträge eine wissenschaftlich-theoretische Darstellung der Krisis in der Theologie erhalten, so wurde sie dadurch zur unmittelbaren konkreten Anschauung gebracht.",
      "Man hörte nicht bloß über die Krisis reden, man erlebte sie unmittelbar. In diesem modernen Konziliumstreit machte das kernhafte, 192 entschiedene Auftreten Dr. Rittelmeyers einen bedeutenden Ein- druck.",
      "Sein Vortrag war zugleich eine Entscheidung, welche zu der lastenden Negation, die der Stoff mit sich brachte, ein erlö- sendes Gegengewicht bildete. [...] Von den vier Abendvorträgen in der Universität, die im Rahmen dieses Kurses abgehalten worden sind, hielt Dr. Geyer aus Nürnberg einen solchen über Anthroposophie und Chri- stentum.",
      "Seine launige Art, wie er sowohl mit der Theologie wie mit sich selber ins Gericht ging, trug ihm reichen Beifall der zahlreichen Zuhörerschaft ein. Sein Verhalten zur Anthroposo- phie ist ein positiv kämpfendes.",
      "Er will mit einem guten Blick auf die anthroposophische Bewegung hinschauen. Und er forderte die Zeitgenossen auf, ein Gleiches zu tun. Schwebsch sprach in geistvoller und zündender Art über . The- berat gab in seinem Vortrage ein feinsinniges Apercu über war keineswegs als eine Herausforderung gemeint, wie es in der allmählich auf- merksam werdenden theologischen Presse aufgefaßt worden; es 195 sollte vielmehr ein vollauf ernstzunehmendes Bekenntnis von den Erneuerungskräften der Anthroposophie und ein beachtunghei- schendes Anerbieten an die theologische Wissenschaft sein.",
      "In seinem Einleitungsvortrag über entwickelte Dr. Steiner, wie der in seinem ganzen geist-leiblichen Organismus gesunde und die geistig-göttliche Wirklichkeit wahrhaft erlebende Mensch zu einer differenzierten religiösen Erfahrung, einem Erleben des Vatergottes, des Christus und des Geistes komme; andererseits sei Atheismus wirkliche Krankheit, den Christus-nicht-finden Schicksal, den Gott-nicht-entdecken Beschränktheit.",
      "Das folgende Referat von Lic. Bock über den zeigte mit seinen methodologisch grundlegenden Ausführungen, daß durch die psychologistische Methode, die durch ihren Rückzug auf das Subjektiv-Seelische immer mehr das Objektiv-Göttliche verliert, aller Glaube an göttliche Offenbarung und alles Be- wußtsein einer geistigen Welt zugrunde geht.",
      "Dann sprach Dr. Rittelmeyer über den . Geistvoll durchleuchtete er die Versuche von Rudolf Otto, Christoph Schrempf und Paul Göhre, die das Göttliche als das bestimmen. Dieses sei aber eine inhaltsleere Bestimmung des Göttlichen, bei der eine lebendige Frömmigkeit und Theologie nicht stehenbleiben dürfe.",
      "Den Gottesglauben neu und besser zu begründen, vermöge die Anthroposophie; nicht durch logische Beweise oder psycholo- gische Erklärungen, sondern durch eine zu eigenem, unmittel- barem Erleben und Erkennen führende Geisteserziehung. Vom redete zuletzt D.",
      "Geyer. Mit umfassender Sachkenntnis führte er durch die Phasen der Geschichte des Christusglaubens und konstatierte ihren gegenwärtigen Stand: auf der einen Seite ist über der rein- historischen Erforschung des geschichtlichen Jesus der geistig- lebendige Christus verloren worden; andererseits über dem abstrakten Christusprinzip der geschichtliche Jesus.",
      "Ein zweiter Vortrag D. Geyers am Samstag Abend schloß die theologischen Darbietungen wirkungsvoll ab. Mit wahrhaft jugendlicher Fri- sche sprach der bejahrte Theologe über . In überaus fesselnder und humorvoller Darstellung schilderte er, daß Anthroposophie und Christentum zunächst wenig miteinander zu tun hätten; denn jene sei Wissenschaft, 196 dieses Religion.",
      "Und doch hätten beide auch wieder viel mitein- ander zu tun, wie ja, nach Naumanns Wort, Frömmigkeit und Weltanschauung zusammengehören wie der Weinstock und die Mauer, die ihn stützt. Zuletzt empfahl er, auch die Anthropo- sophie mit einem anzusehen, hauptsächlich aber, sie praktisch mit ihren Seelenübungen zu erproben.",
      "Die an die theologischen Vorträge sich anschließenden Diskussionen zeig- ten, daß ein wirklich ernstes und eindringendes Verständnis auf seilen der Gegner noch kaum vorhanden ist. Auch die anderen Abende versammelte die Kursteilnehmer zu Vorträgen.",
      "Eine Reihe, die von der Berliner Ortsgruppe des veranstaltet war, wurde in der Universität gehalten. An dieser Stätte wies in seinem Vortrag Dr. Unger die unwissenschaftliche Behandlung der Anthroposophie durch den Berliner Universitätsprofessor Dr.",
      "Max Dessoir mit energischen Worten zurück. An den übrigen vier Abenden redete Dr. Steiner in der Philharmonie. Da eröffnete er die großartige Perspektive auf die künftige Harmonisierung von Wissenschaft, Kunst und Religion durch die Anthroposophie.",
      "Die Geistesgebiete seien verschiedenartige Ausgestaltungen ein und desselben Urphäno- mens; und wie sie vor alters eins waren in den Mysterien, würden sie auch wieder in eine, alsdann höhere, Einheit zurückkehren. Diese wird erreicht durch Aufstieg zu den höheren Erkenntnisarten der Imagination, Inspiration und Intuition.",
      "Des Lebens Inhalt, den die Anthroposophie zu bieten vermag, besteht nicht in einem Fertigen, einer Gabe, die man bloß hinzunehmen braucht; er liegt vielmehr darin, daß man durch innere Aktivität sich Früchte erobern kann, die nicht bloße Denkresultate, sondern Lebens- fähigkeiten sind; im Sinne des Goethe-Spruchs: Mit andringender Herzenswärme redete Steiner am letzten Abend über die Zeitbedürfnisse. Die Anthroposophie schaffe auch gerade den furchtbaren sozialen Krankheitszuständen Heilung durch ihre lebensvollen Ideen und aufbauenden Impulse.",
      "Sie sei kein , wie eine gegnerische Persönlichkeit geäußert, sondern der Wahrweg zur Rettung aus der großen Kulturkrise. Starker, anhaltender Beifall tat kund, wie innerlich angefaßt die Hörerschaft war.",
      "Mehrere eurythmische Aufführungen rundeten den Kursus künstlerisch 197 ab. Die unter schwierigen Verhältnissen veranstalteten Auffüh- rungen fanden bei der unbefangenen Mehrheit ihren verdienten dankbaren Beifall.",
      "Man kann sagen, daß der Berliner Kursus ein voller Erfolg gewesen ist. Konnte man doch von verschiedensten Seiten hören, welchen Eindruck es gemacht, daß hier eine nicht kleine Anzahl von Persönlichkeiten durch den ungewöhnlichen Geistgehalt und die ungemeine innere und äußere Lebendigkeit ihrer Darbietungen eine solche kulturschöpferische Energie vorgeführt.",
      "Gesteigert konnte man diesen Eindruck von Dr. Steiner haben, dessen Reden wahrhaft geistesmächtige Taten waren. So war der Berliner Kursus ein kulturhistorisches Ereignis; findet sich doch eine derartige Veranstaltung heute sonst nirgends.",
      "Daß unsre ge- genwärtige materialistisch-intellektualistische Wissenschaft ihre Ergänzung und Fortbildung finden kann in der aus Geist und Leben erwachsenen Initiations-Wissenschaft der Anthroposo- phie, - davon haben die Teilnehmer des Berliner Hochschulkur- ses einen starken Eindruck und eine zukunftsfrohe Einsicht empfangen.» Auszug aus Heinrich Frick: «Wer hat herausgefordert?», in «Die Christliche Welt», Nr. 13 vom 30. März 1922, S. 226: «Der Andrang von Besuchern war sehr stark.",
      "Besonders die Abendvorträge, aber auch die Morgenstunden, zumal die Päd- agogik und ganz besonders die Theologie erfreuten sich eines Massenbesuches von vielen Hunderten. Man tagte Morgens in der Singakademie.",
      "Schon beim Eintritt bekam man Gelegenheit, an vielen Tischen anthroposophische Literatur zu sehen und zu kaufen. Diese Bücher erweckten zusammen mit den Medikamen- ten aus den chemischen Werken der AG , mit Bildern des Goetheanums und Flugschriften einen ersten Eindruck davon, welche Anregungen auf den verschiedensten Gebieten von der Anthroposophie gegeben werden können.» 198 Auszug aus Heinrich Frick: «Anthroposophle und evangelische Theo- logie», in «Die Christliche Welt», Nr. 17 vom 27.",
      "April 1922, S. 303: «In der Anthroposophle ein Bildungs- und Kultur-Phänomen, aber keine religiöse Bewegung zu sehen, dazu hat mich besonders der Berliner Kursus veranlaßt. Wenn da in acht Tagen so ziemlich alle Wissensgebiete, alle aktuellen Fragen, alle Nöte des moder- nen Menschen vom Valutastand bis zur Gottesfrage hin erörtert wurden, so bestand für das Publikum ein großer Teil des Anreizes in dem enzyklopädischen Charakter der Veranstaltung.",
      "Dieses kompendienartig knappe Universalwissen ist überhaupt für die Bildungshungrigen ein Hauptmotiv, das sie zu Steiner treibt. Schien doch nach dem Programm das Zeitalter Goethes hier erneuert zu werden: aus zersplittertem Spezialistentum heraus zum Ganzen, aus formlosen Teilstücken des Wissens zur orga- nischen Einheit, und das alles sinnvoll gelagert um einen Mittelpunkt: Anthroposophie!» 199"
    ],
    "sentences": [
      [
        "Auszug aus dem Bericht «Der Anthroposophische Hochschulkurs in Berlin» von Ernst Uehli, erschienen in der Zeitschrift «Dreigliederung des sozialen Organismus», Stuttgart, 3.",
        "Jg., Nrn. 38 - 40 vom 23., 30."
      ],
      [
        "März und 6.",
        "April 1922.",
        "«Was die ganze Veranstaltung auszeichnete, war, daß sie von einer lebendig schwingenden Geistigkeit durchdrungen war, die ganz allgemein empfunden wurde und sich in der Frequenz der Einzelvorträge äußerte."
      ],
      [
        "Es war eine Resonanz vorhanden, der sich auch der Skeptiker auf die Dauer nicht entziehen konnte.",
        "Daß diese in dem kühlen Großstadtmilieu Berlins sich so stark zur Geltung bringen konnte, darf als ein Zeugnis gelten für die lebendige Kraft, welche von der anthroposophischen Geisteswis- senschaft ausgeht, denn für den genauer Beobachtenden war es klar, daß in dieser Veranstaltung nicht nur ein geistig, sondern auch ein sozial verbindendes Element zur Auswirkung gelangte."
      ],
      [
        "Die Vorträge in der Singakademie begannen morgens um 9 Uhr und dauerten fortlaufend mit kurzer Pause bis nachmittags 3 Uhr.",
        "Sie waren so angeordnet, daß jeweilen ein Tag einer bestimmten Wissenschaft gewidmet war."
      ],
      [
        "Rudolf Steiner hielt für jede der behandelten Wissenschaften den einleitenden Vor- trag.",
        "Vor dem letzten Vortrag wurde eine Diskussionsstunde eingeschaltet.",
        "Leider hatte diese Anordnung den entschiedenen Nachteil, daß die Diskussion nicht genügend fruchtbar gemacht werden konnte, da die Vortragenden meist nicht genügend Zeit hatten, auf Fragen und Einwände mit der nötigen Gründlichkeit zu antworten."
      ],
      [
        "Man konnte angesichts der Gesamtanordnung einige Besorgnis haben für den Besuch des letzten Vortrages.",
        "Diese Besorgnis erwies sich jedoch als unbegründet, denn es zeigte sich in der Regel eine Geschlossenheit des Besuches bis zum Schluß der sechsstündigen Tagesveranstaltung."
      ],
      [
        "Und diese Tatsache scheint mir für die geistige Wertung dieses Kurses von besonderer Bedeutung zu sein. [...] Dr.",
        "Steiner eröffnete jeden Tag, der einer besonderen Wis- senschaft gewidmet war, mit einem einleitenden Vortrag für die betreffende Wissenschaft."
      ],
      [
        "Man kann in einem einstündigen 189 Vortrage nichts Erschöpfendes sagen über das betreffende Fach- gebiet.",
        "Was Dr.",
        "Steiner in diesen sieben einleitenden Vorträgen für sieben fachwissenschaftliche Gebiete gab, trug den Charakter des Fresko."
      ],
      [
        "Sie waren großartige Skizzen, aber Skizzen von durchleuchteter Klarheit, von einer ganz sicheren Linienführung, so daß gerade durch eine solche Darstellung die betreffende Wissenschaft im Bilde so erschien, wie sie von anthroposophischer Geisteswissenschaft für die Zukunft gemeint ist.",
        "Ebenso wie in der Skizze eines Künstlers sich für den künstlerisch Schauenden das ganze Gemälde offenbart, das erst ausgeführt werden soll, so waren diese Einleitungsvorträge wissenschaftlich-künstleri- sche Skizzen für dasjenige, was für jedes einzelne dieser Wissen- schaftsgebiete als Zukunftsaufgabe zur Ausgestaltung kommen muß, wenn Wissenschaft nicht immer mehr in ein riesiges atomistisches Trümmerfeld zerfallen soll. [...] Gegenüber der tiefen Wirkung, die Rudolf Steiner mit seinen Vorträgen über Anthroposophie wie über Fachwissenschaften im besonderen, vornehmlich in gebildeten, namentlich in Akade- mikerkreisen erzielt hat, was in Berlin ganz offensichtlich der Fall war, ist in der Presse geltend gemacht worden, sie beruhe auf Suggestion."
      ],
      [
        "Wer auch nur ein wenig die menschlich-geistigen Zusammenhänge kennt, der weiß, daß es sich hierbei um Totengräber-Urteile handelt.",
        "Von solcher Seite mag auch gegen den vorliegenden Bericht gesagt werden, er sei lediglich subjektiv und persönlich."
      ],
      [
        "Gerade darauf kommt es mir an, meine per- sönlichen Erlebnisse mitzuteilen, und wenn eine gewisse Sorte von Journalisten in den Spalten ihrer Blätter den Großstadtschmutz als ihre persönlichen Erlebnisse über anthroposophische Ver- anstaltungen ablädt, so nehme ich mir das Recht, meine Erleb- nisse dagegenzustellen.",
        "Mir trat aus den Vorträgen Rudolf Steiners als tiefstes Erlebnis etwas entgegen, das ich als bezeichnen möchte, als objektive Liebe in dem Sinne, weil ihr ganzer Inhalt sich in einer für alle Menschen gültigen Erkenntnisform gibt."
      ],
      [
        "Hierin erblicke ich den tiefsten Grund der Erfolge Dr.",
        "Steiners.",
        "Die fachwissenschaftlichen Vorträge der übrigen Redner, die sich an die einleitenden Vorträge Dr.",
        "Steiners anschlössen, haben im großen und ganzen ein schönes in sich abgeschlossenes Bild dessen, was Anthroposophie gegenwärtig zur Befruchtung der Wissenschaften beizutragen vermag, gegeben."
      ],
      [
        "Daß man sich 190 hierin noch im Anfang befindet, das wissen die wissenschaftlichen Vertreter der Anthroposophie selbst am allerbesten.",
        "Das Ent- scheidende Hegt darin, daß bereits eine stattliche und immer mehr wachsende Zahl von Wissenschaftlern aller Zweige den Mut gefunden hat, die Konsequenzen aus dem wissenschaftlichen Betrieb der Gegenwart zu ziehen und den Anfang zu machen."
      ],
      [
        "Diese Tatsache ist es neben dem eigentlichen Inhalt der Vorträge, welche in Berlin auf viele der besten unter den Zuhörern einen ganz offensichtlichen Eindruck machen konnte. [...] Es lebte in diesen Vorträgen dasjenige, was ein neutraler Diskussionsredner als ein von ihm erlebtes Phänomen hervorhob, es lebte Enthusiasmus in ihnen.",
        "Man spürte den gemeinsamen Untergrund, die anthroposophische Geisteswissenschaft, deren Lebensquell in besonders intimer Weise zu vernehmen war an dem pädagogischen Tag, der nach meinem Empfinden einen Höhepunkt dieser Hochschulwoche bildete."
      ],
      [
        "Was hier vertreten wurde als die pädagogischen Methoden der Waldorfschule, wozu der Schlußvortrag des sprachwissenschaftlichen Tages mitgerechnet werden muß, welcher in die Waldorfschulpädagogik einmündete mitsamt der feinsinnigen treffenden Kritik der Experimentalpäd- agogik, das stimmte zu einem schönen Gesamteindruck dessen zusammen, was die Freie Waldorfschule an Bedeutung für das gegenwärtige Zivilisationsleben sich errungen hat. [...] Es sprachen [...] eine ganze Reihe Lehrer der Waldorfschule.",
        "Stein gab mit seinem Vortrag ein Bild, wie eine Erzie- hungspsychologie beschaffen sein müsse."
      ],
      [
        "Aber er gab mehr als ein Bild.",
        "Im vollen Erleben stehend, stellte er ein an der Wal- dorfschule geübtes Erziehungsideal hin, das den Lehrer als einen der Kinderseele dienenden Menschen zeigt.",
        "Fräulein Dr. von Heydebrand sprach gegen Experimentalpädagogik."
      ],
      [
        "Aber man empfand, hier spricht eine Persönlichkeit mit feinstem Verständnis auch für die pädagogischen Irrungen.",
        "Sie meisterte ihren Stoff nicht bloß durch Wissen, sondern durch einen überlegenen Humor, durch ein liebevolles Ruhen in ihm."
      ],
      [
        "Ihre Kritik hatte zugleich etwas Menschlich-Versöhnendes.",
        "Man empfand, daß man einer im besten Sinne des Wortes kultivierten Seele gegenüberstand.",
        "Schwebschs sprühender Vortrag über das Künstlerische in der Pädagogik gab eine Anschauung davon, was Pädagogik sein kann, wenn sie nicht Vorschrift, sondern in jedem Augenblick persönlichste Schöpfung ist und eben dadurch erst 191 wirkenden moralischen Wert für das Kind schafft."
      ],
      [
        "Von innerer Gediegenheit und feinstem persönlichen Empfinden durchleuchtet war der Vortrag Dr.",
        "Hahns, der vieles über den Sprachunterricht in der Waldorfschule vermittelte.",
        "Man erhielt durch diese Persönlichkeit eine Empfindung für das geistig-soziale Element der Sprache."
      ],
      [
        "Schubert sprach über das Wort.",
        "Er gab kulturgeschichtliche Ausblicke über die moralische Anwendung des Wortes.",
        "Er hämmerte, formte Sätze, die ganze Apercus enthielten und oft von fesselnder Originalität waren."
      ],
      [
        "Er suchte das Wissensmaterial künstlerisch umzubilden. [...] Der theologische Tag erfreute sich in besonderem Maße eines ausgesprochenen offiziellen Interesses.",
        "Das Tagesprogramm, welches den Untergang der Religion in der gegenwärtigen Theologie und die Neubegründung durch Anthroposophie vorsah, war von theologischer Seite als eine Herausforderung seitens der Anthroposophie statt als eine wissenschaftliche Auseinanderset- zung mit der gegenwärtigen Lage in der Theologie aufgefaßt worden."
      ],
      [
        "Steiner sah sich daher veranlaßt, zu erklären, daß er sich seinerseits zu nichts anderem veranlaßt sehen könne, als die ihm gestellte Aufgabe zu erfüllen, das Verhältnis der An- throposophie zur Theolgie darzulegen.",
        "In den drei nachfolgenden kritischen Vorträgen wurde allerdings in objektiver Weise die schwere Krisis des religiösen Lebens von drei verschiedenen Gesichtspunkten festgestellt, eine Feststellung, die in der Dis- kussion als zutreffend zugegeben werden mußte."
      ],
      [
        "Und so hatte man das Gefühl, an einem Leichenbegängnis der Theologie teil- genommen zu haben (die schwarzen Röcke der zahlreich er- schienenen Pfarrer erhöhten nur diesen Eindruck).",
        "Die Diskus- sion nahm einen völlig unfruchtbaren Verlauf, sie nahm sogar von Seite der Opposition einen peinlich berührenden polemischen Charakter an."
      ],
      [
        "Während von der theologischen Opposition auf die in ihrem Lager vorhandene Frömmigkeit hingewiesen wurde, brachte es fast gleichzeitig ein Theologe fertig, Dr.",
        "Steiner eine bewußte Irreführung des Publikums durch seine Vorträge vor- zuwerfen."
      ],
      [
        "Aber auch dieses schlug zum Besten aus.",
        "Hatte man durch die Vorträge eine wissenschaftlich-theoretische Darstellung der Krisis in der Theologie erhalten, so wurde sie dadurch zur unmittelbaren konkreten Anschauung gebracht."
      ],
      [
        "Man hörte nicht bloß über die Krisis reden, man erlebte sie unmittelbar.",
        "In diesem modernen Konziliumstreit machte das kernhafte, 192 entschiedene Auftreten Dr.",
        "Rittelmeyers einen bedeutenden Ein- druck."
      ],
      [
        "Sein Vortrag war zugleich eine Entscheidung, welche zu der lastenden Negation, die der Stoff mit sich brachte, ein erlö- sendes Gegengewicht bildete. [...] Von den vier Abendvorträgen in der Universität, die im Rahmen dieses Kurses abgehalten worden sind, hielt Dr.",
        "Geyer aus Nürnberg einen solchen über Anthroposophie und Chri- stentum."
      ],
      [
        "Seine launige Art, wie er sowohl mit der Theologie wie mit sich selber ins Gericht ging, trug ihm reichen Beifall der zahlreichen Zuhörerschaft ein.",
        "Sein Verhalten zur Anthroposo- phie ist ein positiv kämpfendes."
      ],
      [
        "Er will mit einem guten Blick auf die anthroposophische Bewegung hinschauen.",
        "Und er forderte die Zeitgenossen auf, ein Gleiches zu tun.",
        "Schwebsch sprach in geistvoller und zündender Art über .",
        "The- berat gab in seinem Vortrage ein feinsinniges Apercu über war keineswegs als eine Herausforderung gemeint, wie es in der allmählich auf- merksam werdenden theologischen Presse aufgefaßt worden; es 195 sollte vielmehr ein vollauf ernstzunehmendes Bekenntnis von den Erneuerungskräften der Anthroposophie und ein beachtunghei- schendes Anerbieten an die theologische Wissenschaft sein."
      ],
      [
        "In seinem Einleitungsvortrag über entwickelte Dr.",
        "Steiner, wie der in seinem ganzen geist-leiblichen Organismus gesunde und die geistig-göttliche Wirklichkeit wahrhaft erlebende Mensch zu einer differenzierten religiösen Erfahrung, einem Erleben des Vatergottes, des Christus und des Geistes komme; andererseits sei Atheismus wirkliche Krankheit, den Christus-nicht-finden Schicksal, den Gott-nicht-entdecken Beschränktheit."
      ],
      [
        "Das folgende Referat von Lic.",
        "Bock über den zeigte mit seinen methodologisch grundlegenden Ausführungen, daß durch die psychologistische Methode, die durch ihren Rückzug auf das Subjektiv-Seelische immer mehr das Objektiv-Göttliche verliert, aller Glaube an göttliche Offenbarung und alles Be- wußtsein einer geistigen Welt zugrunde geht."
      ],
      [
        "Dann sprach Dr.",
        "Rittelmeyer über den .",
        "Geistvoll durchleuchtete er die Versuche von Rudolf Otto, Christoph Schrempf und Paul Göhre, die das Göttliche als das bestimmen.",
        "Dieses sei aber eine inhaltsleere Bestimmung des Göttlichen, bei der eine lebendige Frömmigkeit und Theologie nicht stehenbleiben dürfe."
      ],
      [
        "Den Gottesglauben neu und besser zu begründen, vermöge die Anthroposophie; nicht durch logische Beweise oder psycholo- gische Erklärungen, sondern durch eine zu eigenem, unmittel- barem Erleben und Erkennen führende Geisteserziehung.",
        "Vom redete zuletzt D."
      ],
      [
        "Geyer.",
        "Mit umfassender Sachkenntnis führte er durch die Phasen der Geschichte des Christusglaubens und konstatierte ihren gegenwärtigen Stand: auf der einen Seite ist über der rein- historischen Erforschung des geschichtlichen Jesus der geistig- lebendige Christus verloren worden; andererseits über dem abstrakten Christusprinzip der geschichtliche Jesus."
      ],
      [
        "Ein zweiter Vortrag D.",
        "Geyers am Samstag Abend schloß die theologischen Darbietungen wirkungsvoll ab.",
        "Mit wahrhaft jugendlicher Fri- sche sprach der bejahrte Theologe über .",
        "In überaus fesselnder und humorvoller Darstellung schilderte er, daß Anthroposophie und Christentum zunächst wenig miteinander zu tun hätten; denn jene sei Wissenschaft, 196 dieses Religion."
      ],
      [
        "Und doch hätten beide auch wieder viel mitein- ander zu tun, wie ja, nach Naumanns Wort, Frömmigkeit und Weltanschauung zusammengehören wie der Weinstock und die Mauer, die ihn stützt.",
        "Zuletzt empfahl er, auch die Anthropo- sophie mit einem anzusehen, hauptsächlich aber, sie praktisch mit ihren Seelenübungen zu erproben."
      ],
      [
        "Die an die theologischen Vorträge sich anschließenden Diskussionen zeig- ten, daß ein wirklich ernstes und eindringendes Verständnis auf seilen der Gegner noch kaum vorhanden ist.",
        "Auch die anderen Abende versammelte die Kursteilnehmer zu Vorträgen."
      ],
      [
        "Eine Reihe, die von der Berliner Ortsgruppe des veranstaltet war, wurde in der Universität gehalten.",
        "An dieser Stätte wies in seinem Vortrag Dr.",
        "Unger die unwissenschaftliche Behandlung der Anthroposophie durch den Berliner Universitätsprofessor Dr."
      ],
      [
        "Max Dessoir mit energischen Worten zurück.",
        "An den übrigen vier Abenden redete Dr.",
        "Steiner in der Philharmonie.",
        "Da eröffnete er die großartige Perspektive auf die künftige Harmonisierung von Wissenschaft, Kunst und Religion durch die Anthroposophie."
      ],
      [
        "Die Geistesgebiete seien verschiedenartige Ausgestaltungen ein und desselben Urphäno- mens; und wie sie vor alters eins waren in den Mysterien, würden sie auch wieder in eine, alsdann höhere, Einheit zurückkehren.",
        "Diese wird erreicht durch Aufstieg zu den höheren Erkenntnisarten der Imagination, Inspiration und Intuition."
      ],
      [
        "Des Lebens Inhalt, den die Anthroposophie zu bieten vermag, besteht nicht in einem Fertigen, einer Gabe, die man bloß hinzunehmen braucht; er liegt vielmehr darin, daß man durch innere Aktivität sich Früchte erobern kann, die nicht bloße Denkresultate, sondern Lebens- fähigkeiten sind; im Sinne des Goethe-Spruchs: Mit andringender Herzenswärme redete Steiner am letzten Abend über die Zeitbedürfnisse.",
        "Die Anthroposophie schaffe auch gerade den furchtbaren sozialen Krankheitszuständen Heilung durch ihre lebensvollen Ideen und aufbauenden Impulse."
      ],
      [
        "Sie sei kein , wie eine gegnerische Persönlichkeit geäußert, sondern der Wahrweg zur Rettung aus der großen Kulturkrise.",
        "Starker, anhaltender Beifall tat kund, wie innerlich angefaßt die Hörerschaft war."
      ],
      [
        "Mehrere eurythmische Aufführungen rundeten den Kursus künstlerisch 197 ab.",
        "Die unter schwierigen Verhältnissen veranstalteten Auffüh- rungen fanden bei der unbefangenen Mehrheit ihren verdienten dankbaren Beifall."
      ],
      [
        "Man kann sagen, daß der Berliner Kursus ein voller Erfolg gewesen ist.",
        "Konnte man doch von verschiedensten Seiten hören, welchen Eindruck es gemacht, daß hier eine nicht kleine Anzahl von Persönlichkeiten durch den ungewöhnlichen Geistgehalt und die ungemeine innere und äußere Lebendigkeit ihrer Darbietungen eine solche kulturschöpferische Energie vorgeführt."
      ],
      [
        "Gesteigert konnte man diesen Eindruck von Dr.",
        "Steiner haben, dessen Reden wahrhaft geistesmächtige Taten waren.",
        "So war der Berliner Kursus ein kulturhistorisches Ereignis; findet sich doch eine derartige Veranstaltung heute sonst nirgends."
      ],
      [
        "Daß unsre ge- genwärtige materialistisch-intellektualistische Wissenschaft ihre Ergänzung und Fortbildung finden kann in der aus Geist und Leben erwachsenen Initiations-Wissenschaft der Anthroposo- phie, - davon haben die Teilnehmer des Berliner Hochschulkur- ses einen starken Eindruck und eine zukunftsfrohe Einsicht empfangen.» Auszug aus Heinrich Frick: «Wer hat herausgefordert?», in «Die Christliche Welt», Nr. 13 vom 30.",
        "März 1922, S. 226: «Der Andrang von Besuchern war sehr stark."
      ],
      [
        "Besonders die Abendvorträge, aber auch die Morgenstunden, zumal die Päd- agogik und ganz besonders die Theologie erfreuten sich eines Massenbesuches von vielen Hunderten.",
        "Man tagte Morgens in der Singakademie."
      ],
      [
        "Schon beim Eintritt bekam man Gelegenheit, an vielen Tischen anthroposophische Literatur zu sehen und zu kaufen.",
        "Diese Bücher erweckten zusammen mit den Medikamen- ten aus den chemischen Werken der AG , mit Bildern des Goetheanums und Flugschriften einen ersten Eindruck davon, welche Anregungen auf den verschiedensten Gebieten von der Anthroposophie gegeben werden können.» 198 Auszug aus Heinrich Frick: «Anthroposophle und evangelische Theo- logie», in «Die Christliche Welt», Nr. 17 vom 27."
      ],
      [
        "April 1922, S. 303: «In der Anthroposophle ein Bildungs- und Kultur-Phänomen, aber keine religiöse Bewegung zu sehen, dazu hat mich besonders der Berliner Kursus veranlaßt.",
        "Wenn da in acht Tagen so ziemlich alle Wissensgebiete, alle aktuellen Fragen, alle Nöte des moder- nen Menschen vom Valutastand bis zur Gottesfrage hin erörtert wurden, so bestand für das Publikum ein großer Teil des Anreizes in dem enzyklopädischen Charakter der Veranstaltung."
      ],
      [
        "Dieses kompendienartig knappe Universalwissen ist überhaupt für die Bildungshungrigen ein Hauptmotiv, das sie zu Steiner treibt.",
        "Schien doch nach dem Programm das Zeitalter Goethes hier erneuert zu werden: aus zersplittertem Spezialistentum heraus zum Ganzen, aus formlosen Teilstücken des Wissens zur orga- nischen Einheit, und das alles sinnvoll gelagert um einen Mittelpunkt: Anthroposophie!» 199"
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "Hinweise zum Text",
    "paragraphs": [
      "Werke Rudolf Steiners innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer erwähnt. Siehe auch die Übersicht am Schlusß des Bandes. Zu Sehe 15 Emil Du Bois-Reymond, 1818-1896, deutscher Physiologe. - «Über die Grenzen des Naturerkennens.",
      "Vortrag, gehalten in der zweiten öffentlichen Sitzung der 45. Versammlung Deutscher Naturfor- scher und Ärzte zu Leipzig am 14. August 1872», Leipzig 1872. wenn ich mich des Bu Bois-Reymondschen Ausdruckes bedienen darf: Ebenda, S. 2: «Naturerkennen - genauer gesagt naturwissen- schaftliches Erkennen oder Erkennen der Körperwelt mit Hülfe und im Sinne der theoretischen Naturwissenschaft - ist Zurück- führen der Veränderungen in der Körperwelt auf Bewegungen von Atomen, die durch deren von der Zeit unabhängige Centralkräfte bewirkt werden, oder Auflösung der Naturvorgänge in Mechanik der Atome.",
      "Es ist psychologische Erfahrungstatsache, daß, wo solche Auflösung gelingt, unser Causalitätsbedürfniss vorläufig sich befriedigt fühlt.» 16Rudolf Vircbow, 1821-1902, Mediziner und Anthropologe, Profes- sor der pathologischen Anatomie und zeitweise Rektor der König- lichen Friedrich-Wilhelm-Universität in Berlin. - «Die Gründung der Berliner Universität und der Übergang aus dem philosophi- schen in das naturwissenschaftliche Zeitalter», Rede, gehalten am 3. August 1893, Berlin 1893. 17Ernst Mach, 1838-1916, österreichischer Physiker und materialisti- scher Philosoph.",
      "Er war einer der Begründer des Empiriokritizis- mus, erneuerte in der Erkenntnistheorie die Anschauungen Berke- leys und Humes. £5 handelt sich bei Goethe einfach um das, was in seinen Worten liegt: Siehe «J. Goethe: Naturwissenschaftliche Schriften», mit Einleitungen, Fußnoten und Erläuterungen im Text herausgegeben von Rudolf Steiner; photomechanischer Nachdruck nach der Erstauflage in «Kürschners Deutsche National-Litteratur» (1884 - 1897), 5 Bände, GA 1a-e; Bd. 5, GA 1e, «Sprüche in Prosa», 1.",
      "Abt.: «Das Erkennen», S. 376: «Das Höchste wäre, zu begreifen, daß alles Faktische schon Theorie ist. Die Bläue des Himmels offenbart uns das Grundgesetz der Chromatik. Man suche nur nichts hinter den Phänomenen; sie selbst sind die Lehre.» Goethe kam ja auf diesem Wege zur Statuierung dessen, was er «Urphänomen» nannte: Ebenda, Bd. 3, GA 2c, 2.",
      "Abt.: «Physische 203 Farben», X. «Dioptrische Farben. Der ersten Klasse», S. 135, § 150f. und S. 141f., § 174-177. Zu § 175 fügte Rudolf Steiner in einer Fußnote folgendes bei (S.141): «Hier spricht Goethe seine Ansicht über die eigentliche Aufgabe der Naturwissenschaft aus.",
      "Was wir unmittelbar in der Natur wahrnehmen, sind Phänomene, die von den mannigfaltigsten Bedingungen abhängen. Wenn wir irgend eine oder mehrere von diesen Bedingungen ändern, so ändert sich auch das Phänomen.",
      "Es wird sich nun darum handeln, festzustellen, wann diese Änderung eine untergeordnete, nebensächliche und wann eine durchgreifende ist. Alle jene Phänomene, die durch eine Änderung der Bedingungen sich nur unwesentlich ändern wird und einen verwandten Zug zeigen, weisen uns auf ein Grund- oder Urphänomen hin, das ihnen allen zu Grund liegt und in dem sich ein Naturgesetz ausspricht.",
      "Aufgabe des Naturforschers wird es also sein, eine solche Reihe von Phänomenen nebeneinanderzustel- len, die immer nur durch eine Änderung der Bedingungen Modi- fikationen einer Grunderscheinung sind. Diese Grunderscheinung aber ist das objektive Naturgesetz.",
      "Keine Naturerklärung kann als solche über die Urphänomene hinausgehen. Es ist ein großer Irrtum, wenn man glaubt, die Urphänomene beweisen oder weiter erklären zu können. Wenn es selbst gelänge, irgendwo in der Welt das Atom nachzuweisen, so wäre die Wirkung des Atoms auf das Atom doch auch durch nichts anderes auszusprechen als durch ein Urphänomen.",
      "Man sollte daher die tiefsinnige Erfassung der Natur durch Goethe nicht fortwährend als Dilettantismus ansehen, während sie sich von der modernen Naturwissenschaft gerade durch die streng philosophische Begriffsfassung und Methode auszeichnet. Auch die Philosophie kann nicht über die Urphäno- mene hinausgehen; sie hat nur die Aufgabe, die durch die Naturforschung festgestellten Urphänomene in ihrer ideellen Folge aus einander zu entwickeln.",
      "Während der Naturforscher die Phänomene nebeneinanderstellt, damit sich in ihnen das Urphäno- men ausspricht, stellt der Philosoph die Urphänomene neben einander, damit sich darinnen die Naturideen aussprechen.» - Siehe ferner Rudolf Steiner in Bd. 2, GA Ib, Kap. «Verhältnis der Goetheschen Denkweise zu anderen Ansichten», S.",
      "LXI; Bd. 3, GA Ic, Kap. «Einleitung», 2. «Das Urphänomen», S. X ff.; Bd. 4, G A Id, Kap. «Einleitung», 3., S. VI ff. (In den «Einleitungen zu Goethes Naturwissenschaftlichen Schriften. Zugleich eine Grundlegung der Geisteswissenschaft (Anthroposophie)», GA l, entsprechen diese Stellen den S. 226f., 266ff., 311ff.) 17 Satz ..., den ich in den 80er Jahren des vorigen Jahrhunderts ausgesprochen habe: In «J.",
      "Goethe: Naturwissenschaftliche Schriften» (siehe den 2. Hinweis zu S. 17), Bd. l, GA l a, S. LXXIII; bzw. in «Einleitungen zu Goethes Naturwissenschaftlichen Schrif- 204 ten», GA l, S. 107: «Goethe ist der Kopernikus und Kepler der organischen Welt.» 18 Nikolaus Kopernikus, 1473-1543, Astronom, Mathematiker, Arzt, Jurist, Humanist und Domherr.",
      "Begründer des heliozentrischen Weltbildes. Johannes Kepler: Siehe Hinweis zu S. 61. der Kantsche Satz: Siehe «Metaphysische Anfangsgründe der Na- turwissenschaft», 1786, in «Immanuel Kants sämtliche Werke», Leipzig 1897, Bd. 4, Vorrede, S. 360, wörtlich: «Ich behaupte aber, daß in jeder besonderen Naturlehre nur so viel eigentliche Wissenschaft angetroffen werden könne, als darin Mathematik anzutreffen ist.» 19 Zuletzt sagte er sich: «Das Causalgesetz ist ... hinreichend charak- terisirt, wenn man sagt, es setzte eine Abhängigkeit der Erschei- nungen von einander voraus.",
      "Gewisse müssige Fragen, z.B. ob die Ursache der Wirkung vorausgehe oder gleichzeitig sei, verschwinden damit von selbst.» - «Nennen wir die Gesammtheit der Erschei- nungen, von denen eine Erscheinung a als abhängig betrachtet werden kann, die Ursache von oc. Wenn diese Gesammtheit gegeben ist, so ist a bestimmt und zwar eindeutig bestimmt.",
      "Man kann also das Causalgesetz auch m der Form ausdrücken: und 1903-1908», GA 34. 82 «Die Philosophie der Freiheit»: Rudolf Steiner: «Die Philosophie der Freiheit. Grundzüge einer modernen Weltanschauung - Seeli- sche Beobachtungsresultate nach naturwissenschaftlicher Metho- de» (1894), GA 4. 89 Jugendbewegung: Um 1900 in Deutschland entstandene Protestbe- wegung junger Menschen, die sich gegen traditionelle bürgerliche Auffassungen wendete und nach ihr wesensgemäßen Lebensformen suchte (Wandervogel etc.).",
      "Nach dem Weltkrieg 1914 zer- splitterte die Jugendbewegung nach und nach in einzelne «Bünde». 96 in meinen «Kernpunkten ...»: Rudolf Steiner: «Die Kernpunkte der sozialen Frage in den Lebensnotwendigkeiten der Gegenwart und Zukunft» (1919), GA 23. 99 Versailler Vertrag: Dieser Friedensvertrag zwischen den Alliierten und dem Deutschen Reich wurde am 28. Juni 1919 unterzeichnet und trat am 10.",
      "Januar 1920 in Kraft. 100 Theoretiker ... allerlei Diskussionen: Siehe z. B. die Zeitschrift «Tribüne. Halbmonatsschrift für soziale Verständigung», Tübin- gen, die ihre 1. Nummer (Juni oder Juli 1919) der Diskussion über Rudolf Steiners Dreigliederungsidee widmete.",
      "Die betreffenden Aufsätze sind abgedruckt in den «Beiträgen zur Rudolf Steiner Gesamtausgabe», Nr. 106, Dornach, Ostern 1991. 213 101 Es kam das ganze furchtbare Valuta-Elend: Die deutsche Währung wurde nach dem 1. Weltkrieg durch eine sich ständig steigernde Inflation (1923 l Goldmark = l Billion) völlig entwertet. mein «Aufruf an das deutsche Volk ...»: Dieser Aufruf «An das deutsche Volk und an die Kulturwelt», von Rudolf Steiner verfaßt und von einer Anzahl bekannter Persönlichkeiten des öffentlichen Lebens unterzeichnet, wurde im März 1919 als Flugblatt gedruckt und weit verbreitet. - Abgedruckt in «Aufsätze über die Drei- gliederung des sozialen Organismus und zur Zeitlage 1915-1921», GA 24, sowie als Anhang in den «Kernpunkten» (siehe Hinweis zu S. 96). 102was ich wiederholt am Schlüsse von Vorträgen, die ich im Anschlüsse an die «Kernpunkte» hielt, damals gerufen habe: Siehe Vortrags- zyklus «Neugestaltung des sozialen Organismus» (1919), GA 330. 103ein Artikel: Nicht bekannt.",
      "David Lloyd George, 1863-1945, 1916 englischer Minister- präsident. Vortrage, den ich hier zuletzt in der Philharmonie gehalten habe: Bezieht sich auf den öffentlichen Vortrag «Anthroposophie in ihrem Wissenschaftscharakter», den Rudolf Steiner am 7.",
      "März 1922 im weiteren Rahmen dieses Hochschulkurses hielt (noch nicht veröffentlicht). Das wirtschaftliche Leben hat sich zunächst: Siehe hierzu die ausführlichere Darstellung in den Vorträgen vom 26., 28. und 29.",
      "August 1922 in «Die geistig-seelischen Grundkräfte der Erzie- hungskunst. Spirituelle Werte in Erziehung und sozialem Leben», GA 305. 106 Adam Smith, 1723-1790, englischer Nationalökonom und Philo- soph.",
      "Hauptwerk: «An Inquiry into the Nature and Causes of the Wealth of Nations», 4 Bände, 1776. Deutsch von Max Stirner: «Untersuchungen über die Natur und die Ursache des Wohlstandes der Nationen», 1846/47.",
      "Karl Marx, 1818-1883, Begründer des wissenschaftlichen Sozialis- mus und des historischen Materialismus. Hauptwerke: «Zur Kritik der politischen Ökonomie», 1859, und «Das Kapital. Kritik der politischen Ökonomie», 1867/94. 107 David Ricardo, 1772-1823, englischer Nationalökonom, Schüler von Adam Smith, Lehrer von Karl Marx.",
      "John Stuart Mill: Siehe Hinweis zu S. 58. 214 108die sogenannten «Vierzehn Punkte» Woodrow Wilsons: Woodrow Wilson (1856-1924), amerikanischer Präsident von 1912-1920, stellte 1918 dem amerikanischen Kongreß sein Programm für ei- nen Weltfrieden vor, bekannt als die «Vierzehn Punkte». Dieses Programm wurde im Versailler Vertrag 1919 nicht verwirklicht.",
      "Siehe «Die Reden Woodrow Wilsons», englisch und deutsch, Der Freie Verlag Bern, Bern 1919. 109Im Jahre 1917 versuchte ich: Bereits im Jahre 1917 verfaßte Ru- dolf Steiner nach Gesprächen mit Graf Otto Lerchenfeld und Graf Ludwig Polzer-Hoditz zwei Memoranden, in denen er zu grundlegenden politischen Fragen angesichts der damaligen Situa- tion Stellung nahm. Die beiden genannten Persönlichkeiten wand- ten sich mit diesen Memoranden an einflußreiche Politiker, so u.a. an den deutschen Staatssekretär Kühlmann und an Arthur Polzer- Hoditz, den Kabinettchef Kaiser Karls von Österreich.",
      "Die Me- moranden wurden erstmals veröffentlicht in Roman Boos: «Rudolf Steiner während des Weltkrieges», Dornach 1933. Innerhalb der Gesamtausgabe siehe «Aufsätze über die Dreigliederung des sozialen Organismus und zur Zeitlage 1915-1921», GA 24. 110fast jeden Nachmittag nach zwei Uhr: Vgl. hierzu «Mein Le- bensgang», GA 28, Kap.",
      "VIII, S. 148f. 111die alten Stände: Die Formulierung «Nährstand, Wehrstand, Lehrstand» stammt von Erasmus Alberus (1500-1553), ähnlich auch Luther; sie faßt das von Plato in der «Politeia» über die Stände Gesagte zusammen; siehe den «phönikischen Mythos», wonach Gott den Herrschenden (Weisen) bei der Geburt Gold, ihren Beihelfern, den Wächtern, Silber, den Bauern und Handwerkern aber Eisen und Erz beigemischt habe («Politeia» III. Buch, 414ff.",
      "St.). Siehe hierzu auch Vincenz Knauer: «Die Hauptprobleme der Philosophie», Wien und Leipzig 1892. Das Buch befindet sich in der Bibliothek Rudolf Steiners. Dort heißt es in den Vorlesungen über Plato (S. 124): «Wie sich das Seelische im einzelnen Menschen in das Vernünftige, Irascible und Concupiscible gliedert, so finden sich im Staate drei Stände, die wir einer uns geläufigen Redeweise ganz entsprechend als Lehr-, Nähr- und Wehrstand bezeichnen können.» 114 wie ja der natürliche Organismus auch unter dem Einfluß seiner relativen Dreigliederung: Vgl.",
      "Rudolf Steiner: «Von Seelenrätseln» (1917), GA 21, Kap. «Die physischen und die geistigen Abhängig- keiten der Menschen-Wesenheit». Dort wird die Dreigliedrigkeit der Seele durch ihr Denken, Fühlen und Wollen dargestellt.",
      "Zu Begriffen wie Arbeit und Kapital siehe u.a. Rudolf Steiners Ausführungen im Zyklus «Nationalökonomischer Kurs. Aufgaben 215 einer neuen Wirtschaftswissenschaft, Band I» (Dornach 1922), GA 340, Stichwortregister. 118 Zum «Theologentag» des Berliner Hochschulkurses siehe die Be- richte von Ernst Uehli und Eberhard Kurras im Anhang, S. 189ff. und 194ff..",
      "In dieser Zeitungsnotiz steht: In der Wochenschrift «Die Christ- liche Welt», Marburg, 36. Jg., Nr. 9, 2. März 1922, S. 157f., erschien folgende Notiz: «[...] Diese Veranstaltung am Freitag ist nun eine unzweideutige Herausforderung Steiners und seiner Anhänger an die heutigen Theologen.",
      "Ich sage das ohne jeden Vorwurf. Denn theologische Wissenschaft ist so wenig sakrosankt wie irgend eine andre. Und wie gern wir sie (und uns mit) der Kritik unterwerfen, wissen unsre Leser. Es weiß es vor allem auch Rittelmeyer [...] So ist auch der Waffengang der Steinergruppe willkommen.",
      "Nur wird eben der Handschuh aufgehoben werden müssen. Bisher haben wir unserseits uns am Für und Wider genügen lassen [...] Die Männer haben recht, es gibt da auf die Dauer keine Neutralität, und sie wollen uns eine Schlacht liefern, die sie entweder gewinnen oder verlieren.",
      "Ich meinerseits kann nur wünschen, daß diese Tagung wirklich ein entscheidendes Ergebnis zeitigt. Und wäre es eben nur dies: ob wir Steiner alle ernstlich studieren müssen oder nicht [...] Wir sind daran mehr interessiert als andre Gruppen innerhalb der heutigen Theologie, weil Geyer und Rittelmeyer zu unsern aner- kannten und geschätztesten Freunden gehören [...]» (D.",
      "Rade). - Heinrich Frick, Berichterstatter der «Christlichen Welt», schrieb dazu in Nr. 13 vom 30. März 1922, S. 227: «Ich habe alsbald privatim Dr. Rittelmeyer und öffentlich zu Beginn der Aussprache (Dr.",
      "R. erteilte mir freundlichst als erstem Redner das Wort zu meiner Erklärung) dargelegt, daß der Ausdruck in der C[hristhchen] W[elt] nicht gemeint gewesen sei als auf eine bestimmte Person im Sinne eines ethischen Vorwurfes gerichtet (denn Niemand von uns wußte ja, wer eigentlich das Thema formuliert hatte), sondern daß die Formulierung selbst (rein sachlich ihr Wortlaut) als Herausforderung empfunden werden mußte. Ich erinnerte daran, daß bei ruhiger Lektüre des Programms es auffallen müsse, daß an keinem Tage so scharf eine ganz bestimmte Größe nicht nur genannt, sondern zugleich bewertet wird wie gerade die Theologie, von der doch dasteht: und dann dreimal wiederholt das Stichwort Untergang - Untergang - Untergang> in einem -Ismus!",
      "Das sei doch, ganz menschlich genommen, eine , und ich bäte die Zuhörer, doch ja bei sich das Mißverständnis abzuwehren, als ob bei der Schriftleitung der CW eine Animosität gegen die Anthroposophie vorläge [...] 216 Dr. Rittelmeyer erklärte demgegenüber privatim und öffentlich, er selbst habe, als er das Thema formulierte, nicht an eine gedacht, sondern nur an eine ernste Frage, diese allerdings mit allem Nachdruck den Theologen ins Gewissen schieben wollen.» 120experimentelle Psychologie: Bezieht sich auf eine Richtung der Psychologie, die v.a. von Forschern wie Wundt, Stumpf, Lange, James, Ziehen, Külpe, Ebbinghaus, G.E.Müller, Martius, Stern und Neumann vertreten wurde. 121Ernst Haeckel: Siehe Hinweis zu S. 43.",
      "«Es ist nichts im Verstände, was nicht vorher in den Sinnen ist»: «Nihil est in intellectu, quod non fuerit in sensu.» In dieser Formulierung findet sich der Satz erst bei Thomas von Aquino (Quaestiones de veritate II, 3. Coloniae 1475), ähnlich formuliert auch schon bei Cicero (De finibus I, 19); jedoch entspricht er den Ausführungen in Aristoteles' Schrift «De anima».",
      "Siehe besonders Buch 3, Kap. 8: «Da es aber außer den empfundenen Größen (nämlich durch Sinnesempfindung), wie es scheint, kein Ding gibt, das abgetrennt für sich existierte, so ist in den empfundenen Formen auch das Gedachtwerdende, das durch Abstraktion Ge- sagte, und alle Beschaffenheit und Zustände des Empfundenen. Und deshalb kann man, wenn man nichts empfindet, auch nichts lernen, noch verstehen.» (Übersetzt von F.",
      "Kreuz). der Leibnizsche Satz: «Nihil est in intellectu, quod non fuerit in sensu, nisi ipse intellectus». Siehe Gottfried Wilhelm Leibniz (1646 bis 1716): «Neue Abhandlungen über den menschlichen Verstand», Buch II, Kap.",
      "I, (Theophilus): «Man wird mir jenes von den Philosophen anerkannte Axiom entgegenhalten, daß nichts in der Seele ist, das nicht von den Sinnen stammt. Aber man muß die Seele selbst und ihre Affektionen davon ausnehmen.",
      "Nihil est in intel- lectu, quod non fuerit in sensu, excipe: nisi intellectus ipse. Die Seele schließt in sich das Sein, die Substanz, das Eine, das Gleiche, die Ursache, die Perzeption, das vernünftige Denken und viele andere Begriffe, die die Sinne nicht geben können.» - Siehe dazu auch R.",
      "Steiners Vortrag vom 17. September 1915 in «Der Wert des Den- kens für eine den Menschen befriedigende Erkenntnis. Das Verhält- nis der Geisteswissenschaft zur Naturwissenschaft», GA 164. 123 wenn mir Dinge gesagt wurden, wie zum Beispiel von einer heute auch hier anwesenden sehr verehrten Persönlichkeit: Friedrich Rittelmeyer (1872-1938), war protestantischer Geistlicher, von 1902 ein bekannter Prediger in Nürnberg, dann an der «Neuen Kirche» in Berlin, und Verfasser theologischer Schriften. 217 Er stand seit 1911 in Verbindung mit Rudolf Steiner («Meine Lebensbegegnung mit Rudolf Steiner», Stuttgart 1928) und gab 1921 das Sammelwerk «Vom Lebenswerk Rudolf Steiners» heraus.",
      "Er leitete den hier vorliegenden «Berliner Hochschulkurs» und war Mitbegründer und erster Erzoberlenker der im Herbst 1922 begründeten «Christengemeinschaft, Bewegung für religiöse Er- neuerung»; von 1923 an auch im Vorstand der Deutschen An- throposophischen Gesellschaft. Eine kurze Biographie Friedrich Rittelmeyers ist enthalten in Rudolf Gädekes «Die Gründer der Christengemeinschaft», Dornach 1992. - Rittelmeyer hatte sich dahingehend auch in seinem Aufsatz «Johannes Müller und Rudolf Steiner» in der Zeitschrift «Die Christliche Welt», Nr. 22/23, 30.",
      "Mai 1918, geäußert. Auf eine Beschuldigung Müllers, Rudolf Steiner mache «aus der okkulten Welt eine Sensation für die Neugier und Lüsternheit der abergläubischen Instinkte der Men- schen» erwiderte Rittelmeyer dort (S. 215, Fußnote): «Weder die Themata noch die Vorträge selbst haben je das Geringste von solcher Spekulation enthalten.",
      "Steiner mutet insbesondere den Hörern der öffentlichen Vorträge meist eine geistige Anstrengung zu, die alle nicht sehr ernsthaften Hörer bald wieder abschreckt, und macht ihrer Neugier und Sensationslüsternheit kein Zuge- ständnis [...]». 129 Vater-Erlehnis: Vgl. hierzu z. B. die Vorträge vom 20.",
      "Februar und 13. März 1917 in «Bausteine zu einer Erkenntnis des Mysteriums von Golgatha. Kosmische und menschliche Metamorphose», GA 175, und «Wie finde ich den Christus?» vom 16. Oktober 1918 in «Der Tod als Lebenswandlung», GA 182.",
      "Was ich gestern gesagt habe über das Ausbilden des Urteils: Bezieht sich auf den öffentlichen Abendvortrag «Anthroposophie als Lebensinhalt», den Rudolf Steiner am 9. März 1922 anläßlich des Hochschulkurses hielt (noch nicht veröffentlicht). 130 Wladimir Solowjew: Siehe u.a. seine «Zwölf Vorlesungen über das Gottmenschentum», Stuttgart 1921/22. 133«Ich bin bei Euch alle Tage bis an das Ende der Welt»: Matth. 28, 20. 134Friedrich Nietzsche, 1844-1900, Philosoph.",
      "In dem Buche von Friedrich Nietzsches Freund Overbeck: Franz Overbeck (1837-1905), Professor der Theologie in Basel, Freund Friedrich Nietzsches. - «Über die Christlichkeit unserer heutigen Theologie», 1873. 135 Johannes Scotus Erigena, 810-877, irischer Philosoph, Vorläufer der scholastischen Philosophie. 218 135Thomas von Aquino, 1225-1274, christlicher Kirchenlehrer, Philo- soph und Scholastiker. 1323 heilig gesprochen. 136Schon vor vielen Jahren hielt ich einmal in einer süddeutschen Stadt ... einen Vortrag über «Bibel und Weisheit»: In Colmar im Jahr 1905. Eine Nachschrift liegt nicht vor.",
      "Über das Thema «Bibel und Weisheit» hat Rudolf Steiner an verschiedenen Orten gesprochen. Gedruckt sind die Berliner Vorträge vom 12. und 14. November 1908 in «Wo und wie findet man den Geist?», GA 57; Einzelaus- gabe Dornach 1993. 138 Waldorfschule: Siehe hierzu den Vortrag «Anthroposophie und Erziehungswissenschaft» in diesem Band. 140Bei einem kurzen Kurse: Rudolf Steiner: «Geisteswissenschaftliche Sprachbetrachtungen.",
      "Eine Anregung für Erzieher» (6 Vorträge, Stuttgart 1919/1920), GA 229. 141Ich habe zu Weihnachten in Dornach am Goetheanum einen Vortragszyklus zu halten gehabt: «Die gesunde Entwickelung des Menschenwesens. Eine Einführung in die anthroposophische Päd- agogik und Didaktik» («Weihnachtskurs für Lehrer», 16 Vorträge und 3 Fragenbeantwortungen, Dornach 1921/22), GA 303. 142in einem dieser Vorträge: Ebenda, Vortrag vom 7.",
      "Januar 1922: «Die ethische und die religiöse Erziehung im besonderen». gestern: Bei dem Vortrag «Anthroposophie und Theologie». 143 Rittelmeyer hat ... geantwortet mit dem Vergleich zwischen dem Kopf und dem Buch: Zu Friedrich Rittelmeyer siehe den Hinweis zu S. 123. - Vermutlich hatte Rittelmeyer in der Diskussion den bekannten Aphorismus Georg Christoph Lichtenbergs zitiert: «Wenn ein Buch und ein Kopf zusammenstoßen und es klingt hohl, ist das allemal im Buch?» 148 Ich habe jene eine große Umwandlung hier wiederholt charakteri- siert: Siehe u.a. folgende Berliner Vorträge: 26. Januar 1911 in «Antworten der Geisteswissenschaft auf die großen Fragen des Daseins», GA 60; 15.",
      "Februar 1912 in «Menschengeschichte im Lichte der Geistesforschung», GA 61; und 13. Februar 1913 in «Ergebnisse der Geisteswissenschaft», GA 62. 155 Wilhelm Wundt, 1832-1920, Arzt, Philosoph und Psychologe, Professor in Heidelberg, Zürich und Leipzig. - Siehe seine «Völkerpsychologie.",
      "Eine Untersuchung der Entwicklungsgesetze von Sprache, Mythus und Sitte», 1. Band: «Die Sprache», 1. Teil, Leipzig 1900; Kap. 9: «Der Ursprung der Sprache», I. «Allgemeine Standpunkte» und II. «Kritische Übersicht der vier Haupttheo- rien», S. 584-603. 219 155gestern: Siehe den Vortrag «Anthroposophie und Theologie» in diesem Band. 156Christian Geyer, 1862-1929, evangelischer Theologe, Hauptpredi- ger an der Sebalduskirche in Nürnberg. - Geyer hatte als Vor- tragsthema «Der Untergang des Christentums in Historismus».",
      "Seine Ausführungen sind den Herausgebern nicht bekannt. 159 Eurythmievorstellung im Deutschen Theater: Am Sonntag, den 12. März, fand um 11.00 Uhr eine Eurythmievorstellung statt. Von den einleitenden Worten, die Rudolf Steiner hierzu sprach, ist keine Nachschrift vorhanden. 164Hegel hat ja bereits in seiner Philosophie ... gesagt: Eventuell handelt es sich hier um einen Hör- oder Ubertragungsfehler des Stenographen. 165Emil Leinbas, 1878-1967, Mitbegründer und später Generaldi- rektor der «Kommender Tag AG», Stuttgart.",
      "Ab Februar 1923 im Vorstand der Anthroposophischen Gesellschaft in Deutschland. 166Emil Bock, 1895-1959, Lic. theol., im Herbst 1922 Mitbegründer und Oberlenker der Christengemeinschaft, ab 1938 deren Erz- oberlenker. Zu seiner Biographie siehe «Die Gründer der Chri- stengemeinschaft» von Rudolf F.",
      "Gädeke, Dornach 1992, und Gunhild Kacer-Bock: «Emil Bock. Leben und Werk», Stuttgart 1993. «Der Untergang der Religion ... »: Rudolf Steiner gibt die Titel hier frei wieder. 169 ein Privatdozent: Paul Tillich, 1886-1965, war zur damaligen Zeit Dozent an der Theologischen Fakultät in Berlin, ab 1924 Professor für Religionswissenschaft und Sozialphilosophie u.a. in Leipzig, Dresden, Frankfurt.",
      "Tillich emigrierte 1933 nach Amerika, wo er zum führenden protestantischen Theologen der USA wurde. Siehe hierzu den Bericht «Wer hat ?» von Heinrich Frick, in: «Die Christliche Welt», 36. Jg., Nr. 13, 30.",
      "März 1922, S. 225 ff. ein Pfarrer: Carl-Günther Schweitzer, 1889-1965. 1921 gründete Schweitzer die apologetische Zentrale, u.a. zur Auseinandersetzung der evangelischen Theologie mit Geistesströmungen der damaligen Zeit. Gott sei eben das Unbedingte, das überall durchbricht: In einem Aufsatz «Anthroposophie und evangelische Theologie», veröffent- licht in der Zeitschrift «Die Christliche Welt», Nr. 17, vom 27.",
      "April 1922, schreibt Heinrich Frick hierzu: 220 «Als intellektualistisch empfinde ich überhaupt die Denkungs- weise [der Anthroposophen], -wie sie aus den meisten Vorträgen des Kursus sprach. Was heißt z.B.",
      "Welten? Der Komparativ und das Wort selbst sind aus räumlicher Anschauung genommen. Ein großer Teil unsrer Begriffe entstammt ja räumlichen Bezie- hungen. Nun können wir auch vom Unräumlichen nicht anders reden als in solchen Begriffen; aber es liegt darin die große Gefahr, daß wir den Begriff und das Gemeinte nicht scharf genug aus- einander halten.",
      "Der Begriff färbt ab, und wenn man lang genug räumliche Begriffe für Unräumliches gebraucht hat, kommt schließlich ein Stadium, in dem auch das Denken räumlich wird. Im Weltbild und erst recht im Gottesbegriff der Anthroposophie liegt offenbar eine solche Verräumlichung des Denkens vor. , , und Welten: wer so von Gott redet, macht ihn schließlich zu einem Zielpunkte, auf den mensch- liche Bewegung hinführen soll.",
      "Das ist aber Intellektualismus. Denn keine menschliche Bewe- gung führt näher zu Gott, niemals wird in räumlichen Bildern das Unräumliche wirklich erfaßt. Definieren läßt sich Gott nur in Paradoxieen. Das Heilige ist immer solcher Art, daß es gleichzeitig im Zeiträumlichen sich objektiviert und die bereits gelungene Objektivation zertrümmert.",
      "Man mag durch tausend Welten immer steigen, Gott kommt man damit nicht um Haaresbreite näher. Denn Er ist nicht da, wohin wir mit unseren Kräften aufsteigen könnten, sondern Er ist da, wo er sich offenbaren will.",
      "Er wird faßbar in einem . Ich wiederhole damit nur, was viele schon längst gesagt haben, was auf dem Kurs besonders Tillich treffend in folgendem Bild aussprach. Man hatte ihm gesagt, er stünde im , Anthroposophie im Allerheiligsten, woge- gen er einwand, daß vor Gott wir alle im Vorhof stehen.",
      "Denn Gott wohnt nicht in einem Tempel von Menschenhänden gemacht, sondern Tempel ist da, wo Gott im Paradoxon der Wirklichkeit durchbricht. Und mag der Vorhof heißen, wie er will, er wird eben erst durch solchen Durchbruch Gottes zum Tempel.",
      "Gott ist da, oder er ist nicht da, aber es gibt kein oder zu ihm nach Menschenweise.» 169 Habe nun, ach!: Goethe: «Faust» I, Studierzimmer, Zeilen 354ff.: «Habe nun, ach! Philosophie, /Juristerei und Medizin, / Und leider auch Theologie / Durchaus studiert mit heißem Bemühn.» 171 John Henry Newman, 1801-1890.",
      "Englischer Religionsphilosoph, ursprünglich anglikanischer Geistlicher. 1845 zum Katholizismus übergetreten, 1879 Kardinal. - Vgl. zu Newman auch Rudolf Steiners Vorträge Stuttgart, 15. Juni 1921, in «Vorträge und Kurse über christlich-religiöses Wirken, I», GA 342, und London, 24.",
      "April 1922: «Die dreifache Sonne und der auferstandene Christus» 221 in «Das Sonnenmysterium und das Mysterium von Tod und Auferstehung ...», GA 211. 172Paul Tillich: Siehe den 1. Hinweis zu S. 169. 173Leo XIII, 1810-1903.",
      "Papst von 1878-1903. Er erklärte Thomas von Aquino zum ersten Lehrer der katholischen Kirche. 174in den letzten Vorträgen: Siehe die Vorträge vom 24. und 26. Februar 1922 in «Alte und neue Einweihungsmethoden», GA 210. 175Hans Theberat, 1891-1971, Dr. der Chemie, war 1921 im Forschungsinstitut der AG «Der Kommende Tag» tätig, später auf Rat Rudolf Steiners Lehrer an der Goetheschule in Hamburg.",
      "Kurt Grelling: Über Kurt Grelling ist nichts Näheres bekannt, da die Debatte nicht mitgeschrieben wurde. Auch über Grellings Auftreten beim Stuttgarter Kongreß ist nichts bekannt. im Stuttgarter Kursus: Vom 28.",
      "August bis 7. September 1921 fand in Stuttgart der Erste allgemeine öffentliche Kongreß «Kultur- ausblicke der anthroposophischen Bewegung» statt. Rudolf Steiner hielt dabei den Vortragszyklus «Anthroposophie, ihre Erkennt- niswurzeln und ihre Lebensfrüchte, mit einer Einleitung über den Agnostizismus als Verderber echten Menschentums», abgedruckt in GA 78. 176 Wiener Kongreß: Der «Zweite internationale Kongreß der anthro- posophischen Bewegung zur Verständigung westlicher und östlicher Weltgegensätzlichkeit» fand vom 1. - 12.",
      "Juni 1922 statt und trug den Titel «West und Ost». In der Gesamtausgabe erschienen unter dem Titel «Westliche und östliche Weltgegensätzlichkeit. Wege zu ihrer Verständigung durch Anthroposophie», GA 83. 178Die hier genannten Vortragenden, Karl Schubert (1889-1949), Walter Johannes Stein (1891-1957) und Erich Schwebsch (1889-1953) waren Lehrer an der Freien Waldorfschule in Stuttgart.",
      "Siehe: «Der Lehrerkreis um Rudolf Steiner in der ersten Waldorfschule», Stuttgart 1977. Die Vorträge dieser Persönlichkeiten sind nicht mitgeschrieben worden. 179Eurythmie-Vorstellungen am Donnerstag und Sonntag: Von diesen beiden «kurzen Eurythmie-Vorstellungen» ist nichts bekannt.",
      "Zur Vorstellung im Deutschen Theater siehe Hinweis zu S. 159. Stuttgarter anthroposophischer Kongreß: Siehe Hinweis zu S. 175. 222"
    ],
    "sentences": [
      [
        "Werke Rudolf Steiners innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer erwähnt.",
        "Siehe auch die Übersicht am Schlusß des Bandes.",
        "Zu Sehe 15 Emil Du Bois-Reymond, 1818-1896, deutscher Physiologe. - «Über die Grenzen des Naturerkennens."
      ],
      [
        "Vortrag, gehalten in der zweiten öffentlichen Sitzung der 45.",
        "Versammlung Deutscher Naturfor- scher und Ärzte zu Leipzig am 14.",
        "August 1872», Leipzig 1872. wenn ich mich des Bu Bois-Reymondschen Ausdruckes bedienen darf: Ebenda, S. 2: «Naturerkennen - genauer gesagt naturwissen- schaftliches Erkennen oder Erkennen der Körperwelt mit Hülfe und im Sinne der theoretischen Naturwissenschaft - ist Zurück- führen der Veränderungen in der Körperwelt auf Bewegungen von Atomen, die durch deren von der Zeit unabhängige Centralkräfte bewirkt werden, oder Auflösung der Naturvorgänge in Mechanik der Atome."
      ],
      [
        "Es ist psychologische Erfahrungstatsache, daß, wo solche Auflösung gelingt, unser Causalitätsbedürfniss vorläufig sich befriedigt fühlt.» 16Rudolf Vircbow, 1821-1902, Mediziner und Anthropologe, Profes- sor der pathologischen Anatomie und zeitweise Rektor der König- lichen Friedrich-Wilhelm-Universität in Berlin. - «Die Gründung der Berliner Universität und der Übergang aus dem philosophi- schen in das naturwissenschaftliche Zeitalter», Rede, gehalten am 3.",
        "August 1893, Berlin 1893. 17Ernst Mach, 1838-1916, österreichischer Physiker und materialisti- scher Philosoph."
      ],
      [
        "Er war einer der Begründer des Empiriokritizis- mus, erneuerte in der Erkenntnistheorie die Anschauungen Berke- leys und Humes. £5 handelt sich bei Goethe einfach um das, was in seinen Worten liegt: Siehe «J.",
        "Goethe: Naturwissenschaftliche Schriften», mit Einleitungen, Fußnoten und Erläuterungen im Text herausgegeben von Rudolf Steiner; photomechanischer Nachdruck nach der Erstauflage in «Kürschners Deutsche National-Litteratur» (1884 - 1897), 5 Bände, GA 1a-e; Bd. 5, GA 1e, «Sprüche in Prosa», 1."
      ],
      [
        "Abt.: «Das Erkennen», S. 376: «Das Höchste wäre, zu begreifen, daß alles Faktische schon Theorie ist.",
        "Die Bläue des Himmels offenbart uns das Grundgesetz der Chromatik.",
        "Man suche nur nichts hinter den Phänomenen; sie selbst sind die Lehre.» Goethe kam ja auf diesem Wege zur Statuierung dessen, was er «Urphänomen» nannte: Ebenda, Bd. 3, GA 2c, 2."
      ],
      [
        "Abt.: «Physische 203 Farben», X.",
        "«Dioptrische Farben.",
        "Der ersten Klasse», S. 135, § 150f. und S. 141f., § 174-177.",
        "Zu § 175 fügte Rudolf Steiner in einer Fußnote folgendes bei (S.141): «Hier spricht Goethe seine Ansicht über die eigentliche Aufgabe der Naturwissenschaft aus."
      ],
      [
        "Was wir unmittelbar in der Natur wahrnehmen, sind Phänomene, die von den mannigfaltigsten Bedingungen abhängen.",
        "Wenn wir irgend eine oder mehrere von diesen Bedingungen ändern, so ändert sich auch das Phänomen."
      ],
      [
        "Es wird sich nun darum handeln, festzustellen, wann diese Änderung eine untergeordnete, nebensächliche und wann eine durchgreifende ist.",
        "Alle jene Phänomene, die durch eine Änderung der Bedingungen sich nur unwesentlich ändern wird und einen verwandten Zug zeigen, weisen uns auf ein Grund- oder Urphänomen hin, das ihnen allen zu Grund liegt und in dem sich ein Naturgesetz ausspricht."
      ],
      [
        "Aufgabe des Naturforschers wird es also sein, eine solche Reihe von Phänomenen nebeneinanderzustel- len, die immer nur durch eine Änderung der Bedingungen Modi- fikationen einer Grunderscheinung sind.",
        "Diese Grunderscheinung aber ist das objektive Naturgesetz."
      ],
      [
        "Keine Naturerklärung kann als solche über die Urphänomene hinausgehen.",
        "Es ist ein großer Irrtum, wenn man glaubt, die Urphänomene beweisen oder weiter erklären zu können.",
        "Wenn es selbst gelänge, irgendwo in der Welt das Atom nachzuweisen, so wäre die Wirkung des Atoms auf das Atom doch auch durch nichts anderes auszusprechen als durch ein Urphänomen."
      ],
      [
        "Man sollte daher die tiefsinnige Erfassung der Natur durch Goethe nicht fortwährend als Dilettantismus ansehen, während sie sich von der modernen Naturwissenschaft gerade durch die streng philosophische Begriffsfassung und Methode auszeichnet.",
        "Auch die Philosophie kann nicht über die Urphäno- mene hinausgehen; sie hat nur die Aufgabe, die durch die Naturforschung festgestellten Urphänomene in ihrer ideellen Folge aus einander zu entwickeln."
      ],
      [
        "Während der Naturforscher die Phänomene nebeneinanderstellt, damit sich in ihnen das Urphäno- men ausspricht, stellt der Philosoph die Urphänomene neben einander, damit sich darinnen die Naturideen aussprechen.» - Siehe ferner Rudolf Steiner in Bd. 2, GA Ib, Kap.",
        "«Verhältnis der Goetheschen Denkweise zu anderen Ansichten», S."
      ],
      [
        "LXI; Bd. 3, GA Ic, Kap.",
        "«Einleitung», 2.",
        "«Das Urphänomen», S.",
        "X ff.; Bd. 4, G A Id, Kap.",
        "«Einleitung», 3., S.",
        "VI ff. (In den «Einleitungen zu Goethes Naturwissenschaftlichen Schriften.",
        "Zugleich eine Grundlegung der Geisteswissenschaft (Anthroposophie)», GA l, entsprechen diese Stellen den S. 226f., 266ff., 311ff.) 17 Satz ..., den ich in den 80er Jahren des vorigen Jahrhunderts ausgesprochen habe: In «J."
      ],
      [
        "Goethe: Naturwissenschaftliche Schriften» (siehe den 2.",
        "Hinweis zu S. 17), Bd. l, GA l a, S.",
        "LXXIII; bzw. in «Einleitungen zu Goethes Naturwissenschaftlichen Schrif- 204 ten», GA l, S. 107: «Goethe ist der Kopernikus und Kepler der organischen Welt.» 18 Nikolaus Kopernikus, 1473-1543, Astronom, Mathematiker, Arzt, Jurist, Humanist und Domherr."
      ],
      [
        "Begründer des heliozentrischen Weltbildes.",
        "Johannes Kepler: Siehe Hinweis zu S. 61. der Kantsche Satz: Siehe «Metaphysische Anfangsgründe der Na- turwissenschaft», 1786, in «Immanuel Kants sämtliche Werke», Leipzig 1897, Bd. 4, Vorrede, S. 360, wörtlich: «Ich behaupte aber, daß in jeder besonderen Naturlehre nur so viel eigentliche Wissenschaft angetroffen werden könne, als darin Mathematik anzutreffen ist.» 19 Zuletzt sagte er sich: «Das Causalgesetz ist ... hinreichend charak- terisirt, wenn man sagt, es setzte eine Abhängigkeit der Erschei- nungen von einander voraus."
      ],
      [
        "Gewisse müssige Fragen, z.B. ob die Ursache der Wirkung vorausgehe oder gleichzeitig sei, verschwinden damit von selbst.» - «Nennen wir die Gesammtheit der Erschei- nungen, von denen eine Erscheinung a als abhängig betrachtet werden kann, die Ursache von oc.",
        "Wenn diese Gesammtheit gegeben ist, so ist a bestimmt und zwar eindeutig bestimmt."
      ],
      [
        "Man kann also das Causalgesetz auch m der Form ausdrücken: und 1903-1908», GA 34. 82 «Die Philosophie der Freiheit»: Rudolf Steiner: «Die Philosophie der Freiheit.",
        "Grundzüge einer modernen Weltanschauung - Seeli- sche Beobachtungsresultate nach naturwissenschaftlicher Metho- de» (1894), GA 4. 89 Jugendbewegung: Um 1900 in Deutschland entstandene Protestbe- wegung junger Menschen, die sich gegen traditionelle bürgerliche Auffassungen wendete und nach ihr wesensgemäßen Lebensformen suchte (Wandervogel etc.)."
      ],
      [
        "Nach dem Weltkrieg 1914 zer- splitterte die Jugendbewegung nach und nach in einzelne «Bünde». 96 in meinen «Kernpunkten ...»: Rudolf Steiner: «Die Kernpunkte der sozialen Frage in den Lebensnotwendigkeiten der Gegenwart und Zukunft» (1919), GA 23. 99 Versailler Vertrag: Dieser Friedensvertrag zwischen den Alliierten und dem Deutschen Reich wurde am 28.",
        "Juni 1919 unterzeichnet und trat am 10."
      ],
      [
        "Januar 1920 in Kraft. 100 Theoretiker ... allerlei Diskussionen: Siehe z.",
        "B. die Zeitschrift «Tribüne.",
        "Halbmonatsschrift für soziale Verständigung», Tübin- gen, die ihre 1.",
        "Nummer (Juni oder Juli 1919) der Diskussion über Rudolf Steiners Dreigliederungsidee widmete."
      ],
      [
        "Die betreffenden Aufsätze sind abgedruckt in den «Beiträgen zur Rudolf Steiner Gesamtausgabe», Nr. 106, Dornach, Ostern 1991. 213 101 Es kam das ganze furchtbare Valuta-Elend: Die deutsche Währung wurde nach dem 1.",
        "Weltkrieg durch eine sich ständig steigernde Inflation (1923 l Goldmark = l Billion) völlig entwertet. mein «Aufruf an das deutsche Volk ...»: Dieser Aufruf «An das deutsche Volk und an die Kulturwelt», von Rudolf Steiner verfaßt und von einer Anzahl bekannter Persönlichkeiten des öffentlichen Lebens unterzeichnet, wurde im März 1919 als Flugblatt gedruckt und weit verbreitet. - Abgedruckt in «Aufsätze über die Drei- gliederung des sozialen Organismus und zur Zeitlage 1915-1921», GA 24, sowie als Anhang in den «Kernpunkten» (siehe Hinweis zu S. 96). 102was ich wiederholt am Schlüsse von Vorträgen, die ich im Anschlüsse an die «Kernpunkte» hielt, damals gerufen habe: Siehe Vortrags- zyklus «Neugestaltung des sozialen Organismus» (1919), GA 330. 103ein Artikel: Nicht bekannt."
      ],
      [
        "David Lloyd George, 1863-1945, 1916 englischer Minister- präsident.",
        "Vortrage, den ich hier zuletzt in der Philharmonie gehalten habe: Bezieht sich auf den öffentlichen Vortrag «Anthroposophie in ihrem Wissenschaftscharakter», den Rudolf Steiner am 7."
      ],
      [
        "März 1922 im weiteren Rahmen dieses Hochschulkurses hielt (noch nicht veröffentlicht).",
        "Das wirtschaftliche Leben hat sich zunächst: Siehe hierzu die ausführlichere Darstellung in den Vorträgen vom 26., 28. und 29."
      ],
      [
        "August 1922 in «Die geistig-seelischen Grundkräfte der Erzie- hungskunst.",
        "Spirituelle Werte in Erziehung und sozialem Leben», GA 305. 106 Adam Smith, 1723-1790, englischer Nationalökonom und Philo- soph."
      ],
      [
        "Hauptwerk: «An Inquiry into the Nature and Causes of the Wealth of Nations», 4 Bände, 1776.",
        "Deutsch von Max Stirner: «Untersuchungen über die Natur und die Ursache des Wohlstandes der Nationen», 1846/47."
      ],
      [
        "Karl Marx, 1818-1883, Begründer des wissenschaftlichen Sozialis- mus und des historischen Materialismus.",
        "Hauptwerke: «Zur Kritik der politischen Ökonomie», 1859, und «Das Kapital.",
        "Kritik der politischen Ökonomie», 1867/94. 107 David Ricardo, 1772-1823, englischer Nationalökonom, Schüler von Adam Smith, Lehrer von Karl Marx."
      ],
      [
        "John Stuart Mill: Siehe Hinweis zu S. 58. 214 108die sogenannten «Vierzehn Punkte» Woodrow Wilsons: Woodrow Wilson (1856-1924), amerikanischer Präsident von 1912-1920, stellte 1918 dem amerikanischen Kongreß sein Programm für ei- nen Weltfrieden vor, bekannt als die «Vierzehn Punkte».",
        "Dieses Programm wurde im Versailler Vertrag 1919 nicht verwirklicht."
      ],
      [
        "Siehe «Die Reden Woodrow Wilsons», englisch und deutsch, Der Freie Verlag Bern, Bern 1919. 109Im Jahre 1917 versuchte ich: Bereits im Jahre 1917 verfaßte Ru- dolf Steiner nach Gesprächen mit Graf Otto Lerchenfeld und Graf Ludwig Polzer-Hoditz zwei Memoranden, in denen er zu grundlegenden politischen Fragen angesichts der damaligen Situa- tion Stellung nahm.",
        "Die beiden genannten Persönlichkeiten wand- ten sich mit diesen Memoranden an einflußreiche Politiker, so u.a. an den deutschen Staatssekretär Kühlmann und an Arthur Polzer- Hoditz, den Kabinettchef Kaiser Karls von Österreich."
      ],
      [
        "Die Me- moranden wurden erstmals veröffentlicht in Roman Boos: «Rudolf Steiner während des Weltkrieges», Dornach 1933.",
        "Innerhalb der Gesamtausgabe siehe «Aufsätze über die Dreigliederung des sozialen Organismus und zur Zeitlage 1915-1921», GA 24. 110fast jeden Nachmittag nach zwei Uhr: Vgl. hierzu «Mein Le- bensgang», GA 28, Kap."
      ],
      [
        "VIII, S. 148f. 111die alten Stände: Die Formulierung «Nährstand, Wehrstand, Lehrstand» stammt von Erasmus Alberus (1500-1553), ähnlich auch Luther; sie faßt das von Plato in der «Politeia» über die Stände Gesagte zusammen; siehe den «phönikischen Mythos», wonach Gott den Herrschenden (Weisen) bei der Geburt Gold, ihren Beihelfern, den Wächtern, Silber, den Bauern und Handwerkern aber Eisen und Erz beigemischt habe («Politeia» III.",
        "Buch, 414ff."
      ],
      [
        "St.).",
        "Siehe hierzu auch Vincenz Knauer: «Die Hauptprobleme der Philosophie», Wien und Leipzig 1892.",
        "Das Buch befindet sich in der Bibliothek Rudolf Steiners.",
        "Dort heißt es in den Vorlesungen über Plato (S. 124): «Wie sich das Seelische im einzelnen Menschen in das Vernünftige, Irascible und Concupiscible gliedert, so finden sich im Staate drei Stände, die wir einer uns geläufigen Redeweise ganz entsprechend als Lehr-, Nähr- und Wehrstand bezeichnen können.» 114 wie ja der natürliche Organismus auch unter dem Einfluß seiner relativen Dreigliederung: Vgl."
      ],
      [
        "Rudolf Steiner: «Von Seelenrätseln» (1917), GA 21, Kap.",
        "«Die physischen und die geistigen Abhängig- keiten der Menschen-Wesenheit».",
        "Dort wird die Dreigliedrigkeit der Seele durch ihr Denken, Fühlen und Wollen dargestellt."
      ],
      [
        "Zu Begriffen wie Arbeit und Kapital siehe u.a.",
        "Rudolf Steiners Ausführungen im Zyklus «Nationalökonomischer Kurs.",
        "Aufgaben 215 einer neuen Wirtschaftswissenschaft, Band I» (Dornach 1922), GA 340, Stichwortregister. 118 Zum «Theologentag» des Berliner Hochschulkurses siehe die Be- richte von Ernst Uehli und Eberhard Kurras im Anhang, S. 189ff. und 194ff.."
      ],
      [
        "In dieser Zeitungsnotiz steht: In der Wochenschrift «Die Christ- liche Welt», Marburg, 36.",
        "Jg., Nr. 9, 2.",
        "März 1922, S. 157f., erschien folgende Notiz: «[...] Diese Veranstaltung am Freitag ist nun eine unzweideutige Herausforderung Steiners und seiner Anhänger an die heutigen Theologen."
      ],
      [
        "Ich sage das ohne jeden Vorwurf.",
        "Denn theologische Wissenschaft ist so wenig sakrosankt wie irgend eine andre.",
        "Und wie gern wir sie (und uns mit) der Kritik unterwerfen, wissen unsre Leser.",
        "Es weiß es vor allem auch Rittelmeyer [...] So ist auch der Waffengang der Steinergruppe willkommen."
      ],
      [
        "Nur wird eben der Handschuh aufgehoben werden müssen.",
        "Bisher haben wir unserseits uns am Für und Wider genügen lassen [...] Die Männer haben recht, es gibt da auf die Dauer keine Neutralität, und sie wollen uns eine Schlacht liefern, die sie entweder gewinnen oder verlieren."
      ],
      [
        "Ich meinerseits kann nur wünschen, daß diese Tagung wirklich ein entscheidendes Ergebnis zeitigt.",
        "Und wäre es eben nur dies: ob wir Steiner alle ernstlich studieren müssen oder nicht [...] Wir sind daran mehr interessiert als andre Gruppen innerhalb der heutigen Theologie, weil Geyer und Rittelmeyer zu unsern aner- kannten und geschätztesten Freunden gehören [...]» (D."
      ],
      [
        "Rade). - Heinrich Frick, Berichterstatter der «Christlichen Welt», schrieb dazu in Nr. 13 vom 30.",
        "März 1922, S. 227: «Ich habe alsbald privatim Dr.",
        "Rittelmeyer und öffentlich zu Beginn der Aussprache (Dr."
      ],
      [
        "R. erteilte mir freundlichst als erstem Redner das Wort zu meiner Erklärung) dargelegt, daß der Ausdruck in der C[hristhchen] W[elt] nicht gemeint gewesen sei als auf eine bestimmte Person im Sinne eines ethischen Vorwurfes gerichtet (denn Niemand von uns wußte ja, wer eigentlich das Thema formuliert hatte), sondern daß die Formulierung selbst (rein sachlich ihr Wortlaut) als Herausforderung empfunden werden mußte.",
        "Ich erinnerte daran, daß bei ruhiger Lektüre des Programms es auffallen müsse, daß an keinem Tage so scharf eine ganz bestimmte Größe nicht nur genannt, sondern zugleich bewertet wird wie gerade die Theologie, von der doch dasteht: und dann dreimal wiederholt das Stichwort Untergang - Untergang - Untergang> in einem -Ismus!"
      ],
      [
        "Das sei doch, ganz menschlich genommen, eine , und ich bäte die Zuhörer, doch ja bei sich das Mißverständnis abzuwehren, als ob bei der Schriftleitung der CW eine Animosität gegen die Anthroposophie vorläge [...] 216 Dr.",
        "Rittelmeyer erklärte demgegenüber privatim und öffentlich, er selbst habe, als er das Thema formulierte, nicht an eine gedacht, sondern nur an eine ernste Frage, diese allerdings mit allem Nachdruck den Theologen ins Gewissen schieben wollen.» 120experimentelle Psychologie: Bezieht sich auf eine Richtung der Psychologie, die v.a. von Forschern wie Wundt, Stumpf, Lange, James, Ziehen, Külpe, Ebbinghaus, G.E.Müller, Martius, Stern und Neumann vertreten wurde. 121Ernst Haeckel: Siehe Hinweis zu S. 43."
      ],
      [
        "«Es ist nichts im Verstände, was nicht vorher in den Sinnen ist»: «Nihil est in intellectu, quod non fuerit in sensu.» In dieser Formulierung findet sich der Satz erst bei Thomas von Aquino (Quaestiones de veritate II, 3.",
        "Coloniae 1475), ähnlich formuliert auch schon bei Cicero (De finibus I, 19); jedoch entspricht er den Ausführungen in Aristoteles' Schrift «De anima»."
      ],
      [
        "Siehe besonders Buch 3, Kap. 8: «Da es aber außer den empfundenen Größen (nämlich durch Sinnesempfindung), wie es scheint, kein Ding gibt, das abgetrennt für sich existierte, so ist in den empfundenen Formen auch das Gedachtwerdende, das durch Abstraktion Ge- sagte, und alle Beschaffenheit und Zustände des Empfundenen.",
        "Und deshalb kann man, wenn man nichts empfindet, auch nichts lernen, noch verstehen.» (Übersetzt von F."
      ],
      [
        "Kreuz). der Leibnizsche Satz: «Nihil est in intellectu, quod non fuerit in sensu, nisi ipse intellectus».",
        "Siehe Gottfried Wilhelm Leibniz (1646 bis 1716): «Neue Abhandlungen über den menschlichen Verstand», Buch II, Kap."
      ],
      [
        "I, (Theophilus): «Man wird mir jenes von den Philosophen anerkannte Axiom entgegenhalten, daß nichts in der Seele ist, das nicht von den Sinnen stammt.",
        "Aber man muß die Seele selbst und ihre Affektionen davon ausnehmen."
      ],
      [
        "Nihil est in intel- lectu, quod non fuerit in sensu, excipe: nisi intellectus ipse.",
        "Die Seele schließt in sich das Sein, die Substanz, das Eine, das Gleiche, die Ursache, die Perzeption, das vernünftige Denken und viele andere Begriffe, die die Sinne nicht geben können.» - Siehe dazu auch R."
      ],
      [
        "Steiners Vortrag vom 17.",
        "September 1915 in «Der Wert des Den- kens für eine den Menschen befriedigende Erkenntnis.",
        "Das Verhält- nis der Geisteswissenschaft zur Naturwissenschaft», GA 164. 123 wenn mir Dinge gesagt wurden, wie zum Beispiel von einer heute auch hier anwesenden sehr verehrten Persönlichkeit: Friedrich Rittelmeyer (1872-1938), war protestantischer Geistlicher, von 1902 ein bekannter Prediger in Nürnberg, dann an der «Neuen Kirche» in Berlin, und Verfasser theologischer Schriften. 217 Er stand seit 1911 in Verbindung mit Rudolf Steiner («Meine Lebensbegegnung mit Rudolf Steiner», Stuttgart 1928) und gab 1921 das Sammelwerk «Vom Lebenswerk Rudolf Steiners» heraus."
      ],
      [
        "Er leitete den hier vorliegenden «Berliner Hochschulkurs» und war Mitbegründer und erster Erzoberlenker der im Herbst 1922 begründeten «Christengemeinschaft, Bewegung für religiöse Er- neuerung»; von 1923 an auch im Vorstand der Deutschen An- throposophischen Gesellschaft.",
        "Eine kurze Biographie Friedrich Rittelmeyers ist enthalten in Rudolf Gädekes «Die Gründer der Christengemeinschaft», Dornach 1992. - Rittelmeyer hatte sich dahingehend auch in seinem Aufsatz «Johannes Müller und Rudolf Steiner» in der Zeitschrift «Die Christliche Welt», Nr. 22/23, 30."
      ],
      [
        "Mai 1918, geäußert.",
        "Auf eine Beschuldigung Müllers, Rudolf Steiner mache «aus der okkulten Welt eine Sensation für die Neugier und Lüsternheit der abergläubischen Instinkte der Men- schen» erwiderte Rittelmeyer dort (S. 215, Fußnote): «Weder die Themata noch die Vorträge selbst haben je das Geringste von solcher Spekulation enthalten."
      ],
      [
        "Steiner mutet insbesondere den Hörern der öffentlichen Vorträge meist eine geistige Anstrengung zu, die alle nicht sehr ernsthaften Hörer bald wieder abschreckt, und macht ihrer Neugier und Sensationslüsternheit kein Zuge- ständnis [...]». 129 Vater-Erlehnis: Vgl. hierzu z.",
        "B. die Vorträge vom 20."
      ],
      [
        "Februar und 13.",
        "März 1917 in «Bausteine zu einer Erkenntnis des Mysteriums von Golgatha.",
        "Kosmische und menschliche Metamorphose», GA 175, und «Wie finde ich den Christus?» vom 16.",
        "Oktober 1918 in «Der Tod als Lebenswandlung», GA 182."
      ],
      [
        "Was ich gestern gesagt habe über das Ausbilden des Urteils: Bezieht sich auf den öffentlichen Abendvortrag «Anthroposophie als Lebensinhalt», den Rudolf Steiner am 9.",
        "März 1922 anläßlich des Hochschulkurses hielt (noch nicht veröffentlicht). 130 Wladimir Solowjew: Siehe u.a. seine «Zwölf Vorlesungen über das Gottmenschentum», Stuttgart 1921/22. 133«Ich bin bei Euch alle Tage bis an das Ende der Welt»: Matth. 28, 20. 134Friedrich Nietzsche, 1844-1900, Philosoph."
      ],
      [
        "In dem Buche von Friedrich Nietzsches Freund Overbeck: Franz Overbeck (1837-1905), Professor der Theologie in Basel, Freund Friedrich Nietzsches. - «Über die Christlichkeit unserer heutigen Theologie», 1873. 135 Johannes Scotus Erigena, 810-877, irischer Philosoph, Vorläufer der scholastischen Philosophie. 218 135Thomas von Aquino, 1225-1274, christlicher Kirchenlehrer, Philo- soph und Scholastiker. 1323 heilig gesprochen. 136Schon vor vielen Jahren hielt ich einmal in einer süddeutschen Stadt ... einen Vortrag über «Bibel und Weisheit»: In Colmar im Jahr 1905.",
        "Eine Nachschrift liegt nicht vor."
      ],
      [
        "Über das Thema «Bibel und Weisheit» hat Rudolf Steiner an verschiedenen Orten gesprochen.",
        "Gedruckt sind die Berliner Vorträge vom 12. und 14.",
        "November 1908 in «Wo und wie findet man den Geist?», GA 57; Einzelaus- gabe Dornach 1993. 138 Waldorfschule: Siehe hierzu den Vortrag «Anthroposophie und Erziehungswissenschaft» in diesem Band. 140Bei einem kurzen Kurse: Rudolf Steiner: «Geisteswissenschaftliche Sprachbetrachtungen."
      ],
      [
        "Eine Anregung für Erzieher» (6 Vorträge, Stuttgart 1919/1920), GA 229. 141Ich habe zu Weihnachten in Dornach am Goetheanum einen Vortragszyklus zu halten gehabt: «Die gesunde Entwickelung des Menschenwesens.",
        "Eine Einführung in die anthroposophische Päd- agogik und Didaktik» («Weihnachtskurs für Lehrer», 16 Vorträge und 3 Fragenbeantwortungen, Dornach 1921/22), GA 303. 142in einem dieser Vorträge: Ebenda, Vortrag vom 7."
      ],
      [
        "Januar 1922: «Die ethische und die religiöse Erziehung im besonderen». gestern: Bei dem Vortrag «Anthroposophie und Theologie». 143 Rittelmeyer hat ... geantwortet mit dem Vergleich zwischen dem Kopf und dem Buch: Zu Friedrich Rittelmeyer siehe den Hinweis zu S. 123. - Vermutlich hatte Rittelmeyer in der Diskussion den bekannten Aphorismus Georg Christoph Lichtenbergs zitiert: «Wenn ein Buch und ein Kopf zusammenstoßen und es klingt hohl, ist das allemal im Buch?» 148 Ich habe jene eine große Umwandlung hier wiederholt charakteri- siert: Siehe u.a. folgende Berliner Vorträge: 26.",
        "Januar 1911 in «Antworten der Geisteswissenschaft auf die großen Fragen des Daseins», GA 60; 15."
      ],
      [
        "Februar 1912 in «Menschengeschichte im Lichte der Geistesforschung», GA 61; und 13.",
        "Februar 1913 in «Ergebnisse der Geisteswissenschaft», GA 62. 155 Wilhelm Wundt, 1832-1920, Arzt, Philosoph und Psychologe, Professor in Heidelberg, Zürich und Leipzig. - Siehe seine «Völkerpsychologie."
      ],
      [
        "Eine Untersuchung der Entwicklungsgesetze von Sprache, Mythus und Sitte», 1.",
        "Band: «Die Sprache», 1.",
        "Teil, Leipzig 1900; Kap. 9: «Der Ursprung der Sprache», I.",
        "«Allgemeine Standpunkte» und II.",
        "«Kritische Übersicht der vier Haupttheo- rien», S. 584-603. 219 155gestern: Siehe den Vortrag «Anthroposophie und Theologie» in diesem Band. 156Christian Geyer, 1862-1929, evangelischer Theologe, Hauptpredi- ger an der Sebalduskirche in Nürnberg. - Geyer hatte als Vor- tragsthema «Der Untergang des Christentums in Historismus»."
      ],
      [
        "Seine Ausführungen sind den Herausgebern nicht bekannt. 159 Eurythmievorstellung im Deutschen Theater: Am Sonntag, den 12.",
        "März, fand um 11.00 Uhr eine Eurythmievorstellung statt.",
        "Von den einleitenden Worten, die Rudolf Steiner hierzu sprach, ist keine Nachschrift vorhanden. 164Hegel hat ja bereits in seiner Philosophie ... gesagt: Eventuell handelt es sich hier um einen Hör- oder Ubertragungsfehler des Stenographen. 165Emil Leinbas, 1878-1967, Mitbegründer und später Generaldi- rektor der «Kommender Tag AG», Stuttgart."
      ],
      [
        "Ab Februar 1923 im Vorstand der Anthroposophischen Gesellschaft in Deutschland. 166Emil Bock, 1895-1959, Lic. theol., im Herbst 1922 Mitbegründer und Oberlenker der Christengemeinschaft, ab 1938 deren Erz- oberlenker.",
        "Zu seiner Biographie siehe «Die Gründer der Chri- stengemeinschaft» von Rudolf F."
      ],
      [
        "Gädeke, Dornach 1992, und Gunhild Kacer-Bock: «Emil Bock.",
        "Leben und Werk», Stuttgart 1993.",
        "«Der Untergang der Religion ... »: Rudolf Steiner gibt die Titel hier frei wieder. 169 ein Privatdozent: Paul Tillich, 1886-1965, war zur damaligen Zeit Dozent an der Theologischen Fakultät in Berlin, ab 1924 Professor für Religionswissenschaft und Sozialphilosophie u.a. in Leipzig, Dresden, Frankfurt."
      ],
      [
        "Tillich emigrierte 1933 nach Amerika, wo er zum führenden protestantischen Theologen der USA wurde.",
        "Siehe hierzu den Bericht «Wer hat ?» von Heinrich Frick, in: «Die Christliche Welt», 36.",
        "Jg., Nr. 13, 30."
      ],
      [
        "März 1922, S. 225 ff. ein Pfarrer: Carl-Günther Schweitzer, 1889-1965. 1921 gründete Schweitzer die apologetische Zentrale, u.a. zur Auseinandersetzung der evangelischen Theologie mit Geistesströmungen der damaligen Zeit.",
        "Gott sei eben das Unbedingte, das überall durchbricht: In einem Aufsatz «Anthroposophie und evangelische Theologie», veröffent- licht in der Zeitschrift «Die Christliche Welt», Nr. 17, vom 27."
      ],
      [
        "April 1922, schreibt Heinrich Frick hierzu: 220 «Als intellektualistisch empfinde ich überhaupt die Denkungs- weise [der Anthroposophen], -wie sie aus den meisten Vorträgen des Kursus sprach.",
        "Was heißt z.B."
      ],
      [
        "Welten?",
        "Der Komparativ und das Wort selbst sind aus räumlicher Anschauung genommen.",
        "Ein großer Teil unsrer Begriffe entstammt ja räumlichen Bezie- hungen.",
        "Nun können wir auch vom Unräumlichen nicht anders reden als in solchen Begriffen; aber es liegt darin die große Gefahr, daß wir den Begriff und das Gemeinte nicht scharf genug aus- einander halten."
      ],
      [
        "Der Begriff färbt ab, und wenn man lang genug räumliche Begriffe für Unräumliches gebraucht hat, kommt schließlich ein Stadium, in dem auch das Denken räumlich wird.",
        "Im Weltbild und erst recht im Gottesbegriff der Anthroposophie liegt offenbar eine solche Verräumlichung des Denkens vor. , , und Welten: wer so von Gott redet, macht ihn schließlich zu einem Zielpunkte, auf den mensch- liche Bewegung hinführen soll."
      ],
      [
        "Das ist aber Intellektualismus.",
        "Denn keine menschliche Bewe- gung führt näher zu Gott, niemals wird in räumlichen Bildern das Unräumliche wirklich erfaßt.",
        "Definieren läßt sich Gott nur in Paradoxieen.",
        "Das Heilige ist immer solcher Art, daß es gleichzeitig im Zeiträumlichen sich objektiviert und die bereits gelungene Objektivation zertrümmert."
      ],
      [
        "Man mag durch tausend Welten immer steigen, Gott kommt man damit nicht um Haaresbreite näher.",
        "Denn Er ist nicht da, wohin wir mit unseren Kräften aufsteigen könnten, sondern Er ist da, wo er sich offenbaren will."
      ],
      [
        "Er wird faßbar in einem .",
        "Ich wiederhole damit nur, was viele schon längst gesagt haben, was auf dem Kurs besonders Tillich treffend in folgendem Bild aussprach.",
        "Man hatte ihm gesagt, er stünde im , Anthroposophie im Allerheiligsten, woge- gen er einwand, daß vor Gott wir alle im Vorhof stehen."
      ],
      [
        "Denn Gott wohnt nicht in einem Tempel von Menschenhänden gemacht, sondern Tempel ist da, wo Gott im Paradoxon der Wirklichkeit durchbricht.",
        "Und mag der Vorhof heißen, wie er will, er wird eben erst durch solchen Durchbruch Gottes zum Tempel."
      ],
      [
        "Gott ist da, oder er ist nicht da, aber es gibt kein oder zu ihm nach Menschenweise.» 169 Habe nun, ach!: Goethe: «Faust» I, Studierzimmer, Zeilen 354ff.: «Habe nun, ach!",
        "Philosophie, /Juristerei und Medizin, / Und leider auch Theologie / Durchaus studiert mit heißem Bemühn.» 171 John Henry Newman, 1801-1890."
      ],
      [
        "Englischer Religionsphilosoph, ursprünglich anglikanischer Geistlicher. 1845 zum Katholizismus übergetreten, 1879 Kardinal. - Vgl. zu Newman auch Rudolf Steiners Vorträge Stuttgart, 15.",
        "Juni 1921, in «Vorträge und Kurse über christlich-religiöses Wirken, I», GA 342, und London, 24."
      ],
      [
        "April 1922: «Die dreifache Sonne und der auferstandene Christus» 221 in «Das Sonnenmysterium und das Mysterium von Tod und Auferstehung ...», GA 211. 172Paul Tillich: Siehe den 1.",
        "Hinweis zu S. 169. 173Leo XIII, 1810-1903."
      ],
      [
        "Papst von 1878-1903.",
        "Er erklärte Thomas von Aquino zum ersten Lehrer der katholischen Kirche. 174in den letzten Vorträgen: Siehe die Vorträge vom 24. und 26.",
        "Februar 1922 in «Alte und neue Einweihungsmethoden», GA 210. 175Hans Theberat, 1891-1971, Dr. der Chemie, war 1921 im Forschungsinstitut der AG «Der Kommende Tag» tätig, später auf Rat Rudolf Steiners Lehrer an der Goetheschule in Hamburg."
      ],
      [
        "Kurt Grelling: Über Kurt Grelling ist nichts Näheres bekannt, da die Debatte nicht mitgeschrieben wurde.",
        "Auch über Grellings Auftreten beim Stuttgarter Kongreß ist nichts bekannt. im Stuttgarter Kursus: Vom 28."
      ],
      [
        "August bis 7.",
        "September 1921 fand in Stuttgart der Erste allgemeine öffentliche Kongreß «Kultur- ausblicke der anthroposophischen Bewegung» statt.",
        "Rudolf Steiner hielt dabei den Vortragszyklus «Anthroposophie, ihre Erkennt- niswurzeln und ihre Lebensfrüchte, mit einer Einleitung über den Agnostizismus als Verderber echten Menschentums», abgedruckt in GA 78. 176 Wiener Kongreß: Der «Zweite internationale Kongreß der anthro- posophischen Bewegung zur Verständigung westlicher und östlicher Weltgegensätzlichkeit» fand vom 1. - 12."
      ],
      [
        "Juni 1922 statt und trug den Titel «West und Ost».",
        "In der Gesamtausgabe erschienen unter dem Titel «Westliche und östliche Weltgegensätzlichkeit.",
        "Wege zu ihrer Verständigung durch Anthroposophie», GA 83. 178Die hier genannten Vortragenden, Karl Schubert (1889-1949), Walter Johannes Stein (1891-1957) und Erich Schwebsch (1889-1953) waren Lehrer an der Freien Waldorfschule in Stuttgart."
      ],
      [
        "Siehe: «Der Lehrerkreis um Rudolf Steiner in der ersten Waldorfschule», Stuttgart 1977.",
        "Die Vorträge dieser Persönlichkeiten sind nicht mitgeschrieben worden. 179Eurythmie-Vorstellungen am Donnerstag und Sonntag: Von diesen beiden «kurzen Eurythmie-Vorstellungen» ist nichts bekannt."
      ],
      [
        "Zur Vorstellung im Deutschen Theater siehe Hinweis zu S. 159.",
        "Stuttgarter anthroposophischer Kongreß: Siehe Hinweis zu S. 175. 222"
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
