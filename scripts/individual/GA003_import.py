#!/usr/bin/env python3
"""Standalone import script for GA003 — GA003 - Wahrheit und Wissenschaft (1892)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA003 - Wahrheit und Wissenschaft (1892)"""
GA_NUMBER = "GA003"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "VORREDE",
    "paragraphs": [
      "Die Philosophie der Gegenwart leidet an einem ungesun­den Kant-Glauben. Die vorliegende Schrift soll ein Beitrag zu seiner Überwindung sein. Frevelhaft wäre es, die un­sterblichen Verdienste dieses Mannes um die Entwickelung der deutschen Wissenschaft herabwürdigen zu wollen. Aber wir müssen endlich einsehen, daß wir nur dann den Grund zu einer wahrhaft befriedigenden Welt- und Lebensanschauung legen können, wenn wir uns in entschiedenen Gegensatz zu diesem Geiste stellen. Was hat Kant geleistet? Er hat gezeigt, daß der jenseits unserer Sinnen- und Ver­nunftwelt liegende Urgrund der Dinge, den seine Vorgän­ger mit Hilfe falsch verstandener Begriffsschablonen such­ten, für unser Erkenntnisvermögen unzugänglich ist. Daraus hat er gefolgert, daß unser wissenschaftliches Bestreben sich innerhalb des erfahrungsmäßig Erreichbaren halten müsse und an die Erkenntnis des übersinnlichen Urgrundes, des Dinges an sich», nicht herankommen könne. Wie aber, wenn dieses « Ding an sich » samt dem jenseitigen Urgrund der Dinge nur ein Phantom wäre! Leicht ist einzusehen, daß sich die Sache so verhält. Nach dem tiefsten Wesen der Dinge, nach den Urprinzipien derselben zu forschen, ist ein von der Menschennatur untrennbarer Trieb. Er liegt allem wissenschaftlichen Treiben zugrunde.",
      "Nicht die geringste Veranlassung aber ist, diesen Ur­grund außerhalb  der uns gegebenen sinnlichen und geistigen Welt zu suchen, solange nicht ein allseitiges Durchforschen dieser Welt ergibt, daß sich innerhalb derselben Elemente finden, die deutlich auf einen Einfluß von außen hinweisen.",
      "Unsere Schrift sucht nun den Beweis zu führen, daß für",
      "unser Denken alles erreichbar ist, was zur Erklärung und Ergründung der Welt herbeigezogen werden muß. Die An­nahme von außerhalb unserer Welt liegenden Prinzipien derselben zeigt sich als das Vorurteil einer abgestorbenen, in eitlem Dogmenwahn lebenden Philosophie.",
      "Zu diesem Ergebnisse hätte Kant kommen müssen, wenn er wirklich untersucht hätte, wozu unser Denken veranlagt ist. Statt dessen bewies er in der umständlichsten Art, daß wir zu den letzten Prinzipien, die jenseits unserer Erfahrung lie­gen, wegen der Einrichtung unseres Erkenntnisvermögens nicht gelangen können.",
      "Vernünftigerweise dürfen wir sie aber gar nicht in ein solches Jenseits verlegen. Kant hat wohl die « dogmatische » Philosophie widerlegt, aber er hat nichts an deren Stelle gesetzt. Die zeitlich an ihn anknüp­fende deutsche Philosophie entwickelte sich daher überall im Gegensatz zu Kant.",
      "Fichte, Schelling, Hegel kümmerten sich nicht weiter um die von ihrem Vorgänger abgesteckten Grenzen unseres Erkennens und suchten die Urprinzipien der Dinge innerhalb des Diesseits der menschlichen Ver­nunft. Selbst Schopenhauer, der doch behauptet, die Resul­tate der Kantschen Vernunftkritik seien ewig unumstöß­liche Wahrheiten, kann nicht umhin, von denen seines Meisters abweichende Wege zur Erkenntnis der letzten Weltursachen einzuschlagen.",
      "Das Verhängnis dieser Denker war, daß sie Erkenntnisse der höchsten Wahrheiten such­ten, ohne für solches Beginnen durch eine Untersuchung der Natur des Erkennens selbst den Grund gelegt zu haben. Die stolzen Gedankengebäude Fichtes, Schellings und He­gels stehen daher ohne Fundament da.",
      "Der Mangel eines solchen wirkte aber auch schädigend auf die Gedanken­gänge der Philosophen. Ohne Kenntnis der Bedeutung der",
      "reinen Ideenwelt und ihrer Beziehung zum Gebiet der Sinneswahmehmung bauten dieselben Irrtum auf Irrtum, Einseitigkeit auf Einseitigkeit. Kein Wunder, daß die all­zukühnen Systeme den Stürmen einer philosophiefeind­lichen Zeit nicht zu trotzen vermochten, und viel Gutes, das sie enthielten, mit dem Schlechten erbarmungslos hin­weggeweht worden ist.",
      "Einem hiemit angedeuteten Mangel sollen die folgenden Untersuchungen abhelfen. Nicht wie Kant es tat, wollen sie darlegen, was das Erkenntnisvermögen nicht vermag; son­dern ihr Zweck ist, zu zeigen, was es wirklich imstande ist.",
      "Das Resultat dieser Untersuchungen ist, daß die Wahr­heit nicht, wie man gewöhnlich annimmt, die ideelle Abspiegelung von irgendeinem Realen ist, sondern ein freies Erzeugnis des Menschengeistes, das überhaupt nirgends existierte, wenn wir es nicht selbst hervorbrächten. Die Aufgabe der Erkenntnis ist nicht: etwas schon anderwärts Vorhandenes in begrifflicher Form zu wiederholen, sondern die: ein ganz neues Gebiet zu schaffen, das mit der sinnenfällig gegebenen Welt zusammen erst die volle Wirklichkeit ergibt. Damit ist die höchste Tätigkeit des Menschen, sein geistiges Schaffen, organisch dem allgemeinen Weltgesche­hen eingegliedert. Ohne diese Tätigkeit wäre das Welt­geschehen gar nicht als in sich abgeschlossene Ganzheit zu denken. Der Mensch ist dem Weltlauf gegenüber nicht ein müßiger Zuschauer, der innerhalb seines Geistes das bildlich wiederholt, was sich ohne sein Zutun im Kosmos vollzieht, sondern der tätige Mitschöpfer des Weltprozesses; und das Erkennen ist das vollendetste Glied im Organismus des Universums.",
      "Für die Gesetze unseres Handelns, für unsere sittlichen",
      "Ideale hat diese Anschauung die wichtige Konsequenz, daß auch diese nicht als das Abbild von etwas außer uns Befind­lichem angesehen werden können, sondern als ein nur in uns Vorhandenes. Eine Macht, als deren Gebote wir unsere Sittengesetze ansehen müßten, ist damit ebenfalls abge­wiesen. Einen « kategorischen Imperativ», gleichsam eine Stimme aus dem Jenseits, die uns vorschriebe, was wir zu tun oder zu lassen haben, kennen wir nicht. Unsere sitt­lichen Ideale sind unser eigenes freies Erzeugnis. Wir haben nur auszuführen, was wir uns selbst als Norm unseres Han­delns vorschreiben. Die Anschauung von der Wahrheit als Freiheitstat begründet somit auch eine Sittenlehre, deren Grundlage die vollkommen freie Persönlichkeit ist.",
      "Diese Sätze gelten natürlich nur von jenem Teil unseres Handelns, dessen Gesetze wir in vollkommener Erkenntnis ideell durchdringen. Solange die letzteren bloß natürliche oder begrifflich noch unklare Motive sind, kann wohl ein geistig Höherstehender erkennen, inwiefern diese Gesetze unseres Tuns innerhalb unserer Individualität begründet sind, wir selbst aber empfinden sie als von außen auf uns wirkend, uns zwingend. Jedesmal, wenn es uns gelingt, ein solches Motiv klar erkennend zu durchdringen, machen wir eine Eroberung im Gebiet der Freiheit.",
      "Wie sich unsere Anschauungen zu der bedeutendsten phi­losophischen Erscheinung der Gegenwart, zur Weltauffas­sung Eduard von Hartmanns, verhalten, wird der Leser aus unserer Schrift in ausführlicher Weise, soweit das Er­kenntnisproblem in Frage kommt, ersehen.",
      "Eine Philosophie der Freiheit? ist es, wozu wir mit dem Gegenwärtigen ein Vorspiel geschaffen haben. Diese selbst in ausführlicher Gestalt soll bald nachfolgen.",
      "Die Erhöhung des Daseinswertes der menschlichen Per­sönlichkeit ist doch das Endziel aller Wissenschaft. Wer letztere nicht in dieser Absicht betreibt, der arbeitet nur, weil er von seinem Meister solches gesehen hat, er « forscht», weil er das gerade zufällig gelernt hat. Ein « freier Denker kann er nicht genannt werden.",
      "Was den Wissenschaften erst den wahren Wert verleiht, ist die philosophische Darlegung der menschlichen Bedeu­tung ihrer Resultate. Einen Beitrag zu dieser Darlegung wollte ich liefern. Aber vielleicht verlangt die Wissenschaft der Gegenwart gar nicht nach ihrer philosophischen Recht­fertigung! Dann ist zweierlei gewiß: erstens, daß ich eine unnötige Schrift geliefert habe, zweitens, daß die moderne Gelehrsamkeit im Trüben fischt und nicht weiß, was sie will.",
      "Am Schlusse dieser Vorrede kann ich eine persönliche Be­merkung nicht unterdrücken. Ich habe meine philosophischen Anschauungen bisher immer anknüpfend an die Goethe­sche Weltanschauung dargelegt, in die ich durch meinen über alles verehrten Lehrer Karl Julius Schröer zuerst ein­geführt worden bin, der mir in der Goetheforschung so hoch steht, weil sein Blick immer über das Einzelne hinaus auf die Ideen geht.",
      "Mit dieser Schrift hoffe ich aber nun gezeigt zu haben, daß mein Gedankengebäude eine in sich selbst begründete Ganzheit ist, die nicht aus der Goetheschen Weltanschauung abgeleitet zu werden braucht. Meine Gedanken, wie sie hier vorliegen und weiter als «Philosophie der Freiheit» nachfolgen werden, sind im Laufe vieler Jahre entstanden. Und es geht nur aus einem tiefen Dankesgefühl hervor, wenn ich noch sage, daß die liebevolle Art, mit der mir das",
      "Haus Specht in Wien entgegenkam während der Zeit, in der ich die Erziehung der Kinder desselben zu besorgen hatte, ein einzig wünschenswertes «Milieu» zum Ausbau meiner Ideen darbot; ferner daß ich die Stimmung zum letzten Abrunden manches Gedankens meiner vorläufig auf S.86 bis 88 keimartig skizzierten «Freiheitsphilosophie» den anregenden Gesprächen mit meiner hochgeschätzten Freundin Rosa Mayreder in Wien verdanke, deren literari­sche Arbeiten, die aus einer feinsinnigen, vornehmen Künst­lernatur entspringen, voraussichtlich bald der Öffentlichkeit übergeben sein werden.",
      "Geschrieben zu Wien, Anfang Dezember 1891.",
      "Dr. Rudolf Steiner"
    ],
    "sentences": [
      [
        "Die Philosophie der Gegenwart leidet an einem ungesun­den Kant-Glauben.",
        "Die vorliegende Schrift soll ein Beitrag zu seiner Überwindung sein.",
        "Frevelhaft wäre es, die un­sterblichen Verdienste dieses Mannes um die Entwickelung der deutschen Wissenschaft herabwürdigen zu wollen.",
        "Aber wir müssen endlich einsehen, daß wir nur dann den Grund zu einer wahrhaft befriedigenden Welt- und Lebensanschauung legen können, wenn wir uns in entschiedenen Gegensatz zu diesem Geiste stellen.",
        "Was hat Kant geleistet?",
        "Er hat gezeigt, daß der jenseits unserer Sinnen- und Ver­nunftwelt liegende Urgrund der Dinge, den seine Vorgän­ger mit Hilfe falsch verstandener Begriffsschablonen such­ten, für unser Erkenntnisvermögen unzugänglich ist.",
        "Daraus hat er gefolgert, daß unser wissenschaftliches Bestreben sich innerhalb des erfahrungsmäßig Erreichbaren halten müsse und an die Erkenntnis des übersinnlichen Urgrundes, des Dinges an sich», nicht herankommen könne.",
        "Wie aber, wenn dieses « Ding an sich » samt dem jenseitigen Urgrund der Dinge nur ein Phantom wäre!",
        "Leicht ist einzusehen, daß sich die Sache so verhält.",
        "Nach dem tiefsten Wesen der Dinge, nach den Urprinzipien derselben zu forschen, ist ein von der Menschennatur untrennbarer Trieb.",
        "Er liegt allem wissenschaftlichen Treiben zugrunde."
      ],
      [
        "Nicht die geringste Veranlassung aber ist, diesen Ur­grund außerhalb der uns gegebenen sinnlichen und geistigen Welt zu suchen, solange nicht ein allseitiges Durchforschen dieser Welt ergibt, daß sich innerhalb derselben Elemente finden, die deutlich auf einen Einfluß von außen hinweisen."
      ],
      [
        "Unsere Schrift sucht nun den Beweis zu führen, daß für"
      ],
      [
        "unser Denken alles erreichbar ist, was zur Erklärung und Ergründung der Welt herbeigezogen werden muß.",
        "Die An­nahme von außerhalb unserer Welt liegenden Prinzipien derselben zeigt sich als das Vorurteil einer abgestorbenen, in eitlem Dogmenwahn lebenden Philosophie."
      ],
      [
        "Zu diesem Ergebnisse hätte Kant kommen müssen, wenn er wirklich untersucht hätte, wozu unser Denken veranlagt ist.",
        "Statt dessen bewies er in der umständlichsten Art, daß wir zu den letzten Prinzipien, die jenseits unserer Erfahrung lie­gen, wegen der Einrichtung unseres Erkenntnisvermögens nicht gelangen können."
      ],
      [
        "Vernünftigerweise dürfen wir sie aber gar nicht in ein solches Jenseits verlegen.",
        "Kant hat wohl die « dogmatische » Philosophie widerlegt, aber er hat nichts an deren Stelle gesetzt.",
        "Die zeitlich an ihn anknüp­fende deutsche Philosophie entwickelte sich daher überall im Gegensatz zu Kant."
      ],
      [
        "Fichte, Schelling, Hegel kümmerten sich nicht weiter um die von ihrem Vorgänger abgesteckten Grenzen unseres Erkennens und suchten die Urprinzipien der Dinge innerhalb des Diesseits der menschlichen Ver­nunft.",
        "Selbst Schopenhauer, der doch behauptet, die Resul­tate der Kantschen Vernunftkritik seien ewig unumstöß­liche Wahrheiten, kann nicht umhin, von denen seines Meisters abweichende Wege zur Erkenntnis der letzten Weltursachen einzuschlagen."
      ],
      [
        "Das Verhängnis dieser Denker war, daß sie Erkenntnisse der höchsten Wahrheiten such­ten, ohne für solches Beginnen durch eine Untersuchung der Natur des Erkennens selbst den Grund gelegt zu haben.",
        "Die stolzen Gedankengebäude Fichtes, Schellings und He­gels stehen daher ohne Fundament da."
      ],
      [
        "Der Mangel eines solchen wirkte aber auch schädigend auf die Gedanken­gänge der Philosophen.",
        "Ohne Kenntnis der Bedeutung der"
      ],
      [
        "reinen Ideenwelt und ihrer Beziehung zum Gebiet der Sinneswahmehmung bauten dieselben Irrtum auf Irrtum, Einseitigkeit auf Einseitigkeit.",
        "Kein Wunder, daß die all­zukühnen Systeme den Stürmen einer philosophiefeind­lichen Zeit nicht zu trotzen vermochten, und viel Gutes, das sie enthielten, mit dem Schlechten erbarmungslos hin­weggeweht worden ist."
      ],
      [
        "Einem hiemit angedeuteten Mangel sollen die folgenden Untersuchungen abhelfen.",
        "Nicht wie Kant es tat, wollen sie darlegen, was das Erkenntnisvermögen nicht vermag; son­dern ihr Zweck ist, zu zeigen, was es wirklich imstande ist."
      ],
      [
        "Das Resultat dieser Untersuchungen ist, daß die Wahr­heit nicht, wie man gewöhnlich annimmt, die ideelle Abspiegelung von irgendeinem Realen ist, sondern ein freies Erzeugnis des Menschengeistes, das überhaupt nirgends existierte, wenn wir es nicht selbst hervorbrächten.",
        "Die Aufgabe der Erkenntnis ist nicht: etwas schon anderwärts Vorhandenes in begrifflicher Form zu wiederholen, sondern die: ein ganz neues Gebiet zu schaffen, das mit der sinnenfällig gegebenen Welt zusammen erst die volle Wirklichkeit ergibt.",
        "Damit ist die höchste Tätigkeit des Menschen, sein geistiges Schaffen, organisch dem allgemeinen Weltgesche­hen eingegliedert.",
        "Ohne diese Tätigkeit wäre das Welt­geschehen gar nicht als in sich abgeschlossene Ganzheit zu denken.",
        "Der Mensch ist dem Weltlauf gegenüber nicht ein müßiger Zuschauer, der innerhalb seines Geistes das bildlich wiederholt, was sich ohne sein Zutun im Kosmos vollzieht, sondern der tätige Mitschöpfer des Weltprozesses; und das Erkennen ist das vollendetste Glied im Organismus des Universums."
      ],
      [
        "Für die Gesetze unseres Handelns, für unsere sittlichen"
      ],
      [
        "Ideale hat diese Anschauung die wichtige Konsequenz, daß auch diese nicht als das Abbild von etwas außer uns Befind­lichem angesehen werden können, sondern als ein nur in uns Vorhandenes.",
        "Eine Macht, als deren Gebote wir unsere Sittengesetze ansehen müßten, ist damit ebenfalls abge­wiesen.",
        "Einen « kategorischen Imperativ», gleichsam eine Stimme aus dem Jenseits, die uns vorschriebe, was wir zu tun oder zu lassen haben, kennen wir nicht.",
        "Unsere sitt­lichen Ideale sind unser eigenes freies Erzeugnis.",
        "Wir haben nur auszuführen, was wir uns selbst als Norm unseres Han­delns vorschreiben.",
        "Die Anschauung von der Wahrheit als Freiheitstat begründet somit auch eine Sittenlehre, deren Grundlage die vollkommen freie Persönlichkeit ist."
      ],
      [
        "Diese Sätze gelten natürlich nur von jenem Teil unseres Handelns, dessen Gesetze wir in vollkommener Erkenntnis ideell durchdringen.",
        "Solange die letzteren bloß natürliche oder begrifflich noch unklare Motive sind, kann wohl ein geistig Höherstehender erkennen, inwiefern diese Gesetze unseres Tuns innerhalb unserer Individualität begründet sind, wir selbst aber empfinden sie als von außen auf uns wirkend, uns zwingend.",
        "Jedesmal, wenn es uns gelingt, ein solches Motiv klar erkennend zu durchdringen, machen wir eine Eroberung im Gebiet der Freiheit."
      ],
      [
        "Wie sich unsere Anschauungen zu der bedeutendsten phi­losophischen Erscheinung der Gegenwart, zur Weltauffas­sung Eduard von Hartmanns, verhalten, wird der Leser aus unserer Schrift in ausführlicher Weise, soweit das Er­kenntnisproblem in Frage kommt, ersehen."
      ],
      [
        "Eine Philosophie der Freiheit? ist es, wozu wir mit dem Gegenwärtigen ein Vorspiel geschaffen haben.",
        "Diese selbst in ausführlicher Gestalt soll bald nachfolgen."
      ],
      [
        "Die Erhöhung des Daseinswertes der menschlichen Per­sönlichkeit ist doch das Endziel aller Wissenschaft.",
        "Wer letztere nicht in dieser Absicht betreibt, der arbeitet nur, weil er von seinem Meister solches gesehen hat, er « forscht», weil er das gerade zufällig gelernt hat.",
        "Ein « freier Denker kann er nicht genannt werden."
      ],
      [
        "Was den Wissenschaften erst den wahren Wert verleiht, ist die philosophische Darlegung der menschlichen Bedeu­tung ihrer Resultate.",
        "Einen Beitrag zu dieser Darlegung wollte ich liefern.",
        "Aber vielleicht verlangt die Wissenschaft der Gegenwart gar nicht nach ihrer philosophischen Recht­fertigung!",
        "Dann ist zweierlei gewiß: erstens, daß ich eine unnötige Schrift geliefert habe, zweitens, daß die moderne Gelehrsamkeit im Trüben fischt und nicht weiß, was sie will."
      ],
      [
        "Am Schlusse dieser Vorrede kann ich eine persönliche Be­merkung nicht unterdrücken.",
        "Ich habe meine philosophischen Anschauungen bisher immer anknüpfend an die Goethe­sche Weltanschauung dargelegt, in die ich durch meinen über alles verehrten Lehrer Karl Julius Schröer zuerst ein­geführt worden bin, der mir in der Goetheforschung so hoch steht, weil sein Blick immer über das Einzelne hinaus auf die Ideen geht."
      ],
      [
        "Mit dieser Schrift hoffe ich aber nun gezeigt zu haben, daß mein Gedankengebäude eine in sich selbst begründete Ganzheit ist, die nicht aus der Goetheschen Weltanschauung abgeleitet zu werden braucht.",
        "Meine Gedanken, wie sie hier vorliegen und weiter als «Philosophie der Freiheit» nachfolgen werden, sind im Laufe vieler Jahre entstanden.",
        "Und es geht nur aus einem tiefen Dankesgefühl hervor, wenn ich noch sage, daß die liebevolle Art, mit der mir das"
      ],
      [
        "Haus Specht in Wien entgegenkam während der Zeit, in der ich die Erziehung der Kinder desselben zu besorgen hatte, ein einzig wünschenswertes «Milieu» zum Ausbau meiner Ideen darbot; ferner daß ich die Stimmung zum letzten Abrunden manches Gedankens meiner vorläufig auf S.86 bis 88 keimartig skizzierten «Freiheitsphilosophie» den anregenden Gesprächen mit meiner hochgeschätzten Freundin Rosa Mayreder in Wien verdanke, deren literari­sche Arbeiten, die aus einer feinsinnigen, vornehmen Künst­lernatur entspringen, voraussichtlich bald der Öffentlichkeit übergeben sein werden."
      ],
      [
        "Geschrieben zu Wien, Anfang Dezember 1891."
      ],
      [
        "Rudolf Steiner"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "EINLEITUNG",
    "paragraphs": [
      "GA003 - Wahrheit und Wissenschaft",
      "Die folgenden Erörterungen haben die Aufgabe, durch eine auf die letzten Elemente zurückgehende Analyse des Er­kenntnisaktes das Erkenntnisproblem richtig zu formulie­ren und den Weg zu einer Lösung desselben anzugeben. Sie zeigen durch eine Kritik der auf Kantschem Gedankengange fußenden Erkenntnistheorien, daß von diesem Standpunkte aus niemals eine Lösung der einschlägigen Fragen möglich sein wird.",
      "Dabei ist allerdings anzuerkennen, daß ohne die grundlegenden Vorarbeiten Volkelts («Erfahrung und Den­ken. Kritische Grundlegung der Erkenntnistheorie», von Johannes Volkelt. Hamburg und Leipzig 1886) mit ihren gründlichen Untersuchungen über den Erfahrungsbegriff die präzise Fassung des Begriffes des « Gegebenen », wie wir sie versuchen, sehr erschwert worden wäre.",
      "Wir geben uns aber der Hoffnung hin, daß wir zu einer Überwindung des Sub­jektivismus, der den von Kant ausgehenden Erkenntnistheorien anhaftet, den Grund gelegt haben. Und zwar glau­ben wir dies durch unseren Nachweis getan zu haben, daß die subjektive Form, in welcher das Weltbild vor der Be­arbeitung desselben durch die Wissenschaft für den Er­kenntnisakt auftritt, nur eine notwendige Durchgangsstufe ist, die aber im Erkenntnisprozesse selbst überwunden wird.",
      "Uns gilt die sogenannte Erfahrung, die der Positivismus und der Neukantianismus so gerne als das einzig Gewisse hinstellen möchten, gerade für das Subjektivste. Und indem wir dieses zeigen, begründen wir den objektiven Idealismus als notwendige Folge einer sich selbst verstehenden Er­kenntnistheorie.",
      "Derselbe unterscheidet sich von dem Hegel­schen metaphysischen, absoluten Idealismus dadurch, daß",
      "er den Grund für die Spaltung der Wirklichkeit in gegebe­nes Sein und Begriff im Erkenntnissubjekt sucht und die Vermittlung derselben nicht in einer objektiven Weltdia­lektik, sondern im subjektiven Erkenntnisprozesse sieht. Der Schreiber dieser Zeilen hat diesen Standpunkt schon einmal auf Grund von Untersuchungen, die sich in der Methode von den vorliegenden freilich wesentlich unter­scheiden, und denen auch das Zurückgehen auf die ersten Elemente des Erkennens fehlt, im Jahre 1885 in seinen « Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung »* schriftstellerisch vertreten.",
      "Die neuere Literatur, die für diese Erörterungen in Be­tracht kommt, ist folgende. Wir führen dabei nicht nur das­jenige an, worauf unsere Darstellung unmittelbar Bezug hat, sondern auch alle jene Schriften, in denen Fragen be­handelt werden, die den von uns erörterten ähnlich sind. Von einer besonderen Anführung der Schriften der eigent­lichen philosophischen Klassiker sehen wir ab.",
      "Für die Erkenntnistheorie im allgemeinen kommen in Betracht:",
      "R.    Avenarius, Philosophie als Denken der Welt gemäß dem Prinzip des kleinsten Kraftmaßes usw.; Leipzig 1876",
      "Kritik der reinen Erfahrung; 1. Bd. Leipzig 1888",
      "J.    F. A. Bahnsen, Der Widerspruch im Wissen und Wesen der Welt; 1. Bd. Leipzig 1882",
      "J.    Baumann, Philosophie als Orientierung über die Welt; Leipzig 1872",
      "J.    S. Beck, Einzig möglicher Standpunkt, aus welchem die kritische Philosophie beurteilt werden muß; Riga 1796",
      "-016-*    Letzte Ausgabe Freiburg i. Br. 1948.",
      "F.    E. Beneke, System der Metaphysik und Religionsphilo­sophie usw.; Berlin 1839",
      "Julius Bergmann, Sein und Erkennen usw.; Berlin 1880 A. E. Biedermann, Christliche Dogmatik; 2. Aufl. Berlin 1884/85",
      "H.    Cohen, Kants Theorie der Erfahrung; Berlin 1871",
      "P.    Deussen, Die Elemente der Metaphysik; 2. Auflage, Leipzig 1890",
      "W.    Dilthey, Einleitung in die Geisteswissenschaften usw.; Leipzig 1883. - Besonders die einleitenden Kapitel, welche das Verhältnis der Erkenntnistheorie zu den übrigen Wissenschaften behandeln. - Ferner käme vom gleichen Verfasser auch noch in Betracht: Beiträge zur Lösung der Frage vom Ursprung unseres Glaubens an die Realität der Außenwelt und seinem Recht; Sitzungsberichte der Kgl. Preuß. Akademie der Wissenschaften zu Berlin, Berlin 1890, S.977",
      "A.    Dorner, Das menschliche Erkennen usw.; Berlin 1887",
      "E.    Dreher, Über Wahrnehmung und Denken; Berlin 1878",
      "G.    Engel, Sein und Denken; Berlin 1889",
      "W.    Enoch, Der Begriff der Wahrnehmung; Hamburg 1890",
      "B.    Erdmann, Kants Kriticismus in der ersten und zweiten Auflage seiner Kritik der reinen Vernunft; Leipzig 1878",
      "F.    v. Feldegg, Das Gefühl als Fundament der Weltordnung; Wien 1890",
      "E.    L. Fischer, Die Grundfragen der Erkenntnistheorie; Mainz 1887",
      "K.    Fischer, System der Logik und Metaphysik oder Wissen­schaftslehre; 2. Auflage, Heidelberg 1865",
      "Geschichte der neueren Philosophie; Mannheim 1860 (be­sonders die auf Kant bezüglichen Teile)",
      "A.    Ganser, Die Wahrheit; Graz 1890",
      "C.    Göring, System der kritischen Philosophie; Leipzig 1874 Über den Begriff der Erfahrung; Vierteljahrsschrift für wissenschaftliche Philosophie; Leipzig 1. Jg. 1877, S.384",
      "E.    Grimm, Zur Geschichte des Erkenntnisproblems usw.; Leipzig 1890",
      "F.    Grung, Das Problem der Gewißheit; Heidelberg 1886",
      "R.    Hamerling, Die Atomistik des Willens; Hamburg 1891",
      "F.    Harms, Die Philosophie seit Kant; Berlin 1876",
      "E.    v. Hartmann, Kritische Grundlegung des transzenden­talen Realismus; 2. Aufl. Berlin 1875",
      "J. H. v. Kirchmanns erkenntnistheoretischer Realismus; Berlin 1875",
      "Das Grundproblem der Erkenntnistheorie usw.; Leipzig",
      "Kritische Wanderungen durch die Philosophie der Gegen­wart; Leipzig 1889",
      "H.    L. F. v. Helmholtz, Die Tatsachen in der Wahrneh­mung; Berlin 1879",
      "G.    Heymans, Die Gesetze und Elemente des wissenschaft­lichen Denkens; Leyden 1890",
      "A.    Hölder, Darstellung der Kantischen Erkenntnistheorie; Tübingen 1874",
      "A.    Horwicz, Analyse des Denkens usw.; Halle 1875",
      "F.    H. Jacobi, David Hume über den Glauben oder Idealis­mus und Realismus; Breslau 1787",
      "M.    Kappes, Der « Common Sense » als Prinzip der Gewiß­heit in der Philosophie des Schotten Thomas Reid; Mün­chen 1890",
      "M.    Kauffmann, Fundamente der Erkenntnistheorie und Wissenschaftslehre; Leipzig 1890",
      "B.    Kerry, System einer Theorie der Grenzgebiete; Wien 1890",
      "J.    H. v. Kirchmann, Die Lehre vom Wissen als Einleitung in das Studium philosophischer Werke; Berlin 1868",
      "E.    Laas, Die Kausalität des Ich; Vierteljahrsschrift für wis­senschaftliche Philosophie; Leipzig, 4. Jahrgang (1880) S.1 ff, 185ff, 311 ff Idealismus und Positivismus; Berlin 1879",
      "FA. Lange, Geschichte des Materialismus; Iserlohn 1873/75",
      "A. v. Leclair, Beiträge zu einer monistischen Erkenntnis­theorie; Breslau 1882",
      "Das kategorische Gepräge des Denkens; Vierteljahrs­schrift für wissenschaftliche Philosophie, Leipzig, 7.Jahr-gang (1883) S.257 ff",
      "0.    Liebmann, Kant und die Epigonen; Stuttgart 1865",
      "Zur Analysis der Wirklichkeit; Straßburg 1880",
      "Gedanken und Tatsachen; Straßburg 1882",
      "Die Klimax der Theorien; Straßburg 1884",
      "Th. Lipps, Grundtatsachen des Seelenlebens; Bonn 1883 H. R. Lotze, System der Philosophie, 1. Teil: Logik; Leip­zig 1874",
      "J.    V. Mayer, Vom Erkennen; Freiburg i. Br. 1885",
      "A.    Meinong, Hume-Studien; Wien 1877",
      "J.    St. Mill, System der induktiven und deduktiven Logik; 1843; deutsch Braunschweig 1849",
      "W.    Münz, Die Grundlagen der Kantschen Erkenntnistheorie; 2. Auflage, Breslau 1885",
      "G.    Neudecker, Das Grundproblem der Erkenntnistheorie; Nördlingen 1881",
      "F.    Paulsen, Versuch einer Entwicklungsgeschichte der Kant­schen Erkenntnistheorie; Leipzig 1875",
      "J.    Rehmke, Die Welt als Wahrnehmung und Begriff usw.; Berlin 1880",
      "Th. Reid, Untersuchungen über den menschlichen Geist nach Prinzipien des gesunden Menschenverstandes; 1764, deutsch Leipzig 1782",
      "A.    Riehl, Der philosophische Kritizismus und seine Be­deutung für die positive Wissenschaft; Leipzig 1887",
      "J.    Rülf, Wissenschaft des Weltgedankens und der Gedan­kenwelt, System einer neuen Metaphysik; Leipzig 1888",
      "R.    v. Schubert-Soldern, Grundlagen einer Erkenntnistheo­rie; Leipzig 1884",
      "G.    E. Schulze, Aenesidemus; Helmstädt 1792 W. Schuppe, Zur voraussetzungslosen Erkenntnistheorie; Philosophische Monatshefte, Berlin, Leipzig, Heidelberg 1882, Band XVIII, Heft 6 u. 7",
      "R.    Seydel, Logik oder Wissenschaft vom Wissen; Leipzig 1866",
      "Christoph v. Sigwart, Logik; Freiburg i. Br. 1878",
      "A.    Stadler, Die Grundsätze der reinen Erkenntnistheorie in der Kantischen Philosophie; Leipzig 1876",
      "H.    Taine, De l'Intelligence; 5. Auflage, Paris 1888",
      "A.    Trendelenburg, Logische Untersuchungen; Leipzig 1862",
      "F.    Ueberweg, System der Logik; 3. Auflage, Bonn 1882",
      "H. Vaihinger, Hartmann, Dühring und Lange; Iserlohn 1876",
      "Th. Vambühler, Widerlegung der Kritik der reinen Ver­nunft; Leipzig 1890",
      "J.    Volkelt, Immanuel Kants Erkenntnistheorie usw.; Ham­burg 1879 Erfahrung und Denken; Hamburg 1886 R. Wahle, Gehirn und Bewußtsein; Wien 1884",
      "W.    Windelband, Präludien; Freiburg i. Br. 1884",
      "Die verschiedenen Phasen der Kantschen Lehre vom « Ding an sich»; Vierteljahrsschrift für wissenschaftliche Philosophie, Leipzig, 1.Jahrgang (1877), S.224 ff",
      "J.    H. Witte, Beiträge zum Verständnis Kants; Berlin 1874 Vorstudien zur Erkenntnis des unerfahrbaren Seins;",
      "H.    Wolff, Über den Zusammenhang unserer Vorstellungen mit den Dingen außer uns; Leipzig 1874",
      "J.    Wolff, Das Bewußtsein und sein Objekt; Berlin 1889",
      "W.    Wundt, Logik, 1. Bd.: Erkenntnislehre; Stuttgart 1880",
      "Für Fichte kommen in Betracht:",
      "F. C. Biedermann, De Genetica philosophandi ratione et methodo, praesertim Fichtii, Schellingii, Hegelii, Disser­tationis particula prima, syntheticam Fichtii methodum exhibens usw.; Lipsiae 1835",
      "F. Frederichs, Der Freiheitsbegriff Kants und Fichtes; Ber­lin 1886",
      "O. Gühlhof, Der transcendentale Idealismus; Halle 1888",
      "P. Hensel, Über die Beziehung des reinen Ich bei Fichte zur Einheit der Apperception bei Kant; Freiburg i. Br. 1885",
      "G. Schwabe, Fichtes und Schopenhauers Lehre vom Willen mit ihren Consequenzen für Weltbegreifung und Lebens­führung; Jena 1887",
      "Die zahlreichen zum Fichte-Jubiläum 1862 erschienenen Schriften finden natürlich hier keine Berücksichtigung. Höchstens die Rede Trendelenburgs (A. Trendelenburg, Zur Erinnerung an J. G. Fichte; Berlin 1862), welche wich­tigere theoretische Gesichtspunkte enthält, möge erwähnt werden."
    ],
    "sentences": [
      [
        "GA003 - Wahrheit und Wissenschaft"
      ],
      [
        "Die folgenden Erörterungen haben die Aufgabe, durch eine auf die letzten Elemente zurückgehende Analyse des Er­kenntnisaktes das Erkenntnisproblem richtig zu formulie­ren und den Weg zu einer Lösung desselben anzugeben.",
        "Sie zeigen durch eine Kritik der auf Kantschem Gedankengange fußenden Erkenntnistheorien, daß von diesem Standpunkte aus niemals eine Lösung der einschlägigen Fragen möglich sein wird."
      ],
      [
        "Dabei ist allerdings anzuerkennen, daß ohne die grundlegenden Vorarbeiten Volkelts («Erfahrung und Den­ken.",
        "Kritische Grundlegung der Erkenntnistheorie», von Johannes Volkelt.",
        "Hamburg und Leipzig 1886) mit ihren gründlichen Untersuchungen über den Erfahrungsbegriff die präzise Fassung des Begriffes des « Gegebenen », wie wir sie versuchen, sehr erschwert worden wäre."
      ],
      [
        "Wir geben uns aber der Hoffnung hin, daß wir zu einer Überwindung des Sub­jektivismus, der den von Kant ausgehenden Erkenntnistheorien anhaftet, den Grund gelegt haben.",
        "Und zwar glau­ben wir dies durch unseren Nachweis getan zu haben, daß die subjektive Form, in welcher das Weltbild vor der Be­arbeitung desselben durch die Wissenschaft für den Er­kenntnisakt auftritt, nur eine notwendige Durchgangsstufe ist, die aber im Erkenntnisprozesse selbst überwunden wird."
      ],
      [
        "Uns gilt die sogenannte Erfahrung, die der Positivismus und der Neukantianismus so gerne als das einzig Gewisse hinstellen möchten, gerade für das Subjektivste.",
        "Und indem wir dieses zeigen, begründen wir den objektiven Idealismus als notwendige Folge einer sich selbst verstehenden Er­kenntnistheorie."
      ],
      [
        "Derselbe unterscheidet sich von dem Hegel­schen metaphysischen, absoluten Idealismus dadurch, daß"
      ],
      [
        "er den Grund für die Spaltung der Wirklichkeit in gegebe­nes Sein und Begriff im Erkenntnissubjekt sucht und die Vermittlung derselben nicht in einer objektiven Weltdia­lektik, sondern im subjektiven Erkenntnisprozesse sieht.",
        "Der Schreiber dieser Zeilen hat diesen Standpunkt schon einmal auf Grund von Untersuchungen, die sich in der Methode von den vorliegenden freilich wesentlich unter­scheiden, und denen auch das Zurückgehen auf die ersten Elemente des Erkennens fehlt, im Jahre 1885 in seinen « Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung »* schriftstellerisch vertreten."
      ],
      [
        "Die neuere Literatur, die für diese Erörterungen in Be­tracht kommt, ist folgende.",
        "Wir führen dabei nicht nur das­jenige an, worauf unsere Darstellung unmittelbar Bezug hat, sondern auch alle jene Schriften, in denen Fragen be­handelt werden, die den von uns erörterten ähnlich sind.",
        "Von einer besonderen Anführung der Schriften der eigent­lichen philosophischen Klassiker sehen wir ab."
      ],
      [
        "Für die Erkenntnistheorie im allgemeinen kommen in Betracht:"
      ],
      [
        "Avenarius, Philosophie als Denken der Welt gemäß dem Prinzip des kleinsten Kraftmaßes usw.; Leipzig 1876"
      ],
      [
        "Kritik der reinen Erfahrung; 1.",
        "Leipzig 1888"
      ],
      [
        "Bahnsen, Der Widerspruch im Wissen und Wesen der Welt; 1.",
        "Leipzig 1882"
      ],
      [
        "Baumann, Philosophie als Orientierung über die Welt; Leipzig 1872"
      ],
      [
        "Beck, Einzig möglicher Standpunkt, aus welchem die kritische Philosophie beurteilt werden muß; Riga 1796"
      ],
      [
        "-016-* Letzte Ausgabe Freiburg i.",
        "Br. 1948."
      ],
      [
        "Beneke, System der Metaphysik und Religionsphilo­sophie usw.; Berlin 1839"
      ],
      [
        "Julius Bergmann, Sein und Erkennen usw.; Berlin 1880 A.",
        "Biedermann, Christliche Dogmatik; 2.",
        "Aufl.",
        "Berlin 1884/85"
      ],
      [
        "Cohen, Kants Theorie der Erfahrung; Berlin 1871"
      ],
      [
        "Deussen, Die Elemente der Metaphysik; 2.",
        "Auflage, Leipzig 1890"
      ],
      [
        "Dilthey, Einleitung in die Geisteswissenschaften usw.; Leipzig 1883. - Besonders die einleitenden Kapitel, welche das Verhältnis der Erkenntnistheorie zu den übrigen Wissenschaften behandeln. - Ferner käme vom gleichen Verfasser auch noch in Betracht: Beiträge zur Lösung der Frage vom Ursprung unseres Glaubens an die Realität der Außenwelt und seinem Recht; Sitzungsberichte der Kgl.",
        "Preuß.",
        "Akademie der Wissenschaften zu Berlin, Berlin 1890, S.977"
      ],
      [
        "Dorner, Das menschliche Erkennen usw.; Berlin 1887"
      ],
      [
        "Dreher, Über Wahrnehmung und Denken; Berlin 1878"
      ],
      [
        "Engel, Sein und Denken; Berlin 1889"
      ],
      [
        "Enoch, Der Begriff der Wahrnehmung; Hamburg 1890"
      ],
      [
        "Erdmann, Kants Kriticismus in der ersten und zweiten Auflage seiner Kritik der reinen Vernunft; Leipzig 1878"
      ],
      [
        "F. v.",
        "Feldegg, Das Gefühl als Fundament der Weltordnung; Wien 1890"
      ],
      [
        "Fischer, Die Grundfragen der Erkenntnistheorie; Mainz 1887"
      ],
      [
        "Fischer, System der Logik und Metaphysik oder Wissen­schaftslehre; 2.",
        "Auflage, Heidelberg 1865"
      ],
      [
        "Geschichte der neueren Philosophie; Mannheim 1860 (be­sonders die auf Kant bezüglichen Teile)"
      ],
      [
        "Ganser, Die Wahrheit; Graz 1890"
      ],
      [
        "Göring, System der kritischen Philosophie; Leipzig 1874 Über den Begriff der Erfahrung; Vierteljahrsschrift für wissenschaftliche Philosophie; Leipzig 1.",
        "Jg. 1877, S.384"
      ],
      [
        "Grimm, Zur Geschichte des Erkenntnisproblems usw.; Leipzig 1890"
      ],
      [
        "Grung, Das Problem der Gewißheit; Heidelberg 1886"
      ],
      [
        "Hamerling, Die Atomistik des Willens; Hamburg 1891"
      ],
      [
        "Harms, Die Philosophie seit Kant; Berlin 1876"
      ],
      [
        "E. v.",
        "Hartmann, Kritische Grundlegung des transzenden­talen Realismus; 2.",
        "Aufl.",
        "Berlin 1875"
      ],
      [
        "H. v.",
        "Kirchmanns erkenntnistheoretischer Realismus; Berlin 1875"
      ],
      [
        "Das Grundproblem der Erkenntnistheorie usw.; Leipzig"
      ],
      [
        "Kritische Wanderungen durch die Philosophie der Gegen­wart; Leipzig 1889"
      ],
      [
        "F. v.",
        "Helmholtz, Die Tatsachen in der Wahrneh­mung; Berlin 1879"
      ],
      [
        "Heymans, Die Gesetze und Elemente des wissenschaft­lichen Denkens; Leyden 1890"
      ],
      [
        "Hölder, Darstellung der Kantischen Erkenntnistheorie; Tübingen 1874"
      ],
      [
        "Horwicz, Analyse des Denkens usw.; Halle 1875"
      ],
      [
        "Jacobi, David Hume über den Glauben oder Idealis­mus und Realismus; Breslau 1787"
      ],
      [
        "Kappes, Der « Common Sense » als Prinzip der Gewiß­heit in der Philosophie des Schotten Thomas Reid; Mün­chen 1890"
      ],
      [
        "Kauffmann, Fundamente der Erkenntnistheorie und Wissenschaftslehre; Leipzig 1890"
      ],
      [
        "Kerry, System einer Theorie der Grenzgebiete; Wien 1890"
      ],
      [
        "H. v.",
        "Kirchmann, Die Lehre vom Wissen als Einleitung in das Studium philosophischer Werke; Berlin 1868"
      ],
      [
        "Laas, Die Kausalität des Ich; Vierteljahrsschrift für wis­senschaftliche Philosophie; Leipzig, 4.",
        "Jahrgang (1880) S.1 ff, 185ff, 311 ff Idealismus und Positivismus; Berlin 1879"
      ],
      [
        "Lange, Geschichte des Materialismus; Iserlohn 1873/75"
      ],
      [
        "A. v.",
        "Leclair, Beiträge zu einer monistischen Erkenntnis­theorie; Breslau 1882"
      ],
      [
        "Das kategorische Gepräge des Denkens; Vierteljahrs­schrift für wissenschaftliche Philosophie, Leipzig, 7.Jahr-gang (1883) S.257 ff"
      ],
      [
        "Liebmann, Kant und die Epigonen; Stuttgart 1865"
      ],
      [
        "Zur Analysis der Wirklichkeit; Straßburg 1880"
      ],
      [
        "Gedanken und Tatsachen; Straßburg 1882"
      ],
      [
        "Die Klimax der Theorien; Straßburg 1884"
      ],
      [
        "Lipps, Grundtatsachen des Seelenlebens; Bonn 1883 H.",
        "Lotze, System der Philosophie, 1.",
        "Teil: Logik; Leip­zig 1874"
      ],
      [
        "Mayer, Vom Erkennen; Freiburg i.",
        "Br. 1885"
      ],
      [
        "Meinong, Hume-Studien; Wien 1877"
      ],
      [
        "Mill, System der induktiven und deduktiven Logik; 1843; deutsch Braunschweig 1849"
      ],
      [
        "Münz, Die Grundlagen der Kantschen Erkenntnistheorie; 2.",
        "Auflage, Breslau 1885"
      ],
      [
        "Neudecker, Das Grundproblem der Erkenntnistheorie; Nördlingen 1881"
      ],
      [
        "Paulsen, Versuch einer Entwicklungsgeschichte der Kant­schen Erkenntnistheorie; Leipzig 1875"
      ],
      [
        "Rehmke, Die Welt als Wahrnehmung und Begriff usw.; Berlin 1880"
      ],
      [
        "Reid, Untersuchungen über den menschlichen Geist nach Prinzipien des gesunden Menschenverstandes; 1764, deutsch Leipzig 1782"
      ],
      [
        "Riehl, Der philosophische Kritizismus und seine Be­deutung für die positive Wissenschaft; Leipzig 1887"
      ],
      [
        "Rülf, Wissenschaft des Weltgedankens und der Gedan­kenwelt, System einer neuen Metaphysik; Leipzig 1888"
      ],
      [
        "R. v.",
        "Schubert-Soldern, Grundlagen einer Erkenntnistheo­rie; Leipzig 1884"
      ],
      [
        "Schulze, Aenesidemus; Helmstädt 1792 W.",
        "Schuppe, Zur voraussetzungslosen Erkenntnistheorie; Philosophische Monatshefte, Berlin, Leipzig, Heidelberg 1882, Band XVIII, Heft 6 u. 7"
      ],
      [
        "Seydel, Logik oder Wissenschaft vom Wissen; Leipzig 1866"
      ],
      [
        "Christoph v.",
        "Sigwart, Logik; Freiburg i.",
        "Br. 1878"
      ],
      [
        "Stadler, Die Grundsätze der reinen Erkenntnistheorie in der Kantischen Philosophie; Leipzig 1876"
      ],
      [
        "Taine, De l'Intelligence; 5.",
        "Auflage, Paris 1888"
      ],
      [
        "Trendelenburg, Logische Untersuchungen; Leipzig 1862"
      ],
      [
        "Ueberweg, System der Logik; 3.",
        "Auflage, Bonn 1882"
      ],
      [
        "Vaihinger, Hartmann, Dühring und Lange; Iserlohn 1876"
      ],
      [
        "Vambühler, Widerlegung der Kritik der reinen Ver­nunft; Leipzig 1890"
      ],
      [
        "Volkelt, Immanuel Kants Erkenntnistheorie usw.; Ham­burg 1879 Erfahrung und Denken; Hamburg 1886 R.",
        "Wahle, Gehirn und Bewußtsein; Wien 1884"
      ],
      [
        "Windelband, Präludien; Freiburg i.",
        "Br. 1884"
      ],
      [
        "Die verschiedenen Phasen der Kantschen Lehre vom « Ding an sich»; Vierteljahrsschrift für wissenschaftliche Philosophie, Leipzig, 1.Jahrgang (1877), S.224 ff"
      ],
      [
        "Witte, Beiträge zum Verständnis Kants; Berlin 1874 Vorstudien zur Erkenntnis des unerfahrbaren Seins;"
      ],
      [
        "Wolff, Über den Zusammenhang unserer Vorstellungen mit den Dingen außer uns; Leipzig 1874"
      ],
      [
        "Wolff, Das Bewußtsein und sein Objekt; Berlin 1889"
      ],
      [
        "Wundt, Logik, 1.",
        "Bd.: Erkenntnislehre; Stuttgart 1880"
      ],
      [
        "Für Fichte kommen in Betracht:"
      ],
      [
        "Biedermann, De Genetica philosophandi ratione et methodo, praesertim Fichtii, Schellingii, Hegelii, Disser­tationis particula prima, syntheticam Fichtii methodum exhibens usw.; Lipsiae 1835"
      ],
      [
        "Frederichs, Der Freiheitsbegriff Kants und Fichtes; Ber­lin 1886"
      ],
      [
        "Gühlhof, Der transcendentale Idealismus; Halle 1888"
      ],
      [
        "Hensel, Über die Beziehung des reinen Ich bei Fichte zur Einheit der Apperception bei Kant; Freiburg i.",
        "Br. 1885"
      ],
      [
        "Schwabe, Fichtes und Schopenhauers Lehre vom Willen mit ihren Consequenzen für Weltbegreifung und Lebens­führung; Jena 1887"
      ],
      [
        "Die zahlreichen zum Fichte-Jubiläum 1862 erschienenen Schriften finden natürlich hier keine Berücksichtigung.",
        "Höchstens die Rede Trendelenburgs (A.",
        "Trendelenburg, Zur Erinnerung an J.",
        "Fichte; Berlin 1862), welche wich­tigere theoretische Gesichtspunkte enthält, möge erwähnt werden."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "I. VORBEMERKUNGEN",
    "paragraphs": [
      "GA003 - Wahrheit und Wissenschaft",
      "Die Erkenntnistheorie soll eine wissenschaftliche Unter­suchung desjenigen sein, was alle übrigen Wissenschaften ungeprüft voraussetzen: des Erkennens selbst. Damit ist ihr von vornherein der Charakter der philosophischen Funda­mentalwissenschaft zugesprochen.",
      "Denn erst durch sie kön­nen wir erfahren, welchen Wert und welche Bedeutung die durch die anderen Wissenschaften gewonnenen Einsichten haben. Sie bildet in dieser Hinsicht die Grundlage für alles wissenschaftliche Streben.",
      "Es ist aber klar, daß sie dieser ihrer Aufgabe nur dann gerecht werden kann, wenn sie selbst, soweit das bei der Natur des menschlichen Erkennt­nisvermögens möglich ist, voraussetzungslos ist. Dies wird wohl allgemein zugestanden.",
      "Dennoch findet man bei eingehender Prüfung der bekannteren erkenntnistheoretischen Systeme, daß schon in den Ausgangspunkten der Unter­suchung eine ganze Reihe von Voraussetzungen gemacht werden, die dann die überzeugende Wirkung der weiteren Darlegungen wesentlich beeinträchtigen. Namentlich wird man bemerken, daß gewöhnlich schon bei Aufstellung der erkenntnistheoretischen Grundprobleme gewisse versteckte Annahmen gemacht werden.",
      "Wenn aber die Fragestellun­gen einer Wissenschaft verfehlte sind, dann muß man wohl an einer richtigen Lösung von vornherein zweifeln. Die Ge­schichte der Wissenschaften lehrt uns doch, daß unzählige Irrtümer, an denen ganze Zeitalter krankten, einzig und allein darauf zurückzuführen sind, daß gewisse Probleme falsch gestellt worden sind.",
      "Wir brauchen nicht bis auf die",
      "Physik des Aristoteles oder die Ars magna Lulliana zurück­zugehen, um diesen Satz zu erhärten, sondern wir können in der neueren Zeit Beispiele genug finden. Die zahlreichen Fragen nach der Bedeutung rudimentärer Organe bei ge­wissen Organismen konnten erst dann in richtiger Weise gestellt werden, als durch die Auffindung des biogenetischen Grundgesetzes die Bedingungen hierzu geschaffen waren.",
      "Solange die Biologie unter dem Einflusse teleologischer An­schauungen stand, war es unmöglich, die entsprechenden Probleme so aufzuwerfen, daß eine befriedigende Antwort möglich geworden wäre. Welche abenteuerlichen Vorstel­lungen hatte man z.",
      "B. über die Aufgabe der sogenannten Zirbeldrüse im menschlichen Gehirne, solange man nach einer solchen Aufgabe überhaupt fragte! Erst als man auf dem Wege der vergleichenden Anatomie die Klarstellung der Sache suchte und sich fragte, ob dieses Organ nicht bloß ein beim Menschen stehengebliebener Rest aus niederen Entwickelungsformen sei, gelangte man zu einem Ziele.",
      "Oder, um noch ein Beispiel anzuführen, welche Modifika­tionen erfuhren gewisse Fragestellungen in der Physik durch die Entdeckung des mechanischen Wärmeäquivalentes und des Gesetzes von der Erhaltung der Kraft! Kurz, der Erfolg wissenschaftlicher Untersuchungen ist ganz wesentlich da­von abhängig, ob man die Probleme richtig zu stellen im­stande ist.",
      "Wenn auch die Erkenntnistheorie als Voraus­setzung aller übrigen Wissenschaften eine ganz besondere Stellung einnimmt, so ist dennoch vorauszusehen, daß auch in ihr ein erfolgreiches Fortschreiten in der Untersuchung nur dann möglich sein wird, wenn die Grundfragen in rich­tiger Form aufgeworfen werden.",
      "Die folgenden Auseinandersetzungen streben nun in erster",
      "Linie eine solche Formulierung des Erkenntnisproblems an, die dem Charakter der Erkenntnistheorie als vollstän­dig voraussetzungsloser Wissenschaft strenge gerecht wird. Sie wollen dann auch das Verhältnis von J. G. Fichtes Wis­senschaftslehre zu einer solchen philosophischen Grund­wissenschaft beleuchten. Warum wir gerade Fichtes Versuch, den Wissenschaften eine unbedingt gewisse Grundlage zu schaffen, mit dieser Aufgabe in nähere Verbindung bringen, wird sich im Verlaufe der Untersuchung von selbst ergeben."
    ],
    "sentences": [
      [
        "GA003 - Wahrheit und Wissenschaft"
      ],
      [
        "Die Erkenntnistheorie soll eine wissenschaftliche Unter­suchung desjenigen sein, was alle übrigen Wissenschaften ungeprüft voraussetzen: des Erkennens selbst.",
        "Damit ist ihr von vornherein der Charakter der philosophischen Funda­mentalwissenschaft zugesprochen."
      ],
      [
        "Denn erst durch sie kön­nen wir erfahren, welchen Wert und welche Bedeutung die durch die anderen Wissenschaften gewonnenen Einsichten haben.",
        "Sie bildet in dieser Hinsicht die Grundlage für alles wissenschaftliche Streben."
      ],
      [
        "Es ist aber klar, daß sie dieser ihrer Aufgabe nur dann gerecht werden kann, wenn sie selbst, soweit das bei der Natur des menschlichen Erkennt­nisvermögens möglich ist, voraussetzungslos ist.",
        "Dies wird wohl allgemein zugestanden."
      ],
      [
        "Dennoch findet man bei eingehender Prüfung der bekannteren erkenntnistheoretischen Systeme, daß schon in den Ausgangspunkten der Unter­suchung eine ganze Reihe von Voraussetzungen gemacht werden, die dann die überzeugende Wirkung der weiteren Darlegungen wesentlich beeinträchtigen.",
        "Namentlich wird man bemerken, daß gewöhnlich schon bei Aufstellung der erkenntnistheoretischen Grundprobleme gewisse versteckte Annahmen gemacht werden."
      ],
      [
        "Wenn aber die Fragestellun­gen einer Wissenschaft verfehlte sind, dann muß man wohl an einer richtigen Lösung von vornherein zweifeln.",
        "Die Ge­schichte der Wissenschaften lehrt uns doch, daß unzählige Irrtümer, an denen ganze Zeitalter krankten, einzig und allein darauf zurückzuführen sind, daß gewisse Probleme falsch gestellt worden sind."
      ],
      [
        "Wir brauchen nicht bis auf die"
      ],
      [
        "Physik des Aristoteles oder die Ars magna Lulliana zurück­zugehen, um diesen Satz zu erhärten, sondern wir können in der neueren Zeit Beispiele genug finden.",
        "Die zahlreichen Fragen nach der Bedeutung rudimentärer Organe bei ge­wissen Organismen konnten erst dann in richtiger Weise gestellt werden, als durch die Auffindung des biogenetischen Grundgesetzes die Bedingungen hierzu geschaffen waren."
      ],
      [
        "Solange die Biologie unter dem Einflusse teleologischer An­schauungen stand, war es unmöglich, die entsprechenden Probleme so aufzuwerfen, daß eine befriedigende Antwort möglich geworden wäre.",
        "Welche abenteuerlichen Vorstel­lungen hatte man z."
      ],
      [
        "B. über die Aufgabe der sogenannten Zirbeldrüse im menschlichen Gehirne, solange man nach einer solchen Aufgabe überhaupt fragte!",
        "Erst als man auf dem Wege der vergleichenden Anatomie die Klarstellung der Sache suchte und sich fragte, ob dieses Organ nicht bloß ein beim Menschen stehengebliebener Rest aus niederen Entwickelungsformen sei, gelangte man zu einem Ziele."
      ],
      [
        "Oder, um noch ein Beispiel anzuführen, welche Modifika­tionen erfuhren gewisse Fragestellungen in der Physik durch die Entdeckung des mechanischen Wärmeäquivalentes und des Gesetzes von der Erhaltung der Kraft!",
        "Kurz, der Erfolg wissenschaftlicher Untersuchungen ist ganz wesentlich da­von abhängig, ob man die Probleme richtig zu stellen im­stande ist."
      ],
      [
        "Wenn auch die Erkenntnistheorie als Voraus­setzung aller übrigen Wissenschaften eine ganz besondere Stellung einnimmt, so ist dennoch vorauszusehen, daß auch in ihr ein erfolgreiches Fortschreiten in der Untersuchung nur dann möglich sein wird, wenn die Grundfragen in rich­tiger Form aufgeworfen werden."
      ],
      [
        "Die folgenden Auseinandersetzungen streben nun in erster"
      ],
      [
        "Linie eine solche Formulierung des Erkenntnisproblems an, die dem Charakter der Erkenntnistheorie als vollstän­dig voraussetzungsloser Wissenschaft strenge gerecht wird.",
        "Sie wollen dann auch das Verhältnis von J.",
        "Fichtes Wis­senschaftslehre zu einer solchen philosophischen Grund­wissenschaft beleuchten.",
        "Warum wir gerade Fichtes Versuch, den Wissenschaften eine unbedingt gewisse Grundlage zu schaffen, mit dieser Aufgabe in nähere Verbindung bringen, wird sich im Verlaufe der Untersuchung von selbst ergeben."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "II. KANTS ERKENNTNISTHEORETISCHE GRUNDFRAGE",
    "paragraphs": [
      "GA003 - Wahrheit und Wissenschaft",
      "Als der Begründer der Erkenntnistheorie im modernen Sinne des Wortes wird gewöhnlich Kant genannt. Gegen diese Auffassung könnte man wohl mit Recht einwenden, daß die Geschichte der Philosophie vor Kant zahlreiche Untersuchungen aufweist, die denn doch als mehr denn als bloße Keime zu einer solchen Wissenschaft anzusehen sind. So bemerkt auch Volkelt in seinem grundlegenden Werke über Erkenntnistheorie, daß schon mit Locke die kritische Behandlung dieser Wissenschaft ihren Anfang genommen habe. Aber auch bei noch früheren Philosophen, ja schon in der Philosophie der Griechen, findet man Erörterungen, die gegenwärtig in der Erkenntnistheorie* angestellt zu wer­den pflegen. Indessen sind durch Kant alle hier in Betracht kommenden Probleme in ihren Tiefen aufgewühlt worden, und an ihn anknüpfend haben zahlreiche Denker dieselben so allseitig durchgearbeitet, daß man die bereits früher vor­kommenden Lösungsversuche entweder bei Kant selbst oder bei seinen Epigonen wiederfindet. Wenn es sich also um ein rein sachliches und nicht um ein historisches Studium der Erkenntnistheorie handelt, so wird man kaum an einer wichtigen Erscheinung vorübergehen, wenn man bloß die Zeit seit Kants Auftreten mit der Kritik der reinen Ver­nunft in Rechnung bringt. Was vorher auf diesem Felde ge­leistet worden ist, wiederholt sich in dieser Epoche wieder.",
      "-025-* Erfahrung und Denken. Kritische Grundlegung der Erkenntnis­theorie. Hamburg und Leipzig 1886, S.20.",
      "Kants erkenntnistheoretische Grundfrage ist: Wie sind synthetische Urteile a priori möglich? Sehen wir diese Frage einmal auf ihre Voraussetzungslosigkeit hin an! Kant wirft dieselbe deswegen auf, weil er der Meinung ist, daß wir ein unbedingt gewisses Wissen nur dann erlangen können, wenn wir in der Lage sind, die Berechtigung synthetischer Urteile a priori nachzuweisen. Er sagt: «In der Auflösung obiger Aufgabe ist zugleich die Möglichkeit des reinen Ver­nunftgebrauches in Gründung und Ausführung aller Wis­senschaften, die eine theoretische Erkenntnis a priori von Gegenständen enthalten, mit begriffen»* und «Auf die Auflösung dieser Aufgabe nun kommt das Stehen und Fal­len der Metaphysik, und also ihre Existenz gänzlich an»**.",
      "Ist diese Frage nun, so wie Kant sie stellt, voraussetzungs­los? Keineswegs, denn sie macht die Möglichkeit eines un­bedingt gewissen Systems vom Wissen davon abhängig, daß es sich nur aus synthetischen und aus solchen Urteilen aufbaut, die unabhängig von aller Erfahrung gewonnen werden. Synthetische Urteile nennt Kant solche, bei welchen der Prädikatbegriff etwas zum Subjektbegriff hinzubringt, was ganz außer demselben liegt, «ob es zwar mit demsel­ben in Verknüpfung steht»***, wogegen bei den analyti­schen Urteilen das Prädikat nur etwas aussagt, was (ver­steckterweise) schon im Subjekt enthalten ist. Es kann hier wohl nicht der Ort sein, auf die scharfsinnigen Einwände",
      "-026-* Kritik der reinen Vernunft S. 61 ff nach der Ausgabe von Kirchmann, auf welche Ausgabe auch alle anderen Seitenzahlen bei Zitaten aus der Kritik der reinen Vernunft und der  zu beziehen sind.",
      "-026-** Prolegomena § 5.",
      "-026-***     Kritik der reinen Vernunft S.53 f.",
      "Johannes Rehmkes* gegen diese Gliederung der Urteile einzugehen. Für unseren gegenwärtigen Zweck genügt es, einzusehen, daß wir ein wahrhaftes Wissen nur durch solche Urteile erlangen können, die zu einem Begriffe einen zwei­ten hinzufügen, dessen Inhalt wenigstens für uns in jenem ersten noch nicht gelegen war.",
      "Wollen wir diese Klasse von Urteilen mit Kant synthetische nennen, so können wir im­merhin zugestehen, daß Erkenntnisse in Urteilsform nur dann gewonnen werden können, wenn die Verbindung des Prädikats mit dem Subjekte eine solche synthetische ist. Anders aber steht die Sache mit dem zweiten Teil der Frage, der verlangt, daß diese Urteile a priori, d. i. unab­hängig von aller Erfahrung, gewonnen sein müssen.",
      "Es ist ja durchaus möglich (wir meinen hiermit natürlich die bloße Denkmöglichkeit), daß es solche Urteile überhaupt gar nicht gibt. Für den Anfang der Erkenntnistheorie muß es als gänzlich unausgemacht gelten, ob wir anders als durch Erfahrung, oder nur durch diese zu Urteilen kommen kön­nen.",
      "Ja, einer unbefangenen Überlegung gegenüber scheint eine solche Unabhängigkeit von vornherein unmöglich. Denn was auch immer Gegenstand unseres Wissens werden mag: es muß doch einmal als unmittelbares, individuelles Erlebnis an uns herantreten, das heißt zur Erfahrung wer­den.",
      "Auch die mathematischen Urteile gewinnen wir auf keinem anderen Wege, als indem wir sie in bestimmten ein­zelnen Fällen erfahren. Selbst wenn man, wie z. Otto Liebmann (Zur Analysis der Wirklichkeit. Gedanken und Tatsachen), dieselben in einer gewissen Organisation un­seres Bewußtseins begründet sein läßt, so stellt sich die",
      "-027-* Die Welt als Wahrnehmung und Begriff S.161 ff.",
      "Sache nicht anders dar. Man kann dann wohl sagen: dieser oder jener Satz sei notwendig gültig, denn würde seine Wahrheit aufgehoben, so würde das Bewußtsein mit aufgehoben: aber den Inhalt desselben als Erkenntnis können wir doch nur gewinnen, wenn er einmal Erlebnis für uns wird, ganz in derselben Weise wie ein Vorgang in der äuße­ren Natur. Mag immer der Inhalt eines solchen Satzes Ele­mente enthalten, die seine absolute Gültigkeit verbürgen, oder mag dieselbe aus anderen Gründen gesichert sein: ich kann seiner nicht anders habhaft werden, als wenn er mir einmal als Erfahrung gegenübertritt. Dies ist das eine.",
      "Das zweite Bedenken besteht darin, daß man am Beginne der erkenntnistheoretischen Untersuchungen durchaus nicht behaupten darf, aus der Erfahrung können keine unbedingt gültigen Erkenntnisse stammen. Es ist zweifellos ganz gut denkbar, daß die Erfahrung selbst ein Kennzeichen aufwiese, durch welches die Gewißheit der aus ihr gewonne­nen Einsichten verbürgt würde.",
      "So liegen in der Kantschen Fragestellung zwei Voraus­setzungen: erstens, daß wir außer der Erfahrung noch einen Weg haben müssen, um zu Erkenntnissen zu gelangen, und zweitens, daß alles Erfahrungswissen nur bedingte Gültig­keit haben könne. Daß diese Sätze einer Prüfung bedürftig sind, daß sie bezweifelt werden können, dies kommt Kant gar nicht zum Bewußtsein. Er nimmt sie einfach als Vor­urteile aus der dogmatischen Philosophie herüber und legt sie seinen kritischen Untersuchungen zum Grunde. Die dogmatische Philosophie setzt sie als gültig voraus und wendet sie einfach an, um zu einem ihnen entsprechenden Wissen zu gelangen; Kant setzt sie als gültig voraus und fragt sich nur: unter welchen Bedingungen können sie gültig",
      "sein? Wie: wenn sie aber überhaupt nicht gültig sind? Dann fehlt dem Kantschen Lehrgebäude jede Grundlage. Alles, was Kant in den fünf Paragraphen, die der For­mulierung seiner Grundfrage vorangehen, vorbringt, ist der Versuch eines Beweises, daß die mathematischen Urteile synthetisch sind*.",
      "Aber gerade die von uns angeführten zwei Voraussetzungen bleiben als wissenschaftliche Vor­urteile stehen. In Einleitung II der Kritik der reinen Ver­nunft heißt es: « Erfahrung lehrt uns zwar, daß etwas so oder so beschaffen sei, aber nicht, daß es nicht anders sein könne » und: « Erfahrung gibt niemals ihren Urteilen wahre oder strenge, sondern nur angenommene und komparative Allgemeinheit (durch Induktion). » In Prolegomena Para­graph 1 finden wir: «Zuerst, was die Quellen einer meta­physischen Erkenntnis betrifft:, so liegt es schon in ihrem Begriffe, daß sie nicht empirische sein können.",
      "Die Prinzi­pien derselben (wozu nicht bloß ihre Grundsätze, sondern auch ihre Grundbegriffe gehören) müssen also niemals aus der Erfahrung genommen sein, denn sie soll nicht physische, sondern metaphysische, d. i. jenseits der Erfahrung liegende Erkenntnis sein. » Endlich sagt Kant in der Kritik der rei­nen Vernunft (S.58): « Zuvörderst muß bemerkt werden, daß eigentliche mathematische Sätze jederzeit Urteile a priori und nicht empirisch sind, weil sie Notwendigkeit bei sich führen, welche aus der Erfahrung nicht abgenom­men werden kann. Will man aber dieses nicht einräumen, wohlan, so schränke ich meinen Satz auf die reine Mathe­matik ein, deren Begriff es schon mit sich bringt, daß sie",
      "-029-* Ein Versuch, der übrigens durch die Einwendungen Rob. Zim­mermanns (Über Kants  mathematisches Vorurteil und dessen Folgen), wenn auch nicht gänzlich widerlegt, so doch sehr in Frage gestellt ist.",
      "nicht empirische, sondern bloß reine Erkenntnis a priori enthalte.» Wir mögen die Kritik der reinen Vernunft auf­schlagen, wo wir wollen, so werden wir finden, daß alle Untersuchungen innerhalb derselben unter Voraussetzung dieser dogmatischen Sätze geführt werden. Cohen* und Stadler** versuchen zu beweisen, Kant habe die apriorische Natur der mathematischen und rein-naturwissenschaftlichen Sätze dargetan. Nun läßt sich aber alles, was in der Kritik versucht wird, im folgenden zusammenfassen:",
      "Weil Mathematik und reine Naturwissenschaft apriorische Wissenschaften sind, deshalb muß die Form aller Erfahrung im Subjekt begründet sein. Es bleibt also nur das Material der Empfindungen, das empirisch gegeben ist. Dieses wird durch die im Gemüte liegenden Formen zum Systeme der Erfahrung aufgebaut. Nur als ordnende Prinzipien für das Empfindungsmaterial haben die formalen Wahrheiten der apriorischen Theorien Sinn und Bedeutung, sie machen die Erfahrung möglich, reichen aber nicht über dieselbe hin­aus. Diese formalen Wahrheiten sind aber die synthetischen Urteile a priori, welche somit als Bedingungen aller mög­lichen Erfahrung so weit reichen müssen als diese selbst. Die Kritik der reinen Vernunft beweist also durchaus nicht die Apriorität der Mathematik und reinen Naturwissen­schaft, sondern bestimmt nur deren Geltungsgebiet unter der Voraussetzung, daß ihre Wahrheiten von der Erfah­rung unabhängig gewonnen werden sollen. Ja, Kant läßt sich so wenig auf einen Beweis für diese Apriorität ein, daß er einfach denjenigen Teil der Mathematik ausschließt (siehe",
      "-030-* Kants Theorie der Erfahrung S.90 ff.",
      "-030-** Die Grundsätze der reinen Erkenntnistheorie in der Kantschen Philosophie S.76 f.",
      "oben S. 29 Z. 26 f.), bei dem dieselbe etwa, auch nach seiner Ansicht, bezweifelt werden könnte, und sich nur auf den beschränkt, bei dem er sie aus dem bloßen Begriff folgern zu können glaubt. Auch Johannes Volkelt findet, daß « Kant von ausdrücklicher Voraussetzung» ausgehe, «daß es tatsächlich ein allgemeines und notwendiges Wissen gebe». Er sagt darüber noch weiter: «Diese von Kant nie aus­drücklich in Prüfung gezogene Voraussetzung steht mit dem Charakter der kritischen Erkenntnistheorie derart in Wi­derspruch, daß man sich ernstlich die Frage vorlegen muß, ob die Kritik der reinen Vernunft als kritische Erkenntnis­theorie gelten dürfe. » Volkelt findet zwar, daß man diese Frage aus guten Gründen bejahen dürfe, aber es ist « doch durch jene dogmatische Voraussetzung die kritische Hal­tung der Kantschen Erkenntnistheorie in durchgreifender Weise gestört». Genug, auch Volkelt findet, daß die Kri­tik der reinen Vernunft keine voraussetzungslose Erkennt­nistheorie ist.",
      "Im wesentlichen mit der unseren übereinstimmen auch die Auffassungen 0. Liebmanns, Hölders, Windelbands, Überwegs, Ed. v.Hartmanns** und Kuno Fischers*** in bezug",
      "-031-* Erfahrung und Denken S.21.",
      "-031-** Liebmann, Analysis S. 211 ff., Hölder, Erkenntnistheorie S. 14 ff., Windelband, Phasen S. 239, Überweg, System der Logik S. 380 f., Hartmann, Kritische Grundlegung S.142-172.",
      "-031-*** Geschichte der neueren Philosophie VB. S.60. In bezug auf Kuno Fischer irrt Volkelt, wenn er (Kants Erkenntnistheorie S. 198 f. Anmerkung) sagt, es würde «aus der Darstellung K. Fischers nicht klar, ob seiner Ansicht nach Kant nur die psychologische Tatsächlichkeit der allgemeinen und notwendigen Urteile oder zugleich die objektive Gültigkeit und Rechtmäßigkeit derselben voraussetze». Denn an der angeführten Stelle sagt Fischer, daß die Hauptschwierigkeit der Kritik der reinen Vernunft darin zu suchen sei, daß deren «Grundlegungen ­von gewissen Voraussetzungen abhängig» seien, «die man eingeräumt haben müsse, um das Folgende gelten zu lassen». Diese Voraussetzun­gen sind auch für Fischer der Umstand, daß «erst die Tatsache der Erkenntnis» festgestellt wird und dann durch Analyse die Erkenntnisvermögen gefunden, «aus denen jene Tatsache selbst erklärt wird».",
      "auf den Umstand, daß Kant die apriorische Gültigkeit der reinen Mathematik und Naturlehre als Voraussetzung an die Spitze seiner Erörterungen stellt.",
      "Daß wir wirklich Erkenntnisse haben, die von aller Er­fahrung unabhängig sind, und daß die letzteren nur Ein­sichten von komparativer Allgemeinheit liefern, könnten wir nur als Folgesätze von anderen Urteilen gelten lassen. Es müßte diesen Behauptungen unbedingt eine Untersuchung über das Wesen der Erfahrung und eine solche über das Wesen unseres Erkennens vorangehen. Aus jener könnte der erste, aus dieser der zweite der obigen Sätze folgen.",
      "Nun könnte man auf unsere der Vernunftkritik gegen­über geltend gemachten Einwände noch folgendes erwidern. Man könnte sagen, daß doch jede Erkenntnistheorie den Leser erst dahin führen müsse, wo der voraussetzungslose Ausgangspunkt zu finden ist. Denn was wir zu irgendeinem Zeitpunkte unseres Lebens als Erkenntnisse besitzen, hat sich weit von diesem Ausgangspunkte entfernt, und wir müssen erst wieder künstlich zu ihm zurückgeführt werden. In der Tat ist eine solche rein didaktische Verständigung über den Anfang seiner Wissenschaft für jeden Erkenntnistheoretiker eine Notwendigkeit. Dieselbe muß sich aber jedenfalls darauf beschränken, zu zeigen, inwiefern der in Rede stehende Anfang des Erkennens wirklich ein solcher ist, sie müßte in rein selbstverständlichen analytischen Sät­zen verlaufen und keinerlei wirkliche inhaltsvolle Behauptungen",
      "aufstellen, die den Inhalt der folgenden Erörterun­gen beeinflussen, wie das bei Kant der Fall ist. Auch obliegt es dem Erkenntnistheoretiker, zu zeigen, daß der von ihm angenommene Anfang wirklich voraussetzungslos ist. Aber alles das hat mit dem Wesen dieses Anfanges selbst nichts zu tun, steht ganz außerhalb desselben, sagt nichts über ihn aus. Auch am Beginne des Mathematikunterrichts muß ich mich ja bemühen, den Schüler von dem axiomatischen Cha­rakter gewisser Wahrheiten zu überzeugen. Aber niemand wird behaupten wollen, daß der Inhalt der Axiome von diesen vorher angestellten Erwägungen abhängig gemacht wird*. Genau in derselben Weise müßte der Erkenntnistheoretiker in seinen einleitenden Bemerkungen den Weg zeigen, wie man zu einem voraussetzungslosen Anfang kommen kann; der eigentliche Inhalt aber desselben muß von diesen Erwägungen unabhängig sein. Von einer solchen Einleitung in die Erkenntnistheorie ist der aber jedenfalls weit entfernt, der wie Kant am Anfange Behauptungen mit ganz bestimmtem, dogmatischem Charakter aufstellt.",
      "-032-* Inwiefern wir mit unseren eigenen erkenntnistheoretischen Er­wägungen ganz in derselben Weise vorgehen, zeigen wir in Kapitel IV: Die Ausgangspunkte der Erkenntnistheorie."
    ],
    "sentences": [
      [
        "GA003 - Wahrheit und Wissenschaft"
      ],
      [
        "Als der Begründer der Erkenntnistheorie im modernen Sinne des Wortes wird gewöhnlich Kant genannt.",
        "Gegen diese Auffassung könnte man wohl mit Recht einwenden, daß die Geschichte der Philosophie vor Kant zahlreiche Untersuchungen aufweist, die denn doch als mehr denn als bloße Keime zu einer solchen Wissenschaft anzusehen sind.",
        "So bemerkt auch Volkelt in seinem grundlegenden Werke über Erkenntnistheorie, daß schon mit Locke die kritische Behandlung dieser Wissenschaft ihren Anfang genommen habe.",
        "Aber auch bei noch früheren Philosophen, ja schon in der Philosophie der Griechen, findet man Erörterungen, die gegenwärtig in der Erkenntnistheorie* angestellt zu wer­den pflegen.",
        "Indessen sind durch Kant alle hier in Betracht kommenden Probleme in ihren Tiefen aufgewühlt worden, und an ihn anknüpfend haben zahlreiche Denker dieselben so allseitig durchgearbeitet, daß man die bereits früher vor­kommenden Lösungsversuche entweder bei Kant selbst oder bei seinen Epigonen wiederfindet.",
        "Wenn es sich also um ein rein sachliches und nicht um ein historisches Studium der Erkenntnistheorie handelt, so wird man kaum an einer wichtigen Erscheinung vorübergehen, wenn man bloß die Zeit seit Kants Auftreten mit der Kritik der reinen Ver­nunft in Rechnung bringt.",
        "Was vorher auf diesem Felde ge­leistet worden ist, wiederholt sich in dieser Epoche wieder."
      ],
      [
        "-025-* Erfahrung und Denken.",
        "Kritische Grundlegung der Erkenntnis­theorie.",
        "Hamburg und Leipzig 1886, S.20."
      ],
      [
        "Kants erkenntnistheoretische Grundfrage ist: Wie sind synthetische Urteile a priori möglich?",
        "Sehen wir diese Frage einmal auf ihre Voraussetzungslosigkeit hin an!",
        "Kant wirft dieselbe deswegen auf, weil er der Meinung ist, daß wir ein unbedingt gewisses Wissen nur dann erlangen können, wenn wir in der Lage sind, die Berechtigung synthetischer Urteile a priori nachzuweisen.",
        "Er sagt: «In der Auflösung obiger Aufgabe ist zugleich die Möglichkeit des reinen Ver­nunftgebrauches in Gründung und Ausführung aller Wis­senschaften, die eine theoretische Erkenntnis a priori von Gegenständen enthalten, mit begriffen»* und «Auf die Auflösung dieser Aufgabe nun kommt das Stehen und Fal­len der Metaphysik, und also ihre Existenz gänzlich an»**."
      ],
      [
        "Ist diese Frage nun, so wie Kant sie stellt, voraussetzungs­los?",
        "Keineswegs, denn sie macht die Möglichkeit eines un­bedingt gewissen Systems vom Wissen davon abhängig, daß es sich nur aus synthetischen und aus solchen Urteilen aufbaut, die unabhängig von aller Erfahrung gewonnen werden.",
        "Synthetische Urteile nennt Kant solche, bei welchen der Prädikatbegriff etwas zum Subjektbegriff hinzubringt, was ganz außer demselben liegt, «ob es zwar mit demsel­ben in Verknüpfung steht»***, wogegen bei den analyti­schen Urteilen das Prädikat nur etwas aussagt, was (ver­steckterweise) schon im Subjekt enthalten ist.",
        "Es kann hier wohl nicht der Ort sein, auf die scharfsinnigen Einwände"
      ],
      [
        "-026-* Kritik der reinen Vernunft S. 61 ff nach der Ausgabe von Kirchmann, auf welche Ausgabe auch alle anderen Seitenzahlen bei Zitaten aus der Kritik der reinen Vernunft und der zu beziehen sind."
      ],
      [
        "-026-** Prolegomena § 5."
      ],
      [
        "-026-*** Kritik der reinen Vernunft S.53 f."
      ],
      [
        "Johannes Rehmkes* gegen diese Gliederung der Urteile einzugehen.",
        "Für unseren gegenwärtigen Zweck genügt es, einzusehen, daß wir ein wahrhaftes Wissen nur durch solche Urteile erlangen können, die zu einem Begriffe einen zwei­ten hinzufügen, dessen Inhalt wenigstens für uns in jenem ersten noch nicht gelegen war."
      ],
      [
        "Wollen wir diese Klasse von Urteilen mit Kant synthetische nennen, so können wir im­merhin zugestehen, daß Erkenntnisse in Urteilsform nur dann gewonnen werden können, wenn die Verbindung des Prädikats mit dem Subjekte eine solche synthetische ist.",
        "Anders aber steht die Sache mit dem zweiten Teil der Frage, der verlangt, daß diese Urteile a priori, d. i. unab­hängig von aller Erfahrung, gewonnen sein müssen."
      ],
      [
        "Es ist ja durchaus möglich (wir meinen hiermit natürlich die bloße Denkmöglichkeit), daß es solche Urteile überhaupt gar nicht gibt.",
        "Für den Anfang der Erkenntnistheorie muß es als gänzlich unausgemacht gelten, ob wir anders als durch Erfahrung, oder nur durch diese zu Urteilen kommen kön­nen."
      ],
      [
        "Ja, einer unbefangenen Überlegung gegenüber scheint eine solche Unabhängigkeit von vornherein unmöglich.",
        "Denn was auch immer Gegenstand unseres Wissens werden mag: es muß doch einmal als unmittelbares, individuelles Erlebnis an uns herantreten, das heißt zur Erfahrung wer­den."
      ],
      [
        "Auch die mathematischen Urteile gewinnen wir auf keinem anderen Wege, als indem wir sie in bestimmten ein­zelnen Fällen erfahren.",
        "Selbst wenn man, wie z.",
        "Otto Liebmann (Zur Analysis der Wirklichkeit.",
        "Gedanken und Tatsachen), dieselben in einer gewissen Organisation un­seres Bewußtseins begründet sein läßt, so stellt sich die"
      ],
      [
        "-027-* Die Welt als Wahrnehmung und Begriff S.161 ff."
      ],
      [
        "Sache nicht anders dar.",
        "Man kann dann wohl sagen: dieser oder jener Satz sei notwendig gültig, denn würde seine Wahrheit aufgehoben, so würde das Bewußtsein mit aufgehoben: aber den Inhalt desselben als Erkenntnis können wir doch nur gewinnen, wenn er einmal Erlebnis für uns wird, ganz in derselben Weise wie ein Vorgang in der äuße­ren Natur.",
        "Mag immer der Inhalt eines solchen Satzes Ele­mente enthalten, die seine absolute Gültigkeit verbürgen, oder mag dieselbe aus anderen Gründen gesichert sein: ich kann seiner nicht anders habhaft werden, als wenn er mir einmal als Erfahrung gegenübertritt.",
        "Dies ist das eine."
      ],
      [
        "Das zweite Bedenken besteht darin, daß man am Beginne der erkenntnistheoretischen Untersuchungen durchaus nicht behaupten darf, aus der Erfahrung können keine unbedingt gültigen Erkenntnisse stammen.",
        "Es ist zweifellos ganz gut denkbar, daß die Erfahrung selbst ein Kennzeichen aufwiese, durch welches die Gewißheit der aus ihr gewonne­nen Einsichten verbürgt würde."
      ],
      [
        "So liegen in der Kantschen Fragestellung zwei Voraus­setzungen: erstens, daß wir außer der Erfahrung noch einen Weg haben müssen, um zu Erkenntnissen zu gelangen, und zweitens, daß alles Erfahrungswissen nur bedingte Gültig­keit haben könne.",
        "Daß diese Sätze einer Prüfung bedürftig sind, daß sie bezweifelt werden können, dies kommt Kant gar nicht zum Bewußtsein.",
        "Er nimmt sie einfach als Vor­urteile aus der dogmatischen Philosophie herüber und legt sie seinen kritischen Untersuchungen zum Grunde.",
        "Die dogmatische Philosophie setzt sie als gültig voraus und wendet sie einfach an, um zu einem ihnen entsprechenden Wissen zu gelangen; Kant setzt sie als gültig voraus und fragt sich nur: unter welchen Bedingungen können sie gültig"
      ],
      [
        "sein?",
        "Wie: wenn sie aber überhaupt nicht gültig sind?",
        "Dann fehlt dem Kantschen Lehrgebäude jede Grundlage.",
        "Alles, was Kant in den fünf Paragraphen, die der For­mulierung seiner Grundfrage vorangehen, vorbringt, ist der Versuch eines Beweises, daß die mathematischen Urteile synthetisch sind*."
      ],
      [
        "Aber gerade die von uns angeführten zwei Voraussetzungen bleiben als wissenschaftliche Vor­urteile stehen.",
        "In Einleitung II der Kritik der reinen Ver­nunft heißt es: « Erfahrung lehrt uns zwar, daß etwas so oder so beschaffen sei, aber nicht, daß es nicht anders sein könne » und: « Erfahrung gibt niemals ihren Urteilen wahre oder strenge, sondern nur angenommene und komparative Allgemeinheit (durch Induktion). » In Prolegomena Para­graph 1 finden wir: «Zuerst, was die Quellen einer meta­physischen Erkenntnis betrifft:, so liegt es schon in ihrem Begriffe, daß sie nicht empirische sein können."
      ],
      [
        "Die Prinzi­pien derselben (wozu nicht bloß ihre Grundsätze, sondern auch ihre Grundbegriffe gehören) müssen also niemals aus der Erfahrung genommen sein, denn sie soll nicht physische, sondern metaphysische, d. i. jenseits der Erfahrung liegende Erkenntnis sein. » Endlich sagt Kant in der Kritik der rei­nen Vernunft (S.58): « Zuvörderst muß bemerkt werden, daß eigentliche mathematische Sätze jederzeit Urteile a priori und nicht empirisch sind, weil sie Notwendigkeit bei sich führen, welche aus der Erfahrung nicht abgenom­men werden kann.",
        "Will man aber dieses nicht einräumen, wohlan, so schränke ich meinen Satz auf die reine Mathe­matik ein, deren Begriff es schon mit sich bringt, daß sie"
      ],
      [
        "-029-* Ein Versuch, der übrigens durch die Einwendungen Rob.",
        "Zim­mermanns (Über Kants mathematisches Vorurteil und dessen Folgen), wenn auch nicht gänzlich widerlegt, so doch sehr in Frage gestellt ist."
      ],
      [
        "nicht empirische, sondern bloß reine Erkenntnis a priori enthalte.» Wir mögen die Kritik der reinen Vernunft auf­schlagen, wo wir wollen, so werden wir finden, daß alle Untersuchungen innerhalb derselben unter Voraussetzung dieser dogmatischen Sätze geführt werden.",
        "Cohen* und Stadler** versuchen zu beweisen, Kant habe die apriorische Natur der mathematischen und rein-naturwissenschaftlichen Sätze dargetan.",
        "Nun läßt sich aber alles, was in der Kritik versucht wird, im folgenden zusammenfassen:"
      ],
      [
        "Weil Mathematik und reine Naturwissenschaft apriorische Wissenschaften sind, deshalb muß die Form aller Erfahrung im Subjekt begründet sein.",
        "Es bleibt also nur das Material der Empfindungen, das empirisch gegeben ist.",
        "Dieses wird durch die im Gemüte liegenden Formen zum Systeme der Erfahrung aufgebaut.",
        "Nur als ordnende Prinzipien für das Empfindungsmaterial haben die formalen Wahrheiten der apriorischen Theorien Sinn und Bedeutung, sie machen die Erfahrung möglich, reichen aber nicht über dieselbe hin­aus.",
        "Diese formalen Wahrheiten sind aber die synthetischen Urteile a priori, welche somit als Bedingungen aller mög­lichen Erfahrung so weit reichen müssen als diese selbst.",
        "Die Kritik der reinen Vernunft beweist also durchaus nicht die Apriorität der Mathematik und reinen Naturwissen­schaft, sondern bestimmt nur deren Geltungsgebiet unter der Voraussetzung, daß ihre Wahrheiten von der Erfah­rung unabhängig gewonnen werden sollen.",
        "Ja, Kant läßt sich so wenig auf einen Beweis für diese Apriorität ein, daß er einfach denjenigen Teil der Mathematik ausschließt (siehe"
      ],
      [
        "-030-* Kants Theorie der Erfahrung S.90 ff."
      ],
      [
        "-030-** Die Grundsätze der reinen Erkenntnistheorie in der Kantschen Philosophie S.76 f."
      ],
      [
        "oben S. 29 Z. 26 f.), bei dem dieselbe etwa, auch nach seiner Ansicht, bezweifelt werden könnte, und sich nur auf den beschränkt, bei dem er sie aus dem bloßen Begriff folgern zu können glaubt.",
        "Auch Johannes Volkelt findet, daß « Kant von ausdrücklicher Voraussetzung» ausgehe, «daß es tatsächlich ein allgemeines und notwendiges Wissen gebe».",
        "Er sagt darüber noch weiter: «Diese von Kant nie aus­drücklich in Prüfung gezogene Voraussetzung steht mit dem Charakter der kritischen Erkenntnistheorie derart in Wi­derspruch, daß man sich ernstlich die Frage vorlegen muß, ob die Kritik der reinen Vernunft als kritische Erkenntnis­theorie gelten dürfe. » Volkelt findet zwar, daß man diese Frage aus guten Gründen bejahen dürfe, aber es ist « doch durch jene dogmatische Voraussetzung die kritische Hal­tung der Kantschen Erkenntnistheorie in durchgreifender Weise gestört».",
        "Genug, auch Volkelt findet, daß die Kri­tik der reinen Vernunft keine voraussetzungslose Erkennt­nistheorie ist."
      ],
      [
        "Im wesentlichen mit der unseren übereinstimmen auch die Auffassungen 0.",
        "Liebmanns, Hölders, Windelbands, Überwegs, Ed. v.Hartmanns** und Kuno Fischers*** in bezug"
      ],
      [
        "-031-* Erfahrung und Denken S.21."
      ],
      [
        "-031-** Liebmann, Analysis S. 211 ff., Hölder, Erkenntnistheorie S. 14 ff., Windelband, Phasen S. 239, Überweg, System der Logik S. 380 f., Hartmann, Kritische Grundlegung S.142-172."
      ],
      [
        "-031-*** Geschichte der neueren Philosophie VB.",
        "S.60.",
        "In bezug auf Kuno Fischer irrt Volkelt, wenn er (Kants Erkenntnistheorie S. 198 f.",
        "Anmerkung) sagt, es würde «aus der Darstellung K.",
        "Fischers nicht klar, ob seiner Ansicht nach Kant nur die psychologische Tatsächlichkeit der allgemeinen und notwendigen Urteile oder zugleich die objektive Gültigkeit und Rechtmäßigkeit derselben voraussetze».",
        "Denn an der angeführten Stelle sagt Fischer, daß die Hauptschwierigkeit der Kritik der reinen Vernunft darin zu suchen sei, daß deren «Grundlegungen ­von gewissen Voraussetzungen abhängig» seien, «die man eingeräumt haben müsse, um das Folgende gelten zu lassen».",
        "Diese Voraussetzun­gen sind auch für Fischer der Umstand, daß «erst die Tatsache der Erkenntnis» festgestellt wird und dann durch Analyse die Erkenntnisvermögen gefunden, «aus denen jene Tatsache selbst erklärt wird»."
      ],
      [
        "auf den Umstand, daß Kant die apriorische Gültigkeit der reinen Mathematik und Naturlehre als Voraussetzung an die Spitze seiner Erörterungen stellt."
      ],
      [
        "Daß wir wirklich Erkenntnisse haben, die von aller Er­fahrung unabhängig sind, und daß die letzteren nur Ein­sichten von komparativer Allgemeinheit liefern, könnten wir nur als Folgesätze von anderen Urteilen gelten lassen.",
        "Es müßte diesen Behauptungen unbedingt eine Untersuchung über das Wesen der Erfahrung und eine solche über das Wesen unseres Erkennens vorangehen.",
        "Aus jener könnte der erste, aus dieser der zweite der obigen Sätze folgen."
      ],
      [
        "Nun könnte man auf unsere der Vernunftkritik gegen­über geltend gemachten Einwände noch folgendes erwidern.",
        "Man könnte sagen, daß doch jede Erkenntnistheorie den Leser erst dahin führen müsse, wo der voraussetzungslose Ausgangspunkt zu finden ist.",
        "Denn was wir zu irgendeinem Zeitpunkte unseres Lebens als Erkenntnisse besitzen, hat sich weit von diesem Ausgangspunkte entfernt, und wir müssen erst wieder künstlich zu ihm zurückgeführt werden.",
        "In der Tat ist eine solche rein didaktische Verständigung über den Anfang seiner Wissenschaft für jeden Erkenntnistheoretiker eine Notwendigkeit.",
        "Dieselbe muß sich aber jedenfalls darauf beschränken, zu zeigen, inwiefern der in Rede stehende Anfang des Erkennens wirklich ein solcher ist, sie müßte in rein selbstverständlichen analytischen Sät­zen verlaufen und keinerlei wirkliche inhaltsvolle Behauptungen"
      ],
      [
        "aufstellen, die den Inhalt der folgenden Erörterun­gen beeinflussen, wie das bei Kant der Fall ist.",
        "Auch obliegt es dem Erkenntnistheoretiker, zu zeigen, daß der von ihm angenommene Anfang wirklich voraussetzungslos ist.",
        "Aber alles das hat mit dem Wesen dieses Anfanges selbst nichts zu tun, steht ganz außerhalb desselben, sagt nichts über ihn aus.",
        "Auch am Beginne des Mathematikunterrichts muß ich mich ja bemühen, den Schüler von dem axiomatischen Cha­rakter gewisser Wahrheiten zu überzeugen.",
        "Aber niemand wird behaupten wollen, daß der Inhalt der Axiome von diesen vorher angestellten Erwägungen abhängig gemacht wird*.",
        "Genau in derselben Weise müßte der Erkenntnistheoretiker in seinen einleitenden Bemerkungen den Weg zeigen, wie man zu einem voraussetzungslosen Anfang kommen kann; der eigentliche Inhalt aber desselben muß von diesen Erwägungen unabhängig sein.",
        "Von einer solchen Einleitung in die Erkenntnistheorie ist der aber jedenfalls weit entfernt, der wie Kant am Anfange Behauptungen mit ganz bestimmtem, dogmatischem Charakter aufstellt."
      ],
      [
        "-032-* Inwiefern wir mit unseren eigenen erkenntnistheoretischen Er­wägungen ganz in derselben Weise vorgehen, zeigen wir in Kapitel IV: Die Ausgangspunkte der Erkenntnistheorie."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "III. DIE ERKENNTNISTHEORIE NACH KANT",
    "paragraphs": [
      "GA003 - Wahrheit und Wissenschaft",
      "Von der fehlerhaften Fragestellung bei Kant sind nun alle nachfolgenden Erkenntnistheoretiker mehr oder weniger beeinflußt worden. Bei Kant tritt die Anschauung, daß alle uns gegebenen Gegenstände unsere Vorstellungen seien, als Resultat seines Apriorismus auf.",
      "Seither ist sie nun zum Grundsatze und Ausgangspunkte fast aller erkenntnistheo­retischen Systeme gemacht worden. Was uns zunächst und unmittelbar als gewiß feststehe, sei einzig und allein der Satz, daß wir ein Wissen von unseren Vorstellungen haben; das ist zu einer fast allgemein geltenden Überzeugung der Philosophen geworden.",
      "Schulze behauptet bereits 1792 in seinem «Anesidemus», daß alle unsere Erkenntnisse bloße Vorstellungen seien, und daß wir über unsere Vor­stellungen nie hinausgehen können. Schopenhauer vertritt mit dem ihm eigenen philosophischen Pathos die Ansicht. daß der bleibende Gewinn der Kantschen Philosophie die Ansicht sei, daß die Welt «meine Vorstellung» ist, Ed. v.",
      "Hartmann findet diesen Satz so unantastbar, daß er in sei­ner Schrift «Kritische Grundlegung des transzendentalen Realismus» überhaupt nur solche Leser voraussetzt, die sich von der naiven Identifikation ihres Wahrnehmungsbildes mit dem Dinge an sich kritisch losgerungen haben und sich die absolute Heterogeneität eines durch den Vorstellungs­akt als subjektiv-idealen Bewußtseinsinhalts gegebenen An­schauungsobjekts und eines von dem Vorstellungsakt und der Form des Bewußtseins unabhängigen, an und für sich bestehenden Dinges zur Evidenz gebracht haben, d. i. solche,",
      "die von der Überzeugung durchdrungen sind, daß die Ge­samtheit dessen, was uns unmittelbar gegeben ist, Vorstellungen seien*. In seiner letzten erkenntnistheoretischen Pu­blikation sucht Hartmann diese seine Ansicht allerdings auch noch zu begründen.",
      "Wie sich eine vorurteilsfreie Er­kenntnistheorie zu einer solchen Begründung stellen muß, werden unsere weiteren Ausführungen zeigen. Otto Liebmann spricht als sakrosankten obersten Grundsatz aller Erkenntnislehre den aus: «Das Bewußtsein kann sich selbst nicht überspringen**»Volkelt hat das Urteil, daß die erste unmittelbarste Wahrheit die sei: «all unser Wissen erstrecke sich zunächst nur auf unsere Vorstellungen», das positivistische Erkenntnisprinzip genannt, und er betrach­tet nur diejenige Erkenntnistheorie als «eminent kritisch», welche dieses «Prinzip, als das im Anfange des Philosophie­rens einzig Feststehende an die Spitze stellt und es dann konsequent durchdenkt ~ Bei anderen Philosophen fin­det man wieder andere Behauptungen an die Spitze der Er­kenntnistheorie gestellt, z.",
      "B. die, daß das eigentliche Pro­blem derselben in der Frage bestehe nach dem Verhältnis zwischen Denken und Sein und der Möglichkeit einer Ver­mittlung zwischen beiden**** oder auch in der: wie wird das Seiende bewußt (Rehmke) usw. Kirchmann geht von zwei erkenntnistheoretischen Axiomen aus: «das Wahrge­nommene ist»und «der Widerspruch ist nicht ~ Nach E.",
      "Fischer besteht das Erkennen in dem Wissen von einem Tatsächlichen, Realen******, und er läßt dieses Dogma ebenso ungeprüft wie Göring, der ähnliches behauptet:",
      "-035-* Kritische Grundlegung, Vorrede S.10.",
      "-035-** Zur Analysis S.28 ff",
      "-035-***    Kants Erkenntnistheorie § 1.",
      "-035-**** Dorner, Das menschliche Er­kennen.",
      "-035-***** Die Lehre vom Wissen.",
      "-035-****** Grundfragen S. 385.",
      "«Erkennen heißt immer, ein Seiendes erkennen, das ist Tatsache, welche weder Skeptizismus noch Kantscher Kri­tizismus leugnen kann». Bei den beiden letzteren wird einfach dekretiert: das ist Erkennen, ohne zu fragen, mit welchem Rechte denn dies geschehen kann.",
      "Selbst wenn diese verschiedenen Behauptungen richtig wären, oder zu richtigen Problemstellungen führten, könn­ten sie durchaus nicht am Anfange der Erkenntnistheorie zur Erörterung kommen. Denn sie stehen, als ganz be­stimmte Einsichten, alle schon innerhalb des Gebietes des Erkennens. Wenn ich sage: mein Wissen erstreckt sich zu­nächst nur auf meine Vorstellungen, so ist das doch ein ganz bestimmtes Erkenntnisurteil. Ich füge durch diesen Satz der mir gegebenen Welt ein Prädikat bei, nämlich die Exi­stenz in Form der Vorstellung. Woher aber soll ich vor allem Erkennen wissen, daß die mir gegebenen Dinge Vor­stellungen sind?",
      "Wir werden uns von der Richtigkeit der Behauptung, daß dieser Satz nicht an die Spitze der Erkenntnistheorie ge­stellt werden darf, am besten überzeugen, wenn wir den Weg verfolgen, den der menschliche Geist nehmen muß, um zu ihm zu kommen. Der Satz ist fast ein Bestandteil des ganzen modernen wissenschaftlichen Bewußtseins geworden. Die Erwägungen, die dasselbe zu ihm hingedrängt haben, finden sich in ziemlicher Vollständigkeit systematisch zu­sammengestellt in dem 1. Abschnitt von Ed. v. Hartmanns Schrift: «Das Grundproblem der Erkenntnistheorie». Das in derselben Vorgebrachte kann somit als eine Art von Leit­faden dienen, wenn man sich zur Aufgabe macht, alle Gründe zu erörtern, die zu jener Annahme führen können",
      "-036-* System S. 257.",
      "Diese Gründe sind physikalische, psycho-physische, phy­siologische und eigentlich philosophische.",
      "Der Physiker gelangt durch Beobachtung derjenigen Er­scheinungen, die sich in unserer Umgebung abspielen, wenn wir z. B. eine Schallempfindung haben, zu der Annahme, daß in diesen Erscheinungen nichts liege, das mit dem auch nur die entfernteste Ähnlichkeit hätte, was wir unmittelbar als Schall wahrnehmen.",
      "Draußen, in dem uns umgebenden Raume, sind lediglich longitudinale Schwingungen der Körper und der Luft aufzufinden. Daraus wird gefolgert, daß das, was wir im gewöhnlichen Leben Schall oder Ton nennen, lediglich eine subjektive Reaktion unseres Organis­mus auf jene Wellenbewegung sei.",
      "Ebenso findet man, daß das Licht und die Farbe oder die Wärme etwas rein Subjek­tives sind. Die Erscheinungen der Farbenzerstreuung, der Brechung, Interferenz und Polarisation belehren uns, daß den obengenannten Empfindungsqualitäten im Außenraume gewisse transversale Schwingungen entsprechen, die wir teils den Körpern, teils einem unmeßbar feinen, elastischen Fluidum, dem Äther, zuzuschreiben uns veranlaßt fühlen.",
      "Ferner sieht sich der Physiker gezwungen, aus gewissen Er­scheinungen in der Körperwelt den Glauben an die Kon­tinuität der Gegenstände im Raume aufzugeben und die­selben auf Systeme von kleinsten Teilen (Molekülen, Ato­men) zurückzuführen, deren Größen im Verhältnisse zu ihren Entfernungen unmeßbar klein sind. Daraus wird ge­schlossen, daß alle Wirkung der Körper aufeinander durch den leeren Raum hindurch geschehe, somit eine wahre actio in distans sei.",
      "Die Physik glaubt sich berechtigt anzuneh­men, daß die Wirkung der Körper auf unseren Tast- und Wärmesinn nicht durch unmittelbare Berührung geschehe,",
      "weil ja immer eine gewisse, wenn auch kleine, Entfernung zwischen der den Körper berührenden Hautstelle und die­sem selbst da sein müsse. Daraus ergebe sich, daß das, was wir z.B. als Härte oder Wärme der Körper empfinden, nur Reaktionen unserer Tast- und Wärmenerven-End­organe auf die durch den leeren Raum hindurch wirkenden Molekularkräfte der Körper seien.",
      "Als Ergänzung treten zu diesen Erwägungen des Physi­kers jene des Psycho-Physikers hinzu, die in der Lehre von den spezifischen Sinnes-Energien ihren Ausdruck finden. J. Müller hat gezeigt, daß jeder Sinn nur in der ihm eigen­tümlichen, durch seine Organisation bedingten Weise affi­ziert werden kann, und daß er immer in derselben Weise reagiert, was auch immer für ein äußerer Eindruck auf ihn ausgeübt wird. Wird der Sehnerv erregt, so empfinden wir Licht, gleichgültig, ob es Druck oder elektrischer Strom oder Licht ist, was auf den Nerv einwirkt. Andererseits erzeugen dieselben äußeren Vorgänge ganz verschiedene Empfindungen, je nachdem sie von diesem oder jenem Sinne perzipiert werden. Daraus hat man gefolgert, daß es nur eine Art von Vorgängen in der Außenwelt gebe, nämlich Bewegungen, und daß die Mannigfaltigkeit der von uns wahrgenommenen Welt wesentlich eine Reaktion unserer Sinne auf diese Vorgänge sei. Nach dieser Ansicht nehmen wir nicht die Außenwelt als solche wahr, sondern bloß die in uns von ihr ausgelösten, subjektiven Empfindungen.",
      "Zu den Erwägungen der Physik treten auch noch jene der Physiologie. Jene verfolgt die außer unserem Organismus vor sich gehenden Erscheinungen, welche den Wahrneh­mungen korrespondieren; diese sucht die Vorgänge im eige­nen Leibe des Menschen zu erforschen, die sich abspielen,",
      "während in uns eine gewisse Sinnesqualität ausgelöst wird. Die Physiologie lehrt, daß die Epidermis gegen Reize der Außenwelt vollständig unempfindlich ist. Wenn also z. B. die Endorgane unserer Tastnerven an der Körperperipherie von den Einwirkungen der Außenwelt affiziert werden sollen, so muß der Schwingungsvorgang, der außerhalb un­seres Leibes liegt, erst durch die Epidermis fortgepflanzt werden. Beim Gehör- und Gesichtssinne wird außerdem der äußere Bewegungsvorgang durch eine Reihe von Orga­nen in den Sinneswerkzeugen verändert, bevor er an den Nerv herankommt. Diese Affektion der Endorgane muß nun durch den Nerv bis zum Zentralorgan geleitet werden, und hier erst kann sich das vollziehen, wodurch auf Grund von rein mechanischen Vorgängen im Gehirne die Emp­findung erzeugt wird. Es ist klar, daß durch diese Umfor­mungen, die der Reiz, der auf die Sinnesorgane ausgeübt wird, erleidet, derselbe so vollständig umgewandelt wird, daß jede Spur von Ahnlichkeit zwischen der ersten Ein­wirkung auf die Sinne und der zuletzt im Bewußtsein auf­tretenden Empfindung verwischt sein muß. Hartmann spricht das Ergebnis dieser Überlegung mit folgenden Wor­ten aus: «Dieser Bewußtseinsinhalt besteht ursprünglich aus Empfindungen, mit welchen die Seele auf die Be­wegungszustände ihres obersten Hirnzentrums reflektorisch reagiert, welche aber mit den molekularen Bewegungs­zuständen, durch welche sie ausgeübt werden, nicht die ge­ringste Ähnlichkeit haben.",
      "Wer diesen Gedankengang vollständig bis ans Ende durchdenkt, muß zugeben, daß, wenn er richtig ist, auch nicht der geringste Rest von dem, was man äußeres Dasein nennen kann, in unserem Bewußtseinsinhalt enthalten wäre.",
      "Hartmann fügt zu den physikalischen und physiologischen Einwänden gegen den sogenannten «naiven Realismus »noch solche, die er im eigentlichen Sinne philosophische nennt, hinzu. Bei einer logischen Durchmusterung der beiden ersten Einwände bemerken wir, daß wir im Grunde doch nur dann zu dem angezeigten Resultate kommen können, wenn wir von dem Dasein und dem Zusammenhange der äußeren Dinge, wie sie das gewöhnliche naive Bewußtsein annimmt, ausgehen und dann untersuchen, wie diese Außen­welt bei unserer Organisation in unser Bewußtsein kommen kann.",
      "Wir haben gesehen, daß uns jede Spur von einer sol­chen Außenwelt auf dem Wege vom Sinneseindruck bis zum Eintritt in das Bewußtsein verlorengeht, und in dem letzteren nichts als unsere Vorstellungen übrig bleiben. Wir müssen daher annehmen, daß jenes Bild der Außenwelt, das wir wirklich haben, von der Seele auf Grund des Emp­findungsmaterials aufgebaut werde.",
      "Zunächst wird aus den Empfindungen des Gesichts- und des Tastsinns ein räum­liches Weltbild konstruiert, in das dann die Empfindungen der übrigen Sinne eingefügt werden. Wenn wir uns ge­zwungen sehen, einen bestimmten Komplex von Empfin­dungen zusammenhängend zu denken, so kommen wir zum Begriffe der Substanz, die wir als Träger derselben ansehen.",
      "Bemerken wir, daß an einer Substanz Empfindungsqualitäten verschwinden und andere wieder auftauchen, so schrei­ben wir solches einem durch das Gesetz der Kausalität ge­regelten Wechsel in der Erscheinungswelt zu. So setzt sich, nach dieser Auffassung, unser ganzes Weltbild aus sub­jektivem Empfindungsinhalt zusammen, der durch die eigene Seelentätigkeit geordnet wird.",
      "Hartmann sagt:",
      "«Was das Subjekt wahrnimmt, sind also immer nur Mo­difikationen",
      "seiner eigenen psychischen Zustände und nichts anderes*.»",
      "Fragen wir uns nun: wie kommen wir zu einer solchen Überzeugung? Das Skelett des angestellten Gedankengan­ges ist folgendes: Wenn eine Außenwelt existiert, so wird sie von uns nicht als solche wahrgenommen, sondern durch unsere Organisation in eine Vorstellungswelt umgewandelt. Wir haben es hier mit einer Voraussetzung zu tun, die, kon­sequent verfolgt, sich selbst aufhebt. Ist dieser Gedankengang aber geeignet, irgendeine Überzeugung zu begrün­den? Sind wir berechtigt, das uns gegebene Weltbild deshalb als subjektiven Vorstellungsinhalt anzusehen, weil die An­nahme des naiven Bewußtseins, strenge durchgedacht, zu dieser Ansicht führt? Unser Ziel ist ja doch, diese Annahme selbst als ungültig zu erweisen. Dann müßte es möglich sein, daß eine Behauptung sich als falsch erwiese und doch das Resultat, zu dem sie gelangt, ein richtiges sei. Das kann ja immerhin irgendwo vorkommen; aber nimmermehr kann dann das Resultat als aus jener Behauptung erwiesen an­gesehen werden.",
      "Man nennt gewöhnlich die Weltansicht, welche die Reali­tät des uns unmittelbar gegebenen Weltbildes wie etwas nicht weiter Anzuzweifelndes, Selbstverständliches hin­nimmt, naiven Realismus. Die entgegengesetzte dagegen, die dieses Weltbild bloß für unseren Bewußtseinsinhalt hält, transzendentalen Idealismus. Wir können somit auch das Ergebnis der vorangehenden Erwägungen mit folgenden Worten zusammenfassen: Der transzendentale Idealismus erweist seine Richtigkeit, indem er mit den Mitteln des naiven Realismus, dessen Widerlegung er anstrebt, operiert.",
      "-041-* Grundproblem S. 37.",
      "Er ist berechtigt, wenn der naive Realismus falsch ist; aber die Falschheit wird nur mit Hilfe der falschen Ansicht selbst bewiesen. Wer sich dieses vor Augen bringt, für den bleibt nichts übrig, als den Weg zu verlassen, der hier eingeschla­gen wird, um zu einer Weltansicht zu gelangen, und einen anderen zu gehen.",
      "Soll das aber, auf gut Glück, versuchs­weise geschehen, bis wir zufällig auf das Rechte treffen? Ed. v. Hartmann ist allerdings dieser Ansicht, wenn er die Gültigkeit seines erkenntnistheoretischen Standpunktes da­mit dargetan zu haben glaubt, daß dieser die Welterschei­nungen erklärt, während die anderen das nicht tun.",
      "Nach der Ansicht dieses Denkers nehmen die einzelnen Welt­anschauungen eine Art von Kampf ums Dasein auf, und diejenige, welche sich in demselben am besten bewährt, wird zuletzt als Siegerin akzeptiert. Aber ein solches Ver­fahren scheint uns schon deshalb unstatthaft, weil es ja ganz gut mehrere Hypothesen geben könnte, die gleich befrie­digend zur Erklärung der Welterscheinungen führen.",
      "Des­halb wollen wir uns lieber an den obigen Gedankengang zur Widerlegung des naiven Realismus halten und nach­sehen, wo eigentlich sein Mangel liegt. Der naive Realismus ist doch diejenige Auffassung, von der alle Menschen aus­gehen.",
      "Schon deshalb empfiehlt es sich, die Korrektur ge­rade bei ihm zu beginnen. Haben wir dann eingesehen, warum er mangelhaft sein muß, dann werden wir mit ganz anderer Sicherheit auf einen richtigen Weg geführt werden, als wenn wir einen solchen einfach auf gut Glück versuchen.",
      "Der oben skizzierte Subjektivismus beruht auf einer den­kenden Verarbeitung gewisser Tatsachen. Er setzt also voraus, daß, von einem tatsächlichen Ausgangspunkte aus, durch folgerichtiges Denken (logische Kombination be­stimmter",
      "Beobachtungen) richtige Überzeugungen gewon­nen werden können. Das Recht zu einer solchen Anwen­dung unseres Denkens wird aber auf diesem Standpunkt nicht geprüft. Und darin liegt seine Schwäche. Während der naive Realismus von der ungeprüften Annahme ausgeht, daß der von uns wahrgenommene Erfahrungsinhalt objek­tive Realität habe, geht der charakterisierte Standpunkt von der ebenfalls ungeprüften Überzeugung aus, daß man durch Anwendung des Denkens zu wissenschaftlich berech­tigten Überzeugungen kommen könne.",
      "Im Gegensatz zum naiven Realismus kann man diesen Standpunkt naiven Rationalismus nennen. Um diese Terminologie zu recht­fertigen, möchten wir hier eine kurze Bemerkung über den Begriff des «Naiven»einschalten.",
      "Doring sucht diesen Begriff in seinem Aufsatze: «Über den Begriff des naiven Realismus»naher zu bestimmen*. Er sagt darüber: «Der Begriff der Naivität bezeichnet gleichsam den Nullpunkt auf der Skala der Reflektion über das eigene Verhalten.",
      "In­haltlich kann die Naivität durchaus das Richtige treffen, denn sie ist zwar reflexionslos und eben darum kritiklos oder unkritisch, aber dies Fehlen der Reflexion und Kritik schließt nur die objektive Sicherheit des Richtigen aus; es schließt die Möglichkeit und Gefahr des Verfehlens, keines­wegs die Notwendigkeit desselben in sich. Es gibt eine Naivität des Fühlens und Wollens, wie des Vorstellens und Denkens im weitesten Sinne des letzteren Wortes, ferner eine Naivität der Äußerungen dieser inneren Zustände im Gegensatz gegen die durch Rücksichten, Reflexion bewirkte Repression oder Modifikation derselben.",
      "Die Naivität ist, wenigstens bewußt, nicht beeinflußt vom Hergebrachten,",
      "-043-*    Philosophische Monatshefte Bd. XXVI, 5.390, Heidelberg 1890.",
      "Angelernten und Vorschriftsmäßigen, sie ist auf allen Ge­bieten, was das Stammwort nativus ausdrückt, das Unbe­wußte, Impulsive, Instinktive, Dämonische.»Wir wollen, von diesen Sätzen ausgehend, den Begriff des Naiven doch noch etwas präziser fassen. Bei aller Tätigkeit, die wir voll­bringen, kommt zweierlei in Betracht: die Tätigkeit selbst und das Wissen um deren Gesetzmäßigkeit.",
      "Wir können in der ersten vollständig aufgehen, ohne nach der letzteren zu fragen. Der Künstler, der die Gesetze seines Schaffens nicht in reflexionsmäßiger Form kennt, sondern sie dem Gefühle, der Empfindung nach übt, ist in diesem Falle.",
      "Wir nennen ihn naiv. Aber es gibt eine Art von Selbstbeobach­tung, die sich um die Gesetzlichkeit des eigenen Tuns fragt, und welche für die soeben geschilderte Naivität das Be­wußtsein eintauscht, daß sie genau die Tragweite und Be­rechtigung dessen kennt, was sie vollführt.",
      "Diese wollen wir kritisch nennen. Wir glauben damit am besten den Sinn dieses Begriffes zu treffen, wie er sich seit Kant mit mehr oder minder klarem Bewußtsein in der Philosophie eingebürgert hat. Kritische Besonnenheit ist demnach das Ge­genteil von Naivität.",
      "Wir nennen ein Verhalten kritisch, das sich der Gesetze der eigenen Tätigkeit bemächtigt, um deren Sicherheit und Grenzen kennen zu lernen. Die Er­kenntnistheorie kann aber nur eine kritische Wissenschaft sein.",
      "Ihr Objekt ist ja ein eminent subjektives Tun des Men­schen: das Erkennen, und was sie darlegen will, ist die Gesetzmäßigkeit des Erkennens. Von dieser Wissenschaft muß also alle Naivität ausgeschlossen sein.",
      "Sie muß gerade dar­innen ihre Stärke sehen, daß sie dasjenige vollzieht, von dem sich viele aufs Praktische gerichtete Geister rühmen, es nie getan zu haben, nämlich das «Denken über das Denken»."
    ],
    "sentences": [
      [
        "GA003 - Wahrheit und Wissenschaft"
      ],
      [
        "Von der fehlerhaften Fragestellung bei Kant sind nun alle nachfolgenden Erkenntnistheoretiker mehr oder weniger beeinflußt worden.",
        "Bei Kant tritt die Anschauung, daß alle uns gegebenen Gegenstände unsere Vorstellungen seien, als Resultat seines Apriorismus auf."
      ],
      [
        "Seither ist sie nun zum Grundsatze und Ausgangspunkte fast aller erkenntnistheo­retischen Systeme gemacht worden.",
        "Was uns zunächst und unmittelbar als gewiß feststehe, sei einzig und allein der Satz, daß wir ein Wissen von unseren Vorstellungen haben; das ist zu einer fast allgemein geltenden Überzeugung der Philosophen geworden."
      ],
      [
        "Schulze behauptet bereits 1792 in seinem «Anesidemus», daß alle unsere Erkenntnisse bloße Vorstellungen seien, und daß wir über unsere Vor­stellungen nie hinausgehen können.",
        "Schopenhauer vertritt mit dem ihm eigenen philosophischen Pathos die Ansicht. daß der bleibende Gewinn der Kantschen Philosophie die Ansicht sei, daß die Welt «meine Vorstellung» ist, Ed. v."
      ],
      [
        "Hartmann findet diesen Satz so unantastbar, daß er in sei­ner Schrift «Kritische Grundlegung des transzendentalen Realismus» überhaupt nur solche Leser voraussetzt, die sich von der naiven Identifikation ihres Wahrnehmungsbildes mit dem Dinge an sich kritisch losgerungen haben und sich die absolute Heterogeneität eines durch den Vorstellungs­akt als subjektiv-idealen Bewußtseinsinhalts gegebenen An­schauungsobjekts und eines von dem Vorstellungsakt und der Form des Bewußtseins unabhängigen, an und für sich bestehenden Dinges zur Evidenz gebracht haben, d. i. solche,"
      ],
      [
        "die von der Überzeugung durchdrungen sind, daß die Ge­samtheit dessen, was uns unmittelbar gegeben ist, Vorstellungen seien*.",
        "In seiner letzten erkenntnistheoretischen Pu­blikation sucht Hartmann diese seine Ansicht allerdings auch noch zu begründen."
      ],
      [
        "Wie sich eine vorurteilsfreie Er­kenntnistheorie zu einer solchen Begründung stellen muß, werden unsere weiteren Ausführungen zeigen.",
        "Otto Liebmann spricht als sakrosankten obersten Grundsatz aller Erkenntnislehre den aus: «Das Bewußtsein kann sich selbst nicht überspringen**»Volkelt hat das Urteil, daß die erste unmittelbarste Wahrheit die sei: «all unser Wissen erstrecke sich zunächst nur auf unsere Vorstellungen», das positivistische Erkenntnisprinzip genannt, und er betrach­tet nur diejenige Erkenntnistheorie als «eminent kritisch», welche dieses «Prinzip, als das im Anfange des Philosophie­rens einzig Feststehende an die Spitze stellt und es dann konsequent durchdenkt ~ Bei anderen Philosophen fin­det man wieder andere Behauptungen an die Spitze der Er­kenntnistheorie gestellt, z."
      ],
      [
        "B. die, daß das eigentliche Pro­blem derselben in der Frage bestehe nach dem Verhältnis zwischen Denken und Sein und der Möglichkeit einer Ver­mittlung zwischen beiden**** oder auch in der: wie wird das Seiende bewußt (Rehmke) usw.",
        "Kirchmann geht von zwei erkenntnistheoretischen Axiomen aus: «das Wahrge­nommene ist»und «der Widerspruch ist nicht ~ Nach E."
      ],
      [
        "Fischer besteht das Erkennen in dem Wissen von einem Tatsächlichen, Realen******, und er läßt dieses Dogma ebenso ungeprüft wie Göring, der ähnliches behauptet:"
      ],
      [
        "-035-* Kritische Grundlegung, Vorrede S.10."
      ],
      [
        "-035-** Zur Analysis S.28 ff"
      ],
      [
        "-035-*** Kants Erkenntnistheorie § 1."
      ],
      [
        "-035-**** Dorner, Das menschliche Er­kennen."
      ],
      [
        "-035-***** Die Lehre vom Wissen."
      ],
      [
        "-035-****** Grundfragen S. 385."
      ],
      [
        "«Erkennen heißt immer, ein Seiendes erkennen, das ist Tatsache, welche weder Skeptizismus noch Kantscher Kri­tizismus leugnen kann».",
        "Bei den beiden letzteren wird einfach dekretiert: das ist Erkennen, ohne zu fragen, mit welchem Rechte denn dies geschehen kann."
      ],
      [
        "Selbst wenn diese verschiedenen Behauptungen richtig wären, oder zu richtigen Problemstellungen führten, könn­ten sie durchaus nicht am Anfange der Erkenntnistheorie zur Erörterung kommen.",
        "Denn sie stehen, als ganz be­stimmte Einsichten, alle schon innerhalb des Gebietes des Erkennens.",
        "Wenn ich sage: mein Wissen erstreckt sich zu­nächst nur auf meine Vorstellungen, so ist das doch ein ganz bestimmtes Erkenntnisurteil.",
        "Ich füge durch diesen Satz der mir gegebenen Welt ein Prädikat bei, nämlich die Exi­stenz in Form der Vorstellung.",
        "Woher aber soll ich vor allem Erkennen wissen, daß die mir gegebenen Dinge Vor­stellungen sind?"
      ],
      [
        "Wir werden uns von der Richtigkeit der Behauptung, daß dieser Satz nicht an die Spitze der Erkenntnistheorie ge­stellt werden darf, am besten überzeugen, wenn wir den Weg verfolgen, den der menschliche Geist nehmen muß, um zu ihm zu kommen.",
        "Der Satz ist fast ein Bestandteil des ganzen modernen wissenschaftlichen Bewußtseins geworden.",
        "Die Erwägungen, die dasselbe zu ihm hingedrängt haben, finden sich in ziemlicher Vollständigkeit systematisch zu­sammengestellt in dem 1.",
        "Abschnitt von Ed. v.",
        "Hartmanns Schrift: «Das Grundproblem der Erkenntnistheorie».",
        "Das in derselben Vorgebrachte kann somit als eine Art von Leit­faden dienen, wenn man sich zur Aufgabe macht, alle Gründe zu erörtern, die zu jener Annahme führen können"
      ],
      [
        "-036-* System S. 257."
      ],
      [
        "Diese Gründe sind physikalische, psycho-physische, phy­siologische und eigentlich philosophische."
      ],
      [
        "Der Physiker gelangt durch Beobachtung derjenigen Er­scheinungen, die sich in unserer Umgebung abspielen, wenn wir z.",
        "B. eine Schallempfindung haben, zu der Annahme, daß in diesen Erscheinungen nichts liege, das mit dem auch nur die entfernteste Ähnlichkeit hätte, was wir unmittelbar als Schall wahrnehmen."
      ],
      [
        "Draußen, in dem uns umgebenden Raume, sind lediglich longitudinale Schwingungen der Körper und der Luft aufzufinden.",
        "Daraus wird gefolgert, daß das, was wir im gewöhnlichen Leben Schall oder Ton nennen, lediglich eine subjektive Reaktion unseres Organis­mus auf jene Wellenbewegung sei."
      ],
      [
        "Ebenso findet man, daß das Licht und die Farbe oder die Wärme etwas rein Subjek­tives sind.",
        "Die Erscheinungen der Farbenzerstreuung, der Brechung, Interferenz und Polarisation belehren uns, daß den obengenannten Empfindungsqualitäten im Außenraume gewisse transversale Schwingungen entsprechen, die wir teils den Körpern, teils einem unmeßbar feinen, elastischen Fluidum, dem Äther, zuzuschreiben uns veranlaßt fühlen."
      ],
      [
        "Ferner sieht sich der Physiker gezwungen, aus gewissen Er­scheinungen in der Körperwelt den Glauben an die Kon­tinuität der Gegenstände im Raume aufzugeben und die­selben auf Systeme von kleinsten Teilen (Molekülen, Ato­men) zurückzuführen, deren Größen im Verhältnisse zu ihren Entfernungen unmeßbar klein sind.",
        "Daraus wird ge­schlossen, daß alle Wirkung der Körper aufeinander durch den leeren Raum hindurch geschehe, somit eine wahre actio in distans sei."
      ],
      [
        "Die Physik glaubt sich berechtigt anzuneh­men, daß die Wirkung der Körper auf unseren Tast- und Wärmesinn nicht durch unmittelbare Berührung geschehe,"
      ],
      [
        "weil ja immer eine gewisse, wenn auch kleine, Entfernung zwischen der den Körper berührenden Hautstelle und die­sem selbst da sein müsse.",
        "Daraus ergebe sich, daß das, was wir z.B. als Härte oder Wärme der Körper empfinden, nur Reaktionen unserer Tast- und Wärmenerven-End­organe auf die durch den leeren Raum hindurch wirkenden Molekularkräfte der Körper seien."
      ],
      [
        "Als Ergänzung treten zu diesen Erwägungen des Physi­kers jene des Psycho-Physikers hinzu, die in der Lehre von den spezifischen Sinnes-Energien ihren Ausdruck finden.",
        "Müller hat gezeigt, daß jeder Sinn nur in der ihm eigen­tümlichen, durch seine Organisation bedingten Weise affi­ziert werden kann, und daß er immer in derselben Weise reagiert, was auch immer für ein äußerer Eindruck auf ihn ausgeübt wird.",
        "Wird der Sehnerv erregt, so empfinden wir Licht, gleichgültig, ob es Druck oder elektrischer Strom oder Licht ist, was auf den Nerv einwirkt.",
        "Andererseits erzeugen dieselben äußeren Vorgänge ganz verschiedene Empfindungen, je nachdem sie von diesem oder jenem Sinne perzipiert werden.",
        "Daraus hat man gefolgert, daß es nur eine Art von Vorgängen in der Außenwelt gebe, nämlich Bewegungen, und daß die Mannigfaltigkeit der von uns wahrgenommenen Welt wesentlich eine Reaktion unserer Sinne auf diese Vorgänge sei.",
        "Nach dieser Ansicht nehmen wir nicht die Außenwelt als solche wahr, sondern bloß die in uns von ihr ausgelösten, subjektiven Empfindungen."
      ],
      [
        "Zu den Erwägungen der Physik treten auch noch jene der Physiologie.",
        "Jene verfolgt die außer unserem Organismus vor sich gehenden Erscheinungen, welche den Wahrneh­mungen korrespondieren; diese sucht die Vorgänge im eige­nen Leibe des Menschen zu erforschen, die sich abspielen,"
      ],
      [
        "während in uns eine gewisse Sinnesqualität ausgelöst wird.",
        "Die Physiologie lehrt, daß die Epidermis gegen Reize der Außenwelt vollständig unempfindlich ist.",
        "Wenn also z.",
        "B. die Endorgane unserer Tastnerven an der Körperperipherie von den Einwirkungen der Außenwelt affiziert werden sollen, so muß der Schwingungsvorgang, der außerhalb un­seres Leibes liegt, erst durch die Epidermis fortgepflanzt werden.",
        "Beim Gehör- und Gesichtssinne wird außerdem der äußere Bewegungsvorgang durch eine Reihe von Orga­nen in den Sinneswerkzeugen verändert, bevor er an den Nerv herankommt.",
        "Diese Affektion der Endorgane muß nun durch den Nerv bis zum Zentralorgan geleitet werden, und hier erst kann sich das vollziehen, wodurch auf Grund von rein mechanischen Vorgängen im Gehirne die Emp­findung erzeugt wird.",
        "Es ist klar, daß durch diese Umfor­mungen, die der Reiz, der auf die Sinnesorgane ausgeübt wird, erleidet, derselbe so vollständig umgewandelt wird, daß jede Spur von Ahnlichkeit zwischen der ersten Ein­wirkung auf die Sinne und der zuletzt im Bewußtsein auf­tretenden Empfindung verwischt sein muß.",
        "Hartmann spricht das Ergebnis dieser Überlegung mit folgenden Wor­ten aus: «Dieser Bewußtseinsinhalt besteht ursprünglich aus Empfindungen, mit welchen die Seele auf die Be­wegungszustände ihres obersten Hirnzentrums reflektorisch reagiert, welche aber mit den molekularen Bewegungs­zuständen, durch welche sie ausgeübt werden, nicht die ge­ringste Ähnlichkeit haben."
      ],
      [
        "Wer diesen Gedankengang vollständig bis ans Ende durchdenkt, muß zugeben, daß, wenn er richtig ist, auch nicht der geringste Rest von dem, was man äußeres Dasein nennen kann, in unserem Bewußtseinsinhalt enthalten wäre."
      ],
      [
        "Hartmann fügt zu den physikalischen und physiologischen Einwänden gegen den sogenannten «naiven Realismus »noch solche, die er im eigentlichen Sinne philosophische nennt, hinzu.",
        "Bei einer logischen Durchmusterung der beiden ersten Einwände bemerken wir, daß wir im Grunde doch nur dann zu dem angezeigten Resultate kommen können, wenn wir von dem Dasein und dem Zusammenhange der äußeren Dinge, wie sie das gewöhnliche naive Bewußtsein annimmt, ausgehen und dann untersuchen, wie diese Außen­welt bei unserer Organisation in unser Bewußtsein kommen kann."
      ],
      [
        "Wir haben gesehen, daß uns jede Spur von einer sol­chen Außenwelt auf dem Wege vom Sinneseindruck bis zum Eintritt in das Bewußtsein verlorengeht, und in dem letzteren nichts als unsere Vorstellungen übrig bleiben.",
        "Wir müssen daher annehmen, daß jenes Bild der Außenwelt, das wir wirklich haben, von der Seele auf Grund des Emp­findungsmaterials aufgebaut werde."
      ],
      [
        "Zunächst wird aus den Empfindungen des Gesichts- und des Tastsinns ein räum­liches Weltbild konstruiert, in das dann die Empfindungen der übrigen Sinne eingefügt werden.",
        "Wenn wir uns ge­zwungen sehen, einen bestimmten Komplex von Empfin­dungen zusammenhängend zu denken, so kommen wir zum Begriffe der Substanz, die wir als Träger derselben ansehen."
      ],
      [
        "Bemerken wir, daß an einer Substanz Empfindungsqualitäten verschwinden und andere wieder auftauchen, so schrei­ben wir solches einem durch das Gesetz der Kausalität ge­regelten Wechsel in der Erscheinungswelt zu.",
        "So setzt sich, nach dieser Auffassung, unser ganzes Weltbild aus sub­jektivem Empfindungsinhalt zusammen, der durch die eigene Seelentätigkeit geordnet wird."
      ],
      [
        "Hartmann sagt:"
      ],
      [
        "«Was das Subjekt wahrnimmt, sind also immer nur Mo­difikationen"
      ],
      [
        "seiner eigenen psychischen Zustände und nichts anderes*.»"
      ],
      [
        "Fragen wir uns nun: wie kommen wir zu einer solchen Überzeugung?",
        "Das Skelett des angestellten Gedankengan­ges ist folgendes: Wenn eine Außenwelt existiert, so wird sie von uns nicht als solche wahrgenommen, sondern durch unsere Organisation in eine Vorstellungswelt umgewandelt.",
        "Wir haben es hier mit einer Voraussetzung zu tun, die, kon­sequent verfolgt, sich selbst aufhebt.",
        "Ist dieser Gedankengang aber geeignet, irgendeine Überzeugung zu begrün­den?",
        "Sind wir berechtigt, das uns gegebene Weltbild deshalb als subjektiven Vorstellungsinhalt anzusehen, weil die An­nahme des naiven Bewußtseins, strenge durchgedacht, zu dieser Ansicht führt?",
        "Unser Ziel ist ja doch, diese Annahme selbst als ungültig zu erweisen.",
        "Dann müßte es möglich sein, daß eine Behauptung sich als falsch erwiese und doch das Resultat, zu dem sie gelangt, ein richtiges sei.",
        "Das kann ja immerhin irgendwo vorkommen; aber nimmermehr kann dann das Resultat als aus jener Behauptung erwiesen an­gesehen werden."
      ],
      [
        "Man nennt gewöhnlich die Weltansicht, welche die Reali­tät des uns unmittelbar gegebenen Weltbildes wie etwas nicht weiter Anzuzweifelndes, Selbstverständliches hin­nimmt, naiven Realismus.",
        "Die entgegengesetzte dagegen, die dieses Weltbild bloß für unseren Bewußtseinsinhalt hält, transzendentalen Idealismus.",
        "Wir können somit auch das Ergebnis der vorangehenden Erwägungen mit folgenden Worten zusammenfassen: Der transzendentale Idealismus erweist seine Richtigkeit, indem er mit den Mitteln des naiven Realismus, dessen Widerlegung er anstrebt, operiert."
      ],
      [
        "-041-* Grundproblem S. 37."
      ],
      [
        "Er ist berechtigt, wenn der naive Realismus falsch ist; aber die Falschheit wird nur mit Hilfe der falschen Ansicht selbst bewiesen.",
        "Wer sich dieses vor Augen bringt, für den bleibt nichts übrig, als den Weg zu verlassen, der hier eingeschla­gen wird, um zu einer Weltansicht zu gelangen, und einen anderen zu gehen."
      ],
      [
        "Soll das aber, auf gut Glück, versuchs­weise geschehen, bis wir zufällig auf das Rechte treffen?",
        "Ed. v.",
        "Hartmann ist allerdings dieser Ansicht, wenn er die Gültigkeit seines erkenntnistheoretischen Standpunktes da­mit dargetan zu haben glaubt, daß dieser die Welterschei­nungen erklärt, während die anderen das nicht tun."
      ],
      [
        "Nach der Ansicht dieses Denkers nehmen die einzelnen Welt­anschauungen eine Art von Kampf ums Dasein auf, und diejenige, welche sich in demselben am besten bewährt, wird zuletzt als Siegerin akzeptiert.",
        "Aber ein solches Ver­fahren scheint uns schon deshalb unstatthaft, weil es ja ganz gut mehrere Hypothesen geben könnte, die gleich befrie­digend zur Erklärung der Welterscheinungen führen."
      ],
      [
        "Des­halb wollen wir uns lieber an den obigen Gedankengang zur Widerlegung des naiven Realismus halten und nach­sehen, wo eigentlich sein Mangel liegt.",
        "Der naive Realismus ist doch diejenige Auffassung, von der alle Menschen aus­gehen."
      ],
      [
        "Schon deshalb empfiehlt es sich, die Korrektur ge­rade bei ihm zu beginnen.",
        "Haben wir dann eingesehen, warum er mangelhaft sein muß, dann werden wir mit ganz anderer Sicherheit auf einen richtigen Weg geführt werden, als wenn wir einen solchen einfach auf gut Glück versuchen."
      ],
      [
        "Der oben skizzierte Subjektivismus beruht auf einer den­kenden Verarbeitung gewisser Tatsachen.",
        "Er setzt also voraus, daß, von einem tatsächlichen Ausgangspunkte aus, durch folgerichtiges Denken (logische Kombination be­stimmter"
      ],
      [
        "Beobachtungen) richtige Überzeugungen gewon­nen werden können.",
        "Das Recht zu einer solchen Anwen­dung unseres Denkens wird aber auf diesem Standpunkt nicht geprüft.",
        "Und darin liegt seine Schwäche.",
        "Während der naive Realismus von der ungeprüften Annahme ausgeht, daß der von uns wahrgenommene Erfahrungsinhalt objek­tive Realität habe, geht der charakterisierte Standpunkt von der ebenfalls ungeprüften Überzeugung aus, daß man durch Anwendung des Denkens zu wissenschaftlich berech­tigten Überzeugungen kommen könne."
      ],
      [
        "Im Gegensatz zum naiven Realismus kann man diesen Standpunkt naiven Rationalismus nennen.",
        "Um diese Terminologie zu recht­fertigen, möchten wir hier eine kurze Bemerkung über den Begriff des «Naiven»einschalten."
      ],
      [
        "Doring sucht diesen Begriff in seinem Aufsatze: «Über den Begriff des naiven Realismus»naher zu bestimmen*.",
        "Er sagt darüber: «Der Begriff der Naivität bezeichnet gleichsam den Nullpunkt auf der Skala der Reflektion über das eigene Verhalten."
      ],
      [
        "In­haltlich kann die Naivität durchaus das Richtige treffen, denn sie ist zwar reflexionslos und eben darum kritiklos oder unkritisch, aber dies Fehlen der Reflexion und Kritik schließt nur die objektive Sicherheit des Richtigen aus; es schließt die Möglichkeit und Gefahr des Verfehlens, keines­wegs die Notwendigkeit desselben in sich.",
        "Es gibt eine Naivität des Fühlens und Wollens, wie des Vorstellens und Denkens im weitesten Sinne des letzteren Wortes, ferner eine Naivität der Äußerungen dieser inneren Zustände im Gegensatz gegen die durch Rücksichten, Reflexion bewirkte Repression oder Modifikation derselben."
      ],
      [
        "Die Naivität ist, wenigstens bewußt, nicht beeinflußt vom Hergebrachten,"
      ],
      [
        "-043-* Philosophische Monatshefte Bd.",
        "XXVI, 5.390, Heidelberg 1890."
      ],
      [
        "Angelernten und Vorschriftsmäßigen, sie ist auf allen Ge­bieten, was das Stammwort nativus ausdrückt, das Unbe­wußte, Impulsive, Instinktive, Dämonische.»Wir wollen, von diesen Sätzen ausgehend, den Begriff des Naiven doch noch etwas präziser fassen.",
        "Bei aller Tätigkeit, die wir voll­bringen, kommt zweierlei in Betracht: die Tätigkeit selbst und das Wissen um deren Gesetzmäßigkeit."
      ],
      [
        "Wir können in der ersten vollständig aufgehen, ohne nach der letzteren zu fragen.",
        "Der Künstler, der die Gesetze seines Schaffens nicht in reflexionsmäßiger Form kennt, sondern sie dem Gefühle, der Empfindung nach übt, ist in diesem Falle."
      ],
      [
        "Wir nennen ihn naiv.",
        "Aber es gibt eine Art von Selbstbeobach­tung, die sich um die Gesetzlichkeit des eigenen Tuns fragt, und welche für die soeben geschilderte Naivität das Be­wußtsein eintauscht, daß sie genau die Tragweite und Be­rechtigung dessen kennt, was sie vollführt."
      ],
      [
        "Diese wollen wir kritisch nennen.",
        "Wir glauben damit am besten den Sinn dieses Begriffes zu treffen, wie er sich seit Kant mit mehr oder minder klarem Bewußtsein in der Philosophie eingebürgert hat.",
        "Kritische Besonnenheit ist demnach das Ge­genteil von Naivität."
      ],
      [
        "Wir nennen ein Verhalten kritisch, das sich der Gesetze der eigenen Tätigkeit bemächtigt, um deren Sicherheit und Grenzen kennen zu lernen.",
        "Die Er­kenntnistheorie kann aber nur eine kritische Wissenschaft sein."
      ],
      [
        "Ihr Objekt ist ja ein eminent subjektives Tun des Men­schen: das Erkennen, und was sie darlegen will, ist die Gesetzmäßigkeit des Erkennens.",
        "Von dieser Wissenschaft muß also alle Naivität ausgeschlossen sein."
      ],
      [
        "Sie muß gerade dar­innen ihre Stärke sehen, daß sie dasjenige vollzieht, von dem sich viele aufs Praktische gerichtete Geister rühmen, es nie getan zu haben, nämlich das «Denken über das Denken»."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "IV. DIE AUSGANGSPUNKTE DER ERKENNTNIS­THEORIE",
    "paragraphs": [
      "IV. DIE AUSGANGSPUNKTE DER ERKENNTNIS­THEORIE",
      "Am Beginne der erkenntnistheoretischen Untersuchungen ist nach allem, was wir gesehen haben, das abzuweisen, was selbst schon in das Gebiet des Erkennens gehört. Die Erkenntnis ist etwas vom Menschen zustande Gebrachtes, etwas durch seine Tätigkeit Entstandenes. Soll sich die Erkenntnistheorie wirklich aufklärend über das ganze Gebiet des Erkennens erstrecken, dann muß sie etwas zum Ausgangspunkte nehmen, was von dieser Tätigkeit ganz unberührt geblieben ist, wovon die letztere vielmehr selbst erst den Anstoß erhält. Womit anzufangen ist, das liegt außerhalb des Erkennens, das kann selbst noch keine Erkenntnis sein. Aber wir haben es unmittelbar vor dem Erkennen zu suchen, so daß schon der nächste Schritt, den der Mensch von demselben aus unternimmt, erkennende Tätigkeit ist. Die Art nun, wie dieses absolut Erste zu bestimmen ist, muß eine solche sein, daß in dieselbe nichts mit einfließt, was schon von einem Erkennen herrührt.",
      "Ein solcher Anfang kann aber nur mit dem unmittelbar gegebenen Weltbilde gemacht werden, d. i. jenem Welt­bilde, das dem Menschen vorliegt, bevor er es in irgend­einer Weise dem Erkenntnisprozesse unterworfen hat, also bevor er auch nur die allergeringste Aussage über dasselbe gemacht, die allergeringste gedankliche Bestimmung mit demselben vorgenommen hat. Was da an uns vorüberzieht, und woran wir vorüberziehen, dieses zusammenhanglose",
      "und doch auch nicht in individuelle Einzelheiten gesonderte* Weltbild, in dem nichts voneinander unterschieden, nichts aufeinander bezogen ist, nichts durch ein anderes bestimmt erscheint: das ist das unmittelbar Gegebene. Auf dieser Stufe des Daseins - wenn wir diesen Ausdruck gebrauchen dürfen - ist kein Gegenstand, kein Geschehnis wichtiger, bedeutungsvoller als ein anderer bzw. ein anderes. Das ru­dimentäre Organ des Tieres, das vielleicht für eine spätere, schon durch das Erkennen erhellte Stufe des Daseins ohne alle Bedeutung für die Entwicklung und das Leben dessel­ben ist, steht gerade mit demselben Anspruch auf Beach­tung da, wie der edelste, notwendigste Teil des Organismus. Vor aller erkennenden Tätigkeit stellt sich im Weltbilde nichts als Substanz, nichts als Akzidenz, nichts als Ursache oder Wirkung dar; die Gegensätze von Materie und Geist, von Leib und Seele sind noch nicht geschaffen. Aber auch jedes andere Prädikat müssen wir von dem auf dieser Stufe festgehaltenen Weltbilde fernhalten. Es kann weder als Wirklichkeit noch als Schein, weder als subjektiv noch als objektiv, weder als zufällig noch als notwendig aufgefaßt werden; ob es «Ding an sich»oder bloße Vorstellung ist, darüber ist auf dieser Stufe nicht zu entscheiden. Denn daß die Erkenntnisse der Physik und Physiologie, die zur Sub­summierung des Gegebenen unter eine der obigen Katego­rien verleiten, nicht an die Spitze der Erkenntnistheorie gestellt werden dürfen, haben wir bereits gesehen.",
      "Wenn ein Wesen mit vollentwickelter, menschlicher In­telligenz plötzlich aus dem Nichts geschaffen würde und der Welt gegenüberträte, so wäre der erste Eindruck, den",
      "-046-* Das Absondern individueller Einzelheiten aus dem ganz unter­schiedlosen gegebenen Weltbild ist schon ein Akt gedanklicher Tätigkeit.",
      "letztere auf seine Sinne und sein Denken machte, etwa das, was wir mit dem unmittelbar gegebenen Weltbilde bezeich­nen. Dem Menschen liegt dasselbe allerdings in keinem Augenblicke seines Lebens in dieser Gestalt wirklich vor; es ist in seiner Entwicklung nirgends eine Grenze zwischen reinem, passiven Hinauswenden zum unmittelbar Gegebe­nen und dem denkenden Erkennen desselben vorhanden.",
      "Dieser Umstand könnte Bedenken gegen unsere Aufstellung eines Anfangs der Erkenntnistheorie erregen. So sagt z. Ed. v. Hartmann: «Wir fragen nicht, welches der Bewußt­seinsinhalt des zum Bewußtsein erwachenden Kindes oder des auf der untersten Stufe der Lebewesen stehenden Tieres sei, denn davon hat der philosophierende Mensch keine Er­fahrung, und die Schlüsse, durch welche er diesen Bewußt­seinsinhalt primitiver biogenetischer oder ontogenetischer Stufen zu rekonstruieren versucht, müssen doch immer wie­der auf seiner persönlichen Erfahrung fußen.",
      "Wir haben also zunächst festzustellen, was der vom philosophierenden Menschen beim Beginn der philosophischen Reflexion vorgefundene Bewußtseinsinhalt sei*.»Dagegen ist aber ein­zuwenden, daß das Weltbild, das wir am Beginne der phi­losophischen Reflexion haben, schon Prädikate trägt, die nur durch das Erkennen vermittelt sind. Diese dürfen nicht kritiklos hingenommen, sondern müssen sorgfältig aus dem Weltbilde herausgeschält werden, damit es ganz rein von allem durch den Erkenntnisprozeß Hinzugefügten erscheint.",
      "Die Grenze zwischen Gegebenem und Erkanntem wird überhaupt mit keinem Augenblicke der menschlichen Ent­wicklung zusammenfallen, sondern sie muß künstlich gezogen­",
      "-047-* Grundproblem S.1.",
      "werden. Dies aber kann auf jeder Entwicklungsstufe geschehen, wenn wir nur den Schnitt zwischen dem, was ohne gedankliche Bestimmung vor dem Erkennen an uns herantritt, und dem, was durch letzteres erst daraus ge­macht wird, richtig führen.",
      "Nun kann man uns vorwerfen, daß wir eine ganze Reihe von gedanklichen Bestimmungen bereits angehäuft haben, um jenes angeblich unmittelbare Weltbild aus dem durch erkennende Bearbeitung von den Menschen vervollständig­ten herauszuschälen. Aber dagegen ist folgendes zu sagen: was wir an Gedanken aufgebracht haben, sollte ja nicht jenes Weltbild etwa charakterisieren, sollte gar keine Eigenschaft desselben angeben, überhaupt nichts über dasselbe aussagen, sondern nur unsere Betrachtung so lenken, daß sie bis zu jener Grenze geführt wird, wo sich das Erkennen an seinen Anfang gestellt sieht. Von Wahrheit oder Irrtum, Richtigkeit oder Unrichtigkeit jener Ausführungen, die nach unserer Auffassung dem Augenblicke vorangehen, in dem wir am Beginne der Erkenntnistheorie stehen, kann daher nirgends die Rede sein. Dieselben haben nur die Aufgabe, zweckmäßig zu diesem Anfange hinzuleiten. Niemand, der im Begriffe steht, sich mit erkenntnistheoretischen Proble­men zu befassen, steht zugleich dem mit Recht so genannten Anfange des Erkennens gegenüber, sondern er hat bereits, bis zu einem gewissen Grade, entwickelte Erkenntnisse. Aus diesen alles zu entfernen, was durch die Arbeit des Erken­nens gewonnen ist, und den vor derselben liegenden An­fang festzustellen, kann nur durch begriffliche Erwägungen geschehen. Aber den Begriffen kommt auf dieser Stufe kein Erkenntniswert zu, sie haben die rein negative Aufgabe, alles aus dem Gesichtsfelde zu entfernen, was der Erkenntnis",
      "angehört, und dahin zu leiten, wo die letztere erst ein­setzt. Diese Erwägungen sind die Wegweiser zu jenem An­fang, an den der Akt des Erkennens herantritt, gehören aber demselben noch nicht an. Bei allem, was der Erkennt­nistheoretiker vor der Feststellung des Anfangs vorzubrin­gen hat, gibt es also nur Zweckmäßigkeit oder Unzweck­mäßigkeit, nicht Wahrheit oder Irrtum. Aber auch in diesem Anfangspunkte selbst ist aller Irrtum ausgeschlossen, denn der letztere kann erst mit dem Erkennen beginnen, also nicht vor demselben liegen.",
      "Den letzten Satz darf keine andere als die Erkenntnis­theorie für sich in Anspruch nehmen, die von unseren Er­wägungen ausgeht. Wo der Ausgangspunkt von einem Ob­jekte (oder Subjekte) mit einer gedanklichen Bestimmung gemacht wird, da ist der Irrtum allerdings auch im Anfange, nämlich gleich bei dieser Bestimmung, möglich. Es hängt ja die Berechtigung derselben von den Gesetzen ab, welche der Erkenntnisakt zugrunde legt. Dieselbe kann sich aber erst im Verlaufe der erkenntnistheoretischen Untersuchungen ergeben. Nur wenn man sagt: ich sondere alle gedanklichen, durch Erkennen erlangten Bestimmungen aus meinem Weltbilde aus und halte nur alles dasjenige fest, was ohne mein Zutun in den Horizont meiner Beobachtung tritt, dann ist aller Irrtum ausgeschlossen. Wo ich mich grundsätzlich aller Aussage enthalte, da kann ich auch keinen Irrtum begehen.",
      "Insofern der Irrtum erkenntnistheoretisch in Betracht kommt, kann er nur innerhalb des Erkenntnisaktes liegen. Die Sinnestäuschung ist kein Irrtum. Wenn uns der Mond im Aufgangspunkte größer erscheint als im Zenit, so haben wir es nicht mit einem Irrtume, sondern mit einer in den Naturgesetzen wohl begründeten Tatsache zu tun. Ein Fehler­",
      "in der Erkenntnis entstünde erst, wenn wir bei der Kombination der gegebenen Wahrnehmungen im Denken jenes «größer»und «kleiner»in unrichtiger Weise deu­teten. Diese Deutung liegt aber innerhalb des Erkenntnis­aktes.",
      "Will man wirklich das Erkennen in seiner ganzen Wesen­heit begreifen, dann muß man es unzweifelhaft zunächst da erfassen, wo es an seinen Anfang gestellt ist, wo es einsetzt. Auch ist klar, daß dasjenige, was vor diesem Anfang liegt, nicht in die Erklärung des Erkennens mit einbezogen wer­den darf, sondern eben vorausgesetzt werden muß. In das Wesen dessen einzudringen, was hier von uns vorausgesetzt wird, ist Aufgabe der wissenschaftlichen Erkenntnis in ihren einzelnen Zweigen. Hier wollen wir aber nicht besondere Erkenntnisse über dieses oder jenes gewinnen, sondern das Erkennen selbst untersuchen. Erst wenn wir den Erkennt­nisakt begriffen haben, können wir ein Urteil darüber ge­winnen, was die Aussagen über den Weltinhalt für eine Be­deutung haben, die im Erkennen über denselben gemacht werden.",
      "Deshalb enthalten wir uns solange jeglicher Bestimmung über das unmittelbar Gegebene, solange wir nicht wissen, welchen Bezug eine solche Bestimmung zu dem Bestimmten hat. Selbst mit dem Begriff des «Unmittelbar-Gegebenen »sprechen wir nichts über das vor dem Erkennen Liegende aus. Er hat nur den Zweck, auf dasselbe hinzuweisen, den Blick darauf zu richten. Die begriffliche Form ist hier im Anfange der Erkenntnistheorie nur die erste Beziehung, in welche sich das Erkennen zum Weltinhalte setzt. Es ist mit dieser Bezeichnung selbst für den Fall vorgesorgt, daß der gesamte Weltinhalt nur ein Gespinst unseres eigenen «Ich»",
      "ist, daß also der exklusive Subjektivismus zu Recht be­stünde; denn von einem Gegebensein dieser Tatsache kann ja nicht die Rede sein. Sie könnte nur das Ergebnis erken­nender Erwägung sein, d.h. sich durch die Erkenntnis­theorie erst als richtig herausstellen, nicht aber ihr als Vor­aussetzung dienen.",
      "In diesem unmittelbar gegebenen Weltinhalt ist nun alles eingeschlossen, was überhaupt innerhalb des Horizontes unserer Erlebnisse im weitesten Sinne auftauchen kann:",
      "Empfindungen, Wahrnehmungen, Anschauungen, Gefühle, Willensakte, Traum- und Phantasiegebilde, Vorstellungen, Begriffe und Ideen.",
      "Auch die Illusionen und Halluzinationen stehen auf die­ser Stufe ganz gleichberechtigt da mit anderen Teilen des Weltinhalts. Denn welches Verhältnis dieselben zu anderen Wahrnehmungen haben, das kann erst die erkennende Be­trachtung lehren.",
      "Wenn die Erkenntnistheorie von der Annahme ausgeht, daß alles eben Angeführte unser Bewußtseinsinhalt sei, dann entsteht natürlich sofort die Frage: wie kommen wir aus dem Bewußtsein heraus zur Erkenntnis des Seins, wo ist das Sprungbrett, das uns aus dem Subjektiven ins Transsubjektive führt? Für uns liegt die Sache ganz anders. Für uns sind das Bewußtsein sowohl wie die «Ich»-Vorstellung zunächst nur Teile des Unmittelbar-Gegebenen, und wel­ches Verhältnis die ersteren zu den letzteren haben, ist erst ein Ergebnis der Erkenntnis. Nicht vom Bewußtsein aus wollen wir das Erkennen bestimmen, sondern umgekehrt:",
      "vom Erkennen aus das Bewußtsein und das Verhältnis von Subjektivität und Objektivität. Da wir das Gegebene zu­nächst ohne alle Prädikate lassen, so müssen wir fragen:",
      "wie kommen wir überhaupt zu einer Bestimmung desselben, wie ist es möglich, mit dem Erkennen irgendwo anzufan­gen? Wie können wir den einen Teil des Weltbildes z. B. als Wahrnehmung, den andern als Begriff, den einen als Sein, den andern als Schein, jenen als Ursache, diesen als Wir­kung bezeichnen, wie können wir uns selbst von dem Ob­jektiven abscheiden und als «Ich»gegenüber dem «Nicht-Ich» ansehen?",
      "Wir müssen die Brücke von dem gegebenen Weltbilde zu jenem finden, welches wir durch unser Erkennen entwickeln. Dabei begegnen wir aber der folgenden Schwierigkeit. So­lange wir das Gegebene bloß passiv anstarren, können wir nirgends einen Ansatzpunkt finden, an den wir an­knüpfen könnten, um von da aus das Erkennen weiter­zuspinnen. Wir müßten im Gegebenen irgendwo den Ort finden, wo wir eingreifen können, wo etwas dem Erkennen Homogenes liegt. Wäre alles wirklich nur gegeben, dann müßte es beim bloßen Hinausstarren in die Außenwelt und einem völlig gleichwertigen Hineinstarren in die Welt un­serer Individualität sein Bewenden haben. Wir könnten dann die Dinge höchstens als Außenstehende beschreiben, aber niemals sie begreifen. Unsere Begriffe hätten nur einen rein äußerlichen Bezug zu dem, worauf sie sich beziehen, keinen innerlichen. Es hängt für das wahrhafte Erkennen alles davon ab, daß wir irgendwo im Gegebenen ein Gebiet finden, wo unsere erkennende Tätigkeit sich nicht bloß ein Gegebenes voraussetzt, sondern in dem Gegebenen tätig mitten darinnen steht. Mit anderen Worten: Es muß sich gerade bei dem strengen Festhalten an dem Bloß-Gegebe­nen herausstellen, daß nicht alles ein solches ist. Unsere Forderung muß eine solche gewesen sein, daß sie durch ihre",
      "strenge Einhaltung sich teilweise selbst aufhebt. Wir haben sie gestellt, damit wir nicht willkürlich irgend einen Anfang der Erkenntnistheorie festsetzen, sondern denselben wirk­lich aufsuchen. Gegeben in unserem Sinne kann alles wer­den, auch das seiner innersten Natur nach Nicht-Gegebene. Es tritt uns eben dann bloß formell als Gegebenes entgegen, entpuppt sich aber bei genauerer Betrachtung von selbst als das, was es wirklich ist.",
      "Alle Schwierigkeit in dem Begreifen des Erkennens liegt darinnen, daß wir den Weltinhalt nicht aus uns selbst her­vorbringen. Würden wir das, so gäbe es überhaupt kein Er­kennen. Eine Frage für mich kann durch ein Ding nur ent­stehen, wenn es mir «gegeben»wird. Was ich hervorbringe, dem erteile ich seine Bestimmungen; ich brauche also nach ihrer Berechtigung nicht erst zu fragen.",
      "Dies ist der zweite Punkt unserer Erkenntnistheorie. Er besteht in dem Postulat: es muß im Gebiete des Gegebenen etwas liegen, wo unsere Tätigkeit nicht im Leeren schwebt, wo der Inhalt der Welt selbst in diese Tätigkeit eingeht.",
      "Haben wir den Anfang der Erkenntnistheorie in der Weise bestimmt, daß wir ihn völlig vor die erkennende Tätigkeit legten, um durch kein Vorurteil innerhalb des Erkennens dieses selbst zu trüben, so bestimmen wir jetzt den ersten Schritt, den wir in unserer Entwicklung machen, auch so, daß von Irrtum oder Unrichtigkeit nicht die Rede sein kann. Denn wir fällen kein Urteil über irgend etwas, sondern zeigen nur die Forderung auf, die erfüllt werden muß, wenn überhaupt Erkenntnis zustande kommen soll. Es kommt alles darauf an, daß wir mit vollkommener kri­tischer Besonnenheit uns des folgenden bewußt sind: wir stellen das Charakteristikum selbst als Postulat auf, welches­",
      "jener Teil des Weltinhalts haben muß, bei dem wir mit unserer Erkenntnistätigkeit einsetzen können.",
      "Ein anderes ist aber auch durchaus unmöglich. Der Weltinhalt als gegebener ist ja ganz bestimmungslos. Kein Teil kann durch sich selbst den Anstoß geben, von ihm aus den Anfang zu einer Ordnung in diesem Chaos zu machen. Da muß also die erkennende Tätigkeit einen Machtspruch tun und sagen: so und so muß dieser Teil beschaffen sein. Ein solcher Machtspruch tastet auch das Gegebene in keiner Weise in seiner Qualität an. Er bringt keine willkürliche Behauptung in die Wissenschaft. Er behauptet eben gar nichts, sondern er sagt nur: wenn Erkenntnis als möglich erklärbar sein soll, dann muß nach einem Gebiet gesucht werden, wie es oben bezeichnet worden ist. Ist ein solches vorhanden, dann gibt es eine Erklärung des Erkennens, sonst nicht. Während wir den Anfang der Erkenntnistheorie mit dem «Gegebenen»im allgemeinen machten, schränken wir jetzt die Forderung darauf ein, einen bestimmten Punkt desselben ins Auge zu fassen.",
      "Wir wollen nun an unsere Forderung näher herantreten. Wo finden wir irgend etwas in dem Weltbilde, das nicht bloß ein Gegebenes, sondern das nur insofern gegeben ist, als es zugleich ein im Erkenntnisakte Hervorgebrachtes ist?",
      "Wir müssen uns vollständig klar darüber sein, daß wir dieses Hervorbringen in aller Unmittelbarkeit wieder ge­geben haben müssen. Es dürfen nicht etwa Schlußfolgerun­gen nötig sein, um dasselbe zu erkennen. Daraus geht schon hervor, daß die Sinnesqualitäten nicht unserer Forderung genügen. Denn von dem Umstande, daß diese nicht ohne unsere Tätigkeit entstehen, wissen wir nicht unmittelbar, sondern nur durch physikalische und physiologische Erwägungen.",
      "Wohl aber wissen wir unmittelbar, daß Begriffe und Ideen immer erst im Erkenntnisakt und durch diesen in die Sphäre des Unmittelbar-Gegebenen eintreten. Daher täuscht sich auch kein Mensch über diesen Charakter der Begriffe und Ideen.",
      "Man kann eine Halluzination wohl für ein von außen Gegebenes halten, aber man wird niemals von seinen Begriffen glauben, daß sie ohne eigene Denkarbeit uns gegeben werden. Ein Wahnsinniger hält nur Dinge und Verhältnisse, die mit Prädikaten der «Wirklich­keit»ausgestattet sind, für real, obgleich sie es faktisch nicht sind; nie aber wird er von seinen Begriffen und Ideen sagen, daß sie ohne eigene Tätigkeit in die Welt des Ge­gebenen eintreten.",
      "Alles andere in unserem Weltbilde trägt eben einen solchen Charakter, daß es gegeben werden muß, wenn wir es erleben wollen, nur bei Begriffen und Ideen tritt noch das Umgekehrte ein: wir müssen sie hervorbrin­gen, wenn wir sie erleben wollen. Nur die Begriffe und Ideen sind uns in der Form gegeben, die man die intellek­tuelle Anschauung genannt hat.",
      "Kant und die neueren an ihn anknüpfenden Philosophen sprechen dieses Vermögen dem Menschen vollständig ab, weil alles Denken sich nur auf Gegenstände beziehe und aus sich selbst absolut nichts hervorbringe. In der intellektuellen Anschauung muß mit der Denkform zugleich der Inhalt mitgegeben sein.",
      "Ist dies aber nicht bei den reinen Begriffen und Ideen wirklich der Fall? (Unter Begriff verstehe ich eine Regel, nach welcher die zusammenhanglosen Elemente der Wahrnehmung zu einer Einheit verbunden werden. Kausalität z.",
      "B. ist ein Begriff. Idee ist nur ein Begriff mit größerem Inhalt. Or­ganismus, ganz abstrakt genommen, ist eine Idee.) Man muß sie nur in der Form betrachten, in der sie von allem",
      "empirischen Inhalt noch ganz frei sind. Wenn man z. B. den reinen Begriff der Kausalität erfassen will, darf man sich nicht an irgend eine bestimmte Kausalität oder an die Summe aller Kausalitäten halten, sondern an den bloßen Begriff derselben. Ursachen und Wirkungen müssen wir in der Welt aufsuchen, Ursachlichkeit als Gedankenform müs­sen wir selbst hervorbringen, ehe wir die ersteren in der Welt finden können. Wenn man aber an der Kantschen Behauptung festhalten wollte, Begriffe ohne Anschauungen seien leer, so wäre es undenkbar, die Möglichkeit einer Be­stimmung der gegebenen Welt durch Begriffe darzutun. Denn man nehme an, es seien zwei Elemente des Welt­inhaltes gegeben: a und b. Soll ich zwischen denselben ein Verhältnis aufsuchen, so muß ich das an der Hand einer inhaltlich bestimmten Regel tun; diese kann ich aber nur im Erkenntnisakte selbst produzieren, denn aus dem Ob­jekte kann ich sie deshalb nicht nehmen, weil die Bestim­mungen dieses letzteren mit Hilfe der Regel eben erst ge­wonnen werden sollen. Eine solche Regel zur Bestimmung des Wirklichen geht also vollständig innerhalb der rein begrifflichen Entität auf.",
      "Bevor wir nun weiterschreiten, wollen wir erst einen möglichen Einwand beseitigen. Es scheint nämlich, als ob unbewußt in unserem Gedankengange die Vorstellung des «Ich», des «persönlichen Subjekts»eine Rolle spiele, und daß wir diese Vorstellung in dem Fortschritte unserer Ge­dankenentwicklung benützen, ohne die Berechtigung dazu dargetan zu haben. Es ist das der Fall, wenn wir z.B. sagen:",
      "«wir bringen Begriffe hervor»oder «wir stellen diese oder jene Forderung». Aber nichts in unseren Ausführungen gibt Veranlassung, in solchen Sätzen mehr als stilistische Wendungen",
      "zu sehen. Daß der Erkenntnisakt einem «Ich»an­gehört und von demselben ausgeht, das kann, wie wir schon gesagt haben, nur auf Grund erkennender Erwägungen festgestellt werden. Eigentlich müßten wir vorläufig nur von dem Erkenntnisakt sprechen, ohne einen Träger des­selben auch nur zu erwähnen. Denn alles, was bis jetzt feststeht, beschränkt sich darauf, daß ein «Gegebenes vorliegt, und daß aus einem Punkte dieses «Gegebenen das oben angeführte Postulat entspringt; endlich, daß Be­griffe und Ideen das Gebiet sind, das diesem Postulate ent­spricht. Daß der Punkt, aus dem das Postulat entspringt, das «Ich»ist, soll damit nicht geleugnet werden. Aber wir beschränken uns fürs erste darauf, jene beiden Schritte der Erkenntnistheorie in ihrer Reinheit hinzustellen."
    ],
    "sentences": [
      [
        "DIE AUSGANGSPUNKTE DER ERKENNTNIS­THEORIE"
      ],
      [
        "Am Beginne der erkenntnistheoretischen Untersuchungen ist nach allem, was wir gesehen haben, das abzuweisen, was selbst schon in das Gebiet des Erkennens gehört.",
        "Die Erkenntnis ist etwas vom Menschen zustande Gebrachtes, etwas durch seine Tätigkeit Entstandenes.",
        "Soll sich die Erkenntnistheorie wirklich aufklärend über das ganze Gebiet des Erkennens erstrecken, dann muß sie etwas zum Ausgangspunkte nehmen, was von dieser Tätigkeit ganz unberührt geblieben ist, wovon die letztere vielmehr selbst erst den Anstoß erhält.",
        "Womit anzufangen ist, das liegt außerhalb des Erkennens, das kann selbst noch keine Erkenntnis sein.",
        "Aber wir haben es unmittelbar vor dem Erkennen zu suchen, so daß schon der nächste Schritt, den der Mensch von demselben aus unternimmt, erkennende Tätigkeit ist.",
        "Die Art nun, wie dieses absolut Erste zu bestimmen ist, muß eine solche sein, daß in dieselbe nichts mit einfließt, was schon von einem Erkennen herrührt."
      ],
      [
        "Ein solcher Anfang kann aber nur mit dem unmittelbar gegebenen Weltbilde gemacht werden, d. i. jenem Welt­bilde, das dem Menschen vorliegt, bevor er es in irgend­einer Weise dem Erkenntnisprozesse unterworfen hat, also bevor er auch nur die allergeringste Aussage über dasselbe gemacht, die allergeringste gedankliche Bestimmung mit demselben vorgenommen hat.",
        "Was da an uns vorüberzieht, und woran wir vorüberziehen, dieses zusammenhanglose"
      ],
      [
        "und doch auch nicht in individuelle Einzelheiten gesonderte* Weltbild, in dem nichts voneinander unterschieden, nichts aufeinander bezogen ist, nichts durch ein anderes bestimmt erscheint: das ist das unmittelbar Gegebene.",
        "Auf dieser Stufe des Daseins - wenn wir diesen Ausdruck gebrauchen dürfen - ist kein Gegenstand, kein Geschehnis wichtiger, bedeutungsvoller als ein anderer bzw. ein anderes.",
        "Das ru­dimentäre Organ des Tieres, das vielleicht für eine spätere, schon durch das Erkennen erhellte Stufe des Daseins ohne alle Bedeutung für die Entwicklung und das Leben dessel­ben ist, steht gerade mit demselben Anspruch auf Beach­tung da, wie der edelste, notwendigste Teil des Organismus.",
        "Vor aller erkennenden Tätigkeit stellt sich im Weltbilde nichts als Substanz, nichts als Akzidenz, nichts als Ursache oder Wirkung dar; die Gegensätze von Materie und Geist, von Leib und Seele sind noch nicht geschaffen.",
        "Aber auch jedes andere Prädikat müssen wir von dem auf dieser Stufe festgehaltenen Weltbilde fernhalten.",
        "Es kann weder als Wirklichkeit noch als Schein, weder als subjektiv noch als objektiv, weder als zufällig noch als notwendig aufgefaßt werden; ob es «Ding an sich»oder bloße Vorstellung ist, darüber ist auf dieser Stufe nicht zu entscheiden.",
        "Denn daß die Erkenntnisse der Physik und Physiologie, die zur Sub­summierung des Gegebenen unter eine der obigen Katego­rien verleiten, nicht an die Spitze der Erkenntnistheorie gestellt werden dürfen, haben wir bereits gesehen."
      ],
      [
        "Wenn ein Wesen mit vollentwickelter, menschlicher In­telligenz plötzlich aus dem Nichts geschaffen würde und der Welt gegenüberträte, so wäre der erste Eindruck, den"
      ],
      [
        "-046-* Das Absondern individueller Einzelheiten aus dem ganz unter­schiedlosen gegebenen Weltbild ist schon ein Akt gedanklicher Tätigkeit."
      ],
      [
        "letztere auf seine Sinne und sein Denken machte, etwa das, was wir mit dem unmittelbar gegebenen Weltbilde bezeich­nen.",
        "Dem Menschen liegt dasselbe allerdings in keinem Augenblicke seines Lebens in dieser Gestalt wirklich vor; es ist in seiner Entwicklung nirgends eine Grenze zwischen reinem, passiven Hinauswenden zum unmittelbar Gegebe­nen und dem denkenden Erkennen desselben vorhanden."
      ],
      [
        "Dieser Umstand könnte Bedenken gegen unsere Aufstellung eines Anfangs der Erkenntnistheorie erregen.",
        "So sagt z.",
        "Ed. v.",
        "Hartmann: «Wir fragen nicht, welches der Bewußt­seinsinhalt des zum Bewußtsein erwachenden Kindes oder des auf der untersten Stufe der Lebewesen stehenden Tieres sei, denn davon hat der philosophierende Mensch keine Er­fahrung, und die Schlüsse, durch welche er diesen Bewußt­seinsinhalt primitiver biogenetischer oder ontogenetischer Stufen zu rekonstruieren versucht, müssen doch immer wie­der auf seiner persönlichen Erfahrung fußen."
      ],
      [
        "Wir haben also zunächst festzustellen, was der vom philosophierenden Menschen beim Beginn der philosophischen Reflexion vorgefundene Bewußtseinsinhalt sei*.»Dagegen ist aber ein­zuwenden, daß das Weltbild, das wir am Beginne der phi­losophischen Reflexion haben, schon Prädikate trägt, die nur durch das Erkennen vermittelt sind.",
        "Diese dürfen nicht kritiklos hingenommen, sondern müssen sorgfältig aus dem Weltbilde herausgeschält werden, damit es ganz rein von allem durch den Erkenntnisprozeß Hinzugefügten erscheint."
      ],
      [
        "Die Grenze zwischen Gegebenem und Erkanntem wird überhaupt mit keinem Augenblicke der menschlichen Ent­wicklung zusammenfallen, sondern sie muß künstlich gezogen­"
      ],
      [
        "-047-* Grundproblem S.1."
      ],
      [
        "werden.",
        "Dies aber kann auf jeder Entwicklungsstufe geschehen, wenn wir nur den Schnitt zwischen dem, was ohne gedankliche Bestimmung vor dem Erkennen an uns herantritt, und dem, was durch letzteres erst daraus ge­macht wird, richtig führen."
      ],
      [
        "Nun kann man uns vorwerfen, daß wir eine ganze Reihe von gedanklichen Bestimmungen bereits angehäuft haben, um jenes angeblich unmittelbare Weltbild aus dem durch erkennende Bearbeitung von den Menschen vervollständig­ten herauszuschälen.",
        "Aber dagegen ist folgendes zu sagen: was wir an Gedanken aufgebracht haben, sollte ja nicht jenes Weltbild etwa charakterisieren, sollte gar keine Eigenschaft desselben angeben, überhaupt nichts über dasselbe aussagen, sondern nur unsere Betrachtung so lenken, daß sie bis zu jener Grenze geführt wird, wo sich das Erkennen an seinen Anfang gestellt sieht.",
        "Von Wahrheit oder Irrtum, Richtigkeit oder Unrichtigkeit jener Ausführungen, die nach unserer Auffassung dem Augenblicke vorangehen, in dem wir am Beginne der Erkenntnistheorie stehen, kann daher nirgends die Rede sein.",
        "Dieselben haben nur die Aufgabe, zweckmäßig zu diesem Anfange hinzuleiten.",
        "Niemand, der im Begriffe steht, sich mit erkenntnistheoretischen Proble­men zu befassen, steht zugleich dem mit Recht so genannten Anfange des Erkennens gegenüber, sondern er hat bereits, bis zu einem gewissen Grade, entwickelte Erkenntnisse.",
        "Aus diesen alles zu entfernen, was durch die Arbeit des Erken­nens gewonnen ist, und den vor derselben liegenden An­fang festzustellen, kann nur durch begriffliche Erwägungen geschehen.",
        "Aber den Begriffen kommt auf dieser Stufe kein Erkenntniswert zu, sie haben die rein negative Aufgabe, alles aus dem Gesichtsfelde zu entfernen, was der Erkenntnis"
      ],
      [
        "angehört, und dahin zu leiten, wo die letztere erst ein­setzt.",
        "Diese Erwägungen sind die Wegweiser zu jenem An­fang, an den der Akt des Erkennens herantritt, gehören aber demselben noch nicht an.",
        "Bei allem, was der Erkennt­nistheoretiker vor der Feststellung des Anfangs vorzubrin­gen hat, gibt es also nur Zweckmäßigkeit oder Unzweck­mäßigkeit, nicht Wahrheit oder Irrtum.",
        "Aber auch in diesem Anfangspunkte selbst ist aller Irrtum ausgeschlossen, denn der letztere kann erst mit dem Erkennen beginnen, also nicht vor demselben liegen."
      ],
      [
        "Den letzten Satz darf keine andere als die Erkenntnis­theorie für sich in Anspruch nehmen, die von unseren Er­wägungen ausgeht.",
        "Wo der Ausgangspunkt von einem Ob­jekte (oder Subjekte) mit einer gedanklichen Bestimmung gemacht wird, da ist der Irrtum allerdings auch im Anfange, nämlich gleich bei dieser Bestimmung, möglich.",
        "Es hängt ja die Berechtigung derselben von den Gesetzen ab, welche der Erkenntnisakt zugrunde legt.",
        "Dieselbe kann sich aber erst im Verlaufe der erkenntnistheoretischen Untersuchungen ergeben.",
        "Nur wenn man sagt: ich sondere alle gedanklichen, durch Erkennen erlangten Bestimmungen aus meinem Weltbilde aus und halte nur alles dasjenige fest, was ohne mein Zutun in den Horizont meiner Beobachtung tritt, dann ist aller Irrtum ausgeschlossen.",
        "Wo ich mich grundsätzlich aller Aussage enthalte, da kann ich auch keinen Irrtum begehen."
      ],
      [
        "Insofern der Irrtum erkenntnistheoretisch in Betracht kommt, kann er nur innerhalb des Erkenntnisaktes liegen.",
        "Die Sinnestäuschung ist kein Irrtum.",
        "Wenn uns der Mond im Aufgangspunkte größer erscheint als im Zenit, so haben wir es nicht mit einem Irrtume, sondern mit einer in den Naturgesetzen wohl begründeten Tatsache zu tun.",
        "Ein Fehler­"
      ],
      [
        "in der Erkenntnis entstünde erst, wenn wir bei der Kombination der gegebenen Wahrnehmungen im Denken jenes «größer»und «kleiner»in unrichtiger Weise deu­teten.",
        "Diese Deutung liegt aber innerhalb des Erkenntnis­aktes."
      ],
      [
        "Will man wirklich das Erkennen in seiner ganzen Wesen­heit begreifen, dann muß man es unzweifelhaft zunächst da erfassen, wo es an seinen Anfang gestellt ist, wo es einsetzt.",
        "Auch ist klar, daß dasjenige, was vor diesem Anfang liegt, nicht in die Erklärung des Erkennens mit einbezogen wer­den darf, sondern eben vorausgesetzt werden muß.",
        "In das Wesen dessen einzudringen, was hier von uns vorausgesetzt wird, ist Aufgabe der wissenschaftlichen Erkenntnis in ihren einzelnen Zweigen.",
        "Hier wollen wir aber nicht besondere Erkenntnisse über dieses oder jenes gewinnen, sondern das Erkennen selbst untersuchen.",
        "Erst wenn wir den Erkennt­nisakt begriffen haben, können wir ein Urteil darüber ge­winnen, was die Aussagen über den Weltinhalt für eine Be­deutung haben, die im Erkennen über denselben gemacht werden."
      ],
      [
        "Deshalb enthalten wir uns solange jeglicher Bestimmung über das unmittelbar Gegebene, solange wir nicht wissen, welchen Bezug eine solche Bestimmung zu dem Bestimmten hat.",
        "Selbst mit dem Begriff des «Unmittelbar-Gegebenen »sprechen wir nichts über das vor dem Erkennen Liegende aus.",
        "Er hat nur den Zweck, auf dasselbe hinzuweisen, den Blick darauf zu richten.",
        "Die begriffliche Form ist hier im Anfange der Erkenntnistheorie nur die erste Beziehung, in welche sich das Erkennen zum Weltinhalte setzt.",
        "Es ist mit dieser Bezeichnung selbst für den Fall vorgesorgt, daß der gesamte Weltinhalt nur ein Gespinst unseres eigenen «Ich»"
      ],
      [
        "ist, daß also der exklusive Subjektivismus zu Recht be­stünde; denn von einem Gegebensein dieser Tatsache kann ja nicht die Rede sein.",
        "Sie könnte nur das Ergebnis erken­nender Erwägung sein, d.h. sich durch die Erkenntnis­theorie erst als richtig herausstellen, nicht aber ihr als Vor­aussetzung dienen."
      ],
      [
        "In diesem unmittelbar gegebenen Weltinhalt ist nun alles eingeschlossen, was überhaupt innerhalb des Horizontes unserer Erlebnisse im weitesten Sinne auftauchen kann:"
      ],
      [
        "Empfindungen, Wahrnehmungen, Anschauungen, Gefühle, Willensakte, Traum- und Phantasiegebilde, Vorstellungen, Begriffe und Ideen."
      ],
      [
        "Auch die Illusionen und Halluzinationen stehen auf die­ser Stufe ganz gleichberechtigt da mit anderen Teilen des Weltinhalts.",
        "Denn welches Verhältnis dieselben zu anderen Wahrnehmungen haben, das kann erst die erkennende Be­trachtung lehren."
      ],
      [
        "Wenn die Erkenntnistheorie von der Annahme ausgeht, daß alles eben Angeführte unser Bewußtseinsinhalt sei, dann entsteht natürlich sofort die Frage: wie kommen wir aus dem Bewußtsein heraus zur Erkenntnis des Seins, wo ist das Sprungbrett, das uns aus dem Subjektiven ins Transsubjektive führt?",
        "Für uns liegt die Sache ganz anders.",
        "Für uns sind das Bewußtsein sowohl wie die «Ich»-Vorstellung zunächst nur Teile des Unmittelbar-Gegebenen, und wel­ches Verhältnis die ersteren zu den letzteren haben, ist erst ein Ergebnis der Erkenntnis.",
        "Nicht vom Bewußtsein aus wollen wir das Erkennen bestimmen, sondern umgekehrt:"
      ],
      [
        "vom Erkennen aus das Bewußtsein und das Verhältnis von Subjektivität und Objektivität.",
        "Da wir das Gegebene zu­nächst ohne alle Prädikate lassen, so müssen wir fragen:"
      ],
      [
        "wie kommen wir überhaupt zu einer Bestimmung desselben, wie ist es möglich, mit dem Erkennen irgendwo anzufan­gen?",
        "Wie können wir den einen Teil des Weltbildes z.",
        "B. als Wahrnehmung, den andern als Begriff, den einen als Sein, den andern als Schein, jenen als Ursache, diesen als Wir­kung bezeichnen, wie können wir uns selbst von dem Ob­jektiven abscheiden und als «Ich»gegenüber dem «Nicht-Ich» ansehen?"
      ],
      [
        "Wir müssen die Brücke von dem gegebenen Weltbilde zu jenem finden, welches wir durch unser Erkennen entwickeln.",
        "Dabei begegnen wir aber der folgenden Schwierigkeit.",
        "So­lange wir das Gegebene bloß passiv anstarren, können wir nirgends einen Ansatzpunkt finden, an den wir an­knüpfen könnten, um von da aus das Erkennen weiter­zuspinnen.",
        "Wir müßten im Gegebenen irgendwo den Ort finden, wo wir eingreifen können, wo etwas dem Erkennen Homogenes liegt.",
        "Wäre alles wirklich nur gegeben, dann müßte es beim bloßen Hinausstarren in die Außenwelt und einem völlig gleichwertigen Hineinstarren in die Welt un­serer Individualität sein Bewenden haben.",
        "Wir könnten dann die Dinge höchstens als Außenstehende beschreiben, aber niemals sie begreifen.",
        "Unsere Begriffe hätten nur einen rein äußerlichen Bezug zu dem, worauf sie sich beziehen, keinen innerlichen.",
        "Es hängt für das wahrhafte Erkennen alles davon ab, daß wir irgendwo im Gegebenen ein Gebiet finden, wo unsere erkennende Tätigkeit sich nicht bloß ein Gegebenes voraussetzt, sondern in dem Gegebenen tätig mitten darinnen steht.",
        "Mit anderen Worten: Es muß sich gerade bei dem strengen Festhalten an dem Bloß-Gegebe­nen herausstellen, daß nicht alles ein solches ist.",
        "Unsere Forderung muß eine solche gewesen sein, daß sie durch ihre"
      ],
      [
        "strenge Einhaltung sich teilweise selbst aufhebt.",
        "Wir haben sie gestellt, damit wir nicht willkürlich irgend einen Anfang der Erkenntnistheorie festsetzen, sondern denselben wirk­lich aufsuchen.",
        "Gegeben in unserem Sinne kann alles wer­den, auch das seiner innersten Natur nach Nicht-Gegebene.",
        "Es tritt uns eben dann bloß formell als Gegebenes entgegen, entpuppt sich aber bei genauerer Betrachtung von selbst als das, was es wirklich ist."
      ],
      [
        "Alle Schwierigkeit in dem Begreifen des Erkennens liegt darinnen, daß wir den Weltinhalt nicht aus uns selbst her­vorbringen.",
        "Würden wir das, so gäbe es überhaupt kein Er­kennen.",
        "Eine Frage für mich kann durch ein Ding nur ent­stehen, wenn es mir «gegeben»wird.",
        "Was ich hervorbringe, dem erteile ich seine Bestimmungen; ich brauche also nach ihrer Berechtigung nicht erst zu fragen."
      ],
      [
        "Dies ist der zweite Punkt unserer Erkenntnistheorie.",
        "Er besteht in dem Postulat: es muß im Gebiete des Gegebenen etwas liegen, wo unsere Tätigkeit nicht im Leeren schwebt, wo der Inhalt der Welt selbst in diese Tätigkeit eingeht."
      ],
      [
        "Haben wir den Anfang der Erkenntnistheorie in der Weise bestimmt, daß wir ihn völlig vor die erkennende Tätigkeit legten, um durch kein Vorurteil innerhalb des Erkennens dieses selbst zu trüben, so bestimmen wir jetzt den ersten Schritt, den wir in unserer Entwicklung machen, auch so, daß von Irrtum oder Unrichtigkeit nicht die Rede sein kann.",
        "Denn wir fällen kein Urteil über irgend etwas, sondern zeigen nur die Forderung auf, die erfüllt werden muß, wenn überhaupt Erkenntnis zustande kommen soll.",
        "Es kommt alles darauf an, daß wir mit vollkommener kri­tischer Besonnenheit uns des folgenden bewußt sind: wir stellen das Charakteristikum selbst als Postulat auf, welches­"
      ],
      [
        "jener Teil des Weltinhalts haben muß, bei dem wir mit unserer Erkenntnistätigkeit einsetzen können."
      ],
      [
        "Ein anderes ist aber auch durchaus unmöglich.",
        "Der Weltinhalt als gegebener ist ja ganz bestimmungslos.",
        "Kein Teil kann durch sich selbst den Anstoß geben, von ihm aus den Anfang zu einer Ordnung in diesem Chaos zu machen.",
        "Da muß also die erkennende Tätigkeit einen Machtspruch tun und sagen: so und so muß dieser Teil beschaffen sein.",
        "Ein solcher Machtspruch tastet auch das Gegebene in keiner Weise in seiner Qualität an.",
        "Er bringt keine willkürliche Behauptung in die Wissenschaft.",
        "Er behauptet eben gar nichts, sondern er sagt nur: wenn Erkenntnis als möglich erklärbar sein soll, dann muß nach einem Gebiet gesucht werden, wie es oben bezeichnet worden ist.",
        "Ist ein solches vorhanden, dann gibt es eine Erklärung des Erkennens, sonst nicht.",
        "Während wir den Anfang der Erkenntnistheorie mit dem «Gegebenen»im allgemeinen machten, schränken wir jetzt die Forderung darauf ein, einen bestimmten Punkt desselben ins Auge zu fassen."
      ],
      [
        "Wir wollen nun an unsere Forderung näher herantreten.",
        "Wo finden wir irgend etwas in dem Weltbilde, das nicht bloß ein Gegebenes, sondern das nur insofern gegeben ist, als es zugleich ein im Erkenntnisakte Hervorgebrachtes ist?"
      ],
      [
        "Wir müssen uns vollständig klar darüber sein, daß wir dieses Hervorbringen in aller Unmittelbarkeit wieder ge­geben haben müssen.",
        "Es dürfen nicht etwa Schlußfolgerun­gen nötig sein, um dasselbe zu erkennen.",
        "Daraus geht schon hervor, daß die Sinnesqualitäten nicht unserer Forderung genügen.",
        "Denn von dem Umstande, daß diese nicht ohne unsere Tätigkeit entstehen, wissen wir nicht unmittelbar, sondern nur durch physikalische und physiologische Erwägungen."
      ],
      [
        "Wohl aber wissen wir unmittelbar, daß Begriffe und Ideen immer erst im Erkenntnisakt und durch diesen in die Sphäre des Unmittelbar-Gegebenen eintreten.",
        "Daher täuscht sich auch kein Mensch über diesen Charakter der Begriffe und Ideen."
      ],
      [
        "Man kann eine Halluzination wohl für ein von außen Gegebenes halten, aber man wird niemals von seinen Begriffen glauben, daß sie ohne eigene Denkarbeit uns gegeben werden.",
        "Ein Wahnsinniger hält nur Dinge und Verhältnisse, die mit Prädikaten der «Wirklich­keit»ausgestattet sind, für real, obgleich sie es faktisch nicht sind; nie aber wird er von seinen Begriffen und Ideen sagen, daß sie ohne eigene Tätigkeit in die Welt des Ge­gebenen eintreten."
      ],
      [
        "Alles andere in unserem Weltbilde trägt eben einen solchen Charakter, daß es gegeben werden muß, wenn wir es erleben wollen, nur bei Begriffen und Ideen tritt noch das Umgekehrte ein: wir müssen sie hervorbrin­gen, wenn wir sie erleben wollen.",
        "Nur die Begriffe und Ideen sind uns in der Form gegeben, die man die intellek­tuelle Anschauung genannt hat."
      ],
      [
        "Kant und die neueren an ihn anknüpfenden Philosophen sprechen dieses Vermögen dem Menschen vollständig ab, weil alles Denken sich nur auf Gegenstände beziehe und aus sich selbst absolut nichts hervorbringe.",
        "In der intellektuellen Anschauung muß mit der Denkform zugleich der Inhalt mitgegeben sein."
      ],
      [
        "Ist dies aber nicht bei den reinen Begriffen und Ideen wirklich der Fall? (Unter Begriff verstehe ich eine Regel, nach welcher die zusammenhanglosen Elemente der Wahrnehmung zu einer Einheit verbunden werden.",
        "Kausalität z."
      ],
      [
        "B. ist ein Begriff.",
        "Idee ist nur ein Begriff mit größerem Inhalt.",
        "Or­ganismus, ganz abstrakt genommen, ist eine Idee.) Man muß sie nur in der Form betrachten, in der sie von allem"
      ],
      [
        "empirischen Inhalt noch ganz frei sind.",
        "Wenn man z.",
        "B. den reinen Begriff der Kausalität erfassen will, darf man sich nicht an irgend eine bestimmte Kausalität oder an die Summe aller Kausalitäten halten, sondern an den bloßen Begriff derselben.",
        "Ursachen und Wirkungen müssen wir in der Welt aufsuchen, Ursachlichkeit als Gedankenform müs­sen wir selbst hervorbringen, ehe wir die ersteren in der Welt finden können.",
        "Wenn man aber an der Kantschen Behauptung festhalten wollte, Begriffe ohne Anschauungen seien leer, so wäre es undenkbar, die Möglichkeit einer Be­stimmung der gegebenen Welt durch Begriffe darzutun.",
        "Denn man nehme an, es seien zwei Elemente des Welt­inhaltes gegeben: a und b.",
        "Soll ich zwischen denselben ein Verhältnis aufsuchen, so muß ich das an der Hand einer inhaltlich bestimmten Regel tun; diese kann ich aber nur im Erkenntnisakte selbst produzieren, denn aus dem Ob­jekte kann ich sie deshalb nicht nehmen, weil die Bestim­mungen dieses letzteren mit Hilfe der Regel eben erst ge­wonnen werden sollen.",
        "Eine solche Regel zur Bestimmung des Wirklichen geht also vollständig innerhalb der rein begrifflichen Entität auf."
      ],
      [
        "Bevor wir nun weiterschreiten, wollen wir erst einen möglichen Einwand beseitigen.",
        "Es scheint nämlich, als ob unbewußt in unserem Gedankengange die Vorstellung des «Ich», des «persönlichen Subjekts»eine Rolle spiele, und daß wir diese Vorstellung in dem Fortschritte unserer Ge­dankenentwicklung benützen, ohne die Berechtigung dazu dargetan zu haben.",
        "Es ist das der Fall, wenn wir z.B. sagen:"
      ],
      [
        "«wir bringen Begriffe hervor»oder «wir stellen diese oder jene Forderung».",
        "Aber nichts in unseren Ausführungen gibt Veranlassung, in solchen Sätzen mehr als stilistische Wendungen"
      ],
      [
        "zu sehen.",
        "Daß der Erkenntnisakt einem «Ich»an­gehört und von demselben ausgeht, das kann, wie wir schon gesagt haben, nur auf Grund erkennender Erwägungen festgestellt werden.",
        "Eigentlich müßten wir vorläufig nur von dem Erkenntnisakt sprechen, ohne einen Träger des­selben auch nur zu erwähnen.",
        "Denn alles, was bis jetzt feststeht, beschränkt sich darauf, daß ein «Gegebenes vorliegt, und daß aus einem Punkte dieses «Gegebenen das oben angeführte Postulat entspringt; endlich, daß Be­griffe und Ideen das Gebiet sind, das diesem Postulate ent­spricht.",
        "Daß der Punkt, aus dem das Postulat entspringt, das «Ich»ist, soll damit nicht geleugnet werden.",
        "Aber wir beschränken uns fürs erste darauf, jene beiden Schritte der Erkenntnistheorie in ihrer Reinheit hinzustellen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "V. ERKENNEN UND WIRKLICHKEIT",
    "paragraphs": [
      "V. ERKENNEN UND WIRKLICHKEIT",
      "Begriffe und Ideen sind es also, in denen wir das gegeben haben, was zugleich über das Gegebene hinausführt. Damit aber ist die Möglichkeit geboten, auch das Wesen der übri­gen Erkenntnistätigkeit zu bestimmen.",
      "Wir haben durch ein Postulat aus dem gegebenen Weltbilde einen Teil ausgesondert, weil es in der Natur des Er­kennens liegt, gerade von diesem so gearteten Teile auszuge­hen. Diese Aussonderung wurde also nur gemacht, um das Erkennen begreifen zu können. Damit müssen wir uns aber auch zugleich klar darüber sein, daß wir die Einheit des Weltbildes künstlich zerrissen haben. Wir müssen einsehen, daß das von uns aus dem Gegebenen abgetrennte Segment, abgesehen von unserer Forderung und außer derselben, in einer notwendigen Verbindung mit dem Weltinhalte stehe. Damit ist der nächste Schritt der Erkenntnistheorie gegeben. Er wird darinnen bestehen, die Einheit, welche behufs Er­möglichung der Erkenntnis zerrissen worden ist, wieder herzustellen. Diese Wiederherstellung geschieht in dem Denken über die gegebene Welt. In der denkenden Weltbetrachtung vollzieht sich tatsächlich die Vereinigung der zwei Teile des Weltinhalts: dessen, den wir als Gegebenes auf dem Horizonte unserer Erlebnisse überblicken, und dessen, der im Erkenntnisakt produziert werden muß, um auch gegeben zu sein. Der Erkenntnisakt ist die Synthese dieser beiden Elemente. Und zwar erscheint in jedem einzelnen Erkenntnisakte das eine derselben als ein im Akte selbst Produziertes, durch ihn zu dem bloß Gegebenen",
      "Hinzugebrachtes. Nur im Anfang der Erkenntnistheorie selbst erscheint das sonst stets Produzierte als ein Gege­benes.",
      "Die gegebene Welt mit Begriffen und Ideen durchdringen, ist aber denkende Betrachtung der Dinge. Das Denken ist somit tatsächlich der Akt, wodurch die Erkenntnis ver­mittelt wird. Nur wenn das Denken von sich aus den In­halt des Weltbildes ordnet, kann Erkenntnis zustande kommen. Das Denken selbst ist ein Tun, das einen eigenen Inhalt im Momente des Erkennens hervorbringt. Soweit also der erkannte Inhalt aus dem Denken allein fließt, bie­tet er für das Erkennen keine Schwierigkeit. Hier brauchen wir bloß zu beobachten; und wir haben das Wesen unmittel­bar gegeben. Die Beschreibung des Denkens ist zugleich die Wissenschaft des Denkens. In der Tat war auch die Logik nie etwas anderes als eine Beschreibung der Denkformen, nie eine beweisende Wissenschaft. Der Beweis tritt erst ein, wenn eine Synthesis des Gedachten mit anderweitigem Weltinhalte stattfindet. Mit Recht sagt daher Gideon Spik­ker in seinem Buche: «Lessings Weltanschauung» (S.5):",
      "«Daß das Denken an sich richtig sei, können wir nie er­fahren, weder empirisch, noch logisch.»Wir können hinzufügen: Beim Denken hört alles Beweisen auf. Denn der Be­weis setzt bereits das Denken voraus. Man kann wohl ein einzelnes Faktum, nicht aber das Beweisen selbst beweisen. Wir können nur beschreiben, was ein Beweis ist. In der Logik ist alle Theorie nur Empirie; in dieser Wissenschaft gibt es nur Beobachtung. Wenn wir aber außer unserem Denken etwas erkennen wollen, so können wir das nur mit Hilfe des Denkens, d.h. das Denken muß an ein Gegebenes herantreten und es aus der chaotischen Verbindung in eine",
      "systematische mit dem Weltbilde bringen. Das Denken tritt also als formendes Prinzip an den gegebenen Weltinhalt heran. Der Vorgang dabei ist folgender: Es werden zunächst gedanklich gewisse Einzelheiten aus der Gesamtheit des Weltganzen herausgehoben. Denn im Gegebenen ist eigent­lich kein Einzelnes, sondern alles in kontinuierlicher Ver­bindung. Diese gesonderten Einzelheiten bezieht nun das Denken nach Maßgabe der von ihm produzierten Formen aufeinander und bestimmt zuletzt, was sich aus dieser Be­ziehung ergibt. Dadurch, daß das Denken einen Bezug zwi­schen zwei abgesonderten Partien des Weltinhaltes her­stellt, hat es gar nichts von sich aus über dieselben bestimmt. Es wartet ja ab, was sich infolge der Herstellung des Bezuges von selbst ergibt. Dieses Ergebnis erst ist eine Erkenntnis über die betreffenden Teile des Weltinhaltes. Läge es in der Natur des letzteren, durch jenen Bezug überhaupt nichts über sich zu äußern: nun, dann müßte eben der Denkver­such mißlingen und ein neuer an seine Stelle treten. Alle Erkenntnisse beruhen darauf, daß der Mensch zwei oder mehrere Elemente der Wirklichkeit in die richtige Verbin­dung bringt und das sich hieraus Ergebende erfaßt.",
      "Es ist zweifellos, daß wir nicht nur in den Wissenschaften, wo es uns die Geschichte derselben sattsam lehrt, sondern auch im gewöhnlichen Leben viele solche vergebliche Denkversuche machen; nur tritt in den einfachen Fällen, die uns doch zumeist begegnen, der richtige so rasch an die Stelle der falschen, daß uns diese letzteren gar nicht oder nur sel­ten zum Bewußtsein kommen.",
      "Kant schwebte diese von uns abgeleitete Tätigkeit des Denkens zum Behufe der systematischen Gliederung des Weltinhaltes bei seiner «synthetischen Einheit der Apperzeption»",
      "vor. Aber wie wenig sich derselbe die eigentliche Aufgabe des Denkens dabei zum Bewußtsein gebracht hat, geht daraus hervor, daß er glaubt, aus den Regeln, nach denen sich diese Synthesis vollzieht, lassen sich die Gesetze a priori der reinen Naturwissenschaft ableiten. Er hat dabei nicht bedacht, daß die synthetische Tätigkeit des Denkens nur eine solche ist, welche die Gewinnung der eigentlichen Naturgesetze vorbereitet. Denken wir uns, wir lösen irgend einen Inhalt a aus dem Weltbilde los, und ebenso einen an­dern b. Wenn es zur Erkenntnis eines gesetzmäßigen Zu­sammenhanges zwischen a und b kommen soll, so hat das Denken zunächst a in ein solches Verhältnis zu b zu brin­gen, durch das es möglich wird, daß sich uns die bestehende Abhängigkeit als gegebene darstellt. Der eigentliche Inhalt eines Naturgesetzes resultiert also aus dem Gegebenen, und dem Denken kommt es bloß zu, die Gelegenheit herbei­zuführen, durch die die Teile des Weltbildes in solche Ver­hältnisse gebracht werden, daß ihre Gesetzmäßigkeit er­sichtlich wird. Aus der bloßen synthetischen Tätigkeit des Denkens folgen also keinerlei objektive Gesetze.",
      "Wir müssen uns nun fragen, welchen Anteil hat das Den­ken bei der Herstellung unseres wissenschaftlichen Weltbildes im Gegensatz zum bloß gegebenen Weltbilde? Aus unserer Darstellung folgt, daß es die Form der Gesetz­mäßigkeit besorgt. Nehmen wir in unserem obigen Schema an, daß a die Ursache, b die Wirkung sei. Es könnte der kausale Zusammenhang von a und b nie Erkenntnis wer­den, wenn das Denken nicht in der Lage wäre, den Begriff der Kausalität zu bilden. Aber um im gegebenen Falle a als Ursache, b als Wirkung zu erkennen, dazu ist notwen­dig, daß jene beiden dem entsprechen, was unter Ursache",
      "und Wirkung verstanden wird. Ebenso steht es mit anderen Kategorien des Denkens.",
      "Es wird zweckmäßig sein, hier auf die Ausführungen Humes über den Begriff der Kausalität mit einigen Worten hinzuweisen. Hume sagt, die Begriffe von Ursache und Wirkung haben ihren Ursprung lediglich in unserer Ge­wohnheit. Wir beobachten öfters, daß auf ein gewisses Er­eignis ein anderes folgt, und gewöhnen uns daran, die bei­den in Kausalverbindung zu denken, so daß wir erwarten, daß das zweite eintritt, wenn wir das erste bemerken. Diese Auffassung geht aber von einer ganz irrigen Vorstellung von dem Kausalitätsverhältnis aus. Begegne ich durch eine Reihe von Tagen immer demselben Menschen, wenn ich aus dem Tore meines Wohnhauses trete, so werde ich mich zwar nach und nach gewöhnen, die zeitliche Folge der beiden Ereignisse zu erwarten, aber es wird mir gar nicht ein­fallen, hier einen Kausalzusammenhang zwischen meinem und des andern Menschen Erscheinen an demselben Orte zu konstatieren. Ich werde noch wesentlich andere Teile des Weltinhaltes aufsuchen, um die unmittelbare Folge der angeführten Tatsachen zu erklären. Wir bestimmen den Kausalzusammenhang eben durchaus nicht nach der zeit­lichen Folge, sondern nach der inhaltlichen Bedeutung der als Ursache und Wirkung bezeichneten Teile des Welt­inhaltes.",
      "Daraus, daß das Denken nur eine formale Tätigkeit beim Zustandebringen unseres wissenschaftlichen Weltbildes aus­übt, folgt: der Inhalt eines jeden Erkenntnisses kann kein a priori vor der Beobachtung (Auseinandersetzung des Den­kens mit dem Gegebenen) feststehender sein, sondern muß restlos aus der letzteren hervorgehen. In diesem Sinne sind",
      "alle unsere Erkenntnisse empirisch. Es ist aber auch gar nicht zu begreifen, wie das anders sein sollte. Denn die Kantschen Urteile a priori sind im Grunde gar keine Er­kenntnisse, sondern nur Postulate. Man kann im Kantschen Sinne immer nur sagen: wenn ein Ding Objekt einer mög­lichen Erfahrung werden soll, dann muß es sich diesen Ge­setzen fügen. Das sind also Vorschriften, die das Subjekt den Objekten macht. Man sollte aber doch glauben, wenn uns Erkenntnisse von dem Gegebenen zuteil werden sollen, so müssen dieselben nicht aus der Subjektivität, sondern aus der Objektivität fließen.",
      "Das Denken sagt nichts a priori über das Gegebene aus, aber es stellt jene Formen her, durch deren Zugrundelegung a posterion die Gesetzmäßigkeit der Erscheinungen zum Vorschein kommt.",
      "Es ist klar, daß diese Ansicht über die Grade der Ge­wißheit, die ein gewonnenes Erkenntnisurteil hat, a priori nichts ausmachen kann. Denn auch die Gewißheit kann aus nichts anderem denn aus dem Gegebenen selbst gewon­nen werden. Es läßt sich dagegen einwenden, daß die Be­obachtung nie etwas anderes sage, als daß einmal irgend­ein Zusammenhang der Erscheinungen stattfindet, nicht aber, daß er stattfinden muß und in gleichem Falle immer stattfinden wird. Aber auch diese Annahme ist eine irr­tümliche. Denn wenn ich einen gewissen Zusammenhang zwischen Teilen des Weltbildes erkenne, so ist er in unserem Sinne nichts anderes, als was aus diesen Teilen selbst sich ergibt, es ist nichts, was ich zu diesen Teilen hinzudenke, sondern etwas, was wesentlich zu denselben gehört, was also notwendig dann immer da sein muß, wenn sie selbst da sind.",
      "Nur eine Ansicht, die davon ausgeht, daß alles wissen­schaftliche Treiben nur darinnen bestehe, die Tatsachen der Erfahrung nach außer denselben liegenden, subjektiven Maximen zu verknüpfen, kann glauben, daß a und b heute nach diesem, morgen nach jenem Gesetze verknüpft sein können (J. St. Mill). Wer aber einsieht, daß die Natur­gesetze aus dem Gegebenen stammen, somit dasjenige sind, was den Zusammenhang der Erscheinungen ausmacht und bestimmt, dem wird es gar nicht einfallen, von einer bloß komparativen Allgemeinheit der aus der Beobachtung ge­wonnenen Gesetze zu sprechen. Damit wollen wir natürlich nicht behaupten, daß die von uns einmal als richtig an­genommenen Naturgesetze auch unbedingt gültig sein müs­sen. Aber wenn ein späterer Fall ein aufgestelltes Gesetz umstößt, dann rührt dies nicht davon her, daß dasselbe das erstemal nur mit komparativer Allgemeinheit hat gefolgert werden können, sondern davon, daß es auch dazumal nicht vollkommen richtig gefolgert war. Ein echtes Naturgesetz ist nichts anderes als der Ausdruck eines Zusammenhanges im gegebenen Weltbilde, und es ist ebensowenig ohne die Tatsachen da, die es regelt, wie diese ohne jenes da sind.",
      "Wir haben es oben als die Natur des Erkenntnisaktes be­stimmt, daß das gegebene Weltbild denkend mit Begriffen und Ideen durchsetzt wird. Was folgt aus dieser Tatsache? Wäre in dem Unmittelbar-Gegebenen eine abgeschlossene Ganzheit enthalten, dann wäre eine solche Bearbeitung desselben im Erkennen unmöglich und auch unnötig. Wir würden dann einfach das Gegebene hinnehmen, wie es ist, und wären in dieser Gestalt davon befriedigt. Nur wenn in dem Gegebenen etwas verborgen liegt, was noch nicht erscheint, wenn wir es in seiner Unmittelbarkeit betrachten,",
      "sondern erst mit Hilfe der vom Denken hineingebrachten Ordnung, dann ist der Erkenntnisakt möglich. Was in dem Gegebenen vor der gedanklichen Verarbeitung liegt, ist nicht dessen volle Ganzheit.",
      "Dies wird sogleich noch deutlicher, wenn wir auf die im Erkenntnisakt in Betracht kommenden Faktoren näher ein­gehen. Der erste derselben ist das Gegebene. Das Gegebensein ist keine Eigenschaft des Gegebenen, sondern nur ein Ausdruck für dessen Verhältnis zu dem zweiten Faktor des Erkenntnisaktes. Was das Gegebene seiner eigenen Natur nach ist, bleibt also durch diese Bestimmung völlig im Dun­keln. Den zweiten Faktor, den begrifflichen Inhalt des Ge­gebenen, findet das Denken im Erkenntnisakte als notwen­dig mit dem Gegebenen verbunden. Wir fragen uns nun:",
      "1. Wo besteht die Trennung von Gegebenem und Begriff?",
      "2. Wo liegt die Vereinigung derselben? Die Beantwortung dieser beiden Fragen ist ohne Zweifel in unseren voran­gehenden Untersuchungen gegeben. Die Trennung besteht lediglich im Erkenntnisakte, die Verbindung liegt im Ge­gebenen. Daraus geht mit Notwendigkeit hervor, daß der begriffliche Inhalt nur ein Teil des Gegebenen ist, und daß der Erkenntnisakt darin besteht, die für ihn zunächst ge­trennt gegebenen Bestandteile des Weltbildes miteinander zu vereinigen. Das gegebene Weltbild wird somit erst voll­ständig durch jene mittelbare Art Gegebenseins, die durch das Denken herbeigeführt wird. Durch die Form der Un­mittelbarkeit zeigt sich das Weltbild zuerst in einer ganz unvollständigen Gestalt.",
      "Wäre in dem Weltinhalte von vornherein der Gedanken­inhalt mit dem Gegebenen vereinigt; dann gäbe es kein Erkennen. Denn es könnte nirgends das Bedürfnis entstehen,­",
      "über das Gegebene hinauszugehen. Würden wir aber mit dem Denken und in demselben allen Inhalt der Welt erzeugen, dann gäbe es ebensowenig ein Erkennen. Denn was wir selbst produzieren, brauchen wir nicht zu er kennen. Das Erkennen beruht also darauf, daß uns der Weltinhalt ursprünglich in einer Form gegeben ist, die unvollständig ist, die ihn nicht ganz enthält, sondern die außer dem, was sie unmittelbar darbietet, noch eine zweite wesentliche Seite hat. Diese zweite, ursprünglich nicht ge­gebene Seite des Weltinhaltes wird durch die Erkenntnis enthüllt. Was uns im Denken abgesondert erscheint, sind also nicht leere Formen, sondern eine Summe von Bestim­mungen (Kategorien), die aber für den übrigen Weltinhalt Form sind. Erst die durch die Erkenntnis gewonnene Ge­stalt des Weitinhaltes, in der beide au/gezeigte Seiten des­selben vereinigt sind, kann Wirklichkeit genannt werden."
    ],
    "sentences": [
      [
        "ERKENNEN UND WIRKLICHKEIT"
      ],
      [
        "Begriffe und Ideen sind es also, in denen wir das gegeben haben, was zugleich über das Gegebene hinausführt.",
        "Damit aber ist die Möglichkeit geboten, auch das Wesen der übri­gen Erkenntnistätigkeit zu bestimmen."
      ],
      [
        "Wir haben durch ein Postulat aus dem gegebenen Weltbilde einen Teil ausgesondert, weil es in der Natur des Er­kennens liegt, gerade von diesem so gearteten Teile auszuge­hen.",
        "Diese Aussonderung wurde also nur gemacht, um das Erkennen begreifen zu können.",
        "Damit müssen wir uns aber auch zugleich klar darüber sein, daß wir die Einheit des Weltbildes künstlich zerrissen haben.",
        "Wir müssen einsehen, daß das von uns aus dem Gegebenen abgetrennte Segment, abgesehen von unserer Forderung und außer derselben, in einer notwendigen Verbindung mit dem Weltinhalte stehe.",
        "Damit ist der nächste Schritt der Erkenntnistheorie gegeben.",
        "Er wird darinnen bestehen, die Einheit, welche behufs Er­möglichung der Erkenntnis zerrissen worden ist, wieder herzustellen.",
        "Diese Wiederherstellung geschieht in dem Denken über die gegebene Welt.",
        "In der denkenden Weltbetrachtung vollzieht sich tatsächlich die Vereinigung der zwei Teile des Weltinhalts: dessen, den wir als Gegebenes auf dem Horizonte unserer Erlebnisse überblicken, und dessen, der im Erkenntnisakt produziert werden muß, um auch gegeben zu sein.",
        "Der Erkenntnisakt ist die Synthese dieser beiden Elemente.",
        "Und zwar erscheint in jedem einzelnen Erkenntnisakte das eine derselben als ein im Akte selbst Produziertes, durch ihn zu dem bloß Gegebenen"
      ],
      [
        "Hinzugebrachtes.",
        "Nur im Anfang der Erkenntnistheorie selbst erscheint das sonst stets Produzierte als ein Gege­benes."
      ],
      [
        "Die gegebene Welt mit Begriffen und Ideen durchdringen, ist aber denkende Betrachtung der Dinge.",
        "Das Denken ist somit tatsächlich der Akt, wodurch die Erkenntnis ver­mittelt wird.",
        "Nur wenn das Denken von sich aus den In­halt des Weltbildes ordnet, kann Erkenntnis zustande kommen.",
        "Das Denken selbst ist ein Tun, das einen eigenen Inhalt im Momente des Erkennens hervorbringt.",
        "Soweit also der erkannte Inhalt aus dem Denken allein fließt, bie­tet er für das Erkennen keine Schwierigkeit.",
        "Hier brauchen wir bloß zu beobachten; und wir haben das Wesen unmittel­bar gegeben.",
        "Die Beschreibung des Denkens ist zugleich die Wissenschaft des Denkens.",
        "In der Tat war auch die Logik nie etwas anderes als eine Beschreibung der Denkformen, nie eine beweisende Wissenschaft.",
        "Der Beweis tritt erst ein, wenn eine Synthesis des Gedachten mit anderweitigem Weltinhalte stattfindet.",
        "Mit Recht sagt daher Gideon Spik­ker in seinem Buche: «Lessings Weltanschauung» (S.5):"
      ],
      [
        "«Daß das Denken an sich richtig sei, können wir nie er­fahren, weder empirisch, noch logisch.»Wir können hinzufügen: Beim Denken hört alles Beweisen auf.",
        "Denn der Be­weis setzt bereits das Denken voraus.",
        "Man kann wohl ein einzelnes Faktum, nicht aber das Beweisen selbst beweisen.",
        "Wir können nur beschreiben, was ein Beweis ist.",
        "In der Logik ist alle Theorie nur Empirie; in dieser Wissenschaft gibt es nur Beobachtung.",
        "Wenn wir aber außer unserem Denken etwas erkennen wollen, so können wir das nur mit Hilfe des Denkens, d.h. das Denken muß an ein Gegebenes herantreten und es aus der chaotischen Verbindung in eine"
      ],
      [
        "systematische mit dem Weltbilde bringen.",
        "Das Denken tritt also als formendes Prinzip an den gegebenen Weltinhalt heran.",
        "Der Vorgang dabei ist folgender: Es werden zunächst gedanklich gewisse Einzelheiten aus der Gesamtheit des Weltganzen herausgehoben.",
        "Denn im Gegebenen ist eigent­lich kein Einzelnes, sondern alles in kontinuierlicher Ver­bindung.",
        "Diese gesonderten Einzelheiten bezieht nun das Denken nach Maßgabe der von ihm produzierten Formen aufeinander und bestimmt zuletzt, was sich aus dieser Be­ziehung ergibt.",
        "Dadurch, daß das Denken einen Bezug zwi­schen zwei abgesonderten Partien des Weltinhaltes her­stellt, hat es gar nichts von sich aus über dieselben bestimmt.",
        "Es wartet ja ab, was sich infolge der Herstellung des Bezuges von selbst ergibt.",
        "Dieses Ergebnis erst ist eine Erkenntnis über die betreffenden Teile des Weltinhaltes.",
        "Läge es in der Natur des letzteren, durch jenen Bezug überhaupt nichts über sich zu äußern: nun, dann müßte eben der Denkver­such mißlingen und ein neuer an seine Stelle treten.",
        "Alle Erkenntnisse beruhen darauf, daß der Mensch zwei oder mehrere Elemente der Wirklichkeit in die richtige Verbin­dung bringt und das sich hieraus Ergebende erfaßt."
      ],
      [
        "Es ist zweifellos, daß wir nicht nur in den Wissenschaften, wo es uns die Geschichte derselben sattsam lehrt, sondern auch im gewöhnlichen Leben viele solche vergebliche Denkversuche machen; nur tritt in den einfachen Fällen, die uns doch zumeist begegnen, der richtige so rasch an die Stelle der falschen, daß uns diese letzteren gar nicht oder nur sel­ten zum Bewußtsein kommen."
      ],
      [
        "Kant schwebte diese von uns abgeleitete Tätigkeit des Denkens zum Behufe der systematischen Gliederung des Weltinhaltes bei seiner «synthetischen Einheit der Apperzeption»"
      ],
      [
        "vor.",
        "Aber wie wenig sich derselbe die eigentliche Aufgabe des Denkens dabei zum Bewußtsein gebracht hat, geht daraus hervor, daß er glaubt, aus den Regeln, nach denen sich diese Synthesis vollzieht, lassen sich die Gesetze a priori der reinen Naturwissenschaft ableiten.",
        "Er hat dabei nicht bedacht, daß die synthetische Tätigkeit des Denkens nur eine solche ist, welche die Gewinnung der eigentlichen Naturgesetze vorbereitet.",
        "Denken wir uns, wir lösen irgend einen Inhalt a aus dem Weltbilde los, und ebenso einen an­dern b.",
        "Wenn es zur Erkenntnis eines gesetzmäßigen Zu­sammenhanges zwischen a und b kommen soll, so hat das Denken zunächst a in ein solches Verhältnis zu b zu brin­gen, durch das es möglich wird, daß sich uns die bestehende Abhängigkeit als gegebene darstellt.",
        "Der eigentliche Inhalt eines Naturgesetzes resultiert also aus dem Gegebenen, und dem Denken kommt es bloß zu, die Gelegenheit herbei­zuführen, durch die die Teile des Weltbildes in solche Ver­hältnisse gebracht werden, daß ihre Gesetzmäßigkeit er­sichtlich wird.",
        "Aus der bloßen synthetischen Tätigkeit des Denkens folgen also keinerlei objektive Gesetze."
      ],
      [
        "Wir müssen uns nun fragen, welchen Anteil hat das Den­ken bei der Herstellung unseres wissenschaftlichen Weltbildes im Gegensatz zum bloß gegebenen Weltbilde?",
        "Aus unserer Darstellung folgt, daß es die Form der Gesetz­mäßigkeit besorgt.",
        "Nehmen wir in unserem obigen Schema an, daß a die Ursache, b die Wirkung sei.",
        "Es könnte der kausale Zusammenhang von a und b nie Erkenntnis wer­den, wenn das Denken nicht in der Lage wäre, den Begriff der Kausalität zu bilden.",
        "Aber um im gegebenen Falle a als Ursache, b als Wirkung zu erkennen, dazu ist notwen­dig, daß jene beiden dem entsprechen, was unter Ursache"
      ],
      [
        "und Wirkung verstanden wird.",
        "Ebenso steht es mit anderen Kategorien des Denkens."
      ],
      [
        "Es wird zweckmäßig sein, hier auf die Ausführungen Humes über den Begriff der Kausalität mit einigen Worten hinzuweisen.",
        "Hume sagt, die Begriffe von Ursache und Wirkung haben ihren Ursprung lediglich in unserer Ge­wohnheit.",
        "Wir beobachten öfters, daß auf ein gewisses Er­eignis ein anderes folgt, und gewöhnen uns daran, die bei­den in Kausalverbindung zu denken, so daß wir erwarten, daß das zweite eintritt, wenn wir das erste bemerken.",
        "Diese Auffassung geht aber von einer ganz irrigen Vorstellung von dem Kausalitätsverhältnis aus.",
        "Begegne ich durch eine Reihe von Tagen immer demselben Menschen, wenn ich aus dem Tore meines Wohnhauses trete, so werde ich mich zwar nach und nach gewöhnen, die zeitliche Folge der beiden Ereignisse zu erwarten, aber es wird mir gar nicht ein­fallen, hier einen Kausalzusammenhang zwischen meinem und des andern Menschen Erscheinen an demselben Orte zu konstatieren.",
        "Ich werde noch wesentlich andere Teile des Weltinhaltes aufsuchen, um die unmittelbare Folge der angeführten Tatsachen zu erklären.",
        "Wir bestimmen den Kausalzusammenhang eben durchaus nicht nach der zeit­lichen Folge, sondern nach der inhaltlichen Bedeutung der als Ursache und Wirkung bezeichneten Teile des Welt­inhaltes."
      ],
      [
        "Daraus, daß das Denken nur eine formale Tätigkeit beim Zustandebringen unseres wissenschaftlichen Weltbildes aus­übt, folgt: der Inhalt eines jeden Erkenntnisses kann kein a priori vor der Beobachtung (Auseinandersetzung des Den­kens mit dem Gegebenen) feststehender sein, sondern muß restlos aus der letzteren hervorgehen.",
        "In diesem Sinne sind"
      ],
      [
        "alle unsere Erkenntnisse empirisch.",
        "Es ist aber auch gar nicht zu begreifen, wie das anders sein sollte.",
        "Denn die Kantschen Urteile a priori sind im Grunde gar keine Er­kenntnisse, sondern nur Postulate.",
        "Man kann im Kantschen Sinne immer nur sagen: wenn ein Ding Objekt einer mög­lichen Erfahrung werden soll, dann muß es sich diesen Ge­setzen fügen.",
        "Das sind also Vorschriften, die das Subjekt den Objekten macht.",
        "Man sollte aber doch glauben, wenn uns Erkenntnisse von dem Gegebenen zuteil werden sollen, so müssen dieselben nicht aus der Subjektivität, sondern aus der Objektivität fließen."
      ],
      [
        "Das Denken sagt nichts a priori über das Gegebene aus, aber es stellt jene Formen her, durch deren Zugrundelegung a posterion die Gesetzmäßigkeit der Erscheinungen zum Vorschein kommt."
      ],
      [
        "Es ist klar, daß diese Ansicht über die Grade der Ge­wißheit, die ein gewonnenes Erkenntnisurteil hat, a priori nichts ausmachen kann.",
        "Denn auch die Gewißheit kann aus nichts anderem denn aus dem Gegebenen selbst gewon­nen werden.",
        "Es läßt sich dagegen einwenden, daß die Be­obachtung nie etwas anderes sage, als daß einmal irgend­ein Zusammenhang der Erscheinungen stattfindet, nicht aber, daß er stattfinden muß und in gleichem Falle immer stattfinden wird.",
        "Aber auch diese Annahme ist eine irr­tümliche.",
        "Denn wenn ich einen gewissen Zusammenhang zwischen Teilen des Weltbildes erkenne, so ist er in unserem Sinne nichts anderes, als was aus diesen Teilen selbst sich ergibt, es ist nichts, was ich zu diesen Teilen hinzudenke, sondern etwas, was wesentlich zu denselben gehört, was also notwendig dann immer da sein muß, wenn sie selbst da sind."
      ],
      [
        "Nur eine Ansicht, die davon ausgeht, daß alles wissen­schaftliche Treiben nur darinnen bestehe, die Tatsachen der Erfahrung nach außer denselben liegenden, subjektiven Maximen zu verknüpfen, kann glauben, daß a und b heute nach diesem, morgen nach jenem Gesetze verknüpft sein können (J.",
        "Mill).",
        "Wer aber einsieht, daß die Natur­gesetze aus dem Gegebenen stammen, somit dasjenige sind, was den Zusammenhang der Erscheinungen ausmacht und bestimmt, dem wird es gar nicht einfallen, von einer bloß komparativen Allgemeinheit der aus der Beobachtung ge­wonnenen Gesetze zu sprechen.",
        "Damit wollen wir natürlich nicht behaupten, daß die von uns einmal als richtig an­genommenen Naturgesetze auch unbedingt gültig sein müs­sen.",
        "Aber wenn ein späterer Fall ein aufgestelltes Gesetz umstößt, dann rührt dies nicht davon her, daß dasselbe das erstemal nur mit komparativer Allgemeinheit hat gefolgert werden können, sondern davon, daß es auch dazumal nicht vollkommen richtig gefolgert war.",
        "Ein echtes Naturgesetz ist nichts anderes als der Ausdruck eines Zusammenhanges im gegebenen Weltbilde, und es ist ebensowenig ohne die Tatsachen da, die es regelt, wie diese ohne jenes da sind."
      ],
      [
        "Wir haben es oben als die Natur des Erkenntnisaktes be­stimmt, daß das gegebene Weltbild denkend mit Begriffen und Ideen durchsetzt wird.",
        "Was folgt aus dieser Tatsache?",
        "Wäre in dem Unmittelbar-Gegebenen eine abgeschlossene Ganzheit enthalten, dann wäre eine solche Bearbeitung desselben im Erkennen unmöglich und auch unnötig.",
        "Wir würden dann einfach das Gegebene hinnehmen, wie es ist, und wären in dieser Gestalt davon befriedigt.",
        "Nur wenn in dem Gegebenen etwas verborgen liegt, was noch nicht erscheint, wenn wir es in seiner Unmittelbarkeit betrachten,"
      ],
      [
        "sondern erst mit Hilfe der vom Denken hineingebrachten Ordnung, dann ist der Erkenntnisakt möglich.",
        "Was in dem Gegebenen vor der gedanklichen Verarbeitung liegt, ist nicht dessen volle Ganzheit."
      ],
      [
        "Dies wird sogleich noch deutlicher, wenn wir auf die im Erkenntnisakt in Betracht kommenden Faktoren näher ein­gehen.",
        "Der erste derselben ist das Gegebene.",
        "Das Gegebensein ist keine Eigenschaft des Gegebenen, sondern nur ein Ausdruck für dessen Verhältnis zu dem zweiten Faktor des Erkenntnisaktes.",
        "Was das Gegebene seiner eigenen Natur nach ist, bleibt also durch diese Bestimmung völlig im Dun­keln.",
        "Den zweiten Faktor, den begrifflichen Inhalt des Ge­gebenen, findet das Denken im Erkenntnisakte als notwen­dig mit dem Gegebenen verbunden.",
        "Wir fragen uns nun:"
      ],
      [
        "Wo besteht die Trennung von Gegebenem und Begriff?"
      ],
      [
        "Wo liegt die Vereinigung derselben?",
        "Die Beantwortung dieser beiden Fragen ist ohne Zweifel in unseren voran­gehenden Untersuchungen gegeben.",
        "Die Trennung besteht lediglich im Erkenntnisakte, die Verbindung liegt im Ge­gebenen.",
        "Daraus geht mit Notwendigkeit hervor, daß der begriffliche Inhalt nur ein Teil des Gegebenen ist, und daß der Erkenntnisakt darin besteht, die für ihn zunächst ge­trennt gegebenen Bestandteile des Weltbildes miteinander zu vereinigen.",
        "Das gegebene Weltbild wird somit erst voll­ständig durch jene mittelbare Art Gegebenseins, die durch das Denken herbeigeführt wird.",
        "Durch die Form der Un­mittelbarkeit zeigt sich das Weltbild zuerst in einer ganz unvollständigen Gestalt."
      ],
      [
        "Wäre in dem Weltinhalte von vornherein der Gedanken­inhalt mit dem Gegebenen vereinigt; dann gäbe es kein Erkennen.",
        "Denn es könnte nirgends das Bedürfnis entstehen,­"
      ],
      [
        "über das Gegebene hinauszugehen.",
        "Würden wir aber mit dem Denken und in demselben allen Inhalt der Welt erzeugen, dann gäbe es ebensowenig ein Erkennen.",
        "Denn was wir selbst produzieren, brauchen wir nicht zu er kennen.",
        "Das Erkennen beruht also darauf, daß uns der Weltinhalt ursprünglich in einer Form gegeben ist, die unvollständig ist, die ihn nicht ganz enthält, sondern die außer dem, was sie unmittelbar darbietet, noch eine zweite wesentliche Seite hat.",
        "Diese zweite, ursprünglich nicht ge­gebene Seite des Weltinhaltes wird durch die Erkenntnis enthüllt.",
        "Was uns im Denken abgesondert erscheint, sind also nicht leere Formen, sondern eine Summe von Bestim­mungen (Kategorien), die aber für den übrigen Weltinhalt Form sind.",
        "Erst die durch die Erkenntnis gewonnene Ge­stalt des Weitinhaltes, in der beide au/gezeigte Seiten des­selben vereinigt sind, kann Wirklichkeit genannt werden."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "VI. DIE VORAUSSETZUNGSLOSE ERKENNTNISTHEORIE UND FICHTES WISSENSCHAFTSLEHRE",
    "paragraphs": [
      "VI. DIE VORAUSSETZUNGSLOSE ERKENNTNISTHEORIE UND FICHTES WISSENSCHAFTSLEHRE",
      "Mit den bisherigen Ausführungen haben wir die Idee der Erkenntnis festgestellt. Unmittelbar gegeben ist diese Idee nun im menschlichen Bewußtsein, insofern es sich erkennend verhält. Dem «Ich»als Mittelpunkt des Bewußtseins ist die äußere und innere Wahrnehmung und sein eigenes Dasein unmittelbar gegeben. (Es braucht wohl kaum gesagt zu werden, daß wir mit der Bezeichnung «Mittelpunkt hier nicht eine theoretische Ansicht über die Natur des Be­wußtseins verknüpft wissen wollen, sondern daß wir sie nur als stilistische Abkürzung für die Gesamtphysiognomie des Bewußtseins gebrauchen.) Das Ich fühlt den Drang, in diesem Gegebenen mehr zu finden, als was unmittelbar ge­geben ist. Es geht ihm gegenüber der gegebenen Welt die zweite, die des Denkens auf, und es verbindet die beiden da­durch, daß es aus freiem Entschluß das verwirklicht, was wir als Idee des Erkennens festgestellt haben. Hierin liegt nun ein Grundunterschied zwischen der Art, wie sich im Objekt des menschlichen Bewußtseins selbst Begriff und Unmittelbar-Gegebenes zur totalen Wirklichkeit verbun­den zeigen, und jener, die dem übrigen Weltinhalte gegen­über Geltung hat. Bei jedem andern Teil des Weltbildes müssen wir uns vorstellen, daß die Verbindung das Ur­sprüngliche, von vornherein Notwendige ist, und daß nur am Beginne des Erkennens für die Erkenntnis eine künst­liche Trennung eingetreten ist, die aber zuletzt durch das Erkennen, der ursprünglichen Wesenheit des Objektiven",
      "gemäß, wieder aufgehoben wird. Beim menschlichen Be­wußtsein ist das anders. Hier ist die Verbindung nur vor­handen, wenn sie in wirklicher Tätigkeit vom Bewußtsein vollzogen wird. Bei jedem andern Objekte hat die Tren­nung für das Objekt keine Bedeutung, sondern nur für die Erkenntnis.",
      "Die Verbindung ist hier das erste, die Tren­nung das Abgeleitete. Das Erkennen vollzieht nur die Trennung, weil es sich auf seine Art nicht in den Besitz der Verbindung setzen kann, wenn es nicht vorher getrennt hat.",
      "Begriff und gegebene Wirklichkeit des Bewußtseins aber sind ursprünglich getrennt, die Verbindung ist das Ab­geleitete, und deswegen ist das Erkennen so beschaffen, wie wir es geschildert haben. Weil im Bewußtsein notwendig Idee und Gegebenes getrennt auftreten, deswegen spaltet sich für dasselbe die gesamte Wirklichkeit in diese zwei Teile, und weil das Bewußtsein nur durch eigene Tätigkeit die Verbindung der beiden genannten Elemente bewirken kann, deshalb gelangt es nur durch Verwirklichung des Er­kenntnisaktes zur vollen Wirklichkeit.",
      "Die übrigen Kate­gorien (Ideen) wären auch dann notwendig mit den ent­sprechenden Formen des Gegebenen verknüpft, wenn sie nicht in die Erkenntnis aufgenommen würden; die Idee des Erkennens kann mit dem ihr entsprechenden Gegebe­nen nur durch die Tätigkeit des Bewußtseins vereinigt wer­den. Ein wirkliches Bewußtsein existiert nur, wenn es sich selbst verwirklicht.",
      "Damit glauben wir genügend vorberei­tet zu sein, um den Grundfehler von Fichtes «Wissenschafts­lehre»bloßzulegen und zugleich den Schlüssel zu ihrem Verständnis zu liefern. Fichte ist derjenige Philosoph, wel­cher unter Kants Nachfolgern am lebhaftesten gefühlt hat, daß eine Grundlegung aller Wissenschaften nur in einer",
      "Theorie des Bewußtseins bestehen könne; aber er kam nie zur Erkenntnis, warum das so ist. Er empfand, daß das­jenige, was wir als zweiten Schritt der Erkenntnistheorie bezeichnen, und dem wir die Form eines Postulates geben, von dem «Ich»wirklich ausgeführt werden müsse. Wir ersehen dies z. B. aus seinen folgenden Worten: «Die Wissenschaftslehre entsteht also, insofern sie eine systema­tische Wissenschaft sein soll, geradeso wie alle möglichen Wissenschaften, insofern sie systematisch sein sollen, durch eine Bestimmung der Freiheit, welche letztere hier ins­besondere bestimmt ist, die Handlungsart der Intelligenz überhaupt zum Bewußtsein zu erheben; ... Durch diese freie Handlung wird nun etwas, das schon an sich Form ist, die notwendige Handlung der Intelligenz, als Gehalt in eine neue Form des Wissens oder Bewußtseins aufgenom­men . . .~»Was ist hier unter Handlungsart der «Intelli­genz»zu verstehen, wenn man das, was dunkel gefühlt ist, in klaren Begriffen ausspricht? Nichts anderes als die im Bewußtsein sich vollziehende Verwirklichung der Idee des Erkennens. Wäre Fichte sich dessen vollkommen klar be­wußt gewesen, dann hätte er den obigen Satz einfach so formulieren müssen: Die Wissenschaftslehre hat das Er­kennen, insofern es noch unbewußte Tätigkeit des «Ich ist, zum Bewußtsein zu erheben; sie hat zu zeigen, daß im «Ich»als notwendige Handlung die Objektivierung der Idee des Erkennens ausgeführt wird.",
      "Fichte will die Tätigkeit des «Ich»bestimmen. Er findet: «Dasjenige, dessen Seyn (Wesen) bloß darin besteht, daß",
      "-069-* Über den Begriff der Wissenschaftslehre oder der sogenannten Philosophie. Sämtliche Werke, Berlin 1845, Bd. I, S.71 f.",
      "es sich selbst als seyend setzt, ist das Ich, als absolutes Sub­jekt»*. Dieses Setzen des Ich ist für Fichte die erste un­bedingte Tathandlung, die allem übrigen «Bewußtseyn zum Grunde liegt»*. Das Ich kann also im Sinne Fichtes auch nur durch einen absoluten Entschluß alle seine Tätigkeit beginnen.",
      "Aber für Fichte ist es unmöglich, dieser seiner vom Ich absolut gesetzten Tätigkeit zu irgendeinem In­halte ihres Tuns zu verhelfen. Denn er hat nichts, worauf sich diese Tätigkeit richten, wonach sie sich bestimmen soll.",
      "Sein Ich soll eine Tathandlung vollziehen; aber was soll es tun? Weil Fichte den Begriff der Erkenntnis nicht aufstellte, den das Ich verwirklichen soll, deshalb rang er vergeblich, irgendeinen Fortgang von seiner absoluten Tathandlung zu den weiteren Bestimmungen des Ich zu finden.",
      "Ja, er er­klärt zuletzt in bezug auf einen solchen Fortgang, daß die Untersuchung hierüber außerhalb der Grenzen der Theorie liege. Er geht in seiner Deduktion der Vorstellung weder von einer absoluten Tätigkeit des Ich noch des Nicht-Ich, sondern von einem Bestimmten aus, das zugleich Bestim­men ist, weil im Bewußtsein unmittelbar nichts anderes enthalten ist noch enthalten sein kann.",
      "Was diese Bestim­mung wieder bestimmt, bleibt in der Theorie vollständig unentschieden; und durch diese Unbestimmtheit werden wir denn auch über die Theorie hinaus in den praktischen Teil der Wissenschaftslehre getrieben*** Durch diese Er­klärung vernichtet aber Fichte überhaupt alles Erkennen. Denn die praktische Tätigkeit des Ich gehört in ein ganz anderes Gebiet.",
      "Daß das von uns oben aufgestellte Postulat",
      "-070-* Grundlage der gesamten Wissenschaftslehre. Sämtl. Werke 1, S.97.",
      "-070-**    Sämtliche Werke I, S.91.",
      "-070-***    Sämtliche Werke I, S. 178.",
      "nur durch eine freie Handlung des Ich realisiert werden kann, ist ja klar; aber wenn das Ich sich erkennend verhal­ten soll, so kommt es gerade darauf an, daß die Entschlie­ßung desselben dahin geht, die Idee des Erkennens zu ver­wirklichen. Es ist ja gewiß richtig, daß das Ich aus freiem Entschluß noch vieles andere vollführen kann.",
      "Aber nicht auf eine Charakteristik des «freien>, sondern auf eine solche des «erkennenden»Ich kommt es bei der erkenntnis-theoretischen Grundlegung aller Wissenschaften an. Fichte hat sich aber von seinem subjektiven Hange, die Freiheit der menschlichen Persönlichkeit in das hellste Licht zu stellen, allzusehr beeinflussen lassen.",
      "Mit Recht bemerkt Harms in seiner Rede «über die Philosophie Fichtes (S.15): «Seine Weltansicht ist eine vorherrschend und aus­schließlich ethische, und seine Erkenntnistheorie trägt kei­nen anderen Charakter.»Das Erkennen hätte absolut keine Aufgabe, wenn alle Gebiete der Wirklichkeit in ihrer Totalität gegeben wären. Da nun aber das Ich, solange es nicht vom Denken in das systematische Ganze des Weltbildes eingefügt ist, auch nichts anderes ist als ein unmittel­bar Gegebenes, so genügt ein bloßes Aufzeigen seines Tuns durchaus nicht.",
      "Fichte jedoch ist der Ansicht, daß beim Ich mit dem bloßen Aufsuchen schon alles getan sei. «Wir haben den absolut-ersten, schlechthin unbedingten Grund­satz alles menschlichen Wissens aufzusuchen. Beweisen oder bestimmen läßt er sich nicht, wenn er absolut-erster Grund­satz sein soll*.» Wir haben gesehen, daß das Beweisen und Bestimmen einzig und allein dem Inhalte der reinen Logik gegenüber nicht am Platze ist.",
      "Das Ich gehört aber der",
      "-071-* Sämtliche Werke I, S.91.",
      "Wirklichkeit an, und da ist es notwendig, das Vorhanden­sein dieser oder jener Kategorie im Gegebenen festzustellen. Fichte tat das nicht. Und hierinnen ist der Grund zu suchen, warum er seiner Wissenschaftslehre eine so verfehlte Ge­stalt gab. Zeller bemerkt*, daß die logischen Formeln, durch die Fichte zu dem Ich-Begriff kommen will, nur schlecht den Umstand verhüllen, daß dieser eigentlich um jeden Preis den schon vorgefaßten Zweck erreichen wolle, zu diesem Anfangspunkte zu kommen. Diese Worte be­ziehen sich auf die erste Gestalt, die Fichte 1794 seiner Wissenschaftslehre gab. Wenn wir daran festhalten, daß Fichte in der Tat, der ganzen Anlage seines Philosophierens nach, nichts wollen konnte, als die Wissenschaft durch einen absoluten Machtspruch beginnen zu lassen, so gibt es ja nur zwei Wege, die dieses Beginnen verständlich erscheinen lassen. Der eine war der, das Bewußtsein bei irgendeiner seiner empirischen Tätigkeiten anzufassen und durch all­mähliche Losschälung alles dessen, was nicht ursprünglich aus demselben folgt, den reinen Begriff des Ich heraus­zukristallisieren. Der andere Weg aber war, gleich bei der ursprünglichen Tätigkeit des «Ich»einzusetzen und dessen Natur durch Selbstbesinnung und Selbstbeobachtung auf­zuzeigen. Den ersten Weg schlug Fichte am Beginne seines Philosophierens ein; im Verlaufe desselben ging er jedoch allmählich zum zweiten über.",
      "An die Synthesis der «transzendentalen Apperzeption »bei Kant anknüpfend, fand Fichte, daß alle Tätigkeit des Ich in der Zusammenfügung des Stoffes der Erfahrung nach",
      "-072-* Geschichte der deutschen Philosophie seit Leibniz, München 1871 bis 1875, S.605.",
      "den Formen des Urteils bestehe. Das Urteilen besteht in dem Verknüpfen des Prädikats mit dem Subjekte, was in rein formaler Weise durch den Satz ausgedrückt wird: a = a. Dieser Satz wäre unmöglich, wenn das x, das beide a verbindet, nicht auf einem Vermögen schlechthin zu set­zen beruhte.",
      "Denn der Satz bedeutet ja nicht: a ist, son­dern: wenn a ist, so ist a. Also von einem absoluten Setzen des a kann nicht die Rede sein. So bleibt denn nichts, um überhaupt zu einem absoluten, schlechthin Gültigen zu kommen, als das Setzen selbst für absolut zu erklären.",
      "Während das a bedingt ist, ist das Setzen des a unbedingt. Dieses Setzen ist aber eine Tathandlung des Ich. Dem Ich kommt somit eine Fähigkeit zu, schlechthin und unbedingt zu setzen. In dem Satze a = a wird das eine a nur gesetzt, indem das andere vorausgesetzt wird; und zwar wird es durch das Ich gesetzt.",
      "«Wenn a im Ich gesetzt ist, so ist es gesetzt*.»Dieser Zusammenhang ist nur unter der Be­dingung möglich, daß im Ich etwas sich immer Gleichblei­bendes sei, etwas, was von einem a zum andern hinüberfahrt. Und das oben erwähnte x beruht auf diesem Gleich­bleibenden.",
      "Das Ich, welches das eine a setzt, ist dasselbe wie jenes, welches das andere setzt. Das heißt aber Ich Ich. Dieser Satz in Form des Urteils ausgedrückt: Wenn Ich ist, so ist es - hat keinen Sinn. Das Ich wird ja nicht unter der Voraussetzung eines andern gesetzt, sondern es setzt sich selbst voraus.",
      "Das heißt aber: es ist schlechthin und un­bedingt. Die hypothetische Form des Urteils, die ohne die Voraussetzung des absoluten Ich allem Urteilen zukommt, verwandelt sich hier in die Form des absoluten Existenzialsatzes:­",
      "-073-* Sämtliche Werke I,S.94.",
      "Ich bin schlechtweg. Fichte drückt dies auch noch folgendermaßen aus*: «Das Ich setzt ursprünglich schlecht­hin sein eigenes Sein.»Wir sehen, daß diese ganze Ab­leitung Fichtes nichts ist als eine Art pädagogischer Aus­einandersetzung, um seine Leser dahin zu führen, wo ihnen die Erkenntnis der unbedingten Tätigkeit des Ich aufgeht. Es soll denselben jene Handlung des Ich klar vor Augen gebracht werden, ohne deren Vollzug überhaupt gar kein Ich ist.",
      "Wir wollen nun auf Fichtes Gedankengang noch einmal zurückblicken. Bei schärferem Zusehen stellt sich nämlich heraus, daß in demselben ein Sprung ist, und zwar ein sol­cher, der die Richtigkeit der Anschauung von der ursprüng­lichen Tathandlung in Frage stellt. Was ist denn eigentlich wirklich absolut in dem Setzen des Ich? Es wird geurteilt: Wenn a ist, so ist a. Das a wird vom Ich gesetzt. Über dieses Setzen kann also kein Zweifel obwalten. Aber wenn auch als Tätigkeit unbedingt, so kann das Ich doch nur irgend etwas setzen. Es kann nicht die «Tätigkeit an und für sich», sondern nur eine bestimmte Tätigkeit setzen. Kurz: das Setzen muß einen Inhalt haben. Diesen kann es aber nicht aus sich selbst nehmen, denn sonst könnte es nichts weiter als ewig nur das Setzen setzen. Es muß also für das Setzen, für die absolute Tätigkeit des Ich etwas geben, das durch sie realisiert wird. Ohne daß das Ich zu einem Gegebenen greift, das es setzt, kann es überhaupt «nichts, folglich nicht setzen. Das zeigt auch der Fichtesche Satz: Das Ich setzt sein Sein. Dieses Sein ist eine Kategorie. Wir sind wieder bei unserm Satze: Die Tätigkeit des Ich beruht darauf,",
      "-074-* Sämtliche Werke I , S.98.",
      "daß das Ich aus eigenem freiem Entschlusse die Begriffe und Ideen des Gegebenen setzt. Nur dadurch, daß Fichte unbewußt darauf ausgeht, das Ich als «Seiendes»nach­zuweisen, kommt er zu seinem Resultate. Hätte er den Be­griff des Erkennens entwickelt, so wäre er zu dem wahren Ausgangspunkte der Erkenntnistheorie gekommen: Das Ich setzt das Erkennen. Da Fichte sich nicht klarmachte, wo­durch die Tätigkeit des Ich bestimmt wird, bezeichnete er einfach das Setzen des Seins als Charakter dieser Tätigkeit. Damit hatte er aber auch die absolute Tätigkeit des Ich beschränkt. Denn ist nur das «Sein-Setzen»des Ich un­bedingt, dann ist ja alles andere, was vom Ich ausgeht, bedingt. Aber es ist auch jeder Weg abgeschnitten, um vom Unbedingten zum Bedingten zu kommen. Wenn das Ich nur nach der bezeichneten Richtung hin unbedingt ist, dann hört sofort die Möglichkeit für dasselbe auf, etwas anderes als sein eigenes Sein durch einen ursprünglichen Akt zu setzen. Es tritt somit die Notwendigkeit ein, den Grund für alle andere Tätigkeit des Ich anzugeben. Fichte suchte nach einem solchen vergebens, wie wir oben bereits gesehen haben.",
      "Daher wandte er sich zu dem andern der oben bezeich­neten Wege behufs Ableitung des Ich. Schon 1797 in der «Ersten Einleitung in die Wissenschaftslehre»empfiehlt er die Selbstbeobachtung als das Richtige, um das Ich in sei­nem ureigenen Charakter zu erkennen. «Merke auf dich selbst, kehre deinen Blick von allem, was dich umgibt, ab und in dein Inneres - ist die erste Forderung, welche die Philosophie an ihren Lehrling tut. Es ist von nichts, was außer dir ist, die Rede, sondern lediglich von dir selbst*.»",
      "-075-* Sämtliche Werke 1, S.422.",
      "Diese Art, die Wissenschaftslehre einzuleiten, hat allerdings vor der andern einen großen Vorzug. Denn die Selbst-beobachtung liefert ja die Tätigkeit des Ich in der Tat nicht einseitig nach einer bestimmten Richtung hin, sie zeigt es nicht bloß Sein-setzend, sondern sie zeigt es in seiner all­seitigen Entfaltung, wie es denkend den unmittelbar ge­gebenen Weltinhalt zu begreifen sucht.",
      "Der Selbstbeobach­tung zeigt sich das Ich wie es sich das Weltbild aus dem Zusammenfügen von Gegebenem und Begriff aufbaut. Aber für denjenigen, der unsere obige Betrachtung nicht mit durchgemacht hat der also nicht weiß, daß das Ich nur dann zum ganzen Inhalte der Wirklichkeit kommt, wenn es mit seinen Denkformen an das Gegebene heran­tritt -, für den erscheint der Erkenntnisprozeß als ein Her­ausspinnen der Welt aus dem Ich.",
      "Für Fichte wird das Weltbild daher immer mehr zu einer Konstruktion des Ich. Er betont immer stärker, daß es in der Wissenschaftslehre darauf ankomme, den Sinn zu erwecken, der imstande ist, das Ich bei diesem Konstruieren der Welt zu belauschen.",
      "Wer dies vermag, erscheint ihm auf einer höheren Wissensstufe als derjenige, der nur das Konstruierte, das fertige Sein sieht. Wer nur die Welt der Objekte betrachtet, der erkennt nicht, daß sie vom Ich erst geschaffen werden.",
      "Wer aber das Ich in seinem Konstruieren betrachtet, der sieht den Grund des fertigen Weltbildes; er weiß, wodurch es geworden, es erscheint ihm als Folge, zu dem ihm die Vor­aussetzungen gegeben sind. Das gewöhnliche Bewußtsein sieht nur dasjenige, was gesetzt ist, was in dieser oder jener Weise bestimmt ist.",
      "Es fehlt ihm die Einsicht in die Vordersätze, in die Gründe: warum es gerade so gesetzt ist und nicht anders. Das Wissen um diese Vordersätze zu vermitteln,­",
      "ist nach Fichte die Aufgabe eines ganz neuen Sin­nes. Am deutlichsten ausgesprochen finde ich dies in den «Einleitungsvorlesungen in die Wissenschaftslehre. Vor­gelesen im Herbste 1813 auf der Universität zu Berlin»:",
      "«Diese Lehre setzt voraus ein ganz neues inneres Sinneswerkzeug, durch welches eine neue Welt gegeben wird, die für den gewöhnlichen Menschen gar nicht vorhanden ist. Oder: «Die Welt des neuen Sinnes und dadurch er selbst ist vorläufig klar bestimmt: sie ist das Sehen der Vordersätze, auf die das Urteil: es ist etwas, sich gründet; der Grund des Seins, der eben darum, weil er dies ist, nicht selbst wieder ist und ein Sein ist*.",
      "Die klare Einsicht in den Inhalt der vom Ich ausgeführ­ten Tätigkeit fehlt aber Fichte auch hier. Er ist nie zu der­selben durchgedrungen. Deshalb konnte seine Wissenschafts­lehre das nicht werden, was sie sonst, ihrer ganzen Anlage nach, hätte werden müssen: eine Erkenntnistheorie als philosophische Grundwissenschaft. War nämlich einmal er­kannt, daß die Tätigkeit des Ich von diesem selbst gesetzt werden muß, so lag nahe, daran zu denken, daß sie auch vom Ich ihre Bestimmung erhält. Wie kann das aber anders geschehen, als indem man dem rein formellen Tun des Ich einen Inhalt gibt. Soll dieser aber wirklich durch das Ich in dessen sonst ganz unbestimmte Tätigkeit hineingelegt wer­den, so muß derselbe auch seiner Natur nach bestimmt werden. Sonst könnte er doch höchstens durch ein im Ich liegendes «Ding an sich», dessen Werkzeug das Ich ist, nicht aber durch letzteres selbst realisiert werden. Hätte",
      "-077-* J. G. Fichtes nachgelassene Werke. Herausgegeben von J. H. Fichte, Bd. 1, Bonn 1834, S.4 und S.16.",
      "Fichte diese Bestimmung versucht, dann wäre er aber zum Begriffe der Erkenntnis gekommen, der von dem Ich ver­wirklicht werden soll. Fichtes Wissenschaftslehre ist ein Beleg dafür, daß es selbst dem scharfsinnigsten Denken nicht gelingt, auf irgendeinem Felde fruchtbringend ein­zuwirken, wenn man nicht zu der richtigen Gedankenform (Kategorie, Idee) kommt, die, mit dem Gegebenen ergänzt, die Wirklichkeit gibt. Es geht einem solchen Betrachter so, wie jenem Menschen, dem die herrlichsten Melodien ge­boten werden, und der sie gar nicht hört, weil er keine Empfindung für Melodie hat. Das Bewußtsein, als Gegebe­nes, kann nur der charakterisieren, der sich in den Besitz der «Idee des Bewußtseins»zu setzen weiß.",
      "Fichte ist einmal sogar der richtigen Einsicht ganz nahe. Er findet 1797 in den «Einleitungen zur Wissenschafts­lehre», es gäbe zwei theoretische Systeme, den Dogmatis­mus, der das Ich von den Dingen, und den Idealismus, der die Dinge vom Ich bestimmt sein läßt. Beide stehen, nach seiner Ansicht, als mögliche Weltanschauungen fest. Der eine wie der andere gestatte eine konsequente Durchfüh­rung. Aber wenn wir uns dem Dogmatismus ergeben, dann müssen wir eine Selbständigkeit des Ich aufgeben und das­selbe vom Ding an sich abhängig machen. Im umgekehrten Falle sind wir, wenn wir dem Idealismus huldigen. Welches der Systeme der eine oder der andere Philosoph wählen will, das stellt Fichte lediglich dem Belieben des Ich anheim. Wenn dasselbe aber seine Selbständigkeit wahren wolle, so hebe es den Glauben an die Dinge außer uns auf und ergebe sich dem Idealismus.",
      "Nun hätte es nur noch der Überlegung bedurft, daß das Ich ja zu gar keiner wirklichen, gegründeten Entscheidung",
      "und Bestimmung kommen kann, wenn es nicht etwas vor­aussetzt, welches ihm zu einer solchen verhilft. Alle Bestim­mung vom Ich aus bliebe leer und inhaltlos, wenn das Ich nicht etwas Inhaltsvolles, durch und durch Bestimmtes fin­det, was ihm die Bestimmung des Gegebenen möglich macht und damit auch zwischen Idealismus und Dogmatismus die Wahl treffen läßt. Dieses durch und durch Inhaltsvolle ist aber die Welt des Denkens. Und das Gegebene durch das Denken bestimmen heißt Erkennen. Wir mögen Fichte an­fassen, wo wir wollen: überall finden wir, daß sein Ge­dankengang sofort Hand und Fuß gewinnt, wenn wir die bei ihm ganz graue, leere Tätigkeit des Ich erfüllt und geregelt denken von dem, was wir Erkenntnisprozeß ge­nannt haben.",
      "Der Umstand, daß das Ich durch Freiheit sich in Tätig­keit versetzen kann, macht es ihm möglich, aus sich heraus durch Selbstbestimmung die Kategorie des Erkennens zu realisieren, während in der übrigen Welt die Kategorien sich durch objektive Notwendigkeit mit dem ihnen kor­respondierenden Gegebenen verknüpft erweisen. Das We­sen der freien Selbstbestimmung zu untersuchen, wird die Aufgabe einer auf unsere Erkenntnistheorie gestützten Ethik und Metaphysik sein. Diese werden auch die Frage zu erörtern haben, ob das Ich auch noch andere Ideen außer der Erkenntnis zu realisieren vermag. Daß die Realisierung des Erkennens durch Freiheit geschieht, geht aber aus den oben gemachten Anmerkungen bereits klar hervor. Denn wenn das unmittelbar Gegebene und die dazugehörige Form des Denkens durch das Ich im Erkenntnisprozeß vereinigt werden, so kann die Vereinigung der sonst immer getrennt im Bewußtsein verbleibenden zwei Elemente­",
      "der Wirklichkeit nur durch einen Akt der Freiheit geschehen.",
      "Durch unsere Ausführungen wird aber noch in ganz an­derer Weise Licht auf den kritischen Idealismus geworfen. Demjenigen, der sich eingehend mit Fichtes System befaßt hat, erscheint es wie eine Herzensangelegenheit dieses Phi­losophen, den Satz aufrechtzuerhalten, daß in das Ich nichts von außen hineinkommen kann, daß nichts in demselben auftritt, was nicht ursprünglich von demselben selbst ge­setzt wird.",
      "Nun ist aber außer Frage, daß kein Idealismus je imstande sein wird, jene Form des Weltinhaltes aus dem Ich abzuleiten, die wir als die unmittelbar gegebene be­zeichnet haben. Diese Form kann eben nur gegeben> nie­mals aus dem Denken heraus konstruiert werden.",
      "Man erwäge doch nur, daß wir es nicht zustande brächten, selbst wenn uns die ganze übrige Farbenskala gegeben wäre, auch nur eine Farbennuance bloß vom Ich aus zu ergänzen. Wir können uns ein Bild der entferntesten, von uns nie gesehe­nen Ländergebiete machen, wenn wir die Elemente dazu als gegebene einmal individuell erlebt haben.",
      "Wir kom­binieren uns dann das Bild nach gegebener Anleitung aus von uns erlebten Einzeltatsachen. Vergebens aber werden wir danach streben, auch nur ein einziges Wahrnehmungs­element, das nie im Bereich des uns Gegebenen lag, aus uns herauszuspinnen.",
      "Ein anderes aber ist das bloße Kennen der gegebenen Welt; ein anderes das Erkennen von deren Wesenheit. Letztere wird uns, trotzdem sie innig mit dem Weltinhalte verknüpft ist, nicht klar, ohne daß wir die Wirklichkeit aus Gegebenem und Denken selbst erbauen.",
      "Das eigentliche «Was»des Gegebenen wird für das Ich nur durch das letztere selbst gesetzt. Das Ich hätte aber gar",
      "keine Veranlassung, das Wesen eines Gegebenen in sich zu setzen, wenn es nicht die Sache zuerst in ganz bestimmungs­loser Weise sich gegenüber sähe. Was also als Wesen der Welt vom Ich gesetzt wird, das wird nicht ohne das Ich, sondern durch dasselbe gesetzt.",
      "Nicht die erste Gestalt, in der die Wirklichkeit an das Ich herantritt, ist deren wahre, sondern die letzte, die das Ich aus derselben macht. Jene erste Gestalt ist überhaupt ohne Bedeutung für die objektive Welt und hat eine solche nur als Unterlage für den Erkenntnisprozeß. Also nicht die Gestalt der Welt, welche die Theorie derselben gibt, ist die subjektive, sondern vielmehr jene, welche dem Ich zuerst gegeben ist. Will man nach dem Vorgange Volkelts u. a. diese gegebene Welt die Erfahrung nennen, so muß man sagen: die Wissenschaft ergänzt das infolge der Einrichtung unseres Bewußtseins in subjektiver Form, als Erfahrung, auftretende Weltbild zu dem, was es wesentlich ist.",
      "Unsere Erkenntnistheorie liefert die Grundlage für einen im wahren Sinne des Wortes sich selbst verstehenden Idea­lismus. Sie begründet die Überzeugung, daß im Denken die Essenz der Welt vermittelt wird. Durch nichts anderes als durch das Denken kann das Verhältnis der Teile des Welt­inhaltes aufgezeigt werden, ob es nun das Verhältnis der Sonnenwärme zum erwärmten Stein oder des Ich zur Außenwelt ist. Im Denken allein ist das Element gegeben, welches alle Dinge in ihren Verhältnissen zueinander be­stimmt.",
      "Der Einwand, den der Kantianismus noch machen könnte, wäre der, daß die oben charakterisierte Wesensbestimmung des Gegebenen doch nur eine solche für das Ich sei. Dem­gegenüber müssen wir im Sinne unserer Grundauffassung",
      "erwidern, daß ja auch die Spaltung des Ich und der Außen­welt nur innerhalb des Gegebenen Bestand hat, daß also jenes «für das Ich»der denkenden Betrachtung gegenüber, die alle Gegensätze vereinigt, keine Bedeutung hat. Das Ich als ein von der Außenwelt Abgetrenntes geht in der denkenden Weltbetrachtung völlig unter; es hat also gar keinen Sinn mehr, von Bestimmungen bloß für das Ich zu sprechen."
    ],
    "sentences": [
      [
        "DIE VORAUSSETZUNGSLOSE ERKENNTNISTHEORIE UND FICHTES WISSENSCHAFTSLEHRE"
      ],
      [
        "Mit den bisherigen Ausführungen haben wir die Idee der Erkenntnis festgestellt.",
        "Unmittelbar gegeben ist diese Idee nun im menschlichen Bewußtsein, insofern es sich erkennend verhält.",
        "Dem «Ich»als Mittelpunkt des Bewußtseins ist die äußere und innere Wahrnehmung und sein eigenes Dasein unmittelbar gegeben. (Es braucht wohl kaum gesagt zu werden, daß wir mit der Bezeichnung «Mittelpunkt hier nicht eine theoretische Ansicht über die Natur des Be­wußtseins verknüpft wissen wollen, sondern daß wir sie nur als stilistische Abkürzung für die Gesamtphysiognomie des Bewußtseins gebrauchen.) Das Ich fühlt den Drang, in diesem Gegebenen mehr zu finden, als was unmittelbar ge­geben ist.",
        "Es geht ihm gegenüber der gegebenen Welt die zweite, die des Denkens auf, und es verbindet die beiden da­durch, daß es aus freiem Entschluß das verwirklicht, was wir als Idee des Erkennens festgestellt haben.",
        "Hierin liegt nun ein Grundunterschied zwischen der Art, wie sich im Objekt des menschlichen Bewußtseins selbst Begriff und Unmittelbar-Gegebenes zur totalen Wirklichkeit verbun­den zeigen, und jener, die dem übrigen Weltinhalte gegen­über Geltung hat.",
        "Bei jedem andern Teil des Weltbildes müssen wir uns vorstellen, daß die Verbindung das Ur­sprüngliche, von vornherein Notwendige ist, und daß nur am Beginne des Erkennens für die Erkenntnis eine künst­liche Trennung eingetreten ist, die aber zuletzt durch das Erkennen, der ursprünglichen Wesenheit des Objektiven"
      ],
      [
        "gemäß, wieder aufgehoben wird.",
        "Beim menschlichen Be­wußtsein ist das anders.",
        "Hier ist die Verbindung nur vor­handen, wenn sie in wirklicher Tätigkeit vom Bewußtsein vollzogen wird.",
        "Bei jedem andern Objekte hat die Tren­nung für das Objekt keine Bedeutung, sondern nur für die Erkenntnis."
      ],
      [
        "Die Verbindung ist hier das erste, die Tren­nung das Abgeleitete.",
        "Das Erkennen vollzieht nur die Trennung, weil es sich auf seine Art nicht in den Besitz der Verbindung setzen kann, wenn es nicht vorher getrennt hat."
      ],
      [
        "Begriff und gegebene Wirklichkeit des Bewußtseins aber sind ursprünglich getrennt, die Verbindung ist das Ab­geleitete, und deswegen ist das Erkennen so beschaffen, wie wir es geschildert haben.",
        "Weil im Bewußtsein notwendig Idee und Gegebenes getrennt auftreten, deswegen spaltet sich für dasselbe die gesamte Wirklichkeit in diese zwei Teile, und weil das Bewußtsein nur durch eigene Tätigkeit die Verbindung der beiden genannten Elemente bewirken kann, deshalb gelangt es nur durch Verwirklichung des Er­kenntnisaktes zur vollen Wirklichkeit."
      ],
      [
        "Die übrigen Kate­gorien (Ideen) wären auch dann notwendig mit den ent­sprechenden Formen des Gegebenen verknüpft, wenn sie nicht in die Erkenntnis aufgenommen würden; die Idee des Erkennens kann mit dem ihr entsprechenden Gegebe­nen nur durch die Tätigkeit des Bewußtseins vereinigt wer­den.",
        "Ein wirkliches Bewußtsein existiert nur, wenn es sich selbst verwirklicht."
      ],
      [
        "Damit glauben wir genügend vorberei­tet zu sein, um den Grundfehler von Fichtes «Wissenschafts­lehre»bloßzulegen und zugleich den Schlüssel zu ihrem Verständnis zu liefern.",
        "Fichte ist derjenige Philosoph, wel­cher unter Kants Nachfolgern am lebhaftesten gefühlt hat, daß eine Grundlegung aller Wissenschaften nur in einer"
      ],
      [
        "Theorie des Bewußtseins bestehen könne; aber er kam nie zur Erkenntnis, warum das so ist.",
        "Er empfand, daß das­jenige, was wir als zweiten Schritt der Erkenntnistheorie bezeichnen, und dem wir die Form eines Postulates geben, von dem «Ich»wirklich ausgeführt werden müsse.",
        "Wir ersehen dies z.",
        "B. aus seinen folgenden Worten: «Die Wissenschaftslehre entsteht also, insofern sie eine systema­tische Wissenschaft sein soll, geradeso wie alle möglichen Wissenschaften, insofern sie systematisch sein sollen, durch eine Bestimmung der Freiheit, welche letztere hier ins­besondere bestimmt ist, die Handlungsart der Intelligenz überhaupt zum Bewußtsein zu erheben; ...",
        "Durch diese freie Handlung wird nun etwas, das schon an sich Form ist, die notwendige Handlung der Intelligenz, als Gehalt in eine neue Form des Wissens oder Bewußtseins aufgenom­men . . .~»Was ist hier unter Handlungsart der «Intelli­genz»zu verstehen, wenn man das, was dunkel gefühlt ist, in klaren Begriffen ausspricht?",
        "Nichts anderes als die im Bewußtsein sich vollziehende Verwirklichung der Idee des Erkennens.",
        "Wäre Fichte sich dessen vollkommen klar be­wußt gewesen, dann hätte er den obigen Satz einfach so formulieren müssen: Die Wissenschaftslehre hat das Er­kennen, insofern es noch unbewußte Tätigkeit des «Ich ist, zum Bewußtsein zu erheben; sie hat zu zeigen, daß im «Ich»als notwendige Handlung die Objektivierung der Idee des Erkennens ausgeführt wird."
      ],
      [
        "Fichte will die Tätigkeit des «Ich»bestimmen.",
        "Er findet: «Dasjenige, dessen Seyn (Wesen) bloß darin besteht, daß"
      ],
      [
        "-069-* Über den Begriff der Wissenschaftslehre oder der sogenannten Philosophie.",
        "Sämtliche Werke, Berlin 1845, Bd.",
        "I, S.71 f."
      ],
      [
        "es sich selbst als seyend setzt, ist das Ich, als absolutes Sub­jekt»*.",
        "Dieses Setzen des Ich ist für Fichte die erste un­bedingte Tathandlung, die allem übrigen «Bewußtseyn zum Grunde liegt»*.",
        "Das Ich kann also im Sinne Fichtes auch nur durch einen absoluten Entschluß alle seine Tätigkeit beginnen."
      ],
      [
        "Aber für Fichte ist es unmöglich, dieser seiner vom Ich absolut gesetzten Tätigkeit zu irgendeinem In­halte ihres Tuns zu verhelfen.",
        "Denn er hat nichts, worauf sich diese Tätigkeit richten, wonach sie sich bestimmen soll."
      ],
      [
        "Sein Ich soll eine Tathandlung vollziehen; aber was soll es tun?",
        "Weil Fichte den Begriff der Erkenntnis nicht aufstellte, den das Ich verwirklichen soll, deshalb rang er vergeblich, irgendeinen Fortgang von seiner absoluten Tathandlung zu den weiteren Bestimmungen des Ich zu finden."
      ],
      [
        "Ja, er er­klärt zuletzt in bezug auf einen solchen Fortgang, daß die Untersuchung hierüber außerhalb der Grenzen der Theorie liege.",
        "Er geht in seiner Deduktion der Vorstellung weder von einer absoluten Tätigkeit des Ich noch des Nicht-Ich, sondern von einem Bestimmten aus, das zugleich Bestim­men ist, weil im Bewußtsein unmittelbar nichts anderes enthalten ist noch enthalten sein kann."
      ],
      [
        "Was diese Bestim­mung wieder bestimmt, bleibt in der Theorie vollständig unentschieden; und durch diese Unbestimmtheit werden wir denn auch über die Theorie hinaus in den praktischen Teil der Wissenschaftslehre getrieben*** Durch diese Er­klärung vernichtet aber Fichte überhaupt alles Erkennen.",
        "Denn die praktische Tätigkeit des Ich gehört in ein ganz anderes Gebiet."
      ],
      [
        "Daß das von uns oben aufgestellte Postulat"
      ],
      [
        "-070-* Grundlage der gesamten Wissenschaftslehre.",
        "Sämtl.",
        "Werke 1, S.97."
      ],
      [
        "-070-** Sämtliche Werke I, S.91."
      ],
      [
        "-070-*** Sämtliche Werke I, S. 178."
      ],
      [
        "nur durch eine freie Handlung des Ich realisiert werden kann, ist ja klar; aber wenn das Ich sich erkennend verhal­ten soll, so kommt es gerade darauf an, daß die Entschlie­ßung desselben dahin geht, die Idee des Erkennens zu ver­wirklichen.",
        "Es ist ja gewiß richtig, daß das Ich aus freiem Entschluß noch vieles andere vollführen kann."
      ],
      [
        "Aber nicht auf eine Charakteristik des «freien>, sondern auf eine solche des «erkennenden»Ich kommt es bei der erkenntnis-theoretischen Grundlegung aller Wissenschaften an.",
        "Fichte hat sich aber von seinem subjektiven Hange, die Freiheit der menschlichen Persönlichkeit in das hellste Licht zu stellen, allzusehr beeinflussen lassen."
      ],
      [
        "Mit Recht bemerkt Harms in seiner Rede «über die Philosophie Fichtes (S.15): «Seine Weltansicht ist eine vorherrschend und aus­schließlich ethische, und seine Erkenntnistheorie trägt kei­nen anderen Charakter.»Das Erkennen hätte absolut keine Aufgabe, wenn alle Gebiete der Wirklichkeit in ihrer Totalität gegeben wären.",
        "Da nun aber das Ich, solange es nicht vom Denken in das systematische Ganze des Weltbildes eingefügt ist, auch nichts anderes ist als ein unmittel­bar Gegebenes, so genügt ein bloßes Aufzeigen seines Tuns durchaus nicht."
      ],
      [
        "Fichte jedoch ist der Ansicht, daß beim Ich mit dem bloßen Aufsuchen schon alles getan sei.",
        "«Wir haben den absolut-ersten, schlechthin unbedingten Grund­satz alles menschlichen Wissens aufzusuchen.",
        "Beweisen oder bestimmen läßt er sich nicht, wenn er absolut-erster Grund­satz sein soll*.» Wir haben gesehen, daß das Beweisen und Bestimmen einzig und allein dem Inhalte der reinen Logik gegenüber nicht am Platze ist."
      ],
      [
        "Das Ich gehört aber der"
      ],
      [
        "-071-* Sämtliche Werke I, S.91."
      ],
      [
        "Wirklichkeit an, und da ist es notwendig, das Vorhanden­sein dieser oder jener Kategorie im Gegebenen festzustellen.",
        "Fichte tat das nicht.",
        "Und hierinnen ist der Grund zu suchen, warum er seiner Wissenschaftslehre eine so verfehlte Ge­stalt gab.",
        "Zeller bemerkt*, daß die logischen Formeln, durch die Fichte zu dem Ich-Begriff kommen will, nur schlecht den Umstand verhüllen, daß dieser eigentlich um jeden Preis den schon vorgefaßten Zweck erreichen wolle, zu diesem Anfangspunkte zu kommen.",
        "Diese Worte be­ziehen sich auf die erste Gestalt, die Fichte 1794 seiner Wissenschaftslehre gab.",
        "Wenn wir daran festhalten, daß Fichte in der Tat, der ganzen Anlage seines Philosophierens nach, nichts wollen konnte, als die Wissenschaft durch einen absoluten Machtspruch beginnen zu lassen, so gibt es ja nur zwei Wege, die dieses Beginnen verständlich erscheinen lassen.",
        "Der eine war der, das Bewußtsein bei irgendeiner seiner empirischen Tätigkeiten anzufassen und durch all­mähliche Losschälung alles dessen, was nicht ursprünglich aus demselben folgt, den reinen Begriff des Ich heraus­zukristallisieren.",
        "Der andere Weg aber war, gleich bei der ursprünglichen Tätigkeit des «Ich»einzusetzen und dessen Natur durch Selbstbesinnung und Selbstbeobachtung auf­zuzeigen.",
        "Den ersten Weg schlug Fichte am Beginne seines Philosophierens ein; im Verlaufe desselben ging er jedoch allmählich zum zweiten über."
      ],
      [
        "An die Synthesis der «transzendentalen Apperzeption »bei Kant anknüpfend, fand Fichte, daß alle Tätigkeit des Ich in der Zusammenfügung des Stoffes der Erfahrung nach"
      ],
      [
        "-072-* Geschichte der deutschen Philosophie seit Leibniz, München 1871 bis 1875, S.605."
      ],
      [
        "den Formen des Urteils bestehe.",
        "Das Urteilen besteht in dem Verknüpfen des Prädikats mit dem Subjekte, was in rein formaler Weise durch den Satz ausgedrückt wird: a = a.",
        "Dieser Satz wäre unmöglich, wenn das x, das beide a verbindet, nicht auf einem Vermögen schlechthin zu set­zen beruhte."
      ],
      [
        "Denn der Satz bedeutet ja nicht: a ist, son­dern: wenn a ist, so ist a.",
        "Also von einem absoluten Setzen des a kann nicht die Rede sein.",
        "So bleibt denn nichts, um überhaupt zu einem absoluten, schlechthin Gültigen zu kommen, als das Setzen selbst für absolut zu erklären."
      ],
      [
        "Während das a bedingt ist, ist das Setzen des a unbedingt.",
        "Dieses Setzen ist aber eine Tathandlung des Ich.",
        "Dem Ich kommt somit eine Fähigkeit zu, schlechthin und unbedingt zu setzen.",
        "In dem Satze a = a wird das eine a nur gesetzt, indem das andere vorausgesetzt wird; und zwar wird es durch das Ich gesetzt."
      ],
      [
        "«Wenn a im Ich gesetzt ist, so ist es gesetzt*.»Dieser Zusammenhang ist nur unter der Be­dingung möglich, daß im Ich etwas sich immer Gleichblei­bendes sei, etwas, was von einem a zum andern hinüberfahrt.",
        "Und das oben erwähnte x beruht auf diesem Gleich­bleibenden."
      ],
      [
        "Das Ich, welches das eine a setzt, ist dasselbe wie jenes, welches das andere setzt.",
        "Das heißt aber Ich Ich.",
        "Dieser Satz in Form des Urteils ausgedrückt: Wenn Ich ist, so ist es - hat keinen Sinn.",
        "Das Ich wird ja nicht unter der Voraussetzung eines andern gesetzt, sondern es setzt sich selbst voraus."
      ],
      [
        "Das heißt aber: es ist schlechthin und un­bedingt.",
        "Die hypothetische Form des Urteils, die ohne die Voraussetzung des absoluten Ich allem Urteilen zukommt, verwandelt sich hier in die Form des absoluten Existenzialsatzes:­"
      ],
      [
        "-073-* Sämtliche Werke I,S.94."
      ],
      [
        "Ich bin schlechtweg.",
        "Fichte drückt dies auch noch folgendermaßen aus*: «Das Ich setzt ursprünglich schlecht­hin sein eigenes Sein.»Wir sehen, daß diese ganze Ab­leitung Fichtes nichts ist als eine Art pädagogischer Aus­einandersetzung, um seine Leser dahin zu führen, wo ihnen die Erkenntnis der unbedingten Tätigkeit des Ich aufgeht.",
        "Es soll denselben jene Handlung des Ich klar vor Augen gebracht werden, ohne deren Vollzug überhaupt gar kein Ich ist."
      ],
      [
        "Wir wollen nun auf Fichtes Gedankengang noch einmal zurückblicken.",
        "Bei schärferem Zusehen stellt sich nämlich heraus, daß in demselben ein Sprung ist, und zwar ein sol­cher, der die Richtigkeit der Anschauung von der ursprüng­lichen Tathandlung in Frage stellt.",
        "Was ist denn eigentlich wirklich absolut in dem Setzen des Ich?",
        "Es wird geurteilt: Wenn a ist, so ist a.",
        "Das a wird vom Ich gesetzt.",
        "Über dieses Setzen kann also kein Zweifel obwalten.",
        "Aber wenn auch als Tätigkeit unbedingt, so kann das Ich doch nur irgend etwas setzen.",
        "Es kann nicht die «Tätigkeit an und für sich», sondern nur eine bestimmte Tätigkeit setzen.",
        "Kurz: das Setzen muß einen Inhalt haben.",
        "Diesen kann es aber nicht aus sich selbst nehmen, denn sonst könnte es nichts weiter als ewig nur das Setzen setzen.",
        "Es muß also für das Setzen, für die absolute Tätigkeit des Ich etwas geben, das durch sie realisiert wird.",
        "Ohne daß das Ich zu einem Gegebenen greift, das es setzt, kann es überhaupt «nichts, folglich nicht setzen.",
        "Das zeigt auch der Fichtesche Satz: Das Ich setzt sein Sein.",
        "Dieses Sein ist eine Kategorie.",
        "Wir sind wieder bei unserm Satze: Die Tätigkeit des Ich beruht darauf,"
      ],
      [
        "-074-* Sämtliche Werke I , S.98."
      ],
      [
        "daß das Ich aus eigenem freiem Entschlusse die Begriffe und Ideen des Gegebenen setzt.",
        "Nur dadurch, daß Fichte unbewußt darauf ausgeht, das Ich als «Seiendes»nach­zuweisen, kommt er zu seinem Resultate.",
        "Hätte er den Be­griff des Erkennens entwickelt, so wäre er zu dem wahren Ausgangspunkte der Erkenntnistheorie gekommen: Das Ich setzt das Erkennen.",
        "Da Fichte sich nicht klarmachte, wo­durch die Tätigkeit des Ich bestimmt wird, bezeichnete er einfach das Setzen des Seins als Charakter dieser Tätigkeit.",
        "Damit hatte er aber auch die absolute Tätigkeit des Ich beschränkt.",
        "Denn ist nur das «Sein-Setzen»des Ich un­bedingt, dann ist ja alles andere, was vom Ich ausgeht, bedingt.",
        "Aber es ist auch jeder Weg abgeschnitten, um vom Unbedingten zum Bedingten zu kommen.",
        "Wenn das Ich nur nach der bezeichneten Richtung hin unbedingt ist, dann hört sofort die Möglichkeit für dasselbe auf, etwas anderes als sein eigenes Sein durch einen ursprünglichen Akt zu setzen.",
        "Es tritt somit die Notwendigkeit ein, den Grund für alle andere Tätigkeit des Ich anzugeben.",
        "Fichte suchte nach einem solchen vergebens, wie wir oben bereits gesehen haben."
      ],
      [
        "Daher wandte er sich zu dem andern der oben bezeich­neten Wege behufs Ableitung des Ich.",
        "Schon 1797 in der «Ersten Einleitung in die Wissenschaftslehre»empfiehlt er die Selbstbeobachtung als das Richtige, um das Ich in sei­nem ureigenen Charakter zu erkennen.",
        "«Merke auf dich selbst, kehre deinen Blick von allem, was dich umgibt, ab und in dein Inneres - ist die erste Forderung, welche die Philosophie an ihren Lehrling tut.",
        "Es ist von nichts, was außer dir ist, die Rede, sondern lediglich von dir selbst*.»"
      ],
      [
        "-075-* Sämtliche Werke 1, S.422."
      ],
      [
        "Diese Art, die Wissenschaftslehre einzuleiten, hat allerdings vor der andern einen großen Vorzug.",
        "Denn die Selbst-beobachtung liefert ja die Tätigkeit des Ich in der Tat nicht einseitig nach einer bestimmten Richtung hin, sie zeigt es nicht bloß Sein-setzend, sondern sie zeigt es in seiner all­seitigen Entfaltung, wie es denkend den unmittelbar ge­gebenen Weltinhalt zu begreifen sucht."
      ],
      [
        "Der Selbstbeobach­tung zeigt sich das Ich wie es sich das Weltbild aus dem Zusammenfügen von Gegebenem und Begriff aufbaut.",
        "Aber für denjenigen, der unsere obige Betrachtung nicht mit durchgemacht hat der also nicht weiß, daß das Ich nur dann zum ganzen Inhalte der Wirklichkeit kommt, wenn es mit seinen Denkformen an das Gegebene heran­tritt -, für den erscheint der Erkenntnisprozeß als ein Her­ausspinnen der Welt aus dem Ich."
      ],
      [
        "Für Fichte wird das Weltbild daher immer mehr zu einer Konstruktion des Ich.",
        "Er betont immer stärker, daß es in der Wissenschaftslehre darauf ankomme, den Sinn zu erwecken, der imstande ist, das Ich bei diesem Konstruieren der Welt zu belauschen."
      ],
      [
        "Wer dies vermag, erscheint ihm auf einer höheren Wissensstufe als derjenige, der nur das Konstruierte, das fertige Sein sieht.",
        "Wer nur die Welt der Objekte betrachtet, der erkennt nicht, daß sie vom Ich erst geschaffen werden."
      ],
      [
        "Wer aber das Ich in seinem Konstruieren betrachtet, der sieht den Grund des fertigen Weltbildes; er weiß, wodurch es geworden, es erscheint ihm als Folge, zu dem ihm die Vor­aussetzungen gegeben sind.",
        "Das gewöhnliche Bewußtsein sieht nur dasjenige, was gesetzt ist, was in dieser oder jener Weise bestimmt ist."
      ],
      [
        "Es fehlt ihm die Einsicht in die Vordersätze, in die Gründe: warum es gerade so gesetzt ist und nicht anders.",
        "Das Wissen um diese Vordersätze zu vermitteln,­"
      ],
      [
        "ist nach Fichte die Aufgabe eines ganz neuen Sin­nes.",
        "Am deutlichsten ausgesprochen finde ich dies in den «Einleitungsvorlesungen in die Wissenschaftslehre.",
        "Vor­gelesen im Herbste 1813 auf der Universität zu Berlin»:"
      ],
      [
        "«Diese Lehre setzt voraus ein ganz neues inneres Sinneswerkzeug, durch welches eine neue Welt gegeben wird, die für den gewöhnlichen Menschen gar nicht vorhanden ist.",
        "Oder: «Die Welt des neuen Sinnes und dadurch er selbst ist vorläufig klar bestimmt: sie ist das Sehen der Vordersätze, auf die das Urteil: es ist etwas, sich gründet; der Grund des Seins, der eben darum, weil er dies ist, nicht selbst wieder ist und ein Sein ist*."
      ],
      [
        "Die klare Einsicht in den Inhalt der vom Ich ausgeführ­ten Tätigkeit fehlt aber Fichte auch hier.",
        "Er ist nie zu der­selben durchgedrungen.",
        "Deshalb konnte seine Wissenschafts­lehre das nicht werden, was sie sonst, ihrer ganzen Anlage nach, hätte werden müssen: eine Erkenntnistheorie als philosophische Grundwissenschaft.",
        "War nämlich einmal er­kannt, daß die Tätigkeit des Ich von diesem selbst gesetzt werden muß, so lag nahe, daran zu denken, daß sie auch vom Ich ihre Bestimmung erhält.",
        "Wie kann das aber anders geschehen, als indem man dem rein formellen Tun des Ich einen Inhalt gibt.",
        "Soll dieser aber wirklich durch das Ich in dessen sonst ganz unbestimmte Tätigkeit hineingelegt wer­den, so muß derselbe auch seiner Natur nach bestimmt werden.",
        "Sonst könnte er doch höchstens durch ein im Ich liegendes «Ding an sich», dessen Werkzeug das Ich ist, nicht aber durch letzteres selbst realisiert werden.",
        "Hätte"
      ],
      [
        "-077-* J.",
        "Fichtes nachgelassene Werke.",
        "Herausgegeben von J.",
        "Fichte, Bd. 1, Bonn 1834, S.4 und S.16."
      ],
      [
        "Fichte diese Bestimmung versucht, dann wäre er aber zum Begriffe der Erkenntnis gekommen, der von dem Ich ver­wirklicht werden soll.",
        "Fichtes Wissenschaftslehre ist ein Beleg dafür, daß es selbst dem scharfsinnigsten Denken nicht gelingt, auf irgendeinem Felde fruchtbringend ein­zuwirken, wenn man nicht zu der richtigen Gedankenform (Kategorie, Idee) kommt, die, mit dem Gegebenen ergänzt, die Wirklichkeit gibt.",
        "Es geht einem solchen Betrachter so, wie jenem Menschen, dem die herrlichsten Melodien ge­boten werden, und der sie gar nicht hört, weil er keine Empfindung für Melodie hat.",
        "Das Bewußtsein, als Gegebe­nes, kann nur der charakterisieren, der sich in den Besitz der «Idee des Bewußtseins»zu setzen weiß."
      ],
      [
        "Fichte ist einmal sogar der richtigen Einsicht ganz nahe.",
        "Er findet 1797 in den «Einleitungen zur Wissenschafts­lehre», es gäbe zwei theoretische Systeme, den Dogmatis­mus, der das Ich von den Dingen, und den Idealismus, der die Dinge vom Ich bestimmt sein läßt.",
        "Beide stehen, nach seiner Ansicht, als mögliche Weltanschauungen fest.",
        "Der eine wie der andere gestatte eine konsequente Durchfüh­rung.",
        "Aber wenn wir uns dem Dogmatismus ergeben, dann müssen wir eine Selbständigkeit des Ich aufgeben und das­selbe vom Ding an sich abhängig machen.",
        "Im umgekehrten Falle sind wir, wenn wir dem Idealismus huldigen.",
        "Welches der Systeme der eine oder der andere Philosoph wählen will, das stellt Fichte lediglich dem Belieben des Ich anheim.",
        "Wenn dasselbe aber seine Selbständigkeit wahren wolle, so hebe es den Glauben an die Dinge außer uns auf und ergebe sich dem Idealismus."
      ],
      [
        "Nun hätte es nur noch der Überlegung bedurft, daß das Ich ja zu gar keiner wirklichen, gegründeten Entscheidung"
      ],
      [
        "und Bestimmung kommen kann, wenn es nicht etwas vor­aussetzt, welches ihm zu einer solchen verhilft.",
        "Alle Bestim­mung vom Ich aus bliebe leer und inhaltlos, wenn das Ich nicht etwas Inhaltsvolles, durch und durch Bestimmtes fin­det, was ihm die Bestimmung des Gegebenen möglich macht und damit auch zwischen Idealismus und Dogmatismus die Wahl treffen läßt.",
        "Dieses durch und durch Inhaltsvolle ist aber die Welt des Denkens.",
        "Und das Gegebene durch das Denken bestimmen heißt Erkennen.",
        "Wir mögen Fichte an­fassen, wo wir wollen: überall finden wir, daß sein Ge­dankengang sofort Hand und Fuß gewinnt, wenn wir die bei ihm ganz graue, leere Tätigkeit des Ich erfüllt und geregelt denken von dem, was wir Erkenntnisprozeß ge­nannt haben."
      ],
      [
        "Der Umstand, daß das Ich durch Freiheit sich in Tätig­keit versetzen kann, macht es ihm möglich, aus sich heraus durch Selbstbestimmung die Kategorie des Erkennens zu realisieren, während in der übrigen Welt die Kategorien sich durch objektive Notwendigkeit mit dem ihnen kor­respondierenden Gegebenen verknüpft erweisen.",
        "Das We­sen der freien Selbstbestimmung zu untersuchen, wird die Aufgabe einer auf unsere Erkenntnistheorie gestützten Ethik und Metaphysik sein.",
        "Diese werden auch die Frage zu erörtern haben, ob das Ich auch noch andere Ideen außer der Erkenntnis zu realisieren vermag.",
        "Daß die Realisierung des Erkennens durch Freiheit geschieht, geht aber aus den oben gemachten Anmerkungen bereits klar hervor.",
        "Denn wenn das unmittelbar Gegebene und die dazugehörige Form des Denkens durch das Ich im Erkenntnisprozeß vereinigt werden, so kann die Vereinigung der sonst immer getrennt im Bewußtsein verbleibenden zwei Elemente­"
      ],
      [
        "der Wirklichkeit nur durch einen Akt der Freiheit geschehen."
      ],
      [
        "Durch unsere Ausführungen wird aber noch in ganz an­derer Weise Licht auf den kritischen Idealismus geworfen.",
        "Demjenigen, der sich eingehend mit Fichtes System befaßt hat, erscheint es wie eine Herzensangelegenheit dieses Phi­losophen, den Satz aufrechtzuerhalten, daß in das Ich nichts von außen hineinkommen kann, daß nichts in demselben auftritt, was nicht ursprünglich von demselben selbst ge­setzt wird."
      ],
      [
        "Nun ist aber außer Frage, daß kein Idealismus je imstande sein wird, jene Form des Weltinhaltes aus dem Ich abzuleiten, die wir als die unmittelbar gegebene be­zeichnet haben.",
        "Diese Form kann eben nur gegeben> nie­mals aus dem Denken heraus konstruiert werden."
      ],
      [
        "Man erwäge doch nur, daß wir es nicht zustande brächten, selbst wenn uns die ganze übrige Farbenskala gegeben wäre, auch nur eine Farbennuance bloß vom Ich aus zu ergänzen.",
        "Wir können uns ein Bild der entferntesten, von uns nie gesehe­nen Ländergebiete machen, wenn wir die Elemente dazu als gegebene einmal individuell erlebt haben."
      ],
      [
        "Wir kom­binieren uns dann das Bild nach gegebener Anleitung aus von uns erlebten Einzeltatsachen.",
        "Vergebens aber werden wir danach streben, auch nur ein einziges Wahrnehmungs­element, das nie im Bereich des uns Gegebenen lag, aus uns herauszuspinnen."
      ],
      [
        "Ein anderes aber ist das bloße Kennen der gegebenen Welt; ein anderes das Erkennen von deren Wesenheit.",
        "Letztere wird uns, trotzdem sie innig mit dem Weltinhalte verknüpft ist, nicht klar, ohne daß wir die Wirklichkeit aus Gegebenem und Denken selbst erbauen."
      ],
      [
        "Das eigentliche «Was»des Gegebenen wird für das Ich nur durch das letztere selbst gesetzt.",
        "Das Ich hätte aber gar"
      ],
      [
        "keine Veranlassung, das Wesen eines Gegebenen in sich zu setzen, wenn es nicht die Sache zuerst in ganz bestimmungs­loser Weise sich gegenüber sähe.",
        "Was also als Wesen der Welt vom Ich gesetzt wird, das wird nicht ohne das Ich, sondern durch dasselbe gesetzt."
      ],
      [
        "Nicht die erste Gestalt, in der die Wirklichkeit an das Ich herantritt, ist deren wahre, sondern die letzte, die das Ich aus derselben macht.",
        "Jene erste Gestalt ist überhaupt ohne Bedeutung für die objektive Welt und hat eine solche nur als Unterlage für den Erkenntnisprozeß.",
        "Also nicht die Gestalt der Welt, welche die Theorie derselben gibt, ist die subjektive, sondern vielmehr jene, welche dem Ich zuerst gegeben ist.",
        "Will man nach dem Vorgange Volkelts u. a. diese gegebene Welt die Erfahrung nennen, so muß man sagen: die Wissenschaft ergänzt das infolge der Einrichtung unseres Bewußtseins in subjektiver Form, als Erfahrung, auftretende Weltbild zu dem, was es wesentlich ist."
      ],
      [
        "Unsere Erkenntnistheorie liefert die Grundlage für einen im wahren Sinne des Wortes sich selbst verstehenden Idea­lismus.",
        "Sie begründet die Überzeugung, daß im Denken die Essenz der Welt vermittelt wird.",
        "Durch nichts anderes als durch das Denken kann das Verhältnis der Teile des Welt­inhaltes aufgezeigt werden, ob es nun das Verhältnis der Sonnenwärme zum erwärmten Stein oder des Ich zur Außenwelt ist.",
        "Im Denken allein ist das Element gegeben, welches alle Dinge in ihren Verhältnissen zueinander be­stimmt."
      ],
      [
        "Der Einwand, den der Kantianismus noch machen könnte, wäre der, daß die oben charakterisierte Wesensbestimmung des Gegebenen doch nur eine solche für das Ich sei.",
        "Dem­gegenüber müssen wir im Sinne unserer Grundauffassung"
      ],
      [
        "erwidern, daß ja auch die Spaltung des Ich und der Außen­welt nur innerhalb des Gegebenen Bestand hat, daß also jenes «für das Ich»der denkenden Betrachtung gegenüber, die alle Gegensätze vereinigt, keine Bedeutung hat.",
        "Das Ich als ein von der Außenwelt Abgetrenntes geht in der denkenden Weltbetrachtung völlig unter; es hat also gar keinen Sinn mehr, von Bestimmungen bloß für das Ich zu sprechen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "VII. ERKENNTNISTHEORETISCHE SCHLUSSBETRACHTUNG",
    "paragraphs": [
      "VII. ERKENNTNISTHEORETISCHE SCHLUSSBETRACHTUNG",
      "Wir haben die Erkenntnistheorie begründet als die Wissenschaft von der Bedeutung alles menschlichen Wissens. Durch sie erst verschaffen wir uns Aufklärung über das Verhältnis des Inhaltes der einzelnen Wissenschaften zur Welt. Sie macht es uns möglich, mit Hilfe der Wissenschaften zur Weltanschauung zu kommen. Positives Wissen erwerben wir durch die einzelnen Erkenntnisse; den Wert des Wissens für die Wirklichkeit erfahren wir durch die Erkenntnis­theorie. Dadurch, daß wir streng an diesem Grundsatze festgehalten haben und keinerlei Einzelwissen in unseren Auseinandersetzungen verwertet haben, dadurch haben wir alle einseitigen Weltanschauungen überwunden. Die Ein­seitigkeit entspringt gewöhnlich daher, daß die Unter­suchung, statt sich an den Erkenntnisprozeß selbst zu ma­chen, sogleich an irgendwelche Objekte dieses Prozesses herantritt. Nach unseren Auseinandersetzungen muß der Dogmatismus sein «Ding an sich », der subjektive Idealismus sein «Ich»als Urprinzip fallen lassen, denn diese sind ihrem gegenseitigen Verhältnis nach wesentlich erst im Denken bestimmt. «Ding an sich»und «Ich»sind nicht so zu bestimmen, daß man das eine von dem anderen ableitet, sondern beide müssen vom Denken aus nach ihrem Charak­ter und Verhältnis bestimmt werden. Der Skeptizismus muß von seinem Zweifel an der Erkennbarkeit der Welt ablassen, denn an dem «Gegebenen»ist nichts zu bezweifeln, weil es von allen durch das Erkennen erteilten Prä­dikaten",
      "noch unberührt ist. Wollte er aber behaupten, daß das denkende Erkennen nie an die Dinge herankommen könne, so könnte er das nur durch denkende Überlegung selbst tun, womit er sich aber auch selbst widerlegt. Denn wer durch Denken den Zweifel begründen will, der gibt implizite zu, daß dem Denken eine für das Stützen einer Überzeugung hinreichende Kraft zukommt. Unsere Er­kenntnistheorie, endlich, überwindet den einseitigen Em­pirismus und den einseitigen Rationalismus, indem sie beide auf einer höheren Stufe vereinigt. Auf diese Weise wird sie beiden gerecht. Dem Empiriker werden wir gerecht, indem wir zeigen, daß alle inhaltlichen Erkenntnisse über das Ge­gebene nur in unmittelbarer Berührung mit diesem selbst erlangt werden können. Auch der Rationalist findet bei un­seren Auseinandersetzungen seine Rechnung, da wir das Denken für den notwendigen und einzigen Vermittler des Erkennens erklären.",
      "Am nächsten berührt sich unsere Weltanschauung, wie wir sie erkenntnistheoretisch begründet haben, mit der von A. E. Biedermann vertretenen*. Aber Biedermann braucht zur Begründung seines Standpunktes Feststellungen, die durchaus nicht in die Erkenntnistheorie gehören. So operiert er mit den Begriffen: Sein, Substanz, Raum, Zeit usw., ohne vorher den Erkenntnisprozeß für sich untersucht zu haben. Statt festzustellen, daß im Erkenntnisprozeß zu­nächst nur die beiden Elemente Gegebenes und Denken vorhanden sind, spricht er von Seinsweisen der Wirklichkeit.",
      "-084-*Christliche Dogmatik. Die erkenntnistheoretischen Untersuchun­gen im 1. Band. Eine erschöpfende Auseinandersetzung über diesen Standpunkt hat Eduard von Hartmann geliefert, siehe «Kritische Wanderungen durch die Philosophie der Gegenwart» S.200 ff.",
      "So sagt er z. B. § 15: «In allem Bewußtseinsinhalt sind zwei Grundtatsachen enthalten: 1. es ist uns darin zweierlei Sein gegeben, welchen Seinsgegensatz wir als sinnliches und geistiges, dingliches und ideelles Sein bezeich­nen.» Und  §19: «Was räumlich-zeitliches Dasein hat, exi­stiert als etwas Materielles; was Grund alles Daseinspro­zesses und Subjekt des Lebens ist, das existiert ideell, ist real als ein Ideell-Seiendes.»Solche Erwägungen gehören nicht in die Erkenntnistheorie, sondern in die Metaphysik, die erst mit Hilfe der Erkenntnistheorie begründet werden kann. Zugegeben werden muß, daß Biedermanns Behaup­tungen den unseren vielfach ähnlich sind; unsere Methode aber berührt sich mit der seinigen durchaus nicht. Daher fanden wir auch nirgends Veranlassung, uns direkt mit ihm auseinanderzusetzen. Biedermann sucht mit Hilfe eini­ger metaphysischer Axiome einen erkenntnistheoretischen Standpunkt zu gewinnen. Wir suchen durch Betrachtung des Erkenntnisprozesses zu einer Ansicht über die Wirk­lichkeit zu kommen.",
      "Und wir glauben in der Tat gezeigt zu haben, daß aller Streit der Weltanschauungen daher kommt, daß man ein Wissen über ein Objektives (Ding, Ich, Bewußtsein usw.) zu erwerben trachtet, ohne vorher dasjenige genau zu ken­nen, was allein erst über alles andere Wissen Aufschluß geben kann: die Natur des Wissens selbst."
    ],
    "sentences": [
      [
        "VII.",
        "ERKENNTNISTHEORETISCHE SCHLUSSBETRACHTUNG"
      ],
      [
        "Wir haben die Erkenntnistheorie begründet als die Wissenschaft von der Bedeutung alles menschlichen Wissens.",
        "Durch sie erst verschaffen wir uns Aufklärung über das Verhältnis des Inhaltes der einzelnen Wissenschaften zur Welt.",
        "Sie macht es uns möglich, mit Hilfe der Wissenschaften zur Weltanschauung zu kommen.",
        "Positives Wissen erwerben wir durch die einzelnen Erkenntnisse; den Wert des Wissens für die Wirklichkeit erfahren wir durch die Erkenntnis­theorie.",
        "Dadurch, daß wir streng an diesem Grundsatze festgehalten haben und keinerlei Einzelwissen in unseren Auseinandersetzungen verwertet haben, dadurch haben wir alle einseitigen Weltanschauungen überwunden.",
        "Die Ein­seitigkeit entspringt gewöhnlich daher, daß die Unter­suchung, statt sich an den Erkenntnisprozeß selbst zu ma­chen, sogleich an irgendwelche Objekte dieses Prozesses herantritt.",
        "Nach unseren Auseinandersetzungen muß der Dogmatismus sein «Ding an sich », der subjektive Idealismus sein «Ich»als Urprinzip fallen lassen, denn diese sind ihrem gegenseitigen Verhältnis nach wesentlich erst im Denken bestimmt.",
        "«Ding an sich»und «Ich»sind nicht so zu bestimmen, daß man das eine von dem anderen ableitet, sondern beide müssen vom Denken aus nach ihrem Charak­ter und Verhältnis bestimmt werden.",
        "Der Skeptizismus muß von seinem Zweifel an der Erkennbarkeit der Welt ablassen, denn an dem «Gegebenen»ist nichts zu bezweifeln, weil es von allen durch das Erkennen erteilten Prä­dikaten"
      ],
      [
        "noch unberührt ist.",
        "Wollte er aber behaupten, daß das denkende Erkennen nie an die Dinge herankommen könne, so könnte er das nur durch denkende Überlegung selbst tun, womit er sich aber auch selbst widerlegt.",
        "Denn wer durch Denken den Zweifel begründen will, der gibt implizite zu, daß dem Denken eine für das Stützen einer Überzeugung hinreichende Kraft zukommt.",
        "Unsere Er­kenntnistheorie, endlich, überwindet den einseitigen Em­pirismus und den einseitigen Rationalismus, indem sie beide auf einer höheren Stufe vereinigt.",
        "Auf diese Weise wird sie beiden gerecht.",
        "Dem Empiriker werden wir gerecht, indem wir zeigen, daß alle inhaltlichen Erkenntnisse über das Ge­gebene nur in unmittelbarer Berührung mit diesem selbst erlangt werden können.",
        "Auch der Rationalist findet bei un­seren Auseinandersetzungen seine Rechnung, da wir das Denken für den notwendigen und einzigen Vermittler des Erkennens erklären."
      ],
      [
        "Am nächsten berührt sich unsere Weltanschauung, wie wir sie erkenntnistheoretisch begründet haben, mit der von A.",
        "Biedermann vertretenen*.",
        "Aber Biedermann braucht zur Begründung seines Standpunktes Feststellungen, die durchaus nicht in die Erkenntnistheorie gehören.",
        "So operiert er mit den Begriffen: Sein, Substanz, Raum, Zeit usw., ohne vorher den Erkenntnisprozeß für sich untersucht zu haben.",
        "Statt festzustellen, daß im Erkenntnisprozeß zu­nächst nur die beiden Elemente Gegebenes und Denken vorhanden sind, spricht er von Seinsweisen der Wirklichkeit."
      ],
      [
        "-084-*Christliche Dogmatik.",
        "Die erkenntnistheoretischen Untersuchun­gen im 1.",
        "Band.",
        "Eine erschöpfende Auseinandersetzung über diesen Standpunkt hat Eduard von Hartmann geliefert, siehe «Kritische Wanderungen durch die Philosophie der Gegenwart» S.200 ff."
      ],
      [
        "So sagt er z.",
        "B. § 15: «In allem Bewußtseinsinhalt sind zwei Grundtatsachen enthalten: 1. es ist uns darin zweierlei Sein gegeben, welchen Seinsgegensatz wir als sinnliches und geistiges, dingliches und ideelles Sein bezeich­nen.» Und §19: «Was räumlich-zeitliches Dasein hat, exi­stiert als etwas Materielles; was Grund alles Daseinspro­zesses und Subjekt des Lebens ist, das existiert ideell, ist real als ein Ideell-Seiendes.»Solche Erwägungen gehören nicht in die Erkenntnistheorie, sondern in die Metaphysik, die erst mit Hilfe der Erkenntnistheorie begründet werden kann.",
        "Zugegeben werden muß, daß Biedermanns Behaup­tungen den unseren vielfach ähnlich sind; unsere Methode aber berührt sich mit der seinigen durchaus nicht.",
        "Daher fanden wir auch nirgends Veranlassung, uns direkt mit ihm auseinanderzusetzen.",
        "Biedermann sucht mit Hilfe eini­ger metaphysischer Axiome einen erkenntnistheoretischen Standpunkt zu gewinnen.",
        "Wir suchen durch Betrachtung des Erkenntnisprozesses zu einer Ansicht über die Wirk­lichkeit zu kommen."
      ],
      [
        "Und wir glauben in der Tat gezeigt zu haben, daß aller Streit der Weltanschauungen daher kommt, daß man ein Wissen über ein Objektives (Ding, Ich, Bewußtsein usw.) zu erwerben trachtet, ohne vorher dasjenige genau zu ken­nen, was allein erst über alles andere Wissen Aufschluß geben kann: die Natur des Wissens selbst."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "VIII. PRAKTISCHE SCHLUSSBETRACHTUNG",
    "paragraphs": [
      "Wahrheit und Wissenschaft",
      "VIII. PRAKTISCHE SCHLUSSBETRACHTUNG",
      "Die Stellung unserer erkennenden Persönlichkeit zum ob­jektiven Weltwesen war es, worüber wir durch die vorhergehenden Betrachtungen Aufschluß verlangten. Was be­deutet für uns der Besitz von Erkenntnis und Wissenschaft? Das war die Frage, nach deren Beantwortung wir suchten. Wir haben gesehen, daß sich in userem Wissen der in­nerste Kern der Welt auslebt. Die gesetzmäßige Harmonie, von der das Weltall beherrscht wird, kommt in der mensch­lichen Erkenntnis zur Erscheinung.",
      "Es gehört somit zum Berufe des Menschen, die Grund­gesetze der Welt, die sonst zwar alles Dasein beherrschen, aber nie selbst zum Dasein kommen würden, in das Gebiet der erscheinenden Wirklichkeit zu versetzen. Das ist das Wesen des Wissens, daß sich in ihm der in der objektiven Realität nie aufzufindende Weltengrund darstellt. Unser Erkennen ist - bildlich gesprochen - ein stetiges Hineinleben in den Weltengrund.",
      "Eine solche Überzeugung muß auch Licht auf unsere prak­tische Lebensauffassung werfen.",
      "Unsere Lebensführung ist ihrem ganzen Charakter nach bestimmt durch unsere sittlichen Ideale. Diese sind die Ideen, die wir von unseren Aufgaben im Leben haben, oder mit anderen Worten, die wir von dem machen, was wir durch unser Handeln vollbringen sollen.",
      "Unser Handeln ist ein Teil des allgemeinen Weltgesche­hens. Es steht somit auch unter der allgemeinen Gesetz­mäßigkeit dieses Geschehens.",
      "Wenn nun irgendwo im Universum ein Geschehen auftritt, so ist an demselben ein Zweifaches zu unterscheiden: der äußere Verlauf desselben in Raum und Zeit und die innere Gesetzmäßigkeit davon.",
      "Die Erkenntnis dieser Gesetzmäßigkeit für das mensch­liche Handeln ist nur ein besonderer Fall des Erkennens. Die von uns über die Natur der Erkenntnis abgeleiteten Anschauungen müssen also auch hier anwendbar sein.",
      "Sich als handelnde Persönlichkeit erkennen heißt somit: für sein Handeln die entsprechenden Gesetze, d.h. die sittlichen Begriffe und Ideale als Wissen zu besitzen. Wenn wir diese Gesetzmäßigkeit erkannt haben, dann ist unser Handeln auch unser Werk.",
      "Die Gesetzmäßigkeit ist dann nicht als etwas gegeben, was außerhalb des Objektes liegt, an dem das Geschehen erscheint, sondern als der Inhalt des in lebendigem Tun begriffenen Objektes selbst. Das Objekt ist in diesem Falle unser eigenes Ich.",
      "Hat dies letztere sein Handeln dem Wesen nach wirklich erkennend durchdrun­gen, dann fühlt es sich zugleich als den Beherrscher des­selben. Solange ein solches nicht stattfindet, stehen die Gesetze des Handelns uns als etwas Fremdes gegenüber, sie beherrschen uns; was wir vollbringen, steht unter dem Zwange, den sie auf uns ausüben.",
      "Sind sie aus solcher frem­den Wesenheit in das ureigene Tun unseres Ich verwandelt, dann hört dieser Zwang auf. Das Zwingende ist unser eigenes Wesen geworden. Die Gesetzmäßigkeit herrscht nicht mehr über uns, sondern in uns über das von unserm Ich ausgehende Geschehen.",
      "Die Verwirklichung eines Geschehens vermöge einer außer dem Verwirklicher stehenden Gesetzmäßigkeit ist ein Akt der Unfreiheit, jene durch den Verwirklicher selbst ein solcher der Freiheit. Die Gesetze",
      "seines Handelns erkennen heißt sich seiner Freiheit bewußt sein. Der Erkenntnisprozeß ist, nach unseren Ausführun­gen, der Entwicklungsprozeß zur Freiheit.",
      "Nicht alles menschliche Handeln trägt diesen Charakter. In vielen Fällen besitzen wir die Gesetze für unser Han­deln nicht als Wissen. Dieser Teil unseres Handelns ist der unfreie Teil unseres Wirkens. Ihm gegenüber steht derjenige, wo wir uns in diese Gesetze vollkommen einleben. Das ist das freie Gebiet. Sofern unser Leben ihm angehört, ist es allein als sittliches zu bezeichnen. Die Verwandlung des ersten Gebietes in ein solches mit dem Charakter des zwei­ten ist die Aufgabe jeder individuellen Entwicklung, wie auch jener der ganzen Menschheit.",
      "Das wichtigste Problem alles menschlichen Denkens ist das: den Menschen als auf sich selbst gegründete, freie Per­sönlichkeit zu begreifen."
    ],
    "sentences": [
      [
        "Wahrheit und Wissenschaft"
      ],
      [
        "VIII.",
        "PRAKTISCHE SCHLUSSBETRACHTUNG"
      ],
      [
        "Die Stellung unserer erkennenden Persönlichkeit zum ob­jektiven Weltwesen war es, worüber wir durch die vorhergehenden Betrachtungen Aufschluß verlangten.",
        "Was be­deutet für uns der Besitz von Erkenntnis und Wissenschaft?",
        "Das war die Frage, nach deren Beantwortung wir suchten.",
        "Wir haben gesehen, daß sich in userem Wissen der in­nerste Kern der Welt auslebt.",
        "Die gesetzmäßige Harmonie, von der das Weltall beherrscht wird, kommt in der mensch­lichen Erkenntnis zur Erscheinung."
      ],
      [
        "Es gehört somit zum Berufe des Menschen, die Grund­gesetze der Welt, die sonst zwar alles Dasein beherrschen, aber nie selbst zum Dasein kommen würden, in das Gebiet der erscheinenden Wirklichkeit zu versetzen.",
        "Das ist das Wesen des Wissens, daß sich in ihm der in der objektiven Realität nie aufzufindende Weltengrund darstellt.",
        "Unser Erkennen ist - bildlich gesprochen - ein stetiges Hineinleben in den Weltengrund."
      ],
      [
        "Eine solche Überzeugung muß auch Licht auf unsere prak­tische Lebensauffassung werfen."
      ],
      [
        "Unsere Lebensführung ist ihrem ganzen Charakter nach bestimmt durch unsere sittlichen Ideale.",
        "Diese sind die Ideen, die wir von unseren Aufgaben im Leben haben, oder mit anderen Worten, die wir von dem machen, was wir durch unser Handeln vollbringen sollen."
      ],
      [
        "Unser Handeln ist ein Teil des allgemeinen Weltgesche­hens.",
        "Es steht somit auch unter der allgemeinen Gesetz­mäßigkeit dieses Geschehens."
      ],
      [
        "Wenn nun irgendwo im Universum ein Geschehen auftritt, so ist an demselben ein Zweifaches zu unterscheiden: der äußere Verlauf desselben in Raum und Zeit und die innere Gesetzmäßigkeit davon."
      ],
      [
        "Die Erkenntnis dieser Gesetzmäßigkeit für das mensch­liche Handeln ist nur ein besonderer Fall des Erkennens.",
        "Die von uns über die Natur der Erkenntnis abgeleiteten Anschauungen müssen also auch hier anwendbar sein."
      ],
      [
        "Sich als handelnde Persönlichkeit erkennen heißt somit: für sein Handeln die entsprechenden Gesetze, d.h. die sittlichen Begriffe und Ideale als Wissen zu besitzen.",
        "Wenn wir diese Gesetzmäßigkeit erkannt haben, dann ist unser Handeln auch unser Werk."
      ],
      [
        "Die Gesetzmäßigkeit ist dann nicht als etwas gegeben, was außerhalb des Objektes liegt, an dem das Geschehen erscheint, sondern als der Inhalt des in lebendigem Tun begriffenen Objektes selbst.",
        "Das Objekt ist in diesem Falle unser eigenes Ich."
      ],
      [
        "Hat dies letztere sein Handeln dem Wesen nach wirklich erkennend durchdrun­gen, dann fühlt es sich zugleich als den Beherrscher des­selben.",
        "Solange ein solches nicht stattfindet, stehen die Gesetze des Handelns uns als etwas Fremdes gegenüber, sie beherrschen uns; was wir vollbringen, steht unter dem Zwange, den sie auf uns ausüben."
      ],
      [
        "Sind sie aus solcher frem­den Wesenheit in das ureigene Tun unseres Ich verwandelt, dann hört dieser Zwang auf.",
        "Das Zwingende ist unser eigenes Wesen geworden.",
        "Die Gesetzmäßigkeit herrscht nicht mehr über uns, sondern in uns über das von unserm Ich ausgehende Geschehen."
      ],
      [
        "Die Verwirklichung eines Geschehens vermöge einer außer dem Verwirklicher stehenden Gesetzmäßigkeit ist ein Akt der Unfreiheit, jene durch den Verwirklicher selbst ein solcher der Freiheit.",
        "Die Gesetze"
      ],
      [
        "seines Handelns erkennen heißt sich seiner Freiheit bewußt sein.",
        "Der Erkenntnisprozeß ist, nach unseren Ausführun­gen, der Entwicklungsprozeß zur Freiheit."
      ],
      [
        "Nicht alles menschliche Handeln trägt diesen Charakter.",
        "In vielen Fällen besitzen wir die Gesetze für unser Han­deln nicht als Wissen.",
        "Dieser Teil unseres Handelns ist der unfreie Teil unseres Wirkens.",
        "Ihm gegenüber steht derjenige, wo wir uns in diese Gesetze vollkommen einleben.",
        "Das ist das freie Gebiet.",
        "Sofern unser Leben ihm angehört, ist es allein als sittliches zu bezeichnen.",
        "Die Verwandlung des ersten Gebietes in ein solches mit dem Charakter des zwei­ten ist die Aufgabe jeder individuellen Entwicklung, wie auch jener der ganzen Menschheit."
      ],
      [
        "Das wichtigste Problem alles menschlichen Denkens ist das: den Menschen als auf sich selbst gegründete, freie Per­sönlichkeit zu begreifen."
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
