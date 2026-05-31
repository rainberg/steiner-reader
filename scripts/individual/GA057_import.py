#!/usr/bin/env python3
"""Standalone import script for GA057 — GA057 - Wo und wie findet man den Geist? (1908/09)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA057 - Wo und wie findet man den Geist? (1908/09)"""
GA_NUMBER = "GA057"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "GOETHES GEHEIME OFFENBARUNG EXOTERISCH Berlin, 22. Oktober 1908",
    "paragraphs": [
      "GOETHES GEHEIME OFFENBARUNG",
      "Berlin, 22. Oktober 1908",
      "Wer die geistige Entwickelungsgeschichte der Menschheit nicht nur nach den gewöhnlich üblichen Dokumenten und Traditionen verfolgt, sondern ein wenig tiefer geht, indem er sich auf manches einläßt, was vielleicht zunächst nur symptomatisch erscheinen könnte für die Menschheits-entwickelung, was aber doch intensiv hineinweist in die inneren und daher wahren Entwicklungskräfte, der wird eine denkwürdige Szene in der neueren Geistesgeschichte immer wieder und wieder bedeutungsvoll finden, eine Szene, die sich in den neunziger Jahren des achtzehnten Jahrhunderts in Jena zugetragen hat.",
      "Dazumal wurde in der Naturforschenden Gesellschaft in Jena von einem damals sehr bedeutenden Botaniker, na­mens Batsch, ein Vortrag gehalten, der durchaus auf der Höhe der damaligen Wissenschaftlichkeit stand. Zwei Män­ner, ein jüngerer und ein um zehn Jahre älterer, hörten sich diesen Vortrag an, und es trug sich zu, daß sie gleichzeitig aus dem Vortrag hinweggingen und miteinander ins Ge­spräch kamen. Der jüngere der beiden Männer sagte dabei zu dem älteren: Wenn man einen solchen Vortrag auf sich wirken läßt, so zeigt es sich doch immer wieder, wie die wissenschaftliche Betrachtungsweise die Dinge zerpflückt, wie sie das eine neben das andere hinstellt und das einheit­liche geistige Band, das in all' den verschiedenen Einzel­heiten lebt, so wenig berücksichtigt. - Es widerstrebte sozusagen",
      "dem jüngeren Mann, daß da Pflanze an Pflanze hingestellt wurde, ohne Hinweis auf das, was als ein Hö­heres, die verschiedenen Pflanzen Verbindendes, doch auch in der Welt leben muß. Der ältere der beiden Männer sagte darauf, es könne sich vielleicht doch auch eine Betrachtungs­weise der Natur finden, die nicht so zu Werke geht, und die, trotzdem sie eine Erkenntnis ist, eine Betrachtung, die zur Erkenntnis führen muß, sehr wohl auf das Einheitliche geht, auf das, was getrennt ist in den für die verschiedenen Sinne äußerlichen Betrachtungen. - Der Mann nahm einen Bleistift und ein Stück Papier aus seiner Tasche und zeich­nete sogleich ein merkwürdiges Gebilde, ein Gebilde, wel­ches einer Pflanze ähnlich sah, aber keiner der lebenden Pflanzen, die man mit den äußeren physischen Sinnen sehen oder wahrnehmen kann, ein Gebilde, das sozusagen nir­gends einzeln verwirklicht ist, und von dem er sagte, daß es zwar in keiner einzelnen Pflanze lebe, aber die Pflanzen­heit, die Urpflanze in allen Pflanzen sei und das Verbin­dende ausmache. - Der jüngere Mann sah sich das an und sagte darauf: «Ja, was Sie da aufzeichnen, ist aber keine Erfahrung, das ist keine Beobachtung, das ist eine Idee» -und er hatte dabei im Sinne, daß solche Ideen nur der menschliche Geist ausbilden könne, und daß eine solche Idee keine Bedeutung habe für das, was draußen in der sogenannten objektiven Natur lebt.",
      "Der ältere der beiden Männer konnte diesen Einwand gar nicht recht verstehen, denn er erwiderte: Wenn das eine Idee ist, dann sehe ich meine Ideen mit Augen! Er meinte, daß in genau demselben Sinne, wie die einzelne Pflanze für den äußeren Sinn des Auges sichtbar ist, eine Erfahrung ist, so sei seine Urpflanze, obgleich sie nicht durch einen äußeren Sinn gesehen werden kann, ein Objektives, ein in der äußeren Welt Bestehendes, eben das, was in allen Pflanzen lebt, die Urpflanze in allen",
      "einzelnen Pflanzen. - Sie wissen, daß der jüngere der beiden Männer Schiller, der ältere Goethe war.",
      "Dieses Gespräch ist eine symptomatische, bedeutungs­volle Kundgebung der neueren Geisteswissenschaft. Was sprach dazumal eigentlich in Goethe bei seiner Erwiderung gegenüber Schiller? In Goethe sprach das Bewußtsein, daß man nicht nur mit jener Vorstellung, die der äußere Sinn gibt, und die der beschränkte Verstand aus den äußeren Sinneswahrnehmungen gewahrt, ein äußeres Objektives, ein äußeres Wahres erfaßt, sondern daß der Mensch dann, wenn er höhere Geisteskräfte in Bewegung setzt, welche sich nicht an einzelne Sinnesbeobachtungen wenden, ebenso zu einem Wahren, zu einem Wirklichen gelangt, wie man zu einem Wahren, Wirklichen durch die äußere Sinneswahr­nehmung kommt.",
      "Man darf wohl sagen, daß Schiller, der in jenem Augen­blicke noch nicht einsehen konnte, was dahinter war, und der glaubte, es seien Subjektivitäten, die ihm Goethe vor­gezeichnet hatte, das schönste Dokument geliefert hat dafür, wie sich der Mensch bis zu der Höhe hinaufranken kann, die ihm von Goethe gezeigt wurde. Von jenem Zeitpunkte an sehen wir Schiller den Goetheschen Ideen immer mehr Verständnis entgegenbringen. Ein psychologisches Doku­ment allerersten Ranges ist ein Brief Schillers, der da sagt:",
      "«Lange schon habe ich, obgleich aus ziemlicher Ferne, dem Gang Ihres Geistes zugesehen und den Weg, den Sie sich vorgezeichnet haben, mit immer erneuerter Bewunderung bemerkt. Sie suchen das Notwendige der Natur, aber Sie suchen es auf dem schweresten Wege, vor welchem jede schwächere Kraft sich wohl hüten wird. Sie nehmen die ganze Natur zusammen, um über das einzelne Licht zu bekommen; in der Allheit ihrer Erscheinungsarten suchen Sie den Erklärungsgrund für das Individuum auf. Von der",
      "einfachen Organisation steigen Sie, Schritt vor Schritt, zu den mehr verwickelten hinauf, um endlich die verwickeltste von allen, den Menschen, genetisch aus den Materialien des ganzen Naturgebäudes zu erbauen. Dadurch, daß Sie ihn der Natur gleichsam nacherschaffen, suchen Sie in seine verborgene Technik einzudringen. Eine große und wahr­haft heldenmäßige Idee, die zur Genüge zeigt, wie sehr Ihr Geist das reiche Ganze seiner Vorstellungen in einer schö­nen Einheit zusammenhält!»",
      "So dürfen wir, als ein Dokument für die Objektivität der Ideenwelt Goethes, das ansehen, was in Goethes Bewußt­sein zu solcher Antwort führte, und was Schiller später durch diesen Brief bestätigte.",
      "Sehr merkwürdig: Ein Psychologe, der in den zwanziger Jahren des neunzehnten Jahrhunderts lebte und heute ver­gessen ist, Heinroth, hat in seiner «Anthropologie», die eigentlich eine Psychologie ist, ein sehr bedeutsames Wort über Goethe gesprochen, ein Wort, das zu jenen gehört, die durch ihre Wendung gerade methodisch bedeutsam sind und tief hineinleuchten in das, was sie beleuchten sollen. Er gebrauchte für Goethes ganze Anschauungsweise das Wort «Gegenständliches Denken», und er erläuterte dieses Wort, indem er sagte: Goethes Denken ist ein ganz eigenartiges Denken, das sich eigentlich nicht von dem Objektiven der Gegenstände trennt, das ruhig in den Gegenständen lebt, in denen es sich bis zu den Ideen erhebt.",
      "Wer nun tiefer in Goethes ganze Geistesorganisation hineinzublicken vermag, wie wir es heute und übermorgen tun werden, wo wir versuchen wollen, noch tiefer in dieses Thema hineinzudringen, wo wir mehr innerlich betrachten werden, was heute äußerlich vor uns hingestellt werden soll, der wird sehen, daß er in diesem Denken in einer ge­wissen Weise, ohne auf der Oberfläche der Dinge und an",
      "der Sinneserfahrung haften zu bleiben, doch bei den Tat­sachen bleibt, und innerhalb derselben das Geistige, die Ideenwelt findet. Wir sehen, daß Goethes Denken gerade in dieser Art für einen großen Teil unserer modernen Menschheitsentwickelung so bedeutsam geworden ist. Wir dürfen sagen, es ist etwas höchst Eigenartiges mit dieser Wirkung des Goetheschen Geistes auf die verschiedensten Menschen, auf die verschiedensten Anschauungen, ja, auf die verschiedenen aufeinander folgenden Epochen.",
      "Betrachten wir einmal, um was es sich hier eigentlich handelt, und wir werden sehen, wie eigenartig Goethes Geistesart tatsächlich gewirkt hat. Wenn wir zum Beispiel die drei Philosophen des deutschen Geisteslebens vor unsere Seele treten lassen, die im Grunde genommen, ihrer gan­zen Anschauungsweise nach, sehr verschieden sind: Fichte, Hegel, Schopenhauer, so ergibt sich uns aus der Betrachtung ihres gegenseitigen Verhältnisses, aus der Betrachtung des Zusammenhanges in ihren Verhältnissen zu Goethe etwas ganz Eigenartiges über die welthistorische Wirkung der Goetheschen Geistesart.",
      "Fichte erweist sich als ein in abgezogenen Höhen schwe­bender Denker, und ganz besonders war er in abgezogenen Höhen schwebend, als er im Jahre 1794 seine Grundzüge der Wissenschaftslehre in Jena beendet hatte. Es ist schwer, sich zum Verständnis der Fichteschen Eigenart zu erheben, es ist schwer, ihn zu durchdringen, obwohl niemand, der in ihn eindringt, sich nicht sagen müßte, daß er ungeheure Früchte für seine Geistesdisziplin aus ihm schöpfte. Aber es ist nicht jedermanns Sache, in solche Sphären des reinsten Begriffes hinaufzuwandern. Dieser Fichte, der in solch ab­strakten Höhen wandelte, besonders damals, schickte seine «Wissenschaftslehre» mit folgenden bedeutungsvollen Wor­ten an Goethe: «Ich betrachte Sie, und habe Sie immer betrachtet",
      "als den Repräsentanten der reinsten Geistigkeit des Gefühls auf der gegenwärtig errungenen Stufe der Hu­manität. An Sie wendet mit Recht sich die Philosophie. Ihr Gefühl ist derselben Probierstein.» So Fichte zu Goethe.",
      "Sehen wir jetzt auf einen anderen Philosophen, auf Schopenhauer, und sehen wir zuerst, wie Schopenhauer zu Fichte stand. Wahrhaft feindliche Brüder waren sie, wenig­stens war Schopenhauer ein recht feindlicher Bruder zu Fichte. Schopenhauer wird nicht müde, in geradezu Schimpf-worten sich über Fichte zu ergehen. Ein Windbeutel ist er ihm, der in leeren Begriffen gesonnen und geschrieben hat. Immer wieder kommt er darauf zurück, die Wesenlosigkeit, Bedeutungslosigkeit und Unrealität der Fichteschen Philo­sophie zu betonen. Wahrlich, es kann keine größeren Ge­gensätze geben, als Schopenhauer und Fichte. Und Scho­penhauer ging wahrhaftig zu Goethe in die Lehre. Eine Zeitlang hindurch hat er zusammen mit Goethe experimen­tiert, um sich die physikalischen Grundbegriffe klarzuma­chen, und manches, was in Schopenhauers erstem Werke und auch in seinem Hauptwerke steht, ist hervorgegangen aus dem Eindrucke, den Goethe auf ihn gemacht hat. Wer Schopenhauer kennt, weiß aber auch, wie hingebungsvoll er von Goethe sprach. Schopenhauer und Fichte, zwei große Gegensätze, in Goethe vereinigen sie sich und er erscheint wie die vereinigende Kraft der beiden.",
      "Nehmen wir endlich Hegel und Schopenhauer! Auch Hegel ist schwierig mit dem Verständnis zu erreichen. Er, der versucht, sich eine Tatsachenwelt der Begriffe in einer umfassenden, systematischen Organik zu verschaffen, ver­langt, daß der Mensch sich auf eine Stufe erhebt, wo er den Begriff als Tatsache erfaßt, wo er fähig wird, ihn erleben zu können. Schopenhauer findet auch in dieser Begriffs-technik etwas völlig Wertloses; alles sei ein Spiel mit abstrakten",
      "Worten. Und wenn wir uns nun wieder das Ver­hältnis von Hegel zu Goethe vergegenwärtigen wollen, so brauchen wir nur eines zu nennen und wir werden sehen, wie Hegel zu Goethe steht. Einen schönen Brief gibt es, worin Hegel schreibt: Goethe sucht nach den tatsächlichen, geistigen Phänomenen, die hinter den sinnlichen stehen, die Goethe die Urphänomene nennt, wie er die Urpflanze das Urphänomen der Pflanzenwelt nennt. - Während Hegel als Philosoph aus der Höhe der geistigen Welt spricht und uns zeigt, was wir denken und begreifen können, arbeitet er sich auf der anderen Seite hinauf bis zu dem Punkte, wo er mit den aus dem Geiste geschöpften Begriffen in Berüh­rung kommt. So vereinigt sich Goethes Urphänomen mit dem, was die reine, denkende Philosophie von oben erfaßt. Auch hier sehen wir eine Harmonie zwischen Hegel und Goethe wie zwischen Goethe und Schopenhauer. In Goethe finden sie sich zusammen. Und wenn wir von diesen älteren Zeiten in unsere Zeiten heraufgehen, was finden wir da?",
      "In jener Zeit, in der Goethe selber gelebt hat, hat sozusagen das naturwissenschaftliche Forschen noch eine ganz andere Physiognomie gehabt. Noch mehr, als es zu Goethes Zeiten der Fall war, betrachtet man heute als die einzig richtige Methode der strengen Wissenschaft die Forschung, die sich auf die äußere Sinnesbeobachtung stützt, und das reinliche Herausarbeiten dessen, was der Verstand, der sich auf die Beobachtung beschränkt, aus den so gewonnenen Resultaten machen kann. Aber auch ein Haed'el will, wie er in jedem Buche wieder betont, auf dem festen Boden gerade Goethe­scher Weltanschauung stehen, und so sehen wir eine mehr materialistisch gefärbte Weltanschauung geradezu Wert darauf legen, an Goethe sich anzulehnen. Sie können aber auch heute noch Schriften finden, die auf einem Boden ste­hen, für den der Geist eine absolute Realität im eminentesten",
      "Sinne des Wortes ist, und auch bei ihnen können Sie die Berufung auf Goethe bemerken. Feindlich können sich spiritualistische und materialistische Forscher gegenüber­stehen, beide glauben sie aber in gleicher Art zu Goethe aufschauen zu können. So bietet er auch da etwas, was Gegensätze überbrückt.",
      "Diese Tatsachen bezeugen die Kraft der Goetheschen Weltanschauung, die Kraft, die so auf die andern wirkt, daß das, was sich gegenseitig nicht versteht, bei Goethe etwas findet, was es selbst besitzt. Vielleicht wissen einige von Ihnen, in welchem Gegensatze Virchow und Haeckel sich befanden. Aber auch Virchow, der in so wenig Dingen mit Haeckel übereinstimmt, hat sich in einem bedeutungs­vollen Vortrag über Goethe ebenfalls an Goethe angelehnt. Wir haben also in Goethe eine Kraft, die gegenüber den Gegensätzen, dem Kampfe der Weltanschauungen, das in ihnen Gemeinsame bei sich anklingen zu lassen vermag, eine Kraft, die in der Lage ist, zu zeigen, daß es im Grunde genommen bei den Weltanschauungen nicht so ist, wie diese Vertreter der Wissenschaft behaupten und so beharrlich verfechten.",
      "Gerade wenn man das Verhältnis dieser bedeutenden Menschen zu Goethe betrachtet, wird man zu der Erkennt­nis kommen, daß mit dem, was die Menschen Erkenntnis nennen, es sich verhält wie mit den verschiedenen Malern, die um einen Berg herumsitzen, ihn anblicken und von den verschiedensten Standpunkten aus ihn malen. Die Bilder, die sie da bekommen, müssen natürlich sehr verschieden sein, und doch war es derselbe Berg, den sie malten. Eine umfassende Vorstellung von dem Berge wird man nur be­kommen können, wenn man die verschiedenen Darstellun­gen miteinander vergleicht und sie zu einem Ganzen zu-sammenfügt. Wenn man sich so zu den Erkenntnissen stellt,",
      "dann wird man sehen, daß Goethe sich nicht einen einzel­nen Gesichtspunkt wählt, sondern den Berg hinansteigt und zeigt, daß es eine Möglichkeit gibt, den Standpunkt auf dem Bergesgipfel einzunehmen und dort ein umfassendes Panorama zu finden, wo alle Anschauungen in ihrer tiefe-ren Verträglichkeit sich zeigen.",
      "Das ist es aber auch, was Goethe zu einem so eminent modernen Geiste macht, und wenn wir bei einem rückhalt­losen Eingehen auf Goethe das Gefühl erhalten, daß er uns als ein moderner Geist erscheint, dann wird es von selbst schon eine Rechtfertigung sein, wenn wir in den hier oft angestellten Betrachtungen über die Geisteswissenschaft und eine vom Geistigen ausgehende Weltanschauung das, was er machte und wollte, als eine Art von Anleitung betrach­ten, tiefer in sein Wesen einzudringen. Wenn er in so vielen Beziehungen ein anregender Geist ist, warum sollte er da nicht auch ein anregender Geist sein für diejenige Geistes­strömung, die als eines ihrer höchsten und schönsten Ziele das tolerante Eindringen in die verschiedenen Standpunkte der Weltanschauungen hat, und die sich zum Prinzip macht, nicht auf einem einmal fixierten Standpunkte stehen zu bleiben, sondern, um Wahrheit zu finden, immer höher und höher zu steigen durch Methoden, die man auf seine innere Entwickelung, auf die Heranbildung innerer Wahrneh­mungsorgane anzuwenden hat, weil man dadurch, daß man sich seine inneren Organe heranzüchtet, erst dazu kommt, die tieferen geistigen Grundlagen zu sehen.",
      "Inwiefern Goethe auf einem eng begrenzten Gebiete die tiefsten Gefühle auch der heutigen Menschheit trifft, wollen wir jetzt noch betrachten. Beispielsweise sei ein Gefühl ge­wählt, das viele von Ihnen kennen, ein Gefühl, das man mit den Worten charakterisieren könnte, daß es in unserer Zeit Menschen gibt, die danach streben, manche alte Tradition",
      "über Bord zu werfen und sich Gefühle, Gedanken und Vorstellungen zu schaffen, die in die unmittelbare Ge­genwart hineinführen. Sie werden sogleich sehen, was ich meine, wenn ich Sie an ein Bild erinnere, das vielen in unserer Zeit wert geworden ist. Man mag zu dem Bilde stehen, wie man will, aber es ist ein Ausdruck der moder­nen Zeit. Ich meine das Bild: «Komm, Herr Jesus, sei unser Gast...» Das Bild lebt nicht nur bei dem, der es geschaffen hat, sondern auch in denen, die es genießen wollen; es lebt in ihnen die Sehnsucht, die Gestalt des Jesus in der un­mittelbaren Gegenwart zu sehen, wie sie sich hinstellt an den Tisch. Man könnte sagen, daß das Bild nicht nur Wert für diese Zeit hat, sondern für alle Zeiten, daß es ein ewiges, unvergängliches Dasein hat, und daß jede Zeit das Recht hat, diese Gestalt in ihre eigene Epoche hinein-zustellen. Nur mit diesen wenigen Worten sei das Gefühl angedeutet, das viele gegenüber diesem Bilde haben.",
      "Nun könnte man glauben, Goethe gehöre in dieser Be­ziehung noch zu den Alten. Man leitet das ja her aus seiner Vorliebe zu der alten Kunst, die an den alten, guten, künst­lerischen Traditionen festhalten wollte, aus seiner Vorliebe zu den Griechen. Man könnte glauben, Goethe hätte viel­leicht kein tieferes Verständnis für eine Empfindung, wie sie in dem Bilde charakterisiert ist: «Komm, Herr Jesus, sei unser Gast.» Um da einmal einen Blick in Goethes Seele zu tun, wollen wir uns an ein Buch anlehnen, an Bossis Buch über Lionardo da Vincis Abendmahl. Goethe schrieb eine Rezension über dieses Buch. Darin stehen bedeutungsvolle Worte. Von diesem Bilde, das sich im Speisesaale des Klo­sters Santa Maria delle Grazie in Mailand befindet, und das trotz der in letzter Zeit vorgenommenen Restauration den Eindruck macht, als wenn es dem Verfall entgegen-ginge, von diesem Bilde erzählt Goethe, wie er selbst einmal",
      "demselben gegenübergestanden habe zu einer Zeit, als es noch in einer gewissen Frische erhalten war. Und er schil­dert den Eindruck, den er einst von diesem Bilde in seiner Jugend bekommen habe: «Dem Eingang an der schmalen Seite gegenüber, im Grunde des Saals, stand die Tafel des Priors, zu beiden Seiten die Mönchstische, sämtlich auf einer Stufe vom Boden erhöht; und nun, wenn der Hereintre­tende sich umkehrte, sah er an der vierten Wand über den nicht allzuhohen Türen den vierten Tisch gemalt, an demsel­ben Christus und seine Jünger, eben als wenn sie zur Gesell­schaft gehörten» - Ihn, der von den Dominikanern in ihrem Sinne, ihrer Stellung mit der Empfindung aufgerufen wor­den ist: «Komm, Herr Jesus, sei unser Gast».",
      "Es schließe sich, sagt Goethe, das Ganze zu einem einheitlichen Bilde zusammen. Und um gar keinen Zweifel daran zu lassen, was er eigentlich meinte, sagte er noch: «Es muß zur Speise-stunde ein bedeutender Anblick gewesen sein, wenn die Tische des Priors und Christi, als zwei Gegenbilder, auf­einanderblickten und die Mönche an ihren Tafeln sich da­zwischen eingeschlossen fanden.",
      "Und eben deshalb mußte die Weisheit des Malers die vorhandenen Mönchstische zum Vorbilde nehmen. Auch ist gewiß das Tischtuch mit seinen gequetschten Falten, gemusterten Streifen und aufgeknüpf­ten Zipfeln aus der Waschkammer des Klosters genommen, Schüsseln, Teller, Becher und sonstiges Geräte gleichfalls denjenigen nachgeahmt, der sich die Mönche bedienten.",
      "Hier war also keineswegs die Rede von Annäherung an ein unsicheres, veraltetes Kostüm. Höchst ungeschickt wäre es gewesen, an diesem Orte die heilige Gesellschaft auf Polster auszustrecken. Nein, sie sollte der Gegenwart angenähert werden, Christus sollte sein Abendmahl bei den Domini­kanern zu Mailand einnehmen.»",
      "Und nun fragen wir: Hatte Goethe gerade dieses Verständnis,",
      "das man ein modernes Verständnis nennen muß? Er hatte es in jenem umfassenden Stile, der uns wieder ein Beweis dafür sein kann, wie universell seine Kraft ist gegen­über den manchmal einseitigen Kräften, die sich gegenseitig ausschließen und bekämpfen. So müssen wir uns hinein­versetzen in Goethes Seele und wir werden dann begreifen, warum Goethe uns ein so Nahstehender sein kann, und warum wir zu ihm hinaufschauen dürfen, wenn es sich um die vorläufige Orientierung über tiefere Geistesfragen han­delt. Das war Goethes tiefes Bewußtsein, daß es möglich ist für den Menschen, in sich geistige Organe zu erwecken, um hinaufzusteigen zu höheren Anschauungen und dadurch etwas zu gewinnen, was nicht bloß im Geiste des Menschen lebt, sondern was zu gleicher Zeit tiefer liegt.",
      "Wenn hier die Möglichkeit wäre, auf Goethes natur­wissenschaftliche Studien einzugehen, wie Sie dieselben in meinem Buche «Goethes Weltanschauung» ausführlich be­sprochen finden, so könnten wir zeigen, wie diese ganze Goethesche Methode wirkt. Aber wir wollen uns heute Goethe von einer anderen Richtung her nähern. Goethe hatte mancherlei zum Ausdrucke gebracht, was uns auf die tiefe Grundlage seiner Weltanschauung hinweisen kann. Wir werden darüber in den zwei Vorträgen dieses Winter­zyklus über Goethes «Faust» zu sprechen haben. Über ihn sagte er einmal zu Eckermann, daß er ihn so gestaltet habe, daß der Leser, wenn er sich nur an äußere Belehrungen hal­ten will, schon in den bunten Bildern etwas hat; daß er aber auch hinter den Worten die Geheimnisse finden kann, die sich darin befinden. Da weist Goethe in dem zweiten Teil darauf hin, daß zu unterscheiden ist das, was das Außere, und das, was das Innere, das Wesen ist, das, was er hinein­geheimnißt hat. Nach alter Weise bezeichnet man das Äußere als das Exoterische, das Innere als das Esoterische.",
      "Nun wollen wir uns Goethe dadurch nähern, daß wir das Werk, in dem er sein ganzes methodisches Denken und Wollen zum Ausdruck gebracht hat, heute in einer äußer­lichen, exoterischen Weise, und übermorgen dann in einer innerlichen, esoterischen Weise betrachten. Ein verhältnis­mäßig unbekanntes Werkchen von Goethe ist es, an das man sich halten muß, wenn man Goethes tiefste Erkennt­nisgeheimnisse - so darf das, um was es sich hier handelt, wohl genannt werden - durchschauen will. Es ist das Werk­chen, das am Ende der «Unterhaltungen deutscher Aus­gewanderter» unter der Überschrift: «Märchen» steht, und bei dessen Lektüre der, welcher danach strebt, in Goethes Weltanschauung tiefer einzudringen, von Anfang an die Empfindung haben wird, daß Goethe damit mehr sagen will, als was die Bilder zunächst darbieten. Rätsel über Rätsel wird dem sinnenden Betrachter dieses «Märchen» von der grünen Schlange und der schönen Lilie vorlegen.",
      "Und nun gestatten Sie mir, daß ich die hauptsächlichsten Züge dieses Märchens zunächst hier auseinandersetze, denn es ist nicht möglich, über das Märchen zu sprechen, ohne daß wir uns wenigstens diejenigen Züge vor die Seele führen, welche von Wichtigkeit sind, wenn wir einen tie­feren Blick in Goethes Weltanschauung werfen wollen. Es wird also notwendig sein, daß wir einige Zeit dem Inhalte dieses Werkchens widmen; aber dafür werden wir uns auch dann in bezug auf das, was wir zu sagen haben, um so besser verstehen. Es ist mir immer wieder passiert, wenn ich einen Vortrag über dieses Märchen gehalten habe, daß man mir sagte: «Ich weiß nichts davon, daß in Goethes Werken ein Märchen steht.» Ich wiederhole deshalb: es ist in jeder Goetheausgabe enthalten und bildet den Schluß der «Unterhaltungen deutscher Ausgewanderter».",
      "Nun zu den Bildern! An einem Flusse wohnt ein Fähr­mann. Zu diesem Fährmann kommen merkwürdige Ge­stalten: Irrlichter. Sie wollen von dem Fährmann in dem Kahne an das andere Ufer des Flusses hinübergesetzt wer­den. Der Fährmann geht darauf ein und setzt sie über den Fluß hinüber. Sie betragen sich dabei sonderbar, sind un­ruhig und zappelig, so daß er Angst bekommt, sie könnten ihm den Kahn umwerfen. Er führt sie aber glücklich hin­über, und als sie angelangt sind, wollen sie ihn in eigen­artiger Art bezahlen. Sie schütteln sich und es fallen Gold-stücke von ihnen ab; das soll der Lohn sein für die Mühe des Übersetzens. Der Fährmann ist wenig erbaut von den Goldstücken und sagt: Es ist gut, daß nichts in den Fluß gefallen ist, denn er würde wild aufwallen. Ich kann diese Bezahlung aber nicht annehmen, ich kann nur mit Früchten der Natur bezahlt werden. - Und er verlangt drei Zwie­beln, drei Artischocken, drei Kohlköpfe. Mit Früchten soll­ten sie also bezahlen. Wir werden gleich sehen, welche tiefe Bedeutung jeder Zug und jede einzelne Tatsache hat.",
      "Nun sagt der Fährmann weiter: So macht ihr mir noch die Mühe, daß ich das, was ihr als Goldstücke herumgewor­fen habt, den Fluß hinunterführen und begraben muß. -Darauf führt er die Goldstücke tatsächlich ein Stück den Fluß hinunter und vergräbt sie in den Klüften der Erde. Als sie da hinein vergraben worden sind, kommt ein merk­würdiges anderes Wesen an diese Goldstücke heran: die grüne Schlange, die in und auf der Erde herum und durch die Klüfte der Erde hindurchkriecht. Plötzlich sieht sie durch die Spalten der Erde die Goldstücke hereinfallen. Zunächst glaubt sie, daß sie vom Himmel hereinfallen. Sie verzehrt sie aber dann und wird durch die Aufnahme dieser Goldstücke in den eigenen Leib immer leuchtender. Als sie aber an die Oberfläche geht, merkt sie, daß sie in wunderbarer",
      "Weise ein eigenartiges Licht ausstrahlt, leuchtend wie Smaragd und Edelstein.",
      "Nun treffen die Schlange und die Irrlichter zusammen, die Irrlichter immer noch sich schüttelnd und wegwerfend, was sie in sich haben. Die Schlange, die jetzt Geschmack an dem Golde bekommen hat, nimmt in ihren eigenen Leib auf und verarbeitet, was die Irrlichter um sich werfen. Be­deutsames sagen sich die Schlange und die Irrlichter über ihr gegenseitiges Verhältnis. Die Schlange nennt sich Ver­wandte der Irrlichter von der horizontalen Linie und die Irrlichter sich Verwandte der Schlange von der vertikalen Linie. Die Irrlichter fragen noch die Schlange, ob diese nicht Auskunft geben könne, wie sie zur schönen Lilie kommen könnten. Da sagt die Schlange: Die schöne Lilie ist jenseits des Flusses. - Nun, dann haben wir uns etwas Schönes ein­gebrockt! antworten die Irrlichter. Wir haben uns herüber-fahren lassen, weil wir zur schönen Lilie kommen wollten. Könnten wir nur einen Fährmann erreichen, der uns wieder zurückführt! Und nun kommen bedeutungsvolle Worte:",
      "Ihr werdet den Fährmann nicht wiederfinden, und wenn ihr ihn fändet, seid euch klar darüber, daß er euch wohl herüber, aber nicht mehr zurückführen darf. Wenn ihr wie­der auf die andere Seite des Flusses zurück wollt, so könnt ihr es nur auf zweierlei Weise. Entweder ihr versucht am Mittag, wo die Sonne am höchsten steht, eine Brücke zu finden über meinen eigenen Leib, um hinüber zu kommen. -Die Irrlichter sagen: Die Mittagsstunde ist eine Zeit, in der wir nicht gerne reisen. - Oder ihr benützt den zweiten Weg. Es giht nämlich noch eine andere Möglichkeit. In der Dämmerstunde findet ihr an einer bestimmten Stelle den großen Riesen. Er hat gar keine Kraft in sich, aber wenn er seine Hand ausstreckt und der Schatten dieser Hand über den Fluß hinüberfällt, so kann man über den Schatten hinweg",
      "den Fluß überschreiten. Der Schatten hat die Trag­kraft, daß man hinübergehen kann. Wenn ihr also nicht über mich selber gehen wollt zur Mittagsstunde, so suchet den Riesen auf. - Die Irrlichter lassen sich das gesagt sein. Die Schlange aber ist wieder in die Klüfte der Erde zurück­gegangen und freut sich des innerlichen Leuchtend -Werdens durch Aufnahme des Goldes.",
      "Nun bemerkt die Schlange etwas höchst Merkwürdiges. Als sie die Klüfte wieder absucht, bemerkt sie, daß sie da, wo sie früher unregelmäßige Naturprodukte gefunden hatte, jetzt an einer Stelle merkwürdige Gebilde sieht. Frü­her hat sie sie nur durch den Tastsinn wahrgenommen, jetzt, wo sie leuchtend ist, merkt sie, daß sie die Dinge auch sehen kann. Sie konnte Säulen und auch menschenähnliche Gebilde abtasten, aber es war ihr bis dahin nie klargewor­den, was da in den unterirdischen Klüften eigentlich ist. Jetzt bewegt sie sich wieder hinein und das von ihr aus­strahlende Licht dient ihr zur Beleuchtung der Dinge.",
      "Als sie hineindringt in diese große Höhle unter der Erde, kann sie sogleich wahrnehmen, wie in den vier Ecken vier königliche Gestalten stehen: ein goldener König, ein silber­ner König, ein eherner König und in der vierten Ecke ein gemischter König, eine Gestalt, welche aus den anderen Metallen in der buntesten Weise zusammengefügt ist, so daß in ihm alle möglichen Metalle chaotisch ineinander-gefügt sind.",
      "In dem Augenblicke, wo die Schlange in die Höhle hineinkommt und ihr die Beleuchtung der Gestalten ge­lingt, stellt der goldene König die sehr bedeutungsvolle",
      "«Wo kommst du her?»",
      "«Aus den Klüften», versetzte die Schlange, «in denen das Gold wohnt.»",
      "«Was ist herrlicher als Gold?» fragte der König.",
      "Die Schlange antwortet: «Das Licht!»",
      "Und der König fragt weiter: «Was ist erquicklicher als Licht?»",
      "«Das Gespräch.»",
      "Niemand wird bezweifeln, daß in diesen Worten nicht bloß Bilder gegeben werden sollen, sondern daß sie auch einen bedeutungsvollen Inhalt haben.",
      "Als die Schlange hineinkommt in die Höhle, öffnet sich ein Spalt an dem Tempel, in dem die vier Könige wohnen. Es kommt der Alte mit der Lampe in den Raum, und er wird gefragt, warum er gerade jetzt komme? Da sagt er das merkwürdige Wort: Wißt Ihr nicht, daß mein Licht nur er­leuchten darf, was schon erleuchtet ist? daß ich das Dunkle nicht erleuchten darf? - Nachdem die Schlange die Dinge im Raume erleuchtet hat, darf nun auch er mit seiner wun­derwirkenden Lampe kommen.",
      "Jetzt entspinnt sich aufs neue ein Gespräch zwischen den Königen und dem Alten mit der Lampe. Der Alte wird gefragt:",
      "«Wie viele Geheimnisse weißt Du?»",
      "«Drei», antwortet er.",
      "«Welches ist das wichtigste?» fragt der silberne König.",
      "«Das offenbare», versetzt der Alte.",
      "«Willst du es auch uns eröffnen?» fragt der eherne König.",
      "«Sobald ich das vierte weiß.»",
      "Und nun kommen die allerbedeutsamsten Worte des Märchens: «Ich weiß das vierte», sagt die Schlange und zischelt ihm etwas in das Ohr, worauf der Alte mit gewal­tiger Stimme ruft: «Es ist an der Zeit!»",
      "Es gibt eine große Anzahl von Versuchen, die Rätsel dieses Märchens zu lösen. Viele haben auch versucht, das, was man schon zu Schillers und Goethes Zeiten als Rätsel",
      "empfand, so oder so zu deuten. Es ist eigenartig, daß Goethe und Schiller sich darüber einig waren und es aus­drücklich mit den Worten aussprachen: Es liegt das Wort der Lösung für das Märchen im Märchen selber. Also darf man nach des Märchens Lösung nur im Märchen selber suchen, und es wird sich im weiteren Verlauf des Vortrages auch finden, daß das Wort des Rätsels, wenn auch in eigen­artiger Weise, in dem Märchen drinnen ist. Die Schlange zischelt dem Alten etwas ins Ohr, und das, was sie ihm ins Ohr zischelt, was aber nicht gesagt wird, das ist die Lösung des Rätsels. Dann sagt der Alte: «Es ist an der Zeit!» Was also ergründet werden muß, das ist, was die Schlange im unterirdischen Tempel dem Alten ins Ohr geraunt hat.",
      "Der Alte geht nun mit seiner Lampe dahin, wo seine Gattin wohnt. Durch die Kraft des Lichtes der Lampe wer­den die verschiedensten Materien verwandelt: Steine in Gold, Holz in Silber, tote Tiere in Edelsteine, Metalle aber werden vernichtet. Er trifft seine Gattin in geradezu fassungslosem Zustande. Als er fragt, was passiert sei, sagt sie: Es waren ganz merkwürdige Persönlichkeiten da. Man hätte sie für. Irrlichter halten können. Die sind sehr wenig in den Grenzen des Anstandes geblieben. - Nun, meint der Alte, bei deinem Alter wird es wohl bei der allgemeinen Höflichkeit geblieben sein. - Und nun erzählt sie, wie die Irrlichter sich an das Gold herangemacht und es abgeleckt haben, damit sie es wieder abschütteln könnten. Wenn es nur noch das wäre, aber sieh dir mal den Mops an. Der hat von den Goldstücken gefressen, wurde in Edelstein ver­wandelt und starb. Jetzt ist er tot. - Und die Alte sagt weiter: Wenn ich das vorher gewußt hätte, so würde ich ihnen nicht versprochen haben, daß ich ihre Schuld bei dem Fährmann abzahlen werde. Das sind: drei Kohlhäupter, drei Zwiebeln und drei Artischocken.",
      "Nun, sagte der Alte, nimm doch den Mops mit, trage ihn zur schönen Lilie hin, die hat die Eigenschaft, daß sie alles, was Edelstein ist, durch ihre Berührung in Lebendiges ver­wandeln kann. - Sie nimmt also die drei mal drei Früchte, um die übernommene Schuld bei dem Fährmann abzutra­gen, und legt den Mops dazu.",
      "Nun kommt ein sehr bedeutungsvoller Zug des Mär­chens: Als sie den Korb trägt, erscheint er ihr außerordent­lich schwer, obgleich das Tote für sie gar kein Gewicht hat, der Korb mit dem toten Mops allein würde so leicht sein, als wenn er leer wäre; nur durch das Lebendige, durch die Kohlköpfe, Zwiebeln und Artischocken wird der Korb schwer. Auf dem Wege zu dem Fährmann passiert ihr aber noch etwas Eigentümliches. Der Riese legt seinen Arm ge­rade so, daß der Schatten über den Fluß hinüberfällt, greift ihr ein Kohlhaupt, eine Artischocke und eine Zwiebel aus dem Korbe heraus und verzehrt sie, so daß sie jetzt nur noch zwei von jeder Gattung hat. Sie will daher dem Fähr­mann nur einen Teil der Schuld abtragen. Er aber sagt, daß es unbedingt notwendig sei, das Ganze gleich mitzubringen.",
      "Nach vielem Hin- und Herreden sagte der Fährmann: es gäbe noch einen Ausweg, der wäre, wenn sie Bürgschaft für die Beibringung der drei fehlenden Früchte leiste. Sie muß daher die Hand in den Fluß stecken, als Sicherheit dafür, daß sie ihr Versprechen halten werde. Das tut sie, bemerkt aber dann, daß, soweit die Hand in den Fluß hineingesteckt war, sie schwarz und kleiner geworden ist. «Jetzt scheint es nur so», sagte der Alte. «Wenn ihr aber nicht Wort haltet, kann es wahr werden. Die Hand wird nach und nach schwinden und endlich ganz verschwinden, ohne daß ihr den Gebrauch derselben entbehrt. Ihr werdet alles damit verrichten können, nur daß sie niemand sehen wird.» Sie will aber lieber, daß man sie sehe, auch wenn sie nichts mit",
      "der Hand tun könne. Wenn sie zu entsprechender Zeit den Tribut bringt, sagt der Fälirmann, wird alles wieder gut werden.",
      "Auf dem Wege zur schönen Lilie trifft sie nun einen herr­lich-schönen Jüngling, dem aber, wie er sagt, alle seine einstige Kraft und Stärke geschwunden ist; und aus dem Gespräche, das sie miteinander führen, erfahren wir, wie das gekommen ist. Der Jüngling hatte die lebhafte Begierde gefaßt, zur schönen Lilie zu gelangen. Sie war sein Ideal geworden. Aber ihre schönen Augen wirkten so unselig, daß sie ihm alle seine Kraft genommen hatten und dennoch zieht es ihn immer wieder zu ihr hin.",
      "Endlich kommen die beiden zur schönen Lilie hin. Es ist nun zwar alles, was die schöne Lilie umgibt, im höchsten Grade bezeichnend; aber wir können hier nur einzelne Züge herausnehmen. Die schöne Lilie ist das Bild vollkom­menster Schönheit; aber sie hat die Eigenschaft, daß sie alles Lebendige durch ihre Berührung zunächst tötet, und alles, was durch das Leben hindurchgegangen und dem Tode ver­fallen ist, wieder lebendig macht.",
      "Die Alte bringt nun ihr Anliegen vor. Der Jüngling ist gekommen, seine Sehnsucht nach der schönen Lilie zu be­friedigen; wir sehen aber auch, daß die schöne Lilie eben­falls Sehnsucht fühlt. Sie fühlt sich fern von allem fruchtbar Lebendigen; in ihrem Garten gedeihen Pflanzen, aber nur bis zur Blüte, nicht bis zur Frucht; schön ist sie, aber fern von allem Lebendigen. Die Alte sagt dann ein bedeutungs­volles Wort. Sie wiederholt, was der Mann im unterirdi­schen Tempel gesagt hat, und das gibt der Lilie neue Hoff­nung. Das war aber auch der letzte Augenblick, in dem sie Hoffnung fassen konnte; denn das letzte Lebendige, das eine Art Verbindungsband zwischen ihr und dem Leben­digen gebildet hatte, war ihr auch noch verlorengegangen.",
      "Sie hatte einen Kanarienvogel in ihrer Umgebung, und hatte sich sehr gehütet, ihn zu berühren, weil ihn das ge­tötet haben würde. Nun aber war ein Habicht in die Nähe gekommen, der Kanarienvogel floh vor ihm, flog auf die Lilie zu und wurde getötet. Und damit war die schöne Lilie nun in völliger geistiger Einsamkeit und Abgesondertheit von dem, was die Menschen haben.",
      "Nun gibt die Alte der Lilie den Mops. Die Lilie berührt ihn und macht ihn dadurch wieder lebendig. Der Jüngling sucht seine Sehnsucht dadurch zu stillen, daß er die Lilie umfaßt. Dadurch wird er vollends getötet. Das Leben in ihm wird ganz vernichtet.",
      "Die Schlange bildet nun einen magischen Kreis. In diesen Kreis werden der Jüngling und der Kanarienvogel hinein­gelegt. Dadurch soll sich - und die Schlange deutet bedeu­tungsvoll darauf hin - das, was trostlos ist, in allernächster Zeit ändern. Und es ändert sich in der Tat. Wir erfahren, daß nun auch der Alte mit seiner Lampe herankommt, und daß durch ihn tatsächlich eine Lösung der ganzen Situation in Angriff genommen werden kann. Denn es ist gerade Zeit, als der Alte herankommt: die Körper von dem Kana­rienvogel und dem Jüngling sind noch nicht in Verwesung übergegangen.",
      "Der Alte führt sie nach dem unterirdischen Tempel hin, den die Schlange ja schon ausgekundschaftet hatte. Er sagt zu den Irrlichtern: Ihr seid auch dazu geeignet, uns zu die­nen. Wenn wir an die Pforte des Tempels gelangen, werdet Ihr es sein müssen, die uns die Pforte aufschließen. - Nun bildet die Schlange eine Brücke über den Fluß. Der ganze Zug geht über die Schlangenbrücke. Da sehen wir, als sie drüben angekommen sind, daß durch die Berührung mit der Schlange, die jetzt sich zu opfern beschließt, der Jüng­ling zwar noch nicht durchgeistigt, aber doch lebendig wird.",
      "Er geht dadurch, daß die Schlange bereit ist, sich hinzu-opfern, in einen merkwürdigen Zustand über. Er kann wohl sehen, aber das Gesehene noch nicht fassen.",
      "Die Schlange teilt sich in lauter wunderbare Edelsteine, die der Alte in den Fluß senkt und wodurch eine Brücke über den Fluß entsteht. Der Zug bewegt sich unter der An­führung des Alten in den unterirdischen Tempel. Als sie da hineinkommen, sehen wir, daß zwischen den Ankömmlin­gen und den Königen bedeutungsvolle Fragen gestellt wer­den, die darauf hindeuten, daß da ein großes Rätsel ver­borgen ist. Zum Beispiel: «Woher kommt ihr?» «Aus der Welt.» «Wohin geht ihr?» «In die Welt.» «Was wollt ihr bei uns?» «Euch begleiten!», nämlich die Könige.",
      "Nun bewegt sich die Gruppe mit dem Tempel. Sie gehen unter den Fluß und erheben sich dann wieder mit dem gan­zen Tempel. Als sie sich über den Fluß erhoben haben, fällt von oben etwas wie Bretterwerk in den Tempel hinein: es ist die Hütte des Fährmanns. Sie verwandelt sich und wird ein kleines Tempelchen im großen Tempel. Und jetzt spielt sich eine Szene ab, die von Wichtigkeit ist für den Jüngling, der ja bis jetzt belebt, aber noch nicht durchgeistigt war.",
      "Wir haben gesehen: der erste, der goldene König, stellt die Weisheit dar; der zweite, der silberne, den Schein oder die Schönheit; der dritte, der eherne, die Stärke oder den Willen. Wir sehen nun einen symbolischen Akt sich voll­ziehen. Der Jüngling wird durch die drei Könige mit drei verschiedenen Gaben begabt. Durch den ehernen König mit dem Schwert, und indem ihm das Schwert überreicht wird, werden die bedeutungsvollenWorte gesprochen: «Das Schwert an der Linken, die Rechte frei.» - Kraft des Wil­lens. - Durch den silbernen König bekommt er das Zepter mit den Worten: «Weide die Schafe.» Wir werden sehen, daß der Jüngling durch die Gefühlskraft der Seele erfüllt",
      "wird, die sich in der Schönheit ausdrückt. Der goldene König setzt ihm die Krone auf das Haupt, mit den Worten: «Er­kenne das Höchste.» Und die Kraft der Vorstellung erfaßt den Jüngling. In diesem Moment ist er durchgeistigt und darf sich mit der schönen Lilie vereinigen. Wir werden so­dann noch darauf aufmerksam gemacht, daß sich alles ver­jüngt.",
      "Besonders bedeutsam ist noch die eigentümliche Rolle, die der Riese spielt, der keine Kraft in sich selber, wohl aber in seinem Schatten hat. Er stolpert höchst ungeschickt über die Brücke, und der König ist ungehalten darüber. Es stellt sich aber heraus, daß das Kommen des Riesen seinen guten Sinn hat. Wie der Uhrzeiger einer großen Sonnenuhr da-steht, so wird er in der Mitte des Tempelhofes festgehalten. Wir sehen, welche Kraft wir in der Sonnenuhr, in dem die Zeit anzeigenden und harmonisierenden Riesen finden, und wir sehen, wie aus dem Leib der Schlange die Brücke, welche über den Fluß zu dem Tempel hinüberführt, gebildet wird. Wir sehen dann, daß nicht mehr bloß Fußgänger, sondern jetzt Wagen, Reiter, Herden hinüber- und herübergehen können. Es wird uns dargestellt, wie in der Vereinigung mit der schönen Lilie der Jüngling die frühere Kraft, die er durch die Berührung mit ihr verloren, wiedergewinnt, wie er sich jetzt der Lilie nähern, sie umfassen darf, und wie sie beglückt und beseligt beide sind.",
      "Wer möchte nicht, wenn er die Bilder des Märchens auf sich wirken läßt, sagen: Rätsel sind es! Zunächst können wir nur wenig spüren von dem, was in diesem Märchen lebt. Wenn wir aber historisch vorgehen, wenn wir betrach­ten, wie es in der Mitte des Jahres 1795 entsteht, im Beginn der Freundschaft mit Schiller, aus dem, was sich zwischen Goethe und Schiller zugetragen hat, dann werden wir be­greifen, was Goethe sich in dem Märchen für eine Aufgabe",
      "gestellt hat. In diese Zeit fällt die Abfassung eines Werkes, eine Frucht des Studiums Goethescher Weltanschauung, das tief bedeutsam wurde für die Erziehung und Kultivierung des deutschen Geisteslebens: die Briefe Schillers über die ästhetische Erziehung des Menschen. Nur skizzenhaft kön­nen wir darauf hinweisen, was Schiller mit diesen Briefen wollte.",
      "Er fragt sich, wie gelangt der Mensch dahin, seine Kräfte immer höher und höher zu entwickeln, damit er in einer freien und vollkommenen menschlichen Art in die Geheim­nisse der Welt eindringen kann. Dieses Werk ist in Brief-form an den Herzog von Augustenburg geschrieben, und Schiller schrieb darin den bedeutungsvollen Satz: «Jeder individuelle Mensch, kann man sagen, trägt, der Anlage und Bestimmung nach, einen reinen idealischen Menschen in sich, mit dessen unveränderlicher Einheit in allen seinen Abwechselungen übereinzustimmen die große Aufgabe sei­nes Daseins ist.» Und nun sucht Schiller auseinanderzuset­zen, wie sich der Mensch zu den höheren Stufen des Men­schendaseins hinaufzuentwickeln hat.",
      "Zweierlei ist es, was den Menschen unfrei macht, ihm keinen freien Blick in die Geheimnisse des Daseins gibt. Auf der einen Seite ist es das Beherrschtsein von der Sinnlich­keit, auf der anderen Seite die ungenügende Entwickelung der Vernunft. Und nun setzt Schiller diese Dinge so ausein­ander: Nehmen wir einen Menschen, der in sich nicht das Zwingende, Logische der Begriffe, auch nicht den Pflicht­begriff verspürt, sondern seinen Neigungen und Instinkten folgt - er kann die Kräfte seiner Natur nicht frei entwickeln, er steckt in der Sklaverei der Triebe, Begierden und In­stinkte, er ist unfrei. Aber auch derjenige ist nicht frei, der seine Begierden, Triebe und Instinkte zunächst bekämpft und einzig nur einer rein begrifflichen und logischen Vernunftnotwendigkeit",
      "folgt. Ein solcher Mensch wird ent­weder ein Sklave der Naturnotwendigkeit oder ein Sklave der Vernunftnotwendigkeit.",
      "Wodurch kann der Mensch seine inneren Kräfte ent­wickeln? Schiller antwortet: Er muß seine inneren göttlichen Zustände entwickeln, sich bemühen, daß sie gereinigt und geläutert werden und zusammentreffen mit dem, was wir Logik nennen. Wenn seine Triebe und Instinkte dann ge­läutert sind, so daß er gern tut, was er als Pflicht empfindet, wenn die Vernunftnotwendigkeit nicht als zwingend emp­funden wird, dann wird der Mensch gern tun schon aus dem gewöhnlichen Trieb heraus, was vernünftig ist, dann hat Vernunft den Menschen hinunter zur Sinnlichkeit ge­führt, und Sinnlichkeit führt ihn wieder hinauf zur Ver­nunft.",
      "Sehen wir einen Menschen an, der einem Kunstwerke gegenübersteht. Er sieht sich etwas Sinnliches an. Aber durch jedes Glied des Sinnlichen offenbart sich ihm etwas Geisti­ges, denn in dem Sinnlichen kommt dasjenige zum Aus­druck, was der Künstler als Geistiges in das Kunstwerk hineingelegt hat. Geist und Sinnlichkeit in der Anschauung der Schönheit, das wird zum Mittlerzustand. So wird die Kunst, das Leben in Schönheit, für Schiller ein großes Er­ziehungsmittel, ein Mittel zur ästhetischen Erziehung, eine Befreiung der Natur, so daß sie ihre eigenen Kräfte ent­falten kann. Wie entwickelt sich also der Mensch im Sinne Schillers. Er muß seine Natur hinunterführen, daß sie sich bewährt in sinnlicher Natur, und die Sinne hinaufentwik­keln, daß sie sich bewähren in der vernünftigen Natur.",
      "Ein wunderbar schönes Wort spricht Goethe über diese Briefe aus: Sie wirken auf mich so, daß sie mir darstellen, was ich lebte oder zu leben wünschte immerdar. - Man kann nachweisen, daß Goethe angeregt worden ist, sein",
      "Märchen zu schreiben, durch das, was Schiller ausgesprochen hat in seinen Briefen über die ästhetische Erziehung des Menschen. Goethe spricht darin dasselbe in seiner Art aus. Goethe wollte nicht in abstrakten Begriffen die Rätsel der Seele aussprechen. Für Goethe waren die einzelnen Seelen-rätsel zu reich und zu gewaltig, als daß er sie in Natur-notwendigkeit und Logik hätte fassen können. So bildete sich in Goethe das Bedürfnis, des Menschen einzelne Seelen-kräfte in den Gestalten seines Märchens zu personifizieren. Goethe antwortete auf die Schillersche Frage in seinem Mär­chen, und wir werden sehen, wie die Goethesche Psychologie in wunderbarerWeise in dem Märchen charakterisiert wird. Wir sehen, wie die Seele immer aufnimmt und von sich gibt in der Darstellung der Irrlichter, wie gewisse Kräfte per­sonifiziert sind in der Schlange, die nur auf derErde arbeitet gleich der menschlichen Forschung, dem menschlichen Ver­stand, der Erfahrung, die in der horizontalen Linie bleiben, während der Idealist in die Höhe steigt. Die Kraft des reli­giösen Gemütes ist charakterisiert in dem Alten mit der Lampe, und wir sehen endlich, wie durch die Vorgänge, die uns erzählt werden, Goethe darstellt, in welcher Weise eine jede Seelenkraft wirken muß.",
      "Wir werden übermorgen sehen, wie Goethe in der Dar­stellung zeigt, wie jede Seelenkraft maßvoll wirken muß zusammen mit den anderen Seelenkräften, um die Seele zu einem Gesamtbilde zu gestalten, auf daß sie sich ,,in­aufentwickeln könne zu menschlicher Vollkommenheit, zu einem Umfassen der Dinge. Wenn der Mensch unreif die Erkenntnisse erfassen will, so wird er getötet, wie der Jüng­ling. Es gibt ein Heranreifen der Erkenntnis. In dem Mär­chen stellt uns Goethe die Evolution der Seele in richtiger und bildhafter Weise dar, indem er darin das Parallelwerk zu Schillers «Briefen über die ästhetische Erziehung» schuf.",
      "Goethe wußte, daß es ein Ziel der menschlichen Seelen­entwickelung gibt, das man in alten Zeiten die Einweihung in höhere Geheimnisse genannt hat. Er wußte, daß es eine solche Möglichkeit gibt, und er wußte auch, daß es Gesell­schaften gibt, die an verborgenen Orten, in den Tempeln der Einweihung, die Kräfte der Seele entwickeln. Er zeigt auch, wie die neuere Zeit immer mehr dahin kommen muß, daß es der Menschheit möglich wird, im größeren Um­fange diese Einweihung zu erlangen, die Seele zu ent­wickeln. Er zeigt in den Vorgängen, die sich zwischen den einzelnen Menschen abspielen, den Vorgang der Einweihung bis zu den höchsten Stufen, bis dahin, wo die Seele fähig wird, die höchsten Geheimnisse zu erfassen. Das ist exo­terisch, rein historisch angesehen.",
      "Durch das Zusammenleben Goethes mit Schiller erlebte Schiller dasjenige, was Goethe erlebt hat, in einer der wich­tigsten Perioden seines Lebens. Und wenn es Schiller auch schwer wurde, Goethe zu verstehen, so müssen wir doch sagen: Das, was Schiller in abstrakter Weise in den ästheti­schen Briefen sagt, und was Goethe in viel umfassenderer Weise zu sagen hatte, in einer Weise, die nur erreicht wird, wenn man sich ausdrückt in Bildern und Persönlichkeiten, das ist ein und dasselbe. Das Märchen ist Goethe-Psychologie im tiefsten Sinne. Wir sehen, daß Goethe durch die Art sei­nes Strebens so fruchtbar geworden ist, daß wir uns heute noch gern bei ihm orientieren. Goethe erscheint uns noch heute als ein Gegenwärtiger. Wir lesen ihn wie einen Schrift­steller unserer Zeit. Er ist so fruchtbar, weil er so viel von Ewigkeitsgehalt in seinem Schaffen und seiner ganzen Art und Weise hat. So wirkt er im Sinne jener Wahrheit, die er selbst als die richtige angesehen hat, und ein bedeutungs­volles Wort hat er einst gesprochen: «Was fruchtbar ist, allein ist wahr. »",
      "Das heißt, daß der Mensch sich in den Besitz von Wahr­heiten setzen muß, die so wirken, daß, wenn er ins Leben hineintritt, sie ihre Bestätigung finden dadurch, daß sie sich fruchtbar erweisen. Das war für ihn das Kriterium der Wahrheit: Was fruchtbar ist, allein ist wahr!",
      "Gerade diese Vorträge, die Ihnen Goethe veranschau­lichen wollen, sollen uns zeigen, daß Goethe diesen Aus­spruch selber. erprobt hat. Das werden alle diejenigen füh­len, die sich tiefer in ihn hineinleben. Sie werden fühlen, daß in Goethe etwas von echter Wahrheit lebt, denn Goethe ist fruchtbar, und was fruchtbar ist, ist wahr."
    ],
    "sentences": [
      [
        "GOETHES GEHEIME OFFENBARUNG"
      ],
      [
        "Berlin, 22.",
        "Oktober 1908"
      ],
      [
        "Wer die geistige Entwickelungsgeschichte der Menschheit nicht nur nach den gewöhnlich üblichen Dokumenten und Traditionen verfolgt, sondern ein wenig tiefer geht, indem er sich auf manches einläßt, was vielleicht zunächst nur symptomatisch erscheinen könnte für die Menschheits-entwickelung, was aber doch intensiv hineinweist in die inneren und daher wahren Entwicklungskräfte, der wird eine denkwürdige Szene in der neueren Geistesgeschichte immer wieder und wieder bedeutungsvoll finden, eine Szene, die sich in den neunziger Jahren des achtzehnten Jahrhunderts in Jena zugetragen hat."
      ],
      [
        "Dazumal wurde in der Naturforschenden Gesellschaft in Jena von einem damals sehr bedeutenden Botaniker, na­mens Batsch, ein Vortrag gehalten, der durchaus auf der Höhe der damaligen Wissenschaftlichkeit stand.",
        "Zwei Män­ner, ein jüngerer und ein um zehn Jahre älterer, hörten sich diesen Vortrag an, und es trug sich zu, daß sie gleichzeitig aus dem Vortrag hinweggingen und miteinander ins Ge­spräch kamen.",
        "Der jüngere der beiden Männer sagte dabei zu dem älteren: Wenn man einen solchen Vortrag auf sich wirken läßt, so zeigt es sich doch immer wieder, wie die wissenschaftliche Betrachtungsweise die Dinge zerpflückt, wie sie das eine neben das andere hinstellt und das einheit­liche geistige Band, das in all' den verschiedenen Einzel­heiten lebt, so wenig berücksichtigt. - Es widerstrebte sozusagen"
      ],
      [
        "dem jüngeren Mann, daß da Pflanze an Pflanze hingestellt wurde, ohne Hinweis auf das, was als ein Hö­heres, die verschiedenen Pflanzen Verbindendes, doch auch in der Welt leben muß.",
        "Der ältere der beiden Männer sagte darauf, es könne sich vielleicht doch auch eine Betrachtungs­weise der Natur finden, die nicht so zu Werke geht, und die, trotzdem sie eine Erkenntnis ist, eine Betrachtung, die zur Erkenntnis führen muß, sehr wohl auf das Einheitliche geht, auf das, was getrennt ist in den für die verschiedenen Sinne äußerlichen Betrachtungen. - Der Mann nahm einen Bleistift und ein Stück Papier aus seiner Tasche und zeich­nete sogleich ein merkwürdiges Gebilde, ein Gebilde, wel­ches einer Pflanze ähnlich sah, aber keiner der lebenden Pflanzen, die man mit den äußeren physischen Sinnen sehen oder wahrnehmen kann, ein Gebilde, das sozusagen nir­gends einzeln verwirklicht ist, und von dem er sagte, daß es zwar in keiner einzelnen Pflanze lebe, aber die Pflanzen­heit, die Urpflanze in allen Pflanzen sei und das Verbin­dende ausmache. - Der jüngere Mann sah sich das an und sagte darauf: «Ja, was Sie da aufzeichnen, ist aber keine Erfahrung, das ist keine Beobachtung, das ist eine Idee» -und er hatte dabei im Sinne, daß solche Ideen nur der menschliche Geist ausbilden könne, und daß eine solche Idee keine Bedeutung habe für das, was draußen in der sogenannten objektiven Natur lebt."
      ],
      [
        "Der ältere der beiden Männer konnte diesen Einwand gar nicht recht verstehen, denn er erwiderte: Wenn das eine Idee ist, dann sehe ich meine Ideen mit Augen!",
        "Er meinte, daß in genau demselben Sinne, wie die einzelne Pflanze für den äußeren Sinn des Auges sichtbar ist, eine Erfahrung ist, so sei seine Urpflanze, obgleich sie nicht durch einen äußeren Sinn gesehen werden kann, ein Objektives, ein in der äußeren Welt Bestehendes, eben das, was in allen Pflanzen lebt, die Urpflanze in allen"
      ],
      [
        "einzelnen Pflanzen. - Sie wissen, daß der jüngere der beiden Männer Schiller, der ältere Goethe war."
      ],
      [
        "Dieses Gespräch ist eine symptomatische, bedeutungs­volle Kundgebung der neueren Geisteswissenschaft.",
        "Was sprach dazumal eigentlich in Goethe bei seiner Erwiderung gegenüber Schiller?",
        "In Goethe sprach das Bewußtsein, daß man nicht nur mit jener Vorstellung, die der äußere Sinn gibt, und die der beschränkte Verstand aus den äußeren Sinneswahrnehmungen gewahrt, ein äußeres Objektives, ein äußeres Wahres erfaßt, sondern daß der Mensch dann, wenn er höhere Geisteskräfte in Bewegung setzt, welche sich nicht an einzelne Sinnesbeobachtungen wenden, ebenso zu einem Wahren, zu einem Wirklichen gelangt, wie man zu einem Wahren, Wirklichen durch die äußere Sinneswahr­nehmung kommt."
      ],
      [
        "Man darf wohl sagen, daß Schiller, der in jenem Augen­blicke noch nicht einsehen konnte, was dahinter war, und der glaubte, es seien Subjektivitäten, die ihm Goethe vor­gezeichnet hatte, das schönste Dokument geliefert hat dafür, wie sich der Mensch bis zu der Höhe hinaufranken kann, die ihm von Goethe gezeigt wurde.",
        "Von jenem Zeitpunkte an sehen wir Schiller den Goetheschen Ideen immer mehr Verständnis entgegenbringen.",
        "Ein psychologisches Doku­ment allerersten Ranges ist ein Brief Schillers, der da sagt:"
      ],
      [
        "«Lange schon habe ich, obgleich aus ziemlicher Ferne, dem Gang Ihres Geistes zugesehen und den Weg, den Sie sich vorgezeichnet haben, mit immer erneuerter Bewunderung bemerkt.",
        "Sie suchen das Notwendige der Natur, aber Sie suchen es auf dem schweresten Wege, vor welchem jede schwächere Kraft sich wohl hüten wird.",
        "Sie nehmen die ganze Natur zusammen, um über das einzelne Licht zu bekommen; in der Allheit ihrer Erscheinungsarten suchen Sie den Erklärungsgrund für das Individuum auf.",
        "Von der"
      ],
      [
        "einfachen Organisation steigen Sie, Schritt vor Schritt, zu den mehr verwickelten hinauf, um endlich die verwickeltste von allen, den Menschen, genetisch aus den Materialien des ganzen Naturgebäudes zu erbauen.",
        "Dadurch, daß Sie ihn der Natur gleichsam nacherschaffen, suchen Sie in seine verborgene Technik einzudringen.",
        "Eine große und wahr­haft heldenmäßige Idee, die zur Genüge zeigt, wie sehr Ihr Geist das reiche Ganze seiner Vorstellungen in einer schö­nen Einheit zusammenhält!»"
      ],
      [
        "So dürfen wir, als ein Dokument für die Objektivität der Ideenwelt Goethes, das ansehen, was in Goethes Bewußt­sein zu solcher Antwort führte, und was Schiller später durch diesen Brief bestätigte."
      ],
      [
        "Sehr merkwürdig: Ein Psychologe, der in den zwanziger Jahren des neunzehnten Jahrhunderts lebte und heute ver­gessen ist, Heinroth, hat in seiner «Anthropologie», die eigentlich eine Psychologie ist, ein sehr bedeutsames Wort über Goethe gesprochen, ein Wort, das zu jenen gehört, die durch ihre Wendung gerade methodisch bedeutsam sind und tief hineinleuchten in das, was sie beleuchten sollen.",
        "Er gebrauchte für Goethes ganze Anschauungsweise das Wort «Gegenständliches Denken», und er erläuterte dieses Wort, indem er sagte: Goethes Denken ist ein ganz eigenartiges Denken, das sich eigentlich nicht von dem Objektiven der Gegenstände trennt, das ruhig in den Gegenständen lebt, in denen es sich bis zu den Ideen erhebt."
      ],
      [
        "Wer nun tiefer in Goethes ganze Geistesorganisation hineinzublicken vermag, wie wir es heute und übermorgen tun werden, wo wir versuchen wollen, noch tiefer in dieses Thema hineinzudringen, wo wir mehr innerlich betrachten werden, was heute äußerlich vor uns hingestellt werden soll, der wird sehen, daß er in diesem Denken in einer ge­wissen Weise, ohne auf der Oberfläche der Dinge und an"
      ],
      [
        "der Sinneserfahrung haften zu bleiben, doch bei den Tat­sachen bleibt, und innerhalb derselben das Geistige, die Ideenwelt findet.",
        "Wir sehen, daß Goethes Denken gerade in dieser Art für einen großen Teil unserer modernen Menschheitsentwickelung so bedeutsam geworden ist.",
        "Wir dürfen sagen, es ist etwas höchst Eigenartiges mit dieser Wirkung des Goetheschen Geistes auf die verschiedensten Menschen, auf die verschiedensten Anschauungen, ja, auf die verschiedenen aufeinander folgenden Epochen."
      ],
      [
        "Betrachten wir einmal, um was es sich hier eigentlich handelt, und wir werden sehen, wie eigenartig Goethes Geistesart tatsächlich gewirkt hat.",
        "Wenn wir zum Beispiel die drei Philosophen des deutschen Geisteslebens vor unsere Seele treten lassen, die im Grunde genommen, ihrer gan­zen Anschauungsweise nach, sehr verschieden sind: Fichte, Hegel, Schopenhauer, so ergibt sich uns aus der Betrachtung ihres gegenseitigen Verhältnisses, aus der Betrachtung des Zusammenhanges in ihren Verhältnissen zu Goethe etwas ganz Eigenartiges über die welthistorische Wirkung der Goetheschen Geistesart."
      ],
      [
        "Fichte erweist sich als ein in abgezogenen Höhen schwe­bender Denker, und ganz besonders war er in abgezogenen Höhen schwebend, als er im Jahre 1794 seine Grundzüge der Wissenschaftslehre in Jena beendet hatte.",
        "Es ist schwer, sich zum Verständnis der Fichteschen Eigenart zu erheben, es ist schwer, ihn zu durchdringen, obwohl niemand, der in ihn eindringt, sich nicht sagen müßte, daß er ungeheure Früchte für seine Geistesdisziplin aus ihm schöpfte.",
        "Aber es ist nicht jedermanns Sache, in solche Sphären des reinsten Begriffes hinaufzuwandern.",
        "Dieser Fichte, der in solch ab­strakten Höhen wandelte, besonders damals, schickte seine «Wissenschaftslehre» mit folgenden bedeutungsvollen Wor­ten an Goethe: «Ich betrachte Sie, und habe Sie immer betrachtet"
      ],
      [
        "als den Repräsentanten der reinsten Geistigkeit des Gefühls auf der gegenwärtig errungenen Stufe der Hu­manität.",
        "An Sie wendet mit Recht sich die Philosophie.",
        "Ihr Gefühl ist derselben Probierstein.» So Fichte zu Goethe."
      ],
      [
        "Sehen wir jetzt auf einen anderen Philosophen, auf Schopenhauer, und sehen wir zuerst, wie Schopenhauer zu Fichte stand.",
        "Wahrhaft feindliche Brüder waren sie, wenig­stens war Schopenhauer ein recht feindlicher Bruder zu Fichte.",
        "Schopenhauer wird nicht müde, in geradezu Schimpf-worten sich über Fichte zu ergehen.",
        "Ein Windbeutel ist er ihm, der in leeren Begriffen gesonnen und geschrieben hat.",
        "Immer wieder kommt er darauf zurück, die Wesenlosigkeit, Bedeutungslosigkeit und Unrealität der Fichteschen Philo­sophie zu betonen.",
        "Wahrlich, es kann keine größeren Ge­gensätze geben, als Schopenhauer und Fichte.",
        "Und Scho­penhauer ging wahrhaftig zu Goethe in die Lehre.",
        "Eine Zeitlang hindurch hat er zusammen mit Goethe experimen­tiert, um sich die physikalischen Grundbegriffe klarzuma­chen, und manches, was in Schopenhauers erstem Werke und auch in seinem Hauptwerke steht, ist hervorgegangen aus dem Eindrucke, den Goethe auf ihn gemacht hat.",
        "Wer Schopenhauer kennt, weiß aber auch, wie hingebungsvoll er von Goethe sprach.",
        "Schopenhauer und Fichte, zwei große Gegensätze, in Goethe vereinigen sie sich und er erscheint wie die vereinigende Kraft der beiden."
      ],
      [
        "Nehmen wir endlich Hegel und Schopenhauer!",
        "Auch Hegel ist schwierig mit dem Verständnis zu erreichen.",
        "Er, der versucht, sich eine Tatsachenwelt der Begriffe in einer umfassenden, systematischen Organik zu verschaffen, ver­langt, daß der Mensch sich auf eine Stufe erhebt, wo er den Begriff als Tatsache erfaßt, wo er fähig wird, ihn erleben zu können.",
        "Schopenhauer findet auch in dieser Begriffs-technik etwas völlig Wertloses; alles sei ein Spiel mit abstrakten"
      ],
      [
        "Worten.",
        "Und wenn wir uns nun wieder das Ver­hältnis von Hegel zu Goethe vergegenwärtigen wollen, so brauchen wir nur eines zu nennen und wir werden sehen, wie Hegel zu Goethe steht.",
        "Einen schönen Brief gibt es, worin Hegel schreibt: Goethe sucht nach den tatsächlichen, geistigen Phänomenen, die hinter den sinnlichen stehen, die Goethe die Urphänomene nennt, wie er die Urpflanze das Urphänomen der Pflanzenwelt nennt. - Während Hegel als Philosoph aus der Höhe der geistigen Welt spricht und uns zeigt, was wir denken und begreifen können, arbeitet er sich auf der anderen Seite hinauf bis zu dem Punkte, wo er mit den aus dem Geiste geschöpften Begriffen in Berüh­rung kommt.",
        "So vereinigt sich Goethes Urphänomen mit dem, was die reine, denkende Philosophie von oben erfaßt.",
        "Auch hier sehen wir eine Harmonie zwischen Hegel und Goethe wie zwischen Goethe und Schopenhauer.",
        "In Goethe finden sie sich zusammen.",
        "Und wenn wir von diesen älteren Zeiten in unsere Zeiten heraufgehen, was finden wir da?"
      ],
      [
        "In jener Zeit, in der Goethe selber gelebt hat, hat sozusagen das naturwissenschaftliche Forschen noch eine ganz andere Physiognomie gehabt.",
        "Noch mehr, als es zu Goethes Zeiten der Fall war, betrachtet man heute als die einzig richtige Methode der strengen Wissenschaft die Forschung, die sich auf die äußere Sinnesbeobachtung stützt, und das reinliche Herausarbeiten dessen, was der Verstand, der sich auf die Beobachtung beschränkt, aus den so gewonnenen Resultaten machen kann.",
        "Aber auch ein Haed'el will, wie er in jedem Buche wieder betont, auf dem festen Boden gerade Goethe­scher Weltanschauung stehen, und so sehen wir eine mehr materialistisch gefärbte Weltanschauung geradezu Wert darauf legen, an Goethe sich anzulehnen.",
        "Sie können aber auch heute noch Schriften finden, die auf einem Boden ste­hen, für den der Geist eine absolute Realität im eminentesten"
      ],
      [
        "Sinne des Wortes ist, und auch bei ihnen können Sie die Berufung auf Goethe bemerken.",
        "Feindlich können sich spiritualistische und materialistische Forscher gegenüber­stehen, beide glauben sie aber in gleicher Art zu Goethe aufschauen zu können.",
        "So bietet er auch da etwas, was Gegensätze überbrückt."
      ],
      [
        "Diese Tatsachen bezeugen die Kraft der Goetheschen Weltanschauung, die Kraft, die so auf die andern wirkt, daß das, was sich gegenseitig nicht versteht, bei Goethe etwas findet, was es selbst besitzt.",
        "Vielleicht wissen einige von Ihnen, in welchem Gegensatze Virchow und Haeckel sich befanden.",
        "Aber auch Virchow, der in so wenig Dingen mit Haeckel übereinstimmt, hat sich in einem bedeutungs­vollen Vortrag über Goethe ebenfalls an Goethe angelehnt.",
        "Wir haben also in Goethe eine Kraft, die gegenüber den Gegensätzen, dem Kampfe der Weltanschauungen, das in ihnen Gemeinsame bei sich anklingen zu lassen vermag, eine Kraft, die in der Lage ist, zu zeigen, daß es im Grunde genommen bei den Weltanschauungen nicht so ist, wie diese Vertreter der Wissenschaft behaupten und so beharrlich verfechten."
      ],
      [
        "Gerade wenn man das Verhältnis dieser bedeutenden Menschen zu Goethe betrachtet, wird man zu der Erkennt­nis kommen, daß mit dem, was die Menschen Erkenntnis nennen, es sich verhält wie mit den verschiedenen Malern, die um einen Berg herumsitzen, ihn anblicken und von den verschiedensten Standpunkten aus ihn malen.",
        "Die Bilder, die sie da bekommen, müssen natürlich sehr verschieden sein, und doch war es derselbe Berg, den sie malten.",
        "Eine umfassende Vorstellung von dem Berge wird man nur be­kommen können, wenn man die verschiedenen Darstellun­gen miteinander vergleicht und sie zu einem Ganzen zu-sammenfügt.",
        "Wenn man sich so zu den Erkenntnissen stellt,"
      ],
      [
        "dann wird man sehen, daß Goethe sich nicht einen einzel­nen Gesichtspunkt wählt, sondern den Berg hinansteigt und zeigt, daß es eine Möglichkeit gibt, den Standpunkt auf dem Bergesgipfel einzunehmen und dort ein umfassendes Panorama zu finden, wo alle Anschauungen in ihrer tiefe-ren Verträglichkeit sich zeigen."
      ],
      [
        "Das ist es aber auch, was Goethe zu einem so eminent modernen Geiste macht, und wenn wir bei einem rückhalt­losen Eingehen auf Goethe das Gefühl erhalten, daß er uns als ein moderner Geist erscheint, dann wird es von selbst schon eine Rechtfertigung sein, wenn wir in den hier oft angestellten Betrachtungen über die Geisteswissenschaft und eine vom Geistigen ausgehende Weltanschauung das, was er machte und wollte, als eine Art von Anleitung betrach­ten, tiefer in sein Wesen einzudringen.",
        "Wenn er in so vielen Beziehungen ein anregender Geist ist, warum sollte er da nicht auch ein anregender Geist sein für diejenige Geistes­strömung, die als eines ihrer höchsten und schönsten Ziele das tolerante Eindringen in die verschiedenen Standpunkte der Weltanschauungen hat, und die sich zum Prinzip macht, nicht auf einem einmal fixierten Standpunkte stehen zu bleiben, sondern, um Wahrheit zu finden, immer höher und höher zu steigen durch Methoden, die man auf seine innere Entwickelung, auf die Heranbildung innerer Wahrneh­mungsorgane anzuwenden hat, weil man dadurch, daß man sich seine inneren Organe heranzüchtet, erst dazu kommt, die tieferen geistigen Grundlagen zu sehen."
      ],
      [
        "Inwiefern Goethe auf einem eng begrenzten Gebiete die tiefsten Gefühle auch der heutigen Menschheit trifft, wollen wir jetzt noch betrachten.",
        "Beispielsweise sei ein Gefühl ge­wählt, das viele von Ihnen kennen, ein Gefühl, das man mit den Worten charakterisieren könnte, daß es in unserer Zeit Menschen gibt, die danach streben, manche alte Tradition"
      ],
      [
        "über Bord zu werfen und sich Gefühle, Gedanken und Vorstellungen zu schaffen, die in die unmittelbare Ge­genwart hineinführen.",
        "Sie werden sogleich sehen, was ich meine, wenn ich Sie an ein Bild erinnere, das vielen in unserer Zeit wert geworden ist.",
        "Man mag zu dem Bilde stehen, wie man will, aber es ist ein Ausdruck der moder­nen Zeit.",
        "Ich meine das Bild: «Komm, Herr Jesus, sei unser Gast...» Das Bild lebt nicht nur bei dem, der es geschaffen hat, sondern auch in denen, die es genießen wollen; es lebt in ihnen die Sehnsucht, die Gestalt des Jesus in der un­mittelbaren Gegenwart zu sehen, wie sie sich hinstellt an den Tisch.",
        "Man könnte sagen, daß das Bild nicht nur Wert für diese Zeit hat, sondern für alle Zeiten, daß es ein ewiges, unvergängliches Dasein hat, und daß jede Zeit das Recht hat, diese Gestalt in ihre eigene Epoche hinein-zustellen.",
        "Nur mit diesen wenigen Worten sei das Gefühl angedeutet, das viele gegenüber diesem Bilde haben."
      ],
      [
        "Nun könnte man glauben, Goethe gehöre in dieser Be­ziehung noch zu den Alten.",
        "Man leitet das ja her aus seiner Vorliebe zu der alten Kunst, die an den alten, guten, künst­lerischen Traditionen festhalten wollte, aus seiner Vorliebe zu den Griechen.",
        "Man könnte glauben, Goethe hätte viel­leicht kein tieferes Verständnis für eine Empfindung, wie sie in dem Bilde charakterisiert ist: «Komm, Herr Jesus, sei unser Gast.» Um da einmal einen Blick in Goethes Seele zu tun, wollen wir uns an ein Buch anlehnen, an Bossis Buch über Lionardo da Vincis Abendmahl.",
        "Goethe schrieb eine Rezension über dieses Buch.",
        "Darin stehen bedeutungsvolle Worte.",
        "Von diesem Bilde, das sich im Speisesaale des Klo­sters Santa Maria delle Grazie in Mailand befindet, und das trotz der in letzter Zeit vorgenommenen Restauration den Eindruck macht, als wenn es dem Verfall entgegen-ginge, von diesem Bilde erzählt Goethe, wie er selbst einmal"
      ],
      [
        "demselben gegenübergestanden habe zu einer Zeit, als es noch in einer gewissen Frische erhalten war.",
        "Und er schil­dert den Eindruck, den er einst von diesem Bilde in seiner Jugend bekommen habe: «Dem Eingang an der schmalen Seite gegenüber, im Grunde des Saals, stand die Tafel des Priors, zu beiden Seiten die Mönchstische, sämtlich auf einer Stufe vom Boden erhöht; und nun, wenn der Hereintre­tende sich umkehrte, sah er an der vierten Wand über den nicht allzuhohen Türen den vierten Tisch gemalt, an demsel­ben Christus und seine Jünger, eben als wenn sie zur Gesell­schaft gehörten» - Ihn, der von den Dominikanern in ihrem Sinne, ihrer Stellung mit der Empfindung aufgerufen wor­den ist: «Komm, Herr Jesus, sei unser Gast»."
      ],
      [
        "Es schließe sich, sagt Goethe, das Ganze zu einem einheitlichen Bilde zusammen.",
        "Und um gar keinen Zweifel daran zu lassen, was er eigentlich meinte, sagte er noch: «Es muß zur Speise-stunde ein bedeutender Anblick gewesen sein, wenn die Tische des Priors und Christi, als zwei Gegenbilder, auf­einanderblickten und die Mönche an ihren Tafeln sich da­zwischen eingeschlossen fanden."
      ],
      [
        "Und eben deshalb mußte die Weisheit des Malers die vorhandenen Mönchstische zum Vorbilde nehmen.",
        "Auch ist gewiß das Tischtuch mit seinen gequetschten Falten, gemusterten Streifen und aufgeknüpf­ten Zipfeln aus der Waschkammer des Klosters genommen, Schüsseln, Teller, Becher und sonstiges Geräte gleichfalls denjenigen nachgeahmt, der sich die Mönche bedienten."
      ],
      [
        "Hier war also keineswegs die Rede von Annäherung an ein unsicheres, veraltetes Kostüm.",
        "Höchst ungeschickt wäre es gewesen, an diesem Orte die heilige Gesellschaft auf Polster auszustrecken.",
        "Nein, sie sollte der Gegenwart angenähert werden, Christus sollte sein Abendmahl bei den Domini­kanern zu Mailand einnehmen.»"
      ],
      [
        "Und nun fragen wir: Hatte Goethe gerade dieses Verständnis,"
      ],
      [
        "das man ein modernes Verständnis nennen muß?",
        "Er hatte es in jenem umfassenden Stile, der uns wieder ein Beweis dafür sein kann, wie universell seine Kraft ist gegen­über den manchmal einseitigen Kräften, die sich gegenseitig ausschließen und bekämpfen.",
        "So müssen wir uns hinein­versetzen in Goethes Seele und wir werden dann begreifen, warum Goethe uns ein so Nahstehender sein kann, und warum wir zu ihm hinaufschauen dürfen, wenn es sich um die vorläufige Orientierung über tiefere Geistesfragen han­delt.",
        "Das war Goethes tiefes Bewußtsein, daß es möglich ist für den Menschen, in sich geistige Organe zu erwecken, um hinaufzusteigen zu höheren Anschauungen und dadurch etwas zu gewinnen, was nicht bloß im Geiste des Menschen lebt, sondern was zu gleicher Zeit tiefer liegt."
      ],
      [
        "Wenn hier die Möglichkeit wäre, auf Goethes natur­wissenschaftliche Studien einzugehen, wie Sie dieselben in meinem Buche «Goethes Weltanschauung» ausführlich be­sprochen finden, so könnten wir zeigen, wie diese ganze Goethesche Methode wirkt.",
        "Aber wir wollen uns heute Goethe von einer anderen Richtung her nähern.",
        "Goethe hatte mancherlei zum Ausdrucke gebracht, was uns auf die tiefe Grundlage seiner Weltanschauung hinweisen kann.",
        "Wir werden darüber in den zwei Vorträgen dieses Winter­zyklus über Goethes «Faust» zu sprechen haben.",
        "Über ihn sagte er einmal zu Eckermann, daß er ihn so gestaltet habe, daß der Leser, wenn er sich nur an äußere Belehrungen hal­ten will, schon in den bunten Bildern etwas hat; daß er aber auch hinter den Worten die Geheimnisse finden kann, die sich darin befinden.",
        "Da weist Goethe in dem zweiten Teil darauf hin, daß zu unterscheiden ist das, was das Außere, und das, was das Innere, das Wesen ist, das, was er hinein­geheimnißt hat.",
        "Nach alter Weise bezeichnet man das Äußere als das Exoterische, das Innere als das Esoterische."
      ],
      [
        "Nun wollen wir uns Goethe dadurch nähern, daß wir das Werk, in dem er sein ganzes methodisches Denken und Wollen zum Ausdruck gebracht hat, heute in einer äußer­lichen, exoterischen Weise, und übermorgen dann in einer innerlichen, esoterischen Weise betrachten.",
        "Ein verhältnis­mäßig unbekanntes Werkchen von Goethe ist es, an das man sich halten muß, wenn man Goethes tiefste Erkennt­nisgeheimnisse - so darf das, um was es sich hier handelt, wohl genannt werden - durchschauen will.",
        "Es ist das Werk­chen, das am Ende der «Unterhaltungen deutscher Aus­gewanderter» unter der Überschrift: «Märchen» steht, und bei dessen Lektüre der, welcher danach strebt, in Goethes Weltanschauung tiefer einzudringen, von Anfang an die Empfindung haben wird, daß Goethe damit mehr sagen will, als was die Bilder zunächst darbieten.",
        "Rätsel über Rätsel wird dem sinnenden Betrachter dieses «Märchen» von der grünen Schlange und der schönen Lilie vorlegen."
      ],
      [
        "Und nun gestatten Sie mir, daß ich die hauptsächlichsten Züge dieses Märchens zunächst hier auseinandersetze, denn es ist nicht möglich, über das Märchen zu sprechen, ohne daß wir uns wenigstens diejenigen Züge vor die Seele führen, welche von Wichtigkeit sind, wenn wir einen tie­feren Blick in Goethes Weltanschauung werfen wollen.",
        "Es wird also notwendig sein, daß wir einige Zeit dem Inhalte dieses Werkchens widmen; aber dafür werden wir uns auch dann in bezug auf das, was wir zu sagen haben, um so besser verstehen.",
        "Es ist mir immer wieder passiert, wenn ich einen Vortrag über dieses Märchen gehalten habe, daß man mir sagte: «Ich weiß nichts davon, daß in Goethes Werken ein Märchen steht.» Ich wiederhole deshalb: es ist in jeder Goetheausgabe enthalten und bildet den Schluß der «Unterhaltungen deutscher Ausgewanderter»."
      ],
      [
        "Nun zu den Bildern!",
        "An einem Flusse wohnt ein Fähr­mann.",
        "Zu diesem Fährmann kommen merkwürdige Ge­stalten: Irrlichter.",
        "Sie wollen von dem Fährmann in dem Kahne an das andere Ufer des Flusses hinübergesetzt wer­den.",
        "Der Fährmann geht darauf ein und setzt sie über den Fluß hinüber.",
        "Sie betragen sich dabei sonderbar, sind un­ruhig und zappelig, so daß er Angst bekommt, sie könnten ihm den Kahn umwerfen.",
        "Er führt sie aber glücklich hin­über, und als sie angelangt sind, wollen sie ihn in eigen­artiger Art bezahlen.",
        "Sie schütteln sich und es fallen Gold-stücke von ihnen ab; das soll der Lohn sein für die Mühe des Übersetzens.",
        "Der Fährmann ist wenig erbaut von den Goldstücken und sagt: Es ist gut, daß nichts in den Fluß gefallen ist, denn er würde wild aufwallen.",
        "Ich kann diese Bezahlung aber nicht annehmen, ich kann nur mit Früchten der Natur bezahlt werden. - Und er verlangt drei Zwie­beln, drei Artischocken, drei Kohlköpfe.",
        "Mit Früchten soll­ten sie also bezahlen.",
        "Wir werden gleich sehen, welche tiefe Bedeutung jeder Zug und jede einzelne Tatsache hat."
      ],
      [
        "Nun sagt der Fährmann weiter: So macht ihr mir noch die Mühe, daß ich das, was ihr als Goldstücke herumgewor­fen habt, den Fluß hinunterführen und begraben muß. -Darauf führt er die Goldstücke tatsächlich ein Stück den Fluß hinunter und vergräbt sie in den Klüften der Erde.",
        "Als sie da hinein vergraben worden sind, kommt ein merk­würdiges anderes Wesen an diese Goldstücke heran: die grüne Schlange, die in und auf der Erde herum und durch die Klüfte der Erde hindurchkriecht.",
        "Plötzlich sieht sie durch die Spalten der Erde die Goldstücke hereinfallen.",
        "Zunächst glaubt sie, daß sie vom Himmel hereinfallen.",
        "Sie verzehrt sie aber dann und wird durch die Aufnahme dieser Goldstücke in den eigenen Leib immer leuchtender.",
        "Als sie aber an die Oberfläche geht, merkt sie, daß sie in wunderbarer"
      ],
      [
        "Weise ein eigenartiges Licht ausstrahlt, leuchtend wie Smaragd und Edelstein."
      ],
      [
        "Nun treffen die Schlange und die Irrlichter zusammen, die Irrlichter immer noch sich schüttelnd und wegwerfend, was sie in sich haben.",
        "Die Schlange, die jetzt Geschmack an dem Golde bekommen hat, nimmt in ihren eigenen Leib auf und verarbeitet, was die Irrlichter um sich werfen.",
        "Be­deutsames sagen sich die Schlange und die Irrlichter über ihr gegenseitiges Verhältnis.",
        "Die Schlange nennt sich Ver­wandte der Irrlichter von der horizontalen Linie und die Irrlichter sich Verwandte der Schlange von der vertikalen Linie.",
        "Die Irrlichter fragen noch die Schlange, ob diese nicht Auskunft geben könne, wie sie zur schönen Lilie kommen könnten.",
        "Da sagt die Schlange: Die schöne Lilie ist jenseits des Flusses. - Nun, dann haben wir uns etwas Schönes ein­gebrockt! antworten die Irrlichter.",
        "Wir haben uns herüber-fahren lassen, weil wir zur schönen Lilie kommen wollten.",
        "Könnten wir nur einen Fährmann erreichen, der uns wieder zurückführt!",
        "Und nun kommen bedeutungsvolle Worte:"
      ],
      [
        "Ihr werdet den Fährmann nicht wiederfinden, und wenn ihr ihn fändet, seid euch klar darüber, daß er euch wohl herüber, aber nicht mehr zurückführen darf.",
        "Wenn ihr wie­der auf die andere Seite des Flusses zurück wollt, so könnt ihr es nur auf zweierlei Weise.",
        "Entweder ihr versucht am Mittag, wo die Sonne am höchsten steht, eine Brücke zu finden über meinen eigenen Leib, um hinüber zu kommen. -Die Irrlichter sagen: Die Mittagsstunde ist eine Zeit, in der wir nicht gerne reisen. - Oder ihr benützt den zweiten Weg.",
        "Es giht nämlich noch eine andere Möglichkeit.",
        "In der Dämmerstunde findet ihr an einer bestimmten Stelle den großen Riesen.",
        "Er hat gar keine Kraft in sich, aber wenn er seine Hand ausstreckt und der Schatten dieser Hand über den Fluß hinüberfällt, so kann man über den Schatten hinweg"
      ],
      [
        "den Fluß überschreiten.",
        "Der Schatten hat die Trag­kraft, daß man hinübergehen kann.",
        "Wenn ihr also nicht über mich selber gehen wollt zur Mittagsstunde, so suchet den Riesen auf. - Die Irrlichter lassen sich das gesagt sein.",
        "Die Schlange aber ist wieder in die Klüfte der Erde zurück­gegangen und freut sich des innerlichen Leuchtend -Werdens durch Aufnahme des Goldes."
      ],
      [
        "Nun bemerkt die Schlange etwas höchst Merkwürdiges.",
        "Als sie die Klüfte wieder absucht, bemerkt sie, daß sie da, wo sie früher unregelmäßige Naturprodukte gefunden hatte, jetzt an einer Stelle merkwürdige Gebilde sieht.",
        "Frü­her hat sie sie nur durch den Tastsinn wahrgenommen, jetzt, wo sie leuchtend ist, merkt sie, daß sie die Dinge auch sehen kann.",
        "Sie konnte Säulen und auch menschenähnliche Gebilde abtasten, aber es war ihr bis dahin nie klargewor­den, was da in den unterirdischen Klüften eigentlich ist.",
        "Jetzt bewegt sie sich wieder hinein und das von ihr aus­strahlende Licht dient ihr zur Beleuchtung der Dinge."
      ],
      [
        "Als sie hineindringt in diese große Höhle unter der Erde, kann sie sogleich wahrnehmen, wie in den vier Ecken vier königliche Gestalten stehen: ein goldener König, ein silber­ner König, ein eherner König und in der vierten Ecke ein gemischter König, eine Gestalt, welche aus den anderen Metallen in der buntesten Weise zusammengefügt ist, so daß in ihm alle möglichen Metalle chaotisch ineinander-gefügt sind."
      ],
      [
        "In dem Augenblicke, wo die Schlange in die Höhle hineinkommt und ihr die Beleuchtung der Gestalten ge­lingt, stellt der goldene König die sehr bedeutungsvolle"
      ],
      [
        "«Wo kommst du her?»"
      ],
      [
        "«Aus den Klüften», versetzte die Schlange, «in denen das Gold wohnt.»"
      ],
      [
        "«Was ist herrlicher als Gold?» fragte der König."
      ],
      [
        "Die Schlange antwortet: «Das Licht!»"
      ],
      [
        "Und der König fragt weiter: «Was ist erquicklicher als Licht?»"
      ],
      [
        "«Das Gespräch.»"
      ],
      [
        "Niemand wird bezweifeln, daß in diesen Worten nicht bloß Bilder gegeben werden sollen, sondern daß sie auch einen bedeutungsvollen Inhalt haben."
      ],
      [
        "Als die Schlange hineinkommt in die Höhle, öffnet sich ein Spalt an dem Tempel, in dem die vier Könige wohnen.",
        "Es kommt der Alte mit der Lampe in den Raum, und er wird gefragt, warum er gerade jetzt komme?",
        "Da sagt er das merkwürdige Wort: Wißt Ihr nicht, daß mein Licht nur er­leuchten darf, was schon erleuchtet ist? daß ich das Dunkle nicht erleuchten darf? - Nachdem die Schlange die Dinge im Raume erleuchtet hat, darf nun auch er mit seiner wun­derwirkenden Lampe kommen."
      ],
      [
        "Jetzt entspinnt sich aufs neue ein Gespräch zwischen den Königen und dem Alten mit der Lampe.",
        "Der Alte wird gefragt:"
      ],
      [
        "«Wie viele Geheimnisse weißt Du?»"
      ],
      [
        "«Drei», antwortet er."
      ],
      [
        "«Welches ist das wichtigste?» fragt der silberne König."
      ],
      [
        "«Das offenbare», versetzt der Alte."
      ],
      [
        "«Willst du es auch uns eröffnen?» fragt der eherne König."
      ],
      [
        "«Sobald ich das vierte weiß.»"
      ],
      [
        "Und nun kommen die allerbedeutsamsten Worte des Märchens: «Ich weiß das vierte», sagt die Schlange und zischelt ihm etwas in das Ohr, worauf der Alte mit gewal­tiger Stimme ruft: «Es ist an der Zeit!»"
      ],
      [
        "Es gibt eine große Anzahl von Versuchen, die Rätsel dieses Märchens zu lösen.",
        "Viele haben auch versucht, das, was man schon zu Schillers und Goethes Zeiten als Rätsel"
      ],
      [
        "empfand, so oder so zu deuten.",
        "Es ist eigenartig, daß Goethe und Schiller sich darüber einig waren und es aus­drücklich mit den Worten aussprachen: Es liegt das Wort der Lösung für das Märchen im Märchen selber.",
        "Also darf man nach des Märchens Lösung nur im Märchen selber suchen, und es wird sich im weiteren Verlauf des Vortrages auch finden, daß das Wort des Rätsels, wenn auch in eigen­artiger Weise, in dem Märchen drinnen ist.",
        "Die Schlange zischelt dem Alten etwas ins Ohr, und das, was sie ihm ins Ohr zischelt, was aber nicht gesagt wird, das ist die Lösung des Rätsels.",
        "Dann sagt der Alte: «Es ist an der Zeit!» Was also ergründet werden muß, das ist, was die Schlange im unterirdischen Tempel dem Alten ins Ohr geraunt hat."
      ],
      [
        "Der Alte geht nun mit seiner Lampe dahin, wo seine Gattin wohnt.",
        "Durch die Kraft des Lichtes der Lampe wer­den die verschiedensten Materien verwandelt: Steine in Gold, Holz in Silber, tote Tiere in Edelsteine, Metalle aber werden vernichtet.",
        "Er trifft seine Gattin in geradezu fassungslosem Zustande.",
        "Als er fragt, was passiert sei, sagt sie: Es waren ganz merkwürdige Persönlichkeiten da.",
        "Man hätte sie für.",
        "Irrlichter halten können.",
        "Die sind sehr wenig in den Grenzen des Anstandes geblieben. - Nun, meint der Alte, bei deinem Alter wird es wohl bei der allgemeinen Höflichkeit geblieben sein. - Und nun erzählt sie, wie die Irrlichter sich an das Gold herangemacht und es abgeleckt haben, damit sie es wieder abschütteln könnten.",
        "Wenn es nur noch das wäre, aber sieh dir mal den Mops an.",
        "Der hat von den Goldstücken gefressen, wurde in Edelstein ver­wandelt und starb.",
        "Jetzt ist er tot. - Und die Alte sagt weiter: Wenn ich das vorher gewußt hätte, so würde ich ihnen nicht versprochen haben, daß ich ihre Schuld bei dem Fährmann abzahlen werde.",
        "Das sind: drei Kohlhäupter, drei Zwiebeln und drei Artischocken."
      ],
      [
        "Nun, sagte der Alte, nimm doch den Mops mit, trage ihn zur schönen Lilie hin, die hat die Eigenschaft, daß sie alles, was Edelstein ist, durch ihre Berührung in Lebendiges ver­wandeln kann. - Sie nimmt also die drei mal drei Früchte, um die übernommene Schuld bei dem Fährmann abzutra­gen, und legt den Mops dazu."
      ],
      [
        "Nun kommt ein sehr bedeutungsvoller Zug des Mär­chens: Als sie den Korb trägt, erscheint er ihr außerordent­lich schwer, obgleich das Tote für sie gar kein Gewicht hat, der Korb mit dem toten Mops allein würde so leicht sein, als wenn er leer wäre; nur durch das Lebendige, durch die Kohlköpfe, Zwiebeln und Artischocken wird der Korb schwer.",
        "Auf dem Wege zu dem Fährmann passiert ihr aber noch etwas Eigentümliches.",
        "Der Riese legt seinen Arm ge­rade so, daß der Schatten über den Fluß hinüberfällt, greift ihr ein Kohlhaupt, eine Artischocke und eine Zwiebel aus dem Korbe heraus und verzehrt sie, so daß sie jetzt nur noch zwei von jeder Gattung hat.",
        "Sie will daher dem Fähr­mann nur einen Teil der Schuld abtragen.",
        "Er aber sagt, daß es unbedingt notwendig sei, das Ganze gleich mitzubringen."
      ],
      [
        "Nach vielem Hin- und Herreden sagte der Fährmann: es gäbe noch einen Ausweg, der wäre, wenn sie Bürgschaft für die Beibringung der drei fehlenden Früchte leiste.",
        "Sie muß daher die Hand in den Fluß stecken, als Sicherheit dafür, daß sie ihr Versprechen halten werde.",
        "Das tut sie, bemerkt aber dann, daß, soweit die Hand in den Fluß hineingesteckt war, sie schwarz und kleiner geworden ist.",
        "«Jetzt scheint es nur so», sagte der Alte.",
        "«Wenn ihr aber nicht Wort haltet, kann es wahr werden.",
        "Die Hand wird nach und nach schwinden und endlich ganz verschwinden, ohne daß ihr den Gebrauch derselben entbehrt.",
        "Ihr werdet alles damit verrichten können, nur daß sie niemand sehen wird.» Sie will aber lieber, daß man sie sehe, auch wenn sie nichts mit"
      ],
      [
        "der Hand tun könne.",
        "Wenn sie zu entsprechender Zeit den Tribut bringt, sagt der Fälirmann, wird alles wieder gut werden."
      ],
      [
        "Auf dem Wege zur schönen Lilie trifft sie nun einen herr­lich-schönen Jüngling, dem aber, wie er sagt, alle seine einstige Kraft und Stärke geschwunden ist; und aus dem Gespräche, das sie miteinander führen, erfahren wir, wie das gekommen ist.",
        "Der Jüngling hatte die lebhafte Begierde gefaßt, zur schönen Lilie zu gelangen.",
        "Sie war sein Ideal geworden.",
        "Aber ihre schönen Augen wirkten so unselig, daß sie ihm alle seine Kraft genommen hatten und dennoch zieht es ihn immer wieder zu ihr hin."
      ],
      [
        "Endlich kommen die beiden zur schönen Lilie hin.",
        "Es ist nun zwar alles, was die schöne Lilie umgibt, im höchsten Grade bezeichnend; aber wir können hier nur einzelne Züge herausnehmen.",
        "Die schöne Lilie ist das Bild vollkom­menster Schönheit; aber sie hat die Eigenschaft, daß sie alles Lebendige durch ihre Berührung zunächst tötet, und alles, was durch das Leben hindurchgegangen und dem Tode ver­fallen ist, wieder lebendig macht."
      ],
      [
        "Die Alte bringt nun ihr Anliegen vor.",
        "Der Jüngling ist gekommen, seine Sehnsucht nach der schönen Lilie zu be­friedigen; wir sehen aber auch, daß die schöne Lilie eben­falls Sehnsucht fühlt.",
        "Sie fühlt sich fern von allem fruchtbar Lebendigen; in ihrem Garten gedeihen Pflanzen, aber nur bis zur Blüte, nicht bis zur Frucht; schön ist sie, aber fern von allem Lebendigen.",
        "Die Alte sagt dann ein bedeutungs­volles Wort.",
        "Sie wiederholt, was der Mann im unterirdi­schen Tempel gesagt hat, und das gibt der Lilie neue Hoff­nung.",
        "Das war aber auch der letzte Augenblick, in dem sie Hoffnung fassen konnte; denn das letzte Lebendige, das eine Art Verbindungsband zwischen ihr und dem Leben­digen gebildet hatte, war ihr auch noch verlorengegangen."
      ],
      [
        "Sie hatte einen Kanarienvogel in ihrer Umgebung, und hatte sich sehr gehütet, ihn zu berühren, weil ihn das ge­tötet haben würde.",
        "Nun aber war ein Habicht in die Nähe gekommen, der Kanarienvogel floh vor ihm, flog auf die Lilie zu und wurde getötet.",
        "Und damit war die schöne Lilie nun in völliger geistiger Einsamkeit und Abgesondertheit von dem, was die Menschen haben."
      ],
      [
        "Nun gibt die Alte der Lilie den Mops.",
        "Die Lilie berührt ihn und macht ihn dadurch wieder lebendig.",
        "Der Jüngling sucht seine Sehnsucht dadurch zu stillen, daß er die Lilie umfaßt.",
        "Dadurch wird er vollends getötet.",
        "Das Leben in ihm wird ganz vernichtet."
      ],
      [
        "Die Schlange bildet nun einen magischen Kreis.",
        "In diesen Kreis werden der Jüngling und der Kanarienvogel hinein­gelegt.",
        "Dadurch soll sich - und die Schlange deutet bedeu­tungsvoll darauf hin - das, was trostlos ist, in allernächster Zeit ändern.",
        "Und es ändert sich in der Tat.",
        "Wir erfahren, daß nun auch der Alte mit seiner Lampe herankommt, und daß durch ihn tatsächlich eine Lösung der ganzen Situation in Angriff genommen werden kann.",
        "Denn es ist gerade Zeit, als der Alte herankommt: die Körper von dem Kana­rienvogel und dem Jüngling sind noch nicht in Verwesung übergegangen."
      ],
      [
        "Der Alte führt sie nach dem unterirdischen Tempel hin, den die Schlange ja schon ausgekundschaftet hatte.",
        "Er sagt zu den Irrlichtern: Ihr seid auch dazu geeignet, uns zu die­nen.",
        "Wenn wir an die Pforte des Tempels gelangen, werdet Ihr es sein müssen, die uns die Pforte aufschließen. - Nun bildet die Schlange eine Brücke über den Fluß.",
        "Der ganze Zug geht über die Schlangenbrücke.",
        "Da sehen wir, als sie drüben angekommen sind, daß durch die Berührung mit der Schlange, die jetzt sich zu opfern beschließt, der Jüng­ling zwar noch nicht durchgeistigt, aber doch lebendig wird."
      ],
      [
        "Er geht dadurch, daß die Schlange bereit ist, sich hinzu-opfern, in einen merkwürdigen Zustand über.",
        "Er kann wohl sehen, aber das Gesehene noch nicht fassen."
      ],
      [
        "Die Schlange teilt sich in lauter wunderbare Edelsteine, die der Alte in den Fluß senkt und wodurch eine Brücke über den Fluß entsteht.",
        "Der Zug bewegt sich unter der An­führung des Alten in den unterirdischen Tempel.",
        "Als sie da hineinkommen, sehen wir, daß zwischen den Ankömmlin­gen und den Königen bedeutungsvolle Fragen gestellt wer­den, die darauf hindeuten, daß da ein großes Rätsel ver­borgen ist.",
        "Zum Beispiel: «Woher kommt ihr?» «Aus der Welt.» «Wohin geht ihr?» «In die Welt.» «Was wollt ihr bei uns?» «Euch begleiten!», nämlich die Könige."
      ],
      [
        "Nun bewegt sich die Gruppe mit dem Tempel.",
        "Sie gehen unter den Fluß und erheben sich dann wieder mit dem gan­zen Tempel.",
        "Als sie sich über den Fluß erhoben haben, fällt von oben etwas wie Bretterwerk in den Tempel hinein: es ist die Hütte des Fährmanns.",
        "Sie verwandelt sich und wird ein kleines Tempelchen im großen Tempel.",
        "Und jetzt spielt sich eine Szene ab, die von Wichtigkeit ist für den Jüngling, der ja bis jetzt belebt, aber noch nicht durchgeistigt war."
      ],
      [
        "Wir haben gesehen: der erste, der goldene König, stellt die Weisheit dar; der zweite, der silberne, den Schein oder die Schönheit; der dritte, der eherne, die Stärke oder den Willen.",
        "Wir sehen nun einen symbolischen Akt sich voll­ziehen.",
        "Der Jüngling wird durch die drei Könige mit drei verschiedenen Gaben begabt.",
        "Durch den ehernen König mit dem Schwert, und indem ihm das Schwert überreicht wird, werden die bedeutungsvollenWorte gesprochen: «Das Schwert an der Linken, die Rechte frei.» - Kraft des Wil­lens. - Durch den silbernen König bekommt er das Zepter mit den Worten: «Weide die Schafe.» Wir werden sehen, daß der Jüngling durch die Gefühlskraft der Seele erfüllt"
      ],
      [
        "wird, die sich in der Schönheit ausdrückt.",
        "Der goldene König setzt ihm die Krone auf das Haupt, mit den Worten: «Er­kenne das Höchste.» Und die Kraft der Vorstellung erfaßt den Jüngling.",
        "In diesem Moment ist er durchgeistigt und darf sich mit der schönen Lilie vereinigen.",
        "Wir werden so­dann noch darauf aufmerksam gemacht, daß sich alles ver­jüngt."
      ],
      [
        "Besonders bedeutsam ist noch die eigentümliche Rolle, die der Riese spielt, der keine Kraft in sich selber, wohl aber in seinem Schatten hat.",
        "Er stolpert höchst ungeschickt über die Brücke, und der König ist ungehalten darüber.",
        "Es stellt sich aber heraus, daß das Kommen des Riesen seinen guten Sinn hat.",
        "Wie der Uhrzeiger einer großen Sonnenuhr da-steht, so wird er in der Mitte des Tempelhofes festgehalten.",
        "Wir sehen, welche Kraft wir in der Sonnenuhr, in dem die Zeit anzeigenden und harmonisierenden Riesen finden, und wir sehen, wie aus dem Leib der Schlange die Brücke, welche über den Fluß zu dem Tempel hinüberführt, gebildet wird.",
        "Wir sehen dann, daß nicht mehr bloß Fußgänger, sondern jetzt Wagen, Reiter, Herden hinüber- und herübergehen können.",
        "Es wird uns dargestellt, wie in der Vereinigung mit der schönen Lilie der Jüngling die frühere Kraft, die er durch die Berührung mit ihr verloren, wiedergewinnt, wie er sich jetzt der Lilie nähern, sie umfassen darf, und wie sie beglückt und beseligt beide sind."
      ],
      [
        "Wer möchte nicht, wenn er die Bilder des Märchens auf sich wirken läßt, sagen: Rätsel sind es!",
        "Zunächst können wir nur wenig spüren von dem, was in diesem Märchen lebt.",
        "Wenn wir aber historisch vorgehen, wenn wir betrach­ten, wie es in der Mitte des Jahres 1795 entsteht, im Beginn der Freundschaft mit Schiller, aus dem, was sich zwischen Goethe und Schiller zugetragen hat, dann werden wir be­greifen, was Goethe sich in dem Märchen für eine Aufgabe"
      ],
      [
        "gestellt hat.",
        "In diese Zeit fällt die Abfassung eines Werkes, eine Frucht des Studiums Goethescher Weltanschauung, das tief bedeutsam wurde für die Erziehung und Kultivierung des deutschen Geisteslebens: die Briefe Schillers über die ästhetische Erziehung des Menschen.",
        "Nur skizzenhaft kön­nen wir darauf hinweisen, was Schiller mit diesen Briefen wollte."
      ],
      [
        "Er fragt sich, wie gelangt der Mensch dahin, seine Kräfte immer höher und höher zu entwickeln, damit er in einer freien und vollkommenen menschlichen Art in die Geheim­nisse der Welt eindringen kann.",
        "Dieses Werk ist in Brief-form an den Herzog von Augustenburg geschrieben, und Schiller schrieb darin den bedeutungsvollen Satz: «Jeder individuelle Mensch, kann man sagen, trägt, der Anlage und Bestimmung nach, einen reinen idealischen Menschen in sich, mit dessen unveränderlicher Einheit in allen seinen Abwechselungen übereinzustimmen die große Aufgabe sei­nes Daseins ist.» Und nun sucht Schiller auseinanderzuset­zen, wie sich der Mensch zu den höheren Stufen des Men­schendaseins hinaufzuentwickeln hat."
      ],
      [
        "Zweierlei ist es, was den Menschen unfrei macht, ihm keinen freien Blick in die Geheimnisse des Daseins gibt.",
        "Auf der einen Seite ist es das Beherrschtsein von der Sinnlich­keit, auf der anderen Seite die ungenügende Entwickelung der Vernunft.",
        "Und nun setzt Schiller diese Dinge so ausein­ander: Nehmen wir einen Menschen, der in sich nicht das Zwingende, Logische der Begriffe, auch nicht den Pflicht­begriff verspürt, sondern seinen Neigungen und Instinkten folgt - er kann die Kräfte seiner Natur nicht frei entwickeln, er steckt in der Sklaverei der Triebe, Begierden und In­stinkte, er ist unfrei.",
        "Aber auch derjenige ist nicht frei, der seine Begierden, Triebe und Instinkte zunächst bekämpft und einzig nur einer rein begrifflichen und logischen Vernunftnotwendigkeit"
      ],
      [
        "folgt.",
        "Ein solcher Mensch wird ent­weder ein Sklave der Naturnotwendigkeit oder ein Sklave der Vernunftnotwendigkeit."
      ],
      [
        "Wodurch kann der Mensch seine inneren Kräfte ent­wickeln?",
        "Schiller antwortet: Er muß seine inneren göttlichen Zustände entwickeln, sich bemühen, daß sie gereinigt und geläutert werden und zusammentreffen mit dem, was wir Logik nennen.",
        "Wenn seine Triebe und Instinkte dann ge­läutert sind, so daß er gern tut, was er als Pflicht empfindet, wenn die Vernunftnotwendigkeit nicht als zwingend emp­funden wird, dann wird der Mensch gern tun schon aus dem gewöhnlichen Trieb heraus, was vernünftig ist, dann hat Vernunft den Menschen hinunter zur Sinnlichkeit ge­führt, und Sinnlichkeit führt ihn wieder hinauf zur Ver­nunft."
      ],
      [
        "Sehen wir einen Menschen an, der einem Kunstwerke gegenübersteht.",
        "Er sieht sich etwas Sinnliches an.",
        "Aber durch jedes Glied des Sinnlichen offenbart sich ihm etwas Geisti­ges, denn in dem Sinnlichen kommt dasjenige zum Aus­druck, was der Künstler als Geistiges in das Kunstwerk hineingelegt hat.",
        "Geist und Sinnlichkeit in der Anschauung der Schönheit, das wird zum Mittlerzustand.",
        "So wird die Kunst, das Leben in Schönheit, für Schiller ein großes Er­ziehungsmittel, ein Mittel zur ästhetischen Erziehung, eine Befreiung der Natur, so daß sie ihre eigenen Kräfte ent­falten kann.",
        "Wie entwickelt sich also der Mensch im Sinne Schillers.",
        "Er muß seine Natur hinunterführen, daß sie sich bewährt in sinnlicher Natur, und die Sinne hinaufentwik­keln, daß sie sich bewähren in der vernünftigen Natur."
      ],
      [
        "Ein wunderbar schönes Wort spricht Goethe über diese Briefe aus: Sie wirken auf mich so, daß sie mir darstellen, was ich lebte oder zu leben wünschte immerdar. - Man kann nachweisen, daß Goethe angeregt worden ist, sein"
      ],
      [
        "Märchen zu schreiben, durch das, was Schiller ausgesprochen hat in seinen Briefen über die ästhetische Erziehung des Menschen.",
        "Goethe spricht darin dasselbe in seiner Art aus.",
        "Goethe wollte nicht in abstrakten Begriffen die Rätsel der Seele aussprechen.",
        "Für Goethe waren die einzelnen Seelen-rätsel zu reich und zu gewaltig, als daß er sie in Natur-notwendigkeit und Logik hätte fassen können.",
        "So bildete sich in Goethe das Bedürfnis, des Menschen einzelne Seelen-kräfte in den Gestalten seines Märchens zu personifizieren.",
        "Goethe antwortete auf die Schillersche Frage in seinem Mär­chen, und wir werden sehen, wie die Goethesche Psychologie in wunderbarerWeise in dem Märchen charakterisiert wird.",
        "Wir sehen, wie die Seele immer aufnimmt und von sich gibt in der Darstellung der Irrlichter, wie gewisse Kräfte per­sonifiziert sind in der Schlange, die nur auf derErde arbeitet gleich der menschlichen Forschung, dem menschlichen Ver­stand, der Erfahrung, die in der horizontalen Linie bleiben, während der Idealist in die Höhe steigt.",
        "Die Kraft des reli­giösen Gemütes ist charakterisiert in dem Alten mit der Lampe, und wir sehen endlich, wie durch die Vorgänge, die uns erzählt werden, Goethe darstellt, in welcher Weise eine jede Seelenkraft wirken muß."
      ],
      [
        "Wir werden übermorgen sehen, wie Goethe in der Dar­stellung zeigt, wie jede Seelenkraft maßvoll wirken muß zusammen mit den anderen Seelenkräften, um die Seele zu einem Gesamtbilde zu gestalten, auf daß sie sich ,,in­aufentwickeln könne zu menschlicher Vollkommenheit, zu einem Umfassen der Dinge.",
        "Wenn der Mensch unreif die Erkenntnisse erfassen will, so wird er getötet, wie der Jüng­ling.",
        "Es gibt ein Heranreifen der Erkenntnis.",
        "In dem Mär­chen stellt uns Goethe die Evolution der Seele in richtiger und bildhafter Weise dar, indem er darin das Parallelwerk zu Schillers «Briefen über die ästhetische Erziehung» schuf."
      ],
      [
        "Goethe wußte, daß es ein Ziel der menschlichen Seelen­entwickelung gibt, das man in alten Zeiten die Einweihung in höhere Geheimnisse genannt hat.",
        "Er wußte, daß es eine solche Möglichkeit gibt, und er wußte auch, daß es Gesell­schaften gibt, die an verborgenen Orten, in den Tempeln der Einweihung, die Kräfte der Seele entwickeln.",
        "Er zeigt auch, wie die neuere Zeit immer mehr dahin kommen muß, daß es der Menschheit möglich wird, im größeren Um­fange diese Einweihung zu erlangen, die Seele zu ent­wickeln.",
        "Er zeigt in den Vorgängen, die sich zwischen den einzelnen Menschen abspielen, den Vorgang der Einweihung bis zu den höchsten Stufen, bis dahin, wo die Seele fähig wird, die höchsten Geheimnisse zu erfassen.",
        "Das ist exo­terisch, rein historisch angesehen."
      ],
      [
        "Durch das Zusammenleben Goethes mit Schiller erlebte Schiller dasjenige, was Goethe erlebt hat, in einer der wich­tigsten Perioden seines Lebens.",
        "Und wenn es Schiller auch schwer wurde, Goethe zu verstehen, so müssen wir doch sagen: Das, was Schiller in abstrakter Weise in den ästheti­schen Briefen sagt, und was Goethe in viel umfassenderer Weise zu sagen hatte, in einer Weise, die nur erreicht wird, wenn man sich ausdrückt in Bildern und Persönlichkeiten, das ist ein und dasselbe.",
        "Das Märchen ist Goethe-Psychologie im tiefsten Sinne.",
        "Wir sehen, daß Goethe durch die Art sei­nes Strebens so fruchtbar geworden ist, daß wir uns heute noch gern bei ihm orientieren.",
        "Goethe erscheint uns noch heute als ein Gegenwärtiger.",
        "Wir lesen ihn wie einen Schrift­steller unserer Zeit.",
        "Er ist so fruchtbar, weil er so viel von Ewigkeitsgehalt in seinem Schaffen und seiner ganzen Art und Weise hat.",
        "So wirkt er im Sinne jener Wahrheit, die er selbst als die richtige angesehen hat, und ein bedeutungs­volles Wort hat er einst gesprochen: «Was fruchtbar ist, allein ist wahr. »"
      ],
      [
        "Das heißt, daß der Mensch sich in den Besitz von Wahr­heiten setzen muß, die so wirken, daß, wenn er ins Leben hineintritt, sie ihre Bestätigung finden dadurch, daß sie sich fruchtbar erweisen.",
        "Das war für ihn das Kriterium der Wahrheit: Was fruchtbar ist, allein ist wahr!"
      ],
      [
        "Gerade diese Vorträge, die Ihnen Goethe veranschau­lichen wollen, sollen uns zeigen, daß Goethe diesen Aus­spruch selber. erprobt hat.",
        "Das werden alle diejenigen füh­len, die sich tiefer in ihn hineinleben.",
        "Sie werden fühlen, daß in Goethe etwas von echter Wahrheit lebt, denn Goethe ist fruchtbar, und was fruchtbar ist, ist wahr."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "GOETHES GEHEIME OFFENBARUNG ESOTERISCH Berlin, 24. Oktober 1908",
    "paragraphs": [
      "GOETHES GEHEIME OFFENBARUNG",
      "Berlin, 24. Oktober 1908",
      "Einem Vortrage wie dem heutigen kann leicht der Vorwurf gemacht werden, daß in erzwungener Weise symbolische und allegorische Ausdeutungen gegeben werden von etwas, was ein Dichter im freien Spiel der Einbildungskraft ge-schaffen hat. Wir haben uns ja vorgestern die Aufgabe vorgezeichnet, das Goethesche «Märchen» von der grünen Schlange und der schönen Lilie, wie es uns da vor Augen getreten ist, in seinem tieferen Sinn zu erforschen. Immer wieder wird es geschehen, daß eine solche, wenn man so sagen will, Auslegung, Erklärung eines Phantasiewerks mit den Worten abgetan wird: Ach, da werden allerlei tiefsin­nig sein sollende Symbole und Bedeutungen in den Gestal­ten des Werkes gesucht. - Deshalb möchte ich von vorn­herein bemerken, daß das, was heute von mir gesagt werden soll, nichts zu tun hat mit dem, was allerdings gerade von theosophischer Seite aus oft in bezug auf symbolische oder allegorische Ausdeutungen von Märchen oder dichterischen Werken gemacht worden ist. Und weil ich weiß, daß ähn­lichen Auseinandersetzungen, die ich gegeben habe, immer wieder entgegengehalten wurde, auf solche symbolische Deutungen dichterischer Figuren lasse man sich nicht ein, sö kann ich nicht scharf genug betonen, daß das, was hier zu sagen ist, einzig und allein in folgendem Sinne aufgefaßt werden muß.",
      "Uns liegt heute ein dichterisches Werk vor, das Werk",
      "einer umfassenden und in die Tiefe der Dinge dringenden Einbildungskraft oder Phantasie: Das «Märchen» von der grünen Schlange und der schönen Lilie. Die Frage darf wohl aufgeworfen werden: Dürfen wir von irgendeinem Ge­sichtspunkte an das Werk herangehen und versuchen, den ideellen, den wirklichen Inhalt eines solchen dichterischen Produktes zu ergründen?",
      "Wir sehen die Pflanze vor uns. Der Mensch tritt an die Pflanze heran; er untersucht die Gesetze, die innere Regel­mäßigkeit, nach der die Pflanze wächst und gedeiht, nach der sie Stück für Stück ihres Wesens entwickelt.",
      "Hat der Botaniker oder hat jemand, der kein Botaniker ist, sich aber das Werden der Pflanze ideell zurechtlegt, das Recht dazu? Kann man ihm entgegenhalten: Von dem, was du da findest an Gesetzen, weiß die Pflanze nichts, sie kennt nicht die Gesetze ihres Wachstums und ihrer Entwickelung! - Ge­nau den gleichen Wert, den dieser Einwand hätte, wenn man ihn gegen den Botaniker erheben würde oder gegen den Lyriker, der das, was er bei der Pflanze empfindet, in seinen lyrischen Leistungen zum Ausdruck bringt, genau denselben Sinn und Wert hätte der Einwand, den man gegen eine solche Erklärung des Goetheschen Märchens vorbringen könnte.",
      "Nicht möchte ich die Dinge so aufgefaßt wissen, als ob ich sagen würde: Da haben wir eine Schlange, die bedeu­tet dies oder jenes, da haben wir einen goldenen, einen silber­nen, einen ehernen König, sie bedeuten dies oder jenes. Nicht in diesem symbolisch-allegorischen Sinne möchte ich das Märchen deuten, sondern mehr so, daß in gleicherWeise, wie die Pflanze nach Gesetzen wächst, von denen sie in ihrer Unbewußtheit nichts wissen kann, und wie der Botaniker das Recht hat, diese Gesetze des Pflanzenwachstums zu fin­den, man sich auch sagen muß: Das, was hier auseinander­gesetzt wird, braucht der Dichter Goethe niemals so auseinandergesetzt,",
      "niemals so vor sein äußeres Tagesbewußt­sein gebracht zu haben. Dennoch aber ist es ebenso wahr, daß die Gesetzmäßigkeit, der wirkliche, der ideelle Inhalt des Märchens im gleichen Sinne zu betrachten ist wie das, was wir als die Gesetze des Pflanzenwachstums finden, daß es dieselbe Gesetzmäßigkeit ist, nach der die Pflanze wächst, nach der sie entstanden ist, deren sie sich aber in ihrer Un­bewußtheit nicht bewußt ist.",
      "Daher bitte ich, das, was ich zu sagen mir erlauben werde, so aufzufassen, als ob es den Sinn und den Geist der Goetheschen Denkweise und Vorstellungsart darstellte, und als ob derjenige, welcher sich sozusagen berufen fühlt, die ideale Goethesche Weltanschauung vor Sie hinzustellen, eine Berechtigung hätte - damit Sie den Weg finden können zu einem Verständnis der Goetheschen Weltanschauung -, auseinanderzulegen das Erzeugnis Goethescher Phantasie, herauszuheben die Gestalten, und die Wechselbeziehungen zu zeigen, in welchen er sie verwendet hat, genau ebenso, wie der Botaniker zeigt, daß die Pflanze nach den Gesetzen wächst, die er gefunden hat.",
      "Goethes Psychologie oder Seelenlehre, das heißt, was er für das Wesen der Seele maßgebend hält, das ist uns in seinem schönen Märchen von der grünen Schlange und der schönen Lilie veranschaulicht. Und wenn wir uns verständi­gen wollen über das, was darüber gesagt werden muß, so wird es gut sein, wenn wir in einer Vorbetrachtung den Geist seiner Seelenwelt anschaulich zur Sprache bringen. Schon in dem vorgestrigen Vortrage wurde darauf hinge­wiesen, daß die hier vertretene Weltanschauung davon aus­geht, daß die menschliche Erkenntnis nicht als etwas ein für allemal Feststehendes zu betrachten ist. Vielfach herrscht ja die Ansicht: So, wie der Mensch heute ist, so ist er eben, und so wie er ist, kann er über alle Dinge unbedingt entscheiden;",
      "er beobachtet mit seinen Sinnesorganen die Welt, er­faßt sie in ihren Erscheinungen, kombiniert diese mit seinem an die Sinne gefesselten Verstande, und was er da heraus-bringt mit dieser an die Beobachtung sich haltenden Ver­standestätigkeit, das ist eine absolute Welterkenntnis, die für jeden gelten muß. - Im Gegensatze dazu, aber nur im Gegensatze in einer bestimmten Art, steht die geisteswissen­schaftliche Weltanschauung, die hier vertreten wird. Sie geht davon aus, daß das, was unsere Erkenntnis wird, jederzeit abhängig ist von unseren Organen, von unseren Erkenntnisfähigkeiten, und daß wir selbst als Menschen entwicklungsfähig sind, daß wir an uns arbeiten können, daß wir diejenigen Erkenntnisfähigkeiten, die wir auf einer bestimmten Stufe unseres Daseins haben, höher em­porheben können. Sie geht davon aus, daß wir sie ausbilden können, daß wir in ähnlicher Weise, wie sich der Mensch aus unvollkommenem Zustande hinaufentwickelt hat zu seinem gegenwärtigen Standpunkt, sie noch weiter entwickeln können, und daß wir durch die Erhebung zu höheren Gesichtspunkten auch zu tieferem Eindringen in die Dinge, zu einer richtigeren Anschauung der Welt kommen müssen.",
      "Soll ich mich noch deutlicher, wenn auch etwas trivial ausdrücken, so möchte ich sagen: Wenn wir ganz absehen von einer Entwickelung der Menschheit und nur Rücksicht nehmen darauf, wie die Menschen sind, die so um uns herum leben, und dann auf jene Menschen blicken, die man in der Kulturgeschichte zu den primitiven Völkerstämmen rechnet, und wenn wir uns fragen, was sie iinstande sind, von den Gesetzen der Welt um uns herum zu erkennen und zu wissen, und es vergleichen mit dem, was ein Durch-schnitts-Europäer mit einigen wissenschaftlichen Begriffen von der Welt wissen kann, dann werden wir sehen, daß der Angehörige jenes primitiven Volksstammes sich von",
      "dem Durchschnitts-Europäer ganz wesentlich unterscheidet. Nehmen wir zum Beispiel das Weltbild eines Austral­Negers und das eines, sagen wir, europäischen Monisten, welch letzteres dadurch Realität hat, daß man eine Summe wissenschaftlicher Begriffe der gegenwärtigen Zeit auf­genommen hat. Es unterscheiden sich diese zwei Weltbilder durchaus.",
      "Aber andererseits ist die Geisteswissenschaft weit ent­fernt, das Weltbild des auf rein materiellem Standpunkte stehenden Menschen zu perhorreszieren oder es als ungültig zu erklären. Vielmehr werden diese Dinge so angesehen, daß in jedem Falle das Weltbild eines Menschen einer menschlichen Entwickelungsstufe entspricht, und daß der Mensch in der Lage ist, die in ihm enthaltenen Fähigkeiten zu steigern und durch die Steigerung der Fähigkeiten an­deres, Neues zu erfahren.",
      "Es liegt also in der Perspektive der Geisteswissenschaft, daß der Mensch zu immer höherer Erkenntnis dadurch kommt, daß er sich selber weiterentwickelt, und indem er sich weiterentwickelt, ist das, was er in sich erlebt, objek­tiver Welteninhak, den er früher nur nicht gesehen hatte, als er eben noch nicht die Fähigkeit besaß, ihn zu sehen. Die Geisteswissenschaft unterscheidet sich daher wesentlich von anderen, einseitigen Weltanschauungen, seien sie spiri­tualistisch, seien sie materialistisch, weil sie im Grunde ge­nommen eine ein für allemal abgeschlossene unfehlbare Wahrheit nicht kennt, sondern immer nur die Weisheit und Wahrheit einer bestimmten Entwickelungsstufe, und sich so an das Goethesche Wort hält: Der Mensch hat eigentlich immer nur seine eigene Wahrheit, und sie ist doch immer dieselbe. - Sie ist immer dieselbe, weil das, was wir durch unsere Erkenntniskraft in uns aufnehmen, das Objektive, dasselbe ist.",
      "Wodurch nun gelangt der Mensch dazu, die in ihm liegenden Fähigkeiten und Kräfte zu entwickeln? Die Gei­steswissenschaft ist sozusagen so alt wie die denkende Menschheit. Die Geisteswissenschaft stand immer auf dem Standpunkt, daß der Mensch das Ideal einer gewissen Er-kenntnis-Vollkommenheit vor sich hat, der er zustrebt. Man nannte das Prinzip, das darin liegt, immer das Prinzip der Einweihung oder Initiation. Einweihung oder Initia­tion heißt also nichts anderes, als die Fähigkeiten des Men­schen zu immer höheren Stufen der Erkenntnis zu steigern und dadurch zu tieferen Einsichten in das Wesen der Welt um uns herum zu gelangen. Goethe stand gariz und gar, man darf wohl sagen sein ganzes Leben hindurch, auf diesem Standpunkt der in der Entwickelung begriffenen Erkenntnis, auf dem Standpunkte der Einweihung, der Initiation. Gerade das zeigt uns im eminentesten Sinne sein Märchen.",
      "Wir werden uns am leichtesten verstehen, wenn wir von der Anschauung ausgehen, die heute am meisten und im weitesten Umkreise vertreten ist und die in einem gewissen Gegensatz zu dem Einweihungs- oder Initiations-Prinzip steht.",
      "Heute kann man im weitesten Umkreise diejenigen Men­schen, die über solche Sachen nachdenken oder glauben, über solche Dinge ein Urteil zu haben, mehr oder weniger bewußt den Standpunkt vertreten hören, daß über die Wahrheit, über die objektive Wirklichkeit eigentlich nur Sinnesbeobachtung oder Gegenstände der Sinnesbeobach­tung in der Vorstellung entscheiden können. Sie werden es immer wieder hören können: Wissenschaft kann nur sein, was auf der objektiven Grundlage der Beobachtung be­ruht. - Und man versteht so häufig darunter lediglich die Sinnesbeobachtung und die Anwendung des menschlichen",
      "Verstandes und Vorstellungsvermögens auf diese Sinnes­beobachtung. Ein jeder von Ihnen weiß, daß die Fähigkeit, sich Vorstellungen, Begriffe zu bilden, ein menschliches Seelenvermögen ist unter anderen Seelenvermögen, und ebenso weiß ein jeder von Ihnen, daß diese anderen Seelen-vermögen unser Fühlen und unser Wollen sind.",
      "So kann man schon bei einer verhältnismäßig oberflächlichen Be­trachtung sagen: Der Mensch ist nicht bloß ein vorstellen-des, sondern auch ein fühlendes und wollendes Wesen. -Nun werden diejenigen, die da glauben, den reinen Stand­punkt der Wissenschaft vertreten zu müssen, immer wieder sagen: In das, was Wissenschaft ist, darf nur das Vor­stellungsvermögen hineinreden, niemals das menschliche Gefühl, niemals das, was wir als Willensimpulse kennen, denn dadurch würde das, was objektiv ist, nur verunreinigt, dadurch würde das, was in unpersönlicher Art das Vor­stellungsvermögen gewinnen könnte, nur beeinträchtigt. -Es ist richtig, daß, wenn der Mensch in das, was Gegenstand der Wissenschaft sein soll, sein Gefühl, seine Sympathie oder Antipathie hineinbringt, er die Dinge abstoßend oder ansprechend, sympathisch oder antipathisch findet. Und wohin kämen wir, wenn der Mensch sein Begehrungsver-mögen als ein Erkenntnisvermögen betrachten würde, so daß er zu den Dingen sagen könnte: Ich will es, oder: ich will es nicht. - Ob es dir mißfällt oder gefällt, ob du es be­gehrst, das ist dem Ding höchst gleichgültig.",
      "So wahr es ist, daß derjenige, der glaubt, auf dem festen Boden der Wissen­schaft stehen zu müssen, sich nur an die äußeren Dinge hal­ten kann, so wahr ist es, daß das Ding selber es ist, das dir abnötigt zu sagen, es sei rot, daß das, was du als eine Vor­stellung des Wesens des Steines gewinnst, richtig ist. Aber nicht liegt es im Wesen des Dinges, daß es dir häßlich oder schön erscheint, daß du es begehrst oder nicht begehrst.",
      "es dir rot erscheint, hat einen objektiven Grund, daß du es nicht willst, das hat keinen objektiven Grund.",
      "In einer gewissen Beziehung ist nun die heutige Psycho­logie eigentlich über den eben charakterisierten Standpunkt hinausgegangen. Es ist hier nicht meine Aufgabe, für oder gegen diejenige Richtung der heutigen Seelenwissenschaft oder Psychologie zu reden, die da sagt: Wenn wir die Seelenerscheinungen, das Seelenleben betrachten, dürfen wir uns nicht bloß auf den Intellektualismus beschränken, dürfen wir den Menschen nicht bloß in bezug auf die Vor­stellungsfähigkeit betrachten, sondern müssen auch die Ein­flüsse der Gefühls- und Willenswelt berücksichtigen. - Viel­leicht wissen einige von Ihnen, daß dies zum System der Wundtschen Philosophie gehört, welche den Willen als Ursprüngliches der Seelentätigkeit auffaßt. In einer in ge­wisser Beziehung grundlegenden Art, gleichgültig, ob man damit einverstanden ist oder nicht, hat der russische Psy­chologe Losskij in seinem Buche, das sich «Die Grundlegung des Intuitivismus» betitelt, auf die Willensrichtung des menschlichen Seelenlebens hingewiesen. Ich könnte Ihnen noch vieles sagen, wenn ich zeigen wollte, wie die Seelen-lehre bestrebt ist, den einseitigen Intellektualismus zu über­winden, und wenn ich Ihnen ferner zeigen wollte, daß in das, was als menschliche Seelenkraft vorhanden ist, auch die andern Kräfte hineinspielen.",
      "Wer weiter zu denken vermag, wird sich sagen: Daraus sehen wir, wie undurchführbar die Forderung ist, daß nur die auf die Beobachtung beschränkte Vorstellungsfähigkeit zu objektiven Resultaten der Wissenschaft führen dürfe. Wenn die Wissenschaft selbst zeigt, daß dies nicht möglich ist, daß überall Wille mitspielt, woraus wollt ihr dann fest­stellen, daß etwas rein objektive Beobachtung sei? Weil ihr dadurch, daß euer Wille euch den obenerwähnten Streich",
      "spielt und ihr wegen eurer Denkgewohnheiten eine Vorliebe dafür habt, nur dasjenige, was materiell ist, als objektiv anzusehen, und weil ihr nicht die Denkgewohnheit und Gefühlsgewohnheit habt, auch das Geistige in den Dingen anzuerkennen, deshalb laßt ihr das Letztere in euren Theo­rien weg. Es kommt nicht darauf an, wenn wir die Welt begreifen wollen, was wir an abstrakten Idealen uns vor­setzen, sondern was wir in unserer Seele zuwege bringen, was wir können.",
      "Goethe gehört zu denjenigen Menschen, die am schärfsten den Grundsatz ablehnen, daß die Erkenntnis nur durch das einseitige Vorstellungsvermögen, nur durch das Denkver­mögen vermittelt werde. Das ist der hervorstechende, be­deutungsvolle Grundzug in Goethes Wesen, daß er, mehr oder weniger deutlich ausgesprochen, immer der Ansicht ist, daß die ganze menschliche Seele in allen ihren Kräften wirken müsse, wenn der Mensch die Weltenrätsel enträtseln will.",
      "Nun dürfen wir aber auch nicht einseitig und nicht un­gerecht sein. Es ist durchaus richtig, wenn in bezug auf die Erkenntnis eingewendet wird, daß Gefühl und Wille der Persönlichkeit den persönlichen Eigenschaften des Menschen unterworfene Fähigkeiten sind, und wenn gesagt wird:",
      "Wohin würden wir kommen, wenn man nicht bloß das, was die Augen sehen, was das Mikroskop zeigt, sondern was das Gefühl, der Wille dem Menschen sagt, als zu den Dingen gehörig betrachten wollte!",
      "Das ist es aber gerade, was wir uns sagen müssen, um jemanden zu begreifen, der wie Goethe auf dem Prinzip der Einweihung und Entwickelung steht: daß so, wie durch­schnittlich Gefühl und Wille heute im Menschen sind, sie in der Tat nicht zur Erkenntnis verwendet werden können, daß sie die Menschen nur zu einer absoluten Uneinigkeit in",
      "ihrer Erkenntnis führen würden. Der eine will das, der an­dere das, je nach den subjektiven Bedürfnissen des Gefühls und Willens. Der aber, welcher auf dem Boden der Initia­tion steht, ist sich auch darüber klar, daß von den mensch­lichen Seelenkräften - Denken, Vorstellen, Fühlen und Wol­len - in der Entwickelung des gegenwärtigen Durchschnitts­menschen das Vermögen der Vorstellung, das Vermögen des Denkens eben am weitesten vorgeschritten ist, und am ehe­sten geneigt und geeignet ist, das Persönliche auszuschließen und zur Objektivität zu kommen. Denn dasjenige Seelen-vermögen, das sich im Intellektualismus auslebt, ist heute schon so weit, daß die Menschen, wenn sie sich auf dieses Seelenvermögen verlassen, am wenigsten streiten, am mei­sten einig werden über das, was sie sagen. Das ist deshalb so, weil heute die Menschen in bezug auf das Vorstellungs-und Denkvermögen weit entwickelt sind, während Gefühl und Wille noch nicht zu solcher Objektivität entwickelt werden konnten.",
      "Wir könnten auch, wenn wir auf dem Gebiete des Vor­stellungslebens Umschau halten, mit Recht Unterschiede finden. Es gibt weite Gebiete des Vorstellungslebens, die uns vollständig objektive Wahrheiten liefern, Wahrheiten, die die Menschen als solche erkannt haben, ganz unabhängig von der äußeren Erfahrung, wobei es ganz gleich ist, ob eine Million Menschen anders darüber urteilt. Wer die Gründe dafür in sich erlebt hat, der vermag die Wahrheit zu behaupten, auch wenn eine Million Menschen anderes meint. Jeder kann zum Beispiel bei solchen Wahrheiten, die sich auf Zahl- und Raumgrößen beziehen, das Gesagte be­stätigt finden. Daß 3 mal 3 = 9 sind, kann jeder begreifen und erleben, und es ist richtig, selbst wenn eine Million Menschen dem widersprächen. Warum ist das so der Fall? Weil in bezug auf solche Wahrheiten, wie die mathematischen",
      "es sind, die meisten Menschen es dazu gebracht haben, ihre Vorliebe und Abneigung, ihre Sympathie und Anti­pathie, kurz, das Persönliche auszuschalten und nur die Sache für sich sprechen zu lassen. Man hat die Ausschaltung von allem Persönlichen in bezug auf das Denken und auf das Vorstellungsvermögen immer die Läuterung der mensch­lichen Seele genannt, und man betrachtete diese Läuterung als die erste Stufe auf dem Wege der Einweihung oder Ini­tiation, oder, wie man auch sagen könnte, auf dem Wege zur höheren Erkenntnis.",
      "Der Mensch, der in diesen Dingen bewandert ist, sagt sich: Nicht nur in bezug auf das Gefühl und auf den Willen sind die Menschen noch nicht so weit, daß da kein Persön­liches mehr hineinspielt, daß sie Objektivität bewahren können, sondern auch in bezug auf das Denken sind die meisten noch nicht so weit, daß sie sich an das rein hingeben könnten, was ihnen die Dinge, die Ideen der Dinge selbst sagen, so wie es alle Menschen bei den mathematischen Dingen können. Aber es gibt Methoden, das Denken so weit zu läutern, daß wir nicht mehr persönlich denken, son­dern die Gedanken in uns denken lassen, so wie wir die mathematischen Gedanken in uns denken lassen. Wenn wir also die Gedanken gereinigt haben von den Einflüssen der Persönlichkeit, dann sprechen wir von der Läuterung oder Katharsis, wie dies in den alten Eleusinischen Mysterien genannt wurde. Es muß also der Mensch dahin kommen, das Denken zu läutern, das ihm dann die Möglichkeit gibt, die Dinge gedanklich objektiv zu erfassen.",
      "So, wie das möglich ist, ist es nun auch möglich, aus dem Gefühl alles Persönliche auszuschalten, so daß dann auch dasjenige, was von den Dingen das Gefühl anregt, nicht mehr zur Persönlichkeit spricht, nichts mehr zu tun hat mit Person, Sympathie und Antipathie, sondern einzig und",
      "allein das Wesen des Dinges aufruft, insofern es nicht zum bloßen Vorstellungsvermögen sprechen kann. Erlebnisse in unserer Seele, die in unserem Gefühlsleben wurzeln oder urständen, und die dadurch zu innerer Erkenntnis führen, daß sie tiefer in das Wesen eines Dinges hineinführen, die aber auch noch zu anderen Seiten der Seele als zum bloßen Intellektualismus sprechen, können ebenso vom Persönlichen gereinigt werden wie das Denken, so daß das Gefühl dann eben solche Objektivität vermittelt, wie sie das Denken oder das Vorstellungsvermögen vermitteln kann. Diese Reinigung oder Entwickelung des Gefühls nennt man in aller esoterischen Erkenntnislehre die Erleuchtung.",
      "Jeder Mensch, der entwickelungsfähig ist und nicht in beliebiger Weise, wie es in den Intentionen der Persönlich­keit liegt, seine Entwickelung anstrebt, muß sich dahin be­mühen, daß er sich nur durch das, was im Wesen des Dinges liegt, anregen läßt. Wenn er dahin gekommen ist, daß das Ding in ihm persönlich keine Sympathie oder Antipathie erweckt, daß er lediglich das Wesen der Dinge sprechen läßt, so daß er sagt: Was ich auch für Sympathien oder Anti­pathien habe, ist gleichgültig und darf nicht in Betracht kommen -, dann liegt es im Wesen des Dinges, daß das Denken und Handeln des Menschen diese oder jene Rich­tung annimmt, dann ist das eine Aussage des innersten Wesens des Dinges. In der esoterischen Erkenntnislehre hat man diese Entwickelung des Willens die Vollendung ge­nannt.",
      "Wenn der Mensch auf dem Boden der Geisteswissenschaft steht, so sagt er sich also: Wenn ich ein Ding vor mir habe, so lebt in diesem Ding ein Geistiges, und ich kann mein Vorstellungsvermögen so anregen, daß das Wesen der Dinge durch meine Begriffe und Vorstellungen objektiv repräsen­tiert wird. So ist gleichsam, was draußen arbeitet, in mir",
      "gegenwärtig geworden, und ich habe das Wesen des Dinges durch das Vorstellungsvermögen erkannt. Aber das, was ich erkannt habe, ist nur ein Teil des Wesens. Es gibt in den Dingen etwas, das überhaupt nicht zur Vorstellung, son­dern nur zum Gefühl, und zwar zum geläuterten oder ob­jektiv gewordenen Gefühl sprechen kann. - Der, welcher nicht schon in einer solchen Kultur des Gefühls einen der­artigen Teil des Wesens in sich entwickelt hat, der kann das Wesen in dieser Richtung nicht erkennen. Für einen aber, der sich sagt, das Gefühl kann ebenso die Grundlage für die Erkenntnis geben wie das Vorstellungsvermögen",
      "- das Gefühl, nicht wie es ist, sondern wie es durch wohl-begründete Methoden der Erkenntnislehre werden kann -für einen solchen wird es nach und nach klar, daß es Dinge gibt, die tiefer sind als das Vorstellungsvermögen, Dinge, die zu der seelischen Natur und zu dem Gefühl sprechen. Ebenso gibt es Dinge, die sogar bis zum Willen hinab-reichen.",
      "Nun war sich Goethe ganz besonders darüber klar, daß dies sich wirklich so verhält, daß der Mensch diese Ent­wickelungsmöglichkeiten hat. Er stand ganz auf dem Boden des Initiationsprinzips, und er hat uns die Einweihung des Menschen, die ihm durch die Entwickelung seiner Seele, durch die Entwickelung der drei Grundkräfte: Wille, Ge­fühl und Vorstellungsvermögen, werden kann, dadurch dargestellt, daß er in seinem Märchen die Repräsentanten dieser drei Einweihungen des Menschen auftreten läßt.",
      "Der goldene König ist Repräsentant der Einweihung für das Vorstellungsvermögen, der silberne König ist der Re­präsentant für die Einweihung mit dem Erkenntnisver­mögen des objektiven Gefühls, der eherne König ist der Repräsentant der Einweihung für das Erkenntnisvermögen des Willens. Goethe hat uns zu gleicher Zeit nachdrücklich",
      "darauf aufmerksam gemacht, daß der Mensch erst gewisse Dinge überwinden muß, wenn er dazu kommen will, mit diesen drei Gaben begabt zu werden. Der Jüngling, den wir in der Erzählung des Märchens kennengelernt haben, ist nichts anderes als der Repräsentant des nach dem Höch­sten strebenden Menschen. So wie Schiller des Menschen Streben nach vollkommener Menschlichkeit in seinen Ästhe-tischen Briefen hinstellt, stellt uns Goethe in dem Jüngling den nach dem Höchsten strebenden Menschen dar, der zu­nächst die schöne Lilie erreichen will, der aber dann die innere menschliche Vollkommenheit dadurch erlangt, daß ihn die drei Könige, der goldene, der silberne und der erzene König, damit begaben.",
      "Wie das geschieht, wird in dem Gange des Märchens an­gedeutet. Erinnern Sie sich, daß in dem unterirdischen Tem­pel, in den die Schlange durch die Kristallisierungskraft der Erde blickt, in jeder der vier Ecken einer der Könige war. In der ersten war der goldene, in der zweiten der silberne, in der dritten der erzene König. In der vierten Ecke war ein König, der aus den drei Metallen gemischt war, in dem also diese drei Bestandteile so zusammengefügt sind, daß man sie nicht voneinander unterscheiden kann. In diesem vierten Könige stellt uns Goethe den Repräsentanten für diejenige menschliche Entwickelungsstufe hin, in welcher Wille, Vorstellungsvermögen und Empfindungsvermögen gemischt sind. Er ist mit andern Worten derjenige Reprä­sentant der menschlichen Seele, der von Wille, Vorstellung und Gefühl beherrscht wird, weil er selbst nicht Herr über diese drei Vermögen ist. Dagegen ist in dem Jüngling, nachdem er die Begabung von jedem der Könige im be­sonderen erlangt hat - die Begabung des Vorstellungsver­mögens, die Begabung der Gefühlserkenntnis und die Be­gabung der Willenserkenntnis, so daß sie nicht mehr chao­tisch",
      "gemischt sind -, diejenige Erkenntnisstufe dargestellt, die sich nicht mehr von Vorstellung, Gefühl und Wille be­herrschen läßt, sondern über sie herrscht. Beherrscht wird der Mensch von ihnen so lange, wie sie in ihm chaotisch durcheinanderströmen, so lange sie sich in seiner Seele nicht rein, jede für sich selbst wirkend, finden.",
      "Solange derMensch nicht zu dieser Sonderung gekommen ist, ist er auch nicht in der Lage, durch seine drei Erkenntnisvermögen zu wirken. Ist er aber dazu gelangt, beherrscht ihn nicht mehr das Chaotische, sondern beherrscht er umgekehrt selber sein Vorstellungsvermögen, ist es so rein wie der goldene König, so daß ihm nichts anderes beigemischt ist; ist sein Gefühls­vermögen so, daß ihm nichts anderes beigemischt ist, daß es rein und lauter dasteht wie der silberne König, und ist ebenso der Wille so rein wie das Erz des erzenen Königs, so daß ihn Vorstellungen und Gefühle nicht beherrschen und er sich frei in seiner Natur darstellen kann - mit an­dern Worten, ist er fähig, wenn es sich darum handelt, durch die Vorstellung zu erfassen, oder durch das Gefühl zu er­fassen, oder durch den Willen zu erfassen, von Wille, Ge­fühl und Vorstellung einzeln Gebrauch zu machen, dann ist er so weit über sich hinausgeschritten, daß das gesamte reine Erkenntnisvermögen, das uns im Vorstellen, Fühlen und Wollen entgegentritt, ihn zu einer tieferen Einsicht führt, daß er wirklich untertaucht in den Strom des Ge­schehens, untertaucht in das, was die Dinge innerlich sind.",
      "Daß man so untertauchen kann, vermag natürlich nur die Erfahrung zu lehren.",
      "Es wird nun nicht mehr schwer sein, nachdem dieses vor­ausgeschickt worden ist, zuzugeben, daß, wenn Goethe den strebenden Menschen durch den Jüngling repräsentiert sein läßt, wir in der schönen Lilie eine andere Seelenverfassung zu sehen haben, diejenige Seelenverfassung des Menschen,",
      "zu der er gelangt, wenn ihm die in den Dingen liegenden Wesenheiten in der Seele aufgehen und er sein Menschen­dasein dadurch erhöht, daß er die Dinge in sich verschmelzt mit dem Wesen der Dinge in der Außenwelt. Was da der Mensch in seiner Seele erlebt dadurch, daß er über sich hin­auswächst, daß er Herr wird über die Seelenkräfte, Sieger ist über das Chaotische in seiner Seele, das, was der Mensch da erlebt, diese innere Seligkeit, dieses Verbundensein mit den Dingen, dieses Aufgegangensein in den Dingen, wird uns von Goethe repräsentativ dargestellt in der Vereinigung mit der schönen Lilie. Schönheit ist hier nicht bloß Kunst-schönheit, sondern Eigenschaft des bis zu einem gewissen Grade vollendeten Menschen überhaupt. So daß wir jetzt auch begreiflich finden werden, warum uns Goethe darstellt, wie der Jüngling fortzieht, zur schönen Lilie hinstrebt, so daß alle Kräfte zunächst aus ihm verschwinden. Warum ist das so?",
      "Wir verstehen Goethe in der Darstellung eines solchen Bildes, wenn wir an einen Gedanken, den er einst ausge­sprochen hat, anknüpfen: «Alles, was unsern Geist befreit, ohne uns die Herrschaft über uns selbst zu geben, ist ver­derblich.» Erst muß der Mensch frei werden, dahin kom­men, Herr über seine inneren Seelenkräfte zu sein, dann kann er mit wirklicher Erkenntnis zur Vereinigung mit dem höchsten Seelenzustande, mit der schönen Lilie gelangen. Wenn er es aber unvorbereitet, mit noch nicht reifen Kräf­ten erlangen will, dann nimmt ihm das seine Kräfte und wirkt ausdorrend auf seine Seele. Daher wird von Goethe darauf aufmerksam gemacht, daß der Jüngling jene Be­freiung sucht, die ihn zum Herrn über seine Seelenkräfte macht. In dem Augenblick, wo seine Seelenkräfte nicht mehr chaotisch in ihm wirken, sondern geläutert und gereinigt nebeneinanderstehen, in dem Augenblick ist er reif, jenen",
      "Seelenzustand zu erreichen, der durch die Verbindung mit der schönen Lilie charakterisiert oder repräsentiert ist.",
      "So sehen wir, daß Goethe diese verschiedenen Gestalten in freischaffender Phantasie ausbildet, sehen, wenn wir sie als dargestellte Seelenkräfte betrachten, daß sie in seiner ganzen Seele walten und wirken. Wenn wir sie so betrach­ten, wenn wir so fühlen und empfinden, wie in gewisser Weise bezüglich dieser Gestalten Goethe gefühlt und emp­funden hat, der sich nicht damit begnügt, wie ein schlechter didaktischer Dichter zu sagen, was diese oder jene Seelen­kraft bedeutet, sondern der damit ausdrückt, was er selber empfand, dann werden wir erkennen, was sich ihm in sol­chen Dichtergestalten ausdrückt. Daher stehen die verschie­denen Gestalten in einem so persönlichen Verhältnis zuein­ander, wie die Seelenkräfte des Menschen zueinanderstehen.",
      "Es kann nicht scharf genug betont werden, daß es sich nicht so verhält, daß die Gestalten dies oder jenes bedeuten. Das ist durchaus nicht der Fall. Es ist vielmehr so, daß Goethe bei dieser oder jener Seelenkraft dies oder jenes fühlt, und daß sich sein Fühlen dann zu dieser oder jener Gestalt wandelt.Damit schuf er den Vorgang des Märchens, der noch wichtiger ist als die Figuren selbst. So sehen wir die Irrlichter und die grüne Schlange. Wir sehen, daß die Irrlichter vom jenseitigen Ufer des Flusses herüberkommen und ganz merkwürdige Eigenschaften zeigen. Sie nehmen das Gold begierig in sich auf, lecken es sogar von den Wän­den der Stube des Alten und werfen damit in verschwende­rischer Weise um sich. Dasselbe Gold, das also in den Irr-lichtern unter dem Zeichen einer Wertlosigkeit steht, die uns auch dadurch angedeutet wird, daß der Fährmann das Gold zurückweisen muß, weil der Fluß sich aufbäumen würde und nur Früchte in Zahlung nehmen darf, dieses Gold, was bewirkt es im Körper der grünen Schlange? Die",
      "Schlange wird, nachdem sie es aufnahm, innerlich leuchtend! Und das, was an Pflanzen und anderen Dingen um sie her­um ist, wird auch dadurch erleuchtet, daß sie das, was bei den Irrlichtern im Zeichen der Wertlosigkeit steht, in sich aufnimmt. Aber auch den Irrlichtern wird eine gewisse Wichtigkeit zugeschrieben. Sie wissen, daß der Alte in ent­scheidender Stunde gerade die Irrlichter auffordert, die Pforte des Tempels zu öffnen, so daß der ganze Zug sich nun in den Tempel hineinbegeben kann.",
      "Genau dasselbe Ereignis, das sich hier mit der grünen Schlange vollzieht, findet sich als Erlebnis in der mensch­lichen Seele, ein Erlebnis, das uns besonders stark in einer solchen Denkweise hat entgegentreten können, wie wir sie vorgestern durch das Gespräch zwischen Goethe und Schiller konstatiert haben. Wir haben gesehen, daß Schiller in dem Augenblick, als er mit Goethe über die Art der Natur-betrachtung sprach, noch der Meinung war, daß das, was Goethe mit ein paar Strichen als Urpflanze hinzeichnete, eine Idee, etwas Abstraktes sei, das man erhalte, wenn man die unterscheidenden Merkmale wegläßt und das Gemein­same zusammenfügt. Und wir haben gesehen, daß Goethe darauf sagte: Wenn das eine Idee ist, dann sehe ich meine Ideen mit Augen! In diesem Moment standen sich zwei ganz verschiedene Wirklichkeiten gegenüber. Schiller hat sich wirklich ganz zu Goethes Anschauungsweise hinaufgearbei­tet, so daß man sich in der Schillerverehrung nichts vergibt, wenn man ihn als Beispiel anführt für jenes menschliche Seelenvermögen, das in Abstraktionen schwebt und vor­zugsweise in den mit dem bloßen Verstande erfaßten Vor­stellungen der Dinge lebt. Das ist eine besondere Seelen-anlage, die, wenn der Mensch zu einer höheren Entwicke­lung gelangen will, unter Umständen eine recht böse Rolle spielen kann.",
      "Es gibt Menschen, die vorzugsweise in der Richtung zum Abstrakten veranlagt sind. Wenn sie nun die Abstraktheit verbinden mit etwas, was ihnen da als Seelenkraft entgegen­tritt, so ist das in der Regel der Begriff der Unproduktivität. Diese Menschen sind manchmal sehr scharfsinnig, können scharfe Unterscheidungen ausführen, diesen oder jenen Be­griff wunderbar verbinden. Aber gerade eine solche Seelen-stimmung ist oft auch damit verknüpft, daß die geistigen Einflüsse, die Inspirationen, keinen Eingang finden.",
      "Diese Seelenverfassung, die durch Unproduktivität und Abstraktheit gekennzeichnet ist, wird uns in den Irrlichtern reprasentiert. Sie nehmen das Gold auf, wo sie es finden; sie sind frei von aller Erfindungsgabe, sind unproduktiv, können keine Ideen fassen. Diesen Ideen stehen sie fremd gegenüber. Sie haben nicht den Willen, sich selbstlos den Dingen hinzugeben, an die Tatsachen sich zu halten und Begriffe nur soweit zu benutzen, als sie Dolmetscher für die Tatsachen sind. Ihnen kommt es darauf an, ihren Verstand mit Begriffen vollzupfropfen und diese dann wieder in ver­schwenderischer Weise fortzugeben. Sie gleichen einem Men­schen, der sich in Bibliotheken setzt, die Weisheit da sam­melt, in sich aufnimmt und wieder in entsprechender Weise von sich gibt. Diese Irrlichter sind charakteristisch für das­jenige Seelenvermögen, das niemals imstande ist, einen ein­zigen literarischen Gedanken oder Empfindungsgehalt zu fassen, das aber sehr wohl das, was einmal da ist als Lite­raturgeschichte, das, was produktive Geister geleistet haben, in schöne Formen zu fassen vermag. Es soll hier nichts gegen dieses Seelenvermögen gesprochen werden. Hätte der Mensch dieses Seelenvermögen nicht oder pflegte er es nicht, wenn es ihm in zu geringem Maße zuteil geworden ist, so würde ihm etwas fehlen, was in bezug auf die wirkliche Er­kenntnisfähigkeit notwendig vorhanden sein muß. Goethe",
      "stellt durch das Bild der Irrlichter, durch die ganzen Ver­hältnisse, in denen er sie auftreten und wirken läßt, die Art und Weise dar, wie ein solches Seelenvermögen im Verhält­nis zu den anderen Seelenvermögen arbeitet, wie es schadet und nützt. Wahrhaftig, wenn jemand dieses Seelenvermögen nicht hätte und zu höheren Stufen der Erkenntnis aufstei­gen wollte, dann würde nichts da sein, was ihm den Tempel aufschließen könnte. Goethe stellt ebenso die Vorzüge wie auf der anderen Seite die Nachteile dieses Seelenvermögens hin. Das, was in den Irrlichtern gegeben ist, stellt eben ein Seelenelement dar. In dem Augenblick, wo es nach der einen oder andern Seite hin ein selbständiges Leben führen will, wird es schädlich. Es wird aus dieser Abstraktheit ein kriti­sches Vermögen, das die Menschen so gestaltet, daß sie zwar alles lernen, sich aber nicht weiterentwickeln können, weil ihnen das produktive Element fehlt. Goethe zeigt aber ganz klar, inwiefern auch ein Wertvolles in dem ist, was in den Irrlichtern dargestellt wird. Das, was sie in sich haben, kann auch etwas Wertvolles werden: in der Schlange wird das Gold der Irrlichter zu etwas Wertvollem, insofern es die Gegenstände, welche um die Schlange herum sind, be­leuchtet.",
      "Was in den Irrlichtern lebt, wird, wenn es in anderer Weise verarbeitet wird, in der menschlichen Seele äußerst fruchtbar werden. Wenn der Mensch sich bestrebt, das, was er in Begriffen, Ideen und idealen Gebilden erleben kann, nicht für sich als ein Abstraktes hinzustellen, sondern es so zu betrachten, daß es ihm Führer und Dolmetscher wird für das, was an Realitäten um ihn herum ist, so daß er sich ebensogern und hingebungsvoll an die Beobachtungen hält wie an die Abstraktheit der Begriffe, dann ist er mit dieser Seelenkraft in dem gleichen Falle wie die grüne Schlange. Dann kann er aus dem bloß Abstrakten, aus den bloßen",
      "Begriffen Licht und Weisheit gestalten. Dann führt sie ihn nicht dazu, daß er zur vertikalen Linie wird, die alle Ver­bindung und Beziehung zur Fläche verliert. Die Irrlichter sind die Verwandten der Schlange, sie sind aber von der vertikalen Linie. Die Goldstücke fallen zwischen die Felsen hinein, die Schlange nimmt sie auf und wird dadurch inner­lich leuchtend. Die Weisheit nimmt der auf, der mit diesen Begriffen an die Dinge selbst herangeht.",
      "Goethe gibt uns auch ein Beispiel, wie man an den Be­griffen arbeiten soll. Goethe hat den Begriff der Urpflanze. Was ist er zunächst? Ein abstrakter Begriff. Würde er ihn abstrakt ausbilden, so würde er ein leeres Gebilde werden, das alles Lebendige tötet, wie das hingeworfene Gold der Irrlichter den Mops tötet. Denken Sie sich aber, was Goethe mit dem Begriffe der Urpflanze tut. Verfolgen wir ihn auf seiner italienischen Reise, dann sehen wir, wie dieser Begriff nur das Leitmotiv ist, um von Pflanze zu Pflanze, von Wesen zu Wesen zu gehen. Er nimmt den Begriff, geht von ihm aus zur Pflanze über und sieht, wie sie sich in dieser oder jener Form ausgestaltet, wie sie ganz andere Formen annimmt in niederer oder höherer Gegend und so weiter. Nun verfolgt er von Stufe zu Stufe, wie die geistige Realität oder Gestalt in jede sinnliche Gestak hineinkriecht. Er selbst kriecht da herum wie die Schlange in den Klüften der Erde. So ist für Goethe die Begriffswelt nichts anderes als das, was sich in die objektive Wirklichkeit hineinspinnen läßt. Die Schlange ist ihm der Repräsentant der Seelenkraft, die nicht in egoistischer Weise hinaufstrebt zu den höheren Gebieten des Daseins und sich über alles zu erheben ver­sucht, sondern die geduldig den Begriff durch die Beobach­tung fortwährend bewahrheiten läßt, die geduldig von Er­fahrung zu Erfahrung, von Erlebnis zu Erlebnis geht.",
      "Wenn der Mensch nicht bloß theoretisiert, nicht bloß in",
      "den Begriffen lebt, sondern sie auf das Leben, auf die Er­fahrung anwendet, dann ist er mit dieser Seelenkraft in der Lage der Schlange. Das ist in ganz umfassendem Sinne rich­tig. Wer die Philosophie nicht wie eine Theorie aufnimmt, sondern als das, was sie sein soll, wer die geisteswissen­schaftlichen Begriffe als Aufgaben für das Leben betrachtet, der weiß, daß gerade Begriffe, und seien sie auch die höch­sten, so verwendet werden sollen, daß sie in das Leben ein­fließen und an den täglichen Erlebnissen sich bewahrheiten können. Für den, der ein paar Begriffe gelernt hat, sie aber nicht ins Leben übertragen kann, liegt ein ähnliches Ver­hältnis vor wie für den, der ein Kochbuch auswendig gelernt hat, aber doch nicht kochen kann. So wie das Gold ein Mit­tel ist, die Dinge zu beleuchten, so beleuchtet Goethe durch seine Begriffe die Dinge, welche um ihn herum sind.",
      "Das ist das Belehrende und Großartige an Goethes Wis­senschaftlichkeit und allem Goetheschen Streben, daß das, was er an Begriffen und Ideen gibt, Realität hat, daß es wirkt wie ein Licht, leuchtend wird und die Gegenstände um ihn herum beleuchtet. Das vorgestern hervorgehobene Universale bei Goethe macht es, daß wir, wenn wir an ihn herantreten, nie das Gefühl haben, das ist Goethes «Mei­nung». Er steht da und wenn wir ihn sehen, finden wir nur, daß wir die Dinge besser begreifen, die uns vorher nicht so begreiflich waren. Dadurch eben konnte er zum Vereini­gungspunkt feindlicher Brüder werden, wie wir vorgestern gesehen haben. Wollten wir jeden Zug in dem Märchen be­sprechen, jede Gestalt charakterisieren, dann müßte ich über dieses Märchen nicht drei Stunden, sondern drei Wochen sprechen. Ich kann also nur die tieferen Prinzipien in die­sem Märchen angeben. Jeder Zug aber weist uns in Goethes Vorstellungsart und Goethes Weltgesinnung hinein.",
      "Diejenigen Seelenkräfte, welche in den Irrlichtern, in der",
      "grünen Schlange und in den Königen dargestellt sind, be­finden sich auf der einen Seite des Flusses. Drüben auf der andern Seite wohnt die schöne Lilie, das Ideal vollkomme­ner Erkenntnis und vollkommenen Lebens und Schaffens. Von dem Fährmann haben wir gehört, daß er die Gestalten von dem jenseitigen Ufer herüberführen kann, aber nie­mand wieder zurückführen darf. Wenden wir das auf unsere ganze Seelenstimmung und Veredlung an.",
      "Wir Menschen finden uns als seelische Wesenheiten hier auf der Erde. Diese oder jene Seelenkräfte arbeiten an uns als Anlagen, als mehr oder weniger ausgebildete Seelen-kräfte. Sie sind in uns. Es lebt aber in uns auch noch etwas anderes. In uns Menschen, wenn wir uns selbst richtig er­fassen, lebt das Gefühl, die Erkenntnis, daß die Seelen-kräfte in uns, welche uns das Wesen der Dinge zuletzt ver­mitteln, mit den Grundgeistern der Welt, mit den schöpfe­rischen, geistigen Mächten innig verwandt sind. Indem wir uns nach diesen schöpferischen Mächten sehnen, sehnen wir uns nach der schönen Lilie. So wissen wir, daß alles, was einerseits von der schönen Lilie herstammt, andererseits wieder zu ihr zurückzukehren strebt. Unbekannte Kräfte, die wir nicht meistern, haben uns herübergebracht. Wir wis­sen, daß gewisse Kräfte uns von der jenseitigen Welt über den Grenz fluß zur diesseitigen Welt herübergebracht haben. Diese durch den Fährmann charakterisierten, in den Tiefen der unbewußten Natur wirkenden Kräfte können aber uns nicht wieder zurückbringen, denn sonst würde der Mensch ohne seine Arbeit, ohne sein Zutun, genau ebenso wieder in das Reich des Göttlichen zurückkehren, wie er herüber­gekommen ist. Die Kräfte, die uns als unbewußte Natur­kräfte herübergefahren haben in das Reich der strebenden Menschen, dürfen uns nicht wieder zurückführen. Dazu sind andere Kräfte nötig. Das weiß auch Goethe. Goethe will",
      "aber auch zeigen, wie der Mensch es anfangen muß, daß er sich mit der schönen Lilie wieder vereinigen kann.",
      "Zwei Wege gibt es. Der eine geht über die grüne Schlange, über sie konnen wir hinübergehen, da finden wir nach und nach das Reich des Geistes. Der andere Weg geht über den Schatten des Riesen. Es wird uns dargestellt, daß der Riese, der sonst ganz kraftlos ist, in der Dämmerstunde seine Hand ausstreckt, deren Schatten sich dann über den Fluß legt. Über diesen Schatten führt der zweite Weg. Wer also bei hellem Tageslicht hinüber will in das Reich des Geistes, muß sich des Weges bedienen, den die Schlange vermittelt, wer im Dämmerlichte hinüberkominen will, der kann sich des Weges bedienen, der über den Schatten des Riesen führt. Das sind die zwei Wege, um zu einem geistigen Weltenbilde zu kommen. Derjenige, der nicht mit menschlichen Begrif­fen, menschlichen Ideen, nicht mit denjenigen Mächten, die durch das wertlose Gold, bei bloß sophistischen Geistern, und durch die Irrlichter charakterisiert werden, die geistige Welt erstrebt, sondern in Geduld und Selbstlosigkeit von Erlebnis zu Erlebnis geht, gelangt beim hellen Sonnenschein zum jenseitigen Ufer.",
      "Goethe weiß, daß wirkliche Forschung nicht am Mate­riellen kleben bleibt, sondern herüberführen muß über die Grenze, über den Fluß, der uns von dem Geistigen trennt. Es gibt aber noch einen andern Weg, einen Weg für unent­wickeltere Menschen, die nicht den Weg des Erkennens, nicht den Erkenntnispfad gehen wollen, einen Weg, der repräsentiert wird durch den Riesen. Kraftlos ist dieser Riese, nur sein Schatten hat eine gewisse Kraft. Was ist nun im echten Sinne kraftlos? Nehmen Sie alle Zustände, in die der Mensch kommen kann bei herabgestimmtem Bewußt­sein, wie beim Hypnotismus, Somnambulismus, ja selbst bei Traumzuständen: alles das, wodurch das helle Tagesbewußtsein",
      "herabgedämmert wird, wodurch der Mensch niedrigere Seelenkräfte als das helle Tagesbewußtsein in sich wirken läßt, gehört zu diesem zweiten Weg. Da wird die Seele beim Kraftloswerden der alltäglichen Seelenkraft ins wirk­liche Reich des Geistes hinübergeführt. Die Seele wird aber nicht selbst fähig, in das geistige Reich hinüberzugehen, sondern sie bleibt bewußtlos und wird wie der Schatten in das Reich des Geistes hinübergeführt. Goethe nimmt noch alles das, was unbewußt, gewohnheitsmäßig wirkt, ohne daß die Seelenkräfte, die bei hellem Tagesbewußts ein wirk­sam werden, daran beteiligt sind, unter die Kräfte, welche in dem Schatten des Riesen vorzustellen sind. Schiller, der in das, was Goethe meinte, eingeweiht war, schrieb zur Zeit der großen Stürme im westlichen Europa einmal an Goethe:",
      "Froh bin ich, daß Sie von dem Schatten des Riesen nicht unsanft angefaßt worden sind. - Was meint Schiller damit? Er meinte, wenn Goethe weiter nach Westen gewandert wäre, so würde er von den revolutionären Mächten des Westens erfaßt worden sein.",
      "Dann sehen wir, daß das, was der Mensch als Hochstand der Erkenntnisentwickelung erlangen soll, in dem Tempel dargestellt wird. Der Tempel bedeutet also einen höheren Entwicklungsstand des Menschen. In der jetzigen Zeit, würde Goethe sagen, ist der Tempel etwas Verborgenes, ist er unter den engen Klüften der Erde. Eine solche strebende Seelenkraft, wie sie durch die Schlange repräsentiert wird, kann nur undeutlich die Gestalt des Tempels fühlen. Da­durch, daß sie Ideale, das Gold in sich aufnimmt, kann sie diese Gestak erleuchten, aber im Grunde genommen kann dieser Tempel in der jetzigen Zeit nur als ein unterirdisches Geheimnis da sein. Dadurch, daß Goethe diesen Tempel für die äußere Kultur etwas Unterirdisches sein läßt, weist er aber auch darauf hin, daß dieses Geheimnis einem weiterentwickelten",
      "Menschen erschlossen werden muß. Er weist damit auf die geisteswissenschaftliche Strömung hin, die heute schon breite Menschenmassen erfaßt hat, die in um­fassendem Sinne populär zu machen sucht, was der Inhalt der Geisteswissenschaft, der Initiation oder des Einweihungs­prinzips, der Jnhalt der Tempelgeheimnisse ist.",
      "In diesem echt freien Goetheschen Sinne ist daher der Jüngling als Repräsentant der strebenden Menschheit zu betrachten. Daher soll sich der Tempel über den Fluß er­heben, damit nicht nur einzelne wenige, welche Erleuchtung suchen, herüber und hinüber gehen können, sondern damit dann alle Menschen auf der Brücke den Fluß passieren kön­nen. Einen Zukunftszustand stellte Goethe hin in dem Initiations-Tempel über der Erde, der da sein wird, wenn der Mensch aus dem Reiche des Sinnlichen in das Reich des Geistigen und aus dem Reiche des Geistigen in das Reich des Sinnlichen gehen kann.",
      "Wodurch ist das in dem Märchen erreicht worden? Da­durch, daß das eigentliche Geheimnis des Märchens erfüllt ist. Die Lösung des Märchens steht im Märchen selber, sagt Schiller. Er hat aber auch darauf hingewiesen, daß recht sonderbar das Wort der Lösung darinnen steht. Sie erinnern sich des Alten mit der Lampe, die nur leuchtet, wo schon Licht ist. Wer ist nun der Alte? Was ist diese Lampe? Was hat sie für ein eigenartiges Licht? Der Alte steht über der Situation. Seine Lampe hat die merkwürdige Eigenschaft, daß sie die Dinge verwandelt, Holz in Silber, Stein in Gold. Sie hat auch die Eigenschaft, daß sie nur da leuchtet, wo schon eine Empfänglichkeit, eine bestimmte Art des Lichtes vorhanden ist. Als der Alte in den unterirdischen Tempel hineintritt, wird gefragt, wieviel Geheimnisse er kenne. «Drei», versetzt der Alte. Auf die Frage des silbernen Königs: «Welches ist das wichtigste?», antwortet er: «Das",
      "offenbare.» Und auf die Frage des ehernen Königs: «Willst du es auch uns eröffnen?», sagt er: «Sobald ich das vierte weiß.» Darauf zischelt die Schlange dem Alten etwas ins Ohr, worauf er sagt: «Es ist an der Zeit!»",
      "Das, was die Schlange dem Alten ins Ohr sagte, das ist die Lösung des Rätsels, und wir haben zu erforschen, was die Schlange dem Alten ins Ohr gesagt hat. Es würde zu weit führen, ausführlich zu sagen, was die drei Geheimnisse bedeuten. Nur andeuten will ich es.",
      "Es gibt drei Reiche, die in der Entwickelung heute sozu­sagen stationär sind: das Mineral-, das Pflanzen- und das Tierreich, die dem Menschen gegenüber, der sich noch in weiterer Entwickelung befindet, abgeschlossen sind. Die innere Entwickelung, die der Mensch durchmacht, ist so vehement und bedeutsam, daß sie sich mit der Entwickelung der anderen drei Naturreiche nicht vergleichen läßt. Daß ein Naturreich dadurch zu dem gegenwärtigen Stande ge­kommen ist, daß es zu einem Abschluß gelangt ist, das ist es, was in dem Geheimnis des Alten liegt, das ist es, was die Gesetze des Mineral-, Pflanzen- und Tierreichs erklärt. Aber nun kommt das vierte Reich, das Reich des Menschen, das Geheimnis, das in der Seele des Menschen offenbar werden soll. Dieses Geheimnis ist ein solches, das der Alte erst er­fahren muß. Und wie muß er es erfahren? Er weiß, worin es besteht, aber die Schlange muß es ihm erst sagen. Das deutet uns an, daß mit dem Menschen noch etwas Beson­deres vorgehen muß, wenn er ebenso das Ziel der Ent­wickelung erreichen will, wie die anderen drei Reiche es erreicht haben. Was mit dem Menschen im Innersten seiner Seele geschehen ist, und was geschehen muß, wenn er das Ziel erreichen soll, das sagt die Schlange dem Alten ins Ohr. Sie sagt, wie eine bestimmte Seelenkraft sich entwickeln muß, wenn eine höhere Stufe erreicht werden soll, sie sagt,",
      "daß sie den Willen habe, sich dafür aufzuopfern, und sie opfert sich auf. Bisher hat sie nur eineBrücke gebildet, wenn hie und da ein einzelner Mensch hinübergehen wollte; nun aber wird sie zu einer dauernden Brücke werden, indem sie zerfällt, so daß der Mensch eine dauernde Verbindung haben wird zwischen dem Diesseits und Jenseits, zwischen Geistigem und Sinnlichem.",
      "Daß die Schlange den Willen zur Aufopferung hat, das ist es, was als die Bedingung für die Eröffnung des vierten Geheimnisses angesehen werden muß. In dem Augenblick, wo der Alte hört, daß die Schlange sich opfern will, kann er dann auch sagen: «Es ist an der Zeit!» Es ist die Seelen-kraft, die an das Äußere sich hält. Und der Weg muß da­durch betreten werden, daß diese Seelenkraft und innere Wissenschaft nicht Selbstzweck wird, sondern sich hinopfert. Das ist wirklich ein Geheimnis, wenn es auch als ein «offen­bares» Geheimnis angesprochen wird, das heißt, wenn es auch jedem, der es will, offenbar werden kann.",
      "Was in weitem Umkreis als Selbstzweck angesehen wird",
      "- alles, was wir lernen können in der Naturwissenschaft, in der Kulturwissenschaft, in der Geschichte, in der Mathema­tik und allen anderen Wissenschaften -, es kann niemals Selbstzweck sein. Wir können niemals zur wahren Einsicht in die Tiefen der Welt kommen, wenn wir sie als etwas für sich betrachten. Erst wenn wir jederzeit bereit sind, sie in uns aufzunehmen und als Mittel zu betrachten, das wir hinopfern als Brücke, über die wir hinüberschreiten können, dann kommen wir zur wirklichen Erkenntnis. Wir sperren uns ab von der höheren, von der wirklichen Erkenntnis, wenn wir nicht auch bereit sind, uns hinzuopfern. Erst dann wird der Mensch einen Begriff bekommen von dem, was Einweihung ist, wenn er aufhört, sich aus äußerlich-sinnlichen Begriffen eine Weltanschauung zu zimmern. Er",
      "muß ganz Gefühl, ganz Seelenstimmung werden, eine solche Seelenstimmung, die dem entspricht, was Goethe als höchste Errungenschaft des Menschen in seinem «Westöstlichen Divan» charakterisiert:",
      "Und so lang du das nicht hast,",
      "Dieses:    Stirb und Werde!",
      "Bist du nur ein trüber Gast",
      "Auf der dunklen Erde.",
      "Stirb und Werde! Lerne kennen, was das Leben bieten kann, gehe hindurch, aber überwinde, gehe über dich hin­aus. Laß es dir zur Brücke werden, und du wirst in einem höheren Leben aufleben, mit dem Wesen der Dinge eines sein, wenn du nicht mehr in dem Wahne lebst, daß du, ge­trennt von dem höheren Ich, das Wesen der Dinge erschöp­fen kannst. Goethe erinnert sich gern, da, wo er von der Hinopferung des Begriffes und des Seelenmaterials spricht, um in höheren Sphären aufzuleben, wo er von der tiefsten innersten Liebe spricht, an die Worte des Mystikers Jakob Böhme, der dieses Erlebnis der Hinopferung der Schlange in sich kennt. Jakob Böhme hat ihn vielleicht gerade darauf hingewiesen und bewirkt, daß es ihm so klar war, daß der Mensch schon im physischen Leibe hinüberleben kann in eine Welt, die er sonst erst nach dem Tode betritt: in die Welt des Ewigen, des Geistigen. Jakob Böhme wußte auch, daß es von dem Menschen abhängt, ob er in höherem Sinne in die geistige Welt hinübergleiten kann. Er zeigt es in dem Spruche: Wer nicht stirbt, eh' er stirbt, der verdirbt, wenn er stirbt. - Ein bedeutsames Wort! Der Mensch, der nicht stirbt, bevor er stirbt, das heißt, der nicht das Ewige, den inneren Wesenskern in sich entwickelt, der wird auch nicht in der Lage sein, wenn er stirbt, den geistigen Wesenskern in sich wiederzufinden. Das Ewige ist in uns. Wir müssen es",
      "im Leibe entwickeln, damit wir es außer dem Leibe finden können. «Wer nicht stirbt, eh' er stirbt, der verdirbt, wenn er stirbt.» So ist es auch mit dem andern Satze: «Und so ist der Tod die Wurzel alles Lebens.»",
      "Sodann sehen wir, daß das Seelische nur da erleuchten kann, wo schon Licht ist: die Lampe des Alten kann nur das erleuchten, was schon erleuchtet ist. Wieder werden wir auf Seelenkräfte des Menschen hingewiesen, auf jene Seelen-kräfte, die als etwas Besonderes uns entgegentreten, die Seelenkräfte der Devotion, der religiösen Hingabe, die durch Jahrhunderte und Jahrtausende hindurch den Men­schen die Botschaft von geistigen Welten gebracht haben, denen, die das Licht nicht auf dem Wege der Wissenschaft oder sonstwie suchen konnten. Das Licht der verschiedenen religiösen Offenbarungen wird dargestellt in dem Alten, der dieses Licht hat. Wer aber nicht von innen heraus dem religiösen Sinn ein Licht entgegenbringt, dem leuchtet nicht die Lampe der Religion. Nur da kann sie leuchten, wo ihr schon Licht entgegenkommt. Sie ist es gewesen, die die Menschen verwandelt hat, die alles Tote in das beseelte Lebendige hinübergeführt hat.",
      "Und dann sehen wir, daß durch die Hinopferung der Schlange die beiden Reiche miteinander vereinigt werden. Nachdem sie sozusagen durch symbolische Vorgänge durch-macht, was der Mensch bei seiner Höherentwickelung im esoterischen Sinne durchzumachen hat, sehen wir, wie der Tempel der Erkenntnis durch alle drei menschlichen Seelen-kräfte hinaufgeführt wird über den Fluß, wie er hinauf-wandert und wie jede Seelenkraft ihren Dienst verrichtet. Es wird da angedeutet, daß die Seelenkräfte in Harmonie zusammenklingen müssen, indem uns gesagt wird: Die ein­zelne Persönlichkeit vermag nichts; wenn aber alle zur guten Stunde zusammenwirken, wenn die Gewaltigen und",
      "die Geringen im richtigen Verhältnis zueinander wirken, dann kann erstehen, was die Seele befähigt, den höchsten Zustand zu erreichen, die Vereinigung mit der schönen Lilie.",
      "Dann wandert aber auch der Tempel aus den verborgenen Klüften hinauf an die Oberfläche für alle, die in Wahrheit nach Erkenntnis und Weisheit streben. Der Jüngling wird begabt mit den Erkenntniskräften des Denkens und Vor­stellens durch den goldenen König: «Erkenne das Höchste.» Er wird begabt mit den Erkenntniskräften des Gefühls durch den silbernen König, was Goethe so schön andeutet mit den Worten: «Weide die Schafe!» Im Fühlen wurzeln Kunst und Religion, und für Goethe war beides eine Ein­heit, schon damals, als er von seiner italienischen Reise über die Kunstwerke Italiens schrieb: «Da ist Notwendigkeit, da ist Gott!»",
      "Aber da ist auch die Tat - wenn der Mensch sie nicht zum Daseinskampf verwendet, wenn sie ihm zur Waffe wird, um Schönheit und Weisheit zu erkämpfen. Das ist in den Worten enthalten, die der eherne König zu dem Jüngling spricht: «Das Schwert an der Linken, die Rechte frei!» Darin liegt eine ganze Welt. Die Rechte frei zum Wirken aus der menschlichen Natur des Selbst heraus.",
      "Und was geschieht mit dem vierten König, in dem alle drei Elemente durcheinandergemischt sind? Dieser gemischte König schmilzt zu einer grotesken Figur zusammen. Die Irrlichter kommen und lecken das noch vorhandene Gold aus ihm heraus. Die Seelenkräfte des Menschen wollen da noch studieren, was an menschlichen Entwicklungsstufen, die schon überwunden sind, einst vorhanden war.",
      "Nehmen wir noch einen Zug, nämlich den, wie der Riese da taumelnd einherkommt und dann wie eine Bildsäule dasteht und die Stunden anzeigt: Wenn der Mensch sein",
      "Leben in Harmonie gebracht hat, dann hat auch das Unter­geordnete Bedeutung für das, was methodische Ordnung sein soll. Das soll sich wie eine Gewohnheit ausprägen. Selbst das Unbewußte wird dann einen wertvollen Sinn erhalten. Deshalb wird der Riese gleichsam wie eine Uhr dargestellt.",
      "Der Alte mit der Lampe ist vermählt mit der Alten. Diese Alte stellt uns nichts anderes dar als die gesunde ver­ständige menschliche Seelenkraft, die nicht in hohe Regio­nen geistiger Abstraktion eindringt, die aber alles gesund und praktisch angreift, wie zum Beispiel in der Religion, die ja in dem Alten mit der Lampe dargestellt wird. Ge­rade sie kann dann auch dem Fährmann die Löhnung bringen: drei Kohlhäupter, drei Zwiebeln und drei Arti­schocken. Eine solche Entwickelungsstufe ist noch nicht über die Zeitlichkeit hinweggekommen. Daß sie so behandelt wird, wie es von den Irrlichtern geschieht, ist wohl ein Abbild davon, wie abstrakte Geister meistens hochmutig auf Menschen herunterschauen, die aus unmittelbaren In­stinkten oder Intuitionen heraus die Dinge erfassen. .",
      "Jeder Zug, jede Wendung in diesem Märchen ist von tiefgründiger Bedeutung, und tritt man noch in eine Er­klärung ein, die esoterisch sein soll, dann findet man, daß man eigentlich nur die Methode der Erklärung anzugeben vermag. Vertiefen Sie sich in das Märchen selber, dann werden Sie finden, daß eine ganze Welt darinnen zu finden ist, weit mehr, als heute angedeutet werden konnte.",
      "Wie sehr Goethes geistige Weltanschauung sein ganzes Leben durchzieht, wie in den Dingen der Geisteserkenntnis er noch im spätesten Alter in Einklang steht mit früher Ge­schaffenem, das möchte ich Ihnen noch an zwei Beispielen zeigen. Als Goethe den «Faust» schrieb, hatte er eine ge-wisse Vorstellung übernommen, die auf ein Symbolum eines",
      "tieferen Entwickelungsweges der Natur zurückgeht. Als Faust von seinem Vater spricht, der Alchimist war und die alten Lehren gläubig hingenommen, aber schon damals mißverstanden hatte, sagt er, daß sein Vater auch das ge-macht habe, daß sich",
      ". . . ein roter Leu, ein kühner Freier,",
      "Im lauen Bad der Lilie vermählt.",
      "Das sagt Faust, ohne daß er die Bedeutung davon kennt. Solch ein Wort aber kann zur Leiter werden, die auf hohe Entwickelungsstufen hinaufführt. Goethe zeigt in dem Märchen den nach der höchsten Braut strebenden Menschen in seinem Jüngling, und das, womit er vereinigt werden soll, nennt er die schöne Lilie. Sie sehen, diese Lilie finden Sie auch schon in den ersten Partien des «Faust». Und auch das, was als Grundnerv der Goetheschen Anschauung sei­nen Ausdruck im Märchen gefunden hat, finden wir im «Faust», im zweiten Teile, im Chorus mysticus, da, wo Faust vor dem Eintritt in die geistige Welt steht, wo Goethe sein Bekenntnis zur geistigen Weltanschauung mit monumenta­len Worten ablegt. Er zeigt da, wie in drei aufeinander­folgenden Stufen, nämlich die Läuterung der Vorstellung, die Erleuchtung der Gefühle und die Herausarbeitung des Willens zur reinen Tat, der Aufstieg auf dem Erkenntnis-weg erfolgt.",
      "Was der Mensch durch die Läuterung der Vorstellung erlangt, führt ihn dazu, das Geistige hinter allem zu er­kennen. Das Sinnliche wird ein Gleichnis für das Geistige. Er dringt tiefer ein, um das noch zu erfassen, was für die Vorstellung unzugänglich ist. Er erreicht dann eine Stufe, auf der er die Dinge nicht mehr durch die Vorstellung be­trachtet, sondern in die Sache selbst hineingewiesen wird, da, wo das Wesen der Dinge und das, was man nicht beschreiben",
      "kann, Erreichnis wird. Und das, was man nicht beschreiben kann, was man, wie man im Laufe der Winter­Vorträge hören wird, in anderer Weise vorstellen muß, das, wobei man zu den Geheimnissen des Willens vorschreiten muß, bezeichnet er eben als das «Unbeschreibliche». Wenn der Mensch den dreifachen Weg durch die Vorstellung, das Gefühl und den Willen gemacht hat, dann vereinigt er sich mit dem, was im Chorus mysticus das «Ewig-Weibliche» genannt wird, das, was als menschliche Seele durchgemacht hat seine Entwickelung, das, was als die schöne Lilie dar­gestellt wird.",
      "So sehen wir, daß Goethe geradezu sein tiefstes Bekennt­nis, seine geheime Offenbarung auch noch da ausspricht, wo er sein großes Bekenntnisgedicht zum Abschluß bringt, nachdem er durch die Vorstellung, durch das Gefühl und den Willen emporgedrungen ist bis zur Vereinigung mit der schönen Lilie, bis zu dem Zustande, der seinen Aus­druck findet in der erwähnten Stelle des Chorus mysticus, die dasselbe ausdrückt, was Goethes Philosophie und Gei­steswissenschaft und was auch das «Märchen» sagt:",
      "Alles Vergängliche",
      "Ist nur ein Gleichnis!",
      "Das Unzulängliche,",
      "Hier wird's Erreichnis;",
      "Das Unbeschreibliche,",
      "Hier ist's getan;",
      "Das Ewig-Weibliche",
      "Zieht uns hinan!"
    ],
    "sentences": [
      [
        "GOETHES GEHEIME OFFENBARUNG"
      ],
      [
        "Berlin, 24.",
        "Oktober 1908"
      ],
      [
        "Einem Vortrage wie dem heutigen kann leicht der Vorwurf gemacht werden, daß in erzwungener Weise symbolische und allegorische Ausdeutungen gegeben werden von etwas, was ein Dichter im freien Spiel der Einbildungskraft ge-schaffen hat.",
        "Wir haben uns ja vorgestern die Aufgabe vorgezeichnet, das Goethesche «Märchen» von der grünen Schlange und der schönen Lilie, wie es uns da vor Augen getreten ist, in seinem tieferen Sinn zu erforschen.",
        "Immer wieder wird es geschehen, daß eine solche, wenn man so sagen will, Auslegung, Erklärung eines Phantasiewerks mit den Worten abgetan wird: Ach, da werden allerlei tiefsin­nig sein sollende Symbole und Bedeutungen in den Gestal­ten des Werkes gesucht. - Deshalb möchte ich von vorn­herein bemerken, daß das, was heute von mir gesagt werden soll, nichts zu tun hat mit dem, was allerdings gerade von theosophischer Seite aus oft in bezug auf symbolische oder allegorische Ausdeutungen von Märchen oder dichterischen Werken gemacht worden ist.",
        "Und weil ich weiß, daß ähn­lichen Auseinandersetzungen, die ich gegeben habe, immer wieder entgegengehalten wurde, auf solche symbolische Deutungen dichterischer Figuren lasse man sich nicht ein, sö kann ich nicht scharf genug betonen, daß das, was hier zu sagen ist, einzig und allein in folgendem Sinne aufgefaßt werden muß."
      ],
      [
        "Uns liegt heute ein dichterisches Werk vor, das Werk"
      ],
      [
        "einer umfassenden und in die Tiefe der Dinge dringenden Einbildungskraft oder Phantasie: Das «Märchen» von der grünen Schlange und der schönen Lilie.",
        "Die Frage darf wohl aufgeworfen werden: Dürfen wir von irgendeinem Ge­sichtspunkte an das Werk herangehen und versuchen, den ideellen, den wirklichen Inhalt eines solchen dichterischen Produktes zu ergründen?"
      ],
      [
        "Wir sehen die Pflanze vor uns.",
        "Der Mensch tritt an die Pflanze heran; er untersucht die Gesetze, die innere Regel­mäßigkeit, nach der die Pflanze wächst und gedeiht, nach der sie Stück für Stück ihres Wesens entwickelt."
      ],
      [
        "Hat der Botaniker oder hat jemand, der kein Botaniker ist, sich aber das Werden der Pflanze ideell zurechtlegt, das Recht dazu?",
        "Kann man ihm entgegenhalten: Von dem, was du da findest an Gesetzen, weiß die Pflanze nichts, sie kennt nicht die Gesetze ihres Wachstums und ihrer Entwickelung! - Ge­nau den gleichen Wert, den dieser Einwand hätte, wenn man ihn gegen den Botaniker erheben würde oder gegen den Lyriker, der das, was er bei der Pflanze empfindet, in seinen lyrischen Leistungen zum Ausdruck bringt, genau denselben Sinn und Wert hätte der Einwand, den man gegen eine solche Erklärung des Goetheschen Märchens vorbringen könnte."
      ],
      [
        "Nicht möchte ich die Dinge so aufgefaßt wissen, als ob ich sagen würde: Da haben wir eine Schlange, die bedeu­tet dies oder jenes, da haben wir einen goldenen, einen silber­nen, einen ehernen König, sie bedeuten dies oder jenes.",
        "Nicht in diesem symbolisch-allegorischen Sinne möchte ich das Märchen deuten, sondern mehr so, daß in gleicherWeise, wie die Pflanze nach Gesetzen wächst, von denen sie in ihrer Unbewußtheit nichts wissen kann, und wie der Botaniker das Recht hat, diese Gesetze des Pflanzenwachstums zu fin­den, man sich auch sagen muß: Das, was hier auseinander­gesetzt wird, braucht der Dichter Goethe niemals so auseinandergesetzt,"
      ],
      [
        "niemals so vor sein äußeres Tagesbewußt­sein gebracht zu haben.",
        "Dennoch aber ist es ebenso wahr, daß die Gesetzmäßigkeit, der wirkliche, der ideelle Inhalt des Märchens im gleichen Sinne zu betrachten ist wie das, was wir als die Gesetze des Pflanzenwachstums finden, daß es dieselbe Gesetzmäßigkeit ist, nach der die Pflanze wächst, nach der sie entstanden ist, deren sie sich aber in ihrer Un­bewußtheit nicht bewußt ist."
      ],
      [
        "Daher bitte ich, das, was ich zu sagen mir erlauben werde, so aufzufassen, als ob es den Sinn und den Geist der Goetheschen Denkweise und Vorstellungsart darstellte, und als ob derjenige, welcher sich sozusagen berufen fühlt, die ideale Goethesche Weltanschauung vor Sie hinzustellen, eine Berechtigung hätte - damit Sie den Weg finden können zu einem Verständnis der Goetheschen Weltanschauung -, auseinanderzulegen das Erzeugnis Goethescher Phantasie, herauszuheben die Gestalten, und die Wechselbeziehungen zu zeigen, in welchen er sie verwendet hat, genau ebenso, wie der Botaniker zeigt, daß die Pflanze nach den Gesetzen wächst, die er gefunden hat."
      ],
      [
        "Goethes Psychologie oder Seelenlehre, das heißt, was er für das Wesen der Seele maßgebend hält, das ist uns in seinem schönen Märchen von der grünen Schlange und der schönen Lilie veranschaulicht.",
        "Und wenn wir uns verständi­gen wollen über das, was darüber gesagt werden muß, so wird es gut sein, wenn wir in einer Vorbetrachtung den Geist seiner Seelenwelt anschaulich zur Sprache bringen.",
        "Schon in dem vorgestrigen Vortrage wurde darauf hinge­wiesen, daß die hier vertretene Weltanschauung davon aus­geht, daß die menschliche Erkenntnis nicht als etwas ein für allemal Feststehendes zu betrachten ist.",
        "Vielfach herrscht ja die Ansicht: So, wie der Mensch heute ist, so ist er eben, und so wie er ist, kann er über alle Dinge unbedingt entscheiden;"
      ],
      [
        "er beobachtet mit seinen Sinnesorganen die Welt, er­faßt sie in ihren Erscheinungen, kombiniert diese mit seinem an die Sinne gefesselten Verstande, und was er da heraus-bringt mit dieser an die Beobachtung sich haltenden Ver­standestätigkeit, das ist eine absolute Welterkenntnis, die für jeden gelten muß. - Im Gegensatze dazu, aber nur im Gegensatze in einer bestimmten Art, steht die geisteswissen­schaftliche Weltanschauung, die hier vertreten wird.",
        "Sie geht davon aus, daß das, was unsere Erkenntnis wird, jederzeit abhängig ist von unseren Organen, von unseren Erkenntnisfähigkeiten, und daß wir selbst als Menschen entwicklungsfähig sind, daß wir an uns arbeiten können, daß wir diejenigen Erkenntnisfähigkeiten, die wir auf einer bestimmten Stufe unseres Daseins haben, höher em­porheben können.",
        "Sie geht davon aus, daß wir sie ausbilden können, daß wir in ähnlicher Weise, wie sich der Mensch aus unvollkommenem Zustande hinaufentwickelt hat zu seinem gegenwärtigen Standpunkt, sie noch weiter entwickeln können, und daß wir durch die Erhebung zu höheren Gesichtspunkten auch zu tieferem Eindringen in die Dinge, zu einer richtigeren Anschauung der Welt kommen müssen."
      ],
      [
        "Soll ich mich noch deutlicher, wenn auch etwas trivial ausdrücken, so möchte ich sagen: Wenn wir ganz absehen von einer Entwickelung der Menschheit und nur Rücksicht nehmen darauf, wie die Menschen sind, die so um uns herum leben, und dann auf jene Menschen blicken, die man in der Kulturgeschichte zu den primitiven Völkerstämmen rechnet, und wenn wir uns fragen, was sie iinstande sind, von den Gesetzen der Welt um uns herum zu erkennen und zu wissen, und es vergleichen mit dem, was ein Durch-schnitts-Europäer mit einigen wissenschaftlichen Begriffen von der Welt wissen kann, dann werden wir sehen, daß der Angehörige jenes primitiven Volksstammes sich von"
      ],
      [
        "dem Durchschnitts-Europäer ganz wesentlich unterscheidet.",
        "Nehmen wir zum Beispiel das Weltbild eines Austral­Negers und das eines, sagen wir, europäischen Monisten, welch letzteres dadurch Realität hat, daß man eine Summe wissenschaftlicher Begriffe der gegenwärtigen Zeit auf­genommen hat.",
        "Es unterscheiden sich diese zwei Weltbilder durchaus."
      ],
      [
        "Aber andererseits ist die Geisteswissenschaft weit ent­fernt, das Weltbild des auf rein materiellem Standpunkte stehenden Menschen zu perhorreszieren oder es als ungültig zu erklären.",
        "Vielmehr werden diese Dinge so angesehen, daß in jedem Falle das Weltbild eines Menschen einer menschlichen Entwickelungsstufe entspricht, und daß der Mensch in der Lage ist, die in ihm enthaltenen Fähigkeiten zu steigern und durch die Steigerung der Fähigkeiten an­deres, Neues zu erfahren."
      ],
      [
        "Es liegt also in der Perspektive der Geisteswissenschaft, daß der Mensch zu immer höherer Erkenntnis dadurch kommt, daß er sich selber weiterentwickelt, und indem er sich weiterentwickelt, ist das, was er in sich erlebt, objek­tiver Welteninhak, den er früher nur nicht gesehen hatte, als er eben noch nicht die Fähigkeit besaß, ihn zu sehen.",
        "Die Geisteswissenschaft unterscheidet sich daher wesentlich von anderen, einseitigen Weltanschauungen, seien sie spiri­tualistisch, seien sie materialistisch, weil sie im Grunde ge­nommen eine ein für allemal abgeschlossene unfehlbare Wahrheit nicht kennt, sondern immer nur die Weisheit und Wahrheit einer bestimmten Entwickelungsstufe, und sich so an das Goethesche Wort hält: Der Mensch hat eigentlich immer nur seine eigene Wahrheit, und sie ist doch immer dieselbe. - Sie ist immer dieselbe, weil das, was wir durch unsere Erkenntniskraft in uns aufnehmen, das Objektive, dasselbe ist."
      ],
      [
        "Wodurch nun gelangt der Mensch dazu, die in ihm liegenden Fähigkeiten und Kräfte zu entwickeln?",
        "Die Gei­steswissenschaft ist sozusagen so alt wie die denkende Menschheit.",
        "Die Geisteswissenschaft stand immer auf dem Standpunkt, daß der Mensch das Ideal einer gewissen Er-kenntnis-Vollkommenheit vor sich hat, der er zustrebt.",
        "Man nannte das Prinzip, das darin liegt, immer das Prinzip der Einweihung oder Initiation.",
        "Einweihung oder Initia­tion heißt also nichts anderes, als die Fähigkeiten des Men­schen zu immer höheren Stufen der Erkenntnis zu steigern und dadurch zu tieferen Einsichten in das Wesen der Welt um uns herum zu gelangen.",
        "Goethe stand gariz und gar, man darf wohl sagen sein ganzes Leben hindurch, auf diesem Standpunkt der in der Entwickelung begriffenen Erkenntnis, auf dem Standpunkte der Einweihung, der Initiation.",
        "Gerade das zeigt uns im eminentesten Sinne sein Märchen."
      ],
      [
        "Wir werden uns am leichtesten verstehen, wenn wir von der Anschauung ausgehen, die heute am meisten und im weitesten Umkreise vertreten ist und die in einem gewissen Gegensatz zu dem Einweihungs- oder Initiations-Prinzip steht."
      ],
      [
        "Heute kann man im weitesten Umkreise diejenigen Men­schen, die über solche Sachen nachdenken oder glauben, über solche Dinge ein Urteil zu haben, mehr oder weniger bewußt den Standpunkt vertreten hören, daß über die Wahrheit, über die objektive Wirklichkeit eigentlich nur Sinnesbeobachtung oder Gegenstände der Sinnesbeobach­tung in der Vorstellung entscheiden können.",
        "Sie werden es immer wieder hören können: Wissenschaft kann nur sein, was auf der objektiven Grundlage der Beobachtung be­ruht. - Und man versteht so häufig darunter lediglich die Sinnesbeobachtung und die Anwendung des menschlichen"
      ],
      [
        "Verstandes und Vorstellungsvermögens auf diese Sinnes­beobachtung.",
        "Ein jeder von Ihnen weiß, daß die Fähigkeit, sich Vorstellungen, Begriffe zu bilden, ein menschliches Seelenvermögen ist unter anderen Seelenvermögen, und ebenso weiß ein jeder von Ihnen, daß diese anderen Seelen-vermögen unser Fühlen und unser Wollen sind."
      ],
      [
        "So kann man schon bei einer verhältnismäßig oberflächlichen Be­trachtung sagen: Der Mensch ist nicht bloß ein vorstellen-des, sondern auch ein fühlendes und wollendes Wesen. -Nun werden diejenigen, die da glauben, den reinen Stand­punkt der Wissenschaft vertreten zu müssen, immer wieder sagen: In das, was Wissenschaft ist, darf nur das Vor­stellungsvermögen hineinreden, niemals das menschliche Gefühl, niemals das, was wir als Willensimpulse kennen, denn dadurch würde das, was objektiv ist, nur verunreinigt, dadurch würde das, was in unpersönlicher Art das Vor­stellungsvermögen gewinnen könnte, nur beeinträchtigt. -Es ist richtig, daß, wenn der Mensch in das, was Gegenstand der Wissenschaft sein soll, sein Gefühl, seine Sympathie oder Antipathie hineinbringt, er die Dinge abstoßend oder ansprechend, sympathisch oder antipathisch findet.",
        "Und wohin kämen wir, wenn der Mensch sein Begehrungsver-mögen als ein Erkenntnisvermögen betrachten würde, so daß er zu den Dingen sagen könnte: Ich will es, oder: ich will es nicht. - Ob es dir mißfällt oder gefällt, ob du es be­gehrst, das ist dem Ding höchst gleichgültig."
      ],
      [
        "So wahr es ist, daß derjenige, der glaubt, auf dem festen Boden der Wissen­schaft stehen zu müssen, sich nur an die äußeren Dinge hal­ten kann, so wahr ist es, daß das Ding selber es ist, das dir abnötigt zu sagen, es sei rot, daß das, was du als eine Vor­stellung des Wesens des Steines gewinnst, richtig ist.",
        "Aber nicht liegt es im Wesen des Dinges, daß es dir häßlich oder schön erscheint, daß du es begehrst oder nicht begehrst."
      ],
      [
        "es dir rot erscheint, hat einen objektiven Grund, daß du es nicht willst, das hat keinen objektiven Grund."
      ],
      [
        "In einer gewissen Beziehung ist nun die heutige Psycho­logie eigentlich über den eben charakterisierten Standpunkt hinausgegangen.",
        "Es ist hier nicht meine Aufgabe, für oder gegen diejenige Richtung der heutigen Seelenwissenschaft oder Psychologie zu reden, die da sagt: Wenn wir die Seelenerscheinungen, das Seelenleben betrachten, dürfen wir uns nicht bloß auf den Intellektualismus beschränken, dürfen wir den Menschen nicht bloß in bezug auf die Vor­stellungsfähigkeit betrachten, sondern müssen auch die Ein­flüsse der Gefühls- und Willenswelt berücksichtigen. - Viel­leicht wissen einige von Ihnen, daß dies zum System der Wundtschen Philosophie gehört, welche den Willen als Ursprüngliches der Seelentätigkeit auffaßt.",
        "In einer in ge­wisser Beziehung grundlegenden Art, gleichgültig, ob man damit einverstanden ist oder nicht, hat der russische Psy­chologe Losskij in seinem Buche, das sich «Die Grundlegung des Intuitivismus» betitelt, auf die Willensrichtung des menschlichen Seelenlebens hingewiesen.",
        "Ich könnte Ihnen noch vieles sagen, wenn ich zeigen wollte, wie die Seelen-lehre bestrebt ist, den einseitigen Intellektualismus zu über­winden, und wenn ich Ihnen ferner zeigen wollte, daß in das, was als menschliche Seelenkraft vorhanden ist, auch die andern Kräfte hineinspielen."
      ],
      [
        "Wer weiter zu denken vermag, wird sich sagen: Daraus sehen wir, wie undurchführbar die Forderung ist, daß nur die auf die Beobachtung beschränkte Vorstellungsfähigkeit zu objektiven Resultaten der Wissenschaft führen dürfe.",
        "Wenn die Wissenschaft selbst zeigt, daß dies nicht möglich ist, daß überall Wille mitspielt, woraus wollt ihr dann fest­stellen, daß etwas rein objektive Beobachtung sei?",
        "Weil ihr dadurch, daß euer Wille euch den obenerwähnten Streich"
      ],
      [
        "spielt und ihr wegen eurer Denkgewohnheiten eine Vorliebe dafür habt, nur dasjenige, was materiell ist, als objektiv anzusehen, und weil ihr nicht die Denkgewohnheit und Gefühlsgewohnheit habt, auch das Geistige in den Dingen anzuerkennen, deshalb laßt ihr das Letztere in euren Theo­rien weg.",
        "Es kommt nicht darauf an, wenn wir die Welt begreifen wollen, was wir an abstrakten Idealen uns vor­setzen, sondern was wir in unserer Seele zuwege bringen, was wir können."
      ],
      [
        "Goethe gehört zu denjenigen Menschen, die am schärfsten den Grundsatz ablehnen, daß die Erkenntnis nur durch das einseitige Vorstellungsvermögen, nur durch das Denkver­mögen vermittelt werde.",
        "Das ist der hervorstechende, be­deutungsvolle Grundzug in Goethes Wesen, daß er, mehr oder weniger deutlich ausgesprochen, immer der Ansicht ist, daß die ganze menschliche Seele in allen ihren Kräften wirken müsse, wenn der Mensch die Weltenrätsel enträtseln will."
      ],
      [
        "Nun dürfen wir aber auch nicht einseitig und nicht un­gerecht sein.",
        "Es ist durchaus richtig, wenn in bezug auf die Erkenntnis eingewendet wird, daß Gefühl und Wille der Persönlichkeit den persönlichen Eigenschaften des Menschen unterworfene Fähigkeiten sind, und wenn gesagt wird:"
      ],
      [
        "Wohin würden wir kommen, wenn man nicht bloß das, was die Augen sehen, was das Mikroskop zeigt, sondern was das Gefühl, der Wille dem Menschen sagt, als zu den Dingen gehörig betrachten wollte!"
      ],
      [
        "Das ist es aber gerade, was wir uns sagen müssen, um jemanden zu begreifen, der wie Goethe auf dem Prinzip der Einweihung und Entwickelung steht: daß so, wie durch­schnittlich Gefühl und Wille heute im Menschen sind, sie in der Tat nicht zur Erkenntnis verwendet werden können, daß sie die Menschen nur zu einer absoluten Uneinigkeit in"
      ],
      [
        "ihrer Erkenntnis führen würden.",
        "Der eine will das, der an­dere das, je nach den subjektiven Bedürfnissen des Gefühls und Willens.",
        "Der aber, welcher auf dem Boden der Initia­tion steht, ist sich auch darüber klar, daß von den mensch­lichen Seelenkräften - Denken, Vorstellen, Fühlen und Wol­len - in der Entwickelung des gegenwärtigen Durchschnitts­menschen das Vermögen der Vorstellung, das Vermögen des Denkens eben am weitesten vorgeschritten ist, und am ehe­sten geneigt und geeignet ist, das Persönliche auszuschließen und zur Objektivität zu kommen.",
        "Denn dasjenige Seelen-vermögen, das sich im Intellektualismus auslebt, ist heute schon so weit, daß die Menschen, wenn sie sich auf dieses Seelenvermögen verlassen, am wenigsten streiten, am mei­sten einig werden über das, was sie sagen.",
        "Das ist deshalb so, weil heute die Menschen in bezug auf das Vorstellungs-und Denkvermögen weit entwickelt sind, während Gefühl und Wille noch nicht zu solcher Objektivität entwickelt werden konnten."
      ],
      [
        "Wir könnten auch, wenn wir auf dem Gebiete des Vor­stellungslebens Umschau halten, mit Recht Unterschiede finden.",
        "Es gibt weite Gebiete des Vorstellungslebens, die uns vollständig objektive Wahrheiten liefern, Wahrheiten, die die Menschen als solche erkannt haben, ganz unabhängig von der äußeren Erfahrung, wobei es ganz gleich ist, ob eine Million Menschen anders darüber urteilt.",
        "Wer die Gründe dafür in sich erlebt hat, der vermag die Wahrheit zu behaupten, auch wenn eine Million Menschen anderes meint.",
        "Jeder kann zum Beispiel bei solchen Wahrheiten, die sich auf Zahl- und Raumgrößen beziehen, das Gesagte be­stätigt finden.",
        "Daß 3 mal 3 = 9 sind, kann jeder begreifen und erleben, und es ist richtig, selbst wenn eine Million Menschen dem widersprächen.",
        "Warum ist das so der Fall?",
        "Weil in bezug auf solche Wahrheiten, wie die mathematischen"
      ],
      [
        "es sind, die meisten Menschen es dazu gebracht haben, ihre Vorliebe und Abneigung, ihre Sympathie und Anti­pathie, kurz, das Persönliche auszuschalten und nur die Sache für sich sprechen zu lassen.",
        "Man hat die Ausschaltung von allem Persönlichen in bezug auf das Denken und auf das Vorstellungsvermögen immer die Läuterung der mensch­lichen Seele genannt, und man betrachtete diese Läuterung als die erste Stufe auf dem Wege der Einweihung oder Ini­tiation, oder, wie man auch sagen könnte, auf dem Wege zur höheren Erkenntnis."
      ],
      [
        "Der Mensch, der in diesen Dingen bewandert ist, sagt sich: Nicht nur in bezug auf das Gefühl und auf den Willen sind die Menschen noch nicht so weit, daß da kein Persön­liches mehr hineinspielt, daß sie Objektivität bewahren können, sondern auch in bezug auf das Denken sind die meisten noch nicht so weit, daß sie sich an das rein hingeben könnten, was ihnen die Dinge, die Ideen der Dinge selbst sagen, so wie es alle Menschen bei den mathematischen Dingen können.",
        "Aber es gibt Methoden, das Denken so weit zu läutern, daß wir nicht mehr persönlich denken, son­dern die Gedanken in uns denken lassen, so wie wir die mathematischen Gedanken in uns denken lassen.",
        "Wenn wir also die Gedanken gereinigt haben von den Einflüssen der Persönlichkeit, dann sprechen wir von der Läuterung oder Katharsis, wie dies in den alten Eleusinischen Mysterien genannt wurde.",
        "Es muß also der Mensch dahin kommen, das Denken zu läutern, das ihm dann die Möglichkeit gibt, die Dinge gedanklich objektiv zu erfassen."
      ],
      [
        "So, wie das möglich ist, ist es nun auch möglich, aus dem Gefühl alles Persönliche auszuschalten, so daß dann auch dasjenige, was von den Dingen das Gefühl anregt, nicht mehr zur Persönlichkeit spricht, nichts mehr zu tun hat mit Person, Sympathie und Antipathie, sondern einzig und"
      ],
      [
        "allein das Wesen des Dinges aufruft, insofern es nicht zum bloßen Vorstellungsvermögen sprechen kann.",
        "Erlebnisse in unserer Seele, die in unserem Gefühlsleben wurzeln oder urständen, und die dadurch zu innerer Erkenntnis führen, daß sie tiefer in das Wesen eines Dinges hineinführen, die aber auch noch zu anderen Seiten der Seele als zum bloßen Intellektualismus sprechen, können ebenso vom Persönlichen gereinigt werden wie das Denken, so daß das Gefühl dann eben solche Objektivität vermittelt, wie sie das Denken oder das Vorstellungsvermögen vermitteln kann.",
        "Diese Reinigung oder Entwickelung des Gefühls nennt man in aller esoterischen Erkenntnislehre die Erleuchtung."
      ],
      [
        "Jeder Mensch, der entwickelungsfähig ist und nicht in beliebiger Weise, wie es in den Intentionen der Persönlich­keit liegt, seine Entwickelung anstrebt, muß sich dahin be­mühen, daß er sich nur durch das, was im Wesen des Dinges liegt, anregen läßt.",
        "Wenn er dahin gekommen ist, daß das Ding in ihm persönlich keine Sympathie oder Antipathie erweckt, daß er lediglich das Wesen der Dinge sprechen läßt, so daß er sagt: Was ich auch für Sympathien oder Anti­pathien habe, ist gleichgültig und darf nicht in Betracht kommen -, dann liegt es im Wesen des Dinges, daß das Denken und Handeln des Menschen diese oder jene Rich­tung annimmt, dann ist das eine Aussage des innersten Wesens des Dinges.",
        "In der esoterischen Erkenntnislehre hat man diese Entwickelung des Willens die Vollendung ge­nannt."
      ],
      [
        "Wenn der Mensch auf dem Boden der Geisteswissenschaft steht, so sagt er sich also: Wenn ich ein Ding vor mir habe, so lebt in diesem Ding ein Geistiges, und ich kann mein Vorstellungsvermögen so anregen, daß das Wesen der Dinge durch meine Begriffe und Vorstellungen objektiv repräsen­tiert wird.",
        "So ist gleichsam, was draußen arbeitet, in mir"
      ],
      [
        "gegenwärtig geworden, und ich habe das Wesen des Dinges durch das Vorstellungsvermögen erkannt.",
        "Aber das, was ich erkannt habe, ist nur ein Teil des Wesens.",
        "Es gibt in den Dingen etwas, das überhaupt nicht zur Vorstellung, son­dern nur zum Gefühl, und zwar zum geläuterten oder ob­jektiv gewordenen Gefühl sprechen kann. - Der, welcher nicht schon in einer solchen Kultur des Gefühls einen der­artigen Teil des Wesens in sich entwickelt hat, der kann das Wesen in dieser Richtung nicht erkennen.",
        "Für einen aber, der sich sagt, das Gefühl kann ebenso die Grundlage für die Erkenntnis geben wie das Vorstellungsvermögen"
      ],
      [
        "- das Gefühl, nicht wie es ist, sondern wie es durch wohl-begründete Methoden der Erkenntnislehre werden kann -für einen solchen wird es nach und nach klar, daß es Dinge gibt, die tiefer sind als das Vorstellungsvermögen, Dinge, die zu der seelischen Natur und zu dem Gefühl sprechen.",
        "Ebenso gibt es Dinge, die sogar bis zum Willen hinab-reichen."
      ],
      [
        "Nun war sich Goethe ganz besonders darüber klar, daß dies sich wirklich so verhält, daß der Mensch diese Ent­wickelungsmöglichkeiten hat.",
        "Er stand ganz auf dem Boden des Initiationsprinzips, und er hat uns die Einweihung des Menschen, die ihm durch die Entwickelung seiner Seele, durch die Entwickelung der drei Grundkräfte: Wille, Ge­fühl und Vorstellungsvermögen, werden kann, dadurch dargestellt, daß er in seinem Märchen die Repräsentanten dieser drei Einweihungen des Menschen auftreten läßt."
      ],
      [
        "Der goldene König ist Repräsentant der Einweihung für das Vorstellungsvermögen, der silberne König ist der Re­präsentant für die Einweihung mit dem Erkenntnisver­mögen des objektiven Gefühls, der eherne König ist der Repräsentant der Einweihung für das Erkenntnisvermögen des Willens.",
        "Goethe hat uns zu gleicher Zeit nachdrücklich"
      ],
      [
        "darauf aufmerksam gemacht, daß der Mensch erst gewisse Dinge überwinden muß, wenn er dazu kommen will, mit diesen drei Gaben begabt zu werden.",
        "Der Jüngling, den wir in der Erzählung des Märchens kennengelernt haben, ist nichts anderes als der Repräsentant des nach dem Höch­sten strebenden Menschen.",
        "So wie Schiller des Menschen Streben nach vollkommener Menschlichkeit in seinen Ästhe-tischen Briefen hinstellt, stellt uns Goethe in dem Jüngling den nach dem Höchsten strebenden Menschen dar, der zu­nächst die schöne Lilie erreichen will, der aber dann die innere menschliche Vollkommenheit dadurch erlangt, daß ihn die drei Könige, der goldene, der silberne und der erzene König, damit begaben."
      ],
      [
        "Wie das geschieht, wird in dem Gange des Märchens an­gedeutet.",
        "Erinnern Sie sich, daß in dem unterirdischen Tem­pel, in den die Schlange durch die Kristallisierungskraft der Erde blickt, in jeder der vier Ecken einer der Könige war.",
        "In der ersten war der goldene, in der zweiten der silberne, in der dritten der erzene König.",
        "In der vierten Ecke war ein König, der aus den drei Metallen gemischt war, in dem also diese drei Bestandteile so zusammengefügt sind, daß man sie nicht voneinander unterscheiden kann.",
        "In diesem vierten Könige stellt uns Goethe den Repräsentanten für diejenige menschliche Entwickelungsstufe hin, in welcher Wille, Vorstellungsvermögen und Empfindungsvermögen gemischt sind.",
        "Er ist mit andern Worten derjenige Reprä­sentant der menschlichen Seele, der von Wille, Vorstellung und Gefühl beherrscht wird, weil er selbst nicht Herr über diese drei Vermögen ist.",
        "Dagegen ist in dem Jüngling, nachdem er die Begabung von jedem der Könige im be­sonderen erlangt hat - die Begabung des Vorstellungsver­mögens, die Begabung der Gefühlserkenntnis und die Be­gabung der Willenserkenntnis, so daß sie nicht mehr chao­tisch"
      ],
      [
        "gemischt sind -, diejenige Erkenntnisstufe dargestellt, die sich nicht mehr von Vorstellung, Gefühl und Wille be­herrschen läßt, sondern über sie herrscht.",
        "Beherrscht wird der Mensch von ihnen so lange, wie sie in ihm chaotisch durcheinanderströmen, so lange sie sich in seiner Seele nicht rein, jede für sich selbst wirkend, finden."
      ],
      [
        "Solange derMensch nicht zu dieser Sonderung gekommen ist, ist er auch nicht in der Lage, durch seine drei Erkenntnisvermögen zu wirken.",
        "Ist er aber dazu gelangt, beherrscht ihn nicht mehr das Chaotische, sondern beherrscht er umgekehrt selber sein Vorstellungsvermögen, ist es so rein wie der goldene König, so daß ihm nichts anderes beigemischt ist; ist sein Gefühls­vermögen so, daß ihm nichts anderes beigemischt ist, daß es rein und lauter dasteht wie der silberne König, und ist ebenso der Wille so rein wie das Erz des erzenen Königs, so daß ihn Vorstellungen und Gefühle nicht beherrschen und er sich frei in seiner Natur darstellen kann - mit an­dern Worten, ist er fähig, wenn es sich darum handelt, durch die Vorstellung zu erfassen, oder durch das Gefühl zu er­fassen, oder durch den Willen zu erfassen, von Wille, Ge­fühl und Vorstellung einzeln Gebrauch zu machen, dann ist er so weit über sich hinausgeschritten, daß das gesamte reine Erkenntnisvermögen, das uns im Vorstellen, Fühlen und Wollen entgegentritt, ihn zu einer tieferen Einsicht führt, daß er wirklich untertaucht in den Strom des Ge­schehens, untertaucht in das, was die Dinge innerlich sind."
      ],
      [
        "Daß man so untertauchen kann, vermag natürlich nur die Erfahrung zu lehren."
      ],
      [
        "Es wird nun nicht mehr schwer sein, nachdem dieses vor­ausgeschickt worden ist, zuzugeben, daß, wenn Goethe den strebenden Menschen durch den Jüngling repräsentiert sein läßt, wir in der schönen Lilie eine andere Seelenverfassung zu sehen haben, diejenige Seelenverfassung des Menschen,"
      ],
      [
        "zu der er gelangt, wenn ihm die in den Dingen liegenden Wesenheiten in der Seele aufgehen und er sein Menschen­dasein dadurch erhöht, daß er die Dinge in sich verschmelzt mit dem Wesen der Dinge in der Außenwelt.",
        "Was da der Mensch in seiner Seele erlebt dadurch, daß er über sich hin­auswächst, daß er Herr wird über die Seelenkräfte, Sieger ist über das Chaotische in seiner Seele, das, was der Mensch da erlebt, diese innere Seligkeit, dieses Verbundensein mit den Dingen, dieses Aufgegangensein in den Dingen, wird uns von Goethe repräsentativ dargestellt in der Vereinigung mit der schönen Lilie.",
        "Schönheit ist hier nicht bloß Kunst-schönheit, sondern Eigenschaft des bis zu einem gewissen Grade vollendeten Menschen überhaupt.",
        "So daß wir jetzt auch begreiflich finden werden, warum uns Goethe darstellt, wie der Jüngling fortzieht, zur schönen Lilie hinstrebt, so daß alle Kräfte zunächst aus ihm verschwinden.",
        "Warum ist das so?"
      ],
      [
        "Wir verstehen Goethe in der Darstellung eines solchen Bildes, wenn wir an einen Gedanken, den er einst ausge­sprochen hat, anknüpfen: «Alles, was unsern Geist befreit, ohne uns die Herrschaft über uns selbst zu geben, ist ver­derblich.» Erst muß der Mensch frei werden, dahin kom­men, Herr über seine inneren Seelenkräfte zu sein, dann kann er mit wirklicher Erkenntnis zur Vereinigung mit dem höchsten Seelenzustande, mit der schönen Lilie gelangen.",
        "Wenn er es aber unvorbereitet, mit noch nicht reifen Kräf­ten erlangen will, dann nimmt ihm das seine Kräfte und wirkt ausdorrend auf seine Seele.",
        "Daher wird von Goethe darauf aufmerksam gemacht, daß der Jüngling jene Be­freiung sucht, die ihn zum Herrn über seine Seelenkräfte macht.",
        "In dem Augenblick, wo seine Seelenkräfte nicht mehr chaotisch in ihm wirken, sondern geläutert und gereinigt nebeneinanderstehen, in dem Augenblick ist er reif, jenen"
      ],
      [
        "Seelenzustand zu erreichen, der durch die Verbindung mit der schönen Lilie charakterisiert oder repräsentiert ist."
      ],
      [
        "So sehen wir, daß Goethe diese verschiedenen Gestalten in freischaffender Phantasie ausbildet, sehen, wenn wir sie als dargestellte Seelenkräfte betrachten, daß sie in seiner ganzen Seele walten und wirken.",
        "Wenn wir sie so betrach­ten, wenn wir so fühlen und empfinden, wie in gewisser Weise bezüglich dieser Gestalten Goethe gefühlt und emp­funden hat, der sich nicht damit begnügt, wie ein schlechter didaktischer Dichter zu sagen, was diese oder jene Seelen­kraft bedeutet, sondern der damit ausdrückt, was er selber empfand, dann werden wir erkennen, was sich ihm in sol­chen Dichtergestalten ausdrückt.",
        "Daher stehen die verschie­denen Gestalten in einem so persönlichen Verhältnis zuein­ander, wie die Seelenkräfte des Menschen zueinanderstehen."
      ],
      [
        "Es kann nicht scharf genug betont werden, daß es sich nicht so verhält, daß die Gestalten dies oder jenes bedeuten.",
        "Das ist durchaus nicht der Fall.",
        "Es ist vielmehr so, daß Goethe bei dieser oder jener Seelenkraft dies oder jenes fühlt, und daß sich sein Fühlen dann zu dieser oder jener Gestalt wandelt.Damit schuf er den Vorgang des Märchens, der noch wichtiger ist als die Figuren selbst.",
        "So sehen wir die Irrlichter und die grüne Schlange.",
        "Wir sehen, daß die Irrlichter vom jenseitigen Ufer des Flusses herüberkommen und ganz merkwürdige Eigenschaften zeigen.",
        "Sie nehmen das Gold begierig in sich auf, lecken es sogar von den Wän­den der Stube des Alten und werfen damit in verschwende­rischer Weise um sich.",
        "Dasselbe Gold, das also in den Irr-lichtern unter dem Zeichen einer Wertlosigkeit steht, die uns auch dadurch angedeutet wird, daß der Fährmann das Gold zurückweisen muß, weil der Fluß sich aufbäumen würde und nur Früchte in Zahlung nehmen darf, dieses Gold, was bewirkt es im Körper der grünen Schlange?"
      ],
      [
        "Schlange wird, nachdem sie es aufnahm, innerlich leuchtend!",
        "Und das, was an Pflanzen und anderen Dingen um sie her­um ist, wird auch dadurch erleuchtet, daß sie das, was bei den Irrlichtern im Zeichen der Wertlosigkeit steht, in sich aufnimmt.",
        "Aber auch den Irrlichtern wird eine gewisse Wichtigkeit zugeschrieben.",
        "Sie wissen, daß der Alte in ent­scheidender Stunde gerade die Irrlichter auffordert, die Pforte des Tempels zu öffnen, so daß der ganze Zug sich nun in den Tempel hineinbegeben kann."
      ],
      [
        "Genau dasselbe Ereignis, das sich hier mit der grünen Schlange vollzieht, findet sich als Erlebnis in der mensch­lichen Seele, ein Erlebnis, das uns besonders stark in einer solchen Denkweise hat entgegentreten können, wie wir sie vorgestern durch das Gespräch zwischen Goethe und Schiller konstatiert haben.",
        "Wir haben gesehen, daß Schiller in dem Augenblick, als er mit Goethe über die Art der Natur-betrachtung sprach, noch der Meinung war, daß das, was Goethe mit ein paar Strichen als Urpflanze hinzeichnete, eine Idee, etwas Abstraktes sei, das man erhalte, wenn man die unterscheidenden Merkmale wegläßt und das Gemein­same zusammenfügt.",
        "Und wir haben gesehen, daß Goethe darauf sagte: Wenn das eine Idee ist, dann sehe ich meine Ideen mit Augen!",
        "In diesem Moment standen sich zwei ganz verschiedene Wirklichkeiten gegenüber.",
        "Schiller hat sich wirklich ganz zu Goethes Anschauungsweise hinaufgearbei­tet, so daß man sich in der Schillerverehrung nichts vergibt, wenn man ihn als Beispiel anführt für jenes menschliche Seelenvermögen, das in Abstraktionen schwebt und vor­zugsweise in den mit dem bloßen Verstande erfaßten Vor­stellungen der Dinge lebt.",
        "Das ist eine besondere Seelen-anlage, die, wenn der Mensch zu einer höheren Entwicke­lung gelangen will, unter Umständen eine recht böse Rolle spielen kann."
      ],
      [
        "Es gibt Menschen, die vorzugsweise in der Richtung zum Abstrakten veranlagt sind.",
        "Wenn sie nun die Abstraktheit verbinden mit etwas, was ihnen da als Seelenkraft entgegen­tritt, so ist das in der Regel der Begriff der Unproduktivität.",
        "Diese Menschen sind manchmal sehr scharfsinnig, können scharfe Unterscheidungen ausführen, diesen oder jenen Be­griff wunderbar verbinden.",
        "Aber gerade eine solche Seelen-stimmung ist oft auch damit verknüpft, daß die geistigen Einflüsse, die Inspirationen, keinen Eingang finden."
      ],
      [
        "Diese Seelenverfassung, die durch Unproduktivität und Abstraktheit gekennzeichnet ist, wird uns in den Irrlichtern reprasentiert.",
        "Sie nehmen das Gold auf, wo sie es finden; sie sind frei von aller Erfindungsgabe, sind unproduktiv, können keine Ideen fassen.",
        "Diesen Ideen stehen sie fremd gegenüber.",
        "Sie haben nicht den Willen, sich selbstlos den Dingen hinzugeben, an die Tatsachen sich zu halten und Begriffe nur soweit zu benutzen, als sie Dolmetscher für die Tatsachen sind.",
        "Ihnen kommt es darauf an, ihren Verstand mit Begriffen vollzupfropfen und diese dann wieder in ver­schwenderischer Weise fortzugeben.",
        "Sie gleichen einem Men­schen, der sich in Bibliotheken setzt, die Weisheit da sam­melt, in sich aufnimmt und wieder in entsprechender Weise von sich gibt.",
        "Diese Irrlichter sind charakteristisch für das­jenige Seelenvermögen, das niemals imstande ist, einen ein­zigen literarischen Gedanken oder Empfindungsgehalt zu fassen, das aber sehr wohl das, was einmal da ist als Lite­raturgeschichte, das, was produktive Geister geleistet haben, in schöne Formen zu fassen vermag.",
        "Es soll hier nichts gegen dieses Seelenvermögen gesprochen werden.",
        "Hätte der Mensch dieses Seelenvermögen nicht oder pflegte er es nicht, wenn es ihm in zu geringem Maße zuteil geworden ist, so würde ihm etwas fehlen, was in bezug auf die wirkliche Er­kenntnisfähigkeit notwendig vorhanden sein muß.",
        "Goethe"
      ],
      [
        "stellt durch das Bild der Irrlichter, durch die ganzen Ver­hältnisse, in denen er sie auftreten und wirken läßt, die Art und Weise dar, wie ein solches Seelenvermögen im Verhält­nis zu den anderen Seelenvermögen arbeitet, wie es schadet und nützt.",
        "Wahrhaftig, wenn jemand dieses Seelenvermögen nicht hätte und zu höheren Stufen der Erkenntnis aufstei­gen wollte, dann würde nichts da sein, was ihm den Tempel aufschließen könnte.",
        "Goethe stellt ebenso die Vorzüge wie auf der anderen Seite die Nachteile dieses Seelenvermögens hin.",
        "Das, was in den Irrlichtern gegeben ist, stellt eben ein Seelenelement dar.",
        "In dem Augenblick, wo es nach der einen oder andern Seite hin ein selbständiges Leben führen will, wird es schädlich.",
        "Es wird aus dieser Abstraktheit ein kriti­sches Vermögen, das die Menschen so gestaltet, daß sie zwar alles lernen, sich aber nicht weiterentwickeln können, weil ihnen das produktive Element fehlt.",
        "Goethe zeigt aber ganz klar, inwiefern auch ein Wertvolles in dem ist, was in den Irrlichtern dargestellt wird.",
        "Das, was sie in sich haben, kann auch etwas Wertvolles werden: in der Schlange wird das Gold der Irrlichter zu etwas Wertvollem, insofern es die Gegenstände, welche um die Schlange herum sind, be­leuchtet."
      ],
      [
        "Was in den Irrlichtern lebt, wird, wenn es in anderer Weise verarbeitet wird, in der menschlichen Seele äußerst fruchtbar werden.",
        "Wenn der Mensch sich bestrebt, das, was er in Begriffen, Ideen und idealen Gebilden erleben kann, nicht für sich als ein Abstraktes hinzustellen, sondern es so zu betrachten, daß es ihm Führer und Dolmetscher wird für das, was an Realitäten um ihn herum ist, so daß er sich ebensogern und hingebungsvoll an die Beobachtungen hält wie an die Abstraktheit der Begriffe, dann ist er mit dieser Seelenkraft in dem gleichen Falle wie die grüne Schlange.",
        "Dann kann er aus dem bloß Abstrakten, aus den bloßen"
      ],
      [
        "Begriffen Licht und Weisheit gestalten.",
        "Dann führt sie ihn nicht dazu, daß er zur vertikalen Linie wird, die alle Ver­bindung und Beziehung zur Fläche verliert.",
        "Die Irrlichter sind die Verwandten der Schlange, sie sind aber von der vertikalen Linie.",
        "Die Goldstücke fallen zwischen die Felsen hinein, die Schlange nimmt sie auf und wird dadurch inner­lich leuchtend.",
        "Die Weisheit nimmt der auf, der mit diesen Begriffen an die Dinge selbst herangeht."
      ],
      [
        "Goethe gibt uns auch ein Beispiel, wie man an den Be­griffen arbeiten soll.",
        "Goethe hat den Begriff der Urpflanze.",
        "Was ist er zunächst?",
        "Ein abstrakter Begriff.",
        "Würde er ihn abstrakt ausbilden, so würde er ein leeres Gebilde werden, das alles Lebendige tötet, wie das hingeworfene Gold der Irrlichter den Mops tötet.",
        "Denken Sie sich aber, was Goethe mit dem Begriffe der Urpflanze tut.",
        "Verfolgen wir ihn auf seiner italienischen Reise, dann sehen wir, wie dieser Begriff nur das Leitmotiv ist, um von Pflanze zu Pflanze, von Wesen zu Wesen zu gehen.",
        "Er nimmt den Begriff, geht von ihm aus zur Pflanze über und sieht, wie sie sich in dieser oder jener Form ausgestaltet, wie sie ganz andere Formen annimmt in niederer oder höherer Gegend und so weiter.",
        "Nun verfolgt er von Stufe zu Stufe, wie die geistige Realität oder Gestalt in jede sinnliche Gestak hineinkriecht.",
        "Er selbst kriecht da herum wie die Schlange in den Klüften der Erde.",
        "So ist für Goethe die Begriffswelt nichts anderes als das, was sich in die objektive Wirklichkeit hineinspinnen läßt.",
        "Die Schlange ist ihm der Repräsentant der Seelenkraft, die nicht in egoistischer Weise hinaufstrebt zu den höheren Gebieten des Daseins und sich über alles zu erheben ver­sucht, sondern die geduldig den Begriff durch die Beobach­tung fortwährend bewahrheiten läßt, die geduldig von Er­fahrung zu Erfahrung, von Erlebnis zu Erlebnis geht."
      ],
      [
        "Wenn der Mensch nicht bloß theoretisiert, nicht bloß in"
      ],
      [
        "den Begriffen lebt, sondern sie auf das Leben, auf die Er­fahrung anwendet, dann ist er mit dieser Seelenkraft in der Lage der Schlange.",
        "Das ist in ganz umfassendem Sinne rich­tig.",
        "Wer die Philosophie nicht wie eine Theorie aufnimmt, sondern als das, was sie sein soll, wer die geisteswissen­schaftlichen Begriffe als Aufgaben für das Leben betrachtet, der weiß, daß gerade Begriffe, und seien sie auch die höch­sten, so verwendet werden sollen, daß sie in das Leben ein­fließen und an den täglichen Erlebnissen sich bewahrheiten können.",
        "Für den, der ein paar Begriffe gelernt hat, sie aber nicht ins Leben übertragen kann, liegt ein ähnliches Ver­hältnis vor wie für den, der ein Kochbuch auswendig gelernt hat, aber doch nicht kochen kann.",
        "So wie das Gold ein Mit­tel ist, die Dinge zu beleuchten, so beleuchtet Goethe durch seine Begriffe die Dinge, welche um ihn herum sind."
      ],
      [
        "Das ist das Belehrende und Großartige an Goethes Wis­senschaftlichkeit und allem Goetheschen Streben, daß das, was er an Begriffen und Ideen gibt, Realität hat, daß es wirkt wie ein Licht, leuchtend wird und die Gegenstände um ihn herum beleuchtet.",
        "Das vorgestern hervorgehobene Universale bei Goethe macht es, daß wir, wenn wir an ihn herantreten, nie das Gefühl haben, das ist Goethes «Mei­nung».",
        "Er steht da und wenn wir ihn sehen, finden wir nur, daß wir die Dinge besser begreifen, die uns vorher nicht so begreiflich waren.",
        "Dadurch eben konnte er zum Vereini­gungspunkt feindlicher Brüder werden, wie wir vorgestern gesehen haben.",
        "Wollten wir jeden Zug in dem Märchen be­sprechen, jede Gestalt charakterisieren, dann müßte ich über dieses Märchen nicht drei Stunden, sondern drei Wochen sprechen.",
        "Ich kann also nur die tieferen Prinzipien in die­sem Märchen angeben.",
        "Jeder Zug aber weist uns in Goethes Vorstellungsart und Goethes Weltgesinnung hinein."
      ],
      [
        "Diejenigen Seelenkräfte, welche in den Irrlichtern, in der"
      ],
      [
        "grünen Schlange und in den Königen dargestellt sind, be­finden sich auf der einen Seite des Flusses.",
        "Drüben auf der andern Seite wohnt die schöne Lilie, das Ideal vollkomme­ner Erkenntnis und vollkommenen Lebens und Schaffens.",
        "Von dem Fährmann haben wir gehört, daß er die Gestalten von dem jenseitigen Ufer herüberführen kann, aber nie­mand wieder zurückführen darf.",
        "Wenden wir das auf unsere ganze Seelenstimmung und Veredlung an."
      ],
      [
        "Wir Menschen finden uns als seelische Wesenheiten hier auf der Erde.",
        "Diese oder jene Seelenkräfte arbeiten an uns als Anlagen, als mehr oder weniger ausgebildete Seelen-kräfte.",
        "Sie sind in uns.",
        "Es lebt aber in uns auch noch etwas anderes.",
        "In uns Menschen, wenn wir uns selbst richtig er­fassen, lebt das Gefühl, die Erkenntnis, daß die Seelen-kräfte in uns, welche uns das Wesen der Dinge zuletzt ver­mitteln, mit den Grundgeistern der Welt, mit den schöpfe­rischen, geistigen Mächten innig verwandt sind.",
        "Indem wir uns nach diesen schöpferischen Mächten sehnen, sehnen wir uns nach der schönen Lilie.",
        "So wissen wir, daß alles, was einerseits von der schönen Lilie herstammt, andererseits wieder zu ihr zurückzukehren strebt.",
        "Unbekannte Kräfte, die wir nicht meistern, haben uns herübergebracht.",
        "Wir wis­sen, daß gewisse Kräfte uns von der jenseitigen Welt über den Grenz fluß zur diesseitigen Welt herübergebracht haben.",
        "Diese durch den Fährmann charakterisierten, in den Tiefen der unbewußten Natur wirkenden Kräfte können aber uns nicht wieder zurückbringen, denn sonst würde der Mensch ohne seine Arbeit, ohne sein Zutun, genau ebenso wieder in das Reich des Göttlichen zurückkehren, wie er herüber­gekommen ist.",
        "Die Kräfte, die uns als unbewußte Natur­kräfte herübergefahren haben in das Reich der strebenden Menschen, dürfen uns nicht wieder zurückführen.",
        "Dazu sind andere Kräfte nötig.",
        "Das weiß auch Goethe.",
        "Goethe will"
      ],
      [
        "aber auch zeigen, wie der Mensch es anfangen muß, daß er sich mit der schönen Lilie wieder vereinigen kann."
      ],
      [
        "Zwei Wege gibt es.",
        "Der eine geht über die grüne Schlange, über sie konnen wir hinübergehen, da finden wir nach und nach das Reich des Geistes.",
        "Der andere Weg geht über den Schatten des Riesen.",
        "Es wird uns dargestellt, daß der Riese, der sonst ganz kraftlos ist, in der Dämmerstunde seine Hand ausstreckt, deren Schatten sich dann über den Fluß legt.",
        "Über diesen Schatten führt der zweite Weg.",
        "Wer also bei hellem Tageslicht hinüber will in das Reich des Geistes, muß sich des Weges bedienen, den die Schlange vermittelt, wer im Dämmerlichte hinüberkominen will, der kann sich des Weges bedienen, der über den Schatten des Riesen führt.",
        "Das sind die zwei Wege, um zu einem geistigen Weltenbilde zu kommen.",
        "Derjenige, der nicht mit menschlichen Begrif­fen, menschlichen Ideen, nicht mit denjenigen Mächten, die durch das wertlose Gold, bei bloß sophistischen Geistern, und durch die Irrlichter charakterisiert werden, die geistige Welt erstrebt, sondern in Geduld und Selbstlosigkeit von Erlebnis zu Erlebnis geht, gelangt beim hellen Sonnenschein zum jenseitigen Ufer."
      ],
      [
        "Goethe weiß, daß wirkliche Forschung nicht am Mate­riellen kleben bleibt, sondern herüberführen muß über die Grenze, über den Fluß, der uns von dem Geistigen trennt.",
        "Es gibt aber noch einen andern Weg, einen Weg für unent­wickeltere Menschen, die nicht den Weg des Erkennens, nicht den Erkenntnispfad gehen wollen, einen Weg, der repräsentiert wird durch den Riesen.",
        "Kraftlos ist dieser Riese, nur sein Schatten hat eine gewisse Kraft.",
        "Was ist nun im echten Sinne kraftlos?",
        "Nehmen Sie alle Zustände, in die der Mensch kommen kann bei herabgestimmtem Bewußt­sein, wie beim Hypnotismus, Somnambulismus, ja selbst bei Traumzuständen: alles das, wodurch das helle Tagesbewußtsein"
      ],
      [
        "herabgedämmert wird, wodurch der Mensch niedrigere Seelenkräfte als das helle Tagesbewußtsein in sich wirken läßt, gehört zu diesem zweiten Weg.",
        "Da wird die Seele beim Kraftloswerden der alltäglichen Seelenkraft ins wirk­liche Reich des Geistes hinübergeführt.",
        "Die Seele wird aber nicht selbst fähig, in das geistige Reich hinüberzugehen, sondern sie bleibt bewußtlos und wird wie der Schatten in das Reich des Geistes hinübergeführt.",
        "Goethe nimmt noch alles das, was unbewußt, gewohnheitsmäßig wirkt, ohne daß die Seelenkräfte, die bei hellem Tagesbewußts ein wirk­sam werden, daran beteiligt sind, unter die Kräfte, welche in dem Schatten des Riesen vorzustellen sind.",
        "Schiller, der in das, was Goethe meinte, eingeweiht war, schrieb zur Zeit der großen Stürme im westlichen Europa einmal an Goethe:"
      ],
      [
        "Froh bin ich, daß Sie von dem Schatten des Riesen nicht unsanft angefaßt worden sind. - Was meint Schiller damit?",
        "Er meinte, wenn Goethe weiter nach Westen gewandert wäre, so würde er von den revolutionären Mächten des Westens erfaßt worden sein."
      ],
      [
        "Dann sehen wir, daß das, was der Mensch als Hochstand der Erkenntnisentwickelung erlangen soll, in dem Tempel dargestellt wird.",
        "Der Tempel bedeutet also einen höheren Entwicklungsstand des Menschen.",
        "In der jetzigen Zeit, würde Goethe sagen, ist der Tempel etwas Verborgenes, ist er unter den engen Klüften der Erde.",
        "Eine solche strebende Seelenkraft, wie sie durch die Schlange repräsentiert wird, kann nur undeutlich die Gestalt des Tempels fühlen.",
        "Da­durch, daß sie Ideale, das Gold in sich aufnimmt, kann sie diese Gestak erleuchten, aber im Grunde genommen kann dieser Tempel in der jetzigen Zeit nur als ein unterirdisches Geheimnis da sein.",
        "Dadurch, daß Goethe diesen Tempel für die äußere Kultur etwas Unterirdisches sein läßt, weist er aber auch darauf hin, daß dieses Geheimnis einem weiterentwickelten"
      ],
      [
        "Menschen erschlossen werden muß.",
        "Er weist damit auf die geisteswissenschaftliche Strömung hin, die heute schon breite Menschenmassen erfaßt hat, die in um­fassendem Sinne populär zu machen sucht, was der Inhalt der Geisteswissenschaft, der Initiation oder des Einweihungs­prinzips, der Jnhalt der Tempelgeheimnisse ist."
      ],
      [
        "In diesem echt freien Goetheschen Sinne ist daher der Jüngling als Repräsentant der strebenden Menschheit zu betrachten.",
        "Daher soll sich der Tempel über den Fluß er­heben, damit nicht nur einzelne wenige, welche Erleuchtung suchen, herüber und hinüber gehen können, sondern damit dann alle Menschen auf der Brücke den Fluß passieren kön­nen.",
        "Einen Zukunftszustand stellte Goethe hin in dem Initiations-Tempel über der Erde, der da sein wird, wenn der Mensch aus dem Reiche des Sinnlichen in das Reich des Geistigen und aus dem Reiche des Geistigen in das Reich des Sinnlichen gehen kann."
      ],
      [
        "Wodurch ist das in dem Märchen erreicht worden?",
        "Da­durch, daß das eigentliche Geheimnis des Märchens erfüllt ist.",
        "Die Lösung des Märchens steht im Märchen selber, sagt Schiller.",
        "Er hat aber auch darauf hingewiesen, daß recht sonderbar das Wort der Lösung darinnen steht.",
        "Sie erinnern sich des Alten mit der Lampe, die nur leuchtet, wo schon Licht ist.",
        "Wer ist nun der Alte?",
        "Was ist diese Lampe?",
        "Was hat sie für ein eigenartiges Licht?",
        "Der Alte steht über der Situation.",
        "Seine Lampe hat die merkwürdige Eigenschaft, daß sie die Dinge verwandelt, Holz in Silber, Stein in Gold.",
        "Sie hat auch die Eigenschaft, daß sie nur da leuchtet, wo schon eine Empfänglichkeit, eine bestimmte Art des Lichtes vorhanden ist.",
        "Als der Alte in den unterirdischen Tempel hineintritt, wird gefragt, wieviel Geheimnisse er kenne.",
        "«Drei», versetzt der Alte.",
        "Auf die Frage des silbernen Königs: «Welches ist das wichtigste?», antwortet er: «Das"
      ],
      [
        "offenbare.» Und auf die Frage des ehernen Königs: «Willst du es auch uns eröffnen?», sagt er: «Sobald ich das vierte weiß.» Darauf zischelt die Schlange dem Alten etwas ins Ohr, worauf er sagt: «Es ist an der Zeit!»"
      ],
      [
        "Das, was die Schlange dem Alten ins Ohr sagte, das ist die Lösung des Rätsels, und wir haben zu erforschen, was die Schlange dem Alten ins Ohr gesagt hat.",
        "Es würde zu weit führen, ausführlich zu sagen, was die drei Geheimnisse bedeuten.",
        "Nur andeuten will ich es."
      ],
      [
        "Es gibt drei Reiche, die in der Entwickelung heute sozu­sagen stationär sind: das Mineral-, das Pflanzen- und das Tierreich, die dem Menschen gegenüber, der sich noch in weiterer Entwickelung befindet, abgeschlossen sind.",
        "Die innere Entwickelung, die der Mensch durchmacht, ist so vehement und bedeutsam, daß sie sich mit der Entwickelung der anderen drei Naturreiche nicht vergleichen läßt.",
        "Daß ein Naturreich dadurch zu dem gegenwärtigen Stande ge­kommen ist, daß es zu einem Abschluß gelangt ist, das ist es, was in dem Geheimnis des Alten liegt, das ist es, was die Gesetze des Mineral-, Pflanzen- und Tierreichs erklärt.",
        "Aber nun kommt das vierte Reich, das Reich des Menschen, das Geheimnis, das in der Seele des Menschen offenbar werden soll.",
        "Dieses Geheimnis ist ein solches, das der Alte erst er­fahren muß.",
        "Und wie muß er es erfahren?",
        "Er weiß, worin es besteht, aber die Schlange muß es ihm erst sagen.",
        "Das deutet uns an, daß mit dem Menschen noch etwas Beson­deres vorgehen muß, wenn er ebenso das Ziel der Ent­wickelung erreichen will, wie die anderen drei Reiche es erreicht haben.",
        "Was mit dem Menschen im Innersten seiner Seele geschehen ist, und was geschehen muß, wenn er das Ziel erreichen soll, das sagt die Schlange dem Alten ins Ohr.",
        "Sie sagt, wie eine bestimmte Seelenkraft sich entwickeln muß, wenn eine höhere Stufe erreicht werden soll, sie sagt,"
      ],
      [
        "daß sie den Willen habe, sich dafür aufzuopfern, und sie opfert sich auf.",
        "Bisher hat sie nur eineBrücke gebildet, wenn hie und da ein einzelner Mensch hinübergehen wollte; nun aber wird sie zu einer dauernden Brücke werden, indem sie zerfällt, so daß der Mensch eine dauernde Verbindung haben wird zwischen dem Diesseits und Jenseits, zwischen Geistigem und Sinnlichem."
      ],
      [
        "Daß die Schlange den Willen zur Aufopferung hat, das ist es, was als die Bedingung für die Eröffnung des vierten Geheimnisses angesehen werden muß.",
        "In dem Augenblick, wo der Alte hört, daß die Schlange sich opfern will, kann er dann auch sagen: «Es ist an der Zeit!» Es ist die Seelen-kraft, die an das Äußere sich hält.",
        "Und der Weg muß da­durch betreten werden, daß diese Seelenkraft und innere Wissenschaft nicht Selbstzweck wird, sondern sich hinopfert.",
        "Das ist wirklich ein Geheimnis, wenn es auch als ein «offen­bares» Geheimnis angesprochen wird, das heißt, wenn es auch jedem, der es will, offenbar werden kann."
      ],
      [
        "Was in weitem Umkreis als Selbstzweck angesehen wird"
      ],
      [
        "- alles, was wir lernen können in der Naturwissenschaft, in der Kulturwissenschaft, in der Geschichte, in der Mathema­tik und allen anderen Wissenschaften -, es kann niemals Selbstzweck sein.",
        "Wir können niemals zur wahren Einsicht in die Tiefen der Welt kommen, wenn wir sie als etwas für sich betrachten.",
        "Erst wenn wir jederzeit bereit sind, sie in uns aufzunehmen und als Mittel zu betrachten, das wir hinopfern als Brücke, über die wir hinüberschreiten können, dann kommen wir zur wirklichen Erkenntnis.",
        "Wir sperren uns ab von der höheren, von der wirklichen Erkenntnis, wenn wir nicht auch bereit sind, uns hinzuopfern.",
        "Erst dann wird der Mensch einen Begriff bekommen von dem, was Einweihung ist, wenn er aufhört, sich aus äußerlich-sinnlichen Begriffen eine Weltanschauung zu zimmern."
      ],
      [
        "muß ganz Gefühl, ganz Seelenstimmung werden, eine solche Seelenstimmung, die dem entspricht, was Goethe als höchste Errungenschaft des Menschen in seinem «Westöstlichen Divan» charakterisiert:"
      ],
      [
        "Und so lang du das nicht hast,"
      ],
      [
        "Dieses: Stirb und Werde!"
      ],
      [
        "Bist du nur ein trüber Gast"
      ],
      [
        "Auf der dunklen Erde."
      ],
      [
        "Stirb und Werde!",
        "Lerne kennen, was das Leben bieten kann, gehe hindurch, aber überwinde, gehe über dich hin­aus.",
        "Laß es dir zur Brücke werden, und du wirst in einem höheren Leben aufleben, mit dem Wesen der Dinge eines sein, wenn du nicht mehr in dem Wahne lebst, daß du, ge­trennt von dem höheren Ich, das Wesen der Dinge erschöp­fen kannst.",
        "Goethe erinnert sich gern, da, wo er von der Hinopferung des Begriffes und des Seelenmaterials spricht, um in höheren Sphären aufzuleben, wo er von der tiefsten innersten Liebe spricht, an die Worte des Mystikers Jakob Böhme, der dieses Erlebnis der Hinopferung der Schlange in sich kennt.",
        "Jakob Böhme hat ihn vielleicht gerade darauf hingewiesen und bewirkt, daß es ihm so klar war, daß der Mensch schon im physischen Leibe hinüberleben kann in eine Welt, die er sonst erst nach dem Tode betritt: in die Welt des Ewigen, des Geistigen.",
        "Jakob Böhme wußte auch, daß es von dem Menschen abhängt, ob er in höherem Sinne in die geistige Welt hinübergleiten kann.",
        "Er zeigt es in dem Spruche: Wer nicht stirbt, eh' er stirbt, der verdirbt, wenn er stirbt. - Ein bedeutsames Wort!",
        "Der Mensch, der nicht stirbt, bevor er stirbt, das heißt, der nicht das Ewige, den inneren Wesenskern in sich entwickelt, der wird auch nicht in der Lage sein, wenn er stirbt, den geistigen Wesenskern in sich wiederzufinden.",
        "Das Ewige ist in uns.",
        "Wir müssen es"
      ],
      [
        "im Leibe entwickeln, damit wir es außer dem Leibe finden können.",
        "«Wer nicht stirbt, eh' er stirbt, der verdirbt, wenn er stirbt.» So ist es auch mit dem andern Satze: «Und so ist der Tod die Wurzel alles Lebens.»"
      ],
      [
        "Sodann sehen wir, daß das Seelische nur da erleuchten kann, wo schon Licht ist: die Lampe des Alten kann nur das erleuchten, was schon erleuchtet ist.",
        "Wieder werden wir auf Seelenkräfte des Menschen hingewiesen, auf jene Seelen-kräfte, die als etwas Besonderes uns entgegentreten, die Seelenkräfte der Devotion, der religiösen Hingabe, die durch Jahrhunderte und Jahrtausende hindurch den Men­schen die Botschaft von geistigen Welten gebracht haben, denen, die das Licht nicht auf dem Wege der Wissenschaft oder sonstwie suchen konnten.",
        "Das Licht der verschiedenen religiösen Offenbarungen wird dargestellt in dem Alten, der dieses Licht hat.",
        "Wer aber nicht von innen heraus dem religiösen Sinn ein Licht entgegenbringt, dem leuchtet nicht die Lampe der Religion.",
        "Nur da kann sie leuchten, wo ihr schon Licht entgegenkommt.",
        "Sie ist es gewesen, die die Menschen verwandelt hat, die alles Tote in das beseelte Lebendige hinübergeführt hat."
      ],
      [
        "Und dann sehen wir, daß durch die Hinopferung der Schlange die beiden Reiche miteinander vereinigt werden.",
        "Nachdem sie sozusagen durch symbolische Vorgänge durch-macht, was der Mensch bei seiner Höherentwickelung im esoterischen Sinne durchzumachen hat, sehen wir, wie der Tempel der Erkenntnis durch alle drei menschlichen Seelen-kräfte hinaufgeführt wird über den Fluß, wie er hinauf-wandert und wie jede Seelenkraft ihren Dienst verrichtet.",
        "Es wird da angedeutet, daß die Seelenkräfte in Harmonie zusammenklingen müssen, indem uns gesagt wird: Die ein­zelne Persönlichkeit vermag nichts; wenn aber alle zur guten Stunde zusammenwirken, wenn die Gewaltigen und"
      ],
      [
        "die Geringen im richtigen Verhältnis zueinander wirken, dann kann erstehen, was die Seele befähigt, den höchsten Zustand zu erreichen, die Vereinigung mit der schönen Lilie."
      ],
      [
        "Dann wandert aber auch der Tempel aus den verborgenen Klüften hinauf an die Oberfläche für alle, die in Wahrheit nach Erkenntnis und Weisheit streben.",
        "Der Jüngling wird begabt mit den Erkenntniskräften des Denkens und Vor­stellens durch den goldenen König: «Erkenne das Höchste.» Er wird begabt mit den Erkenntniskräften des Gefühls durch den silbernen König, was Goethe so schön andeutet mit den Worten: «Weide die Schafe!» Im Fühlen wurzeln Kunst und Religion, und für Goethe war beides eine Ein­heit, schon damals, als er von seiner italienischen Reise über die Kunstwerke Italiens schrieb: «Da ist Notwendigkeit, da ist Gott!»"
      ],
      [
        "Aber da ist auch die Tat - wenn der Mensch sie nicht zum Daseinskampf verwendet, wenn sie ihm zur Waffe wird, um Schönheit und Weisheit zu erkämpfen.",
        "Das ist in den Worten enthalten, die der eherne König zu dem Jüngling spricht: «Das Schwert an der Linken, die Rechte frei!» Darin liegt eine ganze Welt.",
        "Die Rechte frei zum Wirken aus der menschlichen Natur des Selbst heraus."
      ],
      [
        "Und was geschieht mit dem vierten König, in dem alle drei Elemente durcheinandergemischt sind?",
        "Dieser gemischte König schmilzt zu einer grotesken Figur zusammen.",
        "Die Irrlichter kommen und lecken das noch vorhandene Gold aus ihm heraus.",
        "Die Seelenkräfte des Menschen wollen da noch studieren, was an menschlichen Entwicklungsstufen, die schon überwunden sind, einst vorhanden war."
      ],
      [
        "Nehmen wir noch einen Zug, nämlich den, wie der Riese da taumelnd einherkommt und dann wie eine Bildsäule dasteht und die Stunden anzeigt: Wenn der Mensch sein"
      ],
      [
        "Leben in Harmonie gebracht hat, dann hat auch das Unter­geordnete Bedeutung für das, was methodische Ordnung sein soll.",
        "Das soll sich wie eine Gewohnheit ausprägen.",
        "Selbst das Unbewußte wird dann einen wertvollen Sinn erhalten.",
        "Deshalb wird der Riese gleichsam wie eine Uhr dargestellt."
      ],
      [
        "Der Alte mit der Lampe ist vermählt mit der Alten.",
        "Diese Alte stellt uns nichts anderes dar als die gesunde ver­ständige menschliche Seelenkraft, die nicht in hohe Regio­nen geistiger Abstraktion eindringt, die aber alles gesund und praktisch angreift, wie zum Beispiel in der Religion, die ja in dem Alten mit der Lampe dargestellt wird.",
        "Ge­rade sie kann dann auch dem Fährmann die Löhnung bringen: drei Kohlhäupter, drei Zwiebeln und drei Arti­schocken.",
        "Eine solche Entwickelungsstufe ist noch nicht über die Zeitlichkeit hinweggekommen.",
        "Daß sie so behandelt wird, wie es von den Irrlichtern geschieht, ist wohl ein Abbild davon, wie abstrakte Geister meistens hochmutig auf Menschen herunterschauen, die aus unmittelbaren In­stinkten oder Intuitionen heraus die Dinge erfassen. ."
      ],
      [
        "Jeder Zug, jede Wendung in diesem Märchen ist von tiefgründiger Bedeutung, und tritt man noch in eine Er­klärung ein, die esoterisch sein soll, dann findet man, daß man eigentlich nur die Methode der Erklärung anzugeben vermag.",
        "Vertiefen Sie sich in das Märchen selber, dann werden Sie finden, daß eine ganze Welt darinnen zu finden ist, weit mehr, als heute angedeutet werden konnte."
      ],
      [
        "Wie sehr Goethes geistige Weltanschauung sein ganzes Leben durchzieht, wie in den Dingen der Geisteserkenntnis er noch im spätesten Alter in Einklang steht mit früher Ge­schaffenem, das möchte ich Ihnen noch an zwei Beispielen zeigen.",
        "Als Goethe den «Faust» schrieb, hatte er eine ge-wisse Vorstellung übernommen, die auf ein Symbolum eines"
      ],
      [
        "tieferen Entwickelungsweges der Natur zurückgeht.",
        "Als Faust von seinem Vater spricht, der Alchimist war und die alten Lehren gläubig hingenommen, aber schon damals mißverstanden hatte, sagt er, daß sein Vater auch das ge-macht habe, daß sich"
      ],
      [
        ". . . ein roter Leu, ein kühner Freier,"
      ],
      [
        "Im lauen Bad der Lilie vermählt."
      ],
      [
        "Das sagt Faust, ohne daß er die Bedeutung davon kennt.",
        "Solch ein Wort aber kann zur Leiter werden, die auf hohe Entwickelungsstufen hinaufführt.",
        "Goethe zeigt in dem Märchen den nach der höchsten Braut strebenden Menschen in seinem Jüngling, und das, womit er vereinigt werden soll, nennt er die schöne Lilie.",
        "Sie sehen, diese Lilie finden Sie auch schon in den ersten Partien des «Faust».",
        "Und auch das, was als Grundnerv der Goetheschen Anschauung sei­nen Ausdruck im Märchen gefunden hat, finden wir im «Faust», im zweiten Teile, im Chorus mysticus, da, wo Faust vor dem Eintritt in die geistige Welt steht, wo Goethe sein Bekenntnis zur geistigen Weltanschauung mit monumenta­len Worten ablegt.",
        "Er zeigt da, wie in drei aufeinander­folgenden Stufen, nämlich die Läuterung der Vorstellung, die Erleuchtung der Gefühle und die Herausarbeitung des Willens zur reinen Tat, der Aufstieg auf dem Erkenntnis-weg erfolgt."
      ],
      [
        "Was der Mensch durch die Läuterung der Vorstellung erlangt, führt ihn dazu, das Geistige hinter allem zu er­kennen.",
        "Das Sinnliche wird ein Gleichnis für das Geistige.",
        "Er dringt tiefer ein, um das noch zu erfassen, was für die Vorstellung unzugänglich ist.",
        "Er erreicht dann eine Stufe, auf der er die Dinge nicht mehr durch die Vorstellung be­trachtet, sondern in die Sache selbst hineingewiesen wird, da, wo das Wesen der Dinge und das, was man nicht beschreiben"
      ],
      [
        "kann, Erreichnis wird.",
        "Und das, was man nicht beschreiben kann, was man, wie man im Laufe der Winter­Vorträge hören wird, in anderer Weise vorstellen muß, das, wobei man zu den Geheimnissen des Willens vorschreiten muß, bezeichnet er eben als das «Unbeschreibliche».",
        "Wenn der Mensch den dreifachen Weg durch die Vorstellung, das Gefühl und den Willen gemacht hat, dann vereinigt er sich mit dem, was im Chorus mysticus das «Ewig-Weibliche» genannt wird, das, was als menschliche Seele durchgemacht hat seine Entwickelung, das, was als die schöne Lilie dar­gestellt wird."
      ],
      [
        "So sehen wir, daß Goethe geradezu sein tiefstes Bekennt­nis, seine geheime Offenbarung auch noch da ausspricht, wo er sein großes Bekenntnisgedicht zum Abschluß bringt, nachdem er durch die Vorstellung, durch das Gefühl und den Willen emporgedrungen ist bis zur Vereinigung mit der schönen Lilie, bis zu dem Zustande, der seinen Aus­druck findet in der erwähnten Stelle des Chorus mysticus, die dasselbe ausdrückt, was Goethes Philosophie und Gei­steswissenschaft und was auch das «Märchen» sagt:"
      ],
      [
        "Alles Vergängliche"
      ],
      [
        "Ist nur ein Gleichnis!"
      ],
      [
        "Das Unzulängliche,"
      ],
      [
        "Hier wird's Erreichnis;"
      ],
      [
        "Das Unbeschreibliche,"
      ],
      [
        "Hier ist's getan;"
      ],
      [
        "Das Ewig-Weibliche"
      ],
      [
        "Zieht uns hinan!"
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "BIBEL UND WEISHEIT I Berlin, 12. November 1908",
    "paragraphs": [
      "BIBEL UND WEISHEIT",
      "Berlin, 12. November 1908",
      "Es gibt in unserer Kultur ja zweifellos kein Dokument, das in so tiefer Weise und in so intensiver Art in das ganze Geistesleben eingegriffen hat wie die Bibel. Eine Geschidite, nicht von Jahrhunderten, sondern von Jahrtausenden müßte man schreiben, wenn man die Wirkung der Bibel auf die Menschheit schildern wollte. Und wenn man ganz ab­sehen wollte von dem Einfluß dieses Dokumentes in die Breite, so würde man noch immer in bezug auf den Einfluß und die Wirkung in die Tiefen der Menschenseele in der Bibel ein Unermeßliches finden. Ja, in bezug auf den letz­teren Gesichtspunkt wird vielleicht gesagt werden dürfen, daß gerade unsere heutige Zeit des Interessanten außer­ordentlich vieles darbietet, denn man könnte zeigen, daß heute nicht nur diejenigen, welche in schwächerem oder stärkerem Maße auf dem Boden der Bibel stehen, von die­sem Menschheits-Dokumente tief beeinflußt sind, sondern daß auch sogar die, welche sich von der Bibel abgewendet haben, welche heute glauben, frei zu sein von den Einflüssen der Bibel, daß auch sogar diese, tief bedeutsam, noch immer diesen Einflüssen unterliegen. Denn die Bibel ist wirklich nicht nur ein Dokument, obwohl sie das in hervorragend­stem Maße ist, da sie die Seele erfüllt mit einer Summe von Vorstellungen über die Welt und das Leben, was der Seele also eine Weltanschauung gibt, sondern die Bibel war, durch Jahrtausende hindurch, ein gewaltiges Erziehungs-mittel der Seelen. Sie hat nicht nur für das Vorstellungsleben",
      "etwas bedeutet, und bedeutet dafür heute noch etwas, sondern es ist vielleicht wichtiger und wesentlicher, was wir als eine Wirkung bezeichnen müssen in bezug auf das Emp­findungs- und Gefühlsleben, in bezug auf die Art der Denkgewohnheiten. Da müssen wir, wenn wir fein zu­schauen, ganz gewiß heute vielfach zugeben, daß die Ge­fühle, die Empfindungen sogar derjenigen, welche die Bibel bekämpfen, durch die Bibel in ihren Seelen erst heran­gezogen worden sind.",
      "Aber wer nur ein wenig Umschau hält über das Geistes­leben der Menschheit, insbesondere über das unserer abend­ländischen Menschheit und derjenigen, die mit ihr zusammen­hängt, der wird bemerken, welch gewaltiger Umschwung eingetreten ist in bezug auf die Stellung der Menschheit, oder wenigstens eines großen Teiles der Menschheit, zur Bibel.",
      "Diejenigen, die heute vielleicht noch in einer ganz un­erschütterlichen Weise auf dem Boden der Bibel stehen, könnten das, worauf damit hingedeutet ist, vielleicht zu gering einschätzen. Sie könnten sagen: Mag es auch man­cherlei Leute geben, die heute sich aus diesen oder jenen Gründen von der Bibel abwenden, die behaupten, daß die Bibel nicht mehr dasjenige für die Menschheit sein könne, was sie durch Jahrtausende war, so wird das aber vermut­lich nur eine vorübergehende Zeiterscheinung sein. Wir glauben an die Bibel. Mögen die Herren, die glauben, auf dem Boden der Wissenschaft zu stehen, dieses oder jenes sagen, möge ihnen dieses oder jenes unwahrscheinlich klin­gen - uns gik die Bibel! - Man könnte dieses Urteil, wenn man suchen wollte, unter gewissen Persönlichkeiten sehr verbreitet finden, und es ist nur natürlich, denn wer noch immer das Glück seiner Seele, die Sicherheit und die Kraft der Seele für sich aus der Bibel zu schöpfen vermag, der",
      "kann nach seiner subjektiven Beschaffenheit gar nicht ge­nügend vieles in die Waagschale werfen gegen diejenigen Erscheinungen, die um ihn herum als Kritik und Ableh­nung der Bibel vorliegen.",
      "Dennoch wäre ein solches Urteil im Grunde genommen recht leichtsinnig. Es wäre sogar in gewisser Weise egoistisch, denn der Mensch, wenn er ein solches Urteil ausspricht, sagt sich: Mir gibt die Bibel dieses oder jenes; ob sie anderen Menschen dasselbe gibt, darum kümmere ich mich nicht. -Ein solcher Mensch gibt nicht acht darauf, daß die Mensch­heit im Grunde genommen ein Ganzes ist, und daß das­jenige, was zunächst in einzelnen lebt, von einzelnen gedacht und empfunden wird, hinabflutet in die ganze Menschheit und Allgemeingut wird.",
      "Wer sagt: Ich will nicht hören, was die Kritik und die Gelehrten der Bibel heute sagen, ich kümmere mich darum nicht -, der urteilt nur für sich und denkt nicht daran, ob auch seine Nach­kommen, ob diejenigen Menschen, die auf ihn folgen wer­den, sozusagen das Glück haben werden, das Glück haben können, eine solche Befriedigung in diesem Dokumente zu gewinnen, wenn die Kritik und die Wissenschaft sich an­schicken, dieses Dokument der Menschheit zu nehmen. Die Gewalt der Autoritäten, die an diesem Leben des Doku­mentes beteiligt sind, ist eine große und starke.",
      "Es heißt eigentlich doch, sich blind und taub stellen gegenüber dem, was um einen herum vorgeht, wenn man nur von dem eben charakterisierten Gesichtspunkte des naiven Glaubens, des unbeirrten Glaubens ausgehen will. Heute muß man schon hören, was bei unseren Mitmenschen das Ansehen und die Bedeutung dieses Menschheitsdokumentes erschüttern kann.",
      "Die Erschütterung, die Umwälzungen, die im Verlaufe der letzten Jahrhunderte mit Bezug auf dieses Dokument vor sich gegangen sind, sind ganz gewaltig.",
      "Noch vor wenigen Jahrhunderten hat die Bibel als etwas gegolten, das unbedingte Autorität genoß; sie galt als ein Schriftwerk höheren göttlichen Ursprungs. Dieser Glaube, diese Annahme ist seit langem erschüttert und wird immer mehr und mehr durch immer neue Gründe erschüttert wer­den.",
      "Zunächst war es nicht etwa unsere heutige Wissen­schaft, nicht etwa die gegenwärtige Naturwissenschaft, welche sich gegen die alte Auffassung der Bibel wendete. Es war schon vor weit mehr als hundert Jahren, da wendete sich - wir dürfen den Ausdruck gebrauchen, denn wir haben ihn öfter hier erklärt - die mehr materialistisch sich gestal­tende Denkgewohnheit dazu, die Bibel vom rein äußer­lichen Standpunkte aus anzusehen.",
      "Sprechen wir zunächst von dem Teil der Bibel, den wir als das Alte Testament bezeichnen. Er galt, wie das Neue Testament, durch Jahr­hunderte hindurch als eine Eingebung höherer Mächte. Er galt herausgeschrieben aus einem Bewußtsein, das sich er­heben konnte zu einer Wahrheitssphäre, zu der sich das sinnliche Bewußtsein nicht erheben konnte.",
      "Das war das erste, was den Glauben daran erschütterte, daß die Bibel aus einem höheren Menschheitsbewußtsein heraus geschrie­ben ist, daß ihr eine andere Autorität zukomme als irgend­eine Autorität eines menschlichen Schriftstellers. Das andere ist, daß man sich sagt: Wenn man die Bibel liest, dann stellt sich heraus, daß sie kein einheitliches Dokument ist. - Wir nehmen an, sagte im achtzehnten Jahrhundert ein französi­scher Arzt, die Menschen haben unter dem Einfluß der gei­stigen Welten gestanden, und so seien geschrieben die Ka­pitel, die wir als die Schöpfungsgeschichte Mosis bezeichnen.",
      "Nun lesen wir aber die Schöpfungsgeschichte. Da finden wir, daß einzelne Teile nicht zusammenstimmen. Wir fin­den, daß stilistische und sachliche Widersprüche vorhanden sind. Wir müssen daher annehmen, daß nicht ein einzelner",
      "Schriftsteller, sei es Moses oder irgendein anderer, dieses Dokument verfaßt hat, denn derjenige, der als einzelne persönlichkeit die Verhäknisse hintereinander hätte schil­dern können, der würde nicht die inneren Widersprüche in die Sache hineingebracht haben.",
      "Ich kann alle diese Widersprüche nur ihrem Geiste nach skizzieren. Da müssen alte Urkunden von verschiedenen Seiten her genommen und durch mancherlei Schriftsteller zu­sammen kombiniert worden sein. Das ist sozusagen ein erstes, das sich gegen die Bibel richtet.",
      "Nun wollen wir, abgesehen von dem, wie sich die Dinge abgespiek haben, den Geist dieser Art von Opposition gegen den geistigen Ursprung der Bibel einmal charakteri­sieren. Man sieht da, wie gleich im Anfange in gewaltigen, überwältigenden Bildern die Schöpfung entrollt wird. In ihr werden das sogenannte Sechs- bis Sieben-Tagewerk erzählt. Es wird da weiter erzählt, wie innerhalb dieser Schöpfung der Mensch entstanden ist, wie er in die Sünde kam, wie er weiter und weiter sich von Generation zu Ge­neration bildete. Da bemerkt man, daß in den ersten Tei­len, in den ersten Versen, für die göttlichen Gewalten, für den Gott, eine andere Bezeichnung gewählt ist, als vom vierten Verse des zweiten Kapitels an. Man sieht da, daß tatsächlich diese zwei Bezeichnungen, die Bezeichnung für das Göttliche als die Elohim und die Bezeichnung des Gött­lichen als Jahve öder Jehova, abwechseln. Da muß man sich fragen: Soll ein Schriftsteller das Göttliche mit zwei ver­schiedenen Namen bezeichnet haben? Woher kann das kommen? Man sagt sich, daß derjenige oder diejenigen, welche zuletzt das Dokument zusammenstellten, alte Tra­ditionen oder auch alte Urkunden gefunden haben, die sie zusammengekoppelt und dadurch ein Ganzes gemacht haben. Der eine kann von diesem Völksstamme, der andere",
      "von einem anderen Volksstamme gekommen sein, und das habe man zusammengekoppelt. Das ist sozusagen skizzen­haft das eine, das sich geltend macht. Von diesem ausgehend bemerkt man, immer weiter und weiter gehend, daß ähn­liche und noch andere innere Widersprüche auftauchen. So kam man immer mehr dahin, die ursprünglichen Urkunden zu sondern, zu zerreißen. Und wenn heute jemand zu­sammenstellen wollte eine Bibel, wie es ja geschehen ist, aus den verschiedenen Stücken und Fragmenten, aus denen man endlich glaubt, daß sie zusammengesetzt sein müßte, wenn jemand mit blauen Buchstaben druckte alles dasjenige, was man zur einen Urkunde rechnet, mit Rot, was zur anderen, mit Grün, was zur dritten und so weiter, dann würde ein merkwürdiges Dokument zusammenkommen. Es ist aber schon zustandegekommen - die Regenbogen-Bibel!",
      "Das uralte, ehrwürdige Dokument ist da, man möchte sagen, in einzelnen Lappen, aus denen es bestehen und aus denen es zusammengefügt sein soll. Es ist natürlich ein Dokument, von dem man glaubt, nachweisen zu können, daß es nicht von Moses herrührt, sondern sogar in verhält­nismäßig später Zeit von diesem öder jenem Priesterkölle­gium, während die Berichte der alten griechischen Ent­wickelung zusammengestellt sind aus Sagen und Mythen, die man von da und dort zusammengetragen hat, aus reli­giösen Priester-Anschauungen dieser oder jener Schule. Was auf diese Weise als Ganzes geworden ist, kann nicht gelten als etwas, das als eine Erhebung des geistigen Bewußtseins hineinschauen kann in die geistigen Welten, und das durch eine solche Erhebung der Menschenseele in die Geschichte hineingebracht worden wäre.",
      "Nun darf niemand glauben, daß diese beiden Vorträge, die ich heute und am Sonnabend zu halten habe, bestimmt sein sollen, irgendwie den Fleiß und die Emsigkeit der eben",
      "nur flüchtig skizzierten Arbeiten herabzusetzen. Wer die Dinge kennt, die so verwendet worden sind als geistige Hilfsmittel, die Bibel in kleine Stücke zu zerreißen und als kleine Stücke zu erklären, dem zeigen sich der Fleiß und die Regsamkeit und die Förschergeschicklichkeit bei der ganzen Arbeit. Sie zeigen sich dem, der es versteht, als das Gewal­tigste, was vielleicht in der Wissenschaft geleistet worden ist. Nicht in bezug auf das Formale, nicht in bezug auf das Emsige des Forschens läßt sich etwas Gleiches finden. Wenn man nun das etwas näher betrachtet, was als Folge dieser Forscherarbeit, die von den modernen Theologen geleistet worden ist, also gerade von denjenigen, die vermöge ihres Berufes fest glauben, auf dem Boden des Christentums zu stehen, so müssen wir uns sagen: es muß dazu führen, das Verhältnis der Bibel ganz anders zu gestalten als es durch Jahrhunderte hindurch war. Wenn diese Forschung ihre Früchte trägt, wird die Bibel nicht mehr sein können. Es würde viel dazugehören, die Bibel im einzelnen zu begrün­den, es würde aber die Bibel nicht mehr sein können das Dokument, das den Menschen tröstet und aufrichtet in den traurigsten Angelegenheiten des Lebens.",
      "Dazu kommt noch etwas anderes, nämlich, daß für zahl­reiche Menschen, die sich umgesehen haben im Bereiche der naturwissenschaftlichen Forschung, die sich umgesehen haben in der Geologie, in der Entwickelungsgeschichte des Pflan­zen-, Tier- und Menschenlebens, umgesehen haben in der Kulturgeschichte, in der Anthropologie und so weiter, daß für diese Menschen kaum noch eine Möglichkeit vorhanden ist, sich bei dem, was sie in der Bibel lesen, etwas zu den­ken. Man muß auch in dieser Beziehung gerecht sein und sich nicht einfach auf den Böden des naiven Glaubens stel­len und das sagen, was nichts zu bedeuten hat. Es sind oft diejenigen, die am gewissenhaftesten sind in ihrem Wahrheitsgefühl,",
      "in ihrem Erkenntnisdrang, die sich sagen: Wenn ich durch die auf sicherem Boden stehende Forschung sehe, wie sich die Erde entwickelt hat durch geologische Perioden hindurch, wie wir gewisse Hypothesen für die Sache haben, wie die Astronomie zeigt, wie sich die Erde aus einem Nebel von höherer Temperatur heraus zu der heutigen Ge­stalt entwickelt hat, wie sich das Unlebendige herausent­wickelt hat und aus diesem Unlebendigen die lebendige Wesenheit, wie sich nach und nach alles von dem Einfachen bis zum Kömpliziertesten, dem Menschen, entwickelt hat, wie die Kulturformen zu den heutigen komplizierten For­men aufgestiegen sind, wenn wir sehen, was die Geologie zeigt, welche gewaltigen Zeiträume nötig waren, um die Erde zu erhalten in einer Zeit, als sie noch nicht Amphibien, noch nicht Säugetiere hervorgebracht hatte, wenn wir das alles überblicken und auf uns wirken lassen - so sagen uns zahlreiche Persönlichkeiten -, was sollen wir da machen, wenn uns die Bibel erzählt, daß in sechs bis sieben Tagen die Welt erschaffen worden sein soll? Weder mit der Schöp­fung in sechs bis sieben Tagen noch mit irgend etwas an­derem können wir etwas anfangen.",
      "Was können wir an­fangen mit der Sintflut, mit der wunderbaren Rettung des Noah, wenn wir lesen, daß Noah so viele Tiere in die Arche gebracht hat, und so weiter? - So kommt es, daß manche mit Würde und ernstem Wahrheitssinn begabte Menschen jene scharfe und schneidige Opposition gegen die Bibel energisch vertreten, die sich von dem heutigen naturwissen­schaftlichen Standpunkte aus ergibt, insofern sie sich zu einer Weltanschauung erweitern will. Das alles ist in un­serer Weltanschauung vorhanden.",
      "Das alles können wir nicht wegleugnen.",
      "Nun entsteht aber die Frage: Sind wirklich alle die Dinge berücksichtigt, die der Bibel gegenüber zu berück­sichtigen",
      "sind, wenn entweder der erste historische oder der zweite naturwissenschaftliche Standpunkt geltend gemacht wird? Da muß gesagt werden, daß es heute schon einen dritten Gesichtspunkt gibt gegenüber der Bibel, einen Ge­sichtspunkt, der sich aus jener realen Forschungsmethode und menschlichen Anschauungsweise heraus entwickelt, die in diesen Vorträgen als die geisteswissenschaftliche oder anthroposophische charakterisiert wird. Mit diesem Ge­sichtspunkte gegenüber der Bibel haben wir uns heute und übermorgen zu befassen. Was ist dies für ein Gesichtspunkt? Man sagt heute vielfach, der Mensch dürfe sich nicht auf eine äußere Autorität stützen, er müsse voraussetzungslos an die Welt und an das Leben herangehen und die Wahr­heit erforschen. Man glaubt gerade die Bibel zu treffen, wenn man sich auf einen solchen Gesichtspunkt begibt. Trifft man in Wahrheit damit die Bibel? Es läßt sich das­jenige, was der geisteswissenschaftliche oder anthroposophi­sche Standpunkt der Bibel gegenüber ist, unbedingt ver­gleichen mit etwas, was sich vor einigen Jahrhunderten in bezug auf etwas anderes, wenn auch minder Bedeutendes, für die Menschheit zugetragen hat. Wir werden uns am leichtesten verständigen können über den geisteswissen­schaftlichen Gesichtspunkt der Bibel gegenüber, wenn wir einen Vergleich mit der Umwälzung in bezug auf die An­schauung von der Erde machen.",
      "Da sehen wir das ganze Mittelalter herauf, in allen Schulen, niederen und höheren, das, was in bezug auf die äußere Natur gelehrt worden ist, wir sehen den Kampf in alten Schriften, allerdings in Schriften einer großen und ge­waltigen Persönlichkeit, in den Schriften des alten griechi­schen Philosophen und Naturwissenschaftlers Aristoteles. Also, wenn Sie mit mir zurückgehen könnten an die Stätten des Geisteslebens der älteren Zeit, so würden Sie finden,",
      "daß nicht vorgetragen wurde in den Schulen und Gelehr­ten-Lehrstätten, was in den Laboratorien gefunden worden ist, sondern das, was auf Grund der Autorität der Bücher des Aristoteles gedruckt war. Aristoteles ist die Bibel der Naturwissenschaft. Und überall, wo man darüber vortrug, da erklärte man nur das, was Aristoteles über die Dinge schon gesagt hatte. Nun kamen die Zeiten, in denen eine neue Morgenröte heranbrach in bezug auf das Neue und Neueste von Kopernikus, Kepler und Galilei und allen an­deren bis auf den heutigen Tag. Was war der Grundnerv dieser Morgenröte? Während man vorher den Aristoteles als festen Ausgangspunkt genommen hatte, und so wie er gesprochen hat über die Natur sprach, wendeten nun Ko­pernikus, Kepler und Galilei ihren eigenen Beöbachtungs­und Forschungssinn an. Sie schauten selbst in die Natur hinaus und untersuchten, was das Leben ihnen zeigen konnte. So wollten sie die Natur beschreiben und erklären nach dem, was sie selbst gesehen hatten. Da kamen sie in manchen Widerspruch mit dem, was die streng Aristoteles-Gläubigen lehrten.",
      "Es ist mehr als eine bloße Anekdote, es bezeichnet die tiefe Wahrheit eines Prozesses, der sich damals abgespielt hat, wenn erzählt wird, daß ein Aristoteles-Gläubiger auf­gefordert wurde, sich doch einmal am menschlichen Körper selber anzusehen, daß es nicht richtig ist, daß die Nerven vom Herzen ausgehen, sondern daß sie vom Gehirn aus­gehen. Da ließ sich der Aristoteles-Gläubige bewegen, sich das anzuschauen. Dann sagte er aber: Wenn ich das an-schaue, dann scheint es, daß die Natur dem Aristoteles wi­dersprechen würde. Aber wenn die Natur dem Aristoteles widerspricht, so glaube ich nicht der Natur, sondern dem Aristoteles. - So stand die Naturwissenschaft gegenüber der Tradition. Die Anschauung des Forschers und Sehers",
      "wurde gegenüber dem, was als Tradition durch Jahrhun­derte sich fortgepflanzt hatte und nachgesprochen worden ist, abgelehnt. Wenn wir die Schriften Giordano Brunos lesen, sehen wir die Opposition gegenüber Aristoteles aus dem neuen Geist, der erzählt und erklärt, was der Mensch selber sehen sollte.",
      "Heute stehen wir der ganzen Sache schon wieder anders gegenüber. Wir stehen anders gegenüber der unmittelbaren naturwissenschaftlichen Beobachtung und auch gegenüber Aristoteles. Wir wissen, daß vieles von dem, was im Mittel­alter aus ihm herausgelesen worden ist, nur mißverständ­liche Auslegung war. Aus dem Geiste seiner Zeit heraus sagte ein Forscher, der unmittelbar hineinblickte in die Natur und das wiedergab, was er zu sehen verstand: Wenn wir Aristoteles richtig verstehen, werden wir eingehen kön­nen auf das, was er sagt. Dann erscheint er uns nicht mehr in jenem Widerspruch, in dem er zu stehen schien für die damalige Zeit, zur unmittelbaren wissenschaftlichen Be­obachtung. Dann können wir wieder seine Bewunderer werden. Denn selbst bei der Tatsache des Ausgangs der Nerven vom Herzen statt vom Gehirn zeigt es sich, daß er etwas ganz anderes gemeint hat, nämlich etwas, das selbst für unsere Zeit noch richtig ist.",
      "In einer ganz ähnlichen Art steht die Geistesforschung oder besser die geisteswissenschaftliche Forschung nicht nur zu diesen Dokumenten, sondern auch zu dem abendländi­schen Urdokument, zur Bibel. Was sich im sechzehnten Jahrhundert und seitdem in bezug auf die Beobachtung und Erforschung der äußeren Natur abgespielt hat, das spielt sich heute wieder ab in bezug auf die geistigen Untergründe der Welt. Aus dem Geiste jener Forschung heraus, die in den drei letzten Vorträgen charakterisiert worden ist, sucht die Menschheit wieder einzudringen in diejenigen Welten,",
      "die nicht mit den äußeren Sinnen wahrnehmbar sind, die aber wahrnehmbar sind für die höher entwickelten Sinne des Menschen, für die geistigen Sinne des Menschen, durch die wir ebenso in die geistige Welt hinein sehen können, wie wir durch die physischen Sinne in die physische Welt hinein sehen können.",
      "Es braucht hier nicht weiter ausgeführt zu werden, weil es ja schon öfter gesagt worden ist, daß der Mensch fähig ist, in sich die Kräfte zu entwickeln, daß er nicht nur die sinnlichen Dinge wahrnehmen kann, sondern daß er zwi­schen und hinter dem Sinnlichen eine geistige Welt wahr­nehmen kann, eine geistige Welt, die viel realer ist als die sinnliche Welt. Es hatte seinen guten Grund, daß die Menschheit eine Weile die Methode der geistigen Forschung vergaß. Die großen Fortschritte, die großen Eroberungen in der physischen Welt wurden gemacht dadurch, daß die Instrumente so vervollkommnet wurden, wie es im letzten Jahrhundert der Fall war. Aber wenn das eine in der menschlichen Natur sich vergrößert, dann treten andere Fähigkeiten in den Hintergrund. So sehen wir, wie in dem letzten Jahrhundert die naturwissenschaftlichen Methoden für die äußere physische Tatsachenwelt aufblühten. Nie­mals sind in der großartigen Weise mehr Instrumente ge­funden worden, um der Natur die Geheimnisse abzulau­schen und ihre Gesetze zu erforschen. In ungeheurer Weise sind die Fähigkeiten, die Bezug hierauf haben, vergrößert und verfeinert worden, aber zurückgetreten sind dagegen die Fähigkeiten, durch die der Mensch hineinschauen kann in die geistige Welt. So ist es nicht zu verwundern, wenn der Mensch zu dem Glauben gekommen ist, daß alles mate­riell ist, und daß das Materielle stofflich da sein muß, aus dem uns auch das Geistige erklärt werden kann.",
      "Aber wir stehen in der heutigen Zeit vor dem Einbruch",
      "einer Epoche, wo es der Menschheit wieder zum Bewußtsein kommt, daß es auch noch andere Instrumente und Werk­zeuge gibt, als diejenigen im physikalischen und physiolo­gischen Laboratorium, wo sie in so ausgezeichneter Weise benützt werden. Allerdings haben wir es zu tun mit einem Instrument, das sich gründlich unterscheidet von den an­deren.",
      "Wir haben es mit dem Grund- und Ur-Instrument zu tun, das wir im Menschen selbst zu erblicken haben. Der Mensch ist es, den wir im Laufe des Winters durch die Methoden der Konzentration und der Meditation kennen­lernen werden.",
      "Das sind andere Methoden, die der Mensch auf seine Seele anwenden kann, und durch die er dazu kommt, daß er die Umwelt in einer ganz anderen Weise sieht als er sie vörher gesehen hat. Er kann dazu kommen, daß er sich sagen kann: Ich bin wie ein operierter Blind-geborener, der vorher ableugnen konnte die Farben und das Licht der Welt. - Eingetreten ist aber für ihn nun der Moment, daß er selber sehen konnte.",
      "Er konnte nun sehen, daß zwischen dem, was die Sinne und der Verstand wahr­nehmen, noch etwas anderes ist. Jetzt sieht er hinein in die geistigen Dinge; jetzt weiß er, nicht hypothetisch, nicht durch spekulative Philosophien, sondern wie sinnlich, daß das Stoffliche nur wie eine Verdichtung ist des Geistigen, daß das, was wir mit den Sinnen sehen, sich so zu einem Geistigen hinter ihm verhält, wie sich Eis zu Wasser ver­hält.",
      "Das Wasser ist dünn, das Eis ist fest, und der, welcher das Wasser nicht sehen könnte, aber das Eis sehen kann, der würde sagen: Es ist nichts um das Eis herum da. - So sagt der, welcher nur mit den Sinnen sehen kann, es gebe nichts in weitem Umkreis als sinnliche Vorgänge, nichts als sinnliches Geschehen.",
      "Wir müssen aber vordringen in dieses übersinnliche Ge­biet, in dieses übersinnliche Geschehen, dann können wir",
      "auch das Geistige erkennen und erklären. Wer sich also keine geistigen Ohren und Augen ausgestaltet hat, der sieht in der ganzen Welt nichts als eine Verdichtung wie Eis im Wasser, und es erscheint ihm nicht die Urmutter-Substanz, das Geistige, in dem das Sinnliche nur eingebettet ist. Wenn uns der Geologe zeigt, wie etwa ein Mensch sich befindet, der in die Welt hinein einen Stuhl setzen könnte und schauen könnte, wie sich die Welt entwickelt hat: Der äußere sinnliche Anblick würde ein solcher sein, wie die Naturwissenschaft es schildert. Gegen das, was die Natur-wissenschaft im positiven Sinne zu sagen hat, hat die Gei­steswissenschaft nichts einzuwenden. Aber es zeigt sich dem, der da in richtiger Art in der Naturwissenschaft Bescheid weiß, daß vor dem ersten Entstehen des Physischen das Geistige da war. Da zeigt sich, wie der Fortschritt nur mög­lich wurde dadurch, daß das Geistige dazwischen mitwirkte, und daß am meisten der Geist an der Entwickelung be­teiligt ist.",
      "So weist uns diese geistige Weltanschauungsströmung darauf hin, daß es möglich ist, daß der Mensch sich zum Instrumente macht für die Erforschung der wichtigen Grundlagen der Welt, und so kommt unsere Anschauung endlich dazu, die geistigen Urgründe und Anfänge in uns selbst zu erforschen. So stehen sie da, unabhängig von jedem Dokument. Zunächst sagt die Geisteswissenschaft: Wir for­schen zunächst nicht in einem Dokumente. Wir forschen nicht wie einst Aristoteles in der geistigen Welt. Wir stellen uns so ein: Dasjenige, was Sie als gewöhnliche Schulgeome­trie lernen, die Euklidsche Geometrie, sie wurde in ihren ersten Anfängen durch Euklid, den großen Mathematiker, niedergeschrieben. Wir können das Dokument heute neh­men und es historisch auffassen. Aber wer heute in der Schule Geometrie lernt, lernt der noch nach dem Elementarbuche",
      "des Euklid? Man ahnt, lernt und erkennt an den Dingen selber. Man konstruiert sich zum Beispiel ein Drei­eck im Geiste, und es zeigen sich dann durch die innere Gesetzmäßigkeit die Gründe, wie die Sache ist. Dann kön­nen Sie mit dem, was Sie so aus sich selbst gewonnen haben, an Euklid herantreten und erkennen, inwiefern das schon erreicht war, was Euklid in seinem Buche verzeichnet hat. So forscht der Geisteswissenschaftler unabhängig von Büchern durch seine Organe, wie sich die Welt entwickelt. Und er findet so die Entwickelung der Welt, der Erde und der Zeit, bevor die Erde sich herauskristallisiert hat. Er erforscht die geistigen Vorgänge und findet, wie an einem bestimmten Punkte unser Geist im Dasein einsetzt; er zeigt, wie der Mensch als erster auftritt und nicht sich entwickelt hat aus untergeordneten Geschöpfen, allerdings als Nachkomme geistiger Wesenheiten, die zuerst da waren.",
      "Wir können zurückgehen in frühere Zeiten, wo noch die geistigen Urgründe waren. Wir finden da den Menschen mit diesen geistigen Vorgängen verknüpft, und erst später ent­wickeln sich zu dem Menschen hinzu die niederen Geschöpfe, so wie in der Entwickelung überhaupt gewisse Dinge zu­rückbleiben und andere sich herausentwickeln. Das Niedere ist von dem Höheren abgezweigt, abgegangen. Der Geistes-forscher weiß, daß die Organe sich entwickeln können durch Methoden, die der Geistesförscher zu zeigen vermag. So lehrt die Geistesforschung eine Weltentstehung und ein Wer­den von Gesetzen unabhängig von jedem Dokumente, aus der eigenen Gesetzmäßigkeit heraus, auch nicht gebunden an das, wie sich die Mathematik im Laufe der Geschichte entwickelt hat. Und so, wie sich der Forscher ein Wissen von der Weisheit angeeignet hat, so geht er an die Bibel heran und schaut sich jetzt die Bibel an.",
      "Jetzt zeigt sich uns sowohl der eine Gesichtspunkt in bezug",
      "auf die historisch-kritische Widersprudisförschung, wie auch der Gesichtspunkt der naturwissensdiaftlichen Wider­spruchsforschung. Beide Gesichtspunkte kommen aus einem einzigen großen Irrtum, der dadurch entstand, daß man allgemein glaubte, die Wahrheiten der Bibel von dem phy­sisch-sinnlichen Wahrnehmungs- und dem Beobachtungs­standpunkte aus auffassen zu sollen. Man meinte damals, es sei möglich, mit solchen Maßstäben an die Bibel heran­zutreten. Man hatte noch nicht die Forschungsergebnisse der anthropösophischen Geisteswissenschaft.",
      "Es soll jetzt an einzelnen Beispielen gezeigt werden, was eben gesagt worden ist. Die Geisteswissenschaft zeigt uns, daß zunächst die irdischen Geschöpfe das nächste sind, was um uns ist, daß wir aber mit dem, was in der Geologie und so weiter ist, nur bis zu einem gewissen Punkte kommen, und daß dann die Menschheitsentwickelung ins Unbestimmte nach rückwärts verläuft. Und warum? Niemals, soviel sie auch hoffen mag, wird die sinnliche Wissenschaft den Men­schen bis zum Ursprunge verfolgen können, aus dem Grunde, weil die sinnliche Wissenschaft nur das Sinnliche finden kann. Aber dem Sinnlichen im Menschen ist das Seelische und Geistige vorangegangen. Der Mensch war zuerst Seele und noch früher Geist, und er ist dann heruntergestiegen in das Erdendasein. Nur insofern der Mensch sich an dem Herunterstieg in das Erdendasein beteiligt hat, kann uns die Naturwissenschaft ihn im Niedergange zeigen. Das seelische Leben können wir nicht mit den gewöhnlichen Kräften der sinnlichen Beobachtung erforschen. Auch die Geologie kann uns keinen Leitfaden bieten. Sie bietet uns das, was zurückgeblieben ist an sinnlichen Materien. Sie kann also auch nur angeben, was man heute nicht sehen kann, aber sehen würde, wenn man einen Stuhl in das Welt­all setzen könnte und dann alles sehen würde. Darauf geht",
      "die Geisteswissenschaft nicht ein. Aber um den Menschen in urferner Vergangenheit als Geistwesen zu sehen, dazu muß man die geistigen Augen und die geistigen Ohren entwickelt haben. Hat man diese nicht, dann verschwindet der Mensch. Hat man aber die geistigen Augen, dann verschwindet das Sinnliche, und es ersteht das geistige Bild. Das kann man aber nicht in derselben Weise sehen wie das Sinnliche. Man muß sich ganz andere Begriffe über das Erkennen aneignen, wenn man in solche Urzeiten zurückgehen will. Was man da vom Menschen sich entwickeln sieht, als er erst Seele war, das zeigt sich nicht in sinnlichen gegenständlichen Wahr­nehmungen wie die äußere Sinneswelt sie bietet. Das zeigt sich uns in Bildern. Unser Bewußtsein wird durch die Ent­wickelung der inneren Kräfte der Seele das, was wir ein Bilderbewußtsein, ein imaginatives Bewußtsein nennen. Es ist dann das Bewußtsein ausgefüllt mit Bildern. Wir sind in einem anderen Bewußtseinszustande. Was sich damals ab­gespielt hat, das spielt sich jetzt in Bildern ab. Bildhaft ist das, was so im Inneren des Sehers vorgeht.",
      "Das Rudiment, das von der Sehergabe noch vorhanden ist, das ist der Traum. Der ist aber chaotisch. Das Sehen des ausgebildeten Sehers ist auch in solchen Bildern vorhanden, aber es entspricht der Wirklichkeit. Es ist ähnlich dem, wie der physisch-sinnliche Mensch unterscheiden kann, ob seine Vorstellungen der Wirklichkeit entsprechen oder nur eine Phantasie sind. Wer bei dern Satze stehenbleiben will: «Die Welt ist meine Vorstellung» und «Die äußeren Dinge regen nur die Vorstellung an», dem möchte ich zu erwägen geben, er soll sich ein Stück glühendes Eisen bringen lassen, es in seine Nähe bringen und fühlen, wie es brennt. Er soll es dann wegnehmen und fühlen, ob die bloße Vorstellung auch noch so brennt. Es gibt eben etwas, was die bloße Vorstel­lung unterscheidet von der Wahrnehmung, die durch den",
      "äußeren Gegenstand angeregt ist. Man darf daher nicht sagen, daß der Seher nur in Phantasmen lebt. Er hat eben auf diesem Felde sich so entwickelt, daß er unterscheiden kann, was Phantastik ist, was bloßes Bild oder Wirklichkeit ist für eine geistig-seelische Welt. So werden die Bilder das Ausdrucksmittel für eine geistig-seelische Welt. Der Seher blickt zurück in jene Zeit, die sich ihm in sinnlichen Gegen­ständen darstellte. Ebenso stellen sich bei ihm die wahren geistigen Wesenheiten und Begebenheiten den übersinnlichen Wahrnehmungsorganen dar. Der Geistesforscher spricht nicht von Kräften, die Abstraktionen sind, sondern von wirklichen Wesenheiten. Für ihn werden die geistigen Er­scheinungen zu Wahrheiten und zu Wesenheiten, und für ihn bevölkert sich die geistige Welt wieder mit geistigen Wesenheiten.",
      "Nun stellen Sie sich den Menschen vor in seiner vorzeiti­gen Entwickelung, als eine Wesenskraft eingegriffen hat in seine ganze Evolution, in seine Gestalt, eine Wesenheit, die sich unterscheidet, ganz genau unterscheidet von anderen Wesenheiten, die früher eingegriffen haben, denn wir kön­nen das Geistig-Seelische des Menschen, das schon im Über-sinnlichen ist, noch weiter zurück verfolgen. Wir können es in noch höhere Sphären zurück verfolgen. Dann aber muß der Geistesforscher, wenn er in diese höheren Sphären kommt, in diesen höheren Sphären lebt, und wenn er von geistigen Wesenheiten spricht, auch von anderen geistigen Sphären sprechen.",
      "Nun tritt der Geistesförscher an den Anfang der Bibel heran. Da zeigt sich ihm, daß mit wunderbarer Treue die Bilder gegeben sind, die uns das Seelisch-Geistige in der Entwickelung des Menschen darstellen, bevor er in das phy­sische Leben herausgetreten ist. Der Geistesforscher kann, wenn er seine eigenen Imaginationen, die er in seinem Inneren",
      "hat, dann in den äußeren Dokumenten wieder findet, sich sagen, daß er diese in Wahrheit erkennt. Wenn er nun zurückgeht in die Zeiten, wo der Mensch den noch höheren Sphären angeschlossen war, da muß er für diese Grund­wesen einen anderen Namen wählen, und er findet, daß die Kapitel, die dem vierten Vers des zweiten Kapitels voran­gehen, tatsächlich einen anderen Göttesnamen haben. Genau mit den Ergebnissen der Geistesförschung stimmt es über­ein, daß vom vierten Vers des zweiten Kapitels an für die Darstellung der Urwelten-Entwickelung ein neuer Gottes­name auftritt. So sehen wir uns mit der Geistesforschung in der Lage, in der sich heute ein Kenner der Geometrie befin­det. Er kann Geometrie aus sich finden, und dann weiß er das Werk des Euklid zu schätzen, der dasselbe gefunden hat. So sehen wir die Entwickelung in den wunderbaren Bildern des Alten Testamentes, und jetzt zeigt sich uns etwas höchst Merkwürdiges. Licht und hell wird es über dem Texte der Bibel, wie es nicht heller licht werden konnte bei dem wissenschaftlichen Kritiker.",
      "Ein Forscher sagt: Was die Elohim hat, das muß von einer anderen Seite herrühren als das, was von Jahve her­kommt. Wenn man das im Ernste anwenden will, dann ist es sonderbar. Wir wollen es einmal versuchen. Stellen wir uns dieses Bild einmal vor. Die Schlange war listiger als alle Tiere, die Gott der Herr gemacht hatte und spricht zu dem Weibe: Hat euch nicht Gott gesagt, ihr sollt nicht essen von dem Baume des Gartens. - Wenn nun statt Elohim und Jahve nur «Gott» steht, so ist es sonderbar. Die Schlange war listig, die Gott Jahve gemacht hat. Sollte Gott gesagt haben: Ihr sollt nicht essen? - Es steht nicht Jahve, sondern «die Elohim». Nun fährt das Weib fort und erklärt immer so, daß sie von Gott spricht. Und im achten Vers heißt es weiter: Und sie hörten die Stimme Gottes, des Herrn -",
      "Aber es heißt im Urtext: die Stimme des Jahve. Nun hätten wir die Geschichte der Schlange zusammengestellt, so daß erklärlich wird, daß die, welche die Namen Jahve, Elohim gebraucht haben, eine andere Wesenheit meinen. Das rührt von der einen Tradition her. Und von der Elohim-Tradi­tion rührt es her: Wie? Sollte Gott gesagt haben, ihr sollt nicht essen? - Sie sehen, es wird wirklich aus Lappen die Bibel so zusammengesetzt, daß mitten in den Sätzen dann die Traditionen zusammengenommen werden müssen.",
      "Gehen Sie mit geisteswissenschaftlicher Forschung an die Bibel heran, dann zeigt sich Ihnen, daß dies auch so stehen kann. Es ist die Rede von dem vierten Vers des zweiten Kapitels an, daß die Weltschöpfung von den Elohim an den Jahve übergeht. Er ist also die Macht, die dasjenige zur Entwickelung bringt, was dann bis zum Sündenfall zur Entwickelung kommt. Die Geisteswissenschaft zeigt Ihnen dann, daß der Jahve derjenige Gott ist, der in das Innere der Menschen hinein spricht das, was wir als das Ich haben, das Ich-bin. Diese Wesenheit, die Ich-bin-Wesenheit, ist es, die alles das bewirkt, was vom zweiten Kapitel, vierter Vers, an gesagt wird. Die Wesenheit, die jetzt eingreift, ist das, was Jahve ist, eine Wesenheit, die einer früheren Ent­wickelung angehört, aber nur abgefallen ist. Sie bekommt nicht den Zugang. Daher ist die Rede von Gott-Jahve. Die Schlange aber weiß nichts von Jahve; sie muß sich daher wenden an das, was von ihrem eigenen Stoffe ist, in dem Momente, wo eintritt das, was gerade durch Jahve eintreten muß. Also im achten Vers tritt wieder der Name des Jahve ein.",
      "So erwirbt man sich durch die Geistesforschung ein Be­wußtsein, das Bewußtsein, daß die Bibel eine Urkunde ist, in der nichts, auch gar nichts bloß zufällig steht. Mag sich ein moderner Schriftsteller wundern - es sind nicht solche",
      "Sippen von modernen Schriftstellern, wie sie bei den alten Eingeweihten waren - und sagen: Warum sollte nicht ein­mal dieser Gott einen anderen Namen annehmen? Wo ge­nau und korrekt gesprochen werden soll, wird nicht in stilistischer Form geredet. Was dasteht und was weggelas­sen ist, hat seine Bedeutung. Wenn der Name Jahve auf-tritt, und wenn er weggelassen wird, so bedeutet das etwas höchst Wesentliches. Aber man muß den Grundsatz durch­führen, daß die Bibel höchst genau zu lesen ist. Lesen Sie die Bibel, wenn Sie sie haben! Lesen Sie das Sechs-Tage-Werk durch und Sie finden, daß es so aufgefaßt wird, daß der erste Vers zum zweiten Kapitel fortgelassen wird bis zum Sabbat, und dann kommt also, daß Gott der Herr Himmel und Erde machte. Diese Verse rechnet man ge­wöhnlich als eine Hindeutung auf das Vorherstehende. So, wie wenn das Sieben-Tage-Werk erzählt worden wäre, und noch gesagt wird: So ist es gemacht worden, das Sieben-Tage-Werk, dies ist die Entstehungsgeschichte Himmels und der Erde, und dann soll es weitergehen.",
      "Wer hier den Urtext studiert, der kommt auf das Fol­gende: der vierte Vers des zweiten Kapitels bezieht sich nicht auf das Vorhergehende, sondern auf das Nachfol­gende, geradeso, wie sich später auf das Nachfolgende be­zieht dieses Sündengeschlecht des Adam, auf das Hinterher, auf die folgende Generation, auf dasjenige, was aus Adam entstanden ist. Da wird in derselben Weise gesagt: Was da folgt, das sind die Geschlechter des Himmels und der Erde.",
      "- Im Hebräischen steht auch dasselbe Wort. Wer genau liest, der weiß das Folgende: daß von den Worten an «Im Anfang schuf Gott Himmel und Erde» bis zum dritten Vers des zweiten Kapitels die geistige Welt geschildert wird, wie sie geschaffen ist. Dann wird vom vierten Verse an gesagt:",
      "Das, was Nachkomme ist von Himmel und Erde, wird im",
      "Folgenden geschildert. Es ist der wunderbarste Übergang, wenn man die Sache versteht, von dem Sechs-Tage-Werke zu dem Folgenden. Wer sich auf diese Dinge einläßt, findet, daß es vielleicht kein so gut kombiniertes Buch gibt wie die Bibel, namentlich die ältesten Teile derselben. Der Glaube, daß man ohne geistige Forschung an die Bibel herantreten dürfe, daß man mit äußeren Urkunden an sie herantreten könne, das hat dieses in sich so vollkommene und harmo­nische Werk aufgelöst, so daß es aus lauter Lappen und Fragmenten zusammengesetzt erscheint.",
      "Man muß auch den Grundsatz, genau zu lesen, und den Grundsatz, die Bibel zu haben, noch weiterverfolgen. Man hat die Bibel nicht, wenn man nur den Wortlaut hat, der das einzelne, worauf es ankommt, nur andeutet. Man muß den Grundsatz haben, auf die Bibel einzugehen. Es wird uns an einem späteren Tage des Sechs-Tage-Werkes erzählt, wie Sonne und Mond entstehen, wie Sonne und Mond Tag und Nacht bedingen. Schon vorher wird aber von Tag und Nacht erzählt. Aus der Bibel könnte man die Folgerung ziehen: Tag und Nacht, wie sie mit Sonne und Mond zu­sammenhängen, können nicht gemeint sein mit Tag und Nacht, die von der Sonne und dem Monde abhängen. Hier könnte man einen handgreiflichen Hinweis darauf sehen, wie die Bibel von dem sinnlichen Sonnentag und der Son­nennacht spricht. Sie entstehen durch das, was wir Um­drehung der Erde um die Sonne nennen. Wir können sehen, wie die Bibel von dem sinnlichen Tag hinausweist in das, was im Übersinnlichen, im Geistigen ist, wie sie es erhöht und erweitert in das Geistige hinein.",
      "Diejenigen, welche die Bibel geistig erforschen konnten, waren immer in der Lage, daß sie sich sagten: Wenn einer die Sehergabe, die Gabe des höheren Schauens hat und den Sinn der Bibel in Wirklichkeit finden kann, dann ist es",
      "selbstverständlich, daß dieser Sinn auch aus der Sehergabe erflossen ist. - Wenn wir dadurch, daß sich die Seele in eine andere Geistesstimmung versetzt, hineinblicken können in das, was uns in den gewaltigen Bildern der Bibel gegeben ist, dann wissen wir, daß der, welcher es geschrieben hat, auch unter der Inspiration der geistigen Welt gestanden haben muß. Wir dürfen wohl sagen: Es beginnt die Zeit, wo immer mehr begriffen werden soll, daß es viererlei Stufen gibt, wie man heute die Bibel betrachten kann.",
      "Die erste Stufe ist die des naiven Glaubens. Sie nimmt die Bibel in unbeirrter Sicherheit und ahnt nichts von dem, was heute als Einwendungen gegen die Bibel angeführt worden ist.",
      "Die zweite Stufe: Das sind die gescheiten Leute, diejeni­gen, welche entweder durch Bibelkritik, durch das Erfor­schen der inneren Widersprüche oder durch den naturwis­senschaftlichen Standpunkt finden, daß die Bibel das primi­tive Sagen- und Legendenwerk einer noch nicht forschenden Menschheit war. Sie sind hinaus über die Bibel, sie brau­chen sie nicht mehr, sie greifen sie von den verschiedensten Richtungen an und sagen: Sie ist gut gewesen für die kind­liche Menschheit. Jetzt aber wächst die Menschheit über die Bibel hinaus. - Das sind die Gescheiten, die Freidenker.",
      "Dann gibt es eine weitere Stufe: Der Mensch wächst über diese Gescheitheit hinaus. Die Menschen dieser Stufe sind auch Freidenker, sie sind über diesen zweiten Standpunkt der gescheiten Leute hinausgewachsen. Sie sehen in den Er­zählungen der Bibel - des Alten und Neuen Testamentes -wenigstens symbolische und mythische Einkleidungen von inneren Seelenerlebnissen. Sie sehen das, was in abstrakter Weise in den menschlichen Seelen sich darstellt, was sich in Bildern darstellt. Dazu sind manche Freidenker gezwungen worden. Sie haben den Standpunkt des freidenkerischen",
      "Menschen in den Standpunkt des mythischen Symbolikers, des mythischen Darstellers verwandeln müssen.",
      "Dann gibt es einen vierten Standpunkt. Das ist der, wel­cherlhnen heute als derjenige der Geisteswissenschaft charak­terisiert worden ist. Übermorgen werden wir ihn weiter­verfolgen, diesen geisteswissenschaftlichen Standpunkt. Er zeigt wieder die geistigen Tatsachen in einfachen Beschrei­bungen, allerdings so, wie man diese geistigen Tatsachen in den Imaginationen sehen kann. Es sind die Tatsachen, die in der Bibel beschrieben sind. Wer den naiven Standpunkt verlassen mußte und als Forscher zum gescheiten Menschen, vielleicht zum Symboliker geworden ist, der kann dann kommen zu dem Standpunkte, auf dem der Geistesforscher steht, und er kann dann fähig werden, die Bibel wieder wörtlich zu nehmen, in einem neuen Sinne wörtlich zu neh­men, nämlich, die Worte wirklich zu verstehen.",
      "Während Jahrhunderten hat man eigentlich nicht die Bibel kritisiert. Man hat sein eigenes Phantasiengeschöpf bekämpft, das, was man aus der Bibel gemacht hat. So gibt cs heute noch Kämpfer gegen die Bibel. Sie kämpfen gegen ihr eigenes Phantasiengeschöpf, gegen das, was sie davon verstehen können. Die Bibel treffen sie gar nicht. Wörtlich also kann die Bibel wieder genommen werden, nur muß man das Wort richtig verstehen.",
      "Es ist heute eine gewisse Strömung da, die gegen ein solches Gespräch das Wort geltend machen wird: Nicht der Buchstabe, der Geist muß entscheiden; der Buchstabe tötet, der Geist macht lebendig, und Du bekennst wieder aus gewissen Beziehungen den Buchstaben.",
      "Ich wollte, wir könnten so bald als möglich den echten Bibelbuchstaben der Welt wieder bringen. Die Welt würde erstaunen darüber, was der Urtext enthält. Wie etwas ganz Neues wird er der Menschheit vorkommen. Mit dem Ausspruche:",
      "Der Buchstabe tötet, der Geist macht lebendig -, darf man nicht so hausieren gehen. Es ist gewöhnlich der Herren eigener Geist, in dem die Buchstaben sich bespiegeln. So ist es besonders im Symbolischen. Ist er trivial, so legt er triviale Symbole; ist er geistreich, so legt er geistreiche Symbole hinein. Es ist mit diesemWort wie mit demSpruche von Goethe:",
      "Und solang du das nicht hast,",
      "Dieses:    Stirb und Werde!",
      "Bist du nur ein trüber Gast",
      "Auf der dunklen Erde.",
      "Dieses Wort deutet uns an, wie der Mensch hinauskom­men soll über die sinnliche Anschauung, überhaupt über die gewöhnliche Natur. Wer dieses Wort als eine Anweisung dazu nehmen würde, daß er sich sagt, das Physische habe keinen Wert, der hat übersehen, daß der Geist nach und nach sich aus dem Physischen herausentwickelt. So ist es auch mit dem Buchstaben und dem Geist. Erst muß man den Buchstaben haben, dann ihn enträtseln können, und dann wird man finden, welches der Geist ist. Gewiß, der Buchstabe tötet, aber er erschafft in seinem Tode den Geist, und es entspricht dieser Ausspruch dem anderen: Wer das nicht hat, dieses Stirb und Werde, der bleibt nur ein trüber Gast auf der dunklen Erde.",
      "Nur in den Prinzipien könnte ich Sie heute auf die Kritik der Bibel aufmerksam machen und auf die Gesichtspunkte, welche die Geisteswissenschaft gegenüber der Bibel ein­nehmen wird. Aus den wenigen Andeutungen, die heute gefallen sind, wird man wenigstens erahnen können, daß durch die Arbeit der Geisteswissenschaft sich wird voll­ziehen können etwas wie eine Wiedereroberung der Bibel. Weisheit soll die Geisteswissenschaft finden, unabhängig",
      "von der Bibel. Aber dann kommt die Geisteswissenschaft und erkennt, was in diese Bibel hineingeflossen ist, und dann erlebt man, was viele aus der Geisteswissenschaft heraus gegenüber der Bibel erlebt haben. Einiges hat sie erbauen können, das meiste aber hat für sie keinen Sinn mehr. Dann kommen sie durch die Geisteswissenschaft darauf, was mit diesem und jenem gesagt wird. Dann stehen da aber noch andere Stellen, die recht anfechtbar zu sein scheinen. Man kommt dann zu dem Standpunkte, zu sagen: Es sind in der Bibel Stellen enthalten, die tiefe geisteswissenschaftliche Wahrheiten enthalten, aber es ist manches hineingeflossen, was als etwas Unorganisches hineingegliedert worden ist. -Dann geht man weiter, macht wieder eine Entdeckung und findet, daß es an einem selbst gelegen hat, nämlich daran, daß man nicht weit genug war, die Sache zu verstehen. Und man gelangt dahin, sich zu sagen: Wo man früher geglaubt hat, der Sinn scheine gegen­über der Weisheit nicht haltbar zu sein, da sieht man jetzt, das eine verstehst Du, daß Du die Bibel mit Vertrauen und Verehrung betrachten mußt; das andere verstehst Du eben noch nicht. Aber es wird die Zeit kommen, daß Du es ver­stehen wirst, und Du wirst wieder den Standpunkt finden, wo Du selbst hineinschauen kannst.",
      "Die Geisteswissenschaft wird zur richtigen Schätzung der Bibel führen. Die Geisteswissenschaft ist heute erst am Beginne ihrer Schöpfung. Die Bibel hat eine Krisis, eine Kritik durchzumachen. Die Forschungen der Geisteswissen­schaft werden ihr entgegenkommen, und in neuer Gestalt wird das alte Licht durch das Geistesleben in der Zukunft der Menschheit leuchten."
    ],
    "sentences": [
      [
        "BIBEL UND WEISHEIT"
      ],
      [
        "Berlin, 12.",
        "November 1908"
      ],
      [
        "Es gibt in unserer Kultur ja zweifellos kein Dokument, das in so tiefer Weise und in so intensiver Art in das ganze Geistesleben eingegriffen hat wie die Bibel.",
        "Eine Geschidite, nicht von Jahrhunderten, sondern von Jahrtausenden müßte man schreiben, wenn man die Wirkung der Bibel auf die Menschheit schildern wollte.",
        "Und wenn man ganz ab­sehen wollte von dem Einfluß dieses Dokumentes in die Breite, so würde man noch immer in bezug auf den Einfluß und die Wirkung in die Tiefen der Menschenseele in der Bibel ein Unermeßliches finden.",
        "Ja, in bezug auf den letz­teren Gesichtspunkt wird vielleicht gesagt werden dürfen, daß gerade unsere heutige Zeit des Interessanten außer­ordentlich vieles darbietet, denn man könnte zeigen, daß heute nicht nur diejenigen, welche in schwächerem oder stärkerem Maße auf dem Boden der Bibel stehen, von die­sem Menschheits-Dokumente tief beeinflußt sind, sondern daß auch sogar die, welche sich von der Bibel abgewendet haben, welche heute glauben, frei zu sein von den Einflüssen der Bibel, daß auch sogar diese, tief bedeutsam, noch immer diesen Einflüssen unterliegen.",
        "Denn die Bibel ist wirklich nicht nur ein Dokument, obwohl sie das in hervorragend­stem Maße ist, da sie die Seele erfüllt mit einer Summe von Vorstellungen über die Welt und das Leben, was der Seele also eine Weltanschauung gibt, sondern die Bibel war, durch Jahrtausende hindurch, ein gewaltiges Erziehungs-mittel der Seelen.",
        "Sie hat nicht nur für das Vorstellungsleben"
      ],
      [
        "etwas bedeutet, und bedeutet dafür heute noch etwas, sondern es ist vielleicht wichtiger und wesentlicher, was wir als eine Wirkung bezeichnen müssen in bezug auf das Emp­findungs- und Gefühlsleben, in bezug auf die Art der Denkgewohnheiten.",
        "Da müssen wir, wenn wir fein zu­schauen, ganz gewiß heute vielfach zugeben, daß die Ge­fühle, die Empfindungen sogar derjenigen, welche die Bibel bekämpfen, durch die Bibel in ihren Seelen erst heran­gezogen worden sind."
      ],
      [
        "Aber wer nur ein wenig Umschau hält über das Geistes­leben der Menschheit, insbesondere über das unserer abend­ländischen Menschheit und derjenigen, die mit ihr zusammen­hängt, der wird bemerken, welch gewaltiger Umschwung eingetreten ist in bezug auf die Stellung der Menschheit, oder wenigstens eines großen Teiles der Menschheit, zur Bibel."
      ],
      [
        "Diejenigen, die heute vielleicht noch in einer ganz un­erschütterlichen Weise auf dem Boden der Bibel stehen, könnten das, worauf damit hingedeutet ist, vielleicht zu gering einschätzen.",
        "Sie könnten sagen: Mag es auch man­cherlei Leute geben, die heute sich aus diesen oder jenen Gründen von der Bibel abwenden, die behaupten, daß die Bibel nicht mehr dasjenige für die Menschheit sein könne, was sie durch Jahrtausende war, so wird das aber vermut­lich nur eine vorübergehende Zeiterscheinung sein.",
        "Wir glauben an die Bibel.",
        "Mögen die Herren, die glauben, auf dem Boden der Wissenschaft zu stehen, dieses oder jenes sagen, möge ihnen dieses oder jenes unwahrscheinlich klin­gen - uns gik die Bibel! - Man könnte dieses Urteil, wenn man suchen wollte, unter gewissen Persönlichkeiten sehr verbreitet finden, und es ist nur natürlich, denn wer noch immer das Glück seiner Seele, die Sicherheit und die Kraft der Seele für sich aus der Bibel zu schöpfen vermag, der"
      ],
      [
        "kann nach seiner subjektiven Beschaffenheit gar nicht ge­nügend vieles in die Waagschale werfen gegen diejenigen Erscheinungen, die um ihn herum als Kritik und Ableh­nung der Bibel vorliegen."
      ],
      [
        "Dennoch wäre ein solches Urteil im Grunde genommen recht leichtsinnig.",
        "Es wäre sogar in gewisser Weise egoistisch, denn der Mensch, wenn er ein solches Urteil ausspricht, sagt sich: Mir gibt die Bibel dieses oder jenes; ob sie anderen Menschen dasselbe gibt, darum kümmere ich mich nicht. -Ein solcher Mensch gibt nicht acht darauf, daß die Mensch­heit im Grunde genommen ein Ganzes ist, und daß das­jenige, was zunächst in einzelnen lebt, von einzelnen gedacht und empfunden wird, hinabflutet in die ganze Menschheit und Allgemeingut wird."
      ],
      [
        "Wer sagt: Ich will nicht hören, was die Kritik und die Gelehrten der Bibel heute sagen, ich kümmere mich darum nicht -, der urteilt nur für sich und denkt nicht daran, ob auch seine Nach­kommen, ob diejenigen Menschen, die auf ihn folgen wer­den, sozusagen das Glück haben werden, das Glück haben können, eine solche Befriedigung in diesem Dokumente zu gewinnen, wenn die Kritik und die Wissenschaft sich an­schicken, dieses Dokument der Menschheit zu nehmen.",
        "Die Gewalt der Autoritäten, die an diesem Leben des Doku­mentes beteiligt sind, ist eine große und starke."
      ],
      [
        "Es heißt eigentlich doch, sich blind und taub stellen gegenüber dem, was um einen herum vorgeht, wenn man nur von dem eben charakterisierten Gesichtspunkte des naiven Glaubens, des unbeirrten Glaubens ausgehen will.",
        "Heute muß man schon hören, was bei unseren Mitmenschen das Ansehen und die Bedeutung dieses Menschheitsdokumentes erschüttern kann."
      ],
      [
        "Die Erschütterung, die Umwälzungen, die im Verlaufe der letzten Jahrhunderte mit Bezug auf dieses Dokument vor sich gegangen sind, sind ganz gewaltig."
      ],
      [
        "Noch vor wenigen Jahrhunderten hat die Bibel als etwas gegolten, das unbedingte Autorität genoß; sie galt als ein Schriftwerk höheren göttlichen Ursprungs.",
        "Dieser Glaube, diese Annahme ist seit langem erschüttert und wird immer mehr und mehr durch immer neue Gründe erschüttert wer­den."
      ],
      [
        "Zunächst war es nicht etwa unsere heutige Wissen­schaft, nicht etwa die gegenwärtige Naturwissenschaft, welche sich gegen die alte Auffassung der Bibel wendete.",
        "Es war schon vor weit mehr als hundert Jahren, da wendete sich - wir dürfen den Ausdruck gebrauchen, denn wir haben ihn öfter hier erklärt - die mehr materialistisch sich gestal­tende Denkgewohnheit dazu, die Bibel vom rein äußer­lichen Standpunkte aus anzusehen."
      ],
      [
        "Sprechen wir zunächst von dem Teil der Bibel, den wir als das Alte Testament bezeichnen.",
        "Er galt, wie das Neue Testament, durch Jahr­hunderte hindurch als eine Eingebung höherer Mächte.",
        "Er galt herausgeschrieben aus einem Bewußtsein, das sich er­heben konnte zu einer Wahrheitssphäre, zu der sich das sinnliche Bewußtsein nicht erheben konnte."
      ],
      [
        "Das war das erste, was den Glauben daran erschütterte, daß die Bibel aus einem höheren Menschheitsbewußtsein heraus geschrie­ben ist, daß ihr eine andere Autorität zukomme als irgend­eine Autorität eines menschlichen Schriftstellers.",
        "Das andere ist, daß man sich sagt: Wenn man die Bibel liest, dann stellt sich heraus, daß sie kein einheitliches Dokument ist. - Wir nehmen an, sagte im achtzehnten Jahrhundert ein französi­scher Arzt, die Menschen haben unter dem Einfluß der gei­stigen Welten gestanden, und so seien geschrieben die Ka­pitel, die wir als die Schöpfungsgeschichte Mosis bezeichnen."
      ],
      [
        "Nun lesen wir aber die Schöpfungsgeschichte.",
        "Da finden wir, daß einzelne Teile nicht zusammenstimmen.",
        "Wir fin­den, daß stilistische und sachliche Widersprüche vorhanden sind.",
        "Wir müssen daher annehmen, daß nicht ein einzelner"
      ],
      [
        "Schriftsteller, sei es Moses oder irgendein anderer, dieses Dokument verfaßt hat, denn derjenige, der als einzelne persönlichkeit die Verhäknisse hintereinander hätte schil­dern können, der würde nicht die inneren Widersprüche in die Sache hineingebracht haben."
      ],
      [
        "Ich kann alle diese Widersprüche nur ihrem Geiste nach skizzieren.",
        "Da müssen alte Urkunden von verschiedenen Seiten her genommen und durch mancherlei Schriftsteller zu­sammen kombiniert worden sein.",
        "Das ist sozusagen ein erstes, das sich gegen die Bibel richtet."
      ],
      [
        "Nun wollen wir, abgesehen von dem, wie sich die Dinge abgespiek haben, den Geist dieser Art von Opposition gegen den geistigen Ursprung der Bibel einmal charakteri­sieren.",
        "Man sieht da, wie gleich im Anfange in gewaltigen, überwältigenden Bildern die Schöpfung entrollt wird.",
        "In ihr werden das sogenannte Sechs- bis Sieben-Tagewerk erzählt.",
        "Es wird da weiter erzählt, wie innerhalb dieser Schöpfung der Mensch entstanden ist, wie er in die Sünde kam, wie er weiter und weiter sich von Generation zu Ge­neration bildete.",
        "Da bemerkt man, daß in den ersten Tei­len, in den ersten Versen, für die göttlichen Gewalten, für den Gott, eine andere Bezeichnung gewählt ist, als vom vierten Verse des zweiten Kapitels an.",
        "Man sieht da, daß tatsächlich diese zwei Bezeichnungen, die Bezeichnung für das Göttliche als die Elohim und die Bezeichnung des Gött­lichen als Jahve öder Jehova, abwechseln.",
        "Da muß man sich fragen: Soll ein Schriftsteller das Göttliche mit zwei ver­schiedenen Namen bezeichnet haben?",
        "Woher kann das kommen?",
        "Man sagt sich, daß derjenige oder diejenigen, welche zuletzt das Dokument zusammenstellten, alte Tra­ditionen oder auch alte Urkunden gefunden haben, die sie zusammengekoppelt und dadurch ein Ganzes gemacht haben.",
        "Der eine kann von diesem Völksstamme, der andere"
      ],
      [
        "von einem anderen Volksstamme gekommen sein, und das habe man zusammengekoppelt.",
        "Das ist sozusagen skizzen­haft das eine, das sich geltend macht.",
        "Von diesem ausgehend bemerkt man, immer weiter und weiter gehend, daß ähn­liche und noch andere innere Widersprüche auftauchen.",
        "So kam man immer mehr dahin, die ursprünglichen Urkunden zu sondern, zu zerreißen.",
        "Und wenn heute jemand zu­sammenstellen wollte eine Bibel, wie es ja geschehen ist, aus den verschiedenen Stücken und Fragmenten, aus denen man endlich glaubt, daß sie zusammengesetzt sein müßte, wenn jemand mit blauen Buchstaben druckte alles dasjenige, was man zur einen Urkunde rechnet, mit Rot, was zur anderen, mit Grün, was zur dritten und so weiter, dann würde ein merkwürdiges Dokument zusammenkommen.",
        "Es ist aber schon zustandegekommen - die Regenbogen-Bibel!"
      ],
      [
        "Das uralte, ehrwürdige Dokument ist da, man möchte sagen, in einzelnen Lappen, aus denen es bestehen und aus denen es zusammengefügt sein soll.",
        "Es ist natürlich ein Dokument, von dem man glaubt, nachweisen zu können, daß es nicht von Moses herrührt, sondern sogar in verhält­nismäßig später Zeit von diesem öder jenem Priesterkölle­gium, während die Berichte der alten griechischen Ent­wickelung zusammengestellt sind aus Sagen und Mythen, die man von da und dort zusammengetragen hat, aus reli­giösen Priester-Anschauungen dieser oder jener Schule.",
        "Was auf diese Weise als Ganzes geworden ist, kann nicht gelten als etwas, das als eine Erhebung des geistigen Bewußtseins hineinschauen kann in die geistigen Welten, und das durch eine solche Erhebung der Menschenseele in die Geschichte hineingebracht worden wäre."
      ],
      [
        "Nun darf niemand glauben, daß diese beiden Vorträge, die ich heute und am Sonnabend zu halten habe, bestimmt sein sollen, irgendwie den Fleiß und die Emsigkeit der eben"
      ],
      [
        "nur flüchtig skizzierten Arbeiten herabzusetzen.",
        "Wer die Dinge kennt, die so verwendet worden sind als geistige Hilfsmittel, die Bibel in kleine Stücke zu zerreißen und als kleine Stücke zu erklären, dem zeigen sich der Fleiß und die Regsamkeit und die Förschergeschicklichkeit bei der ganzen Arbeit.",
        "Sie zeigen sich dem, der es versteht, als das Gewal­tigste, was vielleicht in der Wissenschaft geleistet worden ist.",
        "Nicht in bezug auf das Formale, nicht in bezug auf das Emsige des Forschens läßt sich etwas Gleiches finden.",
        "Wenn man nun das etwas näher betrachtet, was als Folge dieser Forscherarbeit, die von den modernen Theologen geleistet worden ist, also gerade von denjenigen, die vermöge ihres Berufes fest glauben, auf dem Boden des Christentums zu stehen, so müssen wir uns sagen: es muß dazu führen, das Verhältnis der Bibel ganz anders zu gestalten als es durch Jahrhunderte hindurch war.",
        "Wenn diese Forschung ihre Früchte trägt, wird die Bibel nicht mehr sein können.",
        "Es würde viel dazugehören, die Bibel im einzelnen zu begrün­den, es würde aber die Bibel nicht mehr sein können das Dokument, das den Menschen tröstet und aufrichtet in den traurigsten Angelegenheiten des Lebens."
      ],
      [
        "Dazu kommt noch etwas anderes, nämlich, daß für zahl­reiche Menschen, die sich umgesehen haben im Bereiche der naturwissenschaftlichen Forschung, die sich umgesehen haben in der Geologie, in der Entwickelungsgeschichte des Pflan­zen-, Tier- und Menschenlebens, umgesehen haben in der Kulturgeschichte, in der Anthropologie und so weiter, daß für diese Menschen kaum noch eine Möglichkeit vorhanden ist, sich bei dem, was sie in der Bibel lesen, etwas zu den­ken.",
        "Man muß auch in dieser Beziehung gerecht sein und sich nicht einfach auf den Böden des naiven Glaubens stel­len und das sagen, was nichts zu bedeuten hat.",
        "Es sind oft diejenigen, die am gewissenhaftesten sind in ihrem Wahrheitsgefühl,"
      ],
      [
        "in ihrem Erkenntnisdrang, die sich sagen: Wenn ich durch die auf sicherem Boden stehende Forschung sehe, wie sich die Erde entwickelt hat durch geologische Perioden hindurch, wie wir gewisse Hypothesen für die Sache haben, wie die Astronomie zeigt, wie sich die Erde aus einem Nebel von höherer Temperatur heraus zu der heutigen Ge­stalt entwickelt hat, wie sich das Unlebendige herausent­wickelt hat und aus diesem Unlebendigen die lebendige Wesenheit, wie sich nach und nach alles von dem Einfachen bis zum Kömpliziertesten, dem Menschen, entwickelt hat, wie die Kulturformen zu den heutigen komplizierten For­men aufgestiegen sind, wenn wir sehen, was die Geologie zeigt, welche gewaltigen Zeiträume nötig waren, um die Erde zu erhalten in einer Zeit, als sie noch nicht Amphibien, noch nicht Säugetiere hervorgebracht hatte, wenn wir das alles überblicken und auf uns wirken lassen - so sagen uns zahlreiche Persönlichkeiten -, was sollen wir da machen, wenn uns die Bibel erzählt, daß in sechs bis sieben Tagen die Welt erschaffen worden sein soll?",
        "Weder mit der Schöp­fung in sechs bis sieben Tagen noch mit irgend etwas an­derem können wir etwas anfangen."
      ],
      [
        "Was können wir an­fangen mit der Sintflut, mit der wunderbaren Rettung des Noah, wenn wir lesen, daß Noah so viele Tiere in die Arche gebracht hat, und so weiter? - So kommt es, daß manche mit Würde und ernstem Wahrheitssinn begabte Menschen jene scharfe und schneidige Opposition gegen die Bibel energisch vertreten, die sich von dem heutigen naturwissen­schaftlichen Standpunkte aus ergibt, insofern sie sich zu einer Weltanschauung erweitern will.",
        "Das alles ist in un­serer Weltanschauung vorhanden."
      ],
      [
        "Das alles können wir nicht wegleugnen."
      ],
      [
        "Nun entsteht aber die Frage: Sind wirklich alle die Dinge berücksichtigt, die der Bibel gegenüber zu berück­sichtigen"
      ],
      [
        "sind, wenn entweder der erste historische oder der zweite naturwissenschaftliche Standpunkt geltend gemacht wird?",
        "Da muß gesagt werden, daß es heute schon einen dritten Gesichtspunkt gibt gegenüber der Bibel, einen Ge­sichtspunkt, der sich aus jener realen Forschungsmethode und menschlichen Anschauungsweise heraus entwickelt, die in diesen Vorträgen als die geisteswissenschaftliche oder anthroposophische charakterisiert wird.",
        "Mit diesem Ge­sichtspunkte gegenüber der Bibel haben wir uns heute und übermorgen zu befassen.",
        "Was ist dies für ein Gesichtspunkt?",
        "Man sagt heute vielfach, der Mensch dürfe sich nicht auf eine äußere Autorität stützen, er müsse voraussetzungslos an die Welt und an das Leben herangehen und die Wahr­heit erforschen.",
        "Man glaubt gerade die Bibel zu treffen, wenn man sich auf einen solchen Gesichtspunkt begibt.",
        "Trifft man in Wahrheit damit die Bibel?",
        "Es läßt sich das­jenige, was der geisteswissenschaftliche oder anthroposophi­sche Standpunkt der Bibel gegenüber ist, unbedingt ver­gleichen mit etwas, was sich vor einigen Jahrhunderten in bezug auf etwas anderes, wenn auch minder Bedeutendes, für die Menschheit zugetragen hat.",
        "Wir werden uns am leichtesten verständigen können über den geisteswissen­schaftlichen Gesichtspunkt der Bibel gegenüber, wenn wir einen Vergleich mit der Umwälzung in bezug auf die An­schauung von der Erde machen."
      ],
      [
        "Da sehen wir das ganze Mittelalter herauf, in allen Schulen, niederen und höheren, das, was in bezug auf die äußere Natur gelehrt worden ist, wir sehen den Kampf in alten Schriften, allerdings in Schriften einer großen und ge­waltigen Persönlichkeit, in den Schriften des alten griechi­schen Philosophen und Naturwissenschaftlers Aristoteles.",
        "Also, wenn Sie mit mir zurückgehen könnten an die Stätten des Geisteslebens der älteren Zeit, so würden Sie finden,"
      ],
      [
        "daß nicht vorgetragen wurde in den Schulen und Gelehr­ten-Lehrstätten, was in den Laboratorien gefunden worden ist, sondern das, was auf Grund der Autorität der Bücher des Aristoteles gedruckt war.",
        "Aristoteles ist die Bibel der Naturwissenschaft.",
        "Und überall, wo man darüber vortrug, da erklärte man nur das, was Aristoteles über die Dinge schon gesagt hatte.",
        "Nun kamen die Zeiten, in denen eine neue Morgenröte heranbrach in bezug auf das Neue und Neueste von Kopernikus, Kepler und Galilei und allen an­deren bis auf den heutigen Tag.",
        "Was war der Grundnerv dieser Morgenröte?",
        "Während man vorher den Aristoteles als festen Ausgangspunkt genommen hatte, und so wie er gesprochen hat über die Natur sprach, wendeten nun Ko­pernikus, Kepler und Galilei ihren eigenen Beöbachtungs­und Forschungssinn an.",
        "Sie schauten selbst in die Natur hinaus und untersuchten, was das Leben ihnen zeigen konnte.",
        "So wollten sie die Natur beschreiben und erklären nach dem, was sie selbst gesehen hatten.",
        "Da kamen sie in manchen Widerspruch mit dem, was die streng Aristoteles-Gläubigen lehrten."
      ],
      [
        "Es ist mehr als eine bloße Anekdote, es bezeichnet die tiefe Wahrheit eines Prozesses, der sich damals abgespielt hat, wenn erzählt wird, daß ein Aristoteles-Gläubiger auf­gefordert wurde, sich doch einmal am menschlichen Körper selber anzusehen, daß es nicht richtig ist, daß die Nerven vom Herzen ausgehen, sondern daß sie vom Gehirn aus­gehen.",
        "Da ließ sich der Aristoteles-Gläubige bewegen, sich das anzuschauen.",
        "Dann sagte er aber: Wenn ich das an-schaue, dann scheint es, daß die Natur dem Aristoteles wi­dersprechen würde.",
        "Aber wenn die Natur dem Aristoteles widerspricht, so glaube ich nicht der Natur, sondern dem Aristoteles. - So stand die Naturwissenschaft gegenüber der Tradition.",
        "Die Anschauung des Forschers und Sehers"
      ],
      [
        "wurde gegenüber dem, was als Tradition durch Jahrhun­derte sich fortgepflanzt hatte und nachgesprochen worden ist, abgelehnt.",
        "Wenn wir die Schriften Giordano Brunos lesen, sehen wir die Opposition gegenüber Aristoteles aus dem neuen Geist, der erzählt und erklärt, was der Mensch selber sehen sollte."
      ],
      [
        "Heute stehen wir der ganzen Sache schon wieder anders gegenüber.",
        "Wir stehen anders gegenüber der unmittelbaren naturwissenschaftlichen Beobachtung und auch gegenüber Aristoteles.",
        "Wir wissen, daß vieles von dem, was im Mittel­alter aus ihm herausgelesen worden ist, nur mißverständ­liche Auslegung war.",
        "Aus dem Geiste seiner Zeit heraus sagte ein Forscher, der unmittelbar hineinblickte in die Natur und das wiedergab, was er zu sehen verstand: Wenn wir Aristoteles richtig verstehen, werden wir eingehen kön­nen auf das, was er sagt.",
        "Dann erscheint er uns nicht mehr in jenem Widerspruch, in dem er zu stehen schien für die damalige Zeit, zur unmittelbaren wissenschaftlichen Be­obachtung.",
        "Dann können wir wieder seine Bewunderer werden.",
        "Denn selbst bei der Tatsache des Ausgangs der Nerven vom Herzen statt vom Gehirn zeigt es sich, daß er etwas ganz anderes gemeint hat, nämlich etwas, das selbst für unsere Zeit noch richtig ist."
      ],
      [
        "In einer ganz ähnlichen Art steht die Geistesforschung oder besser die geisteswissenschaftliche Forschung nicht nur zu diesen Dokumenten, sondern auch zu dem abendländi­schen Urdokument, zur Bibel.",
        "Was sich im sechzehnten Jahrhundert und seitdem in bezug auf die Beobachtung und Erforschung der äußeren Natur abgespielt hat, das spielt sich heute wieder ab in bezug auf die geistigen Untergründe der Welt.",
        "Aus dem Geiste jener Forschung heraus, die in den drei letzten Vorträgen charakterisiert worden ist, sucht die Menschheit wieder einzudringen in diejenigen Welten,"
      ],
      [
        "die nicht mit den äußeren Sinnen wahrnehmbar sind, die aber wahrnehmbar sind für die höher entwickelten Sinne des Menschen, für die geistigen Sinne des Menschen, durch die wir ebenso in die geistige Welt hinein sehen können, wie wir durch die physischen Sinne in die physische Welt hinein sehen können."
      ],
      [
        "Es braucht hier nicht weiter ausgeführt zu werden, weil es ja schon öfter gesagt worden ist, daß der Mensch fähig ist, in sich die Kräfte zu entwickeln, daß er nicht nur die sinnlichen Dinge wahrnehmen kann, sondern daß er zwi­schen und hinter dem Sinnlichen eine geistige Welt wahr­nehmen kann, eine geistige Welt, die viel realer ist als die sinnliche Welt.",
        "Es hatte seinen guten Grund, daß die Menschheit eine Weile die Methode der geistigen Forschung vergaß.",
        "Die großen Fortschritte, die großen Eroberungen in der physischen Welt wurden gemacht dadurch, daß die Instrumente so vervollkommnet wurden, wie es im letzten Jahrhundert der Fall war.",
        "Aber wenn das eine in der menschlichen Natur sich vergrößert, dann treten andere Fähigkeiten in den Hintergrund.",
        "So sehen wir, wie in dem letzten Jahrhundert die naturwissenschaftlichen Methoden für die äußere physische Tatsachenwelt aufblühten.",
        "Nie­mals sind in der großartigen Weise mehr Instrumente ge­funden worden, um der Natur die Geheimnisse abzulau­schen und ihre Gesetze zu erforschen.",
        "In ungeheurer Weise sind die Fähigkeiten, die Bezug hierauf haben, vergrößert und verfeinert worden, aber zurückgetreten sind dagegen die Fähigkeiten, durch die der Mensch hineinschauen kann in die geistige Welt.",
        "So ist es nicht zu verwundern, wenn der Mensch zu dem Glauben gekommen ist, daß alles mate­riell ist, und daß das Materielle stofflich da sein muß, aus dem uns auch das Geistige erklärt werden kann."
      ],
      [
        "Aber wir stehen in der heutigen Zeit vor dem Einbruch"
      ],
      [
        "einer Epoche, wo es der Menschheit wieder zum Bewußtsein kommt, daß es auch noch andere Instrumente und Werk­zeuge gibt, als diejenigen im physikalischen und physiolo­gischen Laboratorium, wo sie in so ausgezeichneter Weise benützt werden.",
        "Allerdings haben wir es zu tun mit einem Instrument, das sich gründlich unterscheidet von den an­deren."
      ],
      [
        "Wir haben es mit dem Grund- und Ur-Instrument zu tun, das wir im Menschen selbst zu erblicken haben.",
        "Der Mensch ist es, den wir im Laufe des Winters durch die Methoden der Konzentration und der Meditation kennen­lernen werden."
      ],
      [
        "Das sind andere Methoden, die der Mensch auf seine Seele anwenden kann, und durch die er dazu kommt, daß er die Umwelt in einer ganz anderen Weise sieht als er sie vörher gesehen hat.",
        "Er kann dazu kommen, daß er sich sagen kann: Ich bin wie ein operierter Blind-geborener, der vorher ableugnen konnte die Farben und das Licht der Welt. - Eingetreten ist aber für ihn nun der Moment, daß er selber sehen konnte."
      ],
      [
        "Er konnte nun sehen, daß zwischen dem, was die Sinne und der Verstand wahr­nehmen, noch etwas anderes ist.",
        "Jetzt sieht er hinein in die geistigen Dinge; jetzt weiß er, nicht hypothetisch, nicht durch spekulative Philosophien, sondern wie sinnlich, daß das Stoffliche nur wie eine Verdichtung ist des Geistigen, daß das, was wir mit den Sinnen sehen, sich so zu einem Geistigen hinter ihm verhält, wie sich Eis zu Wasser ver­hält."
      ],
      [
        "Das Wasser ist dünn, das Eis ist fest, und der, welcher das Wasser nicht sehen könnte, aber das Eis sehen kann, der würde sagen: Es ist nichts um das Eis herum da. - So sagt der, welcher nur mit den Sinnen sehen kann, es gebe nichts in weitem Umkreis als sinnliche Vorgänge, nichts als sinnliches Geschehen."
      ],
      [
        "Wir müssen aber vordringen in dieses übersinnliche Ge­biet, in dieses übersinnliche Geschehen, dann können wir"
      ],
      [
        "auch das Geistige erkennen und erklären.",
        "Wer sich also keine geistigen Ohren und Augen ausgestaltet hat, der sieht in der ganzen Welt nichts als eine Verdichtung wie Eis im Wasser, und es erscheint ihm nicht die Urmutter-Substanz, das Geistige, in dem das Sinnliche nur eingebettet ist.",
        "Wenn uns der Geologe zeigt, wie etwa ein Mensch sich befindet, der in die Welt hinein einen Stuhl setzen könnte und schauen könnte, wie sich die Welt entwickelt hat: Der äußere sinnliche Anblick würde ein solcher sein, wie die Naturwissenschaft es schildert.",
        "Gegen das, was die Natur-wissenschaft im positiven Sinne zu sagen hat, hat die Gei­steswissenschaft nichts einzuwenden.",
        "Aber es zeigt sich dem, der da in richtiger Art in der Naturwissenschaft Bescheid weiß, daß vor dem ersten Entstehen des Physischen das Geistige da war.",
        "Da zeigt sich, wie der Fortschritt nur mög­lich wurde dadurch, daß das Geistige dazwischen mitwirkte, und daß am meisten der Geist an der Entwickelung be­teiligt ist."
      ],
      [
        "So weist uns diese geistige Weltanschauungsströmung darauf hin, daß es möglich ist, daß der Mensch sich zum Instrumente macht für die Erforschung der wichtigen Grundlagen der Welt, und so kommt unsere Anschauung endlich dazu, die geistigen Urgründe und Anfänge in uns selbst zu erforschen.",
        "So stehen sie da, unabhängig von jedem Dokument.",
        "Zunächst sagt die Geisteswissenschaft: Wir for­schen zunächst nicht in einem Dokumente.",
        "Wir forschen nicht wie einst Aristoteles in der geistigen Welt.",
        "Wir stellen uns so ein: Dasjenige, was Sie als gewöhnliche Schulgeome­trie lernen, die Euklidsche Geometrie, sie wurde in ihren ersten Anfängen durch Euklid, den großen Mathematiker, niedergeschrieben.",
        "Wir können das Dokument heute neh­men und es historisch auffassen.",
        "Aber wer heute in der Schule Geometrie lernt, lernt der noch nach dem Elementarbuche"
      ],
      [
        "des Euklid?",
        "Man ahnt, lernt und erkennt an den Dingen selber.",
        "Man konstruiert sich zum Beispiel ein Drei­eck im Geiste, und es zeigen sich dann durch die innere Gesetzmäßigkeit die Gründe, wie die Sache ist.",
        "Dann kön­nen Sie mit dem, was Sie so aus sich selbst gewonnen haben, an Euklid herantreten und erkennen, inwiefern das schon erreicht war, was Euklid in seinem Buche verzeichnet hat.",
        "So forscht der Geisteswissenschaftler unabhängig von Büchern durch seine Organe, wie sich die Welt entwickelt.",
        "Und er findet so die Entwickelung der Welt, der Erde und der Zeit, bevor die Erde sich herauskristallisiert hat.",
        "Er erforscht die geistigen Vorgänge und findet, wie an einem bestimmten Punkte unser Geist im Dasein einsetzt; er zeigt, wie der Mensch als erster auftritt und nicht sich entwickelt hat aus untergeordneten Geschöpfen, allerdings als Nachkomme geistiger Wesenheiten, die zuerst da waren."
      ],
      [
        "Wir können zurückgehen in frühere Zeiten, wo noch die geistigen Urgründe waren.",
        "Wir finden da den Menschen mit diesen geistigen Vorgängen verknüpft, und erst später ent­wickeln sich zu dem Menschen hinzu die niederen Geschöpfe, so wie in der Entwickelung überhaupt gewisse Dinge zu­rückbleiben und andere sich herausentwickeln.",
        "Das Niedere ist von dem Höheren abgezweigt, abgegangen.",
        "Der Geistes-forscher weiß, daß die Organe sich entwickeln können durch Methoden, die der Geistesförscher zu zeigen vermag.",
        "So lehrt die Geistesforschung eine Weltentstehung und ein Wer­den von Gesetzen unabhängig von jedem Dokumente, aus der eigenen Gesetzmäßigkeit heraus, auch nicht gebunden an das, wie sich die Mathematik im Laufe der Geschichte entwickelt hat.",
        "Und so, wie sich der Forscher ein Wissen von der Weisheit angeeignet hat, so geht er an die Bibel heran und schaut sich jetzt die Bibel an."
      ],
      [
        "Jetzt zeigt sich uns sowohl der eine Gesichtspunkt in bezug"
      ],
      [
        "auf die historisch-kritische Widersprudisförschung, wie auch der Gesichtspunkt der naturwissensdiaftlichen Wider­spruchsforschung.",
        "Beide Gesichtspunkte kommen aus einem einzigen großen Irrtum, der dadurch entstand, daß man allgemein glaubte, die Wahrheiten der Bibel von dem phy­sisch-sinnlichen Wahrnehmungs- und dem Beobachtungs­standpunkte aus auffassen zu sollen.",
        "Man meinte damals, es sei möglich, mit solchen Maßstäben an die Bibel heran­zutreten.",
        "Man hatte noch nicht die Forschungsergebnisse der anthropösophischen Geisteswissenschaft."
      ],
      [
        "Es soll jetzt an einzelnen Beispielen gezeigt werden, was eben gesagt worden ist.",
        "Die Geisteswissenschaft zeigt uns, daß zunächst die irdischen Geschöpfe das nächste sind, was um uns ist, daß wir aber mit dem, was in der Geologie und so weiter ist, nur bis zu einem gewissen Punkte kommen, und daß dann die Menschheitsentwickelung ins Unbestimmte nach rückwärts verläuft.",
        "Und warum?",
        "Niemals, soviel sie auch hoffen mag, wird die sinnliche Wissenschaft den Men­schen bis zum Ursprunge verfolgen können, aus dem Grunde, weil die sinnliche Wissenschaft nur das Sinnliche finden kann.",
        "Aber dem Sinnlichen im Menschen ist das Seelische und Geistige vorangegangen.",
        "Der Mensch war zuerst Seele und noch früher Geist, und er ist dann heruntergestiegen in das Erdendasein.",
        "Nur insofern der Mensch sich an dem Herunterstieg in das Erdendasein beteiligt hat, kann uns die Naturwissenschaft ihn im Niedergange zeigen.",
        "Das seelische Leben können wir nicht mit den gewöhnlichen Kräften der sinnlichen Beobachtung erforschen.",
        "Auch die Geologie kann uns keinen Leitfaden bieten.",
        "Sie bietet uns das, was zurückgeblieben ist an sinnlichen Materien.",
        "Sie kann also auch nur angeben, was man heute nicht sehen kann, aber sehen würde, wenn man einen Stuhl in das Welt­all setzen könnte und dann alles sehen würde.",
        "Darauf geht"
      ],
      [
        "die Geisteswissenschaft nicht ein.",
        "Aber um den Menschen in urferner Vergangenheit als Geistwesen zu sehen, dazu muß man die geistigen Augen und die geistigen Ohren entwickelt haben.",
        "Hat man diese nicht, dann verschwindet der Mensch.",
        "Hat man aber die geistigen Augen, dann verschwindet das Sinnliche, und es ersteht das geistige Bild.",
        "Das kann man aber nicht in derselben Weise sehen wie das Sinnliche.",
        "Man muß sich ganz andere Begriffe über das Erkennen aneignen, wenn man in solche Urzeiten zurückgehen will.",
        "Was man da vom Menschen sich entwickeln sieht, als er erst Seele war, das zeigt sich nicht in sinnlichen gegenständlichen Wahr­nehmungen wie die äußere Sinneswelt sie bietet.",
        "Das zeigt sich uns in Bildern.",
        "Unser Bewußtsein wird durch die Ent­wickelung der inneren Kräfte der Seele das, was wir ein Bilderbewußtsein, ein imaginatives Bewußtsein nennen.",
        "Es ist dann das Bewußtsein ausgefüllt mit Bildern.",
        "Wir sind in einem anderen Bewußtseinszustande.",
        "Was sich damals ab­gespielt hat, das spielt sich jetzt in Bildern ab.",
        "Bildhaft ist das, was so im Inneren des Sehers vorgeht."
      ],
      [
        "Das Rudiment, das von der Sehergabe noch vorhanden ist, das ist der Traum.",
        "Der ist aber chaotisch.",
        "Das Sehen des ausgebildeten Sehers ist auch in solchen Bildern vorhanden, aber es entspricht der Wirklichkeit.",
        "Es ist ähnlich dem, wie der physisch-sinnliche Mensch unterscheiden kann, ob seine Vorstellungen der Wirklichkeit entsprechen oder nur eine Phantasie sind.",
        "Wer bei dern Satze stehenbleiben will: «Die Welt ist meine Vorstellung» und «Die äußeren Dinge regen nur die Vorstellung an», dem möchte ich zu erwägen geben, er soll sich ein Stück glühendes Eisen bringen lassen, es in seine Nähe bringen und fühlen, wie es brennt.",
        "Er soll es dann wegnehmen und fühlen, ob die bloße Vorstellung auch noch so brennt.",
        "Es gibt eben etwas, was die bloße Vorstel­lung unterscheidet von der Wahrnehmung, die durch den"
      ],
      [
        "äußeren Gegenstand angeregt ist.",
        "Man darf daher nicht sagen, daß der Seher nur in Phantasmen lebt.",
        "Er hat eben auf diesem Felde sich so entwickelt, daß er unterscheiden kann, was Phantastik ist, was bloßes Bild oder Wirklichkeit ist für eine geistig-seelische Welt.",
        "So werden die Bilder das Ausdrucksmittel für eine geistig-seelische Welt.",
        "Der Seher blickt zurück in jene Zeit, die sich ihm in sinnlichen Gegen­ständen darstellte.",
        "Ebenso stellen sich bei ihm die wahren geistigen Wesenheiten und Begebenheiten den übersinnlichen Wahrnehmungsorganen dar.",
        "Der Geistesforscher spricht nicht von Kräften, die Abstraktionen sind, sondern von wirklichen Wesenheiten.",
        "Für ihn werden die geistigen Er­scheinungen zu Wahrheiten und zu Wesenheiten, und für ihn bevölkert sich die geistige Welt wieder mit geistigen Wesenheiten."
      ],
      [
        "Nun stellen Sie sich den Menschen vor in seiner vorzeiti­gen Entwickelung, als eine Wesenskraft eingegriffen hat in seine ganze Evolution, in seine Gestalt, eine Wesenheit, die sich unterscheidet, ganz genau unterscheidet von anderen Wesenheiten, die früher eingegriffen haben, denn wir kön­nen das Geistig-Seelische des Menschen, das schon im Über-sinnlichen ist, noch weiter zurück verfolgen.",
        "Wir können es in noch höhere Sphären zurück verfolgen.",
        "Dann aber muß der Geistesforscher, wenn er in diese höheren Sphären kommt, in diesen höheren Sphären lebt, und wenn er von geistigen Wesenheiten spricht, auch von anderen geistigen Sphären sprechen."
      ],
      [
        "Nun tritt der Geistesförscher an den Anfang der Bibel heran.",
        "Da zeigt sich ihm, daß mit wunderbarer Treue die Bilder gegeben sind, die uns das Seelisch-Geistige in der Entwickelung des Menschen darstellen, bevor er in das phy­sische Leben herausgetreten ist.",
        "Der Geistesforscher kann, wenn er seine eigenen Imaginationen, die er in seinem Inneren"
      ],
      [
        "hat, dann in den äußeren Dokumenten wieder findet, sich sagen, daß er diese in Wahrheit erkennt.",
        "Wenn er nun zurückgeht in die Zeiten, wo der Mensch den noch höheren Sphären angeschlossen war, da muß er für diese Grund­wesen einen anderen Namen wählen, und er findet, daß die Kapitel, die dem vierten Vers des zweiten Kapitels voran­gehen, tatsächlich einen anderen Göttesnamen haben.",
        "Genau mit den Ergebnissen der Geistesförschung stimmt es über­ein, daß vom vierten Vers des zweiten Kapitels an für die Darstellung der Urwelten-Entwickelung ein neuer Gottes­name auftritt.",
        "So sehen wir uns mit der Geistesforschung in der Lage, in der sich heute ein Kenner der Geometrie befin­det.",
        "Er kann Geometrie aus sich finden, und dann weiß er das Werk des Euklid zu schätzen, der dasselbe gefunden hat.",
        "So sehen wir die Entwickelung in den wunderbaren Bildern des Alten Testamentes, und jetzt zeigt sich uns etwas höchst Merkwürdiges.",
        "Licht und hell wird es über dem Texte der Bibel, wie es nicht heller licht werden konnte bei dem wissenschaftlichen Kritiker."
      ],
      [
        "Ein Forscher sagt: Was die Elohim hat, das muß von einer anderen Seite herrühren als das, was von Jahve her­kommt.",
        "Wenn man das im Ernste anwenden will, dann ist es sonderbar.",
        "Wir wollen es einmal versuchen.",
        "Stellen wir uns dieses Bild einmal vor.",
        "Die Schlange war listiger als alle Tiere, die Gott der Herr gemacht hatte und spricht zu dem Weibe: Hat euch nicht Gott gesagt, ihr sollt nicht essen von dem Baume des Gartens. - Wenn nun statt Elohim und Jahve nur «Gott» steht, so ist es sonderbar.",
        "Die Schlange war listig, die Gott Jahve gemacht hat.",
        "Sollte Gott gesagt haben: Ihr sollt nicht essen? - Es steht nicht Jahve, sondern «die Elohim».",
        "Nun fährt das Weib fort und erklärt immer so, daß sie von Gott spricht.",
        "Und im achten Vers heißt es weiter: Und sie hörten die Stimme Gottes, des Herrn -"
      ],
      [
        "Aber es heißt im Urtext: die Stimme des Jahve.",
        "Nun hätten wir die Geschichte der Schlange zusammengestellt, so daß erklärlich wird, daß die, welche die Namen Jahve, Elohim gebraucht haben, eine andere Wesenheit meinen.",
        "Das rührt von der einen Tradition her.",
        "Und von der Elohim-Tradi­tion rührt es her: Wie?",
        "Sollte Gott gesagt haben, ihr sollt nicht essen? - Sie sehen, es wird wirklich aus Lappen die Bibel so zusammengesetzt, daß mitten in den Sätzen dann die Traditionen zusammengenommen werden müssen."
      ],
      [
        "Gehen Sie mit geisteswissenschaftlicher Forschung an die Bibel heran, dann zeigt sich Ihnen, daß dies auch so stehen kann.",
        "Es ist die Rede von dem vierten Vers des zweiten Kapitels an, daß die Weltschöpfung von den Elohim an den Jahve übergeht.",
        "Er ist also die Macht, die dasjenige zur Entwickelung bringt, was dann bis zum Sündenfall zur Entwickelung kommt.",
        "Die Geisteswissenschaft zeigt Ihnen dann, daß der Jahve derjenige Gott ist, der in das Innere der Menschen hinein spricht das, was wir als das Ich haben, das Ich-bin.",
        "Diese Wesenheit, die Ich-bin-Wesenheit, ist es, die alles das bewirkt, was vom zweiten Kapitel, vierter Vers, an gesagt wird.",
        "Die Wesenheit, die jetzt eingreift, ist das, was Jahve ist, eine Wesenheit, die einer früheren Ent­wickelung angehört, aber nur abgefallen ist.",
        "Sie bekommt nicht den Zugang.",
        "Daher ist die Rede von Gott-Jahve.",
        "Die Schlange aber weiß nichts von Jahve; sie muß sich daher wenden an das, was von ihrem eigenen Stoffe ist, in dem Momente, wo eintritt das, was gerade durch Jahve eintreten muß.",
        "Also im achten Vers tritt wieder der Name des Jahve ein."
      ],
      [
        "So erwirbt man sich durch die Geistesforschung ein Be­wußtsein, das Bewußtsein, daß die Bibel eine Urkunde ist, in der nichts, auch gar nichts bloß zufällig steht.",
        "Mag sich ein moderner Schriftsteller wundern - es sind nicht solche"
      ],
      [
        "Sippen von modernen Schriftstellern, wie sie bei den alten Eingeweihten waren - und sagen: Warum sollte nicht ein­mal dieser Gott einen anderen Namen annehmen?",
        "Wo ge­nau und korrekt gesprochen werden soll, wird nicht in stilistischer Form geredet.",
        "Was dasteht und was weggelas­sen ist, hat seine Bedeutung.",
        "Wenn der Name Jahve auf-tritt, und wenn er weggelassen wird, so bedeutet das etwas höchst Wesentliches.",
        "Aber man muß den Grundsatz durch­führen, daß die Bibel höchst genau zu lesen ist.",
        "Lesen Sie die Bibel, wenn Sie sie haben!",
        "Lesen Sie das Sechs-Tage-Werk durch und Sie finden, daß es so aufgefaßt wird, daß der erste Vers zum zweiten Kapitel fortgelassen wird bis zum Sabbat, und dann kommt also, daß Gott der Herr Himmel und Erde machte.",
        "Diese Verse rechnet man ge­wöhnlich als eine Hindeutung auf das Vorherstehende.",
        "So, wie wenn das Sieben-Tage-Werk erzählt worden wäre, und noch gesagt wird: So ist es gemacht worden, das Sieben-Tage-Werk, dies ist die Entstehungsgeschichte Himmels und der Erde, und dann soll es weitergehen."
      ],
      [
        "Wer hier den Urtext studiert, der kommt auf das Fol­gende: der vierte Vers des zweiten Kapitels bezieht sich nicht auf das Vorhergehende, sondern auf das Nachfol­gende, geradeso, wie sich später auf das Nachfolgende be­zieht dieses Sündengeschlecht des Adam, auf das Hinterher, auf die folgende Generation, auf dasjenige, was aus Adam entstanden ist.",
        "Da wird in derselben Weise gesagt: Was da folgt, das sind die Geschlechter des Himmels und der Erde."
      ],
      [
        "- Im Hebräischen steht auch dasselbe Wort.",
        "Wer genau liest, der weiß das Folgende: daß von den Worten an «Im Anfang schuf Gott Himmel und Erde» bis zum dritten Vers des zweiten Kapitels die geistige Welt geschildert wird, wie sie geschaffen ist.",
        "Dann wird vom vierten Verse an gesagt:"
      ],
      [
        "Das, was Nachkomme ist von Himmel und Erde, wird im"
      ],
      [
        "Folgenden geschildert.",
        "Es ist der wunderbarste Übergang, wenn man die Sache versteht, von dem Sechs-Tage-Werke zu dem Folgenden.",
        "Wer sich auf diese Dinge einläßt, findet, daß es vielleicht kein so gut kombiniertes Buch gibt wie die Bibel, namentlich die ältesten Teile derselben.",
        "Der Glaube, daß man ohne geistige Forschung an die Bibel herantreten dürfe, daß man mit äußeren Urkunden an sie herantreten könne, das hat dieses in sich so vollkommene und harmo­nische Werk aufgelöst, so daß es aus lauter Lappen und Fragmenten zusammengesetzt erscheint."
      ],
      [
        "Man muß auch den Grundsatz, genau zu lesen, und den Grundsatz, die Bibel zu haben, noch weiterverfolgen.",
        "Man hat die Bibel nicht, wenn man nur den Wortlaut hat, der das einzelne, worauf es ankommt, nur andeutet.",
        "Man muß den Grundsatz haben, auf die Bibel einzugehen.",
        "Es wird uns an einem späteren Tage des Sechs-Tage-Werkes erzählt, wie Sonne und Mond entstehen, wie Sonne und Mond Tag und Nacht bedingen.",
        "Schon vorher wird aber von Tag und Nacht erzählt.",
        "Aus der Bibel könnte man die Folgerung ziehen: Tag und Nacht, wie sie mit Sonne und Mond zu­sammenhängen, können nicht gemeint sein mit Tag und Nacht, die von der Sonne und dem Monde abhängen.",
        "Hier könnte man einen handgreiflichen Hinweis darauf sehen, wie die Bibel von dem sinnlichen Sonnentag und der Son­nennacht spricht.",
        "Sie entstehen durch das, was wir Um­drehung der Erde um die Sonne nennen.",
        "Wir können sehen, wie die Bibel von dem sinnlichen Tag hinausweist in das, was im Übersinnlichen, im Geistigen ist, wie sie es erhöht und erweitert in das Geistige hinein."
      ],
      [
        "Diejenigen, welche die Bibel geistig erforschen konnten, waren immer in der Lage, daß sie sich sagten: Wenn einer die Sehergabe, die Gabe des höheren Schauens hat und den Sinn der Bibel in Wirklichkeit finden kann, dann ist es"
      ],
      [
        "selbstverständlich, daß dieser Sinn auch aus der Sehergabe erflossen ist. - Wenn wir dadurch, daß sich die Seele in eine andere Geistesstimmung versetzt, hineinblicken können in das, was uns in den gewaltigen Bildern der Bibel gegeben ist, dann wissen wir, daß der, welcher es geschrieben hat, auch unter der Inspiration der geistigen Welt gestanden haben muß.",
        "Wir dürfen wohl sagen: Es beginnt die Zeit, wo immer mehr begriffen werden soll, daß es viererlei Stufen gibt, wie man heute die Bibel betrachten kann."
      ],
      [
        "Die erste Stufe ist die des naiven Glaubens.",
        "Sie nimmt die Bibel in unbeirrter Sicherheit und ahnt nichts von dem, was heute als Einwendungen gegen die Bibel angeführt worden ist."
      ],
      [
        "Die zweite Stufe: Das sind die gescheiten Leute, diejeni­gen, welche entweder durch Bibelkritik, durch das Erfor­schen der inneren Widersprüche oder durch den naturwis­senschaftlichen Standpunkt finden, daß die Bibel das primi­tive Sagen- und Legendenwerk einer noch nicht forschenden Menschheit war.",
        "Sie sind hinaus über die Bibel, sie brau­chen sie nicht mehr, sie greifen sie von den verschiedensten Richtungen an und sagen: Sie ist gut gewesen für die kind­liche Menschheit.",
        "Jetzt aber wächst die Menschheit über die Bibel hinaus. - Das sind die Gescheiten, die Freidenker."
      ],
      [
        "Dann gibt es eine weitere Stufe: Der Mensch wächst über diese Gescheitheit hinaus.",
        "Die Menschen dieser Stufe sind auch Freidenker, sie sind über diesen zweiten Standpunkt der gescheiten Leute hinausgewachsen.",
        "Sie sehen in den Er­zählungen der Bibel - des Alten und Neuen Testamentes -wenigstens symbolische und mythische Einkleidungen von inneren Seelenerlebnissen.",
        "Sie sehen das, was in abstrakter Weise in den menschlichen Seelen sich darstellt, was sich in Bildern darstellt.",
        "Dazu sind manche Freidenker gezwungen worden.",
        "Sie haben den Standpunkt des freidenkerischen"
      ],
      [
        "Menschen in den Standpunkt des mythischen Symbolikers, des mythischen Darstellers verwandeln müssen."
      ],
      [
        "Dann gibt es einen vierten Standpunkt.",
        "Das ist der, wel­cherlhnen heute als derjenige der Geisteswissenschaft charak­terisiert worden ist.",
        "Übermorgen werden wir ihn weiter­verfolgen, diesen geisteswissenschaftlichen Standpunkt.",
        "Er zeigt wieder die geistigen Tatsachen in einfachen Beschrei­bungen, allerdings so, wie man diese geistigen Tatsachen in den Imaginationen sehen kann.",
        "Es sind die Tatsachen, die in der Bibel beschrieben sind.",
        "Wer den naiven Standpunkt verlassen mußte und als Forscher zum gescheiten Menschen, vielleicht zum Symboliker geworden ist, der kann dann kommen zu dem Standpunkte, auf dem der Geistesforscher steht, und er kann dann fähig werden, die Bibel wieder wörtlich zu nehmen, in einem neuen Sinne wörtlich zu neh­men, nämlich, die Worte wirklich zu verstehen."
      ],
      [
        "Während Jahrhunderten hat man eigentlich nicht die Bibel kritisiert.",
        "Man hat sein eigenes Phantasiengeschöpf bekämpft, das, was man aus der Bibel gemacht hat.",
        "So gibt cs heute noch Kämpfer gegen die Bibel.",
        "Sie kämpfen gegen ihr eigenes Phantasiengeschöpf, gegen das, was sie davon verstehen können.",
        "Die Bibel treffen sie gar nicht.",
        "Wörtlich also kann die Bibel wieder genommen werden, nur muß man das Wort richtig verstehen."
      ],
      [
        "Es ist heute eine gewisse Strömung da, die gegen ein solches Gespräch das Wort geltend machen wird: Nicht der Buchstabe, der Geist muß entscheiden; der Buchstabe tötet, der Geist macht lebendig, und Du bekennst wieder aus gewissen Beziehungen den Buchstaben."
      ],
      [
        "Ich wollte, wir könnten so bald als möglich den echten Bibelbuchstaben der Welt wieder bringen.",
        "Die Welt würde erstaunen darüber, was der Urtext enthält.",
        "Wie etwas ganz Neues wird er der Menschheit vorkommen.",
        "Mit dem Ausspruche:"
      ],
      [
        "Der Buchstabe tötet, der Geist macht lebendig -, darf man nicht so hausieren gehen.",
        "Es ist gewöhnlich der Herren eigener Geist, in dem die Buchstaben sich bespiegeln.",
        "So ist es besonders im Symbolischen.",
        "Ist er trivial, so legt er triviale Symbole; ist er geistreich, so legt er geistreiche Symbole hinein.",
        "Es ist mit diesemWort wie mit demSpruche von Goethe:"
      ],
      [
        "Und solang du das nicht hast,"
      ],
      [
        "Dieses: Stirb und Werde!"
      ],
      [
        "Bist du nur ein trüber Gast"
      ],
      [
        "Auf der dunklen Erde."
      ],
      [
        "Dieses Wort deutet uns an, wie der Mensch hinauskom­men soll über die sinnliche Anschauung, überhaupt über die gewöhnliche Natur.",
        "Wer dieses Wort als eine Anweisung dazu nehmen würde, daß er sich sagt, das Physische habe keinen Wert, der hat übersehen, daß der Geist nach und nach sich aus dem Physischen herausentwickelt.",
        "So ist es auch mit dem Buchstaben und dem Geist.",
        "Erst muß man den Buchstaben haben, dann ihn enträtseln können, und dann wird man finden, welches der Geist ist.",
        "Gewiß, der Buchstabe tötet, aber er erschafft in seinem Tode den Geist, und es entspricht dieser Ausspruch dem anderen: Wer das nicht hat, dieses Stirb und Werde, der bleibt nur ein trüber Gast auf der dunklen Erde."
      ],
      [
        "Nur in den Prinzipien könnte ich Sie heute auf die Kritik der Bibel aufmerksam machen und auf die Gesichtspunkte, welche die Geisteswissenschaft gegenüber der Bibel ein­nehmen wird.",
        "Aus den wenigen Andeutungen, die heute gefallen sind, wird man wenigstens erahnen können, daß durch die Arbeit der Geisteswissenschaft sich wird voll­ziehen können etwas wie eine Wiedereroberung der Bibel.",
        "Weisheit soll die Geisteswissenschaft finden, unabhängig"
      ],
      [
        "von der Bibel.",
        "Aber dann kommt die Geisteswissenschaft und erkennt, was in diese Bibel hineingeflossen ist, und dann erlebt man, was viele aus der Geisteswissenschaft heraus gegenüber der Bibel erlebt haben.",
        "Einiges hat sie erbauen können, das meiste aber hat für sie keinen Sinn mehr.",
        "Dann kommen sie durch die Geisteswissenschaft darauf, was mit diesem und jenem gesagt wird.",
        "Dann stehen da aber noch andere Stellen, die recht anfechtbar zu sein scheinen.",
        "Man kommt dann zu dem Standpunkte, zu sagen: Es sind in der Bibel Stellen enthalten, die tiefe geisteswissenschaftliche Wahrheiten enthalten, aber es ist manches hineingeflossen, was als etwas Unorganisches hineingegliedert worden ist. -Dann geht man weiter, macht wieder eine Entdeckung und findet, daß es an einem selbst gelegen hat, nämlich daran, daß man nicht weit genug war, die Sache zu verstehen.",
        "Und man gelangt dahin, sich zu sagen: Wo man früher geglaubt hat, der Sinn scheine gegen­über der Weisheit nicht haltbar zu sein, da sieht man jetzt, das eine verstehst Du, daß Du die Bibel mit Vertrauen und Verehrung betrachten mußt; das andere verstehst Du eben noch nicht.",
        "Aber es wird die Zeit kommen, daß Du es ver­stehen wirst, und Du wirst wieder den Standpunkt finden, wo Du selbst hineinschauen kannst."
      ],
      [
        "Die Geisteswissenschaft wird zur richtigen Schätzung der Bibel führen.",
        "Die Geisteswissenschaft ist heute erst am Beginne ihrer Schöpfung.",
        "Die Bibel hat eine Krisis, eine Kritik durchzumachen.",
        "Die Forschungen der Geisteswissen­schaft werden ihr entgegenkommen, und in neuer Gestalt wird das alte Licht durch das Geistesleben in der Zukunft der Menschheit leuchten."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "BIBEL UND WEISHEIT II Berlin, 14. November 1908",
    "paragraphs": [
      "BIBEL UND WEISHEIT",
      "Berlin, 14. November 1908",
      "Daß die Geisteswissenschaft in der Lage ist, die tieferen Weisheiten und Wahrheiten der biblischen Urkunden zu er-forschen und dadurch erst die Möglichkeit hat, im richtigen Sinne wiederum dasjenige zu lesen, was in dieser Urkunde steht, das sollte im vorgestrigen Vortrage mit einigen Stri-chen angedeutet werden. Und mit einigen groben Strichen solhe gezeigt werden, wie gegenüber dem Alten Testamente ein solches richtiges Eindringen in den tieferen Sinn der Bibel in einer ganz unerwarteten Art möglich ist und viele Menschen zu einer Wiedereroberung dieser Urkunde für die Menschheit führen kann. Dasjenige, was in diesem letzten Vortrage gesagt werden konnte über die Stellung unserer neueren Zeit, ihre Forschung, ihre Kritik, ihre Weltanschau­ung gegenüber dem Alten Testament, das kann in einer ebensolchen Weise gesagt werden in bezug auf das Neue Testament. Auch hier sind wir wieder in der Lage, darauf hinzuweisen, wie im siebzehnten, achtzehnten Jahrhundert eine Kritik einsetzte, welche das Evangelium, also wiederum eine Urkunde, die durch Jahrhunderte hindurch für unzäh­lige Menschen eine so gewaltige Bedeutung hat, zerfasert, zergliedert, sozusagen in Stücke zerschnitzelt und an der Wurzel die Autorität angreift. Es müßte eine lange Ge­schichte erzählt werden, wenn aufmerksam gemacht werden sollte auf diese Bibelkritik des Neuen Testamentes im ein­zelnen. Wie konnte es auch anders kommen, da seit jener Zeit, nach der Erfindung der Buchdruckerkunst, die Bibel",
      "in alle Hände gekommen ist, und als gleich damit das mate­rialistische Denken überhand nahm! Wie konnte es anders kommen, als daß immer deutlicher und deutlicher den Men­schen vor die Seele trat, daß sich Widersprüche in dem Evangelium finden?",
      "Man braucht nur, wenn man sich rein an den äußeren Buchstaben der Sache hält, zum Beispiel das erste Evan­gelium mit dem Lukas-Evangelium zusammenzuhalten, man braucht nur zu vergleichen die Geschlechterfolge, welche angegeben wird, um die Abstammung des Jesus von Naza­reth anzugeben, und man wird finden, daß schon in den ersten Kapiteln das erste und das dritte Evangelium sich widersprechen. Nicht nur, daß die Ahnenglieder anders angegeben werden bei Lukas als bei Matthäus; auch die Namen stimmen nicht überein. Und wenn man von da aus­gehend die einzelnen Tatsachen in bezug auf das Leben des Jesus von Nazareth vergleicht, kann man überall Wider­sprüche finden. Insbesondere tritt den Menschen vor Augen, wie kraß sich die drei ersten Evangelisten, die Schreiber des Matthäus-,Markus-, Lukas-Evangeliums auf der einen Seite und der Schreiber des vierten, des sogenannten Johannes-Evangeliums, auf der anderen Seite, widersprechen. Die Folge davon war, daß man versuchte, wenigstens das Über-einstimmen der drei ersten Evangelien in einer gewissen Weise herauszustellen, und man glaubte zu finden, daß diese drei ersten Evangelisten, wenn sie auch in vielen Einzel­heiten voneinander abweichen, doch in gewisser Weise darin übereinstimmen, daß sie ein Bild des Jesus von Nazareth geben, das ansprechend ist für die ganze Auffassung und für alle Denkgewohnheiten einer neueren Zeit, wenigstens für viele Persönlichkeiten dieser unserer neueren Zeit.",
      "Dagegen war es seit langem in bezug auf den vierten Evangelisten vielen klar, daß da von einem historischen",
      "Dokumente gar nicht die Rede sein könne. Nicht nur, daß der Schreiber des Johannes-Evangeliums, nachdem er ganz und gar die Tatsachen anders gruppiert bringt, vor allen Dingen in bezug auf das Erzählen der Wunder, die er in ganz anderer Art und Weise schildert; es zeigt sich auch, daß die ganze Stellung des Schreibers des Johannes-Evan­geliums zu dem Mittelpunkte der ganzen Weltgeschichte eine andere ist. Das ist ein Glaube, der sich immer mehr und mehr herausgebildet hat. Und wenn wir - wir können auf die Einzelheiten nicht eingehen - wieder auf den Sinn dieser Forschung hinsteuern wollen, so ist es etwa dieser, daß gesagt wird, die drei ersten Evangelien können, wenn man sie als Schilderungen aus der Glanzzeit betrachtet, das Bild geben der Persönlichkeit des ganz überragenden Jesus von Nazareth, des Gründers und Stifters des Evan­geliums. Das vierte Evangelium ist eine Bekenntnisschrift, eine Art Hymnus auf dasjenige, was der Schreiber in bezug auf seinen Glauben im Verhältnis zu dem gekreuzig­ten Jesus darstellen wollte, und wodurch er nicht eine Geschichte geben wollte, sondern eine Lehrschrift zu geben gedachte.",
      "Insbesondere im neunzehnten Jahrhundert hat sich diese Anschauung durch die sogenannte Tübinger Schule, die unter der Führerschaft des wirklich großen Bibelgelehrten, des genialen Kopfes Christian Baur stand, immer mehr ein­gelebt in die Gemüter zahlreicher Persönlichkeiten. Baurs Anschauung ist etwa diese: Das Johannes-Evangelium sei spät, sehr spät geschrieben worden, wogegen die anderen Evangelisten früher geschrieben haben, noch nach gewissen Predigten derjenigen, die vielleicht das eine oder andere selbst angesehen haben oder es erfahren haben von Personen, welche die Geschichte in Palästina miterlebt haben. Das Johannes-Evangelium aber sei erst im zweiten Jahrhundert",
      "entstanden. Nicht aus der Urgeschichte heraus, sondern be­einflußt durch die griechische Philosophie, beeinflußt durch das, was in den christlichen Gemeinden schon aufgetreten war, sei geschrieben worden, so daß Johannes, durch das beeinflußt, ein Bild des Christus Jesus entworfen habe, das die Menschen so erbauen, so erheben hat können, daß es in gewisser Weise lyrisch ist, das unterrichtet über die Art und Weise, wie man bis ins zweite Jahrhundert hinein begon­nen hat, christlich zu denken, zu fühlen und zu empfinden, das aber nicht mehr unterrichten kann über dasjenige, was geschehen ist im Beginne unserer Zeit.",
      "Gewiß, es hat auch Seelen gegeben, welche die gegen­teilige Anschauung verfochten haben. Wenn man auf der anderen Seite wirklich sagen muß, daß Christian Baur und die, welche seine Schüler waren oder mehr oder weniger mit ihm gearbeitet haben, mit ungeheuer kritischem Scharfsinn vorgegangen sind, so dürfen wir doch einen Bibelforscher wie den Geschichtsschreiber und Gelehrten Girörer nicht vergessen, der in Anspruch nimmt, daß das Evangelium vom Apostel Johannes selber herrührt. Mit Fleiß zeigt er, wie gerade dieses Evangelium fast in jedem Satze zeigt, daß ein Augenzeuge es geschrieben hat oder daß es von einem geschrieben worden ist, der von Augenzeugen seine Bot­schaft erhalten hat. Gfrörer geht so weit, daß er in seiner schwäbischen Art und Weise sagt, daß jeder, der - nach dem von ihm Vorgebrachten - nicht daran glaube, daß das Evan­gelium von Johannes herrühre, nicht gut bei Trost sein könne. Auch gegen solche ist er nicht gut zu sprechen, welche sagen, es sei nicht historisch, und sodann mit allen möglichen Dingen diesem Evangelium zu Leibe rücken.",
      "Die Frage, die uns hier interessiert, ist diese: Hat wirk­lich keiner trotz allen Scharfsinnes, trotz aller Gelehrsam­keit, die keinen Augenblick in Abrede gestellt wird, hat",
      "wirklich nur Forschung, wirklich nur Historie diese An­schauung der neueren Zeit herbeigeführt? - Wer gründlich nicht nur das Äußere der Geschichte durchforschen kann, sondern mit seinem Denken und Fühlen und mit seiner gan­zen Anschauung in die seelischen Untergründe der Mensch­heitsentwickelung hineintauchen kann, der bemerkt bald ein anderes. Es war nicht bloß der historische Sinn, es war nicht bloß die sogenannte objektive Forschung, sondern es waren die Denkgewohnheiten der neueren Zeit, die liebgeworde­nen Anschauungen, die seit dem letzten Jahrhundert, wo sie gegeben waren, immer mehr verbreitet wurden; sie ließen es nicht zu, daß über die Gestak des Christus Jesus in den Seelen sich weiter erhielten der Glaube und die Ideen, die seit Jahrhunderten geherrscht haben, daß in Jesus von Nazareth enthalten war nicht nur eine überragende, son­dern eine universale Wesenheit, eine Wesenheit - bezeich­nen wir sie zunächst als den Christus -, die als geistig-gött­lich nicht nur zur ganzen Menschheit in Beziehung gebracht werden muß, sondern zur ganzen Entwickelung der Welt überhaupt.",
      "Es verloren sich der Glaube und die Idee, daß diese Wesenheit gewirkt hat in dem sterblichen Leibe des Jesus von Nazareth, und daß wir da ein einzigartiges Er­eignis vor uns haben. Das widerspricht so sehr den Denk-gewohnheiten, daß sie sich gegeli einen solchen Glauben richten mußten.",
      "Da war es die kritische Forschung, die sich unbewußt einschlich, um recht zu geben dem, was die Ge­danken-Gewohnheiten vorerst wollten. Immer mehr und mehr kam der Sinn herauf, der nicht ertragen konnte, daß irgend etwas über das normale Menschlich-Persönliche hin­ausragt, der Sinn, der sich sagt: Ja, es hat große Menschen in der Weltenentwickelung gegeben: Sokrates, Plato oder andere.",
      "Gewiß, wir wollen zugeben, daß Jesus von Naza­reth der Größte war. Aber wir müssen innerhalb dieses",
      "Menschheitsniveaus bleiben. - Daß in Jesu etwas gewohnt haben kann, das sich mit dem normalen Menschen nicht ver­gleichen läßt, das widerspricht den materialistischen Vor­stellungen, die sich immer mehr eingenistet haben, ganz besonders. Wir können sehen, wie dieser Sinn unbewußt eingeschlichen ist und sich mit dem verbunden hat, was die sogenannte historische Forschung feststellte.",
      "Warum wurden immer mehr und mehr die drei ersten Evangelisten die geschätzten und der Schreiber des Johan­nes-Evangeliums der bloße Lyriker und Bekenntnisschrei­ber? Weil man sich sagen konnte, die drei ersten Evange­listen, die Synoptiker, schildern eine ideale Menschenfigur, aber immer etwas, welches, wenn auch hoch, doch nicht dar­über hinausragt. Es schmeichelt dem modernen Sinn, wenn gesagt wird, was ein moderner Theologe gesagt hat: Wenn wir abziehen von dem Jesus von Nazareth alles Übersinn­liche und Spirituelle, wenn wir den schlichten Mann von Nazareth nehmen, dann sind wir dem Jesu am nächsten. -Das geht bei dem Johannes-Evangelium nicht an. Es beginnt gleich mit den Worten: Im Urbeginne war der Logos, das Wort. Und das Wort, das im Urbeginne bei Gott war, das war, bevor es eine materielle Welt gab. Was da war in allen geistigen Urgründen, das ist Fleisch geworden, das hat ge­wandelt im Beginne unserer Zeitrechnung in Palästina. -Die höchste Weisheit wendet der Schreiber des Johannes-Evangeliums an, um dieses Ereignis zu verstehen und zum Verständnis zu bringen. Gegenüber dieser Sache geht es nicht an, von dem schlichten Mann von Nazareth zu spre­chen. Daher durfte er niemals mit einer historischen Ur­kunde zu tun haben. Es sind also nicht allein wissenschaft­liche Gründe, es ist die Entwickelung der gewöhnlichen Ge­danken, Gefühle und Empfindungen, die ihren Ausdruck gefunden haben in dem, was heute als Bibelkritik des",
      "Neuen Testamentes, was als sogenannte historische For­schung den Anspruch darauf macht, unbedingte oder wenig­stens relative Autorität über diese Dinge zu haben.",
      "Da entsteht aber aus der Geisteswissenschaft heraus eine weitere Frage. Stellen wir uns geradezu auf den Boden, auf den sich manche neue Forscher gestellt haben. Die einen wollten schildern ein Ereignis, das sich im Beginne unserer Zeitrechnung zugetragen hat.",
      "Diese setzten dannMythisches und Legendäres dazu. Nehmen wir an, wir stellten uns auf diesen Boden. Da müssen wir uns fragen: Ist eine Möglich­keit vorhanden, aus diesen Voraussetzungen heraus noch von einem Christentum als solchem zu sprechen?",
      "Geht es an, von einem Christentum zu sprechen, wenn wir die Ur­kunden, die von diesem Christentum künden, in rein mate­rialistischem Sinne auffassen? Geht das an gegenüber der ganzen Bibel? - Zwei Dinge sollen zunächst angeführt wer­den, welche beweisen werden, daß die Frage gar nicht an­ders gestellt werden kann als wie sie gestellt worden ist, und daß sie andeutend beantwortet werden kann.",
      "Nehmen wir an, Christian Baurs Anschauung wäre richtig, daß in Palä­stina etwas geschehen sei, das so zu erklären ist wie die äußeren historischen Tatsachen, und daß im Laufe der Zeit die Schreiber aus den Vorurteilen ihrer Zeit heraus das­jenige der Nachwek überliefert haben, was in ihnen steckt. Nehmen wir an, wir müßten eine solche Forschung voraus­setzen, vor allem mit dem Glauben, daß eine geistigeWesen­heit aus geistigen Sphären heruntergestiegen sei, die ge­wohnt hat in Jesu von Nazareth, auferstanden ist, den Sieg des Lebens über den Tod davongetragen hat - was wir als die eigentliche Essenz des Mysteriums von Golgatha be­zeichnen.",
      "Mit dieser Lehre - sagt Baur - muß gebrochen werden. Diese Auffassung gilt als eine dogmatische. Diese Auffassung muß gestrichen werden. Es muß das Ereignis in",
      "Palästina so untersucht werden wie ein anderes geschicht­liches Ereignis.",
      "Kann dann im wahren Sinne des Wortes von Christen­tum, überhaupt von der Bibel als einem solchen Werke gesprochen werden, das berichtet, was erscheinen muß? Demgegenüber sei auf zwei Tatsachen hingewiesen. Worauf beruht zunächst die erste große und umfassende Wirkung der christlichen Weltanschauung, eine Wirkung, die nie­mand leugnen kann, worauf beruht die Predigt des Paulus? Beruht sie auf dem, was eine neue nüchterne Forschung aus den Evangelien herausliest? Nimmermehr beruht des Paulus Kraft auf einer Verkündigung dessen, was mit den Mitteln einer Historie zu erschöpfen ist. Auf einem Ereignis, das nur aus übersinnlichen, niemals aus sinnlichen Ursachen zu begreifen ist, beruht die ganze Wirksamkeit des Paulus. Wer eintritt in eine Prüfung der Paulinischen Schriften, wird sehen, daß die ganze Lehre des Paulus einfach darauf beruht, daß er die Überzeugung und die Erfahrung gewin­nen konnte, daß der Christus auferstanden ist, und daß im Mysterium von Golgatha der Sieg des Lebens im Geiste über den Tod davongetragen worden ist.",
      "Woraus schöpft Paulus seine Überzeugung von der wah­ren Natur des Christus Jesus? Er schöpft sie nicht, wie etwa die anderen, die um den Christus Jesus herum waren, aus einer unmittelbaren Anweisung. Er schöpft sie, wie Ihnen allen bekannt ist, aus dem Ereignis von Damaskus. Er schöpft sie daraus, daß er sagen konnte: Ich habe den ge­sehen, der in Palästina gelebt und gelitten hat und gestor­ben ist, ich habe ihn gesehen in seinem Leben. - Nichts anderes meint Paulus, als daß er im Geiste den Christus gesehen hat und aus der geistigen Anschauung heraus die Wahrheit gewonnen hat, daß der Christus lebt. Den Chri­stus, den er kennengelernt hat in seiner geistigen Anschauung,",
      "den verkündigt er. Und er stellt diese Erscheinung gleich den anderen Erscheinungen, denn er sagt uns klar:",
      "Nach dem Tode ist der Christus verschiedenen Persönlich­keiten erschienen, den zwölf Jüngern und anderen, und zu­letzt auch mir als einer unzeitigen Geburt. - Damit meint er, daß er wirklich geschaut hat, in einer höheren Anschauung geschaut hat den, der den Sieg über den Tod davongetragen hat, und daß er seit jener Zeit weiß, daß für den, der in die geistige Welt sich erhebt, der Christus lebt.",
      "Hier stehen wir bereits mitten darinnen in bezug auf das Neue Testament, wo die neue Geisteswissenschaft sich schei­den muß von einer jeden bloß buchstäblichen Auffassung der Bibel. Was finden Sie in der Regel in den Schriften der sogenannten neuen Forschung über das Ereignis von Da­maskus? Sie finden darin in der Regel, daß es ein ekstati­scher Zustand war, in dem der Saulus zum Paulus wurde, ein Zustand, in den man nicht so ganz hineinschauen könne. Das entzieht sich der menschlichen Forschung. Ja, der äußeren menschlichen Forschung entzieht es sich. Das ist es aber gerade, was wir so oft in der Geisteswissenschaft be­tont haben, daß der Mensch - was wir weiter in den folgen­den Vortragszyklen lernen können - hinaufsteigen kann zu der Erkenntnis der höheren Welten. Das ist das, was um den Menschen herum ist, wie die Farbe des Lichtes um den Blinden. Sehen lernen kann der Mensch diese höhere Welt, wie der operierte Blindgeborene sehen lernen kann die Farben und das Licht. Das ist dasjenige, was sich durch die geisteswissenschaftlichen Methoden mit der Seele des wahren Schülers der Geisteswissenschaft vollzieht, was ihn fähig macht, hineinzuschauen in die geistigen Welten, um dasjenige selbst zu schauen, was da ist. Was sich mit diesem Schüler vollzieht, und wovon jeder Schüler heute und zu aller Zeit Zeugnis ablegen kann, das hat sich mit Paulus",
      "vollzogen. Er hat es empfangen: zu hören mit Ohren, die nicht sinnliche Ohren sind, zu sehen mit Augen, die nicht sinnliche Augen sind. Er konnte dann auch Den wahrneh­men, der in Jesu von Nazareth gewohnt hat. Also in das Übersinnliche ragt die ganze Kraft des Paulus. Wenn man den ganzen Paulus nimmt, wie er ist, kann man sagen: Was er gesagt hat, ist durchglüht von dem «Christus lebt, er ist auferstanden. Daher ist nicht eitel unser Glaube».",
      "Und wenn man darauf eingeht, was gerade des Paulus Predigt gewirkt hat, wie gerade er diejenige Gestalt des Christentums verbreitet hat, die durch die Welt gegangen ist, dann kann man nimmermehr sagen, es komme nicht darauf an, an irgendwelche übersinnliche Tatsachen an­zuknüpfen, um die Tatsachen über Jesus zu erforschen. Man müsse die gewöhnlichen wissenschaftlichen Formen anwen­den, sagt man. Man vergißt dann aber nicht nur die Ur­Tatsachen in Palästina, nicht nur das, was in den dreiund­dreißig Jahren geschehen ist, sondern auch dasjenige, was für die Verbreitung des Christentums geschah, man vergißt, daß es auf einem übersinnlichen Ereignis beruht, und daß dieses übersinnliche Ereignis zunächst zu verstehen und zu begreifen ist.",
      "Aber in ganz ähnlicher Weise finden wir auch, wenn wir nur ernst und wirklich die Dinge betrachten, daß das Alte Testament, wenigstens seine wichtigste Urkunde, die Schrif­ten des Moses, auf etwas Ähnlichem beruhen. Wir finden, daß die ganze Sendung des Moses, die ganze Kraft des Mo­ses, durch die er Ungeheueres für sein Volk geschaffen hat, auch auf einem übersinnlichen Ereignis beruht; wie wir vorgestern sagen mußten, daß, wenn sich der Geistesfor­scher hinaufentwickelt, so daß er sehend wird in der geisti­gen Welt und hineinblicken kann in die geistigen Unter­gründe der Dinge, daß er dann dasjenige, was Tatsachen",
      "der geistigen Welt sind, überschaut in Bildern, den Imagi­nationen. Ja, man kann auch die Vorgänge, die in einem selbst geschehen, wenn man so hinaufsteigt in die geistigen Gefilde, nur in Bildern ausdrücken, wobei aber klar sein muß, daß der, welcher in solchen Bildern spricht, nicht über die Bilder als solche sprechen will, sondern meint, daß man in diesen Bildern das Ausdrucksmittel hat für seine über­sinnlichen Erlebnisse.",
      "Das übersinnliche Erlebnis, durch das Moses seine Sen­dung bekommen hat, ist uns deutlich geschildert in der Erscheinung des brennenden Dornbusches. Da sehen wir, wie Moses, der Leiter und Lenker des Volkes, sich seinem Gott gegenübergestellt sieht, dem Gotte Abrahams, Isaaks und Jakobs, der dem Moses den Auftrag gibt, das für sein Volk zu tun, was wir dann als Moses' Tat geschehen finden. Indem wir dieses heranziehen, stehen wir bereits vor einem Grundnerv der ganzen Bibel, nämlich vor der Frage: Wie haben wir uns überhaupt behufs eines tieferen Eindringens in diese Urkunde zu diesen zwei Tatsachen zu stellen, auf die wir hingewiesen haben als übersinnliche Tatsachen, die eine jede bloß äußerliche Forschung unmöglich machen? Wie haben wir uns zu diesem Grundnerv der Bibel in gei­steswissenschaftlichem Sinn zu verhalten? Wir werden ein­dringen können, wenn wir uns den Inhalt der Offenbarung oder des Erlebens des Moses vor Augen führen.",
      "Die wichtigsten Züge seien nur angeführt. Moses sieht sich gegenüber dem Gotte Abrahams, Isaaks und Jakobs. Der Gott gibt ihm zu gleicher Zeit den Auftrag, das Volk aus Ägypten hinaus zu führen, es zu einer bestimmten Größe und zu einem bestimmten Verhalten zu bringen. Als dann Mos es etwas haben will, wodurch er sich rechtfertigen kann vor dem Volke, damit er sagen könne, wer er sei und wer ihn schickt, da enthüllt der Gott seinen Namen: «Ich",
      "bin der Ich-bin.>> Dieses Wort kann niemand verstehen, der nicht auf den ganzen Sinn und das Wesen alter Namen­gebung einzugehen in der Lage ist. Alte Namengebungen sind nicht die heutigen Namengebungen.",
      "Alte Namenge­bungen sollten durchaus ausdrücken das Wesen der Per­sönlichkeit, das Wesen dessen, der uns entgegentritt. In dem «Ich bin der Ich-bin» mußte sich in ganz bestimmter Art das Wesen des Gottes ausdrücken, der dem Moses gegen­überstand, und der sich nennt «der Gott Abrahams, Isaaks und Jakobs».",
      "Warum nennt er sich der Gott Abrahams, Isaaks und Jakobs? Dahinter liegt ein Geheimnis, das ent­rätselt sein will. Wir können es nur enträtseln, wenn wir mit den Mitteln der Geisteswissenschaft daran herantreten.",
      "Wir werden es in den verschiedenen Stellen immer wieder hervorzuheben haben, daß der Mensch besteht aus den verschiedenen Gliedern seiner Wesenheit, daß wir in dem, was wir den physischen Leib nennen, nur einen Teil des Menschen vor uns haben, daß wir außer diesem höhere Glieder haben, die übersinnlich sind, die die eigentlichen Grundlagen, die schöpferischen Prinzipien sind. Wir müs­sen hinzufügen dem physischen Leib den Äther- oder Le­bensleib, dann den Astralleib und als viertes Glied den Ich-Träger.",
      "Den physischen Leib hat der Mensch gemein­schaftlich mit den scheinbar leblosen Wesen, mit den Mine­ralien, den Ätherleib mit den Pflanzen und allen leben­digen Wesen, den Astralleib mit den tierischen Wesen, mit dem, was Leidenschaften und Begierden haben kann. Durch das Ich ragt der Mensch über alle sinnlichen Wesen, die ihn umgeben, hinaus.",
      "Das sind die vier realen Glieder der menschlichen Wesenheit, welche die Geisteswissenschaft im­mer anerkannt hat.",
      "Hinweisen müssen wir darauf, daß das, was wir heute den physischen Leib nennen, ebenso seinen geistigen Urgrund",
      "hat und nur verdichtet ist aus dem Geistigen. Wie das Eis aus dem Wasser, so ist das Physische aus dem Gei­stigen heraus entstanden. Wir müssen weit zurück gehen in der Anschauung der Geistesentwickelung, wenn wir die ersten geistigen Ursprünge des physischen Menschenleibes suchen wollen. Von den vier Gliedern der menschlichen Wesenheit ist dieses vierte Glied durchaus das älteste. Der physische Leib ist heute der dichteste. Er ist das, was vom Geiste ausgegangen ist in ferner Vergangenheit. Er ist im­mer dichter und dichter geworden, durch manche Umwand­lungen hindurch gegangen und hat dadurch seine physische Gestalt angenommen. Das ist das älteste am Menschen. Ein jüngeres Glied ist der Äther- oder Lebensleib. Er ist später hinzugekommen, daher er sich auch in einem geringeren Verdichtungsgrade darstellt. Noch jünger ist der Astralleib. Das jüngste Glied ist das Ich, der Träger des menschlichen Selbstbewußtseins. Alle diese Glieder sind aus geistigen Urgründen und geistigen Wesenheiten, aus göttlich-geisti­gen Wesenheiten heraus entstanden. Wir können sagen, die Geisteswissenschaft zeigt uns, daß dieses Ich, wodurch der Mensch die heutige selbstbewußte Wesenheit geworden ist, sich hineingesenkt hat in den Leib. Er war zusammenge­fügt, bevor er Ich-Wesenheit wurde, aus physischem, Äther-und Astralleib.",
      "Diejenigen Wesenheiten nun, welche die Schöpfer, die Bildner dieser drei Glieder der menschlichen Wesenheit sind, die unterscheidet auch die Bibel. Die Lehre des Moses spricht von dem Schöpfer, dem Bildner des menschlichen Ichs, von dem Schöpfer des Trägers des menschlichen Selbst­bewußtseins. Daher sieht auch die Bibel in dem Gotte, der in den Menschen einfließen ließ das Ich, sozusagen den, der am letzten darangekommen ist in bezug auf die Evolution des Menschen. Die göttlichen Wesenheiten, die als die Elohim",
      "bezeichnet werden, die wir streng unterschieden haben von dem Gotte Jahve oder Jehovah, diese göttlichen We­senheiten sind die Schöpfer von dem physischen, ätherischen und astralischen Leib. Sie sind in der Bibel genau unter­schieden von dem letzten in unserer Evolution auftretenden Gott, von dem Jahve-Gott, von dem, der dem Menschen das Ich gebracht hat. Wenn wir fragen: Wo findet der Mensch die Wesenheit dieses Gottes, dieses jüngsten der schöpferischen Götter, von dem die Bibel zu sprechen be­ginnt im vierten Vers des zweiten Kapitels der Genesis? -da zeigt uns die Geisteswissenschaft, daß da, wo der Mensch in sich sein Ich findet, das sich so wesentlich, schon seinem Namen nach, von allen anderen Wesenheiten um uns herum unterscheidet, daß er da findet in sich einen Tropfen dieser göttlichen Wesenheit. Das ist keine pantheistische Lehre, auch keine Erklärung dafür, daß der Mensch seinen Gott in sich zu finden hat. Das zu behaupten wäre gleich dem, der behauptet, ein Tropfen Wasser ist dasselbe Wesen wie das Meer - und sagt: dieser Tropfen Wasser ist das Meer.",
      "Wenn wir sprechen im Sinne der Geisteswissenschaft, so sprechen wir von einem Unendlichen, Umfassenden, Uni­versalen, das verknüpft ist mit der irdischen Entwickelung und dem anderen, was zu dieser irdischen Entwickelung gehört. In unserem Ich finden wir einen Funken dieser Jahve-Gottheit, wie in dem Wassertropfen dieselbe Wesen­heit ist wie im Meer. Aber es war der Weg, den die Ent­wickelung des Menschen zurücklegen mußte, ein sehr langer, wobei die Jahve-Gottheit anfing, den Menschen so zu for­men, daß er das Ich mit dem Bewußtsein erfassen konnte. Die Kraft des Ichs mußte vorher lange im Menschen arbei­ten, bevor der Mensch zum Bewußtsein des Ichs kam. Moses wurde der große Vorläufer in dem Bringen des Bewußtseins",
      "des Menschen zum Ich. Aber diese Kräfte arbeiten und bilden schon lange an der menschlichen Evolution vorher. Sie bilden so, daß wir ihre Weise erkennen können, wenn wir uns etwas mit der Evolution des menschlichen Bewußt­seins selber beschäftigen.",
      "Blicken wir ein wenig zurück in der Entwickelung des menschlichen Bewußtseins. Das Wort Entwickelung braucht man heute sehr häufig, aber so durchgreifend, so intensiv wie die Geisteswissenschaft Ernst macht mit dem Worte Entwickelung, so ist es bei keiner anderen Wissenschaft der Fall.",
      "Dieses menschliche Bewußtsein, wie es heute ist, hat sich aus anderen Bewußtseinsformen entwickelt. Wenn wir weit, weit zurückgehen in der Herkunft des Menschen, nicht im Sinne materialistischer Wissenschaft, sondern so, wie ich es vorgestern entwickelt habe, dann finden wir, daß das Menschen-Bewußtsein immer mehr als ein anderes erscheint, je weiter wir zurückgehen.",
      "Dieses Bewußtsein, welches die verschiedenen Verstandesbegriffe, die äußeren Sinneswahr­nehmungen in der bekannten Art verknüpft, das ist erst entstanden, wenn auch in urferner Vergangenheit, aber es ist erst entstanden. Wir können in jener Zeit einen Zustand des Bewußtseins finden, der ganz anders war als heute, weil besonders das Gedächtnis ganz anders war.",
      "Das, was der Mensch heute als Gedächtnis hat, ist nur ein herunterge­kommener Rest einer alten Seelenkraft, die in ganz anderer Weise vorhanden war. In alten Zeiten, als der Mensch noch nicht die kombinierende Kraft seines heutigen Verstandes hatte, als er noch nicht imstande war, zu rechnen und zu zählen im heutigen Sinne, als er noch nicht seine Verstan­deslogik ausgebildet hatte, da hatte er dafür eine andere Kraft der Seele: er hatte ein universelles Gedächtnis aus­gebildet.",
      "Dieses mußte abnehmen, mußte zurücktreten, damit auf seine Kosten unser heutiger Verstand zu seiner",
      "Entwickelung kommen konnte. So ist überhaupt der Gang der Entwickelung, daß eine Kraft in den Hintergrund tritt, damit die andere auftauchen kann. Das Gedächtnis ist eine abnehmende Kraft, der Verstand und die Vernunft sind zunehmende Seelenkräfte.",
      "Für diejenigen, die schon längere Jahre hier diese Vor­träge hören, kann es nicht etwas besonders Wunderbares sein, was ich jetzt sagen werde. Für die anderen wird es grotesk erscheinen, wenn über die Natur des Gedächtnisses in der folgenden Weise gesprochen werden wird. Was ist das Äußere des menschlichen Gedächtnisses? Es ist das, daß es sich zurückerinnert an gestern, vorgestern und so weiter, bis in die Kindheit. Dann reißt es aber einmal ab. Dieses Gedächtnis riß nicht ab in urferner Vergangenheit, nicht in der Kindheit, nicht einmal bei der Geburt; sondern wie der heutige Mensch sich erinnert an dasjenige, was er selbst in seinem persönlichen Leben erlebt hat, so erinnerte sich der Mensch der Vorzeit an dasjenige, was der Vater, der Groß­vater, was die ganze Generation hindurch erlebt hat. Das Gedächtnis war durch Generationen hindurch eine Seelen-kraft, die sich real verbreitete. Durch Jahrhunderte hin­durch hat sich in urferner Vergangenheit die Erinnerung erhalten, und mit dieser anderen Ausbildung des Gedächt­nisses hing eine andere Art der Namengebung zusammen.",
      "Wir kommen nun zu der Frage: Warum ist in den ersten Kapiteln der Bibel von Individualitäten die Rede, die wie Adam, Noah Jahrhunderte alt werden? Weil es für die Menschen, die hier gemeint sind, keinen Sinn hätte, die Per­sonen zu begrenzen. Die Erinnerung reicht hinauf durch Generationen bis zu dem Urvater. Dieser ganzen Genera­tion gab man einen Namen. Es hätte keinen Sinn gehabt, einer einzelnen Persönlichkeit den Namen Adam zu geben. So gab man dazumal den Namen dem, was sich, die gleiche",
      "Erinnerung festhaltend, durch Jahrhunderte hindurch von Generation zu Generation zurückerinnerte - Adam, Noah. Und was war das? Es war das, was durch Vater, Sohn und Enkel geht, aber die Erinnerung bewahrte. So treu bewahrt die biblische Urkunde die Geheimnisse der Geisteswissen­schaft.",
      "Wenn wir das Bewußtsein des Ichs, durch das wir die Wesenheit der Jahve-Gottheit erfassen, betrachten, so wer­den wir sehen, daß das Ich in uns lebt zwischen Geburt und Tod, und daß es diese seine einerlei Art aufrechterhält zwi­schen Geburt und Tod. So hielt das Ich sich damals durch Generationen, durch Jahrhunderte hindurch aufrecht.",
      "Wie wir heute von dem Ich sprechen und wissen, daß das Ich zurückgeht so weit, wie wir uns erinnern, ebenso sagte sich der Mensch der Urzeit: Mich selbst ein Ich zu nennen, hat keinen Sinn. Ich erinnere mich zurück an meinen Vater, Großvater, Urgroßvater. - Sein Ich ging durch die Genera­tionen, und es hatte sogar einen Namen.",
      "Wie wir in unse­rem persönlichen Ich einen Ausdruck des Gottes finden, wenn wir uns in dieses Ich vertiefen, so sagte sich der alte Mensch, indem er hinaufsah durch die Generationen: Der Gott, der in dem Ich lebt, lebt durch Generationen hinun­ter, - als eine Gottheit, die dann Moses in den höheren Welten erkannte. Der Gott war kein anderer als der, welcher sich in alten Zeiten als ein Ich von Generation zu Generation hindurch gelebt hat.",
      "Man bezeichnete als Ich, in der Aus­drucksweise der damaligen Zeit, was sich als Ausdruck des Jahve-Gottes fortpflanzte, mit dem Jahve-Worte «Ich bin der Ich-bin». Das war das, was Moses in seiner geistigen Offenbarung erkennen lernte.",
      "Im Erschauen des brennen­den Dornbusches ist das zum ersten Male offenbart worden. Es war derselbe Gott, der früher von Generation zu Gene­ration herunter gelebt hat, der Gott Abrahams, Isaaks und",
      "Jakobs. Es war die Kraft, die also in der lebendigen Er­innerung fortlebte und zu gleicher Zeit alles mit sich brachte, was die menschliche Ordnung begründete. So schauen wir hinauf auf die Vorgängerschaft des Moses. Im biblischen Sinne schauen wir hinauf bis zu den Patriarchen, bis zu denen, in welchen der Gott Abrahams, Isaaks und Jakobs lebte.",
      "Diese Zeiten brauchten keine äußeren Gebote, keine äuße­ren Gesetze. Denn mit dem lebendigen Gedächtnis, mit des­sen ganz anderer Art als das Gedächtnis heute ist, lebte sich fort dasjenige, was man zu tun hatte. Wonach handelte man in diesen Urzeiten? Man kommt darauf, wenn man die Bibel richtig versteht. Man handelte nicht nach Geboten. Man handelte nach dem, was einem die Erinnerung sagte, was der Vater, der Großvater und so weiter getan haben. Mit seinem Blute bekam man eingeboren die Richtung zu dem, was man zu tun hatte. Es war in diesen alten Genera­tionen etwas wie ein vergeistigter Instinkt. Wenn wir heute, als Vergleich gebraucht, sagen: «aus Instinkt heraus han­deln», so ist das ein Gebot. Nein, der alte Mensch handelte nach dem Charakter seines Wesens, nach seinem Gattungs­wesen. Wie handelten die mit Abraham, Isaak und Jakob in der Bibel bezeichneten Wesen? Sie handelten so, wie das durch die Generationen rinnende Blut es ihnen eindrückte. Der Gott Jahves war es, den sie heruntergebracht hatten mit ihrem Ich, ob sie Krieg führten, ob sie in Frieden lebten. Gebote hatten sie nicht, ein Gesetz hatten sie nicht. Es war der vergeistigte Instinkt Gottes, der in ihnen lebte.",
      "Zu der Zeit, als Moses auftrat, da war die menschliche Persönlichkeit auf der ersten Stufe ihrer Ausbildung. Da riß sie sich los in ihrem Bewußtsein von diesem gemein­samen Bewußtsein der Generation. Da hatte schon gründ­lich aufgehört das Gedächtnis, das durch die Generationen",
      "hinaufreichte. Da hatte man nicht mehr den vergeistigten Instinkt zum Handeln. Da mußte etwas anderes an dessen Stelle treten. Da mußte der Gott Abrahams, Isaaks und Jakobs, der in seiner geistigen Naturgestalt Moses das Ge­setz, die Gebote gab, weil man nicht mehr den vergeistigten Instinkt hatte, da mußte er die äußere Ordnung, das soziale Zusammenleben durch die Gebote, durch das Gesetz regeln.",
      "So ist derselbe Gott, der vordem als Naturkraft gewirkt hat, jetzt als Gesetzgeber wirksam, um die äußere Ordnung auf dem Gesetzeswege zu begründen. So sehen wir, daß es einen tiefen Sinn hat, an dieser Stelle die Worte zu lesen:",
      "der Gott Abrahams, Isaaks und Jakobs. Der Gott, der sich bezeichnet als der Gott «Ich bin der Ich-bin», er ist der­selbe wie das vierte Glied der menschlichen Wesenheit, der­selbe, der das Ich in die menschliche Wesenheit einfließen ließ. Aber die Menschen konnten die geistige Natur des Ichs nicht in ihr Bewußtsein aufnehmen. Dazu bedurfte es wieder einer längeren Vorbereitung, und diese fällt in die Zeit, die uns durch die Bibel als das Alte Testament geschil­dert wird, in die Zeit von Moses bis zum Mysterium von Golgatha. Daher ist diese Zeit eine Zeit der Verheißung, die das neue Evangelium darstellt, der Beginn der «Zeit der Erfüllung». Es kündigt sich also dem Moses der Gott an, der den Ausdruck fand «Ich bin der Ich-bin». Er kündigt sich so an, daß er die äußere Ordnung der Menschen, das Zusammenleben derselben durch Gesetze ordnet, auf dem Umwege durch Mosis Schauen, durch Mosis Sehen. So lebte die Menschheit in der vorchristlichen Zeit, in der der Gott schuf, in der der Jahve-Gott bildete, in der der «Ich bin der Ich-bin» lebt, welcher aber noch nicht bewußt leben konnte, sondern nach dem äußerlichen Gesetze, das aber von ihm stammte. Immer mehr rückt die Zeit heran, wo sich die Menschheit des vollen Ichs bewußt werden sollte. Durch das",
      "ganze Altertum hindurch gab es nur ein Mittel für die Men­schen, die noch nicht schauen konnten, noch nicht entgegen­treten konnten dem Gott in der physischen Welt. Nur eine Art gab es, wie dieser Gott für sie wirksam werden konnte. Das war das Gesetz, die Ordnung. Das galt für die äußere Welt.",
      "Außerdem gab es eine übersinnliche Art, diesen Gott kennenzulernen, und das waren die Mysterien oder die Einweihung. Was war die Einweihung? Alles das, was ge­wissen Persönlichkeiten überliefert wurde, welche dazu ge­eignet befunden wurden, die Methoden anzuwenden, die die geisteswissenschaftliche Forschung hat, um die im Men­schen schlummernden Kräfte und Fähigkeiten zu entwickeln, so daß sie in die geistige Welt hineinschauen konnten. Für die Bekenner des Alten Testamentes würde es daher so sein, Gott, der in dem «Ich-bin» lebt, geistig von Angesicht zu Angesicht zu sehen. Wenn sie diese Methode anwendeten, wurden sie in die Lage versetzt, mit geistigen Augen und Ohren zu hören und zu sehen, selbst zu sehen, was Moses gesehen hat, als ihm der Gott, der «Ich-bin», die Mission erteilt hat. Aber nur in den Mysterien, nur durch die Ein­weihung war das möglich.",
      "Aber es gab auch solche, die den «Ich bin der Ich-bin» er­kannten, aber sie mußten dazu alle die Prozeduren, die Methoden durchmachen, wodurch sich der Mensch umge­staltet zu einem Instrumente des höheren Schauens, des Hineinblickens in die geistige Welt. So also war diejenige Gottheit, die schon in Abraham, Isaak und Jakob lebte, nach außen für die physische Welt ganz verhüllt. Sie ord­nete die Welt durch das Gesetz. Für den Eingeweihten wird im Denken das Geheimnis der Mysterien schaubar. Nun kam die Zeit, in der das Mysterium von Golgatha sich voll­ziehen sollte. Was war da eigentlich geschehen? Stellen wir",
      "uns so richtig vor die Seele, was den Eingeweihten in den alten Zeiten passierte. Nur skizzenhaft schildern kann ich Ihnen den Vorgang der Einweihung durch Meditation, Konzentration und die anderen Übungen.",
      "Durch diese wurde die Seele des Einzuweihenden lange vorbereitet. Dann kam ein dreieinhalb Tage währender Abschluß die­ser Einweihungsvorgänge. Da wurde der Mensch, der ein­geweiht werden sollte und der so weit war, durch den Ein­weihungsweisen in einen Zustand gebracht, durch den sein physischer Leib vollständig schlafend war.",
      "Nicht nur schla­fend war er, sondern wie tot, so also, daß der Mensch sich seiner physischen Sinne, seiner physischen Augen und Ohren nicht bedienen konnte. Dafür aber sah er durch die Organe seiner geistigen Glieder hinein in die geistigen Welten.",
      "Er konnte da wahrnehmen, wenn er außerhalb seines Leibes war, wenn er nicht gefesselt war, wenn er in Latenz der physischen Organe war. Er konnte dann in sich schauen, was unsichtbar in ihm lebte als das «Ich bin der Ich-bin»; aber er konnte es nur in den Tiefen der Mysterien schauen.",
      "Dann wurde er - wie jeder weiß, der diese Dinge kennt - auf­geweckt in seinem physischen Leibe und bediente sich wie­der der physischen Sinne. Aber er hatte jetzt das volle Be­wußtsein: «Ich bin der Ich-bin, ich war in der geistigen Welt.",
      "Das, was zu Moses gesprochen hat: , das stand vor mir, und es ist das, was mir die Ewigkeit verwehrt, das, was in meinen Leib eingezogen ist. Mit dem war ich verbunden. Ich war mit dem göttlichen Urträger des Ich-bin verbunden, dessen Abglanz und Spiegelbild mein Ich-bin ist.»",
      "So kehrte der Eingeweihte zurück in die physische Welt und wurde Zeuge dafür, daß es ein Geistiges gibt im Ich, denn er hatte es geschaut. Kunde und Botschaft konnte er ablegen vor seinen Zuhörern, denen er Botschaft zu geben",
      "berufen war. So konnte man aber nur in der geistigen Welt sehen den «Ich bin der Ich-bin». Durch das Ereignis von Golgatha stieg dieselbe Wesenheit, die sich angekündigt hatte bei Moses in dem brennenden Dornbusch mit den Worten «Ich bin der Ich-bin», herab in die Menschen. Das ist ganz im Sinne des Johannes-Evangeliums: Das Ich ist Fleisch geworden in dem Leibe des Jesus von Nazareth, wohnte in demselben und wandelte unter den Menschen. Das war die Urkraft, die gerade den Menschen auf die Höhe gebracht hat, auf der er heute steht. Die Urkraft wurde Mensch; eine Gott-Wesenheit war Mensch geworden und wandelte unter den Menschen. Die Möglichkeit war da, daß innerhalb des geschichtlichen Verlaufs der Menschheit das einmal als historisches Ereignis da war, was die Ein­geweihten nur im Geiste erschauen konnten, was auf Gol­gatha sich als historisches Ereignis vollzogen hat: daß das Christus-Wesen den Sieg über den Tod der Materie davon­getragen hat.",
      "Das ist das Historisch-äußerlich-Wirkliche, das sich in den Mysterien so und so oft an den Eingeweihten vollzogen hat. So ist der Verlauf der Dinge, die während der alten Zeiten in dem tiefen Dunkel der heiligen Mysterien sich ereigneten bei denen, die durch dreieinhalb Tage ihren phy­sischen Leib nach dem Eingeweihten-Drama verließen, und die während dieser Zeit in der geistigen Welt wandelten und in die geistigen Urgründe des Menschen schauten. Daß dieses Ereignis herabsteigt in die physische Welt und sich als historische Tatsache darstellt, das ist der Verlauf.",
      "Jetzt aber kam die Menschheit durch die Hinneigung der Gefühle und Empfindungen und Gedanken zu dem Ereignis von Golgatha durch den Glauben. Dann wurde das Ver­ständnis daraus. Es war etwas Neues gegeben. Es war ge­geben, das äußerlich zu haben, was man sonst nur durch",
      "das Entrücktsein in der geistigen Welt haben konnte. Wenn man das so annimmt, dann verstehen wir, warum der Chri­stus Jesus sagt: Ich bin der Ich-bin in einer völlig neuen Gestalt. - Er sagt: Blickt zurück in die Urzeiten, in das­jenige, was als das Ewige im Menschen gelebt hat, das sich herunter gelebt hat in Abraham, Isaak und Jakob, das sich dann in dem Gesetze des Moses kundgegeben hat. Jetzt ist die Zeit da, wo das Ich sich bewußt wird in der einzelnen Persönlichkeit, wo der Mensch sich in seinem Ich, in dem in ihm wohnenden Göttlichen, voll bewußt werden soll.",
      "War es in den alten Zeiten so, daß der Mensch hinauf-schaute zu dem Gott, daß er schaute und sich sagen konnte:",
      "Was in mir lebt, das lebt durch die Generationen, - so ist es jetzt so, daß, wenn er in sich hineinschaut, er das Göttliche in seinem Ich findet. Das Göttliche, aus dem jedes Ich her­vorgegangen ist, das war der Körper des Jesus von Naza­reth, und der das verstand, der schrieb: Im Urbeginne war das Wort, und das Wort war bei Gott, und Gott war das Wort. - Mit dem Wort ist das Wesen der innersten Men­schennatur und zugleich der Urquell dieses innerstenWesens gemeint. Und dem Matthäus legt er in den Mund: Das, was in mir lebt, von dem ein Funke in jeder menschlichen Per­sönlichkeit ist, das war, ehe das Evangelium war. - Der bedeutsame Satz in dem Johannes-Evangelium war: «Ehe denn Abraham ward, bin Ich.» - Bevor ein Abraham war, war das «Ich-bin», das Ich-bin, das nicht an eine Zeit ge­bunden ist, das vor Abraham war, das da war schon in den geistigen Urgründen des Menschen. Indem er sich selber als den Urquell des Ich-bin bezeichnen mußte, sprach der Chri­stus das bedeutsame Wort: Ehe Abraham ward, war das Ich-bin.",
      "So sehen wir, wie der Sinn der Menschheitsentwickelung, wie ihn die Geisteswissenschaft wieder lebendig macht, in",
      "dem ganzen Grundbuch der Dinge durch das Alte und das Neue Testament hindurchflutet. Und wir sehen, wie uns die wichtigsten Worte erst lesbar werden, wenn wir den Sinn der Worte, unabhängig von den Worten, durch die Geistes­wissenschaft ergründen. Um etwas anzuführen, was dem materialistischen Sinn im Geiste zu bedenken gibt, sei an die Auferweckung des Lazarus erinnert. Sehen Sie, sagt ein solcher Mann wie Gfrörer: Wer behauptet, das Johannes-Evangelium sei nicht von Johannes geschrieben, der hilft sich damit, daß er sagt, vieles hat der Schreiber hingeschrie­ben, so wie er es erlebt und verstanden hat, aber das Laza­rus -Wunder muß ihm erzählt worden sein. Da kann er nicht dabei gewesen sein. - Man muß das Lazarus -Wunder nur richtig verstehen. Fassen wir es doch so, daß der Chri­stus, als er in die Welt trat, den Leib des Jesus von Naza­reth annahm. Fassen wir es doch so, daß das, was im Alten Testamente vorbereitet wurde, im Neuen seinen Ausdruck gefunden hat. Er mußte da eine Persönlichkeit haben, die ihn vollständig verstehen konnte, die im tiefsten Sinne ein­dringen konnte in das, was er verkündigen konnte, das heißt, er mußte auf seine Art eine Persönlichkeit einweihen.",
      "Einweihungsgeschichten werden uns zu allen Zeiten unter Verhüllung erzählt. Das Lazarus -Wunder ist nichts anderes als die wunderbare und gewaltige Darstellung, wie der Christus den ersten Eingeweihten des Neuen Testamentes geschaffen hat, wie der Eingeweihte bei seinem Schüler, der dreieinhalb Tage in einem todähnlichen Zustande lag, die Seele wieder zurückrief in den Leib, nachdem sie die Wan­derung durch die geistige Welt gemacht hatte, um nachher durch den Christus selbst erweckt zu werden. Alles das ist leicht zu durchschauen von dem, der etwas davon versteht, denn es ist die Sprache, in der überhaupt Einweihungs­geschichten erzählt werden. Der Sohn Gottes soll durch die",
      "Krankheit geehrt werden - zur Ehre Gottes. Das bedeutet äußeres Erscheinen als Offenbarung des Inneren; so daß der Satz in Wahrheit zu übersetzen ist: Die Krankheit ist nicht zum Tode, sondern daß der Gott als äußere Erscheinung offenbar werde, damit er auch für die Sinne geoffenbart werden könne. - In der Persönlichkeit des Lazarus schlum­mert die tiefere menschliche Wesenheit, die die Fähigkeit und die Kraft hat, daß sie in geheimnisvoller Art in ihm entwickelt werden konnte, hinaufgeführt werden konnte in die geistige Welt, so daß er erkennen konnte das Wesen des Christus selber, des Sohnes Gottes. Diese Kraft mußte aber erst entwickelt werden. Er entwickelte sie in Lazarus, damit das Göttliche, das in Lazarus ruhte, offenbar werden könne, und offenbaren könne dasjenige, was der Sohn Got­tes sei. So schafft der Christus Jesus in Lazarus den ersten, der aus eigener innerer Beobachtung weiß, wer der Christus Jesus eigentlich ist. Zu gleicher Zeit zeigt dieses Wunder",
      "- denn es ist für den, der nur die äußeren physischen Ge­setze gelten lassen will, ein echtes Wunder -, was der betref­fende Schüler während der dreieinhalb Tage durchmachen muß, denn das kommt einem echten Tode gleich, weil der Ätherleib und der Astralleib aus dem physischen Leib her­ausgehoben wird und nur der physische Leib daliegt.",
      "So also haben wir aus der Geisteswissenschaft heraus selbst ein so wunderbares Ereignis - wunderbar nur für denjenigen, der es nicht erklären kann -,ein so wunderbares Ereignis durchdrungen, wie das Lazarus-Wunder es ist. Alles das enthüllt sich Ihnen in demLazarus-Wunder,wenn Sie nur das Licht haben, das darauf fällt durch die Worte:",
      "Seine Krankheit ist nicht zum Tode, sondern zur Enthül­lung des Inneren. - Wenn diese Fähigkeiten erweckt werden im Menschen, so ist das wie eine Geburt. Wie ein Kind aus dem Mutterschoß hervorgeht, so wird das Höhere aus dem",
      "niederen Menschen geboren. So ist die Krankheit des Laza­rus verbunden mit der Geburt des neuen Lebens, des Gott-Menschen, so daß der göttliche Mensch in dem physischen Menschen, im Lazarus, geboren wird.",
      "So könnten wir Schritt für Schritt das Johannes-Evange­lium durchgehen und würden die Erfahrung machen, daß das, was in der geistigen Einweihung geschehen mußte, an­ders geschildert werden mußte. Wenn wir sehen, wie in alten Zeiten mit ganz anderen Geisteskräften der Gott Abrahams, Isaaks und Jakobs wirkt, und dann wieder hin-einblicken in die Bibel, dann wird sie uns das hohe Uni­versalbuch, das uns das entgegenleuchten läßt, was wir erst selbst gefunden haben. Indem wir zugeben müssen - wir können das sagen -, daß nur derjenige, der höhere geistige Kräfte ausgebildet hat, zu diesen Wahrheiten kommen kann, so mussen wir, wenn sie uns entgegentreten im Johan­nes-Evangelium, auch zugeben und sagen können, was sie in diese Schriften gebracht hat. Indem ein neuer Geistes-forscher an das Evangelium und an die ganze Bibel heran­trat, lernte er das sehen und kann sagen: Die Menschen wer­den wieder zu einem wahren Wert dieser Urkunde kommen und erkennen, daß nur ein materialistisches Vorurteil die Worte sprechen kann: «der schlichte Mann von Nazareth». Wir aber haben als Ergebnis der wahren Erkenntnis in dem Christus eine überwältigende Welt-Wesenheit erkannt, die in dem Leibe des Jesus von Nazareth gelebt hat.",
      "So erscheinen uns die drei ersten Evangelien im Verhält­nis zu dem Johannes-Evangelium etwa so, wie wenn drei Menschen gruppiert am Abhange eines Berges stehen und jeder aufzeichnet, was er sieht. Jeder sieht einen Ausschnitt. Derjenige, der von der höheren Warte heruntersieht, über-sieht mehr und schildert mehr von dieser höheren Warte aus. Wir erfahren nicht nur dasjenige, was die anderen",
      "unten schildern, sondern auch dasjenige, was alle drei zu­gleich erklärlich machen kann. So ist es nicht schwer zu sagen, welcher es war, der auf der höheren Warte stand, sondern für uns ist es so, daß die drei ersten Schreiber auch in gewisser Beziehung Eingeweihte waren. Aber der tiefer Eingeweihte, derjenige, der viel tiefer, viel tiefer hineinsehen konnte als die drei anderen und über die wahren geistigen Tatbestände, die hinter dem Sinnlichen liegen, schreiben konnte, das ist der Schreiber des Johannes-Evan­geliums. So gliedern sich uns die Evangelien zusammen zu einer Harmonie, und das, was als Mysterium von Golgatha sich abgespielt hat und nicht begriffen werden kann als ge­wöhnliches geschichtliches Ereignis, sondern nur erklärlich wird durch einen Prozeß, wie wir ihn bei Paulus finden, der sagt: Nicht ich, sondern Christus lebt in mir.",
      "Was nebenher von der äußeren Forschung gezeigt wird, das wird uns in der Geistesforschung ebenso wichtig. Wenn wir auf das Christentum sehen, so wird es uns wichtig sein, das Hellsehertum des Moses zu durchschauen, das uns in dem Traumbild vom brennenden Dornbusch dargestellt wird. Das ist es, was darzulegen war. Das eine soll nur noch hervorgehoben werden: daß diese neue Geisteswissenschaft fähig sein wird, aus sich selbst heraus das Bild des Welten-geschehens zu bilden, den Christus sozusagen geistig von Angesicht zu Angesicht zu schauen und ihn daher auf wahr-hafte Art wiederzufinden in den Evangelien. Wahrhaft vor­aussetzungslos ist nicht jene Bibelforschung, die da sagt:",
      "Wir wollen die Bibel erforschen wie eine andere Geschichte.",
      "- Denn sie setzt voraus das Dogma, daß es nur gewöhn­liche, sinnliche, natürliche Tatsachenzusammenhänge geben könne. Wahrhaft voraussetzungslos ist nur die Geistes­wissenschaft, und diese führt zu einer erneuerten Anerken­nung und Hochschätzung der Bibel in allen ihren Teilen. Es",
      "wird eine Zeit kommen, wo vielleicht diejenigen verstimmt sein werden, die heute sagen wollten, nur dem schlichten Verstande sei es gegeben, die Bibel zu erfassen. Diese Weis­heit muß die Bibel verkennen. Es wird die Zeit kommen, wo gerade die weiseste Weisheit am höchsten dasjenige schätzen wird, was uns in der Bibel gegeben wird, weil Sehertum sich dem Sehertum in der Bibel gegenüber er­blicken wird. Dann wird manches Wort, das im Neuen Testament geschrieben ist, in einem neuen Licht erscheinen. Es wird sich zeigen, daß ein Dokument wie die Bibel nichts verlieren kann durch unbefangene Forschung. Traurig stünde es, wenn irgendeine Forschung diese Bibel um ihr Ansehen, um ihren Namen bringen könnte. Eine Forschung, welche die Bibel um ihren Namen bringt, ist nur noch nicht weit genug gekommen. Die Forschung, welche bis an das Ende geht, wird die Bibel wieder in ihrer Größe darstellen.",
      "Frei darf der Mensch forschen. Wer die Ansicht hat, durch die Forschung könne die Religion zugrunde gehen, der zeigt damit nur, daß seine Religiosität auf schwachen Füßen steht. Die göttliche Wesenheit hat den Forschungs­trieb in des Menschen Wesen gelegt, damit er sich betätige. Eine Sünde gegen diesen Trieb wäre es, wenn man nicht forschend leben würde. Ich erkenne Gott durch die For­schung. Der Gott erkennt sich in meinem Forschen. Die Wahrheit ist ein Gut in der menschlichen Entwickelung, von der niemals das wahrhaft religiöse Leben etwas zu fürchten haben wird. Das aber ist eine Grundwahrheit, die das Neue Testament völlig durchzieht.",
      "Sie sollten nicht jene berücksichtigen, die aus Bequem­lichkeit die Menschen fernhalten wollen von der Bibel, und die sagen: Wenn ihr zu Philosophen kommt und die Bibel auslegt, so werden diese sagen, sie wollen nichts davon wis­sen. - Ein solches Forschen beruht aber auf Bequemlichkeit.",
      "Dasjenige Forschen dagegen ist berechtigt und richtig, das sagt: Wir können nicht tief genug gehen, um dasjenige zu verstehen, was in der Bibel steht. - Dasjenige Forschen in der Bibel ist das richtige, das in freier Forschung darauf eingeht und dann auch die Bibel im rechten Sinne erfassen wird. Diese Forscher begreifen die Wahrheit des Bibelwortes: Ihr werdet die Wahrheit erkennen, und die Wahr­heit wird euch frei machen."
    ],
    "sentences": [
      [
        "BIBEL UND WEISHEIT"
      ],
      [
        "Berlin, 14.",
        "November 1908"
      ],
      [
        "Daß die Geisteswissenschaft in der Lage ist, die tieferen Weisheiten und Wahrheiten der biblischen Urkunden zu er-forschen und dadurch erst die Möglichkeit hat, im richtigen Sinne wiederum dasjenige zu lesen, was in dieser Urkunde steht, das sollte im vorgestrigen Vortrage mit einigen Stri-chen angedeutet werden.",
        "Und mit einigen groben Strichen solhe gezeigt werden, wie gegenüber dem Alten Testamente ein solches richtiges Eindringen in den tieferen Sinn der Bibel in einer ganz unerwarteten Art möglich ist und viele Menschen zu einer Wiedereroberung dieser Urkunde für die Menschheit führen kann.",
        "Dasjenige, was in diesem letzten Vortrage gesagt werden konnte über die Stellung unserer neueren Zeit, ihre Forschung, ihre Kritik, ihre Weltanschau­ung gegenüber dem Alten Testament, das kann in einer ebensolchen Weise gesagt werden in bezug auf das Neue Testament.",
        "Auch hier sind wir wieder in der Lage, darauf hinzuweisen, wie im siebzehnten, achtzehnten Jahrhundert eine Kritik einsetzte, welche das Evangelium, also wiederum eine Urkunde, die durch Jahrhunderte hindurch für unzäh­lige Menschen eine so gewaltige Bedeutung hat, zerfasert, zergliedert, sozusagen in Stücke zerschnitzelt und an der Wurzel die Autorität angreift.",
        "Es müßte eine lange Ge­schichte erzählt werden, wenn aufmerksam gemacht werden sollte auf diese Bibelkritik des Neuen Testamentes im ein­zelnen.",
        "Wie konnte es auch anders kommen, da seit jener Zeit, nach der Erfindung der Buchdruckerkunst, die Bibel"
      ],
      [
        "in alle Hände gekommen ist, und als gleich damit das mate­rialistische Denken überhand nahm!",
        "Wie konnte es anders kommen, als daß immer deutlicher und deutlicher den Men­schen vor die Seele trat, daß sich Widersprüche in dem Evangelium finden?"
      ],
      [
        "Man braucht nur, wenn man sich rein an den äußeren Buchstaben der Sache hält, zum Beispiel das erste Evan­gelium mit dem Lukas-Evangelium zusammenzuhalten, man braucht nur zu vergleichen die Geschlechterfolge, welche angegeben wird, um die Abstammung des Jesus von Naza­reth anzugeben, und man wird finden, daß schon in den ersten Kapiteln das erste und das dritte Evangelium sich widersprechen.",
        "Nicht nur, daß die Ahnenglieder anders angegeben werden bei Lukas als bei Matthäus; auch die Namen stimmen nicht überein.",
        "Und wenn man von da aus­gehend die einzelnen Tatsachen in bezug auf das Leben des Jesus von Nazareth vergleicht, kann man überall Wider­sprüche finden.",
        "Insbesondere tritt den Menschen vor Augen, wie kraß sich die drei ersten Evangelisten, die Schreiber des Matthäus-,Markus-, Lukas-Evangeliums auf der einen Seite und der Schreiber des vierten, des sogenannten Johannes-Evangeliums, auf der anderen Seite, widersprechen.",
        "Die Folge davon war, daß man versuchte, wenigstens das Über-einstimmen der drei ersten Evangelien in einer gewissen Weise herauszustellen, und man glaubte zu finden, daß diese drei ersten Evangelisten, wenn sie auch in vielen Einzel­heiten voneinander abweichen, doch in gewisser Weise darin übereinstimmen, daß sie ein Bild des Jesus von Nazareth geben, das ansprechend ist für die ganze Auffassung und für alle Denkgewohnheiten einer neueren Zeit, wenigstens für viele Persönlichkeiten dieser unserer neueren Zeit."
      ],
      [
        "Dagegen war es seit langem in bezug auf den vierten Evangelisten vielen klar, daß da von einem historischen"
      ],
      [
        "Dokumente gar nicht die Rede sein könne.",
        "Nicht nur, daß der Schreiber des Johannes-Evangeliums, nachdem er ganz und gar die Tatsachen anders gruppiert bringt, vor allen Dingen in bezug auf das Erzählen der Wunder, die er in ganz anderer Art und Weise schildert; es zeigt sich auch, daß die ganze Stellung des Schreibers des Johannes-Evan­geliums zu dem Mittelpunkte der ganzen Weltgeschichte eine andere ist.",
        "Das ist ein Glaube, der sich immer mehr und mehr herausgebildet hat.",
        "Und wenn wir - wir können auf die Einzelheiten nicht eingehen - wieder auf den Sinn dieser Forschung hinsteuern wollen, so ist es etwa dieser, daß gesagt wird, die drei ersten Evangelien können, wenn man sie als Schilderungen aus der Glanzzeit betrachtet, das Bild geben der Persönlichkeit des ganz überragenden Jesus von Nazareth, des Gründers und Stifters des Evan­geliums.",
        "Das vierte Evangelium ist eine Bekenntnisschrift, eine Art Hymnus auf dasjenige, was der Schreiber in bezug auf seinen Glauben im Verhältnis zu dem gekreuzig­ten Jesus darstellen wollte, und wodurch er nicht eine Geschichte geben wollte, sondern eine Lehrschrift zu geben gedachte."
      ],
      [
        "Insbesondere im neunzehnten Jahrhundert hat sich diese Anschauung durch die sogenannte Tübinger Schule, die unter der Führerschaft des wirklich großen Bibelgelehrten, des genialen Kopfes Christian Baur stand, immer mehr ein­gelebt in die Gemüter zahlreicher Persönlichkeiten.",
        "Baurs Anschauung ist etwa diese: Das Johannes-Evangelium sei spät, sehr spät geschrieben worden, wogegen die anderen Evangelisten früher geschrieben haben, noch nach gewissen Predigten derjenigen, die vielleicht das eine oder andere selbst angesehen haben oder es erfahren haben von Personen, welche die Geschichte in Palästina miterlebt haben.",
        "Das Johannes-Evangelium aber sei erst im zweiten Jahrhundert"
      ],
      [
        "entstanden.",
        "Nicht aus der Urgeschichte heraus, sondern be­einflußt durch die griechische Philosophie, beeinflußt durch das, was in den christlichen Gemeinden schon aufgetreten war, sei geschrieben worden, so daß Johannes, durch das beeinflußt, ein Bild des Christus Jesus entworfen habe, das die Menschen so erbauen, so erheben hat können, daß es in gewisser Weise lyrisch ist, das unterrichtet über die Art und Weise, wie man bis ins zweite Jahrhundert hinein begon­nen hat, christlich zu denken, zu fühlen und zu empfinden, das aber nicht mehr unterrichten kann über dasjenige, was geschehen ist im Beginne unserer Zeit."
      ],
      [
        "Gewiß, es hat auch Seelen gegeben, welche die gegen­teilige Anschauung verfochten haben.",
        "Wenn man auf der anderen Seite wirklich sagen muß, daß Christian Baur und die, welche seine Schüler waren oder mehr oder weniger mit ihm gearbeitet haben, mit ungeheuer kritischem Scharfsinn vorgegangen sind, so dürfen wir doch einen Bibelforscher wie den Geschichtsschreiber und Gelehrten Girörer nicht vergessen, der in Anspruch nimmt, daß das Evangelium vom Apostel Johannes selber herrührt.",
        "Mit Fleiß zeigt er, wie gerade dieses Evangelium fast in jedem Satze zeigt, daß ein Augenzeuge es geschrieben hat oder daß es von einem geschrieben worden ist, der von Augenzeugen seine Bot­schaft erhalten hat.",
        "Gfrörer geht so weit, daß er in seiner schwäbischen Art und Weise sagt, daß jeder, der - nach dem von ihm Vorgebrachten - nicht daran glaube, daß das Evan­gelium von Johannes herrühre, nicht gut bei Trost sein könne.",
        "Auch gegen solche ist er nicht gut zu sprechen, welche sagen, es sei nicht historisch, und sodann mit allen möglichen Dingen diesem Evangelium zu Leibe rücken."
      ],
      [
        "Die Frage, die uns hier interessiert, ist diese: Hat wirk­lich keiner trotz allen Scharfsinnes, trotz aller Gelehrsam­keit, die keinen Augenblick in Abrede gestellt wird, hat"
      ],
      [
        "wirklich nur Forschung, wirklich nur Historie diese An­schauung der neueren Zeit herbeigeführt? - Wer gründlich nicht nur das Äußere der Geschichte durchforschen kann, sondern mit seinem Denken und Fühlen und mit seiner gan­zen Anschauung in die seelischen Untergründe der Mensch­heitsentwickelung hineintauchen kann, der bemerkt bald ein anderes.",
        "Es war nicht bloß der historische Sinn, es war nicht bloß die sogenannte objektive Forschung, sondern es waren die Denkgewohnheiten der neueren Zeit, die liebgeworde­nen Anschauungen, die seit dem letzten Jahrhundert, wo sie gegeben waren, immer mehr verbreitet wurden; sie ließen es nicht zu, daß über die Gestak des Christus Jesus in den Seelen sich weiter erhielten der Glaube und die Ideen, die seit Jahrhunderten geherrscht haben, daß in Jesus von Nazareth enthalten war nicht nur eine überragende, son­dern eine universale Wesenheit, eine Wesenheit - bezeich­nen wir sie zunächst als den Christus -, die als geistig-gött­lich nicht nur zur ganzen Menschheit in Beziehung gebracht werden muß, sondern zur ganzen Entwickelung der Welt überhaupt."
      ],
      [
        "Es verloren sich der Glaube und die Idee, daß diese Wesenheit gewirkt hat in dem sterblichen Leibe des Jesus von Nazareth, und daß wir da ein einzigartiges Er­eignis vor uns haben.",
        "Das widerspricht so sehr den Denk-gewohnheiten, daß sie sich gegeli einen solchen Glauben richten mußten."
      ],
      [
        "Da war es die kritische Forschung, die sich unbewußt einschlich, um recht zu geben dem, was die Ge­danken-Gewohnheiten vorerst wollten.",
        "Immer mehr und mehr kam der Sinn herauf, der nicht ertragen konnte, daß irgend etwas über das normale Menschlich-Persönliche hin­ausragt, der Sinn, der sich sagt: Ja, es hat große Menschen in der Weltenentwickelung gegeben: Sokrates, Plato oder andere."
      ],
      [
        "Gewiß, wir wollen zugeben, daß Jesus von Naza­reth der Größte war.",
        "Aber wir müssen innerhalb dieses"
      ],
      [
        "Menschheitsniveaus bleiben. - Daß in Jesu etwas gewohnt haben kann, das sich mit dem normalen Menschen nicht ver­gleichen läßt, das widerspricht den materialistischen Vor­stellungen, die sich immer mehr eingenistet haben, ganz besonders.",
        "Wir können sehen, wie dieser Sinn unbewußt eingeschlichen ist und sich mit dem verbunden hat, was die sogenannte historische Forschung feststellte."
      ],
      [
        "Warum wurden immer mehr und mehr die drei ersten Evangelisten die geschätzten und der Schreiber des Johan­nes-Evangeliums der bloße Lyriker und Bekenntnisschrei­ber?",
        "Weil man sich sagen konnte, die drei ersten Evange­listen, die Synoptiker, schildern eine ideale Menschenfigur, aber immer etwas, welches, wenn auch hoch, doch nicht dar­über hinausragt.",
        "Es schmeichelt dem modernen Sinn, wenn gesagt wird, was ein moderner Theologe gesagt hat: Wenn wir abziehen von dem Jesus von Nazareth alles Übersinn­liche und Spirituelle, wenn wir den schlichten Mann von Nazareth nehmen, dann sind wir dem Jesu am nächsten. -Das geht bei dem Johannes-Evangelium nicht an.",
        "Es beginnt gleich mit den Worten: Im Urbeginne war der Logos, das Wort.",
        "Und das Wort, das im Urbeginne bei Gott war, das war, bevor es eine materielle Welt gab.",
        "Was da war in allen geistigen Urgründen, das ist Fleisch geworden, das hat ge­wandelt im Beginne unserer Zeitrechnung in Palästina. -Die höchste Weisheit wendet der Schreiber des Johannes-Evangeliums an, um dieses Ereignis zu verstehen und zum Verständnis zu bringen.",
        "Gegenüber dieser Sache geht es nicht an, von dem schlichten Mann von Nazareth zu spre­chen.",
        "Daher durfte er niemals mit einer historischen Ur­kunde zu tun haben.",
        "Es sind also nicht allein wissenschaft­liche Gründe, es ist die Entwickelung der gewöhnlichen Ge­danken, Gefühle und Empfindungen, die ihren Ausdruck gefunden haben in dem, was heute als Bibelkritik des"
      ],
      [
        "Neuen Testamentes, was als sogenannte historische For­schung den Anspruch darauf macht, unbedingte oder wenig­stens relative Autorität über diese Dinge zu haben."
      ],
      [
        "Da entsteht aber aus der Geisteswissenschaft heraus eine weitere Frage.",
        "Stellen wir uns geradezu auf den Boden, auf den sich manche neue Forscher gestellt haben.",
        "Die einen wollten schildern ein Ereignis, das sich im Beginne unserer Zeitrechnung zugetragen hat."
      ],
      [
        "Diese setzten dannMythisches und Legendäres dazu.",
        "Nehmen wir an, wir stellten uns auf diesen Boden.",
        "Da müssen wir uns fragen: Ist eine Möglich­keit vorhanden, aus diesen Voraussetzungen heraus noch von einem Christentum als solchem zu sprechen?"
      ],
      [
        "Geht es an, von einem Christentum zu sprechen, wenn wir die Ur­kunden, die von diesem Christentum künden, in rein mate­rialistischem Sinne auffassen?",
        "Geht das an gegenüber der ganzen Bibel? - Zwei Dinge sollen zunächst angeführt wer­den, welche beweisen werden, daß die Frage gar nicht an­ders gestellt werden kann als wie sie gestellt worden ist, und daß sie andeutend beantwortet werden kann."
      ],
      [
        "Nehmen wir an, Christian Baurs Anschauung wäre richtig, daß in Palä­stina etwas geschehen sei, das so zu erklären ist wie die äußeren historischen Tatsachen, und daß im Laufe der Zeit die Schreiber aus den Vorurteilen ihrer Zeit heraus das­jenige der Nachwek überliefert haben, was in ihnen steckt.",
        "Nehmen wir an, wir müßten eine solche Forschung voraus­setzen, vor allem mit dem Glauben, daß eine geistigeWesen­heit aus geistigen Sphären heruntergestiegen sei, die ge­wohnt hat in Jesu von Nazareth, auferstanden ist, den Sieg des Lebens über den Tod davongetragen hat - was wir als die eigentliche Essenz des Mysteriums von Golgatha be­zeichnen."
      ],
      [
        "Mit dieser Lehre - sagt Baur - muß gebrochen werden.",
        "Diese Auffassung gilt als eine dogmatische.",
        "Diese Auffassung muß gestrichen werden.",
        "Es muß das Ereignis in"
      ],
      [
        "Palästina so untersucht werden wie ein anderes geschicht­liches Ereignis."
      ],
      [
        "Kann dann im wahren Sinne des Wortes von Christen­tum, überhaupt von der Bibel als einem solchen Werke gesprochen werden, das berichtet, was erscheinen muß?",
        "Demgegenüber sei auf zwei Tatsachen hingewiesen.",
        "Worauf beruht zunächst die erste große und umfassende Wirkung der christlichen Weltanschauung, eine Wirkung, die nie­mand leugnen kann, worauf beruht die Predigt des Paulus?",
        "Beruht sie auf dem, was eine neue nüchterne Forschung aus den Evangelien herausliest?",
        "Nimmermehr beruht des Paulus Kraft auf einer Verkündigung dessen, was mit den Mitteln einer Historie zu erschöpfen ist.",
        "Auf einem Ereignis, das nur aus übersinnlichen, niemals aus sinnlichen Ursachen zu begreifen ist, beruht die ganze Wirksamkeit des Paulus.",
        "Wer eintritt in eine Prüfung der Paulinischen Schriften, wird sehen, daß die ganze Lehre des Paulus einfach darauf beruht, daß er die Überzeugung und die Erfahrung gewin­nen konnte, daß der Christus auferstanden ist, und daß im Mysterium von Golgatha der Sieg des Lebens im Geiste über den Tod davongetragen worden ist."
      ],
      [
        "Woraus schöpft Paulus seine Überzeugung von der wah­ren Natur des Christus Jesus?",
        "Er schöpft sie nicht, wie etwa die anderen, die um den Christus Jesus herum waren, aus einer unmittelbaren Anweisung.",
        "Er schöpft sie, wie Ihnen allen bekannt ist, aus dem Ereignis von Damaskus.",
        "Er schöpft sie daraus, daß er sagen konnte: Ich habe den ge­sehen, der in Palästina gelebt und gelitten hat und gestor­ben ist, ich habe ihn gesehen in seinem Leben. - Nichts anderes meint Paulus, als daß er im Geiste den Christus gesehen hat und aus der geistigen Anschauung heraus die Wahrheit gewonnen hat, daß der Christus lebt.",
        "Den Chri­stus, den er kennengelernt hat in seiner geistigen Anschauung,"
      ],
      [
        "den verkündigt er.",
        "Und er stellt diese Erscheinung gleich den anderen Erscheinungen, denn er sagt uns klar:"
      ],
      [
        "Nach dem Tode ist der Christus verschiedenen Persönlich­keiten erschienen, den zwölf Jüngern und anderen, und zu­letzt auch mir als einer unzeitigen Geburt. - Damit meint er, daß er wirklich geschaut hat, in einer höheren Anschauung geschaut hat den, der den Sieg über den Tod davongetragen hat, und daß er seit jener Zeit weiß, daß für den, der in die geistige Welt sich erhebt, der Christus lebt."
      ],
      [
        "Hier stehen wir bereits mitten darinnen in bezug auf das Neue Testament, wo die neue Geisteswissenschaft sich schei­den muß von einer jeden bloß buchstäblichen Auffassung der Bibel.",
        "Was finden Sie in der Regel in den Schriften der sogenannten neuen Forschung über das Ereignis von Da­maskus?",
        "Sie finden darin in der Regel, daß es ein ekstati­scher Zustand war, in dem der Saulus zum Paulus wurde, ein Zustand, in den man nicht so ganz hineinschauen könne.",
        "Das entzieht sich der menschlichen Forschung.",
        "Ja, der äußeren menschlichen Forschung entzieht es sich.",
        "Das ist es aber gerade, was wir so oft in der Geisteswissenschaft be­tont haben, daß der Mensch - was wir weiter in den folgen­den Vortragszyklen lernen können - hinaufsteigen kann zu der Erkenntnis der höheren Welten.",
        "Das ist das, was um den Menschen herum ist, wie die Farbe des Lichtes um den Blinden.",
        "Sehen lernen kann der Mensch diese höhere Welt, wie der operierte Blindgeborene sehen lernen kann die Farben und das Licht.",
        "Das ist dasjenige, was sich durch die geisteswissenschaftlichen Methoden mit der Seele des wahren Schülers der Geisteswissenschaft vollzieht, was ihn fähig macht, hineinzuschauen in die geistigen Welten, um dasjenige selbst zu schauen, was da ist.",
        "Was sich mit diesem Schüler vollzieht, und wovon jeder Schüler heute und zu aller Zeit Zeugnis ablegen kann, das hat sich mit Paulus"
      ],
      [
        "vollzogen.",
        "Er hat es empfangen: zu hören mit Ohren, die nicht sinnliche Ohren sind, zu sehen mit Augen, die nicht sinnliche Augen sind.",
        "Er konnte dann auch Den wahrneh­men, der in Jesu von Nazareth gewohnt hat.",
        "Also in das Übersinnliche ragt die ganze Kraft des Paulus.",
        "Wenn man den ganzen Paulus nimmt, wie er ist, kann man sagen: Was er gesagt hat, ist durchglüht von dem «Christus lebt, er ist auferstanden.",
        "Daher ist nicht eitel unser Glaube»."
      ],
      [
        "Und wenn man darauf eingeht, was gerade des Paulus Predigt gewirkt hat, wie gerade er diejenige Gestalt des Christentums verbreitet hat, die durch die Welt gegangen ist, dann kann man nimmermehr sagen, es komme nicht darauf an, an irgendwelche übersinnliche Tatsachen an­zuknüpfen, um die Tatsachen über Jesus zu erforschen.",
        "Man müsse die gewöhnlichen wissenschaftlichen Formen anwen­den, sagt man.",
        "Man vergißt dann aber nicht nur die Ur­Tatsachen in Palästina, nicht nur das, was in den dreiund­dreißig Jahren geschehen ist, sondern auch dasjenige, was für die Verbreitung des Christentums geschah, man vergißt, daß es auf einem übersinnlichen Ereignis beruht, und daß dieses übersinnliche Ereignis zunächst zu verstehen und zu begreifen ist."
      ],
      [
        "Aber in ganz ähnlicher Weise finden wir auch, wenn wir nur ernst und wirklich die Dinge betrachten, daß das Alte Testament, wenigstens seine wichtigste Urkunde, die Schrif­ten des Moses, auf etwas Ähnlichem beruhen.",
        "Wir finden, daß die ganze Sendung des Moses, die ganze Kraft des Mo­ses, durch die er Ungeheueres für sein Volk geschaffen hat, auch auf einem übersinnlichen Ereignis beruht; wie wir vorgestern sagen mußten, daß, wenn sich der Geistesfor­scher hinaufentwickelt, so daß er sehend wird in der geisti­gen Welt und hineinblicken kann in die geistigen Unter­gründe der Dinge, daß er dann dasjenige, was Tatsachen"
      ],
      [
        "der geistigen Welt sind, überschaut in Bildern, den Imagi­nationen.",
        "Ja, man kann auch die Vorgänge, die in einem selbst geschehen, wenn man so hinaufsteigt in die geistigen Gefilde, nur in Bildern ausdrücken, wobei aber klar sein muß, daß der, welcher in solchen Bildern spricht, nicht über die Bilder als solche sprechen will, sondern meint, daß man in diesen Bildern das Ausdrucksmittel hat für seine über­sinnlichen Erlebnisse."
      ],
      [
        "Das übersinnliche Erlebnis, durch das Moses seine Sen­dung bekommen hat, ist uns deutlich geschildert in der Erscheinung des brennenden Dornbusches.",
        "Da sehen wir, wie Moses, der Leiter und Lenker des Volkes, sich seinem Gott gegenübergestellt sieht, dem Gotte Abrahams, Isaaks und Jakobs, der dem Moses den Auftrag gibt, das für sein Volk zu tun, was wir dann als Moses' Tat geschehen finden.",
        "Indem wir dieses heranziehen, stehen wir bereits vor einem Grundnerv der ganzen Bibel, nämlich vor der Frage: Wie haben wir uns überhaupt behufs eines tieferen Eindringens in diese Urkunde zu diesen zwei Tatsachen zu stellen, auf die wir hingewiesen haben als übersinnliche Tatsachen, die eine jede bloß äußerliche Forschung unmöglich machen?",
        "Wie haben wir uns zu diesem Grundnerv der Bibel in gei­steswissenschaftlichem Sinn zu verhalten?",
        "Wir werden ein­dringen können, wenn wir uns den Inhalt der Offenbarung oder des Erlebens des Moses vor Augen führen."
      ],
      [
        "Die wichtigsten Züge seien nur angeführt.",
        "Moses sieht sich gegenüber dem Gotte Abrahams, Isaaks und Jakobs.",
        "Der Gott gibt ihm zu gleicher Zeit den Auftrag, das Volk aus Ägypten hinaus zu führen, es zu einer bestimmten Größe und zu einem bestimmten Verhalten zu bringen.",
        "Als dann Mos es etwas haben will, wodurch er sich rechtfertigen kann vor dem Volke, damit er sagen könne, wer er sei und wer ihn schickt, da enthüllt der Gott seinen Namen: «Ich"
      ],
      [
        "bin der Ich-bin.>> Dieses Wort kann niemand verstehen, der nicht auf den ganzen Sinn und das Wesen alter Namen­gebung einzugehen in der Lage ist.",
        "Alte Namengebungen sind nicht die heutigen Namengebungen."
      ],
      [
        "Alte Namenge­bungen sollten durchaus ausdrücken das Wesen der Per­sönlichkeit, das Wesen dessen, der uns entgegentritt.",
        "In dem «Ich bin der Ich-bin» mußte sich in ganz bestimmter Art das Wesen des Gottes ausdrücken, der dem Moses gegen­überstand, und der sich nennt «der Gott Abrahams, Isaaks und Jakobs»."
      ],
      [
        "Warum nennt er sich der Gott Abrahams, Isaaks und Jakobs?",
        "Dahinter liegt ein Geheimnis, das ent­rätselt sein will.",
        "Wir können es nur enträtseln, wenn wir mit den Mitteln der Geisteswissenschaft daran herantreten."
      ],
      [
        "Wir werden es in den verschiedenen Stellen immer wieder hervorzuheben haben, daß der Mensch besteht aus den verschiedenen Gliedern seiner Wesenheit, daß wir in dem, was wir den physischen Leib nennen, nur einen Teil des Menschen vor uns haben, daß wir außer diesem höhere Glieder haben, die übersinnlich sind, die die eigentlichen Grundlagen, die schöpferischen Prinzipien sind.",
        "Wir müs­sen hinzufügen dem physischen Leib den Äther- oder Le­bensleib, dann den Astralleib und als viertes Glied den Ich-Träger."
      ],
      [
        "Den physischen Leib hat der Mensch gemein­schaftlich mit den scheinbar leblosen Wesen, mit den Mine­ralien, den Ätherleib mit den Pflanzen und allen leben­digen Wesen, den Astralleib mit den tierischen Wesen, mit dem, was Leidenschaften und Begierden haben kann.",
        "Durch das Ich ragt der Mensch über alle sinnlichen Wesen, die ihn umgeben, hinaus."
      ],
      [
        "Das sind die vier realen Glieder der menschlichen Wesenheit, welche die Geisteswissenschaft im­mer anerkannt hat."
      ],
      [
        "Hinweisen müssen wir darauf, daß das, was wir heute den physischen Leib nennen, ebenso seinen geistigen Urgrund"
      ],
      [
        "hat und nur verdichtet ist aus dem Geistigen.",
        "Wie das Eis aus dem Wasser, so ist das Physische aus dem Gei­stigen heraus entstanden.",
        "Wir müssen weit zurück gehen in der Anschauung der Geistesentwickelung, wenn wir die ersten geistigen Ursprünge des physischen Menschenleibes suchen wollen.",
        "Von den vier Gliedern der menschlichen Wesenheit ist dieses vierte Glied durchaus das älteste.",
        "Der physische Leib ist heute der dichteste.",
        "Er ist das, was vom Geiste ausgegangen ist in ferner Vergangenheit.",
        "Er ist im­mer dichter und dichter geworden, durch manche Umwand­lungen hindurch gegangen und hat dadurch seine physische Gestalt angenommen.",
        "Das ist das älteste am Menschen.",
        "Ein jüngeres Glied ist der Äther- oder Lebensleib.",
        "Er ist später hinzugekommen, daher er sich auch in einem geringeren Verdichtungsgrade darstellt.",
        "Noch jünger ist der Astralleib.",
        "Das jüngste Glied ist das Ich, der Träger des menschlichen Selbstbewußtseins.",
        "Alle diese Glieder sind aus geistigen Urgründen und geistigen Wesenheiten, aus göttlich-geisti­gen Wesenheiten heraus entstanden.",
        "Wir können sagen, die Geisteswissenschaft zeigt uns, daß dieses Ich, wodurch der Mensch die heutige selbstbewußte Wesenheit geworden ist, sich hineingesenkt hat in den Leib.",
        "Er war zusammenge­fügt, bevor er Ich-Wesenheit wurde, aus physischem, Äther-und Astralleib."
      ],
      [
        "Diejenigen Wesenheiten nun, welche die Schöpfer, die Bildner dieser drei Glieder der menschlichen Wesenheit sind, die unterscheidet auch die Bibel.",
        "Die Lehre des Moses spricht von dem Schöpfer, dem Bildner des menschlichen Ichs, von dem Schöpfer des Trägers des menschlichen Selbst­bewußtseins.",
        "Daher sieht auch die Bibel in dem Gotte, der in den Menschen einfließen ließ das Ich, sozusagen den, der am letzten darangekommen ist in bezug auf die Evolution des Menschen.",
        "Die göttlichen Wesenheiten, die als die Elohim"
      ],
      [
        "bezeichnet werden, die wir streng unterschieden haben von dem Gotte Jahve oder Jehovah, diese göttlichen We­senheiten sind die Schöpfer von dem physischen, ätherischen und astralischen Leib.",
        "Sie sind in der Bibel genau unter­schieden von dem letzten in unserer Evolution auftretenden Gott, von dem Jahve-Gott, von dem, der dem Menschen das Ich gebracht hat.",
        "Wenn wir fragen: Wo findet der Mensch die Wesenheit dieses Gottes, dieses jüngsten der schöpferischen Götter, von dem die Bibel zu sprechen be­ginnt im vierten Vers des zweiten Kapitels der Genesis? -da zeigt uns die Geisteswissenschaft, daß da, wo der Mensch in sich sein Ich findet, das sich so wesentlich, schon seinem Namen nach, von allen anderen Wesenheiten um uns herum unterscheidet, daß er da findet in sich einen Tropfen dieser göttlichen Wesenheit.",
        "Das ist keine pantheistische Lehre, auch keine Erklärung dafür, daß der Mensch seinen Gott in sich zu finden hat.",
        "Das zu behaupten wäre gleich dem, der behauptet, ein Tropfen Wasser ist dasselbe Wesen wie das Meer - und sagt: dieser Tropfen Wasser ist das Meer."
      ],
      [
        "Wenn wir sprechen im Sinne der Geisteswissenschaft, so sprechen wir von einem Unendlichen, Umfassenden, Uni­versalen, das verknüpft ist mit der irdischen Entwickelung und dem anderen, was zu dieser irdischen Entwickelung gehört.",
        "In unserem Ich finden wir einen Funken dieser Jahve-Gottheit, wie in dem Wassertropfen dieselbe Wesen­heit ist wie im Meer.",
        "Aber es war der Weg, den die Ent­wickelung des Menschen zurücklegen mußte, ein sehr langer, wobei die Jahve-Gottheit anfing, den Menschen so zu for­men, daß er das Ich mit dem Bewußtsein erfassen konnte.",
        "Die Kraft des Ichs mußte vorher lange im Menschen arbei­ten, bevor der Mensch zum Bewußtsein des Ichs kam.",
        "Moses wurde der große Vorläufer in dem Bringen des Bewußtseins"
      ],
      [
        "des Menschen zum Ich.",
        "Aber diese Kräfte arbeiten und bilden schon lange an der menschlichen Evolution vorher.",
        "Sie bilden so, daß wir ihre Weise erkennen können, wenn wir uns etwas mit der Evolution des menschlichen Bewußt­seins selber beschäftigen."
      ],
      [
        "Blicken wir ein wenig zurück in der Entwickelung des menschlichen Bewußtseins.",
        "Das Wort Entwickelung braucht man heute sehr häufig, aber so durchgreifend, so intensiv wie die Geisteswissenschaft Ernst macht mit dem Worte Entwickelung, so ist es bei keiner anderen Wissenschaft der Fall."
      ],
      [
        "Dieses menschliche Bewußtsein, wie es heute ist, hat sich aus anderen Bewußtseinsformen entwickelt.",
        "Wenn wir weit, weit zurückgehen in der Herkunft des Menschen, nicht im Sinne materialistischer Wissenschaft, sondern so, wie ich es vorgestern entwickelt habe, dann finden wir, daß das Menschen-Bewußtsein immer mehr als ein anderes erscheint, je weiter wir zurückgehen."
      ],
      [
        "Dieses Bewußtsein, welches die verschiedenen Verstandesbegriffe, die äußeren Sinneswahr­nehmungen in der bekannten Art verknüpft, das ist erst entstanden, wenn auch in urferner Vergangenheit, aber es ist erst entstanden.",
        "Wir können in jener Zeit einen Zustand des Bewußtseins finden, der ganz anders war als heute, weil besonders das Gedächtnis ganz anders war."
      ],
      [
        "Das, was der Mensch heute als Gedächtnis hat, ist nur ein herunterge­kommener Rest einer alten Seelenkraft, die in ganz anderer Weise vorhanden war.",
        "In alten Zeiten, als der Mensch noch nicht die kombinierende Kraft seines heutigen Verstandes hatte, als er noch nicht imstande war, zu rechnen und zu zählen im heutigen Sinne, als er noch nicht seine Verstan­deslogik ausgebildet hatte, da hatte er dafür eine andere Kraft der Seele: er hatte ein universelles Gedächtnis aus­gebildet."
      ],
      [
        "Dieses mußte abnehmen, mußte zurücktreten, damit auf seine Kosten unser heutiger Verstand zu seiner"
      ],
      [
        "Entwickelung kommen konnte.",
        "So ist überhaupt der Gang der Entwickelung, daß eine Kraft in den Hintergrund tritt, damit die andere auftauchen kann.",
        "Das Gedächtnis ist eine abnehmende Kraft, der Verstand und die Vernunft sind zunehmende Seelenkräfte."
      ],
      [
        "Für diejenigen, die schon längere Jahre hier diese Vor­träge hören, kann es nicht etwas besonders Wunderbares sein, was ich jetzt sagen werde.",
        "Für die anderen wird es grotesk erscheinen, wenn über die Natur des Gedächtnisses in der folgenden Weise gesprochen werden wird.",
        "Was ist das Äußere des menschlichen Gedächtnisses?",
        "Es ist das, daß es sich zurückerinnert an gestern, vorgestern und so weiter, bis in die Kindheit.",
        "Dann reißt es aber einmal ab.",
        "Dieses Gedächtnis riß nicht ab in urferner Vergangenheit, nicht in der Kindheit, nicht einmal bei der Geburt; sondern wie der heutige Mensch sich erinnert an dasjenige, was er selbst in seinem persönlichen Leben erlebt hat, so erinnerte sich der Mensch der Vorzeit an dasjenige, was der Vater, der Groß­vater, was die ganze Generation hindurch erlebt hat.",
        "Das Gedächtnis war durch Generationen hindurch eine Seelen-kraft, die sich real verbreitete.",
        "Durch Jahrhunderte hin­durch hat sich in urferner Vergangenheit die Erinnerung erhalten, und mit dieser anderen Ausbildung des Gedächt­nisses hing eine andere Art der Namengebung zusammen."
      ],
      [
        "Wir kommen nun zu der Frage: Warum ist in den ersten Kapiteln der Bibel von Individualitäten die Rede, die wie Adam, Noah Jahrhunderte alt werden?",
        "Weil es für die Menschen, die hier gemeint sind, keinen Sinn hätte, die Per­sonen zu begrenzen.",
        "Die Erinnerung reicht hinauf durch Generationen bis zu dem Urvater.",
        "Dieser ganzen Genera­tion gab man einen Namen.",
        "Es hätte keinen Sinn gehabt, einer einzelnen Persönlichkeit den Namen Adam zu geben.",
        "So gab man dazumal den Namen dem, was sich, die gleiche"
      ],
      [
        "Erinnerung festhaltend, durch Jahrhunderte hindurch von Generation zu Generation zurückerinnerte - Adam, Noah.",
        "Und was war das?",
        "Es war das, was durch Vater, Sohn und Enkel geht, aber die Erinnerung bewahrte.",
        "So treu bewahrt die biblische Urkunde die Geheimnisse der Geisteswissen­schaft."
      ],
      [
        "Wenn wir das Bewußtsein des Ichs, durch das wir die Wesenheit der Jahve-Gottheit erfassen, betrachten, so wer­den wir sehen, daß das Ich in uns lebt zwischen Geburt und Tod, und daß es diese seine einerlei Art aufrechterhält zwi­schen Geburt und Tod.",
        "So hielt das Ich sich damals durch Generationen, durch Jahrhunderte hindurch aufrecht."
      ],
      [
        "Wie wir heute von dem Ich sprechen und wissen, daß das Ich zurückgeht so weit, wie wir uns erinnern, ebenso sagte sich der Mensch der Urzeit: Mich selbst ein Ich zu nennen, hat keinen Sinn.",
        "Ich erinnere mich zurück an meinen Vater, Großvater, Urgroßvater. - Sein Ich ging durch die Genera­tionen, und es hatte sogar einen Namen."
      ],
      [
        "Wie wir in unse­rem persönlichen Ich einen Ausdruck des Gottes finden, wenn wir uns in dieses Ich vertiefen, so sagte sich der alte Mensch, indem er hinaufsah durch die Generationen: Der Gott, der in dem Ich lebt, lebt durch Generationen hinun­ter, - als eine Gottheit, die dann Moses in den höheren Welten erkannte.",
        "Der Gott war kein anderer als der, welcher sich in alten Zeiten als ein Ich von Generation zu Generation hindurch gelebt hat."
      ],
      [
        "Man bezeichnete als Ich, in der Aus­drucksweise der damaligen Zeit, was sich als Ausdruck des Jahve-Gottes fortpflanzte, mit dem Jahve-Worte «Ich bin der Ich-bin».",
        "Das war das, was Moses in seiner geistigen Offenbarung erkennen lernte."
      ],
      [
        "Im Erschauen des brennen­den Dornbusches ist das zum ersten Male offenbart worden.",
        "Es war derselbe Gott, der früher von Generation zu Gene­ration herunter gelebt hat, der Gott Abrahams, Isaaks und"
      ],
      [
        "Jakobs.",
        "Es war die Kraft, die also in der lebendigen Er­innerung fortlebte und zu gleicher Zeit alles mit sich brachte, was die menschliche Ordnung begründete.",
        "So schauen wir hinauf auf die Vorgängerschaft des Moses.",
        "Im biblischen Sinne schauen wir hinauf bis zu den Patriarchen, bis zu denen, in welchen der Gott Abrahams, Isaaks und Jakobs lebte."
      ],
      [
        "Diese Zeiten brauchten keine äußeren Gebote, keine äuße­ren Gesetze.",
        "Denn mit dem lebendigen Gedächtnis, mit des­sen ganz anderer Art als das Gedächtnis heute ist, lebte sich fort dasjenige, was man zu tun hatte.",
        "Wonach handelte man in diesen Urzeiten?",
        "Man kommt darauf, wenn man die Bibel richtig versteht.",
        "Man handelte nicht nach Geboten.",
        "Man handelte nach dem, was einem die Erinnerung sagte, was der Vater, der Großvater und so weiter getan haben.",
        "Mit seinem Blute bekam man eingeboren die Richtung zu dem, was man zu tun hatte.",
        "Es war in diesen alten Genera­tionen etwas wie ein vergeistigter Instinkt.",
        "Wenn wir heute, als Vergleich gebraucht, sagen: «aus Instinkt heraus han­deln», so ist das ein Gebot.",
        "Nein, der alte Mensch handelte nach dem Charakter seines Wesens, nach seinem Gattungs­wesen.",
        "Wie handelten die mit Abraham, Isaak und Jakob in der Bibel bezeichneten Wesen?",
        "Sie handelten so, wie das durch die Generationen rinnende Blut es ihnen eindrückte.",
        "Der Gott Jahves war es, den sie heruntergebracht hatten mit ihrem Ich, ob sie Krieg führten, ob sie in Frieden lebten.",
        "Gebote hatten sie nicht, ein Gesetz hatten sie nicht.",
        "Es war der vergeistigte Instinkt Gottes, der in ihnen lebte."
      ],
      [
        "Zu der Zeit, als Moses auftrat, da war die menschliche Persönlichkeit auf der ersten Stufe ihrer Ausbildung.",
        "Da riß sie sich los in ihrem Bewußtsein von diesem gemein­samen Bewußtsein der Generation.",
        "Da hatte schon gründ­lich aufgehört das Gedächtnis, das durch die Generationen"
      ],
      [
        "hinaufreichte.",
        "Da hatte man nicht mehr den vergeistigten Instinkt zum Handeln.",
        "Da mußte etwas anderes an dessen Stelle treten.",
        "Da mußte der Gott Abrahams, Isaaks und Jakobs, der in seiner geistigen Naturgestalt Moses das Ge­setz, die Gebote gab, weil man nicht mehr den vergeistigten Instinkt hatte, da mußte er die äußere Ordnung, das soziale Zusammenleben durch die Gebote, durch das Gesetz regeln."
      ],
      [
        "So ist derselbe Gott, der vordem als Naturkraft gewirkt hat, jetzt als Gesetzgeber wirksam, um die äußere Ordnung auf dem Gesetzeswege zu begründen.",
        "So sehen wir, daß es einen tiefen Sinn hat, an dieser Stelle die Worte zu lesen:"
      ],
      [
        "der Gott Abrahams, Isaaks und Jakobs.",
        "Der Gott, der sich bezeichnet als der Gott «Ich bin der Ich-bin», er ist der­selbe wie das vierte Glied der menschlichen Wesenheit, der­selbe, der das Ich in die menschliche Wesenheit einfließen ließ.",
        "Aber die Menschen konnten die geistige Natur des Ichs nicht in ihr Bewußtsein aufnehmen.",
        "Dazu bedurfte es wieder einer längeren Vorbereitung, und diese fällt in die Zeit, die uns durch die Bibel als das Alte Testament geschil­dert wird, in die Zeit von Moses bis zum Mysterium von Golgatha.",
        "Daher ist diese Zeit eine Zeit der Verheißung, die das neue Evangelium darstellt, der Beginn der «Zeit der Erfüllung».",
        "Es kündigt sich also dem Moses der Gott an, der den Ausdruck fand «Ich bin der Ich-bin».",
        "Er kündigt sich so an, daß er die äußere Ordnung der Menschen, das Zusammenleben derselben durch Gesetze ordnet, auf dem Umwege durch Mosis Schauen, durch Mosis Sehen.",
        "So lebte die Menschheit in der vorchristlichen Zeit, in der der Gott schuf, in der der Jahve-Gott bildete, in der der «Ich bin der Ich-bin» lebt, welcher aber noch nicht bewußt leben konnte, sondern nach dem äußerlichen Gesetze, das aber von ihm stammte.",
        "Immer mehr rückt die Zeit heran, wo sich die Menschheit des vollen Ichs bewußt werden sollte.",
        "Durch das"
      ],
      [
        "ganze Altertum hindurch gab es nur ein Mittel für die Men­schen, die noch nicht schauen konnten, noch nicht entgegen­treten konnten dem Gott in der physischen Welt.",
        "Nur eine Art gab es, wie dieser Gott für sie wirksam werden konnte.",
        "Das war das Gesetz, die Ordnung.",
        "Das galt für die äußere Welt."
      ],
      [
        "Außerdem gab es eine übersinnliche Art, diesen Gott kennenzulernen, und das waren die Mysterien oder die Einweihung.",
        "Was war die Einweihung?",
        "Alles das, was ge­wissen Persönlichkeiten überliefert wurde, welche dazu ge­eignet befunden wurden, die Methoden anzuwenden, die die geisteswissenschaftliche Forschung hat, um die im Men­schen schlummernden Kräfte und Fähigkeiten zu entwickeln, so daß sie in die geistige Welt hineinschauen konnten.",
        "Für die Bekenner des Alten Testamentes würde es daher so sein, Gott, der in dem «Ich-bin» lebt, geistig von Angesicht zu Angesicht zu sehen.",
        "Wenn sie diese Methode anwendeten, wurden sie in die Lage versetzt, mit geistigen Augen und Ohren zu hören und zu sehen, selbst zu sehen, was Moses gesehen hat, als ihm der Gott, der «Ich-bin», die Mission erteilt hat.",
        "Aber nur in den Mysterien, nur durch die Ein­weihung war das möglich."
      ],
      [
        "Aber es gab auch solche, die den «Ich bin der Ich-bin» er­kannten, aber sie mußten dazu alle die Prozeduren, die Methoden durchmachen, wodurch sich der Mensch umge­staltet zu einem Instrumente des höheren Schauens, des Hineinblickens in die geistige Welt.",
        "So also war diejenige Gottheit, die schon in Abraham, Isaak und Jakob lebte, nach außen für die physische Welt ganz verhüllt.",
        "Sie ord­nete die Welt durch das Gesetz.",
        "Für den Eingeweihten wird im Denken das Geheimnis der Mysterien schaubar.",
        "Nun kam die Zeit, in der das Mysterium von Golgatha sich voll­ziehen sollte.",
        "Was war da eigentlich geschehen?",
        "Stellen wir"
      ],
      [
        "uns so richtig vor die Seele, was den Eingeweihten in den alten Zeiten passierte.",
        "Nur skizzenhaft schildern kann ich Ihnen den Vorgang der Einweihung durch Meditation, Konzentration und die anderen Übungen."
      ],
      [
        "Durch diese wurde die Seele des Einzuweihenden lange vorbereitet.",
        "Dann kam ein dreieinhalb Tage währender Abschluß die­ser Einweihungsvorgänge.",
        "Da wurde der Mensch, der ein­geweiht werden sollte und der so weit war, durch den Ein­weihungsweisen in einen Zustand gebracht, durch den sein physischer Leib vollständig schlafend war."
      ],
      [
        "Nicht nur schla­fend war er, sondern wie tot, so also, daß der Mensch sich seiner physischen Sinne, seiner physischen Augen und Ohren nicht bedienen konnte.",
        "Dafür aber sah er durch die Organe seiner geistigen Glieder hinein in die geistigen Welten."
      ],
      [
        "Er konnte da wahrnehmen, wenn er außerhalb seines Leibes war, wenn er nicht gefesselt war, wenn er in Latenz der physischen Organe war.",
        "Er konnte dann in sich schauen, was unsichtbar in ihm lebte als das «Ich bin der Ich-bin»; aber er konnte es nur in den Tiefen der Mysterien schauen."
      ],
      [
        "Dann wurde er - wie jeder weiß, der diese Dinge kennt - auf­geweckt in seinem physischen Leibe und bediente sich wie­der der physischen Sinne.",
        "Aber er hatte jetzt das volle Be­wußtsein: «Ich bin der Ich-bin, ich war in der geistigen Welt."
      ],
      [
        "Das, was zu Moses gesprochen hat: , das stand vor mir, und es ist das, was mir die Ewigkeit verwehrt, das, was in meinen Leib eingezogen ist.",
        "Mit dem war ich verbunden.",
        "Ich war mit dem göttlichen Urträger des Ich-bin verbunden, dessen Abglanz und Spiegelbild mein Ich-bin ist.»"
      ],
      [
        "So kehrte der Eingeweihte zurück in die physische Welt und wurde Zeuge dafür, daß es ein Geistiges gibt im Ich, denn er hatte es geschaut.",
        "Kunde und Botschaft konnte er ablegen vor seinen Zuhörern, denen er Botschaft zu geben"
      ],
      [
        "berufen war.",
        "So konnte man aber nur in der geistigen Welt sehen den «Ich bin der Ich-bin».",
        "Durch das Ereignis von Golgatha stieg dieselbe Wesenheit, die sich angekündigt hatte bei Moses in dem brennenden Dornbusch mit den Worten «Ich bin der Ich-bin», herab in die Menschen.",
        "Das ist ganz im Sinne des Johannes-Evangeliums: Das Ich ist Fleisch geworden in dem Leibe des Jesus von Nazareth, wohnte in demselben und wandelte unter den Menschen.",
        "Das war die Urkraft, die gerade den Menschen auf die Höhe gebracht hat, auf der er heute steht.",
        "Die Urkraft wurde Mensch; eine Gott-Wesenheit war Mensch geworden und wandelte unter den Menschen.",
        "Die Möglichkeit war da, daß innerhalb des geschichtlichen Verlaufs der Menschheit das einmal als historisches Ereignis da war, was die Ein­geweihten nur im Geiste erschauen konnten, was auf Gol­gatha sich als historisches Ereignis vollzogen hat: daß das Christus-Wesen den Sieg über den Tod der Materie davon­getragen hat."
      ],
      [
        "Das ist das Historisch-äußerlich-Wirkliche, das sich in den Mysterien so und so oft an den Eingeweihten vollzogen hat.",
        "So ist der Verlauf der Dinge, die während der alten Zeiten in dem tiefen Dunkel der heiligen Mysterien sich ereigneten bei denen, die durch dreieinhalb Tage ihren phy­sischen Leib nach dem Eingeweihten-Drama verließen, und die während dieser Zeit in der geistigen Welt wandelten und in die geistigen Urgründe des Menschen schauten.",
        "Daß dieses Ereignis herabsteigt in die physische Welt und sich als historische Tatsache darstellt, das ist der Verlauf."
      ],
      [
        "Jetzt aber kam die Menschheit durch die Hinneigung der Gefühle und Empfindungen und Gedanken zu dem Ereignis von Golgatha durch den Glauben.",
        "Dann wurde das Ver­ständnis daraus.",
        "Es war etwas Neues gegeben.",
        "Es war ge­geben, das äußerlich zu haben, was man sonst nur durch"
      ],
      [
        "das Entrücktsein in der geistigen Welt haben konnte.",
        "Wenn man das so annimmt, dann verstehen wir, warum der Chri­stus Jesus sagt: Ich bin der Ich-bin in einer völlig neuen Gestalt. - Er sagt: Blickt zurück in die Urzeiten, in das­jenige, was als das Ewige im Menschen gelebt hat, das sich herunter gelebt hat in Abraham, Isaak und Jakob, das sich dann in dem Gesetze des Moses kundgegeben hat.",
        "Jetzt ist die Zeit da, wo das Ich sich bewußt wird in der einzelnen Persönlichkeit, wo der Mensch sich in seinem Ich, in dem in ihm wohnenden Göttlichen, voll bewußt werden soll."
      ],
      [
        "War es in den alten Zeiten so, daß der Mensch hinauf-schaute zu dem Gott, daß er schaute und sich sagen konnte:"
      ],
      [
        "Was in mir lebt, das lebt durch die Generationen, - so ist es jetzt so, daß, wenn er in sich hineinschaut, er das Göttliche in seinem Ich findet.",
        "Das Göttliche, aus dem jedes Ich her­vorgegangen ist, das war der Körper des Jesus von Naza­reth, und der das verstand, der schrieb: Im Urbeginne war das Wort, und das Wort war bei Gott, und Gott war das Wort. - Mit dem Wort ist das Wesen der innersten Men­schennatur und zugleich der Urquell dieses innerstenWesens gemeint.",
        "Und dem Matthäus legt er in den Mund: Das, was in mir lebt, von dem ein Funke in jeder menschlichen Per­sönlichkeit ist, das war, ehe das Evangelium war. - Der bedeutsame Satz in dem Johannes-Evangelium war: «Ehe denn Abraham ward, bin Ich.» - Bevor ein Abraham war, war das «Ich-bin», das Ich-bin, das nicht an eine Zeit ge­bunden ist, das vor Abraham war, das da war schon in den geistigen Urgründen des Menschen.",
        "Indem er sich selber als den Urquell des Ich-bin bezeichnen mußte, sprach der Chri­stus das bedeutsame Wort: Ehe Abraham ward, war das Ich-bin."
      ],
      [
        "So sehen wir, wie der Sinn der Menschheitsentwickelung, wie ihn die Geisteswissenschaft wieder lebendig macht, in"
      ],
      [
        "dem ganzen Grundbuch der Dinge durch das Alte und das Neue Testament hindurchflutet.",
        "Und wir sehen, wie uns die wichtigsten Worte erst lesbar werden, wenn wir den Sinn der Worte, unabhängig von den Worten, durch die Geistes­wissenschaft ergründen.",
        "Um etwas anzuführen, was dem materialistischen Sinn im Geiste zu bedenken gibt, sei an die Auferweckung des Lazarus erinnert.",
        "Sehen Sie, sagt ein solcher Mann wie Gfrörer: Wer behauptet, das Johannes-Evangelium sei nicht von Johannes geschrieben, der hilft sich damit, daß er sagt, vieles hat der Schreiber hingeschrie­ben, so wie er es erlebt und verstanden hat, aber das Laza­rus -Wunder muß ihm erzählt worden sein.",
        "Da kann er nicht dabei gewesen sein. - Man muß das Lazarus -Wunder nur richtig verstehen.",
        "Fassen wir es doch so, daß der Chri­stus, als er in die Welt trat, den Leib des Jesus von Naza­reth annahm.",
        "Fassen wir es doch so, daß das, was im Alten Testamente vorbereitet wurde, im Neuen seinen Ausdruck gefunden hat.",
        "Er mußte da eine Persönlichkeit haben, die ihn vollständig verstehen konnte, die im tiefsten Sinne ein­dringen konnte in das, was er verkündigen konnte, das heißt, er mußte auf seine Art eine Persönlichkeit einweihen."
      ],
      [
        "Einweihungsgeschichten werden uns zu allen Zeiten unter Verhüllung erzählt.",
        "Das Lazarus -Wunder ist nichts anderes als die wunderbare und gewaltige Darstellung, wie der Christus den ersten Eingeweihten des Neuen Testamentes geschaffen hat, wie der Eingeweihte bei seinem Schüler, der dreieinhalb Tage in einem todähnlichen Zustande lag, die Seele wieder zurückrief in den Leib, nachdem sie die Wan­derung durch die geistige Welt gemacht hatte, um nachher durch den Christus selbst erweckt zu werden.",
        "Alles das ist leicht zu durchschauen von dem, der etwas davon versteht, denn es ist die Sprache, in der überhaupt Einweihungs­geschichten erzählt werden.",
        "Der Sohn Gottes soll durch die"
      ],
      [
        "Krankheit geehrt werden - zur Ehre Gottes.",
        "Das bedeutet äußeres Erscheinen als Offenbarung des Inneren; so daß der Satz in Wahrheit zu übersetzen ist: Die Krankheit ist nicht zum Tode, sondern daß der Gott als äußere Erscheinung offenbar werde, damit er auch für die Sinne geoffenbart werden könne. - In der Persönlichkeit des Lazarus schlum­mert die tiefere menschliche Wesenheit, die die Fähigkeit und die Kraft hat, daß sie in geheimnisvoller Art in ihm entwickelt werden konnte, hinaufgeführt werden konnte in die geistige Welt, so daß er erkennen konnte das Wesen des Christus selber, des Sohnes Gottes.",
        "Diese Kraft mußte aber erst entwickelt werden.",
        "Er entwickelte sie in Lazarus, damit das Göttliche, das in Lazarus ruhte, offenbar werden könne, und offenbaren könne dasjenige, was der Sohn Got­tes sei.",
        "So schafft der Christus Jesus in Lazarus den ersten, der aus eigener innerer Beobachtung weiß, wer der Christus Jesus eigentlich ist.",
        "Zu gleicher Zeit zeigt dieses Wunder"
      ],
      [
        "- denn es ist für den, der nur die äußeren physischen Ge­setze gelten lassen will, ein echtes Wunder -, was der betref­fende Schüler während der dreieinhalb Tage durchmachen muß, denn das kommt einem echten Tode gleich, weil der Ätherleib und der Astralleib aus dem physischen Leib her­ausgehoben wird und nur der physische Leib daliegt."
      ],
      [
        "So also haben wir aus der Geisteswissenschaft heraus selbst ein so wunderbares Ereignis - wunderbar nur für denjenigen, der es nicht erklären kann -,ein so wunderbares Ereignis durchdrungen, wie das Lazarus-Wunder es ist.",
        "Alles das enthüllt sich Ihnen in demLazarus-Wunder,wenn Sie nur das Licht haben, das darauf fällt durch die Worte:"
      ],
      [
        "Seine Krankheit ist nicht zum Tode, sondern zur Enthül­lung des Inneren. - Wenn diese Fähigkeiten erweckt werden im Menschen, so ist das wie eine Geburt.",
        "Wie ein Kind aus dem Mutterschoß hervorgeht, so wird das Höhere aus dem"
      ],
      [
        "niederen Menschen geboren.",
        "So ist die Krankheit des Laza­rus verbunden mit der Geburt des neuen Lebens, des Gott-Menschen, so daß der göttliche Mensch in dem physischen Menschen, im Lazarus, geboren wird."
      ],
      [
        "So könnten wir Schritt für Schritt das Johannes-Evange­lium durchgehen und würden die Erfahrung machen, daß das, was in der geistigen Einweihung geschehen mußte, an­ders geschildert werden mußte.",
        "Wenn wir sehen, wie in alten Zeiten mit ganz anderen Geisteskräften der Gott Abrahams, Isaaks und Jakobs wirkt, und dann wieder hin-einblicken in die Bibel, dann wird sie uns das hohe Uni­versalbuch, das uns das entgegenleuchten läßt, was wir erst selbst gefunden haben.",
        "Indem wir zugeben müssen - wir können das sagen -, daß nur derjenige, der höhere geistige Kräfte ausgebildet hat, zu diesen Wahrheiten kommen kann, so mussen wir, wenn sie uns entgegentreten im Johan­nes-Evangelium, auch zugeben und sagen können, was sie in diese Schriften gebracht hat.",
        "Indem ein neuer Geistes-forscher an das Evangelium und an die ganze Bibel heran­trat, lernte er das sehen und kann sagen: Die Menschen wer­den wieder zu einem wahren Wert dieser Urkunde kommen und erkennen, daß nur ein materialistisches Vorurteil die Worte sprechen kann: «der schlichte Mann von Nazareth».",
        "Wir aber haben als Ergebnis der wahren Erkenntnis in dem Christus eine überwältigende Welt-Wesenheit erkannt, die in dem Leibe des Jesus von Nazareth gelebt hat."
      ],
      [
        "So erscheinen uns die drei ersten Evangelien im Verhält­nis zu dem Johannes-Evangelium etwa so, wie wenn drei Menschen gruppiert am Abhange eines Berges stehen und jeder aufzeichnet, was er sieht.",
        "Jeder sieht einen Ausschnitt.",
        "Derjenige, der von der höheren Warte heruntersieht, über-sieht mehr und schildert mehr von dieser höheren Warte aus.",
        "Wir erfahren nicht nur dasjenige, was die anderen"
      ],
      [
        "unten schildern, sondern auch dasjenige, was alle drei zu­gleich erklärlich machen kann.",
        "So ist es nicht schwer zu sagen, welcher es war, der auf der höheren Warte stand, sondern für uns ist es so, daß die drei ersten Schreiber auch in gewisser Beziehung Eingeweihte waren.",
        "Aber der tiefer Eingeweihte, derjenige, der viel tiefer, viel tiefer hineinsehen konnte als die drei anderen und über die wahren geistigen Tatbestände, die hinter dem Sinnlichen liegen, schreiben konnte, das ist der Schreiber des Johannes-Evan­geliums.",
        "So gliedern sich uns die Evangelien zusammen zu einer Harmonie, und das, was als Mysterium von Golgatha sich abgespielt hat und nicht begriffen werden kann als ge­wöhnliches geschichtliches Ereignis, sondern nur erklärlich wird durch einen Prozeß, wie wir ihn bei Paulus finden, der sagt: Nicht ich, sondern Christus lebt in mir."
      ],
      [
        "Was nebenher von der äußeren Forschung gezeigt wird, das wird uns in der Geistesforschung ebenso wichtig.",
        "Wenn wir auf das Christentum sehen, so wird es uns wichtig sein, das Hellsehertum des Moses zu durchschauen, das uns in dem Traumbild vom brennenden Dornbusch dargestellt wird.",
        "Das ist es, was darzulegen war.",
        "Das eine soll nur noch hervorgehoben werden: daß diese neue Geisteswissenschaft fähig sein wird, aus sich selbst heraus das Bild des Welten-geschehens zu bilden, den Christus sozusagen geistig von Angesicht zu Angesicht zu schauen und ihn daher auf wahr-hafte Art wiederzufinden in den Evangelien.",
        "Wahrhaft vor­aussetzungslos ist nicht jene Bibelforschung, die da sagt:"
      ],
      [
        "Wir wollen die Bibel erforschen wie eine andere Geschichte."
      ],
      [
        "- Denn sie setzt voraus das Dogma, daß es nur gewöhn­liche, sinnliche, natürliche Tatsachenzusammenhänge geben könne.",
        "Wahrhaft voraussetzungslos ist nur die Geistes­wissenschaft, und diese führt zu einer erneuerten Anerken­nung und Hochschätzung der Bibel in allen ihren Teilen."
      ],
      [
        "wird eine Zeit kommen, wo vielleicht diejenigen verstimmt sein werden, die heute sagen wollten, nur dem schlichten Verstande sei es gegeben, die Bibel zu erfassen.",
        "Diese Weis­heit muß die Bibel verkennen.",
        "Es wird die Zeit kommen, wo gerade die weiseste Weisheit am höchsten dasjenige schätzen wird, was uns in der Bibel gegeben wird, weil Sehertum sich dem Sehertum in der Bibel gegenüber er­blicken wird.",
        "Dann wird manches Wort, das im Neuen Testament geschrieben ist, in einem neuen Licht erscheinen.",
        "Es wird sich zeigen, daß ein Dokument wie die Bibel nichts verlieren kann durch unbefangene Forschung.",
        "Traurig stünde es, wenn irgendeine Forschung diese Bibel um ihr Ansehen, um ihren Namen bringen könnte.",
        "Eine Forschung, welche die Bibel um ihren Namen bringt, ist nur noch nicht weit genug gekommen.",
        "Die Forschung, welche bis an das Ende geht, wird die Bibel wieder in ihrer Größe darstellen."
      ],
      [
        "Frei darf der Mensch forschen.",
        "Wer die Ansicht hat, durch die Forschung könne die Religion zugrunde gehen, der zeigt damit nur, daß seine Religiosität auf schwachen Füßen steht.",
        "Die göttliche Wesenheit hat den Forschungs­trieb in des Menschen Wesen gelegt, damit er sich betätige.",
        "Eine Sünde gegen diesen Trieb wäre es, wenn man nicht forschend leben würde.",
        "Ich erkenne Gott durch die For­schung.",
        "Der Gott erkennt sich in meinem Forschen.",
        "Die Wahrheit ist ein Gut in der menschlichen Entwickelung, von der niemals das wahrhaft religiöse Leben etwas zu fürchten haben wird.",
        "Das aber ist eine Grundwahrheit, die das Neue Testament völlig durchzieht."
      ],
      [
        "Sie sollten nicht jene berücksichtigen, die aus Bequem­lichkeit die Menschen fernhalten wollen von der Bibel, und die sagen: Wenn ihr zu Philosophen kommt und die Bibel auslegt, so werden diese sagen, sie wollen nichts davon wis­sen. - Ein solches Forschen beruht aber auf Bequemlichkeit."
      ],
      [
        "Dasjenige Forschen dagegen ist berechtigt und richtig, das sagt: Wir können nicht tief genug gehen, um dasjenige zu verstehen, was in der Bibel steht. - Dasjenige Forschen in der Bibel ist das richtige, das in freier Forschung darauf eingeht und dann auch die Bibel im rechten Sinne erfassen wird.",
        "Diese Forscher begreifen die Wahrheit des Bibelwortes: Ihr werdet die Wahrheit erkennen, und die Wahr­heit wird euch frei machen."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "DER ABERGLAUBE VOM STANDPUNKTE DER GEISTESWISSENSCHAFT Berlin, 10. Dezember 1908",
    "paragraphs": [
      "DER ABERGLAUBE VOM STANDPUNKTE",
      "DER GEISTESWISSENSCHAFT",
      "Berlin, 10. Dezember 1908",
      "Vor einiger Zeit, als ich in einem kleinen Orte Deutsch-lands weilte, machte ich die Bekanntschaft eines Dichters, eines Dramatikers, und in der Zeit unserer Bekanntschaft war er eben damit beschäftigt, ein Drama fertigzuschreiben. An einem Nachmittag arbeitete er, wie ich bei einem Besuch, den ich zu machen hatte, bemerken konnte, geradezu wie mit Dampfkraft an der Fertigstellung seines Dramas. Man konnte gar nicht mit ihm sprechen, denn es handelte sich für ihn nur darum, die Sache so rasch wie möglich vorwärts-zubringen. Am Abend kurz vor acht Uhr machte ich einen Gang. Ich begegnete meinem guten Dramatiker, als er mit einer Riesengeschwindigkeit auf dem Zweirad dahinsauste; er sauste zur Post und war nicht aufzuhalten. Aber es inter­essierte mich doch - Sie werden gleich sehen warum -, war­um der Betreffende gerade an jenem Tage so außerordent­lich rasch zur Post sauste. Es war kurz vor acht Uhr, wo die Po&t geschlossen wurde. Als er zurückkam, sagte er mir auf meine Frage, warum er in solcher Eile gerade heute noch zur Post müsse, das hätte eine besondere Bewandtnis.",
      "Nun werden Sie diese Bewandtnis am besten dann ver­stehen, wenn ich vorausschicke, daß nach einer damals ge­rade beginnenden, dann aber rasch herrschend werdenden Mode der betreffende Dramatiker zu den freiesten Geistern der Gegenwart zählte und dasjenige, was er als seine Welt-anschauung bezeichnete, in den freiesten Phrasen zur Darstellung",
      "brachte. Ein ganz Fortgeschrittener war er. Durch folgenden Zusatz möchte ich zeigen, daß ich keine Indis­kretion begehe. Wenn er hier wäre, so wäre er ganz zufrie­den, zu hören, daß ich diese Sache hier erzähle. Jetzt werden wir uns ein Urteil über das bilden können, was er sagte, als er aus der Post herauskam: Ich bin deshalb so rasch zur Post gegangen, weil ich mein Drama heute zur Post bringen wollte. Heute ist der letzte Glückstag. Hätte ich bis morgen gewartet, so hätte ich mich der Gefahr ausgesetzt, daß die Theaterdirektion das Drama ablehnt. - Sind Sie eigentlich fertig geworden?, fragte ich, denn es schien mir unmöglich. Nein, sagte er, ich habe aber einen Brief geschrieben, damit man mir das Drama wieder zurückschickt, um die letzten Szenen wieder umzuarbeiten. So - das war der freie Geist!",
      "Ich mußte mich erinnern an eine Dame, die vor vielen Jahren an einem Kleide gearbeitet hatte und es am Don­nerstag fertig haben und anziehen wollte. Hätte sie es am Freitag zum ersten Male angezogen, so wäre es sicher zu ihrem Unglück ausgeschlagen. Man berücksichtigt gewöhn­lich nicht in dem Maße, wie es nötig wäre, was es für unser Fühlen und Denken in der Gegenwart heißt, wenn ein freier Geist eine Sendung macht, wie der zur Post sausende Dichter, um das Drama unfertig abzuschicken und dann wieder zurücksenden zu lassen, damit er es fertig machen könne. Sie sehen, daß das, was man als Aberglaube bezeich­net, im Grunde genommen etwas recht Merkwürdiges sein kann. Es kann etwas aus der Weltanschauung eines Men­schen, soweit er diese ausspricht, durchaus Verbanntes sein, und es kann sein, daß er sich in einer bramarbasierenden Weise stark dagegen verwahren wird, mit einem solchen Aberglauben etwas zu tun zu haben. Wenn es aber darauf ankommt, so gibt es Hintertüren, durch die sich dieser Aber-glaube recht sehr einschleichen kann.",
      "Wir leben in einer Zeit, in welcher im wegwerfendsten Sinne von allen möglichen Formen des Aberglaubens ge­sprochen wird. Zu gleicher Zeit geschieht es aber in dieser Gegenwart, daß diejenigen, die über den Aberglauben spre­chen, zuweilen gar keine Ahnung davon haben, durch wel­ches Hintertürchen sich der Aberglaube gerade bei ihnen einschleicht. Denn es braucht ja nicht eine alte Form des Aberglaubens zu sein, wie bei diesem auf dem Zweirad da­hinsausenden Dramatiker. Es können auch allerlei neue Formen des Aberglaubens auftreten. Und da wird vielleicht gerade derjenige, der in achselzuckendem Ton von den alten Formen des Aberglaubens spricht, am ärgsten mancher neuen Form des Aberglaubens ausgesetzt sein. Es ist vielleicht schwer, gerade über dieseBegriffe des Aberglaubens in unse­rer heutigen Zeit irgendwie ins klare zu kommen, denn es herrscht ja in unserer Zeit so sehr die Sucht, alles das, was man selber glaubt, für das einzig Vernünftige zu halten und abzustreiten alles dasjenige, was man selber nicht glaubt. So wird gerade diese Art und Weise des Fühlens in unserer Zeit den mancherlei neuen Formen des Aberglaubens Tür und Tor öffnen. Daher wird es wohl mit dem landläufigen Reden über den Aberglauben nicht weitergehen können, wenn wir uns gründlich auf dasjenige einlassen wollen, was vom geisteswissenschaftlichen Standpunkt aus Aberglaube genannt werden darf.",
      "Es sind mancherlei alte Traditionen in unsere Zeit hin­eingekommen, mancherlei, was unsere Vorfahren geglaubt haben, mancherlei, was bei unseren Vorfahren und bei den Gelehrten der Vorzeit als streng wissenschaftlich galt und was heute in die Region des Aberglaubens verwiesen ist. Wir fragen uns: Sollte denn denjenigen, die achselzuckend den alten Traditionen gegenüberstehen, die sich heute als wissenschaftlich vorgeschritten erscheinen, gar nicht ein",
      "wenig der Gedanke aufleuchten können, daß unter Um­ständen das, was heute geglaubt wird, irrig ist? Könnte es nicht sein, daß dieses einige Jahrhunderte später von unse-ren Nachkommen als der tollste Aberglaube angesehen wer­den kann? Gewiß, derjenige, der glaubt, auf dem festen Boden der Naturwissenschaft zu stehen, wird zum Beispiel leicht geneigt sein, alles dasjenige, was von einem Stand­punkte ausgesprochen wird, der eine geistige Welt neben der physisch wahrnehmbaren annimmt, überhaupt in das Gebiet des Aberglaubens zu werfen. Auf der anderen Seite wird man leicht begreifen können, daß vielleicht ebenso un­begründet - das soll nicht geleugnet werden - von theoso­phischer oder geisteswissenschaftlicher Seite der Aberglaube der Naturwissenschaft angefochten und charakterisiert wird. Daß die eine oder andere Partei dieses oder jenes als Aber­glaube bezeichnet oder empfindet, das kann niemals ein Charakteristikum werden für das eigentliche Wesen des Aberglaubens. Mancherlei, was heute hereinragt aus alten Zeiten, zeigt uns ja gerade, wenn es wirklich ein handgreif­licher Aberglaube ist, wie es bei solchen Dingen viel weniger auf die menschliche Logik, auf die menschliche Vernunft ankommt, als vielmehr auf die menschlichen Denkgewohn­heiten, auf dasjenige, was die Menschen zu denken gewohnt worden sind.",
      "Wie vieles geht heute durch unsere populäre Literatur, durch unsere Tagespresse, was scheinbar dem aufgeklärten Denken stracks zuwiderläuft! So gibt es zum Beispiel eine Stadt in Deutschland - sie ist nicht weit weg von Berlin -, wo Sie vergeblich nach einer Droschke Nummer 13 suchen würden. Der, welcher sie früher gehabt hat, bekam keinen Fahrgast mehr. Sie wurde weggelassen, die Nummer 13. Auch in Hotels können Sie oft die Erfahrung machen, daß die Nummer 13 fehlt in den Zimmernummern. Sie können",
      "auch finden in Badeanstalten, wo lauter aufgeklärte Arzte sind, daß bei den Badekabinen die Nummer 13 weggelassen ist, weil niemand hinein will. Und das mittendrin und neben der Denkweise der heutigen Literatur und Tagespresse. Wer aber ein klein wenig Seelenkenner ist, der wird schon fin­den, daß der Aberglaube doch etwas ist, was sich ganz leise in das Denken und Fühlen des Menschen einschleicht.",
      "So gibt es jetzt ein populäres Büchelchen über den Aber­glauben, in dem manches Vernünftige und manches Absurde steht. Aber dann, nachdem der Verfasser abschlachtet, was Astrologie und Astronomie und andere Formen des Aber­glaubens sind, führt er an, daß es in früherer Zeit Astro­logen gegeben haben soll, welche den Leuten Horoskope stellten und aus dem Momente der Geburt ihr Schicksal be­stimmt haben. Solche Astrologen gäbe es zwar seines Wis­sens nicht mehr; das verrichteten die Hebammen. In Berlin zwar nicht, aber im übrigen Deutschland käme es vor. -Das ist ein Satz, der tatsächlich in diesem Büchlein über Aberglaube steht. Ich glaube nicht, daß jemand es anders bezeichnen kann als einen anderen Aberglauben, denn sonst würde er sagen müssen, daß es heute sehr viele Astrologen gibt, die Horoskope stellen. Was der Mann sagt, entspricht durchaus nicht den Tatsachen; es ist also der purste Aber­glaube. Jede Untersuchung könnte ihm das Gegenteil seiner Behauptung zeigen. Ähnliche Sachen schleichen sich jeden Tag in das Bewußtsein der Menschen ein, wenn es auch weniger handgreifliche Dinge sind und man es als Para­doxon ansehen würde, wenn ich von Aberglaube spräche.",
      "Es ist seit einiger Zeit in gewissen Kreisen naturwissen­schaftlicher Betrachtung die Meinung aufgekommen, daß man für alles dasjenige, was auf seelisch-geistigem Gebiete im Menschen als Erinnerung auftritt, physische Ursachen und womöglich physische Ursachen eines ganz bestimmten",
      "Gebietes, des sexuellen Gebietes, zu suchen hat. Und nicht nur dieses, sondern zahlreich sind die Schriften und Bro­schüren, welche sich damit beschäftigen, die großen Geister auf ihren Geisteszustand zu prüfen.",
      "Ein Leipziger Gelehr­ter hat sich bis vor kurzer Zeit die besondere Mühe gegeben, eine ganze Reihe großer Geister, unter anderen Goethe, Schopenhauer, Scheffel, Conrad Ferdinand Meyer, darauf­hin zu prüfen, inwiefern sie eigentlich von dieser oder jener Geisteskrankheit befallen wären und ihr Genie zusammen­hinge mit dieser oder jener Geisteserkrankung. Auf der an­deren Seite wird die Neigung zur Vererbung mit physischer Erkranküng des Menschen zusammengebracht, und es ent­geht kaum ein Tagesereignis in unserer Zeit einer solchen Deutung.",
      "Hier haben wir es mit einem Aberglauben zu tun, der eben jetzt aufgeht, der aber als eine Landplage unsere Bildung durchsetzt. Künftige Zeiten werden nicht begreifen, wie es möglich war, daß dieWissenschaft eine Zeitlang einem solchenAberglauben huldigen konnte.",
      "Und wenn uns unsere Nachfahren in gleichem Sinne das vergeken werden, in glei­chem Sinne das beurteilen werden, was in früheren Zeiten von unseren Vorfahren geglaubt worden ist, dann werden die, welche auf diesem Gebiete tätig sind, in der schlimmsten Weise wegkommen. So sehen wir schon, indem wir unbe­fangen die Tatsachen überblicken, die alten Formen des Aberglaubens mit Recht zum Fenster hinausgeworfen und auf der anderen Seite neue Formen sich einschleichen, die eben einfach nicht als solche erkannt werden.",
      "Wer sich ein wenig in der Wissenschaft umtut, der weiß, wieviel Dämonen des Aberglaubens sich da und dort ein­schleichen, die zum Glück nur ein kurzes Dasein haben, aber deshalb nicht weniger schädlich sein können. Moderichtun­gen sind manchmal nicht weit von dem entfernt, was man Aberglaube nennen kann. Ich möchte dafür ein Beispiel anführen.",
      "Während meiner Erziehertätigkeit konnte ich manche Beobachtung machen, die nur dadurch möglich war, daß ich ein großes Feld in bezug auf die Menschenentwickelung be­ackern konnte. Es ist jetzt weit über zwanzig Jahre her, da war es üblich, kleinen Kindern - etwa im zweiten, dritten, vierten Jahre - Rotwein, überhaupt Wein zu trinken zu geben. Man konnte sehen, wie durch eine gewisse Mode-richtung der Medizin gerade Kinder in diesem Alter jedes­mal zu Tische ihr Glas Rotwein bekamen. Wer so etwas beobachtet, beobachtet vielleicht zu kurze Zeiträume in bezug auf die Wirkung dieser Dinge. Wenn man diejenigen Menschen, die heute zwanzigjährig sind, nachdem sie da­mals Kinder von zwei bis fünf Jahren waren, mit anderen vergleicht, die damals keinen Wein zur Stärkung bekom­men haben, so zeigt sich an der gegenwärtigen Nervenver­fassung - wie man sich etwa heute in materialistischer Weise ausdrückt - ganz genau der Unterschied zwischen denjeni­gen, welche Wein bekommen haben, und denen, die ihn nicht bekommen haben.",
      "Da gab es dazumal den Aberglauben, daß der Wein eine Stärke in sich enthalte. Das war ein Mode-Aberglaube. Man hat diese Meinung herumgeboten wie irgendeine andere abergläubische Meinung auch herumgeboten wird. Nun kön­nen wir von alledem absehen und auf manche andere Ge­biete übergehen, wo man gar nicht mehr von Aberglauben spricht, obwohl der seelische Tatbestand im Menschen ganz der gleiche ist. Wenn wir sprechen wollten davon, was die Leute im sozialen Leben, im politischen Leben für sonder­bare Götzen, für Fetische, für Schlagworte haben, denen sie nachlaufen, wie andere auf anderem Gebiete bestimmten Götzen nachlaufen, und welches Quantum von Aberglau­ben darin enthalten ist, dann würden Sie sehen: Wenn sich das Quantum Aberglaube auf dem einen Gebiete nicht auslebt,",
      "dann geht es über auf ein anderes Gebiet. Erhebt sich der Mensch also auf der einen Seite über den Aberglauben, flugs kommt er auf einem anderen Gebiete zum Ausdruck, auf dem man es nur nicht so sehr merkt.",
      "Nachdem wir so ein wenig die Situation charakterisiert haben, dürfen wir vielleicht einmal versuchen, auf den eigentlichen Quell des Aberglaubens, auf die eigentümliche Geistesverfassung zu kommen, in der ein Mensch ist, den wir als einen abergläubischen Menschen bezeichnen dürfen. Vor allen Dingen darf man sagen, daß bei der Entstehung dieser Geistesverfassung die Befangenheit eines Menschen in dieser oder jener Denkrichtung die denkbar größte Rolle spielt.",
      "Dieselbe Tatsache wird einer - je nachdem seine Denkrichtung so oder so ist - in der einen oder anderen Weise auffassen. Versuchen wir, uns einmal einen kon­kreten Fall vor das Auge zu rücken. Der jetzt viel genannte französische Physiologe Richet hatte folgendes Erlebnis: Er ging einmal auf der Straße, und auf der anderen Seite der Straße ging auch eine Person.",
      "In diesem Augenblicke hatte er den Gedanken: Es ist doch merkwürdig, daß Professor Lacassagne heute in Paris ist. Aber es ist doch nicht so merk­würdig. Vor vierzehn Tagen hat mir Professor Lacassagne einen Artikel geschickt und geschrieben, daß er in vierzehn Tagen hier sein würde.",
      "Schon wollte Richet auf die andere Seite gehen und ihn begrüßen, als er sich sagte, daß er ja in die Redaktion gehen wolle, und da würde der andere wohl auch hinkommen. In demselben Augenblicke geht ihm der Gedanke auf, wie ähnlich der Professor einem ihm bekann­ten Augenarzt sieht.",
      "Richet geht auf die Redaktion, und nach einer Stunde erscheint dort Professor Lacassagne. Richet sagt zu ihm: Ich habe Sie vor einer Stunde auf der Straße gesehen. - Der Professor antwortet: Das ist nicht mög­lich.",
      "Ich war vor einer Stunde nicht dort, sondern ganz woanders. -",
      "Es ist kein Zweifel, daß Richet ihn nicht gesehen haben konnte. Es ist eigentümlich, wie sich zwei Menschen oft zueinander verhalten, wenn sie zwei verschiedeneDenk­richtungen haben. Richet sah einen Menschen und hatte den bestimmten Eindruck, den Professor L. zu sehen. Als er aber den Professor L. vor sich sah, kam es ihm ganz töricht vor, einen anderen, der groß und blond war, für den Pro­fessor L. gehalten zu haben, während dieser mittelhoch ist und einen dunkeln Schnurrbart trägt. Richet ist nun aber ein Mensch, der an okkulte Wirkungen, an Gedankenüber­tragung glaubt. Er sagte sich, der Professor L. ist in Paris und hat gedacht, er wolle in die Redaktion gehen - und in diesem Momente sah ich diesen Gedanken durch Gedanken­übertragung!",
      "Ein anderer Forscher, der ein Buch über «Aberglaube und Zauberei» geschrieben hat, Lehmann, denkt anders darüber. Er sagt: «Richet glaubt an Gedankenübertragung; deshalb sieht er in diesem ganz gewöhnlichen Erlebnis etwas Mysti­sches, das die Richtigkeit seines Glaubens beweisen soll, übersieht aber dabei ganz die Nebenumstände, welche die Sache durchaus auf natürliche Weise erklären.»",
      "Da haben Sie zwei Menschen, die das gleiche Ereignis je nach der Denkrichtung in ganz verschiedener Weise be­urteilen. Ich selbst möchte dem dänischen Forscher Lehmann recht geben, denn die, welche an okkulte Dinge mit unzu­länglichen Mitteln herangehen, schießen am allerleichtesten über das Ziel hinaus und können sich, wie in diesem Falle, alles mögliche in der Welt damit erklären. Sie sehen aber daraus, wie die Befangenheit, in der sich ein Mensch in be­zug auf seine Ideenrichtung befindet, einen andern Men­schen, den er vor sich sieht, in einer solchen Weise färbt.",
      "Nun denken Sie, wie sich die Dinge, wenn sie nicht genau durchschaut werden, in der menschlichen Seele spiegeln. Da",
      "kommen wir zu dem, was in geisteswissenschaftlichem Sinne über das eigentliche Wesen des Aberglaubens gesagt werden muß. Sie können heute unzählige Schriften und Auseinan­dersetzungen lesen über den Aberglauben an die Alchemie, die unselige Kunst, Gold zu machen, der sich so viele hin­gegeben haben. Die, welche darüber schrieben, waren meist",
      "- der heutigen Auffassung nach - in anderer Beziehung außerordentlich tüchtige, positive Forscher. Sie nehmen in allen möglichen Schriften, in denen auf diese oder jene Weise da oder dort die Kunst, Gold zu machen, mitgeteilt wird, einen hervorragenden Platz ein. Aber was Sie da lesen, er-scheint Ihnen zumeist als der hellste Wahnsinn, als absolute­ster Unsinn. Und außerdem erscheint es ja in zahlreichen Fällen als ein so offenliegender Schwindel, daß sehr leicht zu sehen ist, wie eben damals, als die Menschen so etwas geglaubt haben, auf diesem Gebiete Irrtum über Irrtum verbreitet wurde. Trotzdem sich die Chemie aus der Alche­mie heraus entwickelt hat, müssen wir unendlich froh sein, daß wir endlich die wahre chemische Wissenschaft haben, im Gegensatz zu jenen Fabeleien und Irrtümern, denen sich unsere Vorfahren auf alchemistischem Gebiete hingegeben haben. Nun können wir vielleicht am leichtesten gerade das, was hier als eine Täuschung vorliegt, begreifen.",
      "Um zu zeigen, wie sich das Entsprechende abgespielt hat, werden wir einige einfache Fälle ins Auge fassen. Wir wol­len jetzt absehen von der Zahl Dreizehn, aber Sie wissen, daß für manche Leute die Zahl Sieben etwas Gräßliches hervorruft, daß sie von manchen als Glückszahl angesehen wird, manchmal aber auch als Unglückszahl, womit zauber­hafte Wirkungen zusammenhängen. Ich brauche nur etwas zu erwähnen, das Sie hinführen kann zu dem, was mit der Zahl Sieben zusammenhängt. Ich will nicht nur erwähnen, daß sich die Zahl Sieben auch in der rein physischen Natur",
      "findet - sieben Farben, sieben Töne und so weiter -, was hier schon oft erwähnt worden ist und woraus man schlie­ßen kann, daß mit der Zahl Sieben doch dieses oder jenes verbunden ist. Davon wollen wir aber heute absehen. Auf etwas anderes wollen wir aufmerksam machen.",
      "Es gibt eine Krankheit, die Lungenentzündung, die sieben Tage wächst und dann abnimmt. Erst am siebenten Tage tritt die Krisis ein, so daß derjenige, der einen solchen Kran­ken zu behandeln hat, besonders auf diesen physischen Rhythmus achtzugeben hat.",
      "Da haben wir also an die Zahl Sieben einen ganz bestimmten Vorgang geknüpft, etwas, was in jedem einzelnen Falle beobachtet werden kann. Nun läßt sich die heutige materialistische Wissenschaft durchaus nicht ein auf irgendeine Erklärung dieses Vorgangs.",
      "Würden wir die Medizin in die alten Zeiten zurück verfolgen, in denen Sie durchaus nicht bloß eine Summe von Irrtümern zu sehen haben, wie Sie es heute in der Geschichte der Medi­zin dargestellt finden, würde man sich klarwerden, daß die alten Ärzte und Naturkenner wußten, wie alles Leben in einem gewissen Rhythmus abläuft, daß ein Rhythmus be­steht zwischen dem, was im Menschen geschieht, und man­chem, was draußen in der großen Natur, im Makrokosmos, abläuft. Weil der Mensch eigentlich aus dem Makrokosmos herausgeboren ist und dessen Leben in gewissen äußeren Vorgängen verläuft, so verläuft auch des Menschen Leben in einem bestimmten Rhythmus.",
      "Wer den Rhythmus des menschlichen Lebens kennt, der weiß ganz gut, daß es in einem Organ wie der Lunge einen durch achtundzwanzig Tage, das heißt durch vier mal sieben Tage hindurch gehen­den auf- und abwogenden Rhythmus gibt, in dem gewisse funktionelle Stärken und Schwächen auftreten. Da ist es, sobald man diese Grundlage erkennt, nicht weiter verwun­derlich, daß die Erkrankung der Lunge gerade da besonders",
      "gefährlich wird, wo sie sozusagen zusammenstößt mit dem Rhythmus, um den es sich überhaupt bei den Lebenserschei­nungen handelt. Kurz, wir würden sehen, wenn wir im Sinne der Geistesforschung hineinleuchten würden, wie in tieferer Erkenntnis des Wesens des Menschen und nicht in irgendeiner abergläubischen Weise, sondern in einer Weise, die als streng gesetzmäßig zu bezeichnen ist, wir uns ver­ständlich machen können, warum nach sieben Tagen eine besondere Krisis für die Lungenentzündung reif ist. Aber man will ja in unserem materialistischen Zeitalter auf solche Dinge, die sich nur mit den Mitteln der Geisteswissenschaft verfolgen lassen, nicht eingehen.",
      "Es gab eine Zeit, in der die Ärzte nicht nur wußten, daß dieLungenentzündung am siebenten Tage diese Krisis durch-macht, sondern in der sie auch wußten, warum das so ist. Sie wußten, wie das auch mit dem gesunden Rhythmus zu­sammenhängt. Aber diese geisteswissenschaftliche Erkennt­nis ist für das äußere Leben vergessen. Die eigentliche Ge­setzmäßigkeit kennt man nicht mehr, sie ging der Menschheit verloren. Es blieb die trockene Zahl Sieben. Man wußte schließlich gar nicht mehr, warum es der Lungenentzündung einfällt, nach siebenTagen etwas ganzBesonderes zu zeigen. Und dann nimmt man natürlich solch eine Sache heraus, ohne sie weiter verstehen zu können oder zu wollen. Man wendet sie an, weil man in der Zahl selbst als solcher etwas Besonderes sieht. Man sagt sich, mit der Sieben hängt etwas Besonderes zusammen. Irgendwie kann man sie da oder dort anwenden. Solange man sich an Äußerlichkeiten hält, nicht hineinsieht in die Sache, solange hat man keinen Grund, die Sache da oder dort anzuwenden. Also wendet man sie da an, wo scheinbar eine Veranlassung da ist. Und vor allen Dingen spielt da ein menschliches Gesetz hinein, das nur zu verständlich ist: In allen Fällen, wo man eine",
      "solche Sache als Abstraktion herausgerichtet hat, wo man sie anwendet und es paßt, da geht die Geschichte; paßt es aber nicht, so übersieht man es.",
      "So geht es auch mit manchen Bauernregeln. Wer auf dem Lande aufgewachsen ist, der wird ganz genau wissen, wie aus dem ersten Gewitter, das im Frühling auftritt, das oder jenes prophezeit wird. Trifft das Prophezeite ein, so wird es als Gesetz hingenommen, trifft es nicht ein, so wird es vergessen. Aber trotzdem stecken in manchen Bauernregeln tiefe Weisheiten, und man müßte manche Bauernregel auf ihre tiefe Weisheit hin erforschen. Dann ist es auch wieder so, daß man nicht das rein Äußerliche des Aberglaubens an­wendet, sondern darauf ausgeht, wirklich in die Sache selbst einzudringen. Gewiß, mir hat es auch recht gut gefallen, wenn neben anderen Bauernregeln wieder einmal diese aus­gesprochen wird: Kräht der Hahn auf dem Mist, so ändert sich das Wetter, oder es bleibt, wie es ist. - Da zeigt sich ein gesunder Zug, der nicht generalisiert, sondern individuali­siert werden muß. Und das ist das Wesentliche, auf das es in unserer Geistes- und Seelenentwickelung ankommen soll.",
      "In ähnlicher Weise, nur nicht so durchschaubar, ist es mit vielen Dingen in bezug auf die Alchemie gegangen. Manche von Ihnen, die schon in vorhergehenden Jahren diese Vor­träge angehört haben, werden wissen, wie damals alles be­sprochen worden ist, wie über die Rosenkreuzer-Einweihung gesprochen und der Stein der Weisen erörtert worden ist, wie da gezeigt worden ist, wie unter dem Stein der Weisen in der wirklichen Geisteswissenschaft aller Zeiten etwas ver­standen wird, was vor unserem gegenwärtigen modernsten Denken, wenn man da hineindringt, durchaus bestehen kann. Unter den mancherlei Methoden, welche den Menschen zu den höheren Erkenntnissen heraufführen, namentlich zur Rosenkreuzer-Einweihung, da findet sich auch die eine, die",
      "man geradezu dieBereitung des «Steines derWeisen» nennt. Unter dieser Bereitung des Steins der Weisen wird etwas verstanden, das zusammenhängt mit einer Regelung des Atmungsprozesses. Zu den verschiedenen Methoden, durch die der Mensch sich hinaufarbeitet in die höheren Welten, gehört ein gewisses Bewußtwerden und ein nach geistigen Gesetzen geregeltesAtmen in bestimmten Zeiten. Nach ganz bestimmten Anweisungen atmet derjenige, der ein Jünger der Geisteswissenschaft im positiven Sinne wird.",
      "Dieses Atmen hat für den ganzen Organismus eine ganz bestimmte Folge, welche die äußere Wissenschaft nicht mehr suchen kann, weil sie nichts weiß von der Sache. Der Mensch entwickelt durch das Instrument seines eigenen Leibes in sich etwas ganz Bestimmtes, etwas, das wirklich in seinem Leben bis in den Leib hinein auftritt, das dann da ist und ihn befähigt zu einer ganz anderen Anschauung der Welt, weil durch die Atmung eine Wirkung geschieht, die sich selbst in der mineralischen Zusammensetzung des physischen Leibes ausdrückt. So haben wir durch die Regelung des Atmungsrhythmus in dem Menschen selber durch sein eige­nes Instrument etwas erzeugt, das genannt wurde der Stein der Weisen oder der weise Stein. Es ist das, was notwendig ist zu erzeugen in dem menschlichen Organismus, wenn der Mensch in die höheren Welten hineinwachsen soll. Der Pro­zeß ist genau angebbar, aber man kann ihn nicht ohne wei­teres jedem beliebigen Menschen mitteilen. Denn es kann der Natur der Sache nach nur derjenige diesen Prozeß an­wenden, der das in ganz selbstloser, durch gar keine per­sönliche Rücksicht gebundenen Weise tut.",
      "Als ich einmal in einem kleinen Kreise sprach, wie man es heute schon kann, wie ich es auch rückhaltlos in einem der Vorträge andeuten werde - nur das Letzte darf nicht angegeben werden, weil man da auf die geisteswissenschaftliche",
      "Schulung selbst hindeuten muß -, da sagte einer hin­terher : Das wäre aber doch ganz gut, wenn man diese Methode, ein besonderes Mineral im Menschen zu erzeugen, öffentlich bekanntmachte. Denn dieses Mineral ist etwas sehr Nützliches, wenn man es in großen Massen herstellen könnte. - Ich mußte antworten: Daß Sie diese Frage stellen, das gibt den Grund an, warum es nicht bekanntgemacht werden darf. Solange solche Fragen gestellt werden, ist es eben unmöglich, daß das bekanntgemacht werden darf. Sie können es in der Literatur finden, aber es ist dort ver­schleiert. Es ist nur verständlich für den, der durch die Vor­schule die Art der Ausdrucksweise kennenlernt. Quecksilber, Stein der Weisen, Silber, bedeutet nämlich etwas ganz an­deres. Und wenn man spricht von der Verbindung des Quecksilbers und seiner Hinzufügung zu irgendeinem an­deren Produkte, so bedeutet hier «Quecksilber» und «Stein der Weisen» eben etwas ganz anderes als das Hinstellen äußerer Dinge.",
      "Nun existieren diese Dinge aber in der Literatur. Die­jenigen, welche keine Ahnung davon haben, was in diesem Fall die Ausdrücke bedeuten und namentlich die Zeichen, die damit verbunden sind, die nehmen die Sache einfach wörtlich. Wörtlich genommen ist es aber der barste Unsinn. So zum Beispiel ist es einem dänischen Forscher über Aber­glauben passiert, daß er etwas las über merkwürdige Per­sönlichkeiten des dreizehnten und vierzehnten Jahrhun­derts, über Raimundus Lullus und andere. Es steht jedem frei, diesen für einen Schwindler, für einen Scharlatan oder für den größten Weisen seiner Zeit zu halten, je nachdem er ihn verstehen kann. Nun wird aber erzählt, daß es Rai­mundus Lullus gelungen sei, nach einem dreißigjährigen Studium - für die meisten Leute eine unbequeme Sache -den Stein der Weisen zu finden, und daß er dadurch in die",
      "Lage gekommen sei, Gold zu machen dadurch, daß er einem Teil des Steines eine bestimmte Menge Quecksilber hinzu-gesetzt habe. Wenn man eine kleine Menge davon nehme, dann bekomme sie die Eigenschaft, dasselbe zu erzeugen. Von dem werde dann wieder eine kleine Menge genommen, und so weiter, bis zuletzt das Gold entstehe.",
      "Wenn nun einer hingeht und das probiert, wenn er das nimmt, was er im Buche findet, gewisse Stoffe nimmt, sie mischt und sie dem Quecksilber hinzufügt, so ist das der absoluteste Unsinn, der gemacht werden kann. Es hat jeder das größte Recht, sich darüber lustig zu machen. Das tut auch der Forscher. Er macht sich lustig. Wer aber versteht, die Ausdrücke zu deuten, der wird finden, daß in der Lite­ratur der «Stein der Weisen» ebensogenau vorhanden ist wie in dem, was in Raimundus Lullus' Schriften enthalten ist, und wodurch er zum Ziele gekommen ist. Das ist das Wunderbare an der Sache, daß der Satz seit Jahrhunderten bekannt ist und heute noch richtig ist. Das zeigt dem, der etwas davon weiß, wie grandios richtig es ist. Für den ist es dann klar, daß in Raimundus Lullus wirklich die Seele eines der Weisesten seines Zeitalters steckte. Wer dagegen nur an der äußeren Ausdrucksweise haften bleibt, der macht wirklich Unsinn.",
      "Diesen Unsinn machten auch sehr viele, die geglaubt haben, daß der weise Alchimist äußeres Gold nachgemacht hat, und sie haben auch den Verstand verloren, obgleich ich glaube, daß ein wenig davon schon verloren war, als sie die Geschichte angefangen haben. Psychiater aber behaupten, daß sie dadurch um den Verstand gekommen sind. Um ihr Vermögen können sie gekommen sein, denn Gold haben sie zuletzt nicht gefunden. Daher darf man dem Schreiber, welcher die Alchimie als Unsinn bezeichnet, gar nicht so unrecht geben, denn - was er davon verstehen konnte, ist",
      "eben nur Unsinn. Tatsächlich ist aber kein Unsinn groß genug, um nicht von diesem oder jenem Menschen geglaubt zu werden.",
      "Das hängt mit einer Sucht zusammen, die Sie auf dem Gebiete der Geisteswissenschaft Tag für Tag erleben kön­nen. Sie erleben leicht folgendes: Wenn Sie diesem oder jenem gegenübertreten mit einer Naturerscheinung, die einer Aufklärung bedarf, und versuchen, eine solche Erscheinung im Zusammenhang mit ihren geistigen Untergründen zu erklären und darauf Anspruch machen, eine alltägliche Er­scheinung auf ihre geistige Unterlage zurückzuführen, dann werden Sie bei den meisten Menschen unserer Gegenwart kein besonderes Interesse erregen. Viele Menschen unserer Gegenwart suchen nicht das Erklärliche, sondern das Un­erklärliche. Sie sind froh, wenn sie etwas finden können, was ihnen unerklärlich bleibt. Erzählen Sie einem, daß sich da oder dort etwas zugetragen hat, wofür kein Mensch eine Erklärung weiß, dann sind sie zufrieden. Die Menschen wollen also geradezu hingewiesen werden auf das Uner­klärliche. Sie wollen nicht das, was sich ihnen bietet, durch­dringen, sondern das Wunderbare vermehren. Versuchen Sie, einem Menschen etwas über die Entwickelung der Pflan­zen zu erklären, indem er sie aus den Untergründen der Entwickelung erfassen und tief in die Natur hineinschauen kann, dann von dem Sinnlichen, wo man den Geist an einem Ende anfaßt, tief hineingeführt wird in das Geistige",
      "- dann kann er nicht an eine geistige Welt glauben! Erzäh­len Sie aber einem solchen Menschen, daß eine Hand von einer Statue abhanden gekommen ist, in einer anderen Stadt gefunden wurde und wieder eingesetzt worden ist, da sagen sie: Das kann kein Mensch erklären, folglich glaube ich an eine geistige Welt. - Das ist so, daß die Menschen dem Geiste gegenüber verständnislos bleiben wollen, weil sie",
      "glauben, daß man das nicht ergründen darf. Damit eröffnen sie dem Aberglauben aber Tür und Tor an allen Ecken und Enden.",
      "Wenn der Mensch nicht nach Unbefangenheit strebt mit dem, was ihm in seiner Vernunft und in seinem logischen Denken zur Verfügung steht, so ist er in dem Augenblicke, wo er sich auf dieses nicht verlassen will, sobald etwas auf­tritt, was anders ist als gewohnt, schon allen möglichen For­men des Aberglaubens ausgeliefert. So könnte man zum Beispiel sehen - verzeihen Sie, wenn ich dies sage, obwohl ich voll auf dem Boden der Geisteswissenschaft und Theo-sophie stehe -,wie gerade diejenigen, welche auf dem Boden der Theosophie stehen, ablehnen, was im geisteswissenschaft­lichen Sinne zu einer Aufklärung hinführen könnte.",
      "Als die theosophische Aufklärung in der Welt begonnen hatte, da waren es zwei bedeutsame Menschheitsindividualitäten, von denen diese Weisheit der Menschheit zunächst geoffenbart worden ist. Diejenigen, welche diese Weisheit bekommen haben, haben sich in der Regel nicht so verhalten, wie es hier unzählige Male charakterisiert worden ist.",
      "Denn wie hätte man sich verhalten können gegenüber einer Wahrheit, die von einer unbekannten Seite her erhalten worden ist? Es haben die ersten Vermittler der theosophischen Welt­anschauung gesagt : Von Persönlichkeiten, die sich im Hin­tergrunde halten, haben wir die Weisheit, die wir diesem oder jenem Buche anvertrauten. - Da hätte es sich um folgendes handeln können.",
      "Man hätte sagen können: Nun ja, es sind ja ehrenwerte Leute, die diese Weisheit bringen, aber wir wollen diese Weisheit selber prüfen. - Immer wird betont, daß in den höheren Welten forschen kann nur der­jenige, der sich besondere Fähigkeiten erworben hat. Wenn sie aber mitgeteilt ist, die Weisheit, so daß sie prüfbar ist, wie ist es dann?",
      "Die Prüfung der Weisheit ist in vielen Fällen",
      "nicht eingetreten. Die einen haben auf Treu und Glau­ben, weil ihnen gesagt worden ist, daß sie von höheren Individualitäten gekommen sei, die Sache hingenommen. Die anderen aber sagen: Ob sie begründet ist oder nicht be­gründet ist, das ist nicht von Bedeutung. Ob die höheren Individualitäten überhaupt vorhanden sind,darauf kommt es an. - Da sind sie aber irre geworden. Sie sagen: Wenn man nicht sicher weiß, ob es diese höheren Individualitäten gibt oder nicht gibt, dann lehnen wir die ganze Theosophie ab.",
      "Nun, hätte es denn aber niemals einen geben können, der sich sagte: Mag zunächst diese Weisheit wo auch immer her­gekommen sein. Jch prüfe sie, ob und wie sie zu den Er­scheinungen des Lebens paßt, ob sie sich bewahrheitet im Leben. Ich prüfe sie vor allem daraufhin, wie sie sich ver­hält zu dem, was uns die landläufige Weltarischauung, die auf der positiven Wissenschaft aufgebaut ist, gibt. Wie arm­selig ist das, was uns die positive Weltanschauung gibt gegenüber dem, was von dieser Seite gekonumen ist; aber einsehen kann man es. Da geht also beim prüfen hervor:",
      "Diejenigen, von denen diese Weisheit gekommen ist, sind unbedingt größer als diejenigen, welche auf den sogenann­ten wissenschaftlichen Tatsachen stehen. Und da alles relativ ist, so haben wir keinen Grund, anzunehnten, daß Frau H.P. Blavatsky ihre Weltanschauung aus dem Wolken-regen erhalten hat. Nachdem sie als vernünftig befunden ist, so muß sie von irgendwoher stammen. Es ist das Ver­nünftigste, anzunehmen, daß sie von Menschen stammt. Ob man sie groß nennen muß, das hängt davon ab, was sich ergibt, wenn man diese Weltanschauung mit derjenigen ver­gleicht, die man schon als groß anerkennt. - Das wäre ver­nünftig gewesen. Das ist aber das einzige, was tatsächlich dem menschlichen Geist Ehre macht, nicht das Hinnehmen",
      "auf Treu und Glauben, aber auch nicht das Ablehnen auf Treu und Glauben, sondern das vorurteilslose Prüfen. Gewiß, forschen kann nicht ein jeder. Zum Forschen sind diejeni­gen da, die ihre Geisteskraft in besonderer Weise entwickeln können. Aber unbefangen prüfen kann ein jeder. Wenn er nur nicht so das Unerklärliche statt des Erklärlichen suchte und im Geiste zufrieden wäre, wenn er das Unerklärliche gefunden hat. Solange man zu ihm spricht, er soll sich an­strengen, um den Geist zu ergründen, da will er nicht mit. Wenn man ihm aber etwas mitteilt, das gar nicht zu begrei­fen ist, da ist er dabei, weil es so bequemer ist. Das ist be­sonders charakteristisch für das, was als Seelenzustand für die Menschen existiert.",
      "Da ist ein anderer Fall, der sich abgespielt hat. Ich rede wiederum nicht so, als ob Wahres dahintersteckt, sondern ich rede von der menschlichen Seelenverfassung, die dabei zutage getreten ist. Da wurde erzählt, daß es in gewissen Gegenden Asiens Menschen gebe, welche das Folgende machen können: Sie breiten ein Tuch aus, nehmen ein Seil, werfen das Seil in die Luft, lassen ein kleines Kind daran hinaufklettern, bis es oben unsichtbar wird; sie klettern dann selber nach, und nach einiger Zeit fallen die Glieder des Kindes zerstückelt herunter. Dann kommt der Fakir auch nach, nimmt einen Sack, packt die Glieder hinein, schüttelt das Ganze, schüttelt dann den Sack aus und - das Kind ist wieder vollständig hergestellt. Ich will nicht ent­scheiden, was dahintersteckt, sondern nur über die Art und Weise des Aberglaubens der Menschen sprechen. Der Vor­gang erscheint den Menschen zunächst als etwas, was schwer zu glauben ist. Es gibt aber merkwürdige Abbildungen, die den ganzen Vorgang so darstellen, wie ein Maler ihn ab­bilden würde, der dabei gewesen wäre. Er zeichnete also richtig die verschiedenen Stadien: das hinaufgeworfene Seil,",
      "das emporkletternde Kind und so weiter. Ein weiterer Be­obachter hat die Sache ganz besonders schlau angelegt, denn er gab auch Photographien dazu. Auf diesen Photographien sah man aber immer nur die betreffenden Zuschauer, die auf und ab gingen und die Gesichter nach dem Fakir rich­teten.",
      "Aber das übrige sah man nicht. Ein gewisser S.Ellmore hat eine Erklärung gegeben, so daß die ganze Sache sich leicht aufklären ließ. Er meinte nämlich, der Betreffende, der die Sache ausführte, müsse ein ganz bedeutender Hypno­tiseur sein, der auf Suggestion so eingestellt war, daß er einer ganzen Gesellschaft den betreffenden Vorgang sugge­rieren konnte.",
      "Da sagten sich die Menschen, daß der Vor­gang kein Aberglaube, sondern Suggestion war, und es schien erklärlich, daß alle Leute hypnotisiert waren. Einer Person aber kam dieser suggestive Vorgang noch unwahr­scheinlicher vor als der ursprüngliche Vorgang.",
      "Sie dachte nämlich, es könnte doch in der Welt auch Dinge geben, die mit unseren Gesetzen nicht erklärt werden können, und sagte sich: In bezug auf die Suggestion weiß man schon mehreres, aber in bezug auf die Seelenstärke muß man doch noch manches erforschen. - Da wandte diese Person sich an die Stelle, wo man darüber etwas erfahren konnte, an S. Ellmore.",
      "Dieser erklärte die ganze Geschichte für er­dichtet, worauf schon sein Pseudonym hinweise. Dieses soll nämlich ein Hinweis auf die Frage sein: Kann einer noch mehr betrügen? Diese Person hat also die Sache in eine neue Form gekleidet, da sie den Vorgang in der ursprünglichen Form nicht glauben konnte, aber in der neuen Form für das moderne Bewußtsein annehmbar fand.",
      "Sie sehen also, daß es tatsächlich auf die geistige Verfas­sung ankommt, daß es ankommt auf das, was in unserer Seele selber vorgeht, wenn man sich über den Begriff und über das Wesen des Aberglaubens einigermaßen aufklären",
      "will. Ob eine Sache richtig oder nicht richtig ist, darüber müssen schließlich ganz andere Faktoren entscheiden. Aber was uns alle behüten kann vor irgendwelchen Verirrungen, die zum Aberglauben werden, das kann einzig und allein das Streben nach einer wirklichen Erkenntnis sein, nach einem Durchschauen der Dinge. Derjenige wird immer auf irgendeinem Felde dem Aberglauben verfallen, der nicht wirklich in die Tiefe der Dinge eindringen will. Es ist nun einmal so, daß diese Umlagerung des Quantums Aberglau­ben durchaus herrscht. Und damit spreche ich das Grund­gesetz für den Aberglauben aus, wie ich es vorhin schon angedeutet habe, nämlich: Solange der Mensch in der Be­obachtung der physischen Umwelt bleibt, solange er nicht vordringen will zur Geisteswissenschaft, zur wirklichen Er­kenntnis der geistigen Urgründe der Dinge, solange lebt in ihm ein gewisser Bedarf an Aberglaube.",
      "Nehmen Sie meinetwillen einen heutigen Mediziner:",
      "Wenn er überhaupt denkt, wenn er noch so sehr abweist alle Formen des Aberglaubens - derjenige, der unbefangen ist, kann leicht nachweisen, wie er seinen Bedarf an Aber­glauben in anderer Form reichlich deckt. Das ist das Gesetz der Kompensation in den menschlichen Seelen. Daran sehen Sie, wie charakteristisch das Gesetz ist.",
      "Sie haben einen Menschen, der ganz gewiß in jeder Be­ziehung hinaussein will über den uralten Aberglauben, aber wieviel Aberglaube verzeichnet Haed:el in seinen «Lebens-wundern und Welträtseln»! Diejenigen, die mich kennen, wissen, daß ich Haeckel in allem anerkenne, weil er der große Forscher ist. Wer mich kennt, der weiß auch, daß ich immer auf das Positive hinweise, das Haeckel geleistet hat. Weil er aber den alten Aberglauben hinausgeworfen hat und nicht zurückgehen will auf die geistigen Hintergründe der Dinge, da wendet er sich auf ein anderes Gebiet. Da",
      "wird er der abergläubischste Mensch auf dem anderen Ge­biet. Auf dem Gebiete von Kraft und Stoff, wie er es sich vorstellt, da tanzen und wirbeln die Atome. Das nennt er seinen Gott. Dem Tanzen und Wirbeln der Atome schreibt er zu, daß sie Zustände schaffen können, die einfache Lebe­wesen darstellen, und daß diese wieder sich zusammenset­zen zu komplizierteren, die sich schließlich zusammenfügen zur menschlichen Gehirnform.",
      "Alles, was der Mensch dann fühlen und wollen kann, alles Ideale und Sittliche, ja alle Religionen selber sind für denjenigen, der die Sache unbe­fangen beurteilen kann, dann nur Tanz der Atome. Für ihn besteht kein Unterschied zwischen dem Atomtanz und den großen Fetischen der afrikanischen Wilden.",
      "Ob der afrika­nische Wilde seinen Holzklotz anbetet und ihn als Gott ansieht, oder ob Haeckel seine kleinen Atome tanzen läßt und sie als kleine Götter ansieht - in bezug auf den Aber­glauben ist zwischen beiden kein Unterschied. Auf dem­selben Standpunkte steht der eine wie der andere Aber­glaube.",
      "Es gab eine Zeit - sie liegt in gewisser Weise schon hinter uns -, da konnte man sehen, wie dieser Aberglaube nach und nach heraufkam. Es wurden im Laufe der Zeit neue Entdeckungen der Naturwissenschaft gemacht, nament­lich in der Chemie.",
      "Es wurden neue Verbindungen dadurch erklärbar, daß man Gewichtsunterschiede kleinster Teile im Raume festhielt. Es wurde durch das Gesetz der Atom-gewichte manches erklärt. Da erschien es als fruchtbare An­schauung, eine solche Atom-Theorie zu konstruieren.",
      "Später vergaß man, daß man diese Atom-Theorie im Geiste kon­struiert hat. Die Atome wurden zu wirklichen Götzen, die man anbetete.",
      "Als Schüler schon wurde ich von einem Schuldirektor für den Atom-Aberglauben klar sehend gemacht. Ein Schul-direktor hat dazumal - es ist lange her -, als die neuen",
      "Atom-Theorien heraufgekommen sind, alle Erscheinungen der Physik und der Chemie als Bewegungen berechnet. Er hat allerdings das Denken noch nicht berechnet. Aber bis in die chemischen Erscheinungen hinein hat er Berechnungen angestellt. Das Büchelchen, das diese Dinge enthielt, heißt:",
      "«Die allgemeine Bewegung der Materie als Grundursache aller Naturerscheinungen.» Das war etwas, was denjenigen faszinieren konnte, der auf diese Sache eingeht. Ich würde gerade dieses Büchelchen einem jeden gern in die Hand geben. Es ist aber seit langer Zeit nicht mehr im Buchhandel zu haben. In Bibliotheken dürfte es vielleicht noch zu finden sein. Da sehen wir den Aberglauben in der Allmacht des Atomwirbels auftauchen.",
      "Nun haben wir der Reihe nach alle möglichen Formen des Aberglaubens in der Naturwissenschaft auftreten sehen. Denken Sie einmal, daß wir tatsächlich eine gewisse Rich­tung haben in der Naturwissenschaft, die von der Allmacht der Naturzüchtung spricht. Überall können Sie sehen, daß alles zusammengetragen wird, was für das eine oder andere spricht. Wenn einmal der betreffende Forscher fasziniert ist von dem betreffenden Schlagwort, das wie ein Götze auf ihn wirkt, so sehen wir gerade in unserer Zeit, wenn wir nur ein Auge dafür haben wollten, ähnliche Fälle. Schon am Eingang des Vortrages erwähnte ich, wie sich heran­schleichen die Dinge, die sich in nicht allzuferner Zeit als furchtbarer Zeit-Aberglaube enthüllen werden.",
      "Wo ist nun die Ursache des Aberglaubens selber? Immer tritt die Möglichkeit ein, daß der Aberglaube an die Stelle dessen tritt, was allein als fruchtbarer Gedanke, als frucht­bare Meinung herrschen kann. Wenn der ursprüngliche Ge­danke, die ursprüngliche Meinung vergessen wird und dafür nur die sich bietende Äußerlichkeit genommen wird, dann vergessen wir, wie bei der sieben Tage langen Krisis, das",
      "Wesentliche. Wenn die Siebenzahl herausgerissen und fest­gehalten wird, so besteht die Möglichkeit, daß dies in Aber­glauben umschlägt. Da haben Sie den Grund dafür, daß ake Weise große Naturerscheinungen zeigen konnten.",
      "Das ist es, was die Geisteswissenschaft dem Menschen bringen wird : daß er nicht das Unerklärliche suchen wird, sondern daß er die Erklärung wird suchen wollen. Sonst, wenn er stehenbleibt im Gebiete der Umwelt und sich nicht erheben will auf den höheren Standpunkt, von dem aus er sehen kann, was auf dem einen oder anderen Gebiete be­rechtigt oder unberechtigt ist, dann wird er sich nur in der Umlagerung des Aberglaubens befinden. Wer in der physi­schen Welt stehenbleibt, der verläßt den einen Aberglauben und geht in den anderen ein. Erst wenn er sich erhebt über sich selbst und über den Aberglauben, sieht er das Rechte sowohl in dem einen wie in dem anderen. Jean Jacques Rousseau hat schon festgestellt, daß es keinen Unterschied macht, ob man mehr oder weniger klug ist. Er sagte: Die Gescheiten und die Klugen haben ihre Vorurteile ebenso wie die Dummen, wenn auch die Klugen und Gescheiten manches mehr wissen und mehr Vorurteile haben als die Dummen. Die Dummen halten dafür an dem wenigen um so zäher fest. - Das ist durchaus ein Gesetz, das derjenige, der das Menschenleben beobachtet, in zahlreichen Fällen bestätigt finden kann. So sehen wir, daß es im Grunde ge­nommen eine Heilung gegenüber dem Aberglauben gar nicht anders geben kann als durch das Erheben zu dem höheren Standpunkt, von dem aus die Welt in ihren geisti­gen Untergründen überschaubar wird.",
      "Es wird noch mancherlei Aberglaube heraufziehen, und manches schleicht sich heute in unsere Anschauung ein. Wir sind ja auf einer Bahn der Entwickelung, wo die Menschen eigentlich gar keinen rechten Sinn dafür haben, aus dem",
      "öffentlichen Leben den Aberglauben, wenn er nicht gerade aus alten Zeiten sich übertragen hat, herauszubringen. Oh, es gilt durchaus für unsere Zeit auf mancherlei Gebieten dasjenige, was uns eine alte Erzählung sagt. Nennen Sie es eine Anekdote, aber sie gilt, und sie stellt die Wahrheit bes­ser dar als manches andere. In einer gewissen Gegend Spa­niens, an der Grenze zwischen zwei Provinzen, war einmal eine Epidemie ausgebrochen. Es war in der Nähe von zwei Universitäten. Die eine Universität hatte eine medizinische Fakultät, in der man besonders schwärmte für das Ader-lassen. In der anderen Universität schwärmte man gegen das Aderlassen. Und nun waren in der unglücklichen Gegend, wo die Epidemie ausbrach, zwei Ärzte. Der eine war in der einen, der andere in der anderen Universität ausgebildet. Der eine verordnete Mittel, und der andere ließ zur Ader. Es stellte sich heraus, daß der eine Arzt alle Patienten er­hielt, denn die Patienten des anderen Arztes starben alle. Der eine schiebt den anderen zurück. Wenn dem einen auch alle leben und dem anderen auch alle sterben, so verfahren sie doch beide richtig: der eine zwar falsch in der Praxis, aber richtig nach der Theorie.",
      "Wenn man eine solche Sache erzählt, so kann sie einem albern erscheinen. Wenn man sie aber Tag für Tag sieht, dann findet man, daß sie nichts Falsches sagt, und man findet sie sogar notwendig. Deshalb kann es sich, wenn über den Aberglauben gesprochen wird, nur darum handeln, daß die Geisteswissenschaft wahrhaftig am allerwenigsten einen Grund hat, diesen oder jenen Aberglauben zu propagieren. Sie steht auf dem Boden, daß das Geistesleben erforschbar ist und daß es Mittel und Wege gibt, um hineinzudringen in die geistige Welt, durch die man von einem höheren Ge­sichtspunkte aus die Welt zu überschauen vermag. Dadurch wird der Mensch hinausgeführt über das, was Aberglaube",
      "ist, und auch hinausgeführt über das, was Aberglaube im menschlichen Leben als Schaden anrichten kann. Man kann dasjenige, was hier gilt, mit einem Goetheschen Wort aus­drücken, das in umfassender Weise, wenn auch einfach, die Wahrheit enthüllt: «Die Weisheit ist ewig, und sie wird siegen, und sie wird in uns allen in den mannigfaltigsten Tumulten den Menschen zur Menschheit erhöhen.»"
    ],
    "sentences": [
      [
        "DER ABERGLAUBE VOM STANDPUNKTE"
      ],
      [
        "DER GEISTESWISSENSCHAFT"
      ],
      [
        "Berlin, 10.",
        "Dezember 1908"
      ],
      [
        "Vor einiger Zeit, als ich in einem kleinen Orte Deutsch-lands weilte, machte ich die Bekanntschaft eines Dichters, eines Dramatikers, und in der Zeit unserer Bekanntschaft war er eben damit beschäftigt, ein Drama fertigzuschreiben.",
        "An einem Nachmittag arbeitete er, wie ich bei einem Besuch, den ich zu machen hatte, bemerken konnte, geradezu wie mit Dampfkraft an der Fertigstellung seines Dramas.",
        "Man konnte gar nicht mit ihm sprechen, denn es handelte sich für ihn nur darum, die Sache so rasch wie möglich vorwärts-zubringen.",
        "Am Abend kurz vor acht Uhr machte ich einen Gang.",
        "Ich begegnete meinem guten Dramatiker, als er mit einer Riesengeschwindigkeit auf dem Zweirad dahinsauste; er sauste zur Post und war nicht aufzuhalten.",
        "Aber es inter­essierte mich doch - Sie werden gleich sehen warum -, war­um der Betreffende gerade an jenem Tage so außerordent­lich rasch zur Post sauste.",
        "Es war kurz vor acht Uhr, wo die Po&t geschlossen wurde.",
        "Als er zurückkam, sagte er mir auf meine Frage, warum er in solcher Eile gerade heute noch zur Post müsse, das hätte eine besondere Bewandtnis."
      ],
      [
        "Nun werden Sie diese Bewandtnis am besten dann ver­stehen, wenn ich vorausschicke, daß nach einer damals ge­rade beginnenden, dann aber rasch herrschend werdenden Mode der betreffende Dramatiker zu den freiesten Geistern der Gegenwart zählte und dasjenige, was er als seine Welt-anschauung bezeichnete, in den freiesten Phrasen zur Darstellung"
      ],
      [
        "brachte.",
        "Ein ganz Fortgeschrittener war er.",
        "Durch folgenden Zusatz möchte ich zeigen, daß ich keine Indis­kretion begehe.",
        "Wenn er hier wäre, so wäre er ganz zufrie­den, zu hören, daß ich diese Sache hier erzähle.",
        "Jetzt werden wir uns ein Urteil über das bilden können, was er sagte, als er aus der Post herauskam: Ich bin deshalb so rasch zur Post gegangen, weil ich mein Drama heute zur Post bringen wollte.",
        "Heute ist der letzte Glückstag.",
        "Hätte ich bis morgen gewartet, so hätte ich mich der Gefahr ausgesetzt, daß die Theaterdirektion das Drama ablehnt. - Sind Sie eigentlich fertig geworden?, fragte ich, denn es schien mir unmöglich.",
        "Nein, sagte er, ich habe aber einen Brief geschrieben, damit man mir das Drama wieder zurückschickt, um die letzten Szenen wieder umzuarbeiten.",
        "So - das war der freie Geist!"
      ],
      [
        "Ich mußte mich erinnern an eine Dame, die vor vielen Jahren an einem Kleide gearbeitet hatte und es am Don­nerstag fertig haben und anziehen wollte.",
        "Hätte sie es am Freitag zum ersten Male angezogen, so wäre es sicher zu ihrem Unglück ausgeschlagen.",
        "Man berücksichtigt gewöhn­lich nicht in dem Maße, wie es nötig wäre, was es für unser Fühlen und Denken in der Gegenwart heißt, wenn ein freier Geist eine Sendung macht, wie der zur Post sausende Dichter, um das Drama unfertig abzuschicken und dann wieder zurücksenden zu lassen, damit er es fertig machen könne.",
        "Sie sehen, daß das, was man als Aberglaube bezeich­net, im Grunde genommen etwas recht Merkwürdiges sein kann.",
        "Es kann etwas aus der Weltanschauung eines Men­schen, soweit er diese ausspricht, durchaus Verbanntes sein, und es kann sein, daß er sich in einer bramarbasierenden Weise stark dagegen verwahren wird, mit einem solchen Aberglauben etwas zu tun zu haben.",
        "Wenn es aber darauf ankommt, so gibt es Hintertüren, durch die sich dieser Aber-glaube recht sehr einschleichen kann."
      ],
      [
        "Wir leben in einer Zeit, in welcher im wegwerfendsten Sinne von allen möglichen Formen des Aberglaubens ge­sprochen wird.",
        "Zu gleicher Zeit geschieht es aber in dieser Gegenwart, daß diejenigen, die über den Aberglauben spre­chen, zuweilen gar keine Ahnung davon haben, durch wel­ches Hintertürchen sich der Aberglaube gerade bei ihnen einschleicht.",
        "Denn es braucht ja nicht eine alte Form des Aberglaubens zu sein, wie bei diesem auf dem Zweirad da­hinsausenden Dramatiker.",
        "Es können auch allerlei neue Formen des Aberglaubens auftreten.",
        "Und da wird vielleicht gerade derjenige, der in achselzuckendem Ton von den alten Formen des Aberglaubens spricht, am ärgsten mancher neuen Form des Aberglaubens ausgesetzt sein.",
        "Es ist vielleicht schwer, gerade über dieseBegriffe des Aberglaubens in unse­rer heutigen Zeit irgendwie ins klare zu kommen, denn es herrscht ja in unserer Zeit so sehr die Sucht, alles das, was man selber glaubt, für das einzig Vernünftige zu halten und abzustreiten alles dasjenige, was man selber nicht glaubt.",
        "So wird gerade diese Art und Weise des Fühlens in unserer Zeit den mancherlei neuen Formen des Aberglaubens Tür und Tor öffnen.",
        "Daher wird es wohl mit dem landläufigen Reden über den Aberglauben nicht weitergehen können, wenn wir uns gründlich auf dasjenige einlassen wollen, was vom geisteswissenschaftlichen Standpunkt aus Aberglaube genannt werden darf."
      ],
      [
        "Es sind mancherlei alte Traditionen in unsere Zeit hin­eingekommen, mancherlei, was unsere Vorfahren geglaubt haben, mancherlei, was bei unseren Vorfahren und bei den Gelehrten der Vorzeit als streng wissenschaftlich galt und was heute in die Region des Aberglaubens verwiesen ist.",
        "Wir fragen uns: Sollte denn denjenigen, die achselzuckend den alten Traditionen gegenüberstehen, die sich heute als wissenschaftlich vorgeschritten erscheinen, gar nicht ein"
      ],
      [
        "wenig der Gedanke aufleuchten können, daß unter Um­ständen das, was heute geglaubt wird, irrig ist?",
        "Könnte es nicht sein, daß dieses einige Jahrhunderte später von unse-ren Nachkommen als der tollste Aberglaube angesehen wer­den kann?",
        "Gewiß, derjenige, der glaubt, auf dem festen Boden der Naturwissenschaft zu stehen, wird zum Beispiel leicht geneigt sein, alles dasjenige, was von einem Stand­punkte ausgesprochen wird, der eine geistige Welt neben der physisch wahrnehmbaren annimmt, überhaupt in das Gebiet des Aberglaubens zu werfen.",
        "Auf der anderen Seite wird man leicht begreifen können, daß vielleicht ebenso un­begründet - das soll nicht geleugnet werden - von theoso­phischer oder geisteswissenschaftlicher Seite der Aberglaube der Naturwissenschaft angefochten und charakterisiert wird.",
        "Daß die eine oder andere Partei dieses oder jenes als Aber­glaube bezeichnet oder empfindet, das kann niemals ein Charakteristikum werden für das eigentliche Wesen des Aberglaubens.",
        "Mancherlei, was heute hereinragt aus alten Zeiten, zeigt uns ja gerade, wenn es wirklich ein handgreif­licher Aberglaube ist, wie es bei solchen Dingen viel weniger auf die menschliche Logik, auf die menschliche Vernunft ankommt, als vielmehr auf die menschlichen Denkgewohn­heiten, auf dasjenige, was die Menschen zu denken gewohnt worden sind."
      ],
      [
        "Wie vieles geht heute durch unsere populäre Literatur, durch unsere Tagespresse, was scheinbar dem aufgeklärten Denken stracks zuwiderläuft!",
        "So gibt es zum Beispiel eine Stadt in Deutschland - sie ist nicht weit weg von Berlin -, wo Sie vergeblich nach einer Droschke Nummer 13 suchen würden.",
        "Der, welcher sie früher gehabt hat, bekam keinen Fahrgast mehr.",
        "Sie wurde weggelassen, die Nummer 13.",
        "Auch in Hotels können Sie oft die Erfahrung machen, daß die Nummer 13 fehlt in den Zimmernummern.",
        "Sie können"
      ],
      [
        "auch finden in Badeanstalten, wo lauter aufgeklärte Arzte sind, daß bei den Badekabinen die Nummer 13 weggelassen ist, weil niemand hinein will.",
        "Und das mittendrin und neben der Denkweise der heutigen Literatur und Tagespresse.",
        "Wer aber ein klein wenig Seelenkenner ist, der wird schon fin­den, daß der Aberglaube doch etwas ist, was sich ganz leise in das Denken und Fühlen des Menschen einschleicht."
      ],
      [
        "So gibt es jetzt ein populäres Büchelchen über den Aber­glauben, in dem manches Vernünftige und manches Absurde steht.",
        "Aber dann, nachdem der Verfasser abschlachtet, was Astrologie und Astronomie und andere Formen des Aber­glaubens sind, führt er an, daß es in früherer Zeit Astro­logen gegeben haben soll, welche den Leuten Horoskope stellten und aus dem Momente der Geburt ihr Schicksal be­stimmt haben.",
        "Solche Astrologen gäbe es zwar seines Wis­sens nicht mehr; das verrichteten die Hebammen.",
        "In Berlin zwar nicht, aber im übrigen Deutschland käme es vor. -Das ist ein Satz, der tatsächlich in diesem Büchlein über Aberglaube steht.",
        "Ich glaube nicht, daß jemand es anders bezeichnen kann als einen anderen Aberglauben, denn sonst würde er sagen müssen, daß es heute sehr viele Astrologen gibt, die Horoskope stellen.",
        "Was der Mann sagt, entspricht durchaus nicht den Tatsachen; es ist also der purste Aber­glaube.",
        "Jede Untersuchung könnte ihm das Gegenteil seiner Behauptung zeigen.",
        "Ähnliche Sachen schleichen sich jeden Tag in das Bewußtsein der Menschen ein, wenn es auch weniger handgreifliche Dinge sind und man es als Para­doxon ansehen würde, wenn ich von Aberglaube spräche."
      ],
      [
        "Es ist seit einiger Zeit in gewissen Kreisen naturwissen­schaftlicher Betrachtung die Meinung aufgekommen, daß man für alles dasjenige, was auf seelisch-geistigem Gebiete im Menschen als Erinnerung auftritt, physische Ursachen und womöglich physische Ursachen eines ganz bestimmten"
      ],
      [
        "Gebietes, des sexuellen Gebietes, zu suchen hat.",
        "Und nicht nur dieses, sondern zahlreich sind die Schriften und Bro­schüren, welche sich damit beschäftigen, die großen Geister auf ihren Geisteszustand zu prüfen."
      ],
      [
        "Ein Leipziger Gelehr­ter hat sich bis vor kurzer Zeit die besondere Mühe gegeben, eine ganze Reihe großer Geister, unter anderen Goethe, Schopenhauer, Scheffel, Conrad Ferdinand Meyer, darauf­hin zu prüfen, inwiefern sie eigentlich von dieser oder jener Geisteskrankheit befallen wären und ihr Genie zusammen­hinge mit dieser oder jener Geisteserkrankung.",
        "Auf der an­deren Seite wird die Neigung zur Vererbung mit physischer Erkranküng des Menschen zusammengebracht, und es ent­geht kaum ein Tagesereignis in unserer Zeit einer solchen Deutung."
      ],
      [
        "Hier haben wir es mit einem Aberglauben zu tun, der eben jetzt aufgeht, der aber als eine Landplage unsere Bildung durchsetzt.",
        "Künftige Zeiten werden nicht begreifen, wie es möglich war, daß dieWissenschaft eine Zeitlang einem solchenAberglauben huldigen konnte."
      ],
      [
        "Und wenn uns unsere Nachfahren in gleichem Sinne das vergeken werden, in glei­chem Sinne das beurteilen werden, was in früheren Zeiten von unseren Vorfahren geglaubt worden ist, dann werden die, welche auf diesem Gebiete tätig sind, in der schlimmsten Weise wegkommen.",
        "So sehen wir schon, indem wir unbe­fangen die Tatsachen überblicken, die alten Formen des Aberglaubens mit Recht zum Fenster hinausgeworfen und auf der anderen Seite neue Formen sich einschleichen, die eben einfach nicht als solche erkannt werden."
      ],
      [
        "Wer sich ein wenig in der Wissenschaft umtut, der weiß, wieviel Dämonen des Aberglaubens sich da und dort ein­schleichen, die zum Glück nur ein kurzes Dasein haben, aber deshalb nicht weniger schädlich sein können.",
        "Moderichtun­gen sind manchmal nicht weit von dem entfernt, was man Aberglaube nennen kann.",
        "Ich möchte dafür ein Beispiel anführen."
      ],
      [
        "Während meiner Erziehertätigkeit konnte ich manche Beobachtung machen, die nur dadurch möglich war, daß ich ein großes Feld in bezug auf die Menschenentwickelung be­ackern konnte.",
        "Es ist jetzt weit über zwanzig Jahre her, da war es üblich, kleinen Kindern - etwa im zweiten, dritten, vierten Jahre - Rotwein, überhaupt Wein zu trinken zu geben.",
        "Man konnte sehen, wie durch eine gewisse Mode-richtung der Medizin gerade Kinder in diesem Alter jedes­mal zu Tische ihr Glas Rotwein bekamen.",
        "Wer so etwas beobachtet, beobachtet vielleicht zu kurze Zeiträume in bezug auf die Wirkung dieser Dinge.",
        "Wenn man diejenigen Menschen, die heute zwanzigjährig sind, nachdem sie da­mals Kinder von zwei bis fünf Jahren waren, mit anderen vergleicht, die damals keinen Wein zur Stärkung bekom­men haben, so zeigt sich an der gegenwärtigen Nervenver­fassung - wie man sich etwa heute in materialistischer Weise ausdrückt - ganz genau der Unterschied zwischen denjeni­gen, welche Wein bekommen haben, und denen, die ihn nicht bekommen haben."
      ],
      [
        "Da gab es dazumal den Aberglauben, daß der Wein eine Stärke in sich enthalte.",
        "Das war ein Mode-Aberglaube.",
        "Man hat diese Meinung herumgeboten wie irgendeine andere abergläubische Meinung auch herumgeboten wird.",
        "Nun kön­nen wir von alledem absehen und auf manche andere Ge­biete übergehen, wo man gar nicht mehr von Aberglauben spricht, obwohl der seelische Tatbestand im Menschen ganz der gleiche ist.",
        "Wenn wir sprechen wollten davon, was die Leute im sozialen Leben, im politischen Leben für sonder­bare Götzen, für Fetische, für Schlagworte haben, denen sie nachlaufen, wie andere auf anderem Gebiete bestimmten Götzen nachlaufen, und welches Quantum von Aberglau­ben darin enthalten ist, dann würden Sie sehen: Wenn sich das Quantum Aberglaube auf dem einen Gebiete nicht auslebt,"
      ],
      [
        "dann geht es über auf ein anderes Gebiet.",
        "Erhebt sich der Mensch also auf der einen Seite über den Aberglauben, flugs kommt er auf einem anderen Gebiete zum Ausdruck, auf dem man es nur nicht so sehr merkt."
      ],
      [
        "Nachdem wir so ein wenig die Situation charakterisiert haben, dürfen wir vielleicht einmal versuchen, auf den eigentlichen Quell des Aberglaubens, auf die eigentümliche Geistesverfassung zu kommen, in der ein Mensch ist, den wir als einen abergläubischen Menschen bezeichnen dürfen.",
        "Vor allen Dingen darf man sagen, daß bei der Entstehung dieser Geistesverfassung die Befangenheit eines Menschen in dieser oder jener Denkrichtung die denkbar größte Rolle spielt."
      ],
      [
        "Dieselbe Tatsache wird einer - je nachdem seine Denkrichtung so oder so ist - in der einen oder anderen Weise auffassen.",
        "Versuchen wir, uns einmal einen kon­kreten Fall vor das Auge zu rücken.",
        "Der jetzt viel genannte französische Physiologe Richet hatte folgendes Erlebnis: Er ging einmal auf der Straße, und auf der anderen Seite der Straße ging auch eine Person."
      ],
      [
        "In diesem Augenblicke hatte er den Gedanken: Es ist doch merkwürdig, daß Professor Lacassagne heute in Paris ist.",
        "Aber es ist doch nicht so merk­würdig.",
        "Vor vierzehn Tagen hat mir Professor Lacassagne einen Artikel geschickt und geschrieben, daß er in vierzehn Tagen hier sein würde."
      ],
      [
        "Schon wollte Richet auf die andere Seite gehen und ihn begrüßen, als er sich sagte, daß er ja in die Redaktion gehen wolle, und da würde der andere wohl auch hinkommen.",
        "In demselben Augenblicke geht ihm der Gedanke auf, wie ähnlich der Professor einem ihm bekann­ten Augenarzt sieht."
      ],
      [
        "Richet geht auf die Redaktion, und nach einer Stunde erscheint dort Professor Lacassagne.",
        "Richet sagt zu ihm: Ich habe Sie vor einer Stunde auf der Straße gesehen. - Der Professor antwortet: Das ist nicht mög­lich."
      ],
      [
        "Ich war vor einer Stunde nicht dort, sondern ganz woanders. -"
      ],
      [
        "Es ist kein Zweifel, daß Richet ihn nicht gesehen haben konnte.",
        "Es ist eigentümlich, wie sich zwei Menschen oft zueinander verhalten, wenn sie zwei verschiedeneDenk­richtungen haben.",
        "Richet sah einen Menschen und hatte den bestimmten Eindruck, den Professor L. zu sehen.",
        "Als er aber den Professor L. vor sich sah, kam es ihm ganz töricht vor, einen anderen, der groß und blond war, für den Pro­fessor L. gehalten zu haben, während dieser mittelhoch ist und einen dunkeln Schnurrbart trägt.",
        "Richet ist nun aber ein Mensch, der an okkulte Wirkungen, an Gedankenüber­tragung glaubt.",
        "Er sagte sich, der Professor L. ist in Paris und hat gedacht, er wolle in die Redaktion gehen - und in diesem Momente sah ich diesen Gedanken durch Gedanken­übertragung!"
      ],
      [
        "Ein anderer Forscher, der ein Buch über «Aberglaube und Zauberei» geschrieben hat, Lehmann, denkt anders darüber.",
        "Er sagt: «Richet glaubt an Gedankenübertragung; deshalb sieht er in diesem ganz gewöhnlichen Erlebnis etwas Mysti­sches, das die Richtigkeit seines Glaubens beweisen soll, übersieht aber dabei ganz die Nebenumstände, welche die Sache durchaus auf natürliche Weise erklären.»"
      ],
      [
        "Da haben Sie zwei Menschen, die das gleiche Ereignis je nach der Denkrichtung in ganz verschiedener Weise be­urteilen.",
        "Ich selbst möchte dem dänischen Forscher Lehmann recht geben, denn die, welche an okkulte Dinge mit unzu­länglichen Mitteln herangehen, schießen am allerleichtesten über das Ziel hinaus und können sich, wie in diesem Falle, alles mögliche in der Welt damit erklären.",
        "Sie sehen aber daraus, wie die Befangenheit, in der sich ein Mensch in be­zug auf seine Ideenrichtung befindet, einen andern Men­schen, den er vor sich sieht, in einer solchen Weise färbt."
      ],
      [
        "Nun denken Sie, wie sich die Dinge, wenn sie nicht genau durchschaut werden, in der menschlichen Seele spiegeln."
      ],
      [
        "kommen wir zu dem, was in geisteswissenschaftlichem Sinne über das eigentliche Wesen des Aberglaubens gesagt werden muß.",
        "Sie können heute unzählige Schriften und Auseinan­dersetzungen lesen über den Aberglauben an die Alchemie, die unselige Kunst, Gold zu machen, der sich so viele hin­gegeben haben.",
        "Die, welche darüber schrieben, waren meist"
      ],
      [
        "- der heutigen Auffassung nach - in anderer Beziehung außerordentlich tüchtige, positive Forscher.",
        "Sie nehmen in allen möglichen Schriften, in denen auf diese oder jene Weise da oder dort die Kunst, Gold zu machen, mitgeteilt wird, einen hervorragenden Platz ein.",
        "Aber was Sie da lesen, er-scheint Ihnen zumeist als der hellste Wahnsinn, als absolute­ster Unsinn.",
        "Und außerdem erscheint es ja in zahlreichen Fällen als ein so offenliegender Schwindel, daß sehr leicht zu sehen ist, wie eben damals, als die Menschen so etwas geglaubt haben, auf diesem Gebiete Irrtum über Irrtum verbreitet wurde.",
        "Trotzdem sich die Chemie aus der Alche­mie heraus entwickelt hat, müssen wir unendlich froh sein, daß wir endlich die wahre chemische Wissenschaft haben, im Gegensatz zu jenen Fabeleien und Irrtümern, denen sich unsere Vorfahren auf alchemistischem Gebiete hingegeben haben.",
        "Nun können wir vielleicht am leichtesten gerade das, was hier als eine Täuschung vorliegt, begreifen."
      ],
      [
        "Um zu zeigen, wie sich das Entsprechende abgespielt hat, werden wir einige einfache Fälle ins Auge fassen.",
        "Wir wol­len jetzt absehen von der Zahl Dreizehn, aber Sie wissen, daß für manche Leute die Zahl Sieben etwas Gräßliches hervorruft, daß sie von manchen als Glückszahl angesehen wird, manchmal aber auch als Unglückszahl, womit zauber­hafte Wirkungen zusammenhängen.",
        "Ich brauche nur etwas zu erwähnen, das Sie hinführen kann zu dem, was mit der Zahl Sieben zusammenhängt.",
        "Ich will nicht nur erwähnen, daß sich die Zahl Sieben auch in der rein physischen Natur"
      ],
      [
        "findet - sieben Farben, sieben Töne und so weiter -, was hier schon oft erwähnt worden ist und woraus man schlie­ßen kann, daß mit der Zahl Sieben doch dieses oder jenes verbunden ist.",
        "Davon wollen wir aber heute absehen.",
        "Auf etwas anderes wollen wir aufmerksam machen."
      ],
      [
        "Es gibt eine Krankheit, die Lungenentzündung, die sieben Tage wächst und dann abnimmt.",
        "Erst am siebenten Tage tritt die Krisis ein, so daß derjenige, der einen solchen Kran­ken zu behandeln hat, besonders auf diesen physischen Rhythmus achtzugeben hat."
      ],
      [
        "Da haben wir also an die Zahl Sieben einen ganz bestimmten Vorgang geknüpft, etwas, was in jedem einzelnen Falle beobachtet werden kann.",
        "Nun läßt sich die heutige materialistische Wissenschaft durchaus nicht ein auf irgendeine Erklärung dieses Vorgangs."
      ],
      [
        "Würden wir die Medizin in die alten Zeiten zurück verfolgen, in denen Sie durchaus nicht bloß eine Summe von Irrtümern zu sehen haben, wie Sie es heute in der Geschichte der Medi­zin dargestellt finden, würde man sich klarwerden, daß die alten Ärzte und Naturkenner wußten, wie alles Leben in einem gewissen Rhythmus abläuft, daß ein Rhythmus be­steht zwischen dem, was im Menschen geschieht, und man­chem, was draußen in der großen Natur, im Makrokosmos, abläuft.",
        "Weil der Mensch eigentlich aus dem Makrokosmos herausgeboren ist und dessen Leben in gewissen äußeren Vorgängen verläuft, so verläuft auch des Menschen Leben in einem bestimmten Rhythmus."
      ],
      [
        "Wer den Rhythmus des menschlichen Lebens kennt, der weiß ganz gut, daß es in einem Organ wie der Lunge einen durch achtundzwanzig Tage, das heißt durch vier mal sieben Tage hindurch gehen­den auf- und abwogenden Rhythmus gibt, in dem gewisse funktionelle Stärken und Schwächen auftreten.",
        "Da ist es, sobald man diese Grundlage erkennt, nicht weiter verwun­derlich, daß die Erkrankung der Lunge gerade da besonders"
      ],
      [
        "gefährlich wird, wo sie sozusagen zusammenstößt mit dem Rhythmus, um den es sich überhaupt bei den Lebenserschei­nungen handelt.",
        "Kurz, wir würden sehen, wenn wir im Sinne der Geistesforschung hineinleuchten würden, wie in tieferer Erkenntnis des Wesens des Menschen und nicht in irgendeiner abergläubischen Weise, sondern in einer Weise, die als streng gesetzmäßig zu bezeichnen ist, wir uns ver­ständlich machen können, warum nach sieben Tagen eine besondere Krisis für die Lungenentzündung reif ist.",
        "Aber man will ja in unserem materialistischen Zeitalter auf solche Dinge, die sich nur mit den Mitteln der Geisteswissenschaft verfolgen lassen, nicht eingehen."
      ],
      [
        "Es gab eine Zeit, in der die Ärzte nicht nur wußten, daß dieLungenentzündung am siebenten Tage diese Krisis durch-macht, sondern in der sie auch wußten, warum das so ist.",
        "Sie wußten, wie das auch mit dem gesunden Rhythmus zu­sammenhängt.",
        "Aber diese geisteswissenschaftliche Erkennt­nis ist für das äußere Leben vergessen.",
        "Die eigentliche Ge­setzmäßigkeit kennt man nicht mehr, sie ging der Menschheit verloren.",
        "Es blieb die trockene Zahl Sieben.",
        "Man wußte schließlich gar nicht mehr, warum es der Lungenentzündung einfällt, nach siebenTagen etwas ganzBesonderes zu zeigen.",
        "Und dann nimmt man natürlich solch eine Sache heraus, ohne sie weiter verstehen zu können oder zu wollen.",
        "Man wendet sie an, weil man in der Zahl selbst als solcher etwas Besonderes sieht.",
        "Man sagt sich, mit der Sieben hängt etwas Besonderes zusammen.",
        "Irgendwie kann man sie da oder dort anwenden.",
        "Solange man sich an Äußerlichkeiten hält, nicht hineinsieht in die Sache, solange hat man keinen Grund, die Sache da oder dort anzuwenden.",
        "Also wendet man sie da an, wo scheinbar eine Veranlassung da ist.",
        "Und vor allen Dingen spielt da ein menschliches Gesetz hinein, das nur zu verständlich ist: In allen Fällen, wo man eine"
      ],
      [
        "solche Sache als Abstraktion herausgerichtet hat, wo man sie anwendet und es paßt, da geht die Geschichte; paßt es aber nicht, so übersieht man es."
      ],
      [
        "So geht es auch mit manchen Bauernregeln.",
        "Wer auf dem Lande aufgewachsen ist, der wird ganz genau wissen, wie aus dem ersten Gewitter, das im Frühling auftritt, das oder jenes prophezeit wird.",
        "Trifft das Prophezeite ein, so wird es als Gesetz hingenommen, trifft es nicht ein, so wird es vergessen.",
        "Aber trotzdem stecken in manchen Bauernregeln tiefe Weisheiten, und man müßte manche Bauernregel auf ihre tiefe Weisheit hin erforschen.",
        "Dann ist es auch wieder so, daß man nicht das rein Äußerliche des Aberglaubens an­wendet, sondern darauf ausgeht, wirklich in die Sache selbst einzudringen.",
        "Gewiß, mir hat es auch recht gut gefallen, wenn neben anderen Bauernregeln wieder einmal diese aus­gesprochen wird: Kräht der Hahn auf dem Mist, so ändert sich das Wetter, oder es bleibt, wie es ist. - Da zeigt sich ein gesunder Zug, der nicht generalisiert, sondern individuali­siert werden muß.",
        "Und das ist das Wesentliche, auf das es in unserer Geistes- und Seelenentwickelung ankommen soll."
      ],
      [
        "In ähnlicher Weise, nur nicht so durchschaubar, ist es mit vielen Dingen in bezug auf die Alchemie gegangen.",
        "Manche von Ihnen, die schon in vorhergehenden Jahren diese Vor­träge angehört haben, werden wissen, wie damals alles be­sprochen worden ist, wie über die Rosenkreuzer-Einweihung gesprochen und der Stein der Weisen erörtert worden ist, wie da gezeigt worden ist, wie unter dem Stein der Weisen in der wirklichen Geisteswissenschaft aller Zeiten etwas ver­standen wird, was vor unserem gegenwärtigen modernsten Denken, wenn man da hineindringt, durchaus bestehen kann.",
        "Unter den mancherlei Methoden, welche den Menschen zu den höheren Erkenntnissen heraufführen, namentlich zur Rosenkreuzer-Einweihung, da findet sich auch die eine, die"
      ],
      [
        "man geradezu dieBereitung des «Steines derWeisen» nennt.",
        "Unter dieser Bereitung des Steins der Weisen wird etwas verstanden, das zusammenhängt mit einer Regelung des Atmungsprozesses.",
        "Zu den verschiedenen Methoden, durch die der Mensch sich hinaufarbeitet in die höheren Welten, gehört ein gewisses Bewußtwerden und ein nach geistigen Gesetzen geregeltesAtmen in bestimmten Zeiten.",
        "Nach ganz bestimmten Anweisungen atmet derjenige, der ein Jünger der Geisteswissenschaft im positiven Sinne wird."
      ],
      [
        "Dieses Atmen hat für den ganzen Organismus eine ganz bestimmte Folge, welche die äußere Wissenschaft nicht mehr suchen kann, weil sie nichts weiß von der Sache.",
        "Der Mensch entwickelt durch das Instrument seines eigenen Leibes in sich etwas ganz Bestimmtes, etwas, das wirklich in seinem Leben bis in den Leib hinein auftritt, das dann da ist und ihn befähigt zu einer ganz anderen Anschauung der Welt, weil durch die Atmung eine Wirkung geschieht, die sich selbst in der mineralischen Zusammensetzung des physischen Leibes ausdrückt.",
        "So haben wir durch die Regelung des Atmungsrhythmus in dem Menschen selber durch sein eige­nes Instrument etwas erzeugt, das genannt wurde der Stein der Weisen oder der weise Stein.",
        "Es ist das, was notwendig ist zu erzeugen in dem menschlichen Organismus, wenn der Mensch in die höheren Welten hineinwachsen soll.",
        "Der Pro­zeß ist genau angebbar, aber man kann ihn nicht ohne wei­teres jedem beliebigen Menschen mitteilen.",
        "Denn es kann der Natur der Sache nach nur derjenige diesen Prozeß an­wenden, der das in ganz selbstloser, durch gar keine per­sönliche Rücksicht gebundenen Weise tut."
      ],
      [
        "Als ich einmal in einem kleinen Kreise sprach, wie man es heute schon kann, wie ich es auch rückhaltlos in einem der Vorträge andeuten werde - nur das Letzte darf nicht angegeben werden, weil man da auf die geisteswissenschaftliche"
      ],
      [
        "Schulung selbst hindeuten muß -, da sagte einer hin­terher : Das wäre aber doch ganz gut, wenn man diese Methode, ein besonderes Mineral im Menschen zu erzeugen, öffentlich bekanntmachte.",
        "Denn dieses Mineral ist etwas sehr Nützliches, wenn man es in großen Massen herstellen könnte. - Ich mußte antworten: Daß Sie diese Frage stellen, das gibt den Grund an, warum es nicht bekanntgemacht werden darf.",
        "Solange solche Fragen gestellt werden, ist es eben unmöglich, daß das bekanntgemacht werden darf.",
        "Sie können es in der Literatur finden, aber es ist dort ver­schleiert.",
        "Es ist nur verständlich für den, der durch die Vor­schule die Art der Ausdrucksweise kennenlernt.",
        "Quecksilber, Stein der Weisen, Silber, bedeutet nämlich etwas ganz an­deres.",
        "Und wenn man spricht von der Verbindung des Quecksilbers und seiner Hinzufügung zu irgendeinem an­deren Produkte, so bedeutet hier «Quecksilber» und «Stein der Weisen» eben etwas ganz anderes als das Hinstellen äußerer Dinge."
      ],
      [
        "Nun existieren diese Dinge aber in der Literatur.",
        "Die­jenigen, welche keine Ahnung davon haben, was in diesem Fall die Ausdrücke bedeuten und namentlich die Zeichen, die damit verbunden sind, die nehmen die Sache einfach wörtlich.",
        "Wörtlich genommen ist es aber der barste Unsinn.",
        "So zum Beispiel ist es einem dänischen Forscher über Aber­glauben passiert, daß er etwas las über merkwürdige Per­sönlichkeiten des dreizehnten und vierzehnten Jahrhun­derts, über Raimundus Lullus und andere.",
        "Es steht jedem frei, diesen für einen Schwindler, für einen Scharlatan oder für den größten Weisen seiner Zeit zu halten, je nachdem er ihn verstehen kann.",
        "Nun wird aber erzählt, daß es Rai­mundus Lullus gelungen sei, nach einem dreißigjährigen Studium - für die meisten Leute eine unbequeme Sache -den Stein der Weisen zu finden, und daß er dadurch in die"
      ],
      [
        "Lage gekommen sei, Gold zu machen dadurch, daß er einem Teil des Steines eine bestimmte Menge Quecksilber hinzu-gesetzt habe.",
        "Wenn man eine kleine Menge davon nehme, dann bekomme sie die Eigenschaft, dasselbe zu erzeugen.",
        "Von dem werde dann wieder eine kleine Menge genommen, und so weiter, bis zuletzt das Gold entstehe."
      ],
      [
        "Wenn nun einer hingeht und das probiert, wenn er das nimmt, was er im Buche findet, gewisse Stoffe nimmt, sie mischt und sie dem Quecksilber hinzufügt, so ist das der absoluteste Unsinn, der gemacht werden kann.",
        "Es hat jeder das größte Recht, sich darüber lustig zu machen.",
        "Das tut auch der Forscher.",
        "Er macht sich lustig.",
        "Wer aber versteht, die Ausdrücke zu deuten, der wird finden, daß in der Lite­ratur der «Stein der Weisen» ebensogenau vorhanden ist wie in dem, was in Raimundus Lullus' Schriften enthalten ist, und wodurch er zum Ziele gekommen ist.",
        "Das ist das Wunderbare an der Sache, daß der Satz seit Jahrhunderten bekannt ist und heute noch richtig ist.",
        "Das zeigt dem, der etwas davon weiß, wie grandios richtig es ist.",
        "Für den ist es dann klar, daß in Raimundus Lullus wirklich die Seele eines der Weisesten seines Zeitalters steckte.",
        "Wer dagegen nur an der äußeren Ausdrucksweise haften bleibt, der macht wirklich Unsinn."
      ],
      [
        "Diesen Unsinn machten auch sehr viele, die geglaubt haben, daß der weise Alchimist äußeres Gold nachgemacht hat, und sie haben auch den Verstand verloren, obgleich ich glaube, daß ein wenig davon schon verloren war, als sie die Geschichte angefangen haben.",
        "Psychiater aber behaupten, daß sie dadurch um den Verstand gekommen sind.",
        "Um ihr Vermögen können sie gekommen sein, denn Gold haben sie zuletzt nicht gefunden.",
        "Daher darf man dem Schreiber, welcher die Alchimie als Unsinn bezeichnet, gar nicht so unrecht geben, denn - was er davon verstehen konnte, ist"
      ],
      [
        "eben nur Unsinn.",
        "Tatsächlich ist aber kein Unsinn groß genug, um nicht von diesem oder jenem Menschen geglaubt zu werden."
      ],
      [
        "Das hängt mit einer Sucht zusammen, die Sie auf dem Gebiete der Geisteswissenschaft Tag für Tag erleben kön­nen.",
        "Sie erleben leicht folgendes: Wenn Sie diesem oder jenem gegenübertreten mit einer Naturerscheinung, die einer Aufklärung bedarf, und versuchen, eine solche Erscheinung im Zusammenhang mit ihren geistigen Untergründen zu erklären und darauf Anspruch machen, eine alltägliche Er­scheinung auf ihre geistige Unterlage zurückzuführen, dann werden Sie bei den meisten Menschen unserer Gegenwart kein besonderes Interesse erregen.",
        "Viele Menschen unserer Gegenwart suchen nicht das Erklärliche, sondern das Un­erklärliche.",
        "Sie sind froh, wenn sie etwas finden können, was ihnen unerklärlich bleibt.",
        "Erzählen Sie einem, daß sich da oder dort etwas zugetragen hat, wofür kein Mensch eine Erklärung weiß, dann sind sie zufrieden.",
        "Die Menschen wollen also geradezu hingewiesen werden auf das Uner­klärliche.",
        "Sie wollen nicht das, was sich ihnen bietet, durch­dringen, sondern das Wunderbare vermehren.",
        "Versuchen Sie, einem Menschen etwas über die Entwickelung der Pflan­zen zu erklären, indem er sie aus den Untergründen der Entwickelung erfassen und tief in die Natur hineinschauen kann, dann von dem Sinnlichen, wo man den Geist an einem Ende anfaßt, tief hineingeführt wird in das Geistige"
      ],
      [
        "- dann kann er nicht an eine geistige Welt glauben!",
        "Erzäh­len Sie aber einem solchen Menschen, daß eine Hand von einer Statue abhanden gekommen ist, in einer anderen Stadt gefunden wurde und wieder eingesetzt worden ist, da sagen sie: Das kann kein Mensch erklären, folglich glaube ich an eine geistige Welt. - Das ist so, daß die Menschen dem Geiste gegenüber verständnislos bleiben wollen, weil sie"
      ],
      [
        "glauben, daß man das nicht ergründen darf.",
        "Damit eröffnen sie dem Aberglauben aber Tür und Tor an allen Ecken und Enden."
      ],
      [
        "Wenn der Mensch nicht nach Unbefangenheit strebt mit dem, was ihm in seiner Vernunft und in seinem logischen Denken zur Verfügung steht, so ist er in dem Augenblicke, wo er sich auf dieses nicht verlassen will, sobald etwas auf­tritt, was anders ist als gewohnt, schon allen möglichen For­men des Aberglaubens ausgeliefert.",
        "So könnte man zum Beispiel sehen - verzeihen Sie, wenn ich dies sage, obwohl ich voll auf dem Boden der Geisteswissenschaft und Theo-sophie stehe -,wie gerade diejenigen, welche auf dem Boden der Theosophie stehen, ablehnen, was im geisteswissenschaft­lichen Sinne zu einer Aufklärung hinführen könnte."
      ],
      [
        "Als die theosophische Aufklärung in der Welt begonnen hatte, da waren es zwei bedeutsame Menschheitsindividualitäten, von denen diese Weisheit der Menschheit zunächst geoffenbart worden ist.",
        "Diejenigen, welche diese Weisheit bekommen haben, haben sich in der Regel nicht so verhalten, wie es hier unzählige Male charakterisiert worden ist."
      ],
      [
        "Denn wie hätte man sich verhalten können gegenüber einer Wahrheit, die von einer unbekannten Seite her erhalten worden ist?",
        "Es haben die ersten Vermittler der theosophischen Welt­anschauung gesagt : Von Persönlichkeiten, die sich im Hin­tergrunde halten, haben wir die Weisheit, die wir diesem oder jenem Buche anvertrauten. - Da hätte es sich um folgendes handeln können."
      ],
      [
        "Man hätte sagen können: Nun ja, es sind ja ehrenwerte Leute, die diese Weisheit bringen, aber wir wollen diese Weisheit selber prüfen. - Immer wird betont, daß in den höheren Welten forschen kann nur der­jenige, der sich besondere Fähigkeiten erworben hat.",
        "Wenn sie aber mitgeteilt ist, die Weisheit, so daß sie prüfbar ist, wie ist es dann?"
      ],
      [
        "Die Prüfung der Weisheit ist in vielen Fällen"
      ],
      [
        "nicht eingetreten.",
        "Die einen haben auf Treu und Glau­ben, weil ihnen gesagt worden ist, daß sie von höheren Individualitäten gekommen sei, die Sache hingenommen.",
        "Die anderen aber sagen: Ob sie begründet ist oder nicht be­gründet ist, das ist nicht von Bedeutung.",
        "Ob die höheren Individualitäten überhaupt vorhanden sind,darauf kommt es an. - Da sind sie aber irre geworden.",
        "Sie sagen: Wenn man nicht sicher weiß, ob es diese höheren Individualitäten gibt oder nicht gibt, dann lehnen wir die ganze Theosophie ab."
      ],
      [
        "Nun, hätte es denn aber niemals einen geben können, der sich sagte: Mag zunächst diese Weisheit wo auch immer her­gekommen sein.",
        "Jch prüfe sie, ob und wie sie zu den Er­scheinungen des Lebens paßt, ob sie sich bewahrheitet im Leben.",
        "Ich prüfe sie vor allem daraufhin, wie sie sich ver­hält zu dem, was uns die landläufige Weltarischauung, die auf der positiven Wissenschaft aufgebaut ist, gibt.",
        "Wie arm­selig ist das, was uns die positive Weltanschauung gibt gegenüber dem, was von dieser Seite gekonumen ist; aber einsehen kann man es.",
        "Da geht also beim prüfen hervor:"
      ],
      [
        "Diejenigen, von denen diese Weisheit gekommen ist, sind unbedingt größer als diejenigen, welche auf den sogenann­ten wissenschaftlichen Tatsachen stehen.",
        "Und da alles relativ ist, so haben wir keinen Grund, anzunehnten, daß Frau H.P.",
        "Blavatsky ihre Weltanschauung aus dem Wolken-regen erhalten hat.",
        "Nachdem sie als vernünftig befunden ist, so muß sie von irgendwoher stammen.",
        "Es ist das Ver­nünftigste, anzunehmen, daß sie von Menschen stammt.",
        "Ob man sie groß nennen muß, das hängt davon ab, was sich ergibt, wenn man diese Weltanschauung mit derjenigen ver­gleicht, die man schon als groß anerkennt. - Das wäre ver­nünftig gewesen.",
        "Das ist aber das einzige, was tatsächlich dem menschlichen Geist Ehre macht, nicht das Hinnehmen"
      ],
      [
        "auf Treu und Glauben, aber auch nicht das Ablehnen auf Treu und Glauben, sondern das vorurteilslose Prüfen.",
        "Gewiß, forschen kann nicht ein jeder.",
        "Zum Forschen sind diejeni­gen da, die ihre Geisteskraft in besonderer Weise entwickeln können.",
        "Aber unbefangen prüfen kann ein jeder.",
        "Wenn er nur nicht so das Unerklärliche statt des Erklärlichen suchte und im Geiste zufrieden wäre, wenn er das Unerklärliche gefunden hat.",
        "Solange man zu ihm spricht, er soll sich an­strengen, um den Geist zu ergründen, da will er nicht mit.",
        "Wenn man ihm aber etwas mitteilt, das gar nicht zu begrei­fen ist, da ist er dabei, weil es so bequemer ist.",
        "Das ist be­sonders charakteristisch für das, was als Seelenzustand für die Menschen existiert."
      ],
      [
        "Da ist ein anderer Fall, der sich abgespielt hat.",
        "Ich rede wiederum nicht so, als ob Wahres dahintersteckt, sondern ich rede von der menschlichen Seelenverfassung, die dabei zutage getreten ist.",
        "Da wurde erzählt, daß es in gewissen Gegenden Asiens Menschen gebe, welche das Folgende machen können: Sie breiten ein Tuch aus, nehmen ein Seil, werfen das Seil in die Luft, lassen ein kleines Kind daran hinaufklettern, bis es oben unsichtbar wird; sie klettern dann selber nach, und nach einiger Zeit fallen die Glieder des Kindes zerstückelt herunter.",
        "Dann kommt der Fakir auch nach, nimmt einen Sack, packt die Glieder hinein, schüttelt das Ganze, schüttelt dann den Sack aus und - das Kind ist wieder vollständig hergestellt.",
        "Ich will nicht ent­scheiden, was dahintersteckt, sondern nur über die Art und Weise des Aberglaubens der Menschen sprechen.",
        "Der Vor­gang erscheint den Menschen zunächst als etwas, was schwer zu glauben ist.",
        "Es gibt aber merkwürdige Abbildungen, die den ganzen Vorgang so darstellen, wie ein Maler ihn ab­bilden würde, der dabei gewesen wäre.",
        "Er zeichnete also richtig die verschiedenen Stadien: das hinaufgeworfene Seil,"
      ],
      [
        "das emporkletternde Kind und so weiter.",
        "Ein weiterer Be­obachter hat die Sache ganz besonders schlau angelegt, denn er gab auch Photographien dazu.",
        "Auf diesen Photographien sah man aber immer nur die betreffenden Zuschauer, die auf und ab gingen und die Gesichter nach dem Fakir rich­teten."
      ],
      [
        "Aber das übrige sah man nicht.",
        "Ein gewisser S.Ellmore hat eine Erklärung gegeben, so daß die ganze Sache sich leicht aufklären ließ.",
        "Er meinte nämlich, der Betreffende, der die Sache ausführte, müsse ein ganz bedeutender Hypno­tiseur sein, der auf Suggestion so eingestellt war, daß er einer ganzen Gesellschaft den betreffenden Vorgang sugge­rieren konnte."
      ],
      [
        "Da sagten sich die Menschen, daß der Vor­gang kein Aberglaube, sondern Suggestion war, und es schien erklärlich, daß alle Leute hypnotisiert waren.",
        "Einer Person aber kam dieser suggestive Vorgang noch unwahr­scheinlicher vor als der ursprüngliche Vorgang."
      ],
      [
        "Sie dachte nämlich, es könnte doch in der Welt auch Dinge geben, die mit unseren Gesetzen nicht erklärt werden können, und sagte sich: In bezug auf die Suggestion weiß man schon mehreres, aber in bezug auf die Seelenstärke muß man doch noch manches erforschen. - Da wandte diese Person sich an die Stelle, wo man darüber etwas erfahren konnte, an S.",
        "Ellmore."
      ],
      [
        "Dieser erklärte die ganze Geschichte für er­dichtet, worauf schon sein Pseudonym hinweise.",
        "Dieses soll nämlich ein Hinweis auf die Frage sein: Kann einer noch mehr betrügen?",
        "Diese Person hat also die Sache in eine neue Form gekleidet, da sie den Vorgang in der ursprünglichen Form nicht glauben konnte, aber in der neuen Form für das moderne Bewußtsein annehmbar fand."
      ],
      [
        "Sie sehen also, daß es tatsächlich auf die geistige Verfas­sung ankommt, daß es ankommt auf das, was in unserer Seele selber vorgeht, wenn man sich über den Begriff und über das Wesen des Aberglaubens einigermaßen aufklären"
      ],
      [
        "will.",
        "Ob eine Sache richtig oder nicht richtig ist, darüber müssen schließlich ganz andere Faktoren entscheiden.",
        "Aber was uns alle behüten kann vor irgendwelchen Verirrungen, die zum Aberglauben werden, das kann einzig und allein das Streben nach einer wirklichen Erkenntnis sein, nach einem Durchschauen der Dinge.",
        "Derjenige wird immer auf irgendeinem Felde dem Aberglauben verfallen, der nicht wirklich in die Tiefe der Dinge eindringen will.",
        "Es ist nun einmal so, daß diese Umlagerung des Quantums Aberglau­ben durchaus herrscht.",
        "Und damit spreche ich das Grund­gesetz für den Aberglauben aus, wie ich es vorhin schon angedeutet habe, nämlich: Solange der Mensch in der Be­obachtung der physischen Umwelt bleibt, solange er nicht vordringen will zur Geisteswissenschaft, zur wirklichen Er­kenntnis der geistigen Urgründe der Dinge, solange lebt in ihm ein gewisser Bedarf an Aberglaube."
      ],
      [
        "Nehmen Sie meinetwillen einen heutigen Mediziner:"
      ],
      [
        "Wenn er überhaupt denkt, wenn er noch so sehr abweist alle Formen des Aberglaubens - derjenige, der unbefangen ist, kann leicht nachweisen, wie er seinen Bedarf an Aber­glauben in anderer Form reichlich deckt.",
        "Das ist das Gesetz der Kompensation in den menschlichen Seelen.",
        "Daran sehen Sie, wie charakteristisch das Gesetz ist."
      ],
      [
        "Sie haben einen Menschen, der ganz gewiß in jeder Be­ziehung hinaussein will über den uralten Aberglauben, aber wieviel Aberglaube verzeichnet Haed:el in seinen «Lebens-wundern und Welträtseln»!",
        "Diejenigen, die mich kennen, wissen, daß ich Haeckel in allem anerkenne, weil er der große Forscher ist.",
        "Wer mich kennt, der weiß auch, daß ich immer auf das Positive hinweise, das Haeckel geleistet hat.",
        "Weil er aber den alten Aberglauben hinausgeworfen hat und nicht zurückgehen will auf die geistigen Hintergründe der Dinge, da wendet er sich auf ein anderes Gebiet."
      ],
      [
        "wird er der abergläubischste Mensch auf dem anderen Ge­biet.",
        "Auf dem Gebiete von Kraft und Stoff, wie er es sich vorstellt, da tanzen und wirbeln die Atome.",
        "Das nennt er seinen Gott.",
        "Dem Tanzen und Wirbeln der Atome schreibt er zu, daß sie Zustände schaffen können, die einfache Lebe­wesen darstellen, und daß diese wieder sich zusammenset­zen zu komplizierteren, die sich schließlich zusammenfügen zur menschlichen Gehirnform."
      ],
      [
        "Alles, was der Mensch dann fühlen und wollen kann, alles Ideale und Sittliche, ja alle Religionen selber sind für denjenigen, der die Sache unbe­fangen beurteilen kann, dann nur Tanz der Atome.",
        "Für ihn besteht kein Unterschied zwischen dem Atomtanz und den großen Fetischen der afrikanischen Wilden."
      ],
      [
        "Ob der afrika­nische Wilde seinen Holzklotz anbetet und ihn als Gott ansieht, oder ob Haeckel seine kleinen Atome tanzen läßt und sie als kleine Götter ansieht - in bezug auf den Aber­glauben ist zwischen beiden kein Unterschied.",
        "Auf dem­selben Standpunkte steht der eine wie der andere Aber­glaube."
      ],
      [
        "Es gab eine Zeit - sie liegt in gewisser Weise schon hinter uns -, da konnte man sehen, wie dieser Aberglaube nach und nach heraufkam.",
        "Es wurden im Laufe der Zeit neue Entdeckungen der Naturwissenschaft gemacht, nament­lich in der Chemie."
      ],
      [
        "Es wurden neue Verbindungen dadurch erklärbar, daß man Gewichtsunterschiede kleinster Teile im Raume festhielt.",
        "Es wurde durch das Gesetz der Atom-gewichte manches erklärt.",
        "Da erschien es als fruchtbare An­schauung, eine solche Atom-Theorie zu konstruieren."
      ],
      [
        "Später vergaß man, daß man diese Atom-Theorie im Geiste kon­struiert hat.",
        "Die Atome wurden zu wirklichen Götzen, die man anbetete."
      ],
      [
        "Als Schüler schon wurde ich von einem Schuldirektor für den Atom-Aberglauben klar sehend gemacht.",
        "Ein Schul-direktor hat dazumal - es ist lange her -, als die neuen"
      ],
      [
        "Atom-Theorien heraufgekommen sind, alle Erscheinungen der Physik und der Chemie als Bewegungen berechnet.",
        "Er hat allerdings das Denken noch nicht berechnet.",
        "Aber bis in die chemischen Erscheinungen hinein hat er Berechnungen angestellt.",
        "Das Büchelchen, das diese Dinge enthielt, heißt:"
      ],
      [
        "«Die allgemeine Bewegung der Materie als Grundursache aller Naturerscheinungen.» Das war etwas, was denjenigen faszinieren konnte, der auf diese Sache eingeht.",
        "Ich würde gerade dieses Büchelchen einem jeden gern in die Hand geben.",
        "Es ist aber seit langer Zeit nicht mehr im Buchhandel zu haben.",
        "In Bibliotheken dürfte es vielleicht noch zu finden sein.",
        "Da sehen wir den Aberglauben in der Allmacht des Atomwirbels auftauchen."
      ],
      [
        "Nun haben wir der Reihe nach alle möglichen Formen des Aberglaubens in der Naturwissenschaft auftreten sehen.",
        "Denken Sie einmal, daß wir tatsächlich eine gewisse Rich­tung haben in der Naturwissenschaft, die von der Allmacht der Naturzüchtung spricht.",
        "Überall können Sie sehen, daß alles zusammengetragen wird, was für das eine oder andere spricht.",
        "Wenn einmal der betreffende Forscher fasziniert ist von dem betreffenden Schlagwort, das wie ein Götze auf ihn wirkt, so sehen wir gerade in unserer Zeit, wenn wir nur ein Auge dafür haben wollten, ähnliche Fälle.",
        "Schon am Eingang des Vortrages erwähnte ich, wie sich heran­schleichen die Dinge, die sich in nicht allzuferner Zeit als furchtbarer Zeit-Aberglaube enthüllen werden."
      ],
      [
        "Wo ist nun die Ursache des Aberglaubens selber?",
        "Immer tritt die Möglichkeit ein, daß der Aberglaube an die Stelle dessen tritt, was allein als fruchtbarer Gedanke, als frucht­bare Meinung herrschen kann.",
        "Wenn der ursprüngliche Ge­danke, die ursprüngliche Meinung vergessen wird und dafür nur die sich bietende Äußerlichkeit genommen wird, dann vergessen wir, wie bei der sieben Tage langen Krisis, das"
      ],
      [
        "Wesentliche.",
        "Wenn die Siebenzahl herausgerissen und fest­gehalten wird, so besteht die Möglichkeit, daß dies in Aber­glauben umschlägt.",
        "Da haben Sie den Grund dafür, daß ake Weise große Naturerscheinungen zeigen konnten."
      ],
      [
        "Das ist es, was die Geisteswissenschaft dem Menschen bringen wird : daß er nicht das Unerklärliche suchen wird, sondern daß er die Erklärung wird suchen wollen.",
        "Sonst, wenn er stehenbleibt im Gebiete der Umwelt und sich nicht erheben will auf den höheren Standpunkt, von dem aus er sehen kann, was auf dem einen oder anderen Gebiete be­rechtigt oder unberechtigt ist, dann wird er sich nur in der Umlagerung des Aberglaubens befinden.",
        "Wer in der physi­schen Welt stehenbleibt, der verläßt den einen Aberglauben und geht in den anderen ein.",
        "Erst wenn er sich erhebt über sich selbst und über den Aberglauben, sieht er das Rechte sowohl in dem einen wie in dem anderen.",
        "Jean Jacques Rousseau hat schon festgestellt, daß es keinen Unterschied macht, ob man mehr oder weniger klug ist.",
        "Er sagte: Die Gescheiten und die Klugen haben ihre Vorurteile ebenso wie die Dummen, wenn auch die Klugen und Gescheiten manches mehr wissen und mehr Vorurteile haben als die Dummen.",
        "Die Dummen halten dafür an dem wenigen um so zäher fest. - Das ist durchaus ein Gesetz, das derjenige, der das Menschenleben beobachtet, in zahlreichen Fällen bestätigt finden kann.",
        "So sehen wir, daß es im Grunde ge­nommen eine Heilung gegenüber dem Aberglauben gar nicht anders geben kann als durch das Erheben zu dem höheren Standpunkt, von dem aus die Welt in ihren geisti­gen Untergründen überschaubar wird."
      ],
      [
        "Es wird noch mancherlei Aberglaube heraufziehen, und manches schleicht sich heute in unsere Anschauung ein.",
        "Wir sind ja auf einer Bahn der Entwickelung, wo die Menschen eigentlich gar keinen rechten Sinn dafür haben, aus dem"
      ],
      [
        "öffentlichen Leben den Aberglauben, wenn er nicht gerade aus alten Zeiten sich übertragen hat, herauszubringen.",
        "Oh, es gilt durchaus für unsere Zeit auf mancherlei Gebieten dasjenige, was uns eine alte Erzählung sagt.",
        "Nennen Sie es eine Anekdote, aber sie gilt, und sie stellt die Wahrheit bes­ser dar als manches andere.",
        "In einer gewissen Gegend Spa­niens, an der Grenze zwischen zwei Provinzen, war einmal eine Epidemie ausgebrochen.",
        "Es war in der Nähe von zwei Universitäten.",
        "Die eine Universität hatte eine medizinische Fakultät, in der man besonders schwärmte für das Ader-lassen.",
        "In der anderen Universität schwärmte man gegen das Aderlassen.",
        "Und nun waren in der unglücklichen Gegend, wo die Epidemie ausbrach, zwei Ärzte.",
        "Der eine war in der einen, der andere in der anderen Universität ausgebildet.",
        "Der eine verordnete Mittel, und der andere ließ zur Ader.",
        "Es stellte sich heraus, daß der eine Arzt alle Patienten er­hielt, denn die Patienten des anderen Arztes starben alle.",
        "Der eine schiebt den anderen zurück.",
        "Wenn dem einen auch alle leben und dem anderen auch alle sterben, so verfahren sie doch beide richtig: der eine zwar falsch in der Praxis, aber richtig nach der Theorie."
      ],
      [
        "Wenn man eine solche Sache erzählt, so kann sie einem albern erscheinen.",
        "Wenn man sie aber Tag für Tag sieht, dann findet man, daß sie nichts Falsches sagt, und man findet sie sogar notwendig.",
        "Deshalb kann es sich, wenn über den Aberglauben gesprochen wird, nur darum handeln, daß die Geisteswissenschaft wahrhaftig am allerwenigsten einen Grund hat, diesen oder jenen Aberglauben zu propagieren.",
        "Sie steht auf dem Boden, daß das Geistesleben erforschbar ist und daß es Mittel und Wege gibt, um hineinzudringen in die geistige Welt, durch die man von einem höheren Ge­sichtspunkte aus die Welt zu überschauen vermag.",
        "Dadurch wird der Mensch hinausgeführt über das, was Aberglaube"
      ],
      [
        "ist, und auch hinausgeführt über das, was Aberglaube im menschlichen Leben als Schaden anrichten kann.",
        "Man kann dasjenige, was hier gilt, mit einem Goetheschen Wort aus­drücken, das in umfassender Weise, wenn auch einfach, die Wahrheit enthüllt: «Die Weisheit ist ewig, und sie wird siegen, und sie wird in uns allen in den mannigfaltigsten Tumulten den Menschen zur Menschheit erhöhen.»"
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "ERNÄHRUNGSFRAGEN IM LICHTE DER GEISTESWISSENSCHAFT Berlin, 17. Dezember 1908",
    "paragraphs": [
      "ERNÄHRUNGSFRAGEN IM LICHTE DER",
      "GEISTESWISSENSCHAFT",
      "Berlin, 17. Dezember 1908",
      "Es erscheint manchem sonderbar, wenn die Geisteswissen­schaft spricht über dasjenige, was mit einem gewissen Recht als das Materiellste, als das Ungeistigste von vielen ange­sehen wird: über die Ernährung. Es gibtMenschen, die ihren besonderen Idealismus, ja ihre besondere Geistigkeit da­durch andeuten wollen, daß sie sagen: Ach, wir kümmern uns nur um dasjenige, was erhaben ist über die Fragen, die mit dem materiellenLeben zusammenhängen.- Solche Men­schen glauben dann auch - und in gewisser Beziehung mögen sie recht haben -, daß es im Grunde genommen für die Ent­wickelung im Idealen und Spirituellen gleichgültig sei, wie der Mensch seine Bedürfnisse in bezug auf das Leibliche be­friedigt. Anders urteilt die materialistische Denkweise. Ein großer Philosoph des neunzehnten Jahrhunderts hat einen Ausspruch getan, der viel wiederholt worden ist und der bei vielen Menschen, die geistig idealistisch gesinnt sind, Schauer und Entsetzen hervorruft, den Ausspruch, den Feuerbach getan hat: «Der Mensch ist, was er ißt.» Die meisten Menschen fassen das so auf - und der materialisti­sche Sinn wird durchaus damit einverstanden sein -, der Mensch sei eine Zusammenfassung der Materien, die er sei­nem Leibe zuführt, und dadurch entstehe nicht nur das Wechselspiel seines organischen Lebens, sondern auch das­jenige, was in seinem Geiste sich darbietet.",
      "Wenn Außenstehende manchmal dieses oder jenes mehr",
      "oder weniger oberflächlich hören über Anthroposophie oder Geisteswissenschaft, so glauben sie, daß sich die Anhänger viel zu viel mit Essen, mit Ernährung beschäftigen. Ein Außenstehender kann es nicht begreifen, warum die An­throposophen gar so viel darauf halten, ob einer dies oder jenes ißt. Es soll nicht geleugnet werden, daß in manchen anthroposophischen Kreisen, bei denen, die auf leichte Weise so recht tief in das geistige Leben hineinwollen, recht viel Unklarheit herrscht. Glaubt doch mancher, daß er nur das oder das meiden solle, nicht essen oder trinken solle, um allein dadurch zu gewissen höheren Stufen der Erkennt­nis hinaufzukommen! Das ist ebenso ein Irrtum, wie jene eben charakterisierte Auffassung des Ausspruches von Feuerbach: «Der Mensch ist, was er ißt.» Zum mindesten ist es eine einseitige Auffassung.",
      "Aber in gewisser Weise kann gerade die Geisteswissen­schaft diesen Satz für sich in Anspruch nehmen, nur in einer etwas anderen Art, als es von den Materialisten gemeint ist, und zwar in einer zweifach anderen Art. Zunächst haben wir ja schon öfters betont, daß für die Geisteswissen­schaft alles um uns herum der Ausdruck eines Geistigen ist. Ein Mineral, eine Pflanze oder irgend etwas in unserer Umgebung ist nur seiner Außenseite nach stofflich. Wie das Glied eines Menschen ist es der Ausdruck, die Geste des Geistes. Hinter allem Materiellen ist Geistiges, auch hinter der Nahrung. Mit ihr nehmen wir nicht nur das auf, was materiell vor unseren Augen sich ausbreitet, sondern wir essen mit das, was Geistiges dahinter ist. Wir treten durch die Ernährung durch dieses oder jenes materielle Substrat in Beziehung zu diesem oder jenem Geistigen, das dahinter­steckt. Das ist eine ganz oberflächliche Charakteristik. Aber schon wer dieses erfaßt, wird in gewisser Beziehung den materialistischen Satz zugeben können: Der Mensch ist,",
      "was er ißt. Nur muß zugleich mit dem materiellen Prozeß ein geistiger verstanden werden.",
      "Das ist aber nur die eine Art, wie wir uns über diese Fragen im geisteswissenschaftlichen Sinne orientieren kön­nen. Wenn die Geisteswissenschaft einen gewissen Wert legt und Nachforschungen anstellt auf und über die Natur der Nahrungsmittel, so geschieht das, weil sich hier eine ganz eigenartige Perspektive in bezug auf die Beziehung des Menschen zur Natur herausstellt. Der Mensch steht aller­dings dadurch in einer Beziehung zur Natur, daß er die umgebende Natur in gewisser Weise aufnimmt, sich zu­sammensetzt mit dem, was darinnen ist. Und es entsteht die Frage: Wird der Mensch nicht dadurch, daß er so sich aneignet, was draußen ist, hingegeben an diese Kräfte, die draußen wirken, und kann er sich freimachen von diesen Kräften? Gibt es eine Möglichkeit, daß der Mensch frei wird von dieser seiner Umgebung durch seine Nahrung, so daß er eine gewisse Macht und einen gewissen Einfluß er­hält über die Umgebung? Könnte es nicht so sein, daß der Mensch in der Tat das sein könnte, was er ißt, durch eine gewisse Art der Ernährung - und könnte es nicht so sein, daß durch eine andere Art der Ernährung der Mensch sich frei macht von dem Zwange, der durch die Ernährung auf ihn ausgeübt wird? Also entsteht für die Geisteswissen­schaft die Frage: Wie muß die Ernährung des Menschen gestaltet sein, damit er frei wird von dem Zwange der Ernährung, damit er immer mehr Herr und Gebieter über das wird, was in ihm vorgeht?",
      "Indem wir diese Frage heute vor uns hinstellen, muß einiges über die ganze Stellung der Geisteswissenschaft zu diesen Fragen gesagt werden. Diese Frage, auch die über Gesundheitsfragen, muß so aufgefaßt werden, daß der Geisteswissenschaft in keiner Weise eine Agitation nach",
      "dieser oder jener Richtung zugeschrieben wird. Wer etwa glaubt, daß mit dem, was heute gesagt werden soll, agitiert wird für oder gegen diese oder jene Nahrung oder Genuß­mittel, der hat eine im höchsten Grade irrige Ansicht. Kei­ner sollte heute mit der Ansicht von hier fortgehen, daß hier eingetreten würde für oder gegen Abstinenz, Vege­tarismus, Fleischkost. Alle diese Fragen über Dogmen, über etwas Alleinseligmachendes, haben mit dem innersten Ge­fühlsnerv der Geisteswissenschaft gar nichts zu tun. Wir wollen nicht agitieren, nicht den Menschen nach dieser oder jener Weise kommandieren; wir wollen nur sagen, wie die Dinge wirklich sind. Dann mag sich jeder sein Leben ein­richten, wie er will, nach diesen großen Gesetzen des Da­seins. Also der heutige Vortrag will einzig und allein sagen, was auf diesem Gebiete wirklich ist. Auf der anderen Seite bitte ich sehr, zu berücksichtigen, daß ich nicht für anthro­posophische Kreise im engeren Sinne spreche, die eine ge­wisse Entwickelung durchmachen wollen und spezielle Be­dingungen einzuhalten haben. Heute wird die Frage im allgemeinmenschlichen Sinne erörtert werden. Bei dem gro­ßen Umfange des Themas wird nur einzelnes heraus-genommen werden können, und vor allem muß alles das vermieden werden, was mit dem Gesundheitlichen des Lebens zusammenhängt. Das werden wir in dem nächsten Vortrag hören.",
      "Wir werden uns heute mit der Ernährung im engeren Sinne befassen. Deshalb wird der Atmungsprozeß hier nicht berücksichtigt werden. Der Mensch hat, um den Lebensprozeß seines Organismus zu unterhalten, aufzunehmen:",
      "Eiweiß, Kohlehydrate, Fette und Salze. Sie wissen, daß der Mensch die Bedürfnisse, die sein Organismus nach dieser Richtung hat, durch die sogenannte gemischte Kost befrie­digt. Er übernimmt diese Hauptbestandteile seiner Ernäh­rung",
      "zum Teil aus dem tierischen, zum Teil aus dem pflanz­lichen Reiche. Es gibt unter unseren heutigen Zeitgenossen viel mehr Verteidiger einer gemischten Nahrung als einer einseitigen Kost, sagen wir etwa einer nur tierischen oder nur pflanzlichen Kost. Wir müssen uns fragen: Wie stellt sich dasjenige, was die Gesetze unserer Umgebung sind, aus denen der Mensch seine Nahrung nimmt, zu den wahren Kräften und Bedürfnissen des menschlichen Organismus? Heute ist hier nur vom Menschen die Rede, nicht von den Tieren.",
      "Der Mensch ist leicht geneigt, nach den sogenannten wissenschaftlichen Resultaten seiner Zeit seinen Organismus recht materiell aufzufassen. Die Geisteswissenschaft muß das ersetzen durch die Gesetze der geistigen Zusammen­hänge. Wenn auch theoretisch nicht immer, so liegt doch praktisch dem Verfahren, das eingeschlagen wird, mehr oder weniger unbewußt der Gedanke zugrunde, daß der menschliche Organismus mehr oder weniger nur aus dem physischen Leib, den chemischen Stoffen in ihrer Wechsel­wirkung aufeinander bestehe. Man verfolgt diese Substan­zen bis in ihre chemischen Elemente hinein und versucht, nachdem man erkannt hat, wie diese Substanzen wirken, sich ein Bild davon zu machen, wie sie chemisch weiter-wirken könnten in der großen Retorte, als die man den Menschen ansieht. Es soll nicht behauptet werden, daß nicht etwa viele schon hinaus wären über die Ansicht, der Mensch sei nur eine große Retorte. Es kommt nicht auf die Theorien an, sondern auf die Denkgewohnheiten. Dem wahren Prak­tiker kommt es nicht darauf an, was einer denkt, sondern was für Wirkungen seine Gedanken haben. Darauf kommt es an. Ob einer Idealist ist oder nicht, darauf kommt es nicht an, sondern für das Leben ist es wichtig, ob einer fruchtbare Gedanken hat, die so sind, daß das Leben gedeiht",
      "und fortschreitet. Gerade das darf nicht außer acht gelassen werden, daß Geisteswissenschaft auch nach dieser Richtung hin nichts zu tun hat mit einem Dogma, mit irgendeinem Glauben. Mag einer noch so sehr die spirituell­sten Theorien vertreten: darauf kommt es nicht an, son­dern darauf, daß diese Gedanken fruchtbar sind, wenn er sie ins Leben überführt. Wenn also einer sagt, er sei nicht Materialist, er glaube an die Lebenskraft, ja sogar an einen Geist, aber in der Ernährungsfrage immer so vorgeht, als ob der Mensch eine große Retorte wäre, so kann seine Weltanschauung nicht fruchtbar werden. Nur dann hat Geisteswissenschaft über diese konkreten Fragen etwas zu sagen, wenn sie selbst in das einzelne hineinzuleuchten ver­mag, und das kann sie sowohl in bezug auf die Ernährungs­wie auch in bezug auf die Gesundheitsfragen.",
      "Wir müssen uns wieder über die vielgliedrige menschliche Wesenheit klarwerden. Für den Geistesforscher ist der Mensch nicht nur das physische Wesen, das man mit Augen sehen, mit Händen greifen kann, sondern dieser physische Leib ist nur ein Teil der menschlichen Wesenheit. Dieser physische Leib besteht allerdings aus denselben chemischen Stoffen, die in der Natur ausgebreitet sind. Aber die menschliche Natur hat höhere Glieder. Schon der nächste Teil der menschlichen Wesenheit ist übersinnlich, hat eine höhere Realität als der physische Leib. Er liegt dem physi­schen Leib zugrunde, er ist durch das ganze Leben hindurch ein Kämpfer gegen den Zerfall des physischen Leibes. In dem Augenblick, wo der Mensch durch die Pforte des Todes schreitet, ist der physische Leib nur seinen eigenen Gesetzen unterworfen und zerfällt. Im Leben kämpft der Lebensleib gegen den Zerfall. Er gibt den Stoffen und Kräften andere Richtungen, andere Zusammenhänge als sie haben würden, wenn sie nur sich selber folgten. Für das hellseherische Bewußtsein",
      "ist dieser Leib ebenso sichtbar wie der physische Leib für das Auge. Diesen Lebensleib oder Atherleib hat der Mensch mit der Pflanze gemeinsam.",
      "Wir wissen aus anderen Vorträgen, daß der Mensch noch ein drittes Glied seiner Wesenheit hat, den astralischen Leib. Wie ist er? Er ist der Träger von Lust und Leid, Be­gierden, Trieben und Leidenschaften, von alledem, was wir unser inneres Seelenleben nennen. Alles das hat seinen Sitz im astralischen Leib. Er ist geistig wahrnehmbar, wie der physische Leib für das physische Bewußtsein. Diesen astra­lischen Leib hat der Mensch mit den Tieren gemeinsam.",
      "Das vierte Glied ist der Träger des Ichs, des Selbst­bewußtseins. Dadurch ist der Mensch die Krone der Schöp­fung, dadurch ragt er hinaus über die Dinge der Erde, die ihn umgeben. So steht der Mensch vor uns mit drei unsicht­baren Gliedern und einem sichtbaren Glied. Diese wirken immer durcheinander und miteinander. Alle wirken auf jedes einzelne und jedes einzelne wirkt auf alle andern. So kommt es, daß der physische Leib - ich sage noch einmal in Parenthese, daß das alles nur für den Menschen gilt -, so wie er vor uns steht, ein Ausdruck ist in allen seinen Teilen auch von den unsichtbaren Gliedern der menschlichen Na­tur. Dieser physische Leib könnte in sich nicht die Glieder haben, die der Nahrung, der Fortpflanzung, die dem Leben überhaupt dienen, wenn er nicht den Atherleib hätte. Alle Organe, die zur Ernährung und Fortpflanzung dienen, die Drüsen und so weiter, sind der äußere Ausdruck des Äther-leibes. Sie sind das, was der Atherleib am physischen Leibe baut. Unter anderem ist im physischen Leibe das Nerven­system der Ausdruck des astralischen Leibes. Hier ist der astralische Leib der Akteur, der Aufbauer. Wir können uns vorstellen, gerade wie eine Uhr oder eine Maschine von einem Uhrmacher oder von einem Maschinenbauer aufgebaut",
      "sind, so sind es die Nerven von dem astralischen Leibe. Und die Eigenart der menschlichen Blutzirkulation, der Bluttätigkeit, sie ist der äußere physische Ausdruck des Ich-Trägers, des Trägers des Selbstbewußtseins. So ist auch der menschliche physische Leib in gewisser Weise vierglied­rig. Er ist ein Ausdruck der physischen Glieder, also seiner selbst, und der drei höheren, unsichtbaren Glieder. Rein physisch sind die Sinnesorgane; die Drüsen sind der Aus­druck für den Ätherleib, das Nervensystem für den astra­lischen Leib und das Blut für das Ich.",
      "Sehen wir den Menschen im Gegensatz zur Pflanze an, so steht die Pflanze als zweigliedrige Wesenheit vor uns. Die Pflanze hat einen physischen Leib und einen Ätherleib. Wir vergleichen nun den Menschen mit der Pflanze, indem wir allseitig vorgehen und das Innere, Geistige berücksichtigen. Wir setzen in Beziehung den menschlichen viergliedrigen Organismus mit dem zweigliedrigen Organismus der Pflan­zen. Zum Unterstützen können wir ausgehen von physi­schen, bekannten Tatsachen. Wir können darauf hinweisen, wie die Pflanze ihren Organismus aufbaut. Sie setzt un­organische Stoffe zusammen zu ihrem Körper. Sie hat die Kraft, aus einzelnen unlebendigen Bestandteilen ihren Leib in der wunderbarsten Weise zusammenzugliedern. Wir brauchen ja nur einmal zu sehen, wie die Pflanze in merk­würdiger Wechselwirkung steht zum Atmungsprozeß. Der Mensch atmet Sauerstoff ein und gibt Kohlensäure von sich. Diese, die für den Menschen unbrauchbar ist, kann die Pflanze aufnehmen. Sie behält den Kohlenstoff zurück zum Aufbau ihres Organismus und gibt den Sauerstoff zum größten Teil wieder zurück. Aber sie braucht etwas dazu, was von vielen vielleicht nicht als etwas Besonderes auf­gefaßt wird: sie braucht das Sonnenlicht. Ohne das Sonnen­licht könnte sie nicht ihren Organismus aufbauen. Das",
      "Licht, das zu unserem Entzücken zu uns strömt, das uns auch seelisch so beleben kann, ist zugleich der großartige Helfer zum Aufbau des pflanzlichen Organismus. Wir sehen, wie da ein Wunderwerk vor sich geht, wie das Sonnenlicht hilft, ein organisches Wesen aufzubauen. Was unsere Augen erst wirksam macht, das ist es, was der Pflanze im Aufbau hilft.",
      "Der Mensch hat außer dem physischen und dem Äther-leibe noch den astralischen Leib. Den hat die Pflanze nicht. Das, was dem Sonnenlichte hilft, die Pflanzen in so wun­derbarer Weise aufzubauen, das ist der Ätherleib. Dieser ist auf der einen Seite den Stoffen zugewandt. Der Mensch könnte seinen physischen Organismus nicht entwickeln, wenn er nicht etwas täte, was in gewisser Weise entgegen­gesetzt ist dem, was die Pflanze tut. Schon in dem Atmungs­prozeß tut der Mensch etwas Gegensätzliches. Der Mensch macht hier schon den gegenteiligen Prozeß durch. Dasselbe können wir sagen in bezug auf alle Ernährung des Men­schen. Wir können sagen: Die Ernährung muß so vor sich gehen, daß alles, was in der Pflanze aufgebaut wird, im Menschen wieder abgebaut wird. Der Prozeß im Menschen ist ein sehr eigentümlicher. Wenn nur der Ätherleib einen physischen Leib aufbaute, so würde niemals Bewußtsein, Seelenempfindung auftreten. Es muß innerlich immer wie­der zerstört, abgebaut werden, was der Ätherleib aufgebaut hat. So ist zwar der Ätherleib ein Kämpfer gegen den Zer­fall, aber trotzdem tritt immer ein stückweiser Zerfall ein. Und dasjenige, was diesen Zerfall bewirkt, was immer den Menschen hindert, Pflanze zu sein, das ist der astralische Leib.",
      "Das Sonnenlicht und der menschliche astralische Leib sind in gewisser Weise zwei entgegengesetzte Dinge. Für den, der mit hellseherischem Bewußtsein des Menschen",
      "astralischen Leib kennenlernt, für den ist der astralische Leib ein inneres Licht, das geistiger Art ist, für das äußere Auge unsichtbar. Ein geistiger Lichtleib ist dieser astralische Leib. Er ist der Gegensatz zu dem äußeren, äußerlich leuch­tenden Licht. Denken Sie sich einmal das Sonnenlicht immer schwächer werdend, bis es erlischt, und lassen Sie es jetzt noch weiter nach der anderen Seite gehen, lassen Sie es negativ werden, so haben Sie inneres Licht. Und dieses in­nere Licht hat die entgegengesetzte Aufgabe als das äußere Licht, das aus anorganischen Stoffen den pflanzlichen Leib aufbauen soll. Das innere Licht, das die partielle Zerstörung einleitet, durch die allein Bewußtsein möglich ist, bringt den Menschen zu einer höheren Stufe, als die Pflanze sie einnimmt, dadurch, daß der Prozeß der Pflanzen in einen entgegengesetzten verwandelt wird. So steht der Mensch durch sein inneres Licht in einem gewissen Gegensatz zur Pflanze. Das ist die Sache geistig aufgefaßt, und wir wür­den bei weiterer Betrachtung sehen, wie die durch den astralischen Leib bewirkte Zerstörung durch das Ich weiter fortgesetzt wird. Aber das braucht uns heute nicht weiter zu beschäftigen.",
      "Nehmen wir jetzt das Verhältnis des Menschen zur Pflanze, wenn es so real wird, daß der Mensch seine Nah­rungsstoffe aus der Pflanze aufnimmt. Er bildet in sich selber für den ganzen Weltprozeß eine Fortsetzung der Pflanze. Was durch das Sonnenlicht aufgebaut wird, das zerstört der astralische Leib zwar immer wieder, aber er gliedert dadurch dem Menschen das Nervensystem ein und erhebt dadurch das Leben zu einem bewußten. So ist der astralische Leib dadurch, daß er ein negativer Lichtleib ist, der andere Pol, der dem pflanzlichen entgegengesetzt ist. Diesem Prozeß des Aufbauens des Pflanzenorganismus liegt ein Geistiges zugrunde, denn die Geisteswissenschaft zeigt",
      "uns immer mehr, wie das, was uns als Licht erscheint, auch nur der äußere Ausdruck eines Geistigen ist. Durch das Licht fließt uns fortwährend Geistiges zu, das Licht der Geister fließt uns zu. Was sich hinter diesem physischen Licht verbirgt, das ist es, was in Teile zerteilt auch im astra­lischen Leibe erscheint. Äußerlich im Sonnenlichte erscheint es in seiner physischen Form, im astralischen Leibe in astra­lischer Weise. Das Geistige des Lichtes arbeitet in uns inner­lich am Aufbau unseres Nervensystems. So wunderbar wir­ken zusammen das pflanzliche und das menschliche Leben.",
      "Nehmen wir nun an, der Mensch tritt durch die Nahrung in ein Verhäknis mit der tierischen Welt. Dann ist die Sache anders. In dem Wesen, dem er dann seine Nahrungsmittel entnimmt, ist in gewisser Weise der Prozeß schon voll­zogen. Was er sonst jungfräulich und frisch von der Pflanze entnimmt, das ist im Tiere schon teilweise umgewandelt, schon vorbereitet. Denn auch das Tier gliedert sich schon einen astralischen Leib und ein Nervensystem ein. So nimmt der Mensch dann etwas auf, was ihm nicht jungfräulich ent­gegentritt, sondern was den Prozeß schon durchgemacht hat, was schon astralische Kräfte aufgenommen hat. Was im Tiere lebt, das hat schon in sich entwickelte Kräfte des Astralischen. Nun könnte man glauben, daß dadurch dem Menschen Arbeit erspart würde. Dieser Gedanke ist aber nicht ganz richtig. Denken Sie sich einmal folgendes: Ich mache aus verschiedenen Gerätschaften ein Haus. Ich nehme die ursprünglichen Gerätschaften. Da kann ich das Haus ganz nach meinen ursprünglichen Intentionen aufbauen. Nehmen wir aber an, drei oder vier andere Personen haben schon daran stückweise gearbeitet und nun soll ich daraus ein Ganzes machen. Wird mir das die Arbeit erleichtern? Nein, ganz gewiß nicht. Sie werden in einer weitverbreite­ten Literatur lesen, daß dem Menschen dadurch eben die",
      "Arbeit erleichtert würde, daß er etwas aufnimmt, an dem schon vorgearbeitet ist. Aber der Mensch wird gerade da­durch ein beweglicheres, selbständigeres Wesen, daß er das Ursprüngliche aufnimmt.",
      "Noch ein Bild: Jemand hat eine Waage mit zwei Waag­schalen. Gleiche Gewichte halten sich das Gleichgewicht. Auf beiden Seiten mögen fünfzig Pfund liegen. Aber so ist es nicht immer. Ich kann eine Waage nehmen, auf der das Gewicht zu verschieben ist. Wir haben dann in doppelt so großer Entfernung nur halb so großes Gewicht nötig. Hier wird das Gewicht durch die Entfernung bestimmt. Ebenso kommt es nicht nur auf die Menge der Kräfte an, sondern besonders auf die Feinheit der Stoffe. Das Tier verarbeitet die Stoffe in unvollkommenerem Sinne. Was da aufgenom­men wird vom Menschen, wirkt fort durch das, was durch den Astralleib des Tieres daran geschehen ist, und das hat der Mensch dann erst zu überwinden. Aber weil ein Astral-leib so gewirkt hat, daß in einem bewußten Wesen bereits ein Prozeß sich abgespielt hat, so bekommt der Mensch etwas in seinen Organismus hinein, was auf sein Nerven­system einwirkt.",
      "Das ist der Grundunterschied zwischen Nahrung aus dem Pflanzenreich und Nahrung aus dem Tierreich. Nahrung aus dem Tierreich wirkt in ganz spezifischer Weise auf das Nervensystem und damit auf den Astralleib. Aber bei pflanzlicher Nahrung bleibt das Nervensystem unberührt durch etwas Äußeres. Der Mensch muß sich dann allerdings auch alles selber verdanken in bezug auf das Nervensystem. Dadurch aber durchströmen die Wirkungen seiner Nerven nicht fremde Produkte, sondern nur das, was in ihm selbst urständet. Wer weiß, wie viel im menschlichen Organismus vom Nervensystem abhängt, der wird verstehen, was das heißt. Wenn der Mensch sein Nervensystem selbst aufbaut,",
      "so ist es voll empfänglich für das, was der Mensch ihm zu­muten soll in bezug auf die geistige Welt. Seiner Nahrung aus der Pflanzenwelt verdankt der Mensch das, daß er hinaufblicken kann zu den großen Zusammenhängen der Dinge, die ihn erheben über die Vorurteile, die aus den engen Grenzen des persönlichen Seins entspringen. Überall, wo der Mensch frei und unbekümmert aus den großen Ge­sichtspunkten heraus Leben und Denken regelt, da ver­dankt er diesen raschen Überblick seiner Nahrungsbezie­hung zur Pflanzenwelt. Da, wo der Mensch durch Zorn, Antipathie, durch Vorurteile sich hinreißen läßt, da ver­dankt er das seiner Nahrung aus der Tierwelt.",
      "Es soll hier aber nicht agitiert werden für pflanzliche Nahrung. Im Gegenteil: Die tierische Nahrung war dem Menschen notwendig und ist vielfach noch heute notwendig, weil der Mensch auf der Erde fest sein sollte, ins Persönliche eingeklemmt sein sollte. Alles, was den Menschen zu sei­nen persönlichen Interessen gebracht hat, das hängt zusam­men mit der tierischen Nahrung. Daß es Menschen gegeben hat, die Kriege geführt haben, die Sympathie und Anti­pathie, sinnliche Leidenschaften zueinander hatten, das kommt her von der tierischen Nahrung. Daß aber der Mensch nicht in den engeren Interessen aufging, daß er all­gemeine Interessen fassen kann, das verdankt er seinen Beziehungen zur Pflanzenwelt in bezug auf die Nahrung. So gehen ja auch bei gewissen Völkern, die vorzugsweise pflanzliche Nahrung nehmen, die Anlagen mehr zum Spiri­tuellen, während andere Völker mehr Tapferkeit, Mut, Kühnheit entwickeln, die ja auch zum Leben nötig sind. Diese Dinge sind ohne persönliches Element nicht zu den­ken, und dieses ist nicht möglich ohne tierische Nahrung.",
      "Wir sprechen heute über diese Fragen von ganz allgemein menschlichem Standpunkte aus. Aber das macht uns klar,",
      "daß der Mensch nach dieser oder jener Seite ausschlagen kann, sich also auch in seine persönlichen Interessen hinein­versenken kann durch die tierische Nahrung. Dadurch wird sein Sinn getrübt in bezug auf die große Überschau des Daseins. Man sieht meistens nicht, wie es in der Nahrung begründet ist, wenn der Mensch sagt: Nun weiß ich wieder nicht, wie soll ich dies oder das machen, wie hat er es ge­macht? - Diese Unmöglichkeit des Überschauens der Zu­sammenhänge kommt von der Nahrung her. Vergleichen Sie das mit einem, der große Zusammenhänge überschauen kann. Sie können dann auf die Nahrung dieser Menschen und vielleicht auch auf die Nahrung der Vorfahren zurück­blicken. Ganz anders ist ein Mensch, der schon in seiner Vorfahrenreihe ein jungfräuliches Nervensystem hat. Die­ser Mensch hat einen anderen Sinn für die großen Zusam­menhänge. Ein Leben kann da manchmal das gar nicht zerstören, was die Vorfahren begründet haben. Wenn da auch ein Mensch, der zum Beispiel von Bauern abstammt, doch das aufstachelt, was er in sich hat, so ist es eben nur durch das Fleisch herausgekommen, weil er empfindlicher war.",
      "Der Fortschritt wird darin bestehen, daß der Mensch, in­sofern der Eiweißbedarf nicht in ihm, in der menschlichen Natur selbst zubereitet ist, sich in der tierischen Nahrung beschränkt auf dasjenige, was noch nicht von Leidenschaf­ten durchglüht ist, wie Milch. Die Pflanzennahrung wird einen immer weiteren Raum einnehmen in der menschlichen Nahrung.",
      "In bezug auf einzelne Nahrungsmittel können wir ge­wisse Vorzüge der Pflanzenkost hervorheben. Wenn der Mensch sich sein Eiweiß aus der Pflanzenkost holt, wobei allerdings härtere Arbeit erforderlich ist, so entwickelt er Kräfte, die sein Nervensystem frischer machen. Vieles, dem",
      "die Menschheit entgegengehen würde, wenn die Fleisch­nahrung überhand nähme, wird vermieden durch vorzugs-weises Berücksichtigen der Pflanzenkost. An der vegetari­schen und animalischen Nahrung können wir sehen, wie gegensätzlich sie wirken.",
      "Zur Illustration können wir fol­gendes sagen: Sehen wir uns den physischen Prozeß an unter dem Einfluß von Fleischnahrung. Die roten Blut­körperchen werden schwer, dunkler, das Blut hat eine größere Neigung zu gerinnen.",
      "Es bilden sich in leichterer Weise Einschläge von Salzen, von Phosphaten. Bei vor­zugsweise pflanzlicher Nahrung ist die Senkungskraft der Blutkörperchen viel geringer. Es wird dem Menschen mög­lich, das Blut nicht bis zur dunkelsten Färbung kommen zu lassen.",
      "Dadurch aber ist er gerade imstande, vom Ich aus den Zusammenhang seiner Gedanken zu beherrschen, wäh­rend schweres Blut ein Ausdruck dafür ist, daß er sklavisch hingegeben ist an das, was seinem astralischen Leibe durch die Tiernahrung eingegliedert ist. Dieses Bild zeigt uns durchaus als äußeren Wahrheitsausdruck, was wir sagen wollten.",
      "Der Mensch wird durch das Verhältnis zur Pflan­zenwelt innerlich kräftiger. Durch Fleischnahrung gliedert er sich etwas ein, was nach und nach zu wirklichen Fremd-stoffen wird, die eigene Wege gehen in ihm.",
      "Das wird ver­mieden, wenn die Nahrung vorzugsweise aus Pflanzen besteht. Wenn die Stoffe in uns eigene Wege gehen, so üben sie gerade Kräfte aus, die hysterische, epileptische Zustände hervorrufen. Weil das Nervensystem diese Imprägnierun­gen von außen erhält, verfällt es den verschiedenartigen Nervenkrankheiten.",
      "So sehen wir, wie in gewisser Bezie­hung «der Mensch ist, was er ißt».",
      "In Einzelheiten wäre noch viel mehr nachweisbar, aber durch zwei Beispiele kommen wir darauf, daß man nicht einseitig sein darf. Ein einseitiger Vegetarier könnte sagen:",
      "«Wir dürfen nicht Milch, Butter und Käse genießen.» Aber die Milch ist ein Produkt, an dem im Tiere bei der Erzeu­gung vorzugsweise der Ätherleib beteiligt ist. Der Astral­leib ist zum geringsten Teile daran beteiligt. Der Mensch kann ja in den ersten Zeiten seines Lebens als Säugling nur von Milch leben. Da ist alles darinnen, was er braucht. Bei der Bereitung der Milch kommt der astralische Leib nur in seiner Grenze in Betracht. Wenn man in höherem Alter hauptsächlich Milch, womöglich ausschließlich Milch ge­nießt, so erzielt man damit eine ganz besondere Wirkung. Weil der Mensch dann nichts aufnimmt, was schon äußer­lich bearbeitet ist und was seinen Astralleib beeinflussen kann, und weil er auf der anderen Seite in der Milch etwas aufnimmt, was schon vorbereitet ist, so ist er imstande, be­sondere Kräfte seines Ätherleibes, die heilende Wirkungen auf die Mitmenschen ausüben können, in sich zu entwickeln. Heiler, die heilend auf ihre Mitmenschen einwirken wollen, haben ein besonderes Hilfsmittel in ausschließlichem Milch-genuß.",
      "Auf der anderen Seite wollen wir den Einfluß eines Ge­nußmittels schildern, das aus der Pflanzenwelt genommen wird, den Einfluß des Alkohols. Dieser hat eine ganz be­sondere Bedeutung. Er entsteht erst dann, wenn der eigent­liche pflanzliche Prozeß, das, was durch die wunderbare Einwirkung des Lichtes geschieht, wovon der astralische Leib das Gegenteil ist, aufgehört hat. Dann beginnt ein Prozeß, der sich auf einer niederen Stufe abspielt und den Menschen noch mehr beeinträchtigt als tierische Nahrung. Der Mensch bringt die Stoffe bis zum astralischen Leibe heran, bringt sie durch den Astralleib in ein besonderes Gefüge. Wenn aber das, was an den Astralleib herange­bracht werden soll, in der Weise zerfällt, wie es beim Al­kohol der Fall ist, so geschieht das, was sonst durch den",
      "Astralleib geschehen soll, ohne den Astralleib, nämlich die Wirkung auf das Ich und das Blut. Die Wirkung des Alko­hols ist die, daß das, was sonst aus freiem Entschluß des Ichs geschehen soll, durch den Alkohol geschieht. In ge­wisser Beziehung ist es richtig, daß ein Mensch, der Alkohol genießt, weniger Nahrung nötig hat. Er läßt sein Blut durchziehen von den Kräften des Alkohols; er gibt dem Fremden ab, was er selbst tun sollte. Man kann in gewisser Weise sagen, daß in einem solchen Menschen der Alkohol denkt und fühlt und empfindet. Dadurch, daß der Mensch das, was seinem Ich unterworfen sein soll, an den Alkohol abliefert, stellt sich der Mensch unter den Zwang eines Äußeren. Er verschafif sich ein materielles Ich. Der Mensch kann sagen: Ich fühle dadurch gerade eine Belebung des Ichs. - Gewiß, aber nicht er ist es, sondern etwas anderes, unter das er sein Ich gebannt hat. So könnten wir noch durch mancherlei zeigen, wie der Mensch dazu kommen kann, immer mehr und mehr zu sein, was er ißt. Aber die Geisteswissenschaft zeigt uns auch, wie der Mensch freiwer­den kann von den Kräften der Nahrung.",
      "So wollte ich Ihnen heute nur in großen Zügen des Men­schen Verhältnis zu seiner Umgebung schildern, wie er da-steht in bezug auf die Nahrung zu den ihn umgebenden Reichen. Wer weiterhin diesen oder jenen Vortrag hier besuchen wird, der wird sehen, daß auf einzelne Fragen auch bei anderen Gelegenheiten eingegangen werden kann. Auch dieser Vortrag wird Ihnen gezeigt haben, daß die Geisteswissenschaft etwas ist, das auch auf die allermate­riellsten Bedürfnisse des Lebens seine Wirkung hat. Geistes­wissenschaft ist etwas, was ein Ideal sein kann für die Menschenzukunft. Heute wird man wohl noch oft sagen, wenn man sieht, wie die Stoffe sich im Menschen verbinden und trennen: Es ist wie in einer Retorte, und man wird",
      "glauben, daß man darin etwas Heilsames finden kann für die Menschen. Aber eine Zeit wird kommen, wo das, was über das Licht und den Astralleib gesagt ist, auch dem vor Augen stehen wird, der im Laboratorium forscht. Kann denn nicht auch jemand die gewöhnlichen Beobachtungen chemischer Art machen, wenn er sich sagt, daß hier ins Kleinste herein das Größte wirkt, was das äußere physische Sonnenlicht durchzieht, und was bis ins Geistige hinein im menschlichen Bewußtsein leuchtet? So wird man diese Dinge durchforschen in dem Lichte, das uns einen Überblick gibt über das Ganze.",
      "Aus dem Geiste ist alles geboren, was in unserer Um­gebung ist. Der Geist ist der Urgrund zu allem. Wollen wir zur Wahrheit kommen, so muß der Geist auch beim For­schen hinter uns stehen. Dann werden wir die Wahrheit erkennen, die dem Menschen im Großen und auch im Klei­nen nötig ist."
    ],
    "sentences": [
      [
        "ERNÄHRUNGSFRAGEN IM LICHTE DER"
      ],
      [
        "GEISTESWISSENSCHAFT"
      ],
      [
        "Berlin, 17.",
        "Dezember 1908"
      ],
      [
        "Es erscheint manchem sonderbar, wenn die Geisteswissen­schaft spricht über dasjenige, was mit einem gewissen Recht als das Materiellste, als das Ungeistigste von vielen ange­sehen wird: über die Ernährung.",
        "Es gibtMenschen, die ihren besonderen Idealismus, ja ihre besondere Geistigkeit da­durch andeuten wollen, daß sie sagen: Ach, wir kümmern uns nur um dasjenige, was erhaben ist über die Fragen, die mit dem materiellenLeben zusammenhängen.- Solche Men­schen glauben dann auch - und in gewisser Beziehung mögen sie recht haben -, daß es im Grunde genommen für die Ent­wickelung im Idealen und Spirituellen gleichgültig sei, wie der Mensch seine Bedürfnisse in bezug auf das Leibliche be­friedigt.",
        "Anders urteilt die materialistische Denkweise.",
        "Ein großer Philosoph des neunzehnten Jahrhunderts hat einen Ausspruch getan, der viel wiederholt worden ist und der bei vielen Menschen, die geistig idealistisch gesinnt sind, Schauer und Entsetzen hervorruft, den Ausspruch, den Feuerbach getan hat: «Der Mensch ist, was er ißt.» Die meisten Menschen fassen das so auf - und der materialisti­sche Sinn wird durchaus damit einverstanden sein -, der Mensch sei eine Zusammenfassung der Materien, die er sei­nem Leibe zuführt, und dadurch entstehe nicht nur das Wechselspiel seines organischen Lebens, sondern auch das­jenige, was in seinem Geiste sich darbietet."
      ],
      [
        "Wenn Außenstehende manchmal dieses oder jenes mehr"
      ],
      [
        "oder weniger oberflächlich hören über Anthroposophie oder Geisteswissenschaft, so glauben sie, daß sich die Anhänger viel zu viel mit Essen, mit Ernährung beschäftigen.",
        "Ein Außenstehender kann es nicht begreifen, warum die An­throposophen gar so viel darauf halten, ob einer dies oder jenes ißt.",
        "Es soll nicht geleugnet werden, daß in manchen anthroposophischen Kreisen, bei denen, die auf leichte Weise so recht tief in das geistige Leben hineinwollen, recht viel Unklarheit herrscht.",
        "Glaubt doch mancher, daß er nur das oder das meiden solle, nicht essen oder trinken solle, um allein dadurch zu gewissen höheren Stufen der Erkennt­nis hinaufzukommen!",
        "Das ist ebenso ein Irrtum, wie jene eben charakterisierte Auffassung des Ausspruches von Feuerbach: «Der Mensch ist, was er ißt.» Zum mindesten ist es eine einseitige Auffassung."
      ],
      [
        "Aber in gewisser Weise kann gerade die Geisteswissen­schaft diesen Satz für sich in Anspruch nehmen, nur in einer etwas anderen Art, als es von den Materialisten gemeint ist, und zwar in einer zweifach anderen Art.",
        "Zunächst haben wir ja schon öfters betont, daß für die Geisteswissen­schaft alles um uns herum der Ausdruck eines Geistigen ist.",
        "Ein Mineral, eine Pflanze oder irgend etwas in unserer Umgebung ist nur seiner Außenseite nach stofflich.",
        "Wie das Glied eines Menschen ist es der Ausdruck, die Geste des Geistes.",
        "Hinter allem Materiellen ist Geistiges, auch hinter der Nahrung.",
        "Mit ihr nehmen wir nicht nur das auf, was materiell vor unseren Augen sich ausbreitet, sondern wir essen mit das, was Geistiges dahinter ist.",
        "Wir treten durch die Ernährung durch dieses oder jenes materielle Substrat in Beziehung zu diesem oder jenem Geistigen, das dahinter­steckt.",
        "Das ist eine ganz oberflächliche Charakteristik.",
        "Aber schon wer dieses erfaßt, wird in gewisser Beziehung den materialistischen Satz zugeben können: Der Mensch ist,"
      ],
      [
        "was er ißt.",
        "Nur muß zugleich mit dem materiellen Prozeß ein geistiger verstanden werden."
      ],
      [
        "Das ist aber nur die eine Art, wie wir uns über diese Fragen im geisteswissenschaftlichen Sinne orientieren kön­nen.",
        "Wenn die Geisteswissenschaft einen gewissen Wert legt und Nachforschungen anstellt auf und über die Natur der Nahrungsmittel, so geschieht das, weil sich hier eine ganz eigenartige Perspektive in bezug auf die Beziehung des Menschen zur Natur herausstellt.",
        "Der Mensch steht aller­dings dadurch in einer Beziehung zur Natur, daß er die umgebende Natur in gewisser Weise aufnimmt, sich zu­sammensetzt mit dem, was darinnen ist.",
        "Und es entsteht die Frage: Wird der Mensch nicht dadurch, daß er so sich aneignet, was draußen ist, hingegeben an diese Kräfte, die draußen wirken, und kann er sich freimachen von diesen Kräften?",
        "Gibt es eine Möglichkeit, daß der Mensch frei wird von dieser seiner Umgebung durch seine Nahrung, so daß er eine gewisse Macht und einen gewissen Einfluß er­hält über die Umgebung?",
        "Könnte es nicht so sein, daß der Mensch in der Tat das sein könnte, was er ißt, durch eine gewisse Art der Ernährung - und könnte es nicht so sein, daß durch eine andere Art der Ernährung der Mensch sich frei macht von dem Zwange, der durch die Ernährung auf ihn ausgeübt wird?",
        "Also entsteht für die Geisteswissen­schaft die Frage: Wie muß die Ernährung des Menschen gestaltet sein, damit er frei wird von dem Zwange der Ernährung, damit er immer mehr Herr und Gebieter über das wird, was in ihm vorgeht?"
      ],
      [
        "Indem wir diese Frage heute vor uns hinstellen, muß einiges über die ganze Stellung der Geisteswissenschaft zu diesen Fragen gesagt werden.",
        "Diese Frage, auch die über Gesundheitsfragen, muß so aufgefaßt werden, daß der Geisteswissenschaft in keiner Weise eine Agitation nach"
      ],
      [
        "dieser oder jener Richtung zugeschrieben wird.",
        "Wer etwa glaubt, daß mit dem, was heute gesagt werden soll, agitiert wird für oder gegen diese oder jene Nahrung oder Genuß­mittel, der hat eine im höchsten Grade irrige Ansicht.",
        "Kei­ner sollte heute mit der Ansicht von hier fortgehen, daß hier eingetreten würde für oder gegen Abstinenz, Vege­tarismus, Fleischkost.",
        "Alle diese Fragen über Dogmen, über etwas Alleinseligmachendes, haben mit dem innersten Ge­fühlsnerv der Geisteswissenschaft gar nichts zu tun.",
        "Wir wollen nicht agitieren, nicht den Menschen nach dieser oder jener Weise kommandieren; wir wollen nur sagen, wie die Dinge wirklich sind.",
        "Dann mag sich jeder sein Leben ein­richten, wie er will, nach diesen großen Gesetzen des Da­seins.",
        "Also der heutige Vortrag will einzig und allein sagen, was auf diesem Gebiete wirklich ist.",
        "Auf der anderen Seite bitte ich sehr, zu berücksichtigen, daß ich nicht für anthro­posophische Kreise im engeren Sinne spreche, die eine ge­wisse Entwickelung durchmachen wollen und spezielle Be­dingungen einzuhalten haben.",
        "Heute wird die Frage im allgemeinmenschlichen Sinne erörtert werden.",
        "Bei dem gro­ßen Umfange des Themas wird nur einzelnes heraus-genommen werden können, und vor allem muß alles das vermieden werden, was mit dem Gesundheitlichen des Lebens zusammenhängt.",
        "Das werden wir in dem nächsten Vortrag hören."
      ],
      [
        "Wir werden uns heute mit der Ernährung im engeren Sinne befassen.",
        "Deshalb wird der Atmungsprozeß hier nicht berücksichtigt werden.",
        "Der Mensch hat, um den Lebensprozeß seines Organismus zu unterhalten, aufzunehmen:"
      ],
      [
        "Eiweiß, Kohlehydrate, Fette und Salze.",
        "Sie wissen, daß der Mensch die Bedürfnisse, die sein Organismus nach dieser Richtung hat, durch die sogenannte gemischte Kost befrie­digt.",
        "Er übernimmt diese Hauptbestandteile seiner Ernäh­rung"
      ],
      [
        "zum Teil aus dem tierischen, zum Teil aus dem pflanz­lichen Reiche.",
        "Es gibt unter unseren heutigen Zeitgenossen viel mehr Verteidiger einer gemischten Nahrung als einer einseitigen Kost, sagen wir etwa einer nur tierischen oder nur pflanzlichen Kost.",
        "Wir müssen uns fragen: Wie stellt sich dasjenige, was die Gesetze unserer Umgebung sind, aus denen der Mensch seine Nahrung nimmt, zu den wahren Kräften und Bedürfnissen des menschlichen Organismus?",
        "Heute ist hier nur vom Menschen die Rede, nicht von den Tieren."
      ],
      [
        "Der Mensch ist leicht geneigt, nach den sogenannten wissenschaftlichen Resultaten seiner Zeit seinen Organismus recht materiell aufzufassen.",
        "Die Geisteswissenschaft muß das ersetzen durch die Gesetze der geistigen Zusammen­hänge.",
        "Wenn auch theoretisch nicht immer, so liegt doch praktisch dem Verfahren, das eingeschlagen wird, mehr oder weniger unbewußt der Gedanke zugrunde, daß der menschliche Organismus mehr oder weniger nur aus dem physischen Leib, den chemischen Stoffen in ihrer Wechsel­wirkung aufeinander bestehe.",
        "Man verfolgt diese Substan­zen bis in ihre chemischen Elemente hinein und versucht, nachdem man erkannt hat, wie diese Substanzen wirken, sich ein Bild davon zu machen, wie sie chemisch weiter-wirken könnten in der großen Retorte, als die man den Menschen ansieht.",
        "Es soll nicht behauptet werden, daß nicht etwa viele schon hinaus wären über die Ansicht, der Mensch sei nur eine große Retorte.",
        "Es kommt nicht auf die Theorien an, sondern auf die Denkgewohnheiten.",
        "Dem wahren Prak­tiker kommt es nicht darauf an, was einer denkt, sondern was für Wirkungen seine Gedanken haben.",
        "Darauf kommt es an.",
        "Ob einer Idealist ist oder nicht, darauf kommt es nicht an, sondern für das Leben ist es wichtig, ob einer fruchtbare Gedanken hat, die so sind, daß das Leben gedeiht"
      ],
      [
        "und fortschreitet.",
        "Gerade das darf nicht außer acht gelassen werden, daß Geisteswissenschaft auch nach dieser Richtung hin nichts zu tun hat mit einem Dogma, mit irgendeinem Glauben.",
        "Mag einer noch so sehr die spirituell­sten Theorien vertreten: darauf kommt es nicht an, son­dern darauf, daß diese Gedanken fruchtbar sind, wenn er sie ins Leben überführt.",
        "Wenn also einer sagt, er sei nicht Materialist, er glaube an die Lebenskraft, ja sogar an einen Geist, aber in der Ernährungsfrage immer so vorgeht, als ob der Mensch eine große Retorte wäre, so kann seine Weltanschauung nicht fruchtbar werden.",
        "Nur dann hat Geisteswissenschaft über diese konkreten Fragen etwas zu sagen, wenn sie selbst in das einzelne hineinzuleuchten ver­mag, und das kann sie sowohl in bezug auf die Ernährungs­wie auch in bezug auf die Gesundheitsfragen."
      ],
      [
        "Wir müssen uns wieder über die vielgliedrige menschliche Wesenheit klarwerden.",
        "Für den Geistesforscher ist der Mensch nicht nur das physische Wesen, das man mit Augen sehen, mit Händen greifen kann, sondern dieser physische Leib ist nur ein Teil der menschlichen Wesenheit.",
        "Dieser physische Leib besteht allerdings aus denselben chemischen Stoffen, die in der Natur ausgebreitet sind.",
        "Aber die menschliche Natur hat höhere Glieder.",
        "Schon der nächste Teil der menschlichen Wesenheit ist übersinnlich, hat eine höhere Realität als der physische Leib.",
        "Er liegt dem physi­schen Leib zugrunde, er ist durch das ganze Leben hindurch ein Kämpfer gegen den Zerfall des physischen Leibes.",
        "In dem Augenblick, wo der Mensch durch die Pforte des Todes schreitet, ist der physische Leib nur seinen eigenen Gesetzen unterworfen und zerfällt.",
        "Im Leben kämpft der Lebensleib gegen den Zerfall.",
        "Er gibt den Stoffen und Kräften andere Richtungen, andere Zusammenhänge als sie haben würden, wenn sie nur sich selber folgten.",
        "Für das hellseherische Bewußtsein"
      ],
      [
        "ist dieser Leib ebenso sichtbar wie der physische Leib für das Auge.",
        "Diesen Lebensleib oder Atherleib hat der Mensch mit der Pflanze gemeinsam."
      ],
      [
        "Wir wissen aus anderen Vorträgen, daß der Mensch noch ein drittes Glied seiner Wesenheit hat, den astralischen Leib.",
        "Wie ist er?",
        "Er ist der Träger von Lust und Leid, Be­gierden, Trieben und Leidenschaften, von alledem, was wir unser inneres Seelenleben nennen.",
        "Alles das hat seinen Sitz im astralischen Leib.",
        "Er ist geistig wahrnehmbar, wie der physische Leib für das physische Bewußtsein.",
        "Diesen astra­lischen Leib hat der Mensch mit den Tieren gemeinsam."
      ],
      [
        "Das vierte Glied ist der Träger des Ichs, des Selbst­bewußtseins.",
        "Dadurch ist der Mensch die Krone der Schöp­fung, dadurch ragt er hinaus über die Dinge der Erde, die ihn umgeben.",
        "So steht der Mensch vor uns mit drei unsicht­baren Gliedern und einem sichtbaren Glied.",
        "Diese wirken immer durcheinander und miteinander.",
        "Alle wirken auf jedes einzelne und jedes einzelne wirkt auf alle andern.",
        "So kommt es, daß der physische Leib - ich sage noch einmal in Parenthese, daß das alles nur für den Menschen gilt -, so wie er vor uns steht, ein Ausdruck ist in allen seinen Teilen auch von den unsichtbaren Gliedern der menschlichen Na­tur.",
        "Dieser physische Leib könnte in sich nicht die Glieder haben, die der Nahrung, der Fortpflanzung, die dem Leben überhaupt dienen, wenn er nicht den Atherleib hätte.",
        "Alle Organe, die zur Ernährung und Fortpflanzung dienen, die Drüsen und so weiter, sind der äußere Ausdruck des Äther-leibes.",
        "Sie sind das, was der Atherleib am physischen Leibe baut.",
        "Unter anderem ist im physischen Leibe das Nerven­system der Ausdruck des astralischen Leibes.",
        "Hier ist der astralische Leib der Akteur, der Aufbauer.",
        "Wir können uns vorstellen, gerade wie eine Uhr oder eine Maschine von einem Uhrmacher oder von einem Maschinenbauer aufgebaut"
      ],
      [
        "sind, so sind es die Nerven von dem astralischen Leibe.",
        "Und die Eigenart der menschlichen Blutzirkulation, der Bluttätigkeit, sie ist der äußere physische Ausdruck des Ich-Trägers, des Trägers des Selbstbewußtseins.",
        "So ist auch der menschliche physische Leib in gewisser Weise vierglied­rig.",
        "Er ist ein Ausdruck der physischen Glieder, also seiner selbst, und der drei höheren, unsichtbaren Glieder.",
        "Rein physisch sind die Sinnesorgane; die Drüsen sind der Aus­druck für den Ätherleib, das Nervensystem für den astra­lischen Leib und das Blut für das Ich."
      ],
      [
        "Sehen wir den Menschen im Gegensatz zur Pflanze an, so steht die Pflanze als zweigliedrige Wesenheit vor uns.",
        "Die Pflanze hat einen physischen Leib und einen Ätherleib.",
        "Wir vergleichen nun den Menschen mit der Pflanze, indem wir allseitig vorgehen und das Innere, Geistige berücksichtigen.",
        "Wir setzen in Beziehung den menschlichen viergliedrigen Organismus mit dem zweigliedrigen Organismus der Pflan­zen.",
        "Zum Unterstützen können wir ausgehen von physi­schen, bekannten Tatsachen.",
        "Wir können darauf hinweisen, wie die Pflanze ihren Organismus aufbaut.",
        "Sie setzt un­organische Stoffe zusammen zu ihrem Körper.",
        "Sie hat die Kraft, aus einzelnen unlebendigen Bestandteilen ihren Leib in der wunderbarsten Weise zusammenzugliedern.",
        "Wir brauchen ja nur einmal zu sehen, wie die Pflanze in merk­würdiger Wechselwirkung steht zum Atmungsprozeß.",
        "Der Mensch atmet Sauerstoff ein und gibt Kohlensäure von sich.",
        "Diese, die für den Menschen unbrauchbar ist, kann die Pflanze aufnehmen.",
        "Sie behält den Kohlenstoff zurück zum Aufbau ihres Organismus und gibt den Sauerstoff zum größten Teil wieder zurück.",
        "Aber sie braucht etwas dazu, was von vielen vielleicht nicht als etwas Besonderes auf­gefaßt wird: sie braucht das Sonnenlicht.",
        "Ohne das Sonnen­licht könnte sie nicht ihren Organismus aufbauen."
      ],
      [
        "Licht, das zu unserem Entzücken zu uns strömt, das uns auch seelisch so beleben kann, ist zugleich der großartige Helfer zum Aufbau des pflanzlichen Organismus.",
        "Wir sehen, wie da ein Wunderwerk vor sich geht, wie das Sonnenlicht hilft, ein organisches Wesen aufzubauen.",
        "Was unsere Augen erst wirksam macht, das ist es, was der Pflanze im Aufbau hilft."
      ],
      [
        "Der Mensch hat außer dem physischen und dem Äther-leibe noch den astralischen Leib.",
        "Den hat die Pflanze nicht.",
        "Das, was dem Sonnenlichte hilft, die Pflanzen in so wun­derbarer Weise aufzubauen, das ist der Ätherleib.",
        "Dieser ist auf der einen Seite den Stoffen zugewandt.",
        "Der Mensch könnte seinen physischen Organismus nicht entwickeln, wenn er nicht etwas täte, was in gewisser Weise entgegen­gesetzt ist dem, was die Pflanze tut.",
        "Schon in dem Atmungs­prozeß tut der Mensch etwas Gegensätzliches.",
        "Der Mensch macht hier schon den gegenteiligen Prozeß durch.",
        "Dasselbe können wir sagen in bezug auf alle Ernährung des Men­schen.",
        "Wir können sagen: Die Ernährung muß so vor sich gehen, daß alles, was in der Pflanze aufgebaut wird, im Menschen wieder abgebaut wird.",
        "Der Prozeß im Menschen ist ein sehr eigentümlicher.",
        "Wenn nur der Ätherleib einen physischen Leib aufbaute, so würde niemals Bewußtsein, Seelenempfindung auftreten.",
        "Es muß innerlich immer wie­der zerstört, abgebaut werden, was der Ätherleib aufgebaut hat.",
        "So ist zwar der Ätherleib ein Kämpfer gegen den Zer­fall, aber trotzdem tritt immer ein stückweiser Zerfall ein.",
        "Und dasjenige, was diesen Zerfall bewirkt, was immer den Menschen hindert, Pflanze zu sein, das ist der astralische Leib."
      ],
      [
        "Das Sonnenlicht und der menschliche astralische Leib sind in gewisser Weise zwei entgegengesetzte Dinge.",
        "Für den, der mit hellseherischem Bewußtsein des Menschen"
      ],
      [
        "astralischen Leib kennenlernt, für den ist der astralische Leib ein inneres Licht, das geistiger Art ist, für das äußere Auge unsichtbar.",
        "Ein geistiger Lichtleib ist dieser astralische Leib.",
        "Er ist der Gegensatz zu dem äußeren, äußerlich leuch­tenden Licht.",
        "Denken Sie sich einmal das Sonnenlicht immer schwächer werdend, bis es erlischt, und lassen Sie es jetzt noch weiter nach der anderen Seite gehen, lassen Sie es negativ werden, so haben Sie inneres Licht.",
        "Und dieses in­nere Licht hat die entgegengesetzte Aufgabe als das äußere Licht, das aus anorganischen Stoffen den pflanzlichen Leib aufbauen soll.",
        "Das innere Licht, das die partielle Zerstörung einleitet, durch die allein Bewußtsein möglich ist, bringt den Menschen zu einer höheren Stufe, als die Pflanze sie einnimmt, dadurch, daß der Prozeß der Pflanzen in einen entgegengesetzten verwandelt wird.",
        "So steht der Mensch durch sein inneres Licht in einem gewissen Gegensatz zur Pflanze.",
        "Das ist die Sache geistig aufgefaßt, und wir wür­den bei weiterer Betrachtung sehen, wie die durch den astralischen Leib bewirkte Zerstörung durch das Ich weiter fortgesetzt wird.",
        "Aber das braucht uns heute nicht weiter zu beschäftigen."
      ],
      [
        "Nehmen wir jetzt das Verhältnis des Menschen zur Pflanze, wenn es so real wird, daß der Mensch seine Nah­rungsstoffe aus der Pflanze aufnimmt.",
        "Er bildet in sich selber für den ganzen Weltprozeß eine Fortsetzung der Pflanze.",
        "Was durch das Sonnenlicht aufgebaut wird, das zerstört der astralische Leib zwar immer wieder, aber er gliedert dadurch dem Menschen das Nervensystem ein und erhebt dadurch das Leben zu einem bewußten.",
        "So ist der astralische Leib dadurch, daß er ein negativer Lichtleib ist, der andere Pol, der dem pflanzlichen entgegengesetzt ist.",
        "Diesem Prozeß des Aufbauens des Pflanzenorganismus liegt ein Geistiges zugrunde, denn die Geisteswissenschaft zeigt"
      ],
      [
        "uns immer mehr, wie das, was uns als Licht erscheint, auch nur der äußere Ausdruck eines Geistigen ist.",
        "Durch das Licht fließt uns fortwährend Geistiges zu, das Licht der Geister fließt uns zu.",
        "Was sich hinter diesem physischen Licht verbirgt, das ist es, was in Teile zerteilt auch im astra­lischen Leibe erscheint.",
        "Äußerlich im Sonnenlichte erscheint es in seiner physischen Form, im astralischen Leibe in astra­lischer Weise.",
        "Das Geistige des Lichtes arbeitet in uns inner­lich am Aufbau unseres Nervensystems.",
        "So wunderbar wir­ken zusammen das pflanzliche und das menschliche Leben."
      ],
      [
        "Nehmen wir nun an, der Mensch tritt durch die Nahrung in ein Verhäknis mit der tierischen Welt.",
        "Dann ist die Sache anders.",
        "In dem Wesen, dem er dann seine Nahrungsmittel entnimmt, ist in gewisser Weise der Prozeß schon voll­zogen.",
        "Was er sonst jungfräulich und frisch von der Pflanze entnimmt, das ist im Tiere schon teilweise umgewandelt, schon vorbereitet.",
        "Denn auch das Tier gliedert sich schon einen astralischen Leib und ein Nervensystem ein.",
        "So nimmt der Mensch dann etwas auf, was ihm nicht jungfräulich ent­gegentritt, sondern was den Prozeß schon durchgemacht hat, was schon astralische Kräfte aufgenommen hat.",
        "Was im Tiere lebt, das hat schon in sich entwickelte Kräfte des Astralischen.",
        "Nun könnte man glauben, daß dadurch dem Menschen Arbeit erspart würde.",
        "Dieser Gedanke ist aber nicht ganz richtig.",
        "Denken Sie sich einmal folgendes: Ich mache aus verschiedenen Gerätschaften ein Haus.",
        "Ich nehme die ursprünglichen Gerätschaften.",
        "Da kann ich das Haus ganz nach meinen ursprünglichen Intentionen aufbauen.",
        "Nehmen wir aber an, drei oder vier andere Personen haben schon daran stückweise gearbeitet und nun soll ich daraus ein Ganzes machen.",
        "Wird mir das die Arbeit erleichtern?",
        "Nein, ganz gewiß nicht.",
        "Sie werden in einer weitverbreite­ten Literatur lesen, daß dem Menschen dadurch eben die"
      ],
      [
        "Arbeit erleichtert würde, daß er etwas aufnimmt, an dem schon vorgearbeitet ist.",
        "Aber der Mensch wird gerade da­durch ein beweglicheres, selbständigeres Wesen, daß er das Ursprüngliche aufnimmt."
      ],
      [
        "Noch ein Bild: Jemand hat eine Waage mit zwei Waag­schalen.",
        "Gleiche Gewichte halten sich das Gleichgewicht.",
        "Auf beiden Seiten mögen fünfzig Pfund liegen.",
        "Aber so ist es nicht immer.",
        "Ich kann eine Waage nehmen, auf der das Gewicht zu verschieben ist.",
        "Wir haben dann in doppelt so großer Entfernung nur halb so großes Gewicht nötig.",
        "Hier wird das Gewicht durch die Entfernung bestimmt.",
        "Ebenso kommt es nicht nur auf die Menge der Kräfte an, sondern besonders auf die Feinheit der Stoffe.",
        "Das Tier verarbeitet die Stoffe in unvollkommenerem Sinne.",
        "Was da aufgenom­men wird vom Menschen, wirkt fort durch das, was durch den Astralleib des Tieres daran geschehen ist, und das hat der Mensch dann erst zu überwinden.",
        "Aber weil ein Astral-leib so gewirkt hat, daß in einem bewußten Wesen bereits ein Prozeß sich abgespielt hat, so bekommt der Mensch etwas in seinen Organismus hinein, was auf sein Nerven­system einwirkt."
      ],
      [
        "Das ist der Grundunterschied zwischen Nahrung aus dem Pflanzenreich und Nahrung aus dem Tierreich.",
        "Nahrung aus dem Tierreich wirkt in ganz spezifischer Weise auf das Nervensystem und damit auf den Astralleib.",
        "Aber bei pflanzlicher Nahrung bleibt das Nervensystem unberührt durch etwas Äußeres.",
        "Der Mensch muß sich dann allerdings auch alles selber verdanken in bezug auf das Nervensystem.",
        "Dadurch aber durchströmen die Wirkungen seiner Nerven nicht fremde Produkte, sondern nur das, was in ihm selbst urständet.",
        "Wer weiß, wie viel im menschlichen Organismus vom Nervensystem abhängt, der wird verstehen, was das heißt.",
        "Wenn der Mensch sein Nervensystem selbst aufbaut,"
      ],
      [
        "so ist es voll empfänglich für das, was der Mensch ihm zu­muten soll in bezug auf die geistige Welt.",
        "Seiner Nahrung aus der Pflanzenwelt verdankt der Mensch das, daß er hinaufblicken kann zu den großen Zusammenhängen der Dinge, die ihn erheben über die Vorurteile, die aus den engen Grenzen des persönlichen Seins entspringen.",
        "Überall, wo der Mensch frei und unbekümmert aus den großen Ge­sichtspunkten heraus Leben und Denken regelt, da ver­dankt er diesen raschen Überblick seiner Nahrungsbezie­hung zur Pflanzenwelt.",
        "Da, wo der Mensch durch Zorn, Antipathie, durch Vorurteile sich hinreißen läßt, da ver­dankt er das seiner Nahrung aus der Tierwelt."
      ],
      [
        "Es soll hier aber nicht agitiert werden für pflanzliche Nahrung.",
        "Im Gegenteil: Die tierische Nahrung war dem Menschen notwendig und ist vielfach noch heute notwendig, weil der Mensch auf der Erde fest sein sollte, ins Persönliche eingeklemmt sein sollte.",
        "Alles, was den Menschen zu sei­nen persönlichen Interessen gebracht hat, das hängt zusam­men mit der tierischen Nahrung.",
        "Daß es Menschen gegeben hat, die Kriege geführt haben, die Sympathie und Anti­pathie, sinnliche Leidenschaften zueinander hatten, das kommt her von der tierischen Nahrung.",
        "Daß aber der Mensch nicht in den engeren Interessen aufging, daß er all­gemeine Interessen fassen kann, das verdankt er seinen Beziehungen zur Pflanzenwelt in bezug auf die Nahrung.",
        "So gehen ja auch bei gewissen Völkern, die vorzugsweise pflanzliche Nahrung nehmen, die Anlagen mehr zum Spiri­tuellen, während andere Völker mehr Tapferkeit, Mut, Kühnheit entwickeln, die ja auch zum Leben nötig sind.",
        "Diese Dinge sind ohne persönliches Element nicht zu den­ken, und dieses ist nicht möglich ohne tierische Nahrung."
      ],
      [
        "Wir sprechen heute über diese Fragen von ganz allgemein menschlichem Standpunkte aus.",
        "Aber das macht uns klar,"
      ],
      [
        "daß der Mensch nach dieser oder jener Seite ausschlagen kann, sich also auch in seine persönlichen Interessen hinein­versenken kann durch die tierische Nahrung.",
        "Dadurch wird sein Sinn getrübt in bezug auf die große Überschau des Daseins.",
        "Man sieht meistens nicht, wie es in der Nahrung begründet ist, wenn der Mensch sagt: Nun weiß ich wieder nicht, wie soll ich dies oder das machen, wie hat er es ge­macht? - Diese Unmöglichkeit des Überschauens der Zu­sammenhänge kommt von der Nahrung her.",
        "Vergleichen Sie das mit einem, der große Zusammenhänge überschauen kann.",
        "Sie können dann auf die Nahrung dieser Menschen und vielleicht auch auf die Nahrung der Vorfahren zurück­blicken.",
        "Ganz anders ist ein Mensch, der schon in seiner Vorfahrenreihe ein jungfräuliches Nervensystem hat.",
        "Die­ser Mensch hat einen anderen Sinn für die großen Zusam­menhänge.",
        "Ein Leben kann da manchmal das gar nicht zerstören, was die Vorfahren begründet haben.",
        "Wenn da auch ein Mensch, der zum Beispiel von Bauern abstammt, doch das aufstachelt, was er in sich hat, so ist es eben nur durch das Fleisch herausgekommen, weil er empfindlicher war."
      ],
      [
        "Der Fortschritt wird darin bestehen, daß der Mensch, in­sofern der Eiweißbedarf nicht in ihm, in der menschlichen Natur selbst zubereitet ist, sich in der tierischen Nahrung beschränkt auf dasjenige, was noch nicht von Leidenschaf­ten durchglüht ist, wie Milch.",
        "Die Pflanzennahrung wird einen immer weiteren Raum einnehmen in der menschlichen Nahrung."
      ],
      [
        "In bezug auf einzelne Nahrungsmittel können wir ge­wisse Vorzüge der Pflanzenkost hervorheben.",
        "Wenn der Mensch sich sein Eiweiß aus der Pflanzenkost holt, wobei allerdings härtere Arbeit erforderlich ist, so entwickelt er Kräfte, die sein Nervensystem frischer machen.",
        "Vieles, dem"
      ],
      [
        "die Menschheit entgegengehen würde, wenn die Fleisch­nahrung überhand nähme, wird vermieden durch vorzugs-weises Berücksichtigen der Pflanzenkost.",
        "An der vegetari­schen und animalischen Nahrung können wir sehen, wie gegensätzlich sie wirken."
      ],
      [
        "Zur Illustration können wir fol­gendes sagen: Sehen wir uns den physischen Prozeß an unter dem Einfluß von Fleischnahrung.",
        "Die roten Blut­körperchen werden schwer, dunkler, das Blut hat eine größere Neigung zu gerinnen."
      ],
      [
        "Es bilden sich in leichterer Weise Einschläge von Salzen, von Phosphaten.",
        "Bei vor­zugsweise pflanzlicher Nahrung ist die Senkungskraft der Blutkörperchen viel geringer.",
        "Es wird dem Menschen mög­lich, das Blut nicht bis zur dunkelsten Färbung kommen zu lassen."
      ],
      [
        "Dadurch aber ist er gerade imstande, vom Ich aus den Zusammenhang seiner Gedanken zu beherrschen, wäh­rend schweres Blut ein Ausdruck dafür ist, daß er sklavisch hingegeben ist an das, was seinem astralischen Leibe durch die Tiernahrung eingegliedert ist.",
        "Dieses Bild zeigt uns durchaus als äußeren Wahrheitsausdruck, was wir sagen wollten."
      ],
      [
        "Der Mensch wird durch das Verhältnis zur Pflan­zenwelt innerlich kräftiger.",
        "Durch Fleischnahrung gliedert er sich etwas ein, was nach und nach zu wirklichen Fremd-stoffen wird, die eigene Wege gehen in ihm."
      ],
      [
        "Das wird ver­mieden, wenn die Nahrung vorzugsweise aus Pflanzen besteht.",
        "Wenn die Stoffe in uns eigene Wege gehen, so üben sie gerade Kräfte aus, die hysterische, epileptische Zustände hervorrufen.",
        "Weil das Nervensystem diese Imprägnierun­gen von außen erhält, verfällt es den verschiedenartigen Nervenkrankheiten."
      ],
      [
        "So sehen wir, wie in gewisser Bezie­hung «der Mensch ist, was er ißt»."
      ],
      [
        "In Einzelheiten wäre noch viel mehr nachweisbar, aber durch zwei Beispiele kommen wir darauf, daß man nicht einseitig sein darf.",
        "Ein einseitiger Vegetarier könnte sagen:"
      ],
      [
        "«Wir dürfen nicht Milch, Butter und Käse genießen.» Aber die Milch ist ein Produkt, an dem im Tiere bei der Erzeu­gung vorzugsweise der Ätherleib beteiligt ist.",
        "Der Astral­leib ist zum geringsten Teile daran beteiligt.",
        "Der Mensch kann ja in den ersten Zeiten seines Lebens als Säugling nur von Milch leben.",
        "Da ist alles darinnen, was er braucht.",
        "Bei der Bereitung der Milch kommt der astralische Leib nur in seiner Grenze in Betracht.",
        "Wenn man in höherem Alter hauptsächlich Milch, womöglich ausschließlich Milch ge­nießt, so erzielt man damit eine ganz besondere Wirkung.",
        "Weil der Mensch dann nichts aufnimmt, was schon äußer­lich bearbeitet ist und was seinen Astralleib beeinflussen kann, und weil er auf der anderen Seite in der Milch etwas aufnimmt, was schon vorbereitet ist, so ist er imstande, be­sondere Kräfte seines Ätherleibes, die heilende Wirkungen auf die Mitmenschen ausüben können, in sich zu entwickeln.",
        "Heiler, die heilend auf ihre Mitmenschen einwirken wollen, haben ein besonderes Hilfsmittel in ausschließlichem Milch-genuß."
      ],
      [
        "Auf der anderen Seite wollen wir den Einfluß eines Ge­nußmittels schildern, das aus der Pflanzenwelt genommen wird, den Einfluß des Alkohols.",
        "Dieser hat eine ganz be­sondere Bedeutung.",
        "Er entsteht erst dann, wenn der eigent­liche pflanzliche Prozeß, das, was durch die wunderbare Einwirkung des Lichtes geschieht, wovon der astralische Leib das Gegenteil ist, aufgehört hat.",
        "Dann beginnt ein Prozeß, der sich auf einer niederen Stufe abspielt und den Menschen noch mehr beeinträchtigt als tierische Nahrung.",
        "Der Mensch bringt die Stoffe bis zum astralischen Leibe heran, bringt sie durch den Astralleib in ein besonderes Gefüge.",
        "Wenn aber das, was an den Astralleib herange­bracht werden soll, in der Weise zerfällt, wie es beim Al­kohol der Fall ist, so geschieht das, was sonst durch den"
      ],
      [
        "Astralleib geschehen soll, ohne den Astralleib, nämlich die Wirkung auf das Ich und das Blut.",
        "Die Wirkung des Alko­hols ist die, daß das, was sonst aus freiem Entschluß des Ichs geschehen soll, durch den Alkohol geschieht.",
        "In ge­wisser Beziehung ist es richtig, daß ein Mensch, der Alkohol genießt, weniger Nahrung nötig hat.",
        "Er läßt sein Blut durchziehen von den Kräften des Alkohols; er gibt dem Fremden ab, was er selbst tun sollte.",
        "Man kann in gewisser Weise sagen, daß in einem solchen Menschen der Alkohol denkt und fühlt und empfindet.",
        "Dadurch, daß der Mensch das, was seinem Ich unterworfen sein soll, an den Alkohol abliefert, stellt sich der Mensch unter den Zwang eines Äußeren.",
        "Er verschafif sich ein materielles Ich.",
        "Der Mensch kann sagen: Ich fühle dadurch gerade eine Belebung des Ichs. - Gewiß, aber nicht er ist es, sondern etwas anderes, unter das er sein Ich gebannt hat.",
        "So könnten wir noch durch mancherlei zeigen, wie der Mensch dazu kommen kann, immer mehr und mehr zu sein, was er ißt.",
        "Aber die Geisteswissenschaft zeigt uns auch, wie der Mensch freiwer­den kann von den Kräften der Nahrung."
      ],
      [
        "So wollte ich Ihnen heute nur in großen Zügen des Men­schen Verhältnis zu seiner Umgebung schildern, wie er da-steht in bezug auf die Nahrung zu den ihn umgebenden Reichen.",
        "Wer weiterhin diesen oder jenen Vortrag hier besuchen wird, der wird sehen, daß auf einzelne Fragen auch bei anderen Gelegenheiten eingegangen werden kann.",
        "Auch dieser Vortrag wird Ihnen gezeigt haben, daß die Geisteswissenschaft etwas ist, das auch auf die allermate­riellsten Bedürfnisse des Lebens seine Wirkung hat.",
        "Geistes­wissenschaft ist etwas, was ein Ideal sein kann für die Menschenzukunft.",
        "Heute wird man wohl noch oft sagen, wenn man sieht, wie die Stoffe sich im Menschen verbinden und trennen: Es ist wie in einer Retorte, und man wird"
      ],
      [
        "glauben, daß man darin etwas Heilsames finden kann für die Menschen.",
        "Aber eine Zeit wird kommen, wo das, was über das Licht und den Astralleib gesagt ist, auch dem vor Augen stehen wird, der im Laboratorium forscht.",
        "Kann denn nicht auch jemand die gewöhnlichen Beobachtungen chemischer Art machen, wenn er sich sagt, daß hier ins Kleinste herein das Größte wirkt, was das äußere physische Sonnenlicht durchzieht, und was bis ins Geistige hinein im menschlichen Bewußtsein leuchtet?",
        "So wird man diese Dinge durchforschen in dem Lichte, das uns einen Überblick gibt über das Ganze."
      ],
      [
        "Aus dem Geiste ist alles geboren, was in unserer Um­gebung ist.",
        "Der Geist ist der Urgrund zu allem.",
        "Wollen wir zur Wahrheit kommen, so muß der Geist auch beim For­schen hinter uns stehen.",
        "Dann werden wir die Wahrheit erkennen, die dem Menschen im Großen und auch im Klei­nen nötig ist."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "GESUNDHEITSFRAGEN IM LICHTE DER GEISTE SWISSENSCHAFT Berlin, 14. Januar1909",
    "paragraphs": [
      "GESUNDHEITSFRAGEN IM LICHTE DER",
      "GEISTE SWISSENSCHAFT",
      "Berlin, 14. Januar1909",
      "Das Thema, das uns heute beschäftigen soll, schließt eine Anzahl von Fragen ein, die den Menschen mit Recht auf das allertiefste interessieren. Die Fragen nach der Gesund­heit sind ja solche, die zusammenhängen mit alledem, was den Menschen lebenstüchtig macht, mit alledem, was ihm verhilft, seine Bestimmung in der Welt ungehemmt zu er-füllen, und es ist deshalb die Gesundheit gewiß für die mei­sten Menschen, in dem richtigen Lichte gesehen, etwa so, daß sie sie sozusagen anstreben, wie man äußere Güter an­strebt. Aber die Gesundheit ist auch als ein inneres Gut zu betrachten, wie die äußeren Güter zunächst nicht um ihrer selbst willen von dem gesund denkenden Menschen ange­strebt werden, sondern als Mittel der Arbeit, als Mittel seines Wirkens und Schaffens. Daher können wir es wohl erklären, daß der Drang, die Sehnsucht, sich Aufklärung zu verschaffen über die Rätsel und Fragen des gesunden und kranken Lebens, insbesondere in unserer Gegenwart so tiefgehend sind. Allerdings ist im allgemeinen Denken jene Gesinnung wenig verbreitet, die geeignet ist, den Menschen empfänglich zu machen gerade für diejenigen Antworten, die man braucht, wenn man solche Fragen lösen will, welche so innig mit dem ganzen Wesen des Menschen zusammen­hängen.",
      "Es soll auch heute, wie schon einmal bei einer ähnlichen Gelegenheit, an einen alten Spruch erinnert werden, der",
      "manchem einfällt, wenn von Gesundheit und Krankheit gesprochen wird, an den Ausspruch: Es gibt so viele Krank­heiten und nur eine einzige Gesundheit! - Dieser Ausspruch erscheint im Grunde genommen manchen so selbstverständ­lich als möglich, und dennoch ist er ein Irrtum, ein Irrtum im eminenten Sinne des Wortes, denn es gibt nicht bloß eine Gesundheit, sondern so viele Gesundheiten, wie es Men­schen gibt. Das ist es gerade, was wir in unsere Gesinnung aufnehmen müssen, wenn wir die Fragen nach dem Gesun­den und Kranken im richtigen Lichte sehen wollen. Wir müssen in unsere Gesinnung aufnehmen, daß der Mensch ein individuelles Wesen ist, daß jeder Mensch anders be­schaffen ist als der andere, und daß, was dem einen heilsam und für den anderen schädlich und krankmachend sein kann, ganz abhängt von seiner individuellen Beschaffenheit.",
      "Daß diese Gesichtspunkte nicht so weitverbreitet sind, das zeigt eine Erfahrung, die jeder von uns alltäglich ma­chen kann. Da fehlt dem einen dies oder jenes. Die Mutter erfährt es oder sie nimmt es wahr; auch sie erinnert sich, daß ihr in ähnlichen Fällen dies oder jenes geholfen hat, also darauf los! Dann kommt der Vater, der sich erinnert, daß etwas anderes geholfen hat. Dann kommt die Tante, dann der Onkel, der sagt: In die frische Luft gehen. - Diese Anordnungen sind oft so widersprechend, daß sie gar nicht erfüllt werden können. Jeder hat sein Heilmittel, auf das er eingeschworen ist. Das muß dann losgelassen werden auf den armen Kranken. Wer hätte es nicht erfahren, daß diese sich überstürzenden guten Ratschläge eigentlich eine recht mißliche Sache sind, wenn dem Menschen dies oder jenes fehlt! Alle diese Dinge gehen hervor aus einer unrealisti­schen Denkweise, aus einer abstrakten Denkweise, aus einem Dogmatismus, der gar nicht beachtet, daß der Mensch ein individuelles Einzelwesen ist. Jeder Mensch ist ein Wesen",
      "für sich, und darauf kommt es vor allen Dingen an:",
      "diese Realität Mensch ins Auge zu fassen, wenn man es mit den Erscheinungen gesund und krank zu tun hat.",
      "Nun entspringt ja eine solche Hilfsbedürftigkeit, wie sie der Mensch in der Krankheit hat, gewiß einer Artung sei­nes inneren Wesens, die das Mitgefühl, das Mitleid seiner Umgebung wachrufen muß. Wir können begreifen, daß jeder gern helfend herbeispringen möchte, denn es ist dies nur ein Ausdruck dafür, welches tiefste Interesse gerade diese Fragen im Zusammenhange mit der ganzen Menschen-natur hervorrufen. Allerdings, wenn man auf der einen Seite dieses tiefe Interesse ins Auge faßt, auf der anderen Seite aber nur ein klein wenig hineinblickt in das, was in unserer Zeit an verschiedenen Anschauungen über Gesund­heit und Krankheit herrscht, dann kann man unter Um­ständen recht betrübt werden. Man könnte sagen, die Krankheit sei eine so wichtige Sache im Menschenleben und warum es denn geschehe, daß sich gelehrte und ungelehrte Leute, Mediziner und Laien, nicht nur über die Heilmittel für die einzelnen Krankheiten, nicht nur über die rechten Wege zur Gesundheit, sondern sogar über das Wesen des Krankseins in den mannigfaltigsten Theorien streiten. Es scheint manchmal, daß in unserer Zeit geistiger und wissen­schaftlicher Betriebsamkeit der kranke und vielleicht auch der gesunde Mensch mehr als je den Parteianschauungen ausgesetzt ist, die von allen Seiten sich geltend machen in bezug auf wichtige Fragen der Menschheitsentwickelung und des Menschheitswesens.",
      "Dürfen wir nun - diese Frage wollen wir uns heute stel­len - die Hoffnung hegen, daß die Geisteswissenschaft, die von den verschiedensten Seiten in diesen Vortragszyklen charakterisiert ist und noch charakterisiert werden wird, in gewisser Beziehung auch Licht bringen kann in die Theorien",
      "und Partei-Schattierungen, welche wir heute um uns herum erblicken, wenn wir die Ansichten über Gesundheit und Krankheit einmal an uns herantreten lassen? Es ist ja des öfteren hier betont worden, daß die Geisteswissenschaft einen höheren Gesichtspunkt anstrebt, der es möglich macht, dasjenige, was die Menschen in Parteiungen zerteilt, da­durch, daß sie nur gewisse engere Kreise des Anschauens und Beobachtens haben, zu überbrücken, zu zeigen, wie das eine dem anderen widerstrebt, weil es einseitig ist.",
      "Wir haben öfter gezeigt, daß die Geisteswissenschaft gerade da ist, um das Gute in den Einseitigkeiten zu suchen und die Harmonie unter den verschiedenen Einseitigkeiten herzu­stellen. Einseitigkeit - so muß sich derjenige sagen, der die Sache nicht nur oberflächlich betrachtet - dürfte es doch sein, was uns da entgegentritt, wenn von seiten dieser oder jener Krankheitslehre diese oder jene Dogmen mit einer anspruchsvollen Autorität gepredigt werden.",
      "Sie haben alle erfahren, welche Summen von Wortschattierungen einander gegenüberstehen in bezug auf diese Fragen. Jeder weiß, daß auf der einen Seite dasjenige steht, was man oftmals -heute sogar schon leider im verächtlichen Sinne - die Schul­medizin nennt mit ihrer allopathischen Richtung, und auf der andern Seite jene Richtung, die man als die homöopa­thische bezeichnet.",
      "Dann haben aber auch weite Kreise Zu­trauen gefunden zu dem, was man Naturheilkunde nennt, die vielfach eine andere Auffassung über Krankheit und Gesundheit hat und nicht nur das empfiehlt, was auf den kranken Menschen Bezug hat, sondern auch das, was als richtig gehalten wird für den gesunden Menschen, damit er sich stark und kräftig erhält. Alles ist gefärbt von dieser oder jener Seite, von der medizinischen oder von der mehr der Naturheilkunde zuneigenden Richtung.",
      "Wenn wir uns einmal vor Augen führen, von welchen",
      "Gesichtspunkten aus ein solcher Streit über Krankheit und Gesundheit zum Beispiel existiert zwischen den An­hängern der medizinischen Heilweise und den Anhängern der Naturheilkunde, dann hören wir die Anhänger der Naturheilkunde sagen, die Medizin suche für jede Krank­heit ihr bestimmtes Heilmittel und sei der Anschauung, daß die Krankheit etwas ist, was den Menschen wie etwas Äußerliches, wie durch eine äußerliche Ursache ergreift, und daß es für die Krankheit auch dieses oder jenes äußerliche Heilmittel gibt. Wir wollen bei solcher Charakteristik nicht vergessen, daß das, was da von der einen oder anderen Seite gesagt wird, oft über das Ziel hinausschießt, und wollen nicht vergessen, daß in vielen Dingen die beiden Parteien einander unrecht tun. Aber wir wollen einzelne Vorwürfe herausheben, die uns zur Verdeutlichung dienen können. Der Anhänger der Naturheilkunde wird hervor­heben, daß der Schulmediziner eine Entzündung in ge­wissen Fällen durch Eisumschläge lindere, daß man bei Gelenkrheumatismus durch Salizylsäure und so weiter zu helfen suche.",
      "Besonders weitgehende Anhänger der Naturheilkunde werden kräftige Vorwürfe erheben. Sie werden sagen: Wenn der Magen zuviel Magensäure absondert, dann werde der Mediziner versuchen, diese Magensäure zu neutralisieren. Der Naturheilkundige sagt, das gehe an dem tiefen Wesen der Krankheit und vor allem an dem tiefen Wesen des Menschen vorbei. Das alles treffe den Nagel nicht auf den Kopf. Nehmen wir an, der Magen sondert wirklich zuviel Magensäure ab, so sei das ein Beweis dafür, daß etwas im Organismus nicht richtig ist. Im richtig funktionierenden Organismus wird nicht zuviel Magensäure abgesondert. Wenn man daher die Magensäure, die abgesondert wird, neutralisiert, so hebt man damit noch nicht die Kraft auf,",
      "die Tendenz, zuviel Magensäure zu schaffen. Man müsse also seine Aufmerksamkeit nicht darauf richten, die Magen­säure einfach zu beseitigen.- Das sagen diejenigen, die gegen die Schulmedizin polemisieren. Man würde, wenn man die Magensäure beseitigt, den Organismus geradezu aufstacheln, ja recht viel Magensäure zu erzeugen. Man müsse also tiefer-gehen und die eigentliche Ursache aufsuchen. So insbeson­dere wird der Naturheilkundige, wenn er es bis zum Fana­tiker bringt , wettern: Wenn jemand an Schlaflosigkeit leidet, so hilft man ihm so, daß man ihm Schlafmittel gibt. Schlaf­mittel beseitigen die Schlaflosigkeit für eine gewisse Zeit; aber die Ursache wird nicht beseitigt. Die müsse aber besei­tigt werden, wenn man dem Kranken wirklich helfen will.",
      "Unter denjenigen, die wieder mehr auf dem Arznei-standpunkte stehen, gibt es zwei Parteien: die Allopathen, die ein spezifisches Heilmittel gegen gewisse Krankheiten anführen und gebrauchen, sozusagen ein Heilmittel, welches die Aufgabe hat, diese Krankheit zu beseitigen. Sie gehen also von der Anschauung aus, die Krankheit sei eine Störung im Organismus, und diese Störung müsse durch ein Mittel beseitigt werden. Dagegen wenden die Homöopathen ein, das sei durchaus nicht das eigentliche Wesen der Krankheit, sondern das eigentliche Wesen der Krankheit sei eine Art Reaktion des ganzen Organismus gegen eine Schädlichkeit in demselben. Es sei eine Schädlichkeit aufgetreten im Orga­nismus, und nun wehre sich der ganze Organismus gegen diese Schädlichkeit. Man müsse an den Symptomen, die beim kranken Menschen auftreten, erkennen und darauf Rücksicht nehmen, daß dasjenige, was Fieber und so weiter erzeugt, eine Art Aufruf sei an die Kräfte im Organismus, die den eingeschlichenen Feind vertreiben können. - Daher werden sich die Anhänger dieser Art Heilweise sagen, man müsse gerade zu denjenigen Mitteln in der Natur greifen,",
      "welche, wenn der gesunde Organismus sie zu sich nimmt, die betreffende Krankheit hervorrufen. Man dürfe natür­lich dann diese Mittel dem kranken Organismus nicht in großer Dosis verabreichen, sondern so, daß die Kraft der betreffenden Mittel gerade hinreicht, um im gesunden Or­ganismus die Krankheitserscheinungen hervorzurufen. Das ist das Prinzip der Homöopathie: dasjenige, was im gesun­den Organismus eine bestimmte Krankheit hervorrufen kann, das schließt auch die Möglichkeit in sich, den kranken Organismus zu einer bestimmten Gesundheit zu führen. Das wird angewendet, wenn der Organismus die Krank­heitserscheinungen durch sich selber zeigt. Man denkt das so: Man sieht, daß der Organismus, wenn er im kranken Zustande die Symptome zeigt, sich bemüht, die Krankheit zu überwinden. Deshalb müssen wir ihn mit diesem Mittel unterstützen.",
      "Daher kommt es, daß der homöopathische Arzt in vielen Fällen gerade das Gegenteil von dem anwenden wird, was der allopathische Arzt anwenden würde. Der Naturheil­kundige steht oftmals - nicht immer - auf dem Stand­punkte, daß es vor allen Dingen nicht darauf ankomme, ob irgendein spezifisches Heilmittel eine Krankheitsschädigung aufhebt, sondern darauf, den Organismus und seine Tätig­keit zu unterstützen, damit er seine inneren Gesundungs­kräfte wachruft, um dem Krankheitsprozeß zu begegnen. So wird der Naturheilkundige vor allen Dingen darauf bedacht sein, auch dem Gesunden zu raten, die Tätigkeit des Organismus zu unterstützen. Er wird zum Beispiel be­tonen, daß es auch für Gesunde weniger darauf ankomme, ob eine Nahrung dem Menschen besonders Gelegenheit gäbe, sagen wir, sich vollzupfropfen mit dem oder jenem, sondern ob eine Nahrung dem Menschen Gelegenheit gibt, seine inneren Kräfte so aufzurufen, daß sie in Tätigkeit",
      "kommen. Die Funktion der Organe wird der Naturheil­kundige vor allem auch beim gesunden Menschen betonen. Er wird sagen: Du wirst dein Herz nicht kräftig machen, wenn du dich bemühst, es mit Aufpeitschungsmitteln fort­während anzuspornen, sondern du wirst dein schwaches Herz dadurch stärken, daß du es in Tätigkeit bringst, daß du Bergpartien machst. - So wird derjenige, der auf die Tätigkeit der Organe des Menschen ausgeht, auch dem ge­sunden Menschen anraten, seine Organe in sachgemäßer Art in Tätigkeit zu bringen.",
      "Sie werden vielleicht, wenn Sie sich um solche Fragen gekümmert haben, weil sie doch die heutige Gegenwart so viel beschäftigen, gesehen haben, mit welcher Heftigkeit und mit welchem Dogmatismus von der einen oder anderen Seite oft gekämpft wird, wie die eine und die andere Seite dasjenige hervorhebt, was sie für ihre Anschauung vorzu­bringen hat. So kann die sogenannte Schulmedizin hin­weisen darauf, wie sie im Laufe der letzten Jahrzehnte, namentlich im Verlaufe der letzten drei bis vier Jahrzehnte, großartige Fortschritte gemacht hat gerade dadurch, daß sie darauf gesehen hat, wie die äußeren Krankheitserreger an die Menschen herankommen und sozusagen ihre Gesundheit vernichten. Diese Schulmedizin kann darauf hinweisen, wie sie besorgt war darum, die äußeren Lebensverhältnisse, die Zustände des Lebens so zu verbessern, daß in der Tat in der letzten Zeit ein Aufschwung eingetreten ist. Gerade diejenige Richtung der Medizin, die vorzugsweise auf die äußeren Krankheitserreger sieht - sagen wir auf die heute so gefürchtete Bakterien- und Bazillenwelt -, sie hat da­durch, daß sie auf dem Gebiete der Hygiene und der sani­tären Einrichtungen eingegriffen hat, in einer für die Laien gar nicht so durchschaubaren Weise, ungeheuer viel getan für die Verbesserung der Gesundheitsverhältnisse.",
      "Es wird gewiß - wiederum nicht ganz mit Unrecht, aber auch nur mit einseitigem Recht - von mancher Seite betont, wie diese Schulmedizin geradezu eine Bakterien- und Ba­zillenfurcht hervorgerufen hat. Aber auf der anderen Seite hat die Untersuchung dazu geführt, daß die Gesundheit im Laufe der letzten Jahrzehnte sich gebessert hat.",
      "Mit Stolz weist der Anhänger dieser Richtung darauf hin, um wieviel Prozent die Sterblichkeit da oder dort in den letzten Jahr­zehnten tatsächlich abgenommen hat. Diejenigen aber, die sagen, daß es nicht so sehr die äußeren Ursachen sind, welche für die Betrachtung der Krankheit wichtig sind, sondern daß es vor allen Dingen die im Menschen liegenden Ur­sachen sind, sozusagen seine Krankheitsdisposition, sein vernünftiges oder unvernünftiges Leben, die werden wieder besonders betonen, daß in den letzten Zeiten zwar unleug­bar die Sterblichkeitsziffern abgenommen haben, daß aber die Krankheitsziffern in einer erschreckenden Weise zu­genommen haben.",
      "Es wird betont, wie gewisse Krankheits­formen zugenommen haben: Herzkrankheiten, Krebskrank­heiten, Krankheitsformen, die in den Schriften der älteren Zeit gar nicht verzeichnet sind, Krankheiten der Ver­dauungsorgane und so weiter. Diejenigen Gründe, die von der einen oder anderen Seite hervorgebracht werden, sind durchaus beachtenswert.",
      "Es kann von einem oberflächlichen Standpunkte aus nicht eingewendet werden, die Bazillen oder Bakterien seien nicht Krankheitserreger furchtbarster Art. Es kann aber auf der anderen Seite auch nicht geleug­net werden, daß der Mensch in gewisser Beziehung entweder gefestigt und gesichert ist gegen Einflüsse solcher Krank­heitserreger oder es nicht ist.",
      "Er ist es nicht, wenn er sich durch unvernünftige Lebensweise um seine Widerstands­kraft gebracht hat.",
      "In vieler Beziehung sind diejenigen Dinge bewundernswert,",
      "welche von der Schulmedizin in der letzten Zeit ge­leistet worden sind. Sehen wir doch einmal zu, wie subtil und fein die Untersuchungen über das gelbe Fieber sind im Zusammenhange mit der Art und Weise, wie es durch ge­wisse Insekten von Mensch zu Mensch übertragen wird.",
      "Wie vorzüglich sind die Untersuchungen in bezug auf die Mala­ria und ähnliches! Aber auf der anderen Seite können wir sehen, daß berechtigte Ansprüche dieser Schulmedizin sehr leicht unser ganzes Leben durchkreuzen können, was in ge­wisser Beziehung zu einer Tyrannis führen kann.",
      "Denken wir, daß - und zwar mit einem gewissen Recht - behauptet wird, in einer in der letzten Zeit häufig auftretenden Krank­heit, in der Genickstarre, werde durchaus nicht der Krank­heitserreger auf einen anderen Menschen übertragen, son­dern Menschen, die ganz gesund sind, die ganz fernstehen dem, was man mit Genickstarre bezeichnet, könnten in ge­wisser Beziehung die Krankheitskeime in sich tragen und sie auf andere Menschen übertragen, so daß Menschen, die unter uns herumgehen, die Träger von Krankheitskeimen seien, von denen dann der, welcher dazu geeignet ist, die Krankheit bekommen kann, während die anderen, welche die Keime tragen, durchaus nicht von der Krankheit be­fallen zu werden brauchen. - So kann es dahin kommen, daß die Forderung aufgestellt wird, die Krankheitskeim­träger zu isolieren; denn wenn irgendeiner an Genickstarre erkrankt ist, so sei er gar nicht einmal so gefährlich wie die­jenigen, welche ihn pflegen, und die vielleicht die eigent­lichen Krankheitsträger sind. Zu welchen Konsequenzen das führen muß, wenn man diesen Menschen den Umgang er­schweren wird, das mag man daraus erkennen: Man kann anführen - und es ist schon angeführt worden -, daß an irgendeiner Schule plötzlich eine größere Anzahl von Kin­dern an dieser oder jener Krankheit erkrankt ist.",
      "wußte nicht, woher die Krankheit gekommen ist. Da stellte sich heraus, daß die Lehrer die eigentlichen Krankheitsträger waren. Sie selber sind nicht von der Krankheit befallen worden, aber die ganze Schule ist von ihnen angesteckt worden. Der Ausdruck Bazillenträger oder Bazillenfänger ist ein Ausdruck, der von einer gewissen Seite sogar mit einem gewissen Recht gebraucht werden kann. Daß der­jenige, welcher Laie ist, auf diesem Gebiete, in allem, was ihm entgegentreten kann von dieser oder jener Seite, sich recht wenig auskennt, das ist schon aus dem wenigen, was wir anführen konnten, fast selbstverständlich.",
      "Nun müssen wir sagen: Gerade das, was wir am Ein-gange unserer heutigen Betrachtung ausgeführt haben, müßte ein Leitfaden sein dafür, was eigentlich aus alledem, was an guten Gründen von der einen oder anderen Seite vor­gebracht wird, wirklich zum Heile führen kann.AlsGrund­satz im tiefsten und bedeutsamsten Sinne muß gelten, daß vor allen Dingen vor uns stehen muß die Individualität des Menschen als eine einzelne Realität, als etwas, was anders ist als jeder andere Mensch. Wir werden uns das sozusagen an einem konkreten Beispiel am besten vor die Seele führen. Nehmen wir einen Menschen an - ich erzähle Dinge, die durchaus vorgekommen sind -, der hatte von Kindheit auf einen gar nicht zu bezwingenden Widerwillen gegen alles, was Fleisch heißt. Er konnte Fleisch nicht ausstehen, nicht essen. Auch nicht das konnte er essen, was irgendwie mit Fleisch im Zusammenhang steht. Er entwickelte sich ganz gesund bei seiner Pflanzenkost. Das ging so lange, bis sich wohlwollende, gute Freunde fanden, die all ihre Energie einsetzten, um diesen Menschen doch von seiner paradoxen Empfindung abzubringen. Sie waren es, die ihm zuerst an-rieten, sozusagen ihm zusetzten, zunächst es einmal mit ein wenig Fleischbrühe zu versuchen. Immer weiter und weiter",
      "wurde er getrieben, bis zum Hammelfleisch. Er fühlte sich dabei immer kränker und kränker. Nach einiger Zeit trat bei ihm auf eine Erscheinung wie ein besonderer Überfluß des Blutes. Es trat auf eine eigentümliche Schlafsucht, und der gute Mann ging zugrunde an einer Gehirnentzündung. Hätte man diesen Menschen nicht jeden Tag aufs neue dar­auf aufmerksam gemacht, was er eigentlich essen solle, hätte man ihn bei seinem gesunden Trieb gelassen, hätte man nicht geglaubt, «eines schicke sich für alle», hätte man sich nicht auf einen Dogmatismus eingeschworen, sondern die individuelle Natur des Menschen respektiert, dann wäre er gesund geblieben.",
      "Aus einem solchen Fall sollen wir aber nicht mehr lernen, als die individuelle Natur des Menschen zu respektieren. Wir sollen nicht ein neues Dogma davon ableiten; wir sol­len im Leben einzig davon profitieren. Wenn wir uns über­legen, wodurch in diesem Falle der Tod herbeigeführt wurde, so können wir uns die Frage in folgender Art beantworten. Wenn Sie sich erinnern, was das letzte Mal im Vortrage über die Ernährungsfragen gesagt worden ist, so können wir daraus entnehmen, was man für die Pflanze Lebens-prozeß nennt: die Pflanze verarbeitet leblosen Stoff in lebendigen Organismus. Im menschlichen Organismus wird dieser Prozeß weitergeführt. In gewisser Beziehung ist das­jenige, was der menschliche und auch der tierische Organis­mus tut, ein Abbau dessen, was die Pflanze aufgebaut hat. Darauf beruht gerade in bestimmter Beziehung der mensch­liche und der tierische Leib, daß abgebaut und zerstört wird, was die Pflanze aufgebaut hat.",
      "Nun kann ein Organismus so eingerichtet sein, daß er so­zusagen gerade den Punkt für sich verlangt, da zu begin­nen, wo die Pflanze mit ihrer Tätigkeit aufgehört hat. Dann kann es für ihn im eminentesten Sinne schädlich sein, wenn",
      "er den Teil des Prozesses, den das Tier mit den Pflanzen­produkten bereits besorgt hat, sich abnehmen läßt. Das Tier führt den Pflanzenprozeß bis zu einem gewissen Punkte. Der Mensch kann ihn dann nur fortsetzen, wenn er tierische Nahrung genießt. Wenn ihm das abgenommen wird und seine Natur gerade über die Kräfte verfügt, welche die Pflanzen-nahrung frisch und kräftig aufnehmen und sie dann weiter­führen, dann wird er in sich Kräfte haben, die jetzt unver­wendbar sind für irgendeine Nahrungsaufnahme und Nah­rungsverarbeitung. Diese Kräfte sind da. Diese schaffen wir deshalb nicht weg dadurch, daß wir ihnen nichts zu tun geben, denn dann werfen sie sich auf etwas anderes. Sie wirken im Inneren des menschlichen Organismus. Die Folge davon ist, daß sie als überschüssige Tätigkeit den Organis­mus im Inneren zerstören.",
      "Man sieht, wenn man einen geisteswissenschaftlich nur wenig geschärften Blick hat, wie die überstürzende Tätig­keit, die den ganzen Menschen eingenommen hat, sich auf sein Blut und sein Nervensystem wirft. Man sieht, wie es in dem Organismus so ausgesehen hat, wie bei einem Haus-bau, in den man ungeeignetes Material hineingeworfen hat, so daß man sich bemühen muß, das ungeeignete Material zu ordnen und zu arrangieren. Nicht ungestraft leitet man die Kräfte der Verarbeitung der Nahrungsstoffe nach dem Innern. Wenn wir uns das klarmachen, dann werden wir tolerant werden gegen die Natur. Dann dürfen wir aber jedenfalls nicht in der entgegengesetzten Richtung wieder zum Schablonisieren kommen und Fanatiker werden des Vegetarismus für einen jeden Menschen. Gerade so, wie sich bei dem Manne, den ich gestern als radikales Beispiel ange­führt habe, die nach innen abgelenkte Tätigkeit überstürzte, so kann es auf der anderen Seite sein, daß es Menschen gibt, welche über diese Tätigkeit gar nicht verfügen, die sozusagen",
      "den Pflanzenprozeß unmittelbar da, wo er aufgehört hat, nicht fortsetzen können. Solche Menschen werden, wenn man ihnen zumutet, ohne weiteres Vegetarier zu werden, erleben, daß sie die Kräfte, welche sie da brauchen, not­dürftig aus dem eigenen Organismus nehmen müssen. Sie werden diesen dadurch in gewisser Weise verzehren und ihm zum Verhängnis werden. Das kann also durchaus auf der anderen Seite vorliegen. Worum es sich handelt, ist, daß wir den Blick abwenden von diesen oder jenen Dogmen, wenn wir von gesunden und kranken Verhältnissen reden, abwenden davon, dieses oder jenes zu essen oder es in dieser oder jener Weise zu bearbeiten. Das, worauf es ankommt, ist, die Bedürfnisse des einzelnen Menschen kennenzulernen. Es kommt vor allem darauf an, daß dieser einzelne Mensch die Möglichkeit hat, in gewisser Beziehung seine Bedürf­nisse selber zu fühlen und zu erkennen.",
      "Wenn eine materialistische Anschauung gar zu sehr auf das bloß Stoffliche sieht, so wäre es doch für diese materia­listische Anschauung notwendig, nach dieser Richtung hin sich zu bewegen, die eben jetzt angedeutet worden ist. Ge­rade für sie wäre es unmöglich, zu schablonisieren und zu vereinheitlichen. Und wie schablonisiert man in unserer heutigen Zeit! Da wird zum Beispiel ohne weiteres gesagt, dieses oder jenes Nahrungsmittel oder diese oder jene Arz­nei sei schädlich. Es ist eine förmliche Epidemie derartiger Schablonen ausgebrochen. Es ist daher nichts anderes mög­lich, als jede Einseitigkeit auszuschließen. Es ist ausgebro­chen eine Epidemie unter dem Stichwort «Kraft», so daß man in den naturheilkundlichen Versammlungen sagt, das Leiden sei eine Kraft. Damit glaubt man, genug getan zu haben, um dies oder jenes anzuschwärzen. Gerade die, welche nur ausgehen sozusagen von der Materie, statt in erster Linie den Menschen als Individualität zu betrachten, die",
      "sollten darauf Rücksicht nehmen, wie dann, wenn man zum Beispiel die anderen Lebewesen überblickt, das Wort Kraft im Grunde genommen jeden Sinn verliert. Unsere Anschau­ungen in bezug auf solche Dinge müssen sich da modifizie­ren. Wer würde da nicht daran denken, daß für den Men­schen eine besondere Kraft zu bezeichnen ist! Die Kaninchen fressen ohne Schaden den Schierling. Sokrates starb daran. Andere sagen: Akonit - Eisenhut - kann ich nehmen. Die Pferde können es auch fressen. - Bei all diesen Dingen müs­sen wir also, wenn wir sie regelrecht betrachten, uns immer die Organisation vorhalten. Wenn wir uns die Organisation vorhalten, so können wir sagen: Im kleinen, also homöo­pathisch, ist es richtig für die Menschennatur. Eines schickt sich nicht für alle!",
      "Die Frage ist also: Wie kann der Mensch einen Maßstab für seine Gesundheit in sich selber gewinnen? Ein gewisser Leuchtturm könnte uns das Kind sein. Wir müssen uns da­her durchaus vorhahen, daß das Kind in ganz bestimmter Weise seine Sympathie oder Antipathie für dieses oder jenes Nahrungsmittel äußert. Das sorgfältige Beobachten dieser Dinge würde für jeden von uns von außerordentlicher Wichtigkeit sein. Es ist manchmal durchaus verfehlt, wenn derjenige, der das Kind zu lenken und zu erziehen hat, die Instinkte, die da beim Kinde auftreten und sich als be­stimmtes Wollen äußern, austreiben will, wenn man sie als Ungezogenheit betrachtet. Vielmehr ist es so: Was das Kind als Trieb, als Instinkt äußert, ist ein Anzeichen dafür, wie die innere Natur des Kindes geartet ist. Was das Kind emp­findet und was ihm schmeckt, wonach es Verlangen hat, da ist die Empfindung, das Verlangen nichts anderes als der Ausdruck dafür, daß der Organismus gerade dieses oder jenes verlangt. Ja, ein Fingerzeig, oder, wenn wir radikaler sprechen wollen, ein Leuchtturm für die Erkenntnis kann",
      "uns dieser leitende Instinkt des Kindes sein. Wir können das ganze Leben durchwandern und werden überall die Notwendigkeit finden, daß der Mensch in gewisser Be­ziehung gerade diese innere Sicherheit in sich entwickeln muß für das, was sein Organismus braucht. Das ist unbe­quemer, als sich von dieser oder jener Partei die Richtung vorschreiben und sich sagen zu lassen, was für alle Menschen das Gute ist. Die Menschen haben es nicht so leicht wie die, welche mit einem bestimmten allgemeinen Rezept kommen, das man sich nur in die Tasche zu stecken braucht, um zu wissen, was den Menschen gesundmachen und was ihn krankmachen kann. Gerade wenn man mit einem solchen Leitfaden die Gesundheit betrachtet, wird man auch in be­zug auf die Krankheit sich klarmachen müssen, daß für die verschiedenen Menschen die verschiedensten Bedingungen für Gesundheit und Heilung vorliegen.",
      "Nehmen wir an, jemand habe Migräne. Wer dogmatisch auf dem Standpunkt steht - wenn auch die Schulmedizin dies nicht mehr wahrhaben will -, daß es spezifische Heil-mittel gibt für diese oder jene Krankheit, der wird sagen:",
      "Man gebe dem Kranken bestimmteHeilmittel gegen Migräne. Der Kranke wird sich wohler fühlen, und die Migräne wird verschwinden. - Wer auf dem Standpunkte der Naturheil-kunde steht, wird sagen, wenn er es zum Fanatiker gebracht hat, man kann so nur das Symptom bekämpfen. Man hat manchem damit mehr geschadet als genützt. - Eine andere Richtung sagt: Es komme darauf an, daß man auf die tiefe­ren Ursachen einwirke. Und dann wird man mit allerlei Dingen kommen, die vielleicht mehr auf den Kern der Sache eingehen, aber im einzelnen Fall nicht so schnell ein Wohl­befinden herstellen, die aber wirklich tiefer auf den Krank­heitskern eingehen. Man wird, wenn man sich dogmatisch auf den einen oder anderen Standpunkt stellt, das eine oder",
      "das andere bekämpfen oder für nützlich halten. Es handelt sich aber dabei, so sonderbar es klingen wird, wiederum um den Menschen. Es könnte einen Menschen geben, der sich sagte: Es wäre ganz schön, wenn ich ein Hilfsmittel bekom­men könnte und nicht zu warten brauchte, bis die Natur­heilkunde dem Kern der Sache beigekommen ist, um dann dasjenige zu tun, was es möglich macht, die Krankheit in ihren tieferen Wurzeln zu erkennen und zu beheben. Aber dazu habe ich keine Zeit. Es ist für mich viel wichtiger, daß ich die Migräne so bald wie möglich loskriege und meiner Tätigkeit zurückgegeben werde.",
      "Nehmen wir ferner an, dieser Mensch habe eine die Ge­sundheit fördernde Beschäftigung. Diese sei so geartet, daß er, wenn er durch das Migränemittel das Übel losbekommen hat, sich der günstigen Wirkung der Arbeit hingeben kann. Dann wird ihm das Migränemittel wenig schaden. Er wird wenig aus seiner Tätigkeit gerissen sein, die ihm nützt. Dann wird er nach einem Rezept einer Medizin suchen, die ihn in diesem Zustand erhält.",
      "Dieser Vergleich muß aber bis zu Ende geführt werden. Man darf nicht vergessen, daß einer da sein muß, der da arbeitet, wie der Führer auf der Lokomotive. Nehmen wir an, bei einer Lokomotive zeige sich, daß eine Kurbel beson­ders schwer geht. Da kann jemand sagen: Daran sehe ich, daß dieser Lokomotivführer diese Kurbel nicht treiben kann, weil er zu schwach ist. Ich werde einen anderen Loko­motivführer nehmen, der mehr Kräfte anwenden kann, um die Kurbel zu treiben. - Ich will jetzt auf das Zentrum der Sache eintreten. Ein anderer sagt: Man kann ja vielleicht das, was die Kurbel schwer zu drehen macht, ein wenig aus-feilen, damit die Kurbel leichter geht. Dann kann der Zug-führer bleiben. - Man bessert also die Maschine aus. Natür­lich darf man das nicht als ein allgemeines Rezept anwenden.",
      "Wenn man sagen wollte: Wenn der Lokomotive etwas fehlt, so muß man daran feilen -, so braucht das nicht immer richtig zu sein. Der betreffenden Lokomotive kann es auch abträglich sein. Man muß also feststellen, ob man das tun darf. Damit hat man den Schaden einfach ausgebes­sert. Wenn der Betreffende die innere Kraft hat, so wird er, wenn er nicht gestört wird, schon selbst die Sache wieder in Ordnung bringen.",
      "Freilich würde es unter Umständen schlimm sein, wenn man in derselben Weise dächte gegenüber jemand, der die Migräne loshaben will, aber hinterher nicht zu einer mit seiner Tüchtigkeit zusammenhängenden Tätigkeit geht. Er würde besser getan haben, wenn er die innere Ursache weg­geräumt hätte. So müssen wir also durchaus auch in diese Materie eingedrungen sein, da es ja für das, was man Krank­heit nennt, spezifische Heilmittel gibt. Die Anwendung spe­zifischer Heilmittel hängt in gewisser Beziehung damit zu­sammen, daß unser Organismus ein selbständiges Wesen ist und in vieler Richtung ausgebessert werden kann, wenn man sich darauf verlassen darf, daß nach der Ausbesserung eine recht tüchtige Kraft vorhanden ist, die den Menschen antreibt. Das braucht man nicht zu betonen. Man treibt dann eben nur eine Symptom-Kur, denkt aber eben doch nur materialistisch. Der Naturheilkundige wird manches wissen, was ganz richtig wäre zur Beseitigung dieser oder jener Krankheit, aber ebenso wahr ist es, daß dieser oder jener Mensch nicht die Zeit und nicht die Kraft hat, es durchzuführen, und daß es sich vor allen Dingen für ihn darum handelt, den Schaden wieder gutzumachen.",
      "Sie sehen, daß hier nicht in einseitiger, sondern in all­seitiger Weise gesprochen werden muß. Wenn man die Un­bequemlichkeit mit in Kauf nimmt, so genügt es nicht, Theo­retiker zu sein, sondern man muß auf die Tatsachen eingehen",
      "und hat auf den ganzen Menschen zu sehen. Darauf kommt es an. Wenn wir so sprechen, müssen wir uns dar­über klar sein, daß wir dann, wenn wir den Menschen als Realität betrachten wollen, den ganzen Menschen ins Auge fassen müssen. Der ganze Mensch ist für die Geisteswissen­schaft nicht bloß der äußere physischeLeib, namentlich dann nicht, wenn unsere Gesundheit nicht bloß durch äußere, sondern durch innere Ursachen zerstört ist. Was viel mehr in Betracht kommt, ist die Gesundheit des Ätherleibes, der ein Kämpfer ist gegen die Krankheit bis zum Tode. Dann ist der Astralkörper da, ein Träger der Leidenschaften, Triebe, Begierden und Vorstellungen, und endlich der Ich-Träger, der macht, daß derMensch ein selbstbewußtes Wesen ist. Wer auf den ganzen Menschen Rücksicht nehmen will, der muß auf die vier Glieder durchaus Rücksicht nehmen, und wenn die Frage nach der Gesundheit in Betracht kommt, so handelt es sich nicht nur darum, daß wir Störungen be­rücksichtigen, die den physischen Leib betreffen, sondern auch das betrachten, was in den höheren Gliedern, in den mehr seelisch-geistigen Gliedern, vor sich geht. Da müssen wir feststellen, daß nicht bloß von dieser oder jener Partei-schattierung, sondern von unserer ganzen zeitgenössischen Gesinnung gesündigt wird.",
      "Sehr selten wird die Frage gestellt: Wie hängt die Ge­sundheitsfrage mit den seelisch-geistigen Dingen zusam­men? Man wird heute viel Zustimmung finden, wenn man davon spricht, wieviel dieses oder jenes Nahrungsmittel Brennwert hat, wie dieses oder jenes Nahrungsmittel im Organismus wirkt. Man wird auch viel Zustimmung haben, wenn man auseinandersetzt, wie die Luft in dieser oder jener Gegend ist, wo dieses oder jenes Sanatorium sich be­findet, wie die Luft und auch das Licht da oder dort wirkt. Aber nicht wird man finden Anklang, wenn man seelische",
      "Eigenschaften als Ursache bestimmter Erklärungen angibt. Nehmen wir die Instinkte des Kindes, wie sie sich aus­drücken in Sympathie und Antipathie gegenüber diesem oder jenem Nahrungsmittel. Wir nehmen zunächst als An-zeiger das Ekelgefühl, mit dem sie dies oder jenes zurück­weisen. Es weist darauf hin, daß das, was in sich gesund­heitliches Sein ist, was zugrunde liegt dem physischen Leibe",
      "- der Astralleib, der aus Gefühlen und Empfindungen, Im­pulsen und Begierden besteht -, daß auch das Geistig-See­lische gesund sein muß, und daß, wenn eine Abweichung von dem Gesunden im Menschen erblickt wird, man auf die Gesundung des astralischen Leibes achten muß. Frägt man heute wirklich noch, wenn diese Fragen in Betracht kom­men, was des Menschen Seele erlebt gegenüber der Außen­welt? Der Geisteswissenschaftler muß darauf hinweisen, daß es im Grunde genommen wenig darauf ankommt, ob man einen Menschen, der an diesem oder jenem krankt, da oder dorthin schickt, weil man glaubt, die Luft oder das Licht werde aus äußeren mechanischen oder chemischen Gründen gesundend auf ihn wirken. Eine andere, viel grö­ßere Frage ist es, ob ich ihn in eine solcheUmgebung bringen kann, daß er Freude, Erhebung, in gewisser Beziehung eine Durchleuchtung seines ganzen Gefühlslebens nach einer be­stimmten Richtung erfahren kann. Wenn wir dies im großen betrachten, so werden wir auch verstehen, daß es zu dem Ge­sundsein gehört, wenn dem Menschen eine Speise schmeckt, daß der Mensch sozusagen in seinem Geschmacke, in der unmittelbaren Geschmacksempfindung, in der Annehmlich­keit und Freude, die ihm die Speise bereitet, einen Grad­messer haben muß für dasjenige, was er essen soll, und daß der Mensch auf der anderen Seite an dem richtig auftreten­den Hungergefühl einen Gradmesser haben soll dafür, wann sein Organismus essen soll.",
      "Es sind nicht bloß von der materiellen Welt her kom­mende Einflüsse, welche diese innere Sicherheit im Menschen zerstören, es sind in den weitaus meisten Fällen durchaus auch Einflüsse aus dem geistigen Leben, welche in dem Men­schen die Sicherheit des Hungertriebes untergraben. Statt dem Menschen im richtigen Moment einen gesunden Hunger beizubringen, läuft die geistige Natur so ab, daß dieser Hunger nicht da ist, sondern Appetitlosigkeit. Ein Mensch, der die Bedürfnisse seines Organismus in der richtigen Weise entwickelt hat, so daß ihm das Richtige schmeckt und sym­pathisch ist und auch seinem Organismus dienen kann, ein solcher wird auch das richtige sympathische Gefühl haben, um die richtige Umgebung, die seiner Gesundheit dient in bezug auf Licht und Luft, zu finden, so daß ihm zur rich­tigen Zeit der Hunger danach kommt.",
      "Das sind Forderungen, die einen Zusammenhang mit dem gesundheitlichen Leben haben und die zu dem hinführen, was der astralische Leib und das Ich beizutragen haben zu dieser Gesundheit. Leicht wird der Einwand gemacht: wenn jemand Hunger habe, könne er nicht von dem Gefühle und von der Empfindung leben. Das ist wahr. Auch wenn man ihm eine leckere Speise vorsetzt, so daß ihm unter Umstän­den das Wasser im Munde zusammenfließt, kann man ihn nicht sättigen, indem man ihm imaginäre Geschmacksfreu­den beschafft. Leicht ist dieser Einwand zu machen. Was wir ihm geben können an dem, was seine Seele so beeinflußt, daß sie in richtiger Weise die Empfindungen und Vorstel­lungen ablaufen läßt, das ist ganz gut; daß wir ihn dadurch nicht sättigen und gesundmachen können, ist selbstverständ­lich. Aber was dabei übersehen wird, ist ein anderes. Nicht die Nahrung können wir regulieren, wohl aber den Ge­schmack regeln bis zum Hungergefühl. Hier mündet das, was sich heute zersplittert' weil es nur vom Standpunkte",
      "äußerlicher, stofflicher Betrachtung gehandhabt wird, ein in das Geistig-Seelische; es mündet so ein, daß wir das geistig-seelische Leben treffen.",
      "Es ist nicht einerlei, ob der Mensch diese oder jene Speise mitLust zu sich nimmt, ob er in dieser oder jener Umgebung lebt, diese oder jene Arbeit verrichtet, oder ob er sie mit Unlust tut. Damit hängt in geheimnisvoller Weise, mehr als mit irgend etwas anderem, das zusammen, was man seine innere Gesundheitsdisposition nennt. Wenn wir beim Kinde sehen, daß es richtige Instinkte entwickelt, und wenn man die Möglichkeit hat, seine inneren Instinkte zu beobachten, die es gradmäßig haben muß, so ist es notwendig, daß das Erwachen des Geistig-Seelischen so lebt, daß die richtigen Bedürfnisse zur rechten Zeit vor die Seele hintreten. So ist es notwendig, daß der Mensch fühlt und empfindet, was für ein Verhältnis er herstellen soll zwischen sich und der Außen-welt. Das Leben ist im weitesten Umfange geeignet, den Menschen in Irrtum über Irrtum zu bringen über dieses sein Verhältnis zur Außenwelt. Und gerade unsere heutige Gei­stesrichtung ist in mehr als einer Richtung die Veranlassung solcher Irrtümer.",
      "Damit wir uns besser verstehen, möchte ich auf den klei­nen Anfang hinweisen, den wir mit einer bestimmten Heil-weise gemacht haben. In München wird von einem unserer geisteswissenschaftlichen Genossen eine Art von Kur- oder Heilweise versucht, wie sie sich ergibt aus den Anschau­ungen der Geisteswissenschaft heraus. Wer heute glaubt, auf den Menschen könnten in gesundem Sinne wirken nur stoff­liche, physisch-chemische und physiologische Einflüsse, der wird erstaunt sein, daß die Menschen in eine besonders eigenartig gefärbte Kammer geführt werden, und daß da durch die Kräfte einer gewissen Farbe und durch andere Dinge, die hier nicht weiter erörtert werden können, auf",
      "die menschliche Seele gewirkt wird. Allerdings kann dabei nicht auf die Oberfläche gewirkt werden. Da müssen Sie aber sehen den Unterschied zwischen dieser Wirkungsweise in den Kammern, also einer Art Kammer-Therapie, einer Art Farben-Therapie, und dem, was man Licht-Therapie nennt. Wenn der Mensch mit Licht bestrahlt wird, so liegt dem der Gedanke zugrunde, das Licht, das physische Licht, unmittelbar wirken zu lassen, so daß man sich sagt, wenn man diesen oder jenen Lichtstrahl auf den Menschen wir­ken läßt, so werde durch die Wirkung von außen auf den Menschen gewirkt. Darauf wird bei der erwähnten Farben-Therapie nicht Rücksicht genommen.",
      "Bei dieser der Geisteswissenschaft entnommenen Heil-weise, die unser Freund Dr. Peipers eingerichtet hat, ist nicht darauf gerechnet, was die Lichtstrahlen als solche, un­abhängig von der menschlichen Seele, auf den Menschen bewirken, sondern es ist Rücksicht darauf genommen, was als Vorstellung einer Seele - sagen wir unter Einwirkung der blauen Farbe, nicht des Lichtes - auf dem Umwege durch die Seele bewirkt wird. Es ist beabsichtigt, dadurch auf den ganzen körperlichen Organismus zurückzuwirken.",
      "Diesen gewaltigen Unterschied zwischen dem, was man sonst Licht-Therapie nennt, und dem, was man hier Farben-Therapie nennen kann, muß man ins Auge fassen. Es kommt dazu, daß gewisse Kranke ausgefüllt sind mit dem Inhalte einer ganz bestimmten Farbenvorstellung. Man muß wis­sen, daß Farben in sich Kräfte enthalten, die dann in Er­scheinung treten, wenn sie uns nicht nur bestrahlen, sondern in unserer Seele wirken. Man muß wissen, daß gewisse Far­ben etwas sind, das fördernd wirkt, daß eine andere Farbe etwas ist, was Sehnsuchtskräfte auslöst, daß eine dritte Farbe etwas ist, was die Seele über sich selbst erhebt, und eine andere Farbe etwas, das die Seele unter sich herunterdrückt.",
      "Wenn wir auf diese physisch-geistige Wirkung sehen, dann wird sich uns zeigen, was der Urgrund des Physischen und Ätherischen ist: daß unser astralischer Leib der eigentliche Bildner des Physischen und Ätherischen ist. Das Physische ist nur eine Verdichtung des Geistigen, und das Geistige kann wieder zurückwirken auf das Physische, wenn es in der richtigen Weise durchwirkt und durchlebt wird. Dann werden wir uns den Grundgedanken, der einer solchen Sache zugrunde liegt, vor Augen führen können, so daß wir auch Hoffnung haben dürfen dadurch, daß wir wieder eine Wis­senschaft haben, die hinweist darauf, wie im Menschen Gei­stig-Seelisches lebt und daß durch die Krankheit im Geistig-Seelischen sich die Störung als Krankheit im Physischen ausdrückt.",
      "Wer sich das klarmacht, wird hinsichtlich der Gesund­heitsfragen auf die Geisteswissenschaft hoffen dürfen. So leicht es ist, zu sagen: Mit Weltanschauung könnt ihr einen Menschen nicht füttern, - so ist es doch auch wahr, daß von der Weltanschauung die Gesundheit des Menschen abhängt. Für die heutige Menschheit ist das ein Paradoxon, für die Zukunft eine Selbstverständlichkeit! Ich will es noch ein wenig weiter erörtern. Man kann sagen: Der Mensch muß auf die reine objektive Wahrheit kommen, er muß sie be­greifen, muß sie zu genauen Abbildern der äußeren physi­schen Tatsachen machen. - Eine solche Forderung kann man als Theoretiker aufstellen. Man kann einen Menschen als Ideal hinstellen, der sich bemüht, nur das zu denken, was die Augen sehen, die Ohren hören und die Hände betasten können. Da kommt nun die Geisteswissenschaft und sagt:",
      "Ihr könnt das, was wirklich ist, niemals begreifen, wenn Ihr nur auf das geht, was äußerlich wahrnehmbar ist, was die Augen sehen, die Ohren hören, die Hände greifen kön­nen. Was wirklich ist, enthält das Geistige als Urgrund. Das",
      "Geistige kann man nicht wahrnehmen. Man muß es durch Mitproduktion des Geistigen und Seelischen erleben. Zum Geistigen braucht man produktive Kräfte. Der Geistes-wissenschaftler ist, wenn er von dem eigentlichen Teile sei­ner Wissenschaft spricht, nicht immer in der Lage, hand­greiflich vorzuführen, was zu seinen Begriffen führt. Er schildert dasjenige, was nicht mit Augen, Ohren oder Hän­den gefaßt werden kann, weil es mit den Augen des Geistes verfolgt werden muß. Da kann man dann sagen: Das ist ja eine Schilderung von etwas, das es in der sinnlichen Welt gar nicht gibt. Für uns ist Wahrheit das, was ein inneres Abbild der äußeren Wirklichkeit gibt. - Eine solche Theorie mag man aufstellen, aber über Wahrheit, über Erkenntnis und Wirklichkeit wollen wir heute nicht sprechen. Wir wol­len über den Gesundheitswert sprechen. Die Sache ist so, daß alle diejenigen Vorstellungen, die wir bloß von der äußeren sinnlichen Wirklichkeit abstrahieren, die sozusagen nur Abbilder sind dessen, was man mit Augen sieht, mit Ohren hört, mit Händen betastet, welche nicht beruhen auf der inneren Mittätigkeit der Seele beim Schaffen von Bil­dern, alle diese Abstraktionen, alle treu an der Wirklichkeit der äußeren Sinne haftenden Vorstellungen haben keine inneren Bildekräfte. Daher bleibt die Seele tot; sie rufen die Seele nicht auf, ihre innerlich schlummernden Kräfte in Tätigkeit zu bringen und damit den Organismus in das richtige Fahrwasser seiner Tätigkeit zu bringen.",
      "Es mögen noch so sehr die äußeren Tatsachen-Fanatiker davon sprechen, man solle die Wirklichkeit nicht mit Bil­dern der übersinnlichen Welt durchsetzen. So paradox es auch klingt, diese Bilder bringen unseren Geist wieder in eine Tätigkeit, die ihm angemessen ist. Sie bringen ihn wie­der in Einklang mit dem physischen Organismus. Derjenige, der an den rein abstrakten Vorstellungen der bloß materialistischen",
      "Wissenschaft haftet, der tut aus seinem Geisti­gen nichts für seine Gesundheit. Wer positiv nur Abstrak­tionen in seinem Begreifen sich schafft, macht seine Seele öde und leer, und er ist immer darauf angewiesen, das äußere Instrument des Leibes zum Träger der Gesundheit und zum Träger der Krankheit zu machen. Wer in ungeordneten und verkehrten Vorstellungen lebt, der weiß auch nicht, wie er sich in geheimnisvoller Weise vollpumpt mit den Ursachen der Zerstorung seines Organismus Daher stehen die Geistes-wissenschaftler auf dem Standpunkte, daß durch das, was die Geisteswissenschaft über die übersinnliche Welt geltend macht - über jene Welt, die wir nicht mit unseren Sinnen erkennen, sondern in stiller Weise innerlich wachrufen müssen -, wir unsere Seele innerlich so regsam machen, daß ihre Tätigkeit in Einklang steht mit der geistigen Welt, aus der heraus unser ganzer Organismus geschaffen worden ist. Daher wird unser Organismus nicht durch kleinliche Mittel zur Gesundung gebracht, sondern die Geisteswissenschaft selbst ist das große Heilmittel zur Gesundung.",
      "Derjenige, der aus dem großen Gesichtspunkte der Welt seine Gedanken bildet, diese Gedanken lebendig macht, der ruft eine solche innerliche Tätigkeit hervor, daß auch seine Gefühle und Empfindungen in einer harmonischen, die Seele beseligenden Weise abfließen. Wer auf seine Gedanken so wirkt, wirkt auch auf seine Willensimpulse, und diese wirken dann in einer gesunden Weise. Aber nur dadurch, daß wirklich eine gesunde Weltanschauung, eine gesunde Harmonie der Gedanken unsere Seele erfüllt, werden auch unsere Empfindungen und im Zusammenhange damit unsere Lust und Unlust, unsere Sympathie und Antipathie, unser Verlangen und unser Abscheu so geregelt, daß wir der Welt so gegenüberstehen, daß wir im einzelnen Falle wissen, was zu tun ist, wie das Kind, dessen Instinkt noch nicht verdorben",
      "ist. So werden wir in unserer Seele innerlich diejenigen Gefühle und Empfindungen und Willensimpulse und Be­gierden wachrufen, die uns eine sichereRichtschnur im Leben sind, die uns anweisen, was zu tun ist, um das richtige Ver­hältnis zu der Außenwelt und zu uns selber hervorzurufen.",
      "Es ist nicht zuviel gesagt, wenn wir sagen: Klare, helle Gedanken, umfassende Gedanken, wie sie nur durch eine umfassende, auf das Ganze der Welt, also auch auf das Übersinnliche gehende Weltanschauung hervorgerufen wer­den können, sind Voraussetzung für die Gesundheit. Reine, dem Objektiven des Geistes entsprechende Gefühle, wie sie solchen Gedanken entsprechen und solchen Willensimpulsen, die werden den Menschen die Möglichkeit geben, den ge­sunden Hunger zu empfinden. Wenn man den Menschen auch nicht mit Weltanschauung füttern kann, wird es doch möglich, in dem, was für seine Seele das Entsprechende ist, das Richtige zu finden, zu suchen das für ihn Entsprechende und zu verabscheuen, was nicht entsprechend ist. Die Ge­danken, welche Abbilder sind für die übersinnliche Welt, sind das beste Verdauungsmittel - wenn auch als Para­doxon. Sie sind nicht bloß Gedankenkräfte, die auch gut für die Verdauung sind, sondern sie wirken günstig auch dadurch, daß sie durch die geistkräftigen Gedanken in sich die Kräfte wachrufen, welche die Verdauung in geregelter Weise vor sich gehen lassen.",
      "So lange die Menschen diesen Ruf der Geisteswissenschaft nicht vernehmen, so lange sie immer wieder glauben, das­jenige, was ihnen in dieser oder jener Krankheitsform in dieser oder jener Weise entgegentritt, das habe seine Sühne gefunden, wenn man ein entsprechendes Mittel dafür ge­funden hat, so lange werden sie die Wichtigkeit der Geistes­wissenschaft nicht erkannt haben. Sie werden auch nicht er­kannt haben, inwiefern die Gesundheit im Wesen der Entwickelung",
      "eine Rolle spielt. Auch die gehen nicht weit ge­nug, welche sagen, man solle nicht Symptom-Kuren aus­führen. Auch sie erfassen nicht den geistigen Kern. Wer an die Geisteswissenschaft herantritt, der wird finden, daß sie eine Weltanschauung ist, durch welche innere Seligkeit fließt, eine Weltanschauung der Lust und Freude, daß sie Voraus­setzung ist, um das große Heilmittel für die Gesundheit zu fördern. Leichter ist es, dieses oder jenes Mittel zu gebrau­chen, als sich in den Strom der Geisteswissenschaft zu be­geben, um das zu finden, was die Menschen immer gesunder und gesunder machen wird. Dann wird man aber einsehen, wenn man sich in diese Geisteswissenschaft hinein begibt, daß es wahr ist, was ein altes Wort sagt: «In einem gesun­den Körper wohnt eine gesunde Seele», aber daß es falsch ist, dieses Wort materialistisch aufzufassen. Wer da glaubt, er müsse dieses Wort materialistisch auffassen, der soll nur auch gleich sagen: Hier sehe ich ein Haus. Dieses Haus ist schön. Also schließe ich daraus, weil dieses Haus schön ist, so muß es auch hervorgebracht haben einen schönen Besit­zer. Das schöne Haus macht einen schönen Besitzer. - Viel­leicht ist der doch etwas klüger, der sagt: Hier ist ein schönes Haus; daraus schließe ich, daß darin ein Besitzer lebt, der Geschmack hat. Ich sehe in dem Besitzer des schönen Hauses einen Menschen von gutem Geschmack, und in dem Haus das äußere Anzeichen dafür, daß der Besitzer ein Mensch von gutem Geschmack ist.",
      "Vielleicht findet sich aber auch der Gescheite, der sagt:",
      "Weil äußere Mächte den Körper gesund gemacht haben, hat sich der Körper wieder eine gesunde Seele formiert. - Aber richtig ist es nicht, sondern recht hat wohl, wer da sagt:",
      "Hier sehe ich den gesunden Körper. Das ist ein Zeichen dafür, daß er aufgebaut sein muß von einer gesunden Seele. Er ist gesund, weil die Seele gesund ist. - Deshalb kann",
      "man sagen: Weil man das äußere Symptom des gesunden Leibes erblickt, deshalb muß da eine gesunde Seele zugrunde liegen. Eine materialistische Zeit mag sich das Wort: «Einem gesunden Leibe muß eine gesunde Seele zugrunde liegen» ganz materialistisch auslegen. Die Geisteswissenschaft aber zeigt uns, daß in einem gesunden Leibe eine gesunde Seele am Werke ist."
    ],
    "sentences": [
      [
        "GESUNDHEITSFRAGEN IM LICHTE DER"
      ],
      [
        "GEISTE SWISSENSCHAFT"
      ],
      [
        "Berlin, 14.",
        "Januar1909"
      ],
      [
        "Das Thema, das uns heute beschäftigen soll, schließt eine Anzahl von Fragen ein, die den Menschen mit Recht auf das allertiefste interessieren.",
        "Die Fragen nach der Gesund­heit sind ja solche, die zusammenhängen mit alledem, was den Menschen lebenstüchtig macht, mit alledem, was ihm verhilft, seine Bestimmung in der Welt ungehemmt zu er-füllen, und es ist deshalb die Gesundheit gewiß für die mei­sten Menschen, in dem richtigen Lichte gesehen, etwa so, daß sie sie sozusagen anstreben, wie man äußere Güter an­strebt.",
        "Aber die Gesundheit ist auch als ein inneres Gut zu betrachten, wie die äußeren Güter zunächst nicht um ihrer selbst willen von dem gesund denkenden Menschen ange­strebt werden, sondern als Mittel der Arbeit, als Mittel seines Wirkens und Schaffens.",
        "Daher können wir es wohl erklären, daß der Drang, die Sehnsucht, sich Aufklärung zu verschaffen über die Rätsel und Fragen des gesunden und kranken Lebens, insbesondere in unserer Gegenwart so tiefgehend sind.",
        "Allerdings ist im allgemeinen Denken jene Gesinnung wenig verbreitet, die geeignet ist, den Menschen empfänglich zu machen gerade für diejenigen Antworten, die man braucht, wenn man solche Fragen lösen will, welche so innig mit dem ganzen Wesen des Menschen zusammen­hängen."
      ],
      [
        "Es soll auch heute, wie schon einmal bei einer ähnlichen Gelegenheit, an einen alten Spruch erinnert werden, der"
      ],
      [
        "manchem einfällt, wenn von Gesundheit und Krankheit gesprochen wird, an den Ausspruch: Es gibt so viele Krank­heiten und nur eine einzige Gesundheit! - Dieser Ausspruch erscheint im Grunde genommen manchen so selbstverständ­lich als möglich, und dennoch ist er ein Irrtum, ein Irrtum im eminenten Sinne des Wortes, denn es gibt nicht bloß eine Gesundheit, sondern so viele Gesundheiten, wie es Men­schen gibt.",
        "Das ist es gerade, was wir in unsere Gesinnung aufnehmen müssen, wenn wir die Fragen nach dem Gesun­den und Kranken im richtigen Lichte sehen wollen.",
        "Wir müssen in unsere Gesinnung aufnehmen, daß der Mensch ein individuelles Wesen ist, daß jeder Mensch anders be­schaffen ist als der andere, und daß, was dem einen heilsam und für den anderen schädlich und krankmachend sein kann, ganz abhängt von seiner individuellen Beschaffenheit."
      ],
      [
        "Daß diese Gesichtspunkte nicht so weitverbreitet sind, das zeigt eine Erfahrung, die jeder von uns alltäglich ma­chen kann.",
        "Da fehlt dem einen dies oder jenes.",
        "Die Mutter erfährt es oder sie nimmt es wahr; auch sie erinnert sich, daß ihr in ähnlichen Fällen dies oder jenes geholfen hat, also darauf los!",
        "Dann kommt der Vater, der sich erinnert, daß etwas anderes geholfen hat.",
        "Dann kommt die Tante, dann der Onkel, der sagt: In die frische Luft gehen. - Diese Anordnungen sind oft so widersprechend, daß sie gar nicht erfüllt werden können.",
        "Jeder hat sein Heilmittel, auf das er eingeschworen ist.",
        "Das muß dann losgelassen werden auf den armen Kranken.",
        "Wer hätte es nicht erfahren, daß diese sich überstürzenden guten Ratschläge eigentlich eine recht mißliche Sache sind, wenn dem Menschen dies oder jenes fehlt!",
        "Alle diese Dinge gehen hervor aus einer unrealisti­schen Denkweise, aus einer abstrakten Denkweise, aus einem Dogmatismus, der gar nicht beachtet, daß der Mensch ein individuelles Einzelwesen ist.",
        "Jeder Mensch ist ein Wesen"
      ],
      [
        "für sich, und darauf kommt es vor allen Dingen an:"
      ],
      [
        "diese Realität Mensch ins Auge zu fassen, wenn man es mit den Erscheinungen gesund und krank zu tun hat."
      ],
      [
        "Nun entspringt ja eine solche Hilfsbedürftigkeit, wie sie der Mensch in der Krankheit hat, gewiß einer Artung sei­nes inneren Wesens, die das Mitgefühl, das Mitleid seiner Umgebung wachrufen muß.",
        "Wir können begreifen, daß jeder gern helfend herbeispringen möchte, denn es ist dies nur ein Ausdruck dafür, welches tiefste Interesse gerade diese Fragen im Zusammenhange mit der ganzen Menschen-natur hervorrufen.",
        "Allerdings, wenn man auf der einen Seite dieses tiefe Interesse ins Auge faßt, auf der anderen Seite aber nur ein klein wenig hineinblickt in das, was in unserer Zeit an verschiedenen Anschauungen über Gesund­heit und Krankheit herrscht, dann kann man unter Um­ständen recht betrübt werden.",
        "Man könnte sagen, die Krankheit sei eine so wichtige Sache im Menschenleben und warum es denn geschehe, daß sich gelehrte und ungelehrte Leute, Mediziner und Laien, nicht nur über die Heilmittel für die einzelnen Krankheiten, nicht nur über die rechten Wege zur Gesundheit, sondern sogar über das Wesen des Krankseins in den mannigfaltigsten Theorien streiten.",
        "Es scheint manchmal, daß in unserer Zeit geistiger und wissen­schaftlicher Betriebsamkeit der kranke und vielleicht auch der gesunde Mensch mehr als je den Parteianschauungen ausgesetzt ist, die von allen Seiten sich geltend machen in bezug auf wichtige Fragen der Menschheitsentwickelung und des Menschheitswesens."
      ],
      [
        "Dürfen wir nun - diese Frage wollen wir uns heute stel­len - die Hoffnung hegen, daß die Geisteswissenschaft, die von den verschiedensten Seiten in diesen Vortragszyklen charakterisiert ist und noch charakterisiert werden wird, in gewisser Beziehung auch Licht bringen kann in die Theorien"
      ],
      [
        "und Partei-Schattierungen, welche wir heute um uns herum erblicken, wenn wir die Ansichten über Gesundheit und Krankheit einmal an uns herantreten lassen?",
        "Es ist ja des öfteren hier betont worden, daß die Geisteswissenschaft einen höheren Gesichtspunkt anstrebt, der es möglich macht, dasjenige, was die Menschen in Parteiungen zerteilt, da­durch, daß sie nur gewisse engere Kreise des Anschauens und Beobachtens haben, zu überbrücken, zu zeigen, wie das eine dem anderen widerstrebt, weil es einseitig ist."
      ],
      [
        "Wir haben öfter gezeigt, daß die Geisteswissenschaft gerade da ist, um das Gute in den Einseitigkeiten zu suchen und die Harmonie unter den verschiedenen Einseitigkeiten herzu­stellen.",
        "Einseitigkeit - so muß sich derjenige sagen, der die Sache nicht nur oberflächlich betrachtet - dürfte es doch sein, was uns da entgegentritt, wenn von seiten dieser oder jener Krankheitslehre diese oder jene Dogmen mit einer anspruchsvollen Autorität gepredigt werden."
      ],
      [
        "Sie haben alle erfahren, welche Summen von Wortschattierungen einander gegenüberstehen in bezug auf diese Fragen.",
        "Jeder weiß, daß auf der einen Seite dasjenige steht, was man oftmals -heute sogar schon leider im verächtlichen Sinne - die Schul­medizin nennt mit ihrer allopathischen Richtung, und auf der andern Seite jene Richtung, die man als die homöopa­thische bezeichnet."
      ],
      [
        "Dann haben aber auch weite Kreise Zu­trauen gefunden zu dem, was man Naturheilkunde nennt, die vielfach eine andere Auffassung über Krankheit und Gesundheit hat und nicht nur das empfiehlt, was auf den kranken Menschen Bezug hat, sondern auch das, was als richtig gehalten wird für den gesunden Menschen, damit er sich stark und kräftig erhält.",
        "Alles ist gefärbt von dieser oder jener Seite, von der medizinischen oder von der mehr der Naturheilkunde zuneigenden Richtung."
      ],
      [
        "Wenn wir uns einmal vor Augen führen, von welchen"
      ],
      [
        "Gesichtspunkten aus ein solcher Streit über Krankheit und Gesundheit zum Beispiel existiert zwischen den An­hängern der medizinischen Heilweise und den Anhängern der Naturheilkunde, dann hören wir die Anhänger der Naturheilkunde sagen, die Medizin suche für jede Krank­heit ihr bestimmtes Heilmittel und sei der Anschauung, daß die Krankheit etwas ist, was den Menschen wie etwas Äußerliches, wie durch eine äußerliche Ursache ergreift, und daß es für die Krankheit auch dieses oder jenes äußerliche Heilmittel gibt.",
        "Wir wollen bei solcher Charakteristik nicht vergessen, daß das, was da von der einen oder anderen Seite gesagt wird, oft über das Ziel hinausschießt, und wollen nicht vergessen, daß in vielen Dingen die beiden Parteien einander unrecht tun.",
        "Aber wir wollen einzelne Vorwürfe herausheben, die uns zur Verdeutlichung dienen können.",
        "Der Anhänger der Naturheilkunde wird hervor­heben, daß der Schulmediziner eine Entzündung in ge­wissen Fällen durch Eisumschläge lindere, daß man bei Gelenkrheumatismus durch Salizylsäure und so weiter zu helfen suche."
      ],
      [
        "Besonders weitgehende Anhänger der Naturheilkunde werden kräftige Vorwürfe erheben.",
        "Sie werden sagen: Wenn der Magen zuviel Magensäure absondert, dann werde der Mediziner versuchen, diese Magensäure zu neutralisieren.",
        "Der Naturheilkundige sagt, das gehe an dem tiefen Wesen der Krankheit und vor allem an dem tiefen Wesen des Menschen vorbei.",
        "Das alles treffe den Nagel nicht auf den Kopf.",
        "Nehmen wir an, der Magen sondert wirklich zuviel Magensäure ab, so sei das ein Beweis dafür, daß etwas im Organismus nicht richtig ist.",
        "Im richtig funktionierenden Organismus wird nicht zuviel Magensäure abgesondert.",
        "Wenn man daher die Magensäure, die abgesondert wird, neutralisiert, so hebt man damit noch nicht die Kraft auf,"
      ],
      [
        "die Tendenz, zuviel Magensäure zu schaffen.",
        "Man müsse also seine Aufmerksamkeit nicht darauf richten, die Magen­säure einfach zu beseitigen.- Das sagen diejenigen, die gegen die Schulmedizin polemisieren.",
        "Man würde, wenn man die Magensäure beseitigt, den Organismus geradezu aufstacheln, ja recht viel Magensäure zu erzeugen.",
        "Man müsse also tiefer-gehen und die eigentliche Ursache aufsuchen.",
        "So insbeson­dere wird der Naturheilkundige, wenn er es bis zum Fana­tiker bringt , wettern: Wenn jemand an Schlaflosigkeit leidet, so hilft man ihm so, daß man ihm Schlafmittel gibt.",
        "Schlaf­mittel beseitigen die Schlaflosigkeit für eine gewisse Zeit; aber die Ursache wird nicht beseitigt.",
        "Die müsse aber besei­tigt werden, wenn man dem Kranken wirklich helfen will."
      ],
      [
        "Unter denjenigen, die wieder mehr auf dem Arznei-standpunkte stehen, gibt es zwei Parteien: die Allopathen, die ein spezifisches Heilmittel gegen gewisse Krankheiten anführen und gebrauchen, sozusagen ein Heilmittel, welches die Aufgabe hat, diese Krankheit zu beseitigen.",
        "Sie gehen also von der Anschauung aus, die Krankheit sei eine Störung im Organismus, und diese Störung müsse durch ein Mittel beseitigt werden.",
        "Dagegen wenden die Homöopathen ein, das sei durchaus nicht das eigentliche Wesen der Krankheit, sondern das eigentliche Wesen der Krankheit sei eine Art Reaktion des ganzen Organismus gegen eine Schädlichkeit in demselben.",
        "Es sei eine Schädlichkeit aufgetreten im Orga­nismus, und nun wehre sich der ganze Organismus gegen diese Schädlichkeit.",
        "Man müsse an den Symptomen, die beim kranken Menschen auftreten, erkennen und darauf Rücksicht nehmen, daß dasjenige, was Fieber und so weiter erzeugt, eine Art Aufruf sei an die Kräfte im Organismus, die den eingeschlichenen Feind vertreiben können. - Daher werden sich die Anhänger dieser Art Heilweise sagen, man müsse gerade zu denjenigen Mitteln in der Natur greifen,"
      ],
      [
        "welche, wenn der gesunde Organismus sie zu sich nimmt, die betreffende Krankheit hervorrufen.",
        "Man dürfe natür­lich dann diese Mittel dem kranken Organismus nicht in großer Dosis verabreichen, sondern so, daß die Kraft der betreffenden Mittel gerade hinreicht, um im gesunden Or­ganismus die Krankheitserscheinungen hervorzurufen.",
        "Das ist das Prinzip der Homöopathie: dasjenige, was im gesun­den Organismus eine bestimmte Krankheit hervorrufen kann, das schließt auch die Möglichkeit in sich, den kranken Organismus zu einer bestimmten Gesundheit zu führen.",
        "Das wird angewendet, wenn der Organismus die Krank­heitserscheinungen durch sich selber zeigt.",
        "Man denkt das so: Man sieht, daß der Organismus, wenn er im kranken Zustande die Symptome zeigt, sich bemüht, die Krankheit zu überwinden.",
        "Deshalb müssen wir ihn mit diesem Mittel unterstützen."
      ],
      [
        "Daher kommt es, daß der homöopathische Arzt in vielen Fällen gerade das Gegenteil von dem anwenden wird, was der allopathische Arzt anwenden würde.",
        "Der Naturheil­kundige steht oftmals - nicht immer - auf dem Stand­punkte, daß es vor allen Dingen nicht darauf ankomme, ob irgendein spezifisches Heilmittel eine Krankheitsschädigung aufhebt, sondern darauf, den Organismus und seine Tätig­keit zu unterstützen, damit er seine inneren Gesundungs­kräfte wachruft, um dem Krankheitsprozeß zu begegnen.",
        "So wird der Naturheilkundige vor allen Dingen darauf bedacht sein, auch dem Gesunden zu raten, die Tätigkeit des Organismus zu unterstützen.",
        "Er wird zum Beispiel be­tonen, daß es auch für Gesunde weniger darauf ankomme, ob eine Nahrung dem Menschen besonders Gelegenheit gäbe, sagen wir, sich vollzupfropfen mit dem oder jenem, sondern ob eine Nahrung dem Menschen Gelegenheit gibt, seine inneren Kräfte so aufzurufen, daß sie in Tätigkeit"
      ],
      [
        "kommen.",
        "Die Funktion der Organe wird der Naturheil­kundige vor allem auch beim gesunden Menschen betonen.",
        "Er wird sagen: Du wirst dein Herz nicht kräftig machen, wenn du dich bemühst, es mit Aufpeitschungsmitteln fort­während anzuspornen, sondern du wirst dein schwaches Herz dadurch stärken, daß du es in Tätigkeit bringst, daß du Bergpartien machst. - So wird derjenige, der auf die Tätigkeit der Organe des Menschen ausgeht, auch dem ge­sunden Menschen anraten, seine Organe in sachgemäßer Art in Tätigkeit zu bringen."
      ],
      [
        "Sie werden vielleicht, wenn Sie sich um solche Fragen gekümmert haben, weil sie doch die heutige Gegenwart so viel beschäftigen, gesehen haben, mit welcher Heftigkeit und mit welchem Dogmatismus von der einen oder anderen Seite oft gekämpft wird, wie die eine und die andere Seite dasjenige hervorhebt, was sie für ihre Anschauung vorzu­bringen hat.",
        "So kann die sogenannte Schulmedizin hin­weisen darauf, wie sie im Laufe der letzten Jahrzehnte, namentlich im Verlaufe der letzten drei bis vier Jahrzehnte, großartige Fortschritte gemacht hat gerade dadurch, daß sie darauf gesehen hat, wie die äußeren Krankheitserreger an die Menschen herankommen und sozusagen ihre Gesundheit vernichten.",
        "Diese Schulmedizin kann darauf hinweisen, wie sie besorgt war darum, die äußeren Lebensverhältnisse, die Zustände des Lebens so zu verbessern, daß in der Tat in der letzten Zeit ein Aufschwung eingetreten ist.",
        "Gerade diejenige Richtung der Medizin, die vorzugsweise auf die äußeren Krankheitserreger sieht - sagen wir auf die heute so gefürchtete Bakterien- und Bazillenwelt -, sie hat da­durch, daß sie auf dem Gebiete der Hygiene und der sani­tären Einrichtungen eingegriffen hat, in einer für die Laien gar nicht so durchschaubaren Weise, ungeheuer viel getan für die Verbesserung der Gesundheitsverhältnisse."
      ],
      [
        "Es wird gewiß - wiederum nicht ganz mit Unrecht, aber auch nur mit einseitigem Recht - von mancher Seite betont, wie diese Schulmedizin geradezu eine Bakterien- und Ba­zillenfurcht hervorgerufen hat.",
        "Aber auf der anderen Seite hat die Untersuchung dazu geführt, daß die Gesundheit im Laufe der letzten Jahrzehnte sich gebessert hat."
      ],
      [
        "Mit Stolz weist der Anhänger dieser Richtung darauf hin, um wieviel Prozent die Sterblichkeit da oder dort in den letzten Jahr­zehnten tatsächlich abgenommen hat.",
        "Diejenigen aber, die sagen, daß es nicht so sehr die äußeren Ursachen sind, welche für die Betrachtung der Krankheit wichtig sind, sondern daß es vor allen Dingen die im Menschen liegenden Ur­sachen sind, sozusagen seine Krankheitsdisposition, sein vernünftiges oder unvernünftiges Leben, die werden wieder besonders betonen, daß in den letzten Zeiten zwar unleug­bar die Sterblichkeitsziffern abgenommen haben, daß aber die Krankheitsziffern in einer erschreckenden Weise zu­genommen haben."
      ],
      [
        "Es wird betont, wie gewisse Krankheits­formen zugenommen haben: Herzkrankheiten, Krebskrank­heiten, Krankheitsformen, die in den Schriften der älteren Zeit gar nicht verzeichnet sind, Krankheiten der Ver­dauungsorgane und so weiter.",
        "Diejenigen Gründe, die von der einen oder anderen Seite hervorgebracht werden, sind durchaus beachtenswert."
      ],
      [
        "Es kann von einem oberflächlichen Standpunkte aus nicht eingewendet werden, die Bazillen oder Bakterien seien nicht Krankheitserreger furchtbarster Art.",
        "Es kann aber auf der anderen Seite auch nicht geleug­net werden, daß der Mensch in gewisser Beziehung entweder gefestigt und gesichert ist gegen Einflüsse solcher Krank­heitserreger oder es nicht ist."
      ],
      [
        "Er ist es nicht, wenn er sich durch unvernünftige Lebensweise um seine Widerstands­kraft gebracht hat."
      ],
      [
        "In vieler Beziehung sind diejenigen Dinge bewundernswert,"
      ],
      [
        "welche von der Schulmedizin in der letzten Zeit ge­leistet worden sind.",
        "Sehen wir doch einmal zu, wie subtil und fein die Untersuchungen über das gelbe Fieber sind im Zusammenhange mit der Art und Weise, wie es durch ge­wisse Insekten von Mensch zu Mensch übertragen wird."
      ],
      [
        "Wie vorzüglich sind die Untersuchungen in bezug auf die Mala­ria und ähnliches!",
        "Aber auf der anderen Seite können wir sehen, daß berechtigte Ansprüche dieser Schulmedizin sehr leicht unser ganzes Leben durchkreuzen können, was in ge­wisser Beziehung zu einer Tyrannis führen kann."
      ],
      [
        "Denken wir, daß - und zwar mit einem gewissen Recht - behauptet wird, in einer in der letzten Zeit häufig auftretenden Krank­heit, in der Genickstarre, werde durchaus nicht der Krank­heitserreger auf einen anderen Menschen übertragen, son­dern Menschen, die ganz gesund sind, die ganz fernstehen dem, was man mit Genickstarre bezeichnet, könnten in ge­wisser Beziehung die Krankheitskeime in sich tragen und sie auf andere Menschen übertragen, so daß Menschen, die unter uns herumgehen, die Träger von Krankheitskeimen seien, von denen dann der, welcher dazu geeignet ist, die Krankheit bekommen kann, während die anderen, welche die Keime tragen, durchaus nicht von der Krankheit be­fallen zu werden brauchen. - So kann es dahin kommen, daß die Forderung aufgestellt wird, die Krankheitskeim­träger zu isolieren; denn wenn irgendeiner an Genickstarre erkrankt ist, so sei er gar nicht einmal so gefährlich wie die­jenigen, welche ihn pflegen, und die vielleicht die eigent­lichen Krankheitsträger sind.",
        "Zu welchen Konsequenzen das führen muß, wenn man diesen Menschen den Umgang er­schweren wird, das mag man daraus erkennen: Man kann anführen - und es ist schon angeführt worden -, daß an irgendeiner Schule plötzlich eine größere Anzahl von Kin­dern an dieser oder jener Krankheit erkrankt ist."
      ],
      [
        "wußte nicht, woher die Krankheit gekommen ist.",
        "Da stellte sich heraus, daß die Lehrer die eigentlichen Krankheitsträger waren.",
        "Sie selber sind nicht von der Krankheit befallen worden, aber die ganze Schule ist von ihnen angesteckt worden.",
        "Der Ausdruck Bazillenträger oder Bazillenfänger ist ein Ausdruck, der von einer gewissen Seite sogar mit einem gewissen Recht gebraucht werden kann.",
        "Daß der­jenige, welcher Laie ist, auf diesem Gebiete, in allem, was ihm entgegentreten kann von dieser oder jener Seite, sich recht wenig auskennt, das ist schon aus dem wenigen, was wir anführen konnten, fast selbstverständlich."
      ],
      [
        "Nun müssen wir sagen: Gerade das, was wir am Ein-gange unserer heutigen Betrachtung ausgeführt haben, müßte ein Leitfaden sein dafür, was eigentlich aus alledem, was an guten Gründen von der einen oder anderen Seite vor­gebracht wird, wirklich zum Heile führen kann.AlsGrund­satz im tiefsten und bedeutsamsten Sinne muß gelten, daß vor allen Dingen vor uns stehen muß die Individualität des Menschen als eine einzelne Realität, als etwas, was anders ist als jeder andere Mensch.",
        "Wir werden uns das sozusagen an einem konkreten Beispiel am besten vor die Seele führen.",
        "Nehmen wir einen Menschen an - ich erzähle Dinge, die durchaus vorgekommen sind -, der hatte von Kindheit auf einen gar nicht zu bezwingenden Widerwillen gegen alles, was Fleisch heißt.",
        "Er konnte Fleisch nicht ausstehen, nicht essen.",
        "Auch nicht das konnte er essen, was irgendwie mit Fleisch im Zusammenhang steht.",
        "Er entwickelte sich ganz gesund bei seiner Pflanzenkost.",
        "Das ging so lange, bis sich wohlwollende, gute Freunde fanden, die all ihre Energie einsetzten, um diesen Menschen doch von seiner paradoxen Empfindung abzubringen.",
        "Sie waren es, die ihm zuerst an-rieten, sozusagen ihm zusetzten, zunächst es einmal mit ein wenig Fleischbrühe zu versuchen.",
        "Immer weiter und weiter"
      ],
      [
        "wurde er getrieben, bis zum Hammelfleisch.",
        "Er fühlte sich dabei immer kränker und kränker.",
        "Nach einiger Zeit trat bei ihm auf eine Erscheinung wie ein besonderer Überfluß des Blutes.",
        "Es trat auf eine eigentümliche Schlafsucht, und der gute Mann ging zugrunde an einer Gehirnentzündung.",
        "Hätte man diesen Menschen nicht jeden Tag aufs neue dar­auf aufmerksam gemacht, was er eigentlich essen solle, hätte man ihn bei seinem gesunden Trieb gelassen, hätte man nicht geglaubt, «eines schicke sich für alle», hätte man sich nicht auf einen Dogmatismus eingeschworen, sondern die individuelle Natur des Menschen respektiert, dann wäre er gesund geblieben."
      ],
      [
        "Aus einem solchen Fall sollen wir aber nicht mehr lernen, als die individuelle Natur des Menschen zu respektieren.",
        "Wir sollen nicht ein neues Dogma davon ableiten; wir sol­len im Leben einzig davon profitieren.",
        "Wenn wir uns über­legen, wodurch in diesem Falle der Tod herbeigeführt wurde, so können wir uns die Frage in folgender Art beantworten.",
        "Wenn Sie sich erinnern, was das letzte Mal im Vortrage über die Ernährungsfragen gesagt worden ist, so können wir daraus entnehmen, was man für die Pflanze Lebens-prozeß nennt: die Pflanze verarbeitet leblosen Stoff in lebendigen Organismus.",
        "Im menschlichen Organismus wird dieser Prozeß weitergeführt.",
        "In gewisser Beziehung ist das­jenige, was der menschliche und auch der tierische Organis­mus tut, ein Abbau dessen, was die Pflanze aufgebaut hat.",
        "Darauf beruht gerade in bestimmter Beziehung der mensch­liche und der tierische Leib, daß abgebaut und zerstört wird, was die Pflanze aufgebaut hat."
      ],
      [
        "Nun kann ein Organismus so eingerichtet sein, daß er so­zusagen gerade den Punkt für sich verlangt, da zu begin­nen, wo die Pflanze mit ihrer Tätigkeit aufgehört hat.",
        "Dann kann es für ihn im eminentesten Sinne schädlich sein, wenn"
      ],
      [
        "er den Teil des Prozesses, den das Tier mit den Pflanzen­produkten bereits besorgt hat, sich abnehmen läßt.",
        "Das Tier führt den Pflanzenprozeß bis zu einem gewissen Punkte.",
        "Der Mensch kann ihn dann nur fortsetzen, wenn er tierische Nahrung genießt.",
        "Wenn ihm das abgenommen wird und seine Natur gerade über die Kräfte verfügt, welche die Pflanzen-nahrung frisch und kräftig aufnehmen und sie dann weiter­führen, dann wird er in sich Kräfte haben, die jetzt unver­wendbar sind für irgendeine Nahrungsaufnahme und Nah­rungsverarbeitung.",
        "Diese Kräfte sind da.",
        "Diese schaffen wir deshalb nicht weg dadurch, daß wir ihnen nichts zu tun geben, denn dann werfen sie sich auf etwas anderes.",
        "Sie wirken im Inneren des menschlichen Organismus.",
        "Die Folge davon ist, daß sie als überschüssige Tätigkeit den Organis­mus im Inneren zerstören."
      ],
      [
        "Man sieht, wenn man einen geisteswissenschaftlich nur wenig geschärften Blick hat, wie die überstürzende Tätig­keit, die den ganzen Menschen eingenommen hat, sich auf sein Blut und sein Nervensystem wirft.",
        "Man sieht, wie es in dem Organismus so ausgesehen hat, wie bei einem Haus-bau, in den man ungeeignetes Material hineingeworfen hat, so daß man sich bemühen muß, das ungeeignete Material zu ordnen und zu arrangieren.",
        "Nicht ungestraft leitet man die Kräfte der Verarbeitung der Nahrungsstoffe nach dem Innern.",
        "Wenn wir uns das klarmachen, dann werden wir tolerant werden gegen die Natur.",
        "Dann dürfen wir aber jedenfalls nicht in der entgegengesetzten Richtung wieder zum Schablonisieren kommen und Fanatiker werden des Vegetarismus für einen jeden Menschen.",
        "Gerade so, wie sich bei dem Manne, den ich gestern als radikales Beispiel ange­führt habe, die nach innen abgelenkte Tätigkeit überstürzte, so kann es auf der anderen Seite sein, daß es Menschen gibt, welche über diese Tätigkeit gar nicht verfügen, die sozusagen"
      ],
      [
        "den Pflanzenprozeß unmittelbar da, wo er aufgehört hat, nicht fortsetzen können.",
        "Solche Menschen werden, wenn man ihnen zumutet, ohne weiteres Vegetarier zu werden, erleben, daß sie die Kräfte, welche sie da brauchen, not­dürftig aus dem eigenen Organismus nehmen müssen.",
        "Sie werden diesen dadurch in gewisser Weise verzehren und ihm zum Verhängnis werden.",
        "Das kann also durchaus auf der anderen Seite vorliegen.",
        "Worum es sich handelt, ist, daß wir den Blick abwenden von diesen oder jenen Dogmen, wenn wir von gesunden und kranken Verhältnissen reden, abwenden davon, dieses oder jenes zu essen oder es in dieser oder jener Weise zu bearbeiten.",
        "Das, worauf es ankommt, ist, die Bedürfnisse des einzelnen Menschen kennenzulernen.",
        "Es kommt vor allem darauf an, daß dieser einzelne Mensch die Möglichkeit hat, in gewisser Beziehung seine Bedürf­nisse selber zu fühlen und zu erkennen."
      ],
      [
        "Wenn eine materialistische Anschauung gar zu sehr auf das bloß Stoffliche sieht, so wäre es doch für diese materia­listische Anschauung notwendig, nach dieser Richtung hin sich zu bewegen, die eben jetzt angedeutet worden ist.",
        "Ge­rade für sie wäre es unmöglich, zu schablonisieren und zu vereinheitlichen.",
        "Und wie schablonisiert man in unserer heutigen Zeit!",
        "Da wird zum Beispiel ohne weiteres gesagt, dieses oder jenes Nahrungsmittel oder diese oder jene Arz­nei sei schädlich.",
        "Es ist eine förmliche Epidemie derartiger Schablonen ausgebrochen.",
        "Es ist daher nichts anderes mög­lich, als jede Einseitigkeit auszuschließen.",
        "Es ist ausgebro­chen eine Epidemie unter dem Stichwort «Kraft», so daß man in den naturheilkundlichen Versammlungen sagt, das Leiden sei eine Kraft.",
        "Damit glaubt man, genug getan zu haben, um dies oder jenes anzuschwärzen.",
        "Gerade die, welche nur ausgehen sozusagen von der Materie, statt in erster Linie den Menschen als Individualität zu betrachten, die"
      ],
      [
        "sollten darauf Rücksicht nehmen, wie dann, wenn man zum Beispiel die anderen Lebewesen überblickt, das Wort Kraft im Grunde genommen jeden Sinn verliert.",
        "Unsere Anschau­ungen in bezug auf solche Dinge müssen sich da modifizie­ren.",
        "Wer würde da nicht daran denken, daß für den Men­schen eine besondere Kraft zu bezeichnen ist!",
        "Die Kaninchen fressen ohne Schaden den Schierling.",
        "Sokrates starb daran.",
        "Andere sagen: Akonit - Eisenhut - kann ich nehmen.",
        "Die Pferde können es auch fressen. - Bei all diesen Dingen müs­sen wir also, wenn wir sie regelrecht betrachten, uns immer die Organisation vorhalten.",
        "Wenn wir uns die Organisation vorhalten, so können wir sagen: Im kleinen, also homöo­pathisch, ist es richtig für die Menschennatur.",
        "Eines schickt sich nicht für alle!"
      ],
      [
        "Die Frage ist also: Wie kann der Mensch einen Maßstab für seine Gesundheit in sich selber gewinnen?",
        "Ein gewisser Leuchtturm könnte uns das Kind sein.",
        "Wir müssen uns da­her durchaus vorhahen, daß das Kind in ganz bestimmter Weise seine Sympathie oder Antipathie für dieses oder jenes Nahrungsmittel äußert.",
        "Das sorgfältige Beobachten dieser Dinge würde für jeden von uns von außerordentlicher Wichtigkeit sein.",
        "Es ist manchmal durchaus verfehlt, wenn derjenige, der das Kind zu lenken und zu erziehen hat, die Instinkte, die da beim Kinde auftreten und sich als be­stimmtes Wollen äußern, austreiben will, wenn man sie als Ungezogenheit betrachtet.",
        "Vielmehr ist es so: Was das Kind als Trieb, als Instinkt äußert, ist ein Anzeichen dafür, wie die innere Natur des Kindes geartet ist.",
        "Was das Kind emp­findet und was ihm schmeckt, wonach es Verlangen hat, da ist die Empfindung, das Verlangen nichts anderes als der Ausdruck dafür, daß der Organismus gerade dieses oder jenes verlangt.",
        "Ja, ein Fingerzeig, oder, wenn wir radikaler sprechen wollen, ein Leuchtturm für die Erkenntnis kann"
      ],
      [
        "uns dieser leitende Instinkt des Kindes sein.",
        "Wir können das ganze Leben durchwandern und werden überall die Notwendigkeit finden, daß der Mensch in gewisser Be­ziehung gerade diese innere Sicherheit in sich entwickeln muß für das, was sein Organismus braucht.",
        "Das ist unbe­quemer, als sich von dieser oder jener Partei die Richtung vorschreiben und sich sagen zu lassen, was für alle Menschen das Gute ist.",
        "Die Menschen haben es nicht so leicht wie die, welche mit einem bestimmten allgemeinen Rezept kommen, das man sich nur in die Tasche zu stecken braucht, um zu wissen, was den Menschen gesundmachen und was ihn krankmachen kann.",
        "Gerade wenn man mit einem solchen Leitfaden die Gesundheit betrachtet, wird man auch in be­zug auf die Krankheit sich klarmachen müssen, daß für die verschiedenen Menschen die verschiedensten Bedingungen für Gesundheit und Heilung vorliegen."
      ],
      [
        "Nehmen wir an, jemand habe Migräne.",
        "Wer dogmatisch auf dem Standpunkt steht - wenn auch die Schulmedizin dies nicht mehr wahrhaben will -, daß es spezifische Heil-mittel gibt für diese oder jene Krankheit, der wird sagen:"
      ],
      [
        "Man gebe dem Kranken bestimmteHeilmittel gegen Migräne.",
        "Der Kranke wird sich wohler fühlen, und die Migräne wird verschwinden. - Wer auf dem Standpunkte der Naturheil-kunde steht, wird sagen, wenn er es zum Fanatiker gebracht hat, man kann so nur das Symptom bekämpfen.",
        "Man hat manchem damit mehr geschadet als genützt. - Eine andere Richtung sagt: Es komme darauf an, daß man auf die tiefe­ren Ursachen einwirke.",
        "Und dann wird man mit allerlei Dingen kommen, die vielleicht mehr auf den Kern der Sache eingehen, aber im einzelnen Fall nicht so schnell ein Wohl­befinden herstellen, die aber wirklich tiefer auf den Krank­heitskern eingehen.",
        "Man wird, wenn man sich dogmatisch auf den einen oder anderen Standpunkt stellt, das eine oder"
      ],
      [
        "das andere bekämpfen oder für nützlich halten.",
        "Es handelt sich aber dabei, so sonderbar es klingen wird, wiederum um den Menschen.",
        "Es könnte einen Menschen geben, der sich sagte: Es wäre ganz schön, wenn ich ein Hilfsmittel bekom­men könnte und nicht zu warten brauchte, bis die Natur­heilkunde dem Kern der Sache beigekommen ist, um dann dasjenige zu tun, was es möglich macht, die Krankheit in ihren tieferen Wurzeln zu erkennen und zu beheben.",
        "Aber dazu habe ich keine Zeit.",
        "Es ist für mich viel wichtiger, daß ich die Migräne so bald wie möglich loskriege und meiner Tätigkeit zurückgegeben werde."
      ],
      [
        "Nehmen wir ferner an, dieser Mensch habe eine die Ge­sundheit fördernde Beschäftigung.",
        "Diese sei so geartet, daß er, wenn er durch das Migränemittel das Übel losbekommen hat, sich der günstigen Wirkung der Arbeit hingeben kann.",
        "Dann wird ihm das Migränemittel wenig schaden.",
        "Er wird wenig aus seiner Tätigkeit gerissen sein, die ihm nützt.",
        "Dann wird er nach einem Rezept einer Medizin suchen, die ihn in diesem Zustand erhält."
      ],
      [
        "Dieser Vergleich muß aber bis zu Ende geführt werden.",
        "Man darf nicht vergessen, daß einer da sein muß, der da arbeitet, wie der Führer auf der Lokomotive.",
        "Nehmen wir an, bei einer Lokomotive zeige sich, daß eine Kurbel beson­ders schwer geht.",
        "Da kann jemand sagen: Daran sehe ich, daß dieser Lokomotivführer diese Kurbel nicht treiben kann, weil er zu schwach ist.",
        "Ich werde einen anderen Loko­motivführer nehmen, der mehr Kräfte anwenden kann, um die Kurbel zu treiben. - Ich will jetzt auf das Zentrum der Sache eintreten.",
        "Ein anderer sagt: Man kann ja vielleicht das, was die Kurbel schwer zu drehen macht, ein wenig aus-feilen, damit die Kurbel leichter geht.",
        "Dann kann der Zug-führer bleiben. - Man bessert also die Maschine aus.",
        "Natür­lich darf man das nicht als ein allgemeines Rezept anwenden."
      ],
      [
        "Wenn man sagen wollte: Wenn der Lokomotive etwas fehlt, so muß man daran feilen -, so braucht das nicht immer richtig zu sein.",
        "Der betreffenden Lokomotive kann es auch abträglich sein.",
        "Man muß also feststellen, ob man das tun darf.",
        "Damit hat man den Schaden einfach ausgebes­sert.",
        "Wenn der Betreffende die innere Kraft hat, so wird er, wenn er nicht gestört wird, schon selbst die Sache wieder in Ordnung bringen."
      ],
      [
        "Freilich würde es unter Umständen schlimm sein, wenn man in derselben Weise dächte gegenüber jemand, der die Migräne loshaben will, aber hinterher nicht zu einer mit seiner Tüchtigkeit zusammenhängenden Tätigkeit geht.",
        "Er würde besser getan haben, wenn er die innere Ursache weg­geräumt hätte.",
        "So müssen wir also durchaus auch in diese Materie eingedrungen sein, da es ja für das, was man Krank­heit nennt, spezifische Heilmittel gibt.",
        "Die Anwendung spe­zifischer Heilmittel hängt in gewisser Beziehung damit zu­sammen, daß unser Organismus ein selbständiges Wesen ist und in vieler Richtung ausgebessert werden kann, wenn man sich darauf verlassen darf, daß nach der Ausbesserung eine recht tüchtige Kraft vorhanden ist, die den Menschen antreibt.",
        "Das braucht man nicht zu betonen.",
        "Man treibt dann eben nur eine Symptom-Kur, denkt aber eben doch nur materialistisch.",
        "Der Naturheilkundige wird manches wissen, was ganz richtig wäre zur Beseitigung dieser oder jener Krankheit, aber ebenso wahr ist es, daß dieser oder jener Mensch nicht die Zeit und nicht die Kraft hat, es durchzuführen, und daß es sich vor allen Dingen für ihn darum handelt, den Schaden wieder gutzumachen."
      ],
      [
        "Sie sehen, daß hier nicht in einseitiger, sondern in all­seitiger Weise gesprochen werden muß.",
        "Wenn man die Un­bequemlichkeit mit in Kauf nimmt, so genügt es nicht, Theo­retiker zu sein, sondern man muß auf die Tatsachen eingehen"
      ],
      [
        "und hat auf den ganzen Menschen zu sehen.",
        "Darauf kommt es an.",
        "Wenn wir so sprechen, müssen wir uns dar­über klar sein, daß wir dann, wenn wir den Menschen als Realität betrachten wollen, den ganzen Menschen ins Auge fassen müssen.",
        "Der ganze Mensch ist für die Geisteswissen­schaft nicht bloß der äußere physischeLeib, namentlich dann nicht, wenn unsere Gesundheit nicht bloß durch äußere, sondern durch innere Ursachen zerstört ist.",
        "Was viel mehr in Betracht kommt, ist die Gesundheit des Ätherleibes, der ein Kämpfer ist gegen die Krankheit bis zum Tode.",
        "Dann ist der Astralkörper da, ein Träger der Leidenschaften, Triebe, Begierden und Vorstellungen, und endlich der Ich-Träger, der macht, daß derMensch ein selbstbewußtes Wesen ist.",
        "Wer auf den ganzen Menschen Rücksicht nehmen will, der muß auf die vier Glieder durchaus Rücksicht nehmen, und wenn die Frage nach der Gesundheit in Betracht kommt, so handelt es sich nicht nur darum, daß wir Störungen be­rücksichtigen, die den physischen Leib betreffen, sondern auch das betrachten, was in den höheren Gliedern, in den mehr seelisch-geistigen Gliedern, vor sich geht.",
        "Da müssen wir feststellen, daß nicht bloß von dieser oder jener Partei-schattierung, sondern von unserer ganzen zeitgenössischen Gesinnung gesündigt wird."
      ],
      [
        "Sehr selten wird die Frage gestellt: Wie hängt die Ge­sundheitsfrage mit den seelisch-geistigen Dingen zusam­men?",
        "Man wird heute viel Zustimmung finden, wenn man davon spricht, wieviel dieses oder jenes Nahrungsmittel Brennwert hat, wie dieses oder jenes Nahrungsmittel im Organismus wirkt.",
        "Man wird auch viel Zustimmung haben, wenn man auseinandersetzt, wie die Luft in dieser oder jener Gegend ist, wo dieses oder jenes Sanatorium sich be­findet, wie die Luft und auch das Licht da oder dort wirkt.",
        "Aber nicht wird man finden Anklang, wenn man seelische"
      ],
      [
        "Eigenschaften als Ursache bestimmter Erklärungen angibt.",
        "Nehmen wir die Instinkte des Kindes, wie sie sich aus­drücken in Sympathie und Antipathie gegenüber diesem oder jenem Nahrungsmittel.",
        "Wir nehmen zunächst als An-zeiger das Ekelgefühl, mit dem sie dies oder jenes zurück­weisen.",
        "Es weist darauf hin, daß das, was in sich gesund­heitliches Sein ist, was zugrunde liegt dem physischen Leibe"
      ],
      [
        "- der Astralleib, der aus Gefühlen und Empfindungen, Im­pulsen und Begierden besteht -, daß auch das Geistig-See­lische gesund sein muß, und daß, wenn eine Abweichung von dem Gesunden im Menschen erblickt wird, man auf die Gesundung des astralischen Leibes achten muß.",
        "Frägt man heute wirklich noch, wenn diese Fragen in Betracht kom­men, was des Menschen Seele erlebt gegenüber der Außen­welt?",
        "Der Geisteswissenschaftler muß darauf hinweisen, daß es im Grunde genommen wenig darauf ankommt, ob man einen Menschen, der an diesem oder jenem krankt, da oder dorthin schickt, weil man glaubt, die Luft oder das Licht werde aus äußeren mechanischen oder chemischen Gründen gesundend auf ihn wirken.",
        "Eine andere, viel grö­ßere Frage ist es, ob ich ihn in eine solcheUmgebung bringen kann, daß er Freude, Erhebung, in gewisser Beziehung eine Durchleuchtung seines ganzen Gefühlslebens nach einer be­stimmten Richtung erfahren kann.",
        "Wenn wir dies im großen betrachten, so werden wir auch verstehen, daß es zu dem Ge­sundsein gehört, wenn dem Menschen eine Speise schmeckt, daß der Mensch sozusagen in seinem Geschmacke, in der unmittelbaren Geschmacksempfindung, in der Annehmlich­keit und Freude, die ihm die Speise bereitet, einen Grad­messer haben muß für dasjenige, was er essen soll, und daß der Mensch auf der anderen Seite an dem richtig auftreten­den Hungergefühl einen Gradmesser haben soll dafür, wann sein Organismus essen soll."
      ],
      [
        "Es sind nicht bloß von der materiellen Welt her kom­mende Einflüsse, welche diese innere Sicherheit im Menschen zerstören, es sind in den weitaus meisten Fällen durchaus auch Einflüsse aus dem geistigen Leben, welche in dem Men­schen die Sicherheit des Hungertriebes untergraben.",
        "Statt dem Menschen im richtigen Moment einen gesunden Hunger beizubringen, läuft die geistige Natur so ab, daß dieser Hunger nicht da ist, sondern Appetitlosigkeit.",
        "Ein Mensch, der die Bedürfnisse seines Organismus in der richtigen Weise entwickelt hat, so daß ihm das Richtige schmeckt und sym­pathisch ist und auch seinem Organismus dienen kann, ein solcher wird auch das richtige sympathische Gefühl haben, um die richtige Umgebung, die seiner Gesundheit dient in bezug auf Licht und Luft, zu finden, so daß ihm zur rich­tigen Zeit der Hunger danach kommt."
      ],
      [
        "Das sind Forderungen, die einen Zusammenhang mit dem gesundheitlichen Leben haben und die zu dem hinführen, was der astralische Leib und das Ich beizutragen haben zu dieser Gesundheit.",
        "Leicht wird der Einwand gemacht: wenn jemand Hunger habe, könne er nicht von dem Gefühle und von der Empfindung leben.",
        "Das ist wahr.",
        "Auch wenn man ihm eine leckere Speise vorsetzt, so daß ihm unter Umstän­den das Wasser im Munde zusammenfließt, kann man ihn nicht sättigen, indem man ihm imaginäre Geschmacksfreu­den beschafft.",
        "Leicht ist dieser Einwand zu machen.",
        "Was wir ihm geben können an dem, was seine Seele so beeinflußt, daß sie in richtiger Weise die Empfindungen und Vorstel­lungen ablaufen läßt, das ist ganz gut; daß wir ihn dadurch nicht sättigen und gesundmachen können, ist selbstverständ­lich.",
        "Aber was dabei übersehen wird, ist ein anderes.",
        "Nicht die Nahrung können wir regulieren, wohl aber den Ge­schmack regeln bis zum Hungergefühl.",
        "Hier mündet das, was sich heute zersplittert' weil es nur vom Standpunkte"
      ],
      [
        "äußerlicher, stofflicher Betrachtung gehandhabt wird, ein in das Geistig-Seelische; es mündet so ein, daß wir das geistig-seelische Leben treffen."
      ],
      [
        "Es ist nicht einerlei, ob der Mensch diese oder jene Speise mitLust zu sich nimmt, ob er in dieser oder jener Umgebung lebt, diese oder jene Arbeit verrichtet, oder ob er sie mit Unlust tut.",
        "Damit hängt in geheimnisvoller Weise, mehr als mit irgend etwas anderem, das zusammen, was man seine innere Gesundheitsdisposition nennt.",
        "Wenn wir beim Kinde sehen, daß es richtige Instinkte entwickelt, und wenn man die Möglichkeit hat, seine inneren Instinkte zu beobachten, die es gradmäßig haben muß, so ist es notwendig, daß das Erwachen des Geistig-Seelischen so lebt, daß die richtigen Bedürfnisse zur rechten Zeit vor die Seele hintreten.",
        "So ist es notwendig, daß der Mensch fühlt und empfindet, was für ein Verhältnis er herstellen soll zwischen sich und der Außen-welt.",
        "Das Leben ist im weitesten Umfange geeignet, den Menschen in Irrtum über Irrtum zu bringen über dieses sein Verhältnis zur Außenwelt.",
        "Und gerade unsere heutige Gei­stesrichtung ist in mehr als einer Richtung die Veranlassung solcher Irrtümer."
      ],
      [
        "Damit wir uns besser verstehen, möchte ich auf den klei­nen Anfang hinweisen, den wir mit einer bestimmten Heil-weise gemacht haben.",
        "In München wird von einem unserer geisteswissenschaftlichen Genossen eine Art von Kur- oder Heilweise versucht, wie sie sich ergibt aus den Anschau­ungen der Geisteswissenschaft heraus.",
        "Wer heute glaubt, auf den Menschen könnten in gesundem Sinne wirken nur stoff­liche, physisch-chemische und physiologische Einflüsse, der wird erstaunt sein, daß die Menschen in eine besonders eigenartig gefärbte Kammer geführt werden, und daß da durch die Kräfte einer gewissen Farbe und durch andere Dinge, die hier nicht weiter erörtert werden können, auf"
      ],
      [
        "die menschliche Seele gewirkt wird.",
        "Allerdings kann dabei nicht auf die Oberfläche gewirkt werden.",
        "Da müssen Sie aber sehen den Unterschied zwischen dieser Wirkungsweise in den Kammern, also einer Art Kammer-Therapie, einer Art Farben-Therapie, und dem, was man Licht-Therapie nennt.",
        "Wenn der Mensch mit Licht bestrahlt wird, so liegt dem der Gedanke zugrunde, das Licht, das physische Licht, unmittelbar wirken zu lassen, so daß man sich sagt, wenn man diesen oder jenen Lichtstrahl auf den Menschen wir­ken läßt, so werde durch die Wirkung von außen auf den Menschen gewirkt.",
        "Darauf wird bei der erwähnten Farben-Therapie nicht Rücksicht genommen."
      ],
      [
        "Bei dieser der Geisteswissenschaft entnommenen Heil-weise, die unser Freund Dr.",
        "Peipers eingerichtet hat, ist nicht darauf gerechnet, was die Lichtstrahlen als solche, un­abhängig von der menschlichen Seele, auf den Menschen bewirken, sondern es ist Rücksicht darauf genommen, was als Vorstellung einer Seele - sagen wir unter Einwirkung der blauen Farbe, nicht des Lichtes - auf dem Umwege durch die Seele bewirkt wird.",
        "Es ist beabsichtigt, dadurch auf den ganzen körperlichen Organismus zurückzuwirken."
      ],
      [
        "Diesen gewaltigen Unterschied zwischen dem, was man sonst Licht-Therapie nennt, und dem, was man hier Farben-Therapie nennen kann, muß man ins Auge fassen.",
        "Es kommt dazu, daß gewisse Kranke ausgefüllt sind mit dem Inhalte einer ganz bestimmten Farbenvorstellung.",
        "Man muß wis­sen, daß Farben in sich Kräfte enthalten, die dann in Er­scheinung treten, wenn sie uns nicht nur bestrahlen, sondern in unserer Seele wirken.",
        "Man muß wissen, daß gewisse Far­ben etwas sind, das fördernd wirkt, daß eine andere Farbe etwas ist, was Sehnsuchtskräfte auslöst, daß eine dritte Farbe etwas ist, was die Seele über sich selbst erhebt, und eine andere Farbe etwas, das die Seele unter sich herunterdrückt."
      ],
      [
        "Wenn wir auf diese physisch-geistige Wirkung sehen, dann wird sich uns zeigen, was der Urgrund des Physischen und Ätherischen ist: daß unser astralischer Leib der eigentliche Bildner des Physischen und Ätherischen ist.",
        "Das Physische ist nur eine Verdichtung des Geistigen, und das Geistige kann wieder zurückwirken auf das Physische, wenn es in der richtigen Weise durchwirkt und durchlebt wird.",
        "Dann werden wir uns den Grundgedanken, der einer solchen Sache zugrunde liegt, vor Augen führen können, so daß wir auch Hoffnung haben dürfen dadurch, daß wir wieder eine Wis­senschaft haben, die hinweist darauf, wie im Menschen Gei­stig-Seelisches lebt und daß durch die Krankheit im Geistig-Seelischen sich die Störung als Krankheit im Physischen ausdrückt."
      ],
      [
        "Wer sich das klarmacht, wird hinsichtlich der Gesund­heitsfragen auf die Geisteswissenschaft hoffen dürfen.",
        "So leicht es ist, zu sagen: Mit Weltanschauung könnt ihr einen Menschen nicht füttern, - so ist es doch auch wahr, daß von der Weltanschauung die Gesundheit des Menschen abhängt.",
        "Für die heutige Menschheit ist das ein Paradoxon, für die Zukunft eine Selbstverständlichkeit!",
        "Ich will es noch ein wenig weiter erörtern.",
        "Man kann sagen: Der Mensch muß auf die reine objektive Wahrheit kommen, er muß sie be­greifen, muß sie zu genauen Abbildern der äußeren physi­schen Tatsachen machen. - Eine solche Forderung kann man als Theoretiker aufstellen.",
        "Man kann einen Menschen als Ideal hinstellen, der sich bemüht, nur das zu denken, was die Augen sehen, die Ohren hören und die Hände betasten können.",
        "Da kommt nun die Geisteswissenschaft und sagt:"
      ],
      [
        "Ihr könnt das, was wirklich ist, niemals begreifen, wenn Ihr nur auf das geht, was äußerlich wahrnehmbar ist, was die Augen sehen, die Ohren hören, die Hände greifen kön­nen.",
        "Was wirklich ist, enthält das Geistige als Urgrund."
      ],
      [
        "Geistige kann man nicht wahrnehmen.",
        "Man muß es durch Mitproduktion des Geistigen und Seelischen erleben.",
        "Zum Geistigen braucht man produktive Kräfte.",
        "Der Geistes-wissenschaftler ist, wenn er von dem eigentlichen Teile sei­ner Wissenschaft spricht, nicht immer in der Lage, hand­greiflich vorzuführen, was zu seinen Begriffen führt.",
        "Er schildert dasjenige, was nicht mit Augen, Ohren oder Hän­den gefaßt werden kann, weil es mit den Augen des Geistes verfolgt werden muß.",
        "Da kann man dann sagen: Das ist ja eine Schilderung von etwas, das es in der sinnlichen Welt gar nicht gibt.",
        "Für uns ist Wahrheit das, was ein inneres Abbild der äußeren Wirklichkeit gibt. - Eine solche Theorie mag man aufstellen, aber über Wahrheit, über Erkenntnis und Wirklichkeit wollen wir heute nicht sprechen.",
        "Wir wol­len über den Gesundheitswert sprechen.",
        "Die Sache ist so, daß alle diejenigen Vorstellungen, die wir bloß von der äußeren sinnlichen Wirklichkeit abstrahieren, die sozusagen nur Abbilder sind dessen, was man mit Augen sieht, mit Ohren hört, mit Händen betastet, welche nicht beruhen auf der inneren Mittätigkeit der Seele beim Schaffen von Bil­dern, alle diese Abstraktionen, alle treu an der Wirklichkeit der äußeren Sinne haftenden Vorstellungen haben keine inneren Bildekräfte.",
        "Daher bleibt die Seele tot; sie rufen die Seele nicht auf, ihre innerlich schlummernden Kräfte in Tätigkeit zu bringen und damit den Organismus in das richtige Fahrwasser seiner Tätigkeit zu bringen."
      ],
      [
        "Es mögen noch so sehr die äußeren Tatsachen-Fanatiker davon sprechen, man solle die Wirklichkeit nicht mit Bil­dern der übersinnlichen Welt durchsetzen.",
        "So paradox es auch klingt, diese Bilder bringen unseren Geist wieder in eine Tätigkeit, die ihm angemessen ist.",
        "Sie bringen ihn wie­der in Einklang mit dem physischen Organismus.",
        "Derjenige, der an den rein abstrakten Vorstellungen der bloß materialistischen"
      ],
      [
        "Wissenschaft haftet, der tut aus seinem Geisti­gen nichts für seine Gesundheit.",
        "Wer positiv nur Abstrak­tionen in seinem Begreifen sich schafft, macht seine Seele öde und leer, und er ist immer darauf angewiesen, das äußere Instrument des Leibes zum Träger der Gesundheit und zum Träger der Krankheit zu machen.",
        "Wer in ungeordneten und verkehrten Vorstellungen lebt, der weiß auch nicht, wie er sich in geheimnisvoller Weise vollpumpt mit den Ursachen der Zerstorung seines Organismus Daher stehen die Geistes-wissenschaftler auf dem Standpunkte, daß durch das, was die Geisteswissenschaft über die übersinnliche Welt geltend macht - über jene Welt, die wir nicht mit unseren Sinnen erkennen, sondern in stiller Weise innerlich wachrufen müssen -, wir unsere Seele innerlich so regsam machen, daß ihre Tätigkeit in Einklang steht mit der geistigen Welt, aus der heraus unser ganzer Organismus geschaffen worden ist.",
        "Daher wird unser Organismus nicht durch kleinliche Mittel zur Gesundung gebracht, sondern die Geisteswissenschaft selbst ist das große Heilmittel zur Gesundung."
      ],
      [
        "Derjenige, der aus dem großen Gesichtspunkte der Welt seine Gedanken bildet, diese Gedanken lebendig macht, der ruft eine solche innerliche Tätigkeit hervor, daß auch seine Gefühle und Empfindungen in einer harmonischen, die Seele beseligenden Weise abfließen.",
        "Wer auf seine Gedanken so wirkt, wirkt auch auf seine Willensimpulse, und diese wirken dann in einer gesunden Weise.",
        "Aber nur dadurch, daß wirklich eine gesunde Weltanschauung, eine gesunde Harmonie der Gedanken unsere Seele erfüllt, werden auch unsere Empfindungen und im Zusammenhange damit unsere Lust und Unlust, unsere Sympathie und Antipathie, unser Verlangen und unser Abscheu so geregelt, daß wir der Welt so gegenüberstehen, daß wir im einzelnen Falle wissen, was zu tun ist, wie das Kind, dessen Instinkt noch nicht verdorben"
      ],
      [
        "ist.",
        "So werden wir in unserer Seele innerlich diejenigen Gefühle und Empfindungen und Willensimpulse und Be­gierden wachrufen, die uns eine sichereRichtschnur im Leben sind, die uns anweisen, was zu tun ist, um das richtige Ver­hältnis zu der Außenwelt und zu uns selber hervorzurufen."
      ],
      [
        "Es ist nicht zuviel gesagt, wenn wir sagen: Klare, helle Gedanken, umfassende Gedanken, wie sie nur durch eine umfassende, auf das Ganze der Welt, also auch auf das Übersinnliche gehende Weltanschauung hervorgerufen wer­den können, sind Voraussetzung für die Gesundheit.",
        "Reine, dem Objektiven des Geistes entsprechende Gefühle, wie sie solchen Gedanken entsprechen und solchen Willensimpulsen, die werden den Menschen die Möglichkeit geben, den ge­sunden Hunger zu empfinden.",
        "Wenn man den Menschen auch nicht mit Weltanschauung füttern kann, wird es doch möglich, in dem, was für seine Seele das Entsprechende ist, das Richtige zu finden, zu suchen das für ihn Entsprechende und zu verabscheuen, was nicht entsprechend ist.",
        "Die Ge­danken, welche Abbilder sind für die übersinnliche Welt, sind das beste Verdauungsmittel - wenn auch als Para­doxon.",
        "Sie sind nicht bloß Gedankenkräfte, die auch gut für die Verdauung sind, sondern sie wirken günstig auch dadurch, daß sie durch die geistkräftigen Gedanken in sich die Kräfte wachrufen, welche die Verdauung in geregelter Weise vor sich gehen lassen."
      ],
      [
        "So lange die Menschen diesen Ruf der Geisteswissenschaft nicht vernehmen, so lange sie immer wieder glauben, das­jenige, was ihnen in dieser oder jener Krankheitsform in dieser oder jener Weise entgegentritt, das habe seine Sühne gefunden, wenn man ein entsprechendes Mittel dafür ge­funden hat, so lange werden sie die Wichtigkeit der Geistes­wissenschaft nicht erkannt haben.",
        "Sie werden auch nicht er­kannt haben, inwiefern die Gesundheit im Wesen der Entwickelung"
      ],
      [
        "eine Rolle spielt.",
        "Auch die gehen nicht weit ge­nug, welche sagen, man solle nicht Symptom-Kuren aus­führen.",
        "Auch sie erfassen nicht den geistigen Kern.",
        "Wer an die Geisteswissenschaft herantritt, der wird finden, daß sie eine Weltanschauung ist, durch welche innere Seligkeit fließt, eine Weltanschauung der Lust und Freude, daß sie Voraus­setzung ist, um das große Heilmittel für die Gesundheit zu fördern.",
        "Leichter ist es, dieses oder jenes Mittel zu gebrau­chen, als sich in den Strom der Geisteswissenschaft zu be­geben, um das zu finden, was die Menschen immer gesunder und gesunder machen wird.",
        "Dann wird man aber einsehen, wenn man sich in diese Geisteswissenschaft hinein begibt, daß es wahr ist, was ein altes Wort sagt: «In einem gesun­den Körper wohnt eine gesunde Seele», aber daß es falsch ist, dieses Wort materialistisch aufzufassen.",
        "Wer da glaubt, er müsse dieses Wort materialistisch auffassen, der soll nur auch gleich sagen: Hier sehe ich ein Haus.",
        "Dieses Haus ist schön.",
        "Also schließe ich daraus, weil dieses Haus schön ist, so muß es auch hervorgebracht haben einen schönen Besit­zer.",
        "Das schöne Haus macht einen schönen Besitzer. - Viel­leicht ist der doch etwas klüger, der sagt: Hier ist ein schönes Haus; daraus schließe ich, daß darin ein Besitzer lebt, der Geschmack hat.",
        "Ich sehe in dem Besitzer des schönen Hauses einen Menschen von gutem Geschmack, und in dem Haus das äußere Anzeichen dafür, daß der Besitzer ein Mensch von gutem Geschmack ist."
      ],
      [
        "Vielleicht findet sich aber auch der Gescheite, der sagt:"
      ],
      [
        "Weil äußere Mächte den Körper gesund gemacht haben, hat sich der Körper wieder eine gesunde Seele formiert. - Aber richtig ist es nicht, sondern recht hat wohl, wer da sagt:"
      ],
      [
        "Hier sehe ich den gesunden Körper.",
        "Das ist ein Zeichen dafür, daß er aufgebaut sein muß von einer gesunden Seele.",
        "Er ist gesund, weil die Seele gesund ist. - Deshalb kann"
      ],
      [
        "man sagen: Weil man das äußere Symptom des gesunden Leibes erblickt, deshalb muß da eine gesunde Seele zugrunde liegen.",
        "Eine materialistische Zeit mag sich das Wort: «Einem gesunden Leibe muß eine gesunde Seele zugrunde liegen» ganz materialistisch auslegen.",
        "Die Geisteswissenschaft aber zeigt uns, daß in einem gesunden Leibe eine gesunde Seele am Werke ist."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "TOLSTOJ UND CARNEGIE Berlin, 28. Januar 1909",
    "paragraphs": [
      "TOLSTOJ UND CARNEGIE",
      "Berlin, 28. Januar 1909",
      "Als eine sonderbare Zusammenstellung mag es manchem wohl erscheinen, was heute unserer Betrachtung zugrunde liegen soll: auf der einen Seite Tolstoj, auf der anderen Seite Carnegie, zwei Persönlichkeiten, von denen wohl mancher sagen wird, Verschiedeneres, Entgegengesetzteres könne es kaum geben; auf der einen Seite der aus den Tiefen des geistigen Lebens heraus suchende Rätsellöser der höchsten sozialen und geistigen Probleme - Tolstoj; und auf der an­deren Seite der Stahlkönig, der reichgewordene Mann, der Mann, von dem man literarisch kaum viel mehr weiß, als daß er darüber nachgedacht hat, wie der zusammengebrachte Reichtum am besten zu verwerten sei - Carnegie. Und dann wiederum die Zusammenstellung der beiden Persönlichkei­ten mit der Geisteswissenschaft oder Anthroposophie.",
      "Allerdings, bei Tolstoj wird es wohl niemand einfallen, zu bezweifeln, daß man gerade mit dem Lichte der Geistes­wissenschaft in die Tiefen seiner Seele hineinleuchten kann. Aber bei Carnegie wird wohl mancher sagen: Was hat denn dieser Mann überhaupt, dieser Mann des bloß praktischen, geschäftlichen Wirkens, mit dem zu tun, was man Geistes­wissenschaft nennt?-Wäre die Geisteswissenschaft die graue Theorie, die lebensfremde und lebensfeindliche Weltanschau­ung, als die sie so oft angesehen wird, kümmerte sie sich wenig um die Fragen des praktischen Lebens, wie manch­mal geglaubt wird, so könnte es sonderbar erscheinen, daß gerade zur Veranschaulichung gewisser Fragen ein solcher",
      "Mann des praktischen Lebens herangezogen wird. Hat man aber einigermaßen begriffen, was den Vorträgen,die von hier aus über Geisteswissenschaft gehalten werden, immer zugrunde liegt: daß diese Geisteswissenschaft etwas ist, was in alle einzelnen Gebiete, ja, in die alleralltäglichsten Ge­biete des praktischen Lebens einfließen kann, dann wird man es nicht verwunderlich finden, daß auch diese Persön­lichkeit einmal herangezogen wird, um dadurch manches zu veranschaulichen, was innerhalb der Geisteswissenschaft eben veranschaulicht werden soll. Und zweitens, um im Sinne Emersons zu sprechen, haben wir damit zwei reprä­sentative Persönlichkeiten unserer Zeit vor uns. Der eine wie der andere drückt das ganze Streben, das Sinnen auf der einen, das Arbeiten auf der anderen Seite, wie sie in unserer Zeit walten und weben, typisch aus, eben durchaus repräsentativ. Gerade das Entgegengesetzte der ganzen Persönlichkeits- und Seelenentwickelung bei diesen beiden Männern ist auf der einen Seite für die Mannigfaltigkeit des Lebens und Arbeitens in unserer Zeit so charakteristisch, auf der anderen Seite jedoch wiederum kennzeichnend da-für, wo der Grundnerv, die eigentlichen Ziele unsererGegen­wart liegen.",
      "Wir haben auf der einen Seite Tolstoj, der herausgewach­sen ist aus vornehmem Stande, aus Reichtum und Uberfluß, aus einer Lebenssphäre, in der alles enthalten ist, was das äußere gegenwärtige Leben an Bequemlichkeiten und An­nehmlichkeiten nur bieten kann. Wir haben in ihm einen Menschen, den seine Seelenentwickelung dazu gebracht hat, geradezu die Wertlosigkeit alles dessen, in das er hinein-geboren ist, nicht nur für sich, sondern für die ganze Mensch­heit zu proklamieren wie ein Evangelium. Wir haben auf der anderen Seite den amerikanischen Stahlkönig, eine Per­sönlichkeit, die herausgewachsen ist aus Not und Elend,",
      "herausgewachsen aus einer Lebenssphäre, wo gar nichts von dem vorhanden ist, was das äußere Leben an Annehm­lichkeiten und Bequemlichkeiten bieten kann. Eine Persön­lichkeit, die sich, man möchte sagen, Dollar um Dollar ver­dienen mußte, und die hinaufstieg zu dem größten Reich­tum, den man in der Gegenwart erwerben kann, eine Persönlichkeit, die im Verlaufe ihrer Seelenentwickelung dazu kam, diese Ansammlung des Reichtums als etwas für die Gegenwart durchaus Normales, durchaus Selbstverständ­liches zu halten und nur darüber nachzudenken, wie zum Heil und Glück der Menschheit, zu ihrer entsprechenden Fortentwickelung, dieser angesammelte Reichtum zu ver­werten sei. Dasjenige, was Tolstoj nimmermehr begehrte, als er die Höhe seiner Seelenentwickelung erreicht hatte, war ihm in reichem Maße im Beginne seines Lebens gegeben. Dasjenige, was Carnegie sich zuletzt in ausgiebiger Fülle erworben hatte, die äußeren Güter des Lebens, das war ihm im Beginne seines Lebens völlig versagt.",
      "Das ist, wenn auch in äußerlicher Weise, doch die Cha­rakteristik der beiden Persönlichkeiten, zugleich in einem gewissen Maße der Ausdruck ihres Wesens. Was in unserer Zeit mit einer Persönlichkeit vorgehen kann, was sich spiegeln kann von diesen äußeren Vorgängen an der Per­sönlichkeit und um die Persönlichkeit, alles das zeigt uns bei beiden das, was in unserer Gegenwart in den Unter­gründen des sozialen und seelischen Daseins überhaupt waltet. Wir sehen Tolstoj, wie gesagt, herausgeboren aus einer Sphäre des Lebens, in der alles dasjenige vorhanden war, was man bezeichnen könnte als die Bequemlichkeit, den Reichtum und die Vornehmheit des Lebens. Wir kön­nen uns natürlich nur ganz skizzenhaft mit seinem Leben befassen, denn es handelt sich heute darum, unsere Zeit an diesen repräsentativen Persönlichkeiten zu charakterisieren",
      "und ihre Bedürfnisse in einer gewissen Weise zu erkennen. Im Jahre 1828 ist Leo Tolstoj geboren aus einem russi­schen Grafengeschlecht, von dem er selbst sagt, daß die Familie ursprünglich aus Deutschland eingewandert ist. Wir sehen Tolstoj dann gewisse höhere Güter des Lebens ver­lieren. Kaum ist er anderthalb Jahre alt, verliert er die Mutter, im neunten Jahre den Vater. Er wächst dann her­an unter der Pflege einer Verwandten, die allerdings so­zusagen die verkörperte Liebe ist, und aus deren Seelen-verfassung sich die schöne, herrliche Seelenanlage wie von selbst in seine Seele hineingießen mußte. Aber auf der an­deren Seite steht er unter dem Einfluß einer anderen Ver­wandten, welche ganz und gar aus den Verhältnissen unse­rer Zeit, wie sie sich in gewissen Kreisen bildeten, aus den Anschauungen dieser Kreise heraus erzieherisch wirken will, eine Persönlichkeit, die ganz aufgeht in dem äußerlichen Welttreiben, das dann Tolstoj später so sehr verhaßt ge­worden ist und das er so schwer bekämpft hat. Wir sehen, wie diese Persönlichkeit von Anfang an darnach strebte, aus Tolstoj das zu machen, was man nennt einen Menschen «comme il faut», einen Menschen, der so, wie es dazumal notwendig war, seine Bauern behandeln konnte, der Titel, Rang, Würden und Orden erhalten und auch in der Gesell­schaft eine entsprechende Rolle spielen sollte.",
      "Wir sehen dann, wie Tolstoj auf die Universität kommt, wie er im Grunde genommen ein schlechter Student ist, wie er durchaus findet, daß alles das, was die Professoren an der Universität Kasan sagen, nichts Wissenswertes ist. Was ihn aus der Sphäre der Wissenschaft heraus noch zu be-schäftigen vermag, waren orientalische Sprachen. Alles an­dere ging nicht. Dagegen fesselte ihn der Vergleich eines gewissen Kapitels des Gesetzbuches der Kaiserin Katharina mit dem «Geist der Gesetze» von Montesquieu. Dann versucht",
      "er wiederholt, sein Gut zu bewirtschaften, und wir sehen, wie er geradezu dazu kommt, sich in das üppige Leben eines erwachsenen Menschen aus seinen Kreisen hin­einzusturzen, wie er sich so in dieses Leben hineinstürzt, daß er es selber bezeichnen muß als ein Hineinstürzen in alle möglichen Laster und Nichtigkeiten des Lebens. Wir sehen, wie er zum Spieler wird, große Summen verspielt, aber innerhalb dieses Lebens immer wieder zu Stunden kommt, wo sein eigenes Treiben ihn eigentlich anekelt. Wir sehen, wie er mit den Kreisen seiner eigenen Standes-genossen sowie mit den Kreisen der Literaten zusamlnen­kommt und da ein Leben führt, das er in Augenblicken des Nachdenkens als ein wertloses, ja sogar verderbliches be-zeichnet. Wir sehen aber auch - und das ist wichtig für ihn, der gern die Entwickelung der Seele da betrachtet, wo sich diese Entwickelung an besonders charakteristischen Merk­malen zeigt -, wie bei ihm in der Entwickelung seiner Seele doch besondere Eigentümlichkeiten auftreten, die schon in frühester Jugend uns verraten können, was eigentlich in dieser Seele steckt.",
      "So ist es von ungeheurer Bedeutung, welch tiefen Ein­druck auf Tolstoj im Alter von elf Jahren ein gewisses Ereignis macht. In der Schule - das brachte ein befreundeter Knabe einmal mit nach Hause - habe man eine wichtige Entdeckung, eine neue Erfindung gemacht. Man habe ge­funden, und ein Lehrer habe insbesondere davon gespro­chen, daß es keinen Gott gebe, daß dieser Gott nur eine leere Erfindung vieler Menschen sei, ein leeres Gedanken-bild. Und alles, was man wissen kann über den Eindruck, den dieses Knabenerlebnis auf Tolstoj machte, zeigt uns an der Art, wie er es aufnahm, daß in ihm eine zu den höch­sten Höhen des menschlichen Daseins hinaufstrebende und sich hinaufarbeitende Seele schon damals rang.",
      "Aber sie war auch sonst sonderbar, diese Seele. Die­jenigen Menschen, die so gern nur Äußerlichkeiten anführen und nicht dasjenige in der Seele beachten, was sich aus deren Mittelpunkt, durch alle äußeren Hindernisse hindurch her­vorringt als das eigentlich Individuelle der Seele, sie werden an solchen Jugenderlebnissen gern etwas übersehen und nicht beachten, daß etwas ganz anderes wirkt auf die eine und wieder anders auf die andere Seele. Insbesondere muß man achtgeben, wenn eine Seele in frühester Jugend eine Anlage zu dem zeigt, was man aussprechen könnte mit dem schönen Satz Goethes aus dem zweiten Teile des «Faust»:",
      "«Den lieb ich, der Unmögliches begehrt.» Es ist viel mit diesem Satze gesagt. Eine Seele, die sozusagen etwas be­gehrt, was in ganz offenbarem Sinn für alles philiströse Anschauen eine selbstverständliche Torheit ist, eine solche Seele, namentlich wenn sie sich in ihrer ersten Jugend als solche zeigt, verrät gerade durch solche Absonderlichkeiten Weite des Gesichtskreises, Weite des Strebens. Und so darf man es nicht übersehen, wenn uns Tolstoj etwa solche Dinge erzählt in einer seiner Schriften, die zu den ersten seines literarischen Schaffens gehört, und in denen er Spiegel­bilder seiner eigenen Entwickelung gibt. Wir dürfen es nicht unbeachtet lassen, wenn er da Dinge erzählt, die durchaus für ihn als geltend betrachtet werden müssen, so, wenn sich der Knabe einmal darin gefällt, seine Augenbrauen abzu­rasieren und sich so eine Zeitlang seine äußere, nicht sehr weitgehende Schönheit recht verunstaltet. Das ist etwas, was man für eine große Absonderlichkeit halten kann. Wenn man aber darüber nachdenkt, so wird es zu einer Andeu­tung. Ein anderes ist, daß der Knabe sich einbildet, der Mensch könne auch fliegen, wenn er recht starr die Arme gegen die Knie presse. Wenn er das tue, so müßte er fliegen können, meint er. Er geht also einmal in den zweiten Stock",
      "hinauf und stürzt sich zum Fenster hinaus, die Fersen fest-haltend. Er wird wie durch ein Wunder gerettet und trägt nichts davon als eine kleine Gehirnerschütterung, die sich durch einen achtzehnstündigen Schlaf wieder ausgleicht. Er hat für seine Umgebung damit nichts weiter bewiesen, als daß er ein absonderlicher Junge war. Der aber, der die Seele beobachten will und weiß, was es bedeutet, in frühe­ster Jugend in seiner Seele herauszugehen aus dem Geleise, das einem links und rechts vorgezeichnet ist, der wird solche Züge im Leben eines jungen Menschen nicht über­sehen. So erscheint diese Seele von Anfang an groß und weit angelegt. Daher können wir begreifen, daß er, als er müde war der Ausschweifungen des Lebens, die sich schon einmal aus seinem Stande ergeben haben, mit einem gewissen Ekel erfüllt war vor sich selbst, namentlich nach einer Spielaffäre.",
      "Als er dann in den Kaukasus geht, können wir begreifen, daß da seine Seele vor allen Dingen Liebe und Hinneigung gewinnt zu den einfachen Kosaken, zu denjenigen Leuten, die er da zuerst kennenlernt und von denen ihm aufgeht, daß sie eigentlich ganz andere Seelen haben als alle die­jenigen Leute, die er bisher im Grunde genommen kennen­gelernt hatte. Alles schien ihm so unnatürlich an den Prin­zipien und Grundsätzen seiner Standesgenossen. Alles, was er bisher geglaubt hatte, erschien ihm so fremd, so abge­trennt vom Urquell des Daseins. Die Menschen, die er aber nun kennenlernte, waren Leute, deren Seelen mit den Quel­len der Natur so verwachsen waren wie der Baum durch die Wurzeln mit den Quellen der Natur, wie die Blume mit den Säften des Bodens. Dieses Verwachsensein mit der Natur, dieses Nicht-fremd-geworden-S ein mit den Quellen des Da­seins, das ursprüngliche Hinaussein über das Gut und Böse in diesen Kreisen, das war es, was einen so gewaltigen Ein-druck auf ihn machte.",
      "Und dann, als er, vom Tatendrang ergriffen, Soldat wurde, um am Krimkrieg teilzunehmen, im Jahre 1854 war es wohl, als er zur Don-Armee ging, da sehen wir ihn mit der intensivsten Hingabe das ganze Seelenleben des ein­fachen Soldaten studieren. Wir sehen allerdings, wie jetzt ein spezialisierteres Empfinden in Tolstojs Seele Platz greift, wie er auf der einen Seite tief ergriffen ist von der Ur­sprünglichkeit des einfachen Menschen, auf der anderen Seite aber auch von dem Elend, der Armut, der Gequältheit und Gedrücktheit des einfachen Menschen. Wir sehen, wie er erfüllt ist von Liebe und Lust, zu helfen, und wie auch schon schattenhaft in seinemGeiste aufleuchten die höchsten Ideale von Menschenbeglückung, Menschenheil und Menschenfort­schritt, wie er auf der anderen Seite aber doch wiederum sich ganz klarmacht - aus dem Verhältnis, wie es sich her­ausgebildet hat zwischen ihm, mit seinen Anschauungen, und den natürlichen Menschen, mit ihren Anschauungen -, daß er mit der Art von Idealen, Zielen und Gedanken, wie er sie hat, nicht verstanden werden könne. Das ruft einen Zwiespalt in seiner Seele hervor, etwas, das ihn noch nicht bis zum Grundkern seines Wesens vordringen läßt.",
      "So sehen wir, daß er immer wieder zurückgeworfen wird in das Leben, aus dem er herausgeworfen wird, und daß er gerade bei der Don-Armee von einem Extrem ins andere hinein geworfen wird, so daß ein Vorgesetzter von ihm sagt, er sei ein goldener Mensch, den man nie mehr ver­gessen könne. Er wirke wie eine Seele, die nur Güte aus­gießt, und habe andererseits die Fähigkeit, in den schwie­rigsten Lagen die anderen zu erheitern. Alles war anders, wenn er da war. Einmal war er nicht da, und alles ließ den Kopf hängen. Er hatte sich wieder einmal hineingestürzt in das Leben. Er kam zurück mit einer fürchterlichen Reue, mit schrecklichem Bedauern kam er wieder ins Lager zurück.",
      "Zwischen solchen Stimmungen wurde diese, man kann nicht anders sagen als große Seele hin- und hergeworfen. Aus diesen Stimmungen und Erlebnissen wachsen auch jene Anschauungen und plastischen Erzählungen seiner litera­rischen Laufbahn, jene Erzeugnisse, die zum Beispiel die anerkennendste Kritik selbst eines Turgenjew hervorgerufen haben, und die überall Anerkennung gefunden haben. Wir sehen aber zu gleicher Zeit, wie in einer gewissen Weise das doch nur neben dem eigentlichen Zentrum, dem Mittel­punkt seiner Seele einhergeht, wie in seiner Seele immer der Blick gerichtet ist auf die große Kraft, auf den Grund-quell des Lebens, wie er ringt nach den Begriffen von Wahr­heit und Menschheitsfortschritt, und wie er, selbst einer solchen Persönlichkeit wie Turgenjew gegenüber, bei einem Zusammensein nicht anders kann als sagen: Ach, ihr habt doch eigentlich alle nicht das, was man eine Überzeugung nennt. Ihr redet eigentlich nur, um eure Überzeugung zu verbergen.",
      "Man darf sagen, das Leben hat diese Seele schwer mit­genommen, indem es sie in schwere, bittere Konflikte ge­bracht hat. Allerdings, etwas von dem Schwersten sollte erst kommen. Ende der fünfziger Jahre wurde einer seiner Brüder krank und starb. Tolstoj hatte den Tod oftmals im Kriegsleben gesehen, hatte oftmals sterbende Menschen be­trachtet, aber das Problem des Lebens war ihm in einer solchen Größe noch nicht aufgegangen, wie beim Anblick des Hinsterbens gerade seines von ihm geliebten und ge­schätzten Bruders. Tolstoj war in der damaligen Zeit nicht etwa mit einem philosophischen oder religiösen Inhalt so erfüllt, daß dieser Inhalt ihn hätte tragen können. Er war in einer solchen Grundstimmung, die sich dem Tode gegen­über etwa so zum Ausdruck brachte, daß er sagte: Unfähig bin ich, dem Leben ein Ziel zu setzen. Ich sehe das Leben",
      "abfluten, ich sehe es in meinen Standesgenossen wertlos da­hinbrausen; sie tun Dinge, die nicht wert sind, getan zu werden. Wenn man ein Ereignis an das andere reiht und noch so lange Reihen bildet, es kommt nichts Wertvolles heraus. - Und auch darin, daß die unteren Schichten in Not und Elend sind, konnte er damals keinen Inhalt und kein Lebensziel sehen. Ein solches Leben, dessen Sinn man vergeblich sucht, es wird beendet durch die Sinnlosigkeit des Todes - so sagte er sich damals -, und wenn bei jeder­mann und jedem Tier das Leben in die Sinnlosigkeit des Todes hineinmünden kann, wer vermag dann überhaupt noch von einem Sinn des Lebens zu sprechen? Manchmal hatte sich Tolstoj schon das Ziel vorgesetzt, nach der Voll­kommenheit der Seele zu streben, einen Inhalt zu suchen für die Seele. Er war nicht so weit gekommen, daß sich ihm aus dem Geiste selbst in der Seele hätte irgendein Lebens-inhalt entzünden können. Deshalb hatte der Anblick des Todes das Rätsel des Lebens in so gräßlicher Gestalt vor sein geistiges Auge hingestellt.",
      "Wir sehen ihn gerade in derselben Zeit Europa bereisen. Wir sehen ihn die interessantesten Städte Europas - Frank­reichs, Italiens, Deutschlands - aufsuchen. Wir sehen ihn manche wertvolle Persönlichkeit kennenlernen. Er lernt Schopenhauer persönlich kennen, kurz vor dessen Tode lernt er Liszt kennen und noch manche anderen, manche Größen der Wissenschaft und der Kunst. Er lernt manches aus dem sozialen Leben kennen, lernt das weimarische Hofleben kennen. Alles war ihm zugänglich, alles aber sieht er mit Augen an, aus denen die Gesinnung blickt, die eben charak­terisiert worden ist. Aus alledem hatte er nur das eine ge­wonnen: so wie es zu Hause ist, in den Kreisen, aus denen er herausgewachsen ist, so ist es im Grunde genommen auch in Westeuropa.",
      "Ein Ziel steht jetzt besonders vor ihm, ein pädagogisches Ziel. Eine Art Musterschule hatte er begründen wollen, und er hat sie auch begründet in seinem Heimatort, wo jeder Schüler seiner Fähigkeit nach lernen sollte, wo er nicht Schablone sein sollte. Wir können uns nicht einlassen auf die Beschreibung der Erziehungsgrundsätze, die da gewaltet haben. Aber das muß betont werden, daß ihm ein Er­ziehungsideal vorschwebte, das der Individualität des Kin­des gerecht werden sollte.",
      "Wir sehen, wie nun eine Art Interregnum eintritt, in dem in gewisser Weise für die stürmische Seele, in der sich die Probleme gefördert, die Fragen überstürzt haben, in der die Empfindungen und Gefühle in widersprechender Weise von allen Seiten geflossen sind, wie für diese Seele eine Art von Stillstand eintritt. Ein stilleres Leben waltet in ihr. Diese Zeit beginnt mit der Verheiratung in den sechziger Jahren. Es war die Zeit, aus der die großen Romane stam­men, in denen er die umfassenden gewaltigen Bilder des ge­sellschaftlichen Lebens der Gegenwart und der unmittelbar vorangehenden Zeit gegeben hat: «Krieg und Frieden» und «Anna Karenina». Es sind das die Werke, in die so viel eingefiossen ist von dem, was er gelernt hat.",
      "So lebte er bis in die siebziger Jahre des vorigen Jahr­hunderts hinein. Da kommt ein Zeitpunkt seines Lebens, wo er so recht am Scheideweg steht, wo sich erneuern alle Zweifels- und Skrupelfragen und alle Probleme, die früher wie aus dunklen geistigen Tiefen herauf in dieser Seele walteten. Ein Vergleich, ein Bild, das er formt, ist so recht bezeichnend für das, was diese Seele erlebte. Man braucht nur dieses Bild sich vor die Seele zu rücken und zu wissen, daß es etwas ganz anderes bedeutet für eine Seele, wie sie in Tolstoj ist, als für eine andere, viel oberflächlichere Seele. Man braucht sich nur dieses Bild vor die Seele zu rücken,",
      "und man kann tief in den Geist Tolstojs hineinschauen. Er vergleicht sein eigenes Leben mit demjenigen einer Fabel des Ostens, die er etwa so erzählt:",
      "Da ist ein Mensch, verfolgt von einem wilden Tier. Er flieht, findet einen ausgetrockneten Brunnen und stürzt sich da hinein, um dem wilden Tiere zu entkommen. Er hält sich fest an Zweigen, die herausgewachsen sind an den Seiten der Brunnenwand. Auf diese Weise glaubt er sich vor dem verfolgenden Ungeheuer geschützt. In der Tiefe sieht er nun aber einen Drachen, und er hat das Gefühl, er müsse von ihm verschlungen werden, wenn er nur ein wenig er­müdet oder wenn der Zweig bricht, an dem er sich hält. Da sieht er auch auf den Blättern des Strauches einige Tropfen Honig, von dem er sich nähren könnte. Aber zu gleicher Zeit sieht er auch Mäuse, welche die Wurzeln des Strauches benagen, an dem er sich hält.",
      "Die zwei Dinge, an denen sich Tolstoj hielt, waren Fa­milienliebe und Kunst. Im übrigen sah er das Leben so, daß man verfolgt wird von allen quälenden Sorgen des Lebens. Man entflieht dem einen und wird empfangen von dem anderen Ungeheuer. Und dann findet man, daß das Wenige, das man noch hat, von Mäusen benagt wird. - Man muß das Bild tief genug nehmen, um zu sehen, was in einer solchen Seele vorgeht, was da gezeigt ist und was Tolstoj in allem Denken, Fühlen und Wollen in umfänglichster Art erlebt hat. Die Zweige waren es, die ihn noch erfreuten. Aber er fand nach und nach auch mancherlei, was die Freude an ihnen benagen mußte. Ja, wenn das ganze Leben so ist, daß man in ihm einen Sinn nicht finden kann, daß man vergeblich nach dem Sinn des Lebens forscht, was heißt es dann aber, eine Familie haben, Nachkommen heranbilden und erziehen, auf die man im Grunde genommen dieselbe Sinnlosigkeit überträgt? Auch das war etwas, was ihm vor",
      "der Seele schwebte. Und die Kunst? Ja, wenn das Leben wertlos ist, wie steht es mit dem Spiegel des Lebens, mit der Kunst? Kann die Kunst wertvoll sein, wenn sie nur in der Lage ist, dasjenige abzuspiegeln, in dem man vergeblich nach einem Sinn sucht?",
      "Das war es, was jetzt nach einem Interregnum wiederum so recht vor seiner Seele stand, was so recht in dieser Seele aufbrannte. Wo er sich umsah bei all denen, welche in gro­ßen Philosophien und in den verschiedensten Weltanschau­ungen den Sinn des Lebens zu ergründen versuchten, nir­gends fand er etwas, was im Grunde genommen sein For­schen befriedigen konnte. Und neuerdings war es so, daß er den Blick hinwendete zu denjenigen Menschen, die mit den Quellen des Lebens nach seiner Meinung ursprünglich zu­sammenhingen. Es waren das die Menschen, die sich einen natürlichen Sinn, eine natürliche Religiosität bewahrt hat­ten. Er sagte sich: Der Gelehrte, der so lebt wie ich selber, der seine Vernunft überschätzt, er findet in allem Forschen nichts, was ihm den Sinn des Lebens deuten könnte. Be­trachte ich den gewöhnlichen Menschen, der da in Sekten sich zusammenschließt: er weiß, warum er lebt, er kennt den Sinn des Lebens. Wie weiß er das, und wie kennt er den Sinn des Lebens? Weil er in sich die Empfindung durchlebt:",
      "Es gibt einen Willen, den ewigen göttlichen Willen, wie ich ihn nenne. Und das, was in mir lebt, ergibt sich dem göttlichen Willen. Und das, was ich tue, was ich vom Mor­gen bis zum Abend verrichte, das tue ich als ein Teil des göttlichen Willens. Wenn ich die Hände rege, so rege ich sie im Willen des Göttlichen. Ohne durch die Vernunft zu abstrak­ten Begriffen gebracht zu werden, regen sich die Hände. -Das war es, was ihm so eigenartig entgegenkam, was ihn so ergriff, wenn das Menschliche in der Seele ergriffen ist. Er sagte sich: Es gibt Menschen, die können sich eine Antwort",
      "geben nach dem Sinn des Lebens, die sie brauchen kön­nen. - Es ist sogar grandios, wie er diese einfachen Menschen gegenüberstellt denen, die er in seiner Umgebung kennen­gelernt hat. Alles ist aus dem Monumentalen der Paradig­men heraus gedacht. Er sagt: Ich habe Menschen kennen­gelernt, die verstanden nichts davon, dem Leben einen Sinn zu erwecken oder zu erdenken. Sie lebten aus Gewohn­heit, trotzdem sie dem Leben keinen Sinn abgewinnen konnten, aber ich habe solche kennengelernt, welche ge­rade deshalb, weil sie keinen Sinn im Leben finden konnten, zum Selbstmord gekommen sind. - Tolstoj selbst stand nahe davor.",
      "So nahm er sich die Kategorie von Menschen durch, bei denen er sich sagen mußte: Von einem Sinn des Lebens und von einem Leben in einem Sinn kann nicht die Rede sein. Aber der Mensch, der mit den Quellen der Natur noch zu­sammenhängt, dessen Seele mit den göttlichen Kräften so zusammenhängt wie die Pflanze mit den Kräften des Lebens, der kann sich Antwort auf die Frage geben: Warum lebe ich? - Deshalb kam Tolstoj so weit, eine Gemeinschaft mit jenen einfachen Menschen im religiösen Leben zu suchen. Er wurde in gewisser Weise gläubig, obgleich die äußeren Formen einen abstoßenden Eindruck auf ihn machten. Er ging also wieder zum Abendmahl. Es war jetzt etwas in ihm, das man so bezeichnen kann: Er strebte mit allen Fasern seiner Seele darnach, ein Ziel zu finden, ein Ziel zu fühlen. Aber überall standen ihm doch in gewisser Weise wiederum sein Denken und Fühlen im Wege. Er konnte mit den Leuten, die Gläubige waren im naiven Sinn und sich die Frage nach dem Sinn des Lebens beantworteten, wohl zusammen beten. Er konnte beten - und das ist ungeheuer bezeichnend - bis zu dem Punkte einer einheitlichen Emp­findungsweise. Aber er konnte nicht mit, wenn sie weiter",
      "beteten: Und sollen uns bekennen zum Vater, zum Sohne und zum Heiligen Geiste. - Das hatte für ihn keinen Sinn. Es ist überhaupt bezeichnend, daß er bis zu einem gewissen Punkte mitkonnte, indem vor seiner Seele ein religiöses Leben stand, das bei den Menschen in einer Gemeinschaft ein brüderliches Hinein- und Herausstellen dessen bewirkte, was in der Seele lebt. Eintracht der Gefühle, Eintracht der Gedanken, das sollte hervorgebracht werden durch dieses Leben in der Gläubigkeit. Aber er konnte sich nicht erheben zu dem positiven Inhalt, der Erkenntnis des Geistes, zu geistiger Anschauung, die Wirklichkeit gibt. Die Dogmatik, die überliefert war, bedeutete für ihn gar nichts. Mit den Worten, die in der Dreifaltigkeit gegeben sind, konnte er keinen Sinn verbinden.",
      "So kam er, indem alle diese Dinge zusammenströmten, in die Periode, die er als die reife Periode seines Lebens be­zeichnen muß, in die Periode, in welcher er versuchte, sich ganz und gar zu versenken in das, was er nennen konnte wahres, echtes Christentum. Er strebt so, wie wenn er ge­wollt hätte, die Lebendigkeit der Christus-Seele mit der eigenen Seele zu umfassen, zu durchdringen. Und mit diesem Geiste der Christus-Seele wollte er sich durchdringen. Da sollte ihm eine Weltanschauung heraus erwachsen, und aus dieser sollte sich ergeben etwas wie eine Umformung alles gegenwärtigen Lebens, das er, so wie es sich für ihn dar­stellte, der herbsten Kritik unterwarf. Jetzt, da er glaubt, das, was Christus gedacht und gefühlt hat, mit der eigenen Seele zu fühlen, fühlt er sich stark genug, den Fehdehand­schuh allen Lebens- und Empfindungsweisen und allen Ge­dankenformen der Gegenwart hinzuwerfen, eine herbe Kritik an alledem zu üben, woraus er herausgewachsen ist, und was er in der weiteren Umwelt seiner Gegenwart sehen konnte. Stark genug fühlt er sich, auf der anderen Seite die",
      "Forderung aufzustellen, den Christus-Geist walten zu lassen und eine Erneuerung allen Menschenlebens aus dem Chri­stus-Geist herauszuholen. Damit haben wir sozusagen seine reifende Seele charakterisiert und gesehen, wie diese Seele herausgewachsen ist aus dem, was viele unserer Zeitgenossen die Höhen des Lebens nennen. Wir haben gesehen, wie diese Seele dazu gekommen ist, die herbste Kritik an diesen Höhen des Lebens zu üben, und in der Erneuerung des Christus-Geistes, den sie fremd findet alledem, was gegen­wärtig lebt, in der Erneuerung des Christus-Lebens, das sie nirgends in Wirklichkeit findet, sich das nächste Ziel zu setzen. Also in gewissem Sinne einen Verneiner der Gegen­wart sehen wir aus Tolstoj werden und einen Bejaher des­jenigen, was er den Christus-Geist nennen konnte, den er aber nicht in der Gegenwart finden konnte, sondern nur in den ersten Zeiten des Christentums. Er mußte bis zu den geschichtlichen Quellen zurückgehen, die sich ihm boten. Da haben wir also einen Repräsentanten unserer Gegen­wart, der herausgewachsen ist aus der Gegenwart, ver­neinend diese Gegenwart.",
      "Und nun sehen wir uns den anderen an, der so, wie Tolstoj zu der intensivsten Verneinung der Gegenwart kommt, ebenso zu der intensivsten Bejahung kommt; der im Grunde genommen zu derselben Formel kommt, nur daß sie in ganz anderer Weise angewendet wird. Da sehen wir Carnegie, den Schotten, herauswachsen aus jener Grenzscheide der Kultur der Neuzeit, die wir charakterisieren können da­durch, daß das Großgewerbe, die Großindustrie, alles das­jenige wie hinwegfegt, was in der gesellschaftlichen Ord­nung das Kleingewerbe ist. Wirklich aus jener Grenzscheide des modernen Lebens herauswachsen sehen wir Carnegie, die ein neuerer Dichter so schön charakterisiert mit den",
      "Draußen steht am Waldessaum,",
      "am Wiesengrund eine Schmiede;",
      "Draus tönt nicht mehr der Hammerschlag",
      "zum arbeitsfrohen Liede.",
      "Nicht weit entfernt ragt in die Luft",
      "ein langgestreckt Gebäude;",
      "Drin walten im Maschinenraum",
      "berußte Hammerleute.",
      "Mit Nägeln aus der Dampffabrik",
      "ward zu der Sarg geschlagen,",
      "Der den verarmten Nagelschmied",
      "zu Grabe hat getragen.",
      "Man braucht nur eine solche Stimmung zu erwecken, und man beleuchtet hell jeneGrenzscheide in derKulturentwick­lung der Neuzeit, die so wichtig geworden ist für vieles Leben. Ein Webermeister, der zunächst sein gutes Auskom­men hatte, war Carnegies Vater, ein Schotte. Er arbeitete zunächst für eine Fabrik. Das ging alles gut bis zu dem Zeitpunkt, wo die Großindustrie alles überflutete. Nun sehen wir, wie der letzte Tag herankommt, an dem Car­negies Vater das Fabrizierte noch an den Händler abliefern kann, wie er die letzte Bestellung abliefert. Armut und Elend zieht nun ein bei diesem Webermeister. Er sieht keine Möglichkeit mehr, sich in Schottland fortzubringen. Man beschließt, damit die beiden Jungen nicht in Not leben und umkommen, nach Amerika auszuwandern.",
      "Der Vater findet Arbeit in einer Baumwollfabrik, und der Junge, von dem wir zu sprechen haben, wird im zwölf­ten Jahre als Spuljunge angestellt. Er hat harte Arbeit zu leisten. Aber es gibt nach einer Woche harter, schwerer Ar­beit einen freudigen Tag für den zwölfjährigen Knaben. Es wird ihm zum ersten Male der erste Lohn ausgezahlt:",
      "1 Dollar 20 Cents. Niemals wieder - so sagt Carnegie -hat er irgendeine Einnahme mit solch entzückter Seele auf­genommen wie diesen Dollar unDa findet sich jemand, der ihri in einer anderen Fabrik mit einem besseren Lohn anstellt. Hier hat er noch mehr zu arbeiten, er muß im Keller stehen und hat eine kleine Dampfmaschine zu heizen und in Gang zu halten bei großer Hitze! Er fühlt das als verantwortungsvollen Posten. Die Angst, den Hahn an der Maschine falsch zu drehen, was für die ganze Fabrik ein Unglück bedeuten konnte, ist für ihn furchtbar. Gar oft ertappt er sich dabei, wie er in der Nacht im Bette saß und die ganze Nacht träumte von dem Hahn, an dem er drehte, um ja recht aditzugeben, daß er es in der richtigen Weise mache.",
      "Dann sehen wir, wie er nach einiger Zeit in Pittsburg an-gestellt wird als Telegraphenbote. Da ist er schon hoch-beglückt mit dem geringen Lohn des Telegraphenboten. Er hat zu arbeiten an einem Orte, wo es auch Bücher gibt, die er vorher kaum gesehen hat. Manchmal hat er auch Zeitun­gen zum Lesen. Er hat jetzt nur eine Sorge: Telegraphen­boten sind in der Stadt nicht zu brauchen, wenn sie nicht sämtliche Adressen der Firmen, die Telegramme erhalten, auswendig können. Er bringt es wirklich dahin, die Namen und Adressen der Pittsburger Firmen genau zu kennen. Er entwickelt auch schon eine gewisse Selbständigkeit. Sein Bewußtsein ist außerordentlich mit Klugheit gepaart. Er",
      "geht jetzt etwas früher nach dem Telegraphenamt, und da lernt er durch eigenes Üben selber telegraphieren. So kann er das Ideal ins Auge fassen, das in einem noch jungen, auf­strebenden Gemeinwesen jeder Telegraphenbote haben darf:",
      "selber einmal Telegraphist zu werden. Es gelingt ihm sogar ein besonderes Kunststück. Als eines Morgens der Telegra­phist nicht da war, kommt eine Todesnachricht. Er nimmt die Depesche auf und befördert sie an die Zeitung, an die sie bestimmt war. Es gibt ja Zusammenhänge, wo solch ein Vorgehen, selbst wenn es glückt, nicht günstig angesehen wird. Aber Carnegie stieg dadurch zum Telegraphisten auf.",
      "Jetzt bot sich ihm noch etwas anderes. Ein Mann, der viel mit dem Eisenbahnwesen zu tun hatte, erkennt das Talent­volle an dem jungen Mann und macht ihln eines Tages fol­genden Vorschlag. Er sagte ihm, er solle für fünfhundert Dollar Eisenbahnaktien übernehmen, die gerade freigewor­den seien. Er könne da viel gewinnen, wenn er diese Dinge betreibe. Und nun erzählt Carnegie - es ist entzückend, wie er dies erzählt -, wie er tatsächlich durch die Sorgfalt und Liebe seiner Mutter fünfhundert Dollar aufbrachte, und wie er sich seine Aktien kaufte. Als das erste Erträgnis kam, die erste Anweisung über fünf Dollar, da ging er mit seinen Gefährten hinaus in den Wald. Sie betrachteten die An­weisung und machten sich Gedanken und lernten erkennen, daß es noch etwas anderes gibt als für Arbeit entlohnt zu werden, etwas, das aus Geld Geld macht. Das erweckte große Gesichtspunkte in Carnegies Leben. Er wuchs damit in den Grundzug unserer Zeit hinein.",
      "So sehen wir, wie er gleich Verständnis hatte, als ein an­derer Vorschlag kommt. Es ist bezeichnend, wie er mit völ­liger Geistesgegenwart erfaßt, was zum ersten Male vor seiner Seele auftritt. Ein erfinderischer Kopf zeigt ihm das",
      "Modell des ersten Schlafwagens. Sogleich erkennt er, daß da etwas ungeheuer Fruchtbringendes darinnen ist, so daß er sich daran beteiligt. Nun hebt er wieder hervor, wodurch dieses sein Bewußtsein eigentlich wuchs. Er hatte nicht ge­nug Geld, um in entsprechender Weise sich an dem Unter­nehmen der ersten Schlafwagengesellschaft der Welt zu be­teiligen. Aber sein genialer Kopf bewirkte es, daß er tat­sächlich jetzt schon bei einer Bank Geld bekam: er stellte da seinen ersten Wechsel aus. Das ist nichts Besonderes, sagt er, aber das ist etwas Besonderes, daß er einen Bankier findet, der diesen Wechsel für «gut» nimmt. Und das war der Fall.",
      "Jetzt war er daran, indem das nur ausgebaut zu werden brauchte, ganz der Mann der Gegenwart zu sein. Daher brauchen wir uns nicht zu verwundern, als ihm der Gedanke kam, die vielen Holzb rücken durchEisen- und Stahlbrücken zu ersetzen, und daß er von diesem Augenblick an der große Stahlmann wurde, der Mann, der bis heute in ge­wisser Beziehung den Ton angab für die Stahlindustrie und der ungezählte Reichtümer erworben hat. So sehen wir in ihm geradezu den Typ des Menschen, der in die Gegenwart hineinwächst, die Gegenwart, die das äußerlichste Leben entfaltet. In das Alleräußerlichste der Äußerlichkeit wächst er hinein. Aber er wächst hinein durch seine eigene Kraft, durch seine Fähigkeiten. Er wird zum unermeßlich reichen Menschen aus der Not und dem Elend heraus, indem er sich wirklich vom ersten Dollar an alles selber erworben hat. Und er ist ein nachdenklicher Mensch, der diesen ganzen Impuls seines eigenen Lebens auch seinerseits mit dem Fort­schritt und dem Leben der ganzen Menschheit in Zusam­menhang bringt.",
      "So sehen wir, wie aus seiner Denkweise herauswächst ein anderes merkwürdiges Evangelium, ein Evangelium, das",
      "sich im Grunde genommen - das ist sehr interessant - auch an Christus anlehnt. Nur sagt Carnegie gleich am Eingange seines Evangeliums, es sei ein Evangelium des Reichtums. So ist das Buch in die Welt gekommen als eine Darstellung, in welcher Weise der Reichtum am besten zum Heile und zum Fortschritt in der Menschheit angewendet wird. Er wen­det sich darin gleich gegen Tolstoj, von dem er sagt: Der ist ein Mensch, der den Christus so nimmt, wie er gar nicht für unsere Zeit annehmbar ist, der ihn nimmt als ein fremdes Wesen aus alter Vergangenheit. Man muß den Christus so verstehen, daß man ihn dem Leben der Gegenwart ein-impft. - Carnegie ist ein Mensch, der das ganze Leben der Gegenwart voll bejaht. Er sagt: Blicken wir zurück auf die Zeiten, wo die Menschen einander noch mehr gleich waren als heute, wo sie noch weniger geteilt waren in solche, welche Arbeit zu vergeben haben, und solche, die Arbeit zu nehmen haben, und vergleichen wir die Zeiten, so sehen wir, wie primitiv die einzelnen Kulturen dazumal waren. Der König war in jener alten Zeit nicht imstande, seine Bedürfnisse in einer solchen Weise zu befriedigen - weil sie nicht so befrie­digt werden konnten - wie heute der ärmste Mensch sie befriedigen kann. Was geschehen ist, mußte geschehen. Es ist also richtig, daß die Güter so verteilt sind.",
      "Nun prägt Carnegie eine merkwürdige Lehre von der Verteilung oder Anwendung des Reichtums. Vor allen Din­gen werden wir es bei ihm nur natürlich finden, daß ihm Gedanken in der Seele aufgehen für die rein persönliche Tüchtigkeit, für die Tüchtigkeit des Wesens des Menschen, der sich herausarbeitet aus dem Leben zu dem, was er zu­letzt wird. Es wird ihm klar, wieviel man zu bauen hat aus diesem Mittelpunktswesen. Zunächst sieht er nur äußerliche Güter, dann aber auch, daß der Mensch tüchtig sein muß, äußerlich tüchtig. Und seine Tüchtigkeit muß man dazu",
      "anwenden, nicht bloß Reichtum zu erwerben, sondern auch ihn zu verwalten im Dienste der Menschheit.",
      "Carnegie macht intensiv darauf aufmerksam, daß ganz neue Grundsätze sozusagen eintreten müßten im sozialen Bau der Menschheit, wenn Heil und Fortschritt ersprießen sollen aus dem neuen Fortschritt und der Verteilung der Güter. Er sagt: Wir haben Einrichtungen aus früherer Zeit, die es möglich machen, daß durch die Vererbung vom Vater auf den Sohn und die Enkel Güter, Rang, Titel und Wür­den übergehen. Bei dem Leben in der alten Zeit war das möglich. - Er findet es richtig, daß man durch Routine er­setzen kann, was die persönliche Tüchtigkeit nicht gibt:",
      "Rang, Titel, Würden. Aber von dem Leben, in das er hin­eingewachsen ist, da ist er überzeugt, daß es persönliche, individuelle Tüchtigkeit verlangt. Er weist darauf hin, daß bei sieben falliten Häusern festzustellen war, daß fünf da­von dadurch fallit geworden sind, daß sie übergegangen sind auf die Söhne. Rang, Titel und Würden waren über­gegangen von den Vätern auf die Söhne, niemals aber die Geschäftstüchtigkeit. In denjenigen Teilen des modernen Lebens, wö Geschäftsprinzipien herrschen, sollten sie sich nicht einfach vom Vererber auf die Nachkommen vererben. Viel wichtiger ist es, daß man einen persönlich Tüchtigen heranzieht, als daß man eine Vererbung macht. Daraus zieht Carnegie den Schluß, den er mit dem grotesken Satze ausdrückt: Es muß der, welcher Reichtum erworben hat, dafür sorgen, daß er während dieses Lebens auch den Reich­tum anwendet, anwendet zu solchen Einrichtungen und Be­gründungen, durch welche im weitesten Umfange die Men­schen gefördert werden. - Und der Satz, mit dem er das formuliert, der grotesk erscheinen kann, der aber doch aus der ganzen Denkweise Carnegies hervorgeht, ist dieser:",
      "«Wer reich stirbt, stirbt entehrt.» Man könnte in gewissem",
      "Sinne sagen, noch revolutionärer klinge der Satz des Stahl-königs als mancher Satz Tolstojs. «Wer reich stirbt, stirbt entehrt», das heißt doch: Wer nicht anwendet diejenigen Güter, die er zusammengebracht hat, zu Stiftungen, wo­durch die Menschen etwas lernen können, wodurch sie die Möglichkeit bekommen, sich fortzubilden, wenn ein Mensch also den Reichtum nicht dazu anwendet, daß er möglichst viele Menschen tüchtig macht, sondern ihn übrig läßt, so daß ihn die Nachkommen in ihrer Art und Talentlosigkeit anwenden können und er nur ihrem persönlichen Wohl­leben dient, wer nicht so stirbt, daß er zeit seines Lebens seinen Reichtum zum Heile der Menschheit verwaltet, der stirbt entehrt.",
      "So sehen wir bei Carnegie ein sehr merkwürdiges Prinzip auftauchen. Wir sehen, daß er bejaht das gegenwärtige soziale Leben und Treiben, daß er aber aus ihm einen neuen Grundsatz herausprägt: daß der Mensch einzutreten hat nicht nur für die Verwendung des Reichtums, sondern auch für die Verwaltung, als Verwalter der Güter im Dienste der Menschheit. Kein Glaube ist in diesem Mann daran, daß irgend etwas in der Vererbungslinie von den Vor­eltern auf die Nachkommen übergehen könne. Wenn er auch nur das äußere Leben kennt, so ist es ihm doch klar, daß im Inneren des Menschen die Kräfte sprossen müssen, die den Menschen tüchtig machen zur Auswirkung des Lebens.",
      "So sehen wir diese zwei Repräsentanten unserer Gegen­wart: denjenigen, der eine herbe Kritik übt an allem, das sich nach und nach entwickelt hat, und der aus dem Geiste heraus die Seele zu Höherem führen will, und wir sehen den anderen, der das materielle Leben nimmt, wie das materielle Leben eben ist, und der aus der Betrachtung des materiellen Lebens hingewiesen wird darauf, daß im Inneren",
      "des Menschen der Quell des Arbeitens und der Le­bensgesundheit ist. So sonderbar es klingt, man könnte gerade in dieser Lehre Carnegies etwas finden, was zu fol­gendem Ausspruch berechtigt: Wenn man nicht gedanken­los und sinnlos auf dieses Seelenleben hinblickt, sondern so hinblickt, daß man nach und nach auf die aus den Seelen herausströmenden Kräfte hinsieht, hinsieht auf das Indivi­duelle, und sich durchaus klar darüber ist, daß es sich nicht in der Vererbungslinie fortpflanzt, auf was muß man dann schauen? Man muß auf den wirklichen Ursprung schauen, auf dasjenige, was aus anderen Quellen kommt. Und man wird finden, wenn man durch Geisteswissenschaft zu den Quellen der jetzigen Talente und Fähigkeiten kommt, die in früheren Leben liegen, in dem Gesetz der Wiederverkör­perung und der geistigen Verursachung, des Karma, man wird dann die Möglichkeit finden, gedankenvoll zu ver­arbeiten ein solches Prinzip, welches das praktische Leben einem praktischen Menschen aufgedrängt hat.",
      "Niemand kann hoffen, daß aus einer bloßen Veräußer­lichung des Lebens etwas kommen könnte, was die Seele befriedigen, die Kultur auf die höchsten Höhen bringen könnte. Nimmermehr kann man hoffen, daß auf jenen Bahnen etwas anderes kommen würde als eine im äußeren Sinne heilsame Verteilung des Reichtums. Die Seele würde veröden, sie würde ihre Kräfte verausgaben, aber in sich nichts finden, wenn sie nicht vordringen könnte zu den Quellen des Geistes, die jenseits liegen. Indem die Seele zurückgewiesen wird von einer materiellen Lebensbetrach­tung, muß sie die Quelle finden, die nur aus einer geistigen Lebensanschauung fließen kann. Mit einer solchen Lebens-praxis, wie sie Carnegie hat, wird sich verbinden müssen, damit die Seelen nicht veröden, jene Vertiefung und Ver­geistigung des Lebens, die aus der Geisteswissenschaft",
      "kommt. Fordert Carnegie von der einzelnen Seele das­jenige, was sie lebenstüchtig macht im äußeren Leben, so will Tolstoj der einzelnen Seele dasjenige geben, was sie aus dem tiefen Bronnen der geistigen Wesenheit heraus finden kann.",
      "Ebenso, wie Carnegie mit sicherem Blick das Wesen der Gegenwart aus dem materiellen Leben heraus erfaßt, so finden wir auf der anderen Seite Tolstoj mit sicherem Blick in der Lage, das Eigenartige der Seele zu erfassen. Bis zu einem gewissen Grenzpunkt sehen wir Tolstoj kommen, der uns in der Tat merkwürdig berührt, wenn wir alles das, was in Tolstojs Weltanschauung lebt, vergleichen mit dem, was uns namentlich in der westeuropäischen Kultur ent­gegentritt.",
      "Man kann durchsehen Werk für Werk aus der ungeheuer langen Reihe von Werken, die Tolstoj geschrie­ben hat, und man wird vor allen Dingen eines hervor-glänzen sehen: Dinge, die hier im Westen mit einem un­geheuren Aufwand von philosophischem Nachdenken, gelehrten Grübeleien, Hin- und Herschieben von Schlüssen und Schlußfolgerungen zusammengebracht werden, sie stel­len sich bei Tolstoj so dar, daß sie in fünf bis sechs Zeilen wie Gedankenblitze auftreten und für den, der so etwas auffassen kann, zur Überzeugung werden. Da wird also zum Beispiel von Tolstoj gezeigt, wie wir in der menschlichen Seele etwas finden müssen, was göttlicher Natur ist, das, wenn es in uns aufleuchtet, das Göttliche in der Welt ver­gegenwärtigen kann.",
      "Da sagt Tolstoj Um mich leben die gelehrten Naturforscher; sie erforschen, was draußen im Materiellen, im sogenannten objektiven Dasein wirklich ist. Sie suchen da die göttlichen Urgründe des Daseins. Solche Leute versuchen dann, den Menschen zusammen-zusetzen aus all den Gesetzen, Stoffen, Atomen und so wei­ter, die sie draußen im Raume verteilt suchen.",
      "dann zuletzt zu begreifen, was der Mensch ist, indem sie glauben, alle äußere Wissenschaft zusammenschließen zu müssen, um den Grund des Lebens zu finden. Solche Men­schen, sagt er, kommen mir vor wie Menschen, die um sich herum haben Bäume und Pflanzen der lebendigen Natur. Sie sagen: Das interessiert mich nicht. Aber da in der Ferne ist ein Wald, den sehe ich kaum; diesen Wald will ich er­forschen und beschreiben, dann werde ich auch verstehen die Bäume und die Pflanzen, die neben mir sind, und ich werde sie beschreiben können. - So kommen mir die Leute vor, die mit ihren Instrumenten das Wesen der Tiere erfor­schen, um das Wesen des Menschen erkennen zu lernen. Sie haben es in sich, brauchen nur zu sehen, was in ihrer aller­nächsten Nähe ist. Das tun sie aber nicht. Sie suchen die weit entfernten Bäume, ünd sie suchen das, was sie nicht sehen können, die Atome, zu begreifen. Den Menschen sel­ber aber sehen sie nicht.",
      "Diese Art der Denkweise ist so monumental, daß sie wertvoller ist als Dutzende von Erkenntnistheorien, die aus alten Kulturen heraus geschrieben sind. Das ist charak­teristisch für das ganze Denken Tolstojs. Zu solchen Dingen ist er gekommen, und in solche Dinge muß man hinein-blicken. Für den Westeuropäer ist das höchst unbefriedi­gend; erst im Umweg über Kant kommt er dazu. Mit einer Sicherheit des Seelenwirkens wird Tolstoj dazu getrieben, auszusprechen, was nicht bewiesen, aber wahr ist, was durch unmittelbare Anschauung erkannt wird, und von dem man weiß, wenn man es ausgesprochen erhält, daß es wahr ist. Dieses monumentale ursprüngliche Hervorquellen tiefster Wahrheiten wie aus dem Quell des Lebens, das er gesucht hat, zeigt sein Werk. Das ist es, was in seinen letzten Schrif­ten sich uns oft zeigt, und was so ist, daß es wie eine Mor­genröte leuchten kann einer aufgehenden Zukunft.",
      "So müssen wir sagen: Je weniger wir geneigt sind, Tolstoj dogmatisch zu nehmen, je mehr wir geneigt sind, die Gold­körner eines primitiven paradigmatischen Denkens auf­zunehmen, desto fruchtbarer wird er sein. Freilich, die­jenigen, welche eine Persönlichkeit nur so hinnehmen, daß sie auf ihre Dogmen schwören, sich nicht von ihr befruchten lassen können, die werden von ihm nicht viel haben. Es wird ihnen manches recht schlecht bekommen. Der aber, der sich befruchten lassen kann von ihm, von dem, was aus einer großen Persönlichkeit fließt, der wird viel von Tolstoj empfangen können. Wir sehen, daß in ihm die Wahrheit wirkt, paradigmatisch, und daß diese Wahrheit mit star­ken Kräften einfließt in sein persönliches Leben. Wie fließt es da ein? Es ist recht interessant, zu sehen, daß verschie­dene Anschauungen in seiner Familie herrschen. Sie tole­rieren sich. Wie war er aber imstande, seine Grundsätze in das tägliche Leben hineinzuführen? Durch Arbeiten und Wirken, und nicht bloß mit Grundsätzen. Dadurch wird er ein wahrer Pionier für manches, was in der Zukunft erst aufsprießen muß. Aber wir sehen auf der anderen Seite wiederum, wie Tolstoj doch wieder, trotzdem er ein Pionier der Zukunft ist, ein Kind seiner Zeit ist.",
      "Vielleicht in nichts so sehr als in jenem merkwürdigen Bilde, das aus dem Jahre 1848, wo er zwanzig Jahre alt war, erhalten ist, kann man eindrucksvoller empfinden, wie er sich in die Gegenwart hineinstellt. Man sehe nur das Ge­sicht des Zwanzigjährigen an, das Energie und Willens­stärke ausdrückt, zu gleicher Zeit auch Verschlossenheit. Das geistvolle Blitzen der Augen verrät dabei aber doch etwas, das den Rätseln des Lebens fragend gegenübersteht. Er ist vulkanisch im Innern, aber nicht fähig, den Vulkan zum Ausbruch zu bringen. Allerdings, geheimnisvolle Tie­fen der Seele sehen wir in seiner Physiognomie sich ausdrücken,",
      "und wir bekommen so in seiner Physiognomie den Ausdruck dafür, daß etwas Gewaltiges in ihm lebt, das er doch in diesem Organismus, den er sich ererbt hat, noch nicht voll zum Ausdruck bringen kann.",
      "So ist es auch mit der Mannigfaltigkeit der Kräfte, die in Tolstoj leben, und die nicht so recht zum Ausdruck kommen konnten. Es ist so, wie wenn sie karikiert, verzerrt in man­cher Beziehung, zum Ausdruck kommen müßten. So muß man auch den Charakter in ihm erkennen, der manchmal ins Groteske verzerrt ist. Daher ist es ganz wunderbar, wenn er in der Lage ist, hinzuweisen auf dasjenige, was man bei den Menschen gewöhnlich ein Vergängliches nennt:",
      "Siehe dir an den menschlichen Leib. Wie oft sind seine Stoffe ausgewechselt worden! Nichts ist mehr da an Materiellem von dem, was da war in dem Zehnjährigen. Und dasjenige, was das gewöhnliche Bewußtsein ist, man nehme es und vergleiche es mit dem Vorstellungsleben des Fünfzigjähri­gen: es ist etwas ganz anderes geworden, bis in das Seelen-gefüge hinein. Wir können es nicht ein Dauerndes nennen, aber überall finden wir in ihm den Mittelpunkt, von dem wir sagen müssen, daß er etwa durch folgendes in der Vor­stellung erreicht wird. Die Gegenstände der Außenwelt stehen da. Da steht dieses, dort steht jenes, da ein drittes. Zwei Menschen treten vor die Dinge. Dieselben Dinge sieht das Auge, aber sie sind für den einen so, für den anderen anders. Der eine sagt: Ich mag das; der andere sagt: Ich mag es nicht. - Wenn in der Außenwelt alles dasselbe ist, dieselben Eindrücke da sind, und die eine Seele sagt: Ich mag es, - die andere sagt: Ich mag es nicht, - wenn also die Art des Lebens verschieden ist, so ist ein Mittelpunkt da, der verschieden ist von allem Äußeren, der unerschütterlich bleibt, trotz allem Wechsel des Bewußtseins und des Kör­pers. Etwas ist da, das vor der Geburt da war und nach der",
      "Geburt da sein wird, mein besonderes Ich. Dieses mein be­sonderes Ich hat nicht mit der Geburt begonnen.",
      "Nicht darauf kommt es an, wie man sich mit den west­europäischen Gewohnheiten zu einem solchen Ausspruch stellt, sondern darauf, daß man die Empfindung hat: einen solchen Ausspruch kann man tun. Darin zeigt sich die Größe der Seele. Darin zeigt sich, daß die Seele lebt und wie sie lebt. Darin ist die Unsterblichkeit verbürgt.",
      "So sehen wir, wie Tolstoj hart an die Grenze heran­kommt von dem, was wir, durch die geisteswissenschaftliche Vertiefung verwirklicht, als das innerste Wesen der Seele kennenlernen. Er ist eingezwängt durch die Welt, die er selbst so sehr bekämpft und kann nicht vordringen zu dem wahren Lebensgang dessen, was vor der Geburt da ist, und dessen, was nach dem Tode kommt. Er kommt nicht zu der Lehre von Reinkarnation und Karma. Ebensowenig kommt er auf den inneren Impuls der Seele wie Carnegie, der ihn geradezu fordert. So sehen wir, ob ein Mensch aus tiefstem Inneren in Widerspruch ist mit alledem, was in der Gegen­wart lebt, wirkt und strebt, oder ob er, als ein Ja-Sager, mit alledem übereinstimmt, was sich in der Gegenwart als Lebensform auslebt; er wird geführt an die Pforten dessen, was wir die anthroposophische Lebensanschauung nennen. Tolstoj würde den Weg zu Carnegie finden können, Carne­gie niemals zu Tolstoj",
      "Durch diesen Vortrag sollte gezeigt werden, daß eine Welt- und Lebensanschauung gegeben werden kann, die in die unmittelbare Lebenspraxis hineinführt, die hinuntertra­gen kann das Neuerkannte zu dem Bekannten, zu dem Vollführten. Und so werden wir sehen, wenn wir immer tiefer und tiefer uns in diese Geisteswissenschaft hinein-finden, wie sie für die Menschen sowohl der einen als der anderen Schattierung das bringt, was das Leben bringen",
      "muß, was ja schließlich in seiner Art Tolstoj gefunden hat, was Carnegie in seiner Art gefunden hat: ein in sich befrie­digtes Leben. Aber darauf kommt es nicht an, daß der un­mittelbare Sucher das befriedigte Leben findet, und daß die, welche mit ihm suchen, es auch finden können. Was Tolstoj für sich und was Carnegie für sich als befriedigend gefun­den haben, das kann nur auf unpersönlichem, reinem Wege und durch ein auf die Ebene des Geistes gerichtetes Erken­nen für alle Menschen, die auf diesem Wege suchen, gefun­den werden, wenn in wahrer Geist-Erkenntnis das, was von Leben zu Leben geht, was Bürgschaft für die Ewigkeit in sich trägt - und was Tolstoj in gewisser Weise, weil er es schon geahnt hat, für sich selbst fand -, für alle Menschen gefunden sein wird."
    ],
    "sentences": [
      [
        "TOLSTOJ UND CARNEGIE"
      ],
      [
        "Berlin, 28.",
        "Januar 1909"
      ],
      [
        "Als eine sonderbare Zusammenstellung mag es manchem wohl erscheinen, was heute unserer Betrachtung zugrunde liegen soll: auf der einen Seite Tolstoj, auf der anderen Seite Carnegie, zwei Persönlichkeiten, von denen wohl mancher sagen wird, Verschiedeneres, Entgegengesetzteres könne es kaum geben; auf der einen Seite der aus den Tiefen des geistigen Lebens heraus suchende Rätsellöser der höchsten sozialen und geistigen Probleme - Tolstoj; und auf der an­deren Seite der Stahlkönig, der reichgewordene Mann, der Mann, von dem man literarisch kaum viel mehr weiß, als daß er darüber nachgedacht hat, wie der zusammengebrachte Reichtum am besten zu verwerten sei - Carnegie.",
        "Und dann wiederum die Zusammenstellung der beiden Persönlichkei­ten mit der Geisteswissenschaft oder Anthroposophie."
      ],
      [
        "Allerdings, bei Tolstoj wird es wohl niemand einfallen, zu bezweifeln, daß man gerade mit dem Lichte der Geistes­wissenschaft in die Tiefen seiner Seele hineinleuchten kann.",
        "Aber bei Carnegie wird wohl mancher sagen: Was hat denn dieser Mann überhaupt, dieser Mann des bloß praktischen, geschäftlichen Wirkens, mit dem zu tun, was man Geistes­wissenschaft nennt?-Wäre die Geisteswissenschaft die graue Theorie, die lebensfremde und lebensfeindliche Weltanschau­ung, als die sie so oft angesehen wird, kümmerte sie sich wenig um die Fragen des praktischen Lebens, wie manch­mal geglaubt wird, so könnte es sonderbar erscheinen, daß gerade zur Veranschaulichung gewisser Fragen ein solcher"
      ],
      [
        "Mann des praktischen Lebens herangezogen wird.",
        "Hat man aber einigermaßen begriffen, was den Vorträgen,die von hier aus über Geisteswissenschaft gehalten werden, immer zugrunde liegt: daß diese Geisteswissenschaft etwas ist, was in alle einzelnen Gebiete, ja, in die alleralltäglichsten Ge­biete des praktischen Lebens einfließen kann, dann wird man es nicht verwunderlich finden, daß auch diese Persön­lichkeit einmal herangezogen wird, um dadurch manches zu veranschaulichen, was innerhalb der Geisteswissenschaft eben veranschaulicht werden soll.",
        "Und zweitens, um im Sinne Emersons zu sprechen, haben wir damit zwei reprä­sentative Persönlichkeiten unserer Zeit vor uns.",
        "Der eine wie der andere drückt das ganze Streben, das Sinnen auf der einen, das Arbeiten auf der anderen Seite, wie sie in unserer Zeit walten und weben, typisch aus, eben durchaus repräsentativ.",
        "Gerade das Entgegengesetzte der ganzen Persönlichkeits- und Seelenentwickelung bei diesen beiden Männern ist auf der einen Seite für die Mannigfaltigkeit des Lebens und Arbeitens in unserer Zeit so charakteristisch, auf der anderen Seite jedoch wiederum kennzeichnend da-für, wo der Grundnerv, die eigentlichen Ziele unsererGegen­wart liegen."
      ],
      [
        "Wir haben auf der einen Seite Tolstoj, der herausgewach­sen ist aus vornehmem Stande, aus Reichtum und Uberfluß, aus einer Lebenssphäre, in der alles enthalten ist, was das äußere gegenwärtige Leben an Bequemlichkeiten und An­nehmlichkeiten nur bieten kann.",
        "Wir haben in ihm einen Menschen, den seine Seelenentwickelung dazu gebracht hat, geradezu die Wertlosigkeit alles dessen, in das er hinein-geboren ist, nicht nur für sich, sondern für die ganze Mensch­heit zu proklamieren wie ein Evangelium.",
        "Wir haben auf der anderen Seite den amerikanischen Stahlkönig, eine Per­sönlichkeit, die herausgewachsen ist aus Not und Elend,"
      ],
      [
        "herausgewachsen aus einer Lebenssphäre, wo gar nichts von dem vorhanden ist, was das äußere Leben an Annehm­lichkeiten und Bequemlichkeiten bieten kann.",
        "Eine Persön­lichkeit, die sich, man möchte sagen, Dollar um Dollar ver­dienen mußte, und die hinaufstieg zu dem größten Reich­tum, den man in der Gegenwart erwerben kann, eine Persönlichkeit, die im Verlaufe ihrer Seelenentwickelung dazu kam, diese Ansammlung des Reichtums als etwas für die Gegenwart durchaus Normales, durchaus Selbstverständ­liches zu halten und nur darüber nachzudenken, wie zum Heil und Glück der Menschheit, zu ihrer entsprechenden Fortentwickelung, dieser angesammelte Reichtum zu ver­werten sei.",
        "Dasjenige, was Tolstoj nimmermehr begehrte, als er die Höhe seiner Seelenentwickelung erreicht hatte, war ihm in reichem Maße im Beginne seines Lebens gegeben.",
        "Dasjenige, was Carnegie sich zuletzt in ausgiebiger Fülle erworben hatte, die äußeren Güter des Lebens, das war ihm im Beginne seines Lebens völlig versagt."
      ],
      [
        "Das ist, wenn auch in äußerlicher Weise, doch die Cha­rakteristik der beiden Persönlichkeiten, zugleich in einem gewissen Maße der Ausdruck ihres Wesens.",
        "Was in unserer Zeit mit einer Persönlichkeit vorgehen kann, was sich spiegeln kann von diesen äußeren Vorgängen an der Per­sönlichkeit und um die Persönlichkeit, alles das zeigt uns bei beiden das, was in unserer Gegenwart in den Unter­gründen des sozialen und seelischen Daseins überhaupt waltet.",
        "Wir sehen Tolstoj, wie gesagt, herausgeboren aus einer Sphäre des Lebens, in der alles dasjenige vorhanden war, was man bezeichnen könnte als die Bequemlichkeit, den Reichtum und die Vornehmheit des Lebens.",
        "Wir kön­nen uns natürlich nur ganz skizzenhaft mit seinem Leben befassen, denn es handelt sich heute darum, unsere Zeit an diesen repräsentativen Persönlichkeiten zu charakterisieren"
      ],
      [
        "und ihre Bedürfnisse in einer gewissen Weise zu erkennen.",
        "Im Jahre 1828 ist Leo Tolstoj geboren aus einem russi­schen Grafengeschlecht, von dem er selbst sagt, daß die Familie ursprünglich aus Deutschland eingewandert ist.",
        "Wir sehen Tolstoj dann gewisse höhere Güter des Lebens ver­lieren.",
        "Kaum ist er anderthalb Jahre alt, verliert er die Mutter, im neunten Jahre den Vater.",
        "Er wächst dann her­an unter der Pflege einer Verwandten, die allerdings so­zusagen die verkörperte Liebe ist, und aus deren Seelen-verfassung sich die schöne, herrliche Seelenanlage wie von selbst in seine Seele hineingießen mußte.",
        "Aber auf der an­deren Seite steht er unter dem Einfluß einer anderen Ver­wandten, welche ganz und gar aus den Verhältnissen unse­rer Zeit, wie sie sich in gewissen Kreisen bildeten, aus den Anschauungen dieser Kreise heraus erzieherisch wirken will, eine Persönlichkeit, die ganz aufgeht in dem äußerlichen Welttreiben, das dann Tolstoj später so sehr verhaßt ge­worden ist und das er so schwer bekämpft hat.",
        "Wir sehen, wie diese Persönlichkeit von Anfang an darnach strebte, aus Tolstoj das zu machen, was man nennt einen Menschen «comme il faut», einen Menschen, der so, wie es dazumal notwendig war, seine Bauern behandeln konnte, der Titel, Rang, Würden und Orden erhalten und auch in der Gesell­schaft eine entsprechende Rolle spielen sollte."
      ],
      [
        "Wir sehen dann, wie Tolstoj auf die Universität kommt, wie er im Grunde genommen ein schlechter Student ist, wie er durchaus findet, daß alles das, was die Professoren an der Universität Kasan sagen, nichts Wissenswertes ist.",
        "Was ihn aus der Sphäre der Wissenschaft heraus noch zu be-schäftigen vermag, waren orientalische Sprachen.",
        "Alles an­dere ging nicht.",
        "Dagegen fesselte ihn der Vergleich eines gewissen Kapitels des Gesetzbuches der Kaiserin Katharina mit dem «Geist der Gesetze» von Montesquieu.",
        "Dann versucht"
      ],
      [
        "er wiederholt, sein Gut zu bewirtschaften, und wir sehen, wie er geradezu dazu kommt, sich in das üppige Leben eines erwachsenen Menschen aus seinen Kreisen hin­einzusturzen, wie er sich so in dieses Leben hineinstürzt, daß er es selber bezeichnen muß als ein Hineinstürzen in alle möglichen Laster und Nichtigkeiten des Lebens.",
        "Wir sehen, wie er zum Spieler wird, große Summen verspielt, aber innerhalb dieses Lebens immer wieder zu Stunden kommt, wo sein eigenes Treiben ihn eigentlich anekelt.",
        "Wir sehen, wie er mit den Kreisen seiner eigenen Standes-genossen sowie mit den Kreisen der Literaten zusamlnen­kommt und da ein Leben führt, das er in Augenblicken des Nachdenkens als ein wertloses, ja sogar verderbliches be-zeichnet.",
        "Wir sehen aber auch - und das ist wichtig für ihn, der gern die Entwickelung der Seele da betrachtet, wo sich diese Entwickelung an besonders charakteristischen Merk­malen zeigt -, wie bei ihm in der Entwickelung seiner Seele doch besondere Eigentümlichkeiten auftreten, die schon in frühester Jugend uns verraten können, was eigentlich in dieser Seele steckt."
      ],
      [
        "So ist es von ungeheurer Bedeutung, welch tiefen Ein­druck auf Tolstoj im Alter von elf Jahren ein gewisses Ereignis macht.",
        "In der Schule - das brachte ein befreundeter Knabe einmal mit nach Hause - habe man eine wichtige Entdeckung, eine neue Erfindung gemacht.",
        "Man habe ge­funden, und ein Lehrer habe insbesondere davon gespro­chen, daß es keinen Gott gebe, daß dieser Gott nur eine leere Erfindung vieler Menschen sei, ein leeres Gedanken-bild.",
        "Und alles, was man wissen kann über den Eindruck, den dieses Knabenerlebnis auf Tolstoj machte, zeigt uns an der Art, wie er es aufnahm, daß in ihm eine zu den höch­sten Höhen des menschlichen Daseins hinaufstrebende und sich hinaufarbeitende Seele schon damals rang."
      ],
      [
        "Aber sie war auch sonst sonderbar, diese Seele.",
        "Die­jenigen Menschen, die so gern nur Äußerlichkeiten anführen und nicht dasjenige in der Seele beachten, was sich aus deren Mittelpunkt, durch alle äußeren Hindernisse hindurch her­vorringt als das eigentlich Individuelle der Seele, sie werden an solchen Jugenderlebnissen gern etwas übersehen und nicht beachten, daß etwas ganz anderes wirkt auf die eine und wieder anders auf die andere Seele.",
        "Insbesondere muß man achtgeben, wenn eine Seele in frühester Jugend eine Anlage zu dem zeigt, was man aussprechen könnte mit dem schönen Satz Goethes aus dem zweiten Teile des «Faust»:"
      ],
      [
        "«Den lieb ich, der Unmögliches begehrt.» Es ist viel mit diesem Satze gesagt.",
        "Eine Seele, die sozusagen etwas be­gehrt, was in ganz offenbarem Sinn für alles philiströse Anschauen eine selbstverständliche Torheit ist, eine solche Seele, namentlich wenn sie sich in ihrer ersten Jugend als solche zeigt, verrät gerade durch solche Absonderlichkeiten Weite des Gesichtskreises, Weite des Strebens.",
        "Und so darf man es nicht übersehen, wenn uns Tolstoj etwa solche Dinge erzählt in einer seiner Schriften, die zu den ersten seines literarischen Schaffens gehört, und in denen er Spiegel­bilder seiner eigenen Entwickelung gibt.",
        "Wir dürfen es nicht unbeachtet lassen, wenn er da Dinge erzählt, die durchaus für ihn als geltend betrachtet werden müssen, so, wenn sich der Knabe einmal darin gefällt, seine Augenbrauen abzu­rasieren und sich so eine Zeitlang seine äußere, nicht sehr weitgehende Schönheit recht verunstaltet.",
        "Das ist etwas, was man für eine große Absonderlichkeit halten kann.",
        "Wenn man aber darüber nachdenkt, so wird es zu einer Andeu­tung.",
        "Ein anderes ist, daß der Knabe sich einbildet, der Mensch könne auch fliegen, wenn er recht starr die Arme gegen die Knie presse.",
        "Wenn er das tue, so müßte er fliegen können, meint er.",
        "Er geht also einmal in den zweiten Stock"
      ],
      [
        "hinauf und stürzt sich zum Fenster hinaus, die Fersen fest-haltend.",
        "Er wird wie durch ein Wunder gerettet und trägt nichts davon als eine kleine Gehirnerschütterung, die sich durch einen achtzehnstündigen Schlaf wieder ausgleicht.",
        "Er hat für seine Umgebung damit nichts weiter bewiesen, als daß er ein absonderlicher Junge war.",
        "Der aber, der die Seele beobachten will und weiß, was es bedeutet, in frühe­ster Jugend in seiner Seele herauszugehen aus dem Geleise, das einem links und rechts vorgezeichnet ist, der wird solche Züge im Leben eines jungen Menschen nicht über­sehen.",
        "So erscheint diese Seele von Anfang an groß und weit angelegt.",
        "Daher können wir begreifen, daß er, als er müde war der Ausschweifungen des Lebens, die sich schon einmal aus seinem Stande ergeben haben, mit einem gewissen Ekel erfüllt war vor sich selbst, namentlich nach einer Spielaffäre."
      ],
      [
        "Als er dann in den Kaukasus geht, können wir begreifen, daß da seine Seele vor allen Dingen Liebe und Hinneigung gewinnt zu den einfachen Kosaken, zu denjenigen Leuten, die er da zuerst kennenlernt und von denen ihm aufgeht, daß sie eigentlich ganz andere Seelen haben als alle die­jenigen Leute, die er bisher im Grunde genommen kennen­gelernt hatte.",
        "Alles schien ihm so unnatürlich an den Prin­zipien und Grundsätzen seiner Standesgenossen.",
        "Alles, was er bisher geglaubt hatte, erschien ihm so fremd, so abge­trennt vom Urquell des Daseins.",
        "Die Menschen, die er aber nun kennenlernte, waren Leute, deren Seelen mit den Quel­len der Natur so verwachsen waren wie der Baum durch die Wurzeln mit den Quellen der Natur, wie die Blume mit den Säften des Bodens.",
        "Dieses Verwachsensein mit der Natur, dieses Nicht-fremd-geworden-S ein mit den Quellen des Da­seins, das ursprüngliche Hinaussein über das Gut und Böse in diesen Kreisen, das war es, was einen so gewaltigen Ein-druck auf ihn machte."
      ],
      [
        "Und dann, als er, vom Tatendrang ergriffen, Soldat wurde, um am Krimkrieg teilzunehmen, im Jahre 1854 war es wohl, als er zur Don-Armee ging, da sehen wir ihn mit der intensivsten Hingabe das ganze Seelenleben des ein­fachen Soldaten studieren.",
        "Wir sehen allerdings, wie jetzt ein spezialisierteres Empfinden in Tolstojs Seele Platz greift, wie er auf der einen Seite tief ergriffen ist von der Ur­sprünglichkeit des einfachen Menschen, auf der anderen Seite aber auch von dem Elend, der Armut, der Gequältheit und Gedrücktheit des einfachen Menschen.",
        "Wir sehen, wie er erfüllt ist von Liebe und Lust, zu helfen, und wie auch schon schattenhaft in seinemGeiste aufleuchten die höchsten Ideale von Menschenbeglückung, Menschenheil und Menschenfort­schritt, wie er auf der anderen Seite aber doch wiederum sich ganz klarmacht - aus dem Verhältnis, wie es sich her­ausgebildet hat zwischen ihm, mit seinen Anschauungen, und den natürlichen Menschen, mit ihren Anschauungen -, daß er mit der Art von Idealen, Zielen und Gedanken, wie er sie hat, nicht verstanden werden könne.",
        "Das ruft einen Zwiespalt in seiner Seele hervor, etwas, das ihn noch nicht bis zum Grundkern seines Wesens vordringen läßt."
      ],
      [
        "So sehen wir, daß er immer wieder zurückgeworfen wird in das Leben, aus dem er herausgeworfen wird, und daß er gerade bei der Don-Armee von einem Extrem ins andere hinein geworfen wird, so daß ein Vorgesetzter von ihm sagt, er sei ein goldener Mensch, den man nie mehr ver­gessen könne.",
        "Er wirke wie eine Seele, die nur Güte aus­gießt, und habe andererseits die Fähigkeit, in den schwie­rigsten Lagen die anderen zu erheitern.",
        "Alles war anders, wenn er da war.",
        "Einmal war er nicht da, und alles ließ den Kopf hängen.",
        "Er hatte sich wieder einmal hineingestürzt in das Leben.",
        "Er kam zurück mit einer fürchterlichen Reue, mit schrecklichem Bedauern kam er wieder ins Lager zurück."
      ],
      [
        "Zwischen solchen Stimmungen wurde diese, man kann nicht anders sagen als große Seele hin- und hergeworfen.",
        "Aus diesen Stimmungen und Erlebnissen wachsen auch jene Anschauungen und plastischen Erzählungen seiner litera­rischen Laufbahn, jene Erzeugnisse, die zum Beispiel die anerkennendste Kritik selbst eines Turgenjew hervorgerufen haben, und die überall Anerkennung gefunden haben.",
        "Wir sehen aber zu gleicher Zeit, wie in einer gewissen Weise das doch nur neben dem eigentlichen Zentrum, dem Mittel­punkt seiner Seele einhergeht, wie in seiner Seele immer der Blick gerichtet ist auf die große Kraft, auf den Grund-quell des Lebens, wie er ringt nach den Begriffen von Wahr­heit und Menschheitsfortschritt, und wie er, selbst einer solchen Persönlichkeit wie Turgenjew gegenüber, bei einem Zusammensein nicht anders kann als sagen: Ach, ihr habt doch eigentlich alle nicht das, was man eine Überzeugung nennt.",
        "Ihr redet eigentlich nur, um eure Überzeugung zu verbergen."
      ],
      [
        "Man darf sagen, das Leben hat diese Seele schwer mit­genommen, indem es sie in schwere, bittere Konflikte ge­bracht hat.",
        "Allerdings, etwas von dem Schwersten sollte erst kommen.",
        "Ende der fünfziger Jahre wurde einer seiner Brüder krank und starb.",
        "Tolstoj hatte den Tod oftmals im Kriegsleben gesehen, hatte oftmals sterbende Menschen be­trachtet, aber das Problem des Lebens war ihm in einer solchen Größe noch nicht aufgegangen, wie beim Anblick des Hinsterbens gerade seines von ihm geliebten und ge­schätzten Bruders.",
        "Tolstoj war in der damaligen Zeit nicht etwa mit einem philosophischen oder religiösen Inhalt so erfüllt, daß dieser Inhalt ihn hätte tragen können.",
        "Er war in einer solchen Grundstimmung, die sich dem Tode gegen­über etwa so zum Ausdruck brachte, daß er sagte: Unfähig bin ich, dem Leben ein Ziel zu setzen.",
        "Ich sehe das Leben"
      ],
      [
        "abfluten, ich sehe es in meinen Standesgenossen wertlos da­hinbrausen; sie tun Dinge, die nicht wert sind, getan zu werden.",
        "Wenn man ein Ereignis an das andere reiht und noch so lange Reihen bildet, es kommt nichts Wertvolles heraus. - Und auch darin, daß die unteren Schichten in Not und Elend sind, konnte er damals keinen Inhalt und kein Lebensziel sehen.",
        "Ein solches Leben, dessen Sinn man vergeblich sucht, es wird beendet durch die Sinnlosigkeit des Todes - so sagte er sich damals -, und wenn bei jeder­mann und jedem Tier das Leben in die Sinnlosigkeit des Todes hineinmünden kann, wer vermag dann überhaupt noch von einem Sinn des Lebens zu sprechen?",
        "Manchmal hatte sich Tolstoj schon das Ziel vorgesetzt, nach der Voll­kommenheit der Seele zu streben, einen Inhalt zu suchen für die Seele.",
        "Er war nicht so weit gekommen, daß sich ihm aus dem Geiste selbst in der Seele hätte irgendein Lebens-inhalt entzünden können.",
        "Deshalb hatte der Anblick des Todes das Rätsel des Lebens in so gräßlicher Gestalt vor sein geistiges Auge hingestellt."
      ],
      [
        "Wir sehen ihn gerade in derselben Zeit Europa bereisen.",
        "Wir sehen ihn die interessantesten Städte Europas - Frank­reichs, Italiens, Deutschlands - aufsuchen.",
        "Wir sehen ihn manche wertvolle Persönlichkeit kennenlernen.",
        "Er lernt Schopenhauer persönlich kennen, kurz vor dessen Tode lernt er Liszt kennen und noch manche anderen, manche Größen der Wissenschaft und der Kunst.",
        "Er lernt manches aus dem sozialen Leben kennen, lernt das weimarische Hofleben kennen.",
        "Alles war ihm zugänglich, alles aber sieht er mit Augen an, aus denen die Gesinnung blickt, die eben charak­terisiert worden ist.",
        "Aus alledem hatte er nur das eine ge­wonnen: so wie es zu Hause ist, in den Kreisen, aus denen er herausgewachsen ist, so ist es im Grunde genommen auch in Westeuropa."
      ],
      [
        "Ein Ziel steht jetzt besonders vor ihm, ein pädagogisches Ziel.",
        "Eine Art Musterschule hatte er begründen wollen, und er hat sie auch begründet in seinem Heimatort, wo jeder Schüler seiner Fähigkeit nach lernen sollte, wo er nicht Schablone sein sollte.",
        "Wir können uns nicht einlassen auf die Beschreibung der Erziehungsgrundsätze, die da gewaltet haben.",
        "Aber das muß betont werden, daß ihm ein Er­ziehungsideal vorschwebte, das der Individualität des Kin­des gerecht werden sollte."
      ],
      [
        "Wir sehen, wie nun eine Art Interregnum eintritt, in dem in gewisser Weise für die stürmische Seele, in der sich die Probleme gefördert, die Fragen überstürzt haben, in der die Empfindungen und Gefühle in widersprechender Weise von allen Seiten geflossen sind, wie für diese Seele eine Art von Stillstand eintritt.",
        "Ein stilleres Leben waltet in ihr.",
        "Diese Zeit beginnt mit der Verheiratung in den sechziger Jahren.",
        "Es war die Zeit, aus der die großen Romane stam­men, in denen er die umfassenden gewaltigen Bilder des ge­sellschaftlichen Lebens der Gegenwart und der unmittelbar vorangehenden Zeit gegeben hat: «Krieg und Frieden» und «Anna Karenina».",
        "Es sind das die Werke, in die so viel eingefiossen ist von dem, was er gelernt hat."
      ],
      [
        "So lebte er bis in die siebziger Jahre des vorigen Jahr­hunderts hinein.",
        "Da kommt ein Zeitpunkt seines Lebens, wo er so recht am Scheideweg steht, wo sich erneuern alle Zweifels- und Skrupelfragen und alle Probleme, die früher wie aus dunklen geistigen Tiefen herauf in dieser Seele walteten.",
        "Ein Vergleich, ein Bild, das er formt, ist so recht bezeichnend für das, was diese Seele erlebte.",
        "Man braucht nur dieses Bild sich vor die Seele zu rücken und zu wissen, daß es etwas ganz anderes bedeutet für eine Seele, wie sie in Tolstoj ist, als für eine andere, viel oberflächlichere Seele.",
        "Man braucht sich nur dieses Bild vor die Seele zu rücken,"
      ],
      [
        "und man kann tief in den Geist Tolstojs hineinschauen.",
        "Er vergleicht sein eigenes Leben mit demjenigen einer Fabel des Ostens, die er etwa so erzählt:"
      ],
      [
        "Da ist ein Mensch, verfolgt von einem wilden Tier.",
        "Er flieht, findet einen ausgetrockneten Brunnen und stürzt sich da hinein, um dem wilden Tiere zu entkommen.",
        "Er hält sich fest an Zweigen, die herausgewachsen sind an den Seiten der Brunnenwand.",
        "Auf diese Weise glaubt er sich vor dem verfolgenden Ungeheuer geschützt.",
        "In der Tiefe sieht er nun aber einen Drachen, und er hat das Gefühl, er müsse von ihm verschlungen werden, wenn er nur ein wenig er­müdet oder wenn der Zweig bricht, an dem er sich hält.",
        "Da sieht er auch auf den Blättern des Strauches einige Tropfen Honig, von dem er sich nähren könnte.",
        "Aber zu gleicher Zeit sieht er auch Mäuse, welche die Wurzeln des Strauches benagen, an dem er sich hält."
      ],
      [
        "Die zwei Dinge, an denen sich Tolstoj hielt, waren Fa­milienliebe und Kunst.",
        "Im übrigen sah er das Leben so, daß man verfolgt wird von allen quälenden Sorgen des Lebens.",
        "Man entflieht dem einen und wird empfangen von dem anderen Ungeheuer.",
        "Und dann findet man, daß das Wenige, das man noch hat, von Mäusen benagt wird. - Man muß das Bild tief genug nehmen, um zu sehen, was in einer solchen Seele vorgeht, was da gezeigt ist und was Tolstoj in allem Denken, Fühlen und Wollen in umfänglichster Art erlebt hat.",
        "Die Zweige waren es, die ihn noch erfreuten.",
        "Aber er fand nach und nach auch mancherlei, was die Freude an ihnen benagen mußte.",
        "Ja, wenn das ganze Leben so ist, daß man in ihm einen Sinn nicht finden kann, daß man vergeblich nach dem Sinn des Lebens forscht, was heißt es dann aber, eine Familie haben, Nachkommen heranbilden und erziehen, auf die man im Grunde genommen dieselbe Sinnlosigkeit überträgt?",
        "Auch das war etwas, was ihm vor"
      ],
      [
        "der Seele schwebte.",
        "Und die Kunst?",
        "Ja, wenn das Leben wertlos ist, wie steht es mit dem Spiegel des Lebens, mit der Kunst?",
        "Kann die Kunst wertvoll sein, wenn sie nur in der Lage ist, dasjenige abzuspiegeln, in dem man vergeblich nach einem Sinn sucht?"
      ],
      [
        "Das war es, was jetzt nach einem Interregnum wiederum so recht vor seiner Seele stand, was so recht in dieser Seele aufbrannte.",
        "Wo er sich umsah bei all denen, welche in gro­ßen Philosophien und in den verschiedensten Weltanschau­ungen den Sinn des Lebens zu ergründen versuchten, nir­gends fand er etwas, was im Grunde genommen sein For­schen befriedigen konnte.",
        "Und neuerdings war es so, daß er den Blick hinwendete zu denjenigen Menschen, die mit den Quellen des Lebens nach seiner Meinung ursprünglich zu­sammenhingen.",
        "Es waren das die Menschen, die sich einen natürlichen Sinn, eine natürliche Religiosität bewahrt hat­ten.",
        "Er sagte sich: Der Gelehrte, der so lebt wie ich selber, der seine Vernunft überschätzt, er findet in allem Forschen nichts, was ihm den Sinn des Lebens deuten könnte.",
        "Be­trachte ich den gewöhnlichen Menschen, der da in Sekten sich zusammenschließt: er weiß, warum er lebt, er kennt den Sinn des Lebens.",
        "Wie weiß er das, und wie kennt er den Sinn des Lebens?",
        "Weil er in sich die Empfindung durchlebt:"
      ],
      [
        "Es gibt einen Willen, den ewigen göttlichen Willen, wie ich ihn nenne.",
        "Und das, was in mir lebt, ergibt sich dem göttlichen Willen.",
        "Und das, was ich tue, was ich vom Mor­gen bis zum Abend verrichte, das tue ich als ein Teil des göttlichen Willens.",
        "Wenn ich die Hände rege, so rege ich sie im Willen des Göttlichen.",
        "Ohne durch die Vernunft zu abstrak­ten Begriffen gebracht zu werden, regen sich die Hände. -Das war es, was ihm so eigenartig entgegenkam, was ihn so ergriff, wenn das Menschliche in der Seele ergriffen ist.",
        "Er sagte sich: Es gibt Menschen, die können sich eine Antwort"
      ],
      [
        "geben nach dem Sinn des Lebens, die sie brauchen kön­nen. - Es ist sogar grandios, wie er diese einfachen Menschen gegenüberstellt denen, die er in seiner Umgebung kennen­gelernt hat.",
        "Alles ist aus dem Monumentalen der Paradig­men heraus gedacht.",
        "Er sagt: Ich habe Menschen kennen­gelernt, die verstanden nichts davon, dem Leben einen Sinn zu erwecken oder zu erdenken.",
        "Sie lebten aus Gewohn­heit, trotzdem sie dem Leben keinen Sinn abgewinnen konnten, aber ich habe solche kennengelernt, welche ge­rade deshalb, weil sie keinen Sinn im Leben finden konnten, zum Selbstmord gekommen sind. - Tolstoj selbst stand nahe davor."
      ],
      [
        "So nahm er sich die Kategorie von Menschen durch, bei denen er sich sagen mußte: Von einem Sinn des Lebens und von einem Leben in einem Sinn kann nicht die Rede sein.",
        "Aber der Mensch, der mit den Quellen der Natur noch zu­sammenhängt, dessen Seele mit den göttlichen Kräften so zusammenhängt wie die Pflanze mit den Kräften des Lebens, der kann sich Antwort auf die Frage geben: Warum lebe ich? - Deshalb kam Tolstoj so weit, eine Gemeinschaft mit jenen einfachen Menschen im religiösen Leben zu suchen.",
        "Er wurde in gewisser Weise gläubig, obgleich die äußeren Formen einen abstoßenden Eindruck auf ihn machten.",
        "Er ging also wieder zum Abendmahl.",
        "Es war jetzt etwas in ihm, das man so bezeichnen kann: Er strebte mit allen Fasern seiner Seele darnach, ein Ziel zu finden, ein Ziel zu fühlen.",
        "Aber überall standen ihm doch in gewisser Weise wiederum sein Denken und Fühlen im Wege.",
        "Er konnte mit den Leuten, die Gläubige waren im naiven Sinn und sich die Frage nach dem Sinn des Lebens beantworteten, wohl zusammen beten.",
        "Er konnte beten - und das ist ungeheuer bezeichnend - bis zu dem Punkte einer einheitlichen Emp­findungsweise.",
        "Aber er konnte nicht mit, wenn sie weiter"
      ],
      [
        "beteten: Und sollen uns bekennen zum Vater, zum Sohne und zum Heiligen Geiste. - Das hatte für ihn keinen Sinn.",
        "Es ist überhaupt bezeichnend, daß er bis zu einem gewissen Punkte mitkonnte, indem vor seiner Seele ein religiöses Leben stand, das bei den Menschen in einer Gemeinschaft ein brüderliches Hinein- und Herausstellen dessen bewirkte, was in der Seele lebt.",
        "Eintracht der Gefühle, Eintracht der Gedanken, das sollte hervorgebracht werden durch dieses Leben in der Gläubigkeit.",
        "Aber er konnte sich nicht erheben zu dem positiven Inhalt, der Erkenntnis des Geistes, zu geistiger Anschauung, die Wirklichkeit gibt.",
        "Die Dogmatik, die überliefert war, bedeutete für ihn gar nichts.",
        "Mit den Worten, die in der Dreifaltigkeit gegeben sind, konnte er keinen Sinn verbinden."
      ],
      [
        "So kam er, indem alle diese Dinge zusammenströmten, in die Periode, die er als die reife Periode seines Lebens be­zeichnen muß, in die Periode, in welcher er versuchte, sich ganz und gar zu versenken in das, was er nennen konnte wahres, echtes Christentum.",
        "Er strebt so, wie wenn er ge­wollt hätte, die Lebendigkeit der Christus-Seele mit der eigenen Seele zu umfassen, zu durchdringen.",
        "Und mit diesem Geiste der Christus-Seele wollte er sich durchdringen.",
        "Da sollte ihm eine Weltanschauung heraus erwachsen, und aus dieser sollte sich ergeben etwas wie eine Umformung alles gegenwärtigen Lebens, das er, so wie es sich für ihn dar­stellte, der herbsten Kritik unterwarf.",
        "Jetzt, da er glaubt, das, was Christus gedacht und gefühlt hat, mit der eigenen Seele zu fühlen, fühlt er sich stark genug, den Fehdehand­schuh allen Lebens- und Empfindungsweisen und allen Ge­dankenformen der Gegenwart hinzuwerfen, eine herbe Kritik an alledem zu üben, woraus er herausgewachsen ist, und was er in der weiteren Umwelt seiner Gegenwart sehen konnte.",
        "Stark genug fühlt er sich, auf der anderen Seite die"
      ],
      [
        "Forderung aufzustellen, den Christus-Geist walten zu lassen und eine Erneuerung allen Menschenlebens aus dem Chri­stus-Geist herauszuholen.",
        "Damit haben wir sozusagen seine reifende Seele charakterisiert und gesehen, wie diese Seele herausgewachsen ist aus dem, was viele unserer Zeitgenossen die Höhen des Lebens nennen.",
        "Wir haben gesehen, wie diese Seele dazu gekommen ist, die herbste Kritik an diesen Höhen des Lebens zu üben, und in der Erneuerung des Christus-Geistes, den sie fremd findet alledem, was gegen­wärtig lebt, in der Erneuerung des Christus-Lebens, das sie nirgends in Wirklichkeit findet, sich das nächste Ziel zu setzen.",
        "Also in gewissem Sinne einen Verneiner der Gegen­wart sehen wir aus Tolstoj werden und einen Bejaher des­jenigen, was er den Christus-Geist nennen konnte, den er aber nicht in der Gegenwart finden konnte, sondern nur in den ersten Zeiten des Christentums.",
        "Er mußte bis zu den geschichtlichen Quellen zurückgehen, die sich ihm boten.",
        "Da haben wir also einen Repräsentanten unserer Gegen­wart, der herausgewachsen ist aus der Gegenwart, ver­neinend diese Gegenwart."
      ],
      [
        "Und nun sehen wir uns den anderen an, der so, wie Tolstoj zu der intensivsten Verneinung der Gegenwart kommt, ebenso zu der intensivsten Bejahung kommt; der im Grunde genommen zu derselben Formel kommt, nur daß sie in ganz anderer Weise angewendet wird.",
        "Da sehen wir Carnegie, den Schotten, herauswachsen aus jener Grenzscheide der Kultur der Neuzeit, die wir charakterisieren können da­durch, daß das Großgewerbe, die Großindustrie, alles das­jenige wie hinwegfegt, was in der gesellschaftlichen Ord­nung das Kleingewerbe ist.",
        "Wirklich aus jener Grenzscheide des modernen Lebens herauswachsen sehen wir Carnegie, die ein neuerer Dichter so schön charakterisiert mit den"
      ],
      [
        "Draußen steht am Waldessaum,"
      ],
      [
        "am Wiesengrund eine Schmiede;"
      ],
      [
        "Draus tönt nicht mehr der Hammerschlag"
      ],
      [
        "zum arbeitsfrohen Liede."
      ],
      [
        "Nicht weit entfernt ragt in die Luft"
      ],
      [
        "ein langgestreckt Gebäude;"
      ],
      [
        "Drin walten im Maschinenraum"
      ],
      [
        "berußte Hammerleute."
      ],
      [
        "Mit Nägeln aus der Dampffabrik"
      ],
      [
        "ward zu der Sarg geschlagen,"
      ],
      [
        "Der den verarmten Nagelschmied"
      ],
      [
        "zu Grabe hat getragen."
      ],
      [
        "Man braucht nur eine solche Stimmung zu erwecken, und man beleuchtet hell jeneGrenzscheide in derKulturentwick­lung der Neuzeit, die so wichtig geworden ist für vieles Leben.",
        "Ein Webermeister, der zunächst sein gutes Auskom­men hatte, war Carnegies Vater, ein Schotte.",
        "Er arbeitete zunächst für eine Fabrik.",
        "Das ging alles gut bis zu dem Zeitpunkt, wo die Großindustrie alles überflutete.",
        "Nun sehen wir, wie der letzte Tag herankommt, an dem Car­negies Vater das Fabrizierte noch an den Händler abliefern kann, wie er die letzte Bestellung abliefert.",
        "Armut und Elend zieht nun ein bei diesem Webermeister.",
        "Er sieht keine Möglichkeit mehr, sich in Schottland fortzubringen.",
        "Man beschließt, damit die beiden Jungen nicht in Not leben und umkommen, nach Amerika auszuwandern."
      ],
      [
        "Der Vater findet Arbeit in einer Baumwollfabrik, und der Junge, von dem wir zu sprechen haben, wird im zwölf­ten Jahre als Spuljunge angestellt.",
        "Er hat harte Arbeit zu leisten.",
        "Aber es gibt nach einer Woche harter, schwerer Ar­beit einen freudigen Tag für den zwölfjährigen Knaben.",
        "Es wird ihm zum ersten Male der erste Lohn ausgezahlt:"
      ],
      [
        "1 Dollar 20 Cents.",
        "Niemals wieder - so sagt Carnegie -hat er irgendeine Einnahme mit solch entzückter Seele auf­genommen wie diesen Dollar unDa findet sich jemand, der ihri in einer anderen Fabrik mit einem besseren Lohn anstellt.",
        "Hier hat er noch mehr zu arbeiten, er muß im Keller stehen und hat eine kleine Dampfmaschine zu heizen und in Gang zu halten bei großer Hitze!",
        "Er fühlt das als verantwortungsvollen Posten.",
        "Die Angst, den Hahn an der Maschine falsch zu drehen, was für die ganze Fabrik ein Unglück bedeuten konnte, ist für ihn furchtbar.",
        "Gar oft ertappt er sich dabei, wie er in der Nacht im Bette saß und die ganze Nacht träumte von dem Hahn, an dem er drehte, um ja recht aditzugeben, daß er es in der richtigen Weise mache."
      ],
      [
        "Dann sehen wir, wie er nach einiger Zeit in Pittsburg an-gestellt wird als Telegraphenbote.",
        "Da ist er schon hoch-beglückt mit dem geringen Lohn des Telegraphenboten.",
        "Er hat zu arbeiten an einem Orte, wo es auch Bücher gibt, die er vorher kaum gesehen hat.",
        "Manchmal hat er auch Zeitun­gen zum Lesen.",
        "Er hat jetzt nur eine Sorge: Telegraphen­boten sind in der Stadt nicht zu brauchen, wenn sie nicht sämtliche Adressen der Firmen, die Telegramme erhalten, auswendig können.",
        "Er bringt es wirklich dahin, die Namen und Adressen der Pittsburger Firmen genau zu kennen.",
        "Er entwickelt auch schon eine gewisse Selbständigkeit.",
        "Sein Bewußtsein ist außerordentlich mit Klugheit gepaart."
      ],
      [
        "geht jetzt etwas früher nach dem Telegraphenamt, und da lernt er durch eigenes Üben selber telegraphieren.",
        "So kann er das Ideal ins Auge fassen, das in einem noch jungen, auf­strebenden Gemeinwesen jeder Telegraphenbote haben darf:"
      ],
      [
        "selber einmal Telegraphist zu werden.",
        "Es gelingt ihm sogar ein besonderes Kunststück.",
        "Als eines Morgens der Telegra­phist nicht da war, kommt eine Todesnachricht.",
        "Er nimmt die Depesche auf und befördert sie an die Zeitung, an die sie bestimmt war.",
        "Es gibt ja Zusammenhänge, wo solch ein Vorgehen, selbst wenn es glückt, nicht günstig angesehen wird.",
        "Aber Carnegie stieg dadurch zum Telegraphisten auf."
      ],
      [
        "Jetzt bot sich ihm noch etwas anderes.",
        "Ein Mann, der viel mit dem Eisenbahnwesen zu tun hatte, erkennt das Talent­volle an dem jungen Mann und macht ihln eines Tages fol­genden Vorschlag.",
        "Er sagte ihm, er solle für fünfhundert Dollar Eisenbahnaktien übernehmen, die gerade freigewor­den seien.",
        "Er könne da viel gewinnen, wenn er diese Dinge betreibe.",
        "Und nun erzählt Carnegie - es ist entzückend, wie er dies erzählt -, wie er tatsächlich durch die Sorgfalt und Liebe seiner Mutter fünfhundert Dollar aufbrachte, und wie er sich seine Aktien kaufte.",
        "Als das erste Erträgnis kam, die erste Anweisung über fünf Dollar, da ging er mit seinen Gefährten hinaus in den Wald.",
        "Sie betrachteten die An­weisung und machten sich Gedanken und lernten erkennen, daß es noch etwas anderes gibt als für Arbeit entlohnt zu werden, etwas, das aus Geld Geld macht.",
        "Das erweckte große Gesichtspunkte in Carnegies Leben.",
        "Er wuchs damit in den Grundzug unserer Zeit hinein."
      ],
      [
        "So sehen wir, wie er gleich Verständnis hatte, als ein an­derer Vorschlag kommt.",
        "Es ist bezeichnend, wie er mit völ­liger Geistesgegenwart erfaßt, was zum ersten Male vor seiner Seele auftritt.",
        "Ein erfinderischer Kopf zeigt ihm das"
      ],
      [
        "Modell des ersten Schlafwagens.",
        "Sogleich erkennt er, daß da etwas ungeheuer Fruchtbringendes darinnen ist, so daß er sich daran beteiligt.",
        "Nun hebt er wieder hervor, wodurch dieses sein Bewußtsein eigentlich wuchs.",
        "Er hatte nicht ge­nug Geld, um in entsprechender Weise sich an dem Unter­nehmen der ersten Schlafwagengesellschaft der Welt zu be­teiligen.",
        "Aber sein genialer Kopf bewirkte es, daß er tat­sächlich jetzt schon bei einer Bank Geld bekam: er stellte da seinen ersten Wechsel aus.",
        "Das ist nichts Besonderes, sagt er, aber das ist etwas Besonderes, daß er einen Bankier findet, der diesen Wechsel für «gut» nimmt.",
        "Und das war der Fall."
      ],
      [
        "Jetzt war er daran, indem das nur ausgebaut zu werden brauchte, ganz der Mann der Gegenwart zu sein.",
        "Daher brauchen wir uns nicht zu verwundern, als ihm der Gedanke kam, die vielen Holzb rücken durchEisen- und Stahlbrücken zu ersetzen, und daß er von diesem Augenblick an der große Stahlmann wurde, der Mann, der bis heute in ge­wisser Beziehung den Ton angab für die Stahlindustrie und der ungezählte Reichtümer erworben hat.",
        "So sehen wir in ihm geradezu den Typ des Menschen, der in die Gegenwart hineinwächst, die Gegenwart, die das äußerlichste Leben entfaltet.",
        "In das Alleräußerlichste der Äußerlichkeit wächst er hinein.",
        "Aber er wächst hinein durch seine eigene Kraft, durch seine Fähigkeiten.",
        "Er wird zum unermeßlich reichen Menschen aus der Not und dem Elend heraus, indem er sich wirklich vom ersten Dollar an alles selber erworben hat.",
        "Und er ist ein nachdenklicher Mensch, der diesen ganzen Impuls seines eigenen Lebens auch seinerseits mit dem Fort­schritt und dem Leben der ganzen Menschheit in Zusam­menhang bringt."
      ],
      [
        "So sehen wir, wie aus seiner Denkweise herauswächst ein anderes merkwürdiges Evangelium, ein Evangelium, das"
      ],
      [
        "sich im Grunde genommen - das ist sehr interessant - auch an Christus anlehnt.",
        "Nur sagt Carnegie gleich am Eingange seines Evangeliums, es sei ein Evangelium des Reichtums.",
        "So ist das Buch in die Welt gekommen als eine Darstellung, in welcher Weise der Reichtum am besten zum Heile und zum Fortschritt in der Menschheit angewendet wird.",
        "Er wen­det sich darin gleich gegen Tolstoj, von dem er sagt: Der ist ein Mensch, der den Christus so nimmt, wie er gar nicht für unsere Zeit annehmbar ist, der ihn nimmt als ein fremdes Wesen aus alter Vergangenheit.",
        "Man muß den Christus so verstehen, daß man ihn dem Leben der Gegenwart ein-impft. - Carnegie ist ein Mensch, der das ganze Leben der Gegenwart voll bejaht.",
        "Er sagt: Blicken wir zurück auf die Zeiten, wo die Menschen einander noch mehr gleich waren als heute, wo sie noch weniger geteilt waren in solche, welche Arbeit zu vergeben haben, und solche, die Arbeit zu nehmen haben, und vergleichen wir die Zeiten, so sehen wir, wie primitiv die einzelnen Kulturen dazumal waren.",
        "Der König war in jener alten Zeit nicht imstande, seine Bedürfnisse in einer solchen Weise zu befriedigen - weil sie nicht so befrie­digt werden konnten - wie heute der ärmste Mensch sie befriedigen kann.",
        "Was geschehen ist, mußte geschehen.",
        "Es ist also richtig, daß die Güter so verteilt sind."
      ],
      [
        "Nun prägt Carnegie eine merkwürdige Lehre von der Verteilung oder Anwendung des Reichtums.",
        "Vor allen Din­gen werden wir es bei ihm nur natürlich finden, daß ihm Gedanken in der Seele aufgehen für die rein persönliche Tüchtigkeit, für die Tüchtigkeit des Wesens des Menschen, der sich herausarbeitet aus dem Leben zu dem, was er zu­letzt wird.",
        "Es wird ihm klar, wieviel man zu bauen hat aus diesem Mittelpunktswesen.",
        "Zunächst sieht er nur äußerliche Güter, dann aber auch, daß der Mensch tüchtig sein muß, äußerlich tüchtig.",
        "Und seine Tüchtigkeit muß man dazu"
      ],
      [
        "anwenden, nicht bloß Reichtum zu erwerben, sondern auch ihn zu verwalten im Dienste der Menschheit."
      ],
      [
        "Carnegie macht intensiv darauf aufmerksam, daß ganz neue Grundsätze sozusagen eintreten müßten im sozialen Bau der Menschheit, wenn Heil und Fortschritt ersprießen sollen aus dem neuen Fortschritt und der Verteilung der Güter.",
        "Er sagt: Wir haben Einrichtungen aus früherer Zeit, die es möglich machen, daß durch die Vererbung vom Vater auf den Sohn und die Enkel Güter, Rang, Titel und Wür­den übergehen.",
        "Bei dem Leben in der alten Zeit war das möglich. - Er findet es richtig, daß man durch Routine er­setzen kann, was die persönliche Tüchtigkeit nicht gibt:"
      ],
      [
        "Rang, Titel, Würden.",
        "Aber von dem Leben, in das er hin­eingewachsen ist, da ist er überzeugt, daß es persönliche, individuelle Tüchtigkeit verlangt.",
        "Er weist darauf hin, daß bei sieben falliten Häusern festzustellen war, daß fünf da­von dadurch fallit geworden sind, daß sie übergegangen sind auf die Söhne.",
        "Rang, Titel und Würden waren über­gegangen von den Vätern auf die Söhne, niemals aber die Geschäftstüchtigkeit.",
        "In denjenigen Teilen des modernen Lebens, wö Geschäftsprinzipien herrschen, sollten sie sich nicht einfach vom Vererber auf die Nachkommen vererben.",
        "Viel wichtiger ist es, daß man einen persönlich Tüchtigen heranzieht, als daß man eine Vererbung macht.",
        "Daraus zieht Carnegie den Schluß, den er mit dem grotesken Satze ausdrückt: Es muß der, welcher Reichtum erworben hat, dafür sorgen, daß er während dieses Lebens auch den Reich­tum anwendet, anwendet zu solchen Einrichtungen und Be­gründungen, durch welche im weitesten Umfange die Men­schen gefördert werden. - Und der Satz, mit dem er das formuliert, der grotesk erscheinen kann, der aber doch aus der ganzen Denkweise Carnegies hervorgeht, ist dieser:"
      ],
      [
        "«Wer reich stirbt, stirbt entehrt.» Man könnte in gewissem"
      ],
      [
        "Sinne sagen, noch revolutionärer klinge der Satz des Stahl-königs als mancher Satz Tolstojs.",
        "«Wer reich stirbt, stirbt entehrt», das heißt doch: Wer nicht anwendet diejenigen Güter, die er zusammengebracht hat, zu Stiftungen, wo­durch die Menschen etwas lernen können, wodurch sie die Möglichkeit bekommen, sich fortzubilden, wenn ein Mensch also den Reichtum nicht dazu anwendet, daß er möglichst viele Menschen tüchtig macht, sondern ihn übrig läßt, so daß ihn die Nachkommen in ihrer Art und Talentlosigkeit anwenden können und er nur ihrem persönlichen Wohl­leben dient, wer nicht so stirbt, daß er zeit seines Lebens seinen Reichtum zum Heile der Menschheit verwaltet, der stirbt entehrt."
      ],
      [
        "So sehen wir bei Carnegie ein sehr merkwürdiges Prinzip auftauchen.",
        "Wir sehen, daß er bejaht das gegenwärtige soziale Leben und Treiben, daß er aber aus ihm einen neuen Grundsatz herausprägt: daß der Mensch einzutreten hat nicht nur für die Verwendung des Reichtums, sondern auch für die Verwaltung, als Verwalter der Güter im Dienste der Menschheit.",
        "Kein Glaube ist in diesem Mann daran, daß irgend etwas in der Vererbungslinie von den Vor­eltern auf die Nachkommen übergehen könne.",
        "Wenn er auch nur das äußere Leben kennt, so ist es ihm doch klar, daß im Inneren des Menschen die Kräfte sprossen müssen, die den Menschen tüchtig machen zur Auswirkung des Lebens."
      ],
      [
        "So sehen wir diese zwei Repräsentanten unserer Gegen­wart: denjenigen, der eine herbe Kritik übt an allem, das sich nach und nach entwickelt hat, und der aus dem Geiste heraus die Seele zu Höherem führen will, und wir sehen den anderen, der das materielle Leben nimmt, wie das materielle Leben eben ist, und der aus der Betrachtung des materiellen Lebens hingewiesen wird darauf, daß im Inneren"
      ],
      [
        "des Menschen der Quell des Arbeitens und der Le­bensgesundheit ist.",
        "So sonderbar es klingt, man könnte gerade in dieser Lehre Carnegies etwas finden, was zu fol­gendem Ausspruch berechtigt: Wenn man nicht gedanken­los und sinnlos auf dieses Seelenleben hinblickt, sondern so hinblickt, daß man nach und nach auf die aus den Seelen herausströmenden Kräfte hinsieht, hinsieht auf das Indivi­duelle, und sich durchaus klar darüber ist, daß es sich nicht in der Vererbungslinie fortpflanzt, auf was muß man dann schauen?",
        "Man muß auf den wirklichen Ursprung schauen, auf dasjenige, was aus anderen Quellen kommt.",
        "Und man wird finden, wenn man durch Geisteswissenschaft zu den Quellen der jetzigen Talente und Fähigkeiten kommt, die in früheren Leben liegen, in dem Gesetz der Wiederverkör­perung und der geistigen Verursachung, des Karma, man wird dann die Möglichkeit finden, gedankenvoll zu ver­arbeiten ein solches Prinzip, welches das praktische Leben einem praktischen Menschen aufgedrängt hat."
      ],
      [
        "Niemand kann hoffen, daß aus einer bloßen Veräußer­lichung des Lebens etwas kommen könnte, was die Seele befriedigen, die Kultur auf die höchsten Höhen bringen könnte.",
        "Nimmermehr kann man hoffen, daß auf jenen Bahnen etwas anderes kommen würde als eine im äußeren Sinne heilsame Verteilung des Reichtums.",
        "Die Seele würde veröden, sie würde ihre Kräfte verausgaben, aber in sich nichts finden, wenn sie nicht vordringen könnte zu den Quellen des Geistes, die jenseits liegen.",
        "Indem die Seele zurückgewiesen wird von einer materiellen Lebensbetrach­tung, muß sie die Quelle finden, die nur aus einer geistigen Lebensanschauung fließen kann.",
        "Mit einer solchen Lebens-praxis, wie sie Carnegie hat, wird sich verbinden müssen, damit die Seelen nicht veröden, jene Vertiefung und Ver­geistigung des Lebens, die aus der Geisteswissenschaft"
      ],
      [
        "kommt.",
        "Fordert Carnegie von der einzelnen Seele das­jenige, was sie lebenstüchtig macht im äußeren Leben, so will Tolstoj der einzelnen Seele dasjenige geben, was sie aus dem tiefen Bronnen der geistigen Wesenheit heraus finden kann."
      ],
      [
        "Ebenso, wie Carnegie mit sicherem Blick das Wesen der Gegenwart aus dem materiellen Leben heraus erfaßt, so finden wir auf der anderen Seite Tolstoj mit sicherem Blick in der Lage, das Eigenartige der Seele zu erfassen.",
        "Bis zu einem gewissen Grenzpunkt sehen wir Tolstoj kommen, der uns in der Tat merkwürdig berührt, wenn wir alles das, was in Tolstojs Weltanschauung lebt, vergleichen mit dem, was uns namentlich in der westeuropäischen Kultur ent­gegentritt."
      ],
      [
        "Man kann durchsehen Werk für Werk aus der ungeheuer langen Reihe von Werken, die Tolstoj geschrie­ben hat, und man wird vor allen Dingen eines hervor-glänzen sehen: Dinge, die hier im Westen mit einem un­geheuren Aufwand von philosophischem Nachdenken, gelehrten Grübeleien, Hin- und Herschieben von Schlüssen und Schlußfolgerungen zusammengebracht werden, sie stel­len sich bei Tolstoj so dar, daß sie in fünf bis sechs Zeilen wie Gedankenblitze auftreten und für den, der so etwas auffassen kann, zur Überzeugung werden.",
        "Da wird also zum Beispiel von Tolstoj gezeigt, wie wir in der menschlichen Seele etwas finden müssen, was göttlicher Natur ist, das, wenn es in uns aufleuchtet, das Göttliche in der Welt ver­gegenwärtigen kann."
      ],
      [
        "Da sagt Tolstoj Um mich leben die gelehrten Naturforscher; sie erforschen, was draußen im Materiellen, im sogenannten objektiven Dasein wirklich ist.",
        "Sie suchen da die göttlichen Urgründe des Daseins.",
        "Solche Leute versuchen dann, den Menschen zusammen-zusetzen aus all den Gesetzen, Stoffen, Atomen und so wei­ter, die sie draußen im Raume verteilt suchen."
      ],
      [
        "dann zuletzt zu begreifen, was der Mensch ist, indem sie glauben, alle äußere Wissenschaft zusammenschließen zu müssen, um den Grund des Lebens zu finden.",
        "Solche Men­schen, sagt er, kommen mir vor wie Menschen, die um sich herum haben Bäume und Pflanzen der lebendigen Natur.",
        "Sie sagen: Das interessiert mich nicht.",
        "Aber da in der Ferne ist ein Wald, den sehe ich kaum; diesen Wald will ich er­forschen und beschreiben, dann werde ich auch verstehen die Bäume und die Pflanzen, die neben mir sind, und ich werde sie beschreiben können. - So kommen mir die Leute vor, die mit ihren Instrumenten das Wesen der Tiere erfor­schen, um das Wesen des Menschen erkennen zu lernen.",
        "Sie haben es in sich, brauchen nur zu sehen, was in ihrer aller­nächsten Nähe ist.",
        "Das tun sie aber nicht.",
        "Sie suchen die weit entfernten Bäume, ünd sie suchen das, was sie nicht sehen können, die Atome, zu begreifen.",
        "Den Menschen sel­ber aber sehen sie nicht."
      ],
      [
        "Diese Art der Denkweise ist so monumental, daß sie wertvoller ist als Dutzende von Erkenntnistheorien, die aus alten Kulturen heraus geschrieben sind.",
        "Das ist charak­teristisch für das ganze Denken Tolstojs.",
        "Zu solchen Dingen ist er gekommen, und in solche Dinge muß man hinein-blicken.",
        "Für den Westeuropäer ist das höchst unbefriedi­gend; erst im Umweg über Kant kommt er dazu.",
        "Mit einer Sicherheit des Seelenwirkens wird Tolstoj dazu getrieben, auszusprechen, was nicht bewiesen, aber wahr ist, was durch unmittelbare Anschauung erkannt wird, und von dem man weiß, wenn man es ausgesprochen erhält, daß es wahr ist.",
        "Dieses monumentale ursprüngliche Hervorquellen tiefster Wahrheiten wie aus dem Quell des Lebens, das er gesucht hat, zeigt sein Werk.",
        "Das ist es, was in seinen letzten Schrif­ten sich uns oft zeigt, und was so ist, daß es wie eine Mor­genröte leuchten kann einer aufgehenden Zukunft."
      ],
      [
        "So müssen wir sagen: Je weniger wir geneigt sind, Tolstoj dogmatisch zu nehmen, je mehr wir geneigt sind, die Gold­körner eines primitiven paradigmatischen Denkens auf­zunehmen, desto fruchtbarer wird er sein.",
        "Freilich, die­jenigen, welche eine Persönlichkeit nur so hinnehmen, daß sie auf ihre Dogmen schwören, sich nicht von ihr befruchten lassen können, die werden von ihm nicht viel haben.",
        "Es wird ihnen manches recht schlecht bekommen.",
        "Der aber, der sich befruchten lassen kann von ihm, von dem, was aus einer großen Persönlichkeit fließt, der wird viel von Tolstoj empfangen können.",
        "Wir sehen, daß in ihm die Wahrheit wirkt, paradigmatisch, und daß diese Wahrheit mit star­ken Kräften einfließt in sein persönliches Leben.",
        "Wie fließt es da ein?",
        "Es ist recht interessant, zu sehen, daß verschie­dene Anschauungen in seiner Familie herrschen.",
        "Sie tole­rieren sich.",
        "Wie war er aber imstande, seine Grundsätze in das tägliche Leben hineinzuführen?",
        "Durch Arbeiten und Wirken, und nicht bloß mit Grundsätzen.",
        "Dadurch wird er ein wahrer Pionier für manches, was in der Zukunft erst aufsprießen muß.",
        "Aber wir sehen auf der anderen Seite wiederum, wie Tolstoj doch wieder, trotzdem er ein Pionier der Zukunft ist, ein Kind seiner Zeit ist."
      ],
      [
        "Vielleicht in nichts so sehr als in jenem merkwürdigen Bilde, das aus dem Jahre 1848, wo er zwanzig Jahre alt war, erhalten ist, kann man eindrucksvoller empfinden, wie er sich in die Gegenwart hineinstellt.",
        "Man sehe nur das Ge­sicht des Zwanzigjährigen an, das Energie und Willens­stärke ausdrückt, zu gleicher Zeit auch Verschlossenheit.",
        "Das geistvolle Blitzen der Augen verrät dabei aber doch etwas, das den Rätseln des Lebens fragend gegenübersteht.",
        "Er ist vulkanisch im Innern, aber nicht fähig, den Vulkan zum Ausbruch zu bringen.",
        "Allerdings, geheimnisvolle Tie­fen der Seele sehen wir in seiner Physiognomie sich ausdrücken,"
      ],
      [
        "und wir bekommen so in seiner Physiognomie den Ausdruck dafür, daß etwas Gewaltiges in ihm lebt, das er doch in diesem Organismus, den er sich ererbt hat, noch nicht voll zum Ausdruck bringen kann."
      ],
      [
        "So ist es auch mit der Mannigfaltigkeit der Kräfte, die in Tolstoj leben, und die nicht so recht zum Ausdruck kommen konnten.",
        "Es ist so, wie wenn sie karikiert, verzerrt in man­cher Beziehung, zum Ausdruck kommen müßten.",
        "So muß man auch den Charakter in ihm erkennen, der manchmal ins Groteske verzerrt ist.",
        "Daher ist es ganz wunderbar, wenn er in der Lage ist, hinzuweisen auf dasjenige, was man bei den Menschen gewöhnlich ein Vergängliches nennt:"
      ],
      [
        "Siehe dir an den menschlichen Leib.",
        "Wie oft sind seine Stoffe ausgewechselt worden!",
        "Nichts ist mehr da an Materiellem von dem, was da war in dem Zehnjährigen.",
        "Und dasjenige, was das gewöhnliche Bewußtsein ist, man nehme es und vergleiche es mit dem Vorstellungsleben des Fünfzigjähri­gen: es ist etwas ganz anderes geworden, bis in das Seelen-gefüge hinein.",
        "Wir können es nicht ein Dauerndes nennen, aber überall finden wir in ihm den Mittelpunkt, von dem wir sagen müssen, daß er etwa durch folgendes in der Vor­stellung erreicht wird.",
        "Die Gegenstände der Außenwelt stehen da.",
        "Da steht dieses, dort steht jenes, da ein drittes.",
        "Zwei Menschen treten vor die Dinge.",
        "Dieselben Dinge sieht das Auge, aber sie sind für den einen so, für den anderen anders.",
        "Der eine sagt: Ich mag das; der andere sagt: Ich mag es nicht. - Wenn in der Außenwelt alles dasselbe ist, dieselben Eindrücke da sind, und die eine Seele sagt: Ich mag es, - die andere sagt: Ich mag es nicht, - wenn also die Art des Lebens verschieden ist, so ist ein Mittelpunkt da, der verschieden ist von allem Äußeren, der unerschütterlich bleibt, trotz allem Wechsel des Bewußtseins und des Kör­pers.",
        "Etwas ist da, das vor der Geburt da war und nach der"
      ],
      [
        "Geburt da sein wird, mein besonderes Ich.",
        "Dieses mein be­sonderes Ich hat nicht mit der Geburt begonnen."
      ],
      [
        "Nicht darauf kommt es an, wie man sich mit den west­europäischen Gewohnheiten zu einem solchen Ausspruch stellt, sondern darauf, daß man die Empfindung hat: einen solchen Ausspruch kann man tun.",
        "Darin zeigt sich die Größe der Seele.",
        "Darin zeigt sich, daß die Seele lebt und wie sie lebt.",
        "Darin ist die Unsterblichkeit verbürgt."
      ],
      [
        "So sehen wir, wie Tolstoj hart an die Grenze heran­kommt von dem, was wir, durch die geisteswissenschaftliche Vertiefung verwirklicht, als das innerste Wesen der Seele kennenlernen.",
        "Er ist eingezwängt durch die Welt, die er selbst so sehr bekämpft und kann nicht vordringen zu dem wahren Lebensgang dessen, was vor der Geburt da ist, und dessen, was nach dem Tode kommt.",
        "Er kommt nicht zu der Lehre von Reinkarnation und Karma.",
        "Ebensowenig kommt er auf den inneren Impuls der Seele wie Carnegie, der ihn geradezu fordert.",
        "So sehen wir, ob ein Mensch aus tiefstem Inneren in Widerspruch ist mit alledem, was in der Gegen­wart lebt, wirkt und strebt, oder ob er, als ein Ja-Sager, mit alledem übereinstimmt, was sich in der Gegenwart als Lebensform auslebt; er wird geführt an die Pforten dessen, was wir die anthroposophische Lebensanschauung nennen.",
        "Tolstoj würde den Weg zu Carnegie finden können, Carne­gie niemals zu Tolstoj"
      ],
      [
        "Durch diesen Vortrag sollte gezeigt werden, daß eine Welt- und Lebensanschauung gegeben werden kann, die in die unmittelbare Lebenspraxis hineinführt, die hinuntertra­gen kann das Neuerkannte zu dem Bekannten, zu dem Vollführten.",
        "Und so werden wir sehen, wenn wir immer tiefer und tiefer uns in diese Geisteswissenschaft hinein-finden, wie sie für die Menschen sowohl der einen als der anderen Schattierung das bringt, was das Leben bringen"
      ],
      [
        "muß, was ja schließlich in seiner Art Tolstoj gefunden hat, was Carnegie in seiner Art gefunden hat: ein in sich befrie­digtes Leben.",
        "Aber darauf kommt es nicht an, daß der un­mittelbare Sucher das befriedigte Leben findet, und daß die, welche mit ihm suchen, es auch finden können.",
        "Was Tolstoj für sich und was Carnegie für sich als befriedigend gefun­den haben, das kann nur auf unpersönlichem, reinem Wege und durch ein auf die Ebene des Geistes gerichtetes Erken­nen für alle Menschen, die auf diesem Wege suchen, gefun­den werden, wenn in wahrer Geist-Erkenntnis das, was von Leben zu Leben geht, was Bürgschaft für die Ewigkeit in sich trägt - und was Tolstoj in gewisser Weise, weil er es schon geahnt hat, für sich selbst fand -, für alle Menschen gefunden sein wird."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "DIE PRAKTISCHE AUSBILDUNG DES DENKENS Berlin, 11. Februar 1909",
    "paragraphs": [
      "Die anthroposophische Geisteswissenschaft, welche hier in diesen Vorträgen, natürlich nur stückweise, zur Darstellung kommen soll, wird wohl von sehr vielen Menschen, die sie nicht kennen oder nicht kennen wollen, als ein Gebiet an-gesehen für Träumer, Phantasten und solche Menschen, die eigentlich, wie man so leicht sagt, im wirklichen, im prak­tischen Leben nicht drinnenstehen. Allerdings, wer ober­flächlich aus dieser oder jener Broschüre oder aus einem einzelnen Vortrage sich spärlich unterrichten will über den Inhalt und das Ziel der Geisteswissenschaft, der wird leicht zu einem solchen Urteile kommen können, insbesondere wenn er ausgerüstet ist mit dem geringen Willen, in die geistigen Welten einzudringen, der ja heute so reichlich vorhanden ist, oder wenn er ausgerüstet ist mit den Sugge­stionen, die heute so zahlreich gegen dieses Gebiet vor­handen sind. Und kommt dann noch bewußt oder unbe­wußt böser Wille dazu, dann ist leicht das Urteil fertig:",
      "Ach, diese Geisteswissenschaft hat es ja zu tun mit Dingen, mit denen sich der praktische Mensch nicht abgeben soll, um die er sich nicht kümmern soll!",
      "Die Geisteswissenschaft selbst aber fühlt sich innig ver­wandt mit den allerpraktischsten Gebieten des Lebens, und wo sie recht betrieben wird, da legt sie den allergrößten Wert darauf, daß das Praktischste, das praktische Denken, eine besondere Ausbildung erfahre. Anthroposophische Geistes­wissenschaft will nicht etwas sein, das irgendwo weltenferne",
      "im Wolkenkuckucksheim schwebt und den Menschen abzieht vom täglichen Leben, sondern sie soll etwas sein, was uns jeden Augenblick dienen kann bei allem, was wir denken, tun und fühlen. Zweitens aber ist sie durchaus eine Vorbereitung zu jenen Stufen hinauf, durch die der Mensch selbst eindringt in die höheren Welten. Es ist oft betont worden, daß Geisteswissenschaft nicht nur für den einen Wert habe, der selber schon geöffnete Augen habe, um ein­zudringen in die geistige Welt, sondern daß der gesunde Verstand genügt, um einzudringen in die Mitteilungen von den geistigen Welten, und daß diese Mitteilungen für den Menschen einen unendlichen Wert haben lange, bevor er eindringen kann in die geistigen Welten. Dennoch ist Gei­steswissenschaft für jeden eine Vorbereitung, später selbst hineinzudringen in die höheren Welten.",
      "Wir haben zum Teil schon gesprochen, zum Teil werden wir noch zu sprechen haben von den verschiedenen Metho­den und Verrichtungen, die der Mensch vorzunehmen hat, um hinaufzudringen in die geistigen Welten. Aber da ist immer unbedingte Voraussetzung dabei: Wer hinaufdrin­gen will in die geistigen Welten, wer die genau angegebenen Methoden der Geisteswissenschaft auf sich anwenden will, der sollte nie den Gang in die höheren Gebiete des Lebens wagen, ohne auf dem Grunde eines gesunden, eines prak­tisch ausgebildeten Denkens zu stehen. Dieses gesunde Den­ken ist der Führer, das wahre Leitmotiv, um hineinzudrin­gen in die geistigen Welten. Und am besten gelangt hinein durch die Methoden der Geisteswissenschaft, wer es nicht verschmäht, sich streng zu erziehen zu einem an die Wirk­lichkeit und ihre Gesetze gebundenen Denken. Allerdings, wenn man vom wirklichen praktischen Denken spricht, kommt man leicht in Gegensatz zu dem, was sich in unserer Welt Praxis und auch wohl Denkpraxis nennt. Um diese",
      "zu charakterisieren, braucht man nur an etwas zu erinnern, was hier schon oft angedeutet ist. Was ist die Praxis, von der heute die praktischen Menschen reden? Irgend jemand wird in die Lehre zu irgendeinem Meister gegeben. Da lernt er alle Maßnahmen, die seit Jahrzehnten oder seit Jahr­hunderten vorgenommen sind, und je weniger er dabei denkt, je mehr er in den ausgelaufenen Bahnen geht, desto praktischer findet ihn die Welt. Man findet oftmals das un­praktisch, was von alledem, was man seit langer Zeit treibt, irgendwie abweicht. Das Aufrechterhalten einer solchen Praxis ist einfach an die Brutalität, an die Gewalt gebun­den, nicht an die Vernunft. Wer an irgendeiner ausschlag­gebenden Stelle steht, der dringt durchaus darauf, daß alle andern ebenso vorgehen wie er, und wenn er die Macht hat, drängt er alle hinaus, die anders vorgehen wollen.",
      "Dann kommt das heraus, was ähnlich ist wie der Fall, der hier schon öfter angeführt worden ist. Ein großer Fort­schritt sollte eingeführt werden, die Eisenbahn von Fürth nach Nürnberg. Da sollte auch ein eminent praktisches Kollegium, das bayrische Medizinalkollegium, sein Urteil abgeben, und das Urteil war: Nicht bauen, denn die Ner­ven werden durchaus ruiniert; und wenn man schon Eisen­bahnen bauen wolle, so müsse man sie links und rechts mit hohen Wänden umgeben, damit vorübergehende Menschen keine Gehirnerschütterung bekämen. Das ist 1835 gesche­hen, also gar noch nicht so lange her. Ob die Praktiker auf demselben Gebiete auch heute noch als Praktiker aufgefaßt würden, ist ja die Frage.",
      "Ein anderes Beispiel, das uns so recht zeigen kann, ob die Fortschritte von denen ausgehen, die sich im Leben Prak­tiker nennen, oder von anderen Leuten. Sie finden es sicher sehr praktisch, daß man heute nicht mehr mit jedem Brief zur Post gehen und daß hier aus einem Reisebuche erst das",
      "Porto nach der Entfernung bestimmt werden muß. Erst in den vierziger Jahren des neunzehnten Jahrhunderts wurde das einheitliche Briefporto in England erfunden. Aber nicht ein Praktiker des Postwesens hat es erfunden, sondern ein solcher hat, als die Sache im Parlamente beschlossen werden sollte, gesagt, erstens glaube er nicht, daß sich ein solcher Vorteil ergeben würde, wie Hill da herausrechne, sondern man müßte dann ja das Postgebäude noch vergrößern. Er konnte sich nicht denken, daß das Postgebäude sich nach dem Verkehr und nicht umgekehrt der Verkehr sich nach dem Postgebäude richtet. Und als die erste Bahn von Berlin nach Potsdam gebaut werden konnte, da sagte ein Prak­tiker, nämlich der, welcher seit Jahren zwei Postkutschen nach Potsdam fahren ließ: Wenn die Leute ihr Geld durch­aus aus dem Fenster werfen wollten, dann könnte man die Bahn ja bauen.",
      "Also die sogenannten Praktiker waren durchaus nicht die praktischen Menschen, wenn die großen Dinge des Lebens in Betracht kamen. Daher kann man in Gegensatz zu den Praktikern kommen, wenn man von der praktischen Aus­bildung des Denkens spricht. Dem unbefangenen Beobach­ter bietet sich auf allen Gebieten des Lebens etwas dar, was einem zeigen kann, wie es mit der wahren Praxis im Leben steht. Was praktisches Denken zum Beispiel verhindern kann, trat mir einst an einem ganz anschaulichen Beispiel entgegen. Ein Freund aus meiner Studienzeit kam einmal aufgeregt mit ganz rotem Kopfe zu mir. Er sagte, er müsse gleich zum Professor gehen und ihm mitteilen, daß er eine große Erfindung gemacht habe. Er kam dann zurück und sagte, er könne den Fachmann erst in einer Stunde spre­chen, und dann entwickelte er mir seine Erfindung. Es war eine Einrichtung, die darin bestand, daß man mit Auf­wendung einer ganz geringen Menge einmal zugeführter",
      "Dampfkraft die Maschine in Bewegung setzte, und die Maschine leiste dann fortwährend eine ungeheuere Arbeit. Mein Freund war selbst erstaunt darüber, daß er so klug war, aber die Sache schien zu stimmen. Ich sagte ihm, man solle das Ganze auf einen einfachen Gedanken zurückfüh­ren. Ich sagte: «Denke, Du ständest in einem Eisenbahn­wagen und Du versuchtest, ganz fest gegen die Wände des Wagens zu stoßen, um zu sehen, ob der Wagen so fort­zuschieben ware.»",
      "Mir wurde damals klar, daß ein Haupthindernis alles praktischen Denkens mit einem Terminus technicus bezeich­net werden könnte: Man ist ein Wagenschieber von innen! Das heißt, man ist imstande, ein engbegrenztes Gebiet zu überschauen und hier das, was man gelernt hat, anzuwen­den; aber man ist durch seine Veranlagung gezwungen, dabei auch stehenzubleiben und nicht zu bedenken, daß das ganze Bild sich wesentlich ändert, wenn man aus dem Wagen heraustritt.",
      "Das ist einer der Grundsätze, die vor allen Dingen bei einer praktischen Ausbildung des Denkens beachtet werden müssen. Eine mit einer gewissen inneren Trägheit des Den­kens verbundene Eigentümlichkeit ist, daß das Denken sich gerne einkapselt und das, was draußen ist, vergißt, auch wenn es eng mit dem Betrachteten zusammenhängt. Ich habe Ihnen früher angeführt, daß man die Kant-Laplacische Theorie wie folgt beweisen will: Einstmals war der Welten-nebel da. Dieser kam durch irgendeine Ursache in Rotation; dadurch teilten sich allmählich die einzelnen Planeten des Sonnensystems ab und erhielten die Bewegung, die sie noch heute innehaben. Man macht das sehr deutlich klar an einem Schulexperiment. Man läßt ein Ölkügelchen in einem Gefäße in Wasser schweben. Es wird dann ein Aquator aus einem Kartonblatt ausgeschnitten. Diesen legt man unter",
      "das Ölkügelchen Dann wird eine Nadel durch dieses hin­durchgesteckt, gedreht - und es teilen sich in der Aquator­gegend kleine Ölkügelchen ab, wie Planeten, und sie be­wegen sich um das größere Kügelchen. Man hat dann in denkerischer Beziehung nur das vergessen, daß man «ein Wagenschieber von innen» ist. Man hat sich selbst ver­gessen, was ja sonst manchmal recht gut ist; man hat ver­gessen, daß man selber die Sache gedreht hat. Bei einem Versuch muß man aber alle Dinge, auf die es ankommt, ins Feld führen.",
      "Zuerst muß man den Glauben und das Vertrauen haben an die Wirklichkeit, an die Realität der Gedanken. Aus einem Glase, in dem kein Wasser ist, kann man kein Wasser herausschöpfen; aus einer Welt, in der keine Gedanken sind, kann man keine Gedanken herausholen. Es ist das Absurdeste, anzunehmen, daß alle Gedanken nur in uns selber sich abspielen. Niemand sollte glauben, daß er aus einer Welt, die nicht nach Gedanken gestaltet und geformt ist, irgendeinen Gedanken herausholen könne. Es ist kein Gedanke in unserer Seele, der nicht zuerst draußen in der Welt gewesen ist. Aristoteles hat richtiger als mancher Mo­derne gesagt: Was der Mensch in seinem Denken zuletzt findet, das ist in der Wek draußen als erstes vorhanden.",
      "Hat man aber dieses Vertrauen zu dem Bestehen der Gedanken in den Dingen selber, dann wird man einsehen, daß man sich erziehen muß zum Denken an dem Denken, das man immer vor Augen haben muß, an jenem Denken, dem gegenständlichen Denken, das sich so wenig wie mög­lich absondert von den Dingen. Heinroth tat von Goethe den schönen Ausspruch, daß sein Denken ein gegenständ­liches sei, ein solches, bei dem die Gedanken nichts anderes ausdrücken, als was in den Dingen selber enthalten ist, und daß in den Dingen nichts anderes gesucht wird als gerade",
      "der ideale, der schöpferische Gedanke. Wenn man die Realität der Gedanken einsieht, so wird man einsehen, wie man sich an der Realität erziehen kann zu einem wirklich praktischen, gesunden Denken.",
      "Dreierlei ist da zu beachten: Erstens muß und soll der Mensch Interesse entwickeln für die äußere uns umgebende Wirklichkeit, Interesse in bezug auf den Tatsachensinn und den Gegenstandssinn. Interesse an der Umwelt, das ist das Zauberwort für die Gedankenerziehung. Lust und Liebe an dem, was wir tun, ist das zweite. Und Befriedigung im Nachsinnen, das ist das dritte. Wer das versteht, daß dies die drei Hauptforderungen sind, der wird bald einsehen, was für Forderungen an eine praktische Ausbildung des Denkens zu stellen sind.",
      "Der größte Feind des Denkens ist im Grunde genommen oft das Denken selber. Wenn man nämlich glaubt, nur man selber könne denken und die Dinge hätten nicht Gedanken in sich, so steht man eigentlich der Denkpraxis feindlich gegenüber. Denken wir einmal, ein Mensch hätte sich einige engbegrenzte Vorstellungen gemacht vom Menschen, hätte sich ein paar schablonenhafte schematische Begriffe von den Menschen gemacht. Nun tritt ihm irgendein Mensch ent­gegen, der annähernd die Eigenschaften hat, die in seine Schablone passen. Dann ist er fertig mit seinem Urteil und glaubt nicht, daß dieser Mensch ihm noch etwas Besonderes sagen kann. Gehen wir an alles heran mit dem Gedanken, daß es uns etwas Besonderes sagen kann, daß wir nicht be­rechtigt sind, irgend etwas anderes über die Dinge urteilen zu lassen als die Dinge selber, so werden wir bald die Frucht dieses Verhaltens sehen. Der Glaube, daß uns die Dinge viel mehr sagen können, als wir über die Dinge zu sagen vermögen, ist wieder ein solches Zauberideal für die Praxis des Denkens.",
      "Man denke einmal, daß ein Mensch es über sich brächte, folgende beide Grundsätze gelten zu lassen. Er steht der Tatsache gegenüber, daß jemand gerade heute einen Gang da oder dorthin gemacht hat. Nun will sich der Betreffende denkerisch erziehen. Dann ist es gut, wenn er sich fragt:",
      "Wie ist diese heutige Handlung aus den Ursachen von gestern, vorgestern und so weiter entstanden? Ich gehe zu­rück auf das, was nach meinem Denken als Ursache anzu­sehen ist. Habe ich mir ein solches Ereignis ausgesucht, das ich nachher nachprüfen kann, wo meine Gedanken mit dem, was ich als die Ursache erfahren kann, übereinstim­men, so ist das gut. - Es wird aber in den meisten Fällen nicht der Fall sein. Ist es der Fall, dann kann man die fal­schen Gedanken vergleichen mit dem richtigen Gang der Ereignisse. Dann wird man merken, daß man nach und nach, nach kürzerer oder längerer Zeit, nicht mehr Fehler machen wird, sondern daß man einen Gedanken heraus-schälen kann aus einer Tatsache, der den objektiven Tat­sachen entspricht. Oder man versucht, sich aus einem Er­eignis zu konstruieren, was morgen oder in ein paar Stunden aus diesem Ereignis folgen kann. Auch dies wird zunächst nicht stimmen, aber das Denken wird sich bald so hinein-leben in die Dinge, daß die Dinge so verlaufen wie die Ge­danken, die man sich darüber macht. Verbietet man sich nun noch, abgezogene, abstrakte Gedanken zu bilden, so wird man allmählich fühlen, wie man mit den Dingen zu­sammenwächst.",
      "Es gibt Leute, die mit einem gewissen Instinkt hinge-drängt werden zu einem solchen Denken, so zum Beispiel Goethe. Sein Denken war nicht im Kopfe, sondern in den Dingen. Goethe, der einmal Advokat gewesen ist, hat nicht viel von den Gesetzen gewußt; aber ein sicherer Instinkt sagte ihm, was man in den einzelnen Fällen vornehmen",
      "muß. Es gab kein langes Nachschlagen und Durchstudieren von Akten, wenn wieder ein Fall von neuem vorgenommen werden mußte. Wenn einmal alle Ministerakte Goethes ver­öffentlicht werden, dann wird die Welt erst sehen, wie Goethe eine eminent praktische Natur war, kein weltfrem­der Mensch. So war er bei einer Rekrutenaushebung, beob­achtete da alles, was vorging - und dabei schrieb er die Iphigenie! Vergleichen Sie damit, durch was alles ein heu-tiger Dichter bei der Arbeit nicht gestört werden darf. Und doch war Goethe ein viel größerer Dichter als alle, die heute nicht gestört werden dürfen. Wegen des eminent praktischen Denkens konnte er zum Beispiel auch sagen, wenn er ans Fenster trat: Heute können wir nicht hinaus­gehen, denn in drei Stunden wird es regnen. - Er hatte Wolkenstudien gemacht, aber keine grobe Theorie auf­gestellt. Das hängt allerdings mit einer gewissen Selbstlosig­keit zusammen. Wer zunächst nur an sich denkt, wird es nicht weit bringen. Wer hinterher gleich ausruft, wenn er etwas verglichen hat: Aha, hatte ich's nicht gesagt! -, der wird es nicht weit bringen. Das gedankenvolle Haften an den Dingen ist das erste, so daß man in den Dingen selber denkt.",
      "Das zweite ist Lust und Liebe an dem, was man tut. Sie sind nur dann in wirklichem Sinne vorhanden, wenn es auf den Erfolg nicht ankommt. Wem es nur auf den Erfolg an­kommt, der kann nicht diese Ruhe entwickeln, die nötig ist, damit Lust und Liebe uns allmählich inspirieren kön­nen. Bei nichts lernt man mehr, als wenn man sich mit etwas beschäftigt, nur weil es einem Freude macht. Wenn wir nicht imstande sind, uns an den Mißerfolgen ebenso zu freuen wie an den Erfolgen, so können wir uns niemals von den Dingen die Gedanken sagen lassen, die in ihnen liegen.",
      "Drittens müssen wir Befriedigung finden in dem Denken",
      "selber. Das wird heute am meisten bekämpft. Man hört heute so viel sagen: Was brauchen unsere Kinder das und das zu lernen? Das haben sie ja im Leben nicht nötig. -Das ist der allerunpraktischste Grundsatz.",
      "Es muß Gebiete geben für den Menschen, wo die bloße denkerische Tätig­keit ihm Befriedigung gewährt, ohne daß er erwartet, ob das Denken zu einem Erfolge führen wird. Was der Mensch auch für einen Beruf hat: wenn er nicht Zeit findet, wenn auch nur ganz kurz, irgend etwas zu tun, was er rein denke­risch betreibt und was ihn denkerisch befriedigt, wenn er ein solches Gebiet nicht findet, so kann er immer nur in aus­getretenen Geleisen bleiben.",
      "Findet er aber so etwas, dann hat er etwas, das eine große, starke Wirkung auf ihn aus­übt, etwas, das in die feinere Organisation seines Organis­mus hineinwirkt. Niemals schöpferisch-bildend wirken die Dinge, die uns an den Leib fesseln.",
      "Die nutzen unsere Fähig­keiten ab. Die Dinge, die wir nur zu unserer eigenen denke­rischen Befriedigung treiben, die schaffen uns Lebenskräfte, die gehen bis in die feinste Organisation unseres Organismus und erhöhen unsere Bildung.",
      "Durch das, was wir in uns zu unserer Befriedigung arbeiten, schaffen wir etwas, durch das wir weiterkommen in der Welt. Wenn wir damit dann an das praktische Leben herantreten, so wird sich zeigen, daß das richtig ist.",
      "Bleibt man gefesselt an die Lebenspraxis, so macht sie immer denselben Eindruck, und man hat nicht die Freiheit, Initiative zu entwickeln. Bildet man sich aber höher durch eine solche freie denkerische Tätigkeit, dann steht man sozusagen als zwei Wesen einem solchen Eindruck gegenüber.",
      "Daher gibt es zwar Zeitverlust, wenn man so etwas treibt, was der Lebenspraxis nicht unmittelbar ange­hört, mittelbar fördert es aber die Lebenspraxis durchaus.",
      "Das sind die drei Grundgesetze für die Ausbildung des Denkens. Sehen Sie, wie schön einer der Menschen, die in",
      "außerordentlich scharfsinniger Weise in die Zusammenhänge des Lebens hineingeschaut haben, Leonardo da Vinci, das gewußt hat. Er beschreibt genau, wie man verfahren müsse, wenn man Lust und Liebe an der Arbeit entwickeln will.",
      "Das sind solche Dinge, die uns zunächst zeigen, wie wir durch das Vertrauen in den Weltenaufbau hineinwachsen in die denkerische Praxis, aber auch, indem wir an das Den­ken selber glauben. Der wird viel tun, der systematisch fol­gendes macht: Er denkt über irgend etwas nach; es kann das Alleralltäglichste sein oder das Allerhöchste.",
      "Will man nun rasch eine Lösung finden, so geschieht das meistens nicht durch praktisches Denken. Man soll sich nicht zu viel in die Gedanken hineinmischen. Das ist eine der Hauptforderun­gen: daß wir die Gedanken in uns wirken lassen, daß wir uns gewöhnen, uns zum Schauplatz für das Wirken unseres Denkens zu machen.",
      "Wir können meinen, die Sache lasse sich auf eine bestimmte Weise machen. Aber wir sind keine Dogmatiker. Wir sagen uns daher, es könnte auch so ge­macht werden, vielleicht noch auf eine dritte, vierte oder zehnte Art.",
      "Man muß so sorgfältig, als ob man gar nicht beteiligt wäre, die Sache vor sich hinmalen. Natürlich geht das nur Dingen gegenüber, die sich so behandeln lassen. Man hat die zehn Lösungen; man führe jede mit Liebe aus, und dann lasse man die Sache liegen.",
      "Man darf gar nicht mehr darüber nachdenken, man muß die Gedanken wirken lassen. Man muß sich sagen: Die Gedanken sind Mächte, die in meiner Seele wirken, auch wenn ich nicht dabei bin. Ich warte bis morgen oder übermorgen.",
      "Ich mache es dann vielleicht noch ein zweites oder drittes Mal, und jedesmal wird sich die Frage besser lösen lassen. Ich handle dann aus dem Gedanken heraus, daß die Gedanken eine Wirklichkeit sind, die auch fortwirkt, ohne daß ich sozusagen dabei bin.",
      "Wer dieses eine Zeitlang macht, der wird sehen, wie vielseitig",
      "sein Denken wird, wie er sich zur Schlagfertigkeit entwickelt. Dann wird man dadurch zusammenwachsen, bis in die alleralltäglichsten Dinge hinein zusammenwach­sen mit dem, was geschickt und ungeschickt, was tölpisch und weise ist. Man wird sich niemals so benehmen, wie sich manchmal sogenannte sehr praktische Menschen verhalten. Wenn Sie solche Menschen zum Beispiel auf Reisen sehen, irgendwo, wo sie sich nicht zu Hause fühlen, da nehmen sie sich manchmal recht sonderbar aus. Bis in die Hände her­unter, bis in die Art und Weise, wie man etwas anfaßt, wird das wirken. Viel weniger werden Sie Teller und Töpfe fallen lassen als andere. Praktisches Denken wirkt bis in die Glieder hinein, wenn es täglich und nicht in abstrakter Weise vorgenommen wird.",
      "Das unpraktische Denken zeigt sich gerade am besten da, wo das Denken in der Wissenschaft wirken sollte. Ich habe Ihnen das hypothetische Beispiel aus der Astronomie angeführt. Aber auch in der Gegenwart sind die Wissen­schaften manchmal furchtbar unpraktisch. Die Art, wie sich der heutige Mensch über Dinge hermacht, die einen so unendlichen Wert haben, ist manchmal schauderhaft. Mit Mikroskopen beobachtet man heute Pflanzen. Man sieht merkwürdige Gebilde an der Pflanze, die facettenartige Form zeigen wie die Augen von Insekten, bei manchen Pflanzen selbst etwas wie eine Linse. Man beobachtet in­sektenfressende Pflanzen und so weiter. Das sind wichtige Beobachtungen. Aber man verwechselt das, was im Menschen die Dinge widerspiegelt, mit dem, was man äußerlich an den Pflanzen beobachtet, und wirft ganz konfus durchein­ander Pflanzenseele, Tierseele und Menschenseele. Sie kön­nen das in vielen populären Schriften lesen. Es soll hier nichts gesagt werden gegen die wunderbaren Beobachtun­gen, die durch diese populären Schriften in dieWelt gebracht",
      "werden. Aber die Gedanken sind so, daß es den, der den­ken kann, eigentlich an das Folgende erinnert: Ich kenne eine Art Wesen, die sehr, sehr kunstreich organisiert ist. Sie hat ein Organ in sich, durch welches kleine Wesen wie mit magnetischer Kraft angezogen und verschlungen werden. Dieser Gedanke ist ganz derselbe wie der bei den Pflanzen-beobachtungen, aber das Wesen, das ich im Auge habe, ist -die Mausefalle! Sie können genauso gut von einer Beseelung der Mausefalle sprechen wie von der Beseelung der Pflan­zen, in dem Sinne, wie dieses Denken es will. Auch hier darf man kein innerer Wagenschieber sein.",
      "Dann gibt es aber noch etwas anderes, außerordentlich Wichtiges: daß man Vertrauen hat zu dem innersten geisti­gen Denkorgan. Bei den meisten Menschen sorgt ja die Natur dafür, daß die Menschen sozusagen nicht immer da­bei sind; der Mensch muß ja schlafen. Da wirkt diesesDenk­organ für sich, und der Mensch kann es nicht fortwährend ruinieren. Aber es kommt doch sehr darauf an, ob der Mensch nur die Natur für sich wirken läßt, oder ob man die Ausbildung in die Hand nimmt. Man sollte einmal, wenn auch noch so kurze Zeit, am Tage sich dazu zwingen, gar nichts zu denken. Es ist viel leichter, diese auf- und abflutenden Gedanken wirken zu lassen, bis man erlöst wird durch den Schlaf, als sich zu zwingen, nichts zu den­ken. Dann wirkt das Denkorgan so, daß es Kraft sammelt. LJnd wer sich immer wieder in die Möglichkeit versetzt, nicht zu denken, der wird sehen, wie die Schlagfertigkeit namentlich dadurch wächst, daß er nicht nur den Schlaf auf den Denkapparat wirken läßt, sondern die Führung über­nimmt in der Ausbildung dieses Denkorgans.",
      "Nur wer von allen Geistern der Spiritualität verlassen ist, kann glauben, daß dann überhaupt nicht gedacht wird. Hier gilt das Wort, das Goethe von der Natur sagt: «Gedacht",
      "hat sie und sinnt beständig. » Auch wenn der Mensch gar nicht dabei ist bei seinem Denken, dann denkt etwas in ihm, dessen er sich nur nicht bewußt ist. In diesen Momen­ten, wo der Mensch ohne seine eigenen persönlichen Gedan­ken daliegt, denkt wirklich ein Höheres in ihm. Das Über-bewußte in ihm, das Göttliche in ihm läßt der Mensch dann in sich wirken und weben. Es kündet sich nicht un­mittelbar an, aber in seinen Wirkungen. Es gehört eine ge­wisse Tatkraft dazu, um eine solche Denkübung vorzu­nehmen.",
      "So sehen Sie, wie man das Denken erziehen kann. Heute konnten nur einzelne Beispiele der Selbsterziehung des Den­kens gegeben werden, aber diese Beispiele haben gezeigt, daß man auf wirkliche Heilmittel des Denkens hinzuweisen vermag, deren Früchte nur die Erfahrung, das Leben selbst zu geben vermag. Wer so sein Denken schult, der wird fin­den, daß er auf der einen Seite hinaufsteigen kann in die höchsten Gebiete geistigen Lebens, daß er aber auf der an­dern Seite auch bei den allerpraktischsten Dingen sein Den­ken anwenden kann. Das, was beim Überblicken der geisti­gen Tatsachen gewonnen wird, soll angewandt werden auf das praktische Leben. Alle Gebiete, aber besonders auch die Pädagogik, könnten hierdurch gewinnen. Eine ganz andere Anschauung über Lebenspraxis würde sich ringsherum gel­tend machen. Aber auch der, der hinaufdringen will in die höheren Welten, würde eine sichere Basis haben. Das ist wiederum etwas, was durchaus gefordert werden muß. Und auch die gewöhnliche Wissenschaft würde Ungeheures ge­winnen, wenn sie sich anlehnen wollte an die Geisteswissen­schaft.",
      "Die Wagenschieber des Denkens haben nicht dieses prak­tische Denken; ihnen fehlt es. Sie vermögen nicht, irgend etwas zurückzuführen auf einen einfachen, umfassenden",
      "Gedanken. Das ist, was die Geisteswissenschaft gibt: sie macht uns fähig, das, was sonst fein ausziseliert ist im Leben, unter großen Gesichtspunkten zu überschauen. Dann wird der Mensch von allen unfruchtbaren Spekulationen abge­lenkt, dann wird er zur wirklichen Lebenspraxis geführt. Sehen wir Leonardo da Vinci an, den wir zum Vorbild nehmen können. Er sagt: Theorie ist der Kapitän, Praxis sind die Soldaten.",
      "Wer an die Praxis geht ohne das beherrschende Denken, gleicht dem, der sich auf ein Schiff begibt ohne Kompaß, ohne die Möglichkeit, das Schiff zu steuern. Goethe hat darauf hingewiesen, wie gerade die Wissenschaft durch un­praktisches Denken zu unfruchtbaren Gedanken kommt. Da gibt es Leute, welche die Außenwelt auf Atome, und andere, die sie auf Bewegungen zurückführen; andere leug­nen wieder die Bewegung. Demgegenüber weisen die prak­tischsten Denker darauf hin, daß Einfachheit aus der Größe der Weltanschauung kommt. Er ist durchaus treffend, der Ausspruch, und wir können auch den Goetheschen Spruch uns vor Augen stellen:",
      "Es mag sich Feindliches eräugnen,",
      "Du bleibe ruhig, bleibe stumm;",
      "Und wenn sie Dir die Bewegung leugnen,",
      "Geh ihnen vor der Nas' herum."
    ],
    "sentences": [
      [
        "Die anthroposophische Geisteswissenschaft, welche hier in diesen Vorträgen, natürlich nur stückweise, zur Darstellung kommen soll, wird wohl von sehr vielen Menschen, die sie nicht kennen oder nicht kennen wollen, als ein Gebiet an-gesehen für Träumer, Phantasten und solche Menschen, die eigentlich, wie man so leicht sagt, im wirklichen, im prak­tischen Leben nicht drinnenstehen.",
        "Allerdings, wer ober­flächlich aus dieser oder jener Broschüre oder aus einem einzelnen Vortrage sich spärlich unterrichten will über den Inhalt und das Ziel der Geisteswissenschaft, der wird leicht zu einem solchen Urteile kommen können, insbesondere wenn er ausgerüstet ist mit dem geringen Willen, in die geistigen Welten einzudringen, der ja heute so reichlich vorhanden ist, oder wenn er ausgerüstet ist mit den Sugge­stionen, die heute so zahlreich gegen dieses Gebiet vor­handen sind.",
        "Und kommt dann noch bewußt oder unbe­wußt böser Wille dazu, dann ist leicht das Urteil fertig:"
      ],
      [
        "Ach, diese Geisteswissenschaft hat es ja zu tun mit Dingen, mit denen sich der praktische Mensch nicht abgeben soll, um die er sich nicht kümmern soll!"
      ],
      [
        "Die Geisteswissenschaft selbst aber fühlt sich innig ver­wandt mit den allerpraktischsten Gebieten des Lebens, und wo sie recht betrieben wird, da legt sie den allergrößten Wert darauf, daß das Praktischste, das praktische Denken, eine besondere Ausbildung erfahre.",
        "Anthroposophische Geistes­wissenschaft will nicht etwas sein, das irgendwo weltenferne"
      ],
      [
        "im Wolkenkuckucksheim schwebt und den Menschen abzieht vom täglichen Leben, sondern sie soll etwas sein, was uns jeden Augenblick dienen kann bei allem, was wir denken, tun und fühlen.",
        "Zweitens aber ist sie durchaus eine Vorbereitung zu jenen Stufen hinauf, durch die der Mensch selbst eindringt in die höheren Welten.",
        "Es ist oft betont worden, daß Geisteswissenschaft nicht nur für den einen Wert habe, der selber schon geöffnete Augen habe, um ein­zudringen in die geistige Welt, sondern daß der gesunde Verstand genügt, um einzudringen in die Mitteilungen von den geistigen Welten, und daß diese Mitteilungen für den Menschen einen unendlichen Wert haben lange, bevor er eindringen kann in die geistigen Welten.",
        "Dennoch ist Gei­steswissenschaft für jeden eine Vorbereitung, später selbst hineinzudringen in die höheren Welten."
      ],
      [
        "Wir haben zum Teil schon gesprochen, zum Teil werden wir noch zu sprechen haben von den verschiedenen Metho­den und Verrichtungen, die der Mensch vorzunehmen hat, um hinaufzudringen in die geistigen Welten.",
        "Aber da ist immer unbedingte Voraussetzung dabei: Wer hinaufdrin­gen will in die geistigen Welten, wer die genau angegebenen Methoden der Geisteswissenschaft auf sich anwenden will, der sollte nie den Gang in die höheren Gebiete des Lebens wagen, ohne auf dem Grunde eines gesunden, eines prak­tisch ausgebildeten Denkens zu stehen.",
        "Dieses gesunde Den­ken ist der Führer, das wahre Leitmotiv, um hineinzudrin­gen in die geistigen Welten.",
        "Und am besten gelangt hinein durch die Methoden der Geisteswissenschaft, wer es nicht verschmäht, sich streng zu erziehen zu einem an die Wirk­lichkeit und ihre Gesetze gebundenen Denken.",
        "Allerdings, wenn man vom wirklichen praktischen Denken spricht, kommt man leicht in Gegensatz zu dem, was sich in unserer Welt Praxis und auch wohl Denkpraxis nennt.",
        "Um diese"
      ],
      [
        "zu charakterisieren, braucht man nur an etwas zu erinnern, was hier schon oft angedeutet ist.",
        "Was ist die Praxis, von der heute die praktischen Menschen reden?",
        "Irgend jemand wird in die Lehre zu irgendeinem Meister gegeben.",
        "Da lernt er alle Maßnahmen, die seit Jahrzehnten oder seit Jahr­hunderten vorgenommen sind, und je weniger er dabei denkt, je mehr er in den ausgelaufenen Bahnen geht, desto praktischer findet ihn die Welt.",
        "Man findet oftmals das un­praktisch, was von alledem, was man seit langer Zeit treibt, irgendwie abweicht.",
        "Das Aufrechterhalten einer solchen Praxis ist einfach an die Brutalität, an die Gewalt gebun­den, nicht an die Vernunft.",
        "Wer an irgendeiner ausschlag­gebenden Stelle steht, der dringt durchaus darauf, daß alle andern ebenso vorgehen wie er, und wenn er die Macht hat, drängt er alle hinaus, die anders vorgehen wollen."
      ],
      [
        "Dann kommt das heraus, was ähnlich ist wie der Fall, der hier schon öfter angeführt worden ist.",
        "Ein großer Fort­schritt sollte eingeführt werden, die Eisenbahn von Fürth nach Nürnberg.",
        "Da sollte auch ein eminent praktisches Kollegium, das bayrische Medizinalkollegium, sein Urteil abgeben, und das Urteil war: Nicht bauen, denn die Ner­ven werden durchaus ruiniert; und wenn man schon Eisen­bahnen bauen wolle, so müsse man sie links und rechts mit hohen Wänden umgeben, damit vorübergehende Menschen keine Gehirnerschütterung bekämen.",
        "Das ist 1835 gesche­hen, also gar noch nicht so lange her.",
        "Ob die Praktiker auf demselben Gebiete auch heute noch als Praktiker aufgefaßt würden, ist ja die Frage."
      ],
      [
        "Ein anderes Beispiel, das uns so recht zeigen kann, ob die Fortschritte von denen ausgehen, die sich im Leben Prak­tiker nennen, oder von anderen Leuten.",
        "Sie finden es sicher sehr praktisch, daß man heute nicht mehr mit jedem Brief zur Post gehen und daß hier aus einem Reisebuche erst das"
      ],
      [
        "Porto nach der Entfernung bestimmt werden muß.",
        "Erst in den vierziger Jahren des neunzehnten Jahrhunderts wurde das einheitliche Briefporto in England erfunden.",
        "Aber nicht ein Praktiker des Postwesens hat es erfunden, sondern ein solcher hat, als die Sache im Parlamente beschlossen werden sollte, gesagt, erstens glaube er nicht, daß sich ein solcher Vorteil ergeben würde, wie Hill da herausrechne, sondern man müßte dann ja das Postgebäude noch vergrößern.",
        "Er konnte sich nicht denken, daß das Postgebäude sich nach dem Verkehr und nicht umgekehrt der Verkehr sich nach dem Postgebäude richtet.",
        "Und als die erste Bahn von Berlin nach Potsdam gebaut werden konnte, da sagte ein Prak­tiker, nämlich der, welcher seit Jahren zwei Postkutschen nach Potsdam fahren ließ: Wenn die Leute ihr Geld durch­aus aus dem Fenster werfen wollten, dann könnte man die Bahn ja bauen."
      ],
      [
        "Also die sogenannten Praktiker waren durchaus nicht die praktischen Menschen, wenn die großen Dinge des Lebens in Betracht kamen.",
        "Daher kann man in Gegensatz zu den Praktikern kommen, wenn man von der praktischen Aus­bildung des Denkens spricht.",
        "Dem unbefangenen Beobach­ter bietet sich auf allen Gebieten des Lebens etwas dar, was einem zeigen kann, wie es mit der wahren Praxis im Leben steht.",
        "Was praktisches Denken zum Beispiel verhindern kann, trat mir einst an einem ganz anschaulichen Beispiel entgegen.",
        "Ein Freund aus meiner Studienzeit kam einmal aufgeregt mit ganz rotem Kopfe zu mir.",
        "Er sagte, er müsse gleich zum Professor gehen und ihm mitteilen, daß er eine große Erfindung gemacht habe.",
        "Er kam dann zurück und sagte, er könne den Fachmann erst in einer Stunde spre­chen, und dann entwickelte er mir seine Erfindung.",
        "Es war eine Einrichtung, die darin bestand, daß man mit Auf­wendung einer ganz geringen Menge einmal zugeführter"
      ],
      [
        "Dampfkraft die Maschine in Bewegung setzte, und die Maschine leiste dann fortwährend eine ungeheuere Arbeit.",
        "Mein Freund war selbst erstaunt darüber, daß er so klug war, aber die Sache schien zu stimmen.",
        "Ich sagte ihm, man solle das Ganze auf einen einfachen Gedanken zurückfüh­ren.",
        "Ich sagte: «Denke, Du ständest in einem Eisenbahn­wagen und Du versuchtest, ganz fest gegen die Wände des Wagens zu stoßen, um zu sehen, ob der Wagen so fort­zuschieben ware.»"
      ],
      [
        "Mir wurde damals klar, daß ein Haupthindernis alles praktischen Denkens mit einem Terminus technicus bezeich­net werden könnte: Man ist ein Wagenschieber von innen!",
        "Das heißt, man ist imstande, ein engbegrenztes Gebiet zu überschauen und hier das, was man gelernt hat, anzuwen­den; aber man ist durch seine Veranlagung gezwungen, dabei auch stehenzubleiben und nicht zu bedenken, daß das ganze Bild sich wesentlich ändert, wenn man aus dem Wagen heraustritt."
      ],
      [
        "Das ist einer der Grundsätze, die vor allen Dingen bei einer praktischen Ausbildung des Denkens beachtet werden müssen.",
        "Eine mit einer gewissen inneren Trägheit des Den­kens verbundene Eigentümlichkeit ist, daß das Denken sich gerne einkapselt und das, was draußen ist, vergißt, auch wenn es eng mit dem Betrachteten zusammenhängt.",
        "Ich habe Ihnen früher angeführt, daß man die Kant-Laplacische Theorie wie folgt beweisen will: Einstmals war der Welten-nebel da.",
        "Dieser kam durch irgendeine Ursache in Rotation; dadurch teilten sich allmählich die einzelnen Planeten des Sonnensystems ab und erhielten die Bewegung, die sie noch heute innehaben.",
        "Man macht das sehr deutlich klar an einem Schulexperiment.",
        "Man läßt ein Ölkügelchen in einem Gefäße in Wasser schweben.",
        "Es wird dann ein Aquator aus einem Kartonblatt ausgeschnitten.",
        "Diesen legt man unter"
      ],
      [
        "das Ölkügelchen Dann wird eine Nadel durch dieses hin­durchgesteckt, gedreht - und es teilen sich in der Aquator­gegend kleine Ölkügelchen ab, wie Planeten, und sie be­wegen sich um das größere Kügelchen.",
        "Man hat dann in denkerischer Beziehung nur das vergessen, daß man «ein Wagenschieber von innen» ist.",
        "Man hat sich selbst ver­gessen, was ja sonst manchmal recht gut ist; man hat ver­gessen, daß man selber die Sache gedreht hat.",
        "Bei einem Versuch muß man aber alle Dinge, auf die es ankommt, ins Feld führen."
      ],
      [
        "Zuerst muß man den Glauben und das Vertrauen haben an die Wirklichkeit, an die Realität der Gedanken.",
        "Aus einem Glase, in dem kein Wasser ist, kann man kein Wasser herausschöpfen; aus einer Welt, in der keine Gedanken sind, kann man keine Gedanken herausholen.",
        "Es ist das Absurdeste, anzunehmen, daß alle Gedanken nur in uns selber sich abspielen.",
        "Niemand sollte glauben, daß er aus einer Welt, die nicht nach Gedanken gestaltet und geformt ist, irgendeinen Gedanken herausholen könne.",
        "Es ist kein Gedanke in unserer Seele, der nicht zuerst draußen in der Welt gewesen ist.",
        "Aristoteles hat richtiger als mancher Mo­derne gesagt: Was der Mensch in seinem Denken zuletzt findet, das ist in der Wek draußen als erstes vorhanden."
      ],
      [
        "Hat man aber dieses Vertrauen zu dem Bestehen der Gedanken in den Dingen selber, dann wird man einsehen, daß man sich erziehen muß zum Denken an dem Denken, das man immer vor Augen haben muß, an jenem Denken, dem gegenständlichen Denken, das sich so wenig wie mög­lich absondert von den Dingen.",
        "Heinroth tat von Goethe den schönen Ausspruch, daß sein Denken ein gegenständ­liches sei, ein solches, bei dem die Gedanken nichts anderes ausdrücken, als was in den Dingen selber enthalten ist, und daß in den Dingen nichts anderes gesucht wird als gerade"
      ],
      [
        "der ideale, der schöpferische Gedanke.",
        "Wenn man die Realität der Gedanken einsieht, so wird man einsehen, wie man sich an der Realität erziehen kann zu einem wirklich praktischen, gesunden Denken."
      ],
      [
        "Dreierlei ist da zu beachten: Erstens muß und soll der Mensch Interesse entwickeln für die äußere uns umgebende Wirklichkeit, Interesse in bezug auf den Tatsachensinn und den Gegenstandssinn.",
        "Interesse an der Umwelt, das ist das Zauberwort für die Gedankenerziehung.",
        "Lust und Liebe an dem, was wir tun, ist das zweite.",
        "Und Befriedigung im Nachsinnen, das ist das dritte.",
        "Wer das versteht, daß dies die drei Hauptforderungen sind, der wird bald einsehen, was für Forderungen an eine praktische Ausbildung des Denkens zu stellen sind."
      ],
      [
        "Der größte Feind des Denkens ist im Grunde genommen oft das Denken selber.",
        "Wenn man nämlich glaubt, nur man selber könne denken und die Dinge hätten nicht Gedanken in sich, so steht man eigentlich der Denkpraxis feindlich gegenüber.",
        "Denken wir einmal, ein Mensch hätte sich einige engbegrenzte Vorstellungen gemacht vom Menschen, hätte sich ein paar schablonenhafte schematische Begriffe von den Menschen gemacht.",
        "Nun tritt ihm irgendein Mensch ent­gegen, der annähernd die Eigenschaften hat, die in seine Schablone passen.",
        "Dann ist er fertig mit seinem Urteil und glaubt nicht, daß dieser Mensch ihm noch etwas Besonderes sagen kann.",
        "Gehen wir an alles heran mit dem Gedanken, daß es uns etwas Besonderes sagen kann, daß wir nicht be­rechtigt sind, irgend etwas anderes über die Dinge urteilen zu lassen als die Dinge selber, so werden wir bald die Frucht dieses Verhaltens sehen.",
        "Der Glaube, daß uns die Dinge viel mehr sagen können, als wir über die Dinge zu sagen vermögen, ist wieder ein solches Zauberideal für die Praxis des Denkens."
      ],
      [
        "Man denke einmal, daß ein Mensch es über sich brächte, folgende beide Grundsätze gelten zu lassen.",
        "Er steht der Tatsache gegenüber, daß jemand gerade heute einen Gang da oder dorthin gemacht hat.",
        "Nun will sich der Betreffende denkerisch erziehen.",
        "Dann ist es gut, wenn er sich fragt:"
      ],
      [
        "Wie ist diese heutige Handlung aus den Ursachen von gestern, vorgestern und so weiter entstanden?",
        "Ich gehe zu­rück auf das, was nach meinem Denken als Ursache anzu­sehen ist.",
        "Habe ich mir ein solches Ereignis ausgesucht, das ich nachher nachprüfen kann, wo meine Gedanken mit dem, was ich als die Ursache erfahren kann, übereinstim­men, so ist das gut. - Es wird aber in den meisten Fällen nicht der Fall sein.",
        "Ist es der Fall, dann kann man die fal­schen Gedanken vergleichen mit dem richtigen Gang der Ereignisse.",
        "Dann wird man merken, daß man nach und nach, nach kürzerer oder längerer Zeit, nicht mehr Fehler machen wird, sondern daß man einen Gedanken heraus-schälen kann aus einer Tatsache, der den objektiven Tat­sachen entspricht.",
        "Oder man versucht, sich aus einem Er­eignis zu konstruieren, was morgen oder in ein paar Stunden aus diesem Ereignis folgen kann.",
        "Auch dies wird zunächst nicht stimmen, aber das Denken wird sich bald so hinein-leben in die Dinge, daß die Dinge so verlaufen wie die Ge­danken, die man sich darüber macht.",
        "Verbietet man sich nun noch, abgezogene, abstrakte Gedanken zu bilden, so wird man allmählich fühlen, wie man mit den Dingen zu­sammenwächst."
      ],
      [
        "Es gibt Leute, die mit einem gewissen Instinkt hinge-drängt werden zu einem solchen Denken, so zum Beispiel Goethe.",
        "Sein Denken war nicht im Kopfe, sondern in den Dingen.",
        "Goethe, der einmal Advokat gewesen ist, hat nicht viel von den Gesetzen gewußt; aber ein sicherer Instinkt sagte ihm, was man in den einzelnen Fällen vornehmen"
      ],
      [
        "muß.",
        "Es gab kein langes Nachschlagen und Durchstudieren von Akten, wenn wieder ein Fall von neuem vorgenommen werden mußte.",
        "Wenn einmal alle Ministerakte Goethes ver­öffentlicht werden, dann wird die Welt erst sehen, wie Goethe eine eminent praktische Natur war, kein weltfrem­der Mensch.",
        "So war er bei einer Rekrutenaushebung, beob­achtete da alles, was vorging - und dabei schrieb er die Iphigenie!",
        "Vergleichen Sie damit, durch was alles ein heu-tiger Dichter bei der Arbeit nicht gestört werden darf.",
        "Und doch war Goethe ein viel größerer Dichter als alle, die heute nicht gestört werden dürfen.",
        "Wegen des eminent praktischen Denkens konnte er zum Beispiel auch sagen, wenn er ans Fenster trat: Heute können wir nicht hinaus­gehen, denn in drei Stunden wird es regnen. - Er hatte Wolkenstudien gemacht, aber keine grobe Theorie auf­gestellt.",
        "Das hängt allerdings mit einer gewissen Selbstlosig­keit zusammen.",
        "Wer zunächst nur an sich denkt, wird es nicht weit bringen.",
        "Wer hinterher gleich ausruft, wenn er etwas verglichen hat: Aha, hatte ich's nicht gesagt! -, der wird es nicht weit bringen.",
        "Das gedankenvolle Haften an den Dingen ist das erste, so daß man in den Dingen selber denkt."
      ],
      [
        "Das zweite ist Lust und Liebe an dem, was man tut.",
        "Sie sind nur dann in wirklichem Sinne vorhanden, wenn es auf den Erfolg nicht ankommt.",
        "Wem es nur auf den Erfolg an­kommt, der kann nicht diese Ruhe entwickeln, die nötig ist, damit Lust und Liebe uns allmählich inspirieren kön­nen.",
        "Bei nichts lernt man mehr, als wenn man sich mit etwas beschäftigt, nur weil es einem Freude macht.",
        "Wenn wir nicht imstande sind, uns an den Mißerfolgen ebenso zu freuen wie an den Erfolgen, so können wir uns niemals von den Dingen die Gedanken sagen lassen, die in ihnen liegen."
      ],
      [
        "Drittens müssen wir Befriedigung finden in dem Denken"
      ],
      [
        "selber.",
        "Das wird heute am meisten bekämpft.",
        "Man hört heute so viel sagen: Was brauchen unsere Kinder das und das zu lernen?",
        "Das haben sie ja im Leben nicht nötig. -Das ist der allerunpraktischste Grundsatz."
      ],
      [
        "Es muß Gebiete geben für den Menschen, wo die bloße denkerische Tätig­keit ihm Befriedigung gewährt, ohne daß er erwartet, ob das Denken zu einem Erfolge führen wird.",
        "Was der Mensch auch für einen Beruf hat: wenn er nicht Zeit findet, wenn auch nur ganz kurz, irgend etwas zu tun, was er rein denke­risch betreibt und was ihn denkerisch befriedigt, wenn er ein solches Gebiet nicht findet, so kann er immer nur in aus­getretenen Geleisen bleiben."
      ],
      [
        "Findet er aber so etwas, dann hat er etwas, das eine große, starke Wirkung auf ihn aus­übt, etwas, das in die feinere Organisation seines Organis­mus hineinwirkt.",
        "Niemals schöpferisch-bildend wirken die Dinge, die uns an den Leib fesseln."
      ],
      [
        "Die nutzen unsere Fähig­keiten ab.",
        "Die Dinge, die wir nur zu unserer eigenen denke­rischen Befriedigung treiben, die schaffen uns Lebenskräfte, die gehen bis in die feinste Organisation unseres Organismus und erhöhen unsere Bildung."
      ],
      [
        "Durch das, was wir in uns zu unserer Befriedigung arbeiten, schaffen wir etwas, durch das wir weiterkommen in der Welt.",
        "Wenn wir damit dann an das praktische Leben herantreten, so wird sich zeigen, daß das richtig ist."
      ],
      [
        "Bleibt man gefesselt an die Lebenspraxis, so macht sie immer denselben Eindruck, und man hat nicht die Freiheit, Initiative zu entwickeln.",
        "Bildet man sich aber höher durch eine solche freie denkerische Tätigkeit, dann steht man sozusagen als zwei Wesen einem solchen Eindruck gegenüber."
      ],
      [
        "Daher gibt es zwar Zeitverlust, wenn man so etwas treibt, was der Lebenspraxis nicht unmittelbar ange­hört, mittelbar fördert es aber die Lebenspraxis durchaus."
      ],
      [
        "Das sind die drei Grundgesetze für die Ausbildung des Denkens.",
        "Sehen Sie, wie schön einer der Menschen, die in"
      ],
      [
        "außerordentlich scharfsinniger Weise in die Zusammenhänge des Lebens hineingeschaut haben, Leonardo da Vinci, das gewußt hat.",
        "Er beschreibt genau, wie man verfahren müsse, wenn man Lust und Liebe an der Arbeit entwickeln will."
      ],
      [
        "Das sind solche Dinge, die uns zunächst zeigen, wie wir durch das Vertrauen in den Weltenaufbau hineinwachsen in die denkerische Praxis, aber auch, indem wir an das Den­ken selber glauben.",
        "Der wird viel tun, der systematisch fol­gendes macht: Er denkt über irgend etwas nach; es kann das Alleralltäglichste sein oder das Allerhöchste."
      ],
      [
        "Will man nun rasch eine Lösung finden, so geschieht das meistens nicht durch praktisches Denken.",
        "Man soll sich nicht zu viel in die Gedanken hineinmischen.",
        "Das ist eine der Hauptforderun­gen: daß wir die Gedanken in uns wirken lassen, daß wir uns gewöhnen, uns zum Schauplatz für das Wirken unseres Denkens zu machen."
      ],
      [
        "Wir können meinen, die Sache lasse sich auf eine bestimmte Weise machen.",
        "Aber wir sind keine Dogmatiker.",
        "Wir sagen uns daher, es könnte auch so ge­macht werden, vielleicht noch auf eine dritte, vierte oder zehnte Art."
      ],
      [
        "Man muß so sorgfältig, als ob man gar nicht beteiligt wäre, die Sache vor sich hinmalen.",
        "Natürlich geht das nur Dingen gegenüber, die sich so behandeln lassen.",
        "Man hat die zehn Lösungen; man führe jede mit Liebe aus, und dann lasse man die Sache liegen."
      ],
      [
        "Man darf gar nicht mehr darüber nachdenken, man muß die Gedanken wirken lassen.",
        "Man muß sich sagen: Die Gedanken sind Mächte, die in meiner Seele wirken, auch wenn ich nicht dabei bin.",
        "Ich warte bis morgen oder übermorgen."
      ],
      [
        "Ich mache es dann vielleicht noch ein zweites oder drittes Mal, und jedesmal wird sich die Frage besser lösen lassen.",
        "Ich handle dann aus dem Gedanken heraus, daß die Gedanken eine Wirklichkeit sind, die auch fortwirkt, ohne daß ich sozusagen dabei bin."
      ],
      [
        "Wer dieses eine Zeitlang macht, der wird sehen, wie vielseitig"
      ],
      [
        "sein Denken wird, wie er sich zur Schlagfertigkeit entwickelt.",
        "Dann wird man dadurch zusammenwachsen, bis in die alleralltäglichsten Dinge hinein zusammenwach­sen mit dem, was geschickt und ungeschickt, was tölpisch und weise ist.",
        "Man wird sich niemals so benehmen, wie sich manchmal sogenannte sehr praktische Menschen verhalten.",
        "Wenn Sie solche Menschen zum Beispiel auf Reisen sehen, irgendwo, wo sie sich nicht zu Hause fühlen, da nehmen sie sich manchmal recht sonderbar aus.",
        "Bis in die Hände her­unter, bis in die Art und Weise, wie man etwas anfaßt, wird das wirken.",
        "Viel weniger werden Sie Teller und Töpfe fallen lassen als andere.",
        "Praktisches Denken wirkt bis in die Glieder hinein, wenn es täglich und nicht in abstrakter Weise vorgenommen wird."
      ],
      [
        "Das unpraktische Denken zeigt sich gerade am besten da, wo das Denken in der Wissenschaft wirken sollte.",
        "Ich habe Ihnen das hypothetische Beispiel aus der Astronomie angeführt.",
        "Aber auch in der Gegenwart sind die Wissen­schaften manchmal furchtbar unpraktisch.",
        "Die Art, wie sich der heutige Mensch über Dinge hermacht, die einen so unendlichen Wert haben, ist manchmal schauderhaft.",
        "Mit Mikroskopen beobachtet man heute Pflanzen.",
        "Man sieht merkwürdige Gebilde an der Pflanze, die facettenartige Form zeigen wie die Augen von Insekten, bei manchen Pflanzen selbst etwas wie eine Linse.",
        "Man beobachtet in­sektenfressende Pflanzen und so weiter.",
        "Das sind wichtige Beobachtungen.",
        "Aber man verwechselt das, was im Menschen die Dinge widerspiegelt, mit dem, was man äußerlich an den Pflanzen beobachtet, und wirft ganz konfus durchein­ander Pflanzenseele, Tierseele und Menschenseele.",
        "Sie kön­nen das in vielen populären Schriften lesen.",
        "Es soll hier nichts gesagt werden gegen die wunderbaren Beobachtun­gen, die durch diese populären Schriften in dieWelt gebracht"
      ],
      [
        "werden.",
        "Aber die Gedanken sind so, daß es den, der den­ken kann, eigentlich an das Folgende erinnert: Ich kenne eine Art Wesen, die sehr, sehr kunstreich organisiert ist.",
        "Sie hat ein Organ in sich, durch welches kleine Wesen wie mit magnetischer Kraft angezogen und verschlungen werden.",
        "Dieser Gedanke ist ganz derselbe wie der bei den Pflanzen-beobachtungen, aber das Wesen, das ich im Auge habe, ist -die Mausefalle!",
        "Sie können genauso gut von einer Beseelung der Mausefalle sprechen wie von der Beseelung der Pflan­zen, in dem Sinne, wie dieses Denken es will.",
        "Auch hier darf man kein innerer Wagenschieber sein."
      ],
      [
        "Dann gibt es aber noch etwas anderes, außerordentlich Wichtiges: daß man Vertrauen hat zu dem innersten geisti­gen Denkorgan.",
        "Bei den meisten Menschen sorgt ja die Natur dafür, daß die Menschen sozusagen nicht immer da­bei sind; der Mensch muß ja schlafen.",
        "Da wirkt diesesDenk­organ für sich, und der Mensch kann es nicht fortwährend ruinieren.",
        "Aber es kommt doch sehr darauf an, ob der Mensch nur die Natur für sich wirken läßt, oder ob man die Ausbildung in die Hand nimmt.",
        "Man sollte einmal, wenn auch noch so kurze Zeit, am Tage sich dazu zwingen, gar nichts zu denken.",
        "Es ist viel leichter, diese auf- und abflutenden Gedanken wirken zu lassen, bis man erlöst wird durch den Schlaf, als sich zu zwingen, nichts zu den­ken.",
        "Dann wirkt das Denkorgan so, daß es Kraft sammelt.",
        "LJnd wer sich immer wieder in die Möglichkeit versetzt, nicht zu denken, der wird sehen, wie die Schlagfertigkeit namentlich dadurch wächst, daß er nicht nur den Schlaf auf den Denkapparat wirken läßt, sondern die Führung über­nimmt in der Ausbildung dieses Denkorgans."
      ],
      [
        "Nur wer von allen Geistern der Spiritualität verlassen ist, kann glauben, daß dann überhaupt nicht gedacht wird.",
        "Hier gilt das Wort, das Goethe von der Natur sagt: «Gedacht"
      ],
      [
        "hat sie und sinnt beständig. » Auch wenn der Mensch gar nicht dabei ist bei seinem Denken, dann denkt etwas in ihm, dessen er sich nur nicht bewußt ist.",
        "In diesen Momen­ten, wo der Mensch ohne seine eigenen persönlichen Gedan­ken daliegt, denkt wirklich ein Höheres in ihm.",
        "Das Über-bewußte in ihm, das Göttliche in ihm läßt der Mensch dann in sich wirken und weben.",
        "Es kündet sich nicht un­mittelbar an, aber in seinen Wirkungen.",
        "Es gehört eine ge­wisse Tatkraft dazu, um eine solche Denkübung vorzu­nehmen."
      ],
      [
        "So sehen Sie, wie man das Denken erziehen kann.",
        "Heute konnten nur einzelne Beispiele der Selbsterziehung des Den­kens gegeben werden, aber diese Beispiele haben gezeigt, daß man auf wirkliche Heilmittel des Denkens hinzuweisen vermag, deren Früchte nur die Erfahrung, das Leben selbst zu geben vermag.",
        "Wer so sein Denken schult, der wird fin­den, daß er auf der einen Seite hinaufsteigen kann in die höchsten Gebiete geistigen Lebens, daß er aber auf der an­dern Seite auch bei den allerpraktischsten Dingen sein Den­ken anwenden kann.",
        "Das, was beim Überblicken der geisti­gen Tatsachen gewonnen wird, soll angewandt werden auf das praktische Leben.",
        "Alle Gebiete, aber besonders auch die Pädagogik, könnten hierdurch gewinnen.",
        "Eine ganz andere Anschauung über Lebenspraxis würde sich ringsherum gel­tend machen.",
        "Aber auch der, der hinaufdringen will in die höheren Welten, würde eine sichere Basis haben.",
        "Das ist wiederum etwas, was durchaus gefordert werden muß.",
        "Und auch die gewöhnliche Wissenschaft würde Ungeheures ge­winnen, wenn sie sich anlehnen wollte an die Geisteswissen­schaft."
      ],
      [
        "Die Wagenschieber des Denkens haben nicht dieses prak­tische Denken; ihnen fehlt es.",
        "Sie vermögen nicht, irgend etwas zurückzuführen auf einen einfachen, umfassenden"
      ],
      [
        "Gedanken.",
        "Das ist, was die Geisteswissenschaft gibt: sie macht uns fähig, das, was sonst fein ausziseliert ist im Leben, unter großen Gesichtspunkten zu überschauen.",
        "Dann wird der Mensch von allen unfruchtbaren Spekulationen abge­lenkt, dann wird er zur wirklichen Lebenspraxis geführt.",
        "Sehen wir Leonardo da Vinci an, den wir zum Vorbild nehmen können.",
        "Er sagt: Theorie ist der Kapitän, Praxis sind die Soldaten."
      ],
      [
        "Wer an die Praxis geht ohne das beherrschende Denken, gleicht dem, der sich auf ein Schiff begibt ohne Kompaß, ohne die Möglichkeit, das Schiff zu steuern.",
        "Goethe hat darauf hingewiesen, wie gerade die Wissenschaft durch un­praktisches Denken zu unfruchtbaren Gedanken kommt.",
        "Da gibt es Leute, welche die Außenwelt auf Atome, und andere, die sie auf Bewegungen zurückführen; andere leug­nen wieder die Bewegung.",
        "Demgegenüber weisen die prak­tischsten Denker darauf hin, daß Einfachheit aus der Größe der Weltanschauung kommt.",
        "Er ist durchaus treffend, der Ausspruch, und wir können auch den Goetheschen Spruch uns vor Augen stellen:"
      ],
      [
        "Es mag sich Feindliches eräugnen,"
      ],
      [
        "Du bleibe ruhig, bleibe stumm;"
      ],
      [
        "Und wenn sie Dir die Bewegung leugnen,"
      ],
      [
        "Geh ihnen vor der Nas' herum."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Im Winterhalbjahr 1908/09 führte Rudolf Steiner die sediste der öffentlichen Vortragsreihen durch, wie sie seit 1903 in Berlin regel-mäßig stattfanden. Sie umfaßt achtzehn Vorträge. Davon sind in Buch-form bereits erschienen die Vorträge II und III unter dem Titel Die Nachschriften dieser Vorträge waren nicht zum Dru& be­stimmt und Rudolf Steiner hat sie selber nicht durchgesehen. Wie schon aus der sehr unterschiedlichen Länge ersichtlich, sind vor allem die hier erstmals veröffentlichten Vorträge lüdtenhaft nachgeschrieben worden und weisen daher Mängel auf. Die Zitate wurden wenn immer möglich nachgeptüft.",
      "10    Da ist vor einiger Zeit eine  erschienen: Der «Abriß",
      "der Psychologie> von Prof. Hermann Ebbinghaus, Leipzig 1908.",
      "Die angeführte Stelle steht im Wortlaut auf Seite 18.",
      "18    Goethes Ausspruch: in «Entwurf einer Farbenlehre. Einleitung>.",
      "21    was Novalis sagt: in den «Fragmenten>. Gesammelte Werke,",
      "herausgegeben von Carl Seelig, Herrliberg-Zürich 1946, Dritter",
      "Band, Nr.1771.",
      "23    Vortrag in der Natur forschenden Gesellschafl: vgl. Goethes Auf-",
      "zeichnungen daruber in «Glückliches Ereignis>, 1794.",
      "25    ein Brief Schillers: vom 23. August 1794.",
      "26    gegenständliches Denken: vgl. Goethes Aufsatz «Bedeutende För­dernis durch ein einziges geistreiches Wort», 1823.",
      "27    Brief von Fichte: vom 21. Juni 1794, Abdruck in Heft XV der",
      "«Veröffentlichungen aus dem literarischen Frühwerk von Rudolf",
      "Steiner», Dornach 1942.",
      "29    Brief von Hegel: vom 20. Februar 1821.",
      "30    Virchows Vortrag: «Goethe als Naturforscher und in besonderer",
      "Beziehung auf Schiller>, 1861.",
      "32    das Bild «Komm, Herr Jesus, sei unser Gast. .. !» ist von Fritz",
      "Uhde, 1848-1911. Vgl. den Vortrag von Rudolf Steiner vom",
      "5. Oktober 1917, Vortrag X der Reihe «Kunstgeschichte als Ab­",
      "bild innerer geistiger Impulse>, Dornach 1919.",
      "34    in meinem Buche «Goethes Weltanschauung»: 1. Aufl. 1897, Frei­",
      "burg i. Br. 1948.",
      "34    Goethe zu Eckermann: am 25. Januar 1827.",
      "46    Die Briefe Schillers üher die ästhetische Erziehung des Menschen:",
      "Goethe schreibt darüber Schiller am 26. Oktober 1794. Der zitierte",
      "Satz steht im 4. Brief.",
      "47    Ein wunderbar schönes Wort: im obengenannten Brief Goethes.",
      "49    «was fruchtbar ist, allein ist wahr»: im Gedicht «Vermächtnis»,",
      "55    Das Goethesche Wort: «Kenne ich mein Verhältnis zu mir selbst",
      "und zur Außenwelt, so heiß' ich's Wahrheit. Und so kann jeder",
      "seine eigene Wahrheit haben, und es ist doch immer dieselbige>,",
      "in «Maximen und Reflexionen».",
      "58    Losskij, Nikolaj, geb. 6. Dezember 1870. Das Buch erschien 1908.",
      "66    einen Gedanken, den er einst ausgesprochen hat: in «Maximen",
      "und Reflexionen».",
      "75    Zur Zeit der großen Stürme im westlichen Europa: am 16. Oktober",
      "1795. «Es iSt mir in der Tat lieb, Sie noch ferne von den Händeln",
      "am Main zu wissen. Der Schatten des Riesen könnte Sie leicht",
      "etwas unsanft anfassen.>",
      "84    «Hier wird's Erreichnis»: Erst 1928 wurde eine Handschrift",
      "Goethes mit der Schreibweise Ereignis bekannt.",
      "109    Der Spruch von Goethe: «Selige Sehnsucht», West-östlicher Divan.",
      "113    der wirklich große Bibelgelehrte: Ferdinand Christian Baur, 1792",
      "bis 1860, Theologieprofessor in Tübingen von 1826 bis 1860.",
      "114    So dürfen wir doch einen Bibelforscher ... nicht vergessen: August",
      "Friedrich Gfrörer, 1803 bis 1861. Bibliothekar und Professor in",
      "Stuttgart, wurde 1853 katholisch. «Wer aber jetzt noch, nachdem",
      "das nötige histori5che Licht über die Frage ausgegossen ist, das vierte Evangelium für ein Machwerk und unterschoben erklärt, dem sage ich ins Gesicht, daß er unter dem Hute nicht bei Troste sei . . .» Gfrörer in «Geschichte des Urchristentums», III. Haupt­teil, Seite 346, Stuttgart 1838.",
      "139    Die Wahrheit des Bibelwortes: Joh. 8, 32.",
      "148    Ein anderer Forscher: «Aberglaube und Zauberei von den ältesten Zeiten an bis in die Gegenwart», von Dr. Alfred Lehmann, Direktor des psychophysischen Laboratoriums der Universität Kopenhagen. Deutsche Ausgabe von Dr. Petersen, Stuttgart 1898.",
      "154    Raimundus Lullus 1235 bis 1315. Vgl. über den angeblichen Ver­such das obengenannte Werk von Lehmann, Seite 157.",
      "159    Da wurde erzählt: so z.B . von H.P. Blavatsky in «Isis unveiled». Das wurde übernommen von S. Ellmore (Pseudonym) in der «Chicago Tribune». Er bezeichnete alles später selber als er­dichtet. Vgl. das obengenannte Werk von Lehmann, Seite 305.",
      "162    Ein Schuldirektor: Heinrich Schramm, vgl. Rudolf Steiner «Mein Lebenigang>, Kapitel II.",
      "167    den Ausspruch, den Feuerbach getan: Ludwig Feuerbach, 1804 bis 1872, in der Anzeige von Moleschotts «Lehre der Nahrungs­mittel für das Volk», 1850.",
      "185    ein alter Spruch, der manchem einfällt: z. B. bei Börne: «Es gibt tausend Krankheiten, aber nur eine Gesundheit>. Vermischte Aufsätze, Dramaturgische Blätter, Aphorismen.",
      "212    daß es wahr ist, was ein altes Wort sagt: «mens sana in corpore sano>, Juvenal, Satiren 10, 356.",
      "214    Tolstoj, Leo Nikolajewitsch, 1828-1910. Carnegie, Andrew, 1835-1919.",
      "224    die Zeit, aus der die großen Romane stammen: 1864-1869.",
      "225    eine Fabel des Ostens: aus «Meine Beichte>, 1879 verfaßt.",
      "229    Und nun sehen wir uns den anderen an: die teilweise lücken-hafte Nachichrift ergänzt nach Carnegies «Autobiography> 1920, deutsch 1921.",
      "233    ein anderes merkwürdiges Evangelium: Carnegie: «TIse Gospel of wealth and other timely Essays>, 1900, übersetzt von Heubner:",
      "«Das Evangelium des Reichtums>, Leipzig 1907.",
      "234    Er wendet sich gleich gegen Tolstoj, von dem er sagt: «Das höchste",
      "Lebensideal ist wohl nicht durch eine solche Nachahmung des",
      "Lebens Christi zu erreichen, wie sie uns Graf Tolstoj zeigt, son­",
      "dern dadurch, daß wir, von Christi Geist beseelt, die veränderten",
      "Bedingungen unseres Zeitalters gleichwohl anerkennen und diesen",
      "Geist in neuen, unsern heutigen Verhältnissen angepaßten Formen",
      "Ausdruck finden lassen.>",
      "241    Etwas ist da, das vor der Geburt da war: «Meine besondere",
      "Beziehung zu der Welt ist nicht in diesem Leben festgestellt",
      "worden und hat nicht mit meinem Körper und nicht mit meinem",
      "in der Zeit entstandenen Bewußtsein begonnen>, Tolstoj «Das",
      "Leben», 2. u. 3. Teil, Eugen Diederichs, Jena 1911, Seite 207.",
      "249    Heinroth tat von Goethe den schönen Ausspruch: siehe den Auf­",
      "satz von Goethe «Bedeutende Fördernis durch ein einziges geist­",
      "reiches Wort>. Zur Morphologie. Zweiten Bandes erstes Heft,",
      "258    Goethe-Zitat: Zahme Xenien, Erste Reihe.",
      "261    «Man weint nicht, weil man traurig ist . ..»: Der Satz stammt von William James, 1842-1910, Professor der Psychologie und Philosophie an der Harvard Universität. «Printiples of Psycho­logy>, 1890, deutsch 1909.",
      "273    was Fichte gesagt hat: in «Beiträge zur Berichtigung der Urteile des Publikums über die französische Revolution>. Erster Teil:",
      "Zur Beurteilung ihrer Rechtmäßigkeit, Heft 1-2 (anonym, ohne Druckort), 1793.",
      "277    Francesco Redi: 1626-1689.",
      "290    Er sagte: zu Eckermann, am 6. Juni 1831: «Mein ferneres Leben",
      "kann ich nunmehr als ein reines Geschenk ansehen, und es ist",
      "jetzt im Grunde ganz einerlei, ob und was ich noch etwa tue.»",
      "296    . . . was er schon als Knabe gesucht hatte: vgl. «Dichtung und",
      "Wahrheit>, erster Teil. Erstes Buch.",
      "297    die «Aurea Catena Homeri»: Goldene Kette Homers. 1723 er­",
      "schienenes Buch.",
      "297    Eliphas Levi: «Dogme et Rituel de la haute Magie», 1861.",
      "306    Nostradamus: Michel de Nhtredame, 1503-1566, französischer",
      "Astrolog. Magische Bücher von ihm sind nicht bekannt. Dagegen",
      "kannte Goethe das damals berühmte Werk von Emanuel Swe­",
      "denborg (1688-1772): «Arcana coelestia, Himmlische Geheim­",
      "nssse», 8 Bände, 1749-1756.",
      "310 Wie einer ist, so ist sein Gott: «Wie einer ist, so ist sein Gott:",
      "Darum ward Gott so oft zu Spott.> (Weimar 1814.)",
      "315    wenn er zuletzt an seine weimarischen Freunde schreibt: am",
      "6. September 1787 und am 28. Januar 1787 in «Italienische Reise>.",
      "316    «indem der Mensch auf den Gipfel der Natur gestellt ist»: Goethe",
      "in «Winckelmann» .",
      "334    Plutarch: Marcellus Kap. 20.",
      "342    Nur strebe nicht nach höheren Orden: In Goethes Handschrift",
      "steht «Orden>.",
      "356    . . . hat Goethe in zwei Gedichten zum Ausdruck gebracht: in",
      "«Eins und Alles> (6. Oktober 1821) und in «Vermächtnis> (Fe­",
      "bruar 1829).",
      "357    Erreichnis: vgl. den Hinweis zu Seite 84.",
      "358    . . . das einzige Zusammentreffen mit Friedrich Nietzsche: Rudolf",
      "Steiner in «Mein Lebensgang», Kapitel 18.",
      "359    Noch ehe Friedrich Nietzsche seinen Doktor gemacht hatte:",
      "von 1869 Professor in Basel.",
      "359    Karl Marx' erstes soziales Buch: «Kritik der politischen Uko­",
      "nomie>, 1859.",
      "362    David Friedrich Strauss, 1808-1874. Das «Leben Jesu> erschien",
      "363    Eugen Dühring, 1833-1921, «Kursus der Philosophie>, 1875, in",
      "4. Auflage 1895 als «Wirklichkeitsphilosophie».",
      "369    Goethe: «Wem die Natur ihr offenbares Geheirnnis zu enthüllen",
      "anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer",
      "würdigsten Auslegerin, der Kunst.> Goethe, Sprüche in Prosa.",
      "370    Vorträge über Faust: «Die Rätsel in Goethes Faust>, 13. und 14. Vortrag im vorliegenden Band.",
      "370    Fausts Gang zu den «Müttern»: Vgl. dazu Goethes Gespräch mit Eckermann vom 10. Januar 1830. Die erwähnte Erzählung steht bei Plutarch, Marcellus Kap. 20.",
      "372    «Wie erlangt man Erkenntnisse höherer Welten», zuerst erschienen in «Lucifer-Gnosis» Nr.13-28 (Berlin 1905-1908). Gesamtaus­gabe 1961.",
      "386 Chorus mysticus: Faust 2. Teil, Schlußszene.",
      "403    Mittagsfrau: vgl. dazu Ludwig Laistner «Das Rätsel der Sphinx»,",
      "Berlin 1889. Rudolf Steiner verweist auf dieses Werk im Zusam­",
      "menhang mit dem hier behandelten Gegenstand im Zyklus",
      "«Inneres Wesen des Menschen und Leben zwischen Tod und",
      "neuer Geburt>, 4. Vortrag. Gesamtausgabe 1959.",
      "406    Baldur und Hödur: Siehe auch Rudolf Steiner, Der Baldur-",
      "Mythos und das Karfreitagsmysterium, Dornach 1930.",
      "411    Hu, Ceridwen, Druiden- und Drottenmysterien: Vgl. Charles",
      "William Heckethorn «Geheime Gesellschaften, Geheimbünde und",
      "Geheimlehren», Leipzig 1900. Rudolf Steiner besaß dieses Werk.",
      "418    «Wahrlich, wahrlich, ich sage euch, ehe Abraham war, war ich»:",
      "Johannes 8, 58.",
      "«Ich und der Vater sind eines»: Johannes 10, 30."
    ],
    "sentences": [
      [
        "Im Winterhalbjahr 1908/09 führte Rudolf Steiner die sediste der öffentlichen Vortragsreihen durch, wie sie seit 1903 in Berlin regel-mäßig stattfanden.",
        "Sie umfaßt achtzehn Vorträge.",
        "Davon sind in Buch-form bereits erschienen die Vorträge II und III unter dem Titel Die Nachschriften dieser Vorträge waren nicht zum Dru& be­stimmt und Rudolf Steiner hat sie selber nicht durchgesehen.",
        "Wie schon aus der sehr unterschiedlichen Länge ersichtlich, sind vor allem die hier erstmals veröffentlichten Vorträge lüdtenhaft nachgeschrieben worden und weisen daher Mängel auf.",
        "Die Zitate wurden wenn immer möglich nachgeptüft."
      ],
      [
        "10 Da ist vor einiger Zeit eine erschienen: Der «Abriß"
      ],
      [
        "der Psychologie> von Prof.",
        "Hermann Ebbinghaus, Leipzig 1908."
      ],
      [
        "Die angeführte Stelle steht im Wortlaut auf Seite 18."
      ],
      [
        "18 Goethes Ausspruch: in «Entwurf einer Farbenlehre.",
        "Einleitung>."
      ],
      [
        "21 was Novalis sagt: in den «Fragmenten>.",
        "Gesammelte Werke,"
      ],
      [
        "herausgegeben von Carl Seelig, Herrliberg-Zürich 1946, Dritter"
      ],
      [
        "Band, Nr.1771."
      ],
      [
        "23 Vortrag in der Natur forschenden Gesellschafl: vgl.",
        "Goethes Auf-"
      ],
      [
        "zeichnungen daruber in «Glückliches Ereignis>, 1794."
      ],
      [
        "25 ein Brief Schillers: vom 23.",
        "August 1794."
      ],
      [
        "26 gegenständliches Denken: vgl.",
        "Goethes Aufsatz «Bedeutende För­dernis durch ein einziges geistreiches Wort», 1823."
      ],
      [
        "27 Brief von Fichte: vom 21.",
        "Juni 1794, Abdruck in Heft XV der"
      ],
      [
        "«Veröffentlichungen aus dem literarischen Frühwerk von Rudolf"
      ],
      [
        "Steiner», Dornach 1942."
      ],
      [
        "29 Brief von Hegel: vom 20.",
        "Februar 1821."
      ],
      [
        "30 Virchows Vortrag: «Goethe als Naturforscher und in besonderer"
      ],
      [
        "Beziehung auf Schiller>, 1861."
      ],
      [
        "32 das Bild «Komm, Herr Jesus, sei unser Gast. .. !» ist von Fritz"
      ],
      [
        "Uhde, 1848-1911.",
        "Vgl. den Vortrag von Rudolf Steiner vom"
      ],
      [
        "Oktober 1917, Vortrag X der Reihe «Kunstgeschichte als Ab­"
      ],
      [
        "bild innerer geistiger Impulse>, Dornach 1919."
      ],
      [
        "34 in meinem Buche «Goethes Weltanschauung»: 1.",
        "Aufl. 1897, Frei­"
      ],
      [
        "burg i.",
        "Br. 1948."
      ],
      [
        "34 Goethe zu Eckermann: am 25.",
        "Januar 1827."
      ],
      [
        "46 Die Briefe Schillers üher die ästhetische Erziehung des Menschen:"
      ],
      [
        "Goethe schreibt darüber Schiller am 26.",
        "Oktober 1794.",
        "Der zitierte"
      ],
      [
        "Satz steht im 4.",
        "Brief."
      ],
      [
        "47 Ein wunderbar schönes Wort: im obengenannten Brief Goethes."
      ],
      [
        "49 «was fruchtbar ist, allein ist wahr»: im Gedicht «Vermächtnis»,"
      ],
      [
        "55 Das Goethesche Wort: «Kenne ich mein Verhältnis zu mir selbst"
      ],
      [
        "und zur Außenwelt, so heiß' ich's Wahrheit.",
        "Und so kann jeder"
      ],
      [
        "seine eigene Wahrheit haben, und es ist doch immer dieselbige>,"
      ],
      [
        "in «Maximen und Reflexionen»."
      ],
      [
        "58 Losskij, Nikolaj, geb. 6.",
        "Dezember 1870.",
        "Das Buch erschien 1908."
      ],
      [
        "66 einen Gedanken, den er einst ausgesprochen hat: in «Maximen"
      ],
      [
        "und Reflexionen»."
      ],
      [
        "75 Zur Zeit der großen Stürme im westlichen Europa: am 16.",
        "Oktober"
      ],
      [
        "1795.",
        "«Es iSt mir in der Tat lieb, Sie noch ferne von den Händeln"
      ],
      [
        "am Main zu wissen.",
        "Der Schatten des Riesen könnte Sie leicht"
      ],
      [
        "etwas unsanft anfassen.>"
      ],
      [
        "84 «Hier wird's Erreichnis»: Erst 1928 wurde eine Handschrift"
      ],
      [
        "Goethes mit der Schreibweise Ereignis bekannt."
      ],
      [
        "109 Der Spruch von Goethe: «Selige Sehnsucht», West-östlicher Divan."
      ],
      [
        "113 der wirklich große Bibelgelehrte: Ferdinand Christian Baur, 1792"
      ],
      [
        "bis 1860, Theologieprofessor in Tübingen von 1826 bis 1860."
      ],
      [
        "114 So dürfen wir doch einen Bibelforscher ... nicht vergessen: August"
      ],
      [
        "Friedrich Gfrörer, 1803 bis 1861.",
        "Bibliothekar und Professor in"
      ],
      [
        "Stuttgart, wurde 1853 katholisch.",
        "«Wer aber jetzt noch, nachdem"
      ],
      [
        "das nötige histori5che Licht über die Frage ausgegossen ist, das vierte Evangelium für ein Machwerk und unterschoben erklärt, dem sage ich ins Gesicht, daß er unter dem Hute nicht bei Troste sei . . .» Gfrörer in «Geschichte des Urchristentums», III.",
        "Haupt­teil, Seite 346, Stuttgart 1838."
      ],
      [
        "139 Die Wahrheit des Bibelwortes: Joh. 8, 32."
      ],
      [
        "148 Ein anderer Forscher: «Aberglaube und Zauberei von den ältesten Zeiten an bis in die Gegenwart», von Dr.",
        "Alfred Lehmann, Direktor des psychophysischen Laboratoriums der Universität Kopenhagen.",
        "Deutsche Ausgabe von Dr.",
        "Petersen, Stuttgart 1898."
      ],
      [
        "154 Raimundus Lullus 1235 bis 1315.",
        "Vgl. über den angeblichen Ver­such das obengenannte Werk von Lehmann, Seite 157."
      ],
      [
        "159 Da wurde erzählt: so z.B . von H.P.",
        "Blavatsky in «Isis unveiled».",
        "Das wurde übernommen von S.",
        "Ellmore (Pseudonym) in der «Chicago Tribune».",
        "Er bezeichnete alles später selber als er­dichtet.",
        "Vgl. das obengenannte Werk von Lehmann, Seite 305."
      ],
      [
        "162 Ein Schuldirektor: Heinrich Schramm, vgl.",
        "Rudolf Steiner «Mein Lebenigang>, Kapitel II."
      ],
      [
        "167 den Ausspruch, den Feuerbach getan: Ludwig Feuerbach, 1804 bis 1872, in der Anzeige von Moleschotts «Lehre der Nahrungs­mittel für das Volk», 1850."
      ],
      [
        "185 ein alter Spruch, der manchem einfällt: z.",
        "B. bei Börne: «Es gibt tausend Krankheiten, aber nur eine Gesundheit>.",
        "Vermischte Aufsätze, Dramaturgische Blätter, Aphorismen."
      ],
      [
        "212 daß es wahr ist, was ein altes Wort sagt: «mens sana in corpore sano>, Juvenal, Satiren 10, 356."
      ],
      [
        "214 Tolstoj, Leo Nikolajewitsch, 1828-1910.",
        "Carnegie, Andrew, 1835-1919."
      ],
      [
        "224 die Zeit, aus der die großen Romane stammen: 1864-1869."
      ],
      [
        "225 eine Fabel des Ostens: aus «Meine Beichte>, 1879 verfaßt."
      ],
      [
        "229 Und nun sehen wir uns den anderen an: die teilweise lücken-hafte Nachichrift ergänzt nach Carnegies «Autobiography> 1920, deutsch 1921."
      ],
      [
        "233 ein anderes merkwürdiges Evangelium: Carnegie: «TIse Gospel of wealth and other timely Essays>, 1900, übersetzt von Heubner:"
      ],
      [
        "«Das Evangelium des Reichtums>, Leipzig 1907."
      ],
      [
        "234 Er wendet sich gleich gegen Tolstoj, von dem er sagt: «Das höchste"
      ],
      [
        "Lebensideal ist wohl nicht durch eine solche Nachahmung des"
      ],
      [
        "Lebens Christi zu erreichen, wie sie uns Graf Tolstoj zeigt, son­"
      ],
      [
        "dern dadurch, daß wir, von Christi Geist beseelt, die veränderten"
      ],
      [
        "Bedingungen unseres Zeitalters gleichwohl anerkennen und diesen"
      ],
      [
        "Geist in neuen, unsern heutigen Verhältnissen angepaßten Formen"
      ],
      [
        "Ausdruck finden lassen.>"
      ],
      [
        "241 Etwas ist da, das vor der Geburt da war: «Meine besondere"
      ],
      [
        "Beziehung zu der Welt ist nicht in diesem Leben festgestellt"
      ],
      [
        "worden und hat nicht mit meinem Körper und nicht mit meinem"
      ],
      [
        "in der Zeit entstandenen Bewußtsein begonnen>, Tolstoj «Das"
      ],
      [
        "Leben», 2. u. 3.",
        "Teil, Eugen Diederichs, Jena 1911, Seite 207."
      ],
      [
        "249 Heinroth tat von Goethe den schönen Ausspruch: siehe den Auf­"
      ],
      [
        "satz von Goethe «Bedeutende Fördernis durch ein einziges geist­"
      ],
      [
        "reiches Wort>.",
        "Zur Morphologie.",
        "Zweiten Bandes erstes Heft,"
      ],
      [
        "258 Goethe-Zitat: Zahme Xenien, Erste Reihe."
      ],
      [
        "261 «Man weint nicht, weil man traurig ist . ..»: Der Satz stammt von William James, 1842-1910, Professor der Psychologie und Philosophie an der Harvard Universität.",
        "«Printiples of Psycho­logy>, 1890, deutsch 1909."
      ],
      [
        "273 was Fichte gesagt hat: in «Beiträge zur Berichtigung der Urteile des Publikums über die französische Revolution>.",
        "Erster Teil:"
      ],
      [
        "Zur Beurteilung ihrer Rechtmäßigkeit, Heft 1-2 (anonym, ohne Druckort), 1793."
      ],
      [
        "277 Francesco Redi: 1626-1689."
      ],
      [
        "290 Er sagte: zu Eckermann, am 6.",
        "Juni 1831: «Mein ferneres Leben"
      ],
      [
        "kann ich nunmehr als ein reines Geschenk ansehen, und es ist"
      ],
      [
        "jetzt im Grunde ganz einerlei, ob und was ich noch etwa tue.»"
      ],
      [
        "296 . . . was er schon als Knabe gesucht hatte: vgl.",
        "«Dichtung und"
      ],
      [
        "Wahrheit>, erster Teil.",
        "Erstes Buch."
      ],
      [
        "297 die «Aurea Catena Homeri»: Goldene Kette Homers. 1723 er­"
      ],
      [
        "schienenes Buch."
      ],
      [
        "297 Eliphas Levi: «Dogme et Rituel de la haute Magie», 1861."
      ],
      [
        "306 Nostradamus: Michel de Nhtredame, 1503-1566, französischer"
      ],
      [
        "Astrolog.",
        "Magische Bücher von ihm sind nicht bekannt.",
        "Dagegen"
      ],
      [
        "kannte Goethe das damals berühmte Werk von Emanuel Swe­"
      ],
      [
        "denborg (1688-1772): «Arcana coelestia, Himmlische Geheim­"
      ],
      [
        "nssse», 8 Bände, 1749-1756."
      ],
      [
        "310 Wie einer ist, so ist sein Gott: «Wie einer ist, so ist sein Gott:"
      ],
      [
        "Darum ward Gott so oft zu Spott.> (Weimar 1814.)"
      ],
      [
        "315 wenn er zuletzt an seine weimarischen Freunde schreibt: am"
      ],
      [
        "September 1787 und am 28.",
        "Januar 1787 in «Italienische Reise>."
      ],
      [
        "316 «indem der Mensch auf den Gipfel der Natur gestellt ist»: Goethe"
      ],
      [
        "in «Winckelmann» ."
      ],
      [
        "334 Plutarch: Marcellus Kap. 20."
      ],
      [
        "342 Nur strebe nicht nach höheren Orden: In Goethes Handschrift"
      ],
      [
        "steht «Orden>."
      ],
      [
        "356 . . . hat Goethe in zwei Gedichten zum Ausdruck gebracht: in"
      ],
      [
        "«Eins und Alles> (6.",
        "Oktober 1821) und in «Vermächtnis> (Fe­"
      ],
      [
        "bruar 1829)."
      ],
      [
        "357 Erreichnis: vgl. den Hinweis zu Seite 84."
      ],
      [
        "358 . . . das einzige Zusammentreffen mit Friedrich Nietzsche: Rudolf"
      ],
      [
        "Steiner in «Mein Lebensgang», Kapitel 18."
      ],
      [
        "359 Noch ehe Friedrich Nietzsche seinen Doktor gemacht hatte:"
      ],
      [
        "von 1869 Professor in Basel."
      ],
      [
        "359 Karl Marx' erstes soziales Buch: «Kritik der politischen Uko­"
      ],
      [
        "nomie>, 1859."
      ],
      [
        "362 David Friedrich Strauss, 1808-1874.",
        "Das «Leben Jesu> erschien"
      ],
      [
        "363 Eugen Dühring, 1833-1921, «Kursus der Philosophie>, 1875, in"
      ],
      [
        "Auflage 1895 als «Wirklichkeitsphilosophie»."
      ],
      [
        "369 Goethe: «Wem die Natur ihr offenbares Geheirnnis zu enthüllen"
      ],
      [
        "anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer"
      ],
      [
        "würdigsten Auslegerin, der Kunst.> Goethe, Sprüche in Prosa."
      ],
      [
        "370 Vorträge über Faust: «Die Rätsel in Goethes Faust>, 13. und 14.",
        "Vortrag im vorliegenden Band."
      ],
      [
        "370 Fausts Gang zu den «Müttern»: Vgl. dazu Goethes Gespräch mit Eckermann vom 10.",
        "Januar 1830.",
        "Die erwähnte Erzählung steht bei Plutarch, Marcellus Kap. 20."
      ],
      [
        "372 «Wie erlangt man Erkenntnisse höherer Welten», zuerst erschienen in «Lucifer-Gnosis» Nr.13-28 (Berlin 1905-1908).",
        "Gesamtaus­gabe 1961."
      ],
      [
        "386 Chorus mysticus: Faust 2.",
        "Teil, Schlußszene."
      ],
      [
        "403 Mittagsfrau: vgl. dazu Ludwig Laistner «Das Rätsel der Sphinx»,"
      ],
      [
        "Berlin 1889.",
        "Rudolf Steiner verweist auf dieses Werk im Zusam­"
      ],
      [
        "menhang mit dem hier behandelten Gegenstand im Zyklus"
      ],
      [
        "«Inneres Wesen des Menschen und Leben zwischen Tod und"
      ],
      [
        "neuer Geburt>, 4.",
        "Vortrag.",
        "Gesamtausgabe 1959."
      ],
      [
        "406 Baldur und Hödur: Siehe auch Rudolf Steiner, Der Baldur-"
      ],
      [
        "Mythos und das Karfreitagsmysterium, Dornach 1930."
      ],
      [
        "411 Hu, Ceridwen, Druiden- und Drottenmysterien: Vgl.",
        "Charles"
      ],
      [
        "William Heckethorn «Geheime Gesellschaften, Geheimbünde und"
      ],
      [
        "Geheimlehren», Leipzig 1900.",
        "Rudolf Steiner besaß dieses Werk."
      ],
      [
        "418 «Wahrlich, wahrlich, ich sage euch, ehe Abraham war, war ich»:"
      ],
      [
        "Johannes 8, 58."
      ],
      [
        "«Ich und der Vater sind eines»: Johannes 10, 30."
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
