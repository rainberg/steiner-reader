#!/usr/bin/env python3
"""Standalone import script for GA135 — GA135 - Wiederverkörperung und Karma"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA135 - Wiederverkörperung und Karma"""
GA_NUMBER = "GA135"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG Berlin, 23.Januar 1912",
    "paragraphs": [
      "An die Bemerkungen, die wir über die geistigen Tatsachen und Wesen­heiten der höheren Welten machen konnten und die durch unsere Ge-neralversammlungszeit unterbrochen worden sind, wird sich nunmehr gut einiges anschließen lassen, das uns Aufklärung geben kann über gewisse Dinge, welche mit der gegenwärtigen Entwickelung des Men­schen zusammenhängen. Während also die Betrachtungen, die wir im Herbst gepflogen haben, uns mehr in die Vorgänge gewissermaßen innerhalb der höheren Hierarchien führen sollten, wollen wir heute einiges betrachten, das uns wie so recht menschliche Angelegenheiten naheliegen kann.",
      "Es wird sich gewiß der Mensch, welcher sich eine Weile mit Anthro­posophie beschäftigt hat, und der namentlich die Grundanschauungen von Reinkarnation und Karma und der übrigen Wahrheiten der Menschheit und ihrer Entwickelung aufgenommen hat, leicht fragen:",
      "Warum kommt man denn gar so schwer zu einer unmittelbaren, wirk­lichen Anschauung jener Wesenheit im Menschen, die durch die wie­derholten Erdenleben hindurchgeht, jener Wesenheit des Menschen also, welche, wenn man sie nur einigermaßen genauer und immer genauer kennenlernen würde, ganz selbstverständlich führen müßte auch zu einer Einsicht in die Geheimnisse der wiederholten Erden-leben und eben auch des Karma?",
      "Nun muß allerdings gesagt werden: Alles, was gerade mit dieser Frage zusammenhängt, greift der Mensch gewöhnlich ganz verkehrt an. Zunächst sucht sich ja der Mensch, wie das nur allzu selbstver­ständlich ist, über diese Dinge auch aufzuklären durch die gewöhn­liche Gedankenwelt, durch den gewöhnlichen Verstand, und er fragt sich: Inwiefern kann man aus den Tatsachen des Lebens heraus An­haltspunkte gewinnen dafür, daß die Anschauung von den wieder­holten Erdenleben und von dem Karma eine richtige ist?",
      "Nun wird der Mensch zwar bis zu einem gewissen Punkte mit einem solchen Bestreben kommen können, das im wesentlichen auf Nachdenken",
      "fußt; aber er wird damit eben doch nur bis zu einem gewissen Punkte kommen können. Denn unsere Gedankenwelt ist eigentlich, so wie sie einmal beschaffen ist, ganz und gar abhängig von jenen Ein-richtungen innerhalb unserer Gesamtorganisation als Menschen, die eigentlich bloß auf die eine Inkarnation beschränkt ist, die wir dadurch erhalten, daß wir eben so, wie wir als Menschen zwischen Geburt und Tod leben, diese bestimmte Organisation zugeteilt erhalten.",
      "Und von dieser Organisation, ja, geradezu von der besonderen Ausgestaltung des physischen Leibes und des ja nur um eine Stufe über den physischen Leib hinausragenden Ätherleibes, ist alles abhängig, was wir unsere Gedankenwelt nennen können. Und je scharfsinniger im Grunde ge­nommen diese Gedanken sind, je mehr sie sich einlassen können auf abstrakte Wahrheiten, desto mehr sind diese Gedanken abhängig von der äußeren, nur auf eine Inkarnation beschränkten Organisation des Menschen.",
      "Wir können das schon daraus entnehmen, daß wir, was ja öfter gesagt worden ist, in das Leben zwischen dem Tode und einer neuen Geburt, also in das geistige Leben hinein, von alledem, was wir in der Seele erleben, am allerwenigsten unsere Gedanken mitnehmen können. Also das, was wir am allerscharfsinnigsten ausdenken, müssen wir am allermeisten zurücklassen.",
      "Man könnte förmlich sagen: Was legt denn der Mensch ab, wenn er durch die Pforte des Todes schreitet? Nun, zunächst seinen physischen Leib. Aber von alledem, was nun innerlich ist, legt der Mensch fast ebenso umfänglich, restlos alles ab, was er an abstrakten Gedanken in seiner Seele ausgestaltet hat.",
      "Diese zwei Dinge, physischer Leib und abstrakte Gedanken, ja, geradezu wissenschaftliche Gedanken, kann der Mensch am allerwenigsten mit­nehmen, wenn er durch die Pforte des Todes schreitet. Der Mensch nimmt gewissermaßen leicht mit seine Neigungen, seine Triebe, Be­gierden, wie sie sich herangebildet haben, insbesondere seine Gewohn­heiten, nimmt auch mit die Art und Natur seiner Willensimpulse, aber am allerwenigsten seine Gedanken.",
      "Daraus schon, weil die Gedanken so sehr gebunden sind an die äußere Organisation, kann geschlossen werden, daß sie auch kein Werkzeug sind, das sehr geeignet ist, um einzudringen in die Geheim­nisse von Reinkarnation und Karma, welche ja Wahrheiten sind, die",
      "über die einzelne Inkarnation hinausgehen. Aber bis zu einem gewis­sen Punkte kann man dennoch kommen, und bis zu einem gewissen Punkte muß man sogar das Denken ausbilden, wenn man theoretisch Reinkarnation und Karma einsehen will. Was darüber gesagt werden kann, das ist im Grunde genommen alles gesagt entweder in dem Kapitel über Reinkarnation und Karma in der «Theosophie» oder in der kleinen Schrift «Reinkarnation und Karma, vom Standpunkte der modernen Naturwissenschaft notwendige Vorstellungen». Man wird kaum viel hinzufügen können zu dem, was in diesen beiden Schriften gesagt ist.",
      "Was der Intellekt hinzufügen kann, diese Frage soll uns heute nicht weiter beschäftigen, sondern vielmehr die Frage: Wie kann nun der Mensch zu einer gewissen Anschauung von Reinkarnation und Karma doch kommen, das heißt zu einer Anschauung, die mehr wert ist als eine bloße theoretische Überzeugung, die eine Art innerer Gewißheit geben kann, daß der eigentliche geistig-seelische Wesenskern in uns von früheren Leben herüberkommt und zu späteren Leben hinüber-geht?",
      "Man kommt zu einer solchen bestimmten Anschauung dadurch, daß man innerliche Dinge ausführt, welche keineswegs leicht sind, welche schwierig sind, aber die deshalb doch immerhin ausgeführt werden können. Der erste Schritt, den man da machen kann, ist, daß man die gewöhnliche Art von Selbsterkenntnis ein wenig übt, die Art, die darin bestehen kann, daß der Mensch gewissermaßen auf sein Leben zurückblickt, so zurückblickt, daß er sich fragt: Was bin ich denn überhaupt für ein Mensch gewesen? Bin ich ein Mensch gewesen mit einer starken Neigung zum Nachdenken, zu einem innerlich nachsin­nenden Wesen, oder bin ich ein Mensch gewesen, der stets mehr die Sensationen der Außenwelt geliebt hat, dem dieses oder jenes im Leben gefallen oder nicht gefallen hat? Bin ich ein Mensch gewesen, der in der Schule gern lesen, aber nicht gern rechnen wollte, der die anderen Kinder gern geschlagen hat, aber sich nicht gern hat schlagen lassen? Oder bin ich vielleicht ein Kind gewesen, das immer dazu bestimmt war, eins abzukriegen, und das nicht schlau genug gewesen ist, die anderen eins abkriegen zu lassen? - In dieser Weise ein wenig zurückzublicken",
      "auf sein Leben und insbesondere sich zu fragen: Wozu war ich - in intellektueller Weise oder in derjenigen Weise, die auf die Gemütsstimmungen oder auf die Willensimpulse bezüglich ist -besonders veranlagt? Was ist mir leicht, was ist mir schwierig ge­worden? Was hat mich so getroffen, daß ich ihm gern habe entfliehen wollen? Was hat mich so getroffen, daß ich mir gesagt habe: Es ist mir recht, daß es so gekommen ist und so weiter -, so also auf sein Leben in einer gewissen Weise zurückzublicken, das ist gut zu einer intimeren Erkenntnis seines geistig-seelischen Wesenskernes; vor allem alles das klar vor die Seele zu stellen, was zu dem gehört, was man eigentlich nicht gern gewollt hat. So zum Beispiel, ob man ein Sohn gewesen ist, der vielleicht gern ein Dichter geworden wäre, der von seinem Vater aber zum Handwerker bestimmt worden ist und auch ein Handwerker hat werden müssen, trotzdem er es nie so recht hat werden wollen; er ist es geworden, wäre aber lieber ein Dichter gewor­den. So sich klarmachen, was man eigentlich hat werden wollen, was man aber gegen seinen Willen geworden ist, dann sich klarmachen, was einem gepaßt hat im Jugendleben und was einem nie zuteil geworden ist. Dann weiter sich klarmachen, woraus man so recht hätte heraus­kommen wollen, welchem man so recht hätte entfliehen wollen. Ich bemerke, daß dies, was ich jetzt sage, sich auf das Leben in der Ver­gangenheit beziehen soll, nicht auf die Zukunft; das wäre eine falsche Vorstellung.",
      "Also man soll sich im Grunde genommen klarmachen, was einem ein solcher Rückblick in die Vergangenheit sagt: was man nicht hat wollen, welchem man hat entfliehen wollen und so weiter. Wenn man sich das klargemacht hat, dann hat man eigentlich ein Bild derjenigen Dinge in seinem Leben, die einem so recht am wenigsten gefallen. Darum handelt es sich aber gerade, daß man die Dinge in seinem Le­ben herausbekommt, die einem in der Vergangenheit am wenigsten gefallen haben. Und man muß nun versuchen, sich ganz einzuleben in eine höchst merkwürdige Vorstellung: Alles das, was man nun eigent­lich nicht gewollt und gewünscht hat, energisch zu wollen und zu wün­schen! Also energisch einmal sich vor die Seele stellen: Wie wärest du eigentlich, wenn du lebendig, heftig alles das gewünscht hättest, was",
      "du eigentlich nicht gewünscht hast, was dir im Grunde genommen im Leben gegen den Strich gegangen ist? - Ausschalten muß man dabei in einer gewissen Weise dasjenige, was einem zu überwinden gelungen ist. Denn das allerwichtigste ist, daß man diejenigen Dinge wünscht, oder sich so vorstellt, als ob man sie lebhaft wünschen würde, die man nicht gewünscht hat, oder denen gegenüber man seine Wünsche nicht hat durchsetzen können, so daß man sich in der Empfindung, in Ge­danken ein Wesen schafft, von dem man die Vorstellung haben kann, daß man es im Grunde genommen bisher gar nicht gewesen ist. Und jetzt stelle man sich vor, daß man eigentlich gerade dieses Wesen mit aller Vehemenz, mit aller Intensität gewesen wäre. Wenn man sich das vorstellt, wenn es einem gelingt, sich zu identifizieren mit diesem Wesen, das man auf diese Weise sich selber sozusagen einkonstruiert hat, dann hat man schon wesentlich etwas gewonnen auf dem Wege, seinen inneren seelischen Wesenskern kennenzulernen. Denn es wird einem gerade an dem Bilde, das man sich nun von seiner Eigenpersön­lichkeit in der geschilderten Weise machen kann, etwas aufgehen, was man in der gegenwärtigen Inkarnation nicht ist, was man aber her­eingebracht hat in die gegenwärtige Inkarnation. Sein tieferes Wesen wird einem aufgehen an dem Bilde, das man sich auf diese Weise konstruiert.",
      "Es wird also von dem, der zu seinem inneren Wesenskern kommen will, im Grunde genommen etwas verlangt, was die Menschen in un­serer Gegenwart am allerwenigsten tun. Unsere Gegenwart ist gar nicht dazu veranlagt, auch nur in einer gewissen Weise so etwas her­beizusehnen, was dem ähnlich ist, was jetzt gefordert worden ist; denn in unserer Gegenwart streben eigentlich die Menschen, wenn sie über sich selber nachdenken, am allermeisten danach, sich so, wie sie sind, absolut richtig zu finden. Wenn wir zurückgehen in frühere Zeiten einer noch religiöseren Entwickelung, dann finden wir das Gefühl, daß der Mensch sich zerknirscht empfinden soll, da er so wenig dem ent­spricht, was er als sein göttliches Vorbild bezeichnen kann. Das war zwar nicht die Vorstellung, von der heute gesprochen worden ist, aber es war die Vorstellung, welche von dem, womit der Mensch gewöhn­lich zufrieden ist, abführte und zu etwas anderem hinführte - wenn",
      "auch nicht zu der Überzeugung von einer anderen Inkarnation -, nämlich zu jenem Wesen hinführte, das über unsere Organisation, wie sie sich zwischen Geburt und Tod herausbildet, hinüberlebt. Es wird einem folgendes aufgehen, wenn man das Gegenbild von dem zeich­net, was man ist: Dieses Gegenbild, so schwer es dir geworden ist, es in diesem Leben als dein Bild zu fassen, es hat doch etwas mit dir zu tun; das kannst du nicht leugnen. Wenn du es hast, wird es dich ver­folgen, wird es dir vor der Seele schweben und sich so zusammen­kristallisieren, daß du dir sagen wirst: Dieses Bild hat etwas mit mir zu tun, aber ganz gewiß nicht mit meinem jetzigen Leben. - Dann bildet sich die Empfindung heraus, daß dieses Bild gerade aus einem früheren Leben stammt.",
      "Wenn wir dies uns vor die Seele führen, werden wir bald gewahr werden, wie irrtümlich die meisten Vorstellungen sind, die man sich gewöhnlich über Reinkarnation und Karma bildet. Sie werden es selbst schon gehört haben: wenn einem irgendwo ein Mensch im Leben entgegentritt, der zum Beispiel ein guter Rechner ist, und wenn man dann zugleich Anthroposoph ist, dann wird man sich leicht die Vor­stellung bilden: In der vorhergehenden Inkarnation ist dieser Mensch ein guter Rechner gewesen.",
      "Viele Reinkarnationsketten werden leider von unausgebildeten Anthroposophen in der Weise aufgestellt, daß man einfach glaubt, die vorhergehende Inkarnation dadurch zu fin­den, daß man die Fähigkeiten, die in der gegenwärtigen auftreten, auch in der vorhergehenden oder womöglich in mehreren vorhergehenden Inkarnationen wird finden müssen. Das ist die schlechteste Art, zu spe­kulieren.",
      "Man trifft gewöhnlich damit das Falsche. Denn die wirk­lichen Beobachtungen mit den Mitteln der Geisteswissenschaft zeigen zumeist das genaue Gegenteil. Leute zum Beispiel, die in der vorher­gehenden Inkarnation gute Rechner, gute Mathematiker waren, treten in der gegenwärtigen Inkarnation so auf, daß sie gar keine Begabung für Mathematik zeigen, daß ihnen die mathematische Begabung fehlt.",
      "Und will man wissen, welche Begabungen man höchstwahrscheinlich in der vorigen Inkarnation hatte - ich mache darauf aufmerksam, daß wir jetzt also auf dem Boden der Wahrscheinlichkeit stehen -, will man wissen, welche Fähigkeiten in dieser Richtung an Intelligenz,",
      "künstlerischen Dingen und so weiter man in der vorigen Inkarnation gehabt hat, so tut man gut, wenn man nachdenkt, wozu man in dieser Inkarnation am allerwenigsten Fähigkeiten hat, wozu man in dieser Inkarnation sich am allerwenigsten eignet. Wenn man das heraus­bekommen hat, dann wird man finden, worin man wahrscheinlich in der vorhergehenden Inkarnation brilliert hat, wofür man ganz be­sonders begabt war.",
      "Ich sage «wahrscheinlich» aus dem Grunde, weil diese Dinge auf der einen Seite wahr sind, aber auf der anderen Seite vielfach durchkreuzt werden von anderen Tatsachen. Da kann zum Beispiel der Fall eintreten, daß einer eine besondere mathematische Begabung in der vorhergehenden Inkarnation hatte, aber früh gestor­ben ist, so daß diese mathematische Begabung nicht ganz zum Ausdruck gekommen ist; dann wird er in seiner nächsten Inkarnation wieder mit einer mathematischen Begabung geboren werden, die sich dann wie eine Fortsetzung aus der vorhergehenden Inkarnation darstellen wird.",
      "Der früh verstorbene Mathematiker Abel wird ganz gewiß in seiner nächsten Inkarnation mit einer starken mathematischen Begabung wiedergeboren werden. Wo dagegen ein Rechner besonders alt gewor­den ist, wo sich diese Begabung ausgelebt hat, da wird der Betreffende in seiner nächsten Inkarnation geradezu stumpfsinnig sein in bezug auf Mathematik.",
      "So ist mir eine Persönlichkeit bekannt, die so wenig mathematische Begabung hatte, daß sie als Schulbube geradezu die Ziffern haßte; und während der Betreffende in den anderen Fächern gute Zensuren hatte, war es überhaupt nur dadurch möglich, daß er die Schulklassen durchmachen konnte, daß man ihm in den anderen Fächern besonders gute Zensuren ausstellte. Das rührte davon her, daß er in der vorhergehenden Inkarnation ein besonders guter Mathe­matiker gewesen ist.",
      "Wenn man weiter darauf eingeht, dann stellt sich die Tatsache her­aus, daß das, was man in einer Inkarnation äußerlich treibt, das heißt, was man nicht allein äußerlich treibt, sondern was man für einen äußerlichen oder innerlichen Beruf hat, in der nächsten Inkarnation in die innere Organbildung eingeht, zum Beispiel in der Weise, daß man, wenn man in einer Inkarnation ein besonders guter Mathematiker war, dasjenige, was man sich da angeeignet hat an Zahlen- und Figurenbeherrschung,",
      "mitgenommen und hineingearbeitet hat in eine be­sondere Ausarbeitung seiner Sinnesorgane, zum Beispiel der Augen. Und Menschen, die sehr gut sehen, haben diese sorgfältige Ausbildung der Formen des Auges davon, daß sie in der vorhergehenden Inkar­nation in Formen gedacht und dieses Denken in Formen mitgenommen haben und, indem sie durch die Zeit zwischen Tod und neuer Geburt geschritten sind, ihre Augen besonders ausziseliert haben. Da ist die mathematische Begabung ins Auge hineingeflossen und lebt sich nicht mehr in mathematischer Begabung aus.",
      "Ein anderer den Okkultisten bekannter Fall ist der, wo eine In­dividualität in einer Inkarnation besonders intensiv in Architektur-formen lebte: was sie da empfunden hat, das lebte sich ein als Kräfte in das innere Seelenleben und ziselierte besonders fein aus das Gehör-werkzeug, so daß diese Individualität in der nächsten Inkarnation ein großer Musiker wurde. Sie wurde nicht ein großer Architekt, weil die Empfindungsformen, die sich an die Architektur anlehnten, organauf-bauend wurden, so daß nichts übrigblieb, als in hohem Maße Musik zu empfinden.",
      "Eine äußere Betrachtung der Ähnlichkeiten täuscht in der Regel über das, was Eigentümlichkeiten in den aufeinanderfolgenden Inkar­nationen sind. Und wie wir nachdenken müssen über das, was uns nicht gefallen hat und uns vorstellen müssen, als ob wir es intensiv wünschten, so sollen wir auch nachdenken über die Dinge, zu denen wir am wenigsten befähigt sind, in denen wir sozusagen ganz stumpf­sinnig sind. Und wenn wir die allerstumpfsinnigsten Seiten unseres Wesens entdecken, dann können sie uns mit größter Wahrscheinlich­keit zu dem führen, worin wir in der vorhergehenden Inkarnation am allermeisten geglänzt haben. Daraus sehen wir, daß es naheliegt, gerade diese Dinge am falschen Ende anzufangen. Wie uns im übrigen auch ein gewisses Nachdenken darüber belehren kann, daß es eben der in­nerste seelische Wesenskern ist, der von einer Inkarnation in die andere hinüberlebt, das zeigt zum Beispiel die Erwägung, daß der Mensch Sprachen doch niemals dadurch leichter lernt, daß er in einer vorher­gehenden Inkarnation etwa in einem Sprachgebiete gelebt hat, das mit der betreffenden Sprache, die er jetzt lernen soll, zusammenhing;",
      "denn sonst würden es unsere Gymnasiasten nicht gar so schwer haben, Griechisch oder Lateinisch zu lernen, obwohl viele in ihren früheren Inkarnationen in einem Gebiete gelebt haben, wo sie diese Sprachen als die gewöhnlichen Umgangssprachen gesprochen haben.",
      "Von dem, was wir äußerlich an uns heranbringen, müssen wir sagen, daß es so sehr verbunden ist mit dem, was sich abschließt in dem Leben des Menschen zwischen Geburt und Tod, daß gar nicht davon die Rede sein kann, daß diese Dinge in der nächsten Inkarnation in derselben Weise wiedererscheinen, sondern daß sie in Kräfte umge­wandelt in die nächste oder nächsten Inkarnationen übergehen. Die­jenigen Menschen, die zum Beispiel in einer Inkarnation eine beson­dere Anlage haben zum Sprachen erlernen, werden diese Anlage in ihrer nächsten Inkarnation nicht haben; dafür aber werden sie die Anlage haben, zu mehr unbefangenem Urteilen als die übrigen Men­schen.",
      "Das sind Dinge, die mit den Geheimnissen der Reinkarnation zu­sammenhängen. Und gerade wenn man auf diese Geheimnisse der Re­inkarnation blickt, wird man in der intensivsten Weise eine Vorstel­lung bekommen von dem, was eigentlich wirklich im Menschen in­nerlich ist, und was in einer gewissen Weise doch zu den Äußerlich­keiten gerechnet werden muß. Zum Beispiel ist für den gegenwärtigen Menschen die Sprache durchaus nicht mehr innerlich. Man kann die Sprache um dessentwillen, was sie ausdrückt, um des Volksgeistes wil­len lieben; aber sie ist etwas, was in umgewandelten Kräfteformen von einer Inkarnation in die andere übergeht.",
      "Wenn der Mensch solche Dinge verfolgt, daß er auf der einen Seite sagt: Ich will einmal recht sehr wünschen und wollen, was ich doch gegen meinen Willen geworden bin und wofür ich am wenigsten Ver­anlagung habe - dann kann er wissen: Es werden sich mir die Vor­stellungen, die ich da gewinne, zusammenformen zu dem Bilde meiner vorhergehenden Inkarnation. - Dieses Bild der vorhergehenden In­karnation wird sich mit einer großen Bestimmtheit schon ergeben, wenn man Ernst macht mit denjenigen Dingen, die jetzt einmal etwas genauer charakterisiert worden sind. Man wird nämlich tatsächlich merken, daß man an der ganzen Art und Weise, wie sich einem die",
      "Vorstellungen, die man so gewonnen hat, zusammenfügen, empfinden wird: Dieses Bild ist mir eigentlich ziemlich nahe; es ist gar nicht weit von mir. Oder man wird fühlen: Es ist ein Bild weit, weit weg von mir.",
      "Wenn man nämlich durch die Ausarbeitung der Vorstellungen, die heute geschildert worden sind, ein solches Bild seiner vorhergehenden Inkarnation sich vor die Seele gemalt hat, dann wird man in der Regel abschätzen können, wie stark verblaßt dieses Bild ist. Man wird das Gefühl haben wie aus einer Empfindung heraus: Du stehst hier; dein Vater, dein Großvater, dein Urgroßvater können nicht das Bild sein, das da vor dir steht. - Wenn man aber das Bild auf sich wirken läßt, dann bekommt man in der Tat durch Gefühl und Empfindung die Meinung: So und so viele Personen stehen zwischen dir und diesem Bilde! - Nehmen wir einmal an, man bekommt dieses Gefühl - und ein solches stellt sich heraus -, zwischen einem selbst und diesem Bilde stünden zwölf Personen, und ein anderer bekäme das Gefühl, zwischen ihm selbst und dem Bilde stünden sieben Personen.",
      "Ein solches Gefühl aber bekommt man, und dieses Gefühl ist außerordentlich wichtig. Denn wenn zum Beispiel zwölf Personen zwischen einem selbst und diesem Bilde stehen, so braucht man nur durch drei zu dividieren und würde dann vier herausbekommen.",
      "Das sind dann in der Regel die Jahrhunderte, die einen von der vorhergehenden Inkarnation trennen. Also ein Mensch, der das Gefühl haben würde, daß er von dem Bilde, das ich seiner Entstehung nach geschildert habe, um zwölf Menschen entfernt ist, daß es um zwölf Personen über ihm ist, er müßte sich sagen: Meine vorhergehende Inkarnation fällt vier Jahrhunderte vor die jetzige. - Das ist nur als ein Beispiel angeführt; es wird in den wenigsten Fällen so sein, aber man kommt dadurch zu einer Schätzung.",
      "Die meisten werden finden, daß sie auf diese Weise richtig abschätzen können, wann sie vorher dagewesen sind. Nur sind die Voraussetzun­gen dazu natürlich etwas schwierig.",
      "Damit haben wir eigentlich Dinge berührt, welche dem Gegen­wartsbewußtsein ja so ferne wie möglich liegen. Und es ist ganz und gar nicht zu bezweifeln, daß, wenn irgend jemand diese Dinge Leuten erzählte, die dafür unvorbereitet sind, sie dann finden werden, daß das ja wirklich unverantwortliche Phantastereien sind. Nun ist es",
      "schon einmal das Schicksal der anthroposophischen Weltanschauung, daß sie von allen bisherigen Weltanschauungen am allerallermeisten in einer gewissen Weise sich entgegenstellen muß dem, was das Herge­brachte ist. Denn das Hergebrachte ist im weitesten Umfange, wie es einem entgegentritt, der krasseste, der ödeste Materialismus. Und ge­rade da, wo uns gewisse Weltanschauungen so entgegentreten, als ob sie am allerfestesten auf dem Boden wissenschaftlicher Weltanschauung ständen, da sind sie tatsächlich so, daß sie am ödesten aus einer ge­wissen materialistischen Grundanschauung herauswachsen. Da nun die Anthroposophie dazu verurteilt ist, in einer gewissen Weise selber für die große Welt der Weltanschauungen das zu sein, was heute ver­langt worden ist für den Menschen, der eine Vorstellung bekommen soll von seiner vorhergehenden Inkarnation, so kann es begreiflich erscheinen, daß es dem gegenwärtigen Menschen sehr ferne liegen muß, anthroposophische Anschauungen ernst zu nehmen. Denn die Men­schen werden ebenso abgeneigt sein, zu wünschen und zu wollen, was sie ihr Leben lang nicht gewünscht und gewollt haben, wie ihren Denk-gewohnheiten ferne liegen die spirituellen Wahrheiten.",
      "Nun könnte man die Frage aufwerfen: Warum tritt denn gerade jetzt die spirituelle Wahrheit unter die Menschen? Warum läßt sie nicht den Menschen Zeit, sich zu entwickeln, bis sie reifer sind?",
      "Das rührt davon her, daß auch wieder kaum ein größerer Unter­schied gedacht werden kann zwischen zwei aufeinanderfolgenden Menschheitsepochen, als er sein wird zwischen der Epoche, in der die gegenwärtige Menschheit lebt, und zwischen derjenigen, in welche die Menschheit hineinwachsen wird, wenn die jetzt lebenden Menschen wiedergeboren sein werden in der nächsten Inkarnation. Denn es hängt nicht von den Menschen ab, wie sich gewisse geistige Fähig­keiten herausbilden; das hängt ab von dem ganzen Sinn und der gan­zen Bedeutung und dem ganzen Wesen der Erdentwickelung. Die Menschen sind jetzt nämlich am weitesten davon entfernt, an Rein­karnation und Karma zu glauben. Nicht die Anthroposophen - aber Anthroposophen sind ja nur wenige in der Welt -, nicht die, welche noch alten Religionsformen angehören, sondern die, welche heute die Träger des äußeren Kulturlebens sind, die sind heute am allermeisten",
      "davon entfernt, an Reinkarnaüon und Karma zu glauben. Nun wird merkwürdigerweise gerade diese Tatsache, daß die Menschen heute am allerwenigsten geneigt sind, an Reinkarnation und Karma zu glauben, verbunden mit dem, was die Menschen heute treiben und lernen, näm­lich treiben und lernen, insofern dies in bezug auf intellektuelle Fähig­keiten eine Bedeutung hat - diese Tatsachen werden bewirken, daß bei diesen Menschen der Gegenwart in der nächsten Inkarnation das Gegenteil eintreten wird.",
      "Diese Menschen der Gegenwart werden in der nächsten Inkarnation - gleichgültig, ob sie spirituell oder mate­rialistisch streben - starke Anlage haben, ihre vorhergehende In­karnation zu empfinden. Ganz gleichgültig, was die Menschen der Gegenwart treiben: dadurch, daß sie Menschen der Jetztzeit sind, wer­den sie wiedergeboren werden mit einer starken Anlage und einer starken Sehnsucht, von der vorhergehenden Inkarnation etwas zu erfahren, etwas zu wissen.",
      "Wir stehen gerade an einer solchen Zeiten-wende, welche die Menschen führt von einer solchen Inkarnation, in der sie am allerwenigsten wissen wollen von Reinkarnation und Kar­ma, zu einer Inkarnation, in der in ihnen die lebendigste Empfindung sein wird: Das ganze Leben, das ich jetzt führe, steht für mich in der Luft, wenn ich nicht irgend etwas wissen kann über meine vorher­gehende Inkarnation. - Und die Menschen, welche jetzt am aller­meisten schimpfen über Reinkarnation und Karma, sie werden sich geradezu winden unter der Qual des nächsten Lebens, weil sie sich nicht erklären können, wie das Leben so hat werden können. Nicht um sich eine gewisse Rücksehnsucht nach dem vorhergehenden Leben anzueignen, wird jetzt Anthroposophie getrieben von den Menschen, sondern um Verständnis zu haben für das, was für die gesamte Mensch­heit einmal auftreten wird, wenn die Menschen, die heute leben, wieder da sein werden.",
      "Die Menschen, die heute Anthroposophen sind, werden die Anlage mit den anderen teilen, daß sie sich wieder erinnern wollen; aber sie werden Verständnis haben und dadurch innere Harmonie in bezug auf ihr Seelenleben. Die, welche heute die Anthroposophie zu­rückweisen, sie werden davon wissen wollen, und sie werden so etwas empfinden wie eine innere Qual nach etwas, was eben ihre vorher-gehende Inkarnation wäre im nächsten Leben; sie werden aber nichts",
      "verstehen von dem, was sie am allermeisten drückt und quält; sie werden ratlos sein, werden innerlich disharmonisch sein. Und es wird ihnen gesagt werden müssen in der nächsten Inkarnation: Du lernst erst erkennen, was dir Qualen verursacht, wenn du dir vorstellst, daß du eigentlich im Ernste diese Qual gewollt haben könntest. - Natür­lich werden alle Menschen diese Qual nicht wollen. Aber die Men­schen, die heute Materialisten sind, werden dann in der nächsten Inkarnation anfangen, ihre innere Zerknirschtheit, ihre innere Öde und Qual zu begreifen, wenn sie befolgen werden die Anforderungen, den Rat derer, die dann werden wissen können und ihnen sagen: Stellt euch einmal vor, dieses Leben, wie ihr es fliehen möchtet, das hättet ihr gewollt. - Wenn sie anfangen werden, diesen Rat zu befolgen, nachzudenken darüber: Wodurch kann ich dieses Leben gewollt haben? - dann werden sie sich sagen: Ach ja, da habe ich vielleicht gelebt in einer Inkarnation, in welcher ich gesagt habe: Was, ein an­deres, nächstes Leben oder Inkarnation soll auf dieses Leben folgen? Unsinn! Dummheit! Wie kann man so etwas glauben! Dieses Leben erfüllt sich in sich selber, ist in sich abgeschlossen; das sendet keine Kräfte in ein späteres hinüber! Ja, weil ich dazumal die Empfindung gehabt habe, ein folgendes Leben ist nichtig, ist unsinnig, dadurch ist es nichtig und unsinnig geworden! Ich habe gerade den Gedanken in mich hineingepflanzt als Kraft, der mir jetzt das Leben so öde und leer macht!",
      "Das wird ein richtiger Gedanke sein. So wird sich sozusagen kar­misch der Materialismus ausleben. Sinnvoll wird die nächste Inkarna­tion bei denjenigen Menschen sein, welche sich die Überzeugung ver­schafft haben, daß ihr Leben, wie es jetzt ist, eben nicht nur in sich erfüllt ist, sondern Ursachen enthält für das nächste. Unsinnig, leer und öde wird das Leben derer sein, die durch den Gedanken der Un­sinnigkeit der Reinkarnation sich selber das Leben öde und nichtig gemacht haben.",
      "So sehen wir, daß die Gedanken, die wir hegen, nicht etwa in einer gesteigerten Form in das nächste Leben hinübergehen, sondern um­gewandelt als Kräfte im nächsten Leben auftreten. In der geistigen Welt haben eben Gedanken, so wie sie jetzt sind im Leben zwischen",
      "Geburt und Tod, keine Bedeutung, sondern sie haben nur eine Bedeu­tung in einer umgewandelten Form. Wenn jemand zum Beispiel einen großen Gedanken hat, so kann dieser Gedanke noch so groß sein:",
      "wenn der Mensch durch die Pforte des Todes geht, ist der Gedanke als Gedanke fort. Aber der Enthusiasmus und die Empfindung und das Gefühl, das aufgelebt hat unter dem Einfluß des Gedankens, das geht durch die Pforte des Todes.",
      "Von der Anthroposophie selber nimmt der Mensch nicht die Gedanken mit, wohl aber das, was er an den Gedanken erlebt hat - bis in die Einzelheiten, nicht nur die all­gemeine Grundempfindung. Das ist das, was wir insbesondere fest­halten wollen: daß Gedanken als solche für den physischen Plan das eigentlich Bedeutungsvolle sind, und daß wir, wenn wir von der Wirkung des Gedankens für die höheren Welten sprechen, zugleich sprechen müssen von einer Umwandlung dieser Gedanken nach den höheren Welten hinauf.",
      "Gedanken, welche also eine Wiederverkörpe­rung leugnen, wandeln sich um in dem wiederverkörperten Leben in innere Nichtigkeit, in innere Leerheit des Lebens, und innere Nichtig­keit, innere Leerheit des Lebens wird als Qual, als Disharmonie empfunden. - Sie können sogar durch einen Vergleich eine Vorstel­lung bekommen, wie eine solche innere Nichtigkeit und Leerheit verlaufen muß, wenn Sie sich denken, daß Sie etwas recht gerne haben und es immer dann gern sehen, wenn Sie an einen bestimmten Ort kommen. Sie haben sich zum Beispiel gewöhnt, eine bestimmte Blume in einem Garten an einem bestimmten Ort blühen zu sehen.",
      "Wenn dann die Blume von ruchloser Hand abgeschnitten wird, wer­den Sie Schmerz empfinden. Wenn Sie etwas, was Sie lieben, nicht haben, wenn Ihnen das fehlt, dann empfinden Sie Schmerz. So ist es mit der Gesamtorganisation des Menschen.",
      "Wodurch empfindet der Mensch Schmerz? Wenn der Ätherleib und der Astralleib eines Organs immer an eine bestimmte Stelle des physischen Leibes eingeschaltet sind, und wenn dieses Organ einen Schnitt bekommt und verletzt wird, so können der Ätherleib und der Astralleib nicht gut eingreifen.",
      "Es ist das gerade so, wie wenn Ihnen durch den Schnitt von ruchloser Hand die Rose im Garten an der bestimmten Stelle abgeschnitten wird. Der Ätherleib und der Astralleib finden dann nicht, wenn ein",
      "Organ verletzt wird, was sie suchen; das wird dann als leiblicher Schmerz empfunden. So werden also die Gedanken, die sich der Mensch gemacht hat als fortwirkend in die Zukunft, ihm in der Zu­kunft entgegentreten. Dagegen werden sie ihm fehlen, und er wird nichts finden, wo er sie suchen wird an einem bestimmten Ort, wenn er nichts hinübersendet von Glauben und Erkenntniskräften in die nächste Inkarnation, und dann wird er dieses Fehlen von etwas an einem Orte als Schmerz und Qual empfinden.",
      "Dies sind Angaben, die uns von einer gewissen Seite den karmischen Verlauf gewisser Dinge klarlegen werden. Sie mußten gemacht wer­den, weil wir noch tiefer hineinsehen wollen in die Art und Weise, wie der Mensch noch weiter Veranstaltungen machen kann, um seinen eigentlichen geistig-seelischen Wesenskern zu erkennen."
    ],
    "sentences": [
      [
        "An die Bemerkungen, die wir über die geistigen Tatsachen und Wesen­heiten der höheren Welten machen konnten und die durch unsere Ge-neralversammlungszeit unterbrochen worden sind, wird sich nunmehr gut einiges anschließen lassen, das uns Aufklärung geben kann über gewisse Dinge, welche mit der gegenwärtigen Entwickelung des Men­schen zusammenhängen.",
        "Während also die Betrachtungen, die wir im Herbst gepflogen haben, uns mehr in die Vorgänge gewissermaßen innerhalb der höheren Hierarchien führen sollten, wollen wir heute einiges betrachten, das uns wie so recht menschliche Angelegenheiten naheliegen kann."
      ],
      [
        "Es wird sich gewiß der Mensch, welcher sich eine Weile mit Anthro­posophie beschäftigt hat, und der namentlich die Grundanschauungen von Reinkarnation und Karma und der übrigen Wahrheiten der Menschheit und ihrer Entwickelung aufgenommen hat, leicht fragen:"
      ],
      [
        "Warum kommt man denn gar so schwer zu einer unmittelbaren, wirk­lichen Anschauung jener Wesenheit im Menschen, die durch die wie­derholten Erdenleben hindurchgeht, jener Wesenheit des Menschen also, welche, wenn man sie nur einigermaßen genauer und immer genauer kennenlernen würde, ganz selbstverständlich führen müßte auch zu einer Einsicht in die Geheimnisse der wiederholten Erden-leben und eben auch des Karma?"
      ],
      [
        "Nun muß allerdings gesagt werden: Alles, was gerade mit dieser Frage zusammenhängt, greift der Mensch gewöhnlich ganz verkehrt an.",
        "Zunächst sucht sich ja der Mensch, wie das nur allzu selbstver­ständlich ist, über diese Dinge auch aufzuklären durch die gewöhn­liche Gedankenwelt, durch den gewöhnlichen Verstand, und er fragt sich: Inwiefern kann man aus den Tatsachen des Lebens heraus An­haltspunkte gewinnen dafür, daß die Anschauung von den wieder­holten Erdenleben und von dem Karma eine richtige ist?"
      ],
      [
        "Nun wird der Mensch zwar bis zu einem gewissen Punkte mit einem solchen Bestreben kommen können, das im wesentlichen auf Nachdenken"
      ],
      [
        "fußt; aber er wird damit eben doch nur bis zu einem gewissen Punkte kommen können.",
        "Denn unsere Gedankenwelt ist eigentlich, so wie sie einmal beschaffen ist, ganz und gar abhängig von jenen Ein-richtungen innerhalb unserer Gesamtorganisation als Menschen, die eigentlich bloß auf die eine Inkarnation beschränkt ist, die wir dadurch erhalten, daß wir eben so, wie wir als Menschen zwischen Geburt und Tod leben, diese bestimmte Organisation zugeteilt erhalten."
      ],
      [
        "Und von dieser Organisation, ja, geradezu von der besonderen Ausgestaltung des physischen Leibes und des ja nur um eine Stufe über den physischen Leib hinausragenden Ätherleibes, ist alles abhängig, was wir unsere Gedankenwelt nennen können.",
        "Und je scharfsinniger im Grunde ge­nommen diese Gedanken sind, je mehr sie sich einlassen können auf abstrakte Wahrheiten, desto mehr sind diese Gedanken abhängig von der äußeren, nur auf eine Inkarnation beschränkten Organisation des Menschen."
      ],
      [
        "Wir können das schon daraus entnehmen, daß wir, was ja öfter gesagt worden ist, in das Leben zwischen dem Tode und einer neuen Geburt, also in das geistige Leben hinein, von alledem, was wir in der Seele erleben, am allerwenigsten unsere Gedanken mitnehmen können.",
        "Also das, was wir am allerscharfsinnigsten ausdenken, müssen wir am allermeisten zurücklassen."
      ],
      [
        "Man könnte förmlich sagen: Was legt denn der Mensch ab, wenn er durch die Pforte des Todes schreitet?",
        "Nun, zunächst seinen physischen Leib.",
        "Aber von alledem, was nun innerlich ist, legt der Mensch fast ebenso umfänglich, restlos alles ab, was er an abstrakten Gedanken in seiner Seele ausgestaltet hat."
      ],
      [
        "Diese zwei Dinge, physischer Leib und abstrakte Gedanken, ja, geradezu wissenschaftliche Gedanken, kann der Mensch am allerwenigsten mit­nehmen, wenn er durch die Pforte des Todes schreitet.",
        "Der Mensch nimmt gewissermaßen leicht mit seine Neigungen, seine Triebe, Be­gierden, wie sie sich herangebildet haben, insbesondere seine Gewohn­heiten, nimmt auch mit die Art und Natur seiner Willensimpulse, aber am allerwenigsten seine Gedanken."
      ],
      [
        "Daraus schon, weil die Gedanken so sehr gebunden sind an die äußere Organisation, kann geschlossen werden, daß sie auch kein Werkzeug sind, das sehr geeignet ist, um einzudringen in die Geheim­nisse von Reinkarnation und Karma, welche ja Wahrheiten sind, die"
      ],
      [
        "über die einzelne Inkarnation hinausgehen.",
        "Aber bis zu einem gewis­sen Punkte kann man dennoch kommen, und bis zu einem gewissen Punkte muß man sogar das Denken ausbilden, wenn man theoretisch Reinkarnation und Karma einsehen will.",
        "Was darüber gesagt werden kann, das ist im Grunde genommen alles gesagt entweder in dem Kapitel über Reinkarnation und Karma in der «Theosophie» oder in der kleinen Schrift «Reinkarnation und Karma, vom Standpunkte der modernen Naturwissenschaft notwendige Vorstellungen».",
        "Man wird kaum viel hinzufügen können zu dem, was in diesen beiden Schriften gesagt ist."
      ],
      [
        "Was der Intellekt hinzufügen kann, diese Frage soll uns heute nicht weiter beschäftigen, sondern vielmehr die Frage: Wie kann nun der Mensch zu einer gewissen Anschauung von Reinkarnation und Karma doch kommen, das heißt zu einer Anschauung, die mehr wert ist als eine bloße theoretische Überzeugung, die eine Art innerer Gewißheit geben kann, daß der eigentliche geistig-seelische Wesenskern in uns von früheren Leben herüberkommt und zu späteren Leben hinüber-geht?"
      ],
      [
        "Man kommt zu einer solchen bestimmten Anschauung dadurch, daß man innerliche Dinge ausführt, welche keineswegs leicht sind, welche schwierig sind, aber die deshalb doch immerhin ausgeführt werden können.",
        "Der erste Schritt, den man da machen kann, ist, daß man die gewöhnliche Art von Selbsterkenntnis ein wenig übt, die Art, die darin bestehen kann, daß der Mensch gewissermaßen auf sein Leben zurückblickt, so zurückblickt, daß er sich fragt: Was bin ich denn überhaupt für ein Mensch gewesen?",
        "Bin ich ein Mensch gewesen mit einer starken Neigung zum Nachdenken, zu einem innerlich nachsin­nenden Wesen, oder bin ich ein Mensch gewesen, der stets mehr die Sensationen der Außenwelt geliebt hat, dem dieses oder jenes im Leben gefallen oder nicht gefallen hat?",
        "Bin ich ein Mensch gewesen, der in der Schule gern lesen, aber nicht gern rechnen wollte, der die anderen Kinder gern geschlagen hat, aber sich nicht gern hat schlagen lassen?",
        "Oder bin ich vielleicht ein Kind gewesen, das immer dazu bestimmt war, eins abzukriegen, und das nicht schlau genug gewesen ist, die anderen eins abkriegen zu lassen? - In dieser Weise ein wenig zurückzublicken"
      ],
      [
        "auf sein Leben und insbesondere sich zu fragen: Wozu war ich - in intellektueller Weise oder in derjenigen Weise, die auf die Gemütsstimmungen oder auf die Willensimpulse bezüglich ist -besonders veranlagt?",
        "Was ist mir leicht, was ist mir schwierig ge­worden?",
        "Was hat mich so getroffen, daß ich ihm gern habe entfliehen wollen?",
        "Was hat mich so getroffen, daß ich mir gesagt habe: Es ist mir recht, daß es so gekommen ist und so weiter -, so also auf sein Leben in einer gewissen Weise zurückzublicken, das ist gut zu einer intimeren Erkenntnis seines geistig-seelischen Wesenskernes; vor allem alles das klar vor die Seele zu stellen, was zu dem gehört, was man eigentlich nicht gern gewollt hat.",
        "So zum Beispiel, ob man ein Sohn gewesen ist, der vielleicht gern ein Dichter geworden wäre, der von seinem Vater aber zum Handwerker bestimmt worden ist und auch ein Handwerker hat werden müssen, trotzdem er es nie so recht hat werden wollen; er ist es geworden, wäre aber lieber ein Dichter gewor­den.",
        "So sich klarmachen, was man eigentlich hat werden wollen, was man aber gegen seinen Willen geworden ist, dann sich klarmachen, was einem gepaßt hat im Jugendleben und was einem nie zuteil geworden ist.",
        "Dann weiter sich klarmachen, woraus man so recht hätte heraus­kommen wollen, welchem man so recht hätte entfliehen wollen.",
        "Ich bemerke, daß dies, was ich jetzt sage, sich auf das Leben in der Ver­gangenheit beziehen soll, nicht auf die Zukunft; das wäre eine falsche Vorstellung."
      ],
      [
        "Also man soll sich im Grunde genommen klarmachen, was einem ein solcher Rückblick in die Vergangenheit sagt: was man nicht hat wollen, welchem man hat entfliehen wollen und so weiter.",
        "Wenn man sich das klargemacht hat, dann hat man eigentlich ein Bild derjenigen Dinge in seinem Leben, die einem so recht am wenigsten gefallen.",
        "Darum handelt es sich aber gerade, daß man die Dinge in seinem Le­ben herausbekommt, die einem in der Vergangenheit am wenigsten gefallen haben.",
        "Und man muß nun versuchen, sich ganz einzuleben in eine höchst merkwürdige Vorstellung: Alles das, was man nun eigent­lich nicht gewollt und gewünscht hat, energisch zu wollen und zu wün­schen!",
        "Also energisch einmal sich vor die Seele stellen: Wie wärest du eigentlich, wenn du lebendig, heftig alles das gewünscht hättest, was"
      ],
      [
        "du eigentlich nicht gewünscht hast, was dir im Grunde genommen im Leben gegen den Strich gegangen ist? - Ausschalten muß man dabei in einer gewissen Weise dasjenige, was einem zu überwinden gelungen ist.",
        "Denn das allerwichtigste ist, daß man diejenigen Dinge wünscht, oder sich so vorstellt, als ob man sie lebhaft wünschen würde, die man nicht gewünscht hat, oder denen gegenüber man seine Wünsche nicht hat durchsetzen können, so daß man sich in der Empfindung, in Ge­danken ein Wesen schafft, von dem man die Vorstellung haben kann, daß man es im Grunde genommen bisher gar nicht gewesen ist.",
        "Und jetzt stelle man sich vor, daß man eigentlich gerade dieses Wesen mit aller Vehemenz, mit aller Intensität gewesen wäre.",
        "Wenn man sich das vorstellt, wenn es einem gelingt, sich zu identifizieren mit diesem Wesen, das man auf diese Weise sich selber sozusagen einkonstruiert hat, dann hat man schon wesentlich etwas gewonnen auf dem Wege, seinen inneren seelischen Wesenskern kennenzulernen.",
        "Denn es wird einem gerade an dem Bilde, das man sich nun von seiner Eigenpersön­lichkeit in der geschilderten Weise machen kann, etwas aufgehen, was man in der gegenwärtigen Inkarnation nicht ist, was man aber her­eingebracht hat in die gegenwärtige Inkarnation.",
        "Sein tieferes Wesen wird einem aufgehen an dem Bilde, das man sich auf diese Weise konstruiert."
      ],
      [
        "Es wird also von dem, der zu seinem inneren Wesenskern kommen will, im Grunde genommen etwas verlangt, was die Menschen in un­serer Gegenwart am allerwenigsten tun.",
        "Unsere Gegenwart ist gar nicht dazu veranlagt, auch nur in einer gewissen Weise so etwas her­beizusehnen, was dem ähnlich ist, was jetzt gefordert worden ist; denn in unserer Gegenwart streben eigentlich die Menschen, wenn sie über sich selber nachdenken, am allermeisten danach, sich so, wie sie sind, absolut richtig zu finden.",
        "Wenn wir zurückgehen in frühere Zeiten einer noch religiöseren Entwickelung, dann finden wir das Gefühl, daß der Mensch sich zerknirscht empfinden soll, da er so wenig dem ent­spricht, was er als sein göttliches Vorbild bezeichnen kann.",
        "Das war zwar nicht die Vorstellung, von der heute gesprochen worden ist, aber es war die Vorstellung, welche von dem, womit der Mensch gewöhn­lich zufrieden ist, abführte und zu etwas anderem hinführte - wenn"
      ],
      [
        "auch nicht zu der Überzeugung von einer anderen Inkarnation -, nämlich zu jenem Wesen hinführte, das über unsere Organisation, wie sie sich zwischen Geburt und Tod herausbildet, hinüberlebt.",
        "Es wird einem folgendes aufgehen, wenn man das Gegenbild von dem zeich­net, was man ist: Dieses Gegenbild, so schwer es dir geworden ist, es in diesem Leben als dein Bild zu fassen, es hat doch etwas mit dir zu tun; das kannst du nicht leugnen.",
        "Wenn du es hast, wird es dich ver­folgen, wird es dir vor der Seele schweben und sich so zusammen­kristallisieren, daß du dir sagen wirst: Dieses Bild hat etwas mit mir zu tun, aber ganz gewiß nicht mit meinem jetzigen Leben. - Dann bildet sich die Empfindung heraus, daß dieses Bild gerade aus einem früheren Leben stammt."
      ],
      [
        "Wenn wir dies uns vor die Seele führen, werden wir bald gewahr werden, wie irrtümlich die meisten Vorstellungen sind, die man sich gewöhnlich über Reinkarnation und Karma bildet.",
        "Sie werden es selbst schon gehört haben: wenn einem irgendwo ein Mensch im Leben entgegentritt, der zum Beispiel ein guter Rechner ist, und wenn man dann zugleich Anthroposoph ist, dann wird man sich leicht die Vor­stellung bilden: In der vorhergehenden Inkarnation ist dieser Mensch ein guter Rechner gewesen."
      ],
      [
        "Viele Reinkarnationsketten werden leider von unausgebildeten Anthroposophen in der Weise aufgestellt, daß man einfach glaubt, die vorhergehende Inkarnation dadurch zu fin­den, daß man die Fähigkeiten, die in der gegenwärtigen auftreten, auch in der vorhergehenden oder womöglich in mehreren vorhergehenden Inkarnationen wird finden müssen.",
        "Das ist die schlechteste Art, zu spe­kulieren."
      ],
      [
        "Man trifft gewöhnlich damit das Falsche.",
        "Denn die wirk­lichen Beobachtungen mit den Mitteln der Geisteswissenschaft zeigen zumeist das genaue Gegenteil.",
        "Leute zum Beispiel, die in der vorher­gehenden Inkarnation gute Rechner, gute Mathematiker waren, treten in der gegenwärtigen Inkarnation so auf, daß sie gar keine Begabung für Mathematik zeigen, daß ihnen die mathematische Begabung fehlt."
      ],
      [
        "Und will man wissen, welche Begabungen man höchstwahrscheinlich in der vorigen Inkarnation hatte - ich mache darauf aufmerksam, daß wir jetzt also auf dem Boden der Wahrscheinlichkeit stehen -, will man wissen, welche Fähigkeiten in dieser Richtung an Intelligenz,"
      ],
      [
        "künstlerischen Dingen und so weiter man in der vorigen Inkarnation gehabt hat, so tut man gut, wenn man nachdenkt, wozu man in dieser Inkarnation am allerwenigsten Fähigkeiten hat, wozu man in dieser Inkarnation sich am allerwenigsten eignet.",
        "Wenn man das heraus­bekommen hat, dann wird man finden, worin man wahrscheinlich in der vorhergehenden Inkarnation brilliert hat, wofür man ganz be­sonders begabt war."
      ],
      [
        "Ich sage «wahrscheinlich» aus dem Grunde, weil diese Dinge auf der einen Seite wahr sind, aber auf der anderen Seite vielfach durchkreuzt werden von anderen Tatsachen.",
        "Da kann zum Beispiel der Fall eintreten, daß einer eine besondere mathematische Begabung in der vorhergehenden Inkarnation hatte, aber früh gestor­ben ist, so daß diese mathematische Begabung nicht ganz zum Ausdruck gekommen ist; dann wird er in seiner nächsten Inkarnation wieder mit einer mathematischen Begabung geboren werden, die sich dann wie eine Fortsetzung aus der vorhergehenden Inkarnation darstellen wird."
      ],
      [
        "Der früh verstorbene Mathematiker Abel wird ganz gewiß in seiner nächsten Inkarnation mit einer starken mathematischen Begabung wiedergeboren werden.",
        "Wo dagegen ein Rechner besonders alt gewor­den ist, wo sich diese Begabung ausgelebt hat, da wird der Betreffende in seiner nächsten Inkarnation geradezu stumpfsinnig sein in bezug auf Mathematik."
      ],
      [
        "So ist mir eine Persönlichkeit bekannt, die so wenig mathematische Begabung hatte, daß sie als Schulbube geradezu die Ziffern haßte; und während der Betreffende in den anderen Fächern gute Zensuren hatte, war es überhaupt nur dadurch möglich, daß er die Schulklassen durchmachen konnte, daß man ihm in den anderen Fächern besonders gute Zensuren ausstellte.",
        "Das rührte davon her, daß er in der vorhergehenden Inkarnation ein besonders guter Mathe­matiker gewesen ist."
      ],
      [
        "Wenn man weiter darauf eingeht, dann stellt sich die Tatsache her­aus, daß das, was man in einer Inkarnation äußerlich treibt, das heißt, was man nicht allein äußerlich treibt, sondern was man für einen äußerlichen oder innerlichen Beruf hat, in der nächsten Inkarnation in die innere Organbildung eingeht, zum Beispiel in der Weise, daß man, wenn man in einer Inkarnation ein besonders guter Mathematiker war, dasjenige, was man sich da angeeignet hat an Zahlen- und Figurenbeherrschung,"
      ],
      [
        "mitgenommen und hineingearbeitet hat in eine be­sondere Ausarbeitung seiner Sinnesorgane, zum Beispiel der Augen.",
        "Und Menschen, die sehr gut sehen, haben diese sorgfältige Ausbildung der Formen des Auges davon, daß sie in der vorhergehenden Inkar­nation in Formen gedacht und dieses Denken in Formen mitgenommen haben und, indem sie durch die Zeit zwischen Tod und neuer Geburt geschritten sind, ihre Augen besonders ausziseliert haben.",
        "Da ist die mathematische Begabung ins Auge hineingeflossen und lebt sich nicht mehr in mathematischer Begabung aus."
      ],
      [
        "Ein anderer den Okkultisten bekannter Fall ist der, wo eine In­dividualität in einer Inkarnation besonders intensiv in Architektur-formen lebte: was sie da empfunden hat, das lebte sich ein als Kräfte in das innere Seelenleben und ziselierte besonders fein aus das Gehör-werkzeug, so daß diese Individualität in der nächsten Inkarnation ein großer Musiker wurde.",
        "Sie wurde nicht ein großer Architekt, weil die Empfindungsformen, die sich an die Architektur anlehnten, organauf-bauend wurden, so daß nichts übrigblieb, als in hohem Maße Musik zu empfinden."
      ],
      [
        "Eine äußere Betrachtung der Ähnlichkeiten täuscht in der Regel über das, was Eigentümlichkeiten in den aufeinanderfolgenden Inkar­nationen sind.",
        "Und wie wir nachdenken müssen über das, was uns nicht gefallen hat und uns vorstellen müssen, als ob wir es intensiv wünschten, so sollen wir auch nachdenken über die Dinge, zu denen wir am wenigsten befähigt sind, in denen wir sozusagen ganz stumpf­sinnig sind.",
        "Und wenn wir die allerstumpfsinnigsten Seiten unseres Wesens entdecken, dann können sie uns mit größter Wahrscheinlich­keit zu dem führen, worin wir in der vorhergehenden Inkarnation am allermeisten geglänzt haben.",
        "Daraus sehen wir, daß es naheliegt, gerade diese Dinge am falschen Ende anzufangen.",
        "Wie uns im übrigen auch ein gewisses Nachdenken darüber belehren kann, daß es eben der in­nerste seelische Wesenskern ist, der von einer Inkarnation in die andere hinüberlebt, das zeigt zum Beispiel die Erwägung, daß der Mensch Sprachen doch niemals dadurch leichter lernt, daß er in einer vorher­gehenden Inkarnation etwa in einem Sprachgebiete gelebt hat, das mit der betreffenden Sprache, die er jetzt lernen soll, zusammenhing;"
      ],
      [
        "denn sonst würden es unsere Gymnasiasten nicht gar so schwer haben, Griechisch oder Lateinisch zu lernen, obwohl viele in ihren früheren Inkarnationen in einem Gebiete gelebt haben, wo sie diese Sprachen als die gewöhnlichen Umgangssprachen gesprochen haben."
      ],
      [
        "Von dem, was wir äußerlich an uns heranbringen, müssen wir sagen, daß es so sehr verbunden ist mit dem, was sich abschließt in dem Leben des Menschen zwischen Geburt und Tod, daß gar nicht davon die Rede sein kann, daß diese Dinge in der nächsten Inkarnation in derselben Weise wiedererscheinen, sondern daß sie in Kräfte umge­wandelt in die nächste oder nächsten Inkarnationen übergehen.",
        "Die­jenigen Menschen, die zum Beispiel in einer Inkarnation eine beson­dere Anlage haben zum Sprachen erlernen, werden diese Anlage in ihrer nächsten Inkarnation nicht haben; dafür aber werden sie die Anlage haben, zu mehr unbefangenem Urteilen als die übrigen Men­schen."
      ],
      [
        "Das sind Dinge, die mit den Geheimnissen der Reinkarnation zu­sammenhängen.",
        "Und gerade wenn man auf diese Geheimnisse der Re­inkarnation blickt, wird man in der intensivsten Weise eine Vorstel­lung bekommen von dem, was eigentlich wirklich im Menschen in­nerlich ist, und was in einer gewissen Weise doch zu den Äußerlich­keiten gerechnet werden muß.",
        "Zum Beispiel ist für den gegenwärtigen Menschen die Sprache durchaus nicht mehr innerlich.",
        "Man kann die Sprache um dessentwillen, was sie ausdrückt, um des Volksgeistes wil­len lieben; aber sie ist etwas, was in umgewandelten Kräfteformen von einer Inkarnation in die andere übergeht."
      ],
      [
        "Wenn der Mensch solche Dinge verfolgt, daß er auf der einen Seite sagt: Ich will einmal recht sehr wünschen und wollen, was ich doch gegen meinen Willen geworden bin und wofür ich am wenigsten Ver­anlagung habe - dann kann er wissen: Es werden sich mir die Vor­stellungen, die ich da gewinne, zusammenformen zu dem Bilde meiner vorhergehenden Inkarnation. - Dieses Bild der vorhergehenden In­karnation wird sich mit einer großen Bestimmtheit schon ergeben, wenn man Ernst macht mit denjenigen Dingen, die jetzt einmal etwas genauer charakterisiert worden sind.",
        "Man wird nämlich tatsächlich merken, daß man an der ganzen Art und Weise, wie sich einem die"
      ],
      [
        "Vorstellungen, die man so gewonnen hat, zusammenfügen, empfinden wird: Dieses Bild ist mir eigentlich ziemlich nahe; es ist gar nicht weit von mir.",
        "Oder man wird fühlen: Es ist ein Bild weit, weit weg von mir."
      ],
      [
        "Wenn man nämlich durch die Ausarbeitung der Vorstellungen, die heute geschildert worden sind, ein solches Bild seiner vorhergehenden Inkarnation sich vor die Seele gemalt hat, dann wird man in der Regel abschätzen können, wie stark verblaßt dieses Bild ist.",
        "Man wird das Gefühl haben wie aus einer Empfindung heraus: Du stehst hier; dein Vater, dein Großvater, dein Urgroßvater können nicht das Bild sein, das da vor dir steht. - Wenn man aber das Bild auf sich wirken läßt, dann bekommt man in der Tat durch Gefühl und Empfindung die Meinung: So und so viele Personen stehen zwischen dir und diesem Bilde! - Nehmen wir einmal an, man bekommt dieses Gefühl - und ein solches stellt sich heraus -, zwischen einem selbst und diesem Bilde stünden zwölf Personen, und ein anderer bekäme das Gefühl, zwischen ihm selbst und dem Bilde stünden sieben Personen."
      ],
      [
        "Ein solches Gefühl aber bekommt man, und dieses Gefühl ist außerordentlich wichtig.",
        "Denn wenn zum Beispiel zwölf Personen zwischen einem selbst und diesem Bilde stehen, so braucht man nur durch drei zu dividieren und würde dann vier herausbekommen."
      ],
      [
        "Das sind dann in der Regel die Jahrhunderte, die einen von der vorhergehenden Inkarnation trennen.",
        "Also ein Mensch, der das Gefühl haben würde, daß er von dem Bilde, das ich seiner Entstehung nach geschildert habe, um zwölf Menschen entfernt ist, daß es um zwölf Personen über ihm ist, er müßte sich sagen: Meine vorhergehende Inkarnation fällt vier Jahrhunderte vor die jetzige. - Das ist nur als ein Beispiel angeführt; es wird in den wenigsten Fällen so sein, aber man kommt dadurch zu einer Schätzung."
      ],
      [
        "Die meisten werden finden, daß sie auf diese Weise richtig abschätzen können, wann sie vorher dagewesen sind.",
        "Nur sind die Voraussetzun­gen dazu natürlich etwas schwierig."
      ],
      [
        "Damit haben wir eigentlich Dinge berührt, welche dem Gegen­wartsbewußtsein ja so ferne wie möglich liegen.",
        "Und es ist ganz und gar nicht zu bezweifeln, daß, wenn irgend jemand diese Dinge Leuten erzählte, die dafür unvorbereitet sind, sie dann finden werden, daß das ja wirklich unverantwortliche Phantastereien sind.",
        "Nun ist es"
      ],
      [
        "schon einmal das Schicksal der anthroposophischen Weltanschauung, daß sie von allen bisherigen Weltanschauungen am allerallermeisten in einer gewissen Weise sich entgegenstellen muß dem, was das Herge­brachte ist.",
        "Denn das Hergebrachte ist im weitesten Umfange, wie es einem entgegentritt, der krasseste, der ödeste Materialismus.",
        "Und ge­rade da, wo uns gewisse Weltanschauungen so entgegentreten, als ob sie am allerfestesten auf dem Boden wissenschaftlicher Weltanschauung ständen, da sind sie tatsächlich so, daß sie am ödesten aus einer ge­wissen materialistischen Grundanschauung herauswachsen.",
        "Da nun die Anthroposophie dazu verurteilt ist, in einer gewissen Weise selber für die große Welt der Weltanschauungen das zu sein, was heute ver­langt worden ist für den Menschen, der eine Vorstellung bekommen soll von seiner vorhergehenden Inkarnation, so kann es begreiflich erscheinen, daß es dem gegenwärtigen Menschen sehr ferne liegen muß, anthroposophische Anschauungen ernst zu nehmen.",
        "Denn die Men­schen werden ebenso abgeneigt sein, zu wünschen und zu wollen, was sie ihr Leben lang nicht gewünscht und gewollt haben, wie ihren Denk-gewohnheiten ferne liegen die spirituellen Wahrheiten."
      ],
      [
        "Nun könnte man die Frage aufwerfen: Warum tritt denn gerade jetzt die spirituelle Wahrheit unter die Menschen?",
        "Warum läßt sie nicht den Menschen Zeit, sich zu entwickeln, bis sie reifer sind?"
      ],
      [
        "Das rührt davon her, daß auch wieder kaum ein größerer Unter­schied gedacht werden kann zwischen zwei aufeinanderfolgenden Menschheitsepochen, als er sein wird zwischen der Epoche, in der die gegenwärtige Menschheit lebt, und zwischen derjenigen, in welche die Menschheit hineinwachsen wird, wenn die jetzt lebenden Menschen wiedergeboren sein werden in der nächsten Inkarnation.",
        "Denn es hängt nicht von den Menschen ab, wie sich gewisse geistige Fähig­keiten herausbilden; das hängt ab von dem ganzen Sinn und der gan­zen Bedeutung und dem ganzen Wesen der Erdentwickelung.",
        "Die Menschen sind jetzt nämlich am weitesten davon entfernt, an Rein­karnation und Karma zu glauben.",
        "Nicht die Anthroposophen - aber Anthroposophen sind ja nur wenige in der Welt -, nicht die, welche noch alten Religionsformen angehören, sondern die, welche heute die Träger des äußeren Kulturlebens sind, die sind heute am allermeisten"
      ],
      [
        "davon entfernt, an Reinkarnaüon und Karma zu glauben.",
        "Nun wird merkwürdigerweise gerade diese Tatsache, daß die Menschen heute am allerwenigsten geneigt sind, an Reinkarnation und Karma zu glauben, verbunden mit dem, was die Menschen heute treiben und lernen, näm­lich treiben und lernen, insofern dies in bezug auf intellektuelle Fähig­keiten eine Bedeutung hat - diese Tatsachen werden bewirken, daß bei diesen Menschen der Gegenwart in der nächsten Inkarnation das Gegenteil eintreten wird."
      ],
      [
        "Diese Menschen der Gegenwart werden in der nächsten Inkarnation - gleichgültig, ob sie spirituell oder mate­rialistisch streben - starke Anlage haben, ihre vorhergehende In­karnation zu empfinden.",
        "Ganz gleichgültig, was die Menschen der Gegenwart treiben: dadurch, daß sie Menschen der Jetztzeit sind, wer­den sie wiedergeboren werden mit einer starken Anlage und einer starken Sehnsucht, von der vorhergehenden Inkarnation etwas zu erfahren, etwas zu wissen."
      ],
      [
        "Wir stehen gerade an einer solchen Zeiten-wende, welche die Menschen führt von einer solchen Inkarnation, in der sie am allerwenigsten wissen wollen von Reinkarnation und Kar­ma, zu einer Inkarnation, in der in ihnen die lebendigste Empfindung sein wird: Das ganze Leben, das ich jetzt führe, steht für mich in der Luft, wenn ich nicht irgend etwas wissen kann über meine vorher­gehende Inkarnation. - Und die Menschen, welche jetzt am aller­meisten schimpfen über Reinkarnation und Karma, sie werden sich geradezu winden unter der Qual des nächsten Lebens, weil sie sich nicht erklären können, wie das Leben so hat werden können.",
        "Nicht um sich eine gewisse Rücksehnsucht nach dem vorhergehenden Leben anzueignen, wird jetzt Anthroposophie getrieben von den Menschen, sondern um Verständnis zu haben für das, was für die gesamte Mensch­heit einmal auftreten wird, wenn die Menschen, die heute leben, wieder da sein werden."
      ],
      [
        "Die Menschen, die heute Anthroposophen sind, werden die Anlage mit den anderen teilen, daß sie sich wieder erinnern wollen; aber sie werden Verständnis haben und dadurch innere Harmonie in bezug auf ihr Seelenleben.",
        "Die, welche heute die Anthroposophie zu­rückweisen, sie werden davon wissen wollen, und sie werden so etwas empfinden wie eine innere Qual nach etwas, was eben ihre vorher-gehende Inkarnation wäre im nächsten Leben; sie werden aber nichts"
      ],
      [
        "verstehen von dem, was sie am allermeisten drückt und quält; sie werden ratlos sein, werden innerlich disharmonisch sein.",
        "Und es wird ihnen gesagt werden müssen in der nächsten Inkarnation: Du lernst erst erkennen, was dir Qualen verursacht, wenn du dir vorstellst, daß du eigentlich im Ernste diese Qual gewollt haben könntest. - Natür­lich werden alle Menschen diese Qual nicht wollen.",
        "Aber die Men­schen, die heute Materialisten sind, werden dann in der nächsten Inkarnation anfangen, ihre innere Zerknirschtheit, ihre innere Öde und Qual zu begreifen, wenn sie befolgen werden die Anforderungen, den Rat derer, die dann werden wissen können und ihnen sagen: Stellt euch einmal vor, dieses Leben, wie ihr es fliehen möchtet, das hättet ihr gewollt. - Wenn sie anfangen werden, diesen Rat zu befolgen, nachzudenken darüber: Wodurch kann ich dieses Leben gewollt haben? - dann werden sie sich sagen: Ach ja, da habe ich vielleicht gelebt in einer Inkarnation, in welcher ich gesagt habe: Was, ein an­deres, nächstes Leben oder Inkarnation soll auf dieses Leben folgen?",
        "Unsinn!",
        "Dummheit!",
        "Wie kann man so etwas glauben!",
        "Dieses Leben erfüllt sich in sich selber, ist in sich abgeschlossen; das sendet keine Kräfte in ein späteres hinüber!",
        "Ja, weil ich dazumal die Empfindung gehabt habe, ein folgendes Leben ist nichtig, ist unsinnig, dadurch ist es nichtig und unsinnig geworden!",
        "Ich habe gerade den Gedanken in mich hineingepflanzt als Kraft, der mir jetzt das Leben so öde und leer macht!"
      ],
      [
        "Das wird ein richtiger Gedanke sein.",
        "So wird sich sozusagen kar­misch der Materialismus ausleben.",
        "Sinnvoll wird die nächste Inkarna­tion bei denjenigen Menschen sein, welche sich die Überzeugung ver­schafft haben, daß ihr Leben, wie es jetzt ist, eben nicht nur in sich erfüllt ist, sondern Ursachen enthält für das nächste.",
        "Unsinnig, leer und öde wird das Leben derer sein, die durch den Gedanken der Un­sinnigkeit der Reinkarnation sich selber das Leben öde und nichtig gemacht haben."
      ],
      [
        "So sehen wir, daß die Gedanken, die wir hegen, nicht etwa in einer gesteigerten Form in das nächste Leben hinübergehen, sondern um­gewandelt als Kräfte im nächsten Leben auftreten.",
        "In der geistigen Welt haben eben Gedanken, so wie sie jetzt sind im Leben zwischen"
      ],
      [
        "Geburt und Tod, keine Bedeutung, sondern sie haben nur eine Bedeu­tung in einer umgewandelten Form.",
        "Wenn jemand zum Beispiel einen großen Gedanken hat, so kann dieser Gedanke noch so groß sein:"
      ],
      [
        "wenn der Mensch durch die Pforte des Todes geht, ist der Gedanke als Gedanke fort.",
        "Aber der Enthusiasmus und die Empfindung und das Gefühl, das aufgelebt hat unter dem Einfluß des Gedankens, das geht durch die Pforte des Todes."
      ],
      [
        "Von der Anthroposophie selber nimmt der Mensch nicht die Gedanken mit, wohl aber das, was er an den Gedanken erlebt hat - bis in die Einzelheiten, nicht nur die all­gemeine Grundempfindung.",
        "Das ist das, was wir insbesondere fest­halten wollen: daß Gedanken als solche für den physischen Plan das eigentlich Bedeutungsvolle sind, und daß wir, wenn wir von der Wirkung des Gedankens für die höheren Welten sprechen, zugleich sprechen müssen von einer Umwandlung dieser Gedanken nach den höheren Welten hinauf."
      ],
      [
        "Gedanken, welche also eine Wiederverkörpe­rung leugnen, wandeln sich um in dem wiederverkörperten Leben in innere Nichtigkeit, in innere Leerheit des Lebens, und innere Nichtig­keit, innere Leerheit des Lebens wird als Qual, als Disharmonie empfunden. - Sie können sogar durch einen Vergleich eine Vorstel­lung bekommen, wie eine solche innere Nichtigkeit und Leerheit verlaufen muß, wenn Sie sich denken, daß Sie etwas recht gerne haben und es immer dann gern sehen, wenn Sie an einen bestimmten Ort kommen.",
        "Sie haben sich zum Beispiel gewöhnt, eine bestimmte Blume in einem Garten an einem bestimmten Ort blühen zu sehen."
      ],
      [
        "Wenn dann die Blume von ruchloser Hand abgeschnitten wird, wer­den Sie Schmerz empfinden.",
        "Wenn Sie etwas, was Sie lieben, nicht haben, wenn Ihnen das fehlt, dann empfinden Sie Schmerz.",
        "So ist es mit der Gesamtorganisation des Menschen."
      ],
      [
        "Wodurch empfindet der Mensch Schmerz?",
        "Wenn der Ätherleib und der Astralleib eines Organs immer an eine bestimmte Stelle des physischen Leibes eingeschaltet sind, und wenn dieses Organ einen Schnitt bekommt und verletzt wird, so können der Ätherleib und der Astralleib nicht gut eingreifen."
      ],
      [
        "Es ist das gerade so, wie wenn Ihnen durch den Schnitt von ruchloser Hand die Rose im Garten an der bestimmten Stelle abgeschnitten wird.",
        "Der Ätherleib und der Astralleib finden dann nicht, wenn ein"
      ],
      [
        "Organ verletzt wird, was sie suchen; das wird dann als leiblicher Schmerz empfunden.",
        "So werden also die Gedanken, die sich der Mensch gemacht hat als fortwirkend in die Zukunft, ihm in der Zu­kunft entgegentreten.",
        "Dagegen werden sie ihm fehlen, und er wird nichts finden, wo er sie suchen wird an einem bestimmten Ort, wenn er nichts hinübersendet von Glauben und Erkenntniskräften in die nächste Inkarnation, und dann wird er dieses Fehlen von etwas an einem Orte als Schmerz und Qual empfinden."
      ],
      [
        "Dies sind Angaben, die uns von einer gewissen Seite den karmischen Verlauf gewisser Dinge klarlegen werden.",
        "Sie mußten gemacht wer­den, weil wir noch tiefer hineinsehen wollen in die Art und Weise, wie der Mensch noch weiter Veranstaltungen machen kann, um seinen eigentlichen geistig-seelischen Wesenskern zu erkennen."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG Berlin, 30.Januar 1912",
    "paragraphs": [
      "Die Betrachtungen, die wir das letzte Mal hier angestellt haben, sie werden so, wie sie damals vorgebracht worden sind, noch für man­chen etwas Unverständliches, vielleicht sogar Bedenkliches haben. Aber wenn wir noch auf dieses oder jenes heute eingehen werden, so wer­den uns die Dinge schon nähertreten können.",
      "Was war es denn eigentlich, was wir uns an dem letzten Zweigabend vor die Seele geführt haben? Es war gewissermaßen etwas Ähnliches für die Gesamtwesenheit des Menschen, wie dasjenige ist, was ein Mensch vollbringt, wenn er zum Beispiel in dieser oder jener Lebens­lage ist, in der er sich auf frühere Erfahrungen und Erlebnisse besinnen muß, sich an frühere Erlebnisse oder Erfahrungen erinnern soll.",
      "Erin­nerung, Gedächtnis sind ja menschliche Seelenerlebnisse, die für das gewöhnliche Bewußtsein im Grunde zunächst nur gekannt werden für das Seelenleben, welches da verläuft zwischen Geburt und Tod, oder genauer gesagt - was wir ja öfter ausgesprochen haben - für einen Zeitraum, der eigentlich erst in den späteren Kindheitsjahren beginnt, bis zum Tode hin. Denn wir wissen, daß wir uns für das gewöhnliche Bewußtsein nur erinnern bis zu einem bestimmten Zeitpunkt unserer Kindheit, und daß wir über dasjenige, was vorangegangen ist, allein durch Eltern oder ältere Verwandte und Bekannte etwas erfahren kön­nen.",
      "Wenn wir den eben in dieser Art charakterisierten Zeitraum des Menschenlebens ins Auge fassen, so sprechen wir für diesen Zeitraum in bezug auf das Seelenleben von Erinnerung. Es ist hier natürlich nicht möglich, in feinerer Weise einzugehen auf die Bedeutungen der Worte «Erinnerungsvermögen» oder «Gedächtnis»; das ist auch für unsere Zwecke nicht notwendig.",
      "Wir müssen uns nur zunächst einmal klar vor die Seele führen, daß zu alledem, was mit diesen Worten bezeichnet wird, eben das Sich-Besinnen auf früher gemachte Erfahrungen oder Erlebnisse gehört. Was wir nun das letzte Mal betrachteten, war ge­wissermaßen etwas Ähnliches wie dieses Sich-Besinnen; nur sollte diese Ähnlichkeit nunmehr nicht bloß so gelten wie jenes Erinnerungsvermögen,",
      "das in unser gewöhnliches Leben hereinfällt, sondern es sollte uns gleichsam als ein höheres, erweitertes Erinnerungsvermögen hin-überführen über die gegenwärtige Inkarnation zu einer Art von Ge­wißheit, daß wir vor diesem Erdenleben in anderen Erdenleben da­gewesen sind. Und wie wir das letzte Mal erwähnt haben, sollte es in bezug auf diesen höheren Prozeß so sein, wie das Sich-Besinnen auf irgend etwas Erlebtes im gewöhnlichen Leben.",
      "Wenn wir uns auf der einen Seite einen Menschen vorstellen, der irgend etwas braucht, was er gelernt hat in einer früheren Zeit seines jetzigen Lebens, und der dann seine Seele dazu stimmt, heraufzuholen aus ihren Tiefen, was er da gelernt hat, um es mit dem gegenwärtigen Blick zu verfolgen, wenn wir uns lebhaft diesen Prozeß der Besinnung vormalen, so haben wir in ihm eine solche Verrichtung, die zu unserem gewöhnlichen Erinne­rungsvermögen gehört. Was das letzte Mal erwähnt worden ist, sind Verrichtungen der Seele.",
      "Aber diese Verrichtungen der Seele sollten da­zu führen, daß etwas Ähnliches in unserem Inneren auftritt in bezug auf frühere Erdenleben, wie das, was in bezug auf dieses Erdenleben eintritt in der Seele, wenn wir heraufquellen fühlen in der Erinnerung irgend etwas, was wir früher erlebt haben. Daher dürfen Sie auch nicht das, was das letzte Mal gesagt worden ist, so betrachten, als ob das schon alles wäre, was uns in frühere Erdenleben hineinführen könnte, oder als ob es vor allen Dingen dasjenige wäre, was nun von vorn­herein eine richtige Vorstellung hervorrufen könnte von der Art, wie wir in früheren Erdenleben waren.",
      "Es ist nur eine Hilfe, so wie das Sich-Besinnen auch eine Hilfe ist, um heraufzuholen, was in die Unter­gründe des Seelenlebens hinuntergeschwunden ist. Fassen wir kurz zu­sammen, was wir über solches Sich-Besinnen in bezug auf frühere Erdenleben ins Auge gefaßt haben.",
      "Das kann am besten in folgender Weise geschehen.",
      "Bei einiger Selbsterkenntnis fällt uns in unserem Leben manches auf, wovon wir uns sagen, wir begreifen, daß uns das getroffen hat. Wenn uns irgendein mißliches Ereignis trifft und wir auch nicht ganz ein­sehen, wieso dieses Ereignis hat kommen müssen, uns aber doch sagen:",
      "Du bist eigentlich doch ein recht leichtsinniger Mensch; es ist kein Wunder, daß dir das begegnet ist -, so ist wenigstens etwas wie ein",
      "Anklang da an ein Verständnis dafür, daß uns so etwas getroffen hat. Aber es gibt zahlreiche andere Erlebnisse, die hereintreten in das Leben und von denen wir uns durchaus nicht die Vorstellung bilden können, daß sie zusammenhängen mit unseren Seelenkräften und Fähigkeiten. Wir sprechen dann wohl im gewöhnlichen Leben so, daß wir von Zu­fälligkeiten reden. Von Zufälligkeiten sprechen wir dann, wenn wir nicht einsehen, wie die Dinge, die uns als Schicksalsschläge treffen, mit unserer inneren Seelenstimmung oder sonstigem zusammenhängen. Auch auf andere Erlebnisse ist aufmerksam gemacht worden. Es sind das diejenigen Seelenerlebnisse, bei denen wir gewissermaßen durch das, was wir unser gewöhnliches Ich nennen, uns herausreißen aus ir­gendeiner Lebenslage, in die wir aber eigentlich hineingestellt sind. Als Beispiel ist angeführt worden, wenn jemand von seinen Eltern oder ihm nahestehenden Menschen zu irgendeinem Berufe oder irgendeiner Le­benslage bestimmt worden ist, er aber sich so fühlt, daß er mit aller Gewalt da heraus und zu etwas anderem will. Wenn wir im späteren Leben auf so etwas zurückblicken, so sagen wir uns: Wir waren hinein-versetzt in eine Lebenslage, aber wir haben uns durch unseren Willens-impuls, durch unsere Sympathie und Antipathie daraus herausgeris­sen. - Also von solchen gleichsam Umwendungen dessen, in das wir hineingestellt sind, ist gesprochen worden.",
      "Es handelt sich nicht darum, daß wir bei so einer Rückerinnerung alles mögliche ins Auge fassen, sondern nur dasjenige, was uns wirklich im Leben einmal nahegetreten ist. Wenn jemand zum Beispiel niemals in sich den Beruf gefühlt hat, oder keine Veranlassung gehabt hat, Seefahrer zu werden, so kommt natürlich ein solcher Willensimpuls durchaus nicht in Betracht für die Erwägungen, die wir das letzte Mal angestellt haben, sondern nur solche, wo wir wirklich eine Art Schick­salswendung herbeigeführt haben; also Lagen des Lebens, bei denen wir gleichsam eine Umwendung des Lebens herbeigeführt haben. Und auch das fassen Sie nicht so auf, als ob durch dieses Sich-Besinnen auf seine früheren Erlebnisse, nach den entwickelten Grundsätzen, etwa ein­treten sollte ein reuiges Zurückkehren; so daß, wenn wir uns im spä­teren Leben an dergleichen erinnern und zu der Erkenntnis kommen, wir haben uns da herausgerissen, wir nun reuig zurückkehren und uns",
      "wieder hineinstellen sollten, in was wir dazumal hineingestellt waren und nicht drinnen geblieben sind. Nicht um praktische Konsequenzen handelt es sich, sondern um das Sich-Besinnen, wo solche Wendungen eingetreten sind. Und dann handelt es sich darum, daß wir in ener­gischster Weise solchen Dingen gegenüber, wovon wir sagen: Es trat zufällig an uns heran -, und: Wir waren hineingestellt, haben uns aber herausgerissen -, folgendes innere Erlebnis herbeiführen.",
      "Wir sagen uns: Ich stelle mir vor, daß das, was ich damals nicht ge­wollt habe, aus dem ich mich herausgerissen habe, ein solches gewesen wäre, in das ich mich mit dem stärksten Willensimpuls hineingestellt habe. Also das, was einem antipathisch war - und weil es einem anti­pathisch war, deshalb hat man sich herausgerissen -, das stelle man sich so vor die Seele, daß man sich sagt: Ich will mich probeweise der Vorstellung hingeben, daß ich das mit aller Gewalt gewollt habe, und ich will mir das Bild eines Menschen vor die Seele stellen, der so etwas mit aller Gewalt gewollt hätte. - Und von denjenigen Dingen, von denen wir gesagt haben, sie seien Zufälligkeiten, stellen wir uns auch vor, probeweise, wir hätten sie herbeigeführt. Nehmen wir an, es sei uns nur einmal die Erinnerung nahegetreten, da oder dort wäre uns ein Mauerstein auf die Schulter gefallen und hätte uns recht weh getan. Da wollen wir uns der Vorstellung hingeben: wir wären auf das Dach hinaufgestiegen, hätten dort den Mauerstein gelockert, so daß er im nächsten Augenblick herunterfallen muß und dann wären wir schnell hinuntergerannt, so daß der Stein dann auf uns herunterfallen mußte. Es handelt sich hierbei nicht darum, daß es groteske Vorstellungen sind, sondern um das, was wir damit erreichen wollen.",
      "Nun versetzen wir uns so recht in die Seele eines Menschen, von dem wir so ein Bild konstruiert haben, als ob der alles das gewollt hätte, was uns nur «zufällig» getroffen hat, und alles das gewünscht hätte, aus dem wir uns herausgerissen haben. Nur erfolgt in der Seele nichts, wenn man eine solche Übung zwei-, drei-, viermal macht, aber sehr viel erfolgt, wenn man das in Anknüpfung an die zahlreichsten Erlebnisse macht, die man finden wird, wenn man sie sucht. Wenn man dies immer wieder und wieder macht und es sich recht lebendig vorstellt, wenn man sich geradezu einen Menschen imaginiert, der das alles gewollt hätte, was",
      "wir nicht gewollt haben, dann wird man die Erfahrung machen, daß dieses Menschenbild, das man sich da vor die Seele gerufen hat, uns nicht mehr losläßt, daß es einen ganz merkwürdigen Eindruck auf uns macht, als wenn es tatsächlich etwas wäre, das mit uns etwas zu tun hätte. Wenn man sich auf solche Art etwas Feinheit aneignet in bezug auf eine derartige Selbstprüfung, dann wird man bald dazu kommen, die Ähnlichkeit herauszufinden, welche besteht zwischen einer solchen Stimmung und einem solchen Bilde, das man da konstruiert hat, und zwischen einer solchen Vorstellung, die man heraufgerufen hat aus dem Gedächtnis, bei der man spürt, wie sie da kommt als eine Erinnerungs­vorstellung.",
      "Der Unterschied ist nur der, daß man bei dem gewöhn­lichen Gedächtnisvorgang, bei dem man eine solche Vorstellung aus der Seele heraufschafft, es vorzugsweise zu tun hat mit Vorstellungen; da­gegen ist das, was in unserer Seele lebendig wird, wenn wir jene Übun­gen machen, von denen gesprochen worden ist, etwas Gefühlsartiges, etwas, was mehr mit unseren Seelenstimmungen zusammenhängt, we­niger mit unseren Vorstellungen. Wir fühlen uns in einer sonderbaren Weise gegenüber diesem Bilde.",
      "Auf das Bild kommt es weniger an; aber die Gefühle, die wir haben, machen einen den Erinnerungsvorstellun­gen ähnlichen Eindruck. Und wenn wir dann so etwas wiederholen und immer wieder und wieder wiederholen, dann ergibt sich erfahrungs­gemäß, ganz wie durch eine innere Selbstverständlichkeit die Erkennt­nis, könnte man sagen, daß das Bild, das man sich da konstruiert hat, etwas wird, so wie eine Erinnerungsvorstellung auch immer klarer und klarer wird, während sie zuerst, wenn man sich willkürlich besinnt, dunkel heraufgeholt wird aus den Seelentiefen.",
      "Also nicht darum han­delt es sich, was man da vorstellt, sondern daß sich das verwandelt, was man da vorstellt, daß es etwas anderes wird. Es geht so ein Prozeß vor, wie wenn jemand sich auf einen Namen besinnen will, und er druckst und druckst und hat einen Anklang, und er sagt dann: Nuß - - bau­mer -, aber er hat dann ein Gefühl, daß das doch nicht stimmt, und dann gesellt sich durch Gründe, die er selbst nicht übersehen kann, der richtige Name, vielleicht: Nußdörfer - hinzu.",
      "So wie sich hier die Namen «Nußbaumer» und «Nußdörfer» gegenseitig konstruieren, so wird sich auch das Bild zurechtrücken, wird sich ändern, und demgegenüber",
      "tritt das Gefühl auf: Du hast da etwas erlangt, was in dir steckt, und was durch die Art, wie es in dir steckt und sich verhält zu deinem ganzen übrigen Gemütsleben, dir deutlich zeigt: so können diese Dinge nicht in dir gewesen sein in der jetzigen Inkarnation! -Dadurch ergibt sich dann mit einer großen inneren Deutlichkeit, daß so etwas, wie es da in uns steckt, zurückliegt. Wir müssen jetzt nur be­greifen, daß wir es hier mit einer Art von Erinnerungsvermögen zu tun haben, das ausgebildet werden kann in der menschlichen Seele; ein Er­innerungsvermögen, das man dem gewöhnlichen Erinnerungsvermögen gegenüber mit einem anderen Namen bezeichnen muß. Das gewöhn­liche Erinnerungsvermögen könnte man bezeichnen mit dem Worte «Vorstellungserinnerung»; aber dieses Erinnerungsvermögen, das jetzt in Frage kommt, müßte man eigentlich als eine Art von «Gefühls- und Empfindungserinnerung» bezeichnen. Daß dies eine gewisse Berechti­gung hat, kann Ihnen aus folgenden Erwägungen hervorgehen.",
      "Bedenken Sie, daß tatsächlich unser gewöhnliches Gedächtnis, unser gewöhnliches Erinnerungsvermögen eine Art Vorstellungserinnerung gibt. Besinnen Sie sich nur einmal darauf, wie irgendein besonders schmerzliches Ereignis, das Sie vielleicht vor zwanzig Jahren ganz nie­dergedrückt hat, herauftaucht in der Erinnerung. Vielleicht malt sich Ihnen dieses Ereignis mit allen Einzelheiten bildlich ab, aber den Schmerz, den Sie damals durchgemacht haben, fühlen Sie in der Erin­nerung nicht mehr in der entsprechenden Weise; der ist in einer gewis­sen Weise aus der Erinnerungsvorstellung getilgt. Selbstverständlich gibt es da verschiedene Grade, und es kann ja vorkommen, daß einen Menschen etwas so getroffen hat, daß immer wieder und wieder neuer und heftiger Schmerz auftritt, wenn er sich an das Erlebte erinnert. Aber der allgemeine Satz, der jetzt ausgesprochen ist, gilt dennoch, so daß wir daraus erkennen, daß für die gegenwärtige Inkarnation unser Erinnerungsvermögen ein Vorstellungserinnern ist, während die erleb­ten Gefühle oder selbst Willensimpulse nicht mit derselben Intensität wieder auftauchen in der Seele, jedenfalls nicht so, daß sie sich mit der ursprünglichen vergleichen ließe. Sie brauchen sich nur ein charak­teristisches Beispiel zu vergegenwärtigen und Sie werden sehen, wie groß der Unterschied ist zwischen der Vorstellung, die in der Erinnerung",
      "auftaucht, und dem, was übriggeblieben ist im gewöhnlichen Leben in der gegenwärtigen Inkarnation von den durchgemachten Ge­fühlen und Willensimpulsen. Sie brauchen nur an so etwas zu denken wie an einen Menschen, der seine Memoiren schreibt. Nehmen wir zum Beispiel an, Bismarck wäre beim Schreiben seiner Memoiren bis an den Punkt gekommen, wo er den Deutsch-Österreichischen Krieg vom Jahre 1866 vorbereitet hat, und stellen Sie sich vor, was in Bismarcks Seele vorgegangen sein mag an jenem unendlich kritischen Punkt, wo er gegen eine Welt von Vorurteilen und gegen eine Welt von Willensim­pulsen die Ereignisse gelenkt und geleitet hat. Und nun stellen Sie sich nicht mehr vor, wie das alles damals in Bismarcks Seele gelebt hat, sondern daß alles, was er dazumal unmittelbar unter dem Eindruck der Ereignisse erlebt hat, hinuntergesunken ist in die Tiefen der Seele, und denken Sie an die Verblaßtheit, die eingetreten sein muß gegenüber den Gefühlen und Willensimpulsen, die vorhanden waren, als er die Sache ausführte, im Vergleich zu der Zeit, als er seine Memoiren niederge­schrieben hat. Kein Mensch wird sich darüber unklar sein, welcher Un­terschied besteht zwischen dem Vorstellungsmäßigen der Sache und demjenigen, was den Gefühlen und Willensimpulsen angehört.",
      "Wer nun schon ein wenig an Anthroposophisches herangekommen ist, der wird auch begreifen, wenn gesagt wird, was hier von anderen Gesichtspunkten aus schon öfter gesagt worden ist: daß unser Vorstel­len, also unser gedächtnismäßiges Vorstellen, dasjenige in unserem Seelenleben ist, was, wenn es angeregt ist von außen durch die äußere Welt, in der wir hier im physischen Leibe leben, eigentlich auch nur seine Bedeutung hat für diese einzelne Inkarnation. Wir haben immer aus den anthroposophischen Grundsätzen heraus die große Wahrheit angeführt, daß wir von allen Vorstellungen, von allen Begriffen, die wir uns aneignen, indem wir dieses oder jenes sinnlich wahrnehmen, dieses oder jenes im Leben zu fürchten oder zu hoffen haben - das heißt also jetzt nicht mit Bezug auf die Gemütsimpulse, sondern auf die Vorstellungen -, daß dies alles, was wir im Vorstellungsleben haben, sehr bald verschwunden ist, wenn wir durch die Pforte des Todes ge­gangen sind. Denn die Vorstellungen gehören zu dem, was verfließt im physischen Leben, gehören zu dem, was am wenigsten bleibt. Aber es",
      "kann jemand leicht begreifen, der überhaupt schon von irgendeiner Seite her eingegangen ist auf die Gesetze von Reinkarnation und Kar­ma - ich habe es auch hier schon erwähnt -, daß unsere Vorstellun­gen, insoweit wir sie uns aneignen im Leben, das im Verhältnis zur Außenwelt oder zu den Dingen des physischen Planes verfließt, in der Sprache zum Ausdruck kommen, und daß wir uns daher das Sprechen verbunden denken können in einer gewissen Weise mit dem Vorstel­lungsleben. Nun weiß jeder, daß er das Sprechen irgendeiner Sprache lernen muß in der einzelnen Inkarnation.",
      "Denn während es ganz klar ist, daß eine ganze Anzahl von Gymnasiasten der Gegenwart inkar­niert war im alten Griechenland, wird keinem das Griechischlernen dadurch leichter gemacht, daß er sich erinnern kann, wie er das Grie­chisch in seiner früheren Inkarnation gesprochen hat. Die Sprache ist durchaus ein Ausdruck des Vorstellungslebens, und das Schicksal der Sprache ist ein ähnliches wie das Schicksal des Vorstellungslebens; so daß die Vorstellungen, wie sie in uns leben mit Bezug auf die physische Welt und selbst die Vorstellungen, die wir gewinnen müssen über die höheren Welten, in einer gewissen Weise immer gefärbt sind von den Eindrücken der physischen Welt.",
      "Nur wenn wir hindurchsehen können durch diese Einkleidung, sehen wir, was die Vorstellungen mitteilen können über die höheren Welten. Aber, was wir hier in der physischen Welt an unmittelbaren Vorstellungen gewinnen können, das ist auch an das Leben zwischen Geburt und Tod in einer gewissen Weise ge­bunden.",
      "Nach dem Tode bilden wir uns nämlich nicht Vorstellungen in der Art, wie wir sie uns hier bilden, sondern da sehen wir die Vor­stellungen; da sind sie unsere Wahrnehmungen, da sind sie so vorhan­den, wie in der physischen Welt Farben oder Töne vorhanden sind. Während in der physischen Welt das, was sich der Mensch durch die Vorstellungen vergegenwärtigt, eigentlich nur mit dem physischen Ma­terial ausgedrückt mitgenommen wird, was leicht übersehen werden kann, haben wir im entkörperten Zustande Vorstellungen so vor uns, wie wir Farben oder Töne hier vor uns haben.",
      "Rot oder Blau kann der Mensch allerdings nicht sehen, wie er sie hier mit den physischen Augen sieht; aber, was er hier nicht sieht, worüber er sich hier Vorstellungen bildet, das ist dann für ihn so da, wie Rot oder Grün oder irgendein",
      "Ton hier. Während in der physischen Welt das, was wir rein vorstel­lungsmäßig - oder besser gesagt begriffsmäßig im Sinne der «Philo­sophie der Freiheit» - kennenlernen, nur durch den Schleier des Vor­stellungslebens gesehen werden kann, liegt es für die entkörperte Seele so da, wie die physische Welt für das gewöhnliche Bewußtsein.",
      "In der physischen Welt gibt es Menschen, welche das, was der sinn­liche Eindruck gibt, eigentlich für alles halten. Und was man sich nur durch einen Begriff klarmachen kann, wie zum Beispiel die Art und Weise, wie alles, was die Sinne geben können, umfaßt wird, sagen wir vom Begriff «Lamm», oder wie es umfaßt wird vom Begriff «Wolf», dasjenige also, was aufdröselt das Materielle, das kann von denen, die nur die sinnlichen Eindrücke gelten lassen wollen, sogar geleugnet wer­den. Wir können sagen: Der Mensch kann sich in seinen Vorstellungen ein Bild machen über alles, was er am Lamm sieht, und kann sich eben­falls ein Bild machen über alles, was er am Wolf sieht. Nun versucht eine gewöhnliche Anschauung dem Menschen zu suggerieren, daß das, was da begriffsmäßig gebildet werden kann, nur als «bloßer Begriff» anzuschlagen ist. Aber wenn wir zum Beispiel einen Wolf einsperren würden und ihn längere Zeit hindurch mit lauter Lämmern fütterten, so daß, wenn er früher etwas anderes gefressen hat, dies als Materie jetzt draußen ist, und er angefüllt ist mit lauter Lamm-Materie, so wird doch kein Mensch sich dem Glauben hingeben können, daß der Wolf dadurch ein Lamm geworden sei. Daher werden wir sagen müssen:",
      "Da ist es handgreiflich, daß das, was aufdröselt den Sinneseindruck, der Begriff, ein Wirkliches ist. Doch es wird nicht geleugnet: das, was den Begriff bildet, das stirbt. Aber, was im Wolf lebt, was im Lamm lebt, was da drinnen ist, was nicht gesehen werden kann mit physischen Augen, das wird gesehen, wahrgenommen im Leben zwischen Tod und neuer Geburt.",
      "Wenn also gesagt wird, daß die Vorstellungen gebunden sind an den physischen Leib, so darf niemand daraus den Satz ableiten, daß der Mensch ohne Vorstellungen oder, besser gesagt, ohne den Inhalt der Vorstellungen wäre im Lehen zwischen dem Tode und einer neuen Ge­burt. Nur das, was die Vorstellungen ausarbeitet, das verschwindet. Was wir als unser Vorstellungsleben haben, das hat also, wie wir es hier",
      "in der physischen Welt erleben, auch nur eine Bedeutung für das Leben in dieser Inkarnation. Und ich habe auch schon angeführt, daß in An­knüpfung an das Bewußtsein, daß dieses für die sinnliche Welt in einer Inkarnation geltende Vorstellungsleben nur für diese gilt, Friedrich Hebbel einmal einen netten Plan zu einem Drama in seinem Tagebuch entworfen hat. Er hatte die Idee, daß der wiederverkörperte Plato in einer Gymnasialklasse wäre und auf den Lehrer bestimmt den schlech­testen Eindruck machen würde und am meisten schlechte Zensuren be­kommen könnte, weil er den Plato gar nicht versteht! Das ist auch ein Hinweis darauf, wie das Gedankengebäude des Plato, das gedanken-mäßig in ihm gelebt hat, eben nicht in dieser Form hinüberlebt in die nächste Inkarnation.",
      "Um über diese Dinge vernünftige Gedanken zu bekommen, muß man das Seelenleben des Menschen von einem gewissen Gesichtspunkt aus betrachten. Da muß man sich fragen: Was tragen wir für einen Inhalt in unserem Seelenleben mit uns herum?",
      "Das erste sind unsere Vorstellungen. Daß diese Vorstellungen, zu­sammengedrängt mit Gefühlen, zu Willensimpulsen führen können, das hindert nicht, daß wir von einem besonderen Vorstellungsleben in unserer Seele sprechen können. Denn wenn es auch Menschen gibt, die sich kaum halten können, möchte man sagen, bei einer reinen, bloßen Vorstellung, die, wenn sie sich etwas vorstellen, mächtig in Sympathie oder Antipathie aufflammen, also gleich zu anderen Seelenimpulsen übergehen, so hindert das doch nicht, daß das Vorstellungsleben abge­trennt werden kann von anderen Seeleninhalten.",
      "Das zweite, was wir in unserem Seelenleben herumtragen, sind die Gefühlserlebnisse. Diese treten ja in einer recht vielgestaltigen Weise in uns auf. Da ist der allbekannte Gegensatz im Gefühlsleben, den man bezeichnen kann mit Sympathie und Antipathie, die wir den Dingen entgegenbringen, oder wenn man es deutlicher bezeichnen will: Liebe und Haß. Dann sind da die Gefühle, die man bezeichnen kann als die, welche eine gewisse Erregung bewirken, und wieder die, welche eine gewisse Spannung und Entspannung bewirken. Die lassen sich nicht zusammenwerfen mit den Gefühlen der Sympathie und der Antipathie. Denn ein Seelenimpuls, den man eine Spannung, eine Erregung und",
      "eine Entspannung nennen kann, ist etwas anderes als das, was sich bloß in Sympathie oder Antipathie auslebt. Aber man müßte viel reden, wenn man die verschiedenen Gattungen der Gefühlsinhalte charakteri­sieren wollte. Es gehören auch dazu die, welche man bezeichnen kann als die Gefühle für das Schöne und für das Häßliche, die als ein ganz besonderer Seeleninhalt sich ausnehmen, die sich nicht vergleichen las­sen mit den bloßen Sympathie- und Antipathiegefühlen, wenigstens sich nicht mit ihnen zusammenwerfen lassen. Dann auch könnten wir die Gefühle, die wir haben für Gut und Böse, als eine besondere Gat­tung bezeichnen. Es ist heute nicht die Zeit, um auszuführen, wie das innere Erlebnis, das wir an einer guten oder einer bösen Handlung haben, etwas ganz anderes ist als das Gefühl der Sympathie oder Anti­pathie für eine gute oder böse Handlung, daß wir die gute Handlung lieben, die böse hassen. So treten uns die Gefühle in der mannigfal­tigsten Gestalt entgegen, und wir können sie unterscheiden von den Vorstellungen.",
      "Eine dritte Art von Seelenerlebnissen sind die Willensimpulse, das Willensleben. Das darf wieder nicht zusammengeworfen werden mit dem, was wir Gefühlserlebnisse nennen können, was innerhalb unseres Seelenlebens beschlossen bleiben muß oder kann durch die Art, wie wir es erleben. Zu einem Willensimpuls gehört, daß sich in der Seele aus­drückt: Du sollst dies tun, du sollst jenes nicht tun. - Denn man sollte unterscheiden lernen zwischen dem bloßen Gefühl, das man hat von dem, was einem an sich selber oder an einem anderen als gut oder böse erscheint, und zwischen dem, was mehr als dieses Gefühl in der Seele auftritt, wenn wir gedrängt werden, das Gute zu tun, das Böse zu las­sen. Die Beurteilung kann beim Gefühl stehenbleiben; aber etwas an­deres sind die Willensimpulse. Und obwohl Übergänge sind zwischen dem Gefühlsleben und den Willensimpulsen, sollte man schon aus Gründen der gewöhnlichen Lebensbeobachtung diese nicht ohne wei­teres zusammenwerfen. Im menschlichen Leben sind überall Übergänge. Wie es Menschen gibt, die zu gar keiner reinen Vorstellung kommen, sondern immer gleich zum Ausdruck bringen, was sie lieben oder has­sen, die immer hin- und hergeworfen werden, weil sie ihre Gefühle nicht absondern können von ihren Vorstellungen, so gibt es auch andere,",
      "die, wenn sie etwas sehen, gar nicht davon ablassen können, zu etwas überzugehen, was einem Willensimpuls entspricht, zu einer Handlung, auch wenn diese Handlung gar nicht berechtigt ist. Das führt wieder zu nichts Gutem; das tritt dann als Stehlsucht, als Klepto­manie und so weiter auf. Da ist kein geordnetes Verhältnis zwischen den Gefühlen und den Willensimpulsen. Aber in Wahrheit sind diese Dinge in der strengsten Weise zu unterscheiden. So leben wir in un­serem Seelenleben innerhalb der Vorstellungen, innerhalb der Ge­fühlserlebnisse und innerhalb der Willensimpulse. Wir haben solche Betrachtungen schon öfter angestellt; man kann ohne sie, wenn man den gesamten Menschen ins Auge fassen will, nicht auskommen.",
      "Nun haben wir versucht, einiges anzuführen von dem, was uns nahelegen kann, daß das Vorstellungsleben etwas ist, was gebunden ist an die einmalige Inkarnation zwischen Geburt und Tod. Wir sehen ja auch, wie wir in das Leben hereintreten und uns das Vorstellungsleben aneignen.",
      "So ist es nicht mit dem Gefühlsleben, auch nicht mit dem Wil­lensleben. Wer behaupten wollte, es wäre so, von dem könnte man den­ken, er würde nie vernünftig die Entwickelung eines Kindes betrachtet haben.",
      "Man betrachte nur ein Kind, wenn es noch ganz dumm ist in be­zug auf das Vorstellungsleben, wie es sich gar nicht in Verbindung set­zen kann mit der Umwelt mit seinen Vorstellungen, wie es dagegen aus­gesprochene Sympathien und Antipathien hat, wie es dann wieder an-und abregende Willensimpulse hat. Und die Bestimmtheit, mit der die Willensimpulse auftreten, verführte sogar einen Philosophen, Schopen­hauer, zu dem Glauben, daß der Charakter eines Menschen überhaupt so auftritt, daß er gar nicht geändert werden kann im Leben.",
      "Es ist das nicht richtig; er kann geändert werden. Aber es ist so, wenn wir herein-treten in das physische Leben, daß wir sagen müssen: Es verhält sich mit den Gefühlen und Willensimpulsen keineswegs so wie mit den Vor­stellungen, sondern wir treten mit einem ganz bestimmten Charakter unserer Gefühlserlebnisse und Willensimpulse in die Inkarnation her­ein.",
      "Bei einer richtigen Betrachtung könnten wir schon ahnen, daß wir in den Gefühlen und in den Willensimpulsen etwas haben, was wir uns aus früheren Inkarnationen mitbringen. Aber fassen Sie das zusammen in ein gefühlsmäßiges Gedächtnis im Gegensatz zu dem Vorstellungsgedächtnis",
      "in dem einen Leben. Man kann im Praktischen nicht aus­kommen, wenn man nur eine Vorstellungserinnerung gelten läßt. Alles, was wir im Vorstellungsleben entwickeln, kann uns nicht zu irgend etwas führen, was einen solchen Eindruck hervorrufen könnte, der, wenn wir ihn richtig verstehen, uns sagt: Da hast du etwas in dir, was durch die Geburt mit dir in diese Inkarnation hereingetreten ist. Da müssen wir über das Vorstellungsleben hinausgehen, da muß das Be­sinnen etwas anderes werden. Und da haben wir angeführt, was jetzt das Besinnen wird. Wie besinnen wir uns? Wir besinnen uns so, daß wir uns nicht bloß vorstellen: Das war zufällig in unserem Leben, das ha­ben wir getroffen, da waren wir in einer Lebensiage, die haben wir ver­lassen und so weiter. - Wir dürfen nicht bei den Vorstellungen blei­ben, sondern wir müssen sie lebendig, regsam machen, wie wenn das Bild einer Persönlichkeit vor uns stünde, die das gewollt hat, die in unseren Begehrun gen, Wil lensimpulsen, Gefühlserlehnissen und so wei­ter dies gewollt hat. In das Wollen müssen wir uns hineinleben. Also, es ist ein ganz anderes Sich-Hineinleben als jenes, was als Sich-Hinein-leben in das Vorstellungsleben beim Gedächtnis in Frage kommt; es ist ein Sich-Hineinleben in andere Seelenkräfte, wenn der Ausdruck ge­braucht werden darf.",
      "Diese Praxis, sozusagen wollend, wünschend, begehrend einen See­leninhalt zu entwickeln - die in allen okkulten Schulen, in aller okkul­ten Praxis immer bekannt war und angewendet worden ist -, läßt sich gut mit dem, was wir zu sagen wissen aus der anthroposophischen oder sonstigen Erkenntnis über Vorstellungs-, Gefühls- und Willensleben, rechtfertigen, läßt sich damit begreifen und erklären. Also sagen wir uns klar, daß wir an den besonderen Inhalten des Gefühlslebens, des Willenslebens etwas entwickeln müssen, das gewissermaßen den Erin­nerungsvorstellungen ähnlich ist, aber eben nicht bei den bloßen Vor­stellungen bleibt, daß wir aber dadurch in die Lage kommen, eine an­dere Art, nämlich eine solche Art von Erinnerungsvermögen zu ent­wickeln, die uns allmählich hinausführt über das Leben, das zwischen Geburt und Tod in der einen Inkarnation eingeschlossen ist.",
      "Es muß durchaus betont werden, daß der Weg, der hier gekennzeich­net worden ist, ein absolut guter und sicherer ist - aber ein entsagungsvoller.",
      "Leichter ist es, aus irgendwelchen äußeren Gründen sich einzu­bilden, daß man in der vorhergehenden Inkarnation Marie Antoinette, Maria Magdalena und dergleichen gewesen sei. Aber schwieriger ist es, auf die geschilderte Art und Weise, aus dem in der Seele Vorhandenen, aus wirklich Vorhandenem, zu einem Bilde dessen zu kommen, was man war. Es ist zunächst deshalb recht entsagungsvoll, weil man mei­stens recht enttäuscht werden kann. Wenn aber jemand nun sagen wür­de, das kann alles etwas sein, was wir uns vormachen, so muß man erwidern: Aber es kann sich auch jemand in bezug auf seine Erinne­rungen etwas vormachen, was nicht stimmt. - Diese Dinge sind alle kein Einwand. Eine Art von Kriterium, um die Einbildung von der Phantastik zu unterscheiden, gibt es bloß im Leben.",
      "In einer süddeutschen Stadt sagte einmal jemand zu mir, es könnte alles, was in meiner «Geheimwissenschaft im Umriß» vorgebracht ist, auf einer bloßen Suggestion beruhen, wie es ja sehr lebendige Suggestio­nen gibt, die sogar soweit gehen können, daß jemand, wenn er gar keine Limonade trinkt und sich nur die Limonade recht lebhaft vorstellt, schon den Geschmack der Limonade im Munde hat. Wenn also so etwas möglich ist, warum sollte es dann nicht auch möglich sein, so dachte der Betreffende, daß das in der «Geheimwissenschaft» Vorgebrachte auch auf Suggestionen beruhen sollte?",
      "Theoretisch läßt sich ein solcher Einwand machen. Aber das Leben bringt die Überlegung: Wenn je­mand meint, mit dem Beispiel der Limonade zeigen zu können, wie stark die Suggestion wirken kann, so muß man dazu sagen, der hat nicht verstanden, das Beispiel zu Ende zu denken, denn er sollte einmal probieren, nicht bloß die Limonade sich vorzustellen, sondern sich mit einer bloß vorgestellten Limonade den Durst zu löschen - da wird er sehen, daß es nicht geht.",
      "Es handelt sich immer darum, daß wir an das Ende gehen mit den Erlebnissen. Das läßt sich aber nicht theoretisch bestimmen, sondern nur im unmittelbaren Leben selber erfahren. Und mit derselben Notwendigkeit, mit der wir wissen, daß wir etwas, was herauftaucht aus den Erinnerungsvorstellungen des Lebens, erlebt ha­ben, mit derselben Sicherheit tritt auch das auf, daß herauftauchen aus den Untergründen der Seele die Willensimpulse, die wir hervorrufen über das Zufällige, über das Nichtgewollte, und die mit derselben Notwendigkeit",
      "auftauchen als ein Bild unseres früheren Erdenlebens wie die Erinnerungsvorstellungen. Dem, der nun sagt, das kann Einbildung sein, dem können wir dafür keine Beweise bringen, wie man theore­tisch auch keinen Beweis bringen kann für das, was sich zahlreiche Menschen einbilden, erlebt zu haben und ganz bestimmt nicht erlebt haben, und für das, was sie wirklich erlebt haben. Ebensowenig wie man da einen theoretischen Beweis vorbringen kann, ebensowenig gibt es einen theoretischen Beweis für das andere. Also, man ist dabei in kei­ner anderen Lage, als man ist in dem Leben innerhalb der einen Inkar­nation; man ist genau in derselben Lage.",
      "So haben wir mit diesem gezeigt, wie früheres Erdenleben herein-leuchtet in das gegenwärtige Erdenleben, wie wir wirklich eine Mög­lichkeit haben, durch sorgfältige Seelenentwickelung uns selber die Überzeugung zu verschaffen, nicht nur die theoretische Überzeugung von der Tatsache der Reinkarnation, sondern die praktische Überzeu­gung von dem in uns befindlichen, sich reinkarnierenden Seelenwesen, von dem wir wirklich wissen, es ist etwas, was einmal da war.",
      "Aber es gibt dennoch Erlebnisse ganz anderer Art, die hereintreten in unser Leben und von denen wir nicht sagen können, sie treten so in unser Leben herein, daß wir sie wie eine Erinnerung an ein früheres Erdenleben auffassen können. Es gibt tatsächlich solche Erlebnisse, de­nen gegenüber wir sagen müssen: Wie sie dir da gegenübertreten, so erklären sie sich dir aus deinem früheren Leben nicht! Heute sei nur auf eine Art solcher Erlebnisse hingewiesen. Und auf diese Art von Erleb­nissen will ich zunächst hinweisen, indem ich ein typisches Beispiel an­führe. Dies, was ich als Beispiel anführe, das kann sich auf hunderter­lei Weise, auf tausenderlei Weise vollziehen; aber es ist eben das, was sich da vollzieht, ähnlich dem, was ich als ein typisches Beispiel er­zählen will.",
      "Wir nehmen einen Menschen an, der irgendwo in einem Walde geht, und der, weil er in Gedanken gegangen ist, vergißt, daß er auf einem Waldeswege geht, der unmittelbar - man braucht nur einige Schritte zu machen - an einen tiefen Abgrund angrenzt. Ich will die Sache, die sich durchaus abspielen kann, in dieser Form hier vorbringen; das Bei­spiel ist von mir, weil in entsprechender Weise mir ein ganz ähnlich",
      "gearteter Fall bekannt ist, auch anderswo erzählt worden. Dieser Mensch sieht nun nicht, daß dort ein Abgrund ist, weil ihn etwas be­sonders interessiert. Weil ihn eben sein Problem so stark interessiert, geht er auf den Abgrund los, aber mit einem solchen Schwunge, daß es ihm, wenn er nur zwei, drei Schritte mehr gemacht hätte, unmöglich gewesen wäre, sich zu halten. Er hätte dann im Vorwärtsschreiten hin­unterstürzen müssen, und es wäre mit seinem Leben zu Ende gewesen. In dem Augenblick aber, wo er drauflostapsen will, hört er eine Stim­me: Bleibe stehen! - Die Stimme macht einen solchen Eindruck auf ihn, daß er wie angenagelt stehen bleibt. Der Betreffende denkt, es muß jemand da sein, der sich seiner angenommen hat. Er hat sich besonnen, daß sein Leben zu Ende gewesen wäre, wenn er nicht auf diese Weise festgehalten worden wäre. Er sieht sich um, und sieht niemanden.",
      "Der materialistische Denker wird nun sagen: Durch irgendwelche Umstände hat sich aus den Tiefen der Seele eine Gehörshalluzination ergeben, und es ist ein glücklicher Zufall gewesen, daß der Betreffende auf diese Weise gerettet worden ist. - Aber es ist auch möglich, auf andere Weise über die Sache zu denken; mindestens müßte man dies zu­geben. Ich will es heute nur anführen; denn diese andere Weise läßt sich nur erzählen, nicht beweisen. Man kann sich sagen: Durch Vor­gänge der geistigen Welt ist dir in dem Augenblick, als du an einer karmischen Krisis angekommen warst, dein Leben eigentlich geschenkt worden. Wenn alles so weitergegangen wäre, ohne daß jenes Ereignis geschehen wäre, dann wäre dein Leben zu Ende gewesen. So aber ist es jetzt als eine Art neues Leben an das vorhergehende angestückelt wor­den. Dieses neue Leben ist eine Art Geschenk, und du verdankst jetzt dieses dein Leben den Mächten, die hinter dieser Stimme stehen! - Ein solches Erlebnis könnten viele, viele Menschen der Gegenwart haben, wenn sie nur wirkliche Selbsterkenntnis üben würden. Denn es treten in das Leben geradezu vieler, vieler Menschen der Gegenwart solche Erlebnisse herein. Und es liegt nicht daran, daß die Menschen nicht ein solches Erlebnis gehabt haben, sondern daran, daß die Menschen nicht die nötige Aufmerksamkeit dafür gehabt haben, daß sie darüber hin­weggegangen sind; denn es tritt nicht immer mit dieser jetzt geschilderten",
      "Deutlichkeit auf, sondern so, daß bei der gewöhnlichen Unauf­merksamkeit die Menschen darüber hinwegsehen.",
      "Ich habe zuweilen geschildert, wie stark die Menschen hinwegsehen über etwas, was in der unmittelbaren Gegenwart der Menschen auftritt. Ein charakteristisches Beispiel dafür, wie die Menschen für das, was rings um sie her vorgeht, unaufmerksam sind, ist folgender Fall. Ich kannte einen Schulinspektor eines Landes, wo das Gesetz eingeführt wurde, daß ältere Lehrer, die gewisse Examina nicht abgelegt hatten, überprüft werden müßten. Nun war dieser Schulinspektor ein außer­ordentlich humaner Mensch und sagte sich: Die jüngeren Dachse, die eben vom Seminar gekommen sind, kann man ja über alles fragen; aber die älteren Herren zu fragen, die bereits zwanzig, dreißig Jahre im Amte sind, das ist eine Grausamkeit, die kann man nicht so fragen. Ich frage diese daher am besten über das, was in ihren Büchern steht, aus denen sie Jahr für Jahr die Kinder unterrichten. - Und siehe da:",
      "die meisten wußten nichts von dem, was sie selbst ihren Schülern vortrugen! Und zwar war das ein Examinator, von dem man sagen konnte: er wußte schon aus den Menschen das herauszuziehen, was sie wußten!",
      "Es sollte das nur ein Beispiel dafür sein, wie die Menschen unauf­merksam sind für das, was in ihrer Umgebung vorgeht, ja sogar für das, wo es sich um ihre eigene Person handelt. Man braucht also nicht er­staunt zu sein, wenn ein ähnliches Beispiel, wie das jetzt charakteri­sierte, im Leben vieler, vieler Menschen zu finden ist. Nur bei einer sinnigen, wirklichen Selbstbetrachtung findet man ein solches Ereignis, wie es eben beschrieben worden ist. Und wenn man einem solchen Er­eignis gegenüber die rechte Lebensfrömmigkeit hat, dann kommt man vielleicht auch zu einem ganz besonderen Gefühl; zu dem Gefühl, daß einem das Leben seit jenem Tage geschenkt ist, und daß man, soweit es seit jenem Tage verläuft, es auch in einer besonderen Weise anzuwen­den hat. Das ist ein gutes Gefühl und wirkt ähnlich wie ein Erinne­rungsvorgang, wenn jemand sich sagt: Du warst an einer karmischen Krisis, da war dein Leben abgeschlossen! - Wenn er sich hineinver­tieft in dieses fromme Gefühl, dann kommt etwas, was zunächst so auftritt, daß er sich sagt: Das ist nicht eine Erinnerungsvorstellung",
      "wie die, welche ich im Leben öfter erfahren habe, das ist etwas ganz Besonderes!",
      "Nun werde ich Ihnen im nächsten Vortrag Genaueres sagen können über das, was heute nur angedeutet werden kann. Denn so, wie es jetzt angedeutet worden ist, so prüft ein großer Eingeweihter der neueren Zeit die, welche er für geeignet hält zu seinen Bekennern.",
      "Denn die Dinge, die uns hineinstellen sollen in die geistige Welt, gehen auch aus den geistigen Tatsachen, die um uns herum geschehen, oder aus einer richtigen Erkenntnis dieser Tatsachen hervor. Und eine solche Stimme, wie sie bei vielen Menschen auftritt, ist nicht als eine Halluzination zu betrachten; denn durch eine solche Stimme spricht derjenige Führer, den wir als Christian Rosenkreutz bezeichnen, zu denen, die er sich aus der übrigen Schar auswählt als die, welche seine Bekenner werden kön­nen.",
      "So ergeht der Ruf von der Individualität, von der wir noch wer­den sprechen können als derjenigen, welche in einer besonderen Inkar­nation im 13. Jahrhundert gelebt hat, so daß ein Mensch, der so etwas erlebt, daran ein Merkzeichen, ein Erkennungszeichen hat, durch das er sich hineinstellen kann in die geistige Welt.",
      "Vielleicht werden nicht viele dazu kommen können, einen solchen Ruf zu beachten. Aber die Anthroposophie wird schon dahin wirken, daß die Menschen, wenn nicht jetzt in dieser Inkarnation, so doch später einen solchen Ruf be­achten werden.",
      "Für die meisten Menschen, die so etwas erleben, ist es nun heute so, daß dasjenige, was man bezeichnen kann als: Es ist ihnen gegenübergetreten jener Eingeweihte, der sie bestimmt hat zu denen, die zu ihm gehören können -, sich nicht in einer Inkarnation voll­zogen hat, sondern in dem Leben zwischen dem Tode und der jetzigen Geburt, so daß dies also ein Hinweis darauf ist, daß etwas geschieht in dem Leben zwischen dem Tode und der nächsten Geburt, und daß wir darin Wichtiges, ja wichtigere Vorgänge haben als im Leben zwischen Geburt und Tod. Es kann ja sein und ist in einzelnen Fällen so, daß gewisse zu Christian Rosenkreutz gehörige Menschen auch schon in einer vorhergehenden Inkarnation dazu bestimmt worden sind.",
      "Aber für die meisten ist die Bestimmung, die sich in einem solchen Ereignis abbildet, getroffen worden in dem letzten Leben zwischen Tod und neuer Geburt.",
      "Nun sage ich das nicht, um etwas Sensationelles zu erzählen, nicht einmal um dieses Ereignis zu erzählen, sondern aus einem besonderen Grunde. Und ich möchte dazu noch auf etwas aufmerksam machen, aus einer Erfahrung heraus, die ich innerhalb unseres anthroposophischen Lebens recht häufig gemacht habe: daß Dinge, die man einmal sagt, leicht vergessen oder anders erhalten werden, als man sie sagt. Es soll das vorkommen innerhalb unseres anthroposophischen Lebens. Aus diesem Grunde betone ich manchmal wichtige, wesentliche Dinge ein paarmal, nicht um mich zu wiederholen. Auch heute geschieht das, wenn ich sage, es sind viele Menschen in der Gegenwart, die ein solches Erlebnis, wie es beschrieben worden ist, durchgemacht haben, und daß sie es nicht wissen, liegt nicht daran, daß es nicht da ist, sondern daß man sich nicht daran erinnert, weil man nicht die rechte Aufmerksam­keit darauf verwendet hat. Deshalb soll es ein Trost sein, wenn jemand sich sagen muß: Ich finde nicht so etwas, also gehöre ich nicht zu sol­chen Auserwählten! - Doch kann Ihnen die Versicherung gegeben werden, daß unzählige Menschen in der Gegenwart sind, die so etwas erlebt haben. Das wollte ich nur vorausschicken, um zum eigentlichen Grunde zu kommen, warum so etwas gesagt wird.",
      "Solche Dinge werden erzählt, um uns immer wieder und wieder dar­auf aufmerksam zu machen, daß wir in konkreter Weise - nicht durch abstrakte Theorien - eine Beziehung unseres Seelenlebens zu den gei­stigen Welten finden sollen, und daß die anthroposophische Geistes­wissenschaft uns nicht sein soll eine bloße theoretische Weltanschauung, sondern eine innere Kraft unseres Lebens; daß wir nicht bloß wissen sollen, es gibt eine geistige Welt und der Mensch gehört ihr an; daß wir, indem wir durch das Leben gehen, nicht bloß die Dinge betrachten, die auf unser sinnliches Denken wirken, sondern die Zusammenhänge aufmerksam erfassen, die uns zeigen: Du bist hineingestellt in die geistige Welt, auf diese und jene Weise hineingestellt. - Also das kon­krete Hineingestelitsein, das für den einzelnen reale Hineingestelitsein, das ist es, worauf wir aufmerksam machen. Theoretisch sucht man auch draußen so etwas zu begründen, daß die Welt ein Geistiges haben kann, und daß der Mensch nicht materialistisch zu betrachten ist, son­dern ein Geistiges in sich haben kann. Davon unterscheidet sich unsere",
      "Weltanschauung, indem sie im einzelnen hinstellt: So stehst du im Zusammenhange mit den geistigen Welten! - Immer mehr und mehr werden wir zu solchen Dingen aufsteigen können, die uns zu zeigen vermögen, wie wir die Welt zu betrachten haben, um unsere Zuge­hörigkeit zu dem Geiste der großen Welt, dem Makrokosinischen, ein­zusehen."
    ],
    "sentences": [
      [
        "Die Betrachtungen, die wir das letzte Mal hier angestellt haben, sie werden so, wie sie damals vorgebracht worden sind, noch für man­chen etwas Unverständliches, vielleicht sogar Bedenkliches haben.",
        "Aber wenn wir noch auf dieses oder jenes heute eingehen werden, so wer­den uns die Dinge schon nähertreten können."
      ],
      [
        "Was war es denn eigentlich, was wir uns an dem letzten Zweigabend vor die Seele geführt haben?",
        "Es war gewissermaßen etwas Ähnliches für die Gesamtwesenheit des Menschen, wie dasjenige ist, was ein Mensch vollbringt, wenn er zum Beispiel in dieser oder jener Lebens­lage ist, in der er sich auf frühere Erfahrungen und Erlebnisse besinnen muß, sich an frühere Erlebnisse oder Erfahrungen erinnern soll."
      ],
      [
        "Erin­nerung, Gedächtnis sind ja menschliche Seelenerlebnisse, die für das gewöhnliche Bewußtsein im Grunde zunächst nur gekannt werden für das Seelenleben, welches da verläuft zwischen Geburt und Tod, oder genauer gesagt - was wir ja öfter ausgesprochen haben - für einen Zeitraum, der eigentlich erst in den späteren Kindheitsjahren beginnt, bis zum Tode hin.",
        "Denn wir wissen, daß wir uns für das gewöhnliche Bewußtsein nur erinnern bis zu einem bestimmten Zeitpunkt unserer Kindheit, und daß wir über dasjenige, was vorangegangen ist, allein durch Eltern oder ältere Verwandte und Bekannte etwas erfahren kön­nen."
      ],
      [
        "Wenn wir den eben in dieser Art charakterisierten Zeitraum des Menschenlebens ins Auge fassen, so sprechen wir für diesen Zeitraum in bezug auf das Seelenleben von Erinnerung.",
        "Es ist hier natürlich nicht möglich, in feinerer Weise einzugehen auf die Bedeutungen der Worte «Erinnerungsvermögen» oder «Gedächtnis»; das ist auch für unsere Zwecke nicht notwendig."
      ],
      [
        "Wir müssen uns nur zunächst einmal klar vor die Seele führen, daß zu alledem, was mit diesen Worten bezeichnet wird, eben das Sich-Besinnen auf früher gemachte Erfahrungen oder Erlebnisse gehört.",
        "Was wir nun das letzte Mal betrachteten, war ge­wissermaßen etwas Ähnliches wie dieses Sich-Besinnen; nur sollte diese Ähnlichkeit nunmehr nicht bloß so gelten wie jenes Erinnerungsvermögen,"
      ],
      [
        "das in unser gewöhnliches Leben hereinfällt, sondern es sollte uns gleichsam als ein höheres, erweitertes Erinnerungsvermögen hin-überführen über die gegenwärtige Inkarnation zu einer Art von Ge­wißheit, daß wir vor diesem Erdenleben in anderen Erdenleben da­gewesen sind.",
        "Und wie wir das letzte Mal erwähnt haben, sollte es in bezug auf diesen höheren Prozeß so sein, wie das Sich-Besinnen auf irgend etwas Erlebtes im gewöhnlichen Leben."
      ],
      [
        "Wenn wir uns auf der einen Seite einen Menschen vorstellen, der irgend etwas braucht, was er gelernt hat in einer früheren Zeit seines jetzigen Lebens, und der dann seine Seele dazu stimmt, heraufzuholen aus ihren Tiefen, was er da gelernt hat, um es mit dem gegenwärtigen Blick zu verfolgen, wenn wir uns lebhaft diesen Prozeß der Besinnung vormalen, so haben wir in ihm eine solche Verrichtung, die zu unserem gewöhnlichen Erinne­rungsvermögen gehört.",
        "Was das letzte Mal erwähnt worden ist, sind Verrichtungen der Seele."
      ],
      [
        "Aber diese Verrichtungen der Seele sollten da­zu führen, daß etwas Ähnliches in unserem Inneren auftritt in bezug auf frühere Erdenleben, wie das, was in bezug auf dieses Erdenleben eintritt in der Seele, wenn wir heraufquellen fühlen in der Erinnerung irgend etwas, was wir früher erlebt haben.",
        "Daher dürfen Sie auch nicht das, was das letzte Mal gesagt worden ist, so betrachten, als ob das schon alles wäre, was uns in frühere Erdenleben hineinführen könnte, oder als ob es vor allen Dingen dasjenige wäre, was nun von vorn­herein eine richtige Vorstellung hervorrufen könnte von der Art, wie wir in früheren Erdenleben waren."
      ],
      [
        "Es ist nur eine Hilfe, so wie das Sich-Besinnen auch eine Hilfe ist, um heraufzuholen, was in die Unter­gründe des Seelenlebens hinuntergeschwunden ist.",
        "Fassen wir kurz zu­sammen, was wir über solches Sich-Besinnen in bezug auf frühere Erdenleben ins Auge gefaßt haben."
      ],
      [
        "Das kann am besten in folgender Weise geschehen."
      ],
      [
        "Bei einiger Selbsterkenntnis fällt uns in unserem Leben manches auf, wovon wir uns sagen, wir begreifen, daß uns das getroffen hat.",
        "Wenn uns irgendein mißliches Ereignis trifft und wir auch nicht ganz ein­sehen, wieso dieses Ereignis hat kommen müssen, uns aber doch sagen:"
      ],
      [
        "Du bist eigentlich doch ein recht leichtsinniger Mensch; es ist kein Wunder, daß dir das begegnet ist -, so ist wenigstens etwas wie ein"
      ],
      [
        "Anklang da an ein Verständnis dafür, daß uns so etwas getroffen hat.",
        "Aber es gibt zahlreiche andere Erlebnisse, die hereintreten in das Leben und von denen wir uns durchaus nicht die Vorstellung bilden können, daß sie zusammenhängen mit unseren Seelenkräften und Fähigkeiten.",
        "Wir sprechen dann wohl im gewöhnlichen Leben so, daß wir von Zu­fälligkeiten reden.",
        "Von Zufälligkeiten sprechen wir dann, wenn wir nicht einsehen, wie die Dinge, die uns als Schicksalsschläge treffen, mit unserer inneren Seelenstimmung oder sonstigem zusammenhängen.",
        "Auch auf andere Erlebnisse ist aufmerksam gemacht worden.",
        "Es sind das diejenigen Seelenerlebnisse, bei denen wir gewissermaßen durch das, was wir unser gewöhnliches Ich nennen, uns herausreißen aus ir­gendeiner Lebenslage, in die wir aber eigentlich hineingestellt sind.",
        "Als Beispiel ist angeführt worden, wenn jemand von seinen Eltern oder ihm nahestehenden Menschen zu irgendeinem Berufe oder irgendeiner Le­benslage bestimmt worden ist, er aber sich so fühlt, daß er mit aller Gewalt da heraus und zu etwas anderem will.",
        "Wenn wir im späteren Leben auf so etwas zurückblicken, so sagen wir uns: Wir waren hinein-versetzt in eine Lebenslage, aber wir haben uns durch unseren Willens-impuls, durch unsere Sympathie und Antipathie daraus herausgeris­sen. - Also von solchen gleichsam Umwendungen dessen, in das wir hineingestellt sind, ist gesprochen worden."
      ],
      [
        "Es handelt sich nicht darum, daß wir bei so einer Rückerinnerung alles mögliche ins Auge fassen, sondern nur dasjenige, was uns wirklich im Leben einmal nahegetreten ist.",
        "Wenn jemand zum Beispiel niemals in sich den Beruf gefühlt hat, oder keine Veranlassung gehabt hat, Seefahrer zu werden, so kommt natürlich ein solcher Willensimpuls durchaus nicht in Betracht für die Erwägungen, die wir das letzte Mal angestellt haben, sondern nur solche, wo wir wirklich eine Art Schick­salswendung herbeigeführt haben; also Lagen des Lebens, bei denen wir gleichsam eine Umwendung des Lebens herbeigeführt haben.",
        "Und auch das fassen Sie nicht so auf, als ob durch dieses Sich-Besinnen auf seine früheren Erlebnisse, nach den entwickelten Grundsätzen, etwa ein­treten sollte ein reuiges Zurückkehren; so daß, wenn wir uns im spä­teren Leben an dergleichen erinnern und zu der Erkenntnis kommen, wir haben uns da herausgerissen, wir nun reuig zurückkehren und uns"
      ],
      [
        "wieder hineinstellen sollten, in was wir dazumal hineingestellt waren und nicht drinnen geblieben sind.",
        "Nicht um praktische Konsequenzen handelt es sich, sondern um das Sich-Besinnen, wo solche Wendungen eingetreten sind.",
        "Und dann handelt es sich darum, daß wir in ener­gischster Weise solchen Dingen gegenüber, wovon wir sagen: Es trat zufällig an uns heran -, und: Wir waren hineingestellt, haben uns aber herausgerissen -, folgendes innere Erlebnis herbeiführen."
      ],
      [
        "Wir sagen uns: Ich stelle mir vor, daß das, was ich damals nicht ge­wollt habe, aus dem ich mich herausgerissen habe, ein solches gewesen wäre, in das ich mich mit dem stärksten Willensimpuls hineingestellt habe.",
        "Also das, was einem antipathisch war - und weil es einem anti­pathisch war, deshalb hat man sich herausgerissen -, das stelle man sich so vor die Seele, daß man sich sagt: Ich will mich probeweise der Vorstellung hingeben, daß ich das mit aller Gewalt gewollt habe, und ich will mir das Bild eines Menschen vor die Seele stellen, der so etwas mit aller Gewalt gewollt hätte. - Und von denjenigen Dingen, von denen wir gesagt haben, sie seien Zufälligkeiten, stellen wir uns auch vor, probeweise, wir hätten sie herbeigeführt.",
        "Nehmen wir an, es sei uns nur einmal die Erinnerung nahegetreten, da oder dort wäre uns ein Mauerstein auf die Schulter gefallen und hätte uns recht weh getan.",
        "Da wollen wir uns der Vorstellung hingeben: wir wären auf das Dach hinaufgestiegen, hätten dort den Mauerstein gelockert, so daß er im nächsten Augenblick herunterfallen muß und dann wären wir schnell hinuntergerannt, so daß der Stein dann auf uns herunterfallen mußte.",
        "Es handelt sich hierbei nicht darum, daß es groteske Vorstellungen sind, sondern um das, was wir damit erreichen wollen."
      ],
      [
        "Nun versetzen wir uns so recht in die Seele eines Menschen, von dem wir so ein Bild konstruiert haben, als ob der alles das gewollt hätte, was uns nur «zufällig» getroffen hat, und alles das gewünscht hätte, aus dem wir uns herausgerissen haben.",
        "Nur erfolgt in der Seele nichts, wenn man eine solche Übung zwei-, drei-, viermal macht, aber sehr viel erfolgt, wenn man das in Anknüpfung an die zahlreichsten Erlebnisse macht, die man finden wird, wenn man sie sucht.",
        "Wenn man dies immer wieder und wieder macht und es sich recht lebendig vorstellt, wenn man sich geradezu einen Menschen imaginiert, der das alles gewollt hätte, was"
      ],
      [
        "wir nicht gewollt haben, dann wird man die Erfahrung machen, daß dieses Menschenbild, das man sich da vor die Seele gerufen hat, uns nicht mehr losläßt, daß es einen ganz merkwürdigen Eindruck auf uns macht, als wenn es tatsächlich etwas wäre, das mit uns etwas zu tun hätte.",
        "Wenn man sich auf solche Art etwas Feinheit aneignet in bezug auf eine derartige Selbstprüfung, dann wird man bald dazu kommen, die Ähnlichkeit herauszufinden, welche besteht zwischen einer solchen Stimmung und einem solchen Bilde, das man da konstruiert hat, und zwischen einer solchen Vorstellung, die man heraufgerufen hat aus dem Gedächtnis, bei der man spürt, wie sie da kommt als eine Erinnerungs­vorstellung."
      ],
      [
        "Der Unterschied ist nur der, daß man bei dem gewöhn­lichen Gedächtnisvorgang, bei dem man eine solche Vorstellung aus der Seele heraufschafft, es vorzugsweise zu tun hat mit Vorstellungen; da­gegen ist das, was in unserer Seele lebendig wird, wenn wir jene Übun­gen machen, von denen gesprochen worden ist, etwas Gefühlsartiges, etwas, was mehr mit unseren Seelenstimmungen zusammenhängt, we­niger mit unseren Vorstellungen.",
        "Wir fühlen uns in einer sonderbaren Weise gegenüber diesem Bilde."
      ],
      [
        "Auf das Bild kommt es weniger an; aber die Gefühle, die wir haben, machen einen den Erinnerungsvorstellun­gen ähnlichen Eindruck.",
        "Und wenn wir dann so etwas wiederholen und immer wieder und wieder wiederholen, dann ergibt sich erfahrungs­gemäß, ganz wie durch eine innere Selbstverständlichkeit die Erkennt­nis, könnte man sagen, daß das Bild, das man sich da konstruiert hat, etwas wird, so wie eine Erinnerungsvorstellung auch immer klarer und klarer wird, während sie zuerst, wenn man sich willkürlich besinnt, dunkel heraufgeholt wird aus den Seelentiefen."
      ],
      [
        "Also nicht darum han­delt es sich, was man da vorstellt, sondern daß sich das verwandelt, was man da vorstellt, daß es etwas anderes wird.",
        "Es geht so ein Prozeß vor, wie wenn jemand sich auf einen Namen besinnen will, und er druckst und druckst und hat einen Anklang, und er sagt dann: Nuß - - bau­mer -, aber er hat dann ein Gefühl, daß das doch nicht stimmt, und dann gesellt sich durch Gründe, die er selbst nicht übersehen kann, der richtige Name, vielleicht: Nußdörfer - hinzu."
      ],
      [
        "So wie sich hier die Namen «Nußbaumer» und «Nußdörfer» gegenseitig konstruieren, so wird sich auch das Bild zurechtrücken, wird sich ändern, und demgegenüber"
      ],
      [
        "tritt das Gefühl auf: Du hast da etwas erlangt, was in dir steckt, und was durch die Art, wie es in dir steckt und sich verhält zu deinem ganzen übrigen Gemütsleben, dir deutlich zeigt: so können diese Dinge nicht in dir gewesen sein in der jetzigen Inkarnation! -Dadurch ergibt sich dann mit einer großen inneren Deutlichkeit, daß so etwas, wie es da in uns steckt, zurückliegt.",
        "Wir müssen jetzt nur be­greifen, daß wir es hier mit einer Art von Erinnerungsvermögen zu tun haben, das ausgebildet werden kann in der menschlichen Seele; ein Er­innerungsvermögen, das man dem gewöhnlichen Erinnerungsvermögen gegenüber mit einem anderen Namen bezeichnen muß.",
        "Das gewöhn­liche Erinnerungsvermögen könnte man bezeichnen mit dem Worte «Vorstellungserinnerung»; aber dieses Erinnerungsvermögen, das jetzt in Frage kommt, müßte man eigentlich als eine Art von «Gefühls- und Empfindungserinnerung» bezeichnen.",
        "Daß dies eine gewisse Berechti­gung hat, kann Ihnen aus folgenden Erwägungen hervorgehen."
      ],
      [
        "Bedenken Sie, daß tatsächlich unser gewöhnliches Gedächtnis, unser gewöhnliches Erinnerungsvermögen eine Art Vorstellungserinnerung gibt.",
        "Besinnen Sie sich nur einmal darauf, wie irgendein besonders schmerzliches Ereignis, das Sie vielleicht vor zwanzig Jahren ganz nie­dergedrückt hat, herauftaucht in der Erinnerung.",
        "Vielleicht malt sich Ihnen dieses Ereignis mit allen Einzelheiten bildlich ab, aber den Schmerz, den Sie damals durchgemacht haben, fühlen Sie in der Erin­nerung nicht mehr in der entsprechenden Weise; der ist in einer gewis­sen Weise aus der Erinnerungsvorstellung getilgt.",
        "Selbstverständlich gibt es da verschiedene Grade, und es kann ja vorkommen, daß einen Menschen etwas so getroffen hat, daß immer wieder und wieder neuer und heftiger Schmerz auftritt, wenn er sich an das Erlebte erinnert.",
        "Aber der allgemeine Satz, der jetzt ausgesprochen ist, gilt dennoch, so daß wir daraus erkennen, daß für die gegenwärtige Inkarnation unser Erinnerungsvermögen ein Vorstellungserinnern ist, während die erleb­ten Gefühle oder selbst Willensimpulse nicht mit derselben Intensität wieder auftauchen in der Seele, jedenfalls nicht so, daß sie sich mit der ursprünglichen vergleichen ließe.",
        "Sie brauchen sich nur ein charak­teristisches Beispiel zu vergegenwärtigen und Sie werden sehen, wie groß der Unterschied ist zwischen der Vorstellung, die in der Erinnerung"
      ],
      [
        "auftaucht, und dem, was übriggeblieben ist im gewöhnlichen Leben in der gegenwärtigen Inkarnation von den durchgemachten Ge­fühlen und Willensimpulsen.",
        "Sie brauchen nur an so etwas zu denken wie an einen Menschen, der seine Memoiren schreibt.",
        "Nehmen wir zum Beispiel an, Bismarck wäre beim Schreiben seiner Memoiren bis an den Punkt gekommen, wo er den Deutsch-Österreichischen Krieg vom Jahre 1866 vorbereitet hat, und stellen Sie sich vor, was in Bismarcks Seele vorgegangen sein mag an jenem unendlich kritischen Punkt, wo er gegen eine Welt von Vorurteilen und gegen eine Welt von Willensim­pulsen die Ereignisse gelenkt und geleitet hat.",
        "Und nun stellen Sie sich nicht mehr vor, wie das alles damals in Bismarcks Seele gelebt hat, sondern daß alles, was er dazumal unmittelbar unter dem Eindruck der Ereignisse erlebt hat, hinuntergesunken ist in die Tiefen der Seele, und denken Sie an die Verblaßtheit, die eingetreten sein muß gegenüber den Gefühlen und Willensimpulsen, die vorhanden waren, als er die Sache ausführte, im Vergleich zu der Zeit, als er seine Memoiren niederge­schrieben hat.",
        "Kein Mensch wird sich darüber unklar sein, welcher Un­terschied besteht zwischen dem Vorstellungsmäßigen der Sache und demjenigen, was den Gefühlen und Willensimpulsen angehört."
      ],
      [
        "Wer nun schon ein wenig an Anthroposophisches herangekommen ist, der wird auch begreifen, wenn gesagt wird, was hier von anderen Gesichtspunkten aus schon öfter gesagt worden ist: daß unser Vorstel­len, also unser gedächtnismäßiges Vorstellen, dasjenige in unserem Seelenleben ist, was, wenn es angeregt ist von außen durch die äußere Welt, in der wir hier im physischen Leibe leben, eigentlich auch nur seine Bedeutung hat für diese einzelne Inkarnation.",
        "Wir haben immer aus den anthroposophischen Grundsätzen heraus die große Wahrheit angeführt, daß wir von allen Vorstellungen, von allen Begriffen, die wir uns aneignen, indem wir dieses oder jenes sinnlich wahrnehmen, dieses oder jenes im Leben zu fürchten oder zu hoffen haben - das heißt also jetzt nicht mit Bezug auf die Gemütsimpulse, sondern auf die Vorstellungen -, daß dies alles, was wir im Vorstellungsleben haben, sehr bald verschwunden ist, wenn wir durch die Pforte des Todes ge­gangen sind.",
        "Denn die Vorstellungen gehören zu dem, was verfließt im physischen Leben, gehören zu dem, was am wenigsten bleibt.",
        "Aber es"
      ],
      [
        "kann jemand leicht begreifen, der überhaupt schon von irgendeiner Seite her eingegangen ist auf die Gesetze von Reinkarnation und Kar­ma - ich habe es auch hier schon erwähnt -, daß unsere Vorstellun­gen, insoweit wir sie uns aneignen im Leben, das im Verhältnis zur Außenwelt oder zu den Dingen des physischen Planes verfließt, in der Sprache zum Ausdruck kommen, und daß wir uns daher das Sprechen verbunden denken können in einer gewissen Weise mit dem Vorstel­lungsleben.",
        "Nun weiß jeder, daß er das Sprechen irgendeiner Sprache lernen muß in der einzelnen Inkarnation."
      ],
      [
        "Denn während es ganz klar ist, daß eine ganze Anzahl von Gymnasiasten der Gegenwart inkar­niert war im alten Griechenland, wird keinem das Griechischlernen dadurch leichter gemacht, daß er sich erinnern kann, wie er das Grie­chisch in seiner früheren Inkarnation gesprochen hat.",
        "Die Sprache ist durchaus ein Ausdruck des Vorstellungslebens, und das Schicksal der Sprache ist ein ähnliches wie das Schicksal des Vorstellungslebens; so daß die Vorstellungen, wie sie in uns leben mit Bezug auf die physische Welt und selbst die Vorstellungen, die wir gewinnen müssen über die höheren Welten, in einer gewissen Weise immer gefärbt sind von den Eindrücken der physischen Welt."
      ],
      [
        "Nur wenn wir hindurchsehen können durch diese Einkleidung, sehen wir, was die Vorstellungen mitteilen können über die höheren Welten.",
        "Aber, was wir hier in der physischen Welt an unmittelbaren Vorstellungen gewinnen können, das ist auch an das Leben zwischen Geburt und Tod in einer gewissen Weise ge­bunden."
      ],
      [
        "Nach dem Tode bilden wir uns nämlich nicht Vorstellungen in der Art, wie wir sie uns hier bilden, sondern da sehen wir die Vor­stellungen; da sind sie unsere Wahrnehmungen, da sind sie so vorhan­den, wie in der physischen Welt Farben oder Töne vorhanden sind.",
        "Während in der physischen Welt das, was sich der Mensch durch die Vorstellungen vergegenwärtigt, eigentlich nur mit dem physischen Ma­terial ausgedrückt mitgenommen wird, was leicht übersehen werden kann, haben wir im entkörperten Zustande Vorstellungen so vor uns, wie wir Farben oder Töne hier vor uns haben."
      ],
      [
        "Rot oder Blau kann der Mensch allerdings nicht sehen, wie er sie hier mit den physischen Augen sieht; aber, was er hier nicht sieht, worüber er sich hier Vorstellungen bildet, das ist dann für ihn so da, wie Rot oder Grün oder irgendein"
      ],
      [
        "Ton hier.",
        "Während in der physischen Welt das, was wir rein vorstel­lungsmäßig - oder besser gesagt begriffsmäßig im Sinne der «Philo­sophie der Freiheit» - kennenlernen, nur durch den Schleier des Vor­stellungslebens gesehen werden kann, liegt es für die entkörperte Seele so da, wie die physische Welt für das gewöhnliche Bewußtsein."
      ],
      [
        "In der physischen Welt gibt es Menschen, welche das, was der sinn­liche Eindruck gibt, eigentlich für alles halten.",
        "Und was man sich nur durch einen Begriff klarmachen kann, wie zum Beispiel die Art und Weise, wie alles, was die Sinne geben können, umfaßt wird, sagen wir vom Begriff «Lamm», oder wie es umfaßt wird vom Begriff «Wolf», dasjenige also, was aufdröselt das Materielle, das kann von denen, die nur die sinnlichen Eindrücke gelten lassen wollen, sogar geleugnet wer­den.",
        "Wir können sagen: Der Mensch kann sich in seinen Vorstellungen ein Bild machen über alles, was er am Lamm sieht, und kann sich eben­falls ein Bild machen über alles, was er am Wolf sieht.",
        "Nun versucht eine gewöhnliche Anschauung dem Menschen zu suggerieren, daß das, was da begriffsmäßig gebildet werden kann, nur als «bloßer Begriff» anzuschlagen ist.",
        "Aber wenn wir zum Beispiel einen Wolf einsperren würden und ihn längere Zeit hindurch mit lauter Lämmern fütterten, so daß, wenn er früher etwas anderes gefressen hat, dies als Materie jetzt draußen ist, und er angefüllt ist mit lauter Lamm-Materie, so wird doch kein Mensch sich dem Glauben hingeben können, daß der Wolf dadurch ein Lamm geworden sei.",
        "Daher werden wir sagen müssen:"
      ],
      [
        "Da ist es handgreiflich, daß das, was aufdröselt den Sinneseindruck, der Begriff, ein Wirkliches ist.",
        "Doch es wird nicht geleugnet: das, was den Begriff bildet, das stirbt.",
        "Aber, was im Wolf lebt, was im Lamm lebt, was da drinnen ist, was nicht gesehen werden kann mit physischen Augen, das wird gesehen, wahrgenommen im Leben zwischen Tod und neuer Geburt."
      ],
      [
        "Wenn also gesagt wird, daß die Vorstellungen gebunden sind an den physischen Leib, so darf niemand daraus den Satz ableiten, daß der Mensch ohne Vorstellungen oder, besser gesagt, ohne den Inhalt der Vorstellungen wäre im Lehen zwischen dem Tode und einer neuen Ge­burt.",
        "Nur das, was die Vorstellungen ausarbeitet, das verschwindet.",
        "Was wir als unser Vorstellungsleben haben, das hat also, wie wir es hier"
      ],
      [
        "in der physischen Welt erleben, auch nur eine Bedeutung für das Leben in dieser Inkarnation.",
        "Und ich habe auch schon angeführt, daß in An­knüpfung an das Bewußtsein, daß dieses für die sinnliche Welt in einer Inkarnation geltende Vorstellungsleben nur für diese gilt, Friedrich Hebbel einmal einen netten Plan zu einem Drama in seinem Tagebuch entworfen hat.",
        "Er hatte die Idee, daß der wiederverkörperte Plato in einer Gymnasialklasse wäre und auf den Lehrer bestimmt den schlech­testen Eindruck machen würde und am meisten schlechte Zensuren be­kommen könnte, weil er den Plato gar nicht versteht!",
        "Das ist auch ein Hinweis darauf, wie das Gedankengebäude des Plato, das gedanken-mäßig in ihm gelebt hat, eben nicht in dieser Form hinüberlebt in die nächste Inkarnation."
      ],
      [
        "Um über diese Dinge vernünftige Gedanken zu bekommen, muß man das Seelenleben des Menschen von einem gewissen Gesichtspunkt aus betrachten.",
        "Da muß man sich fragen: Was tragen wir für einen Inhalt in unserem Seelenleben mit uns herum?"
      ],
      [
        "Das erste sind unsere Vorstellungen.",
        "Daß diese Vorstellungen, zu­sammengedrängt mit Gefühlen, zu Willensimpulsen führen können, das hindert nicht, daß wir von einem besonderen Vorstellungsleben in unserer Seele sprechen können.",
        "Denn wenn es auch Menschen gibt, die sich kaum halten können, möchte man sagen, bei einer reinen, bloßen Vorstellung, die, wenn sie sich etwas vorstellen, mächtig in Sympathie oder Antipathie aufflammen, also gleich zu anderen Seelenimpulsen übergehen, so hindert das doch nicht, daß das Vorstellungsleben abge­trennt werden kann von anderen Seeleninhalten."
      ],
      [
        "Das zweite, was wir in unserem Seelenleben herumtragen, sind die Gefühlserlebnisse.",
        "Diese treten ja in einer recht vielgestaltigen Weise in uns auf.",
        "Da ist der allbekannte Gegensatz im Gefühlsleben, den man bezeichnen kann mit Sympathie und Antipathie, die wir den Dingen entgegenbringen, oder wenn man es deutlicher bezeichnen will: Liebe und Haß.",
        "Dann sind da die Gefühle, die man bezeichnen kann als die, welche eine gewisse Erregung bewirken, und wieder die, welche eine gewisse Spannung und Entspannung bewirken.",
        "Die lassen sich nicht zusammenwerfen mit den Gefühlen der Sympathie und der Antipathie.",
        "Denn ein Seelenimpuls, den man eine Spannung, eine Erregung und"
      ],
      [
        "eine Entspannung nennen kann, ist etwas anderes als das, was sich bloß in Sympathie oder Antipathie auslebt.",
        "Aber man müßte viel reden, wenn man die verschiedenen Gattungen der Gefühlsinhalte charakteri­sieren wollte.",
        "Es gehören auch dazu die, welche man bezeichnen kann als die Gefühle für das Schöne und für das Häßliche, die als ein ganz besonderer Seeleninhalt sich ausnehmen, die sich nicht vergleichen las­sen mit den bloßen Sympathie- und Antipathiegefühlen, wenigstens sich nicht mit ihnen zusammenwerfen lassen.",
        "Dann auch könnten wir die Gefühle, die wir haben für Gut und Böse, als eine besondere Gat­tung bezeichnen.",
        "Es ist heute nicht die Zeit, um auszuführen, wie das innere Erlebnis, das wir an einer guten oder einer bösen Handlung haben, etwas ganz anderes ist als das Gefühl der Sympathie oder Anti­pathie für eine gute oder böse Handlung, daß wir die gute Handlung lieben, die böse hassen.",
        "So treten uns die Gefühle in der mannigfal­tigsten Gestalt entgegen, und wir können sie unterscheiden von den Vorstellungen."
      ],
      [
        "Eine dritte Art von Seelenerlebnissen sind die Willensimpulse, das Willensleben.",
        "Das darf wieder nicht zusammengeworfen werden mit dem, was wir Gefühlserlebnisse nennen können, was innerhalb unseres Seelenlebens beschlossen bleiben muß oder kann durch die Art, wie wir es erleben.",
        "Zu einem Willensimpuls gehört, daß sich in der Seele aus­drückt: Du sollst dies tun, du sollst jenes nicht tun. - Denn man sollte unterscheiden lernen zwischen dem bloßen Gefühl, das man hat von dem, was einem an sich selber oder an einem anderen als gut oder böse erscheint, und zwischen dem, was mehr als dieses Gefühl in der Seele auftritt, wenn wir gedrängt werden, das Gute zu tun, das Böse zu las­sen.",
        "Die Beurteilung kann beim Gefühl stehenbleiben; aber etwas an­deres sind die Willensimpulse.",
        "Und obwohl Übergänge sind zwischen dem Gefühlsleben und den Willensimpulsen, sollte man schon aus Gründen der gewöhnlichen Lebensbeobachtung diese nicht ohne wei­teres zusammenwerfen.",
        "Im menschlichen Leben sind überall Übergänge.",
        "Wie es Menschen gibt, die zu gar keiner reinen Vorstellung kommen, sondern immer gleich zum Ausdruck bringen, was sie lieben oder has­sen, die immer hin- und hergeworfen werden, weil sie ihre Gefühle nicht absondern können von ihren Vorstellungen, so gibt es auch andere,"
      ],
      [
        "die, wenn sie etwas sehen, gar nicht davon ablassen können, zu etwas überzugehen, was einem Willensimpuls entspricht, zu einer Handlung, auch wenn diese Handlung gar nicht berechtigt ist.",
        "Das führt wieder zu nichts Gutem; das tritt dann als Stehlsucht, als Klepto­manie und so weiter auf.",
        "Da ist kein geordnetes Verhältnis zwischen den Gefühlen und den Willensimpulsen.",
        "Aber in Wahrheit sind diese Dinge in der strengsten Weise zu unterscheiden.",
        "So leben wir in un­serem Seelenleben innerhalb der Vorstellungen, innerhalb der Ge­fühlserlebnisse und innerhalb der Willensimpulse.",
        "Wir haben solche Betrachtungen schon öfter angestellt; man kann ohne sie, wenn man den gesamten Menschen ins Auge fassen will, nicht auskommen."
      ],
      [
        "Nun haben wir versucht, einiges anzuführen von dem, was uns nahelegen kann, daß das Vorstellungsleben etwas ist, was gebunden ist an die einmalige Inkarnation zwischen Geburt und Tod.",
        "Wir sehen ja auch, wie wir in das Leben hereintreten und uns das Vorstellungsleben aneignen."
      ],
      [
        "So ist es nicht mit dem Gefühlsleben, auch nicht mit dem Wil­lensleben.",
        "Wer behaupten wollte, es wäre so, von dem könnte man den­ken, er würde nie vernünftig die Entwickelung eines Kindes betrachtet haben."
      ],
      [
        "Man betrachte nur ein Kind, wenn es noch ganz dumm ist in be­zug auf das Vorstellungsleben, wie es sich gar nicht in Verbindung set­zen kann mit der Umwelt mit seinen Vorstellungen, wie es dagegen aus­gesprochene Sympathien und Antipathien hat, wie es dann wieder an-und abregende Willensimpulse hat.",
        "Und die Bestimmtheit, mit der die Willensimpulse auftreten, verführte sogar einen Philosophen, Schopen­hauer, zu dem Glauben, daß der Charakter eines Menschen überhaupt so auftritt, daß er gar nicht geändert werden kann im Leben."
      ],
      [
        "Es ist das nicht richtig; er kann geändert werden.",
        "Aber es ist so, wenn wir herein-treten in das physische Leben, daß wir sagen müssen: Es verhält sich mit den Gefühlen und Willensimpulsen keineswegs so wie mit den Vor­stellungen, sondern wir treten mit einem ganz bestimmten Charakter unserer Gefühlserlebnisse und Willensimpulse in die Inkarnation her­ein."
      ],
      [
        "Bei einer richtigen Betrachtung könnten wir schon ahnen, daß wir in den Gefühlen und in den Willensimpulsen etwas haben, was wir uns aus früheren Inkarnationen mitbringen.",
        "Aber fassen Sie das zusammen in ein gefühlsmäßiges Gedächtnis im Gegensatz zu dem Vorstellungsgedächtnis"
      ],
      [
        "in dem einen Leben.",
        "Man kann im Praktischen nicht aus­kommen, wenn man nur eine Vorstellungserinnerung gelten läßt.",
        "Alles, was wir im Vorstellungsleben entwickeln, kann uns nicht zu irgend etwas führen, was einen solchen Eindruck hervorrufen könnte, der, wenn wir ihn richtig verstehen, uns sagt: Da hast du etwas in dir, was durch die Geburt mit dir in diese Inkarnation hereingetreten ist.",
        "Da müssen wir über das Vorstellungsleben hinausgehen, da muß das Be­sinnen etwas anderes werden.",
        "Und da haben wir angeführt, was jetzt das Besinnen wird.",
        "Wie besinnen wir uns?",
        "Wir besinnen uns so, daß wir uns nicht bloß vorstellen: Das war zufällig in unserem Leben, das ha­ben wir getroffen, da waren wir in einer Lebensiage, die haben wir ver­lassen und so weiter. - Wir dürfen nicht bei den Vorstellungen blei­ben, sondern wir müssen sie lebendig, regsam machen, wie wenn das Bild einer Persönlichkeit vor uns stünde, die das gewollt hat, die in unseren Begehrun gen, Wil lensimpulsen, Gefühlserlehnissen und so wei­ter dies gewollt hat.",
        "In das Wollen müssen wir uns hineinleben.",
        "Also, es ist ein ganz anderes Sich-Hineinleben als jenes, was als Sich-Hinein-leben in das Vorstellungsleben beim Gedächtnis in Frage kommt; es ist ein Sich-Hineinleben in andere Seelenkräfte, wenn der Ausdruck ge­braucht werden darf."
      ],
      [
        "Diese Praxis, sozusagen wollend, wünschend, begehrend einen See­leninhalt zu entwickeln - die in allen okkulten Schulen, in aller okkul­ten Praxis immer bekannt war und angewendet worden ist -, läßt sich gut mit dem, was wir zu sagen wissen aus der anthroposophischen oder sonstigen Erkenntnis über Vorstellungs-, Gefühls- und Willensleben, rechtfertigen, läßt sich damit begreifen und erklären.",
        "Also sagen wir uns klar, daß wir an den besonderen Inhalten des Gefühlslebens, des Willenslebens etwas entwickeln müssen, das gewissermaßen den Erin­nerungsvorstellungen ähnlich ist, aber eben nicht bei den bloßen Vor­stellungen bleibt, daß wir aber dadurch in die Lage kommen, eine an­dere Art, nämlich eine solche Art von Erinnerungsvermögen zu ent­wickeln, die uns allmählich hinausführt über das Leben, das zwischen Geburt und Tod in der einen Inkarnation eingeschlossen ist."
      ],
      [
        "Es muß durchaus betont werden, daß der Weg, der hier gekennzeich­net worden ist, ein absolut guter und sicherer ist - aber ein entsagungsvoller."
      ],
      [
        "Leichter ist es, aus irgendwelchen äußeren Gründen sich einzu­bilden, daß man in der vorhergehenden Inkarnation Marie Antoinette, Maria Magdalena und dergleichen gewesen sei.",
        "Aber schwieriger ist es, auf die geschilderte Art und Weise, aus dem in der Seele Vorhandenen, aus wirklich Vorhandenem, zu einem Bilde dessen zu kommen, was man war.",
        "Es ist zunächst deshalb recht entsagungsvoll, weil man mei­stens recht enttäuscht werden kann.",
        "Wenn aber jemand nun sagen wür­de, das kann alles etwas sein, was wir uns vormachen, so muß man erwidern: Aber es kann sich auch jemand in bezug auf seine Erinne­rungen etwas vormachen, was nicht stimmt. - Diese Dinge sind alle kein Einwand.",
        "Eine Art von Kriterium, um die Einbildung von der Phantastik zu unterscheiden, gibt es bloß im Leben."
      ],
      [
        "In einer süddeutschen Stadt sagte einmal jemand zu mir, es könnte alles, was in meiner «Geheimwissenschaft im Umriß» vorgebracht ist, auf einer bloßen Suggestion beruhen, wie es ja sehr lebendige Suggestio­nen gibt, die sogar soweit gehen können, daß jemand, wenn er gar keine Limonade trinkt und sich nur die Limonade recht lebhaft vorstellt, schon den Geschmack der Limonade im Munde hat.",
        "Wenn also so etwas möglich ist, warum sollte es dann nicht auch möglich sein, so dachte der Betreffende, daß das in der «Geheimwissenschaft» Vorgebrachte auch auf Suggestionen beruhen sollte?"
      ],
      [
        "Theoretisch läßt sich ein solcher Einwand machen.",
        "Aber das Leben bringt die Überlegung: Wenn je­mand meint, mit dem Beispiel der Limonade zeigen zu können, wie stark die Suggestion wirken kann, so muß man dazu sagen, der hat nicht verstanden, das Beispiel zu Ende zu denken, denn er sollte einmal probieren, nicht bloß die Limonade sich vorzustellen, sondern sich mit einer bloß vorgestellten Limonade den Durst zu löschen - da wird er sehen, daß es nicht geht."
      ],
      [
        "Es handelt sich immer darum, daß wir an das Ende gehen mit den Erlebnissen.",
        "Das läßt sich aber nicht theoretisch bestimmen, sondern nur im unmittelbaren Leben selber erfahren.",
        "Und mit derselben Notwendigkeit, mit der wir wissen, daß wir etwas, was herauftaucht aus den Erinnerungsvorstellungen des Lebens, erlebt ha­ben, mit derselben Sicherheit tritt auch das auf, daß herauftauchen aus den Untergründen der Seele die Willensimpulse, die wir hervorrufen über das Zufällige, über das Nichtgewollte, und die mit derselben Notwendigkeit"
      ],
      [
        "auftauchen als ein Bild unseres früheren Erdenlebens wie die Erinnerungsvorstellungen.",
        "Dem, der nun sagt, das kann Einbildung sein, dem können wir dafür keine Beweise bringen, wie man theore­tisch auch keinen Beweis bringen kann für das, was sich zahlreiche Menschen einbilden, erlebt zu haben und ganz bestimmt nicht erlebt haben, und für das, was sie wirklich erlebt haben.",
        "Ebensowenig wie man da einen theoretischen Beweis vorbringen kann, ebensowenig gibt es einen theoretischen Beweis für das andere.",
        "Also, man ist dabei in kei­ner anderen Lage, als man ist in dem Leben innerhalb der einen Inkar­nation; man ist genau in derselben Lage."
      ],
      [
        "So haben wir mit diesem gezeigt, wie früheres Erdenleben herein-leuchtet in das gegenwärtige Erdenleben, wie wir wirklich eine Mög­lichkeit haben, durch sorgfältige Seelenentwickelung uns selber die Überzeugung zu verschaffen, nicht nur die theoretische Überzeugung von der Tatsache der Reinkarnation, sondern die praktische Überzeu­gung von dem in uns befindlichen, sich reinkarnierenden Seelenwesen, von dem wir wirklich wissen, es ist etwas, was einmal da war."
      ],
      [
        "Aber es gibt dennoch Erlebnisse ganz anderer Art, die hereintreten in unser Leben und von denen wir nicht sagen können, sie treten so in unser Leben herein, daß wir sie wie eine Erinnerung an ein früheres Erdenleben auffassen können.",
        "Es gibt tatsächlich solche Erlebnisse, de­nen gegenüber wir sagen müssen: Wie sie dir da gegenübertreten, so erklären sie sich dir aus deinem früheren Leben nicht!",
        "Heute sei nur auf eine Art solcher Erlebnisse hingewiesen.",
        "Und auf diese Art von Erleb­nissen will ich zunächst hinweisen, indem ich ein typisches Beispiel an­führe.",
        "Dies, was ich als Beispiel anführe, das kann sich auf hunderter­lei Weise, auf tausenderlei Weise vollziehen; aber es ist eben das, was sich da vollzieht, ähnlich dem, was ich als ein typisches Beispiel er­zählen will."
      ],
      [
        "Wir nehmen einen Menschen an, der irgendwo in einem Walde geht, und der, weil er in Gedanken gegangen ist, vergißt, daß er auf einem Waldeswege geht, der unmittelbar - man braucht nur einige Schritte zu machen - an einen tiefen Abgrund angrenzt.",
        "Ich will die Sache, die sich durchaus abspielen kann, in dieser Form hier vorbringen; das Bei­spiel ist von mir, weil in entsprechender Weise mir ein ganz ähnlich"
      ],
      [
        "gearteter Fall bekannt ist, auch anderswo erzählt worden.",
        "Dieser Mensch sieht nun nicht, daß dort ein Abgrund ist, weil ihn etwas be­sonders interessiert.",
        "Weil ihn eben sein Problem so stark interessiert, geht er auf den Abgrund los, aber mit einem solchen Schwunge, daß es ihm, wenn er nur zwei, drei Schritte mehr gemacht hätte, unmöglich gewesen wäre, sich zu halten.",
        "Er hätte dann im Vorwärtsschreiten hin­unterstürzen müssen, und es wäre mit seinem Leben zu Ende gewesen.",
        "In dem Augenblick aber, wo er drauflostapsen will, hört er eine Stim­me: Bleibe stehen! - Die Stimme macht einen solchen Eindruck auf ihn, daß er wie angenagelt stehen bleibt.",
        "Der Betreffende denkt, es muß jemand da sein, der sich seiner angenommen hat.",
        "Er hat sich besonnen, daß sein Leben zu Ende gewesen wäre, wenn er nicht auf diese Weise festgehalten worden wäre.",
        "Er sieht sich um, und sieht niemanden."
      ],
      [
        "Der materialistische Denker wird nun sagen: Durch irgendwelche Umstände hat sich aus den Tiefen der Seele eine Gehörshalluzination ergeben, und es ist ein glücklicher Zufall gewesen, daß der Betreffende auf diese Weise gerettet worden ist. - Aber es ist auch möglich, auf andere Weise über die Sache zu denken; mindestens müßte man dies zu­geben.",
        "Ich will es heute nur anführen; denn diese andere Weise läßt sich nur erzählen, nicht beweisen.",
        "Man kann sich sagen: Durch Vor­gänge der geistigen Welt ist dir in dem Augenblick, als du an einer karmischen Krisis angekommen warst, dein Leben eigentlich geschenkt worden.",
        "Wenn alles so weitergegangen wäre, ohne daß jenes Ereignis geschehen wäre, dann wäre dein Leben zu Ende gewesen.",
        "So aber ist es jetzt als eine Art neues Leben an das vorhergehende angestückelt wor­den.",
        "Dieses neue Leben ist eine Art Geschenk, und du verdankst jetzt dieses dein Leben den Mächten, die hinter dieser Stimme stehen! - Ein solches Erlebnis könnten viele, viele Menschen der Gegenwart haben, wenn sie nur wirkliche Selbsterkenntnis üben würden.",
        "Denn es treten in das Leben geradezu vieler, vieler Menschen der Gegenwart solche Erlebnisse herein.",
        "Und es liegt nicht daran, daß die Menschen nicht ein solches Erlebnis gehabt haben, sondern daran, daß die Menschen nicht die nötige Aufmerksamkeit dafür gehabt haben, daß sie darüber hin­weggegangen sind; denn es tritt nicht immer mit dieser jetzt geschilderten"
      ],
      [
        "Deutlichkeit auf, sondern so, daß bei der gewöhnlichen Unauf­merksamkeit die Menschen darüber hinwegsehen."
      ],
      [
        "Ich habe zuweilen geschildert, wie stark die Menschen hinwegsehen über etwas, was in der unmittelbaren Gegenwart der Menschen auftritt.",
        "Ein charakteristisches Beispiel dafür, wie die Menschen für das, was rings um sie her vorgeht, unaufmerksam sind, ist folgender Fall.",
        "Ich kannte einen Schulinspektor eines Landes, wo das Gesetz eingeführt wurde, daß ältere Lehrer, die gewisse Examina nicht abgelegt hatten, überprüft werden müßten.",
        "Nun war dieser Schulinspektor ein außer­ordentlich humaner Mensch und sagte sich: Die jüngeren Dachse, die eben vom Seminar gekommen sind, kann man ja über alles fragen; aber die älteren Herren zu fragen, die bereits zwanzig, dreißig Jahre im Amte sind, das ist eine Grausamkeit, die kann man nicht so fragen.",
        "Ich frage diese daher am besten über das, was in ihren Büchern steht, aus denen sie Jahr für Jahr die Kinder unterrichten. - Und siehe da:"
      ],
      [
        "die meisten wußten nichts von dem, was sie selbst ihren Schülern vortrugen!",
        "Und zwar war das ein Examinator, von dem man sagen konnte: er wußte schon aus den Menschen das herauszuziehen, was sie wußten!"
      ],
      [
        "Es sollte das nur ein Beispiel dafür sein, wie die Menschen unauf­merksam sind für das, was in ihrer Umgebung vorgeht, ja sogar für das, wo es sich um ihre eigene Person handelt.",
        "Man braucht also nicht er­staunt zu sein, wenn ein ähnliches Beispiel, wie das jetzt charakteri­sierte, im Leben vieler, vieler Menschen zu finden ist.",
        "Nur bei einer sinnigen, wirklichen Selbstbetrachtung findet man ein solches Ereignis, wie es eben beschrieben worden ist.",
        "Und wenn man einem solchen Er­eignis gegenüber die rechte Lebensfrömmigkeit hat, dann kommt man vielleicht auch zu einem ganz besonderen Gefühl; zu dem Gefühl, daß einem das Leben seit jenem Tage geschenkt ist, und daß man, soweit es seit jenem Tage verläuft, es auch in einer besonderen Weise anzuwen­den hat.",
        "Das ist ein gutes Gefühl und wirkt ähnlich wie ein Erinne­rungsvorgang, wenn jemand sich sagt: Du warst an einer karmischen Krisis, da war dein Leben abgeschlossen! - Wenn er sich hineinver­tieft in dieses fromme Gefühl, dann kommt etwas, was zunächst so auftritt, daß er sich sagt: Das ist nicht eine Erinnerungsvorstellung"
      ],
      [
        "wie die, welche ich im Leben öfter erfahren habe, das ist etwas ganz Besonderes!"
      ],
      [
        "Nun werde ich Ihnen im nächsten Vortrag Genaueres sagen können über das, was heute nur angedeutet werden kann.",
        "Denn so, wie es jetzt angedeutet worden ist, so prüft ein großer Eingeweihter der neueren Zeit die, welche er für geeignet hält zu seinen Bekennern."
      ],
      [
        "Denn die Dinge, die uns hineinstellen sollen in die geistige Welt, gehen auch aus den geistigen Tatsachen, die um uns herum geschehen, oder aus einer richtigen Erkenntnis dieser Tatsachen hervor.",
        "Und eine solche Stimme, wie sie bei vielen Menschen auftritt, ist nicht als eine Halluzination zu betrachten; denn durch eine solche Stimme spricht derjenige Führer, den wir als Christian Rosenkreutz bezeichnen, zu denen, die er sich aus der übrigen Schar auswählt als die, welche seine Bekenner werden kön­nen."
      ],
      [
        "So ergeht der Ruf von der Individualität, von der wir noch wer­den sprechen können als derjenigen, welche in einer besonderen Inkar­nation im 13.",
        "Jahrhundert gelebt hat, so daß ein Mensch, der so etwas erlebt, daran ein Merkzeichen, ein Erkennungszeichen hat, durch das er sich hineinstellen kann in die geistige Welt."
      ],
      [
        "Vielleicht werden nicht viele dazu kommen können, einen solchen Ruf zu beachten.",
        "Aber die Anthroposophie wird schon dahin wirken, daß die Menschen, wenn nicht jetzt in dieser Inkarnation, so doch später einen solchen Ruf be­achten werden."
      ],
      [
        "Für die meisten Menschen, die so etwas erleben, ist es nun heute so, daß dasjenige, was man bezeichnen kann als: Es ist ihnen gegenübergetreten jener Eingeweihte, der sie bestimmt hat zu denen, die zu ihm gehören können -, sich nicht in einer Inkarnation voll­zogen hat, sondern in dem Leben zwischen dem Tode und der jetzigen Geburt, so daß dies also ein Hinweis darauf ist, daß etwas geschieht in dem Leben zwischen dem Tode und der nächsten Geburt, und daß wir darin Wichtiges, ja wichtigere Vorgänge haben als im Leben zwischen Geburt und Tod.",
        "Es kann ja sein und ist in einzelnen Fällen so, daß gewisse zu Christian Rosenkreutz gehörige Menschen auch schon in einer vorhergehenden Inkarnation dazu bestimmt worden sind."
      ],
      [
        "Aber für die meisten ist die Bestimmung, die sich in einem solchen Ereignis abbildet, getroffen worden in dem letzten Leben zwischen Tod und neuer Geburt."
      ],
      [
        "Nun sage ich das nicht, um etwas Sensationelles zu erzählen, nicht einmal um dieses Ereignis zu erzählen, sondern aus einem besonderen Grunde.",
        "Und ich möchte dazu noch auf etwas aufmerksam machen, aus einer Erfahrung heraus, die ich innerhalb unseres anthroposophischen Lebens recht häufig gemacht habe: daß Dinge, die man einmal sagt, leicht vergessen oder anders erhalten werden, als man sie sagt.",
        "Es soll das vorkommen innerhalb unseres anthroposophischen Lebens.",
        "Aus diesem Grunde betone ich manchmal wichtige, wesentliche Dinge ein paarmal, nicht um mich zu wiederholen.",
        "Auch heute geschieht das, wenn ich sage, es sind viele Menschen in der Gegenwart, die ein solches Erlebnis, wie es beschrieben worden ist, durchgemacht haben, und daß sie es nicht wissen, liegt nicht daran, daß es nicht da ist, sondern daß man sich nicht daran erinnert, weil man nicht die rechte Aufmerksam­keit darauf verwendet hat.",
        "Deshalb soll es ein Trost sein, wenn jemand sich sagen muß: Ich finde nicht so etwas, also gehöre ich nicht zu sol­chen Auserwählten! - Doch kann Ihnen die Versicherung gegeben werden, daß unzählige Menschen in der Gegenwart sind, die so etwas erlebt haben.",
        "Das wollte ich nur vorausschicken, um zum eigentlichen Grunde zu kommen, warum so etwas gesagt wird."
      ],
      [
        "Solche Dinge werden erzählt, um uns immer wieder und wieder dar­auf aufmerksam zu machen, daß wir in konkreter Weise - nicht durch abstrakte Theorien - eine Beziehung unseres Seelenlebens zu den gei­stigen Welten finden sollen, und daß die anthroposophische Geistes­wissenschaft uns nicht sein soll eine bloße theoretische Weltanschauung, sondern eine innere Kraft unseres Lebens; daß wir nicht bloß wissen sollen, es gibt eine geistige Welt und der Mensch gehört ihr an; daß wir, indem wir durch das Leben gehen, nicht bloß die Dinge betrachten, die auf unser sinnliches Denken wirken, sondern die Zusammenhänge aufmerksam erfassen, die uns zeigen: Du bist hineingestellt in die geistige Welt, auf diese und jene Weise hineingestellt. - Also das kon­krete Hineingestelitsein, das für den einzelnen reale Hineingestelitsein, das ist es, worauf wir aufmerksam machen.",
        "Theoretisch sucht man auch draußen so etwas zu begründen, daß die Welt ein Geistiges haben kann, und daß der Mensch nicht materialistisch zu betrachten ist, son­dern ein Geistiges in sich haben kann.",
        "Davon unterscheidet sich unsere"
      ],
      [
        "Weltanschauung, indem sie im einzelnen hinstellt: So stehst du im Zusammenhange mit den geistigen Welten! - Immer mehr und mehr werden wir zu solchen Dingen aufsteigen können, die uns zu zeigen vermögen, wie wir die Welt zu betrachten haben, um unsere Zuge­hörigkeit zu dem Geiste der großen Welt, dem Makrokosinischen, ein­zusehen."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG Stuttgart, 20. Februar 1912",
    "paragraphs": [
      "Wenn wir das Leben in Betracht ziehen, wie es sich um uns herum ab­spielt, wie es sozusagen seine Wogen hereinwirft in unser Inneres, in all das, was wir selber während unseres physischen Erdendaseins zu emp­finden und zu leiden haben, oder worüber wir uns zu freuen haben, so können wir mehrere besondere Gruppen oder Arten von Erleben ins Auge fassen.",
      "Wir finden zunächst, wenn wir mehr auf uns selbst schauen, auf das­jenige, was in unseren Fähigkeiten, in unseren Talenten liegt, wir fin­den, wenn uns dieses oder jenes gelingt, daß wir uns sagen können:",
      "Nun, nachdem wir schon einmal dieser oder jener Mensch sind, ist es ganz natürlich und begreiflich, daß uns dieses oder jenes gelingen mußte. - Wir können aber auch gewisse Mißerfolge, die uns betroffen haben, vielleicht gerade das, was wir als Mißgeschick und Unglück be­zeichnen müssen, weil es uns nicht gelungen ist, im ganzen Zusammen-hang unseres Wesens begreiflich finden.",
      "Vielleicht gelingt es uns nicht immer in solchen Fällen, genau nach­zuweisen, wie dieser oder jener Mißerfolg, dieses oder jenes, was uns nicht gelungen ist, zusammenhängt mit unserer Unfähigkeit nach dieser oder jener Richtung. Aber wenn wir uns dann im allgemeinen sagen müssen: Du warst ja in vielen Beziehungen im jetzigen Erdendasein ein leichtsinniges Subjekt, da kannst du begreifen, daß du unter Umständen verdientermaßen diesen oder jenen Mißerfolg haben mußt -, dann können wir vielleicht nicht ganz unmittelbar den Zusammenhang ein­sehen zwischen Mißerfolg und Unfähigkeit, aber im allgemeinen doch begreiflich finden, daß, wenn wir leichtsinnig waren, nicht alles am Schnürchen gelingen konnte.",
      "Von dem, was jetzt besprochen worden ist, können Sie sich denken, daß wir gewissermaßen eine Art ursächlichen Zusammenhanges ein­sehen könnten zwischen dem, was geschehen mußte aus unseren Fähig­keiten und unseren Unfähigkeiten heraus. Es gibt aber viele Dinge im Leben, bei denen wir, auch wenn wir noch so genau zu Werke gehen,",
      "nicht erreichen, das, was uns gelingt oder mißlingt, ohne weiteres in Zusammenhang zu bringen mit unseren Fähigkeiten oder Unfähigkei­ten, bei denen uns gewissermaßen undurchsichtig bleibt, wie wir dieses oder jenes verschuldet haben, oder wie wir es verdient haben. Kurz, wenn wir mehr unser Innenleben ins Auge fassen, werden wir unter­scheiden können zwischen zwei Gruppen von Erlebnissen. Die eine Gruppe ist die, bei der wir uns bewußt sind, wie es mit den Ursachen unseres Gelingens und Mißlingens bestellt ist; bei der anderen Gruppe werden wir einen solchen Zusammenhang nicht überschauen können. Bei dieser letzteren Gruppe wird es uns mehr oder weniger als Zufall erscheinen, daß gerade dieses uns mißlungen, ein anderes uns gelungen ist. Wir wollen uns zunächst merken, daß es im Leben diese letztere Gruppe von Tatsachen und Erfahrungen hinlänglich gibt, und wollen spater einmal das Augenmerk auf diese Gruppe lenken.",
      "Wir können dann, entgegen dem, was jetzt besprochen worden ist, unser äußeres Schicksal mehr ins Auge fassen. Da werden wir eigentlich wiederum zwei Gruppen von Tatsachen in bezug auf unser äußeres Geschick ins Auge fassen müssen. Wir können solche Fälle ins Auge fassen, bei denen wir innerlich einsehen, daß wir in bezug auf diese Er­eignisse, die uns treffen - also nicht, was wir selber unternommen haben -, gewisse Dinge sozusagen selber herbeigeführt haben, schuld sind an solchen Dingen. Aber von einer anderen Gruppe werden wir sehr geneigt sein zu sagen: Wir können den Zusammenhang nicht ein­sehen mit dem, was wir gewollt, was wir beabsichtigt haben. Es sind diejenigen Ereignisse, bei denen man im gewöhnlichen Leben davon spricht, daß sie wie ein Zufall, der anscheinend mit nichts, was wir selber herbeigeführt haben, zusammenhängt, in unser Leben herein­gebrochen sind.",
      "Diese zweite Gruppe ist es, die wir jetzt ins Auge fassen wollen mit Bezug auf das innere Leben, also diejenigen Ereignisse, von denen wir nicht einsehen können, daß sie als etwas Direktes, Unmittelbares mit unseren Fähigkeiten und Unfähigkeiten zu tun haben; äußere Ereig­nisse also, das, was wir Zufallsereignisse nennen, von denen wir von vorneherein nicht die Einsicht gewinnen können, daß sie durch irgend etwas Vorhergehendes herbeigeführt worden sind.",
      "Nun kann man einmal probeweise sozusagen mit diesen beiden Grup­pen von Erlebnissen eine Art Experiment machen. Das Experiment verpflichtet einen ja zunächst zu nichts. Man probiere sozusagen nur einmal dasjenige, was jetzt gesagt, was jetzt charakterisiert werden soll.",
      "Wir können das Experiment machen, indem wir uns vorstellen: Wie wäre es denn, wenn wir einmal eine Art von künstlichem Menschen konstruieren würden, so einen künstlichen Menschen uns ausdenken würden, daß wir von diesem künstlichen Gedankenmenschen, den wir uns ausgedacht haben, sagen würden, gerade diejenigen Dinge, von de­nen wir keinen Zusammenhang wissen mit unseren Fähigkeiten, die seien so, daß wir den künstlichen Menschen, den wir uns ausdenken, begaben mit den Eigenschaften und Fähigkeiten, welche diese bei uns unbegreiflichen Dinge herbeigeführt haben. Also ein Mensch, der sol­che Fähigkeiten hat, daß ihm das gelingen oder mißlingen muß, wovon wir uns nicht zuschreiben können, daß es uns nach unseren Fähigkeiten oder Unfähigkeiten gelinge oder mißlinge. Wir stellen ihn uns also vor als einen solchen Menschen, welcher künstlich, ganz absichtlich herbei­geführt hätte die Dinge, welche zufällig in unserem Leben eingetreten zu sein scheinen.",
      "Man kann von einfachen Beispielen ausgehen, um das zu erläutern. Nehmen wir an, ein Ziegelstein wäre auf unsere Schulter gefallen und hätte uns an der Schulter verletzt. Da werden wir zunächst geneigt sein zu sagen: Das ist ein Zufall. - Aber konstruieren wir einen künst­lichen Menschen probeweise zunächst wie ein Experiment, der folgende sonderbare Sache machen würde. Wir konstruieren einen Menschen, der auf das Dach steigt und dort rasch einen Ziegelstein loslöst, aber nur so weit, daß der Stein noch einen gewissen Halt behält; dann läuft der künstliche Mensch schnell wieder hinunter, so daß, wenn der Stein sich loslöst, er gerade auf seine Schultern fällt. So machen wir es in be­zug auf alle Ereignisse, von denen uns einfällt, daß sie zufällig in un­serem Leben eingetreten sind. Einen künstlichen Menschen konstruieren wir, der alles verschuldet oder herbeiführt, wovon wir im gewöhnlichen Leben nicht einsehen können, wie es mit uns zusammenhängt.",
      "Wenn man das tut, so könnte es zunächst ausschauen wie ein bloßes Gedankenspiel. Und es verpflichtet zu nichts, wenn man das tut. Aber",
      "eine Merkwürdigkeit stellt sich heraus, wenn man das tut. Wenn man einen solchen Menschen ausgedacht hat und ihn begabt hat mit den ge­schilderten Eigenschaften, dann macht dieser künstliche Gedanken­mensch einen ganz merkwürdigen Eindruck auf uns.",
      "Wir kommen näm­lich von dem Bilde eines Menschen, das wir uns da gemacht haben, ob­wohl es scheinbar so künstlich konstruiert ist, nicht mehr los; es faszi­niert uns, es macht den Eindruck, als ob es doch irgend etwas mit uns zu tun haben müßte. Dafür sorgt schon die Empfindung, die man ge­genüber dem künstlichen Gedankenmenschen hat.",
      "Wenn man sich recht sehr hineinvertieft in dieses Bild, so läßt es einen ganz sicher nicht mehr los. Ein merkwürdiger Prozeß bildet sich in unserem Gemüt; ein Pro­zeß, den man vergleichen kann mit folgendem: Wir kommen zu einem inneren Gemütsprozeß, den der Mensch alle Augenblicke durchmacht.",
      "Wir können irgend etwas denken, können einen Entschluß fassen; wir brauchen dazu etwas, was wir einmal gewußt haben, und wir wenden alle möglichen künstlichen Mittel an, um uns auf das zu besinnen, was wir gewußt haben. Bei diesem Anstrengen, in das Gedächtnis etwas heraufzurufen, was uns entfallen ist, machen wir natürlich einen Ge­mütsprozeß durch, das Uns-Besinnen, wie wir es im gewöhnlichen Leben nennen.",
      "Und alle die Gedanken, die wir zu Hilfe nehmen, um uns auf etwas zu besinnen, sind Hilfsgedanken. Versuchen Sie nur ein­mal, darauf zu kommen, wieviel solcher Hilfsgedanken Sie oftmals aufwenden müssen, die Sie dann wieder fallen lassen, um auf das zu kommen, was Sie wissen wollen.",
      "Solche Hilfsgedanken sind dazu da, daß sie den Weg eröffnen auf das zu Besinnende, was wir eigentlich gegenwärtig brauchen.",
      "Gerade so, nur wie etwas weit Umfassenderes, ist jener Gedanken-mensch, den wir geschildert haben, ein Hilfsprozeß. Er läßt uns nicht mehr los; er arbeitet in uns so, daß wir sagen, er ist etwas, was als Ge­danke in uns wohnt, etwas, was da fortwirkt, was sich umwandelt in uns; was tatsächlich sich umwandelt zu der Idee, zu dem Gedanken, der nun auftritt wie etwas, was uns einfällt, wenn wir uns im gewöhn­lichen Erinnerungsprozeß besinnen, der auftritt wie etwas, was uns überwältigt. Wie wenn etwas sagen würde: So kann er nicht bleiben, er ändert sich um in dir, er entfaltet Leben, er wird zu etwas anderem!",
      "Das drängt sich uns auf - machen Sie das Experiment! -, es drängt sich uns so auf, daß er uns sagt: Ja, das ist etwas, was mit einem anderen als deinem jetzigen Erdendasein einiges zu tun hat. Eine Art Be­sinnung auf ein anderes Erdendasein, der Gedanke tritt ganz bestimmt auf. Es ist mehr ein Gefühl als ein Gedanke, eine Empfindung, aber eine solche, wie wenn wir das, was im Gemüt auftritt, so fühlen wie das, was wir selber einmal in einer früheren Inkarnation auf dieser Erde waren.",
      "Anthroposophie ist eben durchaus, wenn wir sie als etwas Ganzes betrachten, nicht bloß eine Summe von Theorien, von Mitteilungen von Tatsachen, die da bestehen, sondern sie gibt uns Vorschriften und An­weisungen, wie man dies oder jenes erreichen kann. Die Anthropo­sophie sagt: Du wirst mehr und mehr dahin geführt, daß du dich leich­ter besinnen kannst, wenn du dies oder jenes machst. - Man kann auch sagen, und das ist durchaus aus dem Gebiet der Erfahrung geschöpft:",
      "Wenn du so vorgehst, bekommst du einen Gemütseindruck, einen Ge­fühlseindruck von dem Menschen, der du früher warst. - Wir kommen da zu dem, was man nennen könnte: eine Erweiterung unseres Gedächt­nisses. Nun ist dies, was sich uns da eröffnet, wirklich zunächst nur eine Gedankentatsache, solange wir den geschilderten Gedankenmen­schen konstruieren. Aber der Gedankenmensch bleibt nicht Gedanken-mensch. Er verwandelt sich in Empfindungs-, in Gemütseindrücke, und indem er dies tut, wissen wir: In dem, was wir empfinden, haben wir etwas, was zu tun hat mit unserer vorhergehenden Inkarnation. Unser Gedächtnis erweitert sich auf unsere frühere Inkarnation.",
      "In dieser Inkarnation erinnern wir uns an die Dinge, bei denen wir mit unseren Gedanken zugegen sind. Sie alle wissen, daß man sich ver­hältnismäßig leicht erinnert an die Dinge, in welche unsere Gedanken hereingespielt haben. Im gewöhnlichen Leben bleibt aber nicht so leicht lebendig dasjenige, was in unser Gefühl hereingespielt hat. Wenn Sie versuchen, zurückzudenken an das, was Ihnen großen Schmerz gemacht hat vor zehn, zwanzig Jahren, so werden Sie sich leicht an die Vorstel­lung erinnern; Sie werden sich an das, was sich da abgespielt hat, in Ihren Vorstellungen zurückversetzen; aber zu einer lebendigen Emp­findung des damals empfundenen Schmerzes können Sie nicht ge­langen. Der Schmerz verblaßt, die Erinnerung an ihn ergießt sich in",
      "unsere Vorstellung. Was jetzt geschildert worden ist, ist ein Gemüts­gedächtnis, ein Gefühlsgedächtnis. Und in der Tat, als solches fühlen wir unsere frühere Inkarnation. In der Tat tritt das auf, was wir nen­nen können: eine Erinnerung an frühere Inkarnationen. Es kann ja nicht so ohne weiteres angesehen werden wie das, was in die gegen­wärtige Inkarnation hereinspielt, was Träger der Erinnerung ist an frühere Inkarnationen. Bedenken Sie nur einmal, wie innig verwachsen unsere Vorstellungen mit dem Ausdruck der Vorstellungen sind, mit unserer Sprache. Die Sprache ist die verkörperte Vorstellungswelt. Und die Sprache muß ein jeder Mensch in den einzelnen Leben wieder ler­nen. Der größte Sprachforscher oder Sprachkenner muß als Kind mit Mühe seine Muttersprache erlernen. Es ist noch nicht der Fall vorge­kommen, daß ein Gymnasiast das Griechische deshalb leicht lernte, weil er sich rasch erinnert hätte an das Griechisch, das er in früheren Inkarnationen gesprochen hat!",
      "Der Dichter Hebbel hat mit einigen Gedanken den Plan eines Dra­mas aufgezeichnet, das er schreiben wollte. Schade, daß er es nicht ge­tan hat, es wäre ein sehr interessantes Drama geworden. Die Handlung war so gedacht, daß der wiederverkörperte Plato als Gymnasiast bei der Erklärung des alten Plato die allerschlechteste Zensur bekäme! Lei­der ist der Plan Hebbels nicht zur Ausführung gekommen. Wir brau­chen nicht bloß daran zu denken, daß die Lehrer zum Teil pedantisch sind und so weiter. Wir wissen, daß das, was Hebbel aufzeichnete, darauf beruht, daß das Vorstellungsmäßige, was sich in den unmittel­baren Erfahrungsvorstellungen abspielt, mehr oder weniger unmittel­bar beschränkt ist auf die gegenwärtige Inkarnation. Und es ist so, wie jetzt angedeutet worden ist, daß die erste Impression, der erste Ein­druck von der vorhergehenden Inkarnation unmittelbar auftritt als Gefühlsgedächtnis, als eine neue Art von Gedächtnis. Was wir als Ein­druck haben, wenn dieses Gedächtnis von dem Gedankenmenschen her entsteht, den wir konstruiert haben, ist mehr ein Gefühl, aber ein sol­ches Gefühl, daß man versteht: Der Eindruck rührt von einem Kerl her, der einmal existiert hat und der du selber warst! - Man bekommt etwas wie ein Erinnerungsgefühl als ersten Eindruck an die vorher­gehende Inkarnation.",
      "Was da geschildert worden ist als Konstruktion eines Gedanken­menschen, das ist nur ein Mittel. Dieses Mittel wandelt sich um in einen solchen Gemüts- oder Gefühlseindruck. Jeder Mensch, der an die An­throposophie herantritt, hat eigentlich mehr oder weniger Gelegenheit, leicht dasjenige auszuführen, was jetzt geschildert worden ist. Und wenn er dieses ausführt, wird er schon sehen, daß er wirklich in seinem Inneren einen Eindruck erhält, sagen wir - um ein anderes Beispiel zu gebrauchen - einen Eindruck, den er so schildern könnte: Ich habe einmal eine Landschaft gesehen, ich habe vergessen, wie sie aussieht, sie hat mir aber gefallen! - Nun wird, wenn es in diesem Leben war, die Landschaft keinen sehr lebendigen Gefühlseindruck mehr machen; aber wenn der Eindruck aus einer vorhergehenden Inkarnation stammte, so wird er einen besonders lebendigen Gefühlseindruck machen. Wir kön­nen uns so einen besonders lebendigen Eindruck als Gefühlseindruck von unserer früheren Inkarnation machen. Und wenn wir dann objek­tiv die geschilderten Eindrücke beobachten, werden wir zuweilen etwas wie ein bitteres oder ein bittersüßes oder ein saures Gefühl haben aus dem, was sich ergibt als Umwandlung des Gedankenmenschen. Dieses sauersüße oder sonstige Gefühl ist der Eindruck, den unsere frühere Inkarnation auf uns macht; es ist eine Art von Gefühls- oder Gemüts-eindruck.",
      "Damit wurde versucht, Sie aufmerksam zu machen auf etwas, was dazu führen kann, bei jedem Menschen eine Art unmittelbarer Gewiß­heit hervorzurufen, daß er in früheren Leben existiert hat; Gewißheit dadurch, daß er sich ein Gefühl verschafft, daß er Gemüts- oder Ge­fühlseindrücke hat, von denen er weiß: Das hast du gewiß nicht in diesem Leben irgendwo erworben. - Ein solcher Eindruck tritt aber so auf, wie für das gewöhnliche Leben eine Erinnerungsvorstellung auf­tritt. Nun kann man fragen: Wie kann man wissen, daß der Eindruck, den man hat, eine Erinnerung ist? - Sehen Sie, da kann man nur sagen, beweisen läßt sich so etwas nicht. Aber es liegt derselbe Tatbestand vor, der auch sonst im Leben vorliegt, wenn wir uns an etwas erinnern und bei gesunden Sinnen sind. Da können wir wissen, daß das, was in uns auftritt in Gedanken, sich wirklich bezieht auf etwas, was wir erlebt haben. Die Erfahrung selber gibt die Gewißheit. Was wir uns in der",
      "angegebenen Art vorstellen, gibt uns die Gewißheit davon, daß der Eindruck, der im Gemüt auftaucht, sich nicht auf etwas bezieht, was mit uns zu tun hatte im gegenwärtigen Leben, sondern auf etwas, was mit uns zu tun hatte im vorhergehenden Leben.",
      "Da haben wir auf künstliche Weise in uns hervorgerufen etwas, was uns mit unserem vorhergehenden Leben in Zusammenhang bringt. Wir können noch mancherlei andere Arten von innerlichen probeweisen Er­fahrungen und Erlebnissen hernehmen und können dadurch wieder weitergehen und in uns wachrufen so etwas wie Empfindungen von früheren Leben. Da können wir wiederum in anderer Hinsicht die Er­lebnisse dessen, was wir im Leben durchmachen, teilen; wir können sie in anderer Weise in Gruppen teilen. Wir können auf der einen Seite in eine Gruppe fassen, was wir an Leiden, an Schmerzen, an Hemmnissen im Leben durchgemacht haben; auf der anderen Seite, was uns bewußt geworden ist als Förderungen, als Freude, Lust und so weiter.",
      "Nun können wir wiederum probeweise uns auf folgenden Stand­punkt stellen. Wir können einmal sagen: Ja, wir haben diese Schmer­zen, diese Leiden erfahren. So wie wir in dieser Inkarnation einmal sind, wie das normale Leben nun einmal abläuft, sind uns unsere Schmerzen, unsere Leiden etwas Fatales, etwas, was wir in gewisser Beziehung gern von uns hinwegstoßen würden. Tun wir dies einmal probeweise nicht. Nehmen wir probeweise an, wir würden aus einem gewissen Grunde diese Schmerzen, diese Leiden und Hemmnisse selber herbeigeführt haben, denn durch diese früheren Leben, wenn sie wirk­lich da sind, sind wir in gewisser Weise durch das, was wir getan haben, unvollkommener geworden. Wir werden ja durch die Inkarnationen-folge nicht nur vollkommener, sondern wir werden in einer gewissen Weise auch unvollkommener. Oder sind wir etwa nicht unvollkomme­ner, als wir vorher waren, wenn wir einem Menschen eine Beleidigung, ein Ungemach zugefügt haben? Nicht nur diesem Menschen haben wir etwas zugefügt, wir haben uns selber etwas genommen; wir wären als Gesamtpersönlichkeit mehr wert, wenn wir das nicht getan hätten. Solche Dinge haben wir viele auf unser Kerbholz geschrieben, die wir getan haben, und die, weil wir sie getan haben, unsere Unvollkommen­heit begründen. Wenn wir einem Menschen ein Ungemach zugefügt haben",
      "und den Wert, den wir vorher gehabt haben, wieder haben wollen, was muß da geschehen? Wir müssen das Ungemach ausgleichen, wir müssen eine ausgleichende Tat in die Welt setzen, müssen irgend etwas erfinden, was sozusagen uns zwingt, etwas zu überwinden.",
      "Und wenn wir in dieser Richtung nachdenken über unsere Leiden und Schmer­zen, so können wir vielfach sagen: Unsere Leiden, unsere Schmerzen sind geeignet, wenn wir sie überwinden, uns Kraft anzueignen in der Überwindung unserer Unvollkommenheiten. Vollkommener können wir werden durch die Leiden. - Im normalen Menschenleben denken wir ja nicht so; da verhalten wir uns ablehnend gegen die Leiden.",
      "Wir können aber sagen: Jeder Schmerz, jedes Leid, jedes Hemmnis im Le­ben soll eine Andeutung dafür sein, daß wir einen gescheiteren Men­schen in uns haben, als wir selber sind. Den Menschen, der wir selber sind, betrachten wir für eine Weile, trotzdem er derjenige ist, der unser Bewußtsein umfaßt, als den weniger gescheiten; aber einen gescheiteren haben wir, der in den Untergründen unserer Seele schlummert.",
      "Wir, mit unserem gewöhnlichen Bewußtsein, verhalten uns gegen Schmerzen und Leiden ablehnend, aber der Gescheitere führt uns gegen unser Be­wußtsein zu diesen Schmerzen hin, weil wir durch Überwindung dieser Schmerzen etwas abstreifen können. Er führt uns hin zu dem Schmerz und Leid, er weist uns an, das durchzumachen. - Mag sein, daß es zu­nächst ein harter Gedanke ist, aber er verpflichtet uns ja zu nichts, wir können ihn ja nur einmal probeweise machen.",
      "Wir können sagen: Da drin­nen in uns ist ein gescheiterer Mensch, der uns zu Leiden und Schmer­zen hinführt, zu etwas, was wir im Bewußtsein am liebsten vermeiden möchten. Davon denken wir, daß es der Gescheitere in uns ist.",
      "Auf diese Weise kommen wir zu dem für manchen störenden inneren Ergebnis, daß der Gescheitere uns immer zu dem uns Unsympathischen hinführt!",
      "Wir wollen also einmal annehmen, es sei solch ein Gescheiterer in uns, der uns zu dem uns Unsympathischen hinführt, damit wir vor­wärtskommen.",
      "Wir machen aber noch etwas anderes. Nehmen wir unsere Freuden, unsere Förderungen, unsere Lust und sagen wir von diesen wiederum probeweise: Wie wäre es, wenn du dir die Vorstellung bildetest, gleich­gültig, wie es in Wahrheit sich verhält: Du hast deine Lust, deine",
      "Freude, deine Förderungen gar nicht verdient, sie sind dir durch Gnade der höheren geistigen Mächte zugekommen. - Es braucht dies nicht für alles der Fall zu sein, aber probeweise wollen wir annehmen, wir hätten alle Schmerzen und Leiden so herbeigeführt, daß der Gescheitere in uns zu ihnen uns hingeführt hätte, weil wir anerkennen, daß wir sie infolge unserer Unvollkommenheiten notwendig haben und doch nur durch Schmerzen und Leiden hinauskommen können über unsere Unvollkom­menheiten. Und dann wollen wir probeweise das Gegenteilige anneh­men: wir schreiben uns unsere Freuden so zu, als ob sie nicht unser Verdienst wären, sondern als ob sie uns von geistigen Mächten gegeben worden wären.",
      "Es mag wiederum für manchen eitlen Menschen eine bittere Pille sein, so zu denken. Aber probeweise das durchzumachen, ist durchaus etwas, das, wenn der Mensch in seinem Gemüt ganz intensiv solcher Vorstellung fähig ist, zu der Grundempfindung führt, weil es sich wie­derum verwandelt und insofern es unrichtig ist, sich von selber rektifi­ziert: In dir lebt etwas, was nichts zu tun hat mit dem gewöhnlichen Bewußtsein, was tatsächlich tiefer ist, als was du in diesem Leben be­wußt erfahren hast; es ist also etwas in dir, was ein gescheiterer Mensch in dir ist, der sich gern an die ewigen göttlich-geistigen Mächte wendet, die die Welt durchleben. - Da wird dann im inneren Leben selber zur Gewißheit, daß hinter der äußeren eine innere, höhere Individualität liegt. Wir werden uns des ewigen geistigen Wesenskernes durch solche Gedankenübungen bewußt. Das ist außerordentlich bedeutsam. Damit haben wir wiederum etwas, von dem wir sagen können, wir können es ausführen.",
      "Anthroposophie kann eben in jeder Beziehung eine Anweisung sein, um nicht nur irgend etwas zu wissen über das Dasein einer anderen Welt, sondern um in sich selber sich als einen Angehörigen einer ande­ren Welt zu fühlen, um sich als eine solche Individualität zu fühlen, die durch die aufeinanderfolgenden Inkarnationen hindurchgeht.",
      "Es gibt noch eine dritte Art von Erlebnissen. Bei dieser dritten Art wird es allerdings schon schwieriger sein, sie sozusagen zu benützen, um wirklich zu einer Art von innerer Erfahrung von Karma und Reinkar-nation zu kommen. Aber wenn es auch schwierig und langwierig ist,",
      "das, was jetzt gesagt werden soll, es kann wiederum so benützt werden, daß es probeweise genommen wird. Und im redlichen Anwenden auf das äußere Leben wird sich schon herausstellen - zunächst die Wahr­scheinlichkeit, wenn man es glauben kann, dann aber die immer grös­sere Gewißheit -, daß wirklich in dieser Weise unser gegenwärtiges Leben mit dem vorhergehenden zusammenhängt.",
      "Wir wollen einmal annehmen, wir durchleben unser gegenwärtiges Leben zwischen Geburt und Tod, und wir machen uns einmal klar, wenn wir, sagen wir, schon so weit sind, daß wir die Dreißigerjahre er­reicht oder überschritten haben - wir werden schon sehen, daß auch für diejenigen, die jetzt noch nicht so weit sind, es später entsprechende Erlebnisse geben wird -, wir besinnen uns darauf, wie wir gerade um die Dreißigerjahre mit diesen oder jenen Menschen in der Außenwelt zusammengeführt worden sind; wir sind in den Dreißigerjahren bis zum vierzigsten Jahr in den verschiedenen Lebensverbindungen zu­sammengeführt worden mit Menschen der äußeren Welt. Da stellt sich für uns heraus, daß uns die Verbindungen, die wir da geschlossen haben, so erscheinen, als ob wir sie, man möchte sagen, in unserem lebensreif­sten Zustande gemacht hätten, so daß wir wirklich ganz als reife Men­schen am allermeisten dabei waren.",
      "Das kann sich uns durch Über­legung ergeben. Eine Überlegung, die aber aus den Grundsätzen, den Erkenntnissen der Geisteswissenschaft heraus gewonnen worden ist, kann uns doch darauf führen, daß das richtig ist, was jetzt von mir nicht bloß aus solcher Erwägung heraus gesprochen, sondern aus der geisteswissenschaftlichen Forschung heraus mitgeteilt wird.",
      "Also, was ich jetzt sage, ist nicht bloß aus Gedanken logisch gefunden, sondern durch die geisteswissenschaftliche Forschung festgestellt worden, aber logisches Denken kann die Tatsache erhärten und vernünftig finden. Wenn man so nachdenkt über mancherlei, was wir gelernt haben zum Beispiel über die Art, wie die verschiedenen einzelnen menschlichen Glieder herauskommen im Verlaufe des Lebens - wir wissen, daß im siebenten Jahre der Ätherleib, im vierzehnten Jahre der Astralleib, im einundzwanzigsten Jahre die Empfindungsseele, im achtundzwanzig­sten Jahre die Verstandes- und im fünfunddreißigsten Jahre die Be­wußtseinsseele herauskommt -, wenn wir dieses überdenken, dann",
      "können wir sagen: In der Zeit vom dreißigsten bis zum vierzigsten Jahre haben wir es zu tun mit der Ausbildung der Verstandes- und der Bewußtseinsseele.",
      "Die Verstandes- und die Bewußtseinsseele, sie sind diejenigen Kräfte in der menschlichen Natur, welche uns am allermeisten zusammenfüh­ren mit der äußeren physischen Welt, denn sie sind dazu da, daß sie gerade in demjenigen Lebensalter besonders herauskommen, in dem wir am allermeisten im Wechselverkehr mit der äußeren physischen Welt stehen. Im ersten Kindheitsalter werden die Kräfte unseres physischen Leibes herausdirigiert, herausbestimmt, verursacht aus dem, was noch im Inneren unmittelbar verschlossen ist.",
      "Was der Mensch sich als Ur­sachen angeeignet hat in vorhergehenden Inkarnationen, was durchge­gangen ist mit uns durch die Pforte des Todes, was wir an geistigen Kräften gesammelt haben, was wir aus dem früheren Leben mitbringen, das wirkt und webt am Aufbau unseres physischen Leibes. Es wirkt fortwährend unsichtbar vom Inneren heraus in den Leib hinein.",
      "Mit dem fortschreitenden Lebensalter wird diese Einwirkung immer ge­ringer; immer mehr rückt die Lebenszeit heran, da die alten Kräfte den Leib so hergestellt haben. Und dann kommt die Zeit, wo wir der Welt mit einem fertigen Organismus gegenüberstehen.",
      "Was wir im Inneren tragen, hat seine Ausprägung erfahren in unserem äußeren Leibe. Wir treten um das dreißigste Jahr herum - es kann auch etwas früher oder etwas später sein - der Welt am allerphysischsten entgegen, wir stehen da mit der Welt so in Beziehung, daß wir am allerverwandtesten sind mit dem physischen Plan.",
      "Wenn wir nun da glauben, am allermeisten Klarheit, äußere physische Klarheit zu haben über die Lebensverhält­nisse, die wir da anknüpfen, so müssen wir sagen: diese Lebensverhält­nisse, die wir da anknüpfen, sind diejenigen, die für diese Inkarnation eigentlich am wenigsten zusammenhängen mit dem, was im Innersten in uns wirkt und webt von unserer Geburt aus. Dennoch können wir annehmen, daß wir durchaus nicht aus Zufall um das dreißigste Jahr herum mit Menschen zusammengeführt werden, welche gerade dann in unserer Umgebung auftreten müssen.",
      "Wir können vielmehr annehmen, daß auch da unser Karma am Werk ist, daß auch diese Personen etwas mit einer unserer früheren Inkarnationen zu tun haben.",
      "Und da zeigen die geisteswissenschaftlichen Tatsachen, die verschie­dentlich erforscht sind, daß sehr häufig die Personen, mit denen wir zusammenkommen um das dreißigste Jahr herum, in früheren Inkar­nationen so mit uns verwoben sind, daß wir mit ihnen zusammenhän­gen können, meistens am Anfang der unmittelbar vorhergehenden In­karnation oder auch noch früher, als Eltern oder Geschwister. Das ist zunächst eine merkwürdige, überraschende Tatsache.",
      "Es muß nicht so sein, aber viele Fälle zeigen der geisteswissenschaftlichen Forschung, daß es so ist, daß tatsächlich unsere Eltern, die Personen, die beim Aus­gangspunkt unseres vorhergehenden Lebens uns zur Seite gestanden haben, die uns in den physischen Plan hineingestellt haben, denen wir später entwachsen sind, daß die mit uns karmisch so verwoben sind, daß sie in unserem neuen Leben nicht in unserer Kindheit wieder mit uns zusammengeführt werden, sondern erst dann, wenn wir am meisten auf den physischen Plan herausgetreten sind. Es muß nicht so sein, denn die geisteswissenschaftliche Forschung zeigt sehr häufig, daß wir erst in einer nächsten Inkarnation zusammengeführt werden mit sol­chen als Eltern, als Geschwister, überhaupt als Blutsverwandte in Fra­ge Kommenden, mit denen wir in dieser Inkarnation um die Dreißiger-jahre herum uns zusammenfanden.",
      "Also die Bekanntschaften um die Dreißigerjahre herum in irgendeiner Inkarnation können sich so stellen, daß die Personen, die in Betracht kommen, mit uns selber blutsver­wandt sind in vorhergehender oder nachfolgender Inkarnation. Wir können also sagen: Mit den Persönlichkeiten, mit denen dich das Leben zusammenführt in den Dreißigerjahren, mit denen warst du entweder wie mit Eltern und Geschwistern zusammen in einer vorhergehenden Inkarnation, oder du kannst voraussetzen, daß sie in einer der nächsten Inkarnationen mit dir in solcher Eigenschaft zusammenhängen.",
      "Auch das Umgekehrte gilt. Wenn wir diejenigen Persönlichkeiten betrachten, die wir uns willkürlich durch äußere Kräfte, die für den physischen Plan geeignet sind, am wenigsten wählen, also unsere Eltern und Geschwister, mit denen wir am Anfang unseres Lebens zusammen-trafen, wenn wir diese ins Auge fassen, kommen wir sehr häufig darauf, daß wir gerade die Personen, die uns hereingeleiten von der Kindheit an ins Leben, um die Dreißigerjahre herum in einer anderen Inkarnation",
      "wie willkürlich mit unseren Kräften selber ausgewählt haben; mit anderen Worten, daß wir in der Mitte des vorhergehenden Lebens die ausgewählt haben, die jetzt unsere Eltern und Geschwister gewor­den sind.",
      "Besonders interessant ist also die Tatsache, die sich merkwürdiger­weise herausstellt, daß die Sache nicht so liegt, daß wir in aufeinander-folgenden Inkarnationen in den gleichen Verhältnissen sind mit den Persönlichkeiten, mit denen wir zusammenkommen; auch daß wir nicht in den entsprechenden Lebensaltern wie vorher mit ihnen zusam­mentreffen. Auch nicht gerade das Umgekehrte ist der Fall: nicht die Persönlichkeiten, mit denen wir am Lebensende zusammentrafen, ste­hen in einer anderen Inkarnation in Beziehung zu unserem Lebens-anfang, sondern die Persönlichkeiten, mit denen wir in der Lebensmitte zusammentreffen. Also weder die jetzt am Lebensanfang noch die am Lebensende mit uns zusammenkommenden Persönlichkeiten, sondern die jetzt in der Mitte des Lebens mit uns in Berührung kommenden Per­sönlichkeiten waren am Anfang einer vorhergehenden Inkarnation als unsere Blutsverwandten um uns. Die damals im Lebensanfang mit uns zusammen waren, die treten jetzt in der Mitte unseres Lebens auf; und die jetzt am Anfang unseres Lebens um uns sind, von denen können wir voraussetzen, daß wir uns mit ihnen in der Mitte einer der nächsten Inkarnationen zusammenfinden, daß sie als unsere frei gewählten, irgendwo gewählten Lebensgenossen mit uns in Zusammenhang kom­men werden. So merkwürdig sind die karmischen Zusammenhänge.",
      "Was ich jetzt gesagt habe, das sind Dinge, welche die geisteswissen­schaftliche Forschung ergibt. Aber ich habe schon darauf aufmerksam gemacht, daß, wenn man auf die Art und Weise, wie das die geistes­wissenschaftliche Forschung zeigt, die inneren Zusammenhänge zwi­schen Lebensanfang unserer einen und Lebensmitte unserer anderen Inkarnation betrachtet, man begreift, daß das nicht etwas Unsinniges oder Unnützes ist. Die andere Seite ist eben die, daß durch solche Dinge, wenn sie an uns herangebracht werden und wenn wir uns vernünftig dazu stellen, das Leben hell und klar wird. Es wird hell und klar, wenn wir nicht alles einfach hinnehmen, man möchte sagen dumpf, um nicht zu sagen dumm; es wird hell und klar, wenn man versucht, das, was",
      "uns im Leben trifft, irgendwie so zu begreifen, so auffassen zu wollen, daß wir die Beziehungen zu konkreten machen, die ja doch noch nicht ganz verständlich sind, so lange man nur ganz abstrakt im allgemeinen von Karma spricht.",
      "Es ist nützlich, darüber nachzudenken: Woher kommt es, daß wir in der Mitte unseres Lebens förmlich durch Karma getrieben werden, scheinbar mit aller Verstandeskraft diese oder jene Bekanntschaft zu machen, von der wir sagen können: es scheint nicht, als ob sie unab­hängig, objektiv geschlossen wäre? - Das liegt eben daran, daß solche Persönlichkeiten im früheren Leben blutsverwandt mit uns waren und durch unser Karma jetzt mit uns zusammengeführt werden, weil wir etwas mit ihnen zu tun haben.",
      "Wenn wir jedesmal solche Erwägungen anstellen gegenüber dem Ver­lauf des eigenen Lebens, werden wir sehen, daß wirklich Licht in unser Leben hineinkommt. Wenn wir uns auch einmal irren, und selbst wenn es zehnmal unrichtig ist, bei irgendeinem Menschen, den wir im Leben treffen, können wir doch auf das Richtige verfallen. Und wenn wir aus solchen Erwägungen heraus sagen: Diesen Menschen haben wir da oder dort getroffen -, so ist ein solcher Gedanke etwas, das uns wie ein Wegweiser zu anderen Dingen führt, die uns sonst nicht aufgefallen wären und die uns durch ihr Zusammenfallen immer mehr und mehr Gewißheit verschaffen von der Richtigkeit der einzelnen Tatsachen.",
      "Die karmischen Zusammenhänge sind eben nicht solche, die sich durch einen Schlag gewinnen lassen. Wir müssen die höchsten Erkennt­nisse des Lebens, die wichtigsten unser Leben erhellenden Erkenntnisse langsam und allmählich erwerben. Daran wollen allerdings die Men­schen nicht gern glauben. Es ist leichter zu glauben, daß man durch ir­gendeinen Lichtblitz finden könnte: Mit diesen und jenen Persönlich­keiten war ich in einem früheren Leben zusammen, oder dieser oder jener war ich selber. - Daß das alles langsam erworbene Erkenntnisse sein müssen, ist vielleicht unbequem zu denken, aber dennoch ist es so. Selbst wenn wir schon den Glauben hegen, daß es so sein könnte, müs­sen wir noch immer weiterforschen, und unser Glaube wird dann Ge­wißheit annehmen. Selbst für das, was schon mehr und mehr Wahr­scheinlichkeit erweckt auf diesem Gebiete, kommen wir durch Forschen",
      "weiter. Wir vermauern uns die geistige Welt, wenn wir uns auf solchen Gebieten auf rasches Urteilen einlassen.",
      "Versuchen Sie einmal nachzudenken über das, was heute gesagt wor­den ist über die Bekanntschaften in der Mitte unseres Lebens und ihren Zusammenhang mit uns näherstehenden Persönlichkeiten in einer vor­hergehenden Inkarnation. Sie werden dabei auf sehr fruchtbare Ge­danken kommen; namentlich wenn man das gerade noch in Betracht zieht, was gesagt ist in der Schrift über «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft». Dann zeigt sich klar und deutlich, daß das Ergebnis Ihres Nachdenkens mit dem in dieser Schrift Gesagten in Einklang steht.",
      "An das heute Gesagte muß aber noch eine ernstliche Mahnung ge­knüpft werden: Der wirkliche Geistesforscher hütet sich davor, Schlüs­se zu ziehen; er läßt die Dinge an sich herankommen. Wenn sie da sind, prüft er sie erst mit der gewöhnlichen Logik.",
      "Dann kann etwas nicht passieren, was mir vor kurzem erst wieder einmal gegenübertrat und was recht charakteristisch ist für die Art, wie man sich heute der An­throposophie entgegenstellen möchte. Da sagte mir ein sehr gescheiter Herr - ich sage das ohne alle Ironie, mit vollständigem Bekenntnis, daß er wirklich ein gescheiter Herr ist -: Wenn ich lese, was in Ihrem Buch «Geheimwissenschaft im Umriß» steht, so muß ich sagen, es er­scheint das so logisch, so im Zusammenhang mit dem, was die Welt sonst noch an Tatsachen zeigt, daß ich gestehen muß, man könnte auf diese Dinge auch durch bloßes Nachdenken kommen.",
      "Diese Dinge brauchen nicht das Ergebnis übersinnlicher Forschung zu sein. Was in diesem Buch gesagt ist, sind gar keine zweifelhaften Sachen; sie stim­men mit der Wirklichkeit überein. - Ich konnte diesem Herrn die Ver­sicherung geben, daß ich nicht glaube, daß ich durch bloßes Nachden­ken darauf gekommen wäre, und daß ich bei allem Respekt vor seiner Gescheitheit auch nicht glaube, daß er durch bloßes Nachdenken diese Tatsachen gefunden hätte.",
      "Es ist schon wirklich so, daß alles, was lo­gisch eingesehen werden kann auf geisteswissenschaftlichem Gebiet, wirklich nicht durch bloßes Nachdenken gefunden werden könnte! Daß man eine Sache logisch prüfen und begreifen kann, sollte doch noch kein Grund sein, an ihrem geisteswissenschaftlichen Ursprung zu",
      "zweifeln! Ich meine im Gegenteil, daß es eine Art von Beruhigung sein müßte, daß geisteswissenschaftliche Mitteilungen durch logisches Nachdenken als unzweifelhaft richtig erkannt werden können. Es kann schon nicht der Ehrgeiz des Geistesforschers sein, lauter unlogi­sche Dinge zu sagen, damit er Glauben finde. Sie sehen, daß der Geistes-forscher selber nicht auf dem Boden stehen kann, er finde diese Dinge durch Nachdenken. Aber wenn man nachdenkt über die auf geisteswis­senschaftlichem Wege gefundenen Dinge, können sie so logisch erschei­nen, daß sie zu logisch scheinen, so daß man gar keinen Glauben mehr an die geisteswissenschaftlichen Quellen findet, aus denen die Dinge stammen. So ist es tatsächlich bei allen Dingen, von denen gesagt ist, daß sie auf dem Boden reiner geisteswissenschaftlicher Forschung ent­standen sind.",
      "Wenn Ihnen auch zunächst das, was heute hier gesagt worden ist, grotesk erscheint, so versuchen Sie jetzt doch einmal, über die Dinge logisch nachzudenken. Ich würde wahrhaftig nicht, wenn mich nicht geistige Tatsachen dazu geführt hätten, aus dem gewöhnlichen logi­schen Denken es abgeleitet haben, aber nachdem es einmal da ist, kann man es logisch prüfen. Und da wird man sehen: je subtiler, je gewissen­hafter man mit der Prüfung zu Werke geht, desto mehr wird sich her­ausstellen, daß alles stimmt. Selbst von solchen Dingen, bei denen man nicht prüfen kann, ob sie richtig sind, wie das, was heute gesagt worden ist über Eltern und Geschwister des einen Lebens und die Bekannt­schaften in der Mitte des anderen Lebens, wird man schon aus der Art, wie die verschiedenen Glieder in den Zusammenhängen sich verhalten, finden müssen, daß sie einen im höchsten Grad nicht nur wahrschein­lichen, sondern einen bis an die Gewißheit grenzenden Eindruck ma­chen. Und namentlich stellt sich eine Gewißheit als begründet heraus, wenn man die Dinge am Leben prüft. Man wird bei so manchen Per­sönlichkeiten, die man trifft, das eigene Verhalten und das der anderen in einem ganz anderen Lichte sehen, wenn man gleichsam jemandem, den man in der Mitte des Lebens findet, so gegenübersteht, als ob man im vorhergehenden Leben zusammen Geschwister gewesen wäre. Und dadurch wird das ganze Verhältnis viel fruchtbarer werden, als wenn man nur dumpf durchs Leben schreitet.",
      "So können wir sagen: Anthroposophie wird immer mehr nicht nur etwas, was Wissen und Erkenntnis gibt vom Leben, sondern was uns auch Anweisung gibt, wie wir die Verhältnisse des Lebens auffassen und lichtvoll nicht nur für uns selber, sondern auch für unser Ver­halten gegenüber dem Leben und für unsere Lebensaufgabe machen können. Es ist das wichtig, daß wir nicht glauben, wir verderben uns das unmittelbare Drauflosleben. Nur ängstliche Menschen, die es nicht ganz ernst meinen mit dem Leben, können das glauben. Wir aber sol­len uns klar sein, daß dadurch, daß wir das Leben genauer kennen­lernen, wir das Leben auch fruchtbarer, inhaltsreicher machen. Was im Leben an uns herantritt, das soll durch Anthroposophie in einen Ge­sichtskreis gerückt werden, durch den alle Kräfte reicher, zuversicht­licher, hoffnungserweckender werden, als sie waren, bevor sie in die­sen Gesichtskreis gerückt worden sind."
    ],
    "sentences": [
      [
        "Wenn wir das Leben in Betracht ziehen, wie es sich um uns herum ab­spielt, wie es sozusagen seine Wogen hereinwirft in unser Inneres, in all das, was wir selber während unseres physischen Erdendaseins zu emp­finden und zu leiden haben, oder worüber wir uns zu freuen haben, so können wir mehrere besondere Gruppen oder Arten von Erleben ins Auge fassen."
      ],
      [
        "Wir finden zunächst, wenn wir mehr auf uns selbst schauen, auf das­jenige, was in unseren Fähigkeiten, in unseren Talenten liegt, wir fin­den, wenn uns dieses oder jenes gelingt, daß wir uns sagen können:"
      ],
      [
        "Nun, nachdem wir schon einmal dieser oder jener Mensch sind, ist es ganz natürlich und begreiflich, daß uns dieses oder jenes gelingen mußte. - Wir können aber auch gewisse Mißerfolge, die uns betroffen haben, vielleicht gerade das, was wir als Mißgeschick und Unglück be­zeichnen müssen, weil es uns nicht gelungen ist, im ganzen Zusammen-hang unseres Wesens begreiflich finden."
      ],
      [
        "Vielleicht gelingt es uns nicht immer in solchen Fällen, genau nach­zuweisen, wie dieser oder jener Mißerfolg, dieses oder jenes, was uns nicht gelungen ist, zusammenhängt mit unserer Unfähigkeit nach dieser oder jener Richtung.",
        "Aber wenn wir uns dann im allgemeinen sagen müssen: Du warst ja in vielen Beziehungen im jetzigen Erdendasein ein leichtsinniges Subjekt, da kannst du begreifen, daß du unter Umständen verdientermaßen diesen oder jenen Mißerfolg haben mußt -, dann können wir vielleicht nicht ganz unmittelbar den Zusammenhang ein­sehen zwischen Mißerfolg und Unfähigkeit, aber im allgemeinen doch begreiflich finden, daß, wenn wir leichtsinnig waren, nicht alles am Schnürchen gelingen konnte."
      ],
      [
        "Von dem, was jetzt besprochen worden ist, können Sie sich denken, daß wir gewissermaßen eine Art ursächlichen Zusammenhanges ein­sehen könnten zwischen dem, was geschehen mußte aus unseren Fähig­keiten und unseren Unfähigkeiten heraus.",
        "Es gibt aber viele Dinge im Leben, bei denen wir, auch wenn wir noch so genau zu Werke gehen,"
      ],
      [
        "nicht erreichen, das, was uns gelingt oder mißlingt, ohne weiteres in Zusammenhang zu bringen mit unseren Fähigkeiten oder Unfähigkei­ten, bei denen uns gewissermaßen undurchsichtig bleibt, wie wir dieses oder jenes verschuldet haben, oder wie wir es verdient haben.",
        "Kurz, wenn wir mehr unser Innenleben ins Auge fassen, werden wir unter­scheiden können zwischen zwei Gruppen von Erlebnissen.",
        "Die eine Gruppe ist die, bei der wir uns bewußt sind, wie es mit den Ursachen unseres Gelingens und Mißlingens bestellt ist; bei der anderen Gruppe werden wir einen solchen Zusammenhang nicht überschauen können.",
        "Bei dieser letzteren Gruppe wird es uns mehr oder weniger als Zufall erscheinen, daß gerade dieses uns mißlungen, ein anderes uns gelungen ist.",
        "Wir wollen uns zunächst merken, daß es im Leben diese letztere Gruppe von Tatsachen und Erfahrungen hinlänglich gibt, und wollen spater einmal das Augenmerk auf diese Gruppe lenken."
      ],
      [
        "Wir können dann, entgegen dem, was jetzt besprochen worden ist, unser äußeres Schicksal mehr ins Auge fassen.",
        "Da werden wir eigentlich wiederum zwei Gruppen von Tatsachen in bezug auf unser äußeres Geschick ins Auge fassen müssen.",
        "Wir können solche Fälle ins Auge fassen, bei denen wir innerlich einsehen, daß wir in bezug auf diese Er­eignisse, die uns treffen - also nicht, was wir selber unternommen haben -, gewisse Dinge sozusagen selber herbeigeführt haben, schuld sind an solchen Dingen.",
        "Aber von einer anderen Gruppe werden wir sehr geneigt sein zu sagen: Wir können den Zusammenhang nicht ein­sehen mit dem, was wir gewollt, was wir beabsichtigt haben.",
        "Es sind diejenigen Ereignisse, bei denen man im gewöhnlichen Leben davon spricht, daß sie wie ein Zufall, der anscheinend mit nichts, was wir selber herbeigeführt haben, zusammenhängt, in unser Leben herein­gebrochen sind."
      ],
      [
        "Diese zweite Gruppe ist es, die wir jetzt ins Auge fassen wollen mit Bezug auf das innere Leben, also diejenigen Ereignisse, von denen wir nicht einsehen können, daß sie als etwas Direktes, Unmittelbares mit unseren Fähigkeiten und Unfähigkeiten zu tun haben; äußere Ereig­nisse also, das, was wir Zufallsereignisse nennen, von denen wir von vorneherein nicht die Einsicht gewinnen können, daß sie durch irgend etwas Vorhergehendes herbeigeführt worden sind."
      ],
      [
        "Nun kann man einmal probeweise sozusagen mit diesen beiden Grup­pen von Erlebnissen eine Art Experiment machen.",
        "Das Experiment verpflichtet einen ja zunächst zu nichts.",
        "Man probiere sozusagen nur einmal dasjenige, was jetzt gesagt, was jetzt charakterisiert werden soll."
      ],
      [
        "Wir können das Experiment machen, indem wir uns vorstellen: Wie wäre es denn, wenn wir einmal eine Art von künstlichem Menschen konstruieren würden, so einen künstlichen Menschen uns ausdenken würden, daß wir von diesem künstlichen Gedankenmenschen, den wir uns ausgedacht haben, sagen würden, gerade diejenigen Dinge, von de­nen wir keinen Zusammenhang wissen mit unseren Fähigkeiten, die seien so, daß wir den künstlichen Menschen, den wir uns ausdenken, begaben mit den Eigenschaften und Fähigkeiten, welche diese bei uns unbegreiflichen Dinge herbeigeführt haben.",
        "Also ein Mensch, der sol­che Fähigkeiten hat, daß ihm das gelingen oder mißlingen muß, wovon wir uns nicht zuschreiben können, daß es uns nach unseren Fähigkeiten oder Unfähigkeiten gelinge oder mißlinge.",
        "Wir stellen ihn uns also vor als einen solchen Menschen, welcher künstlich, ganz absichtlich herbei­geführt hätte die Dinge, welche zufällig in unserem Leben eingetreten zu sein scheinen."
      ],
      [
        "Man kann von einfachen Beispielen ausgehen, um das zu erläutern.",
        "Nehmen wir an, ein Ziegelstein wäre auf unsere Schulter gefallen und hätte uns an der Schulter verletzt.",
        "Da werden wir zunächst geneigt sein zu sagen: Das ist ein Zufall. - Aber konstruieren wir einen künst­lichen Menschen probeweise zunächst wie ein Experiment, der folgende sonderbare Sache machen würde.",
        "Wir konstruieren einen Menschen, der auf das Dach steigt und dort rasch einen Ziegelstein loslöst, aber nur so weit, daß der Stein noch einen gewissen Halt behält; dann läuft der künstliche Mensch schnell wieder hinunter, so daß, wenn der Stein sich loslöst, er gerade auf seine Schultern fällt.",
        "So machen wir es in be­zug auf alle Ereignisse, von denen uns einfällt, daß sie zufällig in un­serem Leben eingetreten sind.",
        "Einen künstlichen Menschen konstruieren wir, der alles verschuldet oder herbeiführt, wovon wir im gewöhnlichen Leben nicht einsehen können, wie es mit uns zusammenhängt."
      ],
      [
        "Wenn man das tut, so könnte es zunächst ausschauen wie ein bloßes Gedankenspiel.",
        "Und es verpflichtet zu nichts, wenn man das tut.",
        "Aber"
      ],
      [
        "eine Merkwürdigkeit stellt sich heraus, wenn man das tut.",
        "Wenn man einen solchen Menschen ausgedacht hat und ihn begabt hat mit den ge­schilderten Eigenschaften, dann macht dieser künstliche Gedanken­mensch einen ganz merkwürdigen Eindruck auf uns."
      ],
      [
        "Wir kommen näm­lich von dem Bilde eines Menschen, das wir uns da gemacht haben, ob­wohl es scheinbar so künstlich konstruiert ist, nicht mehr los; es faszi­niert uns, es macht den Eindruck, als ob es doch irgend etwas mit uns zu tun haben müßte.",
        "Dafür sorgt schon die Empfindung, die man ge­genüber dem künstlichen Gedankenmenschen hat."
      ],
      [
        "Wenn man sich recht sehr hineinvertieft in dieses Bild, so läßt es einen ganz sicher nicht mehr los.",
        "Ein merkwürdiger Prozeß bildet sich in unserem Gemüt; ein Pro­zeß, den man vergleichen kann mit folgendem: Wir kommen zu einem inneren Gemütsprozeß, den der Mensch alle Augenblicke durchmacht."
      ],
      [
        "Wir können irgend etwas denken, können einen Entschluß fassen; wir brauchen dazu etwas, was wir einmal gewußt haben, und wir wenden alle möglichen künstlichen Mittel an, um uns auf das zu besinnen, was wir gewußt haben.",
        "Bei diesem Anstrengen, in das Gedächtnis etwas heraufzurufen, was uns entfallen ist, machen wir natürlich einen Ge­mütsprozeß durch, das Uns-Besinnen, wie wir es im gewöhnlichen Leben nennen."
      ],
      [
        "Und alle die Gedanken, die wir zu Hilfe nehmen, um uns auf etwas zu besinnen, sind Hilfsgedanken.",
        "Versuchen Sie nur ein­mal, darauf zu kommen, wieviel solcher Hilfsgedanken Sie oftmals aufwenden müssen, die Sie dann wieder fallen lassen, um auf das zu kommen, was Sie wissen wollen."
      ],
      [
        "Solche Hilfsgedanken sind dazu da, daß sie den Weg eröffnen auf das zu Besinnende, was wir eigentlich gegenwärtig brauchen."
      ],
      [
        "Gerade so, nur wie etwas weit Umfassenderes, ist jener Gedanken-mensch, den wir geschildert haben, ein Hilfsprozeß.",
        "Er läßt uns nicht mehr los; er arbeitet in uns so, daß wir sagen, er ist etwas, was als Ge­danke in uns wohnt, etwas, was da fortwirkt, was sich umwandelt in uns; was tatsächlich sich umwandelt zu der Idee, zu dem Gedanken, der nun auftritt wie etwas, was uns einfällt, wenn wir uns im gewöhn­lichen Erinnerungsprozeß besinnen, der auftritt wie etwas, was uns überwältigt.",
        "Wie wenn etwas sagen würde: So kann er nicht bleiben, er ändert sich um in dir, er entfaltet Leben, er wird zu etwas anderem!"
      ],
      [
        "Das drängt sich uns auf - machen Sie das Experiment! -, es drängt sich uns so auf, daß er uns sagt: Ja, das ist etwas, was mit einem anderen als deinem jetzigen Erdendasein einiges zu tun hat.",
        "Eine Art Be­sinnung auf ein anderes Erdendasein, der Gedanke tritt ganz bestimmt auf.",
        "Es ist mehr ein Gefühl als ein Gedanke, eine Empfindung, aber eine solche, wie wenn wir das, was im Gemüt auftritt, so fühlen wie das, was wir selber einmal in einer früheren Inkarnation auf dieser Erde waren."
      ],
      [
        "Anthroposophie ist eben durchaus, wenn wir sie als etwas Ganzes betrachten, nicht bloß eine Summe von Theorien, von Mitteilungen von Tatsachen, die da bestehen, sondern sie gibt uns Vorschriften und An­weisungen, wie man dies oder jenes erreichen kann.",
        "Die Anthropo­sophie sagt: Du wirst mehr und mehr dahin geführt, daß du dich leich­ter besinnen kannst, wenn du dies oder jenes machst. - Man kann auch sagen, und das ist durchaus aus dem Gebiet der Erfahrung geschöpft:"
      ],
      [
        "Wenn du so vorgehst, bekommst du einen Gemütseindruck, einen Ge­fühlseindruck von dem Menschen, der du früher warst. - Wir kommen da zu dem, was man nennen könnte: eine Erweiterung unseres Gedächt­nisses.",
        "Nun ist dies, was sich uns da eröffnet, wirklich zunächst nur eine Gedankentatsache, solange wir den geschilderten Gedankenmen­schen konstruieren.",
        "Aber der Gedankenmensch bleibt nicht Gedanken-mensch.",
        "Er verwandelt sich in Empfindungs-, in Gemütseindrücke, und indem er dies tut, wissen wir: In dem, was wir empfinden, haben wir etwas, was zu tun hat mit unserer vorhergehenden Inkarnation.",
        "Unser Gedächtnis erweitert sich auf unsere frühere Inkarnation."
      ],
      [
        "In dieser Inkarnation erinnern wir uns an die Dinge, bei denen wir mit unseren Gedanken zugegen sind.",
        "Sie alle wissen, daß man sich ver­hältnismäßig leicht erinnert an die Dinge, in welche unsere Gedanken hereingespielt haben.",
        "Im gewöhnlichen Leben bleibt aber nicht so leicht lebendig dasjenige, was in unser Gefühl hereingespielt hat.",
        "Wenn Sie versuchen, zurückzudenken an das, was Ihnen großen Schmerz gemacht hat vor zehn, zwanzig Jahren, so werden Sie sich leicht an die Vorstel­lung erinnern; Sie werden sich an das, was sich da abgespielt hat, in Ihren Vorstellungen zurückversetzen; aber zu einer lebendigen Emp­findung des damals empfundenen Schmerzes können Sie nicht ge­langen.",
        "Der Schmerz verblaßt, die Erinnerung an ihn ergießt sich in"
      ],
      [
        "unsere Vorstellung.",
        "Was jetzt geschildert worden ist, ist ein Gemüts­gedächtnis, ein Gefühlsgedächtnis.",
        "Und in der Tat, als solches fühlen wir unsere frühere Inkarnation.",
        "In der Tat tritt das auf, was wir nen­nen können: eine Erinnerung an frühere Inkarnationen.",
        "Es kann ja nicht so ohne weiteres angesehen werden wie das, was in die gegen­wärtige Inkarnation hereinspielt, was Träger der Erinnerung ist an frühere Inkarnationen.",
        "Bedenken Sie nur einmal, wie innig verwachsen unsere Vorstellungen mit dem Ausdruck der Vorstellungen sind, mit unserer Sprache.",
        "Die Sprache ist die verkörperte Vorstellungswelt.",
        "Und die Sprache muß ein jeder Mensch in den einzelnen Leben wieder ler­nen.",
        "Der größte Sprachforscher oder Sprachkenner muß als Kind mit Mühe seine Muttersprache erlernen.",
        "Es ist noch nicht der Fall vorge­kommen, daß ein Gymnasiast das Griechische deshalb leicht lernte, weil er sich rasch erinnert hätte an das Griechisch, das er in früheren Inkarnationen gesprochen hat!"
      ],
      [
        "Der Dichter Hebbel hat mit einigen Gedanken den Plan eines Dra­mas aufgezeichnet, das er schreiben wollte.",
        "Schade, daß er es nicht ge­tan hat, es wäre ein sehr interessantes Drama geworden.",
        "Die Handlung war so gedacht, daß der wiederverkörperte Plato als Gymnasiast bei der Erklärung des alten Plato die allerschlechteste Zensur bekäme!",
        "Lei­der ist der Plan Hebbels nicht zur Ausführung gekommen.",
        "Wir brau­chen nicht bloß daran zu denken, daß die Lehrer zum Teil pedantisch sind und so weiter.",
        "Wir wissen, daß das, was Hebbel aufzeichnete, darauf beruht, daß das Vorstellungsmäßige, was sich in den unmittel­baren Erfahrungsvorstellungen abspielt, mehr oder weniger unmittel­bar beschränkt ist auf die gegenwärtige Inkarnation.",
        "Und es ist so, wie jetzt angedeutet worden ist, daß die erste Impression, der erste Ein­druck von der vorhergehenden Inkarnation unmittelbar auftritt als Gefühlsgedächtnis, als eine neue Art von Gedächtnis.",
        "Was wir als Ein­druck haben, wenn dieses Gedächtnis von dem Gedankenmenschen her entsteht, den wir konstruiert haben, ist mehr ein Gefühl, aber ein sol­ches Gefühl, daß man versteht: Der Eindruck rührt von einem Kerl her, der einmal existiert hat und der du selber warst! - Man bekommt etwas wie ein Erinnerungsgefühl als ersten Eindruck an die vorher­gehende Inkarnation."
      ],
      [
        "Was da geschildert worden ist als Konstruktion eines Gedanken­menschen, das ist nur ein Mittel.",
        "Dieses Mittel wandelt sich um in einen solchen Gemüts- oder Gefühlseindruck.",
        "Jeder Mensch, der an die An­throposophie herantritt, hat eigentlich mehr oder weniger Gelegenheit, leicht dasjenige auszuführen, was jetzt geschildert worden ist.",
        "Und wenn er dieses ausführt, wird er schon sehen, daß er wirklich in seinem Inneren einen Eindruck erhält, sagen wir - um ein anderes Beispiel zu gebrauchen - einen Eindruck, den er so schildern könnte: Ich habe einmal eine Landschaft gesehen, ich habe vergessen, wie sie aussieht, sie hat mir aber gefallen! - Nun wird, wenn es in diesem Leben war, die Landschaft keinen sehr lebendigen Gefühlseindruck mehr machen; aber wenn der Eindruck aus einer vorhergehenden Inkarnation stammte, so wird er einen besonders lebendigen Gefühlseindruck machen.",
        "Wir kön­nen uns so einen besonders lebendigen Eindruck als Gefühlseindruck von unserer früheren Inkarnation machen.",
        "Und wenn wir dann objek­tiv die geschilderten Eindrücke beobachten, werden wir zuweilen etwas wie ein bitteres oder ein bittersüßes oder ein saures Gefühl haben aus dem, was sich ergibt als Umwandlung des Gedankenmenschen.",
        "Dieses sauersüße oder sonstige Gefühl ist der Eindruck, den unsere frühere Inkarnation auf uns macht; es ist eine Art von Gefühls- oder Gemüts-eindruck."
      ],
      [
        "Damit wurde versucht, Sie aufmerksam zu machen auf etwas, was dazu führen kann, bei jedem Menschen eine Art unmittelbarer Gewiß­heit hervorzurufen, daß er in früheren Leben existiert hat; Gewißheit dadurch, daß er sich ein Gefühl verschafft, daß er Gemüts- oder Ge­fühlseindrücke hat, von denen er weiß: Das hast du gewiß nicht in diesem Leben irgendwo erworben. - Ein solcher Eindruck tritt aber so auf, wie für das gewöhnliche Leben eine Erinnerungsvorstellung auf­tritt.",
        "Nun kann man fragen: Wie kann man wissen, daß der Eindruck, den man hat, eine Erinnerung ist? - Sehen Sie, da kann man nur sagen, beweisen läßt sich so etwas nicht.",
        "Aber es liegt derselbe Tatbestand vor, der auch sonst im Leben vorliegt, wenn wir uns an etwas erinnern und bei gesunden Sinnen sind.",
        "Da können wir wissen, daß das, was in uns auftritt in Gedanken, sich wirklich bezieht auf etwas, was wir erlebt haben.",
        "Die Erfahrung selber gibt die Gewißheit.",
        "Was wir uns in der"
      ],
      [
        "angegebenen Art vorstellen, gibt uns die Gewißheit davon, daß der Eindruck, der im Gemüt auftaucht, sich nicht auf etwas bezieht, was mit uns zu tun hatte im gegenwärtigen Leben, sondern auf etwas, was mit uns zu tun hatte im vorhergehenden Leben."
      ],
      [
        "Da haben wir auf künstliche Weise in uns hervorgerufen etwas, was uns mit unserem vorhergehenden Leben in Zusammenhang bringt.",
        "Wir können noch mancherlei andere Arten von innerlichen probeweisen Er­fahrungen und Erlebnissen hernehmen und können dadurch wieder weitergehen und in uns wachrufen so etwas wie Empfindungen von früheren Leben.",
        "Da können wir wiederum in anderer Hinsicht die Er­lebnisse dessen, was wir im Leben durchmachen, teilen; wir können sie in anderer Weise in Gruppen teilen.",
        "Wir können auf der einen Seite in eine Gruppe fassen, was wir an Leiden, an Schmerzen, an Hemmnissen im Leben durchgemacht haben; auf der anderen Seite, was uns bewußt geworden ist als Förderungen, als Freude, Lust und so weiter."
      ],
      [
        "Nun können wir wiederum probeweise uns auf folgenden Stand­punkt stellen.",
        "Wir können einmal sagen: Ja, wir haben diese Schmer­zen, diese Leiden erfahren.",
        "So wie wir in dieser Inkarnation einmal sind, wie das normale Leben nun einmal abläuft, sind uns unsere Schmerzen, unsere Leiden etwas Fatales, etwas, was wir in gewisser Beziehung gern von uns hinwegstoßen würden.",
        "Tun wir dies einmal probeweise nicht.",
        "Nehmen wir probeweise an, wir würden aus einem gewissen Grunde diese Schmerzen, diese Leiden und Hemmnisse selber herbeigeführt haben, denn durch diese früheren Leben, wenn sie wirk­lich da sind, sind wir in gewisser Weise durch das, was wir getan haben, unvollkommener geworden.",
        "Wir werden ja durch die Inkarnationen-folge nicht nur vollkommener, sondern wir werden in einer gewissen Weise auch unvollkommener.",
        "Oder sind wir etwa nicht unvollkomme­ner, als wir vorher waren, wenn wir einem Menschen eine Beleidigung, ein Ungemach zugefügt haben?",
        "Nicht nur diesem Menschen haben wir etwas zugefügt, wir haben uns selber etwas genommen; wir wären als Gesamtpersönlichkeit mehr wert, wenn wir das nicht getan hätten.",
        "Solche Dinge haben wir viele auf unser Kerbholz geschrieben, die wir getan haben, und die, weil wir sie getan haben, unsere Unvollkommen­heit begründen.",
        "Wenn wir einem Menschen ein Ungemach zugefügt haben"
      ],
      [
        "und den Wert, den wir vorher gehabt haben, wieder haben wollen, was muß da geschehen?",
        "Wir müssen das Ungemach ausgleichen, wir müssen eine ausgleichende Tat in die Welt setzen, müssen irgend etwas erfinden, was sozusagen uns zwingt, etwas zu überwinden."
      ],
      [
        "Und wenn wir in dieser Richtung nachdenken über unsere Leiden und Schmer­zen, so können wir vielfach sagen: Unsere Leiden, unsere Schmerzen sind geeignet, wenn wir sie überwinden, uns Kraft anzueignen in der Überwindung unserer Unvollkommenheiten.",
        "Vollkommener können wir werden durch die Leiden. - Im normalen Menschenleben denken wir ja nicht so; da verhalten wir uns ablehnend gegen die Leiden."
      ],
      [
        "Wir können aber sagen: Jeder Schmerz, jedes Leid, jedes Hemmnis im Le­ben soll eine Andeutung dafür sein, daß wir einen gescheiteren Men­schen in uns haben, als wir selber sind.",
        "Den Menschen, der wir selber sind, betrachten wir für eine Weile, trotzdem er derjenige ist, der unser Bewußtsein umfaßt, als den weniger gescheiten; aber einen gescheiteren haben wir, der in den Untergründen unserer Seele schlummert."
      ],
      [
        "Wir, mit unserem gewöhnlichen Bewußtsein, verhalten uns gegen Schmerzen und Leiden ablehnend, aber der Gescheitere führt uns gegen unser Be­wußtsein zu diesen Schmerzen hin, weil wir durch Überwindung dieser Schmerzen etwas abstreifen können.",
        "Er führt uns hin zu dem Schmerz und Leid, er weist uns an, das durchzumachen. - Mag sein, daß es zu­nächst ein harter Gedanke ist, aber er verpflichtet uns ja zu nichts, wir können ihn ja nur einmal probeweise machen."
      ],
      [
        "Wir können sagen: Da drin­nen in uns ist ein gescheiterer Mensch, der uns zu Leiden und Schmer­zen hinführt, zu etwas, was wir im Bewußtsein am liebsten vermeiden möchten.",
        "Davon denken wir, daß es der Gescheitere in uns ist."
      ],
      [
        "Auf diese Weise kommen wir zu dem für manchen störenden inneren Ergebnis, daß der Gescheitere uns immer zu dem uns Unsympathischen hinführt!"
      ],
      [
        "Wir wollen also einmal annehmen, es sei solch ein Gescheiterer in uns, der uns zu dem uns Unsympathischen hinführt, damit wir vor­wärtskommen."
      ],
      [
        "Wir machen aber noch etwas anderes.",
        "Nehmen wir unsere Freuden, unsere Förderungen, unsere Lust und sagen wir von diesen wiederum probeweise: Wie wäre es, wenn du dir die Vorstellung bildetest, gleich­gültig, wie es in Wahrheit sich verhält: Du hast deine Lust, deine"
      ],
      [
        "Freude, deine Förderungen gar nicht verdient, sie sind dir durch Gnade der höheren geistigen Mächte zugekommen. - Es braucht dies nicht für alles der Fall zu sein, aber probeweise wollen wir annehmen, wir hätten alle Schmerzen und Leiden so herbeigeführt, daß der Gescheitere in uns zu ihnen uns hingeführt hätte, weil wir anerkennen, daß wir sie infolge unserer Unvollkommenheiten notwendig haben und doch nur durch Schmerzen und Leiden hinauskommen können über unsere Unvollkom­menheiten.",
        "Und dann wollen wir probeweise das Gegenteilige anneh­men: wir schreiben uns unsere Freuden so zu, als ob sie nicht unser Verdienst wären, sondern als ob sie uns von geistigen Mächten gegeben worden wären."
      ],
      [
        "Es mag wiederum für manchen eitlen Menschen eine bittere Pille sein, so zu denken.",
        "Aber probeweise das durchzumachen, ist durchaus etwas, das, wenn der Mensch in seinem Gemüt ganz intensiv solcher Vorstellung fähig ist, zu der Grundempfindung führt, weil es sich wie­derum verwandelt und insofern es unrichtig ist, sich von selber rektifi­ziert: In dir lebt etwas, was nichts zu tun hat mit dem gewöhnlichen Bewußtsein, was tatsächlich tiefer ist, als was du in diesem Leben be­wußt erfahren hast; es ist also etwas in dir, was ein gescheiterer Mensch in dir ist, der sich gern an die ewigen göttlich-geistigen Mächte wendet, die die Welt durchleben. - Da wird dann im inneren Leben selber zur Gewißheit, daß hinter der äußeren eine innere, höhere Individualität liegt.",
        "Wir werden uns des ewigen geistigen Wesenskernes durch solche Gedankenübungen bewußt.",
        "Das ist außerordentlich bedeutsam.",
        "Damit haben wir wiederum etwas, von dem wir sagen können, wir können es ausführen."
      ],
      [
        "Anthroposophie kann eben in jeder Beziehung eine Anweisung sein, um nicht nur irgend etwas zu wissen über das Dasein einer anderen Welt, sondern um in sich selber sich als einen Angehörigen einer ande­ren Welt zu fühlen, um sich als eine solche Individualität zu fühlen, die durch die aufeinanderfolgenden Inkarnationen hindurchgeht."
      ],
      [
        "Es gibt noch eine dritte Art von Erlebnissen.",
        "Bei dieser dritten Art wird es allerdings schon schwieriger sein, sie sozusagen zu benützen, um wirklich zu einer Art von innerer Erfahrung von Karma und Reinkar-nation zu kommen.",
        "Aber wenn es auch schwierig und langwierig ist,"
      ],
      [
        "das, was jetzt gesagt werden soll, es kann wiederum so benützt werden, daß es probeweise genommen wird.",
        "Und im redlichen Anwenden auf das äußere Leben wird sich schon herausstellen - zunächst die Wahr­scheinlichkeit, wenn man es glauben kann, dann aber die immer grös­sere Gewißheit -, daß wirklich in dieser Weise unser gegenwärtiges Leben mit dem vorhergehenden zusammenhängt."
      ],
      [
        "Wir wollen einmal annehmen, wir durchleben unser gegenwärtiges Leben zwischen Geburt und Tod, und wir machen uns einmal klar, wenn wir, sagen wir, schon so weit sind, daß wir die Dreißigerjahre er­reicht oder überschritten haben - wir werden schon sehen, daß auch für diejenigen, die jetzt noch nicht so weit sind, es später entsprechende Erlebnisse geben wird -, wir besinnen uns darauf, wie wir gerade um die Dreißigerjahre mit diesen oder jenen Menschen in der Außenwelt zusammengeführt worden sind; wir sind in den Dreißigerjahren bis zum vierzigsten Jahr in den verschiedenen Lebensverbindungen zu­sammengeführt worden mit Menschen der äußeren Welt.",
        "Da stellt sich für uns heraus, daß uns die Verbindungen, die wir da geschlossen haben, so erscheinen, als ob wir sie, man möchte sagen, in unserem lebensreif­sten Zustande gemacht hätten, so daß wir wirklich ganz als reife Men­schen am allermeisten dabei waren."
      ],
      [
        "Das kann sich uns durch Über­legung ergeben.",
        "Eine Überlegung, die aber aus den Grundsätzen, den Erkenntnissen der Geisteswissenschaft heraus gewonnen worden ist, kann uns doch darauf führen, daß das richtig ist, was jetzt von mir nicht bloß aus solcher Erwägung heraus gesprochen, sondern aus der geisteswissenschaftlichen Forschung heraus mitgeteilt wird."
      ],
      [
        "Also, was ich jetzt sage, ist nicht bloß aus Gedanken logisch gefunden, sondern durch die geisteswissenschaftliche Forschung festgestellt worden, aber logisches Denken kann die Tatsache erhärten und vernünftig finden.",
        "Wenn man so nachdenkt über mancherlei, was wir gelernt haben zum Beispiel über die Art, wie die verschiedenen einzelnen menschlichen Glieder herauskommen im Verlaufe des Lebens - wir wissen, daß im siebenten Jahre der Ätherleib, im vierzehnten Jahre der Astralleib, im einundzwanzigsten Jahre die Empfindungsseele, im achtundzwanzig­sten Jahre die Verstandes- und im fünfunddreißigsten Jahre die Be­wußtseinsseele herauskommt -, wenn wir dieses überdenken, dann"
      ],
      [
        "können wir sagen: In der Zeit vom dreißigsten bis zum vierzigsten Jahre haben wir es zu tun mit der Ausbildung der Verstandes- und der Bewußtseinsseele."
      ],
      [
        "Die Verstandes- und die Bewußtseinsseele, sie sind diejenigen Kräfte in der menschlichen Natur, welche uns am allermeisten zusammenfüh­ren mit der äußeren physischen Welt, denn sie sind dazu da, daß sie gerade in demjenigen Lebensalter besonders herauskommen, in dem wir am allermeisten im Wechselverkehr mit der äußeren physischen Welt stehen.",
        "Im ersten Kindheitsalter werden die Kräfte unseres physischen Leibes herausdirigiert, herausbestimmt, verursacht aus dem, was noch im Inneren unmittelbar verschlossen ist."
      ],
      [
        "Was der Mensch sich als Ur­sachen angeeignet hat in vorhergehenden Inkarnationen, was durchge­gangen ist mit uns durch die Pforte des Todes, was wir an geistigen Kräften gesammelt haben, was wir aus dem früheren Leben mitbringen, das wirkt und webt am Aufbau unseres physischen Leibes.",
        "Es wirkt fortwährend unsichtbar vom Inneren heraus in den Leib hinein."
      ],
      [
        "Mit dem fortschreitenden Lebensalter wird diese Einwirkung immer ge­ringer; immer mehr rückt die Lebenszeit heran, da die alten Kräfte den Leib so hergestellt haben.",
        "Und dann kommt die Zeit, wo wir der Welt mit einem fertigen Organismus gegenüberstehen."
      ],
      [
        "Was wir im Inneren tragen, hat seine Ausprägung erfahren in unserem äußeren Leibe.",
        "Wir treten um das dreißigste Jahr herum - es kann auch etwas früher oder etwas später sein - der Welt am allerphysischsten entgegen, wir stehen da mit der Welt so in Beziehung, daß wir am allerverwandtesten sind mit dem physischen Plan."
      ],
      [
        "Wenn wir nun da glauben, am allermeisten Klarheit, äußere physische Klarheit zu haben über die Lebensverhält­nisse, die wir da anknüpfen, so müssen wir sagen: diese Lebensverhält­nisse, die wir da anknüpfen, sind diejenigen, die für diese Inkarnation eigentlich am wenigsten zusammenhängen mit dem, was im Innersten in uns wirkt und webt von unserer Geburt aus.",
        "Dennoch können wir annehmen, daß wir durchaus nicht aus Zufall um das dreißigste Jahr herum mit Menschen zusammengeführt werden, welche gerade dann in unserer Umgebung auftreten müssen."
      ],
      [
        "Wir können vielmehr annehmen, daß auch da unser Karma am Werk ist, daß auch diese Personen etwas mit einer unserer früheren Inkarnationen zu tun haben."
      ],
      [
        "Und da zeigen die geisteswissenschaftlichen Tatsachen, die verschie­dentlich erforscht sind, daß sehr häufig die Personen, mit denen wir zusammenkommen um das dreißigste Jahr herum, in früheren Inkar­nationen so mit uns verwoben sind, daß wir mit ihnen zusammenhän­gen können, meistens am Anfang der unmittelbar vorhergehenden In­karnation oder auch noch früher, als Eltern oder Geschwister.",
        "Das ist zunächst eine merkwürdige, überraschende Tatsache."
      ],
      [
        "Es muß nicht so sein, aber viele Fälle zeigen der geisteswissenschaftlichen Forschung, daß es so ist, daß tatsächlich unsere Eltern, die Personen, die beim Aus­gangspunkt unseres vorhergehenden Lebens uns zur Seite gestanden haben, die uns in den physischen Plan hineingestellt haben, denen wir später entwachsen sind, daß die mit uns karmisch so verwoben sind, daß sie in unserem neuen Leben nicht in unserer Kindheit wieder mit uns zusammengeführt werden, sondern erst dann, wenn wir am meisten auf den physischen Plan herausgetreten sind.",
        "Es muß nicht so sein, denn die geisteswissenschaftliche Forschung zeigt sehr häufig, daß wir erst in einer nächsten Inkarnation zusammengeführt werden mit sol­chen als Eltern, als Geschwister, überhaupt als Blutsverwandte in Fra­ge Kommenden, mit denen wir in dieser Inkarnation um die Dreißiger-jahre herum uns zusammenfanden."
      ],
      [
        "Also die Bekanntschaften um die Dreißigerjahre herum in irgendeiner Inkarnation können sich so stellen, daß die Personen, die in Betracht kommen, mit uns selber blutsver­wandt sind in vorhergehender oder nachfolgender Inkarnation.",
        "Wir können also sagen: Mit den Persönlichkeiten, mit denen dich das Leben zusammenführt in den Dreißigerjahren, mit denen warst du entweder wie mit Eltern und Geschwistern zusammen in einer vorhergehenden Inkarnation, oder du kannst voraussetzen, daß sie in einer der nächsten Inkarnationen mit dir in solcher Eigenschaft zusammenhängen."
      ],
      [
        "Auch das Umgekehrte gilt.",
        "Wenn wir diejenigen Persönlichkeiten betrachten, die wir uns willkürlich durch äußere Kräfte, die für den physischen Plan geeignet sind, am wenigsten wählen, also unsere Eltern und Geschwister, mit denen wir am Anfang unseres Lebens zusammen-trafen, wenn wir diese ins Auge fassen, kommen wir sehr häufig darauf, daß wir gerade die Personen, die uns hereingeleiten von der Kindheit an ins Leben, um die Dreißigerjahre herum in einer anderen Inkarnation"
      ],
      [
        "wie willkürlich mit unseren Kräften selber ausgewählt haben; mit anderen Worten, daß wir in der Mitte des vorhergehenden Lebens die ausgewählt haben, die jetzt unsere Eltern und Geschwister gewor­den sind."
      ],
      [
        "Besonders interessant ist also die Tatsache, die sich merkwürdiger­weise herausstellt, daß die Sache nicht so liegt, daß wir in aufeinander-folgenden Inkarnationen in den gleichen Verhältnissen sind mit den Persönlichkeiten, mit denen wir zusammenkommen; auch daß wir nicht in den entsprechenden Lebensaltern wie vorher mit ihnen zusam­mentreffen.",
        "Auch nicht gerade das Umgekehrte ist der Fall: nicht die Persönlichkeiten, mit denen wir am Lebensende zusammentrafen, ste­hen in einer anderen Inkarnation in Beziehung zu unserem Lebens-anfang, sondern die Persönlichkeiten, mit denen wir in der Lebensmitte zusammentreffen.",
        "Also weder die jetzt am Lebensanfang noch die am Lebensende mit uns zusammenkommenden Persönlichkeiten, sondern die jetzt in der Mitte des Lebens mit uns in Berührung kommenden Per­sönlichkeiten waren am Anfang einer vorhergehenden Inkarnation als unsere Blutsverwandten um uns.",
        "Die damals im Lebensanfang mit uns zusammen waren, die treten jetzt in der Mitte unseres Lebens auf; und die jetzt am Anfang unseres Lebens um uns sind, von denen können wir voraussetzen, daß wir uns mit ihnen in der Mitte einer der nächsten Inkarnationen zusammenfinden, daß sie als unsere frei gewählten, irgendwo gewählten Lebensgenossen mit uns in Zusammenhang kom­men werden.",
        "So merkwürdig sind die karmischen Zusammenhänge."
      ],
      [
        "Was ich jetzt gesagt habe, das sind Dinge, welche die geisteswissen­schaftliche Forschung ergibt.",
        "Aber ich habe schon darauf aufmerksam gemacht, daß, wenn man auf die Art und Weise, wie das die geistes­wissenschaftliche Forschung zeigt, die inneren Zusammenhänge zwi­schen Lebensanfang unserer einen und Lebensmitte unserer anderen Inkarnation betrachtet, man begreift, daß das nicht etwas Unsinniges oder Unnützes ist.",
        "Die andere Seite ist eben die, daß durch solche Dinge, wenn sie an uns herangebracht werden und wenn wir uns vernünftig dazu stellen, das Leben hell und klar wird.",
        "Es wird hell und klar, wenn wir nicht alles einfach hinnehmen, man möchte sagen dumpf, um nicht zu sagen dumm; es wird hell und klar, wenn man versucht, das, was"
      ],
      [
        "uns im Leben trifft, irgendwie so zu begreifen, so auffassen zu wollen, daß wir die Beziehungen zu konkreten machen, die ja doch noch nicht ganz verständlich sind, so lange man nur ganz abstrakt im allgemeinen von Karma spricht."
      ],
      [
        "Es ist nützlich, darüber nachzudenken: Woher kommt es, daß wir in der Mitte unseres Lebens förmlich durch Karma getrieben werden, scheinbar mit aller Verstandeskraft diese oder jene Bekanntschaft zu machen, von der wir sagen können: es scheint nicht, als ob sie unab­hängig, objektiv geschlossen wäre? - Das liegt eben daran, daß solche Persönlichkeiten im früheren Leben blutsverwandt mit uns waren und durch unser Karma jetzt mit uns zusammengeführt werden, weil wir etwas mit ihnen zu tun haben."
      ],
      [
        "Wenn wir jedesmal solche Erwägungen anstellen gegenüber dem Ver­lauf des eigenen Lebens, werden wir sehen, daß wirklich Licht in unser Leben hineinkommt.",
        "Wenn wir uns auch einmal irren, und selbst wenn es zehnmal unrichtig ist, bei irgendeinem Menschen, den wir im Leben treffen, können wir doch auf das Richtige verfallen.",
        "Und wenn wir aus solchen Erwägungen heraus sagen: Diesen Menschen haben wir da oder dort getroffen -, so ist ein solcher Gedanke etwas, das uns wie ein Wegweiser zu anderen Dingen führt, die uns sonst nicht aufgefallen wären und die uns durch ihr Zusammenfallen immer mehr und mehr Gewißheit verschaffen von der Richtigkeit der einzelnen Tatsachen."
      ],
      [
        "Die karmischen Zusammenhänge sind eben nicht solche, die sich durch einen Schlag gewinnen lassen.",
        "Wir müssen die höchsten Erkennt­nisse des Lebens, die wichtigsten unser Leben erhellenden Erkenntnisse langsam und allmählich erwerben.",
        "Daran wollen allerdings die Men­schen nicht gern glauben.",
        "Es ist leichter zu glauben, daß man durch ir­gendeinen Lichtblitz finden könnte: Mit diesen und jenen Persönlich­keiten war ich in einem früheren Leben zusammen, oder dieser oder jener war ich selber. - Daß das alles langsam erworbene Erkenntnisse sein müssen, ist vielleicht unbequem zu denken, aber dennoch ist es so.",
        "Selbst wenn wir schon den Glauben hegen, daß es so sein könnte, müs­sen wir noch immer weiterforschen, und unser Glaube wird dann Ge­wißheit annehmen.",
        "Selbst für das, was schon mehr und mehr Wahr­scheinlichkeit erweckt auf diesem Gebiete, kommen wir durch Forschen"
      ],
      [
        "weiter.",
        "Wir vermauern uns die geistige Welt, wenn wir uns auf solchen Gebieten auf rasches Urteilen einlassen."
      ],
      [
        "Versuchen Sie einmal nachzudenken über das, was heute gesagt wor­den ist über die Bekanntschaften in der Mitte unseres Lebens und ihren Zusammenhang mit uns näherstehenden Persönlichkeiten in einer vor­hergehenden Inkarnation.",
        "Sie werden dabei auf sehr fruchtbare Ge­danken kommen; namentlich wenn man das gerade noch in Betracht zieht, was gesagt ist in der Schrift über «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft».",
        "Dann zeigt sich klar und deutlich, daß das Ergebnis Ihres Nachdenkens mit dem in dieser Schrift Gesagten in Einklang steht."
      ],
      [
        "An das heute Gesagte muß aber noch eine ernstliche Mahnung ge­knüpft werden: Der wirkliche Geistesforscher hütet sich davor, Schlüs­se zu ziehen; er läßt die Dinge an sich herankommen.",
        "Wenn sie da sind, prüft er sie erst mit der gewöhnlichen Logik."
      ],
      [
        "Dann kann etwas nicht passieren, was mir vor kurzem erst wieder einmal gegenübertrat und was recht charakteristisch ist für die Art, wie man sich heute der An­throposophie entgegenstellen möchte.",
        "Da sagte mir ein sehr gescheiter Herr - ich sage das ohne alle Ironie, mit vollständigem Bekenntnis, daß er wirklich ein gescheiter Herr ist -: Wenn ich lese, was in Ihrem Buch «Geheimwissenschaft im Umriß» steht, so muß ich sagen, es er­scheint das so logisch, so im Zusammenhang mit dem, was die Welt sonst noch an Tatsachen zeigt, daß ich gestehen muß, man könnte auf diese Dinge auch durch bloßes Nachdenken kommen."
      ],
      [
        "Diese Dinge brauchen nicht das Ergebnis übersinnlicher Forschung zu sein.",
        "Was in diesem Buch gesagt ist, sind gar keine zweifelhaften Sachen; sie stim­men mit der Wirklichkeit überein. - Ich konnte diesem Herrn die Ver­sicherung geben, daß ich nicht glaube, daß ich durch bloßes Nachden­ken darauf gekommen wäre, und daß ich bei allem Respekt vor seiner Gescheitheit auch nicht glaube, daß er durch bloßes Nachdenken diese Tatsachen gefunden hätte."
      ],
      [
        "Es ist schon wirklich so, daß alles, was lo­gisch eingesehen werden kann auf geisteswissenschaftlichem Gebiet, wirklich nicht durch bloßes Nachdenken gefunden werden könnte!",
        "Daß man eine Sache logisch prüfen und begreifen kann, sollte doch noch kein Grund sein, an ihrem geisteswissenschaftlichen Ursprung zu"
      ],
      [
        "zweifeln!",
        "Ich meine im Gegenteil, daß es eine Art von Beruhigung sein müßte, daß geisteswissenschaftliche Mitteilungen durch logisches Nachdenken als unzweifelhaft richtig erkannt werden können.",
        "Es kann schon nicht der Ehrgeiz des Geistesforschers sein, lauter unlogi­sche Dinge zu sagen, damit er Glauben finde.",
        "Sie sehen, daß der Geistes-forscher selber nicht auf dem Boden stehen kann, er finde diese Dinge durch Nachdenken.",
        "Aber wenn man nachdenkt über die auf geisteswis­senschaftlichem Wege gefundenen Dinge, können sie so logisch erschei­nen, daß sie zu logisch scheinen, so daß man gar keinen Glauben mehr an die geisteswissenschaftlichen Quellen findet, aus denen die Dinge stammen.",
        "So ist es tatsächlich bei allen Dingen, von denen gesagt ist, daß sie auf dem Boden reiner geisteswissenschaftlicher Forschung ent­standen sind."
      ],
      [
        "Wenn Ihnen auch zunächst das, was heute hier gesagt worden ist, grotesk erscheint, so versuchen Sie jetzt doch einmal, über die Dinge logisch nachzudenken.",
        "Ich würde wahrhaftig nicht, wenn mich nicht geistige Tatsachen dazu geführt hätten, aus dem gewöhnlichen logi­schen Denken es abgeleitet haben, aber nachdem es einmal da ist, kann man es logisch prüfen.",
        "Und da wird man sehen: je subtiler, je gewissen­hafter man mit der Prüfung zu Werke geht, desto mehr wird sich her­ausstellen, daß alles stimmt.",
        "Selbst von solchen Dingen, bei denen man nicht prüfen kann, ob sie richtig sind, wie das, was heute gesagt worden ist über Eltern und Geschwister des einen Lebens und die Bekannt­schaften in der Mitte des anderen Lebens, wird man schon aus der Art, wie die verschiedenen Glieder in den Zusammenhängen sich verhalten, finden müssen, daß sie einen im höchsten Grad nicht nur wahrschein­lichen, sondern einen bis an die Gewißheit grenzenden Eindruck ma­chen.",
        "Und namentlich stellt sich eine Gewißheit als begründet heraus, wenn man die Dinge am Leben prüft.",
        "Man wird bei so manchen Per­sönlichkeiten, die man trifft, das eigene Verhalten und das der anderen in einem ganz anderen Lichte sehen, wenn man gleichsam jemandem, den man in der Mitte des Lebens findet, so gegenübersteht, als ob man im vorhergehenden Leben zusammen Geschwister gewesen wäre.",
        "Und dadurch wird das ganze Verhältnis viel fruchtbarer werden, als wenn man nur dumpf durchs Leben schreitet."
      ],
      [
        "So können wir sagen: Anthroposophie wird immer mehr nicht nur etwas, was Wissen und Erkenntnis gibt vom Leben, sondern was uns auch Anweisung gibt, wie wir die Verhältnisse des Lebens auffassen und lichtvoll nicht nur für uns selber, sondern auch für unser Ver­halten gegenüber dem Leben und für unsere Lebensaufgabe machen können.",
        "Es ist das wichtig, daß wir nicht glauben, wir verderben uns das unmittelbare Drauflosleben.",
        "Nur ängstliche Menschen, die es nicht ganz ernst meinen mit dem Leben, können das glauben.",
        "Wir aber sol­len uns klar sein, daß dadurch, daß wir das Leben genauer kennen­lernen, wir das Leben auch fruchtbarer, inhaltsreicher machen.",
        "Was im Leben an uns herantritt, das soll durch Anthroposophie in einen Ge­sichtskreis gerückt werden, durch den alle Kräfte reicher, zuversicht­licher, hoffnungserweckender werden, als sie waren, bevor sie in die­sen Gesichtskreis gerückt worden sind."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG Stuttgart, 21.Februar 1912",
    "paragraphs": [
      "Es waren gestern Fragen, die das menschliche Karma berührten, welche wir zur Sprache zu bringen hatten, und zwar wurde versucht, diese Fragen des menschlichen Karmas so zu behandeln, daß sie uns erschei­nen in Anknüpfung an innere Vorgänge der menschlichen Seele; man möchte sagen, daß sie uns erscheinen in Anknüpfung an etwas Erreich­bares. Denn es wurde darauf aufmerksam gemacht, daß man gewisse Dinge sozusagen probeweise in seinem Seelenleben einrichten könne und daß man dadurch in seinem Seelenleben gewisse innere Erfahrun­gen hervorrufen kann, welche zu einer ganz bestimmt ausgesprochenen Überzeugung von der Wahrheit des Karmagesetzes führen müssen.",
      "Wenn wir solche Fragen immer wieder und wieder in die Gesichtskreise unserer anthroposophischen Betrachtung rücken, so ist dies durchaus nichts irgendwie Willkürliches, sondern es hängt damit zusammen, daß ja immer mehr und mehr wird erkannt werden müssen, wie sich das, was wir Anthroposophie im wahren, echten Sinne des Wortes nennen, zum Leben und zu der ganzen menschlichen Entwickelung verhält. Man kann sich ja zweifellos eine wenigstens annähernd richtige Vor­stellung davon bilden, wie alles menschliche Lehen nach und nach ver­ändert werden muß, wenn erst eine größere Anzahl von Personen die Überzeugung, die ja zugrunde liegt solch einer Betrachtung wie der gestrigen, zu der ihrigen machen wird.",
      "Das Leben muß sich dadurch, daß die Menschen sich durch die Durchdringung solcher Wahrheiten anders zum Leben stellen, in gewisser Weise ändern. Und wir kom­men dadurch zu der außerordentlich wichtigen Frage, die eine Ge­wissensfrage sein müßte für diejenigen Persönlichkeiten, die sich der anthroposophischen Bewegung einfügen, wir kommen zu der Frage: Was macht eigentlich einen Menschen der Gegenwart zum Anthropo­sophen?",
      "Nun ist ja sehr leicht ein Mißverständnis möglich, wenn man diese Frage in einer entsprechenden Weise zu beantworten versucht, denn es verwechseln ja heute noch sehr viele Persönlichkeiten, auch solche Persönlichkeiten,",
      "die zu uns gehören, die anthroposophische Bewegung mit irgendeiner äußeren Organisation. Nichts soll gesagt werden gegen eine solche äußere Organisation, die ja in gewisser Beziehung da sein muß, damit auf dem physischen Plane die Pflege der Anthroposophie mög­lich sei; aber wichtig ist es, sich klar darüber zu werden, daß zu einer solchen äußeren Organisation im Grunde genommen alle diejenigen Menschen gehören können, die in ernster, aufrichtiger Weise ein tie­feres Interesse haben an den Fragen des Geisteslebens und die ihre Welt­anschauung im Sinne einer solchen Bewegung des Geisteslebens ver­tiefen wollen. Damit ist schon gesagt, daß keinerlei Dogma, keinerlei positives Bekenntnis gefordert werden muß von denjenigen, welche sich einer so charakterisierten Organisation anschließen. Aber ein an­deres ist es, einmal klipp und klar hinzuweisen auf dasjenige, was den modernen Menschen, den Menschen unserer Gegenwart, eigentlich zum Anthroposophen macht.",
      "Die gewöhnliche Überzeugung, daß man es zu tun habe mit einer geistigen Welt, sie ist gewiß der Anfang der anthroposophischen Über­zeugung, und sie muß immer da betont werden, wo man die Anthro­posophie hinausträgt in die Öffentlichkeit und von ihren Aufgaben, ihren Zielen, ihrer gegenwärtigen Mission gegenüber der Öffentlichkeit spricht. Aber innerhalb der eigentlichen anthroposophischen Kreise muß man sich doch klar werden, daß etwas viel Bestimmteres, viel Aus­gesprocheneres als nur die Überzeugung von einer geistigen Welt den Anthroposophen ausmacht. Denn schließlich hat man diese Überzeu­gung von einer geistigen Welt immer gehabt in denjenigen Kreisen, die nicht geradezu materialistisch waren. Das, was den gegenwärtigen Menschen zum Anthroposophen macht, was im Grunde genommen noch nicht in der Theosophie zum Beispiel des Jakob Böhme oder eines anderen Theosophen der Vorzeit enthalten war, ist etwas, worauf die Kultur unseres Abendlandes mit aller Gewalt hingearbeitet hat; auf der einen Seite so, daß geradezu dieses Hinarbeiten zu einer charakte­ristischen Eigenschaft des Strebens vieler Menschen geworden ist. Und auf der anderen Seite steht dem gegenüber die Tatsache, daß dieses, was so eigenartig den Anthroposophen als solchen charakterisiert, heute noch von der äußeren Kultur, der äußeren menschlichen Bildung",
      "am allermeisten angefochten wird, als etwas Törichtes angesehen wird.",
      "Gewiß, wir lernen vieles durch die Anthroposophie kennen. Wir ler­nen kennen die Entwickelung der Menschheit, wir lernen kennen selbst die Entwickelung unserer Erde und unseres Planetensystems. Alle diese Dinge gehören zu den Grundlagen des anthroposophisch Strebenden. Aber das hier Gemeinte, besonders Bedeutsame für den Anthropo­sophen der Gegenwart ist das Erringen einer Überzeugung in bezug auf die Fragen von Reinkarnation und Karma. Und die Art und Weise, wie die Menschen sich aneignen werden diese Überzeugung von Reinkar­nation und Karma, wie sie die Möglichkeit finden werden, den Gedan­ken von Reinkarnation und Karma in das allgemeine Leben überzu­führen, das wird eben dieses moderne Leben von der Gegenwart in die Zukunft hinein im wesentlichen umgestalten. Es wird ganz neue Le­bensformen, ein ganz neues menschliches Zusammenleben schaffen; ein solches Zusammenleben aber, wie es notwendig ist, wenn die Kultur der Menschheit nicht dem Niedergang verfallen soll, sondern wirklich aufwärtssteigen, vorwärtsgehen soll. Solche Erwägungen, solche inne­ren Seelenerlebnisse, wie sie gestern hervorgehoben worden sind, kann im Grunde genommen jeder moderne Mensch schon machen; und wenn er nur genügend Energie und Tatkraft hat, so wird er schon zu einer inneren Überzeugung der Wahrheit von Reinkarnation und Karma kommen. Demjenigen aber, was wahre Anthroposophie eigentlich wollen soll, dem steht gegenüber, man möchte sagen, der ganze äußere Grundcharakter unserer gegenwärtigen Zeit.",
      "Dieser Grundcharakter unserer gegenwärtigen Zeit, er drückt sich vielleicht in keiner Tatsache so radikal charakteristisch aus als darin, daß man immerhin ein mehr oder weniger großes Interesse an den Zen­tralfragen finden kann, die sich auf religiöse Dinge beziehen, die sich beziehen auf die Entwickelung des Menschen und der Welt; auch auf Karma und Reinkarnation. Man wird mit solchen Fragen auch noch, wenn sie sich erstrecken auf dasjenige, was die einzelnen positiven Leh­ren der einzelnen Religionsbekenntnisse sind - sagen wir in bezug auf die Natur des Buddha oder des Christus -, man wird mit der Be­sprechung solcher Fragen heute immerhin noch ein weites Interesse finden.",
      "Aber dieses Interesse wird wesentlich schwächer, läßt nach; läßt auch bei denjenigen, die sich heute Anthroposophen nennen, recht sehr nach, wenn davon gesprochen wird im einzelnen Konkreten, wie sich Anthroposophie einleben soll in alle Einzelheiten des äußeren Lebens. Es ist das ja im wesentlichen sehr begreiflich. Der Mensch steht im äußeren Leben drinnen, der eine hat diese, der andere jene Position in der Welt. Man möchte sagen, daß so, wie die Welt sich darlebt mit ihren heutigen Ordnungen, es sich fast ausnimmt wie ein großes Etablisse­ment; der einzelne Mensch ist darin wie ein Triebrad. So fühlt er sich in dieser Welt mit seiner Arbeit, seinen Sorgen, mit dem, was ihn be­schäftigt vom Morgen bis zum Abend, und er weiß nichts anderes, als daß er sich dieser äußeren Weltordnung zu fügen hat.",
      "Daneben tritt dann die Frage auf, die für jede Seele da sein muß, die nur ein wenig aufzublicken vermag von dem, was der Alltag ihr gibt, die Frage nach dem Schicksal der Seele, nach dem Anfang und Ende des Seelenlebens, nach dem Zusammenhang mit den göttlich-geistigen Wesenheiten, nach den Kräften der Welt. Und zwischen dem, was dem Menschen der Alltag zu geben hat, worüber er Sorge hat und so weiter, und dem, was er auf dem Gebiete der Anthroposophie erhält, tritt ein tiefer Abgrund, eine weite Kluft auf.",
      "Und man möchte sagen: Für die meisten Menschen, und auch für die Anthroposophen der Gegenwart, ist dieses Zusammenstimmen ihrer anthroposophischen Überzeugung mit dem, was sie draußen im alltäglichen Leben tun und vorstellen, fast gar nicht vorhanden. Man braucht nur irgendeine konkrete Frage in der Öffentlichkeit aufzuwerfen und im geisteswissenschaftlichen, im anthroposophischen Sinn zu behandeln, so wird man gleich sehen, daß das Interesse, welches für die Behandlung allgemeiner religiöser und ähnlicher Fragen noch vorhanden war, für solche konkrete Fragen nicht da ist.",
      "Nun kann man ja nicht verlangen, daß Anthroposophie sich gleich unmittelbar einlebt, daß sie jeder schon in seinen Handgrif­fen zum Ausdruck bringt. Aber aufmerksam muß darauf gemacht wer­den, daß die anthroposophische Geisteswissenschaft die Mission hat, gerade alles dasjenige ins Leben einzuführen, dem Leben einzuverlei­ben, was aus einer Seele folgen muß, welche sich nach und nach die Überzeugung verschafft, daß die Ideen von Reinkarnation und Karma",
      "Realitäten sind. So könnte geradezu hingestellt werden als charakte­ristisches Kennzeichen des gegenwärtigen Anthroposophen, daß er auf dem Wege ist, sich eine begründete innere Überzeugung vom Walten der Idee von Reinkarnation und Karma anzueignen. Alles Übrige, möchte man sagen, ergibt sich daraus dann schon von selber als unmit­telbare Konsequenz, als Folgeerscheinung.",
      "Das kann natürlich auch nicht so gehen, daß nun jeder etwa denkt, mit dem, was ich aus Reinkarnation und Karma gewinne, werde ich jetzt unmittelbar das äußere Leben anfassen. Das geht natürlich nicht. Aber Vorstellungen muß man davon gewinnen, wie Reinkarnation und Karma sich in das äußere Leben hineinfinden müssen, so daß sie zu dirigierenden Mächten des äußeren Lebens werden können.",
      "Nehmen wir einmal die Idee des Karma, wie das Karma wirkt durch die verschiedenen Verkörperungen des Menschen hindurch. Da müssen wir, wenn ein Mensch hereintritt in die Welt, seine Fähigkeiten und Kräfte letzten Endes ansehen als das Ergebnis der Ursachen, die er sel­ber in früheren Verkörperungen gelegt hat. Wir müssen, wenn wir konse­quent diese Idee durchführen, wirklich jeden Menschen als eine Art von innerem Rätsel behandeln, als etwas, aus dem sich herausarbeiten muß dasjenige, was in den dunklen Untergründen seiner früheren Inkarna­tionen schwebt. Nicht nur in der Erziehung, sondern im ganzen Leben wird ein ganz bedeutsamer Umschwung herbeigeführt, wenn Ernst ge­macht wird mit einer solchen Idee vom Karma. Und es würde, wenn das eingesehen würde, die Idee vom Karma aus einer bloß theoretischen Idee umgewandelt in etwas, was wirklich in das praktische Leben eingreifen muß, was wirklich eine praktische Sache des Lebens werden könnte.",
      "Alles äußere Leben, so wie es sich uns heute darbietet, ist aber überall ein Bild eines solchen menschlichen Zusammenhanges, der geformt und gebildet worden ist mit Ausschluß, ja mit Verleugnung der Idee von Reinkarnation und Karma. Und gleichsam, als ob man verschütten wollte alle Möglichkeiten, daß die Menschen durch die eigene Seelenentwickelung darauf kommen könnten, daß es Reinkarnation und Kar­ma gibt, so ist dieses äußere Leben heute eingerichtet. In der Tat, es gibt zum Beispiel nichts, was so sehr feindlich gesinnt ist einer wirklichen Überzeugung von Reinkarnation und Karma als der Grundsatz des",
      "Lebens, daß man für dasjenige, was man unmittelbar als Arbeit leistet, einen der Arbeit entsprechenden Lohn, der die Arbeit geradezu bezahlt, einheimsen müsse. Nicht wahr, eine solche Rede klingt sonderbar, recht sonderbar! Nun müssen Sie die Sache auch nicht so betrachten, als wenn die Anthroposophie nun gleich radikal die Grundsätze einer Lebenspraxis über den Haufen werfen und über Nacht eine neue Lebensord­nung einführen wollte. Das kann nicht sein. Aber der Gedanke müßte den Menschen nahetreten, daß in der Tat in einer Weltordnung, in der man daran denkt, Lohn und Arbeit müßten sich unmittelbar ent­sprechen, in der man sozusagen durch seine Arbeit dasjenige verdienen muß, was zum Leben notwendig ist, niemals eine wirkliche Grundüber­zeugung von Reinkarnation und Karma gedeihen kann. Selbstverständ­lich muß die bestehende Lebensordnung zunächst so bleiben, denn ge­rade der Anthroposoph muß einsehen, daß das, was besteht, wiederum durch die Karmaordnung hervorgerufen worden ist, und daß es in die­ser Beziehung zu Recht und mit Notwendigkeit besteht. Aber er muß durchaus die Möglichkeit haben zu begreifen, daß sich wie ein neuer Keim innerhalb des Organismus unserer Weltordnung dasjenige ent­wickelt, was aus der Anerkennung der Idee von Reinkarnation und Karma folgen kann und muß.",
      "Vor allen Dingen folgt aus der Idee des Karma, daß wir nicht durch einen Zufall - das geht gerade aus der gestrigen Betrachtung hervor, wie ich glaube - uns hereingestellt fühlen sollen in die Weltordnung, nicht durch Zufall uns hingestellt fühlen sollen auf den Posten, auf dem wir uns befinden im Leben, sondern daß diesem Hingestelltsein gleich­sam eine Art von unterbewußtem Willensentschluß zugrunde liegt; daß wir gewissermaßen, bevor wir in dieses irdische Dasein getreten sind, in das wir uns herausgearbeitet haben aus der geistigen Welt zwischen Tod und Geburt, als Ergebnis unserer früheren Inkarnationen in der geistigen Welt den Willensentschluß gefaßt haben - den wir nur wie­der vergessen haben, als wir uns in den Körper einlebten -, uns hinzu­stellen an den Platz, an dem wir stehen. So daß das Ergebnis eines vor­geburtlichen, vorirdischen eigenen Willensentschlusses uns an unseren Lebensplatz hinstellt und uns ausstattet gerade mit der Neigung für diejenigen Schicksalsschläge, die uns treffen. Wenn der Mensch dann",
      "zu der Überzeugung kommt von der Wahrheit des Karmagesetzes, kann es nicht ausbleiben, daß er in gewisser Beziehung beginnt, Neigung, ja vielleicht sogar Liebe zu haben für den Posten der Welt, auf den er sich gestellt hat, welcher Art dieser Posten auch sein mag.",
      "Nun können Sie allerdings sagen: Ja, du sprichst ganz merkwürdige Worte, sonderbare, merkwürdige Worte! Bei Dichtern, Schriftstellern, bei anderen geistig wirkenden Menschen mag dies ja gehen. Da hast du dann, wenn du zu diesen sprichst, gut predigen, daß sie Freude, Liebe, Hingebung haben sollen für den Posten, auf dem sie im Leben stehen. Aber wie ist es denn mit all denjenigen Menschen, welche auf Lebensposten stehen, die wahrhaftig zunächst nicht geeignet sind, mit ihrem Inhalt, ihren Tätigkeiten auf den Menschen sonderlich sympathisch zu wirken, die geeignet sind, in den Menschenseelen die Empfindung her­vorzurufen, daß man zu den vernachlässigten, den vom Leben unter­jochten Persönlichkeiten gehört? - Wer möchte leugnen, daß ein großer Teil der gegenwärtigen Kulturbestrebungen darauf hinausgeht, fort­während Verbesserungen in unser Leben einzuführen, die sozusagen Abhilfe schaffen können jenem Unzufriedensein mit einem so unsym­pathischen Hineingestelltsein in das Leben. Wie vielgestaltige Partei­ungen, wie viele sektiererische Bestrebungen gibt es, die sozusagen das Leben nach allen Richtungen so verbessern wollen, daß auch in äußer­licher Beziehung eintreten könnte eine Art von Erträglichkeit des ge­samten Erdenlebens der Menschheit.",
      "Aber alle diese Bestrebungen rechnen nicht mit dem einen, damit nämlich, daß die Art von Unbefriedigtsein, die für viele Menschen ge­rade heute aus dem Leben fließen muß, in vielfacher Beziehung zusam­menhängt mit dem ganzen Gang der Menschheitsentwickelung, daß im Grunde genommen durch die Art und Weise, wie sich die Menschen in der Vorzeit entwickelt haben, sie zu einem solchen Karma gekom­men sind, und daß aus dem Zusammenwirken dieser verschiedenen Karmen der heutige Zustand der menschlichen Kulturentwickelung mit Notwendigkeit hervorgegangen ist. Und wenn wir diesen Zustand der Kultur charakterisieren wollen, müssen wir sagen, er erweist sich im höchsten Grade als kompliziert. Wir müssen auch sagen, daß das, was der Mensch tut, was er ausführt, immer weniger zusammenhängt",
      "mit dem, was der Mensch liebt. Und wenn man heute die Menschen abzählen würde, die eine von ihnen ungeliebte Betätigung in ihrer äußeren Lebensposition vollbringen müssen, ihre Zahl würde wahrhaftig weit größer sein als die Zahl derjenigen, die sich dazu bekennen: Ich kann nicht anders sagen, als daß ich meine äußere Betätigung liebe, daß sie mich glücklich und zufrieden macht!",
      "Erst vor kurzem hörte ich, wie ein Mensch zu einer befreundeten Persönlichkeit merkwürdige Worte sprach. Er meinte: Überblicke ich mein Leben mit allen Einzelheiten, so muß ich sagen, wenn ich dieses Leben im gegenwärtigen Augenblicke wiederum von Kindheit an be­ginnen sollte und es gerade so durchleben könnte, wie ich es haben möchte, ich würde das gleiche wiederum tun, was ich bis jetzt getan habe. - Da antwortete die befreundete Persönlichkeit: Dann gehören Sie zu den Menschen, die in der Gegenwart am wenigsten zu finden sind. - Wahrscheinlich hat diese Persönlichkeit in bezug auf die mei­sten Menschen der Gegenwart recht.",
      "Es gibt nicht viele Zeitgenossen, die den Ausspruch fällen, sie würden, wenn es auf sie ankäme, das Le­ben mit all dem, was es an Freude, an Schmerz, an Schicksalsschlägen, an Hemmnissen gebracht hat, sogleich wiederum beginnen und wären ganz zufrieden, wenn es ihnen wiederum genau dasselbe bieten würde. Man kann nicht sagen, daß diese Tatsache, die angeführt worden ist, nämlich daß es so wenig Menschen gibt in der Gegenwart, die sozusagen ihr gegenwärtiges Karma wiederum aufnehmen würden mit allen Ein­zelheiten, nicht zusammenhänge mit alledem, was der heutige Kulturzustand der Menschheit gebracht hat.",
      "Unser Leben ist komplizierter geworden, aber es ist so geworden, wie es ist, durch die verschieden­artigen Karmen der einzelnen heute auf der Erde lebenden Persönlich­keiten. Das ist ganz zweifellos. Für denjenigen, der nur ein wenig hineinsieht in den Gang der Menschheitsentwickelung, liegt die Sache gar nicht so, daß wir etwa in der Zukunft einem Leben entgegengehen könnten, das weniger kompliziert wäre.",
      "Im Gegenteil, das Leben wird immer komplizierter und komplizierter werden! Das äußere Leben wird immer komplizierter, und wenn in Zukunft noch so viele Tätig­keiten dem Menschen abgenommen werden durch die Maschinen.",
      "Le­ben, welche die Menschen in dieser physischen Inkarnation beseligen,",
      "wird es in sehr geringem Umfang geben können, wenn nicht ganz an­dere Verhältnisse eintreten als jene, die sich wirksam erweisen in unserer Kultur. Und diese anderen Verhältnisse müssen die sein, die sich ergeben aus dem Durchdrungensein der Menschenseele mit der Wahrheit von Reinkarnation und Karma.",
      "Durch diese Wahrheit wird man erkennen, daß mit der Komplika­tion der äußeren Kultur etwas noch ganz anderes parallel gehen wird. Was wird notwendig sein, damit die Menschen immer mehr und mehr durchdrungen werden von der Wahrheit von Reinkarnation und Kar­ma? Was wird notwendig sein, damit der Begriff von Reinkarnation und Karma, wie es durchaus sein muß, wenn unsere Kultur nicht einen Niedergang erfahren soll, in verhältnismäßig ganz kurzer Zeit so in unsere Schulbildung hineinwirkt, daß er die Menschen schon in ihrer Kindheit ergreift, wie heute die Überzeugung von der Richtigkeit des kopernikanischen Weltsystems schon das Kind ergreift?",
      "Was war notwendig, damit das kopernikanische Weltsystem die Seelen ergriffen hat? - Mit diesem kopernikanischen Weltsystem ist es eine ganz eigentümliche Sache. Ich will nicht über das kopernikanische Weltsystem sprechen, sondern nur über sein In-die-Welt-Treten. Be­denken Sie doch nur einmal, daß dieses kopernikanische Weltsystem ausgedacht worden ist von einem christlichen Domherrn, und daß Kopernikus so über dieses Weltsystem denken konnte, daß er sein Werk, in dem er dieses Weltsystem ausgebaut hatte, dem Papst gewidmet hat. Er konnte glauben, daß es ganz im Sinne des Christentums sei, was er ausgedacht hatte. Gab es damals einen Beweis für den Kopernikanis­mus? Konnte jemand das beweisen, was Kopernikus ausgedacht hatte? Niemand konnte den Kopernikanismus beweisen. Und dennoch, be­denken Sie die Schnelligkeit, mit der er eingezogen ist in die Mensch­heit! Seit wann kann man ihn erst beweisen? Einigermaßen sicher erst, soweit er richtig ist, seit den fünfzigerjahren des 19. Jahrhunderts, erst seit dem Foucaultschen Pendelversuch. Es gab früher keinen Beweis dafür, daß die Erde sich dreht. Es ist ein Unsinn, wenn behauptet wird, daß Kopernikus alles das, was er als Hypothese aufgestellt und ein­gesehen hat, auch hat beweisen können; das gilt auch hinsichtlich der Behauptung, daß die Erde sich um ihre Achse dreht.",
      "Erst seit man darauf gekommen ist, daß das schwingende Polpendel das Bestreben hat, seine Schwingungsebene auch gegenüber der Um­drehung der Erde beizubehalten, und daß, wenn man ein langes Pendel schwingen läßt, sich dessen Schwingungsrichtung in bezug auf die Erd­oberfläche dreht, konnte man den Schluß ziehen: es muß sich die Erde unter dem Pendel weggedreht haben. Dieser Versuch, der eigentlich erst ein wirklicher Beweis dafür ist, daß die Erde sich bewegt, der wurde erst im 19. Jahrhundert gemacht. Früher gab es keine Möglichkeit, den Kopernikanismus als etwas anderes denn als eine Hypothese anzu­sehen. Dennoch hat er so gewirkt auf die Natur der menschlichen Seele der neueren Zeit, daß, während Kopernikus zwar geglaubt hat, daß er sein Werk dem Papst widmen dürfe, es bis zum Jahre 1822 auf dem Index stand. Erst im Jahre 1822 wurde das Werk, auf dem der Koper­nikanismus aufgebaut ist, abgesetzt vom Index. Es wurde also abge­setzt, bevor es einen richtigen Beweis für die Anschauung des Koperni­kus gab. Die Kraft des Impulses, mit dem sich das kopernikanische Weltsystem in die menschliche Seele einlebte, dieser Kopernikanismus selbst zwang die Kirche, ihn als etwas anzuerkennen, was nicht etwas Ketzerisches ist.",
      "Es ist mir immer im tiefsten Sinne charakteristisch erschienen, daß mir diese Erkenntnis von der Erdbewegung, als ich ein kleiner Bub war, in der Schule zuerst von einem Pfarrer, nicht von einem Lehrer vorgetragen worden ist. Und wer will daran zweifeln, daß der Koper­nikanismus sich eingenistet hat, daß er sich bis in das Kindergemüt eingenistet hat? - Wir wollen aber jetzt nicht von seinen Wahrheiten und seinen Irrtümern sprechen.",
      "So muß sich einnisten - aber dazu hat die Menschheit nicht so lange Zeit wie zur Aufnahme des Kopernikanismus -, wenn nicht die Menschheitskultur einen Niedergang erfahren will, die Wahrheit von Reinkarnation und Karma. Und jene, die sich heute Anthroposophen nennen, sind dazu berufen, das ihrige zu tun, daß die Wahrheit von Reinkarnation und Karma sich bis in das Kindergemüt hinein ergießt. Damit ist natürlich nicht gesagt, daß jetzt jene Anthroposophen, die Kinder haben, nun ihren Kindern dieses als ein Dogma beibringen. Ein­sicht in diese Dinge muß man haben.",
      "Ich habe nicht umsonst den Kopernikanismus angeführt. An dem, was dem Kopernikanismus seinen Erfolg gebracht hat, können wir lernen, was dem Reinkarnations- und dem Karmagedanken seine Kul­turerfolge bringen kann. Was gehörte denn dazu, daß der Kopernika­nismus sich so schnell verbreitete? - Ich werde jetzt etwas furchtbar Ketzerisches aussprechen, etwas geradezu Greuliches für den modernen Menschen. Aber es handelt sich eben darum, daß Anthroposophie von den Anthroposophen ebenso ernst und bedeutsam aufgefaßt werde, wie einmal das Christentum bei seinem ersten Entstehen von den ersten Christen aufgefaßt worden ist, die sich auch in Gegensatz gebracht haben zu dem, was da war. Wenn Anthroposophie nicht so ernst ge­nommen wird von ihren Bekennern, so kann sie nicht für die Mensch­heit leisten, was geleistet werden muß.",
      "Also ich muß etwas Greuliches sagen, und das besteht darin: Der Kopernikanismus, dasjenige, was die Menschen heute lernen als koper­nikanisches Weltsystem, dem wahrhaftig nicht sein großes Verdienst und damit seine Bedeutung als Kulturtatsache allerersten Ranges ab­gesprochen werden soll, konnte sich einnisten in die menschliche Seele dadurch, daß man ein oberflächlicher Mensch sein konnte, um ein An­hänger dieses Systems zu sein. Oberflächlichkeit und Äußerlichkeit ge­hörten dazu, um sich vom Kopernikanismus schneller zu überzeugen. Damit ist nicht gesagt, daß die Bedeutung des Kopernikus für die Menschheit herabgemindert werden soll. Nein; aber gesagt kann wer­den, daß man kein sehr tiefer Mensch sein muß, daß man sich nicht verinnerlichen, sondern geradezu sich veräußerlichen muß, um An­hänger des Kopernikanismus zu sein. Und wahrhaftig, es hat ein hoher Grad von Veräußerlichung des menschlichen Gemüts dazu gehört, daß die Menschen solche Sätze finden konnten wie die trivialen, die man in modernen, monistischen Büchern findet, wo man mit einer gewissen Begeisterung sagt: Die Erde, so wie die Menschen sie bewohnen, ist ein Staubkorn im Weltenall den anderen Welten gegenüber. - Das ist eine triviale Tirade, aus dem einfachen Grunde, weil dieses Staubkorn mit allen Einzelheiten die Menschen auf der Erde angeht, und die anderen Dinge, die im Weltall ausgebreitet sind und mit denen die Erde ver­glichen werden soll, gehen den Menschen wenig an. Ganz veräußerlichen",
      "mußte sich die Menschheitsentwickelung, um sozusagen schnell fähig zu werden, den Kopernikanismus anzunehmen.",
      "Was aber muß die Menschheit tun, um sich die Lehre von Reinkar­nation und Karma anzueignen? - Erfolg muß diese Lehre viel schnel­ler haben, wenn die Menschheit nicht ihrem Niedergang entgegen­gehen soll. Aber, was ist notwendig, damit sie sich einnistet in das Kindergemüt?",
      "Veräußerlichung war für den Kopernikanismus notwendig, Ver­innerlichung ist notwendig, um sich einzuleben in die Wahrheiten von Reinkarnation und Karma; ein Ernstnehmen-Können solcher Dinge, wie wir sie gestern besprochen haben, ein Eingehen-Können auf innerliche Seelenerfahrungen, auf Intimitäten des Gemütes, auf solche Dinge, die jede Seele in den tiefen inneren Untergründen des eigenen Wesenskernes erleben muß. Was aus dem Kopernikanismus für die gegenwärtige Kultur erfolgt ist, wird heute überall, in allen populären Mitteilungen dargelegt, und man sieht einen ganz besonde­ren Erfolg darin, daß man dieses alles auch im Bilde, womöglich in kinematographischen Aufnahmen, den Menschen darbieten kann. Schon das charakterisiert die ungeheure Veräußerlichung dieser Kultur.",
      "Man wird wenig zeigen können in Bildern, wird wenig mitteilen können über die Intimitäten jener Wahrheiten, die sich zusammen­fassen in den Worten Reinkarnation und Karma. In der Ausbildung und Verinnerlichung solcher Dinge, wie sie gestern ausgesprochen wor­den sind, liegt es, wie die Menschen darauf kommen werden, daß die Überzeugung von Reinkarnation und Karma begründet ist. So wird der Gegenpol notwendig sein, damit sich die Ideen von Reinkarnation und Karma einleben in die Menschheit, das Gegenteil von dem, was ge­radezu gang und gäbe ist in der gegenwärtigen äußeren Kultur. Daher muß so darauf gedrungen werden, daß diese Verinnerlichung auch wirklich auf anthroposophischem Felde stattfindet. Wenn es auch zwar nicht geleugnet werden soll, daß gewisse schematische Darstellungen für die Erfassung von Grundwahrheiten durch den Verstand nützlich sein können, so muß doch gesagt werden: Das Wichtigste auf anthro­posophischem Felde ist die Hinlenkung auf die in der Tiefe der Seele wirksamen Gesetze, auf dasjenige, was unter den Kräften der Seele",
      "in ähnlicher Art innerlich wirkt, wie die äußeren physischen Gesetze draußen in Zeit- und Raumeswelten wirken.",
      "Aber auch von diesen einzelnen Karmagesetzen verstehen die Men­schen im Grunde genommen heute noch sehr wenig. Das können wir so­zusagen ablesen an Dingen, welche heute immer und immer wiederum von der äußeren Kultur wiederholt werden. Wer würde heute nicht als ein in der äußeren Kultur aufgeklärter Mensch denken, die Mensch­heit sei hinausgekommen über das Kindheitsstadium, in dem sie ge­glaubt hat, und die Menschheit sei eingetreten in das Mannesalter, wo sie wissen kann. Solche Reden werden immer wieder und wiederum vordeklamiert, und vieles geht von solchem aus, was die Menschen draußen betört, was aber die Anthroposophen nimmermehr betören sollte, Redensarten wie jene, daß das Wissen den Glauben ablösen müsse.",
      "Aber alle diese Tiraden von Glauben und Wissen rechnen nicht mit solchen Dingen, die man karmische Zusammenhänge nennen kann im Leben. Wenn derjenige, der imstande ist, okkulte Forschungen anzu­stellen bei besonders gläubigen, hingebungsvoll gläubigen Naturen der Gegenwart, wenn der Umschau hält und sich fragt: Warum ist dieser oder jener Mensch eine besonders gläubige Persönlichkeit? Warum ist die Inbrunst des Glaubens, der Enthusiasmus, warum ist in diesem oder jenem Menschen geradezu ein Genie für religiöse Andacht, für Hinord­nung der Gedanken nach der übersinnlichen Welt? - wenn man sich diese Fragen stellt, dann bekommt man eine merkwürdige Antwort. Geht man zurück bei solchen gläubigen Naturen, bei denen vielleicht der Glaube als wichtige Tatsache ihres Lebens sogar erst im späteren Lebensalter auftritt, zu früheren Inkarnationen, so findet man die merkwürdige Tatsache, daß dies Individualitäten sind, die in früheren, in vorhergehenden Inkarnationen Wissende waren. Das Wissen ihrer vorhergehenden Inkarnation, das rationelle Element der Vernunft der früheren Inkarnation hat sich gerade in das Glaubenselement der ge­genwärtigen Inkarnation verwandelt. Da haben wir eine jener merk­würdigen karmischen Tatsachen, die sich neben eine andere Tatsache so sonderbar hinstellt: Wenn man nun herantritt an Menschen, die als besonders materialistische Menschen nicht mehr glauben, sondern nur",
      "wissen wollen - verzeihen Sie, wenn ich etwas sage, was zwar keinen der Hiersitzenden, wohl aber manchen der Draußenstehenden schok­kieren würde, die nur auf das schwören, nur das anzunehmen erklären, was die Sinne und der an das Gehirn beschränkte Verstand dar-bieten -, so findet man - es ist eine ganze Rätseltatsache - Stumpf-sinn in der vorhergehenden Inkarnation. So daß wirkliche Untersu­chung der verschiedenen Inkarnationen dieses sonderbare Ergebnis liefert, daß gerade enthusiastische Glaubensnaturen, die nicht fanatisch sind, sondern innerlich feststehen in der Hinordnung ihres Wesens zu den höheren Welten, diesen Glauben der Gegenwart aufbauten auf ei­nem Wissen, das sie sich erworben haben in vorhergehenden Inkarna­tionen, während man sich das Wissen auf materialistischer Grundlage durch Stumpfheit gegenüber den Weltanschauungen in früheren Inkar­nationen erworben hat.",
      "Bedenken Sie, wie die ganze Anschauung des Lebens sich ändert, wenn man so den Blick hinausrichtet von dem, was man in der unmit­telbaren Gegenwart erlebt, zu dem, was die menschliche Individualität in ihrem Durchgang durch die verschiedenen Inkarnationen erlebt!",
      "Da nimmt sich manches, worauf der Mensch in der gegenwärtigen Inkarnation stolz ist, sonderbar aus, wenn man es in dem Zusammen­hang betrachtet, in der Art, wie es erworben worden ist in der vorher­gehenden Inkarnation. Wenn man es vom Standpunkt der Reinkarna­tion betrachtet, erscheint manches nicht so unglaublich. Man braucht am Menschen nur ins Auge zu fassen, wie er unter dem Einfluß dieser inneren Seelenkräfte in einer Inkarnation sich entwickelt. Man braucht nur die Seelenkraft des Glaubens zu betrachten, die Seelenkraft, die der Mensch haben kann im Glauben an etwas, was sich als Übersinn­liches hinaushebt über die gewöhnlichen Sinneserscheinungen. Es mag ein moderner materialistischer Monist sich noch so sehr dagegen stem­men, er mag sagen: Nur das Wissen gilt, der Glaube hat kein sicheres Fundament -, ihm gegenüber gilt eine andere Tatsache, die Tatsache, daß gerade das Seelenverhältnis des Glaubens belebend wirkt auf un­seren Astralleib, während die Ungläubigkeit, das Nicht-glauben-Kön­nen den Astralleib ausdörrt, ihn vertrocknen läßt. Wie die Nahrung auf den physischen Leib, so wirkt der Glaube auf den Astralleib. Und",
      "ist es nicht von Wichtigkeit, einzusehen, was der Glaube für den Men­schen, für sein Heil, für seine Seelengesundheit und - weil diese auch das Wirksame für die körperliche Gesundheit ist - für diesen Körper wirkt? Ist es nicht sonderbar, wenn man auf der einen Seite den Glau­ben abschaffen und dem Wissen Platz machen will, und wenn auf der anderen Seite das gilt, daß ein Mensch, der nicht glauben kann, einen ausgetrockneten, verdorrten Astralleib bekommen muß?",
      "Wenn das wirklich ins Auge gefaßt werden soll, so kann das geschehen, wenn man nur das eine Leben betrachtet. Denn, zu erkennen, daß ein glaubens­loser Mensch einen ausgetrockneten Astralleib bekommt, dazu braucht man nicht aufeinanderfolgende Inkarnationen zu überblicken, es ge­nügt, den Menschen in einer Inkarnation zu überblicken.",
      "Wir können also sagen: Glaubenslosigkeit verdorrt unseren Astralleib, wir machen uns arm durch Glaubenslosigkeit; in der nachfolgenden Inkarnation trocknen wir unsere Individualität aus. Wir werden durch die Glau­benslosigkeit stumpf für die nächste Inkarnation und unfähig, ein Wis­sen zu erwerben.",
      "Es ist eine eitle, trockene, nüchterne Logik, wenn man Wissen in Gegensatz bringt zum Glauben. Für denjenigen, der in die Dinge hineinsieht, haben all die Trivialitäten, die über Glauben und Wissen vorgebracht werden, ungefähr die Bedeutung, die eine Diskus­sion hätte zwischen zwei Menschen, von denen der eine behauptete, bis jetzt hätten für die menschliche Fortentwickelung größere Bedeutung die Männer gehabt, der andere sagen würde, die Frauen.",
      "Im Kindheits-zeitalter der Menschheit habe also das eine Geschlecht Bedeutung ge­habt, jetzt aber das andere. Für den Kenner der geistigen Tatsachen ist es klar: So wie im äußeren physischen Leben sich die beiden Geschlech­ter verhalten, so verhalten sich Glauben und Wissen.",
      "Das müssen wir als scharfe und bedeutsame Tatsache ins Auge fassen, und wir sehen damit richtig. Bis so weit geht der Parallelismus, daß wir sagen können:",
      "Wie ein Mensch - wir haben das öfters betont - in den aufeinander­folgenden Inkarnationen das Geschlecht wechselt, so daß er in der Re­gel abwechselnd Mann und Weib ist, so folgt in der Regel auf eine mehr gläubige eine mehr vernunftmäßige Inkarnation, dann wieder eine mehr gläubige und so weiter. Ausnahmen gibt es ja, so daß auch meh­rere männliche oder weibliche Inkarnationen aufeinander folgen können.",
      "Aber die Dinge stehen in der Regel durchaus in gegenseitiger Be­fruchtung und Ergänzung.",
      "Aber noch andere Kräfte der Menschen stehen in einer ähnlichen Ergänzung, zum Beispiel die beiden Seelen fähigkeiten, die wir bezeich­nen wollen als Liebefähigkeit und innere Kraft, so daß im Menschen Selbstgefühl liegt, innere Harmonie, inneres auf Sich-selbst-Gebautsein, und daß wir wissen, was wir zu tun haben im Leben. Auch in dieser Be­ziehung wirkt das menschliche Karma abwechselnd in den verschie­denen Inkarnationen, indem es in einem Menschen in einer Inkarnation mehr ausprägt die hingebungsvolle Liebe für seine Umgebung, eine Art Selbstvergessenheit, eine Art Aufgehen in seiner Umgebung.",
      "Und es wird eine solche Inkarnation abwechseln mit einer Inkarnation, wo der Mensch sich wiederum mehr berufen fühlt, sich nicht zu verlieren an die Außenwelt, sondern sich zu stärken in seinem Inneren, so daß er die Kraft dazu verwendet, um selber weiterzukommen. Natürlich wird dieses letztere nicht ausarten dürfen zu Lieblosigkeit, wie ersteres auch nicht ausarten darf und kann in vollständiges Verlieren des eigenen Selbstes.",
      "Diese zwei Dinge gehören wiederum zusammen. Und es darf durchaus immer wieder betont werden, daß es nicht schon genügt, wenn Anthroposophen ein Opfer bringen wollen. Manche Menschen wollen recht gern und recht viele Opfer bringen - aber um für die Welt taug­liche Opfer zu bringen, muß der Mensch erst die Kraft haben für diese Opfer.",
      "Der Mensch muß erst etwas sein, bevor er sich opfern kann, sonst ist das Opfer der Ichheit nicht besonders viel wert. Es ist auch in gewisser Beziehung eine Art von - wenn auch verhaltenem - Egois­mus, von Bequemlichkeit, wenn man nicht dahin strebt, sich zu vervoll­kommnen, weiterzustreben, damit das, was man leisten kann, auch ein Wertvolles ist.",
      "Es könnte scheinen - aber ich bitte, dies nicht mißzuverstehen -, wie wenn wir die Lieblosigkeit predigten. Es ist so, daß sehr leicht die äußere Welt den Anthroposophen heute vorwirft: Ihr strebt danach, eure Seele zu vervollkommnen, vorwärtszukommen in bezug auf eure Seele! Ihr werdet Egoisten! - Nun muß zugegeben werden, daß viele Schrullen, viele Fehlerhaftigkeiten und Irrtümer in diesem Streben der Menschen nach Vollkommenheit auftreten können. Man braucht",
      "durchaus nicht immer gerade bloß eitel Sympathie zu haben mit dem­jenigen, was sehr häufig unter Anthroposophen auftaucht unter dem Prinzip der Entwickelung. Hinter diesem Streben steckt vielfach aus­serordentlich viel unerlaubter Egoismus.",
      "Auf der anderen Seite muß betont werden, daß wir in einer Zeit leben, in einer Kulturepoche, in der unendlich viel Verschwendung ge­trieben wird gerade mit hingebungsvoller Opferwilligkeit. Wenn auch Lieblosigkeit allerorten vorhanden ist, so ist auch ungeheuer viel Ver­schwendung von Liebe und Opferwilligkeit vorhanden. Das soll nicht mißverstanden werden; aber man soll sich klar darüber sein, daß Liebe, wenn sie nicht mit weiser Führung des Lebens, mit weiser Einsicht in die entsprechenden Verhältnisse auftritt, sehr am unrechten Orte sein kann und so eher zum Schaden als zum Nutzen der Menschen sein kann.",
      "Wir leben in dem Zeitalter, in dem eine große Anzahl von Menschen nötig hat, daß wiederum etwas hereindringt in die Seele, was die Seele vorwärtszubringen vermag, wiederum etwas von dem, was die Anthro­posophie bringt, um ihre Seelen reicher, inhaltsvoller zu machen. Die Menschheit muß für die nächste Inkarnation und auch schon für das Wirken zwischen Tod und neuer Geburt dasjenige anstreben, was Taten sein können, die nicht nur auf altem Herkommen beruhen, sondern was neue Taten sind. Diese Dinge müssen durchaus mit großem Ernst und wahrer Würde betrachtet werden, denn das muß als Tatsache fest­stehen, daß die Anthroposophie eine Mission hat, daß sie wie ein Kul­turkeim ist, der eben in die Zukunft hineinwächst und aufsprießen muß. Wie das aber sich vollzieht im Leben, das können wir am besten einsehen, wenn wir solche karmischen Zusammenhänge, wie Glaube und Vernunft, Liebe und Selbstgefühl ins Auge fassen. Derjenige Mensch, der im Sinne unserer Zeitentwickelung davon überzeugt ist, daß, wenn man durch die Pforte des Todes geht, sich gleich anschließt eine außerirdische Ewigkeit, irgendwo außerhalb dieser Welt, der wird niemals zu wahrer Würdigung des Seelenfortschritts kommen können, denn er wird sich sagen: Wenn ein Fortschritt da ist, so kannst du ihn doch nicht ganz umfassend gestalten als solchen, denn du bist nur vor­übergehend, nur eine kurze Weile in dieser Welt und hast dich nur für die andere Welt vorzubereiten.",
      "Und doch ist es so, daß wir am allerlebensweisesten werden an dem, was wir verfehlt haben. Wir lernen an dem, was wir verfehlt haben. Gerade an dem, was uns nicht gelungen ist, werden wir am allerweise­sten. Und fragen Sie sich ernsthaft, wie oft Sie die Gelegenheit haben, das, was Sie verfehlt haben, genau in derselben Situation wie vorher zu wiederholen? Selten wird sich diese Lage ergeben. Und wäre das Leben nicht etwas höchst Sinnloses, wenn die Lebensweisheit, die wir uns aus den Fehlern aneignen können, für diese irdische Menschheit verloren-ginge? Nur dann, wenn wir wiederum zurückkehren können, wenn wir in einem ganz neuen Leben anwenden können, was wir als Lebens­erfahrung uns in früheren Leben angeeignet haben, nur dann hat das Leben einen Sinn. Daher ist es sinnlos, überhaupt nach Vollkommenheit der Seele zu streben, für dieses Erdendasein sowohl, wenn es als ein­ziges angesehen wird, wie auch für jene außerirdische Ewigkeit.",
      "Und erst recht sinnlos ist es für diejenigen, die nach dem Durchgang durch die Todespforte alles Dasein zu Ende sein lassen. Was für Kräfte, was für Energien und Lebenssicherheit würde es den Menschen geben, wenn sie wüßten, daß sie die Kraft, die scheinbar verlorengeht, in einem neuen Leben verwerten können! Die Kultur der Gegenwart ist deshalb eine solche, wie sie ist, weil außerordentlich wenig für diese Kultur ge­sammelt worden ist in den Inkarnationen, die der Mensch vorher durchgemacht hat. Wahrhaftig, die Seelen sind verarmt in den aufein­anderfolgenden Inkarnationen. Woher kommt es, daß die Seelen ver­armt sind?",
      "Blicken wir zurück auf jene uralten Zeiten, die vor dem Mysterium von Golgatha liegen; da war noch ein altes Hellsehen, da waren noch magische Willenskräfte vorhanden. So war es noch bis in die christliche Zeit hinein. Aber was hereingeragt hat aus den höheren Welten in den letzten Zeiten des alten Hellsehens, das war nur noch das Böse, das Dämonische. Überall sehen wir in den Evangelien angeführt in der Um­gebung des Christus Jesus dämonische Naturen. Was in den alten Zei­ten in den menschlichen Seelen war als ursprünglicher Zusammenhang mit den göttlich-geistigen Kräften und Wesenheiten, das war den See­len verlorengegangen. Dann trat der Christus in die Menschheit herein. Die Menschen, die gegenwärtig leben, haben zwei, drei oder vier Inkar­nationen",
      "seit jenem Zeitpunkt erlebt, je nach ihrem Karma. So wie das Christentum gewirkt hat bis jetzt, so hat es wirken müssen, weil schwache, ausgeleerte Seelen in der Menschheit waren. Es konnte seine innerliche Kraft nicht entfalten, weil schwache Seelen in der Mensch­heitsentwickelung drinnen waren.",
      "Wie das der Fall war, kann man er­messen, wenn man eine andere Welle der Menschheitskultur ins Auge Faßt, nämlich jene Welle, die im Morgenland die Menschheitsentwicke­lung zum Buddhismus geführt hat. Der Buddhismus hat die Überzeu­gung von Reinkarnation und Karma, aber er hat sie so, daß er den Fortgang der Menschheitsentwickelung so betrachtet, als ob er nur die Aufgabe hätte, den Menschen nun so schnell wie möglich aus dem Le­ben herauszubringen.",
      "Im Morgenlande wirkte eine Welle, in der der Drang nach Dasein nicht mehr vorhanden war. Also sehen wir, wie al­les, was den Menschen zur Erdenmission begeistern soll, bestimmen soll, wie alles das gewichen ist bei den Angehörigen derjenigen Kulturwelle, die den Buddhismus trägt.",
      "Und würde der Buddhismus im Abendlande eine besondere Verbreitung gewinnen, so würde dies ein Beweis dafür sein, daß diejenigen Seelen zahlreich sind, die zu den schwächsten, den lebensuntüchtigsten gehören, denn diese wären es, welche ihn annehmen würden. Überall, wo der Buddhismus auftreten könnte in irgendeiner Form im Abendlande, würde das ein Beweis sein dafür, daß die Seelen so schnell wie möglich hinaus wollen aus der Erdenmission, daß sie sich nicht abfinden können mit ihr.",
      "Als das Christentum sich ausbreitete im südlichen Europa und über­nommen wurde von den nördlichen Völkern, da waren diese Völker-seelen stark in ihrer instinktiven Kraft. Sie verleibten sich das Christen­tum ein, aber es konnte zunächst nur seine äußeren Seiten hervorheben, das heißt dasjenige, wofür es besonders wichtig ist, daß der Mensch in der gegenwärtigen Kultur eine Vertiefung des Christus-Impulses er­reichen kann, so daß dieser Christus-Impuls die innerste Kraft der menschlichen Seele selber wird und daher die Seele immer reicher und reicher wird und immer innerlicher und innerlicher, indem sie der Zu­kunft entgegenlebt. Schwächere Inkarnationen haben die menschlichen Seelen durchgemacht; das Christentum hat sie zunächst äußerlich ge­stützt. Jetzt sind die Zeiten gekommen, wo die Seelen innerlich stark",
      "und kräftig werden müssen. Daher wird es im späteren Gang der Zu­kunft wenig ausmachen, was die Seele im äußeren Leben tun wird. Dar­auf aber wird es ankommen, daß sie sich selber findet, daß sie sich verinnerlicht, daß sie Vorstellungen darüber gewinnt, wie man das In­nerliche in das äußere Leben einführt, wie man die Erdenmission durch­ziehen kann mit dem, was man an Bewußtsein, an starker Innerlichkeit gewinnt durch das Durchdrungensein mit den Wahrheiten von Rein­karnation und Karma.",
      "Wenn der Anfang auch nur bescheiden gemacht wird mit dem Ein-dringen der Ideen von Reinkarnation und Karma in das Leben, diese bescheidenen Anfänge sind doch von ungeheurer Wichtigkeit. Je mehr wir dazu kommen, den Menschen sozusagen nach seinen innerlichen Fähigkeiten zu beurteilen, das Leben zu verinnerlichen, desto mehr führen wir das herbei, was der Grundcharakter einer zukünftigen Menschheit sein muß. Das äußere Leben wird immer komplizierter, das läßt sich nicht aufhalten; aber zusammenfinden werden sich die Seelen in der Innerlichkeit. Da mag der einzelne diese oder jene Tätigkeit äußerlich vollbringen, was innerliches Gut der Seele ist, das wird im anthroposophischen Leben die einzelnen Seelen zusammenführen und sie dahin wirken lassen, daß dieses anthroposophische Leben immer mehr auch in die äußere Kultur einzufließen vermag. Wir wissen, daß das gesamte äußere Leben gestärkt wird, wenn die Seele ihre Wirklich­keit findet in der Anthroposophie; deshalb finden sich Menschen aller einzelnen äußeren Lebensrichtungen und aller einzelnen äußeren Le­bensberufe und äußeren Lebenscharaktere zusammen. Die Seele der äußeren Kulturbewegung selber wird geschaffen durch das, was uns in der Anthroposophie entgegentreten kann: Beseelung des äußeren Le­bens. Damit diese eintreten kann, muß zuerst einziehen in die Seele das Bewußtsein von dem wichtigen Karmagesetz. Je mehr wir der Zukunft entgegenleben, um so mehr muß der einzelne in ihm Beseelung des ganzen Lebens fühlen können.",
      "Durch die äußeren Gesetze, die äußeren Einrichtungen wird die äußere Lebensführung so kompliziert werden, daß die Menschen sich nicht mehr auskennen werden. Dagegen wird durch das Durchdrungen­sein mit dem Karmagesetz in die Seele sich einleben das Wissen dessen,",
      "was sie tun soll, um von innen heraus den Weg durch die Welt zu ge­hen. Das wird sie am besten finden da, wo die Dinge durch das innere Seelenleben geregelt sind. Wir haben im Leben solche Dinge, wo es ganz gut vorwärtsgeht, weil jeder dem inneren Trieb folgt, der ihn sicher leitet.",
      "Eine solche Sache ist zum Beispiel das Auf-der-Straße-Gehen. Es ist durchaus noch nicht jedem einzelnen vorgeschrieben, daß er auf diese oder auf die andere Straßenseite ausweichen soll. Und dennoch stoßen nicht jedesmal zwei Menschen, die einander begegnen, zusam­men, weil es eine innere Notwendigkeit gibt, der sie folgen.",
      "Sonst müßte man neben jeden Menschen einen Schutzmann hinstellen, der ihm be­fiehlt, links oder rechts zu gehen. Es ist zwar das Bestreben in einzelnen Kreisen, daß der Mensch immer auf der einen Seite einen Schutzmann, auf der anderen Seite einen Arzt haben soll; das läßt sich ja noch nicht ausführen!",
      "Aber man kommt da am besten vorwärts, wo man seinem ungezwungenen Inneren folgt. Dazu muß dieses hingerichtet sein im menschlichen Zusammenleben auf die menschliche Achtung, muß ins Auge fassen die menschliche Würde.",
      "Und das kann nur geschehen, wenn die Menschen so erfaßt werden, wie sie erfaßt werden können, wenn das Gesetz von Reinkarnation und Karma berücksichtigt wird. Dieses menschliche Zusammenleben wird sich nur dann auf einem höheren Gebiet vollziehen, wenn in die Seele sich einleben wird die Bedeutung dieses Gesetzes von Reinkarnation und Karma.",
      "Das zeigt uns am be­sten eine konkrete Betrachtung wie etwa der Zusammenhang von Glaube, Inbrunst und von Wissen, von Liebe und von Selbstgefühl; das zeigt uns solch eine Betrachtung, wie wir sie gestern angestellt haben.",
      "Nicht umsonst wollte ich solche Vorträge wie den gestrigen und den heutigen vor Ihnen halten. Es handelt sich hierbei nicht so sehr um das, was gesagt wird; das könnte auch anders gesagt werden. Was gestern und heute gesagt worden ist, erscheint nicht in erster Linie von Wichtig­keit. Von Wichtigkeit aber scheint mir das zu sein, daß sich diejenigen, die sich zur Kulturbewegung der Anthroposophie bekennen, so durch­dringen mit den Ideen von Reinkarnation und Karma, daß sie ein Bewußtsein davon bekommen, wie das Leben anders werden muß, wenn das Bewußtsein von Reinkarnation und Karma in jeder Men­schenseele vorhanden sein wird.",
      "Es hat sich eben das gegenwärtige Kulturleben mit Ausschluß des Bewußtseins von Reinkarnation und Karma gebildet. Und das ist das Bedeutsamste, was durch die Anthroposophie eintreten wird, daß diese Dinge jetzt tatsächlich das Leben ergreifen, daß sie die Kultur durch­setzen und dadurch auch im wesentlichen umgestalten werden.",
      "Geradeso wie sich ein heutiger Mensch, der da sagt, Reinkarnation und Karma seien Träumerei, Unsinn, man sehe ja, wie die Menschen geboren werden und wie sie sterben, daß aber etwas herausfliege beim Tode, das sehe man nicht, also brauche man keine Rücksicht darauf zu nehmen -, wie sich ein Mensch, der so spricht, zu dem verhält, der da sagt: Man sieht es nicht herausfliegen, aber man kann diese Gesetze in Rechnung ziehen und wird dann erst alle Lebensvorgänge erklärlich finden, kann gewisse, sonst unerklärliche Dinge erfassen -, so wird sich verhalten die Kultur der Gegenwart zu der der Zukunft, die dann umschließen wird die Gesetze, die Lehre von Reinkarnation und Kar­ma. Und wenn diese beiden bei dem Zustandekommen der gegenwärti­gen Kultur als allgemeine Gedanken der Menschheit keine Rolle ge­spielt haben, bei allen Kulturen der Zukunft werden diese Ideen eine allererste Rolle spielen!",
      "Daß der Anthroposoph fühle, wie er in dieser Weise mitarbeitet an dem Hervorbringen einer neuen Kultur, das muß in seinem Bewußtsein leben. Diese Empfindung, dieses Gefühl von der intensiven Bedeutung von Reinkarnation und Karma für das Leben, dieses würde etwas sein, was heute eine Gruppe von Menschen zusammenhalten könnte, unge­achtet der äußeren Verhältnisse, in denen diese Menschen sind. Die Menschen, die von solcher Gesinnung zusammengehalten werden, kön­nen sich nur durch die Anthroposophie zusammenfinden."
    ],
    "sentences": [
      [
        "Es waren gestern Fragen, die das menschliche Karma berührten, welche wir zur Sprache zu bringen hatten, und zwar wurde versucht, diese Fragen des menschlichen Karmas so zu behandeln, daß sie uns erschei­nen in Anknüpfung an innere Vorgänge der menschlichen Seele; man möchte sagen, daß sie uns erscheinen in Anknüpfung an etwas Erreich­bares.",
        "Denn es wurde darauf aufmerksam gemacht, daß man gewisse Dinge sozusagen probeweise in seinem Seelenleben einrichten könne und daß man dadurch in seinem Seelenleben gewisse innere Erfahrun­gen hervorrufen kann, welche zu einer ganz bestimmt ausgesprochenen Überzeugung von der Wahrheit des Karmagesetzes führen müssen."
      ],
      [
        "Wenn wir solche Fragen immer wieder und wieder in die Gesichtskreise unserer anthroposophischen Betrachtung rücken, so ist dies durchaus nichts irgendwie Willkürliches, sondern es hängt damit zusammen, daß ja immer mehr und mehr wird erkannt werden müssen, wie sich das, was wir Anthroposophie im wahren, echten Sinne des Wortes nennen, zum Leben und zu der ganzen menschlichen Entwickelung verhält.",
        "Man kann sich ja zweifellos eine wenigstens annähernd richtige Vor­stellung davon bilden, wie alles menschliche Lehen nach und nach ver­ändert werden muß, wenn erst eine größere Anzahl von Personen die Überzeugung, die ja zugrunde liegt solch einer Betrachtung wie der gestrigen, zu der ihrigen machen wird."
      ],
      [
        "Das Leben muß sich dadurch, daß die Menschen sich durch die Durchdringung solcher Wahrheiten anders zum Leben stellen, in gewisser Weise ändern.",
        "Und wir kom­men dadurch zu der außerordentlich wichtigen Frage, die eine Ge­wissensfrage sein müßte für diejenigen Persönlichkeiten, die sich der anthroposophischen Bewegung einfügen, wir kommen zu der Frage: Was macht eigentlich einen Menschen der Gegenwart zum Anthropo­sophen?"
      ],
      [
        "Nun ist ja sehr leicht ein Mißverständnis möglich, wenn man diese Frage in einer entsprechenden Weise zu beantworten versucht, denn es verwechseln ja heute noch sehr viele Persönlichkeiten, auch solche Persönlichkeiten,"
      ],
      [
        "die zu uns gehören, die anthroposophische Bewegung mit irgendeiner äußeren Organisation.",
        "Nichts soll gesagt werden gegen eine solche äußere Organisation, die ja in gewisser Beziehung da sein muß, damit auf dem physischen Plane die Pflege der Anthroposophie mög­lich sei; aber wichtig ist es, sich klar darüber zu werden, daß zu einer solchen äußeren Organisation im Grunde genommen alle diejenigen Menschen gehören können, die in ernster, aufrichtiger Weise ein tie­feres Interesse haben an den Fragen des Geisteslebens und die ihre Welt­anschauung im Sinne einer solchen Bewegung des Geisteslebens ver­tiefen wollen.",
        "Damit ist schon gesagt, daß keinerlei Dogma, keinerlei positives Bekenntnis gefordert werden muß von denjenigen, welche sich einer so charakterisierten Organisation anschließen.",
        "Aber ein an­deres ist es, einmal klipp und klar hinzuweisen auf dasjenige, was den modernen Menschen, den Menschen unserer Gegenwart, eigentlich zum Anthroposophen macht."
      ],
      [
        "Die gewöhnliche Überzeugung, daß man es zu tun habe mit einer geistigen Welt, sie ist gewiß der Anfang der anthroposophischen Über­zeugung, und sie muß immer da betont werden, wo man die Anthro­posophie hinausträgt in die Öffentlichkeit und von ihren Aufgaben, ihren Zielen, ihrer gegenwärtigen Mission gegenüber der Öffentlichkeit spricht.",
        "Aber innerhalb der eigentlichen anthroposophischen Kreise muß man sich doch klar werden, daß etwas viel Bestimmteres, viel Aus­gesprocheneres als nur die Überzeugung von einer geistigen Welt den Anthroposophen ausmacht.",
        "Denn schließlich hat man diese Überzeu­gung von einer geistigen Welt immer gehabt in denjenigen Kreisen, die nicht geradezu materialistisch waren.",
        "Das, was den gegenwärtigen Menschen zum Anthroposophen macht, was im Grunde genommen noch nicht in der Theosophie zum Beispiel des Jakob Böhme oder eines anderen Theosophen der Vorzeit enthalten war, ist etwas, worauf die Kultur unseres Abendlandes mit aller Gewalt hingearbeitet hat; auf der einen Seite so, daß geradezu dieses Hinarbeiten zu einer charakte­ristischen Eigenschaft des Strebens vieler Menschen geworden ist.",
        "Und auf der anderen Seite steht dem gegenüber die Tatsache, daß dieses, was so eigenartig den Anthroposophen als solchen charakterisiert, heute noch von der äußeren Kultur, der äußeren menschlichen Bildung"
      ],
      [
        "am allermeisten angefochten wird, als etwas Törichtes angesehen wird."
      ],
      [
        "Gewiß, wir lernen vieles durch die Anthroposophie kennen.",
        "Wir ler­nen kennen die Entwickelung der Menschheit, wir lernen kennen selbst die Entwickelung unserer Erde und unseres Planetensystems.",
        "Alle diese Dinge gehören zu den Grundlagen des anthroposophisch Strebenden.",
        "Aber das hier Gemeinte, besonders Bedeutsame für den Anthropo­sophen der Gegenwart ist das Erringen einer Überzeugung in bezug auf die Fragen von Reinkarnation und Karma.",
        "Und die Art und Weise, wie die Menschen sich aneignen werden diese Überzeugung von Reinkar­nation und Karma, wie sie die Möglichkeit finden werden, den Gedan­ken von Reinkarnation und Karma in das allgemeine Leben überzu­führen, das wird eben dieses moderne Leben von der Gegenwart in die Zukunft hinein im wesentlichen umgestalten.",
        "Es wird ganz neue Le­bensformen, ein ganz neues menschliches Zusammenleben schaffen; ein solches Zusammenleben aber, wie es notwendig ist, wenn die Kultur der Menschheit nicht dem Niedergang verfallen soll, sondern wirklich aufwärtssteigen, vorwärtsgehen soll.",
        "Solche Erwägungen, solche inne­ren Seelenerlebnisse, wie sie gestern hervorgehoben worden sind, kann im Grunde genommen jeder moderne Mensch schon machen; und wenn er nur genügend Energie und Tatkraft hat, so wird er schon zu einer inneren Überzeugung der Wahrheit von Reinkarnation und Karma kommen.",
        "Demjenigen aber, was wahre Anthroposophie eigentlich wollen soll, dem steht gegenüber, man möchte sagen, der ganze äußere Grundcharakter unserer gegenwärtigen Zeit."
      ],
      [
        "Dieser Grundcharakter unserer gegenwärtigen Zeit, er drückt sich vielleicht in keiner Tatsache so radikal charakteristisch aus als darin, daß man immerhin ein mehr oder weniger großes Interesse an den Zen­tralfragen finden kann, die sich auf religiöse Dinge beziehen, die sich beziehen auf die Entwickelung des Menschen und der Welt; auch auf Karma und Reinkarnation.",
        "Man wird mit solchen Fragen auch noch, wenn sie sich erstrecken auf dasjenige, was die einzelnen positiven Leh­ren der einzelnen Religionsbekenntnisse sind - sagen wir in bezug auf die Natur des Buddha oder des Christus -, man wird mit der Be­sprechung solcher Fragen heute immerhin noch ein weites Interesse finden."
      ],
      [
        "Aber dieses Interesse wird wesentlich schwächer, läßt nach; läßt auch bei denjenigen, die sich heute Anthroposophen nennen, recht sehr nach, wenn davon gesprochen wird im einzelnen Konkreten, wie sich Anthroposophie einleben soll in alle Einzelheiten des äußeren Lebens.",
        "Es ist das ja im wesentlichen sehr begreiflich.",
        "Der Mensch steht im äußeren Leben drinnen, der eine hat diese, der andere jene Position in der Welt.",
        "Man möchte sagen, daß so, wie die Welt sich darlebt mit ihren heutigen Ordnungen, es sich fast ausnimmt wie ein großes Etablisse­ment; der einzelne Mensch ist darin wie ein Triebrad.",
        "So fühlt er sich in dieser Welt mit seiner Arbeit, seinen Sorgen, mit dem, was ihn be­schäftigt vom Morgen bis zum Abend, und er weiß nichts anderes, als daß er sich dieser äußeren Weltordnung zu fügen hat."
      ],
      [
        "Daneben tritt dann die Frage auf, die für jede Seele da sein muß, die nur ein wenig aufzublicken vermag von dem, was der Alltag ihr gibt, die Frage nach dem Schicksal der Seele, nach dem Anfang und Ende des Seelenlebens, nach dem Zusammenhang mit den göttlich-geistigen Wesenheiten, nach den Kräften der Welt.",
        "Und zwischen dem, was dem Menschen der Alltag zu geben hat, worüber er Sorge hat und so weiter, und dem, was er auf dem Gebiete der Anthroposophie erhält, tritt ein tiefer Abgrund, eine weite Kluft auf."
      ],
      [
        "Und man möchte sagen: Für die meisten Menschen, und auch für die Anthroposophen der Gegenwart, ist dieses Zusammenstimmen ihrer anthroposophischen Überzeugung mit dem, was sie draußen im alltäglichen Leben tun und vorstellen, fast gar nicht vorhanden.",
        "Man braucht nur irgendeine konkrete Frage in der Öffentlichkeit aufzuwerfen und im geisteswissenschaftlichen, im anthroposophischen Sinn zu behandeln, so wird man gleich sehen, daß das Interesse, welches für die Behandlung allgemeiner religiöser und ähnlicher Fragen noch vorhanden war, für solche konkrete Fragen nicht da ist."
      ],
      [
        "Nun kann man ja nicht verlangen, daß Anthroposophie sich gleich unmittelbar einlebt, daß sie jeder schon in seinen Handgrif­fen zum Ausdruck bringt.",
        "Aber aufmerksam muß darauf gemacht wer­den, daß die anthroposophische Geisteswissenschaft die Mission hat, gerade alles dasjenige ins Leben einzuführen, dem Leben einzuverlei­ben, was aus einer Seele folgen muß, welche sich nach und nach die Überzeugung verschafft, daß die Ideen von Reinkarnation und Karma"
      ],
      [
        "Realitäten sind.",
        "So könnte geradezu hingestellt werden als charakte­ristisches Kennzeichen des gegenwärtigen Anthroposophen, daß er auf dem Wege ist, sich eine begründete innere Überzeugung vom Walten der Idee von Reinkarnation und Karma anzueignen.",
        "Alles Übrige, möchte man sagen, ergibt sich daraus dann schon von selber als unmit­telbare Konsequenz, als Folgeerscheinung."
      ],
      [
        "Das kann natürlich auch nicht so gehen, daß nun jeder etwa denkt, mit dem, was ich aus Reinkarnation und Karma gewinne, werde ich jetzt unmittelbar das äußere Leben anfassen.",
        "Das geht natürlich nicht.",
        "Aber Vorstellungen muß man davon gewinnen, wie Reinkarnation und Karma sich in das äußere Leben hineinfinden müssen, so daß sie zu dirigierenden Mächten des äußeren Lebens werden können."
      ],
      [
        "Nehmen wir einmal die Idee des Karma, wie das Karma wirkt durch die verschiedenen Verkörperungen des Menschen hindurch.",
        "Da müssen wir, wenn ein Mensch hereintritt in die Welt, seine Fähigkeiten und Kräfte letzten Endes ansehen als das Ergebnis der Ursachen, die er sel­ber in früheren Verkörperungen gelegt hat.",
        "Wir müssen, wenn wir konse­quent diese Idee durchführen, wirklich jeden Menschen als eine Art von innerem Rätsel behandeln, als etwas, aus dem sich herausarbeiten muß dasjenige, was in den dunklen Untergründen seiner früheren Inkarna­tionen schwebt.",
        "Nicht nur in der Erziehung, sondern im ganzen Leben wird ein ganz bedeutsamer Umschwung herbeigeführt, wenn Ernst ge­macht wird mit einer solchen Idee vom Karma.",
        "Und es würde, wenn das eingesehen würde, die Idee vom Karma aus einer bloß theoretischen Idee umgewandelt in etwas, was wirklich in das praktische Leben eingreifen muß, was wirklich eine praktische Sache des Lebens werden könnte."
      ],
      [
        "Alles äußere Leben, so wie es sich uns heute darbietet, ist aber überall ein Bild eines solchen menschlichen Zusammenhanges, der geformt und gebildet worden ist mit Ausschluß, ja mit Verleugnung der Idee von Reinkarnation und Karma.",
        "Und gleichsam, als ob man verschütten wollte alle Möglichkeiten, daß die Menschen durch die eigene Seelenentwickelung darauf kommen könnten, daß es Reinkarnation und Kar­ma gibt, so ist dieses äußere Leben heute eingerichtet.",
        "In der Tat, es gibt zum Beispiel nichts, was so sehr feindlich gesinnt ist einer wirklichen Überzeugung von Reinkarnation und Karma als der Grundsatz des"
      ],
      [
        "Lebens, daß man für dasjenige, was man unmittelbar als Arbeit leistet, einen der Arbeit entsprechenden Lohn, der die Arbeit geradezu bezahlt, einheimsen müsse.",
        "Nicht wahr, eine solche Rede klingt sonderbar, recht sonderbar!",
        "Nun müssen Sie die Sache auch nicht so betrachten, als wenn die Anthroposophie nun gleich radikal die Grundsätze einer Lebenspraxis über den Haufen werfen und über Nacht eine neue Lebensord­nung einführen wollte.",
        "Das kann nicht sein.",
        "Aber der Gedanke müßte den Menschen nahetreten, daß in der Tat in einer Weltordnung, in der man daran denkt, Lohn und Arbeit müßten sich unmittelbar ent­sprechen, in der man sozusagen durch seine Arbeit dasjenige verdienen muß, was zum Leben notwendig ist, niemals eine wirkliche Grundüber­zeugung von Reinkarnation und Karma gedeihen kann.",
        "Selbstverständ­lich muß die bestehende Lebensordnung zunächst so bleiben, denn ge­rade der Anthroposoph muß einsehen, daß das, was besteht, wiederum durch die Karmaordnung hervorgerufen worden ist, und daß es in die­ser Beziehung zu Recht und mit Notwendigkeit besteht.",
        "Aber er muß durchaus die Möglichkeit haben zu begreifen, daß sich wie ein neuer Keim innerhalb des Organismus unserer Weltordnung dasjenige ent­wickelt, was aus der Anerkennung der Idee von Reinkarnation und Karma folgen kann und muß."
      ],
      [
        "Vor allen Dingen folgt aus der Idee des Karma, daß wir nicht durch einen Zufall - das geht gerade aus der gestrigen Betrachtung hervor, wie ich glaube - uns hereingestellt fühlen sollen in die Weltordnung, nicht durch Zufall uns hingestellt fühlen sollen auf den Posten, auf dem wir uns befinden im Leben, sondern daß diesem Hingestelltsein gleich­sam eine Art von unterbewußtem Willensentschluß zugrunde liegt; daß wir gewissermaßen, bevor wir in dieses irdische Dasein getreten sind, in das wir uns herausgearbeitet haben aus der geistigen Welt zwischen Tod und Geburt, als Ergebnis unserer früheren Inkarnationen in der geistigen Welt den Willensentschluß gefaßt haben - den wir nur wie­der vergessen haben, als wir uns in den Körper einlebten -, uns hinzu­stellen an den Platz, an dem wir stehen.",
        "So daß das Ergebnis eines vor­geburtlichen, vorirdischen eigenen Willensentschlusses uns an unseren Lebensplatz hinstellt und uns ausstattet gerade mit der Neigung für diejenigen Schicksalsschläge, die uns treffen.",
        "Wenn der Mensch dann"
      ],
      [
        "zu der Überzeugung kommt von der Wahrheit des Karmagesetzes, kann es nicht ausbleiben, daß er in gewisser Beziehung beginnt, Neigung, ja vielleicht sogar Liebe zu haben für den Posten der Welt, auf den er sich gestellt hat, welcher Art dieser Posten auch sein mag."
      ],
      [
        "Nun können Sie allerdings sagen: Ja, du sprichst ganz merkwürdige Worte, sonderbare, merkwürdige Worte!",
        "Bei Dichtern, Schriftstellern, bei anderen geistig wirkenden Menschen mag dies ja gehen.",
        "Da hast du dann, wenn du zu diesen sprichst, gut predigen, daß sie Freude, Liebe, Hingebung haben sollen für den Posten, auf dem sie im Leben stehen.",
        "Aber wie ist es denn mit all denjenigen Menschen, welche auf Lebensposten stehen, die wahrhaftig zunächst nicht geeignet sind, mit ihrem Inhalt, ihren Tätigkeiten auf den Menschen sonderlich sympathisch zu wirken, die geeignet sind, in den Menschenseelen die Empfindung her­vorzurufen, daß man zu den vernachlässigten, den vom Leben unter­jochten Persönlichkeiten gehört? - Wer möchte leugnen, daß ein großer Teil der gegenwärtigen Kulturbestrebungen darauf hinausgeht, fort­während Verbesserungen in unser Leben einzuführen, die sozusagen Abhilfe schaffen können jenem Unzufriedensein mit einem so unsym­pathischen Hineingestelltsein in das Leben.",
        "Wie vielgestaltige Partei­ungen, wie viele sektiererische Bestrebungen gibt es, die sozusagen das Leben nach allen Richtungen so verbessern wollen, daß auch in äußer­licher Beziehung eintreten könnte eine Art von Erträglichkeit des ge­samten Erdenlebens der Menschheit."
      ],
      [
        "Aber alle diese Bestrebungen rechnen nicht mit dem einen, damit nämlich, daß die Art von Unbefriedigtsein, die für viele Menschen ge­rade heute aus dem Leben fließen muß, in vielfacher Beziehung zusam­menhängt mit dem ganzen Gang der Menschheitsentwickelung, daß im Grunde genommen durch die Art und Weise, wie sich die Menschen in der Vorzeit entwickelt haben, sie zu einem solchen Karma gekom­men sind, und daß aus dem Zusammenwirken dieser verschiedenen Karmen der heutige Zustand der menschlichen Kulturentwickelung mit Notwendigkeit hervorgegangen ist.",
        "Und wenn wir diesen Zustand der Kultur charakterisieren wollen, müssen wir sagen, er erweist sich im höchsten Grade als kompliziert.",
        "Wir müssen auch sagen, daß das, was der Mensch tut, was er ausführt, immer weniger zusammenhängt"
      ],
      [
        "mit dem, was der Mensch liebt.",
        "Und wenn man heute die Menschen abzählen würde, die eine von ihnen ungeliebte Betätigung in ihrer äußeren Lebensposition vollbringen müssen, ihre Zahl würde wahrhaftig weit größer sein als die Zahl derjenigen, die sich dazu bekennen: Ich kann nicht anders sagen, als daß ich meine äußere Betätigung liebe, daß sie mich glücklich und zufrieden macht!"
      ],
      [
        "Erst vor kurzem hörte ich, wie ein Mensch zu einer befreundeten Persönlichkeit merkwürdige Worte sprach.",
        "Er meinte: Überblicke ich mein Leben mit allen Einzelheiten, so muß ich sagen, wenn ich dieses Leben im gegenwärtigen Augenblicke wiederum von Kindheit an be­ginnen sollte und es gerade so durchleben könnte, wie ich es haben möchte, ich würde das gleiche wiederum tun, was ich bis jetzt getan habe. - Da antwortete die befreundete Persönlichkeit: Dann gehören Sie zu den Menschen, die in der Gegenwart am wenigsten zu finden sind. - Wahrscheinlich hat diese Persönlichkeit in bezug auf die mei­sten Menschen der Gegenwart recht."
      ],
      [
        "Es gibt nicht viele Zeitgenossen, die den Ausspruch fällen, sie würden, wenn es auf sie ankäme, das Le­ben mit all dem, was es an Freude, an Schmerz, an Schicksalsschlägen, an Hemmnissen gebracht hat, sogleich wiederum beginnen und wären ganz zufrieden, wenn es ihnen wiederum genau dasselbe bieten würde.",
        "Man kann nicht sagen, daß diese Tatsache, die angeführt worden ist, nämlich daß es so wenig Menschen gibt in der Gegenwart, die sozusagen ihr gegenwärtiges Karma wiederum aufnehmen würden mit allen Ein­zelheiten, nicht zusammenhänge mit alledem, was der heutige Kulturzustand der Menschheit gebracht hat."
      ],
      [
        "Unser Leben ist komplizierter geworden, aber es ist so geworden, wie es ist, durch die verschieden­artigen Karmen der einzelnen heute auf der Erde lebenden Persönlich­keiten.",
        "Das ist ganz zweifellos.",
        "Für denjenigen, der nur ein wenig hineinsieht in den Gang der Menschheitsentwickelung, liegt die Sache gar nicht so, daß wir etwa in der Zukunft einem Leben entgegengehen könnten, das weniger kompliziert wäre."
      ],
      [
        "Im Gegenteil, das Leben wird immer komplizierter und komplizierter werden!",
        "Das äußere Leben wird immer komplizierter, und wenn in Zukunft noch so viele Tätig­keiten dem Menschen abgenommen werden durch die Maschinen."
      ],
      [
        "Le­ben, welche die Menschen in dieser physischen Inkarnation beseligen,"
      ],
      [
        "wird es in sehr geringem Umfang geben können, wenn nicht ganz an­dere Verhältnisse eintreten als jene, die sich wirksam erweisen in unserer Kultur.",
        "Und diese anderen Verhältnisse müssen die sein, die sich ergeben aus dem Durchdrungensein der Menschenseele mit der Wahrheit von Reinkarnation und Karma."
      ],
      [
        "Durch diese Wahrheit wird man erkennen, daß mit der Komplika­tion der äußeren Kultur etwas noch ganz anderes parallel gehen wird.",
        "Was wird notwendig sein, damit die Menschen immer mehr und mehr durchdrungen werden von der Wahrheit von Reinkarnation und Kar­ma?",
        "Was wird notwendig sein, damit der Begriff von Reinkarnation und Karma, wie es durchaus sein muß, wenn unsere Kultur nicht einen Niedergang erfahren soll, in verhältnismäßig ganz kurzer Zeit so in unsere Schulbildung hineinwirkt, daß er die Menschen schon in ihrer Kindheit ergreift, wie heute die Überzeugung von der Richtigkeit des kopernikanischen Weltsystems schon das Kind ergreift?"
      ],
      [
        "Was war notwendig, damit das kopernikanische Weltsystem die Seelen ergriffen hat? - Mit diesem kopernikanischen Weltsystem ist es eine ganz eigentümliche Sache.",
        "Ich will nicht über das kopernikanische Weltsystem sprechen, sondern nur über sein In-die-Welt-Treten.",
        "Be­denken Sie doch nur einmal, daß dieses kopernikanische Weltsystem ausgedacht worden ist von einem christlichen Domherrn, und daß Kopernikus so über dieses Weltsystem denken konnte, daß er sein Werk, in dem er dieses Weltsystem ausgebaut hatte, dem Papst gewidmet hat.",
        "Er konnte glauben, daß es ganz im Sinne des Christentums sei, was er ausgedacht hatte.",
        "Gab es damals einen Beweis für den Kopernikanis­mus?",
        "Konnte jemand das beweisen, was Kopernikus ausgedacht hatte?",
        "Niemand konnte den Kopernikanismus beweisen.",
        "Und dennoch, be­denken Sie die Schnelligkeit, mit der er eingezogen ist in die Mensch­heit!",
        "Seit wann kann man ihn erst beweisen?",
        "Einigermaßen sicher erst, soweit er richtig ist, seit den fünfzigerjahren des 19.",
        "Jahrhunderts, erst seit dem Foucaultschen Pendelversuch.",
        "Es gab früher keinen Beweis dafür, daß die Erde sich dreht.",
        "Es ist ein Unsinn, wenn behauptet wird, daß Kopernikus alles das, was er als Hypothese aufgestellt und ein­gesehen hat, auch hat beweisen können; das gilt auch hinsichtlich der Behauptung, daß die Erde sich um ihre Achse dreht."
      ],
      [
        "Erst seit man darauf gekommen ist, daß das schwingende Polpendel das Bestreben hat, seine Schwingungsebene auch gegenüber der Um­drehung der Erde beizubehalten, und daß, wenn man ein langes Pendel schwingen läßt, sich dessen Schwingungsrichtung in bezug auf die Erd­oberfläche dreht, konnte man den Schluß ziehen: es muß sich die Erde unter dem Pendel weggedreht haben.",
        "Dieser Versuch, der eigentlich erst ein wirklicher Beweis dafür ist, daß die Erde sich bewegt, der wurde erst im 19.",
        "Jahrhundert gemacht.",
        "Früher gab es keine Möglichkeit, den Kopernikanismus als etwas anderes denn als eine Hypothese anzu­sehen.",
        "Dennoch hat er so gewirkt auf die Natur der menschlichen Seele der neueren Zeit, daß, während Kopernikus zwar geglaubt hat, daß er sein Werk dem Papst widmen dürfe, es bis zum Jahre 1822 auf dem Index stand.",
        "Erst im Jahre 1822 wurde das Werk, auf dem der Koper­nikanismus aufgebaut ist, abgesetzt vom Index.",
        "Es wurde also abge­setzt, bevor es einen richtigen Beweis für die Anschauung des Koperni­kus gab.",
        "Die Kraft des Impulses, mit dem sich das kopernikanische Weltsystem in die menschliche Seele einlebte, dieser Kopernikanismus selbst zwang die Kirche, ihn als etwas anzuerkennen, was nicht etwas Ketzerisches ist."
      ],
      [
        "Es ist mir immer im tiefsten Sinne charakteristisch erschienen, daß mir diese Erkenntnis von der Erdbewegung, als ich ein kleiner Bub war, in der Schule zuerst von einem Pfarrer, nicht von einem Lehrer vorgetragen worden ist.",
        "Und wer will daran zweifeln, daß der Koper­nikanismus sich eingenistet hat, daß er sich bis in das Kindergemüt eingenistet hat? - Wir wollen aber jetzt nicht von seinen Wahrheiten und seinen Irrtümern sprechen."
      ],
      [
        "So muß sich einnisten - aber dazu hat die Menschheit nicht so lange Zeit wie zur Aufnahme des Kopernikanismus -, wenn nicht die Menschheitskultur einen Niedergang erfahren will, die Wahrheit von Reinkarnation und Karma.",
        "Und jene, die sich heute Anthroposophen nennen, sind dazu berufen, das ihrige zu tun, daß die Wahrheit von Reinkarnation und Karma sich bis in das Kindergemüt hinein ergießt.",
        "Damit ist natürlich nicht gesagt, daß jetzt jene Anthroposophen, die Kinder haben, nun ihren Kindern dieses als ein Dogma beibringen.",
        "Ein­sicht in diese Dinge muß man haben."
      ],
      [
        "Ich habe nicht umsonst den Kopernikanismus angeführt.",
        "An dem, was dem Kopernikanismus seinen Erfolg gebracht hat, können wir lernen, was dem Reinkarnations- und dem Karmagedanken seine Kul­turerfolge bringen kann.",
        "Was gehörte denn dazu, daß der Kopernika­nismus sich so schnell verbreitete? - Ich werde jetzt etwas furchtbar Ketzerisches aussprechen, etwas geradezu Greuliches für den modernen Menschen.",
        "Aber es handelt sich eben darum, daß Anthroposophie von den Anthroposophen ebenso ernst und bedeutsam aufgefaßt werde, wie einmal das Christentum bei seinem ersten Entstehen von den ersten Christen aufgefaßt worden ist, die sich auch in Gegensatz gebracht haben zu dem, was da war.",
        "Wenn Anthroposophie nicht so ernst ge­nommen wird von ihren Bekennern, so kann sie nicht für die Mensch­heit leisten, was geleistet werden muß."
      ],
      [
        "Also ich muß etwas Greuliches sagen, und das besteht darin: Der Kopernikanismus, dasjenige, was die Menschen heute lernen als koper­nikanisches Weltsystem, dem wahrhaftig nicht sein großes Verdienst und damit seine Bedeutung als Kulturtatsache allerersten Ranges ab­gesprochen werden soll, konnte sich einnisten in die menschliche Seele dadurch, daß man ein oberflächlicher Mensch sein konnte, um ein An­hänger dieses Systems zu sein.",
        "Oberflächlichkeit und Äußerlichkeit ge­hörten dazu, um sich vom Kopernikanismus schneller zu überzeugen.",
        "Damit ist nicht gesagt, daß die Bedeutung des Kopernikus für die Menschheit herabgemindert werden soll.",
        "Nein; aber gesagt kann wer­den, daß man kein sehr tiefer Mensch sein muß, daß man sich nicht verinnerlichen, sondern geradezu sich veräußerlichen muß, um An­hänger des Kopernikanismus zu sein.",
        "Und wahrhaftig, es hat ein hoher Grad von Veräußerlichung des menschlichen Gemüts dazu gehört, daß die Menschen solche Sätze finden konnten wie die trivialen, die man in modernen, monistischen Büchern findet, wo man mit einer gewissen Begeisterung sagt: Die Erde, so wie die Menschen sie bewohnen, ist ein Staubkorn im Weltenall den anderen Welten gegenüber. - Das ist eine triviale Tirade, aus dem einfachen Grunde, weil dieses Staubkorn mit allen Einzelheiten die Menschen auf der Erde angeht, und die anderen Dinge, die im Weltall ausgebreitet sind und mit denen die Erde ver­glichen werden soll, gehen den Menschen wenig an.",
        "Ganz veräußerlichen"
      ],
      [
        "mußte sich die Menschheitsentwickelung, um sozusagen schnell fähig zu werden, den Kopernikanismus anzunehmen."
      ],
      [
        "Was aber muß die Menschheit tun, um sich die Lehre von Reinkar­nation und Karma anzueignen? - Erfolg muß diese Lehre viel schnel­ler haben, wenn die Menschheit nicht ihrem Niedergang entgegen­gehen soll.",
        "Aber, was ist notwendig, damit sie sich einnistet in das Kindergemüt?"
      ],
      [
        "Veräußerlichung war für den Kopernikanismus notwendig, Ver­innerlichung ist notwendig, um sich einzuleben in die Wahrheiten von Reinkarnation und Karma; ein Ernstnehmen-Können solcher Dinge, wie wir sie gestern besprochen haben, ein Eingehen-Können auf innerliche Seelenerfahrungen, auf Intimitäten des Gemütes, auf solche Dinge, die jede Seele in den tiefen inneren Untergründen des eigenen Wesenskernes erleben muß.",
        "Was aus dem Kopernikanismus für die gegenwärtige Kultur erfolgt ist, wird heute überall, in allen populären Mitteilungen dargelegt, und man sieht einen ganz besonde­ren Erfolg darin, daß man dieses alles auch im Bilde, womöglich in kinematographischen Aufnahmen, den Menschen darbieten kann.",
        "Schon das charakterisiert die ungeheure Veräußerlichung dieser Kultur."
      ],
      [
        "Man wird wenig zeigen können in Bildern, wird wenig mitteilen können über die Intimitäten jener Wahrheiten, die sich zusammen­fassen in den Worten Reinkarnation und Karma.",
        "In der Ausbildung und Verinnerlichung solcher Dinge, wie sie gestern ausgesprochen wor­den sind, liegt es, wie die Menschen darauf kommen werden, daß die Überzeugung von Reinkarnation und Karma begründet ist.",
        "So wird der Gegenpol notwendig sein, damit sich die Ideen von Reinkarnation und Karma einleben in die Menschheit, das Gegenteil von dem, was ge­radezu gang und gäbe ist in der gegenwärtigen äußeren Kultur.",
        "Daher muß so darauf gedrungen werden, daß diese Verinnerlichung auch wirklich auf anthroposophischem Felde stattfindet.",
        "Wenn es auch zwar nicht geleugnet werden soll, daß gewisse schematische Darstellungen für die Erfassung von Grundwahrheiten durch den Verstand nützlich sein können, so muß doch gesagt werden: Das Wichtigste auf anthro­posophischem Felde ist die Hinlenkung auf die in der Tiefe der Seele wirksamen Gesetze, auf dasjenige, was unter den Kräften der Seele"
      ],
      [
        "in ähnlicher Art innerlich wirkt, wie die äußeren physischen Gesetze draußen in Zeit- und Raumeswelten wirken."
      ],
      [
        "Aber auch von diesen einzelnen Karmagesetzen verstehen die Men­schen im Grunde genommen heute noch sehr wenig.",
        "Das können wir so­zusagen ablesen an Dingen, welche heute immer und immer wiederum von der äußeren Kultur wiederholt werden.",
        "Wer würde heute nicht als ein in der äußeren Kultur aufgeklärter Mensch denken, die Mensch­heit sei hinausgekommen über das Kindheitsstadium, in dem sie ge­glaubt hat, und die Menschheit sei eingetreten in das Mannesalter, wo sie wissen kann.",
        "Solche Reden werden immer wieder und wiederum vordeklamiert, und vieles geht von solchem aus, was die Menschen draußen betört, was aber die Anthroposophen nimmermehr betören sollte, Redensarten wie jene, daß das Wissen den Glauben ablösen müsse."
      ],
      [
        "Aber alle diese Tiraden von Glauben und Wissen rechnen nicht mit solchen Dingen, die man karmische Zusammenhänge nennen kann im Leben.",
        "Wenn derjenige, der imstande ist, okkulte Forschungen anzu­stellen bei besonders gläubigen, hingebungsvoll gläubigen Naturen der Gegenwart, wenn der Umschau hält und sich fragt: Warum ist dieser oder jener Mensch eine besonders gläubige Persönlichkeit?",
        "Warum ist die Inbrunst des Glaubens, der Enthusiasmus, warum ist in diesem oder jenem Menschen geradezu ein Genie für religiöse Andacht, für Hinord­nung der Gedanken nach der übersinnlichen Welt? - wenn man sich diese Fragen stellt, dann bekommt man eine merkwürdige Antwort.",
        "Geht man zurück bei solchen gläubigen Naturen, bei denen vielleicht der Glaube als wichtige Tatsache ihres Lebens sogar erst im späteren Lebensalter auftritt, zu früheren Inkarnationen, so findet man die merkwürdige Tatsache, daß dies Individualitäten sind, die in früheren, in vorhergehenden Inkarnationen Wissende waren.",
        "Das Wissen ihrer vorhergehenden Inkarnation, das rationelle Element der Vernunft der früheren Inkarnation hat sich gerade in das Glaubenselement der ge­genwärtigen Inkarnation verwandelt.",
        "Da haben wir eine jener merk­würdigen karmischen Tatsachen, die sich neben eine andere Tatsache so sonderbar hinstellt: Wenn man nun herantritt an Menschen, die als besonders materialistische Menschen nicht mehr glauben, sondern nur"
      ],
      [
        "wissen wollen - verzeihen Sie, wenn ich etwas sage, was zwar keinen der Hiersitzenden, wohl aber manchen der Draußenstehenden schok­kieren würde, die nur auf das schwören, nur das anzunehmen erklären, was die Sinne und der an das Gehirn beschränkte Verstand dar-bieten -, so findet man - es ist eine ganze Rätseltatsache - Stumpf-sinn in der vorhergehenden Inkarnation.",
        "So daß wirkliche Untersu­chung der verschiedenen Inkarnationen dieses sonderbare Ergebnis liefert, daß gerade enthusiastische Glaubensnaturen, die nicht fanatisch sind, sondern innerlich feststehen in der Hinordnung ihres Wesens zu den höheren Welten, diesen Glauben der Gegenwart aufbauten auf ei­nem Wissen, das sie sich erworben haben in vorhergehenden Inkarna­tionen, während man sich das Wissen auf materialistischer Grundlage durch Stumpfheit gegenüber den Weltanschauungen in früheren Inkar­nationen erworben hat."
      ],
      [
        "Bedenken Sie, wie die ganze Anschauung des Lebens sich ändert, wenn man so den Blick hinausrichtet von dem, was man in der unmit­telbaren Gegenwart erlebt, zu dem, was die menschliche Individualität in ihrem Durchgang durch die verschiedenen Inkarnationen erlebt!"
      ],
      [
        "Da nimmt sich manches, worauf der Mensch in der gegenwärtigen Inkarnation stolz ist, sonderbar aus, wenn man es in dem Zusammen­hang betrachtet, in der Art, wie es erworben worden ist in der vorher­gehenden Inkarnation.",
        "Wenn man es vom Standpunkt der Reinkarna­tion betrachtet, erscheint manches nicht so unglaublich.",
        "Man braucht am Menschen nur ins Auge zu fassen, wie er unter dem Einfluß dieser inneren Seelenkräfte in einer Inkarnation sich entwickelt.",
        "Man braucht nur die Seelenkraft des Glaubens zu betrachten, die Seelenkraft, die der Mensch haben kann im Glauben an etwas, was sich als Übersinn­liches hinaushebt über die gewöhnlichen Sinneserscheinungen.",
        "Es mag ein moderner materialistischer Monist sich noch so sehr dagegen stem­men, er mag sagen: Nur das Wissen gilt, der Glaube hat kein sicheres Fundament -, ihm gegenüber gilt eine andere Tatsache, die Tatsache, daß gerade das Seelenverhältnis des Glaubens belebend wirkt auf un­seren Astralleib, während die Ungläubigkeit, das Nicht-glauben-Kön­nen den Astralleib ausdörrt, ihn vertrocknen läßt.",
        "Wie die Nahrung auf den physischen Leib, so wirkt der Glaube auf den Astralleib."
      ],
      [
        "ist es nicht von Wichtigkeit, einzusehen, was der Glaube für den Men­schen, für sein Heil, für seine Seelengesundheit und - weil diese auch das Wirksame für die körperliche Gesundheit ist - für diesen Körper wirkt?",
        "Ist es nicht sonderbar, wenn man auf der einen Seite den Glau­ben abschaffen und dem Wissen Platz machen will, und wenn auf der anderen Seite das gilt, daß ein Mensch, der nicht glauben kann, einen ausgetrockneten, verdorrten Astralleib bekommen muß?"
      ],
      [
        "Wenn das wirklich ins Auge gefaßt werden soll, so kann das geschehen, wenn man nur das eine Leben betrachtet.",
        "Denn, zu erkennen, daß ein glaubens­loser Mensch einen ausgetrockneten Astralleib bekommt, dazu braucht man nicht aufeinanderfolgende Inkarnationen zu überblicken, es ge­nügt, den Menschen in einer Inkarnation zu überblicken."
      ],
      [
        "Wir können also sagen: Glaubenslosigkeit verdorrt unseren Astralleib, wir machen uns arm durch Glaubenslosigkeit; in der nachfolgenden Inkarnation trocknen wir unsere Individualität aus.",
        "Wir werden durch die Glau­benslosigkeit stumpf für die nächste Inkarnation und unfähig, ein Wis­sen zu erwerben."
      ],
      [
        "Es ist eine eitle, trockene, nüchterne Logik, wenn man Wissen in Gegensatz bringt zum Glauben.",
        "Für denjenigen, der in die Dinge hineinsieht, haben all die Trivialitäten, die über Glauben und Wissen vorgebracht werden, ungefähr die Bedeutung, die eine Diskus­sion hätte zwischen zwei Menschen, von denen der eine behauptete, bis jetzt hätten für die menschliche Fortentwickelung größere Bedeutung die Männer gehabt, der andere sagen würde, die Frauen."
      ],
      [
        "Im Kindheits-zeitalter der Menschheit habe also das eine Geschlecht Bedeutung ge­habt, jetzt aber das andere.",
        "Für den Kenner der geistigen Tatsachen ist es klar: So wie im äußeren physischen Leben sich die beiden Geschlech­ter verhalten, so verhalten sich Glauben und Wissen."
      ],
      [
        "Das müssen wir als scharfe und bedeutsame Tatsache ins Auge fassen, und wir sehen damit richtig.",
        "Bis so weit geht der Parallelismus, daß wir sagen können:"
      ],
      [
        "Wie ein Mensch - wir haben das öfters betont - in den aufeinander­folgenden Inkarnationen das Geschlecht wechselt, so daß er in der Re­gel abwechselnd Mann und Weib ist, so folgt in der Regel auf eine mehr gläubige eine mehr vernunftmäßige Inkarnation, dann wieder eine mehr gläubige und so weiter.",
        "Ausnahmen gibt es ja, so daß auch meh­rere männliche oder weibliche Inkarnationen aufeinander folgen können."
      ],
      [
        "Aber die Dinge stehen in der Regel durchaus in gegenseitiger Be­fruchtung und Ergänzung."
      ],
      [
        "Aber noch andere Kräfte der Menschen stehen in einer ähnlichen Ergänzung, zum Beispiel die beiden Seelen fähigkeiten, die wir bezeich­nen wollen als Liebefähigkeit und innere Kraft, so daß im Menschen Selbstgefühl liegt, innere Harmonie, inneres auf Sich-selbst-Gebautsein, und daß wir wissen, was wir zu tun haben im Leben.",
        "Auch in dieser Be­ziehung wirkt das menschliche Karma abwechselnd in den verschie­denen Inkarnationen, indem es in einem Menschen in einer Inkarnation mehr ausprägt die hingebungsvolle Liebe für seine Umgebung, eine Art Selbstvergessenheit, eine Art Aufgehen in seiner Umgebung."
      ],
      [
        "Und es wird eine solche Inkarnation abwechseln mit einer Inkarnation, wo der Mensch sich wiederum mehr berufen fühlt, sich nicht zu verlieren an die Außenwelt, sondern sich zu stärken in seinem Inneren, so daß er die Kraft dazu verwendet, um selber weiterzukommen.",
        "Natürlich wird dieses letztere nicht ausarten dürfen zu Lieblosigkeit, wie ersteres auch nicht ausarten darf und kann in vollständiges Verlieren des eigenen Selbstes."
      ],
      [
        "Diese zwei Dinge gehören wiederum zusammen.",
        "Und es darf durchaus immer wieder betont werden, daß es nicht schon genügt, wenn Anthroposophen ein Opfer bringen wollen.",
        "Manche Menschen wollen recht gern und recht viele Opfer bringen - aber um für die Welt taug­liche Opfer zu bringen, muß der Mensch erst die Kraft haben für diese Opfer."
      ],
      [
        "Der Mensch muß erst etwas sein, bevor er sich opfern kann, sonst ist das Opfer der Ichheit nicht besonders viel wert.",
        "Es ist auch in gewisser Beziehung eine Art von - wenn auch verhaltenem - Egois­mus, von Bequemlichkeit, wenn man nicht dahin strebt, sich zu vervoll­kommnen, weiterzustreben, damit das, was man leisten kann, auch ein Wertvolles ist."
      ],
      [
        "Es könnte scheinen - aber ich bitte, dies nicht mißzuverstehen -, wie wenn wir die Lieblosigkeit predigten.",
        "Es ist so, daß sehr leicht die äußere Welt den Anthroposophen heute vorwirft: Ihr strebt danach, eure Seele zu vervollkommnen, vorwärtszukommen in bezug auf eure Seele!",
        "Ihr werdet Egoisten! - Nun muß zugegeben werden, daß viele Schrullen, viele Fehlerhaftigkeiten und Irrtümer in diesem Streben der Menschen nach Vollkommenheit auftreten können.",
        "Man braucht"
      ],
      [
        "durchaus nicht immer gerade bloß eitel Sympathie zu haben mit dem­jenigen, was sehr häufig unter Anthroposophen auftaucht unter dem Prinzip der Entwickelung.",
        "Hinter diesem Streben steckt vielfach aus­serordentlich viel unerlaubter Egoismus."
      ],
      [
        "Auf der anderen Seite muß betont werden, daß wir in einer Zeit leben, in einer Kulturepoche, in der unendlich viel Verschwendung ge­trieben wird gerade mit hingebungsvoller Opferwilligkeit.",
        "Wenn auch Lieblosigkeit allerorten vorhanden ist, so ist auch ungeheuer viel Ver­schwendung von Liebe und Opferwilligkeit vorhanden.",
        "Das soll nicht mißverstanden werden; aber man soll sich klar darüber sein, daß Liebe, wenn sie nicht mit weiser Führung des Lebens, mit weiser Einsicht in die entsprechenden Verhältnisse auftritt, sehr am unrechten Orte sein kann und so eher zum Schaden als zum Nutzen der Menschen sein kann."
      ],
      [
        "Wir leben in dem Zeitalter, in dem eine große Anzahl von Menschen nötig hat, daß wiederum etwas hereindringt in die Seele, was die Seele vorwärtszubringen vermag, wiederum etwas von dem, was die Anthro­posophie bringt, um ihre Seelen reicher, inhaltsvoller zu machen.",
        "Die Menschheit muß für die nächste Inkarnation und auch schon für das Wirken zwischen Tod und neuer Geburt dasjenige anstreben, was Taten sein können, die nicht nur auf altem Herkommen beruhen, sondern was neue Taten sind.",
        "Diese Dinge müssen durchaus mit großem Ernst und wahrer Würde betrachtet werden, denn das muß als Tatsache fest­stehen, daß die Anthroposophie eine Mission hat, daß sie wie ein Kul­turkeim ist, der eben in die Zukunft hineinwächst und aufsprießen muß.",
        "Wie das aber sich vollzieht im Leben, das können wir am besten einsehen, wenn wir solche karmischen Zusammenhänge, wie Glaube und Vernunft, Liebe und Selbstgefühl ins Auge fassen.",
        "Derjenige Mensch, der im Sinne unserer Zeitentwickelung davon überzeugt ist, daß, wenn man durch die Pforte des Todes geht, sich gleich anschließt eine außerirdische Ewigkeit, irgendwo außerhalb dieser Welt, der wird niemals zu wahrer Würdigung des Seelenfortschritts kommen können, denn er wird sich sagen: Wenn ein Fortschritt da ist, so kannst du ihn doch nicht ganz umfassend gestalten als solchen, denn du bist nur vor­übergehend, nur eine kurze Weile in dieser Welt und hast dich nur für die andere Welt vorzubereiten."
      ],
      [
        "Und doch ist es so, daß wir am allerlebensweisesten werden an dem, was wir verfehlt haben.",
        "Wir lernen an dem, was wir verfehlt haben.",
        "Gerade an dem, was uns nicht gelungen ist, werden wir am allerweise­sten.",
        "Und fragen Sie sich ernsthaft, wie oft Sie die Gelegenheit haben, das, was Sie verfehlt haben, genau in derselben Situation wie vorher zu wiederholen?",
        "Selten wird sich diese Lage ergeben.",
        "Und wäre das Leben nicht etwas höchst Sinnloses, wenn die Lebensweisheit, die wir uns aus den Fehlern aneignen können, für diese irdische Menschheit verloren-ginge?",
        "Nur dann, wenn wir wiederum zurückkehren können, wenn wir in einem ganz neuen Leben anwenden können, was wir als Lebens­erfahrung uns in früheren Leben angeeignet haben, nur dann hat das Leben einen Sinn.",
        "Daher ist es sinnlos, überhaupt nach Vollkommenheit der Seele zu streben, für dieses Erdendasein sowohl, wenn es als ein­ziges angesehen wird, wie auch für jene außerirdische Ewigkeit."
      ],
      [
        "Und erst recht sinnlos ist es für diejenigen, die nach dem Durchgang durch die Todespforte alles Dasein zu Ende sein lassen.",
        "Was für Kräfte, was für Energien und Lebenssicherheit würde es den Menschen geben, wenn sie wüßten, daß sie die Kraft, die scheinbar verlorengeht, in einem neuen Leben verwerten können!",
        "Die Kultur der Gegenwart ist deshalb eine solche, wie sie ist, weil außerordentlich wenig für diese Kultur ge­sammelt worden ist in den Inkarnationen, die der Mensch vorher durchgemacht hat.",
        "Wahrhaftig, die Seelen sind verarmt in den aufein­anderfolgenden Inkarnationen.",
        "Woher kommt es, daß die Seelen ver­armt sind?"
      ],
      [
        "Blicken wir zurück auf jene uralten Zeiten, die vor dem Mysterium von Golgatha liegen; da war noch ein altes Hellsehen, da waren noch magische Willenskräfte vorhanden.",
        "So war es noch bis in die christliche Zeit hinein.",
        "Aber was hereingeragt hat aus den höheren Welten in den letzten Zeiten des alten Hellsehens, das war nur noch das Böse, das Dämonische.",
        "Überall sehen wir in den Evangelien angeführt in der Um­gebung des Christus Jesus dämonische Naturen.",
        "Was in den alten Zei­ten in den menschlichen Seelen war als ursprünglicher Zusammenhang mit den göttlich-geistigen Kräften und Wesenheiten, das war den See­len verlorengegangen.",
        "Dann trat der Christus in die Menschheit herein.",
        "Die Menschen, die gegenwärtig leben, haben zwei, drei oder vier Inkar­nationen"
      ],
      [
        "seit jenem Zeitpunkt erlebt, je nach ihrem Karma.",
        "So wie das Christentum gewirkt hat bis jetzt, so hat es wirken müssen, weil schwache, ausgeleerte Seelen in der Menschheit waren.",
        "Es konnte seine innerliche Kraft nicht entfalten, weil schwache Seelen in der Mensch­heitsentwickelung drinnen waren."
      ],
      [
        "Wie das der Fall war, kann man er­messen, wenn man eine andere Welle der Menschheitskultur ins Auge Faßt, nämlich jene Welle, die im Morgenland die Menschheitsentwicke­lung zum Buddhismus geführt hat.",
        "Der Buddhismus hat die Überzeu­gung von Reinkarnation und Karma, aber er hat sie so, daß er den Fortgang der Menschheitsentwickelung so betrachtet, als ob er nur die Aufgabe hätte, den Menschen nun so schnell wie möglich aus dem Le­ben herauszubringen."
      ],
      [
        "Im Morgenlande wirkte eine Welle, in der der Drang nach Dasein nicht mehr vorhanden war.",
        "Also sehen wir, wie al­les, was den Menschen zur Erdenmission begeistern soll, bestimmen soll, wie alles das gewichen ist bei den Angehörigen derjenigen Kulturwelle, die den Buddhismus trägt."
      ],
      [
        "Und würde der Buddhismus im Abendlande eine besondere Verbreitung gewinnen, so würde dies ein Beweis dafür sein, daß diejenigen Seelen zahlreich sind, die zu den schwächsten, den lebensuntüchtigsten gehören, denn diese wären es, welche ihn annehmen würden.",
        "Überall, wo der Buddhismus auftreten könnte in irgendeiner Form im Abendlande, würde das ein Beweis sein dafür, daß die Seelen so schnell wie möglich hinaus wollen aus der Erdenmission, daß sie sich nicht abfinden können mit ihr."
      ],
      [
        "Als das Christentum sich ausbreitete im südlichen Europa und über­nommen wurde von den nördlichen Völkern, da waren diese Völker-seelen stark in ihrer instinktiven Kraft.",
        "Sie verleibten sich das Christen­tum ein, aber es konnte zunächst nur seine äußeren Seiten hervorheben, das heißt dasjenige, wofür es besonders wichtig ist, daß der Mensch in der gegenwärtigen Kultur eine Vertiefung des Christus-Impulses er­reichen kann, so daß dieser Christus-Impuls die innerste Kraft der menschlichen Seele selber wird und daher die Seele immer reicher und reicher wird und immer innerlicher und innerlicher, indem sie der Zu­kunft entgegenlebt.",
        "Schwächere Inkarnationen haben die menschlichen Seelen durchgemacht; das Christentum hat sie zunächst äußerlich ge­stützt.",
        "Jetzt sind die Zeiten gekommen, wo die Seelen innerlich stark"
      ],
      [
        "und kräftig werden müssen.",
        "Daher wird es im späteren Gang der Zu­kunft wenig ausmachen, was die Seele im äußeren Leben tun wird.",
        "Dar­auf aber wird es ankommen, daß sie sich selber findet, daß sie sich verinnerlicht, daß sie Vorstellungen darüber gewinnt, wie man das In­nerliche in das äußere Leben einführt, wie man die Erdenmission durch­ziehen kann mit dem, was man an Bewußtsein, an starker Innerlichkeit gewinnt durch das Durchdrungensein mit den Wahrheiten von Rein­karnation und Karma."
      ],
      [
        "Wenn der Anfang auch nur bescheiden gemacht wird mit dem Ein-dringen der Ideen von Reinkarnation und Karma in das Leben, diese bescheidenen Anfänge sind doch von ungeheurer Wichtigkeit.",
        "Je mehr wir dazu kommen, den Menschen sozusagen nach seinen innerlichen Fähigkeiten zu beurteilen, das Leben zu verinnerlichen, desto mehr führen wir das herbei, was der Grundcharakter einer zukünftigen Menschheit sein muß.",
        "Das äußere Leben wird immer komplizierter, das läßt sich nicht aufhalten; aber zusammenfinden werden sich die Seelen in der Innerlichkeit.",
        "Da mag der einzelne diese oder jene Tätigkeit äußerlich vollbringen, was innerliches Gut der Seele ist, das wird im anthroposophischen Leben die einzelnen Seelen zusammenführen und sie dahin wirken lassen, daß dieses anthroposophische Leben immer mehr auch in die äußere Kultur einzufließen vermag.",
        "Wir wissen, daß das gesamte äußere Leben gestärkt wird, wenn die Seele ihre Wirklich­keit findet in der Anthroposophie; deshalb finden sich Menschen aller einzelnen äußeren Lebensrichtungen und aller einzelnen äußeren Le­bensberufe und äußeren Lebenscharaktere zusammen.",
        "Die Seele der äußeren Kulturbewegung selber wird geschaffen durch das, was uns in der Anthroposophie entgegentreten kann: Beseelung des äußeren Le­bens.",
        "Damit diese eintreten kann, muß zuerst einziehen in die Seele das Bewußtsein von dem wichtigen Karmagesetz.",
        "Je mehr wir der Zukunft entgegenleben, um so mehr muß der einzelne in ihm Beseelung des ganzen Lebens fühlen können."
      ],
      [
        "Durch die äußeren Gesetze, die äußeren Einrichtungen wird die äußere Lebensführung so kompliziert werden, daß die Menschen sich nicht mehr auskennen werden.",
        "Dagegen wird durch das Durchdrungen­sein mit dem Karmagesetz in die Seele sich einleben das Wissen dessen,"
      ],
      [
        "was sie tun soll, um von innen heraus den Weg durch die Welt zu ge­hen.",
        "Das wird sie am besten finden da, wo die Dinge durch das innere Seelenleben geregelt sind.",
        "Wir haben im Leben solche Dinge, wo es ganz gut vorwärtsgeht, weil jeder dem inneren Trieb folgt, der ihn sicher leitet."
      ],
      [
        "Eine solche Sache ist zum Beispiel das Auf-der-Straße-Gehen.",
        "Es ist durchaus noch nicht jedem einzelnen vorgeschrieben, daß er auf diese oder auf die andere Straßenseite ausweichen soll.",
        "Und dennoch stoßen nicht jedesmal zwei Menschen, die einander begegnen, zusam­men, weil es eine innere Notwendigkeit gibt, der sie folgen."
      ],
      [
        "Sonst müßte man neben jeden Menschen einen Schutzmann hinstellen, der ihm be­fiehlt, links oder rechts zu gehen.",
        "Es ist zwar das Bestreben in einzelnen Kreisen, daß der Mensch immer auf der einen Seite einen Schutzmann, auf der anderen Seite einen Arzt haben soll; das läßt sich ja noch nicht ausführen!"
      ],
      [
        "Aber man kommt da am besten vorwärts, wo man seinem ungezwungenen Inneren folgt.",
        "Dazu muß dieses hingerichtet sein im menschlichen Zusammenleben auf die menschliche Achtung, muß ins Auge fassen die menschliche Würde."
      ],
      [
        "Und das kann nur geschehen, wenn die Menschen so erfaßt werden, wie sie erfaßt werden können, wenn das Gesetz von Reinkarnation und Karma berücksichtigt wird.",
        "Dieses menschliche Zusammenleben wird sich nur dann auf einem höheren Gebiet vollziehen, wenn in die Seele sich einleben wird die Bedeutung dieses Gesetzes von Reinkarnation und Karma."
      ],
      [
        "Das zeigt uns am be­sten eine konkrete Betrachtung wie etwa der Zusammenhang von Glaube, Inbrunst und von Wissen, von Liebe und von Selbstgefühl; das zeigt uns solch eine Betrachtung, wie wir sie gestern angestellt haben."
      ],
      [
        "Nicht umsonst wollte ich solche Vorträge wie den gestrigen und den heutigen vor Ihnen halten.",
        "Es handelt sich hierbei nicht so sehr um das, was gesagt wird; das könnte auch anders gesagt werden.",
        "Was gestern und heute gesagt worden ist, erscheint nicht in erster Linie von Wichtig­keit.",
        "Von Wichtigkeit aber scheint mir das zu sein, daß sich diejenigen, die sich zur Kulturbewegung der Anthroposophie bekennen, so durch­dringen mit den Ideen von Reinkarnation und Karma, daß sie ein Bewußtsein davon bekommen, wie das Leben anders werden muß, wenn das Bewußtsein von Reinkarnation und Karma in jeder Men­schenseele vorhanden sein wird."
      ],
      [
        "Es hat sich eben das gegenwärtige Kulturleben mit Ausschluß des Bewußtseins von Reinkarnation und Karma gebildet.",
        "Und das ist das Bedeutsamste, was durch die Anthroposophie eintreten wird, daß diese Dinge jetzt tatsächlich das Leben ergreifen, daß sie die Kultur durch­setzen und dadurch auch im wesentlichen umgestalten werden."
      ],
      [
        "Geradeso wie sich ein heutiger Mensch, der da sagt, Reinkarnation und Karma seien Träumerei, Unsinn, man sehe ja, wie die Menschen geboren werden und wie sie sterben, daß aber etwas herausfliege beim Tode, das sehe man nicht, also brauche man keine Rücksicht darauf zu nehmen -, wie sich ein Mensch, der so spricht, zu dem verhält, der da sagt: Man sieht es nicht herausfliegen, aber man kann diese Gesetze in Rechnung ziehen und wird dann erst alle Lebensvorgänge erklärlich finden, kann gewisse, sonst unerklärliche Dinge erfassen -, so wird sich verhalten die Kultur der Gegenwart zu der der Zukunft, die dann umschließen wird die Gesetze, die Lehre von Reinkarnation und Kar­ma.",
        "Und wenn diese beiden bei dem Zustandekommen der gegenwärti­gen Kultur als allgemeine Gedanken der Menschheit keine Rolle ge­spielt haben, bei allen Kulturen der Zukunft werden diese Ideen eine allererste Rolle spielen!"
      ],
      [
        "Daß der Anthroposoph fühle, wie er in dieser Weise mitarbeitet an dem Hervorbringen einer neuen Kultur, das muß in seinem Bewußtsein leben.",
        "Diese Empfindung, dieses Gefühl von der intensiven Bedeutung von Reinkarnation und Karma für das Leben, dieses würde etwas sein, was heute eine Gruppe von Menschen zusammenhalten könnte, unge­achtet der äußeren Verhältnisse, in denen diese Menschen sind.",
        "Die Menschen, die von solcher Gesinnung zusammengehalten werden, kön­nen sich nur durch die Anthroposophie zusammenfinden."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG Berlin, 5.März 1912",
    "paragraphs": [
      "Wir haben hier an dieser Stelle jahrelang anthroposophische Wahrhei­ten betrachtet, anthroposophische Erkenntnisse. Wir haben versucht, uns dem, was wir glauben Anthroposophie nennen zu müssen, von den verschiedensten Richtungen her zu nähern und in uns dasjenige aufzu­nehmen, was aus den anthroposophischen Erkenntnissen heraus kom­men kann. Es wird sich nun empfehlen, einmal gerade im Verlaufe der Betrachtungen, die wir zuletzt hier angestellt haben und noch anstellen werden, die Frage aufzuwerfen, was den Menschen der Gegenwart, den Menschen unserer Zeit die Anthroposophie überhaupt eigentlich geben soll und geben kann? Was sie enthält, von dem wissen wir ja durch unsere Betrachtungen ein gut Stück, und wir können daher auf Grundlage der Bekanntschaft mit einigen anthroposophischen Wahr­heiten an die Frage herantreten: Was kann die Anthroposophie den Menschen der Gegenwart geben?",
      "Wenn wir an diese Frage herantreten, müssen wir vor allen Dingen darauf bedacht sein, das anthroposophische Leben, die anthroposo­phische Bewegung - in unseren Gedanken wenigstens - scharf zu trennen von irgendeiner gesellschaftlichen Einrichtung, von irgend etwas, das man mit dem Namen Anthroposophische Gesellschaft be­legen könnte. In der Wirklichkeit wird ja das ganze gegenwärtige Le­ben selbstverständlich immer wieder und wieder notwendig machen, daß sich diejenigen, die Anthroposophie treiben wollen, in gesellschaft­licher Art vereinigen. Aber wenn diese Vereinigung notwendig ist, so ist sie eben mehr notwendig durch das ganze außerhalb der Anthropo­sophie stehende gegenwärtige Leben, als etwa durch den Inhalt und durch Gesinnung oder durch sonst irgend etwas innerhalb der Anthro­posophie selber. Anthroposophie an sich könnte heute durchaus so ver­kündet werden, wie irgend etwas anderes gegenwärtig unter den Men­schen verkündet wird. Anthroposophie als solche könnte - denkbar wäre das durchaus - so verkündet werden, wie etwa Chemie heute unter den Menschen verkündet wird, und es könnten die Menschen zu",
      "den anthroposophischen Wahrheiten herankommen, wie sie an Chemie oder Mathematik herankommen. Was dann für die Seele des einzelnen daraus folgt, wie die Seele des einzelnen die Anthroposophie aufnimmt und zum Impuls des Lebens macht, das könnte dann eben Sache eines jeden einzelnen sein.",
      "Eine Anthroposophische Gesellschaft oder irgend­eine Vereinigung, um Anthroposophie zu treiben, macht der Umstand, die Tatsache notwendig, daß Anthroposophie als solche etwas ist, was als etwas völlig Neues, als eine völlig neue Erkenntnis in unsere Gegen-wart hereintritt und aufgenommen werden soll von dem geistigen Le­ben, während die Menschen draußen im außeranthroposophischen Le­ben eigentlich durchaus nicht nur, sagen wir, die allgemeine Seelen-verfassung der Gegenwart brauchen, um Anthroposophie auf sich wirken zu lassen, sondern auch zu dieser gewöhnlichen Seelenverfas­sung, wie sie die Menschen heute haben, eine besondere Vorbereitung des Gemütes, des Herzens brauchen. Und eine solche Vorbereitung des Gemütes und des Herzens kann nur angeeignet werden durch das Zusammenleben in unseren anthroposophischen Zweigen oder anthro­posophischen Verbindungen oder dergleichen.",
      "Da eignen wir uns eine gewisse Art des Denkens, eine gewisse Art des Fühlens an, so daß wir dadurch in die Lage kommen, Dinge ernsthaft zu betrachten, welche die Menschen, die heute draußen in der Welt stehen und kaum etwas von Anthroposophie gehört haben, ganz selbstverständlich und begreiflicherweise vielleicht sogar als tolle Phantastereien ansehen müssen.",
      "Gewiß, es könnte eingewendet werden, Anthroposophie würde auch verbreitet durch öffentliche Vorträge, welche da zu ganz unvorberei­teten Menschen sprechen. Aber gerade die, welche im engeren Sinne gesellschaftsmäßig unseren Kreisen angehören, werden wissen, daß der ganze Ton und die ganze Art und Weise der Haltung eines anthropo­sophischen Vortrages anders sein muß, wenn er vor einem unvorbe­reiteten Publikum gehalten wird, als vor denjenigen, zu denen man so sprechen kann, daß sie durch den Drang ihres Herzens, durch die ganze Art und Weise ihrer inneren Gesinnung das ernst nehmen, was das große Publikum noch nicht ernstnehmen könnte. Und dies, was jetzt angedeutet worden ist, wird in der nächsten Zukunft nicht etwa besser",
      "werden - davon kann gar keine Rede sein -, sondern es wird in der nächsten Zukunft immer stärker und schärfer hervortreten. Die äußere Gegnerschaft gegen alles Anthroposophische wird immer größer und größer werden in der Welt, und zwar aus dem Grunde, weil gerade Anthroposophie in unserer Gegenwart etwas im höchsten Grade Zeit­gemäßes, etwas im höchsten Grade Notwendiges ist, und weil gegen das Allernotwendigste, gegen das Allerzeitgemäßeste die Auflehnung der Menschen im Grunde genommen immer am allerstärksten ist.",
      "Nun könnte die Frage entstehen: Warum denn das? Warum ist die Auflehnung der Menschenherzen irgendeines Zeitalters am allerstärk­sten gegen das, was dieses Zeitalter am allernotwendigsten braucht? -Das ist etwas, was der Anthroposoph sollte begreifen können, was aber zu schwierig ist, um es vor einem unvorbereiteten Publikum auch nur im allerentferntesten klarzumachen.",
      "Der Anthroposoph weiß, daß es luziferische Kräfte und Wesenheiten gibt, die hinter der allgemeinen Evolution zurückgeblieben sind. Die wirken durch die Menschenherzen, durch die Menschenseelen, und sie haben das allergrößte Interesse daran, in den Zeiten, in welchen das Streben nach aufwärts am größten wird, ihre Attacken, ihre Angriffe am allerstärksten zu machen. Weil nun die Auflehnung der Menschen-herzen gegen das, was vorwärtsstrebt in der Menschheitsentwickelung, von den luziferischen Kräften herrührt, und weil diese ihre Attacken dann unternehmen werden, wenn es ihnen sozusagen an den Kragen geht, deshalb müssen diese Attacken - also auch die Auflehnung der Menschenherzen - in solchen Zeiten am allerstärksten sein. Daher werden wir verstehen, daß die für die Menschheit bedeutsamsten Wahr­heiten sich von jeher dadurch eingelebt haben in die Menschheitsent­wickelung, daß sie mit dem Umstande rechnen mußten, daß sie die stärksten Widerstände finden. Etwas, was sich nicht sehr unterscheidet von dem, was sonst auch vorkommt in der Welt, wird kaum starke Widerstände finden. Aber, was deshalb in die Welt tritt, weil die Menschheit seit langem darnach dürstet und es nicht empfangen hat, das ist zugleich das, was die stärksten Attacken der luziferischen Kräfte herausfordert. Und so ist eine Gesellschaft eigentlich nichts weiter als ein Schutzwall gegen dieses ganze, aber begreiflich charakterisierte Verhalten",
      "der Außenwelt. Man muß etwas haben, innerhalb dessen man diese Dinge so vertreten kann, daß man sagen kann: Diejenigen, zu denen man spricht, oder mit denen man zusammen ist, sie bringen der Sache ein gewisses Verständnis entgegen, und die anderen, welche sich nicht vereinigt haben mit denen, die davon sprechen, die geht es nichts an. - Von dem, was in der Öffentlichkeit vertreten wird, glauben alle Menschen, daß es sie etwas angeht, und daß sie ein Urteil darüber ab­zugeben haben, natürlich gestachelt von den luziferischen Kräften. Daraus ersehen wir, daß es zwar notwendig ist, Anthroposophie zu treiben, daß aber Anthroposophie etwas hereinbringt in unsere Gegen­wart, was hereinkommen muß und verlangt wird von dem geistigen Durste und dem geistigen Nahrungsbedürfnis unserer Zeit, und was unter allen Umständen hereinkommen wird auf irgendeine Art. Denn dafür, daß es hereinkommt, dafür sorgen die geistigen Mächte, die sich der Evolution gewidmet haben.",
      "Daher können wir im rein anthroposophischen Sinne die Frage auf­werfen: Worin liegen die wichtigsten Dinge, die gegenwärtig der Menschheit eingepflanzt werden sollen durch die Anthroposophie? Es werden diejenigen sein, nach denen die gegenwärtige Menschheit ganz besonders dürstet, die am allernotwendigsten sind. Gerade mit der Be­antwortung einer solchen Frage kann man am allermeisten mißver­standen werden. Deshalb ist es so notwendig, für die Gedanken zu-nächst Anthroposophie und Anthroposophische Gesellschaft zu tren­nen. Denn, was die Anthroposophie der Menschheit bringen soll, sind neue Erkenntnisse, neue Wahrheiten. Aber eine Gesellschaft kann nie­mals - und am allerwenigsten in unserer Zeit - auf irgendwelche besonderen Wahrheiten eingeschworen werden. Die Frage wäre die allerunsinnigste: Welchen Glauben habt ihr Anthroposophen? - Un­sinnig ist sie dann, wenn man unter «Anthroposophen> einen Menschen meint, der zur Anthroposophischen Gesellschaft gehört; denn man würde dabei voraussetzen, daß eine ganze Gesellschaft eine gemein­same Überzeugung, ein gemeinsames Dogma haben würde. Das kann nicht sein. In dem Augenblick, wo eine ganze Gesellschaft - statuten-gemäß - auf ein gemeinsames Dogma schwören müßte, hörte sie auf eine Gesellschaft zu sein, und es würde die Sektiererei beginnen. Hier",
      "haben wir die Grenze, wo eine Gesellschaft aufhört, eine Gesellschaft zu sein. In dem Augenblick, wo ein Mensch verpflichtet würde, eine von der Gesellschaft geforderte Überzeugung zu haben, hätte man es mit einer Sektiererei zu tun. Daher kann eine Gesellschaft, welche sich dem widmet, was jetzt charakterisiert worden ist, dies nur unter dem Gesichtspunkte sein, daß sie es ist unter dem naturgemäßen geistigen Drange. Man kann fragen: Welche Menschen kommen herbei, um über Anthroposophie etwas zu hören? - Und man wird sagen können: Es sind die, welche irgend etwas über geistige Dinge hören wollen, die einen Drang haben, über geistige Dinge etwas zu hören. - Dieser Drang ist kein Dogma. Denn wenn jemand etwas sucht, wovon er nicht sagt, ich werde dieses oder jenes finden, sondern wo er, wenn er sucht, !; eben sucht, so ist dieses Suchen das Gemeinsame, was eine Gesellschaft,",
      "die nicht eine Sekte werden will, haben muß. Aber ganz unabhängig davon ist die Frage: Was bringt nun die Anthroposophie als solche der Menschheit? - Und man muß sagen: Die Anthroposophie als solche bringt der Menschheit etwas, was ähnlich, nur geistiger und in bezug auf das menschliche Gemüt tiefer und bedeutungsvoller ist, als alle großen geistigen Wahrheiten gewesen sind, welche je der Menschheit gebracht worden sind.",
      "Nun gibt es unter den Dingen, die wir im Verlaufe unserer Betrach­tungen an uns haben herantreten lassen, manche, von denen man sagen kann: sie sind so, daß sie eigentlich nicht als die bedeutsamen, als die bezeichnenden angegeben werden können, wenn von dem die Rede ist, was eigentlich die gegenwärtige Menschheit als Neues erhalten soll. Aber fundamentale Dinge sind es, fundamentale Wahrheiten, die wirk­lich als neu in die Menschheit hereintreten. Und wir brauchen nicht sehr weit zu gehen, um zu charakterisieren, worin eigentlich das Neue der anthroposophischen Bewegung liegt. Es liegt darin, daß die zwei Wahrheiten, die sozusagen zu unseren fundamentalsten Dingen ge­hören, an die Menschenseele in einer immer überzeugenderen Weise herantreten: die beiden Wahrheiten von Reinkarnation und Karma. Man kann sagen: Was der Anthroposoph in erster Linie auf seinem Wege findet, wenn er heute ernstlich strebt, das ist die Notwendigkeit der Erkenntnis von Reinkarnation und Karma. Wir können zum Beispiel",
      "nicht sagen, daß in der abendländischen Kultur gewisse Dinge, wie etwa die Möglichkeit, in höhere Welten sich zu erheben, durch die Anthroposophie als etwas fundamental Neues auftritt; denn wer die abendländische Entwickelung kennt, wer da weiß, ich will nur sagen, daß es Mystiker gegeben hat, selbst solche Mystiker, wie Jakob Böhme oder Swedenborg oder wie die ganze Jakob Böhmesche Schule, der weiß auch, daß das eine - wenn es auch vielfach strittig war - immer ge­glaubt worden ist, daß es immer da war als Ansicht: daß sich der Mensch aus der gewöhnlichen Sinneswelt zu höheren Welten erheben kann; so daß dies also nicht das fundamental Neue ist. Weiter sind auch gewisse andere Dinge nicht das fundamental Neue.",
      "Selbst wenn wir über das sprechen, was in bezug auf die Evolution fundamental ist; wenn wir zum Beispiel sprechen über die Christus-Frage: in bezug auf die anthroposophische Bewegung als solche ist sie nicht das Fundamen­talste; sondern das Fundamentalste ist die Gestalt, welche die Christus-Frage dadurch erhält, daß Reinkarnation und Karma in die Herzen der Menschen als Wahrheiten aufgenommen werden. Die Beleuchtung, welche die Christus-Frage erhält unter der Voraussetzung der Wahr­heiten von Reinkarnation und Karma, das ist das Wesentliche.",
      "Denn die Christus-Frage hat das Abendland in wahrhaftig tiefer Weise zu den verschiedensten Zeiten beschäftigt. Wir können dabei erinnern an die Zeiten der Gnosis, können erinnern an die Zeiten, in welchen sich vertieft hat das esoterische Christentum zum Beispiel derjenigen, die im Zeichen des Grals oder des Rosenkreuzes sich zusammengefunden ha­ben, wie sie vertieft haben die Christus-Frage.",
      "Also das ist nicht das Fundamentale. Fundamental, wesentlich wird die Frage für die abend-ländischen Gemüter, für die Erkenntnis und religiösen Bedürfnisse nur durch die Wahrheiten von Reinkarnation und Karma, so daß der, welcher eine Erweiterung seines Gemütes erfährt durch die Erkenntnis von Reinkarnation und Karma, auch notwendigerweise fordert eine neue Erkenntnis alter Fragen. - Was die Erkenntnis von Reinkarna­tion und Karma betrifft, so müssen wir das gerade Gegenteil davon sagen.",
      "Wir können höchstens darauf aufmerksam machen, daß Rein­karnation und Karma, man könnte sagen, sich schüchtern hereinfinden in die abendländische Kultur zur Zeit Lessings, der in seiner «Erziehung",
      "des Menschengeschlechts» darauf kommt. Wir finden dann auch wei­tere Beispiele, wie tiefere Geister auf diese Frage kommen. Aber daß Reinkarnation und Karma als ein Bestandteil des menschlichen Be-wußtseins sich geltend machen, daß sie aufgenommen werden in Herz und Gemüt des Menschen so, wie es durch die Anthroposophie ge­schieht, das ist eben etwas, was erst in unserer Gegenwart wirklich ge­schehen kann. Daher könnte man sagen: Das Verhältnis eines Menschen der Gegenwart zur Anthroposophie charakterisiert sich darin, daß er in die Lage kommen kann, aus irgendwelchen Voraussetzungen heraus Reinkarnation und Karma als Erkenntnisse in sich aufzunehmen. Das ist das Wesentliche, worum es sich handelt. Im Grunde genommen folgt alles übrige dann in einer mehr oder weniger selbstverständlichen Weise daraus, ob sich der Mensch zu Reinkarnation und Karma in der ent­sprechenden Weise zu stellen vermag.",
      "Nun müssen wir uns, wenn wir die Frage so ins Auge fassen, auch klar werden, was es für die abendländische Menschheit und für die Menschheit überhaupt bedeutet, wenn Reinkarnation und Karma Er­kenntnisse werden, die sozusagen übergehen in die Alltäglichkeit, wie andere Wahrheiten in die Alltäglichkeit übergegangen sind. In einem noch viel größeren Umfange müssen in der nächsten Zeit Reinkarnation und Karma in das Bewußtsein der Menschheit übergehen, als dies zum Beispiel die kopernikanische Weltanschauung getan hat. In bezug auf die letztere brauchen wir uns nur einmal recht klarzumachen, wie sie eigentlich mit einem raschen Schritt sich eingelebt hat in die Gemüter der Menschen. Denken Sie nur an das, was ich auch im öffentlichen Vortrage gesagt habe: wie lange es erst in bezug auf weltgeschichtliche Verhältnisse her ist, daß diese kopernikanische Weltanschauung sich verbreitet hat, und denken Sie daran, daß bis in die niedersten Schulen hinein diese Weltanschauung die Menschen ergriffen hat.",
      "Nun gibt es einen bedeutsamen Unterschied in bezug auf das Ergrei­fen der Menschenseele zwischen dieser kopernikanischen Weltanschau­ung und der anthroposophischen Weltanschauung, insofern sich diese aufbaut auf dem Fundament von Reinkarnation und Karma. Um die­sen Unterschied zu charakterisieren, braucht man wahrhaftig einen anthroposophischen Zweig mit Menschen, die in gutem Willen zusammensitzen;",
      "denn man muß eigentlich dabei ein Ding sagen, wenn man diesen Unterschied charakterisieren will, muß es notwendigerweise sagen, bei dem sich den außerhalb der anthroposophischen Bewegung stehenden Menschen wahrhaftig der Magen umdreht.",
      "Was gehörte denn dazu, daß die Menschen so schnell, so rasch und bis in das Kindheitsalter hinein die kopernikanische Weltanschauung angenommen haben? Die, welche mich über die kopernikanische Welt­anschauung oder über neuere Naturwissenschaft haben reden hören, die werden gewiß wissen, daß ich nicht irgendwie ein abträgliches Ur­teil fälle über diese moderne naturwissenschaftliche Anschauung.",
      "Da­her darf es schon gestattet sein, wenn man diesen betreffenden Unter­schied wirklich charakterisieren will, zu sagen: Um dieses Weltbild aufzunehmen, das rein auf eine Charakteristik des Raumes, auf äußere Raumverhältnisse beschränkt ist, war notwendig eine Epoche der Oberflächlichkeit! - Und der Grund, warum so schnell die koperni­kanische Weltanschauung sich eingelebt hat, ist kein anderer als der, daß die Menschen durch ein Zeitalter hindurch oberflächlich wurden. Oberflächlichkeit in der Auffassung der Welt war die notwendige Vor-bedingung für das Sich-Einleben der kopernikanischen Weltanschau­ung.",
      "Tiefe, Innerlichkeit - also gerade das Entgegengesetzte - wird notwendig sein, wenn sich einleben will, was die Wahrheiten der An­throposophie sind, und besonders in bezug auf die Grund- und Funda­mentalwahrheiten von Reinkarnation und Karma. Wenn wir uns daher heute die Überzeugung verschaffen, daß noch in einer viel, viel stärke­ren Weise und in einem viel größeren Umfange die Wahrheiten von Reinkarnation und Karma sich einleben müssen in die Menschheit, so müssen wir uns zugleich klar sein, daß wir in dieser Beziehung doch an der Grenze zweier Zeitalter stehen: des Zeitalters der Oberflächlich­keit - und des Zeitalters der notwendigen Vertiefung, der Verinner­lichung der Menschenseele und des Menschenherzens.",
      "Das ist es, was wir uns vor allen Dingen in die Seele schreiben müssen, wenn wir uns voll bewußt sein wollen, was Anthroposophie in der Gegenwart der modernen Menschheit zu bringen hat. Und dann müssen wir uns fra­gen: Wie wird sich denn dieses Leben gestalten müssen unter dem Ein­fluß der Erkenntnisse von Reinkarnation und Karma?",
      "Da müssen wir nur bedenken, was es denn eigentlich für das Menschenherz ist, zu erkennen: Reinkarnation und Karma sind eine Wahrheit. Was ist es für das ganze menschliche Bewußtsein, für das ganze Fühlen und Denken der menschlichen Seele? - Nichts Geringeres ist es doch, das kann jeder einsehen, wenn er über diese Dinge nachdenkt, als eine Erweiterung des menschlichen Seibstes durch Wissen, durch Erkenntnis über gewisse Grenzen hinaus, die sonst dem Wissen und der Erkenntnis gezogen sind. Denn daß man nur dasjenige wissen und erkennen könne, was eingeschlossen ist zwi­schen Geburt und Tod, das wurde ja gerade im abgelaufenen Zeit­alter mit aller Schärfe betont, und daß man höchstens im Glauben aufschauen könne zu einem, der wissend hineingeht in eine geistige Welt, das war eine immer stärker werdende Überzeugung. Aber die Sache ist nicht von einer so großen Bedeutung, wenn man auf dem Erkenntnisstandpunkt stehenbleibt; sondern von Bedeutung wird sie erst, wenn man vom Erkenntnisstandpunkt übergeht zum morali­schen Standpunkt, zum gemüthaft-moralischen Standpunkt. Da erst zeigt sich die ganze Größe und Bedeutung der Ideen von Reinkarna­tion und Karma.",
      "Wir könnten Hunderte von Dingen anführen zur Erhärtung dessen, was jetzt gesagt worden ist, aber es soll nur das eine gesagt werden. Nehmen wir den Menschen der früheren Zeiten der abendländischen Kultur und die weitaus großte Anzahl der Menschen noch heute inner­halb der abendländischen Kultur. Selbst wenn diese Menschen noch im intensivsten Maße an der Annahme hängen, daß der Mensch in bezug auf seine Wesenheit intakt erhalten bleibt, wenn er durch die Pforte des Todes auf dieser Erde geschritten ist, so wird doch, ohne daß man an Reinkarnation und Karma denkt, dieses ganze an den Tod sich an­schließende geistige Leben des Menschen dem Erdendasein entzogen. Man hat es zu tun mit dem Betreten einer geistigen Welt; aber mit Ausnahme eben jener «Ausnahmen», die von den mehr oder weniger spiritualistisch angelegten Naturen geltengelassen werden, daß Abge­storbene in Ausnahmefällen hereinwirken, haben wir es - wenn Rein­karnation und Karma nicht gelten - mit einer Idee zu tun, daß das, was in einer geistigen Welt sich abspielt, sei es Strafe oder Belohnung,",
      "wenn der Mensch durch die Pforte des Todes geschritten ist, der irdi­schen Sphäre als solcher entzogen ist, und daß sich das, was sich als Folge seines Lebens ergibt, auf einem ganz anderen, außerirdischen Schauplatze abspielt.",
      "Wenn der Mensch nun übergeht zur Erkenntnis von Reinkarnation und Karma, wird die Sache ganz anders. Da müssen wir uns klar sein, daß das, was für einen solchen Menschen in seiner Seele lebt, nicht bloß, wenn er durch die Pforte des Todes geschritten ist, eine Bedeutung hat für eine erdentrückte Sphäre, sondern daß von dem, was er erlebt zwischen Geburt und Tod, die Zukunft der Erdengestaltung abhängt. Die Erde wird sozusagen die äußere Konfiguration haben, welche die Menschen ihr geben, die vorher da waren. Der ganze Planet in seiner Zukunftskonfiguration, das Zusammenleben der Menschen in der Zu­kunft, hängt davon ab, wie die Menschen früher gelebt haben in ihren früheren Verleiblichungen. Das ist das Gemüthaft-Moralische, das sich an diese Ideen anknüpft; so daß ein Mensch, der dies angenommen hat, weiß: Wie ich war in dem Leben, so werde ich wirken auf alles, was in der Zukunft geschieht, auf die ganze Kultur der Zukunft! - Da er­weitert sich etwas mit dem Wissen von Reinkarnation und Karma über die Grenzen von Geburt und Tod hinaus, was der Mensch bisher nur in engsten Grenzen kennengelernt hat: das Verantwortlichkeitsgefühl! Da sehen wir herauswachsen ein gesteigertes Verantwortlichkeitsge­fühl. Darin prägt sich aus, was als eine tief bedeutsame moralische Folge auftritt von Ideen, wie es Reinkarnation und Karma sind. Der Mensch, der nicht an Reinkarnation und Karma glaubt, kann sagen:",
      "Wenn ich durch die Pforte des Todes gegangen bin, werde ich höchstens bestraft oder belohnt für das, was ich hier getan habe; ich erfahre die Folgen dieses Daseins in einer anderen Welt; diese andere Welt steht aber unter dem Regiment irgendwelcher geistiger Mächte, und die wer­den schon verhindern, daß das, was ich in mir trage, gar zu schädlich werde der Gesamtwelt. - So kann der nicht mehr sagen, der da weiß, daß Reinkarnation und Karma eine erkenntnismäßig sich ergebende Idee ist; denn er weiß, daß die Menschen durch die Wiederverkörpe­rung so sein werden, je nach dem, wie sie in dem vorhergehenden Leben gelebt haben.",
      "Das wird das Bedeutsame und Wichtige sein, daß übergehen werden die Fundamentalideen der anthroposophischen Weltanschauung in das Gemütsieben und in die Gesinnung der Menschen und auftreten werden als moralische Impulse, von denen die Menschen in den abgelaufenen Zeiten im Grunde genommen gar keine Ahnung hatten. Das Verant­wortlichkeitsgefühl, haben wir gesehen, wird hervorsprießen in einer Weise, wie dies früher überhaupt nicht möglich war; und andere moralische Ideen werden sich notwendig dann in einer ähnlichen Weise ergeben wie dieses Verantwortlichkeitsgefühl. Wir werden als Menschen, die unter dem Einfluß der Ideen von Reinkarnation und Karma leben, wissen lernen, daß es sich nicht handeln kann um eine Beurteilung unseres Lebens bloß nach den Voraussetzungen, welche sich zwischen Geburt und Tod ausleben, sondern nach Voraussetzun­gen, welche über viele, viele Leben hin verbreitet sind.",
      "Wenn wir unter den Voraussetzungen, die es bisher gegeben hat, an den anderen Menschen herantreten, so entwickeln wir zu diesem an­deren Menschen Sympathie, Antipathie, größere oder geringere Liebe und dergleichen. Man muß sagen, die Art und Weise, wie sich Mensch zu Mensch stellt in der Gegenwart, ist doch in Wahrheit das Ergebnis jener Anschauung, die das Leben auf der Erde einmal eingeschlossen denkt zwischen Geburt und Tod. Wir leben in Wahrheit wirklich so, wie wir leben müßten, wenn es eben richtig wäre, daß der Mensch nur einmal auf der Erde da wäre. Wir können sagen: Wir begegnen unseren Freunden, Eltern, Geschwistern und so weiter so, daß bei allem, was wir fühlen und empfinden, das eben mitlebt, daß wir nur einmal auf der Erde sind. Und es wird eine ganz außerordentliche Umgestaltung des Lebens vor sich gehen, wenn nicht nur in einigen Köpfen, wie es heute noch vielfach der Fall ist, als Theorie das lebt, daß es Reinkar­nation und Karma gibt. Bis heute ist es im weitesten Umfange noch Theorie. Man kann sagen, heute ist es so, daß es eine Anzahl Anthro­posophen gibt, die glauben an Reinkarnation und Karma; aber sie leben so, als wenn es Reinkarnation und Karma nicht gäbe, sondern als wenn das Leben einmal eingeschlossen wäre zwischen Geburt und Tod. Das kann auch nicht anders sein. Denn die Gewohnheiten, die das Leben mit sich bringt, ändern sich weniger rasch, als die Ideen sich ändern. Wenn",
      "wir richtige und konkrete Ideen über Reinkarnation und Karma - nur um diese kann es sich handeln - in unser Leben einführen, dann erst werden wir sehen, wie dieses Leben befruchtet werden kann durch solche Ideen.",
      "Wir sehen, daß wir als Menschen hereintreten in das Leben, indem wir im Beginne desselben zusammenkommen mit Eltern, mit Geschwi­stern und so weiter. Wir sehen, daß wir durch diese Natureinrichtung notwendigerweise in der ersten Zeit unseres Lebens vorzugsweise so in demselben drinnenstehen, daß die, welche um uns herum sind, mehr oder weniger durch Naturelemente um uns herum gestellt sind: durch Blutsverwandtschaft, Nähe des Ortes und so weiter. Dann sehen wir, wenn wir heranwachsen, wie diese Kreise der Blutsverwandtschaft sich erweitern, wie wir in ganz andere, nicht mehr von Blutsverwandt­schaft abhängige Verbindungen mit diesen oder jenen Menschen treten. Nun handelt es sich darum, daß diese Dinge erst karmisch eingesehen werden müssen; dann werden sie eine ganz neue Beleuchtung für das Leben gewinnen. Denn Karma wird erst bedeutungsvoll für das Leben, wenn wir es konkret fassen, wenn wir wirklich auf das Leben anwen­den, was die geisteswissenschaftliche Forschung ergibt. Festgestellt wer­den kann das selbstverständlich nur von der geisteswissenschaftlichen Forschung, kann aber dann auf das Leben angewendet werden.",
      "Eine bedeutungsvolle karmische Frage ist im wesentlichen diese: Wie kommt es denn, daß wir zum Beispiel im gegenwärtigen Leben mit den Menschen zusammenkommen, mit denen wir auf die ja jedem begreif­liche Weise durch die Blutsverwandtschaft zusammenkommen? Warum kommen wir mit diesen im Beginne dieses Lebens zusammen? - Nun zeigt die geisteswissenschaftliche Forschung über diese Frage etwas sehr Eigentümliches. In der Regel ist es so - denn wenn auch einzelne Tatsachen angegeben werden, gibt es doch wieder unzählige Aus­nahmen -, daß wir mit den Menschen, die wir unwillkürlich treffen im Beginne unseres Lebens, schon in einem vorhergehenden Leben zu­sammen waren, meistens sogar in dem unmittelbar vorhergehenden, in der Mitte unseres Lebens, so in den Dreißigerjahren. Da haben wir sie uns in irgendeiner Weise freiwillig gewählt, indem wir zu ihnen hin-getrieben waren durch unsere Herzensneigung und so weiter. Wir würden",
      "ganz fehl gehen, wenn wir die Menschen, mit denen wir im Beginne unseres Lebens zusammenkommen, als solche betrachten würden, mit denen wir auch wieder im Beginne eines anderen Lebens zusammen wa­ren. Nicht am Anfange, nicht am Ende, sondern in der Mitte eines Lebens waren wir durch freiwillige Wahl mit jenen zusammen, mit denen wir dann in einem folgenden Leben zusammentreffen durch Blutsverwandtschaft. Sehr häufig sind die Fälle so, daß man zu dem, mit dem man verheiratet war, den man sich also durch freie Wahl ge­nommen hat, im nächsten Leben im Vater- oder Mutterverhältnis oder im Geschwisterverhältnis steht. Die geisteswissenschaftliche Forschung zeigt, daß das, was man aus der Spekulation voraussetzen würde, was man denken würde, wenn man etwas ausspintisiert über die Dinge, gewöhnlich falsch ist. Die Tatsachen machen gewöhnlich einen Strich durch die Rechnung der Spekulation.",
      "Denken wir nur einmal diese jetzt geschilderte Tatsache und fassen wir sie so auf, wie sie sich wirklich, wenn man vorurteilsfrei forscht, aus der Geisteswissenschaft ergibt, wie sie wieder unser ganzes Verhält­nis und unsere ganze Beziehung zum Leben erweitert. Es ist ja nach und nach im Verlaufe der abendländischen Kultur dazu gekommen, daß der Mensch eigentlich jetzt schon gar nicht mehr anders kann, als von Zufall zu reden, wenn er nachdenkt über sein Verhältnis zu den­jenigen, mit denen er blutsverwandt ist. Man redet von Zufall, man glaubt auch vielfach schon an den Zufall. Wie sollte man denn an etwas anderes glauben als an Zufall, wenn man das Leben nur einmal einge­schlossen denkt zwischen Geburt und Tod. Für das eine Leben wird man selbstverständlich zugeben, daß man verantwortlich ist für die Folgen der Ereignisse, die man selbst herbeigeführt hat. Indem man sein eigenes Selbst hinüberführt über das, was sich abspielt zwischen Ge­burt und Tod, indem man sein Selbst verbunden fühlt mit anderen Menschen der anderen Verkörperung, fühlt man sich verantwortlich wie hier im Leben seinen eigenen Taten gegenüber. Es werden immer mehr und mehr die Menschen diese konkreten Tatsachen erfahren müs­sen. Die allgemeine Idee, wenn man sagt, der Mensch habe sich im Sinne des Karma seine Eltern selber gewählt, gibt noch nichts Beson­deres. Aber man bekommt eine Vorstellung von dieser Wahl, die wirklich",
      "nun durch alle übrigen Erfahrungen des Lebens bekräftigt werden kann, wenn man weiß: Die, welche du dir jetzt am allerunbewußtesten gewählt hast, die hast du dir in einem früheren Leben in einem Zeit­punkte deiner größten Bewußtheit gewählt, wo du am allerreifsten warst.",
      "Das mag manchem vielleicht heute unangenehm sein, aber wahr ist es doch. Denn man wird lernen, wenn man mit seinen Blutsverwandten nicht zufrieden ist, daß man eben zu dieser Unzufriedenheit selber den Grund gelegt hat, daß man also für die nächste Inkarnation wird anders vorsorgen müssen; und dann wird schon die Idee von Reinkarnation und Karma fruchtbar werden für das Leben. Und das ist es ja, daß diese Ideen nicht für die Befriedigung irgendeiner Neugierde und so weiter, sondern für unsere Vervollkommnung und damit für die Ver­vollkommnung des ganzen Lebens gelten. Und weiter werden wir wis­sen, daß das, was gesagt worden ist, etwas Ähnliches für das gegen­wärtige Leben und dessen Folgen nach sich zieht; daß diejenigen, mit denen wir in den Dreißigerjahren zusammengeführt werden, wo wir also mit unserem vollen Verstande zu urteilen glauben, durchaus so mit uns verbunden werden, daß sie in einem nächsten Leben uns gleich am Ausgangspunkte, vielleicht als Eltern oder Geschwister, entgegentreten werden. Wenn wir wissen, was davon abhängt, daß sich Familienkon­figurationen bilden, daß diese oder jene Leute zusammenkommen, so wird sich unser Verantwortlichkeitsgefühl unter den Ideen von Rein­karnation und Karma bedeutsam erweitern.",
      "Ich sagte, daß wir betonen können, daß diese Dinge sich als begreif­lich im Leben erweisen. Müssen nicht die Kräfte, die eine Menschen-individualität herunterbringen in eine Familie, ganz bedeutende, starke sein? Stark können sie aber nicht sein in dem Menschen, der jetzt ver­körpert wird; denn da können sie nicht viel zu tun haben mit den Welten, in die er herunterkommt. Muß es nicht begreiflich sein, daß die Kräfte, die im Tiefsten der Seele wirken, aus Zeiten stammen müssen des vergangenen Lebens, wo mit der starken Kraft der Freundschaft, der «bewußten Liebe», wenn man es so nennen darf, die Zusammen­hänge von uns herbeigeführt wurden? Was als bewußte Kräfte in dem einen Leben gewaltet hat, das wirkt als unbewußte Kräfte in dem",
      "nächsten Leben; was auf mehr oder weniger unbewußte Art geschieht, das erklärt sich auf diese Weise.",
      "Allerdings ist es notwendig, daß man sich die Tatsachen der For­schung nicht trübt, weil diese Tatsachen der Forschung fast immer einen Strich durch die Spekulation machen, so daß man nur hinterher die Logik in den Tatsachen finden kann. Man soll sich nicht verleiten lassen, durch Spekulation vorgehen zu wollen; denn da wird man nicht zu dem richtigen Gesichtspunkt kommen, sondern immer zu etwas Ähnlichem, was sich charakterisieren läßt durch jenes Gespräch, das ich auch schon erzählte. In einer süddeutschen Stadt nämlich sagte mir einmal ein Theologe: Ich habe Ihre Schriften gelesen und habe gesehen, daß sie so logisch sind; daher habe ich mir gedacht, wenn sie so logisch sind, so kann ihr Verfasser vielleicht auch auf dem Wege der bloßen Logik dazu gekommen sein. - Wenn ich mich also bemüht hätte, weniger «logisch» zu schreiben, so würde ich mir damit ein Verdienst erworben haben in den Augen des betreffenden Theologen, weil er dann gesehen haben würde, daß die Darstellungen nicht durch bloße Logik gefunden worden sind. Wer aber auf die Schriften eingeht, der wird sehen, daß die logischen Formen ihnen nachher gegeben sind, daß sie aber nicht durch Logik gefunden worden sind. Ich wenigstens könnte es nicht, das versichere ich Ihnen. Vielleicht könnten es andere durch bloße Logik finden.",
      "Wenn wir die Dinge so ansehen, erweist es sich als eine tief bedeut­same Idee, daß die wichtigsten Impulse, die aus der Anthroposophie hervorgehen müssen, moralisch-gemüthafte Impulse sein müssen. Wir haben heute das Verantwortlichkeitsgefühl auf verschiedenen Gebieten hervorgehoben. Wir könnten ebenso Liebe, Mitleid verfolgen, die alle verschiedene Formen annehmen unter dem Einfluß der Ideen von Re­inkarnation und Karma. Aus diesem Grunde war es auch, warum wir im Verlaufe der Jahre so sehr Wert darauf gelegt haben, selbst bis in die öffentlichen Vorträge hinein, Anthroposophie immer mit Bezug auf das Leben, mit Bezug auf die unmittelbarsten Erscheinungen des Le­bens zu betrachten. So haben wir gesprochen über die Mission des Zor­nes, über das menschliche Gewissen, über das Gebet, über die Erziehung des Kindes, über die verschiedenen Lebensalter des Menschen - und",
      "haben alle diese Dinge in das Licht gerückt, in das sie gerückt werden müssen, wenn man die Ideen von Reinkarnation und Karma als die richtigen voraussetzt. Und da hat sich uns ergeben, wie umgestaltend diese Ideen von Reinkarnation und Karma in das Leben eingreifen.",
      "Das hat ja im Grunde genommen den Hauptteil unserer Betrachtungen ausgemacht, daß wir die fundamentalen Ideen in ihrer Wirkung für das Leben betrachtet haben. Wenn auch nicht immer, ich möchte sa­gen, mit abstrakten Worten aus Reinkarnation und Karma die Be­deutung hergeleitet wird, die zum Beispiel Gemütseigenschaften, oder das Gewissen, der Charakter, das Gebet erfahren, wenn das auch nicht immer so hergeleitet wird, daß man sagt: Wenn man Reinkarnation und Karma annimmt, dann ergibt sich - und so weiter, so standen doch alle unsere Betrachtungen unter dem Impuls von Reinkarnation und Karma.",
      "Und das wird das Bedeutsame sein für die nächste Gegen­wart, daß nicht nur die Seelenwissenschaft eine Beeinflussung erfahren wird durch die Ideen von Reinkarnation und Karma, sondern auch die anderen Wissenschaften. Wenn Sie einen solchen Vortrag verfolgen wie den letzten öffentlichen: «Der Tod bei Mensch, Tier und Pflanze», so werden Sie sehen, daß es sich darum handelte zu zeigen, wie die Men­schen denken lernen werden über den Tod bei Pflanze, Tier und Mensch, wenn sie in sich selbst das sehen, was über das einzelne Leben des Menschen hinausgeht.",
      "Wir kamen auf die Bedeutung des Todes bei Mensch, Tier und Pflanze dadurch, daß wir uns klar wurden:",
      "Anders lebt das Selbst im Menschen, anders beim Tier und wieder anders bei den Pflanzen. Beim Menschen ist es ein individuelles Ich, bei den Tieren ist es die Gruppenseele, und bei den Pflanzen haben wir es mit einem Teil des ganzen Planetenseelensystems zu tun. Dadurch faßten wir bei den Pflanzen als ein bloßes Einschlafen und Aufwachen auf, was uns als Tod und Entstehen äußerlich entgegentritt. Bei den Tieren ist es wieder anders; da ist es ähnlich wie in uns selber, indem das Selbst in einer Inkarnation vorrückt, gewisse Instinkte und so weiter überwindet. Aber erst beim Menschen, der selbst seine Verkör­perungen herbeiführt, waren wir uns klar, daß erst der Tod die Ge­währ bietet für die Unsterblichkeit, und daß das Wort Tod in dieser Bedeutung nur beim Menschen so gebraucht werden dürfte, oder daß",
      "wir, wenn wir das Wort Tod allgemein gebrauchen, hervorheben müß­ten, wie der Mensch, wie das Tier und wie die Pflanze stirbt, und daß wir ein ganz neues Wort gebrauchen müßten bei Tier und Pflanze.",
      "Alles andere in der Anthroposophie ist ein solches, daß die Menschen-seele fordert, etwas zu erfahren über diese oder jene Dinge; aber es macht sozusagen das «Andere» im Grunde genommen gar nicht den Anthroposophen aus. Zu gewissen Dingen kommt er schon, wenn es Zeit ist. Wenn er zunächst in der Lage ist, die Ideen von Reinkarnation und Karma in dem Sinne aufzunehmen, wie wir sie geben müssen im Unterschiede von älteren Ideen von Reinkarnation und Karma, wie zum Beispiel im Buddhismus, so kommt der Mensch im Ver­laufe der Forschung ganz von selbst schon zu anderen Dingen. Daher war der Hauptteil unserer Arbeit dem gewidmet, den Einfluß von Reinkarnation und Karma auf das gesamte Menschenleben ins Auge zu fassen.",
      "In dieser Beziehung sollte es klar sein, daß die Arbeit innerhalb ir­gendwelcher anthroposophischer Vereinigung oder Gesellschaft im Sinne dieser Mission der Anthroposophie aufgefaßt werden müßte. Da­her ist es begreiflich, daß wir im Grunde genommen über diejenigen Fragen, welche dem Außenstehenden, dem von der Anthroposophie als solcher weniger Berührten, vielleicht zunächst als die wichtigsten erscheinen, eigentlich nur reden, wenn wir eben von den Grundwahr­heiten aufsteigen wollen zu denjenigen Dingen, die jeder Seele, weil sie eine abendländische Seele ist, am nächsten sind. Es wäre durchaus der Fall denkbar, daß man das Neue, was heute als das fundamental Neue charakterisiert worden ist, von der Anthroposophie aufnehmen würde und sich zunächst gar nicht kümmerte um irgendwelche religiösen Ge­gensätze der Menschen. Denn das ist gar nicht das Charakteristische dieser neuen Geisteswissenschaft, daß etwa vergleichende Religions­wissenschaft getrieben würde; wenn das zwar heute auch getrieben wird, genug sogar. Aber gegenüber dem, was sonst heute da getan wird, ist das, was bei den Theosophen getrieben wird, gar nicht das Geist-reichere. Das ist aber das Bedeutsame, daß in der Anthroposophie alle diese Dinge in das Licht gerückt werden. das von den Ideen von Rein­karnation und Karma ausgeht.",
      "Namentlich wird noch in einer anderen Beziehung das Verantwort­lichkeitsgefühl unter dem Einfluß von Reinkarnation und Karma ganz beträchtlich wachsen. Wenn wir nur einmal auf das sehen, was heute gesagt worden ist über das Verhältnis von Blutsverwandten zu frei gewählten Menschen, so sehen wir schon, daß ein gewisser Gegensatz besteht: Was in einem Leben das Innerlichste, das Verborgenste an Im­pulsen ist, das ist in dem anderen das Offenbarste.",
      "Wenn wir unsere tiefsten Freundschaftsgefühle in der einen Inkarnation Menschen ent­gegenbringen, so bereiten wir dadurch wohl vor eine äußere Verwandt­schaft, eine Blutsverwandtschaft oder dergleichen. Ähnlich ist es auf einem anderen Gebiete.",
      "Die Art, wie wir über irgend etwas denken, was uns als das Unwirklichste in dieser Inkarnation erscheint, das wird uns das Maßgebendste, das die eigentlichen Impulse für die nächste In­karnation Bedingende sein. Die Art, wie wir denken, ob wir uns leich­ten Herzens einer Wahrheit hingeben, oder ob wir mit allen Mitteln, die uns zur Verfügung stehen, prüfend uns an eine Wahrheit heran-machen, ob wir Wahrheitssinn oder Fanatismus haben, das tritt in ein ganz anderes Verhältnis zur menschlichen Entwickelung durch das Sich-Einleben in die Ideen von Reinkarnation und Karma, als es heute der Fall ist.",
      "Denn, was wir nur in unserem Innersten haben in der ge­genwärtigen Inkarnation, das werden wir am offenbarsten haben in der nächsten. Und wer viel lügt oder Neigung hat, leichten Herzens dieses oder jenes anzunehmen, der wird ein leichtsinniger Mensch wer­den in der nächsten oder einer nächsten Inkarnation; denn, was wir denken, wie wir denken, wie wir uns zur Wahrheit stellen, was also in dieser Inkarnation innerlich ist, das wird das Maß des Verhaltens in unserer nächsten Inkarnation bilden.",
      "Wenn wir zum Beispiel, ohne daß wir sehr genau prüfen, in dieser Inkarnation einen Menschen für einen schlechten halten, während er sich, wenn wir ihn genau prüfen würden, vielleicht als ein guter oder höchstens als ein halbguter erweisen würde, wenn wir diesen Gedanken ungeprüft durch das Leben tragen, so wird sich herausstellen, daß wir, indem wir uns in dieser Weise Urteile bilden über Menschen, unverträgliche, zänkische, abscheuliche Menschen wer­den in der nächsten Inkarnation! Da haben wir wieder eine Erweite­rung des moralisch-gemüthaften Elementes in unsere Seele.",
      "Das ist außerordentlich wichtig, daß wir solche Dinge recht sehr ins Auge fassen, und daß wir uns einmal mit dem Gedanken bekannt­machen, welche fundamentale Bedeutung es hat, in sein Innerstes, in sein ganzes Gemüt das aufzunehmen, was nun wirklich als Neues und alles andere dadurch in einer gewissen Weise Erneuernde in die geistige Entwickelung der Gegenwart mit den Ideen von Reinkarnation und Karma hereintritt. Daher ist es, daß wir darauf den Hauptwert legten in dem ganzen Verlauf unserer anthroposophischen Bewegung, und daß wir gewissermaßen andere Fragen, die gewiß mit Notwendigkeit sich aus diesen ergeben, auch nur in dieser Weise behandeln, wie das sich notwendig ergeben muß.",
      "Daher könnte zum Beispiel unsere Eigenart, unsere ganze Art und Weise, wie Anthroposophie in unserer Mitte ge­trieben wird, wenn die Dinge in Wahrheit dargestellt werden, wie wir es machen, niemals als im Gegensatze zu einer Bewegung aufgefaßt wer­den, welche Reinkarnation und Karma in den Mittelpunkt der Be­trachtungen stellt. Der Gegensatz zu uns muß immer von außen kon­struiert werden; es ist unmöglich, daß er sich ergeben kann, wenn man die Dinge, die in unserer Mitte geschehen, wirklich richtig darstellt.",
      "Wir brauchen nur das eine Moment ins Auge zu fassen: Wie wenig wird eigentlich über die Christus-Frage in unserer Mitte gesprochen! Da darf niemand das, was gesagt wird, deshalb vergrößern, weil er es für sein Herz als besonders wichtig empfindet, sondern er muß es ob­jektiv betrachten; so daß niemand einen Grund hat, weil dieses oder jenes als notwendige Folge für das gereifte Begreifen von Reinkarna­tion und Karma sich ergibt, zu sagen, daß wir viel über die Christus-Frage sprechen.",
      "Denn das ist nicht das Fundamentale, was den An­throposophen in der Gegenwart ausmacht, sondern das ist es, was neu in die Welt hereintritt, und daß das, was neu hereintritt, wirklich von der Menschheit aufgenommen wird. So also müßten wir dies verstehen, daß es eigentlich nur durch eine unrichtige, oder unter der Voraus­setzung einer unrichtigen Darstellung der Art und Weise, wie wir die Dinge hier treiben, möglich wäre, einen Gegensatz zu konstruieren; denn der muß immer von außen zu uns konstruiert werden.",
      "Man kann Gegner sein von uns, aber wir brauchen nicht irgendeine Gegnerschaft zu konstruieren; denn das Sich-nicht-Kümmern um etwas, bedeutet",
      "nicht eine Gegnerschaft, sonst müßte man ein Gegner sein von allem, worum man sich nicht kümmert!",
      "Das wollte ich Ihnen besonders an die Seele legen: daß wir nach­denken, was das Fundamentale, was das Neue an der Anthroposophie eigentlich ausmacht. Selbstverständlich soll damit nicht gesagt sein:",
      "Eine anthroposophische Gesellschaft ist die, welche an Reinkarnation und Karma glaubt. Sondern es soll damit gesagt sein: So wie einmal eine Zeit reif geworden ist, um die kopernikanische Weltanschauung aufzunehmen, so ist unsere Zeit reif geworden, die Lehre von Rein­karnation und Karma zum allgemeinen Bewußtsein der Menschheit zu bringen. Und was geschehen soll im Verlaufe der Menschheitsentwicke­lung, das wird geschehen, wie viele Mächte sich auch dagegen erheben. Und mit Reinkarnation und Karma, mit dem wirklichen Begreifen von Reinkarnation und Karma werden sich alle anderen Dinge von selbst ergeben. Die anderen Dinge ergeben sich durch das Licht, das von Rein­karnation und Karma ausstrahlt.",
      "Es war gewiß einmal ganz nützlich, betrachtet zu haben, was eigent­lich das fundamental Unterscheidende ist zwischen denjenigen, die sich an der Anthroposophie interessiert fühlen, und denjenigen, die ihre Gegnerschaft gegen sie entwickeln. Das Annehmen einer höheren Welt als solches ist es eigentlich nicht; sondern das ist es, was die Vorstel­lungen an Höherem erfahren durch die Voraussetzung der Ideen von Reinkarnation und Karma. Damit haben wir heute etwas angegeben, was als das Wesentliche der anthroposophischen Weltanschauung an­gesehen werden kann."
    ],
    "sentences": [
      [
        "Wir haben hier an dieser Stelle jahrelang anthroposophische Wahrhei­ten betrachtet, anthroposophische Erkenntnisse.",
        "Wir haben versucht, uns dem, was wir glauben Anthroposophie nennen zu müssen, von den verschiedensten Richtungen her zu nähern und in uns dasjenige aufzu­nehmen, was aus den anthroposophischen Erkenntnissen heraus kom­men kann.",
        "Es wird sich nun empfehlen, einmal gerade im Verlaufe der Betrachtungen, die wir zuletzt hier angestellt haben und noch anstellen werden, die Frage aufzuwerfen, was den Menschen der Gegenwart, den Menschen unserer Zeit die Anthroposophie überhaupt eigentlich geben soll und geben kann?",
        "Was sie enthält, von dem wissen wir ja durch unsere Betrachtungen ein gut Stück, und wir können daher auf Grundlage der Bekanntschaft mit einigen anthroposophischen Wahr­heiten an die Frage herantreten: Was kann die Anthroposophie den Menschen der Gegenwart geben?"
      ],
      [
        "Wenn wir an diese Frage herantreten, müssen wir vor allen Dingen darauf bedacht sein, das anthroposophische Leben, die anthroposo­phische Bewegung - in unseren Gedanken wenigstens - scharf zu trennen von irgendeiner gesellschaftlichen Einrichtung, von irgend etwas, das man mit dem Namen Anthroposophische Gesellschaft be­legen könnte.",
        "In der Wirklichkeit wird ja das ganze gegenwärtige Le­ben selbstverständlich immer wieder und wieder notwendig machen, daß sich diejenigen, die Anthroposophie treiben wollen, in gesellschaft­licher Art vereinigen.",
        "Aber wenn diese Vereinigung notwendig ist, so ist sie eben mehr notwendig durch das ganze außerhalb der Anthropo­sophie stehende gegenwärtige Leben, als etwa durch den Inhalt und durch Gesinnung oder durch sonst irgend etwas innerhalb der Anthro­posophie selber.",
        "Anthroposophie an sich könnte heute durchaus so ver­kündet werden, wie irgend etwas anderes gegenwärtig unter den Men­schen verkündet wird.",
        "Anthroposophie als solche könnte - denkbar wäre das durchaus - so verkündet werden, wie etwa Chemie heute unter den Menschen verkündet wird, und es könnten die Menschen zu"
      ],
      [
        "den anthroposophischen Wahrheiten herankommen, wie sie an Chemie oder Mathematik herankommen.",
        "Was dann für die Seele des einzelnen daraus folgt, wie die Seele des einzelnen die Anthroposophie aufnimmt und zum Impuls des Lebens macht, das könnte dann eben Sache eines jeden einzelnen sein."
      ],
      [
        "Eine Anthroposophische Gesellschaft oder irgend­eine Vereinigung, um Anthroposophie zu treiben, macht der Umstand, die Tatsache notwendig, daß Anthroposophie als solche etwas ist, was als etwas völlig Neues, als eine völlig neue Erkenntnis in unsere Gegen-wart hereintritt und aufgenommen werden soll von dem geistigen Le­ben, während die Menschen draußen im außeranthroposophischen Le­ben eigentlich durchaus nicht nur, sagen wir, die allgemeine Seelen-verfassung der Gegenwart brauchen, um Anthroposophie auf sich wirken zu lassen, sondern auch zu dieser gewöhnlichen Seelenverfas­sung, wie sie die Menschen heute haben, eine besondere Vorbereitung des Gemütes, des Herzens brauchen.",
        "Und eine solche Vorbereitung des Gemütes und des Herzens kann nur angeeignet werden durch das Zusammenleben in unseren anthroposophischen Zweigen oder anthro­posophischen Verbindungen oder dergleichen."
      ],
      [
        "Da eignen wir uns eine gewisse Art des Denkens, eine gewisse Art des Fühlens an, so daß wir dadurch in die Lage kommen, Dinge ernsthaft zu betrachten, welche die Menschen, die heute draußen in der Welt stehen und kaum etwas von Anthroposophie gehört haben, ganz selbstverständlich und begreiflicherweise vielleicht sogar als tolle Phantastereien ansehen müssen."
      ],
      [
        "Gewiß, es könnte eingewendet werden, Anthroposophie würde auch verbreitet durch öffentliche Vorträge, welche da zu ganz unvorberei­teten Menschen sprechen.",
        "Aber gerade die, welche im engeren Sinne gesellschaftsmäßig unseren Kreisen angehören, werden wissen, daß der ganze Ton und die ganze Art und Weise der Haltung eines anthropo­sophischen Vortrages anders sein muß, wenn er vor einem unvorbe­reiteten Publikum gehalten wird, als vor denjenigen, zu denen man so sprechen kann, daß sie durch den Drang ihres Herzens, durch die ganze Art und Weise ihrer inneren Gesinnung das ernst nehmen, was das große Publikum noch nicht ernstnehmen könnte.",
        "Und dies, was jetzt angedeutet worden ist, wird in der nächsten Zukunft nicht etwa besser"
      ],
      [
        "werden - davon kann gar keine Rede sein -, sondern es wird in der nächsten Zukunft immer stärker und schärfer hervortreten.",
        "Die äußere Gegnerschaft gegen alles Anthroposophische wird immer größer und größer werden in der Welt, und zwar aus dem Grunde, weil gerade Anthroposophie in unserer Gegenwart etwas im höchsten Grade Zeit­gemäßes, etwas im höchsten Grade Notwendiges ist, und weil gegen das Allernotwendigste, gegen das Allerzeitgemäßeste die Auflehnung der Menschen im Grunde genommen immer am allerstärksten ist."
      ],
      [
        "Nun könnte die Frage entstehen: Warum denn das?",
        "Warum ist die Auflehnung der Menschenherzen irgendeines Zeitalters am allerstärk­sten gegen das, was dieses Zeitalter am allernotwendigsten braucht? -Das ist etwas, was der Anthroposoph sollte begreifen können, was aber zu schwierig ist, um es vor einem unvorbereiteten Publikum auch nur im allerentferntesten klarzumachen."
      ],
      [
        "Der Anthroposoph weiß, daß es luziferische Kräfte und Wesenheiten gibt, die hinter der allgemeinen Evolution zurückgeblieben sind.",
        "Die wirken durch die Menschenherzen, durch die Menschenseelen, und sie haben das allergrößte Interesse daran, in den Zeiten, in welchen das Streben nach aufwärts am größten wird, ihre Attacken, ihre Angriffe am allerstärksten zu machen.",
        "Weil nun die Auflehnung der Menschen-herzen gegen das, was vorwärtsstrebt in der Menschheitsentwickelung, von den luziferischen Kräften herrührt, und weil diese ihre Attacken dann unternehmen werden, wenn es ihnen sozusagen an den Kragen geht, deshalb müssen diese Attacken - also auch die Auflehnung der Menschenherzen - in solchen Zeiten am allerstärksten sein.",
        "Daher werden wir verstehen, daß die für die Menschheit bedeutsamsten Wahr­heiten sich von jeher dadurch eingelebt haben in die Menschheitsent­wickelung, daß sie mit dem Umstande rechnen mußten, daß sie die stärksten Widerstände finden.",
        "Etwas, was sich nicht sehr unterscheidet von dem, was sonst auch vorkommt in der Welt, wird kaum starke Widerstände finden.",
        "Aber, was deshalb in die Welt tritt, weil die Menschheit seit langem darnach dürstet und es nicht empfangen hat, das ist zugleich das, was die stärksten Attacken der luziferischen Kräfte herausfordert.",
        "Und so ist eine Gesellschaft eigentlich nichts weiter als ein Schutzwall gegen dieses ganze, aber begreiflich charakterisierte Verhalten"
      ],
      [
        "der Außenwelt.",
        "Man muß etwas haben, innerhalb dessen man diese Dinge so vertreten kann, daß man sagen kann: Diejenigen, zu denen man spricht, oder mit denen man zusammen ist, sie bringen der Sache ein gewisses Verständnis entgegen, und die anderen, welche sich nicht vereinigt haben mit denen, die davon sprechen, die geht es nichts an. - Von dem, was in der Öffentlichkeit vertreten wird, glauben alle Menschen, daß es sie etwas angeht, und daß sie ein Urteil darüber ab­zugeben haben, natürlich gestachelt von den luziferischen Kräften.",
        "Daraus ersehen wir, daß es zwar notwendig ist, Anthroposophie zu treiben, daß aber Anthroposophie etwas hereinbringt in unsere Gegen­wart, was hereinkommen muß und verlangt wird von dem geistigen Durste und dem geistigen Nahrungsbedürfnis unserer Zeit, und was unter allen Umständen hereinkommen wird auf irgendeine Art.",
        "Denn dafür, daß es hereinkommt, dafür sorgen die geistigen Mächte, die sich der Evolution gewidmet haben."
      ],
      [
        "Daher können wir im rein anthroposophischen Sinne die Frage auf­werfen: Worin liegen die wichtigsten Dinge, die gegenwärtig der Menschheit eingepflanzt werden sollen durch die Anthroposophie?",
        "Es werden diejenigen sein, nach denen die gegenwärtige Menschheit ganz besonders dürstet, die am allernotwendigsten sind.",
        "Gerade mit der Be­antwortung einer solchen Frage kann man am allermeisten mißver­standen werden.",
        "Deshalb ist es so notwendig, für die Gedanken zu-nächst Anthroposophie und Anthroposophische Gesellschaft zu tren­nen.",
        "Denn, was die Anthroposophie der Menschheit bringen soll, sind neue Erkenntnisse, neue Wahrheiten.",
        "Aber eine Gesellschaft kann nie­mals - und am allerwenigsten in unserer Zeit - auf irgendwelche besonderen Wahrheiten eingeschworen werden.",
        "Die Frage wäre die allerunsinnigste: Welchen Glauben habt ihr Anthroposophen? - Un­sinnig ist sie dann, wenn man unter «Anthroposophen> einen Menschen meint, der zur Anthroposophischen Gesellschaft gehört; denn man würde dabei voraussetzen, daß eine ganze Gesellschaft eine gemein­same Überzeugung, ein gemeinsames Dogma haben würde.",
        "Das kann nicht sein.",
        "In dem Augenblick, wo eine ganze Gesellschaft - statuten-gemäß - auf ein gemeinsames Dogma schwören müßte, hörte sie auf eine Gesellschaft zu sein, und es würde die Sektiererei beginnen.",
        "Hier"
      ],
      [
        "haben wir die Grenze, wo eine Gesellschaft aufhört, eine Gesellschaft zu sein.",
        "In dem Augenblick, wo ein Mensch verpflichtet würde, eine von der Gesellschaft geforderte Überzeugung zu haben, hätte man es mit einer Sektiererei zu tun.",
        "Daher kann eine Gesellschaft, welche sich dem widmet, was jetzt charakterisiert worden ist, dies nur unter dem Gesichtspunkte sein, daß sie es ist unter dem naturgemäßen geistigen Drange.",
        "Man kann fragen: Welche Menschen kommen herbei, um über Anthroposophie etwas zu hören? - Und man wird sagen können: Es sind die, welche irgend etwas über geistige Dinge hören wollen, die einen Drang haben, über geistige Dinge etwas zu hören. - Dieser Drang ist kein Dogma.",
        "Denn wenn jemand etwas sucht, wovon er nicht sagt, ich werde dieses oder jenes finden, sondern wo er, wenn er sucht, !; eben sucht, so ist dieses Suchen das Gemeinsame, was eine Gesellschaft,"
      ],
      [
        "die nicht eine Sekte werden will, haben muß.",
        "Aber ganz unabhängig davon ist die Frage: Was bringt nun die Anthroposophie als solche der Menschheit? - Und man muß sagen: Die Anthroposophie als solche bringt der Menschheit etwas, was ähnlich, nur geistiger und in bezug auf das menschliche Gemüt tiefer und bedeutungsvoller ist, als alle großen geistigen Wahrheiten gewesen sind, welche je der Menschheit gebracht worden sind."
      ],
      [
        "Nun gibt es unter den Dingen, die wir im Verlaufe unserer Betrach­tungen an uns haben herantreten lassen, manche, von denen man sagen kann: sie sind so, daß sie eigentlich nicht als die bedeutsamen, als die bezeichnenden angegeben werden können, wenn von dem die Rede ist, was eigentlich die gegenwärtige Menschheit als Neues erhalten soll.",
        "Aber fundamentale Dinge sind es, fundamentale Wahrheiten, die wirk­lich als neu in die Menschheit hereintreten.",
        "Und wir brauchen nicht sehr weit zu gehen, um zu charakterisieren, worin eigentlich das Neue der anthroposophischen Bewegung liegt.",
        "Es liegt darin, daß die zwei Wahrheiten, die sozusagen zu unseren fundamentalsten Dingen ge­hören, an die Menschenseele in einer immer überzeugenderen Weise herantreten: die beiden Wahrheiten von Reinkarnation und Karma.",
        "Man kann sagen: Was der Anthroposoph in erster Linie auf seinem Wege findet, wenn er heute ernstlich strebt, das ist die Notwendigkeit der Erkenntnis von Reinkarnation und Karma.",
        "Wir können zum Beispiel"
      ],
      [
        "nicht sagen, daß in der abendländischen Kultur gewisse Dinge, wie etwa die Möglichkeit, in höhere Welten sich zu erheben, durch die Anthroposophie als etwas fundamental Neues auftritt; denn wer die abendländische Entwickelung kennt, wer da weiß, ich will nur sagen, daß es Mystiker gegeben hat, selbst solche Mystiker, wie Jakob Böhme oder Swedenborg oder wie die ganze Jakob Böhmesche Schule, der weiß auch, daß das eine - wenn es auch vielfach strittig war - immer ge­glaubt worden ist, daß es immer da war als Ansicht: daß sich der Mensch aus der gewöhnlichen Sinneswelt zu höheren Welten erheben kann; so daß dies also nicht das fundamental Neue ist.",
        "Weiter sind auch gewisse andere Dinge nicht das fundamental Neue."
      ],
      [
        "Selbst wenn wir über das sprechen, was in bezug auf die Evolution fundamental ist; wenn wir zum Beispiel sprechen über die Christus-Frage: in bezug auf die anthroposophische Bewegung als solche ist sie nicht das Fundamen­talste; sondern das Fundamentalste ist die Gestalt, welche die Christus-Frage dadurch erhält, daß Reinkarnation und Karma in die Herzen der Menschen als Wahrheiten aufgenommen werden.",
        "Die Beleuchtung, welche die Christus-Frage erhält unter der Voraussetzung der Wahr­heiten von Reinkarnation und Karma, das ist das Wesentliche."
      ],
      [
        "Denn die Christus-Frage hat das Abendland in wahrhaftig tiefer Weise zu den verschiedensten Zeiten beschäftigt.",
        "Wir können dabei erinnern an die Zeiten der Gnosis, können erinnern an die Zeiten, in welchen sich vertieft hat das esoterische Christentum zum Beispiel derjenigen, die im Zeichen des Grals oder des Rosenkreuzes sich zusammengefunden ha­ben, wie sie vertieft haben die Christus-Frage."
      ],
      [
        "Also das ist nicht das Fundamentale.",
        "Fundamental, wesentlich wird die Frage für die abend-ländischen Gemüter, für die Erkenntnis und religiösen Bedürfnisse nur durch die Wahrheiten von Reinkarnation und Karma, so daß der, welcher eine Erweiterung seines Gemütes erfährt durch die Erkenntnis von Reinkarnation und Karma, auch notwendigerweise fordert eine neue Erkenntnis alter Fragen. - Was die Erkenntnis von Reinkarna­tion und Karma betrifft, so müssen wir das gerade Gegenteil davon sagen."
      ],
      [
        "Wir können höchstens darauf aufmerksam machen, daß Rein­karnation und Karma, man könnte sagen, sich schüchtern hereinfinden in die abendländische Kultur zur Zeit Lessings, der in seiner «Erziehung"
      ],
      [
        "des Menschengeschlechts» darauf kommt.",
        "Wir finden dann auch wei­tere Beispiele, wie tiefere Geister auf diese Frage kommen.",
        "Aber daß Reinkarnation und Karma als ein Bestandteil des menschlichen Be-wußtseins sich geltend machen, daß sie aufgenommen werden in Herz und Gemüt des Menschen so, wie es durch die Anthroposophie ge­schieht, das ist eben etwas, was erst in unserer Gegenwart wirklich ge­schehen kann.",
        "Daher könnte man sagen: Das Verhältnis eines Menschen der Gegenwart zur Anthroposophie charakterisiert sich darin, daß er in die Lage kommen kann, aus irgendwelchen Voraussetzungen heraus Reinkarnation und Karma als Erkenntnisse in sich aufzunehmen.",
        "Das ist das Wesentliche, worum es sich handelt.",
        "Im Grunde genommen folgt alles übrige dann in einer mehr oder weniger selbstverständlichen Weise daraus, ob sich der Mensch zu Reinkarnation und Karma in der ent­sprechenden Weise zu stellen vermag."
      ],
      [
        "Nun müssen wir uns, wenn wir die Frage so ins Auge fassen, auch klar werden, was es für die abendländische Menschheit und für die Menschheit überhaupt bedeutet, wenn Reinkarnation und Karma Er­kenntnisse werden, die sozusagen übergehen in die Alltäglichkeit, wie andere Wahrheiten in die Alltäglichkeit übergegangen sind.",
        "In einem noch viel größeren Umfange müssen in der nächsten Zeit Reinkarnation und Karma in das Bewußtsein der Menschheit übergehen, als dies zum Beispiel die kopernikanische Weltanschauung getan hat.",
        "In bezug auf die letztere brauchen wir uns nur einmal recht klarzumachen, wie sie eigentlich mit einem raschen Schritt sich eingelebt hat in die Gemüter der Menschen.",
        "Denken Sie nur an das, was ich auch im öffentlichen Vortrage gesagt habe: wie lange es erst in bezug auf weltgeschichtliche Verhältnisse her ist, daß diese kopernikanische Weltanschauung sich verbreitet hat, und denken Sie daran, daß bis in die niedersten Schulen hinein diese Weltanschauung die Menschen ergriffen hat."
      ],
      [
        "Nun gibt es einen bedeutsamen Unterschied in bezug auf das Ergrei­fen der Menschenseele zwischen dieser kopernikanischen Weltanschau­ung und der anthroposophischen Weltanschauung, insofern sich diese aufbaut auf dem Fundament von Reinkarnation und Karma.",
        "Um die­sen Unterschied zu charakterisieren, braucht man wahrhaftig einen anthroposophischen Zweig mit Menschen, die in gutem Willen zusammensitzen;"
      ],
      [
        "denn man muß eigentlich dabei ein Ding sagen, wenn man diesen Unterschied charakterisieren will, muß es notwendigerweise sagen, bei dem sich den außerhalb der anthroposophischen Bewegung stehenden Menschen wahrhaftig der Magen umdreht."
      ],
      [
        "Was gehörte denn dazu, daß die Menschen so schnell, so rasch und bis in das Kindheitsalter hinein die kopernikanische Weltanschauung angenommen haben?",
        "Die, welche mich über die kopernikanische Welt­anschauung oder über neuere Naturwissenschaft haben reden hören, die werden gewiß wissen, daß ich nicht irgendwie ein abträgliches Ur­teil fälle über diese moderne naturwissenschaftliche Anschauung."
      ],
      [
        "Da­her darf es schon gestattet sein, wenn man diesen betreffenden Unter­schied wirklich charakterisieren will, zu sagen: Um dieses Weltbild aufzunehmen, das rein auf eine Charakteristik des Raumes, auf äußere Raumverhältnisse beschränkt ist, war notwendig eine Epoche der Oberflächlichkeit! - Und der Grund, warum so schnell die koperni­kanische Weltanschauung sich eingelebt hat, ist kein anderer als der, daß die Menschen durch ein Zeitalter hindurch oberflächlich wurden.",
        "Oberflächlichkeit in der Auffassung der Welt war die notwendige Vor-bedingung für das Sich-Einleben der kopernikanischen Weltanschau­ung."
      ],
      [
        "Tiefe, Innerlichkeit - also gerade das Entgegengesetzte - wird notwendig sein, wenn sich einleben will, was die Wahrheiten der An­throposophie sind, und besonders in bezug auf die Grund- und Funda­mentalwahrheiten von Reinkarnation und Karma.",
        "Wenn wir uns daher heute die Überzeugung verschaffen, daß noch in einer viel, viel stärke­ren Weise und in einem viel größeren Umfange die Wahrheiten von Reinkarnation und Karma sich einleben müssen in die Menschheit, so müssen wir uns zugleich klar sein, daß wir in dieser Beziehung doch an der Grenze zweier Zeitalter stehen: des Zeitalters der Oberflächlich­keit - und des Zeitalters der notwendigen Vertiefung, der Verinner­lichung der Menschenseele und des Menschenherzens."
      ],
      [
        "Das ist es, was wir uns vor allen Dingen in die Seele schreiben müssen, wenn wir uns voll bewußt sein wollen, was Anthroposophie in der Gegenwart der modernen Menschheit zu bringen hat.",
        "Und dann müssen wir uns fra­gen: Wie wird sich denn dieses Leben gestalten müssen unter dem Ein­fluß der Erkenntnisse von Reinkarnation und Karma?"
      ],
      [
        "Da müssen wir nur bedenken, was es denn eigentlich für das Menschenherz ist, zu erkennen: Reinkarnation und Karma sind eine Wahrheit.",
        "Was ist es für das ganze menschliche Bewußtsein, für das ganze Fühlen und Denken der menschlichen Seele? - Nichts Geringeres ist es doch, das kann jeder einsehen, wenn er über diese Dinge nachdenkt, als eine Erweiterung des menschlichen Seibstes durch Wissen, durch Erkenntnis über gewisse Grenzen hinaus, die sonst dem Wissen und der Erkenntnis gezogen sind.",
        "Denn daß man nur dasjenige wissen und erkennen könne, was eingeschlossen ist zwi­schen Geburt und Tod, das wurde ja gerade im abgelaufenen Zeit­alter mit aller Schärfe betont, und daß man höchstens im Glauben aufschauen könne zu einem, der wissend hineingeht in eine geistige Welt, das war eine immer stärker werdende Überzeugung.",
        "Aber die Sache ist nicht von einer so großen Bedeutung, wenn man auf dem Erkenntnisstandpunkt stehenbleibt; sondern von Bedeutung wird sie erst, wenn man vom Erkenntnisstandpunkt übergeht zum morali­schen Standpunkt, zum gemüthaft-moralischen Standpunkt.",
        "Da erst zeigt sich die ganze Größe und Bedeutung der Ideen von Reinkarna­tion und Karma."
      ],
      [
        "Wir könnten Hunderte von Dingen anführen zur Erhärtung dessen, was jetzt gesagt worden ist, aber es soll nur das eine gesagt werden.",
        "Nehmen wir den Menschen der früheren Zeiten der abendländischen Kultur und die weitaus großte Anzahl der Menschen noch heute inner­halb der abendländischen Kultur.",
        "Selbst wenn diese Menschen noch im intensivsten Maße an der Annahme hängen, daß der Mensch in bezug auf seine Wesenheit intakt erhalten bleibt, wenn er durch die Pforte des Todes auf dieser Erde geschritten ist, so wird doch, ohne daß man an Reinkarnation und Karma denkt, dieses ganze an den Tod sich an­schließende geistige Leben des Menschen dem Erdendasein entzogen.",
        "Man hat es zu tun mit dem Betreten einer geistigen Welt; aber mit Ausnahme eben jener «Ausnahmen», die von den mehr oder weniger spiritualistisch angelegten Naturen geltengelassen werden, daß Abge­storbene in Ausnahmefällen hereinwirken, haben wir es - wenn Rein­karnation und Karma nicht gelten - mit einer Idee zu tun, daß das, was in einer geistigen Welt sich abspielt, sei es Strafe oder Belohnung,"
      ],
      [
        "wenn der Mensch durch die Pforte des Todes geschritten ist, der irdi­schen Sphäre als solcher entzogen ist, und daß sich das, was sich als Folge seines Lebens ergibt, auf einem ganz anderen, außerirdischen Schauplatze abspielt."
      ],
      [
        "Wenn der Mensch nun übergeht zur Erkenntnis von Reinkarnation und Karma, wird die Sache ganz anders.",
        "Da müssen wir uns klar sein, daß das, was für einen solchen Menschen in seiner Seele lebt, nicht bloß, wenn er durch die Pforte des Todes geschritten ist, eine Bedeutung hat für eine erdentrückte Sphäre, sondern daß von dem, was er erlebt zwischen Geburt und Tod, die Zukunft der Erdengestaltung abhängt.",
        "Die Erde wird sozusagen die äußere Konfiguration haben, welche die Menschen ihr geben, die vorher da waren.",
        "Der ganze Planet in seiner Zukunftskonfiguration, das Zusammenleben der Menschen in der Zu­kunft, hängt davon ab, wie die Menschen früher gelebt haben in ihren früheren Verleiblichungen.",
        "Das ist das Gemüthaft-Moralische, das sich an diese Ideen anknüpft; so daß ein Mensch, der dies angenommen hat, weiß: Wie ich war in dem Leben, so werde ich wirken auf alles, was in der Zukunft geschieht, auf die ganze Kultur der Zukunft! - Da er­weitert sich etwas mit dem Wissen von Reinkarnation und Karma über die Grenzen von Geburt und Tod hinaus, was der Mensch bisher nur in engsten Grenzen kennengelernt hat: das Verantwortlichkeitsgefühl!",
        "Da sehen wir herauswachsen ein gesteigertes Verantwortlichkeitsge­fühl.",
        "Darin prägt sich aus, was als eine tief bedeutsame moralische Folge auftritt von Ideen, wie es Reinkarnation und Karma sind.",
        "Der Mensch, der nicht an Reinkarnation und Karma glaubt, kann sagen:"
      ],
      [
        "Wenn ich durch die Pforte des Todes gegangen bin, werde ich höchstens bestraft oder belohnt für das, was ich hier getan habe; ich erfahre die Folgen dieses Daseins in einer anderen Welt; diese andere Welt steht aber unter dem Regiment irgendwelcher geistiger Mächte, und die wer­den schon verhindern, daß das, was ich in mir trage, gar zu schädlich werde der Gesamtwelt. - So kann der nicht mehr sagen, der da weiß, daß Reinkarnation und Karma eine erkenntnismäßig sich ergebende Idee ist; denn er weiß, daß die Menschen durch die Wiederverkörpe­rung so sein werden, je nach dem, wie sie in dem vorhergehenden Leben gelebt haben."
      ],
      [
        "Das wird das Bedeutsame und Wichtige sein, daß übergehen werden die Fundamentalideen der anthroposophischen Weltanschauung in das Gemütsieben und in die Gesinnung der Menschen und auftreten werden als moralische Impulse, von denen die Menschen in den abgelaufenen Zeiten im Grunde genommen gar keine Ahnung hatten.",
        "Das Verant­wortlichkeitsgefühl, haben wir gesehen, wird hervorsprießen in einer Weise, wie dies früher überhaupt nicht möglich war; und andere moralische Ideen werden sich notwendig dann in einer ähnlichen Weise ergeben wie dieses Verantwortlichkeitsgefühl.",
        "Wir werden als Menschen, die unter dem Einfluß der Ideen von Reinkarnation und Karma leben, wissen lernen, daß es sich nicht handeln kann um eine Beurteilung unseres Lebens bloß nach den Voraussetzungen, welche sich zwischen Geburt und Tod ausleben, sondern nach Voraussetzun­gen, welche über viele, viele Leben hin verbreitet sind."
      ],
      [
        "Wenn wir unter den Voraussetzungen, die es bisher gegeben hat, an den anderen Menschen herantreten, so entwickeln wir zu diesem an­deren Menschen Sympathie, Antipathie, größere oder geringere Liebe und dergleichen.",
        "Man muß sagen, die Art und Weise, wie sich Mensch zu Mensch stellt in der Gegenwart, ist doch in Wahrheit das Ergebnis jener Anschauung, die das Leben auf der Erde einmal eingeschlossen denkt zwischen Geburt und Tod.",
        "Wir leben in Wahrheit wirklich so, wie wir leben müßten, wenn es eben richtig wäre, daß der Mensch nur einmal auf der Erde da wäre.",
        "Wir können sagen: Wir begegnen unseren Freunden, Eltern, Geschwistern und so weiter so, daß bei allem, was wir fühlen und empfinden, das eben mitlebt, daß wir nur einmal auf der Erde sind.",
        "Und es wird eine ganz außerordentliche Umgestaltung des Lebens vor sich gehen, wenn nicht nur in einigen Köpfen, wie es heute noch vielfach der Fall ist, als Theorie das lebt, daß es Reinkar­nation und Karma gibt.",
        "Bis heute ist es im weitesten Umfange noch Theorie.",
        "Man kann sagen, heute ist es so, daß es eine Anzahl Anthro­posophen gibt, die glauben an Reinkarnation und Karma; aber sie leben so, als wenn es Reinkarnation und Karma nicht gäbe, sondern als wenn das Leben einmal eingeschlossen wäre zwischen Geburt und Tod.",
        "Das kann auch nicht anders sein.",
        "Denn die Gewohnheiten, die das Leben mit sich bringt, ändern sich weniger rasch, als die Ideen sich ändern.",
        "Wenn"
      ],
      [
        "wir richtige und konkrete Ideen über Reinkarnation und Karma - nur um diese kann es sich handeln - in unser Leben einführen, dann erst werden wir sehen, wie dieses Leben befruchtet werden kann durch solche Ideen."
      ],
      [
        "Wir sehen, daß wir als Menschen hereintreten in das Leben, indem wir im Beginne desselben zusammenkommen mit Eltern, mit Geschwi­stern und so weiter.",
        "Wir sehen, daß wir durch diese Natureinrichtung notwendigerweise in der ersten Zeit unseres Lebens vorzugsweise so in demselben drinnenstehen, daß die, welche um uns herum sind, mehr oder weniger durch Naturelemente um uns herum gestellt sind: durch Blutsverwandtschaft, Nähe des Ortes und so weiter.",
        "Dann sehen wir, wenn wir heranwachsen, wie diese Kreise der Blutsverwandtschaft sich erweitern, wie wir in ganz andere, nicht mehr von Blutsverwandt­schaft abhängige Verbindungen mit diesen oder jenen Menschen treten.",
        "Nun handelt es sich darum, daß diese Dinge erst karmisch eingesehen werden müssen; dann werden sie eine ganz neue Beleuchtung für das Leben gewinnen.",
        "Denn Karma wird erst bedeutungsvoll für das Leben, wenn wir es konkret fassen, wenn wir wirklich auf das Leben anwen­den, was die geisteswissenschaftliche Forschung ergibt.",
        "Festgestellt wer­den kann das selbstverständlich nur von der geisteswissenschaftlichen Forschung, kann aber dann auf das Leben angewendet werden."
      ],
      [
        "Eine bedeutungsvolle karmische Frage ist im wesentlichen diese: Wie kommt es denn, daß wir zum Beispiel im gegenwärtigen Leben mit den Menschen zusammenkommen, mit denen wir auf die ja jedem begreif­liche Weise durch die Blutsverwandtschaft zusammenkommen?",
        "Warum kommen wir mit diesen im Beginne dieses Lebens zusammen? - Nun zeigt die geisteswissenschaftliche Forschung über diese Frage etwas sehr Eigentümliches.",
        "In der Regel ist es so - denn wenn auch einzelne Tatsachen angegeben werden, gibt es doch wieder unzählige Aus­nahmen -, daß wir mit den Menschen, die wir unwillkürlich treffen im Beginne unseres Lebens, schon in einem vorhergehenden Leben zu­sammen waren, meistens sogar in dem unmittelbar vorhergehenden, in der Mitte unseres Lebens, so in den Dreißigerjahren.",
        "Da haben wir sie uns in irgendeiner Weise freiwillig gewählt, indem wir zu ihnen hin-getrieben waren durch unsere Herzensneigung und so weiter.",
        "Wir würden"
      ],
      [
        "ganz fehl gehen, wenn wir die Menschen, mit denen wir im Beginne unseres Lebens zusammenkommen, als solche betrachten würden, mit denen wir auch wieder im Beginne eines anderen Lebens zusammen wa­ren.",
        "Nicht am Anfange, nicht am Ende, sondern in der Mitte eines Lebens waren wir durch freiwillige Wahl mit jenen zusammen, mit denen wir dann in einem folgenden Leben zusammentreffen durch Blutsverwandtschaft.",
        "Sehr häufig sind die Fälle so, daß man zu dem, mit dem man verheiratet war, den man sich also durch freie Wahl ge­nommen hat, im nächsten Leben im Vater- oder Mutterverhältnis oder im Geschwisterverhältnis steht.",
        "Die geisteswissenschaftliche Forschung zeigt, daß das, was man aus der Spekulation voraussetzen würde, was man denken würde, wenn man etwas ausspintisiert über die Dinge, gewöhnlich falsch ist.",
        "Die Tatsachen machen gewöhnlich einen Strich durch die Rechnung der Spekulation."
      ],
      [
        "Denken wir nur einmal diese jetzt geschilderte Tatsache und fassen wir sie so auf, wie sie sich wirklich, wenn man vorurteilsfrei forscht, aus der Geisteswissenschaft ergibt, wie sie wieder unser ganzes Verhält­nis und unsere ganze Beziehung zum Leben erweitert.",
        "Es ist ja nach und nach im Verlaufe der abendländischen Kultur dazu gekommen, daß der Mensch eigentlich jetzt schon gar nicht mehr anders kann, als von Zufall zu reden, wenn er nachdenkt über sein Verhältnis zu den­jenigen, mit denen er blutsverwandt ist.",
        "Man redet von Zufall, man glaubt auch vielfach schon an den Zufall.",
        "Wie sollte man denn an etwas anderes glauben als an Zufall, wenn man das Leben nur einmal einge­schlossen denkt zwischen Geburt und Tod.",
        "Für das eine Leben wird man selbstverständlich zugeben, daß man verantwortlich ist für die Folgen der Ereignisse, die man selbst herbeigeführt hat.",
        "Indem man sein eigenes Selbst hinüberführt über das, was sich abspielt zwischen Ge­burt und Tod, indem man sein Selbst verbunden fühlt mit anderen Menschen der anderen Verkörperung, fühlt man sich verantwortlich wie hier im Leben seinen eigenen Taten gegenüber.",
        "Es werden immer mehr und mehr die Menschen diese konkreten Tatsachen erfahren müs­sen.",
        "Die allgemeine Idee, wenn man sagt, der Mensch habe sich im Sinne des Karma seine Eltern selber gewählt, gibt noch nichts Beson­deres.",
        "Aber man bekommt eine Vorstellung von dieser Wahl, die wirklich"
      ],
      [
        "nun durch alle übrigen Erfahrungen des Lebens bekräftigt werden kann, wenn man weiß: Die, welche du dir jetzt am allerunbewußtesten gewählt hast, die hast du dir in einem früheren Leben in einem Zeit­punkte deiner größten Bewußtheit gewählt, wo du am allerreifsten warst."
      ],
      [
        "Das mag manchem vielleicht heute unangenehm sein, aber wahr ist es doch.",
        "Denn man wird lernen, wenn man mit seinen Blutsverwandten nicht zufrieden ist, daß man eben zu dieser Unzufriedenheit selber den Grund gelegt hat, daß man also für die nächste Inkarnation wird anders vorsorgen müssen; und dann wird schon die Idee von Reinkarnation und Karma fruchtbar werden für das Leben.",
        "Und das ist es ja, daß diese Ideen nicht für die Befriedigung irgendeiner Neugierde und so weiter, sondern für unsere Vervollkommnung und damit für die Ver­vollkommnung des ganzen Lebens gelten.",
        "Und weiter werden wir wis­sen, daß das, was gesagt worden ist, etwas Ähnliches für das gegen­wärtige Leben und dessen Folgen nach sich zieht; daß diejenigen, mit denen wir in den Dreißigerjahren zusammengeführt werden, wo wir also mit unserem vollen Verstande zu urteilen glauben, durchaus so mit uns verbunden werden, daß sie in einem nächsten Leben uns gleich am Ausgangspunkte, vielleicht als Eltern oder Geschwister, entgegentreten werden.",
        "Wenn wir wissen, was davon abhängt, daß sich Familienkon­figurationen bilden, daß diese oder jene Leute zusammenkommen, so wird sich unser Verantwortlichkeitsgefühl unter den Ideen von Rein­karnation und Karma bedeutsam erweitern."
      ],
      [
        "Ich sagte, daß wir betonen können, daß diese Dinge sich als begreif­lich im Leben erweisen.",
        "Müssen nicht die Kräfte, die eine Menschen-individualität herunterbringen in eine Familie, ganz bedeutende, starke sein?",
        "Stark können sie aber nicht sein in dem Menschen, der jetzt ver­körpert wird; denn da können sie nicht viel zu tun haben mit den Welten, in die er herunterkommt.",
        "Muß es nicht begreiflich sein, daß die Kräfte, die im Tiefsten der Seele wirken, aus Zeiten stammen müssen des vergangenen Lebens, wo mit der starken Kraft der Freundschaft, der «bewußten Liebe», wenn man es so nennen darf, die Zusammen­hänge von uns herbeigeführt wurden?",
        "Was als bewußte Kräfte in dem einen Leben gewaltet hat, das wirkt als unbewußte Kräfte in dem"
      ],
      [
        "nächsten Leben; was auf mehr oder weniger unbewußte Art geschieht, das erklärt sich auf diese Weise."
      ],
      [
        "Allerdings ist es notwendig, daß man sich die Tatsachen der For­schung nicht trübt, weil diese Tatsachen der Forschung fast immer einen Strich durch die Spekulation machen, so daß man nur hinterher die Logik in den Tatsachen finden kann.",
        "Man soll sich nicht verleiten lassen, durch Spekulation vorgehen zu wollen; denn da wird man nicht zu dem richtigen Gesichtspunkt kommen, sondern immer zu etwas Ähnlichem, was sich charakterisieren läßt durch jenes Gespräch, das ich auch schon erzählte.",
        "In einer süddeutschen Stadt nämlich sagte mir einmal ein Theologe: Ich habe Ihre Schriften gelesen und habe gesehen, daß sie so logisch sind; daher habe ich mir gedacht, wenn sie so logisch sind, so kann ihr Verfasser vielleicht auch auf dem Wege der bloßen Logik dazu gekommen sein. - Wenn ich mich also bemüht hätte, weniger «logisch» zu schreiben, so würde ich mir damit ein Verdienst erworben haben in den Augen des betreffenden Theologen, weil er dann gesehen haben würde, daß die Darstellungen nicht durch bloße Logik gefunden worden sind.",
        "Wer aber auf die Schriften eingeht, der wird sehen, daß die logischen Formen ihnen nachher gegeben sind, daß sie aber nicht durch Logik gefunden worden sind.",
        "Ich wenigstens könnte es nicht, das versichere ich Ihnen.",
        "Vielleicht könnten es andere durch bloße Logik finden."
      ],
      [
        "Wenn wir die Dinge so ansehen, erweist es sich als eine tief bedeut­same Idee, daß die wichtigsten Impulse, die aus der Anthroposophie hervorgehen müssen, moralisch-gemüthafte Impulse sein müssen.",
        "Wir haben heute das Verantwortlichkeitsgefühl auf verschiedenen Gebieten hervorgehoben.",
        "Wir könnten ebenso Liebe, Mitleid verfolgen, die alle verschiedene Formen annehmen unter dem Einfluß der Ideen von Re­inkarnation und Karma.",
        "Aus diesem Grunde war es auch, warum wir im Verlaufe der Jahre so sehr Wert darauf gelegt haben, selbst bis in die öffentlichen Vorträge hinein, Anthroposophie immer mit Bezug auf das Leben, mit Bezug auf die unmittelbarsten Erscheinungen des Le­bens zu betrachten.",
        "So haben wir gesprochen über die Mission des Zor­nes, über das menschliche Gewissen, über das Gebet, über die Erziehung des Kindes, über die verschiedenen Lebensalter des Menschen - und"
      ],
      [
        "haben alle diese Dinge in das Licht gerückt, in das sie gerückt werden müssen, wenn man die Ideen von Reinkarnation und Karma als die richtigen voraussetzt.",
        "Und da hat sich uns ergeben, wie umgestaltend diese Ideen von Reinkarnation und Karma in das Leben eingreifen."
      ],
      [
        "Das hat ja im Grunde genommen den Hauptteil unserer Betrachtungen ausgemacht, daß wir die fundamentalen Ideen in ihrer Wirkung für das Leben betrachtet haben.",
        "Wenn auch nicht immer, ich möchte sa­gen, mit abstrakten Worten aus Reinkarnation und Karma die Be­deutung hergeleitet wird, die zum Beispiel Gemütseigenschaften, oder das Gewissen, der Charakter, das Gebet erfahren, wenn das auch nicht immer so hergeleitet wird, daß man sagt: Wenn man Reinkarnation und Karma annimmt, dann ergibt sich - und so weiter, so standen doch alle unsere Betrachtungen unter dem Impuls von Reinkarnation und Karma."
      ],
      [
        "Und das wird das Bedeutsame sein für die nächste Gegen­wart, daß nicht nur die Seelenwissenschaft eine Beeinflussung erfahren wird durch die Ideen von Reinkarnation und Karma, sondern auch die anderen Wissenschaften.",
        "Wenn Sie einen solchen Vortrag verfolgen wie den letzten öffentlichen: «Der Tod bei Mensch, Tier und Pflanze», so werden Sie sehen, daß es sich darum handelte zu zeigen, wie die Men­schen denken lernen werden über den Tod bei Pflanze, Tier und Mensch, wenn sie in sich selbst das sehen, was über das einzelne Leben des Menschen hinausgeht."
      ],
      [
        "Wir kamen auf die Bedeutung des Todes bei Mensch, Tier und Pflanze dadurch, daß wir uns klar wurden:"
      ],
      [
        "Anders lebt das Selbst im Menschen, anders beim Tier und wieder anders bei den Pflanzen.",
        "Beim Menschen ist es ein individuelles Ich, bei den Tieren ist es die Gruppenseele, und bei den Pflanzen haben wir es mit einem Teil des ganzen Planetenseelensystems zu tun.",
        "Dadurch faßten wir bei den Pflanzen als ein bloßes Einschlafen und Aufwachen auf, was uns als Tod und Entstehen äußerlich entgegentritt.",
        "Bei den Tieren ist es wieder anders; da ist es ähnlich wie in uns selber, indem das Selbst in einer Inkarnation vorrückt, gewisse Instinkte und so weiter überwindet.",
        "Aber erst beim Menschen, der selbst seine Verkör­perungen herbeiführt, waren wir uns klar, daß erst der Tod die Ge­währ bietet für die Unsterblichkeit, und daß das Wort Tod in dieser Bedeutung nur beim Menschen so gebraucht werden dürfte, oder daß"
      ],
      [
        "wir, wenn wir das Wort Tod allgemein gebrauchen, hervorheben müß­ten, wie der Mensch, wie das Tier und wie die Pflanze stirbt, und daß wir ein ganz neues Wort gebrauchen müßten bei Tier und Pflanze."
      ],
      [
        "Alles andere in der Anthroposophie ist ein solches, daß die Menschen-seele fordert, etwas zu erfahren über diese oder jene Dinge; aber es macht sozusagen das «Andere» im Grunde genommen gar nicht den Anthroposophen aus.",
        "Zu gewissen Dingen kommt er schon, wenn es Zeit ist.",
        "Wenn er zunächst in der Lage ist, die Ideen von Reinkarnation und Karma in dem Sinne aufzunehmen, wie wir sie geben müssen im Unterschiede von älteren Ideen von Reinkarnation und Karma, wie zum Beispiel im Buddhismus, so kommt der Mensch im Ver­laufe der Forschung ganz von selbst schon zu anderen Dingen.",
        "Daher war der Hauptteil unserer Arbeit dem gewidmet, den Einfluß von Reinkarnation und Karma auf das gesamte Menschenleben ins Auge zu fassen."
      ],
      [
        "In dieser Beziehung sollte es klar sein, daß die Arbeit innerhalb ir­gendwelcher anthroposophischer Vereinigung oder Gesellschaft im Sinne dieser Mission der Anthroposophie aufgefaßt werden müßte.",
        "Da­her ist es begreiflich, daß wir im Grunde genommen über diejenigen Fragen, welche dem Außenstehenden, dem von der Anthroposophie als solcher weniger Berührten, vielleicht zunächst als die wichtigsten erscheinen, eigentlich nur reden, wenn wir eben von den Grundwahr­heiten aufsteigen wollen zu denjenigen Dingen, die jeder Seele, weil sie eine abendländische Seele ist, am nächsten sind.",
        "Es wäre durchaus der Fall denkbar, daß man das Neue, was heute als das fundamental Neue charakterisiert worden ist, von der Anthroposophie aufnehmen würde und sich zunächst gar nicht kümmerte um irgendwelche religiösen Ge­gensätze der Menschen.",
        "Denn das ist gar nicht das Charakteristische dieser neuen Geisteswissenschaft, daß etwa vergleichende Religions­wissenschaft getrieben würde; wenn das zwar heute auch getrieben wird, genug sogar.",
        "Aber gegenüber dem, was sonst heute da getan wird, ist das, was bei den Theosophen getrieben wird, gar nicht das Geist-reichere.",
        "Das ist aber das Bedeutsame, daß in der Anthroposophie alle diese Dinge in das Licht gerückt werden. das von den Ideen von Rein­karnation und Karma ausgeht."
      ],
      [
        "Namentlich wird noch in einer anderen Beziehung das Verantwort­lichkeitsgefühl unter dem Einfluß von Reinkarnation und Karma ganz beträchtlich wachsen.",
        "Wenn wir nur einmal auf das sehen, was heute gesagt worden ist über das Verhältnis von Blutsverwandten zu frei gewählten Menschen, so sehen wir schon, daß ein gewisser Gegensatz besteht: Was in einem Leben das Innerlichste, das Verborgenste an Im­pulsen ist, das ist in dem anderen das Offenbarste."
      ],
      [
        "Wenn wir unsere tiefsten Freundschaftsgefühle in der einen Inkarnation Menschen ent­gegenbringen, so bereiten wir dadurch wohl vor eine äußere Verwandt­schaft, eine Blutsverwandtschaft oder dergleichen.",
        "Ähnlich ist es auf einem anderen Gebiete."
      ],
      [
        "Die Art, wie wir über irgend etwas denken, was uns als das Unwirklichste in dieser Inkarnation erscheint, das wird uns das Maßgebendste, das die eigentlichen Impulse für die nächste In­karnation Bedingende sein.",
        "Die Art, wie wir denken, ob wir uns leich­ten Herzens einer Wahrheit hingeben, oder ob wir mit allen Mitteln, die uns zur Verfügung stehen, prüfend uns an eine Wahrheit heran-machen, ob wir Wahrheitssinn oder Fanatismus haben, das tritt in ein ganz anderes Verhältnis zur menschlichen Entwickelung durch das Sich-Einleben in die Ideen von Reinkarnation und Karma, als es heute der Fall ist."
      ],
      [
        "Denn, was wir nur in unserem Innersten haben in der ge­genwärtigen Inkarnation, das werden wir am offenbarsten haben in der nächsten.",
        "Und wer viel lügt oder Neigung hat, leichten Herzens dieses oder jenes anzunehmen, der wird ein leichtsinniger Mensch wer­den in der nächsten oder einer nächsten Inkarnation; denn, was wir denken, wie wir denken, wie wir uns zur Wahrheit stellen, was also in dieser Inkarnation innerlich ist, das wird das Maß des Verhaltens in unserer nächsten Inkarnation bilden."
      ],
      [
        "Wenn wir zum Beispiel, ohne daß wir sehr genau prüfen, in dieser Inkarnation einen Menschen für einen schlechten halten, während er sich, wenn wir ihn genau prüfen würden, vielleicht als ein guter oder höchstens als ein halbguter erweisen würde, wenn wir diesen Gedanken ungeprüft durch das Leben tragen, so wird sich herausstellen, daß wir, indem wir uns in dieser Weise Urteile bilden über Menschen, unverträgliche, zänkische, abscheuliche Menschen wer­den in der nächsten Inkarnation!",
        "Da haben wir wieder eine Erweite­rung des moralisch-gemüthaften Elementes in unsere Seele."
      ],
      [
        "Das ist außerordentlich wichtig, daß wir solche Dinge recht sehr ins Auge fassen, und daß wir uns einmal mit dem Gedanken bekannt­machen, welche fundamentale Bedeutung es hat, in sein Innerstes, in sein ganzes Gemüt das aufzunehmen, was nun wirklich als Neues und alles andere dadurch in einer gewissen Weise Erneuernde in die geistige Entwickelung der Gegenwart mit den Ideen von Reinkarnation und Karma hereintritt.",
        "Daher ist es, daß wir darauf den Hauptwert legten in dem ganzen Verlauf unserer anthroposophischen Bewegung, und daß wir gewissermaßen andere Fragen, die gewiß mit Notwendigkeit sich aus diesen ergeben, auch nur in dieser Weise behandeln, wie das sich notwendig ergeben muß."
      ],
      [
        "Daher könnte zum Beispiel unsere Eigenart, unsere ganze Art und Weise, wie Anthroposophie in unserer Mitte ge­trieben wird, wenn die Dinge in Wahrheit dargestellt werden, wie wir es machen, niemals als im Gegensatze zu einer Bewegung aufgefaßt wer­den, welche Reinkarnation und Karma in den Mittelpunkt der Be­trachtungen stellt.",
        "Der Gegensatz zu uns muß immer von außen kon­struiert werden; es ist unmöglich, daß er sich ergeben kann, wenn man die Dinge, die in unserer Mitte geschehen, wirklich richtig darstellt."
      ],
      [
        "Wir brauchen nur das eine Moment ins Auge zu fassen: Wie wenig wird eigentlich über die Christus-Frage in unserer Mitte gesprochen!",
        "Da darf niemand das, was gesagt wird, deshalb vergrößern, weil er es für sein Herz als besonders wichtig empfindet, sondern er muß es ob­jektiv betrachten; so daß niemand einen Grund hat, weil dieses oder jenes als notwendige Folge für das gereifte Begreifen von Reinkarna­tion und Karma sich ergibt, zu sagen, daß wir viel über die Christus-Frage sprechen."
      ],
      [
        "Denn das ist nicht das Fundamentale, was den An­throposophen in der Gegenwart ausmacht, sondern das ist es, was neu in die Welt hereintritt, und daß das, was neu hereintritt, wirklich von der Menschheit aufgenommen wird.",
        "So also müßten wir dies verstehen, daß es eigentlich nur durch eine unrichtige, oder unter der Voraus­setzung einer unrichtigen Darstellung der Art und Weise, wie wir die Dinge hier treiben, möglich wäre, einen Gegensatz zu konstruieren; denn der muß immer von außen zu uns konstruiert werden."
      ],
      [
        "Man kann Gegner sein von uns, aber wir brauchen nicht irgendeine Gegnerschaft zu konstruieren; denn das Sich-nicht-Kümmern um etwas, bedeutet"
      ],
      [
        "nicht eine Gegnerschaft, sonst müßte man ein Gegner sein von allem, worum man sich nicht kümmert!"
      ],
      [
        "Das wollte ich Ihnen besonders an die Seele legen: daß wir nach­denken, was das Fundamentale, was das Neue an der Anthroposophie eigentlich ausmacht.",
        "Selbstverständlich soll damit nicht gesagt sein:"
      ],
      [
        "Eine anthroposophische Gesellschaft ist die, welche an Reinkarnation und Karma glaubt.",
        "Sondern es soll damit gesagt sein: So wie einmal eine Zeit reif geworden ist, um die kopernikanische Weltanschauung aufzunehmen, so ist unsere Zeit reif geworden, die Lehre von Rein­karnation und Karma zum allgemeinen Bewußtsein der Menschheit zu bringen.",
        "Und was geschehen soll im Verlaufe der Menschheitsentwicke­lung, das wird geschehen, wie viele Mächte sich auch dagegen erheben.",
        "Und mit Reinkarnation und Karma, mit dem wirklichen Begreifen von Reinkarnation und Karma werden sich alle anderen Dinge von selbst ergeben.",
        "Die anderen Dinge ergeben sich durch das Licht, das von Rein­karnation und Karma ausstrahlt."
      ],
      [
        "Es war gewiß einmal ganz nützlich, betrachtet zu haben, was eigent­lich das fundamental Unterscheidende ist zwischen denjenigen, die sich an der Anthroposophie interessiert fühlen, und denjenigen, die ihre Gegnerschaft gegen sie entwickeln.",
        "Das Annehmen einer höheren Welt als solches ist es eigentlich nicht; sondern das ist es, was die Vorstel­lungen an Höherem erfahren durch die Voraussetzung der Ideen von Reinkarnation und Karma.",
        "Damit haben wir heute etwas angegeben, was als das Wesentliche der anthroposophischen Weltanschauung an­gesehen werden kann."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Die in den Vorträgen genannten geschriebenen Werke von Rudolf Steiner sind alle innerhalb der Gesamtausgabe erschienen. Siehe die Übersicht am Schlusse des Bandes.",
      "9    die Betrachtungen, die wir im Herbst gepflo gen haben: Siehe Rudolf Stei­ner, «Die Evolution vom Gesichtspunkte des Wahrhaftigen», 5 Vorträge in",
      "Berlin vom 31.Oktober bis 5. Dezember 1911, Bibliographie-Nr. 132,",
      "Gesamtausgabe Dornach 1969.",
      "mit Anthroposophie beschäftigt hat: Die seinerzeit in den Vorträgen ge­brauchten Worte «Theosophie» und «theosophisch», die Rudolf Steiner brauchte im Sinne seiner anthroposophisch orientierten Geisteswissenschaft (Anthroposophie), sind hier, um Mißverständnisse zu vermeiden, durch «Anthroposophie» und «anthroposophisch» ersetzt.",
      "11    in der kleinen Schrift «Reinkarnation und Karma, vom Standpunkte der modernen Naturwissenschaft notwendige Vorstellungen>: Berlin 1903, in «Luzifer-Gnosis 1903-1908», Bibliographie-Nr. 34, Gesamtausgabe Dorn-ach 1960; auch als Einzelausgabe.",
      "15    Der früh verstorbene Mathematiker Abel: Niels Henrik Abel, 1802-1829,",
      "Mathematiker, berühmt durch die Begründung der Theorie der elliptischen",
      "Funktionen und die allgemeine Theorie der Integrale algebraischer",
      "Funktionen.",
      "So ist mir eine Persönlichkeit bekannt: Es ist nicht bekannt, wen Rudolf Steiner hier im Auge hatte.",
      "in der nächsten inkarnation in innere Organbildung eingeht: Siehe Ru­dolf Steiner, «Entsprechungen zwischen Mikrokosmos und Makrokosmos",
      "- Der Mensch, eine Hieroglyphe des Weltenalls», 16 Vorträge, Dornach, 9. April bis 16. Mai 1920, Bibliographie-Nr. 201, Dornach 1958.",
      "30 Otto von Bismarck, 1815-1898, «Gedanken und Erinnerungen«.",
      "33 u. 49    Friedrich Hebbel: Siehe Friedrich Hebbel, Sämtliche Werke, besorgt von Richard Maria Werner, Berlin 1901 ff., 2. Abtlg.: Tagebücher. 1. Bd., Seite 392, Nr.1745: «Nach der Seelenwanderung ist es möglich, daß Plato jetzt wieder auf einer Schulbank Prügel bekommt, weil er den Plato nicht versteht~»",
      "33    Was tragen wir für einen Inhalt in unserem Seelenleben mit uns herum:",
      "Siehe hierzu Rudolf Steiner, «Anthroposophie, Psychosophie, Pneumato­sophie», 12 Vorträge, Berlin 1909-1911. Bibliographie-Nr. 115. Gesamt­ausgabe Dornach 1965.",
      "35    Arthur Schopenhauer, 1788-1860.",
      "38/41    das Beispiel ist von mir... auch anderswo erzählt worden   so ergeht der Ruf von der Individualität, von der wir noch sprechen werden: Siehe Rudolf Steiner, «Das esoterische Christentum und die geistige Führung der Menschheit», Bibliographie-Nr. 130, Gesamtausgabe Dornach 1962.",
      "59    «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft»:",
      "Berlin 1907, in «Luzifer-Gnosis 1903-1908«, Bibliographie-Nr. 34, Ge­samtausgabe Dornach 1960; auch als Einzelausgabe.",
      "67    daß man für dasjenige, was man unmittelbar als Arbeit leistet, einen der Arbeit entsp rechenden Lohn, der die Arbeit geradezu bezahlt, einheimsen müsse: Siehe Rudolf Steiner, «Geisteswissenschaft und soziale Frage», Drei Aufsätze, Berlin 1905/06, in «Luzifer-Gnosis 1903-1908», Biblio­graphie-Nr. 34, Gesamtausgabe Dornach 1960; auch als Einzelausgabe.",
      "70    . sein Werk... dem Papst gewidmet hat: Nikolaus Koper­nikus, 1473-1543. Sein schon viel früher ver      er « e revolutioni-bus orbium coelestium libri VI», gewidmet Papst Paul III., gelangte erst 1543 in Nürnb erg zum Druck. Zunächst durch die Widmung an den Papst geschützt, kam das Werk jedoch 1615 auf den Index .Bei den Einschrän­kungen von 1757 wurde es nicht vom Index entfernt; erst 1822 wurde es gestrichen, als das Sacrum Officium erklärte, daß die Herausgabe von Werken, welche von der Bewegung der Erde und dem Stillstand der Sonne handeln, nicht verboten sei.",
      "seit dem Foucaultschen Pendelversuch: Der Physiker Léon Foucault, 1819 bis 1868, demonstrierte im Jahre 1851 im Panthéon zu Paris die Drehung der Erde durch ein freischwingendes Pendel.",
      "71    daß mir diese Erkenntnis von der Erdbewegung, als ich ein kleiner Bub war: Siehe «Mein Lebensgang». Bibliographie-Nr. 28, Gesamtausgabe Dorn-ach 1962.",
      "72    Die Erde . . . ist ein Staubkorn im Weltenall den anderen Welten gegen­über: Ein von Herbert Spencer, 1820-1903, geprägtes Wort.",
      "84    anthroposophische Bewegung - in unseren Gedanken wenigstens - scharf zu trennen von irgendeiner gesellschaftlichen Einrichtung: Einen dem Geist der anthroposophischen Bewegung entsprechenden Gesellschaftsorga­nismus zu bild en, war für Rudolf Steiner ein Hauptanliegen. Zu Weih­nachten 1923 versuchte er dies bei der Neubegründung der Allgemeinen Anthroposophischen Gesellschaft, indem er deren Vorsitz übernahm. Siehe Rudolf Steiner",
      "Dornach 1963.",
      "86    daß es luziferische Kräfte und Wesenheiten gibt: Siehe Rudolf Steiner «Die Geheimwissenschaft im Umriß», Bibliographie-Nr. 13, Gesamtaus­gabe Dornach 1968.",
      "89 f. Lessings «Erziehung des Menschengeschlechts»: Erschienen 1780.",
      "90    im öffentlichen Vortrage: «Kopernikus und seine Zeit im Lichte der Geisteswissenschaft», Berlin, 15. Februar 1912, in «Menschengeschichte im Lichte der Geistesforschung», 16 Vorträge, 19. Oktober 1911 bis 28. März 1912. Bibliographie-Nr. 61, Gesamtausgabe Dornach 1962.",
      "98    So haben wir gesprochen über die Mission des Zornes, über das mensch­liche Gewissen, über das Gebet: Siehe Rudolf Steiner, «Metamorphosen",
      "des Seelenlebens», 7 Vortrage, Berlin 1909/10, Bibliographie - Nr . 59, Ge­samtausgabe Dornach 1957, sowie «Pfade der Seelenerlehnisse», 8 Vor­träge, Berlin 1909/10, Bibliographie-Nr. 58, Gesamtausgabe Dornach 1957.",
      "99    Wenn Sie einen solchen Vortrag verfolgen wie den letzten öffentlichen:",
      "«Der Tod bei Mensch, Tier und Pflanze», Vortrag vom 29. Februar 1912,",
      "in «Menschengeschichte im Lichte der Geistesforschung», 16 Vorträge,",
      "Berlin 1911/12, Bibliographie-Nr. 61, Gesamtausgabe Dornach 1962.",
      "102    Der Gegensatz zu uns . . .: Rudolf Steiner bezieht sich hier auf die da­malige Auseinandersetzung mit der Theosophischen Gesellschaft. Vgl. «Die Geschichte und die Bedingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesellschaft», Bibliographie-Nr. 258, Gesamtausgabe Dornach 1959."
    ],
    "sentences": [
      [
        "Die in den Vorträgen genannten geschriebenen Werke von Rudolf Steiner sind alle innerhalb der Gesamtausgabe erschienen.",
        "Siehe die Übersicht am Schlusse des Bandes."
      ],
      [
        "9 die Betrachtungen, die wir im Herbst gepflo gen haben: Siehe Rudolf Stei­ner, «Die Evolution vom Gesichtspunkte des Wahrhaftigen», 5 Vorträge in"
      ],
      [
        "Berlin vom 31.Oktober bis 5.",
        "Dezember 1911, Bibliographie-Nr. 132,"
      ],
      [
        "Gesamtausgabe Dornach 1969."
      ],
      [
        "mit Anthroposophie beschäftigt hat: Die seinerzeit in den Vorträgen ge­brauchten Worte «Theosophie» und «theosophisch», die Rudolf Steiner brauchte im Sinne seiner anthroposophisch orientierten Geisteswissenschaft (Anthroposophie), sind hier, um Mißverständnisse zu vermeiden, durch «Anthroposophie» und «anthroposophisch» ersetzt."
      ],
      [
        "11 in der kleinen Schrift «Reinkarnation und Karma, vom Standpunkte der modernen Naturwissenschaft notwendige Vorstellungen>: Berlin 1903, in «Luzifer-Gnosis 1903-1908», Bibliographie-Nr. 34, Gesamtausgabe Dorn-ach 1960; auch als Einzelausgabe."
      ],
      [
        "15 Der früh verstorbene Mathematiker Abel: Niels Henrik Abel, 1802-1829,"
      ],
      [
        "Mathematiker, berühmt durch die Begründung der Theorie der elliptischen"
      ],
      [
        "Funktionen und die allgemeine Theorie der Integrale algebraischer"
      ],
      [
        "Funktionen."
      ],
      [
        "So ist mir eine Persönlichkeit bekannt: Es ist nicht bekannt, wen Rudolf Steiner hier im Auge hatte."
      ],
      [
        "in der nächsten inkarnation in innere Organbildung eingeht: Siehe Ru­dolf Steiner, «Entsprechungen zwischen Mikrokosmos und Makrokosmos"
      ],
      [
        "- Der Mensch, eine Hieroglyphe des Weltenalls», 16 Vorträge, Dornach, 9.",
        "April bis 16.",
        "Mai 1920, Bibliographie-Nr. 201, Dornach 1958."
      ],
      [
        "30 Otto von Bismarck, 1815-1898, «Gedanken und Erinnerungen«."
      ],
      [
        "33 u. 49 Friedrich Hebbel: Siehe Friedrich Hebbel, Sämtliche Werke, besorgt von Richard Maria Werner, Berlin 1901 ff., 2.",
        "Abtlg.: Tagebücher. 1.",
        "Bd., Seite 392, Nr.1745: «Nach der Seelenwanderung ist es möglich, daß Plato jetzt wieder auf einer Schulbank Prügel bekommt, weil er den Plato nicht versteht~»"
      ],
      [
        "33 Was tragen wir für einen Inhalt in unserem Seelenleben mit uns herum:"
      ],
      [
        "Siehe hierzu Rudolf Steiner, «Anthroposophie, Psychosophie, Pneumato­sophie», 12 Vorträge, Berlin 1909-1911.",
        "Bibliographie-Nr. 115.",
        "Gesamt­ausgabe Dornach 1965."
      ],
      [
        "35 Arthur Schopenhauer, 1788-1860."
      ],
      [
        "38/41 das Beispiel ist von mir... auch anderswo erzählt worden so ergeht der Ruf von der Individualität, von der wir noch sprechen werden: Siehe Rudolf Steiner, «Das esoterische Christentum und die geistige Führung der Menschheit», Bibliographie-Nr. 130, Gesamtausgabe Dornach 1962."
      ],
      [
        "59 «Die Erziehung des Kindes vom Gesichtspunkte der Geisteswissenschaft»:"
      ],
      [
        "Berlin 1907, in «Luzifer-Gnosis 1903-1908«, Bibliographie-Nr. 34, Ge­samtausgabe Dornach 1960; auch als Einzelausgabe."
      ],
      [
        "67 daß man für dasjenige, was man unmittelbar als Arbeit leistet, einen der Arbeit entsp rechenden Lohn, der die Arbeit geradezu bezahlt, einheimsen müsse: Siehe Rudolf Steiner, «Geisteswissenschaft und soziale Frage», Drei Aufsätze, Berlin 1905/06, in «Luzifer-Gnosis 1903-1908», Biblio­graphie-Nr. 34, Gesamtausgabe Dornach 1960; auch als Einzelausgabe."
      ],
      [
        "70 . sein Werk... dem Papst gewidmet hat: Nikolaus Koper­nikus, 1473-1543.",
        "Sein schon viel früher ver er « e revolutioni-bus orbium coelestium libri VI», gewidmet Papst Paul III., gelangte erst 1543 in Nürnb erg zum Druck.",
        "Zunächst durch die Widmung an den Papst geschützt, kam das Werk jedoch 1615 auf den Index .Bei den Einschrän­kungen von 1757 wurde es nicht vom Index entfernt; erst 1822 wurde es gestrichen, als das Sacrum Officium erklärte, daß die Herausgabe von Werken, welche von der Bewegung der Erde und dem Stillstand der Sonne handeln, nicht verboten sei."
      ],
      [
        "seit dem Foucaultschen Pendelversuch: Der Physiker Léon Foucault, 1819 bis 1868, demonstrierte im Jahre 1851 im Panthéon zu Paris die Drehung der Erde durch ein freischwingendes Pendel."
      ],
      [
        "71 daß mir diese Erkenntnis von der Erdbewegung, als ich ein kleiner Bub war: Siehe «Mein Lebensgang».",
        "Bibliographie-Nr. 28, Gesamtausgabe Dorn-ach 1962."
      ],
      [
        "72 Die Erde . . . ist ein Staubkorn im Weltenall den anderen Welten gegen­über: Ein von Herbert Spencer, 1820-1903, geprägtes Wort."
      ],
      [
        "84 anthroposophische Bewegung - in unseren Gedanken wenigstens - scharf zu trennen von irgendeiner gesellschaftlichen Einrichtung: Einen dem Geist der anthroposophischen Bewegung entsprechenden Gesellschaftsorga­nismus zu bild en, war für Rudolf Steiner ein Hauptanliegen.",
        "Zu Weih­nachten 1923 versuchte er dies bei der Neubegründung der Allgemeinen Anthroposophischen Gesellschaft, indem er deren Vorsitz übernahm.",
        "Siehe Rudolf Steiner"
      ],
      [
        "Dornach 1963."
      ],
      [
        "86 daß es luziferische Kräfte und Wesenheiten gibt: Siehe Rudolf Steiner «Die Geheimwissenschaft im Umriß», Bibliographie-Nr. 13, Gesamtaus­gabe Dornach 1968."
      ],
      [
        "89 f.",
        "Lessings «Erziehung des Menschengeschlechts»: Erschienen 1780."
      ],
      [
        "90 im öffentlichen Vortrage: «Kopernikus und seine Zeit im Lichte der Geisteswissenschaft», Berlin, 15.",
        "Februar 1912, in «Menschengeschichte im Lichte der Geistesforschung», 16 Vorträge, 19.",
        "Oktober 1911 bis 28.",
        "März 1912.",
        "Bibliographie-Nr. 61, Gesamtausgabe Dornach 1962."
      ],
      [
        "98 So haben wir gesprochen über die Mission des Zornes, über das mensch­liche Gewissen, über das Gebet: Siehe Rudolf Steiner, «Metamorphosen"
      ],
      [
        "des Seelenlebens», 7 Vortrage, Berlin 1909/10, Bibliographie - Nr . 59, Ge­samtausgabe Dornach 1957, sowie «Pfade der Seelenerlehnisse», 8 Vor­träge, Berlin 1909/10, Bibliographie-Nr. 58, Gesamtausgabe Dornach 1957."
      ],
      [
        "99 Wenn Sie einen solchen Vortrag verfolgen wie den letzten öffentlichen:"
      ],
      [
        "«Der Tod bei Mensch, Tier und Pflanze», Vortrag vom 29.",
        "Februar 1912,"
      ],
      [
        "in «Menschengeschichte im Lichte der Geistesforschung», 16 Vorträge,"
      ],
      [
        "Berlin 1911/12, Bibliographie-Nr. 61, Gesamtausgabe Dornach 1962."
      ],
      [
        "102 Der Gegensatz zu uns . . .: Rudolf Steiner bezieht sich hier auf die da­malige Auseinandersetzung mit der Theosophischen Gesellschaft.",
        "Vgl.",
        "«Die Geschichte und die Bedingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesellschaft», Bibliographie-Nr. 258, Gesamtausgabe Dornach 1959."
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
