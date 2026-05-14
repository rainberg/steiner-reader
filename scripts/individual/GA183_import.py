#!/usr/bin/env python3
"""Standalone import script for GA183 — GA183 - Die Wissenschaft vom Werden des Menschen"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA183 - Die Wissenschaft vom Werden des Menschen"""
GA_NUMBER = "GA183"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG Dornach, 17. August 1918",
    "paragraphs": [
      "Daß es mir die tiefste Befriedigung gewährt, die Arbeit in Ihrer Mitte an diesem unserem Bau und um unseren Bau herum hier wiederum aufnehmen zu können, das werden Sie mir wohl ohne weiteres glau­ben. Es ist ja tatsächlich so, daß heute nicht nur bei tieferem Nach­denken, sondern, man darf sagen, schon bei oberflächlicherem Nach­denken demjenigen, der der ganzen Aura dieses Baues nahegetreten ist, der Gedanke aufgehen könnte, daß mit diesem Bau doch etwas verknüpft ist, was mit den bedeutungsvollsten, schwerwiegendsten Aufgaben der Menschenzukunft zusammenhängt. Und nach längerer, erzwungener Abwesenheit ist es ja selbstverständiich, daß man sich mit tiefster Befriedigung wiederum an der Stätte befindet, an der dieser Bau als ein Symbolum unserer Sache steht.",
      "Zu dem Gesagten darf ich wohl hinzufügen, daß für mich besonders jedesmal, wenn ich jetzt nach längerer Abwesenheit wieder komme, die tiefste Befriedigung daraus resultiert, daß ich ja immer dann sehen kann, wie schön und wie bedeutungsvoll die Arbeit an diesem Bau durch die hingebungsvolle Tätigkeit der am Bau Arbeitenden weiter gefördert worden ist. Insbesondere in diesen Monaten meiner letzten Abwesenheit, wo ja unter so schwierigen Verhältnissen gearbeitet worden ist, ist ja gerade ein Teil der künstlerischen Arbeit in einer unvergleichlichen Weise fortgeschritten, fortgeschritten in dem Geiste, der dieses Ganze durchdringen soll.",
      "Aber auch mit tiefer Befriedigung sehe ich bei Verfolgung des Geistes unserer Arbeit, bei Verfolgung desjenigen, was hier entsteht, das Verbundensein treuer Gesinnung bei vielen unserer Freunde, treuer Gesinnung gegenüber dem, was sich gerade in diesem Bau ver­körpert. Und dasjenige, was dann beim Wieder auf sich wirken ­Lassen dieser Sache der Seele sich offenbart, das ist doch, daß hier eine Stätte vorhanden ist, mit welcher verbunden ist eine solche treue Gesinnung einer Anzahl von Freunden unserer geistigen Bewegung, einer solch treuen Gesinnung, die da verspricht, daß sich die besten",
      "Impulse unserer geistigen Bewegung in die Zukunft der Menschheit hinein halten werden, der sie so notwendig sein werden. Es gibt schon innerhalb gerade der diesem Bau gewidmeten Arbeit etwas, was Vor­bild sein könnte für dasjenige, was im allgemeinen mit dem, was sich unter uns heute Anthroposophlsche Gesellschaft nennt, eigentlich gewollt ist.",
      "Aber ich habe auf der andern Seite vielfach wiederum das Gefühl, daß das Günstige, das bedeutungsvoll Gute, das man hier im Zusam­menwirken von Menschenarbeit und Menschengefühl mit diesem Bau finden kann, gerade darinnen besteht, daß dieser Bau etwas ist, was gewissermaßen in seiner Objektivität das, was durch unsere Bewegung gewollt wird, loslöst von den subjektiven Interessen der einzelnen Menschen.",
      "Über dieses jetzt eben Berührte waren ja - und sind - in allen ähn­lichen Gesellschaften, auch in der Anthroposophischen Gesellschaft, gewisse merkwürdige Anschauungen vorhanden, die eigentlich nichts anderes sind als merkwürdige Illusionen. Man predigt viel von Selbst-losigkeit, von allgemeiner Menschenliebe; aber das sind oftmals bloße Masken für gewisse, nur raffinierte egoistische Interessen der einzel­nen Menschen. Gewiß, die einzelnen Menschen wissen nicht, daß es sich für sie um bloße egoistische Interessen handelt, sie sind vor ihrem eigenen Bewußtsein gewissermaßen unschuldig; aber es ist doch so. Der Bau selbst verlangt aber von einer schon ziemlich großen Anzahl unserer Freunde eine selbstlose Hingabe an etwas Objektives, an etwas, was als ein von jeder einzelnen Persönlichkeit losgelöstes Symbolum unserer Sache dasteht. Und insoferne wird wohl dasjenige, was mit diesem Bau zusammenhängt, vorbildlich sein können für das, was unsere Bewegung will.",
      "Meine lieben Freunde, wenn wir uns so wie heute wiederum be­grüßen, da dürfen wir insbesondere die Blicke richten auf das Frucht­bare und Umfassende dieser unserer geistigen Bewegung, und wir dürfen bei einer solchen Begrüßung bedenken, daß es uns ernst sein kann mit dem Glauben: Wie es auch immer geschehen mag - das Wie, das kann ja noch so oder so, je nach den Verhältnissen sich abspielen -, aus der furchtbaren Sackgasse, in welche die Menschheit hineingeraten",
      "ist in der Gegenwart, wird sie nicht früher herauskommen, als bis sie sich entschließt, in irgendeiner Weise Anknüpfungspunkte zu suchen für fruchtbares Wirken, fruchtbares Tun innerhalb einer solchen gei­stigen Bewegung, wie es die unsrige ist. Wir werden ja ganz gewiß nicht in egoistischer Weise darauf bestehen, die Wahrheit gerade nur innerhalb unseres engen, beschränkten Kreises zu haben; aber wir dürfen uns in einem Kreise zusammengehörig wissen, welcher er­kennt, daß die Menscheit wegen des Vernachlässigens ihrer Geistes-substanz sich in diese furchtbare Lage der Gegenwart gebracht hat. Wissen können wir uns als solche Menschen, die vereint sind mit jenen Ideen, die einzig und allein hinausführen können aus der Sack-gasse, in welche die Menschheit gekommen ist.",
      "Es ist ja in den Seelen der heutigen Menschen ungemein vieles un­geklärt. Wenn man wiederum da und dort sich hat unterrichten kön­nen über die Bedürfnisse, die obwalten nach unserer geistigen Bewe­gung, so kann man auf der einen Seite sagen: Ja, es sind doch die Seelen derjenigen, die da dürsten nach jenem spirituellen Leben, das wir meinen, der Zahl nach in starker Zunahme begriffen.",
      "Die Sehn­sucht nach solchem spirituellem Leben, sie hat sich, das darf wohl ge­sagt werden, ungeheuer vergrößert. Die Aufmerksamkeit, welche entgegengebracht wird unseren Impulsen, sie ist unstreitig in den letzten Jahren auch eine größere geworden, wenigstens auf den Ge­bieten, die mit in äußerlicher Weise in diesen letzten Jahren und ins­besondere in den letzten Monaten zugänglich waren.",
      "Auch das wird nicht ganz bedeutungslos sein, zu bemerken, daß eine solche Ver­größerung und Verstärkung dieser Sehnsucht der Menschenseelen nach dem spirituellen Leben ganz deutlich vorhanden ist. Allerdings steht dieser Verstärkung und Verschärfung der Sehnsucht nach dem spirituellen Leben das andere gegenüber: jene furchtbare Beirrung, unter welcher der weitaus größte Teil der Menschheit leidet, jene furchtbare Beirrung, welche durch die altüberkommenen Ideen, oder man könnte besser sagen, durch die altüberkommene Ideenlosigkeit innerhalb der Menschheit bewirkt wird, die, man möchte sagen, Be­quemlichkeit gegenüber jedem starken, jedem scharfen Gedanken, jene Bequemlichkeit, die einfach herrührt aus der Laxheit, aus der",
      "Trägheit, mit der das Gedankenleben seit vielen Jahrzehnten über die Erde hin geführt worden ist. Diese Laxheit, diese Trägheit beirrt die Seelen in dem vorhandenen Sehnen nach dem spirituellen Leben. Auf der einen Seite stecken die Menschen drinnen in einer wirklichen Sehn­sucht nach Geistigkeit, nach übersinnlichen, starken Impulsen. Auf der andern Seite werden die Seelen niedergehalten von all jenen alten Mächten, die nicht abtreten mögen vom Schauplatz des Menschen-wirkens und die doch sehen könnten aus dem, wie weit sie es gebracht haben, daß sie nicht mehr auf diesen Schauplatz des Menschenwirkens gehören. Man möchte sagen, daß man diesen dunkeln Eindruck, diesen zwiespältigen Eindruck überall hat.",
      "Ich habe ja unter unseren Mitgliedern an manchen Orten, in Ham­burg, in Berlin, in München, vielfach, in Anknüpfung an durch Licht-bilder wiedergegebene Darstellungen, von unserer Gruppe gespro­chen, die an der Hauptstelle unseres Baues stehen soll. Man konnte auf der einen Seite sehen, wie tatsächlich mächtige Impulse in die Seelen auch derjenigen hlneingehen, die durch die Verhältnisse der letzten Jahre niemals einen Blick werfen konnten auf das, was hier geschieht. Ein neues Menschenverständnis geht schon aus von derArt und Weise, wie das Ahrimanisch-Luziferische mit dem Christlichen zusammen gedacht wird und dargestellt, geoffenbart wird durch unsere Gruppe. Es ergreift die Seelen, wenn das, was durch diese Dinge gegeben wird, an diese Seelen herantritt. Allein, auf der andern Seite zeigen sich über­all die hemmenden Einflüsse dessen, was als Überbleibsel des Alten, Verfaulten am sogenannten Kulturleben sich über die Menschheit verbreitet.",
      "Das hat man ja insbesondere sehen können an der, man darf wahr­haftig im tiefsten Sinne sagen, humoristischen Art, wie den Vorträgen begegnet wurde, die ich im Kunsthause unseres Freundes, des Herrn von Bernus in München gehalten habe, worinnen ich versuchte, die inneren Impulse unserer hier betätigten Kunstanschauung einem größeren Publikum nahezubringen. Ja, Interesse hat das bei den Leu­ten außerordentlich viel erregt, denn ich habe im Februar und im Mai solche Vorträge in München gehalten, und ich mußte jeden dieser Vorträge zweimal halten; Herr von Bernus aber versicherte mir, es",
      "wären so viel Anfragen da, daß ich jeden dieser Vorträge vor einem öffentlichen Publikum, worin ich die Prinzipien meiner Kunstan­schauung, wie sie hier in dem Bau zutage treten, dargelegt habe, hätte viermal halten können. Interesse war schon da. Aber da, wo man selbstverständlich unfroh sein würde, wenn Zustimmung vorhanden wäre, bei der Münchner Zeitungskritik, da war, man kann schon sa­gen, in edelstem Sinne humoristisches Zähnefletschen da. Es war ins­besondere humoristisch, weil der innere Groll gegen etwas, was man gar nicht verstehen konnte, sich da so geltend machte: Es war alles solch - nicht gesprochenes, sondern gespieenes Zeug! Verzeihen Sie den harten Ausdruck. Und es zeigte sich gerade an dem Interesse, das der Sache entgegengebracht wurde, worinnen Ehrlichkeit und Auf­richtigkeit sich aussprach, im Gegensatze zu dem, was aus diesem Kunstmittelpunkte sonst sich zeigte - das ist ja München selbstver-ständlich, nicht wahr, das ist ja bekannt -, es zeigte sich also, wie in diesem Kunstmittelpunkte sowohl das verständigste als auch das un­verständigste Zeug geredet wurde. Gerade an dieser Diskrepanz zeigte sich an einem Beispiel, wie diese zwei Strömungen, von denen ich Ihnen sprach, in der Gegenwart vorhanden sind; wie wir wirklich uns bewußt sein dürfen, in etwas ganz Wesentlichem und Wichtigem drinnenzustehen, das für die Welt, für die Zukunft zu erkämpfen ist.",
      "Ich sage das alles sicher nicht deshalb, weil ich irgendwie anstreben würde, wenn die Dinge in die Öffentlichkeit treten, wie man sagt, eine «gute Presse» zu bekommen; denn ich würde in dem Augenblicke, wo eine «gute Presse» auftritt, glauben: Da muß selbstverständlich irgend etwas nicht richtig sein, da muß irgend etwas Falsches auf unserer Seite geschehen sein.",
      "Alle diese Dinge sind ja geeignet, in uns das Bewußtsein hervorzu­rufen, daß wir gar sehr nötig haben, mit aller Entschiedenheit auf dem Boden unserer Sache zu stehen. Denn nichts könnte uns in schimmere Verwirrung hineinführen, als wenn wir irgendwelche Kompromisse schließen wollten mit dem, wovon die Außenwelt meint, daß es das Richtige wäre für uns. Nur in den Prinzipien unserer Sache selbst müssen wir dasjenige finden, was uns die Richtung für unser Tun angibt.",
      "Auch für so etwas, das mehr nuttelbar mit unserer Sache zusammen­hängt, aber doch innerlich zusammenhängt, auch für die Eurythmie hat sich ja in der letzten Zeit ein immer steigendes Interesse an den verschiedensten Orten gezeigt. Und wenn wir, die wir da waren, uns erinnern, wie zum Beispiel gerade die Eurythmie in einem Orte auf­genommen worden ist, wo sie fast noch gar nicht gesehen worden ist, wo sie zum Teil sogar etwas Neues war für diejenigen, die sie gesehen haben, in Hamburg, so muß man sich wirklich an die Art, wie da die Sache aufgenommen wurde, mit einer tiefen Befriedigung erinnern.",
      "Gerade in Hamburg konnte man sehen, wie bedeutungsvoll die Im­pulse sind, die auch von einer solchen Sache ausgehen können. Und da waren Leute, die eigentlich im Grunde zum erstenmal so recht einen eurythmischen Wurf gesehen haben.",
      "Und es wird vielleicht auch für die Eurythmie die Möglichkeit kommen, mit ihr in die Öffentlich­keit einzutreten. Aber gerade dann mussen wir mit solch einer Sache auf dem allerfestesten Boden stehen, nichts anderes tun, als was ledig­lich aus unserer Sache selbst heraus folgt.",
      "Sonst würde sich sehr bald zeigen, daß von einem gewissen Punkte ab niemand glauben darf, daß ich in einer gewissen Sache, wenn es auf mich selbst ankommt, bieg­sam bin. Die meisten von Ihnen wissen schon, daß ich selbstverständ­lich überall da, wo es nicht auf etwas Prinzipielles ankommt, sondern wo es darauf ankommt, menschlich zu sein, das Menschliche in den Vordergrund zu stellen, in jeder Weise mit allen Menschen mitgehe -aber wo es an die Grenze kommt, daß auch nur im geringsten irgend etwas Prinzipielles verleugnet werden müßte, da würde ich mich nicht als biegsam erweisen.",
      "Wenn also in der jetzigen Zeit, wo so vieles an Tänzerei gesehen werden kann - denn überall wird ja getanzt, das ist ja ganz schrecklich, man könnte an jedem Abend, wenn man in einer größeren Stadt wohnt, einen Tanzabend mitmachen, wo überall schaugetanzt wird -, wenn man da glauben würde, und ich sage diese Sache nicht so ohne Begründung, obwohl ich auf nichts Konkretes hinweise, daß, wenn diese unsere Eurvthmie jetzt vor die Öffentlich­keit treten würde, wir irgendwie uns binden sollten an eine journa­listische Verständnislosigkeit, die irgendwelche Anforderungen stellte, so würde ich mich in der ganz entschiedensten Weise dagegen verwahren.",
      "Dasjenige, was Geschmacksrichtung ist, was Geschmacks­tendenz ist, muß lediglich aus unserer Sache selbst hervorgehen.",
      "Wir müssen uns manchmal auch erinnern, insbesondere wenn wir uns wieder begrüßen, an das aus dem Willen folgende, notwendige, geradiinige Sich-Bewegen nach Maßgabe unserer spirituellen Impulse. Diese spirituellen Impulse werden ja gegen manches zu kämpfen ha­ben.",
      "Man kann heute nicht mehr bloß sagen Vorurteil, denn die Dinge wirken zu stark, als daß man sie mit dem schwachen Wort Vorurteil belegen könnte; diese Impulse, die werden gegen mancherlei zu kämp­fen haben. Immer wieder und wiederum muß ja hingewiesen werden auf die große Krankheit unserer Zeit, welche in der Zügellosigkeit gegenüber dem Gedankenieben besteht.",
      "Denn das Gedankenleben ist schon ein spirituelles Leben, wenn man es richtig erfaßt. Und weil die Menscheit so wenig sich an das Gedankenleben halten will, findet sie so wenig den Weg in spirituelle Welten hinein.",
      "Und ich muß schon von der verschiedensten Seite immer wieder und wieder eines berüh­ren: Man hält heute furchtbar viel von dem bloßen Inhalt der Gedan­ken. Aber der Inhalt der Gedanken ist an den Gedanken das am aller­wenigsten Wichtige.",
      "Nicht wahr, ein Weizenkorn ist ein Weizenkorn; es läßt sich nicht bestreiten. Aber mag ein Weizenkorn auch ein Wei­zenkorn sein: Wenn Sie ein Weizenkorn in einen guten, fruchtbaren Weizenboden hineinsenken, so bekommen Sie eine saftige Weizen­ähre daraus; wenn Sie ein Weizenkorn in einen ganz unfruchtbaren, steinigen Boden hineinsenken, bekommen Sie entweder gar nichts oder eine sehr korrupte Weizenähre.",
      "Jedesmal haben Sie es mit einem Weizenkorn zu tun.",
      "Sagen wir jetzt etwas anderes statt Weizenkorn. Sagen wir statt Weizenkorn «Idee der freien Menschheit», von der ja heute so viel gesprochen wird; «Idee der freien Menschheit» ist «Idee der freien Menscheit», wird mancher sagen. Das ist geradeso wie: Weizenkorn ist Weizenkorn. Es ist ein Unterschied, ob «Idee der freien Mensch­heit» in einem Herzen, in einer Seele gedeiht - ganz genau dieselbe Idee mit derselben Begründung -, wo dieses Herz und diese Seele fruchtbarer Boden ist, oder ob die «Idee der freien Menschheit» in Woodrow Wilsons Kopf gedeiht! So wenig wie ein Weizenkorn gedeihen",
      "kann, wenn es in einen steinigen Boden oder gar in den Felsen hineingesenkt wird, so bedeuten all die sogenannten schönen Ideen, die in den Programmen Woodrow Wilsons vorkommen, nichts, wenn sie aus diesem Kopfe kommen. Allein dies ist etwas, was der gegen­wärtigen Menschheit so unendlich schwer wird einzusehen, weil die gegenwärtige Menschheit eben der Anschauung ist: Man hält sich an den Inhalt von Programmen, an den Inhalt von Ideen. Aber der Inhalt von Programmen, der Inhalt von Ideen, der hat ebensowenig eine Bedeutung, als die Keimkraft eines Weizenkorns eine Bedeutung hat, bevor dieses Weizenkorn in einen gerade für es fruchtbaren Weizen­boden gesenkt wird.",
      "Real denken, das ist dasjenige, was der Menschheit so ungeheuer not tut. Und mit dem Unrealdenken der Gegenwart hängt etwas anderes zusammen, hängt zusammen, daß die Menschheit fast von allen Er­eignis sen überrascht wird. Man kann schon die Frage aufwerfen: Von was ist denn die Menschheit nicht überrascht worden in den letzten Jahren? - Von allem ist sie überrascht worden, und sie wird weiter noch viel mehr überrascht werden, als sie überrascht ist. Aber die Menschheit läßt sich ja nicht irgendwie auf dasjenige ein, was wirksam ist in der Welt. Daher ist es auch heute unmöglich, für irgendeine Sache die Menschheit zu irgendeiner Voraussicht zu bringen.",
      "Wenn man mit bloßen Ideen arbeitet, dann kann man von allen Seiten alles durch alles begründen. Wenn man mit dem bloßen Inhalt von Ideen arbeitet, kann man wirklich alles mit allem begründen. Auch das ist etwas, was im Grunde genommen immer mehr und mehr und immer tiefer und tiefer eingesehen werden muß, was aber nicht einge­sehen werden will.",
      "Gewöhnlich wenn man von solchen Dingen spricht und dann Bei­spiele anführt, findet man keinen rechten Glauben, weil die Beispiele zu grotesk sich ausnehmen. Aber von solchen Dingen, die in so gro­tesken Beispielen zutage treten, ist unser ganzes gegenwärtiges Seelen- und Geistesleben durchschwirrt. Ich weiß, daß gar mancher vielleicht mit Groll zuhört, wenn ich Ihnen eine recht ausgefallene Idee als ein Beispiel anführe. Ich will eine ganz ausgefallene Idee anführen.",
      "Da ist ein Universitätsprofessor, ein alter, angesehener Universitäts­professor auf die Tatsache gestoßen, daß Goethe in seinem langen Leben Neigungen gehabt hat für verschiedene Frauen. Darauf ist also ein Universitätsprofessor gestoßen, der sich zur Aufgabe gemacht hat, Goethes Leben und das Leben der mit ihm zusammenhängenden Gei­ster gründlich zu studieren.",
      "Und siehe da, selbstverständlich hat er, trotzdem er nicht gerade ein europäischer Universitätsprofessor ist, es sich zur Aufgabe gemacht, bei diesen Studien so gründlich zu Werke zu gehen, wie sonst in der Regel nur mitteleuropäische Universitäts­professoren zu Werke gehen: er hat die ganze Galerie der Goetheschen Frauengestalten in ihrem Verhältnis zu Goethe an seiner Seele Revue passieren lassen. Und was hat er herausgefunden?",
      "Fast wörtlich kann ich es Ihnen anführen. Er hat herausgefunden: Was man über die je­weilig geliebte Frau in Goethes Leben sagen kann, das ist, daß jede für Goethe eine Art Belgien war, gegenüber welcher er die Neutralität verletzte, und dann darüber geseufzt hat, daß sein Herz blute, indem er über eine leuchtende Unschuld herfallen mußte.",
      "Aber er hat auch ticht vergessen, jedesmal wiederum wie der deutsche Kanzler zu be­haupten, daß das Gebiet der verletzten Neutralität ein besseres Schick­sal verdient haben würde, daß aber er, Goethe, nicht anders gekonnt habe, da seine Bestimmung, die Rechte seines geistigen Lebens ihn verpflichteten, die Geliebte zu opfern, ja den Schmerz seines eigenen Herzens zu opfern auf dem Altar der Pflicht, die er habe gegen sein eigenes unsterbliches Ich.",
      "Nun, aus diesem Buche könnte ich Ihnen noch manche ausgefallene Idee hier vorlegen. Sie würden sagen: Wozu das? - Aber es hat schon seine guten Gründe, denn derlei Ideen finden Sie heute überallhin über die Erde zerstreut. Sie sind so, die Ideen der heutigen Menschheit. Und nicht umsonst zeigen sich solche Ideen da, wo der Extrakt des menschlichen Denkens in der Literatur auftritt, denn diese Anschau­ung wird vertreten von San/qyana, dem Professor der Harvard-Univer­sität in Amerika, einem sehr angesehenen Spanier, der sich aber ganz amerikanisiert hat, dessen Buch während dieser Menschheitskatastro­phe geschrieben worden ist, und dessen französische Ausgabe einge­leitet worden ist von Boutroux> der kurz vor dem Kriege von Heidelberg",
      "aus eine große Lobrede über die deutsche Philosophie gehalten hat. Dieses Buch heißt: «L'erreur de la philosophie allemande», und ist wahrhaftig nicht ein Zufallsbuch, sondern es ist ganz charakte­ristisch für das Denken der Gegenwart, weil ja wirklich mit derselben Leichtigkeit, mit welcher der Professor Santayana die Verletzung der belgischen Neutralität mit den Taten Goethes gegenüber verschiede­nen Frauen vergleicht, diese Menschheit das Entferntliegendste zu­sammenhält. Denn diese Art des Denkens tritt Ihnen, wenn Sie wirk­lich beobachten können, auf allen Gebieten der sogenannten heutigen Wissenschaft entgegen.",
      "Es ist ja schon einmal die Aufgabe jener geistigen Impulse, denen unsere anthroposophisch orientierte Geisteswissenschaft gewidmet ist, gegen drei Grundübel in der gegenwärtigen sogenannten Mensch­heitskultur anzukämpfen. Sie kann gar nicht anders, als gegen diese drei Grundübel anzukämpfen. Das eine Grundübel zeigt sich auf dem Gebiete des Denkens, das andere auf dem Gebiete des Fühlens, und das dritte auf dem Gebiete des Wollens.",
      "Auf dem Gebiete des Denkens ist es allmählich dazu gekommen, daß die Menschen nur so denken können, wie dasjenige Denken verläuft, das eng an das physische Gehirn gebunden ist. Aber dieses Denken, das eng an das physische Gehirn gebunden ist, das sich nicht erheben will in freiem Aufschwung zum Spirituellen, das ist unter allen Umständen dazu verurteilt, borniert zu werden, beschränkt zu werden. Und das bedeutungsvollste Kennzeichen, namentlich des gegenwärtigen wis­senschaftlichen Denkens, ist die Borniertheit, ist die Beschränktheit. Gewiß, man kann auf dem Felde des Beschränkten, des Bornierten, Großartiges leisten. Das tut zum Beispiel die gegenwärtige Natur­wissenschaft. Aber zur Naturwissenschaft, wie sie heute gedacht wird, ist ja keine Genialität notwendig. Also: Borniertheit, Beschränktheit, das ist dasjenige, was namentlich auf intellektuellem Gebiete be­kämpft werden muß. Ich will heute mehr skizzieren, wir werden diese Dinge genauer besprechen.",
      "Auf dem Gebiete des Fühlens handelt es sich darum, daß die Mensch­heit allmählich zu einer gewissen Philistrosität gekommen ist - man kann das nicht anders nennen -, Engherzigkeit, Philistrosität, Eingeschränktheit",
      "auf gewisse engumgrenzte Kreise. Das ist ja das haupt-sächlichste Kennzeichen des Philisters, daß er sich nicht für große Weltenzusammenhänge interessieren kann. Kirchtumpolitiker sind immer Philister. Das kann natürlich auf dem Gebiete der Geisteswis­senschaft nicht genügen, denn da kann man sich nicht auf die engsten Kreise beschränken. Man muß sich sogar für das Außerirdische, man muß sich für sehr weite Kreise interessieren. Und die Leute ärgert es ja, wenn jemand auch nur vorgibt, für so weite Kreise, wie Mond, Sonne, Saturn, etwas wissen zu wollen. Aber die Philistrosität muß schon auf allen Gebieten der Nichtphilistrosität weichen, wenn Gei­steswissenschaft durchdringen soll. Das ist manchmal nicht bequem, denn das fordert rückhaltloses Sich-der-Sache-Gegenüberstellen, und ein mehr vorurteilsloses Sich-der-Sache-Gegenüberstellen.",
      "Da ist ja in der letzten Zeit einmal etwas recht Niedliches gerade auf unserem Boden passiert; aber ich habe vorgebeugt, es ist nichts Schlimmes passiert, es hätte nur etwas passieren können! Ich habe -Sie werden sich daran noch aus den vorjährigen Zürcher Vorträgen erinnern - unter den verschiedenen Beispielen, wie aus der Natur­wissenschaft selber eine Art Überwindung des Darwinismus heraus-wachsen kann, auf das ausgezeichnete Buch «Das Werden der Orga­nismen» von Oskar Hertwig hingewiesen. Ich habe hier und sonst überall, wo ich nur Gelegenheit gefunden habe, auf dieses ausgezeich­nete Buch hingewiesen. Nun erschien sehr bald nach diesem Buch ein kürzeres Buch, worin derselbe Oskar Hertwig über das soziale, das ethische und das politische Leben spricht, und ich hatte mir schon gedacht: Da kann passieren, daß einzelne unserer Mitglieder, wenn sie gehört haben, daß ich gesagt habe, das Buch von Oskar Hertwig «Das Werden der Organismen» sei ein ausgezeichnetes Buch, nun glauben, daß ich denselben Oskar Hertwig für eine unfehlbare Autorität an­sehe. Dieses Buch, das als zweites erschienen ist von Oskar Hertwig, ist ein Buch, das nichts taugt, ein Buch, das herrührt von einem Men­schen, der auf dem Gebiete, um das es sich da handelt, auf dem Ge­biete des sozialen, des ethischen, des politischen Lebens, absolut keinen einzigen ordentlichen Gedanken fassen kann. Ich fürchtete schon, daß einzelne unserer Mitglieder nun hätten finden können, daß auch dieses",
      "Buch irgendeinen Wert haben könnte, weil es von demselben Oskar Hertwig herrührt. So mußte ich denn vorbauen und habe auch über­all, wo ich bisher die Gelegenheit ergreifen konnte, sie ergriffen, um darauf aufmerksam zu machen, daß ich dieses zweite Buch desselben Verfassers, der ein ausgezeichnetes naturwissenschaftliches Buch ge­schrieben hat, für ein ganz unfruchtbares, törichtes Zeug halte, von einem Menschen, der gar nicht die Möglichkeit hat, über die Dinge zu reden, über die er da redet. Bequem das eine aus dem andern zu fol­gern, ohne sich jedesmal den Tatsachen aufs neue vorurteilslos gegen­überzustellen, das läßt unsere anthroposophisch orientierte Geistes­wissenschaft nicht zu. Die fordert eben wirklich von den Menschen eine Prüfung der Konkretheit gegenüber jedem einzelnen Falle. Philistrosität ist etwas, was schwinden wird, wenn die Impulse der Geisteswissenschaft sich verbreiten. Das auf dem Gebiete des Fühlens.",
      "Und auf dem Gebiete des Wollens, da ist es dasjenige, was so ganz besonders in der neueren Zeit im weitesten Sinne die Menschheit er­griffen hat und was ich doch nicht anders benennen kann denn als Ungeschicklichkeit. Durch das Eingeschränktsein desjenigen, was man lernt auf einem engen Kreis, kann der heutige Mensch in der Regel viel auf einem engen Kreise, und er ist ziemlich ungeschickt in bezug auf alles, was außerhalb dieses Kreises liegt. Man kann heute Männer kennenlernen, die sich keinen Hosenknopf annähen können! Unge­schicklichkeit außerhalb eines engsten Kreises, das ist dasjenige, was auf dem Gebiete des Willens insbesondere verbreitet ist.",
      "Wer nun nicht mit den bloßen abstrakten Gedanken, sondern mit der ganzen Seele bei dem ist, was man hier Geisteswissenschaft nennt, der wird sehen, daß diese Geisteswissenschaft in die Geschicklichkeit der Hände hineingeht, daß sie den Menschen geschickter macht, daß sie ihn geeignet macht, wirklich wiederum sein Interesse auf weitere Kreise, sein Wollen über eine weitere Welt auszudehnen. Natürlich ist gerade mit Bezug auf die Ungeschicklichkeit Geisteswissenschaft noch zu schwach, aber je stärker wir sie aufnehmen, desto mehr wird sie eine Bekämpferin sein der Ungeschicklichkeit.",
      "Also das ist es, was beim heutigen Aufnehmen der Geisteswissen­schaft, ich möchte sagen, als eine Trinität ihr gegenübersteht: Borniertheit",
      "auf intellektuellem Gebiete, Philistrosität, das heißt Eng­herzigkeit auf dem Fühlensgebiete, Ungeschicklichkeit auf dem Wil­lensgebiete. Und die drei liebt man heute, wenn man auch sich dessen nicht voll bewußt ist. Nichts wird heute mehr geliebt in der ganzen Welt als Ungeschicklichkeit, Philistrosität und Borniertheit. Und in­dem man diese drei liebt, wird man nicht leicht vordringen können zu den großen Aspekten, zu denen die Menschheit vordringen muß: zu den Aspekten, die sich an die Benennungen Ahriman und Luzifer anknüpfen. Und gerade hier ist etwas Wichtiges zu begreifen in unse­rer Zeit, denn in unserer Zeit ist unter mannigfaltigen andern Dingen auch ein sehr wichtiger Übergang vom Luziferischen zum Ahrima­nischen. Und da sich dieser Übergang nicht bloß sonstwo, sondern auch schon durchaus hier in der Schweiz zeigt, so kann man ja auch hier davon sprechen. Auf diesem Gebiet hat vielleicht hier das erste gerade durch schweizerische Gepflogenheiten weniger Bedeutung erlangt, aber das zweite, das hat alle Aussicht, gerade auf diesem Bo­den mehr Bedeutung zu erlangen. Die Menschheit ist nämlich in bezug auf gewisse Dinge in einem Übergang von luziferischen zu ahrimani­schen Untugenden, von luziferischen Kontraimpulsen in bezug auf die Entwickelung der Menschheit zu ahrimanischen Kontraimpulsen.",
      "Durchaus luziferisch geartet waren gewisse Impulse, die man in der früheren Zeit im Erziehungswesen geltend machte. Man rechnete im Erziehungswesen - wir alle, als wir jung waren, mit Ausnahme der Jüngsten unter uns, wissen ja das sehr genau - mit dem Ehrgeiz, mit der Eitelkeit. Also man rechnete - vielleicht hier in der Schweiz weniger, aber sonst ziemlich viel in der Welt - mit dem Ehrgeiz und der Eitelkeit, mit Ordenswesen, Titelwesen und so weiter, nicht wahr! Die ganze Laufbahn mancher Menschen war aufgebaut auf diesen luziferischen Impulsen der Eitelkeit, des Ehrgeizes, des Mehr-Geltens als ein anderer Mensch und so weiter. Versuchen Sie zurückzudenken, wie das Erziehungswesen schon aufgebaut war auf diesen luziferischen Impulsen.",
      "In der Gegenwart strebt man danach, an die Stelle dieser luzife­rischen Impulse ahrimanische zu setzen. Sie hüllen sich heute in das niedliche Wort «Begabtenprüfungen». Das will auf ahrimanischem",
      "Gebiete, was das Pochen auf den Ehrgeiz und die Eitelkeit schon bei dem Kinde auf luziferischem Gebiete war. Man strebt heute danach, die Begabtesten herauszufinden, diejenigen, die schon ohnedies in den Klassen am meisten können; aus denen sollen wiederum einzelne her­ausgezogen werden. Dann stellt man mit diesen Begabtenprüfungen an, Prüfungen des Intellekts, Prüfungen des Gedächtnisses, Prüfun­gen der Auffassungsgabe und so weiter. Und das ist etwas, wofür die Verfassung des Schweizer Gemütes sehr viel Veranlagung hat. Und wenn auch das Luziferische hier weniger eine Rolle spielte, dieses Ahrimanische, das zeigt sich schon in sehr niedlichen Keimen: Ver­ständnis für diese Begabtenprüfungen. Denn diese Begabtenprüfun­gen gehen ja aus von der Intelligenz, von der Wissenschaft, von der gegenwärtigen Gelehrtenpsychologie. Da setzt man sich hin, nicht wahr, diejenigen, deren Begabung man prüfen will, man schreibt ihnen auf: Mörder - Spiegel - Opftr des Mörders.",
      "Nun sitzen sie da, die armen Lämmer, vor den drei Worten Mör­der, Spiegel, Opfer des Mörders und sollen Verbindungsglieder su­chen. Das eine Kind findet: Der Mörder schleicht sich an sein Opfer heran, aber das Opfer hat einen Spiegel, und in dem spiegelt sich gerade der Mörder, und da kann sich das Opfer noch retten. - Das ist das erste Kind. Seine Auffassungsgabe geht dahin, die drei Worte so zu verbinden.",
      "Jetzt kommt ein anderes: Ein Mörder schleicht sich an sein Opfer heran, sieht sich in einem Spiegel; da kommt ihm sein Gesicht vor wie jemand, der kein gutes Gewissen hat, und der Mörder läßt ab von seinem Opfer, weil er sein Gesicht im Spiegel sieht. - Das ist das zweite Kind.",
      "Das dritte Kind macht eine andere Kombination: Ein Mörder schleicht heran. Dieser Mörder findet einen Spiegel. Er stößt sich an dem Spiegel; der Spiegel fällt herunter, macht einen furchtbaren Lärm, poltert. Das Opfer des Mörders wird auf das Gepolter auf­merksam und kann zur rechten Zeit sich rüsten gegen den Mörder.",
      "Das letzte Kind ist das Begabteste! Das erste hat nur das Aller­nächste an Ideenkombinationen gefunden, das zweite eine nahe­liegende moralische Sache, das dritte Kind hat aber eine sehr komplizierte",
      "Ideenverbindung gefunden. Das ist das Begabteste! Nun ja, es ist schon so ähnlich. Man muß ja natürlich alles, wenn man es kurz darstellen will, ein bißchen in seiner eigenartigen Wesenheit darstel­len. Aber so will man in der nächsten Zeit die Begabung der Kinder prüfen, damit man die Begabtesten herausbekomme.",
      "Das eine ist sicher: Wenn diejenigen Menschen, die diese Methoden erfinden, nachdenken würden, wer die Großen sind, die sie verehren, so Helmholtz, Newton und so weiter, so müßten sie sagen, die wären bei diesen Begabtenprüfungen alle, durch die Bank, als die unbe­gabtesten Kerlchen angesehen worden! - Es wäre nichts herausge­kommen. Denn Helmholtz, der heute bei den Leuten, die da die Be­gabtenprüfungen machen, ganz gewiß als ein großer Physiker ange­sehen wird, hatte einen Wasserkopf und war sehr unbegabt in seiner Jugend.",
      "Was will man denn da prüfen? Den bloßen äußeren Organismus, lediglich dasjenige, was als physisches Werkzeug des Menschen in Betracht kommt, das rein Ahrimanische der Menschennatur! Werden",
      "jemals die Früchte dieser Begabtenprüfungen in der Menschheit irgend etwas bedeuten, dann werden noch greulichere Gedankenge­bilde heraufkommen, als diejenigen sind, die zu der gegenwärtigen Menschheitskatastrophe geführt haben. Allein wenn man heute den Menschen spricht von dem, was vielleicht erst in hundert Jahren zu katastrophalen Ereignissen führen kann, so interessiert das ja die Menschen nicht. Aber wir leben jetzt in diesem Übergang von luzi­ferischem Erziehungssystem zum ahrimanischen Erziehungssystem, und wir müssen zu denen gehören, die solche Sachen ins Auge zu fassen verstehen.",
      "Dasjenige, was wirksame Kraft für die Zukunft ist, müssen die Menschen umsetzen in Kräfte der Gegenwart. Denn das ist es, was heute von uns gefordert wird: Gefordert wird echtes, wahres, unbe-fangenes Sich Gegenüberstellen dem, was konkrete, unmittelbare Wirklichkeit ist.",
      "Darinnen kann man ja sehr sonderbare Erfahrungen machen. Ich weiß nicht, ob ich hier eine Erfahrung schon erwähnt habe, die ganz interessant ist. Es gibt Schriften von Woodrow Wilson, eine Schrift",
      "über die Freiheit, eine andere Schrift heißt «Nur Literatur», die viel bewundert worden sind, auch heute noch von vielen sehr bewundert werden. In der einen Schrift, die «Nur Literatur» heißt, ist ein in­teressanter Essay wiedergegeben, den Woodrow Wilson über die historische Entwickelung von Amerika geschrieben hat.",
      "Auch sonst sind interessante Essays von Woodrow Wilson wiedergegeben mit weiten historischen Gesichtspunkten. Als ich diese Schriften las, machte ich eine interessante Erfahrung. In diesen Schriften finden sich einzelne Sätze, die mir ungemein bekannt schienen, und die doch ganz gewiß nicht von irgend etwas abgeschrieben waren; sie schienen mir aber doch außerordentlich bekannt.",
      "Und ich kam sehr bald dar­auf, daß diese Sätze, die da bei Woodrow Wilson stehen, ebensogut bei Herman Grimm stehen könnten, ja, daß mancher dieser Sätze so­gar wörtlich bei Herman Grimm steht. Herman Grimm liebe ich; Woodrow Wilson, das wissen Sie ja wohl, liebe ich nicht gerade.",
      "Aber ich kann deshalb doch nicht die objektive Tatsache verschweigen, daß in bezug auf den Inhalt der Sätze man Sätze von Herman Grimm in Vorträgen, Aufsätzen einfach herübernehmen und hineinstellen könnte in Wilsons Aufsätze, und umgekehrt Sätze von Wilson in Werke von Herman Grimm herübernehmen könnte. Da sagen zwei dem einfachen, gewöhnlichen Wortlaute nach eines und dasselbe.",
      "Aber in der Gegenwart muß man lernen: Wenn zwei dasselbe sagen, ist es nicht dasselbe! Denn es liegt die interessante Tatsache vor: Herman Grimms Sätze sind persönlich erkämpft, sind errungen, Schritt für Schritt von der Seele errungen.",
      "Woodrow Wilsons ganz gleichlautende Sätze rühren von einer eigentümlichen Besessenheit her. Von einem unterbewußten Ich ist der Mann besessen, das diese Sätze herauftreibt in das bewußte Leben.",
      "Wer solche Dinge beurteilen kann, der kommt darauf, daß es sich hier darum handelt: Weizenkorn ist Weizenkorn; aber es ist ein Un­terschied, ob das Weizenkorn in diesen Boden oder in jenen Boden gesenkt wird. Es ist ein Unterschied, ob jemand eine Idee so sehr als die seinige hat, daß er sie Stück für Stück auf seinem eigenen, per­sönlichsten Wege erkämpft hat, oder ob jemand diese Idee dadurch hat, daß ein Unterbewußtes ihn von sich, von diesem Unterbewußten,",
      "besessen gemacht hat: da tönt alles aus einem besessenen Unterbe­wußten heraus, aus einem Bewußtsein, das vom Unterbewußten be­sessen ist. Also es kommt heute schon darauf an, zu verstehen: Auf den Inhalt der Gedanken, auf den Inhalt von Programmen kommt es nicht an, sondern auf das lebendige Leben kommt es an, das die Menschheit lebt.",
      "Man kann materialistische Philosophie lehren, man kann bloße Gedankenphilosophie lehren, man kann bloße materialistische Na­turwissenschaft lehren, man kann mit bloß materialistischer Natur­wissenschaft ein ausgezeichneter europäischer Gelehrter sein, eine Zierde der Universität sein und daneben ein braver Staatsbürger: es ist ja der Typus nicht so selten, nicht wahr? Sie sind ja überall zu finden, die Zierden und Leuchten der Wissenschaft, die zu gleicher Zeit ganz tadellose, brave Staatsbürger sind!",
      "Das kann man ja ganz gut sein. Aber nehmen Sie irgendeine bestimmt geartete Idee, etwa den Kampf ums Dasein, um eine triviale Idee zu nennen, oder eine Idee, wie sie selbst zahmere Leute wie Oskar Hertwig vertreten, oder Ideen, wie sie Spenser oder Mill oder Boutroux und Bergson vertreten, die eben durchaus nicht zu spirituellem Leben vordringen wollen, sondern bei bloßen Gedankenphilosophien bleiben - aber noch mehr: Nehmen Sie das, was materialistische naturwissenschaftliche Ideen sind, nehmen Sie diese Ideen -, gewiß, sie können wachsen im Gehirn von braven Staatsbürgern; schön, aber Weizenkorn ist Wei­zenkorn, doch es ist ein Unterschied, ob ein Weizenkorn in weizen-fruchtbarem Boden wächst oder in felsigem Boden, und es ist ein Unterschied, ob dieselbe naturwissenschaftliche Idee, die in Europa als eine Zierde der Naturwissenschaft errungen werden kann und an den Universitäten gilt, in den Gehirnen der Universitätslehrer wächst, oder ob sie wächst in dem Gehirn eines Menschen, der einen Bruder hat, welcher schon als junger Mann, am Ende der achtziger Jahre, als eine Leuchte der Wissenschaft in einem Petersburger Laboratorium gilt, der voller fruchtbarer chemischer Ideen ist, mit einer besonderen Medaille ausgezeichnet, von allen, die mit ihm gearbeitet haben, als junger Mann schon hochverehrt wird - und dieser Bruder ist plötz­[ich nicht mehr da!",
      "Eben noch von der Universitätsbehörde ausgezeichnet,",
      "plötzlich nicht mehr da! Auf allen möglichen Umwegen sollen dann seine Kollegen erfahren haben, daß er mittlerweile ge­henkt worden ist, weil er an Verschwörungen teilgenommen hatte gegen Alexander III., den Reaktionär. Solche Tatsachen beleuchten die Dinge, die in der Gegenwart spielen, als Lichtblitze. Es ist nun ein Unterschied, ob dieselbe Idee in das Gehirn eines braven west­europäischen Universitätsprofessors fällt oder in das Gehirn des Bruders dieses unter solchen Voraussetzungen Gehenkten. Wenn sie in das Gehirn dieses Bruders fällt, dann verwandelt sich dieser Bruder in einen Lenin - denn der Bruder dieses Gehenkten ist Lenin -, und dann wird dieselbe Idee zur Triebkraft von alledem,was Sie jetzt im Osten Europas aufgehen sehen.",
      "Idee ist Idee, wie Weizenkorn Weizenkorn ist, aber man muß er­kennen, ob etwas dieselbe Idee ist und nun auftritt, je nachdem, in dem Gehirn des Universitätsprofessors oder in dem Gehirn des Bruders des dazumal Gehenkten. Man muß den Willen haben, hineinzu-schauen in diejenigen Untergründe des Daseins, wo die wirklichen Impulse des Geschehens liegen. Und man muß den Mut haben, abzu­lehnen all das Phrasenzeug von Programmen und Ideen von Wissen­schaftern, die da glauben, wenn sie dies oder jenes vertreten, so komme etwas darauf an. Vertreten kann man dem Inhalte nach dies oder jenes; doch darauf kommt es an, in welchem Gebiete des leben­digen Lebens dieses also Vertretene ist, so wie es darauf ankommt, in welches Gebiet das Weizenkorn fällt, ob in einen fruchtbaren Boden oder in einen unfruchtbaren Boden. Den Weg von der Ab­straktion, die unter den heutigen ernsten Verhältnissen überall zur Illusion oder zum Chaos führt, zu der Wirklichkeit, die einzig und allein in der Spiritualität gefunden werden kann, diesen Weg muß auf allen Gebieten die Menschheit suchen. Und wenn es noch so lange dauert: Auf diesem Wege allein kann die Menschheit das Heil und den Segen aus der gegenwärtigen Verwirrung heraus finden.",
      "Das ist es, was wir uns ins Herz schreiben sollten, worinnen wir uns zusammenfinden sollen. Das ist es, womit wir uns in einer ernsten Begrüßung begrüßen sollten: in diesem Wissen, dazuzugehören zu dem, was die Gebrechen der Menschheit heilen muß. Sie sind heilbar,",
      "aber sie dürfen nicht mit Quacksalbereien geheilt werden wollen. Sie müssen geheilt werden mit demjenigen, durch dessen Mangel die Menschheit gerade in das Chaos hineingekommen ist.",
      "Niemals hätte im Osten der Leninismus Platz greifen können, wenn nicht im Westen die materialistische Wissenschaft, die manchmal gar nicht sich materialistisch glaubt, gelehrt worden wäre. Denn was im Osten gemacht wird, ist direkt ein Kind der materialistischen Wissen­schaft. Ein Wechselbalg ist durch Karl Marx entstanden. Das wirk­liche Kind der materialistischen Wissenschaft ist schon im Osten vorhanden. Aber man muß den Willen haben, in alle diese Dinge wirk­lich hineinzuschauen.",
      "Das, meine lieben Freunde, ist gewissermaßen der Hintergrund, auf dem sich nun, ich möchte sagen, abhebt unser Bau. Und einzelne Menschen hier bei diesem Bau, sie arbeiten, denken an den Bau wahr­haftig recht abseits von den Ideen, die auf so vielen Territorien heute die Menschheit bewegen.",
      "Man kann sich gut denken, daß da draußen auf den andern Territorien viele Menschen sind, die da finden, daß hier Menschen leben, die sich absondern von dem, was heute die Welt bewegt und, wie die Menschen glauben, auch bewegen sollte. Man könnte sich das denken, daß die Leute vorwurfsvoll an diesen Ort hinsehen.",
      "Diejenigen, die mit ganzem Herzen und ganzer Seele bei diesem Bau sind, brauchen sich aus diesem Vorwurf nichts zu machen. Denn, möge dieser Bau vielleicht gar nicht seine Aufgabe erfüllen, möge dieser Bau gar nicht sein Ziel erreichen: was an die­sem Bau aber arbeitet und was von denen aus gearbeitet wird, die an diesem Bau mit Hingabe arbeiten, das ist dasjenige, was das Aller­wichtigste ist in der Gegenwart, das ist dasjenige, was die gegenwärtige Menschheit herausführen muß aus alldem, in das sie hineingekommen ist.",
      "Und wenn die Menschen draußen etwa glauben: Hier arbeiten Leute abseits von den Aufgaben der gegenwärtigen Menschheit -, so muß man diesen Leuten sagen können: Hier wird gerade gearbeitet für das Allerwichtigste, für das Allerwesentlichste in der Gegenwart, das nur die andern nicht kennen, wovon die andern noch nichts wis­sen. Aber davon wird es gerade abhängen, daß die Menschheit werde etwas wissen wollen von dem, was hier geschieht.",
      "Noch einmal sei es betont: Nicht darauf kommt es an, ob dieser Bau sein Ziel erreicht - obgleich es gut wäre, wenn er sein Ziel er­reichen würde -, sondern darauf kommt es an, daß aus gewissen Ideen heraus an diesem Bau gearbeitet worden ist, daß sich Menschen ge­funden haben für das Arbeiten an diesem Bau. Und nicht der Inhalt dieser Ideen, sondern die Art, wie diese Ideen leben, das ist dasjenige, was die Menschheitsimpulse für die Zukunft sind, während das, woran heute viele glauben, nichts anderes ist als die zum Grabe sich neigen-den, in die Auflösung übergehenden, für die Auflösung auch reifen Ideen der Vorzeit. Davon wollen wir dann morgen weiter reden."
    ],
    "sentences": [
      [
        "Daß es mir die tiefste Befriedigung gewährt, die Arbeit in Ihrer Mitte an diesem unserem Bau und um unseren Bau herum hier wiederum aufnehmen zu können, das werden Sie mir wohl ohne weiteres glau­ben.",
        "Es ist ja tatsächlich so, daß heute nicht nur bei tieferem Nach­denken, sondern, man darf sagen, schon bei oberflächlicherem Nach­denken demjenigen, der der ganzen Aura dieses Baues nahegetreten ist, der Gedanke aufgehen könnte, daß mit diesem Bau doch etwas verknüpft ist, was mit den bedeutungsvollsten, schwerwiegendsten Aufgaben der Menschenzukunft zusammenhängt.",
        "Und nach längerer, erzwungener Abwesenheit ist es ja selbstverständiich, daß man sich mit tiefster Befriedigung wiederum an der Stätte befindet, an der dieser Bau als ein Symbolum unserer Sache steht."
      ],
      [
        "Zu dem Gesagten darf ich wohl hinzufügen, daß für mich besonders jedesmal, wenn ich jetzt nach längerer Abwesenheit wieder komme, die tiefste Befriedigung daraus resultiert, daß ich ja immer dann sehen kann, wie schön und wie bedeutungsvoll die Arbeit an diesem Bau durch die hingebungsvolle Tätigkeit der am Bau Arbeitenden weiter gefördert worden ist.",
        "Insbesondere in diesen Monaten meiner letzten Abwesenheit, wo ja unter so schwierigen Verhältnissen gearbeitet worden ist, ist ja gerade ein Teil der künstlerischen Arbeit in einer unvergleichlichen Weise fortgeschritten, fortgeschritten in dem Geiste, der dieses Ganze durchdringen soll."
      ],
      [
        "Aber auch mit tiefer Befriedigung sehe ich bei Verfolgung des Geistes unserer Arbeit, bei Verfolgung desjenigen, was hier entsteht, das Verbundensein treuer Gesinnung bei vielen unserer Freunde, treuer Gesinnung gegenüber dem, was sich gerade in diesem Bau ver­körpert.",
        "Und dasjenige, was dann beim Wieder auf sich wirken ­Lassen dieser Sache der Seele sich offenbart, das ist doch, daß hier eine Stätte vorhanden ist, mit welcher verbunden ist eine solche treue Gesinnung einer Anzahl von Freunden unserer geistigen Bewegung, einer solch treuen Gesinnung, die da verspricht, daß sich die besten"
      ],
      [
        "Impulse unserer geistigen Bewegung in die Zukunft der Menschheit hinein halten werden, der sie so notwendig sein werden.",
        "Es gibt schon innerhalb gerade der diesem Bau gewidmeten Arbeit etwas, was Vor­bild sein könnte für dasjenige, was im allgemeinen mit dem, was sich unter uns heute Anthroposophlsche Gesellschaft nennt, eigentlich gewollt ist."
      ],
      [
        "Aber ich habe auf der andern Seite vielfach wiederum das Gefühl, daß das Günstige, das bedeutungsvoll Gute, das man hier im Zusam­menwirken von Menschenarbeit und Menschengefühl mit diesem Bau finden kann, gerade darinnen besteht, daß dieser Bau etwas ist, was gewissermaßen in seiner Objektivität das, was durch unsere Bewegung gewollt wird, loslöst von den subjektiven Interessen der einzelnen Menschen."
      ],
      [
        "Über dieses jetzt eben Berührte waren ja - und sind - in allen ähn­lichen Gesellschaften, auch in der Anthroposophischen Gesellschaft, gewisse merkwürdige Anschauungen vorhanden, die eigentlich nichts anderes sind als merkwürdige Illusionen.",
        "Man predigt viel von Selbst-losigkeit, von allgemeiner Menschenliebe; aber das sind oftmals bloße Masken für gewisse, nur raffinierte egoistische Interessen der einzel­nen Menschen.",
        "Gewiß, die einzelnen Menschen wissen nicht, daß es sich für sie um bloße egoistische Interessen handelt, sie sind vor ihrem eigenen Bewußtsein gewissermaßen unschuldig; aber es ist doch so.",
        "Der Bau selbst verlangt aber von einer schon ziemlich großen Anzahl unserer Freunde eine selbstlose Hingabe an etwas Objektives, an etwas, was als ein von jeder einzelnen Persönlichkeit losgelöstes Symbolum unserer Sache dasteht.",
        "Und insoferne wird wohl dasjenige, was mit diesem Bau zusammenhängt, vorbildlich sein können für das, was unsere Bewegung will."
      ],
      [
        "Meine lieben Freunde, wenn wir uns so wie heute wiederum be­grüßen, da dürfen wir insbesondere die Blicke richten auf das Frucht­bare und Umfassende dieser unserer geistigen Bewegung, und wir dürfen bei einer solchen Begrüßung bedenken, daß es uns ernst sein kann mit dem Glauben: Wie es auch immer geschehen mag - das Wie, das kann ja noch so oder so, je nach den Verhältnissen sich abspielen -, aus der furchtbaren Sackgasse, in welche die Menschheit hineingeraten"
      ],
      [
        "ist in der Gegenwart, wird sie nicht früher herauskommen, als bis sie sich entschließt, in irgendeiner Weise Anknüpfungspunkte zu suchen für fruchtbares Wirken, fruchtbares Tun innerhalb einer solchen gei­stigen Bewegung, wie es die unsrige ist.",
        "Wir werden ja ganz gewiß nicht in egoistischer Weise darauf bestehen, die Wahrheit gerade nur innerhalb unseres engen, beschränkten Kreises zu haben; aber wir dürfen uns in einem Kreise zusammengehörig wissen, welcher er­kennt, daß die Menscheit wegen des Vernachlässigens ihrer Geistes-substanz sich in diese furchtbare Lage der Gegenwart gebracht hat.",
        "Wissen können wir uns als solche Menschen, die vereint sind mit jenen Ideen, die einzig und allein hinausführen können aus der Sack-gasse, in welche die Menschheit gekommen ist."
      ],
      [
        "Es ist ja in den Seelen der heutigen Menschen ungemein vieles un­geklärt.",
        "Wenn man wiederum da und dort sich hat unterrichten kön­nen über die Bedürfnisse, die obwalten nach unserer geistigen Bewe­gung, so kann man auf der einen Seite sagen: Ja, es sind doch die Seelen derjenigen, die da dürsten nach jenem spirituellen Leben, das wir meinen, der Zahl nach in starker Zunahme begriffen."
      ],
      [
        "Die Sehn­sucht nach solchem spirituellem Leben, sie hat sich, das darf wohl ge­sagt werden, ungeheuer vergrößert.",
        "Die Aufmerksamkeit, welche entgegengebracht wird unseren Impulsen, sie ist unstreitig in den letzten Jahren auch eine größere geworden, wenigstens auf den Ge­bieten, die mit in äußerlicher Weise in diesen letzten Jahren und ins­besondere in den letzten Monaten zugänglich waren."
      ],
      [
        "Auch das wird nicht ganz bedeutungslos sein, zu bemerken, daß eine solche Ver­größerung und Verstärkung dieser Sehnsucht der Menschenseelen nach dem spirituellen Leben ganz deutlich vorhanden ist.",
        "Allerdings steht dieser Verstärkung und Verschärfung der Sehnsucht nach dem spirituellen Leben das andere gegenüber: jene furchtbare Beirrung, unter welcher der weitaus größte Teil der Menschheit leidet, jene furchtbare Beirrung, welche durch die altüberkommenen Ideen, oder man könnte besser sagen, durch die altüberkommene Ideenlosigkeit innerhalb der Menschheit bewirkt wird, die, man möchte sagen, Be­quemlichkeit gegenüber jedem starken, jedem scharfen Gedanken, jene Bequemlichkeit, die einfach herrührt aus der Laxheit, aus der"
      ],
      [
        "Trägheit, mit der das Gedankenleben seit vielen Jahrzehnten über die Erde hin geführt worden ist.",
        "Diese Laxheit, diese Trägheit beirrt die Seelen in dem vorhandenen Sehnen nach dem spirituellen Leben.",
        "Auf der einen Seite stecken die Menschen drinnen in einer wirklichen Sehn­sucht nach Geistigkeit, nach übersinnlichen, starken Impulsen.",
        "Auf der andern Seite werden die Seelen niedergehalten von all jenen alten Mächten, die nicht abtreten mögen vom Schauplatz des Menschen-wirkens und die doch sehen könnten aus dem, wie weit sie es gebracht haben, daß sie nicht mehr auf diesen Schauplatz des Menschenwirkens gehören.",
        "Man möchte sagen, daß man diesen dunkeln Eindruck, diesen zwiespältigen Eindruck überall hat."
      ],
      [
        "Ich habe ja unter unseren Mitgliedern an manchen Orten, in Ham­burg, in Berlin, in München, vielfach, in Anknüpfung an durch Licht-bilder wiedergegebene Darstellungen, von unserer Gruppe gespro­chen, die an der Hauptstelle unseres Baues stehen soll.",
        "Man konnte auf der einen Seite sehen, wie tatsächlich mächtige Impulse in die Seelen auch derjenigen hlneingehen, die durch die Verhältnisse der letzten Jahre niemals einen Blick werfen konnten auf das, was hier geschieht.",
        "Ein neues Menschenverständnis geht schon aus von derArt und Weise, wie das Ahrimanisch-Luziferische mit dem Christlichen zusammen gedacht wird und dargestellt, geoffenbart wird durch unsere Gruppe.",
        "Es ergreift die Seelen, wenn das, was durch diese Dinge gegeben wird, an diese Seelen herantritt.",
        "Allein, auf der andern Seite zeigen sich über­all die hemmenden Einflüsse dessen, was als Überbleibsel des Alten, Verfaulten am sogenannten Kulturleben sich über die Menschheit verbreitet."
      ],
      [
        "Das hat man ja insbesondere sehen können an der, man darf wahr­haftig im tiefsten Sinne sagen, humoristischen Art, wie den Vorträgen begegnet wurde, die ich im Kunsthause unseres Freundes, des Herrn von Bernus in München gehalten habe, worinnen ich versuchte, die inneren Impulse unserer hier betätigten Kunstanschauung einem größeren Publikum nahezubringen.",
        "Ja, Interesse hat das bei den Leu­ten außerordentlich viel erregt, denn ich habe im Februar und im Mai solche Vorträge in München gehalten, und ich mußte jeden dieser Vorträge zweimal halten; Herr von Bernus aber versicherte mir, es"
      ],
      [
        "wären so viel Anfragen da, daß ich jeden dieser Vorträge vor einem öffentlichen Publikum, worin ich die Prinzipien meiner Kunstan­schauung, wie sie hier in dem Bau zutage treten, dargelegt habe, hätte viermal halten können.",
        "Interesse war schon da.",
        "Aber da, wo man selbstverständlich unfroh sein würde, wenn Zustimmung vorhanden wäre, bei der Münchner Zeitungskritik, da war, man kann schon sa­gen, in edelstem Sinne humoristisches Zähnefletschen da.",
        "Es war ins­besondere humoristisch, weil der innere Groll gegen etwas, was man gar nicht verstehen konnte, sich da so geltend machte: Es war alles solch - nicht gesprochenes, sondern gespieenes Zeug!",
        "Verzeihen Sie den harten Ausdruck.",
        "Und es zeigte sich gerade an dem Interesse, das der Sache entgegengebracht wurde, worinnen Ehrlichkeit und Auf­richtigkeit sich aussprach, im Gegensatze zu dem, was aus diesem Kunstmittelpunkte sonst sich zeigte - das ist ja München selbstver-ständlich, nicht wahr, das ist ja bekannt -, es zeigte sich also, wie in diesem Kunstmittelpunkte sowohl das verständigste als auch das un­verständigste Zeug geredet wurde.",
        "Gerade an dieser Diskrepanz zeigte sich an einem Beispiel, wie diese zwei Strömungen, von denen ich Ihnen sprach, in der Gegenwart vorhanden sind; wie wir wirklich uns bewußt sein dürfen, in etwas ganz Wesentlichem und Wichtigem drinnenzustehen, das für die Welt, für die Zukunft zu erkämpfen ist."
      ],
      [
        "Ich sage das alles sicher nicht deshalb, weil ich irgendwie anstreben würde, wenn die Dinge in die Öffentlichkeit treten, wie man sagt, eine «gute Presse» zu bekommen; denn ich würde in dem Augenblicke, wo eine «gute Presse» auftritt, glauben: Da muß selbstverständlich irgend etwas nicht richtig sein, da muß irgend etwas Falsches auf unserer Seite geschehen sein."
      ],
      [
        "Alle diese Dinge sind ja geeignet, in uns das Bewußtsein hervorzu­rufen, daß wir gar sehr nötig haben, mit aller Entschiedenheit auf dem Boden unserer Sache zu stehen.",
        "Denn nichts könnte uns in schimmere Verwirrung hineinführen, als wenn wir irgendwelche Kompromisse schließen wollten mit dem, wovon die Außenwelt meint, daß es das Richtige wäre für uns.",
        "Nur in den Prinzipien unserer Sache selbst müssen wir dasjenige finden, was uns die Richtung für unser Tun angibt."
      ],
      [
        "Auch für so etwas, das mehr nuttelbar mit unserer Sache zusammen­hängt, aber doch innerlich zusammenhängt, auch für die Eurythmie hat sich ja in der letzten Zeit ein immer steigendes Interesse an den verschiedensten Orten gezeigt.",
        "Und wenn wir, die wir da waren, uns erinnern, wie zum Beispiel gerade die Eurythmie in einem Orte auf­genommen worden ist, wo sie fast noch gar nicht gesehen worden ist, wo sie zum Teil sogar etwas Neues war für diejenigen, die sie gesehen haben, in Hamburg, so muß man sich wirklich an die Art, wie da die Sache aufgenommen wurde, mit einer tiefen Befriedigung erinnern."
      ],
      [
        "Gerade in Hamburg konnte man sehen, wie bedeutungsvoll die Im­pulse sind, die auch von einer solchen Sache ausgehen können.",
        "Und da waren Leute, die eigentlich im Grunde zum erstenmal so recht einen eurythmischen Wurf gesehen haben."
      ],
      [
        "Und es wird vielleicht auch für die Eurythmie die Möglichkeit kommen, mit ihr in die Öffentlich­keit einzutreten.",
        "Aber gerade dann mussen wir mit solch einer Sache auf dem allerfestesten Boden stehen, nichts anderes tun, als was ledig­lich aus unserer Sache selbst heraus folgt."
      ],
      [
        "Sonst würde sich sehr bald zeigen, daß von einem gewissen Punkte ab niemand glauben darf, daß ich in einer gewissen Sache, wenn es auf mich selbst ankommt, bieg­sam bin.",
        "Die meisten von Ihnen wissen schon, daß ich selbstverständ­lich überall da, wo es nicht auf etwas Prinzipielles ankommt, sondern wo es darauf ankommt, menschlich zu sein, das Menschliche in den Vordergrund zu stellen, in jeder Weise mit allen Menschen mitgehe -aber wo es an die Grenze kommt, daß auch nur im geringsten irgend etwas Prinzipielles verleugnet werden müßte, da würde ich mich nicht als biegsam erweisen."
      ],
      [
        "Wenn also in der jetzigen Zeit, wo so vieles an Tänzerei gesehen werden kann - denn überall wird ja getanzt, das ist ja ganz schrecklich, man könnte an jedem Abend, wenn man in einer größeren Stadt wohnt, einen Tanzabend mitmachen, wo überall schaugetanzt wird -, wenn man da glauben würde, und ich sage diese Sache nicht so ohne Begründung, obwohl ich auf nichts Konkretes hinweise, daß, wenn diese unsere Eurvthmie jetzt vor die Öffentlich­keit treten würde, wir irgendwie uns binden sollten an eine journa­listische Verständnislosigkeit, die irgendwelche Anforderungen stellte, so würde ich mich in der ganz entschiedensten Weise dagegen verwahren."
      ],
      [
        "Dasjenige, was Geschmacksrichtung ist, was Geschmacks­tendenz ist, muß lediglich aus unserer Sache selbst hervorgehen."
      ],
      [
        "Wir müssen uns manchmal auch erinnern, insbesondere wenn wir uns wieder begrüßen, an das aus dem Willen folgende, notwendige, geradiinige Sich-Bewegen nach Maßgabe unserer spirituellen Impulse.",
        "Diese spirituellen Impulse werden ja gegen manches zu kämpfen ha­ben."
      ],
      [
        "Man kann heute nicht mehr bloß sagen Vorurteil, denn die Dinge wirken zu stark, als daß man sie mit dem schwachen Wort Vorurteil belegen könnte; diese Impulse, die werden gegen mancherlei zu kämp­fen haben.",
        "Immer wieder und wiederum muß ja hingewiesen werden auf die große Krankheit unserer Zeit, welche in der Zügellosigkeit gegenüber dem Gedankenieben besteht."
      ],
      [
        "Denn das Gedankenleben ist schon ein spirituelles Leben, wenn man es richtig erfaßt.",
        "Und weil die Menscheit so wenig sich an das Gedankenleben halten will, findet sie so wenig den Weg in spirituelle Welten hinein."
      ],
      [
        "Und ich muß schon von der verschiedensten Seite immer wieder und wieder eines berüh­ren: Man hält heute furchtbar viel von dem bloßen Inhalt der Gedan­ken.",
        "Aber der Inhalt der Gedanken ist an den Gedanken das am aller­wenigsten Wichtige."
      ],
      [
        "Nicht wahr, ein Weizenkorn ist ein Weizenkorn; es läßt sich nicht bestreiten.",
        "Aber mag ein Weizenkorn auch ein Wei­zenkorn sein: Wenn Sie ein Weizenkorn in einen guten, fruchtbaren Weizenboden hineinsenken, so bekommen Sie eine saftige Weizen­ähre daraus; wenn Sie ein Weizenkorn in einen ganz unfruchtbaren, steinigen Boden hineinsenken, bekommen Sie entweder gar nichts oder eine sehr korrupte Weizenähre."
      ],
      [
        "Jedesmal haben Sie es mit einem Weizenkorn zu tun."
      ],
      [
        "Sagen wir jetzt etwas anderes statt Weizenkorn.",
        "Sagen wir statt Weizenkorn «Idee der freien Menschheit», von der ja heute so viel gesprochen wird; «Idee der freien Menschheit» ist «Idee der freien Menscheit», wird mancher sagen.",
        "Das ist geradeso wie: Weizenkorn ist Weizenkorn.",
        "Es ist ein Unterschied, ob «Idee der freien Mensch­heit» in einem Herzen, in einer Seele gedeiht - ganz genau dieselbe Idee mit derselben Begründung -, wo dieses Herz und diese Seele fruchtbarer Boden ist, oder ob die «Idee der freien Menschheit» in Woodrow Wilsons Kopf gedeiht!",
        "So wenig wie ein Weizenkorn gedeihen"
      ],
      [
        "kann, wenn es in einen steinigen Boden oder gar in den Felsen hineingesenkt wird, so bedeuten all die sogenannten schönen Ideen, die in den Programmen Woodrow Wilsons vorkommen, nichts, wenn sie aus diesem Kopfe kommen.",
        "Allein dies ist etwas, was der gegen­wärtigen Menschheit so unendlich schwer wird einzusehen, weil die gegenwärtige Menschheit eben der Anschauung ist: Man hält sich an den Inhalt von Programmen, an den Inhalt von Ideen.",
        "Aber der Inhalt von Programmen, der Inhalt von Ideen, der hat ebensowenig eine Bedeutung, als die Keimkraft eines Weizenkorns eine Bedeutung hat, bevor dieses Weizenkorn in einen gerade für es fruchtbaren Weizen­boden gesenkt wird."
      ],
      [
        "Real denken, das ist dasjenige, was der Menschheit so ungeheuer not tut.",
        "Und mit dem Unrealdenken der Gegenwart hängt etwas anderes zusammen, hängt zusammen, daß die Menschheit fast von allen Er­eignis sen überrascht wird.",
        "Man kann schon die Frage aufwerfen: Von was ist denn die Menschheit nicht überrascht worden in den letzten Jahren? - Von allem ist sie überrascht worden, und sie wird weiter noch viel mehr überrascht werden, als sie überrascht ist.",
        "Aber die Menschheit läßt sich ja nicht irgendwie auf dasjenige ein, was wirksam ist in der Welt.",
        "Daher ist es auch heute unmöglich, für irgendeine Sache die Menschheit zu irgendeiner Voraussicht zu bringen."
      ],
      [
        "Wenn man mit bloßen Ideen arbeitet, dann kann man von allen Seiten alles durch alles begründen.",
        "Wenn man mit dem bloßen Inhalt von Ideen arbeitet, kann man wirklich alles mit allem begründen.",
        "Auch das ist etwas, was im Grunde genommen immer mehr und mehr und immer tiefer und tiefer eingesehen werden muß, was aber nicht einge­sehen werden will."
      ],
      [
        "Gewöhnlich wenn man von solchen Dingen spricht und dann Bei­spiele anführt, findet man keinen rechten Glauben, weil die Beispiele zu grotesk sich ausnehmen.",
        "Aber von solchen Dingen, die in so gro­tesken Beispielen zutage treten, ist unser ganzes gegenwärtiges Seelen- und Geistesleben durchschwirrt.",
        "Ich weiß, daß gar mancher vielleicht mit Groll zuhört, wenn ich Ihnen eine recht ausgefallene Idee als ein Beispiel anführe.",
        "Ich will eine ganz ausgefallene Idee anführen."
      ],
      [
        "Da ist ein Universitätsprofessor, ein alter, angesehener Universitäts­professor auf die Tatsache gestoßen, daß Goethe in seinem langen Leben Neigungen gehabt hat für verschiedene Frauen.",
        "Darauf ist also ein Universitätsprofessor gestoßen, der sich zur Aufgabe gemacht hat, Goethes Leben und das Leben der mit ihm zusammenhängenden Gei­ster gründlich zu studieren."
      ],
      [
        "Und siehe da, selbstverständlich hat er, trotzdem er nicht gerade ein europäischer Universitätsprofessor ist, es sich zur Aufgabe gemacht, bei diesen Studien so gründlich zu Werke zu gehen, wie sonst in der Regel nur mitteleuropäische Universitäts­professoren zu Werke gehen: er hat die ganze Galerie der Goetheschen Frauengestalten in ihrem Verhältnis zu Goethe an seiner Seele Revue passieren lassen.",
        "Und was hat er herausgefunden?"
      ],
      [
        "Fast wörtlich kann ich es Ihnen anführen.",
        "Er hat herausgefunden: Was man über die je­weilig geliebte Frau in Goethes Leben sagen kann, das ist, daß jede für Goethe eine Art Belgien war, gegenüber welcher er die Neutralität verletzte, und dann darüber geseufzt hat, daß sein Herz blute, indem er über eine leuchtende Unschuld herfallen mußte."
      ],
      [
        "Aber er hat auch ticht vergessen, jedesmal wiederum wie der deutsche Kanzler zu be­haupten, daß das Gebiet der verletzten Neutralität ein besseres Schick­sal verdient haben würde, daß aber er, Goethe, nicht anders gekonnt habe, da seine Bestimmung, die Rechte seines geistigen Lebens ihn verpflichteten, die Geliebte zu opfern, ja den Schmerz seines eigenen Herzens zu opfern auf dem Altar der Pflicht, die er habe gegen sein eigenes unsterbliches Ich."
      ],
      [
        "Nun, aus diesem Buche könnte ich Ihnen noch manche ausgefallene Idee hier vorlegen.",
        "Sie würden sagen: Wozu das? - Aber es hat schon seine guten Gründe, denn derlei Ideen finden Sie heute überallhin über die Erde zerstreut.",
        "Sie sind so, die Ideen der heutigen Menschheit.",
        "Und nicht umsonst zeigen sich solche Ideen da, wo der Extrakt des menschlichen Denkens in der Literatur auftritt, denn diese Anschau­ung wird vertreten von San/qyana, dem Professor der Harvard-Univer­sität in Amerika, einem sehr angesehenen Spanier, der sich aber ganz amerikanisiert hat, dessen Buch während dieser Menschheitskatastro­phe geschrieben worden ist, und dessen französische Ausgabe einge­leitet worden ist von Boutroux> der kurz vor dem Kriege von Heidelberg"
      ],
      [
        "aus eine große Lobrede über die deutsche Philosophie gehalten hat.",
        "Dieses Buch heißt: «L'erreur de la philosophie allemande», und ist wahrhaftig nicht ein Zufallsbuch, sondern es ist ganz charakte­ristisch für das Denken der Gegenwart, weil ja wirklich mit derselben Leichtigkeit, mit welcher der Professor Santayana die Verletzung der belgischen Neutralität mit den Taten Goethes gegenüber verschiede­nen Frauen vergleicht, diese Menschheit das Entferntliegendste zu­sammenhält.",
        "Denn diese Art des Denkens tritt Ihnen, wenn Sie wirk­lich beobachten können, auf allen Gebieten der sogenannten heutigen Wissenschaft entgegen."
      ],
      [
        "Es ist ja schon einmal die Aufgabe jener geistigen Impulse, denen unsere anthroposophisch orientierte Geisteswissenschaft gewidmet ist, gegen drei Grundübel in der gegenwärtigen sogenannten Mensch­heitskultur anzukämpfen.",
        "Sie kann gar nicht anders, als gegen diese drei Grundübel anzukämpfen.",
        "Das eine Grundübel zeigt sich auf dem Gebiete des Denkens, das andere auf dem Gebiete des Fühlens, und das dritte auf dem Gebiete des Wollens."
      ],
      [
        "Auf dem Gebiete des Denkens ist es allmählich dazu gekommen, daß die Menschen nur so denken können, wie dasjenige Denken verläuft, das eng an das physische Gehirn gebunden ist.",
        "Aber dieses Denken, das eng an das physische Gehirn gebunden ist, das sich nicht erheben will in freiem Aufschwung zum Spirituellen, das ist unter allen Umständen dazu verurteilt, borniert zu werden, beschränkt zu werden.",
        "Und das bedeutungsvollste Kennzeichen, namentlich des gegenwärtigen wis­senschaftlichen Denkens, ist die Borniertheit, ist die Beschränktheit.",
        "Gewiß, man kann auf dem Felde des Beschränkten, des Bornierten, Großartiges leisten.",
        "Das tut zum Beispiel die gegenwärtige Natur­wissenschaft.",
        "Aber zur Naturwissenschaft, wie sie heute gedacht wird, ist ja keine Genialität notwendig.",
        "Also: Borniertheit, Beschränktheit, das ist dasjenige, was namentlich auf intellektuellem Gebiete be­kämpft werden muß.",
        "Ich will heute mehr skizzieren, wir werden diese Dinge genauer besprechen."
      ],
      [
        "Auf dem Gebiete des Fühlens handelt es sich darum, daß die Mensch­heit allmählich zu einer gewissen Philistrosität gekommen ist - man kann das nicht anders nennen -, Engherzigkeit, Philistrosität, Eingeschränktheit"
      ],
      [
        "auf gewisse engumgrenzte Kreise.",
        "Das ist ja das haupt-sächlichste Kennzeichen des Philisters, daß er sich nicht für große Weltenzusammenhänge interessieren kann.",
        "Kirchtumpolitiker sind immer Philister.",
        "Das kann natürlich auf dem Gebiete der Geisteswis­senschaft nicht genügen, denn da kann man sich nicht auf die engsten Kreise beschränken.",
        "Man muß sich sogar für das Außerirdische, man muß sich für sehr weite Kreise interessieren.",
        "Und die Leute ärgert es ja, wenn jemand auch nur vorgibt, für so weite Kreise, wie Mond, Sonne, Saturn, etwas wissen zu wollen.",
        "Aber die Philistrosität muß schon auf allen Gebieten der Nichtphilistrosität weichen, wenn Gei­steswissenschaft durchdringen soll.",
        "Das ist manchmal nicht bequem, denn das fordert rückhaltloses Sich-der-Sache-Gegenüberstellen, und ein mehr vorurteilsloses Sich-der-Sache-Gegenüberstellen."
      ],
      [
        "Da ist ja in der letzten Zeit einmal etwas recht Niedliches gerade auf unserem Boden passiert; aber ich habe vorgebeugt, es ist nichts Schlimmes passiert, es hätte nur etwas passieren können!",
        "Ich habe -Sie werden sich daran noch aus den vorjährigen Zürcher Vorträgen erinnern - unter den verschiedenen Beispielen, wie aus der Natur­wissenschaft selber eine Art Überwindung des Darwinismus heraus-wachsen kann, auf das ausgezeichnete Buch «Das Werden der Orga­nismen» von Oskar Hertwig hingewiesen.",
        "Ich habe hier und sonst überall, wo ich nur Gelegenheit gefunden habe, auf dieses ausgezeich­nete Buch hingewiesen.",
        "Nun erschien sehr bald nach diesem Buch ein kürzeres Buch, worin derselbe Oskar Hertwig über das soziale, das ethische und das politische Leben spricht, und ich hatte mir schon gedacht: Da kann passieren, daß einzelne unserer Mitglieder, wenn sie gehört haben, daß ich gesagt habe, das Buch von Oskar Hertwig «Das Werden der Organismen» sei ein ausgezeichnetes Buch, nun glauben, daß ich denselben Oskar Hertwig für eine unfehlbare Autorität an­sehe.",
        "Dieses Buch, das als zweites erschienen ist von Oskar Hertwig, ist ein Buch, das nichts taugt, ein Buch, das herrührt von einem Men­schen, der auf dem Gebiete, um das es sich da handelt, auf dem Ge­biete des sozialen, des ethischen, des politischen Lebens, absolut keinen einzigen ordentlichen Gedanken fassen kann.",
        "Ich fürchtete schon, daß einzelne unserer Mitglieder nun hätten finden können, daß auch dieses"
      ],
      [
        "Buch irgendeinen Wert haben könnte, weil es von demselben Oskar Hertwig herrührt.",
        "So mußte ich denn vorbauen und habe auch über­all, wo ich bisher die Gelegenheit ergreifen konnte, sie ergriffen, um darauf aufmerksam zu machen, daß ich dieses zweite Buch desselben Verfassers, der ein ausgezeichnetes naturwissenschaftliches Buch ge­schrieben hat, für ein ganz unfruchtbares, törichtes Zeug halte, von einem Menschen, der gar nicht die Möglichkeit hat, über die Dinge zu reden, über die er da redet.",
        "Bequem das eine aus dem andern zu fol­gern, ohne sich jedesmal den Tatsachen aufs neue vorurteilslos gegen­überzustellen, das läßt unsere anthroposophisch orientierte Geistes­wissenschaft nicht zu.",
        "Die fordert eben wirklich von den Menschen eine Prüfung der Konkretheit gegenüber jedem einzelnen Falle.",
        "Philistrosität ist etwas, was schwinden wird, wenn die Impulse der Geisteswissenschaft sich verbreiten.",
        "Das auf dem Gebiete des Fühlens."
      ],
      [
        "Und auf dem Gebiete des Wollens, da ist es dasjenige, was so ganz besonders in der neueren Zeit im weitesten Sinne die Menschheit er­griffen hat und was ich doch nicht anders benennen kann denn als Ungeschicklichkeit.",
        "Durch das Eingeschränktsein desjenigen, was man lernt auf einem engen Kreis, kann der heutige Mensch in der Regel viel auf einem engen Kreise, und er ist ziemlich ungeschickt in bezug auf alles, was außerhalb dieses Kreises liegt.",
        "Man kann heute Männer kennenlernen, die sich keinen Hosenknopf annähen können!",
        "Unge­schicklichkeit außerhalb eines engsten Kreises, das ist dasjenige, was auf dem Gebiete des Willens insbesondere verbreitet ist."
      ],
      [
        "Wer nun nicht mit den bloßen abstrakten Gedanken, sondern mit der ganzen Seele bei dem ist, was man hier Geisteswissenschaft nennt, der wird sehen, daß diese Geisteswissenschaft in die Geschicklichkeit der Hände hineingeht, daß sie den Menschen geschickter macht, daß sie ihn geeignet macht, wirklich wiederum sein Interesse auf weitere Kreise, sein Wollen über eine weitere Welt auszudehnen.",
        "Natürlich ist gerade mit Bezug auf die Ungeschicklichkeit Geisteswissenschaft noch zu schwach, aber je stärker wir sie aufnehmen, desto mehr wird sie eine Bekämpferin sein der Ungeschicklichkeit."
      ],
      [
        "Also das ist es, was beim heutigen Aufnehmen der Geisteswissen­schaft, ich möchte sagen, als eine Trinität ihr gegenübersteht: Borniertheit"
      ],
      [
        "auf intellektuellem Gebiete, Philistrosität, das heißt Eng­herzigkeit auf dem Fühlensgebiete, Ungeschicklichkeit auf dem Wil­lensgebiete.",
        "Und die drei liebt man heute, wenn man auch sich dessen nicht voll bewußt ist.",
        "Nichts wird heute mehr geliebt in der ganzen Welt als Ungeschicklichkeit, Philistrosität und Borniertheit.",
        "Und in­dem man diese drei liebt, wird man nicht leicht vordringen können zu den großen Aspekten, zu denen die Menschheit vordringen muß: zu den Aspekten, die sich an die Benennungen Ahriman und Luzifer anknüpfen.",
        "Und gerade hier ist etwas Wichtiges zu begreifen in unse­rer Zeit, denn in unserer Zeit ist unter mannigfaltigen andern Dingen auch ein sehr wichtiger Übergang vom Luziferischen zum Ahrima­nischen.",
        "Und da sich dieser Übergang nicht bloß sonstwo, sondern auch schon durchaus hier in der Schweiz zeigt, so kann man ja auch hier davon sprechen.",
        "Auf diesem Gebiet hat vielleicht hier das erste gerade durch schweizerische Gepflogenheiten weniger Bedeutung erlangt, aber das zweite, das hat alle Aussicht, gerade auf diesem Bo­den mehr Bedeutung zu erlangen.",
        "Die Menschheit ist nämlich in bezug auf gewisse Dinge in einem Übergang von luziferischen zu ahrimani­schen Untugenden, von luziferischen Kontraimpulsen in bezug auf die Entwickelung der Menschheit zu ahrimanischen Kontraimpulsen."
      ],
      [
        "Durchaus luziferisch geartet waren gewisse Impulse, die man in der früheren Zeit im Erziehungswesen geltend machte.",
        "Man rechnete im Erziehungswesen - wir alle, als wir jung waren, mit Ausnahme der Jüngsten unter uns, wissen ja das sehr genau - mit dem Ehrgeiz, mit der Eitelkeit.",
        "Also man rechnete - vielleicht hier in der Schweiz weniger, aber sonst ziemlich viel in der Welt - mit dem Ehrgeiz und der Eitelkeit, mit Ordenswesen, Titelwesen und so weiter, nicht wahr!",
        "Die ganze Laufbahn mancher Menschen war aufgebaut auf diesen luziferischen Impulsen der Eitelkeit, des Ehrgeizes, des Mehr-Geltens als ein anderer Mensch und so weiter.",
        "Versuchen Sie zurückzudenken, wie das Erziehungswesen schon aufgebaut war auf diesen luziferischen Impulsen."
      ],
      [
        "In der Gegenwart strebt man danach, an die Stelle dieser luzife­rischen Impulse ahrimanische zu setzen.",
        "Sie hüllen sich heute in das niedliche Wort «Begabtenprüfungen».",
        "Das will auf ahrimanischem"
      ],
      [
        "Gebiete, was das Pochen auf den Ehrgeiz und die Eitelkeit schon bei dem Kinde auf luziferischem Gebiete war.",
        "Man strebt heute danach, die Begabtesten herauszufinden, diejenigen, die schon ohnedies in den Klassen am meisten können; aus denen sollen wiederum einzelne her­ausgezogen werden.",
        "Dann stellt man mit diesen Begabtenprüfungen an, Prüfungen des Intellekts, Prüfungen des Gedächtnisses, Prüfun­gen der Auffassungsgabe und so weiter.",
        "Und das ist etwas, wofür die Verfassung des Schweizer Gemütes sehr viel Veranlagung hat.",
        "Und wenn auch das Luziferische hier weniger eine Rolle spielte, dieses Ahrimanische, das zeigt sich schon in sehr niedlichen Keimen: Ver­ständnis für diese Begabtenprüfungen.",
        "Denn diese Begabtenprüfun­gen gehen ja aus von der Intelligenz, von der Wissenschaft, von der gegenwärtigen Gelehrtenpsychologie.",
        "Da setzt man sich hin, nicht wahr, diejenigen, deren Begabung man prüfen will, man schreibt ihnen auf: Mörder - Spiegel - Opftr des Mörders."
      ],
      [
        "Nun sitzen sie da, die armen Lämmer, vor den drei Worten Mör­der, Spiegel, Opfer des Mörders und sollen Verbindungsglieder su­chen.",
        "Das eine Kind findet: Der Mörder schleicht sich an sein Opfer heran, aber das Opfer hat einen Spiegel, und in dem spiegelt sich gerade der Mörder, und da kann sich das Opfer noch retten. - Das ist das erste Kind.",
        "Seine Auffassungsgabe geht dahin, die drei Worte so zu verbinden."
      ],
      [
        "Jetzt kommt ein anderes: Ein Mörder schleicht sich an sein Opfer heran, sieht sich in einem Spiegel; da kommt ihm sein Gesicht vor wie jemand, der kein gutes Gewissen hat, und der Mörder läßt ab von seinem Opfer, weil er sein Gesicht im Spiegel sieht. - Das ist das zweite Kind."
      ],
      [
        "Das dritte Kind macht eine andere Kombination: Ein Mörder schleicht heran.",
        "Dieser Mörder findet einen Spiegel.",
        "Er stößt sich an dem Spiegel; der Spiegel fällt herunter, macht einen furchtbaren Lärm, poltert.",
        "Das Opfer des Mörders wird auf das Gepolter auf­merksam und kann zur rechten Zeit sich rüsten gegen den Mörder."
      ],
      [
        "Das letzte Kind ist das Begabteste!",
        "Das erste hat nur das Aller­nächste an Ideenkombinationen gefunden, das zweite eine nahe­liegende moralische Sache, das dritte Kind hat aber eine sehr komplizierte"
      ],
      [
        "Ideenverbindung gefunden.",
        "Das ist das Begabteste!",
        "Nun ja, es ist schon so ähnlich.",
        "Man muß ja natürlich alles, wenn man es kurz darstellen will, ein bißchen in seiner eigenartigen Wesenheit darstel­len.",
        "Aber so will man in der nächsten Zeit die Begabung der Kinder prüfen, damit man die Begabtesten herausbekomme."
      ],
      [
        "Das eine ist sicher: Wenn diejenigen Menschen, die diese Methoden erfinden, nachdenken würden, wer die Großen sind, die sie verehren, so Helmholtz, Newton und so weiter, so müßten sie sagen, die wären bei diesen Begabtenprüfungen alle, durch die Bank, als die unbe­gabtesten Kerlchen angesehen worden! - Es wäre nichts herausge­kommen.",
        "Denn Helmholtz, der heute bei den Leuten, die da die Be­gabtenprüfungen machen, ganz gewiß als ein großer Physiker ange­sehen wird, hatte einen Wasserkopf und war sehr unbegabt in seiner Jugend."
      ],
      [
        "Was will man denn da prüfen?",
        "Den bloßen äußeren Organismus, lediglich dasjenige, was als physisches Werkzeug des Menschen in Betracht kommt, das rein Ahrimanische der Menschennatur!",
        "Werden"
      ],
      [
        "jemals die Früchte dieser Begabtenprüfungen in der Menschheit irgend etwas bedeuten, dann werden noch greulichere Gedankenge­bilde heraufkommen, als diejenigen sind, die zu der gegenwärtigen Menschheitskatastrophe geführt haben.",
        "Allein wenn man heute den Menschen spricht von dem, was vielleicht erst in hundert Jahren zu katastrophalen Ereignissen führen kann, so interessiert das ja die Menschen nicht.",
        "Aber wir leben jetzt in diesem Übergang von luzi­ferischem Erziehungssystem zum ahrimanischen Erziehungssystem, und wir müssen zu denen gehören, die solche Sachen ins Auge zu fassen verstehen."
      ],
      [
        "Dasjenige, was wirksame Kraft für die Zukunft ist, müssen die Menschen umsetzen in Kräfte der Gegenwart.",
        "Denn das ist es, was heute von uns gefordert wird: Gefordert wird echtes, wahres, unbe-fangenes Sich Gegenüberstellen dem, was konkrete, unmittelbare Wirklichkeit ist."
      ],
      [
        "Darinnen kann man ja sehr sonderbare Erfahrungen machen.",
        "Ich weiß nicht, ob ich hier eine Erfahrung schon erwähnt habe, die ganz interessant ist.",
        "Es gibt Schriften von Woodrow Wilson, eine Schrift"
      ],
      [
        "über die Freiheit, eine andere Schrift heißt «Nur Literatur», die viel bewundert worden sind, auch heute noch von vielen sehr bewundert werden.",
        "In der einen Schrift, die «Nur Literatur» heißt, ist ein in­teressanter Essay wiedergegeben, den Woodrow Wilson über die historische Entwickelung von Amerika geschrieben hat."
      ],
      [
        "Auch sonst sind interessante Essays von Woodrow Wilson wiedergegeben mit weiten historischen Gesichtspunkten.",
        "Als ich diese Schriften las, machte ich eine interessante Erfahrung.",
        "In diesen Schriften finden sich einzelne Sätze, die mir ungemein bekannt schienen, und die doch ganz gewiß nicht von irgend etwas abgeschrieben waren; sie schienen mir aber doch außerordentlich bekannt."
      ],
      [
        "Und ich kam sehr bald dar­auf, daß diese Sätze, die da bei Woodrow Wilson stehen, ebensogut bei Herman Grimm stehen könnten, ja, daß mancher dieser Sätze so­gar wörtlich bei Herman Grimm steht.",
        "Herman Grimm liebe ich; Woodrow Wilson, das wissen Sie ja wohl, liebe ich nicht gerade."
      ],
      [
        "Aber ich kann deshalb doch nicht die objektive Tatsache verschweigen, daß in bezug auf den Inhalt der Sätze man Sätze von Herman Grimm in Vorträgen, Aufsätzen einfach herübernehmen und hineinstellen könnte in Wilsons Aufsätze, und umgekehrt Sätze von Wilson in Werke von Herman Grimm herübernehmen könnte.",
        "Da sagen zwei dem einfachen, gewöhnlichen Wortlaute nach eines und dasselbe."
      ],
      [
        "Aber in der Gegenwart muß man lernen: Wenn zwei dasselbe sagen, ist es nicht dasselbe!",
        "Denn es liegt die interessante Tatsache vor: Herman Grimms Sätze sind persönlich erkämpft, sind errungen, Schritt für Schritt von der Seele errungen."
      ],
      [
        "Woodrow Wilsons ganz gleichlautende Sätze rühren von einer eigentümlichen Besessenheit her.",
        "Von einem unterbewußten Ich ist der Mann besessen, das diese Sätze herauftreibt in das bewußte Leben."
      ],
      [
        "Wer solche Dinge beurteilen kann, der kommt darauf, daß es sich hier darum handelt: Weizenkorn ist Weizenkorn; aber es ist ein Un­terschied, ob das Weizenkorn in diesen Boden oder in jenen Boden gesenkt wird.",
        "Es ist ein Unterschied, ob jemand eine Idee so sehr als die seinige hat, daß er sie Stück für Stück auf seinem eigenen, per­sönlichsten Wege erkämpft hat, oder ob jemand diese Idee dadurch hat, daß ein Unterbewußtes ihn von sich, von diesem Unterbewußten,"
      ],
      [
        "besessen gemacht hat: da tönt alles aus einem besessenen Unterbe­wußten heraus, aus einem Bewußtsein, das vom Unterbewußten be­sessen ist.",
        "Also es kommt heute schon darauf an, zu verstehen: Auf den Inhalt der Gedanken, auf den Inhalt von Programmen kommt es nicht an, sondern auf das lebendige Leben kommt es an, das die Menschheit lebt."
      ],
      [
        "Man kann materialistische Philosophie lehren, man kann bloße Gedankenphilosophie lehren, man kann bloße materialistische Na­turwissenschaft lehren, man kann mit bloß materialistischer Natur­wissenschaft ein ausgezeichneter europäischer Gelehrter sein, eine Zierde der Universität sein und daneben ein braver Staatsbürger: es ist ja der Typus nicht so selten, nicht wahr?",
        "Sie sind ja überall zu finden, die Zierden und Leuchten der Wissenschaft, die zu gleicher Zeit ganz tadellose, brave Staatsbürger sind!"
      ],
      [
        "Das kann man ja ganz gut sein.",
        "Aber nehmen Sie irgendeine bestimmt geartete Idee, etwa den Kampf ums Dasein, um eine triviale Idee zu nennen, oder eine Idee, wie sie selbst zahmere Leute wie Oskar Hertwig vertreten, oder Ideen, wie sie Spenser oder Mill oder Boutroux und Bergson vertreten, die eben durchaus nicht zu spirituellem Leben vordringen wollen, sondern bei bloßen Gedankenphilosophien bleiben - aber noch mehr: Nehmen Sie das, was materialistische naturwissenschaftliche Ideen sind, nehmen Sie diese Ideen -, gewiß, sie können wachsen im Gehirn von braven Staatsbürgern; schön, aber Weizenkorn ist Wei­zenkorn, doch es ist ein Unterschied, ob ein Weizenkorn in weizen-fruchtbarem Boden wächst oder in felsigem Boden, und es ist ein Unterschied, ob dieselbe naturwissenschaftliche Idee, die in Europa als eine Zierde der Naturwissenschaft errungen werden kann und an den Universitäten gilt, in den Gehirnen der Universitätslehrer wächst, oder ob sie wächst in dem Gehirn eines Menschen, der einen Bruder hat, welcher schon als junger Mann, am Ende der achtziger Jahre, als eine Leuchte der Wissenschaft in einem Petersburger Laboratorium gilt, der voller fruchtbarer chemischer Ideen ist, mit einer besonderen Medaille ausgezeichnet, von allen, die mit ihm gearbeitet haben, als junger Mann schon hochverehrt wird - und dieser Bruder ist plötz­[ich nicht mehr da!"
      ],
      [
        "Eben noch von der Universitätsbehörde ausgezeichnet,"
      ],
      [
        "plötzlich nicht mehr da!",
        "Auf allen möglichen Umwegen sollen dann seine Kollegen erfahren haben, daß er mittlerweile ge­henkt worden ist, weil er an Verschwörungen teilgenommen hatte gegen Alexander III., den Reaktionär.",
        "Solche Tatsachen beleuchten die Dinge, die in der Gegenwart spielen, als Lichtblitze.",
        "Es ist nun ein Unterschied, ob dieselbe Idee in das Gehirn eines braven west­europäischen Universitätsprofessors fällt oder in das Gehirn des Bruders dieses unter solchen Voraussetzungen Gehenkten.",
        "Wenn sie in das Gehirn dieses Bruders fällt, dann verwandelt sich dieser Bruder in einen Lenin - denn der Bruder dieses Gehenkten ist Lenin -, und dann wird dieselbe Idee zur Triebkraft von alledem,was Sie jetzt im Osten Europas aufgehen sehen."
      ],
      [
        "Idee ist Idee, wie Weizenkorn Weizenkorn ist, aber man muß er­kennen, ob etwas dieselbe Idee ist und nun auftritt, je nachdem, in dem Gehirn des Universitätsprofessors oder in dem Gehirn des Bruders des dazumal Gehenkten.",
        "Man muß den Willen haben, hineinzu-schauen in diejenigen Untergründe des Daseins, wo die wirklichen Impulse des Geschehens liegen.",
        "Und man muß den Mut haben, abzu­lehnen all das Phrasenzeug von Programmen und Ideen von Wissen­schaftern, die da glauben, wenn sie dies oder jenes vertreten, so komme etwas darauf an.",
        "Vertreten kann man dem Inhalte nach dies oder jenes; doch darauf kommt es an, in welchem Gebiete des leben­digen Lebens dieses also Vertretene ist, so wie es darauf ankommt, in welches Gebiet das Weizenkorn fällt, ob in einen fruchtbaren Boden oder in einen unfruchtbaren Boden.",
        "Den Weg von der Ab­straktion, die unter den heutigen ernsten Verhältnissen überall zur Illusion oder zum Chaos führt, zu der Wirklichkeit, die einzig und allein in der Spiritualität gefunden werden kann, diesen Weg muß auf allen Gebieten die Menschheit suchen.",
        "Und wenn es noch so lange dauert: Auf diesem Wege allein kann die Menschheit das Heil und den Segen aus der gegenwärtigen Verwirrung heraus finden."
      ],
      [
        "Das ist es, was wir uns ins Herz schreiben sollten, worinnen wir uns zusammenfinden sollen.",
        "Das ist es, womit wir uns in einer ernsten Begrüßung begrüßen sollten: in diesem Wissen, dazuzugehören zu dem, was die Gebrechen der Menschheit heilen muß.",
        "Sie sind heilbar,"
      ],
      [
        "aber sie dürfen nicht mit Quacksalbereien geheilt werden wollen.",
        "Sie müssen geheilt werden mit demjenigen, durch dessen Mangel die Menschheit gerade in das Chaos hineingekommen ist."
      ],
      [
        "Niemals hätte im Osten der Leninismus Platz greifen können, wenn nicht im Westen die materialistische Wissenschaft, die manchmal gar nicht sich materialistisch glaubt, gelehrt worden wäre.",
        "Denn was im Osten gemacht wird, ist direkt ein Kind der materialistischen Wissen­schaft.",
        "Ein Wechselbalg ist durch Karl Marx entstanden.",
        "Das wirk­liche Kind der materialistischen Wissenschaft ist schon im Osten vorhanden.",
        "Aber man muß den Willen haben, in alle diese Dinge wirk­lich hineinzuschauen."
      ],
      [
        "Das, meine lieben Freunde, ist gewissermaßen der Hintergrund, auf dem sich nun, ich möchte sagen, abhebt unser Bau.",
        "Und einzelne Menschen hier bei diesem Bau, sie arbeiten, denken an den Bau wahr­haftig recht abseits von den Ideen, die auf so vielen Territorien heute die Menschheit bewegen."
      ],
      [
        "Man kann sich gut denken, daß da draußen auf den andern Territorien viele Menschen sind, die da finden, daß hier Menschen leben, die sich absondern von dem, was heute die Welt bewegt und, wie die Menschen glauben, auch bewegen sollte.",
        "Man könnte sich das denken, daß die Leute vorwurfsvoll an diesen Ort hinsehen."
      ],
      [
        "Diejenigen, die mit ganzem Herzen und ganzer Seele bei diesem Bau sind, brauchen sich aus diesem Vorwurf nichts zu machen.",
        "Denn, möge dieser Bau vielleicht gar nicht seine Aufgabe erfüllen, möge dieser Bau gar nicht sein Ziel erreichen: was an die­sem Bau aber arbeitet und was von denen aus gearbeitet wird, die an diesem Bau mit Hingabe arbeiten, das ist dasjenige, was das Aller­wichtigste ist in der Gegenwart, das ist dasjenige, was die gegenwärtige Menschheit herausführen muß aus alldem, in das sie hineingekommen ist."
      ],
      [
        "Und wenn die Menschen draußen etwa glauben: Hier arbeiten Leute abseits von den Aufgaben der gegenwärtigen Menschheit -, so muß man diesen Leuten sagen können: Hier wird gerade gearbeitet für das Allerwichtigste, für das Allerwesentlichste in der Gegenwart, das nur die andern nicht kennen, wovon die andern noch nichts wis­sen.",
        "Aber davon wird es gerade abhängen, daß die Menschheit werde etwas wissen wollen von dem, was hier geschieht."
      ],
      [
        "Noch einmal sei es betont: Nicht darauf kommt es an, ob dieser Bau sein Ziel erreicht - obgleich es gut wäre, wenn er sein Ziel er­reichen würde -, sondern darauf kommt es an, daß aus gewissen Ideen heraus an diesem Bau gearbeitet worden ist, daß sich Menschen ge­funden haben für das Arbeiten an diesem Bau.",
        "Und nicht der Inhalt dieser Ideen, sondern die Art, wie diese Ideen leben, das ist dasjenige, was die Menschheitsimpulse für die Zukunft sind, während das, woran heute viele glauben, nichts anderes ist als die zum Grabe sich neigen-den, in die Auflösung übergehenden, für die Auflösung auch reifen Ideen der Vorzeit.",
        "Davon wollen wir dann morgen weiter reden."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG Dornach, 18. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Ich möchte heute davon ausgehen, eine Art Skizze zu geben von der menschlichen Seele, so wie diese menschliche Seele in ihrem Verhalten zur Welt und zu sich selbst ist. Ich möchte diese Skizze so halten, daß man etwa sagen kann: Wir sehen uns den Menschen als Seelenwe sen an im Profil. Also, damit wir uns verstehen: Wie wenn wir uns den physischen Menschen - nicht das Seelenwesen - so ansehen würden, daß wir ihn etwa nicht en face, sondern im Profil haben würden, meinetwillen nach rechts hinüberschauend. Betrachten wir ihn einmal",
      "# Bild s. 29",
      "so. Natürlich müssen wir, wenn wir versuchen, so etwas skizzenhaft zu entwerfen, uns immer klar darüber sein, daß wir es mit imagina­tiver Erkenntnis zu tun haben, daß also das Wirkliche, das hinter einer solchen Sache steht, durch ein Bild wiedergegeben ist. Das Bild deutet auf die Sache hin, und man macht ja auch das Bild so, daß es in richtiger",
      "Art auf die Sache hindeutet. Aber natürlich darf man sich eine Zeichnung, eine Skizze, welche darstellen soll ein Seelisch-Geistiges, nicht so denken, wie man sich irgend etwas vorstellt, das in natura­listischer Art eine äußere sinnenfällige Wirklichkeit kopiert. Dessen, was ich jetzt sage, muß man sich schon fortwährend bewußt sein. Ich werde also alles, was den physischen und den niederen ätherischen Organismus des Menschen betrifft, fortlassen, werde nur das Seelische, das Seelisch-Geistige zu skizzieren versuchen (siehe Zeichnung).",
      "Wie Sie ja aus den verschiedenen Darstellungen, die gegeben wor­den sind, wissen, steht dieses Seelisch-Geistige mit der seelisch-geisti­gen Umwelt mehr in einem unmittelbaren Zusammenhang als der physische Mensch mit der physischen Umgebung. Der physische Mensch ist ja gegenüber der physisch-sinnenfälligen Umgebung ein ziemlich abgeschlossenes Wesen. Man möchte sagen: Dieser physisch-sinnliche Mensch ist wirklich auch real in seiner Haut eingeschlossen. -So ist es nicht bei dem, was man als den geistig-seelischen Menschen bezeichnen kann; da muß man sich einen fortdauernden Übergang denken in den Strömungen, die im seelisch-geistigen Inneren des Menschen pulsieren, und in all den Bewegungen und Strömungen, die in der allgemeinen, universellen geistig-seelischen Welt bestehen.",
      "Wollte ich nun zunächst von der einen Seite her charakterisieren, wie dieses Verhältnis des menschlich Geistig-Seelischen zu dem Gei­stig-Seelischen der universellen Umgebung ist, so müßte ich das viel­leicht in der folgenden Weise tun. Ich müßte dasjenige, was aus dem Universum, also aus der Unendlichkeit des Raumes in geistig-seeli­scher Weise hereinkommt, zunächst in dieser Art malen. Eigentlich müßte ich den ganzen Raum so ausmalen, aber das ist ja nicht nötig, ich werde nur dasjenige, was zunächst Umgebung des Menschen ist, ausmalen. Das ist also jetzt dasjenige, was als Umwelt aufzufassen ist (siehe Zeichnung Seite 31, blau). Denken Sie sich also in seelisch-geistiger Bildhaftigkeit das, worin der Mensch hmeingestellt ist. Der Mensch ist ja jetzt noch nicht da, sondern es ist nur das, was aus der Umgebung angrenzt, mit diesem Blau gekennzeichnet. Denken Sie sich das wie ein in sich wogendes blaues Meer, das den Raum aber aus­füllt. Wenn ich sage: Blaues Meer -, ist das natürlich so aufzufassen,",
      "# Bild s. 31",
      "wie ich das öfter in den Büchern, die Ihnen ja vorliegen, charakteri­siert habe, so wie Farben als Bezeichnung des Aurischen, des Seelisch-Geistigen aufzufassen sind.",
      "Schwimmend, möchte ich sagen, oder schwebend getragen, wie eine Woge getragen, ist nun ein anderes Geistig-Seelisches. Das ist dasjenige, welches ich jetzt etwa in der folgenden Weise darstellen müßte. Wir können also, wenn wir von der universellen Umwelt zum",
      "Menschen übergehen, uns und das menschliche Geistig-Seelische etwa wie schwebend auf diesem Rot denken. Da hätten wir zunächst einen Teil des Geistig-Seelischen; davon müßten wir nur, wenn wir etwas der Wirklichkeit gemäß die Skizze machen wollten, den oberen Teil in einem etwas ins Violettliche, ins Lila fallenden Rot geben. Das würde nur richtig gegeben sein, wenn hier oben das Rot sich violett abstumpfte.",
      "Damit habe ich Ihnen zunächst, ich möchte sagen, den einen Pol des Geistig-Seelischen des Menschen gegeben. Den andern Pol be­kommen wir, wenn wir das, was hier an das universell Geistig-Seeli­sche sich anschließend gegen das physische menschiiche Antlitz zu schwimmend-schwebend sich verhält, etwa in der folgenden Weise eingliedern: Gelb, Grün, Orange; Grün geht ins Blaue noch hinein.",
      "Damit haben Sie eine, ich möchte sagen Normalaura des Menschen im Profil, also von der rechten Seite aus gesehen. Ich sage ausdrück­lich: eine Normalaura von der rechten Seite aus gesehen. Dasjenige, was sich dem Schauen so darstellen würde, daß das Schauen eben diese Figur vor sich hätte, das charakterisiert das Hineingestelltsein des Menschen in seine geistig-seelische Umgebung. Es charakterisiert aber auch die Stellung des Menschen, des Seelisch-Geistigen des Men­schen zu sich selber. Man kann, gerade wenn man dasjenige studiert, was durch diese Figur dargestellt ist, so recht sehen, wie der Mensch nach zwei Seiten hin ein begrenztes Wesen ist. Diese zwei Seiten, nach denen hin der Mensch ein begrenztes Wesen ist, die werden im Leben immer bemerkt; allein sie werden nicht richtig gedeutet, sie werden nicht richtig ins Auge gefaßt, werden wenigstens nicht verstanden. Sie wissen ja, daß man in der äußeren Naturwissenschaft davon spricht, daß der Mensch, wenn er die Welt betrachtet, wenn er sich Erkennt­nisse verschaffen will von der Welt, mit seiner Wissenschaft, mit seiner Erkenntnis an bestimmte Grenzen kommt. Wir haben öfter von die­sen Grenzen gesprochen, von diesem berühmten «Ignorabimus» -wir werden niemals wissen -, welches von seiten der Naturforscher, von seiten mancher Philosophen geltend gemacht wird. Man sagt, der Mensch komme eben zu bestimmten Grenzen seines Erkennens, seines Anschauens der Außenwelt. Ich habe Ihnen wohl auch schon",
      "den berühmten Ausspruch angeführt, den Du Bois-Reymond auf der Leipziger Naturforscherversaminlung in den siebziger Jahren getan hat: In die Regiönen hinein, so sagte ungefähr dazumal Du Bois­Reymond, in denen Materie spukt, wird das menschliche Erkennen niemals dringen.",
      "Man würde richtiger über diese Erkenntnisgrenzen des Menschen sprechen, wenn man vielleicht sagen würde: Der Mensch ist genötigt, indem er die Welt betrachtet, gewisse Begriffe sich festzusetzen, welche er mit seinem naturwissenschaftlichen Erkennen, auch mit seinem gewöhnlichen Philosophenerkennen nicht durchdringt. Sie brauchen ja nur zu denken an solche Betrachtungen wie den Begriff des Atoms. Vom Atom redet die Naturwissenschaft. Aber das Atom hat natürlich nur dann einen Sinn, wenn man eigentlich nicht davon reden kann, wenn man nicht sagen kann, was ein Atom ist; denn in dem Augenblicke, wo man anfangen würde, das Atom zu beschreiben, wäre es nicht mehr ein Atom. Es ist ein schlechthin Unnahbares. Und so ist es eigentlich schon die Materie, der Stoff selber. Es müssen ge­wisse Begriffe festgesetzt werden, an die man nicht herankommt. So ist es mit dem Erkennen der Außenwelt. Es müssen Begriffe festge­setzt werden, wie Materie, Kraft und so weiter, an die man nicht herankommt.",
      "Daß solche Begriffe festgesetzt werden müssen, das beruht einfach darauf, daß jenes innerlich geistig-seelisch Leuchtende des Menschen hier nach außen in ein Dunkles hinein sich erstreckt. Das, was da konstatiert wird als Erkenntnisgrenze, das kann man, ich möchte sa­gen, aurisch wirklich richtig sehen. Es liegt hier dem Menschen eine Grenze vor. Das Wesen, das er selbst ist, wird hier dargestellt durch dasjenige, was ich aurisch habe verlaufen lassen als hellgrün ins Blau-violett übergehend (siehe Zeichnung Seite 31>. Aber indem es ins Blauviolette übergeht, ist es nicht mehr der Mensch, da ist es das Universelle der Umgebung. Da gelangt der Mensch mit seinem Wesen, das die innere Kraft seines Anschauens der Welt ist, an eine Grenze, da gelangt er gewissermaßen an das Nichts, und da muß er solche Begriffe, wie Materie, Atom, Stoff, Kraft festsetzen, die keinen Inhalt haben. Das liegt in der menschlichen Organisation, das liegt im Zusammenhange",
      "des Menschen mit dem ganzen Weltenall. Da geht wirk­lich die Verbindung des Menschen mit dem Weltenall vor sich. Man kann, wenn man im Sinne geisteswissenschaftlicher Vorstellung diese Grenze da bezeichnet, das so machen, daß man sagt: Diese Grenze [äßt den Menschen in bezug auf seine Seele in Berührung kommen mit dem Universum. - Man kann, indem man die Richtung nach dem Universum hin mit der einen Schleife einer Lemhiskate bezeichnet, das, was dem Menschen angehört, mit der andern Schleife bezeichnen ;",
      "# Bild s. 34a",
      "nur geht das, was aus dem Menschen herausgeht, in das Universum, in das Unendliche hinein. Man muß daher die Schleifenlinie, die Lemniskate, auf der einen Seite offenlassen, und auf der einen zu­machen, und man muß dann diese Schleifenlinle so zeichnen: Hier ist die Schleifenlinie geschlossen, hier geht sie ins Unendliche hinaus. Es ist dieselbe Linie, die ich dort gezeichnet habe, nur gehen die Schenkel hier ins Unendliche hinaus.",
      "# Bild s. 34b",
      "Was ich hier so zeichne als offene Lemniskate, als offene Schleifen-linie, das ist nicht bloß etwas Ausgedachtes, das ist etwas, was Sie tatsächlich wie ein- und auslaufende Blitze in einer sanften, aber sehr langsamen Bewegung als Ausdruck des Verhältnisses des Menschen zum Universum sehen können. Die Strömungen des Universums nähern sich fortwährend dem Menschen ; er zieht sie an, sie verschlingen",
      "sich in seiner Nähe und gehen wieder heraus. Also es strömt so etwas dem Menschen zu, verschlingt sich, geht wieder heraus. Der Mensch ist von solchen dem Universum angehörenden Strömungen durchsetzt, die sich hier vor ihm aufhalten. Dadurch ist der Mensch, wie Sie sich vorstellen können, von einer Art weibgem Aurischen um­geben ; es kommen diese Strömungen vom Universum herein, machen hier einen Wirbel, grüßen gleichsam den Menschen, indem sie einen Wirbel vor ihm machen, so daß er hier von einer Art aurischer Strö­mung umgeben ist. Das ist wesentlich ein Ausdruck des Verhältnisses des Menschen zum Universum, zur geistig-seelischen Umwelt.",
      "Nun aber können Sie dasjenige, was Sie eigentlich als in Ihrem Be­wußtsein liegend empfinden, hier dargestellt finden als bläulich-grün­lich-gelblich, nach innen zu orange verlaufend. Aber das stößt hier auf; im Inneren des menschlichen Seelischen stößt dieses Gelblich-Orange auf das auf, was auf dem blauen Meere als das Geistig-Seelische des unteren Menschen schwingt, des niederen Menschen. Was ich hier rot und im Übergang ins Orange gezeichnet habe, das gehört zu den unterbewußten Teilen des Menschen, entspricht ja auch denjenigen Vorgängen im Physischen, die sich hauptsächlich als Verdauungs-tätigkeit und Ähnliches abspielen, woran das Bewußtsein keinen An­teil hat. Dasjenige, was mit dem Bewußtsein zusammenhängt, das würde aurisch charakterisiert sein in den hellen Partien, die ich hier",
      "# Bild s. 35",
      "dargestellt habe (siehe Zeichnung Seite 31). So wie hier zusammen­stoßen des Menschen Geistig-Seelisches mit dem Geistig-Seelischen der Umwelt, so stößt nach innen des Menschen Geistig-Seelisches mit seinem Unterbewußten - also auch eigentlich dem Universum ange­hörig - zusammen. Dieses Zusammenstoßen muß ich in den Strö­mungen so zeichnen, daß die einen Strömungen ins Unendliche hinausgehen ; anders muß ich dieses Zusammenstoßen im Inneren des Menschen zeichnen. Da muß ich auch eine Schleifenlinle zeichnen, aber diese muß ich so zeichnen, daß sie nach innen verläuft. Geben Sie acht: Ich zeichne durchaus eine Schieifenlinie, aber ich nehme die untere Schleife und schlage sie um, so daß die Schleifenlinie so wird:",
      "# Bild s. 36",
      "Also ich schlage die untere Schleife um (siehe Zeichnung, rechts). Im Gegensatz zu hier (siehe Zeichnung Seite 35), wo ich die eine Schleife ins Unendliche verlaufen lasse, also ins Unendliche ver-größere, schlage ich nun die untere Schleife um. - Dann habe ich dadurch bildlich bezeichnet die Stauungen, die sich ergeben da, wo das Geistig-Seelische hier innen auf das unterbewußte, als auch univer­selle Geistig-Seelische auftrifft. Ich muß also diese Stauungen, die im Menschen entstehen, wenn ich sie entsprechend denen hier zeichne, in dieser Weise charakterisieren (sieben Leruniskaten mit umgeschla­gener Schleife). Das sind die Stauungen, welche entsprechen einer inneren Welle im Menschen.",
      "Wenn Sie diese innere Welle tatsächlich verfolgen wollten, so würde die Hauptrichtung dieser Welle - aber eben nur die Hauptrichtung -etwa so verlaufen, daß sie entlangliefe dem Zusammenstoßen von den, wie Sie wissen, unrichtig benannten, aber sogenannten sensitiven und motorischen Nerven im Menschen. Das nur nebenbei gesagt, denn ich will heute hauptsächlich das Geistig-Seelische der Sache erörtern.",
      "# Bild s. 37",
      "Sie sehen daran den starken Gegensatz, der besteht in dem Verhält­nis des Menschen zur geistig-seelischen Umwelt und zu sich selber, zu dem Stück, das er aus der geistig-seelischen Umwelt als sein Unter-bewußtes hereinnimmt, und das ich hier durch die rötliche Woge, die auf dem allgemeinen blauen Meere des geistig-seelischen Universums schwimmt, zu skizzieren gehabt habe.",
      "Wir haben gesagt, daß diese Welle hier (siehe Zeichnung Seite 31, rechts) gewissermaßen der Schranke entspricht, auf die der Mensch aufstößt, wenn er die Außenwelt erkennen will. Aber auch hier (links) ist eine Schranke ; im Inneren des Menschen selbst ist eine Schranke. Wäre diese Schranke nicht vorhanden, dann würden Sie immer in Ihr Inneres hinuntersehen. Jeder Mensch würde in sein Inneres hinunter-schauen. So wie, wenn diese Schranke (rechts) nicht vorhanden wäre, der Mensch in die Außenwelt hineinschauen würde, so würde er, wenn diese Schranke (links) nicht vorhanden wäre, in sein Inneres hinunterschauen. Er würde allerdings, so wie der Mensch im gegen­wärtigen Bntwickelungszyklus einmal ist, wenn er so in sein Inneres hinunterschauen würde, wenig Freude haben über dieses sein Inneres, weil das, was er da sehen würde, ein höchst unvollkommenes, chaoti­sches, brodelndes Gewoge der inneren Menschennatur ist, etwas, wor­über der Mensch keine große Freude haben könnte ; aber es ist das­jenige, in welches die phantastischen Mystiker glauben hinunterschauen",
      "zu können, wenn sie von Mystik sprechen. Dasjenige, was sehr häufig von phantastischen Mystikern als das Erstrebenswerte an­gesehen wird, was namentlich bei sehr vielen solchen Mystikern -ich habe sie im Vorjahre charakterisiert -, die wirklich glauben, indem sie in ihr Inneres schauen, das Universum erkennen zu können, als Mystik figuriert, das ist beim Menschen gerade durch diese Stauwelle zugedeckt, richtig zugedeckt.",
      "Der Mensch kann nicht in sein Inneres hinuterschauen. Dasjenige, was sich hier innerhalb dieser Region bildet (links), das staut sich und spiegelt sich, kann sich wenigstens in sich selbst zurückspiegeln, und die Erscheinung dieses Zurückspiegelns, das ist die Erinnerung, das Gedächtnis.",
      "Jedesmal, wenn ein Gedanke oder ein Eindruck, den Sie gefaßt haben, wiederum zurückkommt in der Erinnerung, so kommt er dadurch zurück, daß diese Stauung hier zu funktionieren beginnt. Wenn Sie diese Stauwelle nicht hätten, so würde jeder Eindruck, den Sie von außen bekommen, jeder Gedanke, den Sie fassen, durch Sie hindurchgehen, nicht in Ihnen bleiben kön­nen und in das übrige geistig-seelische Universum hineingehen.",
      "Nur dadurch halten Sie die Eindrücke auf, die Sie empfangen, daß Sie diese Stauwelle haben. Dadurch sind Sie aber imstande, durch ge­wisse Vorgänge, die wir noch charakterisieren werden, die Eindrücke wiederum zurückzubekommen.",
      "Und das drückt sich aus im Funk­tionieren des Gedächtnisses, im Funktionieren der Erinnerung. Sie können sich also vorstellen, daß Sie in sich etwas haben wie eine Tafel, was hier im Profil gezeichnet ist - denn es ist ja im Profil gezeichnet, nicht wahr, es ist solch eine Ebene, die in Ihnen ist -, da wird zurück­geschlagen dasjenige, was nicht durchgehen soll.",
      "Sie bleiben, wenn Sie wachend sind, mit der Außenwelt vereint, sonst würde alles in wachem Zustande durch Sie durchgehen. Sie würden eigentlich von den Eindrücken nichts wissen, Sie würden die Eindrücke bekommen, aber könnten sie gar nicht festhalten.",
      "Das ist also dasjenige, was auf die Erinnerung deutet. Und das, was gewissermaßen als die Fläche dieser Stauwelle unsere Erinnerung bewirkt, deckt dasjenige zu, was der phantastische Mystiker gern in sich sehen möchte. Was da drunten ist, davon könnte man schon sagen: Für den, der die Dinge wirklich kennt, gilt das Wort: Der",
      "Mensch «begehre nimmer und nimmer zu schauen, was sie [die Götter] gnädig bedecken mit Nacht und Grauen». - Doch die Mystiker sind phantastisch und wollen da hinunterschauen. Aber sie können es ja ohnedies nicht, weil sie das normale Bewußtsein so durchlöchern, so korrumpieren würden, daß sich die Gedächtniswelle nicht zurück­schlüge. Dasselbe, was unsere Erinnerung ausmacht, was wir so not­wendig brauchen zum äußeren Leben, das bedeckt uns dasjenige, was die phantastischen Mystiker wohl schauen möchten, was aber der Mensch nicht schauen soll. Unter Ihrem Gedächtnis, unter Ihrer Gedächtnisursache, unter Ihrer Gedächtnisfläche liegt etwas Wesen­haftes vom Menschen. Aber geradeso wie die Hinterwand eines Spie­gels, wie der Belag eines Spiegels das, was vorn ist, zurückwirft, so geht, was also in Ihrem Bewußtsein ist, nicht da hinten hin ; das wird wieder zurückgeworfen und kann deshalb fortwährend als Erinnerung da sein. So kann überhaupt unser ganzes Leben sich als Erinnerung spiegeln. Und im wesentlichen ist ja dasjenige, was wir das Leben unseres Ich nennen, das Spiegeln dieser Erinnerung.",
      "Sie sehen also, unser bewußtes Leben leben wir eigentlich zwischen dieser Welle hier (rechts) und zwischen dieser Welle (links>. Wir wären also Schläuche, die alles durch sich hindurchlassen, wenn wir nicht diese Stauwelle hätten, die der Erinnerung zugrunde liegt, und wir sähen in die Geheimnisse jenseits der Erkenntnisgrenze hinein, wenn wir nicht genötigt wären, außerhalb des Gebietes des Sinnen-fälligen Begriffe zu setzen, für die wir keinen Inhalt mehr haben. Wären wir so organisiert, daß wir diese Stauung hier nicht erzeugen könnten, so würden wir Schläuche sein. Wären wir so organisiert, daß wir nicht genötigt wären, diese gewissermaßen unausgefüllten Be­griffe, diese dunklen Begriffe vor uns hinzusetzen, so wären wir liebe-leere und liebelose Wesen ; steinerne Naturen wären wir, trockene Naturen. Wir könnten nichts in der Welt gern haben, wir wären alle Mephistopelesnaturen.",
      "Daß wir so organisiert sind, daß wir an gewisses Geistig-Seelisches unserer Umgebung nicht herankommen können mit unseren abstrak­ten Begriffen, mit unserem Fassungsvermögen, das bewirkt, daß wir lieben können. Denn was wir lieben sollen, an das sollen wir nicht so",
      "herankommen, daß wir es analysieren im gewöhnlichen Sinne des Wortes, daß wir es zergliedern, daß wir es behandeln wie der Chemi­ker im Laboratorium die chemischen Stoffe. Man liebt ja nicht, wenn man chemisch analysiert oder chemisch synthetisiert. Erinnerungs-fähigkeit, Liebefähigkeit, das sind die zwei Fähigkeiten, die zugleich entsprechen zwei Grenzen der menschiichen Natur. Der einen Grenze nach innen entspricht die Erinnerungsfähigkeit ; was jenseits der Er­innerungszone liegt, ist unterbewußtes menschliches Innere. Die andere Zone entspricht der Kraft der Liebefähigkeit ; was jenseits dieser Zone liegt, entspricht dem Geistig-Seelischen des Universums. Das Unbewußte der menschlichen Natur liegt also jenseits dieser Zone, soweit das menschliche Innere reicht ; das Geistig-Seelische des Uni­versums geht unbegrenzt in die Weiten hinaus von der andern Zone an.",
      "Wir können also sprechen von Liebezone, von Erinnerungszone und können dasjenige, was das menschlich Geistig-Seelische ist, inner­halb dieser Zonen einschließen ; müssen aber jenseits der einen Zone da drüben (siehe Zeichnung Seite 31, links) dasjenige suchen, was un­bewußt bleibt, und was deshalb, weil es unbewußt bleibt, gerade sehr stark zusammenhängt mit der menschiichen Körperlichkeit, mit den körperlichen Verrichtungen. Natürlich sind die Dinge in der Wirk­lichkeit nicht so einfach, wie man sie darstellen muß, weil alles inein­andergreift. Das, was hier rot ist (siehe Zeichnung Seite 31), das greift in Dinge hinein, das verändert sich ; und wiederum dasjenige, was grün und blau ist, das verändert sich auch. In der Wirklichkeit greifen die Dinge alle ineinander ein. Aber trotzdem ist in der Hauptsache die skizzenhafte Zeichnung richtig und entspricht den Tatsachen.",
      "Daraus aber ersehen Sie, daß für das physische Leben auf der Erde hier ein starkes, bewußtes Geistiges ist. Hier (links) ist ein unbewußtes Geistiges, das eigentlich mit dem Universum zusammen verschwimmt. Diese zwei Stücke des Menschen unterscheiden sich sehr deutlich von­einander. Dieses Geistige (in der Mitte), das ist daher zunächst für das irdische Leben ein solches, das sehr fein gewoben ist. Wie fein gewo­benes Licht, möchte ich sagen, ist alles hier (gelb). Würde ich am Menschen zu zeigen haben, wo dieses fein gewobene Licht ist, so würde in das hinein, was ich jetzt umfassend so umschreibe, das",
      "menschliche Haupt fallen. Also was ich so umschrieben habe, was ich dorthin als das Gelbe, Gelb-Grünliche, Gelb-Orange nach der andern Seite gezeichnet habe, das ist fein gewobenes, wenn ich so sagen darf, Geistlicht.",
      "Das hat keine starke Verwandtschaft mit der irdischen Materie ; das hat eine möglichst geringe Verwandtschaft mit der irdi­schen Materie. Deshalb, weil es wenig Verwandtschaft hat, kann es auch nicht mit der Materie sich gut verbinden, und so bleibt es zum großen Teile unverbunden mit der Materie ; es wird diesem Teil ge­geben eine solche Materie, die eigentlich immer jeweils aus der vori­gen Inkarnation des Menschen stammt.",
      "Das Haupt, das, was das menschliche. Haupt formt, die Formungskräfte des menschlichen Hauptes, das wird im wesentlichen hereingetragen aus der vorigen Inkarnation, und da ist nur eine lose Verbindung zwischen diesem feingewobenen Geistig-Seelischen und dem Körperhaften, das eigent­lich von der vorigen Inkarnation zusammengehalten wird.",
      "Ihre Phy­siognomie tragen Sie ja eigentlich nach Ihren Verrichtungen und Eigenschaften in der vorigen Inkarnation. Und derjenige, der sich gut versteht auf Deutungen von Menschen, der sieht gerade durch das Physiognomische des Hauptes hindurch; nicht durch dasjenige, was von dem luziferischen Inneren stammt, sondern mehr durch die An­passung an das Universum.",
      "Man muß ja die Physiognomie so sehen, als wenn sie in den Menschen hineingedrückt wäre. Nicht so sehr, als ob sie herausginge, sondern man muß gewissermaßen das Negativ des Seelischen sehen ; das sieht man in diesem Negativ des Gesichts.",
      "Wenn Sie einen Abdruck machen würden von jedem Gesicht, da würden Sie eigentlich die Physiognomie sehen, die ein furchtbar starker Verräter ist desjenigen, was Sie in der vorigen Inkarnation angestellt haben. Dagegen ist alles, was ich da unten wie nur zusammenhängend mit dem wogenden Meere des Geistig-Seelischen der Welt skizziert habe, was so aufzufassen ist, daß es des Menschen Unterbewußtem oder Unbewußtem entspricht, stark verwandt mit der Körperlichkeit ; das durchsetzt die Körperlichkeit.",
      "Diese Körperlichkeit, die verbindet sich so mit dem Geistigen, daß das Geistige als Geistiges gar nicht erscheinen kann. Daher würde man, wenn man hinunterschaute, dieses Ineinanderbrod ein von Geistigem und Leiblichem schauen, was hinter",
      "der Schwelle der Erinnerung liegt. Das ist das, was vorbereitet das Haupt der nächsten Inkarnation, das ist das, was sich metamorpho­sieren will zu dem, was in der Zukunft erst feste materielle Form be­kommt, erst Haupt sein wird in der nächsten Inkarnation. Denn das Haupt des Menschen ist ein über das Maß seiner Entwickelung Hinaus-geschrittenes. Daher ist das Haupt - wie Sie sich erinnern aus den früheren Vorträgen, die ich hier gehalten habe - eigentlich mit dem siebenundzwanzigsten, achtundzwanzigsten Jahre des Menschen in seiner Entwickelung schon abgeschlossen. Da ist schon Überbildung des Menschen, in der Hauptesform.",
      "Aber der übrige Mensch, der ist auch ein Haupt, so sonderbar das aussieht ; nur ist er noch nicht so weit als das Haupt. Wenn Sie sich den Menschen geköpft denken, so ist das, was übrigbleibt, auch ein Haupt des Menschen, aber auf einer noch sehr zurückgebliebenen Stufe. Wenn es sich weitet entwickelt, dann wird es auch Haupt, während das, was Sie als Haupt des Menschen haben, der übrige Organismus gewesen ist in früherer Inkarnation. Wenn Sie dann dasjenige entleiblicht sich denken, vom Leibe befreit, was in Ihrem gegenwärtigen Organismus noch nicht Haupt ist, wenn Sie sich also das Haupt wegdenken vom gegenwärtigen Organismus, der erst in der nächsten Inkarnation Haupt wird - aber dieser Ihr Organismus ist ja ein Abbild, alles Physische ist ein Abbild eines Geistigen -, wenn Sie sich dafür das Geistige denken, was also in seiner äußeren Form nicht bis zum Men­schen vorgeschritten ist: da sehen Sie es sich nun an unserer luziferi­schen Figur bei der Gruppe drüben an, da haben Sie es!",
      "Und jetzt denken Sie sich all das Geistig-Seelische, das bei Ihnen zurückgehalten ist von Ihrem Haupte, in den Menschen hineingefügt, also all das, was beim Menschen eine Grenze ist, was er nicht durch­dringen kann (rechts, siehe Zeichnung Seite 31), in den menschlichen Kopf hineingepreßt: dann wird der Mensch nicht nur ein so altes, ehrwürdiges Haupt haben, wie er es ohnedies schon hat, sondern er wird ein ganz verknöchertes Haupt haben, wird überhaupt ganz ver­knöchern, wie die Ahrimanfigur bei unserer Gruppe drüben.",
      "Wenn Sie sich also dasjenige, was hier unter der Erinnerungsgrenze ist, ausgegossen denken über das Innere des Menschen, bekommen Sie",
      "alles Luziferische. Wenn Sie sich alles dasjenige, was jenseits dieser Stauwelle ist (rechts), hereinergossen denken in die menschliche Figur, bekommen Sie die ahrimanische Form. Und der Mensch ist zwischen beiden.",
      "Was ich Ihnen da auseinandergesetzt habe, das hat nicht nur eine große Bedeutung für das Verständnis des Menschen, sondern das hat auch eine große Bedeutung für das Verständnis der geistigen Vor­gänge in der Menschheitsentwickelung. Man versteht nicht, wie das Christentum und der Christus-Impuls in die Menschheitsentwickelung hereingekommen ist, wenn man nicht gründlich diese Dinge versteht. Man versteht auch nicht, welche Funktionen die katholische Kirche hatte, welche Funktionen Jesuitismus und ähnliche Strömungen ha­ben, welche Osttum und Westtum haben, wenn man sie nicht im Zu­sammenhange betrachten kann mit diesen Dingen.",
      "Über diese Strömungen, die eigentlich richtig erst verstanden wer­den können, wenn man diese Grundlagen des geistig-seelischen Men­schen sich einmal anschaulich vor das Auge führt, Ost-, Westtum, Jesuitismus, Amerikanismus und so weiter, werde ich mir morgen erlauben, ein weniges zu sprechen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Ich möchte heute davon ausgehen, eine Art Skizze zu geben von der menschlichen Seele, so wie diese menschliche Seele in ihrem Verhalten zur Welt und zu sich selbst ist.",
        "Ich möchte diese Skizze so halten, daß man etwa sagen kann: Wir sehen uns den Menschen als Seelenwe sen an im Profil.",
        "Also, damit wir uns verstehen: Wie wenn wir uns den physischen Menschen - nicht das Seelenwesen - so ansehen würden, daß wir ihn etwa nicht en face, sondern im Profil haben würden, meinetwillen nach rechts hinüberschauend.",
        "Betrachten wir ihn einmal"
      ],
      [
        "# Bild s. 29"
      ],
      [
        "Natürlich müssen wir, wenn wir versuchen, so etwas skizzenhaft zu entwerfen, uns immer klar darüber sein, daß wir es mit imagina­tiver Erkenntnis zu tun haben, daß also das Wirkliche, das hinter einer solchen Sache steht, durch ein Bild wiedergegeben ist.",
        "Das Bild deutet auf die Sache hin, und man macht ja auch das Bild so, daß es in richtiger"
      ],
      [
        "Art auf die Sache hindeutet.",
        "Aber natürlich darf man sich eine Zeichnung, eine Skizze, welche darstellen soll ein Seelisch-Geistiges, nicht so denken, wie man sich irgend etwas vorstellt, das in natura­listischer Art eine äußere sinnenfällige Wirklichkeit kopiert.",
        "Dessen, was ich jetzt sage, muß man sich schon fortwährend bewußt sein.",
        "Ich werde also alles, was den physischen und den niederen ätherischen Organismus des Menschen betrifft, fortlassen, werde nur das Seelische, das Seelisch-Geistige zu skizzieren versuchen (siehe Zeichnung)."
      ],
      [
        "Wie Sie ja aus den verschiedenen Darstellungen, die gegeben wor­den sind, wissen, steht dieses Seelisch-Geistige mit der seelisch-geisti­gen Umwelt mehr in einem unmittelbaren Zusammenhang als der physische Mensch mit der physischen Umgebung.",
        "Der physische Mensch ist ja gegenüber der physisch-sinnenfälligen Umgebung ein ziemlich abgeschlossenes Wesen.",
        "Man möchte sagen: Dieser physisch-sinnliche Mensch ist wirklich auch real in seiner Haut eingeschlossen. -So ist es nicht bei dem, was man als den geistig-seelischen Menschen bezeichnen kann; da muß man sich einen fortdauernden Übergang denken in den Strömungen, die im seelisch-geistigen Inneren des Menschen pulsieren, und in all den Bewegungen und Strömungen, die in der allgemeinen, universellen geistig-seelischen Welt bestehen."
      ],
      [
        "Wollte ich nun zunächst von der einen Seite her charakterisieren, wie dieses Verhältnis des menschlich Geistig-Seelischen zu dem Gei­stig-Seelischen der universellen Umgebung ist, so müßte ich das viel­leicht in der folgenden Weise tun.",
        "Ich müßte dasjenige, was aus dem Universum, also aus der Unendlichkeit des Raumes in geistig-seeli­scher Weise hereinkommt, zunächst in dieser Art malen.",
        "Eigentlich müßte ich den ganzen Raum so ausmalen, aber das ist ja nicht nötig, ich werde nur dasjenige, was zunächst Umgebung des Menschen ist, ausmalen.",
        "Das ist also jetzt dasjenige, was als Umwelt aufzufassen ist (siehe Zeichnung Seite 31, blau).",
        "Denken Sie sich also in seelisch-geistiger Bildhaftigkeit das, worin der Mensch hmeingestellt ist.",
        "Der Mensch ist ja jetzt noch nicht da, sondern es ist nur das, was aus der Umgebung angrenzt, mit diesem Blau gekennzeichnet.",
        "Denken Sie sich das wie ein in sich wogendes blaues Meer, das den Raum aber aus­füllt.",
        "Wenn ich sage: Blaues Meer -, ist das natürlich so aufzufassen,"
      ],
      [
        "# Bild s. 31"
      ],
      [
        "wie ich das öfter in den Büchern, die Ihnen ja vorliegen, charakteri­siert habe, so wie Farben als Bezeichnung des Aurischen, des Seelisch-Geistigen aufzufassen sind."
      ],
      [
        "Schwimmend, möchte ich sagen, oder schwebend getragen, wie eine Woge getragen, ist nun ein anderes Geistig-Seelisches.",
        "Das ist dasjenige, welches ich jetzt etwa in der folgenden Weise darstellen müßte.",
        "Wir können also, wenn wir von der universellen Umwelt zum"
      ],
      [
        "Menschen übergehen, uns und das menschliche Geistig-Seelische etwa wie schwebend auf diesem Rot denken.",
        "Da hätten wir zunächst einen Teil des Geistig-Seelischen; davon müßten wir nur, wenn wir etwas der Wirklichkeit gemäß die Skizze machen wollten, den oberen Teil in einem etwas ins Violettliche, ins Lila fallenden Rot geben.",
        "Das würde nur richtig gegeben sein, wenn hier oben das Rot sich violett abstumpfte."
      ],
      [
        "Damit habe ich Ihnen zunächst, ich möchte sagen, den einen Pol des Geistig-Seelischen des Menschen gegeben.",
        "Den andern Pol be­kommen wir, wenn wir das, was hier an das universell Geistig-Seeli­sche sich anschließend gegen das physische menschiiche Antlitz zu schwimmend-schwebend sich verhält, etwa in der folgenden Weise eingliedern: Gelb, Grün, Orange; Grün geht ins Blaue noch hinein."
      ],
      [
        "Damit haben Sie eine, ich möchte sagen Normalaura des Menschen im Profil, also von der rechten Seite aus gesehen.",
        "Ich sage ausdrück­lich: eine Normalaura von der rechten Seite aus gesehen.",
        "Dasjenige, was sich dem Schauen so darstellen würde, daß das Schauen eben diese Figur vor sich hätte, das charakterisiert das Hineingestelltsein des Menschen in seine geistig-seelische Umgebung.",
        "Es charakterisiert aber auch die Stellung des Menschen, des Seelisch-Geistigen des Men­schen zu sich selber.",
        "Man kann, gerade wenn man dasjenige studiert, was durch diese Figur dargestellt ist, so recht sehen, wie der Mensch nach zwei Seiten hin ein begrenztes Wesen ist.",
        "Diese zwei Seiten, nach denen hin der Mensch ein begrenztes Wesen ist, die werden im Leben immer bemerkt; allein sie werden nicht richtig gedeutet, sie werden nicht richtig ins Auge gefaßt, werden wenigstens nicht verstanden.",
        "Sie wissen ja, daß man in der äußeren Naturwissenschaft davon spricht, daß der Mensch, wenn er die Welt betrachtet, wenn er sich Erkennt­nisse verschaffen will von der Welt, mit seiner Wissenschaft, mit seiner Erkenntnis an bestimmte Grenzen kommt.",
        "Wir haben öfter von die­sen Grenzen gesprochen, von diesem berühmten «Ignorabimus» -wir werden niemals wissen -, welches von seiten der Naturforscher, von seiten mancher Philosophen geltend gemacht wird.",
        "Man sagt, der Mensch komme eben zu bestimmten Grenzen seines Erkennens, seines Anschauens der Außenwelt.",
        "Ich habe Ihnen wohl auch schon"
      ],
      [
        "den berühmten Ausspruch angeführt, den Du Bois-Reymond auf der Leipziger Naturforscherversaminlung in den siebziger Jahren getan hat: In die Regiönen hinein, so sagte ungefähr dazumal Du Bois­Reymond, in denen Materie spukt, wird das menschliche Erkennen niemals dringen."
      ],
      [
        "Man würde richtiger über diese Erkenntnisgrenzen des Menschen sprechen, wenn man vielleicht sagen würde: Der Mensch ist genötigt, indem er die Welt betrachtet, gewisse Begriffe sich festzusetzen, welche er mit seinem naturwissenschaftlichen Erkennen, auch mit seinem gewöhnlichen Philosophenerkennen nicht durchdringt.",
        "Sie brauchen ja nur zu denken an solche Betrachtungen wie den Begriff des Atoms.",
        "Vom Atom redet die Naturwissenschaft.",
        "Aber das Atom hat natürlich nur dann einen Sinn, wenn man eigentlich nicht davon reden kann, wenn man nicht sagen kann, was ein Atom ist; denn in dem Augenblicke, wo man anfangen würde, das Atom zu beschreiben, wäre es nicht mehr ein Atom.",
        "Es ist ein schlechthin Unnahbares.",
        "Und so ist es eigentlich schon die Materie, der Stoff selber.",
        "Es müssen ge­wisse Begriffe festgesetzt werden, an die man nicht herankommt.",
        "So ist es mit dem Erkennen der Außenwelt.",
        "Es müssen Begriffe festge­setzt werden, wie Materie, Kraft und so weiter, an die man nicht herankommt."
      ],
      [
        "Daß solche Begriffe festgesetzt werden müssen, das beruht einfach darauf, daß jenes innerlich geistig-seelisch Leuchtende des Menschen hier nach außen in ein Dunkles hinein sich erstreckt.",
        "Das, was da konstatiert wird als Erkenntnisgrenze, das kann man, ich möchte sa­gen, aurisch wirklich richtig sehen.",
        "Es liegt hier dem Menschen eine Grenze vor.",
        "Das Wesen, das er selbst ist, wird hier dargestellt durch dasjenige, was ich aurisch habe verlaufen lassen als hellgrün ins Blau-violett übergehend (siehe Zeichnung Seite 31>.",
        "Aber indem es ins Blauviolette übergeht, ist es nicht mehr der Mensch, da ist es das Universelle der Umgebung.",
        "Da gelangt der Mensch mit seinem Wesen, das die innere Kraft seines Anschauens der Welt ist, an eine Grenze, da gelangt er gewissermaßen an das Nichts, und da muß er solche Begriffe, wie Materie, Atom, Stoff, Kraft festsetzen, die keinen Inhalt haben.",
        "Das liegt in der menschlichen Organisation, das liegt im Zusammenhange"
      ],
      [
        "des Menschen mit dem ganzen Weltenall.",
        "Da geht wirk­lich die Verbindung des Menschen mit dem Weltenall vor sich.",
        "Man kann, wenn man im Sinne geisteswissenschaftlicher Vorstellung diese Grenze da bezeichnet, das so machen, daß man sagt: Diese Grenze [äßt den Menschen in bezug auf seine Seele in Berührung kommen mit dem Universum. - Man kann, indem man die Richtung nach dem Universum hin mit der einen Schleife einer Lemhiskate bezeichnet, das, was dem Menschen angehört, mit der andern Schleife bezeichnen ;"
      ],
      [
        "# Bild s. 34a"
      ],
      [
        "nur geht das, was aus dem Menschen herausgeht, in das Universum, in das Unendliche hinein.",
        "Man muß daher die Schleifenlinie, die Lemniskate, auf der einen Seite offenlassen, und auf der einen zu­machen, und man muß dann diese Schleifenlinle so zeichnen: Hier ist die Schleifenlinie geschlossen, hier geht sie ins Unendliche hinaus.",
        "Es ist dieselbe Linie, die ich dort gezeichnet habe, nur gehen die Schenkel hier ins Unendliche hinaus."
      ],
      [
        "# Bild s. 34b"
      ],
      [
        "Was ich hier so zeichne als offene Lemniskate, als offene Schleifen-linie, das ist nicht bloß etwas Ausgedachtes, das ist etwas, was Sie tatsächlich wie ein- und auslaufende Blitze in einer sanften, aber sehr langsamen Bewegung als Ausdruck des Verhältnisses des Menschen zum Universum sehen können.",
        "Die Strömungen des Universums nähern sich fortwährend dem Menschen ; er zieht sie an, sie verschlingen"
      ],
      [
        "sich in seiner Nähe und gehen wieder heraus.",
        "Also es strömt so etwas dem Menschen zu, verschlingt sich, geht wieder heraus.",
        "Der Mensch ist von solchen dem Universum angehörenden Strömungen durchsetzt, die sich hier vor ihm aufhalten.",
        "Dadurch ist der Mensch, wie Sie sich vorstellen können, von einer Art weibgem Aurischen um­geben ; es kommen diese Strömungen vom Universum herein, machen hier einen Wirbel, grüßen gleichsam den Menschen, indem sie einen Wirbel vor ihm machen, so daß er hier von einer Art aurischer Strö­mung umgeben ist.",
        "Das ist wesentlich ein Ausdruck des Verhältnisses des Menschen zum Universum, zur geistig-seelischen Umwelt."
      ],
      [
        "Nun aber können Sie dasjenige, was Sie eigentlich als in Ihrem Be­wußtsein liegend empfinden, hier dargestellt finden als bläulich-grün­lich-gelblich, nach innen zu orange verlaufend.",
        "Aber das stößt hier auf; im Inneren des menschlichen Seelischen stößt dieses Gelblich-Orange auf das auf, was auf dem blauen Meere als das Geistig-Seelische des unteren Menschen schwingt, des niederen Menschen.",
        "Was ich hier rot und im Übergang ins Orange gezeichnet habe, das gehört zu den unterbewußten Teilen des Menschen, entspricht ja auch denjenigen Vorgängen im Physischen, die sich hauptsächlich als Verdauungs-tätigkeit und Ähnliches abspielen, woran das Bewußtsein keinen An­teil hat.",
        "Dasjenige, was mit dem Bewußtsein zusammenhängt, das würde aurisch charakterisiert sein in den hellen Partien, die ich hier"
      ],
      [
        "# Bild s. 35"
      ],
      [
        "dargestellt habe (siehe Zeichnung Seite 31).",
        "So wie hier zusammen­stoßen des Menschen Geistig-Seelisches mit dem Geistig-Seelischen der Umwelt, so stößt nach innen des Menschen Geistig-Seelisches mit seinem Unterbewußten - also auch eigentlich dem Universum ange­hörig - zusammen.",
        "Dieses Zusammenstoßen muß ich in den Strö­mungen so zeichnen, daß die einen Strömungen ins Unendliche hinausgehen ; anders muß ich dieses Zusammenstoßen im Inneren des Menschen zeichnen.",
        "Da muß ich auch eine Schleifenlinle zeichnen, aber diese muß ich so zeichnen, daß sie nach innen verläuft.",
        "Geben Sie acht: Ich zeichne durchaus eine Schieifenlinie, aber ich nehme die untere Schleife und schlage sie um, so daß die Schleifenlinie so wird:"
      ],
      [
        "# Bild s. 36"
      ],
      [
        "Also ich schlage die untere Schleife um (siehe Zeichnung, rechts).",
        "Im Gegensatz zu hier (siehe Zeichnung Seite 35), wo ich die eine Schleife ins Unendliche verlaufen lasse, also ins Unendliche ver-größere, schlage ich nun die untere Schleife um. - Dann habe ich dadurch bildlich bezeichnet die Stauungen, die sich ergeben da, wo das Geistig-Seelische hier innen auf das unterbewußte, als auch univer­selle Geistig-Seelische auftrifft.",
        "Ich muß also diese Stauungen, die im Menschen entstehen, wenn ich sie entsprechend denen hier zeichne, in dieser Weise charakterisieren (sieben Leruniskaten mit umgeschla­gener Schleife).",
        "Das sind die Stauungen, welche entsprechen einer inneren Welle im Menschen."
      ],
      [
        "Wenn Sie diese innere Welle tatsächlich verfolgen wollten, so würde die Hauptrichtung dieser Welle - aber eben nur die Hauptrichtung -etwa so verlaufen, daß sie entlangliefe dem Zusammenstoßen von den, wie Sie wissen, unrichtig benannten, aber sogenannten sensitiven und motorischen Nerven im Menschen.",
        "Das nur nebenbei gesagt, denn ich will heute hauptsächlich das Geistig-Seelische der Sache erörtern."
      ],
      [
        "# Bild s. 37"
      ],
      [
        "Sie sehen daran den starken Gegensatz, der besteht in dem Verhält­nis des Menschen zur geistig-seelischen Umwelt und zu sich selber, zu dem Stück, das er aus der geistig-seelischen Umwelt als sein Unter-bewußtes hereinnimmt, und das ich hier durch die rötliche Woge, die auf dem allgemeinen blauen Meere des geistig-seelischen Universums schwimmt, zu skizzieren gehabt habe."
      ],
      [
        "Wir haben gesagt, daß diese Welle hier (siehe Zeichnung Seite 31, rechts) gewissermaßen der Schranke entspricht, auf die der Mensch aufstößt, wenn er die Außenwelt erkennen will.",
        "Aber auch hier (links) ist eine Schranke ; im Inneren des Menschen selbst ist eine Schranke.",
        "Wäre diese Schranke nicht vorhanden, dann würden Sie immer in Ihr Inneres hinuntersehen.",
        "Jeder Mensch würde in sein Inneres hinunter-schauen.",
        "So wie, wenn diese Schranke (rechts) nicht vorhanden wäre, der Mensch in die Außenwelt hineinschauen würde, so würde er, wenn diese Schranke (links) nicht vorhanden wäre, in sein Inneres hinunterschauen.",
        "Er würde allerdings, so wie der Mensch im gegen­wärtigen Bntwickelungszyklus einmal ist, wenn er so in sein Inneres hinunterschauen würde, wenig Freude haben über dieses sein Inneres, weil das, was er da sehen würde, ein höchst unvollkommenes, chaoti­sches, brodelndes Gewoge der inneren Menschennatur ist, etwas, wor­über der Mensch keine große Freude haben könnte ; aber es ist das­jenige, in welches die phantastischen Mystiker glauben hinunterschauen"
      ],
      [
        "zu können, wenn sie von Mystik sprechen.",
        "Dasjenige, was sehr häufig von phantastischen Mystikern als das Erstrebenswerte an­gesehen wird, was namentlich bei sehr vielen solchen Mystikern -ich habe sie im Vorjahre charakterisiert -, die wirklich glauben, indem sie in ihr Inneres schauen, das Universum erkennen zu können, als Mystik figuriert, das ist beim Menschen gerade durch diese Stauwelle zugedeckt, richtig zugedeckt."
      ],
      [
        "Der Mensch kann nicht in sein Inneres hinuterschauen.",
        "Dasjenige, was sich hier innerhalb dieser Region bildet (links), das staut sich und spiegelt sich, kann sich wenigstens in sich selbst zurückspiegeln, und die Erscheinung dieses Zurückspiegelns, das ist die Erinnerung, das Gedächtnis."
      ],
      [
        "Jedesmal, wenn ein Gedanke oder ein Eindruck, den Sie gefaßt haben, wiederum zurückkommt in der Erinnerung, so kommt er dadurch zurück, daß diese Stauung hier zu funktionieren beginnt.",
        "Wenn Sie diese Stauwelle nicht hätten, so würde jeder Eindruck, den Sie von außen bekommen, jeder Gedanke, den Sie fassen, durch Sie hindurchgehen, nicht in Ihnen bleiben kön­nen und in das übrige geistig-seelische Universum hineingehen."
      ],
      [
        "Nur dadurch halten Sie die Eindrücke auf, die Sie empfangen, daß Sie diese Stauwelle haben.",
        "Dadurch sind Sie aber imstande, durch ge­wisse Vorgänge, die wir noch charakterisieren werden, die Eindrücke wiederum zurückzubekommen."
      ],
      [
        "Und das drückt sich aus im Funk­tionieren des Gedächtnisses, im Funktionieren der Erinnerung.",
        "Sie können sich also vorstellen, daß Sie in sich etwas haben wie eine Tafel, was hier im Profil gezeichnet ist - denn es ist ja im Profil gezeichnet, nicht wahr, es ist solch eine Ebene, die in Ihnen ist -, da wird zurück­geschlagen dasjenige, was nicht durchgehen soll."
      ],
      [
        "Sie bleiben, wenn Sie wachend sind, mit der Außenwelt vereint, sonst würde alles in wachem Zustande durch Sie durchgehen.",
        "Sie würden eigentlich von den Eindrücken nichts wissen, Sie würden die Eindrücke bekommen, aber könnten sie gar nicht festhalten."
      ],
      [
        "Das ist also dasjenige, was auf die Erinnerung deutet.",
        "Und das, was gewissermaßen als die Fläche dieser Stauwelle unsere Erinnerung bewirkt, deckt dasjenige zu, was der phantastische Mystiker gern in sich sehen möchte.",
        "Was da drunten ist, davon könnte man schon sagen: Für den, der die Dinge wirklich kennt, gilt das Wort: Der"
      ],
      [
        "Mensch «begehre nimmer und nimmer zu schauen, was sie [die Götter] gnädig bedecken mit Nacht und Grauen». - Doch die Mystiker sind phantastisch und wollen da hinunterschauen.",
        "Aber sie können es ja ohnedies nicht, weil sie das normale Bewußtsein so durchlöchern, so korrumpieren würden, daß sich die Gedächtniswelle nicht zurück­schlüge.",
        "Dasselbe, was unsere Erinnerung ausmacht, was wir so not­wendig brauchen zum äußeren Leben, das bedeckt uns dasjenige, was die phantastischen Mystiker wohl schauen möchten, was aber der Mensch nicht schauen soll.",
        "Unter Ihrem Gedächtnis, unter Ihrer Gedächtnisursache, unter Ihrer Gedächtnisfläche liegt etwas Wesen­haftes vom Menschen.",
        "Aber geradeso wie die Hinterwand eines Spie­gels, wie der Belag eines Spiegels das, was vorn ist, zurückwirft, so geht, was also in Ihrem Bewußtsein ist, nicht da hinten hin ; das wird wieder zurückgeworfen und kann deshalb fortwährend als Erinnerung da sein.",
        "So kann überhaupt unser ganzes Leben sich als Erinnerung spiegeln.",
        "Und im wesentlichen ist ja dasjenige, was wir das Leben unseres Ich nennen, das Spiegeln dieser Erinnerung."
      ],
      [
        "Sie sehen also, unser bewußtes Leben leben wir eigentlich zwischen dieser Welle hier (rechts) und zwischen dieser Welle (links>.",
        "Wir wären also Schläuche, die alles durch sich hindurchlassen, wenn wir nicht diese Stauwelle hätten, die der Erinnerung zugrunde liegt, und wir sähen in die Geheimnisse jenseits der Erkenntnisgrenze hinein, wenn wir nicht genötigt wären, außerhalb des Gebietes des Sinnen-fälligen Begriffe zu setzen, für die wir keinen Inhalt mehr haben.",
        "Wären wir so organisiert, daß wir diese Stauung hier nicht erzeugen könnten, so würden wir Schläuche sein.",
        "Wären wir so organisiert, daß wir nicht genötigt wären, diese gewissermaßen unausgefüllten Be­griffe, diese dunklen Begriffe vor uns hinzusetzen, so wären wir liebe-leere und liebelose Wesen ; steinerne Naturen wären wir, trockene Naturen.",
        "Wir könnten nichts in der Welt gern haben, wir wären alle Mephistopelesnaturen."
      ],
      [
        "Daß wir so organisiert sind, daß wir an gewisses Geistig-Seelisches unserer Umgebung nicht herankommen können mit unseren abstrak­ten Begriffen, mit unserem Fassungsvermögen, das bewirkt, daß wir lieben können.",
        "Denn was wir lieben sollen, an das sollen wir nicht so"
      ],
      [
        "herankommen, daß wir es analysieren im gewöhnlichen Sinne des Wortes, daß wir es zergliedern, daß wir es behandeln wie der Chemi­ker im Laboratorium die chemischen Stoffe.",
        "Man liebt ja nicht, wenn man chemisch analysiert oder chemisch synthetisiert.",
        "Erinnerungs-fähigkeit, Liebefähigkeit, das sind die zwei Fähigkeiten, die zugleich entsprechen zwei Grenzen der menschiichen Natur.",
        "Der einen Grenze nach innen entspricht die Erinnerungsfähigkeit ; was jenseits der Er­innerungszone liegt, ist unterbewußtes menschliches Innere.",
        "Die andere Zone entspricht der Kraft der Liebefähigkeit ; was jenseits dieser Zone liegt, entspricht dem Geistig-Seelischen des Universums.",
        "Das Unbewußte der menschlichen Natur liegt also jenseits dieser Zone, soweit das menschliche Innere reicht ; das Geistig-Seelische des Uni­versums geht unbegrenzt in die Weiten hinaus von der andern Zone an."
      ],
      [
        "Wir können also sprechen von Liebezone, von Erinnerungszone und können dasjenige, was das menschlich Geistig-Seelische ist, inner­halb dieser Zonen einschließen ; müssen aber jenseits der einen Zone da drüben (siehe Zeichnung Seite 31, links) dasjenige suchen, was un­bewußt bleibt, und was deshalb, weil es unbewußt bleibt, gerade sehr stark zusammenhängt mit der menschiichen Körperlichkeit, mit den körperlichen Verrichtungen.",
        "Natürlich sind die Dinge in der Wirk­lichkeit nicht so einfach, wie man sie darstellen muß, weil alles inein­andergreift.",
        "Das, was hier rot ist (siehe Zeichnung Seite 31), das greift in Dinge hinein, das verändert sich ; und wiederum dasjenige, was grün und blau ist, das verändert sich auch.",
        "In der Wirklichkeit greifen die Dinge alle ineinander ein.",
        "Aber trotzdem ist in der Hauptsache die skizzenhafte Zeichnung richtig und entspricht den Tatsachen."
      ],
      [
        "Daraus aber ersehen Sie, daß für das physische Leben auf der Erde hier ein starkes, bewußtes Geistiges ist.",
        "Hier (links) ist ein unbewußtes Geistiges, das eigentlich mit dem Universum zusammen verschwimmt.",
        "Diese zwei Stücke des Menschen unterscheiden sich sehr deutlich von­einander.",
        "Dieses Geistige (in der Mitte), das ist daher zunächst für das irdische Leben ein solches, das sehr fein gewoben ist.",
        "Wie fein gewo­benes Licht, möchte ich sagen, ist alles hier (gelb).",
        "Würde ich am Menschen zu zeigen haben, wo dieses fein gewobene Licht ist, so würde in das hinein, was ich jetzt umfassend so umschreibe, das"
      ],
      [
        "menschliche Haupt fallen.",
        "Also was ich so umschrieben habe, was ich dorthin als das Gelbe, Gelb-Grünliche, Gelb-Orange nach der andern Seite gezeichnet habe, das ist fein gewobenes, wenn ich so sagen darf, Geistlicht."
      ],
      [
        "Das hat keine starke Verwandtschaft mit der irdischen Materie ; das hat eine möglichst geringe Verwandtschaft mit der irdi­schen Materie.",
        "Deshalb, weil es wenig Verwandtschaft hat, kann es auch nicht mit der Materie sich gut verbinden, und so bleibt es zum großen Teile unverbunden mit der Materie ; es wird diesem Teil ge­geben eine solche Materie, die eigentlich immer jeweils aus der vori­gen Inkarnation des Menschen stammt."
      ],
      [
        "Das Haupt, das, was das menschliche.",
        "Haupt formt, die Formungskräfte des menschlichen Hauptes, das wird im wesentlichen hereingetragen aus der vorigen Inkarnation, und da ist nur eine lose Verbindung zwischen diesem feingewobenen Geistig-Seelischen und dem Körperhaften, das eigent­lich von der vorigen Inkarnation zusammengehalten wird."
      ],
      [
        "Ihre Phy­siognomie tragen Sie ja eigentlich nach Ihren Verrichtungen und Eigenschaften in der vorigen Inkarnation.",
        "Und derjenige, der sich gut versteht auf Deutungen von Menschen, der sieht gerade durch das Physiognomische des Hauptes hindurch; nicht durch dasjenige, was von dem luziferischen Inneren stammt, sondern mehr durch die An­passung an das Universum."
      ],
      [
        "Man muß ja die Physiognomie so sehen, als wenn sie in den Menschen hineingedrückt wäre.",
        "Nicht so sehr, als ob sie herausginge, sondern man muß gewissermaßen das Negativ des Seelischen sehen ; das sieht man in diesem Negativ des Gesichts."
      ],
      [
        "Wenn Sie einen Abdruck machen würden von jedem Gesicht, da würden Sie eigentlich die Physiognomie sehen, die ein furchtbar starker Verräter ist desjenigen, was Sie in der vorigen Inkarnation angestellt haben.",
        "Dagegen ist alles, was ich da unten wie nur zusammenhängend mit dem wogenden Meere des Geistig-Seelischen der Welt skizziert habe, was so aufzufassen ist, daß es des Menschen Unterbewußtem oder Unbewußtem entspricht, stark verwandt mit der Körperlichkeit ; das durchsetzt die Körperlichkeit."
      ],
      [
        "Diese Körperlichkeit, die verbindet sich so mit dem Geistigen, daß das Geistige als Geistiges gar nicht erscheinen kann.",
        "Daher würde man, wenn man hinunterschaute, dieses Ineinanderbrod ein von Geistigem und Leiblichem schauen, was hinter"
      ],
      [
        "der Schwelle der Erinnerung liegt.",
        "Das ist das, was vorbereitet das Haupt der nächsten Inkarnation, das ist das, was sich metamorpho­sieren will zu dem, was in der Zukunft erst feste materielle Form be­kommt, erst Haupt sein wird in der nächsten Inkarnation.",
        "Denn das Haupt des Menschen ist ein über das Maß seiner Entwickelung Hinaus-geschrittenes.",
        "Daher ist das Haupt - wie Sie sich erinnern aus den früheren Vorträgen, die ich hier gehalten habe - eigentlich mit dem siebenundzwanzigsten, achtundzwanzigsten Jahre des Menschen in seiner Entwickelung schon abgeschlossen.",
        "Da ist schon Überbildung des Menschen, in der Hauptesform."
      ],
      [
        "Aber der übrige Mensch, der ist auch ein Haupt, so sonderbar das aussieht ; nur ist er noch nicht so weit als das Haupt.",
        "Wenn Sie sich den Menschen geköpft denken, so ist das, was übrigbleibt, auch ein Haupt des Menschen, aber auf einer noch sehr zurückgebliebenen Stufe.",
        "Wenn es sich weitet entwickelt, dann wird es auch Haupt, während das, was Sie als Haupt des Menschen haben, der übrige Organismus gewesen ist in früherer Inkarnation.",
        "Wenn Sie dann dasjenige entleiblicht sich denken, vom Leibe befreit, was in Ihrem gegenwärtigen Organismus noch nicht Haupt ist, wenn Sie sich also das Haupt wegdenken vom gegenwärtigen Organismus, der erst in der nächsten Inkarnation Haupt wird - aber dieser Ihr Organismus ist ja ein Abbild, alles Physische ist ein Abbild eines Geistigen -, wenn Sie sich dafür das Geistige denken, was also in seiner äußeren Form nicht bis zum Men­schen vorgeschritten ist: da sehen Sie es sich nun an unserer luziferi­schen Figur bei der Gruppe drüben an, da haben Sie es!"
      ],
      [
        "Und jetzt denken Sie sich all das Geistig-Seelische, das bei Ihnen zurückgehalten ist von Ihrem Haupte, in den Menschen hineingefügt, also all das, was beim Menschen eine Grenze ist, was er nicht durch­dringen kann (rechts, siehe Zeichnung Seite 31), in den menschlichen Kopf hineingepreßt: dann wird der Mensch nicht nur ein so altes, ehrwürdiges Haupt haben, wie er es ohnedies schon hat, sondern er wird ein ganz verknöchertes Haupt haben, wird überhaupt ganz ver­knöchern, wie die Ahrimanfigur bei unserer Gruppe drüben."
      ],
      [
        "Wenn Sie sich also dasjenige, was hier unter der Erinnerungsgrenze ist, ausgegossen denken über das Innere des Menschen, bekommen Sie"
      ],
      [
        "alles Luziferische.",
        "Wenn Sie sich alles dasjenige, was jenseits dieser Stauwelle ist (rechts), hereinergossen denken in die menschliche Figur, bekommen Sie die ahrimanische Form.",
        "Und der Mensch ist zwischen beiden."
      ],
      [
        "Was ich Ihnen da auseinandergesetzt habe, das hat nicht nur eine große Bedeutung für das Verständnis des Menschen, sondern das hat auch eine große Bedeutung für das Verständnis der geistigen Vor­gänge in der Menschheitsentwickelung.",
        "Man versteht nicht, wie das Christentum und der Christus-Impuls in die Menschheitsentwickelung hereingekommen ist, wenn man nicht gründlich diese Dinge versteht.",
        "Man versteht auch nicht, welche Funktionen die katholische Kirche hatte, welche Funktionen Jesuitismus und ähnliche Strömungen ha­ben, welche Osttum und Westtum haben, wenn man sie nicht im Zu­sammenhange betrachten kann mit diesen Dingen."
      ],
      [
        "Über diese Strömungen, die eigentlich richtig erst verstanden wer­den können, wenn man diese Grundlagen des geistig-seelischen Men­schen sich einmal anschaulich vor das Auge führt, Ost-, Westtum, Jesuitismus, Amerikanismus und so weiter, werde ich mir morgen erlauben, ein weniges zu sprechen."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG Dornach, 19. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Ich bemühte mich gestern, Ihnen ein Bild des seellschen Menschen zu geben. Dasjenige, was wir für heute einmal aus diesem Bilde des seeli­schen Menschen herausgreifen wollen, das sollen die beiden Grenz­zonen sein, die wir gestern kennengelernt haben. Die eine Grenzzone ergibt sich ja dadurch, daß der Mensch genötigt ist, haltzumachen, wenn er versucht, die Außenwelt, so wie sie sich ihm zunächst sinnen-fällig ergibt, zu durchschauen. Von Grenzen des Erkennens reden dann die Naturforscher, Philosophen und so weiter. Wir wissen, daß diese Grenzen des Erkennens nicht in Wahrheit vorhanden sind, daß sie aber in der Tat für das sinnliche, für das physische Anschauen des Menschen vorhanden sind.",
      "Die andere Grenze ist dadurch gegeben, daß alles in unserem Be­wußtsein Befindliche oder in das Bewußtsein Eintretende gewisser­maßen reflektiert wird, zurückgespiegelt wird an einer inneren Zone und dadurch zur Erinnerung werden kann. Es geht das, was wir im Bewußtsein haben, nicht in die volle Tiefe derjenigen Region hinunter, die nur unterbewußt für den Menschen bleibt. Wir wollen diese beiden Grenzen herauszeichnen (siehe Zeichnung Seite 45), die Erinnerungs-grenze (links) und - wir können sie geradezu nennen die Liebefähig­keitsgrenze (rechts), die zugleich die Grenze des Naturerkennens ist. Wir haben sie bezeichnet, indem wir Leruniskaten, die nach außen offen sind, hier zu zeichnen hatten (rechts), und hier (links) hatten wir gewissermaßen Lemniskaten mit einer umgestülpten Schieife zu ver­zeichnen. Das (rechts) also ist dann die Region des Außen, in das der Mensch nicht mehr hineinsieht mit dem gewöhnlichen sinnlichen Anschauung svermögen, also: nicht perzipierbar. Das (links) ist die Grenze des bewußten Lebens nach innen, in die der Mensch nicht unterzutauchen vermag mit dem Bewußtsein. Der Mensch bleibt mit seinem Bewußtsein oberhalb dieser Grenze. Würde er mit seinen be­wußten Vorstellungen hinuntertauchen, so würde er keine Erinnerung haben.",
      "# Bild s. 45",
      "Nun ist aber gerade in bezug auf das Leben des seelischen Menschen angesichts dieser beiden Grenzen etwas ganz Bestimmtes zu sagen. Wenn wir in der Entwickelung der Menscheit zurückgehen etwa hinter das 8. vorchristliche Jahrhundert - Sie wissen, 747 vor Christus be­ginnt der vierte nachatlantische Zeitraum -, wenn wir hinter diesen Zeitpunkt zurückgehen in die früheren nachatlantischen Zeiträume, dann gilt für den Menschen dieses, daß dasjenige, was jenseits dieser Grenze liegt, doch in einer gewissen Weise noch hereinwirkte in das Bewußtsein. Und darauf beruhte eben jenes damals noch vorhandene atavistische Hellsehen. Es drangen gewisse Impulse damals herein aus dem Universum und machten sich geltend als atavistische Schauun­gen. So daß wir sagen können: Ganz undurchsichtig - ich meine jetzt intellektuell undurchsichtig - wurde dieses Außen erst seit dem 8. vor-christlichen Jahrhundert, und es wurde immer mehr und mehr un­durchsichtig. - Jetzt leben wir im fünften nachatlantischen Zeitraum. Es ist ja undurchsichtig geblieben. Und darauf pochen ja die Leute",
      "heute ganz außerordentlich, indem sie immerzu behaupten, daß über­haupt kein Mensch eindringen könne in jenes «Ding an sich», oder wie sie es dann nennen, was da jenseits dieser Grenze liegt.",
      "Dagegen darf gesagt werden, daß immer mehr und mehr sich eine andere Tendenz geltend macht und gegen den sechsten nachatlantischen Zeitraum sich immer mehr und mehr geltend machen wird. Das ist, es wird gewissermaßen diese Zone hier (links) durchiässig werden.",
      "Es wird die Zeit kommen, wo aus den Tiefen der Menschennatur das­jenige, was ich Ihnen gestern als das Brodelnde geschildert habe, als dasjenige, in das der Mensch nicht hinunterschauen soll - in dem Sinne vor allen Dingen nicht, wie die phantastischen Mystiker das wollen -, es wird aus diesem Gebiete von dem sechsten nachatlantischen Zeit­raum an gewissermaßen allerlei durchsickern wollen. Ja, es wird diese Zeit schon im fünften nachatlantischen Zeitraum beginnen, in unserem Zeitraum.",
      "Es wird allerlei durchsickern wollen. Es wird sich das ja vor allen Dingen dadurch äußern, daß viel mehr Menschen, als man heute denkt, immer mehr und mehr aus gewissen rein inneren Erfah­rungen entnehmen werden, daß es wiederholte Erdenleben gibt und dergleichen.",
      "Diese Dinge kommen, man möchte sagen, heute schon, obwohl spärlich, zum Durchbruche. Ich habe öfter, hier ja wohl auch schon, den Namen eines merkwürdigen Menschen der Gegenwart genannt, des Otto Weininger, der ja besonders bekanntgeworden ist durch sein dickes Buch «Geschlecht und Charakter».",
      "Noch interessan­ter aber ist dasjenige Buch, das nach seinem Tode sein Freund Rappa­port herausgegeben hat, und in dem allerlei außerordentlich Interes­santes drinnensteht. Es sind zum großen Teil Aphorismen.",
      "Das Ganze trägt den Titel «Über die letzten Dinge». Einer dieser Apho­rismen besagt ungefähr dieses: Weininger behauptet, die Seele des Menschen hätte in ihrem vorgeburtlichen Leben ein gewisses Grauen vor sich selber zur Entwickelung gebracht und hätte dadurch die Sehn­sucht bekommen, dieses Leben zu vergessen und sich in das Vergessen hineinzustürzen, was die Verleiblichung bedeutete. - Also Weininger spricht vollständig von dem vorgeburtlichen Leben, von dem Ver-leiblichen; nur spricht er in seiner düsteren, pessimistischen An­schauung davon, daß die Seele sich zu betäuben sucht gegenüber",
      "ihrem vorgeburtlichen Leben, und die Betäubung sucht sie in der Verleiblichung in einem physischen Menschenleib.",
      "Aber solche unmittelbaren Eindrücke heutiger Menschen von dem Wege der Seele gibt es ja viele, und sie werden immer zahlreicher und zahlreicher werden. Bei solch einem Menschen wie Weininger kann man schon heute sehen, wie dichter, kompakter möchte ich sagen, das Ich innerlich den Menschen anfaßt. Bei Weininger sieht man schon deutlich, wie diese Grenze etwas durchlässig wird und da allerlei her­aufdringt. Interessant ist es zum Beispiel, welche Notiz er hingeschrie­ben hat über seinen eigenen Tod. Er verübte frühzeitig, mit dreiund­zwanzig Jahren schon, Selbstmord. Er schrieb eine ganze Reihe von Notizen nieder, die außerordentlich interessant sind, weil sie geradezu Imaginationen astralischen Schauens darstellen. Das alles paarte sich mit einem gewissen Charakterzug, der ihn dann dahin führte, eines Tages sich einzumieten in Beethovens Sterbehaus in Wien und in diesem sich gleich am nächsten Morgen selber zu ermorden, mit drei­undzwanzig Jahren. Und darüber schrieb er die Notiz, daß er sich ermorden müsse, weil er sonst fürchten müsse, getrieben zu werden durch einen unbestimmten Drang, ein Mörder zu werden, einen andern ermorden zu müssen.",
      "Man sieht, da rumoren furchtbarste Dinge in der Seele eines außer­ordentlichen genialischen Menschen, die nicht so ohne weiteres be­zwungen werden können durch das, was in seinem Bewußtsein ist, weil da vieles aus diesem Unterbewußten herauf rumort. Sie werden begreifen, daß man schon mit einem gewissen Recht darauf hinweisen muß, daß die gewöhnliche Gescheitheit, die der Mensch jetzt ent­wickeln kann, nicht ausreicht, um das, was da aus den unbekannten Tiefen herauf kommt, zu erkennen. Denn es sollte ja gar nicht herauf­kommen, es sollte da unten bleiben, aber es wird doch heraufkommen. Geradeso wie bis zum Jahre 747 vor Christus von außen etwas herein­gekommen ist, so wird nachher von innen etwas aufsteigen. Durch das, was der Mensch sich erringen wird an gewöhnlicher, normaler Ge­scheitheit, wird das nicht bezwungen werden können, bei weitem nicht bezwungen werden können. Da wird man eben brauchen jenes Ver­stehen der Welt, welches durch die Geisteswissenschaft zu erwerben",
      "ist. Es wird Harmonie, innerliche Festigkeit und innerliche Gediegen­heit in das menschliche Seelenleben nur eindringen können, wenn die Menschen dieses innerliche Seelenleben werden ordnen, harmonisie­ren wollen durch dasjenige, was aus der Erkenntnis des Geistes heraus errungen werden kann. Es strebt die Entwickelung der Menschheit also aus einem Zustande heraus, in welchem von der Außenwelt mehr wahrnehmbar war, als heute wahrnehmbar ist, und es strebt diese Ent­wickelung der Menschheit einem Zustande zu, in welchem aus dem tiefsten Inneren des Menschen mehr auftauchen wird, als heute im Normalzustand auftaucht.",
      "Diese Dinge, von denen ich jetzt spreche, sie kennt man eigentlich in den eingeweihten Kreisen da und dort sehr gut. Von jenem alten Erkennen, das bis ins 8. vorchristliche Jahrhundert den Menschen zu­gänglich war, spricht ja noch das ganze morgenländische Geistesleben, das ganze asiatische Geistesleben.",
      "Ja, es spricht nicht nur das Geistes­leben, es spricht im Grunde genommen die ganze asiatische Kultur davon. Daher kommt es, daß es eigentlich so schwer verständlich ist für den Europäer, wenn heute der Orientale, der asiatische Orientale von seiner Kultur spricht.",
      "Da muß man schon, wenn man diese Leute verstehen will, sich hineinfinden in eine andere Art, die Vorstellungen, die Gedanken zu bilden. Heute würde es zum Beispiel für sehr viele Menschen sehr interessant sein niüssen, so etwas Tonangebendes zu verfolgen, wie die Rede ist, welche Rabindranath Tagore, der Inder, ge­halten hat über den Geist Japans.",
      "Sie wissen: Tagore ist der von der Nobel-Stiftung preisgekrönte Inder. Er hat über den Geist Japans einen Vortrag gehalten. Es ist weniger wichtig, was er über den Geist Japans gerade spricht, als der Geist, aus dem heraus er spricht, der Geist des heutigen Orientalen, der nur verstanden werden kann, wenn man weiß, daß etwas in den Orientalen noch zurückgeblieben ist von jenem Her­auf-, von jenem Hereinkommen der Außenwelt, wie es heute nicht perzi­pierbar ist.",
      "Für die meisten Europäer reden die Orientalen, wenn sie im Sinne ihrer Kultur reden, eben eigentlich etwas ziemlich Unverständ­liches. Man versteht gewöhnlich gar nicht, wovon sie eigentlich reden.",
      "Auch die andere Erscheinung kommt vor, daß dasjenige, was eigent­lich erst in der Zukunft auftreten sollte, in einer gewissen Weise dann",
      "vorweggenommen wird. Vergleichen könnte ich das damit, daß ich hinweise auf Kinder, die als Kinder schon greisenhaft sind. Sie neh­men das Greisenhafte als Kinder schon voraus. Da ist die Unregel-mäßigkeit in der Entwickelung dadurch eingetreten, daß etwas, das später kommen sollte, früher hereingeschoben ist, in eine frühere Zeit.",
      "Während nun im orientalischen Denken, in der orientalischen An­schauungsweise gerade bei den hervorragendsten Geistern ein aus alter Zeit Zurückgebliebenes in der Weise herrscht, wie ich es eben angedeutet habe, herrscht namentlich bei so ganz im Sinne des Ameri­kanismus denkenden Geistern ein Hereinnehmen von Späterem, ein Hereinschieben von Späterem. Da merkt man deutlich, wenn man auf solche Sachen eingehen kann, daß gerade hervorragendere Geister vieles von dem haben, was da (links) durchsickert.",
      "Sie bekommen eine Vorstellung von solchem Durchsickerndem, wenn Sie zum Bei­spiel jenen Essay lesen, den Woodrow Wilson geschrieben hat über die Entwickelung des amerikanischen, des nordamerikanischen Volkes im besonderen. Man kann sich nichts denken, das mehr den Nagel auf den Kopf trifft, das treffender wäre als dieser Essay, den Woodrow Wilson über die Entwickelung des amerikanischen Volkes geschrieben hat.",
      "Da ist jedes Wort darinnen so, daß man das Gefühl hat: es ist die Sache in der allerallerschärfsten Weise charakterisiert und getroffen. Und das fällt insbesondere deshalb auf, weil Wilson in diesem Fall sehr scharf aufmerksam macht darauf, daß eine ganze Anzahl von Leuten auch in Amerika die Ansicht haben, die eigentlich nur zu rechtfertigen ist, wenn man das amerikanische Volk heute noch auffaßt - wogegen er, Woodrow Wilson, sich wendet - gleichsam als eine Dependance des englischen Volkes.",
      "Diese Menschen, die heute noch die Amerika­ner so auffassen, als ob diese etwas wären wie Abkömmlinge, wie ein Zweig der europäischen Engländer, diese Leute lehnt Woodrow Wil­son im strengsten Sinne des Wortes ab. Die verstehen nichts, meint er, von der eigentlichen Entwickelung des amerikanischen Volkes im 19.",
      "Jahrhundert. Denn der Amerikaner beginnt von innen erst Ame­rikaner zu sein - so spricht Wilson aus echt amerikanischem Geiste heraus, außerordentlich prägnant und treffend - in dem Momente, wo er aufhört anzuknüpfen mit seinem Seelenhaften an das, was von England",
      "herübergekommen ist, wo er beginnt, als Bebauer des Bodens von Osten nach dem Westen hinüberzudringen, von der amerikani­schen Ostküste nach der Westküste hinüberzudringen. In diesem Aus­roden der Urwäider, in der Arbeit mit der Flinte, in der Arbeit mit dem Spaten, in der Arbeit mit dem Pflug und dem Pferde, in diesem Über­winden jenes Widerstandes, der zu überwinden ist bei der Arbeit von dem Osten nach dem Westen hinüber, entwickelt sich für ihn der Westmann, der «WesterneD>, wie er es nennt. Und in dieser Art und Weise der Eroberung des Bodens sieht er, so daß es unmittelbar über. zeugendsten Eindruck macht, den eigentlichen Nerv der amerikani­schen Entwickelung. Man hat überall gerade das Gefühl - man muß natürlich verstehen, das Wie zu lesen in einem solchen Fall, nicht bloß das Was -, da spricht viel mehr als der Wilson. Denn wenn der Wilson selber spricht - ja, da wird nicht viel Gescheites daraus. Da spricht viel mehr, da spricht dasjenige, wovon der Mann als von seinem eigenen Inneren her besessen ist, da sprechen Därnonennaturen, die geradezu grandiose Zukunftsgeheimnisse eingeben. In diese Geheim­nisse müßte eigentlich die Menschheit eindringen, wenn die Ent­wickelung verstanden werden soll.",
      "Man muß heute tatsächlich einen Unterschied machen zwischen der bloßen wissenschaftlichen und zeitungsgemäßen Erfassung der Welt, die ja bequem ist, die auch allbeliebt ist, und der wahren Erfassung der Welt. Die wahre Erfassung der Welt, die muß solche Gegensätze sich klarmachen können wie die, welche ich jetzt auseinandergesetzt habe:",
      "von dem Hereinkommen bei den orientalischen Völkern von etwas, das da draußen liegt (siehe Zeichnung Seite 45, rechts) ; von dem Heraufkommen bei den amerikanischen Völkern von etwas, was da drinnen (links) liegt. Und was da heraufkommt, es braucht das nicht etwas bloß Verwerfliches zu sein, es kann in gewissem Sinne grandiose ahrimanische Offenbarung sein, die da heraufkommt. Denn ahrima-nische Offenbarung ist es im wesentlichen, welche in jenem ausge­zeichneten Aufsatze von Woodrow Wilson über die Entwickelung des amerikanischen Volkes gegeben ist.",
      "Die Eingeweihten des Ostens und die Eingeweihten des amerikani­schen Volkes, die wissen auch das Nötige aus diesen Dingen zu machen.",
      "Man will von beiden Seiten die Entwickelung der Menschheit durchaus in gewisse Bahnen bringen. Die orientalischen Völker, das heißt ihre Eingeweihten, haben ganz bestimmte Absichten für die Zukunftsentwickelung der Menschheit.",
      "Diese Leute sehen, was in der Entwickelung richtig liegt und versuchen dasjenige, was in der Ent­wickelung richtig liegt, soweit der Mensch es beeinflussen kann, zu beeinflussen. Sie suchen ihm eine gewisse Richtung, einen gewissen Impuls zu geben.",
      "Und der Impuls, der da von den orientalischen Ein­geweihten der Entwickelung gegeben werden will, der beruht im wesentlichen darauf, daß man nicht mehr rechnen will, so ungefähr nach der Häffte der sechsten nachatlantischen Zeit, auf die mensch­liche Generation. Man möchte verzichten auf das irdische Menschen­geschlecht nach dieser Zeit.",
      "Man möchte die Entwickelung der Menschheit dahin bringen, daß die Menschen nachher eigentlich nicht mehr so recht physische Nachkommen haben, daß die Seelen dann schon sich vergeistigen, nicht mehr auf die Erde herunterkommen in Verleiblichungen. Man möchte das Reich des Geistes für die Mensch­heit schon von der Mitte der sechsten nachatlantischen Zeit an be­gründen.",
      "Dies würde man nur können, wenn man gewisse Kultur­ingredienzien abweisen würde. Nicht nur die Eingeweihten des Orients, sondern eigentlich instinktiv jeder gebildete Orientale lehnt daher im eminentesten Sinne gewisse Europäismen ab ; gerade die­jenigen Europäismen, auf die der Europäer ganz besonders stolz ist, lehnt er ab.",
      "Er lehnt ab namentlich alles dasjenige, was sich ja aus der rein technischen, materiellen Kultur in Europa und seinem Anhange Amerika ergeben hat. Wer die Entwickelung der Menschheit studiert, namentlich im 19.",
      "Jahrhundert und in das 20. Jahrhundert herein, der wird finden, daß man mit Recht sagt: Die Techhik hat es ungeheuer weit gebracht, die Technik hat den Menschen Arbeitskräfte abge­nommen. Wenn man heute davon redet, die Erde habe so und so viel hundert Millionen Einwohner, so ist dieses eigentlich nicht ganz richtig, weil man auch rechnen kann, wieviel die Erde Einwohner hat nach dem, wieviel gearbeitet wird.",
      "Nun wird mit vollständigem Recht gesagt, daß seit dem letzten Drittel des 18. Jahrhunderts von den Maschinen, die nach und nach entstanden sind, menschliche Arbeitskraft",
      "verrichtet wird. Man kann berechnen, ziemlich exakt berechnen, wieviel Millionen Menschen mehr die Erde haben müßte, wenn alle die Arbeit, die von den Maschinen verrichtet wird, von den Menschen verrichtet würde. Die Erde müßte fünfhundert Millionen Menschen mehr haben. Man kann schon sagen: Heute sind auf der Erde nicht nur diejenigen Menschen mit zwei Beinen und einem Kopf, die statistisch berechnet werden können, sondern fünfhundert Millionen mehr, gemessen an der Arbeitskraft; die Arbeitskraft wird eben von Maschlnen verrichtet.",
      "Aber es gibt nichts Materielles, hinter dem nicht ein Geistiges steht. Diese fünfhundert Millionen Menschenkräfte, die sind die Gelegen­heit zum Aufenthalte von ebensovielen ahrimanischen Dämonen innerhalb der menschlichen Kultur. Diese ahrimanischen Dämonen sind einmal da. Und diese ahrimanischen Dänionen, die lehnt der Orientale aus einem gewissen Instinkt heraus radikal ab ; die will er nicht. Das sehen Sie eigentlich aus jeder Manifestation eines feingebil­deten Orientalen heraus, daß er diese ahrimanische Dämonologie ab­lehnt. Denn diese ahrimanische Dämonologie, die gibt dem Menschen eine gewisse Schwere, die niemals möglich macht, daß dasjenige ge­schleht, was die orientalische Initiation anstrebt: daß das Menschen­geschlecht mit der Mitte der sechsten nachatlantischen Zeit physisch aufhört auf der Erde zu sein, weil die Menschen zurückgehalten wer­den durch das, was sich auf diese Weise dämonologisch-ahrimanisch entwickelt.",
      "Einem andern Ziel streben die Eingeweihten des Amerikanismus zu. Sie streben dem entgegengesetzten Ziele zu. Sie streben danach, eine innigere Gemeinschaft zu bilden, als im normalen Verlauf der Mensch­heitsentwickelung geschehen soll, zwischen den Menschenseelen und derjenigen Leiblichkeit, welche auf der Erde zu finden sein wird, der dichten, groben Leiblichkeit, die auf der Erde zu finden sein wird von dem sechsten nachatlantischen Zeitraume an. Die seelische Kultur wird sehr vertieft sein, aber die leibliche wird grob sein. Aber eine innigere Verbindung mit dieser groben Leiblichkeit strebt man im amerikanischen Westen an, eine innigere Verbindung als die normale ist, ein stärkeres Untertauchen in die Leiblichkeit. Man will entgegenkommen",
      "dem, was da durchsickert (siehe Zeichnung Seite 45, links), will ihm entgegengehen durch stärkeres Eindringen in die Leiblich­keit. Während man also eine Kultur begründen will von seiten der Orientalen, die nicht rechnet mit den Menschenleibern der späteren Erdenentwickelung, will man die Seelen ketten an diese spätere Erdenentwickelung innerhalb der amerikanischen Kultur des Westens. Man will die Leiber möglichst so gestalten, daß die Seelen, wenn sie durch den Tod gegangen sind, möglichst bald wiederum in einen Leib herunterkommen können, daß sie möglichst wenig sich aufhalten in der geistigen Welt. Man will die Seelen möglichst abhalten von einem Aufenthalt in der geistigen Welt, man will, daß sie möglichst bald wiederum auf die Erde herunterkommen. Man will sie innigst ver­binden mit dem Leben der Erde.",
      "Das sind Tendenzen, die man kennenlernen muß. So sonderbar es dem heutigen Menschen noch erscheint, wenn man von diesen Ten­denzen spricht, so schädlich ist es ihm, daß sie übersehen werden. Denn notwendig ist, daß der Mensch sich mit vollem Bewußtsein hin-einstellt in dasjenige, das eigentlich mit ihm selbst gewollt wird und demgegenüber er oftmals leider, leider so steht, daß man sagen kann:",
      "er läßt alles mögliche mit sich geschehen.",
      "Aber dieses westliche Ideal, diese Dämonologisierung des Men­schen, das wird nur erreicht werden können, wenn der geistige, psy­chische Amerikanismus unterstützt werden kann von einer andern Weltanschauungsströmung, die viel verwandter mit dem Amerikanis­mus ist, als man denkt. Sie haben ja gesehen: Es ist wesentlich ein Hin-neigen des Amerikanismus zur Ahrimankultur, was das Ausschlag­gebende ist. Aber eine richtige Förderung würde dieser Amerikanis­mus erhalten können, wenn er unterstützt würde von einer andern Weltanschauung, die viel verwandter mit ihm ist, als man denkt. Das ist der Jesuitismus. Jesuitismus und Amerikanismus sind zwei sehr, sehr verwandte Dinge. Denn als der fünfte nachatlantische Zeitraum begann, da handelte es sich darum, einen Impuls zu finden, durch den man sich in den Stand setzen konnte, die Menschen möglichst hinweg-zuführen von dem Verständnisse des Christus. Und diejenige Bestre­bung in der Kulturentwickelung, welche es sich zur Aufgabe gesetzt",
      "hat, kein Verständnis des Christus aufkommen zu lassen, das Ver­stänanis des Christus vollständig zu untergraben, das ist der Jesuitis­mus. Der Jesuitismus strebt danach, allmählich jede Möglichkeit eines Christus-Verständnisses auszurotten.",
      "Denn dasjenige, was da zugrun­de liegt, das hängt schon mit einem tiefen Mysterium zusammen. Da-mit, daß etwas von außen (siehe Zeichnung Seite 45, rechts) immer da hereinkam in das menschliche Innere, hängt es zusammen, wie ich sagte, daß die Menschen vorher, vor dem 7., 8. vorchristlichen Jahr­hundert, atavistisches Hellsehen hatten.",
      "Aber durch dieses atavistische Hellsehen sahen sie auch im Universum den Christus. Der Christus war etwas, was sie sehen konnten im alten Hellsehen. Ich habe das ja oft dargestellt, ich habe es dargestellt in der «Geheimwissenschaft im Umriß», und der ganze Sinn meines Buches «Das Christentum als mystische Tatsache» gipfelt ja schließlich darin.",
      "Man sah den Christus im Kosmos, man sah den Christus im Universum. Aber nun denken Sie: Vom 7., 8. vorchristlichen Jahrhundert ab haben wir Menschen die Möglichkeit verloren, in das Universum hinauszuschauen.",
      "Was hätten denn die Menschen mitverloren, wenn nichts anderes gekom­men wäre, dadurch, daß sie gar nicht mehr hinausschauen konnten ins Universum? Was hätten die Menschen verloren? Die Möglichkeit, von einem Christus-Geiste überhaupt etwas zu wissen, wenn der Christus nicht zu ihnen gekommen wäre durch das Mysterium von Golgatha, wenn der Christus nicht auf die Erde heruntergekommen wäre.",
      "In dem historischen Zeitmomente, wo die Menschen nicht mehr den Christus im Kosmos schauen konnten, kam der Christus auf die Erde herunter, verband sich mit dem Jesus. Von da ab war es des Menschen Aufgabe, den Christus in dem Menschen zu erfassen.",
      "Und gerettet werden muß die Möglichkeit, daß mit dem, was da durch­sickert (siehe Zeichnung, rechts), der Christus erkannt werde. Denn der Christus ist zu den Menschen heruntergestiegen. Der Jesus ist ein Mensch, in dem der Christus gewohnt hat.",
      "Wirkliche menschliche Selbsterkenntnis muß den Jesus-Keim tragen. Dadurch wird man in die Zukunft übersiedeln können. Tief begründet ist es, daß wir von einem Christus Jesus sprechen. Denn der Christus entspricht dem Kos­mischen ; aber dieses Kosmische ist auf die Erde heruntergekommen",
      "und hat in dem Jesus Wohnung genommen, und der Jesus entspricht dem Irdischen mit der ganzen irdischen Zukunft.",
      "Will man den Menschen abschließen vom Geistigen, so nimmt man ihm den Christus. Dann hat man die Möglichkeit, den Jesus so zu benützen, daß die Erde nur in ihrem irdischen Aspekt vorhanden bleibt. Sie werden daher beim Jesuitismus eine fortwährende Be­kämpfung der Christologie finden, dagegen ein scharfes Betonen des­sen, daß man ein Heer ist, eine Armee für den Jesus. Ja, natürlich:",
      "Geisteswissenschaft ist schon ein Mittel, daß solche Dinge erkannt werden, daß den Menschen die Schuppen von den Augen fallen. Da­her werden jene, die nicht erkannt sein wollen, immer wütender und wütender werden auf dasjenige, was Geisteswissenschaft will.",
      "Wüten­der, man sieht es: Das Juliheft der jesuitischen Zeitschrift «Stimmen der Zeit» - früher «Stimmen aus Maria-Laach» - enthält nicht nur einen, sondern gleich zwei Artikel gegen mich. Und wer dieses im Zusammenhang zu denken vermag mit dem, was sonst jetzt sich an neuen Aspirationen des Jesuitismus in der Welt entwickelt, der wird daraus überhaupt etwas Tieferes sehen können.",
      "Nur leider, man spricht ja von solchen Dingen heute doch zumeist vor einer schlafen­den Menschheit. Die Menschen lieben es, die wichtigsten Dinge zu vrschlafen, nicht hinzuhören auf dasjenige, was nun wirklich zu­kunifbestimmend ist.",
      "Daher werden die Menschen jetzt von allen Dingen, wie ich vorgestern sagte, überrascht. Sie wollen ja auch über­rascht sein. Spricht man möglichst früh von den Dingen, die im Schoße der Zeit liegen, so betrachten die Menschen das als etwas Unbequemes, weil sie möglichst lange gut brav bürgerlich bequem auf ihren Polster­sesseln sitzen möchten, auch wenn sie verantwortungsvolle, führende Menschheitsstellen innehaben.",
      "Aber diejenigen, welche sich für Geisteswissenschaft interessieren, sollten schon sich in die Seelen ein­gravieren, daß man alles tun wird, um diese Geisteswissenschaft un­wirksam zu machen. Es ist nicht gerade gut, wenn auch wir innerhalb unserer Kreise allzusehr schlafen mit Bezug auf die Beobachtung des­jenigen, was in der Welt vorgeht.",
      "Zuweilen ist es ja recht schwierig, zu sehen, wie doch immer alles, was so persönlich spielt, höhergestellt wird als dasjenige, was in der",
      "gegenwärtigen Zeit so ganz besonders wichtig und wesentlich ist: das Hinschauen auf die großen Angelegenheiten der Menschheit, die sich langsam vorbereiten. Die Angriffe, die zu tun haben mit den großen Wollungen, die kommen schon von den verschiedensten gegnerischen, ernst zu nehmenden Seiten. Solch ein Angriff wie der, von dem ich eben gesprochen habe, er ist schon in gewissem Sinne ernster zu neh­men. Man muß ihn in der richtigen Weise taxieren können. Nicht ernst zu nehmen nach dieser Richtung hin sind ja natürlich jene schö­nen Angriffe, welche aus dem Unterirdischen unserer Gesellschaft selber immer wiederum auftauchen, und die ja zum Teil bloß deshalb ein böses Ansehen haben, weil immer wieder und wiederum die Ten­denz bemerkbar ist, daß man gerade die größte, liebevollste Teilnahme gegenüber jenen Leuten hat, welche dasjenige, was ernst erstrebt wird in unseren Reihen, verlästern, zu verunglimpfen suchen und derglei­chen. Und erst wenn das Unheil da ist, dann entschließt man sich nach und nach, wirklich zu sehen ; vorher werden manche Leute gehätschelt, welche dann das Unheil bringen.",
      "Ich sage dies nicht, weil ich daran denke, daß das oder jenes anders sein sollte, sondern weil ich mich wirklich verpflichtet fühle, darauf aufmerksam zu machen, daß die Menschheit aufwachen muß, und daß wir vor allen Dingen zu denen gehören müssen, welche nach Wachheit streben.",
      "Auf gewissen Gebieten kann man ja heute alles mögliche tun. Der von mir hier gemeinte Schlaf der Menschheit, der nur überwunden werden kann durch ein Eindringen in die geistigen Welten, der ist außerordentlich schwer zu überwinden, der Schlaf der Menschen. Und mit Bezug auf die Verbreitung des geisteswissenschaftlichen Erkennt­nisgutes hat man es vielfach gerade mit diesem Schlaf zu tun als dem Gegner. Ich will dabei gar nicht von einer einzelnen Erscheinung sprechen, sondern in der ganzen Kulturbewegung ist gegenwärtig etwas Schläfriges gegenüber den eigentlichen Impulsen, die überall, an allen Stellen den Menschen über den Kopf hinauswachsen. Zwei Dinge sind notwendig, die man sich wie goldene Regeln eigentlich einschrei­ben müßte in seine Seele: Niemals war mehr als in unserem fünften nachatlantischen Zeitraum die Notwendigkeit vorhanden, daß die",
      "Menschen sich immer mehr und mehr bemühen - und daß Menschen da sind, die das können, daran ist nicht zu zweifeln -, gerade das zu erreichen, was besonders wertvoll ist: geisteswissenschaftliche Er­kenntnisse zu verstehen. Gewiß, geisteswissenschaftllche Erkenntnisse müssen gesucht werden durch hellsichtiges Eindringen in die geistige Welt ; das ist eine Notwendigkeit.",
      "Aber das ist eine Selbstverständ­lichkeit, daß es Hellseher geben muß, die eindringen in die geistige Welt, daß es Leute geben muß, die übersinnliche Erkenntnisse an­streben. Zweitens aber ist besonders wichtig, daß sich für diese geistes-wissenschaftlichen Erkenntnisse, für diese in übersinnlichen Welten gesuchte Erkenntnis Leute finden, die kraft des Intellekts die Sache verstehen.",
      "Das vernünftige, verständige Begreifen der Geisteswissen­schaft, das ist heute ganz besonders notwendig, denn das ist dasjenige, wodurch die widerstrebendsten Kulturmächte gerade überwunden werden. Der Intellekt der Menschen ist heute so groß, daß die ganze Geisteswissenschaft verstanden werden kann, wenn man nur will.",
      "Und gerade dieses Verständnis anzustreben, ist ein allgemein-menschliches, nicht ein egoistisches Interesse der Kultur. Denn dieses Verständnis kann angestrebt werden, wenn jene intellektuellen Kräfte, die heute verwendet werden auf naturwissenschaftlichen Gebieten an allerlei Kleinkram, wenn jene intellektuellen Kräfte, die heute volkswirt­schaftlich recht fruchtlos verwendet werden, und endlich, wenn jene Kräfte, die in einer fruchtlosen, vielleicht sogar menschenmörderi­schen Technik verwendet werden, entsprechend angewendet würden, und die Menschen nicht verzogen würden von frühester Kindheit an.",
      "Dann würde man sehen, wie leicht das spirituelle Geistesgut wirklich zum Verständnisse der Menschheit gebracht werden könnte. Das ist das eine.",
      "Die andere goldene Regel ist diese, daß man heute noch etwas an­deres braucht für das Fruchtbarmachen des spirituellen Geistesgutes für unsere Kultur. Das erste ist etwas, was Ahriman abgerungen wer­den muß. Die Menschen sind heute schon gescheit, denn Ahriman sorgt dafür, daß die Menschen gescheit sind. Oh, die Menschen sind gescheit! Sie verwenden ihre Gescheitheit eben nur im materialisti­schen Interesse. Die Menschen sind nicht nur gescheit, sie sind übergescheit.",
      "Davon werden wir aber in den nächsten Vorträgen noch sprechen, damit Sie sehen, welchen ungeheuren Einfluß gerade das ahrimanische Element auf die menschliche Übergescheitheit der heu­tigen Zeit hat. Aber noch etwas anderes ist notwendig.",
      "Noch einem andern Geiste ist manches abzuringen. Wir brauchen nicht nur Ge­scheitheit, mit der das spirituelle Geistesgut durchdrungen werden soll, wir brauchen vor allen Dingen sehr, sehr dringlich - ja, wie soll ich es ausdrücken -, wir brauchen bei den Menschenseelen, an die das spiri­tuelle Geistesgut herankommt, Temperament, Enthusiasmus, Feuer, Wärme.",
      "Wir brauchen Menschen, welche mit der ganzen, vollen Seele dasjenige vertreten, was spirituelles Geistesgut ist. Gerade auf spiri­tuellem Gebiete muß den luziferischen Kräften, die sonst so wirksam jetzt sind in der Welt, dieses abgerungen werden.",
      "Es gibt einen schö­nen Anblick: es ist der Anblick desjenigen, der in ruhiger Klarheit, aber mit innerem Feuer und Enthusiasmus, weil es ihm eine Notwen­digkeit ist, für das spirituelle Geistesgut sich erwärmen kann. Es gibt einen andern Anblick: das ist der, wo man möglichst versucht, durch das spirituelle Geistesgut eingelullt zu werden, träumerisch zu werden, hingegossen warm zu werden, aufzugehen in die universellen Kräfte, die Seele zu vereinigen mit dem göttlichen All.",
      "Das sind Gegensätze, die man in der Gegenwart doch wohi beobachten kann, Gegensätze, die es notwendig ist, zu beobachten. Denn es wird nicht leicht werden, das spirituelle Geistesgut der Menschenkultur einzuverleiben.",
      "Und es muß hinein, denn die Menschenkultur braucht es. Man wird über vieles ganz, ganz anders nicht nur denken lernen müssen, sondern auch fühlen und empfinden lernen müssen.",
      "Ja, ich könnte noch manches sagen in Anknüpfung an dasjenige, was ich jetzt eben ausgesprochen habe, aber ich will vielleicht lieber schweigen und will Ihnen Gelegenheit geben, nachzudenken. Man kann über manches nachdenken, was angeregt werden könnte durch manche Tücke, welche ich ganz absichtlich in die eben ausgesprochene Wahrheit hineingelegt habe. Nun, davon wollen wir dann das nächste Mal weiter sprechen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Ich bemühte mich gestern, Ihnen ein Bild des seellschen Menschen zu geben.",
        "Dasjenige, was wir für heute einmal aus diesem Bilde des seeli­schen Menschen herausgreifen wollen, das sollen die beiden Grenz­zonen sein, die wir gestern kennengelernt haben.",
        "Die eine Grenzzone ergibt sich ja dadurch, daß der Mensch genötigt ist, haltzumachen, wenn er versucht, die Außenwelt, so wie sie sich ihm zunächst sinnen-fällig ergibt, zu durchschauen.",
        "Von Grenzen des Erkennens reden dann die Naturforscher, Philosophen und so weiter.",
        "Wir wissen, daß diese Grenzen des Erkennens nicht in Wahrheit vorhanden sind, daß sie aber in der Tat für das sinnliche, für das physische Anschauen des Menschen vorhanden sind."
      ],
      [
        "Die andere Grenze ist dadurch gegeben, daß alles in unserem Be­wußtsein Befindliche oder in das Bewußtsein Eintretende gewisser­maßen reflektiert wird, zurückgespiegelt wird an einer inneren Zone und dadurch zur Erinnerung werden kann.",
        "Es geht das, was wir im Bewußtsein haben, nicht in die volle Tiefe derjenigen Region hinunter, die nur unterbewußt für den Menschen bleibt.",
        "Wir wollen diese beiden Grenzen herauszeichnen (siehe Zeichnung Seite 45), die Erinnerungs-grenze (links) und - wir können sie geradezu nennen die Liebefähig­keitsgrenze (rechts), die zugleich die Grenze des Naturerkennens ist.",
        "Wir haben sie bezeichnet, indem wir Leruniskaten, die nach außen offen sind, hier zu zeichnen hatten (rechts), und hier (links) hatten wir gewissermaßen Lemniskaten mit einer umgestülpten Schieife zu ver­zeichnen.",
        "Das (rechts) also ist dann die Region des Außen, in das der Mensch nicht mehr hineinsieht mit dem gewöhnlichen sinnlichen Anschauung svermögen, also: nicht perzipierbar.",
        "Das (links) ist die Grenze des bewußten Lebens nach innen, in die der Mensch nicht unterzutauchen vermag mit dem Bewußtsein.",
        "Der Mensch bleibt mit seinem Bewußtsein oberhalb dieser Grenze.",
        "Würde er mit seinen be­wußten Vorstellungen hinuntertauchen, so würde er keine Erinnerung haben."
      ],
      [
        "# Bild s. 45"
      ],
      [
        "Nun ist aber gerade in bezug auf das Leben des seelischen Menschen angesichts dieser beiden Grenzen etwas ganz Bestimmtes zu sagen.",
        "Wenn wir in der Entwickelung der Menscheit zurückgehen etwa hinter das 8. vorchristliche Jahrhundert - Sie wissen, 747 vor Christus be­ginnt der vierte nachatlantische Zeitraum -, wenn wir hinter diesen Zeitpunkt zurückgehen in die früheren nachatlantischen Zeiträume, dann gilt für den Menschen dieses, daß dasjenige, was jenseits dieser Grenze liegt, doch in einer gewissen Weise noch hereinwirkte in das Bewußtsein.",
        "Und darauf beruhte eben jenes damals noch vorhandene atavistische Hellsehen.",
        "Es drangen gewisse Impulse damals herein aus dem Universum und machten sich geltend als atavistische Schauun­gen.",
        "So daß wir sagen können: Ganz undurchsichtig - ich meine jetzt intellektuell undurchsichtig - wurde dieses Außen erst seit dem 8. vor-christlichen Jahrhundert, und es wurde immer mehr und mehr un­durchsichtig. - Jetzt leben wir im fünften nachatlantischen Zeitraum.",
        "Es ist ja undurchsichtig geblieben.",
        "Und darauf pochen ja die Leute"
      ],
      [
        "heute ganz außerordentlich, indem sie immerzu behaupten, daß über­haupt kein Mensch eindringen könne in jenes «Ding an sich», oder wie sie es dann nennen, was da jenseits dieser Grenze liegt."
      ],
      [
        "Dagegen darf gesagt werden, daß immer mehr und mehr sich eine andere Tendenz geltend macht und gegen den sechsten nachatlantischen Zeitraum sich immer mehr und mehr geltend machen wird.",
        "Das ist, es wird gewissermaßen diese Zone hier (links) durchiässig werden."
      ],
      [
        "Es wird die Zeit kommen, wo aus den Tiefen der Menschennatur das­jenige, was ich Ihnen gestern als das Brodelnde geschildert habe, als dasjenige, in das der Mensch nicht hinunterschauen soll - in dem Sinne vor allen Dingen nicht, wie die phantastischen Mystiker das wollen -, es wird aus diesem Gebiete von dem sechsten nachatlantischen Zeit­raum an gewissermaßen allerlei durchsickern wollen.",
        "Ja, es wird diese Zeit schon im fünften nachatlantischen Zeitraum beginnen, in unserem Zeitraum."
      ],
      [
        "Es wird allerlei durchsickern wollen.",
        "Es wird sich das ja vor allen Dingen dadurch äußern, daß viel mehr Menschen, als man heute denkt, immer mehr und mehr aus gewissen rein inneren Erfah­rungen entnehmen werden, daß es wiederholte Erdenleben gibt und dergleichen."
      ],
      [
        "Diese Dinge kommen, man möchte sagen, heute schon, obwohl spärlich, zum Durchbruche.",
        "Ich habe öfter, hier ja wohl auch schon, den Namen eines merkwürdigen Menschen der Gegenwart genannt, des Otto Weininger, der ja besonders bekanntgeworden ist durch sein dickes Buch «Geschlecht und Charakter»."
      ],
      [
        "Noch interessan­ter aber ist dasjenige Buch, das nach seinem Tode sein Freund Rappa­port herausgegeben hat, und in dem allerlei außerordentlich Interes­santes drinnensteht.",
        "Es sind zum großen Teil Aphorismen."
      ],
      [
        "Das Ganze trägt den Titel «Über die letzten Dinge».",
        "Einer dieser Apho­rismen besagt ungefähr dieses: Weininger behauptet, die Seele des Menschen hätte in ihrem vorgeburtlichen Leben ein gewisses Grauen vor sich selber zur Entwickelung gebracht und hätte dadurch die Sehn­sucht bekommen, dieses Leben zu vergessen und sich in das Vergessen hineinzustürzen, was die Verleiblichung bedeutete. - Also Weininger spricht vollständig von dem vorgeburtlichen Leben, von dem Ver-leiblichen; nur spricht er in seiner düsteren, pessimistischen An­schauung davon, daß die Seele sich zu betäuben sucht gegenüber"
      ],
      [
        "ihrem vorgeburtlichen Leben, und die Betäubung sucht sie in der Verleiblichung in einem physischen Menschenleib."
      ],
      [
        "Aber solche unmittelbaren Eindrücke heutiger Menschen von dem Wege der Seele gibt es ja viele, und sie werden immer zahlreicher und zahlreicher werden.",
        "Bei solch einem Menschen wie Weininger kann man schon heute sehen, wie dichter, kompakter möchte ich sagen, das Ich innerlich den Menschen anfaßt.",
        "Bei Weininger sieht man schon deutlich, wie diese Grenze etwas durchlässig wird und da allerlei her­aufdringt.",
        "Interessant ist es zum Beispiel, welche Notiz er hingeschrie­ben hat über seinen eigenen Tod.",
        "Er verübte frühzeitig, mit dreiund­zwanzig Jahren schon, Selbstmord.",
        "Er schrieb eine ganze Reihe von Notizen nieder, die außerordentlich interessant sind, weil sie geradezu Imaginationen astralischen Schauens darstellen.",
        "Das alles paarte sich mit einem gewissen Charakterzug, der ihn dann dahin führte, eines Tages sich einzumieten in Beethovens Sterbehaus in Wien und in diesem sich gleich am nächsten Morgen selber zu ermorden, mit drei­undzwanzig Jahren.",
        "Und darüber schrieb er die Notiz, daß er sich ermorden müsse, weil er sonst fürchten müsse, getrieben zu werden durch einen unbestimmten Drang, ein Mörder zu werden, einen andern ermorden zu müssen."
      ],
      [
        "Man sieht, da rumoren furchtbarste Dinge in der Seele eines außer­ordentlichen genialischen Menschen, die nicht so ohne weiteres be­zwungen werden können durch das, was in seinem Bewußtsein ist, weil da vieles aus diesem Unterbewußten herauf rumort.",
        "Sie werden begreifen, daß man schon mit einem gewissen Recht darauf hinweisen muß, daß die gewöhnliche Gescheitheit, die der Mensch jetzt ent­wickeln kann, nicht ausreicht, um das, was da aus den unbekannten Tiefen herauf kommt, zu erkennen.",
        "Denn es sollte ja gar nicht herauf­kommen, es sollte da unten bleiben, aber es wird doch heraufkommen.",
        "Geradeso wie bis zum Jahre 747 vor Christus von außen etwas herein­gekommen ist, so wird nachher von innen etwas aufsteigen.",
        "Durch das, was der Mensch sich erringen wird an gewöhnlicher, normaler Ge­scheitheit, wird das nicht bezwungen werden können, bei weitem nicht bezwungen werden können.",
        "Da wird man eben brauchen jenes Ver­stehen der Welt, welches durch die Geisteswissenschaft zu erwerben"
      ],
      [
        "ist.",
        "Es wird Harmonie, innerliche Festigkeit und innerliche Gediegen­heit in das menschliche Seelenleben nur eindringen können, wenn die Menschen dieses innerliche Seelenleben werden ordnen, harmonisie­ren wollen durch dasjenige, was aus der Erkenntnis des Geistes heraus errungen werden kann.",
        "Es strebt die Entwickelung der Menschheit also aus einem Zustande heraus, in welchem von der Außenwelt mehr wahrnehmbar war, als heute wahrnehmbar ist, und es strebt diese Ent­wickelung der Menschheit einem Zustande zu, in welchem aus dem tiefsten Inneren des Menschen mehr auftauchen wird, als heute im Normalzustand auftaucht."
      ],
      [
        "Diese Dinge, von denen ich jetzt spreche, sie kennt man eigentlich in den eingeweihten Kreisen da und dort sehr gut.",
        "Von jenem alten Erkennen, das bis ins 8. vorchristliche Jahrhundert den Menschen zu­gänglich war, spricht ja noch das ganze morgenländische Geistesleben, das ganze asiatische Geistesleben."
      ],
      [
        "Ja, es spricht nicht nur das Geistes­leben, es spricht im Grunde genommen die ganze asiatische Kultur davon.",
        "Daher kommt es, daß es eigentlich so schwer verständlich ist für den Europäer, wenn heute der Orientale, der asiatische Orientale von seiner Kultur spricht."
      ],
      [
        "Da muß man schon, wenn man diese Leute verstehen will, sich hineinfinden in eine andere Art, die Vorstellungen, die Gedanken zu bilden.",
        "Heute würde es zum Beispiel für sehr viele Menschen sehr interessant sein niüssen, so etwas Tonangebendes zu verfolgen, wie die Rede ist, welche Rabindranath Tagore, der Inder, ge­halten hat über den Geist Japans."
      ],
      [
        "Sie wissen: Tagore ist der von der Nobel-Stiftung preisgekrönte Inder.",
        "Er hat über den Geist Japans einen Vortrag gehalten.",
        "Es ist weniger wichtig, was er über den Geist Japans gerade spricht, als der Geist, aus dem heraus er spricht, der Geist des heutigen Orientalen, der nur verstanden werden kann, wenn man weiß, daß etwas in den Orientalen noch zurückgeblieben ist von jenem Her­auf-, von jenem Hereinkommen der Außenwelt, wie es heute nicht perzi­pierbar ist."
      ],
      [
        "Für die meisten Europäer reden die Orientalen, wenn sie im Sinne ihrer Kultur reden, eben eigentlich etwas ziemlich Unverständ­liches.",
        "Man versteht gewöhnlich gar nicht, wovon sie eigentlich reden."
      ],
      [
        "Auch die andere Erscheinung kommt vor, daß dasjenige, was eigent­lich erst in der Zukunft auftreten sollte, in einer gewissen Weise dann"
      ],
      [
        "vorweggenommen wird.",
        "Vergleichen könnte ich das damit, daß ich hinweise auf Kinder, die als Kinder schon greisenhaft sind.",
        "Sie neh­men das Greisenhafte als Kinder schon voraus.",
        "Da ist die Unregel-mäßigkeit in der Entwickelung dadurch eingetreten, daß etwas, das später kommen sollte, früher hereingeschoben ist, in eine frühere Zeit."
      ],
      [
        "Während nun im orientalischen Denken, in der orientalischen An­schauungsweise gerade bei den hervorragendsten Geistern ein aus alter Zeit Zurückgebliebenes in der Weise herrscht, wie ich es eben angedeutet habe, herrscht namentlich bei so ganz im Sinne des Ameri­kanismus denkenden Geistern ein Hereinnehmen von Späterem, ein Hereinschieben von Späterem.",
        "Da merkt man deutlich, wenn man auf solche Sachen eingehen kann, daß gerade hervorragendere Geister vieles von dem haben, was da (links) durchsickert."
      ],
      [
        "Sie bekommen eine Vorstellung von solchem Durchsickerndem, wenn Sie zum Bei­spiel jenen Essay lesen, den Woodrow Wilson geschrieben hat über die Entwickelung des amerikanischen, des nordamerikanischen Volkes im besonderen.",
        "Man kann sich nichts denken, das mehr den Nagel auf den Kopf trifft, das treffender wäre als dieser Essay, den Woodrow Wilson über die Entwickelung des amerikanischen Volkes geschrieben hat."
      ],
      [
        "Da ist jedes Wort darinnen so, daß man das Gefühl hat: es ist die Sache in der allerallerschärfsten Weise charakterisiert und getroffen.",
        "Und das fällt insbesondere deshalb auf, weil Wilson in diesem Fall sehr scharf aufmerksam macht darauf, daß eine ganze Anzahl von Leuten auch in Amerika die Ansicht haben, die eigentlich nur zu rechtfertigen ist, wenn man das amerikanische Volk heute noch auffaßt - wogegen er, Woodrow Wilson, sich wendet - gleichsam als eine Dependance des englischen Volkes."
      ],
      [
        "Diese Menschen, die heute noch die Amerika­ner so auffassen, als ob diese etwas wären wie Abkömmlinge, wie ein Zweig der europäischen Engländer, diese Leute lehnt Woodrow Wil­son im strengsten Sinne des Wortes ab.",
        "Die verstehen nichts, meint er, von der eigentlichen Entwickelung des amerikanischen Volkes im 19."
      ],
      [
        "Jahrhundert.",
        "Denn der Amerikaner beginnt von innen erst Ame­rikaner zu sein - so spricht Wilson aus echt amerikanischem Geiste heraus, außerordentlich prägnant und treffend - in dem Momente, wo er aufhört anzuknüpfen mit seinem Seelenhaften an das, was von England"
      ],
      [
        "herübergekommen ist, wo er beginnt, als Bebauer des Bodens von Osten nach dem Westen hinüberzudringen, von der amerikani­schen Ostküste nach der Westküste hinüberzudringen.",
        "In diesem Aus­roden der Urwäider, in der Arbeit mit der Flinte, in der Arbeit mit dem Spaten, in der Arbeit mit dem Pflug und dem Pferde, in diesem Über­winden jenes Widerstandes, der zu überwinden ist bei der Arbeit von dem Osten nach dem Westen hinüber, entwickelt sich für ihn der Westmann, der «WesterneD>, wie er es nennt.",
        "Und in dieser Art und Weise der Eroberung des Bodens sieht er, so daß es unmittelbar über. zeugendsten Eindruck macht, den eigentlichen Nerv der amerikani­schen Entwickelung.",
        "Man hat überall gerade das Gefühl - man muß natürlich verstehen, das Wie zu lesen in einem solchen Fall, nicht bloß das Was -, da spricht viel mehr als der Wilson.",
        "Denn wenn der Wilson selber spricht - ja, da wird nicht viel Gescheites daraus.",
        "Da spricht viel mehr, da spricht dasjenige, wovon der Mann als von seinem eigenen Inneren her besessen ist, da sprechen Därnonennaturen, die geradezu grandiose Zukunftsgeheimnisse eingeben.",
        "In diese Geheim­nisse müßte eigentlich die Menschheit eindringen, wenn die Ent­wickelung verstanden werden soll."
      ],
      [
        "Man muß heute tatsächlich einen Unterschied machen zwischen der bloßen wissenschaftlichen und zeitungsgemäßen Erfassung der Welt, die ja bequem ist, die auch allbeliebt ist, und der wahren Erfassung der Welt.",
        "Die wahre Erfassung der Welt, die muß solche Gegensätze sich klarmachen können wie die, welche ich jetzt auseinandergesetzt habe:"
      ],
      [
        "von dem Hereinkommen bei den orientalischen Völkern von etwas, das da draußen liegt (siehe Zeichnung Seite 45, rechts) ; von dem Heraufkommen bei den amerikanischen Völkern von etwas, was da drinnen (links) liegt.",
        "Und was da heraufkommt, es braucht das nicht etwas bloß Verwerfliches zu sein, es kann in gewissem Sinne grandiose ahrimanische Offenbarung sein, die da heraufkommt.",
        "Denn ahrima-nische Offenbarung ist es im wesentlichen, welche in jenem ausge­zeichneten Aufsatze von Woodrow Wilson über die Entwickelung des amerikanischen Volkes gegeben ist."
      ],
      [
        "Die Eingeweihten des Ostens und die Eingeweihten des amerikani­schen Volkes, die wissen auch das Nötige aus diesen Dingen zu machen."
      ],
      [
        "Man will von beiden Seiten die Entwickelung der Menschheit durchaus in gewisse Bahnen bringen.",
        "Die orientalischen Völker, das heißt ihre Eingeweihten, haben ganz bestimmte Absichten für die Zukunftsentwickelung der Menschheit."
      ],
      [
        "Diese Leute sehen, was in der Entwickelung richtig liegt und versuchen dasjenige, was in der Ent­wickelung richtig liegt, soweit der Mensch es beeinflussen kann, zu beeinflussen.",
        "Sie suchen ihm eine gewisse Richtung, einen gewissen Impuls zu geben."
      ],
      [
        "Und der Impuls, der da von den orientalischen Ein­geweihten der Entwickelung gegeben werden will, der beruht im wesentlichen darauf, daß man nicht mehr rechnen will, so ungefähr nach der Häffte der sechsten nachatlantischen Zeit, auf die mensch­liche Generation.",
        "Man möchte verzichten auf das irdische Menschen­geschlecht nach dieser Zeit."
      ],
      [
        "Man möchte die Entwickelung der Menschheit dahin bringen, daß die Menschen nachher eigentlich nicht mehr so recht physische Nachkommen haben, daß die Seelen dann schon sich vergeistigen, nicht mehr auf die Erde herunterkommen in Verleiblichungen.",
        "Man möchte das Reich des Geistes für die Mensch­heit schon von der Mitte der sechsten nachatlantischen Zeit an be­gründen."
      ],
      [
        "Dies würde man nur können, wenn man gewisse Kultur­ingredienzien abweisen würde.",
        "Nicht nur die Eingeweihten des Orients, sondern eigentlich instinktiv jeder gebildete Orientale lehnt daher im eminentesten Sinne gewisse Europäismen ab ; gerade die­jenigen Europäismen, auf die der Europäer ganz besonders stolz ist, lehnt er ab."
      ],
      [
        "Er lehnt ab namentlich alles dasjenige, was sich ja aus der rein technischen, materiellen Kultur in Europa und seinem Anhange Amerika ergeben hat.",
        "Wer die Entwickelung der Menschheit studiert, namentlich im 19."
      ],
      [
        "Jahrhundert und in das 20.",
        "Jahrhundert herein, der wird finden, daß man mit Recht sagt: Die Techhik hat es ungeheuer weit gebracht, die Technik hat den Menschen Arbeitskräfte abge­nommen.",
        "Wenn man heute davon redet, die Erde habe so und so viel hundert Millionen Einwohner, so ist dieses eigentlich nicht ganz richtig, weil man auch rechnen kann, wieviel die Erde Einwohner hat nach dem, wieviel gearbeitet wird."
      ],
      [
        "Nun wird mit vollständigem Recht gesagt, daß seit dem letzten Drittel des 18.",
        "Jahrhunderts von den Maschinen, die nach und nach entstanden sind, menschliche Arbeitskraft"
      ],
      [
        "verrichtet wird.",
        "Man kann berechnen, ziemlich exakt berechnen, wieviel Millionen Menschen mehr die Erde haben müßte, wenn alle die Arbeit, die von den Maschinen verrichtet wird, von den Menschen verrichtet würde.",
        "Die Erde müßte fünfhundert Millionen Menschen mehr haben.",
        "Man kann schon sagen: Heute sind auf der Erde nicht nur diejenigen Menschen mit zwei Beinen und einem Kopf, die statistisch berechnet werden können, sondern fünfhundert Millionen mehr, gemessen an der Arbeitskraft; die Arbeitskraft wird eben von Maschlnen verrichtet."
      ],
      [
        "Aber es gibt nichts Materielles, hinter dem nicht ein Geistiges steht.",
        "Diese fünfhundert Millionen Menschenkräfte, die sind die Gelegen­heit zum Aufenthalte von ebensovielen ahrimanischen Dämonen innerhalb der menschlichen Kultur.",
        "Diese ahrimanischen Dämonen sind einmal da.",
        "Und diese ahrimanischen Dänionen, die lehnt der Orientale aus einem gewissen Instinkt heraus radikal ab ; die will er nicht.",
        "Das sehen Sie eigentlich aus jeder Manifestation eines feingebil­deten Orientalen heraus, daß er diese ahrimanische Dämonologie ab­lehnt.",
        "Denn diese ahrimanische Dämonologie, die gibt dem Menschen eine gewisse Schwere, die niemals möglich macht, daß dasjenige ge­schleht, was die orientalische Initiation anstrebt: daß das Menschen­geschlecht mit der Mitte der sechsten nachatlantischen Zeit physisch aufhört auf der Erde zu sein, weil die Menschen zurückgehalten wer­den durch das, was sich auf diese Weise dämonologisch-ahrimanisch entwickelt."
      ],
      [
        "Einem andern Ziel streben die Eingeweihten des Amerikanismus zu.",
        "Sie streben dem entgegengesetzten Ziele zu.",
        "Sie streben danach, eine innigere Gemeinschaft zu bilden, als im normalen Verlauf der Mensch­heitsentwickelung geschehen soll, zwischen den Menschenseelen und derjenigen Leiblichkeit, welche auf der Erde zu finden sein wird, der dichten, groben Leiblichkeit, die auf der Erde zu finden sein wird von dem sechsten nachatlantischen Zeitraume an.",
        "Die seelische Kultur wird sehr vertieft sein, aber die leibliche wird grob sein.",
        "Aber eine innigere Verbindung mit dieser groben Leiblichkeit strebt man im amerikanischen Westen an, eine innigere Verbindung als die normale ist, ein stärkeres Untertauchen in die Leiblichkeit.",
        "Man will entgegenkommen"
      ],
      [
        "dem, was da durchsickert (siehe Zeichnung Seite 45, links), will ihm entgegengehen durch stärkeres Eindringen in die Leiblich­keit.",
        "Während man also eine Kultur begründen will von seiten der Orientalen, die nicht rechnet mit den Menschenleibern der späteren Erdenentwickelung, will man die Seelen ketten an diese spätere Erdenentwickelung innerhalb der amerikanischen Kultur des Westens.",
        "Man will die Leiber möglichst so gestalten, daß die Seelen, wenn sie durch den Tod gegangen sind, möglichst bald wiederum in einen Leib herunterkommen können, daß sie möglichst wenig sich aufhalten in der geistigen Welt.",
        "Man will die Seelen möglichst abhalten von einem Aufenthalt in der geistigen Welt, man will, daß sie möglichst bald wiederum auf die Erde herunterkommen.",
        "Man will sie innigst ver­binden mit dem Leben der Erde."
      ],
      [
        "Das sind Tendenzen, die man kennenlernen muß.",
        "So sonderbar es dem heutigen Menschen noch erscheint, wenn man von diesen Ten­denzen spricht, so schädlich ist es ihm, daß sie übersehen werden.",
        "Denn notwendig ist, daß der Mensch sich mit vollem Bewußtsein hin-einstellt in dasjenige, das eigentlich mit ihm selbst gewollt wird und demgegenüber er oftmals leider, leider so steht, daß man sagen kann:"
      ],
      [
        "er läßt alles mögliche mit sich geschehen."
      ],
      [
        "Aber dieses westliche Ideal, diese Dämonologisierung des Men­schen, das wird nur erreicht werden können, wenn der geistige, psy­chische Amerikanismus unterstützt werden kann von einer andern Weltanschauungsströmung, die viel verwandter mit dem Amerikanis­mus ist, als man denkt.",
        "Sie haben ja gesehen: Es ist wesentlich ein Hin-neigen des Amerikanismus zur Ahrimankultur, was das Ausschlag­gebende ist.",
        "Aber eine richtige Förderung würde dieser Amerikanis­mus erhalten können, wenn er unterstützt würde von einer andern Weltanschauung, die viel verwandter mit ihm ist, als man denkt.",
        "Das ist der Jesuitismus.",
        "Jesuitismus und Amerikanismus sind zwei sehr, sehr verwandte Dinge.",
        "Denn als der fünfte nachatlantische Zeitraum begann, da handelte es sich darum, einen Impuls zu finden, durch den man sich in den Stand setzen konnte, die Menschen möglichst hinweg-zuführen von dem Verständnisse des Christus.",
        "Und diejenige Bestre­bung in der Kulturentwickelung, welche es sich zur Aufgabe gesetzt"
      ],
      [
        "hat, kein Verständnis des Christus aufkommen zu lassen, das Ver­stänanis des Christus vollständig zu untergraben, das ist der Jesuitis­mus.",
        "Der Jesuitismus strebt danach, allmählich jede Möglichkeit eines Christus-Verständnisses auszurotten."
      ],
      [
        "Denn dasjenige, was da zugrun­de liegt, das hängt schon mit einem tiefen Mysterium zusammen.",
        "Da-mit, daß etwas von außen (siehe Zeichnung Seite 45, rechts) immer da hereinkam in das menschliche Innere, hängt es zusammen, wie ich sagte, daß die Menschen vorher, vor dem 7., 8. vorchristlichen Jahr­hundert, atavistisches Hellsehen hatten."
      ],
      [
        "Aber durch dieses atavistische Hellsehen sahen sie auch im Universum den Christus.",
        "Der Christus war etwas, was sie sehen konnten im alten Hellsehen.",
        "Ich habe das ja oft dargestellt, ich habe es dargestellt in der «Geheimwissenschaft im Umriß», und der ganze Sinn meines Buches «Das Christentum als mystische Tatsache» gipfelt ja schließlich darin."
      ],
      [
        "Man sah den Christus im Kosmos, man sah den Christus im Universum.",
        "Aber nun denken Sie: Vom 7., 8. vorchristlichen Jahrhundert ab haben wir Menschen die Möglichkeit verloren, in das Universum hinauszuschauen."
      ],
      [
        "Was hätten denn die Menschen mitverloren, wenn nichts anderes gekom­men wäre, dadurch, daß sie gar nicht mehr hinausschauen konnten ins Universum?",
        "Was hätten die Menschen verloren?",
        "Die Möglichkeit, von einem Christus-Geiste überhaupt etwas zu wissen, wenn der Christus nicht zu ihnen gekommen wäre durch das Mysterium von Golgatha, wenn der Christus nicht auf die Erde heruntergekommen wäre."
      ],
      [
        "In dem historischen Zeitmomente, wo die Menschen nicht mehr den Christus im Kosmos schauen konnten, kam der Christus auf die Erde herunter, verband sich mit dem Jesus.",
        "Von da ab war es des Menschen Aufgabe, den Christus in dem Menschen zu erfassen."
      ],
      [
        "Und gerettet werden muß die Möglichkeit, daß mit dem, was da durch­sickert (siehe Zeichnung, rechts), der Christus erkannt werde.",
        "Denn der Christus ist zu den Menschen heruntergestiegen.",
        "Der Jesus ist ein Mensch, in dem der Christus gewohnt hat."
      ],
      [
        "Wirkliche menschliche Selbsterkenntnis muß den Jesus-Keim tragen.",
        "Dadurch wird man in die Zukunft übersiedeln können.",
        "Tief begründet ist es, daß wir von einem Christus Jesus sprechen.",
        "Denn der Christus entspricht dem Kos­mischen ; aber dieses Kosmische ist auf die Erde heruntergekommen"
      ],
      [
        "und hat in dem Jesus Wohnung genommen, und der Jesus entspricht dem Irdischen mit der ganzen irdischen Zukunft."
      ],
      [
        "Will man den Menschen abschließen vom Geistigen, so nimmt man ihm den Christus.",
        "Dann hat man die Möglichkeit, den Jesus so zu benützen, daß die Erde nur in ihrem irdischen Aspekt vorhanden bleibt.",
        "Sie werden daher beim Jesuitismus eine fortwährende Be­kämpfung der Christologie finden, dagegen ein scharfes Betonen des­sen, daß man ein Heer ist, eine Armee für den Jesus.",
        "Ja, natürlich:"
      ],
      [
        "Geisteswissenschaft ist schon ein Mittel, daß solche Dinge erkannt werden, daß den Menschen die Schuppen von den Augen fallen.",
        "Da­her werden jene, die nicht erkannt sein wollen, immer wütender und wütender werden auf dasjenige, was Geisteswissenschaft will."
      ],
      [
        "Wüten­der, man sieht es: Das Juliheft der jesuitischen Zeitschrift «Stimmen der Zeit» - früher «Stimmen aus Maria-Laach» - enthält nicht nur einen, sondern gleich zwei Artikel gegen mich.",
        "Und wer dieses im Zusammenhang zu denken vermag mit dem, was sonst jetzt sich an neuen Aspirationen des Jesuitismus in der Welt entwickelt, der wird daraus überhaupt etwas Tieferes sehen können."
      ],
      [
        "Nur leider, man spricht ja von solchen Dingen heute doch zumeist vor einer schlafen­den Menschheit.",
        "Die Menschen lieben es, die wichtigsten Dinge zu vrschlafen, nicht hinzuhören auf dasjenige, was nun wirklich zu­kunifbestimmend ist."
      ],
      [
        "Daher werden die Menschen jetzt von allen Dingen, wie ich vorgestern sagte, überrascht.",
        "Sie wollen ja auch über­rascht sein.",
        "Spricht man möglichst früh von den Dingen, die im Schoße der Zeit liegen, so betrachten die Menschen das als etwas Unbequemes, weil sie möglichst lange gut brav bürgerlich bequem auf ihren Polster­sesseln sitzen möchten, auch wenn sie verantwortungsvolle, führende Menschheitsstellen innehaben."
      ],
      [
        "Aber diejenigen, welche sich für Geisteswissenschaft interessieren, sollten schon sich in die Seelen ein­gravieren, daß man alles tun wird, um diese Geisteswissenschaft un­wirksam zu machen.",
        "Es ist nicht gerade gut, wenn auch wir innerhalb unserer Kreise allzusehr schlafen mit Bezug auf die Beobachtung des­jenigen, was in der Welt vorgeht."
      ],
      [
        "Zuweilen ist es ja recht schwierig, zu sehen, wie doch immer alles, was so persönlich spielt, höhergestellt wird als dasjenige, was in der"
      ],
      [
        "gegenwärtigen Zeit so ganz besonders wichtig und wesentlich ist: das Hinschauen auf die großen Angelegenheiten der Menschheit, die sich langsam vorbereiten.",
        "Die Angriffe, die zu tun haben mit den großen Wollungen, die kommen schon von den verschiedensten gegnerischen, ernst zu nehmenden Seiten.",
        "Solch ein Angriff wie der, von dem ich eben gesprochen habe, er ist schon in gewissem Sinne ernster zu neh­men.",
        "Man muß ihn in der richtigen Weise taxieren können.",
        "Nicht ernst zu nehmen nach dieser Richtung hin sind ja natürlich jene schö­nen Angriffe, welche aus dem Unterirdischen unserer Gesellschaft selber immer wiederum auftauchen, und die ja zum Teil bloß deshalb ein böses Ansehen haben, weil immer wieder und wiederum die Ten­denz bemerkbar ist, daß man gerade die größte, liebevollste Teilnahme gegenüber jenen Leuten hat, welche dasjenige, was ernst erstrebt wird in unseren Reihen, verlästern, zu verunglimpfen suchen und derglei­chen.",
        "Und erst wenn das Unheil da ist, dann entschließt man sich nach und nach, wirklich zu sehen ; vorher werden manche Leute gehätschelt, welche dann das Unheil bringen."
      ],
      [
        "Ich sage dies nicht, weil ich daran denke, daß das oder jenes anders sein sollte, sondern weil ich mich wirklich verpflichtet fühle, darauf aufmerksam zu machen, daß die Menschheit aufwachen muß, und daß wir vor allen Dingen zu denen gehören müssen, welche nach Wachheit streben."
      ],
      [
        "Auf gewissen Gebieten kann man ja heute alles mögliche tun.",
        "Der von mir hier gemeinte Schlaf der Menschheit, der nur überwunden werden kann durch ein Eindringen in die geistigen Welten, der ist außerordentlich schwer zu überwinden, der Schlaf der Menschen.",
        "Und mit Bezug auf die Verbreitung des geisteswissenschaftlichen Erkennt­nisgutes hat man es vielfach gerade mit diesem Schlaf zu tun als dem Gegner.",
        "Ich will dabei gar nicht von einer einzelnen Erscheinung sprechen, sondern in der ganzen Kulturbewegung ist gegenwärtig etwas Schläfriges gegenüber den eigentlichen Impulsen, die überall, an allen Stellen den Menschen über den Kopf hinauswachsen.",
        "Zwei Dinge sind notwendig, die man sich wie goldene Regeln eigentlich einschrei­ben müßte in seine Seele: Niemals war mehr als in unserem fünften nachatlantischen Zeitraum die Notwendigkeit vorhanden, daß die"
      ],
      [
        "Menschen sich immer mehr und mehr bemühen - und daß Menschen da sind, die das können, daran ist nicht zu zweifeln -, gerade das zu erreichen, was besonders wertvoll ist: geisteswissenschaftliche Er­kenntnisse zu verstehen.",
        "Gewiß, geisteswissenschaftllche Erkenntnisse müssen gesucht werden durch hellsichtiges Eindringen in die geistige Welt ; das ist eine Notwendigkeit."
      ],
      [
        "Aber das ist eine Selbstverständ­lichkeit, daß es Hellseher geben muß, die eindringen in die geistige Welt, daß es Leute geben muß, die übersinnliche Erkenntnisse an­streben.",
        "Zweitens aber ist besonders wichtig, daß sich für diese geistes-wissenschaftlichen Erkenntnisse, für diese in übersinnlichen Welten gesuchte Erkenntnis Leute finden, die kraft des Intellekts die Sache verstehen."
      ],
      [
        "Das vernünftige, verständige Begreifen der Geisteswissen­schaft, das ist heute ganz besonders notwendig, denn das ist dasjenige, wodurch die widerstrebendsten Kulturmächte gerade überwunden werden.",
        "Der Intellekt der Menschen ist heute so groß, daß die ganze Geisteswissenschaft verstanden werden kann, wenn man nur will."
      ],
      [
        "Und gerade dieses Verständnis anzustreben, ist ein allgemein-menschliches, nicht ein egoistisches Interesse der Kultur.",
        "Denn dieses Verständnis kann angestrebt werden, wenn jene intellektuellen Kräfte, die heute verwendet werden auf naturwissenschaftlichen Gebieten an allerlei Kleinkram, wenn jene intellektuellen Kräfte, die heute volkswirt­schaftlich recht fruchtlos verwendet werden, und endlich, wenn jene Kräfte, die in einer fruchtlosen, vielleicht sogar menschenmörderi­schen Technik verwendet werden, entsprechend angewendet würden, und die Menschen nicht verzogen würden von frühester Kindheit an."
      ],
      [
        "Dann würde man sehen, wie leicht das spirituelle Geistesgut wirklich zum Verständnisse der Menschheit gebracht werden könnte.",
        "Das ist das eine."
      ],
      [
        "Die andere goldene Regel ist diese, daß man heute noch etwas an­deres braucht für das Fruchtbarmachen des spirituellen Geistesgutes für unsere Kultur.",
        "Das erste ist etwas, was Ahriman abgerungen wer­den muß.",
        "Die Menschen sind heute schon gescheit, denn Ahriman sorgt dafür, daß die Menschen gescheit sind.",
        "Oh, die Menschen sind gescheit!",
        "Sie verwenden ihre Gescheitheit eben nur im materialisti­schen Interesse.",
        "Die Menschen sind nicht nur gescheit, sie sind übergescheit."
      ],
      [
        "Davon werden wir aber in den nächsten Vorträgen noch sprechen, damit Sie sehen, welchen ungeheuren Einfluß gerade das ahrimanische Element auf die menschliche Übergescheitheit der heu­tigen Zeit hat.",
        "Aber noch etwas anderes ist notwendig."
      ],
      [
        "Noch einem andern Geiste ist manches abzuringen.",
        "Wir brauchen nicht nur Ge­scheitheit, mit der das spirituelle Geistesgut durchdrungen werden soll, wir brauchen vor allen Dingen sehr, sehr dringlich - ja, wie soll ich es ausdrücken -, wir brauchen bei den Menschenseelen, an die das spiri­tuelle Geistesgut herankommt, Temperament, Enthusiasmus, Feuer, Wärme."
      ],
      [
        "Wir brauchen Menschen, welche mit der ganzen, vollen Seele dasjenige vertreten, was spirituelles Geistesgut ist.",
        "Gerade auf spiri­tuellem Gebiete muß den luziferischen Kräften, die sonst so wirksam jetzt sind in der Welt, dieses abgerungen werden."
      ],
      [
        "Es gibt einen schö­nen Anblick: es ist der Anblick desjenigen, der in ruhiger Klarheit, aber mit innerem Feuer und Enthusiasmus, weil es ihm eine Notwen­digkeit ist, für das spirituelle Geistesgut sich erwärmen kann.",
        "Es gibt einen andern Anblick: das ist der, wo man möglichst versucht, durch das spirituelle Geistesgut eingelullt zu werden, träumerisch zu werden, hingegossen warm zu werden, aufzugehen in die universellen Kräfte, die Seele zu vereinigen mit dem göttlichen All."
      ],
      [
        "Das sind Gegensätze, die man in der Gegenwart doch wohi beobachten kann, Gegensätze, die es notwendig ist, zu beobachten.",
        "Denn es wird nicht leicht werden, das spirituelle Geistesgut der Menschenkultur einzuverleiben."
      ],
      [
        "Und es muß hinein, denn die Menschenkultur braucht es.",
        "Man wird über vieles ganz, ganz anders nicht nur denken lernen müssen, sondern auch fühlen und empfinden lernen müssen."
      ],
      [
        "Ja, ich könnte noch manches sagen in Anknüpfung an dasjenige, was ich jetzt eben ausgesprochen habe, aber ich will vielleicht lieber schweigen und will Ihnen Gelegenheit geben, nachzudenken.",
        "Man kann über manches nachdenken, was angeregt werden könnte durch manche Tücke, welche ich ganz absichtlich in die eben ausgesprochene Wahrheit hineingelegt habe.",
        "Nun, davon wollen wir dann das nächste Mal weiter sprechen."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG Dornach, 24. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Wenn man eine Zeit, in der man selbst lebt, verstehen will, so muß man sie aus größeren Weltenzusammenhängen heraus verstehen. Das ist gerade das Kleinliche der gegenwärtigen Zeit, daß man nicht will die Impulse, die Kräfte, die wirksam sind in der Gegenwart, aus größe-rem Zusammenhang heraus sich klarmachen. Und insbesondere wird es immer wieder und wiederum notwendig sein, um das eine oder das andere gegenwärtig Wirksame zu verstehen, zurückzugreifen zu den Verhältnissen, durch welche die Menschheitsentwickelung gegangen ist zur Zeit des Mysteriums von Golgatha. Dieses Mysterium von Golgatha, wir haben es ja von den verschiedensten Gesichtspunkten aus dargestellt und haben gesehen, wie tief, wie bedeutsam es eingreift in den ganzen Evolutionsgang, die ganze Entwickelung der Mensch­heit. Wir wissen, daß die Menschen vor dem Mysterium von Golgatha anders die Welt empfanden, anders anschauten als nach dem Myste­rium von Golgatha. Natürlich geht das nicht so auf einmal aus dem einen Zustand in den andern Zustand über. Aber der rückschauenden Betrachtung ergibt sich schon dasjenige, was wir von den verschie­densten Gesichtspunkten aus dargelegt haben. Insbesondere möchte ich heute, um eine gewisse Grundlage für die nächsten Betrachtungen zu finden, auf eines hinweisen.",
      "Wenn wir die Stimmung, die Verfassung der Menschenseelen vor dem Mysterium von Golgatha betrachten, so können wir im allge­meinen sagen, daß innerhalb der Kulturmenschheit, also de4enigen Menschheit, aus der die heutige Kulturmenschheit hervorgegangen ist, vor dem Mysteruim von Golgatha eine gewisse Fähigkeit in den Seelen vorhanden war, in die Geheimnisse der kosmischen, geistigen Welt hineinzuschauen. Es war für die Menschen vor dem Mysterium von Golgatha gewissermaßen selbstverständlich, nicht so zum Ster­nenhimmel hinaufzuschauen, wie heute der Mensch zum Sternen-himmel hinaufschaut. Wir wissen ja, heute schaut der Mensch zum Sternenhimmel hinauf, indem er sich sagt: Mit unserer Erde sind",
      "einige andere Planeten verbunden, die mit ihr zusammen um die Sonne kreisen; dann sind unzählige andere Fixsterne da, die wiederum ihre Planeten haben. - Und wenn dann der Mensch darauf achtet, was er eigentlich, indem er sich so etwas überlegt, für einen Gedanken hat, so muß er sich doch sagen, er hat den Gedanken einer großen Welt-maschinerie. Daß da noch anderes waltet und wirkt als die Kräfte dieser großen Weltmaschinerie, das macht sich der Mensch der Ge­genwart nur sehr, sehr wenig klar.",
      "Das war mehr oder weniger für den Menschen vor dem Mysterium von Golgatha selbstverständlich. Insbesondere war für ihn selbstverständlich, die Sonne zum Beispiel nicht bloß als dasjenige anzuschauen, als was sie der heutige Pyhsiker anschaut, roh gesprochen, eine Art glühender Kugel im Weltenraume draußen, sondern der Mensch vor dem Mysterium von Golgatha wußte ganz genau: Diese Sonne, von der die Physik spricht, diese Sonne ist nur ein Element in der ganzen Sonne.",
      "Dieser Sonne liegt zu­grunde ein Seelisches und ein Geistiges. Und das Geistige, das dieser Sonne zugrunde liegt, sprach ja noch der griechische Weise als das allgemeine Weltgute an, als das Gute der Welt, als das einheitliche, die Welt durchwallende Gute.",
      "Das war ihm der Geist der Sonne. Ihm wäre es, diesem griechischen Weisen, als stärkster Aberglaube vorgekom­men, so zu denken, wie der heutige Physiker denkt, daß da draußen im Weltenraume einfach eine glühende Kugel schwebe; sondern ihm war diese glühende, schwebende Kugel die Offenbarung des einheit­lich Guten, das in der Welt zentral wirksam ist.",
      "Und mit diesem zen­tralen Guten, das geistiger Art ist, ist wiederum verbunden ein Seeli-sches: der Helios, wie es die Griechen nannten. Und erst das dritte, der physische Ausdruck des Guten und des Helios, war dann die phy­sische Sonne.",
      "Es sah also der Mensch damals an Stelle der Sonne ein Dreifaches. Und mit diesem Dreifachen, das in der Sonne in alten Zeiten gesehen worden ist, brachten diejenigen Menschen, welche in der Zeit des Mysteriums von Golgatha dachten - ausgerüstet mit dem Wissen dieses Mysteriums von Golgatha, ausgerüstet mit dem Wissen der alten Mysterien -, mit diesem dreifachen Sonnenmysterium brach­ten diese Weisen das Chnstus-Mysterium zusammen, das Mysterium von Golgatha selber.",
      "Mit der Sonnenverehrung war verbunden für",
      "diejenigen, die etwas wußten, die Christus-Verehrung. Mit der Sonnen­weisheit war wiederum für diejenigen, die etwas wußten, verbunden die Christus-Weisheit.",
      "Um aber das, was ich jetzt auseinandergesetzt habe, naturgemäß zu fühlen, als etwas Selbstverständliches zu empfinden, dazu war eben die Konstitution der Seele notwendig, die damals da war. Und diese Kon­stitution der Seele verschwand eben.",
      "Sie verschwand schon seit dem 8. vorchristlichen Jahrhundert, mit dem Jahre 747 - dies ist die wirk­kiche Gründungszahl von Rom - vor dem Mysterium von Golgatha. Mit der Gründung Roms schwindet eigentlich die alte Möglichkeit, in dem Kosmos draußen das Geistige zu sehen.",
      "Mit dem Eintritt Roms in die Geschichte tritt das in die Menschheitsevolution ein, was man das prosaische Element nennen kann. Die Griechen zum Bei­spiel bewahrten in ihrer ganzen Weltanschauung noch die Möglich­keit, hinter der Sonne eben die zwei andern Sonnen, die seelische und die geistige Sonne zu sehen.",
      "Und nur dadurch, daß nun nicht rein in griechische Weisheit und in griechisches Empfinden das Mysterium von Golgatha getaucht worden ist, sondern in römische Weisheit und in römisches Empfinden, dadurch ist es gekommen, daß man ge­brochen hat mit dem Wissen von dem Zusammenhang des Christus mit der geistigen Sonne. Damit haben sich ja namentlich die christ­lichen Kirchenväter und die christlichen Kirchenlehrer zu befassen gehabt, dieses Mysterium von der Sonne zu verhüllen, dieses Myste­rium von der Sonne für die Menschheit vergessen zu machen, es nicht herauskommen zu lassen.",
      "Es sollte gewissermaßen ein Schleier gebreitet werden durch die fortgehende Entwickelung des Christen­tums, wie man das nennt, über die tiefe, die bedeutsame, die um­fassende Weisheit von dem Zusammenhange des Christus mit dem Sonnenmysterium.",
      "Wenn man definieren sollte die Aufgabe der Kirche, jener Kirche, die entstanden ist dadurch, daß das Christentum in das Römertum eingesenkt worden ist, dann müßte man dies so tun, daß man sagte:",
      "Die römisch gefärbte christliche Kirche hatte sich namentlich zur Aufgabe zu machen, das Christus-Mysterium möglichst zu ver­hüllen, es möglichst wenig bekanntwerden zu lassen. - Die Einrichtung,",
      "welche die Kirche durch den Romanismus erfahren hat, die ist insbesondere geeignet gewesen, die Menschen so wenig wie moglich von dem Christus-Geheimnis wissen zu lassen. Die Kirche war da­durch eine Institution zur Geheimhaltung des Christus-Mysteriums geworden, eine Institution geworden, möglichst wenig in die Welt kommen zu lassen von dem Christus-Mysterium. Dies ist etwas, was immer mehr und mehr in der jetzigen Zeit der Menschheit klarwerden muß, weil beginnen muß diejenige Zeit, welche in der Lage ist, wie­derum mit andern Begriffen zu arbeiten als mit den römischen Be­griffen. Römische Begriffe haben gerade das Scharfumrissene, das Scharfkonturierte, das Kadaverhafte. Diejenigen Begriffe, welche ent­wickelt werden, um zum Beispiel den Menschen in seiner Wahrheit zu begreifen, wie ich ihn in seiner Normalaura, möchte ich sagen, Ihnen vor acht Tagen hier auf die Tafel gezeichnet, skizziert habe, die Be­griffe, die notwendig sind, um die wahre Wirklichkeit des Menschen wieder zu erfassen und damit die wahre Wirklichkeit der Welt einiger­maßen zu begreifen, diese Begriffe müssen flüssig sein, diese Be­griffe dürfen nicht scharf konturiert sein, denn die Wirklichkeit ist nichts Starres, sondern etwas Werdendes. Und wollen wir mit unse­ren Begriffen und Ideen die Wirklichkeit erfassen, so müssen wir mit unseren Begriffen dem Fluß, dem Werden der Wirklichkeit nach-schreiten.",
      "Wenn außer acht gelassen wird dieses Flüssigwerden der Begriffe, dann kommt das zustande, was heute zum Unheil der Menschheit an zahlreichen Orten beobachtet werden kann. Nehmen Sie eine Erschei­nung, die heute für etwas gründlichere, nicht schlafende Weltenbeob-achter sich geradezu aufdrängt. Es ist die folgende Erscheinung. Nicht wahr, wir haben in der Welt unter uns Gelehrte, Gelehrte auf den mannigfaltigsten Gebieten. Diese Gelehrten vertreten, bewahren, wie man sagt, die Wissenschaft, und die heutige Menschheit, die ja nicht autoritätsgläubig ist, glaubt aber trotz ihres aus der Welt geschafften Autoritätsglaubens aufs Wort alles dasjenige, was von den Gelehrten der verschiedenen Gebiete vertreten wird. Und die Gelehrten unter­einander glauben den andern immer dasjenige, was nicht gerade in ihrem Gebiete ist. In diese Verhältnisse sehen die Menschen heute",
      "nicht gern hinein, weil das ganze Zerfaserte und Chaotische unserer Kultur den Menschen auflallen müßte, wenn sie in diese Verhältnisse hineinsehen würden. Aber wir haben ja zum Beispiel das Folgende er­lebt.",
      "Nehmen wir an, so ein Gelehrter - wir könnten immer für die verschiedenen Gebiete einen herausheben - hat zu seinem speziellen Gebiete, nun, meinetwillen - ich will etwas Ausgefallenes nehmen -, die Ägyptologie. Da besteht dann sein Beruf darinnen, daß er über die Eigentümlichkeit des ägyptischen Volkes die übrigen Menschen, die sich nicht beschäftigen können mit dem, was man die Quellen nennt, unterrichtet, daß er auch über die Beziehungen des ägyptischen Volkes zu andern Völkern des Altertums die Menschen unterrichtet.",
      "Der Menschen Aufgabe ist es, das aufs Wort zu glauben, denn der Mann ist ja in der Ägyptologie eine Autorität. Nun ist aber in unserer Zeit ein Unheil gekommen: Eine große Anzahl von diesen Gelehrten, die solche Spezialgebiete vertreten, haben nicht geschwiegen, sondern über Themen gesprochen, die nicht zu ihrem Fachgebiet gehören.",
      "Es wäre ja besser gewesen, wenn sie geschwiegen hätten, aber sie haben nicht geschwiegen; sie haben zum Beispiel ihr Denken, ihre Gedan­kenformen, heute unter dem Eindruck dieser Ereignisse angewendet auf ihr eigenes Volk und auf seine Beziehungen zu den andern Völ­kern. Und da hat man nun genügend Gelegenheit zu sehen, was für Unsinn eigentlich die Leute reden.",
      "Nun müßte man Schlüsse ziehen, Schlüsse, die sehr real gedacht werden können. Gar mancher, der da gilt, sagen wir, auf dem Gebiete der Ägyptologie, und von dem man die Meinung hat, daß seine Begriffe mit Bezug auf die Eigentürrilich­keiten des ägyptischen Volkes und seines Verhältnisses zu andern Völkern unanfechtbar seien, der redet nun plötzlich in der Gegen­wart lauter Unsinn über sein eigenes Volk und über das Verhältnis seines eigenen Volkes zu den andern Völkern.",
      "Ja, glauben Sie, er wird nun über die Ägypter und über ihre Beziehungen zu andern Völkern gescheiter reden und geredet haben? Wenn Bheute über das Verhältnis seines Volkes zu der übrigen Welt spricht, oder wenn Houston Stewart Chamberl¹in fortwährend Unsinn redet über das Ver­hältnis der Menschen zu den andern Menschen, da könnten einige auch ohne Nachdenken irgendwie herauskriegen, daß die Leute Unsinn",
      "reden, völligen Unsinn reden! Aber nun hat der Chamberlain ge­schrieben «Die Grundlagen des 19. Jahrhunderts» und eine große Anzahl anderer Bücher, bei denen man nicht die Gelegenheit hat, die Geschichte zu prüfen. Er hat natürlich ganz genau denselben Unsinn geredet dazumal.",
      "Es ist schon einmal gegenwärtig die Zeit der Prüfung, und nament­lich die Zeit der Prüfung dafür, nun endlich einmal einzusehen, daß es nicht bloß darauf ankommt, Urteile abzugeben, die einen gewissen eingeschränkten Wert haben, indem sie richtig sind auf einem be­stimmten Gebiete - das ist fast jedes Urteil, das Falscheste ist auf einem bestimmten Gebiete richtig -, sondern daß es darauf ankommt, geradezu zu suchen jene Flüssigkeit der Urteile, die nur durch die Geisteswissenschaft gefunden werden kann, die in die Realität ein­dringt.",
      "Es ist ja merkwürdig, welche Kollisionen zwischen gesundem Den­ken und zeitgemäßem Denken gerade heute an die Oberfläche treten. Man hat in den letzten Tagen von einer religiösen Diskussion gehört, die stattgefunden hat in Petersburg - Petrograd, so hat man eine Zeit­lang gesagt, ich weiß nicht, ob man jetzt schon wieder Petersburg sagt -, also von einer religiösen Diskussion, die in dem ehemaligen St. Petersburg stattgefunden hat. Mitten drinnen im Bolschewismus hat man von einer religiösen Diskussion gehört. Da haben über die Religion und ihre Entwickelung gesprochen Sozialisten, Popen, selbst­verständlich auch allerlei Bourgeoisleute. Die haben natürlich das Ge­scheiteste nicht geredet. Nun könnte man aus der Diskussion, die da gepflogen worden ist, die natürlich in der Wolle gefärbt war von der Gegenwart, aber durchaus mit den starrsten alten Begriffen arbeitete, wie es scheint, doch manches lernen. Zum Beispiel hat da ein Pope etwas höchst Interessantes vorgebracht. Der Pope fühlt sich genötigt, zu seinen Lämmern so zu sprechen, wie er es bisher gewohnt war. Nun hat er natürlich bisher so geredet, daß alles dasjenige, was auf der Welt ist, der Zarismus und alles, alles selbstverständlich von Gott kommt. Was kann er heute machen, der gute Pope? Er muß natürlich das, was er gewohnt war, früher seinen Lämmern zu sagen - jetzt sind es keine Lämmer mehr -, heute wenigstens irgendwie beibehalten,",
      "denn er will ja nicht zu neueren Begriffen übergehen. Da sagt er denn: Die Welt ist von Gott, alles ist von Gott; da wir jetzt eine Sowjet­regierung haben, ist sie auch von Gott. Bolschewismus ist eben von Gott der Menschheit geschickt. Da alles von Gott ist, ist auch der Bolschewismus von Gott. - Was soll er anderes sagen? Ich bin ganz überzeugt davon, die Schlußfolgerung kann auch noch weiter aus­gedehnt werden. Warum sollte man nicht sehr schön plausibel machen können, daß der Teufel von Gott ist? Der Teufel ist einge­setzt von Gott, nach ganz derselben Schlußfolgerung! - Das ist es ja, daß man wirklich einmal tiefer hineinleuchtet in dasjenige, was not­wendig ist. Das findet natürlich auf allen Gebieten stärkste Gegner­schaft. Schlafen aber kann man nicht, wenn man sich vorgenommen hat, teilzunehmen an dieser Umarbeitung des Vorstellungsvermögens der Menschen.",
      "Begriffe, die der Materialismus herausgearbeitet hat und die gerade­zu als unanfechtbar gelten, sie gehören zu demjenigen, was gewisser­maßen am gründlichsten überwunden werden müßte. Nichts begegnet einem ja heute häufiger aus der sogenannten Autorität der Wissen­schaft heraus als dasjenige, was genannt wird das Gesetz von der Er­haltung der Energie und des Stoffes, Erhaltung von Kraft und Stoff. Das ist dasjenige, was ganz besonders der Menschheit ans Herz ge­wachsen ist. Die ganz und gar mechanistisch, physikalisch gewordene Weltanschauung will sich betäuben gegenüber dem Vorhandensein des Geistes. Da sie den Geist nicht anerkennen will, kann sie dem Geist auch nicht Dauer, nicht Ewigkeit zuschreiben; sie schreibt die Ewigkeit ihrem kleinen Götzen, dem Atom, oder überhaupt dem Stoff oder der Kraft zu. Aber, die Wahrheit ist, daß von alldem, was Sie sinnlich anschauen können, was Sie da stofflich und als Kräfte in der Welt umgibt, nach den Gesetzen des Weltenalis nichts, aber auch gar nichts über die Stufe des Venuszeitalters hinaus existieren wird. Wir wissen, daß auf die Evolution der Erde die Jupiterevolution folgt, und auf die Jupiterevolution die Venusevolution, dann die Vulkanevolu­tion. So wie sich der Mensch in verschiedenen Verkörperungen wiederfindet, so findet sich die Erde wieder als Jupiter nach der Ju­piterevolution als Venus, nach der Venusevolution als Vulkan. Dasjenige,",
      "was heute von irgendeinem physikalischen Experiment als Stoff und Stoffgefüge gefunden werden kann, es hat nicht Bestand über das Venusdasein hinaus. Es gibt keine Erhaltung des Stoffes und der Kraft - solchen Stoffes, solcher Kraft, von der die Physiker spre­chen können - über das Venusdasein hinaus. Das ganze Gesetz von der Erhaltung des Stoffes und der Kraft ist lediglich ein Aberglaube, ist dasjenige, wovon alle physikalischen Begriffe beherrscht werden. Aber etwas wird zugedeckt, indem man geradezu davon spricht, die Welt bestehe aus unzerstörbarem Stoff, der sich immer in andern Gruppierungen ergibt. Zugedeckt wird das, was als Antwort kommen muß, wenn man die Frage aufwirft: Ja, was bleibt denn dann, wenn alles das, was unsere Sinne in weiterem Umkreise umgibt, schon nicht mehr da sein wird, wenn die Venuszeit gekommen oder in ihrer Mitte angelangt sein wird? Was bleibt dann? Wo ist denn irgend etwas, was bleibt?",
      "Nun, richten Sie Ihre Augen hinaus in den weiten Umkreis, den Sie überschauen können. Schauen Sie sich alles, alles an, schauen Sie sich die Gesamtheit des mineralischen, des pflanzlichen, des tierischen, des menschlichen Reiches an; schauen Sie sich an alles dasjenige, was Sie sehen können als Sterne, Lichterscheinungen, alle Lufterscheinungen, alle Wassererscheinungen, sehen Sie hin, wo Sie hinsehen wollen, fas­sen Sie alles zusammen, was Sie irgendwie in Ihren äußeren Sinnes­wahrnehmungen zusammenfassen können und stellen Sie sich die Frage: Wo ist etwas, was von unserem jetzigen Dasein bleibt? - In keinem Tier, in keiner Pflanze, in keinem Mineral, in keiner Luft, in keinem Wasser, nirgends als nur im Menschen! In allem, was Sie heute sehen können, ist nichts enthalten, was regelrecht über das Venusdasein hinausgeht, als einzig und allein der Mensch selber. In nichts anderem können Sie etwas Bleibendes, etwas, was mit dem Begriffe der Ewigkeit angesprochen werden kann, suchen, in nichts anderem als in dem Menschen. Das heißt: Suchen wir die Keime für die wahre Weltenzukunft, wo müssen wir sie suchen? - Wir mussen sie im Menschen suchen! Wir können sie bei keinem andern Geschöpf, in keinem Naturreiche suchen. Aber durch die Naturreiche haben die alten Menschen vor dem Mysterium von Golgatha das kosmische All,",
      "geistig natürlich, gesehen. Wenn wir die Sonne nehmen: Sie haben einen glühenden Ball gesehen, aber sie haben durch den glühenden Ball den Helios und das Gute gesehen. Doch dieser glühende Sonnen­ball wird nicht länger vorhanden sein als das Venusdasein; dann ist er weg. Und alles dasjenige, wodurch man wie die Alten als durch einen Schleier die Konstituion irgendeines geistigen Daseins gesehen hat, es wird weg sein. Und von alledem, was jetzt da ist, bleibt für die Zukunft nur das, was in den Menschen keimhaft veranlagt ist.",
      "Was ist denn also eigentlich geschehen? Die Menschen haben vor dem Mysterium von Golgatha hinausgesehen in das weite Weltenall; sie haben gesehen Sterne über Sterne, sie haben gesehen die Sonne und den Mond, sie haben gesehen Luft und Wasser, die verschiedenen Reiche. Aber sie haben sie nicht so angeschaut wie der heutige Mensch, sondern sie haben hinter alldem das geistig-göttliche Dasein geschaut, und sie haben hinter alldem den Christus, der noch nicht zur Erde niedergestiegen war, geschaut. In diesen alten Zeiten hat man den Christus verbunden mit dem Kosmos, außerirdisch hat man ihn ge­sehen. In all dem, worinnen man den Christus gesehen hat, ist nichts, was über das Venusdasein hinaus dauert. Alles, wodurch sich in den Zeiten vor dem Mysterium von Golgatha dem Menschen das Geistige enthüllt hat und auch der Christus im Kosmos, hat nur einen Bestand bis zum Venusdasein. Die Menschen lebten vor dem Mysterium von Golgatha mit dem Himmel, aber dieser Himmel ist so sinnlich, daß er auch mit dem Venusdasein verschwindet. Was über das Venusdasein hinaus bleibt, das hat seine Keime nur im Menschen. Der Christus mußte aus dem Weltenall zu dem Menschen kommen, wenn er mit dem Menschen den Gang in die Ewigkeit antreten wollte. Weil das alles so ist, wie ich es Ihnen jetzt geschildert habe, deshalb stieg der Christus aus dem Kosmos herab, um fortan mit dem zu sein, was als Keim im Menschen in die Ewigkeit hinaus dauert.",
      "Das ist das große kosmische Ereignis, das man verstehen muß. Die Menschen vor dem Mysterium von Golgatha konnten den Gott, den Christus im Weltenall verehren. Die Menschen, die darauf kommen mußten - und es ist die Zeit seit dem Mysterium von Golgatha immer mehr und mehr darauf gekommen, daß nur im Menschen der Keim",
      "ist für die ewige Weltenzukunft -, diese Menschen mußten einen Christus haben nicht im Weltenall draußen, das zet£ällt, sondern ver­eint mit dem Menschen, mit der menschlichen Organisation, mit dem menschlichen Reiche. Wörtlich wahr ist es: Dasjenige, was da ist im weiten Umkreis der Sinne als Sterne, als Himmeiskörper, es wird vergehen. Aber das Wort, der Logos, der erschienen ist in dem Christus, und der sich vereinigt mit dem ewigen Wesenskern des Menschen, der wird bleiben. Und das ist eine wörtliche Wahrheit, wie die Dinge in den wirklichen okkulten, religiösen Urkunden wört­liche Wahrheiten sind.",
      "Das aber ist auch der Grund, warum wir gewissermaßen einen Dua­lismus in der Namengebung haben müssen - ich habe darauf schon hingedeutet -, in der Namengebung Christus Jesus. Den Christus, der dem außerirdischen Weltenall angehört, dieses geistige Wesen, das vor dem Mysterium von Golgatha nicht mit den Menschen der Erde ver­bunden war, muß man auf der einen Seite erkennen; das darf nicht vergessen werden, denn das ist heruntergestiegen und hat sich mit der Menschennatur, mit dem Jesus verbunden. In dem Dualismus Chri­stus Jesus liegt dasjenige, was notwendig ist, zu verstehen. In dem Christus muß man das Kosmisch-Geistige sehen; in dem Jesus muß man dasjenige sehen, durch welches dieses Kosmisch-Geistige in die historische Entwickelung eingetreten ist und sich so mit der Mensch­heit verbunden hat, daß es mit dem Menschenkeim nun weiter in die Ewigkeiten leben kann.",
      "Dieses mit den alten Mysterien zusammenhängende Christusge­heimnis zu verhüllen, zu entstellen, das war gewissermaßen die Auf­gabe der Kirche in den verflossenen Jahrhunderten. Und versuchen Sie einmal, den Werdegang der Menschheit in diesen verflossenen Jahrhunderten wirklich zu studieren, versuchen Sie sich klarzumachen, wie es denjenigen einzelnen Menschen gegangen ist, welche den Christus Jesus wirklich suchen wollten, die wirklich den Weg finden wollten zu dem Christus Jesus: es war immer ein Märtyrerweg. Er mußte immer gesucht werden, der Christus Jesus, gegen die Konven­tionen, wie er ja auch heute selbstverständlich gegen dasjenige, was von den Konventionen geblieben ist, gesucht werden muß. Aber",
      "man kann dem Christus-Geheimnis nicht nahekommen, wenn man es nicht verbindet mit dem Naturgeheimnis.",
      "Sie sehen, die Notwendigkeit, die wir vor unsere Seele hingestellt haben, von dem Herunterkommen des Christus aus kosmischen Höhen zu dem Menschenkeim, das Geheimnis von dem Jesus-Werden des Christus, man kann es nur verstehen, wenn eine Einheit wird Naturbetrachtung, Weltbetrachtung, Kosmologie und die Wissen­schaft von dem Werden des Menschen und des Göttlichen in der Menschheit. Das möchte man gerade von einer gewissen Seite her ver­meiden, daß Naturwissenschaft zu gleicher Zeit Geisteswissenschaft und Geisteswissenschaft zu gleicher Zeit Naturwissenschaft werde. Das ist ja das Bestreben der meisten Theologen, und auf der andern Seite wiederum das Bestreben der meisten Naturgelehrten der Ge­genwart, daß eine Schranke aufgerichtet werde zwischen der Natur­wissenschaft auf der einen Seite und der Geisteswissenschaft auf der andern Seite. Nur ja soll nicht über den Christus Jesus etwas gesagt werden, was zu gleicher Zeit zusammenhängt mit der Erdenevolu­tion, und nur ja soll nicht über die Erdenevolution, das heißt über ihre einzelnen Teile etwas gesagt werden, was zusammenhängt mit dem großen geistigen Mysterium.",
      "Indem man diese Dinge berührt, berührt man in der Tat Wichtig­stes, Allerwichtigstes im Menschenleben der Gegenwart. Denn jenes konfuse Geschwätz von allerlei Geistigem, auf das auch unsere Freunde einen so oftmals aufmerksam machen, und zum Ekel einen aufmerksam machen, dieses konfuse Geschwätz vom Geiste nützt gar nichts. Ich meine, es kommt alle Augenblicke einer und sagt: Nun sehen Sie einmal, der hat wiederum ganz theosophisch oder anthropo­sophisch geredet, er hat das und das gesagt! - Dieses bequeme Suchen nach Stützen in der gegenwärtigen Konfusion, das ist nicht dasjenige, was wir anstreben sollen, sondern wir sollen schon auf dem Funda­ment feststehen, das uns die Geisteswissenschaft sein wird. Und die Zeit ist zu ernst, um weitere Kompromisse, besonders auf diesem Ge­biete zu pflegen.",
      "Die Brücke zu schaffen zwischen dem Naturwissen, überhaupt zwischen dem Wissen des Wahrgenommenen und dem Wissen desjenigen,",
      "zu dem die Sünde, zu dem die Erlösung, kurz, zu dem die religiösen Wahrheiten gehören, die Brücke zu schaffen zwischen die­sen zwei Gebieten, das kann nur geschehen, wenn man den Mut haben wird, in das Geistige wirklich real einzudringen. Aber auch über die Lebenswahrheiten wird man nichts Vernünftiges wissen können, wenn man nicht den Mut hat, in das Geistige real, wirklich einzudringen. Zum Eindringen in das geistig Reale gehört vor allen Dingen diese Möglichkeit: wiederum etwas zurückzublicken zu dem dreifachen Sonnenmysterium der alten Zeit, aber in dem neuen Sinne, wie es der gegenwärtigen Menschheit angemessen ist. Geradeso wie die Sonne eine Dreiheit ist, so ist ja der Mensch auch eine Dreiheit. Aber es handelt sich darum, daß wir diesen dreifachen Menschen wirklich studieren. Das ist Wichtigstes für die Gegenwart: den drei­fachen Menschen zu studieren. Ich möchte Ihnen heute einmal vor­bereitend - morgen und übermorgen werden wir diese wichtige Sache zu Ende führen - schematisch etwas angeben, was Sie führen kann auf dem Wege, der eigentlich gesucht werden müßte, um den drei­fachen Menschen zu begreifen.",
      "Denken Sie sich einmal das Folgende - also das, was ich jetzt skiz-ziere, soll ein Schema sein -, denken Sie sich, Sie hätten ein Gebilde, das ganz und gar nur Bild, nur Abbild sei, das im Grunde gar keine Bedeutung in sich selber hat, also Abbild ist. Das will ich so skizzieren:",
      "ich zeichne einfach einen Kreis (siehe Zeichnung Seite 71, blau), eine Kreisfläche. Das ist ein Gebilde, das Abbild ist von etwas anderem, aber dadurch, daß es Abbild ist, hat es das andere, wovon es Abbild ist, vollständig aufgezehrt. Es ist ja sonderbar, wenn ich folgendes sage, aber denken Sie sich einmal: In unserer Kuppel, in der kleinen Kuppel arbeiten vier Damen; nehmen wir einmal an, diese vier Da­men würden, auf jeder Seite zwei, malen, sich selber porträtieren, aber dieses Porträtieren hätte eine besondere Folge. Also denken Sie sich, diese vier Damen, die porträtieren sich in der kleinen Kuppel, malen sich selber da ab, aber dieses Sich selber Porträtieren, das hätte eine ganz bestimmte Folge: sie verschwänden nämiich dadurch, sie gingen über in ihr Abbild, sie hörten auf zu sein. Wenn sie fertig sind, sind sie nicht mehr da. Dadurch, daß die Abbilder entstanden sind,",
      "sind sie selbst nicht mehr da. - Solch ein Gebilde stellen Sie sich unter dem, was ich hier skizzenhaft aufgezeichnet habe, einmal vor: ein Gebilde, das dadurch entstanden ist, daß es gemacht worden ist von etwas, wovon es Abbild ist; aber dadurch, daß das Abbild da ist, ist das andere aufgezehrt.",
      "Nun ist aber dieses Aufgezehrte nicht allein in der Welt. Stellen Sie sich nämlich vor, es wäre die Geschichte noch nicht aus mit diesen vier Damen. Gut, diese vier Damen wären verschwunden, sie hätten sich da aufgemalt und wären verschwunden; aber die Bilder sind da. Sie sind nicht allein da im Weltenall, das Weltenall ist mit seinen Kräften außerdem noch da. Die Damen sind verschwunden, sind von den Bildern gewissermaßen aufgesogen worden; aber dadurch, daß die Bilder da sind, zieht sich aus dem Weltenall wiederum Substan­tielles zusammen und bildet die Damen neu, allerdings jetzt als Kinder:",
      "sie entstehen langsam wieder, enstehen da daneben. So entsteht neben diesem Gebilde wiederum sein Urbild (siehe Zeichnung, gelb). Ich",
      "# Bild s. 71",
      "müßte es eigentlich ein Stückchen hinein zeichnen, ich zeichne es nun daneben auf: das ist das Urbild. Das ist das Urbild, aber es ist ein sehr loser Zusammenhang zwischen diesem Abbild und dem Urbild, ein sehr loser Zusammenhang. Beide haben fast gar nichts miteinander zu tun. Dieses Abbild ist richtig verhärtet und hat fast gar nichts mit seinem Urbilde zu tun.",
      "Dann denken Sie sich ein zweites Gebilde. Ich will das zweite Ge­bilde so skizzieren, daß ich es nun auch als Abbild mache (siehe Zeichnung Seite 72, violett); nur ist das erste drinnen in dem zweiten. Das erste ist etwas für sich, aber es ist auch drinnen in dem zweiten. Also ich zeichne da kühn über das erste das zweite drüber. Das ist wiederum solch ein Abbild, und wiederum so ähnlich ein Abbild von einem andern, das ich auch nun da drauf zeichnen will (siehe Zeichnung,",
      "# Bild s. 72",
      "rot); das muss ich aber nun schon inniger mit dem verbin­den. Da ist die Sache also so, daß ich nicht den Vergleich wählen könnte, den ich früher mit den vier Damen gewählt habe, sondern wenn ich bezüglich dieses Bildes und Abbildes jetzt einen Vergleich wählen würde, müßte ich so sagen: Es sind also die vier Damen da, sie malen in der kleinen Kuppel, und während sie malen, geht schon auch etwas von ihnen selber auf, wird aufgesogen. Aber nur zur Hälfte werden sie aufgesogen; zuletzt sind sie so, daß sie - nun, ich will also sagen, um nicht einen unästhetischen Vergleich hervorzu­rufen: Es wird von der einen die linke Körperhäffte aufgesogen, die rechte ragt noch heraus von dem Bilde; von der andern die rechte Körperhälfte aufgesogen, die linke ragt noch heraus. Also sie sind teilweise aufgesogen; teilweise ragen sie noch heraus. Das ist das zweite.",
      "Dann stellen Sie sich ein drittes vor, das also wiederum das erste mitumfaßt und das zweite auch mitumfaßt (siehe Zeichnung Seite 73, grün). Das aber ist zum großen Teil mit seinem Abbilde verbunden, das ist noch nicht getrennt von seinem Abbilde. Da müßte ich also, wenn ich den Vergleich festhalten wollte, sagen: Die Damen malen, aber sie bleiben auch als Damen vorhanden, und das Ganze, was ich vor mir habe, sind die Damen und ihre Abbilder. Das ist vorhanden (siehe Zeichnung, orange), das ist zum größten Teile auch im Urbilde vorhanden.",
      "So haben Sie also hier (Zeichnung Seite 71) etwas schematisch ge­zeichnet: zuerst oben ein Abbild, verhärtet, kristallisiert, es hat möglichst",
      "# Bild s. 73",
      "wenig mit seinem Urbilde zu tun; das Urbild ist daneben, neu entstehend. Das ist nämlich Ihr Kopf; der ist der materiellste, ver­härtetste Teil der Menschennatur. Sein Urbild hat geradezu nichts mit ihm zu tun, entsteht neu; und wenn Sie achtundzwanzig Jahre alt geworden sind, ist Ihr Kopf so, daß er aus sich selber gar nicht ein­mal mehr etwas hergibt, ausgewachsen ist. Der größte Materialist in der Menschennatur ist das Haupt. Ein zweites Gebilde ist Brust und Atmung und alles, was dazugehört. Das ist ungefähr so, daß ich das zweite als Schema gebrauchen könnte (Zeichnung Seite 72). Das ist schon mehr verbunden, da hängen Geist und Materie schon mehr zu­sammen, das ist schon durchgeistigter. Alles das, was Lunge und Atmungsprozeß ist, ist schon für die Erde vergeistigter. Und was übrigbleibt, Gliedmaßen, im Zusammenhange damit alles das, was die Sexualität umfaßt, da ist Geistiges mit Physischem eins, da sind sie noch zusammen. Das gehört zum dritten Schema (Zeichnung oben).",
      "Das ist der dreifache Mensch. Ich habe es Ihnen heute nur schema­tisch auf die Tafel zeichnen können. Dieses zu gleicher Zeit wunder­bare und furchtbare, dieses großartige und tiefeindringende Myste­rium vom dreifachen Menschen hängt wiederum mit dem dreifachen Sonnenmysterium zusammen. Das aber hängt wiederum zusammen",
      "mit all den Wahrheiten, die wir brauchen wie das Brot des Lebens für alles dasjenige, was sich setzen muß an die Stelle dessen, was in das Chaos, was in die Sackgasse hineingekommen ist und zu den gegen­wärtigen Menschheitskatastrophen geführt hat. Davon werden wir morgen weiter sprechen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Wenn man eine Zeit, in der man selbst lebt, verstehen will, so muß man sie aus größeren Weltenzusammenhängen heraus verstehen.",
        "Das ist gerade das Kleinliche der gegenwärtigen Zeit, daß man nicht will die Impulse, die Kräfte, die wirksam sind in der Gegenwart, aus größe-rem Zusammenhang heraus sich klarmachen.",
        "Und insbesondere wird es immer wieder und wiederum notwendig sein, um das eine oder das andere gegenwärtig Wirksame zu verstehen, zurückzugreifen zu den Verhältnissen, durch welche die Menschheitsentwickelung gegangen ist zur Zeit des Mysteriums von Golgatha.",
        "Dieses Mysterium von Golgatha, wir haben es ja von den verschiedensten Gesichtspunkten aus dargestellt und haben gesehen, wie tief, wie bedeutsam es eingreift in den ganzen Evolutionsgang, die ganze Entwickelung der Mensch­heit.",
        "Wir wissen, daß die Menschen vor dem Mysterium von Golgatha anders die Welt empfanden, anders anschauten als nach dem Myste­rium von Golgatha.",
        "Natürlich geht das nicht so auf einmal aus dem einen Zustand in den andern Zustand über.",
        "Aber der rückschauenden Betrachtung ergibt sich schon dasjenige, was wir von den verschie­densten Gesichtspunkten aus dargelegt haben.",
        "Insbesondere möchte ich heute, um eine gewisse Grundlage für die nächsten Betrachtungen zu finden, auf eines hinweisen."
      ],
      [
        "Wenn wir die Stimmung, die Verfassung der Menschenseelen vor dem Mysterium von Golgatha betrachten, so können wir im allge­meinen sagen, daß innerhalb der Kulturmenschheit, also de4enigen Menschheit, aus der die heutige Kulturmenschheit hervorgegangen ist, vor dem Mysteruim von Golgatha eine gewisse Fähigkeit in den Seelen vorhanden war, in die Geheimnisse der kosmischen, geistigen Welt hineinzuschauen.",
        "Es war für die Menschen vor dem Mysterium von Golgatha gewissermaßen selbstverständlich, nicht so zum Ster­nenhimmel hinaufzuschauen, wie heute der Mensch zum Sternen-himmel hinaufschaut.",
        "Wir wissen ja, heute schaut der Mensch zum Sternenhimmel hinauf, indem er sich sagt: Mit unserer Erde sind"
      ],
      [
        "einige andere Planeten verbunden, die mit ihr zusammen um die Sonne kreisen; dann sind unzählige andere Fixsterne da, die wiederum ihre Planeten haben. - Und wenn dann der Mensch darauf achtet, was er eigentlich, indem er sich so etwas überlegt, für einen Gedanken hat, so muß er sich doch sagen, er hat den Gedanken einer großen Welt-maschinerie.",
        "Daß da noch anderes waltet und wirkt als die Kräfte dieser großen Weltmaschinerie, das macht sich der Mensch der Ge­genwart nur sehr, sehr wenig klar."
      ],
      [
        "Das war mehr oder weniger für den Menschen vor dem Mysterium von Golgatha selbstverständlich.",
        "Insbesondere war für ihn selbstverständlich, die Sonne zum Beispiel nicht bloß als dasjenige anzuschauen, als was sie der heutige Pyhsiker anschaut, roh gesprochen, eine Art glühender Kugel im Weltenraume draußen, sondern der Mensch vor dem Mysterium von Golgatha wußte ganz genau: Diese Sonne, von der die Physik spricht, diese Sonne ist nur ein Element in der ganzen Sonne."
      ],
      [
        "Dieser Sonne liegt zu­grunde ein Seelisches und ein Geistiges.",
        "Und das Geistige, das dieser Sonne zugrunde liegt, sprach ja noch der griechische Weise als das allgemeine Weltgute an, als das Gute der Welt, als das einheitliche, die Welt durchwallende Gute."
      ],
      [
        "Das war ihm der Geist der Sonne.",
        "Ihm wäre es, diesem griechischen Weisen, als stärkster Aberglaube vorgekom­men, so zu denken, wie der heutige Physiker denkt, daß da draußen im Weltenraume einfach eine glühende Kugel schwebe; sondern ihm war diese glühende, schwebende Kugel die Offenbarung des einheit­lich Guten, das in der Welt zentral wirksam ist."
      ],
      [
        "Und mit diesem zen­tralen Guten, das geistiger Art ist, ist wiederum verbunden ein Seeli-sches: der Helios, wie es die Griechen nannten.",
        "Und erst das dritte, der physische Ausdruck des Guten und des Helios, war dann die phy­sische Sonne."
      ],
      [
        "Es sah also der Mensch damals an Stelle der Sonne ein Dreifaches.",
        "Und mit diesem Dreifachen, das in der Sonne in alten Zeiten gesehen worden ist, brachten diejenigen Menschen, welche in der Zeit des Mysteriums von Golgatha dachten - ausgerüstet mit dem Wissen dieses Mysteriums von Golgatha, ausgerüstet mit dem Wissen der alten Mysterien -, mit diesem dreifachen Sonnenmysterium brach­ten diese Weisen das Chnstus-Mysterium zusammen, das Mysterium von Golgatha selber."
      ],
      [
        "Mit der Sonnenverehrung war verbunden für"
      ],
      [
        "diejenigen, die etwas wußten, die Christus-Verehrung.",
        "Mit der Sonnen­weisheit war wiederum für diejenigen, die etwas wußten, verbunden die Christus-Weisheit."
      ],
      [
        "Um aber das, was ich jetzt auseinandergesetzt habe, naturgemäß zu fühlen, als etwas Selbstverständliches zu empfinden, dazu war eben die Konstitution der Seele notwendig, die damals da war.",
        "Und diese Kon­stitution der Seele verschwand eben."
      ],
      [
        "Sie verschwand schon seit dem 8. vorchristlichen Jahrhundert, mit dem Jahre 747 - dies ist die wirk­kiche Gründungszahl von Rom - vor dem Mysterium von Golgatha.",
        "Mit der Gründung Roms schwindet eigentlich die alte Möglichkeit, in dem Kosmos draußen das Geistige zu sehen."
      ],
      [
        "Mit dem Eintritt Roms in die Geschichte tritt das in die Menschheitsevolution ein, was man das prosaische Element nennen kann.",
        "Die Griechen zum Bei­spiel bewahrten in ihrer ganzen Weltanschauung noch die Möglich­keit, hinter der Sonne eben die zwei andern Sonnen, die seelische und die geistige Sonne zu sehen."
      ],
      [
        "Und nur dadurch, daß nun nicht rein in griechische Weisheit und in griechisches Empfinden das Mysterium von Golgatha getaucht worden ist, sondern in römische Weisheit und in römisches Empfinden, dadurch ist es gekommen, daß man ge­brochen hat mit dem Wissen von dem Zusammenhang des Christus mit der geistigen Sonne.",
        "Damit haben sich ja namentlich die christ­lichen Kirchenväter und die christlichen Kirchenlehrer zu befassen gehabt, dieses Mysterium von der Sonne zu verhüllen, dieses Myste­rium von der Sonne für die Menschheit vergessen zu machen, es nicht herauskommen zu lassen."
      ],
      [
        "Es sollte gewissermaßen ein Schleier gebreitet werden durch die fortgehende Entwickelung des Christen­tums, wie man das nennt, über die tiefe, die bedeutsame, die um­fassende Weisheit von dem Zusammenhange des Christus mit dem Sonnenmysterium."
      ],
      [
        "Wenn man definieren sollte die Aufgabe der Kirche, jener Kirche, die entstanden ist dadurch, daß das Christentum in das Römertum eingesenkt worden ist, dann müßte man dies so tun, daß man sagte:"
      ],
      [
        "Die römisch gefärbte christliche Kirche hatte sich namentlich zur Aufgabe zu machen, das Christus-Mysterium möglichst zu ver­hüllen, es möglichst wenig bekanntwerden zu lassen. - Die Einrichtung,"
      ],
      [
        "welche die Kirche durch den Romanismus erfahren hat, die ist insbesondere geeignet gewesen, die Menschen so wenig wie moglich von dem Christus-Geheimnis wissen zu lassen.",
        "Die Kirche war da­durch eine Institution zur Geheimhaltung des Christus-Mysteriums geworden, eine Institution geworden, möglichst wenig in die Welt kommen zu lassen von dem Christus-Mysterium.",
        "Dies ist etwas, was immer mehr und mehr in der jetzigen Zeit der Menschheit klarwerden muß, weil beginnen muß diejenige Zeit, welche in der Lage ist, wie­derum mit andern Begriffen zu arbeiten als mit den römischen Be­griffen.",
        "Römische Begriffe haben gerade das Scharfumrissene, das Scharfkonturierte, das Kadaverhafte.",
        "Diejenigen Begriffe, welche ent­wickelt werden, um zum Beispiel den Menschen in seiner Wahrheit zu begreifen, wie ich ihn in seiner Normalaura, möchte ich sagen, Ihnen vor acht Tagen hier auf die Tafel gezeichnet, skizziert habe, die Be­griffe, die notwendig sind, um die wahre Wirklichkeit des Menschen wieder zu erfassen und damit die wahre Wirklichkeit der Welt einiger­maßen zu begreifen, diese Begriffe müssen flüssig sein, diese Be­griffe dürfen nicht scharf konturiert sein, denn die Wirklichkeit ist nichts Starres, sondern etwas Werdendes.",
        "Und wollen wir mit unse­ren Begriffen und Ideen die Wirklichkeit erfassen, so müssen wir mit unseren Begriffen dem Fluß, dem Werden der Wirklichkeit nach-schreiten."
      ],
      [
        "Wenn außer acht gelassen wird dieses Flüssigwerden der Begriffe, dann kommt das zustande, was heute zum Unheil der Menschheit an zahlreichen Orten beobachtet werden kann.",
        "Nehmen Sie eine Erschei­nung, die heute für etwas gründlichere, nicht schlafende Weltenbeob-achter sich geradezu aufdrängt.",
        "Es ist die folgende Erscheinung.",
        "Nicht wahr, wir haben in der Welt unter uns Gelehrte, Gelehrte auf den mannigfaltigsten Gebieten.",
        "Diese Gelehrten vertreten, bewahren, wie man sagt, die Wissenschaft, und die heutige Menschheit, die ja nicht autoritätsgläubig ist, glaubt aber trotz ihres aus der Welt geschafften Autoritätsglaubens aufs Wort alles dasjenige, was von den Gelehrten der verschiedenen Gebiete vertreten wird.",
        "Und die Gelehrten unter­einander glauben den andern immer dasjenige, was nicht gerade in ihrem Gebiete ist.",
        "In diese Verhältnisse sehen die Menschen heute"
      ],
      [
        "nicht gern hinein, weil das ganze Zerfaserte und Chaotische unserer Kultur den Menschen auflallen müßte, wenn sie in diese Verhältnisse hineinsehen würden.",
        "Aber wir haben ja zum Beispiel das Folgende er­lebt."
      ],
      [
        "Nehmen wir an, so ein Gelehrter - wir könnten immer für die verschiedenen Gebiete einen herausheben - hat zu seinem speziellen Gebiete, nun, meinetwillen - ich will etwas Ausgefallenes nehmen -, die Ägyptologie.",
        "Da besteht dann sein Beruf darinnen, daß er über die Eigentümlichkeit des ägyptischen Volkes die übrigen Menschen, die sich nicht beschäftigen können mit dem, was man die Quellen nennt, unterrichtet, daß er auch über die Beziehungen des ägyptischen Volkes zu andern Völkern des Altertums die Menschen unterrichtet."
      ],
      [
        "Der Menschen Aufgabe ist es, das aufs Wort zu glauben, denn der Mann ist ja in der Ägyptologie eine Autorität.",
        "Nun ist aber in unserer Zeit ein Unheil gekommen: Eine große Anzahl von diesen Gelehrten, die solche Spezialgebiete vertreten, haben nicht geschwiegen, sondern über Themen gesprochen, die nicht zu ihrem Fachgebiet gehören."
      ],
      [
        "Es wäre ja besser gewesen, wenn sie geschwiegen hätten, aber sie haben nicht geschwiegen; sie haben zum Beispiel ihr Denken, ihre Gedan­kenformen, heute unter dem Eindruck dieser Ereignisse angewendet auf ihr eigenes Volk und auf seine Beziehungen zu den andern Völ­kern.",
        "Und da hat man nun genügend Gelegenheit zu sehen, was für Unsinn eigentlich die Leute reden."
      ],
      [
        "Nun müßte man Schlüsse ziehen, Schlüsse, die sehr real gedacht werden können.",
        "Gar mancher, der da gilt, sagen wir, auf dem Gebiete der Ägyptologie, und von dem man die Meinung hat, daß seine Begriffe mit Bezug auf die Eigentürrilich­keiten des ägyptischen Volkes und seines Verhältnisses zu andern Völkern unanfechtbar seien, der redet nun plötzlich in der Gegen­wart lauter Unsinn über sein eigenes Volk und über das Verhältnis seines eigenen Volkes zu den andern Völkern."
      ],
      [
        "Ja, glauben Sie, er wird nun über die Ägypter und über ihre Beziehungen zu andern Völkern gescheiter reden und geredet haben?",
        "Wenn Bheute über das Verhältnis seines Volkes zu der übrigen Welt spricht, oder wenn Houston Stewart Chamberl¹in fortwährend Unsinn redet über das Ver­hältnis der Menschen zu den andern Menschen, da könnten einige auch ohne Nachdenken irgendwie herauskriegen, daß die Leute Unsinn"
      ],
      [
        "reden, völligen Unsinn reden!",
        "Aber nun hat der Chamberlain ge­schrieben «Die Grundlagen des 19.",
        "Jahrhunderts» und eine große Anzahl anderer Bücher, bei denen man nicht die Gelegenheit hat, die Geschichte zu prüfen.",
        "Er hat natürlich ganz genau denselben Unsinn geredet dazumal."
      ],
      [
        "Es ist schon einmal gegenwärtig die Zeit der Prüfung, und nament­lich die Zeit der Prüfung dafür, nun endlich einmal einzusehen, daß es nicht bloß darauf ankommt, Urteile abzugeben, die einen gewissen eingeschränkten Wert haben, indem sie richtig sind auf einem be­stimmten Gebiete - das ist fast jedes Urteil, das Falscheste ist auf einem bestimmten Gebiete richtig -, sondern daß es darauf ankommt, geradezu zu suchen jene Flüssigkeit der Urteile, die nur durch die Geisteswissenschaft gefunden werden kann, die in die Realität ein­dringt."
      ],
      [
        "Es ist ja merkwürdig, welche Kollisionen zwischen gesundem Den­ken und zeitgemäßem Denken gerade heute an die Oberfläche treten.",
        "Man hat in den letzten Tagen von einer religiösen Diskussion gehört, die stattgefunden hat in Petersburg - Petrograd, so hat man eine Zeit­lang gesagt, ich weiß nicht, ob man jetzt schon wieder Petersburg sagt -, also von einer religiösen Diskussion, die in dem ehemaligen St.",
        "Petersburg stattgefunden hat.",
        "Mitten drinnen im Bolschewismus hat man von einer religiösen Diskussion gehört.",
        "Da haben über die Religion und ihre Entwickelung gesprochen Sozialisten, Popen, selbst­verständlich auch allerlei Bourgeoisleute.",
        "Die haben natürlich das Ge­scheiteste nicht geredet.",
        "Nun könnte man aus der Diskussion, die da gepflogen worden ist, die natürlich in der Wolle gefärbt war von der Gegenwart, aber durchaus mit den starrsten alten Begriffen arbeitete, wie es scheint, doch manches lernen.",
        "Zum Beispiel hat da ein Pope etwas höchst Interessantes vorgebracht.",
        "Der Pope fühlt sich genötigt, zu seinen Lämmern so zu sprechen, wie er es bisher gewohnt war.",
        "Nun hat er natürlich bisher so geredet, daß alles dasjenige, was auf der Welt ist, der Zarismus und alles, alles selbstverständlich von Gott kommt.",
        "Was kann er heute machen, der gute Pope?",
        "Er muß natürlich das, was er gewohnt war, früher seinen Lämmern zu sagen - jetzt sind es keine Lämmer mehr -, heute wenigstens irgendwie beibehalten,"
      ],
      [
        "denn er will ja nicht zu neueren Begriffen übergehen.",
        "Da sagt er denn: Die Welt ist von Gott, alles ist von Gott; da wir jetzt eine Sowjet­regierung haben, ist sie auch von Gott.",
        "Bolschewismus ist eben von Gott der Menschheit geschickt.",
        "Da alles von Gott ist, ist auch der Bolschewismus von Gott. - Was soll er anderes sagen?",
        "Ich bin ganz überzeugt davon, die Schlußfolgerung kann auch noch weiter aus­gedehnt werden.",
        "Warum sollte man nicht sehr schön plausibel machen können, daß der Teufel von Gott ist?",
        "Der Teufel ist einge­setzt von Gott, nach ganz derselben Schlußfolgerung! - Das ist es ja, daß man wirklich einmal tiefer hineinleuchtet in dasjenige, was not­wendig ist.",
        "Das findet natürlich auf allen Gebieten stärkste Gegner­schaft.",
        "Schlafen aber kann man nicht, wenn man sich vorgenommen hat, teilzunehmen an dieser Umarbeitung des Vorstellungsvermögens der Menschen."
      ],
      [
        "Begriffe, die der Materialismus herausgearbeitet hat und die gerade­zu als unanfechtbar gelten, sie gehören zu demjenigen, was gewisser­maßen am gründlichsten überwunden werden müßte.",
        "Nichts begegnet einem ja heute häufiger aus der sogenannten Autorität der Wissen­schaft heraus als dasjenige, was genannt wird das Gesetz von der Er­haltung der Energie und des Stoffes, Erhaltung von Kraft und Stoff.",
        "Das ist dasjenige, was ganz besonders der Menschheit ans Herz ge­wachsen ist.",
        "Die ganz und gar mechanistisch, physikalisch gewordene Weltanschauung will sich betäuben gegenüber dem Vorhandensein des Geistes.",
        "Da sie den Geist nicht anerkennen will, kann sie dem Geist auch nicht Dauer, nicht Ewigkeit zuschreiben; sie schreibt die Ewigkeit ihrem kleinen Götzen, dem Atom, oder überhaupt dem Stoff oder der Kraft zu.",
        "Aber, die Wahrheit ist, daß von alldem, was Sie sinnlich anschauen können, was Sie da stofflich und als Kräfte in der Welt umgibt, nach den Gesetzen des Weltenalis nichts, aber auch gar nichts über die Stufe des Venuszeitalters hinaus existieren wird.",
        "Wir wissen, daß auf die Evolution der Erde die Jupiterevolution folgt, und auf die Jupiterevolution die Venusevolution, dann die Vulkanevolu­tion.",
        "So wie sich der Mensch in verschiedenen Verkörperungen wiederfindet, so findet sich die Erde wieder als Jupiter nach der Ju­piterevolution als Venus, nach der Venusevolution als Vulkan.",
        "Dasjenige,"
      ],
      [
        "was heute von irgendeinem physikalischen Experiment als Stoff und Stoffgefüge gefunden werden kann, es hat nicht Bestand über das Venusdasein hinaus.",
        "Es gibt keine Erhaltung des Stoffes und der Kraft - solchen Stoffes, solcher Kraft, von der die Physiker spre­chen können - über das Venusdasein hinaus.",
        "Das ganze Gesetz von der Erhaltung des Stoffes und der Kraft ist lediglich ein Aberglaube, ist dasjenige, wovon alle physikalischen Begriffe beherrscht werden.",
        "Aber etwas wird zugedeckt, indem man geradezu davon spricht, die Welt bestehe aus unzerstörbarem Stoff, der sich immer in andern Gruppierungen ergibt.",
        "Zugedeckt wird das, was als Antwort kommen muß, wenn man die Frage aufwirft: Ja, was bleibt denn dann, wenn alles das, was unsere Sinne in weiterem Umkreise umgibt, schon nicht mehr da sein wird, wenn die Venuszeit gekommen oder in ihrer Mitte angelangt sein wird?",
        "Was bleibt dann?",
        "Wo ist denn irgend etwas, was bleibt?"
      ],
      [
        "Nun, richten Sie Ihre Augen hinaus in den weiten Umkreis, den Sie überschauen können.",
        "Schauen Sie sich alles, alles an, schauen Sie sich die Gesamtheit des mineralischen, des pflanzlichen, des tierischen, des menschlichen Reiches an; schauen Sie sich an alles dasjenige, was Sie sehen können als Sterne, Lichterscheinungen, alle Lufterscheinungen, alle Wassererscheinungen, sehen Sie hin, wo Sie hinsehen wollen, fas­sen Sie alles zusammen, was Sie irgendwie in Ihren äußeren Sinnes­wahrnehmungen zusammenfassen können und stellen Sie sich die Frage: Wo ist etwas, was von unserem jetzigen Dasein bleibt? - In keinem Tier, in keiner Pflanze, in keinem Mineral, in keiner Luft, in keinem Wasser, nirgends als nur im Menschen!",
        "In allem, was Sie heute sehen können, ist nichts enthalten, was regelrecht über das Venusdasein hinausgeht, als einzig und allein der Mensch selber.",
        "In nichts anderem können Sie etwas Bleibendes, etwas, was mit dem Begriffe der Ewigkeit angesprochen werden kann, suchen, in nichts anderem als in dem Menschen.",
        "Das heißt: Suchen wir die Keime für die wahre Weltenzukunft, wo müssen wir sie suchen? - Wir mussen sie im Menschen suchen!",
        "Wir können sie bei keinem andern Geschöpf, in keinem Naturreiche suchen.",
        "Aber durch die Naturreiche haben die alten Menschen vor dem Mysterium von Golgatha das kosmische All,"
      ],
      [
        "geistig natürlich, gesehen.",
        "Wenn wir die Sonne nehmen: Sie haben einen glühenden Ball gesehen, aber sie haben durch den glühenden Ball den Helios und das Gute gesehen.",
        "Doch dieser glühende Sonnen­ball wird nicht länger vorhanden sein als das Venusdasein; dann ist er weg.",
        "Und alles dasjenige, wodurch man wie die Alten als durch einen Schleier die Konstituion irgendeines geistigen Daseins gesehen hat, es wird weg sein.",
        "Und von alledem, was jetzt da ist, bleibt für die Zukunft nur das, was in den Menschen keimhaft veranlagt ist."
      ],
      [
        "Was ist denn also eigentlich geschehen?",
        "Die Menschen haben vor dem Mysterium von Golgatha hinausgesehen in das weite Weltenall; sie haben gesehen Sterne über Sterne, sie haben gesehen die Sonne und den Mond, sie haben gesehen Luft und Wasser, die verschiedenen Reiche.",
        "Aber sie haben sie nicht so angeschaut wie der heutige Mensch, sondern sie haben hinter alldem das geistig-göttliche Dasein geschaut, und sie haben hinter alldem den Christus, der noch nicht zur Erde niedergestiegen war, geschaut.",
        "In diesen alten Zeiten hat man den Christus verbunden mit dem Kosmos, außerirdisch hat man ihn ge­sehen.",
        "In all dem, worinnen man den Christus gesehen hat, ist nichts, was über das Venusdasein hinaus dauert.",
        "Alles, wodurch sich in den Zeiten vor dem Mysterium von Golgatha dem Menschen das Geistige enthüllt hat und auch der Christus im Kosmos, hat nur einen Bestand bis zum Venusdasein.",
        "Die Menschen lebten vor dem Mysterium von Golgatha mit dem Himmel, aber dieser Himmel ist so sinnlich, daß er auch mit dem Venusdasein verschwindet.",
        "Was über das Venusdasein hinaus bleibt, das hat seine Keime nur im Menschen.",
        "Der Christus mußte aus dem Weltenall zu dem Menschen kommen, wenn er mit dem Menschen den Gang in die Ewigkeit antreten wollte.",
        "Weil das alles so ist, wie ich es Ihnen jetzt geschildert habe, deshalb stieg der Christus aus dem Kosmos herab, um fortan mit dem zu sein, was als Keim im Menschen in die Ewigkeit hinaus dauert."
      ],
      [
        "Das ist das große kosmische Ereignis, das man verstehen muß.",
        "Die Menschen vor dem Mysterium von Golgatha konnten den Gott, den Christus im Weltenall verehren.",
        "Die Menschen, die darauf kommen mußten - und es ist die Zeit seit dem Mysterium von Golgatha immer mehr und mehr darauf gekommen, daß nur im Menschen der Keim"
      ],
      [
        "ist für die ewige Weltenzukunft -, diese Menschen mußten einen Christus haben nicht im Weltenall draußen, das zet£ällt, sondern ver­eint mit dem Menschen, mit der menschlichen Organisation, mit dem menschlichen Reiche.",
        "Wörtlich wahr ist es: Dasjenige, was da ist im weiten Umkreis der Sinne als Sterne, als Himmeiskörper, es wird vergehen.",
        "Aber das Wort, der Logos, der erschienen ist in dem Christus, und der sich vereinigt mit dem ewigen Wesenskern des Menschen, der wird bleiben.",
        "Und das ist eine wörtliche Wahrheit, wie die Dinge in den wirklichen okkulten, religiösen Urkunden wört­liche Wahrheiten sind."
      ],
      [
        "Das aber ist auch der Grund, warum wir gewissermaßen einen Dua­lismus in der Namengebung haben müssen - ich habe darauf schon hingedeutet -, in der Namengebung Christus Jesus.",
        "Den Christus, der dem außerirdischen Weltenall angehört, dieses geistige Wesen, das vor dem Mysterium von Golgatha nicht mit den Menschen der Erde ver­bunden war, muß man auf der einen Seite erkennen; das darf nicht vergessen werden, denn das ist heruntergestiegen und hat sich mit der Menschennatur, mit dem Jesus verbunden.",
        "In dem Dualismus Chri­stus Jesus liegt dasjenige, was notwendig ist, zu verstehen.",
        "In dem Christus muß man das Kosmisch-Geistige sehen; in dem Jesus muß man dasjenige sehen, durch welches dieses Kosmisch-Geistige in die historische Entwickelung eingetreten ist und sich so mit der Mensch­heit verbunden hat, daß es mit dem Menschenkeim nun weiter in die Ewigkeiten leben kann."
      ],
      [
        "Dieses mit den alten Mysterien zusammenhängende Christusge­heimnis zu verhüllen, zu entstellen, das war gewissermaßen die Auf­gabe der Kirche in den verflossenen Jahrhunderten.",
        "Und versuchen Sie einmal, den Werdegang der Menschheit in diesen verflossenen Jahrhunderten wirklich zu studieren, versuchen Sie sich klarzumachen, wie es denjenigen einzelnen Menschen gegangen ist, welche den Christus Jesus wirklich suchen wollten, die wirklich den Weg finden wollten zu dem Christus Jesus: es war immer ein Märtyrerweg.",
        "Er mußte immer gesucht werden, der Christus Jesus, gegen die Konven­tionen, wie er ja auch heute selbstverständlich gegen dasjenige, was von den Konventionen geblieben ist, gesucht werden muß.",
        "Aber"
      ],
      [
        "man kann dem Christus-Geheimnis nicht nahekommen, wenn man es nicht verbindet mit dem Naturgeheimnis."
      ],
      [
        "Sie sehen, die Notwendigkeit, die wir vor unsere Seele hingestellt haben, von dem Herunterkommen des Christus aus kosmischen Höhen zu dem Menschenkeim, das Geheimnis von dem Jesus-Werden des Christus, man kann es nur verstehen, wenn eine Einheit wird Naturbetrachtung, Weltbetrachtung, Kosmologie und die Wissen­schaft von dem Werden des Menschen und des Göttlichen in der Menschheit.",
        "Das möchte man gerade von einer gewissen Seite her ver­meiden, daß Naturwissenschaft zu gleicher Zeit Geisteswissenschaft und Geisteswissenschaft zu gleicher Zeit Naturwissenschaft werde.",
        "Das ist ja das Bestreben der meisten Theologen, und auf der andern Seite wiederum das Bestreben der meisten Naturgelehrten der Ge­genwart, daß eine Schranke aufgerichtet werde zwischen der Natur­wissenschaft auf der einen Seite und der Geisteswissenschaft auf der andern Seite.",
        "Nur ja soll nicht über den Christus Jesus etwas gesagt werden, was zu gleicher Zeit zusammenhängt mit der Erdenevolu­tion, und nur ja soll nicht über die Erdenevolution, das heißt über ihre einzelnen Teile etwas gesagt werden, was zusammenhängt mit dem großen geistigen Mysterium."
      ],
      [
        "Indem man diese Dinge berührt, berührt man in der Tat Wichtig­stes, Allerwichtigstes im Menschenleben der Gegenwart.",
        "Denn jenes konfuse Geschwätz von allerlei Geistigem, auf das auch unsere Freunde einen so oftmals aufmerksam machen, und zum Ekel einen aufmerksam machen, dieses konfuse Geschwätz vom Geiste nützt gar nichts.",
        "Ich meine, es kommt alle Augenblicke einer und sagt: Nun sehen Sie einmal, der hat wiederum ganz theosophisch oder anthropo­sophisch geredet, er hat das und das gesagt! - Dieses bequeme Suchen nach Stützen in der gegenwärtigen Konfusion, das ist nicht dasjenige, was wir anstreben sollen, sondern wir sollen schon auf dem Funda­ment feststehen, das uns die Geisteswissenschaft sein wird.",
        "Und die Zeit ist zu ernst, um weitere Kompromisse, besonders auf diesem Ge­biete zu pflegen."
      ],
      [
        "Die Brücke zu schaffen zwischen dem Naturwissen, überhaupt zwischen dem Wissen des Wahrgenommenen und dem Wissen desjenigen,"
      ],
      [
        "zu dem die Sünde, zu dem die Erlösung, kurz, zu dem die religiösen Wahrheiten gehören, die Brücke zu schaffen zwischen die­sen zwei Gebieten, das kann nur geschehen, wenn man den Mut haben wird, in das Geistige wirklich real einzudringen.",
        "Aber auch über die Lebenswahrheiten wird man nichts Vernünftiges wissen können, wenn man nicht den Mut hat, in das Geistige real, wirklich einzudringen.",
        "Zum Eindringen in das geistig Reale gehört vor allen Dingen diese Möglichkeit: wiederum etwas zurückzublicken zu dem dreifachen Sonnenmysterium der alten Zeit, aber in dem neuen Sinne, wie es der gegenwärtigen Menschheit angemessen ist.",
        "Geradeso wie die Sonne eine Dreiheit ist, so ist ja der Mensch auch eine Dreiheit.",
        "Aber es handelt sich darum, daß wir diesen dreifachen Menschen wirklich studieren.",
        "Das ist Wichtigstes für die Gegenwart: den drei­fachen Menschen zu studieren.",
        "Ich möchte Ihnen heute einmal vor­bereitend - morgen und übermorgen werden wir diese wichtige Sache zu Ende führen - schematisch etwas angeben, was Sie führen kann auf dem Wege, der eigentlich gesucht werden müßte, um den drei­fachen Menschen zu begreifen."
      ],
      [
        "Denken Sie sich einmal das Folgende - also das, was ich jetzt skiz-ziere, soll ein Schema sein -, denken Sie sich, Sie hätten ein Gebilde, das ganz und gar nur Bild, nur Abbild sei, das im Grunde gar keine Bedeutung in sich selber hat, also Abbild ist.",
        "Das will ich so skizzieren:"
      ],
      [
        "ich zeichne einfach einen Kreis (siehe Zeichnung Seite 71, blau), eine Kreisfläche.",
        "Das ist ein Gebilde, das Abbild ist von etwas anderem, aber dadurch, daß es Abbild ist, hat es das andere, wovon es Abbild ist, vollständig aufgezehrt.",
        "Es ist ja sonderbar, wenn ich folgendes sage, aber denken Sie sich einmal: In unserer Kuppel, in der kleinen Kuppel arbeiten vier Damen; nehmen wir einmal an, diese vier Da­men würden, auf jeder Seite zwei, malen, sich selber porträtieren, aber dieses Porträtieren hätte eine besondere Folge.",
        "Also denken Sie sich, diese vier Damen, die porträtieren sich in der kleinen Kuppel, malen sich selber da ab, aber dieses Sich selber Porträtieren, das hätte eine ganz bestimmte Folge: sie verschwänden nämiich dadurch, sie gingen über in ihr Abbild, sie hörten auf zu sein.",
        "Wenn sie fertig sind, sind sie nicht mehr da.",
        "Dadurch, daß die Abbilder entstanden sind,"
      ],
      [
        "sind sie selbst nicht mehr da. - Solch ein Gebilde stellen Sie sich unter dem, was ich hier skizzenhaft aufgezeichnet habe, einmal vor: ein Gebilde, das dadurch entstanden ist, daß es gemacht worden ist von etwas, wovon es Abbild ist; aber dadurch, daß das Abbild da ist, ist das andere aufgezehrt."
      ],
      [
        "Nun ist aber dieses Aufgezehrte nicht allein in der Welt.",
        "Stellen Sie sich nämlich vor, es wäre die Geschichte noch nicht aus mit diesen vier Damen.",
        "Gut, diese vier Damen wären verschwunden, sie hätten sich da aufgemalt und wären verschwunden; aber die Bilder sind da.",
        "Sie sind nicht allein da im Weltenall, das Weltenall ist mit seinen Kräften außerdem noch da.",
        "Die Damen sind verschwunden, sind von den Bildern gewissermaßen aufgesogen worden; aber dadurch, daß die Bilder da sind, zieht sich aus dem Weltenall wiederum Substan­tielles zusammen und bildet die Damen neu, allerdings jetzt als Kinder:"
      ],
      [
        "sie entstehen langsam wieder, enstehen da daneben.",
        "So entsteht neben diesem Gebilde wiederum sein Urbild (siehe Zeichnung, gelb)."
      ],
      [
        "# Bild s. 71"
      ],
      [
        "müßte es eigentlich ein Stückchen hinein zeichnen, ich zeichne es nun daneben auf: das ist das Urbild.",
        "Das ist das Urbild, aber es ist ein sehr loser Zusammenhang zwischen diesem Abbild und dem Urbild, ein sehr loser Zusammenhang.",
        "Beide haben fast gar nichts miteinander zu tun.",
        "Dieses Abbild ist richtig verhärtet und hat fast gar nichts mit seinem Urbilde zu tun."
      ],
      [
        "Dann denken Sie sich ein zweites Gebilde.",
        "Ich will das zweite Ge­bilde so skizzieren, daß ich es nun auch als Abbild mache (siehe Zeichnung Seite 72, violett); nur ist das erste drinnen in dem zweiten.",
        "Das erste ist etwas für sich, aber es ist auch drinnen in dem zweiten.",
        "Also ich zeichne da kühn über das erste das zweite drüber.",
        "Das ist wiederum solch ein Abbild, und wiederum so ähnlich ein Abbild von einem andern, das ich auch nun da drauf zeichnen will (siehe Zeichnung,"
      ],
      [
        "# Bild s. 72"
      ],
      [
        "rot); das muss ich aber nun schon inniger mit dem verbin­den.",
        "Da ist die Sache also so, daß ich nicht den Vergleich wählen könnte, den ich früher mit den vier Damen gewählt habe, sondern wenn ich bezüglich dieses Bildes und Abbildes jetzt einen Vergleich wählen würde, müßte ich so sagen: Es sind also die vier Damen da, sie malen in der kleinen Kuppel, und während sie malen, geht schon auch etwas von ihnen selber auf, wird aufgesogen.",
        "Aber nur zur Hälfte werden sie aufgesogen; zuletzt sind sie so, daß sie - nun, ich will also sagen, um nicht einen unästhetischen Vergleich hervorzu­rufen: Es wird von der einen die linke Körperhäffte aufgesogen, die rechte ragt noch heraus von dem Bilde; von der andern die rechte Körperhälfte aufgesogen, die linke ragt noch heraus.",
        "Also sie sind teilweise aufgesogen; teilweise ragen sie noch heraus.",
        "Das ist das zweite."
      ],
      [
        "Dann stellen Sie sich ein drittes vor, das also wiederum das erste mitumfaßt und das zweite auch mitumfaßt (siehe Zeichnung Seite 73, grün).",
        "Das aber ist zum großen Teil mit seinem Abbilde verbunden, das ist noch nicht getrennt von seinem Abbilde.",
        "Da müßte ich also, wenn ich den Vergleich festhalten wollte, sagen: Die Damen malen, aber sie bleiben auch als Damen vorhanden, und das Ganze, was ich vor mir habe, sind die Damen und ihre Abbilder.",
        "Das ist vorhanden (siehe Zeichnung, orange), das ist zum größten Teile auch im Urbilde vorhanden."
      ],
      [
        "So haben Sie also hier (Zeichnung Seite 71) etwas schematisch ge­zeichnet: zuerst oben ein Abbild, verhärtet, kristallisiert, es hat möglichst"
      ],
      [
        "# Bild s. 73"
      ],
      [
        "wenig mit seinem Urbilde zu tun; das Urbild ist daneben, neu entstehend.",
        "Das ist nämlich Ihr Kopf; der ist der materiellste, ver­härtetste Teil der Menschennatur.",
        "Sein Urbild hat geradezu nichts mit ihm zu tun, entsteht neu; und wenn Sie achtundzwanzig Jahre alt geworden sind, ist Ihr Kopf so, daß er aus sich selber gar nicht ein­mal mehr etwas hergibt, ausgewachsen ist.",
        "Der größte Materialist in der Menschennatur ist das Haupt.",
        "Ein zweites Gebilde ist Brust und Atmung und alles, was dazugehört.",
        "Das ist ungefähr so, daß ich das zweite als Schema gebrauchen könnte (Zeichnung Seite 72).",
        "Das ist schon mehr verbunden, da hängen Geist und Materie schon mehr zu­sammen, das ist schon durchgeistigter.",
        "Alles das, was Lunge und Atmungsprozeß ist, ist schon für die Erde vergeistigter.",
        "Und was übrigbleibt, Gliedmaßen, im Zusammenhange damit alles das, was die Sexualität umfaßt, da ist Geistiges mit Physischem eins, da sind sie noch zusammen.",
        "Das gehört zum dritten Schema (Zeichnung oben)."
      ],
      [
        "Das ist der dreifache Mensch.",
        "Ich habe es Ihnen heute nur schema­tisch auf die Tafel zeichnen können.",
        "Dieses zu gleicher Zeit wunder­bare und furchtbare, dieses großartige und tiefeindringende Myste­rium vom dreifachen Menschen hängt wiederum mit dem dreifachen Sonnenmysterium zusammen.",
        "Das aber hängt wiederum zusammen"
      ],
      [
        "mit all den Wahrheiten, die wir brauchen wie das Brot des Lebens für alles dasjenige, was sich setzen muß an die Stelle dessen, was in das Chaos, was in die Sackgasse hineingekommen ist und zu den gegen­wärtigen Menschheitskatastrophen geführt hat.",
        "Davon werden wir morgen weiter sprechen."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG Dornach, 25. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Auf den dreigeteilten Menschen habe ich gestern schematisch hinge­wiesen. Es ist ja durchaus so, daß aus unserem gegenwärtigen Geistes­leben heraus wenig Empfindungen vorhanden sind für das Verständ­nis des Wesens des Menschen, so wie es erfaßt werden muß vom geisteswissenschaftlichen Standpunkte. Allein, wir müssen uns doch bemühen, an dieses Menschenwesen heranzukommen. Die wichtig­sten Vorstellungen, die man auch über das Gesamtleben des Menschen gewinnen muß, über die Entwickelung des Menschen zwischen dem Tode und einer neuen Geburt, auch sie sind nur zu beherrschen, wenn man ausgeht von einem solchen Verständnisse, das an diesen dreige­teilten Menschen anknüpft. Betrachten wir für heute einmal im ein­zelnen diesen dreigeteilten Menschen.",
      "Es wurde ja gestern schon darauf aufmerksam gemacht, daß wir da zunächst auf das Haupt des Menschen hinweisen können. In einem gewissen Sinne ist dieses Haupt des Menschen wirklich eine Art selb­ständige Formwesenheit. Sie können sich ja selber hinstellen vor ein Menschenskelett, und Sie können leicht das Haupt abheben. Wie eine Kugel können Sie es abheben. In Wirklichkeit ist allerdings die Trennung zwischen den drei Gliedern der menschlichen Natur nicht so einfach, daß man sagen könnte: Dasjenige, was man da vom üb­rigen Skelett so bequem abhebt wie eine Kugel, das ist dieser Hauptes-teil. - So streng sind die Dinge nicht geschieden. Aber man muß sich ja allmählich herausarbeiten aus dem bloßen Schematismus, auch aus dem, den einem die Natur selbst nahelegt, zu einer lebendigen Empfindung. Und ich mußte ja gestern schon, wie Sie gesehen haben, nicht etwa drei nebeneinanderliegende Kreise aufzeichnen, sondern einen Kreis für das Haupt, einen zweiten Kreis, der dieses Haupt übergriff, und einen dritten Kreis, der wiederum beide übergriff. So daß, wenn man schematisch den dreigeteilten Menschen zeichnen würde nach seiner physischen Wesenheit, man eben ihn so zu zeich­nen haben würde, daß man sagt: Der Hauptesteil (siehe Zeichnung",
      "roter Kreis A), der Rumpfteil (oval, gelb), und dann der Glied­maßenteil (orange) -, eigentlich drei Kugeln, wenn auch diese Kugeln in die Länge gezogen werden müssen. Mit dem Hauptesteil, also mit dem, was hier als roter Kreis A bezeichnet worden ist, mit diesem Hauptesteil steht das Geistige, das, wie Sie gestern gesehen haben, eine junge Bildung ist, im Zusammenhange (hellschraffierter kleiner Kreis, weiß). Dieses Geistige des Hauptes, das ist eine junge geistige Bildung, während das Haupt selbst eine alte physische Bildung, eine physische Formwesenheit ist. Bei dem Haupte ist daher vor allen Dingen richtig, was man sonst im allgemeinen für den Menschen an­führt, was aber in dieser Allgemeinheit, wie man es anführt, nicht ganz richtig ist; für das Haupt ist es richtig. Was ich hier als Weißes, Geistiges bezeichnet habe in bezug auf das Haupt, das ist, wenn Sie schlafen, heraußen aus dem Haupte. Wenn Sie wachen, ist es mit dem Haupt vereinigt, ist zum größten Teile im physischen Haupte drinnen. Es kann sich also am leichtesten vom physischen Haupte trennen; es geht heraus und geht wiederum zurück, hinein.",
      "# Bild s. 76",
      "Das ist schon durchaus nicht so für den mittleren Menschen, nennen wir ihn meinetwillen den Brustmenschen. Alles dasjenige, was vom Thorax, vom Brustkorbe eingeschlossen ist, von den Rippen und vom Rückgrat, das ist mit dem Geistigen verbunden, aber es ist nicht",
      "so ausgesprochen das Geistige heraußen, wenn Sie schlafen. Das Geistige steht schon auch während des Schiafens für diesen mittleren Menschen in einer starken Verbindung mit dem Physischen. Und für den dritten Menschen, für den Gliedmaßenmenschen, wozu auch der sexuelle Mensch gehört, da ist eigentlich praktisch eine Trennung zwischen Schlafen und Wachen in Wirklichkeit doch nicht vorhanden. Da kann man gar nicht sagen, daß wirklich das Geistig-Seelische im Schlafe sich trennt; die bleiben mehr oder weniger auch im Schlafe vereint. So daß man nach einem andern Schema den wachenden Menschen gut so zeichnen könnte, daß man sagte: Wenn das der physische Mensch ist, wachend (siehe Zeichnung a, dunkel schraf­",
      "# Bild s. 77",
      "fiert, rot), so würde dieses der geistige Mensch sein (hell schraffiert, weiß). Das würde der schlafende Mensch sein (siehe Zeichnung b, rot und weiß); es bliebe also dieses mehr oder weniger mit dem Leib­lichen vereint, und nur das geht eigentlich heraus (siehe Zeichnung b). Das würde von einem gewissen Gesichtspunkte aus die eigentliche Zeichnung sein für den Gegensatz des wachenden und schlafenden Menschen.",
      "Nun werden Sie die wichtigen Dinge, die wir zu besprechen haben, nur dann verstehen, wenn Sie diese Gliederung des dreigeteilten Men­schen, die wir eben besprochen haben, für sich durchkreuzen mit einer andern Gliederung des Menschen, die anknüpft an dasjenige, was ich die vorige Woche hier auseinandergesetzt habe.",
      "Wenn wir so noch einmal das Haupt, den Rumpfmenschen, den Gliedmaßenmenschen durchsprechen, so können wir ja sagen: Im eigentlichsten Sinne Mensch ist nur der Rumpfmensch. Der ist daher auch de4enige, dem der lebendige Odem eingehaucht ist durch die Elohim. Er ist der atmende Mensch. Da ist die Teilung nicht so ganz bequem wie beim Skelett; der Atmungsvorgang durch Nase und Mund gehört schon zum Rumpfmenschen. Also, nicht wahr, es ist die Teilung in Wirklichkeit nicht so schematisch bequem zu machen, wie man es sich gern aufzeichnen möchte, aber das sind ja natürlich die Schwierigkeiten des Verständnisses für eine solche Sache.",
      "Also der eigentliche Mensch, der Erdenmensch, ist der Rumpf-mensch. Und der Kopfmensch, als physische Gestaltung, das ist eigentlich nicht etwas durch und durch Menschliches. Man kann nicht sagen, daß der Menschenkopf etwas durch und durch Mensch­liches ist. Der Menschenkopf hat eben sehr viel Ahrimanisches in sich. Er ist im wesentlichen so gegliedert, wie er gegliedert ist, aus dem Grunde, weil gewisse Bildungsprinzipien in ihm namentlich dieje­nigen sind, die noch von der alten Sonne, also von diesem zweiten Erdenstadium - Saturn, Sonne -, zurückgeblieben sind. Unser Haupt mit seiner ganzen komplizierten Bildung wäre nicht so, wie es ist, wenn es nicht seine erste Bildung bekommen hätte in diesen uralten Zeiten der alten Sonne. Und es sind also eigentlich alte, uralte Bil­dungsprinzipien, die heute hereinragen in die Erdensphäre, und die wir aus diesem Grunde als ahrimanische bezeichnen müssen. Zurück­gebliebene Prinzipien müssen wir ja immer als luziferische oder ahrimanische, je nach den Gesichtspunkten, ansehen. Dasjenige, was den Menschen als Erdenmenschen ausmacht, wo die Prinzipien des Erdenwerdens hauptsächlich spielen, das ist der Brust-, der Rumpf-mensch.",
      "Der Gliedmaßenmensch ist auch nicht rein der Mensch, sondern der hat sehr viel Luziferisches in sich, und seine Bildungsprinzipien sind eigentlich noch nicht volle Bildungsprinzipien, sondern sie sind solche, welche ihre volle Ausgestaltung erst haben werden, wenn die Erde ins Venusstadium gekommen sein wird, wenn also das Jupiter-stadium vorausgegangen und im Übergange sein wird in das Venusstadium.",
      "Dann werden die Bildungsprinzipien, die heute, ich möchte sagen, noch diesen Schatten von einem Wesen ausbilden, der der Extremitätenmensch ist, dieses dritte menschliche Wesen, in ihrer vollen Intensität, in ihrer richtigen Gestalt wirken: wenn die Venus-zeit da sein wird. Also das nimmt der Mensch voraus, was in der Venuszeit erst da sein wird und bildet es heute unvollkommen, keim-haft, läßt es nicht über das Keimhafte hinauskommen.",
      "So ist die Sache kosmisch betrachtet. Kosmisch betrachtet also sind wir in unserer Gestaltung so, daß wir in unserem Haupte gewisser­maßen nach den Kräften die alte Sonnenzeit wiederholen, in unserer Brust das Erdenwerden tragen; indem wir Extremitätenmenschen sind, tragen wir die Keime zum Venuswerden in uns. Das ist kosmisch betrachtet.",
      "Humanistisch betrachtet ist es etwas anderes. Da müssen wir auf die menschliche Individualität sehen, wie diese menschliche Indivi­dualität von Inkarnation zu Inkarnation schreitet. Da müssen wir sagen: Was wir heute in dieser Inkarnation als Haupt an uns tragen, das hat sich verwandt erwiesen unserer vorigen Inkarnation; dasjenige, was wir jetzt als Brustmenschen in uns tragen, das ist eigentlich rein verwandt unserer gegenwärtigen Inkarnation; und dasjenige, was wir als Extremitätenmensch in uns tragen, das wird ja Haupt in der näch­sten Inkarnation, das ist verwandt schon mit der nächsten Inkarnation. Ich habe Ihnen in der vorigen Woche gesagt: Das Haupt hat etwas Ver­räterisches, insbesondere in seinem Negativ. Wenn Sie einen Abdruck nehmen würden von der Physiognomie des Hauptes und diese Phy­siognomie anschauen würden, so würden Sie in dieser negativen Physiognomie Ihres Hauptes viel von dem erkennen, was Sie in einer vorigen Inkarnation angestellt haben.",
      "Umgekehrt ist es mit dem Extremitätenmenschen. Da können Sie aber nicht einen Abdruck nehmen, sondern da müssen Sie anders vor­gehen. Denken Sie sich vom Menschen das Haupt und den Rumpf-menschen weg, aber denken Sie sich alles das, was nun Ihre Hände und Beine tun, machen Sie sich ein Bild von dem, was Ihre Hände und Beine tun. Sie müssen sich da eine Art Landkarte machen. Nicht wahr, jedesmal, wenn Sie mit Ihren Händen das oder jenes tun, geschieht",
      "es ja an einem andern Orte. Sie gehen ja außerdem herum, Sie kommen in Beziehung zu andern Wesen Wenn Sie das alles malen würden, was Ihre Hände und Beine tun, und ein Bild im Laufe Ihres Lebens entwerfen würden - es würde ein sehr bewegtes Bild werden - von dem, was Ihre Hände und Füße, Arme und Beine tun, dann würden Sie in dieser Zeichnung eine komplizierte Landkarte erblicken; aus der würden Sie viel von dem verraten bekommen, was Ihnen karmisch aufbewahrt ist für Ihre nächste Inkarnation.",
      "Dar­innen würden Sie viel ablesen können von dem Karma der nächsten Inkarnation. Es ist durchaus bedeutsam: So wie der Negativabdruck der Physiognomie in seiner Ruhe, in seiner festen, konturierten Zeichnung verräterisch ist für das, was in der vorigen Inkarnation schon geschehen ist, so würde dasjenige, was man abpunktieren könnte von dem, wie sich Arme, Hände, Beine, Füße verhalten, außerordent­lich instruktiv sein für das, was der Mensch in der nächsten Inkar­nation ausführen wird.",
      "Namentlich ist es auch instruktiv für das, was der Mensch in der nächsten Inkarnation ausführt, wohin er geht, wo­hin ihn seine Beine tragen. Wenn Sie alle die Orte, wenn Sie einfach den Weg verfolgen würden, wohin Sie Ihre Beine tragen, so würde da eine Landkarte daraus werden.",
      "Sie würden merkwürdige Figuren bekommen. Nicht ganz ohne Einfluß sind die Neigungen der Men­schen auf diese Figuren. Es spricht sich viel von den geheimen Nei­gungen in diesen Figuren aus. Die sind sehr verräterisch, diese Spuren, die da bleiben, für dasjenige, was die nächste Inkarnation dem Men­schen bringt.",
      "Also das wäre humanistisch betrachtet. Das andere war kosmisch betrachtet.",
      "Diese Gliederung des Menschen, &e, ich möchte sagen, abzielt auf die Gegenwart, bedeutet aber wiederum eine Verbindung mit den Geheimnissen der alten Mysterien, in denen man mehr atavistisch die Sache gewußt hat, aber in denen man solche Geheimnisse, wie sie jetzt eben angeführt worden sind, schon gekannt hat. Es gibt eine schöne Sage, anknüpfend an den König Salomo, über die Bestimmt­heit, mit welcher der Mensch seine Füße dorthin setzt, wo er seinen Tod finden soll. Gleichsam ist der Sinn dieser Sage, daß ein bestimmter Ort auf der Erde ist, wo der Mensch seinen Tod finden soll - Sie",
      "werden einen Zweigvortrag finden, wo ich gerade über diese Salomo-Sage vorgetragen habe -, dahin setzt der Mensch dann seine Füße. Das hängt zusammen mit dem alten Mysterienwissen von diesen Dingen.",
      "Nun, der Mensch hat ja eigentlich, wenn er so im allgemeinen lebt, nur sein gewöhnliches Bewußtsein; aber er ist, wie Sie sehen, ein recht kompliziertes Wesen, der Mensch. Wenn er wachend ist, wenn er sein jüngstes geistiges Glied, das Haupt, in seinem physischen Haupte drinnen hat, dann weiß er ja nichts von seinem Haupte.",
      "Sie werden mit Recht sagen: Gott sei Dank, daß man nichts vom Haupte weiß; denn weiß man vom Haupte, so ist es nur der Kopfschmerz. - Auf eine andere Weise wird sich der Mensch seines Hauptes nicht bewußt, als wenn er Kopfschmerz kriegt; dann weiß er, daß er ein Haupt hat. Sonst bleibt das unbewußt, im eminentesten Sinne unbewußt, viel un­bewußter, als ein übriges Glied des menschlichen physischen Leibes.",
      "Der Mensch darf ganz froh sein, wenn er im normalen Bewußtsein von seinem Haupte nichts weiß. Aber unter diesem Bewußtsein des Hauptes, das gewöhnlich eigentlich nur von der Außenwelt Kenntnis nimmt, das nur darauf ausgeht, zu wissen von dem, was in der Um­gebung ist, unter diesem Wissen ruht ein anderes, eine Art Traum­bewußtsein, ein Traumeswissen.",
      "Ihr Haupt träumt fortwährend. Und während Sie von der Außenwelt wissen in der Art, wie Ihnen das wohi bekannt ist, träumen Sie eigentlich unter der Schwelle des Be­wußtseins, im Unterbewußtsein, fortwährend.",
      "Und was Sie da träu­men, dieses Träumen im Haupte, wenn Sie es voll auffassen könnten, wenn Sie es ganz in das Bewußtsein hereinbringen könnten, so würde Ihnen das ein Bild geben, ein richtiges, zusammenfassendes Bild Ihrer vorigen Inkarnation. Denn Ihre vorige Inkarnation träumen Sie unterbewußt in Ihrem Haupte.",
      "Das ist schon so. Es ist immer ein leises Bewußtsein vorhanden, das nur übertäubt ist von dem stärkeren Lichte des gewöhnlichen Bewußtseins, ein träumendes Bewußtsein von der vorigen Inkarnation.",
      "Mit dem Jahre 747 vor dem Mysterium von Golgatha ist das äußere Bewußtsein so stark geworden, daß nach und nach dieses Unterbe­wußtsein der vorigen Inkarnation völlig ausgelöscht worden ist. Aber",
      "vor diesem Jahre 747 hat man viel gewußt von diesem Traumesbewußt­sein des Hauptes. Daher finden Sie auch überall auf dem Grunde der alten Kulturen die wiederholten Erdenieben als eine Tatsache ange­führt. Das rührt einfach davon her, daß dazumal dieses Unterbewußt­sein des Hauptes noch nicht so völlig in den Hintergrund getreten war wie jetzt, wie das geschehen ist durch den vierten, namentlich durch den fünften nachatlantischen Zeitraum.",
      "Von dem, was seelisch-geistig mit dem Brustkorb und dem Rumpf des Menschen zusammenhängt, wissen Sie ja auch im gewöhnlichen Bewußtsein sehr wenig. Das ist schon an sich ein Traumhaftes. Es schlägt nur manchmal, und dann sehr chaotisch, unregelmäßig, dieses Rumpf- und Brustkorbbewußtsein in das Bewußtsein des Menschen im Traume herauf.",
      "Wenn der Mensch regelmäßig atmen kann, wenn sein Herzschlag regelmäßig ist, also wenn alle seine Funktionen des Brustkorbes und Rumpfes regelmäßig sind, so verläuft das Bewußt­sein des Rumpfes nicht so hell wie das Kopfbewußtsein, sondern es verläuft auch im gewöhnlichen Leben traumhaft. Man träumt im Ge­fühle - ich habe das im vorigen Jahre hier ausgeführt - von diesem mittleren Menschen.",
      "Aber dieses, was da im Gefühle liegt, was der Mensch nur im Gefühle erlebt, wenn es heraufgeholt wird durch ein mehr heliseherisch werdendes Bewußtsein, wenn mit andern Wor­ten der Mensch das, was in seinem Brustkorb sich bewußt abspielt, ebenso zu überschauen lernt, wie er sonst im wachen Zustande nur das überschaut, was in seinem Hauptesbewußtsein ist, ja, dann teilt sich dieses Rumpf- und Brustkorbbewußtsein deutlich in zwei Teile. Der eine Teil träumt zurück in die ganze Zeit zwischen dem vorigen Tod und der jetzigen Geburt oder Empfängnis.",
      "Also während Sie traumhaft, in sehr tiefen Träumen in Ihrem Hauptesbewußtsein unter­bewußt haben dasjenige, was in der vorigen Inkarnation war, haben Sie das, was seit der vorigen Inkarnation bis zu der jetzigen Geburt in der Zwischenzeit verflossen ist, in den Träumen des Brustkorbes. Und in den Träumen, die mehr nach den unteren Partien des Brustkorbes gelegen sind, haben Sie ein starkes Bewußtsein von dem, was zwischen Ihrem kommenden Tode und dem nächsten Erdenieben ist.",
      "Also das Bewußtsein, das im Brustkorb konzentriert ist, das aber mehr oder",
      "weniger unterbewußt bleibt für den gegenwärtigen Menschen, das ist eigentlich ein traumhaftes Bewußtsein sowohl für die Zeit vor dieser Geburt wie für die Zeit nach diesem Tode. Was zwischen unserem letzten Erdentode und unserer nächsten Erdenempfängnis liegt, mit Ausnahme desjenigen oder auch mit Einschluß desjenigen, was wir jetzt erleben zwischen Geburt und Tod, das enträtselt sich für dieses Unterbewußtsein des mittleren Menschen.",
      "Und in demjenigen, was recht sehr stark durch das ganze Leben hin­durch unterbewußt bleibt, was nur heraufgezogen werden kann, wenn der Mensch imstande ist, es durch immerwährendes Sich-Beschäftigen mit geisteswissenschaftlichen Studien und Übungen heraufzuziehen, so daß gewisse Momente des Schlaflebens, die sonst eben schlafend, unbewußt vor sich gehen, heraufgehoben werden und der Mensch mitten aus dem Schlaf heraus bewußt wird, da kann sich das Tableau von der nächsten Erdeninkarnation aus diesem dritten Menschen, aus dem Unterbewußtsein des Extremitätenmenschen heraus entwickeln. Dasjenige, was der Mensch als sein gewöhnliches, heute wachendes Bewußtsein hat, ist eigentlich eine Art Seitentrieb des Menschen; das strahlt in das Haupt herein von außen. Aber hinter diesem Bewußt­sein liegt ein anderes Bewußtsein, das sich verbreitet über die vorige Inkarnation, über das Leben von der vorigen Inkarnation bis zu die­ser, über das Leben von dieser Inkarnation bis zur nächsten, und dann wiederum über die nächste Inkarnation. Nur verschläft der Mensch dieses Bewußtsein.",
      "Es ist das Bewußtsein der vorigen Inkarnation im Haupte. In all den Organen, die vorzugsweise dem Ausatmen dienen, wirkt ein starkes Bewußtsein für das Leben zwischen der vorigen Inkarnation und die­ser. In all den Funktionen, die vorzugsweise dem Einatmen dienen, wirkt ein Bewußtsein von der jetzigen Inkarnation bis zur nächsten Erdeninkarnation. Und in dem Gliedmaßenmenschen, in all den ge­heimnisvollen Vorgängen des Gliedmaßenmenschen wirkt ein sehr, sehr unterbewußt bleibendes Bewußtsein der nächsten menschlichen Inkarnation.",
      "Diese Bewußtseine sind mehr oder weniger verdeckt worden seit dem Beginn der vierten nachatlantischen Zeit, seit 747 vor dem Mysterium",
      "von Golgatha. Und der Beruf unserer Zeit ist wiederum, aus dem allgemeinen chaotischen Menschenbewußtsein heraus die be­stimmten Bewußtsejne von diesen konkreten Vorgängen der kos­mischen und der Menschheitsevolution herauszuholen.",
      "Mit alldem, was ich jetzt entwickelt habe, muß sich eine andere Ein­sicht in die Menschenwesenheit, ich möchte sagen, kreuzen. Ja, es ist schon notwendig, daß wir uns in so schwierige Erörterungen ein­lassen, wir kommen sonst nicht zum genaueren Verständnisse. Ich hätte ja so gerne, wenn für diese schwierigen Erörterungen nicht nur ein gewisses Über-sich-ergehen-Lassen waltete, sondern wenn gerade für diese schwierigen Dinge - weil das der gegenwärtigen Menschheit so notwendig wäre - ein bißchen Enthusiasmus, ein bißchen tempe­ramentvolles Eingehen aufzubringen wäre, was ja in einer Gesell­schaft der heutigen Zeit so unendlich schwierig ist.",
      "Sehen Sie, Sie richten Ihre Sinne nach außen. Da finden Sie durch Ihre Sinne die Außenwelt als eine sinnen£aliige ausgebreitet. Ich zeichne das schematisch, was da nach außen als sinnenfällig ausge­breitet um uns herum liegt. Bitte, es soll das, was da außen herum liegt, dieses (siehe Zeichnung, blau) sein. Wenn Sie Ihre Augen, Ihre Ohren, wenn Sie Ihren Geruchssinn, was Sie wollen, auf die Außenwelt rich­ten, so wendet sich Ihnen gewissermaßen entgegen, es wendet sich diesen Sinnen entgegen dasjenige, was die Innenseite dieses Außen ist -also bitte: die Innenseite dieses Außen (links). Nehmen Sie an, Sie wenden Ihre Sinne dem zu, was ich da gezeichnet habe (siehe Zeich­nung, Pfeile), so sind diese Sinne auf diese Außenwelt gerichtet und Sie sehen das, was sich innen hier hineinneigt. Nun folgt die schwie­rige Vorstellung, auf die ich aber schon kommen muß. Alles das, was Sie da anschauen, zeigt sich Ihnen von innen. Denken Sie sich, daß das auch eine Außenseite haben muß. Nun, ich will es schematisch da­durch vor Ihre Seele rufen, daß ich sage: Wenn Sie so hinausschauen, sehen Sie als Grenze Ihres Schauens das Firmament: das hier ist ja fast so, nur daß ich es klein gezeichnet habe. Aber jetzt denken Sie sich, Sie könnten flugs da hinausfliegen und könnten da durchfliegen und von der andern Seite gucken, Ihre sinnenfalligen Eindrücke von der andern Seite angucken. Also Sie könnten so hinschauen (siehe",
      "# Bild s. 85",
      "Zeichnung, Pfeile oben). Bitte, das sehen Sie natürlich nicht; aber könnten Sie so hinschauen, so würde das der andere Aspekt sein. Sie würden aus sich heraus müssen und würden von der andern Seite Ihre ganze sinnenfällige Welt anschauen müssen. Sie würden also das, was sich Ihnen als Farbe zuwendet, von der Rückseite betrachten, das, was sich Ihnen als Ton zuwendet, von der Rückseite betrachten und so weiter; was sich Ihnen als Geruch zuwendet, würden Sie von der Rückseite betrachten, Sie würden von der Rückseite den Geruch in die Nase fassen. Also von der andern Seite denken Sie sich die Welt-betrachtung: wie einen Teppich ausgebreitet die sinnenfälligen Dinge, und nun den Teppich von der andern Seite einmal angesehen. Ein",
      "kleines Stück sehen Sie nur, ein sehr, sehr kleines Stück von dieser Rückseite. Dieses sehr kleine Stück, das kann ich hier nur dadurch zur Darstellung bringen, daß ich die Sache so mache: Denken Sie sich jetzt, ich zeichne das, was Sie da von der andern Seite sehen würden, rot ein; so daß ich sagen kann, schematisch sieht man das Sinnen-fällige so: Wie man es gewöhnlich sieht, so sieht es blau aus; sieht man es von der andern Seite, so sieht es rot aus, aber das sieht man natür­lich nicht.",
      "In diesem, was man da rot sehen würde, steckt erstens alles das drin, was erlebt werden kann zwischen dem Tod und einer neuen Geburt, zweitens alles das, was beschrieben ist in der «Geheimwissen-schaft im Umriß» als Saturn-, Sonnen-, Monden-, Erdenentwickelung und so weiter. Dasjenige liegt da aufgespeichert, was eben verborgen ist für die sinnenfällige Anschauung.",
      "Das ist da auf der andern Seite der Kugel. Aber ein kleines Stück sehen Sie davon; das kann ich nur so zeichnen, daß ich jetzt sage: Nehmen Sie dieses kleine Stück von dem Roten, das ginge da herüber (siehe Zeichnung, unten) und durch­kreuzt sich mit dem Blauen, so daß das Blaue, statt daß es jetzt vorne ist, dahinter ist.",
      "Ich müßte eigentlich hier vierdimensional zeichnen, wenn ich es wirklich zeichnen würde, ich kann es daher nur ganz schematisch zeichnen. Also da (links) sind die Sinne jetzt hier dem Blauen zugewendet; da sind sie nicht zugewendet dem Blauen, son­dern dem Roten, das Sie sonst nicht sehen.",
      "Aber hinter dem Rot hat sich jetzt gekreuzt das, was sonst gesehen wird, und das ist jetzt dar­unter. Und dieses kleine Stück, das da sich kreuzt mit dem andern, das sehen Sie fortwährend im gewöhnlichen Bewußtsein.",
      "Das sind näm­lich Ihre aufgespeicherten Erinnerungen. Alles, was als Erinnerung entsteht, entsteht nicht nach Gesetzen dieser äußeren Wahrnehmungs-weit, sondern es entsteht nach den Gesetzen, die dieser hinteren Welt da entsprechen.",
      "Dieses Innere, das Sie als Ihre Erinnerungen haben, das entspricht wirklich dem, was da auf der andern Seite ist (rechts). In­dem Sie in sich hineinblicken, in alles das, was Ihre Erinnerungen sind, sehen Sie tatsächlich die Welt auf einem Stück von der andern Seite; da ragt das andere ein wenig herein, da sehen Sie die Welt von der andern Seite.",
      "Und wenn Sie jetzt durch Ihre Erinnerungen, wie sie so aufgeschrieben sind, durchschlüpfen könnten - ich habe vor",
      "acht Tagen davon gesprochen -, wenn Sie da hinunter könnten, unter Ihre Erinnerungen sehen und sie von der andern Seite anschauen könnten, von da drüben (siehe Zeichnung, rechts), da würden Sie die Erinnerungen als Ihre Aura sehen. Da würden Sie den Menschen sehen als ein geistig-seelisches aurisches Wesen, wie Sie sonst die äußere Welt sinnenfällig in den Wahrnehmungen sehen. Nur wäre es eben­sowenig angenehm - wie ich das vor acht Tagen hier charakterisiert habe -, weil da der Mensch noch nicht schön ist von dieser andern Seite.",
      "Also das ist das Interessante, was man kreuzen muß mit dem an­dern Verständnis des dreigliedrigen Menschen. Diese Kreuzung hier, die liegt nun im mittleren Menschen, im Brustmenschen. Sie erinnern sich an die Zeichnung, die ich vor acht Tagen gemacht habe, wo ich ja die in sich gewundenen Lemniskaten mit den zurückgeschiagenen Schleifen hatte: die müßte ich hier zeichnen. Hier müßte ich diesen Brustmenschen zeichnen mit den zurückgeschiagenen Lemniskaten (siehe Zeichnung Seite 85, links unten): Das würde zusammenfallen mit der Erinnerungssphäre. So daß dieser dreigliedrige Mensch hier in seinem mittleren Teil diese Umwendung des Menschen hat, wo das Innere äußerlich und das Äußere innerlich wird, wo Sie ein Tableau, das Sie sonst als Welttableau, als die große Welterinnerung sehen würden, nun als Ihre eigene kleine mikrokosmische Erinnerung sehen. Sie sehen in Ihrem gewöhnlichen Bewußtsein dasjenige, was sich zugetragen hat von Ihrem dritten Jahre an bis jetzt: das ist eine innere Aufzeichnung, ein kleines Stück für das, was gleichartig mit dem ist, was sonst Aufzeichnung für die ganze Weltenevolution ist, was auf der andern Seite liegt.",
      "Nicht ohne Grund habe ich seinerzeit, wie den meisten von Ihnen wohl bekannt sein wird, davon gesprochen - und ich habe es ja wieder­um ausgeführt in meinem letzten Buche «Von Seelenrätseln» am Schluß in der Anmerkung -, nicht ohne Grund habe ich davon ge­sprochen, daß der Mensch eigentlich zwölf Sinne hat. Diese Sinne müssen wir uns so denken, daß eine Anzahl von diesen zwölf Sinnen nach dem Sinnenfälligen zugewendet sind, eine andere Anzahl von diesen zwölf Sinnen sind aber nach rückwärts gerichtet. Sie sind auch",
      "da unten (siehe Zeichnung Seite 85) nach dem gerichtet, was schon das Gewendete ist. Und zwar sind nach dem äußeren Sinnenfaliigen gerichtet: Ichsinn, Denksinn, Sprachsinn, Hörsinn, Sehsinn, Ge­schmackssinn, Geruchssinn. Diese Sinne sind gerichtet nach dem Sinnenfälligen. Die andern Sinne kommen ja eigentlich dem Men­schen deshalb nicht zum Bewußtsein, weil sie zunächst nach seinem eigenen Inneren und dann nach dem Umgekehrten der Welt gerichtet sind. Das sind vorzugsweise: Wärmesinn, Lebenssinn, Gleichge­wichts sinn, Bewegungssinn, Tastsinn. So daß wir sagen können: Für das gewöhnliche Bewußtsein liegen sieben Sinne im Hellen (oben) und fünf Sinne im Dunkeln (unten). Und diese fünf Sinne, die im Dunkeln liegen, die sind der andern Seite der Welt zugewendet, auch im Menschen der andern Seite (siehe Zeichnung Seite 85).",
      "Sie können daher einen vollständigen Parallelismus haben zwischen den Sinnen und zwischen etwas anderem, wovon wir gleich sprechen werden (siehe Zeichnung, Kreis). Also nehmen wir an, wir hätten als Sinne zu verzeichnen den Hörsinn, den Sprachsinn, den Denksinn, den Ichsinn, den Wärmesinn, den Lebenssinn, den Gleichgewichts­sinn, den Bewegungssinn, den Tastsinn, den Geruchssinn, den Ge­schmackssinn, den Sehsinn, so haben Sie im wesentlichen alles das­jenige, was vom Ichsinn geht bis zum Geruchssinn, im Hellen liegend, in dem, was dem gewöhnlichen Bewußtsein zugänglich ist (siehe Zeichnung, schraffiert). Und alles dasjenige, was abgewendet ist vom gewöhnlichen Bewußtsein, so wie die Nacht vom Tag abgekehrt ist, das gehört den andern Sinnen an.",
      "Es ist natürlich die Grenze auch wiederum nur schematisiert; es fällt etwas ineinander; es sind die Wirklichkeiten nicht so bequem. Aber diese Gliederung des Menschen nach den Sinnen ist so, daß Sie schon im Schema an die Stelle der Sinne nur zu zeichnen brauchen die Himmelszeichen, so haben Sie: Widder, Stier, Zwillinge, Krebs, Löwe, Jungfrau, Waage - sieben Himmelszeichen für die helle Seite; fünf für die dunkle Seite: Skorpion, Schütze, Steinbock, Wassermann, Fische: Tag, Nacht; Nacht, Tag. Und Sie haben einen vollständigen Parallelismus zwischen dem mikrokosmischen Menschen - dem, was zugewendet ist seinen Sinnen, und dem, was abgewendet ist, aber",
      "# Bild s. 89",
      "eigentlich zugewendet ist seinen unteren Sinnen - und zwischen dem, was im äußeren Kosmos den Wechsel bedeutet von Tag und Nacht. Es geht gewissermaßen im Menschen dasselbe vor, was im Weltenge­bäude vorgeht. Im Weltengebäude wechseln Tag und Nacht, im Menschen wechselt auch Tag und Nacht, nänllich Wachen und Schlafen, wenn sich auch beide voneinander emanzipiert haben für den gegenwärtigen Bewußtseinszyklus des Menschen. Während des Tages ist der Mensch zugewendet den Tagessinnen; wir können ebensogut sagen: Widder, Stier, Zwillinge, Krebs, Lowe, Jungfrau, Waage, wie wir sagen könnten: Ichsinn, Denksinn, Sprachsinn und so weiter. Sie können jedes Ich eines andern Menschen sehen, Sie können die Gedanken des andern Menschen verstehen, Sie können hören, sehen, schmecken, riechen: das sind die Tagessinne. In der Nacht ist der Mensch so, wie sonst die Erde nach der andern Seite ge­wendet ist, den andern Sinnen zugewendet, nur sind diese noch nicht",
      "vollentwickelt. Sie werden erst nach der Venuszeit so voll entwickelt sein, daß sie wahrnehmen können, was da nach der andern Seite ist. Sie sind noch nicht so voll entwickelt, daß sie das wahrnehmen kön­nen, was da nach der andern Seite ist. Sie sind in Nacht gehüllt, wie beim Durchgang durch die andern Himmelsregionen, die andern Bilder des Tierkreises, die Erde in der Nacht ist. Das Durchschreiten des Menschen durch seine Sinne ist ganz zu parallelisieren mit dem Gang - ob Sie nun sagen der Sonne um die Erde oder der Erde um die Sonne, das ist ja schließlich für diesen Zweck gleichgültig; aber diese Dinge hängen zusammen. Und diese Zusammenhänge kannten die Weisen der alten Mysterien sehr gut.",
      "Das verschwand für das Bewußtsein eben allmählich in der vierten nachatlantischen Zeit, aber es muß wieder heraufgeholt werden, muß auch gegen die Widerstände, die sich dagegen erheben, wiederum heraufgeholt werden für die Menschheitskultur. Denn in den Be­griffen, die man sich da aneignet, liegt dasjenige, was einem auch ver­ständlich erscheinen läßt, was nun im sozialen, im geschichtlichen Leben vor sich geht. Solange Sie Naturleben und geistiges Leben in der Art trennen, wie das die moderne Menschheit heute liebt, so lange kommen Sie nicht zu solchen Begriffen, die im geschichtlichen Werden eine Rolle spielen könnten, sondern Sie werden überwältigt von den Begriffen, die im geschichtlichen Leben eine Rolle spielen. Überwältigt werden Sie. Dafür gibt es ja viele Beispiele.",
      "Nicht wahr, die Menschen haben seit, nun, sagen wir zweihundert Jahren, wie sie glauben, furchtbar viel gedacht. Man kann zusammen­stellen, was die Menschen seit zweihundert Jahren gedacht haben, was sie an Idealen ausgebildet haben, wovon sie als den großen Idealen gesprochen haben und immer wieder sprechen: von dem Ideal der Aufklärungszeit bis jetzt zu dem Ideal des großen Cäsar-Ersatzes Woodrow Wilson. All dasjenige, was da über die verschiedenen Ideale ge­sprochen worden ist, das haben die Menschen durch die Jahrhunderte, durch zwei Jahrhunderte hindurch gedacht; das bildete die Gedanken der Menschen. Aber die Weltgeschichte ist wenig bewegt worden von diesen Gedanken. Die Weltgeschichte ist von etwas ganz anderem be­wegt worden: von jenen Gedanken, die in den Dingen gewirkt und gewebt",
      "haben. Und niemals waren eigentlich die Gedanken, die in den Menschenköpfen wimmeln, weiter entfernt von den großen kosmi­schen Gedanken, die in den Dingen leben, als in unserer Zeit. Das­jenige, was seit, man kann sagen, hundertfünfzig Jahren die Menschen dazu getrieben hat, eine gewisse Gestaltung der Welt zu bewirken, das sind nicht die Gedanken von Freiheit, Gleichheit, Brüderlichkeit, Gerechtigkeit und so weiter, sondern das sind die Gedanken, welche verwoben waren zum Beispiel mit dem Aufkommen des mechanischen Webstuhls.",
      "Daß der mechanische Webstuhl hereingekommen ist in die moderne Entwickelung in der zweiten Hälfte des 18. Jahrhunderts, daß sich diese bedeutsame Erfindung des mechanischen Webstuhls an die Stelle der alten Handweberei hineingefunden hat in die Mensch­heitsentwickelung, und daß von diesem mechanischen Webstuhl die ganze Maschinenkultur der neueren Zeit ausgegangen ist, darinnen weben die objektiven Gedanken, die wirklichen Gedanken, welche der Welt die Gestaltung gegeben haben, die sie bis heute hat, und aus der das gegenwärtige katastrophale Chaos entstanden ist.",
      "Man muß nicht, wenn man eine Geschichte schreiben will des gegenwärtigen katastrophalen Chaos, an die Gedanken, die in dem Menschenbewußt-sein gewimmelt haben, sich wenden, sondern an diese objektiven Ge­danken von der Begründung, von der Erfindung des mechanischen Webstuhls bis zu dem Werden der Großindustrie und ihres Schattens, des Sozialismus. Denn wenn das auch scheinbare Gegensätze sind, Großindustrie und Sozialismus, so sind sie polarische Gegensätze, die zueinander gehören, sie sind nicht voneinander zu trennen.",
      "Bei die­sen objektiven Gedanken muß man anfragen und das geschichtliche Werden betrachten.",
      "Da findet man dann, daß die Menschen sich vielen Illusionen hinge­geben haben in der Zeit des 18. Jahrhunderts, das 19. Jahrhundert hindurch, und namentlich in dem Teil des 20. Jahrhunderts, in dem wir jetzt leben. Sie haben sich vielen Illusionen hingegeben in ihren Gedanken; aber überwältigt sind sie worden von den objektiven, historisch-kosmischen Gedanken. Die weben in den Dingen. Und ein Interesse für diese objektiv webenden Gedanken, wenn auch ein furchtbar einseitiges Interesse, haben eigentlich doch nur diejenigen",
      "Menschen allmählich entwickelt, welche den Sozialismus als Welt­anschauung ausgebildet haben. Und das ist etwas ungeheuer Charak­teristisches. Wenn Sie das 19. Jahrhundert verfolgen: das Bourgeois­tum verliert immer mehr und mehr das Interesse für große Weltan­schauungsfragen.",
      "Große Weltanschauungsfragen werden sogar dem Bourgeoistum höchst unangenehm, sie werden womöglich in die Ästhetik hinein abgeschoben. Ob es geistige Wesen gibt oder nicht, darüber mag man, wenn man ein richtiger Durchschnittsbourgeois ist, von der Bühne herunter allerlei vernehmen, wo man nicht daran zu glauben braucht, wo es nicht darauf ankommt, ob die Dinge Wahr­heiten sind oder nicht: da läßt man sich von Björnson und ähnlichen Leuten das Mannigfaltigste vormachen.",
      "So in das Ästhetische hinein, in das Spielen mit allerlei sogenannten Künstlerischem, dahin wird das Weltanschauungsgemäße für das Bourgeoistum in der neueren Zeit abgeschoben. Wirklich für Weltanschauungsfragen die Köpfe gegen­seitig zerschlagen - womit ich das nicht als ein Ideal betrachten will im physischen Sinne, aber im geistigen Sinne ist es in gewissem Sinne ein Ideal: Sie wissen, ich habe mit einem seht starken Aplomb darauf hingewiesen, daß ich gerne Temperament haben würde auch beim Vertreten anthroposophischer Wahrheiten -, die Köpfe eingeschiagen hat man sich in den letzten Jahrzehnten auf sozialistischem Gebiete.",
      "Und darum haben sich die andern nicht gekümmert. Sie haben, möchte ich sagen, diejenigen Leute allein gelassen, welche die Welt eigentlich von einem sehr engen Aspekt aus gesehen haben, welche die Welt nur gesehen haben von dem Aspekt der Fabrik aus, von dem Inneren der Fabrik aus, von dem Inneren der Buchdruckerwerkstätte und so weiter.",
      "Und es ist ja im höchsten Maße interessant, was für eine sogenannte Weltanschauung herausgekommen ist von dem Aspekte der Fabrik aus: denn das ist der Sozialismus! Das ist vom Aspekt des Inneren der Fabrik, das ist vom Aspekt der Menschen aus, die gar nichts anderes kennen als das Innere der Fabrik.",
      "Und für das, was da sich heranentwickelte, hat sich das Bourgeoistum, das sich mit allerlei abstrakten Ideen, aber auch im Abstrakten mit Ästhetisieren befaßt, so daß man nicht sehr sich die Köpfe zu zerschlagen brauchte, für das, was da unten sich entwickelt hat, hat sich das Bourgeoistum",
      "eigentlich wenig interessiert. Und so ist das Bourgeoistum kurioser­weise in die Mitte hineingekommen zwischen der absterbenden, der ganz absterbenden alten Weltanschauung, die alles Geistige verloren hat, die alle großen Fragen überhaupt in den Ästhetizismus hinein abschieben möchte, und dem, was da neu heraufkommt, dem Sozialis­mus, der überhaupt noch keine Begriffe hat, der noch lediglich mit Worten allerlei Systeme bereitet, weil er die Welt überhaupt noch nicht sehen kann, sondern nur die Fabrik sehen kann, nur das alleräußerste Mechanische sehen kann. Denken Sie sich doch, was es eigentlich zu bedeuten hat, wenn der Mensch innerlich nichts weiß von Mineral-reich, Pflanzenreich und Tierreich, sondern nur weiß von der Art und Weise, wie in der Maschine mechanisch sich dieser oder jener Zapfen auf und ab bewegt, das oder jenes zugefeilt und zugehobelt wird und dergleichen! Der Sozialismus ist eine Weltanschauung, die da fußt auf der Anschauung einer Welt, die rein mechanisch ist. Es ist für den Sozialisten das Stück der Welt herausgeschnitten, das mechanisch ist; danach formt er sich seine Begriffe.",
      "Das hat man entstehen lassen, weil man das Prinzip hatte, sich eigentlich nur ästhetisch um die Dinge zu bekümmern. Als die Theo­sophische Gesellschaft zuerst begründet worden ist, hat man ja auch ihren Hauptgrundsatz gesehen in der Liebe aller Menschen unterein­ander. Wieviel ist darüber deklamiert worden! Nun, ich habe mich ja über diesen Punkt genügend ausgesprochen. Er ist ebenso bequem wie unfruchtbar. Aber er rührt auch davon her, daß man möglichst abschieben will dasjenige, was wirklich konkreten Inhalt hat, in das Inhaltlose hinein. Und so konnte man auch nicht ein eigentliches Interesse fassen für den wirklichen Hergang der Dinge. Einzelnen Menschen fiel das Absonderliche herkömmlicher, sagen wir Ge­schichtsbetrachtung auf. Nehmen wir einen Fall.",
      "Nehmen Sie eine beliebte Darstellung der römischen Kaiserzeit; versuchen Sie in den Schulbüchern oder in den Büchern auch, die die großen autoritativen Historiker geschrieben haben, über die rö­mische Kaiserzeit sich zu unterrichten. Ich glaube, Sie werden aus diesen Darstellungen außerordentlich wenig vernehmen über eine gewisse Persönlichkeit, die schon unter Nero eine bedeutende politische",
      "Rolle gespielt hat - so unter Nero kommen bereits die politi­schen Aspirationen durch -, dann ganz besonderes Aufsehen erregte und bedeutenden Einfluß auf die Politik Roms erlangte unter Ves­pasian und Titus, so daß man sagen kann, daß diese Persönlichkeit die Seele der Regierung des Vespasianus und Titus war. Dann wendete sich diese Persönlichkeit der andern Seite zu unter der Regierung des Domitianus, den sie für einen Schädling des Römertums hielt.",
      "Sie wendete sich der andern Seite zu. Es wird ihr der Prozeß gemacht, ein sehr aufsehenerregender Prozeß in Rom, der sehr interessant ver­laufen ist, in welchem Domitianus geradezu umgeschlagen hat vom Tyrannen zu einem, der sich gegenüber diesem Prozeß nicht zu helfen wußte, daher den Mann nicht verurteilen konnte.",
      "Dann wiederum, als an Stelle des Domitianus Nerva kam, sehen wir diese Persönlich­keit wieder energisch verbunden mit dem Kaiser, dem Cäsar. Da sehen wir aber diese Persönlichkeit große Politik machen aus der gesamten Weltanschauung der damaligen Zeit heraus, und wir sehen zu gleicher Zeit diese Persönlichkeit versuchen, wirklich weitgehende, aus dem Kosmos heruntergeholte Begriffe noch einmal, zum letzten Male während der römischen Kaiserzeit, den politischen Ereignissen ein­zuimpfen.",
      "Und kurioserweise finden Sie ja eine richtige Beschreibung dieser Persönlichkeit in gar keinem gebräuchlichen Geschichtsbuche, nicht einmal bei Sueton und Tacitus> sondern nur bei Philostratus. Und Philostratus schildert auch nur so, daß man nicht wußte, schildert er einen Roman oder eine Wirklichkeit.",
      "Er schildert das Leben des Apollonius von Tyana. Denn Apollonius von Tyana ist der, von dem ich Ihnen gesagt habe, daß er von Nero an bis zu Nerva und nament­lich unter Vespasian und Titus einen so großen Einfluß auf die Politik hatte, und den Philostratus beschrieb.",
      "Und der Tübinger Theologe Baur, der Historiker Baur war im höchsten Grade erstaunt, daß man so gar nichts findet über eine Persönlichkeit wie den Apollonius, der eine erste Rolle spielen müßte in der Geschichtsdarstellung. Natür­lich sah Baur nicht ein, worauf es ankommt.",
      "Es kommt darauf an, daß in Apollonius eine Persönlichkeit dasteht in der Geschichte, die schon diesen großen Einfluß hatte, aber die aus dem überragenden Kosmischen die Prinzipien herunterholte. Das war dem ins Römische",
      "hineinmündenden Christentum im höchsten Grade fatal. Und nun bitte ich Sie zu berücksichtigen, daß alles dasjenige, was historisch da ist, von der Kirche Gnaden da ist. Es ist ja sonst nichts da, als was die Kirche aus Gnade den Menschen gelassen hat. Nicht mit Unrecht hat ein alter, gar nicht dummer Mensch behauptet, daß es überhaupt einen Plato, einen Sophokles gar nicht gegeben hatte, sondern daß Mönche vom 14. und 15. Jahrhundert des Sophokles' Dramen ge­schrieben hatten; denn ein strikter Beweis dafür, daß Sophokles ge­lebt hat, ist nicht da. Wenn auch die Behauptung nicht haltbar ist, selbstverständlich Unsinn ist, aber wie unsicher alles dasjenige ist, was geschichtliche Fable convenue ist, wir haben es ja schon oft be­tont. Und wir müssen uns darüber klar sein. Wir müssen ja die Gegen­wart mit der Vergangenheit in Zusammenhang bringen, denn wir nähern uns jetzt einer großen, bedeutungsvollen Frage.",
      "Wir haben wiederum, vom modernen Standpunkte jetzt, hinge­wiesen auf den dreigeteilten Menschen, auf diesen Zusammenhang mit kosmischen Wahrheiten, auf die Notwendigkeit, daß das wieder ent­hüllt werde. Ja, worin bestand denn eigentlich die Haupttätigkeit der Kirche, namentlich seit dem achten ökumenischen Konzil in Konstan­tinopel, das 869 stattfand? Sie bestand darinnen, auszulöschen, aus­zutilgen vom menschlichen Bewußtsein dasjenige, was in jenen alten Zeiten auch das Christentum an Verständnis für den Zusammenhang des Menschen mit dem Kosmos, mit der großen geistigen Welt hatte. Mit einer wahren Ängstlichkeit hat man alles dasjenige beseitigt, was diesen Zusammenhang verrät. Und nur, weil nicht alles beseitigt werden kann, weil das Karma dem schon entgegenwirkt, sind solche Werke wie das des Philostratus geblieben. Und daher können Sie es begreifen, wenn Sie jetzt die Vergangenheit mit der Gegenwart zu­sammenbringen, daß gewisse Menschen von kirchlicher Seite heil­lose Angst bekommen, wenn in der Gegenwart wiederum die An­knüpfung gepflogen werden soll zwischen dem, was den Menschen zu einem Wesen des Kosmos macht, und diesem Menschen selber und seiner Aufgabe.",
      "Es geht eben nicht an, daß man nur schläfrig dasjenige verfolgt, was durch die anthroposophische Bewegung gewollt sein sollte. Man",
      "muß es in lebendigem, kraftvollem Bewußtsein verfolgen. Das ist schon notwendig. Damit habe ich hingewiesen auf dasjenige, was wir nun weiter ausführen wollen. Morgen werde ich den Vortrag hier halten, in dem ich diese Betrachtungen fortsetzen werde."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Auf den dreigeteilten Menschen habe ich gestern schematisch hinge­wiesen.",
        "Es ist ja durchaus so, daß aus unserem gegenwärtigen Geistes­leben heraus wenig Empfindungen vorhanden sind für das Verständ­nis des Wesens des Menschen, so wie es erfaßt werden muß vom geisteswissenschaftlichen Standpunkte.",
        "Allein, wir müssen uns doch bemühen, an dieses Menschenwesen heranzukommen.",
        "Die wichtig­sten Vorstellungen, die man auch über das Gesamtleben des Menschen gewinnen muß, über die Entwickelung des Menschen zwischen dem Tode und einer neuen Geburt, auch sie sind nur zu beherrschen, wenn man ausgeht von einem solchen Verständnisse, das an diesen dreige­teilten Menschen anknüpft.",
        "Betrachten wir für heute einmal im ein­zelnen diesen dreigeteilten Menschen."
      ],
      [
        "Es wurde ja gestern schon darauf aufmerksam gemacht, daß wir da zunächst auf das Haupt des Menschen hinweisen können.",
        "In einem gewissen Sinne ist dieses Haupt des Menschen wirklich eine Art selb­ständige Formwesenheit.",
        "Sie können sich ja selber hinstellen vor ein Menschenskelett, und Sie können leicht das Haupt abheben.",
        "Wie eine Kugel können Sie es abheben.",
        "In Wirklichkeit ist allerdings die Trennung zwischen den drei Gliedern der menschlichen Natur nicht so einfach, daß man sagen könnte: Dasjenige, was man da vom üb­rigen Skelett so bequem abhebt wie eine Kugel, das ist dieser Hauptes-teil. - So streng sind die Dinge nicht geschieden.",
        "Aber man muß sich ja allmählich herausarbeiten aus dem bloßen Schematismus, auch aus dem, den einem die Natur selbst nahelegt, zu einer lebendigen Empfindung.",
        "Und ich mußte ja gestern schon, wie Sie gesehen haben, nicht etwa drei nebeneinanderliegende Kreise aufzeichnen, sondern einen Kreis für das Haupt, einen zweiten Kreis, der dieses Haupt übergriff, und einen dritten Kreis, der wiederum beide übergriff.",
        "So daß, wenn man schematisch den dreigeteilten Menschen zeichnen würde nach seiner physischen Wesenheit, man eben ihn so zu zeich­nen haben würde, daß man sagt: Der Hauptesteil (siehe Zeichnung"
      ],
      [
        "roter Kreis A), der Rumpfteil (oval, gelb), und dann der Glied­maßenteil (orange) -, eigentlich drei Kugeln, wenn auch diese Kugeln in die Länge gezogen werden müssen.",
        "Mit dem Hauptesteil, also mit dem, was hier als roter Kreis A bezeichnet worden ist, mit diesem Hauptesteil steht das Geistige, das, wie Sie gestern gesehen haben, eine junge Bildung ist, im Zusammenhange (hellschraffierter kleiner Kreis, weiß).",
        "Dieses Geistige des Hauptes, das ist eine junge geistige Bildung, während das Haupt selbst eine alte physische Bildung, eine physische Formwesenheit ist.",
        "Bei dem Haupte ist daher vor allen Dingen richtig, was man sonst im allgemeinen für den Menschen an­führt, was aber in dieser Allgemeinheit, wie man es anführt, nicht ganz richtig ist; für das Haupt ist es richtig.",
        "Was ich hier als Weißes, Geistiges bezeichnet habe in bezug auf das Haupt, das ist, wenn Sie schlafen, heraußen aus dem Haupte.",
        "Wenn Sie wachen, ist es mit dem Haupt vereinigt, ist zum größten Teile im physischen Haupte drinnen.",
        "Es kann sich also am leichtesten vom physischen Haupte trennen; es geht heraus und geht wiederum zurück, hinein."
      ],
      [
        "# Bild s. 76"
      ],
      [
        "Das ist schon durchaus nicht so für den mittleren Menschen, nennen wir ihn meinetwillen den Brustmenschen.",
        "Alles dasjenige, was vom Thorax, vom Brustkorbe eingeschlossen ist, von den Rippen und vom Rückgrat, das ist mit dem Geistigen verbunden, aber es ist nicht"
      ],
      [
        "so ausgesprochen das Geistige heraußen, wenn Sie schlafen.",
        "Das Geistige steht schon auch während des Schiafens für diesen mittleren Menschen in einer starken Verbindung mit dem Physischen.",
        "Und für den dritten Menschen, für den Gliedmaßenmenschen, wozu auch der sexuelle Mensch gehört, da ist eigentlich praktisch eine Trennung zwischen Schlafen und Wachen in Wirklichkeit doch nicht vorhanden.",
        "Da kann man gar nicht sagen, daß wirklich das Geistig-Seelische im Schlafe sich trennt; die bleiben mehr oder weniger auch im Schlafe vereint.",
        "So daß man nach einem andern Schema den wachenden Menschen gut so zeichnen könnte, daß man sagte: Wenn das der physische Mensch ist, wachend (siehe Zeichnung a, dunkel schraf­"
      ],
      [
        "# Bild s. 77"
      ],
      [
        "fiert, rot), so würde dieses der geistige Mensch sein (hell schraffiert, weiß).",
        "Das würde der schlafende Mensch sein (siehe Zeichnung b, rot und weiß); es bliebe also dieses mehr oder weniger mit dem Leib­lichen vereint, und nur das geht eigentlich heraus (siehe Zeichnung b).",
        "Das würde von einem gewissen Gesichtspunkte aus die eigentliche Zeichnung sein für den Gegensatz des wachenden und schlafenden Menschen."
      ],
      [
        "Nun werden Sie die wichtigen Dinge, die wir zu besprechen haben, nur dann verstehen, wenn Sie diese Gliederung des dreigeteilten Men­schen, die wir eben besprochen haben, für sich durchkreuzen mit einer andern Gliederung des Menschen, die anknüpft an dasjenige, was ich die vorige Woche hier auseinandergesetzt habe."
      ],
      [
        "Wenn wir so noch einmal das Haupt, den Rumpfmenschen, den Gliedmaßenmenschen durchsprechen, so können wir ja sagen: Im eigentlichsten Sinne Mensch ist nur der Rumpfmensch.",
        "Der ist daher auch de4enige, dem der lebendige Odem eingehaucht ist durch die Elohim.",
        "Er ist der atmende Mensch.",
        "Da ist die Teilung nicht so ganz bequem wie beim Skelett; der Atmungsvorgang durch Nase und Mund gehört schon zum Rumpfmenschen.",
        "Also, nicht wahr, es ist die Teilung in Wirklichkeit nicht so schematisch bequem zu machen, wie man es sich gern aufzeichnen möchte, aber das sind ja natürlich die Schwierigkeiten des Verständnisses für eine solche Sache."
      ],
      [
        "Also der eigentliche Mensch, der Erdenmensch, ist der Rumpf-mensch.",
        "Und der Kopfmensch, als physische Gestaltung, das ist eigentlich nicht etwas durch und durch Menschliches.",
        "Man kann nicht sagen, daß der Menschenkopf etwas durch und durch Mensch­liches ist.",
        "Der Menschenkopf hat eben sehr viel Ahrimanisches in sich.",
        "Er ist im wesentlichen so gegliedert, wie er gegliedert ist, aus dem Grunde, weil gewisse Bildungsprinzipien in ihm namentlich dieje­nigen sind, die noch von der alten Sonne, also von diesem zweiten Erdenstadium - Saturn, Sonne -, zurückgeblieben sind.",
        "Unser Haupt mit seiner ganzen komplizierten Bildung wäre nicht so, wie es ist, wenn es nicht seine erste Bildung bekommen hätte in diesen uralten Zeiten der alten Sonne.",
        "Und es sind also eigentlich alte, uralte Bil­dungsprinzipien, die heute hereinragen in die Erdensphäre, und die wir aus diesem Grunde als ahrimanische bezeichnen müssen.",
        "Zurück­gebliebene Prinzipien müssen wir ja immer als luziferische oder ahrimanische, je nach den Gesichtspunkten, ansehen.",
        "Dasjenige, was den Menschen als Erdenmenschen ausmacht, wo die Prinzipien des Erdenwerdens hauptsächlich spielen, das ist der Brust-, der Rumpf-mensch."
      ],
      [
        "Der Gliedmaßenmensch ist auch nicht rein der Mensch, sondern der hat sehr viel Luziferisches in sich, und seine Bildungsprinzipien sind eigentlich noch nicht volle Bildungsprinzipien, sondern sie sind solche, welche ihre volle Ausgestaltung erst haben werden, wenn die Erde ins Venusstadium gekommen sein wird, wenn also das Jupiter-stadium vorausgegangen und im Übergange sein wird in das Venusstadium."
      ],
      [
        "Dann werden die Bildungsprinzipien, die heute, ich möchte sagen, noch diesen Schatten von einem Wesen ausbilden, der der Extremitätenmensch ist, dieses dritte menschliche Wesen, in ihrer vollen Intensität, in ihrer richtigen Gestalt wirken: wenn die Venus-zeit da sein wird.",
        "Also das nimmt der Mensch voraus, was in der Venuszeit erst da sein wird und bildet es heute unvollkommen, keim-haft, läßt es nicht über das Keimhafte hinauskommen."
      ],
      [
        "So ist die Sache kosmisch betrachtet.",
        "Kosmisch betrachtet also sind wir in unserer Gestaltung so, daß wir in unserem Haupte gewisser­maßen nach den Kräften die alte Sonnenzeit wiederholen, in unserer Brust das Erdenwerden tragen; indem wir Extremitätenmenschen sind, tragen wir die Keime zum Venuswerden in uns.",
        "Das ist kosmisch betrachtet."
      ],
      [
        "Humanistisch betrachtet ist es etwas anderes.",
        "Da müssen wir auf die menschliche Individualität sehen, wie diese menschliche Indivi­dualität von Inkarnation zu Inkarnation schreitet.",
        "Da müssen wir sagen: Was wir heute in dieser Inkarnation als Haupt an uns tragen, das hat sich verwandt erwiesen unserer vorigen Inkarnation; dasjenige, was wir jetzt als Brustmenschen in uns tragen, das ist eigentlich rein verwandt unserer gegenwärtigen Inkarnation; und dasjenige, was wir als Extremitätenmensch in uns tragen, das wird ja Haupt in der näch­sten Inkarnation, das ist verwandt schon mit der nächsten Inkarnation.",
        "Ich habe Ihnen in der vorigen Woche gesagt: Das Haupt hat etwas Ver­räterisches, insbesondere in seinem Negativ.",
        "Wenn Sie einen Abdruck nehmen würden von der Physiognomie des Hauptes und diese Phy­siognomie anschauen würden, so würden Sie in dieser negativen Physiognomie Ihres Hauptes viel von dem erkennen, was Sie in einer vorigen Inkarnation angestellt haben."
      ],
      [
        "Umgekehrt ist es mit dem Extremitätenmenschen.",
        "Da können Sie aber nicht einen Abdruck nehmen, sondern da müssen Sie anders vor­gehen.",
        "Denken Sie sich vom Menschen das Haupt und den Rumpf-menschen weg, aber denken Sie sich alles das, was nun Ihre Hände und Beine tun, machen Sie sich ein Bild von dem, was Ihre Hände und Beine tun.",
        "Sie müssen sich da eine Art Landkarte machen.",
        "Nicht wahr, jedesmal, wenn Sie mit Ihren Händen das oder jenes tun, geschieht"
      ],
      [
        "es ja an einem andern Orte.",
        "Sie gehen ja außerdem herum, Sie kommen in Beziehung zu andern Wesen Wenn Sie das alles malen würden, was Ihre Hände und Beine tun, und ein Bild im Laufe Ihres Lebens entwerfen würden - es würde ein sehr bewegtes Bild werden - von dem, was Ihre Hände und Füße, Arme und Beine tun, dann würden Sie in dieser Zeichnung eine komplizierte Landkarte erblicken; aus der würden Sie viel von dem verraten bekommen, was Ihnen karmisch aufbewahrt ist für Ihre nächste Inkarnation."
      ],
      [
        "Dar­innen würden Sie viel ablesen können von dem Karma der nächsten Inkarnation.",
        "Es ist durchaus bedeutsam: So wie der Negativabdruck der Physiognomie in seiner Ruhe, in seiner festen, konturierten Zeichnung verräterisch ist für das, was in der vorigen Inkarnation schon geschehen ist, so würde dasjenige, was man abpunktieren könnte von dem, wie sich Arme, Hände, Beine, Füße verhalten, außerordent­lich instruktiv sein für das, was der Mensch in der nächsten Inkar­nation ausführen wird."
      ],
      [
        "Namentlich ist es auch instruktiv für das, was der Mensch in der nächsten Inkarnation ausführt, wohin er geht, wo­hin ihn seine Beine tragen.",
        "Wenn Sie alle die Orte, wenn Sie einfach den Weg verfolgen würden, wohin Sie Ihre Beine tragen, so würde da eine Landkarte daraus werden."
      ],
      [
        "Sie würden merkwürdige Figuren bekommen.",
        "Nicht ganz ohne Einfluß sind die Neigungen der Men­schen auf diese Figuren.",
        "Es spricht sich viel von den geheimen Nei­gungen in diesen Figuren aus.",
        "Die sind sehr verräterisch, diese Spuren, die da bleiben, für dasjenige, was die nächste Inkarnation dem Men­schen bringt."
      ],
      [
        "Also das wäre humanistisch betrachtet.",
        "Das andere war kosmisch betrachtet."
      ],
      [
        "Diese Gliederung des Menschen, &e, ich möchte sagen, abzielt auf die Gegenwart, bedeutet aber wiederum eine Verbindung mit den Geheimnissen der alten Mysterien, in denen man mehr atavistisch die Sache gewußt hat, aber in denen man solche Geheimnisse, wie sie jetzt eben angeführt worden sind, schon gekannt hat.",
        "Es gibt eine schöne Sage, anknüpfend an den König Salomo, über die Bestimmt­heit, mit welcher der Mensch seine Füße dorthin setzt, wo er seinen Tod finden soll.",
        "Gleichsam ist der Sinn dieser Sage, daß ein bestimmter Ort auf der Erde ist, wo der Mensch seinen Tod finden soll - Sie"
      ],
      [
        "werden einen Zweigvortrag finden, wo ich gerade über diese Salomo-Sage vorgetragen habe -, dahin setzt der Mensch dann seine Füße.",
        "Das hängt zusammen mit dem alten Mysterienwissen von diesen Dingen."
      ],
      [
        "Nun, der Mensch hat ja eigentlich, wenn er so im allgemeinen lebt, nur sein gewöhnliches Bewußtsein; aber er ist, wie Sie sehen, ein recht kompliziertes Wesen, der Mensch.",
        "Wenn er wachend ist, wenn er sein jüngstes geistiges Glied, das Haupt, in seinem physischen Haupte drinnen hat, dann weiß er ja nichts von seinem Haupte."
      ],
      [
        "Sie werden mit Recht sagen: Gott sei Dank, daß man nichts vom Haupte weiß; denn weiß man vom Haupte, so ist es nur der Kopfschmerz. - Auf eine andere Weise wird sich der Mensch seines Hauptes nicht bewußt, als wenn er Kopfschmerz kriegt; dann weiß er, daß er ein Haupt hat.",
        "Sonst bleibt das unbewußt, im eminentesten Sinne unbewußt, viel un­bewußter, als ein übriges Glied des menschlichen physischen Leibes."
      ],
      [
        "Der Mensch darf ganz froh sein, wenn er im normalen Bewußtsein von seinem Haupte nichts weiß.",
        "Aber unter diesem Bewußtsein des Hauptes, das gewöhnlich eigentlich nur von der Außenwelt Kenntnis nimmt, das nur darauf ausgeht, zu wissen von dem, was in der Um­gebung ist, unter diesem Wissen ruht ein anderes, eine Art Traum­bewußtsein, ein Traumeswissen."
      ],
      [
        "Ihr Haupt träumt fortwährend.",
        "Und während Sie von der Außenwelt wissen in der Art, wie Ihnen das wohi bekannt ist, träumen Sie eigentlich unter der Schwelle des Be­wußtseins, im Unterbewußtsein, fortwährend."
      ],
      [
        "Und was Sie da träu­men, dieses Träumen im Haupte, wenn Sie es voll auffassen könnten, wenn Sie es ganz in das Bewußtsein hereinbringen könnten, so würde Ihnen das ein Bild geben, ein richtiges, zusammenfassendes Bild Ihrer vorigen Inkarnation.",
        "Denn Ihre vorige Inkarnation träumen Sie unterbewußt in Ihrem Haupte."
      ],
      [
        "Das ist schon so.",
        "Es ist immer ein leises Bewußtsein vorhanden, das nur übertäubt ist von dem stärkeren Lichte des gewöhnlichen Bewußtseins, ein träumendes Bewußtsein von der vorigen Inkarnation."
      ],
      [
        "Mit dem Jahre 747 vor dem Mysterium von Golgatha ist das äußere Bewußtsein so stark geworden, daß nach und nach dieses Unterbe­wußtsein der vorigen Inkarnation völlig ausgelöscht worden ist.",
        "Aber"
      ],
      [
        "vor diesem Jahre 747 hat man viel gewußt von diesem Traumesbewußt­sein des Hauptes.",
        "Daher finden Sie auch überall auf dem Grunde der alten Kulturen die wiederholten Erdenieben als eine Tatsache ange­führt.",
        "Das rührt einfach davon her, daß dazumal dieses Unterbewußt­sein des Hauptes noch nicht so völlig in den Hintergrund getreten war wie jetzt, wie das geschehen ist durch den vierten, namentlich durch den fünften nachatlantischen Zeitraum."
      ],
      [
        "Von dem, was seelisch-geistig mit dem Brustkorb und dem Rumpf des Menschen zusammenhängt, wissen Sie ja auch im gewöhnlichen Bewußtsein sehr wenig.",
        "Das ist schon an sich ein Traumhaftes.",
        "Es schlägt nur manchmal, und dann sehr chaotisch, unregelmäßig, dieses Rumpf- und Brustkorbbewußtsein in das Bewußtsein des Menschen im Traume herauf."
      ],
      [
        "Wenn der Mensch regelmäßig atmen kann, wenn sein Herzschlag regelmäßig ist, also wenn alle seine Funktionen des Brustkorbes und Rumpfes regelmäßig sind, so verläuft das Bewußt­sein des Rumpfes nicht so hell wie das Kopfbewußtsein, sondern es verläuft auch im gewöhnlichen Leben traumhaft.",
        "Man träumt im Ge­fühle - ich habe das im vorigen Jahre hier ausgeführt - von diesem mittleren Menschen."
      ],
      [
        "Aber dieses, was da im Gefühle liegt, was der Mensch nur im Gefühle erlebt, wenn es heraufgeholt wird durch ein mehr heliseherisch werdendes Bewußtsein, wenn mit andern Wor­ten der Mensch das, was in seinem Brustkorb sich bewußt abspielt, ebenso zu überschauen lernt, wie er sonst im wachen Zustande nur das überschaut, was in seinem Hauptesbewußtsein ist, ja, dann teilt sich dieses Rumpf- und Brustkorbbewußtsein deutlich in zwei Teile.",
        "Der eine Teil träumt zurück in die ganze Zeit zwischen dem vorigen Tod und der jetzigen Geburt oder Empfängnis."
      ],
      [
        "Also während Sie traumhaft, in sehr tiefen Träumen in Ihrem Hauptesbewußtsein unter­bewußt haben dasjenige, was in der vorigen Inkarnation war, haben Sie das, was seit der vorigen Inkarnation bis zu der jetzigen Geburt in der Zwischenzeit verflossen ist, in den Träumen des Brustkorbes.",
        "Und in den Träumen, die mehr nach den unteren Partien des Brustkorbes gelegen sind, haben Sie ein starkes Bewußtsein von dem, was zwischen Ihrem kommenden Tode und dem nächsten Erdenieben ist."
      ],
      [
        "Also das Bewußtsein, das im Brustkorb konzentriert ist, das aber mehr oder"
      ],
      [
        "weniger unterbewußt bleibt für den gegenwärtigen Menschen, das ist eigentlich ein traumhaftes Bewußtsein sowohl für die Zeit vor dieser Geburt wie für die Zeit nach diesem Tode.",
        "Was zwischen unserem letzten Erdentode und unserer nächsten Erdenempfängnis liegt, mit Ausnahme desjenigen oder auch mit Einschluß desjenigen, was wir jetzt erleben zwischen Geburt und Tod, das enträtselt sich für dieses Unterbewußtsein des mittleren Menschen."
      ],
      [
        "Und in demjenigen, was recht sehr stark durch das ganze Leben hin­durch unterbewußt bleibt, was nur heraufgezogen werden kann, wenn der Mensch imstande ist, es durch immerwährendes Sich-Beschäftigen mit geisteswissenschaftlichen Studien und Übungen heraufzuziehen, so daß gewisse Momente des Schlaflebens, die sonst eben schlafend, unbewußt vor sich gehen, heraufgehoben werden und der Mensch mitten aus dem Schlaf heraus bewußt wird, da kann sich das Tableau von der nächsten Erdeninkarnation aus diesem dritten Menschen, aus dem Unterbewußtsein des Extremitätenmenschen heraus entwickeln.",
        "Dasjenige, was der Mensch als sein gewöhnliches, heute wachendes Bewußtsein hat, ist eigentlich eine Art Seitentrieb des Menschen; das strahlt in das Haupt herein von außen.",
        "Aber hinter diesem Bewußt­sein liegt ein anderes Bewußtsein, das sich verbreitet über die vorige Inkarnation, über das Leben von der vorigen Inkarnation bis zu die­ser, über das Leben von dieser Inkarnation bis zur nächsten, und dann wiederum über die nächste Inkarnation.",
        "Nur verschläft der Mensch dieses Bewußtsein."
      ],
      [
        "Es ist das Bewußtsein der vorigen Inkarnation im Haupte.",
        "In all den Organen, die vorzugsweise dem Ausatmen dienen, wirkt ein starkes Bewußtsein für das Leben zwischen der vorigen Inkarnation und die­ser.",
        "In all den Funktionen, die vorzugsweise dem Einatmen dienen, wirkt ein Bewußtsein von der jetzigen Inkarnation bis zur nächsten Erdeninkarnation.",
        "Und in dem Gliedmaßenmenschen, in all den ge­heimnisvollen Vorgängen des Gliedmaßenmenschen wirkt ein sehr, sehr unterbewußt bleibendes Bewußtsein der nächsten menschlichen Inkarnation."
      ],
      [
        "Diese Bewußtseine sind mehr oder weniger verdeckt worden seit dem Beginn der vierten nachatlantischen Zeit, seit 747 vor dem Mysterium"
      ],
      [
        "von Golgatha.",
        "Und der Beruf unserer Zeit ist wiederum, aus dem allgemeinen chaotischen Menschenbewußtsein heraus die be­stimmten Bewußtsejne von diesen konkreten Vorgängen der kos­mischen und der Menschheitsevolution herauszuholen."
      ],
      [
        "Mit alldem, was ich jetzt entwickelt habe, muß sich eine andere Ein­sicht in die Menschenwesenheit, ich möchte sagen, kreuzen.",
        "Ja, es ist schon notwendig, daß wir uns in so schwierige Erörterungen ein­lassen, wir kommen sonst nicht zum genaueren Verständnisse.",
        "Ich hätte ja so gerne, wenn für diese schwierigen Erörterungen nicht nur ein gewisses Über-sich-ergehen-Lassen waltete, sondern wenn gerade für diese schwierigen Dinge - weil das der gegenwärtigen Menschheit so notwendig wäre - ein bißchen Enthusiasmus, ein bißchen tempe­ramentvolles Eingehen aufzubringen wäre, was ja in einer Gesell­schaft der heutigen Zeit so unendlich schwierig ist."
      ],
      [
        "Sehen Sie, Sie richten Ihre Sinne nach außen.",
        "Da finden Sie durch Ihre Sinne die Außenwelt als eine sinnen£aliige ausgebreitet.",
        "Ich zeichne das schematisch, was da nach außen als sinnenfällig ausge­breitet um uns herum liegt.",
        "Bitte, es soll das, was da außen herum liegt, dieses (siehe Zeichnung, blau) sein.",
        "Wenn Sie Ihre Augen, Ihre Ohren, wenn Sie Ihren Geruchssinn, was Sie wollen, auf die Außenwelt rich­ten, so wendet sich Ihnen gewissermaßen entgegen, es wendet sich diesen Sinnen entgegen dasjenige, was die Innenseite dieses Außen ist -also bitte: die Innenseite dieses Außen (links).",
        "Nehmen Sie an, Sie wenden Ihre Sinne dem zu, was ich da gezeichnet habe (siehe Zeich­nung, Pfeile), so sind diese Sinne auf diese Außenwelt gerichtet und Sie sehen das, was sich innen hier hineinneigt.",
        "Nun folgt die schwie­rige Vorstellung, auf die ich aber schon kommen muß.",
        "Alles das, was Sie da anschauen, zeigt sich Ihnen von innen.",
        "Denken Sie sich, daß das auch eine Außenseite haben muß.",
        "Nun, ich will es schematisch da­durch vor Ihre Seele rufen, daß ich sage: Wenn Sie so hinausschauen, sehen Sie als Grenze Ihres Schauens das Firmament: das hier ist ja fast so, nur daß ich es klein gezeichnet habe.",
        "Aber jetzt denken Sie sich, Sie könnten flugs da hinausfliegen und könnten da durchfliegen und von der andern Seite gucken, Ihre sinnenfalligen Eindrücke von der andern Seite angucken.",
        "Also Sie könnten so hinschauen (siehe"
      ],
      [
        "# Bild s. 85"
      ],
      [
        "Zeichnung, Pfeile oben).",
        "Bitte, das sehen Sie natürlich nicht; aber könnten Sie so hinschauen, so würde das der andere Aspekt sein.",
        "Sie würden aus sich heraus müssen und würden von der andern Seite Ihre ganze sinnenfällige Welt anschauen müssen.",
        "Sie würden also das, was sich Ihnen als Farbe zuwendet, von der Rückseite betrachten, das, was sich Ihnen als Ton zuwendet, von der Rückseite betrachten und so weiter; was sich Ihnen als Geruch zuwendet, würden Sie von der Rückseite betrachten, Sie würden von der Rückseite den Geruch in die Nase fassen.",
        "Also von der andern Seite denken Sie sich die Welt-betrachtung: wie einen Teppich ausgebreitet die sinnenfälligen Dinge, und nun den Teppich von der andern Seite einmal angesehen."
      ],
      [
        "kleines Stück sehen Sie nur, ein sehr, sehr kleines Stück von dieser Rückseite.",
        "Dieses sehr kleine Stück, das kann ich hier nur dadurch zur Darstellung bringen, daß ich die Sache so mache: Denken Sie sich jetzt, ich zeichne das, was Sie da von der andern Seite sehen würden, rot ein; so daß ich sagen kann, schematisch sieht man das Sinnen-fällige so: Wie man es gewöhnlich sieht, so sieht es blau aus; sieht man es von der andern Seite, so sieht es rot aus, aber das sieht man natür­lich nicht."
      ],
      [
        "In diesem, was man da rot sehen würde, steckt erstens alles das drin, was erlebt werden kann zwischen dem Tod und einer neuen Geburt, zweitens alles das, was beschrieben ist in der «Geheimwissen-schaft im Umriß» als Saturn-, Sonnen-, Monden-, Erdenentwickelung und so weiter.",
        "Dasjenige liegt da aufgespeichert, was eben verborgen ist für die sinnenfällige Anschauung."
      ],
      [
        "Das ist da auf der andern Seite der Kugel.",
        "Aber ein kleines Stück sehen Sie davon; das kann ich nur so zeichnen, daß ich jetzt sage: Nehmen Sie dieses kleine Stück von dem Roten, das ginge da herüber (siehe Zeichnung, unten) und durch­kreuzt sich mit dem Blauen, so daß das Blaue, statt daß es jetzt vorne ist, dahinter ist."
      ],
      [
        "Ich müßte eigentlich hier vierdimensional zeichnen, wenn ich es wirklich zeichnen würde, ich kann es daher nur ganz schematisch zeichnen.",
        "Also da (links) sind die Sinne jetzt hier dem Blauen zugewendet; da sind sie nicht zugewendet dem Blauen, son­dern dem Roten, das Sie sonst nicht sehen."
      ],
      [
        "Aber hinter dem Rot hat sich jetzt gekreuzt das, was sonst gesehen wird, und das ist jetzt dar­unter.",
        "Und dieses kleine Stück, das da sich kreuzt mit dem andern, das sehen Sie fortwährend im gewöhnlichen Bewußtsein."
      ],
      [
        "Das sind näm­lich Ihre aufgespeicherten Erinnerungen.",
        "Alles, was als Erinnerung entsteht, entsteht nicht nach Gesetzen dieser äußeren Wahrnehmungs-weit, sondern es entsteht nach den Gesetzen, die dieser hinteren Welt da entsprechen."
      ],
      [
        "Dieses Innere, das Sie als Ihre Erinnerungen haben, das entspricht wirklich dem, was da auf der andern Seite ist (rechts).",
        "In­dem Sie in sich hineinblicken, in alles das, was Ihre Erinnerungen sind, sehen Sie tatsächlich die Welt auf einem Stück von der andern Seite; da ragt das andere ein wenig herein, da sehen Sie die Welt von der andern Seite."
      ],
      [
        "Und wenn Sie jetzt durch Ihre Erinnerungen, wie sie so aufgeschrieben sind, durchschlüpfen könnten - ich habe vor"
      ],
      [
        "acht Tagen davon gesprochen -, wenn Sie da hinunter könnten, unter Ihre Erinnerungen sehen und sie von der andern Seite anschauen könnten, von da drüben (siehe Zeichnung, rechts), da würden Sie die Erinnerungen als Ihre Aura sehen.",
        "Da würden Sie den Menschen sehen als ein geistig-seelisches aurisches Wesen, wie Sie sonst die äußere Welt sinnenfällig in den Wahrnehmungen sehen.",
        "Nur wäre es eben­sowenig angenehm - wie ich das vor acht Tagen hier charakterisiert habe -, weil da der Mensch noch nicht schön ist von dieser andern Seite."
      ],
      [
        "Also das ist das Interessante, was man kreuzen muß mit dem an­dern Verständnis des dreigliedrigen Menschen.",
        "Diese Kreuzung hier, die liegt nun im mittleren Menschen, im Brustmenschen.",
        "Sie erinnern sich an die Zeichnung, die ich vor acht Tagen gemacht habe, wo ich ja die in sich gewundenen Lemniskaten mit den zurückgeschiagenen Schleifen hatte: die müßte ich hier zeichnen.",
        "Hier müßte ich diesen Brustmenschen zeichnen mit den zurückgeschiagenen Lemniskaten (siehe Zeichnung Seite 85, links unten): Das würde zusammenfallen mit der Erinnerungssphäre.",
        "So daß dieser dreigliedrige Mensch hier in seinem mittleren Teil diese Umwendung des Menschen hat, wo das Innere äußerlich und das Äußere innerlich wird, wo Sie ein Tableau, das Sie sonst als Welttableau, als die große Welterinnerung sehen würden, nun als Ihre eigene kleine mikrokosmische Erinnerung sehen.",
        "Sie sehen in Ihrem gewöhnlichen Bewußtsein dasjenige, was sich zugetragen hat von Ihrem dritten Jahre an bis jetzt: das ist eine innere Aufzeichnung, ein kleines Stück für das, was gleichartig mit dem ist, was sonst Aufzeichnung für die ganze Weltenevolution ist, was auf der andern Seite liegt."
      ],
      [
        "Nicht ohne Grund habe ich seinerzeit, wie den meisten von Ihnen wohl bekannt sein wird, davon gesprochen - und ich habe es ja wieder­um ausgeführt in meinem letzten Buche «Von Seelenrätseln» am Schluß in der Anmerkung -, nicht ohne Grund habe ich davon ge­sprochen, daß der Mensch eigentlich zwölf Sinne hat.",
        "Diese Sinne müssen wir uns so denken, daß eine Anzahl von diesen zwölf Sinnen nach dem Sinnenfälligen zugewendet sind, eine andere Anzahl von diesen zwölf Sinnen sind aber nach rückwärts gerichtet.",
        "Sie sind auch"
      ],
      [
        "da unten (siehe Zeichnung Seite 85) nach dem gerichtet, was schon das Gewendete ist.",
        "Und zwar sind nach dem äußeren Sinnenfaliigen gerichtet: Ichsinn, Denksinn, Sprachsinn, Hörsinn, Sehsinn, Ge­schmackssinn, Geruchssinn.",
        "Diese Sinne sind gerichtet nach dem Sinnenfälligen.",
        "Die andern Sinne kommen ja eigentlich dem Men­schen deshalb nicht zum Bewußtsein, weil sie zunächst nach seinem eigenen Inneren und dann nach dem Umgekehrten der Welt gerichtet sind.",
        "Das sind vorzugsweise: Wärmesinn, Lebenssinn, Gleichge­wichts sinn, Bewegungssinn, Tastsinn.",
        "So daß wir sagen können: Für das gewöhnliche Bewußtsein liegen sieben Sinne im Hellen (oben) und fünf Sinne im Dunkeln (unten).",
        "Und diese fünf Sinne, die im Dunkeln liegen, die sind der andern Seite der Welt zugewendet, auch im Menschen der andern Seite (siehe Zeichnung Seite 85)."
      ],
      [
        "Sie können daher einen vollständigen Parallelismus haben zwischen den Sinnen und zwischen etwas anderem, wovon wir gleich sprechen werden (siehe Zeichnung, Kreis).",
        "Also nehmen wir an, wir hätten als Sinne zu verzeichnen den Hörsinn, den Sprachsinn, den Denksinn, den Ichsinn, den Wärmesinn, den Lebenssinn, den Gleichgewichts­sinn, den Bewegungssinn, den Tastsinn, den Geruchssinn, den Ge­schmackssinn, den Sehsinn, so haben Sie im wesentlichen alles das­jenige, was vom Ichsinn geht bis zum Geruchssinn, im Hellen liegend, in dem, was dem gewöhnlichen Bewußtsein zugänglich ist (siehe Zeichnung, schraffiert).",
        "Und alles dasjenige, was abgewendet ist vom gewöhnlichen Bewußtsein, so wie die Nacht vom Tag abgekehrt ist, das gehört den andern Sinnen an."
      ],
      [
        "Es ist natürlich die Grenze auch wiederum nur schematisiert; es fällt etwas ineinander; es sind die Wirklichkeiten nicht so bequem.",
        "Aber diese Gliederung des Menschen nach den Sinnen ist so, daß Sie schon im Schema an die Stelle der Sinne nur zu zeichnen brauchen die Himmelszeichen, so haben Sie: Widder, Stier, Zwillinge, Krebs, Löwe, Jungfrau, Waage - sieben Himmelszeichen für die helle Seite; fünf für die dunkle Seite: Skorpion, Schütze, Steinbock, Wassermann, Fische: Tag, Nacht; Nacht, Tag.",
        "Und Sie haben einen vollständigen Parallelismus zwischen dem mikrokosmischen Menschen - dem, was zugewendet ist seinen Sinnen, und dem, was abgewendet ist, aber"
      ],
      [
        "# Bild s. 89"
      ],
      [
        "eigentlich zugewendet ist seinen unteren Sinnen - und zwischen dem, was im äußeren Kosmos den Wechsel bedeutet von Tag und Nacht.",
        "Es geht gewissermaßen im Menschen dasselbe vor, was im Weltenge­bäude vorgeht.",
        "Im Weltengebäude wechseln Tag und Nacht, im Menschen wechselt auch Tag und Nacht, nänllich Wachen und Schlafen, wenn sich auch beide voneinander emanzipiert haben für den gegenwärtigen Bewußtseinszyklus des Menschen.",
        "Während des Tages ist der Mensch zugewendet den Tagessinnen; wir können ebensogut sagen: Widder, Stier, Zwillinge, Krebs, Lowe, Jungfrau, Waage, wie wir sagen könnten: Ichsinn, Denksinn, Sprachsinn und so weiter.",
        "Sie können jedes Ich eines andern Menschen sehen, Sie können die Gedanken des andern Menschen verstehen, Sie können hören, sehen, schmecken, riechen: das sind die Tagessinne.",
        "In der Nacht ist der Mensch so, wie sonst die Erde nach der andern Seite ge­wendet ist, den andern Sinnen zugewendet, nur sind diese noch nicht"
      ],
      [
        "vollentwickelt.",
        "Sie werden erst nach der Venuszeit so voll entwickelt sein, daß sie wahrnehmen können, was da nach der andern Seite ist.",
        "Sie sind noch nicht so voll entwickelt, daß sie das wahrnehmen kön­nen, was da nach der andern Seite ist.",
        "Sie sind in Nacht gehüllt, wie beim Durchgang durch die andern Himmelsregionen, die andern Bilder des Tierkreises, die Erde in der Nacht ist.",
        "Das Durchschreiten des Menschen durch seine Sinne ist ganz zu parallelisieren mit dem Gang - ob Sie nun sagen der Sonne um die Erde oder der Erde um die Sonne, das ist ja schließlich für diesen Zweck gleichgültig; aber diese Dinge hängen zusammen.",
        "Und diese Zusammenhänge kannten die Weisen der alten Mysterien sehr gut."
      ],
      [
        "Das verschwand für das Bewußtsein eben allmählich in der vierten nachatlantischen Zeit, aber es muß wieder heraufgeholt werden, muß auch gegen die Widerstände, die sich dagegen erheben, wiederum heraufgeholt werden für die Menschheitskultur.",
        "Denn in den Be­griffen, die man sich da aneignet, liegt dasjenige, was einem auch ver­ständlich erscheinen läßt, was nun im sozialen, im geschichtlichen Leben vor sich geht.",
        "Solange Sie Naturleben und geistiges Leben in der Art trennen, wie das die moderne Menschheit heute liebt, so lange kommen Sie nicht zu solchen Begriffen, die im geschichtlichen Werden eine Rolle spielen könnten, sondern Sie werden überwältigt von den Begriffen, die im geschichtlichen Leben eine Rolle spielen.",
        "Überwältigt werden Sie.",
        "Dafür gibt es ja viele Beispiele."
      ],
      [
        "Nicht wahr, die Menschen haben seit, nun, sagen wir zweihundert Jahren, wie sie glauben, furchtbar viel gedacht.",
        "Man kann zusammen­stellen, was die Menschen seit zweihundert Jahren gedacht haben, was sie an Idealen ausgebildet haben, wovon sie als den großen Idealen gesprochen haben und immer wieder sprechen: von dem Ideal der Aufklärungszeit bis jetzt zu dem Ideal des großen Cäsar-Ersatzes Woodrow Wilson.",
        "All dasjenige, was da über die verschiedenen Ideale ge­sprochen worden ist, das haben die Menschen durch die Jahrhunderte, durch zwei Jahrhunderte hindurch gedacht; das bildete die Gedanken der Menschen.",
        "Aber die Weltgeschichte ist wenig bewegt worden von diesen Gedanken.",
        "Die Weltgeschichte ist von etwas ganz anderem be­wegt worden: von jenen Gedanken, die in den Dingen gewirkt und gewebt"
      ],
      [
        "haben.",
        "Und niemals waren eigentlich die Gedanken, die in den Menschenköpfen wimmeln, weiter entfernt von den großen kosmi­schen Gedanken, die in den Dingen leben, als in unserer Zeit.",
        "Das­jenige, was seit, man kann sagen, hundertfünfzig Jahren die Menschen dazu getrieben hat, eine gewisse Gestaltung der Welt zu bewirken, das sind nicht die Gedanken von Freiheit, Gleichheit, Brüderlichkeit, Gerechtigkeit und so weiter, sondern das sind die Gedanken, welche verwoben waren zum Beispiel mit dem Aufkommen des mechanischen Webstuhls."
      ],
      [
        "Daß der mechanische Webstuhl hereingekommen ist in die moderne Entwickelung in der zweiten Hälfte des 18.",
        "Jahrhunderts, daß sich diese bedeutsame Erfindung des mechanischen Webstuhls an die Stelle der alten Handweberei hineingefunden hat in die Mensch­heitsentwickelung, und daß von diesem mechanischen Webstuhl die ganze Maschinenkultur der neueren Zeit ausgegangen ist, darinnen weben die objektiven Gedanken, die wirklichen Gedanken, welche der Welt die Gestaltung gegeben haben, die sie bis heute hat, und aus der das gegenwärtige katastrophale Chaos entstanden ist."
      ],
      [
        "Man muß nicht, wenn man eine Geschichte schreiben will des gegenwärtigen katastrophalen Chaos, an die Gedanken, die in dem Menschenbewußt-sein gewimmelt haben, sich wenden, sondern an diese objektiven Ge­danken von der Begründung, von der Erfindung des mechanischen Webstuhls bis zu dem Werden der Großindustrie und ihres Schattens, des Sozialismus.",
        "Denn wenn das auch scheinbare Gegensätze sind, Großindustrie und Sozialismus, so sind sie polarische Gegensätze, die zueinander gehören, sie sind nicht voneinander zu trennen."
      ],
      [
        "Bei die­sen objektiven Gedanken muß man anfragen und das geschichtliche Werden betrachten."
      ],
      [
        "Da findet man dann, daß die Menschen sich vielen Illusionen hinge­geben haben in der Zeit des 18.",
        "Jahrhunderts, das 19.",
        "Jahrhundert hindurch, und namentlich in dem Teil des 20.",
        "Jahrhunderts, in dem wir jetzt leben.",
        "Sie haben sich vielen Illusionen hingegeben in ihren Gedanken; aber überwältigt sind sie worden von den objektiven, historisch-kosmischen Gedanken.",
        "Die weben in den Dingen.",
        "Und ein Interesse für diese objektiv webenden Gedanken, wenn auch ein furchtbar einseitiges Interesse, haben eigentlich doch nur diejenigen"
      ],
      [
        "Menschen allmählich entwickelt, welche den Sozialismus als Welt­anschauung ausgebildet haben.",
        "Und das ist etwas ungeheuer Charak­teristisches.",
        "Wenn Sie das 19.",
        "Jahrhundert verfolgen: das Bourgeois­tum verliert immer mehr und mehr das Interesse für große Weltan­schauungsfragen."
      ],
      [
        "Große Weltanschauungsfragen werden sogar dem Bourgeoistum höchst unangenehm, sie werden womöglich in die Ästhetik hinein abgeschoben.",
        "Ob es geistige Wesen gibt oder nicht, darüber mag man, wenn man ein richtiger Durchschnittsbourgeois ist, von der Bühne herunter allerlei vernehmen, wo man nicht daran zu glauben braucht, wo es nicht darauf ankommt, ob die Dinge Wahr­heiten sind oder nicht: da läßt man sich von Björnson und ähnlichen Leuten das Mannigfaltigste vormachen."
      ],
      [
        "So in das Ästhetische hinein, in das Spielen mit allerlei sogenannten Künstlerischem, dahin wird das Weltanschauungsgemäße für das Bourgeoistum in der neueren Zeit abgeschoben.",
        "Wirklich für Weltanschauungsfragen die Köpfe gegen­seitig zerschlagen - womit ich das nicht als ein Ideal betrachten will im physischen Sinne, aber im geistigen Sinne ist es in gewissem Sinne ein Ideal: Sie wissen, ich habe mit einem seht starken Aplomb darauf hingewiesen, daß ich gerne Temperament haben würde auch beim Vertreten anthroposophischer Wahrheiten -, die Köpfe eingeschiagen hat man sich in den letzten Jahrzehnten auf sozialistischem Gebiete."
      ],
      [
        "Und darum haben sich die andern nicht gekümmert.",
        "Sie haben, möchte ich sagen, diejenigen Leute allein gelassen, welche die Welt eigentlich von einem sehr engen Aspekt aus gesehen haben, welche die Welt nur gesehen haben von dem Aspekt der Fabrik aus, von dem Inneren der Fabrik aus, von dem Inneren der Buchdruckerwerkstätte und so weiter."
      ],
      [
        "Und es ist ja im höchsten Maße interessant, was für eine sogenannte Weltanschauung herausgekommen ist von dem Aspekte der Fabrik aus: denn das ist der Sozialismus!",
        "Das ist vom Aspekt des Inneren der Fabrik, das ist vom Aspekt der Menschen aus, die gar nichts anderes kennen als das Innere der Fabrik."
      ],
      [
        "Und für das, was da sich heranentwickelte, hat sich das Bourgeoistum, das sich mit allerlei abstrakten Ideen, aber auch im Abstrakten mit Ästhetisieren befaßt, so daß man nicht sehr sich die Köpfe zu zerschlagen brauchte, für das, was da unten sich entwickelt hat, hat sich das Bourgeoistum"
      ],
      [
        "eigentlich wenig interessiert.",
        "Und so ist das Bourgeoistum kurioser­weise in die Mitte hineingekommen zwischen der absterbenden, der ganz absterbenden alten Weltanschauung, die alles Geistige verloren hat, die alle großen Fragen überhaupt in den Ästhetizismus hinein abschieben möchte, und dem, was da neu heraufkommt, dem Sozialis­mus, der überhaupt noch keine Begriffe hat, der noch lediglich mit Worten allerlei Systeme bereitet, weil er die Welt überhaupt noch nicht sehen kann, sondern nur die Fabrik sehen kann, nur das alleräußerste Mechanische sehen kann.",
        "Denken Sie sich doch, was es eigentlich zu bedeuten hat, wenn der Mensch innerlich nichts weiß von Mineral-reich, Pflanzenreich und Tierreich, sondern nur weiß von der Art und Weise, wie in der Maschine mechanisch sich dieser oder jener Zapfen auf und ab bewegt, das oder jenes zugefeilt und zugehobelt wird und dergleichen!",
        "Der Sozialismus ist eine Weltanschauung, die da fußt auf der Anschauung einer Welt, die rein mechanisch ist.",
        "Es ist für den Sozialisten das Stück der Welt herausgeschnitten, das mechanisch ist; danach formt er sich seine Begriffe."
      ],
      [
        "Das hat man entstehen lassen, weil man das Prinzip hatte, sich eigentlich nur ästhetisch um die Dinge zu bekümmern.",
        "Als die Theo­sophische Gesellschaft zuerst begründet worden ist, hat man ja auch ihren Hauptgrundsatz gesehen in der Liebe aller Menschen unterein­ander.",
        "Wieviel ist darüber deklamiert worden!",
        "Nun, ich habe mich ja über diesen Punkt genügend ausgesprochen.",
        "Er ist ebenso bequem wie unfruchtbar.",
        "Aber er rührt auch davon her, daß man möglichst abschieben will dasjenige, was wirklich konkreten Inhalt hat, in das Inhaltlose hinein.",
        "Und so konnte man auch nicht ein eigentliches Interesse fassen für den wirklichen Hergang der Dinge.",
        "Einzelnen Menschen fiel das Absonderliche herkömmlicher, sagen wir Ge­schichtsbetrachtung auf.",
        "Nehmen wir einen Fall."
      ],
      [
        "Nehmen Sie eine beliebte Darstellung der römischen Kaiserzeit; versuchen Sie in den Schulbüchern oder in den Büchern auch, die die großen autoritativen Historiker geschrieben haben, über die rö­mische Kaiserzeit sich zu unterrichten.",
        "Ich glaube, Sie werden aus diesen Darstellungen außerordentlich wenig vernehmen über eine gewisse Persönlichkeit, die schon unter Nero eine bedeutende politische"
      ],
      [
        "Rolle gespielt hat - so unter Nero kommen bereits die politi­schen Aspirationen durch -, dann ganz besonderes Aufsehen erregte und bedeutenden Einfluß auf die Politik Roms erlangte unter Ves­pasian und Titus, so daß man sagen kann, daß diese Persönlichkeit die Seele der Regierung des Vespasianus und Titus war.",
        "Dann wendete sich diese Persönlichkeit der andern Seite zu unter der Regierung des Domitianus, den sie für einen Schädling des Römertums hielt."
      ],
      [
        "Sie wendete sich der andern Seite zu.",
        "Es wird ihr der Prozeß gemacht, ein sehr aufsehenerregender Prozeß in Rom, der sehr interessant ver­laufen ist, in welchem Domitianus geradezu umgeschlagen hat vom Tyrannen zu einem, der sich gegenüber diesem Prozeß nicht zu helfen wußte, daher den Mann nicht verurteilen konnte."
      ],
      [
        "Dann wiederum, als an Stelle des Domitianus Nerva kam, sehen wir diese Persönlich­keit wieder energisch verbunden mit dem Kaiser, dem Cäsar.",
        "Da sehen wir aber diese Persönlichkeit große Politik machen aus der gesamten Weltanschauung der damaligen Zeit heraus, und wir sehen zu gleicher Zeit diese Persönlichkeit versuchen, wirklich weitgehende, aus dem Kosmos heruntergeholte Begriffe noch einmal, zum letzten Male während der römischen Kaiserzeit, den politischen Ereignissen ein­zuimpfen."
      ],
      [
        "Und kurioserweise finden Sie ja eine richtige Beschreibung dieser Persönlichkeit in gar keinem gebräuchlichen Geschichtsbuche, nicht einmal bei Sueton und Tacitus> sondern nur bei Philostratus.",
        "Und Philostratus schildert auch nur so, daß man nicht wußte, schildert er einen Roman oder eine Wirklichkeit."
      ],
      [
        "Er schildert das Leben des Apollonius von Tyana.",
        "Denn Apollonius von Tyana ist der, von dem ich Ihnen gesagt habe, daß er von Nero an bis zu Nerva und nament­lich unter Vespasian und Titus einen so großen Einfluß auf die Politik hatte, und den Philostratus beschrieb."
      ],
      [
        "Und der Tübinger Theologe Baur, der Historiker Baur war im höchsten Grade erstaunt, daß man so gar nichts findet über eine Persönlichkeit wie den Apollonius, der eine erste Rolle spielen müßte in der Geschichtsdarstellung.",
        "Natür­lich sah Baur nicht ein, worauf es ankommt."
      ],
      [
        "Es kommt darauf an, daß in Apollonius eine Persönlichkeit dasteht in der Geschichte, die schon diesen großen Einfluß hatte, aber die aus dem überragenden Kosmischen die Prinzipien herunterholte.",
        "Das war dem ins Römische"
      ],
      [
        "hineinmündenden Christentum im höchsten Grade fatal.",
        "Und nun bitte ich Sie zu berücksichtigen, daß alles dasjenige, was historisch da ist, von der Kirche Gnaden da ist.",
        "Es ist ja sonst nichts da, als was die Kirche aus Gnade den Menschen gelassen hat.",
        "Nicht mit Unrecht hat ein alter, gar nicht dummer Mensch behauptet, daß es überhaupt einen Plato, einen Sophokles gar nicht gegeben hatte, sondern daß Mönche vom 14. und 15.",
        "Jahrhundert des Sophokles' Dramen ge­schrieben hatten; denn ein strikter Beweis dafür, daß Sophokles ge­lebt hat, ist nicht da.",
        "Wenn auch die Behauptung nicht haltbar ist, selbstverständlich Unsinn ist, aber wie unsicher alles dasjenige ist, was geschichtliche Fable convenue ist, wir haben es ja schon oft be­tont.",
        "Und wir müssen uns darüber klar sein.",
        "Wir müssen ja die Gegen­wart mit der Vergangenheit in Zusammenhang bringen, denn wir nähern uns jetzt einer großen, bedeutungsvollen Frage."
      ],
      [
        "Wir haben wiederum, vom modernen Standpunkte jetzt, hinge­wiesen auf den dreigeteilten Menschen, auf diesen Zusammenhang mit kosmischen Wahrheiten, auf die Notwendigkeit, daß das wieder ent­hüllt werde.",
        "Ja, worin bestand denn eigentlich die Haupttätigkeit der Kirche, namentlich seit dem achten ökumenischen Konzil in Konstan­tinopel, das 869 stattfand?",
        "Sie bestand darinnen, auszulöschen, aus­zutilgen vom menschlichen Bewußtsein dasjenige, was in jenen alten Zeiten auch das Christentum an Verständnis für den Zusammenhang des Menschen mit dem Kosmos, mit der großen geistigen Welt hatte.",
        "Mit einer wahren Ängstlichkeit hat man alles dasjenige beseitigt, was diesen Zusammenhang verrät.",
        "Und nur, weil nicht alles beseitigt werden kann, weil das Karma dem schon entgegenwirkt, sind solche Werke wie das des Philostratus geblieben.",
        "Und daher können Sie es begreifen, wenn Sie jetzt die Vergangenheit mit der Gegenwart zu­sammenbringen, daß gewisse Menschen von kirchlicher Seite heil­lose Angst bekommen, wenn in der Gegenwart wiederum die An­knüpfung gepflogen werden soll zwischen dem, was den Menschen zu einem Wesen des Kosmos macht, und diesem Menschen selber und seiner Aufgabe."
      ],
      [
        "Es geht eben nicht an, daß man nur schläfrig dasjenige verfolgt, was durch die anthroposophische Bewegung gewollt sein sollte."
      ],
      [
        "muß es in lebendigem, kraftvollem Bewußtsein verfolgen.",
        "Das ist schon notwendig.",
        "Damit habe ich hingewiesen auf dasjenige, was wir nun weiter ausführen wollen.",
        "Morgen werde ich den Vortrag hier halten, in dem ich diese Betrachtungen fortsetzen werde."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SECHSTER VORTRAG Dornach, 26. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Gewisse Fragen werden dem denkenden Menschen sich doch immer wieder und wiederum aufdrängen, wenn er auch in Zeiten, in denen die materialistische Kultur überwiegt, diesen Fragen mehr oder we­niger aus dem Wege gehen möchte. Es sind viele Fragen. Ich möchte heute ein paar aus der großen Reihe der Fragen herausheben, die da­von kommen, daß der Mensch doch, selbst wenn er sich sträubt, eine geistige Welt anzuerkennen, den Eindruck dieser geistigen Welt ver­spürt. Zu solchen Fragen gehört zum Beispiel diese, die ja, man möchte sagen, das Leben alltäglich aufwirft: Gewisse Menschen sterben jung, andere sterben ganz alt, andere dazwischen. Gegenüber dieser Tatsache, daß auf der einen Seite ganz junge Kinder sterben, auf der andern Seite Leute ganz alt werden und dann sterben, erheben sich für den Menschen Fragen, welche mit den Mitteln, die man heute wissenschaftliche Mittel nennt, niemals - bei klarer Besinnung wird das jeder zugeben müssen - werden zu beantworten sein. Und doch sind sie für das Menschenleben brennende Fragen, und jeder kann eigentlich empfinden, daß sich für das Leben Unendliches aufklären müßte dadurch, daß man diesen Fragen nahetreten könnte: Warum sterben Menschen zuweilen früher, im Kindesalter, im Jugendalter, in der Mitte der gewöhnlichen Lebenszeit? Warum sterben andere alt? Was hat das für eine Bedeutung im gesamten Weltenall?",
      "Sich solche Fragen zu beantworten, dazu hatten die Menschen bis zu jenem Zeitpunkte, den ich Ihnen in diesen Betrachtungen schon angegeben habe, bis zu dem Zeitpunkt der beginnenden vierten nach-atlantischen Zeit, so ungefähr bis in die Mitte des 8. vorchristlichen Jahrhunderts, noch Vorstellungen, Begriffe. Aus alter Weisheit her­überbekommen hatten sie Begriffe. Es gab auch in jenen alten Zeiten, die dem 8. vorchristlichen Jahrhundert vorangingen, über die da­malige Erdenkultur verbreitet überall Vorstellungen, welche nach dem Sinn der damaligen Zeit den Menschen Aufschluß gaben über solche Fragen wie die eben angedeuteten. Dasjenige, was wir heute",
      "Wissenschaft nennen, kann nicht einmal einen rechten Sinn verbinden mit solchen Fragen, kommt gar nicht darauf, daß etwas mit diesen Fragen gegeben ist, wozu man irgendeine Antwort suchen sollte. Das alles rührt davon her, daß in der Zeit, die seit dem eben angedeuteten Zeitpunkte verflossen ist, eigentlich alle Vorstellungen verlorenge­gangen sind, die sich auf den geistigen und damit auf den ewigen Menschen beziehen. Es sind nur diejenigen Vorstellungen geblieben, die sich auf den vergänglichen Menschen und den zwischen Geburt und Tod eingeschlossenen Menschen beziehen.",
      "Ich habe darauf aufmerksam gemacht, daß in allen alten Weltan­schauungen von einer dreifachen Sonne gesprochen wurde, von jener Sonne, die man mit den physischen Sinnen wahrnimmt als eine leuchtende Kugel im Weltenraume draußen. Hinter dieser Sonne aber sahen die alten Weisen die seelische Sonne - im griechischen Sinne gesprochen, den Helios - und erst hinter dieser seelischen Sonne die geistige Sonne, die zum Beispiel noch Plato identifizierte mit dem Guten.",
      "Es hat für den heutigen Menschen eigentlich keinen rechten Sinn, von dem Helios, der seelischen Sonne, oder gar von der geisti­gen Sonne, von dem Guten, zu sprechen. Aber so wie uns hier zwi­schen Geburt und Tod die physische Sonne leuchtet, so scheint, wenn ich sagen darf, in unser Ich hinein in der Zeit, die wir verbringen zwischen dem Tod und einer neuen Geburt, die geistige Sonne, die eben noch von Plato identifiziert wird mit dem Guten.",
      "Für die Zeit zwischen dem Tod und einer neuen Geburt von dieser leuchtenden Kugel zu sprechen, von der unsere heutige materialistische Weltan­schauung spricht, hat keinen Sinn; zwischen dem Tod und einer neuen Geburt hat nur Sinn zu sprechen von der geistigen Sonne, von dem, was Plato noch als das Gute bezeichnet. Aber gerade ein solcher Be­griff sollte uns auf etwas hinweisen.",
      "Er sollte uns darauf hinweisen, nachzudenken, wie es sich eigentlich verhält mit dem, was wir uns als physische Vorstellung von der Welt bilden. Daß wir in dem, was wir uns als physische Vorstellungen von der Welt bilden, in dem, was sinnenfällig vor uns ausgebreitet ist, zu sehen haben eine Art von Täuschung, eine Art von Maja, das wird doch nicht im vollen Sinne des Wortes ernst genommen, wenigstens nicht so ernst, daß die Anschauung",
      "des Lebens wirklich mit diesen Dingen durchdrungen würde.",
      "So eine Art Vorstellung von der Sonne hat im Grunde derjenige, der die heutige Physik, Astrophysik meinetwillen, autoritativ nimmt: Wenn er da hinauffahren könnte, wohin die Physiker die Sonne ver­setzen, so würde er, indem er sich der Sonne nähert - nun, sehen wir jetzt von menschlichen Lebensbedingungen ab, setzen wir voraus, daß die Lebensbedingungen absolut sein könnten -, gewaltige Hitze ver­spüren, so stellt er es sich vor, und er würde da, wenn er innerhalb des Raumes ankommt, den sich der Physiker von der Sonne ausge­füllt denkt, innerhalb dieses Raumes glühendes Gas oder dergleichen finden. So stellt sich der Physiker ja das eigentlich vor: einen glühen­den Gasball oder so etwas.",
      "Aber so ist es nicht, das ist eine richtige Maja, eine richtige Täuschung. Und diese Vorstellung hält vor den wahren physikalischen Anschauungen, die man gewinnen kann, auch nicht stand, geschweige denn vor der wirklichen übersinnlichen An­schauung.",
      "Wenn man sich nämlich wirklich der Sonne nähern könnte und dahin kommen würde, wo die Sonne ist - ja, indem man sich nähert, da findet man schon so etwas, wie wenn man durch flutendes Licht durchgehen müßte (es wird gezeichnet: gelber Kreis, innen blauer Kern); aber wenn man da hineinkommt, wo die Physiker die physische Sonne vermuten, findet man zunächst das, was man an­sprechen könnte als leeren Raum. Da ist überhaupt nichts; es ist gar nichts da, wo man die physische Sonne vermutet.",
      "Ich zeichne es schematisch (blau), weil eigentlich nichts dort ist. Da ist nichts, da ist leerer Raum. Aber ein sonderbarer leerer Raum ist das! Wenn ich sage: Es ist nichts da -, so rede ich eigentlich nicht ganz richtig; es ist weniger als nichts da.",
      "Es ist nicht nur ein leerer Raum da, sondern es ist weniger als nichts da. Und das ist es, was als eine Vorstellung für abendländische Menschen heute außerordentlich schwer zu bilden ist. Der Morgenländer hat diese Vorstellung auch heute noch ohne wei­teres; für den ist es gar nichts Wunderbares oder Schwerverständ­liches, wenn man ihm davon spricht, daß da weniger als nichts ist.",
      "Der Abendländer denkt sich, und er denkt sich das insbesondere, wenn er ein waschechter Kantianer ist, denn viel mehr Leute, als man",
      "heute denkt, sind Kantianer, sind unbewußte Kantianer: Wenn nichts im Raum ist, so ist es eben leerer Raum! - Aber das ist nicht der Fall; es kann auch ausgeschöpfter Raum sein. Wenn Sie nämlich da durch diese Sonnenkorona durchsehen würden, so würden Sie diesen leeren Raum, in den Sie da eintreten würden, höchst unbehaglich empfinden: er zerreißt Sie nämlich. Und darin zeigt er seine Wesenheit, daß er mehr ist - oder weniger ist, wie ich besser sagen kann - als ein leerer Raum. Sie brauchen ja nur die einfachsten mathematischen Begriffe zu Hilfr zu nehmen, so wird Ihnen nicht ganz unklar bleiben können, was ich da meine: leerer Raum ist weniger noch als bloß leer. Nehmen wir an, Sie besitzen irgend etwas an Vermögen. Aber es kann auch vorkommen, daß Sie alles, was Sie besitzen, ausgegeben haben, daß Sie nichts haben. Aber man kann weniger als nichts haben: man kann Schulden haben, dann hat man wirklich weniger als nichts. Man kann, wenn man von der Raumerfüllung zu immer dünnerer und dünnerer Raumerfüllung übergeht, bis zum leeren Raum kommen; man kann aber dann hinter die bloße Leerheit noch hinübergehen, wie man von dem Nichts zu den Schulden gehen kann.",
      "Das ist der größte Fehler der heutigen Weltanschauung, daß sie diese eigentümliche Art von negativer Stofflichkeit - wenn ich mich so ausdrücken darf - nicht kennt, daß sie nur die Leerheit kennt und die Erfüllung, und nicht dasjenige, was weniger ist als die Leerheit. Denn dadurch, daß das heutige Wissen, die heutige Weltanschauung das, was weniger ist als die Leerheit, nicht kennt, dadurch wird diese heutige Weltanschauung mehr oder weniger im Materialismus fest­gehalten, richtig im Materialismus festgehalten, ich möchte sagen:",
      "gebannt in den Materialismus. Denn es gibt auch im Menschen, wenn ich mich so ausdrücken darf, einen Ort, welcher leerer ist als leer; nicht in seiner Gänze, aber welcher eingelagert hat Teile, die leerer sind als leer. Im ganzen ist ja der Mensch - ich meine der physische Mensch -ein Wesen, welches einen Raum materiell ausfüllt; aber ein gewisses Glied der menschlichen Natur, von den dreien, die ich angeführt habe, hat tatsächlich etwas in sich, was sonnenähnlich ist, leerer ist als leer. Das ist - ja, Sie müssen es schon hinnehmen - der Kopf. Und gerade darauf, daß der Mensch so organisiert ist, daß sein Kopf sich immer",
      "entleeren kann und in gewissen Gliedern leerer sein kann als leer, da­durch hat dieser Kopf die Möglichkeit, das Geistige sich einzulagern. Stellen Sie sich einmal die Sache vor, wie sie eigentlich ist. Natürlich muß man die Dinge sich schematisch vorstellen; aber denken Sie sich, alles dasjenige, was materiell Ihren Kopf ausfüllt, würde ich schematisch durch das Folgende zeichnen. Das wäre schematisch Ihr Kopf (siehe Zeichnung, rot). Nun aber muß ich, wenn ich ihn vollständig zeichnen will, in diesem Kopf leere Stellen lassen. Das ist natürlich jetzt nicht so groß, aber drinnen sind leere Stellen. In diese leeren Stellen kann dasjenige hinein, was ich Ihnen den jungen Geist genannt habe in die­sen Tagen. In die leeren Stellen hinein muß der junge Geist, gewisser­maßen in seinen Strahlen, gezeichnet werden (gelb).",
      "# Bild s. 101",
      "Ja, die Materialisten sagen: Das Gehirn ist das Werkzeug des Seelen­lebens, des Denkens. - Das Umgekehrte ist wahr: Die Löcher im Gehirn, ja sogar dasjenige, was mehr ist als Löcher, oder ich könnte auch sagen, weniger ist als Löcher, was leerer ist als leer, das ist das Werkzeug des Seelenlebens. Und da, wo das Seelenleben nicht ist, wo das Seelenleben fortwährend aufstößt, wo der Raum unseres Schädels mit Gehirnmasse ausgefüllt ist, da wird nichts gedacht, da wird nichts seelisch erlebt. Wir brauchen unser physisches Gehirn nicht zum Seelenleben, sondern wir brauchen es nur, damit wir das Seelenleben einfangen, physisch einfangen. Wenn da nicht das Seelenleben, das in den Löchern des Gehirnes eigentlich lebt, überall aufstoßen würde, so",
      "würde es verfliegen; es käme uns nicht zum Bewußtsein. Aber es lebt in den Löchern des Gehirns, die leerer sind als leer.",
      "So müssen wir uns die Begriffe allmählich korrigieren. Wir nehmen, wenn wir vor dem Spiegel stehen, nicht uns wahr, sondern unser Spiegelbild. Uns können wir vergessen. Wir sehen uns im Spiegel drinnen. So erlebt der Mensch auch nicht sich, indem er durch sein Gehirn dasjenige zusammenhält, was in den Löchern des Gehirnes liegt; er erlebt, wie sich überall sein Seelenleben spiegelt, indem es an die Gehirnmasse anstößt. Es spiegelt sich überall; das erlebt der Mensch. Er erlebt eigentlich sein Spiegelbild. Das aber, was da in die Löcher hereingeschlüpft ist, das ist dasjenige, was dann, wenn der Mensch durch die Pforte des Todes geht, ohne die Widerlage des Ge­hirnes seiner selbst bewußt wird, weil es dann in entgegengesetzter Weise mit Bewußtsein durchsetzt wird.",
      "Nun will ich ein anderes Schema aufzeichnen. Nehmen Sie das Folgende. Bitte, ich will jetzt das Gehirn recht drastisch zeichnen, wie das Löcher läßt (blau). Da sei die Gehirnmasse, da lasse es die Löcher, und dahinein in diese Löcher geht das Seelenleben (gelb). Dieses Seelenleben, das setzt sich aber vor den Löchern fort. Da kommen wir in die ja natürlich nur in der Nähe des Menschen sichtbare, aber ins Unbestimmte auslaufende Menschenaura hinein.",
      "# Bild s. 102",
      "Denken wir uns jetzt das Gehirn weg, und denken wir uns, wir sehen beim gewöhniichen Menschen zwischen Geburt und Tod das",
      "Seelenleben an, dann würden wir sagen müssen: Der wahre Mensch, in dieser Weise gesehen, der ist in seinem Zustande zwischen Geburt und Tod so, daß er eigentlich - da muß ich allerdings das jetzt anders schematisch zeichnen - sein Antlitz seinem Körper so zuwendet (siehe Zeichnung Seite 105, lila); sein Seelenleben wendet er dem Körper­lichen zu. Und wenn wir auf das Gehirn sehen, so streckt dieses Seelenleben hier Fühlhörner vor, die in die Löcher des Gehirns hin­eingehen. Was ich dort (siehe Zeichnung Seite 102) gelb gezeichnet habe, zeichne ich hier lila, weil das besser dem Anblick im lebenden Menschen entspricht. Das wäre das, was sich ins Gehirn erstreckt beim lebenden Menschen.",
      "Wollte ich jetzt danach etwa den physischen Menschen zeichnen, so würde ich das am besten dadurch andeuten können, daß ich Ihnen etwa hier die Grenze, die mit dem Erinnerungsvermögen gegeben ist, hereinzeichne. Sie würde da nach außen gehen, und da würde die äußere Grenze, die Grenze des Erkennens sein, von der ich Ihnen ja auch gesprochen habe. Da brauchen Sie sich ja nur an die letzthin und gestern gemachte Zeichnung zu erinnern.",
      "Jetzt aber ist es wirklich so,daß, wenn man von außen den Men­schen geistig anschaut, sich das Seelenleben so in den Menschen hin­ein erstreckt. Ich will also das einzelne Hineinerstrecken nur in bezug auf das Gehirn zeichnen. Aber dieses Seelenleben ist in sich auch differenziert: so würde ich, wenn ich dieses Seelenleben weiter verfolgen würde, hier eine andere Region zeichnen müssen (rot unter dem Lila), hier eine andere Region (blau); das würde also alles zu der den Menschen konstituierenden Aura gehören. Dann eine andere Region (grün): Sie sehen, dieser Teil, den ich da jetzt schematisch zeichne, liegt jenseits der Grenze des menschlichen Erkennens. Dann diese Region (gelb) - im Grunde genommen gehört das alles zum Men­schen - und diese Region (orange).",
      "Das bewegt sich, wenn der Mensch einschläft, mehr oder weniger aus dem Körper heraus, sowie das gestern gezeichnet worden ist (Zeich­nung Seite 77); wenn der Mensch wachend ist, mehr oder weniger in den Körper hinein, so daß eigentlich die Aura nur in der unmittelbar­sten Umgebung des Körpers seelisch wahrzunehmen ist. Wenn man den",
      "physischen Menschen beschreibt, dann tut man es so, daß man sagt: Dieser physische Mensch besteht aus Lunge, Herz, Leber, Galle und so weiter. Das sagt der physische Anatom, der Physiologe und so weiter. Geradeso können Sie aber den geistig-seelischen Menschen be­schreiben, der in dieser Weise sich eigentlich in die Löcher des Men­schen hereinerstreckt, in das, was mehr ist als Leere, in den Menschen hineinerstreckt. Sie können das ebenso beschreiben. Da müssen Sie dann nur angeben, aus was dieser geistig-seelische Mensch besteht. Und ebenso wie man beim physischen Menschen Organe unterschei­det, so kann man hier Strömungen unterscheiden. Man kann sagen: Hier, wo ich das Rot gezeichnet habe, würde der physische Mensch so im Profil drinnenstehen, hierher das Gesicht gerichtet haben, hier etwa die Augen (siehe Zeichnung); hier würde sein die Region der Begierdenglut (rot). Das würde ein Bestandteil des seelisch-geistigen Menschen sein, der seiner Substanz nach entnommen ist der Region, die Sie aus der «Theosophle» kennen als die Region der Begierden­glut. Also Begierdenglut, gewissermaßen etwas von ihr entnommen, in den Menschen hineinversetzt, gibt diese Partie des Menschen.",
      "Das, was ich hier lila gezeichnet habe, das würde ich bezeichnen müssen, wenn ich die Einzelheiten beschriebe, mit Seelenleben. Sie wissen, eine bestimmte Partie des Seelengebietes, des Seelenlandes, ist mit «Seelenleben» bezeichnet. Die Substanz daraus würde dieses Violette, dieses Lila sein, was im Menschen einen Teil des Geistig-Seelischen bildet. Das, was ich hier als orange bezeichnet habe, würden wir zu nennen haben, wenn wir diese Benennung beibehielten, tätige Seelenkraft. So daß Sie sich vorzustellen hätten: Dasjenige, was am intensivsten durch Ihre Sinne in Sie hineingeht beim Leben zwischen Geburt und Tod, das ist das Seelenleben; und dahinter, sich auch hin­stopfend, aber nicht so hineinkönnend, aufgehalten werdend durch das Seelenleben: tätige Seelenkraft. Und noch mehr dahinter dasjenige, was man nennen kann: Seelenlicht. Ich habe es hier gelb bezeichnet. Ziemlich anschließend an dieses Seelenlicht, sich so durchdrückend, würde dann das sein, was der Region von Lust und Unlust entnom­men ist. Das würde ich hier etwa dem grünen Gebiete zuzuschreiben haben (siehe Zeichnung). Dann würde dem schon bläulich werdenden",
      "Gebiete zuzuschreiben sein: Wünsche. Und anstoßend nun hier das Blaue, schon wiederum mehr in das Blaurote hineingehend, das würde die Region ffießender Reizbarkeit sein. Das, was ich hier nenne Be­gierdenglut, fließende Reizbarkeit, Wünsche, das sind aurische Strö­mungen. Diese aurischen Strömungen konstituieren, wie Sie wissen, die Seelenwelt; sie konstituieren aber auch den seelisch-geistigen Menschen, der etwa so aufgebaut ist aus den Ingredienzien dieser Seelenwelt.",
      "# Bild s. 105",
      "Wenn dann der Tod eintritt, dann ist das so, daß der physische Leib abfällt und der Mensch das fortnimmt, was sich durch seine Löcher in ihn hineinerstreckt hat. Er nimmt es nun fort. Dadurch, daß er es fortnimmt",
      "- wir können uns diesen physischen Menschen wegdenken -, kommt nun der Mensch in eine gewisseVerwandtschaft mit der Seelen­weit, und dann auch mit dem Geisterland, wie Sie es ja in der «Theo­sophie» dargestellt finden. Er hat eine gewisse Verwandtschaft da­durch, daß er diese Ingredienzen in sich hat. Aber während des phy­sischen Lebens sind sie gebunden an den physischen Leib; dann werden sie frei. Dadurch aber, daß sie frei werden, verwandelt sich nach und nach das Ganze. Während es so war, daß sich - wenn ich jetzt die Differenzierungen weglasse und das Seelenleben so zeichne -während des physischen Lebens die Fühler (dunkel schraffiert) in un­sere Löcher hineinerstrecken, nehmen sich nach dem Tode diese Fühler zurück. Dadurch aber, daß sich die Fühler zurücknehmen, höhlt sich das Seelenleben selbst aus, und im Seelenleben drinnen geht das geistige Leben auf; von der andern Seite geht das geistige Leben auf (beIl schraffiert).",
      "# Bild s. 106",
      "In dem selben Maße, in welchem der Mensch aufhört unterzutau­chen in den physischen Leib, hellt sich auf sein Geistig-Seelisches, diese seine Aura von der andern Seite durchleuchtend. Und wie der Mensch ein Bewußtsein erlangen kann dadurch, daß beim Hinein-stoßen des Seelisch-Geistigen in den physischen Körper dieses immer anstößt und dadurch sich immer spiegelt, so bekommt der Mensch jetzt dadurch ein Bewußtsein, daß er sich zurückzieht gegen das Licht. Aber dies ist jenes Licht der Sonne, welches das erste Licht ist: das Gute. Während der Mensch also während seines physischen Lebens als geistig-seelisches Wesen gegen das Sonnenverwandte, nämlich gegen die überleeren Löcher im Gehirn stößt, stößt er, sich zurückziehend",
      "nach dem Tode, nach der andern Sonne, nach der guten Sonne, nach der ersten Sonne.",
      "Sie sehen, wie zusammenhängt mit den Grundvorstellungen der uralten Mysterien die Möglichkeit, Begriffe zu erhalten von dem Leben zwischen dem Tod und einer neuen Geburt. Denn so stecken wir drinnen in diesem ganzen kosmischen Leben, wie ich es Ihnen jetzt in diesen Tagen dargestellt habe. Aber allerdings muß man, um richtige Begriffe von diesen Dingen zu bekommen, tiefer in das eigent­liche Gefüge der menschlichen Evolution durch die Erdenzeit hin­durch eingehen. Nicht wahr, es wäre ja möglich, daß jemand durch besonderen Glücksfall, wie man das so nennen könnte, hellsichtig das Ganze, was ich jetzt dargestellt habe, schaute. Aber der Glücksfall könnte nicht weiter gehen, als daß er sich verwandelnde Gebilde schaut. Etwa so: Nehmen wir an, ein Mensch würde durch irgendein Wunder - es geschieht schon nicht durch ein Wunder -, durch irgend etwas hellsichtig, übersinnlich schauend, so würde er schon, so ähnlich, wie ich es hier versucht habe aufzuzeichnen, das geistig-seelische Leben des Menschen sehen. Daß dies etwas anders ausschaut, als was ich vor einiger Zeit als Normalaura aufgezeichnet habe, das werden Sie begreiflich finden, wenn Sie verstehen, daß ich vor einigen Tagen das aufgezeichnet habe (siehe Seite 31), was sich als Aura ergibt, wenn man den ganzen Menschen sieht, also den physischen Menschen und die Aura ringsherum; jetzt habe ich aber herausgeholt den geistig­seelischen Menschen, so daß der geistig-seelische Mensch von dem physischen Menschen abstrahiert wird.",
      "Daran sehen Sie schon, daß man einmal so, das andere Mal anders die Farben setzen muß; daran sehen Sie auch, daß für das übersinn­liche Bewußtsein die Dinge sehr verschieden ausschauen. Nehmen Sie sich vor, die Aura des Menschen einfach so zu sehen, wie sie ist, indem der Mensch den physischen Leib hat, dann sehen Sie diese Aura - also wenn Sie sich vornehmen, abgesehen vom geistig-seelischen Men­schen jetzt den Menschen zu sehen, der nur seine Organe vorstreckt in den physischen Menschen hinein. Aber wenn Sie nun den Men­schen in der Zeit zwischen dem Tod und einer neuen Geburt sehen, da sehen Sie wiederum, wie sich das Ganze verwandelt. Da geht also",
      "vor allen Dingen diese Region, die ich hier rot gezeichnet habe, weg von hier, geht hier herauf, das Gelbe geht hier herunter, das Ganze kommt nach und nach durcheinander. Man kann solche Dinge an­schauen, aber das Anschauen hat etwas Verwirrendes. Und daher werden sich auch für den neueren Menschen nicht leicht Möglich­keiten finden, Sinn und Bedeutung in dieses Verwirrende hineinzu­bringen, wenn er nicht zu andern Hilfsmitteln seine Zuflucht nimmt.",
      "Wir haben hingewiesen daranf, daß das Haupt des Menschen, der Kopf, auf die Vergangenheit weist, der Extremitätenmensch auf die Zukunft weist. Es ist ein vollständiger Gegensatz, polarisch; beides, das Haupt des Menschen und der Extremitätenmensch - erinnern Sie sich nur an dasjenige, was ich gestern auseinandergesetzt habe -, beide sind eigentlich ein und dasselbe; nur daß das Haupt eben eine sehr alte Bildung ist, eine Überbildung. Daher hat es auch die Löcher. Der Extremitätenmensch hat diese Löcher noch nicht; der ist eben noch ganz von Materie ausgefüllt. Löcher kriegen, das ist ein Zeichen von Überentwickelung. Rückgängige Entwickelung im Haupte sehen können, darauf kommt viel an. Und viel kommt darauf an, daß man verstehen kann: der Extremitätenmensch ist eine junge Metamor­phose, das Haupt ist eine alte Metamorphose. Und weil der Extremi­tätenmensch eine junge Metamorphose ist, kann er noch nicht hier im physischen Leben denken, sondern es bleibt sein Bewußtsein unbe­wußt. Er öffnet nicht dem geistig-seelischen Menschen solche Löcher wie das Gehirn.",
      "Das ist von unendlicher Wichtigkeit und wird in Zukunft immer wichtiger und wichtiger werden für die Geistes kultur: einzusehen so etwas, daß zwei Dinge, die äußerlich physisch ganz voneinander ver­schieden sind wie der Kopfmensch und der Extremitätenmensch, geistig-seelisch ein und dasselbe sind, nur der Zeit nach auf verschie­denen Entwickelungsstufen. Viele Geheimnisse liegen gerade in die­ser Tatsache, daß zwei physisch verschiedene Dinge dadurch, daß sie auf zeitlich verschiedenen Entwickelungsstufen stehen, eigentlich ein und dasselbe sein können. Sie sind äußerlich physisch etwas ganz Verschiedenes, aber Verwandlungszustände, also Metamorphosen eines und desselben.",
      "In elementarer Weise hat den Anfang mit Begriffen, durch die man so etwas erfassen kann, eben Goethe gemacht mit seiner Metamor­phosenlehre. Während sonst eigentlich in der Ausbildung der Be­griffe ein Stillstand ist seit alten Zeiten, setzt bei Goethe wiederum die Fähigkeit ein, Begriffe zu bilden.",
      "Und diese Begriffe sind die lebendi­gen Metamorphosenbegriffe. Goethe hat allerdings angefangen mit dem Einfachsten. Er hat gesagt: Wenn wir eine Pflanze anschauen, so haben wir das grüne Pflanzenblatt, aber das verwandelt sich dann in das farbige Blumenblatt.",
      "Beides ist ein und dasselbe, es sind nur Metamorphosen voneinander. - So wie das grüne Pflanzenblatt und das rote Rosenblatt verschiedene Metamorphosen sind, ein und das­selbe auf verscHedenen Stufen, so sind das Haupt des Menschen und der Extremitätenorganismus einfach Metamorphosen voneinander. Wenn wir den Goetheschen Metamorphosengedanken für die Pflanze nehmen, haben wir etwas Primitives, Einfaches; aber es kann dieser Gedanke fruchtbar gemacht werden für ein Höchstes: für das Be­schreiben des Überganges des Menschen von einer Inkarnation in die andere.",
      "Wir sehen eine Pflanze mit grünem Blatt und mit der Blüte und sagen: Die Blüte, die rote Rosenblüte ist umgewandelt aus dem grünen Pflanzenblatt. Wir sehen einen Menschen vor uns stehen und sagen: Das Haupt, das du trägst, das sind deine umgewandelten Arme, Hände, Beine, Füße aus der vorhergehenden Inkarnation; und das, was du jetzt an dir, wie Arme, Hände, Beine, Füße trägst, das wird sich umwandeln für die nächste Inkarnation in deinen Kopf.",
      "Aber jetzt kommt ein Einwand, der Ihnen offenbar in der Seele schwer sitzt. Jetzt werden Sie sagen: Ja, um Gottes willen, aber ich lasse doch meine Beine und meine Füße zurück, und meine Arme und meine Hände auch; die nehme ich doch nicht mit in die nächste In­karnation! Wie soll denn da mein Kopf daraus werden? - Nicht wahr, das kann man einwenden. Wiederum stehen Sie eben hier vor einer Maja. Es ist nämlich nicht wahr, daß Sie wirklich Ihre Beine und Ihre Füße, Ihre Hände und Ihre Arme zurücklassen. Das ist nämlich nicht wahr; das sagen Sie deshalb, weil Sie an der Maja, an der großen Täuschung hängenbleiben. Was Sie nämlich mit dern gewöhnlichen Bewußtsein Ihre Arme und Hände, Ihre Beine und Füße nennen, das",
      "sind nicht Ihre Arme und Hände und Ihre Beine und Füße, sondern das ist dasjenige, was als Blut und andere Säfte Ihre Arme und Hände und Ihre Beine und Füße ausfüllt. Es ist hier wieder eine schwierige Vorstellung, aber es ist so.",
      "Nehmen Sie an, hier haben Sie Arme und Hände, Beine und Füße; aber das, was hier ist, ist geistig, das sind geistige Kräfte. Bitte, stellen",
      "# Bild s. 110",
      "Sie sich vor: Ihre Arme und Hände, Ihre Beine und Füße seien Kräfte, übersinnliche Kräfte. Würden Sie nur sie haben, Sie würden sie nicht mit den Augen sehen. Sie sind angefüllt, diese Kräfte sind angefüllt mit den Säften, mit dem Blute, und das, was als mineralische Masse, flüssig oder zum Teil fest, zum geringsten Teile fest, Unsichtbares ausfüllt, das sehen Sie (schraffiert). Was Sie im Grabe lassen, was ver­brannt wird, das sind nur, ich möchte sagen, die mineralischen Ein­schlüsse. Ihre Arme und Hände, Ihre Beine und Füße sind nicht sicht­bare Füße, sind Kräfte, und diese nehmen Sie mit. Die Formen neh­men Sie mit. Sie sagen: Ich habe Hände und Füße. - Derjenige, der in die geistigen Welten hineinsieht, der sagt nicht: Ich habe Hände",
      "und Füße -, sondern er sagt: Es gibt Geister der Form, Elohim, die denken kosmisch, und deren Gedanken sind meine Arme und Hände und Beine und Füße; und deren Gedanken sind mit Blut und andern Säften ausgefüllt. - Aber Blut und andere Säfte sind auch wiederum nicht das, als was sie im Physischen erscheinen; diese Stoffe sind wie­derum die Vorstellungen der Geister der Weisheit, und dasjenige, was der Physiker Stoff nennt, das ist nur der äußere Schein. Wo der Physiker den Stoff hinsetzt, müßte er sagen: Da stoße ich auf einen Gedanken der Geister der Weisheit, der Kyriotetes.",
      "Und wo Sie Arme und Hände, Beine und Füße sehen, da können Sie nicht einmal darauf stoßen, da müssen Sie sagen: Hier bilden die kosmischen Ge­danken der Geister der Form meine Formen. - Kurz, so sonderbar das klingt: Ihren Körper gibt es ja gar nicht, sondern da, wo im Raume Ihr Körper ist, da leben durcheinander die kosmischen Ge­danken der höheren Hierarchien. Und würden Sie nicht der Maja ge­mäß, sondern richtig sehen, so würden Sie sagen: Hier erstrecken sich herein die kosmischen Gedanken der Exusial, der Geister der Form, der Elohim.",
      "Diese kosmischen Gedanken machen sich mir sichtbar, indem sie ausgefüllt sind mit den kosmischen Gedanken der Geister der Weisheit. Das gibt Arme und Hände, Beine und Füße. Gar nicht steht das da, als was es in der Maja erscheint, vor dern geistigen Blicke, sondern da stehen die kosmischen Gedanken, und diese kosmischen Gedanken ballen sich zusammen, kondensieren sich, schieben sich ineinander, und daher erscheinen sie uns als diese Schattenfigur, als die wir herumgehen, von der wir glauben, daß sie wirklich ist.",
      "Also den physischen Menschen, den gibt es gar nicht.",
      "Wir können mit einem gewissen Recht sagen: In der Stunde des Todes scheiden die Geister der Form ihre kosmischen Gedanken von den kosmischen Gedanken der Geister der Weisheit. Die Geister der Form nehmen ihre Gedanken in die Luft hinauf, die Geister der Weis­heit senken ihre stofflichen Gedanken in die Erde hinein. Dadurch ist im Leichnam so ein Nachschatten von den Gedanken der Geister der Weisheit noch vorhanden, wenn die Geister der Form ihre Gedanken zurückgenommen haben in die Luft. Das ist der physische Tod; das ist er in Wahrheit.",
      "Kurz, wenn wir anfangen, über Wirklichkeiten zu denken, so kom­men wir zu einer Auflösung desjenigen, was gewöhnlich die physische Welt genannt wird. Denn diese physische Welt besteht dadurch, daß die Geister der höheren Hierarchien ihre Gedanken ineinander-schieben, und deshalb - bitte stellen Sie sich vor: fein verteilte Wasser-partien gehen irgendwo hinein und bilden einen dichten Nebel - er­scheint Ihr Leib auch so als ein Schattengebilde, weil die Gedanken der Geister der Form hineindringen in die Gedanken der Geister der Weisheit, die Formgedanken in die Stoffgedanken hineingehen. Die ganze Welt löst sich vor dieser Anschauung in Geistiges auf. Aber man muß die Möglichkeit haben, die Welt wirklich geistig vorzu­stellen, zu wissen: Das ist nur etwas ganz Scheinbares, daß meine Arme und Hände, meine Füße und Beine der Erde übergeben werden. In Wirklichkeit beginnt da die Metamorphose meiner Arme und Beine, Hände und Füße und vollendet sich in dem Leben zwischen dem Tod und einer neuen Geburt, und meine Arme und Beine, Hände und Füße werden mein Kopf in der nächsten Inkarnation.",
      "Ich habe Ihnen mancherlei jetzt gesprochen, was Sie wenigstens in der Form vielleicht etwas sonderbar berührt hat. Aber was ist denn das schließlich, was wir da besprochen haben, anderes, als daß wir vom scheinbaren Menschen aufsteigen zum wahren Menschen, von dem, was äußerlich in der Maja lebt, aufsteigen zu der Stufenfolge der Hierarchien? Nur wenn man das tut, kann man in einer reifen Form heute davon sprechen, daß der Mensch in sich wissen darf ein soge­nanntes höheres Selbst. Wenn man bloß daklamiert von dem höheren Selbst, wenn man bloß sagt: Ich fühle in mir ein höheres Selbst - da ist dieses höhere Selbst ein reines leeres Abstraktum, da hat es keinen Inhalt; denn das gewöhnliche Selbst gehört der Maja an, ist also selbst Maja. Das höhere Selbst hat nur einen Sinn, wenn man von ihm spricht gegenüber der Welt der höheren Hierarchien. Vom höheren Selbst zu sprechen, ohne auf die Welt Rücksicht zu nehmen, die da besteht aus den Geistern der Form und den Engeln, Erzengeln und so weiter, vom höheren Selbst zu sprechen, ohne auf diese Welt Rücksicht zu nehmen, bedeutet: man spricht von leeren Abstrak­tionen, bedeutet zugleich: man spricht nicht von demjenigen, was da",
      "lebt im Menschen zwischen dem Tod und einer neuen Geburt. Denn so wie wir hier mit Tieren, Pflanzen und Mineralien leben, so leben wir zwischen dem Tod und einer neuen Geburt mit den Reichen der höheren Hierarchien, von denen wir oftmals gesprochen haben. Nur wenn man sich nach und nach diesen Vorstellungen und Be­griffen nähert, dann - wir werden davon erst vielleicht in acht Tagen sprechen-, dann kommt man zu einer Annäherung an so etwas, was Ant­wort geben kann auf die Frage: Warum sterben manche Menschen als junge Kinder, warum manche im höchsten Alter, andere dazwischen?",
      "Was ich Ihnen jetzt skizzenhaft dargestellt habe, sind konkrete Be­griffe für die Wirklichkeiten der Welt. Es sind ja wahrhaftig nicht abstrakte Begriffe, die ich Ihnen dargestellt habe, es sind konkrete Begriffe für die Wirklichkeiten der Welt. Diese konkreten Begriffe, sie gab es, allerdings für ein mehr atavistisches Anschauen, in den alten Mysterien. Sie sind für das menschliche Anschauen verloren­gegangen von dem 8. vorchristlichen Jahrhundert an; sie müssen durch eine Vertiefung in der Auffassung des Christus-Wesens wieder­um gewonnen werden. Das kann nur auf geisteswissenschaftlichem Wege geschehen.",
      "Verschaffen wir uns von einem gewissen Gesichtspunkte aus noch einmal eine Art Vorstellung von der Menschheitsevolution. Wir wollen jetzt sehr, sehr wichtige Begriffe ins Auge fassen. Da kann man sagen: Wenn man zurückgeht in der Menschheitsentwickelung, da kommt man - ich habe ja das öfter dargestellt - darauf, daß in alten Zeiten die Menschen mehr Gruppenseelen hatten und sich dann erst die individuellen Seelen hineingliederten in das Gruppenseelentum. Sie können das in verschiedenen Zyklen lesen. Dann könnte man schematisch die Entwickelung der Menschheit so darstellen, daß man sagt: In alten Zeiten gab es Gruppenseelen; jede dieser Gruppenseelen spaltete sich wiederum - das würde für eine bloße seelische An­schauung sein, für eine geistige wäre es etwas anders -, aber jede solche Seele umlileidet sich mit einem Leibe, den ich hier in der Form mit einem roten Strich andeute (siehe Zeichnung Seite 114).",
      "Diese Zeichnung oder etwas ähnliches wie diese Zeichnung hat man noch bis in die Pythagoräische Schule hinein immer gemacht, indem",
      "# Bild s. 114",
      "man gesagt hat: Seht ihr die Leiber an, den Leibern nach sind die Menschen getrennt, jeder für sich ein Leib - daher sind die roten Striche hier isoliert -, den Seelen nach findet man aber eine Einheit der Menschheit, indem man hinaufgeht bis zur Gruppenseele, die allerdings weit zurückliegt. - Man hat eine Einheit. Wenn Sie sich das Rote wegdenken, so bildet das heller Schraffierte eine einheitliche Figur.",
      "Aber es hat nur einen Sinn, über diese Figur zu sprechen, wenn man zuerst von dem Geistigen so gesprochen hat, wie wir es heute getan haben; denn dann weiß man, was in diesen Seelen alles mitwirkt, wie die höheren Hierarchien mitwirken an diesem Seelischen. Es hat keinen Sinn, von dieser Figur zu sprechen, wenn man nicht im Hin­blick auf die Hierarchien spricht. So hat man auch gesprochen bis in die Pythagoräische Schule herein, und aus den Pythagoräischen Schu­len hat wiederum Apollonius dasjenige gelernt, wovon ich gestern ge­sprochen habe, von dem ich in der nächsten Woche weiter sprechen werde. Dann aber, seit dem 8. vorchristlichen Jahrhundert - schon die Pythagoräischen Schulen waren Nachzügler -, hat sich die Möglich­keit, so zu sprechen, verloren. Und allmählich sind die Begriffe, die konkret sind, die wirklich sind, wenn sie sich auf die höheren Hierar­chien beziehen, den Leuten konfus geworden, verschwommen ge­worden. Und so ist ihnen statt der Welt der Engel, Erzengel, Ur­kräfte, Formen, Bewegungen, Weisheiten, Throne, statt all diesem konkreten Geistweben ist ihnen ein Begriff gekommen, der nun schon in der griechischen Anschauung eine gewisse Rolle spielt: der Begriff",
      "des Pneuma, in dem alles durcheinander schwimmt. Pneuma, allge­meiner Geist - dieser verschwommene Begriff, den noch heute die Pantheisten lieben: Geist, Geist, Geist, Geist! Ich habe öfter davon gesprochen, daß die Pantheisten überall den Geist hinsetzen. Aber das geht schon im griechischen Leben auf. Da hat man wieder diese Figur gezeichnet; aber Sie sehen: Was früher konkret war - die Fülle der Gottheiten-, ist zum abstrakten Begriff geworden, ist zum Pneuma geworden. Das Weiße ist das Pneuma, das Rote ist die physische Materie (siehe Zeichnung Seite 114), wenn man die Menschenevo­lution in Betracht zieht. Aber von diesem Pneuma, von dem haben die Griechen wenigstens noch eine Anschauung gehabt, denn sie haben immerhin noch etwas Aurisches gesehen; so daß also das, was sie sich da in dem weißen Gezweige vorstellten, für sie noch etwas Aurisches, also etwas wirklich Anschauliches war. Das ist die große Bedeutung des Überganges vom Griechentum ins Römertum, daß die Griechen in ihrer Anschauung noch das Pneuma als wirkliches Geistiges erlebt haben, die Römer nicht mehr. Bei den Römern ist es schon ganz abstrakt geworden, vollständige Abstraktion geworden, bloße Begriffe. Die Römer sind das Volk der abstrakten Begriffe.",
      "Meine lieben Freunde, in der neueren Zeit finden Sie in der Natur­wissenschaft wiederum dasselbe Schema ! Sie können es heute in materialistischen naturwissenschaftlichen Büchern aufschlagen: da finden Sie ganz genau dieses Schema, das Sie in den alten Mysterien aufgezeichnet gefunden haben, in den Pythagoräischen Schulen, wo alles noch auf die Hierarchien bezüglich war. Sie haben es bei den Griechen, wo es auf das Pneuma bezüglich war; Sie finden es heute wieder gezeichnet. Wir werden sehen, was es heute ist. Heute sagt der Naturforscher, indem er diese selbe Zeichnung seinen Schülern auf die Tafel zeichnet: Indem das Menschengeschlecht sich fort-pflanzt, geht die Keimsubstanz der Eltern über auf die Kinder; ein Teil der Keimsubstanz bleibt aber so erhalten, daß er in der nächsten Generation wiederum auf die Kinder übergehen kann, und von dem bleibt wiederum ein Teil so, daß er wieder auf die Kinder über­gehen kann, während ein anderer Teil der Keimsubstanz die Zellen des physischen Leibes bildet. - Sie haben ganz dasselbe Schema, nur",
      "sieht der heutige Naturforscher in dern Weißen (siehe Zeichnung) die Kontinuität der Keimsubstanz. Er sagt: Wenn wir zu den alten Men­schenvorfahren hinaufgehen und ihre Keimsubstanz nehmen, die männliche und die weibliche Keimsubstanz nehmen, und gehen zu den jetzigen Menschen herunter und nehmen ihre jetzige Keimsub­stanz, so ist das ein einziger Strom; die Keimsubstanz ist kontinuier­lich. Es bleibt immer in der Keimsubstanz etwas ewig - so stellt es sich der Naturforscher vor - und nur gewissermaßen die Hälfte des Keimplasmas geht über in die andere Körperlichkeit. - Der Natur-forscher hat wiederum dieselbe Figur, nur hat er jetzt nicht mehr das Pneuma, sondern das Weiße, das ist ihm jetzt die materielle Keimsub­stanz. Es ist nichts Seelisch-Geistiges mehr, es ist ihm die materielle Keimsubstanz. Das können Sie bei den heutigen Naturforschern lesen, das nimmt man heute an als eine große, bedeutsame Entdeckung. Das ist Materialisierung einer hochgeistigen Vorstellung, indem sie durch die Abstraktion durchgegangen ist; der abstrakte Begriff steht mitten drinnen. Und drollig ist es, daß ein Naturgelehrter der neue­ren Zeit ein Buch geschrieben hat - für jemanden, der ordentlich denken kann, ist es drollig -, in welchem er geradezu sagt: Was die Griechen sich noch unter Pneuma vorgestellt haben, ist heute die kontinuierlich bleibende Keimsubstanz. - Ja, es ist närrisch, aber es ist heute hohe Weisheit.",
      "Aber Sie sehen daraus eines: die Zeichnung macht es nicht ! Und Sie werden daraus begreifen, warum ich immer in einer gewissen Weise mich gewendet habe gegen das Aufzeichnen von Schemen, solange wir noch versuchten, unsere Anthroposophie durch die Theo­sophische Gesellschaft durchzutragen. Man brauchte nur in irgend­einen theo sophischen Zweig einzutreten: die Wände waren in der Regel behängt mit allerlei solchen Schemen. Da war alles mögliche aufgezeichnet, da standen dann Worte dabei, und da waren ganze Stammbäume und alles mögliche aufgezeichnet. Aber auf diese Zeichnungen kommt es nicht an, sondern es kommt darauf an, daß man wirklich zu dern lebendigen Vorstellen gehen kann; denn die Zeichnung kann ganz dieselbe sein, ob Sie sie als Ausfluß der Hier­archien, Geistig-Seelisches sich vorstellen, oder ob Sie sich das kontinuierliche",
      "Keimplasma, eine reine Materie, vorstellen. Diese Dinge verschwimmen dern heutigen Menschen. Daher ist es so wichtig, sich klar darüber zu sein, wie der Grieche noch etwas gewußt hat von dern realen Selbst im Menschen, von dern realen Geistigen, und wie das beim Römer in den abstrakten Begriff übergegangen ist. Sie können das an Äußerlichkeiten sehen. Indem der Grieche von seinen Göttern redet, redet er so, daß man ganz genau sieht: der Grieche denkt sich noch konkrete Figuren hinter den Göttern. Beim Römer sind die Götter im Grunde nur noch Namen, nur Bezeichnungen, sind Ab­straktionen und werden immer mehr Abstraktionen. Beim Griechen war immer noch eine gewisse Vorstellung vorhanden, daß in dern Menschen, der hier steht, die Hierarchien leben, und in jedem Men­schen verschieden die Hierarchien leben. Der Grieche nahm den Menschen seiner Realität nach, und wenn er sprach: Das ist der Alki­biades, das ist der Sokrates, das ist der Plato -, so hatte er noch den Begriff: da in den Alkibiades, in den Sokrates, in den Plato, da ragen herein die kosmischen Gedanken der Hierarchien in verschiedener Weise, und dadurch, daß da die kosmischen Gedanken in verschie­dener Weise hereinragen, treten so verschiedene Figuren aufl",
      "Das ging beim Römer verloren. Daher bildete sich beim Römer ein System von Begriffen aus, das sein Extrem darinnen hat, daß von Augustus an - eigentlich schon früher - der römische Cäsar selber als Gott galt. Die Gottheit war allmählich verabstrahiert, und der rö­mische Cäsar war selber ein Gott, weil der Begriff vollständig abstrakt geworden war. Aber so abstrakt wurden auch die andern Begriffe. So abstrakt wurden namentlich die Begriffe, die als Rechtsbegriffe, als moralische Begriffe das römische Wesen durchsetzten, und so trat an die Stelle von alten Lebendigkeiten eine Summe von Abstraktio­nen. Und diese Summe von Abstraktionen, die ist als Erbschaft ge­blieben durch das ganze Mittelalter hindurch, ist auf die neuere Zeit heraufgekommen, ist bis in das 19. Jahrhundert herein als Erbschaft geblieben: abstrakte Begriffe, die überall hineingetragen werden.",
      "Da kam etwas Überraschendes im 19. Jahrhundert. Unter den ab­strakten Begriffen hat man den Menschen vollständig verloren ge­habt. Der Grieche ahnte noch etwas von dern wirklichen Menschen,",
      "der aus dem Kosmos herein gebildet wird; durch das Römertum hin­durch ist der Mensch verlorengegangen. Das 19. Jahrhundert war genötigt, ihn wieder zu entdecken durch alle die Verhältnisse, auf die ich Sie schon hingewiesen habe, auf die ich Sie noch genauer hin­weisen werde.",
      "Und die Entdeckung des Menschen, die geschah jetzt von dem andern Pol aus. Das Griechentum hat sehen wollen den Menschen, der aus der Hierarchie kommt, den göttlichen Menschen; die Römer haben an die Stelle eine Reihe von abstrakten Begriffen gesetzt; das 19.",
      "Jahrhundert, schon das 18. Jahrhundert, aber nament­lich das 19. Jahrhundert war genötigt, den Menschen von der andern Seite, von seiner Tierseite aus wieder zu entdecken. Und da konnte er jetzt nicht gefaßt werden mit diesen abstrakten Begriffen.",
      "Das war der große Schock. Und das ist der große Schock, das ist die tiefe Kluft, die entsteht: Was ist denn das eigentlich, was da auf zwei Beinen vor uns steht und mit den Händen fuchtelt und allerlei ißt und trinkt, was ist denn das?",
      "Die Griechen haben es noch gewußt; dann ist es in abstrakte Begriffe verwandelt worden. Jetzt überrascht es die Men­schen im 19. Jahrhundert; da steht es, aber man hat keine Begriffe, es zu fassen. Man faßt es als bloßes höheres Tier auf: es wird auf der einen Seite der Darwinismus, naturwissenschaftlich, auf der andern Seite, im Geistigen, der Sozialismus, der den Menschen nur als Tier in die Sozietät hineinstellen will.",
      "Es ist der Mensch, der vor sich selber überrascht steht: Was ist denn das eigentlich? - und der ohn­mächtig ist, diese Frage zu beantworten.",
      "Das ist die Situation von heute, das ist die Situation, die nicht nur, je nachdem die Menschen es wollen, richtige oder unrichtige Be­griffe schaffen wird, sondern die dazu berufen ist, katastrophale oder heilsame Tatsachen zu schaffen. Aber das ist sie, die Situation: der Schock, den der Mensch vor sich selber hat. Wiederum müssen die Elemente zum Begreifen des geistigen Menschen gefunden werden. Man wird sie nicht anders finden, als wenn man auf die Metamor­phosenlehre eingeht. Da liegt der wesentliche Punkt. Die Metamor­phosenbegriffe des Goetheanismus sind allein imstande, die fluk­tuierenden Erscheinungen zu fassen, welche sich dem Anschauen der Wirklichkeit darbieten.",
      "Nun, nach dieser Richtung, möchte ich sagen, schob die geistige Ent­wickelung schon immer. Auch damals - ich habe das im «Reich» in einer Reihe von Aufsätzen über «Die chymische Hochzeit des Christian Rosen­kreutz» angedeutet-, als im 17. Jahrhundert «Die chymische Hochzeit» und andere Schriften auf so wunderbare Weise veröffentlicht worden sind, da war schon das Bestreben, vorzusorgen, daß eine solche soziale Struktur, die der wahren Wesenheit des Menschen entspricht, unter die Menschen kommen sollte. Auf diese Weise ist ja «Die chymische Hoch­zeit des Christian Rosenkreutz» von dem sogenannten Valentin Andreae entstanden. Aber auf der andern Seite ist ja auch das Buch entstanden, das er nannte «Allgemeine Reformation der ganzen weiten Welt», wo er einen großen politischen Überblick gibt, wie die sozialen Verhältnisse werden sollen. Der Dreißigjährige Krieg hat die Sache hinweggefegt.",
      "Dort ist es der Dreißigjährige Krieg, der die Dinge hinweggefegt hat. Heute ist es möglich, daß die Weltordnung entweder dahin geht, die Dinge wirklich wiederum hinwegzufegen, oder aber sie in die Menschheitsentwickelung hineinzunehmen. Damit berühren wir die große Grundfrage der Gegenwart, mit der sich die Menschen be­schäftigen sollten, statt mit all den sekundären Fragen, mit denen sich die Menschen heute beschäftigen. Würden sich die Menschen mit die­ser Grundfrage beschäftigen, dann würden sie die Mittel und Wege finden, fruchtbare Begriffe in die heutige Wirklichkeit hineinzutragen; dann würde man meiden die abstrakten Begriffe.",
      "Es ist nicht so leicht, Wirklichkeit von Täuschung zu unterscheiden. Da muß man schon wirklich im Ernste und mit allem guten Willen ins Leben hinein wollen, nicht bei Programmen und bei Vorurtellen Halt machen wollen. Nach dieser Richtung könnte ich ja vieles er­zählen. Ich will nur ein Faktum anführen: Im Beginne der neunziger Jahre, da traten eine Anzahl von Menschen zusammen in den ver­schiedensten Städten in Europa und machten wiederum einmal etwas Amerikanisches nach: nämlich die «Bewegung für ethische Kultur». Es war dazumal unter gewissen Intellektuellen alles darauf aus, «Ge­sellschaften für ethische Kultur» zu gründen. Die Leute haben sehr schöne Sachen vorgebracht, und wenn Sie heute noch die Auf­sätze lesen, die dazumal von diesen Vertretern der Gesellschaften für",
      "ethische Kultur geschrieben worden sind, wenn Sie Sinn haben für",
      "- ja, butteriges Zeug, so werden Sie wahrscheinlich heute noch ent­zückt sein können von all den schönen, wunderschönen Idealen, in denen die Leute dazumal geschwelgt haben. Und es war wahrhaftig keine angenehme Aufgabe, sich gegen dieses Schwelgen in den but­terigen Idealen zu wenden.",
      "Ich schrieb aber dazumal in einer der ersten Nummern der Zeitschrift «Die Zukunft» einen Artikel gegen dieses ganze butterige Zeug von der «ethischen Kultur», schimpfte mordsmäßig über diese «ethische Kultur». Es war selbstverständlich eine schändliche Tat, denn wie könnte es nicht etwas Schändliches sein, wenn man sich gegen etwas so Gutes wendet, wenn die Leute daran gehen, die ganze Welt zu ethisieren, durchaumoralisieren !",
      "Ich lebte dazumal in Weimar, kam aber einmal nach Berlin, sprach auch mit Herman Grimm; der sagte: Was wollen Sie denn eigentlich mit dieser «ethischen KultuD>? Gehen Sie doch hin zu den Leuten, Sie werden sehen: die in Berlin hier zusammenkommen, diese Ethiker sind lauter recht nette, liebe Leute.",
      "Man kann gegen sie gar nichts haben. Es sind Leute, die einem ganz sympathisch sein können, die einem ganz gut gefallen können. - Das war auch gar nicht zu leugnen, und für den damaligen Moment hatte selbstverständlich Herman Grimm ebenso recht wie ich.",
      "Äußerlich genommen hatte der eine ebenso recht für den Moment wie der andere; das eine ließ sich eben­sogut beweisen wie das andere, und ich will gar nicht behaupten, daß rein logisch meine Gründe gegen die Ethiker besser waren als die Gründe, die die Ethiker vorgebracht haben. Aber aus all diesem Butteridealismus ist ja die gegenwärtige Katastrophe hervorgegan­gen, und nur diejenigen Menschen hatten recht und sind durch die Tatsachen gerechtfertigt, die dazumal gesagt haben: Mit all eurem Schwelgen und Reden von irgend solchen Butteridealen, durch die ihr allgemeinen Frieden und dergleichen und allgemeine Moral unter die Menschen bringen wollt, erzeugt ihr nichts anderes als das, was ich dann das soziale Karzinom genannt habe, was endlich in diese katastrophale Gegenwart hineinführen mußte.",
      "Die Zeit hat gezeigt, wer mit realen Begriffen arbeitete und wer mit bloßen Abstraktionen arbeitete. Nach dem bloßen abstrakten Charakter kann man gar nicht",
      "entscheiden, ob irgend jemand recht oder unrecht hat; das entschei­det bloß das, ob irdendein Begriff richtig sich hineinfügt in den Gang der Tatsachen oder nicht. Wenn ein Professor an seiner Universität heute Naturwissenschaft lehrt, dann kann er selbstverständlich wun­derschön beweisen, logisch beweisen, daß das alles richtig ist, was er sagt.",
      "Das geht auch alles in die Löcher der Köpfe hinein; das darf ich ja natürlich im allerbesten Sinne heute sagen. Und siehe da, darum handelt es sich aber nicht, ob scheinbare gute logische Gründe dafür anzuführen sind, sondern: dieselben Gedanken dann in einen Lenin­Kopf hineingesenkt, werden Bolschewismus.",
      "Was ein Gedanke in der Wirklichkeit wird, darauf kommt es an. Nicht darauf kommt es an, was man über ihn denken kann, was man über ihn abstrakt fühlen kann, sondern darauf, welche Kraft in der Wirklichkeit einen Gedan­ken bildet.",
      "Und wenn man diejenige Weltanschauung, von der am meisten in der neueren Zeit gesprochen worden ist, weil die andern ästhetisierend waren, wie ich gestern ausgeführt habe, wenn man den Sozialismus prüft, so handelt es sich heute nicht darum, sich nun hin-zusetzen, um den Karl Marx oder Lassalle oder den Bernstein zu «ochsen», also deren Bücher zu studieren, diese Autoren zu studieren, sondern darum handelt es sich, ein Gefühl, eine lebendige Erfahrung dafür zu haben, was im Fortgang der Menschheit dann wird, wenn eine Anzahl von Menschen - solche Menschen, die an Maschinen stehen - diesen Gedanken haben. Darauf kommt es an, und nicht darauf, über die soziale Struktur der nächsten Zukunft die Gedanken zu haben, die man im landläufigen Gang der heutigen diplomatischen Schulung lehrt.",
      "Sondern jetzt ist die Zeit, wo es darauf ankommt, Gedanken wägen zu können, um sich die Frage beantworten zu kön­nen: Was will die Zeit in den nächsten Jahrzehnten? Es ist heute schon einmal die Zeit gekommen, wo die Bequemlichkeit nicht ge­stattet ist, auf den verschiedensten kurulischen Stühlen zu sitzen und bequem das Alte fortaupflegen, sondern die Zeit ist gekommen, wo die Menschheit den Schock vor sich selbst fühlen muß, und wo bei denen, die irgendwo verantwortlich sind für irgend etwas, der Ge­danke auftauchen muß: Wie löst man diese Frage aus dem geistigen Leben heraus?",
      "Wir werden das nächste mal davon weiter sprechen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Gewisse Fragen werden dem denkenden Menschen sich doch immer wieder und wiederum aufdrängen, wenn er auch in Zeiten, in denen die materialistische Kultur überwiegt, diesen Fragen mehr oder we­niger aus dem Wege gehen möchte.",
        "Es sind viele Fragen.",
        "Ich möchte heute ein paar aus der großen Reihe der Fragen herausheben, die da­von kommen, daß der Mensch doch, selbst wenn er sich sträubt, eine geistige Welt anzuerkennen, den Eindruck dieser geistigen Welt ver­spürt.",
        "Zu solchen Fragen gehört zum Beispiel diese, die ja, man möchte sagen, das Leben alltäglich aufwirft: Gewisse Menschen sterben jung, andere sterben ganz alt, andere dazwischen.",
        "Gegenüber dieser Tatsache, daß auf der einen Seite ganz junge Kinder sterben, auf der andern Seite Leute ganz alt werden und dann sterben, erheben sich für den Menschen Fragen, welche mit den Mitteln, die man heute wissenschaftliche Mittel nennt, niemals - bei klarer Besinnung wird das jeder zugeben müssen - werden zu beantworten sein.",
        "Und doch sind sie für das Menschenleben brennende Fragen, und jeder kann eigentlich empfinden, daß sich für das Leben Unendliches aufklären müßte dadurch, daß man diesen Fragen nahetreten könnte: Warum sterben Menschen zuweilen früher, im Kindesalter, im Jugendalter, in der Mitte der gewöhnlichen Lebenszeit?",
        "Warum sterben andere alt?",
        "Was hat das für eine Bedeutung im gesamten Weltenall?"
      ],
      [
        "Sich solche Fragen zu beantworten, dazu hatten die Menschen bis zu jenem Zeitpunkte, den ich Ihnen in diesen Betrachtungen schon angegeben habe, bis zu dem Zeitpunkt der beginnenden vierten nach-atlantischen Zeit, so ungefähr bis in die Mitte des 8. vorchristlichen Jahrhunderts, noch Vorstellungen, Begriffe.",
        "Aus alter Weisheit her­überbekommen hatten sie Begriffe.",
        "Es gab auch in jenen alten Zeiten, die dem 8. vorchristlichen Jahrhundert vorangingen, über die da­malige Erdenkultur verbreitet überall Vorstellungen, welche nach dem Sinn der damaligen Zeit den Menschen Aufschluß gaben über solche Fragen wie die eben angedeuteten.",
        "Dasjenige, was wir heute"
      ],
      [
        "Wissenschaft nennen, kann nicht einmal einen rechten Sinn verbinden mit solchen Fragen, kommt gar nicht darauf, daß etwas mit diesen Fragen gegeben ist, wozu man irgendeine Antwort suchen sollte.",
        "Das alles rührt davon her, daß in der Zeit, die seit dem eben angedeuteten Zeitpunkte verflossen ist, eigentlich alle Vorstellungen verlorenge­gangen sind, die sich auf den geistigen und damit auf den ewigen Menschen beziehen.",
        "Es sind nur diejenigen Vorstellungen geblieben, die sich auf den vergänglichen Menschen und den zwischen Geburt und Tod eingeschlossenen Menschen beziehen."
      ],
      [
        "Ich habe darauf aufmerksam gemacht, daß in allen alten Weltan­schauungen von einer dreifachen Sonne gesprochen wurde, von jener Sonne, die man mit den physischen Sinnen wahrnimmt als eine leuchtende Kugel im Weltenraume draußen.",
        "Hinter dieser Sonne aber sahen die alten Weisen die seelische Sonne - im griechischen Sinne gesprochen, den Helios - und erst hinter dieser seelischen Sonne die geistige Sonne, die zum Beispiel noch Plato identifizierte mit dem Guten."
      ],
      [
        "Es hat für den heutigen Menschen eigentlich keinen rechten Sinn, von dem Helios, der seelischen Sonne, oder gar von der geisti­gen Sonne, von dem Guten, zu sprechen.",
        "Aber so wie uns hier zwi­schen Geburt und Tod die physische Sonne leuchtet, so scheint, wenn ich sagen darf, in unser Ich hinein in der Zeit, die wir verbringen zwischen dem Tod und einer neuen Geburt, die geistige Sonne, die eben noch von Plato identifiziert wird mit dem Guten."
      ],
      [
        "Für die Zeit zwischen dem Tod und einer neuen Geburt von dieser leuchtenden Kugel zu sprechen, von der unsere heutige materialistische Weltan­schauung spricht, hat keinen Sinn; zwischen dem Tod und einer neuen Geburt hat nur Sinn zu sprechen von der geistigen Sonne, von dem, was Plato noch als das Gute bezeichnet.",
        "Aber gerade ein solcher Be­griff sollte uns auf etwas hinweisen."
      ],
      [
        "Er sollte uns darauf hinweisen, nachzudenken, wie es sich eigentlich verhält mit dem, was wir uns als physische Vorstellung von der Welt bilden.",
        "Daß wir in dem, was wir uns als physische Vorstellungen von der Welt bilden, in dem, was sinnenfällig vor uns ausgebreitet ist, zu sehen haben eine Art von Täuschung, eine Art von Maja, das wird doch nicht im vollen Sinne des Wortes ernst genommen, wenigstens nicht so ernst, daß die Anschauung"
      ],
      [
        "des Lebens wirklich mit diesen Dingen durchdrungen würde."
      ],
      [
        "So eine Art Vorstellung von der Sonne hat im Grunde derjenige, der die heutige Physik, Astrophysik meinetwillen, autoritativ nimmt: Wenn er da hinauffahren könnte, wohin die Physiker die Sonne ver­setzen, so würde er, indem er sich der Sonne nähert - nun, sehen wir jetzt von menschlichen Lebensbedingungen ab, setzen wir voraus, daß die Lebensbedingungen absolut sein könnten -, gewaltige Hitze ver­spüren, so stellt er es sich vor, und er würde da, wenn er innerhalb des Raumes ankommt, den sich der Physiker von der Sonne ausge­füllt denkt, innerhalb dieses Raumes glühendes Gas oder dergleichen finden.",
        "So stellt sich der Physiker ja das eigentlich vor: einen glühen­den Gasball oder so etwas."
      ],
      [
        "Aber so ist es nicht, das ist eine richtige Maja, eine richtige Täuschung.",
        "Und diese Vorstellung hält vor den wahren physikalischen Anschauungen, die man gewinnen kann, auch nicht stand, geschweige denn vor der wirklichen übersinnlichen An­schauung."
      ],
      [
        "Wenn man sich nämlich wirklich der Sonne nähern könnte und dahin kommen würde, wo die Sonne ist - ja, indem man sich nähert, da findet man schon so etwas, wie wenn man durch flutendes Licht durchgehen müßte (es wird gezeichnet: gelber Kreis, innen blauer Kern); aber wenn man da hineinkommt, wo die Physiker die physische Sonne vermuten, findet man zunächst das, was man an­sprechen könnte als leeren Raum.",
        "Da ist überhaupt nichts; es ist gar nichts da, wo man die physische Sonne vermutet."
      ],
      [
        "Ich zeichne es schematisch (blau), weil eigentlich nichts dort ist.",
        "Da ist nichts, da ist leerer Raum.",
        "Aber ein sonderbarer leerer Raum ist das!",
        "Wenn ich sage: Es ist nichts da -, so rede ich eigentlich nicht ganz richtig; es ist weniger als nichts da."
      ],
      [
        "Es ist nicht nur ein leerer Raum da, sondern es ist weniger als nichts da.",
        "Und das ist es, was als eine Vorstellung für abendländische Menschen heute außerordentlich schwer zu bilden ist.",
        "Der Morgenländer hat diese Vorstellung auch heute noch ohne wei­teres; für den ist es gar nichts Wunderbares oder Schwerverständ­liches, wenn man ihm davon spricht, daß da weniger als nichts ist."
      ],
      [
        "Der Abendländer denkt sich, und er denkt sich das insbesondere, wenn er ein waschechter Kantianer ist, denn viel mehr Leute, als man"
      ],
      [
        "heute denkt, sind Kantianer, sind unbewußte Kantianer: Wenn nichts im Raum ist, so ist es eben leerer Raum! - Aber das ist nicht der Fall; es kann auch ausgeschöpfter Raum sein.",
        "Wenn Sie nämlich da durch diese Sonnenkorona durchsehen würden, so würden Sie diesen leeren Raum, in den Sie da eintreten würden, höchst unbehaglich empfinden: er zerreißt Sie nämlich.",
        "Und darin zeigt er seine Wesenheit, daß er mehr ist - oder weniger ist, wie ich besser sagen kann - als ein leerer Raum.",
        "Sie brauchen ja nur die einfachsten mathematischen Begriffe zu Hilfr zu nehmen, so wird Ihnen nicht ganz unklar bleiben können, was ich da meine: leerer Raum ist weniger noch als bloß leer.",
        "Nehmen wir an, Sie besitzen irgend etwas an Vermögen.",
        "Aber es kann auch vorkommen, daß Sie alles, was Sie besitzen, ausgegeben haben, daß Sie nichts haben.",
        "Aber man kann weniger als nichts haben: man kann Schulden haben, dann hat man wirklich weniger als nichts.",
        "Man kann, wenn man von der Raumerfüllung zu immer dünnerer und dünnerer Raumerfüllung übergeht, bis zum leeren Raum kommen; man kann aber dann hinter die bloße Leerheit noch hinübergehen, wie man von dem Nichts zu den Schulden gehen kann."
      ],
      [
        "Das ist der größte Fehler der heutigen Weltanschauung, daß sie diese eigentümliche Art von negativer Stofflichkeit - wenn ich mich so ausdrücken darf - nicht kennt, daß sie nur die Leerheit kennt und die Erfüllung, und nicht dasjenige, was weniger ist als die Leerheit.",
        "Denn dadurch, daß das heutige Wissen, die heutige Weltanschauung das, was weniger ist als die Leerheit, nicht kennt, dadurch wird diese heutige Weltanschauung mehr oder weniger im Materialismus fest­gehalten, richtig im Materialismus festgehalten, ich möchte sagen:"
      ],
      [
        "gebannt in den Materialismus.",
        "Denn es gibt auch im Menschen, wenn ich mich so ausdrücken darf, einen Ort, welcher leerer ist als leer; nicht in seiner Gänze, aber welcher eingelagert hat Teile, die leerer sind als leer.",
        "Im ganzen ist ja der Mensch - ich meine der physische Mensch -ein Wesen, welches einen Raum materiell ausfüllt; aber ein gewisses Glied der menschlichen Natur, von den dreien, die ich angeführt habe, hat tatsächlich etwas in sich, was sonnenähnlich ist, leerer ist als leer.",
        "Das ist - ja, Sie müssen es schon hinnehmen - der Kopf.",
        "Und gerade darauf, daß der Mensch so organisiert ist, daß sein Kopf sich immer"
      ],
      [
        "entleeren kann und in gewissen Gliedern leerer sein kann als leer, da­durch hat dieser Kopf die Möglichkeit, das Geistige sich einzulagern.",
        "Stellen Sie sich einmal die Sache vor, wie sie eigentlich ist.",
        "Natürlich muß man die Dinge sich schematisch vorstellen; aber denken Sie sich, alles dasjenige, was materiell Ihren Kopf ausfüllt, würde ich schematisch durch das Folgende zeichnen.",
        "Das wäre schematisch Ihr Kopf (siehe Zeichnung, rot).",
        "Nun aber muß ich, wenn ich ihn vollständig zeichnen will, in diesem Kopf leere Stellen lassen.",
        "Das ist natürlich jetzt nicht so groß, aber drinnen sind leere Stellen.",
        "In diese leeren Stellen kann dasjenige hinein, was ich Ihnen den jungen Geist genannt habe in die­sen Tagen.",
        "In die leeren Stellen hinein muß der junge Geist, gewisser­maßen in seinen Strahlen, gezeichnet werden (gelb)."
      ],
      [
        "# Bild s. 101"
      ],
      [
        "Ja, die Materialisten sagen: Das Gehirn ist das Werkzeug des Seelen­lebens, des Denkens. - Das Umgekehrte ist wahr: Die Löcher im Gehirn, ja sogar dasjenige, was mehr ist als Löcher, oder ich könnte auch sagen, weniger ist als Löcher, was leerer ist als leer, das ist das Werkzeug des Seelenlebens.",
        "Und da, wo das Seelenleben nicht ist, wo das Seelenleben fortwährend aufstößt, wo der Raum unseres Schädels mit Gehirnmasse ausgefüllt ist, da wird nichts gedacht, da wird nichts seelisch erlebt.",
        "Wir brauchen unser physisches Gehirn nicht zum Seelenleben, sondern wir brauchen es nur, damit wir das Seelenleben einfangen, physisch einfangen.",
        "Wenn da nicht das Seelenleben, das in den Löchern des Gehirnes eigentlich lebt, überall aufstoßen würde, so"
      ],
      [
        "würde es verfliegen; es käme uns nicht zum Bewußtsein.",
        "Aber es lebt in den Löchern des Gehirns, die leerer sind als leer."
      ],
      [
        "So müssen wir uns die Begriffe allmählich korrigieren.",
        "Wir nehmen, wenn wir vor dem Spiegel stehen, nicht uns wahr, sondern unser Spiegelbild.",
        "Uns können wir vergessen.",
        "Wir sehen uns im Spiegel drinnen.",
        "So erlebt der Mensch auch nicht sich, indem er durch sein Gehirn dasjenige zusammenhält, was in den Löchern des Gehirnes liegt; er erlebt, wie sich überall sein Seelenleben spiegelt, indem es an die Gehirnmasse anstößt.",
        "Es spiegelt sich überall; das erlebt der Mensch.",
        "Er erlebt eigentlich sein Spiegelbild.",
        "Das aber, was da in die Löcher hereingeschlüpft ist, das ist dasjenige, was dann, wenn der Mensch durch die Pforte des Todes geht, ohne die Widerlage des Ge­hirnes seiner selbst bewußt wird, weil es dann in entgegengesetzter Weise mit Bewußtsein durchsetzt wird."
      ],
      [
        "Nun will ich ein anderes Schema aufzeichnen.",
        "Nehmen Sie das Folgende.",
        "Bitte, ich will jetzt das Gehirn recht drastisch zeichnen, wie das Löcher läßt (blau).",
        "Da sei die Gehirnmasse, da lasse es die Löcher, und dahinein in diese Löcher geht das Seelenleben (gelb).",
        "Dieses Seelenleben, das setzt sich aber vor den Löchern fort.",
        "Da kommen wir in die ja natürlich nur in der Nähe des Menschen sichtbare, aber ins Unbestimmte auslaufende Menschenaura hinein."
      ],
      [
        "# Bild s. 102"
      ],
      [
        "Denken wir uns jetzt das Gehirn weg, und denken wir uns, wir sehen beim gewöhniichen Menschen zwischen Geburt und Tod das"
      ],
      [
        "Seelenleben an, dann würden wir sagen müssen: Der wahre Mensch, in dieser Weise gesehen, der ist in seinem Zustande zwischen Geburt und Tod so, daß er eigentlich - da muß ich allerdings das jetzt anders schematisch zeichnen - sein Antlitz seinem Körper so zuwendet (siehe Zeichnung Seite 105, lila); sein Seelenleben wendet er dem Körper­lichen zu.",
        "Und wenn wir auf das Gehirn sehen, so streckt dieses Seelenleben hier Fühlhörner vor, die in die Löcher des Gehirns hin­eingehen.",
        "Was ich dort (siehe Zeichnung Seite 102) gelb gezeichnet habe, zeichne ich hier lila, weil das besser dem Anblick im lebenden Menschen entspricht.",
        "Das wäre das, was sich ins Gehirn erstreckt beim lebenden Menschen."
      ],
      [
        "Wollte ich jetzt danach etwa den physischen Menschen zeichnen, so würde ich das am besten dadurch andeuten können, daß ich Ihnen etwa hier die Grenze, die mit dem Erinnerungsvermögen gegeben ist, hereinzeichne.",
        "Sie würde da nach außen gehen, und da würde die äußere Grenze, die Grenze des Erkennens sein, von der ich Ihnen ja auch gesprochen habe.",
        "Da brauchen Sie sich ja nur an die letzthin und gestern gemachte Zeichnung zu erinnern."
      ],
      [
        "Jetzt aber ist es wirklich so,daß, wenn man von außen den Men­schen geistig anschaut, sich das Seelenleben so in den Menschen hin­ein erstreckt.",
        "Ich will also das einzelne Hineinerstrecken nur in bezug auf das Gehirn zeichnen.",
        "Aber dieses Seelenleben ist in sich auch differenziert: so würde ich, wenn ich dieses Seelenleben weiter verfolgen würde, hier eine andere Region zeichnen müssen (rot unter dem Lila), hier eine andere Region (blau); das würde also alles zu der den Menschen konstituierenden Aura gehören.",
        "Dann eine andere Region (grün): Sie sehen, dieser Teil, den ich da jetzt schematisch zeichne, liegt jenseits der Grenze des menschlichen Erkennens.",
        "Dann diese Region (gelb) - im Grunde genommen gehört das alles zum Men­schen - und diese Region (orange)."
      ],
      [
        "Das bewegt sich, wenn der Mensch einschläft, mehr oder weniger aus dem Körper heraus, sowie das gestern gezeichnet worden ist (Zeich­nung Seite 77); wenn der Mensch wachend ist, mehr oder weniger in den Körper hinein, so daß eigentlich die Aura nur in der unmittelbar­sten Umgebung des Körpers seelisch wahrzunehmen ist.",
        "Wenn man den"
      ],
      [
        "physischen Menschen beschreibt, dann tut man es so, daß man sagt: Dieser physische Mensch besteht aus Lunge, Herz, Leber, Galle und so weiter.",
        "Das sagt der physische Anatom, der Physiologe und so weiter.",
        "Geradeso können Sie aber den geistig-seelischen Menschen be­schreiben, der in dieser Weise sich eigentlich in die Löcher des Men­schen hereinerstreckt, in das, was mehr ist als Leere, in den Menschen hineinerstreckt.",
        "Sie können das ebenso beschreiben.",
        "Da müssen Sie dann nur angeben, aus was dieser geistig-seelische Mensch besteht.",
        "Und ebenso wie man beim physischen Menschen Organe unterschei­det, so kann man hier Strömungen unterscheiden.",
        "Man kann sagen: Hier, wo ich das Rot gezeichnet habe, würde der physische Mensch so im Profil drinnenstehen, hierher das Gesicht gerichtet haben, hier etwa die Augen (siehe Zeichnung); hier würde sein die Region der Begierdenglut (rot).",
        "Das würde ein Bestandteil des seelisch-geistigen Menschen sein, der seiner Substanz nach entnommen ist der Region, die Sie aus der «Theosophle» kennen als die Region der Begierden­glut.",
        "Also Begierdenglut, gewissermaßen etwas von ihr entnommen, in den Menschen hineinversetzt, gibt diese Partie des Menschen."
      ],
      [
        "Das, was ich hier lila gezeichnet habe, das würde ich bezeichnen müssen, wenn ich die Einzelheiten beschriebe, mit Seelenleben.",
        "Sie wissen, eine bestimmte Partie des Seelengebietes, des Seelenlandes, ist mit «Seelenleben» bezeichnet.",
        "Die Substanz daraus würde dieses Violette, dieses Lila sein, was im Menschen einen Teil des Geistig-Seelischen bildet.",
        "Das, was ich hier als orange bezeichnet habe, würden wir zu nennen haben, wenn wir diese Benennung beibehielten, tätige Seelenkraft.",
        "So daß Sie sich vorzustellen hätten: Dasjenige, was am intensivsten durch Ihre Sinne in Sie hineingeht beim Leben zwischen Geburt und Tod, das ist das Seelenleben; und dahinter, sich auch hin­stopfend, aber nicht so hineinkönnend, aufgehalten werdend durch das Seelenleben: tätige Seelenkraft.",
        "Und noch mehr dahinter dasjenige, was man nennen kann: Seelenlicht.",
        "Ich habe es hier gelb bezeichnet.",
        "Ziemlich anschließend an dieses Seelenlicht, sich so durchdrückend, würde dann das sein, was der Region von Lust und Unlust entnom­men ist.",
        "Das würde ich hier etwa dem grünen Gebiete zuzuschreiben haben (siehe Zeichnung).",
        "Dann würde dem schon bläulich werdenden"
      ],
      [
        "Gebiete zuzuschreiben sein: Wünsche.",
        "Und anstoßend nun hier das Blaue, schon wiederum mehr in das Blaurote hineingehend, das würde die Region ffießender Reizbarkeit sein.",
        "Das, was ich hier nenne Be­gierdenglut, fließende Reizbarkeit, Wünsche, das sind aurische Strö­mungen.",
        "Diese aurischen Strömungen konstituieren, wie Sie wissen, die Seelenwelt; sie konstituieren aber auch den seelisch-geistigen Menschen, der etwa so aufgebaut ist aus den Ingredienzien dieser Seelenwelt."
      ],
      [
        "# Bild s. 105"
      ],
      [
        "Wenn dann der Tod eintritt, dann ist das so, daß der physische Leib abfällt und der Mensch das fortnimmt, was sich durch seine Löcher in ihn hineinerstreckt hat.",
        "Er nimmt es nun fort.",
        "Dadurch, daß er es fortnimmt"
      ],
      [
        "- wir können uns diesen physischen Menschen wegdenken -, kommt nun der Mensch in eine gewisseVerwandtschaft mit der Seelen­weit, und dann auch mit dem Geisterland, wie Sie es ja in der «Theo­sophie» dargestellt finden.",
        "Er hat eine gewisse Verwandtschaft da­durch, daß er diese Ingredienzen in sich hat.",
        "Aber während des phy­sischen Lebens sind sie gebunden an den physischen Leib; dann werden sie frei.",
        "Dadurch aber, daß sie frei werden, verwandelt sich nach und nach das Ganze.",
        "Während es so war, daß sich - wenn ich jetzt die Differenzierungen weglasse und das Seelenleben so zeichne -während des physischen Lebens die Fühler (dunkel schraffiert) in un­sere Löcher hineinerstrecken, nehmen sich nach dem Tode diese Fühler zurück.",
        "Dadurch aber, daß sich die Fühler zurücknehmen, höhlt sich das Seelenleben selbst aus, und im Seelenleben drinnen geht das geistige Leben auf; von der andern Seite geht das geistige Leben auf (beIl schraffiert)."
      ],
      [
        "# Bild s. 106"
      ],
      [
        "In dem selben Maße, in welchem der Mensch aufhört unterzutau­chen in den physischen Leib, hellt sich auf sein Geistig-Seelisches, diese seine Aura von der andern Seite durchleuchtend.",
        "Und wie der Mensch ein Bewußtsein erlangen kann dadurch, daß beim Hinein-stoßen des Seelisch-Geistigen in den physischen Körper dieses immer anstößt und dadurch sich immer spiegelt, so bekommt der Mensch jetzt dadurch ein Bewußtsein, daß er sich zurückzieht gegen das Licht.",
        "Aber dies ist jenes Licht der Sonne, welches das erste Licht ist: das Gute.",
        "Während der Mensch also während seines physischen Lebens als geistig-seelisches Wesen gegen das Sonnenverwandte, nämlich gegen die überleeren Löcher im Gehirn stößt, stößt er, sich zurückziehend"
      ],
      [
        "nach dem Tode, nach der andern Sonne, nach der guten Sonne, nach der ersten Sonne."
      ],
      [
        "Sie sehen, wie zusammenhängt mit den Grundvorstellungen der uralten Mysterien die Möglichkeit, Begriffe zu erhalten von dem Leben zwischen dem Tod und einer neuen Geburt.",
        "Denn so stecken wir drinnen in diesem ganzen kosmischen Leben, wie ich es Ihnen jetzt in diesen Tagen dargestellt habe.",
        "Aber allerdings muß man, um richtige Begriffe von diesen Dingen zu bekommen, tiefer in das eigent­liche Gefüge der menschlichen Evolution durch die Erdenzeit hin­durch eingehen.",
        "Nicht wahr, es wäre ja möglich, daß jemand durch besonderen Glücksfall, wie man das so nennen könnte, hellsichtig das Ganze, was ich jetzt dargestellt habe, schaute.",
        "Aber der Glücksfall könnte nicht weiter gehen, als daß er sich verwandelnde Gebilde schaut.",
        "Etwa so: Nehmen wir an, ein Mensch würde durch irgendein Wunder - es geschieht schon nicht durch ein Wunder -, durch irgend etwas hellsichtig, übersinnlich schauend, so würde er schon, so ähnlich, wie ich es hier versucht habe aufzuzeichnen, das geistig-seelische Leben des Menschen sehen.",
        "Daß dies etwas anders ausschaut, als was ich vor einiger Zeit als Normalaura aufgezeichnet habe, das werden Sie begreiflich finden, wenn Sie verstehen, daß ich vor einigen Tagen das aufgezeichnet habe (siehe Seite 31), was sich als Aura ergibt, wenn man den ganzen Menschen sieht, also den physischen Menschen und die Aura ringsherum; jetzt habe ich aber herausgeholt den geistig­seelischen Menschen, so daß der geistig-seelische Mensch von dem physischen Menschen abstrahiert wird."
      ],
      [
        "Daran sehen Sie schon, daß man einmal so, das andere Mal anders die Farben setzen muß; daran sehen Sie auch, daß für das übersinn­liche Bewußtsein die Dinge sehr verschieden ausschauen.",
        "Nehmen Sie sich vor, die Aura des Menschen einfach so zu sehen, wie sie ist, indem der Mensch den physischen Leib hat, dann sehen Sie diese Aura - also wenn Sie sich vornehmen, abgesehen vom geistig-seelischen Men­schen jetzt den Menschen zu sehen, der nur seine Organe vorstreckt in den physischen Menschen hinein.",
        "Aber wenn Sie nun den Men­schen in der Zeit zwischen dem Tod und einer neuen Geburt sehen, da sehen Sie wiederum, wie sich das Ganze verwandelt.",
        "Da geht also"
      ],
      [
        "vor allen Dingen diese Region, die ich hier rot gezeichnet habe, weg von hier, geht hier herauf, das Gelbe geht hier herunter, das Ganze kommt nach und nach durcheinander.",
        "Man kann solche Dinge an­schauen, aber das Anschauen hat etwas Verwirrendes.",
        "Und daher werden sich auch für den neueren Menschen nicht leicht Möglich­keiten finden, Sinn und Bedeutung in dieses Verwirrende hineinzu­bringen, wenn er nicht zu andern Hilfsmitteln seine Zuflucht nimmt."
      ],
      [
        "Wir haben hingewiesen daranf, daß das Haupt des Menschen, der Kopf, auf die Vergangenheit weist, der Extremitätenmensch auf die Zukunft weist.",
        "Es ist ein vollständiger Gegensatz, polarisch; beides, das Haupt des Menschen und der Extremitätenmensch - erinnern Sie sich nur an dasjenige, was ich gestern auseinandergesetzt habe -, beide sind eigentlich ein und dasselbe; nur daß das Haupt eben eine sehr alte Bildung ist, eine Überbildung.",
        "Daher hat es auch die Löcher.",
        "Der Extremitätenmensch hat diese Löcher noch nicht; der ist eben noch ganz von Materie ausgefüllt.",
        "Löcher kriegen, das ist ein Zeichen von Überentwickelung.",
        "Rückgängige Entwickelung im Haupte sehen können, darauf kommt viel an.",
        "Und viel kommt darauf an, daß man verstehen kann: der Extremitätenmensch ist eine junge Metamor­phose, das Haupt ist eine alte Metamorphose.",
        "Und weil der Extremi­tätenmensch eine junge Metamorphose ist, kann er noch nicht hier im physischen Leben denken, sondern es bleibt sein Bewußtsein unbe­wußt.",
        "Er öffnet nicht dem geistig-seelischen Menschen solche Löcher wie das Gehirn."
      ],
      [
        "Das ist von unendlicher Wichtigkeit und wird in Zukunft immer wichtiger und wichtiger werden für die Geistes kultur: einzusehen so etwas, daß zwei Dinge, die äußerlich physisch ganz voneinander ver­schieden sind wie der Kopfmensch und der Extremitätenmensch, geistig-seelisch ein und dasselbe sind, nur der Zeit nach auf verschie­denen Entwickelungsstufen.",
        "Viele Geheimnisse liegen gerade in die­ser Tatsache, daß zwei physisch verschiedene Dinge dadurch, daß sie auf zeitlich verschiedenen Entwickelungsstufen stehen, eigentlich ein und dasselbe sein können.",
        "Sie sind äußerlich physisch etwas ganz Verschiedenes, aber Verwandlungszustände, also Metamorphosen eines und desselben."
      ],
      [
        "In elementarer Weise hat den Anfang mit Begriffen, durch die man so etwas erfassen kann, eben Goethe gemacht mit seiner Metamor­phosenlehre.",
        "Während sonst eigentlich in der Ausbildung der Be­griffe ein Stillstand ist seit alten Zeiten, setzt bei Goethe wiederum die Fähigkeit ein, Begriffe zu bilden."
      ],
      [
        "Und diese Begriffe sind die lebendi­gen Metamorphosenbegriffe.",
        "Goethe hat allerdings angefangen mit dem Einfachsten.",
        "Er hat gesagt: Wenn wir eine Pflanze anschauen, so haben wir das grüne Pflanzenblatt, aber das verwandelt sich dann in das farbige Blumenblatt."
      ],
      [
        "Beides ist ein und dasselbe, es sind nur Metamorphosen voneinander. - So wie das grüne Pflanzenblatt und das rote Rosenblatt verschiedene Metamorphosen sind, ein und das­selbe auf verscHedenen Stufen, so sind das Haupt des Menschen und der Extremitätenorganismus einfach Metamorphosen voneinander.",
        "Wenn wir den Goetheschen Metamorphosengedanken für die Pflanze nehmen, haben wir etwas Primitives, Einfaches; aber es kann dieser Gedanke fruchtbar gemacht werden für ein Höchstes: für das Be­schreiben des Überganges des Menschen von einer Inkarnation in die andere."
      ],
      [
        "Wir sehen eine Pflanze mit grünem Blatt und mit der Blüte und sagen: Die Blüte, die rote Rosenblüte ist umgewandelt aus dem grünen Pflanzenblatt.",
        "Wir sehen einen Menschen vor uns stehen und sagen: Das Haupt, das du trägst, das sind deine umgewandelten Arme, Hände, Beine, Füße aus der vorhergehenden Inkarnation; und das, was du jetzt an dir, wie Arme, Hände, Beine, Füße trägst, das wird sich umwandeln für die nächste Inkarnation in deinen Kopf."
      ],
      [
        "Aber jetzt kommt ein Einwand, der Ihnen offenbar in der Seele schwer sitzt.",
        "Jetzt werden Sie sagen: Ja, um Gottes willen, aber ich lasse doch meine Beine und meine Füße zurück, und meine Arme und meine Hände auch; die nehme ich doch nicht mit in die nächste In­karnation!",
        "Wie soll denn da mein Kopf daraus werden? - Nicht wahr, das kann man einwenden.",
        "Wiederum stehen Sie eben hier vor einer Maja.",
        "Es ist nämlich nicht wahr, daß Sie wirklich Ihre Beine und Ihre Füße, Ihre Hände und Ihre Arme zurücklassen.",
        "Das ist nämlich nicht wahr; das sagen Sie deshalb, weil Sie an der Maja, an der großen Täuschung hängenbleiben.",
        "Was Sie nämlich mit dern gewöhnlichen Bewußtsein Ihre Arme und Hände, Ihre Beine und Füße nennen, das"
      ],
      [
        "sind nicht Ihre Arme und Hände und Ihre Beine und Füße, sondern das ist dasjenige, was als Blut und andere Säfte Ihre Arme und Hände und Ihre Beine und Füße ausfüllt.",
        "Es ist hier wieder eine schwierige Vorstellung, aber es ist so."
      ],
      [
        "Nehmen Sie an, hier haben Sie Arme und Hände, Beine und Füße; aber das, was hier ist, ist geistig, das sind geistige Kräfte.",
        "Bitte, stellen"
      ],
      [
        "# Bild s. 110"
      ],
      [
        "Sie sich vor: Ihre Arme und Hände, Ihre Beine und Füße seien Kräfte, übersinnliche Kräfte.",
        "Würden Sie nur sie haben, Sie würden sie nicht mit den Augen sehen.",
        "Sie sind angefüllt, diese Kräfte sind angefüllt mit den Säften, mit dem Blute, und das, was als mineralische Masse, flüssig oder zum Teil fest, zum geringsten Teile fest, Unsichtbares ausfüllt, das sehen Sie (schraffiert).",
        "Was Sie im Grabe lassen, was ver­brannt wird, das sind nur, ich möchte sagen, die mineralischen Ein­schlüsse.",
        "Ihre Arme und Hände, Ihre Beine und Füße sind nicht sicht­bare Füße, sind Kräfte, und diese nehmen Sie mit.",
        "Die Formen neh­men Sie mit.",
        "Sie sagen: Ich habe Hände und Füße. - Derjenige, der in die geistigen Welten hineinsieht, der sagt nicht: Ich habe Hände"
      ],
      [
        "und Füße -, sondern er sagt: Es gibt Geister der Form, Elohim, die denken kosmisch, und deren Gedanken sind meine Arme und Hände und Beine und Füße; und deren Gedanken sind mit Blut und andern Säften ausgefüllt. - Aber Blut und andere Säfte sind auch wiederum nicht das, als was sie im Physischen erscheinen; diese Stoffe sind wie­derum die Vorstellungen der Geister der Weisheit, und dasjenige, was der Physiker Stoff nennt, das ist nur der äußere Schein.",
        "Wo der Physiker den Stoff hinsetzt, müßte er sagen: Da stoße ich auf einen Gedanken der Geister der Weisheit, der Kyriotetes."
      ],
      [
        "Und wo Sie Arme und Hände, Beine und Füße sehen, da können Sie nicht einmal darauf stoßen, da müssen Sie sagen: Hier bilden die kosmischen Ge­danken der Geister der Form meine Formen. - Kurz, so sonderbar das klingt: Ihren Körper gibt es ja gar nicht, sondern da, wo im Raume Ihr Körper ist, da leben durcheinander die kosmischen Ge­danken der höheren Hierarchien.",
        "Und würden Sie nicht der Maja ge­mäß, sondern richtig sehen, so würden Sie sagen: Hier erstrecken sich herein die kosmischen Gedanken der Exusial, der Geister der Form, der Elohim."
      ],
      [
        "Diese kosmischen Gedanken machen sich mir sichtbar, indem sie ausgefüllt sind mit den kosmischen Gedanken der Geister der Weisheit.",
        "Das gibt Arme und Hände, Beine und Füße.",
        "Gar nicht steht das da, als was es in der Maja erscheint, vor dern geistigen Blicke, sondern da stehen die kosmischen Gedanken, und diese kosmischen Gedanken ballen sich zusammen, kondensieren sich, schieben sich ineinander, und daher erscheinen sie uns als diese Schattenfigur, als die wir herumgehen, von der wir glauben, daß sie wirklich ist."
      ],
      [
        "Also den physischen Menschen, den gibt es gar nicht."
      ],
      [
        "Wir können mit einem gewissen Recht sagen: In der Stunde des Todes scheiden die Geister der Form ihre kosmischen Gedanken von den kosmischen Gedanken der Geister der Weisheit.",
        "Die Geister der Form nehmen ihre Gedanken in die Luft hinauf, die Geister der Weis­heit senken ihre stofflichen Gedanken in die Erde hinein.",
        "Dadurch ist im Leichnam so ein Nachschatten von den Gedanken der Geister der Weisheit noch vorhanden, wenn die Geister der Form ihre Gedanken zurückgenommen haben in die Luft.",
        "Das ist der physische Tod; das ist er in Wahrheit."
      ],
      [
        "Kurz, wenn wir anfangen, über Wirklichkeiten zu denken, so kom­men wir zu einer Auflösung desjenigen, was gewöhnlich die physische Welt genannt wird.",
        "Denn diese physische Welt besteht dadurch, daß die Geister der höheren Hierarchien ihre Gedanken ineinander-schieben, und deshalb - bitte stellen Sie sich vor: fein verteilte Wasser-partien gehen irgendwo hinein und bilden einen dichten Nebel - er­scheint Ihr Leib auch so als ein Schattengebilde, weil die Gedanken der Geister der Form hineindringen in die Gedanken der Geister der Weisheit, die Formgedanken in die Stoffgedanken hineingehen.",
        "Die ganze Welt löst sich vor dieser Anschauung in Geistiges auf.",
        "Aber man muß die Möglichkeit haben, die Welt wirklich geistig vorzu­stellen, zu wissen: Das ist nur etwas ganz Scheinbares, daß meine Arme und Hände, meine Füße und Beine der Erde übergeben werden.",
        "In Wirklichkeit beginnt da die Metamorphose meiner Arme und Beine, Hände und Füße und vollendet sich in dem Leben zwischen dem Tod und einer neuen Geburt, und meine Arme und Beine, Hände und Füße werden mein Kopf in der nächsten Inkarnation."
      ],
      [
        "Ich habe Ihnen mancherlei jetzt gesprochen, was Sie wenigstens in der Form vielleicht etwas sonderbar berührt hat.",
        "Aber was ist denn das schließlich, was wir da besprochen haben, anderes, als daß wir vom scheinbaren Menschen aufsteigen zum wahren Menschen, von dem, was äußerlich in der Maja lebt, aufsteigen zu der Stufenfolge der Hierarchien?",
        "Nur wenn man das tut, kann man in einer reifen Form heute davon sprechen, daß der Mensch in sich wissen darf ein soge­nanntes höheres Selbst.",
        "Wenn man bloß daklamiert von dem höheren Selbst, wenn man bloß sagt: Ich fühle in mir ein höheres Selbst - da ist dieses höhere Selbst ein reines leeres Abstraktum, da hat es keinen Inhalt; denn das gewöhnliche Selbst gehört der Maja an, ist also selbst Maja.",
        "Das höhere Selbst hat nur einen Sinn, wenn man von ihm spricht gegenüber der Welt der höheren Hierarchien.",
        "Vom höheren Selbst zu sprechen, ohne auf die Welt Rücksicht zu nehmen, die da besteht aus den Geistern der Form und den Engeln, Erzengeln und so weiter, vom höheren Selbst zu sprechen, ohne auf diese Welt Rücksicht zu nehmen, bedeutet: man spricht von leeren Abstrak­tionen, bedeutet zugleich: man spricht nicht von demjenigen, was da"
      ],
      [
        "lebt im Menschen zwischen dem Tod und einer neuen Geburt.",
        "Denn so wie wir hier mit Tieren, Pflanzen und Mineralien leben, so leben wir zwischen dem Tod und einer neuen Geburt mit den Reichen der höheren Hierarchien, von denen wir oftmals gesprochen haben.",
        "Nur wenn man sich nach und nach diesen Vorstellungen und Be­griffen nähert, dann - wir werden davon erst vielleicht in acht Tagen sprechen-, dann kommt man zu einer Annäherung an so etwas, was Ant­wort geben kann auf die Frage: Warum sterben manche Menschen als junge Kinder, warum manche im höchsten Alter, andere dazwischen?"
      ],
      [
        "Was ich Ihnen jetzt skizzenhaft dargestellt habe, sind konkrete Be­griffe für die Wirklichkeiten der Welt.",
        "Es sind ja wahrhaftig nicht abstrakte Begriffe, die ich Ihnen dargestellt habe, es sind konkrete Begriffe für die Wirklichkeiten der Welt.",
        "Diese konkreten Begriffe, sie gab es, allerdings für ein mehr atavistisches Anschauen, in den alten Mysterien.",
        "Sie sind für das menschliche Anschauen verloren­gegangen von dem 8. vorchristlichen Jahrhundert an; sie müssen durch eine Vertiefung in der Auffassung des Christus-Wesens wieder­um gewonnen werden.",
        "Das kann nur auf geisteswissenschaftlichem Wege geschehen."
      ],
      [
        "Verschaffen wir uns von einem gewissen Gesichtspunkte aus noch einmal eine Art Vorstellung von der Menschheitsevolution.",
        "Wir wollen jetzt sehr, sehr wichtige Begriffe ins Auge fassen.",
        "Da kann man sagen: Wenn man zurückgeht in der Menschheitsentwickelung, da kommt man - ich habe ja das öfter dargestellt - darauf, daß in alten Zeiten die Menschen mehr Gruppenseelen hatten und sich dann erst die individuellen Seelen hineingliederten in das Gruppenseelentum.",
        "Sie können das in verschiedenen Zyklen lesen.",
        "Dann könnte man schematisch die Entwickelung der Menschheit so darstellen, daß man sagt: In alten Zeiten gab es Gruppenseelen; jede dieser Gruppenseelen spaltete sich wiederum - das würde für eine bloße seelische An­schauung sein, für eine geistige wäre es etwas anders -, aber jede solche Seele umlileidet sich mit einem Leibe, den ich hier in der Form mit einem roten Strich andeute (siehe Zeichnung Seite 114)."
      ],
      [
        "Diese Zeichnung oder etwas ähnliches wie diese Zeichnung hat man noch bis in die Pythagoräische Schule hinein immer gemacht, indem"
      ],
      [
        "# Bild s. 114"
      ],
      [
        "man gesagt hat: Seht ihr die Leiber an, den Leibern nach sind die Menschen getrennt, jeder für sich ein Leib - daher sind die roten Striche hier isoliert -, den Seelen nach findet man aber eine Einheit der Menschheit, indem man hinaufgeht bis zur Gruppenseele, die allerdings weit zurückliegt. - Man hat eine Einheit.",
        "Wenn Sie sich das Rote wegdenken, so bildet das heller Schraffierte eine einheitliche Figur."
      ],
      [
        "Aber es hat nur einen Sinn, über diese Figur zu sprechen, wenn man zuerst von dem Geistigen so gesprochen hat, wie wir es heute getan haben; denn dann weiß man, was in diesen Seelen alles mitwirkt, wie die höheren Hierarchien mitwirken an diesem Seelischen.",
        "Es hat keinen Sinn, von dieser Figur zu sprechen, wenn man nicht im Hin­blick auf die Hierarchien spricht.",
        "So hat man auch gesprochen bis in die Pythagoräische Schule herein, und aus den Pythagoräischen Schu­len hat wiederum Apollonius dasjenige gelernt, wovon ich gestern ge­sprochen habe, von dem ich in der nächsten Woche weiter sprechen werde.",
        "Dann aber, seit dem 8. vorchristlichen Jahrhundert - schon die Pythagoräischen Schulen waren Nachzügler -, hat sich die Möglich­keit, so zu sprechen, verloren.",
        "Und allmählich sind die Begriffe, die konkret sind, die wirklich sind, wenn sie sich auf die höheren Hierar­chien beziehen, den Leuten konfus geworden, verschwommen ge­worden.",
        "Und so ist ihnen statt der Welt der Engel, Erzengel, Ur­kräfte, Formen, Bewegungen, Weisheiten, Throne, statt all diesem konkreten Geistweben ist ihnen ein Begriff gekommen, der nun schon in der griechischen Anschauung eine gewisse Rolle spielt: der Begriff"
      ],
      [
        "des Pneuma, in dem alles durcheinander schwimmt.",
        "Pneuma, allge­meiner Geist - dieser verschwommene Begriff, den noch heute die Pantheisten lieben: Geist, Geist, Geist, Geist!",
        "Ich habe öfter davon gesprochen, daß die Pantheisten überall den Geist hinsetzen.",
        "Aber das geht schon im griechischen Leben auf.",
        "Da hat man wieder diese Figur gezeichnet; aber Sie sehen: Was früher konkret war - die Fülle der Gottheiten-, ist zum abstrakten Begriff geworden, ist zum Pneuma geworden.",
        "Das Weiße ist das Pneuma, das Rote ist die physische Materie (siehe Zeichnung Seite 114), wenn man die Menschenevo­lution in Betracht zieht.",
        "Aber von diesem Pneuma, von dem haben die Griechen wenigstens noch eine Anschauung gehabt, denn sie haben immerhin noch etwas Aurisches gesehen; so daß also das, was sie sich da in dem weißen Gezweige vorstellten, für sie noch etwas Aurisches, also etwas wirklich Anschauliches war.",
        "Das ist die große Bedeutung des Überganges vom Griechentum ins Römertum, daß die Griechen in ihrer Anschauung noch das Pneuma als wirkliches Geistiges erlebt haben, die Römer nicht mehr.",
        "Bei den Römern ist es schon ganz abstrakt geworden, vollständige Abstraktion geworden, bloße Begriffe.",
        "Die Römer sind das Volk der abstrakten Begriffe."
      ],
      [
        "Meine lieben Freunde, in der neueren Zeit finden Sie in der Natur­wissenschaft wiederum dasselbe Schema !",
        "Sie können es heute in materialistischen naturwissenschaftlichen Büchern aufschlagen: da finden Sie ganz genau dieses Schema, das Sie in den alten Mysterien aufgezeichnet gefunden haben, in den Pythagoräischen Schulen, wo alles noch auf die Hierarchien bezüglich war.",
        "Sie haben es bei den Griechen, wo es auf das Pneuma bezüglich war; Sie finden es heute wieder gezeichnet.",
        "Wir werden sehen, was es heute ist.",
        "Heute sagt der Naturforscher, indem er diese selbe Zeichnung seinen Schülern auf die Tafel zeichnet: Indem das Menschengeschlecht sich fort-pflanzt, geht die Keimsubstanz der Eltern über auf die Kinder; ein Teil der Keimsubstanz bleibt aber so erhalten, daß er in der nächsten Generation wiederum auf die Kinder übergehen kann, und von dem bleibt wiederum ein Teil so, daß er wieder auf die Kinder über­gehen kann, während ein anderer Teil der Keimsubstanz die Zellen des physischen Leibes bildet. - Sie haben ganz dasselbe Schema, nur"
      ],
      [
        "sieht der heutige Naturforscher in dern Weißen (siehe Zeichnung) die Kontinuität der Keimsubstanz.",
        "Er sagt: Wenn wir zu den alten Men­schenvorfahren hinaufgehen und ihre Keimsubstanz nehmen, die männliche und die weibliche Keimsubstanz nehmen, und gehen zu den jetzigen Menschen herunter und nehmen ihre jetzige Keimsub­stanz, so ist das ein einziger Strom; die Keimsubstanz ist kontinuier­lich.",
        "Es bleibt immer in der Keimsubstanz etwas ewig - so stellt es sich der Naturforscher vor - und nur gewissermaßen die Hälfte des Keimplasmas geht über in die andere Körperlichkeit. - Der Natur-forscher hat wiederum dieselbe Figur, nur hat er jetzt nicht mehr das Pneuma, sondern das Weiße, das ist ihm jetzt die materielle Keimsub­stanz.",
        "Es ist nichts Seelisch-Geistiges mehr, es ist ihm die materielle Keimsubstanz.",
        "Das können Sie bei den heutigen Naturforschern lesen, das nimmt man heute an als eine große, bedeutsame Entdeckung.",
        "Das ist Materialisierung einer hochgeistigen Vorstellung, indem sie durch die Abstraktion durchgegangen ist; der abstrakte Begriff steht mitten drinnen.",
        "Und drollig ist es, daß ein Naturgelehrter der neue­ren Zeit ein Buch geschrieben hat - für jemanden, der ordentlich denken kann, ist es drollig -, in welchem er geradezu sagt: Was die Griechen sich noch unter Pneuma vorgestellt haben, ist heute die kontinuierlich bleibende Keimsubstanz. - Ja, es ist närrisch, aber es ist heute hohe Weisheit."
      ],
      [
        "Aber Sie sehen daraus eines: die Zeichnung macht es nicht !",
        "Und Sie werden daraus begreifen, warum ich immer in einer gewissen Weise mich gewendet habe gegen das Aufzeichnen von Schemen, solange wir noch versuchten, unsere Anthroposophie durch die Theo­sophische Gesellschaft durchzutragen.",
        "Man brauchte nur in irgend­einen theo sophischen Zweig einzutreten: die Wände waren in der Regel behängt mit allerlei solchen Schemen.",
        "Da war alles mögliche aufgezeichnet, da standen dann Worte dabei, und da waren ganze Stammbäume und alles mögliche aufgezeichnet.",
        "Aber auf diese Zeichnungen kommt es nicht an, sondern es kommt darauf an, daß man wirklich zu dern lebendigen Vorstellen gehen kann; denn die Zeichnung kann ganz dieselbe sein, ob Sie sie als Ausfluß der Hier­archien, Geistig-Seelisches sich vorstellen, oder ob Sie sich das kontinuierliche"
      ],
      [
        "Keimplasma, eine reine Materie, vorstellen.",
        "Diese Dinge verschwimmen dern heutigen Menschen.",
        "Daher ist es so wichtig, sich klar darüber zu sein, wie der Grieche noch etwas gewußt hat von dern realen Selbst im Menschen, von dern realen Geistigen, und wie das beim Römer in den abstrakten Begriff übergegangen ist.",
        "Sie können das an Äußerlichkeiten sehen.",
        "Indem der Grieche von seinen Göttern redet, redet er so, daß man ganz genau sieht: der Grieche denkt sich noch konkrete Figuren hinter den Göttern.",
        "Beim Römer sind die Götter im Grunde nur noch Namen, nur Bezeichnungen, sind Ab­straktionen und werden immer mehr Abstraktionen.",
        "Beim Griechen war immer noch eine gewisse Vorstellung vorhanden, daß in dern Menschen, der hier steht, die Hierarchien leben, und in jedem Men­schen verschieden die Hierarchien leben.",
        "Der Grieche nahm den Menschen seiner Realität nach, und wenn er sprach: Das ist der Alki­biades, das ist der Sokrates, das ist der Plato -, so hatte er noch den Begriff: da in den Alkibiades, in den Sokrates, in den Plato, da ragen herein die kosmischen Gedanken der Hierarchien in verschiedener Weise, und dadurch, daß da die kosmischen Gedanken in verschie­dener Weise hereinragen, treten so verschiedene Figuren aufl"
      ],
      [
        "Das ging beim Römer verloren.",
        "Daher bildete sich beim Römer ein System von Begriffen aus, das sein Extrem darinnen hat, daß von Augustus an - eigentlich schon früher - der römische Cäsar selber als Gott galt.",
        "Die Gottheit war allmählich verabstrahiert, und der rö­mische Cäsar war selber ein Gott, weil der Begriff vollständig abstrakt geworden war.",
        "Aber so abstrakt wurden auch die andern Begriffe.",
        "So abstrakt wurden namentlich die Begriffe, die als Rechtsbegriffe, als moralische Begriffe das römische Wesen durchsetzten, und so trat an die Stelle von alten Lebendigkeiten eine Summe von Abstraktio­nen.",
        "Und diese Summe von Abstraktionen, die ist als Erbschaft ge­blieben durch das ganze Mittelalter hindurch, ist auf die neuere Zeit heraufgekommen, ist bis in das 19.",
        "Jahrhundert herein als Erbschaft geblieben: abstrakte Begriffe, die überall hineingetragen werden."
      ],
      [
        "Da kam etwas Überraschendes im 19.",
        "Jahrhundert.",
        "Unter den ab­strakten Begriffen hat man den Menschen vollständig verloren ge­habt.",
        "Der Grieche ahnte noch etwas von dern wirklichen Menschen,"
      ],
      [
        "der aus dem Kosmos herein gebildet wird; durch das Römertum hin­durch ist der Mensch verlorengegangen.",
        "Das 19.",
        "Jahrhundert war genötigt, ihn wieder zu entdecken durch alle die Verhältnisse, auf die ich Sie schon hingewiesen habe, auf die ich Sie noch genauer hin­weisen werde."
      ],
      [
        "Und die Entdeckung des Menschen, die geschah jetzt von dem andern Pol aus.",
        "Das Griechentum hat sehen wollen den Menschen, der aus der Hierarchie kommt, den göttlichen Menschen; die Römer haben an die Stelle eine Reihe von abstrakten Begriffen gesetzt; das 19."
      ],
      [
        "Jahrhundert, schon das 18.",
        "Jahrhundert, aber nament­lich das 19.",
        "Jahrhundert war genötigt, den Menschen von der andern Seite, von seiner Tierseite aus wieder zu entdecken.",
        "Und da konnte er jetzt nicht gefaßt werden mit diesen abstrakten Begriffen."
      ],
      [
        "Das war der große Schock.",
        "Und das ist der große Schock, das ist die tiefe Kluft, die entsteht: Was ist denn das eigentlich, was da auf zwei Beinen vor uns steht und mit den Händen fuchtelt und allerlei ißt und trinkt, was ist denn das?"
      ],
      [
        "Die Griechen haben es noch gewußt; dann ist es in abstrakte Begriffe verwandelt worden.",
        "Jetzt überrascht es die Men­schen im 19.",
        "Jahrhundert; da steht es, aber man hat keine Begriffe, es zu fassen.",
        "Man faßt es als bloßes höheres Tier auf: es wird auf der einen Seite der Darwinismus, naturwissenschaftlich, auf der andern Seite, im Geistigen, der Sozialismus, der den Menschen nur als Tier in die Sozietät hineinstellen will."
      ],
      [
        "Es ist der Mensch, der vor sich selber überrascht steht: Was ist denn das eigentlich? - und der ohn­mächtig ist, diese Frage zu beantworten."
      ],
      [
        "Das ist die Situation von heute, das ist die Situation, die nicht nur, je nachdem die Menschen es wollen, richtige oder unrichtige Be­griffe schaffen wird, sondern die dazu berufen ist, katastrophale oder heilsame Tatsachen zu schaffen.",
        "Aber das ist sie, die Situation: der Schock, den der Mensch vor sich selber hat.",
        "Wiederum müssen die Elemente zum Begreifen des geistigen Menschen gefunden werden.",
        "Man wird sie nicht anders finden, als wenn man auf die Metamor­phosenlehre eingeht.",
        "Da liegt der wesentliche Punkt.",
        "Die Metamor­phosenbegriffe des Goetheanismus sind allein imstande, die fluk­tuierenden Erscheinungen zu fassen, welche sich dem Anschauen der Wirklichkeit darbieten."
      ],
      [
        "Nun, nach dieser Richtung, möchte ich sagen, schob die geistige Ent­wickelung schon immer.",
        "Auch damals - ich habe das im «Reich» in einer Reihe von Aufsätzen über «Die chymische Hochzeit des Christian Rosen­kreutz» angedeutet-, als im 17.",
        "Jahrhundert «Die chymische Hochzeit» und andere Schriften auf so wunderbare Weise veröffentlicht worden sind, da war schon das Bestreben, vorzusorgen, daß eine solche soziale Struktur, die der wahren Wesenheit des Menschen entspricht, unter die Menschen kommen sollte.",
        "Auf diese Weise ist ja «Die chymische Hoch­zeit des Christian Rosenkreutz» von dem sogenannten Valentin Andreae entstanden.",
        "Aber auf der andern Seite ist ja auch das Buch entstanden, das er nannte «Allgemeine Reformation der ganzen weiten Welt», wo er einen großen politischen Überblick gibt, wie die sozialen Verhältnisse werden sollen.",
        "Der Dreißigjährige Krieg hat die Sache hinweggefegt."
      ],
      [
        "Dort ist es der Dreißigjährige Krieg, der die Dinge hinweggefegt hat.",
        "Heute ist es möglich, daß die Weltordnung entweder dahin geht, die Dinge wirklich wiederum hinwegzufegen, oder aber sie in die Menschheitsentwickelung hineinzunehmen.",
        "Damit berühren wir die große Grundfrage der Gegenwart, mit der sich die Menschen be­schäftigen sollten, statt mit all den sekundären Fragen, mit denen sich die Menschen heute beschäftigen.",
        "Würden sich die Menschen mit die­ser Grundfrage beschäftigen, dann würden sie die Mittel und Wege finden, fruchtbare Begriffe in die heutige Wirklichkeit hineinzutragen; dann würde man meiden die abstrakten Begriffe."
      ],
      [
        "Es ist nicht so leicht, Wirklichkeit von Täuschung zu unterscheiden.",
        "Da muß man schon wirklich im Ernste und mit allem guten Willen ins Leben hinein wollen, nicht bei Programmen und bei Vorurtellen Halt machen wollen.",
        "Nach dieser Richtung könnte ich ja vieles er­zählen.",
        "Ich will nur ein Faktum anführen: Im Beginne der neunziger Jahre, da traten eine Anzahl von Menschen zusammen in den ver­schiedensten Städten in Europa und machten wiederum einmal etwas Amerikanisches nach: nämlich die «Bewegung für ethische Kultur».",
        "Es war dazumal unter gewissen Intellektuellen alles darauf aus, «Ge­sellschaften für ethische Kultur» zu gründen.",
        "Die Leute haben sehr schöne Sachen vorgebracht, und wenn Sie heute noch die Auf­sätze lesen, die dazumal von diesen Vertretern der Gesellschaften für"
      ],
      [
        "ethische Kultur geschrieben worden sind, wenn Sie Sinn haben für"
      ],
      [
        "- ja, butteriges Zeug, so werden Sie wahrscheinlich heute noch ent­zückt sein können von all den schönen, wunderschönen Idealen, in denen die Leute dazumal geschwelgt haben.",
        "Und es war wahrhaftig keine angenehme Aufgabe, sich gegen dieses Schwelgen in den but­terigen Idealen zu wenden."
      ],
      [
        "Ich schrieb aber dazumal in einer der ersten Nummern der Zeitschrift «Die Zukunft» einen Artikel gegen dieses ganze butterige Zeug von der «ethischen Kultur», schimpfte mordsmäßig über diese «ethische Kultur».",
        "Es war selbstverständlich eine schändliche Tat, denn wie könnte es nicht etwas Schändliches sein, wenn man sich gegen etwas so Gutes wendet, wenn die Leute daran gehen, die ganze Welt zu ethisieren, durchaumoralisieren !"
      ],
      [
        "Ich lebte dazumal in Weimar, kam aber einmal nach Berlin, sprach auch mit Herman Grimm; der sagte: Was wollen Sie denn eigentlich mit dieser «ethischen KultuD>?",
        "Gehen Sie doch hin zu den Leuten, Sie werden sehen: die in Berlin hier zusammenkommen, diese Ethiker sind lauter recht nette, liebe Leute."
      ],
      [
        "Man kann gegen sie gar nichts haben.",
        "Es sind Leute, die einem ganz sympathisch sein können, die einem ganz gut gefallen können. - Das war auch gar nicht zu leugnen, und für den damaligen Moment hatte selbstverständlich Herman Grimm ebenso recht wie ich."
      ],
      [
        "Äußerlich genommen hatte der eine ebenso recht für den Moment wie der andere; das eine ließ sich eben­sogut beweisen wie das andere, und ich will gar nicht behaupten, daß rein logisch meine Gründe gegen die Ethiker besser waren als die Gründe, die die Ethiker vorgebracht haben.",
        "Aber aus all diesem Butteridealismus ist ja die gegenwärtige Katastrophe hervorgegan­gen, und nur diejenigen Menschen hatten recht und sind durch die Tatsachen gerechtfertigt, die dazumal gesagt haben: Mit all eurem Schwelgen und Reden von irgend solchen Butteridealen, durch die ihr allgemeinen Frieden und dergleichen und allgemeine Moral unter die Menschen bringen wollt, erzeugt ihr nichts anderes als das, was ich dann das soziale Karzinom genannt habe, was endlich in diese katastrophale Gegenwart hineinführen mußte."
      ],
      [
        "Die Zeit hat gezeigt, wer mit realen Begriffen arbeitete und wer mit bloßen Abstraktionen arbeitete.",
        "Nach dem bloßen abstrakten Charakter kann man gar nicht"
      ],
      [
        "entscheiden, ob irgend jemand recht oder unrecht hat; das entschei­det bloß das, ob irdendein Begriff richtig sich hineinfügt in den Gang der Tatsachen oder nicht.",
        "Wenn ein Professor an seiner Universität heute Naturwissenschaft lehrt, dann kann er selbstverständlich wun­derschön beweisen, logisch beweisen, daß das alles richtig ist, was er sagt."
      ],
      [
        "Das geht auch alles in die Löcher der Köpfe hinein; das darf ich ja natürlich im allerbesten Sinne heute sagen.",
        "Und siehe da, darum handelt es sich aber nicht, ob scheinbare gute logische Gründe dafür anzuführen sind, sondern: dieselben Gedanken dann in einen Lenin­Kopf hineingesenkt, werden Bolschewismus."
      ],
      [
        "Was ein Gedanke in der Wirklichkeit wird, darauf kommt es an.",
        "Nicht darauf kommt es an, was man über ihn denken kann, was man über ihn abstrakt fühlen kann, sondern darauf, welche Kraft in der Wirklichkeit einen Gedan­ken bildet."
      ],
      [
        "Und wenn man diejenige Weltanschauung, von der am meisten in der neueren Zeit gesprochen worden ist, weil die andern ästhetisierend waren, wie ich gestern ausgeführt habe, wenn man den Sozialismus prüft, so handelt es sich heute nicht darum, sich nun hin-zusetzen, um den Karl Marx oder Lassalle oder den Bernstein zu «ochsen», also deren Bücher zu studieren, diese Autoren zu studieren, sondern darum handelt es sich, ein Gefühl, eine lebendige Erfahrung dafür zu haben, was im Fortgang der Menschheit dann wird, wenn eine Anzahl von Menschen - solche Menschen, die an Maschinen stehen - diesen Gedanken haben.",
        "Darauf kommt es an, und nicht darauf, über die soziale Struktur der nächsten Zukunft die Gedanken zu haben, die man im landläufigen Gang der heutigen diplomatischen Schulung lehrt."
      ],
      [
        "Sondern jetzt ist die Zeit, wo es darauf ankommt, Gedanken wägen zu können, um sich die Frage beantworten zu kön­nen: Was will die Zeit in den nächsten Jahrzehnten?",
        "Es ist heute schon einmal die Zeit gekommen, wo die Bequemlichkeit nicht ge­stattet ist, auf den verschiedensten kurulischen Stühlen zu sitzen und bequem das Alte fortaupflegen, sondern die Zeit ist gekommen, wo die Menschheit den Schock vor sich selbst fühlen muß, und wo bei denen, die irgendwo verantwortlich sind für irgend etwas, der Ge­danke auftauchen muß: Wie löst man diese Frage aus dem geistigen Leben heraus?"
      ],
      [
        "Wir werden das nächste mal davon weiter sprechen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SIEBENTER VORTRAG Dornach, 31. August 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Ich habe in der letzten Zeit hier eine Reihe von wichtigen Tatsachen über den Menschen vorgebracht, die geisteswissenschaftlich erforscht werden können. Ich lege weniger Wert darauf, daß die Einzelheiten dieser Tatsachen aufgefaßt werden - denn ich habe mich ja über die Natur dieser Tatsachen öfter ausgesprochen-, als vielmehr darauf, daß ein gewisser Eindruck durch diese Tatsachen erweckt werde: der Ein-druck über das Wesen desjenigen, was man die Täuschung der physischen Außenwelt nennen kann, auf daß Sie ein Gefühi davon erhalten, was eigentlich gemeint ist, wenn man davon spricht: Die Außenwelt, so wie wir sie um uns herum sehen - ich sage sehen, nicht haben -, ist Täuschung zunächst, und hinter ihr liegt die wahre, die wirkliche Welt. Und ich wollte ein gründlicheres Gefühi hervorrufen von dem, was gemeint ist, wenn man auf dem Boden der Geistes-wissenschaft von der wirklichen Welt spricht. Also mehr um diese allgemeinen Gefühie handelt es sich. Und damit bin ich an demjenigen Punkte angelangt, wo wir gewissermaßen wiederum eine Möglichkeit haben, unsere geisteswissenschaftlichen Betrachtungen anzuknüpfen an wichtige, an bedeutsame Interessen im Geistesleben der Gegen­wart, wobei ich natürlich an eine weitere Gegenwart denke, nicht bloß an die heutigen Tage, sondern an die Jahrhunderte, in denen wir leben.",
      "Unser Geistesleben ist in einem Zwiespalt begriffen, in einem Zwiespalt, den man in der verschiedensten Weise charakterisieren kann, den man so oder so definieren kann. Aber alle diese Definitionen müssen zuletzt wiederum zusammenlaufen in eine Art Empfindung für zwei Strömungen, die wir uns als Ideenströmungen bilden müssen aus der Geisteskultur der Gegenwart heraus, und die gewissermaßen sich nicht recht vereinigen lassen. Zwei Strömungen von Ideen sind vorhanden. Die eine, man kann sie im weitesten Sinne nennen die naturwissenschaftliche Strömung, wobei ich nicht etwa bloß das meine, was in den Kreisen der Naturforscher gedacht und behauptet wird, sondern jene naturwissenschaftliche Strömung, welche heute ja",
      "mehr oder weniger in der Empfindung der ganzen Menschheit lebt. Diese naturwissenschaftliche Strömung ist nach und nach eine popu­läre, eine weitverbreitete Anschauung geworden. Sie produziert Be­griffe, die tief, tief sich eingewurzelt haben in das Seelenleben der Menschen der Gegenwart.",
      "Man kann am besten sehen, wie diese na­turwissenschaftliche Weltanschauung sich eingewurzelt hat, wenn man bedenkt, daß sie da am tiefsten Wurzel gefaßt hat, wo man glaubt, an spirituelles Leben heranzudringen. Schließlich ist ja dasjenige, was man landläufig Spiritismus nennt und was von sehr vielen als theo­sophische Theorie vertreten wird, nichts anderes als ein Ausfluß ma­terialistischer Weltanschauung.",
      "Dasjenige, was man zumeist an Be­griffen hat über Ätherleib, Astralleib, dasjenige, was man experimen­tell produziert in spiritistischen Sitzungen, wird ganz und gar einge­fangen in Begriffe, welche der naturwissenschaftlichen Weltanschauung entlehnt sind, was am besten solche Leute beweisen wie zum Beispiel du Prel, der glaubt, gerade auf die Geisteswelt loszugehen. Aber alles dasjenige, was er über die Geisteswelt sagt, denkt er in naturwissen­schaftlichen Begriffen, das heißt in solchen Begriffen, in denen man bloß über die Natur denken sollte, nicht über den Geist.",
      "Ebenso ist es geradezu auffällig, wie materialistisch doch die Theorien der mei­sten Theosophen sind, wie sie sich geradezu bemühen, Vorstellungen wie Ätherleib oder selbst Astralleib an die naturwissenschaftlichen Begriffe, die man nur auf die Natur anwenden sollte, heranzurücken. Der Ätherleib wird sehr häufig vorgestellt als etwas ganz Materielles, als ein feiner Dunst oder dergleichen.",
      "Nun, ich habe mich ja über diese Dinge öfter ausgesprochen.",
      "Dies ist die eine, ich möchte sagen Begriffsmasse, die wir haben:",
      "die naturwissenschaftlichen Begriffe. Und weniger Wert - ich betone das noch einmal, damit ich nicht mißverstanden werde - ist darauf zu legen, daß diese naturwissenschaftlichen Begriffe in den Naturwissen­schaften selbst sich finden, wo sie ja zum großen Teil berechtigt sind, sondern das Wichtige ist, daß sie sich eben einschieichen in die allge­meine Weltanschauung, und daß sie verwendet werden, um Spiri­tuelles begreifen zu wollen, ja, daß manche geradezu in dem Wahne leben, sie sagten etwas Besonderes, wenn sie die Ähnlichkeit der Begriffe,",
      "die sie im Spirituellen haben, mit den naturwissenschaftlichen Begriffen hervorheben.",
      "Die bedeutsame Tatsache, die wir da ins Auge fassen müssen, ist diese, daß diese naturwissenschaftlichen Begriffe nur eine gewisse Sphäre unserer Welt, eine gewisse Sphäre der Welt, in der wir leben, einfangen können in unser Verständnis, daß eine andere Welt außer unserem Verständnis bleiben muß, wenn wir nur naturwissenschaft­liche Begriffe anwenden. Diese naturwissenschaftlichen Begriffe bil­den also die eine Strömung.",
      "Die andere Strömung bilden gewisse Begriffe, die wir uns machen über Ideelles oder Jdeales, und wohl auch heute, schon seit langer Zeit, über Moralisches. Nehmen Sie einen naturwissenschaftlichen Begriff wie den Begriff der Vererbung oder den Begriff der Entwicke­lung.",
      "Sie denken naturwissenschaftlich, wenn Sie diesen Begriff rein­lich und sauber denken; Sie denken verworren, wenn Sie diese Begriffe von Vererbung und von Entwickelung, wie sie in der Naturwissen­schaft üblich sind, auf Spirituelles ausdehnen. Nehmen Sie gewisse Begriffe, die man im Leben braucht, zum Beispiel den Begriff der inneren Freiheit unserer Seele, den Begriff des Wohlwollens, den Be­griff der sittlichen Vollkommenheit, oder höhere Begriffe, den Begriff der Liebe und dergleichen, so haben Sie wiederum eine Strömung von Ideen, von Begriffen, die auch berechtigt sind, weil sie ja zum Leben gebraucht werden.",
      "Aber nur wenn man sich einer Selbsttäuschung hingibt, kann man sich von der Art, wie heute naturwissenschaftlich gedacht wird, zu der Art, wie heute ideal oder ideell oder moralisch gedacht wird, eine Brücke bauen. Denkt jemand rein naturwissen­schaftlich, das heißt, sucht er sich ein naturwissenschaftliches Welt­bild, so wie das heute das Ideal vieler Leute ist, so hat innerhalb einer Welt, welche diesem Weltbild entspricht, alles das keinen Platz, was unter Begriffe wie Wohlwollen, meinetwillen auch Glück, Liebe, innere Freiheit und so weiter gefaßt ist.",
      "Ein gewisses Ideal natur-wissenschaftlicher Denkungsart ist, alles, wie man sagt, unter den Kausalbegriff zu bringen, alles nach Ursachen und Wirkungen zusammenzudenken. Und eine sehr beliebte Verallgemeinerung ist -ich habe das schon hier erwähnt - das Gesetz von der Erhaltung der",
      "Kraft und der Erhaltung des Stoffes. Bilden Sie sich eine Weltan­schauung so, daß Sie dazu nur die Begriffe von Ursache und Wirkung im naturwissenschaftlichen Sinne verwenden oder von der Erhaltung der Kraft und des Stoffes, so können Sie nur entweder weltanschau­lich unehrlich sein, oder Sie müssen sagen: Innerhalb einer solchen Weltenordnung, in welcher nur das Kausalitätsgesetz, nur das Ur­sachengesetz gilt, oder in welcher das Gesetz von der Erhaltung des Stoffes und der Kraft gilt, in einer solchen Welt ist alles, was Ideale sind, was Ideen sind, was moralische Begriffe sind, im Grunde ge­nommen eigentlich nur Spaß. - Denn für eine Weltanschauung, welche etwa das Gesetz von der Erhaltung der Kraft und des Stoffes univer­sell denkt, hat nichts anderes Sinn, als sich zu sagen: Nach diesem Gesetze von der Erhaltung der Kraft und des Stoffes entwickelt sich unsere Weltenordnung. - Aus gewissen Ursachen heraus ist inner­halb dieser Weltenordnung auch das Menschengeschlecht hervorge­gangen.",
      "Dieses Menschengeschlecht träumt von Wohlwollen, von Liebe, von innerer Freiheit, aber all das sind Begriffe, die sich die Menschen machen, und wenn einmal jener Zustand eingetreten sein wird in unserem Weltensystem, der eintreten muß nach naturwissen­schaftlichen Vorstellungen, dann ist eigentlich ein allgemeines Grab da für alle solche Vorstellungen von Wohlwollen, innerer Freiheit, von Liebe und so weiter. Das sind Träume, welche die Menschen träumen, während sie eben der reinen naturgesetzlichen Ordnung gemäß ihr Dasein innerhalb der Erdenentwickelung vollenden, und es hat gar keinen Sinn, von etwas anderem zu sprechen in bezug auf die Geltung der Ideale und Ideen, als davon, daß sie Träume der Menschen sind, denn innerhalb einer solchen naturwissenschaftlichen Weltanschauung haben Ideen und Ideale keine Kraft, sich zu realisie­ren.",
      "Was sollen denn, wenn die Welt wirklich entsprechen würde der naturwissenschaftlichen Weltanschauung, die Ideen und Ideale einmal machen, sobald der Zustand eingetreten ist, den man notwendig denken muß, wenn man nur mit naturwissenschaftlichen Begriffen denkt? Sie sind begraben, die Ideen und Ideale!",
      "Die Ideen und Ideale werden heute aber von den Menschen so gedacht - wenn sie das auch nicht zugeben -, daß sie keine innere Kraft haben, sich zu realisieren.",
      "Sie sind eben bloße Gedanken, die sich dadurch realisieren, daß die Menschen ihre Gefühle daran hängen, daß die Menschen sich gegen­einander so verhalten, wie es den Ideen entspricht. Aber sie haben keine innere Kraft, sich zu realisieren, diese Ideen, wie es der Magne­tismus, wie es die Elektrizität oder die Wärme hat - die hat innere Kraft, sich zu realisieren! Die Ideen als solche - denken Sie also immer meinetwiller an die moralischen Ideen - haben nicht eine solche innere Kraft, sich zu realisieren innerhalb unserer Weltanschauung, wenn wir sie nur naturwissenschaftlich denken.",
      "Gewiß, die wenigsten Menschen machen sich den Zwiespalt klar, der zwischen diesen zwei Strömungen unserer Gegenwart besteht, aber er ist da, und es ist die Tatsache, daß er im Unterbewußtsein der Menschen sein Spiel treibt, viel wichtiger, als daß man sich theore­tisch darüber klar ist. Theoretisch klar ist sich nur eine Schichte der Menschen über das, was ich eben gesagt habe, und diese eine Schichte der Menschen, auf die sollte man wohi ein Auge haben im Leben der Gegenwart.",
      "Klar ausgesprochen, daß die Sache so ist, daß die ganze Welt nur naturwissenschaftlich geordnet ist und daß Ideen und Ideale nur eine Bedeutung haben deshalb, weil die Menschen nun einmal das Gefühl haben, sie müßten sich geradezu danach richten in ihrem gegenseitigen Verhalten, findet man diese Anschauung nur innerhalb der sozialistischen Theorie der Gegenwart. Die sozialistische Theorie der Gegenwart lehnt daher jede Geisteswissenschaft ab, betrachtet sogar die Spuren alter Geisteswissenschaft, die sich noch in der Juris­prudenz, in der Moral und der Theologie finden, als Vorurteile, die den Kinderjahren der Menschheitsentwickelung angehören, und sie will alles, was man Geisteswissenschaft nennen könnte, als Gesell­schaftswissenschaft aufgefaßt wissen: sie will die sozialistische Gesell­schaftswissenschaft bilden als bloß gültig für das gegenseitige Ver­halten der Menschen.",
      "Die Welt ist naturwissenschaftlich geordnet, und außer der naturwissenschaftlichen Erklärung der Welt gibt es nur noch eine Gesellschaftswissenschaft. Das ist Grundüberzeugung jedes seiner selbst bewußten Sozialisten.",
      "Man darf, wenn man solchen Dingen auf den Grund gehen will, nicht konfusen Begriffen sich hingeben. Ich weiß selbstverständlich,",
      "daß man kommen kann und sagen: Ja, so denken doch nicht die Sozialisten! - Aber darauf kommt es nicht an - das habe ich ja gerade in den ersten Tagen, in denen ich hier wieder vorgetragen habe, aus­geführt -, was Ideen für einen Inhalt haben, sondern durch was Ideen sich betätigen, wie sie eindringen, sich einleben. Und die sozialisti­sche Idee lebt sich dadurch ein, daß sie ablehnt jedes Reden über irgendeinen geistigen Weltinhalt, daß sie behauptet, der Weltinhalt sei nur naturwissenschaftlich geordnet und Geisteswissenschaft sei durch bloße Gesellschaftswissenschaft zu ersetzen.",
      "Nun fühit der Mensch, daß bloße Ideen und Ideale, wenn sie so gedacht werden, wie sie in der Gegenwart gedacht werden, eben wirklich nicht mehr Kraft haben, als sich in das menschiiche Gemüts-leben hineinzufinden und sich dadurch zu realisieren, zu realisieren als ein Traum, den die Menschheit innerhalb der Erdenentwickelung träumt. Keine Idee, und wäre sie die schönste, die idealste, hat die Kraft, irgend etwas wachsen zu lassen, irgendwo Wärme zu erzeugen, einen Magneten zu bewegen oder dergleichen. Damit ist sie schon ver­urteilt, bloßer Traum zu sein, weil sie ja - solange man die Welten-ordnung nur denkt als die Summe von elektrischen, magnetischen Kräften, von Lichtkräften, Wärmekräften und so weiter - in das Gefüge dieser Kräfte nicht eingreifen kann, insbesondere wenn man das Gesetz von der Erhaltung der Kraft und des Stoffes aufstellt, wo­nach Kraft und Stoff eine ewige Geltung haben sollen. Denn dann sind sie immer da, und dann können Ideen nirgends eingreifen, denn Kraft und Stoff haben dann ihre eigenen, ewigen Gesetze.",
      "Mit diesem Gesetze - das sage ich nur in Parenthese - von der Er­haltung der Kraft und des Stoffes wird ja viel Unfug getrieben. So wie man in der Literatur heute von dem Gesetz der Erhaltung der Kraft und des Stoffes, namentlich von Kraft und Energie gesprochen findet, wird es auch häufig zurückgeführt auf Julius Robert Mayer. Wer Julius Robert Mayers Schriften wirklich kennt, der weiß, daß es ebenso gescheit ist, das Gesetz von der Erhaltung der Kraft und des Stoffes auf Julius Robert Mayer zurückzuführen, so wie es heute in der Literatur geschieht, wie wenn man etwa die Schundliteratur auf die Erfindung der Buchdruckerkunst durch Gutenberg zurückführte.",
      "Denn das, was heute in Lehrbüchern und gebräuchlichen Hand­büchern als Gesetz von der Erhaltung der Kraft und des Stoffes fun­giert, das hat mit dem Gesetz von Julius Robert Mayer, den man für seine Tat ins Irrenhaus eingesperrt hat, nichts zu tun.",
      "Nun entsteht eigentlich für den, der Geisteswissenschaft ernst nimmt, aus alledem, was ich dargestellt habe, eben die Frage: Welches Verhältnis, welcher Bezug besteht zwischen dem, was nimmer ver­einigt werden kann innerhalb der gegenwärtigen Weltanschauung: moralischem Idealismus und naturalistischem Anschauen der Welt? -Diese Frage läßt sich nicht so ohne weiteres theoretisch beantworten. Die Gegenwart wünscht vielfach theoretische Antworten, und auch diejenigen, die zur Theosophie oder Anthroposophie kommen, wün­schen manchmal am allermeisten theoretisch-dogmatische Antworten.",
      "Aber die Antworten, die auf dem Boden der Geisteswissenschaft ge­geben werden sollen, müssen Antworten der Anschauung sein. In dieser Beziehung geht es nicht, daß man gerade die Vorliebe der Gegenwart für Dogmatismen auch wiederum in die Geisteswissen­schaft hineinträgt.",
      "Die Geisteswissenschaft verlangt anderes. Die Geisteswissenschafter verlangen freilich vielfach, daß andere Dogmen aufgestellt würden, aber die Geisteswissenschaft kann ganz und gar nicht der Ansicht sein, daß bloß andere Dogmen aufgestellt werden, als sie schon aufgestellt sind, sondern daß anders gedacht und anders angeschaut werde, daß überhaupt gewisse Dinge unter ganz andern Gesichtspunkten gedacht werden.",
      "Dasjenige, was vielfach heute auch als Geisteswissenschaft, namentlich auch als Theosophie getrieben wird, das kann einem oftmals den Eindruck machen einer etwas ver­änderten Scholastik des Mittelalters. Ich will mich gar nicht gegen Scholastik wenden, denn die Scholastik hat Dinge in sich, die viel bedeutsamer sind als dasjenige, was philosophisch in der Gegenwart hervorgebracht wird.",
      "Aber der Hang vieler Menschen in der Gegen­wart ist dahingehend, nur wiederum andere Dogmen zu haben, über Gott und Unsterblichkeit und weiß Gott was, eben anders zu denken, aber eben doch nur zu denken, nicht zu Anschauungen zu kommen, die aus ganz anderem Fond heraus sind als frühere Vorstellungen. Steht man recht auf dem Boden der Geisteswissenschaft, so sagt man sich:",
      "Zur Zeit der Scholastik ist über die Dreieinigkeit, über das Wesen des Menschen, über seine Unsterblichkeit, über das Christus-Problem genug spintisiert worden, wenn ich den Ausdruck jetzt gar nicht mit irgendeinem üblen Beigeschmack anwende. Denn der eigentliche Wert dieser Scholastik liegt nicht in den Dogmen, die sie aufgestellt hat, sondern in der Technik des Denkens, wie ich es einmal darge­stellt habe in meiner Schrift «Philosophie und Anthroposophie», die jetzt in einer neuen Auflage wesentlich erweitert wiederum erscheinen wird; er liegt in der Art, über die Dinge zu denken.",
      "Aber dieses Den­ken, das eignet man sich heute eigentlich besser an, wenn man zu den Scholastikern geht, als wenn man zu den vielfach konfusen Ideen, die man in der neueren Zeit theologische oder philosophische nennt, sich hinwendet. Da ist genug theoretisiert worden im Mittelalter über diese Dinge.",
      "Da hat man zum Beispiel so theoretisch mit dem Christus-Problem gerungen. Wer das Wesen dieses Ringens kennt, der kann nicht viel Geschmack abgewinnen einem etwas veränderten Schola­stizieren, wie es zum Beispiel in der Theosophie vielfach getrieben worden ist, wo man halt, statt daß man früher, nicht wahr, Dreieinig­keit, Unsterblichkeit oder anderes hatte, nun wiederum physischen Leib, Ätherleib, Astralleib hat.",
      "Es ist ein anderes Theoretisieren, aber es ist im Grunde genommen qualitativ dieselbe Sache. Derjenige, der recht eingehen mag auf diese Schule des Mittelalters, der weiß, daß das gewissermaßen eine erledigte Angelegenheit ist, so vordringen zu wollen, sagen wir, zu dem Mysterium von Golgatha.",
      "Da ist heute viel wichtiger, zum Beispiel nach der Gestalt des Christus Jesus zu dringen, was versucht wird von uns hier in der Mittelpunktsgruppe des Baues, wo gesucht wird, die Gestalt des Christus Jesus wirklich wiederum zu finden. Derjenige, der sich richtig für frühere Dogmen interessiert, wird sich heute viel mehr dafür interessieren, die Ge­staltung des Christus aus dem geistigen Leben herauszuholen, weil heute die Zeit dazu da ist, dies zu tun.",
      "Im Mittelalter war die Zeit, scharfsinnig nachzudenken und scholastische Begriffe auszuspinti­sieren; heute - das habe ich ja vielfach charakterisiert - ist ein solcher Punkt der fünften nachatlantischen Zeit, wo hingelenkt werden muß die Anschauung der Menschen nach den geistigen Formen. Dasjenige,",
      "was früher als Gestaltung des Christus gesucht wurde, sind ja phan­tastische Gestaltungen. Ich habe über die Entwickelung der Christus-gestalt ja öfter hier gesprochen. Mit den Mitteln der geistigen An­schauung wird sich die Gestalt des Christus wiederum finden lassen. So hat jede Zeit ihre besondere Aufgabe. Denn nicht darauf kommt es an, daß irgend etwas festgelegt wird, sondern darauf, daß die Mensch­heit in ihrer Entwickelung sucht und dadurch sich zu immer weiteren und weiteren Stufen ihrer Entwickelung durchringt.",
      "Also darauf kommt es an, daß man gewissermaßen eine Brücke finden kann da, wo die moderne Weltanschauung eine Brücke eben nicht finden kann, sondern wo, wenn sie sich selbst richtig versteht, sie notwendigerweise zum Sozialismus, das heißt zur sozialistischen Theorie kommen muß - nicht zum Sozialismus in seiner Berechti­gung; darüber habe ich ja auch schon öfter gesprochen. Diese Brücke kann man aber nur finden, wenn man den ehrlicher Willen hat, eben­so wie man in dasjenige eindringt, was zwischen der Geburt und dem Tode verläuft, auch in dasjenige einzudringen, was zwischen dem Tode und einer neuen Geburt verläuft, wenn man also nicht bloß den Willen hat, gewissermaßen die Welt hier zu analysieren, sondern wenn man den Willen hat, sich wirklich auf das Geistige einzulassen.",
      "Man redet von dem Menschen und sagt: Der Mensch besteht aus physischem Leib, Ätherleib, astralischem Leib, Ich und so weiter. - Das ist ge­wiß berechtigt; aber es ist für den Menschen berechtigt, der hier zwischen der Geburt und dem Tode lebt. Das, was ich das vorige Mal und das vorvorige Mal hier ausgeführt habe, das kann Sie aber schon darauf hinweisen, daß man in einer ähnlichen Weise nun reden kann über den Menschen nach dem Tode, über den Menschen zwischen dem Tode und einer neuen Geburt.",
      "Wenn Sie schon fragen wollen: Aus was besteht der Mensch? - so können Sie nicht bloß fragen: Aus was besteht der Mensch hier auf Erden? - und antworten: Da besteht er aus physischem, Ätherleib, Astralleib und Ich -, sondern wir müssen jetzt auch die Frage aufwerfen: Aus was besteht der Mensch, wenn er nicht auf Erden ist, sondern in einer geistigen Welt zwischen Tod und neuer Geburt? Wie kann man da von den Gliedern der mensch­lichen Natur reden? - Da muß man in ebenso realer Weise von den",
      "Gliedern der menschlichen Natur reden können. Und man muß sich, wenn man ganz ehrlich bei einer solchen Sache mit sich zu Rate geht, eben bewußt werden, daß jedes Zeitalter seine besondere Aufgabe hat.",
      "Die Menschen werden sich nicht recht bewußt, daß eigentlich die Art, wie sie denken, vorstellen, selbst wie sie empfinden, ja, selbst wie sie die Außenwelt anschauen - erinnern Sie sich nur an gewisse Ausführungen, die ich in meinen «Rätseln der Philosophie» gemacht habe über den verhältnismäßig kurzen Zeitraum von sechshundert Jahren vor unserer Zeitrechnung bis zu uns -, eben nur jetzt so ist. Wir können nicht über das 8.",
      "Jahrhundert vor dem Mysterium von Golgatha zurückgehen mit dem Denken und dem Empfinden und dem Anschauen, das wir jetzt haben. Ich habe Ihnen das genaue Jahr angegeben: 747 vor dem Mysterium von Golgatha ist die wahre Gründungszahi der Stadt Rom.",
      "Wenn man hinter dieses 8. vorchrist­liche Jahrhundert zurückgeht, dann ist die ganze Art des mensch­lichen Lebens eine andere als diejenige, die man jetzt als Seelenieben eben kennt. Da werden alle Arten, die Welt anzuschauen, anders.",
      "Da ist allerdings eine Grenzscheide, die man schon besser beobachten kann als die andere, die eigentlich auch gut zu beobachten ist, aber noch nicht für den Menschen der Gegenwart: die Grenzscheide, die im 15. Jahrhundert liegt.",
      "Das 15. Jahrhundert liegt den Menschen der Gegenwart zu nahe; da können sie sich nicht so recht in den großen Umschwung hineinversetzen, der da eingetreten ist. Im ganzen stellen sich die Menschen vor: gedacht und gesonnen hat man immer so wie jetzt, auch wenn man immer weiter zurückgeht; aber wie wenig weit geht man zurück!",
      "Nun ja, die Sache ist eben diese, daß, sobald man hinter das 8. vorchristliche Jahrhundert zurückgeht, man eine ganz andere Art zu denken hat. Und nun können wir die Frage aufwerfen:",
      "Warum hatte man denn da eine andere Art zu denken? Über diese andere Art zu denken machen sich die Menschen jetzt, wenn sie sich Vorstellungen machen, ziemlich törichte Vorstellungen, könnte man sagen. Wenn die Menschen der Gegenwart jetzt hören, wie, sagen wir, in den ägyptischen Mysterien - es waren dazumal die gesuchtesten -gelehrt worden ist, wenn sie etwas hören von der Art, wie da die Wahrheiten erörtert worden sind, da meinen sie: Nun ja, das entspricht",
      "eben der phantastischen Zeit von dazumal, da waren die Men­schen noch nicht so gescheit wie jetzt, da haben sie sich noch kin­dische Vorstellungen gemacht; das Richtige, das haben wir jetzt! -Es liegt besonders dem Menschen der Gegenwart nahe, so zu denken, denn er kann sich, weil er so furchtbar eingerutscht ist in diese Denk­weise der Gegenwart, nicht irgend etwas anderes dabei denken. Nehmen wir an, ein Grieche, Pythagoras zum Beispiel, sei nach Ägyp­ten gekommen und hätte dort gelernt, so wie heute irgend jemand nach einer berühmten Universität geht, um zu lernen. Aber was hat er gelernt? Ich will Ihnen etwas sagen, was der Pythagoras wirklich dort hat lernen können: Er hat dort gelernt, daß in Urzeiten der Merkur mit dem Monde einmal Schach gespielt hat, und bei diesem Schachspiel hat der Merkurius gewonnen. Er hat nämlich dem Monde für jeden Tag zwanzig Minuten abgewonnen, und diese zwanzig Minuten, die sind dann von den Eingeweihten zusammengezählt worden. Wieviel machen sie aus, diese zwanzig Minuten in drei­hundertsechzig Tagen? Die machen nämlich gerade fünf Tage aus. Daher hat man nicht dreihundertsechzig Tage als das Jahr gerechnet, sondern dreihundertfünfundsechzig Tage. Diese fünf Tage sind das­jenige, was der Merkur dem Monde im Spiel abgewonnen hat, und was er dann den übrigen Planeten und dem ganzen Menschenge­schlecht zu dreihundertsechzig Tagen im Jahr hinzugeschenkt hat.",
      "Nun, nicht wahr, wenn man sagt, so etwas habe der Pythagoras bei den weisen Ägyptern lernen können, dann lacht jeder Mensch in der Gegenwart, ganz selbstverständlich. Dennoch ist es nur eine andere Binkleidung für eine tiefe geistige Wahrheit - wir werden davon in diesen Tagen noch sprechen -, die die Gegenwart noch gar nicht wieder entdeckt hat, die aber eine Wahrheit ist.",
      "Sie könnten fragen: Warum ist dazumal ganz anders gerechnet worden? - Vergleichen Sie den Vortrag eines solchen ägyptischen Weisen, der also dem krassen Fuchs Pythagoras vorträgt: Der Mer­kur hat im Schachspiel für jeden Tag dem Monde zwanzig Minuten abgewonnen - mit einem Vortrag über moderne Astronomie, der in einem Hörsaal gehalten wird, so werden Sie besser auf den Unter­schied aufmerksam werden. Fragt man sich aber: Warum ist ein",
      "solcher Unterschied? - dann muß man etwas tiefer hineingehen in das ganze Wesen der menschlichen Enwickelung. Denn wenn man hinter das 8. vorchristliche Jahrhundert zurückgeht - Pythagoras gehört zwar nicht dieser frühen Zeit an, aber in Ägypten haben sich die Reste einer Weisheit, die eben weit vor dem 8. vorchristlichen Jahr­hundert begründet worden ist, erhalten, da konnte man sie sich noch einprägen -, wenn in diesen alten Zeiten so gelehrt worden ist, so hat das schon seinen tiefen Grund. Es war das ganze Verhältnis des Menschen zur Welt anders angesehen worden, mußte anders in der damaligen Zeit angesehen werden.",
      "Ich möchte darauf hinweisen, daß ja noch verschiedene Reste alter Anschauung immer wieder und wieder atavistisch erneuert worden sind, wobei ich unter dem Wort «atavistisch» nicht irgend etwas Ab­fälliges meine und verstehe. Wer zum Beispiel ein Werk liest, wie Jakob Böhmes «De signatura rerum», der wird, wenn er ehrlich ist, eigentlich auch heute sagen: er kann nichts damit anfangen.",
      "Denn da werden ganz merkwürdige Auseinandersetzungen gegeben, die ent­weder von einem höheren Gesichtspunkte aus beurteilt werden müs­sen - dann bekommen sie einen Sinn -, oder aber die vom Stand­punkte des modern denkenden Menschen als unvernünftiges Zeug eines Laien, der ein bißchen spintisiert hat, eigentlich abgelehnt wer­den müßten. All das tolle Gerede, das vielfach getrieben wird von unreifen theosophischen Kreisen über Jakob Böhme, ist eigentlich vom Übel.",
      "Dennoch erinnert dieser Jakob Böhme von einem höheren Standpunkte aus in seinem ganzen Geistesgefüge, in der Art, wie er sich namentlich zur Analyse von gewissen Worten verhält, wenn er zum Beispiel Worte wie Sulfur zerlegt und in den zerlegten Teilen etwas sucht - wir wollen nicht auf das Materielle dabei sehen, sondern auf die Art, wie er da etwa in seinem Werke «De signatura rerum» vorgeht -, er erinnert viel mehr als irgendeine von den abstrakten Wissenschaften, die es ja nur heute in der Öffentlichkeit gibt, an einen gewissen konkreten Zusammenhang des Menschen mit der gesamten geistigen Welt. Er steht, dieser Jakob Böhme, viel mehr in dieser geistigen Welt darinnen.",
      "Und dieses Darinnenstehen in der geistigen Welt, das ist das Charakteristische für solche Denker, die vor dem 8.",
      "vorchristlichen Jahrhundert, vor unserer Zeitrechnung eben Denker waren. Sie dachten nicht mit der individuellen Einzelvernunft, mit der wir heute denken.Wir denken ja alle mit der individuellen Einzelver­nunft; die dachten mehr noch mit der kosmischen Vernunft, mit der schöpferischen Vernunft, mit der Vernunft, die man, ich möchte sagen, in einzelnen ihrer Schöpfungen noch erlauschen muß wenn man auf sie kommen will.",
      "Heute gibt es eigentlich nur noch ein Gebiet, in dem man ein klein wenig merken kann, wie ins Menschenleben noch so etwas wie die schöpferische Vernunft sich hereinergießt und hereinwirkt. Man kann noch auf einem Gebiet etwas bemerken von einem Sich-Realisieren von Ideellem; aber, ich möchte sagen, es ist nur noch ein Schatten davon da, und dieser Schatten wird zumeist auch nicht berücksichtigt.",
      "Es existieren heute eine ganze Anzahi von naturalistischen anthropo­logischen Theorien über die Entstehung der Sprache, wie sie sich entwickelt haben soll. Sie wissen, es gibt - ich habe das öfter erwähnt -zwei hauptsächliche Theorien.",
      "Man nennt die eine die Wauwau-Theorie, die andere die Bimbam-Theorie. Die Wauwau-Theorie ist mehr von kontinentalen Gelehrten vertreten, die Bimbam-Theorie ist von Max Müller vertreten. Die Wauwau-Theorie beruht darauf, daß Menschen von primitivsten Zuständen ausgegangen sind und da ihre inneren organischen Erlebnisse so herausgebellt haben wie der Hund, wenn er «wauwau» macht, und durch eine entsprechende Ent­wickelung - alles entwickelt sich ja, nicht wahr, vom Primitiven bis zum Vollkommenen - ist das Wauwau des Hundes, das heute noch beim Menschen auf seiner primitiven Stufe zu bemerken ist, zur menschlichen Sprache geworden.",
      "Wenn man alles in der Entwicke­lung verfolgt vom Wauwau bis zum heutigen Sprechen, so ähnlich, nicht wahr, wie es die Deszendenztheorie macht, Darwin oder Haeckel, beginnend mit der einfachsten Monere, also von der einfachsten Weise, von der unartikuliertesten Weise bis zu der heutigen Sprache, dann ist das eben die Wauwau-Theorie. Eine andere Theorie besagt, daß man ein gewisses Gefühi entwickeln kann der Verwandtschaft mit den Tönen der Glocke: Bimbam; man hätte jedesmal einen bestimm­ten inneren Klang, den man imitiert.",
      "Danach würde man mit dem",
      "Wauwau mehr eine Evolutionstheorie verfolgen, mit der Bimbam­Theorie mehr eine Anpassungstheorie, eine Anpassung des Menschen an die innere Natur der materiellen Worte. Dann kann man ja auch geistreich die Dinge verbinden, die Bimbam-Theorie mit der Wauwau-Theorie, das ist dann etwas Vollkommeneres, dann hat man Ent­wickelung mit Anpassung verbunden. Nun ja, diese Dinge sind heute mehr oder weniger gang und gäbe. Es gibt auch solche, die über diese beiden Theorien lachen und die andere Theorien haben; aber im Prinzip sind sie eben auch nicht viel anders.",
      "Geistig betrachtet, geistig angeschaut kann gar keine Rede davon sein, daß die Sprachentwickelung eine solche ist, wie sie eben cha­rakterisiert worden ist, sondern schon rein äußerlich zeigt das Ge­füge der Sprache, daß im Sprachbilden, im Entstehen der Sprache wirkliche Vernunft waltet. Und zwar ist es interessant, gerade an der Sprache das Walten der Vernunft festzuhalten, aus dem einfachen Grunde, weil am anschaulichsten noch in der Sprache ein ideelles Moment lebt, also dasjenige, was in der einen Strömung heute ange­schaut wird, und weil die Sprache nicht bloß an das Gemüt des Men­schen sich wendet, sondern ihre eigene Gesetzmäßigkeit hat, also das Ideelle in einer gewissen Weise sich in ihr schon realisiert, wenn auch gegenüber natürlichen Gesetzen schattenhaft.",
      "Nehmen Sie zum Bei­spiel ein Wort - ich will Sie nur auf ein paar sehr elementare Fälle auf­merksam machen -, wo Sie sehen können, wie innere Vernunft im Sprachentstehen waltet; nehmen Sie ein Wort wie: Oratio, die Rede. Es ist nun merkwürdig, wenn man solch ein Wort nimmt wie Oratio, die Rede, und dann beobachtet, was aus diesem Worte wird im Leben des Menschen nach dem Tode, so stellt sich eine merkwürdige Ähn­lichkeit ein mit dem, was als werdende Vernunft in der Entwickelung der Sprache gewirkt hat.",
      "Das gibt gewisse Sicherheiten, die man heute auf einem andern Weg kaum gewinnen kann. Auf einem andern Wege kann man höchstens Hypothesen gewinnen. Der Tote wird selten, wenigstens nachdem eine bestimmte Zeit seit dem Tode verflossen ist, das Wort Oratio noch verstehen; er wird es nicht mehr verstehen, er verliert das Verständnis dafür.",
      "Dagegen wird er immer noch ver­stehen eine Anschauung, eine Imagination, welche zurückführt auf",
      "das, was man ausdrücken kann durch die Worte: Os, Oris, Mund, und: Ratio, Vernunft. Der Tote löst das Wort Oratio auf in Os und Ratio. Und in der Entwickelung hat sich der umgekehrte Vorgang wirklich abgespielt: Das Wort Oratio ist wirklich entstanden durch eine Synthesis ursprünglicher Wörter, Os und Ratio. Oratio ist kein so ursprüngliches Wort wie Os, Oris und Ratio, sondern Oratio ist aus Os und Ratio gebildet.",
      "Ein paar solcher elementarer Dinge möchte ich Ihnen anführen. Diese Dinge können am anschaulichsten noch an der lateinischen Sprache studiert werden, weil sie da am deutlichsten noch zutage treten, es sind aber die Gesetze, die dabei gefunden werden können, auch für andere Sprachen von Bedeutung. Nehmen Sie zum Beispiel drei ursprungliche Worte: Ne ego otior; das würde heißen, wenn man es als Wort nimmt: Ich bin nicht müßig. Ego otior: Ich bin müßig; ne ego otior: Ich bin nicht müßig. Diese drei Worte setzen sich durch die waltende kosmische Vernunft zusammen in Negotior, das heißt:",
      "Handel treiben. Da haben Sie drei Worte in eins zusammengefügt, und Sie sehen vernunftmäßig den Aufbau der Worte. Sie sehen Vernunft walten in der Entwickelung der Sprache.",
      "Ich würde, wie gesagt, dieses nicht so strikte behaupten, wenn nicht die merkwürdige Tatsache eintreten würde, daß der Tote das, was hier in der Welt zusammengefügt worden ist, wiederum auflöst. Der Tote löst wiederum so etwas wie das Negotior auf in: Ne ego otior, und er versteht nur diese drei Worte beziehungsweise Anschauungen, die er sich aus dieser Trinität zusammenfügt, und er vergißt dasjenige, was durch die Zusammenfügung entstanden ist.",
      "Ein anderes naheliegendes Beispiel ist: Unus, der eine, und Alterque, der andere; das ist zusammengezogen in das lateinische Wort Uterque, jeder von beiden. Wir könnten recht froh sein, wenn wir in den mo­dernen Sprachen ein solches Wort hätten wie Uterque, das jenen Be­griff gibt; der Franzose kann es höchstens ausdrücken, indem er bei dem oberen bleibt: l'un et l'autre; er hat nicht einen einzigen Begriff, um das auszudrücken. Aber Uterque drückt das viel präziser aus.",
      "Nehmen Sie einen Fall, damit Sie sehen, welches Prinzip ich eigent­lich meine. Sie alle kennen selbstverständlich das Wort «se», das französische",
      "Wort «se»: sich. Sie kennen das Wort «hors»: außer sich, her­aus, könnte man auch sagen, und «tireD> - ich behalte davon nur das «tir» bei -: «tiD>, ziehen, sich wegziehen. Wenn Sie diese drei Dinge dann nach demselben Prinzip zusammensetzen, so bekommen Sie hier das «sortir», weggehen, was nichts anderes ist als eine Zusammen-fügung von «se hors tir»; «tir» ist der Rest des Wortes «tirer». Da sehen Sie noch in einer modernen Sprache diese selbe waltende Ver­nunft darinnen. Oder nehmen Sie ein Beispiel, wo die Sache etwas dadurch kaschiert ist, daß verschiedene Sprachstufen wirken: «cceur», das Herz; «rage», das ist das Lebendige, das sich Belebende, der Enthusiasmus, der vom Herzen ausgeht; zusammengesetzt: «cou­rage». Das sind nicht irgendwelche Erfindungen, sondern das sind reale Geschehnisse, die wirklich da waren. So sind die Worte ge­bildet.",
      "Aber die Möglichkeit, so Worte zu bilden, sie ist heute nicht mehr da. Heute hat sich der Mensch herausgestellt aus dem lebendigen Zu­sammenhang mit der kosmischen Vernunft, und daher kann höch­stens noch in ganz sporadischen Fällen eine Möglichkeit vorhinden sein, sich heranzuwagen an die Sprache, um irgendwelche Worte aus der Sprache herauszuholen, die, wie man sagt, im Geiste der Sprache sind. Aber je weiter man zurückgeht, und namentlich je weiter man zurückgeht hinter das 8. vorchristliche Jahrhundert, auch bei der griechischen, bei der lateinischen Sprache, desto mehr ist im leben­digen Leben das Prinzip tätig, daß in dieser Weise gerade Sprachent­wickelung wirkt. Und dabei bleibt immer das Bedeutsame, daß man wie auf ein Eurythmisches auf dieses hinzuweisen hat dadurch, daß man beim Toten entdeckt: Er zieht die Worte wieder auseinander, er zerlegt sie wieder in ihre Teile. Er hat mehr Empfindung, der Tote, für diese Teile der Worte, als für die ganzen Worte. Denken Sie sich konsequent die Sache durchentwickelt, so würden Sie die Worte überhaupt auseinanderkriegen in die Laute, und wenn Sie die Laute wiederum umsetzen, jetzt nicht in Luftbewegungen, sondern in Be­wegungen des ganzen Menschen, dann haben Sie die Eurythmie. Die Eurythmie ist daher etwas, was der Tote in der Tat sehr gut ver­stehen kann, wenn sie vollkommen betrieben wird. Und Sie sehen,",
      "daß sich solche Dinge, wie auch die Eurythmie, nicht äußerlich be­urteilen lassen, sondern daß man ihre ganze Stellung im Gesamtge-füge der menschlichen Entwickelung nur einsehen kann, wenn man auch einzugehen vermag auf diese Gesamtentwickelung des Men­schen.",
      "Es ließe sich noch viel mehr sagen über das, was Eurythmie eigent­lich will, aber dazu wird sich später noch Gelegenheit bieten. Ich wollte damit zunächst einmal Sie auf ein wenn auch schattenhaftes Gebiet hinweisen, wo noch in den älteren Zeiten irn lebendigen Wir­ken der Menschen selber ein Hereinspielen des Idealen in das Reale war.",
      "Ich sagte heute im Eingange: In der heutigen Weltanschauung finden wir nicht mehr die Möglichkeit, eine Brücke zu bauen zwischen dem Ideellen, Idealen, Moralischen, und zwischen dem, was in der Natur lebt. Es fehit die Brücke.",
      "Das ist auch dem heutigen Entwickelungs-zyklus des Menschen ganz natürlich, daß diese Brücke fehlt. Das Ideelle schafft nicht mehr. Ich wollte Ihnen im menschlichen Gebiet selbst ein Beispiel zeigen, wenn auch, wie gesagt, ein schattenhaftes, wo in dem Menschen selbst noch ein Ideelles schafft.",
      "Denn in dem Zusam­mensetzen solcher Worte, da wirkte nicht Verabredung der Menschen oder die Überlegung einer einzelnen menschlichen Individualität oder Persönlichkeit, sondern da wirkte Vernunft, ohne daß der Mensch so richtig dabei war. Heute wollen die Menschen ja bei allem dabei sein, was sie machen: Nun, wenn so etwas Schönes, Großes, Bedeutsames gemacht werden sollte wie das hier - da sollten Sie sehen, was mit der heutigen Weisheit der Menschen herauskäme, wenn heute Sprache gebildet werden sollte!",
      "Aber gerade in den Zeiten, in denen der Mensch noch nicht so bei sich war, sind diese großartigen, weisen, be­deutsamen Dinge in der Menschheit geschehen, und sie sind so ge­schehen, daß in diesem Geschehen noch ein nahes Zusammensein von Ideellem und von Realem ineinanderwirkte, nämlich ideellem, also vernünftigem Werden, und realem Bewegen der Luft durch die menschlichen Atmungsorgane. Heute können wir nicht zwischen der moralischen Idee und meinetwillen der elektrischen Kraft eine Brücke bauen; aber hier ist eine Brücke gebaut zwischen etwas Geschehendem und etwas Vernünftigem.",
      "Das führt uns natürlich nicht dazu - ich",
      "werde das morgen weiter ausführen -, dieselbe Brücke zu bauen; sie muß heute in ganz anderer Weise gebaut werden. Aber Sie können daraus sehen, daß die Menschheit zu dem heutigen Zustande vorge­schritten ist von einem andern Zustande: von einem Drinnenstehen in einem lebendigen Weben, das nahe war dem, was in einer gewissen Weise umgekehrt Post mortem, also nach dem Tode der Menschen sich vollzieht. Der Mensch muß heute nach dem Tode, um sein Fort­kommen zu finden zwischen dem Tode und einer neuen Geburt, das wieder auseinandernehmen, was durch Kräfte - wir werden morgen noch dayon sprechen - so zusammengefügt worden ist, daß man die­ses Zusammenfügen noch deutlich sehen kann, wenn man in die älteren Stufen des Sprachbildens zurückgeht.",
      "Das sind wichtige Dinge, Dinge, die man wirklich ins Auge fassen muß, wenn man den Blick darauf wendet: Wie soll sich - wir haben ja darüber oft gesprochen, daß dies von uns ins Auge gefaßt werden muß - in das ganze Gefüge des gegenwärtigen Geisteslebens hinein­stellen dasjenige, was auf dem Boden der Geisteswissenschaft ge­funden werden kann? - Und wenn man immer wieder spricht von der Wichtigkeit dieses Hineinstellens der Geisteswissenschaft in die ganze Entwickelung, so muß man schon auch auf diesem Gebiete konkret denken. In diesen Vorträgen möchte ich jetzt einiges beitragen zu diesem konkreten Denken.",
      "Wenn es einmal sein könnte, daß Geistes­wissenschaft getragen würde von einer gewissen Bewegung in der Gegenwart, von einer Menschenbewegung, dann würde auf allen Gebieten diese Geisteswissenschaft befruchtend wirken können. Aber es müßte natürlich vor allen Dingen der Wille vorhanden sein, auf solche Subtilitäten auch einzugehen, wie sie hier oftmals betont wer­den.",
      "Denn auf diese Subtilitäten, die sich immer beziehen auf das Ver­hältnis unserer Geisteswissenschaft zur gegenwärtigen Geisteskultur, müssen wir das begründen, was wir nennen können unser eigenes Uns­Hineinstellen in die Geistesbewegung der Gegenwart mit der Geistes­wissenschaft. Es ist wirklich so, daß die traurigen, katastrophalen Ereignisse der Gegenwart den Menschen aufmerksam machen soll­ten, daß alte Weltanschauungen Bankrott gemacht haben.",
      "An der Geisteswissenschaft allein nicht, aber an ihrer Beziehung zu diesen",
      "alten Weltanschauungen könnte man sehen, was zu geschehen hat, damit wir aus dem Bankrott der gegenwärtigen Zeit hinauskommen.",
      "Dazu wäre freilich notwendig, daß man endlich einginge auf die Intentionen, welche ich ja oftmals gerade als diejenigen der geistes-wissenschaftlichen Bewegung ausgesprochen habe. Es wäre wirklich notwendig, einzusehen, welches die Gründe sind, warum zum Bei­spiel auf der einen Seite es innerhalb gewisser Kreise so fruchtbar ge­worden ist, hier am Bau zu wirken, und warum andere Bestrebungen der Anthroposophischen Gesellschaft gewissermaßen ebenso un­fruchtbar geblieben sind; warum, wenn man absieht von dem, was sie wirklich geleistet hat, nämlich daß sie den Dornacher Bau in die Welt setzt, die Gesellschaft doch vielfach versagt.",
      "Ein solches Leisten auf der einen Seite bedingt immer, wenn es nicht oftmals das Gegen­teil wachrufen soll, daß manches andere geschieht. Es wäre notwendig, daß auch auf andern Gebieten die Anthroposophische Gesellschaft nicht versagte, wie sie vollständig versagt hat in den Jahren, in denen sie besteht.",
      "Dieses Versagen, das brauchte man nicht immer wieder und wiederum zu betonen, wenn viel stärker die Meinung verbreitet wäre, daß man nachdenken muß, warum die Anthroposophische Gesellschaft in bezug auf so vieles andere versagt. Wenn man gründ­licher nachdenken würde, so würde man erkennen, worauf es zum Beispiel beruht, daß draußen in der Welt immer wieder und wiederum die Meinung sich verbreitet, ich führte die Anthroposophische Ge­sellschaft nur so am Gängelbande und gäbe alles an; während es kaum eine Gesellschaft in der Welt gibt, wo weniger dasjenige geschieht, was ein sogenannter Führer will, als in der Anthroposophischen Ge­sellschaft!",
      "Es geschieht ja in der Regel das Gegenteil von dem, was ich eigentlich beabsichtige. Also, nicht wahr, gerade an der Anthro­posophischen Gesellschaft kann es sich zeigen, wie im Praktischen eine Wirklichkeit weit ab ist auch von ihren sogenannten Idealen.",
      "Aber man muß dann auch den Willen haben, sich auf den Boden der Wirklichkeit zu stellen. In einer Gesellschaft gibt es selbstverständ­lich Persönliches; aber man muß dieses Persöniiche auch als Per­sönliches auffassen.",
      "Wenn irgendwo in einem Zweige sich die Leute streiten aus rein persönlichen Gründen, so soll man da nicht aus",
      "Weiß Schwarz machen, oder aus Schwarz Weiß machen, sondern man soll ruhig zugestehen: Wir haben persönliche Gründe, wir mögen den und den nicht aus persönlichen Gründen. - Dann ist man bei der Wahrheit; man braucht ja nicht die Wirklichkeit in Ideale zu ver­kehren. So wäre es notwendig, daß, während auf der einen Seite mein Bestreben dahin geht, alles Geisteswissenschaftliche aus dem Sek­tiererischen herauszuheben, alles Sektiererische abzustreifen, die An­throposophische Gesellschaft immer mehr und mehr in das Sek­tiererische hineinplumpst und eine gewisse Liebe gerade für das Sektiererische hat. Wenn irgendwo das Bestreben besteht, aus dem Sektiererischen herauszukommen, so haßt man gerade hier dieses Herauskommenwollen aus dem Sektiererischen.",
      "Ich möchte natürlich nicht irgend jemanden tadeln, möchte auch nicht undankbar sein gegen die schönen Bestrebungen, die da und dort überall sind, ich erkenne alles voll an, aber es ist notwendig, daß man über manche Dinge ein wenig nachdenkt, sonst werden sich im­mer wieder und wiederum die Dinge finden, von denen mir auch in diesen Tagen wiederum erzähit worden ist. Nicht wahr, es ist auch da das Persönliche mit der Sache schon innig verquickt.",
      "Wenn jetzt in einem Lande wiederum irgendein Unheil auftaucht, so ist wiederum die Konstitution gerade der Anthroposophischen Gesellschaft so, daß, ich möchte sagen, die Gesellschaft die Sensation hat, sich wie­derum ein bißchen zu zanken, und aus diesem ganzen Zank kommt ja das heraus, daß ich selbst persönlich in der wüstesten Weise beschimpft werde. Ja, wenn sich das immer wieder und wieder wiederholt, so kommen wir nicht weiter.",
      "Wenn ich immer in der wüstesten Weise beschimpft werde, weil die andern zanken und ich ausgespielt werde, wenn es immer wiederum darauf hinauskommt, daß ich ausgespielt werde, so kann ich natürlich nicht mehr die anthroposophische Be­wegung in der Welt halten. Es wäre möglich, in positiver Weise bloß zu wirken, wenn man sich mehr auf das Positive verlegen wollte, das ich ja genügend immer wieder andeute.",
      "Es wäre möglich, solche Dinge hintanzuhalten, die zumeist auf furchtbar inferioren Dingen beruhen. Aber man hat in vielen Kreisen viel mehr Lust, zu zanken, viel mehr Lust, namentlich auch zum Dogmenstreit, aus dem sich",
      "dann oftmals persönliche Zänkereien herausentwickeln. Und dann wird es so, daß das Schimpfen sich gewöhnlich auf mich ablenkt - was mich ja persönlich höchst kühl läßt, aber die Bewegung kann nicht weiterbestehen, wenn es so weitergehen soll.",
      "Es ist nicht so, daß ich in diesem Fall tadie, was die Freunde in einem solchen Falle getan haben, aber ich mache darauf aufmerksam, daß sie etwas anderes nicht getan haben, was mir nicht zukommt, gerade in plumper Weise anzudeuten, wodurch aber in viel sicherer Weise verhindert würde dasjenige, was fortwährend geschieht, als auf die Weise, wie es fort­während versucht wird. Heute steht es schon so, daß man sagen kann: Wir haben Zyklen nur abgegeben an Mitglieder der Gesellschaft, und ich weiß, wie ich selber oftmals sonderbar von dem oder jenem aus der Gesellschaft angesprochen werde, wenn ich viel liberaler bin, als fernerstehende Mitglieder oftmals in der Abgabe von Zyklen sein wollen.",
      "Ja, schlimmer hätte es dem, was durch die Zyklen in die Welt gesetzt worden ist, durch Außenstehende niemals ergehen können, als es durch Mitglieder der Anthroposophischen Gesellschaft ge­schehen ist! Das muß man auch in Betracht ziehen.",
      "Wir sind heute schon durchaus so weit, daß die Zyklen in einer Weise mißbraucht werden durch Mitglieder, durch abgefallene Mitglieder der Anthro­posophischen Gesellschaft, daß es eigentlich sehr bald nahe daran sein kann, daß man sagt: Wir machen gar keine Grenze mehr, wir ver­kaufen die Zyklen an jeden, der sie haben will. - Es kann nicht viel schlechter werden.",
      "Ich sage nicht, daß es morgen schon geschehen soll, aber ich deute nur an, daß die Gesellschaft so gar nicht als Gesellschaft wirkt - immer außer dem Bau und außer einzelnen Kreisen -, daß sie gar nicht eigent­lich das macht, was sonst eine Gesellschaft macht. Damit ist die Ge­sellschaft gar keine Hilfe; sie ist gar nicht dasjenige, was eine Bewe­gung ergeben würde.",
      "Hier ist es so klar, daß ich niemanden persönlich meinen kann, daß ich ganz unbefangen dieses hier besprechen kann, aus dem einfachen Grunde, weil hier ja gerade die Stätte ist, wo eben fruchtbar aus der Gesellschaft heraus geschafft wird, nämlich am Bau. Der ist schon eine wirkliche Sache, die aus der Gesellschaft heraus entstanden ist.",
      "Und würden andere Dinge, die viel billiger sein könnten als der Bau, aus einem solchen Gesellschaftsgeiste heraus arbeiten, wie die Arbei­ter an unserem Bau, dann würde aus der Anthroposophischen Ge­sellschaft ungeheuer Segensreiches ersprießen können. Aber man muß dann das Weiße weiß und das Schwarze schwarz nennen. Man muß wirklich auch sagen, da wo persönliche Dinge vorliegen: das sind persönliche Dinge - und sie nicht in einen hohen Idealismus heraufschrauben; sonst wird man eben nachdenken müssen, was an die Stelle der Anthroposophischen Gesellschaft gesetzt werden muß. Eine Gesellschaft würde dann ja nicht an die Stelle gesetzt werden können, denn es würde ja wiederum dieselbe Misere sein! Nicht wahr, es kann nicht die Gesellschaft bloß ein Mittel sein, daß man sich herumbalgen sollte mit allen möglichen inferioren Persönlichkeiten. Aber sie ist ein Mittel geworden, das einen zwingt, immer wieder Rücksicht zu nehmen auf alles mögliche inferiore Zeug.",
      "Nun, ich will Sie heute nicht länger langweilen mit der Sache, son­dern ich wollte sie nur, nachdem die Zeit abgelaufen war, noch an­fügen. Ich habe den Vortrag vorher zu Ende geführt; solche Sachen sage ich nur, wenn die Vortragszeit abgelaufen ist, hinterher als An­satz."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Ich habe in der letzten Zeit hier eine Reihe von wichtigen Tatsachen über den Menschen vorgebracht, die geisteswissenschaftlich erforscht werden können.",
        "Ich lege weniger Wert darauf, daß die Einzelheiten dieser Tatsachen aufgefaßt werden - denn ich habe mich ja über die Natur dieser Tatsachen öfter ausgesprochen-, als vielmehr darauf, daß ein gewisser Eindruck durch diese Tatsachen erweckt werde: der Ein-druck über das Wesen desjenigen, was man die Täuschung der physischen Außenwelt nennen kann, auf daß Sie ein Gefühi davon erhalten, was eigentlich gemeint ist, wenn man davon spricht: Die Außenwelt, so wie wir sie um uns herum sehen - ich sage sehen, nicht haben -, ist Täuschung zunächst, und hinter ihr liegt die wahre, die wirkliche Welt.",
        "Und ich wollte ein gründlicheres Gefühi hervorrufen von dem, was gemeint ist, wenn man auf dem Boden der Geistes-wissenschaft von der wirklichen Welt spricht.",
        "Also mehr um diese allgemeinen Gefühie handelt es sich.",
        "Und damit bin ich an demjenigen Punkte angelangt, wo wir gewissermaßen wiederum eine Möglichkeit haben, unsere geisteswissenschaftlichen Betrachtungen anzuknüpfen an wichtige, an bedeutsame Interessen im Geistesleben der Gegen­wart, wobei ich natürlich an eine weitere Gegenwart denke, nicht bloß an die heutigen Tage, sondern an die Jahrhunderte, in denen wir leben."
      ],
      [
        "Unser Geistesleben ist in einem Zwiespalt begriffen, in einem Zwiespalt, den man in der verschiedensten Weise charakterisieren kann, den man so oder so definieren kann.",
        "Aber alle diese Definitionen müssen zuletzt wiederum zusammenlaufen in eine Art Empfindung für zwei Strömungen, die wir uns als Ideenströmungen bilden müssen aus der Geisteskultur der Gegenwart heraus, und die gewissermaßen sich nicht recht vereinigen lassen.",
        "Zwei Strömungen von Ideen sind vorhanden.",
        "Die eine, man kann sie im weitesten Sinne nennen die naturwissenschaftliche Strömung, wobei ich nicht etwa bloß das meine, was in den Kreisen der Naturforscher gedacht und behauptet wird, sondern jene naturwissenschaftliche Strömung, welche heute ja"
      ],
      [
        "mehr oder weniger in der Empfindung der ganzen Menschheit lebt.",
        "Diese naturwissenschaftliche Strömung ist nach und nach eine popu­läre, eine weitverbreitete Anschauung geworden.",
        "Sie produziert Be­griffe, die tief, tief sich eingewurzelt haben in das Seelenleben der Menschen der Gegenwart."
      ],
      [
        "Man kann am besten sehen, wie diese na­turwissenschaftliche Weltanschauung sich eingewurzelt hat, wenn man bedenkt, daß sie da am tiefsten Wurzel gefaßt hat, wo man glaubt, an spirituelles Leben heranzudringen.",
        "Schließlich ist ja dasjenige, was man landläufig Spiritismus nennt und was von sehr vielen als theo­sophische Theorie vertreten wird, nichts anderes als ein Ausfluß ma­terialistischer Weltanschauung."
      ],
      [
        "Dasjenige, was man zumeist an Be­griffen hat über Ätherleib, Astralleib, dasjenige, was man experimen­tell produziert in spiritistischen Sitzungen, wird ganz und gar einge­fangen in Begriffe, welche der naturwissenschaftlichen Weltanschauung entlehnt sind, was am besten solche Leute beweisen wie zum Beispiel du Prel, der glaubt, gerade auf die Geisteswelt loszugehen.",
        "Aber alles dasjenige, was er über die Geisteswelt sagt, denkt er in naturwissen­schaftlichen Begriffen, das heißt in solchen Begriffen, in denen man bloß über die Natur denken sollte, nicht über den Geist."
      ],
      [
        "Ebenso ist es geradezu auffällig, wie materialistisch doch die Theorien der mei­sten Theosophen sind, wie sie sich geradezu bemühen, Vorstellungen wie Ätherleib oder selbst Astralleib an die naturwissenschaftlichen Begriffe, die man nur auf die Natur anwenden sollte, heranzurücken.",
        "Der Ätherleib wird sehr häufig vorgestellt als etwas ganz Materielles, als ein feiner Dunst oder dergleichen."
      ],
      [
        "Nun, ich habe mich ja über diese Dinge öfter ausgesprochen."
      ],
      [
        "Dies ist die eine, ich möchte sagen Begriffsmasse, die wir haben:"
      ],
      [
        "die naturwissenschaftlichen Begriffe.",
        "Und weniger Wert - ich betone das noch einmal, damit ich nicht mißverstanden werde - ist darauf zu legen, daß diese naturwissenschaftlichen Begriffe in den Naturwissen­schaften selbst sich finden, wo sie ja zum großen Teil berechtigt sind, sondern das Wichtige ist, daß sie sich eben einschieichen in die allge­meine Weltanschauung, und daß sie verwendet werden, um Spiri­tuelles begreifen zu wollen, ja, daß manche geradezu in dem Wahne leben, sie sagten etwas Besonderes, wenn sie die Ähnlichkeit der Begriffe,"
      ],
      [
        "die sie im Spirituellen haben, mit den naturwissenschaftlichen Begriffen hervorheben."
      ],
      [
        "Die bedeutsame Tatsache, die wir da ins Auge fassen müssen, ist diese, daß diese naturwissenschaftlichen Begriffe nur eine gewisse Sphäre unserer Welt, eine gewisse Sphäre der Welt, in der wir leben, einfangen können in unser Verständnis, daß eine andere Welt außer unserem Verständnis bleiben muß, wenn wir nur naturwissenschaft­liche Begriffe anwenden.",
        "Diese naturwissenschaftlichen Begriffe bil­den also die eine Strömung."
      ],
      [
        "Die andere Strömung bilden gewisse Begriffe, die wir uns machen über Ideelles oder Jdeales, und wohl auch heute, schon seit langer Zeit, über Moralisches.",
        "Nehmen Sie einen naturwissenschaftlichen Begriff wie den Begriff der Vererbung oder den Begriff der Entwicke­lung."
      ],
      [
        "Sie denken naturwissenschaftlich, wenn Sie diesen Begriff rein­lich und sauber denken; Sie denken verworren, wenn Sie diese Begriffe von Vererbung und von Entwickelung, wie sie in der Naturwissen­schaft üblich sind, auf Spirituelles ausdehnen.",
        "Nehmen Sie gewisse Begriffe, die man im Leben braucht, zum Beispiel den Begriff der inneren Freiheit unserer Seele, den Begriff des Wohlwollens, den Be­griff der sittlichen Vollkommenheit, oder höhere Begriffe, den Begriff der Liebe und dergleichen, so haben Sie wiederum eine Strömung von Ideen, von Begriffen, die auch berechtigt sind, weil sie ja zum Leben gebraucht werden."
      ],
      [
        "Aber nur wenn man sich einer Selbsttäuschung hingibt, kann man sich von der Art, wie heute naturwissenschaftlich gedacht wird, zu der Art, wie heute ideal oder ideell oder moralisch gedacht wird, eine Brücke bauen.",
        "Denkt jemand rein naturwissen­schaftlich, das heißt, sucht er sich ein naturwissenschaftliches Welt­bild, so wie das heute das Ideal vieler Leute ist, so hat innerhalb einer Welt, welche diesem Weltbild entspricht, alles das keinen Platz, was unter Begriffe wie Wohlwollen, meinetwillen auch Glück, Liebe, innere Freiheit und so weiter gefaßt ist."
      ],
      [
        "Ein gewisses Ideal natur-wissenschaftlicher Denkungsart ist, alles, wie man sagt, unter den Kausalbegriff zu bringen, alles nach Ursachen und Wirkungen zusammenzudenken.",
        "Und eine sehr beliebte Verallgemeinerung ist -ich habe das schon hier erwähnt - das Gesetz von der Erhaltung der"
      ],
      [
        "Kraft und der Erhaltung des Stoffes.",
        "Bilden Sie sich eine Weltan­schauung so, daß Sie dazu nur die Begriffe von Ursache und Wirkung im naturwissenschaftlichen Sinne verwenden oder von der Erhaltung der Kraft und des Stoffes, so können Sie nur entweder weltanschau­lich unehrlich sein, oder Sie müssen sagen: Innerhalb einer solchen Weltenordnung, in welcher nur das Kausalitätsgesetz, nur das Ur­sachengesetz gilt, oder in welcher das Gesetz von der Erhaltung des Stoffes und der Kraft gilt, in einer solchen Welt ist alles, was Ideale sind, was Ideen sind, was moralische Begriffe sind, im Grunde ge­nommen eigentlich nur Spaß. - Denn für eine Weltanschauung, welche etwa das Gesetz von der Erhaltung der Kraft und des Stoffes univer­sell denkt, hat nichts anderes Sinn, als sich zu sagen: Nach diesem Gesetze von der Erhaltung der Kraft und des Stoffes entwickelt sich unsere Weltenordnung. - Aus gewissen Ursachen heraus ist inner­halb dieser Weltenordnung auch das Menschengeschlecht hervorge­gangen."
      ],
      [
        "Dieses Menschengeschlecht träumt von Wohlwollen, von Liebe, von innerer Freiheit, aber all das sind Begriffe, die sich die Menschen machen, und wenn einmal jener Zustand eingetreten sein wird in unserem Weltensystem, der eintreten muß nach naturwissen­schaftlichen Vorstellungen, dann ist eigentlich ein allgemeines Grab da für alle solche Vorstellungen von Wohlwollen, innerer Freiheit, von Liebe und so weiter.",
        "Das sind Träume, welche die Menschen träumen, während sie eben der reinen naturgesetzlichen Ordnung gemäß ihr Dasein innerhalb der Erdenentwickelung vollenden, und es hat gar keinen Sinn, von etwas anderem zu sprechen in bezug auf die Geltung der Ideale und Ideen, als davon, daß sie Träume der Menschen sind, denn innerhalb einer solchen naturwissenschaftlichen Weltanschauung haben Ideen und Ideale keine Kraft, sich zu realisie­ren."
      ],
      [
        "Was sollen denn, wenn die Welt wirklich entsprechen würde der naturwissenschaftlichen Weltanschauung, die Ideen und Ideale einmal machen, sobald der Zustand eingetreten ist, den man notwendig denken muß, wenn man nur mit naturwissenschaftlichen Begriffen denkt?",
        "Sie sind begraben, die Ideen und Ideale!"
      ],
      [
        "Die Ideen und Ideale werden heute aber von den Menschen so gedacht - wenn sie das auch nicht zugeben -, daß sie keine innere Kraft haben, sich zu realisieren."
      ],
      [
        "Sie sind eben bloße Gedanken, die sich dadurch realisieren, daß die Menschen ihre Gefühle daran hängen, daß die Menschen sich gegen­einander so verhalten, wie es den Ideen entspricht.",
        "Aber sie haben keine innere Kraft, sich zu realisieren, diese Ideen, wie es der Magne­tismus, wie es die Elektrizität oder die Wärme hat - die hat innere Kraft, sich zu realisieren!",
        "Die Ideen als solche - denken Sie also immer meinetwiller an die moralischen Ideen - haben nicht eine solche innere Kraft, sich zu realisieren innerhalb unserer Weltanschauung, wenn wir sie nur naturwissenschaftlich denken."
      ],
      [
        "Gewiß, die wenigsten Menschen machen sich den Zwiespalt klar, der zwischen diesen zwei Strömungen unserer Gegenwart besteht, aber er ist da, und es ist die Tatsache, daß er im Unterbewußtsein der Menschen sein Spiel treibt, viel wichtiger, als daß man sich theore­tisch darüber klar ist.",
        "Theoretisch klar ist sich nur eine Schichte der Menschen über das, was ich eben gesagt habe, und diese eine Schichte der Menschen, auf die sollte man wohi ein Auge haben im Leben der Gegenwart."
      ],
      [
        "Klar ausgesprochen, daß die Sache so ist, daß die ganze Welt nur naturwissenschaftlich geordnet ist und daß Ideen und Ideale nur eine Bedeutung haben deshalb, weil die Menschen nun einmal das Gefühl haben, sie müßten sich geradezu danach richten in ihrem gegenseitigen Verhalten, findet man diese Anschauung nur innerhalb der sozialistischen Theorie der Gegenwart.",
        "Die sozialistische Theorie der Gegenwart lehnt daher jede Geisteswissenschaft ab, betrachtet sogar die Spuren alter Geisteswissenschaft, die sich noch in der Juris­prudenz, in der Moral und der Theologie finden, als Vorurteile, die den Kinderjahren der Menschheitsentwickelung angehören, und sie will alles, was man Geisteswissenschaft nennen könnte, als Gesell­schaftswissenschaft aufgefaßt wissen: sie will die sozialistische Gesell­schaftswissenschaft bilden als bloß gültig für das gegenseitige Ver­halten der Menschen."
      ],
      [
        "Die Welt ist naturwissenschaftlich geordnet, und außer der naturwissenschaftlichen Erklärung der Welt gibt es nur noch eine Gesellschaftswissenschaft.",
        "Das ist Grundüberzeugung jedes seiner selbst bewußten Sozialisten."
      ],
      [
        "Man darf, wenn man solchen Dingen auf den Grund gehen will, nicht konfusen Begriffen sich hingeben.",
        "Ich weiß selbstverständlich,"
      ],
      [
        "daß man kommen kann und sagen: Ja, so denken doch nicht die Sozialisten! - Aber darauf kommt es nicht an - das habe ich ja gerade in den ersten Tagen, in denen ich hier wieder vorgetragen habe, aus­geführt -, was Ideen für einen Inhalt haben, sondern durch was Ideen sich betätigen, wie sie eindringen, sich einleben.",
        "Und die sozialisti­sche Idee lebt sich dadurch ein, daß sie ablehnt jedes Reden über irgendeinen geistigen Weltinhalt, daß sie behauptet, der Weltinhalt sei nur naturwissenschaftlich geordnet und Geisteswissenschaft sei durch bloße Gesellschaftswissenschaft zu ersetzen."
      ],
      [
        "Nun fühit der Mensch, daß bloße Ideen und Ideale, wenn sie so gedacht werden, wie sie in der Gegenwart gedacht werden, eben wirklich nicht mehr Kraft haben, als sich in das menschiiche Gemüts-leben hineinzufinden und sich dadurch zu realisieren, zu realisieren als ein Traum, den die Menschheit innerhalb der Erdenentwickelung träumt.",
        "Keine Idee, und wäre sie die schönste, die idealste, hat die Kraft, irgend etwas wachsen zu lassen, irgendwo Wärme zu erzeugen, einen Magneten zu bewegen oder dergleichen.",
        "Damit ist sie schon ver­urteilt, bloßer Traum zu sein, weil sie ja - solange man die Welten-ordnung nur denkt als die Summe von elektrischen, magnetischen Kräften, von Lichtkräften, Wärmekräften und so weiter - in das Gefüge dieser Kräfte nicht eingreifen kann, insbesondere wenn man das Gesetz von der Erhaltung der Kraft und des Stoffes aufstellt, wo­nach Kraft und Stoff eine ewige Geltung haben sollen.",
        "Denn dann sind sie immer da, und dann können Ideen nirgends eingreifen, denn Kraft und Stoff haben dann ihre eigenen, ewigen Gesetze."
      ],
      [
        "Mit diesem Gesetze - das sage ich nur in Parenthese - von der Er­haltung der Kraft und des Stoffes wird ja viel Unfug getrieben.",
        "So wie man in der Literatur heute von dem Gesetz der Erhaltung der Kraft und des Stoffes, namentlich von Kraft und Energie gesprochen findet, wird es auch häufig zurückgeführt auf Julius Robert Mayer.",
        "Wer Julius Robert Mayers Schriften wirklich kennt, der weiß, daß es ebenso gescheit ist, das Gesetz von der Erhaltung der Kraft und des Stoffes auf Julius Robert Mayer zurückzuführen, so wie es heute in der Literatur geschieht, wie wenn man etwa die Schundliteratur auf die Erfindung der Buchdruckerkunst durch Gutenberg zurückführte."
      ],
      [
        "Denn das, was heute in Lehrbüchern und gebräuchlichen Hand­büchern als Gesetz von der Erhaltung der Kraft und des Stoffes fun­giert, das hat mit dem Gesetz von Julius Robert Mayer, den man für seine Tat ins Irrenhaus eingesperrt hat, nichts zu tun."
      ],
      [
        "Nun entsteht eigentlich für den, der Geisteswissenschaft ernst nimmt, aus alledem, was ich dargestellt habe, eben die Frage: Welches Verhältnis, welcher Bezug besteht zwischen dem, was nimmer ver­einigt werden kann innerhalb der gegenwärtigen Weltanschauung: moralischem Idealismus und naturalistischem Anschauen der Welt? -Diese Frage läßt sich nicht so ohne weiteres theoretisch beantworten.",
        "Die Gegenwart wünscht vielfach theoretische Antworten, und auch diejenigen, die zur Theosophie oder Anthroposophie kommen, wün­schen manchmal am allermeisten theoretisch-dogmatische Antworten."
      ],
      [
        "Aber die Antworten, die auf dem Boden der Geisteswissenschaft ge­geben werden sollen, müssen Antworten der Anschauung sein.",
        "In dieser Beziehung geht es nicht, daß man gerade die Vorliebe der Gegenwart für Dogmatismen auch wiederum in die Geisteswissen­schaft hineinträgt."
      ],
      [
        "Die Geisteswissenschaft verlangt anderes.",
        "Die Geisteswissenschafter verlangen freilich vielfach, daß andere Dogmen aufgestellt würden, aber die Geisteswissenschaft kann ganz und gar nicht der Ansicht sein, daß bloß andere Dogmen aufgestellt werden, als sie schon aufgestellt sind, sondern daß anders gedacht und anders angeschaut werde, daß überhaupt gewisse Dinge unter ganz andern Gesichtspunkten gedacht werden."
      ],
      [
        "Dasjenige, was vielfach heute auch als Geisteswissenschaft, namentlich auch als Theosophie getrieben wird, das kann einem oftmals den Eindruck machen einer etwas ver­änderten Scholastik des Mittelalters.",
        "Ich will mich gar nicht gegen Scholastik wenden, denn die Scholastik hat Dinge in sich, die viel bedeutsamer sind als dasjenige, was philosophisch in der Gegenwart hervorgebracht wird."
      ],
      [
        "Aber der Hang vieler Menschen in der Gegen­wart ist dahingehend, nur wiederum andere Dogmen zu haben, über Gott und Unsterblichkeit und weiß Gott was, eben anders zu denken, aber eben doch nur zu denken, nicht zu Anschauungen zu kommen, die aus ganz anderem Fond heraus sind als frühere Vorstellungen.",
        "Steht man recht auf dem Boden der Geisteswissenschaft, so sagt man sich:"
      ],
      [
        "Zur Zeit der Scholastik ist über die Dreieinigkeit, über das Wesen des Menschen, über seine Unsterblichkeit, über das Christus-Problem genug spintisiert worden, wenn ich den Ausdruck jetzt gar nicht mit irgendeinem üblen Beigeschmack anwende.",
        "Denn der eigentliche Wert dieser Scholastik liegt nicht in den Dogmen, die sie aufgestellt hat, sondern in der Technik des Denkens, wie ich es einmal darge­stellt habe in meiner Schrift «Philosophie und Anthroposophie», die jetzt in einer neuen Auflage wesentlich erweitert wiederum erscheinen wird; er liegt in der Art, über die Dinge zu denken."
      ],
      [
        "Aber dieses Den­ken, das eignet man sich heute eigentlich besser an, wenn man zu den Scholastikern geht, als wenn man zu den vielfach konfusen Ideen, die man in der neueren Zeit theologische oder philosophische nennt, sich hinwendet.",
        "Da ist genug theoretisiert worden im Mittelalter über diese Dinge."
      ],
      [
        "Da hat man zum Beispiel so theoretisch mit dem Christus-Problem gerungen.",
        "Wer das Wesen dieses Ringens kennt, der kann nicht viel Geschmack abgewinnen einem etwas veränderten Schola­stizieren, wie es zum Beispiel in der Theosophie vielfach getrieben worden ist, wo man halt, statt daß man früher, nicht wahr, Dreieinig­keit, Unsterblichkeit oder anderes hatte, nun wiederum physischen Leib, Ätherleib, Astralleib hat."
      ],
      [
        "Es ist ein anderes Theoretisieren, aber es ist im Grunde genommen qualitativ dieselbe Sache.",
        "Derjenige, der recht eingehen mag auf diese Schule des Mittelalters, der weiß, daß das gewissermaßen eine erledigte Angelegenheit ist, so vordringen zu wollen, sagen wir, zu dem Mysterium von Golgatha."
      ],
      [
        "Da ist heute viel wichtiger, zum Beispiel nach der Gestalt des Christus Jesus zu dringen, was versucht wird von uns hier in der Mittelpunktsgruppe des Baues, wo gesucht wird, die Gestalt des Christus Jesus wirklich wiederum zu finden.",
        "Derjenige, der sich richtig für frühere Dogmen interessiert, wird sich heute viel mehr dafür interessieren, die Ge­staltung des Christus aus dem geistigen Leben herauszuholen, weil heute die Zeit dazu da ist, dies zu tun."
      ],
      [
        "Im Mittelalter war die Zeit, scharfsinnig nachzudenken und scholastische Begriffe auszuspinti­sieren; heute - das habe ich ja vielfach charakterisiert - ist ein solcher Punkt der fünften nachatlantischen Zeit, wo hingelenkt werden muß die Anschauung der Menschen nach den geistigen Formen.",
        "Dasjenige,"
      ],
      [
        "was früher als Gestaltung des Christus gesucht wurde, sind ja phan­tastische Gestaltungen.",
        "Ich habe über die Entwickelung der Christus-gestalt ja öfter hier gesprochen.",
        "Mit den Mitteln der geistigen An­schauung wird sich die Gestalt des Christus wiederum finden lassen.",
        "So hat jede Zeit ihre besondere Aufgabe.",
        "Denn nicht darauf kommt es an, daß irgend etwas festgelegt wird, sondern darauf, daß die Mensch­heit in ihrer Entwickelung sucht und dadurch sich zu immer weiteren und weiteren Stufen ihrer Entwickelung durchringt."
      ],
      [
        "Also darauf kommt es an, daß man gewissermaßen eine Brücke finden kann da, wo die moderne Weltanschauung eine Brücke eben nicht finden kann, sondern wo, wenn sie sich selbst richtig versteht, sie notwendigerweise zum Sozialismus, das heißt zur sozialistischen Theorie kommen muß - nicht zum Sozialismus in seiner Berechti­gung; darüber habe ich ja auch schon öfter gesprochen.",
        "Diese Brücke kann man aber nur finden, wenn man den ehrlicher Willen hat, eben­so wie man in dasjenige eindringt, was zwischen der Geburt und dem Tode verläuft, auch in dasjenige einzudringen, was zwischen dem Tode und einer neuen Geburt verläuft, wenn man also nicht bloß den Willen hat, gewissermaßen die Welt hier zu analysieren, sondern wenn man den Willen hat, sich wirklich auf das Geistige einzulassen."
      ],
      [
        "Man redet von dem Menschen und sagt: Der Mensch besteht aus physischem Leib, Ätherleib, astralischem Leib, Ich und so weiter. - Das ist ge­wiß berechtigt; aber es ist für den Menschen berechtigt, der hier zwischen der Geburt und dem Tode lebt.",
        "Das, was ich das vorige Mal und das vorvorige Mal hier ausgeführt habe, das kann Sie aber schon darauf hinweisen, daß man in einer ähnlichen Weise nun reden kann über den Menschen nach dem Tode, über den Menschen zwischen dem Tode und einer neuen Geburt."
      ],
      [
        "Wenn Sie schon fragen wollen: Aus was besteht der Mensch? - so können Sie nicht bloß fragen: Aus was besteht der Mensch hier auf Erden? - und antworten: Da besteht er aus physischem, Ätherleib, Astralleib und Ich -, sondern wir müssen jetzt auch die Frage aufwerfen: Aus was besteht der Mensch, wenn er nicht auf Erden ist, sondern in einer geistigen Welt zwischen Tod und neuer Geburt?",
        "Wie kann man da von den Gliedern der mensch­lichen Natur reden? - Da muß man in ebenso realer Weise von den"
      ],
      [
        "Gliedern der menschlichen Natur reden können.",
        "Und man muß sich, wenn man ganz ehrlich bei einer solchen Sache mit sich zu Rate geht, eben bewußt werden, daß jedes Zeitalter seine besondere Aufgabe hat."
      ],
      [
        "Die Menschen werden sich nicht recht bewußt, daß eigentlich die Art, wie sie denken, vorstellen, selbst wie sie empfinden, ja, selbst wie sie die Außenwelt anschauen - erinnern Sie sich nur an gewisse Ausführungen, die ich in meinen «Rätseln der Philosophie» gemacht habe über den verhältnismäßig kurzen Zeitraum von sechshundert Jahren vor unserer Zeitrechnung bis zu uns -, eben nur jetzt so ist.",
        "Wir können nicht über das 8."
      ],
      [
        "Jahrhundert vor dem Mysterium von Golgatha zurückgehen mit dem Denken und dem Empfinden und dem Anschauen, das wir jetzt haben.",
        "Ich habe Ihnen das genaue Jahr angegeben: 747 vor dem Mysterium von Golgatha ist die wahre Gründungszahi der Stadt Rom."
      ],
      [
        "Wenn man hinter dieses 8. vorchrist­liche Jahrhundert zurückgeht, dann ist die ganze Art des mensch­lichen Lebens eine andere als diejenige, die man jetzt als Seelenieben eben kennt.",
        "Da werden alle Arten, die Welt anzuschauen, anders."
      ],
      [
        "Da ist allerdings eine Grenzscheide, die man schon besser beobachten kann als die andere, die eigentlich auch gut zu beobachten ist, aber noch nicht für den Menschen der Gegenwart: die Grenzscheide, die im 15.",
        "Jahrhundert liegt."
      ],
      [
        "Das 15.",
        "Jahrhundert liegt den Menschen der Gegenwart zu nahe; da können sie sich nicht so recht in den großen Umschwung hineinversetzen, der da eingetreten ist.",
        "Im ganzen stellen sich die Menschen vor: gedacht und gesonnen hat man immer so wie jetzt, auch wenn man immer weiter zurückgeht; aber wie wenig weit geht man zurück!"
      ],
      [
        "Nun ja, die Sache ist eben diese, daß, sobald man hinter das 8. vorchristliche Jahrhundert zurückgeht, man eine ganz andere Art zu denken hat.",
        "Und nun können wir die Frage aufwerfen:"
      ],
      [
        "Warum hatte man denn da eine andere Art zu denken?",
        "Über diese andere Art zu denken machen sich die Menschen jetzt, wenn sie sich Vorstellungen machen, ziemlich törichte Vorstellungen, könnte man sagen.",
        "Wenn die Menschen der Gegenwart jetzt hören, wie, sagen wir, in den ägyptischen Mysterien - es waren dazumal die gesuchtesten -gelehrt worden ist, wenn sie etwas hören von der Art, wie da die Wahrheiten erörtert worden sind, da meinen sie: Nun ja, das entspricht"
      ],
      [
        "eben der phantastischen Zeit von dazumal, da waren die Men­schen noch nicht so gescheit wie jetzt, da haben sie sich noch kin­dische Vorstellungen gemacht; das Richtige, das haben wir jetzt! -Es liegt besonders dem Menschen der Gegenwart nahe, so zu denken, denn er kann sich, weil er so furchtbar eingerutscht ist in diese Denk­weise der Gegenwart, nicht irgend etwas anderes dabei denken.",
        "Nehmen wir an, ein Grieche, Pythagoras zum Beispiel, sei nach Ägyp­ten gekommen und hätte dort gelernt, so wie heute irgend jemand nach einer berühmten Universität geht, um zu lernen.",
        "Aber was hat er gelernt?",
        "Ich will Ihnen etwas sagen, was der Pythagoras wirklich dort hat lernen können: Er hat dort gelernt, daß in Urzeiten der Merkur mit dem Monde einmal Schach gespielt hat, und bei diesem Schachspiel hat der Merkurius gewonnen.",
        "Er hat nämlich dem Monde für jeden Tag zwanzig Minuten abgewonnen, und diese zwanzig Minuten, die sind dann von den Eingeweihten zusammengezählt worden.",
        "Wieviel machen sie aus, diese zwanzig Minuten in drei­hundertsechzig Tagen?",
        "Die machen nämlich gerade fünf Tage aus.",
        "Daher hat man nicht dreihundertsechzig Tage als das Jahr gerechnet, sondern dreihundertfünfundsechzig Tage.",
        "Diese fünf Tage sind das­jenige, was der Merkur dem Monde im Spiel abgewonnen hat, und was er dann den übrigen Planeten und dem ganzen Menschenge­schlecht zu dreihundertsechzig Tagen im Jahr hinzugeschenkt hat."
      ],
      [
        "Nun, nicht wahr, wenn man sagt, so etwas habe der Pythagoras bei den weisen Ägyptern lernen können, dann lacht jeder Mensch in der Gegenwart, ganz selbstverständlich.",
        "Dennoch ist es nur eine andere Binkleidung für eine tiefe geistige Wahrheit - wir werden davon in diesen Tagen noch sprechen -, die die Gegenwart noch gar nicht wieder entdeckt hat, die aber eine Wahrheit ist."
      ],
      [
        "Sie könnten fragen: Warum ist dazumal ganz anders gerechnet worden? - Vergleichen Sie den Vortrag eines solchen ägyptischen Weisen, der also dem krassen Fuchs Pythagoras vorträgt: Der Mer­kur hat im Schachspiel für jeden Tag dem Monde zwanzig Minuten abgewonnen - mit einem Vortrag über moderne Astronomie, der in einem Hörsaal gehalten wird, so werden Sie besser auf den Unter­schied aufmerksam werden.",
        "Fragt man sich aber: Warum ist ein"
      ],
      [
        "solcher Unterschied? - dann muß man etwas tiefer hineingehen in das ganze Wesen der menschlichen Enwickelung.",
        "Denn wenn man hinter das 8. vorchristliche Jahrhundert zurückgeht - Pythagoras gehört zwar nicht dieser frühen Zeit an, aber in Ägypten haben sich die Reste einer Weisheit, die eben weit vor dem 8. vorchristlichen Jahr­hundert begründet worden ist, erhalten, da konnte man sie sich noch einprägen -, wenn in diesen alten Zeiten so gelehrt worden ist, so hat das schon seinen tiefen Grund.",
        "Es war das ganze Verhältnis des Menschen zur Welt anders angesehen worden, mußte anders in der damaligen Zeit angesehen werden."
      ],
      [
        "Ich möchte darauf hinweisen, daß ja noch verschiedene Reste alter Anschauung immer wieder und wieder atavistisch erneuert worden sind, wobei ich unter dem Wort «atavistisch» nicht irgend etwas Ab­fälliges meine und verstehe.",
        "Wer zum Beispiel ein Werk liest, wie Jakob Böhmes «De signatura rerum», der wird, wenn er ehrlich ist, eigentlich auch heute sagen: er kann nichts damit anfangen."
      ],
      [
        "Denn da werden ganz merkwürdige Auseinandersetzungen gegeben, die ent­weder von einem höheren Gesichtspunkte aus beurteilt werden müs­sen - dann bekommen sie einen Sinn -, oder aber die vom Stand­punkte des modern denkenden Menschen als unvernünftiges Zeug eines Laien, der ein bißchen spintisiert hat, eigentlich abgelehnt wer­den müßten.",
        "All das tolle Gerede, das vielfach getrieben wird von unreifen theosophischen Kreisen über Jakob Böhme, ist eigentlich vom Übel."
      ],
      [
        "Dennoch erinnert dieser Jakob Böhme von einem höheren Standpunkte aus in seinem ganzen Geistesgefüge, in der Art, wie er sich namentlich zur Analyse von gewissen Worten verhält, wenn er zum Beispiel Worte wie Sulfur zerlegt und in den zerlegten Teilen etwas sucht - wir wollen nicht auf das Materielle dabei sehen, sondern auf die Art, wie er da etwa in seinem Werke «De signatura rerum» vorgeht -, er erinnert viel mehr als irgendeine von den abstrakten Wissenschaften, die es ja nur heute in der Öffentlichkeit gibt, an einen gewissen konkreten Zusammenhang des Menschen mit der gesamten geistigen Welt.",
        "Er steht, dieser Jakob Böhme, viel mehr in dieser geistigen Welt darinnen."
      ],
      [
        "Und dieses Darinnenstehen in der geistigen Welt, das ist das Charakteristische für solche Denker, die vor dem 8."
      ],
      [
        "vorchristlichen Jahrhundert, vor unserer Zeitrechnung eben Denker waren.",
        "Sie dachten nicht mit der individuellen Einzelvernunft, mit der wir heute denken.Wir denken ja alle mit der individuellen Einzelver­nunft; die dachten mehr noch mit der kosmischen Vernunft, mit der schöpferischen Vernunft, mit der Vernunft, die man, ich möchte sagen, in einzelnen ihrer Schöpfungen noch erlauschen muß wenn man auf sie kommen will."
      ],
      [
        "Heute gibt es eigentlich nur noch ein Gebiet, in dem man ein klein wenig merken kann, wie ins Menschenleben noch so etwas wie die schöpferische Vernunft sich hereinergießt und hereinwirkt.",
        "Man kann noch auf einem Gebiet etwas bemerken von einem Sich-Realisieren von Ideellem; aber, ich möchte sagen, es ist nur noch ein Schatten davon da, und dieser Schatten wird zumeist auch nicht berücksichtigt."
      ],
      [
        "Es existieren heute eine ganze Anzahi von naturalistischen anthropo­logischen Theorien über die Entstehung der Sprache, wie sie sich entwickelt haben soll.",
        "Sie wissen, es gibt - ich habe das öfter erwähnt -zwei hauptsächliche Theorien."
      ],
      [
        "Man nennt die eine die Wauwau-Theorie, die andere die Bimbam-Theorie.",
        "Die Wauwau-Theorie ist mehr von kontinentalen Gelehrten vertreten, die Bimbam-Theorie ist von Max Müller vertreten.",
        "Die Wauwau-Theorie beruht darauf, daß Menschen von primitivsten Zuständen ausgegangen sind und da ihre inneren organischen Erlebnisse so herausgebellt haben wie der Hund, wenn er «wauwau» macht, und durch eine entsprechende Ent­wickelung - alles entwickelt sich ja, nicht wahr, vom Primitiven bis zum Vollkommenen - ist das Wauwau des Hundes, das heute noch beim Menschen auf seiner primitiven Stufe zu bemerken ist, zur menschlichen Sprache geworden."
      ],
      [
        "Wenn man alles in der Entwicke­lung verfolgt vom Wauwau bis zum heutigen Sprechen, so ähnlich, nicht wahr, wie es die Deszendenztheorie macht, Darwin oder Haeckel, beginnend mit der einfachsten Monere, also von der einfachsten Weise, von der unartikuliertesten Weise bis zu der heutigen Sprache, dann ist das eben die Wauwau-Theorie.",
        "Eine andere Theorie besagt, daß man ein gewisses Gefühi entwickeln kann der Verwandtschaft mit den Tönen der Glocke: Bimbam; man hätte jedesmal einen bestimm­ten inneren Klang, den man imitiert."
      ],
      [
        "Danach würde man mit dem"
      ],
      [
        "Wauwau mehr eine Evolutionstheorie verfolgen, mit der Bimbam­Theorie mehr eine Anpassungstheorie, eine Anpassung des Menschen an die innere Natur der materiellen Worte.",
        "Dann kann man ja auch geistreich die Dinge verbinden, die Bimbam-Theorie mit der Wauwau-Theorie, das ist dann etwas Vollkommeneres, dann hat man Ent­wickelung mit Anpassung verbunden.",
        "Nun ja, diese Dinge sind heute mehr oder weniger gang und gäbe.",
        "Es gibt auch solche, die über diese beiden Theorien lachen und die andere Theorien haben; aber im Prinzip sind sie eben auch nicht viel anders."
      ],
      [
        "Geistig betrachtet, geistig angeschaut kann gar keine Rede davon sein, daß die Sprachentwickelung eine solche ist, wie sie eben cha­rakterisiert worden ist, sondern schon rein äußerlich zeigt das Ge­füge der Sprache, daß im Sprachbilden, im Entstehen der Sprache wirkliche Vernunft waltet.",
        "Und zwar ist es interessant, gerade an der Sprache das Walten der Vernunft festzuhalten, aus dem einfachen Grunde, weil am anschaulichsten noch in der Sprache ein ideelles Moment lebt, also dasjenige, was in der einen Strömung heute ange­schaut wird, und weil die Sprache nicht bloß an das Gemüt des Men­schen sich wendet, sondern ihre eigene Gesetzmäßigkeit hat, also das Ideelle in einer gewissen Weise sich in ihr schon realisiert, wenn auch gegenüber natürlichen Gesetzen schattenhaft."
      ],
      [
        "Nehmen Sie zum Bei­spiel ein Wort - ich will Sie nur auf ein paar sehr elementare Fälle auf­merksam machen -, wo Sie sehen können, wie innere Vernunft im Sprachentstehen waltet; nehmen Sie ein Wort wie: Oratio, die Rede.",
        "Es ist nun merkwürdig, wenn man solch ein Wort nimmt wie Oratio, die Rede, und dann beobachtet, was aus diesem Worte wird im Leben des Menschen nach dem Tode, so stellt sich eine merkwürdige Ähn­lichkeit ein mit dem, was als werdende Vernunft in der Entwickelung der Sprache gewirkt hat."
      ],
      [
        "Das gibt gewisse Sicherheiten, die man heute auf einem andern Weg kaum gewinnen kann.",
        "Auf einem andern Wege kann man höchstens Hypothesen gewinnen.",
        "Der Tote wird selten, wenigstens nachdem eine bestimmte Zeit seit dem Tode verflossen ist, das Wort Oratio noch verstehen; er wird es nicht mehr verstehen, er verliert das Verständnis dafür."
      ],
      [
        "Dagegen wird er immer noch ver­stehen eine Anschauung, eine Imagination, welche zurückführt auf"
      ],
      [
        "das, was man ausdrücken kann durch die Worte: Os, Oris, Mund, und: Ratio, Vernunft.",
        "Der Tote löst das Wort Oratio auf in Os und Ratio.",
        "Und in der Entwickelung hat sich der umgekehrte Vorgang wirklich abgespielt: Das Wort Oratio ist wirklich entstanden durch eine Synthesis ursprünglicher Wörter, Os und Ratio.",
        "Oratio ist kein so ursprüngliches Wort wie Os, Oris und Ratio, sondern Oratio ist aus Os und Ratio gebildet."
      ],
      [
        "Ein paar solcher elementarer Dinge möchte ich Ihnen anführen.",
        "Diese Dinge können am anschaulichsten noch an der lateinischen Sprache studiert werden, weil sie da am deutlichsten noch zutage treten, es sind aber die Gesetze, die dabei gefunden werden können, auch für andere Sprachen von Bedeutung.",
        "Nehmen Sie zum Beispiel drei ursprungliche Worte: Ne ego otior; das würde heißen, wenn man es als Wort nimmt: Ich bin nicht müßig.",
        "Ego otior: Ich bin müßig; ne ego otior: Ich bin nicht müßig.",
        "Diese drei Worte setzen sich durch die waltende kosmische Vernunft zusammen in Negotior, das heißt:"
      ],
      [
        "Handel treiben.",
        "Da haben Sie drei Worte in eins zusammengefügt, und Sie sehen vernunftmäßig den Aufbau der Worte.",
        "Sie sehen Vernunft walten in der Entwickelung der Sprache."
      ],
      [
        "Ich würde, wie gesagt, dieses nicht so strikte behaupten, wenn nicht die merkwürdige Tatsache eintreten würde, daß der Tote das, was hier in der Welt zusammengefügt worden ist, wiederum auflöst.",
        "Der Tote löst wiederum so etwas wie das Negotior auf in: Ne ego otior, und er versteht nur diese drei Worte beziehungsweise Anschauungen, die er sich aus dieser Trinität zusammenfügt, und er vergißt dasjenige, was durch die Zusammenfügung entstanden ist."
      ],
      [
        "Ein anderes naheliegendes Beispiel ist: Unus, der eine, und Alterque, der andere; das ist zusammengezogen in das lateinische Wort Uterque, jeder von beiden.",
        "Wir könnten recht froh sein, wenn wir in den mo­dernen Sprachen ein solches Wort hätten wie Uterque, das jenen Be­griff gibt; der Franzose kann es höchstens ausdrücken, indem er bei dem oberen bleibt: l'un et l'autre; er hat nicht einen einzigen Begriff, um das auszudrücken.",
        "Aber Uterque drückt das viel präziser aus."
      ],
      [
        "Nehmen Sie einen Fall, damit Sie sehen, welches Prinzip ich eigent­lich meine.",
        "Sie alle kennen selbstverständlich das Wort «se», das französische"
      ],
      [
        "Wort «se»: sich.",
        "Sie kennen das Wort «hors»: außer sich, her­aus, könnte man auch sagen, und «tireD> - ich behalte davon nur das «tir» bei -: «tiD>, ziehen, sich wegziehen.",
        "Wenn Sie diese drei Dinge dann nach demselben Prinzip zusammensetzen, so bekommen Sie hier das «sortir», weggehen, was nichts anderes ist als eine Zusammen-fügung von «se hors tir»; «tir» ist der Rest des Wortes «tirer».",
        "Da sehen Sie noch in einer modernen Sprache diese selbe waltende Ver­nunft darinnen.",
        "Oder nehmen Sie ein Beispiel, wo die Sache etwas dadurch kaschiert ist, daß verschiedene Sprachstufen wirken: «cceur», das Herz; «rage», das ist das Lebendige, das sich Belebende, der Enthusiasmus, der vom Herzen ausgeht; zusammengesetzt: «cou­rage».",
        "Das sind nicht irgendwelche Erfindungen, sondern das sind reale Geschehnisse, die wirklich da waren.",
        "So sind die Worte ge­bildet."
      ],
      [
        "Aber die Möglichkeit, so Worte zu bilden, sie ist heute nicht mehr da.",
        "Heute hat sich der Mensch herausgestellt aus dem lebendigen Zu­sammenhang mit der kosmischen Vernunft, und daher kann höch­stens noch in ganz sporadischen Fällen eine Möglichkeit vorhinden sein, sich heranzuwagen an die Sprache, um irgendwelche Worte aus der Sprache herauszuholen, die, wie man sagt, im Geiste der Sprache sind.",
        "Aber je weiter man zurückgeht, und namentlich je weiter man zurückgeht hinter das 8. vorchristliche Jahrhundert, auch bei der griechischen, bei der lateinischen Sprache, desto mehr ist im leben­digen Leben das Prinzip tätig, daß in dieser Weise gerade Sprachent­wickelung wirkt.",
        "Und dabei bleibt immer das Bedeutsame, daß man wie auf ein Eurythmisches auf dieses hinzuweisen hat dadurch, daß man beim Toten entdeckt: Er zieht die Worte wieder auseinander, er zerlegt sie wieder in ihre Teile.",
        "Er hat mehr Empfindung, der Tote, für diese Teile der Worte, als für die ganzen Worte.",
        "Denken Sie sich konsequent die Sache durchentwickelt, so würden Sie die Worte überhaupt auseinanderkriegen in die Laute, und wenn Sie die Laute wiederum umsetzen, jetzt nicht in Luftbewegungen, sondern in Be­wegungen des ganzen Menschen, dann haben Sie die Eurythmie.",
        "Die Eurythmie ist daher etwas, was der Tote in der Tat sehr gut ver­stehen kann, wenn sie vollkommen betrieben wird.",
        "Und Sie sehen,"
      ],
      [
        "daß sich solche Dinge, wie auch die Eurythmie, nicht äußerlich be­urteilen lassen, sondern daß man ihre ganze Stellung im Gesamtge-füge der menschlichen Entwickelung nur einsehen kann, wenn man auch einzugehen vermag auf diese Gesamtentwickelung des Men­schen."
      ],
      [
        "Es ließe sich noch viel mehr sagen über das, was Eurythmie eigent­lich will, aber dazu wird sich später noch Gelegenheit bieten.",
        "Ich wollte damit zunächst einmal Sie auf ein wenn auch schattenhaftes Gebiet hinweisen, wo noch in den älteren Zeiten irn lebendigen Wir­ken der Menschen selber ein Hereinspielen des Idealen in das Reale war."
      ],
      [
        "Ich sagte heute im Eingange: In der heutigen Weltanschauung finden wir nicht mehr die Möglichkeit, eine Brücke zu bauen zwischen dem Ideellen, Idealen, Moralischen, und zwischen dem, was in der Natur lebt.",
        "Es fehit die Brücke."
      ],
      [
        "Das ist auch dem heutigen Entwickelungs-zyklus des Menschen ganz natürlich, daß diese Brücke fehlt.",
        "Das Ideelle schafft nicht mehr.",
        "Ich wollte Ihnen im menschlichen Gebiet selbst ein Beispiel zeigen, wenn auch, wie gesagt, ein schattenhaftes, wo in dem Menschen selbst noch ein Ideelles schafft."
      ],
      [
        "Denn in dem Zusam­mensetzen solcher Worte, da wirkte nicht Verabredung der Menschen oder die Überlegung einer einzelnen menschlichen Individualität oder Persönlichkeit, sondern da wirkte Vernunft, ohne daß der Mensch so richtig dabei war.",
        "Heute wollen die Menschen ja bei allem dabei sein, was sie machen: Nun, wenn so etwas Schönes, Großes, Bedeutsames gemacht werden sollte wie das hier - da sollten Sie sehen, was mit der heutigen Weisheit der Menschen herauskäme, wenn heute Sprache gebildet werden sollte!"
      ],
      [
        "Aber gerade in den Zeiten, in denen der Mensch noch nicht so bei sich war, sind diese großartigen, weisen, be­deutsamen Dinge in der Menschheit geschehen, und sie sind so ge­schehen, daß in diesem Geschehen noch ein nahes Zusammensein von Ideellem und von Realem ineinanderwirkte, nämlich ideellem, also vernünftigem Werden, und realem Bewegen der Luft durch die menschlichen Atmungsorgane.",
        "Heute können wir nicht zwischen der moralischen Idee und meinetwillen der elektrischen Kraft eine Brücke bauen; aber hier ist eine Brücke gebaut zwischen etwas Geschehendem und etwas Vernünftigem."
      ],
      [
        "Das führt uns natürlich nicht dazu - ich"
      ],
      [
        "werde das morgen weiter ausführen -, dieselbe Brücke zu bauen; sie muß heute in ganz anderer Weise gebaut werden.",
        "Aber Sie können daraus sehen, daß die Menschheit zu dem heutigen Zustande vorge­schritten ist von einem andern Zustande: von einem Drinnenstehen in einem lebendigen Weben, das nahe war dem, was in einer gewissen Weise umgekehrt Post mortem, also nach dem Tode der Menschen sich vollzieht.",
        "Der Mensch muß heute nach dem Tode, um sein Fort­kommen zu finden zwischen dem Tode und einer neuen Geburt, das wieder auseinandernehmen, was durch Kräfte - wir werden morgen noch dayon sprechen - so zusammengefügt worden ist, daß man die­ses Zusammenfügen noch deutlich sehen kann, wenn man in die älteren Stufen des Sprachbildens zurückgeht."
      ],
      [
        "Das sind wichtige Dinge, Dinge, die man wirklich ins Auge fassen muß, wenn man den Blick darauf wendet: Wie soll sich - wir haben ja darüber oft gesprochen, daß dies von uns ins Auge gefaßt werden muß - in das ganze Gefüge des gegenwärtigen Geisteslebens hinein­stellen dasjenige, was auf dem Boden der Geisteswissenschaft ge­funden werden kann? - Und wenn man immer wieder spricht von der Wichtigkeit dieses Hineinstellens der Geisteswissenschaft in die ganze Entwickelung, so muß man schon auch auf diesem Gebiete konkret denken.",
        "In diesen Vorträgen möchte ich jetzt einiges beitragen zu diesem konkreten Denken."
      ],
      [
        "Wenn es einmal sein könnte, daß Geistes­wissenschaft getragen würde von einer gewissen Bewegung in der Gegenwart, von einer Menschenbewegung, dann würde auf allen Gebieten diese Geisteswissenschaft befruchtend wirken können.",
        "Aber es müßte natürlich vor allen Dingen der Wille vorhanden sein, auf solche Subtilitäten auch einzugehen, wie sie hier oftmals betont wer­den."
      ],
      [
        "Denn auf diese Subtilitäten, die sich immer beziehen auf das Ver­hältnis unserer Geisteswissenschaft zur gegenwärtigen Geisteskultur, müssen wir das begründen, was wir nennen können unser eigenes Uns­Hineinstellen in die Geistesbewegung der Gegenwart mit der Geistes­wissenschaft.",
        "Es ist wirklich so, daß die traurigen, katastrophalen Ereignisse der Gegenwart den Menschen aufmerksam machen soll­ten, daß alte Weltanschauungen Bankrott gemacht haben."
      ],
      [
        "An der Geisteswissenschaft allein nicht, aber an ihrer Beziehung zu diesen"
      ],
      [
        "alten Weltanschauungen könnte man sehen, was zu geschehen hat, damit wir aus dem Bankrott der gegenwärtigen Zeit hinauskommen."
      ],
      [
        "Dazu wäre freilich notwendig, daß man endlich einginge auf die Intentionen, welche ich ja oftmals gerade als diejenigen der geistes-wissenschaftlichen Bewegung ausgesprochen habe.",
        "Es wäre wirklich notwendig, einzusehen, welches die Gründe sind, warum zum Bei­spiel auf der einen Seite es innerhalb gewisser Kreise so fruchtbar ge­worden ist, hier am Bau zu wirken, und warum andere Bestrebungen der Anthroposophischen Gesellschaft gewissermaßen ebenso un­fruchtbar geblieben sind; warum, wenn man absieht von dem, was sie wirklich geleistet hat, nämlich daß sie den Dornacher Bau in die Welt setzt, die Gesellschaft doch vielfach versagt."
      ],
      [
        "Ein solches Leisten auf der einen Seite bedingt immer, wenn es nicht oftmals das Gegen­teil wachrufen soll, daß manches andere geschieht.",
        "Es wäre notwendig, daß auch auf andern Gebieten die Anthroposophische Gesellschaft nicht versagte, wie sie vollständig versagt hat in den Jahren, in denen sie besteht."
      ],
      [
        "Dieses Versagen, das brauchte man nicht immer wieder und wiederum zu betonen, wenn viel stärker die Meinung verbreitet wäre, daß man nachdenken muß, warum die Anthroposophische Gesellschaft in bezug auf so vieles andere versagt.",
        "Wenn man gründ­licher nachdenken würde, so würde man erkennen, worauf es zum Beispiel beruht, daß draußen in der Welt immer wieder und wiederum die Meinung sich verbreitet, ich führte die Anthroposophische Ge­sellschaft nur so am Gängelbande und gäbe alles an; während es kaum eine Gesellschaft in der Welt gibt, wo weniger dasjenige geschieht, was ein sogenannter Führer will, als in der Anthroposophischen Ge­sellschaft!"
      ],
      [
        "Es geschieht ja in der Regel das Gegenteil von dem, was ich eigentlich beabsichtige.",
        "Also, nicht wahr, gerade an der Anthro­posophischen Gesellschaft kann es sich zeigen, wie im Praktischen eine Wirklichkeit weit ab ist auch von ihren sogenannten Idealen."
      ],
      [
        "Aber man muß dann auch den Willen haben, sich auf den Boden der Wirklichkeit zu stellen.",
        "In einer Gesellschaft gibt es selbstverständ­lich Persönliches; aber man muß dieses Persöniiche auch als Per­sönliches auffassen."
      ],
      [
        "Wenn irgendwo in einem Zweige sich die Leute streiten aus rein persönlichen Gründen, so soll man da nicht aus"
      ],
      [
        "Weiß Schwarz machen, oder aus Schwarz Weiß machen, sondern man soll ruhig zugestehen: Wir haben persönliche Gründe, wir mögen den und den nicht aus persönlichen Gründen. - Dann ist man bei der Wahrheit; man braucht ja nicht die Wirklichkeit in Ideale zu ver­kehren.",
        "So wäre es notwendig, daß, während auf der einen Seite mein Bestreben dahin geht, alles Geisteswissenschaftliche aus dem Sek­tiererischen herauszuheben, alles Sektiererische abzustreifen, die An­throposophische Gesellschaft immer mehr und mehr in das Sek­tiererische hineinplumpst und eine gewisse Liebe gerade für das Sektiererische hat.",
        "Wenn irgendwo das Bestreben besteht, aus dem Sektiererischen herauszukommen, so haßt man gerade hier dieses Herauskommenwollen aus dem Sektiererischen."
      ],
      [
        "Ich möchte natürlich nicht irgend jemanden tadeln, möchte auch nicht undankbar sein gegen die schönen Bestrebungen, die da und dort überall sind, ich erkenne alles voll an, aber es ist notwendig, daß man über manche Dinge ein wenig nachdenkt, sonst werden sich im­mer wieder und wiederum die Dinge finden, von denen mir auch in diesen Tagen wiederum erzähit worden ist.",
        "Nicht wahr, es ist auch da das Persönliche mit der Sache schon innig verquickt."
      ],
      [
        "Wenn jetzt in einem Lande wiederum irgendein Unheil auftaucht, so ist wiederum die Konstitution gerade der Anthroposophischen Gesellschaft so, daß, ich möchte sagen, die Gesellschaft die Sensation hat, sich wie­derum ein bißchen zu zanken, und aus diesem ganzen Zank kommt ja das heraus, daß ich selbst persönlich in der wüstesten Weise beschimpft werde.",
        "Ja, wenn sich das immer wieder und wieder wiederholt, so kommen wir nicht weiter."
      ],
      [
        "Wenn ich immer in der wüstesten Weise beschimpft werde, weil die andern zanken und ich ausgespielt werde, wenn es immer wiederum darauf hinauskommt, daß ich ausgespielt werde, so kann ich natürlich nicht mehr die anthroposophische Be­wegung in der Welt halten.",
        "Es wäre möglich, in positiver Weise bloß zu wirken, wenn man sich mehr auf das Positive verlegen wollte, das ich ja genügend immer wieder andeute."
      ],
      [
        "Es wäre möglich, solche Dinge hintanzuhalten, die zumeist auf furchtbar inferioren Dingen beruhen.",
        "Aber man hat in vielen Kreisen viel mehr Lust, zu zanken, viel mehr Lust, namentlich auch zum Dogmenstreit, aus dem sich"
      ],
      [
        "dann oftmals persönliche Zänkereien herausentwickeln.",
        "Und dann wird es so, daß das Schimpfen sich gewöhnlich auf mich ablenkt - was mich ja persönlich höchst kühl läßt, aber die Bewegung kann nicht weiterbestehen, wenn es so weitergehen soll."
      ],
      [
        "Es ist nicht so, daß ich in diesem Fall tadie, was die Freunde in einem solchen Falle getan haben, aber ich mache darauf aufmerksam, daß sie etwas anderes nicht getan haben, was mir nicht zukommt, gerade in plumper Weise anzudeuten, wodurch aber in viel sicherer Weise verhindert würde dasjenige, was fortwährend geschieht, als auf die Weise, wie es fort­während versucht wird.",
        "Heute steht es schon so, daß man sagen kann: Wir haben Zyklen nur abgegeben an Mitglieder der Gesellschaft, und ich weiß, wie ich selber oftmals sonderbar von dem oder jenem aus der Gesellschaft angesprochen werde, wenn ich viel liberaler bin, als fernerstehende Mitglieder oftmals in der Abgabe von Zyklen sein wollen."
      ],
      [
        "Ja, schlimmer hätte es dem, was durch die Zyklen in die Welt gesetzt worden ist, durch Außenstehende niemals ergehen können, als es durch Mitglieder der Anthroposophischen Gesellschaft ge­schehen ist!",
        "Das muß man auch in Betracht ziehen."
      ],
      [
        "Wir sind heute schon durchaus so weit, daß die Zyklen in einer Weise mißbraucht werden durch Mitglieder, durch abgefallene Mitglieder der Anthro­posophischen Gesellschaft, daß es eigentlich sehr bald nahe daran sein kann, daß man sagt: Wir machen gar keine Grenze mehr, wir ver­kaufen die Zyklen an jeden, der sie haben will. - Es kann nicht viel schlechter werden."
      ],
      [
        "Ich sage nicht, daß es morgen schon geschehen soll, aber ich deute nur an, daß die Gesellschaft so gar nicht als Gesellschaft wirkt - immer außer dem Bau und außer einzelnen Kreisen -, daß sie gar nicht eigent­lich das macht, was sonst eine Gesellschaft macht.",
        "Damit ist die Ge­sellschaft gar keine Hilfe; sie ist gar nicht dasjenige, was eine Bewe­gung ergeben würde."
      ],
      [
        "Hier ist es so klar, daß ich niemanden persönlich meinen kann, daß ich ganz unbefangen dieses hier besprechen kann, aus dem einfachen Grunde, weil hier ja gerade die Stätte ist, wo eben fruchtbar aus der Gesellschaft heraus geschafft wird, nämlich am Bau.",
        "Der ist schon eine wirkliche Sache, die aus der Gesellschaft heraus entstanden ist."
      ],
      [
        "Und würden andere Dinge, die viel billiger sein könnten als der Bau, aus einem solchen Gesellschaftsgeiste heraus arbeiten, wie die Arbei­ter an unserem Bau, dann würde aus der Anthroposophischen Ge­sellschaft ungeheuer Segensreiches ersprießen können.",
        "Aber man muß dann das Weiße weiß und das Schwarze schwarz nennen.",
        "Man muß wirklich auch sagen, da wo persönliche Dinge vorliegen: das sind persönliche Dinge - und sie nicht in einen hohen Idealismus heraufschrauben; sonst wird man eben nachdenken müssen, was an die Stelle der Anthroposophischen Gesellschaft gesetzt werden muß.",
        "Eine Gesellschaft würde dann ja nicht an die Stelle gesetzt werden können, denn es würde ja wiederum dieselbe Misere sein!",
        "Nicht wahr, es kann nicht die Gesellschaft bloß ein Mittel sein, daß man sich herumbalgen sollte mit allen möglichen inferioren Persönlichkeiten.",
        "Aber sie ist ein Mittel geworden, das einen zwingt, immer wieder Rücksicht zu nehmen auf alles mögliche inferiore Zeug."
      ],
      [
        "Nun, ich will Sie heute nicht länger langweilen mit der Sache, son­dern ich wollte sie nur, nachdem die Zeit abgelaufen war, noch an­fügen.",
        "Ich habe den Vortrag vorher zu Ende geführt; solche Sachen sage ich nur, wenn die Vortragszeit abgelaufen ist, hinterher als An­satz."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "ACHTER VORTRAG Dornach, 1. September 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Ich werde die Betrachtungen, die wir jetzt hier pflegen, so anlegen müssen, daß ich heute die gestern gemachten Auseinandersetzungen erweiternd vorbringe, um dann morgen zu einem gewissen vorläufigen kleinen Abschluß zu kommen. Daher wird das Heutige mehr eine Episode zu bedeuten haben.",
      "Man hat in der Gegenwart ja sehr, sehr viel Veraniassung, auch aus den Zeitereignissen heraus, über dies oder jenes nachzudenken, wenn man nicht die Absicht hat, die wichtigsten Impulse unserer Zeit zu verschlafen. Besonders auffällig in der Gegenwart und, ich möchte sagen, Fragen herausfordernd ist ja die Erscheinung, die Ihnen doch wohl hinlänglich bekannt ist, daß im weitesten Sinne in dieser Gegen­wart die ungeheuerste Unwahrhaftigkeit Platz gegriffen hat, daß ge­rade da, wo Umfassendes heute spielt, Unwahrhaftigkeit vorhanden ist. Solche Dinge, wie das Auftreten von so wirksamer, so einschnei­dender Unwahrhaftigkeit veraniaßt dann auch, über allerlei damit Zusammenhängendes geisteswissenschaftlich nachzuforschen. Und da, kann man sagen, tritt einem oftmals ganz besonders die Tatsache entgegen, die ich auch hier schon öfter berührt habe, daß das, was zumeist als Geschichte der Menschheit mitgeteilt wird, eine Art Fable convenue ist. Dabei handelt es sich nicht so sehr darum, daß Tat­sachen, die mitgeteilt werden, etwa nicht bis zu einem gewissen Grade für richtig zu halten wären; aber andere Tatsachen - Sie erinnern sich, ich habe letzthin hier auseinandergesetzt, wie tiefstgehende Ein-flüsse eines Menschen aus der römischen Geschichte einfach gestrichen worden sind , sie werden einfach getilgt. Ungeheures an Tatsachen hat ja die Kirche aus der Geschichte ausgetilgt, weil der Kirche daran gelegen war, daß gewisse Tatsachen nicht zur Kenntnis der Menschen kommen.",
      "Nun haben wir gestern wiederum von einem Gesichtspunkte aus über die Zeit gesprochen, welche die griechisch4ateinische Kultur-periode einleitete, über den wichtigen Zeitabschnitt im 8. vorchrist­lichen",
      "Jahrhundert. Es ist ja eine Zeit, aus der heraus nicht mehr viel die historischen Überlieferungen sprechen. Die historischen Über­lieferungen werden da schon sehr, sehr unsicher, aber es glänzt aus dem Beginne dieser Zeitepoche heraus eine Persönlichkeit, die sehr, sehr vielen Leuten Betrachtungen der verschiedensten Art abge­rungen hat. Es glänzt da aus der Entstehungszeit, also nach dem 8. vor­christlichen Jahrhunderte, der Name des Pythagoras heraus, der Name auch der Pythagoräischen Schule. Und ich habe ja gestern darauf hin­gewiesen, was aus den Überbleibseln der alten ägyptischen Mysterien­wahrheiten Pythagoras hat empfangen können, welcher Art diese Dinge waren, die Pythagoras hat empfangen können.",
      "Nun ist es nicht nur interessant, das zu betrachten, was Pythagoras und seine Schüler gesagt und getan haben, was ja sehr einschneidend war, denn sie haben nicht nur eine Lehrtätigkeit entwickelt, sondern eine weitgehende politische Tätigkeit. Was Pythagoras und seine Schüler getan haben, ist interessant, aber außerdem ist es bedeutsam, die Welt zu betrachten, die gewissermaßen dieses pythagoräische Treiben umgibt, die Welt, aus der dann auch das spätere Griechentum herausgewachsen ist, das ja schon einen gewissen Einfluß aufgenom­men hat auch desjenigen, was man, von besonderem Glänze erhellt, bei Pythagoras findet.",
      "Wenn man im 7., 6., 5. Jahrhundert vor unserer Zeitrechnung das Leben nimmt, aus dem dann das spätere griechisch-lateinische herausgewachsen ist, wenn man dieses Leben nimmt auf der griechischen Halbinsel und den angrenzenden Ländern und der italienischen Halbinsel, so fällt einem dann, wenn man die Dinge nicht der geschichtlichen Fable convenue nach betrachtet, sondern wenn man sie betrachtet im Lichte der Wahrheit - dazu muß immer die geisteswissenschaftliche Forschung dann ihre Beiträge geben -, be­sonders auf, daß eine Eigenschaft der Menschheit über dieses Leben sehr verbreitet war.",
      "Es wurde nämlich kaum zu irgendeiner Zeit so viel gelogen als zu dieser Zeit über die Mittelmeerländer hin. Das Lügen, das die Unwahrheitsagen den andern Menschen, das war eine ganz auffällige charakteristische Erscheinung alles desjenigen Lebens, aus dem dann das spätere Griechentum und Römertum hervorge­wachsen ist.",
      "Man muß sich in solchen Dingen keinen Täuschungen hingeben. Alles dasjenige, was man als die gewaltige Schönheit, als die bewun­derungswürdige Summe von Phantasieschöpfungen Griechenlands, was man als die großartigste Summe von Abstraktionen, die es je in der Welt gegeben hat, im Römertum sich entwickeln sieht, das alles wächst heraus, so wie die Pflanzenwelt aus dem Dünger herauswächst, aus einem Boden, der über die Mittelmeerländer ausgedehnt ist, aus einem Boden, den Menschen bewohnen, die ganz erfüllt sind von der Sucht, von der Leidenschaft des Lügens. Das ist etwas, was von der Geschichte weniger betont wird, was aber verstanden werden muß , wenn man richtig hineinsehen will in die untergehende dritte nach-atlantische Kulturzeit. Wir haben es ja, indem wir von den früheren Jahrhunderten und Jahrtausenden zum 8. vorchristlichen Jahrhundert heraufkommen, mit dem untergehenden dritten nachatlantischen Kul­turzeitraum zu tun. Und die Menschen, die damals die Kulturträger waren des dritten nachatlantischen Kulturzeitraumes, des untergehen­den dritten nachatlantischen Kulturzeitraumes, die waren im wesent­lichen große Lügner. Das ist gleichzeitig diejenige Epoche, in welcher sich ganz besonders entwickelt jene Fähigkeit, von der ich Ihnen gestern gesprochen habe und die so außerordentlich interessant ist:",
      "jene Fähigkeit, aus dem Kosmischen der Vernunft heraus die Sprache zu bilden. Und es war das größte Talent eben dazumal vorhanden -neben solchen Dingen, wie ich sie gestern auseinandergesetzt habe -in der großen Sucht, zu lügen.",
      "Man darf sich in diesen Dingen ebensowenig einer Täuschung hin-geben, wenn man die Wirklichkeit betrachten will, wie man sich einer Täuschung darüber hingeben darf, daß das Veilchen, das im Frühling blüht, wiederum vergeht und die Kräfte des Vergänglichen, während es schön und herrlich blüht, schon in sich trägt. Da hat man bei dem Veilchen gewissermaßen nacheinander Entstehungskräfte und Zer­störungskräfte. Im Menschenleben, namentlich im großen Mensch­heitsieben, hat man das sehr, sehr häufig auch zeitlich nebeneinander , und man begreift nicht die Wirklichkeit, wenn man nicht die Notwen­digkeit begreift, daß solche Dinge nebeneinander sich bilden: Evo­lution und Devolution, die Möglichkeit, aufbauend zu wirken, wie",
      "zum Beispiel eben in der Sprachbildung, und gleichzeitig jene ver­heerende Wirkung, welche auf das Geistesleben das Lügen ausübt.",
      "Das ist gewissermaßen die Kehrseite desjenigen, was ich Ihnen gestern auseinandergesetzt habe. Es gibt auch eine Lichtseite. Diese Lichtseite ist noch geisteswissenschaftlicherer Natur. Ich habe schon gestern darauf aufmerksam gemacht, daß es ja nicht möglich wäre, heute mit einer solchen Sicherheit über diese Dinge der Sprachbildung, die wir gestern besprochen haben, zu reden, wenn nicht das Leben des Menschen nach dem Tode einem den deutlichen Beweis davon geben würde, indem dasjenige, was hier im Leben zum Beispiel aus einzelnen Wortatomen oder Wortteilen zusammengesetzt wird an Worten, wiederum gelöst wird.",
      "Und dieses Lösen von Worten, dieses Zer­stäuben von Worten, das ist etwas, das im Leben der Toten eine be­deutsame Rolle spielt. Gewissermaßen lebt der Tote von diesem Zer­stäuben der Worte. Und der Tote hat das entschiedenste Gefühl, daß er in seinem Leben, also vor seinem Tode, von der geistigen Welt, in der er sich nach seinem Tode befindet, dadurch abgeschlossen war, daß er aus Lauten, aus Buchstaben zusammengesetzte Worte gebildet hat.",
      "Der Tote hat das Gefühl, daß die Sprache gewissermaßen ein Teppich ist, der sich im Leben vor die geistige Welt hingelegt hat. Und in dem Aufdröseln dieses Teppichs, in dem Auflösen der Worte hat er das Gefühl, daß er nun wiederum in die geistige Welt eintritt.",
      "Daher ist es eine der Eigenschaften des Toten, die Menschenworte, die der Betreffende kennengelernt hat innerhalb des Lebens zwischen Geburt und Tod, aufzulösen, zu zerpflücken, in ihre Bestandteile aufzu­lösen. Der Tote hat zum Beispiel ein ganz feierliches, großes Gefühl, wenn es ihm gelingt, ein gewisses Verständnis sich durch solche Auf­lösung zu erwerben.",
      "Ich habe Ihnen öfter davon gesprochen, daß der Moment des Todes ja in einer gewissen Beziehung etwas Schreck­haftes ist für das Leben hier im physischen Leibe. Die Menschen wenden ja auch gerne ihr Antlitz von dem Tode ab.",
      "Nach dem Tode ist der Anblick des Todes immer da - ich habe das öfters schon be­tont -, aber er bedeutet dann nichts Furchtbares; sondern indem der Mensch hinblickt auf seinen eigenen Tod von der andern Seite des Lebens aus, ist in diesem Anblick immer die Gewißheit",
      "vorhanden, daß er ein Ich ist und ein Ich bleibt. Das habe ich ja öfter betont.",
      "Aber nun handelt es sich für den Toten darum, dasjenige zu ver­stehen, was sich ihm im Anblick des Todes von der andern Seite des Lebens aus offenbart. Dieses versteht er dadurch immer besser und besser, daß er, je nachdem er diese oder jene Sprache gesprochen hat, diese oder jene Worte auflöst.",
      "Die alten Hebräer und mit einer ge­wissen Ähnlichkeit noch die Römer, haben ja ihren sogenannten ge­heiligten Namen, den unaussprechlichen Namen des Gottes, Jahve. Dieser unaussprechliche Name bestand ja für die Hebräer in einer gewissen Zusammenfügung der von uns als fünf Vokzle empfundenen Laute, die verbunden gedacht wurden während des physischen Le­bens.",
      "Noch in dem römischen Jovis, Jupiter, ist ja nur eine andere Form des Jahvenamens verdeckt enthalten; er ist im Grunde in bezug auf die fünf Vokale in einer gewissen Weise verbunden in dem Jovis In der Auflösung desjenigen, was hier verbunden war in diesem Gottesnamen, lebte der Tote, und indem er die Vokale, die zusammen­gesetzt waren im Leben, auflöste, enthüllte sich ihm auch zugleich der Sinn, könnte man sagen, des Todes. Die Enthüllung dieses Sinnes des Todes, die muß man nur versuchen, in der richtigen Weise wenig­stens zu ahnen.",
      "Man muß verstehen, daß sich dem Toten enthüllt dieser Sinn des Todes durch die Auflösung des heiligen Namens in seine Bestandteile, die dann verklingen und verklingend forttönen in der Welt. Die Auflösung dieses heiligen Namens ist verknüpft mit dem Verständnis der Vergeistigung des Todes.",
      "Es ist das ein Begriff, den man außerordentlich schwer schildern kann. Der Tod, von der andern Seite angesehen, kann Vergeistigung genannt werden. Indem der Tod von der andern Seite angeblickt wird, ist dieser Anblick ver­knüpft mit der Entstehung von Geistigem.",
      "Und in dem Zerpflücken des Wortes nach den Vokalen enthüllt sich das Geistige aus dem Zer­fall heraus, den der Tod bedeutet. Zerfall ist da zu gleicher Zeit Ge­burt des Geistigen, Entstehung des Geistigen.",
      "Während man den Zerfall in unsympathischer Weise als etwas Unschönes empfindet wie jede Zerstörung, enthüllt sich von der andern Seite gesehen diese Zerstörung als ein Aufleuchten des Geistigen, das dann verstanden",
      "wird in dem Verklingen. Es ist, als ob das heilige Wort weit hinaus­klänge, hinausstrahlte, und im Hinausstrahien sich eben in seine vo­kalischen Bestandteile auflöste, die dann hörbar sind wie aus der Peripherie der Welt herein, und dann hörbar machen den Sinn des Todes, den Geistsinn des Todes.",
      "Das schon wird Sie darauf lunleiten, daß es berechtigt ist, geradeso wie man von Gliedern der Menschennatur spricht hier im Leben, physischer Leib, Ätherleib, astralischer Leib und Ich, zu sprechen von den Gliedern der Menschennatur, die diese Menschennatur zwi­schen dem Tod und einer neuen Geburt hat. Denn indem ich Ihnen gewissermaßen die zentrale Erscheinung, die der Mensch fortwäh­rend zwischen dem Tod und einer neuen Geburt hat, diese Enthüllung des geistigen Sinnes des Todes selbst, hingestellt habe, muß die Frage entstehen: Wie sieht denn eigentlich diese Welt aus, die da nach dem Tod für die Menschen sich enthüllen soll? - Das kann man aber nicht anders fassen, als indem man die Natur und Wesenheit des Menschen selbst etwas kennenlernt.",
      "Nun wollen wir heute zunächst einmal versuchen, den Toten eben­so zu beschreiben, wie man sonst den Lebenden beschreibt. Da kann man zunächst anfangen mit demjenigen Gliede des toten Menschen, welches noch viel Zusammenhang - nicht Verwandtschaft, aber Zu­sammenhang - hat mit dem, was der Mensch hier durchiebt zwischen der Geburt und dem Tode. Da hat man es also dann mit dem ersten Gliede der Menschennatur zu tun, das man auch das Ich nennen kann, wie man gewissermaßen für hier das zunächst höchste Glied der Menschennatur zwischen Geburt und Tod nennt. Wir sehen jetzt da­von ab, daß es zunächst, unmittelbar nach dem Tode, noch die Hülle des Ätherleibes hat, der dann abgelöst wird, und noch die Hülle des Astralleibes hat, die auch im Laufe der Zeit abgelöst wird; das sind Bestandteile, die gewissermaßen nicht dazugehören. Wenn man von dem toten Menschen spricht, so ist als ureigenes Glied dieses toten Menschen doch zunächst nur anzuerkennen das Ich. Ich sagte, es ist ein Zusammenhang mit dem Ich des Erdeniebens, nicht aber eine eigentliche Verwandtschaft; denn in der Tat stellt sich dieses Ich nach dem Tode in einer ganz andern Weise dar, als das Ich erlebt wird zwischen",
      "der Geburt und dem Tode. Zwischen der Geburt und dem Tode ist das Ich gewissermaßen etwas Flüssiges, etwas, was in sich die Kraft fühlt, jeden Tag anders zu werden. Denken Sie nur, wie schrecklich es im leiblichen Leben zwischen Geburt und Tod wäre, wenn Sie nicht imstande wären, den Gedanken zu fassen: Ich habe gestern irgend etwas Schlimmes getan, aber ich kann das wiederum ausbes­sern, ich kann dafür etwas Gutes tun. - Oder wenn Sie, noch jünger, sagen müßten: Ich habe wenig gelernt, aber ich kann nichts dazu­lernen. - Jn keinem Momente des Lebens zwischen der Geburt und dem Tode ist das Ich etwas so Festes, daß es nicht gewissermaßen durch seine eigene Willenskraft von innen heraus geändert werden könnte.",
      "Dasjenige, was Sie erleben als Ich nach dem Tode, das ist etwas Festgewordenes, das hat gewisse Eigenschaften angenommen, die nun nicht unmittelbar geändert werden können; das bleibt so, wie es ist. Die Umwandlung des im Leben zwischen Geburt und Tod fort-dauernd flüssigen Ich in ein festes Gebilde, in dem nichts sich ändern kann, das so bleibt, wie es sich im Leben geformt hat, das ist das Wesentliche, das festgehalten werden muß zum Verständnis dieses Ich nach dem Tode.",
      "Von einer Entwickelung, von der wir ja sprechen müssen für das Ich zwischen Geburt und Tod, kann nach dem Tode nicht die Rede sein. Nach dem Tode ist das Ich gewissermaßen ein festes Geistgebilde, das herausentspringt aus dem Anblick des Todes selber, und es kann nichts an diesem Ich geändert werden.",
      "Man könnte sagen, wenn man diese Sache mehr oder weniger banal aussprechen wollte: Der Mensch ist verurteilt, nach dem Tode alle Einzelheiten seines Lebens wie etwas Festes anzusehen. Wie Sie, wenn Sie über einen Acker hinsehen, die nahen Pflanzungen und die fernen Pflan­zungen nebeneinander sehen, und wie Sie dadrinnen nichts Flüssiges, sondern ein festes, ausgedehntes, zunächst bleibendes Gebilde sehen, so übersehen Sie die ganze Strecke Ihres Lebenslaufes, aber so, daß nicht immer, wie es im Leben des physischen Leibes ist, das Vordere durch das Hintere ausgelöscht wird, sondern Sie übersehen es als ein bleibendes konkretes Feld, in dem Sie durch den bloßen Anblick zu-nächst nichts ändern können.",
      "Es wäre auch schlimm für den Toten, wenn das nicht so wäre; denn sein Blick, der Blick des Toten ist eigentlich",
      "zunächst hauptsächlich in Anspruch genommen von diesem Ich. Er ist wie hineingebannt in dieses Ich. Und würde dieses Ich ver­schwinden, so würde es für den Toten ebenso sein, als wenn für den Lebenden die umliegende Welt der Sinne verschwinden würde. Der einzelne Mensch in seinem Ich ist tatsächlich für sich selbst, wenn ich mich so ausdrücken darf, so wichtig - damit sprechen wir aber eine bedeutsame Wahrheit aus - wie die ganze Sinnenwelt, die wir als Menschen gemeinsam haben, für den Menschen hier im physischen Leben ist. Ein ungeheurer Abgrund täte sich auf, der Abgrund des Nichts geradezu, wenn wir nach dem Tode nicht imstande wären, das erstarrte Ich, das aus dem flüssigen Zustande erstarrte Ich im An­blick zu haben.",
      "Als zweites haben wir eine Art von Geistwesen, das wir in Analogie mit dem, was wir schon kennen, auch Geistselbst nennen können. Als zweites Glied also der menschlichen Wesenheit nach dem Tode haben wir eine Art Geistwesenheit. Diese Geistwesenheit wird dem Men­schen hauptsächlich so bewußt, daß ihm dieses Bewußtsein des Geist-selbst wie von innen aufgeht. Während das Ich eine Art äußeren An­blick darbietet, geht das Bewußtsein dieses Geistselbst von innen heraus auf. Und in demselben Maße, in dem man fühlt: Dieses Geist-selbst belebt sich -, in demselben Maße treten herauf aus dem Be­wußtsein, so daß man weiß, sie sind da, die Wesenheiten der höheren Hierarchien. Ich nenne dieses also: «das Geistselbst» - ich muß es ge­nau so definieren, wie ich es jetzt auf die Tafel schreibe, sonst würde ich Ihnen etwas Ungenaues schreiben - «gerichtet durch die Hierar­chien auf das Ich».",
      "Das, was ich jetzt geschrieben habe, gibt ungefähr den Tatbestand ganz richtig. Sie haben das Gefühl: Da ist ein Wesen aus der Hierar­chie der Angeloi, aus der Hierarchie der Exusiai, das richtet jetzt den Blick auf Ihr Ich. Indem Sie Ihren Blick auf das Ich richten, das eine Mal durch irgendein Wesen einer Hierarchie, das andere Mal dadurch, daß Sie wissen, jetzt ist Ihr Blick auf das Ich durch ein Wesen der andern Hierarchie gerichtet, lernen Sie diese Hierarchie innerhalb des Wirkens Ihres Geistselbst kennen. Also in Ihrer eigenen Betätigung lernen Sie die Hierarchien kennen. Sie fangen an, durch Ihr Geistselbst",
      "sich in Gesellschaft der Hierarchien zu befinden. Und während Sie, bevor dieses Geistselbst aufleuchtet, noch das Gefühl haben, nur Sie selbst beschäftigen sich damit, den Blick hinzurichten auf das eigene Ich, bekommen Sie immer deutlicher das Gefühl, daß sich immer mehr und mehr Wesenheiten der höheren Hierarchien um Sie kümmern und sich hineinmischen in Ihr Schauen, Ihre Blicke lenken. Sie fühlen sich, indem Sie Ihre höhere Sinnestätigkeit entwickeln , durch das Geistselbst immer mehr und mehr so, daß in dieser Sinnes-tätigkeit mittätig sind die Wesen der höheren Hierarchien. Was un­erträglich wäre für den Menschen der Sinneswelt hier, das wird ge­radezu das Lebenselement für den Menschen im Zustande nach dem Tode.",
      "Denken Sie sich einmal, Sie stünden hier am Fenster und schauten hinaus und sollten die Umgebung betrachten. Einer von Ihnen stellte sich dahin und wollte die Umgebung betrachten, und der erste, der hier sitzt, geht hin, dreht Ihnen den Kopf nach der einen Seite, damit Sie irgend etwas betrachten nach jener Richtung; ein zweiter geht hin, dreht Ihnen den Kopf ein bißchen hinauf, damit Sie etwas anderes betrachten; ein dritter wiederum ein bißchen herum, damit Sie wieder etwas anderes betrachten, und so würde die ganze Gesellschaft, die hier sitzt, von hinten Ihnen sich nähern, und Sie würden nur dadurch den Aspekt Ihrer Umgebung draußen haben, daß dasjenige, was hier herinnen sitzt, Ihnen den Kopf fortwährend darnach hinrichtet. Denken Sie das jetzt nicht von außen angesehen, sondern als inneres Erlebnis, als inneres Empfinden, dann haben Sie aber etwas, was recht analog ist diesem Erleben, das Sie als Ihr Geistselbst haben. Sie leben sich in das Lehen der höheren Hierarchien dadurch immer mehr hinein, daß diese höheren Hierarchien in Ihre Blickrichtung hineinkommen.",
      "In dem Auflösen der Worte, von dem wir schon gesprochen haben , wirken schon die Wesenheiten der höheren Hierarchien. Das ist eine Seite desjenigen, was da erlebt wird. Aber es ist ja die fortdauernde Bereicherung des Lebens, die dadurch entsteht, daß man nach und nach immer mehr und mehr mit den Hierarchien bekannt wird. Und in einer ganz ähnlichen Weise wird man bekannt mit den Wesenheiten ,",
      "mit denen man irgendwie karmisch vor dem Tode verbunden war. Und da fühlt man, daß man gewissermaßen geleitet und gelenkt wird. Das ist dasjenige, was gesagt werden kann über das zweite Glied der menschlichen Wesenheit in dem Leben zwischen dem Tod und einer neuen Geburt.",
      "Das dritte Glied ist etwas, was zunächst vielleicht auf das Ver­ständnis des Menschen etwas schocklerend wirken könnte. Man fühlt sich nach und nach, indem man sich in dieses Leben nach dem Tode hineinlebt, durchsetzt von einer gewissen Kraft, ich könnte vielleicht sagen, von einem Kräftezusammenhang. Indem man zuerst gefühlt hat, die Hierarchien kommen heran und leiten einen bei der übersinn­lichen Sinnestätigkeit - wenn ich den Ausdruck bilden darf -, fühlt man nach und nach: diese Hierarchien durchträufeln einen mit Kraft, geben einem Kraft. Man fühlt sich nach und nach erfüllt von dieser Kraft, welche die Hierarchien mit einfließen lassen, indem sie sich in einen hineinsetzen, indem sie ihr Wesen in einen hineinträufeln. Diese Kraft fühlt man allmählich. Man fühlt, daß man durch die Hierarchien nicht nur hingelenkt wird auf das oder jenes, sondern man fühlt, daß man durch diese Tätigkeit der Hierarchien, die zunächst auftritt wie eine das Schauen vermittelnde Tätigkeit, selbst innerlich krafterfülit wird. Man fühlt die Kräfte des Kosmos, wirklich des Kosmos in sich einströmen wie belebende Säfte. Aber nun, was das Schockierende ist, das ist, daß die Kräfte, die man jetzt in sich einströmen fühlt, von einer ganz eigentümlichen Art sind. Es sind Kräfte, welche zunächst durchaus nicht fördernd, sondern auflösend, vernichtend sind für das, was man hier in der physischen Welt Leben nennt. Man fühlt sich nach und nach erfüllt von kosmischer, todbringender Weltenkraft.",
      "Es ist wichtig, solche merkwürdigen Vorstellungen in sich aufzu­nehmen, weil nur dadurch die geistige Welt wirklich begriffen werden kann. Denken Sie sich einmal eben in Ihrer geistig-seelischen Wesen­heit nach und nach erfüllt von Kräften, von denen Sie das Bewußt­sein erhalten, indem Sie sie in sich erleben: Durch diese Kräfte wird alles dasjenige, was hier auf der Erde lebt, wenn Sie es berühren wür­den, getötet. - Also Sie kleiden sich drittens in das, was ich, in Analogie mit etwas, was wir schon kennen, nennen kann den Lebensgeist.",
      "Sie kleiden sich in etwas , was man Lebensgeist nennen kann, was aber seine hauptsächlichsten Eigenschaften dadurch hat, daß es er-tötend ist für dasjenige, was man sonst die Kraft des Lebensleibes nennen kann. Und Sie bekommen ein drittes Glied Ihrer Wesenheit, durch das Sie in der Lage sind, jeden Ätherleib, der Ihnen in die Quere kommt, zu töten.",
      "Alles, was Sie berühren durch dieses Glied Ihrer Wesenheit, wird in dem Sinne tot, in dem man von dem Tode hier auf Erden spricht. Und indem Sie durch das, was Sie da an Kräf­ten bekommen, töten, wecken Sie aus dem Getöteten Geistiges auf, zunächst eigentlich Seelisches au£ Es ist dieses ein merkwürdiges Er­lebnis, das darin besteht, daß durch die Berührung von Lebendigem das Lebendige getötet wird, aber aus dieser Tötung Seelisches ent­springt, Seelisches erlöst wird.",
      "Es ist ein Töten, aber es ist zu gleicher Zeit eine Erlösung des Seelischen aus den Banden des Lebens. So daß man sagen kann: Der Lebensgeist tötet irdisch Lebendiges, in ihm Seelisches auslösend. Und man kommt zu dieser merkwürdigen Er­fahrung dadurch, daß in dem Leben, in dem Lebendigen gewisser­maßen Seelisches verzaubert ist, und daß durch diesen Vorgang, der da nach dem Tode geübt wird, das verzauberte Seelische aus dem Lebendigen herauserlöst wird.",
      "Man könnte geneigt sein, in der Tötung, in der ja im wesentlichen die Kraft wirkt, von der wir hier reden, etwas Furchtbares, Unsympathisches zu sehen. Für das Leben nach dem Tode ist das nicht der Fall, weil in dem Töten, in der töten­den Kraft das fortwährende Aufleuchten des Seelischen liegt, weil da­durch das fortwährende Entstehen des Seelischen entzündet wird.",
      "Aber dieses Bewußtsein muß der Tote haben: nicht nur, daß er immer hinsieht auf den Tod, den er selbst durchgemacht hat, sondern er muß auch bewußt sein dessen, daß dasjenige, was das Wesen seines Todes ist, sich gewissermaßen auf dem Untergrunde alles desjenigen aus­hreitet, was er nun in der geistigen Welt erlebt. Es ist, wie wenn man in der geistigen Welt nunmehr so lebte, daß man sagen kann: Hier in dieser geistigen Welt entstehen fortwährend geistige Gebilde, zu­nächst eigentlich seelische Gebilde; Seelisches leuchtet auf in der ver-schiedensten Weise.",
      "Aber wenn man nachfragen würde, was der Boden ist, aus dem all dieses Seelische heraussprießt, so ist es diese",
      "Tötekraft, die wir soeben besprochen haben. Eine solche, das ge­wöhnliche hier auf der Erde befindliche Leben zerstörende Kraft ist also unser wesentliches Seelisches, das wir uns aneignen müssen zwi­schen dem Tod und einer neuen Geburt, wie wir uns hier im Leben aneignen müssen unseren fleischlichen Leib.",
      "Als viertes Glied kann ich, wiederum in Analogie mit dem, was wir schon kennen, sagen: der Geistesmensch. Dieser Geistesmensch, der wird als etwas, was man in der Zeit zwischen dem Tod und einer neuen Geburt zu sich zu rechnen geneigt ist, dadurch empfunden, daß nun wiederum mit den Kräften, die schon eingeträufelt werden durch die Hierarchien, wie ich geschildert habe, einem jetzt die Möglichkeit ein­geträufelt wird, nicht nur Leben - was man hier auf Erden Leben nennt - zu töten, zu zerstören, aufzulösen, sondern Formen zu ver­nichten beziehungsweise auch in andere zu verwandeln. Also: Erstens das Ich; zweitens das Geistselbst, gerichtet durch die Hierarchien auf das Ich; drittens der Lebensgeist tötet irdisch Lebendiges, in ihm Seelisches auslösend; viertens der Geistesmensch.",
      "Es wird natürlich immer schwieriger, diese Dinge zu schildern. Aber im wesentlichen ist die Kraft dieses Geistesmenschen, wie man sie hat zwischen dem Tod und einer neuen Geburt, darin bestehend, daß man die entgegengesetzte Tätigkeit - wenn ich mich so aus­drücken darf - von alldem verrichtet, was man nennen könnte: Er­zeugung von Formen im weitesten Sinne. Hier - wenn ich mich bei einem speziellen Beispiele beruhigen will - zeichnet man Dreiecke, Vierecke und so weiter. Nach dem Tode, vermöge der Kräfte, die hier entwickelt werden, «entzeichnet» man, man löst alles Gezeichnete, die Formen au£ Aber das Eigentümliche ist, daß dies nicht bloß be­deutet, daß man etwas entzeichnet, sondern das ist zu gleicher Zeit eine kosmische Tätigkeit. Man ist jetzt selber in der kosmischen Tätig­keit drinnen, man ist verknüpft mit der kosmischen Tätigkeit. Denn dieses Entzeichnen, dieses Entformen, dieses Auflösen von Formen, das ist eine kosmische Tätigkeit, und der Mensch, indem er sich an­geeignet hat, nachdem er mit dem Lebensgeiste durchzogen war, diese Kraft der Entformung, ist mit ein Stück der kosmischen Welt ge­worden. Er wirkt im Kosmos drinnen.",
      "Es hat dasjenige, was hier auf der Erde Zerstörung, Untergang heißt, viel zu tun mit Entstehung, mit Bildung in den geistigen Welten. Und umgekehrt: Mit dem, was für uns Her wie Zerstörung, wie Untergang, wie Entformung, Entzeichnung aussieht, hat Ent­stehung in den andern, in den geistigen Welten viel zu tun. So daß, wenn ich von Entzeichnung, Eniformung spreche, ich nicht von Untergang in der geistigen Welt, sondern nur von Untergang in der seelischen Welt, dagegen von Auftauchen von geistig Neuem in der geistigen Welt spreche.",
      "Mit diesen Dingen hängen mancherlei Geheimnisse in der Welt zu­sammen. Sie nähern sich heute Unteritalien von Mittelitalien aus; Sie kommen, indem Sie sich Unteritalien nähern, in Gegenden, die arm sind, die gar nicht besonders fruchtbar sind, in denen wenig Natur-reichtum den Menschen zur Verfügung steht.",
      "Es sind dieselben Gegenden, in denen zur Zeit des aufgehenden vieflen nachatlanti­schen Zeitraumes Pythagoras gewirkt hat. Und Pythagoras' Wirksam­keit war damals inmitten fruchtbarster, reichster, üppigster Gegenden.",
      "So kurz die Zeit ist seit jener Epoche: indem man gerade auf diesen Fleck Erde hinweist, wo Phythagoras gewirkt hat, hat man die Um­wandlung von einer Fruchtbarkeit und Üppigkeit, die bis zu dem Grade der Sybaris ging, die Sybaris in Armut umgewandelt, sogar bis zur Entstehung bedenklicher Krankheitserscheinungen. An der Stelle von sprossendem, üppigem Leben, das in jenen Zeiten da war, in die nur noch wenig Historisches zurückgeht, entwickelt sich etwas, was imVer­gleich zu jenem üppigen, sprossenden Leben auch Naturarmut ist.",
      "Und es ist eigentlich im höchsten Grade interessant, solche Übergänge in der äußeren Welt zu sehen. In dieser äußeren Welt gliedern sich forwährend zusammen Entstehen, Vergehen. Die Menschen denken mit ihrer Geschichtsforschung nur nicht so weit, daß sie das fort­währende Entstehen und Vergehen miteinander richtig verknüpfen würden.",
      "Mitten in der strotzenden Üppigkeit, in der ganz großartig gelogen wurde, hat Pythagoras seine Tätigkeit entfaltet, und diese Tätigkeit setzte sich fort nach seinem Tode. Und dasjenige, was Py­Ihagoras und die Pythagoräerseelen nach dem Tode zu tun hatten, hängt vielfach mit dem zusammen , was sich äußerte in dem Untergang",
      "des blühenden, sprossenden Lebens, imrütten dessen Pythagoras war. Nicht ganz unbeteiligt an dem Zerstörungswerk - das für das Jenseits ein Entstehungswerk ist, -, das sich an der Stätte üppigen, sprossenden Lebens innerhalb der Natur aufrichtete in der nach­pythagoräischen Zeit, sind Pythagoras und die Seelen seiner Ar:ään­ger. Und man muß sich, wenn man die Gesamtwelt verstehen will, eben bekanntmachen damit, daß von den verschiedenen Aspekten aus hier zwischen Geburt und Tod und zwischen Tod und neuer Geburt die Dinge sich ganz anders ausnehmen. Derjenige, der Frevel be­gehen würde, wenn er hier üppiges, sprossendes Leben künstlich untergraben würde, der tut gewissermaßen nur etwas, was im Sinne der ewigen Notwendigkeit geschieht, wenn er sich in dem Leben zwischen Tod und neuer Geburt an einem solchen Werke beteiligt, das hier offenbar Untergang bedeutet.",
      "Mit dem dritten nachatlantischen Zeitraum sollte auch etwas un­tergehen, und das hinterließ seine Schatten. Viel sollte untergehen auf einem andern Gebiete, als das eben besprochene. Und mit diesem Untergehen der dritten nachatlantischen Epoche hängt es im wesent­lichen zusammen, daß damals so viel gelogen worden ist. Auf der Erde wurde gelogen, weil die Menschen, wie ich Ihnen gestern aus­geführt habe, noch mit den kosmischen Kräften in Verbindung stan­den; aber gerade die kosmischen Kräfte, die dazumal vor dem 8. vor-christlichen Jahrhundert in die Erdenentwickelung hereinspielten, waren vielfach lügnerische Kräfte. Dämonische Lügner waren tätig in der Sphäre, in die der Mensch seine Seele hineiniebte, indem er die Worte so entwickelte, wie ich gestern auseinandergesetzt habe. Er mußte gleichsam seinen Seelenkopf hineinstecken in eine Sphäre, in der er das tun konnte: die Sphäre der kosmischen Vernunft. Indem er aber seinen Seelenkopf hineinsteckte, war darinnen jene ahrimanische Kraft, welche sich äußerte in der Tätigkeit von unzähligen Lügen-dämonen. Und aus dieser selben Quelle heraus, aus der die sprach-bildende Kraft der damaligen Zeit geschöpft worden ist, aus derselben Kraft heraus entwickelte sich auf dem Boden der mittelmeerländischen Kultur diese riesige Kraft, diese gigantische Kraft des Lügens. Die Menschen logen, weil die Dämonen, die verbunden waren mit jenen",
      "andern Dämonen, welche das sprachbildende Vermögen eingaben, Lügner waten. Und diese dämonischen Lügner, die ahrimanischer Natur waren , hatten die Aufgabe, dasjenige zum Untergange zu bringen, was untergehen mußte, damit der dritte nachatlantische Zeit­raum hinuntergehen konnte und der vierte nachatlantische Zeitraum heraufkommen konnte.",
      "Die Welt ist eingerichtet nach Notwendigkeiten, und man muß auf diese Notwendigkeiten hinblicken, wenn man die große Frage, die wir gestern im Beginne unserer Betrachtungen aufgestellt haben, die große Frage nach dem Zusammenhange des Moralischen und des Ideellen mit dem Naturgeschehen, beantworten will. Davon will ich dann morgen weitersprechen, um diese Betrachtungen vorläufig zu einem kleinen Abschluß zu bringen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Ich werde die Betrachtungen, die wir jetzt hier pflegen, so anlegen müssen, daß ich heute die gestern gemachten Auseinandersetzungen erweiternd vorbringe, um dann morgen zu einem gewissen vorläufigen kleinen Abschluß zu kommen.",
        "Daher wird das Heutige mehr eine Episode zu bedeuten haben."
      ],
      [
        "Man hat in der Gegenwart ja sehr, sehr viel Veraniassung, auch aus den Zeitereignissen heraus, über dies oder jenes nachzudenken, wenn man nicht die Absicht hat, die wichtigsten Impulse unserer Zeit zu verschlafen.",
        "Besonders auffällig in der Gegenwart und, ich möchte sagen, Fragen herausfordernd ist ja die Erscheinung, die Ihnen doch wohl hinlänglich bekannt ist, daß im weitesten Sinne in dieser Gegen­wart die ungeheuerste Unwahrhaftigkeit Platz gegriffen hat, daß ge­rade da, wo Umfassendes heute spielt, Unwahrhaftigkeit vorhanden ist.",
        "Solche Dinge, wie das Auftreten von so wirksamer, so einschnei­dender Unwahrhaftigkeit veraniaßt dann auch, über allerlei damit Zusammenhängendes geisteswissenschaftlich nachzuforschen.",
        "Und da, kann man sagen, tritt einem oftmals ganz besonders die Tatsache entgegen, die ich auch hier schon öfter berührt habe, daß das, was zumeist als Geschichte der Menschheit mitgeteilt wird, eine Art Fable convenue ist.",
        "Dabei handelt es sich nicht so sehr darum, daß Tat­sachen, die mitgeteilt werden, etwa nicht bis zu einem gewissen Grade für richtig zu halten wären; aber andere Tatsachen - Sie erinnern sich, ich habe letzthin hier auseinandergesetzt, wie tiefstgehende Ein-flüsse eines Menschen aus der römischen Geschichte einfach gestrichen worden sind , sie werden einfach getilgt.",
        "Ungeheures an Tatsachen hat ja die Kirche aus der Geschichte ausgetilgt, weil der Kirche daran gelegen war, daß gewisse Tatsachen nicht zur Kenntnis der Menschen kommen."
      ],
      [
        "Nun haben wir gestern wiederum von einem Gesichtspunkte aus über die Zeit gesprochen, welche die griechisch4ateinische Kultur-periode einleitete, über den wichtigen Zeitabschnitt im 8. vorchrist­lichen"
      ],
      [
        "Jahrhundert.",
        "Es ist ja eine Zeit, aus der heraus nicht mehr viel die historischen Überlieferungen sprechen.",
        "Die historischen Über­lieferungen werden da schon sehr, sehr unsicher, aber es glänzt aus dem Beginne dieser Zeitepoche heraus eine Persönlichkeit, die sehr, sehr vielen Leuten Betrachtungen der verschiedensten Art abge­rungen hat.",
        "Es glänzt da aus der Entstehungszeit, also nach dem 8. vor­christlichen Jahrhunderte, der Name des Pythagoras heraus, der Name auch der Pythagoräischen Schule.",
        "Und ich habe ja gestern darauf hin­gewiesen, was aus den Überbleibseln der alten ägyptischen Mysterien­wahrheiten Pythagoras hat empfangen können, welcher Art diese Dinge waren, die Pythagoras hat empfangen können."
      ],
      [
        "Nun ist es nicht nur interessant, das zu betrachten, was Pythagoras und seine Schüler gesagt und getan haben, was ja sehr einschneidend war, denn sie haben nicht nur eine Lehrtätigkeit entwickelt, sondern eine weitgehende politische Tätigkeit.",
        "Was Pythagoras und seine Schüler getan haben, ist interessant, aber außerdem ist es bedeutsam, die Welt zu betrachten, die gewissermaßen dieses pythagoräische Treiben umgibt, die Welt, aus der dann auch das spätere Griechentum herausgewachsen ist, das ja schon einen gewissen Einfluß aufgenom­men hat auch desjenigen, was man, von besonderem Glänze erhellt, bei Pythagoras findet."
      ],
      [
        "Wenn man im 7., 6., 5.",
        "Jahrhundert vor unserer Zeitrechnung das Leben nimmt, aus dem dann das spätere griechisch-lateinische herausgewachsen ist, wenn man dieses Leben nimmt auf der griechischen Halbinsel und den angrenzenden Ländern und der italienischen Halbinsel, so fällt einem dann, wenn man die Dinge nicht der geschichtlichen Fable convenue nach betrachtet, sondern wenn man sie betrachtet im Lichte der Wahrheit - dazu muß immer die geisteswissenschaftliche Forschung dann ihre Beiträge geben -, be­sonders auf, daß eine Eigenschaft der Menschheit über dieses Leben sehr verbreitet war."
      ],
      [
        "Es wurde nämlich kaum zu irgendeiner Zeit so viel gelogen als zu dieser Zeit über die Mittelmeerländer hin.",
        "Das Lügen, das die Unwahrheitsagen den andern Menschen, das war eine ganz auffällige charakteristische Erscheinung alles desjenigen Lebens, aus dem dann das spätere Griechentum und Römertum hervorge­wachsen ist."
      ],
      [
        "Man muß sich in solchen Dingen keinen Täuschungen hingeben.",
        "Alles dasjenige, was man als die gewaltige Schönheit, als die bewun­derungswürdige Summe von Phantasieschöpfungen Griechenlands, was man als die großartigste Summe von Abstraktionen, die es je in der Welt gegeben hat, im Römertum sich entwickeln sieht, das alles wächst heraus, so wie die Pflanzenwelt aus dem Dünger herauswächst, aus einem Boden, der über die Mittelmeerländer ausgedehnt ist, aus einem Boden, den Menschen bewohnen, die ganz erfüllt sind von der Sucht, von der Leidenschaft des Lügens.",
        "Das ist etwas, was von der Geschichte weniger betont wird, was aber verstanden werden muß , wenn man richtig hineinsehen will in die untergehende dritte nach-atlantische Kulturzeit.",
        "Wir haben es ja, indem wir von den früheren Jahrhunderten und Jahrtausenden zum 8. vorchristlichen Jahrhundert heraufkommen, mit dem untergehenden dritten nachatlantischen Kul­turzeitraum zu tun.",
        "Und die Menschen, die damals die Kulturträger waren des dritten nachatlantischen Kulturzeitraumes, des untergehen­den dritten nachatlantischen Kulturzeitraumes, die waren im wesent­lichen große Lügner.",
        "Das ist gleichzeitig diejenige Epoche, in welcher sich ganz besonders entwickelt jene Fähigkeit, von der ich Ihnen gestern gesprochen habe und die so außerordentlich interessant ist:"
      ],
      [
        "jene Fähigkeit, aus dem Kosmischen der Vernunft heraus die Sprache zu bilden.",
        "Und es war das größte Talent eben dazumal vorhanden -neben solchen Dingen, wie ich sie gestern auseinandergesetzt habe -in der großen Sucht, zu lügen."
      ],
      [
        "Man darf sich in diesen Dingen ebensowenig einer Täuschung hin-geben, wenn man die Wirklichkeit betrachten will, wie man sich einer Täuschung darüber hingeben darf, daß das Veilchen, das im Frühling blüht, wiederum vergeht und die Kräfte des Vergänglichen, während es schön und herrlich blüht, schon in sich trägt.",
        "Da hat man bei dem Veilchen gewissermaßen nacheinander Entstehungskräfte und Zer­störungskräfte.",
        "Im Menschenleben, namentlich im großen Mensch­heitsieben, hat man das sehr, sehr häufig auch zeitlich nebeneinander , und man begreift nicht die Wirklichkeit, wenn man nicht die Notwen­digkeit begreift, daß solche Dinge nebeneinander sich bilden: Evo­lution und Devolution, die Möglichkeit, aufbauend zu wirken, wie"
      ],
      [
        "zum Beispiel eben in der Sprachbildung, und gleichzeitig jene ver­heerende Wirkung, welche auf das Geistesleben das Lügen ausübt."
      ],
      [
        "Das ist gewissermaßen die Kehrseite desjenigen, was ich Ihnen gestern auseinandergesetzt habe.",
        "Es gibt auch eine Lichtseite.",
        "Diese Lichtseite ist noch geisteswissenschaftlicherer Natur.",
        "Ich habe schon gestern darauf aufmerksam gemacht, daß es ja nicht möglich wäre, heute mit einer solchen Sicherheit über diese Dinge der Sprachbildung, die wir gestern besprochen haben, zu reden, wenn nicht das Leben des Menschen nach dem Tode einem den deutlichen Beweis davon geben würde, indem dasjenige, was hier im Leben zum Beispiel aus einzelnen Wortatomen oder Wortteilen zusammengesetzt wird an Worten, wiederum gelöst wird."
      ],
      [
        "Und dieses Lösen von Worten, dieses Zer­stäuben von Worten, das ist etwas, das im Leben der Toten eine be­deutsame Rolle spielt.",
        "Gewissermaßen lebt der Tote von diesem Zer­stäuben der Worte.",
        "Und der Tote hat das entschiedenste Gefühl, daß er in seinem Leben, also vor seinem Tode, von der geistigen Welt, in der er sich nach seinem Tode befindet, dadurch abgeschlossen war, daß er aus Lauten, aus Buchstaben zusammengesetzte Worte gebildet hat."
      ],
      [
        "Der Tote hat das Gefühl, daß die Sprache gewissermaßen ein Teppich ist, der sich im Leben vor die geistige Welt hingelegt hat.",
        "Und in dem Aufdröseln dieses Teppichs, in dem Auflösen der Worte hat er das Gefühl, daß er nun wiederum in die geistige Welt eintritt."
      ],
      [
        "Daher ist es eine der Eigenschaften des Toten, die Menschenworte, die der Betreffende kennengelernt hat innerhalb des Lebens zwischen Geburt und Tod, aufzulösen, zu zerpflücken, in ihre Bestandteile aufzu­lösen.",
        "Der Tote hat zum Beispiel ein ganz feierliches, großes Gefühl, wenn es ihm gelingt, ein gewisses Verständnis sich durch solche Auf­lösung zu erwerben."
      ],
      [
        "Ich habe Ihnen öfter davon gesprochen, daß der Moment des Todes ja in einer gewissen Beziehung etwas Schreck­haftes ist für das Leben hier im physischen Leibe.",
        "Die Menschen wenden ja auch gerne ihr Antlitz von dem Tode ab."
      ],
      [
        "Nach dem Tode ist der Anblick des Todes immer da - ich habe das öfters schon be­tont -, aber er bedeutet dann nichts Furchtbares; sondern indem der Mensch hinblickt auf seinen eigenen Tod von der andern Seite des Lebens aus, ist in diesem Anblick immer die Gewißheit"
      ],
      [
        "vorhanden, daß er ein Ich ist und ein Ich bleibt.",
        "Das habe ich ja öfter betont."
      ],
      [
        "Aber nun handelt es sich für den Toten darum, dasjenige zu ver­stehen, was sich ihm im Anblick des Todes von der andern Seite des Lebens aus offenbart.",
        "Dieses versteht er dadurch immer besser und besser, daß er, je nachdem er diese oder jene Sprache gesprochen hat, diese oder jene Worte auflöst."
      ],
      [
        "Die alten Hebräer und mit einer ge­wissen Ähnlichkeit noch die Römer, haben ja ihren sogenannten ge­heiligten Namen, den unaussprechlichen Namen des Gottes, Jahve.",
        "Dieser unaussprechliche Name bestand ja für die Hebräer in einer gewissen Zusammenfügung der von uns als fünf Vokzle empfundenen Laute, die verbunden gedacht wurden während des physischen Le­bens."
      ],
      [
        "Noch in dem römischen Jovis, Jupiter, ist ja nur eine andere Form des Jahvenamens verdeckt enthalten; er ist im Grunde in bezug auf die fünf Vokale in einer gewissen Weise verbunden in dem Jovis In der Auflösung desjenigen, was hier verbunden war in diesem Gottesnamen, lebte der Tote, und indem er die Vokale, die zusammen­gesetzt waren im Leben, auflöste, enthüllte sich ihm auch zugleich der Sinn, könnte man sagen, des Todes.",
        "Die Enthüllung dieses Sinnes des Todes, die muß man nur versuchen, in der richtigen Weise wenig­stens zu ahnen."
      ],
      [
        "Man muß verstehen, daß sich dem Toten enthüllt dieser Sinn des Todes durch die Auflösung des heiligen Namens in seine Bestandteile, die dann verklingen und verklingend forttönen in der Welt.",
        "Die Auflösung dieses heiligen Namens ist verknüpft mit dem Verständnis der Vergeistigung des Todes."
      ],
      [
        "Es ist das ein Begriff, den man außerordentlich schwer schildern kann.",
        "Der Tod, von der andern Seite angesehen, kann Vergeistigung genannt werden.",
        "Indem der Tod von der andern Seite angeblickt wird, ist dieser Anblick ver­knüpft mit der Entstehung von Geistigem."
      ],
      [
        "Und in dem Zerpflücken des Wortes nach den Vokalen enthüllt sich das Geistige aus dem Zer­fall heraus, den der Tod bedeutet.",
        "Zerfall ist da zu gleicher Zeit Ge­burt des Geistigen, Entstehung des Geistigen."
      ],
      [
        "Während man den Zerfall in unsympathischer Weise als etwas Unschönes empfindet wie jede Zerstörung, enthüllt sich von der andern Seite gesehen diese Zerstörung als ein Aufleuchten des Geistigen, das dann verstanden"
      ],
      [
        "wird in dem Verklingen.",
        "Es ist, als ob das heilige Wort weit hinaus­klänge, hinausstrahlte, und im Hinausstrahien sich eben in seine vo­kalischen Bestandteile auflöste, die dann hörbar sind wie aus der Peripherie der Welt herein, und dann hörbar machen den Sinn des Todes, den Geistsinn des Todes."
      ],
      [
        "Das schon wird Sie darauf lunleiten, daß es berechtigt ist, geradeso wie man von Gliedern der Menschennatur spricht hier im Leben, physischer Leib, Ätherleib, astralischer Leib und Ich, zu sprechen von den Gliedern der Menschennatur, die diese Menschennatur zwi­schen dem Tod und einer neuen Geburt hat.",
        "Denn indem ich Ihnen gewissermaßen die zentrale Erscheinung, die der Mensch fortwäh­rend zwischen dem Tod und einer neuen Geburt hat, diese Enthüllung des geistigen Sinnes des Todes selbst, hingestellt habe, muß die Frage entstehen: Wie sieht denn eigentlich diese Welt aus, die da nach dem Tod für die Menschen sich enthüllen soll? - Das kann man aber nicht anders fassen, als indem man die Natur und Wesenheit des Menschen selbst etwas kennenlernt."
      ],
      [
        "Nun wollen wir heute zunächst einmal versuchen, den Toten eben­so zu beschreiben, wie man sonst den Lebenden beschreibt.",
        "Da kann man zunächst anfangen mit demjenigen Gliede des toten Menschen, welches noch viel Zusammenhang - nicht Verwandtschaft, aber Zu­sammenhang - hat mit dem, was der Mensch hier durchiebt zwischen der Geburt und dem Tode.",
        "Da hat man es also dann mit dem ersten Gliede der Menschennatur zu tun, das man auch das Ich nennen kann, wie man gewissermaßen für hier das zunächst höchste Glied der Menschennatur zwischen Geburt und Tod nennt.",
        "Wir sehen jetzt da­von ab, daß es zunächst, unmittelbar nach dem Tode, noch die Hülle des Ätherleibes hat, der dann abgelöst wird, und noch die Hülle des Astralleibes hat, die auch im Laufe der Zeit abgelöst wird; das sind Bestandteile, die gewissermaßen nicht dazugehören.",
        "Wenn man von dem toten Menschen spricht, so ist als ureigenes Glied dieses toten Menschen doch zunächst nur anzuerkennen das Ich.",
        "Ich sagte, es ist ein Zusammenhang mit dem Ich des Erdeniebens, nicht aber eine eigentliche Verwandtschaft; denn in der Tat stellt sich dieses Ich nach dem Tode in einer ganz andern Weise dar, als das Ich erlebt wird zwischen"
      ],
      [
        "der Geburt und dem Tode.",
        "Zwischen der Geburt und dem Tode ist das Ich gewissermaßen etwas Flüssiges, etwas, was in sich die Kraft fühlt, jeden Tag anders zu werden.",
        "Denken Sie nur, wie schrecklich es im leiblichen Leben zwischen Geburt und Tod wäre, wenn Sie nicht imstande wären, den Gedanken zu fassen: Ich habe gestern irgend etwas Schlimmes getan, aber ich kann das wiederum ausbes­sern, ich kann dafür etwas Gutes tun. - Oder wenn Sie, noch jünger, sagen müßten: Ich habe wenig gelernt, aber ich kann nichts dazu­lernen. - Jn keinem Momente des Lebens zwischen der Geburt und dem Tode ist das Ich etwas so Festes, daß es nicht gewissermaßen durch seine eigene Willenskraft von innen heraus geändert werden könnte."
      ],
      [
        "Dasjenige, was Sie erleben als Ich nach dem Tode, das ist etwas Festgewordenes, das hat gewisse Eigenschaften angenommen, die nun nicht unmittelbar geändert werden können; das bleibt so, wie es ist.",
        "Die Umwandlung des im Leben zwischen Geburt und Tod fort-dauernd flüssigen Ich in ein festes Gebilde, in dem nichts sich ändern kann, das so bleibt, wie es sich im Leben geformt hat, das ist das Wesentliche, das festgehalten werden muß zum Verständnis dieses Ich nach dem Tode."
      ],
      [
        "Von einer Entwickelung, von der wir ja sprechen müssen für das Ich zwischen Geburt und Tod, kann nach dem Tode nicht die Rede sein.",
        "Nach dem Tode ist das Ich gewissermaßen ein festes Geistgebilde, das herausentspringt aus dem Anblick des Todes selber, und es kann nichts an diesem Ich geändert werden."
      ],
      [
        "Man könnte sagen, wenn man diese Sache mehr oder weniger banal aussprechen wollte: Der Mensch ist verurteilt, nach dem Tode alle Einzelheiten seines Lebens wie etwas Festes anzusehen.",
        "Wie Sie, wenn Sie über einen Acker hinsehen, die nahen Pflanzungen und die fernen Pflan­zungen nebeneinander sehen, und wie Sie dadrinnen nichts Flüssiges, sondern ein festes, ausgedehntes, zunächst bleibendes Gebilde sehen, so übersehen Sie die ganze Strecke Ihres Lebenslaufes, aber so, daß nicht immer, wie es im Leben des physischen Leibes ist, das Vordere durch das Hintere ausgelöscht wird, sondern Sie übersehen es als ein bleibendes konkretes Feld, in dem Sie durch den bloßen Anblick zu-nächst nichts ändern können."
      ],
      [
        "Es wäre auch schlimm für den Toten, wenn das nicht so wäre; denn sein Blick, der Blick des Toten ist eigentlich"
      ],
      [
        "zunächst hauptsächlich in Anspruch genommen von diesem Ich.",
        "Er ist wie hineingebannt in dieses Ich.",
        "Und würde dieses Ich ver­schwinden, so würde es für den Toten ebenso sein, als wenn für den Lebenden die umliegende Welt der Sinne verschwinden würde.",
        "Der einzelne Mensch in seinem Ich ist tatsächlich für sich selbst, wenn ich mich so ausdrücken darf, so wichtig - damit sprechen wir aber eine bedeutsame Wahrheit aus - wie die ganze Sinnenwelt, die wir als Menschen gemeinsam haben, für den Menschen hier im physischen Leben ist.",
        "Ein ungeheurer Abgrund täte sich auf, der Abgrund des Nichts geradezu, wenn wir nach dem Tode nicht imstande wären, das erstarrte Ich, das aus dem flüssigen Zustande erstarrte Ich im An­blick zu haben."
      ],
      [
        "Als zweites haben wir eine Art von Geistwesen, das wir in Analogie mit dem, was wir schon kennen, auch Geistselbst nennen können.",
        "Als zweites Glied also der menschlichen Wesenheit nach dem Tode haben wir eine Art Geistwesenheit.",
        "Diese Geistwesenheit wird dem Men­schen hauptsächlich so bewußt, daß ihm dieses Bewußtsein des Geist-selbst wie von innen aufgeht.",
        "Während das Ich eine Art äußeren An­blick darbietet, geht das Bewußtsein dieses Geistselbst von innen heraus auf.",
        "Und in demselben Maße, in dem man fühlt: Dieses Geist-selbst belebt sich -, in demselben Maße treten herauf aus dem Be­wußtsein, so daß man weiß, sie sind da, die Wesenheiten der höheren Hierarchien.",
        "Ich nenne dieses also: «das Geistselbst» - ich muß es ge­nau so definieren, wie ich es jetzt auf die Tafel schreibe, sonst würde ich Ihnen etwas Ungenaues schreiben - «gerichtet durch die Hierar­chien auf das Ich»."
      ],
      [
        "Das, was ich jetzt geschrieben habe, gibt ungefähr den Tatbestand ganz richtig.",
        "Sie haben das Gefühl: Da ist ein Wesen aus der Hierar­chie der Angeloi, aus der Hierarchie der Exusiai, das richtet jetzt den Blick auf Ihr Ich.",
        "Indem Sie Ihren Blick auf das Ich richten, das eine Mal durch irgendein Wesen einer Hierarchie, das andere Mal dadurch, daß Sie wissen, jetzt ist Ihr Blick auf das Ich durch ein Wesen der andern Hierarchie gerichtet, lernen Sie diese Hierarchie innerhalb des Wirkens Ihres Geistselbst kennen.",
        "Also in Ihrer eigenen Betätigung lernen Sie die Hierarchien kennen.",
        "Sie fangen an, durch Ihr Geistselbst"
      ],
      [
        "sich in Gesellschaft der Hierarchien zu befinden.",
        "Und während Sie, bevor dieses Geistselbst aufleuchtet, noch das Gefühl haben, nur Sie selbst beschäftigen sich damit, den Blick hinzurichten auf das eigene Ich, bekommen Sie immer deutlicher das Gefühl, daß sich immer mehr und mehr Wesenheiten der höheren Hierarchien um Sie kümmern und sich hineinmischen in Ihr Schauen, Ihre Blicke lenken.",
        "Sie fühlen sich, indem Sie Ihre höhere Sinnestätigkeit entwickeln , durch das Geistselbst immer mehr und mehr so, daß in dieser Sinnes-tätigkeit mittätig sind die Wesen der höheren Hierarchien.",
        "Was un­erträglich wäre für den Menschen der Sinneswelt hier, das wird ge­radezu das Lebenselement für den Menschen im Zustande nach dem Tode."
      ],
      [
        "Denken Sie sich einmal, Sie stünden hier am Fenster und schauten hinaus und sollten die Umgebung betrachten.",
        "Einer von Ihnen stellte sich dahin und wollte die Umgebung betrachten, und der erste, der hier sitzt, geht hin, dreht Ihnen den Kopf nach der einen Seite, damit Sie irgend etwas betrachten nach jener Richtung; ein zweiter geht hin, dreht Ihnen den Kopf ein bißchen hinauf, damit Sie etwas anderes betrachten; ein dritter wiederum ein bißchen herum, damit Sie wieder etwas anderes betrachten, und so würde die ganze Gesellschaft, die hier sitzt, von hinten Ihnen sich nähern, und Sie würden nur dadurch den Aspekt Ihrer Umgebung draußen haben, daß dasjenige, was hier herinnen sitzt, Ihnen den Kopf fortwährend darnach hinrichtet.",
        "Denken Sie das jetzt nicht von außen angesehen, sondern als inneres Erlebnis, als inneres Empfinden, dann haben Sie aber etwas, was recht analog ist diesem Erleben, das Sie als Ihr Geistselbst haben.",
        "Sie leben sich in das Lehen der höheren Hierarchien dadurch immer mehr hinein, daß diese höheren Hierarchien in Ihre Blickrichtung hineinkommen."
      ],
      [
        "In dem Auflösen der Worte, von dem wir schon gesprochen haben , wirken schon die Wesenheiten der höheren Hierarchien.",
        "Das ist eine Seite desjenigen, was da erlebt wird.",
        "Aber es ist ja die fortdauernde Bereicherung des Lebens, die dadurch entsteht, daß man nach und nach immer mehr und mehr mit den Hierarchien bekannt wird.",
        "Und in einer ganz ähnlichen Weise wird man bekannt mit den Wesenheiten ,"
      ],
      [
        "mit denen man irgendwie karmisch vor dem Tode verbunden war.",
        "Und da fühlt man, daß man gewissermaßen geleitet und gelenkt wird.",
        "Das ist dasjenige, was gesagt werden kann über das zweite Glied der menschlichen Wesenheit in dem Leben zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Das dritte Glied ist etwas, was zunächst vielleicht auf das Ver­ständnis des Menschen etwas schocklerend wirken könnte.",
        "Man fühlt sich nach und nach, indem man sich in dieses Leben nach dem Tode hineinlebt, durchsetzt von einer gewissen Kraft, ich könnte vielleicht sagen, von einem Kräftezusammenhang.",
        "Indem man zuerst gefühlt hat, die Hierarchien kommen heran und leiten einen bei der übersinn­lichen Sinnestätigkeit - wenn ich den Ausdruck bilden darf -, fühlt man nach und nach: diese Hierarchien durchträufeln einen mit Kraft, geben einem Kraft.",
        "Man fühlt sich nach und nach erfüllt von dieser Kraft, welche die Hierarchien mit einfließen lassen, indem sie sich in einen hineinsetzen, indem sie ihr Wesen in einen hineinträufeln.",
        "Diese Kraft fühlt man allmählich.",
        "Man fühlt, daß man durch die Hierarchien nicht nur hingelenkt wird auf das oder jenes, sondern man fühlt, daß man durch diese Tätigkeit der Hierarchien, die zunächst auftritt wie eine das Schauen vermittelnde Tätigkeit, selbst innerlich krafterfülit wird.",
        "Man fühlt die Kräfte des Kosmos, wirklich des Kosmos in sich einströmen wie belebende Säfte.",
        "Aber nun, was das Schockierende ist, das ist, daß die Kräfte, die man jetzt in sich einströmen fühlt, von einer ganz eigentümlichen Art sind.",
        "Es sind Kräfte, welche zunächst durchaus nicht fördernd, sondern auflösend, vernichtend sind für das, was man hier in der physischen Welt Leben nennt.",
        "Man fühlt sich nach und nach erfüllt von kosmischer, todbringender Weltenkraft."
      ],
      [
        "Es ist wichtig, solche merkwürdigen Vorstellungen in sich aufzu­nehmen, weil nur dadurch die geistige Welt wirklich begriffen werden kann.",
        "Denken Sie sich einmal eben in Ihrer geistig-seelischen Wesen­heit nach und nach erfüllt von Kräften, von denen Sie das Bewußt­sein erhalten, indem Sie sie in sich erleben: Durch diese Kräfte wird alles dasjenige, was hier auf der Erde lebt, wenn Sie es berühren wür­den, getötet. - Also Sie kleiden sich drittens in das, was ich, in Analogie mit etwas, was wir schon kennen, nennen kann den Lebensgeist."
      ],
      [
        "Sie kleiden sich in etwas , was man Lebensgeist nennen kann, was aber seine hauptsächlichsten Eigenschaften dadurch hat, daß es er-tötend ist für dasjenige, was man sonst die Kraft des Lebensleibes nennen kann.",
        "Und Sie bekommen ein drittes Glied Ihrer Wesenheit, durch das Sie in der Lage sind, jeden Ätherleib, der Ihnen in die Quere kommt, zu töten."
      ],
      [
        "Alles, was Sie berühren durch dieses Glied Ihrer Wesenheit, wird in dem Sinne tot, in dem man von dem Tode hier auf Erden spricht.",
        "Und indem Sie durch das, was Sie da an Kräf­ten bekommen, töten, wecken Sie aus dem Getöteten Geistiges auf, zunächst eigentlich Seelisches au£ Es ist dieses ein merkwürdiges Er­lebnis, das darin besteht, daß durch die Berührung von Lebendigem das Lebendige getötet wird, aber aus dieser Tötung Seelisches ent­springt, Seelisches erlöst wird."
      ],
      [
        "Es ist ein Töten, aber es ist zu gleicher Zeit eine Erlösung des Seelischen aus den Banden des Lebens.",
        "So daß man sagen kann: Der Lebensgeist tötet irdisch Lebendiges, in ihm Seelisches auslösend.",
        "Und man kommt zu dieser merkwürdigen Er­fahrung dadurch, daß in dem Leben, in dem Lebendigen gewisser­maßen Seelisches verzaubert ist, und daß durch diesen Vorgang, der da nach dem Tode geübt wird, das verzauberte Seelische aus dem Lebendigen herauserlöst wird."
      ],
      [
        "Man könnte geneigt sein, in der Tötung, in der ja im wesentlichen die Kraft wirkt, von der wir hier reden, etwas Furchtbares, Unsympathisches zu sehen.",
        "Für das Leben nach dem Tode ist das nicht der Fall, weil in dem Töten, in der töten­den Kraft das fortwährende Aufleuchten des Seelischen liegt, weil da­durch das fortwährende Entstehen des Seelischen entzündet wird."
      ],
      [
        "Aber dieses Bewußtsein muß der Tote haben: nicht nur, daß er immer hinsieht auf den Tod, den er selbst durchgemacht hat, sondern er muß auch bewußt sein dessen, daß dasjenige, was das Wesen seines Todes ist, sich gewissermaßen auf dem Untergrunde alles desjenigen aus­hreitet, was er nun in der geistigen Welt erlebt.",
        "Es ist, wie wenn man in der geistigen Welt nunmehr so lebte, daß man sagen kann: Hier in dieser geistigen Welt entstehen fortwährend geistige Gebilde, zu­nächst eigentlich seelische Gebilde; Seelisches leuchtet auf in der ver-schiedensten Weise."
      ],
      [
        "Aber wenn man nachfragen würde, was der Boden ist, aus dem all dieses Seelische heraussprießt, so ist es diese"
      ],
      [
        "Tötekraft, die wir soeben besprochen haben.",
        "Eine solche, das ge­wöhnliche hier auf der Erde befindliche Leben zerstörende Kraft ist also unser wesentliches Seelisches, das wir uns aneignen müssen zwi­schen dem Tod und einer neuen Geburt, wie wir uns hier im Leben aneignen müssen unseren fleischlichen Leib."
      ],
      [
        "Als viertes Glied kann ich, wiederum in Analogie mit dem, was wir schon kennen, sagen: der Geistesmensch.",
        "Dieser Geistesmensch, der wird als etwas, was man in der Zeit zwischen dem Tod und einer neuen Geburt zu sich zu rechnen geneigt ist, dadurch empfunden, daß nun wiederum mit den Kräften, die schon eingeträufelt werden durch die Hierarchien, wie ich geschildert habe, einem jetzt die Möglichkeit ein­geträufelt wird, nicht nur Leben - was man hier auf Erden Leben nennt - zu töten, zu zerstören, aufzulösen, sondern Formen zu ver­nichten beziehungsweise auch in andere zu verwandeln.",
        "Also: Erstens das Ich; zweitens das Geistselbst, gerichtet durch die Hierarchien auf das Ich; drittens der Lebensgeist tötet irdisch Lebendiges, in ihm Seelisches auslösend; viertens der Geistesmensch."
      ],
      [
        "Es wird natürlich immer schwieriger, diese Dinge zu schildern.",
        "Aber im wesentlichen ist die Kraft dieses Geistesmenschen, wie man sie hat zwischen dem Tod und einer neuen Geburt, darin bestehend, daß man die entgegengesetzte Tätigkeit - wenn ich mich so aus­drücken darf - von alldem verrichtet, was man nennen könnte: Er­zeugung von Formen im weitesten Sinne.",
        "Hier - wenn ich mich bei einem speziellen Beispiele beruhigen will - zeichnet man Dreiecke, Vierecke und so weiter.",
        "Nach dem Tode, vermöge der Kräfte, die hier entwickelt werden, «entzeichnet» man, man löst alles Gezeichnete, die Formen au£ Aber das Eigentümliche ist, daß dies nicht bloß be­deutet, daß man etwas entzeichnet, sondern das ist zu gleicher Zeit eine kosmische Tätigkeit.",
        "Man ist jetzt selber in der kosmischen Tätig­keit drinnen, man ist verknüpft mit der kosmischen Tätigkeit.",
        "Denn dieses Entzeichnen, dieses Entformen, dieses Auflösen von Formen, das ist eine kosmische Tätigkeit, und der Mensch, indem er sich an­geeignet hat, nachdem er mit dem Lebensgeiste durchzogen war, diese Kraft der Entformung, ist mit ein Stück der kosmischen Welt ge­worden.",
        "Er wirkt im Kosmos drinnen."
      ],
      [
        "Es hat dasjenige, was hier auf der Erde Zerstörung, Untergang heißt, viel zu tun mit Entstehung, mit Bildung in den geistigen Welten.",
        "Und umgekehrt: Mit dem, was für uns Her wie Zerstörung, wie Untergang, wie Entformung, Entzeichnung aussieht, hat Ent­stehung in den andern, in den geistigen Welten viel zu tun.",
        "So daß, wenn ich von Entzeichnung, Eniformung spreche, ich nicht von Untergang in der geistigen Welt, sondern nur von Untergang in der seelischen Welt, dagegen von Auftauchen von geistig Neuem in der geistigen Welt spreche."
      ],
      [
        "Mit diesen Dingen hängen mancherlei Geheimnisse in der Welt zu­sammen.",
        "Sie nähern sich heute Unteritalien von Mittelitalien aus; Sie kommen, indem Sie sich Unteritalien nähern, in Gegenden, die arm sind, die gar nicht besonders fruchtbar sind, in denen wenig Natur-reichtum den Menschen zur Verfügung steht."
      ],
      [
        "Es sind dieselben Gegenden, in denen zur Zeit des aufgehenden vieflen nachatlanti­schen Zeitraumes Pythagoras gewirkt hat.",
        "Und Pythagoras' Wirksam­keit war damals inmitten fruchtbarster, reichster, üppigster Gegenden."
      ],
      [
        "So kurz die Zeit ist seit jener Epoche: indem man gerade auf diesen Fleck Erde hinweist, wo Phythagoras gewirkt hat, hat man die Um­wandlung von einer Fruchtbarkeit und Üppigkeit, die bis zu dem Grade der Sybaris ging, die Sybaris in Armut umgewandelt, sogar bis zur Entstehung bedenklicher Krankheitserscheinungen.",
        "An der Stelle von sprossendem, üppigem Leben, das in jenen Zeiten da war, in die nur noch wenig Historisches zurückgeht, entwickelt sich etwas, was imVer­gleich zu jenem üppigen, sprossenden Leben auch Naturarmut ist."
      ],
      [
        "Und es ist eigentlich im höchsten Grade interessant, solche Übergänge in der äußeren Welt zu sehen.",
        "In dieser äußeren Welt gliedern sich forwährend zusammen Entstehen, Vergehen.",
        "Die Menschen denken mit ihrer Geschichtsforschung nur nicht so weit, daß sie das fort­währende Entstehen und Vergehen miteinander richtig verknüpfen würden."
      ],
      [
        "Mitten in der strotzenden Üppigkeit, in der ganz großartig gelogen wurde, hat Pythagoras seine Tätigkeit entfaltet, und diese Tätigkeit setzte sich fort nach seinem Tode.",
        "Und dasjenige, was Py­Ihagoras und die Pythagoräerseelen nach dem Tode zu tun hatten, hängt vielfach mit dem zusammen , was sich äußerte in dem Untergang"
      ],
      [
        "des blühenden, sprossenden Lebens, imrütten dessen Pythagoras war.",
        "Nicht ganz unbeteiligt an dem Zerstörungswerk - das für das Jenseits ein Entstehungswerk ist, -, das sich an der Stätte üppigen, sprossenden Lebens innerhalb der Natur aufrichtete in der nach­pythagoräischen Zeit, sind Pythagoras und die Seelen seiner Ar:ään­ger.",
        "Und man muß sich, wenn man die Gesamtwelt verstehen will, eben bekanntmachen damit, daß von den verschiedenen Aspekten aus hier zwischen Geburt und Tod und zwischen Tod und neuer Geburt die Dinge sich ganz anders ausnehmen.",
        "Derjenige, der Frevel be­gehen würde, wenn er hier üppiges, sprossendes Leben künstlich untergraben würde, der tut gewissermaßen nur etwas, was im Sinne der ewigen Notwendigkeit geschieht, wenn er sich in dem Leben zwischen Tod und neuer Geburt an einem solchen Werke beteiligt, das hier offenbar Untergang bedeutet."
      ],
      [
        "Mit dem dritten nachatlantischen Zeitraum sollte auch etwas un­tergehen, und das hinterließ seine Schatten.",
        "Viel sollte untergehen auf einem andern Gebiete, als das eben besprochene.",
        "Und mit diesem Untergehen der dritten nachatlantischen Epoche hängt es im wesent­lichen zusammen, daß damals so viel gelogen worden ist.",
        "Auf der Erde wurde gelogen, weil die Menschen, wie ich Ihnen gestern aus­geführt habe, noch mit den kosmischen Kräften in Verbindung stan­den; aber gerade die kosmischen Kräfte, die dazumal vor dem 8. vor-christlichen Jahrhundert in die Erdenentwickelung hereinspielten, waren vielfach lügnerische Kräfte.",
        "Dämonische Lügner waren tätig in der Sphäre, in die der Mensch seine Seele hineiniebte, indem er die Worte so entwickelte, wie ich gestern auseinandergesetzt habe.",
        "Er mußte gleichsam seinen Seelenkopf hineinstecken in eine Sphäre, in der er das tun konnte: die Sphäre der kosmischen Vernunft.",
        "Indem er aber seinen Seelenkopf hineinsteckte, war darinnen jene ahrimanische Kraft, welche sich äußerte in der Tätigkeit von unzähligen Lügen-dämonen.",
        "Und aus dieser selben Quelle heraus, aus der die sprach-bildende Kraft der damaligen Zeit geschöpft worden ist, aus derselben Kraft heraus entwickelte sich auf dem Boden der mittelmeerländischen Kultur diese riesige Kraft, diese gigantische Kraft des Lügens.",
        "Die Menschen logen, weil die Dämonen, die verbunden waren mit jenen"
      ],
      [
        "andern Dämonen, welche das sprachbildende Vermögen eingaben, Lügner waten.",
        "Und diese dämonischen Lügner, die ahrimanischer Natur waren , hatten die Aufgabe, dasjenige zum Untergange zu bringen, was untergehen mußte, damit der dritte nachatlantische Zeit­raum hinuntergehen konnte und der vierte nachatlantische Zeitraum heraufkommen konnte."
      ],
      [
        "Die Welt ist eingerichtet nach Notwendigkeiten, und man muß auf diese Notwendigkeiten hinblicken, wenn man die große Frage, die wir gestern im Beginne unserer Betrachtungen aufgestellt haben, die große Frage nach dem Zusammenhange des Moralischen und des Ideellen mit dem Naturgeschehen, beantworten will.",
        "Davon will ich dann morgen weitersprechen, um diese Betrachtungen vorläufig zu einem kleinen Abschluß zu bringen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "NEUNTER VORTRAG Dornach, 2. September 1918",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "Die Betrachtungen, die wir gegenwärtig anstellen, betreffen Dinge, welche von vielen Menschen, die etwas in der einen oder andern Form davon wissen, als Mysterien behandelt werden. Und es wird aus ge­wissen Gründen das Wissen von diesen Dingen der Welt von vielen Seiten her ferne gehalten, weil man der Ansicht ist, daß eben die Dinge, die in Betracht kommen, Teile sind von einem umfassenden Wissen über übersinnliche Angelegenheiten, das der Menschheit heute noch nicht mitgeteilt werden solle. Ich halte diese Anschauung mit Bezug auf gewisse Dinge, von denen hier die Rede ist, nicht für richtig, sondern mir erscheint es notwendig, daß die Menschheit den mutigen Entschluß fasse, einzutreten in eine wirkliche Betrachtung der übersinnlichen Welten. Und das kann man doch nicht anders, als wenn man das, was konkret über die betreffende Frage in Betracht kommt, unmittelbar anfaßt.",
      "Nun möchte ich heute gewissermaßen zuerst eine Art von Vorfrage erledigen. Wir haben gestern gesprochen über die Gliederung des Menschen zwischen dem Tode und einer neuen Geburt. Ein sehr ver­breiteter Einwand gegen das Besprechen dieser Dinge, jetzt nicht von seiten der Eingeweihten, sondern von seiten der Uneingeweihten, ist der, daß man einfach sagt: Ja, wozu ist es nötig, über diese Dinge etwas zu wissen? Man könnte ja warten, bis der Mensch durch die Pforte des Todes durchgeht, und dann werde er schon sehen, wie es da in der geistigen Welt eigentlich aussieht. - Es ist also etwas, das sehr häufig gesagt wird. Nun, die Sache ist aber so, daß wir solche Fragen niemals von einem gewissermaßen absoluten Standpunkte aus beantworten können, wenn wir über das Wirkliche sprechen, sondern daß wir sie, geisteswissenschaftlich betrachtet, immer beantworten müssen von dem Gesichtspunkte der Zeit, in der wir leben. Wir leben im fünften nachatlantischen Zeitraum, der begonnen hat im 15. Jahrhundert un­serer Zeitrechnung. Er schloß den vierten nachatlantischen Zeitraum ab , wie wir wissen, der im 8. vorchtistlichen Jahrhundert begonnen",
      "und im 15. nachchristlichen Jahrhundert seinen Abschluß gefunden hat. Man hat sieben solcher Kulturzeiträume zu verzeichen. Daraus aber ist ersichtlich, daß wir die Mitte der Kulturentwickelung der Erde überschritten haben, die im vierten nachatlantischen Zeitraum lag, und daß wir einfach durch diesen Umstand eintreten - wir sind ja auch in der fünften großen Erdenperiode - in die Zeit, in der die Erde in absteigender Entwickelung ist.",
      "Schon die Betrachtungen, die wir in diesen Tagen angestellt haben , können Sie darauf aufmerksam machen, daß es darauf ankommt, hin-zuschauen auf die absteigende Entwickelung, auf dasjenige, was ge­wissermaßen nicht in der Evolution, sondern in der Devolution ist , was in der Rückentwickelung ist. Unsere ganze Erdenentwickelung ist in der Rückentwickelung.",
      "Da hören gewisse Fähigkeiten, gewisse Kräfte auf, die in der vorhergehenden Zeit der aufsteigenden Ent­wickelung da waten, und andere müssen für diese aufhörenden Kräfte und Fähigkeiten eintreten. Und so ist es insbesondere mit Bezug auf gewisse innere seelische Fähigkeiten des Menschen.",
      "Man kann sagen: Bis zum vierten nachatlantischen Zeitraum, bis gegen die Zeit des Mysteriums von Golgatha hin, waren in den Menschen noch die Fähigkeiten vorhanden, mit der übersinnlichen Welt einen gewissen Zusammenhang zu haben. Wir wissen, daß in der mannigfaltigsten Weise diese Fähigkeiten verschwunden sind.",
      "Sie sind nicht mehr als elementarische Fähigkeiten vorhanden, sie sind gewissermaßen dahin-geschwunden. Nicht nur hat sich das Leben des Menschen auf der Erde zwischen der Geburt und dem Tode geändert mit Bezug auf solche Fähigkeiten, sondern eigentlich, und noch radikaler, hat sich das Leben der Menschen zwischen dem Tod und einer neuen Geburt geändert.",
      "Und da muß gesagt werden, daß für diesen Zeitraum, vom Tode bis zur neuen Geburt, es im gegenwärtigen Menschheitszyklus, der also schon zu den absteigenden gehört, so ist, daß die Menschen , wenn sie durch die Pforte des Todes treten, gewisse Erinnerungen ha­ben müssen an dasjenige, was sie sich erworben haben hier im physi­schen Leibe, wenn sie die richtige Stellung und das richtige Verhältnis zu den Ereignissen, denen sie ausgesetzt sind zwischen dem Tod und einer neuen Geburt, finden wollen. Es gehört geradezu zu den notwendigen",
      "Vorbedingungen eines rechten Lebens nach dem Tode, daß die Menschen immer mehr und mehr hier vor dem Tode gewisse Vor­stellungen sich erwerben über das Leben nach dem Tode, denn nur, wenn sie sich erinnern an diese Vorstellungen, die sie sich hier er­worben haben, können sie sich orientieren in der Zeit zwischen dem Tod und einer neuen Geburt. Es ist sachlich unrichtig, wenn behauptet wird, man könne warten bis zum Tode mit solchen Vorstellungen über das Leben zwischen dem Tod und einer neuen Geburt.",
      "Würden die Menschen fortfahren, in diesen Vorurteilen zu leben, würden sie es fortdauernd ablehnen, Vorstellungen schon hier gewinnen zu wol­len über das Leben zwischen dem Tod und einer neuen Geburt, so würde dieses Leben, dieses leibfreie Leben für sie ein finsteres werden, ein unorientiertes werden; sie würden nicht - durch alles dasjenige, was ich Ihnen gestern geschildert habe - in der richtigen Weise in ihre geistige Umgebung eindringen können. Bis nahe zum Mysterium von Golgatha war es so, daß die Menschen sich hier ins physische Leben Fähigkeiten hereingebracht haben, die aus der geistigen Welt stamm­ten.",
      "Daher hatten sie atavistisches Hellsehen. Dieses atavistische Hell-sehen kam davon, daß gewisse geistige Fähigkeiten sich aus dem Zu­stand vor der Geburt hereinerstreckten in dieses Leben. Das hörte auf.",
      "Die Menschen haben keine Fähigkeiten mehr hier im physischen Leben, die sich hereinerstrecken aus dem vorgeburtlichen Leben. Das wissen Sie ja. Aber dafür muß umgekehrt das andere eintreten: Die Men­schen müssen sich immer mehr und mehr hier auf der Erde Vorstel­lungen über das Post-mortem-Leben, das Leben nach dem Tode, erwerben, damit sie sich erinnern können nach dem Tode, damit sie durch des Todes Pforte etwas durchtragen können.",
      "Das ist dasjenige, was ich zu dieser Vorfrage insbesondere bemer­ken will. Also die bequeme Rede, daß man warten könne bis zum Tode mit solchen Vorstellungen, die gilt nicht, wenn man im Kon­kreten ins Auge faßt, in welchem Zeitpunkt der Erdenentwickelung wir uns eigentlich befinden. Und das muß man wirklich immer im Konkreten ins Auge fassen. Denn Ansichten, die absolut gelten, die zu allen Zeiten gelten, die gibt es nicht, sondern es gibt immer nur Anschauungen, welche für einen gewissen Zeitraum den Menschen",
      "orientieren können. Das ist dasjenige, was man gerade durch Geistes­wissenschaft sich in so eminentem Sinne aneignen muß.",
      "Und nun möchte ich auf einiges eingehen, das unsere Betrachtungen zu einem vorläufigen kleinen Abschluß bringen kann. Wir sind ausge­gangen davon, daß der gegenwärtige Mensch eine Kluft empfindet zwischen dem, was er Ideale nennt, seien es moralische oder sonstige Ideale, was er auch Ideen nennt, und dem, was er als seine Anschau­ungen empfindet über die rein natürliche Weltenordnung. Die Be­griffe und Anschauungen, die sich der Mensch macht über die natür­liche Weltenordnung, die befähigen ihn nicht, anzunehmen, daß das-j enige, was er als Ideale in seinem Herzen trägt, reale Macht hat, sich wirklich so wie eine Naturkraft realisieren kann.",
      "Das Wesentliche, was für diese Frage in Betracht kommt, ist nun das Folgende: Wir wissen jetzt, wie es mit der Gliederung des Men­schen hier auf der physischen Erde steht. Wir wissen auch, wie es steht mit der Gliederung des Menschen in der geistigen Welt zwischen dem Tod und einer neuen Geburt.",
      "Ich habe vor einiger Zeit eine Frage aufgeworfen, welche eigentlich schon als eine konkrete Frage vor die menschliche Seele tritt, wenn der Mensch das Leben betrachtet, welche aber gerade eine Frage ist, der gegenüber man gar nichts sagen kann, wenn man vor der eben charakterisierten Kluft zwischen Idealismus und Realismus steht, das ist die Frage: Wie kommt es, daß in unserer Weltenordnung manche Menschen ganz jung sterben, schon als Kin­der oder als junge Leute oder im mittleren Lebensalter, andere erst sterben, wenn sie alt geworden sind? Mit was in der Weltenordnung hängt dieses zusammen? - Weder der Idealismus auf der einen Seite , noch der Realismus auf der andern Seite, der die Ideale nicht als reale Mächte ansehen kann, können irgend etwas über solche Fragen, die aber Lebensfragen sind, ausmachen.",
      "Diesen Fragen kann man auch nur dann nahetreten, wenn man etwas ganz Bestimmtes ins Auge faßt. Und das ist, wenn man ins Auge faßt, daß der gegenwärtige Mensch, so wie er einmal als Erdenmensch vor uns steht, verhältnis-mäßig leicht fertig wird mit dem Raume, aber er wird nicht in gleicher Weise fertig mit der Zeit.",
      "In dieser Beziehung bieten die sämtlichen philosophischen Anschauungen, die es bis heute gibt, eigentlich keinen",
      "irgendwie nennenswerten Aufschluß, und die Frage nach dem Wesen der Zeit ist eigentlich bisher nur in engsten menschlichen Kreisen be­handelt worden. Es ist auch nicht so ganz leicht, über die Zeit und ihr Wesen populär zu sprechen, aber vielleicht gelingt es doch, bei Ihnen eine Vorstellung hervorzurufen von dem, was ich eigentlich meine, wenn ich die Zeit in Analogie mit dem Raume einmal zur Erörterung bringe. Ich muß da allerdings Ihre Geduld etwas in Anspruch nehmen, weil scheinbar, aber eben nur scheinbar, die kurze Betrachtung, die ich darüber anstellen will, einen etwas abstrakten Charakter hat.",
      "Wenn Sie einfach ein Stück der Räumlichkeit überschauen, so wis­sen Sie, daß dasjenige, was Sie da überschauen, sich Ihnen offenbart in einem perspektivischen Charakter. Sie müssen mit der Perspektive des Raumes rechnen, wenn Sie ein Stück Raum überschauen. Wenn Sie nun das Stück Raum, das Sie überschauen und dem Sie ganz instinktiv einen perspektivischen Charakter zuschreiben, auf eine Fläche bringen, dann berücksichtigen Sie die Perspektive dabei. Nicht wahr, wenn Sie in eine Allee hineinschauen, so sehen Sie die entfernten Bäume der Allee kleiner und näher aneinandergerückt. Das können Sie in der Perspektive ausdrücken, und Sie können in einer gewissen Weise per­spektivisch auf einer Fläche zum Ausdruck bringen, was Sie im Raume sehen.",
      "Nun ist es klar, daß dasjenige, was Sie im Raume sehen, in der Fläche nebeneinander ist. Im Raume ist es nicht nebeneinander; da sind diese zwei Bäume da vorne (siehe Zeichnung S.164), und zwei Bäume sind weit entfernt. Aber indem Sie den überschaubaren Raum in die Fläche bringen, setzen Sie dasjenige, was hintereinander ist, nebeneinander. Sie haben wiederum instinktiv die Fähigkeit, das, was Sie so male­risch oder zeichnerisch auf einer Fläche sehen, gewissermaßen in das Räumliche umzusetzen. Daß Sie diese Fähigkeit haben, das rührt da­von her, daß der Mensch, so wie er jetzt einmal als Erdenmensch ist, sich von dem Raume als solchem verhältnismäßig stark losgelöst hat.",
      "Nicht in gleicher Weise hat sich der Mensch von der Zeit losgelöst. Und das ist etwas ungeheuer Eingreifendes und Wichtiges, aber etwas leider kaum Bemerktes, kaum von der Wissenschaft Bemerktes. Der Mensch glaubt, wenn er sich in der Zeit entwickelt, die Zeit zu überschauen,",
      "# Bild s. 164",
      "die Zeit zu haben. Aber er hat in Wirklichkeit nicht die reale Zeit. Er hat gar nicht die reale Zeit, sondern das, was Sie als Zeit er­leben, das ist eigentlich im Verhältnis zu der wirklichen Zeit etwas, was man ein Abbild nennen kann. So wie dieses Bild (siehe Zeich­nung) in der Fläche sich zu dem Raume verhält, so verhält sich das , was der gewöhniiche Mensch Zeit nennt, zu der wirklichen Zeit. Der gewöhnliche Mensch erlebt nämlich nicht die wirkliche Zeit, sondern er erlebt ein Abbild der Zeit, er erlebt tatsächlich ein Abbild der Zeit. Und das kann man sich so sehr schwer vorstellen.",
      "Sie können sich zum Beispiel außerordentlich schwer vorstellen, daß dasjenige, was heute wirkt, gar nicht im jetzigen Zeitpunkt vor­handen zu sein braucht, sondern in einem viel früheren Zeitpunkte real ist und im heutigen Zeitpunkte nicht real ist. Sie sehen gleich­sam dasjenige, was in sehr frühem Zeitraume vorhanden ist, perspek­tivisch in Ihre eigene Zeit hereinwirken.",
      "Das, was ich jetzt gesagt habe, hat eine sehr bedeutsame Folge. Das hat nämlich die Folge, daß alles das, was wir Natur nennen, einen ganz andern Charakter trägt als alles dasjenige, was wir als einen gewissen Teil des Menschen selbst betrachten müssen. In der Natur draußen wirkt zum Beispiel auch Ahriman, beziehungsweise es wirken die ahrimanischen Mächte; aber die ahrimanischen Mächte wirken in der Natur draußen niemals gegenwärtig. Wenn Sie die gesamte Natur überschauen, so wirkt schon Ahriman in der Natur, aber er wirkt von",
      "einer entfernten Zeit her. Von der Vergangenheit her wirkt Ahriman. Und ob Sie das mineralische, das pflanzliche, das tierische Reich über­blicken, Sie dürfen niemals sagen, in dem, was gegenwärtig vor Ihren Augen sich ausbreitet, liege etwas, worin Ahriman tätig ist. Und doch ist Ahriman drinnen tätig; aber von der Vergangenheit her. Wenn ich also die Sache zeichnen wollte, so müßte ich sagen: Hier ist die Entwickelungslinie von der Vergangenheit in die Zukunft hin, und hier überblicken Sie die Natur.",
      "# Bild s. 165a",
      "Ja, nun müssen Sie es sich so denken, daß Sie da hineinschauen. In dem, was Sie als Gegenwärtiges überschauen, ist nichts von ahri­manischen Mächten enthalten, aber aus der Vergangenheit, aus einer bestimmten Vergangenheit wirkt Ahriman herüber in die Natur.",
      "# Bild s. 165b",
      "Und Ihnen erscheint Ahriman in der Natur, wenn Sie ihn da gewahr werden, perspektivisch. Würden Sie sagen: Ahriman wirkt gegen­wärtig - dann begehen Sie der Natur gegenüber denselben Fehler, wie wenn Sie sagen würden: Überschaue ich einen Raum, so stehen die entfernten Bäume, weil sie sich perspektivisch in die Fläche hinein­stellen lassen, so neben den nahen Bäumen (siehe Zeichnung Seite 164).",
      "Eine Grundforderung für ein reales Schauen in der geistigen Welt ist dieses, daß man zeitlich perspektivisch sehen lernt, daß man lernt, zeitlich jegliches Wesen an seinen richtigen Zeitpunkt zu setzen.",
      "Wenn ich nun gestern gesagt habe: Das Ich wird nach dem Tode gewissermaßen aus dem flüssigen Zustand heraus in eine Art festen",
      "Zustandes versetzt -, so ist das noch nicht alles, sondern es kommt noch das andere dazu. Nehmen Sie an, Sie lebten hier auf der Erde mit Ihrem Ich vom Jahre 1850 bis zum Jahre 1920, und im Jahre 1920 werden Sie Ihr Ich gewahr. Ich meine also: Wohl werden Sie es schon früher gewahr, aber nun blicken Sie zurück, mit dem Geistselbst durch die Hierarchien blicken Sie auf Ihr Ich zurück; da sehen Sie Ihr Ich immer als stehengeblieben vom Jahre 1850 bis 1920. Das Ich bleibt da, bleibt stehen. Das heißt: Ihre Erlebnisse gehen bald nach Ihrem Tode nicht mit Ihnen, sondern Sie sehen auf sie zurück, Sie schauen nun von einer zeitlich entfernten Perspektive auf das zurück, und Sie sehen in die Zeitenlänge hinein, wie Sie hier in der physischen Welt in die Raumeslänge hineinsehen. Ich kann es auch so ausdrücken: Indem Sie, sagen wir, 1920 sterben, leben Sie mit alidem, was ich Ihnen ge­stern als die Glieder Ihres Wesens geschildert habe, dann weiter; aber Sie sehen zurück auf die Zeitstrecke, in der Sie hier auf Erden mit Ihrem Ich gelebt haben. Und diese Zeitstrecke bleibt dort, und Sie sehen sie immer, indem Sie perspektivisch weiterleben, an der Zeitstelle, wo sie war. Und so müssen Sie sich vorstellen, daß Ahriman wirksam ist draußen in der Natur, aber von einer früheren Zeitstelle aus.",
      "Das ist sehr wichtig. Das ist etwas, was sehr wenig berücksichtigt wird. Wenn man die Welt verstehen will, wenn man geisteswissen­schaftlich von der Zeit sprechen will, so muß man durchaus die Zeit raumähnlich vorstellen und muß dieses Verbundenbleiben des Wesen-haften mit der Zeit ins Auge fassen. Das ist sehr wichtig.",
      "Nun ist das, was ich Ihnen mit Bezug auf die ahrimanischen Mächte gesagt habe, daß sie von der Vergangenheit her wirken, für die Natur so richtig. Aber beim Menschen wird es gerade anders. Beim Men­schen wird es eben, während er hier zwischen Geburt und Tod lebt, dadurch anders, daß für ihn alles in der Zeit Ablaufende eben zur Maja, zur Täuschung wird. Der Mensch lebt, während er hier lebt, selber im Laufe der Zeit drinnen, und indem er eine gewisse Anzahl von Jahren durchlebt, durchlebt er den Zeiteniauf mit. Indem die Zeit abläuft, läuft er selber mit der Zeit ab. Das ist mit dem Raume nicht der Fall. Wenn Sie eine Allee entlanggehen, bleiben die Bäume zurück",
      "und Sie schreiten vorwärts, und Sie nehmen die Bäume, die zurück­geblleben sind, also auch Ihre Eindrücke, nicht so mit, daß Sie, indem Sie einen Schritt machen würden, die Meinung hätten, es ginge das Baumbild mit Ihnen mit. Mit dem Zeitbilde machen Sie das. Hier im physischen Leibe machen Sie das tatsächlich so - weil Sie selbst in der Zeit sich weiterentwickeln -, daß Sie sich über die Zeit in bezug auf ihre Perspektive einer Täuschung hingeben. Sie merken die Perspek­tive der Zeit nicht. Und insbesondere merkt es nicht das Unterbewußt-sein des Menschen. Das Unterbewußtsein des Menschen merkt erst recht dieses Mitleben mit der Zeit nicht, gibt sich einer vollständigen Täuschung mit Bezug auf die Perspektive der Zeit hin. Das aber hat eine ganz bestimmte Folge. Das hat die Folge, daß nun in demjenigen, was im Menschen geschieht, ahrimanische Mächte als gegenwärtige Mächte wirken können. Ins menschliche Seelenleben herein wirken ahrimanische Mächte als gegenwärtige Mächte. So daß der Mensch der Natur so gegenübersteht: Indem er in die Natur hinaussieht, ist im Gegenwartigen nichts Ahrimanisches. In ihm wirkt das Ahrimanische als Gegenwärtiges, eben gerade als Maja, als Täuschung. Aber der Mensch ist dieser Täuschung über die Dinge, die ich Ihnen ausein­andergesetzt habe, hingegeben, so daß durch den Menschen die ahri­manischen Mächte die Möglichkeit gewinnen, in die Gegenwart her­einzukriechen, in die Gegenwart hereinzuwandeln. Wir können sagen:",
      "Die ahrimanischen Mächte - und so ist es nun auch mit den luziferi­schen Mächten , wenn auch von einem gewissen andern Gesichts­punkte aus, wovon wir gleich sprechen werden - wirken in der Natur so, daß sie eigentlich mit der Gegenwart nichts zu tun haben, sondern von der Vorzeit herein ihre Wirkungen erstrecken. Im Menschen wir­ken diese ahrimanischen Mächte gegenwärtig.",
      "Was ist die Folge? Die Folge davon ist, daß der Mensch in seinem tiefsten Seelischen in bezug auf den eben auseinandergesetzten Punkt sich nicht verwandt mit der Natur fühlen kann. Er sieht auf sein Wesen, beziehungsweise fühlt sich in seinem Wesen, empfindet das naturgemäße Wesen. Weil in ihm ahrimanische Mächte Gegenwarts-mächte sind, in der Natur ahrimanische Mächte Vergangenheits-mächte sind, erscheint ihm alles dasjenige, was naturgemäß ist, anders",
      "als dasjenige, was sich in ihm selbst entwickelt. Den Unterschied, den der Mensch zwischen sich und der Natur merkt, den enträtselt er sich nicht in der richtigen Weise. Würde er sich ihn in der richtigen Weise enträtseln, so wäre es so, wie ich es eben auseinandergesetzt habe. Er würde sagen: Draußen in der Natur wirkt Ahriman von der Ver­gangenheit aus; in mir wirkt Ahriman als eine gegenwärtige Macht. -Dadurch aber kommt es, wenn er auch den Unterschied nicht weiß , daß er sich im Sinne dieses Unterschiedes verhält, und die Natur als geistlos empfindet. Er empfindet es schon, daß in der Gegenwart die ahrimanischen Mächte nicht in der Natur unmittelbar wirksam sind , aber er empfindet die Natur als geistlos, weil er sich nicht sagt: Ahri-man wirkt von der Vergangenheit her -, sondern er sieht nur auf die gegenwärtige Natur. Darinnen wirkt nicht Ahriman.",
      "Nun ist aber Ahriman, so sonderbar das klingen mag, diejenige Macht, deren sich die allgemeine Weltenschöpfung bedient, um die Natur hervorzubringen. Wenn man von dem Geist der Natur spricht, wenn man vom reinen Geist der Natur spricht, müßte man eigentlich von dem ahrimanischen Geiste sprechen. Da ist er vollberechtigt, der ahrimanische Geist. Die Wesenheiten der normalen Hierarchien, die bedienen sich des ahrimanischen Geistes, um das hervorzubringen, was sich als Natur um uns herum ausbreitet. Daß wir die Natur nicht durchgeistigt empfinden, das rührt eben davon her, daß im gegen­wärtigen Leben der Natur der Geist nicht enthalten ist, sondern daß er von der Vergangenheit her wirkt. Und das ist das Geheimnis , möchte ich sagen, der weitschöpferischen Mächte, daß sie sich eines Geistes, den sie stehengelassen haben auf einer früheren Stufe, bedie­nen zur Wirkung auf einer späteren Stufe, aber ihn von der Vergangen­heit herein wirken lassen.",
      "Wir müßten, wenn wir von der Natur sprechen, nicht von Stoff sprechen, auch nicht von Kräften sprechen, wir müßten von ahrima­nischen Wesenheiten sprechen; aber wir müßten dann so sprechen, daß wir diese ahrimanischen Wesenheiten in die Vergangenheit setzten. So daß das Sonderbare herauskommt: Nehmen Sie an, irgendein Naturphilosoph sinnt, sinnt nach, was hinter den Erscheinungen der Natur ist. Nun, da macht er sich allerlei Theorien und Hypothesen",
      "über Atomausammenhänge und dergleichen. So ist aber die Sache nicht. Hinter dem, was sich da sinnenfällig um uns herum ausbreitet, ist eigentlich nicht das, was die Naturphilosophen gewöhnlich ver­muten, sondern hinter alldem ist die Summe der ahrimanischen Mächte, aber nicht als gegenwärtige.",
      "Ist also der Naturphilosoph ge­nötigt, sagen wir, hinter den chemischen Elementen irgendwelche Atomstrukturen zu vermuten, so ist das falsch; hinter den chemischen Elementen stehen ahrimanische Mächte. Aber wenn Sie das, was Sie sehen, von den chemischen Elementen abheben könnten und dahin­terschauen, so würden Sie in der Gegenwart nichts dahinter sehen: da wäre es hohl, wo man die Atome sucht, und das, was wirkt, wirkt in diesen Hohlraum aus der Vergangenheit herein.",
      "So ist es in Wirklich­keit. Daher diese vielen verunglückten Theorien über dasjenige, was das «Ding an sich» ist; denn dieses «Ding an sich» ist in der Gegen­wart überhaupt nicht da. Sondern es ist an der Stelle, wo das «Ding an sich» gesucht wird, nichts; aber die Wirkung ist dort aus der Ver­gangenheit herein.",
      "So daß man sagen könnte, wenn Kant sein «Ding an sich» gesucht hat, so hätte er sagen müssen: Da, wo ich an das «Ding an sich» heran will, da kann ich nicht heran. - Das hat er ja auch gesagt. Aber er ist nicht darauf gekommen, daß er da überhaupt zunächst gegenwärtig nichts gefunden hätte, und daß er, wenn er hinter den Schleier der Dinge gegangen wäre, hätte weit zurück­gehen müssen; dann hätte er ahrimanische Mächte gefunden.",
      "Im Menschen selbst ist es anders. Gerade dadurch, daß der Mensch lebendig in die Zeit versetzt wird, dadurch ist es den ahrimanischen Mächten möglich gewesen, durch die Pforte der Menschheit in unsere Welt einzudringen und innerhalb des Menschen als solchem zu wirken. Und die Folge davon, daß die ahrimanischen Mächte im Menschen wirken, ist die, daß der Mensch loslöst dasjenige, was er in der Gegen­wart sieht, von dem Geistigen, daß der Mensch sein Gegenwarts-dasein löst von dem Geistigen. Das ist die Folge dessen, daß wir die ahrimanischen Mächte innerhalb der Maja in uns tragen. So daß man sagen kann: So wie wir die Welt materiell ansehen, losgelöst vom Geiste, als bloße Naturordnung, die ihren Gipfel zu finden glaubt in dem Gesetz der Erhaltung der Kraft und des Stoffes - was eine Illusion",
      "ist -, was wir da als eine Naturordnung sehen, es ist lediglich durch den Umstand herbeigeführt, daß wir die ahrimanischen Mächte in uns tragen, und daß sie in der Natur draußen als gegenwärtige Mächte nicht sind. - Es stimmt deshalb dasjenige, was wir über die Natur denken, indem wir sie bloß materiell denken, nicht mit der Natur überein, stimmt nur mit der gegenwärtigen Natur überein. Aber diese gegenwärtige Natur ist eben ein Abstraktum, weil in ihr der vergangene Ahriman immer hereinwirkt.",
      "Nun wirkt in den Menschen nicht nur das Ahrimanische, sondern auch das Luziferische herein. Dieses Luziferische aber, das hat ge­wissermaßen eine andere Tendenz im Weltenall als das Ahrimanische. Vergegenwärtigen wir uns die Tendenz des Ahrunanischen, so wie wir die Sache jetzt ausgesprochen haben.",
      "Die Tendenz des Ahrimani­schen in uns besteht darin, die Welt materialistisch vorzustellen. Daß wir die Welt materialistisch vorstellen, daß wir uns eine bloße Natur-ordnung denken, ist die Folge davon, daß wir Ahrimanisches in uns tragen.",
      "Daß wir Ideale in uns tragen, welche sich loslösen von der allgemeinen Natur, nach denen wir uns in unserem gegenseitigen Ver­halten richten wollen, die uns aber doch nur wie Träume erscheinen müssen innerhalb der gegewärtigen Weltanschauung, die ausgeträumt sind, wenn nach der Naturordnung die Erde an ihrem Endzustand angekommen ist, das ist die Folge davon, daß die luziferischen Mächte , die ebenso wie die ahrimanischen in uns leben, immerfort das Be-streben haben, den Teil von uns, der ihnen zugänglich ist, ganz aus der Naturordnung herauszureißen und vollständig zu vergeistigen. Die luziferischen Mächte haben nämlich zu ihrer Haupttendenz, insofern sie in uns wohnen, uns so geistig wie möglich zu machen, uns wo­möglich loszureißen von allem materiellen Leben.",
      "Daher gaukeln sie uns solche Ideale vor, die keine Naturmächte sind, sondern die macht-los sind in der gegenwärtigen Naturordnung. Und verfiele der Mensch ganz und gar im Laufe der zukünftigen Erdenperiode dem luziferi­schen Einfluß, so daß er glauben würde, Ideale seien eben nur ge­dachte Dinge, nach denen sich das Gemüt richten kann, so würde dieser Mensch den luziferischen Mächten folgen.",
      "Die materielle Erde, zu der wir gehören, würde verfallen, zerstieben im Weltenall, würde",
      "ihren Zweck nicht erfüllen, und die luziferischen Mächte würden den Menschen in eine andere geistige Welt führen, in die er nicht gehört. Dazu brauchen sie den Ktiff, uns Ideale vorzugaukeln, die eigentlich bloße Träume sind. Wie uns Ahriman nach der einen Seite eine Welt vormacht, welche eine bloße Naturordnung ist, so macht uns Luzifer auf der andern Seite eine Welt vor, die rein nur in gedachten Idealen besteht.",
      "Das ist etwas sehr Bedeutungsvolles. Und gegenwärtig wird nur ein Ausgleich, möchte ich sagen, in den Gebieten herbeigeführt, die noch im menschlichen Unbewußten liegen. Aber die Menschen müs­sen sich dieser Sache immer mehr und mehr bewußt werden, sonst kommen sie aus diesem Dilemma nicht heraus, kommen nicht dazu, eine Brücke zwischen dem Idealismus und dem Realismus zu bauen, welche Brücke aber notwendig ist.",
      "Dasjenige, was gegenwärtig noch eine Art Ausgleich schafft, das ist das Folgende. Wenn gegenwärtig ganz junge Menschen sterben, zum Beispiel Kinder, so haben diese Kinder - bei jungen Menschen ist es ebenso - eben in die Welt hereingeschaut; sie haben nicht voll das Dasein hier auf dem physischen Plane ausgelebt. Mit einem auf dem physischen Plane unausgelebten Leben kommen sie hinüber in die andere Welt, die zwischen dem Tode und einer neuen Geburt verlebt wird, so verlebt wird, wie ich es gestern geschildert habe. Dadurch, daß sie einen Teil nur des Erdenlebens gelebt haben, bringen sie etwas vom Erdenleben mit hinüber in die geistige Welt, das man nicht hin­überbringen kann, wenn man alt geworden ist. Man kommt anders in der geistigen Welt an, wenn man alt geworden ist, als wenn man jung stirbt. Wenn man jung stirbt, so hat man das Leben so durchlebt, daß man noch viele Kräfte in sich hat vom vorgeburtlichen Leben. Man hat als Kind und als junger Mensch das leibliche Leben so durchlebt, daß man darinnen noch viel von den Kräften in sich hat, die man vor der Geburt in der geistigen Welt hatte. Dadurch hat man eine innige Verbindung geschaffen zwischen dem Geistigen, das man mitge­bracht hat, und dem Physischen, das man hier erlebt hat. Und durch diese innige Verbindung kann man etwas, was man auf der Erde er­wirbt, in die geistige Welt mit hinübernehmen. Kinder oder sonst",
      "jung gestorbene Leute, nehmen von dem Erdenleben etwas in die geistige Welt mit hinüber, was gar nicht mit hinübergenommen wer­den kann, wenn man als älterer Mensch stirbt. Das, was da mitgenom­men wird, ist dann drüben in der geistigen Welt, und was da hinüber-getragen wird durch Kinder und junge Leute, das gibt der geistigen Welt eine gewisse Schwere, die sie sonst nicht haben würde, der­jenigen geistigen Welt, in der dann die Menschen gemeinsam drinnen leben, das gibt eine gewisse Schwere der geistigen Welt und verhindert die luziferischen Mächte, die geistige Welt ganz loszutrennen von der physischen.",
      "Also denken Sie, auf welches riesige Geheimnis wir da blicken! Wenn Kinder und junge Leute sterben, so nehmen sie von hier etwas mit, wodurch sie die luziferischen Mächte verhindern an deren Be­streben, uns ganz loszulösen von dem Erdenleben. Das ist außer­ordentlich wichtig, daß man dies ins Auge faßt.",
      "Wird man älter hier auf der Erde, so kann man in der geschilderten Weise den luziferischen Mächten die Rechnung noch nicht verderben; denn von einem gewissen Alter an hat man nicht mehr jene innige Verbindung zwischen dem, was man mitgebracht hat bei der Geburt und dem physischen Erdenleben. Ist man alt geworden, so löst sich diese innerliche Verbindung, und es tritt gerade das Umgekehrte ein. Von einem gewissen Lebensalter an träufeln wir in einer gewissen Weise dem innerhalb der physischen Erde befindlichen Geistigen un­ser eigenes Wesen ein. Wir machen die physische Erde geistiger als sie sonst wäre. Also von einem bestimmten Alter an vergeistigen wir in einer gewissen Weise, die man nicht mit äußeren Sinnen wahrnehmen kann, die physische Erde. Wir tragen Geistiges in die physische Erde hinein, wie wir Physisches in die geistige Welt hinauftragen, wenn wir jung sterben; wir pressen gewissermaßen Geistiges aus, wenn wir alt werden, ich kann es nicht anders sagen. Das Altwerden besteht im geistigen Sinne von einem gewissen Aspekt aus darinnen, daß man Geistiges hier auf der Erde auspreßt. Dadurch wird wiederum die Rechnung des Ahriman verhindert. Dadurch kann Ahriman nicht auf die Dauer heute schon so intensiv auf die Menschen wirken, daß völlig erlöschen könnte die Meinung, Ideale hätten doch eine gewisse Bedeutung.",
      "Aber wir sind im heutigen Zeitraume schon sehr, sehr nahe daran, daß die Menschen in die furchtbarsten Irrtümer gerade mit Be­zug auf das Gesagte verfallen. Auch Gutmeinende verfallen leicht in bezug auf das Gesagte in solche Irrtümer. Und diese Irrtümer werden immer größer und größer werden und mit zunehmender Erdenent­wickelung eben riesig werden können.",
      "Um Ihnen ein Beispiel anzuführen: Ein recht geistvoller Philosoph hat 1882 eine «Anthroposophie» geschrieben, Robert Zimmermann. Ich habe das schon einmal in einem Zusammenhange erwähnt. Diese «Anthroposophie» ist nicht dasjenige, was wir Anthroposophie jetzt nennen, sie ist mehr oder weniger ein Begriffsgestrüpp.",
      "Aber das ist ja aus dem Grunde, weil eben Robert Zimmermann nicht in die geistige Welt hineinsehen konnte, sondern nur Herbartianischer Philosoph war. Nun hat er diese «Anthroposophie» geschrieben. Aber gerade in dieser «Anthroposophie» beschäftigt sich Robert Zimmermann von seinem Gesichtspunkte aus mit der Frage, die ich in diesen Tagen an die Spitze unserer Betrachtungen gestellt habe.",
      "Er sieht auf der einen Seite die Ideen, logische Ideen, ästhetische Ideen, ethische Ideen; er sieht auf der andern Seite die Naturordnung. Und er kann nicht irgend­wie eine Brücke finden zwischen den logischen, den ästhetischen, den ethischen Ideen und der Naturordnung, sondern er bleibt doch dabei stehen: Da ist auf der einen Seite die Naturordnung, und auf der an­dern Seite sind die Ideen.",
      "Und wozu er zuletzt kommt, das ist doch außerordentlich interessant, denn es ist eigentlich typisch für einen Menschen der Gegenwart. Er kommt dahin, zu sagen, es sei ein für allemal dem Menschen versagt, die Natur mit Ideen zu bevölkern und den Ideen Naturgewalt beizulegen.",
      "Die beiden Welten seien eigent­lich nur im Kopfe des Menschen miteinander zu verbinden. So sagt er. Und daher meint er an einer Stelle, wo er geradezu alles zusammen­faßt, was er sagt und was er denkt: «Die Verwirklichung der Ideen ist weder eine Tatsache, die in der Vergangenheit, noch eine solche, die in der Gegenwart, sondern eine Aufgabe, deren Erfüllung in der Zukunft und in den Händen des Menschen liegt.",
      "Der Traum eines ,goldenen Zeitalters', von welchem ein nüchterner Rationalist wie Kant als von jenem des ,ewigen Friedens', ein extremer Positivist wie",
      "Comte als dem ,état positif' schwärmte, wird dann erfüllt sein , wenn die gesamte Ideenwelt real geworden und die gesamte Wirklichkeit von den Ideen durchdrungen, d.h. wenn dasjenige, was Schiller ,das Kunstgeheimnis des Meisters' nannte, die ,Vertilgung des Stoffes durch die Form' offenbar, wie Schleiermacher es ausdrückte ,wenn die Ethik Physik und die Physik Ethik' geworden sein wird.»",
      "Ja, aber das kann nie werden! Es kann nur das werden, daß die Menschen in ihrer sozialen Ordnung die Ideen realisieren. Wenn aber die Erde einmal an ihrem Ende angelangt sein wird, so wird der ganze Ideentraum ausgeträumt sein. Ein anderes ist nach einer solchen Philosophie nicht möglich. Daher bleibt eine solche Philosophie im­mer abstrakt und muß zuletzt gestehen: «Eine Philosophie, welche, wie die vorstehende, sich weder wie die Theosophie auf einen mensch­lichem Wissen unzugänglichen theozentrischen Standpunkt versetzt , um von ihm aus den ,Vernunfttraum' als längst geschaffene Wirklich­keit, noch wie die Anthropologie auf den zwar anthropozentrischen aber unkritischen Standpunkt gemeiner Erfahrung stellt, um von ihm aus eine ideenerfülite Wirklichkeit als ,Traum der Vernunft' an­zusehen, welche sonach zugleich anthropozentrisch d. i. von mensch­licher Erfahrung ausgehend und doch Philosophie d. i. an der Hand des logischen Denkens über dieselbe hinausgehend sein will ist An­throposophie.» «Anthroposophie» ist also hier das Eingeständnis, daß man niemals über diese Kluft hinüberkommen könne zwischen un­realen Ideen und ideenloser Realität.",
      "Nun ist aber im Menschen selbst ein Naturwesen, das also der Na­turordnung angehört, verbunden mit einem Geistwesen, das in sich aufnehmen kann das Geistige. Das leugnet ja auch nicht ein solcher Anthroposoph wie Robert Zimmermann. Aber von der gegenwär­tigen Wissenschaft kann auch der Mensch nicht so betrachtet werden, daß sich durch den Menschen, durch diesen Mikrokosmos, das Rätsel lösen würde.",
      "Blicken wir jetzt zurück auf etwas, was wir auch schon während des diesmaligen Aufenthaltes erwähnt haben. Wir haben gesagt, daß wir eigentlich den Menschen gliedern müssen in drei Teile, natürlich nicht so bequem, wie es am Skelett ist. das habe ich schon ausgeführt.",
      "Aber ich habe mich ja darüber auch ausgesprochen in den Schluß­notizen zu meinem Buche «Von Seelenrätseln». Wir können den Menschen gliedern in drei Teile: den Hauptesmenschen, den Rumpf-menschen und den Extrerritätenrnenschen' indem zum Extremitäten-menschen alles dasjenige gehört, was inwärts der Extremitäten ge­legen ist, also auch alles Sexuelle zum Extremitäteumenschen gehört.",
      "Wenn wir den Menschen so gliedern und jetzt anwenden dasjenige, was wir schon wissen: daß die Kopf bildung, die Kopfform auf Kräfte hinweist der vorigen Inkarnation, der Extremitätenmensch hinweist auf die zukünftige Inkarnation und eigentlich nur der Rumpfmensch der Gegenwart angehört, so werden Sie nach dem, was ich heute aus­geführt habe, es nicht mehr sehr unbegreiffich finden, wenn ich Ihnen sage: Insofern der Mensch sein Haupt trägt, weist dieses Haupt auf die frühere Inkarnation zurück, in die Vergangenheit. Ins Haupt herein wirken Kräfte der Vergangenheit, ahrimanische Kräfte, und dasjenige, was für die ahrimanischen Kräfte im allgemeinen gilt, gilt für das menschliche Haupt im besonderen.",
      "Alles, was eigentliche Hauptes-bildung im Menschen ist, gehört nicht eigentlich der Gegenwart an, sondern in das Haupt wirken hinein die Kräfte der vorgehenden In-karnation; und die schöpferischen Mächte bedienen sich der ahri­manischen Mächte, um unser Haupt zu formen, um unserem Haupte die eigentliche Formung zu geben. Würden nicht die schöpferischen Mächte sich der ahrimanischen Geister bedienen, um unser Haupt zu formen, dann würden wir alle - verzeihen Sie, aber es ist so - zwar ein viel weicheres Haupt tragen, aber wir würden alle ein tierisches Haupt tragen: der eine, welcher in seinem Charakter stiermäßig ist, würde ein Stierhaupt, der andere, der in seinem Charakter lammäßig ist, würde ein Lämmerhaupt tragen und so weiter.",
      "Von dem Einfluß der ahrimanischen Mächte, deren sich die schöpferischen Gewalten be-dienen, um uns zu formen, rührt es her, daß dieses tierische Haupt, das wir sonst tragen würden, nicht wirklich uns aufsitzt, so wie es die Ägypter gezeichnet haben an manchen ihrer Figuren; daß wir nicht so herumgehen wie diese ägyptischen Gestalten, die ihre guten Gründe haben, weil in den ägyptischen Mysterien auch, wenn auch von einem atavistischen Standpunkte aus, solche Dinge gelehrt worden sind, wie",
      "sie jetzt wieder gelehrt werden können; daß wir auch nicht so noch herumgehen wie in den Rosenkreuzerbildern etwa, wo jede Frau mit einem Löwenkopf, jeder Mann mit einem Ochsenkopf gemalt wird. So ist ja das Rosenkreuzergemalde des Menschen. Die Rosenkreuzer haben mehr ein Durchschnitts-Tier gewählt und haben daher das , was für die Frauen am meisten ähnlich ist, den Löwenkopf, den Frauen aufgesetzt, und dem Manne, was ihm am meisten ähnlich ist, den Ochsenkopf, den Stierkopf. Sie sehen daher auf rosenkreuzerischen Figuren Mann und Frau nebeneinandergestellt: die Frau mit dem schönsten Löwenkopf, den Mann mit einem Stierkopfe. Dies ist aber durchaus richtig. Daß die Metamorphose - jetzt goethisch gespro­chen - sich vollziehen kann, daß unser in seiner Form nach der Tier­heit tendierendes Haupt so gestaltet wird, daß es Menschenhaupt ist, rührt von dem Einfluß der ahrimanischen Mächte her. Würden sich nicht die Gottheiten Ahrimans bedienen, um unser knöchernes Haupt zu formen, dann würden wir mit Tierhäuptern herumgehen.",
      "Aber die göttlichen Mächte bedienen sich auch der luziferischen Geister. Würden sie sich dieser luziferischen Geister nicht bedienen , so würde wiederum unser Extremitätenmensch von der jetzigen zu der nächsten Inkarnation sich nicht umwandeln können. Dazu sind die luziferischen Wesenheiten notwendig. Den luziferischen Wesen­heiten verdanken wir es wiederum, daß, indem wir sterben, umge­wandelt wird nach und nach die Form, die jetzt noch der Extremi­tätenmensch hat, in die weitere Form, die sie in der nächsten Inkar­nation haben soll. Da muß dann in der Mitte des Weges zwischen dem Tod und einer neuen Geburt Ahriman eintreten, um die andere Auf­gabe zu übernehmen: um das Haupt wiederum in der entsprechenden Weise umzuformen. Wie wir mit Tierhäuptern herumgehen würden , wenn wir es Ahriman nicht zu verdanken hätten, daß wir einen Men­schenkopf bekommen, so würde unsere Extremitätennatur sich nicht ins Menschliche metamorphosieren bis zur nächsten Inkarnation, sondern sie würde ins Dämonische übergehen. Unseren Kopf, wie wir ihn jetzt haben, verlieren wir ja unter allen Umständen durch den Tod, nicht nur als Materie, die sich mit der Erde vereinigt, sondern auch als Form; in die nächste Inkarnation tragen wir ja das, was Kopf",
      "wird, vom Extremitätenmenschen hinüber. Aber das würde ein dä­monisches Wesen werden, wenn wir es nicht den luziferischen Mäch­ten, die mit uns verbunden sind, zu verdanken hätten, daß die Umge­staltung stattfinden könne vom Dämon, der ein bloß Geistig-Seeli­sches wäre, in die Menschengestalt der nächsten Inkarnation.",
      "So müssen bei unserem Menschenwerden ahrimanische und luzi­ferische Mächte mitwirken, und es kann das Menschliche nlcht be­griffen werden, ohne daß das Ahrimanische und das Luziferische zu Hilfe gerufen wird. Der Menschheit kann es gegen die Zukunft hin nicht erspart werden, die Wirksamkeit Ahrimans und Luzifers wirk­lich zu verstehen. Mit vollem Rechte sagt die Bibel, daß jene Gottheit, von der im Anfange der Bibel die Rede ist, dem Menschen den le­bendigen Odem einhauchte. Aber der lebendige Odem wirkt im Rumpfmenschen. Insofern wir es also zu tun haben mit den normal wirkenden göttlichen Wesenheiten, haben wir es nur mit dem Rumpf-menschen zu tun. Insofern wir es mit dem Kopfmenschen zu tun haben, haben wir es mit einem Gegner der Jahvemächte zu tun, da­durch auch mit einem Gegner des Christus. Und auch insofern wir es mit dem Extremitätenmenschen zu tun haben, haben wir es mit dem luziferischen Gegner zu tun.",
      "Daher wird man den Menschen nur verstehen, wenn man ihn unter diesen drei Aspekten vorstellt. Sie haben daher in unserer Mittel­punktsgruppe für unseren Bau eben diese Trinität: den Menschheits­repräsentanten, der aber so ausgebildet ist, daß in ihm vorzugsweise die Kräfte der Atmung, des Rumpfes wirken, die Herztätigkeit und so weiter - das ist die mittlere Figur -, dann diejenige Figur, in der alles Hauptmäßige, Kopfmäßige wirkt: Ahriman; diejenige Figur, in der alles Extremitätenmäßige wirkt: Luzifer.",
      "Man muß das Menschliche in dieser Weise auseinandernehmen, wenn man den Menschen verstehen will, denn im Menschen ist der Mensch als solcher mit Ahriman und Luzifer vereint. Das ist gleich­zeitig wohl darauf hinweisend, daß alles, was mehr oder weniger mit dem menschlichen Denken zusammenhängt, welches ja in bezug auf seinen physischen Zusammenhang an den Kopf gebunden ist - das menschliche Denken verffießt auf Grund der Wahrnehmungen als",
      "eines Äußerlich-Sinnenfälligen -, daß alles das einen ahrimanischen Charakter hat. Durch die Sinne des Kopfes nehmen wir ja vorzugs­weise die Natur wahr, und wir bauen uns ein Naturhild auf mit dem eben vorhin geschilderten ahrimanischen Charakter, weil wir selbst das Ahrimanische in der Bildung, in der Formung unseres Kopfes an uns tragen.",
      "Die Ideale wiederum haben innerlich, psychologisch- darauf komme ich dann in der nächsten Zeit noch zurück -, sehr viel mit der Liebe zu tun, mit alidem, was dem Extremitätenmenschen angehört. Daher hat zu den Idealen die luziferische Macht den besonderen Zutritt. Durch unser Haupt faßt uns Ahriman, durch unsere Extremitäten faßt uns Luzifer. Durch unser Haupt verführt uns Ahriman dazu, die Natur geistlos vorzustellen; durch unseren Extremitätenrnenschen verführt uns Luzifer dazu, die Ideale ohne Naturgewalt vorzustellen.",
      "Das aber ist die Aufgabe des gegenwärtigen Menschen, dadurch, daß er solches überschaut, zu einer richtigen Übersicht zu kommen. Denn sehen Sie: In uns ist eine gewisse Grenzscheide, gerade in un­serem Brustmenschen, in unserem Rumpfmenschen, wodurch die Gewalten des Hauptes, welche ahrimanische Gewalten sind, abgetrennt werden von den luziferischen Gewalten, die dem Extremitätenmen­schen angehören. Würden wir , in dem wir mystisch in uns hinein­schauen, uns ganz durchschauen können, dann würden wir zwar durch das Haupt die Naturordnung begreifen, aber wir würden auch durch die Naturordnung in uns selbst hineinschauen. Und würden in uns die luziferischen Mächte entscheiden, dann würden die luziferischen Mächte uns auch über die ahrimanischen Mächte aufklären, und wir würden auf diese Weise zu einer Verbindung zwischen Naturordnung und Geistordnung kommen. Aber das können wir aus einem gewissen Grunde nicht, und zwar aus dem Grunde, weil wir ein Gedächtnis haben. Dasjenige, was wir aus der Natur aufnehmen an Vorstellungen und Begriffen, an Eindrücken, das speichern wir in unserem Ge­dächtnisse auf. Und wenn das da hier (siehe Zeichnung Seite 179) -schematisch nur gezeichnet - der Hauptesmensch, das der Brust- und Rumpfmensch, das der Extremitätenmensch ist, so ist im Rumpf-menschen die Scheidewand, die dazu führt, daß dasjenige, was wir",
      "# Bild s. 179",
      "durch das Haupt aufnehmen an Naturordnung, uns wiederum als Gedächtnisstoff zurückkommt. Dadurch sehen wir nicht bis zum Luziferischen hinunter, und dadurch bemerken wir das Ahrimanische nicht, wie wir das nicht sehen, was vor einem Spiegel ist, sondern das­jenige, was sich spiegelt. Hier spiegelt sich die Naturordnung in dem, was zu gleicher Zeit unser Ahrimanisches von unserem Luziferischen abtrennt, und was die Grundlage ist für das sich bildende Gedächtnis, für die sich bildende Erinnerungskraft. Wenn wir uns nicht an die er­lebten Dinge erinnern könnten, wenn diese Scheidewand nicht da wäre, wenn wir uns, in uns blickend, durchschauen würden, so würden wir bis zum Luziferischen hinunterblicken in uns. Dann würden wir auch das Ahrimanische wahrnehmen.",
      "Aber jetzt bedenken Sie: Dasjenige gerade, was uns durch diesen Spiegel erscheint, das ist ja dasjenige, was wir im Lebenslauf durch-leben, das ist, worauf wir nach dem Tode zurückblicken, das ist, was aus einem flüssigen Ich zu einem festen Ich wird. Darauf blicken wir zurück. Das ist dasjenige, womit wir leben. Und Ahriman und Luzifer wirken mit uns, wirken mit uns so, daß Ahriman uns dahin bringt, ein Menschenhaupt zu tragen, Luzifer uns dahin bringt, nicht zum Dämon",
      "zu werden, sondern die Möglichkeit zu haben, zu einer nächsten In­karnation zu kommen.",
      "Ich habe Ihre Geduld etwas in Anspruch genommen mit Dingen, die ja vielleicht etwas schwieriger verständlich sind, allein ich wollte zunächst wenigstens ein Gefühl dafür hervorrufen, wodurch eigent­lich die Kluft entsteht zwischen Idealismus und Realismus. Sie ent­steht dadurch, daß das Luziferische in uns den Idealismus erregt, der machtlos ist in der Natur, daß das Ahrimanische in uns die bloße Na­turordnung hervorruft, welche uns geistlos erscheint.",
      "So stehen eigent­lich die Idealisten, die abstrakten Idealisten unter luziferischem Ein­fluß, die Materialisten unter ahrimanischem Einfluß. Es ist schon not­wendig, daß man auf diese Dinge sich einläßt, daß man nicht bloß sche­matisch die sogenannte Theosophie treibt, sondern auf diese genaue­ren Dinge sich einläßt.",
      "Denn es ist notwendig, daß der Mensch sich bewußt werde, er müsse etwas dazu tun, um mit dem Geiste für den Rest der Erdenentwickelung vereint bleiben zu können. Es ist eine unbequeme Wahrheit, man könnte sagen, sogar auch eine gehaßte Wahrheit, richtig eine gehaßte Wahrheit, denn sie widerspricht ja so vielem, was den Menschen sympathisch ist, aus Bequemlichkeit sym­pathisch ist.",
      "Nichts wird dem Menschen heute schwieriger, als wenn man ihm sagt: Wenn du dir in Zukunft deine Verbindung mit dem Geiste erhalten willst, so mußt du etwas dazu tun. - Es möchten ja die meisten Menschen, daß das Mysterium von Golgatha aus dem Grunde verflossen wäre, damit sie nur ja nichts zu tun haben zu ihrer Angelegenheit, damit sie durch Christus von ihren Sünden erlöst wer­den und ohne ihr Zutun in den Himmel kommen können. Und des­halb werden ja die meisten Theologen so wütend auf die Anthropo­sophie, weil das selbstverständlich von anthroposophischer Seite nie­mals zugegeben werden kann, daß der Mensch nichts zu tun habe, um seine Verbindung mit dem Geiste aufrechtzuerhalten, daß das ganz ohne sein Zutun auch in der Zukunft der Erdenentwickelung vor sich gehen könne.",
      "Die Verbindung zwischen dem Physischen und dem Geistigen, zwischen dem, was die Glieder des Menschen sind zwischen Geburt und Tod, und dem, was die Glieder des Menschen sind zwi­schen Tod und neuer Geburt, diese Verbindung wird in Frage gestellt",
      "durch die zukünftige Erdenentwickelung, und sie wird nur dann nicht in Unordnung kommen, wenn sich die Menschen mit dem Geistigen gegen die Zukunft hin wirklich befassen werden. Dafür gibt es heute schon geisteswissenschaftliche Beweise. Diese geistes-wissenschaftlichen Beweise, sie sind höchst, höchst unbequeme Wahr­heiten, aber sie werfen Licht auf Wichtiges, auf Bedeutungsvolles.",
      "Der Zusammenhang zwischen dem Seelisch-Geistigen und dem Physisch-Ätherischen im Menschen der Gegenwart ist, möchte ich sagen, schon sehr locker geworden, und der Mensch hat es notwen­dig, immer mehr und mehr bei sich Wache zu stehen, damit nicht in dem Zusammenhang zwischen seinem Physisch-Ätherischen und Seelisch-Geistigen etwas geschieht, was ihn gewissermaßen aussaugen könnte, was ihn seelisch-geistig aussaugen könnte. Denn wenn solche Vorurteile immer reger werden, man brauche im Leben nichts zu wissen über die Art, wie es nach dem Tode aussieht, oder wenn die Kluft immer größer wird zwischen sogenanntem Idealismus und rein natürlicher Ordnung, ist die Gefahr, der die Menschen entgegengehen, daß sie immer mehr und mehr ihre Seele verlieren könnten. Heute ist noch, ich möchte sagen, diesem Verlieren der Damm vorgesetzt, der dadurch gegeben ist, daß, wenn junge Leute sterben, der geistigen Welt eine gewisse Schwere verliehen wird und Luzifer die Rechnung verdorben wird, und wenn alte Leute sterben, so viel ausgepreßt wird an Geistigkeit in die physische Welt herein, daß Ahriman die Rech­nung verdorben wird. Aber man darf nicht vergessen, daß dadurch, daß die Menschen sich lossagen vom geistigen Gebiet, die ahrimani­nischen und die luziferischen Mächte immer mächtiger und mächtiger werden, und daß nach und nach, indem die Devolution der Erde im­mer weiter und weiter geht, dieser Damm nicht mehr voll wirken könnte.",
      "Das ist dasjenige, was ich gern möchte, daß es sich als eine Art Bodensatz aus unseren Betrachtungen ergäbe wie ein Gefühl - und Gefühle sind immer das Wichtigste, was aus dem geisteswissenschaft­lichen Leben hervorgehen kann - von der Notwendigkeit, sich vom gegenwärtigen Erdenzyklus ab mit dem Geistigen zu befassen. Von den verschiedensten Gesichtspunkten aus habe ich dieses betont, daß",
      "es von der Gegenwart aus notwendig ist, daß die Menschen sich mit dem Geistigen befassen. Und anders wird man sich nicht mit dem Geistigen befassen können in der Zukunft als dadurch, daß man sich Verständnis erwirbt und sich nicht sträubt, solche auch schwierigere Betrachtungen wirklich in sich aufzunehmen, wie wir sie in diesen Tagen und insbesondere auch heute gepflogen haben. Es muß unter die Menschen kommen das Verständnis von der Perspektivität der Zeit. Wenn dieses Verständnis von der Perspektivität der Zeit unter die Menschen kommt, dann werden sie nicht mehr sagen: Hier ist der Idealismus, der aber nur ein bloßer Traum ist, der keine Naturgewalt hat, und auf der andern Seite liegt die Naturordnung -, sondern die Menschen werden darauf kommen, anzuerkennen, daß, was als Ideale in uns lebt, Keim ist für die Zukunft, und daß, was Naturordnung ist, Frucht ist der Vergangenheit.",
      "Dieser Satz ist eine goldene Regel: Jedes Ideal ist Keim für zu-künftiges Naturgeschehen; jedes Naturgeschehen ist Frucht vergan­genen Geistgeschehens. - Nur durch diese Regel findet man die Brücke zwischen Idealismus und Realismus. Aber dazu ist eines notwendig. Irgendein Ideal könnte nie und nimmermehr Keim für ein zukünftiges Naturgeschehen werden, wenn dieses zukünftige Naturgeschehen durch das gegenwärtige Naturgeschehen verhindert würde. Wir kön­nen uns irgendeine Hypothese vor die Augen führen. Nehmen wir die Möglichkeit an, die heute gilt, daß einmal durch das sogenannte Gesetz der Entropie die Erdenentwickelung in eine Art von allgemeiner Durchwärmung übergehe, und daß alle andern Naturkräfte aufhören , so würde innerhalb dieses Endrustandes natürlich alles Ideale erstor­ben sein. Dieser Endaustand, der folgt ganz gut, wenn man annimmt, daß sich nach reiner Kausalität die gegenwärtigen physikalischen Zu­stände eben weiter fortsetzen werden. Denkt man so, wie die gegen­wärtige Physik denkt, daß nach dem Gesetze der Erhaltung der Kraft und des Stoffes einmal ein solcher Endaustand da sein wird, dann ist in diesem Endzustand kein Platz dafür, daß in ihm einmal ein Ideal als das zukünftige Naturgeschehen aufgehe, denn das zukünftige wird einfach die Folge des gegenwärtigen Naturgeschehens sein. Aber so ist es nicht, so stellt es sich nicht der gegenwärtigen Naturbetrachtung",
      "dar, sondern es stellt sich dieses anders dar. Dasjenige, was heute an Stoffen, an Kräften existiert, alles das wird in einer bestimmten Zu­kunft nicht da sein. Das Gesetz der Erhaltung des Stoffes und der Kraft gibt es nicht. Da, wo man den Stoff sucht, ist überhaupt nichts als ein Hereinwirken eines vergangenen Ahrimanischen, und dasjenige, was uns umgibt im Sinnenfälligen, wird in einer gewissen Zukunft nicht mehr sein da. Und dann, wenn von alledem, was jetzt physisch ist, nichts mehr da ist, wenn das ganz aufgelöst ist, dann ist die Zeit da, wo sich die gegenwärtigen Ideale als Naturgeschehen anreihen werden an das, was jetzt zugrunde gehen wird.",
      "So ist es im großen Weltenall. Und für den einzelnen Menschen ist es so, daß er in der nächsten Welteninkarnation wieder inkarniert wird, wenn partiell alles dasjenige überwunden ist, in das er mit der gegenwartigen Inkarnation hineingewachsen ist, wenn also für ihn eine Umgebung hergestellt werden kann, die anders ist als die gegenwärtige Umgebung, wenn aus der gegenwärtigen Umgebung all das heraus sein kann, was ihn jetzt hier auf der Erde hält. Wenn sich das alles so geändert hat, daß er Neues erleben kann, dann wird er wieder inkar­niert. Die gegenwartigen Ideale, die im Menschen sich bilden können, werden Natur sein , wenn alles dasjenige, was jetzt Natur ist, nicht mehr da sein wird, sondern Neues entstanden sein wird. Aber das Neue, das entsteht, ist eben nichts anderes als das Natur gewordene Geistige.",
      "Hinter den Erscheinungen und hinter den Idealen müssen wir das­jenige suchen, was die Brücke über dem Abgrunde bildet. Aber zu dem muß man eben dahinterkommen. Man kommt heute nur dahinter wenn man sich nicht scheut, die Begriffe so kräftig zu entwickeln, daß sie selbst in die Realität eindringen können. Daher hat die heutige Zeit wirklich die Notwendigkeit, sich gar sehr einzulassen auf alles das­jenige, was geistig erfahren werden kann. Nur - lassen Sie mich das noch anhänglich hinzufügen -, nur wird eben notwendig sein, daß gegenüber geistigen Betrachtungen immer größere und größere Un­befangenheit walten könnte. Vorgestern habe ich zum Schlusse, wie es manchen vielleicht erscheinen könnte, recht unnötig - aber trotz­dem ich es nicht gerne tue, ist es nie unnötig - auf mancherlei hinge­wiesen, was dem gedeihlichen geisteswissenschaftlichen Wirken auch",
      "von seiten der Anthroposophischen Gesellschaft entgegensteht. Da ist vor allen Dingen auf diesem Boden immer wieder und wiederum zu fordern wirkliche Unbefangenheit. Immer wieder und wiederum erleben wir ja, daß das Auflösende, das eigentlich den Materialismus hervorgebracht hat, das die alte Geistigkeit zugrunde gerichtet hat , im menschlichen Denken gerade auch in das Spirituelle, in das ge­wollte Spirituelle hereindringt.",
      "Ich habe ja darauf aufmerksam ge­macht, wie materialistisch manche theosophische Anschauung ist. Man hat es natürlich nicht leicht, wenn man geisteswissenschaftliche Dinge auseinandersetzt, die bezeichnenden Worte zu finden, weil ja unsere Sprache heute nicht mehr für das Geistige geeignet ist, weil wir erst wieder suchen müssen eine solche Verbindung zwischen der Sprache und der Sache, welche für das Geistige geeignet ist.",
      "Aber das ist notwendig, daß nicht immer mit dem, was das Schädlichste ist, die geisteswissenschaftliche Bewegung verdorben wird. Man muß un­befangen charakterisieren dasjenige, was im Geiste vorgeht. Immer wiederum erlebe ich, daß ich gefragt werde: Da ist jemand, dort ist jemand, der hat geistige Erlebnisse. - Der Sinn der Fragen, die häufig so gestellt werden, ist der, daß eigentlich gefragt wird: Darf man nun mit blindem Glauben an die Wahrheit dessen sich hingeben, was der oder jener schaut? - Und wenn man diese Frage bejaht, ja, dann ent­steht blinde Anhängerschaft; wenn man sie verneint, dann entsteht das, daß der Betreffende gleich verketzert wird und gesagt wird: Nun ja, das ist atavistisches Hellsehen, auf das gibt man nichts. - Ja, dieses Entweder-Oder muß doch auf diesem Gebiete ganz anders genommen werden.",
      "Wir müssen uns wirklich mit aller gesunden Vernunft auch den Aussagen über das Geistige gegenüberstellen. Wenn wir aber Dogmatiker werden wollen, können wir nicht Geisteswissenschafter werden. Wenn wir entweder vergöttern oder verketzern wollen, kön­nen wir nicht Geisteswissenschafter werden.",
      "Es werden unendlich wertvolle Beiträge zur Charakteristik der geistigen Welt auch von Seiten kommen, auf die man nicht unbedingt schwören will.",
      "Auch das andere erlebt man, daß eine Zeitlang auf irgendeine sehe­rische Persönlichkeit geschworen wird. Dann kann man nachweisen, daß diese seherische Persönlichkeit irgendwann - nun, vielleicht sogar",
      "einmal ein wenig retuschiert hat, oder stark retuschiert hat; dann ist die Persönlichkeit unten durch. Vorher haben dieselben Leute auf sie geschworen, bei denen sie nachher unten durch ist.",
      "Ja, in dieser Weise kommt man nicht vorwärts; innerhalb der Menschheit mit dem Entweder-Oder der Vergöttlichung oder Ver­ketzerung kommt man nicht vorwärts innerhalb der Menschheit, sondern nur dadurch, daß man sich mit seinem gesunden Menschen­verstand den Dingen gegenüberstellt. Es kann zum Beispiel auch der Fall eintreten, daß durch jemanden, von dem man sogar weiß: Nun, der verschmäht es nicht, ab und zu recht stark zu schwindeln - einmal etwas ganz Wahres, Wichtiges, Wesentliches aus der geistigen Welt herauskommt.",
      "Man würde nicht zu dem Entweder-Oder kommen, das ich hier meine , wenn man nicht Dogmatik einführen wollte, sondern wenn man sich mit dem gesunden Menschenverstand gerade innerhalb dieser anthroposophischen Bewegung hineinstellen wollte. Das ist das eine.",
      "Das andere ist dieses, daß es außerordentlich schwierig ist, durch die Art und Weise, wie die Dinge oftmals innerhalb unseres Kreises ge­handhabt werden, die Anthroposophische Gesellschaft in die Kultur-bewegung der Gegenwart hineinzustellen. Dazu gehört Unterschei­dungsvermögen bei denjenigen Menschen, die schon drinnen sind in dieser Gesellschaft.",
      "Es erwächst einem eine gewisse Verpflichtung für diese Unterscheidungskraft, wenn man schon drinnen ist. Denn wir werden ganz fehlgehen mit dieser Anthroposophischen Gesellschaft, wenn wir nicht die Anknüpfung an die allgemeine Geisteskultur der Gegenwart suchen, wenn wir immer wieder und wiederum in den Fehler verfallen, Sektiererisches zu treiben.",
      "Das wird der Tod sein unserer Bewegung, wenn wir sektiererisch werden. Bedenken Sie doch nur, daß solche Dinge, wie wir sie in diesen Tagen jetzt erörtert haben, sich gar nicht besonders sonderbar ausnehmen werden für den­jenigen, der gerade in Wissenschaftlichem und im Kulturleben der Gegenwart drinnensteht, wenn er sich nur die nötige Vorurteilslosig­keit erwerben wird.",
      "Aber um auf diesem Wege etwas zu erreichen, ist es notwendig, daß der Wille besteht zur Unterscheidung. Bei uns kommt es leicht vor, daß nur um irgend etwas Schematisches gefragt",
      "wird, wenn es sich darum handelt: Soll irgend jemand bei anthropo­sophischen Vorträgen zuhören, oder soll er einen Zyklus bekommen? -So wird schematisch gefragt, ohne daß man Rücksicht nimmt auf den Bildungsgrad, auf die ganze Weltstellung des betreffenden Menschen. Aber das Schematische ist das absolut Schädliche bei uns. Das Sche­matische bringt es dahin, daß solch ein Mensch, wie jetzt wiederum der in Holland, um den sich eine ganze Summe von Unfug kristallisiert, in die Anthroposophische Gesellschaft hineinschwimmen und dort Protektoren finden kann, währenddem Leute, die urteilsfähig sind, gerade durch das Gebaren oftmals abgestoßen werden.",
      "Um auf ein Konkretes hinzuweisen: Sehen Sie, vor einiger Zeit trat Herr von Bernus auf innerhalb der Anthroposophischen Gesellschaft, mit dem deutlichen Bestreben - das man ja ein bißchen besser, ein bißchen schlechter finden kann, dafür mag der gesunde Menschenver­stand sprechen -, eine Brücke zu ziehen zwischen dem allgemeinen Kulturleben, dem literarischen und wissenschaftlichen Leben der Ge­genwart, und unserem anthroposophischen Leben. Nun, Herr von Bernus hat in seiner Art zum Beispiel eine Anzahl von Dingen, die zum Teil in meinen Büchern stehen, zum Teil in Zyklen, in seiner Art dichterisch umgegossen und in die Welt gebracht.",
      "Er hat mir es selbst gezeigt: einen Stoß von Briefen, von schimpfenden Briefen hat er dafür erhalten, daß da einmal ein wirklich zeitgemäßer Versuch ge­macht worden ist! Man würde sich gar nicht wundern, wenn jemand, der vielleicht viel aufs Spiel setzt, abgestoßen werden könnte durch ein solches Gebaren, wie es dazumal aus der Anthroposophischen Gesellschaft ihm gegenüber verübt worden ist.",
      "Dennoch, die Zeit­schrift, die er gegründet hat, sie wird ungeheuer dienlich sein können der anthroposophischen Bewegung. Er hatte es ja auch zuwege ge­bracht, daß die anthroposophische Bewegung in München vertreten werden konnte in seinem Kunsthaus.",
      "Aber man konnte überall gewisse Widerstände bemerken gegen etwas, was so berechtigt wie möglich war! Und wenn man gerade Bernus' Erlebnisse überschaut, so hat man an ihnen so recht ein Bild von dem, wie die anthroposophische Bewegung, die Anthroposophische Gesellschaft lernen sollte, wirklich eine Gesellschaft zu sein.",
      "Insofern der Dornacher Bau zustande gekommen ist, ist sie eine Gesellschaft. Aber vieles andere namentlich wird unterlassen, wodurch deutlich gezeigt wird, daß die Anthroposophische Gesellschaft sich gar nicht als Gesellschaft auffaßt, sondern als eine Summe von ein­zelnen sektiererischen kleinen Kreisen. Aber über dieses Stadium des Sektiererischen müssen wir hinauskommen. Und wir kommen nicht hinaus, wenn nicht über die Sache irgendwie nachgedacht wird.",
      "Es ist ja so schwierig, und nicht wahr, man sagt solche Dinge sehr ungern, aber schließlich, manches wird mir ja dadurch notwendig zu sagen, da ich persönlich so stark verquickt bin mit dieser anthropo­sophischen Bewegung. Wenn nun die Anthroposophische Gesell­schaft sich nach und nach immer mehr und mehr dazu entwickeln sollte, daß sie eigentlich eine Gesellschaft ist mit der ausgesprochenen Tendenz, mich totzuschweigen - wozu sie sich eigentlich entwickelt, und was sie immer als Tendenz gehabt hat -, so ist es nicht eine per­sönliche Eitelkeit, wenn ich dieses betone. Es ist mir sehr unange­nehm, daß ich es betonen muß, aber es ist in der Anthroposophischen Gesellschaft vielfach gerade die Tendenz vorhanden, mich totzu­schweigen, und da ist das Persönliche mit dem Sachlichen eben ver­knüpft. Dadurch - weil alles dasjenige nicht getan wird, was sonst eine Gesellschaft tut - kommt es, daß nur das als Giftblasen an die Ober­fläche kommt, was die abgefallenen Mitglieder an Geschimpfe in die Welt setzen.",
      "Ja, das sind Dinge, auf die ich schon manchmal eben hinweisen muß und die nicht unbesprochen bleiben dürfen. Ich habe sie an den Orten, wo ich in der letzten Zeit sprechen konnte, zur Besprechung gebracht, weil ich ja wirklich glaube, daß in dieser katastrophalen Zeit vieles darauf ankäme, daß Anthroposophie in der richtigen Weise in der Welt vertreten wird. Aber es ist so schwer, es dahin zu bringen, daß tiefer nachgedacht würde: Wie soll man es eigentlich auf dem anthro­posophischen Felde tun, um diese Anthroposophische Gesellschaft zu einer wirklichen Gesellschaft zu machen? - Die Ansätze sind wirklich gemacht von einzelnen Menschen, aber es bleibt in der Regel in den Ansätzen alles stecken. Nun, ich denke, daß vielleicht, indem ich noch ein zweites Mal auf die Sache aufmerksam gemacht habe, ein bißchen",
      "darüber nachgedacht werden wird. Ich sage es nicht aus persönlichen Gründen, sondern aus gewissen Notwendigkeiten der Zeit heraus, wie Sie ja auch aus dem, was ich gerade in diesen Tagen vorgebracht habe, mancherlei Keime entnehmen werden, die Ihnen zum Verständ­nisse unserer katastrophalen Zeit einige Dienste werden leisten kön­nen."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "Die Betrachtungen, die wir gegenwärtig anstellen, betreffen Dinge, welche von vielen Menschen, die etwas in der einen oder andern Form davon wissen, als Mysterien behandelt werden.",
        "Und es wird aus ge­wissen Gründen das Wissen von diesen Dingen der Welt von vielen Seiten her ferne gehalten, weil man der Ansicht ist, daß eben die Dinge, die in Betracht kommen, Teile sind von einem umfassenden Wissen über übersinnliche Angelegenheiten, das der Menschheit heute noch nicht mitgeteilt werden solle.",
        "Ich halte diese Anschauung mit Bezug auf gewisse Dinge, von denen hier die Rede ist, nicht für richtig, sondern mir erscheint es notwendig, daß die Menschheit den mutigen Entschluß fasse, einzutreten in eine wirkliche Betrachtung der übersinnlichen Welten.",
        "Und das kann man doch nicht anders, als wenn man das, was konkret über die betreffende Frage in Betracht kommt, unmittelbar anfaßt."
      ],
      [
        "Nun möchte ich heute gewissermaßen zuerst eine Art von Vorfrage erledigen.",
        "Wir haben gestern gesprochen über die Gliederung des Menschen zwischen dem Tode und einer neuen Geburt.",
        "Ein sehr ver­breiteter Einwand gegen das Besprechen dieser Dinge, jetzt nicht von seiten der Eingeweihten, sondern von seiten der Uneingeweihten, ist der, daß man einfach sagt: Ja, wozu ist es nötig, über diese Dinge etwas zu wissen?",
        "Man könnte ja warten, bis der Mensch durch die Pforte des Todes durchgeht, und dann werde er schon sehen, wie es da in der geistigen Welt eigentlich aussieht. - Es ist also etwas, das sehr häufig gesagt wird.",
        "Nun, die Sache ist aber so, daß wir solche Fragen niemals von einem gewissermaßen absoluten Standpunkte aus beantworten können, wenn wir über das Wirkliche sprechen, sondern daß wir sie, geisteswissenschaftlich betrachtet, immer beantworten müssen von dem Gesichtspunkte der Zeit, in der wir leben.",
        "Wir leben im fünften nachatlantischen Zeitraum, der begonnen hat im 15.",
        "Jahrhundert un­serer Zeitrechnung.",
        "Er schloß den vierten nachatlantischen Zeitraum ab , wie wir wissen, der im 8. vorchtistlichen Jahrhundert begonnen"
      ],
      [
        "und im 15. nachchristlichen Jahrhundert seinen Abschluß gefunden hat.",
        "Man hat sieben solcher Kulturzeiträume zu verzeichen.",
        "Daraus aber ist ersichtlich, daß wir die Mitte der Kulturentwickelung der Erde überschritten haben, die im vierten nachatlantischen Zeitraum lag, und daß wir einfach durch diesen Umstand eintreten - wir sind ja auch in der fünften großen Erdenperiode - in die Zeit, in der die Erde in absteigender Entwickelung ist."
      ],
      [
        "Schon die Betrachtungen, die wir in diesen Tagen angestellt haben , können Sie darauf aufmerksam machen, daß es darauf ankommt, hin-zuschauen auf die absteigende Entwickelung, auf dasjenige, was ge­wissermaßen nicht in der Evolution, sondern in der Devolution ist , was in der Rückentwickelung ist.",
        "Unsere ganze Erdenentwickelung ist in der Rückentwickelung."
      ],
      [
        "Da hören gewisse Fähigkeiten, gewisse Kräfte auf, die in der vorhergehenden Zeit der aufsteigenden Ent­wickelung da waten, und andere müssen für diese aufhörenden Kräfte und Fähigkeiten eintreten.",
        "Und so ist es insbesondere mit Bezug auf gewisse innere seelische Fähigkeiten des Menschen."
      ],
      [
        "Man kann sagen: Bis zum vierten nachatlantischen Zeitraum, bis gegen die Zeit des Mysteriums von Golgatha hin, waren in den Menschen noch die Fähigkeiten vorhanden, mit der übersinnlichen Welt einen gewissen Zusammenhang zu haben.",
        "Wir wissen, daß in der mannigfaltigsten Weise diese Fähigkeiten verschwunden sind."
      ],
      [
        "Sie sind nicht mehr als elementarische Fähigkeiten vorhanden, sie sind gewissermaßen dahin-geschwunden.",
        "Nicht nur hat sich das Leben des Menschen auf der Erde zwischen der Geburt und dem Tode geändert mit Bezug auf solche Fähigkeiten, sondern eigentlich, und noch radikaler, hat sich das Leben der Menschen zwischen dem Tod und einer neuen Geburt geändert."
      ],
      [
        "Und da muß gesagt werden, daß für diesen Zeitraum, vom Tode bis zur neuen Geburt, es im gegenwärtigen Menschheitszyklus, der also schon zu den absteigenden gehört, so ist, daß die Menschen , wenn sie durch die Pforte des Todes treten, gewisse Erinnerungen ha­ben müssen an dasjenige, was sie sich erworben haben hier im physi­schen Leibe, wenn sie die richtige Stellung und das richtige Verhältnis zu den Ereignissen, denen sie ausgesetzt sind zwischen dem Tod und einer neuen Geburt, finden wollen.",
        "Es gehört geradezu zu den notwendigen"
      ],
      [
        "Vorbedingungen eines rechten Lebens nach dem Tode, daß die Menschen immer mehr und mehr hier vor dem Tode gewisse Vor­stellungen sich erwerben über das Leben nach dem Tode, denn nur, wenn sie sich erinnern an diese Vorstellungen, die sie sich hier er­worben haben, können sie sich orientieren in der Zeit zwischen dem Tod und einer neuen Geburt.",
        "Es ist sachlich unrichtig, wenn behauptet wird, man könne warten bis zum Tode mit solchen Vorstellungen über das Leben zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Würden die Menschen fortfahren, in diesen Vorurteilen zu leben, würden sie es fortdauernd ablehnen, Vorstellungen schon hier gewinnen zu wol­len über das Leben zwischen dem Tod und einer neuen Geburt, so würde dieses Leben, dieses leibfreie Leben für sie ein finsteres werden, ein unorientiertes werden; sie würden nicht - durch alles dasjenige, was ich Ihnen gestern geschildert habe - in der richtigen Weise in ihre geistige Umgebung eindringen können.",
        "Bis nahe zum Mysterium von Golgatha war es so, daß die Menschen sich hier ins physische Leben Fähigkeiten hereingebracht haben, die aus der geistigen Welt stamm­ten."
      ],
      [
        "Daher hatten sie atavistisches Hellsehen.",
        "Dieses atavistische Hell-sehen kam davon, daß gewisse geistige Fähigkeiten sich aus dem Zu­stand vor der Geburt hereinerstreckten in dieses Leben.",
        "Das hörte auf."
      ],
      [
        "Die Menschen haben keine Fähigkeiten mehr hier im physischen Leben, die sich hereinerstrecken aus dem vorgeburtlichen Leben.",
        "Das wissen Sie ja.",
        "Aber dafür muß umgekehrt das andere eintreten: Die Men­schen müssen sich immer mehr und mehr hier auf der Erde Vorstel­lungen über das Post-mortem-Leben, das Leben nach dem Tode, erwerben, damit sie sich erinnern können nach dem Tode, damit sie durch des Todes Pforte etwas durchtragen können."
      ],
      [
        "Das ist dasjenige, was ich zu dieser Vorfrage insbesondere bemer­ken will.",
        "Also die bequeme Rede, daß man warten könne bis zum Tode mit solchen Vorstellungen, die gilt nicht, wenn man im Kon­kreten ins Auge faßt, in welchem Zeitpunkt der Erdenentwickelung wir uns eigentlich befinden.",
        "Und das muß man wirklich immer im Konkreten ins Auge fassen.",
        "Denn Ansichten, die absolut gelten, die zu allen Zeiten gelten, die gibt es nicht, sondern es gibt immer nur Anschauungen, welche für einen gewissen Zeitraum den Menschen"
      ],
      [
        "orientieren können.",
        "Das ist dasjenige, was man gerade durch Geistes­wissenschaft sich in so eminentem Sinne aneignen muß."
      ],
      [
        "Und nun möchte ich auf einiges eingehen, das unsere Betrachtungen zu einem vorläufigen kleinen Abschluß bringen kann.",
        "Wir sind ausge­gangen davon, daß der gegenwärtige Mensch eine Kluft empfindet zwischen dem, was er Ideale nennt, seien es moralische oder sonstige Ideale, was er auch Ideen nennt, und dem, was er als seine Anschau­ungen empfindet über die rein natürliche Weltenordnung.",
        "Die Be­griffe und Anschauungen, die sich der Mensch macht über die natür­liche Weltenordnung, die befähigen ihn nicht, anzunehmen, daß das-j enige, was er als Ideale in seinem Herzen trägt, reale Macht hat, sich wirklich so wie eine Naturkraft realisieren kann."
      ],
      [
        "Das Wesentliche, was für diese Frage in Betracht kommt, ist nun das Folgende: Wir wissen jetzt, wie es mit der Gliederung des Men­schen hier auf der physischen Erde steht.",
        "Wir wissen auch, wie es steht mit der Gliederung des Menschen in der geistigen Welt zwischen dem Tod und einer neuen Geburt."
      ],
      [
        "Ich habe vor einiger Zeit eine Frage aufgeworfen, welche eigentlich schon als eine konkrete Frage vor die menschliche Seele tritt, wenn der Mensch das Leben betrachtet, welche aber gerade eine Frage ist, der gegenüber man gar nichts sagen kann, wenn man vor der eben charakterisierten Kluft zwischen Idealismus und Realismus steht, das ist die Frage: Wie kommt es, daß in unserer Weltenordnung manche Menschen ganz jung sterben, schon als Kin­der oder als junge Leute oder im mittleren Lebensalter, andere erst sterben, wenn sie alt geworden sind?",
        "Mit was in der Weltenordnung hängt dieses zusammen? - Weder der Idealismus auf der einen Seite , noch der Realismus auf der andern Seite, der die Ideale nicht als reale Mächte ansehen kann, können irgend etwas über solche Fragen, die aber Lebensfragen sind, ausmachen."
      ],
      [
        "Diesen Fragen kann man auch nur dann nahetreten, wenn man etwas ganz Bestimmtes ins Auge faßt.",
        "Und das ist, wenn man ins Auge faßt, daß der gegenwärtige Mensch, so wie er einmal als Erdenmensch vor uns steht, verhältnis-mäßig leicht fertig wird mit dem Raume, aber er wird nicht in gleicher Weise fertig mit der Zeit."
      ],
      [
        "In dieser Beziehung bieten die sämtlichen philosophischen Anschauungen, die es bis heute gibt, eigentlich keinen"
      ],
      [
        "irgendwie nennenswerten Aufschluß, und die Frage nach dem Wesen der Zeit ist eigentlich bisher nur in engsten menschlichen Kreisen be­handelt worden.",
        "Es ist auch nicht so ganz leicht, über die Zeit und ihr Wesen populär zu sprechen, aber vielleicht gelingt es doch, bei Ihnen eine Vorstellung hervorzurufen von dem, was ich eigentlich meine, wenn ich die Zeit in Analogie mit dem Raume einmal zur Erörterung bringe.",
        "Ich muß da allerdings Ihre Geduld etwas in Anspruch nehmen, weil scheinbar, aber eben nur scheinbar, die kurze Betrachtung, die ich darüber anstellen will, einen etwas abstrakten Charakter hat."
      ],
      [
        "Wenn Sie einfach ein Stück der Räumlichkeit überschauen, so wis­sen Sie, daß dasjenige, was Sie da überschauen, sich Ihnen offenbart in einem perspektivischen Charakter.",
        "Sie müssen mit der Perspektive des Raumes rechnen, wenn Sie ein Stück Raum überschauen.",
        "Wenn Sie nun das Stück Raum, das Sie überschauen und dem Sie ganz instinktiv einen perspektivischen Charakter zuschreiben, auf eine Fläche bringen, dann berücksichtigen Sie die Perspektive dabei.",
        "Nicht wahr, wenn Sie in eine Allee hineinschauen, so sehen Sie die entfernten Bäume der Allee kleiner und näher aneinandergerückt.",
        "Das können Sie in der Perspektive ausdrücken, und Sie können in einer gewissen Weise per­spektivisch auf einer Fläche zum Ausdruck bringen, was Sie im Raume sehen."
      ],
      [
        "Nun ist es klar, daß dasjenige, was Sie im Raume sehen, in der Fläche nebeneinander ist.",
        "Im Raume ist es nicht nebeneinander; da sind diese zwei Bäume da vorne (siehe Zeichnung S.164), und zwei Bäume sind weit entfernt.",
        "Aber indem Sie den überschaubaren Raum in die Fläche bringen, setzen Sie dasjenige, was hintereinander ist, nebeneinander.",
        "Sie haben wiederum instinktiv die Fähigkeit, das, was Sie so male­risch oder zeichnerisch auf einer Fläche sehen, gewissermaßen in das Räumliche umzusetzen.",
        "Daß Sie diese Fähigkeit haben, das rührt da­von her, daß der Mensch, so wie er jetzt einmal als Erdenmensch ist, sich von dem Raume als solchem verhältnismäßig stark losgelöst hat."
      ],
      [
        "Nicht in gleicher Weise hat sich der Mensch von der Zeit losgelöst.",
        "Und das ist etwas ungeheuer Eingreifendes und Wichtiges, aber etwas leider kaum Bemerktes, kaum von der Wissenschaft Bemerktes.",
        "Der Mensch glaubt, wenn er sich in der Zeit entwickelt, die Zeit zu überschauen,"
      ],
      [
        "# Bild s. 164"
      ],
      [
        "die Zeit zu haben.",
        "Aber er hat in Wirklichkeit nicht die reale Zeit.",
        "Er hat gar nicht die reale Zeit, sondern das, was Sie als Zeit er­leben, das ist eigentlich im Verhältnis zu der wirklichen Zeit etwas, was man ein Abbild nennen kann.",
        "So wie dieses Bild (siehe Zeich­nung) in der Fläche sich zu dem Raume verhält, so verhält sich das , was der gewöhniiche Mensch Zeit nennt, zu der wirklichen Zeit.",
        "Der gewöhnliche Mensch erlebt nämlich nicht die wirkliche Zeit, sondern er erlebt ein Abbild der Zeit, er erlebt tatsächlich ein Abbild der Zeit.",
        "Und das kann man sich so sehr schwer vorstellen."
      ],
      [
        "Sie können sich zum Beispiel außerordentlich schwer vorstellen, daß dasjenige, was heute wirkt, gar nicht im jetzigen Zeitpunkt vor­handen zu sein braucht, sondern in einem viel früheren Zeitpunkte real ist und im heutigen Zeitpunkte nicht real ist.",
        "Sie sehen gleich­sam dasjenige, was in sehr frühem Zeitraume vorhanden ist, perspek­tivisch in Ihre eigene Zeit hereinwirken."
      ],
      [
        "Das, was ich jetzt gesagt habe, hat eine sehr bedeutsame Folge.",
        "Das hat nämlich die Folge, daß alles das, was wir Natur nennen, einen ganz andern Charakter trägt als alles dasjenige, was wir als einen gewissen Teil des Menschen selbst betrachten müssen.",
        "In der Natur draußen wirkt zum Beispiel auch Ahriman, beziehungsweise es wirken die ahrimanischen Mächte; aber die ahrimanischen Mächte wirken in der Natur draußen niemals gegenwärtig.",
        "Wenn Sie die gesamte Natur überschauen, so wirkt schon Ahriman in der Natur, aber er wirkt von"
      ],
      [
        "einer entfernten Zeit her.",
        "Von der Vergangenheit her wirkt Ahriman.",
        "Und ob Sie das mineralische, das pflanzliche, das tierische Reich über­blicken, Sie dürfen niemals sagen, in dem, was gegenwärtig vor Ihren Augen sich ausbreitet, liege etwas, worin Ahriman tätig ist.",
        "Und doch ist Ahriman drinnen tätig; aber von der Vergangenheit her.",
        "Wenn ich also die Sache zeichnen wollte, so müßte ich sagen: Hier ist die Entwickelungslinie von der Vergangenheit in die Zukunft hin, und hier überblicken Sie die Natur."
      ],
      [
        "# Bild s. 165a"
      ],
      [
        "Ja, nun müssen Sie es sich so denken, daß Sie da hineinschauen.",
        "In dem, was Sie als Gegenwärtiges überschauen, ist nichts von ahri­manischen Mächten enthalten, aber aus der Vergangenheit, aus einer bestimmten Vergangenheit wirkt Ahriman herüber in die Natur."
      ],
      [
        "# Bild s. 165b"
      ],
      [
        "Und Ihnen erscheint Ahriman in der Natur, wenn Sie ihn da gewahr werden, perspektivisch.",
        "Würden Sie sagen: Ahriman wirkt gegen­wärtig - dann begehen Sie der Natur gegenüber denselben Fehler, wie wenn Sie sagen würden: Überschaue ich einen Raum, so stehen die entfernten Bäume, weil sie sich perspektivisch in die Fläche hinein­stellen lassen, so neben den nahen Bäumen (siehe Zeichnung Seite 164)."
      ],
      [
        "Eine Grundforderung für ein reales Schauen in der geistigen Welt ist dieses, daß man zeitlich perspektivisch sehen lernt, daß man lernt, zeitlich jegliches Wesen an seinen richtigen Zeitpunkt zu setzen."
      ],
      [
        "Wenn ich nun gestern gesagt habe: Das Ich wird nach dem Tode gewissermaßen aus dem flüssigen Zustand heraus in eine Art festen"
      ],
      [
        "Zustandes versetzt -, so ist das noch nicht alles, sondern es kommt noch das andere dazu.",
        "Nehmen Sie an, Sie lebten hier auf der Erde mit Ihrem Ich vom Jahre 1850 bis zum Jahre 1920, und im Jahre 1920 werden Sie Ihr Ich gewahr.",
        "Ich meine also: Wohl werden Sie es schon früher gewahr, aber nun blicken Sie zurück, mit dem Geistselbst durch die Hierarchien blicken Sie auf Ihr Ich zurück; da sehen Sie Ihr Ich immer als stehengeblieben vom Jahre 1850 bis 1920.",
        "Das Ich bleibt da, bleibt stehen.",
        "Das heißt: Ihre Erlebnisse gehen bald nach Ihrem Tode nicht mit Ihnen, sondern Sie sehen auf sie zurück, Sie schauen nun von einer zeitlich entfernten Perspektive auf das zurück, und Sie sehen in die Zeitenlänge hinein, wie Sie hier in der physischen Welt in die Raumeslänge hineinsehen.",
        "Ich kann es auch so ausdrücken: Indem Sie, sagen wir, 1920 sterben, leben Sie mit alidem, was ich Ihnen ge­stern als die Glieder Ihres Wesens geschildert habe, dann weiter; aber Sie sehen zurück auf die Zeitstrecke, in der Sie hier auf Erden mit Ihrem Ich gelebt haben.",
        "Und diese Zeitstrecke bleibt dort, und Sie sehen sie immer, indem Sie perspektivisch weiterleben, an der Zeitstelle, wo sie war.",
        "Und so müssen Sie sich vorstellen, daß Ahriman wirksam ist draußen in der Natur, aber von einer früheren Zeitstelle aus."
      ],
      [
        "Das ist sehr wichtig.",
        "Das ist etwas, was sehr wenig berücksichtigt wird.",
        "Wenn man die Welt verstehen will, wenn man geisteswissen­schaftlich von der Zeit sprechen will, so muß man durchaus die Zeit raumähnlich vorstellen und muß dieses Verbundenbleiben des Wesen-haften mit der Zeit ins Auge fassen.",
        "Das ist sehr wichtig."
      ],
      [
        "Nun ist das, was ich Ihnen mit Bezug auf die ahrimanischen Mächte gesagt habe, daß sie von der Vergangenheit her wirken, für die Natur so richtig.",
        "Aber beim Menschen wird es gerade anders.",
        "Beim Men­schen wird es eben, während er hier zwischen Geburt und Tod lebt, dadurch anders, daß für ihn alles in der Zeit Ablaufende eben zur Maja, zur Täuschung wird.",
        "Der Mensch lebt, während er hier lebt, selber im Laufe der Zeit drinnen, und indem er eine gewisse Anzahl von Jahren durchlebt, durchlebt er den Zeiteniauf mit.",
        "Indem die Zeit abläuft, läuft er selber mit der Zeit ab.",
        "Das ist mit dem Raume nicht der Fall.",
        "Wenn Sie eine Allee entlanggehen, bleiben die Bäume zurück"
      ],
      [
        "und Sie schreiten vorwärts, und Sie nehmen die Bäume, die zurück­geblleben sind, also auch Ihre Eindrücke, nicht so mit, daß Sie, indem Sie einen Schritt machen würden, die Meinung hätten, es ginge das Baumbild mit Ihnen mit.",
        "Mit dem Zeitbilde machen Sie das.",
        "Hier im physischen Leibe machen Sie das tatsächlich so - weil Sie selbst in der Zeit sich weiterentwickeln -, daß Sie sich über die Zeit in bezug auf ihre Perspektive einer Täuschung hingeben.",
        "Sie merken die Perspek­tive der Zeit nicht.",
        "Und insbesondere merkt es nicht das Unterbewußt-sein des Menschen.",
        "Das Unterbewußtsein des Menschen merkt erst recht dieses Mitleben mit der Zeit nicht, gibt sich einer vollständigen Täuschung mit Bezug auf die Perspektive der Zeit hin.",
        "Das aber hat eine ganz bestimmte Folge.",
        "Das hat die Folge, daß nun in demjenigen, was im Menschen geschieht, ahrimanische Mächte als gegenwärtige Mächte wirken können.",
        "Ins menschliche Seelenleben herein wirken ahrimanische Mächte als gegenwärtige Mächte.",
        "So daß der Mensch der Natur so gegenübersteht: Indem er in die Natur hinaussieht, ist im Gegenwartigen nichts Ahrimanisches.",
        "In ihm wirkt das Ahrimanische als Gegenwärtiges, eben gerade als Maja, als Täuschung.",
        "Aber der Mensch ist dieser Täuschung über die Dinge, die ich Ihnen ausein­andergesetzt habe, hingegeben, so daß durch den Menschen die ahri­manischen Mächte die Möglichkeit gewinnen, in die Gegenwart her­einzukriechen, in die Gegenwart hereinzuwandeln.",
        "Wir können sagen:"
      ],
      [
        "Die ahrimanischen Mächte - und so ist es nun auch mit den luziferi­schen Mächten , wenn auch von einem gewissen andern Gesichts­punkte aus, wovon wir gleich sprechen werden - wirken in der Natur so, daß sie eigentlich mit der Gegenwart nichts zu tun haben, sondern von der Vorzeit herein ihre Wirkungen erstrecken.",
        "Im Menschen wir­ken diese ahrimanischen Mächte gegenwärtig."
      ],
      [
        "Was ist die Folge?",
        "Die Folge davon ist, daß der Mensch in seinem tiefsten Seelischen in bezug auf den eben auseinandergesetzten Punkt sich nicht verwandt mit der Natur fühlen kann.",
        "Er sieht auf sein Wesen, beziehungsweise fühlt sich in seinem Wesen, empfindet das naturgemäße Wesen.",
        "Weil in ihm ahrimanische Mächte Gegenwarts-mächte sind, in der Natur ahrimanische Mächte Vergangenheits-mächte sind, erscheint ihm alles dasjenige, was naturgemäß ist, anders"
      ],
      [
        "als dasjenige, was sich in ihm selbst entwickelt.",
        "Den Unterschied, den der Mensch zwischen sich und der Natur merkt, den enträtselt er sich nicht in der richtigen Weise.",
        "Würde er sich ihn in der richtigen Weise enträtseln, so wäre es so, wie ich es eben auseinandergesetzt habe.",
        "Er würde sagen: Draußen in der Natur wirkt Ahriman von der Ver­gangenheit aus; in mir wirkt Ahriman als eine gegenwärtige Macht. -Dadurch aber kommt es, wenn er auch den Unterschied nicht weiß , daß er sich im Sinne dieses Unterschiedes verhält, und die Natur als geistlos empfindet.",
        "Er empfindet es schon, daß in der Gegenwart die ahrimanischen Mächte nicht in der Natur unmittelbar wirksam sind , aber er empfindet die Natur als geistlos, weil er sich nicht sagt: Ahri-man wirkt von der Vergangenheit her -, sondern er sieht nur auf die gegenwärtige Natur.",
        "Darinnen wirkt nicht Ahriman."
      ],
      [
        "Nun ist aber Ahriman, so sonderbar das klingen mag, diejenige Macht, deren sich die allgemeine Weltenschöpfung bedient, um die Natur hervorzubringen.",
        "Wenn man von dem Geist der Natur spricht, wenn man vom reinen Geist der Natur spricht, müßte man eigentlich von dem ahrimanischen Geiste sprechen.",
        "Da ist er vollberechtigt, der ahrimanische Geist.",
        "Die Wesenheiten der normalen Hierarchien, die bedienen sich des ahrimanischen Geistes, um das hervorzubringen, was sich als Natur um uns herum ausbreitet.",
        "Daß wir die Natur nicht durchgeistigt empfinden, das rührt eben davon her, daß im gegen­wärtigen Leben der Natur der Geist nicht enthalten ist, sondern daß er von der Vergangenheit her wirkt.",
        "Und das ist das Geheimnis , möchte ich sagen, der weitschöpferischen Mächte, daß sie sich eines Geistes, den sie stehengelassen haben auf einer früheren Stufe, bedie­nen zur Wirkung auf einer späteren Stufe, aber ihn von der Vergangen­heit herein wirken lassen."
      ],
      [
        "Wir müßten, wenn wir von der Natur sprechen, nicht von Stoff sprechen, auch nicht von Kräften sprechen, wir müßten von ahrima­nischen Wesenheiten sprechen; aber wir müßten dann so sprechen, daß wir diese ahrimanischen Wesenheiten in die Vergangenheit setzten.",
        "So daß das Sonderbare herauskommt: Nehmen Sie an, irgendein Naturphilosoph sinnt, sinnt nach, was hinter den Erscheinungen der Natur ist.",
        "Nun, da macht er sich allerlei Theorien und Hypothesen"
      ],
      [
        "über Atomausammenhänge und dergleichen.",
        "So ist aber die Sache nicht.",
        "Hinter dem, was sich da sinnenfällig um uns herum ausbreitet, ist eigentlich nicht das, was die Naturphilosophen gewöhnlich ver­muten, sondern hinter alldem ist die Summe der ahrimanischen Mächte, aber nicht als gegenwärtige."
      ],
      [
        "Ist also der Naturphilosoph ge­nötigt, sagen wir, hinter den chemischen Elementen irgendwelche Atomstrukturen zu vermuten, so ist das falsch; hinter den chemischen Elementen stehen ahrimanische Mächte.",
        "Aber wenn Sie das, was Sie sehen, von den chemischen Elementen abheben könnten und dahin­terschauen, so würden Sie in der Gegenwart nichts dahinter sehen: da wäre es hohl, wo man die Atome sucht, und das, was wirkt, wirkt in diesen Hohlraum aus der Vergangenheit herein."
      ],
      [
        "So ist es in Wirklich­keit.",
        "Daher diese vielen verunglückten Theorien über dasjenige, was das «Ding an sich» ist; denn dieses «Ding an sich» ist in der Gegen­wart überhaupt nicht da.",
        "Sondern es ist an der Stelle, wo das «Ding an sich» gesucht wird, nichts; aber die Wirkung ist dort aus der Ver­gangenheit herein."
      ],
      [
        "So daß man sagen könnte, wenn Kant sein «Ding an sich» gesucht hat, so hätte er sagen müssen: Da, wo ich an das «Ding an sich» heran will, da kann ich nicht heran. - Das hat er ja auch gesagt.",
        "Aber er ist nicht darauf gekommen, daß er da überhaupt zunächst gegenwärtig nichts gefunden hätte, und daß er, wenn er hinter den Schleier der Dinge gegangen wäre, hätte weit zurück­gehen müssen; dann hätte er ahrimanische Mächte gefunden."
      ],
      [
        "Im Menschen selbst ist es anders.",
        "Gerade dadurch, daß der Mensch lebendig in die Zeit versetzt wird, dadurch ist es den ahrimanischen Mächten möglich gewesen, durch die Pforte der Menschheit in unsere Welt einzudringen und innerhalb des Menschen als solchem zu wirken.",
        "Und die Folge davon, daß die ahrimanischen Mächte im Menschen wirken, ist die, daß der Mensch loslöst dasjenige, was er in der Gegen­wart sieht, von dem Geistigen, daß der Mensch sein Gegenwarts-dasein löst von dem Geistigen.",
        "Das ist die Folge dessen, daß wir die ahrimanischen Mächte innerhalb der Maja in uns tragen.",
        "So daß man sagen kann: So wie wir die Welt materiell ansehen, losgelöst vom Geiste, als bloße Naturordnung, die ihren Gipfel zu finden glaubt in dem Gesetz der Erhaltung der Kraft und des Stoffes - was eine Illusion"
      ],
      [
        "ist -, was wir da als eine Naturordnung sehen, es ist lediglich durch den Umstand herbeigeführt, daß wir die ahrimanischen Mächte in uns tragen, und daß sie in der Natur draußen als gegenwärtige Mächte nicht sind. - Es stimmt deshalb dasjenige, was wir über die Natur denken, indem wir sie bloß materiell denken, nicht mit der Natur überein, stimmt nur mit der gegenwärtigen Natur überein.",
        "Aber diese gegenwärtige Natur ist eben ein Abstraktum, weil in ihr der vergangene Ahriman immer hereinwirkt."
      ],
      [
        "Nun wirkt in den Menschen nicht nur das Ahrimanische, sondern auch das Luziferische herein.",
        "Dieses Luziferische aber, das hat ge­wissermaßen eine andere Tendenz im Weltenall als das Ahrimanische.",
        "Vergegenwärtigen wir uns die Tendenz des Ahrunanischen, so wie wir die Sache jetzt ausgesprochen haben."
      ],
      [
        "Die Tendenz des Ahrimani­schen in uns besteht darin, die Welt materialistisch vorzustellen.",
        "Daß wir die Welt materialistisch vorstellen, daß wir uns eine bloße Natur-ordnung denken, ist die Folge davon, daß wir Ahrimanisches in uns tragen."
      ],
      [
        "Daß wir Ideale in uns tragen, welche sich loslösen von der allgemeinen Natur, nach denen wir uns in unserem gegenseitigen Ver­halten richten wollen, die uns aber doch nur wie Träume erscheinen müssen innerhalb der gegewärtigen Weltanschauung, die ausgeträumt sind, wenn nach der Naturordnung die Erde an ihrem Endzustand angekommen ist, das ist die Folge davon, daß die luziferischen Mächte , die ebenso wie die ahrimanischen in uns leben, immerfort das Be-streben haben, den Teil von uns, der ihnen zugänglich ist, ganz aus der Naturordnung herauszureißen und vollständig zu vergeistigen.",
        "Die luziferischen Mächte haben nämlich zu ihrer Haupttendenz, insofern sie in uns wohnen, uns so geistig wie möglich zu machen, uns wo­möglich loszureißen von allem materiellen Leben."
      ],
      [
        "Daher gaukeln sie uns solche Ideale vor, die keine Naturmächte sind, sondern die macht-los sind in der gegenwärtigen Naturordnung.",
        "Und verfiele der Mensch ganz und gar im Laufe der zukünftigen Erdenperiode dem luziferi­schen Einfluß, so daß er glauben würde, Ideale seien eben nur ge­dachte Dinge, nach denen sich das Gemüt richten kann, so würde dieser Mensch den luziferischen Mächten folgen."
      ],
      [
        "Die materielle Erde, zu der wir gehören, würde verfallen, zerstieben im Weltenall, würde"
      ],
      [
        "ihren Zweck nicht erfüllen, und die luziferischen Mächte würden den Menschen in eine andere geistige Welt führen, in die er nicht gehört.",
        "Dazu brauchen sie den Ktiff, uns Ideale vorzugaukeln, die eigentlich bloße Träume sind.",
        "Wie uns Ahriman nach der einen Seite eine Welt vormacht, welche eine bloße Naturordnung ist, so macht uns Luzifer auf der andern Seite eine Welt vor, die rein nur in gedachten Idealen besteht."
      ],
      [
        "Das ist etwas sehr Bedeutungsvolles.",
        "Und gegenwärtig wird nur ein Ausgleich, möchte ich sagen, in den Gebieten herbeigeführt, die noch im menschlichen Unbewußten liegen.",
        "Aber die Menschen müs­sen sich dieser Sache immer mehr und mehr bewußt werden, sonst kommen sie aus diesem Dilemma nicht heraus, kommen nicht dazu, eine Brücke zwischen dem Idealismus und dem Realismus zu bauen, welche Brücke aber notwendig ist."
      ],
      [
        "Dasjenige, was gegenwärtig noch eine Art Ausgleich schafft, das ist das Folgende.",
        "Wenn gegenwärtig ganz junge Menschen sterben, zum Beispiel Kinder, so haben diese Kinder - bei jungen Menschen ist es ebenso - eben in die Welt hereingeschaut; sie haben nicht voll das Dasein hier auf dem physischen Plane ausgelebt.",
        "Mit einem auf dem physischen Plane unausgelebten Leben kommen sie hinüber in die andere Welt, die zwischen dem Tode und einer neuen Geburt verlebt wird, so verlebt wird, wie ich es gestern geschildert habe.",
        "Dadurch, daß sie einen Teil nur des Erdenlebens gelebt haben, bringen sie etwas vom Erdenleben mit hinüber in die geistige Welt, das man nicht hin­überbringen kann, wenn man alt geworden ist.",
        "Man kommt anders in der geistigen Welt an, wenn man alt geworden ist, als wenn man jung stirbt.",
        "Wenn man jung stirbt, so hat man das Leben so durchlebt, daß man noch viele Kräfte in sich hat vom vorgeburtlichen Leben.",
        "Man hat als Kind und als junger Mensch das leibliche Leben so durchlebt, daß man darinnen noch viel von den Kräften in sich hat, die man vor der Geburt in der geistigen Welt hatte.",
        "Dadurch hat man eine innige Verbindung geschaffen zwischen dem Geistigen, das man mitge­bracht hat, und dem Physischen, das man hier erlebt hat.",
        "Und durch diese innige Verbindung kann man etwas, was man auf der Erde er­wirbt, in die geistige Welt mit hinübernehmen.",
        "Kinder oder sonst"
      ],
      [
        "jung gestorbene Leute, nehmen von dem Erdenleben etwas in die geistige Welt mit hinüber, was gar nicht mit hinübergenommen wer­den kann, wenn man als älterer Mensch stirbt.",
        "Das, was da mitgenom­men wird, ist dann drüben in der geistigen Welt, und was da hinüber-getragen wird durch Kinder und junge Leute, das gibt der geistigen Welt eine gewisse Schwere, die sie sonst nicht haben würde, der­jenigen geistigen Welt, in der dann die Menschen gemeinsam drinnen leben, das gibt eine gewisse Schwere der geistigen Welt und verhindert die luziferischen Mächte, die geistige Welt ganz loszutrennen von der physischen."
      ],
      [
        "Also denken Sie, auf welches riesige Geheimnis wir da blicken!",
        "Wenn Kinder und junge Leute sterben, so nehmen sie von hier etwas mit, wodurch sie die luziferischen Mächte verhindern an deren Be­streben, uns ganz loszulösen von dem Erdenleben.",
        "Das ist außer­ordentlich wichtig, daß man dies ins Auge faßt."
      ],
      [
        "Wird man älter hier auf der Erde, so kann man in der geschilderten Weise den luziferischen Mächten die Rechnung noch nicht verderben; denn von einem gewissen Alter an hat man nicht mehr jene innige Verbindung zwischen dem, was man mitgebracht hat bei der Geburt und dem physischen Erdenleben.",
        "Ist man alt geworden, so löst sich diese innerliche Verbindung, und es tritt gerade das Umgekehrte ein.",
        "Von einem gewissen Lebensalter an träufeln wir in einer gewissen Weise dem innerhalb der physischen Erde befindlichen Geistigen un­ser eigenes Wesen ein.",
        "Wir machen die physische Erde geistiger als sie sonst wäre.",
        "Also von einem bestimmten Alter an vergeistigen wir in einer gewissen Weise, die man nicht mit äußeren Sinnen wahrnehmen kann, die physische Erde.",
        "Wir tragen Geistiges in die physische Erde hinein, wie wir Physisches in die geistige Welt hinauftragen, wenn wir jung sterben; wir pressen gewissermaßen Geistiges aus, wenn wir alt werden, ich kann es nicht anders sagen.",
        "Das Altwerden besteht im geistigen Sinne von einem gewissen Aspekt aus darinnen, daß man Geistiges hier auf der Erde auspreßt.",
        "Dadurch wird wiederum die Rechnung des Ahriman verhindert.",
        "Dadurch kann Ahriman nicht auf die Dauer heute schon so intensiv auf die Menschen wirken, daß völlig erlöschen könnte die Meinung, Ideale hätten doch eine gewisse Bedeutung."
      ],
      [
        "Aber wir sind im heutigen Zeitraume schon sehr, sehr nahe daran, daß die Menschen in die furchtbarsten Irrtümer gerade mit Be­zug auf das Gesagte verfallen.",
        "Auch Gutmeinende verfallen leicht in bezug auf das Gesagte in solche Irrtümer.",
        "Und diese Irrtümer werden immer größer und größer werden und mit zunehmender Erdenent­wickelung eben riesig werden können."
      ],
      [
        "Um Ihnen ein Beispiel anzuführen: Ein recht geistvoller Philosoph hat 1882 eine «Anthroposophie» geschrieben, Robert Zimmermann.",
        "Ich habe das schon einmal in einem Zusammenhange erwähnt.",
        "Diese «Anthroposophie» ist nicht dasjenige, was wir Anthroposophie jetzt nennen, sie ist mehr oder weniger ein Begriffsgestrüpp."
      ],
      [
        "Aber das ist ja aus dem Grunde, weil eben Robert Zimmermann nicht in die geistige Welt hineinsehen konnte, sondern nur Herbartianischer Philosoph war.",
        "Nun hat er diese «Anthroposophie» geschrieben.",
        "Aber gerade in dieser «Anthroposophie» beschäftigt sich Robert Zimmermann von seinem Gesichtspunkte aus mit der Frage, die ich in diesen Tagen an die Spitze unserer Betrachtungen gestellt habe."
      ],
      [
        "Er sieht auf der einen Seite die Ideen, logische Ideen, ästhetische Ideen, ethische Ideen; er sieht auf der andern Seite die Naturordnung.",
        "Und er kann nicht irgend­wie eine Brücke finden zwischen den logischen, den ästhetischen, den ethischen Ideen und der Naturordnung, sondern er bleibt doch dabei stehen: Da ist auf der einen Seite die Naturordnung, und auf der an­dern Seite sind die Ideen."
      ],
      [
        "Und wozu er zuletzt kommt, das ist doch außerordentlich interessant, denn es ist eigentlich typisch für einen Menschen der Gegenwart.",
        "Er kommt dahin, zu sagen, es sei ein für allemal dem Menschen versagt, die Natur mit Ideen zu bevölkern und den Ideen Naturgewalt beizulegen."
      ],
      [
        "Die beiden Welten seien eigent­lich nur im Kopfe des Menschen miteinander zu verbinden.",
        "So sagt er.",
        "Und daher meint er an einer Stelle, wo er geradezu alles zusammen­faßt, was er sagt und was er denkt: «Die Verwirklichung der Ideen ist weder eine Tatsache, die in der Vergangenheit, noch eine solche, die in der Gegenwart, sondern eine Aufgabe, deren Erfüllung in der Zukunft und in den Händen des Menschen liegt."
      ],
      [
        "Der Traum eines ,goldenen Zeitalters', von welchem ein nüchterner Rationalist wie Kant als von jenem des ,ewigen Friedens', ein extremer Positivist wie"
      ],
      [
        "Comte als dem ,état positif' schwärmte, wird dann erfüllt sein , wenn die gesamte Ideenwelt real geworden und die gesamte Wirklichkeit von den Ideen durchdrungen, d.h. wenn dasjenige, was Schiller ,das Kunstgeheimnis des Meisters' nannte, die ,Vertilgung des Stoffes durch die Form' offenbar, wie Schleiermacher es ausdrückte ,wenn die Ethik Physik und die Physik Ethik' geworden sein wird.»"
      ],
      [
        "Ja, aber das kann nie werden!",
        "Es kann nur das werden, daß die Menschen in ihrer sozialen Ordnung die Ideen realisieren.",
        "Wenn aber die Erde einmal an ihrem Ende angelangt sein wird, so wird der ganze Ideentraum ausgeträumt sein.",
        "Ein anderes ist nach einer solchen Philosophie nicht möglich.",
        "Daher bleibt eine solche Philosophie im­mer abstrakt und muß zuletzt gestehen: «Eine Philosophie, welche, wie die vorstehende, sich weder wie die Theosophie auf einen mensch­lichem Wissen unzugänglichen theozentrischen Standpunkt versetzt , um von ihm aus den ,Vernunfttraum' als längst geschaffene Wirklich­keit, noch wie die Anthropologie auf den zwar anthropozentrischen aber unkritischen Standpunkt gemeiner Erfahrung stellt, um von ihm aus eine ideenerfülite Wirklichkeit als ,Traum der Vernunft' an­zusehen, welche sonach zugleich anthropozentrisch d. i. von mensch­licher Erfahrung ausgehend und doch Philosophie d. i. an der Hand des logischen Denkens über dieselbe hinausgehend sein will ist An­throposophie.» «Anthroposophie» ist also hier das Eingeständnis, daß man niemals über diese Kluft hinüberkommen könne zwischen un­realen Ideen und ideenloser Realität."
      ],
      [
        "Nun ist aber im Menschen selbst ein Naturwesen, das also der Na­turordnung angehört, verbunden mit einem Geistwesen, das in sich aufnehmen kann das Geistige.",
        "Das leugnet ja auch nicht ein solcher Anthroposoph wie Robert Zimmermann.",
        "Aber von der gegenwär­tigen Wissenschaft kann auch der Mensch nicht so betrachtet werden, daß sich durch den Menschen, durch diesen Mikrokosmos, das Rätsel lösen würde."
      ],
      [
        "Blicken wir jetzt zurück auf etwas, was wir auch schon während des diesmaligen Aufenthaltes erwähnt haben.",
        "Wir haben gesagt, daß wir eigentlich den Menschen gliedern müssen in drei Teile, natürlich nicht so bequem, wie es am Skelett ist. das habe ich schon ausgeführt."
      ],
      [
        "Aber ich habe mich ja darüber auch ausgesprochen in den Schluß­notizen zu meinem Buche «Von Seelenrätseln».",
        "Wir können den Menschen gliedern in drei Teile: den Hauptesmenschen, den Rumpf-menschen und den Extrerritätenrnenschen' indem zum Extremitäten-menschen alles dasjenige gehört, was inwärts der Extremitäten ge­legen ist, also auch alles Sexuelle zum Extremitäteumenschen gehört."
      ],
      [
        "Wenn wir den Menschen so gliedern und jetzt anwenden dasjenige, was wir schon wissen: daß die Kopf bildung, die Kopfform auf Kräfte hinweist der vorigen Inkarnation, der Extremitätenmensch hinweist auf die zukünftige Inkarnation und eigentlich nur der Rumpfmensch der Gegenwart angehört, so werden Sie nach dem, was ich heute aus­geführt habe, es nicht mehr sehr unbegreiffich finden, wenn ich Ihnen sage: Insofern der Mensch sein Haupt trägt, weist dieses Haupt auf die frühere Inkarnation zurück, in die Vergangenheit.",
        "Ins Haupt herein wirken Kräfte der Vergangenheit, ahrimanische Kräfte, und dasjenige, was für die ahrimanischen Kräfte im allgemeinen gilt, gilt für das menschliche Haupt im besonderen."
      ],
      [
        "Alles, was eigentliche Hauptes-bildung im Menschen ist, gehört nicht eigentlich der Gegenwart an, sondern in das Haupt wirken hinein die Kräfte der vorgehenden In-karnation; und die schöpferischen Mächte bedienen sich der ahri­manischen Mächte, um unser Haupt zu formen, um unserem Haupte die eigentliche Formung zu geben.",
        "Würden nicht die schöpferischen Mächte sich der ahrimanischen Geister bedienen, um unser Haupt zu formen, dann würden wir alle - verzeihen Sie, aber es ist so - zwar ein viel weicheres Haupt tragen, aber wir würden alle ein tierisches Haupt tragen: der eine, welcher in seinem Charakter stiermäßig ist, würde ein Stierhaupt, der andere, der in seinem Charakter lammäßig ist, würde ein Lämmerhaupt tragen und so weiter."
      ],
      [
        "Von dem Einfluß der ahrimanischen Mächte, deren sich die schöpferischen Gewalten be-dienen, um uns zu formen, rührt es her, daß dieses tierische Haupt, das wir sonst tragen würden, nicht wirklich uns aufsitzt, so wie es die Ägypter gezeichnet haben an manchen ihrer Figuren; daß wir nicht so herumgehen wie diese ägyptischen Gestalten, die ihre guten Gründe haben, weil in den ägyptischen Mysterien auch, wenn auch von einem atavistischen Standpunkte aus, solche Dinge gelehrt worden sind, wie"
      ],
      [
        "sie jetzt wieder gelehrt werden können; daß wir auch nicht so noch herumgehen wie in den Rosenkreuzerbildern etwa, wo jede Frau mit einem Löwenkopf, jeder Mann mit einem Ochsenkopf gemalt wird.",
        "So ist ja das Rosenkreuzergemalde des Menschen.",
        "Die Rosenkreuzer haben mehr ein Durchschnitts-Tier gewählt und haben daher das , was für die Frauen am meisten ähnlich ist, den Löwenkopf, den Frauen aufgesetzt, und dem Manne, was ihm am meisten ähnlich ist, den Ochsenkopf, den Stierkopf.",
        "Sie sehen daher auf rosenkreuzerischen Figuren Mann und Frau nebeneinandergestellt: die Frau mit dem schönsten Löwenkopf, den Mann mit einem Stierkopfe.",
        "Dies ist aber durchaus richtig.",
        "Daß die Metamorphose - jetzt goethisch gespro­chen - sich vollziehen kann, daß unser in seiner Form nach der Tier­heit tendierendes Haupt so gestaltet wird, daß es Menschenhaupt ist, rührt von dem Einfluß der ahrimanischen Mächte her.",
        "Würden sich nicht die Gottheiten Ahrimans bedienen, um unser knöchernes Haupt zu formen, dann würden wir mit Tierhäuptern herumgehen."
      ],
      [
        "Aber die göttlichen Mächte bedienen sich auch der luziferischen Geister.",
        "Würden sie sich dieser luziferischen Geister nicht bedienen , so würde wiederum unser Extremitätenmensch von der jetzigen zu der nächsten Inkarnation sich nicht umwandeln können.",
        "Dazu sind die luziferischen Wesenheiten notwendig.",
        "Den luziferischen Wesen­heiten verdanken wir es wiederum, daß, indem wir sterben, umge­wandelt wird nach und nach die Form, die jetzt noch der Extremi­tätenmensch hat, in die weitere Form, die sie in der nächsten Inkar­nation haben soll.",
        "Da muß dann in der Mitte des Weges zwischen dem Tod und einer neuen Geburt Ahriman eintreten, um die andere Auf­gabe zu übernehmen: um das Haupt wiederum in der entsprechenden Weise umzuformen.",
        "Wie wir mit Tierhäuptern herumgehen würden , wenn wir es Ahriman nicht zu verdanken hätten, daß wir einen Men­schenkopf bekommen, so würde unsere Extremitätennatur sich nicht ins Menschliche metamorphosieren bis zur nächsten Inkarnation, sondern sie würde ins Dämonische übergehen.",
        "Unseren Kopf, wie wir ihn jetzt haben, verlieren wir ja unter allen Umständen durch den Tod, nicht nur als Materie, die sich mit der Erde vereinigt, sondern auch als Form; in die nächste Inkarnation tragen wir ja das, was Kopf"
      ],
      [
        "wird, vom Extremitätenmenschen hinüber.",
        "Aber das würde ein dä­monisches Wesen werden, wenn wir es nicht den luziferischen Mäch­ten, die mit uns verbunden sind, zu verdanken hätten, daß die Umge­staltung stattfinden könne vom Dämon, der ein bloß Geistig-Seeli­sches wäre, in die Menschengestalt der nächsten Inkarnation."
      ],
      [
        "So müssen bei unserem Menschenwerden ahrimanische und luzi­ferische Mächte mitwirken, und es kann das Menschliche nlcht be­griffen werden, ohne daß das Ahrimanische und das Luziferische zu Hilfe gerufen wird.",
        "Der Menschheit kann es gegen die Zukunft hin nicht erspart werden, die Wirksamkeit Ahrimans und Luzifers wirk­lich zu verstehen.",
        "Mit vollem Rechte sagt die Bibel, daß jene Gottheit, von der im Anfange der Bibel die Rede ist, dem Menschen den le­bendigen Odem einhauchte.",
        "Aber der lebendige Odem wirkt im Rumpfmenschen.",
        "Insofern wir es also zu tun haben mit den normal wirkenden göttlichen Wesenheiten, haben wir es nur mit dem Rumpf-menschen zu tun.",
        "Insofern wir es mit dem Kopfmenschen zu tun haben, haben wir es mit einem Gegner der Jahvemächte zu tun, da­durch auch mit einem Gegner des Christus.",
        "Und auch insofern wir es mit dem Extremitätenmenschen zu tun haben, haben wir es mit dem luziferischen Gegner zu tun."
      ],
      [
        "Daher wird man den Menschen nur verstehen, wenn man ihn unter diesen drei Aspekten vorstellt.",
        "Sie haben daher in unserer Mittel­punktsgruppe für unseren Bau eben diese Trinität: den Menschheits­repräsentanten, der aber so ausgebildet ist, daß in ihm vorzugsweise die Kräfte der Atmung, des Rumpfes wirken, die Herztätigkeit und so weiter - das ist die mittlere Figur -, dann diejenige Figur, in der alles Hauptmäßige, Kopfmäßige wirkt: Ahriman; diejenige Figur, in der alles Extremitätenmäßige wirkt: Luzifer."
      ],
      [
        "Man muß das Menschliche in dieser Weise auseinandernehmen, wenn man den Menschen verstehen will, denn im Menschen ist der Mensch als solcher mit Ahriman und Luzifer vereint.",
        "Das ist gleich­zeitig wohl darauf hinweisend, daß alles, was mehr oder weniger mit dem menschlichen Denken zusammenhängt, welches ja in bezug auf seinen physischen Zusammenhang an den Kopf gebunden ist - das menschliche Denken verffießt auf Grund der Wahrnehmungen als"
      ],
      [
        "eines Äußerlich-Sinnenfälligen -, daß alles das einen ahrimanischen Charakter hat.",
        "Durch die Sinne des Kopfes nehmen wir ja vorzugs­weise die Natur wahr, und wir bauen uns ein Naturhild auf mit dem eben vorhin geschilderten ahrimanischen Charakter, weil wir selbst das Ahrimanische in der Bildung, in der Formung unseres Kopfes an uns tragen."
      ],
      [
        "Die Ideale wiederum haben innerlich, psychologisch- darauf komme ich dann in der nächsten Zeit noch zurück -, sehr viel mit der Liebe zu tun, mit alidem, was dem Extremitätenmenschen angehört.",
        "Daher hat zu den Idealen die luziferische Macht den besonderen Zutritt.",
        "Durch unser Haupt faßt uns Ahriman, durch unsere Extremitäten faßt uns Luzifer.",
        "Durch unser Haupt verführt uns Ahriman dazu, die Natur geistlos vorzustellen; durch unseren Extremitätenrnenschen verführt uns Luzifer dazu, die Ideale ohne Naturgewalt vorzustellen."
      ],
      [
        "Das aber ist die Aufgabe des gegenwärtigen Menschen, dadurch, daß er solches überschaut, zu einer richtigen Übersicht zu kommen.",
        "Denn sehen Sie: In uns ist eine gewisse Grenzscheide, gerade in un­serem Brustmenschen, in unserem Rumpfmenschen, wodurch die Gewalten des Hauptes, welche ahrimanische Gewalten sind, abgetrennt werden von den luziferischen Gewalten, die dem Extremitätenmen­schen angehören.",
        "Würden wir , in dem wir mystisch in uns hinein­schauen, uns ganz durchschauen können, dann würden wir zwar durch das Haupt die Naturordnung begreifen, aber wir würden auch durch die Naturordnung in uns selbst hineinschauen.",
        "Und würden in uns die luziferischen Mächte entscheiden, dann würden die luziferischen Mächte uns auch über die ahrimanischen Mächte aufklären, und wir würden auf diese Weise zu einer Verbindung zwischen Naturordnung und Geistordnung kommen.",
        "Aber das können wir aus einem gewissen Grunde nicht, und zwar aus dem Grunde, weil wir ein Gedächtnis haben.",
        "Dasjenige, was wir aus der Natur aufnehmen an Vorstellungen und Begriffen, an Eindrücken, das speichern wir in unserem Ge­dächtnisse auf.",
        "Und wenn das da hier (siehe Zeichnung Seite 179) -schematisch nur gezeichnet - der Hauptesmensch, das der Brust- und Rumpfmensch, das der Extremitätenmensch ist, so ist im Rumpf-menschen die Scheidewand, die dazu führt, daß dasjenige, was wir"
      ],
      [
        "# Bild s. 179"
      ],
      [
        "durch das Haupt aufnehmen an Naturordnung, uns wiederum als Gedächtnisstoff zurückkommt.",
        "Dadurch sehen wir nicht bis zum Luziferischen hinunter, und dadurch bemerken wir das Ahrimanische nicht, wie wir das nicht sehen, was vor einem Spiegel ist, sondern das­jenige, was sich spiegelt.",
        "Hier spiegelt sich die Naturordnung in dem, was zu gleicher Zeit unser Ahrimanisches von unserem Luziferischen abtrennt, und was die Grundlage ist für das sich bildende Gedächtnis, für die sich bildende Erinnerungskraft.",
        "Wenn wir uns nicht an die er­lebten Dinge erinnern könnten, wenn diese Scheidewand nicht da wäre, wenn wir uns, in uns blickend, durchschauen würden, so würden wir bis zum Luziferischen hinunterblicken in uns.",
        "Dann würden wir auch das Ahrimanische wahrnehmen."
      ],
      [
        "Aber jetzt bedenken Sie: Dasjenige gerade, was uns durch diesen Spiegel erscheint, das ist ja dasjenige, was wir im Lebenslauf durch-leben, das ist, worauf wir nach dem Tode zurückblicken, das ist, was aus einem flüssigen Ich zu einem festen Ich wird.",
        "Darauf blicken wir zurück.",
        "Das ist dasjenige, womit wir leben.",
        "Und Ahriman und Luzifer wirken mit uns, wirken mit uns so, daß Ahriman uns dahin bringt, ein Menschenhaupt zu tragen, Luzifer uns dahin bringt, nicht zum Dämon"
      ],
      [
        "zu werden, sondern die Möglichkeit zu haben, zu einer nächsten In­karnation zu kommen."
      ],
      [
        "Ich habe Ihre Geduld etwas in Anspruch genommen mit Dingen, die ja vielleicht etwas schwieriger verständlich sind, allein ich wollte zunächst wenigstens ein Gefühl dafür hervorrufen, wodurch eigent­lich die Kluft entsteht zwischen Idealismus und Realismus.",
        "Sie ent­steht dadurch, daß das Luziferische in uns den Idealismus erregt, der machtlos ist in der Natur, daß das Ahrimanische in uns die bloße Na­turordnung hervorruft, welche uns geistlos erscheint."
      ],
      [
        "So stehen eigent­lich die Idealisten, die abstrakten Idealisten unter luziferischem Ein­fluß, die Materialisten unter ahrimanischem Einfluß.",
        "Es ist schon not­wendig, daß man auf diese Dinge sich einläßt, daß man nicht bloß sche­matisch die sogenannte Theosophie treibt, sondern auf diese genaue­ren Dinge sich einläßt."
      ],
      [
        "Denn es ist notwendig, daß der Mensch sich bewußt werde, er müsse etwas dazu tun, um mit dem Geiste für den Rest der Erdenentwickelung vereint bleiben zu können.",
        "Es ist eine unbequeme Wahrheit, man könnte sagen, sogar auch eine gehaßte Wahrheit, richtig eine gehaßte Wahrheit, denn sie widerspricht ja so vielem, was den Menschen sympathisch ist, aus Bequemlichkeit sym­pathisch ist."
      ],
      [
        "Nichts wird dem Menschen heute schwieriger, als wenn man ihm sagt: Wenn du dir in Zukunft deine Verbindung mit dem Geiste erhalten willst, so mußt du etwas dazu tun. - Es möchten ja die meisten Menschen, daß das Mysterium von Golgatha aus dem Grunde verflossen wäre, damit sie nur ja nichts zu tun haben zu ihrer Angelegenheit, damit sie durch Christus von ihren Sünden erlöst wer­den und ohne ihr Zutun in den Himmel kommen können.",
        "Und des­halb werden ja die meisten Theologen so wütend auf die Anthropo­sophie, weil das selbstverständlich von anthroposophischer Seite nie­mals zugegeben werden kann, daß der Mensch nichts zu tun habe, um seine Verbindung mit dem Geiste aufrechtzuerhalten, daß das ganz ohne sein Zutun auch in der Zukunft der Erdenentwickelung vor sich gehen könne."
      ],
      [
        "Die Verbindung zwischen dem Physischen und dem Geistigen, zwischen dem, was die Glieder des Menschen sind zwischen Geburt und Tod, und dem, was die Glieder des Menschen sind zwi­schen Tod und neuer Geburt, diese Verbindung wird in Frage gestellt"
      ],
      [
        "durch die zukünftige Erdenentwickelung, und sie wird nur dann nicht in Unordnung kommen, wenn sich die Menschen mit dem Geistigen gegen die Zukunft hin wirklich befassen werden.",
        "Dafür gibt es heute schon geisteswissenschaftliche Beweise.",
        "Diese geistes-wissenschaftlichen Beweise, sie sind höchst, höchst unbequeme Wahr­heiten, aber sie werfen Licht auf Wichtiges, auf Bedeutungsvolles."
      ],
      [
        "Der Zusammenhang zwischen dem Seelisch-Geistigen und dem Physisch-Ätherischen im Menschen der Gegenwart ist, möchte ich sagen, schon sehr locker geworden, und der Mensch hat es notwen­dig, immer mehr und mehr bei sich Wache zu stehen, damit nicht in dem Zusammenhang zwischen seinem Physisch-Ätherischen und Seelisch-Geistigen etwas geschieht, was ihn gewissermaßen aussaugen könnte, was ihn seelisch-geistig aussaugen könnte.",
        "Denn wenn solche Vorurteile immer reger werden, man brauche im Leben nichts zu wissen über die Art, wie es nach dem Tode aussieht, oder wenn die Kluft immer größer wird zwischen sogenanntem Idealismus und rein natürlicher Ordnung, ist die Gefahr, der die Menschen entgegengehen, daß sie immer mehr und mehr ihre Seele verlieren könnten.",
        "Heute ist noch, ich möchte sagen, diesem Verlieren der Damm vorgesetzt, der dadurch gegeben ist, daß, wenn junge Leute sterben, der geistigen Welt eine gewisse Schwere verliehen wird und Luzifer die Rechnung verdorben wird, und wenn alte Leute sterben, so viel ausgepreßt wird an Geistigkeit in die physische Welt herein, daß Ahriman die Rech­nung verdorben wird.",
        "Aber man darf nicht vergessen, daß dadurch, daß die Menschen sich lossagen vom geistigen Gebiet, die ahrimani­nischen und die luziferischen Mächte immer mächtiger und mächtiger werden, und daß nach und nach, indem die Devolution der Erde im­mer weiter und weiter geht, dieser Damm nicht mehr voll wirken könnte."
      ],
      [
        "Das ist dasjenige, was ich gern möchte, daß es sich als eine Art Bodensatz aus unseren Betrachtungen ergäbe wie ein Gefühl - und Gefühle sind immer das Wichtigste, was aus dem geisteswissenschaft­lichen Leben hervorgehen kann - von der Notwendigkeit, sich vom gegenwärtigen Erdenzyklus ab mit dem Geistigen zu befassen.",
        "Von den verschiedensten Gesichtspunkten aus habe ich dieses betont, daß"
      ],
      [
        "es von der Gegenwart aus notwendig ist, daß die Menschen sich mit dem Geistigen befassen.",
        "Und anders wird man sich nicht mit dem Geistigen befassen können in der Zukunft als dadurch, daß man sich Verständnis erwirbt und sich nicht sträubt, solche auch schwierigere Betrachtungen wirklich in sich aufzunehmen, wie wir sie in diesen Tagen und insbesondere auch heute gepflogen haben.",
        "Es muß unter die Menschen kommen das Verständnis von der Perspektivität der Zeit.",
        "Wenn dieses Verständnis von der Perspektivität der Zeit unter die Menschen kommt, dann werden sie nicht mehr sagen: Hier ist der Idealismus, der aber nur ein bloßer Traum ist, der keine Naturgewalt hat, und auf der andern Seite liegt die Naturordnung -, sondern die Menschen werden darauf kommen, anzuerkennen, daß, was als Ideale in uns lebt, Keim ist für die Zukunft, und daß, was Naturordnung ist, Frucht ist der Vergangenheit."
      ],
      [
        "Dieser Satz ist eine goldene Regel: Jedes Ideal ist Keim für zu-künftiges Naturgeschehen; jedes Naturgeschehen ist Frucht vergan­genen Geistgeschehens. - Nur durch diese Regel findet man die Brücke zwischen Idealismus und Realismus.",
        "Aber dazu ist eines notwendig.",
        "Irgendein Ideal könnte nie und nimmermehr Keim für ein zukünftiges Naturgeschehen werden, wenn dieses zukünftige Naturgeschehen durch das gegenwärtige Naturgeschehen verhindert würde.",
        "Wir kön­nen uns irgendeine Hypothese vor die Augen führen.",
        "Nehmen wir die Möglichkeit an, die heute gilt, daß einmal durch das sogenannte Gesetz der Entropie die Erdenentwickelung in eine Art von allgemeiner Durchwärmung übergehe, und daß alle andern Naturkräfte aufhören , so würde innerhalb dieses Endrustandes natürlich alles Ideale erstor­ben sein.",
        "Dieser Endaustand, der folgt ganz gut, wenn man annimmt, daß sich nach reiner Kausalität die gegenwärtigen physikalischen Zu­stände eben weiter fortsetzen werden.",
        "Denkt man so, wie die gegen­wärtige Physik denkt, daß nach dem Gesetze der Erhaltung der Kraft und des Stoffes einmal ein solcher Endaustand da sein wird, dann ist in diesem Endzustand kein Platz dafür, daß in ihm einmal ein Ideal als das zukünftige Naturgeschehen aufgehe, denn das zukünftige wird einfach die Folge des gegenwärtigen Naturgeschehens sein.",
        "Aber so ist es nicht, so stellt es sich nicht der gegenwärtigen Naturbetrachtung"
      ],
      [
        "dar, sondern es stellt sich dieses anders dar.",
        "Dasjenige, was heute an Stoffen, an Kräften existiert, alles das wird in einer bestimmten Zu­kunft nicht da sein.",
        "Das Gesetz der Erhaltung des Stoffes und der Kraft gibt es nicht.",
        "Da, wo man den Stoff sucht, ist überhaupt nichts als ein Hereinwirken eines vergangenen Ahrimanischen, und dasjenige, was uns umgibt im Sinnenfälligen, wird in einer gewissen Zukunft nicht mehr sein da.",
        "Und dann, wenn von alledem, was jetzt physisch ist, nichts mehr da ist, wenn das ganz aufgelöst ist, dann ist die Zeit da, wo sich die gegenwärtigen Ideale als Naturgeschehen anreihen werden an das, was jetzt zugrunde gehen wird."
      ],
      [
        "So ist es im großen Weltenall.",
        "Und für den einzelnen Menschen ist es so, daß er in der nächsten Welteninkarnation wieder inkarniert wird, wenn partiell alles dasjenige überwunden ist, in das er mit der gegenwartigen Inkarnation hineingewachsen ist, wenn also für ihn eine Umgebung hergestellt werden kann, die anders ist als die gegenwärtige Umgebung, wenn aus der gegenwärtigen Umgebung all das heraus sein kann, was ihn jetzt hier auf der Erde hält.",
        "Wenn sich das alles so geändert hat, daß er Neues erleben kann, dann wird er wieder inkar­niert.",
        "Die gegenwartigen Ideale, die im Menschen sich bilden können, werden Natur sein , wenn alles dasjenige, was jetzt Natur ist, nicht mehr da sein wird, sondern Neues entstanden sein wird.",
        "Aber das Neue, das entsteht, ist eben nichts anderes als das Natur gewordene Geistige."
      ],
      [
        "Hinter den Erscheinungen und hinter den Idealen müssen wir das­jenige suchen, was die Brücke über dem Abgrunde bildet.",
        "Aber zu dem muß man eben dahinterkommen.",
        "Man kommt heute nur dahinter wenn man sich nicht scheut, die Begriffe so kräftig zu entwickeln, daß sie selbst in die Realität eindringen können.",
        "Daher hat die heutige Zeit wirklich die Notwendigkeit, sich gar sehr einzulassen auf alles das­jenige, was geistig erfahren werden kann.",
        "Nur - lassen Sie mich das noch anhänglich hinzufügen -, nur wird eben notwendig sein, daß gegenüber geistigen Betrachtungen immer größere und größere Un­befangenheit walten könnte.",
        "Vorgestern habe ich zum Schlusse, wie es manchen vielleicht erscheinen könnte, recht unnötig - aber trotz­dem ich es nicht gerne tue, ist es nie unnötig - auf mancherlei hinge­wiesen, was dem gedeihlichen geisteswissenschaftlichen Wirken auch"
      ],
      [
        "von seiten der Anthroposophischen Gesellschaft entgegensteht.",
        "Da ist vor allen Dingen auf diesem Boden immer wieder und wiederum zu fordern wirkliche Unbefangenheit.",
        "Immer wieder und wiederum erleben wir ja, daß das Auflösende, das eigentlich den Materialismus hervorgebracht hat, das die alte Geistigkeit zugrunde gerichtet hat , im menschlichen Denken gerade auch in das Spirituelle, in das ge­wollte Spirituelle hereindringt."
      ],
      [
        "Ich habe ja darauf aufmerksam ge­macht, wie materialistisch manche theosophische Anschauung ist.",
        "Man hat es natürlich nicht leicht, wenn man geisteswissenschaftliche Dinge auseinandersetzt, die bezeichnenden Worte zu finden, weil ja unsere Sprache heute nicht mehr für das Geistige geeignet ist, weil wir erst wieder suchen müssen eine solche Verbindung zwischen der Sprache und der Sache, welche für das Geistige geeignet ist."
      ],
      [
        "Aber das ist notwendig, daß nicht immer mit dem, was das Schädlichste ist, die geisteswissenschaftliche Bewegung verdorben wird.",
        "Man muß un­befangen charakterisieren dasjenige, was im Geiste vorgeht.",
        "Immer wiederum erlebe ich, daß ich gefragt werde: Da ist jemand, dort ist jemand, der hat geistige Erlebnisse. - Der Sinn der Fragen, die häufig so gestellt werden, ist der, daß eigentlich gefragt wird: Darf man nun mit blindem Glauben an die Wahrheit dessen sich hingeben, was der oder jener schaut? - Und wenn man diese Frage bejaht, ja, dann ent­steht blinde Anhängerschaft; wenn man sie verneint, dann entsteht das, daß der Betreffende gleich verketzert wird und gesagt wird: Nun ja, das ist atavistisches Hellsehen, auf das gibt man nichts. - Ja, dieses Entweder-Oder muß doch auf diesem Gebiete ganz anders genommen werden."
      ],
      [
        "Wir müssen uns wirklich mit aller gesunden Vernunft auch den Aussagen über das Geistige gegenüberstellen.",
        "Wenn wir aber Dogmatiker werden wollen, können wir nicht Geisteswissenschafter werden.",
        "Wenn wir entweder vergöttern oder verketzern wollen, kön­nen wir nicht Geisteswissenschafter werden."
      ],
      [
        "Es werden unendlich wertvolle Beiträge zur Charakteristik der geistigen Welt auch von Seiten kommen, auf die man nicht unbedingt schwören will."
      ],
      [
        "Auch das andere erlebt man, daß eine Zeitlang auf irgendeine sehe­rische Persönlichkeit geschworen wird.",
        "Dann kann man nachweisen, daß diese seherische Persönlichkeit irgendwann - nun, vielleicht sogar"
      ],
      [
        "einmal ein wenig retuschiert hat, oder stark retuschiert hat; dann ist die Persönlichkeit unten durch.",
        "Vorher haben dieselben Leute auf sie geschworen, bei denen sie nachher unten durch ist."
      ],
      [
        "Ja, in dieser Weise kommt man nicht vorwärts; innerhalb der Menschheit mit dem Entweder-Oder der Vergöttlichung oder Ver­ketzerung kommt man nicht vorwärts innerhalb der Menschheit, sondern nur dadurch, daß man sich mit seinem gesunden Menschen­verstand den Dingen gegenüberstellt.",
        "Es kann zum Beispiel auch der Fall eintreten, daß durch jemanden, von dem man sogar weiß: Nun, der verschmäht es nicht, ab und zu recht stark zu schwindeln - einmal etwas ganz Wahres, Wichtiges, Wesentliches aus der geistigen Welt herauskommt."
      ],
      [
        "Man würde nicht zu dem Entweder-Oder kommen, das ich hier meine , wenn man nicht Dogmatik einführen wollte, sondern wenn man sich mit dem gesunden Menschenverstand gerade innerhalb dieser anthroposophischen Bewegung hineinstellen wollte.",
        "Das ist das eine."
      ],
      [
        "Das andere ist dieses, daß es außerordentlich schwierig ist, durch die Art und Weise, wie die Dinge oftmals innerhalb unseres Kreises ge­handhabt werden, die Anthroposophische Gesellschaft in die Kultur-bewegung der Gegenwart hineinzustellen.",
        "Dazu gehört Unterschei­dungsvermögen bei denjenigen Menschen, die schon drinnen sind in dieser Gesellschaft."
      ],
      [
        "Es erwächst einem eine gewisse Verpflichtung für diese Unterscheidungskraft, wenn man schon drinnen ist.",
        "Denn wir werden ganz fehlgehen mit dieser Anthroposophischen Gesellschaft, wenn wir nicht die Anknüpfung an die allgemeine Geisteskultur der Gegenwart suchen, wenn wir immer wieder und wiederum in den Fehler verfallen, Sektiererisches zu treiben."
      ],
      [
        "Das wird der Tod sein unserer Bewegung, wenn wir sektiererisch werden.",
        "Bedenken Sie doch nur, daß solche Dinge, wie wir sie in diesen Tagen jetzt erörtert haben, sich gar nicht besonders sonderbar ausnehmen werden für den­jenigen, der gerade in Wissenschaftlichem und im Kulturleben der Gegenwart drinnensteht, wenn er sich nur die nötige Vorurteilslosig­keit erwerben wird."
      ],
      [
        "Aber um auf diesem Wege etwas zu erreichen, ist es notwendig, daß der Wille besteht zur Unterscheidung.",
        "Bei uns kommt es leicht vor, daß nur um irgend etwas Schematisches gefragt"
      ],
      [
        "wird, wenn es sich darum handelt: Soll irgend jemand bei anthropo­sophischen Vorträgen zuhören, oder soll er einen Zyklus bekommen? -So wird schematisch gefragt, ohne daß man Rücksicht nimmt auf den Bildungsgrad, auf die ganze Weltstellung des betreffenden Menschen.",
        "Aber das Schematische ist das absolut Schädliche bei uns.",
        "Das Sche­matische bringt es dahin, daß solch ein Mensch, wie jetzt wiederum der in Holland, um den sich eine ganze Summe von Unfug kristallisiert, in die Anthroposophische Gesellschaft hineinschwimmen und dort Protektoren finden kann, währenddem Leute, die urteilsfähig sind, gerade durch das Gebaren oftmals abgestoßen werden."
      ],
      [
        "Um auf ein Konkretes hinzuweisen: Sehen Sie, vor einiger Zeit trat Herr von Bernus auf innerhalb der Anthroposophischen Gesellschaft, mit dem deutlichen Bestreben - das man ja ein bißchen besser, ein bißchen schlechter finden kann, dafür mag der gesunde Menschenver­stand sprechen -, eine Brücke zu ziehen zwischen dem allgemeinen Kulturleben, dem literarischen und wissenschaftlichen Leben der Ge­genwart, und unserem anthroposophischen Leben.",
        "Nun, Herr von Bernus hat in seiner Art zum Beispiel eine Anzahl von Dingen, die zum Teil in meinen Büchern stehen, zum Teil in Zyklen, in seiner Art dichterisch umgegossen und in die Welt gebracht."
      ],
      [
        "Er hat mir es selbst gezeigt: einen Stoß von Briefen, von schimpfenden Briefen hat er dafür erhalten, daß da einmal ein wirklich zeitgemäßer Versuch ge­macht worden ist!",
        "Man würde sich gar nicht wundern, wenn jemand, der vielleicht viel aufs Spiel setzt, abgestoßen werden könnte durch ein solches Gebaren, wie es dazumal aus der Anthroposophischen Gesellschaft ihm gegenüber verübt worden ist."
      ],
      [
        "Dennoch, die Zeit­schrift, die er gegründet hat, sie wird ungeheuer dienlich sein können der anthroposophischen Bewegung.",
        "Er hatte es ja auch zuwege ge­bracht, daß die anthroposophische Bewegung in München vertreten werden konnte in seinem Kunsthaus."
      ],
      [
        "Aber man konnte überall gewisse Widerstände bemerken gegen etwas, was so berechtigt wie möglich war!",
        "Und wenn man gerade Bernus' Erlebnisse überschaut, so hat man an ihnen so recht ein Bild von dem, wie die anthroposophische Bewegung, die Anthroposophische Gesellschaft lernen sollte, wirklich eine Gesellschaft zu sein."
      ],
      [
        "Insofern der Dornacher Bau zustande gekommen ist, ist sie eine Gesellschaft.",
        "Aber vieles andere namentlich wird unterlassen, wodurch deutlich gezeigt wird, daß die Anthroposophische Gesellschaft sich gar nicht als Gesellschaft auffaßt, sondern als eine Summe von ein­zelnen sektiererischen kleinen Kreisen.",
        "Aber über dieses Stadium des Sektiererischen müssen wir hinauskommen.",
        "Und wir kommen nicht hinaus, wenn nicht über die Sache irgendwie nachgedacht wird."
      ],
      [
        "Es ist ja so schwierig, und nicht wahr, man sagt solche Dinge sehr ungern, aber schließlich, manches wird mir ja dadurch notwendig zu sagen, da ich persönlich so stark verquickt bin mit dieser anthropo­sophischen Bewegung.",
        "Wenn nun die Anthroposophische Gesell­schaft sich nach und nach immer mehr und mehr dazu entwickeln sollte, daß sie eigentlich eine Gesellschaft ist mit der ausgesprochenen Tendenz, mich totzuschweigen - wozu sie sich eigentlich entwickelt, und was sie immer als Tendenz gehabt hat -, so ist es nicht eine per­sönliche Eitelkeit, wenn ich dieses betone.",
        "Es ist mir sehr unange­nehm, daß ich es betonen muß, aber es ist in der Anthroposophischen Gesellschaft vielfach gerade die Tendenz vorhanden, mich totzu­schweigen, und da ist das Persönliche mit dem Sachlichen eben ver­knüpft.",
        "Dadurch - weil alles dasjenige nicht getan wird, was sonst eine Gesellschaft tut - kommt es, daß nur das als Giftblasen an die Ober­fläche kommt, was die abgefallenen Mitglieder an Geschimpfe in die Welt setzen."
      ],
      [
        "Ja, das sind Dinge, auf die ich schon manchmal eben hinweisen muß und die nicht unbesprochen bleiben dürfen.",
        "Ich habe sie an den Orten, wo ich in der letzten Zeit sprechen konnte, zur Besprechung gebracht, weil ich ja wirklich glaube, daß in dieser katastrophalen Zeit vieles darauf ankäme, daß Anthroposophie in der richtigen Weise in der Welt vertreten wird.",
        "Aber es ist so schwer, es dahin zu bringen, daß tiefer nachgedacht würde: Wie soll man es eigentlich auf dem anthro­posophischen Felde tun, um diese Anthroposophische Gesellschaft zu einer wirklichen Gesellschaft zu machen? - Die Ansätze sind wirklich gemacht von einzelnen Menschen, aber es bleibt in der Regel in den Ansätzen alles stecken.",
        "Nun, ich denke, daß vielleicht, indem ich noch ein zweites Mal auf die Sache aufmerksam gemacht habe, ein bißchen"
      ],
      [
        "darüber nachgedacht werden wird.",
        "Ich sage es nicht aus persönlichen Gründen, sondern aus gewissen Notwendigkeiten der Zeit heraus, wie Sie ja auch aus dem, was ich gerade in diesen Tagen vorgebracht habe, mancherlei Keime entnehmen werden, die Ihnen zum Verständ­nisse unserer katastrophalen Zeit einige Dienste werden leisten kön­nen."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Die Wissenschaft vom Werden des Menschen",
      "9    an diesem unserem Bau: Siehe «Der Baugedanke des Goetheanum». Lichtbildervortrag in Bern, 29. Juni1921, mit 104 Abbildungen des ersten Goetheanum. Gesamtausgabe, Stuttgart 1958.",
      "nach längerer, erzwungener Abwesenheit: Dr. Steiner hatte zuletzt am 17. Januar 1918 zu den Mitgliedern in Dornach gesprochen, war also sieben Monate fort gewesen.",
      "10    Anthropnsophische Gesellschaft: Begründet am 28. Dezember 1912 bei der Loslösung von der Thensophischen Gesellschaft. Siehe: «Die Geschichte und die Bedingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesell­schaft», 8 Vorträge, 10.-17. Juni 1923, Gesamtausgabe Dornach 1959.",
      "12    wie den Vorträgen begegnet wurde: «Das Sinnlich-Übersinnliche in seiner Verwirklichung durch die Kunst», München, 15. und 17. Februar 1918, und «Die Quellen der künst­lerischen Phantasie und die Quellen der übersinnlichen Erkenntnis», München, 5. und 6. Mai 1918, im Bande «Kunst und Kunsterkenntnis», Gesamtausgabe Dornach 1961.",
      "Alexander von Bernns, 1880-1965, Dichter. Gab von 1916 bis 1921 in Manchen die Vierteljshres-Zeitschrift «Das Reich» heraus. In seinem «Kunsthaus» «Das Reich» hielt Rudolf Steiner zeitweise seine Münchner Vorträge.",
      "15    IVooerow Wilson, 1856-1924, Präsident der USA von 1912 bis 1920. Verleladete am",
      "8.    Januar 1918 ein Friedensprogramm, die Vierzehn Punkte.",
      "17    ein Universiiätsprofessor: George Santayans, 1863-1952, englischer Philosoph spani­scher Abstammung. Kam schon 1872 nach Amerika, wo er bis 1912 blieb.",
      "Emile Boutroux, 1845-1921, französischer Philosoph. G. Ssntayar'a, «L'erreur dc la philosophie allemande». Paris 1917, préface d'Emile Boutroux.",
      "19    so weile Kreise, wie Mond, Sonne, Saturn: Es sind damit frühere Evolutionazustände des Erdplaneten gemeint, nicht die heute so genannten Weltkörper. Siehe «Die Ge­heimwissenschaft im Umriß», Gesamtausgabe Dornach 1962, Kapitel «Die Welt-entwickelung und der Mensch».",
      "aus den vorjäbrigen Zürcher Vorträgen: «Anthroposophie und aleadernische Wissen­schaften», 4 Vorträge vom 5. bis 14. November 1917, Zürich 1950.",
      "Oskar Hertwig, 1849-1922, Anatom und Biologe. «Das Werden der Organismen, zur",
      "Widerlegung von Darwins Zufsllstheorie durch das Gesetz in der Entwicklung».",
      "ein kürzeres' Buch: «Zur Abwehr des ethischen, des sozialen und des politischen Darwinismus». Jens 1918.",
      "23    He,\"'ann von Helmboltz 1821-1894, Physiologe und Physiker. Erinder des Augen­spiegels, 1851.",
      "23/24 eine Schrift über die Freiheit: Woodrow Wilson, «Die neue Freiheit». 1913. Deutsche Übersetzung München 1914. «Nur Literatur, Betrachtungen eines Amerikaners» 1893. Deutsche Übersetzung 1913, darin der Essay «Der Verlauf amerikanischer Ge­schichte».",
      "24 Herman Grimm, 18281901.",
      "26    Wladimir llfits'h Lenin, eigentlich Uljsnow, 1870-1924, führte 1917 die bolsehe­wittische Revolution durch.",
      "27    Karl Marx, 1818-1883. Begründer des wissenschaftlichen Sozialismus und Mitver­fasser des «Kommunistischen Manifests» 1848.",
      "31    in den Büchern, die Ihnen ja vorliegen: «Theosophie», Gesamtausgabe Dornach 1961, und «Die Geheimwissenschaft im Umriß», Gesamtausgabe Dornach 1962.",
      "32    «Ignorahimus»: Der Ausspruch des Berliner Physiologen Emil Du Bois-Reymond,",
      "18181896, in seiner Rede «Über die Grenzen des Naturerkennens». Leipzig 1872.",
      "38    gilt das Wort: Aus Schiller «Der Taucher». Wörtlich: «Da unten aber ist's fürchter­lich, / Und der Mensch versuche die Götter nicht/ Und begehre nimmer und nimmer zu schauen, / Was sie gnädig bedecken mit Nacht und Grauen.»",
      "42    hei unserer Gruppe drüben: Die plastische Gruppe des Menschheitarepräsentanten zwi­schen Luzifer und Ahriman.",
      "46    Ich habe öfter: Siehe den Vortrag vom 25. Juni 1918 in Berlin, im Bande «Erden-sterben und Weltenleben», Gesamtausgabe Dornach 1967.",
      "hier ja wohl auch schon: Im Vortrag vom 29. Juli 1916. im Bande «Das Rätsel des Menschen», Gesamtausgabe Dornach 1963.",
      "Otto Weininger, 1880-1903. «Über die letzten Dinge» 4. Auflage Wien und Leipzig 1918.",
      "Einer dieser Aphorismen: Wörtlich: «Aus unserem Zustand vor der Geburt ist viel­leicht darum keine Erinnerung möglich, weil wir so tief gesunken sind durch die",
      "Geburt:    wir haben das Bewußtsein verloren und gänzlich triebartig geboren zu wer­den verlangt, ohne vernünftigen Entschluß und ohne Wissen, und darum wissen wir gar nichts von dieser Vergangenheit.»",
      "47    Und darüber schrieb er die Notiz: Wörtlich: «Ich morde mich selbst, um nicht einen andern morden zu müssen.»",
      "48    Babindranath Tagore, 1861-1941, indischer Dichter und Philosoph.",
      "49    jenen Essay: «Der Verlauf amerikanischer Geschichte» in «Nur Literatur» von Woodrow Wilson.",
      "55    zwei Artikel gegen mich: Otto Zimmermann S. J.: Anthroposophische lirlehren, «Stimmen der Zeit», 48. Jg., 10. H., Juli 1918, S.328 ff., Joseph Kreitmaier S. J.:",
      "«Vom Expressionismus», ebenda S. 356 ff.",
      "60    der griechische Weise: Platon, im 6. Buch vom «Staat».",
      "63    Arthur Ba«oir, 18481930; 1916 Außenminister Großbritanniens. Honeton Stewart Chamberlain, 1855-1927.",
      "81    Sie werden einen Zweigvnrtrag finden: Vortrag vom 23. Mai 1916 in «Gegenwärtiges und Vergangenes im Menschengeiste», Gesamtausgabe Dornach 1962.",
      "82    kh habe das im vorigen Jahre hier ausgeführt: Siehe den Vortrag vom 14. Oktober 1917 in «Die spirituellen Hintergründe der äußeren Welt. Der Sturz der Geister der Finster­nis», Gesamtausgabe Dornach 1965.",
      "87    von der ande\"n Seite: Siehe den Vortrag vom 20. August 1918 (Zeichnung Seite 31) Sie erinnern sich an die Zeichnung: Auf Seite 31 dieses Bandes.",
      "«Von Seelenrätseln», Gesamtausgabe Dornach 1960. «Skizzenhafte Erweiterungan des Ir'haltes dieser Schrift: S. Über die wirkliche Grundlage der intentior'alen Be-ziehung».",
      "92 Björnstierne Björnson, 1832-1910, norwegischer Dichter.",
      "93 Nero, regierte 54-68",
      "94    Vespasianuc, regierte 69-79",
      "Titns, regierte 79-81",
      "Domitianus, regierte 81-96",
      "Ners'a, regierte 96-98",
      "Si,'tonius, schrieb im 1.Jahrhundert n.Chr. Kaiserbiographien.",
      "Tacitns, um 55 bis um 120, römischer Geschichtsschreiber.",
      "Flavius P. Philostratus der Altere, griechischer Sophist zu Ende des 2. Jahrhunderts n.Chr. Beschrieb das Leben des Apollonius von Tyana.",
      "Apollnnius von Tyana, Prophet und Wundertäter im 1.Jahrhundert n.Chr.",
      "der Tübinger Theologe Baur: Ferdinand Christian Baur, 1792-1860, protestantischer Theologe, «Apollonius von Tysna und Christus», Tübingen 1832.",
      "113    Sie können das in verschiedenen Zyklen lesen: Zum Beispiel in «Welt, Erde und Mensch», Gesamtausgabe Dornach 1960; «Ägyptische Mythen und Mysterien», Gesamtaus­gabe Dornach 1960.",
      "117 Augustus, 63 v.Chr. bis 14 n.Chr., erster römischer Kaiser, Caesar Augustus",
      "119 im «Reich»: In der Vierteljahresachrift «Das Reich». München, 2. Jahr, Buch 3 und",
      "4; 3.Jahr, Buch 1, Oktober 1917 bis April 1918.",
      ": In «Philosophie und Anthroposo­phie», Gesamtausgabe Dornach 1965 und in Johann Valentin Andreae, «Die Chy­mische Hochzeit des Christian Rosenkreutz Anno 1459», ina Neuhochdeutache über­tragen von Walter Weber, Stuttgart 1957; beigefügt sind die Ausführungen Rudolf Steiners in der Zeitschrift «Das Reich», Verlag Freiea Geistesleben, Stuttgart 1957.",
      "Johann Valentin Andreae, 1586-1654, Dichter und theologischer Schriftsteller.",
      "«Allgemeine Reformation der ganzen weiten Weil>: Nach W.Weber (s o.) Seite 181 ist dieses Werk die Übersetzung eines Kapitels aus Boecalnis «Ragguali di Parnasso», Venedig 1612.",
      "«Bewegung für ethitehe Kultur»: Vgl. hier:':a Rudolf Steiner, «Mein Lebeosgang», Kap. XVII.",
      "120    «Dic Zukunft>, Wochensehrift, herausgegeben von Maximilian Harden (eig­Witkowski), 1861-1927. In «Gesamn,elte Aufsätze zur Kulturgeschichte 1887-1901», Gesamtausgabe Dornach 1966.",
      "was kh dann das soziale Karzinom genannt babe: Im Vortragazyklus",
      "121    Wladimir Iljitsch Lenin: Siehe Hinweise zu Seite 26. Karl Marx: Siehe Hinweise zu Seite 27.",
      "Ferdinand Lassalle, 1825-1864, sozialistischer Führer.",
      "Edaard Ber\"stein, 1850-1932, sozialistischer Theoretiker, der Begründer des Revisio­nismus.",
      "123    Carl Freiherr du Pre4 1839-1899. «Das Rätsel des Menschen». Leipzig 1892.",
      "127    Julius Robert Mayer, 1814-1878, Arzt und Physiker.",
      "129    «Philosophie und Anthroposophic»: Sonderdruck aus dem gleichnamigen Band der Ge­samtausgabe, Dornach 1964.",
      "in der Mittelpunktsgruppe des Baues: Holzgruppe, den Menschheitsrepräsentanten, Christus, zwischen Luzifer und Ahriman darstellend.",
      "130    Ich habe über dic Entwickelung der Christuc- Gestalt ja öfter hier geprochen: Zum Beispiel am 29. Oktober 1917, 13. Vortrag in «Kunstgeschichte als Abbild innerer geistiger Impulse», Dornach 1957.",
      "132 Pythagoras, etwa 582 v.Chr.",
      "132    daß in Urzeiten der Merkur mit dem Monde einmal Seharh gespielt hat: Diese Erzählung findet sich bei Plutarch in «Über Isis und Osiris».",
      "eines solehen agy ptischen Weiten: Plutarch nennt den Priester Oinuphis von Heliopolis als Lehrer des Pythagoras.",
      "133    Jakob Böhme, 1575-1624.",
      "134    Max Müller, 1823-1900, Sanskrit- und Religionaforscher in Oxford. Charles Darwin, 1809-1882, englischer Naturforscher.",
      "Ernst Ha'ckel, 1834-1919, Zoologe.",
      "142    Wir haben Zyklen nur abgegeben an die Mitglieder der Gesellschaft: Diese Beschränkung wurde an der Weihnachtstagung 1923 aufgehoben.",
      "144    tiefstgehende Einflüsse eines Menschen: des Apollonius von Tyana.",
      "148    als fünf Vokale: Jehova (v = u).",
      "156    Sybaris: Stadt in Unteritalien, gegründet 700 v.Chr., im Altertum sprichwörtlich durch die Schwelgerei ihrer Bewohner.",
      "169    Immanuel Kant, 1724-1804. «Kritik der reinen Vernunft» 1781.",
      "173    Robert Zimmermann, 1824-1898, Ästhetiker und Philosoph. «Anthroposophie im Umriß» Wien 1882, S. 307 f.",
      "174    Augnste Gomte, 1798-1857, französischer Philosoph. Begründer des Positivismus und der Soziologie.",
      "Friedrich Schiller, 1759-1805.",
      "Friedrich Schleiermacher, 176818M, evangalischer Theologe, Prediger und Philosoph.",
      "175    in den Schlußnotizen: «Von Seelertratseln», Gesamtausgabe Dornach 1960, Kapitel IV,",
      "6. «Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit».",
      "176    in den Rosenkreuzerbildern: «Die geheimen Figuren der Rosenkreuzer».",
      "186    Alexander von Be\"nus: Siehe Hinweis zu Seite 12.",
      "die Zeitschrift, die er gegründet hat: Siehe Hinweis zu Seite 12. in seinem Kunethans: Siehe Hinweis zu Seite 12."
    ],
    "sentences": [
      [
        "Die Wissenschaft vom Werden des Menschen"
      ],
      [
        "9 an diesem unserem Bau: Siehe «Der Baugedanke des Goetheanum».",
        "Lichtbildervortrag in Bern, 29.",
        "Juni1921, mit 104 Abbildungen des ersten Goetheanum.",
        "Gesamtausgabe, Stuttgart 1958."
      ],
      [
        "nach längerer, erzwungener Abwesenheit: Dr.",
        "Steiner hatte zuletzt am 17.",
        "Januar 1918 zu den Mitgliedern in Dornach gesprochen, war also sieben Monate fort gewesen."
      ],
      [
        "10 Anthropnsophische Gesellschaft: Begründet am 28.",
        "Dezember 1912 bei der Loslösung von der Thensophischen Gesellschaft.",
        "Siehe: «Die Geschichte und die Bedingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesell­schaft», 8 Vorträge, 10.-17.",
        "Juni 1923, Gesamtausgabe Dornach 1959."
      ],
      [
        "12 wie den Vorträgen begegnet wurde: «Das Sinnlich-Übersinnliche in seiner Verwirklichung durch die Kunst», München, 15. und 17.",
        "Februar 1918, und «Die Quellen der künst­lerischen Phantasie und die Quellen der übersinnlichen Erkenntnis», München, 5. und 6.",
        "Mai 1918, im Bande «Kunst und Kunsterkenntnis», Gesamtausgabe Dornach 1961."
      ],
      [
        "Alexander von Bernns, 1880-1965, Dichter.",
        "Gab von 1916 bis 1921 in Manchen die Vierteljshres-Zeitschrift «Das Reich» heraus.",
        "In seinem «Kunsthaus» «Das Reich» hielt Rudolf Steiner zeitweise seine Münchner Vorträge."
      ],
      [
        "15 IVooerow Wilson, 1856-1924, Präsident der USA von 1912 bis 1920.",
        "Verleladete am"
      ],
      [
        "Januar 1918 ein Friedensprogramm, die Vierzehn Punkte."
      ],
      [
        "17 ein Universiiätsprofessor: George Santayans, 1863-1952, englischer Philosoph spani­scher Abstammung.",
        "Kam schon 1872 nach Amerika, wo er bis 1912 blieb."
      ],
      [
        "Emile Boutroux, 1845-1921, französischer Philosoph.",
        "Ssntayar'a, «L'erreur dc la philosophie allemande».",
        "Paris 1917, préface d'Emile Boutroux."
      ],
      [
        "19 so weile Kreise, wie Mond, Sonne, Saturn: Es sind damit frühere Evolutionazustände des Erdplaneten gemeint, nicht die heute so genannten Weltkörper.",
        "Siehe «Die Ge­heimwissenschaft im Umriß», Gesamtausgabe Dornach 1962, Kapitel «Die Welt-entwickelung und der Mensch»."
      ],
      [
        "aus den vorjäbrigen Zürcher Vorträgen: «Anthroposophie und aleadernische Wissen­schaften», 4 Vorträge vom 5. bis 14.",
        "November 1917, Zürich 1950."
      ],
      [
        "Oskar Hertwig, 1849-1922, Anatom und Biologe.",
        "«Das Werden der Organismen, zur"
      ],
      [
        "Widerlegung von Darwins Zufsllstheorie durch das Gesetz in der Entwicklung»."
      ],
      [
        "ein kürzeres' Buch: «Zur Abwehr des ethischen, des sozialen und des politischen Darwinismus».",
        "Jens 1918."
      ],
      [
        "23 He,\"'ann von Helmboltz 1821-1894, Physiologe und Physiker.",
        "Erinder des Augen­spiegels, 1851."
      ],
      [
        "23/24 eine Schrift über die Freiheit: Woodrow Wilson, «Die neue Freiheit». 1913.",
        "Deutsche Übersetzung München 1914.",
        "«Nur Literatur, Betrachtungen eines Amerikaners» 1893.",
        "Deutsche Übersetzung 1913, darin der Essay «Der Verlauf amerikanischer Ge­schichte»."
      ],
      [
        "24 Herman Grimm, 18281901."
      ],
      [
        "26 Wladimir llfits'h Lenin, eigentlich Uljsnow, 1870-1924, führte 1917 die bolsehe­wittische Revolution durch."
      ],
      [
        "27 Karl Marx, 1818-1883.",
        "Begründer des wissenschaftlichen Sozialismus und Mitver­fasser des «Kommunistischen Manifests» 1848."
      ],
      [
        "31 in den Büchern, die Ihnen ja vorliegen: «Theosophie», Gesamtausgabe Dornach 1961, und «Die Geheimwissenschaft im Umriß», Gesamtausgabe Dornach 1962."
      ],
      [
        "32 «Ignorahimus»: Der Ausspruch des Berliner Physiologen Emil Du Bois-Reymond,"
      ],
      [
        "18181896, in seiner Rede «Über die Grenzen des Naturerkennens».",
        "Leipzig 1872."
      ],
      [
        "38 gilt das Wort: Aus Schiller «Der Taucher».",
        "Wörtlich: «Da unten aber ist's fürchter­lich, / Und der Mensch versuche die Götter nicht/ Und begehre nimmer und nimmer zu schauen, / Was sie gnädig bedecken mit Nacht und Grauen.»"
      ],
      [
        "42 hei unserer Gruppe drüben: Die plastische Gruppe des Menschheitarepräsentanten zwi­schen Luzifer und Ahriman."
      ],
      [
        "46 Ich habe öfter: Siehe den Vortrag vom 25.",
        "Juni 1918 in Berlin, im Bande «Erden-sterben und Weltenleben», Gesamtausgabe Dornach 1967."
      ],
      [
        "hier ja wohl auch schon: Im Vortrag vom 29.",
        "Juli 1916. im Bande «Das Rätsel des Menschen», Gesamtausgabe Dornach 1963."
      ],
      [
        "Otto Weininger, 1880-1903.",
        "«Über die letzten Dinge» 4.",
        "Auflage Wien und Leipzig 1918."
      ],
      [
        "Einer dieser Aphorismen: Wörtlich: «Aus unserem Zustand vor der Geburt ist viel­leicht darum keine Erinnerung möglich, weil wir so tief gesunken sind durch die"
      ],
      [
        "Geburt: wir haben das Bewußtsein verloren und gänzlich triebartig geboren zu wer­den verlangt, ohne vernünftigen Entschluß und ohne Wissen, und darum wissen wir gar nichts von dieser Vergangenheit.»"
      ],
      [
        "47 Und darüber schrieb er die Notiz: Wörtlich: «Ich morde mich selbst, um nicht einen andern morden zu müssen.»"
      ],
      [
        "48 Babindranath Tagore, 1861-1941, indischer Dichter und Philosoph."
      ],
      [
        "49 jenen Essay: «Der Verlauf amerikanischer Geschichte» in «Nur Literatur» von Woodrow Wilson."
      ],
      [
        "55 zwei Artikel gegen mich: Otto Zimmermann S.",
        "J.: Anthroposophische lirlehren, «Stimmen der Zeit», 48.",
        "Jg., 10.",
        "H., Juli 1918, S.328 ff., Joseph Kreitmaier S."
      ],
      [
        "«Vom Expressionismus», ebenda S. 356 ff."
      ],
      [
        "60 der griechische Weise: Platon, im 6.",
        "Buch vom «Staat»."
      ],
      [
        "63 Arthur Ba«oir, 18481930; 1916 Außenminister Großbritanniens.",
        "Honeton Stewart Chamberlain, 1855-1927."
      ],
      [
        "81 Sie werden einen Zweigvnrtrag finden: Vortrag vom 23.",
        "Mai 1916 in «Gegenwärtiges und Vergangenes im Menschengeiste», Gesamtausgabe Dornach 1962."
      ],
      [
        "82 kh habe das im vorigen Jahre hier ausgeführt: Siehe den Vortrag vom 14.",
        "Oktober 1917 in «Die spirituellen Hintergründe der äußeren Welt.",
        "Der Sturz der Geister der Finster­nis», Gesamtausgabe Dornach 1965."
      ],
      [
        "87 von der ande\"n Seite: Siehe den Vortrag vom 20.",
        "August 1918 (Zeichnung Seite 31) Sie erinnern sich an die Zeichnung: Auf Seite 31 dieses Bandes."
      ],
      [
        "«Von Seelenrätseln», Gesamtausgabe Dornach 1960.",
        "«Skizzenhafte Erweiterungan des Ir'haltes dieser Schrift: S.",
        "Über die wirkliche Grundlage der intentior'alen Be-ziehung»."
      ],
      [
        "92 Björnstierne Björnson, 1832-1910, norwegischer Dichter."
      ],
      [
        "93 Nero, regierte 54-68"
      ],
      [
        "94 Vespasianuc, regierte 69-79"
      ],
      [
        "Titns, regierte 79-81"
      ],
      [
        "Domitianus, regierte 81-96"
      ],
      [
        "Ners'a, regierte 96-98"
      ],
      [
        "Si,'tonius, schrieb im 1.Jahrhundert n.Chr.",
        "Kaiserbiographien."
      ],
      [
        "Tacitns, um 55 bis um 120, römischer Geschichtsschreiber."
      ],
      [
        "Flavius P.",
        "Philostratus der Altere, griechischer Sophist zu Ende des 2.",
        "Jahrhunderts n.Chr.",
        "Beschrieb das Leben des Apollonius von Tyana."
      ],
      [
        "Apollnnius von Tyana, Prophet und Wundertäter im 1.Jahrhundert n.Chr."
      ],
      [
        "der Tübinger Theologe Baur: Ferdinand Christian Baur, 1792-1860, protestantischer Theologe, «Apollonius von Tysna und Christus», Tübingen 1832."
      ],
      [
        "113 Sie können das in verschiedenen Zyklen lesen: Zum Beispiel in «Welt, Erde und Mensch», Gesamtausgabe Dornach 1960; «Ägyptische Mythen und Mysterien», Gesamtaus­gabe Dornach 1960."
      ],
      [
        "117 Augustus, 63 v.Chr. bis 14 n.Chr., erster römischer Kaiser, Caesar Augustus"
      ],
      [
        "119 im «Reich»: In der Vierteljahresachrift «Das Reich».",
        "München, 2.",
        "Jahr, Buch 3 und"
      ],
      [
        "4; 3.Jahr, Buch 1, Oktober 1917 bis April 1918."
      ],
      [
        ": In «Philosophie und Anthroposo­phie», Gesamtausgabe Dornach 1965 und in Johann Valentin Andreae, «Die Chy­mische Hochzeit des Christian Rosenkreutz Anno 1459», ina Neuhochdeutache über­tragen von Walter Weber, Stuttgart 1957; beigefügt sind die Ausführungen Rudolf Steiners in der Zeitschrift «Das Reich», Verlag Freiea Geistesleben, Stuttgart 1957."
      ],
      [
        "Johann Valentin Andreae, 1586-1654, Dichter und theologischer Schriftsteller."
      ],
      [
        "«Allgemeine Reformation der ganzen weiten Weil>: Nach W.Weber (s o.) Seite 181 ist dieses Werk die Übersetzung eines Kapitels aus Boecalnis «Ragguali di Parnasso», Venedig 1612."
      ],
      [
        "«Bewegung für ethitehe Kultur»: Vgl. hier:':a Rudolf Steiner, «Mein Lebeosgang», Kap.",
        "XVII."
      ],
      [
        "120 «Dic Zukunft>, Wochensehrift, herausgegeben von Maximilian Harden (eig­Witkowski), 1861-1927.",
        "In «Gesamn,elte Aufsätze zur Kulturgeschichte 1887-1901», Gesamtausgabe Dornach 1966."
      ],
      [
        "was kh dann das soziale Karzinom genannt babe: Im Vortragazyklus"
      ],
      [
        "121 Wladimir Iljitsch Lenin: Siehe Hinweise zu Seite 26.",
        "Karl Marx: Siehe Hinweise zu Seite 27."
      ],
      [
        "Ferdinand Lassalle, 1825-1864, sozialistischer Führer."
      ],
      [
        "Edaard Ber\"stein, 1850-1932, sozialistischer Theoretiker, der Begründer des Revisio­nismus."
      ],
      [
        "123 Carl Freiherr du Pre4 1839-1899.",
        "«Das Rätsel des Menschen».",
        "Leipzig 1892."
      ],
      [
        "127 Julius Robert Mayer, 1814-1878, Arzt und Physiker."
      ],
      [
        "129 «Philosophie und Anthroposophic»: Sonderdruck aus dem gleichnamigen Band der Ge­samtausgabe, Dornach 1964."
      ],
      [
        "in der Mittelpunktsgruppe des Baues: Holzgruppe, den Menschheitsrepräsentanten, Christus, zwischen Luzifer und Ahriman darstellend."
      ],
      [
        "130 Ich habe über dic Entwickelung der Christuc- Gestalt ja öfter hier geprochen: Zum Beispiel am 29.",
        "Oktober 1917, 13.",
        "Vortrag in «Kunstgeschichte als Abbild innerer geistiger Impulse», Dornach 1957."
      ],
      [
        "132 Pythagoras, etwa 582 v.Chr."
      ],
      [
        "132 daß in Urzeiten der Merkur mit dem Monde einmal Seharh gespielt hat: Diese Erzählung findet sich bei Plutarch in «Über Isis und Osiris»."
      ],
      [
        "eines solehen agy ptischen Weiten: Plutarch nennt den Priester Oinuphis von Heliopolis als Lehrer des Pythagoras."
      ],
      [
        "133 Jakob Böhme, 1575-1624."
      ],
      [
        "134 Max Müller, 1823-1900, Sanskrit- und Religionaforscher in Oxford.",
        "Charles Darwin, 1809-1882, englischer Naturforscher."
      ],
      [
        "Ernst Ha'ckel, 1834-1919, Zoologe."
      ],
      [
        "142 Wir haben Zyklen nur abgegeben an die Mitglieder der Gesellschaft: Diese Beschränkung wurde an der Weihnachtstagung 1923 aufgehoben."
      ],
      [
        "144 tiefstgehende Einflüsse eines Menschen: des Apollonius von Tyana."
      ],
      [
        "148 als fünf Vokale: Jehova (v = u)."
      ],
      [
        "156 Sybaris: Stadt in Unteritalien, gegründet 700 v.Chr., im Altertum sprichwörtlich durch die Schwelgerei ihrer Bewohner."
      ],
      [
        "169 Immanuel Kant, 1724-1804.",
        "«Kritik der reinen Vernunft» 1781."
      ],
      [
        "173 Robert Zimmermann, 1824-1898, Ästhetiker und Philosoph.",
        "«Anthroposophie im Umriß» Wien 1882, S. 307 f."
      ],
      [
        "174 Augnste Gomte, 1798-1857, französischer Philosoph.",
        "Begründer des Positivismus und der Soziologie."
      ],
      [
        "Friedrich Schiller, 1759-1805."
      ],
      [
        "Friedrich Schleiermacher, 176818M, evangalischer Theologe, Prediger und Philosoph."
      ],
      [
        "175 in den Schlußnotizen: «Von Seelertratseln», Gesamtausgabe Dornach 1960, Kapitel IV,"
      ],
      [
        "«Die physischen und die geistigen Abhängigkeiten der Menschen-Wesenheit»."
      ],
      [
        "176 in den Rosenkreuzerbildern: «Die geheimen Figuren der Rosenkreuzer»."
      ],
      [
        "186 Alexander von Be\"nus: Siehe Hinweis zu Seite 12."
      ],
      [
        "die Zeitschrift, die er gegründet hat: Siehe Hinweis zu Seite 12. in seinem Kunethans: Siehe Hinweis zu Seite 12."
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
