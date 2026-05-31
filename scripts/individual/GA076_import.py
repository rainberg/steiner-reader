#!/usr/bin/env python3
"""Standalone import script for GA076 — GA076 - Die befruchtende Wirkung der Anthroposophie auf die Fachwissenschaften"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA076 - Die befruchtende Wirkung der Anthroposophie auf die Fachwissenschaften"""
GA_NUMBER = "GA076"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "Inhalt",
    "paragraphs": [
      "Die befruchtende Wirkung der Anthroposophie auf die Fachwissenschaften Vorträge und Ansprachen im zweiten anthroposophischen Hochschulkurs",
      "vom 3. bis 10. April 1921 in Dornach 1977",
      "RUDOLF STEINER VERLAG DORNACH/SCHWEIZ",
      "Nach vom Vortragenden nicht durchgesehenen Nachschriften herausgegeben   von   der   Rudolf   Steiner-Nachlaßverwaltung",
      "Die Herausgabe besorgten Ernst Weidmannund Paul G. Bellmann",
      "2., neu durchgesehene und veränderte Auflage, Gesamtausgabe Dornach 1977 Bibliographie-Nr. 76 Alle Rechte bei der Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz © 1977 by Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz Printed in Germany.",
      "Gesamtherstellung Greiserdruck Rastatt ISBN 3-7274-0760-3",
      "eröffnungsrede, Dornach, 3. April 1921 9 Am Ufer einer erfüllten Vergangenheit richtete der Grieche das Wahrwort auf: Mensch, erkenne dich selbst! - Am Ufer einer unbestimmten Zukunft müssen wir das Wahrwort auf- richten: Mensch, erkenne dich selbst und werde ein freies Wesen!",
      "Dazwischen liegt eine Episode menschheitlicher Ent- wickelung, der dreifache Schritt zur Freiheit: Freiheit im inneren Erleben des Menschlichsten, Freiheit im Schaffen, auch im künstlerischen Schaffen, Freiheit im religiösen Erle- ben. Dazu soll führen die Befruchtung der einzelnen Wissen- schaften und des ganzen sozialen Lebens durch eine im Geiste erlebte Weltanschauung. erster vortrag, 4.",
      "April 1921 26 Philosophie Das bedeutsame philosophische Werk von Ludwig Haller. Seine Kritik des Kantianismus. Eduard von Hartmanns Auseinandersetzung mit Ludwig Haller. Kants Weg von Wolff zu David Hume.",
      "Kants Antipode Goethe. Die Ent- wickelung der Begriffswelt seit dem Altertum. Das Erreichen des reinen Denkens im Sinne der «Philosophie der Freiheit». Wirkliche Freiheit ist nicht möglich ohne dieses reine Denken.",
      "Das Problem der neueren philosophischen Entwickelung: das Erfassen des irrealen bildhaften Denkens. Schlußwort zur Disputation 47 zweiter vortrag, 5. April 1921 60 Mathematik und anorganische Naturwissenschaften Kants Ausspruch über die Mathematik in den Wissenschaften.",
      "Anderer Sinn einer mathematischen Methode bei Descartes und Spinoza. Durchschaubarkeit der mathematischen Be- wußtseinsinhalte als das Wesentliche des mathematischen Denkens. Hinweis auf die nichteuklidische Geometrie.",
      "Goe- thes Einstellung zur Anwendung des Mathematischen auf die Naturerkenntnis. Der Weg von der irrealen mathematischen Denkungsart zu der realen naturwissenschaftlichen Den- kungsart, erläutert an einem Beispiel aus der synthetischen Geometrie.",
      "Der Weg von der analytischen Geometrie in die synthetische Geometrie als inneres Erlebnis, entsprechend dem Aufsteigen von der gewöhnlichen Logik zu dem Imagina- tiven. Der entgegengesetzte Weg der Geisteswissenschaft zur Realisierung der irrealen Erkenntnis.",
      "Schlußwort zur Disputation 84 dritter vortrag, 6. April 1921 96 Organische Naturwissenschaften und Medizin Goethes Einstellung zum Gebrauch der Verstandes- oder Ver- nunftkraft. Die Idee des Vitalismus und seine «Aufwär- mung» durch den Neovitalismus.",
      "Verdrängung der Philo- sophie durch naturwissenschaftliche Methoden, Brentano und Mach. Das Übertragen der Methoden anorganischer Natur- wissenschaften auf organische Naturwissenschaften ist nicht angängig.",
      "Wissenschaftliche Betrachtung des Organischen er- fordert neue Bewußtseinsformen: imaginatives, inspiriertes und intuitives Bewußtsein. Erst im imaginativen Erkennen enthüllt sich das Geheimnis des Lebens.",
      "Goethe konnte seine Betrachtungsweise des Pflanzenreichs nicht auf das Tierreich ausdehnen. Haeckels Evolutionslehre. Ihr Gegensatz zu einer wirklich sinngemäßen Evolutionslehre. Beispiel der Be- trachtung des menschlichen Hauptes erweist den Zusam- menhang zwischen dem Geistig-Seelischen und dem Phy- sisch-Leiblichen.",
      "Der Übergang über die Pathologie zu einer rationalen Therapie. vierter vortrag, 7. April 1921 118 Sprachwissenschaft Wilhelm Scherers Zug zur Physiologie. Der Übergang vom bildhaften Erleben zur Abstraktion, eingeleitet durch Aristo- teles.",
      "Die Wauwau- und die Bimbam-Theorien. Imagination und Inspiration führen zum Erfassen der inneren Struktur des Seelenlebens im Konkreten. Einflüsse von Zahnwechsel und Geschlechtsreife auf das Verhältnis des Menschen zur Außenwelt.",
      "Was in den Dingen verstummt, wird durch die Entmaterialisierung innerlich im Menschen hörbar und kommt zum Sprechen. In der Sprache drückt sich aus eine Wechselwirkung zwischen astralischem und Ätherleib.",
      "Wie sich Physiologie und Philologie finden können. Antworten am dritten Disputationsabend 141 fünfter vortrag, 8. April 1921 169 Sozialwissenschaft und soziale Praxis Das aristotelische Dogma von dem Nichtvorhandensein der Präexistenz ist zu einer nichtchristlichen Lehre der abendlän- dischen Christen geworden.",
      "Das Erringen gesunder Urteile über das Obersinnliche führt auch zu gesunden Urteilen über das soziale Leben. In Sozialwissenschaft und sozialer Praxis leben Willensimpulse. Sie können daher nicht nur erkenntnis- mäßig betrachtet werden.",
      "Lebensfremdheit der abstrahieren- den Wissenschaftlichkeit. Kant. Herbart. Das Buch «Kern- punkte der sozialen Frage» ist im eminentesten Sinne prak- tisch gedacht; es sollte nicht nur die Intellekte, sondern den Willen ergreifen.",
      "Woodrow Wilsons Vierzehn Punkte. Har- ding und Lloyd George. Gegnerschaft gegen den Impuls der sozialen Dreigliederung: Arbeiterführer und Vertreter des alten Bourgeoistums. Karl Giskras Ausspruch über die soziale Frage in Österreich.",
      "Enthusiasmus und Wille gegen- über der Wahrheit müssen unseren Willen durchdringen, sonst entsteht nicht einmal der Anfang zu einer fruchtbaren Behandlung der sozialen Frage und Praxis. Schlußwort zum vierten Disputationsabend . . . .195 Schlußwort zu einer Studentenversammlung 9.",
      "April 1921 202 schlussrede, 10. April 1921 218 Geisteswissenschaft überschreitet die Grenzen herkömmlicher Fachwissenschaft nach außen (Naturerkenntnis) und nach innen (Erfassung der menschlichen Wesenheit im ganzen).",
      "Irrige Meinung, es fehle an der Popularisierung des bisher wissenschaftlich Geleisteten. Wichtiger als dieses Hinaustra- gen aus unseren Bildungsanstalten ist, in diese hineinzutra- gen dasjenige, was die geistige Forschung über die äußere sinnliche und verstandesmäßige Forschung hinaus beitragen kann.",
      "Die Schrift Cosacks über die «Universitätsreform». Schumpeter, Ricken und Windelband und die wertungsfreie Wissenschaft. Das Zusammenwirken von Wissenschaft, Kunst und Religion muß wieder gefunden werden.",
      "Hinweise 241 Personenregister 260 Übersicht über die Rudolf Steiner Gesamtausgabe . . . 263"
    ],
    "sentences": [
      [
        "Die befruchtende Wirkung der Anthroposophie auf die Fachwissenschaften Vorträge und Ansprachen im zweiten anthroposophischen Hochschulkurs"
      ],
      [
        "vom 3. bis 10.",
        "April 1921 in Dornach 1977"
      ],
      [
        "RUDOLF STEINER VERLAG DORNACH/SCHWEIZ"
      ],
      [
        "Nach vom Vortragenden nicht durchgesehenen Nachschriften herausgegeben von der Rudolf Steiner-Nachlaßverwaltung"
      ],
      [
        "Die Herausgabe besorgten Ernst Weidmannund Paul G.",
        "Bellmann"
      ],
      [
        "2., neu durchgesehene und veränderte Auflage, Gesamtausgabe Dornach 1977 Bibliographie-Nr. 76 Alle Rechte bei der Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz © 1977 by Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz Printed in Germany."
      ],
      [
        "Gesamtherstellung Greiserdruck Rastatt ISBN 3-7274-0760-3"
      ],
      [
        "eröffnungsrede, Dornach, 3.",
        "April 1921 9 Am Ufer einer erfüllten Vergangenheit richtete der Grieche das Wahrwort auf: Mensch, erkenne dich selbst! - Am Ufer einer unbestimmten Zukunft müssen wir das Wahrwort auf- richten: Mensch, erkenne dich selbst und werde ein freies Wesen!"
      ],
      [
        "Dazwischen liegt eine Episode menschheitlicher Ent- wickelung, der dreifache Schritt zur Freiheit: Freiheit im inneren Erleben des Menschlichsten, Freiheit im Schaffen, auch im künstlerischen Schaffen, Freiheit im religiösen Erle- ben.",
        "Dazu soll führen die Befruchtung der einzelnen Wissen- schaften und des ganzen sozialen Lebens durch eine im Geiste erlebte Weltanschauung. erster vortrag, 4."
      ],
      [
        "April 1921 26 Philosophie Das bedeutsame philosophische Werk von Ludwig Haller.",
        "Seine Kritik des Kantianismus.",
        "Eduard von Hartmanns Auseinandersetzung mit Ludwig Haller.",
        "Kants Weg von Wolff zu David Hume."
      ],
      [
        "Kants Antipode Goethe.",
        "Die Ent- wickelung der Begriffswelt seit dem Altertum.",
        "Das Erreichen des reinen Denkens im Sinne der «Philosophie der Freiheit».",
        "Wirkliche Freiheit ist nicht möglich ohne dieses reine Denken."
      ],
      [
        "Das Problem der neueren philosophischen Entwickelung: das Erfassen des irrealen bildhaften Denkens.",
        "Schlußwort zur Disputation 47 zweiter vortrag, 5.",
        "April 1921 60 Mathematik und anorganische Naturwissenschaften Kants Ausspruch über die Mathematik in den Wissenschaften."
      ],
      [
        "Anderer Sinn einer mathematischen Methode bei Descartes und Spinoza.",
        "Durchschaubarkeit der mathematischen Be- wußtseinsinhalte als das Wesentliche des mathematischen Denkens.",
        "Hinweis auf die nichteuklidische Geometrie."
      ],
      [
        "Goe- thes Einstellung zur Anwendung des Mathematischen auf die Naturerkenntnis.",
        "Der Weg von der irrealen mathematischen Denkungsart zu der realen naturwissenschaftlichen Den- kungsart, erläutert an einem Beispiel aus der synthetischen Geometrie."
      ],
      [
        "Der Weg von der analytischen Geometrie in die synthetische Geometrie als inneres Erlebnis, entsprechend dem Aufsteigen von der gewöhnlichen Logik zu dem Imagina- tiven.",
        "Der entgegengesetzte Weg der Geisteswissenschaft zur Realisierung der irrealen Erkenntnis."
      ],
      [
        "Schlußwort zur Disputation 84 dritter vortrag, 6.",
        "April 1921 96 Organische Naturwissenschaften und Medizin Goethes Einstellung zum Gebrauch der Verstandes- oder Ver- nunftkraft.",
        "Die Idee des Vitalismus und seine «Aufwär- mung» durch den Neovitalismus."
      ],
      [
        "Verdrängung der Philo- sophie durch naturwissenschaftliche Methoden, Brentano und Mach.",
        "Das Übertragen der Methoden anorganischer Natur- wissenschaften auf organische Naturwissenschaften ist nicht angängig."
      ],
      [
        "Wissenschaftliche Betrachtung des Organischen er- fordert neue Bewußtseinsformen: imaginatives, inspiriertes und intuitives Bewußtsein.",
        "Erst im imaginativen Erkennen enthüllt sich das Geheimnis des Lebens."
      ],
      [
        "Goethe konnte seine Betrachtungsweise des Pflanzenreichs nicht auf das Tierreich ausdehnen.",
        "Haeckels Evolutionslehre.",
        "Ihr Gegensatz zu einer wirklich sinngemäßen Evolutionslehre.",
        "Beispiel der Be- trachtung des menschlichen Hauptes erweist den Zusam- menhang zwischen dem Geistig-Seelischen und dem Phy- sisch-Leiblichen."
      ],
      [
        "Der Übergang über die Pathologie zu einer rationalen Therapie. vierter vortrag, 7.",
        "April 1921 118 Sprachwissenschaft Wilhelm Scherers Zug zur Physiologie.",
        "Der Übergang vom bildhaften Erleben zur Abstraktion, eingeleitet durch Aristo- teles."
      ],
      [
        "Die Wauwau- und die Bimbam-Theorien.",
        "Imagination und Inspiration führen zum Erfassen der inneren Struktur des Seelenlebens im Konkreten.",
        "Einflüsse von Zahnwechsel und Geschlechtsreife auf das Verhältnis des Menschen zur Außenwelt."
      ],
      [
        "Was in den Dingen verstummt, wird durch die Entmaterialisierung innerlich im Menschen hörbar und kommt zum Sprechen.",
        "In der Sprache drückt sich aus eine Wechselwirkung zwischen astralischem und Ätherleib."
      ],
      [
        "Wie sich Physiologie und Philologie finden können.",
        "Antworten am dritten Disputationsabend 141 fünfter vortrag, 8.",
        "April 1921 169 Sozialwissenschaft und soziale Praxis Das aristotelische Dogma von dem Nichtvorhandensein der Präexistenz ist zu einer nichtchristlichen Lehre der abendlän- dischen Christen geworden."
      ],
      [
        "Das Erringen gesunder Urteile über das Obersinnliche führt auch zu gesunden Urteilen über das soziale Leben.",
        "In Sozialwissenschaft und sozialer Praxis leben Willensimpulse.",
        "Sie können daher nicht nur erkenntnis- mäßig betrachtet werden."
      ],
      [
        "Lebensfremdheit der abstrahieren- den Wissenschaftlichkeit.",
        "Kant.",
        "Herbart.",
        "Das Buch «Kern- punkte der sozialen Frage» ist im eminentesten Sinne prak- tisch gedacht; es sollte nicht nur die Intellekte, sondern den Willen ergreifen."
      ],
      [
        "Woodrow Wilsons Vierzehn Punkte.",
        "Har- ding und Lloyd George.",
        "Gegnerschaft gegen den Impuls der sozialen Dreigliederung: Arbeiterführer und Vertreter des alten Bourgeoistums.",
        "Karl Giskras Ausspruch über die soziale Frage in Österreich."
      ],
      [
        "Enthusiasmus und Wille gegen- über der Wahrheit müssen unseren Willen durchdringen, sonst entsteht nicht einmal der Anfang zu einer fruchtbaren Behandlung der sozialen Frage und Praxis.",
        "Schlußwort zum vierten Disputationsabend . . . .195 Schlußwort zu einer Studentenversammlung 9."
      ],
      [
        "April 1921 202 schlussrede, 10.",
        "April 1921 218 Geisteswissenschaft überschreitet die Grenzen herkömmlicher Fachwissenschaft nach außen (Naturerkenntnis) und nach innen (Erfassung der menschlichen Wesenheit im ganzen)."
      ],
      [
        "Irrige Meinung, es fehle an der Popularisierung des bisher wissenschaftlich Geleisteten.",
        "Wichtiger als dieses Hinaustra- gen aus unseren Bildungsanstalten ist, in diese hineinzutra- gen dasjenige, was die geistige Forschung über die äußere sinnliche und verstandesmäßige Forschung hinaus beitragen kann."
      ],
      [
        "Die Schrift Cosacks über die «Universitätsreform».",
        "Schumpeter, Ricken und Windelband und die wertungsfreie Wissenschaft.",
        "Das Zusammenwirken von Wissenschaft, Kunst und Religion muß wieder gefunden werden."
      ],
      [
        "Hinweise 241 Personenregister 260 Übersicht über die Rudolf Steiner Gesamtausgabe . . . 263"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ERÖFFNUNGSREDE Dornach, 3. April 1921",
    "paragraphs": [
      "Meine sehr verehrten Anwesenden! Unsere Zeit ist eine Zeit der Zweifel und Rätsel, die der Menschheit aufgege- ben sind. Und man kann sagen, wohl dem, der sich in sei- nem Inneren ehrlich und mit Kraft gegenüber den Ge- schehnissen der Gegenwart sagen kann: Ja, für mich ist diese Zeit eine Zeit der Zweifel, der Rätsel und der Fra- gen, die gelöst werden müssen. - Denn könnte er sich dies nicht sagen und würde er doch mit wacher Seele hinblicken auf die Geschehnisse der Zeit, so gäbe es für ihn eigentlich nur den anderen Pol: die Verzweiflung an dem Fortgange der menschlichen Zivilisation im Abendlande.",
      "Und wenn in unserer Zeit Zweifel, Fragen, Rätsel verborgen sind, die gelöst werden müssen, dann bedarf es dazu der starken Kraft der Menschen, die sich zurechtfinden können in dem gegenwärtigen Zivilisationschaos, und die aus der Flut der Fragen und Rätsel das aufsprießen lassen können, was zu einem neuen Fortgang, zu einem Aufbau unserer abend- ländischen Zivilisation führen kann. Etwas dazu beitragen, daß die Kräfte, welche die Zeit also braucht, damit die Zweifel und Rätsel aus den menschlichen Seelen heraus ge- löst werden können, das möchte alles, was von diesem Goetheanum aus unternommen wird.",
      "In einer solchen Zeit der Fragen und Rätsel wird sich auch für manches, was Inhalt alter Überlieferung ist, die Not- wendigkeit zeigen, in einem neuen Lichte zu erscheinen. Nun leuchtet uns herauf - gewissermaßen wie ein uralt heiliges Vermächtnis der Griechenkultur - das oft und oft wiederholte apollinische Wort: Mensch, erkenne dich selbst!",
      "Und vieles in der abendländischen Zivilisation seit der alten Griechenzeit hat gestanden im Zeichen dieses Wortes. Mir scheint aber, daß selbst ein solches, wie es schien, felsenfest in der Menschheitsentwickelung drinnen- stehendes Zauberwort heute, in unseren Zeiten der großen Verwandlungen, nur mehr Bestand haben kann, wenn es, aufnehmend die Kräfte unserer Zeit, selbst eine Art Ver- wandlung durchmacht.",
      "Und so scheint mir, daß das uralte Delphiwort heute also zu den Menschen klingen müsse: Mensch, erkenne dich selbst und werde ein freies Wesen! - Wir müssen das Weltgeschehen, insofern es sich auf den Menschen bezieht, hin- und herschwingend schauen können zwischen den beiden Polen der Selbsterkenntnis und der wahren menschlichen Freiheit. Warum schrieb griechische Weisheit auf den Tempel zu Delphi das bedeutungsvolle Wort: Erkenne dich selbst? - Zu diesem Griechentum leuchtete herauf, aus uralten, hi- storisch ihrem Anfange nach unbestimmbaren Zeiten, eine uralte geheiligte Weisheit und Wissenschaft.",
      "Die Ur- sprünge dieser Wissenschaft gehen in das Dunkel der vor- geschichtlichen Zeiten zurück. In Ägypten hatte man noch ein unmittelbares Drinnenstehen in dieser Urweisheit. In Griechenland hatte man nur noch ein, allerdings in die edle griechische Menschlichkeit getauchtes Gefühl davon, und man fühlte: aus der Welt, aus der weisheitsvollen Welt selbst heraus war den Menschen diese Weisheit gekommen.",
      "Der Mensch hatte sich innerhalb der Welt der Weisheit gefühlt wie ein mehr oder weniger nur instinktiv lebendes, mehr oder weniger unbewußtes Glied des Weltenganzen. Da dämmerte herauf im griechischen Fühlen die Empfin- dung der Selbständigkeit der Menschenseele.",
      "Zu dem alten Welterkennen hinzu sollte erstrebt werden die Selbst- 10 erkenntnis des Menschen. Im Grunde genommen war der uralten Weisheit Devise: Erkenne die Welt und in der Welt den Menschen! - Diese Devise uralter Weisheit strahlte in das Griechentum herein.",
      "Aber geltend machte sich jetzt der Drang, zu dieser Welterkenntnis mit dem Menschen darinnen, die selbständige menschliche Selbst- erkenntnis zu erstreben. Zu dem: Erkenne die Welt! trat hinzu das: Erkenne dich selbst! - Der Grieche stand wie am Ufer der Vergangenheit, hereinnehmend mit ihrem vollen Inhalt der Vergangenheit Weisheitsschätze.",
      "Wir - und ich glaube, jeder Unbefangene kann das fühlen - stehen an einem anderen Ufer. Wir stehen an dem Ufer einer unbestimmten Zukunft, aber einer Zukunft, welche die Menschheit in geistiger Beziehung selbst schaffen muß.",
      "Und wir fühlen, wir brauchen ein neues Wahrwort, um uns mit voller menschlicher Kraft zu besinnen auf das, was aus unserem Inneren als Schaffendes hinüberwirken kann in die unbestimmte Zukunft. Am Ufer der Vergangenheit richtete der Grieche das Wahrwort auf: Erkenne dich selbst!",
      "Am Ufer einer unbestimmten Zukunft müssen wir das Wahrwort aufrichten: Werde ein freies Wesen! Das, was in dem Hinundherschwingen zwischen den bei- den Polen der menschlichen Gegenwartsaufgaben liegt, davon möchte dieser Bau und alles, was in ihm gewirkt wird, sprechen.",
      "Davon möchte auch wiederum die kurze Reihe von Erkenntnis- und künstlerischen Darbietungen, die in den nächsten Tagen stattfinden sollen, sprechen. Wir stehen am Ausgangspunkt des großen naturwissen- schaftlichen Rätsels.",
      "Die Menschheit hat noch nicht den vollen Mut in sich erlebt, dieses große, gewaltige natur- wissenschaftliche Rätsel ins Auge zu fassen. Naturwissen- schaft hat Gewaltiges und Großes geleistet. Sie hat eine Anschauungsweise angenommen, durch die in der Kette 11 der Ursachen und Wirkungen sich immer eines der Ereig- nisse, die unsere Seelen schauen, an das andere der Ereig- nisse mit Notwendigkeit schließt.",
      "Und es ist der Natur- wissenschaft natürlichstes Bestreben, den Menschen einzu- beziehen in diese Kette natürlicher Notwendigkeit. Es ist das große Ideal naturwissenschaftlicher Erkenntnis, die Naturerscheinungen mit diesem Ursachengesetz zu studie- ren, sie - als ihrer Wesenheit entsprechend - gemäß diesem Ursachengesetze zu empfinden und so auch vom Menschen zu verstehen, was nach diesem Ursachengesetze von ihm zu verstehen ist.",
      "Man durchdringt nur nicht heute schon mit vollem lebendigem Gefühl, was in diesem Bestreben, in diesem Ideal für das menschliche Leben eigentlich liegt. Leben wir uns ganz in das ein, was wir in rechter Natur- erkenntnis als die Weltnotwendigkeit aufnehmen, dann stehen wir selbst mit unserem Bewußtsein in dieser Welt- notwendigkeit darinnen, dann müssen wir uns sagen: Alles, was in uns selber erlebt wird, ist nur ein Glied in der Kette der Notwendigkeiten.",
      "Wenn wir aber aus einer rechten Vertiefung in die naturwissenschaftliche Lebensauffassung uns ein solches Bewußtsein angeeignet haben, dann revoltiert unser Innerstes gegen diese Emp- findung, dann spricht ein unsere Seele durchleuchtendes Erlebnis gegen diese Empfindung, dann sagen wir uns: Als Mensch bin ich frei und meine Freiheit muß ich begreifen, mit meiner Erkenntnis muß ich eindringen ebenso wie in das Gewebe der Naturerscheinungen so in das Leben meiner Freiheit. Faßt man im vollen Sinne des Wortes dieses innere Frei- heitsrätsel auf, dann kommt man dazu, sich zu sagen: Das bedeutsame Wissen, dessen Entwickelung sich durch die letzten drei bis vier Jahrhunderte zieht und das in die 12 Natur so bedeutsam hineingeleuchtet hat, das braucht eine Erweiterung, um hineinzuleuchten auch in das Erlebnis der menschlichen Freiheit. - Denn immerzu gerechtfertigt wür- den diejenigen erscheinen, die aus dem naturwissenschaft- lichen Bewußtsein der Gegenwart heraus gesagt haben und immer wieder sagen: Wir können nur die Natur begreifen; wir können nicht anders, als haltmachen vor dem Begrei- fen der menschlichen Freiheit.",
      "Wir müssen das alte Kan- tische Wort wiederholen: Um für den Glauben Platz zu bekommen, müssen wir das Wissen vernichten. Jawohl, solange wir im bloßen Naturwissen drinnenstehen, so lange gilt dieses Wort.",
      "Dann aber kommt dagegen die Auf- bäumung, die Revolte des menschlichen Bewußtseins. Und gerade im richtigen Würdigen der größten naturwissen- schaftlichen Errungenschaften der neueren Zeit muß der Drang entstehen nach dem Wissen, nach dem Erkennen des Erlebnisses der menschlichen Freiheit.",
      "Und ein Erlebnis muß zugleich diese Erkenntnis sein. Denn von ihr ausgehend müssen wir die Kraft, die wir aus ihr gewinnen, hinaus- tragen in das soziale Leben, das uns heute nicht weniger Rätsel und Fragen aufgibt als das Erkenntnis- und Glau- bensleben.",
      "Wie sich die Rätsel und Fragen des Erkennens und des Glaubenslebens in der einsamen Stube in inner- lichen Seelenkämpfen ausleben, so wirken die anderen, die sozialen Rätsel und Fragen tumultuarisch durch die Welt: weil nicht Menschenkräfte in ihnen wirken, die aus klarem Freiheitsbewußtsein, aus erkenntnismäßig erlebtem Frei- heitsbewußtsein sich einzusetzen wissen gegen das, was uns als soziales Chaos heute umgibt. Wer das Freiheitsrätsel mit lebendigem Wissen durch- dringt, der allein ist imstande, in das soziale Leben die Kraft harmonischen menschlichen Zusammenlebens hinaus- zutragen.",
      "Weil uns in den letzten Jahrhunderten gerade dadurch, daß wir in die Tiefe des äußeren Geschehens eingedrungen sind, diese Kraft genommen worden ist, leben wir heute in dem sozialen Chaos. Licht wird es in diesem Chaos erst werden, wenn wir hineintreten mit der inneren Kraft, die uns das wissende Durchschauen des Freiheitsrätsels gibt.",
      "So wie einstmals der alte Grieche fragend gestanden hat vor alledem, was ihm eine alte Weisheit überlieferte, fragend gestanden hat vor dem: Erkenne die Welt! - und übergegangen ist zu dem: Er- kenne dich selbst! -, so müssen wir fragend stehen heute vor dem: Mensch, werde ein freies Wesen! Zwischen diesen beiden Polen menschlichen Geschehens, zwischen dem Pol, wo der griechische Weise hineinwarf in die Menge der Denkenden und Unbefangenen das Wort: Erkenne dich selbst! , und dem anderen Pole, der sich ausspricht in den Worten: Mensch, werde ein freies We- sen! - liegt im Grunde genommen eine Episode mensch- heitlicher Entwickelung.",
      "Es ist mit Händen zu greifen, wie zwischen diesen beiden Polen eine Episode menschheitlicher Entwickelung liegt. Nehmen wir den modernsten Menschen, von dem diese Freie Hochschule für Geisteswissenschaft ihren Namen leihend trägt, Goethe.",
      "Er fand sich hinein in das damals schon dämmernde und drängende neuzeitliche Leben, es vorempfindend in einer Zeit, in der die meisten noch voll in den Traditionen des Alten lebten. Wie wirkte es in Goethes Seele auf der einen Seite nach wahrer Erkenntnis, auf der anderen Seite nach wahrer Kunst hin, und in der Kunst bei ihm auch nach religiöser Vertiefung, nach reli- giöser Innerlichkeit.",
      "Es durchwogten seine Seele alle die Im- pulse welche eigentlich damals von ihm allein bemerkt wurden, höchstens noch von einigen seiner Freunde, welche aber mittlerweile in das allgemeine Menschenleben herauf- gestiegen sind -, alle die Impulse, die hinneigen, hinzielen nach dem in Freiheit ergriffenen sozialen Leben. Und als er stark genug gefühlt hat, was wie die Morgendämmerung einer neuen Zeit in ihm lebte, da wandte er der nordischen Welt den Rücken und ging hin nach dem Süden, um aus dem, was übriggeblieben war von der alten Griechenkultur herauszuempfinden, was dieser Griechenkultur tiefstes Wesen war.",
      "Dieser moderne Mensch, Goethe, hatte in seiner eigenen Seele die weitgespannte Brücke schlagen wollen über die Episode hin zwischen den Zukunftsaufgaben der modernen Menschheit und dem weltumfassenden Resümee der Vergangenheit, wie es im Griechentum gezogen wor- den ist. Und lebt denn nicht das, was Goethe so an seiner eigenen Persönlichkeit dargestellt hat, im Grunde genommen heute in jedem Menschen, der hinaufstreben will nach jener Sphäre, wo ihm entgegentreten können in ihren wahren Gestalten die großen Weltenfragen?",
      "Schöpfen denn die- jenigen, die sich unserer Bildung widmen, nicht noch immer das, was dieser Bildung den formalen Untergrund geben soll, aus dem Griechentum? Wird nicht das Herz und der Verstand derer, die für diese Bildung heranerzogen wer- den, in unserer Gymnasialbildung noch immer vom Grie- chentum durchdrungen? - Wir müssen diese Episode emp- finden, wie sie erst tragisch und dann erlösend Goethe der Menschheit vorempfunden hat.",
      "Dann aber werden wir auch verstehen, wie wir uns in einer neuen Weise zuwen- den müssen auch dem anderen Pole, dem Pole menschlicher Selbsterkenntnis, wie wir uns in dem Augenblicke welt- geschichtlicher Entwickelung, in dem aus unserem tiefsten Inneren das Wort herauftönt: Mensch, werde ein freies Wesen! - auch dem: Erkenne dich selbst! - anders nähern müssen, als der Grieche sich ihm genähert hat. Sehen wir uns um gerade unter denjenigen, die sich mit ihrer ganzen Seelenverfassung hineingelebt haben in die moderne naturwissenschaftliche Weltanschauung, die auf ihrem Boden so groß geworden ist.",
      "Wir sehen, wie sich da der Mensch in der Beobachtung sowohl wie im Experiment, durch die ja so viele Rätsel für den modernen Menschen gelöst worden sind, vertieft in das materielle Dasein. Und man sollte genauer, als man das gewohnt ist, hinhorchen auf ein solches Wort, wie es aus diesem neuzeitlichen Be- wußtsein heraus etwa ein Du Bois-Reymond gesprochen hat: Da, wo Materie spukt, kann die menschliche Erkennt- nis nichts anfangen!",
      "Das materielle Dasein zu durchdrin- gen, daran hat sich die moderne Erkenntnis gewöhnt. Sie hat Großartiges auf diesem Gebiete geleistet. Überall ver- folgt sie, wie die materielle Welt sich in den materiellen Erscheinungen gliedert.",
      "Aber indem sie das Gewebe der materiellen Erscheinungen entziffern will, muß sie das- jenige voraussetzen, in das sie niemals hineindringen kann, wenn sie auf ihrem eigenen Boden bleibt: die Welt der Materie selber. Es ist eine lange Geschichte, was sich da abgespielt hat zwischen dem Streben menschlicher Erkenntnis und dem Materierätsel.",
      "Was sich auf theoretischem Gebiete da abge- spielt hat, kann uns in diesem Augenblicke weniger inter- essieren. Auf das aber, was als Rückstand geblieben ist im menschlichen Gemüte, im ganzen menschlichen Leben, darauf muß aufmerksam gemacht werden.",
      "So sehr man glaubte, auf bloßen Erkenntniswegen zu wandeln bei der Beschäftigung mit den materiellen Erscheinungen, so sehr begründete man, indem man die Materie als solche voraus- setzte, in der Seelentiefe eine Empfindungsgrundlage, die das ganze menschliche Leben durchsetzt. Und eine solche Empfindungsgrundlage haben wir.",
      "Bei den besten unserer 16 Zeitgenossen können wir sie bemerken. Sie mühen sich ab an dem Materierätsel; sie ringen mit diesem Materierätsel. Und eine ganze Anzahl von ihnen konnte nicht anders, als aus diesem Ringen sich herausheben und zugeben, daß das Menschenrätsel doch auf diesem Wege nicht gefunden, nicht gelöst werden könne, auch nicht im relativen Sinne.",
      "Und doch ist diese Lösung für die Sicherheit der menschlichen Seele notwendig. Man möchte nun «im Inneren des Men- schen» dem wahren Wesen des Menschen beikommen, aber man hat seinen Geist an der Außenwelt, «die nicht zu durchschauen ist», an den «Voraussetzungen des materiel- len Daseins» zu denken, zu empfinden gewöhnt.",
      "Was man sich da angewöhnt hat, es verzichtet auf das Durchschauen. Und wendet man diesen Geist, der auf das Durchschauen verzichtet, nach innen, so wird man im modernen schlech- ten Sinne Mystiker. Das bemerken heute leider nur allzuwenige: daß die Besten, die von unserer Naturerkenntnis sich abwenden und zu einem Streben nach Erkenntnis des menschlichen Inneren kommen, sich ihre Denk- und Empfindungsge- wohnheiten an dem Betrachten der Materie, «die undurch- schaubar ist», angeeignet haben, und nun in das mensch- liche Innere das, was sie sich als Denk- und Empfindungs- gewohnheiten am Betrachten der Außenwelt angeeignet haben, hineintragen.",
      "Wenn man aber den Blick, den man zuerst an der dunklen, finsteren «Materie» geschult hat, nach innen wendet, dann wird nebulose Mystik daraus, und die nebulose Mystik verriegelt das Tor zu dem: Er- kenne dich selbst! Das ist es, worauf mit starker Betonung alles hinweisen möchte, was innerhalb dieser Freien Hochschule für Gei- steswissenschaft gewirkt wird.",
      "Vermieden muß werden der Weg nebuloser Mystik ebenso wie der Weg, der einzig und allein in äußere naturwissenschaftliche Notwendigkeit und damit in Vernichtung der Freiheitserkenntnis hinein- führt. Vermeiden können wir diese Wege nur, wenn wir wirkliche Geisteswissenschaft suchen, nicht jene Geistes- wissenschaft, die nicht haltmachen darf vor dem mensch- lichen Inneren, welche dann, nachdem sie haltgemacht hat, den Weg doch weiter fortsetzt, indem sie mystische Nebel in dieses menschliche Innere hineinstrahlt.",
      "Nicht darf dieses die hier gemeinte Geisteswissenschaft tun! Mit jener Schu- lung, die gewonnen worden ist in heller, klarer, lichtvoller Erkenntnis an den äußeren Tatsachen, muß mystikfrei, aber geisteswissenschaftlich hineingeleuchtet werden kön- nen in das menschliche Innere.",
      "Das: Erkenne dich selbst! - darf nicht in mystischem Leben, dunkel, es muß in heller, lichter Klarheit erfaßt werden. Dann wird sich zusammen- schließen das, was dem Menschen ersprießt aus der Innen- erkenntnis, aus der Erfüllung des Wortes: Erkenne dich selbst! und was ihm ersprießt aus dem sich zur äuße- ren Natur Erkennendverhalten unter dem Wahrworte: Mensch, werde ein freies Wesen!",
      "Wie zwei Säulen, die ideell im Geiste dastehen, wenn man diesen Bau betritt, möchten angesehen werden diese zwei Wahrworte: die Säule wahrhaftiger, lichtvoller menschlicher Selbsterkenntnis und die Säule der mensch- lichen Freiheit. Die erste ist geeignet, an dasjenige den Menschen zu mahnen, was ihm Sicherheit und Halt, künst- lerische Betätigung und religiöse Befriedigung gewähren kann.",
      "Die andere ist geeignet, ihn mit Kraft auszustatten, mitzuwirken bei den drängenden sozialen Fragen der Ge- genwart und der nächsten Zukunft. Von alledem, was hier in der Befruchtung der einzelnen Fachwissenschaften ange- strebt wird, wie sich insbesondere in den nächsten Tagen zeigen soll, möchte der weltgeschichtliche Moment erfaßt 18 sein, so gut er eben in aller Bescheidenheit erfaßt wer- den kann, der uns ebenso an das Ufer einer unbestimmten Zukunft stellt, wie der Grieche an das Ufer einer er- füllten, überwältigend wirkenden Vergangenheit gestellt war.",
      "Dazu aber müssen wir kommen, daß wir das lichtvolle Erfassen des menschlichen Inneren in dem Wissen selber fühlen, daß wir das Wissen nicht mehr bloß hinschleppen am äußeren Beobachten und am äußeren Experimente, sondern daß wir es frei erheben und, indem wir es durch- kraften mit dem inneren Wesen des Menschen, uns mit diesem Wissen hineinversetzen in das Leben der Freiheit, in das uns die bloße naturwissenschaftliche Betrachtung niemals hineinversetzen kann. Naturwissenschaftlich ist es ehrlich, die Freiheit zu leugnen, menschlich ist es, gegen diese Leugnung zu protestieren und in diesem Protest den Ausgangspunkt einer freien, aus dem menschlichen Inneren ihren Organen nach geborenen Geisteswissenschaft zu sehen.",
      "Dieser Geisteswissenschaft gegenüber braucht man, weil sie eindringt nicht in das Tote, sondern in das Leben, nicht zu fürchten, daß sie wie die tote Verstandeswissenschaft ertötend wirken werde auf die Kunst. Sie wird aus dem, was sie aus dem Geiste herausholt, die Kunst befruchten können.",
      "Es wird dieses Erkennen selbst nach außen künst- lerisch wirken können, weil es in lichtvoller Klarheit hin- untertaucht in menschliche Tiefen. Es wird einlaufen aus dem wahren Erkennen in das Verehren desjenigen, was sich im menschlichen Inneren offenbaren kann.",
      "Und es wird eine solche, nur mehr die Form der Mystik festhal- tende Erkenntnis, die aber zum Lichte strebt, zu gleicher Zeit auslaufen lassen das menschliche Wissen in religiöse Verehrung des Höchsten, was durch die Welt hindurch lebt und webt. Neue künstlerische Kräfte, neue religiöse Ver- tiefungen werden aus einem solchen, das Innere des Men- schen erfassenden Wissen kommen können.",
      "Und das Leben, in das ein solches Wissen untertauchen darf, wird ein Leben in Freiheit sein. Es wird dem Menschen zunächst das Be- wußtsein der Freiheit sicherstellen. Der Mensch wird sich nicht zu verlieren brauchen an die äußere Naturnotwen- digkeit, an die er sich mit dem bloßen naturwissenschaft- lichen Bewußtsein verliert, weil diesem nur Notwendigkeit und nicht Freiheit vorliegt.",
      "Und frei wird der Künstler werden von dem bloßen Modell in der Nachahmung der äußeren Natur, die er doch niemals erreichen kann. Aus geistigen Höhen herun- ter wird er holen, was er der Materie einprägen will.",
      "Ein schwacher Anfang zu solchem Herunterholen von Formen, die dem freien Geiste sich offenbaren, die sich nicht knüp- fen an Nachahmung im Modell, soll sein, was aus den For- men und dem Bildnerischen und dem sonstigen Künstle- rischen dieses Baues spricht. Und frei von allem bloß Traditionellen, das an den Menschen als ein Äußeres, als ein Unfreies herantritt, soll das religiöse Erleben werden: frei ergreifend, was sich als das Göttliche im Inneren des Menschen selber enthüllt, frei im Inneren sich verbindend mit derjenigen Kraft, die sich ihrer wahren Wesenheit nach doch nur in Freiheit mit diesem menschlichen Inneren wahrhaftig verbinden will: der Christus-Kraft.",
      "Wissen nach den verschiedensten Gebieten hin nach dem äußeren Natürlichen, nach dem Inneren des Men- schen, nach dem beides umfassenden Einheitlichen -, das ist das neue Streben nach Erfüllung des Wortes: Erkenne dich selbst! - Dreifacher Schritt der Freiheit: Freiheit im inneren Erleben des Menschlichsten, Freiheit im Schaffen, 20 auch im künstlerischen Schaffen, Freiheit im religiösen Erleben, das ist das andere. Dazu soll führen die Befruchtung der einzelnen Wissen- schaften und menschlichen Lebenszweige und des ganzen sozialen Lebens, wovon in den nächsten Tagen hier ge- sprochen werden soll.",
      "Gezeigt werden soll, daß aus den einzelnen Wissenschaften heraus nicht nur - wie es eine moderne, in den Tod gehende Philosophie tun will ge- wisse Sätze gewonnen werden können, aus denen man dann eine abstrakte Weltanschauung zusammenzimmert, sondern daß durch Geistbeobachtung eine Weltanschauung über allem Sinnlichen gewonnen werden kann, und daß in die einzelnen Fachwissenschaften diese allgemeine, licht- voll erfaßte Weltanschauung hineinleuchten kann. Man hat auch verlangt, daß die Weltanschauung sich nähre aus dem, was ihr die einzelnen Wissenschaften und ihre Ergebnisse abgeben.",
      "Die Zeit ist gekommen, wo aus einer im Geiste erlebten Weltanschauung die Ergebnisse herunterstrahlen in die einzelnen Wissenschaften. Mag das die Welt heute noch wenig erkennen, das, was hier an die- sem Orte geschieht, das soll niemals aus einem anderen Ton als aus dem heraus kommen, der selber impulsiert ist auf der einen Seite von dem wahrhaftigen: Erkenne dich selbst! - auf der anderen Seite von dem: Mensch, werde ein freies Wesen! - Das ruft uns aber nicht nur die einsame Wissenschaftsbetrachtung im menschlichen Inneren zu.",
      "Das ruft uns zu unsere ganze katastrophale Zeit von heute. Und wenn wir zusammenfassen, was im Tiefsten ruht in den Zeitenrätseln und Zeitenfragen, so ist es das, was ich versuchte heute anzutönen. Von dem, was uns so aufgegeben ist von den Zeichen der Zeit wie von dem fühlenden Menschenwesen, das inner- halb dieser Zeit steht, darf man so sprechen zum Alter.",
      "Diese älteren Menschen haben es erfahren, was es heißt, in einer katastrophalen Zeit zu leben. Sie fühlen, wie ab- getaut sind die Ideale ihrer Jugend. Sie fühlen, wie ausge- flossen ist in ein Zivilisationschaos, was sie glaubten in ihrer Jugend hinauszutragen in die moderne abendlän- dische Zivilisation.",
      "Zu ihnen, die solches erfahren haben, darf so gesprochen werden, wie heute gesprochen worden ist. Denn es muß solches Wort die Seite im menschlichen Seelenleben finden, die da sagt: Wir müssen noch benützen des Lebens Rest, um die Menschheit hinzuweisen auf Stär- keres, als dasjenige war, was durch uns gewirkt hat.",
      "Und auch zur Jugend darf mit solchen Worten gespro- chen werden. Denn sie schaut noch in voller Kraft, was im Zusammensturz ist, was in der Katastrophe lebt. Sie kann fühlen, innehabend ihre volle Menschenkraft und volle Menschenbegeisterung, daß etwas Neues, etwas Kraftvolles geschehen muß.",
      "Und der rechte Alte von heute wird suchen das Wort, das zünden kann in der Jugend, auf daß andere Zeiten sehen die Seelen, die aus den Augen der heutigen Jugend in die Welt blicken, als sehen müssen die Seelen, die durch heute alte Augen in die Welt blicken. Und so darf man wohl zu jedem Lebensalter sprechen.",
      "So darf man sprechen zu denen, die man in einer gewissen Sprache die «alten Häuser» aller Sorten nennt, so darf man sprechen zu den jungen Kommilitonen. Denn so darf man sprechen nicht nur aus den Zeitenaufgaben heraus, sondern aus den größten Aufgaben des menschlichen We- sens selbst.",
      "Und wir leben in einer Zeit, wo des Menschen größte Lebensfragen Zeitaufgaben geworden sind. Wir leben in einer Zeit, in der wir hineinschauen können in der Menschen tiefstes Innere. Und wir werden da geschrieben sehen die Aufforderung zu handeln, zu handeln in einer Richtung, die wir zugleich angegeben finden, wenn wir 22 hinschauen auf die äußeren Zeichen der Zeit mit ihrer deutlichen Sprache.",
      "Von dem, was in dieser zweifachen Blickrichtung liegt, möchte in den nächsten Tagen gesprochen werden. Möchte das Gesprochene Aufmerksamkeit finden. Denn in der heutigen Zeit den Menschen verstehen, heißt, ein Wichtig- stes im Menschenleben selber empfinden und fühlen.",
      "Der allein stellt sich heute recht und gerecht in das menschliche Wirken der Zeit hinein, der sich zu sagen versteht: in den Zeichen der Zeit liegt die Aufforderung ausgesprochen, ins tiefste menschliche Innere erkennend, geist-erkennend hin- einzuschauen. Und was der Mensch nur in seinem Inneren heute ergründen kann, ist zu gleicher Zeit das, was zu erkennen, zu fühlen, zu wollen, zu vollbringen uns auf- fordern die deutlich sprechenden Zeichen der Zeit.",
      "Auf die Eröffnungsrede Rudolf Steiners folgte ein Vortrag Albert Steffens über «Das Werden des Kunstwerks». Darauf sprach Frau Marie Steiner die von Rudolf Steiner schon für die Eröffnungsfeier des Ersten Hochschulkurses umgestalteten Worte des Hilarius aus: «Der Hüter der Schwelle»: In jenes Geistes Namen, der den Seelen In unsrem Strebensorte sich verkündet, Erscheine ich in diesem Augenblicke Vor Menschen, die von jetzt an hören wollen Das Wort, das hier den Seelen ernst erklingt.",
      "Nicht frühern Zeiten konnten jene Mächte, Die unsres Erdenwerdens Ziele lenken, In vollbewußter Art sich offenbaren. Denn wie im Kinderleibe erst allmählich Die Kräfte reifen müssen und erstarken, Die zu des Wissens Trägern sind bestimmt, So mußte sich als Ganzes auch entfalten Das Menschentum in seinem Erdenlauf.",
      "In Dumpfheit lebten erst die Seelentriebe, Die später würdig sich erweisen sollten, Aus hohen Welten Geisteslicht zu schauen. Doch wurden als der Menschen weise Führer Im Erdbeginn dem Geist ergebne Seelen Von höhren Daseinsmächten auserwählt.",
      "Sie pflegten in des Wissens Strebeorten Die Geisteskräfte, die Erkenntnisstrahlen In Seelen sandten, die nur dumpf bewußt Von ihrem Schauen sich durchdringen konnten. Erst später konnten aus der Menschen Reihen Die Geistesforscher sich die Schüler holen, Die durch das willensstarke Prüfungsleben Sich reif erwiesen, in Bewußtheits Helle Zum Geisteswissen zielvoll hinzustreben.",
      "Und als der ersten Führer Schüler später Das edle Gut in Würde pflegen konnten, Verschwand die unbewußte Führerschaft, Daß freie Seelen wissend streben durften. Und freie Seelen wählten sich dann Menschen, Die ihnen folgen durften in der Pflege Des Geistesschatzes; und so ging es weiter Von einem Menschenalter hin zum ändern.",
      "Es sind bis jetzt ja alle Wissensstätten, Die dies in Wahrheit sind, gerecht entsprungen Der höchsten, die in Geistessphären steht. In ernstem Suchen streben wir allhier Nach wahrem Geistes-Menschenerbe hin.",
      "Wir werden niemals von Erkenntnis sprechen, Die nicht des Geistes eignes Siegel trägt, Allein vom Lichte aus den Geisteswelten, Das schauend Menschen sich erschließen kann, Die sich ihm strebend anvertrauen wollen, Um ihrer Seele Tiefen zu ergründen. Zu diesem Lichte würdig hinzustreben, Das weiset uns der Zeitenwende Ernst Und ihre Not; die Zeichen sind fürwahr Bedeutungsschwer, die sich im Weltenplane Jetzt Geistesaugen deutlich offenbaren."
    ],
    "sentences": [
      [
        "Meine sehr verehrten Anwesenden!",
        "Unsere Zeit ist eine Zeit der Zweifel und Rätsel, die der Menschheit aufgege- ben sind.",
        "Und man kann sagen, wohl dem, der sich in sei- nem Inneren ehrlich und mit Kraft gegenüber den Ge- schehnissen der Gegenwart sagen kann: Ja, für mich ist diese Zeit eine Zeit der Zweifel, der Rätsel und der Fra- gen, die gelöst werden müssen. - Denn könnte er sich dies nicht sagen und würde er doch mit wacher Seele hinblicken auf die Geschehnisse der Zeit, so gäbe es für ihn eigentlich nur den anderen Pol: die Verzweiflung an dem Fortgange der menschlichen Zivilisation im Abendlande."
      ],
      [
        "Und wenn in unserer Zeit Zweifel, Fragen, Rätsel verborgen sind, die gelöst werden müssen, dann bedarf es dazu der starken Kraft der Menschen, die sich zurechtfinden können in dem gegenwärtigen Zivilisationschaos, und die aus der Flut der Fragen und Rätsel das aufsprießen lassen können, was zu einem neuen Fortgang, zu einem Aufbau unserer abend- ländischen Zivilisation führen kann.",
        "Etwas dazu beitragen, daß die Kräfte, welche die Zeit also braucht, damit die Zweifel und Rätsel aus den menschlichen Seelen heraus ge- löst werden können, das möchte alles, was von diesem Goetheanum aus unternommen wird."
      ],
      [
        "In einer solchen Zeit der Fragen und Rätsel wird sich auch für manches, was Inhalt alter Überlieferung ist, die Not- wendigkeit zeigen, in einem neuen Lichte zu erscheinen.",
        "Nun leuchtet uns herauf - gewissermaßen wie ein uralt heiliges Vermächtnis der Griechenkultur - das oft und oft wiederholte apollinische Wort: Mensch, erkenne dich selbst!"
      ],
      [
        "Und vieles in der abendländischen Zivilisation seit der alten Griechenzeit hat gestanden im Zeichen dieses Wortes.",
        "Mir scheint aber, daß selbst ein solches, wie es schien, felsenfest in der Menschheitsentwickelung drinnen- stehendes Zauberwort heute, in unseren Zeiten der großen Verwandlungen, nur mehr Bestand haben kann, wenn es, aufnehmend die Kräfte unserer Zeit, selbst eine Art Ver- wandlung durchmacht."
      ],
      [
        "Und so scheint mir, daß das uralte Delphiwort heute also zu den Menschen klingen müsse: Mensch, erkenne dich selbst und werde ein freies Wesen! - Wir müssen das Weltgeschehen, insofern es sich auf den Menschen bezieht, hin- und herschwingend schauen können zwischen den beiden Polen der Selbsterkenntnis und der wahren menschlichen Freiheit.",
        "Warum schrieb griechische Weisheit auf den Tempel zu Delphi das bedeutungsvolle Wort: Erkenne dich selbst? - Zu diesem Griechentum leuchtete herauf, aus uralten, hi- storisch ihrem Anfange nach unbestimmbaren Zeiten, eine uralte geheiligte Weisheit und Wissenschaft."
      ],
      [
        "Die Ur- sprünge dieser Wissenschaft gehen in das Dunkel der vor- geschichtlichen Zeiten zurück.",
        "In Ägypten hatte man noch ein unmittelbares Drinnenstehen in dieser Urweisheit.",
        "In Griechenland hatte man nur noch ein, allerdings in die edle griechische Menschlichkeit getauchtes Gefühl davon, und man fühlte: aus der Welt, aus der weisheitsvollen Welt selbst heraus war den Menschen diese Weisheit gekommen."
      ],
      [
        "Der Mensch hatte sich innerhalb der Welt der Weisheit gefühlt wie ein mehr oder weniger nur instinktiv lebendes, mehr oder weniger unbewußtes Glied des Weltenganzen.",
        "Da dämmerte herauf im griechischen Fühlen die Empfin- dung der Selbständigkeit der Menschenseele."
      ],
      [
        "Zu dem alten Welterkennen hinzu sollte erstrebt werden die Selbst- 10 erkenntnis des Menschen.",
        "Im Grunde genommen war der uralten Weisheit Devise: Erkenne die Welt und in der Welt den Menschen! - Diese Devise uralter Weisheit strahlte in das Griechentum herein."
      ],
      [
        "Aber geltend machte sich jetzt der Drang, zu dieser Welterkenntnis mit dem Menschen darinnen, die selbständige menschliche Selbst- erkenntnis zu erstreben.",
        "Zu dem: Erkenne die Welt! trat hinzu das: Erkenne dich selbst! - Der Grieche stand wie am Ufer der Vergangenheit, hereinnehmend mit ihrem vollen Inhalt der Vergangenheit Weisheitsschätze."
      ],
      [
        "Wir - und ich glaube, jeder Unbefangene kann das fühlen - stehen an einem anderen Ufer.",
        "Wir stehen an dem Ufer einer unbestimmten Zukunft, aber einer Zukunft, welche die Menschheit in geistiger Beziehung selbst schaffen muß."
      ],
      [
        "Und wir fühlen, wir brauchen ein neues Wahrwort, um uns mit voller menschlicher Kraft zu besinnen auf das, was aus unserem Inneren als Schaffendes hinüberwirken kann in die unbestimmte Zukunft.",
        "Am Ufer der Vergangenheit richtete der Grieche das Wahrwort auf: Erkenne dich selbst!"
      ],
      [
        "Am Ufer einer unbestimmten Zukunft müssen wir das Wahrwort aufrichten: Werde ein freies Wesen!",
        "Das, was in dem Hinundherschwingen zwischen den bei- den Polen der menschlichen Gegenwartsaufgaben liegt, davon möchte dieser Bau und alles, was in ihm gewirkt wird, sprechen."
      ],
      [
        "Davon möchte auch wiederum die kurze Reihe von Erkenntnis- und künstlerischen Darbietungen, die in den nächsten Tagen stattfinden sollen, sprechen.",
        "Wir stehen am Ausgangspunkt des großen naturwissen- schaftlichen Rätsels."
      ],
      [
        "Die Menschheit hat noch nicht den vollen Mut in sich erlebt, dieses große, gewaltige natur- wissenschaftliche Rätsel ins Auge zu fassen.",
        "Naturwissen- schaft hat Gewaltiges und Großes geleistet.",
        "Sie hat eine Anschauungsweise angenommen, durch die in der Kette 11 der Ursachen und Wirkungen sich immer eines der Ereig- nisse, die unsere Seelen schauen, an das andere der Ereig- nisse mit Notwendigkeit schließt."
      ],
      [
        "Und es ist der Natur- wissenschaft natürlichstes Bestreben, den Menschen einzu- beziehen in diese Kette natürlicher Notwendigkeit.",
        "Es ist das große Ideal naturwissenschaftlicher Erkenntnis, die Naturerscheinungen mit diesem Ursachengesetz zu studie- ren, sie - als ihrer Wesenheit entsprechend - gemäß diesem Ursachengesetze zu empfinden und so auch vom Menschen zu verstehen, was nach diesem Ursachengesetze von ihm zu verstehen ist."
      ],
      [
        "Man durchdringt nur nicht heute schon mit vollem lebendigem Gefühl, was in diesem Bestreben, in diesem Ideal für das menschliche Leben eigentlich liegt.",
        "Leben wir uns ganz in das ein, was wir in rechter Natur- erkenntnis als die Weltnotwendigkeit aufnehmen, dann stehen wir selbst mit unserem Bewußtsein in dieser Welt- notwendigkeit darinnen, dann müssen wir uns sagen: Alles, was in uns selber erlebt wird, ist nur ein Glied in der Kette der Notwendigkeiten."
      ],
      [
        "Wenn wir aber aus einer rechten Vertiefung in die naturwissenschaftliche Lebensauffassung uns ein solches Bewußtsein angeeignet haben, dann revoltiert unser Innerstes gegen diese Emp- findung, dann spricht ein unsere Seele durchleuchtendes Erlebnis gegen diese Empfindung, dann sagen wir uns: Als Mensch bin ich frei und meine Freiheit muß ich begreifen, mit meiner Erkenntnis muß ich eindringen ebenso wie in das Gewebe der Naturerscheinungen so in das Leben meiner Freiheit.",
        "Faßt man im vollen Sinne des Wortes dieses innere Frei- heitsrätsel auf, dann kommt man dazu, sich zu sagen: Das bedeutsame Wissen, dessen Entwickelung sich durch die letzten drei bis vier Jahrhunderte zieht und das in die 12 Natur so bedeutsam hineingeleuchtet hat, das braucht eine Erweiterung, um hineinzuleuchten auch in das Erlebnis der menschlichen Freiheit. - Denn immerzu gerechtfertigt wür- den diejenigen erscheinen, die aus dem naturwissenschaft- lichen Bewußtsein der Gegenwart heraus gesagt haben und immer wieder sagen: Wir können nur die Natur begreifen; wir können nicht anders, als haltmachen vor dem Begrei- fen der menschlichen Freiheit."
      ],
      [
        "Wir müssen das alte Kan- tische Wort wiederholen: Um für den Glauben Platz zu bekommen, müssen wir das Wissen vernichten.",
        "Jawohl, solange wir im bloßen Naturwissen drinnenstehen, so lange gilt dieses Wort."
      ],
      [
        "Dann aber kommt dagegen die Auf- bäumung, die Revolte des menschlichen Bewußtseins.",
        "Und gerade im richtigen Würdigen der größten naturwissen- schaftlichen Errungenschaften der neueren Zeit muß der Drang entstehen nach dem Wissen, nach dem Erkennen des Erlebnisses der menschlichen Freiheit."
      ],
      [
        "Und ein Erlebnis muß zugleich diese Erkenntnis sein.",
        "Denn von ihr ausgehend müssen wir die Kraft, die wir aus ihr gewinnen, hinaus- tragen in das soziale Leben, das uns heute nicht weniger Rätsel und Fragen aufgibt als das Erkenntnis- und Glau- bensleben."
      ],
      [
        "Wie sich die Rätsel und Fragen des Erkennens und des Glaubenslebens in der einsamen Stube in inner- lichen Seelenkämpfen ausleben, so wirken die anderen, die sozialen Rätsel und Fragen tumultuarisch durch die Welt: weil nicht Menschenkräfte in ihnen wirken, die aus klarem Freiheitsbewußtsein, aus erkenntnismäßig erlebtem Frei- heitsbewußtsein sich einzusetzen wissen gegen das, was uns als soziales Chaos heute umgibt.",
        "Wer das Freiheitsrätsel mit lebendigem Wissen durch- dringt, der allein ist imstande, in das soziale Leben die Kraft harmonischen menschlichen Zusammenlebens hinaus- zutragen."
      ],
      [
        "Weil uns in den letzten Jahrhunderten gerade dadurch, daß wir in die Tiefe des äußeren Geschehens eingedrungen sind, diese Kraft genommen worden ist, leben wir heute in dem sozialen Chaos.",
        "Licht wird es in diesem Chaos erst werden, wenn wir hineintreten mit der inneren Kraft, die uns das wissende Durchschauen des Freiheitsrätsels gibt."
      ],
      [
        "So wie einstmals der alte Grieche fragend gestanden hat vor alledem, was ihm eine alte Weisheit überlieferte, fragend gestanden hat vor dem: Erkenne die Welt! - und übergegangen ist zu dem: Er- kenne dich selbst! -, so müssen wir fragend stehen heute vor dem: Mensch, werde ein freies Wesen!",
        "Zwischen diesen beiden Polen menschlichen Geschehens, zwischen dem Pol, wo der griechische Weise hineinwarf in die Menge der Denkenden und Unbefangenen das Wort: Erkenne dich selbst! , und dem anderen Pole, der sich ausspricht in den Worten: Mensch, werde ein freies We- sen! - liegt im Grunde genommen eine Episode mensch- heitlicher Entwickelung."
      ],
      [
        "Es ist mit Händen zu greifen, wie zwischen diesen beiden Polen eine Episode menschheitlicher Entwickelung liegt.",
        "Nehmen wir den modernsten Menschen, von dem diese Freie Hochschule für Geisteswissenschaft ihren Namen leihend trägt, Goethe."
      ],
      [
        "Er fand sich hinein in das damals schon dämmernde und drängende neuzeitliche Leben, es vorempfindend in einer Zeit, in der die meisten noch voll in den Traditionen des Alten lebten.",
        "Wie wirkte es in Goethes Seele auf der einen Seite nach wahrer Erkenntnis, auf der anderen Seite nach wahrer Kunst hin, und in der Kunst bei ihm auch nach religiöser Vertiefung, nach reli- giöser Innerlichkeit."
      ],
      [
        "Es durchwogten seine Seele alle die Im- pulse welche eigentlich damals von ihm allein bemerkt wurden, höchstens noch von einigen seiner Freunde, welche aber mittlerweile in das allgemeine Menschenleben herauf- gestiegen sind -, alle die Impulse, die hinneigen, hinzielen nach dem in Freiheit ergriffenen sozialen Leben.",
        "Und als er stark genug gefühlt hat, was wie die Morgendämmerung einer neuen Zeit in ihm lebte, da wandte er der nordischen Welt den Rücken und ging hin nach dem Süden, um aus dem, was übriggeblieben war von der alten Griechenkultur herauszuempfinden, was dieser Griechenkultur tiefstes Wesen war."
      ],
      [
        "Dieser moderne Mensch, Goethe, hatte in seiner eigenen Seele die weitgespannte Brücke schlagen wollen über die Episode hin zwischen den Zukunftsaufgaben der modernen Menschheit und dem weltumfassenden Resümee der Vergangenheit, wie es im Griechentum gezogen wor- den ist.",
        "Und lebt denn nicht das, was Goethe so an seiner eigenen Persönlichkeit dargestellt hat, im Grunde genommen heute in jedem Menschen, der hinaufstreben will nach jener Sphäre, wo ihm entgegentreten können in ihren wahren Gestalten die großen Weltenfragen?"
      ],
      [
        "Schöpfen denn die- jenigen, die sich unserer Bildung widmen, nicht noch immer das, was dieser Bildung den formalen Untergrund geben soll, aus dem Griechentum?",
        "Wird nicht das Herz und der Verstand derer, die für diese Bildung heranerzogen wer- den, in unserer Gymnasialbildung noch immer vom Grie- chentum durchdrungen? - Wir müssen diese Episode emp- finden, wie sie erst tragisch und dann erlösend Goethe der Menschheit vorempfunden hat."
      ],
      [
        "Dann aber werden wir auch verstehen, wie wir uns in einer neuen Weise zuwen- den müssen auch dem anderen Pole, dem Pole menschlicher Selbsterkenntnis, wie wir uns in dem Augenblicke welt- geschichtlicher Entwickelung, in dem aus unserem tiefsten Inneren das Wort herauftönt: Mensch, werde ein freies Wesen! - auch dem: Erkenne dich selbst! - anders nähern müssen, als der Grieche sich ihm genähert hat.",
        "Sehen wir uns um gerade unter denjenigen, die sich mit ihrer ganzen Seelenverfassung hineingelebt haben in die moderne naturwissenschaftliche Weltanschauung, die auf ihrem Boden so groß geworden ist."
      ],
      [
        "Wir sehen, wie sich da der Mensch in der Beobachtung sowohl wie im Experiment, durch die ja so viele Rätsel für den modernen Menschen gelöst worden sind, vertieft in das materielle Dasein.",
        "Und man sollte genauer, als man das gewohnt ist, hinhorchen auf ein solches Wort, wie es aus diesem neuzeitlichen Be- wußtsein heraus etwa ein Du Bois-Reymond gesprochen hat: Da, wo Materie spukt, kann die menschliche Erkennt- nis nichts anfangen!"
      ],
      [
        "Das materielle Dasein zu durchdrin- gen, daran hat sich die moderne Erkenntnis gewöhnt.",
        "Sie hat Großartiges auf diesem Gebiete geleistet.",
        "Überall ver- folgt sie, wie die materielle Welt sich in den materiellen Erscheinungen gliedert."
      ],
      [
        "Aber indem sie das Gewebe der materiellen Erscheinungen entziffern will, muß sie das- jenige voraussetzen, in das sie niemals hineindringen kann, wenn sie auf ihrem eigenen Boden bleibt: die Welt der Materie selber.",
        "Es ist eine lange Geschichte, was sich da abgespielt hat zwischen dem Streben menschlicher Erkenntnis und dem Materierätsel."
      ],
      [
        "Was sich auf theoretischem Gebiete da abge- spielt hat, kann uns in diesem Augenblicke weniger inter- essieren.",
        "Auf das aber, was als Rückstand geblieben ist im menschlichen Gemüte, im ganzen menschlichen Leben, darauf muß aufmerksam gemacht werden."
      ],
      [
        "So sehr man glaubte, auf bloßen Erkenntniswegen zu wandeln bei der Beschäftigung mit den materiellen Erscheinungen, so sehr begründete man, indem man die Materie als solche voraus- setzte, in der Seelentiefe eine Empfindungsgrundlage, die das ganze menschliche Leben durchsetzt.",
        "Und eine solche Empfindungsgrundlage haben wir."
      ],
      [
        "Bei den besten unserer 16 Zeitgenossen können wir sie bemerken.",
        "Sie mühen sich ab an dem Materierätsel; sie ringen mit diesem Materierätsel.",
        "Und eine ganze Anzahl von ihnen konnte nicht anders, als aus diesem Ringen sich herausheben und zugeben, daß das Menschenrätsel doch auf diesem Wege nicht gefunden, nicht gelöst werden könne, auch nicht im relativen Sinne."
      ],
      [
        "Und doch ist diese Lösung für die Sicherheit der menschlichen Seele notwendig.",
        "Man möchte nun «im Inneren des Men- schen» dem wahren Wesen des Menschen beikommen, aber man hat seinen Geist an der Außenwelt, «die nicht zu durchschauen ist», an den «Voraussetzungen des materiel- len Daseins» zu denken, zu empfinden gewöhnt."
      ],
      [
        "Was man sich da angewöhnt hat, es verzichtet auf das Durchschauen.",
        "Und wendet man diesen Geist, der auf das Durchschauen verzichtet, nach innen, so wird man im modernen schlech- ten Sinne Mystiker.",
        "Das bemerken heute leider nur allzuwenige: daß die Besten, die von unserer Naturerkenntnis sich abwenden und zu einem Streben nach Erkenntnis des menschlichen Inneren kommen, sich ihre Denk- und Empfindungsge- wohnheiten an dem Betrachten der Materie, «die undurch- schaubar ist», angeeignet haben, und nun in das mensch- liche Innere das, was sie sich als Denk- und Empfindungs- gewohnheiten am Betrachten der Außenwelt angeeignet haben, hineintragen."
      ],
      [
        "Wenn man aber den Blick, den man zuerst an der dunklen, finsteren «Materie» geschult hat, nach innen wendet, dann wird nebulose Mystik daraus, und die nebulose Mystik verriegelt das Tor zu dem: Er- kenne dich selbst!",
        "Das ist es, worauf mit starker Betonung alles hinweisen möchte, was innerhalb dieser Freien Hochschule für Gei- steswissenschaft gewirkt wird."
      ],
      [
        "Vermieden muß werden der Weg nebuloser Mystik ebenso wie der Weg, der einzig und allein in äußere naturwissenschaftliche Notwendigkeit und damit in Vernichtung der Freiheitserkenntnis hinein- führt.",
        "Vermeiden können wir diese Wege nur, wenn wir wirkliche Geisteswissenschaft suchen, nicht jene Geistes- wissenschaft, die nicht haltmachen darf vor dem mensch- lichen Inneren, welche dann, nachdem sie haltgemacht hat, den Weg doch weiter fortsetzt, indem sie mystische Nebel in dieses menschliche Innere hineinstrahlt."
      ],
      [
        "Nicht darf dieses die hier gemeinte Geisteswissenschaft tun!",
        "Mit jener Schu- lung, die gewonnen worden ist in heller, klarer, lichtvoller Erkenntnis an den äußeren Tatsachen, muß mystikfrei, aber geisteswissenschaftlich hineingeleuchtet werden kön- nen in das menschliche Innere."
      ],
      [
        "Das: Erkenne dich selbst! - darf nicht in mystischem Leben, dunkel, es muß in heller, lichter Klarheit erfaßt werden.",
        "Dann wird sich zusammen- schließen das, was dem Menschen ersprießt aus der Innen- erkenntnis, aus der Erfüllung des Wortes: Erkenne dich selbst! und was ihm ersprießt aus dem sich zur äuße- ren Natur Erkennendverhalten unter dem Wahrworte: Mensch, werde ein freies Wesen!"
      ],
      [
        "Wie zwei Säulen, die ideell im Geiste dastehen, wenn man diesen Bau betritt, möchten angesehen werden diese zwei Wahrworte: die Säule wahrhaftiger, lichtvoller menschlicher Selbsterkenntnis und die Säule der mensch- lichen Freiheit.",
        "Die erste ist geeignet, an dasjenige den Menschen zu mahnen, was ihm Sicherheit und Halt, künst- lerische Betätigung und religiöse Befriedigung gewähren kann."
      ],
      [
        "Die andere ist geeignet, ihn mit Kraft auszustatten, mitzuwirken bei den drängenden sozialen Fragen der Ge- genwart und der nächsten Zukunft.",
        "Von alledem, was hier in der Befruchtung der einzelnen Fachwissenschaften ange- strebt wird, wie sich insbesondere in den nächsten Tagen zeigen soll, möchte der weltgeschichtliche Moment erfaßt 18 sein, so gut er eben in aller Bescheidenheit erfaßt wer- den kann, der uns ebenso an das Ufer einer unbestimmten Zukunft stellt, wie der Grieche an das Ufer einer er- füllten, überwältigend wirkenden Vergangenheit gestellt war."
      ],
      [
        "Dazu aber müssen wir kommen, daß wir das lichtvolle Erfassen des menschlichen Inneren in dem Wissen selber fühlen, daß wir das Wissen nicht mehr bloß hinschleppen am äußeren Beobachten und am äußeren Experimente, sondern daß wir es frei erheben und, indem wir es durch- kraften mit dem inneren Wesen des Menschen, uns mit diesem Wissen hineinversetzen in das Leben der Freiheit, in das uns die bloße naturwissenschaftliche Betrachtung niemals hineinversetzen kann.",
        "Naturwissenschaftlich ist es ehrlich, die Freiheit zu leugnen, menschlich ist es, gegen diese Leugnung zu protestieren und in diesem Protest den Ausgangspunkt einer freien, aus dem menschlichen Inneren ihren Organen nach geborenen Geisteswissenschaft zu sehen."
      ],
      [
        "Dieser Geisteswissenschaft gegenüber braucht man, weil sie eindringt nicht in das Tote, sondern in das Leben, nicht zu fürchten, daß sie wie die tote Verstandeswissenschaft ertötend wirken werde auf die Kunst.",
        "Sie wird aus dem, was sie aus dem Geiste herausholt, die Kunst befruchten können."
      ],
      [
        "Es wird dieses Erkennen selbst nach außen künst- lerisch wirken können, weil es in lichtvoller Klarheit hin- untertaucht in menschliche Tiefen.",
        "Es wird einlaufen aus dem wahren Erkennen in das Verehren desjenigen, was sich im menschlichen Inneren offenbaren kann."
      ],
      [
        "Und es wird eine solche, nur mehr die Form der Mystik festhal- tende Erkenntnis, die aber zum Lichte strebt, zu gleicher Zeit auslaufen lassen das menschliche Wissen in religiöse Verehrung des Höchsten, was durch die Welt hindurch lebt und webt.",
        "Neue künstlerische Kräfte, neue religiöse Ver- tiefungen werden aus einem solchen, das Innere des Men- schen erfassenden Wissen kommen können."
      ],
      [
        "Und das Leben, in das ein solches Wissen untertauchen darf, wird ein Leben in Freiheit sein.",
        "Es wird dem Menschen zunächst das Be- wußtsein der Freiheit sicherstellen.",
        "Der Mensch wird sich nicht zu verlieren brauchen an die äußere Naturnotwen- digkeit, an die er sich mit dem bloßen naturwissenschaft- lichen Bewußtsein verliert, weil diesem nur Notwendigkeit und nicht Freiheit vorliegt."
      ],
      [
        "Und frei wird der Künstler werden von dem bloßen Modell in der Nachahmung der äußeren Natur, die er doch niemals erreichen kann.",
        "Aus geistigen Höhen herun- ter wird er holen, was er der Materie einprägen will."
      ],
      [
        "Ein schwacher Anfang zu solchem Herunterholen von Formen, die dem freien Geiste sich offenbaren, die sich nicht knüp- fen an Nachahmung im Modell, soll sein, was aus den For- men und dem Bildnerischen und dem sonstigen Künstle- rischen dieses Baues spricht.",
        "Und frei von allem bloß Traditionellen, das an den Menschen als ein Äußeres, als ein Unfreies herantritt, soll das religiöse Erleben werden: frei ergreifend, was sich als das Göttliche im Inneren des Menschen selber enthüllt, frei im Inneren sich verbindend mit derjenigen Kraft, die sich ihrer wahren Wesenheit nach doch nur in Freiheit mit diesem menschlichen Inneren wahrhaftig verbinden will: der Christus-Kraft."
      ],
      [
        "Wissen nach den verschiedensten Gebieten hin nach dem äußeren Natürlichen, nach dem Inneren des Men- schen, nach dem beides umfassenden Einheitlichen -, das ist das neue Streben nach Erfüllung des Wortes: Erkenne dich selbst! - Dreifacher Schritt der Freiheit: Freiheit im inneren Erleben des Menschlichsten, Freiheit im Schaffen, 20 auch im künstlerischen Schaffen, Freiheit im religiösen Erleben, das ist das andere.",
        "Dazu soll führen die Befruchtung der einzelnen Wissen- schaften und menschlichen Lebenszweige und des ganzen sozialen Lebens, wovon in den nächsten Tagen hier ge- sprochen werden soll."
      ],
      [
        "Gezeigt werden soll, daß aus den einzelnen Wissenschaften heraus nicht nur - wie es eine moderne, in den Tod gehende Philosophie tun will ge- wisse Sätze gewonnen werden können, aus denen man dann eine abstrakte Weltanschauung zusammenzimmert, sondern daß durch Geistbeobachtung eine Weltanschauung über allem Sinnlichen gewonnen werden kann, und daß in die einzelnen Fachwissenschaften diese allgemeine, licht- voll erfaßte Weltanschauung hineinleuchten kann.",
        "Man hat auch verlangt, daß die Weltanschauung sich nähre aus dem, was ihr die einzelnen Wissenschaften und ihre Ergebnisse abgeben."
      ],
      [
        "Die Zeit ist gekommen, wo aus einer im Geiste erlebten Weltanschauung die Ergebnisse herunterstrahlen in die einzelnen Wissenschaften.",
        "Mag das die Welt heute noch wenig erkennen, das, was hier an die- sem Orte geschieht, das soll niemals aus einem anderen Ton als aus dem heraus kommen, der selber impulsiert ist auf der einen Seite von dem wahrhaftigen: Erkenne dich selbst! - auf der anderen Seite von dem: Mensch, werde ein freies Wesen! - Das ruft uns aber nicht nur die einsame Wissenschaftsbetrachtung im menschlichen Inneren zu."
      ],
      [
        "Das ruft uns zu unsere ganze katastrophale Zeit von heute.",
        "Und wenn wir zusammenfassen, was im Tiefsten ruht in den Zeitenrätseln und Zeitenfragen, so ist es das, was ich versuchte heute anzutönen.",
        "Von dem, was uns so aufgegeben ist von den Zeichen der Zeit wie von dem fühlenden Menschenwesen, das inner- halb dieser Zeit steht, darf man so sprechen zum Alter."
      ],
      [
        "Diese älteren Menschen haben es erfahren, was es heißt, in einer katastrophalen Zeit zu leben.",
        "Sie fühlen, wie ab- getaut sind die Ideale ihrer Jugend.",
        "Sie fühlen, wie ausge- flossen ist in ein Zivilisationschaos, was sie glaubten in ihrer Jugend hinauszutragen in die moderne abendlän- dische Zivilisation."
      ],
      [
        "Zu ihnen, die solches erfahren haben, darf so gesprochen werden, wie heute gesprochen worden ist.",
        "Denn es muß solches Wort die Seite im menschlichen Seelenleben finden, die da sagt: Wir müssen noch benützen des Lebens Rest, um die Menschheit hinzuweisen auf Stär- keres, als dasjenige war, was durch uns gewirkt hat."
      ],
      [
        "Und auch zur Jugend darf mit solchen Worten gespro- chen werden.",
        "Denn sie schaut noch in voller Kraft, was im Zusammensturz ist, was in der Katastrophe lebt.",
        "Sie kann fühlen, innehabend ihre volle Menschenkraft und volle Menschenbegeisterung, daß etwas Neues, etwas Kraftvolles geschehen muß."
      ],
      [
        "Und der rechte Alte von heute wird suchen das Wort, das zünden kann in der Jugend, auf daß andere Zeiten sehen die Seelen, die aus den Augen der heutigen Jugend in die Welt blicken, als sehen müssen die Seelen, die durch heute alte Augen in die Welt blicken.",
        "Und so darf man wohl zu jedem Lebensalter sprechen."
      ],
      [
        "So darf man sprechen zu denen, die man in einer gewissen Sprache die «alten Häuser» aller Sorten nennt, so darf man sprechen zu den jungen Kommilitonen.",
        "Denn so darf man sprechen nicht nur aus den Zeitenaufgaben heraus, sondern aus den größten Aufgaben des menschlichen We- sens selbst."
      ],
      [
        "Und wir leben in einer Zeit, wo des Menschen größte Lebensfragen Zeitaufgaben geworden sind.",
        "Wir leben in einer Zeit, in der wir hineinschauen können in der Menschen tiefstes Innere.",
        "Und wir werden da geschrieben sehen die Aufforderung zu handeln, zu handeln in einer Richtung, die wir zugleich angegeben finden, wenn wir 22 hinschauen auf die äußeren Zeichen der Zeit mit ihrer deutlichen Sprache."
      ],
      [
        "Von dem, was in dieser zweifachen Blickrichtung liegt, möchte in den nächsten Tagen gesprochen werden.",
        "Möchte das Gesprochene Aufmerksamkeit finden.",
        "Denn in der heutigen Zeit den Menschen verstehen, heißt, ein Wichtig- stes im Menschenleben selber empfinden und fühlen."
      ],
      [
        "Der allein stellt sich heute recht und gerecht in das menschliche Wirken der Zeit hinein, der sich zu sagen versteht: in den Zeichen der Zeit liegt die Aufforderung ausgesprochen, ins tiefste menschliche Innere erkennend, geist-erkennend hin- einzuschauen.",
        "Und was der Mensch nur in seinem Inneren heute ergründen kann, ist zu gleicher Zeit das, was zu erkennen, zu fühlen, zu wollen, zu vollbringen uns auf- fordern die deutlich sprechenden Zeichen der Zeit."
      ],
      [
        "Auf die Eröffnungsrede Rudolf Steiners folgte ein Vortrag Albert Steffens über «Das Werden des Kunstwerks».",
        "Darauf sprach Frau Marie Steiner die von Rudolf Steiner schon für die Eröffnungsfeier des Ersten Hochschulkurses umgestalteten Worte des Hilarius aus: «Der Hüter der Schwelle»: In jenes Geistes Namen, der den Seelen In unsrem Strebensorte sich verkündet, Erscheine ich in diesem Augenblicke Vor Menschen, die von jetzt an hören wollen Das Wort, das hier den Seelen ernst erklingt."
      ],
      [
        "Nicht frühern Zeiten konnten jene Mächte, Die unsres Erdenwerdens Ziele lenken, In vollbewußter Art sich offenbaren.",
        "Denn wie im Kinderleibe erst allmählich Die Kräfte reifen müssen und erstarken, Die zu des Wissens Trägern sind bestimmt, So mußte sich als Ganzes auch entfalten Das Menschentum in seinem Erdenlauf."
      ],
      [
        "In Dumpfheit lebten erst die Seelentriebe, Die später würdig sich erweisen sollten, Aus hohen Welten Geisteslicht zu schauen.",
        "Doch wurden als der Menschen weise Führer Im Erdbeginn dem Geist ergebne Seelen Von höhren Daseinsmächten auserwählt."
      ],
      [
        "Sie pflegten in des Wissens Strebeorten Die Geisteskräfte, die Erkenntnisstrahlen In Seelen sandten, die nur dumpf bewußt Von ihrem Schauen sich durchdringen konnten.",
        "Erst später konnten aus der Menschen Reihen Die Geistesforscher sich die Schüler holen, Die durch das willensstarke Prüfungsleben Sich reif erwiesen, in Bewußtheits Helle Zum Geisteswissen zielvoll hinzustreben."
      ],
      [
        "Und als der ersten Führer Schüler später Das edle Gut in Würde pflegen konnten, Verschwand die unbewußte Führerschaft, Daß freie Seelen wissend streben durften.",
        "Und freie Seelen wählten sich dann Menschen, Die ihnen folgen durften in der Pflege Des Geistesschatzes; und so ging es weiter Von einem Menschenalter hin zum ändern."
      ],
      [
        "Es sind bis jetzt ja alle Wissensstätten, Die dies in Wahrheit sind, gerecht entsprungen Der höchsten, die in Geistessphären steht.",
        "In ernstem Suchen streben wir allhier Nach wahrem Geistes-Menschenerbe hin."
      ],
      [
        "Wir werden niemals von Erkenntnis sprechen, Die nicht des Geistes eignes Siegel trägt, Allein vom Lichte aus den Geisteswelten, Das schauend Menschen sich erschließen kann, Die sich ihm strebend anvertrauen wollen, Um ihrer Seele Tiefen zu ergründen.",
        "Zu diesem Lichte würdig hinzustreben, Das weiset uns der Zeitenwende Ernst Und ihre Not; die Zeichen sind fürwahr Bedeutungsschwer, die sich im Weltenplane Jetzt Geistesaugen deutlich offenbaren."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "PHILOSOPHIE Erster Vortrag, Dornach, 4. April 1921",
    "paragraphs": [
      "Die Vorträge dieser Woche sollen so eingerichtet sein, daß jeder Tag einem anderen Fache gewidmet ist, so daß er- scheinen kann, was als Befruchtung der einzelnen Fach- wissenschaften und Zweige des praktischen Lebens von der Geisteswissenschaft bewirkt werden soll. Heute soll mit dem wissenschaftlichen Fach begonnen werden, das in einer gewissen Beziehung der Geisteswissenschaft, wie sie hier gemeint ist, selber am nächsten steht: mit dem Fache der Philosophie.",
      "Was ich hier selbst werde zu sagen haben, soll eine Art Einleitung sein zu den Fragen, die im Laufe des heutigen Tages behandelt werden sollen. Ich möchte dabei von einem der interessantesten und sogar bedeutsamsten Phänomene der neueren philosophi- schen Entwickelung ausgehen.",
      "Es ist ja durchaus so, daß nicht immer diejenigen Erscheinungen die bedeutsamsten und interessantesten sind, die bald darauf in den gebräuch- lichen Geschichtswerken verzeichnet werden. Und so möch- te ich denn von einer Erscheinung ausgehen, die noch sehr wenig geschichtlich zum Ausdrucke gekommen ist, von der ganzen Bedeutung eines 1888 erschienenen philosophischen Werkes, das herrührt von Ludwig Haller, einem Regie- rungsrat und Staatsanwalt, und das den Titel trägt «Alles in Allen: Metalogik, Metaphysik, Metapsychik».",
      "Ich darf von diesem Phänomen im philosophischen Leben um so mehr ausgehen, als derjenige, der meine eigene schrift- stellerische Laufbahn verfolgt, sehen kann, daß ich selbst von diesem Phänomen ganz unbeeinflußt geblieben bin, 26 weil dasjenige, was meine Stellung zur Philosophie aus- macht, durchaus schon enthalten ist in meinen Schriften, die vor dieser «Metalogik, Metaphysik, Metapsychik» er- schienen sind, und das, was ich später gesagt habe, nur eine sachgemäße und konsequente Ausgestaltung des in meinen ersten Schriften Enthaltenen ist. Vor allen Dingen tritt uns in dem Staatsanwalt und Regierungsrat Ludwig Haller, der sonst nichts geschrieben hat als das genannte Werk, ein Mensch entgegen, bei dem das, was man Philosophie nennt, nicht nur Fachwissen- schaft ist - obwohl er in einer gewissen Beziehung durchaus befähigt ist, sich mit dieser Fachwissenschaft auseinander- zusetzen , sondern bei dem das, was er vorbringt, aus unmittelbar persönlichem philosophischem Erleben heraus kommt.",
      "Wir haben es mit einer Persönlichkeit zu tun, wel- cher das philosophische Streben innerlichstes persönliches Erleben geworden ist. Und wenn wir gleich eingehen auf das Bedeutsamste bei Ludwig Haller, dann müssen wir verzeichnen, daß er eigentlich mit der ganzen Art des philosophischen Denkens der neueren Zeit auf dem Kriegs- fuße steht.",
      "Er hat sich offenbar viel umgetan in allerlei Philosophie und auch in denjenigen Literaturwerken, in denen «Lebensphilosophie» sprudelt. Er hat sich einge- wöhnt in das philosophische Denken seiner Zeit und er hat gefunden es ist das, wie gesagt, seine Meinung , daß man sich mit diesem philosophischen Denken eigentlich in einer Art von unwirklichem Kreise dreht, daß man mit diesem philosophischen Denken niemals in die Lage kommt, in die Wirklichkeit selber unterzutauchen.",
      "Ludwig Haller möchte mit seinem Philosophieren in die geistige Wirklichkeit eindringen, die er, indem er offenbar seiner Erziehung nach herausgewachsen ist aus mehr reli- giösen Vorstellungen, «das Göttliche» oder auch wohl «Gott» nennt. In diesem «Göttlichen» oder in «Gott» sucht er den Quell alles dessen, was als die eigentliche Wesenheit auch in der menschlichen Seele leben und dessen sich die Menschenseele auch bewußt werden müsse.",
      "Aber er kommt eben darauf, daß diese Seele, indem sie die zu seiner Zeit gebräuchlichen Begriffsgewebe verarbeitet, in dieses Zen- trum ihres Wesens, wo sie eins ist mit dem Göttlich-Geisti- gen der Welt, nicht eindringen könne. Da dieses Gedankenweben der Philosophen Ende der achtziger Jahre, in denen das genannte Werk erschien, ja noch vielfach ganz und gar beeinflußt war von Kant und also Kantische Gedanken in diesem Gedankenweben leb- ten, so fühlte sich Ludwig Haller vor allen Dingen auch veranlaßt, sich mit dem Kantianismus und alledem, was von dem Kantianismus herrührt, zu beschäftigen.",
      "Aber gerade in all den Gedanken, in die nur irgendwie Kanti- sches hineinfließt, sah er das Unwirkliche, dasjenige, was niemals in die Wirklichkeit der Welt untertauchen kann. Und er war eigentlich unglücklich darüber, daß er, weil er eben philosophisch in seiner Zeit sprechen wollte, sich mit diesem vom Kantianismus durch und durch infizierten Denken beschäftigen müsse, daß er immer wieder und wiederum darauf zurückkommen müsse, sich mit dem Kantianismus auseinanderzusetzen.",
      "Er fand recht scharfe Worte, um erstens den Kantianismus selbst zu charakteri- sieren, und dann auch für das ihm so unsympathische Sich- auseinandersetzen-Müssen mit dem Kantianismus. Ich möchte Ihnen zwei Proben aus diesem Beurteilen des Kantianismus hier mitteilen, damit Sie sehen, womit ein Mensch, für den Philosophie eine innerlichst persönliche Angelegenheit ist, in unseren Zeiten ringt.",
      "Einmal spricht da Ludwig Haller vom Kantianismus so, daß er über ihn sagt: der «pseudodialektische, halbwahre, 28 im Tiefsten unredliche Charakter dieser Misosophie, welche dem Arsenal des Lichtes die Waffen zu stehlen versucht, um sie im Dienste der Finsternis zu verwenden». Ein andermal wird er, ich möchte sagen, schriftstellerisch wütend darüber, daß er immer wieder und wiederum sich genötigt findet, weil er doch mit seinen Zeitgenossen sich auseinandersetzen muß, auf das Kantische Denken einzu- gehen, und er sagt: «Ich, der ich von Gott und seiner Herr- lichkeit reden könnte und möchte, sehe mich immer von Neuem dazu verdammt, von Kant und seiner Erbärmlich- keit zu reden ich eines Gecken Geck.» Ich wollte auf dieses Phänomen hinweisen, weil es ein Abdruck ist von den Kämpfen, die eine wirklich philoso- phisch angelegte Natur am Ende des 19.",
      "Jahrhunderts zu bestehen hatte. Man nimmt heute, was philosophisches Reden und Schreiben ist, durchaus auch so, daß man dar- aus möglichst eine Angelegenheit macht, die sozusagen ein Stück über den menschlichen Köpfen darüber schwebt, bei der man persönlich gar nicht dabei ist.",
      "Daher werden die inneren tragischen Phänomene des philosophischen Lebens in unserer Zeit viel zu wenig gewürdigt. Und ich glaube, daß dieses Phänomen, das zu dem Tragischesten in den inneren philosophischen Erlebnissen unseres Zeit- alters gehört, eigentlich in weiteren Kreisen recht wenig bekanntgeworden ist.",
      "Wer das Geistesleben dieser Zeit wirklich kennt, der weiß, wieviel von solchen Stimmungen in Menschen unse- res Zeitalters gelebt hat. Und eigentlich muß man auch, wenn man das Wesen philosophischen Denkens in unserer Zeit darlegen will, gerade von diesen Erscheinungen reden, die ja von den philosophischen Fachmännern nicht beachtet werden, die aber für das eigentliche menschliche Erleben um so wichtiger sind.",
      "Nun möchte ich, anknüpfend an dieses Phänomen, ein anderes, das im Grunde genommen auch nur ein sozusagen subjektiv persönliches philosophisches Erlebnis ist, charak- terisieren. Der bekannter als Ludwig Haller gewordene Philosoph Eduard von Hartmann hat sich mit Ludwig Haller auseinandergesetzt.",
      "In dieser Auseinandersetzung ist ein Punkt von ganz besonderer Bedeutung. Ludwig Haller, der sich viel zu tun macht, Sie sahen, er nennt sich wegen dieses Sich-viel-zu-tun-Machens «eines Gecken Geck», mit dem Sich-Hineinfinden in das kantisch infi- zierte Gedankenweben seiner Zeit, unseres Zeitalters - er verspürt nämlich, indem er so mit dem Denken von Be- griff zu Begriff geht, indem er sich dem philosophischen Denken überläßt, das sieht man ganz deutlich überall durchleuchten aus seinem Buche - er verspürt, daß die Begriffe, denen er nun folgt mit dem Denken, ein merk- würdiges Innenleben gewinnen.",
      "Es ist ihm so, als ob die Begriffe in seinem Gemüte anfingen ein selbständiges Leben zu führen. Das hebt er an den verschiedensten Stellen seiner «Metalogik, Metaphysik, Metapsychik» her- vor. Wenn wir psychologisch auf dieses interessante Phäno- men eingehen wollen, so können wir nicht anders als das Folgende sagen: Ludwig Haller versetzt sich mit aller Ge- walt in die besondere Natur des gegenwärtigen philoso- phischen Denkens.",
      "Aber sein inneres menschliches Erleben will eigentlich etwas anderes; zu diesem anderen kann er nicht kommen, weil in den achtziger Jahren ja auch nicht die Spuren einer wirklich modernen Geisteswissenschaft vorhanden waren. Es fehlt in seinem Inneren das, was dieses menschliche Innere mit wirklicher Geisteswissen- schaft erfüllen könnte.",
      "Aber es lebt, möchte ich sagen, auf eine merkwürdig instinktiv unbewußte Art darin. Er weiß 30 nichts davon, aber er merkt es an diesem sonderbaren Phä- nomen, daß die Begriffswelt bei ihm lebendig wird, ein selbständiges Leben führt.",
      "Wer im Sinne der hier vertretenen Geisteswissenschaft forschen kann, der kennt dieses selbständige Leben der Begriffe sehr gut. Aber er kann es auch beherrschen. Er kann es in dem Sinne beherrschen, wie man den Übergang von einem mathematischen Begriff zu dem anderen mathe- matischen Begriff im gewöhnlichen Mathematisieren be- herrschen kann.",
      "Aber dieses Beherrschen, das muß durch innerliche Übung errungen werden. Es ist ganz selbstver- ständlich, daß man in ein dem gewöhnlichen Bewußtsein ganz fernes Leben hineinkommt, wenn man so plötzlich merkt - was sonst nur die Speisen in unserem Organismus tun, daß sie ohne unser Zutun ihr eigenes Leben in der Verdauung führen -, daß die aufgenommenen Begriffe anfangen, innerlich ein eigenes Leben zu führen.",
      "Es ist nicht unbegreiflich, sondern sehr, sehr begreiflich, daß nun ein Philosoph wie Eduard von Hartmann, der ja geistvoll war, der auf manchen Gebieten auch durchaus Eindring- liches geleistet hat, der aber durchaus herausgewachsen ist aus dem philosophischen Denken seines Zeitalters, mit diesem Erlebnis Ludwig Hallers nichts Besonderes anfan- gen konnte. Und indem Eduard von Hartmann seine Kritik über Ludwig Haller schreibt, merkt man, daß ihm auf der einen Seite ganz schwül wird.",
      "Was soll denn das werden - so sagt sich der richtig zeitgemäße Philosoph -, wenn da die Begriffe, denen ich mich hingebe, plötzlich anfangen in meinem Inneren wie Kobolde zu tanzen, sich gegenseitig zu umhalsen oder dergleichen? Das ist ja etwas Fürchterliches, dem kann man sich nicht aussetzen! - Und er gibt demgemäß auch, als richtiger zeitgemäßer Philo- soph, diese Kritik in einer recht bedeutsamen Weise ab, indem er sagt, er habe niemals etwas bemerkt von diesem neckischen, koboldartigen Treiben der selbständig lebendig gewordenen Begriffe.",
      "Man kann Eduard von Hartmann durchaus glauben, daß er diese Schwüle im Inneren beim Lesen der «Metalo- gik, Metaphysik, Metapsychik» Ludwig Hallers empfand. Er hat, wie seine Kritik zeigt, deshalb doch nicht aufge- hört, das ganze Buch durchzulesen, hat es sogar in einem gewissen Sinne sehr bedeutend gefunden.",
      "Ich glaube, viele andere, die sich in dem Zeitalter, das auf 1888 gefolgt ist, fachmännisch mit Philosophie beschäftigt haben, sind wohl kaum über die ersten Seiten dieses Buches hinausgekom- men, wenn sie überhaupt auch nur das Titelblatt kennen- gelernt haben! Worauf ich Sie da hinweise, ist eine durchaus bedeut- same Erscheinung.",
      "Und wir verstehen sie nur, wenn wir die philosophische Entwickelung des Abendlandes so ver- folgen, wie ich sie zu verfolgen versuchte in meinem Buche «Die Rätsel der Philosophie». Wenn man auf das eingeht, was ich dort genauer und in allen Einzelheiten an der Hand der Philosophiegeschichte ausgeführt habe und was ich hier nur andeuten kann, so sieht man, daß im Zeitalter des griechischen Philosophierens die ganze menschliche Seelenverfassung eine andere war, als sie später geworden ist und als sie namentlich in unserer Zeit ist.",
      "Wir sehen, wie im griechischen Philosophieren durchaus das, was wir Denken nennen, was wir Vorstellen nennen, in einer ähn- lichen Weise mit den Bedingungen der Außenwelt, insofern sie sich dem Menschen darstellt, verknüpft ist, wie für uns nurmehr die sinnlichen Wahrnehmungsqualitäten. Indem wir wahrnehmen, schreiben wir, wenigstens im naiven Be- wußtsein, dem, was wir wahrnehmen, die sinnlichen Qua- litäten zu.",
      "Gewiß, die erkenntnistheoretischen Erörterun- gen seit Locke und anderen denken anders, aber sie brau- dien uns in diesem Augenblicke weniger zu interessieren; ich will für die herangezogene Tatsache nur auf das naive Bewußtsein verweisen. Man schreibt in diesem naiven Bewußtsein den Dingen die Sinnesqualitäten rot, blau, weiß, warm, kalt, lau, süß, bitter und so weiter zu, und man ist sich heute klar darüber, daß dasjenige, was man an den Sinnesobjekten denkt und vorstellt, im Bewußtwerden abgesondert ist von dem Objektiven, daß es subjektiv erlebt wird.",
      "Der Grieche schrieb aber sein Denken, seine Vorstellungen dem Objekte noch so zu, wie wir rot, blau, süß, bitter und so weiter dem Objekte zuschreiben; er hatte, was er im Erkennen erlebte, zu einem noch größeren Teile sozusagen in der Wahrnehmung drinnen, als wir das haben. Er hatte durchaus das Bewußtsein, daß er mit dem Rot, Grün und so weiter zugleich den begrifflichen Inhalt wahrnahm.",
      "Und was, ich möchte sagen, in der am meisten logischen Weise im griechischen Denken zutage trat, das war bis in das 13., 14., 15. Jahrhundert herauf, bis in die Galilei- Kopernikus-Zeit, im Grunde genommen eine Eigentüm- lichkeit des allgemeinen forschenden Bewußtseins.",
      "Wer sich vertieft in dasjenige, was zutage getreten ist in wissen- schaftlichen Leistungen, die ja für diese Zeit durchaus noch eins waren mit dem philosophischen Forschen, wer sich vertieft in die entsprechende Literatur, soweit sie vorhan- den ist, wird sagen, daß diese älteren Forscher und Denker durchaus, indem sie von den Dingen reden, an den Dingen dasjenige noch als objektiv schildern, was der heutige For- scher durchaus von den Dingen abgesondert denkt und dem Subjekte zuschreibt. Man kann verfolgen, und dieses Verfolgen ist außer- ordentlich interessant, wie im Zeitalter der Scholastik das 33 philosophische Leben die Richtung nimmt, sich klarzuwer- den, wie eigentlich das, was wir das Denken in Begriffen nennen, noch verbunden gedacht werden darf mit dem Objektiven.",
      "Vor dem scholastischen Zeitalter war die Ver- bindung desjenigen, was als Vorstellung und Begriff an den Dingen erlebt wird, mit diesen Dingen selbstverständ- lich. Eine Frage, ein Rätsel wurde diese Verbindung erst, als sich für das menschliche Erleben das Begriffliche, das Vorstellungsmäßige von dem löste, was man die objektive Wahrnehmung nennt.",
      "Und aus diesem philosophischen Er- leben heraus ist dann der Scholastik jenes Problem entstan- den, das man heute viel gründlicher studieren sollte, als man es studiert, das Problem des «Realismus» und des «Nomi- nalismus». Heute verbindet man sogar ganz andere Vor- stellungen mit diesen Worten «Realismus» und «Nomina- lismus», als es im Zeitalter der Scholastik der Fall war.",
      "Im Zeitalter der Scholastik war ein Realist, wie zum Beispiel Thomas von Aquino, derjenige, der den Begriffen, den Vorstellungen eine objektive Realität beilegte, so daß er sagte: Die Begriffe, die Vorstellungen haben etwas, was in seinem Inhalte objektiv ist, was nicht bloß dem Subjekte angehört, was nicht bloß gedacht ist. Ein Nominalist war derjenige, der die Realität nur in dem suchte, was außer- halb des Begrifflichen liegt, der in den Begriffen nur etwas sah, wodurch der Mensch zusammenfaßt, was ihm als Wahrnehmung gegeben ist, so daß die Begriffe für den Nominalisten eben bloße Namen waren.",
      "Solch ein Problem taucht immer dann auf in der Mensch- heitsentwickelung, wenn innerlich etwas durchgemacht wird. Der Mensch hatte eben dieses innerlich durchzu- machen im Mittelalter, daß er sich immer verwandter und verwandter machte in seinem eigenen Inneren mit dem begrifflichen Leben, daß er das, was Außenwelt genannt 34 wird, nur in dem Wahrnehmbaren sah.",
      "Daher wurde es für ihn eine Frage: Wie ist man berechtigt, dasjenige, was man im Grunde genommen innerlich nur als Name hat, was man nur so erfaßt, daß man die äußerlichen Wahrneh- mungen damit zusammenordnet, auf diese äußerlichen Wahrnehmungen irgendwie zu beziehen? Ein bedeutsamer Skeptizismus geht aus dem Nominalismus hervor.",
      "Und im Grunde genommen ist das, was dann in der Kantischen Philosophie aufgetreten ist, nichts anderes als, ich möchte sagen, die letzte Konsequenz dieses Scholasti- kerproblems. Nur kam Kant auf eine eigentümliche Weise gerade zu seiner Formulierung des Scholastikerproblems: In dem Zeitalter, in dem Kant als Jüngling seine philoso- phischen Studien gemacht hat, war der etwas verdünnte Leibnizianismus innerhalb der Kreise herrschend, in denen eben Kant seine Studien machte.",
      "Der Leibnizianismus, der in seiner Art etwas Großes ist, wenn auch etwas außer- ordentlich Abstraktes, der noch durchaus einen Zusammen- hang mit Wirklichkeitsgeist hat, war im Wolffianismus, der für Kant das Jugendstadium bildete, philosophisch sublimiert, verdünnt. Man hatte in dieser Zeit schon durch- aus zu tun mit den Ansprüchen der mathematisierenden Wissenschaft, mit den Ansprüchen der Wissenschaft, die sich eben zusammensetzt aus den Ergebnissen der Außen- beobachtung der Welt.",
      "Aber aus der alten Gewohnheit heraus, daß der Mensch doch etwas mitzusprechen habe, wenn über die Welt etwas ausgemacht wird, hatte man neben dieser empirischen Wissenschaft, neben dieser Er- fahrungswissenschaft, die breite Vernunftlehre statuiert. Man hatte statuiert: über alles Vergängliche können durch Erfahrung, durch Empirie, Ungewisse Urteile gewonnen werden; aber diese Urteile sind eben durchaus nur auf das Vergängliche gerichtet und sind ungewiß.",
      "Man kann nicht 35 wissen, ob sich das, was man über irgendeine Tatsache der vergänglichen Welt durch Beobachtung und Verstan- deserkenntnis erkennt, auch wirklich, wie notwendig für alle Zeiten, so verhalten muß. Man kann nicht einmal wissen, daß die Sonne jeden Morgen aufgehen muß, denn man hat nur den einen Erfahrungsbeweis, daß sie bis jetzt an jedem Morgen aufgegangen ist.",
      "Daraus kann man schließen, daß sie auch zukünftig aufgehen wird; aber es ist eben nur ein Erfahrungsschluß. Über diese Erfahrungs- wissenschaft hinaus suchte nun der Wolffianismus, suchte auch Kant in seiner Jugend, ganz im Einklang mit dem Wolffianismus, eine Vernunftwissenschaft.",
      "Es ist charak- teristisch, daß ein Buch von Wolff so heißt: «Vernünftige Gedanken von Gott, der Welt und der Seele des Menschen, auch allen Dingen überhaupt.» Also es handelte sich darum, auf der einen Seite ein Erfahrungswissen zu gewinnen über den Umkreis der Welt, soweit er der Erfahrung zugänglich ist, und auf der anderen Seite ein über alles sich erstreckendes Vernunft- wissen, das gewissermaßen aus der Vernunft allein heraus gewonnen werden soll. Und man begründete neben der, sagen wir, geoffenbarten Theologie eine vernünftige, eine rationelle Theologie, neben der Erfahrungs-Seelenkunde eine rationelle Psychologie, neben der Weltkunde, die man durch Erfahrung gewinnt, eine rationelle Geologie und so weiter.",
      "Gewohnheitsmäßig lag diesem Suchen nach einer besonderen Vernunftwissenschaft zugrunde, daß man sich sagte: In einer äußeren Welt gibt es keine Gewißheit für das wissenschaftliche Forschen. Will man aber eine solche Gewißheit haben, kann man sie nur dadurch gewinnen, daß man sie aus der Vernunft selber heraus gewinnt.",
      "Allerdings liegt dem ganzen Forschen des Wolffianismus noch das zugrunde, daß zuerst auf irgendeine transzendete 36 Weise in diese Vernunft, aus der heraus der Mensch dann seine «Vernunftwahrheiten» gewinnt, eine Wirklichkeit hineingelegt worden ist. Zweierlei trat bei Kant auf, und wer ganz unbefangen Kant studiert, wird scharf hingewiesen auf das, was bei ihm nach zwei Seiten hin auftaucht: Auf der einen Seite hatte er sich eingewöhnt in das Suchen nach «gewissen Urteilen».",
      "Er hatte sich zum Beispiel gesagt: In der Mathe- matik haben wir solche Urteile, die ganz notwendig immer gelten, die also nicht aus der Erfahrung stammen können, weil die Erfahrung keine solchen Urteile gibt. Wir haben auch in einigen Partien des naturwissenschaftlichen Den- kens solche Urteile, die für immer gelten, die also wirklich nur aus dem Menschen selbst heraus gewonnen werden können.",
      "Gewißheit muß es geben in der Philosophie. - Das war die eine Seite dessen, was Kant wollte. Und wer nicht ins Auge faßt, wie Kant fest auf dem Boden stand: Gewißheit muß es geben - auch im Sinne der Wolffischen Philosophie -, der versteht eben Kant nicht, weil er sich nicht einlassen kann auf die Erkenntnis dieses Pochens Kants auf die Gewißheit gewisser Urteile.",
      "Aber an dem Wolffianismus, seinem Inhalte nach, war Kant irre geworden durch das Studium von Hume, dem englischen Philosophen, der ein bloßer Erfahrungsphilo- soph sein wollte. Und er sagte sich, eben unter dem Ein- fluß Humes: So etwas, wie eine Wirklichkeit herausspin- nen aus der Vernunft, das gibt es ja nicht; es gibt eigent- lich nur eine Erfahrung. - Das war die zweite Seite.",
      "Gewißheit muß es geben auf der einen Seite; aber alles, was in der Erfahrung auftritt, was die einzige Grundlage für wirkliches Erkennen ist, das liefert keine Gewißheit. Wie kommt man aus diesem Dilemma heraus?",
      "Und das ganz zwangsmäßige Suchen, aus diesem Dilemma heraus- 37 zukommen, das ist im Grunde genommen der Haupt- impuls des Kantischen Denkens. Ich habe das ausführlich dargestellt in meiner Schrift «Wahrheit und Wissenschaft» und habe es noch durchleuchten lassen in meiner «Philo- sophie der Freiheit», wie eigentlich Kants Suchen nicht darauf hinauslief, irgend etwas wesentlich zu erkennen, sondern zu fragen: Wie kommt man zu einer absoluten Gewißheit?",
      "Das Kantsche Problem ist kein Wahrheitsproblem, ist kein Erkenntnisproblem, sondern ein Gewißheitsproblem. Und wenn man es nicht als ein Gewißheitsproblem faßt, kann man es eigentlich nicht verstehen. Die Lösung wird von Kant dadurch gesucht, daß er sagt: Zum Herausspin- nen von Wirklichkeitsurteilen aus der Vernunft ist die Menschenseele allerdings nicht geeignet, aber diese Urteile kommen doch zustande; sie werden, wie man zum Beispiel in der Mathematik sieht, angewendet auf die äußere Er- fahrung.",
      "Wir schauen solche Figuren (es wird gezeichnet) nicht bloß an, sondern wir schauen sie mathematisch an und sagen: Es sind zwei Dreiecke oder, anders gezeichnet, es ist ein Sechseck. Wir vermischen das, was wir innerlich aus der Vernunft herausspinnen, mit dem, was uns durch die äußere Erfahrung kommt.",
      "Wir stülpen das innerlich a priori Erkannte über das a posteriori, von außen Er- fahrene hinüber. So kam Kant dazu, zu sagen: Wahrheitserkenntnis kann allerdings aus der Vernunft nicht gewonnen werden. Aber die menschliche Vernunft wird auf die Erfahrung ange- wendet.",
      "Sie stülpt ihr Urteil über die äußere Erfahrung hinüber. Sie macht selbst ihr Urteil über die äußere Er- fahrung. Weil Kant sagte: Gewißheit muß es geben in der Philosophie, Gewißheit muß man finden können, aber man findet sie nicht, wenn man sie in Wolffischer Weise sucht, wenn man glaubt, man könne eine Wirklichkeit in der Vernunft gewinnen und daneben die Erfahrung neben- herlaufen lassen , weil Kant das nicht zusammenbringen konnte, so sagte er: Der Mensch spinnt eben aus seiner Vernunft das heraus, was die Erfahrung dann in sich auf- nimmt; der Mensch macht selber die Erkenntnis; die Dinge der Erfahrung sind deshalb gewiß und insofern gewiß, als wir sie aus unserem Geiste heraus gewiß machen.",
      "Sie sehen, eigentlich ist damit das Wesen der Erkenntnis entthront. Eigentlich ist damit die Erkenntnis beseitigt. Und sie ist auf scharfsinnige Weise beseitigt, so scharfsin- nig, daß die Kantianer sich bis heute an diese Scharfsinnig- keit halten und nicht merken, was eigentlich darinnensteckt.",
      "Kommt dann ein Mensch wie Ludwig Haller, der da fühlt, wie eigentlich das Kantische Denken ganz abkam von der Wirklichkeit, wie es im Unwirklichen nach der Gewißheit schnappt, dann findet er eben Worte, wie ich sie Ihnen mitgeteilt habe. Er findet, daß da menschlicher Scharfsinn angewendet wird auf ein unmögliches Problem, auf ein Problem, das dem Menschen die Erkenntnis nicht aufhellt, sondern mit Nebel umhüllt.",
      "Deshalb sagt Ludwig Haller, wie er es empfindet: Diese Misosophie versucht zu stehlen ihre Waffen aus dem Arsenal des Lichtes und verwendet sie im Dienste der Finsternis. Aber auf der anderen Seite muß man auch einsehen, wie diese ganze Entwickelung der neueren Zeit im Grunde genommen notwendig war.",
      "Was sich heraufentwickelt hat an menschlichem Denken und menschlichem Forschen seit der Griechenzeit, war nicht eine Entwickelungslinie, die man nur so verfolgen kann, wie ich es jetzt eben getan habe, sondern die man auch nach einer anderen Seite ver- folgen kann. Auch darauf habe ich in meinen «Rätseln der Philosophie» hingedeutet.",
      "Wir stehen heute vor einer 39 Naturerkenntnis, welche das Naturphänomen rein aufzu- fassen versucht. Man kann allerdings sagen: Gerade derjenigen Natur- erkenntnis, die heute immerdar besonders damit prunkt, daß sie das Naturphänomen rein auffaßt, gelingt es kaum, das Naturphänomen rein aufzufassen, das heißt, es nicht mehr, gar nicht mehr zu durchdringen mit dem Gedanken- gewebe desjenigen, was nur im Begriffe, innerlich subjek- tiv, gemacht ist. - Es werden ja noch immer über den äußeren Phänomenverlauf allerlei Hypothesen aufgestellt, nicht nur berechtigte, sondern unberechtigte.",
      "Aber ein Mensch hat doch in der neueren Zeit scharf betont, und zwar verhältnismäßig früh, daß diese neuere Zeit in bezug auf das Betrachten der äußeren natürlichen Vorgänge nach dem reinen Phänomen, nach der reinen Phänomenologie hinstreben muß. Und das war Kants Antipode Goethe.",
      "Er hat verlangt, daß die Phänomene, die Erscheinungen rein sich selbst aussprechen. Er hat scharf betont, daß dasjenige, was sich in der Verstandesentwicke- lung abspielt, durchaus ferne bleiben muß demjenigen, was man als Beschreibung der Phänomene und des phänomena- len Verlaufs selber hinstellt.",
      "Und in allerschärfster, in bewunderungswürdiger Weise fordert Goethe wiederholt diesen reinen Phänomenalismus. Aber je mehr man diesem reinen Phänomenalismus zustrebt, desto mehr muß man nach einer besonderen Eigen- tümlichkeit der Begriffswelt streben.",
      "Und diese Eigentüm- lichkeit der Begriffswelt ist auch in hohem Grade erreicht. Diese Eigentümlichkeit ist eine durchaus berechtigte für ein gewisses Zeitalter der menschlichen Entwickelung. Wer sich nicht allein darauf beschränkt, die Philosophie zu stu- dieren seit dem Zeitalter des Cartesius, sondern wer ein Organ dafür hat, auch einzugehen auf die guten Seiten 40 scholastischer Philosophie, mittelalterlicher Philosophie, und wer Aristoteles und Plato nicht durch die Brille der modernen Philosophie-Geschichtsschreiber sieht, sondern sie in ihrer ursprünglichen Gestalt vor seine Seele stellen kann, der weiß, daß die Art und Weise, wie die Begriffs-, die Vorstellungswelt in der menschlichen Seele lebt, heute eine ganz andere ist als im griechischen Altertum und selbst noch im scholastischen Mittelalter.",
      "Im scholastischen Mit- telalter fühlte noch die Seele, daß, indem sie den Begriff erlebte, in diesem Begriff etwas von Substantialität lag, so wie in dem Rot, in dem Blau, das man als Wahrnehmung hat, noch etwas von Substantialität liegt. In der neuesten Zeit erst ist der Begriff zum vollständigen Abbild gewor- den.",
      "In der neuesten Zeit erst ist der Begriff seines Inhaltes völlig entleert. In der neuesten Zeit erst ist in der Mensch- heitsentwickelung und in der Philosophie möglich gewor- den, was ich in meiner «Philosophie der Freiheit» das reine Denken genannt habe.",
      "Wenn man das Freiheitsproblem zu belauschen sucht, so wie ich es versuchte in meiner «Philosophie der Frei- heit», lernt man zu gleicher Zeit diesen neuzeitlichen Cha- rakter des Denkens kennen. Man lernt dasjenige Denken kennen, welches im Grunde genommen alles äußeren Er- fahrungsinhaltes entleert ist, heranerzogen ist zwar an diesem äußeren Erfahrungsinhalt, aber doch nur als sub- jektive Tatsache lebt.",
      "Von diesem reinen Denken kann man ebensogut sagen, und ich habe das in der Neuauflage meiner «Philosophie der Freiheit» deutlich durchmerken lassen, daß es im Be- reiche des Wollens vor sich geht. Aber es ist das Wollen zum Denken ummetamorphosiert, wie man sagen kann.",
      "Es ist das Ergebnis desjenigen Denkens, das alle äußere Erfahrung abgestreift hat. Dieses reine Denken ist nur mehr Bild, und ist ganz Bild. Und man muß, wenn man überhaupt zu einem philosophischen Verständnis in unse- rem Zeitalter kommen will, den Boden erreichen, auf dem man dieses reine Denken hat.",
      "Goethe hat gefühlt, was in diesem reinen Denken liegt. Die anderen können es ihm nur nachfühlen. Daher zitieren sie einen Goetheschen Ausspruch immer falsch, der etwa sagt, der gütige Gott habe ihn davor bewahrt, «über das Denken zu denken».",
      "So wie Goethe das meint, so ist es schon richtig. Goethe hat niemals «über das Denken ge- dacht», weil man allerdings mit dem Denken, in das man sich eingewöhnt hat, dieses reine Denken nicht erreichen kann.",
      "Man muß es als Bild anschauen. So daß man sagen kann: Das Denken selber, das man erkennen will, das reine Denken, wird zu einem Anschauen dieses reinen Denkens. Nicht dialektisch, aber anschaulich ist das reine Denken zu erreichen.",
      "Man kommt zu diesem Punkt philosophischer Entwickelung an dem Freiheitsproblem, weshalb die Frei- heit, wirkliche Freiheit, gar nicht möglich ist ohne die Errei- chung dieses reinen Denkens, das bloßes Bild ist. Solange eine Realität in uns unser Handeln motivieren würde, so lange kann unser Handeln nicht frei sein.",
      "Da- her ist kein instinktives, kein traditionelles Handeln, kein Handeln unter einem Gewohnten wirklich frei, sondern allein ein Handeln, welches den Bildern, die im reinen Denken weben, folgen kann. Sobald man einer Realität folgt, wird man gestoßen.",
      "Wenn man frei sein will, muß man in seinen Willen das Irreale aufnehmen. Wenn Sie sich irgendwie anstoßen, so fühlen Sie, daß der Gegenstand auf Sie eine Wirkung hat. Wenn Sie unter einem Instinkt, unter einem Triebe eine Handlung vollbringen, so müs- sen Sie fühlen, daß da etwas stößt, daß da keine Freiheit vorliegt.",
      "Wenn Sie aber vor einen Spiegel treten, das Bild im Spiegel sehen, so werden Sie sich klar sein darüber, daß das Spiegelbild Ihnen niemals eine Ohrfeige geben kann, daß das Spiegelbild Ihnen niemals einen Stoß geben kann. Das Bild kann nichts machen von sich aus.",
      "Der muß machen, der muß handeln, der diesem Bilde gegenüber- tritt. Da aber das Bild nichts macht, so wird die Hand- lung dann zu einer freien Handlung. So kann nur ein Denken, das nicht im Realen wurzelt, sondern das reines Bild ist, ein freies Handeln motivieren.",
      "Deshalb erlauscht man an dem Problem der Freiheit das Problem des moder- nen Denkens, des reinen Denkens. Aber man steht in die- sem Denken in einer Bilderwelt darinnen. Die moderne Philosophie, alles, was in dieser modernen Philosophie durch Kant und die Kantianer lebt, das kommt instinktiv, obwohl es zumeist dieses reine Denken nicht begreift, an dieses reine Denken heran.",
      "Man muß eben, wenn man in der modernen Zeit anfängt zu denken und sein Denken schult an der Naturwissenschaft, die für sich alle Autorität in Anspruch nimmt und die nicht wirkliche Naturwissenschaft, wirkliche Realitätswissenschaft wäre, wenn sie etwas anderes in uns hereinstopfte als nur Bilder, man muß, wenn man sein Denken in dieser Richtung bewegt, sich zunächst einem Irrealen nähern. Wir haben in dem Denken, durch dessen Eigentümlichkeiten wir durchgehen mit unserer modernen philosophischen und wissenschaftlichen Entwickelung, keine Realität, wir haben bloßes Bild einer Realität.",
      "Und indem wir auf dieses Den- ken hinblicken, kommen wir auf der einen Seite zu dem Problem, das die neueren Erkenntnistheoretiker bewegt. Sie möchten die Brücke schlagen von dem, was inner- lich erlebt wird, zu dem, was äußerlich im Sein besteht.",
      "Sie merken nicht, daß sie gar nicht von einer Realität zur anderen zunächst die Brücke schlagen, sondern von 43 etwas, was in Bildern lebt, zu etwas, was Realität sein soll. Und auf der anderen Seite kommen wir dazu, daß die gewissenhaften Naturdenker sich gestehen: mit diesem irrealen Denken, mit diesem Denken, das im Bildcharakter aufgeht, können wir doch nicht untertauchen in die Reali- tät.",
      "Der Punkt, «wo Materie spukt», ist damit nicht zu er- reichen. Denn man webt in Bildern. Die moderne Philoso- phie webt in Bildern, weiß es nicht und sucht die Realität in diesen Bildern. Daher die Empfindung einer «Misosophie» bei Ludwig Haller, daher das Gefühl, man komme nicht in die Wirklichkeit hinein, wenn man sich in diesem Denken bewegt.",
      "Das ist das Problem der neueren philosophischen Ent- wickelung: daß notwendigerweise die Menschheitsgeschichte zu einem reinen Erfassen des irrealen bildhaften Denkens treiben mußte. Um der Entwickelung der Freiheit willen mußte die moderne Menschheit sich zu diesem irrealen bildhaften Denken erheben.",
      "Aber man kann in ihm nicht bleiben, wenn man ein Vollmensch ist, wenn man die Realität in allem menschlichen Wesen fühlt. Denn man muß den Widerspruch fühlen zwischen dem, was da drängt und lebt und webt in dem menschlichen Wesen, und dem, was vor dem Bewußtsein steht als ein bloßer Umkreis von irrealen Bildern.",
      "Wir haben es nicht bloß mit einem logisch formalen Problem zu tun, wir haben es mit einem realen Problem zu tun, mit einem realen Problem, das sich dadurch ergeben hat, daß der Mensch allmählich sein Denken, sein Vorstellen herausgezogen hat aus der äußeren Wirklichkeit. Es ist ihm die dunkle, finstere Materie, die er nicht be- greifen kann, in der Außenwelt übriggeblieben.",
      "Aber sein Denken ist nicht eine Realität geworden, es ist Bild ge- 44 worden. Und er muß weitergehen in diesem Bilde. Das Denken, das heute bloßes Bild ist, war für den Griechen noch Wahrnehmungsinhalt. Dieses Denken hat sich bewegt in der Richtung von außen nach innen.",
      "Es schreitet so vor, daß der Mensch erst denkend untertaucht in die äußere Welt. Jetzt ist er mit seinem Philosophieren auf dem Punkte, wo er in dem aus der äußeren Welt herausgeschäl- ten Denken webt. Er muß in dieser Richtung weitergehen.",
      "Er muß die Realität wieder suchen. Die Materie hat dem Menschen in alten Zeiten und bis in unser Zeitalter die Stütze für das Denken gegeben, indem sie ihm das Denken real gemacht hat. Das Denken aber ist, weil es die Grund- lage werden mußte für die Entwickelung der menschlichen Freiheit, in den Bildcharakter übergegangen.",
      "So schwebt es zwischen der Außenerfahrung und dem Innenerlebnis. Es muß untertauchen in dieses Innenerlebnis. Es muß wie- derum Realität bekommen. Der Mensch muß mit vollem Bewußtsein eintauchen in die Regionen, bei denen es Eduard von Hartmann und mit ihm allen modernen Phi- losophen so schwül wird, weil die Gedanken ihnen schei- nen anzufangen, wie Kobolde zu tanzen.",
      "Wenn der Mensch mit seinem Denken aus dem Bild- charakter herausgeht wo es ihm allerdings, wenn er drin- nen webt und lebt, weil es bloß Bilder sind, nicht so schwül zu werden braucht -, wenn er heraustritt und hineintritt in die eigene Realität, dann muß er allerdings durch die Übungen der Geisteswissenschaft die Möglichkeit in seine inneren Fähigkeiten aufnehmen, sich in diesem Selbstleben der Begriffswelt umzutun, wie sonst im mathematischen Denken. Er muß die Fähigkeit erwerben, die Wirklichkeit in diesem Selbstleben selbständig zu erfassen.",
      "Wie es einem ja auch nicht schwül wird, wenn die Dinge da draußen im Räume nicht stillstehen - damit unsere Erkenntnis nicht 45 beunruhigt werde -, sondern wenn sie, sich bewegend, lau- fen, so muß der Mensch im Aufsteigen zur Geist-Erklä- rung, zur Geistoffenbarung fähig werden, seinem Bild- begriff wiederum einen Inhalt zu geben. Erfaßt man an diesem Punkt das eigentliche, das drän- gende philosophische Leben der Gegenwart, dann kommt man von all den Redereien ab, daß der Philosoph nicht einsehen könne, was der Geistesforscher sagt.",
      "Er kann es einsehen, sobald er den Bildcharakter seines Denkens ein- gesehen hat, sobald er aber auch eingesehen hat, daß das Denken zu diesem Bildcharakter gekommen ist, weil es sich weltgeschichtlich in der Richtung von außen nach in- nen bewegt, von der Richtung des Geistes in der Materie zu der Anschauung der reinen geistigen Welt. In dieser Weise muß Philosophie fortgeführt werden, indem sie in Empfang genommen wird von der Geistes- wissenschaft, von der Geisteserforschung, indem das Den- ken eingetaucht wird in dasjenige, was die Geisteswissen- schaft, die Geistesforschung zu sagen hat.",
      "Das ist es, was ich Ihnen, wenn auch nur skizzenhaft mit einigen Linien darstellen wollte: in welcher Art befruchtet werden soll Philosophie von der Geisteswissenschaft. In den nächsten Tagen soll dann davon gesprochen werden, wie andere Zweige des menschlichen Denkens und Tuns von dieser Geisteswissenschaft befruchtet werden sollen.",
      "Schlußwort zur Disputation über Philosophie Dornach, 4. April 1921 Es sind im Laufe der Disputation Fragen aufgetaucht, die fachgemäß natürlich eine breite Aussprache erforderten. Ich möchte nur, weil wir ja an einem Abend nicht alles erörtern können, einige Andeutungen methodologischer Art geben, die mir bezüglich der Fragen, die auftauchten, und die, wie es mir wenigstens schien, nicht ganz klar for- muliert waren, nötig scheinen, um in die Richtung zu wei- sen, in der gewisse Lösungen solcher Fragen gesucht wer- den müssen.",
      "In Anbetracht solcher Fragen wie etwa der nach der «Subjektivität der Wahrnehmung», liegt in der jüngsten philosophischen Entwickelung ein vielfaches Konfundie- ren der Vorstellungen vor, ein Anhäufen von Begriffen, die eher die Probleme verdunkeln und verknäueln, als daß sie sie erhellen und zu einer gewissen Lösung führen würden. Es handelt sich nämlich in dem Augenblick, wo man Fragen aufwerfen will, die das Verhältnis von Objekt und Subjekt im Wahrnehmen vorstellend und erkenntnisgemäß betreffen, immer darum, durch eine sorgfältigste Analyse desjenigen, was der Tatbestand ist, darauf zu kommen, wie die Fragen eigentlich gestellt werden müssen.",
      "Denn oft werden schon die Fragen aus irrtümlich gerichteten Vor- stellungen falsch formuliert. Und so ist es vielfach mit den Fragen nach der «Subjektivität der Wahrnehmung». Da wurde auf die Schwierigkeit mit dem partiell Far- benblinden hingedeutet, von dem vorausgesetzt ist, daß er 47 eine, sagen wir, grüne Landschaft anders sehe als der so- genannte normal Sehende.",
      "In dieser Vorstellung des par- tiell Farbenblinden liegt die Schwierigkeit vor: inwieweit muß man dem, was nun auch der sogenannte normal Se- hende, ich sage ganz ausdrücklich: der sogenannte normal Sehende, sieht, Subjektivität beimessen? Nun, da handelt es sich darum, daß man sich zunächst das ganze Problem so vor Augen führen kann, daß es rich- tig erscheint.",
      "«Richtig» bedeutet, daß die Art, wie man die Elemente, die zur Problemstellung zusammengeführt wer- den müssen, daß man dieses Wie des Zusammenführens in der rechten Weise bewirkt. Nehmen Sie nur einmal an, wenn irgend jemand sagt: Ja, die Außenwelt, die mir also, sagen wir, in einer grünen Landschaft mit einer grünen Tingierung erscheint, gibt mir Veranlassung dazu, nachzu- denken, ob nun die Qualität «grün» objektiv ist, ob ich sie der Welt der Objektivität zuschreiben dürfe, oder ob sie als subjektiv angesprochen werden müsse.",
      "Dann muß man sich, um überhaupt zur Problemstellung zu kommen, solche Dinge überlegen, wie zum Beispiel dieses: Ja, wie verhält sich nun die Sache, wenn ich irgend etwas, was meinetwillen weiß oder gelb ist, durch eine grüne Brille ansehe? Da sehen wir es grün tingiert.",
      "Ist das nun der Sphäre der Objektivität zuzuschreiben, oder hat man da von Subjektivität zu sprechen? Man wird sehr bald be- merken, daß man ganz gewiß nicht dem, was da draußen ist, dieses Grün, das ich durch eine grüne Brille sehe, wird zuschreiben dürfen.",
      "Man wird nicht von Objektivität in bezug auf die äußere Umwelt sprechen können. Aber man wird doch auch ganz gewiß nicht davon sprechen können, daß diese grüne Tingierung, die ich da herausbekommen habe durch eine grüne Brille, auf irgend etwas Subjektivem beruht.",
      "Sie ist durchaus gesetzmäßig objektiv bedingt, 48 ohne daß dasjenige, was ich hier als grün bezeichne, wirk- lich grün ist. Sie sehen, ich stelle damit, daß ich mir eine Vorstellung bilde, ich möchte sagen, das Problem in ein besonderes Licht hin, wo ich dasjenige, was ganz gewiß nicht der Außenwelt angehört, doch objektiv, als auf objektive Art entstanden nehmen muß; denn die Brille gehört nicht zu mir, kann also ganz gewiß nicht in die Sphäre der Subjek- tivität einbezogen werden.",
      "Solche Dinge könnten sogar sophistisch erscheinen. Und dennoch sind solche Sophismen sogar sehr häufig das, was einen darauf bringt, die Ele- mente, die einen darauf führen sollen, die Fragen in ent- sprechender Weise zu stellen, auch zusammenzubringen.",
      "Man wird nämlich, wenn man solche scheinbaren Sophis- men in der richtigen Weise durchschaut, die ganze Faden- scheinigkeit der Alltagsbegriffe «Subjekt» und «Objekt», die allmählich in die moderne philosophische Betrachtung hineingebracht worden sind, durchschauen. Und man wird, wenn man in eine richtige Fragestellung hineinkommt, wohl immer mehr und mehr zu dem Weg, wie ich glaube, geführt werden, den ich in meinen Schriften «Wahrheit und Wissenschaft» und «Philosophie der Freiheit» ein- geschlagen habe, wo man überhaupt zunächst nicht den Ausgangspunkt nimmt von den Begriffen «Subjekt» und «Objekt», sondern wo man unabhängig von diesen Be- griffen etwas sucht, was über die Sphäre der Subjektivität und Objektivität hinaus gelegen sein muß: das ist die Funktion des Denkens.",
      "Die Funktion des Denkens! Wenn man die Sache un- abhängig durchschaut, erscheint einem das Denken eigent- lich über das Subjektive und Objektive durchaus hinaus- liegend. Und damit hat man einen Ausgangspunkt gewon- nen, von dem aus man dann auch in entsprechender Weise 49 da geführt werden kann, wo es sich um das solche Schwie- rigkeiten bietende Problem der «Subjektivität» und «Ob- jektivität» handelt.",
      "Denn man wird dann dazu geführt und Sie werden diesen Weg in diesen meinen beiden Büchern durchaus eingehalten finden -, nicht zu fragen: Wie wirkt eine äußere «objektive» Welt auf irgendeine «subjektive» Welt, für die etwa der Vermittler, sagen wir, das Auge ist? sondern man wird zu etwas ganz anderem geführt. Man wird nämlich dazu geführt, sich zu fragen: Wie ist denn die Tatsache der Sinne selber?",
      "Welche Wesen- haftigkeit zeigt einem der Sinn? Also zum Beispiel die Konstitution des Auges? Man wird dann finden, daß in dem Problem, das man sich so stellt, etwas zutage tritt, das ich jetzt, weil ich kurz sein muß - es könnte natürlich in einer stundenlangen Erläuterung auch mit dem adäquaten Begriff umfaßt wer- den , durch einen Vergleich klarmachen will: Ich kann auch durch eine Brille schauen und dennoch die Umwelt so sehen, wie das naive Bewußtsein sie als wirklich empfin- det, mit ihren Farbentingierungen, mit allen ihren Sinnes- qualitäten.",
      "Ich muß nur durch eine farblos-durchsichtige Brille schauen; ich darf nicht durch eine Brille schauen, die mir die Außenwelt selber verändert. Und ich muß mich jetzt hineinfinden in den Unterschied zwischen einer die äußere Tingierung verändernden Brille und einer farblos durchsichtigen Brille, die jede äußere Tingierung vermei- det.",
      "Von diesem Vergleich aus wie gesagt, es könnten langatmige Überlegungen anstelle des Vergleichs gesetzt werden - werde ich finden: wenn ich die Einrichtung des sogenannten normalen Auges nehme, habe ich in ihm eine Einrichtung gegeben, die sich gerade als durchsichtig er- weist, die sich vergleichen läßt mit dem durchsichtig-farb- losen Glase. Ich finde nichts im normalen Auge, was dar- auf hinweist, daß die Außenwelt qualitativ in irgendeiner Weise verändert wird.",
      "Aber ich muß diese Untersuchung anstellen nicht mit den gewöhnlichen Begriffen, die ich im alltäglichen Bewußtsein habe, sondern mit dem imagina- tiven Bewußtsein, das wirklich in die Einrichtungen des Auges eindringen kann. Für das imaginative Bewußtsein ist ein sogenanntes nor- males Auge ein durchsichtiges Organ.",
      "Ein Auge, das par- tiell farbenblind ist, das erweist sich für das imaginative Bewußtsein als in einer gewissen Weise vergleichbar mit einer farbigen Brille, als etwas, das allerdings eine Ver- änderung vornimmt in dem «Subjekt». So kommt man indem man die Subjektivität aber in einer höheren Auffassung auffaßt - gerade darauf, die Sinnesapparate im weitesten Umfange als dasjenige an- zusehen, was sich vergleichen läßt mit dem Durchsichtigen, was gerade so eingerichtet ist, daß es die eigene Produk- tion der Sinnesqualitäten in sich aufhebt.",
      "Man lernt als eine reine Phantasterei die Vorstellung erkennen, als ob in diesem ideell Durchsichtigen - das gerade so eingerichtet ist, daß es irgendeine Produktion der Sinnesqualitäten in sich aufhebt -, in diesem ideell durchsichtigen Sinnesappa- rat irgend etwas auftreten könnte, was Sinnesqualitäten erst hervorriefe, was zu etwas anderem da wäre als den Sinnesqualitäten den Durchgang zu lassen. Wie gesagt, ich will nur auf die Richtung deuten.",
      "Und ich will zu gleicher Zeit darauf hinweisen, daß sich das gewöhnliche Philosophieren auf den Punkt stellen sollte, zu sagen: Die Tatsachen der Welt erweisen sich, wenn ich sie vorurteilslos untersuche, so, daß sie mir Ergebnisse lie- fern, die einfach unauflösbar sind für das gewöhnliche Verstandesbewußtsein; die Tatsachen selber zeigen mir, daß ich hinausgehen muß über dieses gewöhnliche Ver- 51 standesbewußtsein. - Ehrlich ist es nicht, aus, sagen wir, der Tatsache des partiell Farbenblinden auf die Subjekti- vität der Farbenqualitäten zu schließen. Denn jedes solche Schließen hat irgendeinen logischen Fehler in sich, der im- mer irgendwie nachweisbar ist.",
      "Ehrlich wäre es, zu sagen: Man kommt einfach mit dem gewöhnlichen Philosophieren zu keinem Resultat, wenn man die Schwierigkeit, die sich aus dem Vergleich der partiellen Farbenblindheit mit dem Sehen des sogenannten normalen Auges ergibt, lösen will. - Das gewöhnliche Bewußtsein hat eben in diesem Punkte die Aufgabe, die Schwierigkeiten hinzustellen und zu sagen: Da sind sie. - Und würde man sich wirklich der Tragweite der Logik bewußt werden, des real-logischen Denkens innerhalb des Bewußtseins, so würde man über- all, ich möchte sagen, hinlegen die Probleme und würde sagen: Da ist wiederum eins, unauflösbar für das gewöhn- liche Bewußtsein, das zweite, das dritte - und würde sehen, daß die gewöhnliche Philosophie in vieler Bezie- hung nichts weiter ist als ein Hinweis auf Probleme und eine Hervorbringung einer Stimmung des Wartens, daß diese Probleme von einer höheren Stufe des Bewußtseins aus gelöst werden. Es ist nur der Drang, mit dem gewöhn- lichen Bewußtsein zurechtzukommen, der einen Nebel über die Probleme breitet und der nicht zugeben möchte, daß man mit ihm die Probleme nur aufwerfen kann und hin- weisen muß darauf, daß nun die menschliche Seele eine Entwickelung und Übungen durchmachen muß, diese Pro- bleme zu lösen.",
      "Das Gesetz der spezifischen Sinnesenergien ist eben durchaus nicht etwas, das innerhalb des gewöhn- lichen Bewußtseins behandelt werden kann. Wie gesagt, ich wollte nur auf den Hauptpunkt der Er- örterungen hinweisen, über das Thema der Farben, wollte darauf hinweisen, daß vor allen Dingen der Philosophie 52 und auch philosophischen Physiologie, Philologie und so weiter, in der Gegenwart notwendig wäre ein ganz gewis- senhaftes Umgrenzen desjenigen, was sie durch ihr Denken eigentlich vor das gewöhnliche Bewußtsein hinträgt.",
      "Das ist das eine, auf das ich aufmerksam machen möchte, wie gesagt, ganz unzulänglich. Denn es sollte nur auf eine bestimmte Richtung weisen; aber mehr kann auch nicht in einer so kurzen Erörterung getan werden.",
      "Das zweite, worauf ich hinweisen möchte, ist - wie- derum in bloß methodologischer Beziehung - das hier auf- geworfene Problem der Kategorien. Man könnte natürlich über das Kategorienhafte des menschlichen Denkens viele Stunden reden, allein ich möchte da zunächst nur auf das eine hinweisen: Innerhalb der eigentlichen Kategorientafel kommen die «Subjektivität» und die «Objektivität» gar nicht vor.",
      "Und daß innerhalb der eigentlichen Kategorien- tafel, der eigentlichen, der Urkategorientafel, «Subjekt» und «Objekt» gar nicht vorkommen, das bildet an sich eine Art von Beweis über das Wesen des kategorialen Den- kens: Wenn man die Kategorien in der Weise nimmt, wie sie nun nicht aus irgendeinem Beweis hervorgehen, sondern einfach, ich möchte sagen, aus der Logik herausgelöst wer- den, so müssen sie, indem man sie aufstellt, anwendbar sein auf dasjenige, was über «subjektiv» und «objektiv» erhaben ist. Es muß das, worauf die Kategorien zunächst anwendbar sind, ein Übersubjektives und -objektives sein.",
      "Damit aber nun, daß die Kategorien durch den Menschen selbst angewendet werden, ist ein klarer Beweis gegeben, daß im kategorialen Denken nicht ein Subjektives gegeben ist, sondern ein Subjektiv-Objektives. Es ist dies das Problem, über das auch Goethe so sehr viel gedacht hat.",
      "Und die Art und Weise seines Denkens, die ihn dazu führte, immer den Punkt aufzusuchen, wo 53 Subjektivität und Objektivität für den Menschen im menschlichen Erleben verschwinden, sich aufheben, dieses Bestreben machte ihn eigentlich zu dem Antipoden Kants. Es ist selbstverständlich durchaus richtig, daß man, wie gesagt wurde, auch im positiven Sinne aus Kant heraus arbeiten könnte; aber man kann aus allem in der Welt in positiver Weise heraus arbeiten, auch, aus dem größten Irrtum!",
      "Denn es gibt nichts in der Welt, woraus man nicht auch ein Positives herausschälen kann. Wir haben unter den Grundübungen - ich brauche nur daran zu erinnern: im zweiten Teil meiner «Geheimwissenschaft im Umriß» finden Sie die Sache besprochen - für den, der etwas zur höheren Erkenntnis kommen will, gerade diese Positivität angeführt, dieses Aufsuchen des Positiven.",
      "Das darf einen natürlich nicht blind machen für die Anerkennung von Abirrungen. Und schließlich, wenn wir das Historische ins Auge fassen, so können wir sagen: Positiv ist aus Kant sehr viel herausgearbeitet worden.",
      "Es gibt ja nicht nur die kritischen Kant-Philologen, nicht nur die Neukantianer vom Schlage Liebmanns, Volkelts und so weiter, sondern es gibt gerade die in dieser Beziehung sehr tätige Marbur- ger Schule Cohen, Cassirer, Dilthey und so weiter , die versuchte, in gewisser Beziehung aus Kant positiv heraus- zuarbeiten. Nun, ich habe gezeigt, wie wenig zu einer wirklichkeits- gemäßen Anschauung dieses «positive Herausarbeiten aus dem Kantianismus» führen kann: in meinen «Rätseln der Philosophie», wo ich kurz auch diese Bestrebungen der Marburger Schule besprochen habe.",
      "Also auch beim Kate- gorienproblem handelt es sich darum, es richtig in seiner ganzen inneren Wesenheit vor die Seele hinzustellen, um zu sehen, wie gerade durch das Kategorienproblem die Frage nach dem «Subjektiven» im Gegensatze zum «Ob- 54 jektiven» nicht so gestellt werden kann, wie es unter dem Einfluß des Kantianismus die neuere Philosophie getan hat. Dieses geradezu erkenntnistheoretische Einspannen in die Subjektivität ist etwas, was zahllose ungerechtfertigte Vorstellungen in unsere moderne Philosophie hinein- gebracht und uns Vorstellungen hat verlieren lassen, die schon da waren, und die in entsprechender gerader Fort- entwickelung zu etwas recht Fruchtbarem hätten führen können.",
      "Ich muß da immer wieder und wiederum darauf auf- merksam machen was ich ja schon öfter getan habe , wie ein außerordentlich begabter Philosoph des 19. Jahr- hunderts, Franz Brentano, 1874 den ersten Band seiner «Psychologie» hat erscheinen lassen.",
      "Es ist im Grunde ein geistvolles Buch. Dieser Band «Psychologie» von Brentano erschien im Frühling 1874. Für den Herbst desselben Jah- res versprach er den zweiten Band. In kurzer Zeit sollten dann die drei folgenden Bände erscheinen.",
      "Auf fünf Bände hatte Brentano zunächst diese «Psychologie vom empi- rischen Standpunkte» berechnet. Der erste Band war nur eine Vorbereitung. In ihm findet sich aber doch eine höchst merkwürdige Stelle, in der darauf hingedeutet wird, wie Franz Brentano in der Tat auf die bedeutsamsten psycho- logischen Probleme hinzielte.",
      "Er sagt da: Wenn wahrhaftig alles moderne Denken nur dazu führen sollte, zu unter- suchen, wie Vorstellungen auf- und niedersteigen, sich mit- einander vergesellschaften, wie sich das Gedächtnis bildet und dergleichen, und wenn man darüber nur zur Unge- wißheit kommen könnte über die eigentlichen psychologi- schen Fragen eines Plato und Aristoteles, zum Beispiel, ob die Seele erhalten bleibe, wenn ihr äußerer physischer Leib zerfällt, dann hätte man durch die moderne Wissenschaft- lichkeit wahrhaftig für die Bedürfnisse des Menschen nicht 55 viel gewonnen! - Nun, man kann aus allem anderen, was Brentano da andeutet im ersten Bande seiner «Psychologie vom empirischen Standpunkte», schon ersehen, wie er durch seine fünf Bände hindurch das Problem bis zu diesen Grundfragen des Plato und Aristoteles bringen wollte. Das Merkwürdige ist, daß im Herbst der zweite Band nicht erschien.",
      "Er erschien auch im nächsten Jahr nicht. Und in den neunziger Jahren versprach Brentano neuer- dings, daß er nun daran gehen werde, wenigstens eine Art Surrogat in einer Art deskriptiver Psychologie zu schaffen.",
      "Also es sollte schon 1874 der zweite Band der «Psycho- logie» erscheinen. Nichts erschien bis in die neunziger Jahre; da erschien ein zweites Versprechen, wurde aber nicht erfüllt! Franz Brentano ist vor einigen Jahren in Zürich gestorben.",
      "Das Versprechen ist bis heute nicht er- füllt. Es ist beim ersten Bande der «Psychologie vom em- pirischen Standpunkte» geblieben. Warum? Weil Brentano in seiner Privatdozentenschrift den Satz aufgestellt hat: «Die Philosophie hat zu folgen denselben Methoden, die in der Naturwissenschaft angewendet werden», weil Bren- tano treu bleiben wollte diesem methodologischen Satz, den er damals aufgestellt hat, und mit dem sich eben nicht weiterkommen ließ.",
      "Brentano war eine viel zu ehrliche Natur, als daß er durch irgendwelche anderen Mittel als durch die Mittel der äußeren wissenschaftlichen Methode hätte weiterkommen wollen. Daher schwieg er einfach über das, was über den ersten Band hinauskam.",
      "Ich habe das in meinem Buche «Von Seelenrätseln» aus- gesprochen. Der Brentano-Schüler Kraus hat allerdings gesagt, es lägen allerlei andere Gründe vor dafür, daß Brentano die späteren Bände nicht veröffentlicht hat; al- lein man muß sagen, wenn die Gründe bloß vorgelegen hätten, auf die Kraus da hinschaute, dann hätte Brentano ein richtiger Philister sein müssen.",
      "Und das war er gewiß nicht. Er war schon eine Persönlichkeit, die durchaus den Impulsen des Inneren folgte und ihnen allein! Aber es war doch etwas vorhanden in Brentano, welches ihm wenig- stens die Hoffnung erweckte, daß man in die Dinge der Welt eindringen könne.",
      "Und im Grunde genommen hat jeder solche Philosoph es sind ja ihrer wenige, die in be- gründeter Weise in der neueren Zeit diese Hoffnung ge- habt haben - sich gegen Kant gewendet, selbstverständlich auch Franz Brentano. Es war etwas in ihm, was diese Hoffnung begründete.",
      "Und das finde ich in einem Begriff, der, ich möchte sagen, vereinzelt immer wiederum aus dem Brentanoschen Philo- sophieren herauf taucht, und den er im Sinne einer älteren Philosophie von der Art, als man noch aus der Wirklich- keit geschöpft hat, wie ich es heute morgen angedeutet habe - entlehnt hat: es ist der Begriff des intentionalen Inneseins, den er auf die Erkenntnis- und Wahrnehmungs- vorstellungen anwendet. Dieser Begriff, der muß formuliert werden.",
      "Dann wird man von da aus eine Annäherung an dasjenige erhalten, was ich eben vorhin angedeutet habe: zu untersuchen, in- wiefern das menschliche Sinnesorgan ein Sich-selbst-Aus- löschendes ist, dem man also gar nicht zuschreiben darf, daß es der Produzent der Sinnesqualitäten sein könne. Und dieser Begriff - nun nicht des realen Inneseins irgend- eines Prozesses, sondern des intentionalen Inneseins - ent- hält in sich das Leben des Hinweisens, das dann für das imaginative Vorstellen beobachtbar wird.",
      "Und dieses Le- ben des Hinweisens, das gegeben ist mit dem Begriff des intentionalen Inneseins, bringt dann die Möglichkeit, das zu erfassen, was man seit Johannes Müller, dem Physiolo- gen aus der ersten Hälfte des 19. Jahrhunderts, in so un- 57 zulänglicher Weise mit der Lehre von den «spezifischen Sinnesenergien» erfassen wollte.",
      "So daß man sagen möchte, der Vergleich mit dem durchsichtigen, farblosen Glase ist nicht ganz zutreffend aus dem Grunde, weil man sich nicht ein unlebendiges Farbloses, sich selbst also Aufhebendes vorzustellen hat, sondern ein lebendiges und gerade durch seine Lebendigkeit sich Aufhebendes und dadurch in einem entsprechenden Prozeß Drinnenstehendes, der ein Objek- tives erleben läßt, indem er das Objektive nicht herein- nimmt, sondern aus sich den Prozeß des Hinweisens durch und in dem Hinweisen auf dieses Objektive erfaßt. Ich habe das, was durch eine im Sinne moderner Welt- auffassung gehaltene Erneuerung dieses Begriffs des in- tentionalen Inneseins liegt, nur bei einigen neueren ameri- kanischen Philosophen gefunden, welche - wahrscheinlich sogar ohne diesen Begriff, den ich eben angeführt habe, zu kennen versuchen, die Kontinuität des menschlichen Be- wußtseins zu erfassen.",
      "Sagen wir zum Beispiel: im neun- undzwanzigsten Lebensjahre schaut der Mensch erinne- rungsgemäß zurück auf dasjenige, was er durchgemacht hat, sagen wir im achtzehnten Lebensjahr. Dann ist das, was den Menschen im neunundzwanzigsten Lebensjahr zurückweist, wenn man es innerlich erfaßt, etwas dem- jenigen Ähnliches, was man als ein intentionales Innesein bezeichnen könnte.",
      "Und in bezug auf diesen Prozeß tritt bei einigen neueren amerikanischen Erkenntnistheoretikern dieser Begriff wieder auf. Man sieht gerade an solchen Erscheinungen, wie ein be- griffliches Arbeiten in dem philosophischen Streben der Gegenwart lebendig ist.",
      "Aber dieses Arbeiten muß durch- aus in einer solchen Weise ehrlich werden, wie ich es vorhin bezeichnet habe, indem man dazu kommt, klar zu zeigen: Es liegen Probleme vor; das gewöhnliche Bewußtsein aber, 58 die gewöhnliche Verstandestätigkeit, das kann die Pro- bleme nur aufwerfen; und nun muß weiter fortgeschritten werden zu der Lösung der Probleme. Würde man in dieser Weise wissenschaftliche Ehrlichkeit entwickeln, dann würde diese die Grundlage sein für das Aufsteigen zum Imaginativen und den anderen Erkenntnisstufen.",
      "Das sollen nur ganz unzulängliche, methodologische Hinweise sein."
    ],
    "sentences": [
      [
        "Die Vorträge dieser Woche sollen so eingerichtet sein, daß jeder Tag einem anderen Fache gewidmet ist, so daß er- scheinen kann, was als Befruchtung der einzelnen Fach- wissenschaften und Zweige des praktischen Lebens von der Geisteswissenschaft bewirkt werden soll.",
        "Heute soll mit dem wissenschaftlichen Fach begonnen werden, das in einer gewissen Beziehung der Geisteswissenschaft, wie sie hier gemeint ist, selber am nächsten steht: mit dem Fache der Philosophie."
      ],
      [
        "Was ich hier selbst werde zu sagen haben, soll eine Art Einleitung sein zu den Fragen, die im Laufe des heutigen Tages behandelt werden sollen.",
        "Ich möchte dabei von einem der interessantesten und sogar bedeutsamsten Phänomene der neueren philosophi- schen Entwickelung ausgehen."
      ],
      [
        "Es ist ja durchaus so, daß nicht immer diejenigen Erscheinungen die bedeutsamsten und interessantesten sind, die bald darauf in den gebräuch- lichen Geschichtswerken verzeichnet werden.",
        "Und so möch- te ich denn von einer Erscheinung ausgehen, die noch sehr wenig geschichtlich zum Ausdrucke gekommen ist, von der ganzen Bedeutung eines 1888 erschienenen philosophischen Werkes, das herrührt von Ludwig Haller, einem Regie- rungsrat und Staatsanwalt, und das den Titel trägt «Alles in Allen: Metalogik, Metaphysik, Metapsychik»."
      ],
      [
        "Ich darf von diesem Phänomen im philosophischen Leben um so mehr ausgehen, als derjenige, der meine eigene schrift- stellerische Laufbahn verfolgt, sehen kann, daß ich selbst von diesem Phänomen ganz unbeeinflußt geblieben bin, 26 weil dasjenige, was meine Stellung zur Philosophie aus- macht, durchaus schon enthalten ist in meinen Schriften, die vor dieser «Metalogik, Metaphysik, Metapsychik» er- schienen sind, und das, was ich später gesagt habe, nur eine sachgemäße und konsequente Ausgestaltung des in meinen ersten Schriften Enthaltenen ist.",
        "Vor allen Dingen tritt uns in dem Staatsanwalt und Regierungsrat Ludwig Haller, der sonst nichts geschrieben hat als das genannte Werk, ein Mensch entgegen, bei dem das, was man Philosophie nennt, nicht nur Fachwissen- schaft ist - obwohl er in einer gewissen Beziehung durchaus befähigt ist, sich mit dieser Fachwissenschaft auseinander- zusetzen , sondern bei dem das, was er vorbringt, aus unmittelbar persönlichem philosophischem Erleben heraus kommt."
      ],
      [
        "Wir haben es mit einer Persönlichkeit zu tun, wel- cher das philosophische Streben innerlichstes persönliches Erleben geworden ist.",
        "Und wenn wir gleich eingehen auf das Bedeutsamste bei Ludwig Haller, dann müssen wir verzeichnen, daß er eigentlich mit der ganzen Art des philosophischen Denkens der neueren Zeit auf dem Kriegs- fuße steht."
      ],
      [
        "Er hat sich offenbar viel umgetan in allerlei Philosophie und auch in denjenigen Literaturwerken, in denen «Lebensphilosophie» sprudelt.",
        "Er hat sich einge- wöhnt in das philosophische Denken seiner Zeit und er hat gefunden es ist das, wie gesagt, seine Meinung , daß man sich mit diesem philosophischen Denken eigentlich in einer Art von unwirklichem Kreise dreht, daß man mit diesem philosophischen Denken niemals in die Lage kommt, in die Wirklichkeit selber unterzutauchen."
      ],
      [
        "Ludwig Haller möchte mit seinem Philosophieren in die geistige Wirklichkeit eindringen, die er, indem er offenbar seiner Erziehung nach herausgewachsen ist aus mehr reli- giösen Vorstellungen, «das Göttliche» oder auch wohl «Gott» nennt.",
        "In diesem «Göttlichen» oder in «Gott» sucht er den Quell alles dessen, was als die eigentliche Wesenheit auch in der menschlichen Seele leben und dessen sich die Menschenseele auch bewußt werden müsse."
      ],
      [
        "Aber er kommt eben darauf, daß diese Seele, indem sie die zu seiner Zeit gebräuchlichen Begriffsgewebe verarbeitet, in dieses Zen- trum ihres Wesens, wo sie eins ist mit dem Göttlich-Geisti- gen der Welt, nicht eindringen könne.",
        "Da dieses Gedankenweben der Philosophen Ende der achtziger Jahre, in denen das genannte Werk erschien, ja noch vielfach ganz und gar beeinflußt war von Kant und also Kantische Gedanken in diesem Gedankenweben leb- ten, so fühlte sich Ludwig Haller vor allen Dingen auch veranlaßt, sich mit dem Kantianismus und alledem, was von dem Kantianismus herrührt, zu beschäftigen."
      ],
      [
        "Aber gerade in all den Gedanken, in die nur irgendwie Kanti- sches hineinfließt, sah er das Unwirkliche, dasjenige, was niemals in die Wirklichkeit der Welt untertauchen kann.",
        "Und er war eigentlich unglücklich darüber, daß er, weil er eben philosophisch in seiner Zeit sprechen wollte, sich mit diesem vom Kantianismus durch und durch infizierten Denken beschäftigen müsse, daß er immer wieder und wiederum darauf zurückkommen müsse, sich mit dem Kantianismus auseinanderzusetzen."
      ],
      [
        "Er fand recht scharfe Worte, um erstens den Kantianismus selbst zu charakteri- sieren, und dann auch für das ihm so unsympathische Sich- auseinandersetzen-Müssen mit dem Kantianismus.",
        "Ich möchte Ihnen zwei Proben aus diesem Beurteilen des Kantianismus hier mitteilen, damit Sie sehen, womit ein Mensch, für den Philosophie eine innerlichst persönliche Angelegenheit ist, in unseren Zeiten ringt."
      ],
      [
        "Einmal spricht da Ludwig Haller vom Kantianismus so, daß er über ihn sagt: der «pseudodialektische, halbwahre, 28 im Tiefsten unredliche Charakter dieser Misosophie, welche dem Arsenal des Lichtes die Waffen zu stehlen versucht, um sie im Dienste der Finsternis zu verwenden».",
        "Ein andermal wird er, ich möchte sagen, schriftstellerisch wütend darüber, daß er immer wieder und wiederum sich genötigt findet, weil er doch mit seinen Zeitgenossen sich auseinandersetzen muß, auf das Kantische Denken einzu- gehen, und er sagt: «Ich, der ich von Gott und seiner Herr- lichkeit reden könnte und möchte, sehe mich immer von Neuem dazu verdammt, von Kant und seiner Erbärmlich- keit zu reden ich eines Gecken Geck.» Ich wollte auf dieses Phänomen hinweisen, weil es ein Abdruck ist von den Kämpfen, die eine wirklich philoso- phisch angelegte Natur am Ende des 19."
      ],
      [
        "Jahrhunderts zu bestehen hatte.",
        "Man nimmt heute, was philosophisches Reden und Schreiben ist, durchaus auch so, daß man dar- aus möglichst eine Angelegenheit macht, die sozusagen ein Stück über den menschlichen Köpfen darüber schwebt, bei der man persönlich gar nicht dabei ist."
      ],
      [
        "Daher werden die inneren tragischen Phänomene des philosophischen Lebens in unserer Zeit viel zu wenig gewürdigt.",
        "Und ich glaube, daß dieses Phänomen, das zu dem Tragischesten in den inneren philosophischen Erlebnissen unseres Zeit- alters gehört, eigentlich in weiteren Kreisen recht wenig bekanntgeworden ist."
      ],
      [
        "Wer das Geistesleben dieser Zeit wirklich kennt, der weiß, wieviel von solchen Stimmungen in Menschen unse- res Zeitalters gelebt hat.",
        "Und eigentlich muß man auch, wenn man das Wesen philosophischen Denkens in unserer Zeit darlegen will, gerade von diesen Erscheinungen reden, die ja von den philosophischen Fachmännern nicht beachtet werden, die aber für das eigentliche menschliche Erleben um so wichtiger sind."
      ],
      [
        "Nun möchte ich, anknüpfend an dieses Phänomen, ein anderes, das im Grunde genommen auch nur ein sozusagen subjektiv persönliches philosophisches Erlebnis ist, charak- terisieren.",
        "Der bekannter als Ludwig Haller gewordene Philosoph Eduard von Hartmann hat sich mit Ludwig Haller auseinandergesetzt."
      ],
      [
        "In dieser Auseinandersetzung ist ein Punkt von ganz besonderer Bedeutung.",
        "Ludwig Haller, der sich viel zu tun macht, Sie sahen, er nennt sich wegen dieses Sich-viel-zu-tun-Machens «eines Gecken Geck», mit dem Sich-Hineinfinden in das kantisch infi- zierte Gedankenweben seiner Zeit, unseres Zeitalters - er verspürt nämlich, indem er so mit dem Denken von Be- griff zu Begriff geht, indem er sich dem philosophischen Denken überläßt, das sieht man ganz deutlich überall durchleuchten aus seinem Buche - er verspürt, daß die Begriffe, denen er nun folgt mit dem Denken, ein merk- würdiges Innenleben gewinnen."
      ],
      [
        "Es ist ihm so, als ob die Begriffe in seinem Gemüte anfingen ein selbständiges Leben zu führen.",
        "Das hebt er an den verschiedensten Stellen seiner «Metalogik, Metaphysik, Metapsychik» her- vor.",
        "Wenn wir psychologisch auf dieses interessante Phäno- men eingehen wollen, so können wir nicht anders als das Folgende sagen: Ludwig Haller versetzt sich mit aller Ge- walt in die besondere Natur des gegenwärtigen philoso- phischen Denkens."
      ],
      [
        "Aber sein inneres menschliches Erleben will eigentlich etwas anderes; zu diesem anderen kann er nicht kommen, weil in den achtziger Jahren ja auch nicht die Spuren einer wirklich modernen Geisteswissenschaft vorhanden waren.",
        "Es fehlt in seinem Inneren das, was dieses menschliche Innere mit wirklicher Geisteswissen- schaft erfüllen könnte."
      ],
      [
        "Aber es lebt, möchte ich sagen, auf eine merkwürdig instinktiv unbewußte Art darin.",
        "Er weiß 30 nichts davon, aber er merkt es an diesem sonderbaren Phä- nomen, daß die Begriffswelt bei ihm lebendig wird, ein selbständiges Leben führt."
      ],
      [
        "Wer im Sinne der hier vertretenen Geisteswissenschaft forschen kann, der kennt dieses selbständige Leben der Begriffe sehr gut.",
        "Aber er kann es auch beherrschen.",
        "Er kann es in dem Sinne beherrschen, wie man den Übergang von einem mathematischen Begriff zu dem anderen mathe- matischen Begriff im gewöhnlichen Mathematisieren be- herrschen kann."
      ],
      [
        "Aber dieses Beherrschen, das muß durch innerliche Übung errungen werden.",
        "Es ist ganz selbstver- ständlich, daß man in ein dem gewöhnlichen Bewußtsein ganz fernes Leben hineinkommt, wenn man so plötzlich merkt - was sonst nur die Speisen in unserem Organismus tun, daß sie ohne unser Zutun ihr eigenes Leben in der Verdauung führen -, daß die aufgenommenen Begriffe anfangen, innerlich ein eigenes Leben zu führen."
      ],
      [
        "Es ist nicht unbegreiflich, sondern sehr, sehr begreiflich, daß nun ein Philosoph wie Eduard von Hartmann, der ja geistvoll war, der auf manchen Gebieten auch durchaus Eindring- liches geleistet hat, der aber durchaus herausgewachsen ist aus dem philosophischen Denken seines Zeitalters, mit diesem Erlebnis Ludwig Hallers nichts Besonderes anfan- gen konnte.",
        "Und indem Eduard von Hartmann seine Kritik über Ludwig Haller schreibt, merkt man, daß ihm auf der einen Seite ganz schwül wird."
      ],
      [
        "Was soll denn das werden - so sagt sich der richtig zeitgemäße Philosoph -, wenn da die Begriffe, denen ich mich hingebe, plötzlich anfangen in meinem Inneren wie Kobolde zu tanzen, sich gegenseitig zu umhalsen oder dergleichen?",
        "Das ist ja etwas Fürchterliches, dem kann man sich nicht aussetzen! - Und er gibt demgemäß auch, als richtiger zeitgemäßer Philo- soph, diese Kritik in einer recht bedeutsamen Weise ab, indem er sagt, er habe niemals etwas bemerkt von diesem neckischen, koboldartigen Treiben der selbständig lebendig gewordenen Begriffe."
      ],
      [
        "Man kann Eduard von Hartmann durchaus glauben, daß er diese Schwüle im Inneren beim Lesen der «Metalo- gik, Metaphysik, Metapsychik» Ludwig Hallers empfand.",
        "Er hat, wie seine Kritik zeigt, deshalb doch nicht aufge- hört, das ganze Buch durchzulesen, hat es sogar in einem gewissen Sinne sehr bedeutend gefunden."
      ],
      [
        "Ich glaube, viele andere, die sich in dem Zeitalter, das auf 1888 gefolgt ist, fachmännisch mit Philosophie beschäftigt haben, sind wohl kaum über die ersten Seiten dieses Buches hinausgekom- men, wenn sie überhaupt auch nur das Titelblatt kennen- gelernt haben!",
        "Worauf ich Sie da hinweise, ist eine durchaus bedeut- same Erscheinung."
      ],
      [
        "Und wir verstehen sie nur, wenn wir die philosophische Entwickelung des Abendlandes so ver- folgen, wie ich sie zu verfolgen versuchte in meinem Buche «Die Rätsel der Philosophie».",
        "Wenn man auf das eingeht, was ich dort genauer und in allen Einzelheiten an der Hand der Philosophiegeschichte ausgeführt habe und was ich hier nur andeuten kann, so sieht man, daß im Zeitalter des griechischen Philosophierens die ganze menschliche Seelenverfassung eine andere war, als sie später geworden ist und als sie namentlich in unserer Zeit ist."
      ],
      [
        "Wir sehen, wie im griechischen Philosophieren durchaus das, was wir Denken nennen, was wir Vorstellen nennen, in einer ähn- lichen Weise mit den Bedingungen der Außenwelt, insofern sie sich dem Menschen darstellt, verknüpft ist, wie für uns nurmehr die sinnlichen Wahrnehmungsqualitäten.",
        "Indem wir wahrnehmen, schreiben wir, wenigstens im naiven Be- wußtsein, dem, was wir wahrnehmen, die sinnlichen Qua- litäten zu."
      ],
      [
        "Gewiß, die erkenntnistheoretischen Erörterun- gen seit Locke und anderen denken anders, aber sie brau- dien uns in diesem Augenblicke weniger zu interessieren; ich will für die herangezogene Tatsache nur auf das naive Bewußtsein verweisen.",
        "Man schreibt in diesem naiven Bewußtsein den Dingen die Sinnesqualitäten rot, blau, weiß, warm, kalt, lau, süß, bitter und so weiter zu, und man ist sich heute klar darüber, daß dasjenige, was man an den Sinnesobjekten denkt und vorstellt, im Bewußtwerden abgesondert ist von dem Objektiven, daß es subjektiv erlebt wird."
      ],
      [
        "Der Grieche schrieb aber sein Denken, seine Vorstellungen dem Objekte noch so zu, wie wir rot, blau, süß, bitter und so weiter dem Objekte zuschreiben; er hatte, was er im Erkennen erlebte, zu einem noch größeren Teile sozusagen in der Wahrnehmung drinnen, als wir das haben.",
        "Er hatte durchaus das Bewußtsein, daß er mit dem Rot, Grün und so weiter zugleich den begrifflichen Inhalt wahrnahm."
      ],
      [
        "Und was, ich möchte sagen, in der am meisten logischen Weise im griechischen Denken zutage trat, das war bis in das 13., 14., 15.",
        "Jahrhundert herauf, bis in die Galilei- Kopernikus-Zeit, im Grunde genommen eine Eigentüm- lichkeit des allgemeinen forschenden Bewußtseins."
      ],
      [
        "Wer sich vertieft in dasjenige, was zutage getreten ist in wissen- schaftlichen Leistungen, die ja für diese Zeit durchaus noch eins waren mit dem philosophischen Forschen, wer sich vertieft in die entsprechende Literatur, soweit sie vorhan- den ist, wird sagen, daß diese älteren Forscher und Denker durchaus, indem sie von den Dingen reden, an den Dingen dasjenige noch als objektiv schildern, was der heutige For- scher durchaus von den Dingen abgesondert denkt und dem Subjekte zuschreibt.",
        "Man kann verfolgen, und dieses Verfolgen ist außer- ordentlich interessant, wie im Zeitalter der Scholastik das 33 philosophische Leben die Richtung nimmt, sich klarzuwer- den, wie eigentlich das, was wir das Denken in Begriffen nennen, noch verbunden gedacht werden darf mit dem Objektiven."
      ],
      [
        "Vor dem scholastischen Zeitalter war die Ver- bindung desjenigen, was als Vorstellung und Begriff an den Dingen erlebt wird, mit diesen Dingen selbstverständ- lich.",
        "Eine Frage, ein Rätsel wurde diese Verbindung erst, als sich für das menschliche Erleben das Begriffliche, das Vorstellungsmäßige von dem löste, was man die objektive Wahrnehmung nennt."
      ],
      [
        "Und aus diesem philosophischen Er- leben heraus ist dann der Scholastik jenes Problem entstan- den, das man heute viel gründlicher studieren sollte, als man es studiert, das Problem des «Realismus» und des «Nomi- nalismus».",
        "Heute verbindet man sogar ganz andere Vor- stellungen mit diesen Worten «Realismus» und «Nomina- lismus», als es im Zeitalter der Scholastik der Fall war."
      ],
      [
        "Im Zeitalter der Scholastik war ein Realist, wie zum Beispiel Thomas von Aquino, derjenige, der den Begriffen, den Vorstellungen eine objektive Realität beilegte, so daß er sagte: Die Begriffe, die Vorstellungen haben etwas, was in seinem Inhalte objektiv ist, was nicht bloß dem Subjekte angehört, was nicht bloß gedacht ist.",
        "Ein Nominalist war derjenige, der die Realität nur in dem suchte, was außer- halb des Begrifflichen liegt, der in den Begriffen nur etwas sah, wodurch der Mensch zusammenfaßt, was ihm als Wahrnehmung gegeben ist, so daß die Begriffe für den Nominalisten eben bloße Namen waren."
      ],
      [
        "Solch ein Problem taucht immer dann auf in der Mensch- heitsentwickelung, wenn innerlich etwas durchgemacht wird.",
        "Der Mensch hatte eben dieses innerlich durchzu- machen im Mittelalter, daß er sich immer verwandter und verwandter machte in seinem eigenen Inneren mit dem begrifflichen Leben, daß er das, was Außenwelt genannt 34 wird, nur in dem Wahrnehmbaren sah."
      ],
      [
        "Daher wurde es für ihn eine Frage: Wie ist man berechtigt, dasjenige, was man im Grunde genommen innerlich nur als Name hat, was man nur so erfaßt, daß man die äußerlichen Wahrneh- mungen damit zusammenordnet, auf diese äußerlichen Wahrnehmungen irgendwie zu beziehen?",
        "Ein bedeutsamer Skeptizismus geht aus dem Nominalismus hervor."
      ],
      [
        "Und im Grunde genommen ist das, was dann in der Kantischen Philosophie aufgetreten ist, nichts anderes als, ich möchte sagen, die letzte Konsequenz dieses Scholasti- kerproblems.",
        "Nur kam Kant auf eine eigentümliche Weise gerade zu seiner Formulierung des Scholastikerproblems: In dem Zeitalter, in dem Kant als Jüngling seine philoso- phischen Studien gemacht hat, war der etwas verdünnte Leibnizianismus innerhalb der Kreise herrschend, in denen eben Kant seine Studien machte."
      ],
      [
        "Der Leibnizianismus, der in seiner Art etwas Großes ist, wenn auch etwas außer- ordentlich Abstraktes, der noch durchaus einen Zusammen- hang mit Wirklichkeitsgeist hat, war im Wolffianismus, der für Kant das Jugendstadium bildete, philosophisch sublimiert, verdünnt.",
        "Man hatte in dieser Zeit schon durch- aus zu tun mit den Ansprüchen der mathematisierenden Wissenschaft, mit den Ansprüchen der Wissenschaft, die sich eben zusammensetzt aus den Ergebnissen der Außen- beobachtung der Welt."
      ],
      [
        "Aber aus der alten Gewohnheit heraus, daß der Mensch doch etwas mitzusprechen habe, wenn über die Welt etwas ausgemacht wird, hatte man neben dieser empirischen Wissenschaft, neben dieser Er- fahrungswissenschaft, die breite Vernunftlehre statuiert.",
        "Man hatte statuiert: über alles Vergängliche können durch Erfahrung, durch Empirie, Ungewisse Urteile gewonnen werden; aber diese Urteile sind eben durchaus nur auf das Vergängliche gerichtet und sind ungewiß."
      ],
      [
        "Man kann nicht 35 wissen, ob sich das, was man über irgendeine Tatsache der vergänglichen Welt durch Beobachtung und Verstan- deserkenntnis erkennt, auch wirklich, wie notwendig für alle Zeiten, so verhalten muß.",
        "Man kann nicht einmal wissen, daß die Sonne jeden Morgen aufgehen muß, denn man hat nur den einen Erfahrungsbeweis, daß sie bis jetzt an jedem Morgen aufgegangen ist."
      ],
      [
        "Daraus kann man schließen, daß sie auch zukünftig aufgehen wird; aber es ist eben nur ein Erfahrungsschluß.",
        "Über diese Erfahrungs- wissenschaft hinaus suchte nun der Wolffianismus, suchte auch Kant in seiner Jugend, ganz im Einklang mit dem Wolffianismus, eine Vernunftwissenschaft."
      ],
      [
        "Es ist charak- teristisch, daß ein Buch von Wolff so heißt: «Vernünftige Gedanken von Gott, der Welt und der Seele des Menschen, auch allen Dingen überhaupt.» Also es handelte sich darum, auf der einen Seite ein Erfahrungswissen zu gewinnen über den Umkreis der Welt, soweit er der Erfahrung zugänglich ist, und auf der anderen Seite ein über alles sich erstreckendes Vernunft- wissen, das gewissermaßen aus der Vernunft allein heraus gewonnen werden soll.",
        "Und man begründete neben der, sagen wir, geoffenbarten Theologie eine vernünftige, eine rationelle Theologie, neben der Erfahrungs-Seelenkunde eine rationelle Psychologie, neben der Weltkunde, die man durch Erfahrung gewinnt, eine rationelle Geologie und so weiter."
      ],
      [
        "Gewohnheitsmäßig lag diesem Suchen nach einer besonderen Vernunftwissenschaft zugrunde, daß man sich sagte: In einer äußeren Welt gibt es keine Gewißheit für das wissenschaftliche Forschen.",
        "Will man aber eine solche Gewißheit haben, kann man sie nur dadurch gewinnen, daß man sie aus der Vernunft selber heraus gewinnt."
      ],
      [
        "Allerdings liegt dem ganzen Forschen des Wolffianismus noch das zugrunde, daß zuerst auf irgendeine transzendete 36 Weise in diese Vernunft, aus der heraus der Mensch dann seine «Vernunftwahrheiten» gewinnt, eine Wirklichkeit hineingelegt worden ist.",
        "Zweierlei trat bei Kant auf, und wer ganz unbefangen Kant studiert, wird scharf hingewiesen auf das, was bei ihm nach zwei Seiten hin auftaucht: Auf der einen Seite hatte er sich eingewöhnt in das Suchen nach «gewissen Urteilen»."
      ],
      [
        "Er hatte sich zum Beispiel gesagt: In der Mathe- matik haben wir solche Urteile, die ganz notwendig immer gelten, die also nicht aus der Erfahrung stammen können, weil die Erfahrung keine solchen Urteile gibt.",
        "Wir haben auch in einigen Partien des naturwissenschaftlichen Den- kens solche Urteile, die für immer gelten, die also wirklich nur aus dem Menschen selbst heraus gewonnen werden können."
      ],
      [
        "Gewißheit muß es geben in der Philosophie. - Das war die eine Seite dessen, was Kant wollte.",
        "Und wer nicht ins Auge faßt, wie Kant fest auf dem Boden stand: Gewißheit muß es geben - auch im Sinne der Wolffischen Philosophie -, der versteht eben Kant nicht, weil er sich nicht einlassen kann auf die Erkenntnis dieses Pochens Kants auf die Gewißheit gewisser Urteile."
      ],
      [
        "Aber an dem Wolffianismus, seinem Inhalte nach, war Kant irre geworden durch das Studium von Hume, dem englischen Philosophen, der ein bloßer Erfahrungsphilo- soph sein wollte.",
        "Und er sagte sich, eben unter dem Ein- fluß Humes: So etwas, wie eine Wirklichkeit herausspin- nen aus der Vernunft, das gibt es ja nicht; es gibt eigent- lich nur eine Erfahrung. - Das war die zweite Seite."
      ],
      [
        "Gewißheit muß es geben auf der einen Seite; aber alles, was in der Erfahrung auftritt, was die einzige Grundlage für wirkliches Erkennen ist, das liefert keine Gewißheit.",
        "Wie kommt man aus diesem Dilemma heraus?"
      ],
      [
        "Und das ganz zwangsmäßige Suchen, aus diesem Dilemma heraus- 37 zukommen, das ist im Grunde genommen der Haupt- impuls des Kantischen Denkens.",
        "Ich habe das ausführlich dargestellt in meiner Schrift «Wahrheit und Wissenschaft» und habe es noch durchleuchten lassen in meiner «Philo- sophie der Freiheit», wie eigentlich Kants Suchen nicht darauf hinauslief, irgend etwas wesentlich zu erkennen, sondern zu fragen: Wie kommt man zu einer absoluten Gewißheit?"
      ],
      [
        "Das Kantsche Problem ist kein Wahrheitsproblem, ist kein Erkenntnisproblem, sondern ein Gewißheitsproblem.",
        "Und wenn man es nicht als ein Gewißheitsproblem faßt, kann man es eigentlich nicht verstehen.",
        "Die Lösung wird von Kant dadurch gesucht, daß er sagt: Zum Herausspin- nen von Wirklichkeitsurteilen aus der Vernunft ist die Menschenseele allerdings nicht geeignet, aber diese Urteile kommen doch zustande; sie werden, wie man zum Beispiel in der Mathematik sieht, angewendet auf die äußere Er- fahrung."
      ],
      [
        "Wir schauen solche Figuren (es wird gezeichnet) nicht bloß an, sondern wir schauen sie mathematisch an und sagen: Es sind zwei Dreiecke oder, anders gezeichnet, es ist ein Sechseck.",
        "Wir vermischen das, was wir innerlich aus der Vernunft herausspinnen, mit dem, was uns durch die äußere Erfahrung kommt."
      ],
      [
        "Wir stülpen das innerlich a priori Erkannte über das a posteriori, von außen Er- fahrene hinüber.",
        "So kam Kant dazu, zu sagen: Wahrheitserkenntnis kann allerdings aus der Vernunft nicht gewonnen werden.",
        "Aber die menschliche Vernunft wird auf die Erfahrung ange- wendet."
      ],
      [
        "Sie stülpt ihr Urteil über die äußere Erfahrung hinüber.",
        "Sie macht selbst ihr Urteil über die äußere Er- fahrung.",
        "Weil Kant sagte: Gewißheit muß es geben in der Philosophie, Gewißheit muß man finden können, aber man findet sie nicht, wenn man sie in Wolffischer Weise sucht, wenn man glaubt, man könne eine Wirklichkeit in der Vernunft gewinnen und daneben die Erfahrung neben- herlaufen lassen , weil Kant das nicht zusammenbringen konnte, so sagte er: Der Mensch spinnt eben aus seiner Vernunft das heraus, was die Erfahrung dann in sich auf- nimmt; der Mensch macht selber die Erkenntnis; die Dinge der Erfahrung sind deshalb gewiß und insofern gewiß, als wir sie aus unserem Geiste heraus gewiß machen."
      ],
      [
        "Sie sehen, eigentlich ist damit das Wesen der Erkenntnis entthront.",
        "Eigentlich ist damit die Erkenntnis beseitigt.",
        "Und sie ist auf scharfsinnige Weise beseitigt, so scharfsin- nig, daß die Kantianer sich bis heute an diese Scharfsinnig- keit halten und nicht merken, was eigentlich darinnensteckt."
      ],
      [
        "Kommt dann ein Mensch wie Ludwig Haller, der da fühlt, wie eigentlich das Kantische Denken ganz abkam von der Wirklichkeit, wie es im Unwirklichen nach der Gewißheit schnappt, dann findet er eben Worte, wie ich sie Ihnen mitgeteilt habe.",
        "Er findet, daß da menschlicher Scharfsinn angewendet wird auf ein unmögliches Problem, auf ein Problem, das dem Menschen die Erkenntnis nicht aufhellt, sondern mit Nebel umhüllt."
      ],
      [
        "Deshalb sagt Ludwig Haller, wie er es empfindet: Diese Misosophie versucht zu stehlen ihre Waffen aus dem Arsenal des Lichtes und verwendet sie im Dienste der Finsternis.",
        "Aber auf der anderen Seite muß man auch einsehen, wie diese ganze Entwickelung der neueren Zeit im Grunde genommen notwendig war."
      ],
      [
        "Was sich heraufentwickelt hat an menschlichem Denken und menschlichem Forschen seit der Griechenzeit, war nicht eine Entwickelungslinie, die man nur so verfolgen kann, wie ich es jetzt eben getan habe, sondern die man auch nach einer anderen Seite ver- folgen kann.",
        "Auch darauf habe ich in meinen «Rätseln der Philosophie» hingedeutet."
      ],
      [
        "Wir stehen heute vor einer 39 Naturerkenntnis, welche das Naturphänomen rein aufzu- fassen versucht.",
        "Man kann allerdings sagen: Gerade derjenigen Natur- erkenntnis, die heute immerdar besonders damit prunkt, daß sie das Naturphänomen rein auffaßt, gelingt es kaum, das Naturphänomen rein aufzufassen, das heißt, es nicht mehr, gar nicht mehr zu durchdringen mit dem Gedanken- gewebe desjenigen, was nur im Begriffe, innerlich subjek- tiv, gemacht ist. - Es werden ja noch immer über den äußeren Phänomenverlauf allerlei Hypothesen aufgestellt, nicht nur berechtigte, sondern unberechtigte."
      ],
      [
        "Aber ein Mensch hat doch in der neueren Zeit scharf betont, und zwar verhältnismäßig früh, daß diese neuere Zeit in bezug auf das Betrachten der äußeren natürlichen Vorgänge nach dem reinen Phänomen, nach der reinen Phänomenologie hinstreben muß.",
        "Und das war Kants Antipode Goethe."
      ],
      [
        "Er hat verlangt, daß die Phänomene, die Erscheinungen rein sich selbst aussprechen.",
        "Er hat scharf betont, daß dasjenige, was sich in der Verstandesentwicke- lung abspielt, durchaus ferne bleiben muß demjenigen, was man als Beschreibung der Phänomene und des phänomena- len Verlaufs selber hinstellt."
      ],
      [
        "Und in allerschärfster, in bewunderungswürdiger Weise fordert Goethe wiederholt diesen reinen Phänomenalismus.",
        "Aber je mehr man diesem reinen Phänomenalismus zustrebt, desto mehr muß man nach einer besonderen Eigen- tümlichkeit der Begriffswelt streben."
      ],
      [
        "Und diese Eigentüm- lichkeit der Begriffswelt ist auch in hohem Grade erreicht.",
        "Diese Eigentümlichkeit ist eine durchaus berechtigte für ein gewisses Zeitalter der menschlichen Entwickelung.",
        "Wer sich nicht allein darauf beschränkt, die Philosophie zu stu- dieren seit dem Zeitalter des Cartesius, sondern wer ein Organ dafür hat, auch einzugehen auf die guten Seiten 40 scholastischer Philosophie, mittelalterlicher Philosophie, und wer Aristoteles und Plato nicht durch die Brille der modernen Philosophie-Geschichtsschreiber sieht, sondern sie in ihrer ursprünglichen Gestalt vor seine Seele stellen kann, der weiß, daß die Art und Weise, wie die Begriffs-, die Vorstellungswelt in der menschlichen Seele lebt, heute eine ganz andere ist als im griechischen Altertum und selbst noch im scholastischen Mittelalter."
      ],
      [
        "Im scholastischen Mit- telalter fühlte noch die Seele, daß, indem sie den Begriff erlebte, in diesem Begriff etwas von Substantialität lag, so wie in dem Rot, in dem Blau, das man als Wahrnehmung hat, noch etwas von Substantialität liegt.",
        "In der neuesten Zeit erst ist der Begriff zum vollständigen Abbild gewor- den."
      ],
      [
        "In der neuesten Zeit erst ist der Begriff seines Inhaltes völlig entleert.",
        "In der neuesten Zeit erst ist in der Mensch- heitsentwickelung und in der Philosophie möglich gewor- den, was ich in meiner «Philosophie der Freiheit» das reine Denken genannt habe."
      ],
      [
        "Wenn man das Freiheitsproblem zu belauschen sucht, so wie ich es versuchte in meiner «Philosophie der Frei- heit», lernt man zu gleicher Zeit diesen neuzeitlichen Cha- rakter des Denkens kennen.",
        "Man lernt dasjenige Denken kennen, welches im Grunde genommen alles äußeren Er- fahrungsinhaltes entleert ist, heranerzogen ist zwar an diesem äußeren Erfahrungsinhalt, aber doch nur als sub- jektive Tatsache lebt."
      ],
      [
        "Von diesem reinen Denken kann man ebensogut sagen, und ich habe das in der Neuauflage meiner «Philosophie der Freiheit» deutlich durchmerken lassen, daß es im Be- reiche des Wollens vor sich geht.",
        "Aber es ist das Wollen zum Denken ummetamorphosiert, wie man sagen kann."
      ],
      [
        "Es ist das Ergebnis desjenigen Denkens, das alle äußere Erfahrung abgestreift hat.",
        "Dieses reine Denken ist nur mehr Bild, und ist ganz Bild.",
        "Und man muß, wenn man überhaupt zu einem philosophischen Verständnis in unse- rem Zeitalter kommen will, den Boden erreichen, auf dem man dieses reine Denken hat."
      ],
      [
        "Goethe hat gefühlt, was in diesem reinen Denken liegt.",
        "Die anderen können es ihm nur nachfühlen.",
        "Daher zitieren sie einen Goetheschen Ausspruch immer falsch, der etwa sagt, der gütige Gott habe ihn davor bewahrt, «über das Denken zu denken»."
      ],
      [
        "So wie Goethe das meint, so ist es schon richtig.",
        "Goethe hat niemals «über das Denken ge- dacht», weil man allerdings mit dem Denken, in das man sich eingewöhnt hat, dieses reine Denken nicht erreichen kann."
      ],
      [
        "Man muß es als Bild anschauen.",
        "So daß man sagen kann: Das Denken selber, das man erkennen will, das reine Denken, wird zu einem Anschauen dieses reinen Denkens.",
        "Nicht dialektisch, aber anschaulich ist das reine Denken zu erreichen."
      ],
      [
        "Man kommt zu diesem Punkt philosophischer Entwickelung an dem Freiheitsproblem, weshalb die Frei- heit, wirkliche Freiheit, gar nicht möglich ist ohne die Errei- chung dieses reinen Denkens, das bloßes Bild ist.",
        "Solange eine Realität in uns unser Handeln motivieren würde, so lange kann unser Handeln nicht frei sein."
      ],
      [
        "Da- her ist kein instinktives, kein traditionelles Handeln, kein Handeln unter einem Gewohnten wirklich frei, sondern allein ein Handeln, welches den Bildern, die im reinen Denken weben, folgen kann.",
        "Sobald man einer Realität folgt, wird man gestoßen."
      ],
      [
        "Wenn man frei sein will, muß man in seinen Willen das Irreale aufnehmen.",
        "Wenn Sie sich irgendwie anstoßen, so fühlen Sie, daß der Gegenstand auf Sie eine Wirkung hat.",
        "Wenn Sie unter einem Instinkt, unter einem Triebe eine Handlung vollbringen, so müs- sen Sie fühlen, daß da etwas stößt, daß da keine Freiheit vorliegt."
      ],
      [
        "Wenn Sie aber vor einen Spiegel treten, das Bild im Spiegel sehen, so werden Sie sich klar sein darüber, daß das Spiegelbild Ihnen niemals eine Ohrfeige geben kann, daß das Spiegelbild Ihnen niemals einen Stoß geben kann.",
        "Das Bild kann nichts machen von sich aus."
      ],
      [
        "Der muß machen, der muß handeln, der diesem Bilde gegenüber- tritt.",
        "Da aber das Bild nichts macht, so wird die Hand- lung dann zu einer freien Handlung.",
        "So kann nur ein Denken, das nicht im Realen wurzelt, sondern das reines Bild ist, ein freies Handeln motivieren."
      ],
      [
        "Deshalb erlauscht man an dem Problem der Freiheit das Problem des moder- nen Denkens, des reinen Denkens.",
        "Aber man steht in die- sem Denken in einer Bilderwelt darinnen.",
        "Die moderne Philosophie, alles, was in dieser modernen Philosophie durch Kant und die Kantianer lebt, das kommt instinktiv, obwohl es zumeist dieses reine Denken nicht begreift, an dieses reine Denken heran."
      ],
      [
        "Man muß eben, wenn man in der modernen Zeit anfängt zu denken und sein Denken schult an der Naturwissenschaft, die für sich alle Autorität in Anspruch nimmt und die nicht wirkliche Naturwissenschaft, wirkliche Realitätswissenschaft wäre, wenn sie etwas anderes in uns hereinstopfte als nur Bilder, man muß, wenn man sein Denken in dieser Richtung bewegt, sich zunächst einem Irrealen nähern.",
        "Wir haben in dem Denken, durch dessen Eigentümlichkeiten wir durchgehen mit unserer modernen philosophischen und wissenschaftlichen Entwickelung, keine Realität, wir haben bloßes Bild einer Realität."
      ],
      [
        "Und indem wir auf dieses Den- ken hinblicken, kommen wir auf der einen Seite zu dem Problem, das die neueren Erkenntnistheoretiker bewegt.",
        "Sie möchten die Brücke schlagen von dem, was inner- lich erlebt wird, zu dem, was äußerlich im Sein besteht."
      ],
      [
        "Sie merken nicht, daß sie gar nicht von einer Realität zur anderen zunächst die Brücke schlagen, sondern von 43 etwas, was in Bildern lebt, zu etwas, was Realität sein soll.",
        "Und auf der anderen Seite kommen wir dazu, daß die gewissenhaften Naturdenker sich gestehen: mit diesem irrealen Denken, mit diesem Denken, das im Bildcharakter aufgeht, können wir doch nicht untertauchen in die Reali- tät."
      ],
      [
        "Der Punkt, «wo Materie spukt», ist damit nicht zu er- reichen.",
        "Denn man webt in Bildern.",
        "Die moderne Philoso- phie webt in Bildern, weiß es nicht und sucht die Realität in diesen Bildern.",
        "Daher die Empfindung einer «Misosophie» bei Ludwig Haller, daher das Gefühl, man komme nicht in die Wirklichkeit hinein, wenn man sich in diesem Denken bewegt."
      ],
      [
        "Das ist das Problem der neueren philosophischen Ent- wickelung: daß notwendigerweise die Menschheitsgeschichte zu einem reinen Erfassen des irrealen bildhaften Denkens treiben mußte.",
        "Um der Entwickelung der Freiheit willen mußte die moderne Menschheit sich zu diesem irrealen bildhaften Denken erheben."
      ],
      [
        "Aber man kann in ihm nicht bleiben, wenn man ein Vollmensch ist, wenn man die Realität in allem menschlichen Wesen fühlt.",
        "Denn man muß den Widerspruch fühlen zwischen dem, was da drängt und lebt und webt in dem menschlichen Wesen, und dem, was vor dem Bewußtsein steht als ein bloßer Umkreis von irrealen Bildern."
      ],
      [
        "Wir haben es nicht bloß mit einem logisch formalen Problem zu tun, wir haben es mit einem realen Problem zu tun, mit einem realen Problem, das sich dadurch ergeben hat, daß der Mensch allmählich sein Denken, sein Vorstellen herausgezogen hat aus der äußeren Wirklichkeit.",
        "Es ist ihm die dunkle, finstere Materie, die er nicht be- greifen kann, in der Außenwelt übriggeblieben."
      ],
      [
        "Aber sein Denken ist nicht eine Realität geworden, es ist Bild ge- 44 worden.",
        "Und er muß weitergehen in diesem Bilde.",
        "Das Denken, das heute bloßes Bild ist, war für den Griechen noch Wahrnehmungsinhalt.",
        "Dieses Denken hat sich bewegt in der Richtung von außen nach innen."
      ],
      [
        "Es schreitet so vor, daß der Mensch erst denkend untertaucht in die äußere Welt.",
        "Jetzt ist er mit seinem Philosophieren auf dem Punkte, wo er in dem aus der äußeren Welt herausgeschäl- ten Denken webt.",
        "Er muß in dieser Richtung weitergehen."
      ],
      [
        "Er muß die Realität wieder suchen.",
        "Die Materie hat dem Menschen in alten Zeiten und bis in unser Zeitalter die Stütze für das Denken gegeben, indem sie ihm das Denken real gemacht hat.",
        "Das Denken aber ist, weil es die Grund- lage werden mußte für die Entwickelung der menschlichen Freiheit, in den Bildcharakter übergegangen."
      ],
      [
        "So schwebt es zwischen der Außenerfahrung und dem Innenerlebnis.",
        "Es muß untertauchen in dieses Innenerlebnis.",
        "Es muß wie- derum Realität bekommen.",
        "Der Mensch muß mit vollem Bewußtsein eintauchen in die Regionen, bei denen es Eduard von Hartmann und mit ihm allen modernen Phi- losophen so schwül wird, weil die Gedanken ihnen schei- nen anzufangen, wie Kobolde zu tanzen."
      ],
      [
        "Wenn der Mensch mit seinem Denken aus dem Bild- charakter herausgeht wo es ihm allerdings, wenn er drin- nen webt und lebt, weil es bloß Bilder sind, nicht so schwül zu werden braucht -, wenn er heraustritt und hineintritt in die eigene Realität, dann muß er allerdings durch die Übungen der Geisteswissenschaft die Möglichkeit in seine inneren Fähigkeiten aufnehmen, sich in diesem Selbstleben der Begriffswelt umzutun, wie sonst im mathematischen Denken.",
        "Er muß die Fähigkeit erwerben, die Wirklichkeit in diesem Selbstleben selbständig zu erfassen."
      ],
      [
        "Wie es einem ja auch nicht schwül wird, wenn die Dinge da draußen im Räume nicht stillstehen - damit unsere Erkenntnis nicht 45 beunruhigt werde -, sondern wenn sie, sich bewegend, lau- fen, so muß der Mensch im Aufsteigen zur Geist-Erklä- rung, zur Geistoffenbarung fähig werden, seinem Bild- begriff wiederum einen Inhalt zu geben.",
        "Erfaßt man an diesem Punkt das eigentliche, das drän- gende philosophische Leben der Gegenwart, dann kommt man von all den Redereien ab, daß der Philosoph nicht einsehen könne, was der Geistesforscher sagt."
      ],
      [
        "Er kann es einsehen, sobald er den Bildcharakter seines Denkens ein- gesehen hat, sobald er aber auch eingesehen hat, daß das Denken zu diesem Bildcharakter gekommen ist, weil es sich weltgeschichtlich in der Richtung von außen nach in- nen bewegt, von der Richtung des Geistes in der Materie zu der Anschauung der reinen geistigen Welt.",
        "In dieser Weise muß Philosophie fortgeführt werden, indem sie in Empfang genommen wird von der Geistes- wissenschaft, von der Geisteserforschung, indem das Den- ken eingetaucht wird in dasjenige, was die Geisteswissen- schaft, die Geistesforschung zu sagen hat."
      ],
      [
        "Das ist es, was ich Ihnen, wenn auch nur skizzenhaft mit einigen Linien darstellen wollte: in welcher Art befruchtet werden soll Philosophie von der Geisteswissenschaft.",
        "In den nächsten Tagen soll dann davon gesprochen werden, wie andere Zweige des menschlichen Denkens und Tuns von dieser Geisteswissenschaft befruchtet werden sollen."
      ],
      [
        "Schlußwort zur Disputation über Philosophie Dornach, 4.",
        "April 1921 Es sind im Laufe der Disputation Fragen aufgetaucht, die fachgemäß natürlich eine breite Aussprache erforderten.",
        "Ich möchte nur, weil wir ja an einem Abend nicht alles erörtern können, einige Andeutungen methodologischer Art geben, die mir bezüglich der Fragen, die auftauchten, und die, wie es mir wenigstens schien, nicht ganz klar for- muliert waren, nötig scheinen, um in die Richtung zu wei- sen, in der gewisse Lösungen solcher Fragen gesucht wer- den müssen."
      ],
      [
        "In Anbetracht solcher Fragen wie etwa der nach der «Subjektivität der Wahrnehmung», liegt in der jüngsten philosophischen Entwickelung ein vielfaches Konfundie- ren der Vorstellungen vor, ein Anhäufen von Begriffen, die eher die Probleme verdunkeln und verknäueln, als daß sie sie erhellen und zu einer gewissen Lösung führen würden.",
        "Es handelt sich nämlich in dem Augenblick, wo man Fragen aufwerfen will, die das Verhältnis von Objekt und Subjekt im Wahrnehmen vorstellend und erkenntnisgemäß betreffen, immer darum, durch eine sorgfältigste Analyse desjenigen, was der Tatbestand ist, darauf zu kommen, wie die Fragen eigentlich gestellt werden müssen."
      ],
      [
        "Denn oft werden schon die Fragen aus irrtümlich gerichteten Vor- stellungen falsch formuliert.",
        "Und so ist es vielfach mit den Fragen nach der «Subjektivität der Wahrnehmung».",
        "Da wurde auf die Schwierigkeit mit dem partiell Far- benblinden hingedeutet, von dem vorausgesetzt ist, daß er 47 eine, sagen wir, grüne Landschaft anders sehe als der so- genannte normal Sehende."
      ],
      [
        "In dieser Vorstellung des par- tiell Farbenblinden liegt die Schwierigkeit vor: inwieweit muß man dem, was nun auch der sogenannte normal Se- hende, ich sage ganz ausdrücklich: der sogenannte normal Sehende, sieht, Subjektivität beimessen?",
        "Nun, da handelt es sich darum, daß man sich zunächst das ganze Problem so vor Augen führen kann, daß es rich- tig erscheint."
      ],
      [
        "«Richtig» bedeutet, daß die Art, wie man die Elemente, die zur Problemstellung zusammengeführt wer- den müssen, daß man dieses Wie des Zusammenführens in der rechten Weise bewirkt.",
        "Nehmen Sie nur einmal an, wenn irgend jemand sagt: Ja, die Außenwelt, die mir also, sagen wir, in einer grünen Landschaft mit einer grünen Tingierung erscheint, gibt mir Veranlassung dazu, nachzu- denken, ob nun die Qualität «grün» objektiv ist, ob ich sie der Welt der Objektivität zuschreiben dürfe, oder ob sie als subjektiv angesprochen werden müsse."
      ],
      [
        "Dann muß man sich, um überhaupt zur Problemstellung zu kommen, solche Dinge überlegen, wie zum Beispiel dieses: Ja, wie verhält sich nun die Sache, wenn ich irgend etwas, was meinetwillen weiß oder gelb ist, durch eine grüne Brille ansehe?",
        "Da sehen wir es grün tingiert."
      ],
      [
        "Ist das nun der Sphäre der Objektivität zuzuschreiben, oder hat man da von Subjektivität zu sprechen?",
        "Man wird sehr bald be- merken, daß man ganz gewiß nicht dem, was da draußen ist, dieses Grün, das ich durch eine grüne Brille sehe, wird zuschreiben dürfen."
      ],
      [
        "Man wird nicht von Objektivität in bezug auf die äußere Umwelt sprechen können.",
        "Aber man wird doch auch ganz gewiß nicht davon sprechen können, daß diese grüne Tingierung, die ich da herausbekommen habe durch eine grüne Brille, auf irgend etwas Subjektivem beruht."
      ],
      [
        "Sie ist durchaus gesetzmäßig objektiv bedingt, 48 ohne daß dasjenige, was ich hier als grün bezeichne, wirk- lich grün ist.",
        "Sie sehen, ich stelle damit, daß ich mir eine Vorstellung bilde, ich möchte sagen, das Problem in ein besonderes Licht hin, wo ich dasjenige, was ganz gewiß nicht der Außenwelt angehört, doch objektiv, als auf objektive Art entstanden nehmen muß; denn die Brille gehört nicht zu mir, kann also ganz gewiß nicht in die Sphäre der Subjek- tivität einbezogen werden."
      ],
      [
        "Solche Dinge könnten sogar sophistisch erscheinen.",
        "Und dennoch sind solche Sophismen sogar sehr häufig das, was einen darauf bringt, die Ele- mente, die einen darauf führen sollen, die Fragen in ent- sprechender Weise zu stellen, auch zusammenzubringen."
      ],
      [
        "Man wird nämlich, wenn man solche scheinbaren Sophis- men in der richtigen Weise durchschaut, die ganze Faden- scheinigkeit der Alltagsbegriffe «Subjekt» und «Objekt», die allmählich in die moderne philosophische Betrachtung hineingebracht worden sind, durchschauen.",
        "Und man wird, wenn man in eine richtige Fragestellung hineinkommt, wohl immer mehr und mehr zu dem Weg, wie ich glaube, geführt werden, den ich in meinen Schriften «Wahrheit und Wissenschaft» und «Philosophie der Freiheit» ein- geschlagen habe, wo man überhaupt zunächst nicht den Ausgangspunkt nimmt von den Begriffen «Subjekt» und «Objekt», sondern wo man unabhängig von diesen Be- griffen etwas sucht, was über die Sphäre der Subjektivität und Objektivität hinaus gelegen sein muß: das ist die Funktion des Denkens."
      ],
      [
        "Die Funktion des Denkens!",
        "Wenn man die Sache un- abhängig durchschaut, erscheint einem das Denken eigent- lich über das Subjektive und Objektive durchaus hinaus- liegend.",
        "Und damit hat man einen Ausgangspunkt gewon- nen, von dem aus man dann auch in entsprechender Weise 49 da geführt werden kann, wo es sich um das solche Schwie- rigkeiten bietende Problem der «Subjektivität» und «Ob- jektivität» handelt."
      ],
      [
        "Denn man wird dann dazu geführt und Sie werden diesen Weg in diesen meinen beiden Büchern durchaus eingehalten finden -, nicht zu fragen: Wie wirkt eine äußere «objektive» Welt auf irgendeine «subjektive» Welt, für die etwa der Vermittler, sagen wir, das Auge ist? sondern man wird zu etwas ganz anderem geführt.",
        "Man wird nämlich dazu geführt, sich zu fragen: Wie ist denn die Tatsache der Sinne selber?"
      ],
      [
        "Welche Wesen- haftigkeit zeigt einem der Sinn?",
        "Also zum Beispiel die Konstitution des Auges?",
        "Man wird dann finden, daß in dem Problem, das man sich so stellt, etwas zutage tritt, das ich jetzt, weil ich kurz sein muß - es könnte natürlich in einer stundenlangen Erläuterung auch mit dem adäquaten Begriff umfaßt wer- den , durch einen Vergleich klarmachen will: Ich kann auch durch eine Brille schauen und dennoch die Umwelt so sehen, wie das naive Bewußtsein sie als wirklich empfin- det, mit ihren Farbentingierungen, mit allen ihren Sinnes- qualitäten."
      ],
      [
        "Ich muß nur durch eine farblos-durchsichtige Brille schauen; ich darf nicht durch eine Brille schauen, die mir die Außenwelt selber verändert.",
        "Und ich muß mich jetzt hineinfinden in den Unterschied zwischen einer die äußere Tingierung verändernden Brille und einer farblos durchsichtigen Brille, die jede äußere Tingierung vermei- det."
      ],
      [
        "Von diesem Vergleich aus wie gesagt, es könnten langatmige Überlegungen anstelle des Vergleichs gesetzt werden - werde ich finden: wenn ich die Einrichtung des sogenannten normalen Auges nehme, habe ich in ihm eine Einrichtung gegeben, die sich gerade als durchsichtig er- weist, die sich vergleichen läßt mit dem durchsichtig-farb- losen Glase.",
        "Ich finde nichts im normalen Auge, was dar- auf hinweist, daß die Außenwelt qualitativ in irgendeiner Weise verändert wird."
      ],
      [
        "Aber ich muß diese Untersuchung anstellen nicht mit den gewöhnlichen Begriffen, die ich im alltäglichen Bewußtsein habe, sondern mit dem imagina- tiven Bewußtsein, das wirklich in die Einrichtungen des Auges eindringen kann.",
        "Für das imaginative Bewußtsein ist ein sogenanntes nor- males Auge ein durchsichtiges Organ."
      ],
      [
        "Ein Auge, das par- tiell farbenblind ist, das erweist sich für das imaginative Bewußtsein als in einer gewissen Weise vergleichbar mit einer farbigen Brille, als etwas, das allerdings eine Ver- änderung vornimmt in dem «Subjekt».",
        "So kommt man indem man die Subjektivität aber in einer höheren Auffassung auffaßt - gerade darauf, die Sinnesapparate im weitesten Umfange als dasjenige an- zusehen, was sich vergleichen läßt mit dem Durchsichtigen, was gerade so eingerichtet ist, daß es die eigene Produk- tion der Sinnesqualitäten in sich aufhebt."
      ],
      [
        "Man lernt als eine reine Phantasterei die Vorstellung erkennen, als ob in diesem ideell Durchsichtigen - das gerade so eingerichtet ist, daß es irgendeine Produktion der Sinnesqualitäten in sich aufhebt -, in diesem ideell durchsichtigen Sinnesappa- rat irgend etwas auftreten könnte, was Sinnesqualitäten erst hervorriefe, was zu etwas anderem da wäre als den Sinnesqualitäten den Durchgang zu lassen.",
        "Wie gesagt, ich will nur auf die Richtung deuten."
      ],
      [
        "Und ich will zu gleicher Zeit darauf hinweisen, daß sich das gewöhnliche Philosophieren auf den Punkt stellen sollte, zu sagen: Die Tatsachen der Welt erweisen sich, wenn ich sie vorurteilslos untersuche, so, daß sie mir Ergebnisse lie- fern, die einfach unauflösbar sind für das gewöhnliche Verstandesbewußtsein; die Tatsachen selber zeigen mir, daß ich hinausgehen muß über dieses gewöhnliche Ver- 51 standesbewußtsein. - Ehrlich ist es nicht, aus, sagen wir, der Tatsache des partiell Farbenblinden auf die Subjekti- vität der Farbenqualitäten zu schließen.",
        "Denn jedes solche Schließen hat irgendeinen logischen Fehler in sich, der im- mer irgendwie nachweisbar ist."
      ],
      [
        "Ehrlich wäre es, zu sagen: Man kommt einfach mit dem gewöhnlichen Philosophieren zu keinem Resultat, wenn man die Schwierigkeit, die sich aus dem Vergleich der partiellen Farbenblindheit mit dem Sehen des sogenannten normalen Auges ergibt, lösen will. - Das gewöhnliche Bewußtsein hat eben in diesem Punkte die Aufgabe, die Schwierigkeiten hinzustellen und zu sagen: Da sind sie. - Und würde man sich wirklich der Tragweite der Logik bewußt werden, des real-logischen Denkens innerhalb des Bewußtseins, so würde man über- all, ich möchte sagen, hinlegen die Probleme und würde sagen: Da ist wiederum eins, unauflösbar für das gewöhn- liche Bewußtsein, das zweite, das dritte - und würde sehen, daß die gewöhnliche Philosophie in vieler Bezie- hung nichts weiter ist als ein Hinweis auf Probleme und eine Hervorbringung einer Stimmung des Wartens, daß diese Probleme von einer höheren Stufe des Bewußtseins aus gelöst werden.",
        "Es ist nur der Drang, mit dem gewöhn- lichen Bewußtsein zurechtzukommen, der einen Nebel über die Probleme breitet und der nicht zugeben möchte, daß man mit ihm die Probleme nur aufwerfen kann und hin- weisen muß darauf, daß nun die menschliche Seele eine Entwickelung und Übungen durchmachen muß, diese Pro- bleme zu lösen."
      ],
      [
        "Das Gesetz der spezifischen Sinnesenergien ist eben durchaus nicht etwas, das innerhalb des gewöhn- lichen Bewußtseins behandelt werden kann.",
        "Wie gesagt, ich wollte nur auf den Hauptpunkt der Er- örterungen hinweisen, über das Thema der Farben, wollte darauf hinweisen, daß vor allen Dingen der Philosophie 52 und auch philosophischen Physiologie, Philologie und so weiter, in der Gegenwart notwendig wäre ein ganz gewis- senhaftes Umgrenzen desjenigen, was sie durch ihr Denken eigentlich vor das gewöhnliche Bewußtsein hinträgt."
      ],
      [
        "Das ist das eine, auf das ich aufmerksam machen möchte, wie gesagt, ganz unzulänglich.",
        "Denn es sollte nur auf eine bestimmte Richtung weisen; aber mehr kann auch nicht in einer so kurzen Erörterung getan werden."
      ],
      [
        "Das zweite, worauf ich hinweisen möchte, ist - wie- derum in bloß methodologischer Beziehung - das hier auf- geworfene Problem der Kategorien.",
        "Man könnte natürlich über das Kategorienhafte des menschlichen Denkens viele Stunden reden, allein ich möchte da zunächst nur auf das eine hinweisen: Innerhalb der eigentlichen Kategorientafel kommen die «Subjektivität» und die «Objektivität» gar nicht vor."
      ],
      [
        "Und daß innerhalb der eigentlichen Kategorien- tafel, der eigentlichen, der Urkategorientafel, «Subjekt» und «Objekt» gar nicht vorkommen, das bildet an sich eine Art von Beweis über das Wesen des kategorialen Den- kens: Wenn man die Kategorien in der Weise nimmt, wie sie nun nicht aus irgendeinem Beweis hervorgehen, sondern einfach, ich möchte sagen, aus der Logik herausgelöst wer- den, so müssen sie, indem man sie aufstellt, anwendbar sein auf dasjenige, was über «subjektiv» und «objektiv» erhaben ist.",
        "Es muß das, worauf die Kategorien zunächst anwendbar sind, ein Übersubjektives und -objektives sein."
      ],
      [
        "Damit aber nun, daß die Kategorien durch den Menschen selbst angewendet werden, ist ein klarer Beweis gegeben, daß im kategorialen Denken nicht ein Subjektives gegeben ist, sondern ein Subjektiv-Objektives.",
        "Es ist dies das Problem, über das auch Goethe so sehr viel gedacht hat."
      ],
      [
        "Und die Art und Weise seines Denkens, die ihn dazu führte, immer den Punkt aufzusuchen, wo 53 Subjektivität und Objektivität für den Menschen im menschlichen Erleben verschwinden, sich aufheben, dieses Bestreben machte ihn eigentlich zu dem Antipoden Kants.",
        "Es ist selbstverständlich durchaus richtig, daß man, wie gesagt wurde, auch im positiven Sinne aus Kant heraus arbeiten könnte; aber man kann aus allem in der Welt in positiver Weise heraus arbeiten, auch, aus dem größten Irrtum!"
      ],
      [
        "Denn es gibt nichts in der Welt, woraus man nicht auch ein Positives herausschälen kann.",
        "Wir haben unter den Grundübungen - ich brauche nur daran zu erinnern: im zweiten Teil meiner «Geheimwissenschaft im Umriß» finden Sie die Sache besprochen - für den, der etwas zur höheren Erkenntnis kommen will, gerade diese Positivität angeführt, dieses Aufsuchen des Positiven."
      ],
      [
        "Das darf einen natürlich nicht blind machen für die Anerkennung von Abirrungen.",
        "Und schließlich, wenn wir das Historische ins Auge fassen, so können wir sagen: Positiv ist aus Kant sehr viel herausgearbeitet worden."
      ],
      [
        "Es gibt ja nicht nur die kritischen Kant-Philologen, nicht nur die Neukantianer vom Schlage Liebmanns, Volkelts und so weiter, sondern es gibt gerade die in dieser Beziehung sehr tätige Marbur- ger Schule Cohen, Cassirer, Dilthey und so weiter , die versuchte, in gewisser Beziehung aus Kant positiv heraus- zuarbeiten.",
        "Nun, ich habe gezeigt, wie wenig zu einer wirklichkeits- gemäßen Anschauung dieses «positive Herausarbeiten aus dem Kantianismus» führen kann: in meinen «Rätseln der Philosophie», wo ich kurz auch diese Bestrebungen der Marburger Schule besprochen habe."
      ],
      [
        "Also auch beim Kate- gorienproblem handelt es sich darum, es richtig in seiner ganzen inneren Wesenheit vor die Seele hinzustellen, um zu sehen, wie gerade durch das Kategorienproblem die Frage nach dem «Subjektiven» im Gegensatze zum «Ob- 54 jektiven» nicht so gestellt werden kann, wie es unter dem Einfluß des Kantianismus die neuere Philosophie getan hat.",
        "Dieses geradezu erkenntnistheoretische Einspannen in die Subjektivität ist etwas, was zahllose ungerechtfertigte Vorstellungen in unsere moderne Philosophie hinein- gebracht und uns Vorstellungen hat verlieren lassen, die schon da waren, und die in entsprechender gerader Fort- entwickelung zu etwas recht Fruchtbarem hätten führen können."
      ],
      [
        "Ich muß da immer wieder und wiederum darauf auf- merksam machen was ich ja schon öfter getan habe , wie ein außerordentlich begabter Philosoph des 19.",
        "Jahr- hunderts, Franz Brentano, 1874 den ersten Band seiner «Psychologie» hat erscheinen lassen."
      ],
      [
        "Es ist im Grunde ein geistvolles Buch.",
        "Dieser Band «Psychologie» von Brentano erschien im Frühling 1874.",
        "Für den Herbst desselben Jah- res versprach er den zweiten Band.",
        "In kurzer Zeit sollten dann die drei folgenden Bände erscheinen."
      ],
      [
        "Auf fünf Bände hatte Brentano zunächst diese «Psychologie vom empi- rischen Standpunkte» berechnet.",
        "Der erste Band war nur eine Vorbereitung.",
        "In ihm findet sich aber doch eine höchst merkwürdige Stelle, in der darauf hingedeutet wird, wie Franz Brentano in der Tat auf die bedeutsamsten psycho- logischen Probleme hinzielte."
      ],
      [
        "Er sagt da: Wenn wahrhaftig alles moderne Denken nur dazu führen sollte, zu unter- suchen, wie Vorstellungen auf- und niedersteigen, sich mit- einander vergesellschaften, wie sich das Gedächtnis bildet und dergleichen, und wenn man darüber nur zur Unge- wißheit kommen könnte über die eigentlichen psychologi- schen Fragen eines Plato und Aristoteles, zum Beispiel, ob die Seele erhalten bleibe, wenn ihr äußerer physischer Leib zerfällt, dann hätte man durch die moderne Wissenschaft- lichkeit wahrhaftig für die Bedürfnisse des Menschen nicht 55 viel gewonnen! - Nun, man kann aus allem anderen, was Brentano da andeutet im ersten Bande seiner «Psychologie vom empirischen Standpunkte», schon ersehen, wie er durch seine fünf Bände hindurch das Problem bis zu diesen Grundfragen des Plato und Aristoteles bringen wollte.",
        "Das Merkwürdige ist, daß im Herbst der zweite Band nicht erschien."
      ],
      [
        "Er erschien auch im nächsten Jahr nicht.",
        "Und in den neunziger Jahren versprach Brentano neuer- dings, daß er nun daran gehen werde, wenigstens eine Art Surrogat in einer Art deskriptiver Psychologie zu schaffen."
      ],
      [
        "Also es sollte schon 1874 der zweite Band der «Psycho- logie» erscheinen.",
        "Nichts erschien bis in die neunziger Jahre; da erschien ein zweites Versprechen, wurde aber nicht erfüllt!",
        "Franz Brentano ist vor einigen Jahren in Zürich gestorben."
      ],
      [
        "Das Versprechen ist bis heute nicht er- füllt.",
        "Es ist beim ersten Bande der «Psychologie vom em- pirischen Standpunkte» geblieben.",
        "Warum?",
        "Weil Brentano in seiner Privatdozentenschrift den Satz aufgestellt hat: «Die Philosophie hat zu folgen denselben Methoden, die in der Naturwissenschaft angewendet werden», weil Bren- tano treu bleiben wollte diesem methodologischen Satz, den er damals aufgestellt hat, und mit dem sich eben nicht weiterkommen ließ."
      ],
      [
        "Brentano war eine viel zu ehrliche Natur, als daß er durch irgendwelche anderen Mittel als durch die Mittel der äußeren wissenschaftlichen Methode hätte weiterkommen wollen.",
        "Daher schwieg er einfach über das, was über den ersten Band hinauskam."
      ],
      [
        "Ich habe das in meinem Buche «Von Seelenrätseln» aus- gesprochen.",
        "Der Brentano-Schüler Kraus hat allerdings gesagt, es lägen allerlei andere Gründe vor dafür, daß Brentano die späteren Bände nicht veröffentlicht hat; al- lein man muß sagen, wenn die Gründe bloß vorgelegen hätten, auf die Kraus da hinschaute, dann hätte Brentano ein richtiger Philister sein müssen."
      ],
      [
        "Und das war er gewiß nicht.",
        "Er war schon eine Persönlichkeit, die durchaus den Impulsen des Inneren folgte und ihnen allein!",
        "Aber es war doch etwas vorhanden in Brentano, welches ihm wenig- stens die Hoffnung erweckte, daß man in die Dinge der Welt eindringen könne."
      ],
      [
        "Und im Grunde genommen hat jeder solche Philosoph es sind ja ihrer wenige, die in be- gründeter Weise in der neueren Zeit diese Hoffnung ge- habt haben - sich gegen Kant gewendet, selbstverständlich auch Franz Brentano.",
        "Es war etwas in ihm, was diese Hoffnung begründete."
      ],
      [
        "Und das finde ich in einem Begriff, der, ich möchte sagen, vereinzelt immer wiederum aus dem Brentanoschen Philo- sophieren herauf taucht, und den er im Sinne einer älteren Philosophie von der Art, als man noch aus der Wirklich- keit geschöpft hat, wie ich es heute morgen angedeutet habe - entlehnt hat: es ist der Begriff des intentionalen Inneseins, den er auf die Erkenntnis- und Wahrnehmungs- vorstellungen anwendet.",
        "Dieser Begriff, der muß formuliert werden."
      ],
      [
        "Dann wird man von da aus eine Annäherung an dasjenige erhalten, was ich eben vorhin angedeutet habe: zu untersuchen, in- wiefern das menschliche Sinnesorgan ein Sich-selbst-Aus- löschendes ist, dem man also gar nicht zuschreiben darf, daß es der Produzent der Sinnesqualitäten sein könne.",
        "Und dieser Begriff - nun nicht des realen Inneseins irgend- eines Prozesses, sondern des intentionalen Inneseins - ent- hält in sich das Leben des Hinweisens, das dann für das imaginative Vorstellen beobachtbar wird."
      ],
      [
        "Und dieses Le- ben des Hinweisens, das gegeben ist mit dem Begriff des intentionalen Inneseins, bringt dann die Möglichkeit, das zu erfassen, was man seit Johannes Müller, dem Physiolo- gen aus der ersten Hälfte des 19.",
        "Jahrhunderts, in so un- 57 zulänglicher Weise mit der Lehre von den «spezifischen Sinnesenergien» erfassen wollte."
      ],
      [
        "So daß man sagen möchte, der Vergleich mit dem durchsichtigen, farblosen Glase ist nicht ganz zutreffend aus dem Grunde, weil man sich nicht ein unlebendiges Farbloses, sich selbst also Aufhebendes vorzustellen hat, sondern ein lebendiges und gerade durch seine Lebendigkeit sich Aufhebendes und dadurch in einem entsprechenden Prozeß Drinnenstehendes, der ein Objek- tives erleben läßt, indem er das Objektive nicht herein- nimmt, sondern aus sich den Prozeß des Hinweisens durch und in dem Hinweisen auf dieses Objektive erfaßt.",
        "Ich habe das, was durch eine im Sinne moderner Welt- auffassung gehaltene Erneuerung dieses Begriffs des in- tentionalen Inneseins liegt, nur bei einigen neueren ameri- kanischen Philosophen gefunden, welche - wahrscheinlich sogar ohne diesen Begriff, den ich eben angeführt habe, zu kennen versuchen, die Kontinuität des menschlichen Be- wußtseins zu erfassen."
      ],
      [
        "Sagen wir zum Beispiel: im neun- undzwanzigsten Lebensjahre schaut der Mensch erinne- rungsgemäß zurück auf dasjenige, was er durchgemacht hat, sagen wir im achtzehnten Lebensjahr.",
        "Dann ist das, was den Menschen im neunundzwanzigsten Lebensjahr zurückweist, wenn man es innerlich erfaßt, etwas dem- jenigen Ähnliches, was man als ein intentionales Innesein bezeichnen könnte."
      ],
      [
        "Und in bezug auf diesen Prozeß tritt bei einigen neueren amerikanischen Erkenntnistheoretikern dieser Begriff wieder auf.",
        "Man sieht gerade an solchen Erscheinungen, wie ein be- griffliches Arbeiten in dem philosophischen Streben der Gegenwart lebendig ist."
      ],
      [
        "Aber dieses Arbeiten muß durch- aus in einer solchen Weise ehrlich werden, wie ich es vorhin bezeichnet habe, indem man dazu kommt, klar zu zeigen: Es liegen Probleme vor; das gewöhnliche Bewußtsein aber, 58 die gewöhnliche Verstandestätigkeit, das kann die Pro- bleme nur aufwerfen; und nun muß weiter fortgeschritten werden zu der Lösung der Probleme.",
        "Würde man in dieser Weise wissenschaftliche Ehrlichkeit entwickeln, dann würde diese die Grundlage sein für das Aufsteigen zum Imaginativen und den anderen Erkenntnisstufen."
      ],
      [
        "Das sollen nur ganz unzulängliche, methodologische Hinweise sein."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "MATHEMATIK UND ANORGANISCHE NATURWISSENSCHAFTEN Zweiter Vortrag, Dornach, 5. April 1921",
    "paragraphs": [
      "Wenn ich heute versuche, den Übergang zu machen vom eigentlichen philosophischen Gebiete in das Gebiet der speziellen Fachwissenschaften, so ist dieser Übergang in unserer gegenwärtigen Zeitepoche ganz naturgemäß über eine Anschauung des mathematischen und des physikali- schen, chemischen, das heißt des anorganischen Naturgebie- tes zu bewerkstelligen: weil weitaus die meisten der gegen- wärtigen philosophischen Vorstellungen so aufgebaut sind, daß die Philosophen ihnen das zugrunde legen, was sie an Begriffen und Ideen aus jenem Wissenschaftsgebiet gewon- nen haben, das heute als das sicherste gilt, aus dem mathe- matischen und dem der anorganischen Naturwissenschaft. Wenn man die heute so beliebte mathematische Behand- lung des Gebietes der anorganischen Naturwissenschaften besprechen will, muß immer wiederum an etwas erinnert werden, das schon in der Eröffnungsrede erwähnt worden ist: an die Anknüpfung, welche das gegenwärtige Denken glaubt an Kant machen zu können gerade mit der Einfüh- rung der Mathematik in die anorganischen Naturwissen- schaften, ja, in die Wissenschaft überhaupt.",
      "Worauf in diesem und auch in einem späteren Zusam- menhange von der negativen Seite her, ich sage ausdrück- lich von der negativen Seite her, wird aufmerksam gemacht werden müssen, das wurde auch schon bemerkt von ein- zelnen Denkern, die sehr weit abstehen von dem Gebrauche übersinnlicher Erkenntnisse. So wird man das Nega- 60 tive, das heißt das Zurückweisen des rein mathematischen Behandeins der Naturwissenschaft, zum Beispiel selbst bei einem Denker wie Fritz Mauthner, ganz trefflich finden, wie er aus einem gewissen Scharfsinn heraus in negativer Beziehung, das heißt im Zurückweisen desjenigen, was als falsche Ansprüche einer falschen Wissenschaftlichkeit auf- tritt, durchaus nicht unglücklich ist.",
      "Und in bezug auf die Frage: Was kann die gegenwärtige Wissenschaft nicht? kann man gerade von einem Denker wie Fritz Mauthner viel lernen, lernen durch das Negative, das er vorbringt, und lernen durch die Tatsache, daß er bei diesem Nega- tiven stehenbleiben, durchaus nicht vorwärtsdringen möch- te zu einer positiven Erkenntnis. Warum sollten Sie nicht auch von einem solchen nega- tiven Denker lernen?",
      "Wenn ich gestern den Ausspruch Ludwig Hallers anführen konnte, daß nach seiner Mei- nung Kant dem Arsenal des Lichtes die Waffen entnom- men habe, um sie im Dienste der Finsternis zu verwenden, warum sollten Sie nicht auch dem Arsenal der Finsternis, sogar der gewollten Finsternis des Erkennens, wie sie sich bei Fritz Mauthner findet, die Waffen entlehnen, um sie im Dienste des Lichtes zu verwenden? Aufmerksam ist, wie gesagt, auf jenen Ausspruch Kants zu machen, der lautet, es finde sich in jeder einzelnen Dis- ziplin nur soviel eigentliche Wissenschaft, als Mathematik darin anzutreffen ist.",
      "Wenn man die Geschichte der Verwendung dieses Kan- tischen Ausspruches bis in unsere Tage herein studiert, dann bekommt man ein interessantes Beispiel zur Beant- wortung der Frage, wie man überhaupt in der neueren Zeit Kantianer ist. Denn die Leute, die sich auf diesen Ausspruch berufen, meinen, daß in jede einzelne Wissen- schaft so viel wirkliche Wissenschaftlichkeit hineingetragen werde, als Mathematik darinnen ist.",
      "Kant meint aber etwas ganz anderes. Kant meint: so viel er Mathematik in die Wissenschaft hineinträgt, so viel ist eben Mathema- tik, das heißt wirkliche Wissenschaft drinnen, und das andere ist eben in den einzelnen Wissenschaften überhaupt gar keine Wissenschaft.",
      "Sie sehen, man wird Kantianer, wenn man einen Kan- tischen Ausspruch gründlich mißversteht. Denn die Kant- schaft auf diesem Gebiete hat etwa die folgende Logik: Wenn ich sage, in einer Versammlung, in der tausend Menschen sind, ist so viel Genialität darinnen, als drei geniale Menschen hineingetragen haben, so meine ich ganz gewiß nicht, daß die tausend Menschen nun die Genialität der drei Menschen übertragen bekommen haben.",
      "Eben- sowenig meint Kant, daß das übrige in der Wissenschaft die Wissenschaftlichkeit der Mathematik bekommen habe; sondern er meint eben, daß nur der kleine Teil, der auch in den Wissenschaften Mathematik geblieben ist, wirkliche Wissenschaft, das andere aber überhaupt keine Wissen- schaft ist. Man muß solche Dinge im Ernste - und in einem em- pirischen Zeitalter sollte man das empirisch, nicht a priori tun studieren, damit sich solche Fragen nicht so beant- worten, wie es heute vielfach geschieht, sondern damit man der Wahrheit auf die Spuren kommt.",
      "Nun kann man aber noch auf etwas anderes hinweisen: Die hervorragendsten mathematischen Denker der neueren Zeit definieren die Mathematik etwa so: sie wäre die «Wissenschaft von den Größen». Nun ja, heute ist sie die Wissenschaft von den Größen.",
      "Aber man gehe nur ein paar Jahrhunderte zurück in die Zeit, in welcher Cartesius und Spinoza eine große Befriedigung daran gefunden haben, ihre Philosophie «nach mathematischer Methode» 6z darzustellen, wie sie sagen, und man wird finden, daß es etwas ganz anderes ist, was Cartesius und Spinoza als mathematische Methode in ihre Philosophie hineinbringen wollten als dasjenige, was in der neueren Zeit als Mathe- matik in die Naturwissenschaft hineingetragen werden soll. Gehen wir bis zu Cartesius und Spinoza zurück, dann finden wir, daß diese beiden Philosophen ihr philosophi- sches System so aufstellen wollen, daß eine ebenso große Sicherheit im Übergang von einem Satz zum anderen herrscht, wie sie in der Mathematik herrscht.",
      "Das heißt, sie wollen ihre Philosophie aufbauen nach dem Muster dieser mathematischen Methoden; aber nicht, sie wollen in ihre Philosophie das hineintragen, was man heute unter Mathematik versteht. Da haben wir also bereits, indem wir so zu Cartesius und Spinoza zurückgehen, mit dem Worte Mathematik einen ganz anderen Sinn verknüpft.",
      "Wir haben - mit Absehen von dem, was sich bloß auf Größen bezieht den Sinn verknüpft des inneren sicheren Übergehens von Urteil zu Urteil, von Schluß zu Schluß. Wir haben die Art des mathematischen Denkens ins Auge gefaßt, nicht das, was wir eine Größenwissenschaft nen- nen können.",
      "Und gehen wir noch weiter zurück. Dann bekommt in älteren Zeiten das Wort «Mathematik» überhaupt einen ganz anderen Sinn. Dann ist es identisch mit dem Worte Wissenschaft. Das heißt, man hat, wenn man «Wissen- schaft» gemeint hat, von «Mathesis» oder «Mathematik» gesprochen, weil man im Mathematisieren die Sicherheit des inneren Durchschauens eines im Bewußtsein vorhan- denen Tatbestandes fand.",
      "Man verband mit diesem Worte den Sinn «Wissen» und «Wissenschaft». Und so ist ein viel allgemeinerer Begriff auf das enge Gebiet der Grö- ßenlehre übertragen worden. 63 Heute haben wir alle Veranlassung, uns an solche Dinge zu erinnern, weil wir in die Notwendigkeit versetzt sind, wiederum auf das hinzuschauen, was im mathematischen Denken eigentlich vorliegt.",
      "Was ist das Wesentliche des mathematischen Denkens? Das Wesentliche des mathe- matischen Denkens ist eben die Durchschaubarkeit der mathematischen Bewußtseinsinhalte. Wenn ich ein Dreieck aufzeichne, seine drei Winkel ins Auge fasse, Alpha, Beta, Gamma, und den Beweis liefern will, daß die Summe dieser drei Winkel 180 Grad ist, dann mache ich das Folgende (siehe Abbildung 1): Ich ziehe zur Grundlinie eine Parallele durch den obersten Punkt des Dreiecks, betrachte mir das Verhältnis der Winkel Alpha und Gamma zu den an der Parallele entstehenden Wechsel- winkeln und habe dann, indem ich überschaue, wie sich die drei Winkel, welche an der Parallele entstehen - Gamma', Alpha', und Beta -, aneinander lagern, und wie sie einen Winkel von 180 Grad bilden, den Beweis, daß auch die drei Winkel des Dreiecks 180 Grad sind.",
      "Das heißt, was bis in die Beweisgänge hinein im Mathemati- schen als Bewußtseinstatbestand vorhanden ist, das ist überschaubar, das wird vom Anfang bis zum Ende von innerlichem Erleben begleitet. Und darauf beruht die Sicherheit, die man im Mathematisieren fühlt: daß alles, was als Bewußtseinsbestand vorliegt, von innerlichem Er- 64 leben begleitet wird bis zum Urteil und bis zum Beweis hin.",
      "Und wenn man dann die äußere Natur betrachtet, in deren materielle Grundlagen man mit einer solchen Über- schaubarkeit nicht hineindringen kann, dann fühlt man sich im Betrachten der äußeren Natur dennoch befriedigt, wenn man wenigstens ihre Erscheinungen in dem Erleben verfolgen kann, das einem zuerst in der Überschaulichkeit entgegengetreten ist. Die Sicherheit, die man in dieser Überschaubarkeit des Bewußtseinsbestandes beim Mathematischen fühlt, tritt besonders dann zutage, wenn man auf das eingeht, was von allen Seiten als ein großer Fortschritt im Mathema- tischen innerhalb des 19.",
      "Jahrhunderts angesehen wird: was als «nichteuklidische Geometrie», als «Metageometrie» bei Lobatschewskij, Bolyai, Legendre und so weiter her- vorgetreten ist. Da sehen wir, wie man - im Grunde genommen doch bauend auf die innere Sicherheit des Anschauens zuerst die euklidischen Axiome abändert und durch Abänderung der euklidischen Axiome mögliche andere Geometrien als die euklidische aufbaut, und wie man dann versucht, mit dem, was man da als eine Erweiterung der Anschaulich- keit aufgebaut hat, gegenüber einer undurchschaubaren Wirklichkeit zurechtzukommen.",
      "Alle Vorstellungen, die durch diese «Metageometrie» in das moderne Denken ein- gezogen sind, sind im Grunde genommen ein Tatsachen- beweis für die Sicherheit, die man in dem Überschau- baren des Mathematisierens fühlt. Und niemand wird mit Bezug auf den euklidischen Raum - denn die Räume der anderen Geometrien sind eben andere Räume -, der ja dadurch charakterisiert ist, daß drei aufeinander senkrecht stehende Koordinaten- achsen bis in die Unendlichkeit hinein in ihren Richtungen aufeinander senkrecht gestellt gedacht werden müssen, daran zweifeln, daß für diesen euklidischen Raum gilt, was hier als Beweis für die 180-Gradigkeit der drei Win- kel eines Dreiecks hingestellt worden ist.",
      "Und jeder wird sich klar sein darüber, daß, wenn er die euklidischen Axiome abändert, dies vielleicht Beziehung habe auf un- seren Raum, in dem wir sind - der ist eben dann nicht der euklidische Raum, der ist vielleicht ein innerlich ge- krümmter Raum -, aber daß für den euklidisch überschau- baren Raum die euklidischen Resultate wegen ihrer Durchschaubarkeit als sicher angenommen werden müssen. Daran wird niemand zweifeln.",
      "Und gerade wenn man diese Tatbestände durchschaut, dann wird man finden: die Anwendung der Mathematik auf das Gebiet der Naturwissenschaft beruht darauf, daß man in der Außenwelt das erst innerlich Gefundene wieder findet, daß gewissermaßen die Tatsachen der Außenwelt sich so verhalten, wie es den mathematischen Ergebnissen entspricht, die wir erst unabhängig von dieser Außenwelt in innerer Anschauung gefunden haben. Aber eines ist durchaus zu konstatieren: Die, ich möchte sagen, Vorausbedingung für diese innerliche Anschauung des Mathematischen ist, daß dieses Mathematische uns zuerst als Bild entgegentritt.",
      "Jene innere freie Tätigkeit des Konstruierens, die wir im Mathematisieren erleben, ist eine solche innere freie Tätigkeit nur dadurch, daß in ihr nichts waltet von dem, was sonst innerhalb unserer mensch- lichen Wesenheit waltet, wenn wir zum Beispiel, einem Instinkt folgend, wollen oder dergleichen. Aus diesem ist gewissermaßen bis zur Bildhaftigkeit herausgehoben, was als Bewußtseinsbestand im Mathematisieren auftritt.",
      "Das Mathematische ist in bezug auf das, was «äußerliche Na- 66 turwirklichkeit» ist, Unwirklichkeit. Und wir fühlen die Befriedigung in der Anwendung des Mathematischen auf die Naturerkenntnis gerade dadurch, daß wir das frei in Bildlichkeit Erfaßte im Reiche des Seins wieder erkennen können.",
      "Aber gerade daraus wird man zugeben müssen, daß es auf der einen Seite berechtigt ist, wenn solche Geister, die nicht bloß auf das gehen wollen, was die Naturwirklich- keit als solche in der menschlichen Anschauung als wirklich zeigt, sondern die auf das Volle, Totale der Wirklichkeit gehen wollen, wie Goethe, wenn solche Geister das hat Goethe besonders bei der Behandlung der «Farbenlehre» klar gezeigt - nicht eine totale Anwendung des Mathema- tischen auf die ganze äußere Wirklichkeit wollen. Goethes Ablehnen der Mathematik ging gerade aus der Erkenntnis hervor, daß man zwar dasjenige, was der bildhaften An- schaulichkeit des Mathematischen entspricht, in der äuße- ren Natur durch Mathematik finden kann, daß man aber damit zu gleicher Zeit Abstand nimmt von allem Qualita- tiven.",
      "Goethe wollte bei der Behandlung der äußeren Natur nicht bloß das Quantitative, er wollte auch das Qualitative einbezogen haben. Auf der anderen Seite aber muß man sagen, daß die ganze innerliche Größe der Mathematik auf ihrer Bildlich- keit beruht, und daß gerade in dieser Bildlichkeit das- jenige zu suchen ist, was ihr den Charakter einer apriori- schen Wissenschaft gibt, einer Wissenschaft, die rein durch innere Anschauung zu finden ist.",
      "Aber damit ist man zu gleicher Zeit, indem man mathe- matisiert, gerade aus dem Natursein, demgegenüber die Mathematik einen ganz besonders interessiert, eigentlich draußen. Man ergreift nirgends ein In-sich-Wirksames, sondern nur die durch die mathematischen Formeln aus- drückbaren Beziehungen dieses Wirksamen.",
      "Wenn Sie in mathematischen Formeln eine zukünftige Mondenfinster- nis oder, mit Einsetzung entsprechender Größen in nega- tiver Form, eine in früherer Zeit vorübergegangene Mon- denfinsternis errechnen, so müssen Sie sich bewußt sein, daß Sie niemals in das innere Wesen desjenigen eindringen, was da geschieht, sondern nur von einem gewissen Ge- sichtspunkte aus die Quanten von Verhältnissen mit mathematischen Formeln umfassen. Das heißt, man muß sich klar sein, daß man niemals in das innerlich wesenhaft Differenzierte durch das Mathematische hineindringen kann, wenn man dieses Mathematische in dem engen Sinne faßt, in dem es noch heute vielfach gefaßt wird.",
      "Aber schon sehen wir auch innerhalb des Mathemati- schen eine Art Weg, der aus dem Mathematischen selber herausführt. Aus dem, was ich eben gesagt habe, können Sie entnehmen, daß dieser Weg, der aus dem Mathemati- schen herausführt, ähnlich sein müßte dem Weg, den wir durchlaufen, wenn wir mit dem ganz bildhaft Mathemati- schen, mit dem undurchkrafteten, unwirksam bildhaften Mathematischen nun untertauchen in die durchkraftete und durchkraftende Natur.",
      "Da tauchen wir in etwas unter, was uns gewissermaßen mit unserer freien mathematisie- renden Tätigkeit abfängt und die mathematischen Formeln in ein Geschehen einzwängt, das in sich wirksam ist, das in sich etwas ist, von dem wir uns sagen müssen: wir kommen nicht vollständig heran mit dem Mathematischen; das Ding behauptet gegenüber der innerlichen Durchschaubarkeit des Mathematischen seine wesenhafte Selbständigkeit und sein wesenhaftes Innensein. Dieser Weg, der da gegangen wird, wenn man einfach den Übergang sucht von der irrealen mathematischen Den- kungsart zu der realen naturwissenschaftlichen Denkungs- 68 art, kann in einer gewissen Weise heute schon innerhalb des Mathematischen selber in einer gewissen Beziehung gefunden werden.",
      "Und wir sehen, wie er gefunden werden kann, wenn wir nicht äußerlich, sondern innerlich die Ver- suche betrachten, welche das Denken gemacht hat beim Übergang von der bloß analytischen Geometrie zu der projektivischen oder synthetischen Geometrie, wie sie die neuere Wissenschaft vorstellt. Ich möchte an einem ganz elementaren, an einem allerelementarsten und bekannte- sten Beispiel der synthetischen Geometrie erläutern, was ich mit dem eben ausgesprochenen Satze meine.",
      "Wenn man synthetische, neuere projektivische Geome- trie treibt, so unterscheidet man sich von dem analytischen Geometer dadurch, daß der analytische Geometer mit mathematischen Formeln rechnet, daß er also rechnet, daß er zählt und so weiter. Als synthetischer Geometer benützt man ich meine das jetzt natürlich ideell nur das Lineal, den Zirkel und das, was durch Lineal und Zirkel im Bewußtsein als Tatbestand auftreten kann, was aus der Anschauung zunächst hervorgeht.",
      "Fragen wir uns aber, ob es auch rein innerhalb der Anschauung verbleibt. Denken wir uns eine Linie - was man in der gewöhn- lichen Geometrie eine Linie nennt und auf dieser Linie drei Punkte. Dann haben wir das folgende mathematische Gebilde (siehe Abbildung 2): eine Linie, auf der sich die drei Punkte I, II, III befinden.",
      "Es gibt nun - ich kann, was ich hier anzuführen habe, natürlich nur in den Hauptlinien andeuten, gewissermaßen appellierend an das, was Sie über die Sache schon wissen - ein anderes Gebilde, welches in einer gewissen Weise in seiner ganzen Konfiguration entsprechend ist diesem eben aufgezeichneten mathematischen Gebilde. Und dieses andere Gebilde entsteht dadurch, daß ich drei Linien in 69 einer ähnlichen Weise behandle, wie ich diese drei Punkte hier behandelt habe, und daß ich einen Punkt in einer ähn- lichen Weise behandle, wie ich hier die Linie behandelt habe.",
      "Denken Sie sich also, ich zeichne statt der drei Punkte I, II, III, drei Linien an die Tafel, und statt der Linie, welche durch die drei Punkte geht, zeichne ich einen Punkt (siehe Abbildung 3); und damit eine Entsprechung entstehe, nehme ich den Punkt, in dem sich die drei Linien schneiden: Ich habe hier ein anderes Gebilde gezeichnet (Abb. 3). Der Punkt, den ich oben mit einem kleinen Ringelchen ge- zeichnet habe, entspricht der Linie links, die drei, wie man sie nennt, Strahlen, die sich in einem Punkt schneiden, und die ich mit I, II, III bezeichne, die entsprechen den drei Punkten I, II, III, die auf der Linie links liegen (Abb. 2).",
      "Sie müssen, wenn Sie das ganze Gewicht dieses eben aus- gesprochenen Urteiles empfinden wollen, genau den Wort- laut nehmen, wie ich ihn eben ausgesprochen habe. Sie müssen sagen: der Punkt rechts (Abbildung 3), den ich oben mit einem kleinen Ringelchen bezeichnet habe, ent- spricht der Linie links (Abbildung 2), auf der die drei Punkte liegen; und die Strahlen I, II, III rechts entspre- 7° chen den Punkten I, II, III links.",
      "Und indem sich die drei Strahlen I, II, III rechts in dem einen Punkt oben schnei- den, entspricht dieses ihr Schneiden dem Liegen der drei punkte links I, II, III auf der links gezeichneten geraden Linie. So ausgesprochen, liegt ein ganz bestimmter Bewußtseins- tatbestand vor und ein entsprechendes Gebilde links gegen- über dem Gebilde rechts.",
      "Man kann nun indem man zunächst rein innerhalb desjenigen bleibt, was anschaulich ist, was sich also kon- struieren läßt mit Zirkel und Lineal, wozu kein Rechnen nötig ist - zu dem folgenden Bewußtseinstatbestande über- gehen: Ich zeichne links noch einmal eine Linie, und noch einmal auf dieser Linie drei Punkte (die untere Linie in Abbildung 4). Ich habe nun - ich bitte, jetzt ganz genau die Ausdrucks- weise, die ich befolgen werde, als maßgeblich zu betrachten für den Tatbestand -, ich habe nun links die Linie gezeich- net, auf welcher sich die drei Punkte 1, 2, 3 liegend befin- den.",
      "Ich werde weitergehen und nehme an - bitte wohl zu beachten das Wort, das ich ausspreche: «und nehme an» -, ich werde weiter das Folgende tun und nehme dann etwas an. Ich werde in einer gewissen Weise die Punkte links 71 von der einen Linie mit den Punkten von der anderen Linie verbinden und werde dadurch Verbindungslinien be- kommen, die sich schneiden werden (siehe Abbildung 5).",
      "Ich werde verbinden links in meinem Gebilde den Punkt I mit dem Punkt 3, den Punkt III mit dem Punkt I, den Punkt I mit dem Punkt 2, den Punkt II mit dem Punkt I, den Punkt III mit dem Punkt 2, den Punkt II mit dem Punkt 3, und werde durch diese Linien Schnittpunkte be- kommen, die ich dann wiederum - ich nehme es jetzt an - durch eine gerade Linie verbinden kann. Also meine Kon- struktion sei in anschaulicher Durchsichtigkeit so ausge- führt, daß ich das wirklich vollziehen könne, was ich jetzt angegeben habe.",
      "Man kann nämlich diese Konstruktion so ausführen (punktierte Linie in Abbildung 5): Sie sehen, ich habe die drei Schnittpunkte, die ich auf die vorhin be- schriebene Weise bekommen habe, so bekommen, daß ich durch sie die hier strichpunktierte Gerade ziehen kann. Ich nehme nun an, daß ich, indem ich zu dem rechten Strahlenbüschel (Abbildung 3), so nennt man es, ein anderes hinzufüge, daß ich in dem Verhältnis der Aus- strahlung dasselbe Verhältnis drinnen habe wie in der Entfernung der auf der linken Geraden liegenden Punkte.",
      "Ich werde also ein zweites Strahlenbüschel rechts hinein- 72 zeichnen (Abbildung 6), das in bezug auf seine Ausstrah- lungsverhältnisse den Lagenverhältnissen der Punkte auf den Linien links entspricht. Ich habe also hier (Abbil- dung 6) ein anderes Strahlenbüschel hineingezeichnet und nenne es 1, 2, 3, indem ich annehme, daß 1, 2, 3 in bezug auf die Strahlen rechts entspricht 1, 2, 3 in bezug auf die Punkte links.",
      "Und ich werde jetzt die entsprechende Prozedur bei meinen zwei Strahlengebilden rechts ausführen, die ich links (Abbildung 5) bei meinen Linien- und Punktgebilden ausgeführt habe, nur muß ich berücksichtigen, daß einer Linie links ein Punkt rechts entspricht: während ich links eine Linie gesucht habe, die zwei Punkte verbindet, muß ich rechts einen Punkt suchen, der entsteht, indem zwei Strahlen sich schneiden. Das Schneiden rechts soll entspre- chen dem Verbinden links (die Schnittpunkte in Abbil- dung 6 werden durch kleine Kreise markiert, siehe Abbil- dung 7).",
      "Sie sehen, was ich gemacht habe: wenn ich links III mit 1 und 3 mit I als Punkte verbunden habe, habe ich 73 hier rechts I mit 3 und 1 mit III als Linien zum Schnitt gebracht. Und wenn ich links zwei Linien gezogen habe von Punk- ten aus und sie zum Schnitt gebracht habe in einem Punkt, so werde ich jetzt entsprechend rechts durch die beiden Punkte, die ich bekommen habe, eine Linie ziehen (strich- liert in Abbildung 7), und ich werde dieselbe Prozedur mit Bezug auf die anderen Strahlen jetzt ausführen.",
      "Das heißt [der Vortragende verdeutlicht nochmals die Entsprechung der geringelten Schnittpunkte von Abbildung 7 mit den Verbindungslinien von Abbildung 5], ich werde II mit 1 zum Schnitt bringen, I mit 2, III mit 2, II mit 3; ich werde also rechts die Schnittpunkte suchen, wie ich links die Ver- bindungslinien gesucht habe; und, wie Sie sehen, habe ich rechts durch das Zum-Schnitt-Bringen der Strahlen diese Schnittpunkte gesucht, um Linien durch diese Schnitt- punkte zu ziehen (strichliert in Abbildung 7), wie ich links durch das Verbinden der Punkte Linien gesucht habe, um 74 die Schnittpunkte dieser sich schneidenden Linien zu ge- winnen (geringelt in Abbildung 5). Die Verbindungslinien aber der Schnittpunkte, die ich rechts gewonnen habe, schneiden sich ebenso in einem hier durch ein Ringelchen bezeichneten Punkt oben (P in Ab- bildung 7), wie die drei Punkte, die ich links bekommen habe, in einer geraden Linie liegen (strichliert in Abbil- dung 5).",
      "Das heißt, im Gebilde rechts, wo statt der Punkte Linien, statt der Verbindungslinien Schnittpunkte sind, be- komme ich, wie ich links eine Linie bekommen habe, die durch die drei Punkte geht, einen Punkt, in dem sich die drei Geraden schneiden. Ich bekomme rechts wiederum einen Punkt für die Linie links.",
      "Hier bleibe ich, indem ich rein vom Gebiete des An- schaulichen ausgehe, zwar innerhalb desjenigen, was von der Anschauung ausgeht, was aber doch zu etwas anderem führt. Und ich bitte Sie, das Folgende zu berücksichtigen.",
      "Nehmen Sie an, Sie schauen in der Linie, in der Richtung, die angegeben wird durch die (gestrichelte) Linie links, die durch die drei Schnittpunkte - Alpha, Beta, Gamma - geht, dann werden Sie auf einen Schnittpunkt aufschauen, der die anderen verdeckt, gegenüber dem die anderen hinter ihm sind (Abbildung 8). Sie haben hier, in der Linie auseinandergelegt, nicht nur «drei Punkte».",
      "Sondern so- bald man zu einem Wirklichkeitsverhältnis übergeht, tritt gegenüber diesen drei Punkten etwas auf, was ganz an- schaulich ist: der Punkt Gamma ist der Vordere, und hinter ihm sind die Punkte Beta und Alpha. Das haben Sie in der linken Figur klar auseinandergelegt in der An- schauung.",
      "Gehen wir jetzt durch eine ganz gesetzmäßige Prozedur, die ich beschrieben habe, über zu dem rechts entsprechen- den Gebilde, so haben wir statt der Linie einen Punkt ins 75 Auge zu fassen (P in Abbildung 9). Wenn wir ihn ins Auge fassen, so müssen wir sagen, geradeso wie links durch die Verbindung von III mit 2 und die Verbindung von 3 mit II ein Schnittpunkt entsteht, Gamma, der die anderen Schnittpunkte zudeckt, so daß das Verhältnis entsteht: Gamma ist vorn, Alpha ist hinten, so entsteht rechts die Notwendigkeit, das Folgende vorzustellen und damit, durch das Verbindungsgesetz, aus dem Anschaulichen ins Unanschauliche überzutreten: Rechts (Abbildung 9) ent- steht die Notwendigkeit, den geringelten Punkt (P) so vorzustellen, daß der Strahl (Gamma), der durch die Ver- bindung der Schnittpunkte der Linien III und 2, II und 3, entsteht, sich zunächst in dem geringelten Punkt mit dem- jenigen Strahl (Beta) schneidet, der durch das voran- liegende Verhältnis (III mit 1, I mit 3) entsteht; und wir müssen uns vorstellen, daß innerhalb dieses geringelten Punktes die Schnitte, die durch die drei strichlierten Strah- 76 len entstehen, ebenso als drei innerlich differenzierte Enti- täten liegen wie links auf der strichpunktierten Linie die drei Punkte Gamma, Beta, Alpha.",
      "Das heißt, ich muß die Schnitte rechts im einzelnen Punkt so angeordnet finden, daß sie sich übereinander decken. Das heißt mit anderen Worten nichts Geringeres als: Geradeso wie ich für ein hinschauendes Auge die strich- punktierte Linie links so zu denken habe, daß für die Punkte Gamma, Beta, Alpha ein Vorne und Hinten ent- steht, so habe ich innerhalb des Punktes, das heißt einer Raumausdehnung von Null, nach allen drei Dimensionen eine Differenzierung zu denken.",
      "Ich habe in diesem Punkte angeschaut aus der Art heraus, wie er aus diesem Gebilde entstanden ist - nicht etwas Undifferenziertes, sondern ein Vorne und Hinten zu denken. Ich bekomme hier die Notwendigkeit, einen Punkt nicht neutral nach allen Seiten zu denken, sondern den Punkt zu denken mit einem Vorne und Hinten.",
      "Ich mache hier einen Weg, durch den ich aus dem freien Bilden des Mathematischen hineingezwungen werde in etwas, wo das Objektive zu einer Eigenbestimmung, zu einem Innensein übergeht. Sie sehen, dieser Weg ist ähn- lich demjenigen, durch den ich übergehe von dem mathe- matisch freien Bilden zu dem In-Empfang-Nehmen dieses Bildens vom innerlichen Bestimmtsein innerhalb der Naturordnung.",
      "Und ich bekomme, indem ich von der analytischen zu der synthetischen Geometrie übergehe, den Anfang des Weges, der mir gezeigt wird von der Mathe- matik zur anorganischen Naturwissenschaft. Es ist dann im Grunde genommen nur noch ein kleiner Weg zu etwas anderem.",
      "Man kann, indem man diese Er- wägungen, auf die ich jetzt hingedeutet habe, fortsetzt, zum innerlichen Begreifen auch des folgenden Bewußtseins- 77 tatbestandes kommen: Wenn man rein mit Hilfe der pro- jektiven, der synthetischen Geometrie verfolgt, wie sich ein Hyperbel zu einer Asymptote verhält, so bekommt man rein anschaulich heraus, daß nach der einen Seite, sa- gen wir rechts oben, die Asymptote sich dem Hyperbelast nähert, aber ihn niemals erreicht, daß man aber dennoch die Vorstellung bekommt, die Hyperbel komme wiederum von links unten zurück mit dem anderen Ast, und die Asymptote komme ebenfalls von links unten zurück mit ihrer anderen Seite. Mit anderen Worten: ich bekomme durch dieses Verhältnis von Asymptote zur Hyperbel etwas, was ich etwa in der folgenden Art Ihnen auf die Tafel zeichnen könnte (Abbildung 10): Rechts oben geht die Asymptote, die gerade Linie, im- mer näher an die Hyperbel heran.",
      "Ich habe dort eine Schraffierung hinzugefügt, um auszudrücken, was für ein Verhältnis die Asymptote eigentlich zum Hyperbelast hat. Sie kommt ihm immer näher, sie will an ihn heran, sie kommt immer näher und näher in das Sein ihres Verhält- 78 nisses zu ihm hinein.",
      "Wenn man nun dieses Verhältnis ver- folgt nach rechts oben, so kommt man zuletzt durch rein projektives Denken ich kann das hier nur andeuten dazu, die Richtung der Linie, die man nach rechts oben hat, sei es die Hyperbel, sei es die Asymptote, von links unten wieder herkommend, zu finden, den Hyperbelast und die Asymptote, und diese so, daß sie mit ihrem Sein in der schraffierten Andeutung den Hyperbelast immer mehr und mehr verläßt. So daß wir sagen können: diese Asymptote hat eine merkwürdige Eigenschaft.",
      "Indem sie nach rechts oben hinansteigt, wendet sie sich mit ihrem Verhältnis zur Hyperbel der Hyperbel zu, indem sie von links unten wieder heraufkommt, wendet sie sich mit ihrem Verhält- nis zur Hyperbel von der Hyperbel ab. Diese Linie, die Asymptote, hat, wenn ich sie in ihrer Vollständigkeit, Totalität betrachte, wiederum ein Vorne und Hinten.",
      "Des- halb konnte ich auch die Schraffierung das eine Mal auf der einen Seite, das andere Mal auf der anderen Seite zeichnen. Ich komme wiederum in eine innere Differen- zierung des Linearen hinein, wie ich in eine innere Diffe- renzierung hineinkomme, wenn ich das rein mathematisch Bildhafte in das Gebiet des Naturgeschehens hineindränge.",
      "Das heißt, ich nähere mich dem, was als Differenzierung im Naturgeschehen auftritt, wenn ich in richtiger Weise mit Hilfe der projektiven Geometrie die mathematischen Ge- bilde selbst erfassen will. Was da durch die projektive Geometrie geschieht, das kann niemals in derselben Weise durch die bloße analy- tische Geometrie gemacht werden.",
      "Denn die bloße analy- tische Geometrie bleibt, indem sie also in Koordinaten konstruiert und dann in ihrer Rechnungsform die End- punkte der Abszissen und Ordinaten aufsucht, mit dem, 79 was sie konstruiert, in ihrer Form ganz außerhalb der Kurve oder außerhalb des Gebildes selber stehen. Die pro- jektive Geometrie bleibt nicht außerhalb der Kurve und des Gebildes stehen, sondern sie dringt in die innere Diffe- renzierung des Gebildes: bis zum Punkte, bei dem man unterscheiden muß ein Vorne und Hinten bis zur Gera- den, bei der man ebenfalls unterscheiden muß ein Vorne und Hinten.",
      "Ich habe nur diese Eigenschaften wegen der Kürze der Zeit angegeben, ich könnte noch andere Eigen- schaften angeben, zum Beispiel ein gewisses Krümmungs- verhältnis, das der nach den drei Raumdimensionen aus- gedehnte Punkt in sich hat und so weiter. Wenn man wirklich mit innerem Seelenanteil den Weg verfolgt, der da von der analytischen Geometrie in die synthetische Geometrie hineinführt, wenn man sieht, wie man da, ich möchte sagen, aufgefangen wird von etwas, was schon der Realität sich nähert, wie diese Realität im äußeren Naturdasein vorhanden ist, dann hat man das- selbe innere Erlebnis, genau dasselbe innere Erlebnis, das man hat, wenn man aufsteigt von dem gewöhnlichen Ver- standesbegriff, von der gewöhnlichen Logik, zu dem Ima- ginativen.",
      "Man muß im imaginativen Erkennen nur wei- tergehen. Aber den Anfang hat man gegeben, wenn man anfängt, von der analytischen Geometrie zu der syntheti- schen überzugehen. Man merkt da das Abgefangenwerden von dem, was sich aus der Bestimmtheit durch die äußere Realität ergibt, nach der man das Resultat gefaßt hat, und man merkt das ebenso im imaginativen Erkennen.",
      "Und nun, welches ist der entgegengesetzte Weg inner- halb der Geisteswissenschaft gegenüber demjenigen, der vom gewöhnlichen gegenständlichen Erkennen ins imagi- native Erkennen hineinführt? Es wäre derjenige, der von der Intuition oben zur inspirierten Erkenntnis hinunter- 80 führte.",
      "Da finden wir aber bereits, daß wir drinnenstehen im Realen. Denn mit der Intuition stehen wir im Realen drinnen. Und wir gehen weg vom Realen. Indem wir von der Intuition heruntersteigen zu der Inspiration, entfernen wir uns wiederum von dem Realen.",
      "Und wenn wir bis zur Imagination herunterkommen, haben wir nur noch das Bild des innerlich Realen. Dieser Weg, der ist zu gleicher Zeit derjenige, den das Reale durchmacht, um unser Erkenntnisobjekt zu werden.",
      "Natürlich, in der Intuition stehen wir in der Realität drinnen. Wir gehen von der Realität ab, zu der Inspira- tion, zu der Imagination, und kommen zu unseren gegen- ständlichen Erkenntnissen. Die haben wir dann in unserem heutigen Erkennen.",
      "Wir machen den Weg von der Realität zu unserem Erkennen herein. Wir stehen gewissermaßen zuerst innerhalb der Realität und kommen von dieser Realität ab zu dem irrealen Erkennen. Auf dem Weg, den wir zurücklegen von der analytischen Geometrie in die projektive oder synthetische Geometrie hinein, versuchen wir uns wiederum nach der entgegengesetzten Richtung zu bewegen, von der rein verstandesmäßigen analytischen Geometrie in dasjenige, wo wir anfangen können real zu denken, wenn wir überhaupt zu etwas kommen wollen.",
      "Wir gehen der Entrealisierung der Natur, die sie durch- macht, indem sie Erkenntnis werden will, entgegen, indem wir realisieren die irreale Erkenntnis. Sie sehen, man hat nicht etwa nötig, anzunehmen, daß unsere moderne Geisteswissenschaft, wie sie hier auftritt, anders mathematisieren wollte, als es die Mathematiker tun, wenn sie nur recht in ihrem Sinne mathematisieren.",
      "Man hat nicht einmal nötig - außer dem Aufsuchen von besonderen Versuchsanordnungen, die aus dem Quantita- tiven ins Qualitative hineinführen viel anderes zu tun 81 auf den Gebieten, die ja eine quantitative Naturwissen- schaft heute schon betreten hat. Und wenn diese äußere quantitative Naturwissenschaft heute der modernen An- throposophie ihre «gesunden Ergebnisse» entgegenhält, dann ist es ungefähr so, wie wenn jemand ein Gedicht vorgelesen hat, das in ganz andere Regionen geht, und einer kommt: Ja, da kann ich ja nicht entscheiden durch meine Seelenverfassung, ob man in einem Gedichte leben kann, ich aber weiß etwas ganz gewiß: daß zwei mal zwei vier ist! - Niemand bezweifelt, daß zwei mal zwei vier ist; ebensowenig bezweifelt dasjenige, was die moderne anorganische Naturwissenschaft gibt, wer zur Geisteswis- senschaft aufrücken will.",
      "Aber es ist gegen den Inhalt eines Gedichtes zum Beispiel just kein besonderer Einwand, wenn man ihm entgegenhält: zwei mal zwei ist vier. Es handelt sich aber darum, daß dasjenige, wohin die einzelnen Wissenschaften schon besonders tendieren, wohin sie wollen, daß das ernst und mutig als Weg zu einer wahren Wirklichkeitserkenntnis von Anthroposophie in Angriff genommen wird.",
      "Und während manche Leute heute in fruchtlosem Skeptizismus eine Finsternis errichten wollen über dem, was sie, oftmals mit Recht, als Grenzen des Naturerkennens empfinden, möchte Anthroposophie da, wo Naturwissenschaft finster wird, beginnen, das Licht des geistigen Erkennens zu entzünden. Und so wird sie vielleicht mit Bezug auf diejenigen Wissenschaften, die heute erwähnt worden sind, nicht ge- rade groß andere Methoden einschlagen; aber sie wird die Bedeutung, den inneren Seinswert der Wissenschaften, von denen heute gesprochen worden ist, vor die Menschheit hin- stellen und wird dadurch bewirken, daß man weiß, warum man mit Mathematik ins Sein eindringt, nicht bloß, warum man mit Mathematik zu einer gewissen Sicherheit kommt.",
      "Denn zum Schluß kommt es ja nicht darauf an, bloße Gewißheitsprodukte zu entwickeln. Da könnten wir uns im engsten Kreis abschließen und immer und immer wieder im engsten Kreise drehen, wenn wir bloß «das Gewisseste» festhalten wollten.",
      "Sondern es handelt sich um Erweite- rung des Erkennens. Die aber kann nicht gefunden wer- den, wenn man den Weg scheut aus dem inneren Erleben in das äußere, in sich selber differenzierte Sein. Dieser Weg wird vielfach sogar in der Mathematik und mathe- matischen Naturwissenschaft der Gegenwart angedeutet.",
      "Man muß ihn nur erkennen und dann im Sinne dieser Er- kentnis wissenschaftlich handeln. Schlußwort zur Disputation Dornach, 5. April 1921 Meine sehr verehrten Anwesenden! Ich will, zum Teil wegen der vorgerückten Zeit und zum Teil aus anderen Gründen, nicht mehr als ein paar Bemerkungen machen, die mit am heutigen Abend Vorgebrachtem, Vorgekom- menem, zusammenhängen.",
      "Da möchte ich zunächst auf die Frage betreffend Pro- fessor Rein ganz kurz zurückkommen aus dem Grunde, weil ein Umstand gerade in dieser Angelegenheit doch scharf hervorgehoben werden sollte. Daß von seiten eines Herbartianers, namentlich eines Herbartianers, der durch die historische Schule gegangen ist, über meine «Philosophie der Freiheit» nicht sonderlich viel Zustimmendes gesagt werden kann, das weiß ich sehr gut.",
      "Das hat sich ja auch gleich nach dem Erscheinen der «Philosophie der Freiheit» 1894 gezeigt. Denn eine der ersten Besprechungen, die erschienen sind über die «Philo- sophie der Freiheit», war die des Herbartianers Robert Zimmermann.",
      "Aber ich muß sagen, trotzdem diese Bespre- chung außerordentlich gegensätzlich war, hat sie mich ge- freut aus dem Grunde, weil damals im Gegensatz einige wirklich große Gesichtspunkte angeschlagen worden sind. Wie also notwendig das Verhältnis sein muß zwischen einer Herbartianer-Beurteilung und dem, was meine «Philosophie der Freiheit» enthält, darüber gebe ich mich nicht dem geringsten Zweifel hin.",
      "Allein, es ist schade, daß ich jetzt die Besprechung der «Philosophie der Frei- heit» durch Professor Rein nicht hier habe und das Zitat so belegen könnte, wie ich es gern tun würde. - Es ist mir nun soeben gebracht worden, und ich kann daher an der Hand der Besprechung manches noch genauer sagen, als es sonst möglich wäre. Da beginnt also diese Bespre- chung zunächst mit den Worten: «In Zeiten eines morali- schen Tiefstandes, wie ihn das deutsche Volk wohl noch nicht erlebt hat, ist es doppelt not, die großen Landmar- ken der Moral, wie sie von Kant und Herbart aufgerichtet worden sind, zu verteidigen und sie nicht zugunsten relati- vistischer Neigungen verrücken zu lassen.",
      "Das Wort des Freiherrn v. Stein, daß ein Volk nur stark bleiben kann durch die Tugenden, durch welche es groß geworden ist, lebendig zu halten, muß heute zu den ersten Aufgaben inmitten der Auflösung aller moralischen Begriffe gerech- net werden.",
      "Daß an dieser Auflösung eine Schrift des Führers der Anthroposophen in Deutschland, des Dr. Steiner, be- teiligt ist, muß besonders beklagt werden, da man den idealistischen Grundzug dieser Bewegung, die auf eine starke Verinnerlichung des Einzelmenschen hinzielt, nicht leugnen und in seinem Plan der Dreigliederung des sozia- len Körpers gesunde, das Volkswohl fördernde Gedanken finden kann.",
      "Aber in der Schrift (Berlin 1918) überspannt er seine individualistische Einstellung in einer Weise, die zur Auflösung der sozialen Gemeinschaft führen und deshalb bekämpft werden muß.» Sie sehen hier deutlich gesagt, daß die «Philosophie der Freiheit» herausentstanden sei aus der Auflösung aller mo- ralischen Vorstellungen und so weiter und das kann man ja auch glauben, daß es die Meinung eines Mannes sein kann. Nun, ein großer Teil der hier Anwesenden kennt meine Ansichten in bezug auf wissenschaftliche Genauigkeit, auf 85 wissenschaftliche Gewissenhaftigkeit, und vor allen Din- gen darüber, daß man sich über das, worüber man schreibt, zunächst ordentlich unterrichten soll.",
      "Die «Philosophie der Freiheit», die 1894 erschienen ist, auch nur stilistisch in Zusammenhang zu bringen mit dem, worauf hier gedeutet ist in den ersten Sätzen, ist eine Leichtfertigkeit. Und eine solche Leichtfertigkeit darf nicht damit entschuldigt wer- den, daß derjenige, der als ein Professor der Pädagogik an einer Hochschule wirkt, durchaus - wie ich glaube, daß es gesagt wurde - «nicht über die Grenze einer wirklich objektiven Beurteilung hinausgegangen» sei.",
      "Es handelt sich darum, daß wir eine Gesundung gerade derjenigen Verhältnisse, die heute abend hier in einer recht herzhaf- ten Weise besprochen worden sind, nur dann herbeiführen können, wenn wir uns derselben Leichtfertigkeit nicht schuldig machen, sondern wenn wir wissenschaftliche Ge- wissenhaftigkeit streng ausüben gerade denen gegenüber, die von Amts wegen den Beruf haben, erzieherisch auf die Jugend zu wirken. Da darf man dem, der diesen Beruf hat, nicht erlauben, zu übersehen, aus welchen Verhältnis- sen heraus und in welchen Zeiten eine Schrift, die man beurteilen will, entstanden ist.",
      "Das ist das erste, was ich zu sagen habe. Dann die Art und Weise des Zitierens. Sie finden in diesem Artikel eine unglaubliche Art, Sätze aus dem Zu- sammenhange herauszureißen und an herausgerissene Sätze dann nicht das anzuknüpfen, was in meiner «Philosophie der Freiheit» steht, sondern das, was der Artikelschreiber meint, nach seiner eigenen Meinung anknüpfen zu sollen, was aus der Deutung der Sätze, die er herausgerissen, nach seiner Meinung gefolgert werden kann.",
      "Wer sich die Mühe nimmt, die «Philosophie der Freiheit» wirklich durchzunehmen, der wird sehen, daß überall in 86 dieser «Philosophie der Freiheit» in vollständig klarer Weise auseinandergesetzt ist, wie das vermieden werden kann, was durch Professor Rein aus Mißverständnis an in beliebiger Weise aus dem Zusammenhang herausgeris- senen Sätzen moniert wird. Dem, was er über das Herausholen der «Philosophie der Freiheit» aus den Zeitverhältnissen schreibt, entspricht das Hineinstellen in unmögliche Zusammenhänge: «Hören wir so Herrn Dr.",
      "Steiner reden, so könnte man versucht sein, ihn als Apostel des ethischen Libertinismus anzusprechen. Er hat dies auch gefühlt und ist dem Einwand begegnet, der dahin geht: Wenn jeder Mensch nur danach strebt, sich auszuleben und zu tun, was ihm beliebt, dann gibt es keinen Unterschied zwischen guter Handlung und Ver- brechen.",
      "Jede Gaunerei, die in mir liegt, hat gleichen An- spruch, sich auszuleben, wie die Intention, dem allgemei- nen Besten zu dienen. Diesen Einwand sucht Dr. Steiner durch den Hinweis zu entkräften, daß der Mensch erst dann auf die geforderte Freiheit Anspruch erheben darf, wenn er die Fähigkeit erworben hat, sich zum intuitiven Ideengehalt der Welt zu erheben.",
      "Diese Fähigkeit sich an- zueignen, ist Aufgabe des Anthroposophen, der sich auf den Standpunkt des ethischen Individualismus erheben soll.» Nun, bitte, legen Sie sich die Frage vor, ob jemand als Beurteilung der «Philosophie der Freiheit» solche Sätze hinschreiben darf. Die «Philosophie der Freiheit» ist 1894 veröffentlicht, wo es noch keine «Anthroposophen» gege- ben hat.",
      "Also Professor Rein stellt die «Philosophie der Freiheit» auch in ein Milieu hinein, das überhaupt für die «Philosophie der Freiheit» zur Zeit ihres Erscheinens ein unmögliches war, abgesehen von den Trivialitäten, die dann kommen, wo er davon spricht, daß das eine Ethik für Anthroposophen und Engel und dergleichen wäre und so fort. Es handelt sich wirklich hier nicht darum, in irgend- einer Weise auf, ich möchte sagen, einen «gegenteiligen Standpunkt» irgendwie ein schiefes Licht werfen zu wol- len, sondern darum, daß diese Art, geistige Dinge zu be- urteilen, durchaus in die ganze Welt desjenigen hineinge- hört, was aus unserer Kultur heraus muß, wenn die Zu- stände, die heute hier besprochen werden sollten, besser werden sollen.",
      "Ich darf wohl sagen, daß ich mir gut über- legt habe, ob ich schließlich diese Worte hier aussprechen solle oder nicht. Aber mir scheint die Sache denn doch wich- tig genug zu sein, und ich glaube, daß ich die Grenze der Objektivität nicht überschritten habe, daß ich mich eigent- lich im wesentlichen darauf beschränkt habe, die Art und Weise des Urteilens und nicht den «Standpunkt» vor Ihnen hier zu charakterisieren.",
      "Ich weiß, daß man immer gewissermaßen auf dünnes Eis tritt, wenn allerlei Ver- wandtschaftliches vorgeführt wird. Allein, ich kann mich darnach nicht richten, obzwar ich ja auch sonst nicht ge- bunden bin, denn ich habe innerhalb der Professorenschaft keinen Schwiegervater!",
      "Nun möchte ich noch einige andere Bemerkungen ma- chen und dazu an einen Satz anknüpfen, der heute auch hier besprochen worden ist. Wirklich nur, um symptoma- tisch zu sprechen, möchte ich da ein kleines Erlebnis vor- bringen, das aber nur illustrieren soll.",
      "Es ist gesagt worden, es sei richtig, daß nicht alle Stu- denten, die an eine Universität oder Hochschule kommen, auch reif seien für diese Hochschule; allein dafür könnten ja die Professoren an den Hochschulen nichts, sondern diese Studenten würden ihnen eben zugeschickt von den höheren Schulen. Ja, aber da konnte ich wirklich nicht an- 88 ders, als mir ein Gespräch einfallen lassen, das einmal mit einem der berühmtesten Literaturhistoriker an deutschen Universitäten in meiner Gegenwart geführt worden war.",
      "Dieser Literaturhistoriker war auch in der Prüfungskom- mission für das Gymnasiallehramt. Ich tue es eigentlich ungern; aber heute sind die Zeiten so ernst, daß man schon auch solche Dinge vorbringen muß. - Er sagte: Ja, mit diesen Gymnasiallehrern, wir kennen sie ja, wir müssen sie ja prüfen, aber wir haben manchmal ganz sonderbare Gedanken, wenn wir diese Kamele als Gymnasiallehrer auf die Gymnasien hinauslassen müssen!",
      "Nun, es ist nur, wie gesagt, eine Illustration, die ich durch dieses Erlebnis geben möchte. Ich weiß nicht, ob es sehr stark für die Universitätslehrer spricht, wenn ein Prüfungskommissar und berühmter Universitätslehrer sich dazu herbeiläßt, diejenigen Lehrer der Jugend, die an die Gymnasien hinausgeschickt werden, «Kamele» zu nennen.",
      "Ich sage es nicht, aber der betreffende Mann hat es gesagt. Ich zitiere nur. - Nun, es muß schon jeder Gedanke zu En- de gedacht werden. Und da glaube ich, wenn der Gedanke zu Ende gedacht wird, daß sich die Universitätslehrer nicht beklagen dürfen, wenn unfähige Gymnasial-Abitu- rienten die Pforte der Universität betreten; denn die Uni- versitätslehrer haben ja erst die Gymnasiallehrer hinaus- geschickt, die ihnen diese Absolventen zugerichtet haben.",
      "Also schließlich ist es doch notwendig, wie gesagt, den Gedanken zu Ende zu denken. Und der zeigt uns, daß wir, wenn auch mit einiger Nachsicht, in einer gewissen Beziehung schon den Schuldbegriff anwenden dürfen.",
      "Aber es sind heute so sonderbare Worte gefallen, sehen Sie. Und da muß ich sagen, eines der sonderbarsten Worte, schon fast eine von den kleinen Pikanterien, war doch dies, daß gesagt worden ist, ein Universitätslehrer 89 hätte gesagt: Wir erwarten die Erlösung von der Studen- tenschaft! - Ich wundere mich nur, daß er dann nicht auch noch gesagt hat: Von dem Augenblicke, wo wir uns auf die Schulbänke setzen und die Studenten auf das Katheder hinauf befördern. - Sehen Sie, es ist schon notwendig, daß man den überall schleißig werdenden Urteilen, die so die Gegenwart durchschwirren und die dennoch überall die Veranlassung sind zu unseren heutigen Zuständen, daß man der Schleißigkeit dieser Urteile etwas nachgeht.",
      "Selbstverständlich verkennt man dann, wenn man das tut, doch nicht, daß überall Ausnahmezustände und Aus- nahmen vorhanden sind, und man kann zum Beispiel vieles, sehr vieles von dem unterschreiben, was in bezug auf den Kunstunterricht an den Akademien gesagt worden ist. Aber im ganzen und großen muß man schon sagen: Es ist doch nicht so außerordentlich viel Grund dazu vor- handen, gute Hoffnungen in die Zukunft zu senden, wenn man nicht bereit ist, nicht bloß im Äußeren, durch irgend- welche Verbände oder dergleichen, sich zusammenscharen zu wollen, um irgendeinem Unbestimmten entgegenzu- gehen, sondern wenn man bereit ist nur, wenn man bereit ist -, wirklich einzugehen auf eine gründliche Er- neuerung und Wiederbelebung unseres Geisteslebens selbst.",
      "Es greift schon das, was die eigentlichen Schäden sind, in unser Geistesleben selbst hinein. Und wer das ganze Gefüge des anthroposophischen Lebens kennt, wie es zum Beispiel geführt hat zu dieser Freien Hochschule für Geisteswis- senschaft: uns braucht man ganz gewiß nicht zu sagen, daß «jedem es frei stehen müsse, seine Weltanschauung zu vertreten und aus seiner freien Überzeugung heraus zu reden!» Die vielen böswilligen Naturen, die heute da sind, um alles mögliche Unzutreffende über die anthroposophi- sche Bewegung und was damit zusammenhängt, zu sagen, 9° die werden daraus gleich wieder Kapital schlagen und sagen: Diese Anthroposophen wollen, daß ihre Weltan- schauung überall vertreten ist.",
      "Nun, die Waldorfschule ist aus unserer Mitte heraus begründet worden, ohne daß damit in irgendeiner Weise eine Weltanschauungsschule gegründet worden ist. Gerade das Gegenteil einer Weltanschaungsschule sollte begründet werden.",
      "Das ist immer wieder und wieder betont worden. Und wer da glaubt, die Waldorfschule sei «eine anthropo- sophische Schule», der kennt sie eben ganz und gar nicht. Und ebensowenig kann irgendwie hier am Goetheanum gesagt werden, daß in alledem, was geschieht, irgend jemand beeinträchtigt werde in dem freien Bekenntnis seiner ureigensten Überzeugung.",
      "Aber dasjenige, wofür ich wenigstens immer kämpfen werde, das ist, bei aller Freiheit, bei aller Individualität und Intellektualität: wissenschaftliche Gewissenhaftigkeit, Gründlichkeit, Unterrrichtetsein von dem, über das man eben schreibt -, nicht ein bloßes Hinstellen der eigenen Meinung, weil man glaubt, es könnten unter Umständen auch irgendwelche Schäden entstehen aus demjenigen, das man sich in Wirklichkeit nicht bemüht zu verstehen, und aus dem man einige Sätze herausreißt, um einen Artikel zu schreiben. Ich sage das ganz ohne Leidenschaft.",
      "Sie wissen, ich be- nütze gewöhnlich die Dinge, die als «Besprechungen» sich über Anthroposophie hermachen, eigentlich nur als einen hier naheliegenden Anlaß, um allgemeine Zustände zu charakterisieren. Die persönlichen Angriffe interessieren mich im Grunde genommen gar nicht, nur insofern, als sie hinweisen auf das, was aus unseren Zuständen hinaus muß.",
      "Und da glaube ich doch, daß der Kommilitone aus Bonn in seiner herzhaften Weise einen richtigen Ton ge- troffen hat, einen richtigen Ton insofern, als die Studen- ten, die er gemeint hat, tatsächlich heute an den Universi- täten oder an den Hochschulen das nicht finden können, was sie suchen. Aber nicht «wegen des Lehrplanes», nicht «weil man nicht in der richtigen Weise auswählt», sondern weil die heutige Jugend ganz instinktiv - sie ist sich dessen nicht voll bewußt aus dem tiefsten Inneren heraus doch nach etwas verlangt, was innerhalb der allgemeinen Wissen- schaftlichkeit noch nicht da ist, was aber geschaffen wer- den muß innerhalb der allgemeinen Wissenschaftlichkeit.",
      "Das erwartet die Jugend. Diese Jugend wird ganz gewiß nicht ermangeln, mit vollen Händen zuzugreifen, wenn ihr wirklich geboten wird - was sie eigentlich will - ein wirklich neuer Geist. Denn einen solchen neuen Geist braucht die Gegenwart.",
      "Das ist im Grunde genommen auch der Grund der Ab- neigung gegen das, was von anthroposophischer Geistes- wissenschaft ausgeht, auch wenn man die Phrase im Munde führt, «man wolle jedem Neuen entgegenkom- men». Wenn es sich geltend macht, dann tut man es doch nicht.",
      "Weil man es im Grunde genommen auch gar nicht kann. Es würde nichts nützen, diese Dinge in irgendeiner Weise zu kaschieren, sondern es muß scharf, klipp und klar auf diese Dinge hingewiesen werden. Dann ist hier die Frage des Weltschulvereins gestellt worden.",
      "Was ich über diesen Weltschulverein zu sagen habe in bezug auf seine Absichten, habe ich, wie ich glaube, mit voller Deutlichkeit ausgesprochen am Ende unserer letzten Hochschulkurse im Herbst hier. Ich habe dann wiederum ungefähr in derselben Weise die Notwendigkeit der Begründung eines solchen allgemeinen Weltschulver- eins im Haag, in Amsterdam, in Utrecht, in Rotterdam 92 und in Hilversum ausgesprochen: daß die Möglichkeit, in einem Weltschulverein zu wirken, davon abhänge, daß sich die Überzeugung, daß ein neuer Geist in das allge- meine Schulwesen einziehen müsse, in einer möglichst gro- ßen Anzahl von Menschen verbreitet.",
      "Ich habe darauf hingewiesen, daß es heute gar nicht darauf ankommen könne, da oder dort Schulen zu begründen, die vereinzelt dastehen würden, und in denen man eine in dieser oder jener Hinsicht verbreitete Methode anwendet, sondern daß aus dem Gedanken des sich selbsttragenden, in sich befreiten Geistesleben heraus das Schulwesen der neueren Zivilisation in die Hand genommen werden müsse, das Schulwesen aller Kategorien, aller Stoffe. Soviel mir bekanntgeworden ist, sind die Worte und Aufforderungen, die ich bis jetzt gesprochen habe, das einzige, worüber ich im Grunde genommen zu berichten habe.",
      "Diese Worte waren darauf berechnet, in der zivili- sierten Bevölkerung der Gegenwart ein Echo zu finden. Ich habe von keinem solchen Echo zu berichten. Und ich glaube, ein richtiges Wort hat der Kommilitone aus Bonn gesprochen, indem er darauf hingewiesen hat, daß schließ- lich doch diejenige Studentenschaft, aus deren Herzen her- aus er hier geredet hat, in der Minderzahl ist.",
      "Ich glaube, sie ist sehr, sehr in der Minderzahl, insbesondere in Deutschland. Aber auch sonst - ich will niemandem Un- freundlichkeiten sagen , sonst, von wo wir gar nicht weit weg sind. Das zeigt der Besuch dieses Hochschulkurses.",
      "Er sagte: Der größte Teil der Studentenschaft schläft! Ja, er tobt zuweilen auch. Aber man kann auch tobend schlafen in bezug auf die Dinge, um die es sich da handelt. Und in bezug auf die Angelegenheiten, in bezug auf welche diese Forderung nach dem Weltschulverein erhoben worden ist, schläft alles auch in weitesten Kreisen einen 93 sanften Schlaf.",
      "Und es muß schon einmal gesagt werden: Man hat sich noch nicht recht daran gewöhnt, wie sehr es notwendig ist, anthroposophisches Wirken in die moderne Zivilisation hineinzutragen. - Man sollte sich daran ge- wöhnen, und ich sehne den Tag herbei, an dem ich Reich- licheres berichten kann auf die Frage hin nach dem Welt- schulverein. Heute könnte ich noch immer nicht viel mehr sagen, als was ich am Ende der Hochschulkurse hier im vorigen Herbst gesagt habe, obwohl das, was ich gesagt habe, darauf berechnet war, daß heute etwas ganz anderes darüber berichtet werden könnte.",
      "Aber so geht es auch mit anderen Dingen, und es ist sehr schwierig, gerade die Punkte, auf die es eigentlich ankommt in der heutigen Zeit, der heutigen Welt zum Be- wußtsein zu bringen. Ich habe in einem Berliner Vortrage, nachdem Lloyd George nach einem Streik in England, der schon ausge- brochen war, ein Zusammenleimen gemacht hat, darauf hingewiesen, daß man mit solchen Dingen nichts erreicht, daß das nur eine Vertagung ist.",
      "Die Leute haben es, wie es scheint, dazumal für eine Phrase genommen. Nun, bitte, überzeugen Sie sich heute, Sie könnten das schon seit eini- gen Tagen tun, ob das, was ich dazumal gesprochen habe, eine bloße Phrase war, oder ob es nicht vielleicht doch aus einer tieferen Erkenntnis der sozialen Zusammenhänge und der Notwendigkeit der sozialen Zusammenhänge her- vorgegangen ist.",
      "Das ist das Schwierige, daß man heute so wenige Men- schen mit jener Begeisterung findet, die ein wirkliches inneres Dabeisein bewirkt mit dem, was sie ja immerhin auch gern hören. Und deshalb freue ich mich immer, wenn sich Jugend findet, die etwas darüber zu sagen hat, wie sie das oder jenes, was sie sucht, da oder dort noch findet.",
      "Denn ich glaube, aus solchen Impulsen wird doch das her- vorgehen, was wir zu aller Einsicht, zu allem Verstehen brauchen: innerliches Dabeisein, innerliches Dabeisein, das weiß, wie stark die Metamorphose sein muß, die uns von den Niedergangskräften einer alten Zivilisation zu den Impulsen der neuen Zivilisation führt. Jawohl, wir brau- chen gewissenhaftes Verständnis, wir brauchen eine ein- dringliche Einsicht.",
      "Wir brauchen aber auch vor allen Din- gen das, was die Jugend aus ihren Naturanlagen heraus bringen könnte. Wir brauchen aber nicht nur in der Jugend, wir brauchen in den weitesten Kreisen der gegenwärtigen zivilisierten Menschheit nicht nur Einsicht, nicht nur ein- dringliches Verständnis der Wahrheit, wir brauchen Begei- sterung für die Wahrheit! 95"
    ],
    "sentences": [
      [
        "Wenn ich heute versuche, den Übergang zu machen vom eigentlichen philosophischen Gebiete in das Gebiet der speziellen Fachwissenschaften, so ist dieser Übergang in unserer gegenwärtigen Zeitepoche ganz naturgemäß über eine Anschauung des mathematischen und des physikali- schen, chemischen, das heißt des anorganischen Naturgebie- tes zu bewerkstelligen: weil weitaus die meisten der gegen- wärtigen philosophischen Vorstellungen so aufgebaut sind, daß die Philosophen ihnen das zugrunde legen, was sie an Begriffen und Ideen aus jenem Wissenschaftsgebiet gewon- nen haben, das heute als das sicherste gilt, aus dem mathe- matischen und dem der anorganischen Naturwissenschaft.",
        "Wenn man die heute so beliebte mathematische Behand- lung des Gebietes der anorganischen Naturwissenschaften besprechen will, muß immer wiederum an etwas erinnert werden, das schon in der Eröffnungsrede erwähnt worden ist: an die Anknüpfung, welche das gegenwärtige Denken glaubt an Kant machen zu können gerade mit der Einfüh- rung der Mathematik in die anorganischen Naturwissen- schaften, ja, in die Wissenschaft überhaupt."
      ],
      [
        "Worauf in diesem und auch in einem späteren Zusam- menhange von der negativen Seite her, ich sage ausdrück- lich von der negativen Seite her, wird aufmerksam gemacht werden müssen, das wurde auch schon bemerkt von ein- zelnen Denkern, die sehr weit abstehen von dem Gebrauche übersinnlicher Erkenntnisse.",
        "So wird man das Nega- 60 tive, das heißt das Zurückweisen des rein mathematischen Behandeins der Naturwissenschaft, zum Beispiel selbst bei einem Denker wie Fritz Mauthner, ganz trefflich finden, wie er aus einem gewissen Scharfsinn heraus in negativer Beziehung, das heißt im Zurückweisen desjenigen, was als falsche Ansprüche einer falschen Wissenschaftlichkeit auf- tritt, durchaus nicht unglücklich ist."
      ],
      [
        "Und in bezug auf die Frage: Was kann die gegenwärtige Wissenschaft nicht? kann man gerade von einem Denker wie Fritz Mauthner viel lernen, lernen durch das Negative, das er vorbringt, und lernen durch die Tatsache, daß er bei diesem Nega- tiven stehenbleiben, durchaus nicht vorwärtsdringen möch- te zu einer positiven Erkenntnis.",
        "Warum sollten Sie nicht auch von einem solchen nega- tiven Denker lernen?"
      ],
      [
        "Wenn ich gestern den Ausspruch Ludwig Hallers anführen konnte, daß nach seiner Mei- nung Kant dem Arsenal des Lichtes die Waffen entnom- men habe, um sie im Dienste der Finsternis zu verwenden, warum sollten Sie nicht auch dem Arsenal der Finsternis, sogar der gewollten Finsternis des Erkennens, wie sie sich bei Fritz Mauthner findet, die Waffen entlehnen, um sie im Dienste des Lichtes zu verwenden?",
        "Aufmerksam ist, wie gesagt, auf jenen Ausspruch Kants zu machen, der lautet, es finde sich in jeder einzelnen Dis- ziplin nur soviel eigentliche Wissenschaft, als Mathematik darin anzutreffen ist."
      ],
      [
        "Wenn man die Geschichte der Verwendung dieses Kan- tischen Ausspruches bis in unsere Tage herein studiert, dann bekommt man ein interessantes Beispiel zur Beant- wortung der Frage, wie man überhaupt in der neueren Zeit Kantianer ist.",
        "Denn die Leute, die sich auf diesen Ausspruch berufen, meinen, daß in jede einzelne Wissen- schaft so viel wirkliche Wissenschaftlichkeit hineingetragen werde, als Mathematik darinnen ist."
      ],
      [
        "Kant meint aber etwas ganz anderes.",
        "Kant meint: so viel er Mathematik in die Wissenschaft hineinträgt, so viel ist eben Mathema- tik, das heißt wirkliche Wissenschaft drinnen, und das andere ist eben in den einzelnen Wissenschaften überhaupt gar keine Wissenschaft."
      ],
      [
        "Sie sehen, man wird Kantianer, wenn man einen Kan- tischen Ausspruch gründlich mißversteht.",
        "Denn die Kant- schaft auf diesem Gebiete hat etwa die folgende Logik: Wenn ich sage, in einer Versammlung, in der tausend Menschen sind, ist so viel Genialität darinnen, als drei geniale Menschen hineingetragen haben, so meine ich ganz gewiß nicht, daß die tausend Menschen nun die Genialität der drei Menschen übertragen bekommen haben."
      ],
      [
        "Eben- sowenig meint Kant, daß das übrige in der Wissenschaft die Wissenschaftlichkeit der Mathematik bekommen habe; sondern er meint eben, daß nur der kleine Teil, der auch in den Wissenschaften Mathematik geblieben ist, wirkliche Wissenschaft, das andere aber überhaupt keine Wissen- schaft ist.",
        "Man muß solche Dinge im Ernste - und in einem em- pirischen Zeitalter sollte man das empirisch, nicht a priori tun studieren, damit sich solche Fragen nicht so beant- worten, wie es heute vielfach geschieht, sondern damit man der Wahrheit auf die Spuren kommt."
      ],
      [
        "Nun kann man aber noch auf etwas anderes hinweisen: Die hervorragendsten mathematischen Denker der neueren Zeit definieren die Mathematik etwa so: sie wäre die «Wissenschaft von den Größen».",
        "Nun ja, heute ist sie die Wissenschaft von den Größen."
      ],
      [
        "Aber man gehe nur ein paar Jahrhunderte zurück in die Zeit, in welcher Cartesius und Spinoza eine große Befriedigung daran gefunden haben, ihre Philosophie «nach mathematischer Methode» 6z darzustellen, wie sie sagen, und man wird finden, daß es etwas ganz anderes ist, was Cartesius und Spinoza als mathematische Methode in ihre Philosophie hineinbringen wollten als dasjenige, was in der neueren Zeit als Mathe- matik in die Naturwissenschaft hineingetragen werden soll.",
        "Gehen wir bis zu Cartesius und Spinoza zurück, dann finden wir, daß diese beiden Philosophen ihr philosophi- sches System so aufstellen wollen, daß eine ebenso große Sicherheit im Übergang von einem Satz zum anderen herrscht, wie sie in der Mathematik herrscht."
      ],
      [
        "Das heißt, sie wollen ihre Philosophie aufbauen nach dem Muster dieser mathematischen Methoden; aber nicht, sie wollen in ihre Philosophie das hineintragen, was man heute unter Mathematik versteht.",
        "Da haben wir also bereits, indem wir so zu Cartesius und Spinoza zurückgehen, mit dem Worte Mathematik einen ganz anderen Sinn verknüpft."
      ],
      [
        "Wir haben - mit Absehen von dem, was sich bloß auf Größen bezieht den Sinn verknüpft des inneren sicheren Übergehens von Urteil zu Urteil, von Schluß zu Schluß.",
        "Wir haben die Art des mathematischen Denkens ins Auge gefaßt, nicht das, was wir eine Größenwissenschaft nen- nen können."
      ],
      [
        "Und gehen wir noch weiter zurück.",
        "Dann bekommt in älteren Zeiten das Wort «Mathematik» überhaupt einen ganz anderen Sinn.",
        "Dann ist es identisch mit dem Worte Wissenschaft.",
        "Das heißt, man hat, wenn man «Wissen- schaft» gemeint hat, von «Mathesis» oder «Mathematik» gesprochen, weil man im Mathematisieren die Sicherheit des inneren Durchschauens eines im Bewußtsein vorhan- denen Tatbestandes fand."
      ],
      [
        "Man verband mit diesem Worte den Sinn «Wissen» und «Wissenschaft».",
        "Und so ist ein viel allgemeinerer Begriff auf das enge Gebiet der Grö- ßenlehre übertragen worden. 63 Heute haben wir alle Veranlassung, uns an solche Dinge zu erinnern, weil wir in die Notwendigkeit versetzt sind, wiederum auf das hinzuschauen, was im mathematischen Denken eigentlich vorliegt."
      ],
      [
        "Was ist das Wesentliche des mathematischen Denkens?",
        "Das Wesentliche des mathe- matischen Denkens ist eben die Durchschaubarkeit der mathematischen Bewußtseinsinhalte.",
        "Wenn ich ein Dreieck aufzeichne, seine drei Winkel ins Auge fasse, Alpha, Beta, Gamma, und den Beweis liefern will, daß die Summe dieser drei Winkel 180 Grad ist, dann mache ich das Folgende (siehe Abbildung 1): Ich ziehe zur Grundlinie eine Parallele durch den obersten Punkt des Dreiecks, betrachte mir das Verhältnis der Winkel Alpha und Gamma zu den an der Parallele entstehenden Wechsel- winkeln und habe dann, indem ich überschaue, wie sich die drei Winkel, welche an der Parallele entstehen - Gamma', Alpha', und Beta -, aneinander lagern, und wie sie einen Winkel von 180 Grad bilden, den Beweis, daß auch die drei Winkel des Dreiecks 180 Grad sind."
      ],
      [
        "Das heißt, was bis in die Beweisgänge hinein im Mathemati- schen als Bewußtseinstatbestand vorhanden ist, das ist überschaubar, das wird vom Anfang bis zum Ende von innerlichem Erleben begleitet.",
        "Und darauf beruht die Sicherheit, die man im Mathematisieren fühlt: daß alles, was als Bewußtseinsbestand vorliegt, von innerlichem Er- 64 leben begleitet wird bis zum Urteil und bis zum Beweis hin."
      ],
      [
        "Und wenn man dann die äußere Natur betrachtet, in deren materielle Grundlagen man mit einer solchen Über- schaubarkeit nicht hineindringen kann, dann fühlt man sich im Betrachten der äußeren Natur dennoch befriedigt, wenn man wenigstens ihre Erscheinungen in dem Erleben verfolgen kann, das einem zuerst in der Überschaulichkeit entgegengetreten ist.",
        "Die Sicherheit, die man in dieser Überschaubarkeit des Bewußtseinsbestandes beim Mathematischen fühlt, tritt besonders dann zutage, wenn man auf das eingeht, was von allen Seiten als ein großer Fortschritt im Mathema- tischen innerhalb des 19."
      ],
      [
        "Jahrhunderts angesehen wird: was als «nichteuklidische Geometrie», als «Metageometrie» bei Lobatschewskij, Bolyai, Legendre und so weiter her- vorgetreten ist.",
        "Da sehen wir, wie man - im Grunde genommen doch bauend auf die innere Sicherheit des Anschauens zuerst die euklidischen Axiome abändert und durch Abänderung der euklidischen Axiome mögliche andere Geometrien als die euklidische aufbaut, und wie man dann versucht, mit dem, was man da als eine Erweiterung der Anschaulich- keit aufgebaut hat, gegenüber einer undurchschaubaren Wirklichkeit zurechtzukommen."
      ],
      [
        "Alle Vorstellungen, die durch diese «Metageometrie» in das moderne Denken ein- gezogen sind, sind im Grunde genommen ein Tatsachen- beweis für die Sicherheit, die man in dem Überschau- baren des Mathematisierens fühlt.",
        "Und niemand wird mit Bezug auf den euklidischen Raum - denn die Räume der anderen Geometrien sind eben andere Räume -, der ja dadurch charakterisiert ist, daß drei aufeinander senkrecht stehende Koordinaten- achsen bis in die Unendlichkeit hinein in ihren Richtungen aufeinander senkrecht gestellt gedacht werden müssen, daran zweifeln, daß für diesen euklidischen Raum gilt, was hier als Beweis für die 180-Gradigkeit der drei Win- kel eines Dreiecks hingestellt worden ist."
      ],
      [
        "Und jeder wird sich klar sein darüber, daß, wenn er die euklidischen Axiome abändert, dies vielleicht Beziehung habe auf un- seren Raum, in dem wir sind - der ist eben dann nicht der euklidische Raum, der ist vielleicht ein innerlich ge- krümmter Raum -, aber daß für den euklidisch überschau- baren Raum die euklidischen Resultate wegen ihrer Durchschaubarkeit als sicher angenommen werden müssen.",
        "Daran wird niemand zweifeln."
      ],
      [
        "Und gerade wenn man diese Tatbestände durchschaut, dann wird man finden: die Anwendung der Mathematik auf das Gebiet der Naturwissenschaft beruht darauf, daß man in der Außenwelt das erst innerlich Gefundene wieder findet, daß gewissermaßen die Tatsachen der Außenwelt sich so verhalten, wie es den mathematischen Ergebnissen entspricht, die wir erst unabhängig von dieser Außenwelt in innerer Anschauung gefunden haben.",
        "Aber eines ist durchaus zu konstatieren: Die, ich möchte sagen, Vorausbedingung für diese innerliche Anschauung des Mathematischen ist, daß dieses Mathematische uns zuerst als Bild entgegentritt."
      ],
      [
        "Jene innere freie Tätigkeit des Konstruierens, die wir im Mathematisieren erleben, ist eine solche innere freie Tätigkeit nur dadurch, daß in ihr nichts waltet von dem, was sonst innerhalb unserer mensch- lichen Wesenheit waltet, wenn wir zum Beispiel, einem Instinkt folgend, wollen oder dergleichen.",
        "Aus diesem ist gewissermaßen bis zur Bildhaftigkeit herausgehoben, was als Bewußtseinsbestand im Mathematisieren auftritt."
      ],
      [
        "Das Mathematische ist in bezug auf das, was «äußerliche Na- 66 turwirklichkeit» ist, Unwirklichkeit.",
        "Und wir fühlen die Befriedigung in der Anwendung des Mathematischen auf die Naturerkenntnis gerade dadurch, daß wir das frei in Bildlichkeit Erfaßte im Reiche des Seins wieder erkennen können."
      ],
      [
        "Aber gerade daraus wird man zugeben müssen, daß es auf der einen Seite berechtigt ist, wenn solche Geister, die nicht bloß auf das gehen wollen, was die Naturwirklich- keit als solche in der menschlichen Anschauung als wirklich zeigt, sondern die auf das Volle, Totale der Wirklichkeit gehen wollen, wie Goethe, wenn solche Geister das hat Goethe besonders bei der Behandlung der «Farbenlehre» klar gezeigt - nicht eine totale Anwendung des Mathema- tischen auf die ganze äußere Wirklichkeit wollen.",
        "Goethes Ablehnen der Mathematik ging gerade aus der Erkenntnis hervor, daß man zwar dasjenige, was der bildhaften An- schaulichkeit des Mathematischen entspricht, in der äuße- ren Natur durch Mathematik finden kann, daß man aber damit zu gleicher Zeit Abstand nimmt von allem Qualita- tiven."
      ],
      [
        "Goethe wollte bei der Behandlung der äußeren Natur nicht bloß das Quantitative, er wollte auch das Qualitative einbezogen haben.",
        "Auf der anderen Seite aber muß man sagen, daß die ganze innerliche Größe der Mathematik auf ihrer Bildlich- keit beruht, und daß gerade in dieser Bildlichkeit das- jenige zu suchen ist, was ihr den Charakter einer apriori- schen Wissenschaft gibt, einer Wissenschaft, die rein durch innere Anschauung zu finden ist."
      ],
      [
        "Aber damit ist man zu gleicher Zeit, indem man mathe- matisiert, gerade aus dem Natursein, demgegenüber die Mathematik einen ganz besonders interessiert, eigentlich draußen.",
        "Man ergreift nirgends ein In-sich-Wirksames, sondern nur die durch die mathematischen Formeln aus- drückbaren Beziehungen dieses Wirksamen."
      ],
      [
        "Wenn Sie in mathematischen Formeln eine zukünftige Mondenfinster- nis oder, mit Einsetzung entsprechender Größen in nega- tiver Form, eine in früherer Zeit vorübergegangene Mon- denfinsternis errechnen, so müssen Sie sich bewußt sein, daß Sie niemals in das innere Wesen desjenigen eindringen, was da geschieht, sondern nur von einem gewissen Ge- sichtspunkte aus die Quanten von Verhältnissen mit mathematischen Formeln umfassen.",
        "Das heißt, man muß sich klar sein, daß man niemals in das innerlich wesenhaft Differenzierte durch das Mathematische hineindringen kann, wenn man dieses Mathematische in dem engen Sinne faßt, in dem es noch heute vielfach gefaßt wird."
      ],
      [
        "Aber schon sehen wir auch innerhalb des Mathemati- schen eine Art Weg, der aus dem Mathematischen selber herausführt.",
        "Aus dem, was ich eben gesagt habe, können Sie entnehmen, daß dieser Weg, der aus dem Mathemati- schen herausführt, ähnlich sein müßte dem Weg, den wir durchlaufen, wenn wir mit dem ganz bildhaft Mathemati- schen, mit dem undurchkrafteten, unwirksam bildhaften Mathematischen nun untertauchen in die durchkraftete und durchkraftende Natur."
      ],
      [
        "Da tauchen wir in etwas unter, was uns gewissermaßen mit unserer freien mathematisie- renden Tätigkeit abfängt und die mathematischen Formeln in ein Geschehen einzwängt, das in sich wirksam ist, das in sich etwas ist, von dem wir uns sagen müssen: wir kommen nicht vollständig heran mit dem Mathematischen; das Ding behauptet gegenüber der innerlichen Durchschaubarkeit des Mathematischen seine wesenhafte Selbständigkeit und sein wesenhaftes Innensein.",
        "Dieser Weg, der da gegangen wird, wenn man einfach den Übergang sucht von der irrealen mathematischen Den- kungsart zu der realen naturwissenschaftlichen Denkungs- 68 art, kann in einer gewissen Weise heute schon innerhalb des Mathematischen selber in einer gewissen Beziehung gefunden werden."
      ],
      [
        "Und wir sehen, wie er gefunden werden kann, wenn wir nicht äußerlich, sondern innerlich die Ver- suche betrachten, welche das Denken gemacht hat beim Übergang von der bloß analytischen Geometrie zu der projektivischen oder synthetischen Geometrie, wie sie die neuere Wissenschaft vorstellt.",
        "Ich möchte an einem ganz elementaren, an einem allerelementarsten und bekannte- sten Beispiel der synthetischen Geometrie erläutern, was ich mit dem eben ausgesprochenen Satze meine."
      ],
      [
        "Wenn man synthetische, neuere projektivische Geome- trie treibt, so unterscheidet man sich von dem analytischen Geometer dadurch, daß der analytische Geometer mit mathematischen Formeln rechnet, daß er also rechnet, daß er zählt und so weiter.",
        "Als synthetischer Geometer benützt man ich meine das jetzt natürlich ideell nur das Lineal, den Zirkel und das, was durch Lineal und Zirkel im Bewußtsein als Tatbestand auftreten kann, was aus der Anschauung zunächst hervorgeht."
      ],
      [
        "Fragen wir uns aber, ob es auch rein innerhalb der Anschauung verbleibt.",
        "Denken wir uns eine Linie - was man in der gewöhn- lichen Geometrie eine Linie nennt und auf dieser Linie drei Punkte.",
        "Dann haben wir das folgende mathematische Gebilde (siehe Abbildung 2): eine Linie, auf der sich die drei Punkte I, II, III befinden."
      ],
      [
        "Es gibt nun - ich kann, was ich hier anzuführen habe, natürlich nur in den Hauptlinien andeuten, gewissermaßen appellierend an das, was Sie über die Sache schon wissen - ein anderes Gebilde, welches in einer gewissen Weise in seiner ganzen Konfiguration entsprechend ist diesem eben aufgezeichneten mathematischen Gebilde.",
        "Und dieses andere Gebilde entsteht dadurch, daß ich drei Linien in 69 einer ähnlichen Weise behandle, wie ich diese drei Punkte hier behandelt habe, und daß ich einen Punkt in einer ähn- lichen Weise behandle, wie ich hier die Linie behandelt habe."
      ],
      [
        "Denken Sie sich also, ich zeichne statt der drei Punkte I, II, III, drei Linien an die Tafel, und statt der Linie, welche durch die drei Punkte geht, zeichne ich einen Punkt (siehe Abbildung 3); und damit eine Entsprechung entstehe, nehme ich den Punkt, in dem sich die drei Linien schneiden: Ich habe hier ein anderes Gebilde gezeichnet (Abb. 3).",
        "Der Punkt, den ich oben mit einem kleinen Ringelchen ge- zeichnet habe, entspricht der Linie links, die drei, wie man sie nennt, Strahlen, die sich in einem Punkt schneiden, und die ich mit I, II, III bezeichne, die entsprechen den drei Punkten I, II, III, die auf der Linie links liegen (Abb. 2)."
      ],
      [
        "Sie müssen, wenn Sie das ganze Gewicht dieses eben aus- gesprochenen Urteiles empfinden wollen, genau den Wort- laut nehmen, wie ich ihn eben ausgesprochen habe.",
        "Sie müssen sagen: der Punkt rechts (Abbildung 3), den ich oben mit einem kleinen Ringelchen bezeichnet habe, ent- spricht der Linie links (Abbildung 2), auf der die drei Punkte liegen; und die Strahlen I, II, III rechts entspre- 7° chen den Punkten I, II, III links."
      ],
      [
        "Und indem sich die drei Strahlen I, II, III rechts in dem einen Punkt oben schnei- den, entspricht dieses ihr Schneiden dem Liegen der drei punkte links I, II, III auf der links gezeichneten geraden Linie.",
        "So ausgesprochen, liegt ein ganz bestimmter Bewußtseins- tatbestand vor und ein entsprechendes Gebilde links gegen- über dem Gebilde rechts."
      ],
      [
        "Man kann nun indem man zunächst rein innerhalb desjenigen bleibt, was anschaulich ist, was sich also kon- struieren läßt mit Zirkel und Lineal, wozu kein Rechnen nötig ist - zu dem folgenden Bewußtseinstatbestande über- gehen: Ich zeichne links noch einmal eine Linie, und noch einmal auf dieser Linie drei Punkte (die untere Linie in Abbildung 4).",
        "Ich habe nun - ich bitte, jetzt ganz genau die Ausdrucks- weise, die ich befolgen werde, als maßgeblich zu betrachten für den Tatbestand -, ich habe nun links die Linie gezeich- net, auf welcher sich die drei Punkte 1, 2, 3 liegend befin- den."
      ],
      [
        "Ich werde weitergehen und nehme an - bitte wohl zu beachten das Wort, das ich ausspreche: «und nehme an» -, ich werde weiter das Folgende tun und nehme dann etwas an.",
        "Ich werde in einer gewissen Weise die Punkte links 71 von der einen Linie mit den Punkten von der anderen Linie verbinden und werde dadurch Verbindungslinien be- kommen, die sich schneiden werden (siehe Abbildung 5)."
      ],
      [
        "Ich werde verbinden links in meinem Gebilde den Punkt I mit dem Punkt 3, den Punkt III mit dem Punkt I, den Punkt I mit dem Punkt 2, den Punkt II mit dem Punkt I, den Punkt III mit dem Punkt 2, den Punkt II mit dem Punkt 3, und werde durch diese Linien Schnittpunkte be- kommen, die ich dann wiederum - ich nehme es jetzt an - durch eine gerade Linie verbinden kann.",
        "Also meine Kon- struktion sei in anschaulicher Durchsichtigkeit so ausge- führt, daß ich das wirklich vollziehen könne, was ich jetzt angegeben habe."
      ],
      [
        "Man kann nämlich diese Konstruktion so ausführen (punktierte Linie in Abbildung 5): Sie sehen, ich habe die drei Schnittpunkte, die ich auf die vorhin be- schriebene Weise bekommen habe, so bekommen, daß ich durch sie die hier strichpunktierte Gerade ziehen kann.",
        "Ich nehme nun an, daß ich, indem ich zu dem rechten Strahlenbüschel (Abbildung 3), so nennt man es, ein anderes hinzufüge, daß ich in dem Verhältnis der Aus- strahlung dasselbe Verhältnis drinnen habe wie in der Entfernung der auf der linken Geraden liegenden Punkte."
      ],
      [
        "Ich werde also ein zweites Strahlenbüschel rechts hinein- 72 zeichnen (Abbildung 6), das in bezug auf seine Ausstrah- lungsverhältnisse den Lagenverhältnissen der Punkte auf den Linien links entspricht.",
        "Ich habe also hier (Abbil- dung 6) ein anderes Strahlenbüschel hineingezeichnet und nenne es 1, 2, 3, indem ich annehme, daß 1, 2, 3 in bezug auf die Strahlen rechts entspricht 1, 2, 3 in bezug auf die Punkte links."
      ],
      [
        "Und ich werde jetzt die entsprechende Prozedur bei meinen zwei Strahlengebilden rechts ausführen, die ich links (Abbildung 5) bei meinen Linien- und Punktgebilden ausgeführt habe, nur muß ich berücksichtigen, daß einer Linie links ein Punkt rechts entspricht: während ich links eine Linie gesucht habe, die zwei Punkte verbindet, muß ich rechts einen Punkt suchen, der entsteht, indem zwei Strahlen sich schneiden.",
        "Das Schneiden rechts soll entspre- chen dem Verbinden links (die Schnittpunkte in Abbil- dung 6 werden durch kleine Kreise markiert, siehe Abbil- dung 7)."
      ],
      [
        "Sie sehen, was ich gemacht habe: wenn ich links III mit 1 und 3 mit I als Punkte verbunden habe, habe ich 73 hier rechts I mit 3 und 1 mit III als Linien zum Schnitt gebracht.",
        "Und wenn ich links zwei Linien gezogen habe von Punk- ten aus und sie zum Schnitt gebracht habe in einem Punkt, so werde ich jetzt entsprechend rechts durch die beiden Punkte, die ich bekommen habe, eine Linie ziehen (strich- liert in Abbildung 7), und ich werde dieselbe Prozedur mit Bezug auf die anderen Strahlen jetzt ausführen."
      ],
      [
        "Das heißt [der Vortragende verdeutlicht nochmals die Entsprechung der geringelten Schnittpunkte von Abbildung 7 mit den Verbindungslinien von Abbildung 5], ich werde II mit 1 zum Schnitt bringen, I mit 2, III mit 2, II mit 3; ich werde also rechts die Schnittpunkte suchen, wie ich links die Ver- bindungslinien gesucht habe; und, wie Sie sehen, habe ich rechts durch das Zum-Schnitt-Bringen der Strahlen diese Schnittpunkte gesucht, um Linien durch diese Schnitt- punkte zu ziehen (strichliert in Abbildung 7), wie ich links durch das Verbinden der Punkte Linien gesucht habe, um 74 die Schnittpunkte dieser sich schneidenden Linien zu ge- winnen (geringelt in Abbildung 5).",
        "Die Verbindungslinien aber der Schnittpunkte, die ich rechts gewonnen habe, schneiden sich ebenso in einem hier durch ein Ringelchen bezeichneten Punkt oben (P in Ab- bildung 7), wie die drei Punkte, die ich links bekommen habe, in einer geraden Linie liegen (strichliert in Abbil- dung 5)."
      ],
      [
        "Das heißt, im Gebilde rechts, wo statt der Punkte Linien, statt der Verbindungslinien Schnittpunkte sind, be- komme ich, wie ich links eine Linie bekommen habe, die durch die drei Punkte geht, einen Punkt, in dem sich die drei Geraden schneiden.",
        "Ich bekomme rechts wiederum einen Punkt für die Linie links."
      ],
      [
        "Hier bleibe ich, indem ich rein vom Gebiete des An- schaulichen ausgehe, zwar innerhalb desjenigen, was von der Anschauung ausgeht, was aber doch zu etwas anderem führt.",
        "Und ich bitte Sie, das Folgende zu berücksichtigen."
      ],
      [
        "Nehmen Sie an, Sie schauen in der Linie, in der Richtung, die angegeben wird durch die (gestrichelte) Linie links, die durch die drei Schnittpunkte - Alpha, Beta, Gamma - geht, dann werden Sie auf einen Schnittpunkt aufschauen, der die anderen verdeckt, gegenüber dem die anderen hinter ihm sind (Abbildung 8).",
        "Sie haben hier, in der Linie auseinandergelegt, nicht nur «drei Punkte»."
      ],
      [
        "Sondern so- bald man zu einem Wirklichkeitsverhältnis übergeht, tritt gegenüber diesen drei Punkten etwas auf, was ganz an- schaulich ist: der Punkt Gamma ist der Vordere, und hinter ihm sind die Punkte Beta und Alpha.",
        "Das haben Sie in der linken Figur klar auseinandergelegt in der An- schauung."
      ],
      [
        "Gehen wir jetzt durch eine ganz gesetzmäßige Prozedur, die ich beschrieben habe, über zu dem rechts entsprechen- den Gebilde, so haben wir statt der Linie einen Punkt ins 75 Auge zu fassen (P in Abbildung 9).",
        "Wenn wir ihn ins Auge fassen, so müssen wir sagen, geradeso wie links durch die Verbindung von III mit 2 und die Verbindung von 3 mit II ein Schnittpunkt entsteht, Gamma, der die anderen Schnittpunkte zudeckt, so daß das Verhältnis entsteht: Gamma ist vorn, Alpha ist hinten, so entsteht rechts die Notwendigkeit, das Folgende vorzustellen und damit, durch das Verbindungsgesetz, aus dem Anschaulichen ins Unanschauliche überzutreten: Rechts (Abbildung 9) ent- steht die Notwendigkeit, den geringelten Punkt (P) so vorzustellen, daß der Strahl (Gamma), der durch die Ver- bindung der Schnittpunkte der Linien III und 2, II und 3, entsteht, sich zunächst in dem geringelten Punkt mit dem- jenigen Strahl (Beta) schneidet, der durch das voran- liegende Verhältnis (III mit 1, I mit 3) entsteht; und wir müssen uns vorstellen, daß innerhalb dieses geringelten Punktes die Schnitte, die durch die drei strichlierten Strah- 76 len entstehen, ebenso als drei innerlich differenzierte Enti- täten liegen wie links auf der strichpunktierten Linie die drei Punkte Gamma, Beta, Alpha."
      ],
      [
        "Das heißt, ich muß die Schnitte rechts im einzelnen Punkt so angeordnet finden, daß sie sich übereinander decken.",
        "Das heißt mit anderen Worten nichts Geringeres als: Geradeso wie ich für ein hinschauendes Auge die strich- punktierte Linie links so zu denken habe, daß für die Punkte Gamma, Beta, Alpha ein Vorne und Hinten ent- steht, so habe ich innerhalb des Punktes, das heißt einer Raumausdehnung von Null, nach allen drei Dimensionen eine Differenzierung zu denken."
      ],
      [
        "Ich habe in diesem Punkte angeschaut aus der Art heraus, wie er aus diesem Gebilde entstanden ist - nicht etwas Undifferenziertes, sondern ein Vorne und Hinten zu denken.",
        "Ich bekomme hier die Notwendigkeit, einen Punkt nicht neutral nach allen Seiten zu denken, sondern den Punkt zu denken mit einem Vorne und Hinten."
      ],
      [
        "Ich mache hier einen Weg, durch den ich aus dem freien Bilden des Mathematischen hineingezwungen werde in etwas, wo das Objektive zu einer Eigenbestimmung, zu einem Innensein übergeht.",
        "Sie sehen, dieser Weg ist ähn- lich demjenigen, durch den ich übergehe von dem mathe- matisch freien Bilden zu dem In-Empfang-Nehmen dieses Bildens vom innerlichen Bestimmtsein innerhalb der Naturordnung."
      ],
      [
        "Und ich bekomme, indem ich von der analytischen zu der synthetischen Geometrie übergehe, den Anfang des Weges, der mir gezeigt wird von der Mathe- matik zur anorganischen Naturwissenschaft.",
        "Es ist dann im Grunde genommen nur noch ein kleiner Weg zu etwas anderem."
      ],
      [
        "Man kann, indem man diese Er- wägungen, auf die ich jetzt hingedeutet habe, fortsetzt, zum innerlichen Begreifen auch des folgenden Bewußtseins- 77 tatbestandes kommen: Wenn man rein mit Hilfe der pro- jektiven, der synthetischen Geometrie verfolgt, wie sich ein Hyperbel zu einer Asymptote verhält, so bekommt man rein anschaulich heraus, daß nach der einen Seite, sa- gen wir rechts oben, die Asymptote sich dem Hyperbelast nähert, aber ihn niemals erreicht, daß man aber dennoch die Vorstellung bekommt, die Hyperbel komme wiederum von links unten zurück mit dem anderen Ast, und die Asymptote komme ebenfalls von links unten zurück mit ihrer anderen Seite.",
        "Mit anderen Worten: ich bekomme durch dieses Verhältnis von Asymptote zur Hyperbel etwas, was ich etwa in der folgenden Art Ihnen auf die Tafel zeichnen könnte (Abbildung 10): Rechts oben geht die Asymptote, die gerade Linie, im- mer näher an die Hyperbel heran."
      ],
      [
        "Ich habe dort eine Schraffierung hinzugefügt, um auszudrücken, was für ein Verhältnis die Asymptote eigentlich zum Hyperbelast hat.",
        "Sie kommt ihm immer näher, sie will an ihn heran, sie kommt immer näher und näher in das Sein ihres Verhält- 78 nisses zu ihm hinein."
      ],
      [
        "Wenn man nun dieses Verhältnis ver- folgt nach rechts oben, so kommt man zuletzt durch rein projektives Denken ich kann das hier nur andeuten dazu, die Richtung der Linie, die man nach rechts oben hat, sei es die Hyperbel, sei es die Asymptote, von links unten wieder herkommend, zu finden, den Hyperbelast und die Asymptote, und diese so, daß sie mit ihrem Sein in der schraffierten Andeutung den Hyperbelast immer mehr und mehr verläßt.",
        "So daß wir sagen können: diese Asymptote hat eine merkwürdige Eigenschaft."
      ],
      [
        "Indem sie nach rechts oben hinansteigt, wendet sie sich mit ihrem Verhältnis zur Hyperbel der Hyperbel zu, indem sie von links unten wieder heraufkommt, wendet sie sich mit ihrem Verhält- nis zur Hyperbel von der Hyperbel ab.",
        "Diese Linie, die Asymptote, hat, wenn ich sie in ihrer Vollständigkeit, Totalität betrachte, wiederum ein Vorne und Hinten."
      ],
      [
        "Des- halb konnte ich auch die Schraffierung das eine Mal auf der einen Seite, das andere Mal auf der anderen Seite zeichnen.",
        "Ich komme wiederum in eine innere Differen- zierung des Linearen hinein, wie ich in eine innere Diffe- renzierung hineinkomme, wenn ich das rein mathematisch Bildhafte in das Gebiet des Naturgeschehens hineindränge."
      ],
      [
        "Das heißt, ich nähere mich dem, was als Differenzierung im Naturgeschehen auftritt, wenn ich in richtiger Weise mit Hilfe der projektiven Geometrie die mathematischen Ge- bilde selbst erfassen will.",
        "Was da durch die projektive Geometrie geschieht, das kann niemals in derselben Weise durch die bloße analy- tische Geometrie gemacht werden."
      ],
      [
        "Denn die bloße analy- tische Geometrie bleibt, indem sie also in Koordinaten konstruiert und dann in ihrer Rechnungsform die End- punkte der Abszissen und Ordinaten aufsucht, mit dem, 79 was sie konstruiert, in ihrer Form ganz außerhalb der Kurve oder außerhalb des Gebildes selber stehen.",
        "Die pro- jektive Geometrie bleibt nicht außerhalb der Kurve und des Gebildes stehen, sondern sie dringt in die innere Diffe- renzierung des Gebildes: bis zum Punkte, bei dem man unterscheiden muß ein Vorne und Hinten bis zur Gera- den, bei der man ebenfalls unterscheiden muß ein Vorne und Hinten."
      ],
      [
        "Ich habe nur diese Eigenschaften wegen der Kürze der Zeit angegeben, ich könnte noch andere Eigen- schaften angeben, zum Beispiel ein gewisses Krümmungs- verhältnis, das der nach den drei Raumdimensionen aus- gedehnte Punkt in sich hat und so weiter.",
        "Wenn man wirklich mit innerem Seelenanteil den Weg verfolgt, der da von der analytischen Geometrie in die synthetische Geometrie hineinführt, wenn man sieht, wie man da, ich möchte sagen, aufgefangen wird von etwas, was schon der Realität sich nähert, wie diese Realität im äußeren Naturdasein vorhanden ist, dann hat man das- selbe innere Erlebnis, genau dasselbe innere Erlebnis, das man hat, wenn man aufsteigt von dem gewöhnlichen Ver- standesbegriff, von der gewöhnlichen Logik, zu dem Ima- ginativen."
      ],
      [
        "Man muß im imaginativen Erkennen nur wei- tergehen.",
        "Aber den Anfang hat man gegeben, wenn man anfängt, von der analytischen Geometrie zu der syntheti- schen überzugehen.",
        "Man merkt da das Abgefangenwerden von dem, was sich aus der Bestimmtheit durch die äußere Realität ergibt, nach der man das Resultat gefaßt hat, und man merkt das ebenso im imaginativen Erkennen."
      ],
      [
        "Und nun, welches ist der entgegengesetzte Weg inner- halb der Geisteswissenschaft gegenüber demjenigen, der vom gewöhnlichen gegenständlichen Erkennen ins imagi- native Erkennen hineinführt?",
        "Es wäre derjenige, der von der Intuition oben zur inspirierten Erkenntnis hinunter- 80 führte."
      ],
      [
        "Da finden wir aber bereits, daß wir drinnenstehen im Realen.",
        "Denn mit der Intuition stehen wir im Realen drinnen.",
        "Und wir gehen weg vom Realen.",
        "Indem wir von der Intuition heruntersteigen zu der Inspiration, entfernen wir uns wiederum von dem Realen."
      ],
      [
        "Und wenn wir bis zur Imagination herunterkommen, haben wir nur noch das Bild des innerlich Realen.",
        "Dieser Weg, der ist zu gleicher Zeit derjenige, den das Reale durchmacht, um unser Erkenntnisobjekt zu werden."
      ],
      [
        "Natürlich, in der Intuition stehen wir in der Realität drinnen.",
        "Wir gehen von der Realität ab, zu der Inspira- tion, zu der Imagination, und kommen zu unseren gegen- ständlichen Erkenntnissen.",
        "Die haben wir dann in unserem heutigen Erkennen."
      ],
      [
        "Wir machen den Weg von der Realität zu unserem Erkennen herein.",
        "Wir stehen gewissermaßen zuerst innerhalb der Realität und kommen von dieser Realität ab zu dem irrealen Erkennen.",
        "Auf dem Weg, den wir zurücklegen von der analytischen Geometrie in die projektive oder synthetische Geometrie hinein, versuchen wir uns wiederum nach der entgegengesetzten Richtung zu bewegen, von der rein verstandesmäßigen analytischen Geometrie in dasjenige, wo wir anfangen können real zu denken, wenn wir überhaupt zu etwas kommen wollen."
      ],
      [
        "Wir gehen der Entrealisierung der Natur, die sie durch- macht, indem sie Erkenntnis werden will, entgegen, indem wir realisieren die irreale Erkenntnis.",
        "Sie sehen, man hat nicht etwa nötig, anzunehmen, daß unsere moderne Geisteswissenschaft, wie sie hier auftritt, anders mathematisieren wollte, als es die Mathematiker tun, wenn sie nur recht in ihrem Sinne mathematisieren."
      ],
      [
        "Man hat nicht einmal nötig - außer dem Aufsuchen von besonderen Versuchsanordnungen, die aus dem Quantita- tiven ins Qualitative hineinführen viel anderes zu tun 81 auf den Gebieten, die ja eine quantitative Naturwissen- schaft heute schon betreten hat.",
        "Und wenn diese äußere quantitative Naturwissenschaft heute der modernen An- throposophie ihre «gesunden Ergebnisse» entgegenhält, dann ist es ungefähr so, wie wenn jemand ein Gedicht vorgelesen hat, das in ganz andere Regionen geht, und einer kommt: Ja, da kann ich ja nicht entscheiden durch meine Seelenverfassung, ob man in einem Gedichte leben kann, ich aber weiß etwas ganz gewiß: daß zwei mal zwei vier ist! - Niemand bezweifelt, daß zwei mal zwei vier ist; ebensowenig bezweifelt dasjenige, was die moderne anorganische Naturwissenschaft gibt, wer zur Geisteswis- senschaft aufrücken will."
      ],
      [
        "Aber es ist gegen den Inhalt eines Gedichtes zum Beispiel just kein besonderer Einwand, wenn man ihm entgegenhält: zwei mal zwei ist vier.",
        "Es handelt sich aber darum, daß dasjenige, wohin die einzelnen Wissenschaften schon besonders tendieren, wohin sie wollen, daß das ernst und mutig als Weg zu einer wahren Wirklichkeitserkenntnis von Anthroposophie in Angriff genommen wird."
      ],
      [
        "Und während manche Leute heute in fruchtlosem Skeptizismus eine Finsternis errichten wollen über dem, was sie, oftmals mit Recht, als Grenzen des Naturerkennens empfinden, möchte Anthroposophie da, wo Naturwissenschaft finster wird, beginnen, das Licht des geistigen Erkennens zu entzünden.",
        "Und so wird sie vielleicht mit Bezug auf diejenigen Wissenschaften, die heute erwähnt worden sind, nicht ge- rade groß andere Methoden einschlagen; aber sie wird die Bedeutung, den inneren Seinswert der Wissenschaften, von denen heute gesprochen worden ist, vor die Menschheit hin- stellen und wird dadurch bewirken, daß man weiß, warum man mit Mathematik ins Sein eindringt, nicht bloß, warum man mit Mathematik zu einer gewissen Sicherheit kommt."
      ],
      [
        "Denn zum Schluß kommt es ja nicht darauf an, bloße Gewißheitsprodukte zu entwickeln.",
        "Da könnten wir uns im engsten Kreis abschließen und immer und immer wieder im engsten Kreise drehen, wenn wir bloß «das Gewisseste» festhalten wollten."
      ],
      [
        "Sondern es handelt sich um Erweite- rung des Erkennens.",
        "Die aber kann nicht gefunden wer- den, wenn man den Weg scheut aus dem inneren Erleben in das äußere, in sich selber differenzierte Sein.",
        "Dieser Weg wird vielfach sogar in der Mathematik und mathe- matischen Naturwissenschaft der Gegenwart angedeutet."
      ],
      [
        "Man muß ihn nur erkennen und dann im Sinne dieser Er- kentnis wissenschaftlich handeln.",
        "Schlußwort zur Disputation Dornach, 5.",
        "April 1921 Meine sehr verehrten Anwesenden!",
        "Ich will, zum Teil wegen der vorgerückten Zeit und zum Teil aus anderen Gründen, nicht mehr als ein paar Bemerkungen machen, die mit am heutigen Abend Vorgebrachtem, Vorgekom- menem, zusammenhängen."
      ],
      [
        "Da möchte ich zunächst auf die Frage betreffend Pro- fessor Rein ganz kurz zurückkommen aus dem Grunde, weil ein Umstand gerade in dieser Angelegenheit doch scharf hervorgehoben werden sollte.",
        "Daß von seiten eines Herbartianers, namentlich eines Herbartianers, der durch die historische Schule gegangen ist, über meine «Philosophie der Freiheit» nicht sonderlich viel Zustimmendes gesagt werden kann, das weiß ich sehr gut."
      ],
      [
        "Das hat sich ja auch gleich nach dem Erscheinen der «Philosophie der Freiheit» 1894 gezeigt.",
        "Denn eine der ersten Besprechungen, die erschienen sind über die «Philo- sophie der Freiheit», war die des Herbartianers Robert Zimmermann."
      ],
      [
        "Aber ich muß sagen, trotzdem diese Bespre- chung außerordentlich gegensätzlich war, hat sie mich ge- freut aus dem Grunde, weil damals im Gegensatz einige wirklich große Gesichtspunkte angeschlagen worden sind.",
        "Wie also notwendig das Verhältnis sein muß zwischen einer Herbartianer-Beurteilung und dem, was meine «Philosophie der Freiheit» enthält, darüber gebe ich mich nicht dem geringsten Zweifel hin."
      ],
      [
        "Allein, es ist schade, daß ich jetzt die Besprechung der «Philosophie der Frei- heit» durch Professor Rein nicht hier habe und das Zitat so belegen könnte, wie ich es gern tun würde. - Es ist mir nun soeben gebracht worden, und ich kann daher an der Hand der Besprechung manches noch genauer sagen, als es sonst möglich wäre.",
        "Da beginnt also diese Bespre- chung zunächst mit den Worten: «In Zeiten eines morali- schen Tiefstandes, wie ihn das deutsche Volk wohl noch nicht erlebt hat, ist es doppelt not, die großen Landmar- ken der Moral, wie sie von Kant und Herbart aufgerichtet worden sind, zu verteidigen und sie nicht zugunsten relati- vistischer Neigungen verrücken zu lassen."
      ],
      [
        "Das Wort des Freiherrn v.",
        "Stein, daß ein Volk nur stark bleiben kann durch die Tugenden, durch welche es groß geworden ist, lebendig zu halten, muß heute zu den ersten Aufgaben inmitten der Auflösung aller moralischen Begriffe gerech- net werden."
      ],
      [
        "Daß an dieser Auflösung eine Schrift des Führers der Anthroposophen in Deutschland, des Dr.",
        "Steiner, be- teiligt ist, muß besonders beklagt werden, da man den idealistischen Grundzug dieser Bewegung, die auf eine starke Verinnerlichung des Einzelmenschen hinzielt, nicht leugnen und in seinem Plan der Dreigliederung des sozia- len Körpers gesunde, das Volkswohl fördernde Gedanken finden kann."
      ],
      [
        "Aber in der Schrift (Berlin 1918) überspannt er seine individualistische Einstellung in einer Weise, die zur Auflösung der sozialen Gemeinschaft führen und deshalb bekämpft werden muß.» Sie sehen hier deutlich gesagt, daß die «Philosophie der Freiheit» herausentstanden sei aus der Auflösung aller mo- ralischen Vorstellungen und so weiter und das kann man ja auch glauben, daß es die Meinung eines Mannes sein kann.",
        "Nun, ein großer Teil der hier Anwesenden kennt meine Ansichten in bezug auf wissenschaftliche Genauigkeit, auf 85 wissenschaftliche Gewissenhaftigkeit, und vor allen Din- gen darüber, daß man sich über das, worüber man schreibt, zunächst ordentlich unterrichten soll."
      ],
      [
        "Die «Philosophie der Freiheit», die 1894 erschienen ist, auch nur stilistisch in Zusammenhang zu bringen mit dem, worauf hier gedeutet ist in den ersten Sätzen, ist eine Leichtfertigkeit.",
        "Und eine solche Leichtfertigkeit darf nicht damit entschuldigt wer- den, daß derjenige, der als ein Professor der Pädagogik an einer Hochschule wirkt, durchaus - wie ich glaube, daß es gesagt wurde - «nicht über die Grenze einer wirklich objektiven Beurteilung hinausgegangen» sei."
      ],
      [
        "Es handelt sich darum, daß wir eine Gesundung gerade derjenigen Verhältnisse, die heute abend hier in einer recht herzhaf- ten Weise besprochen worden sind, nur dann herbeiführen können, wenn wir uns derselben Leichtfertigkeit nicht schuldig machen, sondern wenn wir wissenschaftliche Ge- wissenhaftigkeit streng ausüben gerade denen gegenüber, die von Amts wegen den Beruf haben, erzieherisch auf die Jugend zu wirken.",
        "Da darf man dem, der diesen Beruf hat, nicht erlauben, zu übersehen, aus welchen Verhältnis- sen heraus und in welchen Zeiten eine Schrift, die man beurteilen will, entstanden ist."
      ],
      [
        "Das ist das erste, was ich zu sagen habe.",
        "Dann die Art und Weise des Zitierens.",
        "Sie finden in diesem Artikel eine unglaubliche Art, Sätze aus dem Zu- sammenhange herauszureißen und an herausgerissene Sätze dann nicht das anzuknüpfen, was in meiner «Philosophie der Freiheit» steht, sondern das, was der Artikelschreiber meint, nach seiner eigenen Meinung anknüpfen zu sollen, was aus der Deutung der Sätze, die er herausgerissen, nach seiner Meinung gefolgert werden kann."
      ],
      [
        "Wer sich die Mühe nimmt, die «Philosophie der Freiheit» wirklich durchzunehmen, der wird sehen, daß überall in 86 dieser «Philosophie der Freiheit» in vollständig klarer Weise auseinandergesetzt ist, wie das vermieden werden kann, was durch Professor Rein aus Mißverständnis an in beliebiger Weise aus dem Zusammenhang herausgeris- senen Sätzen moniert wird.",
        "Dem, was er über das Herausholen der «Philosophie der Freiheit» aus den Zeitverhältnissen schreibt, entspricht das Hineinstellen in unmögliche Zusammenhänge: «Hören wir so Herrn Dr."
      ],
      [
        "Steiner reden, so könnte man versucht sein, ihn als Apostel des ethischen Libertinismus anzusprechen.",
        "Er hat dies auch gefühlt und ist dem Einwand begegnet, der dahin geht: Wenn jeder Mensch nur danach strebt, sich auszuleben und zu tun, was ihm beliebt, dann gibt es keinen Unterschied zwischen guter Handlung und Ver- brechen."
      ],
      [
        "Jede Gaunerei, die in mir liegt, hat gleichen An- spruch, sich auszuleben, wie die Intention, dem allgemei- nen Besten zu dienen.",
        "Diesen Einwand sucht Dr.",
        "Steiner durch den Hinweis zu entkräften, daß der Mensch erst dann auf die geforderte Freiheit Anspruch erheben darf, wenn er die Fähigkeit erworben hat, sich zum intuitiven Ideengehalt der Welt zu erheben."
      ],
      [
        "Diese Fähigkeit sich an- zueignen, ist Aufgabe des Anthroposophen, der sich auf den Standpunkt des ethischen Individualismus erheben soll.» Nun, bitte, legen Sie sich die Frage vor, ob jemand als Beurteilung der «Philosophie der Freiheit» solche Sätze hinschreiben darf.",
        "Die «Philosophie der Freiheit» ist 1894 veröffentlicht, wo es noch keine «Anthroposophen» gege- ben hat."
      ],
      [
        "Also Professor Rein stellt die «Philosophie der Freiheit» auch in ein Milieu hinein, das überhaupt für die «Philosophie der Freiheit» zur Zeit ihres Erscheinens ein unmögliches war, abgesehen von den Trivialitäten, die dann kommen, wo er davon spricht, daß das eine Ethik für Anthroposophen und Engel und dergleichen wäre und so fort.",
        "Es handelt sich wirklich hier nicht darum, in irgend- einer Weise auf, ich möchte sagen, einen «gegenteiligen Standpunkt» irgendwie ein schiefes Licht werfen zu wol- len, sondern darum, daß diese Art, geistige Dinge zu be- urteilen, durchaus in die ganze Welt desjenigen hineinge- hört, was aus unserer Kultur heraus muß, wenn die Zu- stände, die heute hier besprochen werden sollten, besser werden sollen."
      ],
      [
        "Ich darf wohl sagen, daß ich mir gut über- legt habe, ob ich schließlich diese Worte hier aussprechen solle oder nicht.",
        "Aber mir scheint die Sache denn doch wich- tig genug zu sein, und ich glaube, daß ich die Grenze der Objektivität nicht überschritten habe, daß ich mich eigent- lich im wesentlichen darauf beschränkt habe, die Art und Weise des Urteilens und nicht den «Standpunkt» vor Ihnen hier zu charakterisieren."
      ],
      [
        "Ich weiß, daß man immer gewissermaßen auf dünnes Eis tritt, wenn allerlei Ver- wandtschaftliches vorgeführt wird.",
        "Allein, ich kann mich darnach nicht richten, obzwar ich ja auch sonst nicht ge- bunden bin, denn ich habe innerhalb der Professorenschaft keinen Schwiegervater!"
      ],
      [
        "Nun möchte ich noch einige andere Bemerkungen ma- chen und dazu an einen Satz anknüpfen, der heute auch hier besprochen worden ist.",
        "Wirklich nur, um symptoma- tisch zu sprechen, möchte ich da ein kleines Erlebnis vor- bringen, das aber nur illustrieren soll."
      ],
      [
        "Es ist gesagt worden, es sei richtig, daß nicht alle Stu- denten, die an eine Universität oder Hochschule kommen, auch reif seien für diese Hochschule; allein dafür könnten ja die Professoren an den Hochschulen nichts, sondern diese Studenten würden ihnen eben zugeschickt von den höheren Schulen.",
        "Ja, aber da konnte ich wirklich nicht an- 88 ders, als mir ein Gespräch einfallen lassen, das einmal mit einem der berühmtesten Literaturhistoriker an deutschen Universitäten in meiner Gegenwart geführt worden war."
      ],
      [
        "Dieser Literaturhistoriker war auch in der Prüfungskom- mission für das Gymnasiallehramt.",
        "Ich tue es eigentlich ungern; aber heute sind die Zeiten so ernst, daß man schon auch solche Dinge vorbringen muß. - Er sagte: Ja, mit diesen Gymnasiallehrern, wir kennen sie ja, wir müssen sie ja prüfen, aber wir haben manchmal ganz sonderbare Gedanken, wenn wir diese Kamele als Gymnasiallehrer auf die Gymnasien hinauslassen müssen!"
      ],
      [
        "Nun, es ist nur, wie gesagt, eine Illustration, die ich durch dieses Erlebnis geben möchte.",
        "Ich weiß nicht, ob es sehr stark für die Universitätslehrer spricht, wenn ein Prüfungskommissar und berühmter Universitätslehrer sich dazu herbeiläßt, diejenigen Lehrer der Jugend, die an die Gymnasien hinausgeschickt werden, «Kamele» zu nennen."
      ],
      [
        "Ich sage es nicht, aber der betreffende Mann hat es gesagt.",
        "Ich zitiere nur. - Nun, es muß schon jeder Gedanke zu En- de gedacht werden.",
        "Und da glaube ich, wenn der Gedanke zu Ende gedacht wird, daß sich die Universitätslehrer nicht beklagen dürfen, wenn unfähige Gymnasial-Abitu- rienten die Pforte der Universität betreten; denn die Uni- versitätslehrer haben ja erst die Gymnasiallehrer hinaus- geschickt, die ihnen diese Absolventen zugerichtet haben."
      ],
      [
        "Also schließlich ist es doch notwendig, wie gesagt, den Gedanken zu Ende zu denken.",
        "Und der zeigt uns, daß wir, wenn auch mit einiger Nachsicht, in einer gewissen Beziehung schon den Schuldbegriff anwenden dürfen."
      ],
      [
        "Aber es sind heute so sonderbare Worte gefallen, sehen Sie.",
        "Und da muß ich sagen, eines der sonderbarsten Worte, schon fast eine von den kleinen Pikanterien, war doch dies, daß gesagt worden ist, ein Universitätslehrer 89 hätte gesagt: Wir erwarten die Erlösung von der Studen- tenschaft! - Ich wundere mich nur, daß er dann nicht auch noch gesagt hat: Von dem Augenblicke, wo wir uns auf die Schulbänke setzen und die Studenten auf das Katheder hinauf befördern. - Sehen Sie, es ist schon notwendig, daß man den überall schleißig werdenden Urteilen, die so die Gegenwart durchschwirren und die dennoch überall die Veranlassung sind zu unseren heutigen Zuständen, daß man der Schleißigkeit dieser Urteile etwas nachgeht."
      ],
      [
        "Selbstverständlich verkennt man dann, wenn man das tut, doch nicht, daß überall Ausnahmezustände und Aus- nahmen vorhanden sind, und man kann zum Beispiel vieles, sehr vieles von dem unterschreiben, was in bezug auf den Kunstunterricht an den Akademien gesagt worden ist.",
        "Aber im ganzen und großen muß man schon sagen: Es ist doch nicht so außerordentlich viel Grund dazu vor- handen, gute Hoffnungen in die Zukunft zu senden, wenn man nicht bereit ist, nicht bloß im Äußeren, durch irgend- welche Verbände oder dergleichen, sich zusammenscharen zu wollen, um irgendeinem Unbestimmten entgegenzu- gehen, sondern wenn man bereit ist nur, wenn man bereit ist -, wirklich einzugehen auf eine gründliche Er- neuerung und Wiederbelebung unseres Geisteslebens selbst."
      ],
      [
        "Es greift schon das, was die eigentlichen Schäden sind, in unser Geistesleben selbst hinein.",
        "Und wer das ganze Gefüge des anthroposophischen Lebens kennt, wie es zum Beispiel geführt hat zu dieser Freien Hochschule für Geisteswis- senschaft: uns braucht man ganz gewiß nicht zu sagen, daß «jedem es frei stehen müsse, seine Weltanschauung zu vertreten und aus seiner freien Überzeugung heraus zu reden!» Die vielen böswilligen Naturen, die heute da sind, um alles mögliche Unzutreffende über die anthroposophi- sche Bewegung und was damit zusammenhängt, zu sagen, 9° die werden daraus gleich wieder Kapital schlagen und sagen: Diese Anthroposophen wollen, daß ihre Weltan- schauung überall vertreten ist."
      ],
      [
        "Nun, die Waldorfschule ist aus unserer Mitte heraus begründet worden, ohne daß damit in irgendeiner Weise eine Weltanschauungsschule gegründet worden ist.",
        "Gerade das Gegenteil einer Weltanschaungsschule sollte begründet werden."
      ],
      [
        "Das ist immer wieder und wieder betont worden.",
        "Und wer da glaubt, die Waldorfschule sei «eine anthropo- sophische Schule», der kennt sie eben ganz und gar nicht.",
        "Und ebensowenig kann irgendwie hier am Goetheanum gesagt werden, daß in alledem, was geschieht, irgend jemand beeinträchtigt werde in dem freien Bekenntnis seiner ureigensten Überzeugung."
      ],
      [
        "Aber dasjenige, wofür ich wenigstens immer kämpfen werde, das ist, bei aller Freiheit, bei aller Individualität und Intellektualität: wissenschaftliche Gewissenhaftigkeit, Gründlichkeit, Unterrrichtetsein von dem, über das man eben schreibt -, nicht ein bloßes Hinstellen der eigenen Meinung, weil man glaubt, es könnten unter Umständen auch irgendwelche Schäden entstehen aus demjenigen, das man sich in Wirklichkeit nicht bemüht zu verstehen, und aus dem man einige Sätze herausreißt, um einen Artikel zu schreiben.",
        "Ich sage das ganz ohne Leidenschaft."
      ],
      [
        "Sie wissen, ich be- nütze gewöhnlich die Dinge, die als «Besprechungen» sich über Anthroposophie hermachen, eigentlich nur als einen hier naheliegenden Anlaß, um allgemeine Zustände zu charakterisieren.",
        "Die persönlichen Angriffe interessieren mich im Grunde genommen gar nicht, nur insofern, als sie hinweisen auf das, was aus unseren Zuständen hinaus muß."
      ],
      [
        "Und da glaube ich doch, daß der Kommilitone aus Bonn in seiner herzhaften Weise einen richtigen Ton ge- troffen hat, einen richtigen Ton insofern, als die Studen- ten, die er gemeint hat, tatsächlich heute an den Universi- täten oder an den Hochschulen das nicht finden können, was sie suchen.",
        "Aber nicht «wegen des Lehrplanes», nicht «weil man nicht in der richtigen Weise auswählt», sondern weil die heutige Jugend ganz instinktiv - sie ist sich dessen nicht voll bewußt aus dem tiefsten Inneren heraus doch nach etwas verlangt, was innerhalb der allgemeinen Wissen- schaftlichkeit noch nicht da ist, was aber geschaffen wer- den muß innerhalb der allgemeinen Wissenschaftlichkeit."
      ],
      [
        "Das erwartet die Jugend.",
        "Diese Jugend wird ganz gewiß nicht ermangeln, mit vollen Händen zuzugreifen, wenn ihr wirklich geboten wird - was sie eigentlich will - ein wirklich neuer Geist.",
        "Denn einen solchen neuen Geist braucht die Gegenwart."
      ],
      [
        "Das ist im Grunde genommen auch der Grund der Ab- neigung gegen das, was von anthroposophischer Geistes- wissenschaft ausgeht, auch wenn man die Phrase im Munde führt, «man wolle jedem Neuen entgegenkom- men».",
        "Wenn es sich geltend macht, dann tut man es doch nicht."
      ],
      [
        "Weil man es im Grunde genommen auch gar nicht kann.",
        "Es würde nichts nützen, diese Dinge in irgendeiner Weise zu kaschieren, sondern es muß scharf, klipp und klar auf diese Dinge hingewiesen werden.",
        "Dann ist hier die Frage des Weltschulvereins gestellt worden."
      ],
      [
        "Was ich über diesen Weltschulverein zu sagen habe in bezug auf seine Absichten, habe ich, wie ich glaube, mit voller Deutlichkeit ausgesprochen am Ende unserer letzten Hochschulkurse im Herbst hier.",
        "Ich habe dann wiederum ungefähr in derselben Weise die Notwendigkeit der Begründung eines solchen allgemeinen Weltschulver- eins im Haag, in Amsterdam, in Utrecht, in Rotterdam 92 und in Hilversum ausgesprochen: daß die Möglichkeit, in einem Weltschulverein zu wirken, davon abhänge, daß sich die Überzeugung, daß ein neuer Geist in das allge- meine Schulwesen einziehen müsse, in einer möglichst gro- ßen Anzahl von Menschen verbreitet."
      ],
      [
        "Ich habe darauf hingewiesen, daß es heute gar nicht darauf ankommen könne, da oder dort Schulen zu begründen, die vereinzelt dastehen würden, und in denen man eine in dieser oder jener Hinsicht verbreitete Methode anwendet, sondern daß aus dem Gedanken des sich selbsttragenden, in sich befreiten Geistesleben heraus das Schulwesen der neueren Zivilisation in die Hand genommen werden müsse, das Schulwesen aller Kategorien, aller Stoffe.",
        "Soviel mir bekanntgeworden ist, sind die Worte und Aufforderungen, die ich bis jetzt gesprochen habe, das einzige, worüber ich im Grunde genommen zu berichten habe."
      ],
      [
        "Diese Worte waren darauf berechnet, in der zivili- sierten Bevölkerung der Gegenwart ein Echo zu finden.",
        "Ich habe von keinem solchen Echo zu berichten.",
        "Und ich glaube, ein richtiges Wort hat der Kommilitone aus Bonn gesprochen, indem er darauf hingewiesen hat, daß schließ- lich doch diejenige Studentenschaft, aus deren Herzen her- aus er hier geredet hat, in der Minderzahl ist."
      ],
      [
        "Ich glaube, sie ist sehr, sehr in der Minderzahl, insbesondere in Deutschland.",
        "Aber auch sonst - ich will niemandem Un- freundlichkeiten sagen , sonst, von wo wir gar nicht weit weg sind.",
        "Das zeigt der Besuch dieses Hochschulkurses."
      ],
      [
        "Er sagte: Der größte Teil der Studentenschaft schläft!",
        "Ja, er tobt zuweilen auch.",
        "Aber man kann auch tobend schlafen in bezug auf die Dinge, um die es sich da handelt.",
        "Und in bezug auf die Angelegenheiten, in bezug auf welche diese Forderung nach dem Weltschulverein erhoben worden ist, schläft alles auch in weitesten Kreisen einen 93 sanften Schlaf."
      ],
      [
        "Und es muß schon einmal gesagt werden: Man hat sich noch nicht recht daran gewöhnt, wie sehr es notwendig ist, anthroposophisches Wirken in die moderne Zivilisation hineinzutragen. - Man sollte sich daran ge- wöhnen, und ich sehne den Tag herbei, an dem ich Reich- licheres berichten kann auf die Frage hin nach dem Welt- schulverein.",
        "Heute könnte ich noch immer nicht viel mehr sagen, als was ich am Ende der Hochschulkurse hier im vorigen Herbst gesagt habe, obwohl das, was ich gesagt habe, darauf berechnet war, daß heute etwas ganz anderes darüber berichtet werden könnte."
      ],
      [
        "Aber so geht es auch mit anderen Dingen, und es ist sehr schwierig, gerade die Punkte, auf die es eigentlich ankommt in der heutigen Zeit, der heutigen Welt zum Be- wußtsein zu bringen.",
        "Ich habe in einem Berliner Vortrage, nachdem Lloyd George nach einem Streik in England, der schon ausge- brochen war, ein Zusammenleimen gemacht hat, darauf hingewiesen, daß man mit solchen Dingen nichts erreicht, daß das nur eine Vertagung ist."
      ],
      [
        "Die Leute haben es, wie es scheint, dazumal für eine Phrase genommen.",
        "Nun, bitte, überzeugen Sie sich heute, Sie könnten das schon seit eini- gen Tagen tun, ob das, was ich dazumal gesprochen habe, eine bloße Phrase war, oder ob es nicht vielleicht doch aus einer tieferen Erkenntnis der sozialen Zusammenhänge und der Notwendigkeit der sozialen Zusammenhänge her- vorgegangen ist."
      ],
      [
        "Das ist das Schwierige, daß man heute so wenige Men- schen mit jener Begeisterung findet, die ein wirkliches inneres Dabeisein bewirkt mit dem, was sie ja immerhin auch gern hören.",
        "Und deshalb freue ich mich immer, wenn sich Jugend findet, die etwas darüber zu sagen hat, wie sie das oder jenes, was sie sucht, da oder dort noch findet."
      ],
      [
        "Denn ich glaube, aus solchen Impulsen wird doch das her- vorgehen, was wir zu aller Einsicht, zu allem Verstehen brauchen: innerliches Dabeisein, innerliches Dabeisein, das weiß, wie stark die Metamorphose sein muß, die uns von den Niedergangskräften einer alten Zivilisation zu den Impulsen der neuen Zivilisation führt.",
        "Jawohl, wir brau- chen gewissenhaftes Verständnis, wir brauchen eine ein- dringliche Einsicht."
      ],
      [
        "Wir brauchen aber auch vor allen Din- gen das, was die Jugend aus ihren Naturanlagen heraus bringen könnte.",
        "Wir brauchen aber nicht nur in der Jugend, wir brauchen in den weitesten Kreisen der gegenwärtigen zivilisierten Menschheit nicht nur Einsicht, nicht nur ein- dringliches Verständnis der Wahrheit, wir brauchen Begei- sterung für die Wahrheit! 95"
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "ORGANISCHE NATURWISSENSCHAFTEN UND MEDIZIN Dritter Vortrag, Dornach, 6. April 1921",
    "paragraphs": [
      "Das Gebiet, auf das ich heute zu sprechen kommen werde, ist ein so ausgedehntes selbst wenn es nur von einem einzigen Gesichtspunkte aus beleuchtet werden soll -, daß dasjenige, was ich in der Lage sein werde heute zu geben, nur spärliche Andeutungen werden sein können, und ich bitte Sie, dies in Berücksichtigung zu ziehen. Es handelt sich ja darum, daß im Fortschreiten von den anorganischen Naturwissenschaften zu den organischen Naturwissen- schaften - und dann weiterhin zu psychologischer und geistiger Betrachtung - auf der einen Seite sich immer mehr und mehr die Notwendigkeit geisteswissenschaftlich- anthroposophischer Betrachtung ergibt, daß sich aber auch andererseits bei diesem Fortschreiten immer mehr und mehr zeigt, wie das, was hier Geisteswissenschaft genannt wird, befruchtend wirken kann auf die einzelnen Fach- wissenschaften.",
      "Bei dem, was gesagt werden konnte über das Wesen des Mathematischen, über das Wesen der anorganischen Na- turwissenschaften, da handelte es sich weniger darum, daß durch geisteswissenschaftliche Betrachtung irgendwie in einer ganz durchgreifenden Art eine andere Behandlungs- weise und namentlich ein anderer Inhalt herbeigeführt werde, als er in unserer gegenwärtigen Wissenschaftsgesin- nung schon vorhanden ist. Sie haben daher aus den bis- herigen Vorträgen über Mathematisches und über anorga- nische Naturwissenschaften einen gewissen Grundton ver- nehmen können, der dahin ging, anzudeuten, wie überall, 96 im Mathematischen sowohl wie im Anorganischen, die, wenn auch von den meisten unbemerkten, Anfänge zu derjenigen Behandlungsweise dieser Wissenschaften vorlie- gen, die von der hier gemeinten Geisteswissenschaft als die richtige anerkannt werden muß.",
      "Sie haben gesehen, wie man hindeuten muß auf den Übergang von der analyti- schen Behandlung der Geometrie zu der synthetischen Be- handlung, und wie man da findet, wie ein Weiterbeschrei- ten dieses Weges in imaginatives Betrachten hinführt, wenn man nur nicht beim Formalen stehenbleibt, sondern zu einem lebendigen Erfassen desjenigen, was da eigentlich vorliegt, übergeht. Und Sie haben dann gesehen, als eine mehr rein mathematische Betrachtung dargeboten wurde, wie aus einer gewissen lebendigeren Behandlung der Pro- bleme dasjenige hervorgehen soll, was man sich im Mathe- matischen und in den anorganischen Naturwissenschaften als das im anthroposophischen Sinne Richtige zu denken hat.",
      "Gewissermaßen sind wir untergetaucht in diese Wissen- schaften und haben in ihnen selber die Kraftpunkte ge- sucht, in deren Richtungen weitergegangen werden soll. Es handelt sich nur darum, daß man bei diesen Wissenschaf- ten streng innerhalb der gegenständlichen Betrachtungs- weise bleibt, welche die Eigentümlichkeit des gegenwärti- gen Menschheitsbewußtseins ist, und daß man nicht nötig hat, zu etwas anderem zu kommen als zu einem gewissen Wie in der Behandlungsweise dieser Betrachtung.",
      "In derselben Lage ist man nicht bei den organischen Naturwissenschaften, obwohl etwas wiederum in anderer Beziehung Ähnliches auch hier vorliegt. Wenn man heute von Mathematik, von anorganischen Naturwissenschaften, von Phoronomie, Mechanik und so weiter spricht, dann hat man auf die Denkweise hinzuweisen, an der man etwas zu reformieren hat, wie das gestern geschehen ist. 97 Bei den organischen Naturwissenschaften beginnt aber, daß man hinzuweisen hat nicht auf das Abzuweisende, sondern auf das Aufzunehmende.",
      "Das beginnt schon in- nerhalb der Tatsachenwelt selber. Da kann durch eine bloße Reform der Denkweise eigentlich nichts Ausgiebiges erreicht werden. Ich möchte zunächst eine kurze historische Betrachtung erläuternd voranschicken, durch die klargemacht werden soll, in welcher Weise auf diesem Gebiete vorzuschreiten ist, um zu einer fruchtbaren Anschauung zu kommen.",
      "Wir haben an anderen Stellen in unserer Betrachtung darauf hingewiesen, daß im fortlaufenden Entwickelungsgange der Menschheit eigentlich erst seit dem 15. Jahrhundert der nachchristlichen Zeit herauf getaucht ist, was wir die beson- dere Art unseres heutigen Bewußtseins nennen.",
      "Alle frü- here Betrachtungsweise war im Grunde genommen eine ganz andere. Es ergriff die Menschheit erst von dem ge- nannten Zeitpunkte an jene Bewußtseinsform recht, die auf der einen Seite zum Gebrauche der Freiheit führt, aber auf der anderen Seite den Menschen, dadurch daß sie ihn auf sich selbst zurückweist, in eine Abstraktion hin- einwirft, durch die er gegenüber der Seinswelt in einer gewissen Weise wirklichkeitsfremd wird.",
      "Es ist die Be- trachtungsweise, die sich nur an äußere Beobachtungen und deren Beschreibung hält, an Anordnung von Versuchen, von Experimenten und Beobachtung ihrer Ergebnisse, das heißt der Antworten, die die Natur erteilt, wenn ihr nicht bloß theoretisch, sondern praktisch, im Experiment, Fra- gen gestellt werden. Was von Seelenkräften angewendet wird, indem auf diese Art die Wissenschaft zustande kommt, das ist die kombinierende Verstandeskraft.",
      "Diese kombinierende Ver- standeskraft ist zunächst, ich möchte sagen, das große 98 praktisch-wissenschaftliche Problem. Sie wird dieses, wenn man die Frage aufwirft nach ihrer richtigen Anwendbar- keit.",
      "Und diese Frage nach der richtigen Anwendbarkeit der Verstandes- oder auch der gewöhnlichen Vernunft- kraft - im Beobachten, im Zusammenfassen der Beobach- tungen, im Experimentieren -, diese Frage ist besonders für Goethe aufgetaucht. Und wer sich - Sie können das nachlesen in meinen jetzt schon fast vierzig Jahre alten «Einleitungen zu Goethes Naturwissenschaftlichen Schrif- ten» - in das vertieft, was da eigentlich bei Goethe zum Problem geworden ist, der wird finden, daß Goethe die Verstandes- oder Vernunftkraft nicht so angewendet wis- sen wollte, daß sie der Wissenschaft einen eigentlichen In- halt gibt, daß man gewissermaßen aus der Verstandes- oder Vernunftkraft heraus etwas über das Sein als solches aussagt, sondern so, daß diese Verstandes- oder Vernunft- kraft nur dazu verwendet wird, die Phänomene so ange- ordnet zu denken, daß das eine Phänomen das andere erklärt.",
      "Dann hat man also, indem man sich seines Ver- standes oder seiner Vernunft bedient, nichts hinzugetragen zu dem, was die Phänomene selber aussprechen. Es handelt sich darum, wenn man rein den Verstand anwenden will, daß man dann auch rückhaltlos vorschrei- tet zu einer reinen Phänomenologie, das heißt, den Ver- stand nur dazu benützt, ein Phänomen reinlich anzu- schauen, nichts anderes zu tun, als es eben zu reinlichem Anschauen zu bringen, und dann das andere dazugehörige Phänomen danebenzustellen; so daß durch diese Anord- nung der Phänomene - was dann im Experiment auch zur praktischen Ausführung kommt - die Phänomene selbst veranlaßt werden, daß sie sich gegenseitig erklären.",
      "Der Verstand hat also bloß eine ordnende, eine gewissermaßen real methodologische Bedeutung, keine qualitative Bedeu- 99 tung. Aus ihm darf im Goetheschen Sinne nichts hervor- gehen, was irgendwie über das Sein selbst etwas aussagt.",
      "Das ist, wie ich glaube, scharf präzisiert, was Goethe als den Gebrauch der Verstandeskraft ansah, und das ist auch dasjenige, dem das allgemeine Bewußtsein der Mensch- heit seit dem ersten Drittel des 15. Jahrhunderts zustrebt.",
      "Man kann sagen, es haben noch nicht alle gelernt, dann, wenn es sich um den Verstand handelt, in einer gewissen Weise zu resignieren, wie das Goethe in seinen eigenen Forschungen tun wollte, wenn es auch bei ihm nicht über- all voll zur Ausführung gekommen ist. Aber unbewußt lebt in dem Wissenschaftsstreben, aus dem gerade Geistes- wissenschaft heraus will aber auf andere Art als durch den Verstand , diese Art des Verstandeslebens doch wie ein unbewußtes Ideal.",
      "Und es ist das, was ich jetzt sage, mit Händen zu grei- fen, wenn man jene Fortgänge sieht, die im naturwissen- schaftlichen Denken vorliegen, sagen wir, von dem An- fang des 19. Jahrhunderts - und ich meine jetzt nicht bei den Naturphilosophen, sondern bei den empirischen Na- turforschern etwa von der Art des Johannes Müller bis etwa zu Mach oder gar zu Poincare und den anderen, oder zu Fritz Mauthner, der allerdings kein Naturfor- scher ist.",
      "Wer so recht eine Anschauung gewinnen will, was da vorliegt, der muß sich bekanntmachen mit etwas, was in der ersten Hälfte des 19. Jahrhunderts noch eine gewisse Rolle gespielt hat, was aber dann gegen die Mitte des 19.",
      "Jahrhunderts vollständig fallengelassen worden ist, und was jetzt in einer merkwürdigen Gestalt da oder dort wiederum in der wissenschaftlichen Betrachtung auftaucht. Das ist die Idee der Lebenskraft, das, was man im wissen- schaftlichen Leben den Vitalismus nennt. 100 Wenn wir zu der Vorstellung von Vitalkraft zurück- gehen, die man in älteren Zeiten hatte, so sieht man, daß die Anhänger des Vorhandenseins dieser Vitalkraft sich sagten: Wenn wir ein Ding der anorganischen Natur be- trachten, so finden wir in diesem Ding der anorganischen Natur allerlei Kräfte, Wärmekraft, Lichtkraft, elektrische Kraft und so weiter; wenn wir aber ein Wesen der organi- schen Welt betrachten, so finden wir außerhalb diesen Kräften, welche die anorganische Natur konstituieren, auch noch die Vitalkraft, die Lebenskraft.",
      "Diese Lebens- kraft ist in jedem Lebewesen vorhanden wie im Magneten die Magnetkraft. Sie bemächtigt sich gewissermaßen der anorganischen Kräfte, um diese zusammenzufassen und aus ihnen Wirkungen hervorzubringen, die sie, auf sich selbst gestellt, nicht leisten können.",
      "Dieser Vitalkraft wurde der letzte Stoß zum Abdanken gegeben durch die Darstellung eines organischen Stoffes in synthetischer Weise von Wöhler und Liebig, und sie wurde als solche in der zweiten Hälfte des 19. Jahrhun- derts fallengelassen.",
      "Aber im sogenannten Neovitalismus taucht sie wiederum in der neuesten Zeit aus der Verbor- genheit auf, weil gewisse Denker dazugekommen sind, sich zu sagen: Wenn wir die Methoden, die wir ausgebil- det haben, um mit Hilfe der anorganischen Kräfte das Anorganische zu erklären, auf das Organische anwenden, dann kommen wir eben nicht aus; wir müssen im Organi- schen etwas anderes suchen. Und, ich möchte sagen, mit einem deutlichen Anklang an die alte Lebenskraft taucht im Neovitalismus wiederum so etwas herauf für die Er- klärung in den organischen Wissenschaften.",
      "Wer sich aber wirklich ordentlich kritisch einläßt auf dasjenige, was als Lebenskraft selbst noch in der Betrach- tung von Johannes Müller vorkommt, der wird finden, 101 daß in dieser Lebenskraft etwas vorliegt, was sich als Be- griff in Wirklichkeit nicht vollziehen läßt. Und ich möchte sagen, an der Unmöglichkeit, die Lebenskraft als Begriff zu fassen, ist sie im Laufe des 19.",
      "Jahrhunderts in der wis- senschaftlichen Betrachtung abgestorben. Man konnte sie nicht fassen. Und warum konnte man sie nicht fassen? Zunächst wird man, wenn man ganz vorsichtig vorgeht in der Betrachtung der organisch-naturwissenschaftlichen Me- thodik des 19.",
      "Jahrhunderts, sehen, wie diejenigen, die da mit der Idee dieser Lebenskraft ringen, finden, sie können damit nichts anfangen. Was sie anfangen wollen, ent- schwindet ihnen sogleich, wenn sie mit ihrer Idee an die Erscheinung herangehen.",
      "Sie kommen doch nicht auf den eigentlichen Nerv der Sache. Sie kommen nicht darauf aus dem Grunde, weil sie die eigentliche Funktion der Ver- standestätigkeit nicht scharf fassen. Die Verstandestätigkeit tendiert in unserem Zeitalter dahin, nur das Phänomen zu betrachten und es hinzustel- len neben ein anderes, damit Phänomen das Phänomen erklärt.",
      "Aber das läßt sich bei der Lebenskraft nicht aus- führen. Bei der Lebenskraft muß man immer, wenn man überhaupt etwas tun will, von der Verstandestätigkeit aus etwas hineinschieben in das Phänomen. Man muß gewis- sermaßen dem Phänomen etwas unterschieben.",
      "Und dar- innen liegt das, was allmählich im Gebrauche der Idee von der Lebenskraft bedenklich geworden ist. Das war dann die Ursache, daß man sie ganz hat fallen lassen und daß als ein gewisses Ideal in weitesten Kreisen entstanden ist, die Lebewesen nun überhaupt als einen Zusammenfluß, eine Kombination derjenigen Kräfte anzuschauen, die auch in der anorganischen Natur walten.",
      "Mit anderen Worten: die Idee der Lebenskraft ist eigentlich eine Art Wechselbalg geworden. Man ist dazu IO2 gekommen, das Konstitutive in den Wissenschaften nur im Phänomen zu suchen. Die Lebenskraft ergab sich als Phänomen nicht.",
      "Man mußte - was aber eigentlich nicht statthaft war in diesem Zeitalter der Menschheitsentwicke- lung - vom Verstande aus die Vitalkraft konstruieren. Das war der negative Teil der Entwickelung, in der wir heute drinnenstehen.",
      "Denn in dem Neovitalismus tritt nichts Anschauliches auf. Was der Neovitalismus an die Stelle einer bloß das Anorganische kombinierenden Erklä- rung der Lebenserscheinungen setzt, das ist nichts anderes als eine Art Aufwärmung des alten Vitalismus.",
      "Und man könnte sagen, daß deutlich im äußeren Betriebe des wis- senschaftlichen Lebens eine Art Abbild dessen vorhanden ist, was da eigentlich vorgeht im inneren Geistesleben. Ich kann heute nur in einzelnen Erscheinungen hinweisen auf dieses Abbild.",
      "Aber wer die beieinanderliegenden Phäno- mene gerade so betrachten kann, daß sie sich gegenseitig aufhellen, der wird schon die Bewahrheitung desjenigen, das ich jetzt meine, auch einsehen. Was sich aus einer älteren Betrachtungsweise erhalten, was die Begriffe und Ideen daraus zurückgehalten hat, das figurierte bis vor kurzer Zeit, bis in die Mitte des 19.",
      "Jahrhunderts, noch recht unansehnlich als Philosophie. Und ich habe das- jenige, was mit dieser Philosophie vorging, in meinem ersten Vortrage dieser Reihe, wenigstens andeutungsweise auseinanderzusetzen versucht.",
      "Allein in der zweiten Hälf- te des 19. Jahrhunderts, da gingen schon einzelne merk- würdige Erscheinungen auf dem Gebiete des philosophi- schen Lebens vor. Wir können sehen, wie ein recht gewissenhafter Denker, der nur nicht in der Lage war, die Probleme, die er auf- warf, zu Ende zu denken ich habe ihn an dieser Stelle in diesen Tagen erwähnt , wie Franz Brentano für die 103 Philosophie die naturwissenschaftliche Methode fordert.",
      "Ihm war nichts anderes gegeben als naturwissenschaft- liche Methode als dasjenige, was eben in der Gegenwart als solche üblich ist. Gewissermaßen war damit das Leit- motiv für alle diejenigen gegeben, die nicht mehr auf eine besondere geistige Methode reflektieren wollten, sondern die sich der allgemeinen Autorität des landläufigen natur- wissenschaftlichen Denkens fügten.",
      "Dann aber kamen noch andere Erscheinungen. An einzelnen Fakultäten, wo, sagen wir, alte Herbartianer wirkten, kam es dazu, daß diese ihre Lehrkanzeln verließen, und es gab dann Fakul- täten, welche an diese unbesetzten Lehrkanzeln für Philo- sophie nunmehr nicht Philosophen im alten Sinne beriefen, sondern naturwissenschaftlich Denkende.",
      "So zum Beispiel war es in Wien, wo Mach, der Naturforscher, die Lehr- kanzel für Philosophie, die leer geworden war, zu bezie- hen hatte. Man empfand das noch etwas unbehaglich, und man nannte deshalb das Fach, das er zu vertreten hatte, «induktive Philosophie», hatte ihm also die Lehrkanzel für Induktive Philosophie übertragen, danebengesetzt allerdings einen Mann ich schätze diesen Mann sehr, aber ich charakterisiere jetzt ja objektiv Kulturerscheinun- gen, und damit spielt die persönliche Schätzung keine Rolle -, der vorher Professor für christliche Philosophie an der theologischen Fakultät der neuen Universität war.",
      "Damit dokumentierte man, daß man dasjenige, was in der Philosophie sein sollte, nicht aus irgendeiner neuen Forschungsweise herausnahm, sondern aus der alten Tra- dition. Und was sich da, ich möchte sagen, in einer ge- wissen auffälligen Weise vollzog, das vollzieht sich ja im- mer wieder.",
      "Abgesehen davon, daß ganz naturwissen- schaftlich Denkende an die psychologischen Lehrkanzeln herangebracht werden und in ein früher als philosophisch 104 angesehenes Gebiet ganz naturwissenschaftliche Denk- weise hineintragen, sehen wir auch sonst, wie naturwissen- schaftlich Denkende heute ganz offiziell als Träger der Philosophie funktionieren. In solchen Erscheinungen spricht sich dasjenige auch äußerlich aus, was ich hier an- zudeuten habe: mit dem, was da in der neueren Zeit her- aufgekommen ist als der kombinierende Verstand, der in seiner Reinheit nur so angewendet werden kann, wie ihn Goethe angewendet wissen wollte, mit dem läßt sich über die Lebenserscheinungen nichts ausmachen.",
      "Hier liegt wiederum der Punkt, wo Ehrlichkeit und Unbefangenheit des wissenschaftlichen Denkens streng ge- fordert werden muß. Und die Methoden, die mit Hilfe äußerer Beobachtung, äußeren Experimentes, mit Hilfe dieses kombinierenden Verstandes forschen, die können, wenn sie mit sich selber richtig kritisch zu Werke gehen, wenn sie sich aus ihren Betrachtungen heraus, wenn ich so sagen darf, ein volles Bewußtsein über ihre eigene Trag- weite verschaffen, nicht anders, als sagen: Wir sind als Methoden nur anwendbar auf das Gebiet der anorgani- schen Naturwissenschaften, da gehören wir hinein, da kön- nen wir die Betrachtungsweise groß machen; aber wir dür- fen nicht, ohne den ganzen Sinn der Betrachtungsweise, auch den Inhalt der Betrachtungsweise zu ändern, in das Gebiet der organischen Naturwissenschaften heraufsteigen.",
      "Das muß von dieser Methode unberührt bleiben. Geisteswissenschaft hat nun von der anderen Seite aus zu sprechen. Geisteswissenschaft hat zu sagen: Es gibt auch die Möglichkeit einer Bewußtseinsentwickelung, ent- sprechend dem Lauf, der von jenen Bewußtseinsformen aus genommen worden ist, die vor dem 14.",
      "Jahrhundert noch ihre letzten Blüten getrieben haben. Wie von diesen Bewußtseinsformen aus zum rein gegenständlichen Be- 105 wußtsein, das nicht in der Phänomenalität steckenbleiben soll, fortgeschritten worden ist, so muß heute, behufs wissenschaftlicher Betrachtungsweise des Organischen, durch die innerliche Entwickelung der Seele heraufge- schritten werden zu den anderen Bewußtseinsformen: zum imaginativen Bewußtsein, inspirierten Bewußtsein, intuitiven Bewußtsein.",
      "Denn soll der Verstand zurechtkommen mit den Le- benserscheinungen, dann muß für den Verstand das, was sich innerhalb des Gebietes der Lebenserscheinungen ab- spielt, Beobachtung werden, Phänomen werden. Das kann es nicht innerhalb der sinnlichen Beobachtung.",
      "Der Verstand kann nicht konstitutiv werden für einen Inhalt der organischen Naturwissenschaften. Der Verstand muß sich auch da kombinierend verhalten. Aber die An- schauung muß ihm geliefert werden. Diese Anschauung wird ihm geliefert im imaginativen Erkennen.",
      "In der Ausbildung des imaginativen Erkennens, wie ich sie dar- gestellt habe in meinem Buche «Wie erlangt man Er- kenntnisse der höheren Welten?», wird nämlich, abgesehen von allem übrigen, was über dasselbe gesagt werden kann, die Möglichkeit errungen, mit dem alten Vitalismus, der einen Wechselbalg von Begrifflichkeit geliefert hat, zu brechen und die imaginative Anschauung des Lebens an dessen Stelle zu setzen. Selbstverständlich kommt jetzt der ungeheuer billige Einwand, der nun gemacht werden kann.",
      "Es kann gesagt werden: Nun ja, aber wir normalen Menschen haben eben nur diesen kombinierenden Verstand. Es mag solche Käuze geben, welche zur Imagination, Inspiration und so weiter fortschreiten. Wir wollen das nicht weiter bezwei- feln, aber wir haben sie eben nicht.",
      "Deshalb gilt für uns eine Philosophie, welche diese Inhalte der Imagination 106 und so weiter ablehnt, welche sich nicht damit zu schaffen macht, diese Inhalte der Imagination, Inspiration und so weiter in sich selber als Philosophie hereinzunehmen. Dieser billige Einwand ist in der folgenden Weise zu entwerten.",
      "Ich will mich mit einem Beispiel verdeutlichen, das ich öfter schon erwähnt habe. Wenn die Geistesfor- schung einfach die Tatsachen nimmt, die heute schon der empirischen organischen Wissenschaft vorliegen, dann kommt man zum Beispiel in der Lehre vom menschlichen Herzen zu ganz anderen Anschauungen als denen, die durch einen falschen, aus alten Zeiten traditionell fortbe- wahrten alten Verstandesgebrauch noch immer in der land- läufigen Wissenschaft zustande kommen.",
      "Da wird das Herz angesehen wie so eine bessere Pumpe, welche das Blut durch den Organismus treibt. Diese Anschauung folgt nur dann als eine «richtige» für den Menschen, wenn er auf den menschlichen Organismus als ein Lebewesen den Verstand anwendet, der darauf nicht anwendbar ist.",
      "So- bald man zur imaginativen Betrachtung aufsteigt, kommt man dazu, sich zu sagen: Nicht das Herz treibt das Blut durch die Adern des Organismus, sondern die Herzbewe- gung ist das Ergebnis des inneren Blutlebens. Das Blut selbst ist es, welches aus dem intensiven eigenen Leben, welches zentralisiert ist im Herzen, diese Bewegung verur- sacht, so daß die Herzbewegung die Folge der Blutbewe- gung, und nicht das Umgekehrte der Fall ist.",
      "Das ergibt sich unmittelbar aus der imaginativen Betrachtung des menschlichen und dann auch des tierischen Organismus. Nun, wer ohne diese imaginative Betrachtung eine Herzlehre, eine Herzbewegungslehre aufstellt, der muß, wenn er ehrlich ist, dazu kommen, in dieser Betrachtungs- weise Unzulängliches zu finden, an dem stehenzubleiben ist.",
      "Und wenn er dann ausschaltet, was er selbst in seiner 107 Erklärung als unzulänglich erkannt hat, aber beibehält die empirische Erkenntnis der Tatsachen, der gesamten Tatsachenwelt des menschlichen und tierischen Organis- mus, insofern sich diese Tatsachenwelt auf Blutbewegung und Herzbewegung bezieht, wenn er alles zusammen- faßt - Geisteswissenschaft schreckt nie vor einer wirk- lich gründlichen und gewissenhaften Prüfung durch andere zurück , was aus dem Umfang der gegenwärtigen Ana- tomie, Physiologie, Biologie und so weiter zu gewinnen ist, namentlich auch, was, erläuternd dieses Problem, aus der Embryologie zu gewinnen ist, dann wird er sich sagen: Nun, derjenige, der auf dem Boden imaginativer Erkennt- nis steht, gibt diese Erklärung. Ich kenne die Tatsachen; setze ich das Ergebnis der imaginativen Erkenntnis ehr- lich voraus, prüfe ich daran meine Tatsachen, die ich gut kenne, dann stimmt das völlig, und es ist damit aller nur wünschenswerte Grund vorhanden, um dasjenige, was durch imaginative Erkenntnis gewonnen wird, anzuneh- men.",
      "Es kann, sobald gewissenhaft und ehrlich auf diesem Gebiete in der Richtung der wissenschaftlichen Bewußt- seinsentwickelung fortgeschritten wird, nicht mehr die Ausrede gelten, wer nicht selber imaginative Erkenntnis habe, der brauche diese imaginative Erkenntnis nicht an- zuerkennen. Sondern es muß an dessen Stelle das andere treten, daß man sagt: Ich kenne gut die Tatsachen, die sich der sinnlichen Beobachtung darbieten, eine Erklärung aber kommt mir nur von seiten des imaginativen An- schauens.",
      "Mit dieser Erklärung finde ich mich zurecht. Die Tatsachen sind verständlich aus ihr heraus; also sind alle Voraussetzungen für die Annahme gegeben. - Und im Grunde genommen zeigt derjenige, der aus dem eben charakterisierten Grunde die übersinnliche Erkenntnis auf 108 diesem Gebiete ablehnt, nicht, daß er die übersinnliche Erkenntnis nicht beherrscht.",
      "Die ist ja heute noch nicht so weit, daß man sie leicht beherrschen könnte. Sondern er beweist, daß er die ihm vorliegenden Tatsachen nicht rich- tig werten kann. Er beweist den Mangel seiner Einsicht in die sinnlich-empirisch gewonnene Tatsachenwelt selber.",
      "Und das ist am häufigsten der Fall in der heutigen Be- trachtungsweise der organischen Naturwissenschaften. Die Betrachtungsweise, die für die organischen Naturwissen- schaften nötig ist, ist diejenige, welche sich von dem blo- ßen gegenständlichen Erkennen zu dem imaginativen Er- kennen erhebt.",
      "Denn im imaginativen Erkennen enthüllt sich erst das Geheimnis des Lebens. Goethe hat von der reinen Phänomenologie aus, die er angewendet wissen wollte zum Beispiel in der Farben- lehre und in der Tonlehre, hingestrebt zu dem, was er seine Morphologie nannte, zu der Erfassung des Sich- Gestaltenden.",
      "Er ist nur bis zu einem gewissen Grade der Erkenntnis gekommen. Was er inauguriert hat, das muß fortgesetzt werden. Man sieht, wie er nur bis zu einem gewissen Grade gekommen ist: nachdem seine Betrach- tungsweise bis zu einem hohen Grade, wenn auch nicht ganz, für das unbewußte Pflanzenreich ausgereicht hatte, mußte er, als er von dem Pflanzenreich zu der Betrach- tung der Metamorphose des tierischen Reiches gehen wollte, stehenbleiben.",
      "Sehen Sie sich die Abhandlungen an, die er in bezug auf die Metamorphose des tierischen Reiches geschrieben hat. Sie werden überall sehen, wie er als ein gewissenhafter Mensch abbricht, weil es eben nicht mehr weitergeht, weil man von einem gewissen Momente von dieser Morphologie Goethes, wenn man weiter kommen will, zu etwas noch Geistigerem hinkommen muß, als die bloße Gestalt ist: zu dem, was innerlich die Bewußtheit 109 mit der Empfindungs- und Willenswelt nun im in- spirierten Erkennen erfassen kann.",
      "Wenn man die Sache so ansieht, dann wird man haupt- sächlich in der Betrachtungsweise, in dem Wie des An- schauens, in dem Wie der Ausbildung der Methodik ein Wesentliches sehen. Und - wie gesagt, ich kann heute nur andeuten - wenn wir von diesem Gesichtspunkte aus einen Blick werfen auf das, was im Verlaufe des 19.",
      "Jahr- hunderts und im Beginne des 20. Jahrhunderts Evolutions- lehre geworden ist, dann werden wir das Folgende finden: Zunächst wird äußerlich empirisch die Reihe der Lebe- wesen verfolgt, von der unvollkommenen, sogenannten unvollkommenen Monere bis herauf zum Menschen, und es wird in der Betrachtungsweise so verfahren, daß man sich immer das Vollkommenere aus dem Unvollkomme- neren hervorgehend denkt.",
      "Wenn man in einer etwas an- deren Weise vorgeht, wie das bis zu einem gewissen Grade Haeckel getan hat, so konstruiert man wenigstens in der Vorfahrenreihe der jetzigen Wesen solche, welche wie- derum ziemlich genaue Abklatsche der jetzigen Lebewesen sind. Die konstruierten Wesen der Vorzeit in dem alten Haeckelschen Stammbaum haben durchaus den Charakter desjenigen, was auch heute lebt.",
      "Dasjenige aber, was sich der Imagination darbietet, führt zu einer ganz anderen Betrachtungsweise. Und ich will - weil es die Kürze der Zeit fordert, nur schema- tisch - diese Betrachtungsweise andeuten: Wenn man vom Standpunkte der imaginativen Anschauungsart ausgeht, kann zum Beispiel das menschliche Haupt in Vergleichung mit der Rückenwirbelsäule sachgemäß nur so betrachtet werden, daß man sagt: Diese menschliche Hauptgestal- tung, so unähnlich sie auch in der äußeren Form, in ihrer heutigen Metamorphose der Rückenwirbelsäule ist, kann HO nur metamorphosisch vorgestellt werden als eine Umbil- dung der Rückenwirbelsäule.",
      "Man hat sich zu denken, daß die Nervenorganisation des Rückenmarks sich umgestaltet, metamorphosiert zu dem, was uns als das Gehirn er- scheint, und daß sich auch die umschließenden Knochen, die Wirbelknochen der Rückenmarkswirbelsäule, umge- stalten zu dem, was die Schädeldecke wird. Aber nun ist es wichtig, das Folgende ins Auge zu fassen.",
      "Man muß sich vorstellen, daß in einer gewissen Beziehung dasje- nige, was ich hier im Gegensatz zu der Linie a-b wie einen Kreis hingezeichnet habe, gewisserma- ßen eine aufgeplusterte Rücken- wirbelsäule ist und hinweist auf dasjenige, was es einmal in einer früheren Metamorphose war: selbst etwas wie eine Rücken- wirbelsäule, aber unter anderen äußeren Bedingungen. Was ich als einen Kreis gezeichnet habe, hat sich also in gewisser Weise aus a-b herausgebildet.",
      "Was aber heute als Rückenwirbelsäule am menschlichen Organismus ist, das hat sich dem also Ausgebildeten erst später angegliedert. Das ist beim Menschen die spätere Bildung. Nachdem sich der Schä- del umgebildet hatte aus einer Kräfteanordnung, die heute in etwas anderer Weise in der Rückenwirbelsäule erscheint, gliederte sich an ihn diese heutige Rückenwirbelsäule an.",
      "Was das «Unvollkommenere» am Menschen ist, ist also 111 das Spätere, und was das «Vollkommenere» ist, ist das Frühere. Und wir werden zurückgeführt, wenn wir sinn- gemäß vorgehen, in ein Zeitalter, in dem in anderer Meta- morphose die Kräfte, welche das menschliche Haupt bil- den, schon vorhanden waren, nicht aber die Kräfte, welche die heutige menschliche Rückenmarksäule bilden.",
      "Wenn wir aber diese letzteren Kräfte ins Auge fassen, dann sind es dieselben Kräfte, die uns zum Beispiel im Tierreiche entgegentreten, wo die Schädelbildung eine Ge- staltung ist, die nur eine geringere Umwandlung gegen- über der Rückenwirbelsäule aufweist als beim Menschen. So daß wir sagen müssen: Was im menschlichen Haupte vorliegt, weist uns als früheste Bildung in ältere Zeiten zurück als das, was dann als Mensch schon mit der Rük- kenwirbelsäule aufgetreten ist, und auch als das, was im Tierreiche vorliegt.",
      "Wir haben in der Evolution nicht den Menschen abzuleiten aus dem Tierreiche, sondern wir ha- ben uns zu sagen, eine sinngemäße Ausdeutung der Tat- sachen selber zeigt uns, daß der Mensch ein älteres Wesen ist als die Tiere, daß die Tiere später entstanden sind und es in ihrer Evolution nur zu dem gebracht haben, was beim Menschen heute auch in seiner späteren Gestaltung als Rückenwirbelsäule zutage tritt, es aber, weil ihnen eine kürzere Zeit zur Verfügung stand, nicht dahin ge- bracht haben, die Schädelmetamorphose in dem mensch- lichen Sinne auszubilden. Wenn Sie diesen Gedanken, den ich hier nur skizzen- haft vorbringen kann, ausdenken, dann kommen Sie zu einer wirklich sinngemäßen Auffassung der Evolutions- lehre.",
      "Die großartigen Tatsachen, die vorliegen, die man nur in ihrem ganzen Umfange kennen muß, werden er- klärlich, wenn man diese aus imaginativem Erkennen ge- schöpfte Anschauungsweise zugrunde legt. Und aus die- 112 sen Voraussetzungen heraus kommt man dann zu ganz gewissen Bezügen, Verhältnissen desjenigen, was in der äußeren Wissenschaft unseren Erdenverhältnissen vorliegt.",
      "Denken Sie, daß man durch Weiterverfolgen dieses Ge- dankens dazu kommt, sich zu sagen, wie der Mensch zu dem Tiere steht. Man kann auf diese Weise aber auch weiterschreiten und erkennen lernen, wie der Mensch steht zu dem Pflanzenreich und zuletzt zu dem mineralischen Reich, das man durch Beobachtung, Experiment und den kombinierenden Verstand in seinem Phänomenzusammen- hang erfaßt.",
      "Mit einer solchen Vorstellungsweise kommt man dazu, des Menschen Verhältnis zu seiner Umwelt wirklich zu durchschauen, wie man in einer gewissen Weise die Bezie- hungen der Gebiete, die uns in der mathematischen Wis- senschaft zu mathematischen Urteilen führen, durchschaut. Man kommt dazu, immer mehr und mehr auszubilden, was Goethe wie ein Ideal vorschwebte, indem er sagte, seine Urpflanze müsse in der Idee etwas werden, mit dem man erkennend jede einzelne Pflanze in ihrem entspre- chenden Charakter vor die Seele hinstellen kann.",
      "Ge- radeso wie man, wenn man den allgemeinen Begriff des Dreieckes hat, auch weiß, was bei irgendeinem besonderen Dreieck auftritt. Diese Metamorphosierung der mensch- lichen Erkenntnis für das organische Erkennen, das ist es, was Goethe als ein Ideal vorschwebte.",
      "Aber nun möchte ich mich wiederum durch ein Beispiel veranschaulichen. Wenn wir von diesem Gesichtspunkte ausgehen, kommen wir dazu, wirklich genauer ins Auge zu fassen, was sich zum Beispiel im menschlichen Haupte als Funktionen abspielt.",
      "Wir lernen erkennen, wie die Funk- tionen des menschlichen Hauptes, indem sie in der Art, wie ich es hier dargestellt habe, der Evolution unterliegen, heute bereits wiederum in Rückbildung begriffen sind, wie sie von anderen Zuständen ausgegangen sind, zum menschlichen Haupte geworden sind, wie aber heute durch die äußeren Einflüsse ein Mineralisierungsprozeß stattfindet im menschlichen Haupte. Und dieser Minerali- sierungsprozeß ist die Parallelerscheinung zu unserem ver- standesmäßigen Erkennen, das auch nur das mineralisch Physische aufzufassen weiß, weil es gebunden ist an einen Mineralisierungsprozeß im menschlichen Nerven-Sinnes- apparat.",
      "Man lernt gerade kennen, wie dem, was man im verstandesmäßigen Erkennen vollbringt, als sein phy- sischer Träger ein ins Organische des Menschlichen hinein sich bauender Mineralisierungsprozeß parallel geht, ein Absetzen von rein Mineralischem innerhalb des Organi- schen. Indem man dieses Mineralische im Organischen ab- setzt, kommt man dazu, für das Seelische dasjenige aus- zuführen, was verstandesmäßige Tätigkeit dieses mensch- lichen Wesens ist.",
      "Man kommt dazu, innerlich den Zusam- menhang zwischen dem Geistig-Seelischen und dem Phy- sisch-Leiblichen wirklich aufzufassen, nicht bloß abstrakt davon herumzureden, wie es die «psychophysischen Par- allelitiker» und ähnliche Phraseure auf dem Gebiete der Psychologie tun. Das ist die Art, wie aus dem gegenwärtigen Bestände der organischen Naturwissenschaft auf den Weg hinge- wiesen werden kann, den sie nehmen muß.",
      "Da kann man nicht dabei stehenbleiben, eine bestimmte Denkweise zu fordern; da kann man nur das, was in den empirischen Tatsachen selber weitertreibt, suchen, da muß man an die Stelle der bestehenden Denkweise eine andere, nämlich die des imaginativen Erkennens wirklich treten lassen. Dann kommt man aber auch zu einer wirklich fruchtba- ren Anwendung dieser Erkenntnis.",
      "Sucht man in der Au- 114 ßenwelt irgend etwas, das nun, versetzt in die Außenwelt, dem entspricht, was im menschlichen Haupte als Minerali- sierungsprozeß parallel dem Verstandeserkennen vor sich geht, dann findet man draußen in der Natur das, was sich abspielt zwischen den Kräften in der Erde und dem, was in der Wurzel der Pflanze vor sich geht, und man findet den innerlichen Bezug zwischen dem, was konstituierend ist in der Wurzelbildung der Pflanze, mit dem, was kon- stituierend ist für das, was im menschlichen Haupte vor sich geht. In einer ähnlichen Weise wird man dann Beziehungen finden zwischen dem, was zum Beispiel im Krautartigen, Blattartigen der Pflanze vor sich geht, und dem, was im rhythmischen System des Menschen, drinnen in seinem Organischen, vor sich geht.",
      "Und man findet die Beziehun- gen zwischen den Funktionen im Blütenhaften und im Fruchtenden mit dem, was im menschlichen Stoffwechsel- system, im Sexualsystem und so weiter vor sich geht. Man kann von diesem Gesichtspunkte aus eine Überschau ge- winnen über das Pflanzenleben.",
      "Wenn man weiß, wie im menschlichen Organismus das, was ich den Mineralisierungsprozeß genannt habe, so wirkt, daß sich dieser Mineralisierungsprozeß innerlich vollzieht, im Gegensatz zu dem äußerlichen Mineralisie- rungsprozeß, der sich auch in dem oberen Bestände der Pflanze vollzieht, dann merkt man den Zusammenhang zwischen dem, was innerlich in der Hauptesorganisation vor sich geht, und dem, was im Wurzelbildungsprozeß vor sich geht, namentlich in dem, was als Mineralisieren- des im Wurzelbildungsprozeß auftritt. Man merkt dann auch, daß in einer gewissen Weise ein Gegensatz vor- liegt - trotz der Ähnlichkeit ein Gegensatz -, wie er sich etwa ausdrückt, wenn ich drei und drei habe, das eine positiv, das andere negativ.",
      "Dann habe ich zweimal drei, aber habe doch einen Gegensatz darinnen. So ist vorhan- den etwas, was in einer gewissen Beziehung gleich und doch gegensätzlich ist: in dem innerlichen Mineralisie- rungsprozeß des menschlichen Hauptes und in dem äuße- ren der Pflanzenwurzelbildung, und auch in dem äußeren Mineralisierungsprozeß des Erdenplaneten selber.",
      "Von hier aus findet man dann auf rationale Weise den thera- peutischen Bezug zwischen dem, was äußerlich ist und dem, was im Menschen innerlich ist. Und der Übergang kann gefunden werden über die Pathologie zur rationalen Therapie.",
      "Auf dieses letztere kann ich hier nur hinweisen. Denen, die es angeht, werden ja noch weitere Aufschlüsse gerade über dieses Kapitel gegeben werden, wie es auch schon in einem Frühlingskurs des vorigen Jahres für Ärzte und Medizinstudierende geschehen ist.",
      "Das wird aber das Be- deutsame sein, daß wirkliche Wissenschaftlichkeit - die zu gleicher Zeit nicht bloß Theorie, sondern Hinweis auf fruchtbares Handeln, auf die Tat ist aus der Geistes- wissenschaft heraus wird geboren werden können. Die Menschheit steht heute, insbesondere auf wissen- schaftlichem Gebiete, vor der Notwendigkeit, nicht einen kleinen, sondern einen großen Entschluß zu fassen: den Entschluß, in das organische Leben hineinzukommen da- durch, daß man nicht bloß den Inhalt der alten Denk- weise etwas modifiziert, sondern daß man in diese alte Denkweise selber ein neues Element hineinbringt, das Ele- ment übersinnlicher Erkenntnis.",
      "Was heute diesem Ent- schluß bei dem größeren Teil derer, die ihn fassen sollten, noch entgegensteht, das ist nicht irgendein Mangel der menschlichen Erkenntnisfähigkeit, das ist ein Mangel, ein begreiflicher Mangel, an Mut für diesen starken radikalen 116 Umschwung. Man möchte viel lieber leiden, als zu etwas Neuem vorschreiten.",
      "Man möchte beim alten bleiben und das Alte in kritischer oder in anderer Weise nur etwas umformen. Aber nicht eher wird Licht in das hineinkommen, was hier für unsere gegenwärtige Zivilisation auf dem Er- kenntnisgebiete vorliegt, als bis man den Mut faßt zum Vorschreiten von der Denkweise, die üblich ist, zu einer anderen Denkweise.",
      "So lange wird nichts Ersprießliches herauskommen, als man bei der Ausrede sich beruhigt, «man könne ja doch die imaginative Denkweise nicht er- reichen», was auch nicht wahr ist. Sondern erst dann wird ein Umschwung eintreten, wenn man einsehen wird: man darf nicht träge bleiben innerlich, wenn die Wissenschaft in ihrer Betrachtungsweise in fruchtbarer Art ihren Fort- gang nehmen soll.",
      "Man muß innerlich regsam und fleißig werden. Ein Willensentschluß, nicht bloß eine theoretische Erwägung ist hier notwendig. Und da zu Willensent- schlüssen - das weiß jeder Psychologe - die Menschheit schwerer zu bringen ist als zu theoretischen Erwägungen, bei denen man hübsch ruhig in seinem Inneren bleiben kann, so hat die moderne Menschheit gerade Gelegenheit, zu zeigen, wie sie aus der Not heraus zur Größe sich er- heben kann, indem sie sich entschließt, zunächst auf dem soeben genannten Gebiete, auf dem Erkenntnisgebiete, auf dem Geistgebiete den Mut zu einem großen Umschwung, nicht zu kleinen Erwägungen aufzubringen."
    ],
    "sentences": [
      [
        "Das Gebiet, auf das ich heute zu sprechen kommen werde, ist ein so ausgedehntes selbst wenn es nur von einem einzigen Gesichtspunkte aus beleuchtet werden soll -, daß dasjenige, was ich in der Lage sein werde heute zu geben, nur spärliche Andeutungen werden sein können, und ich bitte Sie, dies in Berücksichtigung zu ziehen.",
        "Es handelt sich ja darum, daß im Fortschreiten von den anorganischen Naturwissenschaften zu den organischen Naturwissen- schaften - und dann weiterhin zu psychologischer und geistiger Betrachtung - auf der einen Seite sich immer mehr und mehr die Notwendigkeit geisteswissenschaftlich- anthroposophischer Betrachtung ergibt, daß sich aber auch andererseits bei diesem Fortschreiten immer mehr und mehr zeigt, wie das, was hier Geisteswissenschaft genannt wird, befruchtend wirken kann auf die einzelnen Fach- wissenschaften."
      ],
      [
        "Bei dem, was gesagt werden konnte über das Wesen des Mathematischen, über das Wesen der anorganischen Na- turwissenschaften, da handelte es sich weniger darum, daß durch geisteswissenschaftliche Betrachtung irgendwie in einer ganz durchgreifenden Art eine andere Behandlungs- weise und namentlich ein anderer Inhalt herbeigeführt werde, als er in unserer gegenwärtigen Wissenschaftsgesin- nung schon vorhanden ist.",
        "Sie haben daher aus den bis- herigen Vorträgen über Mathematisches und über anorga- nische Naturwissenschaften einen gewissen Grundton ver- nehmen können, der dahin ging, anzudeuten, wie überall, 96 im Mathematischen sowohl wie im Anorganischen, die, wenn auch von den meisten unbemerkten, Anfänge zu derjenigen Behandlungsweise dieser Wissenschaften vorlie- gen, die von der hier gemeinten Geisteswissenschaft als die richtige anerkannt werden muß."
      ],
      [
        "Sie haben gesehen, wie man hindeuten muß auf den Übergang von der analyti- schen Behandlung der Geometrie zu der synthetischen Be- handlung, und wie man da findet, wie ein Weiterbeschrei- ten dieses Weges in imaginatives Betrachten hinführt, wenn man nur nicht beim Formalen stehenbleibt, sondern zu einem lebendigen Erfassen desjenigen, was da eigentlich vorliegt, übergeht.",
        "Und Sie haben dann gesehen, als eine mehr rein mathematische Betrachtung dargeboten wurde, wie aus einer gewissen lebendigeren Behandlung der Pro- bleme dasjenige hervorgehen soll, was man sich im Mathe- matischen und in den anorganischen Naturwissenschaften als das im anthroposophischen Sinne Richtige zu denken hat."
      ],
      [
        "Gewissermaßen sind wir untergetaucht in diese Wissen- schaften und haben in ihnen selber die Kraftpunkte ge- sucht, in deren Richtungen weitergegangen werden soll.",
        "Es handelt sich nur darum, daß man bei diesen Wissenschaf- ten streng innerhalb der gegenständlichen Betrachtungs- weise bleibt, welche die Eigentümlichkeit des gegenwärti- gen Menschheitsbewußtseins ist, und daß man nicht nötig hat, zu etwas anderem zu kommen als zu einem gewissen Wie in der Behandlungsweise dieser Betrachtung."
      ],
      [
        "In derselben Lage ist man nicht bei den organischen Naturwissenschaften, obwohl etwas wiederum in anderer Beziehung Ähnliches auch hier vorliegt.",
        "Wenn man heute von Mathematik, von anorganischen Naturwissenschaften, von Phoronomie, Mechanik und so weiter spricht, dann hat man auf die Denkweise hinzuweisen, an der man etwas zu reformieren hat, wie das gestern geschehen ist. 97 Bei den organischen Naturwissenschaften beginnt aber, daß man hinzuweisen hat nicht auf das Abzuweisende, sondern auf das Aufzunehmende."
      ],
      [
        "Das beginnt schon in- nerhalb der Tatsachenwelt selber.",
        "Da kann durch eine bloße Reform der Denkweise eigentlich nichts Ausgiebiges erreicht werden.",
        "Ich möchte zunächst eine kurze historische Betrachtung erläuternd voranschicken, durch die klargemacht werden soll, in welcher Weise auf diesem Gebiete vorzuschreiten ist, um zu einer fruchtbaren Anschauung zu kommen."
      ],
      [
        "Wir haben an anderen Stellen in unserer Betrachtung darauf hingewiesen, daß im fortlaufenden Entwickelungsgange der Menschheit eigentlich erst seit dem 15.",
        "Jahrhundert der nachchristlichen Zeit herauf getaucht ist, was wir die beson- dere Art unseres heutigen Bewußtseins nennen."
      ],
      [
        "Alle frü- here Betrachtungsweise war im Grunde genommen eine ganz andere.",
        "Es ergriff die Menschheit erst von dem ge- nannten Zeitpunkte an jene Bewußtseinsform recht, die auf der einen Seite zum Gebrauche der Freiheit führt, aber auf der anderen Seite den Menschen, dadurch daß sie ihn auf sich selbst zurückweist, in eine Abstraktion hin- einwirft, durch die er gegenüber der Seinswelt in einer gewissen Weise wirklichkeitsfremd wird."
      ],
      [
        "Es ist die Be- trachtungsweise, die sich nur an äußere Beobachtungen und deren Beschreibung hält, an Anordnung von Versuchen, von Experimenten und Beobachtung ihrer Ergebnisse, das heißt der Antworten, die die Natur erteilt, wenn ihr nicht bloß theoretisch, sondern praktisch, im Experiment, Fra- gen gestellt werden.",
        "Was von Seelenkräften angewendet wird, indem auf diese Art die Wissenschaft zustande kommt, das ist die kombinierende Verstandeskraft."
      ],
      [
        "Diese kombinierende Ver- standeskraft ist zunächst, ich möchte sagen, das große 98 praktisch-wissenschaftliche Problem.",
        "Sie wird dieses, wenn man die Frage aufwirft nach ihrer richtigen Anwendbar- keit."
      ],
      [
        "Und diese Frage nach der richtigen Anwendbarkeit der Verstandes- oder auch der gewöhnlichen Vernunft- kraft - im Beobachten, im Zusammenfassen der Beobach- tungen, im Experimentieren -, diese Frage ist besonders für Goethe aufgetaucht.",
        "Und wer sich - Sie können das nachlesen in meinen jetzt schon fast vierzig Jahre alten «Einleitungen zu Goethes Naturwissenschaftlichen Schrif- ten» - in das vertieft, was da eigentlich bei Goethe zum Problem geworden ist, der wird finden, daß Goethe die Verstandes- oder Vernunftkraft nicht so angewendet wis- sen wollte, daß sie der Wissenschaft einen eigentlichen In- halt gibt, daß man gewissermaßen aus der Verstandes- oder Vernunftkraft heraus etwas über das Sein als solches aussagt, sondern so, daß diese Verstandes- oder Vernunft- kraft nur dazu verwendet wird, die Phänomene so ange- ordnet zu denken, daß das eine Phänomen das andere erklärt."
      ],
      [
        "Dann hat man also, indem man sich seines Ver- standes oder seiner Vernunft bedient, nichts hinzugetragen zu dem, was die Phänomene selber aussprechen.",
        "Es handelt sich darum, wenn man rein den Verstand anwenden will, daß man dann auch rückhaltlos vorschrei- tet zu einer reinen Phänomenologie, das heißt, den Ver- stand nur dazu benützt, ein Phänomen reinlich anzu- schauen, nichts anderes zu tun, als es eben zu reinlichem Anschauen zu bringen, und dann das andere dazugehörige Phänomen danebenzustellen; so daß durch diese Anord- nung der Phänomene - was dann im Experiment auch zur praktischen Ausführung kommt - die Phänomene selbst veranlaßt werden, daß sie sich gegenseitig erklären."
      ],
      [
        "Der Verstand hat also bloß eine ordnende, eine gewissermaßen real methodologische Bedeutung, keine qualitative Bedeu- 99 tung.",
        "Aus ihm darf im Goetheschen Sinne nichts hervor- gehen, was irgendwie über das Sein selbst etwas aussagt."
      ],
      [
        "Das ist, wie ich glaube, scharf präzisiert, was Goethe als den Gebrauch der Verstandeskraft ansah, und das ist auch dasjenige, dem das allgemeine Bewußtsein der Mensch- heit seit dem ersten Drittel des 15.",
        "Jahrhunderts zustrebt."
      ],
      [
        "Man kann sagen, es haben noch nicht alle gelernt, dann, wenn es sich um den Verstand handelt, in einer gewissen Weise zu resignieren, wie das Goethe in seinen eigenen Forschungen tun wollte, wenn es auch bei ihm nicht über- all voll zur Ausführung gekommen ist.",
        "Aber unbewußt lebt in dem Wissenschaftsstreben, aus dem gerade Geistes- wissenschaft heraus will aber auf andere Art als durch den Verstand , diese Art des Verstandeslebens doch wie ein unbewußtes Ideal."
      ],
      [
        "Und es ist das, was ich jetzt sage, mit Händen zu grei- fen, wenn man jene Fortgänge sieht, die im naturwissen- schaftlichen Denken vorliegen, sagen wir, von dem An- fang des 19.",
        "Jahrhunderts - und ich meine jetzt nicht bei den Naturphilosophen, sondern bei den empirischen Na- turforschern etwa von der Art des Johannes Müller bis etwa zu Mach oder gar zu Poincare und den anderen, oder zu Fritz Mauthner, der allerdings kein Naturfor- scher ist."
      ],
      [
        "Wer so recht eine Anschauung gewinnen will, was da vorliegt, der muß sich bekanntmachen mit etwas, was in der ersten Hälfte des 19.",
        "Jahrhunderts noch eine gewisse Rolle gespielt hat, was aber dann gegen die Mitte des 19."
      ],
      [
        "Jahrhunderts vollständig fallengelassen worden ist, und was jetzt in einer merkwürdigen Gestalt da oder dort wiederum in der wissenschaftlichen Betrachtung auftaucht.",
        "Das ist die Idee der Lebenskraft, das, was man im wissen- schaftlichen Leben den Vitalismus nennt. 100 Wenn wir zu der Vorstellung von Vitalkraft zurück- gehen, die man in älteren Zeiten hatte, so sieht man, daß die Anhänger des Vorhandenseins dieser Vitalkraft sich sagten: Wenn wir ein Ding der anorganischen Natur be- trachten, so finden wir in diesem Ding der anorganischen Natur allerlei Kräfte, Wärmekraft, Lichtkraft, elektrische Kraft und so weiter; wenn wir aber ein Wesen der organi- schen Welt betrachten, so finden wir außerhalb diesen Kräften, welche die anorganische Natur konstituieren, auch noch die Vitalkraft, die Lebenskraft."
      ],
      [
        "Diese Lebens- kraft ist in jedem Lebewesen vorhanden wie im Magneten die Magnetkraft.",
        "Sie bemächtigt sich gewissermaßen der anorganischen Kräfte, um diese zusammenzufassen und aus ihnen Wirkungen hervorzubringen, die sie, auf sich selbst gestellt, nicht leisten können."
      ],
      [
        "Dieser Vitalkraft wurde der letzte Stoß zum Abdanken gegeben durch die Darstellung eines organischen Stoffes in synthetischer Weise von Wöhler und Liebig, und sie wurde als solche in der zweiten Hälfte des 19.",
        "Jahrhun- derts fallengelassen."
      ],
      [
        "Aber im sogenannten Neovitalismus taucht sie wiederum in der neuesten Zeit aus der Verbor- genheit auf, weil gewisse Denker dazugekommen sind, sich zu sagen: Wenn wir die Methoden, die wir ausgebil- det haben, um mit Hilfe der anorganischen Kräfte das Anorganische zu erklären, auf das Organische anwenden, dann kommen wir eben nicht aus; wir müssen im Organi- schen etwas anderes suchen.",
        "Und, ich möchte sagen, mit einem deutlichen Anklang an die alte Lebenskraft taucht im Neovitalismus wiederum so etwas herauf für die Er- klärung in den organischen Wissenschaften."
      ],
      [
        "Wer sich aber wirklich ordentlich kritisch einläßt auf dasjenige, was als Lebenskraft selbst noch in der Betrach- tung von Johannes Müller vorkommt, der wird finden, 101 daß in dieser Lebenskraft etwas vorliegt, was sich als Be- griff in Wirklichkeit nicht vollziehen läßt.",
        "Und ich möchte sagen, an der Unmöglichkeit, die Lebenskraft als Begriff zu fassen, ist sie im Laufe des 19."
      ],
      [
        "Jahrhunderts in der wis- senschaftlichen Betrachtung abgestorben.",
        "Man konnte sie nicht fassen.",
        "Und warum konnte man sie nicht fassen?",
        "Zunächst wird man, wenn man ganz vorsichtig vorgeht in der Betrachtung der organisch-naturwissenschaftlichen Me- thodik des 19."
      ],
      [
        "Jahrhunderts, sehen, wie diejenigen, die da mit der Idee dieser Lebenskraft ringen, finden, sie können damit nichts anfangen.",
        "Was sie anfangen wollen, ent- schwindet ihnen sogleich, wenn sie mit ihrer Idee an die Erscheinung herangehen."
      ],
      [
        "Sie kommen doch nicht auf den eigentlichen Nerv der Sache.",
        "Sie kommen nicht darauf aus dem Grunde, weil sie die eigentliche Funktion der Ver- standestätigkeit nicht scharf fassen.",
        "Die Verstandestätigkeit tendiert in unserem Zeitalter dahin, nur das Phänomen zu betrachten und es hinzustel- len neben ein anderes, damit Phänomen das Phänomen erklärt."
      ],
      [
        "Aber das läßt sich bei der Lebenskraft nicht aus- führen.",
        "Bei der Lebenskraft muß man immer, wenn man überhaupt etwas tun will, von der Verstandestätigkeit aus etwas hineinschieben in das Phänomen.",
        "Man muß gewis- sermaßen dem Phänomen etwas unterschieben."
      ],
      [
        "Und dar- innen liegt das, was allmählich im Gebrauche der Idee von der Lebenskraft bedenklich geworden ist.",
        "Das war dann die Ursache, daß man sie ganz hat fallen lassen und daß als ein gewisses Ideal in weitesten Kreisen entstanden ist, die Lebewesen nun überhaupt als einen Zusammenfluß, eine Kombination derjenigen Kräfte anzuschauen, die auch in der anorganischen Natur walten."
      ],
      [
        "Mit anderen Worten: die Idee der Lebenskraft ist eigentlich eine Art Wechselbalg geworden.",
        "Man ist dazu IO2 gekommen, das Konstitutive in den Wissenschaften nur im Phänomen zu suchen.",
        "Die Lebenskraft ergab sich als Phänomen nicht."
      ],
      [
        "Man mußte - was aber eigentlich nicht statthaft war in diesem Zeitalter der Menschheitsentwicke- lung - vom Verstande aus die Vitalkraft konstruieren.",
        "Das war der negative Teil der Entwickelung, in der wir heute drinnenstehen."
      ],
      [
        "Denn in dem Neovitalismus tritt nichts Anschauliches auf.",
        "Was der Neovitalismus an die Stelle einer bloß das Anorganische kombinierenden Erklä- rung der Lebenserscheinungen setzt, das ist nichts anderes als eine Art Aufwärmung des alten Vitalismus."
      ],
      [
        "Und man könnte sagen, daß deutlich im äußeren Betriebe des wis- senschaftlichen Lebens eine Art Abbild dessen vorhanden ist, was da eigentlich vorgeht im inneren Geistesleben.",
        "Ich kann heute nur in einzelnen Erscheinungen hinweisen auf dieses Abbild."
      ],
      [
        "Aber wer die beieinanderliegenden Phäno- mene gerade so betrachten kann, daß sie sich gegenseitig aufhellen, der wird schon die Bewahrheitung desjenigen, das ich jetzt meine, auch einsehen.",
        "Was sich aus einer älteren Betrachtungsweise erhalten, was die Begriffe und Ideen daraus zurückgehalten hat, das figurierte bis vor kurzer Zeit, bis in die Mitte des 19."
      ],
      [
        "Jahrhunderts, noch recht unansehnlich als Philosophie.",
        "Und ich habe das- jenige, was mit dieser Philosophie vorging, in meinem ersten Vortrage dieser Reihe, wenigstens andeutungsweise auseinanderzusetzen versucht."
      ],
      [
        "Allein in der zweiten Hälf- te des 19.",
        "Jahrhunderts, da gingen schon einzelne merk- würdige Erscheinungen auf dem Gebiete des philosophi- schen Lebens vor.",
        "Wir können sehen, wie ein recht gewissenhafter Denker, der nur nicht in der Lage war, die Probleme, die er auf- warf, zu Ende zu denken ich habe ihn an dieser Stelle in diesen Tagen erwähnt , wie Franz Brentano für die 103 Philosophie die naturwissenschaftliche Methode fordert."
      ],
      [
        "Ihm war nichts anderes gegeben als naturwissenschaft- liche Methode als dasjenige, was eben in der Gegenwart als solche üblich ist.",
        "Gewissermaßen war damit das Leit- motiv für alle diejenigen gegeben, die nicht mehr auf eine besondere geistige Methode reflektieren wollten, sondern die sich der allgemeinen Autorität des landläufigen natur- wissenschaftlichen Denkens fügten."
      ],
      [
        "Dann aber kamen noch andere Erscheinungen.",
        "An einzelnen Fakultäten, wo, sagen wir, alte Herbartianer wirkten, kam es dazu, daß diese ihre Lehrkanzeln verließen, und es gab dann Fakul- täten, welche an diese unbesetzten Lehrkanzeln für Philo- sophie nunmehr nicht Philosophen im alten Sinne beriefen, sondern naturwissenschaftlich Denkende."
      ],
      [
        "So zum Beispiel war es in Wien, wo Mach, der Naturforscher, die Lehr- kanzel für Philosophie, die leer geworden war, zu bezie- hen hatte.",
        "Man empfand das noch etwas unbehaglich, und man nannte deshalb das Fach, das er zu vertreten hatte, «induktive Philosophie», hatte ihm also die Lehrkanzel für Induktive Philosophie übertragen, danebengesetzt allerdings einen Mann ich schätze diesen Mann sehr, aber ich charakterisiere jetzt ja objektiv Kulturerscheinun- gen, und damit spielt die persönliche Schätzung keine Rolle -, der vorher Professor für christliche Philosophie an der theologischen Fakultät der neuen Universität war."
      ],
      [
        "Damit dokumentierte man, daß man dasjenige, was in der Philosophie sein sollte, nicht aus irgendeiner neuen Forschungsweise herausnahm, sondern aus der alten Tra- dition.",
        "Und was sich da, ich möchte sagen, in einer ge- wissen auffälligen Weise vollzog, das vollzieht sich ja im- mer wieder."
      ],
      [
        "Abgesehen davon, daß ganz naturwissen- schaftlich Denkende an die psychologischen Lehrkanzeln herangebracht werden und in ein früher als philosophisch 104 angesehenes Gebiet ganz naturwissenschaftliche Denk- weise hineintragen, sehen wir auch sonst, wie naturwissen- schaftlich Denkende heute ganz offiziell als Träger der Philosophie funktionieren.",
        "In solchen Erscheinungen spricht sich dasjenige auch äußerlich aus, was ich hier an- zudeuten habe: mit dem, was da in der neueren Zeit her- aufgekommen ist als der kombinierende Verstand, der in seiner Reinheit nur so angewendet werden kann, wie ihn Goethe angewendet wissen wollte, mit dem läßt sich über die Lebenserscheinungen nichts ausmachen."
      ],
      [
        "Hier liegt wiederum der Punkt, wo Ehrlichkeit und Unbefangenheit des wissenschaftlichen Denkens streng ge- fordert werden muß.",
        "Und die Methoden, die mit Hilfe äußerer Beobachtung, äußeren Experimentes, mit Hilfe dieses kombinierenden Verstandes forschen, die können, wenn sie mit sich selber richtig kritisch zu Werke gehen, wenn sie sich aus ihren Betrachtungen heraus, wenn ich so sagen darf, ein volles Bewußtsein über ihre eigene Trag- weite verschaffen, nicht anders, als sagen: Wir sind als Methoden nur anwendbar auf das Gebiet der anorgani- schen Naturwissenschaften, da gehören wir hinein, da kön- nen wir die Betrachtungsweise groß machen; aber wir dür- fen nicht, ohne den ganzen Sinn der Betrachtungsweise, auch den Inhalt der Betrachtungsweise zu ändern, in das Gebiet der organischen Naturwissenschaften heraufsteigen."
      ],
      [
        "Das muß von dieser Methode unberührt bleiben.",
        "Geisteswissenschaft hat nun von der anderen Seite aus zu sprechen.",
        "Geisteswissenschaft hat zu sagen: Es gibt auch die Möglichkeit einer Bewußtseinsentwickelung, ent- sprechend dem Lauf, der von jenen Bewußtseinsformen aus genommen worden ist, die vor dem 14."
      ],
      [
        "Jahrhundert noch ihre letzten Blüten getrieben haben.",
        "Wie von diesen Bewußtseinsformen aus zum rein gegenständlichen Be- 105 wußtsein, das nicht in der Phänomenalität steckenbleiben soll, fortgeschritten worden ist, so muß heute, behufs wissenschaftlicher Betrachtungsweise des Organischen, durch die innerliche Entwickelung der Seele heraufge- schritten werden zu den anderen Bewußtseinsformen: zum imaginativen Bewußtsein, inspirierten Bewußtsein, intuitiven Bewußtsein."
      ],
      [
        "Denn soll der Verstand zurechtkommen mit den Le- benserscheinungen, dann muß für den Verstand das, was sich innerhalb des Gebietes der Lebenserscheinungen ab- spielt, Beobachtung werden, Phänomen werden.",
        "Das kann es nicht innerhalb der sinnlichen Beobachtung."
      ],
      [
        "Der Verstand kann nicht konstitutiv werden für einen Inhalt der organischen Naturwissenschaften.",
        "Der Verstand muß sich auch da kombinierend verhalten.",
        "Aber die An- schauung muß ihm geliefert werden.",
        "Diese Anschauung wird ihm geliefert im imaginativen Erkennen."
      ],
      [
        "In der Ausbildung des imaginativen Erkennens, wie ich sie dar- gestellt habe in meinem Buche «Wie erlangt man Er- kenntnisse der höheren Welten?», wird nämlich, abgesehen von allem übrigen, was über dasselbe gesagt werden kann, die Möglichkeit errungen, mit dem alten Vitalismus, der einen Wechselbalg von Begrifflichkeit geliefert hat, zu brechen und die imaginative Anschauung des Lebens an dessen Stelle zu setzen.",
        "Selbstverständlich kommt jetzt der ungeheuer billige Einwand, der nun gemacht werden kann."
      ],
      [
        "Es kann gesagt werden: Nun ja, aber wir normalen Menschen haben eben nur diesen kombinierenden Verstand.",
        "Es mag solche Käuze geben, welche zur Imagination, Inspiration und so weiter fortschreiten.",
        "Wir wollen das nicht weiter bezwei- feln, aber wir haben sie eben nicht."
      ],
      [
        "Deshalb gilt für uns eine Philosophie, welche diese Inhalte der Imagination 106 und so weiter ablehnt, welche sich nicht damit zu schaffen macht, diese Inhalte der Imagination, Inspiration und so weiter in sich selber als Philosophie hereinzunehmen.",
        "Dieser billige Einwand ist in der folgenden Weise zu entwerten."
      ],
      [
        "Ich will mich mit einem Beispiel verdeutlichen, das ich öfter schon erwähnt habe.",
        "Wenn die Geistesfor- schung einfach die Tatsachen nimmt, die heute schon der empirischen organischen Wissenschaft vorliegen, dann kommt man zum Beispiel in der Lehre vom menschlichen Herzen zu ganz anderen Anschauungen als denen, die durch einen falschen, aus alten Zeiten traditionell fortbe- wahrten alten Verstandesgebrauch noch immer in der land- läufigen Wissenschaft zustande kommen."
      ],
      [
        "Da wird das Herz angesehen wie so eine bessere Pumpe, welche das Blut durch den Organismus treibt.",
        "Diese Anschauung folgt nur dann als eine «richtige» für den Menschen, wenn er auf den menschlichen Organismus als ein Lebewesen den Verstand anwendet, der darauf nicht anwendbar ist."
      ],
      [
        "So- bald man zur imaginativen Betrachtung aufsteigt, kommt man dazu, sich zu sagen: Nicht das Herz treibt das Blut durch die Adern des Organismus, sondern die Herzbewe- gung ist das Ergebnis des inneren Blutlebens.",
        "Das Blut selbst ist es, welches aus dem intensiven eigenen Leben, welches zentralisiert ist im Herzen, diese Bewegung verur- sacht, so daß die Herzbewegung die Folge der Blutbewe- gung, und nicht das Umgekehrte der Fall ist."
      ],
      [
        "Das ergibt sich unmittelbar aus der imaginativen Betrachtung des menschlichen und dann auch des tierischen Organismus.",
        "Nun, wer ohne diese imaginative Betrachtung eine Herzlehre, eine Herzbewegungslehre aufstellt, der muß, wenn er ehrlich ist, dazu kommen, in dieser Betrachtungs- weise Unzulängliches zu finden, an dem stehenzubleiben ist."
      ],
      [
        "Und wenn er dann ausschaltet, was er selbst in seiner 107 Erklärung als unzulänglich erkannt hat, aber beibehält die empirische Erkenntnis der Tatsachen, der gesamten Tatsachenwelt des menschlichen und tierischen Organis- mus, insofern sich diese Tatsachenwelt auf Blutbewegung und Herzbewegung bezieht, wenn er alles zusammen- faßt - Geisteswissenschaft schreckt nie vor einer wirk- lich gründlichen und gewissenhaften Prüfung durch andere zurück , was aus dem Umfang der gegenwärtigen Ana- tomie, Physiologie, Biologie und so weiter zu gewinnen ist, namentlich auch, was, erläuternd dieses Problem, aus der Embryologie zu gewinnen ist, dann wird er sich sagen: Nun, derjenige, der auf dem Boden imaginativer Erkennt- nis steht, gibt diese Erklärung.",
        "Ich kenne die Tatsachen; setze ich das Ergebnis der imaginativen Erkenntnis ehr- lich voraus, prüfe ich daran meine Tatsachen, die ich gut kenne, dann stimmt das völlig, und es ist damit aller nur wünschenswerte Grund vorhanden, um dasjenige, was durch imaginative Erkenntnis gewonnen wird, anzuneh- men."
      ],
      [
        "Es kann, sobald gewissenhaft und ehrlich auf diesem Gebiete in der Richtung der wissenschaftlichen Bewußt- seinsentwickelung fortgeschritten wird, nicht mehr die Ausrede gelten, wer nicht selber imaginative Erkenntnis habe, der brauche diese imaginative Erkenntnis nicht an- zuerkennen.",
        "Sondern es muß an dessen Stelle das andere treten, daß man sagt: Ich kenne gut die Tatsachen, die sich der sinnlichen Beobachtung darbieten, eine Erklärung aber kommt mir nur von seiten des imaginativen An- schauens."
      ],
      [
        "Mit dieser Erklärung finde ich mich zurecht.",
        "Die Tatsachen sind verständlich aus ihr heraus; also sind alle Voraussetzungen für die Annahme gegeben. - Und im Grunde genommen zeigt derjenige, der aus dem eben charakterisierten Grunde die übersinnliche Erkenntnis auf 108 diesem Gebiete ablehnt, nicht, daß er die übersinnliche Erkenntnis nicht beherrscht."
      ],
      [
        "Die ist ja heute noch nicht so weit, daß man sie leicht beherrschen könnte.",
        "Sondern er beweist, daß er die ihm vorliegenden Tatsachen nicht rich- tig werten kann.",
        "Er beweist den Mangel seiner Einsicht in die sinnlich-empirisch gewonnene Tatsachenwelt selber."
      ],
      [
        "Und das ist am häufigsten der Fall in der heutigen Be- trachtungsweise der organischen Naturwissenschaften.",
        "Die Betrachtungsweise, die für die organischen Naturwissen- schaften nötig ist, ist diejenige, welche sich von dem blo- ßen gegenständlichen Erkennen zu dem imaginativen Er- kennen erhebt."
      ],
      [
        "Denn im imaginativen Erkennen enthüllt sich erst das Geheimnis des Lebens.",
        "Goethe hat von der reinen Phänomenologie aus, die er angewendet wissen wollte zum Beispiel in der Farben- lehre und in der Tonlehre, hingestrebt zu dem, was er seine Morphologie nannte, zu der Erfassung des Sich- Gestaltenden."
      ],
      [
        "Er ist nur bis zu einem gewissen Grade der Erkenntnis gekommen.",
        "Was er inauguriert hat, das muß fortgesetzt werden.",
        "Man sieht, wie er nur bis zu einem gewissen Grade gekommen ist: nachdem seine Betrach- tungsweise bis zu einem hohen Grade, wenn auch nicht ganz, für das unbewußte Pflanzenreich ausgereicht hatte, mußte er, als er von dem Pflanzenreich zu der Betrach- tung der Metamorphose des tierischen Reiches gehen wollte, stehenbleiben."
      ],
      [
        "Sehen Sie sich die Abhandlungen an, die er in bezug auf die Metamorphose des tierischen Reiches geschrieben hat.",
        "Sie werden überall sehen, wie er als ein gewissenhafter Mensch abbricht, weil es eben nicht mehr weitergeht, weil man von einem gewissen Momente von dieser Morphologie Goethes, wenn man weiter kommen will, zu etwas noch Geistigerem hinkommen muß, als die bloße Gestalt ist: zu dem, was innerlich die Bewußtheit 109 mit der Empfindungs- und Willenswelt nun im in- spirierten Erkennen erfassen kann."
      ],
      [
        "Wenn man die Sache so ansieht, dann wird man haupt- sächlich in der Betrachtungsweise, in dem Wie des An- schauens, in dem Wie der Ausbildung der Methodik ein Wesentliches sehen.",
        "Und - wie gesagt, ich kann heute nur andeuten - wenn wir von diesem Gesichtspunkte aus einen Blick werfen auf das, was im Verlaufe des 19."
      ],
      [
        "Jahr- hunderts und im Beginne des 20.",
        "Jahrhunderts Evolutions- lehre geworden ist, dann werden wir das Folgende finden: Zunächst wird äußerlich empirisch die Reihe der Lebe- wesen verfolgt, von der unvollkommenen, sogenannten unvollkommenen Monere bis herauf zum Menschen, und es wird in der Betrachtungsweise so verfahren, daß man sich immer das Vollkommenere aus dem Unvollkomme- neren hervorgehend denkt."
      ],
      [
        "Wenn man in einer etwas an- deren Weise vorgeht, wie das bis zu einem gewissen Grade Haeckel getan hat, so konstruiert man wenigstens in der Vorfahrenreihe der jetzigen Wesen solche, welche wie- derum ziemlich genaue Abklatsche der jetzigen Lebewesen sind.",
        "Die konstruierten Wesen der Vorzeit in dem alten Haeckelschen Stammbaum haben durchaus den Charakter desjenigen, was auch heute lebt."
      ],
      [
        "Dasjenige aber, was sich der Imagination darbietet, führt zu einer ganz anderen Betrachtungsweise.",
        "Und ich will - weil es die Kürze der Zeit fordert, nur schema- tisch - diese Betrachtungsweise andeuten: Wenn man vom Standpunkte der imaginativen Anschauungsart ausgeht, kann zum Beispiel das menschliche Haupt in Vergleichung mit der Rückenwirbelsäule sachgemäß nur so betrachtet werden, daß man sagt: Diese menschliche Hauptgestal- tung, so unähnlich sie auch in der äußeren Form, in ihrer heutigen Metamorphose der Rückenwirbelsäule ist, kann HO nur metamorphosisch vorgestellt werden als eine Umbil- dung der Rückenwirbelsäule."
      ],
      [
        "Man hat sich zu denken, daß die Nervenorganisation des Rückenmarks sich umgestaltet, metamorphosiert zu dem, was uns als das Gehirn er- scheint, und daß sich auch die umschließenden Knochen, die Wirbelknochen der Rückenmarkswirbelsäule, umge- stalten zu dem, was die Schädeldecke wird.",
        "Aber nun ist es wichtig, das Folgende ins Auge zu fassen."
      ],
      [
        "Man muß sich vorstellen, daß in einer gewissen Beziehung dasje- nige, was ich hier im Gegensatz zu der Linie a-b wie einen Kreis hingezeichnet habe, gewisserma- ßen eine aufgeplusterte Rücken- wirbelsäule ist und hinweist auf dasjenige, was es einmal in einer früheren Metamorphose war: selbst etwas wie eine Rücken- wirbelsäule, aber unter anderen äußeren Bedingungen.",
        "Was ich als einen Kreis gezeichnet habe, hat sich also in gewisser Weise aus a-b herausgebildet."
      ],
      [
        "Was aber heute als Rückenwirbelsäule am menschlichen Organismus ist, das hat sich dem also Ausgebildeten erst später angegliedert.",
        "Das ist beim Menschen die spätere Bildung.",
        "Nachdem sich der Schä- del umgebildet hatte aus einer Kräfteanordnung, die heute in etwas anderer Weise in der Rückenwirbelsäule erscheint, gliederte sich an ihn diese heutige Rückenwirbelsäule an."
      ],
      [
        "Was das «Unvollkommenere» am Menschen ist, ist also 111 das Spätere, und was das «Vollkommenere» ist, ist das Frühere.",
        "Und wir werden zurückgeführt, wenn wir sinn- gemäß vorgehen, in ein Zeitalter, in dem in anderer Meta- morphose die Kräfte, welche das menschliche Haupt bil- den, schon vorhanden waren, nicht aber die Kräfte, welche die heutige menschliche Rückenmarksäule bilden."
      ],
      [
        "Wenn wir aber diese letzteren Kräfte ins Auge fassen, dann sind es dieselben Kräfte, die uns zum Beispiel im Tierreiche entgegentreten, wo die Schädelbildung eine Ge- staltung ist, die nur eine geringere Umwandlung gegen- über der Rückenwirbelsäule aufweist als beim Menschen.",
        "So daß wir sagen müssen: Was im menschlichen Haupte vorliegt, weist uns als früheste Bildung in ältere Zeiten zurück als das, was dann als Mensch schon mit der Rük- kenwirbelsäule aufgetreten ist, und auch als das, was im Tierreiche vorliegt."
      ],
      [
        "Wir haben in der Evolution nicht den Menschen abzuleiten aus dem Tierreiche, sondern wir ha- ben uns zu sagen, eine sinngemäße Ausdeutung der Tat- sachen selber zeigt uns, daß der Mensch ein älteres Wesen ist als die Tiere, daß die Tiere später entstanden sind und es in ihrer Evolution nur zu dem gebracht haben, was beim Menschen heute auch in seiner späteren Gestaltung als Rückenwirbelsäule zutage tritt, es aber, weil ihnen eine kürzere Zeit zur Verfügung stand, nicht dahin ge- bracht haben, die Schädelmetamorphose in dem mensch- lichen Sinne auszubilden.",
        "Wenn Sie diesen Gedanken, den ich hier nur skizzen- haft vorbringen kann, ausdenken, dann kommen Sie zu einer wirklich sinngemäßen Auffassung der Evolutions- lehre."
      ],
      [
        "Die großartigen Tatsachen, die vorliegen, die man nur in ihrem ganzen Umfange kennen muß, werden er- klärlich, wenn man diese aus imaginativem Erkennen ge- schöpfte Anschauungsweise zugrunde legt.",
        "Und aus die- 112 sen Voraussetzungen heraus kommt man dann zu ganz gewissen Bezügen, Verhältnissen desjenigen, was in der äußeren Wissenschaft unseren Erdenverhältnissen vorliegt."
      ],
      [
        "Denken Sie, daß man durch Weiterverfolgen dieses Ge- dankens dazu kommt, sich zu sagen, wie der Mensch zu dem Tiere steht.",
        "Man kann auf diese Weise aber auch weiterschreiten und erkennen lernen, wie der Mensch steht zu dem Pflanzenreich und zuletzt zu dem mineralischen Reich, das man durch Beobachtung, Experiment und den kombinierenden Verstand in seinem Phänomenzusammen- hang erfaßt."
      ],
      [
        "Mit einer solchen Vorstellungsweise kommt man dazu, des Menschen Verhältnis zu seiner Umwelt wirklich zu durchschauen, wie man in einer gewissen Weise die Bezie- hungen der Gebiete, die uns in der mathematischen Wis- senschaft zu mathematischen Urteilen führen, durchschaut.",
        "Man kommt dazu, immer mehr und mehr auszubilden, was Goethe wie ein Ideal vorschwebte, indem er sagte, seine Urpflanze müsse in der Idee etwas werden, mit dem man erkennend jede einzelne Pflanze in ihrem entspre- chenden Charakter vor die Seele hinstellen kann."
      ],
      [
        "Ge- radeso wie man, wenn man den allgemeinen Begriff des Dreieckes hat, auch weiß, was bei irgendeinem besonderen Dreieck auftritt.",
        "Diese Metamorphosierung der mensch- lichen Erkenntnis für das organische Erkennen, das ist es, was Goethe als ein Ideal vorschwebte."
      ],
      [
        "Aber nun möchte ich mich wiederum durch ein Beispiel veranschaulichen.",
        "Wenn wir von diesem Gesichtspunkte ausgehen, kommen wir dazu, wirklich genauer ins Auge zu fassen, was sich zum Beispiel im menschlichen Haupte als Funktionen abspielt."
      ],
      [
        "Wir lernen erkennen, wie die Funk- tionen des menschlichen Hauptes, indem sie in der Art, wie ich es hier dargestellt habe, der Evolution unterliegen, heute bereits wiederum in Rückbildung begriffen sind, wie sie von anderen Zuständen ausgegangen sind, zum menschlichen Haupte geworden sind, wie aber heute durch die äußeren Einflüsse ein Mineralisierungsprozeß stattfindet im menschlichen Haupte.",
        "Und dieser Minerali- sierungsprozeß ist die Parallelerscheinung zu unserem ver- standesmäßigen Erkennen, das auch nur das mineralisch Physische aufzufassen weiß, weil es gebunden ist an einen Mineralisierungsprozeß im menschlichen Nerven-Sinnes- apparat."
      ],
      [
        "Man lernt gerade kennen, wie dem, was man im verstandesmäßigen Erkennen vollbringt, als sein phy- sischer Träger ein ins Organische des Menschlichen hinein sich bauender Mineralisierungsprozeß parallel geht, ein Absetzen von rein Mineralischem innerhalb des Organi- schen.",
        "Indem man dieses Mineralische im Organischen ab- setzt, kommt man dazu, für das Seelische dasjenige aus- zuführen, was verstandesmäßige Tätigkeit dieses mensch- lichen Wesens ist."
      ],
      [
        "Man kommt dazu, innerlich den Zusam- menhang zwischen dem Geistig-Seelischen und dem Phy- sisch-Leiblichen wirklich aufzufassen, nicht bloß abstrakt davon herumzureden, wie es die «psychophysischen Par- allelitiker» und ähnliche Phraseure auf dem Gebiete der Psychologie tun.",
        "Das ist die Art, wie aus dem gegenwärtigen Bestände der organischen Naturwissenschaft auf den Weg hinge- wiesen werden kann, den sie nehmen muß."
      ],
      [
        "Da kann man nicht dabei stehenbleiben, eine bestimmte Denkweise zu fordern; da kann man nur das, was in den empirischen Tatsachen selber weitertreibt, suchen, da muß man an die Stelle der bestehenden Denkweise eine andere, nämlich die des imaginativen Erkennens wirklich treten lassen.",
        "Dann kommt man aber auch zu einer wirklich fruchtba- ren Anwendung dieser Erkenntnis."
      ],
      [
        "Sucht man in der Au- 114 ßenwelt irgend etwas, das nun, versetzt in die Außenwelt, dem entspricht, was im menschlichen Haupte als Minerali- sierungsprozeß parallel dem Verstandeserkennen vor sich geht, dann findet man draußen in der Natur das, was sich abspielt zwischen den Kräften in der Erde und dem, was in der Wurzel der Pflanze vor sich geht, und man findet den innerlichen Bezug zwischen dem, was konstituierend ist in der Wurzelbildung der Pflanze, mit dem, was kon- stituierend ist für das, was im menschlichen Haupte vor sich geht.",
        "In einer ähnlichen Weise wird man dann Beziehungen finden zwischen dem, was zum Beispiel im Krautartigen, Blattartigen der Pflanze vor sich geht, und dem, was im rhythmischen System des Menschen, drinnen in seinem Organischen, vor sich geht."
      ],
      [
        "Und man findet die Beziehun- gen zwischen den Funktionen im Blütenhaften und im Fruchtenden mit dem, was im menschlichen Stoffwechsel- system, im Sexualsystem und so weiter vor sich geht.",
        "Man kann von diesem Gesichtspunkte aus eine Überschau ge- winnen über das Pflanzenleben."
      ],
      [
        "Wenn man weiß, wie im menschlichen Organismus das, was ich den Mineralisierungsprozeß genannt habe, so wirkt, daß sich dieser Mineralisierungsprozeß innerlich vollzieht, im Gegensatz zu dem äußerlichen Mineralisie- rungsprozeß, der sich auch in dem oberen Bestände der Pflanze vollzieht, dann merkt man den Zusammenhang zwischen dem, was innerlich in der Hauptesorganisation vor sich geht, und dem, was im Wurzelbildungsprozeß vor sich geht, namentlich in dem, was als Mineralisieren- des im Wurzelbildungsprozeß auftritt.",
        "Man merkt dann auch, daß in einer gewissen Weise ein Gegensatz vor- liegt - trotz der Ähnlichkeit ein Gegensatz -, wie er sich etwa ausdrückt, wenn ich drei und drei habe, das eine positiv, das andere negativ."
      ],
      [
        "Dann habe ich zweimal drei, aber habe doch einen Gegensatz darinnen.",
        "So ist vorhan- den etwas, was in einer gewissen Beziehung gleich und doch gegensätzlich ist: in dem innerlichen Mineralisie- rungsprozeß des menschlichen Hauptes und in dem äuße- ren der Pflanzenwurzelbildung, und auch in dem äußeren Mineralisierungsprozeß des Erdenplaneten selber."
      ],
      [
        "Von hier aus findet man dann auf rationale Weise den thera- peutischen Bezug zwischen dem, was äußerlich ist und dem, was im Menschen innerlich ist.",
        "Und der Übergang kann gefunden werden über die Pathologie zur rationalen Therapie."
      ],
      [
        "Auf dieses letztere kann ich hier nur hinweisen.",
        "Denen, die es angeht, werden ja noch weitere Aufschlüsse gerade über dieses Kapitel gegeben werden, wie es auch schon in einem Frühlingskurs des vorigen Jahres für Ärzte und Medizinstudierende geschehen ist."
      ],
      [
        "Das wird aber das Be- deutsame sein, daß wirkliche Wissenschaftlichkeit - die zu gleicher Zeit nicht bloß Theorie, sondern Hinweis auf fruchtbares Handeln, auf die Tat ist aus der Geistes- wissenschaft heraus wird geboren werden können.",
        "Die Menschheit steht heute, insbesondere auf wissen- schaftlichem Gebiete, vor der Notwendigkeit, nicht einen kleinen, sondern einen großen Entschluß zu fassen: den Entschluß, in das organische Leben hineinzukommen da- durch, daß man nicht bloß den Inhalt der alten Denk- weise etwas modifiziert, sondern daß man in diese alte Denkweise selber ein neues Element hineinbringt, das Ele- ment übersinnlicher Erkenntnis."
      ],
      [
        "Was heute diesem Ent- schluß bei dem größeren Teil derer, die ihn fassen sollten, noch entgegensteht, das ist nicht irgendein Mangel der menschlichen Erkenntnisfähigkeit, das ist ein Mangel, ein begreiflicher Mangel, an Mut für diesen starken radikalen 116 Umschwung.",
        "Man möchte viel lieber leiden, als zu etwas Neuem vorschreiten."
      ],
      [
        "Man möchte beim alten bleiben und das Alte in kritischer oder in anderer Weise nur etwas umformen.",
        "Aber nicht eher wird Licht in das hineinkommen, was hier für unsere gegenwärtige Zivilisation auf dem Er- kenntnisgebiete vorliegt, als bis man den Mut faßt zum Vorschreiten von der Denkweise, die üblich ist, zu einer anderen Denkweise."
      ],
      [
        "So lange wird nichts Ersprießliches herauskommen, als man bei der Ausrede sich beruhigt, «man könne ja doch die imaginative Denkweise nicht er- reichen», was auch nicht wahr ist.",
        "Sondern erst dann wird ein Umschwung eintreten, wenn man einsehen wird: man darf nicht träge bleiben innerlich, wenn die Wissenschaft in ihrer Betrachtungsweise in fruchtbarer Art ihren Fort- gang nehmen soll."
      ],
      [
        "Man muß innerlich regsam und fleißig werden.",
        "Ein Willensentschluß, nicht bloß eine theoretische Erwägung ist hier notwendig.",
        "Und da zu Willensent- schlüssen - das weiß jeder Psychologe - die Menschheit schwerer zu bringen ist als zu theoretischen Erwägungen, bei denen man hübsch ruhig in seinem Inneren bleiben kann, so hat die moderne Menschheit gerade Gelegenheit, zu zeigen, wie sie aus der Not heraus zur Größe sich er- heben kann, indem sie sich entschließt, zunächst auf dem soeben genannten Gebiete, auf dem Erkenntnisgebiete, auf dem Geistgebiete den Mut zu einem großen Umschwung, nicht zu kleinen Erwägungen aufzubringen."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SPRACHWISSENSCHAFT Vierter Vortrag, Dornach, 7. April 1921",
    "paragraphs": [
      "Es ergibt sich mir heute wie etwas Selbstverständliches, daß sich dasjenige, wovon hier, von dieser Stelle aus, in diesen Tagen gesprochen worden ist, das Zusammenklin- gen des Subjektiven und Objektiven, daß sich das jetzt gewissermaßen auch ausgehend von einer Empfindung als Einleitung zu meinem Vortrage einstellt. Gestern vor- mittag schlössen hier die Betrachtungen mit der Rede des Professor Römer, die mir große Befriedigung gemacht hat - das ist das Subjektive - aus dem Grunde, weil aus ihr gesehen werden konnte, wie bei einem Fachmanne, der gründlich und voll in seinem Gebiete drinnensteht, das Bedürfnis entstehen kann, mit dem, was Geisteswissen- schaft vermag, hineinzuleuchten in solch ein einzelnes Fach.",
      "Es wird Ihnen auch aus dem, was Professor Römer heute schon aus seinem Fachgebiet anführen konnte, her- vorgegangen sein, daß vor allen Dingen für dieses In- einanderarbeiten starke, kräftige Arbeit auf seiten der einschlägigen Geisteswissenschaft selber entwickelt werden muß. Denn was bis jetzt gegeben werden konnte es soll das durchaus voll anerkannt werden , das sind zunächst einzelne Richtlinien, die der Verifizierung mit Bezug auf die äußere Wissenschaft bedürfen.",
      "In alledem, was durch diesen Vortrag zu einer gewissen subjektiven Befriedigung an mich herangetreten ist, war enthalten eine Betrachtung über die Zähne. Mit den Zäh- nen also ist gestern geschlossen worden - jetzt komme ich ins Objektive.",
      "Und gestatten Sie, daß ich heute wiederum 118 mit den Zähnen beginne, allerdings zunächst nicht mit etwas, was ich Ihnen von mir aus über die Zähne erzählen will, sondern mit einem Ausspruch, der aus der Gelehr- samkeit des 11. Jahrhunderts, wie sie damals in Mittel- europa war, hervorgegangen ist.",
      "Dieser Ausspruch heißt: Swenne diu zunge den wint fähet unt in in den munt ziuhet, an den zanen si scephet daz wort daz si sprichet. Das heißt also: So wie die Zunge den Wind aus ihrer Umgebung abfängt und ihn in den Mund zieht, so schöpft sie aus den Zähnen das Wort heraus, das sie spricht.",
      "Nun, das ist ein Produkt der Gelehrsamkeit Mittel- europas im 11. Jahrhundert. Die meint also, daß die Zunge aus den Zähnen das Wort hervorzieht wie aus der Außenwelt die Luft, die sie in den Mund hineinzieht.",
      "Jetzt eine Probe aus der Gelehrsamkeit des 19. Jahr- hunderts, letztes Drittel, ein Wort, welches der als mo- derner Abgott von einer zahlreichen Schülerschar verehrte Philologe Wilhelm Scherer ausgesprochen hat, und das Sie verzeichnet finden in seiner «Deutschen Sprachgeschichte», wo er auch dieses Wort, das ich Ihnen eben vorgelesen habe, heranzieht.",
      "Das Wort, das er diesem entgegensetzt, das ist dieses: «Über ein solches Wort lachen wir in der Gegenwart». Das ist das wissenschaftliche Bekenntnis aus dem 19. Jahrhundert über dieses Wort aus dem 11. Jahrhun- dert; es drückt die Wissenschaftsgesinnung aus, die im weitesten Umkreise auch heute noch waltet und von den Vertretern des entsprechenden Faches in weiteren Hinwei- sen wohl auch heute noch ausgesprochen wird. 119 Wenn man diesen ganzen Gegensatz zunächst ins Auge faßt von dem Gesichtspunkte aus, der hier öfter einge- nommen worden ist, daß ein völliger Umschwung statt- gefunden hat in bezug auf die Seelenverfassung der Men- schen seit dem ersten Drittel des 15.",
      "Jahrhunderts, dann haben wir in der Zeit, die zwischen dem erstzitierten Aus- spruch und dem Ausspruch Wilhelm Scherers liegt, unge- fähr gerade das enthalten, was an Zeit verflossen ist seit dem Hinunterdämmern jener Seelenverfassung, die bis zum Beginn des 15. Jahrhunderts vorhanden war, und der Richtung, die seither heraufgekommen ist und bisher eine gewisse Ausbildung erfahren hat.",
      "Wilhelm Scherer setzt nun die Sätze, die er damit be- gonnen hat, daß er über ein solches Wort aus dem 11. Jahrhundert lachen müsse, mit einer Betrachtung fort, die etwa folgendes enthält. Er sagt, alles Bestreben in der Gegenwart müsse mit Bezug auf die Sprachwissenschaft darauf gerichtet sein, dasjenige, was aus der physiologi- schen Organisation des Menschen heraus die Physiologen über das Sprechen, über das Wortebilden zu sagen haben, mit dem zusammenzubringen, was die Philologen über die Entwickelung der Sprache seit älteren Zeiten bis in unsere Gegenwart zu sagen haben.",
      "Mit anderen Worten: Physio- logie und Philologie müßten sich auf diesem Gebiete der Wissenschaft die Hände reichen. Und Wilhelm Scherer fügt hinzu, er müsse leider gestehen, daß die Philologen sehr, sehr weit zurückgeblieben seien, und daß von ihrer Seite noch nicht so bald zu hoffen sei, daß sie den Physio- logen in bezug auf das, was sie aus der physischen Or- ganisation heraus für die Gestaltung des Sprechens zu sagen haben, entgegenkommen werden.",
      "So daß also Phy- siologie und Philologie zwei Wissenschaftszweige sind, deren Sich-Nichtverstehen ein von seiner Zeitgenossen- 120 schaft als berufen angesehener Mann in scharfer Weise zugesteht. Damit ist hingedeutet auf ein Phänomen, das überhaupt in unserer Zeit ein tonangebendes ist: daß sich die einzel- nen Wissenschaften mit ihren Methoden durchaus nicht verstehen, daß sie nebeneinander reden, ohne daß der- jenige, der nun hineingestellt wird in diesen Wissenschafts- betrieb und das hört, was ihm auf der einen Seite die Physiologen und auf der anderen Seite die Philologen zu sagen haben, damit - verzeihen Sie den vielleicht etwas gewagten Vergleich - etwas anderes anzufangen weiß, als daß er von zwei Seiten in bezug auf seine Seele durch die Begriffsbildungen aufgespießt wird.",
      "In einem gewissen Sinne, obwohl ich auch damit nicht viel mehr sagen will als etwas Analogisches, liegt schon in der Wortbezeichnung, die, ich möchte sagen, unbewußt ernst genommen wird von den neueren Wissenschafts- strömungen, ein gewisser Gegensatz ausgedrückt. In der Wortbezeichnung «Physiologie» liegt ausgedrückt, daß sie sein will ein Logos über das Physische des Menschen, also gewissermaßen dasjenige, was logisch, intellektualistisch erfaßt das Physische; in dem Wort «Philologie» liegt: Liebe zur Weisheit, Liebe zum Logos, Liebe zum Worte; es ist also die Wortbezeichnung hergenommen von einem Gefühlserlebnis.",
      "Das eine Mal ist die Wortbezeichnung hergenommen von einem Verstandeserlebnis, das andere Mal von einem Gefühlserlebnis. Und was der Physiologe als eine Art intellektuellen Logos über die menschliche Physis erzeugen will, das - nämlich den Logos - will eigentlich der Philologe lieben.",
      "Wie gesagt, ich will damit zunächst nur analogisch auf etwas hinweisen, was aber dennoch, wenn es weiter verfolgt wird, wenn es nament- lich geschichtlich verfolgt wird, eine gewisse Bedeutung 121 hat; und ich rate dazu, die Sache geschichtlich genauer zu verfolgen. Aber wir können da noch auf etwas anderes hinweisen, welches uns aus der Vorgeschichte, aus der Vorläuferschaft desjenigen, was dann im Menschheitsbewußtsein seit dem Beginne des 15.",
      "Jahrhunderts aufgetreten ist, entgegen- tritt. Man weiß, daß das, was man Logik nennt und was doch in einer gewissen Beziehung in der Sprache sein Ab- bild hat, im wesentlichen wenigstens, eine Schöpfung des Aristoteles ist.",
      "Und wenn man sich darauf berufen wollte, daß selbstverständlich - so wie bei einem heutigen Men- schen, der nicht Logik studiert hat, doch die Logik in sei- ner Seelenbetätigung lebt auch vor Aristoteles die Logik in der Seelenbetätigung der Menschen gelebt habe, so übersieht man, daß die Umwandlung des Unbewußten in Bewußtes dennoch eine tiefere Bedeutung in dem Verlaufe des menschlichen Geschehens hat. Damit, daß das Logische ins Bewußtsein heraufgehoben worden ist, ist auch ein realer Vorgang, allerdings ein innerlich realer Vorgang, in in der menschheitlichen Seelenentwickelung gegeben: zwi- schen dem Begriff und dem Worte bestand in älteren Zei- ten eine innige Beziehung.",
      "Wie eine solche innige Bezie- hung zwischen dem Begriff oder der Vorstellung und der Wahrnehmung bestand, wie Sie das ausgeführt finden in meinen «Rätseln der Philosophie», ebenso bestand ein in- niger Bezug, ein, ich möchte sagen, Ineinandersein von Worten und Vorstellungen. Jene Trennung, die wir heute psychologisch vollziehen müssen zwischen dem Worte und dem Inhalte der Vorstel- lung - besonders bei Betrachtung des Mathematisierens tritt das mit aller Klarheit hervor -, ist in älteren Zeiten nicht gemacht worden.",
      "Und gerade auf diese Unterschei- dung kam zuerst Aristoteles. Er hob innerhalb des Seelen- 122 lebens dasjenige, was Vorstellung, Begriff ist, aus dem Gewebe der Sprache heraus, machte es für die Erkenntnis zu etwas abgesondert Vorliegendem.",
      "Dadurch aber drängte er wiederum dasjenige, was in der Sprache lebt, weiter in das Unbewußte hinunter, als es vorher war. Es wurde gewissermaßen ein Abgrund für die Erkenntnis geschaffen zwischen dem Begriff oder der Vorstellung und dem Worte.",
      "Je weiter wir nämlich zurückgehen in der Betrachtung der menschlichen Sprache, desto mehr finden wir, daß in der Auffassung des Menschen Wort und Begriff oder Vor- stellung als eines erlebt werden, daß der Mensch gewisser- maßen das, was er denkt, innerlich hört, daß er ein Wort- bild, nicht so sehr ein Gedankenbild hat. Der Gedanke wird draußen an die Sinneswahrnehmungen und drinnen an das Wort geknüpft.",
      "Dadurch aber war auch für diese älteren Zeiten eine gewisse Empfindung vorhanden, die sich etwa so charakterisieren läßt: Indem die Menschen sich in ihren Worten aussprachen, fühlten sie, als ob das, was in ihren Worten widerklingt, unmittelbar auf eine im Instinktiven verborgene, unterbewußte Art von den Dingen in ihre Sprache hineingelangt wäre. Sie fühlten gewissermaßen, daß ein realer Vorgang sich abspielt zwi- schen dem, was in den Dingen und namentlich in den Tat- sachen lebt, und dem, was innerlich den Impuls zum Er- klingen des Wortes bildet.",
      "Sie fühlten einen solchen realen Zusammenhang, wie der Mensch heute noch einen realen Zusammenhang zwischen den Stoffen fühlt, die draußen sind, sagen wir Ei, Kalbfleisch, Salat, und dem, was dann in seinem Inneren mit dem Inhalte dieser Stoffe sich ab- spielt, wenn er verdaut. Er wird in diesem Vorgang, der sich abspielt vom Draußensein der Stoffe zu dem, was drinnen in der Verdauung geschieht, einen realen Vorgang sehen.",
      "Diesen realen Vorgang erlebt er unterbewußt. So 123 unterbewußt wenn auch viel deutlicher, von einem ge- wissen dämmerigen Bewußtsein schon durchzogen - war dasjenige, was man an der Sprache erlebte. Man hatte die Empfindung, daß etwas, was in den Dingen lebt, mit den Lauten, mit den Worten verwandt ist.",
      "Wie die Substanzen der Stoffe, die man ißt, mit dem, was innerlich im Men- schen im Stoffwechsel geschieht, zusammenhängen, so empfand man einen inneren Zusammenhang zwischen dem, was in den Dingen und Tatsachen vorgeht, was wortähnlich ist, und dem, was innerlich als Wort erklingt. Und indem Aristoteles das, was man da als einen realen Vorgang empfand, ins Bewußtsein heraufhob, wo die Be- griffe spielen, war für die Sprache dasselbe geleistet, was ein Mensch leistet, der darüber nachdenkt, was die Sub- stanzen der Stoffe in seinem Organismus anfangen.",
      "Etwas weiter voneinander entfernt ist allerdings das Denken über die Verdauung von dem realen Verdauungsvorgange selbst als das Denken von der Sprache. Aber eine Vorstel- lung von dem entsprechenden Verhältnis kann man ge- winnen, wenn man sich diese Vorstellung dadurch ver- deutlicht, daß man von einem Naheliegenderen zu einem Entfernteren und in der Entfernung Deutlicherwerdenden übergeht.",
      "Nun, für uns liegt ja, wenn wir an die Stelle der heuti- gen abstrakten Geschichtsbetrachtung eine mehr konkrete setzen, dieses vor, daß Dinge, die sich in Griechenland in der vorchristlichen Zeit, auch in der voraristotelischen Zeit abgespielt haben, für die mitteleuropäische Bevölkerung - die die Griechen durchaus noch als barbarisch, das heißt auf einer niedrigeren Kulturstufe empfunden haben - sich später abspielten. Und wir werden das Richtige treffen, und Geisteswissenschaft gibt dazu die Anleitung, dieses Gefühl richtig zur Gewißheit zu erheben, wenn wir uns 124 vorstellen, daß die Geistesverfassung, aus der gesprochen wird, gefühlsmäßig gesprochen wird, «die Zunge ziehet die äußere Luft in den Mund, so wie sie aus den Zähnen ziehet das Wort», daß diese Anschauungsweise, diese merkwürdig bildhaft sich aussprechende Anschauungs- weise ungefähr diejenige auch war, die in der voraristote- lischen Zeit auch geherrscht hat innerhalb Griechenlands, und an deren Stelle das getreten ist, was eben treten mußte durch die Abtrennung der Logik, des Logos, durch die Abtrennung des Gedankenhaften von dem, was in der Sprache zur Darstellung kommt.",
      "Sie wissen ja, daß in jener Gelehrsamkeit, welche sich zunächst entwickelt hat seit dem 15. Jahrhundert und aus welcher die verschiedenen Zweige der einzelnen Fachwis- senschaften hervorgegangen sind, daß in dieser Gelehr- samkeit als Bildung viel mitgewirkt hat, was sich als spätgriechische Kultur geltend gemacht hat.",
      "Gerade die Philologen, diejenigen also, die den Logos lieben sollen, sie wurden durchaus beeinflußt von dem, was aus der spätgriechischen Kultur hervorgegangen ist. Und man denke sich nur einmal einen solchen Spätgriechling als germanistischen Forscher, wie Wilhelm Scherer, der Früh- griechik gegenübergestellt, und die sagt ihm: Die Zunge ziehet die Sprache aus den Zähnen -, dann weist er das selbstverständlich zurück, dann will er von seinem Ge- sichtspunkte aus davon nichts wissen.",
      "Man muß solche Tatsachen schon einmal in einem Lichte betrachten, das etwas tiefer in die historischen Zusammenhänge hinunter- zuleuchten bemüht ist als dasjenige, was in der gewöhn- lichen landläufigen Geschichtswissenschaft heute vielfach vorhanden ist, sowohl auf dem Gebiete der äußeren poli- tischen oder Kulturgeschichte wie auch auf dem Gebiete der Sprachgeschichte. 125 Nun handelt es sich darum, welche Wege gesucht wer- den müssen, um in das Gefüge des Sprachorganismus - wenn ich mich so ausdrücken darf - selber wissenschaft- lich hineinzukommen. Schon in Äußerlichkeiten drückt sich aus, wie diejenige Betrachtungsweise, die die Seele allmählich heraufgehoben hat ins Gebiet der abstrakten Begriffe, sich entfernt hat von dem, was in der voraristotelischen Zeit über die Sprache empfunden worden ist.",
      "Was hat zum Beispiel hervorgebracht, als Meinung über die Entstehung der Sprache, diese in dem Zeichen des Aristotelismus stehende Forschung? Nun, sie wurde dadurch, daß sie die Seele heraufhob in das Abstrakte, dem unmittelbaren Zusam- menhang mit der Außenwelt entfremdet, durch den man erleben konnte, was real in den Dingen dem gebildeten Worte entspricht.",
      "Sie wurde dem entfremdet, suchte aber doch, wie ein solcher Zusammenhang aussehen kann, und sie übersetzte sich diesen Zusammenhang nun auch in allerlei Abstraktionen. Was im Inneren gefühlt worden ist, das versetzte sie in das Gebiet, wo man äußerlich, nach den Sinnes- oder sonstigen äußeren Beobachtungen sich Begriffe formt.",
      "Weil es unmöglich war, unterzutauchen in die Dinge, um den Vorgang zu suchen, wie das Wort aus den Dingen heraus in die menschliche Organisation wirkt, setzte man an die Stelle einer solchen Erfassung einen abstrakten Begriff, zum Beispiel in der sogenannten Wau- wau-Theorie oder in der Bimbam-Theorie. Die Wau- wau-Theorie besagt zum Schlüsse nichts anderes, als daß dasjenige, was äußerlich im Organischen als Ton, Laut zutage tritt, nachgeahmt wird.",
      "Es ist eine vollständig äußerliche Betrachtung eines äußerlichen Tatbestandes mit Hilfe von abstrakten Begriffen. Die Bimbam-Theorie unterscheidet sich von der Wauwau-Theorie nur dadurch, 126 daß bei ihr Rücksicht genommen wird auf das Unorgani- sche, wie es gewissermaßen den Ton aus sich entbindet.",
      "Dieser Ton wird dann wiederum auf eine äußerliche Weise von dem Menschen, der der äußeren Natur gegenüber- steht und sich von ihr beeinflussen läßt, nachgeahmt. Und die Umbildung desjenigen also, was - allerdings nicht überall, sondern nur auf einem engbegrenzten Erden- gebiete die Kinder rufen, wenn sie den Hund bellen hören: wau-wau, oder desjenigen, was ihnen in das Sprachgefühl hineinkommt, wenn sie die Glocke ertönen hören: bim-bam-bum, diese Umbildung wird dann durch eine merkwürdige Methode verfolgt.",
      "So sieht man das, was dann zum Organismus der Sprache sich gebildet hat, in den angedeuteten Theorien an, die ja durch nicht viel bessere bis heute ersetzt sind. Wir haben es also zu tun mit einem Innerlichwerden der Betrachtung über die Sprache.",
      "Vor allen Dingen ist anzustreben durch Geisteswissenschaft, wie sie hier ge- meint ist, daß die Sprachbetrachtung wiederum eine inner- liche werde, daß durch das, was erreicht werden kann im Aufsteigen von der sinnlichen zur übersinnlichen Erkennt- nis, dasjenige, allerdings jetzt in einer der vorgerückten Menschheit entsprechenden Gestalt, selbständig wieder- um gefunden werden könne, was einstmals gefühls- und instinktmäßig über die Sprache gedacht worden ist. Und da muß ich - ich kann wegen der Kürze der Zeit nur auf die Richtungen hinweisen, in denen die empirischen Tat- sachen zu verfolgen sind darauf aufmerksam machen, wie Geisteswissenschaft einen streng konkreten Weg ein- schlägt, wenn sie verstehen will, wie der Mensch sich von seiner Kindheit bis zu einem gewissen Lebensalter ent- wickelt.",
      "Sie finden das, was ich hier einigermaßen andeu- ten möchte, dargestellt zum Beispiel in meinem Büchelchen 127 «Die Erziehung des Kindes vom Gesichtspunkte der Gei- steswissenschaft» . Da muß zunächst darauf hingewiesen werden, wie die ganze seelisch-körperliche Konfiguration des Menschen in der Zeit vor dem Zahnwechsel eine wesentlich andere ist, als sie nach dem Zahnwechsel wird.",
      "Wer sich Beobachtun- gen für diese Tatsache angeeignet hat, der weiß, wieviel im seelisch-leiblichen Leben metamorphosiert wird in der Zeit, in der an die Stelle der ersten Zähne die zweiten treten. Und wer nicht durch Abstraktionen wie etwa die Anhänger des psychophysischen Parallelismus die Bezie- hungen von Leib, Seele und Geist sucht, sondern wer sie sucht in konkreten Erscheinungen, wer sie sucht nach einer wirklichen weitergebildeten naturwissenschaftlichen Me- thode, wer die innere Struktur des Seelenlebens im Kon- kreten erfassen kann, der wird eben finden, wie das, was später mehr seelisch in der eigentümlichen Konfiguration des Begriffslebens, in der Durchsetzung desjenigen, was begrifflich erfahren wird, mit Willensimpulsen, die dann zu der Bildung des Urteiles führen, wie das etwas ist, das bis zum Zahnwechsel in der physischen Organisation ge- wirkt hat.",
      "Und er wird nicht darüber spekulieren, was von der Geburt bis zum Zahnwechsel in der physischen Organisation «seelisch wirken» kann. Sondern er wird sich sagen, was dann im Zahnwechsel frei wird, frei wird aus einem Körper, in dem es vorher latent war, das hat vorher latent und gebunden in der physischen Organisa- tion des Menschen gewirkt.",
      "Und diese besondere Art der physischen Organisation, in der das später seelisch zu Be- obachtende wirkt, findet mit dem Herausstoßen der zwei- ten Zähne, auf das Sie auch gestern aufmerksam gemacht worden sind, seinen Abschluß. Nun muß man die Tatsachen, die hier vorliegen, nicht 128 einseitig physiologisch, sondern so betrachten, daß man, wie der Physiologe mit seinen Sinnen und dem an sie gebundenen Verstand in die physischen Vorgänge des menschlichen Organismus, ebenso mit dem, was Imagina- tion und Inspiration ist, in die seelischen Vorgänge ein- dringt, so daß man sie wirklich erkennt, nicht bloß, wie es die heutige Psychologie macht, mit Worten belegt.",
      "Wenn man wirklich in diese Vorgänge eindringt, dann muß man in dem Realen, das zuerst von der Geburt bis zum Zahn- wechsel latent ist, das dann frei wird, auch vorstellungs- gemäß, erkenntnisgemäß ein Reales schauen. Deshalb spricht meine Schrift über «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft», indem sie diesen Vorgang formelhaft zusammenfaßt, davon, daß mit dem Zahnwechsel der Ätherleib des Menschen, der vorher im physischen Leib gewirkt hat, erst frei zur Betätigung im Seelenleben geboren werde.",
      "Dieses «Geborenwerden des Ätherleibes» drückt sich aus im Zahnwechsel. Es ist notwendig, daß man gewissermaßen am Aus- gangspunkte anthroposophisch-geisteswissenschaftlicher Be- trachtung solches Formelhafte habe, wie zum Beispiel «Geburt des Ätherleibes aus dem physischen Leibe», was ja einem tatsächlichen Geschehen entspricht.",
      "Aber dann, wenn der Übergang gesucht werden soll von dieser Gei- steswissenschaft im engeren Sinne - die sich namentlich an die Betrachtung des menschlichen unmittelbaren Tages- erlebens hält zu der Betrachtungsweise in einzelnen Fachwissenschaften, dann wird dasjenige, was in solch formelhafter Weise zunächst ausgesprochen wird, etwas Ähnliches wie die Formel der Mathematik: es wird Me- thode, Methode für die Behandlung der Tatsachen. Und deshalb kann diese Geisteswissenschaft befruchtend auf die einzelnen Wissenschaften wirken, ohne daß immer 129 bloß dasjenige in die einzelnen Wissenschaften hinein fort- gesetzt wird, was allerdings beim Ausgangspunkte klar ins Auge gefaßt werden muß: daß der Mensch gegliedert ist in physischen Leib, Ätherleib und so weiter.",
      "So etwas kann man im Anfange durchaus wissen, und muß es wissen; es muß aber, wenn die Befruchtung durch Geistes- wissenschaft eintreten soll, Tun werden, es muß Methode werden, Art und Weise der Behandlung auch der sinnlich empirisch gegebenen Tatsachen. Und in dieser Beziehung wird Geisteswissenschaft, weil sie, aufsteigend vom Un- organischen, wo sie noch wenig tun kann, durch das Orga- nische heraufkommt in das geistige Gebiet, ich möchte sagen, nicht nur in dem Wie die einzelnen Wissenschaf- ten befruchten können, sondern sie wird ihnen gerade- zu aus ihrem Befunde heraus Tatsachenbestätigungen zu übergeben haben, welche Licht verbreiten über dasjenige, was von der anderen Seite durch sinnlich-physische Be- obachtung gewonnen und dann mit dem Verstande durch- schaut wird.",
      "Es müssen sich begegnen geistige und sinnlich- physische Forschung. Und es ist eine der wichtigsten Auf- gaben für die Zukunft, daß sich diese geistige Forschung und diese sinnlich-physische Forschung begegnen.",
      "Im Vorgang, der sich an dem Zahnwechsel besonders äußerlich offenbart, zeigt sich, daß dasjenige, was man - indem man aber eine konkrete Anschauung, nicht einen Wortbegriff ins Seelenauge faßt - als Ätherleib bezeich- net, für den ganzen menschlichen Organismus frei tätig wird, nachdem es vorher organisierend im physischen Leibe gewirkt hatte. Jetzt steigt es herauf ins Seelische, wird frei und wirkt dann in gewissem Grade bewußt auf den gan- zen Menschen zurück.",
      "Ein Ähnliches tritt wiederum ein mit dem, was äußer- lich sich offenbart als die Geschlechtsreife. Da sehen wir, 130 wie wiederum im menschlichen Erleben etwas dasteht, was sich ausdrückt auf der einen Seite in einem gewissen Meta- morphosieren des physischen Organismus, auf der anderen Seite in einem Metamorphosieren des Geistigen.",
      "Und ein Wesentliches beim Geistesforscher besteht ja darin, daß er sich ein ebensolches konkretes Anschauen für das an- eignet, was so im Geistig-Seelischen auftritt, wie sich der- jenige, der sich nur an der äußeren Anschauung bilden will, ein konkretes Anschauen aneignet für das, was er mit Augen sehen und mit dem Verstande kombinieren kann. Seelisches läßt sich nicht in dieser Weise anschauen, son- dern läßt sich in seiner Wirklichkeit nur imaginativ an- schauen.",
      "Es gibt keine wahre Psychologie, die nicht mit imaginativem Anschauen beginnt, und es gibt keine Mög- lichkeit, das Wechselverhältnis von Leib und Seele oder Körperleib und Geistseele zu finden, als die Brücke zu schlagen zwischen dem, was der äußeren physisch-sinn- lichen Anschauung gegeben ist als das Körperlich-Leibliche, und dem, was herausfällt aus dieser Anschauung, was nur im Aufsteigen zur übersinnlichen Erkenntnis gegeben sein kann als Wirklichkeit, dem Geistig-Seelischen. Wenn man nun dasjenige wiederum betrachtet, was im Stadium der Geschlechtsreife eintritt, dann wird man sich sagen müssen: Da sehen wir in gewissem Sinne den umge- kehrten Vorgang von dem, der beim Zahnwechsel sich ab- gespielt hat.",
      "Wir sehen, wie das, was als Begehrungsver- mögen im Menschen spielt, was der instinktive Charakter seines Willens ist, den Organismus in einer Weise ergreift, wie es ihn früher nicht ergriffen hat. Indem man wieder- um den ganzen breiten Tatsachenkomplex, der damit ins Auge gefaßt wird, formelhaft zusammenfaßt, kommt es dazu, daß man sagt: dasjenige, in dem namentlich die Begierdenatur schlummert, der astralische Leib des Men- 131 sehen wird frei, wenn die Geschlechtsreife eintritt.",
      "Er ist es, der sich nun wenn ich mich so ausdrücken darf als frei in den physischen Organismus hineinsenkt, diesen er- greift, durchsetzt und so die Begierde körperhaft macht, was in dem Geschlechtsreifwerden seinen Ausdruck findet. Nun, was ergibt aber die sachgemäße Vergleichung dieser beiden Vorgänge?",
      "Wir sehen gewissermaßen, wenn der Zahnwechsel eintritt, ein Freiwerden des ätherischen Leibes des Menschen. Wie drückt sich das, was da ge- schieht, eigentlich aus? Es drückt sich so aus, daß der Mensch dadurch fähig wird, die Begriffsbildung, über- haupt das Bewegen im Vorstellungsleben, das früher mehr an seinen ganzen Organismus gebunden war, gebunden an die Kopforganisation weiter auszuführen.",
      "Gewissermaßen sehen wir - und Geisteswissenschaft sieht es nicht nur ge- wissermaßen, sondern in seiner Wirklichkeit -, daß das Ätherische, was wir dem Menschen als Ätherleib zuschrei- ben, sich mit dem Zahnwechsel zurückzieht auf dasjenige, was nur noch im Rhythmischen des menschlichen Organis- mus und im Stoffwechsel-Gliedmaßenorganismus lebt, und daß es an der Ausgestaltung des Hauptes, an der plasti- schen Gestaltung des Hauptes eine freie Tätigkeit ent- wickelt, an der das Bewußtseinsleben des Menschen im Vorstellen teilnimmt. Es wird gewissermaßen die Kopf- organisation in dieser Zeit freigelegt.",
      "Und wenn ich mich bildhaft ausdrücken darf über eine Wirklichkeit, die durchaus besteht, so muß ich sagen, was in den zweiten Zähnen aus der ganzen Organisation des Menschen sich an die Oberfläche treibt, das ist dasjenige seelisch-geistige Wirken, das vorher die ganze Körperorganisation durch- zieht und dann frei wird. Vorher durchzog es den ganzen Menschen bis in das Haupt hinein.",
      "Es zieht sich allmählich vom Haupte zurück; und es zeigt, wie es sich zurückzieht, 132 indem es sein Nicht-mehr-bis-zum-Haupte-Wirken da- durch offenbart, daß es haltmacht und die zweiten Zähne hervorbringt. Sie können sich das geradezu schematisch zur Anschauung bringen.",
      "Wenn ich das, was menschliche physische Organisation ist, mit der weißen Kreide schema- tisch andeute, und das, was ätherische Organisation ist, mit der roten Kreide, dann würde sich folgendes schema- tisch ergeben (siehe Abbildung): Sie sehen in der linksstehenden Figur den Menschen in seiner geistig-seelisch-leiblichen Wirksamkeit, wie er bis zum Zahnwechsel vor Ihnen steht. Sie sehen in der zwei- ten Figur, die rechts von Ihnen ist, wie sich zurückge- zogen hat das Ätherische in seiner unmittelbaren Wirk- samkeit von der Kopforganisation, wie es frei geworden ist in einer gewissen Beziehung, so daß es von da aus frei auf den menschlichen Kopforganismus wirkt.",
      "Und was als letztes geschieht aus diesem Wirken des Seeelisch-Geistigen in dem physischen Organismus, das ist das Heraustreiben der zweiten Zähne. Sie können, was Ihnen hier als geistige Anschauung mitgeteilt wird, ich möchte sagen, in seinem Abbilde beobachten, wenn Sie die Schädel, die Ihnen gestern Herr Professor Römer gezeigt hat, nehmen, indem 133 Sie vergleichen können den Ansatz der ersten Zähne mit dem Ansatz der zweiten Zähne.",
      "Wenn Sie das sinngemäß verfolgen wollen, dann müssen Sie zugrunde legen, was hier aus der Geisteswissenschaft gewonnen ist. Dann müs- sen Sie sich sagen, die ersten Zähne, mit alledem was sich in ihnen ausspricht, sind aus der ganzen menschlichen Organisation, einschließlich der Kopforganisation, heraus- geholt.",
      "Was sich in den zweiten Zähnen ausspricht, ist her- ausgeholt, nachdem sich langsam die innere seelische Or- ganisation, insofern sie den Ätherleib betrifft, in den rhythmischen und Stoffwechselorganismus zurückgezogen hat und für die Hauptesorganisation frei geworden ist. In einer ähnlichen Weise können wir uns sagen - wie ge- sagt, ich kann nur Richtlinien anführen , daß etwas vor- geht mit der Geschlechtsreife.",
      "Da wird dasjenige, was wir astralischen Leib formelhaft nennen, hineinversenkt in den physischen Leib, so daß es ihn schließlich ergreift und eben das bewirkt, was die Geschlechtsreife ausmacht. Nun aber geschieht, was sich am Menschen ereignet, in den mannigfaltigsten Metamorphosen.",
      "Wer einmal einen solchen Vorgang wirklich verstanden hat wie den, der sich mit der Geschlechtsreife ausdrückt, der ein gewisses neues Verhältnis in der menschlichen Entwickelung, in der Ent- wickelung des Menschen zur Außenwelt bewirkt, wer einen solchen Vorgang wirklich innerlich versteht, der er- kennt ihn dann auch, wenn er in einer gewissen Meta- morphose auftritt. Was mit der Geschlechtsreife auftritt, indem es den ganzen Menschen ergreift, indem es gewisser- maßen ein Verhältnis herausbildet des ganzen Menschen zu seiner Umgebung, das wird, ich möchte sagen, in einer anderen Metamorphose vorausgenommen in dem Augen- blicke, wo sich die Sprache in dem Kinde entwickelt.",
      "Nur findet das, was eben mit der Geschlechtsreife stattfindet, beim Kinde in der Sprachbildung in einer anderen Meta- morphose statt. Da spielt sich das, was mit der Ge- schlechtsreife den ganzen Menschen ergreift und sich hin- einergießt in sein Verhältnis zur Außenwelt, zwischen dem rhythmischen und Gliedmaßenmenschen und der Kopf- organisation des Menschen ab.",
      "Gewissermaßen dieselben Kräfte, die beim Geschlechtsreifwerden den ganzen Men- schen ergreifen und dirigierend wirken auf sein Verhältnis zur Außenwelt, machen sich geltend zwischen dem unteren und oberen Menschen. Und indem der untere Mensch lernt den oberen so empfinden, wie sonst der Mensch im spä- teren Alter die Außenwelt empfinden lernt, lernt er spre- chen.",
      "Ein Vorgang, den man äußerlich am Menschen beobachten kann in einem späteren Lebensalter, den muß man in der Lage sein zu verfolgen in seiner Metamorphose bis dahin, wo er als eine innerlich im menschlichen Orga- nismus sich abspielende Metamorphose, im Sprechenlernen eben, erscheint: der Vorgang, der sonst beim ganzen Men- schen in der Geschlechtsreife auftritt. Und hat man diese Sache erfaßt, dann tritt einem die Möglichkeit entgegen, zu begreifen, wie das Zusammen- spielen des unteren Menschen des rhythmischen und des Gliedmaßenmenschen - in seiner Wechselwirkung ein innerliches Erleben von etwas ausbildet, was auch äußer- lich vorhanden ist in der uns umgebenden Natur.",
      "Dieses Erleben auf innerliche Art desjenigen, was äußerlich vor- handen ist, führt dazu, daß das, was äußerlich stumm in den Dingen als deren eigene Sprache bleibt, anfängt zu klingen als die Menschensprache im menschlichen Inneren. Bitte, gehen Sie meinetwillen von diesem Satze wie von einem regulativen Prinzipe aus.",
      "Gehen Sie aus von diesem Satze, daß dasjenige, was in den Dingen, indem sie äußer- lich werden, materiell werden, verstummt, daß das in der Entmaterialisierung innerlich im Menschen hörbar wird und zum Sprechen kommt. Dann werden Sie den Weg fin- den, auf dem Sie nicht eine Wauwau- oder Bimbam- Theorie ausbilden, sondern auf dem Sie dasjenige, was äußerlich an den Dingen ist - und da eben für die äußere Beobachtung nicht wahrgenommen werden kann, weil es ja verstummt und nur noch auf übersinnliche Art vorhan- den ist -, aufgehen sehen als Sprache in des Menschen Inneren.",
      "Was ich damit ausspreche, ist, wie wenn man eine Linie hinzeichnet und damit eine Richtung angibt, in der man eigentlich am liebsten ein weit ausgesponnenes Gemälde malen möchte. Ich kann nur diesen mehr abstrakten Satz über die Beziehung der Dinge und Tatsachen der Außen- welt zur Entstehung der menschlichen Sprache im Inneren vor Sie hinstellen.",
      "Und sie werden alles, was Sie über die Sprache spüren können, in ein neues Licht gerückt sehen, wenn Sie den Weg finden von diesem abstrakt angenom- menen Satze, der zunächst formelhaft klingt, bis zu dem- jenigen, was Ihnen die Tatsachen sinngemäß verbindet. Und wenn Sie dann das, was auf diese Art philologisch gewonnen wird, an die Physiologie heranbringen wollen, dann werden Sie sich belehren lassen können über den Zu- sammenhang der äußeren Geschlechtsmetamorphose mit der Sprachmetamorphose, in dem Sie Tatsachen studieren, die vorliegen als ein noch zurückgebliebener Rest: als der sprachliche Rest der Geschlechtsreife-Metamorphose in dem Verändern der Stimme, das heißt des Kehlkopfes beim Knaben, und in manchen anderen Erscheinungen, die beim Weibe auftreten.",
      "Wenn Sie nur den Willen haben, einzu- gehen auf die Tatsachen und die Fäden ziehen von einer Tatsachenreihe zur anderen, sich nicht einkapseln in un- fruchtbare Spezialwissenschaften, sondern dasjenige wirk- 136 lich beleuchten wollen, was in der einen Wissenschaft vor- handen ist als Tatsache, durch die Tatsachen, die durch andere Wissenschaften zutage treten, dann werden die ein- zelnen Spezialwissenschaften das werden können, was der Mensch in ihnen suchen muß, wenn er eben weiterkom- men will auf der Bahn seines Erkennens sowohl wie auf der Bahn seines Wollens. Es wird sich uns morgen in einem Zusammenhang, der, wie es scheinen könnte, gar nicht hineingehört, sehr natur- gemäß ergeben, wie wir nun von dem Zahnwechsel zur Spracherscheinung und dann weiter zurückgehen können zu dem, was das dritte ist auf dieser rückläufigen Bahn: Wir sehen gewissermaßen in dem, was sich im Zahnwech- sel ausdrückt, eine Wechselwirkung zwischen physischem Leib und Ätherleib.",
      "Wir sehen wiederum in dem, was sich in der Sprache ausdrückt, eine Wechselwirkung zwischen astralischem Leib und Ätherleib. Und wir müssen suchen als drittes ein Wechselverhältnis zwischen dem Ich und dem, was im Menschen als astralischer Leib lebt, und wer- den da geführt werden auf dasjenige, was das dritte ist in dieser rückläufigen Betrachtung: auf die Einkörperung des Geistig-Seelischen, auf dasjenige, was in dem Geistig- Seelischen geboren wird.",
      "Sucht man den Weg vom Zahn- wechsel durch das Sprachentstehen, so ist die dritte Etappe die Etappe des Vereinens des präexistierenden mensch- lichen Geistig-Seelischen mit dem Leiblichen. Indem Aristoteles den Ausweg von der Betrachtung des Zahnwechsels zu der Betrachtung der Sprache durch seine Abstraktion vermauert hat, war er genötigt, zu dem Dogma seine Zuflucht zu nehmen, daß mit jedem neuen Menschenwesen ein neues Geistig-Seelisches geboren werde.",
      "Aus einem Mangel an Wille zum Weitergehen eines Er- kenntnisweges ist die Erkenntnis von der menschlichen 137 Präexistenz abhandengekommen und damit von alledem, was in wahrer Weise zur Erkenntnis der menschlichen Seele führt. Wir sehen einen geschichtlichen Zusammenhang, der sich aber auslebt in der Behandlung gewisser Probleme, und wir können zum Schlüsse sagen: Es stehen sich heute, nach dem Ausspruche eines im gegenwärtigen Sinne ganz be- deutenden Philologen, Philologie und Physiologie so ge- genüber, daß sie sich nicht verstehen können.",
      "Warum dieses? Weil Physiologie den Körper des Menschen stu- diert und bei diesem Studium nicht rückläufig zum Geiste kommt. Verfolgt man eine wahre Physiologie, dann fin- det man über das Körperliche der physiologischen Be- trachtung wiederum das Geistig-Seelische im Menschen.",
      "Wie nun, wenn man eine wahre Philologie verfolgt? Wenn man eine wahre Philologie verfolgt, so wird einem nicht der Logos ein Abstraktum, für das man dann sucht Nachbilder zu durchschauen, Nachbilder in naturwissen- schaftlicher Methode, sondern man sucht einzudringen in dasjenige, was man als «Philo»-loge angeblich liebt, durch imaginative und sonstige Betrachtung.",
      "Dann aber, wenn man in das eindringt, was für die heutige Philologie ein Schattenhaftes, Nebuloses geworden ist, nämlich den Sprachgenius, den schöpferischen Sprachgenius, wenn man in ihn eindringt, dann dringt man durch den Geist zu der äußeren Körperlichkeit. Physiologie findet auf dem Wege durch die innere Physis den Geist.",
      "Philologie, richtig betrachtet, findet auf dem Weg nach außen durch den Sprachgenius das in den Dingen, was aus den Dingen selber spricht und verstummt ist. Sie findet nicht Wauwau und Bimbam, sondern sie findet in den körperlich uns umgebenden Dingen die Ver- anlassung dazu, daß Worte, daß die Sprache in uns ent- 138 stehen.",
      "Die Physiologie hat den Weg verloren zu ihrem Ziel, indem sie beim Körper stehenbleibt und nicht durch den Körper zum Geist innerlich vordringt. Die Philologie hat den Weg verloren, weil sie beim Sprachgenius, den sie dann nur abstrakt faßt, stehenbleibt und nicht vordringt in das Innere der äußeren Dinge, aus denen das erklingt, was im Worte lebt.",
      "Wenn Philologie nicht so reden wird, als ob das Wauwau und Bimbam in äußerlich abstrakter Weise nachgemacht werde durch den Menschen, sondern so reden wird über die äußerliche Körperlichkeit, daß ihr klar werden wird in Imaginationen, wie aus dieser äußer- lichen Körperlichkeit das Wort entspringt, das im Inneren echohaft widertönt, wenn also Physiologie den Geist, Philologie die Körperlichkeit gefunden haben wird, dann werden sie sich finden. Damit habe ich den Weg, den in gewissenhafter Arbeit die Geisteswissenschaft im anthroposophischen Sinne lei- ten will, fadengezogen.",
      "Ich habe nur einige Andeutungen auf diesem besonderen Gebiete der einleitenden Sprach- wissenschaft gegeben. Nun, diese Dinge werden unter uns besprochen, diese Dinge werden von uns erstrebt. Während diese Dinge von uns erstrebt werden, daß sie Zeugen sein können für das- jenige, was auf einem Erkenntniswege ganz aus dem Geiste unserer Zeit heraus erstrebt wird, und während Sie sehen können aus dem, was erstrebt wird, wahrscheinlich doch einen gewissen Ernst, der sich messen kann mit dem Ernste, der in anderen Gebieten des Lebens besteht, tobte gestern in Stuttgart eine Versammlung, die unsere Redner zum großen Teile niedertrampelte, die gar nicht den Wil- len hatte, auf irgend etwas hinzuhören, die nicht eingehen wollte auf dasjenige, was wir zu sagen haben, sondern die durch Getrampel und ähnliche Dinge dasjenige niederzu- 139 ringen bestrebt war, was in ernster Weise angestrebt wird.",
      "Und, indem ich mich an die Kommilitonen wende, so darf ich sagen: am gestrigen Abend fehlten in Stuttgart Ihre Kollegen nicht von der anderen Fakultät, sondern von der anderen Gesinnung -, die fehlten da nicht, die waren bei dem Niedertrampeln wohl vorhanden. Meine sehr verehrten Anwesenden, meine lieben Kom- militonen!",
      "Es wird immer deutlicher und deutlicher wer- den, wie von einer gewissen Seite her dasjenige, das man nicht widerlegen kann, weil man es nicht widerlegen will, weil man sich durch träges Fortsetzen eines Alten, das sich überlebt hat, überhaupt auf das Neue nicht einlassen will, daß man das durch äußere Gewalt wird niedertram- peln wollen. Nun, ich möchte nur an Sie hier appellieren in der Weise, daß ich allerdings zu Ihnen den Glauben habe, daß Sie sich vielleicht in Ihrem Inneren sagen: Bei dieser Prozedur des Niedertrampeins haben wir auch noch ein Wort mitzureden!",
      "Möge aber dieses Wort zur Tat werden. 140"
    ],
    "sentences": [
      [
        "Es ergibt sich mir heute wie etwas Selbstverständliches, daß sich dasjenige, wovon hier, von dieser Stelle aus, in diesen Tagen gesprochen worden ist, das Zusammenklin- gen des Subjektiven und Objektiven, daß sich das jetzt gewissermaßen auch ausgehend von einer Empfindung als Einleitung zu meinem Vortrage einstellt.",
        "Gestern vor- mittag schlössen hier die Betrachtungen mit der Rede des Professor Römer, die mir große Befriedigung gemacht hat - das ist das Subjektive - aus dem Grunde, weil aus ihr gesehen werden konnte, wie bei einem Fachmanne, der gründlich und voll in seinem Gebiete drinnensteht, das Bedürfnis entstehen kann, mit dem, was Geisteswissen- schaft vermag, hineinzuleuchten in solch ein einzelnes Fach."
      ],
      [
        "Es wird Ihnen auch aus dem, was Professor Römer heute schon aus seinem Fachgebiet anführen konnte, her- vorgegangen sein, daß vor allen Dingen für dieses In- einanderarbeiten starke, kräftige Arbeit auf seiten der einschlägigen Geisteswissenschaft selber entwickelt werden muß.",
        "Denn was bis jetzt gegeben werden konnte es soll das durchaus voll anerkannt werden , das sind zunächst einzelne Richtlinien, die der Verifizierung mit Bezug auf die äußere Wissenschaft bedürfen."
      ],
      [
        "In alledem, was durch diesen Vortrag zu einer gewissen subjektiven Befriedigung an mich herangetreten ist, war enthalten eine Betrachtung über die Zähne.",
        "Mit den Zäh- nen also ist gestern geschlossen worden - jetzt komme ich ins Objektive."
      ],
      [
        "Und gestatten Sie, daß ich heute wiederum 118 mit den Zähnen beginne, allerdings zunächst nicht mit etwas, was ich Ihnen von mir aus über die Zähne erzählen will, sondern mit einem Ausspruch, der aus der Gelehr- samkeit des 11.",
        "Jahrhunderts, wie sie damals in Mittel- europa war, hervorgegangen ist."
      ],
      [
        "Dieser Ausspruch heißt: Swenne diu zunge den wint fähet unt in in den munt ziuhet, an den zanen si scephet daz wort daz si sprichet.",
        "Das heißt also: So wie die Zunge den Wind aus ihrer Umgebung abfängt und ihn in den Mund zieht, so schöpft sie aus den Zähnen das Wort heraus, das sie spricht."
      ],
      [
        "Nun, das ist ein Produkt der Gelehrsamkeit Mittel- europas im 11.",
        "Jahrhundert.",
        "Die meint also, daß die Zunge aus den Zähnen das Wort hervorzieht wie aus der Außenwelt die Luft, die sie in den Mund hineinzieht."
      ],
      [
        "Jetzt eine Probe aus der Gelehrsamkeit des 19.",
        "Jahr- hunderts, letztes Drittel, ein Wort, welches der als mo- derner Abgott von einer zahlreichen Schülerschar verehrte Philologe Wilhelm Scherer ausgesprochen hat, und das Sie verzeichnet finden in seiner «Deutschen Sprachgeschichte», wo er auch dieses Wort, das ich Ihnen eben vorgelesen habe, heranzieht."
      ],
      [
        "Das Wort, das er diesem entgegensetzt, das ist dieses: «Über ein solches Wort lachen wir in der Gegenwart».",
        "Das ist das wissenschaftliche Bekenntnis aus dem 19.",
        "Jahrhundert über dieses Wort aus dem 11.",
        "Jahrhun- dert; es drückt die Wissenschaftsgesinnung aus, die im weitesten Umkreise auch heute noch waltet und von den Vertretern des entsprechenden Faches in weiteren Hinwei- sen wohl auch heute noch ausgesprochen wird. 119 Wenn man diesen ganzen Gegensatz zunächst ins Auge faßt von dem Gesichtspunkte aus, der hier öfter einge- nommen worden ist, daß ein völliger Umschwung statt- gefunden hat in bezug auf die Seelenverfassung der Men- schen seit dem ersten Drittel des 15."
      ],
      [
        "Jahrhunderts, dann haben wir in der Zeit, die zwischen dem erstzitierten Aus- spruch und dem Ausspruch Wilhelm Scherers liegt, unge- fähr gerade das enthalten, was an Zeit verflossen ist seit dem Hinunterdämmern jener Seelenverfassung, die bis zum Beginn des 15.",
        "Jahrhunderts vorhanden war, und der Richtung, die seither heraufgekommen ist und bisher eine gewisse Ausbildung erfahren hat."
      ],
      [
        "Wilhelm Scherer setzt nun die Sätze, die er damit be- gonnen hat, daß er über ein solches Wort aus dem 11.",
        "Jahrhundert lachen müsse, mit einer Betrachtung fort, die etwa folgendes enthält.",
        "Er sagt, alles Bestreben in der Gegenwart müsse mit Bezug auf die Sprachwissenschaft darauf gerichtet sein, dasjenige, was aus der physiologi- schen Organisation des Menschen heraus die Physiologen über das Sprechen, über das Wortebilden zu sagen haben, mit dem zusammenzubringen, was die Philologen über die Entwickelung der Sprache seit älteren Zeiten bis in unsere Gegenwart zu sagen haben."
      ],
      [
        "Mit anderen Worten: Physio- logie und Philologie müßten sich auf diesem Gebiete der Wissenschaft die Hände reichen.",
        "Und Wilhelm Scherer fügt hinzu, er müsse leider gestehen, daß die Philologen sehr, sehr weit zurückgeblieben seien, und daß von ihrer Seite noch nicht so bald zu hoffen sei, daß sie den Physio- logen in bezug auf das, was sie aus der physischen Or- ganisation heraus für die Gestaltung des Sprechens zu sagen haben, entgegenkommen werden."
      ],
      [
        "So daß also Phy- siologie und Philologie zwei Wissenschaftszweige sind, deren Sich-Nichtverstehen ein von seiner Zeitgenossen- 120 schaft als berufen angesehener Mann in scharfer Weise zugesteht.",
        "Damit ist hingedeutet auf ein Phänomen, das überhaupt in unserer Zeit ein tonangebendes ist: daß sich die einzel- nen Wissenschaften mit ihren Methoden durchaus nicht verstehen, daß sie nebeneinander reden, ohne daß der- jenige, der nun hineingestellt wird in diesen Wissenschafts- betrieb und das hört, was ihm auf der einen Seite die Physiologen und auf der anderen Seite die Philologen zu sagen haben, damit - verzeihen Sie den vielleicht etwas gewagten Vergleich - etwas anderes anzufangen weiß, als daß er von zwei Seiten in bezug auf seine Seele durch die Begriffsbildungen aufgespießt wird."
      ],
      [
        "In einem gewissen Sinne, obwohl ich auch damit nicht viel mehr sagen will als etwas Analogisches, liegt schon in der Wortbezeichnung, die, ich möchte sagen, unbewußt ernst genommen wird von den neueren Wissenschafts- strömungen, ein gewisser Gegensatz ausgedrückt.",
        "In der Wortbezeichnung «Physiologie» liegt ausgedrückt, daß sie sein will ein Logos über das Physische des Menschen, also gewissermaßen dasjenige, was logisch, intellektualistisch erfaßt das Physische; in dem Wort «Philologie» liegt: Liebe zur Weisheit, Liebe zum Logos, Liebe zum Worte; es ist also die Wortbezeichnung hergenommen von einem Gefühlserlebnis."
      ],
      [
        "Das eine Mal ist die Wortbezeichnung hergenommen von einem Verstandeserlebnis, das andere Mal von einem Gefühlserlebnis.",
        "Und was der Physiologe als eine Art intellektuellen Logos über die menschliche Physis erzeugen will, das - nämlich den Logos - will eigentlich der Philologe lieben."
      ],
      [
        "Wie gesagt, ich will damit zunächst nur analogisch auf etwas hinweisen, was aber dennoch, wenn es weiter verfolgt wird, wenn es nament- lich geschichtlich verfolgt wird, eine gewisse Bedeutung 121 hat; und ich rate dazu, die Sache geschichtlich genauer zu verfolgen.",
        "Aber wir können da noch auf etwas anderes hinweisen, welches uns aus der Vorgeschichte, aus der Vorläuferschaft desjenigen, was dann im Menschheitsbewußtsein seit dem Beginne des 15."
      ],
      [
        "Jahrhunderts aufgetreten ist, entgegen- tritt.",
        "Man weiß, daß das, was man Logik nennt und was doch in einer gewissen Beziehung in der Sprache sein Ab- bild hat, im wesentlichen wenigstens, eine Schöpfung des Aristoteles ist."
      ],
      [
        "Und wenn man sich darauf berufen wollte, daß selbstverständlich - so wie bei einem heutigen Men- schen, der nicht Logik studiert hat, doch die Logik in sei- ner Seelenbetätigung lebt auch vor Aristoteles die Logik in der Seelenbetätigung der Menschen gelebt habe, so übersieht man, daß die Umwandlung des Unbewußten in Bewußtes dennoch eine tiefere Bedeutung in dem Verlaufe des menschlichen Geschehens hat.",
        "Damit, daß das Logische ins Bewußtsein heraufgehoben worden ist, ist auch ein realer Vorgang, allerdings ein innerlich realer Vorgang, in in der menschheitlichen Seelenentwickelung gegeben: zwi- schen dem Begriff und dem Worte bestand in älteren Zei- ten eine innige Beziehung."
      ],
      [
        "Wie eine solche innige Bezie- hung zwischen dem Begriff oder der Vorstellung und der Wahrnehmung bestand, wie Sie das ausgeführt finden in meinen «Rätseln der Philosophie», ebenso bestand ein in- niger Bezug, ein, ich möchte sagen, Ineinandersein von Worten und Vorstellungen.",
        "Jene Trennung, die wir heute psychologisch vollziehen müssen zwischen dem Worte und dem Inhalte der Vorstel- lung - besonders bei Betrachtung des Mathematisierens tritt das mit aller Klarheit hervor -, ist in älteren Zeiten nicht gemacht worden."
      ],
      [
        "Und gerade auf diese Unterschei- dung kam zuerst Aristoteles.",
        "Er hob innerhalb des Seelen- 122 lebens dasjenige, was Vorstellung, Begriff ist, aus dem Gewebe der Sprache heraus, machte es für die Erkenntnis zu etwas abgesondert Vorliegendem."
      ],
      [
        "Dadurch aber drängte er wiederum dasjenige, was in der Sprache lebt, weiter in das Unbewußte hinunter, als es vorher war.",
        "Es wurde gewissermaßen ein Abgrund für die Erkenntnis geschaffen zwischen dem Begriff oder der Vorstellung und dem Worte."
      ],
      [
        "Je weiter wir nämlich zurückgehen in der Betrachtung der menschlichen Sprache, desto mehr finden wir, daß in der Auffassung des Menschen Wort und Begriff oder Vor- stellung als eines erlebt werden, daß der Mensch gewisser- maßen das, was er denkt, innerlich hört, daß er ein Wort- bild, nicht so sehr ein Gedankenbild hat.",
        "Der Gedanke wird draußen an die Sinneswahrnehmungen und drinnen an das Wort geknüpft."
      ],
      [
        "Dadurch aber war auch für diese älteren Zeiten eine gewisse Empfindung vorhanden, die sich etwa so charakterisieren läßt: Indem die Menschen sich in ihren Worten aussprachen, fühlten sie, als ob das, was in ihren Worten widerklingt, unmittelbar auf eine im Instinktiven verborgene, unterbewußte Art von den Dingen in ihre Sprache hineingelangt wäre.",
        "Sie fühlten gewissermaßen, daß ein realer Vorgang sich abspielt zwi- schen dem, was in den Dingen und namentlich in den Tat- sachen lebt, und dem, was innerlich den Impuls zum Er- klingen des Wortes bildet."
      ],
      [
        "Sie fühlten einen solchen realen Zusammenhang, wie der Mensch heute noch einen realen Zusammenhang zwischen den Stoffen fühlt, die draußen sind, sagen wir Ei, Kalbfleisch, Salat, und dem, was dann in seinem Inneren mit dem Inhalte dieser Stoffe sich ab- spielt, wenn er verdaut.",
        "Er wird in diesem Vorgang, der sich abspielt vom Draußensein der Stoffe zu dem, was drinnen in der Verdauung geschieht, einen realen Vorgang sehen."
      ],
      [
        "Diesen realen Vorgang erlebt er unterbewußt.",
        "So 123 unterbewußt wenn auch viel deutlicher, von einem ge- wissen dämmerigen Bewußtsein schon durchzogen - war dasjenige, was man an der Sprache erlebte.",
        "Man hatte die Empfindung, daß etwas, was in den Dingen lebt, mit den Lauten, mit den Worten verwandt ist."
      ],
      [
        "Wie die Substanzen der Stoffe, die man ißt, mit dem, was innerlich im Men- schen im Stoffwechsel geschieht, zusammenhängen, so empfand man einen inneren Zusammenhang zwischen dem, was in den Dingen und Tatsachen vorgeht, was wortähnlich ist, und dem, was innerlich als Wort erklingt.",
        "Und indem Aristoteles das, was man da als einen realen Vorgang empfand, ins Bewußtsein heraufhob, wo die Be- griffe spielen, war für die Sprache dasselbe geleistet, was ein Mensch leistet, der darüber nachdenkt, was die Sub- stanzen der Stoffe in seinem Organismus anfangen."
      ],
      [
        "Etwas weiter voneinander entfernt ist allerdings das Denken über die Verdauung von dem realen Verdauungsvorgange selbst als das Denken von der Sprache.",
        "Aber eine Vorstel- lung von dem entsprechenden Verhältnis kann man ge- winnen, wenn man sich diese Vorstellung dadurch ver- deutlicht, daß man von einem Naheliegenderen zu einem Entfernteren und in der Entfernung Deutlicherwerdenden übergeht."
      ],
      [
        "Nun, für uns liegt ja, wenn wir an die Stelle der heuti- gen abstrakten Geschichtsbetrachtung eine mehr konkrete setzen, dieses vor, daß Dinge, die sich in Griechenland in der vorchristlichen Zeit, auch in der voraristotelischen Zeit abgespielt haben, für die mitteleuropäische Bevölkerung - die die Griechen durchaus noch als barbarisch, das heißt auf einer niedrigeren Kulturstufe empfunden haben - sich später abspielten.",
        "Und wir werden das Richtige treffen, und Geisteswissenschaft gibt dazu die Anleitung, dieses Gefühl richtig zur Gewißheit zu erheben, wenn wir uns 124 vorstellen, daß die Geistesverfassung, aus der gesprochen wird, gefühlsmäßig gesprochen wird, «die Zunge ziehet die äußere Luft in den Mund, so wie sie aus den Zähnen ziehet das Wort», daß diese Anschauungsweise, diese merkwürdig bildhaft sich aussprechende Anschauungs- weise ungefähr diejenige auch war, die in der voraristote- lischen Zeit auch geherrscht hat innerhalb Griechenlands, und an deren Stelle das getreten ist, was eben treten mußte durch die Abtrennung der Logik, des Logos, durch die Abtrennung des Gedankenhaften von dem, was in der Sprache zur Darstellung kommt."
      ],
      [
        "Sie wissen ja, daß in jener Gelehrsamkeit, welche sich zunächst entwickelt hat seit dem 15.",
        "Jahrhundert und aus welcher die verschiedenen Zweige der einzelnen Fachwis- senschaften hervorgegangen sind, daß in dieser Gelehr- samkeit als Bildung viel mitgewirkt hat, was sich als spätgriechische Kultur geltend gemacht hat."
      ],
      [
        "Gerade die Philologen, diejenigen also, die den Logos lieben sollen, sie wurden durchaus beeinflußt von dem, was aus der spätgriechischen Kultur hervorgegangen ist.",
        "Und man denke sich nur einmal einen solchen Spätgriechling als germanistischen Forscher, wie Wilhelm Scherer, der Früh- griechik gegenübergestellt, und die sagt ihm: Die Zunge ziehet die Sprache aus den Zähnen -, dann weist er das selbstverständlich zurück, dann will er von seinem Ge- sichtspunkte aus davon nichts wissen."
      ],
      [
        "Man muß solche Tatsachen schon einmal in einem Lichte betrachten, das etwas tiefer in die historischen Zusammenhänge hinunter- zuleuchten bemüht ist als dasjenige, was in der gewöhn- lichen landläufigen Geschichtswissenschaft heute vielfach vorhanden ist, sowohl auf dem Gebiete der äußeren poli- tischen oder Kulturgeschichte wie auch auf dem Gebiete der Sprachgeschichte. 125 Nun handelt es sich darum, welche Wege gesucht wer- den müssen, um in das Gefüge des Sprachorganismus - wenn ich mich so ausdrücken darf - selber wissenschaft- lich hineinzukommen.",
        "Schon in Äußerlichkeiten drückt sich aus, wie diejenige Betrachtungsweise, die die Seele allmählich heraufgehoben hat ins Gebiet der abstrakten Begriffe, sich entfernt hat von dem, was in der voraristotelischen Zeit über die Sprache empfunden worden ist."
      ],
      [
        "Was hat zum Beispiel hervorgebracht, als Meinung über die Entstehung der Sprache, diese in dem Zeichen des Aristotelismus stehende Forschung?",
        "Nun, sie wurde dadurch, daß sie die Seele heraufhob in das Abstrakte, dem unmittelbaren Zusam- menhang mit der Außenwelt entfremdet, durch den man erleben konnte, was real in den Dingen dem gebildeten Worte entspricht."
      ],
      [
        "Sie wurde dem entfremdet, suchte aber doch, wie ein solcher Zusammenhang aussehen kann, und sie übersetzte sich diesen Zusammenhang nun auch in allerlei Abstraktionen.",
        "Was im Inneren gefühlt worden ist, das versetzte sie in das Gebiet, wo man äußerlich, nach den Sinnes- oder sonstigen äußeren Beobachtungen sich Begriffe formt."
      ],
      [
        "Weil es unmöglich war, unterzutauchen in die Dinge, um den Vorgang zu suchen, wie das Wort aus den Dingen heraus in die menschliche Organisation wirkt, setzte man an die Stelle einer solchen Erfassung einen abstrakten Begriff, zum Beispiel in der sogenannten Wau- wau-Theorie oder in der Bimbam-Theorie.",
        "Die Wau- wau-Theorie besagt zum Schlüsse nichts anderes, als daß dasjenige, was äußerlich im Organischen als Ton, Laut zutage tritt, nachgeahmt wird."
      ],
      [
        "Es ist eine vollständig äußerliche Betrachtung eines äußerlichen Tatbestandes mit Hilfe von abstrakten Begriffen.",
        "Die Bimbam-Theorie unterscheidet sich von der Wauwau-Theorie nur dadurch, 126 daß bei ihr Rücksicht genommen wird auf das Unorgani- sche, wie es gewissermaßen den Ton aus sich entbindet."
      ],
      [
        "Dieser Ton wird dann wiederum auf eine äußerliche Weise von dem Menschen, der der äußeren Natur gegenüber- steht und sich von ihr beeinflussen läßt, nachgeahmt.",
        "Und die Umbildung desjenigen also, was - allerdings nicht überall, sondern nur auf einem engbegrenzten Erden- gebiete die Kinder rufen, wenn sie den Hund bellen hören: wau-wau, oder desjenigen, was ihnen in das Sprachgefühl hineinkommt, wenn sie die Glocke ertönen hören: bim-bam-bum, diese Umbildung wird dann durch eine merkwürdige Methode verfolgt."
      ],
      [
        "So sieht man das, was dann zum Organismus der Sprache sich gebildet hat, in den angedeuteten Theorien an, die ja durch nicht viel bessere bis heute ersetzt sind.",
        "Wir haben es also zu tun mit einem Innerlichwerden der Betrachtung über die Sprache."
      ],
      [
        "Vor allen Dingen ist anzustreben durch Geisteswissenschaft, wie sie hier ge- meint ist, daß die Sprachbetrachtung wiederum eine inner- liche werde, daß durch das, was erreicht werden kann im Aufsteigen von der sinnlichen zur übersinnlichen Erkennt- nis, dasjenige, allerdings jetzt in einer der vorgerückten Menschheit entsprechenden Gestalt, selbständig wieder- um gefunden werden könne, was einstmals gefühls- und instinktmäßig über die Sprache gedacht worden ist.",
        "Und da muß ich - ich kann wegen der Kürze der Zeit nur auf die Richtungen hinweisen, in denen die empirischen Tat- sachen zu verfolgen sind darauf aufmerksam machen, wie Geisteswissenschaft einen streng konkreten Weg ein- schlägt, wenn sie verstehen will, wie der Mensch sich von seiner Kindheit bis zu einem gewissen Lebensalter ent- wickelt."
      ],
      [
        "Sie finden das, was ich hier einigermaßen andeu- ten möchte, dargestellt zum Beispiel in meinem Büchelchen 127 «Die Erziehung des Kindes vom Gesichtspunkte der Gei- steswissenschaft» .",
        "Da muß zunächst darauf hingewiesen werden, wie die ganze seelisch-körperliche Konfiguration des Menschen in der Zeit vor dem Zahnwechsel eine wesentlich andere ist, als sie nach dem Zahnwechsel wird."
      ],
      [
        "Wer sich Beobachtun- gen für diese Tatsache angeeignet hat, der weiß, wieviel im seelisch-leiblichen Leben metamorphosiert wird in der Zeit, in der an die Stelle der ersten Zähne die zweiten treten.",
        "Und wer nicht durch Abstraktionen wie etwa die Anhänger des psychophysischen Parallelismus die Bezie- hungen von Leib, Seele und Geist sucht, sondern wer sie sucht in konkreten Erscheinungen, wer sie sucht nach einer wirklichen weitergebildeten naturwissenschaftlichen Me- thode, wer die innere Struktur des Seelenlebens im Kon- kreten erfassen kann, der wird eben finden, wie das, was später mehr seelisch in der eigentümlichen Konfiguration des Begriffslebens, in der Durchsetzung desjenigen, was begrifflich erfahren wird, mit Willensimpulsen, die dann zu der Bildung des Urteiles führen, wie das etwas ist, das bis zum Zahnwechsel in der physischen Organisation ge- wirkt hat."
      ],
      [
        "Und er wird nicht darüber spekulieren, was von der Geburt bis zum Zahnwechsel in der physischen Organisation «seelisch wirken» kann.",
        "Sondern er wird sich sagen, was dann im Zahnwechsel frei wird, frei wird aus einem Körper, in dem es vorher latent war, das hat vorher latent und gebunden in der physischen Organisa- tion des Menschen gewirkt."
      ],
      [
        "Und diese besondere Art der physischen Organisation, in der das später seelisch zu Be- obachtende wirkt, findet mit dem Herausstoßen der zwei- ten Zähne, auf das Sie auch gestern aufmerksam gemacht worden sind, seinen Abschluß.",
        "Nun muß man die Tatsachen, die hier vorliegen, nicht 128 einseitig physiologisch, sondern so betrachten, daß man, wie der Physiologe mit seinen Sinnen und dem an sie gebundenen Verstand in die physischen Vorgänge des menschlichen Organismus, ebenso mit dem, was Imagina- tion und Inspiration ist, in die seelischen Vorgänge ein- dringt, so daß man sie wirklich erkennt, nicht bloß, wie es die heutige Psychologie macht, mit Worten belegt."
      ],
      [
        "Wenn man wirklich in diese Vorgänge eindringt, dann muß man in dem Realen, das zuerst von der Geburt bis zum Zahn- wechsel latent ist, das dann frei wird, auch vorstellungs- gemäß, erkenntnisgemäß ein Reales schauen.",
        "Deshalb spricht meine Schrift über «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft», indem sie diesen Vorgang formelhaft zusammenfaßt, davon, daß mit dem Zahnwechsel der Ätherleib des Menschen, der vorher im physischen Leib gewirkt hat, erst frei zur Betätigung im Seelenleben geboren werde."
      ],
      [
        "Dieses «Geborenwerden des Ätherleibes» drückt sich aus im Zahnwechsel.",
        "Es ist notwendig, daß man gewissermaßen am Aus- gangspunkte anthroposophisch-geisteswissenschaftlicher Be- trachtung solches Formelhafte habe, wie zum Beispiel «Geburt des Ätherleibes aus dem physischen Leibe», was ja einem tatsächlichen Geschehen entspricht."
      ],
      [
        "Aber dann, wenn der Übergang gesucht werden soll von dieser Gei- steswissenschaft im engeren Sinne - die sich namentlich an die Betrachtung des menschlichen unmittelbaren Tages- erlebens hält zu der Betrachtungsweise in einzelnen Fachwissenschaften, dann wird dasjenige, was in solch formelhafter Weise zunächst ausgesprochen wird, etwas Ähnliches wie die Formel der Mathematik: es wird Me- thode, Methode für die Behandlung der Tatsachen.",
        "Und deshalb kann diese Geisteswissenschaft befruchtend auf die einzelnen Wissenschaften wirken, ohne daß immer 129 bloß dasjenige in die einzelnen Wissenschaften hinein fort- gesetzt wird, was allerdings beim Ausgangspunkte klar ins Auge gefaßt werden muß: daß der Mensch gegliedert ist in physischen Leib, Ätherleib und so weiter."
      ],
      [
        "So etwas kann man im Anfange durchaus wissen, und muß es wissen; es muß aber, wenn die Befruchtung durch Geistes- wissenschaft eintreten soll, Tun werden, es muß Methode werden, Art und Weise der Behandlung auch der sinnlich empirisch gegebenen Tatsachen.",
        "Und in dieser Beziehung wird Geisteswissenschaft, weil sie, aufsteigend vom Un- organischen, wo sie noch wenig tun kann, durch das Orga- nische heraufkommt in das geistige Gebiet, ich möchte sagen, nicht nur in dem Wie die einzelnen Wissenschaf- ten befruchten können, sondern sie wird ihnen gerade- zu aus ihrem Befunde heraus Tatsachenbestätigungen zu übergeben haben, welche Licht verbreiten über dasjenige, was von der anderen Seite durch sinnlich-physische Be- obachtung gewonnen und dann mit dem Verstande durch- schaut wird."
      ],
      [
        "Es müssen sich begegnen geistige und sinnlich- physische Forschung.",
        "Und es ist eine der wichtigsten Auf- gaben für die Zukunft, daß sich diese geistige Forschung und diese sinnlich-physische Forschung begegnen."
      ],
      [
        "Im Vorgang, der sich an dem Zahnwechsel besonders äußerlich offenbart, zeigt sich, daß dasjenige, was man - indem man aber eine konkrete Anschauung, nicht einen Wortbegriff ins Seelenauge faßt - als Ätherleib bezeich- net, für den ganzen menschlichen Organismus frei tätig wird, nachdem es vorher organisierend im physischen Leibe gewirkt hatte.",
        "Jetzt steigt es herauf ins Seelische, wird frei und wirkt dann in gewissem Grade bewußt auf den gan- zen Menschen zurück."
      ],
      [
        "Ein Ähnliches tritt wiederum ein mit dem, was äußer- lich sich offenbart als die Geschlechtsreife.",
        "Da sehen wir, 130 wie wiederum im menschlichen Erleben etwas dasteht, was sich ausdrückt auf der einen Seite in einem gewissen Meta- morphosieren des physischen Organismus, auf der anderen Seite in einem Metamorphosieren des Geistigen."
      ],
      [
        "Und ein Wesentliches beim Geistesforscher besteht ja darin, daß er sich ein ebensolches konkretes Anschauen für das an- eignet, was so im Geistig-Seelischen auftritt, wie sich der- jenige, der sich nur an der äußeren Anschauung bilden will, ein konkretes Anschauen aneignet für das, was er mit Augen sehen und mit dem Verstande kombinieren kann.",
        "Seelisches läßt sich nicht in dieser Weise anschauen, son- dern läßt sich in seiner Wirklichkeit nur imaginativ an- schauen."
      ],
      [
        "Es gibt keine wahre Psychologie, die nicht mit imaginativem Anschauen beginnt, und es gibt keine Mög- lichkeit, das Wechselverhältnis von Leib und Seele oder Körperleib und Geistseele zu finden, als die Brücke zu schlagen zwischen dem, was der äußeren physisch-sinn- lichen Anschauung gegeben ist als das Körperlich-Leibliche, und dem, was herausfällt aus dieser Anschauung, was nur im Aufsteigen zur übersinnlichen Erkenntnis gegeben sein kann als Wirklichkeit, dem Geistig-Seelischen.",
        "Wenn man nun dasjenige wiederum betrachtet, was im Stadium der Geschlechtsreife eintritt, dann wird man sich sagen müssen: Da sehen wir in gewissem Sinne den umge- kehrten Vorgang von dem, der beim Zahnwechsel sich ab- gespielt hat."
      ],
      [
        "Wir sehen, wie das, was als Begehrungsver- mögen im Menschen spielt, was der instinktive Charakter seines Willens ist, den Organismus in einer Weise ergreift, wie es ihn früher nicht ergriffen hat.",
        "Indem man wieder- um den ganzen breiten Tatsachenkomplex, der damit ins Auge gefaßt wird, formelhaft zusammenfaßt, kommt es dazu, daß man sagt: dasjenige, in dem namentlich die Begierdenatur schlummert, der astralische Leib des Men- 131 sehen wird frei, wenn die Geschlechtsreife eintritt."
      ],
      [
        "Er ist es, der sich nun wenn ich mich so ausdrücken darf als frei in den physischen Organismus hineinsenkt, diesen er- greift, durchsetzt und so die Begierde körperhaft macht, was in dem Geschlechtsreifwerden seinen Ausdruck findet.",
        "Nun, was ergibt aber die sachgemäße Vergleichung dieser beiden Vorgänge?"
      ],
      [
        "Wir sehen gewissermaßen, wenn der Zahnwechsel eintritt, ein Freiwerden des ätherischen Leibes des Menschen.",
        "Wie drückt sich das, was da ge- schieht, eigentlich aus?",
        "Es drückt sich so aus, daß der Mensch dadurch fähig wird, die Begriffsbildung, über- haupt das Bewegen im Vorstellungsleben, das früher mehr an seinen ganzen Organismus gebunden war, gebunden an die Kopforganisation weiter auszuführen."
      ],
      [
        "Gewissermaßen sehen wir - und Geisteswissenschaft sieht es nicht nur ge- wissermaßen, sondern in seiner Wirklichkeit -, daß das Ätherische, was wir dem Menschen als Ätherleib zuschrei- ben, sich mit dem Zahnwechsel zurückzieht auf dasjenige, was nur noch im Rhythmischen des menschlichen Organis- mus und im Stoffwechsel-Gliedmaßenorganismus lebt, und daß es an der Ausgestaltung des Hauptes, an der plasti- schen Gestaltung des Hauptes eine freie Tätigkeit ent- wickelt, an der das Bewußtseinsleben des Menschen im Vorstellen teilnimmt.",
        "Es wird gewissermaßen die Kopf- organisation in dieser Zeit freigelegt."
      ],
      [
        "Und wenn ich mich bildhaft ausdrücken darf über eine Wirklichkeit, die durchaus besteht, so muß ich sagen, was in den zweiten Zähnen aus der ganzen Organisation des Menschen sich an die Oberfläche treibt, das ist dasjenige seelisch-geistige Wirken, das vorher die ganze Körperorganisation durch- zieht und dann frei wird.",
        "Vorher durchzog es den ganzen Menschen bis in das Haupt hinein."
      ],
      [
        "Es zieht sich allmählich vom Haupte zurück; und es zeigt, wie es sich zurückzieht, 132 indem es sein Nicht-mehr-bis-zum-Haupte-Wirken da- durch offenbart, daß es haltmacht und die zweiten Zähne hervorbringt.",
        "Sie können sich das geradezu schematisch zur Anschauung bringen."
      ],
      [
        "Wenn ich das, was menschliche physische Organisation ist, mit der weißen Kreide schema- tisch andeute, und das, was ätherische Organisation ist, mit der roten Kreide, dann würde sich folgendes schema- tisch ergeben (siehe Abbildung): Sie sehen in der linksstehenden Figur den Menschen in seiner geistig-seelisch-leiblichen Wirksamkeit, wie er bis zum Zahnwechsel vor Ihnen steht.",
        "Sie sehen in der zwei- ten Figur, die rechts von Ihnen ist, wie sich zurückge- zogen hat das Ätherische in seiner unmittelbaren Wirk- samkeit von der Kopforganisation, wie es frei geworden ist in einer gewissen Beziehung, so daß es von da aus frei auf den menschlichen Kopforganismus wirkt."
      ],
      [
        "Und was als letztes geschieht aus diesem Wirken des Seeelisch-Geistigen in dem physischen Organismus, das ist das Heraustreiben der zweiten Zähne.",
        "Sie können, was Ihnen hier als geistige Anschauung mitgeteilt wird, ich möchte sagen, in seinem Abbilde beobachten, wenn Sie die Schädel, die Ihnen gestern Herr Professor Römer gezeigt hat, nehmen, indem 133 Sie vergleichen können den Ansatz der ersten Zähne mit dem Ansatz der zweiten Zähne."
      ],
      [
        "Wenn Sie das sinngemäß verfolgen wollen, dann müssen Sie zugrunde legen, was hier aus der Geisteswissenschaft gewonnen ist.",
        "Dann müs- sen Sie sich sagen, die ersten Zähne, mit alledem was sich in ihnen ausspricht, sind aus der ganzen menschlichen Organisation, einschließlich der Kopforganisation, heraus- geholt."
      ],
      [
        "Was sich in den zweiten Zähnen ausspricht, ist her- ausgeholt, nachdem sich langsam die innere seelische Or- ganisation, insofern sie den Ätherleib betrifft, in den rhythmischen und Stoffwechselorganismus zurückgezogen hat und für die Hauptesorganisation frei geworden ist.",
        "In einer ähnlichen Weise können wir uns sagen - wie ge- sagt, ich kann nur Richtlinien anführen , daß etwas vor- geht mit der Geschlechtsreife."
      ],
      [
        "Da wird dasjenige, was wir astralischen Leib formelhaft nennen, hineinversenkt in den physischen Leib, so daß es ihn schließlich ergreift und eben das bewirkt, was die Geschlechtsreife ausmacht.",
        "Nun aber geschieht, was sich am Menschen ereignet, in den mannigfaltigsten Metamorphosen."
      ],
      [
        "Wer einmal einen solchen Vorgang wirklich verstanden hat wie den, der sich mit der Geschlechtsreife ausdrückt, der ein gewisses neues Verhältnis in der menschlichen Entwickelung, in der Ent- wickelung des Menschen zur Außenwelt bewirkt, wer einen solchen Vorgang wirklich innerlich versteht, der er- kennt ihn dann auch, wenn er in einer gewissen Meta- morphose auftritt.",
        "Was mit der Geschlechtsreife auftritt, indem es den ganzen Menschen ergreift, indem es gewisser- maßen ein Verhältnis herausbildet des ganzen Menschen zu seiner Umgebung, das wird, ich möchte sagen, in einer anderen Metamorphose vorausgenommen in dem Augen- blicke, wo sich die Sprache in dem Kinde entwickelt."
      ],
      [
        "Nur findet das, was eben mit der Geschlechtsreife stattfindet, beim Kinde in der Sprachbildung in einer anderen Meta- morphose statt.",
        "Da spielt sich das, was mit der Ge- schlechtsreife den ganzen Menschen ergreift und sich hin- einergießt in sein Verhältnis zur Außenwelt, zwischen dem rhythmischen und Gliedmaßenmenschen und der Kopf- organisation des Menschen ab."
      ],
      [
        "Gewissermaßen dieselben Kräfte, die beim Geschlechtsreifwerden den ganzen Men- schen ergreifen und dirigierend wirken auf sein Verhältnis zur Außenwelt, machen sich geltend zwischen dem unteren und oberen Menschen.",
        "Und indem der untere Mensch lernt den oberen so empfinden, wie sonst der Mensch im spä- teren Alter die Außenwelt empfinden lernt, lernt er spre- chen."
      ],
      [
        "Ein Vorgang, den man äußerlich am Menschen beobachten kann in einem späteren Lebensalter, den muß man in der Lage sein zu verfolgen in seiner Metamorphose bis dahin, wo er als eine innerlich im menschlichen Orga- nismus sich abspielende Metamorphose, im Sprechenlernen eben, erscheint: der Vorgang, der sonst beim ganzen Men- schen in der Geschlechtsreife auftritt.",
        "Und hat man diese Sache erfaßt, dann tritt einem die Möglichkeit entgegen, zu begreifen, wie das Zusammen- spielen des unteren Menschen des rhythmischen und des Gliedmaßenmenschen - in seiner Wechselwirkung ein innerliches Erleben von etwas ausbildet, was auch äußer- lich vorhanden ist in der uns umgebenden Natur."
      ],
      [
        "Dieses Erleben auf innerliche Art desjenigen, was äußerlich vor- handen ist, führt dazu, daß das, was äußerlich stumm in den Dingen als deren eigene Sprache bleibt, anfängt zu klingen als die Menschensprache im menschlichen Inneren.",
        "Bitte, gehen Sie meinetwillen von diesem Satze wie von einem regulativen Prinzipe aus."
      ],
      [
        "Gehen Sie aus von diesem Satze, daß dasjenige, was in den Dingen, indem sie äußer- lich werden, materiell werden, verstummt, daß das in der Entmaterialisierung innerlich im Menschen hörbar wird und zum Sprechen kommt.",
        "Dann werden Sie den Weg fin- den, auf dem Sie nicht eine Wauwau- oder Bimbam- Theorie ausbilden, sondern auf dem Sie dasjenige, was äußerlich an den Dingen ist - und da eben für die äußere Beobachtung nicht wahrgenommen werden kann, weil es ja verstummt und nur noch auf übersinnliche Art vorhan- den ist -, aufgehen sehen als Sprache in des Menschen Inneren."
      ],
      [
        "Was ich damit ausspreche, ist, wie wenn man eine Linie hinzeichnet und damit eine Richtung angibt, in der man eigentlich am liebsten ein weit ausgesponnenes Gemälde malen möchte.",
        "Ich kann nur diesen mehr abstrakten Satz über die Beziehung der Dinge und Tatsachen der Außen- welt zur Entstehung der menschlichen Sprache im Inneren vor Sie hinstellen."
      ],
      [
        "Und sie werden alles, was Sie über die Sprache spüren können, in ein neues Licht gerückt sehen, wenn Sie den Weg finden von diesem abstrakt angenom- menen Satze, der zunächst formelhaft klingt, bis zu dem- jenigen, was Ihnen die Tatsachen sinngemäß verbindet.",
        "Und wenn Sie dann das, was auf diese Art philologisch gewonnen wird, an die Physiologie heranbringen wollen, dann werden Sie sich belehren lassen können über den Zu- sammenhang der äußeren Geschlechtsmetamorphose mit der Sprachmetamorphose, in dem Sie Tatsachen studieren, die vorliegen als ein noch zurückgebliebener Rest: als der sprachliche Rest der Geschlechtsreife-Metamorphose in dem Verändern der Stimme, das heißt des Kehlkopfes beim Knaben, und in manchen anderen Erscheinungen, die beim Weibe auftreten."
      ],
      [
        "Wenn Sie nur den Willen haben, einzu- gehen auf die Tatsachen und die Fäden ziehen von einer Tatsachenreihe zur anderen, sich nicht einkapseln in un- fruchtbare Spezialwissenschaften, sondern dasjenige wirk- 136 lich beleuchten wollen, was in der einen Wissenschaft vor- handen ist als Tatsache, durch die Tatsachen, die durch andere Wissenschaften zutage treten, dann werden die ein- zelnen Spezialwissenschaften das werden können, was der Mensch in ihnen suchen muß, wenn er eben weiterkom- men will auf der Bahn seines Erkennens sowohl wie auf der Bahn seines Wollens.",
        "Es wird sich uns morgen in einem Zusammenhang, der, wie es scheinen könnte, gar nicht hineingehört, sehr natur- gemäß ergeben, wie wir nun von dem Zahnwechsel zur Spracherscheinung und dann weiter zurückgehen können zu dem, was das dritte ist auf dieser rückläufigen Bahn: Wir sehen gewissermaßen in dem, was sich im Zahnwech- sel ausdrückt, eine Wechselwirkung zwischen physischem Leib und Ätherleib."
      ],
      [
        "Wir sehen wiederum in dem, was sich in der Sprache ausdrückt, eine Wechselwirkung zwischen astralischem Leib und Ätherleib.",
        "Und wir müssen suchen als drittes ein Wechselverhältnis zwischen dem Ich und dem, was im Menschen als astralischer Leib lebt, und wer- den da geführt werden auf dasjenige, was das dritte ist in dieser rückläufigen Betrachtung: auf die Einkörperung des Geistig-Seelischen, auf dasjenige, was in dem Geistig- Seelischen geboren wird."
      ],
      [
        "Sucht man den Weg vom Zahn- wechsel durch das Sprachentstehen, so ist die dritte Etappe die Etappe des Vereinens des präexistierenden mensch- lichen Geistig-Seelischen mit dem Leiblichen.",
        "Indem Aristoteles den Ausweg von der Betrachtung des Zahnwechsels zu der Betrachtung der Sprache durch seine Abstraktion vermauert hat, war er genötigt, zu dem Dogma seine Zuflucht zu nehmen, daß mit jedem neuen Menschenwesen ein neues Geistig-Seelisches geboren werde."
      ],
      [
        "Aus einem Mangel an Wille zum Weitergehen eines Er- kenntnisweges ist die Erkenntnis von der menschlichen 137 Präexistenz abhandengekommen und damit von alledem, was in wahrer Weise zur Erkenntnis der menschlichen Seele führt.",
        "Wir sehen einen geschichtlichen Zusammenhang, der sich aber auslebt in der Behandlung gewisser Probleme, und wir können zum Schlüsse sagen: Es stehen sich heute, nach dem Ausspruche eines im gegenwärtigen Sinne ganz be- deutenden Philologen, Philologie und Physiologie so ge- genüber, daß sie sich nicht verstehen können."
      ],
      [
        "Warum dieses?",
        "Weil Physiologie den Körper des Menschen stu- diert und bei diesem Studium nicht rückläufig zum Geiste kommt.",
        "Verfolgt man eine wahre Physiologie, dann fin- det man über das Körperliche der physiologischen Be- trachtung wiederum das Geistig-Seelische im Menschen."
      ],
      [
        "Wie nun, wenn man eine wahre Philologie verfolgt?",
        "Wenn man eine wahre Philologie verfolgt, so wird einem nicht der Logos ein Abstraktum, für das man dann sucht Nachbilder zu durchschauen, Nachbilder in naturwissen- schaftlicher Methode, sondern man sucht einzudringen in dasjenige, was man als «Philo»-loge angeblich liebt, durch imaginative und sonstige Betrachtung."
      ],
      [
        "Dann aber, wenn man in das eindringt, was für die heutige Philologie ein Schattenhaftes, Nebuloses geworden ist, nämlich den Sprachgenius, den schöpferischen Sprachgenius, wenn man in ihn eindringt, dann dringt man durch den Geist zu der äußeren Körperlichkeit.",
        "Physiologie findet auf dem Wege durch die innere Physis den Geist."
      ],
      [
        "Philologie, richtig betrachtet, findet auf dem Weg nach außen durch den Sprachgenius das in den Dingen, was aus den Dingen selber spricht und verstummt ist.",
        "Sie findet nicht Wauwau und Bimbam, sondern sie findet in den körperlich uns umgebenden Dingen die Ver- anlassung dazu, daß Worte, daß die Sprache in uns ent- 138 stehen."
      ],
      [
        "Die Physiologie hat den Weg verloren zu ihrem Ziel, indem sie beim Körper stehenbleibt und nicht durch den Körper zum Geist innerlich vordringt.",
        "Die Philologie hat den Weg verloren, weil sie beim Sprachgenius, den sie dann nur abstrakt faßt, stehenbleibt und nicht vordringt in das Innere der äußeren Dinge, aus denen das erklingt, was im Worte lebt."
      ],
      [
        "Wenn Philologie nicht so reden wird, als ob das Wauwau und Bimbam in äußerlich abstrakter Weise nachgemacht werde durch den Menschen, sondern so reden wird über die äußerliche Körperlichkeit, daß ihr klar werden wird in Imaginationen, wie aus dieser äußer- lichen Körperlichkeit das Wort entspringt, das im Inneren echohaft widertönt, wenn also Physiologie den Geist, Philologie die Körperlichkeit gefunden haben wird, dann werden sie sich finden.",
        "Damit habe ich den Weg, den in gewissenhafter Arbeit die Geisteswissenschaft im anthroposophischen Sinne lei- ten will, fadengezogen."
      ],
      [
        "Ich habe nur einige Andeutungen auf diesem besonderen Gebiete der einleitenden Sprach- wissenschaft gegeben.",
        "Nun, diese Dinge werden unter uns besprochen, diese Dinge werden von uns erstrebt.",
        "Während diese Dinge von uns erstrebt werden, daß sie Zeugen sein können für das- jenige, was auf einem Erkenntniswege ganz aus dem Geiste unserer Zeit heraus erstrebt wird, und während Sie sehen können aus dem, was erstrebt wird, wahrscheinlich doch einen gewissen Ernst, der sich messen kann mit dem Ernste, der in anderen Gebieten des Lebens besteht, tobte gestern in Stuttgart eine Versammlung, die unsere Redner zum großen Teile niedertrampelte, die gar nicht den Wil- len hatte, auf irgend etwas hinzuhören, die nicht eingehen wollte auf dasjenige, was wir zu sagen haben, sondern die durch Getrampel und ähnliche Dinge dasjenige niederzu- 139 ringen bestrebt war, was in ernster Weise angestrebt wird."
      ],
      [
        "Und, indem ich mich an die Kommilitonen wende, so darf ich sagen: am gestrigen Abend fehlten in Stuttgart Ihre Kollegen nicht von der anderen Fakultät, sondern von der anderen Gesinnung -, die fehlten da nicht, die waren bei dem Niedertrampeln wohl vorhanden.",
        "Meine sehr verehrten Anwesenden, meine lieben Kom- militonen!"
      ],
      [
        "Es wird immer deutlicher und deutlicher wer- den, wie von einer gewissen Seite her dasjenige, das man nicht widerlegen kann, weil man es nicht widerlegen will, weil man sich durch träges Fortsetzen eines Alten, das sich überlebt hat, überhaupt auf das Neue nicht einlassen will, daß man das durch äußere Gewalt wird niedertram- peln wollen.",
        "Nun, ich möchte nur an Sie hier appellieren in der Weise, daß ich allerdings zu Ihnen den Glauben habe, daß Sie sich vielleicht in Ihrem Inneren sagen: Bei dieser Prozedur des Niedertrampeins haben wir auch noch ein Wort mitzureden!"
      ],
      [
        "Möge aber dieses Wort zur Tat werden. 140"
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "Dritter Disputationsabend Dornach, 7. April 1921",
    "paragraphs": [
      "Die Fragen bezogen sich nicht auf das Thema des Tages «Sprach- wissenschaft», sondern griffen auf früher behandelte Probleme zurück. Steiner. Hier ist die Frage: Es ist gesagt, die drei Dimensionen des Raumes wären nicht gleich in ihrer Struktur - worinnen liegt der Unterschied?",
      "Es ist jedenfalls der Satz in dieser Weise niemals ge- faßt worden: Die drei Dimensionen des Raumes seien «nicht gleich in ihrer Struktur», sondern dasjenige, auf das wahrscheinlich hier hingewiesen ist, ist das Folgende. Wir haben zunächst den mathematischen Raum, den Raum, den wir uns so vorstellen wenn wir uns über- haupt eine exakte Vorstellung davon machen -, daß wir uns drei aufeinander senkrecht stehende Dimensionsrich- tungen vorstellen, den wir uns also etwa definieren durch die drei aufeinander senkrecht stehenden Koordinaten- achsen.",
      "So wie wir gewöhnlich mathematisch diesen Raum be- trachten, ist eine absolute Gleichbehandlung der drei Di- mensionen vorhanden. Wir machen so sehr keinen Unter- schied zwischen den Dimensionen oben-unten, rechts-links, vorne-rückwärts, daß wir uns eventuell sogar diese drei Dimensionen als vertauschbar denken können.",
      "Es kommt schließlich beim bloßen mathematischen Raum gar nicht darauf an, ob wir, wenn wir die X-Achse und die Z-Achse aufeinander senkrecht stehend, und die Y-Achse darauf wieder senkrecht stehend haben, nun die Ebene, auf der die Y-Achse steht, oder ob wir diese Achse selbst «hori- 141 zontal» oder «vertikal» nennen oder dergleichen. Ebenso kümmern wir uns bei diesem Raum sozusagen nicht um seine Begrenztheit.",
      "Nicht etwa, daß wir ihn grenzenlos vorstellten. Bis zu dieser Vorstellung steigt man ja ge- wöhnlich nicht auf, sondern man stellt ihn so vor, daß man sich um seine Grenzen nicht kümmert, vielmehr still- schweigend die Annahme macht, man könne von jedem Punkte - sagen wir zum Beispiel der X-Richtung - aus- gehen und ein weiteres Stück an dasjenige, was man bereits nach der X-Richtung abgemessen hat, dazufügen, zu die- sem wieder ein Stück und so weiter, und man würde nie- mals veranlaßt sein, irgendwo ans Ende zu kommen.",
      "Gegen diese im Sinne der euklidischen Geometrie liegende Vorstellung vom Räume ist schon von Seiten der Meta- geometrie im Laufe des 19. Jahrhunderts manches aufge- stellt worden. Ich will nur daran erinnern, wie zum Bei- spiel Riemann unterschieden hat zwischen der «Unbe- grenztheit» des Raumes und der «Unendlichkeit» des Raumes.",
      "Und zunächst ist auch für das rein begriffliche Vorstellen gar keine Nötigung vorhanden, den Begriff der «Unbegrenztheit» und den der «Unendlichkeit» als iden- tisch anzunehmen. Nehmen Sie zum Beispiel eine Kugel- oberfläche.",
      "Wenn Sie auf eine Kugeloberfläche zeichnen, so werden Sie finden, daß Sie nirgends an eine Raum- grenze kommen, durch die Sie gewissermaßen im Fort- führen Ihrer Zeichnung gehindert werden können. Sie werden gewiß, wenn Sie weiterzeichnen, in Ihre letzte Zeichnung wieder hineinfahren; aber Sie werden niemals, wenn Sie auf der Kugeloberfläche bleiben, genötigt sein, sich durch eine Grenze im Zeichnen aufhalten zu lassen.",
      "So daß Sie sich also sagen können: Die Kugeloberfläche ist in bezug auf meine Fähigkeit, darauf zu zeichnen, unbegrenzt. - Aber niemand wird deshalb behaupten, daß 142 die Kugeloberfläche unendlich ist. Also man kann unter- scheiden, rein begrifflich, zwischen der Unbegrenztheit und der Unendlichkeit.",
      "Das kann nun unter gewissen mathematischen Voraus- setzungen auch auf den Raum ausgedehnt werden, kann so auf den Raum ausgedehnt werden, daß man sich vor- stellt: wenn ich in der X- oder Y-Achse eine Strecke dazu- setze, und dann wieder eine und so weiter, und da niemals gehindert werde, immer weitere Strecken anzusetzen, so könnte diese Eigenschaft des Raumes zwar für seine Unbegrenztheit sprechen, aber nicht für die Unendlichkeit des Raumes. Es brauchte trotz dieser Tatsache, daß ich immer neue Stücke anstückeln kann, der Raum durchaus nicht unendlich zu sein, er könnte unbegrenzt sein.",
      "Also diese beiden Begriffe müssen auseinandergehalten werden. So daß man also annehmen könnte, daß der Raum dann, wenn er zwar unbegrenzt, aber nicht unendlich wäre, in derselben Weise, als Raum aber jetzt, eine innerliche Krümmung hätte, daß er also in irgendeiner Weise ebenso in sich wiederum zurückkehren würde, wie eine Kugel- oberfläche in sich zurückkehrt.",
      "Gewisse Vorstellungen der neueren Metageometrie rech- nen durchaus mit solchen Annahmen. Niemand kann ei- gentlich sagen, daß gegen solche Annahmen sich sonderlich viel einwenden läßt; denn, wie gesagt, es gibt gar keine Möglichkeit, aus dem, was wir am Räume erfahren, etwa seine Unendlichkeit in irgendeiner Weise abzuleiten.",
      "Er könnte ganz gut in sich gekrümmt und dann endlich sein. Ich kann diesen Gedankengang natürlich nicht ausfüh- ren, denn er ist fast der durchgehende Gedankengang der ganzen neueren Metageometrie. Sie finden aber in Ab- handlungen von Riemann, Gauß und so weiter, die ja leicht erhältlich sind, genügend Anhaltspunkte, um, wenn 143 Sie auf solche mathematischen Vorstellungen Wert legen, auf sie einzugehen.",
      "Das ist also zunächst von der rein mathematischen Seite her das, was in den, ich möchte sagen starren, nach allen Seiten neutralen Raum der euklidischen Geometrie Ein- wände hineingebracht hat, die eben nur abgeleitet waren aus der «Unbegrenztheit». Aber dasjenige, auf das in der Frage hingedeutet wird, wurzelt noch in etwas anderem.",
      "Nämlich darinnen, daß der Raum, mit dem wir zunächst rechnen und der uns zum Beispiel in der analytischen Geometrie vorliegt, wenn wir uns eben mit den drei auf- einander senkrecht stehenden Koordinatenachsen zu tun machen, daß der Raum zunächst ein Abstraktum ist, eine Abstraktion. Und eine Abstraktion - aus was?",
      "Das ist die Frage, die noch zuerst aufgeworfen werden muß. Es handelt sich darum, ob man bei dieser Abstraktion «Raum» stehenzubleiben hat, oder ob das nicht der Fall ist. Hat man bei dieser Abstraktion des Raumes stehenzu- bleiben?",
      "Ist das der einzige Raum, von dem man sprechen kann? Besser gesagt: Ist dieser abstrakte Begriff des Rau- mes der einzige, von dem man berechtigterweise sprechen kann, dann kann man eigentlich nur das eine einwenden, dasjenige, was eben in der Riemannschen oder einer an- deren Metageometrie genügend eingewendet wird.",
      "Die Sache liegt ja so, daß zum Beispiel die Kantschen Raum- definitionen durchaus auf dem ganz abstrakten Raumbe- griff, bei dem man sich um Unbegrenztheit oder Unend- lichkeit zunächst nicht kümmert, aufgestellt sind, und daß dann im Laufe des 19. Jahrhunderts auch innerlich, in bezug auf seinen Vorstellungsgehalt, dieser Raumbegriff eben von der Mathematik erschüttert worden ist.",
      "Es kann keine Rede davon sein, daß etwa die Kantschen Defini- tionen auch noch gelten würden für einen Raum, der zwar 144 nicht unendlich, aber unbegrenzt ist. Überhaupt würde da noch manches im weiteren Verlaufe der «Kritik der reinen Vernunft», die Paralogismenlehre zum Beispiel, ins Wan- ken kommen, wenn man eben genötigt wäre, überzugehen zu dem Begriff des unbegrenzten, in sich gekrümmten Raumes.",
      "Ich weiß ja, daß für das gewöhnliche Vorstellen dieser Begriff des gekrümmten Raumes Schwierigkeiten macht. Allein vom rein mathematisch-geometrischen Standpunkte aus läßt sich gegen das, was da angenommen ist, nichts anderes einwenden, als daß man sich eben in einem zu- nächst ganz wirklichkeitsfernen Gebiet der reinen Ab- straktion bewegt.",
      "Und wer genauer zusieht, wird finden, daß in den Ableitungen moderner Metageometrie im Grunde genommen ein merkwürdiger Circulus liegt. Es ist dieser, daß man zunächst ausgeht von dem Vorstellen der euklidischen Geometrie, die sich also nicht kümmert um eine Begrenztheit des Raumes.",
      "Daraus bekommt man dann gewisse abgeleitete Vorstellungen, also sagen wir Vorstellungen, die sich eben auf so etwas wie eine Kugel- fläche beziehen. Und dann kann man wiederum, indem man mit den Formen, die sich da ergeben, gewisse Relegie- rungen oder Umdeutungen vornimmt, von da aus Inter- pretationen des Raumes machen.",
      "Man sagt alles eigentlich unter Voraussetzung der euklidischen Koordinatengeome- trie. Man bekommt unter dieser Voraussetzung ein ge- wisses Krümmungsmaß heraus. Man kommt bis zu den Ableitungen. Alles durchaus mit den Vorstellungen der euklidischen Geometrie.",
      "Dann aber wendet man sozusagen um: man benützt nun diese Vorstellungen, die sich erst mit Hilfe der euklidischen Geometrie ergeben können, also zum Beispiel das Krümmungsmaß, um nun wiederum zu einer anderen Vorstellung zu kommen, die zu einer Rele- gierung führen und für das von den krummen Formen Gewonnene eben wiederum eine Deutung ergeben kann. Im Grunde genommen bewegt man sich da in einem wirk- lichkeitsfremden Gebiet, indem man Abstraktionen aus Abstraktionen herausholt.",
      "Berechtigt wäre die Sache nur dann, wenn empirische Tatbestände notwendig machten, sich mit dem, was man durch so etwas herausbekommt, nach den Vorstellungen dieser Tatbestände zu richten. Es handelt sich also darum: Wo liegt das Erfahrungs- gemäße für dasjenige, was die Abstraktion «Raum» ei- gentlich ist?",
      "Denn der Raum als solcher, wie er bei Euklid vorgestellt wird, ist eine Abstraktion. Worinnen liegt das, was erlebbar, was wahrnehmbar ist? Da müssen wir zunächst sagen: Wir müssen von der menschlichen Erfahrung des Raumes ausgehen.",
      "Der Mensch, hineingestellt in die Welt, nimmt durch seine eigene Tätigkeit der Erfahrung eigentlich nur eine Raum- dimension wirklich wahr, und das ist die Tiefendimension. Dieses Wahrnehmen, dieses erarbeitete Wahrnehmen der Tiefendimension durch den Menschen beruht auf einem Bewußtseinsvorgang, der sehr häufig nicht beachtet wird.",
      "Allein dieses erarbeitete Wahrnehmen ist doch etwas ganz anderes als die Vorstellung des Ebenenmäßigen, die Vor- stellung der Ausdehnung in zwei Dimensionen. Wenn wir mit unseren beiden Augen, also mit unserem Totalgesicht in die Welt sehen, so wissen wir nie etwas davon, daß diese zwei Dimensionen durch eine eigene Tätigkeit, durch ein Sich-mit-der-Seele-Betätigen zustande kommen.",
      "Sie sind sozusagen da als zwei Dimensionen. Während die dritte Dimension - wenn auch durchaus dies Tätige ge- wöhnlich nicht ins Bewußtsein herauf gehoben wird - durch eine solche gewisse Betätigung zustande kommt.",
      "Wir müs- sen uns eigentlich erst das Wissen, die Erkenntnis darüber 146 erarbeiten, wie tief im Räume darinnen, wie weit entfernt von uns irgendein Gebilde liegt. Die Ausdehnung der Fläche, die erarbeiten wir uns nicht, die ist durch die An- schauung gegeben.",
      "Aber durch unsere zwei Augen erarbei- ten wir uns tatsächlich die Tiefendimension. So daß die Art und Weise, wie wir die Tiefendimension erleben, zwar hart an der Grenze des Bewußten und des Unbe- wußten liegt; aber wer gelernt hat, auf solche Sachen seine Aufmerksamkeit zu richten, der weiß, daß die halb unbe- wußt oder dritteis unbewußt, nirgends bewußt, zustande kommende Tätigkeit der Abschätzung der Tiefendimen- sion viel mehr einer Verstandes-, überhaupt einer seeli- schen Tätigkeit, einer aktiven Seelentätigkeit ähnlich ist als all dasjenige, was nur in der Ebene angeschaut wird.",
      "Es ist also die eine Dimension des dreidimensionalen Raumes schon für unser gegenständliches Bewußtsein tätig erobert. Und wir können nicht anders sagen als: Indem wir die Stellung des aufrechten Menschen betrachten, ist damit etwas gegeben in bezug auf diese Tiefendimension - vorne-rückwärts -, was nicht vertauschbar ist mit einer anderen Dimension.",
      "Denn einfach dadurch, daß der Mensch in der Welt dasteht und in einer gewissen Weise sich betätigend, diese Dimension erlebt, ist das, was er da erlebt, nicht mit irgendeiner anderen Richtung ver- tauschbar. Für den einzelnen Menschen ist diese Tiefen- dimension etwas, was mit einer anderen Dimension nicht vertauschbar ist.",
      "Es ist durchaus auch so, daß das Erfassen der Zweidimensionalität - also das oben-unten, rechts- links, natürlich auch wenn es vor uns ist - auch an andere Hirnpartien gebunden ist, da es im Sehvorgang, also im sinnlichen Anschauungsvorgang drinnen liegt; während mit Bezug auf die Lokalisation im Hirn das Zustande- kommen der dritten Dimension durchaus jenen Zentren naheliegt, die für die Verstandestätigkeit in Betracht zu ziehen sind. Also hier sehen wir schon, daß beim Zu- standekommen dieser dritten Dimension sogar in bezug auf das Erleben ein wesentlicher Unterschied ist gegenüber den zwei anderen Dimensionen.",
      "Steigen wir dann aber auf bis zur Imagination, dann kommen wir überhaupt heraus aus dem, was wir da in der dritten Dimension erleben: Wir gehen in der Imagina- tion eigentlich zur zweidimensionalen Vorstellung über. Und wir haben uns jetzt - allerdings ebenso leise ange- deutet wie das Erarbeiten der dritten Dimension im gegen- ständlichen Vorstellen auch die andere Vorstellung, die Vorstellung des rechts-links, noch zu erarbeiten; so daß da wiederum ein bestimmtes Erlebnis liegt im rechts-links.",
      "Und endlich: wenn wir zur Inspiration aufsteigen, so gilt dasselbe für das oben-unten. Für das gewöhnliche Vorstellen, das an unser Nerven- Sinnessystem gebunden ist, erarbeiten wir uns die dritte Dimension.",
      "Wenn wir uns aber mit Ausschaltung der gewöhnlichen Tätigkeit des Nerven-Sinnessystems direkt ans rhythmische System wenden - was in einer gewissen Beziehung beim Aufsteigen zur Imagination stattfindet, es ist das nicht ganz genau gesprochen, aber das tut für jetzt nichts , dann haben wir das Erleben der zweiten Dimension. Und das Erleben der ersten Dimension haben wir, wenn wir zur Inspiration aufsteigen, das heißt, wenn wir vorrücken bis zu dem dritten Glied der menschlichen Organisation.",
      "So erweist sich dasjenige, was wir im abstrakten Räume vor uns haben, als genau, weil wir ja alles, was wir uns in der Mathematik erobern, aus uns selbst herausholen. Was sich in der Mathematik ergibt als der dreifache Raum, das ist eigentlich etwas, was wir aus uns selbst heraus 148 haben.",
      "Steigen wir aber in uns hinunter durch die über- sinnlichen Vorstellungen, so ergibt sich nicht der abstrakte Raum mit seinen drei gleich gültigen Dimensionen, sondern es ergeben sich drei verschiedene Wertigkeiten für die drei verschiedenen Dimensionen: vorne-hinten, rechts-links, oben-unten; sie sind nicht miteinander vertauschbar. Daraus folgt noch ein anderes: Wenn diese drei nicht mit- einander vertauschbar sind, ist auch nicht nötig, sie sich mit der gleichen Intensität vorzustellen.",
      "Das ist das We- sentliche des euklidischen Raumes, daß wir die X-, Y-, Z-Achse - es ist das ja vorauszusetzen für jede Berechnung eines Geometrischen - mit gleicher Intensität vorstellen. Wenn wir die X-, Y-, Z-Achse uns vorhalten, so müssen wir - wenn wir bei dem bleiben wollen, was uns unsere Gleichungen sagen in der analytischen Geometrie, aber eine innere Intensität der drei Achsen annehmen - diese Intensität gleichwertig vorstellen.",
      "Wenn wir etwa die X-Achse elastisch vergrößern würden mit einer gewissen Intensität, so müßten sich die Y- und Z-Achsen mit glei- cher Intensität vergrößern. Das heißt, wenn ich dasjenige, was ich ausdehne, nun intensiv fasse, so ist die Kraft des Ausdehnens, wenn ich so sagen darf, für die X-, Y-, Z-Achse, also für die drei Dimensionen des euklidischen Raumes, gleich.",
      "Deshalb möchte ich - den Begriff Raum in dieser Weise natürlich anwendend - diesen Raum den starren Raum nennen. Nun, das ist nicht mehr der Fall, wenn wir den realen Raum nehmen, von dem dieser starre Raum eine Abstrak- tion ist, wenn wir den Raum nehmen, der auf die Weise gewonnen ist, daß er eben aus dem Menschen herausgeholt ist.",
      "Dann können wir nicht mehr davon sprechen, daß diese drei Ausdehnungsintensitäten gleich sind. Sondern im wesentlichen ist die Intensität abhängig von dem, was 149 sich am Menschen vorfindet: des Menschen Größenver- hältnisse sind durchaus das Ergebnis der Raumausdeh- nungsintensitäten.",
      "Und wir müssen zum Beispiel, wenn wir das oben-unten die Y-Achse nennen, uns diese mit einer größeren Ausdehnungsintensität vorstellen als zum Beispiel die X-Achse, die entsprechen würde dem rechts- links. Wenn wir nach einem formelhaften Ausdruck für diesen realen Raum suchen, wenn wir also wiederum, was da real gemeint ist, formelhaft ausdrücken würden - also wiederum Abstraktion; wir müssen uns nur bewußt blei- ben, daß diese Abstraktion eben eine Abstraktion ist -, bekämen wir dann ein dreiachsiges Ellipsoid.",
      "Nun liegt aber auch die Veranlassung vor, diesen drei- achsigen Raum, in dem das übersinnliche Vorstellen leben muß, in seinen drei ganz verschiedenen Ausdehnungsmög- lichkeiten so vorzustellen, daß wir mit dem realen X-, Y-, Z-Achsenerleben, das uns mit unserem physischen Körper gegeben ist, diesen Raum auch als dasjenige erkennen, was dann gleichzeitig das Wirkungsverhältnis der in diesem Raum befindlichen Weltenkörper zum Ausdruck bringt. Wenn wir uns das vorstellen, so müssen wir in einer gewissen Weise bedenken, daß auch alles, was wir uns da draußen in diesem dreidimensionalen Weltenraume denken, nach verschiedenen Richtungen hin nicht einfach mit gleicher Ausdehnungsintensität der X-, Y-, Z-Achse zu denken ist, wie das bei dem euklidischen Raum der Fall ist, sondern wir müssen uns denken, daß der Welten- raum an sich eine Konfiguration hat, die auch durch ein dreiachsiges Ellipsoid vorzustellen wäre.",
      "Und dafür spricht durchaus die Anordnung gewisser Sterne. Man nennt gewöhnlich unser Milchstraßensystem eine Linse und so weiter. Es ist durchaus nicht möglich, es sich als eine Kugelfläche vorzustellen; wir müssen es uns in einer 150 anderen Weise vorstellen, wenn wir schon bei einer rein physischen Tatsache bleiben.",
      "Sie sehen gerade bei der Behandlung des Raumes, wie wenig naturgemäß das neuere Denken ist. In den älteren Zeiten, den älteren Kulturen, hat sich niemand einer solchen Vorstellung hingegeben, wie es die des starren Raumes geworden ist.",
      "Man kann noch nicht einmal sagen, daß in der euklidischen Geometrie schon eine klare Vorstellung von diesem starren Räume mit den drei gleichen Aus- dehnungsintensitäten, auch den drei aufeinander senk- recht stehenden Linien, vorlag. Sondern erst, als man anfing den Raum Euklids rechnend zu behandeln - indem eben das Abstrahieren in der neueren Zeit ein wesent- licher Grundzug des Denkens geworden ist -, ist eigentlich diese abstrakte Vorstellung des Raumes entstanden.",
      "In älteren Zeiten hatte man durchaus ähnliche Erkenntnisse, wie ich sie jetzt eben wiederum aus der Natur des über- sinnlichen Erkennens heraus entwickelt habe. Sie können daraus ersehen, daß Dinge, auf die man heute so unend- lich stark baut, die man als Selbstverständlichkeit betrach- tet, im Grunde genommen eine solche Bedeutung nur aus dem Grunde haben, weil sie in einer wirklichkeitsfremden Sphäre spielen.",
      "Der Raum, mit dem man heute rechnet, ist eine Abstraktion; er spielt durchaus in einer wirklich- keitsfremden Sphäre. Er ist abstrahiert von Erfahrungen, von denen wir allerdings durch reales Erleben wissen kön- nen.",
      "Aber man begnügt sich heute vielfach mit dem, was Abstraktionen sind. In unserer Zeit, wo man so viel auf Empirie pocht, beruft man sich am alleröftesten auf Ab- straktionen. Und man merkt es nicht. Man glaubt, sich in der Wirklichkeit mit den Dingen zu bewegen.",
      "Aber Sie sehen, wie sehr unsere Vorstellungen in dieser Beziehung der Rektifizierung bedürfen. Der Geistesforscher fragt bei jeder Vorstellung nicht bloß, ob sie logisch ist. Logisch ist durchaus der Riemann- sche Raum auch, obwohl er in gewisser Beziehung nur eine Dependance des euklidischen Raumes ist; aber aus dem Grunde ist er im Vorstellen eigentlich doch nicht zu vollziehen, weil man zu ihm kommt mit einem ganz abstrakten Denken, indem man auf Grund einer Schluß- folgerung, zu der man gekommen ist, gewissermaßen mit seinem ganzen Denken umkippt.",
      "Der Geistesforscher fragt beim Vorstellen nicht bloß, ob es logisch ist, sondern ob es auch wirklichkeitsgemäß ist. Das ist für ihn das Ent- scheidende, eine Vorstellung anzunehmen oder nicht. Erst dann nimmt er eine Vorstellung an, wenn diese Vorstel- lung wirklichkeitsgemäß ist.",
      "Und dieses Wirklichkeitsgemäßsein wird als Kriterium gegeben sein, wenn man überhaupt einmal sachgemäß auf solche Vorstellungen eingehen wird, welches die Berechti- gung zum Beispiel von so etwas wie die Relativitätstheorie ist. Sie ist für sich, möchte ich sagen, weil sie sich nur inner- halb des Gebietes der logischen Abstraktion erfaßt, so lo- gisch, wie nur irgend etwas logisch sein kann.",
      "Es kann schon nichts logischer sein als die Relativitätstheorie! Aber die andere Frage ist diese, ob ihre Vorstellungen vollzieh- bar sind. Und da brauchen Sie nur die Vorstellungen, die dort als analoge aufgeführt werden, anzusehen, so werden Sie finden: Das sind eigentlich ganz wirklichkeitsfremde Vorstellungen, mit denen nur so herumgeworfen wird.",
      "Das sei nur zum Versinnlichen da -, sagt man zuvor. Aber es ist eben doch nicht nur zur Versinnbildlichung da. Sonst würde wiederum die ganze Prozedur in der Luft hängen. Das also möchte ich sagen über das, worauf sich die Frage bezieht.",
      "Sie sehen, es ist nicht möglich, Fragen, die auf solche Gebiete hingehen, so ganz leicht zu beantworten. 152 Nun liegt eine Frage vor in bezug auf den Satz: Der Organismus eines alten Ägypters oder Griechen war ganz anders als der des modernen Menschen. Sehr verehrte Anwesende, das habe ich selbstverständ- lich nicht gesagt!",
      "Und da muß ich an dieser Stelle durch- aus auf etwas aufmerksam machen, auf das ich oftmals, und zwar wirklich nicht aus Unbescheidenheit aufmerk- sam mache: Ich pflege mich so genau, wie mir irgend mög- lich ist, auszudrücken. Und es ist eigentlich eine nicht gerade mir persönlich, da ist es ja zu ertragen, aber vom Gesichtspunkt der anthroposophischen Geistesbewegung - außerordentlich schmerzliche Tatsache, daß gegenüber mancherlei Dingen, zu deren Formulierung ich alle mög- lichen Vorsichtsmaßregeln gebraucht habe, um dasjenige, was eigentlich der Tatbestand ist, so adäquat als nur irgend möglich zu treffen, dann alles mögliche gemacht, alles mögliche gesagt wird, und dann diese Behauptungen als «echte anthroposophische Lehre» in die Welt hinaus- gesandt werden.",
      "Zu diesen Behauptungen gehört, ich hätte gesagt, «der Organismus eines alten Ägypters oder Grie- chen war ganz anders als der des modernen Menschen». Es reduziert sich das auf das Folgende. Ich sagte: Die moderne Vorstellungsart stelle sich zu stark vor, daß der Mensch als ganzes Wesen, bis ins Innere, im Grunde ge- nommen immer so gewesen sei, wie er heute ist, bis in eine gewisse sogar historische Zeit zurück.",
      "Ich pflege erst von da ab von «ganz anders», von Metamorphosen des Menschen als solchem zu sprechen, wo große Unterschiede vorliegen, wo der Mensch in gewisser Beziehung «ganz anders» wird: in vorhistorischen Zeiten. Aber derjenige, sagte ich, der auf die Feinheit in der Struktur bis in das innerste Gefüge einzugehen vermag - wie das wohl in der 153 Geisteswissenschaft der Mensch kann -, der findet, daß fortwährend ein Metamorphosieren des Menschen stattfin- det, daß also zum Beispiel der moderne Mensch sich vom Ägypter oder Griechen unterscheide.",
      "Selbstverständlich nicht in bezug auf äußere auffallende Eigenschaften, die so auffallend sind etwa wie äußere Physiognomie und dergleichen. Das ist ja wohl in der Frage gemeint, aber das ist nicht meine Meinung, denn in bezug auf die auf- fallenden Eigenschaften ist natürlich der moderne Mensch nicht «ganz anders» als der Ägypter.",
      "Aber in bezug auf feinere innere Strukturverhältnisse kommt zum Beispiel die Geisteswissenschaft zu folgendem. Sie muß sich sa- gen, daß seit dem ersten Drittel des 15. Jahrhunderts die Menschheit besonders dazu gekommen ist, abstrakt zu denken, immer mehr und mehr überzugehen zu den ab- strakten Gedankengängen.",
      "Das beruht auch im wesent- lichen auf einer anderen Struktur der Gehirnverhältnisse. Und durch die Methode der Geisteswissenschaft kann der Geistesforscher die Sache erkennnen. Dann stellt sich aller- dings heraus, daß es wirklich so ist, daß das Gehirn in den feinsten Strukturen sich seit der ägyptischen Zeit sehr wohl umgeändert hat.",
      "Das Gehirn des Ägypters war so beschaffen, daß er, nehmen wir das Beispiel, auch zu denen gehört hat, von denen Dr. Husemann gesprochen hat, daß auch der alte Ägypter keinen Sinn gehabt habe für die blaue Farbennuance und so weiter.",
      "Überhaupt kann man sehen: der Sinn für Abstraktion tritt auch in demselben Maße auf, wie sich aus der bloßen Dunkelheit das Blau herausnuanciert. Was da im Seelenleben auftritt, das ent- spricht eben durchaus auch einer physischen Metamorpho- sierung.",
      "Das ist außerordentlich wichtig, daß man für den Menschen nicht bloß bei jenen Grobheiten, sagte ich, stehenbleibt, die man dann sich vorlegt, wenn man nun 154 meinetwillen in lange Zeiträume, die vor der Geschichte liegen, zurückgeht. Sondern man muß sich beim Menschen, wenn man ihn als Menschheit betrachten will, auch wäh- rend des geschichtlichen Daseins an die feineren Struktur- Umänderungsverhältnisse halten.",
      "Frage: Es wäre interessant zu hören, in einer mehr intimeren Weise, wie diese Tatsache sich verhält. Nun, es ist tatsächlich gerade in diesen Tagen, sagen wir, auch durch diejenigen Dinge, die Dr. Husemann vor- gebracht hat, recht viel Intimes gesagt worden, wie sich diese Tatsache verhält.",
      "Und es könnte natürlich, wenn noch auf andere Tatsachenfelder eingegangen werden sollte, durchaus auch noch für diese anderen, sehr feineren, intimeren Strukturverhältnisse des Menschen manches gesagt werden. Frage: Wie erklärt man das Phänomen des bekannten Pferdes, das zum Erstaunen aller Gelehrten alle Rechenaufgaben und die mathe- matischen Aufgaben ohne Schwierigkeit löste, und erst dann voll- kommen versagte, als man ihm die Aufgaben vor dem Prüfenden auf Zettel schreiben ließ?",
      "Wenn es nun beim Pferd sich so verhält, daß keiner der im Räume Anwesenden die Aufgabe sehen konnte, beruht das auf einer starken Suggestivität des Tieres? Und wie kommt das zustande? Ich möchte niemals über etwas anderes sprechen als über dasjenige, was ich selber untersucht habe.",
      "Und daher möchte ich in der Antwort auf diese Frage auch nur geben, was ich selber erlebt habe. Ich kenne zum Beispiel die be- rühmten Elberfeider Pferde nicht. Ich kenne auch nicht den Hund Rolf, habe nie die Ehre gehabt, ihn kennenzulernen.",
      "Nun, mit Bezug auf solche Sachen konnte ich immer kon- statieren, daß die Geschichte um so wunderbarer ist, je weniger man in die Verlegenheit kommt, sie wirklich zu durchschauen, sie wirklich kennenzulernen. Aber das Pferd 155 des Herrn von Osten habe ich einstmals gesehen in Berlin.",
      "Ich kann nicht gerade sagen, daß die Rechenaufgaben, die der Herr von Osten dem Pferd vorlegte, so außerordent- lich komplizierte waren. Aber ich konnte mir aus dem, was da vorging wozu man allerdings einzig genau hin- zuschauen brauchte , eine augenblickliche Vorstellung von dem machen, um was es sich eigentlich handelt.",
      "Ich konnte mich allerdings nur wundern darüber, welch merkwürdige Theorien über diese Dinge aufgeworfen worden sind. Es war da ein Dozent, ich glaube Fox oder so ähnlich heißt er, der sollte nun auch diese ganze Ge- schichte mit dem Pferd prüfen; und er stellte nun die Theorie auf, daß jedesmal, wenn der Herr von Osten irgendeine Aufgabe gebe, ganz furchtbar kleine Bewegun- gen im Auge oder irgend etwas dergleichen zustande kämen.",
      "Eine andere kleine Bewegung käme zustande, wenn der Herr von Osten «drei» sagt so, oder wenn er es mal so sagt; eine andere Bewegung käme zustande, wenn er «zwei» ausspreche. So daß also eine gewisse feine Bewegungsreihe zustande käme, wenn Herr von Osten sagte, «drei mal zwei»; dann käme wieder das gleiche Zeichen dieser Bewegung, sechs!",
      "Und das Pferd des Herrn von Osten sollte nun ganz besonders dazu veranlagt sein, diese feinen Bewegungen - von denen der betreffende Dozent sagte, daß er sie nicht irgendwie wahrnehme, son- dern daß er sie nur hypothetisch voraussetze - zu erraten. Also es beruhte schließlich die ganze Theorie doch darauf, daß das Roß des Herrn von Osten viel gescheiter war in der Wahrnehmung, in einem viel stärkeren Maße in der Wirklichkeit, als der Herr Dozent, der diese Theorie auf- stellte.",
      "Man kann, wenn man sich an das blitzblaue Denken im Hypothesenaufstellen hält, Hypothesen in der aller- 156 verschiedensten Weise aufstellen. Für den, der in solche Sachen ein bißchen hineinschauen kann, hatten manche Umstände einen außerordentlich großen Wert, nämlich während der ganzen Zeit, während welcher der Herr von Osten dem staunenden Publikum seine Versuche vorführte mit seinem Roß, gab er - er hatte riesige Taschen da rückwärts drinnen im Rock dem Pferd lauter Süßigkei- ten.",
      "Und das Pferd schleckte eben fortwährend, und so löste es diese Aufgaben auf. Nun denken Sie sich, daß dadurch ein ganz anderes Seelenverhältnis besteht zwischen dem Roß und dem Herrn von Osten selber. Wenn der Herr von Osten dem Pferd fortwährend Zucker gibt, entsteht ein ganz beson- deres Verhältnis der Liebe, der Innigkeit der Beziehungen.",
      "Nun ist die tierische Natur so, daß sie außerordentlich stark variabel ist durch die Innigkeit der Beziehung, die sich herausbildet, sowohl vom Tier zum Menschen wie auch vom Menschen zum Tier. Und da kommen dann Wirkungen zustande, die tatsächlich falsch bezeichnet wer- den, wenn man sie ein «Gedankenlesen» nennt, in dem Sinne, wie das Wort trivial oftmals aufgefaßt wird, aber die doch Vermittler sind für dasjenige, was keine «feinen Zuckungen» sind, die ein Privatdozent hypothetisch auf- stellt, von denen er aber selbst sagt, daß er sie nicht sieht!",
      "Zur Vermittlung der Lösungen braucht es keine feinen Zuckungen. Sie ist auf folgendes zurückzuführen: denken Sie sich, was in dem Herrn von Osten vorging, indem er natürlich die Eitelkeit hatte, daß im Publikum, sensations- lüsternen Leuten, die Spannung, in der es da stand, die unglaublichsten Kurven durchmachte, wenn er das be- merkte, und wenn er dann stand vor der Lösung der Auf- gabe, so gab er dem Pferd ein Stück Zucker.",
      "Und nehmen Sie noch dazu, was durch das seelische Verhältnis auf das 157 Pferd wirkte. Es war wirklich ein nicht durch Worte oder durch Zuckungen, sondern allerdings intim erteilter Be- fehl, der immer von Herrn von Osten an das Pferd aus- ging, wenn er ihm von den Süßigkeiten zu fressen gab.",
      "Suggestion ist wohl nicht das richtige Wort. Beziehungen, die zwischen Mensch und Mensch stattfinden, dürfen nicht auf jedes Lebewesen übertragen werden. Diese Dinge habe ich einmal im Konkreten zu zeigen versucht, indem ich Ihnen einen Umstand, den viele als nebensächlich ansehen werden: das fortwährende Zucker- geben eben als etwas außerordentlich Wesentliches hervor- heben mußte.",
      "Frage: Besteht die Möglichkeit, für das Gebiet der Mineralogie und Kristallogie auf einen ebenso die Systematik belebenden Gesichtspunkt hinzuweisen, wie ein solcher für die Botanik gegeben ist mit der Idee der Urpflanze oder für die Chemie bei einem neuartigen Auf- fassen des periodischen Systems der Elemente? Wir haben es allerdings, wenn wir von Kristallformen sprechen, ich meine jetzt nicht von den durch Konstruk- tionen hinzugekommenen, sondern von den realen Kri- stallformen, mit Formen zu tun, welche real anders sind in ihrem ganzen Verhältnisse zum Kosmos, in ihrer gan- zen Stellung in der Welt, als die Formen, die man sich in der Urpflanze und wiederum in den von der Urpflanze abgeleiteten, sagen wir also, Pflanzengestalten in der Möglichkeit des realen Bestehens vorstellen kann.",
      "Es könnte zum Beispiel durchaus nicht das Prinzip, welches angewendet wird für die Ausgestaltung der Urpflanze, auf das Gebiet der Mineralogie oder der Kristallogie an- gewendet werden. Denn man hat es da zu tun mit etwas, dem man sich von einer ganz anderen Seite her nähern muß.",
      "Und zwar muß man sich ihm zunächst dadurch nähern, daß man eigentlich erst an das Gebiet der poly- 158 edrischen Kristallformen heranrückt. Und dieses Heran- rücken, ich kann es jetzt nur andeuten. Ich habe es einmal in einem Vortragskurs, den ich für einen kleineren Kreis gehalten habe, genauer ausgeführt in seinen einzelnen Darstellungen.",
      "Dieses Annähern, das trifft man, wenn man ausgeht von der Betrachtung, einer innerlichen dyna- mischen Betrachtung des Aggregatzustandes, sagen wir zu- nächst vom gasförmigen Zustand nach abwärts zum festen. Ich kann jetzt nur die Linien ziehen, es würde zu lang dauern, wenn ich es im einzelnen ausführen sollte, aber ich will es andeuten.",
      "Wenn man hinabsteigt - wenn ich mich so ausdrücken darf - vom gasförmigen Aggregat- zustand zum flüssigen, so muß man sagen: der flüssige Aggregatzustand, der zeigt sich darin, daß einem bei ihm, als das ihm im ganzen Zusammenhalt der Natur Ange- messene, eine Niveaubegrenzungsoberfläche entgegentritt, welche eine Kugelfläche ist, und deren Krümmungsmaß von irgendeinem Punkt der Oberfläche man vom Über- gang zu der Tangente an diesem Punkt bekommt. Was man da bekommt also, das schließt ein die Form, die ihren äußeren Umfang in der Kugelfläche hat, und einen Punkt im Inneren, der von dieser Kugelfläche überallhin gleich weit absteht.",
      "Denkt man sich nun den Tropfen in unbegrenzter Art, ich sage nicht in unendlicher, sondern in unbegrenzter Art vergrößert, so bekommt man eine sich der Horizontalen nähernde Niveaufläche, und man hat gewisse Verhältnisse im Sinne der auf diese Niveaufläche Senkrechten zu be- urteilen. Dieselbe Vorstellung aber bekommt man heraus, indem man die Zusammenhänge betrachtet, die sich ergeben, wenn man unsere Erde einfach als einen Kraftzusammen- hang ansieht, der die Gegenstände der Umgebung, die 159 nicht fest mit ihr verbunden sind, anziehen kann.",
      "Wenn man die Erde nicht als Gravitationsmittelpunkt, sondern als Gravitations-Kugeloberfläche betrachtet, dann ergibt sich für diese, ich möchte sagen, Gravitationsfigur ganz dasselbe, was man in anderer Beziehung braucht für die materielle Konstitution des Tropfens. Man bekommt also für einen reinen Kraftzusammenhang etwas, was ent- spricht einem materiellen Zusammenhange.",
      "Und man kommt auf diese Weise zu einer Möglichkeit, Formver- hältnisse im Anorganischen zu studieren. So daß man also sagen kann, in diesem Kräftezusam- menhang, der einem im ganzen Erdkörper vorliegt, hat man es immer zu tun mit der Horizontal-Niveauebene.",
      "Geht man von diesem Kräftezustand nun zu einem sol- chen über, bei dem, sagen wir, in der Mitte nicht ein Punkt wäre, auf den sich die Niveaufläche so bezieht wie beim Tropfen auf den einen Mittelpunkt, sondern mehrere Punkte, so würde man eine merkwürdig zusammengesetzte Oberfläche finden. Diese Beziehungen der Linie auf diese «Mittelpunkte» müßte ich im Diagramm etwa in der fol- genden Weise zeichnen: Aber geht man jetzt dazu über - und jetzt mache ich einen großen Sprung, der allerdings gut begründet ist, aber ich kann ja jetzt in der kurzen Zeit nur hindeuten auf den wahren Inhalt -, geht man dazu über, diese 160 Punkte nicht innen anzunehmen, innerhalb des Systems, mit dem man es zu tun hat, sondern außerhalb, dann würde man vielleicht eine Zeichnung bekommen, die man diagrammatisch in der folgenden Weise machen kann: Verlegt man die Punkte in unermeßliche Weiten, nicht in unendliche Weiten, sondern in sehr große Weiten, dann gehen diese gekrümmten Flächen, die hier durch die ge- krümmten Linien, durch die Kurven, angedeutet sind, in Ebenen über, und wir würden eine polyedrische Form bekommen, welche sich dem nähert, was wir in den be- kannten Kristallgestalten vor uns haben.",
      "Und in der Tat führt uns die geisteswissenschaftliche Betrachtung dazu, den Kristall in einer solchen Weise an- zusehen, so daß wir ihn nicht bloß etwa aus gewissen inneren figurierenden Kräften in irgendeiner materiellen Substanz ableiten, sondern daß wir ihn auf das Äußere des Kosmos beziehen, und daß wir im Kosmos die Rich- tungen suchen, die dann durch die Verteilung ihrer Aus- gangspunkte eben das ergeben, was die einzelne Kristall- form ist. Wir bekommen in der Tat in der einzelnen Kristallform gewissermaßen Abdrücke großer kosmischer Verhältnisse.",
      "Das alles will im einzelnen studiert sein. Ich fürchte, es erscheine Ihnen schon als etwas sehr Wag- halsiges, was ich jetzt, allerdings nur in einzelnen, ganz 161 spärlichen Linien, andeuten konnte. Aber man muß eben schon sagen, daß sich heute die Menschen mit ihrer Vor- stellungswelt in einem sehr engen Gebiete eingekapselt haben, und daß es ihnen deshalb so unbehaglich wird, wenn man nicht bei der Begriffswelt bleibt, die gewöhn- lich heute zugrunde gelegt wird, ich möchte sagen, in allen Wissenschaften zugrunde gelegt wird.",
      "Geisteswissenschaft fordert eben eine - wie es ja die Erfahrung notwendig macht gegenüber dem heutigen Zustand unermeßliche Erweiterung der Begriffe. Und das ist eben manchem un- behaglich. Er sieht sozusagen nicht das Ufer, glaubt, ins Uferlose zu kommen.",
      "Er würde aber merken, daß man dasjenige, was man durch die Weite verliert, doch wieder- um als eine gewisse innere Festigkeit und Sicherheit ge- winnt, so daß man sich nicht so stark zu fürchten braucht vor dem, was da wie eine Erweiterung ins Uferlose auf- tritt. Es ist natürlich viel einfacher, sich irgendein Modell zu machen - wie es heute auch erwähnt worden ist in einer bestimmten Frage , als zu solchen Vorstellungen vorzu- rücken.",
      "Es ist leichter zu sagen: Das Wahre muß einfach sein! - Der Grund, warum man sagt, das Wahre muß einfach sein, ist nämlich nicht der, daß das Wahre wirklich einfach sein muß, denn der menschliche Organismus ist zum Beispiel in unermeßlichster Weise kompliziert. Sondern der Grund, warum man sagt: Das Wahre muß einfach sein! - ist, daß das Einfache bequem ist im Denken.",
      "Das ist der ganze Witz. Und das ist eben nötig, daß man zum Inhaltsvolleren vor allem vorrückt, wenn man nach und nach die Wirklichkeit wirklich begreifen will. Die Frage, die hier noch aufgeworfen worden ist, er- forderte, daß man drei Stunden Theorie vortragen müßte.",
      "Über die Sonne kann man nicht durch «eine kurze Beant- 162 wortung der Frage» sprechen, weil man eben vollständig mißverstanden würde. Und das möchte ich nicht. - So sind ja zunächst die beantwortbaren Fragen notdürftig beantwortet.",
      "Frage: Findet Geisteswissenschaft eine Umwandlung der materiellen Erde mit dem Einzüge des Christus-Geistes in die Erde? Drückt sich die Wirkung der Christus-Kraft in einem der in der neueren Zeit gefundenen Elemente vielleicht besonders aus?",
      "Was soll die Frage? - Nicht wahr, man muß nur be- denken, von welchem Gesichtspunkt aus eine solche Frage gestellt sein kann. Es ist die Frage gestellt: Drückt sich in der materiellen Erde die Wirkung der Christus-Kraft aus? - Sie müssen nur bedenken, daß doch für die Geistes- wissenschaft aus ihrer Forschung heraus eine ganz be- stimmte Vorstellung vorliegt über die Erde, die nicht zusammentrifft mit dem, was man sich von der Erde vor- stellt, wenn man im Sinne des heutigen Wortes «materiell» von der «materiellen Erde» spricht.",
      "Es ist also eigentlich die Frage ohne einen wirklichen Inhalt. Wenn man von so etwas wie einer «Einwirkung der Christus-Kraft auf die Erde» spricht, so muß man da wiederum diese Vor- stellung gewissermaßen der Geisteswissenschaft entlehnt ist - dann auch über die Erde diejenige Vorstellung haben, welche für die Anthroposophie, für die Geisteswissen- schaft gilt.",
      "Und wie da die Christus-Kraft in einem ge- wissen Verhältnisse steht zu der ganzen Metamorphose der Erde, das läßt sich auch wiederum nur darstellen im ganzen Zusammenhang, den ich in der «Geheimwissen- schaft im Umriß» gegeben habe. Und dort findet man dann auch das Nötige zur Beantwortung desjenigen, was mit dieser Frage gemeint ist, wenn sie richtig formuliert wird. 163 Auf Wunsch vieler Kursteilnehmer gibt darauf ein Stuttgarter Herr einen kurzen Bericht über den am Abend vorher vom alldeutschen General v.",
      "Gleich in einer Stuttgarter Massenversammlung gehaltenen Vortrag über «Rudolf Steiner als Prophet einer bedenklichen Lehre» (siehe den Hinweis Rudolf Steiners darauf am Schluß des Vormit- tagvortrags, S. 139/140). Ich möchte nur das eine einfügen, daß besagter General v.",
      "Gleich ziemlich lang vorher, wochenlang vorher, bevor er zu seinem Vortrag und zur Abfassung seiner Broschüre geschritten ist, einen Brief an unseren Freund Herrn Molt richtete, als besorgter Vater, besorgt über das Unglück, daß er, als Besitzer eines vierzigjährigen Adels, seinen Sohn nicht nur «abgegeben» hat an die Anthroposophie, sondern auch an eine vollständig unadelige Dame, die Anthroposophin ist! Als besorgter Vater schrieb er an unseren Freund Molt, er möge ihn besuchen.",
      "Herr Molt tat das auch, sagte aber, daß er mit ihm nichts anzu- fangen wisse. Namentlich sah er das aus dem Umstand, daß Herr v. Gleich die Forderung aufstellte, wir «von der Dreigliederungsbewegung» sollten den bei uns ange- stellten Sohn des Herrn General v.",
      "Gleich künftighin so schlecht honorieren, daß der junge Mann nicht imstande sei, sich zu verheiraten, wir sollten wenigstens durch dieses schlechte Honorieren den General v. Gleich vor dieser Heirat seines Sohnes schützen. - Nach diesen Vorgängen war es begreiflich, daß man von dem Vortrag des Gene- rals v.",
      "Gleich nicht gerade das Beste erwarten konnte. Wir sahen dann tatsächlich auch die schlimmsten Erwar- tungen übertroffen! Es war bei diesem Vortrag so, daß Gleich im wesentlichen den Inhalt einer Broschüre vorge- bracht hat - noch etwas saftiger, sagen wir, ausgestattet -, die zugleich in Ludwigsburg erschien.",
      "Es war das eben schon ausgemacht, daß diese Broschüre zugleich erscheinen sollte mit dem Vortrag. In dieser Broschüre bringt er in 164 der unorientiertesten Weise, ohne irgendwie Beweise für das, was er sagt, zu liefern davon kann sich jeder über- zeugen, der diese Broschüre liest -, gegen Anthroposophie verschiedenes vor, indem er eigentlich nur die Gegner der Anthroposophie benützte.",
      "Es geht das schon aus dem Inhaltsverzeichnis der Broschüre hervor: einige Hinweise auf die Literatur, wo man sich über die Anthroposophie informieren kann. Das wären zunächst die anthroposophi- schen Bücher, sollte man denken.",
      "Aber nein, da stehen zirka zwanzig Gegner, und zwar der allerschofelste gleich vor- an: Max Seiling! v. Gleich bringt im wesentlichen nichts anderes, als was man bei allen Gegnern in der Art der Broschüre von Seiling finden kann, nur noch in der Art und Weise, wie eben der General v.",
      "Gleich seinen Vortrag zu halten pflegte. Und es war so, daß dieser Vortrag «ohne Diskussion» angesagt war. Es waren zahlreiche An- hänger der anthroposophischen Bewegung drinnen. Nach- dem er ihn zu Ende gesprochen hatte, den Vortrag, der in den allerschärfsten Ausdrücken, teilweise mit den gröb- sten Verleumdungen vorging, verließ er einfach, ohne auf irgendeine Diskussion einzugehen, den Saal.",
      "Und als man versuchte, darauf zu Wort zu kommen, und als Herr Molt, der da war und auch in dem Vortrag mehrfach persönlich angegriffen wurde, rief: Er erkläre hiermit öffentlich - er rief das in den Saal hinein, in dem sich eine tobende Menge der Anhänger des Herrn v. Gleich befand -, er erkläre den Herrn v.",
      "Gleich öffentlich als einen Lügner und spreche ihm öffentlich seine Ehre ab - fand Herr v. Gleich es nicht der Mühe wert, irgend etwas zu ant- worten. Er hatte bereits den Saal verlassen. Dagegen ver- suchten die Anhänger, die mit Pfeifen und anderen Lärm- instrumenten ausgerüstet waren, die Anthroposophen, die dagegen etwas vorbringen wollten, niederzuschreien.",
      "Und 165 es war ziemlich nahe an einer Schlägerei. Es war ja auch sehr schwer möglich, auch nur mit Zwischenrufen gegen die schwersten Verleumdungen zu protestieren, da die ganze Versammlung sofort einen bedrohlichen Charakter annahm, und man sah, daß es zu einer Prügelei kommen würde.",
      "Es folgten einige Berichte über den vorangegangenen Vortrag v. Gleichs in Ludwigsburg. Schließlich wurde ein von General v. Gleich an seinen Sohn gerichteter Brief vorgelesen. Ich möchte nur noch ein paar Worte sagen.",
      "Kann ich diesen Brief nochmals haben? Ich möchte nur eine formale Bemerkung machen, eine Bemerkung, die ja nicht die Sache selbst betrifft. Da steht also in dem Brief des Herrn v. Gleich an seinen Sohn: «...",
      "Wollte Gott, Du wärst als anständiger christlicher Adliger fürs Vaterland gefallen, dann könnte ich wenigstens in Stolz um Dich trauern ... Ich bitte zu Gott, die Verblendung wieder von Dir zu nehmen, daß Du aus ihr wieder erwachen mögest...» (Lücke in der Nachschrift.) Sie sehen, es ist viel über die eigene Christlichkeit des Herrn v.",
      "Gleich gesagt; ich möchte dies betonen: die eigene Christlichkeit, zum Vergleich mit der Zumutung, die an uns gestellt worden ist, den Sohn so schlecht zu bezahlen, daß er nun ja nicht heiraten kann. Das scheint mir eine recht christliche Tat zu sein!",
      "Und ich möchte jetzt nicht durch diese «kleinen Pikanterien», die ja auch in diesem Programm sind, wegführen etwa über den Ernst der Lage. Denn ich weiß sehr gut, daß dasjenige, was gestern in Stuttgart geschehen ist, nicht etwa ein Ende ist, sondern ein Anfang, daß dahinter eine starke Organisation steht.",
      "Und gerade aus diesem Gefühl heraus darf ich wohl einer solchen Persönlichkeit, wie sie eben gesprochen hat - aus einem wirklichen inneren Gefühl für dasjenige, was An- 166 throposophie wenigstens sein möchte -, herzlichst danken. Ich möchte aber durchaus hinweisen auf den Ernst der Situation und auf die Notwendigkeit, im Sinne dieser ernsten Situation sich zu verhalten.",
      "Was ich sagen möchte, das muß natürlich unterschieden werden von einem gewissen Verständnisse, das man im- merhin auch solchen Christen gegenüber haben kann, wie zum Beispiel der Herr General v. Gleich ein Christ ist!",
      "Ich will ja nicht einen Vergleich, nicht einen formellen Vergleich machen, sondern ich möchte nur etwas sagen, an das ich mich bei dieser Art von Christlichkeit erinnern mußte. Es gibt nämlich ganz verschiedene Arten von Christlichkeit, sogar von orthodoxem Christentum.",
      "Als der Kriminalanthropologe Moritz Benedikt daran ging, in der Kriminalanthropologie zu arbeiten und zu schreiben, fand er zunächst in Wien wenig Verständnis. Er fand dann bei einem Anstaltsleiter für Schwerverbrecher in Ungarn außerordentliches Verständnis.",
      "Es wurde ihm die Möglichkeit gegeben, Verbrecherschädel zu untersuchen, auch von den schwersten ungarischen Verbrechern die Schädel zu untersuchen. Unter diesen waren die merk- würdigsten Leute, unter anderem auch ein ganz ausge- prägter orthodoxer Christ, welcher sich zwar freilich nicht dem Professor Benedikt gegenüber seinen christlichen In- tentionen gemäß verhalten konnte.",
      "Über den war er sehr wütend, weil er seinen Schädel untersuchen durfte. Und ganz besonders war er darüber wütend, weil er gehört hatte, daß der Gefängnisdirektor damit einverstanden war, daß der Professor Benedikt besonders charakteristi- sche Verbrecherschädel nach dem Tode werde zu studieren bekommen.",
      "Und da er in dieser Anstalt nicht in Freiheit auf den Professor Benedikt losgelassen wurde, so wollte er wenigstens gefesselt diesem Benedikt vorgeführt wer- 167 den. Bei dieser Vorführung sagte er, er könne durchaus nicht zugeben, daß er bei seiner christlichen Gesinnung es erlauben müsse, daß sein Schädel nach dem Tode dem Professor Benedikt nach Wien geschickt werde; er würde dann doch hier begraben werden, und sein Schädel werde in Wien herumliegen!",
      "Und er möchte wissen, wie nun bei der Auferstehung sein Leib und sein Schädel zusammen- gebracht werden sollen. So gut glaubte der an seine leib- liche Auferstehung - er war ein ganz richtiger Verbrecher, ich glaube sogar ein Mörder. 168"
    ],
    "sentences": [
      [
        "Die Fragen bezogen sich nicht auf das Thema des Tages «Sprach- wissenschaft», sondern griffen auf früher behandelte Probleme zurück.",
        "Steiner.",
        "Hier ist die Frage: Es ist gesagt, die drei Dimensionen des Raumes wären nicht gleich in ihrer Struktur - worinnen liegt der Unterschied?"
      ],
      [
        "Es ist jedenfalls der Satz in dieser Weise niemals ge- faßt worden: Die drei Dimensionen des Raumes seien «nicht gleich in ihrer Struktur», sondern dasjenige, auf das wahrscheinlich hier hingewiesen ist, ist das Folgende.",
        "Wir haben zunächst den mathematischen Raum, den Raum, den wir uns so vorstellen wenn wir uns über- haupt eine exakte Vorstellung davon machen -, daß wir uns drei aufeinander senkrecht stehende Dimensionsrich- tungen vorstellen, den wir uns also etwa definieren durch die drei aufeinander senkrecht stehenden Koordinaten- achsen."
      ],
      [
        "So wie wir gewöhnlich mathematisch diesen Raum be- trachten, ist eine absolute Gleichbehandlung der drei Di- mensionen vorhanden.",
        "Wir machen so sehr keinen Unter- schied zwischen den Dimensionen oben-unten, rechts-links, vorne-rückwärts, daß wir uns eventuell sogar diese drei Dimensionen als vertauschbar denken können."
      ],
      [
        "Es kommt schließlich beim bloßen mathematischen Raum gar nicht darauf an, ob wir, wenn wir die X-Achse und die Z-Achse aufeinander senkrecht stehend, und die Y-Achse darauf wieder senkrecht stehend haben, nun die Ebene, auf der die Y-Achse steht, oder ob wir diese Achse selbst «hori- 141 zontal» oder «vertikal» nennen oder dergleichen.",
        "Ebenso kümmern wir uns bei diesem Raum sozusagen nicht um seine Begrenztheit."
      ],
      [
        "Nicht etwa, daß wir ihn grenzenlos vorstellten.",
        "Bis zu dieser Vorstellung steigt man ja ge- wöhnlich nicht auf, sondern man stellt ihn so vor, daß man sich um seine Grenzen nicht kümmert, vielmehr still- schweigend die Annahme macht, man könne von jedem Punkte - sagen wir zum Beispiel der X-Richtung - aus- gehen und ein weiteres Stück an dasjenige, was man bereits nach der X-Richtung abgemessen hat, dazufügen, zu die- sem wieder ein Stück und so weiter, und man würde nie- mals veranlaßt sein, irgendwo ans Ende zu kommen."
      ],
      [
        "Gegen diese im Sinne der euklidischen Geometrie liegende Vorstellung vom Räume ist schon von Seiten der Meta- geometrie im Laufe des 19.",
        "Jahrhunderts manches aufge- stellt worden.",
        "Ich will nur daran erinnern, wie zum Bei- spiel Riemann unterschieden hat zwischen der «Unbe- grenztheit» des Raumes und der «Unendlichkeit» des Raumes."
      ],
      [
        "Und zunächst ist auch für das rein begriffliche Vorstellen gar keine Nötigung vorhanden, den Begriff der «Unbegrenztheit» und den der «Unendlichkeit» als iden- tisch anzunehmen.",
        "Nehmen Sie zum Beispiel eine Kugel- oberfläche."
      ],
      [
        "Wenn Sie auf eine Kugeloberfläche zeichnen, so werden Sie finden, daß Sie nirgends an eine Raum- grenze kommen, durch die Sie gewissermaßen im Fort- führen Ihrer Zeichnung gehindert werden können.",
        "Sie werden gewiß, wenn Sie weiterzeichnen, in Ihre letzte Zeichnung wieder hineinfahren; aber Sie werden niemals, wenn Sie auf der Kugeloberfläche bleiben, genötigt sein, sich durch eine Grenze im Zeichnen aufhalten zu lassen."
      ],
      [
        "So daß Sie sich also sagen können: Die Kugeloberfläche ist in bezug auf meine Fähigkeit, darauf zu zeichnen, unbegrenzt. - Aber niemand wird deshalb behaupten, daß 142 die Kugeloberfläche unendlich ist.",
        "Also man kann unter- scheiden, rein begrifflich, zwischen der Unbegrenztheit und der Unendlichkeit."
      ],
      [
        "Das kann nun unter gewissen mathematischen Voraus- setzungen auch auf den Raum ausgedehnt werden, kann so auf den Raum ausgedehnt werden, daß man sich vor- stellt: wenn ich in der X- oder Y-Achse eine Strecke dazu- setze, und dann wieder eine und so weiter, und da niemals gehindert werde, immer weitere Strecken anzusetzen, so könnte diese Eigenschaft des Raumes zwar für seine Unbegrenztheit sprechen, aber nicht für die Unendlichkeit des Raumes.",
        "Es brauchte trotz dieser Tatsache, daß ich immer neue Stücke anstückeln kann, der Raum durchaus nicht unendlich zu sein, er könnte unbegrenzt sein."
      ],
      [
        "Also diese beiden Begriffe müssen auseinandergehalten werden.",
        "So daß man also annehmen könnte, daß der Raum dann, wenn er zwar unbegrenzt, aber nicht unendlich wäre, in derselben Weise, als Raum aber jetzt, eine innerliche Krümmung hätte, daß er also in irgendeiner Weise ebenso in sich wiederum zurückkehren würde, wie eine Kugel- oberfläche in sich zurückkehrt."
      ],
      [
        "Gewisse Vorstellungen der neueren Metageometrie rech- nen durchaus mit solchen Annahmen.",
        "Niemand kann ei- gentlich sagen, daß gegen solche Annahmen sich sonderlich viel einwenden läßt; denn, wie gesagt, es gibt gar keine Möglichkeit, aus dem, was wir am Räume erfahren, etwa seine Unendlichkeit in irgendeiner Weise abzuleiten."
      ],
      [
        "Er könnte ganz gut in sich gekrümmt und dann endlich sein.",
        "Ich kann diesen Gedankengang natürlich nicht ausfüh- ren, denn er ist fast der durchgehende Gedankengang der ganzen neueren Metageometrie.",
        "Sie finden aber in Ab- handlungen von Riemann, Gauß und so weiter, die ja leicht erhältlich sind, genügend Anhaltspunkte, um, wenn 143 Sie auf solche mathematischen Vorstellungen Wert legen, auf sie einzugehen."
      ],
      [
        "Das ist also zunächst von der rein mathematischen Seite her das, was in den, ich möchte sagen starren, nach allen Seiten neutralen Raum der euklidischen Geometrie Ein- wände hineingebracht hat, die eben nur abgeleitet waren aus der «Unbegrenztheit».",
        "Aber dasjenige, auf das in der Frage hingedeutet wird, wurzelt noch in etwas anderem."
      ],
      [
        "Nämlich darinnen, daß der Raum, mit dem wir zunächst rechnen und der uns zum Beispiel in der analytischen Geometrie vorliegt, wenn wir uns eben mit den drei auf- einander senkrecht stehenden Koordinatenachsen zu tun machen, daß der Raum zunächst ein Abstraktum ist, eine Abstraktion.",
        "Und eine Abstraktion - aus was?"
      ],
      [
        "Das ist die Frage, die noch zuerst aufgeworfen werden muß.",
        "Es handelt sich darum, ob man bei dieser Abstraktion «Raum» stehenzubleiben hat, oder ob das nicht der Fall ist.",
        "Hat man bei dieser Abstraktion des Raumes stehenzu- bleiben?"
      ],
      [
        "Ist das der einzige Raum, von dem man sprechen kann?",
        "Besser gesagt: Ist dieser abstrakte Begriff des Rau- mes der einzige, von dem man berechtigterweise sprechen kann, dann kann man eigentlich nur das eine einwenden, dasjenige, was eben in der Riemannschen oder einer an- deren Metageometrie genügend eingewendet wird."
      ],
      [
        "Die Sache liegt ja so, daß zum Beispiel die Kantschen Raum- definitionen durchaus auf dem ganz abstrakten Raumbe- griff, bei dem man sich um Unbegrenztheit oder Unend- lichkeit zunächst nicht kümmert, aufgestellt sind, und daß dann im Laufe des 19.",
        "Jahrhunderts auch innerlich, in bezug auf seinen Vorstellungsgehalt, dieser Raumbegriff eben von der Mathematik erschüttert worden ist."
      ],
      [
        "Es kann keine Rede davon sein, daß etwa die Kantschen Defini- tionen auch noch gelten würden für einen Raum, der zwar 144 nicht unendlich, aber unbegrenzt ist.",
        "Überhaupt würde da noch manches im weiteren Verlaufe der «Kritik der reinen Vernunft», die Paralogismenlehre zum Beispiel, ins Wan- ken kommen, wenn man eben genötigt wäre, überzugehen zu dem Begriff des unbegrenzten, in sich gekrümmten Raumes."
      ],
      [
        "Ich weiß ja, daß für das gewöhnliche Vorstellen dieser Begriff des gekrümmten Raumes Schwierigkeiten macht.",
        "Allein vom rein mathematisch-geometrischen Standpunkte aus läßt sich gegen das, was da angenommen ist, nichts anderes einwenden, als daß man sich eben in einem zu- nächst ganz wirklichkeitsfernen Gebiet der reinen Ab- straktion bewegt."
      ],
      [
        "Und wer genauer zusieht, wird finden, daß in den Ableitungen moderner Metageometrie im Grunde genommen ein merkwürdiger Circulus liegt.",
        "Es ist dieser, daß man zunächst ausgeht von dem Vorstellen der euklidischen Geometrie, die sich also nicht kümmert um eine Begrenztheit des Raumes."
      ],
      [
        "Daraus bekommt man dann gewisse abgeleitete Vorstellungen, also sagen wir Vorstellungen, die sich eben auf so etwas wie eine Kugel- fläche beziehen.",
        "Und dann kann man wiederum, indem man mit den Formen, die sich da ergeben, gewisse Relegie- rungen oder Umdeutungen vornimmt, von da aus Inter- pretationen des Raumes machen."
      ],
      [
        "Man sagt alles eigentlich unter Voraussetzung der euklidischen Koordinatengeome- trie.",
        "Man bekommt unter dieser Voraussetzung ein ge- wisses Krümmungsmaß heraus.",
        "Man kommt bis zu den Ableitungen.",
        "Alles durchaus mit den Vorstellungen der euklidischen Geometrie."
      ],
      [
        "Dann aber wendet man sozusagen um: man benützt nun diese Vorstellungen, die sich erst mit Hilfe der euklidischen Geometrie ergeben können, also zum Beispiel das Krümmungsmaß, um nun wiederum zu einer anderen Vorstellung zu kommen, die zu einer Rele- gierung führen und für das von den krummen Formen Gewonnene eben wiederum eine Deutung ergeben kann.",
        "Im Grunde genommen bewegt man sich da in einem wirk- lichkeitsfremden Gebiet, indem man Abstraktionen aus Abstraktionen herausholt."
      ],
      [
        "Berechtigt wäre die Sache nur dann, wenn empirische Tatbestände notwendig machten, sich mit dem, was man durch so etwas herausbekommt, nach den Vorstellungen dieser Tatbestände zu richten.",
        "Es handelt sich also darum: Wo liegt das Erfahrungs- gemäße für dasjenige, was die Abstraktion «Raum» ei- gentlich ist?"
      ],
      [
        "Denn der Raum als solcher, wie er bei Euklid vorgestellt wird, ist eine Abstraktion.",
        "Worinnen liegt das, was erlebbar, was wahrnehmbar ist?",
        "Da müssen wir zunächst sagen: Wir müssen von der menschlichen Erfahrung des Raumes ausgehen."
      ],
      [
        "Der Mensch, hineingestellt in die Welt, nimmt durch seine eigene Tätigkeit der Erfahrung eigentlich nur eine Raum- dimension wirklich wahr, und das ist die Tiefendimension.",
        "Dieses Wahrnehmen, dieses erarbeitete Wahrnehmen der Tiefendimension durch den Menschen beruht auf einem Bewußtseinsvorgang, der sehr häufig nicht beachtet wird."
      ],
      [
        "Allein dieses erarbeitete Wahrnehmen ist doch etwas ganz anderes als die Vorstellung des Ebenenmäßigen, die Vor- stellung der Ausdehnung in zwei Dimensionen.",
        "Wenn wir mit unseren beiden Augen, also mit unserem Totalgesicht in die Welt sehen, so wissen wir nie etwas davon, daß diese zwei Dimensionen durch eine eigene Tätigkeit, durch ein Sich-mit-der-Seele-Betätigen zustande kommen."
      ],
      [
        "Sie sind sozusagen da als zwei Dimensionen.",
        "Während die dritte Dimension - wenn auch durchaus dies Tätige ge- wöhnlich nicht ins Bewußtsein herauf gehoben wird - durch eine solche gewisse Betätigung zustande kommt."
      ],
      [
        "Wir müs- sen uns eigentlich erst das Wissen, die Erkenntnis darüber 146 erarbeiten, wie tief im Räume darinnen, wie weit entfernt von uns irgendein Gebilde liegt.",
        "Die Ausdehnung der Fläche, die erarbeiten wir uns nicht, die ist durch die An- schauung gegeben."
      ],
      [
        "Aber durch unsere zwei Augen erarbei- ten wir uns tatsächlich die Tiefendimension.",
        "So daß die Art und Weise, wie wir die Tiefendimension erleben, zwar hart an der Grenze des Bewußten und des Unbe- wußten liegt; aber wer gelernt hat, auf solche Sachen seine Aufmerksamkeit zu richten, der weiß, daß die halb unbe- wußt oder dritteis unbewußt, nirgends bewußt, zustande kommende Tätigkeit der Abschätzung der Tiefendimen- sion viel mehr einer Verstandes-, überhaupt einer seeli- schen Tätigkeit, einer aktiven Seelentätigkeit ähnlich ist als all dasjenige, was nur in der Ebene angeschaut wird."
      ],
      [
        "Es ist also die eine Dimension des dreidimensionalen Raumes schon für unser gegenständliches Bewußtsein tätig erobert.",
        "Und wir können nicht anders sagen als: Indem wir die Stellung des aufrechten Menschen betrachten, ist damit etwas gegeben in bezug auf diese Tiefendimension - vorne-rückwärts -, was nicht vertauschbar ist mit einer anderen Dimension."
      ],
      [
        "Denn einfach dadurch, daß der Mensch in der Welt dasteht und in einer gewissen Weise sich betätigend, diese Dimension erlebt, ist das, was er da erlebt, nicht mit irgendeiner anderen Richtung ver- tauschbar.",
        "Für den einzelnen Menschen ist diese Tiefen- dimension etwas, was mit einer anderen Dimension nicht vertauschbar ist."
      ],
      [
        "Es ist durchaus auch so, daß das Erfassen der Zweidimensionalität - also das oben-unten, rechts- links, natürlich auch wenn es vor uns ist - auch an andere Hirnpartien gebunden ist, da es im Sehvorgang, also im sinnlichen Anschauungsvorgang drinnen liegt; während mit Bezug auf die Lokalisation im Hirn das Zustande- kommen der dritten Dimension durchaus jenen Zentren naheliegt, die für die Verstandestätigkeit in Betracht zu ziehen sind.",
        "Also hier sehen wir schon, daß beim Zu- standekommen dieser dritten Dimension sogar in bezug auf das Erleben ein wesentlicher Unterschied ist gegenüber den zwei anderen Dimensionen."
      ],
      [
        "Steigen wir dann aber auf bis zur Imagination, dann kommen wir überhaupt heraus aus dem, was wir da in der dritten Dimension erleben: Wir gehen in der Imagina- tion eigentlich zur zweidimensionalen Vorstellung über.",
        "Und wir haben uns jetzt - allerdings ebenso leise ange- deutet wie das Erarbeiten der dritten Dimension im gegen- ständlichen Vorstellen auch die andere Vorstellung, die Vorstellung des rechts-links, noch zu erarbeiten; so daß da wiederum ein bestimmtes Erlebnis liegt im rechts-links."
      ],
      [
        "Und endlich: wenn wir zur Inspiration aufsteigen, so gilt dasselbe für das oben-unten.",
        "Für das gewöhnliche Vorstellen, das an unser Nerven- Sinnessystem gebunden ist, erarbeiten wir uns die dritte Dimension."
      ],
      [
        "Wenn wir uns aber mit Ausschaltung der gewöhnlichen Tätigkeit des Nerven-Sinnessystems direkt ans rhythmische System wenden - was in einer gewissen Beziehung beim Aufsteigen zur Imagination stattfindet, es ist das nicht ganz genau gesprochen, aber das tut für jetzt nichts , dann haben wir das Erleben der zweiten Dimension.",
        "Und das Erleben der ersten Dimension haben wir, wenn wir zur Inspiration aufsteigen, das heißt, wenn wir vorrücken bis zu dem dritten Glied der menschlichen Organisation."
      ],
      [
        "So erweist sich dasjenige, was wir im abstrakten Räume vor uns haben, als genau, weil wir ja alles, was wir uns in der Mathematik erobern, aus uns selbst herausholen.",
        "Was sich in der Mathematik ergibt als der dreifache Raum, das ist eigentlich etwas, was wir aus uns selbst heraus 148 haben."
      ],
      [
        "Steigen wir aber in uns hinunter durch die über- sinnlichen Vorstellungen, so ergibt sich nicht der abstrakte Raum mit seinen drei gleich gültigen Dimensionen, sondern es ergeben sich drei verschiedene Wertigkeiten für die drei verschiedenen Dimensionen: vorne-hinten, rechts-links, oben-unten; sie sind nicht miteinander vertauschbar.",
        "Daraus folgt noch ein anderes: Wenn diese drei nicht mit- einander vertauschbar sind, ist auch nicht nötig, sie sich mit der gleichen Intensität vorzustellen."
      ],
      [
        "Das ist das We- sentliche des euklidischen Raumes, daß wir die X-, Y-, Z-Achse - es ist das ja vorauszusetzen für jede Berechnung eines Geometrischen - mit gleicher Intensität vorstellen.",
        "Wenn wir die X-, Y-, Z-Achse uns vorhalten, so müssen wir - wenn wir bei dem bleiben wollen, was uns unsere Gleichungen sagen in der analytischen Geometrie, aber eine innere Intensität der drei Achsen annehmen - diese Intensität gleichwertig vorstellen."
      ],
      [
        "Wenn wir etwa die X-Achse elastisch vergrößern würden mit einer gewissen Intensität, so müßten sich die Y- und Z-Achsen mit glei- cher Intensität vergrößern.",
        "Das heißt, wenn ich dasjenige, was ich ausdehne, nun intensiv fasse, so ist die Kraft des Ausdehnens, wenn ich so sagen darf, für die X-, Y-, Z-Achse, also für die drei Dimensionen des euklidischen Raumes, gleich."
      ],
      [
        "Deshalb möchte ich - den Begriff Raum in dieser Weise natürlich anwendend - diesen Raum den starren Raum nennen.",
        "Nun, das ist nicht mehr der Fall, wenn wir den realen Raum nehmen, von dem dieser starre Raum eine Abstrak- tion ist, wenn wir den Raum nehmen, der auf die Weise gewonnen ist, daß er eben aus dem Menschen herausgeholt ist."
      ],
      [
        "Dann können wir nicht mehr davon sprechen, daß diese drei Ausdehnungsintensitäten gleich sind.",
        "Sondern im wesentlichen ist die Intensität abhängig von dem, was 149 sich am Menschen vorfindet: des Menschen Größenver- hältnisse sind durchaus das Ergebnis der Raumausdeh- nungsintensitäten."
      ],
      [
        "Und wir müssen zum Beispiel, wenn wir das oben-unten die Y-Achse nennen, uns diese mit einer größeren Ausdehnungsintensität vorstellen als zum Beispiel die X-Achse, die entsprechen würde dem rechts- links.",
        "Wenn wir nach einem formelhaften Ausdruck für diesen realen Raum suchen, wenn wir also wiederum, was da real gemeint ist, formelhaft ausdrücken würden - also wiederum Abstraktion; wir müssen uns nur bewußt blei- ben, daß diese Abstraktion eben eine Abstraktion ist -, bekämen wir dann ein dreiachsiges Ellipsoid."
      ],
      [
        "Nun liegt aber auch die Veranlassung vor, diesen drei- achsigen Raum, in dem das übersinnliche Vorstellen leben muß, in seinen drei ganz verschiedenen Ausdehnungsmög- lichkeiten so vorzustellen, daß wir mit dem realen X-, Y-, Z-Achsenerleben, das uns mit unserem physischen Körper gegeben ist, diesen Raum auch als dasjenige erkennen, was dann gleichzeitig das Wirkungsverhältnis der in diesem Raum befindlichen Weltenkörper zum Ausdruck bringt.",
        "Wenn wir uns das vorstellen, so müssen wir in einer gewissen Weise bedenken, daß auch alles, was wir uns da draußen in diesem dreidimensionalen Weltenraume denken, nach verschiedenen Richtungen hin nicht einfach mit gleicher Ausdehnungsintensität der X-, Y-, Z-Achse zu denken ist, wie das bei dem euklidischen Raum der Fall ist, sondern wir müssen uns denken, daß der Welten- raum an sich eine Konfiguration hat, die auch durch ein dreiachsiges Ellipsoid vorzustellen wäre."
      ],
      [
        "Und dafür spricht durchaus die Anordnung gewisser Sterne.",
        "Man nennt gewöhnlich unser Milchstraßensystem eine Linse und so weiter.",
        "Es ist durchaus nicht möglich, es sich als eine Kugelfläche vorzustellen; wir müssen es uns in einer 150 anderen Weise vorstellen, wenn wir schon bei einer rein physischen Tatsache bleiben."
      ],
      [
        "Sie sehen gerade bei der Behandlung des Raumes, wie wenig naturgemäß das neuere Denken ist.",
        "In den älteren Zeiten, den älteren Kulturen, hat sich niemand einer solchen Vorstellung hingegeben, wie es die des starren Raumes geworden ist."
      ],
      [
        "Man kann noch nicht einmal sagen, daß in der euklidischen Geometrie schon eine klare Vorstellung von diesem starren Räume mit den drei gleichen Aus- dehnungsintensitäten, auch den drei aufeinander senk- recht stehenden Linien, vorlag.",
        "Sondern erst, als man anfing den Raum Euklids rechnend zu behandeln - indem eben das Abstrahieren in der neueren Zeit ein wesent- licher Grundzug des Denkens geworden ist -, ist eigentlich diese abstrakte Vorstellung des Raumes entstanden."
      ],
      [
        "In älteren Zeiten hatte man durchaus ähnliche Erkenntnisse, wie ich sie jetzt eben wiederum aus der Natur des über- sinnlichen Erkennens heraus entwickelt habe.",
        "Sie können daraus ersehen, daß Dinge, auf die man heute so unend- lich stark baut, die man als Selbstverständlichkeit betrach- tet, im Grunde genommen eine solche Bedeutung nur aus dem Grunde haben, weil sie in einer wirklichkeitsfremden Sphäre spielen."
      ],
      [
        "Der Raum, mit dem man heute rechnet, ist eine Abstraktion; er spielt durchaus in einer wirklich- keitsfremden Sphäre.",
        "Er ist abstrahiert von Erfahrungen, von denen wir allerdings durch reales Erleben wissen kön- nen."
      ],
      [
        "Aber man begnügt sich heute vielfach mit dem, was Abstraktionen sind.",
        "In unserer Zeit, wo man so viel auf Empirie pocht, beruft man sich am alleröftesten auf Ab- straktionen.",
        "Und man merkt es nicht.",
        "Man glaubt, sich in der Wirklichkeit mit den Dingen zu bewegen."
      ],
      [
        "Aber Sie sehen, wie sehr unsere Vorstellungen in dieser Beziehung der Rektifizierung bedürfen.",
        "Der Geistesforscher fragt bei jeder Vorstellung nicht bloß, ob sie logisch ist.",
        "Logisch ist durchaus der Riemann- sche Raum auch, obwohl er in gewisser Beziehung nur eine Dependance des euklidischen Raumes ist; aber aus dem Grunde ist er im Vorstellen eigentlich doch nicht zu vollziehen, weil man zu ihm kommt mit einem ganz abstrakten Denken, indem man auf Grund einer Schluß- folgerung, zu der man gekommen ist, gewissermaßen mit seinem ganzen Denken umkippt."
      ],
      [
        "Der Geistesforscher fragt beim Vorstellen nicht bloß, ob es logisch ist, sondern ob es auch wirklichkeitsgemäß ist.",
        "Das ist für ihn das Ent- scheidende, eine Vorstellung anzunehmen oder nicht.",
        "Erst dann nimmt er eine Vorstellung an, wenn diese Vorstel- lung wirklichkeitsgemäß ist."
      ],
      [
        "Und dieses Wirklichkeitsgemäßsein wird als Kriterium gegeben sein, wenn man überhaupt einmal sachgemäß auf solche Vorstellungen eingehen wird, welches die Berechti- gung zum Beispiel von so etwas wie die Relativitätstheorie ist.",
        "Sie ist für sich, möchte ich sagen, weil sie sich nur inner- halb des Gebietes der logischen Abstraktion erfaßt, so lo- gisch, wie nur irgend etwas logisch sein kann."
      ],
      [
        "Es kann schon nichts logischer sein als die Relativitätstheorie!",
        "Aber die andere Frage ist diese, ob ihre Vorstellungen vollzieh- bar sind.",
        "Und da brauchen Sie nur die Vorstellungen, die dort als analoge aufgeführt werden, anzusehen, so werden Sie finden: Das sind eigentlich ganz wirklichkeitsfremde Vorstellungen, mit denen nur so herumgeworfen wird."
      ],
      [
        "Das sei nur zum Versinnlichen da -, sagt man zuvor.",
        "Aber es ist eben doch nicht nur zur Versinnbildlichung da.",
        "Sonst würde wiederum die ganze Prozedur in der Luft hängen.",
        "Das also möchte ich sagen über das, worauf sich die Frage bezieht."
      ],
      [
        "Sie sehen, es ist nicht möglich, Fragen, die auf solche Gebiete hingehen, so ganz leicht zu beantworten. 152 Nun liegt eine Frage vor in bezug auf den Satz: Der Organismus eines alten Ägypters oder Griechen war ganz anders als der des modernen Menschen.",
        "Sehr verehrte Anwesende, das habe ich selbstverständ- lich nicht gesagt!"
      ],
      [
        "Und da muß ich an dieser Stelle durch- aus auf etwas aufmerksam machen, auf das ich oftmals, und zwar wirklich nicht aus Unbescheidenheit aufmerk- sam mache: Ich pflege mich so genau, wie mir irgend mög- lich ist, auszudrücken.",
        "Und es ist eigentlich eine nicht gerade mir persönlich, da ist es ja zu ertragen, aber vom Gesichtspunkt der anthroposophischen Geistesbewegung - außerordentlich schmerzliche Tatsache, daß gegenüber mancherlei Dingen, zu deren Formulierung ich alle mög- lichen Vorsichtsmaßregeln gebraucht habe, um dasjenige, was eigentlich der Tatbestand ist, so adäquat als nur irgend möglich zu treffen, dann alles mögliche gemacht, alles mögliche gesagt wird, und dann diese Behauptungen als «echte anthroposophische Lehre» in die Welt hinaus- gesandt werden."
      ],
      [
        "Zu diesen Behauptungen gehört, ich hätte gesagt, «der Organismus eines alten Ägypters oder Grie- chen war ganz anders als der des modernen Menschen».",
        "Es reduziert sich das auf das Folgende.",
        "Ich sagte: Die moderne Vorstellungsart stelle sich zu stark vor, daß der Mensch als ganzes Wesen, bis ins Innere, im Grunde ge- nommen immer so gewesen sei, wie er heute ist, bis in eine gewisse sogar historische Zeit zurück."
      ],
      [
        "Ich pflege erst von da ab von «ganz anders», von Metamorphosen des Menschen als solchem zu sprechen, wo große Unterschiede vorliegen, wo der Mensch in gewisser Beziehung «ganz anders» wird: in vorhistorischen Zeiten.",
        "Aber derjenige, sagte ich, der auf die Feinheit in der Struktur bis in das innerste Gefüge einzugehen vermag - wie das wohl in der 153 Geisteswissenschaft der Mensch kann -, der findet, daß fortwährend ein Metamorphosieren des Menschen stattfin- det, daß also zum Beispiel der moderne Mensch sich vom Ägypter oder Griechen unterscheide."
      ],
      [
        "Selbstverständlich nicht in bezug auf äußere auffallende Eigenschaften, die so auffallend sind etwa wie äußere Physiognomie und dergleichen.",
        "Das ist ja wohl in der Frage gemeint, aber das ist nicht meine Meinung, denn in bezug auf die auf- fallenden Eigenschaften ist natürlich der moderne Mensch nicht «ganz anders» als der Ägypter."
      ],
      [
        "Aber in bezug auf feinere innere Strukturverhältnisse kommt zum Beispiel die Geisteswissenschaft zu folgendem.",
        "Sie muß sich sa- gen, daß seit dem ersten Drittel des 15.",
        "Jahrhunderts die Menschheit besonders dazu gekommen ist, abstrakt zu denken, immer mehr und mehr überzugehen zu den ab- strakten Gedankengängen."
      ],
      [
        "Das beruht auch im wesent- lichen auf einer anderen Struktur der Gehirnverhältnisse.",
        "Und durch die Methode der Geisteswissenschaft kann der Geistesforscher die Sache erkennnen.",
        "Dann stellt sich aller- dings heraus, daß es wirklich so ist, daß das Gehirn in den feinsten Strukturen sich seit der ägyptischen Zeit sehr wohl umgeändert hat."
      ],
      [
        "Das Gehirn des Ägypters war so beschaffen, daß er, nehmen wir das Beispiel, auch zu denen gehört hat, von denen Dr.",
        "Husemann gesprochen hat, daß auch der alte Ägypter keinen Sinn gehabt habe für die blaue Farbennuance und so weiter."
      ],
      [
        "Überhaupt kann man sehen: der Sinn für Abstraktion tritt auch in demselben Maße auf, wie sich aus der bloßen Dunkelheit das Blau herausnuanciert.",
        "Was da im Seelenleben auftritt, das ent- spricht eben durchaus auch einer physischen Metamorpho- sierung."
      ],
      [
        "Das ist außerordentlich wichtig, daß man für den Menschen nicht bloß bei jenen Grobheiten, sagte ich, stehenbleibt, die man dann sich vorlegt, wenn man nun 154 meinetwillen in lange Zeiträume, die vor der Geschichte liegen, zurückgeht.",
        "Sondern man muß sich beim Menschen, wenn man ihn als Menschheit betrachten will, auch wäh- rend des geschichtlichen Daseins an die feineren Struktur- Umänderungsverhältnisse halten."
      ],
      [
        "Frage: Es wäre interessant zu hören, in einer mehr intimeren Weise, wie diese Tatsache sich verhält.",
        "Nun, es ist tatsächlich gerade in diesen Tagen, sagen wir, auch durch diejenigen Dinge, die Dr.",
        "Husemann vor- gebracht hat, recht viel Intimes gesagt worden, wie sich diese Tatsache verhält."
      ],
      [
        "Und es könnte natürlich, wenn noch auf andere Tatsachenfelder eingegangen werden sollte, durchaus auch noch für diese anderen, sehr feineren, intimeren Strukturverhältnisse des Menschen manches gesagt werden.",
        "Frage: Wie erklärt man das Phänomen des bekannten Pferdes, das zum Erstaunen aller Gelehrten alle Rechenaufgaben und die mathe- matischen Aufgaben ohne Schwierigkeit löste, und erst dann voll- kommen versagte, als man ihm die Aufgaben vor dem Prüfenden auf Zettel schreiben ließ?"
      ],
      [
        "Wenn es nun beim Pferd sich so verhält, daß keiner der im Räume Anwesenden die Aufgabe sehen konnte, beruht das auf einer starken Suggestivität des Tieres?",
        "Und wie kommt das zustande?",
        "Ich möchte niemals über etwas anderes sprechen als über dasjenige, was ich selber untersucht habe."
      ],
      [
        "Und daher möchte ich in der Antwort auf diese Frage auch nur geben, was ich selber erlebt habe.",
        "Ich kenne zum Beispiel die be- rühmten Elberfeider Pferde nicht.",
        "Ich kenne auch nicht den Hund Rolf, habe nie die Ehre gehabt, ihn kennenzulernen."
      ],
      [
        "Nun, mit Bezug auf solche Sachen konnte ich immer kon- statieren, daß die Geschichte um so wunderbarer ist, je weniger man in die Verlegenheit kommt, sie wirklich zu durchschauen, sie wirklich kennenzulernen.",
        "Aber das Pferd 155 des Herrn von Osten habe ich einstmals gesehen in Berlin."
      ],
      [
        "Ich kann nicht gerade sagen, daß die Rechenaufgaben, die der Herr von Osten dem Pferd vorlegte, so außerordent- lich komplizierte waren.",
        "Aber ich konnte mir aus dem, was da vorging wozu man allerdings einzig genau hin- zuschauen brauchte , eine augenblickliche Vorstellung von dem machen, um was es sich eigentlich handelt."
      ],
      [
        "Ich konnte mich allerdings nur wundern darüber, welch merkwürdige Theorien über diese Dinge aufgeworfen worden sind.",
        "Es war da ein Dozent, ich glaube Fox oder so ähnlich heißt er, der sollte nun auch diese ganze Ge- schichte mit dem Pferd prüfen; und er stellte nun die Theorie auf, daß jedesmal, wenn der Herr von Osten irgendeine Aufgabe gebe, ganz furchtbar kleine Bewegun- gen im Auge oder irgend etwas dergleichen zustande kämen."
      ],
      [
        "Eine andere kleine Bewegung käme zustande, wenn der Herr von Osten «drei» sagt so, oder wenn er es mal so sagt; eine andere Bewegung käme zustande, wenn er «zwei» ausspreche.",
        "So daß also eine gewisse feine Bewegungsreihe zustande käme, wenn Herr von Osten sagte, «drei mal zwei»; dann käme wieder das gleiche Zeichen dieser Bewegung, sechs!"
      ],
      [
        "Und das Pferd des Herrn von Osten sollte nun ganz besonders dazu veranlagt sein, diese feinen Bewegungen - von denen der betreffende Dozent sagte, daß er sie nicht irgendwie wahrnehme, son- dern daß er sie nur hypothetisch voraussetze - zu erraten.",
        "Also es beruhte schließlich die ganze Theorie doch darauf, daß das Roß des Herrn von Osten viel gescheiter war in der Wahrnehmung, in einem viel stärkeren Maße in der Wirklichkeit, als der Herr Dozent, der diese Theorie auf- stellte."
      ],
      [
        "Man kann, wenn man sich an das blitzblaue Denken im Hypothesenaufstellen hält, Hypothesen in der aller- 156 verschiedensten Weise aufstellen.",
        "Für den, der in solche Sachen ein bißchen hineinschauen kann, hatten manche Umstände einen außerordentlich großen Wert, nämlich während der ganzen Zeit, während welcher der Herr von Osten dem staunenden Publikum seine Versuche vorführte mit seinem Roß, gab er - er hatte riesige Taschen da rückwärts drinnen im Rock dem Pferd lauter Süßigkei- ten."
      ],
      [
        "Und das Pferd schleckte eben fortwährend, und so löste es diese Aufgaben auf.",
        "Nun denken Sie sich, daß dadurch ein ganz anderes Seelenverhältnis besteht zwischen dem Roß und dem Herrn von Osten selber.",
        "Wenn der Herr von Osten dem Pferd fortwährend Zucker gibt, entsteht ein ganz beson- deres Verhältnis der Liebe, der Innigkeit der Beziehungen."
      ],
      [
        "Nun ist die tierische Natur so, daß sie außerordentlich stark variabel ist durch die Innigkeit der Beziehung, die sich herausbildet, sowohl vom Tier zum Menschen wie auch vom Menschen zum Tier.",
        "Und da kommen dann Wirkungen zustande, die tatsächlich falsch bezeichnet wer- den, wenn man sie ein «Gedankenlesen» nennt, in dem Sinne, wie das Wort trivial oftmals aufgefaßt wird, aber die doch Vermittler sind für dasjenige, was keine «feinen Zuckungen» sind, die ein Privatdozent hypothetisch auf- stellt, von denen er aber selbst sagt, daß er sie nicht sieht!"
      ],
      [
        "Zur Vermittlung der Lösungen braucht es keine feinen Zuckungen.",
        "Sie ist auf folgendes zurückzuführen: denken Sie sich, was in dem Herrn von Osten vorging, indem er natürlich die Eitelkeit hatte, daß im Publikum, sensations- lüsternen Leuten, die Spannung, in der es da stand, die unglaublichsten Kurven durchmachte, wenn er das be- merkte, und wenn er dann stand vor der Lösung der Auf- gabe, so gab er dem Pferd ein Stück Zucker."
      ],
      [
        "Und nehmen Sie noch dazu, was durch das seelische Verhältnis auf das 157 Pferd wirkte.",
        "Es war wirklich ein nicht durch Worte oder durch Zuckungen, sondern allerdings intim erteilter Be- fehl, der immer von Herrn von Osten an das Pferd aus- ging, wenn er ihm von den Süßigkeiten zu fressen gab."
      ],
      [
        "Suggestion ist wohl nicht das richtige Wort.",
        "Beziehungen, die zwischen Mensch und Mensch stattfinden, dürfen nicht auf jedes Lebewesen übertragen werden.",
        "Diese Dinge habe ich einmal im Konkreten zu zeigen versucht, indem ich Ihnen einen Umstand, den viele als nebensächlich ansehen werden: das fortwährende Zucker- geben eben als etwas außerordentlich Wesentliches hervor- heben mußte."
      ],
      [
        "Frage: Besteht die Möglichkeit, für das Gebiet der Mineralogie und Kristallogie auf einen ebenso die Systematik belebenden Gesichtspunkt hinzuweisen, wie ein solcher für die Botanik gegeben ist mit der Idee der Urpflanze oder für die Chemie bei einem neuartigen Auf- fassen des periodischen Systems der Elemente?",
        "Wir haben es allerdings, wenn wir von Kristallformen sprechen, ich meine jetzt nicht von den durch Konstruk- tionen hinzugekommenen, sondern von den realen Kri- stallformen, mit Formen zu tun, welche real anders sind in ihrem ganzen Verhältnisse zum Kosmos, in ihrer gan- zen Stellung in der Welt, als die Formen, die man sich in der Urpflanze und wiederum in den von der Urpflanze abgeleiteten, sagen wir also, Pflanzengestalten in der Möglichkeit des realen Bestehens vorstellen kann."
      ],
      [
        "Es könnte zum Beispiel durchaus nicht das Prinzip, welches angewendet wird für die Ausgestaltung der Urpflanze, auf das Gebiet der Mineralogie oder der Kristallogie an- gewendet werden.",
        "Denn man hat es da zu tun mit etwas, dem man sich von einer ganz anderen Seite her nähern muß."
      ],
      [
        "Und zwar muß man sich ihm zunächst dadurch nähern, daß man eigentlich erst an das Gebiet der poly- 158 edrischen Kristallformen heranrückt.",
        "Und dieses Heran- rücken, ich kann es jetzt nur andeuten.",
        "Ich habe es einmal in einem Vortragskurs, den ich für einen kleineren Kreis gehalten habe, genauer ausgeführt in seinen einzelnen Darstellungen."
      ],
      [
        "Dieses Annähern, das trifft man, wenn man ausgeht von der Betrachtung, einer innerlichen dyna- mischen Betrachtung des Aggregatzustandes, sagen wir zu- nächst vom gasförmigen Zustand nach abwärts zum festen.",
        "Ich kann jetzt nur die Linien ziehen, es würde zu lang dauern, wenn ich es im einzelnen ausführen sollte, aber ich will es andeuten."
      ],
      [
        "Wenn man hinabsteigt - wenn ich mich so ausdrücken darf - vom gasförmigen Aggregat- zustand zum flüssigen, so muß man sagen: der flüssige Aggregatzustand, der zeigt sich darin, daß einem bei ihm, als das ihm im ganzen Zusammenhalt der Natur Ange- messene, eine Niveaubegrenzungsoberfläche entgegentritt, welche eine Kugelfläche ist, und deren Krümmungsmaß von irgendeinem Punkt der Oberfläche man vom Über- gang zu der Tangente an diesem Punkt bekommt.",
        "Was man da bekommt also, das schließt ein die Form, die ihren äußeren Umfang in der Kugelfläche hat, und einen Punkt im Inneren, der von dieser Kugelfläche überallhin gleich weit absteht."
      ],
      [
        "Denkt man sich nun den Tropfen in unbegrenzter Art, ich sage nicht in unendlicher, sondern in unbegrenzter Art vergrößert, so bekommt man eine sich der Horizontalen nähernde Niveaufläche, und man hat gewisse Verhältnisse im Sinne der auf diese Niveaufläche Senkrechten zu be- urteilen.",
        "Dieselbe Vorstellung aber bekommt man heraus, indem man die Zusammenhänge betrachtet, die sich ergeben, wenn man unsere Erde einfach als einen Kraftzusammen- hang ansieht, der die Gegenstände der Umgebung, die 159 nicht fest mit ihr verbunden sind, anziehen kann."
      ],
      [
        "Wenn man die Erde nicht als Gravitationsmittelpunkt, sondern als Gravitations-Kugeloberfläche betrachtet, dann ergibt sich für diese, ich möchte sagen, Gravitationsfigur ganz dasselbe, was man in anderer Beziehung braucht für die materielle Konstitution des Tropfens.",
        "Man bekommt also für einen reinen Kraftzusammenhang etwas, was ent- spricht einem materiellen Zusammenhange."
      ],
      [
        "Und man kommt auf diese Weise zu einer Möglichkeit, Formver- hältnisse im Anorganischen zu studieren.",
        "So daß man also sagen kann, in diesem Kräftezusam- menhang, der einem im ganzen Erdkörper vorliegt, hat man es immer zu tun mit der Horizontal-Niveauebene."
      ],
      [
        "Geht man von diesem Kräftezustand nun zu einem sol- chen über, bei dem, sagen wir, in der Mitte nicht ein Punkt wäre, auf den sich die Niveaufläche so bezieht wie beim Tropfen auf den einen Mittelpunkt, sondern mehrere Punkte, so würde man eine merkwürdig zusammengesetzte Oberfläche finden.",
        "Diese Beziehungen der Linie auf diese «Mittelpunkte» müßte ich im Diagramm etwa in der fol- genden Weise zeichnen: Aber geht man jetzt dazu über - und jetzt mache ich einen großen Sprung, der allerdings gut begründet ist, aber ich kann ja jetzt in der kurzen Zeit nur hindeuten auf den wahren Inhalt -, geht man dazu über, diese 160 Punkte nicht innen anzunehmen, innerhalb des Systems, mit dem man es zu tun hat, sondern außerhalb, dann würde man vielleicht eine Zeichnung bekommen, die man diagrammatisch in der folgenden Weise machen kann: Verlegt man die Punkte in unermeßliche Weiten, nicht in unendliche Weiten, sondern in sehr große Weiten, dann gehen diese gekrümmten Flächen, die hier durch die ge- krümmten Linien, durch die Kurven, angedeutet sind, in Ebenen über, und wir würden eine polyedrische Form bekommen, welche sich dem nähert, was wir in den be- kannten Kristallgestalten vor uns haben."
      ],
      [
        "Und in der Tat führt uns die geisteswissenschaftliche Betrachtung dazu, den Kristall in einer solchen Weise an- zusehen, so daß wir ihn nicht bloß etwa aus gewissen inneren figurierenden Kräften in irgendeiner materiellen Substanz ableiten, sondern daß wir ihn auf das Äußere des Kosmos beziehen, und daß wir im Kosmos die Rich- tungen suchen, die dann durch die Verteilung ihrer Aus- gangspunkte eben das ergeben, was die einzelne Kristall- form ist.",
        "Wir bekommen in der Tat in der einzelnen Kristallform gewissermaßen Abdrücke großer kosmischer Verhältnisse."
      ],
      [
        "Das alles will im einzelnen studiert sein.",
        "Ich fürchte, es erscheine Ihnen schon als etwas sehr Wag- halsiges, was ich jetzt, allerdings nur in einzelnen, ganz 161 spärlichen Linien, andeuten konnte.",
        "Aber man muß eben schon sagen, daß sich heute die Menschen mit ihrer Vor- stellungswelt in einem sehr engen Gebiete eingekapselt haben, und daß es ihnen deshalb so unbehaglich wird, wenn man nicht bei der Begriffswelt bleibt, die gewöhn- lich heute zugrunde gelegt wird, ich möchte sagen, in allen Wissenschaften zugrunde gelegt wird."
      ],
      [
        "Geisteswissenschaft fordert eben eine - wie es ja die Erfahrung notwendig macht gegenüber dem heutigen Zustand unermeßliche Erweiterung der Begriffe.",
        "Und das ist eben manchem un- behaglich.",
        "Er sieht sozusagen nicht das Ufer, glaubt, ins Uferlose zu kommen."
      ],
      [
        "Er würde aber merken, daß man dasjenige, was man durch die Weite verliert, doch wieder- um als eine gewisse innere Festigkeit und Sicherheit ge- winnt, so daß man sich nicht so stark zu fürchten braucht vor dem, was da wie eine Erweiterung ins Uferlose auf- tritt.",
        "Es ist natürlich viel einfacher, sich irgendein Modell zu machen - wie es heute auch erwähnt worden ist in einer bestimmten Frage , als zu solchen Vorstellungen vorzu- rücken."
      ],
      [
        "Es ist leichter zu sagen: Das Wahre muß einfach sein! - Der Grund, warum man sagt, das Wahre muß einfach sein, ist nämlich nicht der, daß das Wahre wirklich einfach sein muß, denn der menschliche Organismus ist zum Beispiel in unermeßlichster Weise kompliziert.",
        "Sondern der Grund, warum man sagt: Das Wahre muß einfach sein! - ist, daß das Einfache bequem ist im Denken."
      ],
      [
        "Das ist der ganze Witz.",
        "Und das ist eben nötig, daß man zum Inhaltsvolleren vor allem vorrückt, wenn man nach und nach die Wirklichkeit wirklich begreifen will.",
        "Die Frage, die hier noch aufgeworfen worden ist, er- forderte, daß man drei Stunden Theorie vortragen müßte."
      ],
      [
        "Über die Sonne kann man nicht durch «eine kurze Beant- 162 wortung der Frage» sprechen, weil man eben vollständig mißverstanden würde.",
        "Und das möchte ich nicht. - So sind ja zunächst die beantwortbaren Fragen notdürftig beantwortet."
      ],
      [
        "Frage: Findet Geisteswissenschaft eine Umwandlung der materiellen Erde mit dem Einzüge des Christus-Geistes in die Erde?",
        "Drückt sich die Wirkung der Christus-Kraft in einem der in der neueren Zeit gefundenen Elemente vielleicht besonders aus?"
      ],
      [
        "Was soll die Frage? - Nicht wahr, man muß nur be- denken, von welchem Gesichtspunkt aus eine solche Frage gestellt sein kann.",
        "Es ist die Frage gestellt: Drückt sich in der materiellen Erde die Wirkung der Christus-Kraft aus? - Sie müssen nur bedenken, daß doch für die Geistes- wissenschaft aus ihrer Forschung heraus eine ganz be- stimmte Vorstellung vorliegt über die Erde, die nicht zusammentrifft mit dem, was man sich von der Erde vor- stellt, wenn man im Sinne des heutigen Wortes «materiell» von der «materiellen Erde» spricht."
      ],
      [
        "Es ist also eigentlich die Frage ohne einen wirklichen Inhalt.",
        "Wenn man von so etwas wie einer «Einwirkung der Christus-Kraft auf die Erde» spricht, so muß man da wiederum diese Vor- stellung gewissermaßen der Geisteswissenschaft entlehnt ist - dann auch über die Erde diejenige Vorstellung haben, welche für die Anthroposophie, für die Geisteswissen- schaft gilt."
      ],
      [
        "Und wie da die Christus-Kraft in einem ge- wissen Verhältnisse steht zu der ganzen Metamorphose der Erde, das läßt sich auch wiederum nur darstellen im ganzen Zusammenhang, den ich in der «Geheimwissen- schaft im Umriß» gegeben habe.",
        "Und dort findet man dann auch das Nötige zur Beantwortung desjenigen, was mit dieser Frage gemeint ist, wenn sie richtig formuliert wird. 163 Auf Wunsch vieler Kursteilnehmer gibt darauf ein Stuttgarter Herr einen kurzen Bericht über den am Abend vorher vom alldeutschen General v."
      ],
      [
        "Gleich in einer Stuttgarter Massenversammlung gehaltenen Vortrag über «Rudolf Steiner als Prophet einer bedenklichen Lehre» (siehe den Hinweis Rudolf Steiners darauf am Schluß des Vormit- tagvortrags, S. 139/140).",
        "Ich möchte nur das eine einfügen, daß besagter General v."
      ],
      [
        "Gleich ziemlich lang vorher, wochenlang vorher, bevor er zu seinem Vortrag und zur Abfassung seiner Broschüre geschritten ist, einen Brief an unseren Freund Herrn Molt richtete, als besorgter Vater, besorgt über das Unglück, daß er, als Besitzer eines vierzigjährigen Adels, seinen Sohn nicht nur «abgegeben» hat an die Anthroposophie, sondern auch an eine vollständig unadelige Dame, die Anthroposophin ist!",
        "Als besorgter Vater schrieb er an unseren Freund Molt, er möge ihn besuchen."
      ],
      [
        "Herr Molt tat das auch, sagte aber, daß er mit ihm nichts anzu- fangen wisse.",
        "Namentlich sah er das aus dem Umstand, daß Herr v.",
        "Gleich die Forderung aufstellte, wir «von der Dreigliederungsbewegung» sollten den bei uns ange- stellten Sohn des Herrn General v."
      ],
      [
        "Gleich künftighin so schlecht honorieren, daß der junge Mann nicht imstande sei, sich zu verheiraten, wir sollten wenigstens durch dieses schlechte Honorieren den General v.",
        "Gleich vor dieser Heirat seines Sohnes schützen. - Nach diesen Vorgängen war es begreiflich, daß man von dem Vortrag des Gene- rals v."
      ],
      [
        "Gleich nicht gerade das Beste erwarten konnte.",
        "Wir sahen dann tatsächlich auch die schlimmsten Erwar- tungen übertroffen!",
        "Es war bei diesem Vortrag so, daß Gleich im wesentlichen den Inhalt einer Broschüre vorge- bracht hat - noch etwas saftiger, sagen wir, ausgestattet -, die zugleich in Ludwigsburg erschien."
      ],
      [
        "Es war das eben schon ausgemacht, daß diese Broschüre zugleich erscheinen sollte mit dem Vortrag.",
        "In dieser Broschüre bringt er in 164 der unorientiertesten Weise, ohne irgendwie Beweise für das, was er sagt, zu liefern davon kann sich jeder über- zeugen, der diese Broschüre liest -, gegen Anthroposophie verschiedenes vor, indem er eigentlich nur die Gegner der Anthroposophie benützte."
      ],
      [
        "Es geht das schon aus dem Inhaltsverzeichnis der Broschüre hervor: einige Hinweise auf die Literatur, wo man sich über die Anthroposophie informieren kann.",
        "Das wären zunächst die anthroposophi- schen Bücher, sollte man denken."
      ],
      [
        "Aber nein, da stehen zirka zwanzig Gegner, und zwar der allerschofelste gleich vor- an: Max Seiling! v.",
        "Gleich bringt im wesentlichen nichts anderes, als was man bei allen Gegnern in der Art der Broschüre von Seiling finden kann, nur noch in der Art und Weise, wie eben der General v."
      ],
      [
        "Gleich seinen Vortrag zu halten pflegte.",
        "Und es war so, daß dieser Vortrag «ohne Diskussion» angesagt war.",
        "Es waren zahlreiche An- hänger der anthroposophischen Bewegung drinnen.",
        "Nach- dem er ihn zu Ende gesprochen hatte, den Vortrag, der in den allerschärfsten Ausdrücken, teilweise mit den gröb- sten Verleumdungen vorging, verließ er einfach, ohne auf irgendeine Diskussion einzugehen, den Saal."
      ],
      [
        "Und als man versuchte, darauf zu Wort zu kommen, und als Herr Molt, der da war und auch in dem Vortrag mehrfach persönlich angegriffen wurde, rief: Er erkläre hiermit öffentlich - er rief das in den Saal hinein, in dem sich eine tobende Menge der Anhänger des Herrn v.",
        "Gleich befand -, er erkläre den Herrn v."
      ],
      [
        "Gleich öffentlich als einen Lügner und spreche ihm öffentlich seine Ehre ab - fand Herr v.",
        "Gleich es nicht der Mühe wert, irgend etwas zu ant- worten.",
        "Er hatte bereits den Saal verlassen.",
        "Dagegen ver- suchten die Anhänger, die mit Pfeifen und anderen Lärm- instrumenten ausgerüstet waren, die Anthroposophen, die dagegen etwas vorbringen wollten, niederzuschreien."
      ],
      [
        "Und 165 es war ziemlich nahe an einer Schlägerei.",
        "Es war ja auch sehr schwer möglich, auch nur mit Zwischenrufen gegen die schwersten Verleumdungen zu protestieren, da die ganze Versammlung sofort einen bedrohlichen Charakter annahm, und man sah, daß es zu einer Prügelei kommen würde."
      ],
      [
        "Es folgten einige Berichte über den vorangegangenen Vortrag v.",
        "Gleichs in Ludwigsburg.",
        "Schließlich wurde ein von General v.",
        "Gleich an seinen Sohn gerichteter Brief vorgelesen.",
        "Ich möchte nur noch ein paar Worte sagen."
      ],
      [
        "Kann ich diesen Brief nochmals haben?",
        "Ich möchte nur eine formale Bemerkung machen, eine Bemerkung, die ja nicht die Sache selbst betrifft.",
        "Da steht also in dem Brief des Herrn v.",
        "Gleich an seinen Sohn: «..."
      ],
      [
        "Wollte Gott, Du wärst als anständiger christlicher Adliger fürs Vaterland gefallen, dann könnte ich wenigstens in Stolz um Dich trauern ...",
        "Ich bitte zu Gott, die Verblendung wieder von Dir zu nehmen, daß Du aus ihr wieder erwachen mögest...» (Lücke in der Nachschrift.) Sie sehen, es ist viel über die eigene Christlichkeit des Herrn v."
      ],
      [
        "Gleich gesagt; ich möchte dies betonen: die eigene Christlichkeit, zum Vergleich mit der Zumutung, die an uns gestellt worden ist, den Sohn so schlecht zu bezahlen, daß er nun ja nicht heiraten kann.",
        "Das scheint mir eine recht christliche Tat zu sein!"
      ],
      [
        "Und ich möchte jetzt nicht durch diese «kleinen Pikanterien», die ja auch in diesem Programm sind, wegführen etwa über den Ernst der Lage.",
        "Denn ich weiß sehr gut, daß dasjenige, was gestern in Stuttgart geschehen ist, nicht etwa ein Ende ist, sondern ein Anfang, daß dahinter eine starke Organisation steht."
      ],
      [
        "Und gerade aus diesem Gefühl heraus darf ich wohl einer solchen Persönlichkeit, wie sie eben gesprochen hat - aus einem wirklichen inneren Gefühl für dasjenige, was An- 166 throposophie wenigstens sein möchte -, herzlichst danken.",
        "Ich möchte aber durchaus hinweisen auf den Ernst der Situation und auf die Notwendigkeit, im Sinne dieser ernsten Situation sich zu verhalten."
      ],
      [
        "Was ich sagen möchte, das muß natürlich unterschieden werden von einem gewissen Verständnisse, das man im- merhin auch solchen Christen gegenüber haben kann, wie zum Beispiel der Herr General v.",
        "Gleich ein Christ ist!"
      ],
      [
        "Ich will ja nicht einen Vergleich, nicht einen formellen Vergleich machen, sondern ich möchte nur etwas sagen, an das ich mich bei dieser Art von Christlichkeit erinnern mußte.",
        "Es gibt nämlich ganz verschiedene Arten von Christlichkeit, sogar von orthodoxem Christentum."
      ],
      [
        "Als der Kriminalanthropologe Moritz Benedikt daran ging, in der Kriminalanthropologie zu arbeiten und zu schreiben, fand er zunächst in Wien wenig Verständnis.",
        "Er fand dann bei einem Anstaltsleiter für Schwerverbrecher in Ungarn außerordentliches Verständnis."
      ],
      [
        "Es wurde ihm die Möglichkeit gegeben, Verbrecherschädel zu untersuchen, auch von den schwersten ungarischen Verbrechern die Schädel zu untersuchen.",
        "Unter diesen waren die merk- würdigsten Leute, unter anderem auch ein ganz ausge- prägter orthodoxer Christ, welcher sich zwar freilich nicht dem Professor Benedikt gegenüber seinen christlichen In- tentionen gemäß verhalten konnte."
      ],
      [
        "Über den war er sehr wütend, weil er seinen Schädel untersuchen durfte.",
        "Und ganz besonders war er darüber wütend, weil er gehört hatte, daß der Gefängnisdirektor damit einverstanden war, daß der Professor Benedikt besonders charakteristi- sche Verbrecherschädel nach dem Tode werde zu studieren bekommen."
      ],
      [
        "Und da er in dieser Anstalt nicht in Freiheit auf den Professor Benedikt losgelassen wurde, so wollte er wenigstens gefesselt diesem Benedikt vorgeführt wer- 167 den.",
        "Bei dieser Vorführung sagte er, er könne durchaus nicht zugeben, daß er bei seiner christlichen Gesinnung es erlauben müsse, daß sein Schädel nach dem Tode dem Professor Benedikt nach Wien geschickt werde; er würde dann doch hier begraben werden, und sein Schädel werde in Wien herumliegen!"
      ],
      [
        "Und er möchte wissen, wie nun bei der Auferstehung sein Leib und sein Schädel zusammen- gebracht werden sollen.",
        "So gut glaubte der an seine leib- liche Auferstehung - er war ein ganz richtiger Verbrecher, ich glaube sogar ein Mörder. 168"
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SOZIALWISSENSCHAFT UND SOZIALE PRAXIS Fünfter Vortrag, Dornach, 8. April 1921",
    "paragraphs": [
      "Gestatten Sie, daß ich heute anknüpfe an einiges, das ich gestern nur andeuten konnte und das uns dann überführen soll zu unserer heutigen Betrachtung. Ich hatte gestern an- zuknüpfen an einen Satz, der aus der Weltanschauung des II.",
      "Jahrhunderts, sofern diese in Mitteleuropa herrschte, hervorgegangen ist, an den Satz, daß die Zunge, so wie sie aus der Umgebung die Luft hereinzieht, so aus den Zäh- nen ziehe das Wort, das heißt die Kraft, zu sprechen. Und ich habe Sie darauf aufmerksam gemacht, wie der Gelehrte des 19.",
      "Jahrhunderts zu diesem Satze nur hinzu- zufügen hat, daß er darüber lachen könne. Aber ich habe auch charakterisiert den Abstand, der da liegt zwischen der Zeit, in die eine solche instinktive Anschauung wie die gestern zitierte hineinfällt, und dem Zeitalter, in dem dann diese philiströs-ironische Kritik sich geltend gemacht hat, jenem Zeitalter, das eben beginnt mit dem ersten Drittel des 15.",
      "Jahrhunderts. Jener Ausspruch fällt noch in das vorhergehende Zeitalter hinein und ist durch die Gründe, die ich Ihnen gestern angegeben habe, für dieses Zeitalter in einer gewissen Weise außerordentlich charak- teristisch.",
      "Als charakteristisch muß er aber auch empfunden wer- den seinem Inhalte nach. Denn ich habe Ihnen ja gestern auseinandergesetzt, wie man zum Verständnis der Sprach- fähigkeit und der Sprache überhaupt sich zunächst be- kanntmachen muß mit dem, was Geisteswissenschaft zu sagen hat im Sinne des von mir in meiner kleinen Schrift 169 «Die Erziehung des Kindes vom Gesichtspunkte der Gei- steswissenschaft» Ausgeführten.",
      "Ich habe dort gezeigt, welcher bedeutungsvolle Vorgang sich mit dem Zahn- wechsel vollzieht, wie dasjenige, was den Menschen als rhythmischen Menschen und Gliedmaßen-Stoffwechsel- menschen später noch erfüllt, ihn vorher aber ganz erfüllt hatte, sich zurückzieht aus der Nerven-Sinnesorganisation und daher gerade diesen Vorgang bewirkt, der dort in meiner Schrift «Die Erziehung des Kindes vom Gesichts- punkte der Geisteswissenschaft» als die Geburt des Äther- leibes formelhaft bezeichnet wird. Ich habe Sie dann hin- geführt dazu, wie in einer ähnlichen Weise jener Vorgang erfaßt werden muß, welcher etwa um das vierzehnte, fünfzehnte Jahr herum liegt, das Geschlechtsreifwerden, und ich habe ausgeführt, wie dasjenige, was da vorliegt, formelhaft mit dem Ausdruck umfaßt werden kann: Geburt des astralischen Leibes.",
      "Aber ich habe gesagt, daß die Ereignisse, die so im Leben des Menschen in irgend- einem Lebensabschnitte eintreten, in Metamorphose sich auch zu anderen Zeiten - aber eben dann in Metamor- phose vollziehen, und daß wir das, was sich zwischen dem Menschen und der Außenwelt äußerlich abspielt zur Zeit der Geschlechtsreife, innerlich zu suchen haben als einen Vorgang, der sich abspielt zwischen dem Geistig- Seelischen und dem Körperlich-Leiblichen innerhalb des Menschen als der Vorgang, der im wesentlichen das phy- siologische Korrelat ist für das Sprechenlernen des Kindes, daß man daher auch zu suchen habe die Anhaltspunkte zu einer wirklichen rationellen Sprachwissenschaft, indem man von einer durchdringenden anschauenden Erkenntnis dieses Vorganges ausgeht. Ich habe dann gesagt, daß durch die Begründung und Entwickelung der abstrakten Logik und des abstrakten 170 logischen Denkens diejenige Sphäre des Erlebens, in wel- cher sich lebendig abspielt, was zwischen dem Geistig- Seelischen und dem Leiblich-Physischen vorgeht, gewisser- maßen verlegt wird, hinuntergeschoben wird ins Unter- bewußte, und daß eben Aristoteles dadurch, daß er das Bewußtsein in die Abstraktion hineinleitete, abgeschnitten hat das Hinsehen nach dem Vorgeburtlichen.",
      "Denn hätte man, was man instinktiv im frühen Altertum konnte, jenes Wirken des Astralischen im Geschlechtsreifwerden und im Sprachlichen anschaulich vor sich gehabt, wie wir es jetzt wiederum erstreben müssen, dann hätte man auch das- jenige allmählich anschauend vor sich bekommen können, was die Verbindung des Ich selber mit dem ganzen phy- sisch-ätherisch-astralischen Menschen ist. Das heißt, man hätte auf diesem Gebiet vorrücken können durch die Er- kenntnis des Sprechenlernens zu der Erkenntnis der Ein- gliederung des menschlich geistig-seelischen Ich in sein Leiblich-Physisches.",
      "Und Aristoteles hat gerade deshalb sein Dogma aufgestellt, daß mit jeder einzelnen mensch- lichen Wesenheit, die hier geboren wird, auch das Seelisch- Geistige mitentstehe. Er hat damit aus der Welt der Er- kenntnis weggeschafft die Anschauung der präexistieren- den Menschenseele.",
      "Die Anschauung dieser präexistierenden Menschenseele gibt allein eine wirkliche Erkenntnis von der Ewigkeit der Menschenseele. Diese Erkenntnis wird durch keinerlei philosophische Spekulation geliefert, sondern einzig und allein durch ein anschauendes Urteil in der Richtung, die ich eben jetzt angedeutet habe.",
      "Dieses Dogma von dem Nichtvorhandensein der Präexistenz ist dann in die Kirchenlehre des Christentums übergegangen. Und man muß es streng betonen: daß die Leugnung der Präexistenz, indem sie dann durch Konzile gefestigt wurde, nicht christ- lich in wahrem Sinn des Wortes ist, sondern aristotelisch ist, und mit dem Eindringen des Aristotelismus in die Christenlehre zum christlichen Dogma geworden ist.",
      "In dem Augenblick, wo sich das Christentum von diesem Bestandteil des Aristotelismus wird frei machen können, wird die Bahn auch frei sein für ein Erkennen der Prä- existenz. Man muß sagen: diese Präexistenz, die bis zu Origenes auch nicht angezweifelt worden ist von der christlichen Lehre des Abendlandes, ist durch die staatliche Verfügung des Justinian, der mitgewirkt hat an der Verketzerung des Origenes, aus der Christenlehre des Abendlandes ver- schwunden.",
      "Es ist deshalb den Anhängern dieser nicht- christlichen Christenlehre des Abendlandes so unange- nehm, wenn irgend jemand auf die historischen Tatsachen in den ersten Jahrhunderten des Christentums aufmerk- sam macht. Sie rufen dann alles herbei, was sie an Un- wahrhaftigkeiten aufbringen können über Zusammen- hänge der Anthroposophie mit der Gnosis und so weiter.",
      "Nun, über diese Dinge kann ich hier nicht weiter mich verbreiten. Was ich aber sagen will, ist dieses: Wenn man das Geistig-Seelische im Menschen einzig und allein be- gründet auf das, was für die Anschauung des Bewußtseins seit der Geburt lebt, dann kommt man allmählich zu dem, was die Lehre von der Unsterblichkeit zu einem bloßen Glaubensartikel macht.",
      "Man kann sagen, was im Menschen vorgeburtlich, was präexistent war, das gerät durch den Durchgang durch die Geburt in einen völlig unbewußten Zustand. Das kann erst wiederum angeschaut werden, wenn man sich zur Imagination und zur Inspiration herauf erhebt.",
      "Aber am anderen Pol des Menschen erscheint es in seiner Willens- und emotionellen Natur. Wir haben ja im dreigliedrigen 172 Menschen auf der einen Seite den Nerven-Sinnesmenschen, der zusammenhängt mit dem vorstellenden Menschen, auf der anderen Seite den Gliedmaßen-Stoffwechselmenschen, der zusammenhängt mit der Willensnatur des Menschen und mit seiner emotioneilen Natur.",
      "Dadurch, daß das Vorstellungsleben abgedämpft ist, heruntergedämpft ist bis zum gegenständlichen Anschauen, dadurch ist zunächst für dieses gegenständliche Vorstellen im Erkennen ver- schlossen die Präexistenz. Aber was mit ihr gegeben ist, lebt in der Sphäre des Menschen, die am anderen Pol auf- tritt.",
      "Da tritt auf die Willensnatur, die Emotionsnatur. Aus dieser kann zunächst nicht eine Erkenntnis gewonnen werden, daher ein bloßer Glaube. Und wenn das, was vorgeburtlich ist, durch die Erweiterung der Erkenntnis Erkenntnis werden kann, so kann ohne diese Erweiterung der Erkenntnis das, was in Wille und Emotion lebt, nichts anderes werden als ein Glaubensartikel des Menschen.",
      "Da- her geschieht mit dem Hinabdämmern der übersinnlichen Erkenntnis auch das Hinabdämmern der Erkenntnis der Ewigkeit der Menschenseele bis in die Sprache hinein. Es müßte immerhin auffallen, daß wir in den bekannteren Zivilisationssprachen wohl ein Wort haben für Unsterb- lichkeit, das heißt, für das Leben im Nachtodlichen, daß wir aber nicht ein Wort haben, welches auf dem anderen Pol des Menschen die Ewigkeit der Menschenseele aus- drücken würde, das Ungeborensein.",
      "Das aber wird sich bis in die Sprache hinein die moderne Menschheit wieder erobern müssen: daß die Ewigkeit des Menschen ebenso wie sie nach der einen Seite, nach der Seite des Todes hin, in dem Worte Unsterblichkeit zum Vorschein kommt, auch nach der anderen Seite durch ein Wort wie «Unge- borensein» - das ja selbstverständlich mit der zunehmen- den Zivilisation geschickter werden wird - sichtbar wer- 173 den kann. Dann aber wird dasjenige, was über die Ewig- keit der Menschenseele zu sagen sein wird, nicht mehr bloßer Glaubensartikel sein, sondern ein Erkenntnisinhalt.",
      "Solange man bloß beim Nachtodlichen bleibt, muß die Unsterblichkeitsfrage eine Glaubensfrage sein. Sobald man übergeht zu einer wirklichen Erkenntnis des Übersinn- lichen, wird die Unsterblichkeitsfrage eine Frage der wirk- lichen Erkenntnis.",
      "Das ist ein Zusammenhang, der eingesehen werden muß, das ist ein Rubikon, der überschritten werden muß von der modernen Zivilisation. Denn was aus diesem Über- schreiten folgt, das wird nicht nur etwas sein, was theo- retisch wirkt, sondern das wird in einer ganz anderen Weise noch wirken.",
      "Wir können sagen: Lernen wir sach- gemäß aufsteigen von so etwas, wie es das Verständnis des Zahnwechsels, das Verständnis der Sprache ist, zu dem, wozu wir dann kommen, so eignen wir uns dadurch eine Erkenntnis des unsterblichen Wesens der Menschenseele an. Diejenigen, die im 11.",
      "Jahrhundert gedacht haben und davon gesprochen haben, daß die Zunge aus den Zähnen die Sprache saugt, haben nicht etwa geglaubt, daß es nur Zahnlaute gibt, wie Wilhelm Scherer sonderbarerweise voraussetzt, sondern sie waren in ihrem instinktiven Er- kennen durchdrungen davon, daß man, um die Sprache zu verstehen, hinunterdringen müsse in die menschliche We- senheit, so wie man beim Verstehen des Zahnwechsels hin- unterdringen müsse. Wie da die Kräfte heraufkommen, so müsse man hinunterdringen zu den Ursprüngen des Weges, der mit dem Zahnwechsel zu dem hinweist, was sich auf einem vorigen Schritte der Entwickelung des Men- schen gezeigt: zum Entstehen der Sprache.",
      "Instinktiv, un- terbewußt waren diese Erkenntnisse. Aber wer heute das Entsprechende aus dem Bewußtsein hervorholt, der wird finden, welche Tiefe sie in einer gewissen Beziehung atmen, und welche Philistrosität solche Einwände atmen wie die, von denen ich einzelne gestern besprochen habe.",
      "Wir ge- winnen aber auch, indem wir uns zu solchen Erkenntnissen wie denen über die Sprache hinaufschwingen, zu gleicher Zeit, ich möchte sagen, den Zugang zum Weg, die Un- sterblichkeit zu erkennen. Daher ist mit dem Erkennen dieser übersinnlichen Welt zu gleicher Zeit verbunden das Erringen eines gesunden Urteiles auch über das, was uns im Leben umgibt wie die Sprache.",
      "Und wir können nicht, ohne innerlich unehrlich zu werden, vorgeben, einzudrin- gen in so etwas in unserer Umgebung, wie es die Sprache ist, wenn wir nicht zu gleicher Zeit zugeben: hier liegen Grenzen vor, die nicht bloß als Grenzen der gewohnten Erkenntnis anzuerkennen sind, sondern die notwendig machen, daß sie überschritten werden durch eine anders- artige Erkenntnis. So hängt wirkliche Erkenntnis der äußeren Sinnenwelt schon zusammen mit dem Aufschwung zur übersinnlichen Erkenntnis.",
      "So müssen in der wirklich gesunden Erkennt- nis übersinnliche Anschauung und sinnliche Anschauung zusammenwirken, und es muß das eine das andere tragen. Deshalb darf man glauben, daß mit dem Erringen ge- sunder Urteile über das Übersinnliche auch gesunde Ur- teile in bezug auf das gewonnen werden können, was uns auf einem anderen Gebiete als Menschen umgibt, mit dem wir als Menschen zusammenhängen und innige Verhält- nisse eingehen müssen: das soziale Leben.",
      "In dem Duktus meiner bisherigen Vorträge habe ich so viel als möglich versucht, mich an das zu halten, was man etwa einen ganz wissenschaftlichen Duktus nennen könnte. Indem wir heute überzugehen haben zu dem, was als So- zialwissenschaft und soziale Praxis aus einer solchen inne- ren Seelenverfassung folgt, wie sie aus Geisteswissenschaft, wie sie hier gemeint ist, sich ergeben muß, da stehen wir in der Gegenwart selber inmitten der Praxis.",
      "Denn was in sozialer Beziehung zu sagen ist, das kann heute durchaus nicht etwa in der gleichen Weise betrachtet werden wie das, was vorangegangen ist. Es ist notwendig, daß man folgendes noch berücksich- tigt.",
      "Indem man zur Imagination, Inspiration und so weiter sich hinaufschwingt, wird das, was sonst vorstel- lungsmäßig ist und nicht unmittelbar den Willen motivie- rend sein kann, in den Willen hineingedrängt. Daher ist übersinnliche Erkenntnis willensmotivierend, und es gibt auch kein sittliches oder religiöses Ideal, welches nicht wenigstens unbewußt im Übersinnlichen wurzelte.",
      "Was durch die Vorstellung nur aus dem Sinnlichen gewonnen wird, kann niemals sozial oder sittlich motivierend sein, weil es unwirksam bleibt für den Willen. Deshalb muß man schon sagen, es könnte vielleicht auffällig sein, daß die Menschen, welche meine Schrift über das soziale Leben von der Dreigliederung in die Hand bekamen, wenn sie in dieser Schrift lasen, nun so gar nichts darinnen fanden von dem, was sie gewohnt waren zum Beispiel in meinen anthroposophischen Schriften als den Grundton zu finden.",
      "Man hat vielleicht von manchen Seiten erwartet: wenn derjenige, der sich zur Anthroposophie bekennt, über ein solches Thema schreibt, wie es in meiner Dreigliederung enthalten ist, dann müsse in alle die Einzelheiten, die da auseinandergesetzt werden, alles mögliche hineinfließen von den gewohnten «anthroposophischen» Urteilen; man müsse recht sehr mystelnd zu allerlei Ermahnungen schrei- ten und so weiter. Wenn auch von anthroposophischer Seite her vielfach ein solches Urteil gehört worden ist, dann kommt das den 176 Urteilen in der Qualität ganz gleich, die da wollten, als ich meine «Theosophie» schrieb, daß sie dasselbe darinnen finden sollten, wortwörtlich, was zum Beispiel in meinen Auseinandersetzungen mit dem Haeckelianismus stand.",
      "Die Menschen können eben nicht verstehen, wie wirkliche Anthroposophie, wenn sie übergeht in den Willen, zur Umwelt führt, das heißt, zum sachlichen Betrachten jedes Gebietes, das sie sich entsprechend vornimmt, daß man also nicht die Formeln, die auf einem Gebiete gelegen sind, in das andere einfach hereinzutragen braucht. Man kann es schon glauben, daß diejenigen, die gewohnt gewesen sind, wortwörtlich durch längere Zeiten dieses oder jenes zu hören, es dann ungewohnt finden und unbequem, das- selbe in einer anderen Sprache zu hören.",
      "Allein, die ver- schiedenen Lebensgebiete fordern verschiedene Sprachen. Und es handelt sich darum, daß, wenn über sie gesprochen wird, aus demselben Geiste gesprochen werde, aber nicht darum, daß man überall dieselben wortwörtlich gleich ausgedrückten Begriffe und Vorstellungen finde.",
      "Und in der Anthroposophie kommt es schon darauf an, daß man sie nicht bloß ihrem Wortlaute nach aufnehme, sondern daß man sie ihrem Geiste nach aufnehme. Dann wird man aber erkennen, wenn sie sich betätigen will in einem eminent praktischen Gebiet, wie es das der sozialen Frage ist: welche Betätigung da herausgefordert ist durch die Not der Zeit, durch alles, was an Niedergangskräften in unserer Zeit zutage tritt.",
      "Innerlich hängt eben diese Be- handlung der sozialen Frage durchaus zusammen mit dem, was eben von anderen Erkenntnisgesichtspunkten, aber nicht von anderen praktischen Gesichtspunkten aus auch durch die mehr theoretischen Seiten der Anthroposophie fließt. Daher muß ich Sie heute schon bitten, zu berück- sichtigen, daß ich abgehen muß von dem, was der Duktus 177 meiner bisherigen, eben in den Bahnen einer objektiven Wissenschaftlichkeit gehaltenen Vorträge ist.",
      "Denn es ist nötig, daß das, was im unmittelbaren Leben darinnen als Willensimpulse leben muß, was auch seine Stellung sich erst noch zu erkämpfen hat, daß das in anderer Form erfaßt wird, daß das in anderer Weise an unsere Seelen herantritt als das, von dem man sagen kann: So ist es! Sehen Sie auf dasjenige, was mit der Dreigliederung gegeben ist in meinem Buche «Die Kernpunkte der sozia- len Frage».",
      "Und ich will heute mehr vom Standpunkt der großen sozialen Praxis aus sprechen. Nicht theoretisch, sondern vom Standpunkte der sozialen Praxis aus möchte ich sprechen, von demjenigen, was zunächst im umfassenden Sinne getan werden muß.",
      "Was getan werden muß, hängt innerlich zusammen mit dem, was in den letzten Jahren in bezug auf die Dreigliederungsfrage getan worden ist, trotzdem es ein solches trampelndes Mißfallen der Kom- militonen hervorgerufen hat, wie es zum Beispiel vor- gestern in Stuttgart in einer so abscheulichen Form zutage getreten ist. Deshalb will ich auch ganz aus der Zeit her- aus Ihnen charakterisieren, wie das in diese Zeit hinein- gehört, was Sie seinem Inhalte nach lesen können in mei- nem Buche «Die Kernpunkte der sozialen Frage», in meinem Buch «In Ausführung der Dreigliederung», und was Sie dann nach verschiedenen Seiten charakterisiert finden wer- den in den Vorträgen, die heute hier noch gehalten werden.",
      "Ich möchte nur eine Art von Einleitung zu dem allge- meinen Ton geben, der dann angeschlagen werden wird. Aber ich möchte sagen, daß die Menschheit gerade da- durch, daß sie sich im Laufe der neueren Zeit aus den Gründen, die schon entwickelt worden sind, immer mehr und mehr - trotzdem sie glaubte, so recht praktisch zu sein, glaubte, die Praxis mit Löffeln gegessen zu haben - 178 hinaufhob zu einer Abstraktheit, die niemals woanders günstige Früchte tragen kann als in der naturwissenschaft- lichen Betrachtung des Unorganischen, daß die Menschheit dadurch ganz und gar unpraktisch wurde.",
      "Die Menschheit hatte sich eingelebt in diese Abstraktheit und hatte all- mählich begonnen, aus dieser Abstraktheit auch zu spre- chen über das, was uns unmittelbar als sozial konkretes Leben umgibt. Lesen Sie sich durch alle die theoretischen Auseinandersetzungen, die gewöhnlich moderne, gelehrte Volkswirtschafter ihrem System voransetzen, so werden Sie finden, wie da überall die Frage figuriert: Inwieweit kann überhaupt der wissenschaftliche Betrachter der Volks- wirtschaft hineinschauen in das, was sich unmittelbar praktisch um uns betätigend vollzieht?",
      "Und wie soll der Volkswirtschafter, um dem wissenschaftlichen Anspruch gerecht zu werden - das heißt aber nichts anderes, als dem wissenschaftlichen Anspruch, den man sich aus Gewohn- heit aus der naturwissenschaftlichen Betrachtung ange- eignet hat -, wie soll er sich verhalten, dieser Volkswirt- schafter, damit er diesen wissenschaftlichen Ansprüchen genügen kann? Daß Unklarheit in bezug auf diese Frage herrscht, daß sich in dieser Unklarheit Lebensfremdheit gegenüber dem wirklichen sozialen Leben ausdrückt, das hatte ich zu- nächst zu zeigen in meinem Buche «Die Kernpunkte der sozialen Frage», und daß diese Lebensfremdheit selber im heutigen sich verirrenden sozialen Leben lebt.",
      "Ich hatte zu zeigen, wie tatsächlich die führenden Menschenpersön- lichkeiten in dieser neueren, zur Abstraktion heraufeilen- den Zeit zwar die Möglichkeit gefunden haben, sich ein- zuleben in den technischen Betrieb und in den sozialen Betrieb der Kapitaltechnik, wie aber eben dadurch, daß das Hinschauen auf den Menschen verloren worden ist, von diesen führenden Persönlichkeiten nichts ausgegangen ist für das, was so eng mit dem Menschen und seiner Er- kenntnis zusammenhängt wie die soziale Frage. Hatte man doch auch philosophisch den Zusammenhang zwischen der theoretischen Erkenntnis und der sogenannten prakti- schen Erkenntnis verloren; trotz dem Schopenhauerschen Worte oder vielleicht eben wegen des Sinnes dieses Wor- tes, weil dieser Sinn so sehr lebte in der modernen Mensch- heit - trotz dem Worte: Moralpredigen sei leicht, Moral- begründen sei schwer , trotz diesem Worte konnte man nicht sehen, wie notwendig es ist, nach denjenigen Unter- gründen des Lebens zu suchen, die die Moral nicht nur predigen, wie Schopenhauer sagt, und damit einen theo- retischen Beweis für sie liefern wollen, sondern die die Moral durch Tatsachen begründen wollen, indem sie hin- weisen auf das, was in der Tatsachenwelt wirklich lebt.",
      "In der Kantischen Philosophie drückt sich die Verwir- rung über dieses Gebiet dadurch aus, daß überhaupt ein scharfer Schnitt gezogen worden ist zwischen dem, was theoretische Betrachtung ist, was kritisiert wird in der «Kritik der reinen Vernunft» und dem, was Inhalt eines bloßen Imperativs und daher eines bloßen Glaubens sein soll, und was kritisiert wird in der «Kritik der praktischen Vernunft». Da soll keine Brücke geschlagen werden dür- fen, wogegen sich schon, wie Sie von diesem Platze in diesen Tagen gehört haben, Goethe mit seinem Begriff der «anschauenden Urteilskraft», des «intellectus archetypus», gewendet hat, um dann zu versuchen, dem, was nun das wirklich Praktische ist in der Begründung des mensch- lichen Handelns, anders näherzukommen.",
      "Schopenhauer konnte es nicht finden, weil er das, was in der Vorstel- lungswelt lebt, von vornherein als etwas bloß so Bild- haftes ansah, daß es nicht durchdrungen werden könne 180 mit Seinsgehalt, und weil er bloß rekurrierte auf den Wil- len, der aber wiederum nicht für die gegenständliche Erkenntnis ohne höhere übersinnliche Erkenntnis ins Be- wußtsein heraufgebracht werden kann. So fühlte er das Unzulängliche der theoretischen Begründung eines prakti- schen Handelns.",
      "Durch die bloße theoretische Vernunft war er unvermögend, auf die Begründung des praktischen Handelns selber hinzuweisen, weil er ja im Willen nur ein Blindes sah, niemals ein von dem Lichte einer Erkennt- nis zu Durchdringendes. Denn dieses Licht kann nur das Übersinnliche sein.",
      "Und zu dem wollte sich Schopenhauer auch nicht erheben. Dann kamen andere Versuche, wie zum Beispiel der- jenige Herbarts. Bei Herbart finden wir den Versuch, eine Art Begründung im praktischen Leben für dasjenige, was praktisches Handeln ist, zu finden.",
      "Aber das Charak- teristische für Herbart ist, daß er in seiner praktischen Philosophie sucht, was im Grunde genommen ein ästheti- sches Urteil ist, daß er versucht, die praktische Philosophie als einen Teil der Ästhetik zu begründen. Dadurch kom- men - indem er implicite hinausgeht über das, was er theoretisch im Bewußtsein hat - die fünf bekannten prak- tischen Ideen der Vollkommenheit, des Wohlwollens, der inneren Freiheit, des Rechtes und der Billigkeit zum Vor- schein.",
      "Aber das Verhältnis des Menschen zu ihnen ist das einer Zustimmung, die auch erst wiederum der motivie- renden Kraft bedarf. Ich kann auch hier nur darauf hin- deuten, wie versucht worden ist, ich möchte sagen, zu durchbrechen, was mit dem bloß abstrahierenden Ver- stande gegeben war, wie aber dieser Versuch, weil er nicht vordringen wollte bis zur wirklichen Geisteswissenschaft, in allen möglichen Punkten mißlang.",
      "Daher muß ich darauf hinweisen, daß in dieser Ent- 181 Wickelung des neueren geschichtlichen Lebens der Mensch- heit die Begründung dafür liegt, daß die führenden Per- sönlichkeiten das nicht finden konnten, was an den Men- schen herankommt. Und so fanden sie den Weg zur Ma- schine, so fanden sie den Weg in die Technik, so fanden sie den Weg zum Kapitalismus.",
      "Sie fanden nicht den Weg zum Menschen, den sie neben der Maschine stehen ließen, genau ebenso wie der Naturforscher den wirklichen Men- schen neben dem stehen läßt, was er durch seine Natur- wissenschaft theoretisch erforscht. Was sich da in der Naturwissenschaft auslebt, das wur- zelt in einer tiefen Lebensgewohnheit und drückt sich auf allen Gebieten aus.",
      "Deshalb konnte das erste Kapitel mei- ner «Kernpunkte» nur so sein, daß es diese Wirkung eines lebensfremden Geisteslebens in der neueren Zeit beleuch- tet. Hingewiesen werden mußte scharf auf den Umstand, den mir nicht etwa eine theoretische Erwägung, sondern die in meinem Buche gekennzeichnete Lebenserfahrung geliefert hat, daß die Persönlichkeiten, welche die füh- renden waren bei allen Traditionen auf künstlerischem, religiösem und wissenschaftlichem Gebiet, neben dem, was die bloße Auffassung im Vorstellen in der neueren Zeit hervorgebracht hat, einen Gefühls-, einen religiösen Inhalt schufen, der in derjenigen Klasse nicht entstehen konnte, welche weggeholt wurde von dem Leben in der Tradition und an die Maschine hingestellt wurde, welche von dem, was in dieser neueren Zeit heraufkam, nur die theoretische Abstraktion aufnahm, so daß zu dem Leben in Mühe und Arbeit bei dieser Klasse noch das hinzutrat, was aus der ödigkeit der Seele kommt, die sich zwar theoretisch er- füllen kann mit dem, was eine theoretische naturwissen- schaftliche Denkweise geben kann, die aber nicht leben kann damit. 182 So war das, was leben sollte durch meine «Kernpunkte der sozialen Frage», und schon in dem ihnen vorangehen- den «Aufruf», im eminentesten Sinne praktisch gedacht, war als etwas gedacht, was unmittelbar in das Leben über- gehen muß, was nicht ergreifen sollte bloß die Intellekte, was ergreifen sollte den Willen.",
      "Und es war hervorgegan- gen aus dem, was den Willen ergreifen sollte. Als auch für eine größere Anzahl in der Außenwelt stehende Persönlichkeiten klar war, wie die furchtbaren katastrophalen Ereignisse aus dem zweiten Jahrzehnt des 20.",
      "Jahrhunderts verlaufen werden, da stellte sich in die Ereignisse etwas hinein - ich will heute, wie gesagt, nur Richtungen andeuten, Sie finden das Genauere darüber in meinen Schriften -, das die blutleerste Abstraktion war, etwas ganz und gar nur aus der abstrakten Geistigkeit Herausgeborenes. Mit dieser abstrakten Art der Geistigkeit war derjenige heraufgekommen, der aus einem Gelehrten Präsident der Vereinigten Staaten von Amerika geworden war, Woodrow Wilson.",
      "In seinen Vierzehn Punkten war auch als ein Impuls für das Praktische vor die Welt hin- gestellt, was nur aus einer lebensfremden Abstraktion her- vorging. Den praktischen Beweis dafür hat die Lage ge- liefert - Sie können das bei Maynard Keynes nachlesen -, in der sich Woodrow Wilson bei den Verhandlungen in Versailles befand, wo das, was in seiner Theorie lebte, immer mehr und mehr abschmolz gegenüber dem, was aus den veraltetsten traditionellen Anschauungen heraus da- zumal in Versailles ausgemacht worden war.",
      "Die geschicht- liche Entwickelung selber hat den Beweis für das Lebens- fremde der Vierzehn Punkte Woodrow Wilsons geliefert. Als sie aufgestellt wurden, da bezeugten sie aber, daß man mit solcher Abstraktion durchaus auch etwas in die Wirk- lichkeit hineintragen kann: man trägt in sie etwas hinein, 183 aber man trägt nur den Irrtum hinein!",
      "Es ist nicht so, daß Abstraktionen, wenn sie durch Menschen gehen, nicht Wirklichkeiten hervorzaubern könnten; aber es ist so, daß sie immer in diesen Wirklichkeiten Verwirrungen oder Unzulänglichkeiten werden hervorrufen müssen, weil sie eben nicht aus dem Leben geholt sind. So konnten die Vierzehn Punkte Schiffe und Heere über das Meer brin- gen, aber es konnten diese Vierzehn Punkte nicht einen lebenskräftigen Impuls in die moderne Zivilisation hin- einsenden.",
      "Ich fürchte, daß dasjenige, was damit innerhalb der modernen Zivilisation vorliegt, noch immer nicht von einer genügend großen Anzahl von Menschen irgendwie begrif- fen ist. Denn es folgte nun in der Nachkriegszeit in Amerika auf Woodrow Wilson Harding und wir haben vor kurzer Zeit die Antrittsrede dieses Harding lesen kön- nen: dieselben abstrakten Phrasen, dasselbe Reden von «menschlicher Brüderlichkeit», das nicht motivierend wer- den kann, weil es in Abstraktionen lebt, die Fortsetzung der Wilsonpolitik unter anderem Namen.",
      "Ich kann nicht finden, daß man in einer genügend großen Anzahl von Menschen genügendes Verständnis findet für die Unzu- länglichkeit, die sich hier fortsetzt. Es ist, als ob der moderne Mensch geradezu den Zusammenhang mit jedem Enthusiasmus für die Wahrheit, für die lebendige Wahr- heit verloren hätte und schlafend selbst vorbeigehen würde an einer solchen Lebensfremdheit, wie sie jetzt wiederum in der Antrittsrede des amerikanischen Präsidenten ge- klungen hat.",
      "Dazumal, als die Vierzehn Punkte zuerst hereintraten ins moderne Leben, da sollte entgegengesetzt werden dem- jenigen, was an Lebensfremdheit in diesen Vierzehn Punk- ten enthalten war, eine wirkliche Lebenspraxis, etwas, was 184 herausstammte aus dem Leben, herausstammte zu gleicher Zeit aus den wichtigsten Bestandteilen des modernen öffentlichen Lebens, aus der wirklichen sozialen Praxis, aus einem Erkennen desjenigen, was als soziale Frage durch die gegenwärtige Menschheit pulsiert. In einer lebenswirklichen Art habe ich in einem Stutt- garter Vortrage vor kurzer Zeit auf solche Dinge hinge- wiesen, nachdem Lloyd George den damals drohenden Streikausbruch verhindern wollte und die Verhältnisse leimte.",
      "Nach diesem Leimen der sozialen Verhältnisse sagte ich danach in Stuttgart: Man kann mit solchen Din- gen, die, trotzdem sie von Lloyd George kommen, durch- aus nur theoretisch gedacht sind, zwar die Verhältnisse leimen, aber man kann nicht Wirklichkeiten dirigieren, und die Menschen werden sich überzeugen, daß nur ge- leimt ist theoretisch, daß aber lebenspraktisch nichts er- reicht ist, und daß in Kürze sich das zeigen werde. - Jetzt haben Sie es! Jetzt können Sie sich durch dasjenige, was wirklich eingetreten ist, überzeugen davon, ob dazumal in jenem Stuttgarter Vortrage aus der Erkenntnis der sozialen Kräfte heraus oder ob auch nur theoretisch ge- sprochen worden ist, während man heute nicht nur theo- retisch spricht, sondern auch theoretisch handelt im öffent- lichen und namentlich im sozialen Leben, wo es nun wahr- haft gar nicht am Platze ist.",
      "Und so wurde denn dazumal, als, ich möchte sagen, in klassischer Weise die politische Frucht des modernen Ab- straktismus in den Vierzehn Punkten Woodrow Wilsons auftrat, versucht, bei denjenigen, die es dazumal mutlos, tatenunlustig anhörten, aber darauf in einer gewissen Weise neugierig waren, Verständnis zu erwecken dafür, daß von Europa aus - zunächst war nur Mitteleuropa zu- gänglich - in Kundgebungen der Dreigliederung des sozia- 185 len Organismus ein Konkretes, ein Lebenspraktisches ent- gegengestellt werde den unpraktischen Vierzehn Punkten. Und man hätte überzeugt sein können, wenn man Sinn für Wirklichkeiten, nicht bloß für liebgewordene Theorien gehabt hätte, die dann «praktisch» geworden sind, man hätte sich überzeugt halten können davon, daß, ebenso wie die unpraktischen Abstraktionen in der Wirklichkeit Heere und Schiffe auf den Weg gebracht haben, dasjenige, was aus einer Wirklichkeit heraus gesprochen hätte, wenn sie nur vom richtigen Platze aus vermittelt worden wäre, daß das auch Wirklichkeiten hervorgezaubert hätte.",
      "Aber die, die dazumal mitzureden hatten, sie wollten nicht hören. Die soziale Praxis lag ihnen ferne. Sie waren eingewöhnt in das, was sich herausgebildet hat im Laufe der neueren Zeit: hinzugehen den Weg bis zur Maschine, bis zur Maschinerie der sozialen Ordnung, aber nicht hin- zugehen den Weg zum Menschen, der an der Maschine steht, der da lebt als Mensch innerhalb der Maschinerie der sozialen Ordnung, und der als Mensch ein handelnder ist.",
      "Da man dazumal nicht verstanden hat, was die Lebens- notwendigkeiten forderten, so ergab sich als eine notwen- dige Konsequenz, daß, gleich nachdem die blutige Kriegs- katastrophe beendet war, auf Veranlassung Stuttgarter Freunde das geschehen ist, was in meinem «Aufruf an das deutsche Volk und die Kulturwelt» liegt, was in meinen «Kernpunkten der sozialen Frage» liegt. Und in der Zeit, in der auf gewissen Gebieten des modernen Zivilisations- lebens die alten Gewalten verschwunden waren, wurde versucht, zu den breiten Massen des Volkes zu reden, zu denjenigen, die durch all die Verhältnisse, die ich jetzt angedeutet und sonst immer wieder geschildert habe, am meisten gelitten haben.",
      "Der Anfang war im Grunde ein 186 guter. Man konnte die breite Masse des Volkes erreichen. Sie verstanden nach und nach, was in dem Impuls von der Dreigliederung des sozialen Organismus liegt. Denn es ist ein Humbug, zu sagen, daß das schwer verständlich sei in sich selber.",
      "Die Schwierigkeit des Verstehens beruht lediglich darauf, daß man aus den alten Denkgewohn- heiten nicht heraus kann, daß man nicht verzichten kann, das, woran man gewöhnt ist als starre Denkform, her- überzustülpen auf dasjenige, was eben als ein anderes auftritt. Darin liegt es, nicht in der Schwierigkeit der Sache.",
      "Deshalb war auch die Möglichkeit da, Verständnis zu finden gerade innerhalb derjenigen, die aus ihren Be- dürfnissen heraus nach einer relativen Lösung der sozialen Frage strebten, und die bis dahin schon gesehen hatten, daß sie aus dem alten dogmatischen Marxismus heraus zu keiner befriedigenden Gestaltung des sozialen Lebens in der neueren Zeit kommen können. Da wurde ein Strich durch die Rechnung gemacht da- durch, daß sich auf der einen Seite ablehnend verhielten, nicht die Arbeiter, wohl aber die Führer dieser Arbeiter, und auf der anderen Seite führende Persönlichkeiten des alten Bourgeoistums.",
      "Von allen Seiten wurde man sozu- sagen mit Bezug auf den Impuls der Dreigliederung im Stiche gelassen. Zunächst hatten es diejenigen, die führende Kreise wa- ren, im Frühling 1919 mit einer heillosen Angst zu tun, und sie schnappten nach allem, was sich irgendwie mit der sozialen Frage beschäftigte.",
      "Dadurch fanden sich einige dazumal im ersten Anhub zur Dreigliederung, wie sie an sie herankam, hatten aber nicht die Kraft und nicht den Mut, weiter dabei auszuhalten. Einer der gefeierten Führer der Bourgeoisie eines mitteleuropäischen Gebietes sagte mir, als wir dazumal mitten drinnen standen in dem, was 187 geschehen sollte: Ja, in der Art und Weise, wie Sie selber verstanden werden und reden zu der breiten Masse des Volkes, da könnte man sich ja etwas versprechen; aber eine solche Sache darf, das werden Sie einem Parteiführer der alten Parteien zugeben, nicht auf zwei Augen gestellt sein; andere sieht man noch nicht - ich zitiere nur -, die wirksam nach dieser Richtung wären; daher verlassen wir uns schon nicht auf diese ganze breite Bewegung, son- dern wir wollen die alte Ordnung, trotzdem sie vielleicht nur noch höchstens durch fünfzehn oder zwanzig Jahre zu halten ist, halten mit den Kanonen und Flinten.",
      "Das war das Echo von der einen Seite. Aber lassen Sie mich auch sprechen von dem Echo von der anderen Seite, weil ich praktisch zu charakterisieren habe, worum es sich handelt. Die arbeitende Bevölkerung, insofern ich zu ihr sprechen konnte, hat sich mit einer verhältnismäßigen Leichtigkeit und mit innerem Verständnis in die Drei- gliederungsbewegung hineinzuleben versucht.",
      "Da kamen die Arbeiterführer, und sie wurden, ich möchte sagen, blaß vor Neid, daß jetzt auch von anderer Seite als von Seiten ihres eingetrichterten Marxismus zu der Arbeiterschaft ge- sprochen werden konnte. Und sie erfanden, ebenso wie die anderen, alle möglichen Verleumdungen, alle möglichen Schmierigkeiten, um den Arbeitern, die ja autoritätsgläu- big in dieser Beziehung zu ihren Führern sind, den Weg zum Verständnisse zu verlegen.",
      "Die Arbeiter aber sind heute noch nicht so weit, um sich in dem aus den letzten Jahrzehnten herübergenommenen Autoritätsglauben in der rechten Art zurechtzufinden. In dem Augenblicke, wo man innerhalb der Arbeiterschaft einsehen wird, worum es sich den niederen und höheren Arbeiterführern handelt, wird manches zerstieben, was heute noch auf diesem Felde als gutgemeinter Glaube vorhanden ist, wenn man ein- 188 sehen wird, daß diejenigen, die etwa von der Sorte des Lenin und Trotzkij, des Lunatsdiarskij, an der Spitze stehen, in ihrem wirklichen Wollen nicht etwa das Glück und Wohlergehen der Menge im Auge haben, sondern daß sie zu sich und untereinander etwa sagen: Die breite Masse des Volkes ist dumm und wird immer von Leidenschaften durchsetzt sein; mit der kann man nichts machen, als sie tyrannisieren; daher muß es nicht auffällig sein, daß wir ebenso tyrannisieren, ob wir nun Zar Nikolaus oder Lenin heißen; für uns handelt es sich nur darum, daß diejenigen, die früher auf den kurulischen Stühlen gesessen haben, heruntergefallen sind und wir nun darauf sitzen; für uns handelt es sich um die Eroberung der Regierungssitze!",
      "In dem Augenblicke, in dem diese Erkenntnis in weite- sten Kreisen aufgehen wird, wird manches anders werden. Dann aber wird auch die Zeit gekommen sein, wo in das soziale Leben wirklich soziale Praxis wird einziehen kön- nen.",
      "Dann wird man mit praktischem Verständnisse das- jenige anschauen, was ich im zweiten und dritten Kapitel meiner «Kernpunkte der sozialen Frage», ich möchte sa- gen, wie exemplifizierend für das, was aus solchem Geiste heraus zu geschehen hat, ausgesprochen habe. Dann wird man sehen, daß da alles nicht aus einer Theorie heraus erfunden ist, sondern daß da alles aus einer schwer errun- genen Lebenspraxis heraus gewonnen ist, geradeso wie dazumal, als nach dem Bekanntwerden der Vierzehn Punkte Woodrow Wilsons diese Idee von der Dreigliede- rung des sozialen Organismus zuerst auftrat.",
      "Ich spreche als jemand, der sein halbes Leben, dreißig Jahre, in Österreich, in diesem Experimentierland für so- ziale Unmöglichkeiten zugebracht hat. Ich spreche als je- mand, der wohl weiß, wie man in diesem österreichischen Experimentierland in einem Ministerium, einem liberalen 189 Ministerium geredet hat.",
      "Der Liberale Giskra hat, als die Blütezeit des österreichischen Liberalismus war, und als schon hinter dem Liberalismus die soziale Frage auf- tauchte, gesagt: In Österreich haben wir mit der sozialen Frage nichts zu tun, denn die soziale Frage hört bei Boden- bach auf! Das wurde im Parlamente des Liberalismus in Österreich von dem verantwortlichen Minister des Innern verkündet, im letzten Drittel des 19.",
      "Jahrhunderts. Wer nun studieren will, wie in diesem österreichischen Parlamente, ich möchte sagen, in der Reinkultur gewirkt hat das unmögliche Durcheinandermischen der drei Glie- der des sozialen Organismus - was ich schon ausgedrückt habe in meinen «Kernpunkten», indem ich angeführt habe die Zusammensetzung des Parlaments aus vier Wirt- schaftskurien , der kann sehen, wie allmählich die Dinge sich entwickelten.",
      "Und wer das Ultimatum an Serbien verstehen will, der muß alles, was seit dem Jahre 1867 in Österreich geschehen ist bis zu den Zeiten hin, die dem Ultimatum an Serbien vorangingen, vollinhaltlich studie- ren. Dann wird er sehen, wie es ausgesehen hat mit dem Brotmangel, mit der Teuerung, mit den Teuerungskon- flikten in den Monaten, die dem Kriegsausbruch voran- gegangen sind gerade in österreichischen Landen, und er wird Gelegenheit haben, an den dortigen sozialen Fak- toren zu studieren, wo im Tieferen die wesentlichen Ur- sachen liegen.",
      "Und da würde man in eine neue Art der Betrachtungsweise hineingeführt werden. Aber was aus jeder solchen Betrachtung hervorgehen muß, das ist, daß es sich darum handelt, für das praktische soziale Leben Impulse zu finden, die aus diesem Leben selbst heraus sprechen.",
      "Dann werden wir vielleicht zu der Zeit kommen, in welcher es eine genügend große Anzahl von Menschen gibt, die - unbeirrt durch die alten Rich- 190 tungsbezeichnungen «rechts» und «links» ihre Aufmerk- samkeit dem Sachlich-Praktischen zuwenden, das, weil es eben aus der Wirklichkeit fließt, sich berufen glauben darf, mitzureden in den wichtigsten Angelegenheiten des Lebens. Und das sind die sozialen Angelegenheiten.",
      "Man stellt sich vielfach heute auf den Standpunkt, die Welt werde in Ordnung kommen, wenn es nur gelinge, die alten Impulse fortzusetzen, und man probiert jetzt schon wiederum seit langem, wie es gehen kann mit dem Fortlaufenlassen des Alten. Man wendet die Augen davon ab, wie unter diesem unsachlichen, wirklichkeitsfremden Operieren immer mehr hinaufkommt, was zermürbend zu gleicher Zeit wirken muß für die ganze moderne Zivilisa- tion.",
      "Nicht eher aber wird eine Möglichkeit entstehen weiter- zukommen, als dann, wenn man einsehen wird, wie ohne diesen Blick nach links oder rechts auf das sachliche Be- trachten des unmittelbaren Lebens losgegangen werden muß. Denn dadurch allein bekommen wir das Verständnis für solche praktisch-sozialen Ideen, welche ein ethisch- soziales Leben nicht nur predigen, sondern begründen können.",
      "Denn auf die Begründung dieses Lebens sollte hingewiesen werden mit der Dreigliederung des sozialen Organismus. Die Theoretiker haben aus ihren theoreti- schen Anschauungen heraus lange genug wiederholt, daß man heute «sozial» betrachten müsse, was auch in der Ethik lebt.",
      "Der Mensch sei hineingestellt seit der Arbeits- teilung ganz und gar ins soziale Gebiet, und man müsse «aus dem Sozialen heraus» begreifen, was im Menschen motivierend wirke, wenn er handeln solle. Solange dieses Urteil blutleer bleibt, solange es eine Abstraktion bleibt, so lange wird es nichts bewirken.",
      "Denn es ist als Abstraktion ebenso wahr wie falsch. Daß 191 es falsch ist, habe ich in meiner «Philosophie der Freiheit» gezeigt. Es hat die andere, die bedenkliche wahre Seite, daß der Mensch sich immer mehr und mehr mit seiner Freiheit an den objektiven Wirtschaftsprozeß und der- gleichen übergibt, wie das sogar theoretisch im Marxis- mus ausgeführt ist.",
      "Und indem der Mensch sich also dem Wirtschaftsprozeß oder dem Staatsprozeß oder den son- stigen sozialen Einrichtungen, die wir jetzt haben, über- gibt, wird natürlich immer mehr und mehr seine Tatmoti- vierung zu einer sozialen. Das kann und darf eingesehen werden.",
      "Denn daß Menschen mit Menschen lernen in Arbeitsteilung leben, darauf zielt die moderne Zivilisa- tion. Wenn aber die soziale Ordnung in dem Menschen ein sachgemäßes soziales Handeln motivieren soll, dann muß sie ein sozialer Organismus sein, der aus der inneren Gesetzmäßigkeit eines solchen Organismus heraus eben zur Motivierung des Willens befähigt ist, dann muß man durch einen lebensfähigen sozialen Organismus nicht nur Moral predigen, sondern soziale Moral begründen.",
      "Man muß Moral auf diesem Gebiete nicht durch Worte und Ideen, man muß sie durch die Sache, durch die Wirklich- keiten begründen. Wirklichkeiten sollten angeregt werden durch den Impuls der Dreigliederung des sozialen Orga- nismus.",
      "So wenig verstand man die Sache, daß sich die Abstrakt- linge sogar lustig machten, weil ich immer und immer wie- derum das Wort «Impuls» statt «Idee» gebrauchte, um anzudeuten, daß Kraft darinnen sein sollte in dieser Ten- denz des dreigegliederten sozialen Organismus, nicht bloß Rederei. Das sollte schon im Leben dieses Arbeitens zur Dreigliederung liegen: daß Wirklichkeit darinnen ist, nicht bloßes Reden.",
      "Sonst kann man auch als ethisierender Wanderredner, wie es jetzt so viele gibt, herumziehen 192 und den Leuten zureden wollen: Werdet nur wiederum ethisch, werdet nur wiederum gut, dann wird schon eine soziale Harmonie entstehen! - Ich habe zu denen, die es hören wollten, immer gesagt, wenn man zum Ofen im Zimmer spricht: Du Ofen, deiner Wesenheit nach ist es dein kategorischer Imperativ, das Zimmer warm zu machen - er wird das Zimmer nicht warm machen. Aber man braucht nicht zu predigen, wenn man Holz hineinlegt und es anzündet.",
      "Man braucht nicht theoretisch zu ethi- sieren, mystelnd zu ästhetisieren. Man hat nötig nicht bloß «praktische» Ideengemenge, sondern man hat nötig wirk- liche Impulse, um ideenerfüllte soziale Kräfte anzuregen, wenn es sich um soziale Praxis handeln soll.",
      "Und in dem Augenblicke, wo man aufbringen wird das Verständnis für diesen Tatbestand, wird man erst lernen, über das, was die Dreigliederung eigentlich will, richtig zu denken. Weil das aber hinunterreicht in Gemüt und Wille, so wird vorausgesetzt für dieses Verständnis der Dreigliede- rung nicht nur ein theoretisches Interesse an der Wahrheit und an einer theoretischen Diskussion, sondern vorausge- setzt wird Enthusiasmus und Bekenntnis für und gegen- über der Wahrheit.",
      "Solange wir nicht imstande sind, die Wahrheit in unseren Willen aufzunehmen, sie aus der Theorie herauszuholen und unseren ganzen Menschen da- mit zu durchdringen, kann auch nicht einmal der Anfang zu einer fruchtbaren Behandlung der sozialen Frage und sozialen Praxis entstehen. Darum handelt es sich: daß diejenigen, die Verständnis suchen für das, was Dreigliederung will, mit ihrem ganzen Menschen dieses Verständnis suchen mögen.",
      "Dann kommt Enthusiasmus nicht aus blinden Instinkten, sondern er wird angeregt aus lichtvoller Erkenntnis. Dann bleibt er selber nicht blind, sondern wird selber leuchten. Wenn 193 die Willensimpulse nicht aus Instinkten und Trieben kom- men, sondern aus einem Überschauen des sozialen Lebens, dann bleiben sie nicht blind und finster, dann werden sie selber sehend und leuchtend.",
      "Und daß Enthusiasmus und Wille gegenüber der Wahrheit in diesem Sinne immer leuchtender und leuchtender werde, davon hängt der Weg bezüglich des Impulses der Dreigliederung des sozialen Organismus ab. Und daß dasjenige, was nach dieser Rich- tung hier gesprochen werden kann, einiges dazu beitrage, in diesem Sinne nicht zu einem blinden und finsteren Enthusiasmus und Willen anzuregen, sondern zu licht- vollen willentlichen Gestaltungen des Lebens, das möchte ich hier am Schlüsse gerade dieser Betrachtung als eine Hoffnung ausgesprochen haben. 194"
    ],
    "sentences": [
      [
        "Gestatten Sie, daß ich heute anknüpfe an einiges, das ich gestern nur andeuten konnte und das uns dann überführen soll zu unserer heutigen Betrachtung.",
        "Ich hatte gestern an- zuknüpfen an einen Satz, der aus der Weltanschauung des II."
      ],
      [
        "Jahrhunderts, sofern diese in Mitteleuropa herrschte, hervorgegangen ist, an den Satz, daß die Zunge, so wie sie aus der Umgebung die Luft hereinzieht, so aus den Zäh- nen ziehe das Wort, das heißt die Kraft, zu sprechen.",
        "Und ich habe Sie darauf aufmerksam gemacht, wie der Gelehrte des 19."
      ],
      [
        "Jahrhunderts zu diesem Satze nur hinzu- zufügen hat, daß er darüber lachen könne.",
        "Aber ich habe auch charakterisiert den Abstand, der da liegt zwischen der Zeit, in die eine solche instinktive Anschauung wie die gestern zitierte hineinfällt, und dem Zeitalter, in dem dann diese philiströs-ironische Kritik sich geltend gemacht hat, jenem Zeitalter, das eben beginnt mit dem ersten Drittel des 15."
      ],
      [
        "Jahrhunderts.",
        "Jener Ausspruch fällt noch in das vorhergehende Zeitalter hinein und ist durch die Gründe, die ich Ihnen gestern angegeben habe, für dieses Zeitalter in einer gewissen Weise außerordentlich charak- teristisch."
      ],
      [
        "Als charakteristisch muß er aber auch empfunden wer- den seinem Inhalte nach.",
        "Denn ich habe Ihnen ja gestern auseinandergesetzt, wie man zum Verständnis der Sprach- fähigkeit und der Sprache überhaupt sich zunächst be- kanntmachen muß mit dem, was Geisteswissenschaft zu sagen hat im Sinne des von mir in meiner kleinen Schrift 169 «Die Erziehung des Kindes vom Gesichtspunkte der Gei- steswissenschaft» Ausgeführten."
      ],
      [
        "Ich habe dort gezeigt, welcher bedeutungsvolle Vorgang sich mit dem Zahn- wechsel vollzieht, wie dasjenige, was den Menschen als rhythmischen Menschen und Gliedmaßen-Stoffwechsel- menschen später noch erfüllt, ihn vorher aber ganz erfüllt hatte, sich zurückzieht aus der Nerven-Sinnesorganisation und daher gerade diesen Vorgang bewirkt, der dort in meiner Schrift «Die Erziehung des Kindes vom Gesichts- punkte der Geisteswissenschaft» als die Geburt des Äther- leibes formelhaft bezeichnet wird.",
        "Ich habe Sie dann hin- geführt dazu, wie in einer ähnlichen Weise jener Vorgang erfaßt werden muß, welcher etwa um das vierzehnte, fünfzehnte Jahr herum liegt, das Geschlechtsreifwerden, und ich habe ausgeführt, wie dasjenige, was da vorliegt, formelhaft mit dem Ausdruck umfaßt werden kann: Geburt des astralischen Leibes."
      ],
      [
        "Aber ich habe gesagt, daß die Ereignisse, die so im Leben des Menschen in irgend- einem Lebensabschnitte eintreten, in Metamorphose sich auch zu anderen Zeiten - aber eben dann in Metamor- phose vollziehen, und daß wir das, was sich zwischen dem Menschen und der Außenwelt äußerlich abspielt zur Zeit der Geschlechtsreife, innerlich zu suchen haben als einen Vorgang, der sich abspielt zwischen dem Geistig- Seelischen und dem Körperlich-Leiblichen innerhalb des Menschen als der Vorgang, der im wesentlichen das phy- siologische Korrelat ist für das Sprechenlernen des Kindes, daß man daher auch zu suchen habe die Anhaltspunkte zu einer wirklichen rationellen Sprachwissenschaft, indem man von einer durchdringenden anschauenden Erkenntnis dieses Vorganges ausgeht.",
        "Ich habe dann gesagt, daß durch die Begründung und Entwickelung der abstrakten Logik und des abstrakten 170 logischen Denkens diejenige Sphäre des Erlebens, in wel- cher sich lebendig abspielt, was zwischen dem Geistig- Seelischen und dem Leiblich-Physischen vorgeht, gewisser- maßen verlegt wird, hinuntergeschoben wird ins Unter- bewußte, und daß eben Aristoteles dadurch, daß er das Bewußtsein in die Abstraktion hineinleitete, abgeschnitten hat das Hinsehen nach dem Vorgeburtlichen."
      ],
      [
        "Denn hätte man, was man instinktiv im frühen Altertum konnte, jenes Wirken des Astralischen im Geschlechtsreifwerden und im Sprachlichen anschaulich vor sich gehabt, wie wir es jetzt wiederum erstreben müssen, dann hätte man auch das- jenige allmählich anschauend vor sich bekommen können, was die Verbindung des Ich selber mit dem ganzen phy- sisch-ätherisch-astralischen Menschen ist.",
        "Das heißt, man hätte auf diesem Gebiet vorrücken können durch die Er- kenntnis des Sprechenlernens zu der Erkenntnis der Ein- gliederung des menschlich geistig-seelischen Ich in sein Leiblich-Physisches."
      ],
      [
        "Und Aristoteles hat gerade deshalb sein Dogma aufgestellt, daß mit jeder einzelnen mensch- lichen Wesenheit, die hier geboren wird, auch das Seelisch- Geistige mitentstehe.",
        "Er hat damit aus der Welt der Er- kenntnis weggeschafft die Anschauung der präexistieren- den Menschenseele."
      ],
      [
        "Die Anschauung dieser präexistierenden Menschenseele gibt allein eine wirkliche Erkenntnis von der Ewigkeit der Menschenseele.",
        "Diese Erkenntnis wird durch keinerlei philosophische Spekulation geliefert, sondern einzig und allein durch ein anschauendes Urteil in der Richtung, die ich eben jetzt angedeutet habe."
      ],
      [
        "Dieses Dogma von dem Nichtvorhandensein der Präexistenz ist dann in die Kirchenlehre des Christentums übergegangen.",
        "Und man muß es streng betonen: daß die Leugnung der Präexistenz, indem sie dann durch Konzile gefestigt wurde, nicht christ- lich in wahrem Sinn des Wortes ist, sondern aristotelisch ist, und mit dem Eindringen des Aristotelismus in die Christenlehre zum christlichen Dogma geworden ist."
      ],
      [
        "In dem Augenblick, wo sich das Christentum von diesem Bestandteil des Aristotelismus wird frei machen können, wird die Bahn auch frei sein für ein Erkennen der Prä- existenz.",
        "Man muß sagen: diese Präexistenz, die bis zu Origenes auch nicht angezweifelt worden ist von der christlichen Lehre des Abendlandes, ist durch die staatliche Verfügung des Justinian, der mitgewirkt hat an der Verketzerung des Origenes, aus der Christenlehre des Abendlandes ver- schwunden."
      ],
      [
        "Es ist deshalb den Anhängern dieser nicht- christlichen Christenlehre des Abendlandes so unange- nehm, wenn irgend jemand auf die historischen Tatsachen in den ersten Jahrhunderten des Christentums aufmerk- sam macht.",
        "Sie rufen dann alles herbei, was sie an Un- wahrhaftigkeiten aufbringen können über Zusammen- hänge der Anthroposophie mit der Gnosis und so weiter."
      ],
      [
        "Nun, über diese Dinge kann ich hier nicht weiter mich verbreiten.",
        "Was ich aber sagen will, ist dieses: Wenn man das Geistig-Seelische im Menschen einzig und allein be- gründet auf das, was für die Anschauung des Bewußtseins seit der Geburt lebt, dann kommt man allmählich zu dem, was die Lehre von der Unsterblichkeit zu einem bloßen Glaubensartikel macht."
      ],
      [
        "Man kann sagen, was im Menschen vorgeburtlich, was präexistent war, das gerät durch den Durchgang durch die Geburt in einen völlig unbewußten Zustand.",
        "Das kann erst wiederum angeschaut werden, wenn man sich zur Imagination und zur Inspiration herauf erhebt."
      ],
      [
        "Aber am anderen Pol des Menschen erscheint es in seiner Willens- und emotionellen Natur.",
        "Wir haben ja im dreigliedrigen 172 Menschen auf der einen Seite den Nerven-Sinnesmenschen, der zusammenhängt mit dem vorstellenden Menschen, auf der anderen Seite den Gliedmaßen-Stoffwechselmenschen, der zusammenhängt mit der Willensnatur des Menschen und mit seiner emotioneilen Natur."
      ],
      [
        "Dadurch, daß das Vorstellungsleben abgedämpft ist, heruntergedämpft ist bis zum gegenständlichen Anschauen, dadurch ist zunächst für dieses gegenständliche Vorstellen im Erkennen ver- schlossen die Präexistenz.",
        "Aber was mit ihr gegeben ist, lebt in der Sphäre des Menschen, die am anderen Pol auf- tritt."
      ],
      [
        "Da tritt auf die Willensnatur, die Emotionsnatur.",
        "Aus dieser kann zunächst nicht eine Erkenntnis gewonnen werden, daher ein bloßer Glaube.",
        "Und wenn das, was vorgeburtlich ist, durch die Erweiterung der Erkenntnis Erkenntnis werden kann, so kann ohne diese Erweiterung der Erkenntnis das, was in Wille und Emotion lebt, nichts anderes werden als ein Glaubensartikel des Menschen."
      ],
      [
        "Da- her geschieht mit dem Hinabdämmern der übersinnlichen Erkenntnis auch das Hinabdämmern der Erkenntnis der Ewigkeit der Menschenseele bis in die Sprache hinein.",
        "Es müßte immerhin auffallen, daß wir in den bekannteren Zivilisationssprachen wohl ein Wort haben für Unsterb- lichkeit, das heißt, für das Leben im Nachtodlichen, daß wir aber nicht ein Wort haben, welches auf dem anderen Pol des Menschen die Ewigkeit der Menschenseele aus- drücken würde, das Ungeborensein."
      ],
      [
        "Das aber wird sich bis in die Sprache hinein die moderne Menschheit wieder erobern müssen: daß die Ewigkeit des Menschen ebenso wie sie nach der einen Seite, nach der Seite des Todes hin, in dem Worte Unsterblichkeit zum Vorschein kommt, auch nach der anderen Seite durch ein Wort wie «Unge- borensein» - das ja selbstverständlich mit der zunehmen- den Zivilisation geschickter werden wird - sichtbar wer- 173 den kann.",
        "Dann aber wird dasjenige, was über die Ewig- keit der Menschenseele zu sagen sein wird, nicht mehr bloßer Glaubensartikel sein, sondern ein Erkenntnisinhalt."
      ],
      [
        "Solange man bloß beim Nachtodlichen bleibt, muß die Unsterblichkeitsfrage eine Glaubensfrage sein.",
        "Sobald man übergeht zu einer wirklichen Erkenntnis des Übersinn- lichen, wird die Unsterblichkeitsfrage eine Frage der wirk- lichen Erkenntnis."
      ],
      [
        "Das ist ein Zusammenhang, der eingesehen werden muß, das ist ein Rubikon, der überschritten werden muß von der modernen Zivilisation.",
        "Denn was aus diesem Über- schreiten folgt, das wird nicht nur etwas sein, was theo- retisch wirkt, sondern das wird in einer ganz anderen Weise noch wirken."
      ],
      [
        "Wir können sagen: Lernen wir sach- gemäß aufsteigen von so etwas, wie es das Verständnis des Zahnwechsels, das Verständnis der Sprache ist, zu dem, wozu wir dann kommen, so eignen wir uns dadurch eine Erkenntnis des unsterblichen Wesens der Menschenseele an.",
        "Diejenigen, die im 11."
      ],
      [
        "Jahrhundert gedacht haben und davon gesprochen haben, daß die Zunge aus den Zähnen die Sprache saugt, haben nicht etwa geglaubt, daß es nur Zahnlaute gibt, wie Wilhelm Scherer sonderbarerweise voraussetzt, sondern sie waren in ihrem instinktiven Er- kennen durchdrungen davon, daß man, um die Sprache zu verstehen, hinunterdringen müsse in die menschliche We- senheit, so wie man beim Verstehen des Zahnwechsels hin- unterdringen müsse.",
        "Wie da die Kräfte heraufkommen, so müsse man hinunterdringen zu den Ursprüngen des Weges, der mit dem Zahnwechsel zu dem hinweist, was sich auf einem vorigen Schritte der Entwickelung des Men- schen gezeigt: zum Entstehen der Sprache."
      ],
      [
        "Instinktiv, un- terbewußt waren diese Erkenntnisse.",
        "Aber wer heute das Entsprechende aus dem Bewußtsein hervorholt, der wird finden, welche Tiefe sie in einer gewissen Beziehung atmen, und welche Philistrosität solche Einwände atmen wie die, von denen ich einzelne gestern besprochen habe."
      ],
      [
        "Wir ge- winnen aber auch, indem wir uns zu solchen Erkenntnissen wie denen über die Sprache hinaufschwingen, zu gleicher Zeit, ich möchte sagen, den Zugang zum Weg, die Un- sterblichkeit zu erkennen.",
        "Daher ist mit dem Erkennen dieser übersinnlichen Welt zu gleicher Zeit verbunden das Erringen eines gesunden Urteiles auch über das, was uns im Leben umgibt wie die Sprache."
      ],
      [
        "Und wir können nicht, ohne innerlich unehrlich zu werden, vorgeben, einzudrin- gen in so etwas in unserer Umgebung, wie es die Sprache ist, wenn wir nicht zu gleicher Zeit zugeben: hier liegen Grenzen vor, die nicht bloß als Grenzen der gewohnten Erkenntnis anzuerkennen sind, sondern die notwendig machen, daß sie überschritten werden durch eine anders- artige Erkenntnis.",
        "So hängt wirkliche Erkenntnis der äußeren Sinnenwelt schon zusammen mit dem Aufschwung zur übersinnlichen Erkenntnis."
      ],
      [
        "So müssen in der wirklich gesunden Erkennt- nis übersinnliche Anschauung und sinnliche Anschauung zusammenwirken, und es muß das eine das andere tragen.",
        "Deshalb darf man glauben, daß mit dem Erringen ge- sunder Urteile über das Übersinnliche auch gesunde Ur- teile in bezug auf das gewonnen werden können, was uns auf einem anderen Gebiete als Menschen umgibt, mit dem wir als Menschen zusammenhängen und innige Verhält- nisse eingehen müssen: das soziale Leben."
      ],
      [
        "In dem Duktus meiner bisherigen Vorträge habe ich so viel als möglich versucht, mich an das zu halten, was man etwa einen ganz wissenschaftlichen Duktus nennen könnte.",
        "Indem wir heute überzugehen haben zu dem, was als So- zialwissenschaft und soziale Praxis aus einer solchen inne- ren Seelenverfassung folgt, wie sie aus Geisteswissenschaft, wie sie hier gemeint ist, sich ergeben muß, da stehen wir in der Gegenwart selber inmitten der Praxis."
      ],
      [
        "Denn was in sozialer Beziehung zu sagen ist, das kann heute durchaus nicht etwa in der gleichen Weise betrachtet werden wie das, was vorangegangen ist.",
        "Es ist notwendig, daß man folgendes noch berücksich- tigt."
      ],
      [
        "Indem man zur Imagination, Inspiration und so weiter sich hinaufschwingt, wird das, was sonst vorstel- lungsmäßig ist und nicht unmittelbar den Willen motivie- rend sein kann, in den Willen hineingedrängt.",
        "Daher ist übersinnliche Erkenntnis willensmotivierend, und es gibt auch kein sittliches oder religiöses Ideal, welches nicht wenigstens unbewußt im Übersinnlichen wurzelte."
      ],
      [
        "Was durch die Vorstellung nur aus dem Sinnlichen gewonnen wird, kann niemals sozial oder sittlich motivierend sein, weil es unwirksam bleibt für den Willen.",
        "Deshalb muß man schon sagen, es könnte vielleicht auffällig sein, daß die Menschen, welche meine Schrift über das soziale Leben von der Dreigliederung in die Hand bekamen, wenn sie in dieser Schrift lasen, nun so gar nichts darinnen fanden von dem, was sie gewohnt waren zum Beispiel in meinen anthroposophischen Schriften als den Grundton zu finden."
      ],
      [
        "Man hat vielleicht von manchen Seiten erwartet: wenn derjenige, der sich zur Anthroposophie bekennt, über ein solches Thema schreibt, wie es in meiner Dreigliederung enthalten ist, dann müsse in alle die Einzelheiten, die da auseinandergesetzt werden, alles mögliche hineinfließen von den gewohnten «anthroposophischen» Urteilen; man müsse recht sehr mystelnd zu allerlei Ermahnungen schrei- ten und so weiter.",
        "Wenn auch von anthroposophischer Seite her vielfach ein solches Urteil gehört worden ist, dann kommt das den 176 Urteilen in der Qualität ganz gleich, die da wollten, als ich meine «Theosophie» schrieb, daß sie dasselbe darinnen finden sollten, wortwörtlich, was zum Beispiel in meinen Auseinandersetzungen mit dem Haeckelianismus stand."
      ],
      [
        "Die Menschen können eben nicht verstehen, wie wirkliche Anthroposophie, wenn sie übergeht in den Willen, zur Umwelt führt, das heißt, zum sachlichen Betrachten jedes Gebietes, das sie sich entsprechend vornimmt, daß man also nicht die Formeln, die auf einem Gebiete gelegen sind, in das andere einfach hereinzutragen braucht.",
        "Man kann es schon glauben, daß diejenigen, die gewohnt gewesen sind, wortwörtlich durch längere Zeiten dieses oder jenes zu hören, es dann ungewohnt finden und unbequem, das- selbe in einer anderen Sprache zu hören."
      ],
      [
        "Allein, die ver- schiedenen Lebensgebiete fordern verschiedene Sprachen.",
        "Und es handelt sich darum, daß, wenn über sie gesprochen wird, aus demselben Geiste gesprochen werde, aber nicht darum, daß man überall dieselben wortwörtlich gleich ausgedrückten Begriffe und Vorstellungen finde."
      ],
      [
        "Und in der Anthroposophie kommt es schon darauf an, daß man sie nicht bloß ihrem Wortlaute nach aufnehme, sondern daß man sie ihrem Geiste nach aufnehme.",
        "Dann wird man aber erkennen, wenn sie sich betätigen will in einem eminent praktischen Gebiet, wie es das der sozialen Frage ist: welche Betätigung da herausgefordert ist durch die Not der Zeit, durch alles, was an Niedergangskräften in unserer Zeit zutage tritt."
      ],
      [
        "Innerlich hängt eben diese Be- handlung der sozialen Frage durchaus zusammen mit dem, was eben von anderen Erkenntnisgesichtspunkten, aber nicht von anderen praktischen Gesichtspunkten aus auch durch die mehr theoretischen Seiten der Anthroposophie fließt.",
        "Daher muß ich Sie heute schon bitten, zu berück- sichtigen, daß ich abgehen muß von dem, was der Duktus 177 meiner bisherigen, eben in den Bahnen einer objektiven Wissenschaftlichkeit gehaltenen Vorträge ist."
      ],
      [
        "Denn es ist nötig, daß das, was im unmittelbaren Leben darinnen als Willensimpulse leben muß, was auch seine Stellung sich erst noch zu erkämpfen hat, daß das in anderer Form erfaßt wird, daß das in anderer Weise an unsere Seelen herantritt als das, von dem man sagen kann: So ist es!",
        "Sehen Sie auf dasjenige, was mit der Dreigliederung gegeben ist in meinem Buche «Die Kernpunkte der sozia- len Frage»."
      ],
      [
        "Und ich will heute mehr vom Standpunkt der großen sozialen Praxis aus sprechen.",
        "Nicht theoretisch, sondern vom Standpunkte der sozialen Praxis aus möchte ich sprechen, von demjenigen, was zunächst im umfassenden Sinne getan werden muß."
      ],
      [
        "Was getan werden muß, hängt innerlich zusammen mit dem, was in den letzten Jahren in bezug auf die Dreigliederungsfrage getan worden ist, trotzdem es ein solches trampelndes Mißfallen der Kom- militonen hervorgerufen hat, wie es zum Beispiel vor- gestern in Stuttgart in einer so abscheulichen Form zutage getreten ist.",
        "Deshalb will ich auch ganz aus der Zeit her- aus Ihnen charakterisieren, wie das in diese Zeit hinein- gehört, was Sie seinem Inhalte nach lesen können in mei- nem Buche «Die Kernpunkte der sozialen Frage», in meinem Buch «In Ausführung der Dreigliederung», und was Sie dann nach verschiedenen Seiten charakterisiert finden wer- den in den Vorträgen, die heute hier noch gehalten werden."
      ],
      [
        "Ich möchte nur eine Art von Einleitung zu dem allge- meinen Ton geben, der dann angeschlagen werden wird.",
        "Aber ich möchte sagen, daß die Menschheit gerade da- durch, daß sie sich im Laufe der neueren Zeit aus den Gründen, die schon entwickelt worden sind, immer mehr und mehr - trotzdem sie glaubte, so recht praktisch zu sein, glaubte, die Praxis mit Löffeln gegessen zu haben - 178 hinaufhob zu einer Abstraktheit, die niemals woanders günstige Früchte tragen kann als in der naturwissenschaft- lichen Betrachtung des Unorganischen, daß die Menschheit dadurch ganz und gar unpraktisch wurde."
      ],
      [
        "Die Menschheit hatte sich eingelebt in diese Abstraktheit und hatte all- mählich begonnen, aus dieser Abstraktheit auch zu spre- chen über das, was uns unmittelbar als sozial konkretes Leben umgibt.",
        "Lesen Sie sich durch alle die theoretischen Auseinandersetzungen, die gewöhnlich moderne, gelehrte Volkswirtschafter ihrem System voransetzen, so werden Sie finden, wie da überall die Frage figuriert: Inwieweit kann überhaupt der wissenschaftliche Betrachter der Volks- wirtschaft hineinschauen in das, was sich unmittelbar praktisch um uns betätigend vollzieht?"
      ],
      [
        "Und wie soll der Volkswirtschafter, um dem wissenschaftlichen Anspruch gerecht zu werden - das heißt aber nichts anderes, als dem wissenschaftlichen Anspruch, den man sich aus Gewohn- heit aus der naturwissenschaftlichen Betrachtung ange- eignet hat -, wie soll er sich verhalten, dieser Volkswirt- schafter, damit er diesen wissenschaftlichen Ansprüchen genügen kann?",
        "Daß Unklarheit in bezug auf diese Frage herrscht, daß sich in dieser Unklarheit Lebensfremdheit gegenüber dem wirklichen sozialen Leben ausdrückt, das hatte ich zu- nächst zu zeigen in meinem Buche «Die Kernpunkte der sozialen Frage», und daß diese Lebensfremdheit selber im heutigen sich verirrenden sozialen Leben lebt."
      ],
      [
        "Ich hatte zu zeigen, wie tatsächlich die führenden Menschenpersön- lichkeiten in dieser neueren, zur Abstraktion heraufeilen- den Zeit zwar die Möglichkeit gefunden haben, sich ein- zuleben in den technischen Betrieb und in den sozialen Betrieb der Kapitaltechnik, wie aber eben dadurch, daß das Hinschauen auf den Menschen verloren worden ist, von diesen führenden Persönlichkeiten nichts ausgegangen ist für das, was so eng mit dem Menschen und seiner Er- kenntnis zusammenhängt wie die soziale Frage.",
        "Hatte man doch auch philosophisch den Zusammenhang zwischen der theoretischen Erkenntnis und der sogenannten prakti- schen Erkenntnis verloren; trotz dem Schopenhauerschen Worte oder vielleicht eben wegen des Sinnes dieses Wor- tes, weil dieser Sinn so sehr lebte in der modernen Mensch- heit - trotz dem Worte: Moralpredigen sei leicht, Moral- begründen sei schwer , trotz diesem Worte konnte man nicht sehen, wie notwendig es ist, nach denjenigen Unter- gründen des Lebens zu suchen, die die Moral nicht nur predigen, wie Schopenhauer sagt, und damit einen theo- retischen Beweis für sie liefern wollen, sondern die die Moral durch Tatsachen begründen wollen, indem sie hin- weisen auf das, was in der Tatsachenwelt wirklich lebt."
      ],
      [
        "In der Kantischen Philosophie drückt sich die Verwir- rung über dieses Gebiet dadurch aus, daß überhaupt ein scharfer Schnitt gezogen worden ist zwischen dem, was theoretische Betrachtung ist, was kritisiert wird in der «Kritik der reinen Vernunft» und dem, was Inhalt eines bloßen Imperativs und daher eines bloßen Glaubens sein soll, und was kritisiert wird in der «Kritik der praktischen Vernunft».",
        "Da soll keine Brücke geschlagen werden dür- fen, wogegen sich schon, wie Sie von diesem Platze in diesen Tagen gehört haben, Goethe mit seinem Begriff der «anschauenden Urteilskraft», des «intellectus archetypus», gewendet hat, um dann zu versuchen, dem, was nun das wirklich Praktische ist in der Begründung des mensch- lichen Handelns, anders näherzukommen."
      ],
      [
        "Schopenhauer konnte es nicht finden, weil er das, was in der Vorstel- lungswelt lebt, von vornherein als etwas bloß so Bild- haftes ansah, daß es nicht durchdrungen werden könne 180 mit Seinsgehalt, und weil er bloß rekurrierte auf den Wil- len, der aber wiederum nicht für die gegenständliche Erkenntnis ohne höhere übersinnliche Erkenntnis ins Be- wußtsein heraufgebracht werden kann.",
        "So fühlte er das Unzulängliche der theoretischen Begründung eines prakti- schen Handelns."
      ],
      [
        "Durch die bloße theoretische Vernunft war er unvermögend, auf die Begründung des praktischen Handelns selber hinzuweisen, weil er ja im Willen nur ein Blindes sah, niemals ein von dem Lichte einer Erkennt- nis zu Durchdringendes.",
        "Denn dieses Licht kann nur das Übersinnliche sein."
      ],
      [
        "Und zu dem wollte sich Schopenhauer auch nicht erheben.",
        "Dann kamen andere Versuche, wie zum Beispiel der- jenige Herbarts.",
        "Bei Herbart finden wir den Versuch, eine Art Begründung im praktischen Leben für dasjenige, was praktisches Handeln ist, zu finden."
      ],
      [
        "Aber das Charak- teristische für Herbart ist, daß er in seiner praktischen Philosophie sucht, was im Grunde genommen ein ästheti- sches Urteil ist, daß er versucht, die praktische Philosophie als einen Teil der Ästhetik zu begründen.",
        "Dadurch kom- men - indem er implicite hinausgeht über das, was er theoretisch im Bewußtsein hat - die fünf bekannten prak- tischen Ideen der Vollkommenheit, des Wohlwollens, der inneren Freiheit, des Rechtes und der Billigkeit zum Vor- schein."
      ],
      [
        "Aber das Verhältnis des Menschen zu ihnen ist das einer Zustimmung, die auch erst wiederum der motivie- renden Kraft bedarf.",
        "Ich kann auch hier nur darauf hin- deuten, wie versucht worden ist, ich möchte sagen, zu durchbrechen, was mit dem bloß abstrahierenden Ver- stande gegeben war, wie aber dieser Versuch, weil er nicht vordringen wollte bis zur wirklichen Geisteswissenschaft, in allen möglichen Punkten mißlang."
      ],
      [
        "Daher muß ich darauf hinweisen, daß in dieser Ent- 181 Wickelung des neueren geschichtlichen Lebens der Mensch- heit die Begründung dafür liegt, daß die führenden Per- sönlichkeiten das nicht finden konnten, was an den Men- schen herankommt.",
        "Und so fanden sie den Weg zur Ma- schine, so fanden sie den Weg in die Technik, so fanden sie den Weg zum Kapitalismus."
      ],
      [
        "Sie fanden nicht den Weg zum Menschen, den sie neben der Maschine stehen ließen, genau ebenso wie der Naturforscher den wirklichen Men- schen neben dem stehen läßt, was er durch seine Natur- wissenschaft theoretisch erforscht.",
        "Was sich da in der Naturwissenschaft auslebt, das wur- zelt in einer tiefen Lebensgewohnheit und drückt sich auf allen Gebieten aus."
      ],
      [
        "Deshalb konnte das erste Kapitel mei- ner «Kernpunkte» nur so sein, daß es diese Wirkung eines lebensfremden Geisteslebens in der neueren Zeit beleuch- tet.",
        "Hingewiesen werden mußte scharf auf den Umstand, den mir nicht etwa eine theoretische Erwägung, sondern die in meinem Buche gekennzeichnete Lebenserfahrung geliefert hat, daß die Persönlichkeiten, welche die füh- renden waren bei allen Traditionen auf künstlerischem, religiösem und wissenschaftlichem Gebiet, neben dem, was die bloße Auffassung im Vorstellen in der neueren Zeit hervorgebracht hat, einen Gefühls-, einen religiösen Inhalt schufen, der in derjenigen Klasse nicht entstehen konnte, welche weggeholt wurde von dem Leben in der Tradition und an die Maschine hingestellt wurde, welche von dem, was in dieser neueren Zeit heraufkam, nur die theoretische Abstraktion aufnahm, so daß zu dem Leben in Mühe und Arbeit bei dieser Klasse noch das hinzutrat, was aus der ödigkeit der Seele kommt, die sich zwar theoretisch er- füllen kann mit dem, was eine theoretische naturwissen- schaftliche Denkweise geben kann, die aber nicht leben kann damit. 182 So war das, was leben sollte durch meine «Kernpunkte der sozialen Frage», und schon in dem ihnen vorangehen- den «Aufruf», im eminentesten Sinne praktisch gedacht, war als etwas gedacht, was unmittelbar in das Leben über- gehen muß, was nicht ergreifen sollte bloß die Intellekte, was ergreifen sollte den Willen."
      ],
      [
        "Und es war hervorgegan- gen aus dem, was den Willen ergreifen sollte.",
        "Als auch für eine größere Anzahl in der Außenwelt stehende Persönlichkeiten klar war, wie die furchtbaren katastrophalen Ereignisse aus dem zweiten Jahrzehnt des 20."
      ],
      [
        "Jahrhunderts verlaufen werden, da stellte sich in die Ereignisse etwas hinein - ich will heute, wie gesagt, nur Richtungen andeuten, Sie finden das Genauere darüber in meinen Schriften -, das die blutleerste Abstraktion war, etwas ganz und gar nur aus der abstrakten Geistigkeit Herausgeborenes.",
        "Mit dieser abstrakten Art der Geistigkeit war derjenige heraufgekommen, der aus einem Gelehrten Präsident der Vereinigten Staaten von Amerika geworden war, Woodrow Wilson."
      ],
      [
        "In seinen Vierzehn Punkten war auch als ein Impuls für das Praktische vor die Welt hin- gestellt, was nur aus einer lebensfremden Abstraktion her- vorging.",
        "Den praktischen Beweis dafür hat die Lage ge- liefert - Sie können das bei Maynard Keynes nachlesen -, in der sich Woodrow Wilson bei den Verhandlungen in Versailles befand, wo das, was in seiner Theorie lebte, immer mehr und mehr abschmolz gegenüber dem, was aus den veraltetsten traditionellen Anschauungen heraus da- zumal in Versailles ausgemacht worden war."
      ],
      [
        "Die geschicht- liche Entwickelung selber hat den Beweis für das Lebens- fremde der Vierzehn Punkte Woodrow Wilsons geliefert.",
        "Als sie aufgestellt wurden, da bezeugten sie aber, daß man mit solcher Abstraktion durchaus auch etwas in die Wirk- lichkeit hineintragen kann: man trägt in sie etwas hinein, 183 aber man trägt nur den Irrtum hinein!"
      ],
      [
        "Es ist nicht so, daß Abstraktionen, wenn sie durch Menschen gehen, nicht Wirklichkeiten hervorzaubern könnten; aber es ist so, daß sie immer in diesen Wirklichkeiten Verwirrungen oder Unzulänglichkeiten werden hervorrufen müssen, weil sie eben nicht aus dem Leben geholt sind.",
        "So konnten die Vierzehn Punkte Schiffe und Heere über das Meer brin- gen, aber es konnten diese Vierzehn Punkte nicht einen lebenskräftigen Impuls in die moderne Zivilisation hin- einsenden."
      ],
      [
        "Ich fürchte, daß dasjenige, was damit innerhalb der modernen Zivilisation vorliegt, noch immer nicht von einer genügend großen Anzahl von Menschen irgendwie begrif- fen ist.",
        "Denn es folgte nun in der Nachkriegszeit in Amerika auf Woodrow Wilson Harding und wir haben vor kurzer Zeit die Antrittsrede dieses Harding lesen kön- nen: dieselben abstrakten Phrasen, dasselbe Reden von «menschlicher Brüderlichkeit», das nicht motivierend wer- den kann, weil es in Abstraktionen lebt, die Fortsetzung der Wilsonpolitik unter anderem Namen."
      ],
      [
        "Ich kann nicht finden, daß man in einer genügend großen Anzahl von Menschen genügendes Verständnis findet für die Unzu- länglichkeit, die sich hier fortsetzt.",
        "Es ist, als ob der moderne Mensch geradezu den Zusammenhang mit jedem Enthusiasmus für die Wahrheit, für die lebendige Wahr- heit verloren hätte und schlafend selbst vorbeigehen würde an einer solchen Lebensfremdheit, wie sie jetzt wiederum in der Antrittsrede des amerikanischen Präsidenten ge- klungen hat."
      ],
      [
        "Dazumal, als die Vierzehn Punkte zuerst hereintraten ins moderne Leben, da sollte entgegengesetzt werden dem- jenigen, was an Lebensfremdheit in diesen Vierzehn Punk- ten enthalten war, eine wirkliche Lebenspraxis, etwas, was 184 herausstammte aus dem Leben, herausstammte zu gleicher Zeit aus den wichtigsten Bestandteilen des modernen öffentlichen Lebens, aus der wirklichen sozialen Praxis, aus einem Erkennen desjenigen, was als soziale Frage durch die gegenwärtige Menschheit pulsiert.",
        "In einer lebenswirklichen Art habe ich in einem Stutt- garter Vortrage vor kurzer Zeit auf solche Dinge hinge- wiesen, nachdem Lloyd George den damals drohenden Streikausbruch verhindern wollte und die Verhältnisse leimte."
      ],
      [
        "Nach diesem Leimen der sozialen Verhältnisse sagte ich danach in Stuttgart: Man kann mit solchen Din- gen, die, trotzdem sie von Lloyd George kommen, durch- aus nur theoretisch gedacht sind, zwar die Verhältnisse leimen, aber man kann nicht Wirklichkeiten dirigieren, und die Menschen werden sich überzeugen, daß nur ge- leimt ist theoretisch, daß aber lebenspraktisch nichts er- reicht ist, und daß in Kürze sich das zeigen werde. - Jetzt haben Sie es!",
        "Jetzt können Sie sich durch dasjenige, was wirklich eingetreten ist, überzeugen davon, ob dazumal in jenem Stuttgarter Vortrage aus der Erkenntnis der sozialen Kräfte heraus oder ob auch nur theoretisch ge- sprochen worden ist, während man heute nicht nur theo- retisch spricht, sondern auch theoretisch handelt im öffent- lichen und namentlich im sozialen Leben, wo es nun wahr- haft gar nicht am Platze ist."
      ],
      [
        "Und so wurde denn dazumal, als, ich möchte sagen, in klassischer Weise die politische Frucht des modernen Ab- straktismus in den Vierzehn Punkten Woodrow Wilsons auftrat, versucht, bei denjenigen, die es dazumal mutlos, tatenunlustig anhörten, aber darauf in einer gewissen Weise neugierig waren, Verständnis zu erwecken dafür, daß von Europa aus - zunächst war nur Mitteleuropa zu- gänglich - in Kundgebungen der Dreigliederung des sozia- 185 len Organismus ein Konkretes, ein Lebenspraktisches ent- gegengestellt werde den unpraktischen Vierzehn Punkten.",
        "Und man hätte überzeugt sein können, wenn man Sinn für Wirklichkeiten, nicht bloß für liebgewordene Theorien gehabt hätte, die dann «praktisch» geworden sind, man hätte sich überzeugt halten können davon, daß, ebenso wie die unpraktischen Abstraktionen in der Wirklichkeit Heere und Schiffe auf den Weg gebracht haben, dasjenige, was aus einer Wirklichkeit heraus gesprochen hätte, wenn sie nur vom richtigen Platze aus vermittelt worden wäre, daß das auch Wirklichkeiten hervorgezaubert hätte."
      ],
      [
        "Aber die, die dazumal mitzureden hatten, sie wollten nicht hören.",
        "Die soziale Praxis lag ihnen ferne.",
        "Sie waren eingewöhnt in das, was sich herausgebildet hat im Laufe der neueren Zeit: hinzugehen den Weg bis zur Maschine, bis zur Maschinerie der sozialen Ordnung, aber nicht hin- zugehen den Weg zum Menschen, der an der Maschine steht, der da lebt als Mensch innerhalb der Maschinerie der sozialen Ordnung, und der als Mensch ein handelnder ist."
      ],
      [
        "Da man dazumal nicht verstanden hat, was die Lebens- notwendigkeiten forderten, so ergab sich als eine notwen- dige Konsequenz, daß, gleich nachdem die blutige Kriegs- katastrophe beendet war, auf Veranlassung Stuttgarter Freunde das geschehen ist, was in meinem «Aufruf an das deutsche Volk und die Kulturwelt» liegt, was in meinen «Kernpunkten der sozialen Frage» liegt.",
        "Und in der Zeit, in der auf gewissen Gebieten des modernen Zivilisations- lebens die alten Gewalten verschwunden waren, wurde versucht, zu den breiten Massen des Volkes zu reden, zu denjenigen, die durch all die Verhältnisse, die ich jetzt angedeutet und sonst immer wieder geschildert habe, am meisten gelitten haben."
      ],
      [
        "Der Anfang war im Grunde ein 186 guter.",
        "Man konnte die breite Masse des Volkes erreichen.",
        "Sie verstanden nach und nach, was in dem Impuls von der Dreigliederung des sozialen Organismus liegt.",
        "Denn es ist ein Humbug, zu sagen, daß das schwer verständlich sei in sich selber."
      ],
      [
        "Die Schwierigkeit des Verstehens beruht lediglich darauf, daß man aus den alten Denkgewohn- heiten nicht heraus kann, daß man nicht verzichten kann, das, woran man gewöhnt ist als starre Denkform, her- überzustülpen auf dasjenige, was eben als ein anderes auftritt.",
        "Darin liegt es, nicht in der Schwierigkeit der Sache."
      ],
      [
        "Deshalb war auch die Möglichkeit da, Verständnis zu finden gerade innerhalb derjenigen, die aus ihren Be- dürfnissen heraus nach einer relativen Lösung der sozialen Frage strebten, und die bis dahin schon gesehen hatten, daß sie aus dem alten dogmatischen Marxismus heraus zu keiner befriedigenden Gestaltung des sozialen Lebens in der neueren Zeit kommen können.",
        "Da wurde ein Strich durch die Rechnung gemacht da- durch, daß sich auf der einen Seite ablehnend verhielten, nicht die Arbeiter, wohl aber die Führer dieser Arbeiter, und auf der anderen Seite führende Persönlichkeiten des alten Bourgeoistums."
      ],
      [
        "Von allen Seiten wurde man sozu- sagen mit Bezug auf den Impuls der Dreigliederung im Stiche gelassen.",
        "Zunächst hatten es diejenigen, die führende Kreise wa- ren, im Frühling 1919 mit einer heillosen Angst zu tun, und sie schnappten nach allem, was sich irgendwie mit der sozialen Frage beschäftigte."
      ],
      [
        "Dadurch fanden sich einige dazumal im ersten Anhub zur Dreigliederung, wie sie an sie herankam, hatten aber nicht die Kraft und nicht den Mut, weiter dabei auszuhalten.",
        "Einer der gefeierten Führer der Bourgeoisie eines mitteleuropäischen Gebietes sagte mir, als wir dazumal mitten drinnen standen in dem, was 187 geschehen sollte: Ja, in der Art und Weise, wie Sie selber verstanden werden und reden zu der breiten Masse des Volkes, da könnte man sich ja etwas versprechen; aber eine solche Sache darf, das werden Sie einem Parteiführer der alten Parteien zugeben, nicht auf zwei Augen gestellt sein; andere sieht man noch nicht - ich zitiere nur -, die wirksam nach dieser Richtung wären; daher verlassen wir uns schon nicht auf diese ganze breite Bewegung, son- dern wir wollen die alte Ordnung, trotzdem sie vielleicht nur noch höchstens durch fünfzehn oder zwanzig Jahre zu halten ist, halten mit den Kanonen und Flinten."
      ],
      [
        "Das war das Echo von der einen Seite.",
        "Aber lassen Sie mich auch sprechen von dem Echo von der anderen Seite, weil ich praktisch zu charakterisieren habe, worum es sich handelt.",
        "Die arbeitende Bevölkerung, insofern ich zu ihr sprechen konnte, hat sich mit einer verhältnismäßigen Leichtigkeit und mit innerem Verständnis in die Drei- gliederungsbewegung hineinzuleben versucht."
      ],
      [
        "Da kamen die Arbeiterführer, und sie wurden, ich möchte sagen, blaß vor Neid, daß jetzt auch von anderer Seite als von Seiten ihres eingetrichterten Marxismus zu der Arbeiterschaft ge- sprochen werden konnte.",
        "Und sie erfanden, ebenso wie die anderen, alle möglichen Verleumdungen, alle möglichen Schmierigkeiten, um den Arbeitern, die ja autoritätsgläu- big in dieser Beziehung zu ihren Führern sind, den Weg zum Verständnisse zu verlegen."
      ],
      [
        "Die Arbeiter aber sind heute noch nicht so weit, um sich in dem aus den letzten Jahrzehnten herübergenommenen Autoritätsglauben in der rechten Art zurechtzufinden.",
        "In dem Augenblicke, wo man innerhalb der Arbeiterschaft einsehen wird, worum es sich den niederen und höheren Arbeiterführern handelt, wird manches zerstieben, was heute noch auf diesem Felde als gutgemeinter Glaube vorhanden ist, wenn man ein- 188 sehen wird, daß diejenigen, die etwa von der Sorte des Lenin und Trotzkij, des Lunatsdiarskij, an der Spitze stehen, in ihrem wirklichen Wollen nicht etwa das Glück und Wohlergehen der Menge im Auge haben, sondern daß sie zu sich und untereinander etwa sagen: Die breite Masse des Volkes ist dumm und wird immer von Leidenschaften durchsetzt sein; mit der kann man nichts machen, als sie tyrannisieren; daher muß es nicht auffällig sein, daß wir ebenso tyrannisieren, ob wir nun Zar Nikolaus oder Lenin heißen; für uns handelt es sich nur darum, daß diejenigen, die früher auf den kurulischen Stühlen gesessen haben, heruntergefallen sind und wir nun darauf sitzen; für uns handelt es sich um die Eroberung der Regierungssitze!"
      ],
      [
        "In dem Augenblicke, in dem diese Erkenntnis in weite- sten Kreisen aufgehen wird, wird manches anders werden.",
        "Dann aber wird auch die Zeit gekommen sein, wo in das soziale Leben wirklich soziale Praxis wird einziehen kön- nen."
      ],
      [
        "Dann wird man mit praktischem Verständnisse das- jenige anschauen, was ich im zweiten und dritten Kapitel meiner «Kernpunkte der sozialen Frage», ich möchte sa- gen, wie exemplifizierend für das, was aus solchem Geiste heraus zu geschehen hat, ausgesprochen habe.",
        "Dann wird man sehen, daß da alles nicht aus einer Theorie heraus erfunden ist, sondern daß da alles aus einer schwer errun- genen Lebenspraxis heraus gewonnen ist, geradeso wie dazumal, als nach dem Bekanntwerden der Vierzehn Punkte Woodrow Wilsons diese Idee von der Dreigliede- rung des sozialen Organismus zuerst auftrat."
      ],
      [
        "Ich spreche als jemand, der sein halbes Leben, dreißig Jahre, in Österreich, in diesem Experimentierland für so- ziale Unmöglichkeiten zugebracht hat.",
        "Ich spreche als je- mand, der wohl weiß, wie man in diesem österreichischen Experimentierland in einem Ministerium, einem liberalen 189 Ministerium geredet hat."
      ],
      [
        "Der Liberale Giskra hat, als die Blütezeit des österreichischen Liberalismus war, und als schon hinter dem Liberalismus die soziale Frage auf- tauchte, gesagt: In Österreich haben wir mit der sozialen Frage nichts zu tun, denn die soziale Frage hört bei Boden- bach auf!",
        "Das wurde im Parlamente des Liberalismus in Österreich von dem verantwortlichen Minister des Innern verkündet, im letzten Drittel des 19."
      ],
      [
        "Jahrhunderts.",
        "Wer nun studieren will, wie in diesem österreichischen Parlamente, ich möchte sagen, in der Reinkultur gewirkt hat das unmögliche Durcheinandermischen der drei Glie- der des sozialen Organismus - was ich schon ausgedrückt habe in meinen «Kernpunkten», indem ich angeführt habe die Zusammensetzung des Parlaments aus vier Wirt- schaftskurien , der kann sehen, wie allmählich die Dinge sich entwickelten."
      ],
      [
        "Und wer das Ultimatum an Serbien verstehen will, der muß alles, was seit dem Jahre 1867 in Österreich geschehen ist bis zu den Zeiten hin, die dem Ultimatum an Serbien vorangingen, vollinhaltlich studie- ren.",
        "Dann wird er sehen, wie es ausgesehen hat mit dem Brotmangel, mit der Teuerung, mit den Teuerungskon- flikten in den Monaten, die dem Kriegsausbruch voran- gegangen sind gerade in österreichischen Landen, und er wird Gelegenheit haben, an den dortigen sozialen Fak- toren zu studieren, wo im Tieferen die wesentlichen Ur- sachen liegen."
      ],
      [
        "Und da würde man in eine neue Art der Betrachtungsweise hineingeführt werden.",
        "Aber was aus jeder solchen Betrachtung hervorgehen muß, das ist, daß es sich darum handelt, für das praktische soziale Leben Impulse zu finden, die aus diesem Leben selbst heraus sprechen."
      ],
      [
        "Dann werden wir vielleicht zu der Zeit kommen, in welcher es eine genügend große Anzahl von Menschen gibt, die - unbeirrt durch die alten Rich- 190 tungsbezeichnungen «rechts» und «links» ihre Aufmerk- samkeit dem Sachlich-Praktischen zuwenden, das, weil es eben aus der Wirklichkeit fließt, sich berufen glauben darf, mitzureden in den wichtigsten Angelegenheiten des Lebens.",
        "Und das sind die sozialen Angelegenheiten."
      ],
      [
        "Man stellt sich vielfach heute auf den Standpunkt, die Welt werde in Ordnung kommen, wenn es nur gelinge, die alten Impulse fortzusetzen, und man probiert jetzt schon wiederum seit langem, wie es gehen kann mit dem Fortlaufenlassen des Alten.",
        "Man wendet die Augen davon ab, wie unter diesem unsachlichen, wirklichkeitsfremden Operieren immer mehr hinaufkommt, was zermürbend zu gleicher Zeit wirken muß für die ganze moderne Zivilisa- tion."
      ],
      [
        "Nicht eher aber wird eine Möglichkeit entstehen weiter- zukommen, als dann, wenn man einsehen wird, wie ohne diesen Blick nach links oder rechts auf das sachliche Be- trachten des unmittelbaren Lebens losgegangen werden muß.",
        "Denn dadurch allein bekommen wir das Verständnis für solche praktisch-sozialen Ideen, welche ein ethisch- soziales Leben nicht nur predigen, sondern begründen können."
      ],
      [
        "Denn auf die Begründung dieses Lebens sollte hingewiesen werden mit der Dreigliederung des sozialen Organismus.",
        "Die Theoretiker haben aus ihren theoreti- schen Anschauungen heraus lange genug wiederholt, daß man heute «sozial» betrachten müsse, was auch in der Ethik lebt."
      ],
      [
        "Der Mensch sei hineingestellt seit der Arbeits- teilung ganz und gar ins soziale Gebiet, und man müsse «aus dem Sozialen heraus» begreifen, was im Menschen motivierend wirke, wenn er handeln solle.",
        "Solange dieses Urteil blutleer bleibt, solange es eine Abstraktion bleibt, so lange wird es nichts bewirken."
      ],
      [
        "Denn es ist als Abstraktion ebenso wahr wie falsch.",
        "Daß 191 es falsch ist, habe ich in meiner «Philosophie der Freiheit» gezeigt.",
        "Es hat die andere, die bedenkliche wahre Seite, daß der Mensch sich immer mehr und mehr mit seiner Freiheit an den objektiven Wirtschaftsprozeß und der- gleichen übergibt, wie das sogar theoretisch im Marxis- mus ausgeführt ist."
      ],
      [
        "Und indem der Mensch sich also dem Wirtschaftsprozeß oder dem Staatsprozeß oder den son- stigen sozialen Einrichtungen, die wir jetzt haben, über- gibt, wird natürlich immer mehr und mehr seine Tatmoti- vierung zu einer sozialen.",
        "Das kann und darf eingesehen werden."
      ],
      [
        "Denn daß Menschen mit Menschen lernen in Arbeitsteilung leben, darauf zielt die moderne Zivilisa- tion.",
        "Wenn aber die soziale Ordnung in dem Menschen ein sachgemäßes soziales Handeln motivieren soll, dann muß sie ein sozialer Organismus sein, der aus der inneren Gesetzmäßigkeit eines solchen Organismus heraus eben zur Motivierung des Willens befähigt ist, dann muß man durch einen lebensfähigen sozialen Organismus nicht nur Moral predigen, sondern soziale Moral begründen."
      ],
      [
        "Man muß Moral auf diesem Gebiete nicht durch Worte und Ideen, man muß sie durch die Sache, durch die Wirklich- keiten begründen.",
        "Wirklichkeiten sollten angeregt werden durch den Impuls der Dreigliederung des sozialen Orga- nismus."
      ],
      [
        "So wenig verstand man die Sache, daß sich die Abstrakt- linge sogar lustig machten, weil ich immer und immer wie- derum das Wort «Impuls» statt «Idee» gebrauchte, um anzudeuten, daß Kraft darinnen sein sollte in dieser Ten- denz des dreigegliederten sozialen Organismus, nicht bloß Rederei.",
        "Das sollte schon im Leben dieses Arbeitens zur Dreigliederung liegen: daß Wirklichkeit darinnen ist, nicht bloßes Reden."
      ],
      [
        "Sonst kann man auch als ethisierender Wanderredner, wie es jetzt so viele gibt, herumziehen 192 und den Leuten zureden wollen: Werdet nur wiederum ethisch, werdet nur wiederum gut, dann wird schon eine soziale Harmonie entstehen! - Ich habe zu denen, die es hören wollten, immer gesagt, wenn man zum Ofen im Zimmer spricht: Du Ofen, deiner Wesenheit nach ist es dein kategorischer Imperativ, das Zimmer warm zu machen - er wird das Zimmer nicht warm machen.",
        "Aber man braucht nicht zu predigen, wenn man Holz hineinlegt und es anzündet."
      ],
      [
        "Man braucht nicht theoretisch zu ethi- sieren, mystelnd zu ästhetisieren.",
        "Man hat nötig nicht bloß «praktische» Ideengemenge, sondern man hat nötig wirk- liche Impulse, um ideenerfüllte soziale Kräfte anzuregen, wenn es sich um soziale Praxis handeln soll."
      ],
      [
        "Und in dem Augenblicke, wo man aufbringen wird das Verständnis für diesen Tatbestand, wird man erst lernen, über das, was die Dreigliederung eigentlich will, richtig zu denken.",
        "Weil das aber hinunterreicht in Gemüt und Wille, so wird vorausgesetzt für dieses Verständnis der Dreigliede- rung nicht nur ein theoretisches Interesse an der Wahrheit und an einer theoretischen Diskussion, sondern vorausge- setzt wird Enthusiasmus und Bekenntnis für und gegen- über der Wahrheit."
      ],
      [
        "Solange wir nicht imstande sind, die Wahrheit in unseren Willen aufzunehmen, sie aus der Theorie herauszuholen und unseren ganzen Menschen da- mit zu durchdringen, kann auch nicht einmal der Anfang zu einer fruchtbaren Behandlung der sozialen Frage und sozialen Praxis entstehen.",
        "Darum handelt es sich: daß diejenigen, die Verständnis suchen für das, was Dreigliederung will, mit ihrem ganzen Menschen dieses Verständnis suchen mögen."
      ],
      [
        "Dann kommt Enthusiasmus nicht aus blinden Instinkten, sondern er wird angeregt aus lichtvoller Erkenntnis.",
        "Dann bleibt er selber nicht blind, sondern wird selber leuchten.",
        "Wenn 193 die Willensimpulse nicht aus Instinkten und Trieben kom- men, sondern aus einem Überschauen des sozialen Lebens, dann bleiben sie nicht blind und finster, dann werden sie selber sehend und leuchtend."
      ],
      [
        "Und daß Enthusiasmus und Wille gegenüber der Wahrheit in diesem Sinne immer leuchtender und leuchtender werde, davon hängt der Weg bezüglich des Impulses der Dreigliederung des sozialen Organismus ab.",
        "Und daß dasjenige, was nach dieser Rich- tung hier gesprochen werden kann, einiges dazu beitrage, in diesem Sinne nicht zu einem blinden und finsteren Enthusiasmus und Willen anzuregen, sondern zu licht- vollen willentlichen Gestaltungen des Lebens, das möchte ich hier am Schlüsse gerade dieser Betrachtung als eine Hoffnung ausgesprochen haben. 194"
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "Schlußwort zum vierten Disputationsabend Dornach, 8. April 1921",
    "paragraphs": [
      "Im Lauf der sehr regen Disputation zum Thema «Sozialwissen- schaft und soziale Praxis» kam ein holländisches Gesellschaftsmitglied wieder auf den «Weltschulverein» (vgl. S. 92 ff.) zu sprechen. Es forderte dazu auf, «gleich zur Tat zu schreiten», nämlich sofort die Gründung vorzunehmen (im Anschluß an eine holländische Initiative, die von 150 Namen getragen war).",
      "Dabei berief es sich darauf, daß im April 1912 Mitglieder der «Deutschen Sektion» der «Theosophi- schen Gesellschaft», auf Anregung eines aus England zugereisten Mit- glieds, durch eine solche «Tat» einen «Bund» gegründet hätten, aus dem, «was heute als Anthroposophische Gesellschaft bekannt ist, entsprungen» sei. Ich möchte Sie nicht mehr lange aufhalten, sondern nur ein paar Bemerkungen machen, zunächst in Anknüpfung an dasjenige, was unser Freund v.",
      "L. hier vorgeschlagen hat, was gewiß recht anerkennenswert ist, beziehungsweise sein wird, wenn es zu dem versprochenen Ziele führen wird. Ich möchte nur bemerken, daß es eine bedenkliche Grundlage wäre, wenn die Sache auf demselben Unter- grunde aufgebaut würde wie der «Bund», auf den hin- gewiesen worden ist.",
      "Dazumal ist nämlich allerdings mit einem gewissen Eifer so gearbeitet worden, wie Herr v. L. es ungefähr heute skizziert hat: Man hat sich in kleinen Komitees zusammengesetzt, hat alles mögliche beraten, was man tun soll und so weiter.",
      "Aber dann fiel ein Satz bei Herrn v. L., der selbstverständlich zunächst ein kleiner Irrtum ist, der aber, wenn er fortwirken würde, einen großen Irrtum hervorbringen könnte. Es wurde nämlich gesagt, aus dieser Arbeit, die dazumal in jener Nacht so rastlos verübt worden ist, sei dann die Anthroposophische Gesellschaft hervorgegangen. - Nein, davon kann gar nicht die Rede sein: aus jener Nacht und aus jener Bundes- begründung ist nämlich gar nichts hervorgegangen!",
      "Vor diesem Schicksal möchte ich die beabsichtigte «rastlose Arbeit dieser Nacht» doch bewahrt wissen. Es wurde zwar dazumal viel geredet, was zu tun ist, aber geworden ist gar nichts daraus. Und der Irrtum, der entstehen könnte, beruht darauf, daß man meinen könnte, es müsse nun etwas getan werden in der Richtung wie das, auf was mit jenem «Bunde» hingedeutet wurde.",
      "Das, was dann getan worden ist, war, daß diejenigen, die schon in unserer anthroposophischen Arbeit drinnengestanden haben, die also schon durchaus bei uns waren, daß die dann, ganz abgesondert von dieser Bundesgründung, die Anthropo- sophische Gesellschaft gegründet haben, die sich dann weiterentwickelt hat, während der «Bund» aus einem sanften Schlaf allmählich in den sozialen Tod, sagen wir, übergegangen ist. Also, es wäre ein kleiner Irrtum!",
      "Und es muß dies schon durchaus hervorgehoben werden, damit nicht die Fehler jenes Nachtkomitees durch seine zweite Auflage etwa wie- derholt werden. Das ist das eine. Das andere, worauf ich hinweisen möchte, ist, daß das, was etwa angestrebt werden sollte mit dem Weltschulver- ein, nun wirklich auf eine breite Basis gestellt und schon mit einem gewissen Mute und mit einem umfassenden Blick von vornherein in Angriff genommen werden müßte.",
      "Es ist ganz richtig von unserem Freund v. L. hervor- gehoben worden, daß dasjenige, was in bezug auf freies Geistesleben im Zusammenhange mit der Dreigliederung des sozialen Organismus zu vertreten ist, daß das für die verschiedensten Gebiete in verschiedenster Weise be- 196 handelt werden muß.",
      "Allein das muß dann auch wirklich so geschehen, daß die Behandlungsweise für die betreffen- den Territorien wirklichkeitsgemäß passe auf diese Terri- torien. Ich selber werde immer darauf hinweisen, daß zum Beispiel für England es notwendig sein wird, die Dinge in der Art vorzutragen, die eben gerade auf die englischen Zivilisationsverhältnisse paßt.",
      "Man muß gründlich durchschauen, was Einbildung ist gegenüber den großen Menschheitsfragen in der Gegen- wart, und was Wirklichkeit ist. Man darf also nicht etwa die Sache so vertreten, daß man den Glauben hervorruft, daß das englische Geistesleben freier ist als das andere.",
      "Und Sie werden sehen, wenn Sie wirklich die «Kern- punkte» durchgehen, daß da weniger Wert auf das nega- tive Moment - Befreiung des Geisteslebens vom Staate -, daß viel weniger darauf Wert gelegt wird als auf die Begründung eines freien Geisteslebens überhaupt. Und da wird es immer ein gutes Wort bleiben: daß es auf den Menschen ankommt, daß es wirklich darauf ankommt, aus welchen geistigen Grundlagen der Mensch hervorgeht, welche geistigen Grundlagen zu seiner Bildung geschaffen werden.",
      "Nicht so sehr handelt es sich darum, daß man das negative Moment betont, sondern das Positive ist zu betonen. Und ich brauche ja nur das zu sagen: Wenn, sagen wir, formal das Geistesleben befreit würde von dem staatlichen Zwange, und alles bliebe sonst im übrigen beim alten, so würde die Befreiung vom Staate nicht son- derlich viel nützen können.",
      "Es handelt sich darum, daß positiver Geist, so wie er hier in dieser Woche vertreten sein wollte, wie versucht wurde, ihn zu vertreten, daß dieser freie Geist in das Geistesleben international hineingebracht werde. Und dann werden sich die Dinge ergeben, wie sie sich ergeben sollen. 197 Es handelt sich wirklich zum Beispiel bei der Waldorf- schule nicht allein darum, daß sie eine wirklich freie Schule ist, daß sie nicht einmal einen Direktor hat, son- dern daß das Lehrerkollegium eine wirkliche repräsenta- tive Gemeinschaft ist.",
      "Es handelt sich nicht darum, daß alle Maßnahmen so getroffen werden, daß «nichts an- deres» spricht als dasjenige, was aus dem Lehrerkollegium selber hervorgeht, daß man also hier wirklich «eine unab- hängige Geistesgemeinschaft» hat, sondern es handelt sich auch darum, daß in allen Ländern das Geistesleben fehlt, von dem hier die ganze Woche gesprochen worden ist. Und wenn man irgendwo betonen hört, daß ja «das Gei- stesleben hierzulande frei» ist - ich meine jetzt nicht die Schweiz, ich spreche von England -, so ist das eben die andere Frage.",
      "Und dieses Positive vor allen Dingen ist es, auf das es ankommt. Da muß dann hervorgehoben wer- den: Das wird es natürlich nur geben, wenn man versucht, tatsächlich auf die konkreten Verhältnisse in den einzel- nen Ländern und Territorien einzugehen.",
      "Aber man muß Herz und Sinn haben für das, was das unfreie Geistesleben zuletzt in unserer Zeit gemacht hat. Nicht etwa, um auf das, was gestern hier vorgebracht worden ist, einzugehen, sondern um zu zeigen, welche Blüten menschlicher Denkungsart sowohl in intellektueller, wie in moralischer, wie in gemütlicher Beziehung unser gegenwärtiges Geistesleben zutage fördert, möchte ich Ihnen einen Satz vorlesen.",
      "Ich möchte Sie nicht lange auf- halten und nicht von dem Standpunkt, von dem aus gestern hier eine böse Bekämpfung der Anthroposophie und der Dreigliederung auseinandergesetzt worden ist, will ich wieder sprechen; aber ich möchte doch aus jener Broschüre, über die gestern hier gesprochen werden mußte, einen Satz vorlesen. Herr General v.",
      "Gleich schreibt über 198 mich: «Als fast Vierzigjähriger wurde Herr Steiner um die Jahrhundertwende, die auch in der übersinnlichen Welt der Anthroposophie einen Einschnitt bildet, durch Winters Vorträge über Mystik allmählich zur Theosophie hinübergeführt.» Nun können Sie fragen, wer dieser Herr Winter ist, den hier der Herr v. Gleich anführt als denjenigen, durch dessen Vorträge ich in Berlin zur Anthroposophie bekehrt worden bin.",
      "Man kann nur folgende Hypothese aufstel- len: Es gibt in der Vorrede zu jenen Vorträgen, die ich in Berlin im Winter 1901 / 1902 gehalten habe, einen Satz, worinnen ich sage: Es nahm diejenige Bewegung, von der ich sprechen will, ihren Anfang durch meine Vorträge des Winters vom Jahre 1901 / 1902. Aus diesem Winter, in dem ich meine Vorträge gehalten habe, wurde jener Herr «Winter», welcher im Jahre 1901 / 1902 mich zur Theosopie bekehrte.",
      "Sehen Sie, ich will nicht den Ausdruck gebrauchen, der anwendbar ist auf die intellektualistische Verfassung eines Menschen, der jetzt damit zur Führerschaft der Gegner der anthroposophischen Bewegung berufen ist, ich will den Ausdruck nicht gebrauchen; aber Sie werden ihn ja wohl hinlänglich gebrauchen können. Zu solchen Blüten menschlicher Geistestätigkeit führt das Geistesleben, durch das man hindurchgehen konnte in der Gegenwart bis zu jener Stufe, daß man ein Generalmajor werden konnte.",
      "Also man muß schon die Sache aus einer etwas größeren Tiefe heraus ins Auge fassen. Dann wird man erst ein Herz und einen Sinn bekommen für dasjenige, was not- wendig ist. Und nur weil eben das Geistesleben vor allen Dingen vom Schulwesen aus in Angriff genommen werden muß, deshalb wäre es so wünschenswert, daß dieser Welt- schulverein begründet werden könnte, der gar nicht so 199 schwer zu begründen wäre, wenn der Wille für ihn vor- handen ist.",
      "Er muß aber nicht ein kleineres oder größeres Komitee sein, sondern er muß so begründet werden, daß seine Mitgliederschaft unübersehbar ist. Erst dann hat er einen Wert. Er darf - ich will dazu keine Ratschläge geben, denn das, was ich darüber zu sagen habe, habe ich hinlänglich gesagt , er darf selbstverständlich einem Ein- zelnen überhaupt gar keine besonderen Opfer auferlegen.",
      "Er muß da sein, um Stimmung zu machen für dasjenige, wofür heute Stimmung so dringend notwendig ist! - Das ist etwas von dem, was ich noch anknüpfen mußte an dasjenige, was heute zutage getreten ist. Zum Schluß muß ich etwas sagen, was ich lieber nicht sagen würde, was ich aber eben doch sagen muß, da es sonst heute abend gar nicht berührt worden ist und es vielleicht für die nächsten Tage, weil da schon wahrschein- lich Abreiseschmerzen kommen, vielleicht zu spät sein könnte.",
      "Ich muß schon selber auf die Sache hinweisen. Es handelt sich darum, daß es ja eine volle Selbstverständ- lichkeit ist, daß für alles, wovon heute gesprochen worden ist, gewirkt werde. Allein dieses Wirken hat nur einen Sinn, wenn wir das Goetheanum, wie es hier steht, erhal- ten können, und vor allen Dingen zu Ende führen können.",
      "Nun, wenn es noch so gut geht mit «Futurum A.-G.» und noch so gut geht mit dem «Kommenden Tag», irgend- welche ökonomische Stützen für dieses Goetheanum wer- den diese noch lange nicht sein. Ganz gewiß nicht sein.",
      "Und die größte Sorge, trotz allen anderen Sorgen, die heute auf mir lastet - gestatten Sie, daß ich einmal per- sönlich spreche -, ist diese: daß in nicht gar zu ferner Zeit es der Fall sein könnte, daß wir keine ökonomischen Zuflüsse für dieses Goetheanum haben könnten. Deshalb ist es vor allen Dingen auch notwendig, zu betonen, daß 200 ein jeglicher dafür wirke, daß ein jeglicher, der irgend et- was beitragen kann dazu, daß dieser Bau seine Vollendung finden kann, das tun möge!",
      "Das ist es, was vor allen Din- gen notwendig ist: daß wir durch die Freunde unserer Sache in die Lage versetzt werden, dieses Goetheanum er- halten zu können, dieses Goetheanum vor allen Dingen zu Ende bauen zu können. Und das ist, wie gesagt, meine große Sorge.",
      "Ich muß es hier aussprechen. Denn schließlich, was würde es denn helfen, wenn wir noch so viel Propa- ganda machen könnten - und wir dieses Goetheanum viel- leicht von heute ab in drei Monaten zusperren müßten?",
      "Das gehört auch zu den sozialen Sorgen, die schon meiner Meinung nach zusammenhängen mit dem allgemeinen so- zialen Leben der Gegenwart. Und diese Sorge mußte ich betonen, weil wirklich die ihr zugrunde liegenden Tat- sachen nicht vergessen werden sollten: was möglich macht, die Bewegung, die von diesem Goetheanum ausgeht, zu kräftigen.",
      "Wir sehen ja, aus welchen intellektuellen Grundlagen heraus diejenigen kämpfen, die gerade jetzt gegen uns ihre Posten beziehen. Das wird ein Anfang sein. Man muß wachsam sein, sehr wachsam sein, denn diese Leute sind geschickte Leute.",
      "Die wissen sich zu organisieren. Was in Stuttgart geschehen ist, ist ein Anfang, ist als ein Anfang beabsichtigt. Und nur dann wird man gegen sie aufkom- men, wenn man einen solchen Idealismus entfacht , ich möchte es auch diesmal wiederum sagen -, der nicht sagt: Oh, die Ideale sind so furchtbar hoch, sie sind so erhaben, und meine Tasche ist etwas so Geringes, da greife ich nicht hinein, wenn es sich um die erhabenen Ideale han- delt. - Da muß es doch gesagt werden: Der Idealismus erst ist der wahre, der auch einmal für die Ideale in die Taschen greift! 2OI Schlußwort zu einer Studentenversammlung Dornach, 9.",
      "April 1921 Zur Besprechung der Frage, wie anthroposophische Arbeit an den Universitäten aufgebaut werden könne, fand am Nachmittag des 9 April 1921 auf Anregung deutscher Studenten eine Zusammenkunft statt. Steiner ergriff zum Schluß das Wort.",
      "S. hat allerdings auf die drei wichtigsten Dinge, die hier in Betracht kommen, hingewiesen: bei einer Organisa- tion oder bei keiner Organisation, wie es gewünscht wird. Aber ich möchte vor allen Dingen das eine betonen: Wenn man in einer solchen Bewegung drinnensteht, wie es die unsrige ist, so ist es schon notwendig, von dem Vergan- genen ein wenig zu lernen und weitere Stadien der Bewe- gung so zu führen, daß gewisse frühere Fehler vermieden werden.",
      "Worauf es in erster Linie ankommen wird, das wird doch dieses sein, daß Anthroposophie, soweit sie heute schon vom Verständnis der Studentenschaft angenommen werden kann und soweit es durch die vorhandenen Kräfte oder durch die vorhandenen Gelegenheiten irgend möglich ist, daß Anthroposophie in ihren verschiedenen Verzwei- gungen unter der Studentenschaft verbreitet werde als positiver geistiger Inhalt. Wir haben im Grunde genom- men die Erfahrung gemacht, daß etwas Reales doch nur dadurch zu erreichen ist, daß man auf dem Grunde des Positiven wirklich bauen kann.",
      "Ich hatte gestern Gelegenheit darauf hinzuweisen, daß vor Jahren versucht worden ist, eine Art Weltenbund für Geisteswissenschaft zu begründen, und daß aus diesem 202 Weltenbund, der eigentlich bloß nach den Regeln formaler äußerer Organisation vorgehen wollte, doch nichts ge- worden ist. Er ist sozusagen so ausgegangen, wie man im Deutschen sagt, wie «das Hornberger Schießen».",
      "Weil man aber dazumal einen Zusammenhalt, ein Zusammen- arbeiten brauchte, mußten die vorhandenen Bekenner zur Anthroposophie in der «Anthroposophischen Gesellschaft» zusammengefaßt werden. Das waren nun mehr oder we- niger lauter Leute, welche sich eben mit der Anthropo- sophie beschäftigt hatten.",
      "Mit einer solchen Organisation, wo eben schon etwas darinnen ist, kann man dann erst etwas machen. Natürlich wird es für die Studentenschaft ganz beson- ders notwendig sein, nicht nur zu arbeiten im Sinne einer Verbreitung der gegebenen anthroposophischen Probleme im engeren Sinne, sondern schon auch der Ausarbeitung von Generalproblemen und dergleichen in dem Sinne, wie es Dr.",
      "S. eben gemeint hat. Es wird natürlich zunächst gar nicht so sehr nötig sein, mit solchen Dingen auf Disserta- tionen hinzuarbeiten. Es ist oft, wirklich recht oft vorge- kommen, daß ich in der letzten Zeit gefragt worden bin von jüngeren Semestern etwa in der folgenden Richtung: Ja, wir möchten eigentlich die Anthroposophie zusammen- bringen mit unserer speziellen Wissenschaft.",
      "Wie kann man sich da verhalten, daß man in der richtigen Weise mit seinem Ziel nach der Promotion, nach dem Staats- examen, hinarbeitet? Was soll man da tun? Wie soll man seine Arbeit einrichten? - Ich habe dann immer den folgenden Rat gegeben: Versuchen Sie so schnell wie mög- lich sich durch das offizielle Studium durchzuschlängeln, so schnell wie möglich durchzukommen - wobei ich dann immer sehr gern bereit bin, mit irgendeinem Rat zur Seite zu stehen -, wählen Sie sich irgendein wissenschaftliches 203 Thema, das Ihnen hervorzugehen scheint aus dem Verlauf Ihrer Studien, als Dissertationsarbeit oder Staatsprüfungs- arbeit oder dergleichen.",
      "Welches Thema Sie auch wählen, ein jedes ist selbstverständlich anthroposophisch diametral entgegengesetzt den anderen Betrachtungsweisen, darüber kann gar kein Zweifel sein. Jedes ist diametral entgegen- gesetzt.",
      "Aber nun rate ich Ihnen: Schreiben Sie Ihre Dis- sertation so, daß Sie zunächst das hineinschreiben, was der Professor zensieren kann, was er verstehen wird; und neh- men Sie sich ein zweites Heft, da schreiben Sie alles das hinein, was sich Ihnen ergibt im Laufe Ihres Studiums und von dem Sie glauben, daß es eigentlich von der Anthro- posophie her hereingearbeitet werden sollte. Das bewah- ren Sie sich dann auf.",
      "Dann machen Sie ihre zwei Bogen, so lang muß eine Dissertation sein. Die reichen Sie ein. Und versuchen Sie fertig zu werden. Dann können Sie mit dem, was Sie sich außer diesem einen im zweiten Heft nach und nach erworben haben, der Anthroposophie wirk- lich tatkräftig helfen.",
      "Denn man merkt in der Tat eigent- lich erst, was für bedeutsame Probleme - Spezial- und Spezialistenprobleme - einem aufschießen, wenn man in die Notwendigkeit versetzt ist, wirklich wissenschaftlich zu arbeiten mit einem gewissen Thema und dergleichen. Aber es entsteht eine Gefahr durch, ich möchte sagen, ein unklares Zusammenarbeiten mit der Professorenschaft.",
      "Und ein Vorlegen von Dissertationen an die Professoren, die «im anthroposophischen Sinne» gehalten sind die passen gewöhnlich nicht für Professoren -, das halte ich deshalb nicht für günstig, weil es uns in dem Tempo, das die anthroposophische Bewegung haben soll, eigentlich aufhält. Wir brauchen möglichst viele akademisch gebildete Mit- arbeiter.",
      "Wenn uns irgend etwas fehlt, gründlich fehlt 204 heute in der anthroposophischen Bewegung, so ist es eine genügend große Anzahl akademisch gebildeter Mitarbei- ter. Ich will damit nicht die Äußerlichkeit bezeichnen, daß man, sagen wir, abgestempelte Leute braucht.",
      "So ist es nicht gemeint. Aber erstens brauchen wir Leute, die inner- lich wissenschaftlich arbeiten gelernt haben. Dieses inner- lich wissenschaftlich Arbeiten lernt man doch am besten bei seiner eigenen Arbeit.",
      "Zweitens aber brauchen wir möglichst bald die Mitarbeiter, welche aus der Studenten- schaft heraus kommen, und die nicht mehr aufgehalten werden durch die Rücksichten auf ihr späteres Fachstu- dium. (Sehen Sie, es ist gar nicht weiter wunderbar, daß das so schwer geht, wie es zum Beispiel in der Schweiz geht.) Man hat als Student natürlich leicht die Möglichkeit, in den ersten Semestern sich einem solchen Bunde anzu- schließen, wenn man freien Sinn genug dazu hat. Dann kommen die letzten Semester.",
      "Da ist man mit anderem be- schäftigt, und da wird die Sache schwieriger. Und so rei- ßen immer fort und fort die Fäden ab, die man da gezogen hat. Das ist gerade vorhin hervorgehoben worden. Also das möchte ich sagen, speziell für das wissen- schaftliche Zusammenarbeiten: Die Themen müssen schon in einer solchen Übergangszeit eine zweifache Bearbeitung erfahren: die eine, die der Professor versteht, und die an- dere, die man sich aufhebt für später.",
      "Selbstverständlich will ich damit durchaus nicht sagen, daß nicht ganz spezielle Gelegenheiten, die da sind, er- griffen werden, und daß nicht diese Gelegenheiten, die da sind, in ganz eminentestem Sinne von der Studentenschaft wachsam beobachtet und auch wirklich im Sinne und Dienste der Bewegung ausgenützt werden: Ich hoffe auf der einen Seite, fürchte fast ganz leise auf der anderen Seite, daß unser lieber Freund, Professor Römer in Leip- 205 zig, nun mit einer Unsumme von anthroposophischen Dissertationen überschwemmt wird! Aber ich denke, das würde auch zu den Dingen führen, die ihm wahrscheinlich am liebsten wären.",
      "Und ein solches Dokument studenti- schen Vertrauens würde zeigen, daß er nicht zu den Pro- fessoren gehört, von denen jetzt eben gesprochen worden ist. Das würde ja aus dem Fundament hervorgehen. Nun brauchen wir allerdings einen Ausbau desjenigen, was hier in Dornach schon einmal besprochen worden ist, nämlich doch immerhin eine Art von Zusammenarbeit.",
      "Das werden Sie sich später untereinander ausmachen, wie es technisch am besten zu bewerkstelligen ist. Es wäre schon gut, wenn mit Hilfe der Waldorflehrer, die ergänzt würden durch andere Persönlichkeiten aus unseren Reihen - Professor Römer, Dr.",
      "Unger und andere -, ein gewisser Austausch vor allen Dingen über die Wahl der Themen der Dissertationen oder der wissenschaftlichen Arbeiten stattfinden könnte, ohne daß irgendwie die freie Initiative des einzelnen davon beeinträchtigt ist. Es kann alles nur in Form von Ratschlägen geschehen.",
      "Es sollte gerade da- durch für dieses wissenschaftliche Arbeiten ein engerer Zusammenschluß - der ja nicht gerade eine Organisation zu sein braucht, aber ein Ideenaustausch - von Ihnen ge- sucht werden. Das Wirtschaftliche, das ist natürlich eine sehr, sehr be- deutungsvolle Sache.",
      "Es ist schon so, daß namentlich das Universitätswesen, aber eigentlich mehr oder weniger das gesamte Hochschulwesen unter unseren Wirtschaftsnöten außerordentlich leiden wird. Nun handelt es sich dabei darum, daß man nun wirklich einmal klar sieht, daß eigentlich nur geholfen werden kann, wenn es möglich ist, solche Institutionen vorwärtszubringen, wie es zum Bei- spiel für Deutschland der «Kommende Tag» ist, wie es 206 hier das «Futurum» ist.",
      "So daß von diesen Organisationen aus eine Reorganisation auch der wirtschaftlichen Lage des Studententums ausgehen kann. Es sind - ich kann Ihnen die Versicherung geben - all die Dinge, die von uns aus nach solcher Richtung hin in Angriff genommen werden, eigentlich auf schnelles Wachstum berechnet.",
      "Wir haben nicht Zeit, uns Zeit zu lassen, sondern wir müssen tatsächlich mit solchen wirtschaftlichen Organisationen rasch vorwärtskommen. Und da muß ich nun allerdings sagen: da werden uns die Mitglieder der Studentenschaft, vielleicht mit ganz geringfügigen Ausnahmen, vor allen Dingen helfen können durch das Verbreiten des Verständ- nisses für solche Dinge.",
      "Es ist ja wirklich schon vorgekom- men in bezug auf andere Dinge, daß der Student bei sei- nem Papa einiges durchsetzen konnte für dieses oder jenes, etwas durchsetzen konnte auch bei seiner Verwandtschaft. Nicht jeder hat nur mittellose Freunde.",
      "Und da ist dann wirklich etwas vorhanden, was wie eine Lawine wirkt. Lassen Sie sich das nur durchaus durch den Kopf gehen, wie stark erfahrungsgemäß so etwas wie eine Lawine wirkt: wenn man irgendwo anfängt, es geht wei- ter.",
      "Gerade so etwas geht weiter, wo man aus dem Posi- tiven heraus wirkt: Versucht diese Prospekte zu studie- ren, die erschienen sind vom «Kommenden Tag» und «Fu- turum», und versucht, Verständnis hervorzurufen für so etwas. Dieses Verständnis ist es, zu dem sich namentlich die ältesten Leute außerordentlich schwer emporarbeiten.",
      "Ich habe gesehen, wie ältere Leute, ich möchte sagen, gekaut haben an dem Verstehenwollen desjenigen, was «Kom- mender Tag» oder «Futurum» wollen, wie sie immer wie- der und wiederum, wie die Katze auf die Pfoten, zurück- gefallen sind auf ihre alten wirtschaftlichen Vorurteile, 207 mit denen sie eben hineingesaust sind in den wirtschaft- lichen Niedergang, und wie sie sich nicht herausfinden. Da glaube ich, daß wirklich lebt helles Verständnis der lieben Kommilitonen, das auch nach den älteren Genera- tionen hinüber einiges wirken könnte.",
      "Auf eine andere Weise können wir doch nicht vorwärts kommen. Denn ich kann Ihnen sagen: Dann, wenn wir einmal in bezug auf diese wirtschaftlichen Institutionen so weit sind, daß wir wirksam etwas machen können, daß wir erstens genug Mittel haben, um ins Große gehend - denn nur da hilft es - etwas zu tun, und auf der anderen Seite überwinden können den gerade auf diesem Gebiete so scharf hervor- tretenden Widerstand des Proletariats, das sich einfach gerade einer wirtschaftlichen Besserung der Lage der Stu- denten feindlich entgegenstellt, dann wird es tatsächlich die erste Sorge sein müssen dieser unserer wirtschaftlichen Organisationen, wirtschaftlich gerade in bezug auf die Studentenschaft zu arbeiten.",
      "Die «Kampfprobleme»! Ja, sehen Sie, da handelt es sich darum: die Anthroposophische Gesellschaft, wenn sie auch früher nicht so geheißen hat, besteht seit dem Beginn des Jahrhunderts, und sie hat immer eigentlich nur positiv gearbeitet, wenigstens soweit ich selber in Betracht komme.",
      "Sie ließ die Gegner schimpfen, alles mögliche tun. Aber natürlich kommen dann die Gegner mit gewissen Einwän- den. Sie sagen, da ist das gesagt worden, da jenes gesagt worden, ja das, das ist ja nicht einmal widerlegt worden. - Es ist schon so, daß man schwer Verständnis findet dafür, daß eigentlich derjenige, der etwas behauptet, die Beweis- verpflichtung hat, nicht derjenige, dem es angeworfen ist.",
      "Und wir konnten es wirklich erleben, immer wieder und wiederum, daß merkwürdige Anschauungen gerade unter den Akademikern, ich meine jetzt Dozenten, Professoren, 208 Pfarrer und solche, die also aus den Akademikern her- vorgegangen sind, hervortraten. Denken Sie doch nur ein- mal, daß von, ich möchte sagen, für die äußere Welt ehr- würdigen ich sage es aber selbstverständlich nur unter Gänsefüßchen: «ehrwürdigen» - Professoren Dinge vor- gebracht werden gegen Anthroposophie, Anthroposophen und so weiter, die so belegt sind, daß, wenn man diesen Belegen mit Beweisgründen nachgeht, das ein Hohn, ein blutiger Hohn ist auf alle irgendwie möglichen Methoden, wie man irgendwie etwas behauptet in der Wissenschaft.",
      "Daher mußte ich bei so jemandem, wie es der Professor Fuchs ist, einfach sagen: Es ist unmöglich, daß der Mensch etwas anderes ist als ein ganz unmöglicher Anatom! Denn, soll ich glauben, daß er gewissenhaft seine Dinge prüft, wenn er nach alledem, was vorgelegt worden ist, meinen Taufschein in dieser Weise prüft, wie er ihn geprüft hat?",
      "Man muß nämlich von der Art, wie ein Mensch das eine Gebiet behandelt, auf das andere schließen. Solche Dinge zeigen einfach - durch den Umstand, daß die Leute ein- mal heraustreten und ihre besonderen Gewohnheiten zei- gen - die Symptome, wie heute wissenschaftlich gearbeitet wird.",
      "Auch die Dinge, die heute an den Universitäten und an den technischen Hochschulen vorgebracht werden, ste- hen im Grunde genommen kaum auf besseren Füßen, als die Dinge, die auf diese Weise behauptet werden; es treten nur die allgemein ungeheuer locker gewordenen Gewohn- heiten im Wissenschaftsleben auf diese Weise zutage. Und das ist es, was nötig ist: daß man gewissermaßen den Kampf auf ein höheres Niveau hebt.",
      "Und da ist es nicht notwendig, daß man sich, wie zum Beispiel der Kommilitone wünschte, was ich sehr gut be- greife, als «Kampforganisation» ausspiele. Das ist nicht notwendig. Sondern nur das eine: das zu vermeiden, was 209 in der Anthroposophischen Gesellschaft so zahlreich auf- getreten ist.",
      "In der Anthroposophischen Gesellschaft trat immer dieses hervor, so unglaublich es ist natürlich nicht bei allen, aber sehr häufig: Man war genötigt, sich gegen einen wüsten Anwurf zu verteidigen, auch dann irgend- welche scharfen Worte zu gebrauchen, zum Beispiel, sagen wir in dem Fall, wenn ein Herr v. Gleich einen Vortragen- den «Winter» erfindet, indem er liest, daß ich selber Win- tervorträge gehalten habe, dann eine Persönlichkeit «Win- ter» erfindet, und das in einer sehr üblen Weise in den Kampf hineinbringt.",
      "Ja, sehen Sie, ich glaube nicht, daß man in diesem Falle zu scharfe Worte sagt, wenn man von Trottelisis sprechen würde! Denn hier hat man es, selbst wenn es bei einem General auftritt, mit einer echten Trot- telisis in Reinkultur zu tun. - Und in der Anthroposo- phischen Gesellschaft war es dann gewöhnlich so, daß man nicht demjenigen unrecht gegeben hat, der etwa so wie Herr v.",
      "Gleich handelte, sondern demjenigen, der sich verteidigt hat. Bis zum heutigen Tag! Erfuhren wir es doch ein paarmal, daß es hieß: In dieser Weise darf man nicht aggressiv werden. - Aggressiv werden, heißt nämlich in den Augen von vielen Leuten: sich in dieser Weise zu verteidigen.",
      "Da ist schon notwendig, daß man, ohne zu betonen, daß man Kampforganisation ist oder derglei- chen, doch mit wachsamem Auge die Dinge verfolgt und zurückweist. Sie müssen da konkret im Positiven auftre- ten; und dann müssen die anderen dahinterstehen, hinter dem, der genötigt ist, sich zu verteidigen.",
      "Es handelt sich nicht darum, daß wir selber Kampfhähne werden; aber darum handelt es sich, daß, wenn es nötig werden sollte, sich zu verteidigen, daß dann die anderen dahinterstehen. Und es handelt sich darum, daß man wirklich die Sym- ptome des Weltanschaulichen, Wissenschaftlichen, Reli- 210 giösen und so weiter in dieser Beziehung in unserer Zeit verfolgt, sich dafür interessiert.",
      "Nehmen Sie diese einzelne Erscheinung: Ich war genö- tigt, philosophische, oder wie soll man es nennen, Schrei- bereien - es ist nach meiner Meinung gleich, wie man sie nennt -des Grafen Keyserling einmal in der entsprechenden Weise zu charakterisieren, weil er in seiner unglaublichen Oberflächlichkeit hineingemischt hat die Tollheit, ich sei von Haeckelschen Anschauungen ausgegangen. Das ist natürlich eine nicht bloß objektive, sondern in diesem Falle subjektive Unwahrheit, das heißt, eine Lüge, weil man verlangen muß, daß derjenige, der so etwas behaup- tet, nach den Quellen sucht; und er hätte sehen können das Kapitel, das ich in den frühesten Jahren meiner Schriftstellerei geschrieben habe in meinen Auseinander- setzungen mit Haeckel, in der Einleitung zu Goethes Na- turwissenschaftlichen Schriften.",
      "Sie können das ja alle sehr gut nachlesen. Nun hat der Graf Keyserling durch sei- nen Verleger eine kleine Schrift erscheinen lassen: «Der Weg zur Vollendung.» Ich will diese Schrift nicht weiter charakterisieren, empfehle Ihnen aber, daß einer oder zwei sich diese Schrift kaufen und sie herumgehen lassen; denn wenn es alle kaufen wollten, wäre es schade ums Geld; aber ich empfehle Ihnen trotzdem, es zu lesen, da- mit Sie eine Vorstellung bekommen von dem, was sozu- sagen gegen alle Weisheit sich auftut in dieser Schrift «Der Weg zur Vollendung» von Keyserling.",
      "Es steht da folgender Satz, den er sich zurechtzimmerte, so ungefähr, wie er mir im Gedächtnis ist: Ja, wenn ich damit etwas Unrichtiges gesagt habe, daß Dr. Steiner von Haeckel aus- gegangen ist, so hätte ja Dr.",
      "Steiner das einfach rektifizie- ren können; er hätte das bei mir richtigstellen können, denn ich habe - und nun bitte ich, diesen Satz recht genau 211 zu beachten -, denn ich habe für eine besondere Steiner- Quellenforschung keine Zeit. Nun also, sehen Sie, wir haben es bereits in der wissen- schaftlichen Moral so weit gebracht, daß jemand, der eine «Weisheitsschule» gründet, es für berechtigt hält, daß er Dinge in die Welt hinaussenden darf, für deren Erfor- schung er zugestandenermaßen keine Zeit hat, die er also nicht erforscht!",
      "Hier ertappt man einen scheinbar sich vor- nehm Dünkenden denn der Graf Keyserling hat in sei- ner Schreiberei immer die Allmacht angeführt -, das ist dasjenige, was so imponiert bei dem Grafen Keyserling, daß er immer die Allmacht anführt. Die ganze gegenwär- tige Schreiberei ist an einem Punkt angekommen, wo sie am meisten versumpft und verlumpt ist.",
      "Und trotz der Allmacht ist hier eine vollständige moralische Verlumpung der Ansichten da. Und da muß schon einmal den Leuten gesagt werden: Ganz gewiß, es verlangt auch von dir niemand, daß du Steiner-Quellenforschung treibst; aber dann, wenn du schon keine Steiner-Quellenforschung treibst, keine Zeit hast, dann - in bezug auf alle diese Dinge, zu denen du von der Sache etwas wissen müßtest: Halte den Mund!",
      "Sehen Sie, das ist notwendig, daß wir uns keinen Illusio- nen hingeben, daß wir einfach abstreifen jegliches durch das Konventionelle heraufgekommene Autoritätsprinzip und dergleichen, daß wir uns frei gegenüberstellen, wirk- lich, wirklich prüfend, demjenigen, was in unserer Zeit vorhanden ist. Dann werden wir heute schon recht viel solches bemerken können.",
      "Ich würde Ihnen schon raten, manche der Sätze, die der große Germanist Roethe in Berlin ab und zu, immer wie- derum prägt, rein der Form nach - ich will ganz absehen von der Anschauung, die man dabei durchaus respektieren 212 kann - sich anzusehen. Dann werden Sie das Lehrreiche finden.",
      "Wir brauchen keine Kampforganisation zu sein. Wir müssen aber bereit und wachsam sein, um, wenn die Dinge, die heute wirklich so schauderhaft in den Nieder- gang hineinführen, konkret auftreten, dann dagegen auch wirklich aufzutreten.",
      "Brauchen wir denn dazu eine Orga- nisation anthroposophischer Studenten zu sein? Wir brau- chen ja einfach nur wachsame, anständige und wissen- schaftlich gewissenhafte Leute sein zu wollen, dann kön- nen wir immer - ganz von dem absolutesten Privatstand- punkt aus - gegen solche Schäden zu Felde ziehen.",
      "Und wenn wir außerdem noch für die positive Arbeit organi- siert sind, dann kann die Anzahl derjenigen, die dafür organisiert ist, hinter uns stehen und uns halten. Das letz- tere brauchen wir. Aber es wäre durchaus nicht sehr ge- scheit, wenn wir uns als Kampfesorganisation auftun wür- den.",
      "Dagegen handelt es sich darum, daß wir wirklich ernsthaftig arbeiten an der Verbesserung unserer gegen- wärtigen Zustände. Und dazu gehört schon einmal, daß man die furchtbaren Schäden, die auf dem einen oder anderen Feld zutage treten - und die wirklich sich leicht aufdrängen, denn sie sind in Unsummen da , daß man diese Dinge beachtet, und daß man den Mut hat, gegen sie in der Form, in der man es kann, aufzutreten.",
      "Sie haben schon etwas getan, wenn Sie nur das tun kön- nen: bei einer geringen Anzahl Ihrer Kommilitonen ein- fach das Urteil richtigstellen in bezug auf solche Dinge, auch wenn das im kleinsten Kreise geschieht. Ich habe gestern zu jemanden von uns hier in bezug auf den Welt- schulverein gesagt: Ich halte es gerade in bezug auf solche Dinge besonders wertvoll, wenn angefangen wird damit, daß einer zu zwei, drei anderen, also ganz kleinen Grup- pen, davon spricht, selbst wenn es nur zwei sind; und, 213 ganz radikal ausgedrückt, wenn einer gar keinen anderen findet, so sage er es sich wenigstens selber!",
      "Also diese Dinge sind schon durchaus so, daß man anfassen kann dasjenige, was der einzelne vermag. Es werden einzelne viel mehr vermögen, wie es tatsächlich schon vorgekom- men ist bei einem Arzt, der Mitglied war, und dessen Kommilitonen sich als sehr begeisterungsfähig erwiesen.",
      "Es handelt sich darum, daß wir uns nicht dadurch Feinde machen, daß wir in wüster Form als Kampfhähne auf- treten, aber auch darum, daß wir den Kampf nicht scheuen, wenn die anderen anfangen. Das ist es: wir müs- sen immer den anderen anfangen lassen; und dann muß die nötige Hilfe hinter uns stehen, die nicht die Taktik aufkommen läßt, denn es ist eine ganz bestimmte Taktik aufgekommen: daß wir angefangen hätten.",
      "Wenn von drüben angefangen wird, dann ist man genötigt, sich zu verteidigen; und dann können Sie immer lesen, daß von anthroposophischer Seite das und das im Kampfe als An- griff geführt worden ist und so weiter. Es wird immer der Spieß umgedreht.",
      "Das ist geradezu Methode bei den Gegnern. Das dürfen wir nicht aufkommen lassen. Was den Weltschulverein betrifft, so möchte ich dazu nur noch das eine sagen: nach meiner Empfindung wäre es wohl das allerbeste, wenn unabhängig voneinander gleichzeitig der Weltschulverein begründet werden könnte in Entente- und in neutralen Ländern, allerdings auch im deutschen mitteleuropäischen Gebiet.",
      "Wenn es gleichzeitig geschehen könnte, so daß sozusagen unabhängig voneinan- der die Dinge gleichzeitig aufschössen, wäre es das aller- beste. Dazu gehört natürlich eine gewisse Wachsamkeit, was etwa geschieht.",
      "Es müßte dann, wie ich glaube, ganz besonders von der Schweiz hier eine Vermittlung statt- finden. Es wäre gut, wenn man jetzt gerade für den 214 Augenblick die Sache machen könnte. Ich kann Ihnen ver- sichern: die Dinge sind auf des Messers Schneide und wenn eben heute dieselben Kriegsmöglichkeiten vorhanden wären, die im Jahre 1914 vorhanden waren, dann, dann hätten wir längst wiederum Krieg.",
      "Es stehen die Dinge in bezug auf Stimmungen und so weiter auf des Messers Schneide. Und wir bekommen so etwas wie diesen Welt- schulverein nicht zustande, wenn er zum Beispiel jetzt in Deutschland begründet wird, und dann etwa die anderen, wenn auch nur eine Woche, hintennachtrappen müßten.",
      "Er käme einfach nicht zustande, es wäre unpraktisch, es zu machen. Dagegen dürfen wir auf der anderen Seite durchaus wiederum das nicht aufkommen lassen, daß wir im ge- ringsten etwa verleugnen, wie wir überhaupt zu den Dingen stehen.",
      "Diese Hochschule für Geisteswissenschaft heißt Goetheanum. Wir haben diesen Namen «Goe- theanum» im Verlauf des Weltkrieges hier noch gegeben. Die anderen Nationen, insofern sie sich an der Anthropo- sophie beteiligt haben, haben den Namen aufgenommen, haben ihn akzeptiert.",
      "Wir haben niemals verleugnet, daß wir Gründe haben, die Hochschule für Geisteswissenschaft «Goetheanum» zu nennen, und es wäre daher nicht eigent- lich gut, wenn in Deutschland die Sachen als irgendeine Imitation von der anderen Seite auftreten dürften. Also es würde sich schon darum handeln, daß man in dieser Beziehung - verzeihen Sie das harte Wort - ein wenig nicht ungeschickt vorgehen würde, daß man es ein wenig geschickt machen würde im größeren Weltkultur- sinne!",
      "Da müßte nun von der Schweiz hier mit vollem Verständnis gearbeitet werden. Es müßte also eigentlich unbedingt gleichzeitig von Mitteleuropa, von der Entente und von Neutralen aus die Sache in die Höhe schießen. 215 Vorläufig weiß ich ja noch nicht, ob sie auch nur an einem oder zwei Orten in die Höhe schießen wird.",
      "Ich habe heute morgen die Mitteilung bekommen, daß das ge- stern zusammenberufene Komitee, das so wacker arbeiten wollte, wenige Minuten, nachdem die Versammlung von gestern den Saal verlassen hat, schlafen gegangen ist; es sei auf heute abend vertagt worden. Ob sie heute abend tagen, wollen wir zunächst noch abwarten.",
      "Wir haben schon sehr merkwürdige Erfahrungen gemacht; und aus dieser Kenntnis heraus, daß wir schon die verschieden- artigsten Erfahrungen gemacht haben, habe ich mir jetzt erlaubt, zu Ihnen hier darüber zu sprechen, daß man im weiteren Verlauf der Bewegung die gemachten Erfahrun- gen berücksichtigen soll. Ich bin aber auf der anderen Seite überzeugt, wenn ge- rade unter der Kommilitonenschaft sich finden wird der nötige starke Impuls und die gehörige Begeisterung, na- mentlich für dasjenige, was ich selbst und andere mei- ner Freunde im Verlaufe dieses Kurses genannt haben: Begeisterung für die Wahrheit - dann wird die Sache gehen.",
      "Ich möchte noch sagen: Ich habe neulich ein Stück aus einem Feuilleton vorgelesen, und ich kann Ihnen versichern, was neulich in Stuttgart stattgefunden hat, ist nicht im mindesten ein Ende, sondern erst ein Anfang, und ich kann Ihnen die Versicherung geben, daß es noch viel, viel schlimmer kommen wird. Ich habe das zu unseren Freun- den hier des öfteren gesagt - vor sehr, sehr langer Zeit schon -, ich habe neulich ein Stück aus einem Feuilleton vorgelesen, in dem steht: «Geistige Feuerfunken, die Blitzen gleich nach der hölzernen Mäusefalle zischen, sind also genügend vorhanden, und es wird schon einiger Klug- heit Steiners bedürfen, versöhnend zu wirken, damit nicht 216 eines Tages ein richtiger Feuerfunke der Dornacher Herr- lichkeit ein unrühmliches Ende bereitet.» Ich habe wirklich die Meinung, daß dasjenige, was als Reaktion eintreten muß gegen eine solche Aktion, die im- mer stärker und stärker werden wird, daß das besser ge- staltet und vor allen Dingen energischer wird durch- geführt werden müssen.",
      "Und ich glaube, daß Sie, meine lieben Kommilitonen, nach dieser Richtung hin nötig ha- ben, all Ihre jugendliche Begeisterung hineinfließen zu lassen in dasjenige, was wir hier öfter während dieses Kurses genannt haben: Enthusiasmus für die Wahrheit. Jugendlicher Enthusiasmus für die Wahrheit war immer ein sehr guter Impuls in der Fortentwickelung der Mensch- heit.",
      "Möge er es in einer Sache, die Sie für gut erkennen, auch in der nächsten Zukunft durch Sie werden. 217"
    ],
    "sentences": [
      [
        "Im Lauf der sehr regen Disputation zum Thema «Sozialwissen- schaft und soziale Praxis» kam ein holländisches Gesellschaftsmitglied wieder auf den «Weltschulverein» (vgl.",
        "S. 92 ff.) zu sprechen.",
        "Es forderte dazu auf, «gleich zur Tat zu schreiten», nämlich sofort die Gründung vorzunehmen (im Anschluß an eine holländische Initiative, die von 150 Namen getragen war)."
      ],
      [
        "Dabei berief es sich darauf, daß im April 1912 Mitglieder der «Deutschen Sektion» der «Theosophi- schen Gesellschaft», auf Anregung eines aus England zugereisten Mit- glieds, durch eine solche «Tat» einen «Bund» gegründet hätten, aus dem, «was heute als Anthroposophische Gesellschaft bekannt ist, entsprungen» sei.",
        "Ich möchte Sie nicht mehr lange aufhalten, sondern nur ein paar Bemerkungen machen, zunächst in Anknüpfung an dasjenige, was unser Freund v."
      ],
      [
        "L. hier vorgeschlagen hat, was gewiß recht anerkennenswert ist, beziehungsweise sein wird, wenn es zu dem versprochenen Ziele führen wird.",
        "Ich möchte nur bemerken, daß es eine bedenkliche Grundlage wäre, wenn die Sache auf demselben Unter- grunde aufgebaut würde wie der «Bund», auf den hin- gewiesen worden ist."
      ],
      [
        "Dazumal ist nämlich allerdings mit einem gewissen Eifer so gearbeitet worden, wie Herr v.",
        "L. es ungefähr heute skizziert hat: Man hat sich in kleinen Komitees zusammengesetzt, hat alles mögliche beraten, was man tun soll und so weiter."
      ],
      [
        "Aber dann fiel ein Satz bei Herrn v.",
        "L., der selbstverständlich zunächst ein kleiner Irrtum ist, der aber, wenn er fortwirken würde, einen großen Irrtum hervorbringen könnte.",
        "Es wurde nämlich gesagt, aus dieser Arbeit, die dazumal in jener Nacht so rastlos verübt worden ist, sei dann die Anthroposophische Gesellschaft hervorgegangen. - Nein, davon kann gar nicht die Rede sein: aus jener Nacht und aus jener Bundes- begründung ist nämlich gar nichts hervorgegangen!"
      ],
      [
        "Vor diesem Schicksal möchte ich die beabsichtigte «rastlose Arbeit dieser Nacht» doch bewahrt wissen.",
        "Es wurde zwar dazumal viel geredet, was zu tun ist, aber geworden ist gar nichts daraus.",
        "Und der Irrtum, der entstehen könnte, beruht darauf, daß man meinen könnte, es müsse nun etwas getan werden in der Richtung wie das, auf was mit jenem «Bunde» hingedeutet wurde."
      ],
      [
        "Das, was dann getan worden ist, war, daß diejenigen, die schon in unserer anthroposophischen Arbeit drinnengestanden haben, die also schon durchaus bei uns waren, daß die dann, ganz abgesondert von dieser Bundesgründung, die Anthropo- sophische Gesellschaft gegründet haben, die sich dann weiterentwickelt hat, während der «Bund» aus einem sanften Schlaf allmählich in den sozialen Tod, sagen wir, übergegangen ist.",
        "Also, es wäre ein kleiner Irrtum!"
      ],
      [
        "Und es muß dies schon durchaus hervorgehoben werden, damit nicht die Fehler jenes Nachtkomitees durch seine zweite Auflage etwa wie- derholt werden.",
        "Das ist das eine.",
        "Das andere, worauf ich hinweisen möchte, ist, daß das, was etwa angestrebt werden sollte mit dem Weltschulver- ein, nun wirklich auf eine breite Basis gestellt und schon mit einem gewissen Mute und mit einem umfassenden Blick von vornherein in Angriff genommen werden müßte."
      ],
      [
        "Es ist ganz richtig von unserem Freund v.",
        "L. hervor- gehoben worden, daß dasjenige, was in bezug auf freies Geistesleben im Zusammenhange mit der Dreigliederung des sozialen Organismus zu vertreten ist, daß das für die verschiedensten Gebiete in verschiedenster Weise be- 196 handelt werden muß."
      ],
      [
        "Allein das muß dann auch wirklich so geschehen, daß die Behandlungsweise für die betreffen- den Territorien wirklichkeitsgemäß passe auf diese Terri- torien.",
        "Ich selber werde immer darauf hinweisen, daß zum Beispiel für England es notwendig sein wird, die Dinge in der Art vorzutragen, die eben gerade auf die englischen Zivilisationsverhältnisse paßt."
      ],
      [
        "Man muß gründlich durchschauen, was Einbildung ist gegenüber den großen Menschheitsfragen in der Gegen- wart, und was Wirklichkeit ist.",
        "Man darf also nicht etwa die Sache so vertreten, daß man den Glauben hervorruft, daß das englische Geistesleben freier ist als das andere."
      ],
      [
        "Und Sie werden sehen, wenn Sie wirklich die «Kern- punkte» durchgehen, daß da weniger Wert auf das nega- tive Moment - Befreiung des Geisteslebens vom Staate -, daß viel weniger darauf Wert gelegt wird als auf die Begründung eines freien Geisteslebens überhaupt.",
        "Und da wird es immer ein gutes Wort bleiben: daß es auf den Menschen ankommt, daß es wirklich darauf ankommt, aus welchen geistigen Grundlagen der Mensch hervorgeht, welche geistigen Grundlagen zu seiner Bildung geschaffen werden."
      ],
      [
        "Nicht so sehr handelt es sich darum, daß man das negative Moment betont, sondern das Positive ist zu betonen.",
        "Und ich brauche ja nur das zu sagen: Wenn, sagen wir, formal das Geistesleben befreit würde von dem staatlichen Zwange, und alles bliebe sonst im übrigen beim alten, so würde die Befreiung vom Staate nicht son- derlich viel nützen können."
      ],
      [
        "Es handelt sich darum, daß positiver Geist, so wie er hier in dieser Woche vertreten sein wollte, wie versucht wurde, ihn zu vertreten, daß dieser freie Geist in das Geistesleben international hineingebracht werde.",
        "Und dann werden sich die Dinge ergeben, wie sie sich ergeben sollen. 197 Es handelt sich wirklich zum Beispiel bei der Waldorf- schule nicht allein darum, daß sie eine wirklich freie Schule ist, daß sie nicht einmal einen Direktor hat, son- dern daß das Lehrerkollegium eine wirkliche repräsenta- tive Gemeinschaft ist."
      ],
      [
        "Es handelt sich nicht darum, daß alle Maßnahmen so getroffen werden, daß «nichts an- deres» spricht als dasjenige, was aus dem Lehrerkollegium selber hervorgeht, daß man also hier wirklich «eine unab- hängige Geistesgemeinschaft» hat, sondern es handelt sich auch darum, daß in allen Ländern das Geistesleben fehlt, von dem hier die ganze Woche gesprochen worden ist.",
        "Und wenn man irgendwo betonen hört, daß ja «das Gei- stesleben hierzulande frei» ist - ich meine jetzt nicht die Schweiz, ich spreche von England -, so ist das eben die andere Frage."
      ],
      [
        "Und dieses Positive vor allen Dingen ist es, auf das es ankommt.",
        "Da muß dann hervorgehoben wer- den: Das wird es natürlich nur geben, wenn man versucht, tatsächlich auf die konkreten Verhältnisse in den einzel- nen Ländern und Territorien einzugehen."
      ],
      [
        "Aber man muß Herz und Sinn haben für das, was das unfreie Geistesleben zuletzt in unserer Zeit gemacht hat.",
        "Nicht etwa, um auf das, was gestern hier vorgebracht worden ist, einzugehen, sondern um zu zeigen, welche Blüten menschlicher Denkungsart sowohl in intellektueller, wie in moralischer, wie in gemütlicher Beziehung unser gegenwärtiges Geistesleben zutage fördert, möchte ich Ihnen einen Satz vorlesen."
      ],
      [
        "Ich möchte Sie nicht lange auf- halten und nicht von dem Standpunkt, von dem aus gestern hier eine böse Bekämpfung der Anthroposophie und der Dreigliederung auseinandergesetzt worden ist, will ich wieder sprechen; aber ich möchte doch aus jener Broschüre, über die gestern hier gesprochen werden mußte, einen Satz vorlesen.",
        "Herr General v."
      ],
      [
        "Gleich schreibt über 198 mich: «Als fast Vierzigjähriger wurde Herr Steiner um die Jahrhundertwende, die auch in der übersinnlichen Welt der Anthroposophie einen Einschnitt bildet, durch Winters Vorträge über Mystik allmählich zur Theosophie hinübergeführt.» Nun können Sie fragen, wer dieser Herr Winter ist, den hier der Herr v.",
        "Gleich anführt als denjenigen, durch dessen Vorträge ich in Berlin zur Anthroposophie bekehrt worden bin."
      ],
      [
        "Man kann nur folgende Hypothese aufstel- len: Es gibt in der Vorrede zu jenen Vorträgen, die ich in Berlin im Winter 1901 / 1902 gehalten habe, einen Satz, worinnen ich sage: Es nahm diejenige Bewegung, von der ich sprechen will, ihren Anfang durch meine Vorträge des Winters vom Jahre 1901 / 1902.",
        "Aus diesem Winter, in dem ich meine Vorträge gehalten habe, wurde jener Herr «Winter», welcher im Jahre 1901 / 1902 mich zur Theosopie bekehrte."
      ],
      [
        "Sehen Sie, ich will nicht den Ausdruck gebrauchen, der anwendbar ist auf die intellektualistische Verfassung eines Menschen, der jetzt damit zur Führerschaft der Gegner der anthroposophischen Bewegung berufen ist, ich will den Ausdruck nicht gebrauchen; aber Sie werden ihn ja wohl hinlänglich gebrauchen können.",
        "Zu solchen Blüten menschlicher Geistestätigkeit führt das Geistesleben, durch das man hindurchgehen konnte in der Gegenwart bis zu jener Stufe, daß man ein Generalmajor werden konnte."
      ],
      [
        "Also man muß schon die Sache aus einer etwas größeren Tiefe heraus ins Auge fassen.",
        "Dann wird man erst ein Herz und einen Sinn bekommen für dasjenige, was not- wendig ist.",
        "Und nur weil eben das Geistesleben vor allen Dingen vom Schulwesen aus in Angriff genommen werden muß, deshalb wäre es so wünschenswert, daß dieser Welt- schulverein begründet werden könnte, der gar nicht so 199 schwer zu begründen wäre, wenn der Wille für ihn vor- handen ist."
      ],
      [
        "Er muß aber nicht ein kleineres oder größeres Komitee sein, sondern er muß so begründet werden, daß seine Mitgliederschaft unübersehbar ist.",
        "Erst dann hat er einen Wert.",
        "Er darf - ich will dazu keine Ratschläge geben, denn das, was ich darüber zu sagen habe, habe ich hinlänglich gesagt , er darf selbstverständlich einem Ein- zelnen überhaupt gar keine besonderen Opfer auferlegen."
      ],
      [
        "Er muß da sein, um Stimmung zu machen für dasjenige, wofür heute Stimmung so dringend notwendig ist! - Das ist etwas von dem, was ich noch anknüpfen mußte an dasjenige, was heute zutage getreten ist.",
        "Zum Schluß muß ich etwas sagen, was ich lieber nicht sagen würde, was ich aber eben doch sagen muß, da es sonst heute abend gar nicht berührt worden ist und es vielleicht für die nächsten Tage, weil da schon wahrschein- lich Abreiseschmerzen kommen, vielleicht zu spät sein könnte."
      ],
      [
        "Ich muß schon selber auf die Sache hinweisen.",
        "Es handelt sich darum, daß es ja eine volle Selbstverständ- lichkeit ist, daß für alles, wovon heute gesprochen worden ist, gewirkt werde.",
        "Allein dieses Wirken hat nur einen Sinn, wenn wir das Goetheanum, wie es hier steht, erhal- ten können, und vor allen Dingen zu Ende führen können."
      ],
      [
        "Nun, wenn es noch so gut geht mit «Futurum A.-G.» und noch so gut geht mit dem «Kommenden Tag», irgend- welche ökonomische Stützen für dieses Goetheanum wer- den diese noch lange nicht sein.",
        "Ganz gewiß nicht sein."
      ],
      [
        "Und die größte Sorge, trotz allen anderen Sorgen, die heute auf mir lastet - gestatten Sie, daß ich einmal per- sönlich spreche -, ist diese: daß in nicht gar zu ferner Zeit es der Fall sein könnte, daß wir keine ökonomischen Zuflüsse für dieses Goetheanum haben könnten.",
        "Deshalb ist es vor allen Dingen auch notwendig, zu betonen, daß 200 ein jeglicher dafür wirke, daß ein jeglicher, der irgend et- was beitragen kann dazu, daß dieser Bau seine Vollendung finden kann, das tun möge!"
      ],
      [
        "Das ist es, was vor allen Din- gen notwendig ist: daß wir durch die Freunde unserer Sache in die Lage versetzt werden, dieses Goetheanum er- halten zu können, dieses Goetheanum vor allen Dingen zu Ende bauen zu können.",
        "Und das ist, wie gesagt, meine große Sorge."
      ],
      [
        "Ich muß es hier aussprechen.",
        "Denn schließlich, was würde es denn helfen, wenn wir noch so viel Propa- ganda machen könnten - und wir dieses Goetheanum viel- leicht von heute ab in drei Monaten zusperren müßten?"
      ],
      [
        "Das gehört auch zu den sozialen Sorgen, die schon meiner Meinung nach zusammenhängen mit dem allgemeinen so- zialen Leben der Gegenwart.",
        "Und diese Sorge mußte ich betonen, weil wirklich die ihr zugrunde liegenden Tat- sachen nicht vergessen werden sollten: was möglich macht, die Bewegung, die von diesem Goetheanum ausgeht, zu kräftigen."
      ],
      [
        "Wir sehen ja, aus welchen intellektuellen Grundlagen heraus diejenigen kämpfen, die gerade jetzt gegen uns ihre Posten beziehen.",
        "Das wird ein Anfang sein.",
        "Man muß wachsam sein, sehr wachsam sein, denn diese Leute sind geschickte Leute."
      ],
      [
        "Die wissen sich zu organisieren.",
        "Was in Stuttgart geschehen ist, ist ein Anfang, ist als ein Anfang beabsichtigt.",
        "Und nur dann wird man gegen sie aufkom- men, wenn man einen solchen Idealismus entfacht , ich möchte es auch diesmal wiederum sagen -, der nicht sagt: Oh, die Ideale sind so furchtbar hoch, sie sind so erhaben, und meine Tasche ist etwas so Geringes, da greife ich nicht hinein, wenn es sich um die erhabenen Ideale han- delt. - Da muß es doch gesagt werden: Der Idealismus erst ist der wahre, der auch einmal für die Ideale in die Taschen greift! 2OI Schlußwort zu einer Studentenversammlung Dornach, 9."
      ],
      [
        "April 1921 Zur Besprechung der Frage, wie anthroposophische Arbeit an den Universitäten aufgebaut werden könne, fand am Nachmittag des 9 April 1921 auf Anregung deutscher Studenten eine Zusammenkunft statt.",
        "Steiner ergriff zum Schluß das Wort."
      ],
      [
        "S. hat allerdings auf die drei wichtigsten Dinge, die hier in Betracht kommen, hingewiesen: bei einer Organisa- tion oder bei keiner Organisation, wie es gewünscht wird.",
        "Aber ich möchte vor allen Dingen das eine betonen: Wenn man in einer solchen Bewegung drinnensteht, wie es die unsrige ist, so ist es schon notwendig, von dem Vergan- genen ein wenig zu lernen und weitere Stadien der Bewe- gung so zu führen, daß gewisse frühere Fehler vermieden werden."
      ],
      [
        "Worauf es in erster Linie ankommen wird, das wird doch dieses sein, daß Anthroposophie, soweit sie heute schon vom Verständnis der Studentenschaft angenommen werden kann und soweit es durch die vorhandenen Kräfte oder durch die vorhandenen Gelegenheiten irgend möglich ist, daß Anthroposophie in ihren verschiedenen Verzwei- gungen unter der Studentenschaft verbreitet werde als positiver geistiger Inhalt.",
        "Wir haben im Grunde genom- men die Erfahrung gemacht, daß etwas Reales doch nur dadurch zu erreichen ist, daß man auf dem Grunde des Positiven wirklich bauen kann."
      ],
      [
        "Ich hatte gestern Gelegenheit darauf hinzuweisen, daß vor Jahren versucht worden ist, eine Art Weltenbund für Geisteswissenschaft zu begründen, und daß aus diesem 202 Weltenbund, der eigentlich bloß nach den Regeln formaler äußerer Organisation vorgehen wollte, doch nichts ge- worden ist.",
        "Er ist sozusagen so ausgegangen, wie man im Deutschen sagt, wie «das Hornberger Schießen»."
      ],
      [
        "Weil man aber dazumal einen Zusammenhalt, ein Zusammen- arbeiten brauchte, mußten die vorhandenen Bekenner zur Anthroposophie in der «Anthroposophischen Gesellschaft» zusammengefaßt werden.",
        "Das waren nun mehr oder we- niger lauter Leute, welche sich eben mit der Anthropo- sophie beschäftigt hatten."
      ],
      [
        "Mit einer solchen Organisation, wo eben schon etwas darinnen ist, kann man dann erst etwas machen.",
        "Natürlich wird es für die Studentenschaft ganz beson- ders notwendig sein, nicht nur zu arbeiten im Sinne einer Verbreitung der gegebenen anthroposophischen Probleme im engeren Sinne, sondern schon auch der Ausarbeitung von Generalproblemen und dergleichen in dem Sinne, wie es Dr."
      ],
      [
        "S. eben gemeint hat.",
        "Es wird natürlich zunächst gar nicht so sehr nötig sein, mit solchen Dingen auf Disserta- tionen hinzuarbeiten.",
        "Es ist oft, wirklich recht oft vorge- kommen, daß ich in der letzten Zeit gefragt worden bin von jüngeren Semestern etwa in der folgenden Richtung: Ja, wir möchten eigentlich die Anthroposophie zusammen- bringen mit unserer speziellen Wissenschaft."
      ],
      [
        "Wie kann man sich da verhalten, daß man in der richtigen Weise mit seinem Ziel nach der Promotion, nach dem Staats- examen, hinarbeitet?",
        "Was soll man da tun?",
        "Wie soll man seine Arbeit einrichten? - Ich habe dann immer den folgenden Rat gegeben: Versuchen Sie so schnell wie mög- lich sich durch das offizielle Studium durchzuschlängeln, so schnell wie möglich durchzukommen - wobei ich dann immer sehr gern bereit bin, mit irgendeinem Rat zur Seite zu stehen -, wählen Sie sich irgendein wissenschaftliches 203 Thema, das Ihnen hervorzugehen scheint aus dem Verlauf Ihrer Studien, als Dissertationsarbeit oder Staatsprüfungs- arbeit oder dergleichen."
      ],
      [
        "Welches Thema Sie auch wählen, ein jedes ist selbstverständlich anthroposophisch diametral entgegengesetzt den anderen Betrachtungsweisen, darüber kann gar kein Zweifel sein.",
        "Jedes ist diametral entgegen- gesetzt."
      ],
      [
        "Aber nun rate ich Ihnen: Schreiben Sie Ihre Dis- sertation so, daß Sie zunächst das hineinschreiben, was der Professor zensieren kann, was er verstehen wird; und neh- men Sie sich ein zweites Heft, da schreiben Sie alles das hinein, was sich Ihnen ergibt im Laufe Ihres Studiums und von dem Sie glauben, daß es eigentlich von der Anthro- posophie her hereingearbeitet werden sollte.",
        "Das bewah- ren Sie sich dann auf."
      ],
      [
        "Dann machen Sie ihre zwei Bogen, so lang muß eine Dissertation sein.",
        "Die reichen Sie ein.",
        "Und versuchen Sie fertig zu werden.",
        "Dann können Sie mit dem, was Sie sich außer diesem einen im zweiten Heft nach und nach erworben haben, der Anthroposophie wirk- lich tatkräftig helfen."
      ],
      [
        "Denn man merkt in der Tat eigent- lich erst, was für bedeutsame Probleme - Spezial- und Spezialistenprobleme - einem aufschießen, wenn man in die Notwendigkeit versetzt ist, wirklich wissenschaftlich zu arbeiten mit einem gewissen Thema und dergleichen.",
        "Aber es entsteht eine Gefahr durch, ich möchte sagen, ein unklares Zusammenarbeiten mit der Professorenschaft."
      ],
      [
        "Und ein Vorlegen von Dissertationen an die Professoren, die «im anthroposophischen Sinne» gehalten sind die passen gewöhnlich nicht für Professoren -, das halte ich deshalb nicht für günstig, weil es uns in dem Tempo, das die anthroposophische Bewegung haben soll, eigentlich aufhält.",
        "Wir brauchen möglichst viele akademisch gebildete Mit- arbeiter."
      ],
      [
        "Wenn uns irgend etwas fehlt, gründlich fehlt 204 heute in der anthroposophischen Bewegung, so ist es eine genügend große Anzahl akademisch gebildeter Mitarbei- ter.",
        "Ich will damit nicht die Äußerlichkeit bezeichnen, daß man, sagen wir, abgestempelte Leute braucht."
      ],
      [
        "So ist es nicht gemeint.",
        "Aber erstens brauchen wir Leute, die inner- lich wissenschaftlich arbeiten gelernt haben.",
        "Dieses inner- lich wissenschaftlich Arbeiten lernt man doch am besten bei seiner eigenen Arbeit."
      ],
      [
        "Zweitens aber brauchen wir möglichst bald die Mitarbeiter, welche aus der Studenten- schaft heraus kommen, und die nicht mehr aufgehalten werden durch die Rücksichten auf ihr späteres Fachstu- dium. (Sehen Sie, es ist gar nicht weiter wunderbar, daß das so schwer geht, wie es zum Beispiel in der Schweiz geht.) Man hat als Student natürlich leicht die Möglichkeit, in den ersten Semestern sich einem solchen Bunde anzu- schließen, wenn man freien Sinn genug dazu hat.",
        "Dann kommen die letzten Semester."
      ],
      [
        "Da ist man mit anderem be- schäftigt, und da wird die Sache schwieriger.",
        "Und so rei- ßen immer fort und fort die Fäden ab, die man da gezogen hat.",
        "Das ist gerade vorhin hervorgehoben worden.",
        "Also das möchte ich sagen, speziell für das wissen- schaftliche Zusammenarbeiten: Die Themen müssen schon in einer solchen Übergangszeit eine zweifache Bearbeitung erfahren: die eine, die der Professor versteht, und die an- dere, die man sich aufhebt für später."
      ],
      [
        "Selbstverständlich will ich damit durchaus nicht sagen, daß nicht ganz spezielle Gelegenheiten, die da sind, er- griffen werden, und daß nicht diese Gelegenheiten, die da sind, in ganz eminentestem Sinne von der Studentenschaft wachsam beobachtet und auch wirklich im Sinne und Dienste der Bewegung ausgenützt werden: Ich hoffe auf der einen Seite, fürchte fast ganz leise auf der anderen Seite, daß unser lieber Freund, Professor Römer in Leip- 205 zig, nun mit einer Unsumme von anthroposophischen Dissertationen überschwemmt wird!",
        "Aber ich denke, das würde auch zu den Dingen führen, die ihm wahrscheinlich am liebsten wären."
      ],
      [
        "Und ein solches Dokument studenti- schen Vertrauens würde zeigen, daß er nicht zu den Pro- fessoren gehört, von denen jetzt eben gesprochen worden ist.",
        "Das würde ja aus dem Fundament hervorgehen.",
        "Nun brauchen wir allerdings einen Ausbau desjenigen, was hier in Dornach schon einmal besprochen worden ist, nämlich doch immerhin eine Art von Zusammenarbeit."
      ],
      [
        "Das werden Sie sich später untereinander ausmachen, wie es technisch am besten zu bewerkstelligen ist.",
        "Es wäre schon gut, wenn mit Hilfe der Waldorflehrer, die ergänzt würden durch andere Persönlichkeiten aus unseren Reihen - Professor Römer, Dr."
      ],
      [
        "Unger und andere -, ein gewisser Austausch vor allen Dingen über die Wahl der Themen der Dissertationen oder der wissenschaftlichen Arbeiten stattfinden könnte, ohne daß irgendwie die freie Initiative des einzelnen davon beeinträchtigt ist.",
        "Es kann alles nur in Form von Ratschlägen geschehen."
      ],
      [
        "Es sollte gerade da- durch für dieses wissenschaftliche Arbeiten ein engerer Zusammenschluß - der ja nicht gerade eine Organisation zu sein braucht, aber ein Ideenaustausch - von Ihnen ge- sucht werden.",
        "Das Wirtschaftliche, das ist natürlich eine sehr, sehr be- deutungsvolle Sache."
      ],
      [
        "Es ist schon so, daß namentlich das Universitätswesen, aber eigentlich mehr oder weniger das gesamte Hochschulwesen unter unseren Wirtschaftsnöten außerordentlich leiden wird.",
        "Nun handelt es sich dabei darum, daß man nun wirklich einmal klar sieht, daß eigentlich nur geholfen werden kann, wenn es möglich ist, solche Institutionen vorwärtszubringen, wie es zum Bei- spiel für Deutschland der «Kommende Tag» ist, wie es 206 hier das «Futurum» ist."
      ],
      [
        "So daß von diesen Organisationen aus eine Reorganisation auch der wirtschaftlichen Lage des Studententums ausgehen kann.",
        "Es sind - ich kann Ihnen die Versicherung geben - all die Dinge, die von uns aus nach solcher Richtung hin in Angriff genommen werden, eigentlich auf schnelles Wachstum berechnet."
      ],
      [
        "Wir haben nicht Zeit, uns Zeit zu lassen, sondern wir müssen tatsächlich mit solchen wirtschaftlichen Organisationen rasch vorwärtskommen.",
        "Und da muß ich nun allerdings sagen: da werden uns die Mitglieder der Studentenschaft, vielleicht mit ganz geringfügigen Ausnahmen, vor allen Dingen helfen können durch das Verbreiten des Verständ- nisses für solche Dinge."
      ],
      [
        "Es ist ja wirklich schon vorgekom- men in bezug auf andere Dinge, daß der Student bei sei- nem Papa einiges durchsetzen konnte für dieses oder jenes, etwas durchsetzen konnte auch bei seiner Verwandtschaft.",
        "Nicht jeder hat nur mittellose Freunde."
      ],
      [
        "Und da ist dann wirklich etwas vorhanden, was wie eine Lawine wirkt.",
        "Lassen Sie sich das nur durchaus durch den Kopf gehen, wie stark erfahrungsgemäß so etwas wie eine Lawine wirkt: wenn man irgendwo anfängt, es geht wei- ter."
      ],
      [
        "Gerade so etwas geht weiter, wo man aus dem Posi- tiven heraus wirkt: Versucht diese Prospekte zu studie- ren, die erschienen sind vom «Kommenden Tag» und «Fu- turum», und versucht, Verständnis hervorzurufen für so etwas.",
        "Dieses Verständnis ist es, zu dem sich namentlich die ältesten Leute außerordentlich schwer emporarbeiten."
      ],
      [
        "Ich habe gesehen, wie ältere Leute, ich möchte sagen, gekaut haben an dem Verstehenwollen desjenigen, was «Kom- mender Tag» oder «Futurum» wollen, wie sie immer wie- der und wiederum, wie die Katze auf die Pfoten, zurück- gefallen sind auf ihre alten wirtschaftlichen Vorurteile, 207 mit denen sie eben hineingesaust sind in den wirtschaft- lichen Niedergang, und wie sie sich nicht herausfinden.",
        "Da glaube ich, daß wirklich lebt helles Verständnis der lieben Kommilitonen, das auch nach den älteren Genera- tionen hinüber einiges wirken könnte."
      ],
      [
        "Auf eine andere Weise können wir doch nicht vorwärts kommen.",
        "Denn ich kann Ihnen sagen: Dann, wenn wir einmal in bezug auf diese wirtschaftlichen Institutionen so weit sind, daß wir wirksam etwas machen können, daß wir erstens genug Mittel haben, um ins Große gehend - denn nur da hilft es - etwas zu tun, und auf der anderen Seite überwinden können den gerade auf diesem Gebiete so scharf hervor- tretenden Widerstand des Proletariats, das sich einfach gerade einer wirtschaftlichen Besserung der Lage der Stu- denten feindlich entgegenstellt, dann wird es tatsächlich die erste Sorge sein müssen dieser unserer wirtschaftlichen Organisationen, wirtschaftlich gerade in bezug auf die Studentenschaft zu arbeiten."
      ],
      [
        "Die «Kampfprobleme»!",
        "Ja, sehen Sie, da handelt es sich darum: die Anthroposophische Gesellschaft, wenn sie auch früher nicht so geheißen hat, besteht seit dem Beginn des Jahrhunderts, und sie hat immer eigentlich nur positiv gearbeitet, wenigstens soweit ich selber in Betracht komme."
      ],
      [
        "Sie ließ die Gegner schimpfen, alles mögliche tun.",
        "Aber natürlich kommen dann die Gegner mit gewissen Einwän- den.",
        "Sie sagen, da ist das gesagt worden, da jenes gesagt worden, ja das, das ist ja nicht einmal widerlegt worden. - Es ist schon so, daß man schwer Verständnis findet dafür, daß eigentlich derjenige, der etwas behauptet, die Beweis- verpflichtung hat, nicht derjenige, dem es angeworfen ist."
      ],
      [
        "Und wir konnten es wirklich erleben, immer wieder und wiederum, daß merkwürdige Anschauungen gerade unter den Akademikern, ich meine jetzt Dozenten, Professoren, 208 Pfarrer und solche, die also aus den Akademikern her- vorgegangen sind, hervortraten.",
        "Denken Sie doch nur ein- mal, daß von, ich möchte sagen, für die äußere Welt ehr- würdigen ich sage es aber selbstverständlich nur unter Gänsefüßchen: «ehrwürdigen» - Professoren Dinge vor- gebracht werden gegen Anthroposophie, Anthroposophen und so weiter, die so belegt sind, daß, wenn man diesen Belegen mit Beweisgründen nachgeht, das ein Hohn, ein blutiger Hohn ist auf alle irgendwie möglichen Methoden, wie man irgendwie etwas behauptet in der Wissenschaft."
      ],
      [
        "Daher mußte ich bei so jemandem, wie es der Professor Fuchs ist, einfach sagen: Es ist unmöglich, daß der Mensch etwas anderes ist als ein ganz unmöglicher Anatom!",
        "Denn, soll ich glauben, daß er gewissenhaft seine Dinge prüft, wenn er nach alledem, was vorgelegt worden ist, meinen Taufschein in dieser Weise prüft, wie er ihn geprüft hat?"
      ],
      [
        "Man muß nämlich von der Art, wie ein Mensch das eine Gebiet behandelt, auf das andere schließen.",
        "Solche Dinge zeigen einfach - durch den Umstand, daß die Leute ein- mal heraustreten und ihre besonderen Gewohnheiten zei- gen - die Symptome, wie heute wissenschaftlich gearbeitet wird."
      ],
      [
        "Auch die Dinge, die heute an den Universitäten und an den technischen Hochschulen vorgebracht werden, ste- hen im Grunde genommen kaum auf besseren Füßen, als die Dinge, die auf diese Weise behauptet werden; es treten nur die allgemein ungeheuer locker gewordenen Gewohn- heiten im Wissenschaftsleben auf diese Weise zutage.",
        "Und das ist es, was nötig ist: daß man gewissermaßen den Kampf auf ein höheres Niveau hebt."
      ],
      [
        "Und da ist es nicht notwendig, daß man sich, wie zum Beispiel der Kommilitone wünschte, was ich sehr gut be- greife, als «Kampforganisation» ausspiele.",
        "Das ist nicht notwendig.",
        "Sondern nur das eine: das zu vermeiden, was 209 in der Anthroposophischen Gesellschaft so zahlreich auf- getreten ist."
      ],
      [
        "In der Anthroposophischen Gesellschaft trat immer dieses hervor, so unglaublich es ist natürlich nicht bei allen, aber sehr häufig: Man war genötigt, sich gegen einen wüsten Anwurf zu verteidigen, auch dann irgend- welche scharfen Worte zu gebrauchen, zum Beispiel, sagen wir in dem Fall, wenn ein Herr v.",
        "Gleich einen Vortragen- den «Winter» erfindet, indem er liest, daß ich selber Win- tervorträge gehalten habe, dann eine Persönlichkeit «Win- ter» erfindet, und das in einer sehr üblen Weise in den Kampf hineinbringt."
      ],
      [
        "Ja, sehen Sie, ich glaube nicht, daß man in diesem Falle zu scharfe Worte sagt, wenn man von Trottelisis sprechen würde!",
        "Denn hier hat man es, selbst wenn es bei einem General auftritt, mit einer echten Trot- telisis in Reinkultur zu tun. - Und in der Anthroposo- phischen Gesellschaft war es dann gewöhnlich so, daß man nicht demjenigen unrecht gegeben hat, der etwa so wie Herr v."
      ],
      [
        "Gleich handelte, sondern demjenigen, der sich verteidigt hat.",
        "Bis zum heutigen Tag!",
        "Erfuhren wir es doch ein paarmal, daß es hieß: In dieser Weise darf man nicht aggressiv werden. - Aggressiv werden, heißt nämlich in den Augen von vielen Leuten: sich in dieser Weise zu verteidigen."
      ],
      [
        "Da ist schon notwendig, daß man, ohne zu betonen, daß man Kampforganisation ist oder derglei- chen, doch mit wachsamem Auge die Dinge verfolgt und zurückweist.",
        "Sie müssen da konkret im Positiven auftre- ten; und dann müssen die anderen dahinterstehen, hinter dem, der genötigt ist, sich zu verteidigen."
      ],
      [
        "Es handelt sich nicht darum, daß wir selber Kampfhähne werden; aber darum handelt es sich, daß, wenn es nötig werden sollte, sich zu verteidigen, daß dann die anderen dahinterstehen.",
        "Und es handelt sich darum, daß man wirklich die Sym- ptome des Weltanschaulichen, Wissenschaftlichen, Reli- 210 giösen und so weiter in dieser Beziehung in unserer Zeit verfolgt, sich dafür interessiert."
      ],
      [
        "Nehmen Sie diese einzelne Erscheinung: Ich war genö- tigt, philosophische, oder wie soll man es nennen, Schrei- bereien - es ist nach meiner Meinung gleich, wie man sie nennt -des Grafen Keyserling einmal in der entsprechenden Weise zu charakterisieren, weil er in seiner unglaublichen Oberflächlichkeit hineingemischt hat die Tollheit, ich sei von Haeckelschen Anschauungen ausgegangen.",
        "Das ist natürlich eine nicht bloß objektive, sondern in diesem Falle subjektive Unwahrheit, das heißt, eine Lüge, weil man verlangen muß, daß derjenige, der so etwas behaup- tet, nach den Quellen sucht; und er hätte sehen können das Kapitel, das ich in den frühesten Jahren meiner Schriftstellerei geschrieben habe in meinen Auseinander- setzungen mit Haeckel, in der Einleitung zu Goethes Na- turwissenschaftlichen Schriften."
      ],
      [
        "Sie können das ja alle sehr gut nachlesen.",
        "Nun hat der Graf Keyserling durch sei- nen Verleger eine kleine Schrift erscheinen lassen: «Der Weg zur Vollendung.» Ich will diese Schrift nicht weiter charakterisieren, empfehle Ihnen aber, daß einer oder zwei sich diese Schrift kaufen und sie herumgehen lassen; denn wenn es alle kaufen wollten, wäre es schade ums Geld; aber ich empfehle Ihnen trotzdem, es zu lesen, da- mit Sie eine Vorstellung bekommen von dem, was sozu- sagen gegen alle Weisheit sich auftut in dieser Schrift «Der Weg zur Vollendung» von Keyserling."
      ],
      [
        "Es steht da folgender Satz, den er sich zurechtzimmerte, so ungefähr, wie er mir im Gedächtnis ist: Ja, wenn ich damit etwas Unrichtiges gesagt habe, daß Dr.",
        "Steiner von Haeckel aus- gegangen ist, so hätte ja Dr."
      ],
      [
        "Steiner das einfach rektifizie- ren können; er hätte das bei mir richtigstellen können, denn ich habe - und nun bitte ich, diesen Satz recht genau 211 zu beachten -, denn ich habe für eine besondere Steiner- Quellenforschung keine Zeit.",
        "Nun also, sehen Sie, wir haben es bereits in der wissen- schaftlichen Moral so weit gebracht, daß jemand, der eine «Weisheitsschule» gründet, es für berechtigt hält, daß er Dinge in die Welt hinaussenden darf, für deren Erfor- schung er zugestandenermaßen keine Zeit hat, die er also nicht erforscht!"
      ],
      [
        "Hier ertappt man einen scheinbar sich vor- nehm Dünkenden denn der Graf Keyserling hat in sei- ner Schreiberei immer die Allmacht angeführt -, das ist dasjenige, was so imponiert bei dem Grafen Keyserling, daß er immer die Allmacht anführt.",
        "Die ganze gegenwär- tige Schreiberei ist an einem Punkt angekommen, wo sie am meisten versumpft und verlumpt ist."
      ],
      [
        "Und trotz der Allmacht ist hier eine vollständige moralische Verlumpung der Ansichten da.",
        "Und da muß schon einmal den Leuten gesagt werden: Ganz gewiß, es verlangt auch von dir niemand, daß du Steiner-Quellenforschung treibst; aber dann, wenn du schon keine Steiner-Quellenforschung treibst, keine Zeit hast, dann - in bezug auf alle diese Dinge, zu denen du von der Sache etwas wissen müßtest: Halte den Mund!"
      ],
      [
        "Sehen Sie, das ist notwendig, daß wir uns keinen Illusio- nen hingeben, daß wir einfach abstreifen jegliches durch das Konventionelle heraufgekommene Autoritätsprinzip und dergleichen, daß wir uns frei gegenüberstellen, wirk- lich, wirklich prüfend, demjenigen, was in unserer Zeit vorhanden ist.",
        "Dann werden wir heute schon recht viel solches bemerken können."
      ],
      [
        "Ich würde Ihnen schon raten, manche der Sätze, die der große Germanist Roethe in Berlin ab und zu, immer wie- derum prägt, rein der Form nach - ich will ganz absehen von der Anschauung, die man dabei durchaus respektieren 212 kann - sich anzusehen.",
        "Dann werden Sie das Lehrreiche finden."
      ],
      [
        "Wir brauchen keine Kampforganisation zu sein.",
        "Wir müssen aber bereit und wachsam sein, um, wenn die Dinge, die heute wirklich so schauderhaft in den Nieder- gang hineinführen, konkret auftreten, dann dagegen auch wirklich aufzutreten."
      ],
      [
        "Brauchen wir denn dazu eine Orga- nisation anthroposophischer Studenten zu sein?",
        "Wir brau- chen ja einfach nur wachsame, anständige und wissen- schaftlich gewissenhafte Leute sein zu wollen, dann kön- nen wir immer - ganz von dem absolutesten Privatstand- punkt aus - gegen solche Schäden zu Felde ziehen."
      ],
      [
        "Und wenn wir außerdem noch für die positive Arbeit organi- siert sind, dann kann die Anzahl derjenigen, die dafür organisiert ist, hinter uns stehen und uns halten.",
        "Das letz- tere brauchen wir.",
        "Aber es wäre durchaus nicht sehr ge- scheit, wenn wir uns als Kampfesorganisation auftun wür- den."
      ],
      [
        "Dagegen handelt es sich darum, daß wir wirklich ernsthaftig arbeiten an der Verbesserung unserer gegen- wärtigen Zustände.",
        "Und dazu gehört schon einmal, daß man die furchtbaren Schäden, die auf dem einen oder anderen Feld zutage treten - und die wirklich sich leicht aufdrängen, denn sie sind in Unsummen da , daß man diese Dinge beachtet, und daß man den Mut hat, gegen sie in der Form, in der man es kann, aufzutreten."
      ],
      [
        "Sie haben schon etwas getan, wenn Sie nur das tun kön- nen: bei einer geringen Anzahl Ihrer Kommilitonen ein- fach das Urteil richtigstellen in bezug auf solche Dinge, auch wenn das im kleinsten Kreise geschieht.",
        "Ich habe gestern zu jemanden von uns hier in bezug auf den Welt- schulverein gesagt: Ich halte es gerade in bezug auf solche Dinge besonders wertvoll, wenn angefangen wird damit, daß einer zu zwei, drei anderen, also ganz kleinen Grup- pen, davon spricht, selbst wenn es nur zwei sind; und, 213 ganz radikal ausgedrückt, wenn einer gar keinen anderen findet, so sage er es sich wenigstens selber!"
      ],
      [
        "Also diese Dinge sind schon durchaus so, daß man anfassen kann dasjenige, was der einzelne vermag.",
        "Es werden einzelne viel mehr vermögen, wie es tatsächlich schon vorgekom- men ist bei einem Arzt, der Mitglied war, und dessen Kommilitonen sich als sehr begeisterungsfähig erwiesen."
      ],
      [
        "Es handelt sich darum, daß wir uns nicht dadurch Feinde machen, daß wir in wüster Form als Kampfhähne auf- treten, aber auch darum, daß wir den Kampf nicht scheuen, wenn die anderen anfangen.",
        "Das ist es: wir müs- sen immer den anderen anfangen lassen; und dann muß die nötige Hilfe hinter uns stehen, die nicht die Taktik aufkommen läßt, denn es ist eine ganz bestimmte Taktik aufgekommen: daß wir angefangen hätten."
      ],
      [
        "Wenn von drüben angefangen wird, dann ist man genötigt, sich zu verteidigen; und dann können Sie immer lesen, daß von anthroposophischer Seite das und das im Kampfe als An- griff geführt worden ist und so weiter.",
        "Es wird immer der Spieß umgedreht."
      ],
      [
        "Das ist geradezu Methode bei den Gegnern.",
        "Das dürfen wir nicht aufkommen lassen.",
        "Was den Weltschulverein betrifft, so möchte ich dazu nur noch das eine sagen: nach meiner Empfindung wäre es wohl das allerbeste, wenn unabhängig voneinander gleichzeitig der Weltschulverein begründet werden könnte in Entente- und in neutralen Ländern, allerdings auch im deutschen mitteleuropäischen Gebiet."
      ],
      [
        "Wenn es gleichzeitig geschehen könnte, so daß sozusagen unabhängig voneinan- der die Dinge gleichzeitig aufschössen, wäre es das aller- beste.",
        "Dazu gehört natürlich eine gewisse Wachsamkeit, was etwa geschieht."
      ],
      [
        "Es müßte dann, wie ich glaube, ganz besonders von der Schweiz hier eine Vermittlung statt- finden.",
        "Es wäre gut, wenn man jetzt gerade für den 214 Augenblick die Sache machen könnte.",
        "Ich kann Ihnen ver- sichern: die Dinge sind auf des Messers Schneide und wenn eben heute dieselben Kriegsmöglichkeiten vorhanden wären, die im Jahre 1914 vorhanden waren, dann, dann hätten wir längst wiederum Krieg."
      ],
      [
        "Es stehen die Dinge in bezug auf Stimmungen und so weiter auf des Messers Schneide.",
        "Und wir bekommen so etwas wie diesen Welt- schulverein nicht zustande, wenn er zum Beispiel jetzt in Deutschland begründet wird, und dann etwa die anderen, wenn auch nur eine Woche, hintennachtrappen müßten."
      ],
      [
        "Er käme einfach nicht zustande, es wäre unpraktisch, es zu machen.",
        "Dagegen dürfen wir auf der anderen Seite durchaus wiederum das nicht aufkommen lassen, daß wir im ge- ringsten etwa verleugnen, wie wir überhaupt zu den Dingen stehen."
      ],
      [
        "Diese Hochschule für Geisteswissenschaft heißt Goetheanum.",
        "Wir haben diesen Namen «Goe- theanum» im Verlauf des Weltkrieges hier noch gegeben.",
        "Die anderen Nationen, insofern sie sich an der Anthropo- sophie beteiligt haben, haben den Namen aufgenommen, haben ihn akzeptiert."
      ],
      [
        "Wir haben niemals verleugnet, daß wir Gründe haben, die Hochschule für Geisteswissenschaft «Goetheanum» zu nennen, und es wäre daher nicht eigent- lich gut, wenn in Deutschland die Sachen als irgendeine Imitation von der anderen Seite auftreten dürften.",
        "Also es würde sich schon darum handeln, daß man in dieser Beziehung - verzeihen Sie das harte Wort - ein wenig nicht ungeschickt vorgehen würde, daß man es ein wenig geschickt machen würde im größeren Weltkultur- sinne!"
      ],
      [
        "Da müßte nun von der Schweiz hier mit vollem Verständnis gearbeitet werden.",
        "Es müßte also eigentlich unbedingt gleichzeitig von Mitteleuropa, von der Entente und von Neutralen aus die Sache in die Höhe schießen. 215 Vorläufig weiß ich ja noch nicht, ob sie auch nur an einem oder zwei Orten in die Höhe schießen wird."
      ],
      [
        "Ich habe heute morgen die Mitteilung bekommen, daß das ge- stern zusammenberufene Komitee, das so wacker arbeiten wollte, wenige Minuten, nachdem die Versammlung von gestern den Saal verlassen hat, schlafen gegangen ist; es sei auf heute abend vertagt worden.",
        "Ob sie heute abend tagen, wollen wir zunächst noch abwarten."
      ],
      [
        "Wir haben schon sehr merkwürdige Erfahrungen gemacht; und aus dieser Kenntnis heraus, daß wir schon die verschieden- artigsten Erfahrungen gemacht haben, habe ich mir jetzt erlaubt, zu Ihnen hier darüber zu sprechen, daß man im weiteren Verlauf der Bewegung die gemachten Erfahrun- gen berücksichtigen soll.",
        "Ich bin aber auf der anderen Seite überzeugt, wenn ge- rade unter der Kommilitonenschaft sich finden wird der nötige starke Impuls und die gehörige Begeisterung, na- mentlich für dasjenige, was ich selbst und andere mei- ner Freunde im Verlaufe dieses Kurses genannt haben: Begeisterung für die Wahrheit - dann wird die Sache gehen."
      ],
      [
        "Ich möchte noch sagen: Ich habe neulich ein Stück aus einem Feuilleton vorgelesen, und ich kann Ihnen versichern, was neulich in Stuttgart stattgefunden hat, ist nicht im mindesten ein Ende, sondern erst ein Anfang, und ich kann Ihnen die Versicherung geben, daß es noch viel, viel schlimmer kommen wird.",
        "Ich habe das zu unseren Freun- den hier des öfteren gesagt - vor sehr, sehr langer Zeit schon -, ich habe neulich ein Stück aus einem Feuilleton vorgelesen, in dem steht: «Geistige Feuerfunken, die Blitzen gleich nach der hölzernen Mäusefalle zischen, sind also genügend vorhanden, und es wird schon einiger Klug- heit Steiners bedürfen, versöhnend zu wirken, damit nicht 216 eines Tages ein richtiger Feuerfunke der Dornacher Herr- lichkeit ein unrühmliches Ende bereitet.» Ich habe wirklich die Meinung, daß dasjenige, was als Reaktion eintreten muß gegen eine solche Aktion, die im- mer stärker und stärker werden wird, daß das besser ge- staltet und vor allen Dingen energischer wird durch- geführt werden müssen."
      ],
      [
        "Und ich glaube, daß Sie, meine lieben Kommilitonen, nach dieser Richtung hin nötig ha- ben, all Ihre jugendliche Begeisterung hineinfließen zu lassen in dasjenige, was wir hier öfter während dieses Kurses genannt haben: Enthusiasmus für die Wahrheit.",
        "Jugendlicher Enthusiasmus für die Wahrheit war immer ein sehr guter Impuls in der Fortentwickelung der Mensch- heit."
      ],
      [
        "Möge er es in einer Sache, die Sie für gut erkennen, auch in der nächsten Zukunft durch Sie werden. 217"
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "SCHLUSSREDE Dornach, 10. April 1921",
    "paragraphs": [
      "Obwohl ich heute abend noch einen gewissermaßen außer- halb des Programmes stehenden Vortrag um acht Uhr für alle Kursteilnehmer dieser Woche halten werde, stehen wir doch jetzt am Ende unserer Frühjahrs-Vortragsreihe. Wir konnten in der kurzen Zeit, die uns zur Verfügung stand, wie es ja selbstverständlich ist, nur Andeutungen und Richtlinien geben über das, was uns auf ein gewisses Ziel hin vorschwebt.",
      "Und dies Ziel - Sie werden es gerade an diesen Vorträgen haben fühlen können - ist kein an- deres als dieses: zu zeigen, wie das, was hier anthroposo- phisch orientierte Geisteswissenschaft genannt wird, be- fruchtend wirken soll auf die verschiedenen einzelnen Fachwissenschaften und auch auf die verschiedenen Zweige des menschlichen praktischen Lebens in der Gegenwart. Wir haben, um hinweisen zu können, in welcher Art wir uns dieses Ziel vorstellen, zunächst durchgenommen, tageweise, diejenigen Wissenschaften, welche hineinführen in das Leben der äußeren Welt, der äußeren Natur.",
      "Wir haben zu zeigen versucht, wie da von den Erkenntnis- bestrebungen der Gegenwart überall Schranken und Gren- zen aufgerichtet werden, welche aber keine wirklichen Schranken und Grenzen menschlicher Seelentätigkeit über- haupt sein können, weil, wenn sie gelten könnten, das- jenige, was dem Menschen das wesentlichste Ziel der Er- kenntnis sein muß, das Durchschauen der menschlichen Wesenheit selber, niemals erreichbar sein würde. Und vor allen Dingen fehlen müßte eine Erkenntnis, welche An- 218 trieb werden kann des menschlichen Willens, der mensch- lichen Tat.",
      "Der menschliche Wille und die menschliche Tat müßten verurteilt sein, weiterhin nur aus den Instinkten und Trieben heraus das soziale Leben zu gestalten, wäh- rend ein menschenwürdiges Dasein nur begründet werden kann, wenn geistige Einsicht die Kraft hat, über die bloße Naturanschauung hinaus in das rein geistige Leben ein- zutauchen und von daher die sittlichen und die sozialen Ideale zu holen, die mächtig genug sind, um in den Willen impulsierend hineinzuwirken. So mußten wir auf der einen Seite darauf hinweisen, wie Geisteswissenschaft über die Schranken hinauskom- men will, die der äußeren Wissenschaft, insofern sie sich auf die äußere Natur und auf die äußere Welt bezieht, gesteckt sein sollen, nach dem Willen gerade und nach der Meinung und dem Glauben unserer Zeit.",
      "Und wir mußten auf der anderen Seite hinweisen auf die andere Richtung des menschlichen Erkennens: die nach innen geht, die dar- auf geht, den Menschen und sich selber zu erfassen, so daß man hinuntersteigen kann in das, was im Menschen als sein eigentlicher Wesenskern lebt. Und wir haben gezeigt, daß allein, wenn dieser Impuls wirklich in das Innere des Menschen eindringt, in der Erkenntnis lebt, daß dann allein zustande kommen könne zum Beispiel eine wirk- liche Sprachwissenschaft, eine wirkliche Geschichtswissen- schaft auch, und daß dieser Impuls der Innenerkenntnis notwendig ist, um die sprachlichen, die geschichtlichen Wissenschaften zu durchdringen und zu befruchten.",
      "So haben wir nach zwei Richtungen hingewiesen, in de- nen hinweggeschritten werden muß über die Grenzen, welche die gegenwärtige Fachwissenschaft setzen will: in die Richtung nach außen, in die Richtung nach innen. Und wir haben darauf hingewiesen in diesen Tagen, wie der 219 Appell an eine solche Geist-Erkenntnis uns ja hervortönt aus den wichtigsten Zeichen der Zeit.",
      "Da haben wir auf der einen Seite die zahlreichen An- zeichen, wie die Menschen in weitesten Kreisen bestrebt sind, immer tiefer und tiefer hineinzukommen in die Rät- sel des menschlichen Inneren, um da, in diesem mensch- lichen Inneren, einen sicheren Halt zu bekommen, ein rich- tiges Gleichgewicht zum äußeren sozialen Leben zu erhal- ten. Und wenn wir vernehmen die wichtigsten Stimmen des menschlichen Herzens, des menschlichen Gemütes, so müssen wir sagen: es tönt überall aus den Anforderungen der Gegenwart heraus, daß wissenschaftliche Erkenntnis ausmünden müsse in das, was so für die innere Sicherung der menschlichen Seele gefunden werden muß.",
      "Kein Aus- blick nach einem solchen Ziele ist in der gegenwärtigen landläufigen Wissenschaft zu finden. Weil er darinnen nicht zu finden ist, glaubt Geisteswissenschaft den Schritt tun zu müssen, diesen anderen Wissenschaften zu zeigen, wie sie durch wahre geisteswissenschaftliche Forschung be- fruchtet werden können.",
      "Von der anderen Seite her tönen die Klänge aus der sozialen Verwirrung. Große, gewaltige soziale Aufgaben stehen vor den Menschen unseres Zeitalters. Wir werden mit ihnen nur zurechtkommen, wenn wir einsehen, daß ja doch nur das, was wir uns an Einsicht in das Menschen- leben, an Erkenntnis der menschlichen Wesenheit erwer- ben können, uns die Kraft geben kann, an die großen sozialen Aufgaben der Gegenwart heranzutreten.",
      "Führend müssen wieder werden die Einsichten, führend muß das werden, was aus echter, wahrer geisteswissenschaftlicher Forschung hervorgeht, denn das allein kann auch rich- tunggebend sein für die sozial so notwendigen Bestre- bungen. 220 Es wird das gerade unseren Absichten übelgenommen, daß wir die Frage, auf die hiermit gedeutet ist, in einer etwas anderen Weise auffassen müssen als viele unserer Zeitgenossen. Ich habe auf dieses Anderssein schon bei den verschiedensten Gelegenheiten hinweisen müssen.",
      "Aber das ist etwas, was immer wiederum gesagt werden muß. Da- her will ich es auch heute, am Schlüsse unserer Veranstal- tung, hier sagen. Gewiß, es gibt schon viele Leute, die sagen: Über die weitesten Kreise der Bevölkerung hinaus muß Einsicht, muß Wissen sein; Wissen muß popularisiert werden, denn es muß leben in einer genügend großen An- zahl von Menschen; nur wenn es in ihnen lebt, werden sich auch die sozialen Einsichten entwickeln.",
      "Und aus dem guten Willen, der zweifellos dem zugrunde liegt, geht hervor alles, was man unternimmt in der Richtung der Einsetzung von Volkshochschulen, Volksbibliotheken, Po- pularisierung der Wissenschaft, wie sie an unseren heuti- gen Bildungsanstalten gepflegt wird. Man ist der Mei- nung, wenn man nur hinausträgt, was an unseren Bil- dungsanstalten gepflegt wird, in die weitesten Kreise, dann müsse es in der Zukunft verhindern, daß wir in solche katastrophalen Epochen hineinkommen, wie die unsrige es ist.",
      "Aber kann man denn glauben, daß dasjenige, was ja da war für die Menschen, die unmittelbar zu tun hatten mit den Ursachen dieser jetzigen katastrophalen Zeit, daß das, was also von unseren Bildungsanstalten ausgestrahlt ist auf die führenden Kreise und nichts gefruchtet hat, sie zu besserem Tun zu bringen als zu dem, wozu sie gekommen sind, kann man hoffen, daß dasselbe «Geistes- gut», wie man es eben auch nennt, nun wirken werde, wenn es in die große Menge hinausgestreut wird? Man kann solches nur glauben, wenn man sich selber Sand in 221 die Augen streuen will.",
      "Weil wir das nicht wollen, die wir uns hier verbunden fühlen mit den Bestrebungen des Goetheanismus, deshalb müssen wir sagen, trotz alledem, was da gleich aufgerufen wird an allen möglichen Feind- und Gegnerschaften: Nein, anderes ist noch notwendig! - Nicht bloß hinausgetragen werden soll etwas aus unseren Bildungsanstalten, hineingetragen werden muß etwas. Es muß das hineingetragen werden, was erst hineingetragen werden kann, wenn man die geistige Forschung neben der äußeren sinnlichen und verstandesmäßigen anerkennen will.",
      "Was dann in unsere Bildungsanstalten hineingetragen wird, das wird schon ergreifen die Herzen und die Ge- müter der Menschen, weil es hervorgeholt ist aus dem Wesen der Herzen und der Gemüter der Menschen, weil dasjenige, was unbewußt in der Menschen Tiefen schlum- mert, auf diese Weise zutage gefördert wird als Richtungs- kräfte für menschliches Wirken. Wir sind schon einmal in der für viele unsympathischen Lage, uns zu der Ansicht bekennen zu müssen, daß nicht nur etwas herausgetragen werden müßte aus unseren Bildungsanstalten, sondern vor allen Dingen viel, viel hineingetragen werden müsse.",
      "Und daß wir uns vermessen, hinzuweisen auf solche Dinge, das ist es, was uns so viele Feindschaft einträgt. Nun, Sie dürfen es mir glauben: persönlich wäre es mir das allerliebste, wenn der Drang nach solcher Geistes- berufung der Wissenschaften vor allen Dingen sich erhe- ben würde aus den Stätten unserer bisherigen Bildung selber, wenn da sich diejenigen finden würden, die hinwei- sen möchten darauf, was nötig ist.",
      "Über nichts würde ich mich mehr freuen, nichts würde mich mehr befriedigen, als wenn ich solches Streben sehen könnte. Ja, deshalb hatte ich wirklich verzeihen Sie diese einzuschiebende Epi- sode - einige Freude, als ich jüngst in Basel drinnen war 222 und im Schaufenster eine Schrift entdeckte, die den Titel trägt «Universitätsreform», geschrieben von einem Uni- versitätsprofessor selber, wie sich gleich herausstellte.",
      "Das, dachte ich mir, macht vielleicht ganz unnötig das Streben nach einer Begründung des Weltschulvereins, wenn solche Stimmen von solcher Seite herkommen. Und die Schrift beginnt auch gleich außerordentlich verheißungsvoll.",
      "Man hat so das Gefühl, daß mit solchen Sätzen etwas ange- schlagen werden müsse, was die Zeichen der Zeit nach einer gewissen Richtung hin versteht: «Die Organisation unserer Universitäten leidet an großen Mängeln. Ein Re- formwerk tut hier dringend not.",
      "An diesem Werk soll aber allein teilnehmen, wer das Universitätswesen von Grund aus kennt.» Auch darüber könnte man erfreut sein, wenn solche teil- nehmen würden, die das Universtätswesen von Grund auf kennen. Weil ich aber in dem, was ich weiter in dieser Schrift erfahren habe, ein Symptom charakterisieren möchte, so müssen Sie mir schon gestatten, daß ich in aller Kürze über das Erlebnis an dieser Schrift etwas spreche.",
      "Auf Seite 4 findet man ausgedrückt, was der Verfasser nun ausschließt von seiner Betrachtung über dieses Re- formwerk bezüglich der Universitäten: «So werde ich zum Beispiel mich über die Frage der Semestereinteilung und der Universitätsferien nicht äußern. Denn diese Dinge sind noch nicht spruchreif.» Ein Weiteres, das ausgeschlossen werden soll von dieser Betrachtung: «So werde ich ferner die Rechtsverhältnisse der Assistenten unserer Kliniken oder unserer naturwissen- schaftlichen Institute unerörtert lassen.",
      "Denn ich traue mir ein sachverständiges Urteil darüber nicht zu.» Nun, man könnte ja ganz zufrieden sein, wenn diese zwei Punkte ausgeschlossen bleiben würden von einer Be- 223 trachtung darüber, wie notwendig ein Reformwerk an unseren Universitäten ist. Dann wird dasjenige, was nun zu reformieren ist, in einzelnen Kapiteln abgehandelt.",
      "Das erste Kapitel heißt: «Die Einteilung der Universitätslehrer in verschiedene Klassen.» Man erfährt daraus, daß es ordentliche, außer- ordentliche Professoren gibt, Privatdozenten, Honorar- professoren, Lektoren und Assistenten. Man erfährt dar- aus, daß es notwendig ist, hier mit einem großen Reform- werk einzusetzen, daß es zum Beispiel notwendig ist, daß gewisse Leute, die nach dem gegenwärtigen Usus ihr gan- zes Leben lang außerordentliche Professoren geblieben sind, weil sie zum Beispiel nur ein Nebenfach - die Ohren- heilkunde oder die Ägyptologie - zu vertreten hatten, daß die nun zu, nun, auch zu ordentlichen Professoren ernannt werden müssen; nur daß man doch nicht gleich über die Schnur hauen soll, erfährt man, daß man bei all denen, die vom außerordentlichen Professor zum ordentlichen Professor zu ernennen sind, das Gehalt doch ein geringeres wird sein lassen müssen, als dasjenige, welches die richtigen ordentlichen Professoren bekommen.",
      "Dann schreiten wir weiter zum nächsten Kapitel über die Bestellung der Universitätslehrer. Da wird unter an- derem auf das Außerordentliche, Bedeutsame hingewiesen, daß sich ja Diskrepanzen ergeben haben zwischen den Regierungen und den Fakultäten oder den Professoren- kollegien, und daß es etwas Bedenkliches hätte, wenn man etwa gar zu stark darauf rechnen würde, daß aus den Professorenkollegien selber einzig und allein die Ernen- nung hervorgehen könnte.",
      "Die Regierungen haben da manchmal Besseres getan als die Professorenkollegien. Man muß nach einem Ausweg suchen. Es ist allerdings die Schrift für deutsche Verhältnisse 224 geschrieben, allein ich glaube, sie ist für Weltverhältnisse zum mindesten symptomatisch und darf daher hier ange- führt werden.",
      "Da wird nach einem Ausweg gesucht, wie man darüber hinauskommen könne, daß die Diskrepan- zen zwischen den Kollegien und den Regierungen ver- schwinden, und da wird hingewiesen darauf, daß man die wichtige Einrichtung ins Leben rufen müsse eines «Reichs- universitätsrates»! Wir kommen - ich will recht schnell über die Dinge hin- weggehen - zum dritten Kapitel: Das Gehalt der Uni- versitätslehrer.",
      "Nun, da wird eben auseinandergesetzt, wel- che Wünsche vorliegen über die Gehaltsregulierungen. Ein Kleines habe ich Ihnen schon davon mitgeteilt. Wir kommen zum vierten Kapitel: Die Überweisung der Vorlesungsgebühren an die Universitätslehrer.",
      "Da wird darauf hingewiesen, daß mancher, der ein sehr tüch- tiger Mann ist, nur ein ganz kleines Kolleg hat, ein ande- rer, der gerade etwas Beliebtes liest, hat ein großes Kolleg, bekommt also viele Kolleggelder. Es wird darauf hin- gewiesen, daß zum Beispiel derjenige, der nur drei Stun- den zu lesen hätte über seinen Gegenstand, daß der fünf oder sechs Stunden erhält, damit das Kolleggeld höher werde.",
      "Kurz, es sei nicht anders hinauszukommen, als daß man diese Sache einer gründlichen Reform unterziehe. Dann, im fünften Kapitel, wird von der Verleihung von Auszeichnungen an die Universitätslehrer gesprochen, was auch eine Angelegenheit ist, die eine gründliche Re- form erfordert.",
      "In einem sechsten Kapitel wird gesprochen über die Art des Ausscheidens der Universitätslehrer aus ihrer Lehrstel- lung. Da wird darauf hingewiesen, daß da viele Un- gerechtigkeiten geschehen könnten. Allein wenn ein «Uni- versitätsdienstgericht» eingerichtet wird, welches zum Teil 225 besteht aus den würdigsten Mitgliedern des «Reichsuni- versitätsrates», dann wird es mit diesen Dingen schon gehen.",
      "Dann wird darauf hingewiesen, wie durch solche In- stanzen, wie den «Reichsuniversitätsrat» und das «Uni- versitätsdienstgericht», nun auch einmal Ordnung hinein- kommen könne in dasjenige, was im siebenten Kapitel angeführt wird, das «Dienststrafrecht der Universitäts- lehrer», was zu geschehen hat, wenn man sie entlassen will oder wenn sie nur einen Verweis oder so etwas be- kommen sollen. Dann finden wir ein besonderes Kapitel über «Besondere Dienstaufträge der Universitätslehrer».",
      "Wir finden ein Kapitel über die «Verwaltung der Universitätsangelegen- heiten», worinnen aber nur über solche Dinge gesprochen wird, die eben Besprechungen dahin notwendig machen, ob nun auch die außerordentlichen Professoren und die Privatdozenten vielleicht durch einen Vertreter teilnehmen sollen, und in welcher Weise das geschehen soll, an dem, was man ausmacht. In einem elften Kapitel wird über das «Universitäts- vermögen» gesprochen.",
      "In einem zwölften Kapitel davon, wie man zurechtkommen soll, wenn sich Leute melden, die nicht ganz ihre Vorprüfung gemacht haben. In einem dreizehnten Kapitel wird darauf aufmerksam gemacht, daß das Doktorsein durch verschiedene Umstände ein Un- fug ist, und daß man daher künftig nicht doktorieren soll durch Prüfungen, sondern daß derjenige, der die Staatsprüfung, die Assessorprüfung, die philologische Schulamtsprüfung und ähnliches absolviert hat, berechtigt sein soll, sich in Zukunft selber Doktor zu nennen.",
      "Aber das führt doch wiederum zu Schwierigkeiten, nämlich, wenn sich diejenigen, die vom Staat angestellt sind, Dok- 226 tor nennen können - ich weiß nicht den inneren logischen Zusammenhang, ich habe ihn nicht begriffen -, dann wären doch keine Garantien dafür geboten, daß das auch Gelehrte jetzt wären, und deshalb müsse noch extra eine Gelehrtenprüfung eingeführt werden. Man könne aller- dings nicht hoffen, daß die Leute große Lust haben, diese Gelehrtenprüfung noch extra abzulegen; allein, man könne dafür noch extra einen Ersatz eintreten lassen, zum Bei- spiel den, daß dem, der sie abgelegt hat und nachher promoviert wird, daß dem das Jahr, in dem er diese Ge- lehrtenprüfung abgelegt hat, doppelt angerechnet werde zu seiner Dienstzeit.",
      "Ja, meine sehr verehrten Anwesenden, ich rede von einer sehr ernsten Angelegenheit, ich rede von einem Buch über Universitätsreform, das damit beginnt: Die Organi- sation an unseren Universitäten leide an großen Mängeln, ein Reformwerk tue dringend not, und ich habe, als ich dreizehn Kapitel durchgemacht hatte, gesehen, ich war schon auf Seite 43 angekommen, nun gab es noch andert- halb Seiten; ich hoffte, nun wird es kommen! Aber siehe da, jetzt kommt ein vierzehntes Kapitel: «Wissenschaft- liche Forschungsanstalten.» Da wird gesagt, daß ja aller- dings auch für diese einiges zu tun wäre, daß als richtige Forscher zum Beispiel nur diejenigen angestellt werden dürften, die zuerst Universitätsprofessoren gewesen sind, denn nur die seien wirkliche Forscher.",
      "Und dann schließt auf Seite 44 diese Schrift damit: «Es empfiehlt sich des- halb, das Gehalt von Mitgliedern von Forschungsanstalten nicht ganz so hoch zu bemessen wie das von ordentlichen Universitätsprofessoren des gleichen Dienstalters; sie kön- nen sich ja darüber auch nicht beklagen, da sie ja von der schweren Unterrichtslast ganz befreit sind. Auch ist ir- gendwie Vorsorge dahin zu treffen, daß die Mitglieder 227 der Forschungsinstitute ihre Stellung als Honorarprofesso- ren nicht dazu benutzen, um sich übermäßige Vorlesungs- gebühren zu sichern.» Ja, damit ist die Schrift wirklich zu Ende.",
      "Und ich habe eigentlich ganz unvermerkt einiges ausgelassen. Ich hatte allerdings, als ich die Schrift zu Ende gelesen hatte, so das Gefühl: Also die Universitäten bestehen aus Professoren, ordentlichen und außerordentlichen Professoren, Privat- dozenten, Lektoren und Assistenten.",
      "Aber da fiel mir ein: an der Universität, da sind ja auch Studenten, und ich fragte mich, hängen vielleicht diese Studenten doch auch etwas zusammen mit dem Zwecke der Universitäten? Da konnte ich denn konstatieren, daß sieben und zehn, gleich siebzehn Zeilen den Studenten gewidmet sind in dieser Schrift, welche nahezu vierundvierzig Seiten umfaßt.",
      "Aber die ersten sieben Zeilen auf Seite 5 - aus denen konnte ich nichts Besonderes machen. Denn die sagen eigentlich so furchtbar wenig Positives: «Deshalb gehe ich nicht weiter darauf ein, ob sich nicht das Verhältnis zwischen Universitätslehrern und Studenten inniger gestalten und vor allem die Sprechstunde der Universitätslehrer frucht- barer einrichten ließe, als das jetzt im großen und ganzen der Fall ist.",
      "Denn hier wäre mit Verwaltungsvorschriften gar nichts auszurichten. Hier wäre jeder Zwang, der nur von außen käme, hoffnungslos.» Dann wollte ich mich noch halten bezüglich der Studen- tenschaft an die Seite, welche in zehn Zeilen über die Stu- denten handelt.",
      "Aber da konnte ich auch nichts machen, denn die handeln bloß über das «Ordnungsstrafrecht der Studenten». Nun, ich habe das, was ich mitgeteilt habe, eigentlich nicht mitgeteilt, um ironisch zu werden, um Lachen zu erregen oder dergleichen, sondern ich habe es mitgeteilt als 228 auch ein Zeichen der Zeit, und ich bemerke ausdrücklich, daß ich den Mann, der das geschrieben hat, für einen außerordentlich guten, einen außerordentlich gescheiten Menschen halte, der sich nur nicht entschließen kann, be- züglich seines Reformwerkes auf etwas anderes zu reflek- tieren als auf dasjenige - er sagt es selbst -, was sich durch Verwaltungsmaßregeln durchführen läßt.",
      "Nun, ich denke, wir haben heute noch andere Dinge notwendig als die- jenigen, die sich durch Verwaltungsmaßregeln durchführen lassen. Die Zeichen der Zeit fordern durchaus anderes. Aber nicht nur ein gutwilliger, ein gescheiter Mensch ist der Verfasser dieser Schrift über «Universitätsreform», sondern er ist auch ein sich selbst gut kennender Mensch, und er verrät, warum er eigentlich über solche Dinge nicht hinausgeht.",
      "Und da finden wir denn etwas sehr Merk- würdiges auf Seite 4: «So werde ich weiter die Reform des Universitätsunterrichts im engeren Sinne schweigend übergehen. Sie liegt mir freilich sehr am Herzen und ist mindestens so wichtig wie sämtliche übrigen Reformen, die ich demnächst mehr oder weniger ausführlich behan- deln werde.",
      "Mein Schweigen fällt mir deshalb schwer. Allein was ich darüber sachkundig zu sagen hätte, würde im wesentlichen bloß für den Unterricht in der Rechts- wissenschaft und der Volkswirtschaft gelten, hätte dage- gen für den Unterricht in der Philologie, der Medizin, den Naturwissenschaften nur geringe Bedeutung.",
      "Eine auf den rechtswissenschaftlichen und volkswirtschaftlichen Unter- richt beschränkte Untersuchung würde aber nicht in den Rahmen einer Abhandlung passen, die sich mit der Re- form der Gesamtuniversität befaßt.» Ja, denken wir uns, die Sache hätte nicht ein Jurist ge- schrieben, dann könnte hier stehen: «Mein Schweigen fällt mir deshalb schwer. Allein was ich darüber sachkundig zu 229 sagen hätte, würde im wesentlichen bloß für den Unter- richt in der Medizin gelten, hätte daher für den Unterricht in der Rechtswissenschaft und Volkswirtschaft nur geringe Bedeutung.",
      "Eine auf den medizinischen Unterricht be- schränkte Untersuchung würde aber nicht in den Rahmen einer Abhandlung passen, die sich mit der Reform der Gesamtuniversität befaßt.» Und nun könnte ich Ihnen mit Abänderung des Sub- jekts diesen Satz recht oft vorlesen und Sie würden daraus sehen - wenn Sie sich das dahinterliegende Faktum vor die Seele rufen , wozu namentlich das Spezialistentum, wie es wuchernd geworden ist, geführt hat. Zur Tatlosigkeit hat es den Wissenschafter verurteilt.",
      "Niemand weiß über dasjenige, was im Großen zu geschehen hat, zu reden, weil er Jurist, weil er Volkswirtschafter, Mediziner, Philologe ist und so weiter. Man wird gewissermaßen heute Wissen- schafter, um über die eigentlichen Angelegenheiten des menschlichen Wissens bekennen zu müssen, daß man über sie nichts weiß.",
      "Solch ein Symptom ist deshalb von Bedeu- tung, weil es nun wirklich von einem gescheiten, gutwilli- gen Menschen, der außerdem noch die nötige Bescheiden- heit hat, kommt. Aber ich denke, es weist um so mehr auf die Notwendigkeit hin, daß in die Stätten, um die es sich handelt, etwas hineingetragen werden muß, nicht bloß, daß etwas herausgeholt werden könne zu den Zielen, von denen ich vorhin geredet habe.",
      "Deshalb, glaube ich, mußten wir, durften nicht nur, mußten und müssen es immer wiederum, hinweisen auf das, was von Seiten der Geisteswissenschaft befruchtend hineinwirken soll in die einzelnen Zweige des Fachwis- sens, aber schließlich auch in die einzelnen Zweige des praktischen Denkens. Denn die Art und Weise, wie wir allmählich zu den Abstraktionen in den Wissenschaften 230 gekommen sind, die haben hervorgerufen eine Stellung von Wissenschaftlichkeit in einer trockenen, unpraktischen, lebensfremden Daseinszone.",
      "Und man kann es selbst für das soziale Gebiet erleben, daß ein Mann wie Schumpeter, der wiederum ein außerordentlicher, kluger, gescheiter Mann ist und eine gescheite Abhandlung über Imperialis- men geschrieben hat, mit den Worten schließt: «Eine ethische, ästhetische, politische oder kulturelle Wertung dieses Prozesses liegt den Zielen dieser Studien fern. Ob dieser Prozeß Geschwüre heilt oder Sonnen verlöscht, ist von ihrem Standpunkte (nämlich vom wissenschaftlichen Standpunkte) aus völlig gleichgültig.",
      "Das zu beurteilen ist nicht Sache der Wissenschaft.» Das heißt, Sache der Wissenschaft ist es, etwas hervor- zubringen, was vor dem Leben halt macht, was nicht zu Wertungen führt im ethischen, ästhetischen, im kulturel- len Leben. Wir haben es im Laufe dieser Vortragsreihe gesehen, welche merkwürdige Tatsache aufgetreten ist in- folge dieses abstrakten Gestaltens der Wissenschaftsbestim- mung.",
      "Wir haben gesehen, wie die Wertphilosophie, die Rickertsche, Windelbandsche und so weiter Wertphiloso- phie heraufgezogen ist. Idi glaube, aus den Ausführungen des Dr. Stein ging Ihnen klar hervor, um was es sich ge- handelt hat.",
      "Da hat es sich darum gehandelt, daß nun zunächst auf naturwissenschaftlicher Seite das Sein be- ansprucht wird, aber daß man sich auf der naturwissen- schaftlichen Seite, wo man das Sein in seiner Totalität beansprucht, durchaus nicht darauf einlassen will, noch irgend etwas philosophisch zu treiben. Man will sich auf den Stuhl der Wissenschaft setzen, der das Sein darstellt, und man will alles, was über das Sein auszumachen ist, von naturwissenschaftlicher Seite ausmachen.",
      "Auf philo- sophischer Seite macht man keine Anstalten - verzeihen 231 Sie, das Bild ist nicht so schlimm gemeint, als ich es aus- spreche -, den Stuhl zur Bank zu machen, den anderen etwas zur Seite zu rücken und sich selber auf den Stuhl des Seins zu setzen. Nein, weil einem die Wertung über- lassen ist, weil die Wissenschafter sagen: ethische, ästhe- tische, kulturelle Wertungen liegen der Wissenschaft fern, seien nicht Sache der Wissenschaft, setzt man sich auf den Stuhl der Wertungen, damit man eine reine Abgrenzung hat.",
      "Man spezialisiert bis in die Geistigkeit hinein und verliert die Möglichkeit, wirklich an den Menschen heran- zukommen, der gewiß nicht anders kann, als, indem er im Sein lebt, etwas darzuleben, was für ihn selber eine ethische, ästhetische, kulturelle Wertung darstellen muß. Die Dinge, um die es sich heute handelt, gehen wirklich in die Tiefen.",
      "Und deshalb sollte die Mitwelt schon die Geneigtheit entwickeln, die Grundfrage zu beantworten: Ist diese Geisteswissenschaft, welche von sich behauptet, daß sie die einzelnen Fachwissenschaften und auch Zweige des praktischen Lebens befruchten könne, ist diese Geistes- wissenschaft selber wissenschaftlich? - Und in dieser Be- ziehung wird die Geisteswissenschaft sich auf den Stand- punkt stellen, daß ihr jedes Eingehen auf sie mit voller wissenschaftlicher Gründlichkeit und mit guten wissen- schaftlichen Vorkenntnissen aus den einzelnen Wissen- schaften der Gegenwart heraus - aber natürlich nicht aus Dilettantismus heraus -, daß ihr jedes Eingehen auf sie mit guter Wissenschaftlichkeit willkommen ist. Sie schreckt nicht vor den Prüfungen derer zurück, die etwas wissen, und sie wird um so froher sein, je mehr diejenigen wissen, welche sie vom Standpunkte der einzelnen Wissenschaften heraus prüfen wollen.",
      "Das ist das erste, was ich Ihnen heute am Schlüsse un- serer Frühjahrskurse sagen möchte. 232 Das zweite ist aber das, was viele uns vorwerfen, daß wir in unerlaubter Weise nach dem Übersinnlichen stre- ben, daß wir zu den Menschen reden von einer Erfor- schung des Übersinnlichen, daß aber das schon von vorne- herein unwissenschaftlich sei, denn vom Übersinnlichen könne man ja nichts wissen. Nun, der Nerv der Ausführungen dieser Woche, der war, ich möchte sagen, wie von selbst dahin gerichtet, zu zeigen, daß wir zu dem übersinnlichen Forschen gehen wollen nicht aus dem Grunde, weil wir über die Wissen- schaft hinauswollen zu irgendeinem nebulosen Zeug, daß wir nicht nach dem Übersinnlichen streben, weil wir un- wissenschaftlich sein wollen, sondern daß wir uns auf den Boden der Wissenschaft stellen, so wie sie jetzt ist, daß wir uns aber ehrlich auf diesen Boden stellen.",
      "Und indem wir uns ehrlich auf diesen Boden stellen, finden wir, wo in diesen Wissenschaften überall die Tore sind aus ihnen selbst heraus und in die übersinnliche Welt hinein. Nicht weil wir uns neben die Wissenschaften hinbegeben wollen, nicht aus Unwissenschaftlichkeit reden wir von dem Über- sinnlichen, sondern weil wir aus der Wissenschaft selbst mit wissenschaftlichen Gründen in das Übersinnliche hin- eingeführt werden.",
      "Wir sind Bekenner einer Erkenntnis des Übersinnlichen aus Wissenschaftlichkeit. Nicht nur ist unsere übersinn- liche Erkenntnis wissenschaftlich und läßt sich prüfen von jeder Wissenschaftlichkeit, sondern weil wir das erken- nen, was die anderen Wissenschaften erkennen sollten in ihren Gebieten, streben wir - aus Wissenschaftlichkeit, da wir es müssen aus dieser Wissenschaftlichkeit heraus - zu der Erkenntnis des Übersinnlichen.",
      "Dadurch aber werden wir wirklich geführt zur Erfas- sung des Gesamtmenschen. Denn dasjenige, was ich gerade 233 vorhin angedeutet habe als den Weg nach außen, das führt dazu, Klarheit zu haben über die sogenannten Grenzen des Naturerkennens.",
      "Es führt aber auch dazu, eine An- schauung zu gewinnen, was der Gesamtmensch wird, wenn er sich hineinlebt in ein Erkennen, das solche Grenzen annimmt. Es ist ja nicht bloß, daß wir Wissenschaft trei- ben, sondern indem wir Wissenschaft treiben, sind wir - wenn wir es auch nicht berücksichtigen - Menschen.",
      "Wir werden als Menschen etwas durch den Wissenschafts- betrieb. Wir können aus unserem Bewußtsein herausstrei- chen die Begriffe über die menschliche Wesenheit, aber wir können uns doch nicht in Wahrheit in den Hintergründen gewissermaßen entmenschen innerhalb der Wissenschaft.",
      "Wir müssen zum menschlichen Wesen vordringen. Das können wir nicht, wenn wir uns diejenigen Schranken und Grenzen setzen, von denen heute in der landläufigen Wis- senschaft gesprochen wird, und die auch im praktischen Wissenschaftsbetrieb gefordert werden.",
      "Wir werden zu- rückgeworfen, so daß wir Fähigkeiten verlieren. Wenn man die Muskeln einer Hand nicht gebraucht, so werden sie schwach. Wenn man gewisse Fähigkeiten nicht ge- braucht, weil man sich einbildet, Grenzen seien da und die Fähigkeiten dürften nicht angewandt werden, weil sie sonst die Grenzen überschreiten, so verliert man diese Fähigkeiten.",
      "Nun, meine sehr verehrten Anwesenden, aus dem, was Ihnen hier in diesen acht Tagen vorgeführt worden ist, werden Sie ersehen haben, welch ein Zusammenhang be- steht zwischen der Entwickelung dieser Fähigkeiten, die sich nicht an die gewöhnlich angenommenen Grenzen der Natur binden, und demjenigen, was in der Natur draußen lebt, selber. Dasjenige nämlich, was immer nur hin will bis an die Grenze der Sinneswelt in der äußeren Natur, das kann nicht entfalten jene Kräfte, welche unter die Oberfläche des Sinneswesens hinunterführen und aus dem heraus auch etwas für das menschliche Leben gewonnen werden muß.",
      "Auf dieses, was da gewonnen werden muß, deutet Goethe hin in seinem so bedeutungsvollen, ich möchte sa- gen, gewichtigen Ausspruche: «Wem die Natur ihr offen- bares Geheimnis zu enthüllen anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer würdigsten Aus- legerin, der Kunst.» Hier haben wir den Weg, wo das- jenige, was lebendiges Wissen ist, nicht das Künstlerische abtötet, sondern direkt hineinführt in das Künstlerische. Als die letzten Hochschulkurse im Herbst hier gehalten worden sind, wies ich darauf hin, wie durch dasjenige, was hier gesagt wird, gefunden werden soll, was in ur- alten Zeiten der Menschheit instinktiv vorhanden war: ein Vereinen von Wissenschaft, Kunst und Religion.",
      "Das wird gefunden. Denn wenn man nicht sich selber die Fä- higkeiten abschneidet, ablähmt dadurch, daß man wissen- schaftlich «Grenzen des Naturerkennens» annimmt, dann wird man bemerken, wie man allmählich das, was man an der Natur begreift an Bildungsgesetzen, übergehen las- sen muß in das, was aus diesem Begreifen der Bildungs- gesetze von selber sich künstlerisch gestaltet.",
      "Man kann die menschliche Gestalt, die auch aus der Natur heraus gebildet ist, nicht verstehen, wenn man nicht in der eige- nen Erkenntnis umwandelt, was sonst nur allgemeine Re- geln sind, in künstlerische Anschauung. Wenn dann die Leute kommen und einem sagen: Ja, aber eine Analyse des Erkenntnisvermögens ergibt, daß wir nicht über die Logik hinausgehen dürfen in der Erkenntnis, sondern daß wir alles mit den abstrakten logischen Regeln erfassen müssen, und mit der Beobachtung, mit dem Experiment , dann 235 muß man ihnen erwidern: Aber eine Einsicht, eine geistes- wissenschaftliche Einsicht in die Tatsachen der Welt zeigt etwas anderes. - Die zeigt, daß wir lange reden können, wie Erkenntnis sein muß, wie wir die Erkenntnis gestalten müssen; die Natur aber, sie ergibt sich nicht solchen Er- kenntnissen.",
      "Denn sie schafft selber künstlerisch, und sie will von einem bestimmten Punkte an künstlerisch auf- gefaßt sein. Es gibt einen kontinuierlichen Weg von Wissenschaft in Kunst hinein. Und die Brücke ist keine unnatürliche, die Brücke ist eine selbstverständliche.",
      "Und der andere Weg soll über die Grenzen hinwegführen, welche im Inneren des Menschen aufgerichtet werden. Angedeutet wurde es im Laufe dieser Woche, daß man nicht zu irgendeiner nebulosen, schwammigen mystischen Tiefe kommt, son- dern daß man zu einer klaren Erkenntnis der menschlichen Organisation kommt.",
      "Aber man kommt, indem man die- sen anderen Weg geht - Geisteswissenschaft zeigt das, in- dem sie auf diesem anderen Weg auch wiederum zu Erkenntnissen aufsteigt -, zu etwas, was man nun aus- sprechen möchte mit einem dem eben zitierten Goetheschen Wort ähnlichen Wort. Goethe sagt: «Wem die Natur ihr offenbares Geheimnis zu enthüllen anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer würdigsten Auslegerin, der Kunst.» Mit Rücksicht auf dasjenige, was man nach innengehend wirklich erkennen kann, wenn man wissenschaftliche Gedankenwahrheit entwickelt, kann man sagen: Wem das menschliche Innere sein geheimnis- volles Wesen zu offenbaren beginnt, der empfindet eine tiefe Sehnsucht nach dem würdigsten sich daranschließen- den Gefühl der religiösen Verehrung des schöpferischen Daseins.",
      "Und so finden wir nach außen in die Natur hinein- 236 schreitend den Weg zur Kunst, nach innen in den Men- schen hineinschreitend durch Erkenntnis den Weg zur Religion. Was sich spezialisiert hat in diesen drei Gebie- ten, in der menschlichen Seele muß es doch einheitlich zu- sammenwirken.",
      "Es muß gefunden werden die Möglichkeit dieses einheitlichen Zusammenwirkens. Wird also die Er- kenntnis wiederum fähig gemacht, unterzutauchen in die Geheimnisse der Dinge, was, wie Sie gesehen haben, in diesen acht Tagen hier angestrebt wurde, dann wird sie erst herantreten können an das, was aus der menschlichen Wesenheit herausquillt: die soziale Frage.",
      "Hier werden - weil der Mensch die äußere Verkörperung eines Geistig- Seelischen ist - helfen müssen die Impulse, die wir aus einer Erkenntnis des Geistig-Seelischen gewinnen können. Die so brennende, drängende soziale Frage, die uns so zu Herzen gehen muß heute, insbesondere, wenn wir der heutigen Jugend angehören, sie wird, soweit sie bewältigt werden muß, nur bewältigt werden können, wenn wir gewissermaßen in das Objekt der sozialen Frage, in den denkenden, fühlenden, begehrenden, nach einem men- schenwürdigen Dasein drängenden Menschen den Weg finden.",
      "Daß Geisteswissenschaft nach dieser Richtung hin bestrebt ist, das gehört zu ihrem Wesen. Und wenn man einsieht, was sie über den Menschen zu sagen hat, dann wird man nicht mehr sagen können: Eine ethische, ästhetische, politische oder kulturelle Wertung des sozialen Prozesses liege dem Ziele einer solchen Studie fern.",
      "Ob dieser Prozeß Geschwüre heile oder Sonnen ver- lösche, sei vom Standpunkte der Wissenschaft aus völlig gleichgültig. Es fehlt nur noch, daß man sagt: Medizin habe die Aufgabe, den menschlichen Organismus zu er- kennen; ob es der Medizin auch gelinge, Kranke zu heilen, sei vom Standpunkte der Wissenschaft aus völlig gleich- 237 gültig. - Die Denkweise, die in solchen Sätzen lebt wie dem erst angeführten, und die Denkweise in einem sol- chen absurden Satz, den ich Ihnen eben jetzt angeführt habe, ist im Grunde genommen eine und dieselbe.",
      "Wir sind so weit gekommen, daß man Absurditäten als solche nicht mehr erkennt, wenn sie sich in landläufige wissen- schaftliche Formeln kleiden, wenn sie von Autoritäten ge- formt in die Menge hinaustönen. Das ist es, was uns hier im Goetheanum die Zunge löst, daß wir sprechen müssen.",
      "Wir können nicht anders - und wenn es noch so viele Feinde und Gegnerschaften gäbe -, als zusammenarbeiten in einer solchen Richtung auch mit der Studentenschaft. Wir wissen, was es heißt, Student zu sein.",
      "Das heißt, in seinem Herzen zu tragen, was als Kraft hinüberfließen muß in die Zukunft. Ja, diese Zukunft, die jetzt die Menschheit erwartet, sie wird kraftvolle Seelen brauchen, in deren Wille und Emotionen hineinspielt eine klare Ein- sicht in Weltwesen und Menschenleben.",
      "Weil wir wissen, daß Sie so etwas brauchen werden, deshalb sprechen wir zu Ihnen, insofern Sie uns mit Verständnis entgegenkom- men wollen. Wir haben Sie wahrhaftig mit hierher geru- fen - obwohl wir Sie alle, wie Sie mir glauben können, persönlich sehr gerne sehen -, wir haben Sie mit hierher gerufen, weil wir hoffen, daß Sie Mitarbeiter werden auf einem Wege, den wir als einen notwendigen für die Ge- genwart und für die nächste Zukunft ansehen, und weil wir die Probe machen wollen - und wir werden sie immer mehr und mehr machen, ich hoffe, sie wird sich trotz aller Widerstände machen lassen , weil wir die Probe darauf- hin machen wollten, wie viele sich finden können, in deren Herzen das ein Echo findet, was wir glauben als eine Not- wendigkeit dieser unserer Zeit zu erhärten. 238 Wir müssen uns nun wiederum trennen, meine sehr ver- ehrten Kursbesucher.",
      "Allein ich glaube, in einem können wir beisammen sein, beisammen bleiben, trotz aller Rau- mesentfernung beisammen bleiben: in der Erkenntnis, daß nach der Richtung, die hier angedeutet wurde, doch fort- geschritten werden müsse, daß gearbeitet werden müsse, daß Wille in dieser Richtung entwickelt werden müsse, so- viel jeder nur kann. Er wird, wenn er die nötige Einsicht gewinnt, diesen Willen entwickeln.",
      "Wir sind heute noch nicht in der Lage - das spreche ich zu Ihnen, meine lieben Kommilitonen -, das, was wir Ihnen hier bieten können, zum Abschlüsse dadurch zu bringen, daß wir Ihnen Abschlußprüfungen ermöglichen, die Ihnen Lebensstellungen geben. Wir sind in dieser Be- ziehung arme Leute, die lediglich an das appellieren kön- nen, was als Wahrheitssinn, als Erkenntnisenthusiasmus in Menschenseelen und Menschenherzen waltet.",
      "Wir kön- nen uns nur der Hoffnung hingeben, daß neben alledem, was in ungesunder Weise in die Prüfungen und Lebens- stellen hineinläuft, auch noch in einer genügend großen Anzahl Jugend sich Herzen und Seelen finden, die hin- wollen zu der Wahrheit, um der Wahrheit willen zu dem, wovon man glauben kann, daß es nach den Zeichen dieser Zeit notwendig sei, um dieser rein menschlichen Notwen- digkeit willen. Wir glauben, daß noch so viel freies Ge- fühl vorhanden ist, daß aus diesem reinen Freiheitsdrang heraus diese beiden Bestrebungen entstehen können.",
      "Weil wir dieses glauben müssen, stehen wir, die wir diese Vorträge gehalten, diese Veranstaltungen gemacht haben im Laufe der letzten Woche, stehen wir alle hier, Ihnen, die Sie nun wieder zurückkehren in das übrige Leben, ein Lebewohl zuzurufen. Aber wir stehen hier, hoffend darauf, daß Sie unsere Helfer sein werden, Sie 239 begleitend mit den Gedanken, die wir gemeinsam durch unsere Seelen haben ziehen lassen, Sie begleitend mit den besten Wünschen dazu, daß Ihr Wille zur Klarheit, Ihr Wille zum entsprechenden Tun stark sei.",
      "In dieser Hoff- nung und mit diesen Wünschen trennen wir uns, um uns hoffentlich wiederzusehen, und sagen Ihnen von dieser Stätte aus ein herzliches Lebewohl und auf Wiedersehen! 240"
    ],
    "sentences": [
      [
        "Obwohl ich heute abend noch einen gewissermaßen außer- halb des Programmes stehenden Vortrag um acht Uhr für alle Kursteilnehmer dieser Woche halten werde, stehen wir doch jetzt am Ende unserer Frühjahrs-Vortragsreihe.",
        "Wir konnten in der kurzen Zeit, die uns zur Verfügung stand, wie es ja selbstverständlich ist, nur Andeutungen und Richtlinien geben über das, was uns auf ein gewisses Ziel hin vorschwebt."
      ],
      [
        "Und dies Ziel - Sie werden es gerade an diesen Vorträgen haben fühlen können - ist kein an- deres als dieses: zu zeigen, wie das, was hier anthroposo- phisch orientierte Geisteswissenschaft genannt wird, be- fruchtend wirken soll auf die verschiedenen einzelnen Fachwissenschaften und auch auf die verschiedenen Zweige des menschlichen praktischen Lebens in der Gegenwart.",
        "Wir haben, um hinweisen zu können, in welcher Art wir uns dieses Ziel vorstellen, zunächst durchgenommen, tageweise, diejenigen Wissenschaften, welche hineinführen in das Leben der äußeren Welt, der äußeren Natur."
      ],
      [
        "Wir haben zu zeigen versucht, wie da von den Erkenntnis- bestrebungen der Gegenwart überall Schranken und Gren- zen aufgerichtet werden, welche aber keine wirklichen Schranken und Grenzen menschlicher Seelentätigkeit über- haupt sein können, weil, wenn sie gelten könnten, das- jenige, was dem Menschen das wesentlichste Ziel der Er- kenntnis sein muß, das Durchschauen der menschlichen Wesenheit selber, niemals erreichbar sein würde.",
        "Und vor allen Dingen fehlen müßte eine Erkenntnis, welche An- 218 trieb werden kann des menschlichen Willens, der mensch- lichen Tat."
      ],
      [
        "Der menschliche Wille und die menschliche Tat müßten verurteilt sein, weiterhin nur aus den Instinkten und Trieben heraus das soziale Leben zu gestalten, wäh- rend ein menschenwürdiges Dasein nur begründet werden kann, wenn geistige Einsicht die Kraft hat, über die bloße Naturanschauung hinaus in das rein geistige Leben ein- zutauchen und von daher die sittlichen und die sozialen Ideale zu holen, die mächtig genug sind, um in den Willen impulsierend hineinzuwirken.",
        "So mußten wir auf der einen Seite darauf hinweisen, wie Geisteswissenschaft über die Schranken hinauskom- men will, die der äußeren Wissenschaft, insofern sie sich auf die äußere Natur und auf die äußere Welt bezieht, gesteckt sein sollen, nach dem Willen gerade und nach der Meinung und dem Glauben unserer Zeit."
      ],
      [
        "Und wir mußten auf der anderen Seite hinweisen auf die andere Richtung des menschlichen Erkennens: die nach innen geht, die dar- auf geht, den Menschen und sich selber zu erfassen, so daß man hinuntersteigen kann in das, was im Menschen als sein eigentlicher Wesenskern lebt.",
        "Und wir haben gezeigt, daß allein, wenn dieser Impuls wirklich in das Innere des Menschen eindringt, in der Erkenntnis lebt, daß dann allein zustande kommen könne zum Beispiel eine wirk- liche Sprachwissenschaft, eine wirkliche Geschichtswissen- schaft auch, und daß dieser Impuls der Innenerkenntnis notwendig ist, um die sprachlichen, die geschichtlichen Wissenschaften zu durchdringen und zu befruchten."
      ],
      [
        "So haben wir nach zwei Richtungen hingewiesen, in de- nen hinweggeschritten werden muß über die Grenzen, welche die gegenwärtige Fachwissenschaft setzen will: in die Richtung nach außen, in die Richtung nach innen.",
        "Und wir haben darauf hingewiesen in diesen Tagen, wie der 219 Appell an eine solche Geist-Erkenntnis uns ja hervortönt aus den wichtigsten Zeichen der Zeit."
      ],
      [
        "Da haben wir auf der einen Seite die zahlreichen An- zeichen, wie die Menschen in weitesten Kreisen bestrebt sind, immer tiefer und tiefer hineinzukommen in die Rät- sel des menschlichen Inneren, um da, in diesem mensch- lichen Inneren, einen sicheren Halt zu bekommen, ein rich- tiges Gleichgewicht zum äußeren sozialen Leben zu erhal- ten.",
        "Und wenn wir vernehmen die wichtigsten Stimmen des menschlichen Herzens, des menschlichen Gemütes, so müssen wir sagen: es tönt überall aus den Anforderungen der Gegenwart heraus, daß wissenschaftliche Erkenntnis ausmünden müsse in das, was so für die innere Sicherung der menschlichen Seele gefunden werden muß."
      ],
      [
        "Kein Aus- blick nach einem solchen Ziele ist in der gegenwärtigen landläufigen Wissenschaft zu finden.",
        "Weil er darinnen nicht zu finden ist, glaubt Geisteswissenschaft den Schritt tun zu müssen, diesen anderen Wissenschaften zu zeigen, wie sie durch wahre geisteswissenschaftliche Forschung be- fruchtet werden können."
      ],
      [
        "Von der anderen Seite her tönen die Klänge aus der sozialen Verwirrung.",
        "Große, gewaltige soziale Aufgaben stehen vor den Menschen unseres Zeitalters.",
        "Wir werden mit ihnen nur zurechtkommen, wenn wir einsehen, daß ja doch nur das, was wir uns an Einsicht in das Menschen- leben, an Erkenntnis der menschlichen Wesenheit erwer- ben können, uns die Kraft geben kann, an die großen sozialen Aufgaben der Gegenwart heranzutreten."
      ],
      [
        "Führend müssen wieder werden die Einsichten, führend muß das werden, was aus echter, wahrer geisteswissenschaftlicher Forschung hervorgeht, denn das allein kann auch rich- tunggebend sein für die sozial so notwendigen Bestre- bungen. 220 Es wird das gerade unseren Absichten übelgenommen, daß wir die Frage, auf die hiermit gedeutet ist, in einer etwas anderen Weise auffassen müssen als viele unserer Zeitgenossen.",
        "Ich habe auf dieses Anderssein schon bei den verschiedensten Gelegenheiten hinweisen müssen."
      ],
      [
        "Aber das ist etwas, was immer wiederum gesagt werden muß.",
        "Da- her will ich es auch heute, am Schlüsse unserer Veranstal- tung, hier sagen.",
        "Gewiß, es gibt schon viele Leute, die sagen: Über die weitesten Kreise der Bevölkerung hinaus muß Einsicht, muß Wissen sein; Wissen muß popularisiert werden, denn es muß leben in einer genügend großen An- zahl von Menschen; nur wenn es in ihnen lebt, werden sich auch die sozialen Einsichten entwickeln."
      ],
      [
        "Und aus dem guten Willen, der zweifellos dem zugrunde liegt, geht hervor alles, was man unternimmt in der Richtung der Einsetzung von Volkshochschulen, Volksbibliotheken, Po- pularisierung der Wissenschaft, wie sie an unseren heuti- gen Bildungsanstalten gepflegt wird.",
        "Man ist der Mei- nung, wenn man nur hinausträgt, was an unseren Bil- dungsanstalten gepflegt wird, in die weitesten Kreise, dann müsse es in der Zukunft verhindern, daß wir in solche katastrophalen Epochen hineinkommen, wie die unsrige es ist."
      ],
      [
        "Aber kann man denn glauben, daß dasjenige, was ja da war für die Menschen, die unmittelbar zu tun hatten mit den Ursachen dieser jetzigen katastrophalen Zeit, daß das, was also von unseren Bildungsanstalten ausgestrahlt ist auf die führenden Kreise und nichts gefruchtet hat, sie zu besserem Tun zu bringen als zu dem, wozu sie gekommen sind, kann man hoffen, daß dasselbe «Geistes- gut», wie man es eben auch nennt, nun wirken werde, wenn es in die große Menge hinausgestreut wird?",
        "Man kann solches nur glauben, wenn man sich selber Sand in 221 die Augen streuen will."
      ],
      [
        "Weil wir das nicht wollen, die wir uns hier verbunden fühlen mit den Bestrebungen des Goetheanismus, deshalb müssen wir sagen, trotz alledem, was da gleich aufgerufen wird an allen möglichen Feind- und Gegnerschaften: Nein, anderes ist noch notwendig! - Nicht bloß hinausgetragen werden soll etwas aus unseren Bildungsanstalten, hineingetragen werden muß etwas.",
        "Es muß das hineingetragen werden, was erst hineingetragen werden kann, wenn man die geistige Forschung neben der äußeren sinnlichen und verstandesmäßigen anerkennen will."
      ],
      [
        "Was dann in unsere Bildungsanstalten hineingetragen wird, das wird schon ergreifen die Herzen und die Ge- müter der Menschen, weil es hervorgeholt ist aus dem Wesen der Herzen und der Gemüter der Menschen, weil dasjenige, was unbewußt in der Menschen Tiefen schlum- mert, auf diese Weise zutage gefördert wird als Richtungs- kräfte für menschliches Wirken.",
        "Wir sind schon einmal in der für viele unsympathischen Lage, uns zu der Ansicht bekennen zu müssen, daß nicht nur etwas herausgetragen werden müßte aus unseren Bildungsanstalten, sondern vor allen Dingen viel, viel hineingetragen werden müsse."
      ],
      [
        "Und daß wir uns vermessen, hinzuweisen auf solche Dinge, das ist es, was uns so viele Feindschaft einträgt.",
        "Nun, Sie dürfen es mir glauben: persönlich wäre es mir das allerliebste, wenn der Drang nach solcher Geistes- berufung der Wissenschaften vor allen Dingen sich erhe- ben würde aus den Stätten unserer bisherigen Bildung selber, wenn da sich diejenigen finden würden, die hinwei- sen möchten darauf, was nötig ist."
      ],
      [
        "Über nichts würde ich mich mehr freuen, nichts würde mich mehr befriedigen, als wenn ich solches Streben sehen könnte.",
        "Ja, deshalb hatte ich wirklich verzeihen Sie diese einzuschiebende Epi- sode - einige Freude, als ich jüngst in Basel drinnen war 222 und im Schaufenster eine Schrift entdeckte, die den Titel trägt «Universitätsreform», geschrieben von einem Uni- versitätsprofessor selber, wie sich gleich herausstellte."
      ],
      [
        "Das, dachte ich mir, macht vielleicht ganz unnötig das Streben nach einer Begründung des Weltschulvereins, wenn solche Stimmen von solcher Seite herkommen.",
        "Und die Schrift beginnt auch gleich außerordentlich verheißungsvoll."
      ],
      [
        "Man hat so das Gefühl, daß mit solchen Sätzen etwas ange- schlagen werden müsse, was die Zeichen der Zeit nach einer gewissen Richtung hin versteht: «Die Organisation unserer Universitäten leidet an großen Mängeln.",
        "Ein Re- formwerk tut hier dringend not."
      ],
      [
        "An diesem Werk soll aber allein teilnehmen, wer das Universitätswesen von Grund aus kennt.» Auch darüber könnte man erfreut sein, wenn solche teil- nehmen würden, die das Universtätswesen von Grund auf kennen.",
        "Weil ich aber in dem, was ich weiter in dieser Schrift erfahren habe, ein Symptom charakterisieren möchte, so müssen Sie mir schon gestatten, daß ich in aller Kürze über das Erlebnis an dieser Schrift etwas spreche."
      ],
      [
        "Auf Seite 4 findet man ausgedrückt, was der Verfasser nun ausschließt von seiner Betrachtung über dieses Re- formwerk bezüglich der Universitäten: «So werde ich zum Beispiel mich über die Frage der Semestereinteilung und der Universitätsferien nicht äußern.",
        "Denn diese Dinge sind noch nicht spruchreif.» Ein Weiteres, das ausgeschlossen werden soll von dieser Betrachtung: «So werde ich ferner die Rechtsverhältnisse der Assistenten unserer Kliniken oder unserer naturwissen- schaftlichen Institute unerörtert lassen."
      ],
      [
        "Denn ich traue mir ein sachverständiges Urteil darüber nicht zu.» Nun, man könnte ja ganz zufrieden sein, wenn diese zwei Punkte ausgeschlossen bleiben würden von einer Be- 223 trachtung darüber, wie notwendig ein Reformwerk an unseren Universitäten ist.",
        "Dann wird dasjenige, was nun zu reformieren ist, in einzelnen Kapiteln abgehandelt."
      ],
      [
        "Das erste Kapitel heißt: «Die Einteilung der Universitätslehrer in verschiedene Klassen.» Man erfährt daraus, daß es ordentliche, außer- ordentliche Professoren gibt, Privatdozenten, Honorar- professoren, Lektoren und Assistenten.",
        "Man erfährt dar- aus, daß es notwendig ist, hier mit einem großen Reform- werk einzusetzen, daß es zum Beispiel notwendig ist, daß gewisse Leute, die nach dem gegenwärtigen Usus ihr gan- zes Leben lang außerordentliche Professoren geblieben sind, weil sie zum Beispiel nur ein Nebenfach - die Ohren- heilkunde oder die Ägyptologie - zu vertreten hatten, daß die nun zu, nun, auch zu ordentlichen Professoren ernannt werden müssen; nur daß man doch nicht gleich über die Schnur hauen soll, erfährt man, daß man bei all denen, die vom außerordentlichen Professor zum ordentlichen Professor zu ernennen sind, das Gehalt doch ein geringeres wird sein lassen müssen, als dasjenige, welches die richtigen ordentlichen Professoren bekommen."
      ],
      [
        "Dann schreiten wir weiter zum nächsten Kapitel über die Bestellung der Universitätslehrer.",
        "Da wird unter an- derem auf das Außerordentliche, Bedeutsame hingewiesen, daß sich ja Diskrepanzen ergeben haben zwischen den Regierungen und den Fakultäten oder den Professoren- kollegien, und daß es etwas Bedenkliches hätte, wenn man etwa gar zu stark darauf rechnen würde, daß aus den Professorenkollegien selber einzig und allein die Ernen- nung hervorgehen könnte."
      ],
      [
        "Die Regierungen haben da manchmal Besseres getan als die Professorenkollegien.",
        "Man muß nach einem Ausweg suchen.",
        "Es ist allerdings die Schrift für deutsche Verhältnisse 224 geschrieben, allein ich glaube, sie ist für Weltverhältnisse zum mindesten symptomatisch und darf daher hier ange- führt werden."
      ],
      [
        "Da wird nach einem Ausweg gesucht, wie man darüber hinauskommen könne, daß die Diskrepan- zen zwischen den Kollegien und den Regierungen ver- schwinden, und da wird hingewiesen darauf, daß man die wichtige Einrichtung ins Leben rufen müsse eines «Reichs- universitätsrates»!",
        "Wir kommen - ich will recht schnell über die Dinge hin- weggehen - zum dritten Kapitel: Das Gehalt der Uni- versitätslehrer."
      ],
      [
        "Nun, da wird eben auseinandergesetzt, wel- che Wünsche vorliegen über die Gehaltsregulierungen.",
        "Ein Kleines habe ich Ihnen schon davon mitgeteilt.",
        "Wir kommen zum vierten Kapitel: Die Überweisung der Vorlesungsgebühren an die Universitätslehrer."
      ],
      [
        "Da wird darauf hingewiesen, daß mancher, der ein sehr tüch- tiger Mann ist, nur ein ganz kleines Kolleg hat, ein ande- rer, der gerade etwas Beliebtes liest, hat ein großes Kolleg, bekommt also viele Kolleggelder.",
        "Es wird darauf hin- gewiesen, daß zum Beispiel derjenige, der nur drei Stun- den zu lesen hätte über seinen Gegenstand, daß der fünf oder sechs Stunden erhält, damit das Kolleggeld höher werde."
      ],
      [
        "Kurz, es sei nicht anders hinauszukommen, als daß man diese Sache einer gründlichen Reform unterziehe.",
        "Dann, im fünften Kapitel, wird von der Verleihung von Auszeichnungen an die Universitätslehrer gesprochen, was auch eine Angelegenheit ist, die eine gründliche Re- form erfordert."
      ],
      [
        "In einem sechsten Kapitel wird gesprochen über die Art des Ausscheidens der Universitätslehrer aus ihrer Lehrstel- lung.",
        "Da wird darauf hingewiesen, daß da viele Un- gerechtigkeiten geschehen könnten.",
        "Allein wenn ein «Uni- versitätsdienstgericht» eingerichtet wird, welches zum Teil 225 besteht aus den würdigsten Mitgliedern des «Reichsuni- versitätsrates», dann wird es mit diesen Dingen schon gehen."
      ],
      [
        "Dann wird darauf hingewiesen, wie durch solche In- stanzen, wie den «Reichsuniversitätsrat» und das «Uni- versitätsdienstgericht», nun auch einmal Ordnung hinein- kommen könne in dasjenige, was im siebenten Kapitel angeführt wird, das «Dienststrafrecht der Universitäts- lehrer», was zu geschehen hat, wenn man sie entlassen will oder wenn sie nur einen Verweis oder so etwas be- kommen sollen.",
        "Dann finden wir ein besonderes Kapitel über «Besondere Dienstaufträge der Universitätslehrer»."
      ],
      [
        "Wir finden ein Kapitel über die «Verwaltung der Universitätsangelegen- heiten», worinnen aber nur über solche Dinge gesprochen wird, die eben Besprechungen dahin notwendig machen, ob nun auch die außerordentlichen Professoren und die Privatdozenten vielleicht durch einen Vertreter teilnehmen sollen, und in welcher Weise das geschehen soll, an dem, was man ausmacht.",
        "In einem elften Kapitel wird über das «Universitäts- vermögen» gesprochen."
      ],
      [
        "In einem zwölften Kapitel davon, wie man zurechtkommen soll, wenn sich Leute melden, die nicht ganz ihre Vorprüfung gemacht haben.",
        "In einem dreizehnten Kapitel wird darauf aufmerksam gemacht, daß das Doktorsein durch verschiedene Umstände ein Un- fug ist, und daß man daher künftig nicht doktorieren soll durch Prüfungen, sondern daß derjenige, der die Staatsprüfung, die Assessorprüfung, die philologische Schulamtsprüfung und ähnliches absolviert hat, berechtigt sein soll, sich in Zukunft selber Doktor zu nennen."
      ],
      [
        "Aber das führt doch wiederum zu Schwierigkeiten, nämlich, wenn sich diejenigen, die vom Staat angestellt sind, Dok- 226 tor nennen können - ich weiß nicht den inneren logischen Zusammenhang, ich habe ihn nicht begriffen -, dann wären doch keine Garantien dafür geboten, daß das auch Gelehrte jetzt wären, und deshalb müsse noch extra eine Gelehrtenprüfung eingeführt werden.",
        "Man könne aller- dings nicht hoffen, daß die Leute große Lust haben, diese Gelehrtenprüfung noch extra abzulegen; allein, man könne dafür noch extra einen Ersatz eintreten lassen, zum Bei- spiel den, daß dem, der sie abgelegt hat und nachher promoviert wird, daß dem das Jahr, in dem er diese Ge- lehrtenprüfung abgelegt hat, doppelt angerechnet werde zu seiner Dienstzeit."
      ],
      [
        "Ja, meine sehr verehrten Anwesenden, ich rede von einer sehr ernsten Angelegenheit, ich rede von einem Buch über Universitätsreform, das damit beginnt: Die Organi- sation an unseren Universitäten leide an großen Mängeln, ein Reformwerk tue dringend not, und ich habe, als ich dreizehn Kapitel durchgemacht hatte, gesehen, ich war schon auf Seite 43 angekommen, nun gab es noch andert- halb Seiten; ich hoffte, nun wird es kommen!",
        "Aber siehe da, jetzt kommt ein vierzehntes Kapitel: «Wissenschaft- liche Forschungsanstalten.» Da wird gesagt, daß ja aller- dings auch für diese einiges zu tun wäre, daß als richtige Forscher zum Beispiel nur diejenigen angestellt werden dürften, die zuerst Universitätsprofessoren gewesen sind, denn nur die seien wirkliche Forscher."
      ],
      [
        "Und dann schließt auf Seite 44 diese Schrift damit: «Es empfiehlt sich des- halb, das Gehalt von Mitgliedern von Forschungsanstalten nicht ganz so hoch zu bemessen wie das von ordentlichen Universitätsprofessoren des gleichen Dienstalters; sie kön- nen sich ja darüber auch nicht beklagen, da sie ja von der schweren Unterrichtslast ganz befreit sind.",
        "Auch ist ir- gendwie Vorsorge dahin zu treffen, daß die Mitglieder 227 der Forschungsinstitute ihre Stellung als Honorarprofesso- ren nicht dazu benutzen, um sich übermäßige Vorlesungs- gebühren zu sichern.» Ja, damit ist die Schrift wirklich zu Ende."
      ],
      [
        "Und ich habe eigentlich ganz unvermerkt einiges ausgelassen.",
        "Ich hatte allerdings, als ich die Schrift zu Ende gelesen hatte, so das Gefühl: Also die Universitäten bestehen aus Professoren, ordentlichen und außerordentlichen Professoren, Privat- dozenten, Lektoren und Assistenten."
      ],
      [
        "Aber da fiel mir ein: an der Universität, da sind ja auch Studenten, und ich fragte mich, hängen vielleicht diese Studenten doch auch etwas zusammen mit dem Zwecke der Universitäten?",
        "Da konnte ich denn konstatieren, daß sieben und zehn, gleich siebzehn Zeilen den Studenten gewidmet sind in dieser Schrift, welche nahezu vierundvierzig Seiten umfaßt."
      ],
      [
        "Aber die ersten sieben Zeilen auf Seite 5 - aus denen konnte ich nichts Besonderes machen.",
        "Denn die sagen eigentlich so furchtbar wenig Positives: «Deshalb gehe ich nicht weiter darauf ein, ob sich nicht das Verhältnis zwischen Universitätslehrern und Studenten inniger gestalten und vor allem die Sprechstunde der Universitätslehrer frucht- barer einrichten ließe, als das jetzt im großen und ganzen der Fall ist."
      ],
      [
        "Denn hier wäre mit Verwaltungsvorschriften gar nichts auszurichten.",
        "Hier wäre jeder Zwang, der nur von außen käme, hoffnungslos.» Dann wollte ich mich noch halten bezüglich der Studen- tenschaft an die Seite, welche in zehn Zeilen über die Stu- denten handelt."
      ],
      [
        "Aber da konnte ich auch nichts machen, denn die handeln bloß über das «Ordnungsstrafrecht der Studenten».",
        "Nun, ich habe das, was ich mitgeteilt habe, eigentlich nicht mitgeteilt, um ironisch zu werden, um Lachen zu erregen oder dergleichen, sondern ich habe es mitgeteilt als 228 auch ein Zeichen der Zeit, und ich bemerke ausdrücklich, daß ich den Mann, der das geschrieben hat, für einen außerordentlich guten, einen außerordentlich gescheiten Menschen halte, der sich nur nicht entschließen kann, be- züglich seines Reformwerkes auf etwas anderes zu reflek- tieren als auf dasjenige - er sagt es selbst -, was sich durch Verwaltungsmaßregeln durchführen läßt."
      ],
      [
        "Nun, ich denke, wir haben heute noch andere Dinge notwendig als die- jenigen, die sich durch Verwaltungsmaßregeln durchführen lassen.",
        "Die Zeichen der Zeit fordern durchaus anderes.",
        "Aber nicht nur ein gutwilliger, ein gescheiter Mensch ist der Verfasser dieser Schrift über «Universitätsreform», sondern er ist auch ein sich selbst gut kennender Mensch, und er verrät, warum er eigentlich über solche Dinge nicht hinausgeht."
      ],
      [
        "Und da finden wir denn etwas sehr Merk- würdiges auf Seite 4: «So werde ich weiter die Reform des Universitätsunterrichts im engeren Sinne schweigend übergehen.",
        "Sie liegt mir freilich sehr am Herzen und ist mindestens so wichtig wie sämtliche übrigen Reformen, die ich demnächst mehr oder weniger ausführlich behan- deln werde."
      ],
      [
        "Mein Schweigen fällt mir deshalb schwer.",
        "Allein was ich darüber sachkundig zu sagen hätte, würde im wesentlichen bloß für den Unterricht in der Rechts- wissenschaft und der Volkswirtschaft gelten, hätte dage- gen für den Unterricht in der Philologie, der Medizin, den Naturwissenschaften nur geringe Bedeutung."
      ],
      [
        "Eine auf den rechtswissenschaftlichen und volkswirtschaftlichen Unter- richt beschränkte Untersuchung würde aber nicht in den Rahmen einer Abhandlung passen, die sich mit der Re- form der Gesamtuniversität befaßt.» Ja, denken wir uns, die Sache hätte nicht ein Jurist ge- schrieben, dann könnte hier stehen: «Mein Schweigen fällt mir deshalb schwer.",
        "Allein was ich darüber sachkundig zu 229 sagen hätte, würde im wesentlichen bloß für den Unter- richt in der Medizin gelten, hätte daher für den Unterricht in der Rechtswissenschaft und Volkswirtschaft nur geringe Bedeutung."
      ],
      [
        "Eine auf den medizinischen Unterricht be- schränkte Untersuchung würde aber nicht in den Rahmen einer Abhandlung passen, die sich mit der Reform der Gesamtuniversität befaßt.» Und nun könnte ich Ihnen mit Abänderung des Sub- jekts diesen Satz recht oft vorlesen und Sie würden daraus sehen - wenn Sie sich das dahinterliegende Faktum vor die Seele rufen , wozu namentlich das Spezialistentum, wie es wuchernd geworden ist, geführt hat.",
        "Zur Tatlosigkeit hat es den Wissenschafter verurteilt."
      ],
      [
        "Niemand weiß über dasjenige, was im Großen zu geschehen hat, zu reden, weil er Jurist, weil er Volkswirtschafter, Mediziner, Philologe ist und so weiter.",
        "Man wird gewissermaßen heute Wissen- schafter, um über die eigentlichen Angelegenheiten des menschlichen Wissens bekennen zu müssen, daß man über sie nichts weiß."
      ],
      [
        "Solch ein Symptom ist deshalb von Bedeu- tung, weil es nun wirklich von einem gescheiten, gutwilli- gen Menschen, der außerdem noch die nötige Bescheiden- heit hat, kommt.",
        "Aber ich denke, es weist um so mehr auf die Notwendigkeit hin, daß in die Stätten, um die es sich handelt, etwas hineingetragen werden muß, nicht bloß, daß etwas herausgeholt werden könne zu den Zielen, von denen ich vorhin geredet habe."
      ],
      [
        "Deshalb, glaube ich, mußten wir, durften nicht nur, mußten und müssen es immer wiederum, hinweisen auf das, was von Seiten der Geisteswissenschaft befruchtend hineinwirken soll in die einzelnen Zweige des Fachwis- sens, aber schließlich auch in die einzelnen Zweige des praktischen Denkens.",
        "Denn die Art und Weise, wie wir allmählich zu den Abstraktionen in den Wissenschaften 230 gekommen sind, die haben hervorgerufen eine Stellung von Wissenschaftlichkeit in einer trockenen, unpraktischen, lebensfremden Daseinszone."
      ],
      [
        "Und man kann es selbst für das soziale Gebiet erleben, daß ein Mann wie Schumpeter, der wiederum ein außerordentlicher, kluger, gescheiter Mann ist und eine gescheite Abhandlung über Imperialis- men geschrieben hat, mit den Worten schließt: «Eine ethische, ästhetische, politische oder kulturelle Wertung dieses Prozesses liegt den Zielen dieser Studien fern.",
        "Ob dieser Prozeß Geschwüre heilt oder Sonnen verlöscht, ist von ihrem Standpunkte (nämlich vom wissenschaftlichen Standpunkte) aus völlig gleichgültig."
      ],
      [
        "Das zu beurteilen ist nicht Sache der Wissenschaft.» Das heißt, Sache der Wissenschaft ist es, etwas hervor- zubringen, was vor dem Leben halt macht, was nicht zu Wertungen führt im ethischen, ästhetischen, im kulturel- len Leben.",
        "Wir haben es im Laufe dieser Vortragsreihe gesehen, welche merkwürdige Tatsache aufgetreten ist in- folge dieses abstrakten Gestaltens der Wissenschaftsbestim- mung."
      ],
      [
        "Wir haben gesehen, wie die Wertphilosophie, die Rickertsche, Windelbandsche und so weiter Wertphiloso- phie heraufgezogen ist.",
        "Idi glaube, aus den Ausführungen des Dr.",
        "Stein ging Ihnen klar hervor, um was es sich ge- handelt hat."
      ],
      [
        "Da hat es sich darum gehandelt, daß nun zunächst auf naturwissenschaftlicher Seite das Sein be- ansprucht wird, aber daß man sich auf der naturwissen- schaftlichen Seite, wo man das Sein in seiner Totalität beansprucht, durchaus nicht darauf einlassen will, noch irgend etwas philosophisch zu treiben.",
        "Man will sich auf den Stuhl der Wissenschaft setzen, der das Sein darstellt, und man will alles, was über das Sein auszumachen ist, von naturwissenschaftlicher Seite ausmachen."
      ],
      [
        "Auf philo- sophischer Seite macht man keine Anstalten - verzeihen 231 Sie, das Bild ist nicht so schlimm gemeint, als ich es aus- spreche -, den Stuhl zur Bank zu machen, den anderen etwas zur Seite zu rücken und sich selber auf den Stuhl des Seins zu setzen.",
        "Nein, weil einem die Wertung über- lassen ist, weil die Wissenschafter sagen: ethische, ästhe- tische, kulturelle Wertungen liegen der Wissenschaft fern, seien nicht Sache der Wissenschaft, setzt man sich auf den Stuhl der Wertungen, damit man eine reine Abgrenzung hat."
      ],
      [
        "Man spezialisiert bis in die Geistigkeit hinein und verliert die Möglichkeit, wirklich an den Menschen heran- zukommen, der gewiß nicht anders kann, als, indem er im Sein lebt, etwas darzuleben, was für ihn selber eine ethische, ästhetische, kulturelle Wertung darstellen muß.",
        "Die Dinge, um die es sich heute handelt, gehen wirklich in die Tiefen."
      ],
      [
        "Und deshalb sollte die Mitwelt schon die Geneigtheit entwickeln, die Grundfrage zu beantworten: Ist diese Geisteswissenschaft, welche von sich behauptet, daß sie die einzelnen Fachwissenschaften und auch Zweige des praktischen Lebens befruchten könne, ist diese Geistes- wissenschaft selber wissenschaftlich? - Und in dieser Be- ziehung wird die Geisteswissenschaft sich auf den Stand- punkt stellen, daß ihr jedes Eingehen auf sie mit voller wissenschaftlicher Gründlichkeit und mit guten wissen- schaftlichen Vorkenntnissen aus den einzelnen Wissen- schaften der Gegenwart heraus - aber natürlich nicht aus Dilettantismus heraus -, daß ihr jedes Eingehen auf sie mit guter Wissenschaftlichkeit willkommen ist.",
        "Sie schreckt nicht vor den Prüfungen derer zurück, die etwas wissen, und sie wird um so froher sein, je mehr diejenigen wissen, welche sie vom Standpunkte der einzelnen Wissenschaften heraus prüfen wollen."
      ],
      [
        "Das ist das erste, was ich Ihnen heute am Schlüsse un- serer Frühjahrskurse sagen möchte. 232 Das zweite ist aber das, was viele uns vorwerfen, daß wir in unerlaubter Weise nach dem Übersinnlichen stre- ben, daß wir zu den Menschen reden von einer Erfor- schung des Übersinnlichen, daß aber das schon von vorne- herein unwissenschaftlich sei, denn vom Übersinnlichen könne man ja nichts wissen.",
        "Nun, der Nerv der Ausführungen dieser Woche, der war, ich möchte sagen, wie von selbst dahin gerichtet, zu zeigen, daß wir zu dem übersinnlichen Forschen gehen wollen nicht aus dem Grunde, weil wir über die Wissen- schaft hinauswollen zu irgendeinem nebulosen Zeug, daß wir nicht nach dem Übersinnlichen streben, weil wir un- wissenschaftlich sein wollen, sondern daß wir uns auf den Boden der Wissenschaft stellen, so wie sie jetzt ist, daß wir uns aber ehrlich auf diesen Boden stellen."
      ],
      [
        "Und indem wir uns ehrlich auf diesen Boden stellen, finden wir, wo in diesen Wissenschaften überall die Tore sind aus ihnen selbst heraus und in die übersinnliche Welt hinein.",
        "Nicht weil wir uns neben die Wissenschaften hinbegeben wollen, nicht aus Unwissenschaftlichkeit reden wir von dem Über- sinnlichen, sondern weil wir aus der Wissenschaft selbst mit wissenschaftlichen Gründen in das Übersinnliche hin- eingeführt werden."
      ],
      [
        "Wir sind Bekenner einer Erkenntnis des Übersinnlichen aus Wissenschaftlichkeit.",
        "Nicht nur ist unsere übersinn- liche Erkenntnis wissenschaftlich und läßt sich prüfen von jeder Wissenschaftlichkeit, sondern weil wir das erken- nen, was die anderen Wissenschaften erkennen sollten in ihren Gebieten, streben wir - aus Wissenschaftlichkeit, da wir es müssen aus dieser Wissenschaftlichkeit heraus - zu der Erkenntnis des Übersinnlichen."
      ],
      [
        "Dadurch aber werden wir wirklich geführt zur Erfas- sung des Gesamtmenschen.",
        "Denn dasjenige, was ich gerade 233 vorhin angedeutet habe als den Weg nach außen, das führt dazu, Klarheit zu haben über die sogenannten Grenzen des Naturerkennens."
      ],
      [
        "Es führt aber auch dazu, eine An- schauung zu gewinnen, was der Gesamtmensch wird, wenn er sich hineinlebt in ein Erkennen, das solche Grenzen annimmt.",
        "Es ist ja nicht bloß, daß wir Wissenschaft trei- ben, sondern indem wir Wissenschaft treiben, sind wir - wenn wir es auch nicht berücksichtigen - Menschen."
      ],
      [
        "Wir werden als Menschen etwas durch den Wissenschafts- betrieb.",
        "Wir können aus unserem Bewußtsein herausstrei- chen die Begriffe über die menschliche Wesenheit, aber wir können uns doch nicht in Wahrheit in den Hintergründen gewissermaßen entmenschen innerhalb der Wissenschaft."
      ],
      [
        "Wir müssen zum menschlichen Wesen vordringen.",
        "Das können wir nicht, wenn wir uns diejenigen Schranken und Grenzen setzen, von denen heute in der landläufigen Wis- senschaft gesprochen wird, und die auch im praktischen Wissenschaftsbetrieb gefordert werden."
      ],
      [
        "Wir werden zu- rückgeworfen, so daß wir Fähigkeiten verlieren.",
        "Wenn man die Muskeln einer Hand nicht gebraucht, so werden sie schwach.",
        "Wenn man gewisse Fähigkeiten nicht ge- braucht, weil man sich einbildet, Grenzen seien da und die Fähigkeiten dürften nicht angewandt werden, weil sie sonst die Grenzen überschreiten, so verliert man diese Fähigkeiten."
      ],
      [
        "Nun, meine sehr verehrten Anwesenden, aus dem, was Ihnen hier in diesen acht Tagen vorgeführt worden ist, werden Sie ersehen haben, welch ein Zusammenhang be- steht zwischen der Entwickelung dieser Fähigkeiten, die sich nicht an die gewöhnlich angenommenen Grenzen der Natur binden, und demjenigen, was in der Natur draußen lebt, selber.",
        "Dasjenige nämlich, was immer nur hin will bis an die Grenze der Sinneswelt in der äußeren Natur, das kann nicht entfalten jene Kräfte, welche unter die Oberfläche des Sinneswesens hinunterführen und aus dem heraus auch etwas für das menschliche Leben gewonnen werden muß."
      ],
      [
        "Auf dieses, was da gewonnen werden muß, deutet Goethe hin in seinem so bedeutungsvollen, ich möchte sa- gen, gewichtigen Ausspruche: «Wem die Natur ihr offen- bares Geheimnis zu enthüllen anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer würdigsten Aus- legerin, der Kunst.» Hier haben wir den Weg, wo das- jenige, was lebendiges Wissen ist, nicht das Künstlerische abtötet, sondern direkt hineinführt in das Künstlerische.",
        "Als die letzten Hochschulkurse im Herbst hier gehalten worden sind, wies ich darauf hin, wie durch dasjenige, was hier gesagt wird, gefunden werden soll, was in ur- alten Zeiten der Menschheit instinktiv vorhanden war: ein Vereinen von Wissenschaft, Kunst und Religion."
      ],
      [
        "Das wird gefunden.",
        "Denn wenn man nicht sich selber die Fä- higkeiten abschneidet, ablähmt dadurch, daß man wissen- schaftlich «Grenzen des Naturerkennens» annimmt, dann wird man bemerken, wie man allmählich das, was man an der Natur begreift an Bildungsgesetzen, übergehen las- sen muß in das, was aus diesem Begreifen der Bildungs- gesetze von selber sich künstlerisch gestaltet."
      ],
      [
        "Man kann die menschliche Gestalt, die auch aus der Natur heraus gebildet ist, nicht verstehen, wenn man nicht in der eige- nen Erkenntnis umwandelt, was sonst nur allgemeine Re- geln sind, in künstlerische Anschauung.",
        "Wenn dann die Leute kommen und einem sagen: Ja, aber eine Analyse des Erkenntnisvermögens ergibt, daß wir nicht über die Logik hinausgehen dürfen in der Erkenntnis, sondern daß wir alles mit den abstrakten logischen Regeln erfassen müssen, und mit der Beobachtung, mit dem Experiment , dann 235 muß man ihnen erwidern: Aber eine Einsicht, eine geistes- wissenschaftliche Einsicht in die Tatsachen der Welt zeigt etwas anderes. - Die zeigt, daß wir lange reden können, wie Erkenntnis sein muß, wie wir die Erkenntnis gestalten müssen; die Natur aber, sie ergibt sich nicht solchen Er- kenntnissen."
      ],
      [
        "Denn sie schafft selber künstlerisch, und sie will von einem bestimmten Punkte an künstlerisch auf- gefaßt sein.",
        "Es gibt einen kontinuierlichen Weg von Wissenschaft in Kunst hinein.",
        "Und die Brücke ist keine unnatürliche, die Brücke ist eine selbstverständliche."
      ],
      [
        "Und der andere Weg soll über die Grenzen hinwegführen, welche im Inneren des Menschen aufgerichtet werden.",
        "Angedeutet wurde es im Laufe dieser Woche, daß man nicht zu irgendeiner nebulosen, schwammigen mystischen Tiefe kommt, son- dern daß man zu einer klaren Erkenntnis der menschlichen Organisation kommt."
      ],
      [
        "Aber man kommt, indem man die- sen anderen Weg geht - Geisteswissenschaft zeigt das, in- dem sie auf diesem anderen Weg auch wiederum zu Erkenntnissen aufsteigt -, zu etwas, was man nun aus- sprechen möchte mit einem dem eben zitierten Goetheschen Wort ähnlichen Wort.",
        "Goethe sagt: «Wem die Natur ihr offenbares Geheimnis zu enthüllen anfängt, der empfindet eine unwiderstehliche Sehnsucht nach ihrer würdigsten Auslegerin, der Kunst.» Mit Rücksicht auf dasjenige, was man nach innengehend wirklich erkennen kann, wenn man wissenschaftliche Gedankenwahrheit entwickelt, kann man sagen: Wem das menschliche Innere sein geheimnis- volles Wesen zu offenbaren beginnt, der empfindet eine tiefe Sehnsucht nach dem würdigsten sich daranschließen- den Gefühl der religiösen Verehrung des schöpferischen Daseins."
      ],
      [
        "Und so finden wir nach außen in die Natur hinein- 236 schreitend den Weg zur Kunst, nach innen in den Men- schen hineinschreitend durch Erkenntnis den Weg zur Religion.",
        "Was sich spezialisiert hat in diesen drei Gebie- ten, in der menschlichen Seele muß es doch einheitlich zu- sammenwirken."
      ],
      [
        "Es muß gefunden werden die Möglichkeit dieses einheitlichen Zusammenwirkens.",
        "Wird also die Er- kenntnis wiederum fähig gemacht, unterzutauchen in die Geheimnisse der Dinge, was, wie Sie gesehen haben, in diesen acht Tagen hier angestrebt wurde, dann wird sie erst herantreten können an das, was aus der menschlichen Wesenheit herausquillt: die soziale Frage."
      ],
      [
        "Hier werden - weil der Mensch die äußere Verkörperung eines Geistig- Seelischen ist - helfen müssen die Impulse, die wir aus einer Erkenntnis des Geistig-Seelischen gewinnen können.",
        "Die so brennende, drängende soziale Frage, die uns so zu Herzen gehen muß heute, insbesondere, wenn wir der heutigen Jugend angehören, sie wird, soweit sie bewältigt werden muß, nur bewältigt werden können, wenn wir gewissermaßen in das Objekt der sozialen Frage, in den denkenden, fühlenden, begehrenden, nach einem men- schenwürdigen Dasein drängenden Menschen den Weg finden."
      ],
      [
        "Daß Geisteswissenschaft nach dieser Richtung hin bestrebt ist, das gehört zu ihrem Wesen.",
        "Und wenn man einsieht, was sie über den Menschen zu sagen hat, dann wird man nicht mehr sagen können: Eine ethische, ästhetische, politische oder kulturelle Wertung des sozialen Prozesses liege dem Ziele einer solchen Studie fern."
      ],
      [
        "Ob dieser Prozeß Geschwüre heile oder Sonnen ver- lösche, sei vom Standpunkte der Wissenschaft aus völlig gleichgültig.",
        "Es fehlt nur noch, daß man sagt: Medizin habe die Aufgabe, den menschlichen Organismus zu er- kennen; ob es der Medizin auch gelinge, Kranke zu heilen, sei vom Standpunkte der Wissenschaft aus völlig gleich- 237 gültig. - Die Denkweise, die in solchen Sätzen lebt wie dem erst angeführten, und die Denkweise in einem sol- chen absurden Satz, den ich Ihnen eben jetzt angeführt habe, ist im Grunde genommen eine und dieselbe."
      ],
      [
        "Wir sind so weit gekommen, daß man Absurditäten als solche nicht mehr erkennt, wenn sie sich in landläufige wissen- schaftliche Formeln kleiden, wenn sie von Autoritäten ge- formt in die Menge hinaustönen.",
        "Das ist es, was uns hier im Goetheanum die Zunge löst, daß wir sprechen müssen."
      ],
      [
        "Wir können nicht anders - und wenn es noch so viele Feinde und Gegnerschaften gäbe -, als zusammenarbeiten in einer solchen Richtung auch mit der Studentenschaft.",
        "Wir wissen, was es heißt, Student zu sein."
      ],
      [
        "Das heißt, in seinem Herzen zu tragen, was als Kraft hinüberfließen muß in die Zukunft.",
        "Ja, diese Zukunft, die jetzt die Menschheit erwartet, sie wird kraftvolle Seelen brauchen, in deren Wille und Emotionen hineinspielt eine klare Ein- sicht in Weltwesen und Menschenleben."
      ],
      [
        "Weil wir wissen, daß Sie so etwas brauchen werden, deshalb sprechen wir zu Ihnen, insofern Sie uns mit Verständnis entgegenkom- men wollen.",
        "Wir haben Sie wahrhaftig mit hierher geru- fen - obwohl wir Sie alle, wie Sie mir glauben können, persönlich sehr gerne sehen -, wir haben Sie mit hierher gerufen, weil wir hoffen, daß Sie Mitarbeiter werden auf einem Wege, den wir als einen notwendigen für die Ge- genwart und für die nächste Zukunft ansehen, und weil wir die Probe machen wollen - und wir werden sie immer mehr und mehr machen, ich hoffe, sie wird sich trotz aller Widerstände machen lassen , weil wir die Probe darauf- hin machen wollten, wie viele sich finden können, in deren Herzen das ein Echo findet, was wir glauben als eine Not- wendigkeit dieser unserer Zeit zu erhärten. 238 Wir müssen uns nun wiederum trennen, meine sehr ver- ehrten Kursbesucher."
      ],
      [
        "Allein ich glaube, in einem können wir beisammen sein, beisammen bleiben, trotz aller Rau- mesentfernung beisammen bleiben: in der Erkenntnis, daß nach der Richtung, die hier angedeutet wurde, doch fort- geschritten werden müsse, daß gearbeitet werden müsse, daß Wille in dieser Richtung entwickelt werden müsse, so- viel jeder nur kann.",
        "Er wird, wenn er die nötige Einsicht gewinnt, diesen Willen entwickeln."
      ],
      [
        "Wir sind heute noch nicht in der Lage - das spreche ich zu Ihnen, meine lieben Kommilitonen -, das, was wir Ihnen hier bieten können, zum Abschlüsse dadurch zu bringen, daß wir Ihnen Abschlußprüfungen ermöglichen, die Ihnen Lebensstellungen geben.",
        "Wir sind in dieser Be- ziehung arme Leute, die lediglich an das appellieren kön- nen, was als Wahrheitssinn, als Erkenntnisenthusiasmus in Menschenseelen und Menschenherzen waltet."
      ],
      [
        "Wir kön- nen uns nur der Hoffnung hingeben, daß neben alledem, was in ungesunder Weise in die Prüfungen und Lebens- stellen hineinläuft, auch noch in einer genügend großen Anzahl Jugend sich Herzen und Seelen finden, die hin- wollen zu der Wahrheit, um der Wahrheit willen zu dem, wovon man glauben kann, daß es nach den Zeichen dieser Zeit notwendig sei, um dieser rein menschlichen Notwen- digkeit willen.",
        "Wir glauben, daß noch so viel freies Ge- fühl vorhanden ist, daß aus diesem reinen Freiheitsdrang heraus diese beiden Bestrebungen entstehen können."
      ],
      [
        "Weil wir dieses glauben müssen, stehen wir, die wir diese Vorträge gehalten, diese Veranstaltungen gemacht haben im Laufe der letzten Woche, stehen wir alle hier, Ihnen, die Sie nun wieder zurückkehren in das übrige Leben, ein Lebewohl zuzurufen.",
        "Aber wir stehen hier, hoffend darauf, daß Sie unsere Helfer sein werden, Sie 239 begleitend mit den Gedanken, die wir gemeinsam durch unsere Seelen haben ziehen lassen, Sie begleitend mit den besten Wünschen dazu, daß Ihr Wille zur Klarheit, Ihr Wille zum entsprechenden Tun stark sei."
      ],
      [
        "In dieser Hoff- nung und mit diesen Wünschen trennen wir uns, um uns hoffentlich wiederzusehen, und sagen Ihnen von dieser Stätte aus ein herzliches Lebewohl und auf Wiedersehen! 240"
      ]
    ]
  },
  {
    "order": 11,
    "title_de": "Hinweise",
    "paragraphs": [
      "Von vielen Seiten wurde an die Veranstalter des Ersten anthroposo- phischen Hochschulkurses, der vom 26. September bis 16. Oktober 1920 am Goetheanum stattgefunden hat, das Verlangen gerichtet, die Kurse schon vor der eigentlichen Eröffnung des Goetheanums fortzu- setzen.",
      "So erging die Einladung zum Zweiten anthroposophischen Hochschulkursus vom 3. bis 10. April 1921 an der Freien Hoch- schule für Geisteswissenschaft Goetheanum in Dornach. Als Veran- stalter zeichneten der auf Anregung Rudolf Steiners von Roman Boos und zwei Freunden gegründete «Verein Goetheanismus» und der «Bund für anthroposophische Hochschularbeit».",
      "Am Gesamtkurs waren 600 Teilnehmer ständig anwesend. Die Vormittagsvorträge waren jedermann zugänglich. Im Mittelpunkt standen die fünf in diesem Band enthaltenen Vorträge von Dr. Rudolf Steiner, unter dem Titel «Anthroposophie und Fachwissenschaften».",
      "Anschließend daran sprachen zwölf Vortragende über ihr wissenschaftliches Arbeitsgebiet, und in mehreren Disputationen wurden in Frage und Antwort von Rudolf Steiner weitere Klärungen erarbeitet. Der vorliegende Band enthält außer der Eröffnungs- und Schluß- rede von Rudolf Steiner die fünf Vorträge zum Hauptthema sowie die dazugehörigen Beiträge Steiners zu den Disputationen, schließlich auch das Schlußwort Rudolf Steiners zu einer Studentenversammlung.",
      "Die während des Kurses zusätzlich gebotenen Vorträge Rudolf Stei- ners sind in die folgenden Bände der Gesamtausgabe aufgenommen worden: «Urrhythmus, Urgesang und Arrhythmus in ihrem Verhält- nis zur Eurythmie» vom 9. April 1921 in «Eurythmie.",
      "Die Offen- barung der sprechenden Seele» (Bibl.-Nr. 277, Dornach 1972); «Die Kunst des mündlichen Vortrages» vom 6. April 1921 in «Die Kunst der Rezitation und Deklamation» (Bibl.-Nr. 281, Dornach 1967); «Die Psychologie der Künste» vom 9.",
      "April 1921 in «Kunst und Kunsterkenntnis. Das Sinnlich-Übersinnliche in seiner Verwirklichung durch die Kunst» (Bibl.-Nr. 271, Dornach 1961); «Die menschliche Sprache und der Logos» vom 9. April 1921 geplant in «Perspektiven der Menschheitsentwicklung» (Bibl.-Nr. 204).",
      "In dieser Auflage sind zum großen Teil die Hinweise von Roman Boos für die 1. Ausgabe, teilweise gekürzt, übernommen worden. Einige Ergänzungen waren erforderlich. Die acht im Rahmen des Ersten Hochschulkurses vom 26.",
      "Septem- ber bis 16. Oktober 1920 gehaltenen Vorträge Rudolf Steiners über «Grenzen der Naturkenntnis» liegen seit 1969 als Band 322 der Gesamtausgabe vor. 241 zu Seite 13 das alte Kantische Wort: Wörtlich: «Ich mußte also das Wissen aufheben, um zum Glauben Platz zu bekommen», Kant, «Kritik der reinen Vernunft», Vorrede zur 2.",
      "Auflage. 16 Emil Du Bois-Reymond: «Über die Grenzen des Naturerken- nens. Ein Vortrag, gehalten in der zweiten allgemeinen Sitzung der 45. Versammlung Deutscher Naturforscher und Ärzte zu Leipzig am 14. August 1872», Leipzig 1872, S. 12.",
      "Der Vor- trag endet mit dem bekannten «Ignorabimus». 23 die umgestalteten Worte des Hilarius: Vgl. die Gegenüberstel- lung der beiden Reden bei Febe Colazza in «Heute und hier», Dornach 1952. 26 Ludwig Haller: Das Buch (Berlin 1888) ist der Torso eines be- absichtigten Systems der Philosophie in mehreren Bänden. Der Verfasser war 1890 schon verstorben. 28 Immanuel Kant, 1724-1804. 28/29 «pseudodialektische ...",
      "Charakter dieser Misosophie ...»: Siehe Haller a. a. S. 241. 29«Ich, der ich von Gott...»: Siehe Haller, a. a. S. 244. 30Eduard von Hartmann, 1842-1906. «Kritische Wanderungen durch die Philosophie der Gegenwart», Leipzig 1890, VI.",
      "Aufsatz: Eine neue dialektische Form der Mystik, S. 105 (1. Hallers Standpunkt im Allgemeinen; 2. Hallers Dialektik und sein Kampf gegen die Prioritäten; 3. Hallers Mystik). 32 ... lebendig gewordenen Begriffe: Siehe von Hartmann, a.a.O.",
      "S. 156: «Auf die Gefahr hin, von Haller für einen erklärt zu werden (S. 428), muß ich bekennen, daß ich keine Erfahrung über solche irrationale nek- kische Launen der Worte und Begriffe habe, und daß der Schein gegenteiliger Erfahrungen nach meiner Ansicht nur entweder aus einer molluskenhaften Haltlosigkeit und nichtsnutzigen Schlottrigkeit des Denkens oder aus einer auf irrationale Resul- tate gerichteten Tendenz des Denkens stammt.» ... sehr bedeutend gefunden: Siehe von Hartmann, a. a. S. 142 ff.",
      "Rudolf Steiner, «DieDie Rätsel der Philosophie in ihrer Geschichte als Umriß dargestellt», Berlin 1914, Bibl.-Nr. 18, Gesamtaus- gabe Dornach 1968 (auch als Taschenbuchausgaben tb 610/611 [Dornach 1974] erschienen). 242 33John Locke, 1632-1704. 34Thomas von Aquino, 1225-1274. Siehe Rudolf Steiner, «Die Philosophie des Thomas von Aquino», Bibl.-Nr. 74, Gesamt- ausgabe Dornach 1967 (auch als Taschenbuch tb 605 [Dornach 1972] erschienen). 35Gottfried Wilhelm Leibniz, 1646-1716.",
      "Christian Freiherr von Wolff, 1679-1754. 36Buch von Wolff: «Vernünftige Gedanken von Gott, der Welt und der Seele des Menschen, auch allen Dingen überhaupt», Frankfurt und Leipzig 1719. 37David Hume, 17111776. 38Rudolf Steiner, «Wahrheit und Wissenschaft». Vorspiel einer «Philosophie der Freiheit», 1892.",
      "Bibl.-Nr. 3, Gesamtaus- gabe Dornach 1958. Rudolf Steiner, «Die Philosophie der Freiheit». Grundzüge einer modernen Weltanschauung. 1894. Bibl.-Nr. 4, Gesamtaus- gabe Dornach 1973. 40 daß die Phänomene, die Erscheinungen rein sich selbst aus- sprechen: «Man erkundige sich ums Phänomen, nehme es so genau damit als möglich und sehe, wie weit man in der Einsicht und in praktischer Anwendung damit kommen kann, und lasse das Problem ruhig liegen.",
      "Umgekehrt handeln die Physiker: sie gehen gerade aufs Problem los und verwickeln sich unter- wegs in so viel Schwierigkeiten, daß ihnen zuletzt jede Aussicht verschwindet.» Aus «Goethes Naturwissenschaftliche Schriften», herausgegeben und eingeleitet von Rudolf Steiner in «Kürsch- ners Deutsche National-Litteratur» (1883-1894), Band V «Sprüche in Prosa», S. 417 (Bibl.-Nr. ia-e, Nachdruck in fünf Bänden, Dornach 1975). Phänomenalismus Goethes: «Das Höchste wäre, zu begreifen, daß alles Faktische schon Theorie ist.",
      "Die Bläue des Himmels offenbart uns das Grundgesetz der Chromatik. Man suche nur nichts hinter den Phänomenen; sie selbst sind die Lehre.» «Kein Phänomen erklärt sich an und aus sich selbst; nur viele zusammen überschaut, methodisch geordnet, geben zuletzt etwas, was für Theorie gelten könnte.» Aus «Goethes Naturwissen- schaftliche Schriften», Band V «Sprüche in Prosa», S. 376 und 375- 243 40Cartesius: Rene Descartes, 1596-1650. 41in der Neuauflage meiner «Philosophie der Freiheit»; Im «Zusatz zur Neuauflage» zum III.",
      "Kapitel. 42der gütige Gott habe ihn davor bewahrt, «über das Denken zu denken»; Goethe, «Zahme Xenien», VII: «Wie hast du's denn so weit gebracht? / Sie sagen, du habest es gut vollbracht!» Mein Kind! ich hab' es klug gemacht: / Ich habe nie über das Denken gedacht. 47 Disputationen: Im Einladungsprospekt zum Hochschulkurs waren für die Abendstunden angezeigt: «Anregende soziale - wissenschaftliche - künstlerische Disputationen mit kleinen Pikanterien dazwischen.» Rudolf Steiner selbst hatte die Anre- gung gegeben, die «kleinen Pikanterien dazwischen» im Pro- gramm anzuzeigen. Diese Ankündigung weckte bei guten Seelen etliche humorlose Empörung.",
      "Zur Beschwichtigung der Wellen fügte nun Rudolf Steiner seinem Vortrag vom 1. April 1921 (zwei Tage vor der Eröffnung des Kurses) die folgenden erläuternden Worte an: «Meine lieben Freunde, ich möchte jetzt nur noch ein paar Worte über etwas anderes, etwas ganz anderes sagen.",
      "Ich habe ver- nommen, daß eine gewisse Ängstlichkeit herrscht - in den Krei- sen, welche die Verantwortung für die Sache haben -, eine ge- wisse Ängstlichkeit mit Bezug auf den Punkt in unserem Kurs- programm, wo viel ernste soziale und sonstige Unterhaltungen für die Abende vorgesehen sind und die Rede ist von den «klei- nen Pikanterien». Ich war etwas frappiert über diese Ängst- lichkeit, nachdem so oftmals hier davon gesprochen worden ist, daß nur vom seelischen Zusammenwirken aller derjenigen, die sich zur anthroposophischen Bewegung zählen, das Heil dieser Bewegung kommen kann.",
      "Ich war deshalb frappiert, weil ich ge- glaubt habe - da hier so oft dies betont worden ist -, daß we- nigstens mit Bezug auf diese Eigenschaften des Funkensprühen- lassens aus alldem heraus, was man als Geistreichigkeit auf seiner Seele trägt, längst jeder die Seelenvorbereitung an sich getrof- fen hat; und ich habe eigentlich gemeint, daß wir gar kein Ende gerade dieser Abende werden finden können, wo dasje- nige, was individuell an Geistreichigkeit in den Seelen seit lange sich aufgespeichert hat, sich in ganzen Feuergarben von Pikanterien - in noblerem Sinne Pikanterien! - entladen werde! Ich hoffe das auch heute noch, möchte aber doch eben bemer- ken, daß das nicht etwa darinnen bestehen kann, daß man 244 programmäßig etwa so einen nach dem anderen aufs Podium hinaufschickt, daß er Pikanterien losläßt!",
      "Das würde meiner Meinung nach in bezug auf diesen Programmpunkt nicht das Richtige sein. Sondern da muß jeder schon so anspruchslos sein, daß er vielleicht nur zu einem ganz kleinen Kreise der Umge- bung, den er grad in einem Momente trifft, solches Feuersprühen losläßt, so daß diese dann sehen müssen, wie sie feurig sein können.",
      "Es kann manches mit Lachen, es kann aber auch man- ches mit anderen Gefühlsimpulsen, die sich als notwendige Folge ergeben können, gesagt werden. «Pikanterien», das müssen ja nicht bloß Lustigkeiten sein, das können auch andere Dinge sein!",
      "Und so habe ich mir vorgestellt, daß das wirklich von Mensch zu Mensch sich entwickeln werde. Es hat sich ja, was so im per- sönlichen Umgange von Mensch zu Mensch sich abspielt, das letztemal bei dem Kurs (beim i.",
      "Hochschulkurs, Herbst 1920) so wenig gezeigt, daß man denken kann: Es hat sich da eben im stillen vieles aufgespeichert, was jetzt losgelassen werden soll! Aber ich stelle mir das gewissermaßen so vor, daß in diesen paar Tagen - es sind ja nur noch zwei! - jeder mit sich zu Rate geht und nun tief in seine Seele hineinschaut, was er an solchen «Pikanterie» möglichkeiten in seiner Seele trägt, so daß er dann herumgehen kann von einer Gruppe zur anderen, und daß da die Dinge an jedem Abend außerordentlich anregend verlaufen können.",
      "Es wird ja doch nicht fehlen, daß da ein gewisses soziales Leben auf diese Weise sich entspinnt. Es ist nicht notwendig, daß wir uns nur immer auf unsere Sitze setzen und auf unseren Sitzen etwas anhören wollen; denn wenn das jeder tun würde denken Sie, wozu wir dann kommen würden!",
      "Das geht doch nicht, nicht wahr! Es würde ja keinen Sinn haben, von einer «Gesellschaft» zu sprechen, wenn nicht in dieser Weise auch gesellschaftsmäßig etwas auftreten würde. Also, wie gesagt, ich möchte nicht den Anregungen folgen, geradezu eine Anleitung zu der Sache zu geben, sondern ich möchte nur meine Meinung dahin aussprechen, daß nur gesagt zu werden braucht, daß man nicht zurückhalten soll mit sol- chen Dingen; dann werden sie sich ja hoffentlich schon ent- wickeln.",
      "Also hoffen wir, wir werden das Allerbeste auch in dieser Beziehung sehen in den nächsten zehn Tagen!» Tatsächlich waren die Abenddisputationen dann teilweise auch recht munter. Die erste der Disputationen fand Montag, 4.",
      "April, 20 Uhr, im Anschluß an Vorträge von Dr. Stein «Über das Wertproblem» und Dr. Carl Unger über «Das philosophische Bewußtsein und die Erforschung des Übersinnlichen» und seminaristische Übungen zu diesem Thema, statt.",
      "Stenographisch festgehalten wurde nur das Schlußwort Rudolf Steiners. 53innerhalb der Kategorientafel: Weder in den zehn (später acht) Kategorien des Aristoteles noch in den zwölf Kategorien Kants kommen «Subjekt» und «Objekt» vor. Erst der Kantianer Reinhold (1758-1823) hat sie in seinem «Satz des Bewußtseins» zu Stammbegriffen, zu unableitbaren Urformen unseres Den- kens, eben zu «Kategorien» befördert, in welcher Rolle sie seither besonders alles populär-philosophische Treiben durch- wuchern. 54Antipoden Kants: «Hier (bei Kant) liegt überhaupt... etwas Falsches verborgen, das mir daher zu kommen scheint, weil er das subjektive Erkenntnisvermögen nun selbst als Objekt be- trachtet und den Punkt, wo subjektiv und objektiv zusammen- treffen, zwar scharf aber nicht ganz richtig sondert» (Goethe, Weimarer Ausgabe, 2.",
      "Abt., Bd. XI, S. 376). 55Franz Brentano, 1838-1917. 56Der Brentano-Schüler: Siehe Oskar Kraus, «Franz Brentano», München 1919, S. i, 21. 57wie ich es beute morgen: Im Vortrag über «Philosophie»; siehe oben zu S. 26 ff. intentionales Innesein: Mit seinem Begriff des «intentionalen Inneseins» knüpft Brentano an die von Thomas von Aquino im Anschluß an Aristoteles entfaltete Lehre von den Sinnes- qualitäten an.",
      "Vgl. auch Rudolf Steiner, «Von Seelenrätseln», Anhang 5: «Über die wirkliche Grundlage der intentionalen Beziehung», Bibl.-Nr. 21, Gesamtausgabe Dornach 1976. Johannes Müller, 1801-1858, Physiologe und vergleichender Anatom. 61 Fritz Mauthner, 1849-1923, Schriftsteller und Sprachforscher.",
      "Siehe den Artikel «Mathematische Naturerklärung» in seinem «Wörterbuch der Philosophie». Vergleiche auch Rudolf Steiner über Fritz Mauthner, in «Zufall, Notwendigkeit und Vorsehung», Bibl.-Nr. 163, Gesamtausgabe Dornach 1975. die gewollte Finsternis des Erkennens, wie sie sich bei Fritz Mauthner findet: Die «gewollte Finsternis des Erkennens» kommt beispielsweise zum Ausdruck in der «Einleitung» zum 246 «Wörterbuch der Philosophie»: «Ich werde froh sein, wenn ein ganz guter Leser am Ende des Weges sich sagen muß: die skeptische Resignation, die Einsidit in die Unerkennbarkeit der Wirklichkeitswelt, ist keine bloße Negation, ist unser bestes Wissen; die Philosophie ist Erkenntnistheorie, Erkenntnistheorie ist Sprachkritik; Sprachkritik aber ist die Arbeit an dem be- freienden Gedanken, daß die Menschen mit den Wörtern ihrer Sprachen und mit den Worten ihrer Philosophien niemals über die bildliche Darstellung der Welt hinausgelangen.» 61Ausspruch Kants: «Ich behaupte, daß in jeder besonderen Naturlehre nur so viel eigentliche Wissenschaft angetroffen werden könne, als darin Mathematik anzutreffen ist.» (Vor- rede zu der 1786 veröffentlichten Schrift «Metaphysische An- fangsgründe der Naturwissenschaft».) 62Cartesius: Siehe Hinweis zu S. 40.",
      "Buchenau zitiert in seinem Kommentar zu den «Meditationen über die Grundlagen der Philosophie» von Descartes (Leipzig, Meiner) aus den Schriften Descartes' u. a. folgende Aussprüche: «...Nach meiner An- sicht geschieht alles in der Natur auf mathematische Art... Was die Physik betrifft, so würde ich vermeinen, von ihr nichts zu wissen, wenn ich nur zu sagen wüßte, wie die Dinge sich verhalten können, ohne zu beweisen, daß sie nicht anders sein können; denn da ich sie auf Mathematik zurückgeführt habe, so ist dies eine mögliche Anschauung...» «... ich rühme mich, daß ich mich einer solchen Art zu philosophieren bediene, wobei kein Grund zugelassen wird, der nicht mathematisch und evident ist und wobei die Schlußfolgerungen durch unzweifelhafte Er- fahrungen bestätigt werden » Benedictus Spinoza, 1632-1677.",
      "Die einzige Schrift, die Spinoza mit voller Nennung seines Namens herausgegeben hat, trägt den Titel «Descartes' Prinzipien der Philosophie auf geometri- sche Weise begründet». Auch sein eigentliches Lebenswerk, die «Ethik», trägt den Untertitel «nach geometrischer Methode dargestellt». 63 das Wort «Mathematik»; «Mathesis» (von «manthano», lernen) heißt ursprünglich «das Lernen», dann «die Erkenntnis» und «der Unterricht». 65 Adrien Legendre, 17521833, französischer Mathematiker.",
      "Farkas (Wolfgang) Bolyai, 17751856, ungarischer Mathema- tiker, und sein Sohn Johann Bolyai, 1802-1860. 247 65 Nikolai Lobatschewskij, 1793-1856, russischer Mathematiker. 67 Behandlung der «Farbenlehre»; Siehe Hinweis zu S. 109. Goethe ... wollte auch das Qualitative einbezogen haben: «Der Mathematiker ist angewiesen aufs Quantitative, auf alles, was sich durch Zahl und Maß bestimmen läßt, und also gewisser- maßen auf das äußerlich erkennbare Universum.",
      "Betrachten wir aber dieses, insofern uns Fähigkeit gegeben ist, mit vollem Geiste und aus allen Kräften, so erkennen wir, daß Quantität und Qualität als die zwei Pole des erscheinenden Daseins gelten müssen ...» Aus «Goethes Naturwissenschaftliche Schriften», Band V, «Sprüche in Prosa», S. 406. 84 Zweite Disputation: Dienstag, 5. April 1921, sprachen nach Rudolf Steiner («Mathematik und anorganische Naturwissen- schaften») Dr.",
      "Hermann von Baravalle («Raum und Zeit») und Dr. Ernst Blümel («Geisteswissenschaftliche Richtlinien zur mathematischen Behandlung naturwissenschaftlicher Probleme»). Die Abenddisputation hielt sich nicht ans Thema des Tages. (Dieses wurde zwei Tage später aufgegriffen.) Deutsche Stu- denten brachten ihre Nöte zur Sprache.",
      "So klagte ein Student aus Bonn den Universitätsbetrieb an, «aus einem falschen Grundmotiv heraus mit verkehrten Methoden an der Jugend zu arbeiten»; es könne passieren, daß man beim einen Dozen- ten das Gegenteil von dem zu hören bekomme, was der andre sage; die Wissenschaft werde «um ihrer selbst willen» getrie- ben, nicht «um der Menschen willen»; wer Philosophie studiere, müsse sich «der Philosophie hinopfern, absterben als Mensch» - um das Examen bestehen zu können; viele seiner Freunde sagten, daß «sie sich an der Hochschule als Mensch nicht retten könnten». Als der Artikel «Ethische Irrlehren» von Prof.",
      "Rein, Jena («Der Tag» vom 23. November 1920), der eine scharf ablehnende Besprechung der Neuauflage der «Philosophie der Freiheit» enthielt, erwähnt und dem Verfasser vorgeworfen wurde, er habe diese Rezension unter dem Druck der damals gegen Rudolf Steiner stark aufgehetzten «öffentlichen Mei- nung» geschrieben, meldete sich ein Student aus Jena: Professor Rein sei sein Schwiegervater; die «Philosophie der Freiheit» sei ihm von einem führenden Mitgliede der Anthroposophischen Gesellschaft in Jena zugestellt worden; die «öffentliche Mei- nung» spiele nicht herein. - Nach langem, sehr temperament- vollem Hin und Her ergriff Rudolf Steiner das Wort.",
      "Wilhelm Rein, 1847-1921. eine der ersten Besprechungen: Diese Besprechung der «Philo- 248 sophie der Freiheit» durch Robert Zimmermann (1824-1898) konnte bisher nicht aufgefunden werden. 87/88 eine Ethik für Anthroposophen: Die nachfolgenden Sätze Reins lauten: «Diese freien Menschen des Dr. Steiner sind aber bereits keine Menschen mehr.",
      "Sie sind in die Welt der Engel schon auf Erden eingetreten. Die Anthroposophie hat ihnen dazu verhel- fen. Müßte es nicht eine unsagbare Wohltat mitten in den mannigfachen Wirrnissen des Erdenlebens sein, sich in solche Umgebung versetzen zu lassen?» und so weiter. 91Waldorfschule: Aus der Ansprache Rudolf Steiners bei der Eröffnung der «Freien Waldorfschule» am 7.",
      "September 1919: «Jedenfalls soll diese Waldorfschule nicht eine Weltanschau- ungsschule werden. Derjenige, der da sagen wird: die anthropo- sophisch orientierte Geisteswissenschaft gründe die Waldorf- schule und wolle ihre Weltanschauung hineintragen in diese Schule - ich sage das jetzt am Eröffnungstage! -, der wird nicht die Wahrheit sprechen...» Siehe «Rudolf Steiner in der Wal- dorfschule», Ansprachen für Kinder, Eltern und Lehrer 19191924, Bibl.-Nr. 298, Gesamtausgabe, Stuttgart 1958. 92Weltschulverein: Der «Weltschulverein» sollte der organisa- torisch-ökonomische Träger des über alle nationalen Grenzen hinweg sich sammelnden Willens zur Befreiung der Schulen aus den staatlich-politischen Fesselungen sein.",
      "Am 12. Oktober 1920 rief Rudolf Steiner in einem Vortrag über die Grund- probleme der sozialen Struktur - die wahrhaft internationale Zuhörerschaft des ersten Hochschulkurses zum Schluß dazu auf, die Begeisterung, die reichlich vorhanden war, in Tatkraft zu verdichten.",
      "Aber es blieb bei Gefühlen und Worten der Begei- sterung. Zu Taten kam es nicht. unserer letzten Hochschulkurse: Erster anthroposophischer Hochschulkurs vom 27. September bis 16. Oktober 1920, siehe «Grenzen der Naturerkenntnis», Bibl.-Nr. 322, Gesamtaus- gabe Dornach 1969. 94 Sie könnten das schon seit einigen Tagen tun: Am i.",
      "April 1921 war in England der neue Bergarbeiterstreik ausgebrochen. Er zwang die Regierung den «state of emergency» (Zustand drohender Not) zu verkünden, sofort die Einschränkung des Kohlenverbrauchs und das Verbot der Kohlenausfuhr zu ver- fügen und das Ober- und Unterhaus auf den 4.",
      "April einzube- rufen. Der Streik dauerte dann ein volles Vierteljahr. Zahl- 249 reiche Gruben gerieten unter Wasser wegen Nichtbedienung der Pumpen. 97 Phoronomie: Vgl. dazu die Ausführungen Rudolf Steiners in «Geisteswissenschaftliche Impulse zur Enrwickelung der Physik.",
      "Erster Naturwissenschaftlicher Kurs», Bibl.-Nr. 320, Gesamt- ausgabe Dornach 1964 (10. Vortrag). 99 in meinen . . . «Einleitungen zu Goethes Naturwissenschaftlichen Schriften»: In «Kürschners Deutsche National-Litteratur» Bände 114-117, 1883-1897; siehe Rudolf Steiner, «Goethes Naturwissenschaftliche Schriften.",
      "Einleitungen», Bibl.-Nr. i, Gesamtausgabe Dornach 1973. 100 Johannes Müller, 1801-1858, Begründer der modernen Physio- logie. Ernst Mach, 1838-1916, österreichischer Physiker und Philosoph. Henri Poincare, 1854-1912, Mathematiker, Physiker und Astronom.",
      "Fritz Mauthner: Siehe Hinweis zu S. 61. Das ist die Idee der Lebenskraft: Vgl. Driesch, «Der Vitalismus als Geschichte und als Lehre», Leipzig 1905. Über die «Erfin- dung» der Lebenskraft durch Georg Ernst Stahl im 17., 18.",
      "Jahrhundert vgl. Rudolf Steiner, «Der Entstehungsmoment der Naturwissenschaft in der Weltgeschichte und ihre seitherige Ent- wickelung«, 8. Vortrag, Bibl.-Nr. 326, Gesamtausgabe Dornach 101 die Darstellung eines organischen Stoffes in synthetischer Weise von Wohler und Liebig: 1828 gelang zum ersten Mal Friedrich Wohler, 1800-1882, die künstliche Darstellung einer organischen Substanz.",
      "Er gewann Harnstoff aus zyansaurem Ammonium. Justus von Liebig, 1803-1873. 103 in meinem ersten Vortrag dieser Reihe: Siehe S. 26 ff. 109zum Beispiel in der Farbenlehre und in der Tonlehre: Siehe «Goethes Naturwissenschaftliche Schriften», Bände III-V (Far- benlehre) und Band V, S. 596 ff. (Tonlehre). 110Monere: Von Haeckel konstruiertes, tatsächlich nicht existieren- des einfachstes Lebewesen, das nur aus Protoplasma ohne Kern besteht. 250 110 Ernst Haeckel, 1834-1919. 111 eine Umbildung der Rückenwirbelsäule: Über Goethes «Wirbel- theorie des Schädels» vgl. die Anmerkungen Rudolf Steiners zu S. 316 des i.",
      "Bandes von «Goethes Naturwissenschaftlichen Schriften», siehe Hinweis zu S. 99. 112 daß der Mensch ein älteres Wesen ist: Über das entwicklungs- geschichtliche Verhältnis von Mensch und Tier siehe Rudolf Steiner, «Die Geheimwissenschaft im Umriß», Kapitel «Die Weltentwicklung und der Mensch», Bibl.-Nr. 13, Gesamtausgabe Dornach 1977 (auch als Taschenbuchausgabe tb 601 [Dornach 1976] erschienen). 114 die «psychophysischen Parallelitiker»: G. Lipps gibt in seinem «Grundriß der Psychophysik» (Leipzig 1909) eine Charakteri- sierung des «psychophysischen Parallelismus». 116 Frühlingskurs ... für Ärzte und Medizinstudierende: «Geistes- wissenschaft und Medizin». 20 Vorträge, gehalten von Dr.",
      "Ru- dolf Steiner vor Ärzten und Medizinstudierenden in Dornach vom 21. März bis 9. April 1920; Bibl-Nr. 312, Gesamtausgabe Dornach 1976. 118Oskar Römer, 18661952, Prof. Dr. med. et med. dent. h. c., Direktor der operativen Abteilung des Zahnärztlichen Instituts der Universität Leipzig.",
      "«Über die Zahnkaries mit Beziehung auf die Ergebnisse der Geistesforschung Dr. Rudolf Steiners», Stuttgart 1921. 119Dieser Ausspruch heißt: Zitiert am Kopf des Kapitels «Vokal- wandel» von Wilhelm Scherer, «Zur Geschichte der deutschen Sprache»; 2.",
      "Aufl. Berlin 1890, S. 30. Wilhelm Scherer, 1841-1886, vgl. Rudolf Steiner, «Mein Le- bensgang», Kap. XIV, Bibl.-Nr. 28, Gesamtausgabe Dornach 1962. 127in meinem Büchelchen: «Die Erziehung des Kindes vom Ge- sichtspunkte der Geisteswissenschaft», Dornach 1976. 128die Anhänger des psychophysischen Parallelismus: Siehe Hin- weis zu S. 114. auf das Sie auch gestern aufmerksam gemacht worden sind: Prof.",
      "Römer war ausführlich auf die Ergebnisse der Forschung Rudolf Steiners eingegangen, wonach ein Kind im vorschul- 251 Pflichtigen Alter, das «nicht leicht zu einer geschickten Hand- habung der Hände und Füße zu bringen ist» nicht imstande ist, den Zahnbildungsprozeß - als dessen Ergebnis dann die zweiten Zähne hervorkommen - richtig zu entfalten, aus welchem Grunde «regulierend auf den Zahnprozeß in hohem Maße das wirkt, daß man die Kinder anleitet, und zwar schon möglichst früh, kunstvoll zu laufen, zum Beispiel im Kiebitzschritt und dergleichen, und möglichst früh mit eurythmisch beseelten Frei- übungen beginnt... und noch dafür sorgt, daß die Finger ge- schickt gemacht werden ...» 137gar nicht hineingehört: Siehe Vortrag vom 8. April, S. 169 ff. 138ganz bedeutenden Philologen: Siehe das Zitat von Wilhelm Scherer, S. 119. 139tobte gestern in Stuttgart eine Versammlung: Es handelte sich um eine Agitationsversammlung, in welcher der nationalistische General v.",
      "Gleich das große Wort führte. In der Abenddispu- tation wurde eingehender darüber gesprochen. Siehe S. 164 ff. 142Bernhard Rernhard, 1826-1866, Mitbegründer der Funktionen- theorie. 143Karl Friedrich Gauß, 1777-1855. 144die Kantschen Rattmdefinitionen: Kant verwendet beispiels- weise die Wörter «unendlich» und «unbegrenzt» als gleichbe- deutend im V.",
      "Abschnitt der Ausführungen über «Die Anti- nomie der reinen Vernunft» seiner «Kritik der reinen Ver- nunft», wo er zeigt, daß auf die «Frage wegen der Weltgröße des Raumes» unsere Begriffe eine Antwort nicht geben können: «Denn ist sie (die Weltgröße) unendlich und unbegrenzt, so ist sie für allen möglichen empirischen Begriff zu groß. Ist sie endlich und begrenzt, so fragt ihr mit Recht noch: was bestimmt diese Grenze? ...",
      "Also ist eine begrenzte Welt für euren Begriff zu klein...» Aus dieser «Antinomie» kommt Kant dadurch heraus, daß er dekretiert: «...der Raum (ist) nicht eine Beschaffenheit der Dinge außer mir, sondern eine bloße Vorstellungsart in mir...» («Kritik der Urteilskraft», S. 276 der Originalausgabe). 145die Paralogismenlehre: Im Zusammenhang seiner Lehre von den «Paralogismen» (Trugschlüssen) zieht Kant die Erkenntnis- grenze ausdrücklich mitten durch das Problem der «... Ver- knüpfung ... unseres denkenden Wesens ... mit der Körper- 252 welt...» («Kritik der reinen Vernunft», i.",
      "Aufl., S. 395). Ir- gendwelche Antworten auf dieses Problem können nur «einge- bildeter Wissenschaft» entspringen, und zwar «sowohl in An- sehung dessen, der bejahend, als dessen, der verneinend be- hauptet ...",
      "Nichts als die Nüchternheit einer strengen, aber gerechten Kritik kann von diesem dogmatischen Blendwerke ... befreien...» 146 Euklid, um 300 v. Chr., griechischer Mathematiker, lebte in Alexandria. 153nun liegt eine Frage vor: Diese Frage bezieht sich auf Aus- führungen des Vortragenden am Vorabend vor dem zweiten Hochschulkurs. 154Friedrich Husemann, 1887-1959, Facharzt für Psychiatrie. wie sich aus der Dunkelheit das Blau herausnuanciert: Vgl. dazu Charles von Steiger, «Über die Farbwahrnehmungen des Men- schen in früheren Kulturen und die auf diesem Gebiet gemach- ten Entdeckungen», «Gegenwart», 7.",
      "Jg. 1945 Nr. 6, mit Wort- lauten Rudolf Steiners, speziell über den Zusammenhang zwi- schen der «Verschiebung des Spektrum-Anschauens nach dem dunklen Teile hin» und dem Vorgang, daß sich seit der grie- chischen Kulturepoche «der Denkprozeß verinnerlicht» hat. 159 in einem Vortragskurs genauer ausgeführt: Offensichtlich ver- weist hier Rudolf Steiner auf den 8. Vortrag des Kurses über die Wärmelehre, den er in 14 Vorträgen vom 1.-14.",
      "März 1920 in Stuttgart gehalten hat. «Geisteswissenschaftliche Impulse zur Entwickelung der Physik. Die Wärme auf der Grenze positiver und negativer Materialität», Bibl.-Nr. 321, Gesamtausgabe Dornach 1972. 164 Emil Molt, 1876-1936. 167 Moritz Benedikt, 1835-1920, österreichischer Mediziner und Mitbegründer der Kriminalanthropologie.",
      "«Anatomische Stu- dien an Verbrechergehirnen» 1878, und «Aus meinem Leben. Erinnerungen und Erörterungen», 1906, S. 318-319. 171 die Leugnung der Präexistenz: Die früheste in der kirchlichen Dogmensammlung auch heute noch aufgeführte Verdammung der Präexistenzlehre entstammt dem Buch des oströmischen Kaisers Justinian «Liber adversus Origenem».",
      "Die darin ent- haltenen «Canones contra Origenem» wurden nach dem Zeug- 253 nis des Geschichtsschreibers Cassiodorus von Papst Vigilius (540-555) durch nachträgliche Unterschrift bestätigt. (Vgl. Den- zinger & Bannwart, «Enchiridion Symbolorum», Fußnote zu den «Canones».) Canon i besagt: «Wenn jemand sagt oder annimmt, die Seelen der Menschen präexistierten etwa derart, daß sie zuvor Geister und heilige Kräfte gewesen seien und dann, des Anschauens Gottes überdrüssig, schlechter geworden und dadurch aus Gottes Liebe herausgekühlt und deshalb genannt und zur Strafe in Körper verschickt worden seien: anathema sit» (a.a.O.",
      "Dokument 203). 172. Origenes, um 185-254, griechischer Kirchenschriftsteller und Philosoph. Justinian, 483-565. Seit 527 oströmischer Kaiser. 174 Wilhelm Scherer: Siehe Zitat S. 119. 176meine Schrift über das soziale Leben: «Die Kernpunkte der sozialen Frage in den Lebensnotwendigkeiten der Gegenwart und Zukunft» (1919), Bibl.-Nr. 23, Gesamtausgabe Dornach 1976 (auch als Taschenbuchausgabe tb 606 [Dornach 1973] er- schienen). 177meine «Tbeosophie»: «Theosophie.",
      "Einführung in übersinnliche Welterkenntnis und Menschenbestimmung» (1904), Bibl.-Nr. 9, Gesamtausgabe Dornach 1973 (auch als Taschenbuchausgabe tb 615 [Dornach 1976] erschienen). meine Auseinandersetzungen mit dem Haeckelianismus: Zum Beispiel im «Magazin für Literatur» (1898-1900); vgl. auch J. Hemleben, «Rudolf Steiner und Ernst Haeckel», 2.",
      "Aufl. Stuttgart 1965. 178 zum Beispiel vorgestern in Stuttgart: Vgl. die Aussprache auf S. 164 ff. in meinem Buch «In Ausführung der Dreigliederung»: Jetzt im Band «Aufsätze über die Dreigliederung des sozialen Organis- mus und zur Zeitlage 1915-1921», Bibl.-Nr. 24, Gesamtausgabe Dornach 1961. 180Arthur Schopenhauer, 1778-1860.",
      "«Da ergibt sich, daß Moral- Predigen leicht, Moral-Begründen schwer ist...», in: Schriften zur Naturphilosophie und zur Ethik, I. Über den Willen in der Natur. 181Johann Friedrich Herbart, 1776-1841. «Allgemeine praktische Philosophie», 1808 254 183 vorangehenden «Aufruf»; Aufruf an das deutsche Volk und an die Kulturwelt.",
      "Als Anhang abgedruckt in «Die Kernpunkte der sozialen Frage» und in «Aufsätze über die Dreigliede- rung ...», Bibl.-Nr. 24. Darin auf S. 473 Erläuterungen. die blutleerste Abstraktion: Über die in Wilsons Proklamatio- nen enthaltenen «blutleersten Abstraktionen» vgl. u. a. die Memoranden Rudolf Steiners vom Juli 1917, in «Aufsätze über die Dreigliederung...», S. 329 f. und die Hinweise dazu auf S. 471 f.",
      "Woodrow Wilson, 1856-1924, von 19131921 Präsident der USA. Die Vierzehn Punkte wurden im Versailler Vertrag 1919 nicht verwirklicht. John Maynard Keynes, 1883-1946, englischer Nationalökonom. 184Warren Harding, 1865-1923, war als Kandidat der Republika- nischen Partei gewählt worden.",
      "Er hatte sein Amt als Präsident der USA am 4. März 1921 angetreten. 185Lloyd George, 1863-1945. 1916 britischer Premierminister. dasjenige, was wirklich eingetreten ist: Der Bergarbeiterstreik vom April bis Juni 1921.",
      "Siehe Hinweis zu S. 94. 186 zu den breiten Massen des Volkes zu reden: Rudolf Steiner sprach im Frühjahr 1919 in Basel, Zürich, Bern, später beson- ders in Stuttgart und anderen deutschen Städten zu einer aus der Arbeiterbevölkerung zusammengeströmten Zuhörerschaft in Stuttgart z. B. zur Arbeiterschaft der Daimler-Werke; vgl.",
      "Rudolf Steiner, «Neugestaltung des sozialen Organismus», Bibl.-Nr. 330, Gesamtausgabe Dornach 1963. 189 Wladimir Iljitsch Lenin, 1870-1924. Leo Trotzkij, 1879-1940. Anatoli Wissiljewitsch Lunatscharskij, 18751933.",
      "Von 1917 bis 1919 sowjetischer Volkskommissar für das Bildungswesen. 190 Karl Giskra, 18201879. 1846 Professor der Staatswissenschaf- ten in Wien. Den Ausspruch, daß die soziale Frage an der Grenze von Österreich (in Bodenbach) aufhöre, tat Giskra als österreichischer Innenminister Ende der sechziger Jahre. 195 im April 1912: Tatsächlich war im Frühling 1912 ein solcher «Bund» begründet worden.",
      "Er sollte den Rahmen geben für eine theosophische Arbeit unabhängig von Mrs. Annie Besant, die durch Proklamierung des Hinduknaben Krishnamurti zum neuen Messias und durch Ausstreuung von Verleumdungen über Dr.",
      "Steiner autoritäre Allüren angenommen und den Boden der Wahrheit verlassen hatte; durch ein betont deut- liches Links-Liegenlassen des Unfugs sollte der Bund den Zu- sammenschluß der sich immer zahlreicher in vielen Ländern um das Wirken Rudolf Steiners sammelnden Menschen er- möglichen. Dieser «Bund» kam nie über das Stadium der Besprechungen hinaus.",
      "Vielmehr wurde die Entscheidung im unausweichlichen Konflikt mit Mrs. Besant durch ein Tele- gramm des Vorstandes der «Deutschen Sektion» an den «Ge- neral Council» der «Theosophischen Gesellschaft» vom 11.",
      "Dezember 1912 herbeigeführt, das ohne Umschweife die Sache beim wahren Namen nannte: «Der zu außerordentlicher Sitzung zu Berlin am 8. Dezember 1912 versammelte Vorstand der Deutschen Sektion der Theosophischen Gesellschaft erkennt in dem Vorgehen der Präsidentin der Theosophischen Gesellschaft eine fortgesetzte objektive Verschleierung und Entstellung der Tatsachen, die dem obersten Grundsatz der Theosophischen Gesellschaft, der Forderung der Wahrhaftigkeit widerspricht.",
      "Auf Grund dieser Erkenntnis, daß die Präsidentin unausge- setzt und geradezu systematisch gegen den obersten Grundsatz der Theosophischen Gesellschaft («Kein Bekenntnis über die Wahrheit>) verstoßen und in Mißbrauch und Willkür die Präsidialgewalt mit Behinderung positiver Arbeit ausgeübt hat, kann der versammelte Vorstand der Deutschen Sektion, nach genauester Prüfung der Dokumente, nur in der Resigna- tion der Präsidentin die Möglichkeit des weiteren Fortbestandes der Gesellschaft sehen...» (Siehe «Mitteilungen für die Mit- glieder der Deutschen Sektion der Theosophischen Gesellschaft», Nr. XV, herausgegeben von Mathilde Scholl, Köln, Januar 1913.) Durch Feststellung der Wahrheit und Aufforderung zum Rücktritt kam es zum Ausschluß der «Deutschen Sektion» aus der «Theosophischen Gesellschaft» und zur Gründung der Anthroposophischen Gesellschaft.",
      "Der Entschluß zur Absen- dung des entscheidenden Telegramms wurde ohne Mitwirkung Rudolf Steiners, hauptsächlich auf Initiative des Kölner Mit- glieds Fräulein Mathilde Scholl gefaßt. Rudolf Steiner be- zeichnete ihn nachträglich als den einzig und allein möglichen.",
      "Dies zum Verständnis der nachfolgenden Worte Rudolf Stei- 199 in der Vorrede zu jenen Vorträgen... einen Satz: Siehe Rudolf Steiner, «Die Mystik im Aufgange des neuzeitlichen Geistes- 256 lebens und ihr Verhältnis zur modernen Weltanschauung», Vorwort zur i. Aufl., worinnen ich sage (wörtlich): «Was ich in dieser Schrift darstelle, bildete vorher den Inhalt von Vor- trägen, die ich im verflossenen Winter in der theosophischen Bibliothek zu Berlin gehalten habe...» in Bibl.-Nr. 7, Ge- samtausgabe Dornach 1960. 200 «Futurum A.-G.»: ökonomische Gesellschaft zur internationalen Förderung wirtschaftlicher und geistiger Werte, Dornach 1920- 1924.",
      "Siehe «Die Konstitution der Allgemeinen Anthroposo- phischen Gesellschaft und der Freien Hochschule für Geistes- wissenschaft», Bibl.-Nr. 37/26oa, Gesamtausgabe Dornach 1966, S. 714/715; «Kommenden Tag», ebenda S. 719/720. 205Prof. Römer: Siehe Hinweis zu S. 118. 206«Kommenden Tag»: Siehe Hinweis zu S. 200. 207«Futurum»: Siehe Hinweis zu S. 200. 209 Prof.",
      "Fuchs: In Nr. 5 des 2. Jg. der Stuttgarter Wochenschrift «Dreigliederung des sozialen Organismus» (August 1920) hatte Rudolf Steiner in einem Aufsatz «Ein paar Worte zum Fuchs- Angriff» zu einer vom Göttinger Anatomen Prof.",
      "Hugo Fuchs vom Zaune gerissenen Attacke geschrieben: «Von einem Forscher, der ernst genommen werden soll, muß verlangt wer- den, daß er den Sinn für objektive Tatsachen hat. Wer ein anatomisches Präparat vorgelegt erhält, das gegen eine absurde Behauptung spricht, der kann wissenschaftlich nur ernst genom- men werden, wenn er sich das Präparat erst ansieht und seinen Zusammenhang mit ändern Tatsachen ins Auge fassen will.",
      "Prof. Fuchs hört, daß in Stuttgart gegen die blöde Behaup- tung, ich sei Jude, mein Taufschein vorgewiesen worden ist. Er sagt, wie so viele andere, die in gewissenloser Weise die Lüge verbreiten, ich sei Jude, es gebe auch getaufte Juden.",
      "Nun, mein Taufschein enthält aber Daten, die so gegen meine Abstammung von Juden sprechen, daß sich schon aus ihnen die Behauptung meines Judentums als eben blöder Unsinn enthüllt. Ich brauche wohl nicht zu sagen, daß ich selbst keinen Wert auf meine Ab- stammung von diesem Gesichtspunkte aus lege.",
      "Es handelt sich für mich lediglich darum, daß es dreist erlogen ist, wenn man mich zum Juden macht. Für mich aber ist, wer so über Tat- sachen spricht, wie Prof. Fuchs über mein angebliches Judentum, wenn auch nur so nebenher, kein Wissenschafter...» Abge- druckt in «Aufsätze zur Dreigliederung des sozialen Organis- mus und zur Zeitlage 1915-1921», Bibl.-Nr. 24, Gesamtaus- gabe Dornach 1961. 257 210 einen Vortragenden «Winter» erfindet: Siehe Hinweis zu S. 199. 211 Graf Hermann von Keyserling, 1880-1946.",
      "In «Philosophie als Kunst» (Darmstadt 1920) hatte Hermann Keyserling von Ru- dolf Steiner geschrieben, daß «es ... jedenfalls für sein Wesen symbolisch ist, daß seine geistige Laufbahn in gewissen Hin- sichten von Haeckel ausging». Wie Haeckel von sich aus an Rudolf Steiner herangekommen ist, findet sich genau dargestellt in «Mein Lebensgang», Bibl.-Nr. 28, Gesamtausgabe Dornach 1962, Kap.",
      "XV. in den frühesten Jahren meiner Schriftstellerei: Zum Beispiel in «Goethes Naturwissenschaftlichen Schriften», Band I: Ein- leitung, S. LX ff. «Goethe ist der Kopernikus und Kepler der organischen Welt» (S.",
      "LXXIII). eine kleine Schrift erscheinen lassen: «Der Weg zur Vollendung. Mitteilungen der Gesellschaft für Freie Philosophie. Schule der Weisheit.» i. Heft, November 1920. steht da folgender Satz: Wörtlich: «... anstatt einen etwaigen Irrtum meinerseits zu korrigieren, was ich mir gern gefallen ließe, denn zu spezieller Steinerquellenforschung habe ich keine Zeit gehabt... zeiht Steiner mich schlankweg der Lüge...» (a.a.O.",
      "S.47). 212 Gustav Roethe, 1859-1926, Germanist. Verfaßte auch nationa- listische politische Flugschriften und hielt solche Reden. Nach seinem Tode erschienen «Deutsche Reden», 1927. 215 Diese Hochschule heißt...",
      "Goetheanum: Am 18. Oktober 1917 sagte Rudolf Steiner - vollkommen überraschend auch für die anwesenden Anthroposophen, denen der Dornacher Bau «Jö- hannesbau» hieß - in einem öffentlichen Vortrag in Basel: «Ich möchte die Weltanschauung, welche auf die Art wissenschaftlich entsteht, wie ich es angedeutet habe... nach den Quellen, aus denen sie für mich selber stammt ... am liebsten Goetheanismus nennen, so wie ich ... den Bau in Dornach draußen, der dieser Weltanschauung gewidmet ist, am liebsten Goetheanum nennen würde...» 216 Ich habe neulich ein Stück aus einem Feuilleton vorgelesen: Aus dem Jahrbuch von Elsbeth Ebertin, «Ein Blick in die Zukunft», Freiburg i.",
      "Br. 1921, S. 63; siehe hierzu auch die Ausführungen Rudolf Steiners in dem Dornacher Vortrag vom 23. Januar 1921 «Weltwirtschaftsgedanken im Chaos der Gegenwart vom Aspekt der"
    ],
    "sentences": [
      [
        "Von vielen Seiten wurde an die Veranstalter des Ersten anthroposo- phischen Hochschulkurses, der vom 26.",
        "September bis 16.",
        "Oktober 1920 am Goetheanum stattgefunden hat, das Verlangen gerichtet, die Kurse schon vor der eigentlichen Eröffnung des Goetheanums fortzu- setzen."
      ],
      [
        "So erging die Einladung zum Zweiten anthroposophischen Hochschulkursus vom 3. bis 10.",
        "April 1921 an der Freien Hoch- schule für Geisteswissenschaft Goetheanum in Dornach.",
        "Als Veran- stalter zeichneten der auf Anregung Rudolf Steiners von Roman Boos und zwei Freunden gegründete «Verein Goetheanismus» und der «Bund für anthroposophische Hochschularbeit»."
      ],
      [
        "Am Gesamtkurs waren 600 Teilnehmer ständig anwesend.",
        "Die Vormittagsvorträge waren jedermann zugänglich.",
        "Im Mittelpunkt standen die fünf in diesem Band enthaltenen Vorträge von Dr.",
        "Rudolf Steiner, unter dem Titel «Anthroposophie und Fachwissenschaften»."
      ],
      [
        "Anschließend daran sprachen zwölf Vortragende über ihr wissenschaftliches Arbeitsgebiet, und in mehreren Disputationen wurden in Frage und Antwort von Rudolf Steiner weitere Klärungen erarbeitet.",
        "Der vorliegende Band enthält außer der Eröffnungs- und Schluß- rede von Rudolf Steiner die fünf Vorträge zum Hauptthema sowie die dazugehörigen Beiträge Steiners zu den Disputationen, schließlich auch das Schlußwort Rudolf Steiners zu einer Studentenversammlung."
      ],
      [
        "Die während des Kurses zusätzlich gebotenen Vorträge Rudolf Stei- ners sind in die folgenden Bände der Gesamtausgabe aufgenommen worden: «Urrhythmus, Urgesang und Arrhythmus in ihrem Verhält- nis zur Eurythmie» vom 9.",
        "April 1921 in «Eurythmie."
      ],
      [
        "Die Offen- barung der sprechenden Seele» (Bibl.-Nr. 277, Dornach 1972); «Die Kunst des mündlichen Vortrages» vom 6.",
        "April 1921 in «Die Kunst der Rezitation und Deklamation» (Bibl.-Nr. 281, Dornach 1967); «Die Psychologie der Künste» vom 9."
      ],
      [
        "April 1921 in «Kunst und Kunsterkenntnis.",
        "Das Sinnlich-Übersinnliche in seiner Verwirklichung durch die Kunst» (Bibl.-Nr. 271, Dornach 1961); «Die menschliche Sprache und der Logos» vom 9.",
        "April 1921 geplant in «Perspektiven der Menschheitsentwicklung» (Bibl.-Nr. 204)."
      ],
      [
        "In dieser Auflage sind zum großen Teil die Hinweise von Roman Boos für die 1.",
        "Ausgabe, teilweise gekürzt, übernommen worden.",
        "Einige Ergänzungen waren erforderlich.",
        "Die acht im Rahmen des Ersten Hochschulkurses vom 26."
      ],
      [
        "Septem- ber bis 16.",
        "Oktober 1920 gehaltenen Vorträge Rudolf Steiners über «Grenzen der Naturkenntnis» liegen seit 1969 als Band 322 der Gesamtausgabe vor. 241 zu Seite 13 das alte Kantische Wort: Wörtlich: «Ich mußte also das Wissen aufheben, um zum Glauben Platz zu bekommen», Kant, «Kritik der reinen Vernunft», Vorrede zur 2."
      ],
      [
        "Auflage. 16 Emil Du Bois-Reymond: «Über die Grenzen des Naturerken- nens.",
        "Ein Vortrag, gehalten in der zweiten allgemeinen Sitzung der 45.",
        "Versammlung Deutscher Naturforscher und Ärzte zu Leipzig am 14.",
        "August 1872», Leipzig 1872, S. 12."
      ],
      [
        "Der Vor- trag endet mit dem bekannten «Ignorabimus». 23 die umgestalteten Worte des Hilarius: Vgl. die Gegenüberstel- lung der beiden Reden bei Febe Colazza in «Heute und hier», Dornach 1952. 26 Ludwig Haller: Das Buch (Berlin 1888) ist der Torso eines be- absichtigten Systems der Philosophie in mehreren Bänden.",
        "Der Verfasser war 1890 schon verstorben. 28 Immanuel Kant, 1724-1804. 28/29 «pseudodialektische ..."
      ],
      [
        "Charakter dieser Misosophie ...»: Siehe Haller a. a.",
        "S. 241. 29«Ich, der ich von Gott...»: Siehe Haller, a. a.",
        "S. 244. 30Eduard von Hartmann, 1842-1906.",
        "«Kritische Wanderungen durch die Philosophie der Gegenwart», Leipzig 1890, VI."
      ],
      [
        "Aufsatz: Eine neue dialektische Form der Mystik, S. 105 (1.",
        "Hallers Standpunkt im Allgemeinen; 2.",
        "Hallers Dialektik und sein Kampf gegen die Prioritäten; 3.",
        "Hallers Mystik). 32 ... lebendig gewordenen Begriffe: Siehe von Hartmann, a.a.O."
      ],
      [
        "S. 156: «Auf die Gefahr hin, von Haller für einen erklärt zu werden (S. 428), muß ich bekennen, daß ich keine Erfahrung über solche irrationale nek- kische Launen der Worte und Begriffe habe, und daß der Schein gegenteiliger Erfahrungen nach meiner Ansicht nur entweder aus einer molluskenhaften Haltlosigkeit und nichtsnutzigen Schlottrigkeit des Denkens oder aus einer auf irrationale Resul- tate gerichteten Tendenz des Denkens stammt.» ... sehr bedeutend gefunden: Siehe von Hartmann, a. a.",
        "S. 142 ff."
      ],
      [
        "Rudolf Steiner, «DieDie Rätsel der Philosophie in ihrer Geschichte als Umriß dargestellt», Berlin 1914, Bibl.-Nr. 18, Gesamtaus- gabe Dornach 1968 (auch als Taschenbuchausgaben tb 610/611 [Dornach 1974] erschienen). 242 33John Locke, 1632-1704. 34Thomas von Aquino, 1225-1274.",
        "Siehe Rudolf Steiner, «Die Philosophie des Thomas von Aquino», Bibl.-Nr. 74, Gesamt- ausgabe Dornach 1967 (auch als Taschenbuch tb 605 [Dornach 1972] erschienen). 35Gottfried Wilhelm Leibniz, 1646-1716."
      ],
      [
        "Christian Freiherr von Wolff, 1679-1754. 36Buch von Wolff: «Vernünftige Gedanken von Gott, der Welt und der Seele des Menschen, auch allen Dingen überhaupt», Frankfurt und Leipzig 1719. 37David Hume, 17111776. 38Rudolf Steiner, «Wahrheit und Wissenschaft».",
        "Vorspiel einer «Philosophie der Freiheit», 1892."
      ],
      [
        "Bibl.-Nr. 3, Gesamtaus- gabe Dornach 1958.",
        "Rudolf Steiner, «Die Philosophie der Freiheit».",
        "Grundzüge einer modernen Weltanschauung. 1894.",
        "Bibl.-Nr. 4, Gesamtaus- gabe Dornach 1973. 40 daß die Phänomene, die Erscheinungen rein sich selbst aus- sprechen: «Man erkundige sich ums Phänomen, nehme es so genau damit als möglich und sehe, wie weit man in der Einsicht und in praktischer Anwendung damit kommen kann, und lasse das Problem ruhig liegen."
      ],
      [
        "Umgekehrt handeln die Physiker: sie gehen gerade aufs Problem los und verwickeln sich unter- wegs in so viel Schwierigkeiten, daß ihnen zuletzt jede Aussicht verschwindet.» Aus «Goethes Naturwissenschaftliche Schriften», herausgegeben und eingeleitet von Rudolf Steiner in «Kürsch- ners Deutsche National-Litteratur» (1883-1894), Band V «Sprüche in Prosa», S. 417 (Bibl.-Nr. ia-e, Nachdruck in fünf Bänden, Dornach 1975).",
        "Phänomenalismus Goethes: «Das Höchste wäre, zu begreifen, daß alles Faktische schon Theorie ist."
      ],
      [
        "Die Bläue des Himmels offenbart uns das Grundgesetz der Chromatik.",
        "Man suche nur nichts hinter den Phänomenen; sie selbst sind die Lehre.» «Kein Phänomen erklärt sich an und aus sich selbst; nur viele zusammen überschaut, methodisch geordnet, geben zuletzt etwas, was für Theorie gelten könnte.» Aus «Goethes Naturwissen- schaftliche Schriften», Band V «Sprüche in Prosa», S. 376 und 375- 243 40Cartesius: Rene Descartes, 1596-1650. 41in der Neuauflage meiner «Philosophie der Freiheit»; Im «Zusatz zur Neuauflage» zum III."
      ],
      [
        "Kapitel. 42der gütige Gott habe ihn davor bewahrt, «über das Denken zu denken»; Goethe, «Zahme Xenien», VII: «Wie hast du's denn so weit gebracht? / Sie sagen, du habest es gut vollbracht!» Mein Kind! ich hab' es klug gemacht: / Ich habe nie über das Denken gedacht. 47 Disputationen: Im Einladungsprospekt zum Hochschulkurs waren für die Abendstunden angezeigt: «Anregende soziale - wissenschaftliche - künstlerische Disputationen mit kleinen Pikanterien dazwischen.» Rudolf Steiner selbst hatte die Anre- gung gegeben, die «kleinen Pikanterien dazwischen» im Pro- gramm anzuzeigen.",
        "Diese Ankündigung weckte bei guten Seelen etliche humorlose Empörung."
      ],
      [
        "Zur Beschwichtigung der Wellen fügte nun Rudolf Steiner seinem Vortrag vom 1.",
        "April 1921 (zwei Tage vor der Eröffnung des Kurses) die folgenden erläuternden Worte an: «Meine lieben Freunde, ich möchte jetzt nur noch ein paar Worte über etwas anderes, etwas ganz anderes sagen."
      ],
      [
        "Ich habe ver- nommen, daß eine gewisse Ängstlichkeit herrscht - in den Krei- sen, welche die Verantwortung für die Sache haben -, eine ge- wisse Ängstlichkeit mit Bezug auf den Punkt in unserem Kurs- programm, wo viel ernste soziale und sonstige Unterhaltungen für die Abende vorgesehen sind und die Rede ist von den «klei- nen Pikanterien».",
        "Ich war etwas frappiert über diese Ängst- lichkeit, nachdem so oftmals hier davon gesprochen worden ist, daß nur vom seelischen Zusammenwirken aller derjenigen, die sich zur anthroposophischen Bewegung zählen, das Heil dieser Bewegung kommen kann."
      ],
      [
        "Ich war deshalb frappiert, weil ich ge- glaubt habe - da hier so oft dies betont worden ist -, daß we- nigstens mit Bezug auf diese Eigenschaften des Funkensprühen- lassens aus alldem heraus, was man als Geistreichigkeit auf seiner Seele trägt, längst jeder die Seelenvorbereitung an sich getrof- fen hat; und ich habe eigentlich gemeint, daß wir gar kein Ende gerade dieser Abende werden finden können, wo dasje- nige, was individuell an Geistreichigkeit in den Seelen seit lange sich aufgespeichert hat, sich in ganzen Feuergarben von Pikanterien - in noblerem Sinne Pikanterien! - entladen werde!",
        "Ich hoffe das auch heute noch, möchte aber doch eben bemer- ken, daß das nicht etwa darinnen bestehen kann, daß man 244 programmäßig etwa so einen nach dem anderen aufs Podium hinaufschickt, daß er Pikanterien losläßt!"
      ],
      [
        "Das würde meiner Meinung nach in bezug auf diesen Programmpunkt nicht das Richtige sein.",
        "Sondern da muß jeder schon so anspruchslos sein, daß er vielleicht nur zu einem ganz kleinen Kreise der Umge- bung, den er grad in einem Momente trifft, solches Feuersprühen losläßt, so daß diese dann sehen müssen, wie sie feurig sein können."
      ],
      [
        "Es kann manches mit Lachen, es kann aber auch man- ches mit anderen Gefühlsimpulsen, die sich als notwendige Folge ergeben können, gesagt werden.",
        "«Pikanterien», das müssen ja nicht bloß Lustigkeiten sein, das können auch andere Dinge sein!"
      ],
      [
        "Und so habe ich mir vorgestellt, daß das wirklich von Mensch zu Mensch sich entwickeln werde.",
        "Es hat sich ja, was so im per- sönlichen Umgange von Mensch zu Mensch sich abspielt, das letztemal bei dem Kurs (beim i."
      ],
      [
        "Hochschulkurs, Herbst 1920) so wenig gezeigt, daß man denken kann: Es hat sich da eben im stillen vieles aufgespeichert, was jetzt losgelassen werden soll!",
        "Aber ich stelle mir das gewissermaßen so vor, daß in diesen paar Tagen - es sind ja nur noch zwei! - jeder mit sich zu Rate geht und nun tief in seine Seele hineinschaut, was er an solchen «Pikanterie» möglichkeiten in seiner Seele trägt, so daß er dann herumgehen kann von einer Gruppe zur anderen, und daß da die Dinge an jedem Abend außerordentlich anregend verlaufen können."
      ],
      [
        "Es wird ja doch nicht fehlen, daß da ein gewisses soziales Leben auf diese Weise sich entspinnt.",
        "Es ist nicht notwendig, daß wir uns nur immer auf unsere Sitze setzen und auf unseren Sitzen etwas anhören wollen; denn wenn das jeder tun würde denken Sie, wozu wir dann kommen würden!"
      ],
      [
        "Das geht doch nicht, nicht wahr!",
        "Es würde ja keinen Sinn haben, von einer «Gesellschaft» zu sprechen, wenn nicht in dieser Weise auch gesellschaftsmäßig etwas auftreten würde.",
        "Also, wie gesagt, ich möchte nicht den Anregungen folgen, geradezu eine Anleitung zu der Sache zu geben, sondern ich möchte nur meine Meinung dahin aussprechen, daß nur gesagt zu werden braucht, daß man nicht zurückhalten soll mit sol- chen Dingen; dann werden sie sich ja hoffentlich schon ent- wickeln."
      ],
      [
        "Also hoffen wir, wir werden das Allerbeste auch in dieser Beziehung sehen in den nächsten zehn Tagen!» Tatsächlich waren die Abenddisputationen dann teilweise auch recht munter.",
        "Die erste der Disputationen fand Montag, 4."
      ],
      [
        "April, 20 Uhr, im Anschluß an Vorträge von Dr.",
        "Stein «Über das Wertproblem» und Dr.",
        "Carl Unger über «Das philosophische Bewußtsein und die Erforschung des Übersinnlichen» und seminaristische Übungen zu diesem Thema, statt."
      ],
      [
        "Stenographisch festgehalten wurde nur das Schlußwort Rudolf Steiners. 53innerhalb der Kategorientafel: Weder in den zehn (später acht) Kategorien des Aristoteles noch in den zwölf Kategorien Kants kommen «Subjekt» und «Objekt» vor.",
        "Erst der Kantianer Reinhold (1758-1823) hat sie in seinem «Satz des Bewußtseins» zu Stammbegriffen, zu unableitbaren Urformen unseres Den- kens, eben zu «Kategorien» befördert, in welcher Rolle sie seither besonders alles populär-philosophische Treiben durch- wuchern. 54Antipoden Kants: «Hier (bei Kant) liegt überhaupt... etwas Falsches verborgen, das mir daher zu kommen scheint, weil er das subjektive Erkenntnisvermögen nun selbst als Objekt be- trachtet und den Punkt, wo subjektiv und objektiv zusammen- treffen, zwar scharf aber nicht ganz richtig sondert» (Goethe, Weimarer Ausgabe, 2."
      ],
      [
        "Abt., Bd.",
        "XI, S. 376). 55Franz Brentano, 1838-1917. 56Der Brentano-Schüler: Siehe Oskar Kraus, «Franz Brentano», München 1919, S. i, 21. 57wie ich es beute morgen: Im Vortrag über «Philosophie»; siehe oben zu S. 26 ff. intentionales Innesein: Mit seinem Begriff des «intentionalen Inneseins» knüpft Brentano an die von Thomas von Aquino im Anschluß an Aristoteles entfaltete Lehre von den Sinnes- qualitäten an."
      ],
      [
        "Vgl. auch Rudolf Steiner, «Von Seelenrätseln», Anhang 5: «Über die wirkliche Grundlage der intentionalen Beziehung», Bibl.-Nr. 21, Gesamtausgabe Dornach 1976.",
        "Johannes Müller, 1801-1858, Physiologe und vergleichender Anatom. 61 Fritz Mauthner, 1849-1923, Schriftsteller und Sprachforscher."
      ],
      [
        "Siehe den Artikel «Mathematische Naturerklärung» in seinem «Wörterbuch der Philosophie».",
        "Vergleiche auch Rudolf Steiner über Fritz Mauthner, in «Zufall, Notwendigkeit und Vorsehung», Bibl.-Nr. 163, Gesamtausgabe Dornach 1975. die gewollte Finsternis des Erkennens, wie sie sich bei Fritz Mauthner findet: Die «gewollte Finsternis des Erkennens» kommt beispielsweise zum Ausdruck in der «Einleitung» zum 246 «Wörterbuch der Philosophie»: «Ich werde froh sein, wenn ein ganz guter Leser am Ende des Weges sich sagen muß: die skeptische Resignation, die Einsidit in die Unerkennbarkeit der Wirklichkeitswelt, ist keine bloße Negation, ist unser bestes Wissen; die Philosophie ist Erkenntnistheorie, Erkenntnistheorie ist Sprachkritik; Sprachkritik aber ist die Arbeit an dem be- freienden Gedanken, daß die Menschen mit den Wörtern ihrer Sprachen und mit den Worten ihrer Philosophien niemals über die bildliche Darstellung der Welt hinausgelangen.» 61Ausspruch Kants: «Ich behaupte, daß in jeder besonderen Naturlehre nur so viel eigentliche Wissenschaft angetroffen werden könne, als darin Mathematik anzutreffen ist.» (Vor- rede zu der 1786 veröffentlichten Schrift «Metaphysische An- fangsgründe der Naturwissenschaft».) 62Cartesius: Siehe Hinweis zu S. 40."
      ],
      [
        "Buchenau zitiert in seinem Kommentar zu den «Meditationen über die Grundlagen der Philosophie» von Descartes (Leipzig, Meiner) aus den Schriften Descartes' u. a. folgende Aussprüche: «...Nach meiner An- sicht geschieht alles in der Natur auf mathematische Art...",
        "Was die Physik betrifft, so würde ich vermeinen, von ihr nichts zu wissen, wenn ich nur zu sagen wüßte, wie die Dinge sich verhalten können, ohne zu beweisen, daß sie nicht anders sein können; denn da ich sie auf Mathematik zurückgeführt habe, so ist dies eine mögliche Anschauung...» «... ich rühme mich, daß ich mich einer solchen Art zu philosophieren bediene, wobei kein Grund zugelassen wird, der nicht mathematisch und evident ist und wobei die Schlußfolgerungen durch unzweifelhafte Er- fahrungen bestätigt werden » Benedictus Spinoza, 1632-1677."
      ],
      [
        "Die einzige Schrift, die Spinoza mit voller Nennung seines Namens herausgegeben hat, trägt den Titel «Descartes' Prinzipien der Philosophie auf geometri- sche Weise begründet».",
        "Auch sein eigentliches Lebenswerk, die «Ethik», trägt den Untertitel «nach geometrischer Methode dargestellt». 63 das Wort «Mathematik»; «Mathesis» (von «manthano», lernen) heißt ursprünglich «das Lernen», dann «die Erkenntnis» und «der Unterricht». 65 Adrien Legendre, 17521833, französischer Mathematiker."
      ],
      [
        "Farkas (Wolfgang) Bolyai, 17751856, ungarischer Mathema- tiker, und sein Sohn Johann Bolyai, 1802-1860. 247 65 Nikolai Lobatschewskij, 1793-1856, russischer Mathematiker. 67 Behandlung der «Farbenlehre»; Siehe Hinweis zu S. 109.",
        "Goethe ... wollte auch das Qualitative einbezogen haben: «Der Mathematiker ist angewiesen aufs Quantitative, auf alles, was sich durch Zahl und Maß bestimmen läßt, und also gewisser- maßen auf das äußerlich erkennbare Universum."
      ],
      [
        "Betrachten wir aber dieses, insofern uns Fähigkeit gegeben ist, mit vollem Geiste und aus allen Kräften, so erkennen wir, daß Quantität und Qualität als die zwei Pole des erscheinenden Daseins gelten müssen ...» Aus «Goethes Naturwissenschaftliche Schriften», Band V, «Sprüche in Prosa», S. 406. 84 Zweite Disputation: Dienstag, 5.",
        "April 1921, sprachen nach Rudolf Steiner («Mathematik und anorganische Naturwissen- schaften») Dr."
      ],
      [
        "Hermann von Baravalle («Raum und Zeit») und Dr.",
        "Ernst Blümel («Geisteswissenschaftliche Richtlinien zur mathematischen Behandlung naturwissenschaftlicher Probleme»).",
        "Die Abenddisputation hielt sich nicht ans Thema des Tages. (Dieses wurde zwei Tage später aufgegriffen.) Deutsche Stu- denten brachten ihre Nöte zur Sprache."
      ],
      [
        "So klagte ein Student aus Bonn den Universitätsbetrieb an, «aus einem falschen Grundmotiv heraus mit verkehrten Methoden an der Jugend zu arbeiten»; es könne passieren, daß man beim einen Dozen- ten das Gegenteil von dem zu hören bekomme, was der andre sage; die Wissenschaft werde «um ihrer selbst willen» getrie- ben, nicht «um der Menschen willen»; wer Philosophie studiere, müsse sich «der Philosophie hinopfern, absterben als Mensch» - um das Examen bestehen zu können; viele seiner Freunde sagten, daß «sie sich an der Hochschule als Mensch nicht retten könnten».",
        "Als der Artikel «Ethische Irrlehren» von Prof."
      ],
      [
        "Rein, Jena («Der Tag» vom 23.",
        "November 1920), der eine scharf ablehnende Besprechung der Neuauflage der «Philosophie der Freiheit» enthielt, erwähnt und dem Verfasser vorgeworfen wurde, er habe diese Rezension unter dem Druck der damals gegen Rudolf Steiner stark aufgehetzten «öffentlichen Mei- nung» geschrieben, meldete sich ein Student aus Jena: Professor Rein sei sein Schwiegervater; die «Philosophie der Freiheit» sei ihm von einem führenden Mitgliede der Anthroposophischen Gesellschaft in Jena zugestellt worden; die «öffentliche Mei- nung» spiele nicht herein. - Nach langem, sehr temperament- vollem Hin und Her ergriff Rudolf Steiner das Wort."
      ],
      [
        "Wilhelm Rein, 1847-1921. eine der ersten Besprechungen: Diese Besprechung der «Philo- 248 sophie der Freiheit» durch Robert Zimmermann (1824-1898) konnte bisher nicht aufgefunden werden. 87/88 eine Ethik für Anthroposophen: Die nachfolgenden Sätze Reins lauten: «Diese freien Menschen des Dr.",
        "Steiner sind aber bereits keine Menschen mehr."
      ],
      [
        "Sie sind in die Welt der Engel schon auf Erden eingetreten.",
        "Die Anthroposophie hat ihnen dazu verhel- fen.",
        "Müßte es nicht eine unsagbare Wohltat mitten in den mannigfachen Wirrnissen des Erdenlebens sein, sich in solche Umgebung versetzen zu lassen?» und so weiter. 91Waldorfschule: Aus der Ansprache Rudolf Steiners bei der Eröffnung der «Freien Waldorfschule» am 7."
      ],
      [
        "September 1919: «Jedenfalls soll diese Waldorfschule nicht eine Weltanschau- ungsschule werden.",
        "Derjenige, der da sagen wird: die anthropo- sophisch orientierte Geisteswissenschaft gründe die Waldorf- schule und wolle ihre Weltanschauung hineintragen in diese Schule - ich sage das jetzt am Eröffnungstage! -, der wird nicht die Wahrheit sprechen...» Siehe «Rudolf Steiner in der Wal- dorfschule», Ansprachen für Kinder, Eltern und Lehrer 19191924, Bibl.-Nr. 298, Gesamtausgabe, Stuttgart 1958. 92Weltschulverein: Der «Weltschulverein» sollte der organisa- torisch-ökonomische Träger des über alle nationalen Grenzen hinweg sich sammelnden Willens zur Befreiung der Schulen aus den staatlich-politischen Fesselungen sein."
      ],
      [
        "Am 12.",
        "Oktober 1920 rief Rudolf Steiner in einem Vortrag über die Grund- probleme der sozialen Struktur - die wahrhaft internationale Zuhörerschaft des ersten Hochschulkurses zum Schluß dazu auf, die Begeisterung, die reichlich vorhanden war, in Tatkraft zu verdichten."
      ],
      [
        "Aber es blieb bei Gefühlen und Worten der Begei- sterung.",
        "Zu Taten kam es nicht. unserer letzten Hochschulkurse: Erster anthroposophischer Hochschulkurs vom 27.",
        "September bis 16.",
        "Oktober 1920, siehe «Grenzen der Naturerkenntnis», Bibl.-Nr. 322, Gesamtaus- gabe Dornach 1969. 94 Sie könnten das schon seit einigen Tagen tun: Am i."
      ],
      [
        "April 1921 war in England der neue Bergarbeiterstreik ausgebrochen.",
        "Er zwang die Regierung den «state of emergency» (Zustand drohender Not) zu verkünden, sofort die Einschränkung des Kohlenverbrauchs und das Verbot der Kohlenausfuhr zu ver- fügen und das Ober- und Unterhaus auf den 4."
      ],
      [
        "April einzube- rufen.",
        "Der Streik dauerte dann ein volles Vierteljahr.",
        "Zahl- 249 reiche Gruben gerieten unter Wasser wegen Nichtbedienung der Pumpen. 97 Phoronomie: Vgl. dazu die Ausführungen Rudolf Steiners in «Geisteswissenschaftliche Impulse zur Enrwickelung der Physik."
      ],
      [
        "Erster Naturwissenschaftlicher Kurs», Bibl.-Nr. 320, Gesamt- ausgabe Dornach 1964 (10.",
        "Vortrag). 99 in meinen . . .",
        "«Einleitungen zu Goethes Naturwissenschaftlichen Schriften»: In «Kürschners Deutsche National-Litteratur» Bände 114-117, 1883-1897; siehe Rudolf Steiner, «Goethes Naturwissenschaftliche Schriften."
      ],
      [
        "Einleitungen», Bibl.-Nr. i, Gesamtausgabe Dornach 1973. 100 Johannes Müller, 1801-1858, Begründer der modernen Physio- logie.",
        "Ernst Mach, 1838-1916, österreichischer Physiker und Philosoph.",
        "Henri Poincare, 1854-1912, Mathematiker, Physiker und Astronom."
      ],
      [
        "Fritz Mauthner: Siehe Hinweis zu S. 61.",
        "Das ist die Idee der Lebenskraft: Vgl.",
        "Driesch, «Der Vitalismus als Geschichte und als Lehre», Leipzig 1905.",
        "Über die «Erfin- dung» der Lebenskraft durch Georg Ernst Stahl im 17., 18."
      ],
      [
        "Jahrhundert vgl.",
        "Rudolf Steiner, «Der Entstehungsmoment der Naturwissenschaft in der Weltgeschichte und ihre seitherige Ent- wickelung«, 8.",
        "Vortrag, Bibl.-Nr. 326, Gesamtausgabe Dornach 101 die Darstellung eines organischen Stoffes in synthetischer Weise von Wohler und Liebig: 1828 gelang zum ersten Mal Friedrich Wohler, 1800-1882, die künstliche Darstellung einer organischen Substanz."
      ],
      [
        "Er gewann Harnstoff aus zyansaurem Ammonium.",
        "Justus von Liebig, 1803-1873. 103 in meinem ersten Vortrag dieser Reihe: Siehe S. 26 ff. 109zum Beispiel in der Farbenlehre und in der Tonlehre: Siehe «Goethes Naturwissenschaftliche Schriften», Bände III-V (Far- benlehre) und Band V, S. 596 ff. (Tonlehre). 110Monere: Von Haeckel konstruiertes, tatsächlich nicht existieren- des einfachstes Lebewesen, das nur aus Protoplasma ohne Kern besteht. 250 110 Ernst Haeckel, 1834-1919. 111 eine Umbildung der Rückenwirbelsäule: Über Goethes «Wirbel- theorie des Schädels» vgl. die Anmerkungen Rudolf Steiners zu S. 316 des i."
      ],
      [
        "Bandes von «Goethes Naturwissenschaftlichen Schriften», siehe Hinweis zu S. 99. 112 daß der Mensch ein älteres Wesen ist: Über das entwicklungs- geschichtliche Verhältnis von Mensch und Tier siehe Rudolf Steiner, «Die Geheimwissenschaft im Umriß», Kapitel «Die Weltentwicklung und der Mensch», Bibl.-Nr. 13, Gesamtausgabe Dornach 1977 (auch als Taschenbuchausgabe tb 601 [Dornach 1976] erschienen). 114 die «psychophysischen Parallelitiker»: G.",
        "Lipps gibt in seinem «Grundriß der Psychophysik» (Leipzig 1909) eine Charakteri- sierung des «psychophysischen Parallelismus». 116 Frühlingskurs ... für Ärzte und Medizinstudierende: «Geistes- wissenschaft und Medizin». 20 Vorträge, gehalten von Dr."
      ],
      [
        "Ru- dolf Steiner vor Ärzten und Medizinstudierenden in Dornach vom 21.",
        "März bis 9.",
        "April 1920; Bibl-Nr. 312, Gesamtausgabe Dornach 1976. 118Oskar Römer, 18661952, Prof.",
        "Dr. med. et med. dent. h. c., Direktor der operativen Abteilung des Zahnärztlichen Instituts der Universität Leipzig."
      ],
      [
        "«Über die Zahnkaries mit Beziehung auf die Ergebnisse der Geistesforschung Dr.",
        "Rudolf Steiners», Stuttgart 1921. 119Dieser Ausspruch heißt: Zitiert am Kopf des Kapitels «Vokal- wandel» von Wilhelm Scherer, «Zur Geschichte der deutschen Sprache»; 2."
      ],
      [
        "Aufl.",
        "Berlin 1890, S. 30.",
        "Wilhelm Scherer, 1841-1886, vgl.",
        "Rudolf Steiner, «Mein Le- bensgang», Kap.",
        "XIV, Bibl.-Nr. 28, Gesamtausgabe Dornach 1962. 127in meinem Büchelchen: «Die Erziehung des Kindes vom Ge- sichtspunkte der Geisteswissenschaft», Dornach 1976. 128die Anhänger des psychophysischen Parallelismus: Siehe Hin- weis zu S. 114. auf das Sie auch gestern aufmerksam gemacht worden sind: Prof."
      ],
      [
        "Römer war ausführlich auf die Ergebnisse der Forschung Rudolf Steiners eingegangen, wonach ein Kind im vorschul- 251 Pflichtigen Alter, das «nicht leicht zu einer geschickten Hand- habung der Hände und Füße zu bringen ist» nicht imstande ist, den Zahnbildungsprozeß - als dessen Ergebnis dann die zweiten Zähne hervorkommen - richtig zu entfalten, aus welchem Grunde «regulierend auf den Zahnprozeß in hohem Maße das wirkt, daß man die Kinder anleitet, und zwar schon möglichst früh, kunstvoll zu laufen, zum Beispiel im Kiebitzschritt und dergleichen, und möglichst früh mit eurythmisch beseelten Frei- übungen beginnt... und noch dafür sorgt, daß die Finger ge- schickt gemacht werden ...» 137gar nicht hineingehört: Siehe Vortrag vom 8.",
        "April, S. 169 ff. 138ganz bedeutenden Philologen: Siehe das Zitat von Wilhelm Scherer, S. 119. 139tobte gestern in Stuttgart eine Versammlung: Es handelte sich um eine Agitationsversammlung, in welcher der nationalistische General v."
      ],
      [
        "Gleich das große Wort führte.",
        "In der Abenddispu- tation wurde eingehender darüber gesprochen.",
        "Siehe S. 164 ff. 142Bernhard Rernhard, 1826-1866, Mitbegründer der Funktionen- theorie. 143Karl Friedrich Gauß, 1777-1855. 144die Kantschen Rattmdefinitionen: Kant verwendet beispiels- weise die Wörter «unendlich» und «unbegrenzt» als gleichbe- deutend im V."
      ],
      [
        "Abschnitt der Ausführungen über «Die Anti- nomie der reinen Vernunft» seiner «Kritik der reinen Ver- nunft», wo er zeigt, daß auf die «Frage wegen der Weltgröße des Raumes» unsere Begriffe eine Antwort nicht geben können: «Denn ist sie (die Weltgröße) unendlich und unbegrenzt, so ist sie für allen möglichen empirischen Begriff zu groß.",
        "Ist sie endlich und begrenzt, so fragt ihr mit Recht noch: was bestimmt diese Grenze? ..."
      ],
      [
        "Also ist eine begrenzte Welt für euren Begriff zu klein...» Aus dieser «Antinomie» kommt Kant dadurch heraus, daß er dekretiert: «...der Raum (ist) nicht eine Beschaffenheit der Dinge außer mir, sondern eine bloße Vorstellungsart in mir...» («Kritik der Urteilskraft», S. 276 der Originalausgabe). 145die Paralogismenlehre: Im Zusammenhang seiner Lehre von den «Paralogismen» (Trugschlüssen) zieht Kant die Erkenntnis- grenze ausdrücklich mitten durch das Problem der «...",
        "Ver- knüpfung ... unseres denkenden Wesens ... mit der Körper- 252 welt...» («Kritik der reinen Vernunft», i."
      ],
      [
        "Aufl., S. 395).",
        "Ir- gendwelche Antworten auf dieses Problem können nur «einge- bildeter Wissenschaft» entspringen, und zwar «sowohl in An- sehung dessen, der bejahend, als dessen, der verneinend be- hauptet ..."
      ],
      [
        "Nichts als die Nüchternheit einer strengen, aber gerechten Kritik kann von diesem dogmatischen Blendwerke ... befreien...» 146 Euklid, um 300 v.",
        "Chr., griechischer Mathematiker, lebte in Alexandria. 153nun liegt eine Frage vor: Diese Frage bezieht sich auf Aus- führungen des Vortragenden am Vorabend vor dem zweiten Hochschulkurs. 154Friedrich Husemann, 1887-1959, Facharzt für Psychiatrie. wie sich aus der Dunkelheit das Blau herausnuanciert: Vgl. dazu Charles von Steiger, «Über die Farbwahrnehmungen des Men- schen in früheren Kulturen und die auf diesem Gebiet gemach- ten Entdeckungen», «Gegenwart», 7."
      ],
      [
        "Jg. 1945 Nr. 6, mit Wort- lauten Rudolf Steiners, speziell über den Zusammenhang zwi- schen der «Verschiebung des Spektrum-Anschauens nach dem dunklen Teile hin» und dem Vorgang, daß sich seit der grie- chischen Kulturepoche «der Denkprozeß verinnerlicht» hat. 159 in einem Vortragskurs genauer ausgeführt: Offensichtlich ver- weist hier Rudolf Steiner auf den 8.",
        "Vortrag des Kurses über die Wärmelehre, den er in 14 Vorträgen vom 1.-14."
      ],
      [
        "März 1920 in Stuttgart gehalten hat.",
        "«Geisteswissenschaftliche Impulse zur Entwickelung der Physik.",
        "Die Wärme auf der Grenze positiver und negativer Materialität», Bibl.-Nr. 321, Gesamtausgabe Dornach 1972. 164 Emil Molt, 1876-1936. 167 Moritz Benedikt, 1835-1920, österreichischer Mediziner und Mitbegründer der Kriminalanthropologie."
      ],
      [
        "«Anatomische Stu- dien an Verbrechergehirnen» 1878, und «Aus meinem Leben.",
        "Erinnerungen und Erörterungen», 1906, S. 318-319. 171 die Leugnung der Präexistenz: Die früheste in der kirchlichen Dogmensammlung auch heute noch aufgeführte Verdammung der Präexistenzlehre entstammt dem Buch des oströmischen Kaisers Justinian «Liber adversus Origenem»."
      ],
      [
        "Die darin ent- haltenen «Canones contra Origenem» wurden nach dem Zeug- 253 nis des Geschichtsschreibers Cassiodorus von Papst Vigilius (540-555) durch nachträgliche Unterschrift bestätigt. (Vgl.",
        "Den- zinger & Bannwart, «Enchiridion Symbolorum», Fußnote zu den «Canones».) Canon i besagt: «Wenn jemand sagt oder annimmt, die Seelen der Menschen präexistierten etwa derart, daß sie zuvor Geister und heilige Kräfte gewesen seien und dann, des Anschauens Gottes überdrüssig, schlechter geworden und dadurch aus Gottes Liebe herausgekühlt und deshalb genannt und zur Strafe in Körper verschickt worden seien: anathema sit» (a.a.O."
      ],
      [
        "Dokument 203). 172.",
        "Origenes, um 185-254, griechischer Kirchenschriftsteller und Philosoph.",
        "Justinian, 483-565.",
        "Seit 527 oströmischer Kaiser. 174 Wilhelm Scherer: Siehe Zitat S. 119. 176meine Schrift über das soziale Leben: «Die Kernpunkte der sozialen Frage in den Lebensnotwendigkeiten der Gegenwart und Zukunft» (1919), Bibl.-Nr. 23, Gesamtausgabe Dornach 1976 (auch als Taschenbuchausgabe tb 606 [Dornach 1973] er- schienen). 177meine «Tbeosophie»: «Theosophie."
      ],
      [
        "Einführung in übersinnliche Welterkenntnis und Menschenbestimmung» (1904), Bibl.-Nr. 9, Gesamtausgabe Dornach 1973 (auch als Taschenbuchausgabe tb 615 [Dornach 1976] erschienen). meine Auseinandersetzungen mit dem Haeckelianismus: Zum Beispiel im «Magazin für Literatur» (1898-1900); vgl. auch J.",
        "Hemleben, «Rudolf Steiner und Ernst Haeckel», 2."
      ],
      [
        "Aufl.",
        "Stuttgart 1965. 178 zum Beispiel vorgestern in Stuttgart: Vgl. die Aussprache auf S. 164 ff. in meinem Buch «In Ausführung der Dreigliederung»: Jetzt im Band «Aufsätze über die Dreigliederung des sozialen Organis- mus und zur Zeitlage 1915-1921», Bibl.-Nr. 24, Gesamtausgabe Dornach 1961. 180Arthur Schopenhauer, 1778-1860."
      ],
      [
        "«Da ergibt sich, daß Moral- Predigen leicht, Moral-Begründen schwer ist...», in: Schriften zur Naturphilosophie und zur Ethik, I.",
        "Über den Willen in der Natur. 181Johann Friedrich Herbart, 1776-1841.",
        "«Allgemeine praktische Philosophie», 1808 254 183 vorangehenden «Aufruf»; Aufruf an das deutsche Volk und an die Kulturwelt."
      ],
      [
        "Als Anhang abgedruckt in «Die Kernpunkte der sozialen Frage» und in «Aufsätze über die Dreigliede- rung ...», Bibl.-Nr. 24.",
        "Darin auf S. 473 Erläuterungen. die blutleerste Abstraktion: Über die in Wilsons Proklamatio- nen enthaltenen «blutleersten Abstraktionen» vgl. u. a. die Memoranden Rudolf Steiners vom Juli 1917, in «Aufsätze über die Dreigliederung...», S. 329 f. und die Hinweise dazu auf S. 471 f."
      ],
      [
        "Woodrow Wilson, 1856-1924, von 19131921 Präsident der USA.",
        "Die Vierzehn Punkte wurden im Versailler Vertrag 1919 nicht verwirklicht.",
        "John Maynard Keynes, 1883-1946, englischer Nationalökonom. 184Warren Harding, 1865-1923, war als Kandidat der Republika- nischen Partei gewählt worden."
      ],
      [
        "Er hatte sein Amt als Präsident der USA am 4.",
        "März 1921 angetreten. 185Lloyd George, 1863-1945. 1916 britischer Premierminister. dasjenige, was wirklich eingetreten ist: Der Bergarbeiterstreik vom April bis Juni 1921."
      ],
      [
        "Siehe Hinweis zu S. 94. 186 zu den breiten Massen des Volkes zu reden: Rudolf Steiner sprach im Frühjahr 1919 in Basel, Zürich, Bern, später beson- ders in Stuttgart und anderen deutschen Städten zu einer aus der Arbeiterbevölkerung zusammengeströmten Zuhörerschaft in Stuttgart z.",
        "B. zur Arbeiterschaft der Daimler-Werke; vgl."
      ],
      [
        "Rudolf Steiner, «Neugestaltung des sozialen Organismus», Bibl.-Nr. 330, Gesamtausgabe Dornach 1963. 189 Wladimir Iljitsch Lenin, 1870-1924.",
        "Leo Trotzkij, 1879-1940.",
        "Anatoli Wissiljewitsch Lunatscharskij, 18751933."
      ],
      [
        "Von 1917 bis 1919 sowjetischer Volkskommissar für das Bildungswesen. 190 Karl Giskra, 18201879. 1846 Professor der Staatswissenschaf- ten in Wien.",
        "Den Ausspruch, daß die soziale Frage an der Grenze von Österreich (in Bodenbach) aufhöre, tat Giskra als österreichischer Innenminister Ende der sechziger Jahre. 195 im April 1912: Tatsächlich war im Frühling 1912 ein solcher «Bund» begründet worden."
      ],
      [
        "Er sollte den Rahmen geben für eine theosophische Arbeit unabhängig von Mrs.",
        "Annie Besant, die durch Proklamierung des Hinduknaben Krishnamurti zum neuen Messias und durch Ausstreuung von Verleumdungen über Dr."
      ],
      [
        "Steiner autoritäre Allüren angenommen und den Boden der Wahrheit verlassen hatte; durch ein betont deut- liches Links-Liegenlassen des Unfugs sollte der Bund den Zu- sammenschluß der sich immer zahlreicher in vielen Ländern um das Wirken Rudolf Steiners sammelnden Menschen er- möglichen.",
        "Dieser «Bund» kam nie über das Stadium der Besprechungen hinaus."
      ],
      [
        "Vielmehr wurde die Entscheidung im unausweichlichen Konflikt mit Mrs.",
        "Besant durch ein Tele- gramm des Vorstandes der «Deutschen Sektion» an den «Ge- neral Council» der «Theosophischen Gesellschaft» vom 11."
      ],
      [
        "Dezember 1912 herbeigeführt, das ohne Umschweife die Sache beim wahren Namen nannte: «Der zu außerordentlicher Sitzung zu Berlin am 8.",
        "Dezember 1912 versammelte Vorstand der Deutschen Sektion der Theosophischen Gesellschaft erkennt in dem Vorgehen der Präsidentin der Theosophischen Gesellschaft eine fortgesetzte objektive Verschleierung und Entstellung der Tatsachen, die dem obersten Grundsatz der Theosophischen Gesellschaft, der Forderung der Wahrhaftigkeit widerspricht."
      ],
      [
        "Auf Grund dieser Erkenntnis, daß die Präsidentin unausge- setzt und geradezu systematisch gegen den obersten Grundsatz der Theosophischen Gesellschaft («Kein Bekenntnis über die Wahrheit>) verstoßen und in Mißbrauch und Willkür die Präsidialgewalt mit Behinderung positiver Arbeit ausgeübt hat, kann der versammelte Vorstand der Deutschen Sektion, nach genauester Prüfung der Dokumente, nur in der Resigna- tion der Präsidentin die Möglichkeit des weiteren Fortbestandes der Gesellschaft sehen...» (Siehe «Mitteilungen für die Mit- glieder der Deutschen Sektion der Theosophischen Gesellschaft», Nr.",
        "XV, herausgegeben von Mathilde Scholl, Köln, Januar 1913.) Durch Feststellung der Wahrheit und Aufforderung zum Rücktritt kam es zum Ausschluß der «Deutschen Sektion» aus der «Theosophischen Gesellschaft» und zur Gründung der Anthroposophischen Gesellschaft."
      ],
      [
        "Der Entschluß zur Absen- dung des entscheidenden Telegramms wurde ohne Mitwirkung Rudolf Steiners, hauptsächlich auf Initiative des Kölner Mit- glieds Fräulein Mathilde Scholl gefaßt.",
        "Rudolf Steiner be- zeichnete ihn nachträglich als den einzig und allein möglichen."
      ],
      [
        "Dies zum Verständnis der nachfolgenden Worte Rudolf Stei- 199 in der Vorrede zu jenen Vorträgen... einen Satz: Siehe Rudolf Steiner, «Die Mystik im Aufgange des neuzeitlichen Geistes- 256 lebens und ihr Verhältnis zur modernen Weltanschauung», Vorwort zur i.",
        "Aufl., worinnen ich sage (wörtlich): «Was ich in dieser Schrift darstelle, bildete vorher den Inhalt von Vor- trägen, die ich im verflossenen Winter in der theosophischen Bibliothek zu Berlin gehalten habe...» in Bibl.-Nr. 7, Ge- samtausgabe Dornach 1960. 200 «Futurum A.-G.»: ökonomische Gesellschaft zur internationalen Förderung wirtschaftlicher und geistiger Werte, Dornach 1920- 1924."
      ],
      [
        "Siehe «Die Konstitution der Allgemeinen Anthroposo- phischen Gesellschaft und der Freien Hochschule für Geistes- wissenschaft», Bibl.-Nr. 37/26oa, Gesamtausgabe Dornach 1966, S. 714/715; «Kommenden Tag», ebenda S. 719/720. 205Prof.",
        "Römer: Siehe Hinweis zu S. 118. 206«Kommenden Tag»: Siehe Hinweis zu S. 200. 207«Futurum»: Siehe Hinweis zu S. 200. 209 Prof."
      ],
      [
        "Fuchs: In Nr. 5 des 2.",
        "Jg. der Stuttgarter Wochenschrift «Dreigliederung des sozialen Organismus» (August 1920) hatte Rudolf Steiner in einem Aufsatz «Ein paar Worte zum Fuchs- Angriff» zu einer vom Göttinger Anatomen Prof."
      ],
      [
        "Hugo Fuchs vom Zaune gerissenen Attacke geschrieben: «Von einem Forscher, der ernst genommen werden soll, muß verlangt wer- den, daß er den Sinn für objektive Tatsachen hat.",
        "Wer ein anatomisches Präparat vorgelegt erhält, das gegen eine absurde Behauptung spricht, der kann wissenschaftlich nur ernst genom- men werden, wenn er sich das Präparat erst ansieht und seinen Zusammenhang mit ändern Tatsachen ins Auge fassen will."
      ],
      [
        "Prof.",
        "Fuchs hört, daß in Stuttgart gegen die blöde Behaup- tung, ich sei Jude, mein Taufschein vorgewiesen worden ist.",
        "Er sagt, wie so viele andere, die in gewissenloser Weise die Lüge verbreiten, ich sei Jude, es gebe auch getaufte Juden."
      ],
      [
        "Nun, mein Taufschein enthält aber Daten, die so gegen meine Abstammung von Juden sprechen, daß sich schon aus ihnen die Behauptung meines Judentums als eben blöder Unsinn enthüllt.",
        "Ich brauche wohl nicht zu sagen, daß ich selbst keinen Wert auf meine Ab- stammung von diesem Gesichtspunkte aus lege."
      ],
      [
        "Es handelt sich für mich lediglich darum, daß es dreist erlogen ist, wenn man mich zum Juden macht.",
        "Für mich aber ist, wer so über Tat- sachen spricht, wie Prof.",
        "Fuchs über mein angebliches Judentum, wenn auch nur so nebenher, kein Wissenschafter...» Abge- druckt in «Aufsätze zur Dreigliederung des sozialen Organis- mus und zur Zeitlage 1915-1921», Bibl.-Nr. 24, Gesamtaus- gabe Dornach 1961. 257 210 einen Vortragenden «Winter» erfindet: Siehe Hinweis zu S. 199. 211 Graf Hermann von Keyserling, 1880-1946."
      ],
      [
        "In «Philosophie als Kunst» (Darmstadt 1920) hatte Hermann Keyserling von Ru- dolf Steiner geschrieben, daß «es ... jedenfalls für sein Wesen symbolisch ist, daß seine geistige Laufbahn in gewissen Hin- sichten von Haeckel ausging».",
        "Wie Haeckel von sich aus an Rudolf Steiner herangekommen ist, findet sich genau dargestellt in «Mein Lebensgang», Bibl.-Nr. 28, Gesamtausgabe Dornach 1962, Kap."
      ],
      [
        "XV. in den frühesten Jahren meiner Schriftstellerei: Zum Beispiel in «Goethes Naturwissenschaftlichen Schriften», Band I: Ein- leitung, S.",
        "LX ff.",
        "«Goethe ist der Kopernikus und Kepler der organischen Welt» (S."
      ],
      [
        "LXXIII). eine kleine Schrift erscheinen lassen: «Der Weg zur Vollendung.",
        "Mitteilungen der Gesellschaft für Freie Philosophie.",
        "Schule der Weisheit.» i.",
        "Heft, November 1920. steht da folgender Satz: Wörtlich: «... anstatt einen etwaigen Irrtum meinerseits zu korrigieren, was ich mir gern gefallen ließe, denn zu spezieller Steinerquellenforschung habe ich keine Zeit gehabt... zeiht Steiner mich schlankweg der Lüge...» (a.a.O."
      ],
      [
        "S.47). 212 Gustav Roethe, 1859-1926, Germanist.",
        "Verfaßte auch nationa- listische politische Flugschriften und hielt solche Reden.",
        "Nach seinem Tode erschienen «Deutsche Reden», 1927. 215 Diese Hochschule heißt..."
      ],
      [
        "Goetheanum: Am 18.",
        "Oktober 1917 sagte Rudolf Steiner - vollkommen überraschend auch für die anwesenden Anthroposophen, denen der Dornacher Bau «Jö- hannesbau» hieß - in einem öffentlichen Vortrag in Basel: «Ich möchte die Weltanschauung, welche auf die Art wissenschaftlich entsteht, wie ich es angedeutet habe... nach den Quellen, aus denen sie für mich selber stammt ... am liebsten Goetheanismus nennen, so wie ich ... den Bau in Dornach draußen, der dieser Weltanschauung gewidmet ist, am liebsten Goetheanum nennen würde...» 216 Ich habe neulich ein Stück aus einem Feuilleton vorgelesen: Aus dem Jahrbuch von Elsbeth Ebertin, «Ein Blick in die Zukunft», Freiburg i."
      ],
      [
        "Br. 1921, S. 63; siehe hierzu auch die Ausführungen Rudolf Steiners in dem Dornacher Vortrag vom 23.",
        "Januar 1921 «Weltwirtschaftsgedanken im Chaos der Gegenwart vom Aspekt der"
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
